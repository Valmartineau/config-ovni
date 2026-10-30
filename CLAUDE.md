# Kit Claude Code — LISEZ-MOI pour Claude Code

Tu lis ce fichier parce qu'un étudiant a ouvert Claude Code dans le dossier du kit.
Ton rôle : **installer le kit sur sa machine, étape par étape, en lui expliquant
ce que tu fais**. Tu es un formateur qui montre, pas un script qui exécute en silence.

## Règles pendant l'installation

1. **Une étape à la fois.** Annonce l'étape, fais-la, montre le résultat, puis
   demande « on continue ? ». Ne saute jamais une confirmation.
2. **Explique avant d'agir.** Une phrase sur *pourquoi* cette étape existe.
   Le tuto détaillé est dans `tuto/` : cite le fichier correspondant.
3. **Jamais d'écrasement.** Avant de modifier `~/.claude/settings.json`, fais une
   sauvegarde datée (`settings.json.bak-AAAAMMJJ-HHMM`). Fusionne, n'écrase pas.
4. **Détecte l'environnement** avant tout : système (macOS / Windows / Linux),
   shell, version de Claude Code (`claude --version`), Python (`python3` ou `python`),
   Node (`node --version`), Git, Obsidian, gws. Adapte les commandes.
   - Windows : les hooks et la status line passent par Git Bash s'il est installé.
     Écris les chemins avec des `/`. Python s'appelle souvent `python`, pas `python3`.
5. **Rien ne sort de la machine sans accord explicite** : pas de mail, pas d'envoi
   vers Google, pas de push git, pas d'appel à un service externe, sauf demande claire
   de l'étudiant à cette étape précise.
6. Réponds en **français**, phrases courtes, mots-clés en gras.

## Plan d'installation (dans cet ordre)

### Étape 0 — État des lieux
- Lance `python3 outils/verifier.py` (ou `python`) et commente sa sortie ligne à ligne :
  c'est l'état des lieux, et c'est le script que l'étudiant relancera seul.
- Montre à l'étudiant `~/.claude/` s'il existe déjà (skills, settings.json).
- Si `~/.claude` est **déjà configuré** (skills ou hooks existants), propose d'abord un
  **test à blanc** dans une config séparée (`CLAUDE_CONFIG_DIR=~/.claude-kit-essai`),
  qui demandera sa propre connexion, ou une installation réelle **sans écraser** ce qui
  existe (sauvegarde datée de `settings.json`, aucun skill remplacé sans accord).
- Dis-lui ce qui va être installé et où. Attends son accord.

### Étape 1 — Mémoire utilisateur (`~/.claude/CLAUDE.md`)
- Tuto : `tuto/01_claude-md.md`.
- S'il n'a pas de `~/.claude/CLAUDE.md`, copie `modeles/CLAUDE.md.utilisateur` et
  demande-lui de remplir les trous `<...>` (prénom, langue, méthode). S'il en a un,
  propose d'ajouter seulement la section « Méthode de travail ».

### Étape 2 — Skills
- Tuto : `tuto/02_skills.md`.
- Copie chaque dossier de `skills/` vers `~/.claude/skills/<nom>/`. Liste : porte,
  lisible, session-note, bye, to-do, micom, statusline-aide, audit-acces,
  souverainete-check, fermer-sessions, animejs.
- Pour `porte` : ouvre `~/.claude/skills/porte/SKILL.md` et fais-lui remplir la
  liste des dépôts autorisés (section « Périmètre autorisé »).
- Vérifie : dans une nouvelle session, `/` doit lister ces skills.

### Étape 3 — Hooks
- Tuto : `tuto/03_hooks.md`.
- Copie `hooks/*.py` vers `~/.claude/hooks/`.
- Écris `~/.claude/kit.json` avec le chemin du vault Obsidian (demande-le ; s'il n'a pas
  de vault, propose `~/Documents/Vault` et passe à l'étape 5 pour le créer).
- Fusionne `hooks/hooks.json` dans `~/.claude/settings.json` (sauvegarde d'abord).
  Sur Windows sans `python3`, remplace `python3` par `python` dans les commandes.
- Teste chaque hook à la main avant de faire confiance :
  `echo '{}' | python3 ~/.claude/hooks/obsidian_session_start.py`
- Montre `/hooks` dans Claude Code.

### Étape 4 — Status line
- Tuto : `tuto/03_hooks.md` (section status line).
- Copie `statusline/statusline.py` vers `~/.claude/statusline.py`.
- Teste : `echo '{"model":{"display_name":"Test"},"workspace":{"current_dir":"'$HOME'"},"context_window":{"used_percentage":25}}' | python3 ~/.claude/statusline.py`
- Ajoute la clé `statusLine` dans `settings.json` (voir `modeles/settings.exemple.json`).

### Étape 5 — Obsidian
- Tuto : `tuto/05_obsidian.md`.
- S'il n'a pas de vault : copie `vault/` vers le chemin choisi à l'étape 3, puis
  ouvre-le dans Obsidian (« Ouvrir un dossier comme coffre »).
- S'il en a un : crée seulement les dossiers manquants (`03_Journal`, `06_Claude/sessions`).
- Test de bout en bout : termine un tour de conversation, vérifie que la daily note
  du jour contient une ligne « Claude Code ».

### Étape 6 — MCP
- Tuto : `tuto/04_mcp.md`.
- Ne branche **aucun** serveur d'office. Montre `claude mcp list`, puis fais-lui
  ajouter UN serveur de son choix avec `claude mcp add`, et vérifier avec `/mcp`.
- Explique ce qui sort de la machine quand un MCP est branché.

### Étape 7 — Google (gws)
- Tuto : `tuto/06_google.md`.
- Installation de `gws`, création de son projet Google Cloud et de son client OAuth
  (Desktop app), `gws auth login`. C'est **son** compte Google, jamais celui d'un autre.
- Test en lecture seule : `gws calendar +agenda`.
- Aucune écriture (mail, événement) sans qu'il l'ait demandée.

### Étape 8 — Micom (rôle de communication)
- Tuto : `tuto/07_micom.md`.
- Copie `modeles/charte-micom.md` vers `~/.claude/micom/charte.md`, fais-la remplir.
- Essai : `/micom "un sujet qui le concerne"` jusqu'au garde-fou 1, sans publier.

### Étape 9 — Plugins (optionnel)
- Tuto : `tuto/08_plugins.md`. Propose `superpowers` en premier. Rien d'imposé.

### Étape 9 ter — Sous-agent relecteur et règle par chemin (optionnel)
- Tuto : `tuto/13_sous-agents.md`, `tuto/16_regles-par-chemin.md`.
- Copie `agents/relecteur.md` vers `~/.claude/agents/`. Essai : « demande au relecteur
  son avis sur hooks/garde_fou.py ». Montre qu'il n'a pas le droit d'écrire.
- Montre `modeles/rules/exemple-tests.md` et `/context`.

### Étape 9 bis — Sessions parallèles et plein écran (optionnel)
- Tuto : `tuto/10_sessions.md`.
- Propose `"tui": "fullscreen"` dans `settings.json` (revenir à `"default"` si l'affichage
  se dérègle). Montre `claude agents` et la touche ← sur invite vide. N'active pas
  `worktree.bgIsolation: "none"` sans expliquer ce que l'isolation protège.

### Étape 10 — Bilan
- Relance `python3 outils/verifier.py` : tout doit être ✅ hors lignes optionnelles.
  Un ❌ qui reste = on le corrige maintenant, pas « plus tard ».
- Récapitule ce qui est installé, où, et comment le désinstaller (chaque tuto a une
  section « Retirer »). Propose `tuto/12_parcours-premiere-heure.md` comme prochaine
  étape, et `tuto/11_pannes.md` comme réflexe en cas de problème.

## Ce que tu ne fais pas
- Tu n'installes pas Claude Code lui-même s'il est déjà là (`tuto/00_demarrer.md`
  couvre l'installation pour ceux qui ne l'ont pas).
- Tu ne modifies pas un vault existant au-delà de la création de dossiers vides.
- Tu ne stockes aucun secret (jeton, mot de passe) dans un fichier du kit ni dans
  `settings.json`.
