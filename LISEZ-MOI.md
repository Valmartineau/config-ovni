# Kit Claude Code — pour démarrer

Ce kit transmet une configuration de **Claude Code** mise au point sur plusieurs mois
de pratique : méthode de travail, skills, hooks, status line, second cerveau Obsidian,
accès à Google, rôle de communication. Tout est **générique** : aucun projet, aucun
compte, aucune donnée d'origine. Vous remplissez les trous avec les vôtres.

## En 3 gestes

1. Dézippez le kit. Ouvrez un terminal **dans le dossier du kit**.
2. Lancez `claude`. Claude Code lit le fichier `CLAUDE.md` du kit et vous guide,
   étape par étape. Il vous demande votre accord avant chaque geste.
3. Suivez, posez vos questions, lisez le `tuto/` correspondant à chaque étape.

Pas encore Claude Code sur votre machine ? Lisez d'abord `tuto/00_demarrer.md`.

## Ce qu'il y a dedans

| Dossier | Contenu |
|---|---|
| `CLAUDE.md` | Le guide d'installation **que Claude Code exécute** avec vous |
| `tuto/` | Le cours, pas à pas, un fichier par notion (skills, hooks, MCP, Obsidian, Google, sessions, sous-agents, mémoire, `claude -p`, règles…) |
| `outils/verifier.py` | **L'auto-diagnostic** : ✅ / ❌ et la commande qui répare. À relancer à tout moment |
| `agents/` | Un sous-agent relecteur, lecture seule, prêt à copier dans `~/.claude/agents/` |
| `skills/` | 7 skills prêts à copier dans `~/.claude/skills/` |
| `hooks/` | 3 hooks Python + le bloc JSON à fusionner dans `settings.json` |
| `statusline/` | Une status line lisible (contexte, quota, session, notes) |
| `modeles/` | Gabarits : CLAUDE.md utilisateur et projet, settings, MCP, charte Micom |
| `vault/` | Squelette d'un vault Obsidian qui parle avec Claude Code |

## Ordre de lecture conseillé

`00_demarrer` → `01_claude-md` → `02_skills` → `03_hooks` → `04_mcp` →
`05_obsidian` → `06_google` → `07_micom` → `08_plugins` → `09_methode` →
`10_sessions` (plusieurs Claude en parallèle, le menu agent view, le plein écran) →
`11_pannes` (à garder sous la main) → `12_parcours-premiere-heure` (à faire, pas à lire) →
`13_sous-agents` → `14_memoire-automatique` → `15_claude-p` → `16_regles-par-chemin` → `glossaire`.

**En cas de doute à n'importe quel moment :** `python3 outils/verifier.py`.

## Trois principes qui tiennent tout

- **Comprendre avant d'automatiser.** Chaque hook, chaque skill, vous l'avez lu
  et testé à la main avant de le laisser tourner seul.
- **Rien ne sort sans votre accord.** Mail, événement, push, publication :
  c'est votre geste, jamais celui de la machine.
- **État visible = état réel.** Ce qui n'est pas vérifié de bout en bout est
  marqué « en cours », pas « fait ».

## Pour aller plus loin : l'IA souveraine

Ce kit est né d'une pratique : garder la main sur ses données et ses outils.
Le blog d'OVNI Conseil développe cette approche, cas concrets à l'appui :

- Les articles : https://www.ovniconseil.fr/blog
- L'espace pédagogique, guidé par un agent : https://www.ovniconseil.fr/blog/explorer

Parcourez-le après le tuto `09_methode.md` : les deux se répondent.

Licence : le skill `lisible` porte sa licence MIT. Le reste du kit est libre
d'usage et de modification pour un usage pédagogique.
