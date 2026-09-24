#!/usr/bin/env python3
"""
verifier.py — auto-diagnostic du kit Claude Code.

Lance-le à tout moment :  python3 outils/verifier.py   (ou python sur Windows)
Il ne modifie rien. Chaque ligne dit ✅ / ⚠️ / ❌ et, en cas d'échec, la commande
qui répare. Code de sortie : 0 si aucun ❌, 1 sinon.
"""
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

HOME = Path.home()
CLAUDE = HOME / ".claude"
SKILLS_ATTENDUS = ["porte", "lisible", "session-note", "bye", "to-do", "micom", "statusline-aide"]
HOOKS_ATTENDUS = ["kit_config.py", "obsidian_session_start.py", "obsidian_daily.py", "garde_fou.py"]

erreurs = 0


def ok(msg): print(f"  ✅ {msg}")
def warn(msg, fix=""): print(f"  ⚠️  {msg}" + (f"\n      → {fix}" if fix else ""))
def ko(msg, fix=""):
    global erreurs
    erreurs += 1
    print(f"  ❌ {msg}" + (f"\n      → {fix}" if fix else ""))


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20, shell=isinstance(cmd, str))
        return r.returncode, (r.stdout or r.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, str(e)


def titre(t): print(f"\n{t}")


def main() -> int:
    titre("Système")
    ok(f"{platform.system()} {platform.release()} · Python {platform.python_version()}")
    if platform.system() == "Windows":
        git_bash = shutil.which("bash") or Path("C:/Program Files/Git/bin/bash.exe").exists()
        if git_bash: ok("Git Bash trouvé (hooks et status line passeront par lui)")
        else: ko("Git Bash absent : les hooks et la status line ne tourneront pas",
                 "installer Git for Windows : https://git-scm.com/downloads/win")
        if not shutil.which("python3"):
            warn("`python3` absent, `python` présent", "dans settings.json, remplacer python3 par python")

    titre("Claude Code")
    if shutil.which("claude"):
        code, out = run(["claude", "--version"]); ok(out) if code == 0 else ko("claude --version échoue", out)
    else:
        ko("`claude` introuvable dans le PATH", "voir tuto/00_demarrer.md et tuto/11_pannes.md (PATH)")

    titre("Mémoire utilisateur")
    cm = CLAUDE / "CLAUDE.md"
    if cm.exists():
        t = cm.read_text(encoding="utf-8", errors="ignore")
        ok(f"~/.claude/CLAUDE.md ({len(t.splitlines())} lignes)")
        if "<" in t and ">" in t and "<Prénom" in t: warn("des trous <...> du modèle ne sont pas remplis")
    else:
        ko("~/.claude/CLAUDE.md absent", "copier modeles/CLAUDE.md.utilisateur et remplir les <...>")

    titre("Skills")
    for s in SKILLS_ATTENDUS:
        p = CLAUDE / "skills" / s / "SKILL.md"
        if p.exists(): ok(f"/{s}")
        else: ko(f"/{s} absent", f"cp -R skills/{s} ~/.claude/skills/")

    titre("Hooks")
    for h in HOOKS_ATTENDUS:
        p = CLAUDE / "hooks" / h
        if p.exists(): ok(h)
        else: ko(f"hooks/{h} absent", "cp hooks/*.py ~/.claude/hooks/")
    kit = CLAUDE / "kit.json"
    vault = None
    if kit.exists():
        try:
            vault = Path(json.loads(kit.read_text(encoding="utf-8"))["vault"]).expanduser()
            ok(f"kit.json → vault {vault}")
        except (ValueError, KeyError):
            ko("kit.json illisible ou sans clé vault", 'écrire {"vault": "/chemin/du/vault"}')
    else:
        ko("~/.claude/kit.json absent", 'écrire {"vault": "/chemin/du/vault"} dans ~/.claude/kit.json')

    settings = CLAUDE / "settings.json"
    hooks_cfg = {}
    if settings.exists():
        try:
            cfg = json.loads(settings.read_text(encoding="utf-8"))
            hooks_cfg = cfg.get("hooks", {})
            for ev, script in (("SessionStart", "obsidian_session_start"), ("Stop", "obsidian_daily"), ("PreToolUse", "garde_fou")):
                if script in json.dumps(hooks_cfg.get(ev, [])): ok(f"hook {ev} branché")
                else: ko(f"hook {ev} non branché", "fusionner hooks/hooks.json dans ~/.claude/settings.json")
            if cfg.get("disableAllHooks"): warn("disableAllHooks est à true : aucun hook ne tourne")
            sl = cfg.get("statusLine", {}).get("command", "")
            if "statusline.py" in sl: ok("statusLine → statusline.py")
            else: warn("statusLine ne pointe pas sur statusline.py", "voir modeles/settings.exemple.json")
        except ValueError as e:
            ko(f"settings.json invalide : {e}", "corriger le JSON (virgule en trop ?) puis `claude doctor`")
    else:
        ko("~/.claude/settings.json absent", "copier modeles/settings.exemple.json puis adapter")

    titre("Status line")
    slp = CLAUDE / "statusline.py"
    if slp.exists():
        code, out = run([sys.executable, str(slp), "--legende"])
        ok("statusline.py répond à --legende") if code == 0 else ko("statusline.py --legende échoue", out[:200])
    else:
        ko("~/.claude/statusline.py absent", "cp statusline/statusline.py ~/.claude/")

    titre("Hooks : exécution à blanc")
    for h, payload in (("obsidian_session_start.py", "{}"), ("garde_fou.py", '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}')):
        p = CLAUDE / "hooks" / h
        if not p.exists(): continue
        try:
            r = subprocess.run([sys.executable, str(p)], input=payload, capture_output=True, text=True, timeout=10)
        except (OSError, subprocess.TimeoutExpired) as e:
            ko(f"{h} : {e}"); continue
        if h == "garde_fou.py":
            ok("garde_fou refuse `rm -rf /` (exit 2)") if r.returncode == 2 else ko("garde_fou ne bloque pas `rm -rf /`", r.stderr[:200])
        else:
            ok("session_start renvoie du JSON") if r.returncode == 0 and r.stdout.strip().startswith("{") else ko("session_start ne renvoie pas de JSON", (r.stdout or r.stderr)[:200])

    titre("Vault Obsidian")
    if vault:
        if vault.exists():
            ok(f"vault présent")
            for d in ("03_Journal", "06_Claude/sessions", "02_Projets"):
                if (vault / d).is_dir(): ok(f"{d}/")
                else: warn(f"{d}/ manquant", f"mkdir -p \"{vault / d}\"")
        else:
            ko(f"vault absent : {vault}", "copier vault/ du kit à cet endroit, ou corriger kit.json")

    titre("Google (gws) — optionnel")
    if shutil.which("gws"):
        code, out = run(["gws", "auth", "status"])
        try:
            st = json.loads(out); resume = st.get("email") or st.get("account") or "authentifié"
        except ValueError:
            resume = (out.splitlines() or ["ok"])[0][:80]
        ok(f"gws : {resume}") if code == 0 else warn("gws installé mais pas authentifié", "gws auth login -s calendar,drive  (voir tuto/06_google.md)")
    else:
        warn("gws non installé (étape optionnelle)", "brew install googleworkspace-cli  ou  npm install -g @googleworkspace/cli")

    titre("Micom — optionnel")
    ch = CLAUDE / "micom" / "charte.md"
    if ch.exists():
        warn("charte présente mais des <...> restent à remplir") if "<" in ch.read_text(encoding="utf-8", errors="ignore") else ok("charte Micom remplie")
    else:
        warn("pas de charte Micom", "cp modeles/charte-micom.md ~/.claude/micom/charte.md puis remplir")

    print()
    if erreurs:
        print(f"{erreurs} point(s) ❌ à corriger. Relance ce script après.")
        return 1
    print("Tout est en place. Ouvre `claude` dans un projet et tape / pour voir tes skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
