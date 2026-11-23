# Config OVNI pour Codex — pour démarrer

La configuration OVNI, version **Codex** (l'agent de code d'OpenAI) : méthode de
travail, skills, hooks, règles, vault Obsidian. Même esprit que le kit Claude Code,
sans aucune donnée personnelle.

## En 3 gestes

1. Pas encore Codex ? Suivez `tuto/00_installer-codex.md`.
2. Dézippez le kit, ouvrez un terminal **dans le dossier du kit**, lancez `codex`.
3. Écrivez « installe le kit ». Codex lit `AGENTS.md` et vous guide, une étape à la fois.

## Ce qu'il y a dedans

| Dossier | Contenu |
|---|---|
| `AGENTS.md` | Le guide d'installation **que Codex exécute** avec vous |
| `INVENTAIRE.md` | Ce qui passe tel quel, ce qui est adapté, ce qui ne passe pas |
| `tuto/` | Installer Codex, AGENTS.md, skills, hooks, réglages et MCP, sous-agents, Obsidian |
| `outils/verifier.py` | L'auto-diagnostic : ✅ / ❌ et la commande qui répare |
| `skills/` | 10 skills, à copier dans `~/.agents/skills/` |
| `hooks/` | 3 hooks Python, à copier dans `~/.codex/hooks/` |
| `agents/` | Le sous-agent relecteur, au format TOML |
| `modeles/` | AGENTS.md personnel, `config.toml` commenté, `hooks.json`, règles, charte Micom |
| `vault/` | Squelette d'un vault Obsidian |

**En cas de doute :** `python3 outils/verifier.py`.

## Vous utilisez aussi Claude Code ?

Les deux kits cohabitent : l'un vit dans `~/.claude/`, l'autre dans `~/.codex/`
et `~/.agents/skills/`. Le même vault Obsidian sert aux deux.

## Trois principes qui tiennent tout

- **Comprendre avant d'automatiser.** Chaque hook, chaque skill, vous l'avez lu
  et testé à la main avant de le laisser tourner seul.
- **Rien ne sort sans votre accord.** Mail, push, publication : votre geste.
- **État visible = état réel.** Ce qui n'est pas vérifié est marqué « en cours ».

Licence : CC BY-NC 4.0, comme le kit Claude Code (le skill `lisible` reste sous MIT).
Détails : `LICENSE` et `NOTICE`. Source : https://github.com/Valmartineau/config-ovni
