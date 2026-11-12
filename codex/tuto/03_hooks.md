# 03 — Hooks : les automatismes que l'agent ne peut pas oublier

Un hook est une commande que **Codex** lance sur un événement : début de session,
avant une commande, fin de tour. Le modèle ne décide pas : le programme exécute.

Bonne nouvelle : Codex parle le **même langage** que Claude Code. Le script reçoit
un JSON sur son entrée, et le code de sortie **2** bloque l'action. Les trois hooks
du kit tournent presque sans retouche.

## Les trois hooks du kit

| Hook | Événement | Ce qu'il fait |
|---|---|---|
| `garde_fou.py` | `PreToolUse`, outil `Bash` | Refuse `rm -rf /`, `rm -rf ~`, push forcé sur main, écriture disque |
| `obsidian_session_start.py` | `SessionStart` | Dit si la note du jour existe, rappelle d'archiver la session |
| `obsidian_daily.py` | `Stop` | Ajoute une ligne « Codex » dans la note du jour (une par heure) |

## Installer

```bash
mkdir -p ~/.codex/hooks
cp hooks/*.py ~/.codex/hooks/
echo '{"vault": "/chemin/de/votre/vault"}' > ~/.codex/kit.json
cp modeles/hooks.json ~/.codex/hooks.json
```

Dans `~/.codex/hooks.json`, remplacez `~` par le chemin complet de votre dossier
personnel (`/Users/vous` ou `/home/vous`). Sur Windows : `python` au lieu de `python3`.

## Tester à la main, avant de faire confiance

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}' | python3 ~/.codex/hooks/garde_fou.py ; echo $?
```

Le refus s'affiche, puis `2`. Une commande banale (`ls`) doit donner `0`.

## Approuver

Ouvrez une nouvelle session et tapez `/hooks`. Codex **refuse de lancer un hook
que vous n'avez pas relu et approuvé**. Lisez chaque script avant d'accepter.

## Différences avec Claude Code

- Les hooks vont dans `~/.codex/hooks.json` (ou une table `[hooks]` de `config.toml`),
  pas dans `settings.json`.
- `apply_patch` (l'outil qui modifie les fichiers) est un événement à part :
  le garde-fou du kit ne le surveille pas.
- Couper tous les hooks : `[features] hooks = false` dans `~/.codex/config.toml`.

## Doublez le garde-fou par une règle

Codex a aussi des **règles de commandes** (`.rules`), lues par le programme
lui-même : voir `tuto/04_mcp-regles.md`.

## Réussi si

Le test affiche le refus et `2`, `/hooks` liste les trois, et la note du jour
reçoit une ligne « Codex » après un échange.

## Retirer

Supprimez `~/.codex/hooks.json` et `~/.codex/hooks/`.
