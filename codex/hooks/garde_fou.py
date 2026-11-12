#!/usr/bin/env python3
"""
Hook PreToolUse (matcher Bash) : refuse les commandes destructrices évidentes.

C'est l'exemple pédagogique d'un hook QUI BLOQUE : exit 2 + raison sur stderr.
Un hook async ne peut pas bloquer : celui-ci doit rester synchrone.

Entrée  : JSON { tool_name, tool_input: { command } } sur stdin.
Sortie  : exit 0 (laisser passer) ou exit 2 (bloquer, raison sur stderr).
Test    : echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}' | python3 garde_fou.py ; echo $?
"""
import json
import re
import sys

# ponytail: liste courte et lisible. Plafond : un motif contourné par une variable
# ($HOME) ou un alias passe. Upgrade : analyser la commande avec shlex, ou refuser
# tout `rm -rf` hors du dossier de projet.
MOTIFS = [
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+/(\s|$)", "rm récursif sur la racine"),
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+~/?(\s|$)", "rm récursif sur le home"),
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+\$HOME/?(\s|$)", "rm récursif sur le home"),
    (r"\bgit\s+push\b.*(--force|-f)\b.*\b(main|master)\b", "push forcé sur main/master"),
    (r"\bgit\s+push\b.*\b(main|master)\b.*(--force|-f)\b", "push forcé sur main/master"),
    (r"\bmkfs\b|\bdd\s+if=.*of=/dev/", "écriture bas niveau sur un disque"),
]


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    if data.get("tool_name") != "Bash":
        return 0
    cmd = str(data.get("tool_input", {}).get("command", ""))
    for motif, raison in MOTIFS:
        if re.search(motif, cmd):
            print(f"Garde-fou : commande refusée ({raison}). "
                  f"Si c'est voulu, l'utilisateur la lance lui-même.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
