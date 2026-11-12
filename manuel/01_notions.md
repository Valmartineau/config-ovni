<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site 2ee80b0). Ne pas modifier à la main : relancer le script. -->

# 1. Les notions

Claude Code est un agent dans votre terminal. Il repart de zéro à chaque session. Une configuration lui donne une mémoire, des savoir-faire et des limites.

## Les briques d'une configuration

### Le modèle lit et suit

- **CLAUDE.md** (Lu à chaque session) : Le texte que Claude lit au démarrage. Mettez-y ce qu'il ne peut pas deviner : langue, méthode, interdits, commandes. Moins de 200 lignes par fichier. Où : `~/.claude/CLAUDE.md`.
- **Mémoire** (Écrite par Claude) : Des notes que Claude prend sur vous et sur le projet. Seul l'index est chargé. Elle reste sur votre machine. Relisez-la une fois par mois. Où : `~/.claude/projects/<projet>/memory/`.
- **Skill** (Chargé à la demande) : Un dossier avec un fichier SKILL.md. Il s'appelle par /nom, ou Claude le charge quand sa description correspond à votre demande. Où : `~/.claude/skills/<nom>/SKILL.md`.
- **Règle** (Selon le fichier touché) : Une consigne chargée seulement quand Claude travaille sur certains chemins. Elle allège le CLAUDE.md du projet. Où : `.claude/rules/`.

### Le programme exécute

- **Hook** (Un automatisme garanti) : Une commande lancée par Claude Code sur un événement. Le modèle ne peut pas l'oublier. C'est la bonne place pour un journal ou une interdiction. Où : `settings.json, clé hooks`.
- **Permissions** (Allow et deny) : Ce que Claude peut faire sans demander, et ce qu'il ne pourra jamais faire. La règle deny gagne toujours. Où : `settings.json, clé permissions`.
- **Status line** (L'état, sous vos yeux) : La ligne du bas : modèle, contexte, quota. Un script reçoit l'état de la session et l'affiche. Où : `~/.claude/statusline.py`.

### Un autre acteur travaille

- **MCP** (Une porte vers un outil) : Un standard pour brancher des outils externes. Un serveur expose des fonctions, Claude les utilise comme les siennes. Où : `.mcp.json ou claude mcp add`.
- **Sous-agent** (Un Claude contraint) : Une session enfant, avec son contexte et ses outils. Un relecteur sans droit d'écriture ne peut rien modifier, quoi qu'il décide. Où : `~/.claude/agents/<nom>.md`.
- **Plugin** (Un paquet versionné) : Des skills, hooks, agents et MCP livrés ensemble. Installez-en un à la fois et lisez ce qu'il pose sur votre machine. Où : `/plugin`.

## Ce qui est lu, selon le dossier où l'on lance `claude`

| Fichier | Pour qui |
|---|---|
| `~/.claude/CLAUDE.md` | Vous, partout |
| `mon-projet/CLAUDE.md` | Le projet, partagé avec l'équipe |
| `mon-projet/CLAUDE.local.md` | Vous, sur ce projet, hors git |
| `mon-projet/module/CLAUDE.md` | Le module |

Lancé depuis le dossier personnel : seul `~/.claude/CLAUDE.md` est lu. Depuis le projet : les trois premiers au démarrage, celui du module à la demande. Depuis le module : tous.

## L'ordre des hooks pendant un tour

SessionStart → UserPromptSubmit → PreToolUse → L'outil → PostToolUse → Stop

Un hook `PreToolUse` peut bloquer l'outil avant qu'il agisse (code de sortie 2).

## Ce qui sort de votre machine

- **Claude lit un fichier** : Le contenu du fichier part au modèle.
- **Un MCP local répond** : Le serveur tourne chez vous. Sa réponse part quand même au modèle.
- **Un MCP distant répond** : Le service reçoit vos requêtes. Sa réponse part aussi au modèle.

## Où ranger une consigne : les questions, dans l'ordre

1. Cela doit arriver à coup sûr ? → **Hook**
2. Il faut parler à un service externe ? → **MCP**
3. Il faut isoler ou contraindre le travail ? → **Sous-agent**
4. C'est un savoir-faire utile de temps en temps ? → **Skill**
5. C'est valable pour chaque session ? → **CLAUDE.md**

Exemples :

| Situation | Brique | Pourquoi |
|---|---|---|
| Claude doit toujours répondre en français. | CLAUDE.md | Une règle valable à chaque session. |
| Bloquer à coup sûr tout push forcé sur main. | Hook | Une interdiction doit être exécutée par le programme. |
| Une méthode de compte rendu, utile une fois par semaine. | Skill | Un savoir-faire chargé seulement quand il sert. |
| Lire mes pages Notion depuis Claude Code. | MCP | Une porte vers un service externe. |
| Un relecteur qui ne doit jamais pouvoir modifier le code. | Sous-agent | On lui retire les outils d'écriture. |
| Écrire une ligne dans mon journal après chaque réponse. | Hook | Un automatisme sur l'événement Stop. |
| Les commandes de test et de lancement de ce projet. | CLAUDE.md | Le CLAUDE.md du projet, partagé avec l'équipe. |
| Transformer un sujet en post, quand je le demande. | Skill | Un savoir-faire appelé par une commande. |
