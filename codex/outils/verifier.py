#!/usr/bin/env python3
"""
verifier.py — auto-diagnostic de la Config OVNI pour Codex.

Lance-le à tout moment :  python3 outils/verifier.py   (ou python sur Windows)
Il ne modifie rien. Chaque ligne dit ✅ / ⚠️ / ❌ et, en cas d'échec, la commande
qui répare. Code de sortie : 0 si aucun ❌, 1 sinon.
"""
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

HOME = Path.home()
CODEX = HOME / ".codex"
SKILLS_DIR = HOME / ".agents" / "skills"
SKILLS_ATTENDUS = ["porte", "lisible", "session-note", "bye", "to-do", "micom",
                   "audit-acces", "souverainete-check", "animejs", "boussole"]
HOOKS_ATTENDUS = ["kit_config.py", "obsidian_session_start.py", "obsidian_daily.py", "garde_fou.py"]

erreurs = 0


def ok(msg): print(f"  ✅ {msg}")
def warn(msg, fix=""): print(f"  ⚠️  {msg}" + (f"\n      → {fix}" if fix else ""))
def ko(msg, fix=""):
    global erreurs
    erreurs += 1
    print(f"  ❌ {msg}" + (f"\n      → {fix}" if fix else ""))


def titre(t): print(f"\n{t}")


def lancer(cmd, entree=None):
    try:
        r = subprocess.run(cmd, input=entree, capture_output=True, text=True, timeout=20)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, "", str(e)


def main() -> int:
    titre("Système")
    ok(f"{platform.system()} {platform.release()} · Python {platform.python_version()}")
    if shutil.which("git"): ok("git présent")
    else: ko("git absent", "Mac : lancer `git` et accepter les outils ; Windows : https://git-scm.com/downloads/win")

    titre("Codex")
    if shutil.which("codex"):
        code, out, err = lancer(["codex", "--version"])
        ok(out) if code == 0 else ko("codex --version échoue", err[:200])
    else:
        ko("`codex` introuvable", "voir tuto/00_installer-codex.md, puis fermer et rouvrir le terminal")

    titre("Consignes personnelles")
    am = CODEX / "AGENTS.md"
    if am.exists():
        t = am.read_text(encoding="utf-8", errors="ignore")
        ok(f"~/.codex/AGENTS.md ({len(t.encode())} octets sur 32 768 lus)")
        if "<Prénom" in t: warn("des trous <...> du modèle ne sont pas remplis")
        if len(t.encode()) > 32768: ko("AGENTS.md dépasse 32 Ko : la fin est ignorée", "raccourcir")
    else:
        ko("~/.codex/AGENTS.md absent", "copier modeles/AGENTS.md.utilisateur et remplir les <...>")

    titre("Skills (~/.agents/skills)")
    for s in SKILLS_ATTENDUS:
        if (SKILLS_DIR / s / "SKILL.md").exists(): ok(f"${s}")
        else: ko(f"${s} absent", f"mkdir -p ~/.agents/skills && cp -R skills/{s} ~/.agents/skills/")
    if (CODEX / "skills").is_dir():
        warn("~/.codex/skills existe : Codex lit ~/.agents/skills", "déplacer vos skills dans ~/.agents/skills")

    titre("Hooks")
    for h in HOOKS_ATTENDUS:
        if (CODEX / "hooks" / h).exists(): ok(h)
        else: ko(f"hooks/{h} absent", "mkdir -p ~/.codex/hooks && cp hooks/*.py ~/.codex/hooks/")
    vault = None
    kit = CODEX / "kit.json"
    if kit.exists():
        try:
            vault = Path(json.loads(kit.read_text(encoding="utf-8"))["vault"]).expanduser()
            ok(f"kit.json → vault {vault}")
        except (ValueError, KeyError):
            ko("kit.json illisible ou sans clé vault", 'écrire {"vault": "/chemin/du/vault"}')
    else:
        ko("~/.codex/kit.json absent", 'écrire {"vault": "/chemin/du/vault"} dans ~/.codex/kit.json')
    hj = CODEX / "hooks.json"
    if hj.exists():
        try:
            cfg = json.loads(hj.read_text(encoding="utf-8")).get("hooks", {})
            for ev, script in (("SessionStart", "obsidian_session_start"), ("Stop", "obsidian_daily"), ("PreToolUse", "garde_fou")):
                brut = json.dumps(cfg.get(ev, []))
                if script not in brut: ko(f"hook {ev} non branché", "copier ou fusionner modeles/hooks.json")
                elif "~/" in brut: warn(f"hook {ev} : chemin avec ~", "écrire le chemin complet du dossier personnel")
                else: ok(f"hook {ev} branché")
        except ValueError as e:
            ko(f"hooks.json invalide : {e}", "corriger le JSON (virgule en trop ?)")
    else:
        ko("~/.codex/hooks.json absent", "cp modeles/hooks.json ~/.codex/hooks.json puis remplacer ~ par le chemin complet")
    print("      (Codex lance un hook seulement après votre accord dans /hooks)")

    titre("Hooks : exécution à blanc")
    essais = (("garde_fou.py", '{"hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"rm -rf /"}}', 2),
              ("garde_fou.py", '{"hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"ls"}}', 0),
              ("obsidian_session_start.py", '{"hook_event_name":"SessionStart"}', 0))
    for h, payload, attendu in essais:
        p = CODEX / "hooks" / h
        if not p.exists(): continue
        code, out, err = lancer([sys.executable, str(p)], payload)
        if code != attendu: ko(f"{h} : code {code}, attendu {attendu}", err[:200])
        elif h == "obsidian_session_start.py" and not out.startswith("{"): ko("session_start ne renvoie pas de JSON", out[:200])
        else: ok(f"{h} → code {code} comme attendu")

    titre("Réglages (~/.codex/config.toml)")
    ct = CODEX / "config.toml"
    if ct.exists():
        try:
            import tomllib
            cfg = tomllib.loads(ct.read_text(encoding="utf-8"))
            ok(f"config.toml lisible · approval_policy={cfg.get('approval_policy', 'défaut')} · sandbox_mode={cfg.get('sandbox_mode', 'défaut')}")
            if cfg.get("features", {}).get("hooks") is False: warn("[features] hooks = false : aucun hook ne tourne")
            if cfg.get("approval_policy") == "never" and cfg.get("sandbox_mode") == "danger-full-access":
                warn("never + danger-full-access : Codex peut tout faire sans demander")
        except ImportError:
            warn("Python < 3.11 : config.toml non relu")
        except ValueError as e:
            ko(f"config.toml invalide : {e}", "corriger la ligne indiquée")
    else:
        warn("pas de ~/.codex/config.toml (Codex prend ses valeurs par défaut)", "voir modeles/config.exemple.toml")
    regles = list((CODEX / "rules").glob("*.rules")) if (CODEX / "rules").is_dir() else []
    if regles: ok(f"{len(regles)} fichier(s) de règles de commandes")
    else: warn("aucune règle de commandes", "cp modeles/rules/garde-fou.rules ~/.codex/rules/  (optionnel)")

    titre("Sous-agent — optionnel")
    if (CODEX / "agents" / "relecteur.toml").exists(): ok("relecteur.toml")
    else: warn("relecteur absent", "mkdir -p ~/.codex/agents && cp agents/relecteur.toml ~/.codex/agents/")

    titre("Vault Obsidian")
    if vault:
        if vault.exists():
            ok("vault présent")
            for d in ("03_Journal", "06_Claude/sessions", "02_Projets"):
                if (vault / d).is_dir(): ok(f"{d}/")
                else: warn(f"{d}/ manquant", f"mkdir -p \"{vault / d}\"")
        else:
            ko(f"vault absent : {vault}", "copier vault/ du kit à cet endroit, ou corriger kit.json")

    titre("Micom — optionnel")
    ch = CODEX / "micom" / "charte.md"
    if ch.exists():
        warn("charte présente mais des <...> restent à remplir") if "<" in ch.read_text(encoding="utf-8", errors="ignore") else ok("charte Micom remplie")
    else:
        warn("pas de charte Micom", "mkdir -p ~/.codex/micom && cp modeles/charte-micom.md ~/.codex/micom/charte.md")

    print()
    if erreurs:
        print(f"{erreurs} point(s) ❌ à corriger. Relance ce script après.")
        return 1
    print("Tout est en place. Ouvre `codex` dans un projet et tape /skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
