# Mettre à jour la Config OVNI

## Le geste, pour vous

Ouvrez Claude Code et écrivez :

> mets à jour le kit https://github.com/Valmartineau/config-ovni

Claude récupère la nouvelle version, vous dit ce qui a changé, puis propose chaque
ajout **un par un**. Il sauvegarde avant de remplacer un fichier. Il ne touche ni à votre
`CLAUDE.md`, ni à votre mémoire, ni à votre vault sans que vous le demandiez.

Vous aviez cloné le kit avec git ? Ouvrez `claude` dans ce dossier et dites
« mets à jour le kit » : il fera `git pull` avec votre accord.

## Journal des versions

### 2026-11-18 : les boucles

- **`tuto/17_boucles.md`** : faire travailler Claude **sans le relancer**. Trois niveaux :
  `/loop` (il revérifie tout seul), `/porte` (il construit seul, vous jugez),
  `claude -p` planifié (il tourne sans session). Et les quatre questions à se poser avant.
- **Glossaire** : entrée « Boucle ».

Rien à installer. Aucun de vos réglages n'est modifié.

### 2026-11-13 : le mode auto

- **`tuto/00_demarrer.md`** : les modes de permission, et le **mode auto**, devenu le mode
  de départ de Claude Code. Ce qu'il bloque, ce qu'il laisse passer (dont le `git push`),
  et la règle à ajouter pour garder la question avant un push.
- **Exercice 1** (`tuto/12_parcours-premiere-heure.md`) : il se fait en mode manuel.
- **Glossaire** : entrée « Mode auto ».

Rien à installer. Aucun de vos réglages n'est modifié.

### 2026-11-12 : le manuel complet dans le dépôt

- **`manuel/`** : tout le contenu de la page Config OVNI, en fiches texte. Notions, méthode,
  six tutos, exercices, bibliothèque, **catalogue selon votre métier (83 skills, avec ce qu'il
  faut savoir sur chacun)**, pannes, et le parcours guidé de NOVI. Votre Claude Code peut
  désormais répondre comme la page.
- **`etape-2-ia-locale/`** : votre IA locale (Ollama + Hermes), la grille des modèles selon
  la mémoire de votre machine, et le script qui la mesure.
- **`etape-3-construire/`** : construire votre interface. Les mods `ma-jauge` (contexte et
  quotas) et `ma-dictee` (dicter, écouter, poser une question à votre agent local).
- **`exercices/boucle-voix/`** : parler à son ordinateur, avec un coach (`/commencer`).
- **`codex/`** : la même configuration pour Codex (OpenAI).
- Le pilote `CLAUDE.md` sait maintenant **mettre à jour** une installation existante.

Rien n'est installé d'office : les étapes 2 et 3 restent facultatives.

### 2026-10-30 : licence CC BY-NC 4.0, onze skills

Version transmise avant le 12 novembre.
