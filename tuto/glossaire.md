# Glossaire

- **Agent** : programme qui enchaîne lui-même lecture, décision, action, avec un modèle
  de langage aux commandes. Claude Code en est un.
- **CLAUDE.md** : fichier d'instructions lu au démarrage de chaque session. Existe à
  plusieurs niveaux (utilisateur, projet, sous-dossier), concaténés.
- **Contexte (fenêtre de)** : tout ce que le modèle « voit » : vos messages, ses réponses,
  les fichiers lus, les résultats d'outils. Limité. Se remplit. `/compact` le résume.
- **Hook** : commande exécutée **par Claude Code** (pas par le modèle) sur un événement.
  Fiable par construction. Peut injecter du contexte (exit 0) ou bloquer (exit 2).
- **MCP** (Model Context Protocol) : standard pour brancher des outils externes sur un
  modèle. Un serveur MCP = une liste de fonctions décrites. Transport stdio (local) ou http.
- **Marketplace** : catalogue de plugins, souvent un dépôt git.
- **Plugin** : paquet versionné de skills + hooks + agents + MCP.
- **Permission (allow / deny)** : règles dans `settings.json`. `deny` gagne toujours.
- **Porte** (skill du kit) : autonomie bornée ; Claude code seul dans un worktree, sans
  réseau ni action sortante, et attend votre go pour merger.
- **Quota 5 h / 7 j** : fenêtres glissantes de consommation des offres Claude. Visibles
  dans la status line.
- **Scope (OAuth)** : périmètre de droits accordé à une application (lecture agenda,
  écriture mail…). Demander le minimum.
- **Session** : une conversation Claude Code, de `claude` à la fermeture. Vide au départ.
- **Skill** : dossier avec `SKILL.md` ; savoir-faire chargé à la demande, invocable en `/nom`.
- **Status line** : la ligne du bas, produite par un script qui reçoit l'état de session en JSON.
- **stdio / stdin / stdout** : entrée/sortie standard d'un programme. Les hooks lisent
  stdin (JSON) et écrivent stdout.
- **Subagent** : session enfant lancée par Claude pour une sous-tâche, avec son propre contexte.
- **Vault** : dossier de notes markdown ouvert dans Obsidian. Fichiers locaux, liens `[[wiki]]`.
- **Wikilink** : `[[Nom_de_note]]`. Crée un lien ; la note cible affiche les backlinks.
- **Worktree** : copie de travail git parallèle, sur sa propre branche, dans un autre dossier.
- **`$ARGUMENTS`** : dans un skill, le texte tapé après `/nom`.
- **Agent view** : le menu de toutes les sessions en cours (`claude agents`, ou ← sur invite
  vide). Lancer, surveiller, répondre, basculer.
- **Session en arrière-plan** : session qui tourne sans occuper le terminal (`claude --bg`,
  `/bg`, ←). Visible dans agent view.
- **tui fullscreen** : mode d'affichage plein écran sans scintillement (`"tui": "fullscreen"`).
- **Mémoire automatique** : notes que Claude écrit lui-même dans
  `~/.claude/projects/<projet>/memory/` ; l'index `MEMORY.md` est chargé à chaque session.
- **`-p` / `--print`** : Claude Code sans interface, pour un script ou un cron.
- **`--bare`** : `-p` sans rien charger de la machine (ni hooks, ni skills, ni CLAUDE.md).
- **Règle par chemin** : fichier de `.claude/rules/` avec `paths:` ; chargé seulement
  quand Claude touche un fichier correspondant.
- **Sous-agent** (custom) : fichier `.claude/agents/<nom>.md` ; session enfant avec ses
  propres outils, modèle et plafond de tours.
