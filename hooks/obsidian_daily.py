#!/usr/bin/env python3
"""
Hook Stop : trace la session Claude Code dans la daily note Obsidian du jour.

Anti-spam : une seule ligne par heure. Si une ligne existe déjà pour l'heure en
cours, son compteur est incrémenté au lieu d'en créer une nouvelle.

Entrée  : JSON sur stdin (ignoré).
Sortie  : exit 0 toujours (un hook Stop ne doit jamais bloquer).
Test    : echo '{}' | python3 obsidian_daily.py
"""
import json
import re
import sys
from datetime import datetime

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from kit_config import vault_path  # noqa: E402

TEMPLATE = """---
type: journal
date: "{date}"
tags: [journal]
---

# {date_long}

## Priorités du jour
- [ ]

## Sessions Claude Code

{session_entry}

## Notes & réflexions


"""


JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]


def date_longue(d: datetime) -> str:
    """« mardi 22 septembre 2026 », quelle que soit la locale du système."""
    return f"{JOURS[d.weekday()]} {d.day} {MOIS[d.month - 1]} {d.year}"


def session_line(hour_key: str, count: int = 1) -> str:
    suffix = f" ({count} sessions)" if count > 1 else ""
    return f"- **{hour_key}** — Claude Code{suffix}"


def update_or_add(content: str, hour_key: str) -> str:
    pattern = re.compile(
        rf"- \*\*{re.escape(hour_key)}\*\* — Claude Code(?:\s*\((\d+) sessions\))?"
    )
    m = pattern.search(content)
    if m:
        count = int(m.group(1)) if m.group(1) else 1
        return pattern.sub(session_line(hour_key, count + 1), content)
    line = session_line(hour_key)
    if "## Notes & réflexions" in content:
        return content.replace("## Notes & réflexions", f"{line}\n\n## Notes & réflexions")
    return content.rstrip("\n") + f"\n{line}\n"


def main() -> int:
    try:
        now = datetime.now()
        journal = vault_path() / "03_Journal"
        note = journal / f"{now:%Y-%m-%d}.md"
        hour_key = now.strftime("%H:00")
        if note.exists():
            content = update_or_add(note.read_text(encoding="utf-8"), hour_key)
        else:
            journal.mkdir(parents=True, exist_ok=True)
            content = TEMPLATE.format(
                date=f"{now:%Y-%m-%d}",
                date_long=date_longue(now),
                session_entry=session_line(hour_key),
            )
        note.write_text(content, encoding="utf-8")
        print(json.dumps({"systemMessage": f"Journal Obsidian : {note.name}"}))
    except Exception as e:  # jamais bloquer un Stop
        print(json.dumps({"systemMessage": f"Journal Obsidian : erreur {e}"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
