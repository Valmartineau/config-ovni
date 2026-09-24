# 15 — `claude -p` : Claude sans interface, dans un script

## L'idée

`-p` (ou `--print`) lance Claude Code **sans interface** : il lit le prompt, travaille,
imprime le résultat, et sort. C'est ce qui permet de mettre Claude dans un script,
un `Makefile`, un cron, un hook git.

```bash
claude -p "Que fait le module auth ?"
cat erreur.log | claude -p "explique la cause racine en trois lignes"
```

Code de sortie 0 si tout va bien, non nul sinon : un script peut brancher dessus.

## Les options qui comptent

| Option | Rôle |
|---|---|
| `--output-format json` | résultat structuré : `result`, `session_id`, coût, nombre de tours |
| `--json-schema '{…}'` | sortie contrainte à un schéma JSON (`structured_output`) |
| `--allowedTools "Read,Bash(git diff *)"` | outils pré-autorisés ; sans ça, tout ce qui demanderait une permission est refusé |
| `--permission-mode acceptEdits` | ou `plan`, `auto`, `dontAsk` |
| `--max-turns 5` | plafond de tours |
| `--append-system-prompt "…"` | ajoute un rôle sans perdre le comportement de base |
| `--continue`, `--resume <id>` | reprendre une conversation |
| `--strict-mcp-config` | n'utiliser **que** les MCP passés en ligne de commande |
| `--bare` | ne charge **rien** de `~/.claude` ni du projet : ni hooks, ni skills, ni CLAUDE.md, ni mémoire. Pour un résultat identique sur toute machine. Demande une clé API (`ANTHROPIC_API_KEY`), pas votre connexion |

Un skill s'invoque dans le prompt : `claude -p "/session-note bilan du jour"`.

## Lire le résultat

```bash
claude -p "Résume ce projet" --output-format json | jq -r '.result'
id=$(claude -p "Commence une revue" --output-format json | jq -r '.session_id')
claude -p "Continue sur les requêtes SQL" --resume "$id"
```

## Trois usages concrets

**Un linter maison** (dans `package.json`) :
```json
"lint:claude": "git diff main | claude -p \"tu es un correcteur de fautes. Pour chaque faute : fichier:ligne puis le problème. Rien d'autre.\""
```

**Une revue de PR** (`review.sh`) :
```bash
gh pr diff "$1" | claude -p --append-system-prompt "Tu es relecteur sécurité." --output-format json
```

**Une tâche de nuit** (cron ou launchd) :
```bash
0 2 * * *  cd ~/projets/x && claude -p "/to-do-nuit" --strict-mcp-config --permission-mode acceptEdits --max-turns 30 >> ~/journal-nuit.log 2>&1
```

## Les trois portes à fermer avant d'automatiser

1. **Les MCP** : `--strict-mcp-config`. Sans lui, un `-p` connecte tous vos serveurs MCP,
   y compris ceux d'un projet que vous n'avez jamais approuvé.
2. **Les permissions** : listez les outils avec `--allowedTools`, ne passez pas en
   `bypassPermissions` par confort.
3. **Le périmètre** : une tâche de nuit s'exécute dans un dossier précis, sur une
   branche précise, jamais sur `main`. Voir le skill `/porte` : c'est le même principe.

Piège vécu : `--settings '{…}'` **fusionne** avec votre `settings.json`, il ne le
remplace pas. Vos hooks tournent quand même. Pour un test vraiment isolé : `--bare`,
ou une config dédiée avec `CLAUDE_CONFIG_DIR=/chemin/vide` (qui demandera sa propre
connexion).

## Dans une session : `/loop`

Sans script, pour surveiller quelque chose pendant que la session est ouverte :
```
/loop 5m vérifie si le déploiement est fini et dis-moi ce qui s'est passé
/loop 20m /revue-pr 1234
```
Les tâches `/loop` vivent dans la session (7 jours max) et s'arrêtent avec elle,
sauf si vous la passez en arrière-plan (←). Pour une vraie planification sans
session ouverte : cron ou launchd avec `claude -p`.

## Exercice

1. `claude -p "Compte les fichiers markdown de ce dossier" --allowedTools "Bash(ls *),Bash(find *)"`.
2. La même, `--output-format json | jq '.num_turns, .total_cost_usd'`.
3. Écrivez un `revue.sh` qui passe `git diff` à Claude avec un rôle de relecteur.
   Lancez-le sur un vrai diff.
