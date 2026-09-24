"""Lecture de ~/.claude/kit.json (chemin du vault). Partagé par les hooks du kit."""
import json
from pathlib import Path

CONFIG = Path.home() / ".claude" / "kit.json"
DEFAULT_VAULT = Path.home() / "Documents" / "Vault"


def vault_path() -> Path:
    try:
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
        return Path(data["vault"]).expanduser()
    except (OSError, ValueError, KeyError):
        return DEFAULT_VAULT
