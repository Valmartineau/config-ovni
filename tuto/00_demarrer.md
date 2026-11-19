# 00 — Démarrer avec Claude Code

## Ce que c'est

Claude Code est un **agent dans votre terminal**. Il lit vos fichiers, lance des
commandes, écrit du code, et vous demande la permission avant les gestes sensibles.
Ce n'est pas un chat : c'est un collègue qui a accès à votre machine. D'où l'importance
de comprendre ce qu'il fait (ce kit sert à ça).

Il faut un compte Claude **Pro, Max, Team ou Enterprise** (ou une clé API). Le plan
gratuit ne donne pas accès à Claude Code.

## Installer

**macOS, Linux, WSL :**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell) :**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows (CMD) :**
```bat
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Sur Windows, installez aussi **Git for Windows** (https://git-scm.com/downloads/win).
Il apporte Git Bash, dont Claude Code se sert pour lancer les commandes, les hooks
et la status line. Sans Git Bash, Claude Code utilise PowerShell et une partie de ce
kit (hooks en shell) ne fonctionnera pas telle quelle.

Vérifier :
```bash
claude --version
claude doctor
```

## Première session

```bash
cd un-dossier-de-projet
claude
```

La première fois, un navigateur s'ouvre pour vous connecter. Ensuite :

- Tapez une demande en langage naturel.
- `/` ouvre la liste des commandes et des skills.
- `/help` liste les commandes de base. `/config` règle le modèle, le thème, etc.
- `Échap` interrompt. `Ctrl+C` deux fois quitte.
- `/clear` vide la conversation. `/compact` la résume pour libérer de la place.

## Les permissions

En **mode manuel**, Claude Code **demande** avant d'écrire un fichier ou de lancer une commande.
Trois réponses possibles : oui pour cette fois, oui pour toujours dans ce projet, non.
Depuis la version 2.1.283, une session démarre en **mode auto** : voir plus bas.

Ce que vous autorisez « pour toujours » s'écrit dans `.claude/settings.json` du projet
(ou `~/.claude/settings.json` pour toute la machine) sous `permissions.allow`.
Il existe aussi `permissions.deny` : ce que Claude ne pourra **jamais** faire, même
si vous cliquez oui par erreur. Exemple utile : interdire la lecture d'un dossier
personnel. Voir `modeles/settings.exemple.json`.

### Les modes de permission

Le mode dit ce que Claude peut faire **sans vous demander**. Il est écrit sur la ligne
du bas. `Maj+Tab` passe de l'un à l'autre.

| Mode | Ligne du bas | Ce qui passe sans question |
|---|---|---|
| Manuel (`default`) | `manual mode on` | Les lectures |
| Modifications acceptées (`acceptEdits`) | `accept edits on` | Les lectures et les modifications de fichiers |
| Plan (`plan`) | `plan mode on` | Les lectures ; Claude propose un plan, sans rien modifier |
| Auto (`auto`) | `auto mode on` | Presque tout, sous le contrôle d'un second modèle |

**Le mode auto.** Un second modèle, le **classifieur**, examine chaque action avant
qu'elle parte, à votre place. Les lectures et les modifications dans le dossier de travail
passent directement. Depuis Claude Code 2.1.283, c'est le mode de **départ** dans le
terminal et dans VS Code, sur toutes les offres.

- **Bloqué par défaut** : télécharger puis exécuter du code (`curl | bash`), envoyer des
  données sensibles vers l'extérieur, déployer en production, `git push --force`,
  `git reset --hard`, détruire des fichiers qui existaient avant la session.
- **Laissé passer** : le travail dans le dossier, l'installation des dépendances déclarées,
  les requêtes en lecture seule, et **le `git push` vers le dépôt où vous travaillez**.
- **Après 3 blocages de suite ou 20 dans la session**, le mode auto se met en pause et
  Claude recommence à demander.
- Vos règles `deny` et `ask`, et vos hooks, s'appliquent **avant** le classifieur.

Trois choses à retenir :

1. Le mode auto **réduit les questions, il ne garantit pas la sécurité**. Pour un geste
   sensible, repassez en manuel avec `Maj+Tab`.
2. La règle du collectif « rien ne sort sans votre accord » n'est plus tenue par l'outil
   pour le `push`. Pour garder la question, ajoutez dans `~/.claude/settings.json` :

   ```json
   { "permissions": { "ask": ["Bash(git push *)", "Bash(gh pr create *)"] } }
   ```

3. Pour démarrer toujours en manuel : `"permissions": { "defaultMode": "default" }` dans
   `~/.claude/settings.json`. La valeur `"auto"` n'est lue que dans ce fichier, pas dans
   le `.claude/settings.json` d'un projet.

Ce qui sort : en mode auto, le classifieur reçoit vos messages, les actions demandées et
le contenu de votre `CLAUDE.md`. Il tourne chez Anthropic, comme Claude.

Source : <https://code.claude.com/docs/en/permission-modes>, lue le 13/11/2026.

## Les fichiers de Claude Code

| Chemin | Rôle |
|---|---|
| `~/.claude/CLAUDE.md` | Votre mémoire utilisateur, lue dans **toutes** les sessions |
| `~/.claude/settings.json` | Réglages, permissions, hooks, status line |
| `~/.claude/skills/` | Vos skills personnels |
| `~/.claude/projects/` | Historique des conversations (par projet) |
| `~/.claude.json` | Serveurs MCP, état interne |
| `<projet>/CLAUDE.md` | Mémoire du projet, à commiter |
| `<projet>/.claude/` | Settings et skills du projet |
| `<projet>/.mcp.json` | Serveurs MCP partagés avec l'équipe |

## Avant d'aller plus loin : savoir prompter

Claude Code fait ce que vos mots disent, pas ce que vous pensiez. La fiche suivante,
`00b_savoir-prompter`, explique comment on constitue un prompt : rôle, contexte, tâche,
contraintes, format. Dix minutes qui changent tout le reste.

## Le kit, maintenant

Ouvrez un terminal dans le dossier du kit et lancez `claude`. Le fichier `CLAUDE.md`
du kit prend le relais et vous guide.

## Retirer

```bash
rm -f ~/.local/bin/claude && rm -rf ~/.local/share/claude   # macOS / Linux
```
```powershell
Remove-Item "$env:USERPROFILE\.local\bin\claude.exe" -Force
Remove-Item "$env:USERPROFILE\.local\share\claude" -Recurse -Force
```
Vos réglages restent dans `~/.claude/` tant que vous ne les supprimez pas.
