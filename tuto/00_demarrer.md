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

Par défaut, Claude Code **demande** avant d'écrire un fichier ou de lancer une commande.
Trois réponses possibles : oui pour cette fois, oui pour toujours dans ce projet, non.

Ce que vous autorisez « pour toujours » s'écrit dans `.claude/settings.json` du projet
(ou `~/.claude/settings.json` pour toute la machine) sous `permissions.allow`.
Il existe aussi `permissions.deny` : ce que Claude ne pourra **jamais** faire, même
si vous cliquez oui par erreur. Exemple utile : interdire la lecture d'un dossier
personnel. Voir `modeles/settings.exemple.json`.

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
