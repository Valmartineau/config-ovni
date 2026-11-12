#!/usr/bin/env python3
"""Test sans framework de la version Codex : python3 outils/test_vers_codex.py"""
import json
import os
import subprocess
import sys
import tempfile
import tomllib
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CODEX = RACINE / "codex"
PY = sys.executable


def lancer(script, entree, home):
    env = {**os.environ, "HOME": str(home)}
    return subprocess.run([PY, str(script)], input=entree, capture_output=True, text=True, env=env, timeout=20)


with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    zp = tmp / "kit.zip"
    r = subprocess.run([PY, str(RACINE / "outils" / "vers_codex.py"), "--zip", str(zp)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr

    # Skills : en-tête réduit à name + description, appel explicite dans openai.yaml.
    noms = sorted(p.name for p in (CODEX / "skills").iterdir())
    assert len(noms) == 9 and "fermer-sessions" not in noms and "statusline-aide" not in noms, noms
    for n in noms:
        t = (CODEX / "skills" / n / "SKILL.md").read_text(encoding="utf-8")
        tete = t.split("\n---\n", 1)[0].splitlines()[1:]
        assert [l.split(":")[0] for l in tete] == ["name", "description"], (n, tete)
        assert "$ARGUMENTS" not in t and "~/.claude" not in t, n
    for n in ("porte", "bye", "micom", "lisible"):
        y = (CODEX / "skills" / n / "agents" / "openai.yaml").read_text(encoding="utf-8")
        assert "allow_implicit_invocation: false" in y, n
    assert not (CODEX / "skills" / "to-do" / "agents").exists()

    # Hooks, avec des entrées au format Codex (champs communs + champs de l'événement).
    home = tmp / "home"
    (home / ".codex").mkdir(parents=True)
    vault = tmp / "vault"
    (home / ".codex" / "kit.json").write_text(json.dumps({"vault": str(vault)}))
    commun = {"session_id": "s", "transcript_path": None, "cwd": str(tmp), "model": "m", "turn_id": "t"}
    h = CODEX / "hooks"
    def pre(cmd):
        return json.dumps({**commun, "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": cmd}})
    assert lancer(h / "garde_fou.py", pre("rm -rf /"), home).returncode == 2
    assert lancer(h / "garde_fou.py", pre("git push --force origin main"), home).returncode == 2
    assert lancer(h / "garde_fou.py", pre("ls -la"), home).returncode == 0
    r = lancer(h / "obsidian_session_start.py", json.dumps({**commun, "hook_event_name": "SessionStart", "source": "startup"}), home)
    sortie = json.loads(r.stdout)
    assert r.returncode == 0 and "~/.codex/kit.json" in sortie["hookSpecificOutput"]["additionalContext"], r.stdout
    vault.mkdir()
    r = lancer(h / "obsidian_daily.py", json.dumps({**commun, "hook_event_name": "Stop", "stop_hook_active": False}), home)
    assert r.returncode == 0 and json.loads(r.stdout), r.stdout  # Codex exige du JSON sur un Stop
    daily = next((vault / "03_Journal").glob("*.md")).read_text(encoding="utf-8")
    assert "— Codex" in daily and "Claude" not in daily, daily

    # Fichiers de réglages lisibles par un programme.
    tomllib.loads((CODEX / "modeles" / "config.exemple.toml").read_text(encoding="utf-8"))
    agent = tomllib.loads((CODEX / "agents" / "relecteur.toml").read_text(encoding="utf-8"))
    assert {"name", "description", "developer_instructions"} <= agent.keys()
    hooks = json.loads((CODEX / "modeles" / "hooks.json").read_text(encoding="utf-8"))["hooks"]
    assert set(hooks) == {"SessionStart", "Stop", "PreToolUse"}

    # Le zip : un dossier racine, le pilote, le vault, la licence, rien de Claude.
    with zipfile.ZipFile(zp) as z:
        noms_zip = z.namelist()
    assert all(n.startswith("config-ovni-codex/") for n in noms_zip)
    for attendu in ("AGENTS.md", "INVENTAIRE.md", "LICENSE", "NOTICE", "tuto/00_installer-codex.md",
                    "vault/00_Accueil.md", "skills/lisible/LICENSE", "outils/verifier.py"):
        assert f"config-ovni-codex/{attendu}" in noms_zip, attendu
    assert not any("__pycache__" in n or "CLAUDE.md" in n or "settings" in n for n in noms_zip)

    # L'auto-diagnostic tourne sur une machine vide sans planter (code 1 attendu : rien d'installé).
    r = lancer(CODEX / "outils" / "verifier.py", "", tmp / "vide")
    assert r.returncode == 1 and "Traceback" not in r.stderr, r.stderr
    print(f"✅ test_vers_codex : 9 skills, 3 hooks exercés, réglages relus, zip de {len(noms_zip)} fichiers")
