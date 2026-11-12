#!/usr/bin/env python3
"""
vers_codex.py — fabrique la version Codex du kit à partir du kit Claude Code.

    python3 outils/vers_codex.py                 # régénère codex/skills, codex/hooks, modèles
    python3 outils/vers_codex.py --zip a.zip     # idem, puis le zip config-ovni-codex

Une seule source : le kit Claude. Les fichiers propres à Codex (AGENTS.md, tutos, modèles
TOML, verifier.py) sont écrits à la main dans codex/ ; ce script produit le reste.
Il s'arrête en erreur si une conversion laisse un reste propre à Claude Code.
"""
import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CODEX = RACINE / "codex"

SKILLS = ["porte", "lisible", "session-note", "bye", "to-do", "micom",
          "audit-acces", "souverainete-check", "animejs"]
# Exclus : fermer-sessions (sessions d'arrière-plan de Claude Code),
# statusline-aide (Codex n'accepte pas de status line par script).

# Phrases qui utilisent $ARGUMENTS : réécrites une par une (Codex n'a pas d'équivalent).
ARGUMENTS = [
    ("Si `$ARGUMENTS` est fourni, utilise-le comme titre court.",
     "Si l'utilisateur a écrit un titre après la mention du skill, utilise-le comme titre court."),
    ("Si\n   `$ARGUMENTS` est fourni, passe-le comme titre court.",
     "Si\n   l'utilisateur a écrit un titre après `$bye`, passe-le comme titre court."),
    ("Sujet : `$ARGUMENTS`", "Sujet : le texte écrit après `$micom` dans le message de l'utilisateur."),
    ("(outil Skill)", "(mentionne `$session-note`)"),
]


def convertir(texte: str) -> str:
    for avant, apres in ARGUMENTS:
        texte = texte.replace(avant, apres)
    texte = texte.replace("~/.claude/", "~/.codex/").replace('".claude"', '".codex"')
    texte = texte.replace("CLAUDE.md", "AGENTS.md")
    texte = texte.replace("outil: claude-code", "outil: codex")
    texte = texte.replace("Claude Code", "Codex")
    texte = re.sub(r"(?<![_/\w])Claude\b", "Codex", texte)
    for nom in SKILLS:  # appel d'un skill : /nom devient $nom
        texte = re.sub(rf'(?<![\w/.~-])/{re.escape(nom)}\b', f"${nom}", texte)
    return texte


def controler(nom: str, texte: str) -> None:
    restes = [m for m in ("$ARGUMENTS", "~/.claude", "!`", "settings.json") if m in texte]
    restes += re.findall(r"(?<![_/\w])Claude\b", texte)
    if restes:
        sys.exit(f"❌ {nom} : reste propre à Claude Code après conversion : {sorted(set(restes))}")


def entete(texte: str):
    """Sépare l'en-tête YAML du corps. Renvoie (lignes d'en-tête, corps)."""
    if not texte.startswith("---\n"):
        sys.exit("❌ SKILL.md sans en-tête")
    fin = texte.index("\n---\n", 4)
    return texte[4:fin].splitlines(), texte[fin + 5:]


def skill(nom: str) -> None:
    src, dst = RACINE / "skills" / nom, CODEX / "skills" / nom
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))
    lignes, corps = entete((src / "SKILL.md").read_text(encoding="utf-8"))
    garde = [l for l in lignes if l.startswith(("name:", "description:"))]
    if len(garde) != 2:
        sys.exit(f"❌ {nom} : name ou description absent, ou sur plusieurs lignes")
    explicite = any(l.replace(" ", "") == "disable-model-invocation:true" for l in lignes)
    sortie = convertir("---\n" + "\n".join(garde) + "\n---\n" + corps)
    controler(nom, sortie)
    (dst / "SKILL.md").write_text(sortie, encoding="utf-8")
    if explicite:  # équivalent Codex de disable-model-invocation: true
        (dst / "agents").mkdir(exist_ok=True)
        (dst / "agents" / "openai.yaml").write_text(
            "# Ce skill ne se lance que si l'utilisateur l'appelle ($" + nom + ").\n"
            "policy:\n  allow_implicit_invocation: false\n", encoding="utf-8")


def fichier(src: Path, dst: Path, extra=()) -> None:
    texte = src.read_text(encoding="utf-8")
    for avant, apres in extra:
        texte = texte.replace(avant, apres)
    texte = convertir(texte)
    controler(dst.name, texte)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(texte, encoding="utf-8")


def generer() -> None:
    for nom in SKILLS:
        skill(nom)
    for h in ("garde_fou.py", "kit_config.py", "obsidian_daily.py", "obsidian_session_start.py"):
        fichier(RACINE / "hooks" / h, CODEX / "hooks" / h)
    fichier(RACINE / "modeles" / "CLAUDE.md.utilisateur", CODEX / "modeles" / "AGENTS.md.utilisateur",
            extra=[("(doublé par un `deny` dans settings.json)",
                    "(doublé par une règle `forbidden` dans ~/.codex/rules/)")])
    fichier(RACINE / "modeles" / "charte-micom.md", CODEX / "modeles" / "charte-micom.md")
    fichier(RACINE / "tuto" / "05_obsidian.md", CODEX / "tuto" / "06_obsidian.md",
            extra=[("# 05 — Obsidian", "# 06 — Obsidian")])


def zipper(cible: Path) -> int:
    contenus = [(p, Path("config-ovni-codex") / p.relative_to(CODEX)) for p in CODEX.rglob("*")]
    contenus += [(p, Path("config-ovni-codex") / p.relative_to(RACINE)) for p in (RACINE / "vault").rglob("*")]
    contenus += [(RACINE / f, Path("config-ovni-codex") / f) for f in ("LICENSE", "NOTICE")]
    n = 0
    cible.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(cible, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arc in sorted(contenus, key=lambda c: str(c[1])):
            if src.is_file() and "__pycache__" not in src.parts and src.name != ".DS_Store":
                z.write(src, arc.as_posix())
                n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", type=Path, help="chemin du zip à produire")
    a = ap.parse_args()
    generer()
    print(f"✅ {len(SKILLS)} skills, 4 hooks, 3 fichiers convertis dans {CODEX}")
    if a.zip:
        print(f"✅ {zipper(a.zip)} fichiers dans {a.zip}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
