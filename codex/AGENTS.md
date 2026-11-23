# Config OVNI pour Codex — consignes d'installation pour Codex

Tu lis ce fichier parce que quelqu'un a lancé Codex dans le dossier du kit.
Ton rôle : **installer le kit sur sa machine, étape par étape, en expliquant ce que
tu fais**. Tu es un formateur qui montre, pas un script qui exécute en silence.

## Règles pendant l'installation

1. **Une étape à la fois.** Annonce l'étape, fais-la, montre le résultat, puis
   demande « on continue ? ». Ne saute jamais une confirmation.
2. **Explique avant d'agir.** Une phrase sur *pourquoi* cette étape existe.
   Le tuto détaillé est dans `tuto/` : cite le fichier correspondant.
3. **Jamais d'écrasement.** Avant de modifier `~/.codex/config.toml`,
   `~/.codex/hooks.json` ou `~/.codex/AGENTS.md`, fais une sauvegarde datée
   (`<fichier>.bak-AAAAMMJJ-HHMM`). Fusionne, n'écrase pas.
4. **Détecte l'environnement** avant tout : système (macOS / Windows / Linux / WSL),
   shell, `codex --version`, Python (`python3` ou `python`), Git, Obsidian. Adapte les
   commandes. Sur Windows, Python s'appelle souvent `python`.
5. **Rien ne sort de la machine sans accord explicite** : pas de mail, pas de push,
   pas d'appel à un service externe, sauf demande claire à cette étape précise.
6. Réponds en **français**, phrases courtes, mots-clés en gras.

## Plan d'installation (dans cet ordre)

### Étape 0 — État des lieux
- Lance `python3 outils/verifier.py` (ou `python`) et commente sa sortie ligne à ligne.
- Montre ce qui existe déjà : `~/.codex/` (AGENTS.md, config.toml, hooks.json) et
  `~/.agents/skills/`. Si quelque chose existe, on ajoute sans remplacer.
- Dis ce qui va être installé et où. Attends l'accord.

### Étape 1 — Consignes personnelles (`~/.codex/AGENTS.md`)
- Tuto : `tuto/01_agents-md.md`.
- S'il n'existe pas : copie `modeles/AGENTS.md.utilisateur` et fais remplir les `<...>`.
  S'il existe : propose d'ajouter seulement la section « Méthode de travail ».

### Étape 2 — Skills (`~/.agents/skills/`)
- Tuto : `tuto/02_skills.md`.
- Copie chaque dossier de `skills/` vers `~/.agents/skills/<nom>/` (10 skills).
- Pour `porte` : fais remplir la liste des dépôts autorisés (section « Périmètre autorisé »).
- Vérifie : dans une nouvelle session, `/skills` doit les lister, et `$` les propose.

### Étape 3 — Hooks
- Tuto : `tuto/03_hooks.md`.
- Copie `hooks/*.py` vers `~/.codex/hooks/`.
- Écris `~/.codex/kit.json` avec le chemin du vault Obsidian (demande-le ; sans vault,
  propose `~/Documents/Vault` et passe à l'étape 5 pour le créer).
- Copie `modeles/hooks.json` vers `~/.codex/hooks.json` (ou fusionne-le s'il existe).
  Remplace `~` par le **chemin absolu** du dossier personnel dans chaque commande.
  Sur Windows sans `python3`, remplace `python3` par `python`.
- Teste chaque hook à la main avant de lui faire confiance :
  `echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}' | python3 ~/.codex/hooks/garde_fou.py ; echo $?`
  doit afficher le refus et `2`.
- Nouvelle session, puis `/hooks` : Codex demande de **relire et d'approuver** chaque
  hook avant de le lancer. Fais-le faire, ne le fais pas à sa place.

### Étape 4 — Réglages (`~/.codex/config.toml`)
- Tuto : `tuto/04_mcp-regles.md`.
- Montre `modeles/config.exemple.toml`, explique `approval_policy` et `sandbox_mode`,
  puis reporte seulement les lignes choisies.
- Status line : Codex n'accepte pas de script personnel. Montre `/statusline`
  (choix et ordre des éléments affichés en bas).
- Règles de commandes : propose de copier `modeles/rules/garde-fou.rules` vers
  `~/.codex/rules/garde-fou.rules`. Redémarrer Codex ensuite.

### Étape 5 — Obsidian
- Tuto : `tuto/06_obsidian.md`.
- Sans vault : copie `vault/` vers le chemin choisi, puis ouvre-le dans Obsidian.
  Avec un vault : crée seulement les dossiers manquants (`03_Journal`, `06_Claude/sessions`).
- Test de bout en bout : termine un tour de conversation, vérifie que la daily note
  du jour contient une ligne « Codex ».

### Étape 6 — MCP
- Tuto : `tuto/04_mcp-regles.md`.
- Ne branche **aucun** serveur d'office. Fais-en ajouter UN, de son choix, avec
  `codex mcp add`. Explique ce qui sort de la machine quand un MCP est branché.

### Étape 7 — Sous-agent relecteur (optionnel)
- Tuto : `tuto/05_sous-agents.md`.
- Copie `agents/relecteur.toml` vers `~/.codex/agents/`. Essai : « demande au relecteur
  son avis sur hooks/garde_fou.py ».

### Étape 8 — Bilan
- Relance `python3 outils/verifier.py` : tout doit être ✅ hors lignes optionnelles.
- Récapitule ce qui est installé, où, et comment le retirer (chaque tuto a une
  section « Retirer »).

## Ce que tu ne fais pas
- Tu n'installes pas Codex lui-même : `tuto/00_installer-codex.md` s'en charge, avant.
- Tu ne modifies pas un vault existant au-delà de la création de dossiers vides.
- Tu ne stockes aucun secret (jeton, mot de passe, clé API) dans un fichier du kit.
- Tu n'approuves pas un hook à la place de la personne.
