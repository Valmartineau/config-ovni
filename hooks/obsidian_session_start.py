#!/usr/bin/env python3
"""
Hook SessionStart : dit à Claude si la daily note du jour existe, et lui rappelle
d'archiver la session en fin de phase (skill session-note).

Entrée  : JSON sur stdin (ignoré ici).
Sortie  : JSON { hookSpecificOutput: { additionalContext } } — exit 0.
Test    : echo '{}' | python3 obsidian_session_start.py
"""
import json
import sys
from datetime import date

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from kit_config import vault_path  # noqa: E402


def main() -> int:
    vault = vault_path()
    today = date.today().isoformat()
    daily = vault / "03_Journal" / f"{today}.md"

    if not vault.exists():
        etat = f"OBSIDIAN ABSENT : le vault {vault} n'existe pas (voir ~/.claude/kit.json)."
    elif daily.exists():
        etat = "OBSIDIAN ACTIF : la daily note du jour existe."
    else:
        etat = "OBSIDIAN ACTIF : pas encore de daily note aujourd'hui."

    consigne = (
        " AUTONOMIE VAULT : à chaque fin de phase de travail (merge, livraison, "
        "décision actée, clôture), mettre à jour SANS demander la note de session "
        "du jour dans 06_Claude/sessions/ au format du skill session-note "
        "(statut en_cours, UNE seule note par session ; la finaliser statut termine "
        f"en fin de session). Vault : {vault}"
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": etat + consigne,
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
