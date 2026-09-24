#!/usr/bin/env python3
"""
Status line Claude Code — une ligne, libellés en toutes lettres.

  ~/projet main │ Opus 5 (1M) │ contexte ██░░░░░░ 19% │ quota 5h 58% (reste 3h24)
    · quota 7j 42% (reste 6j) │ ouvert 15h08, depuis 1h17 │ notes du jour 2 / 57 au total

Entrée  : JSON sur stdin (champs : model.display_name, workspace.current_dir,
          context_window.used_percentage, rate_limits.five_hour/seven_day
          {used_percentage, resets_at}, transcript_path).
`--legende` : affiche la traduction de chaque segment au lieu de lire stdin.
Portable : Python 3.8+, macOS / Linux / Windows (Git Bash ou PowerShell).
Test    : echo '{"model":{"display_name":"Test"},"workspace":{"current_dir":"/tmp"},"context_window":{"used_percentage":25}}' | python3 statusline.py
"""
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude" / "hooks"))
try:
    from kit_config import vault_path
except ImportError:  # kit non installé : pas de compteur de notes
    vault_path = None

BAR_CELLS = 8
RST, DIM, BOLD = "\033[0m", "\033[2m", "\033[1m"
C_MODEL, C_PATH, C_GIT, C_META, C_NOTE = (
    "\033[38;5;141m", "\033[38;5;110m", "\033[38;5;180m", "\033[38;5;245m", "\033[38;5;79m")


def tint(pct: int) -> str:
    if pct >= 90: return "\033[38;5;203m"
    if pct >= 75: return "\033[38;5;215m"
    if pct >= 50: return "\033[38;5;222m"
    return "\033[38;5;114m"


def bar(pct: int) -> str:
    filled = max(0, min(BAR_CELLS, (pct * BAR_CELLS + 50) // 100))
    return "█" * filled + "░" * (BAR_CELLS - filled)


def dur(s: int) -> str:
    s = max(0, s)
    d, h, m = s // 86400, (s % 86400) // 3600, (s % 3600) // 60
    if d and h: return f"{d}j{h:02d}"
    if d: return f"{d}j"
    if h: return f"{h}h{m:02d}"
    return f"{m}min"


def legende() -> None:
    print(f"{BOLD}Status line — que veut dire chaque segment{RST}\n")
    print(f"  {DIM}~/projet main │ Opus 5 (1M) │ contexte ██░░░░░░ 19% │ quota 5h 58% (reste 3h24) · quota 7j 42% (reste 6j) │ ouvert 15h08, depuis 1h17 │ notes du jour 2 / 57 au total{RST}\n")
    rows = [
        (C_PATH, "~/projet", "répertoire de travail (deux derniers niveaux au-delà de deux)"),
        (C_GIT, "main", "branche git, lue dans .git/HEAD — absente hors dépôt"),
        (C_MODEL, "Opus 5 (1M)", "modèle actif et taille de sa fenêtre de contexte"),
        (tint(19), "contexte [jauge] 19%", "part de la fenêtre déjà occupée par la conversation"),
        (tint(58), "quota 5h 58%", "consommation de ton forfait sur la fenêtre glissante de 5 h"),
        (DIM, "(reste 3h24)", "temps avant la remise à zéro de ce quota"),
        (tint(42), "quota 7j 42%", "même chose sur la fenêtre glissante de 7 jours"),
        (C_META, "ouvert 15h08", "heure d'ouverture réelle de la session"),
        (DIM, "depuis 1h17", "temps écoulé depuis cette ouverture"),
        (C_NOTE, "notes du jour 2", "notes de session écrites aujourd'hui dans le vault"),
        (DIM, "57 au total", "total des notes dans 06_Claude/sessions/"),
    ]
    for c, k, v in rows:
        print(f"  {c}{k:<22}{RST} {v}")
    print(f"\n  {BOLD}Couleur des pourcentages{RST}")
    print(f"  {tint(0)}vert{RST} < 50%   {tint(50)}jaune{RST} < 75%   {tint(75)}orange{RST} < 90%   {tint(90)}rouge{RST} au-delà")
    print(f"\n  {DIM}Le segment « quota » disparaît si ton offre ne renvoie pas ces compteurs.{RST}")


def pct(v) -> int:
    try:
        return int(round(float(v)))
    except (TypeError, ValueError):
        return -1


def git_branch(cwd: str) -> str:
    p = Path(cwd) if cwd else None
    while p and p != p.parent:
        g = p / ".git"
        if g.exists():
            gitdir = g
            if g.is_file():  # worktree : "gitdir: <chemin>"
                target = g.read_text(encoding="utf-8").split(":", 1)[-1].strip()
                gitdir = Path(target) if os.path.isabs(target) else p / target
            head = gitdir / "HEAD"
            if head.is_file():
                h = head.read_text(encoding="utf-8").strip()
                return h.rsplit("/", 1)[-1] if h.startswith("ref:") else h[:7]
            return ""
        p = p.parent
    return ""


def short_dir(cwd: str) -> str:
    home = str(Path.home())
    s = cwd or ""
    if s == home: s = "~"
    elif s.startswith(home + os.sep): s = "~" + s[len(home):]
    s = s.replace("\\", "/")
    parts = s.split("/")
    if len(parts) > 3:
        s = "…/" + "/".join(parts[-2:])
    return s


def session_start(transcript: str):
    try:
        with open(transcript, encoding="utf-8", errors="ignore") as f:
            for line in f:
                m = re.search(r'"timestamp":"([^"]+)"', line)
                if m:
                    t = m.group(1).split(".")[0].rstrip("Z")
                    return datetime.strptime(t, "%Y-%m-%dT%H:%M:%S").replace(
                        tzinfo=__import__("datetime").timezone.utc).timestamp()
        return os.path.getctime(transcript)
    except (OSError, ValueError):
        return None


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] in ("--legende", "--aide", "-h"):
        legende()
        return 0
    try:
        data = json.load(sys.stdin)
    except ValueError:
        data = {}
    ws = data.get("workspace") or {}
    cwd = ws.get("current_dir") or data.get("cwd") or ""
    model = (data.get("model") or {}).get("display_name") or "?"
    model = model.replace("(1M context)", "(1M)")
    ctx = pct((data.get("context_window") or {}).get("used_percentage"))
    rl = data.get("rate_limits") or {}
    h5, d7 = rl.get("five_hour") or {}, rl.get("seven_day") or {}
    now = int(time.time())
    sep = f"{DIM} │ {RST}"

    out = f"{C_PATH}{short_dir(cwd)}{RST}"
    b = git_branch(cwd)
    if b: out += f" {C_GIT}{b}{RST}"
    out += f"{sep}{C_MODEL}{model}{RST}"

    if ctx >= 0:
        c = tint(ctx)
        out += f"{sep}{DIM}contexte{RST} {c}{bar(ctx)}{RST} {c}{BOLD}{ctx}%{RST}"
    else:
        out += f"{sep}{DIM}contexte inconnu{RST}"

    quota = []
    for label, q in (("quota 5h", h5), ("quota 7j", d7)):
        p = pct(q.get("used_percentage"))
        if p < 0: continue
        s = f"{DIM}{label}{RST} {tint(p)}{p}%{RST}"
        at = pct(q.get("resets_at"))
        if at > now: s += f" {DIM}(reste {dur(at - now)}){RST}"
        quota.append(s)
    if quota: out += sep + f" {DIM}·{RST} ".join(quota)

    tr = data.get("transcript_path")
    if tr and os.path.isfile(tr):
        st = session_start(tr)
        if st:
            out += f"{sep}{C_META}ouvert {datetime.fromtimestamp(st):%Hh%M}{RST}{DIM}, depuis {dur(now - int(st))}{RST}"

    if vault_path:
        notes = vault_path() / "06_Claude" / "sessions"
        if notes.is_dir():
            allnotes = list(notes.glob("*.md"))
            today = [n for n in allnotes if n.name.startswith(datetime.now().strftime("%Y-%m-%d"))]
            out += f"{sep}{DIM}notes du jour{RST} {C_NOTE}{len(today)}{RST} {DIM}/ {len(allnotes)} au total{RST}"

    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
