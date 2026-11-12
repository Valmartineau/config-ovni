<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site 2ee80b0). Ne pas modifier à la main : relancer le script. -->

# 3. Installer pas à pas

Il faut une offre Claude Pro, Max, Team ou Enterprise. Le plan gratuit ne donne pas accès à Claude Code.

1. **Installer Claude Code.** Ouvrez un terminal (Mac : Commande + Espace, « terminal » ; Windows : menu Démarrer, « PowerShell »).

   macOS, Linux : `curl -fsSL https://claude.ai/install.sh | bash`
   Windows, PowerShell : `irm https://claude.ai/install.ps1 | iex`
   Windows, CMD : `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`

2. **Vérifier :** `claude --version` puis `claude doctor`.
3. **Récupérer le kit et lancer Claude dedans :** `git clone https://github.com/Valmartineau/config-ovni.git`, `cd config-ovni`, `claude`. La première fois, connectez-vous dans le navigateur.
4. **Lui demander de conduire :** « installe le kit ». Une étape à la fois, avec votre accord.
5. **Contrôler :** `python3 outils/verifier.py` (Windows : `python`).

**Sur Windows :** installez Git for Windows, dont Claude Code se sert pour les hooks et la status line. La commande CMD ne marche pas dans PowerShell. Si `claude` n'est pas reconnu, fermez et rouvrez le terminal.

## Les stations de l'installation

1. **État des lieux** : Claude regarde votre système, vos outils et ce qui existe déjà. Il dit ce qu'il va installer et où.
2. **Mémoire** : Votre ~/.claude/CLAUDE.md : prénom, langue, méthode de travail.
3. **Skills** : Onze dossiers copiés dans ~/.claude/skills/. Ils apparaissent dans la liste / en nouvelle session.
4. **Hooks** : Les trois hooks, branchés après une sauvegarde de settings.json, et testés à la main.
5. **Status line** : La ligne du bas : modèle, contexte, quota.
6. **Obsidian** : Votre vault, créé ou complété. Le test : une ligne apparaît dans la note du jour.
7. **MCP** : Aucun serveur d'office. Vous en ajoutez un, de votre choix, et vous regardez ce qui sort.
8. **Google** : Votre propre projet Google Cloud et votre compte. Essai en lecture seule.
9. **Micom** : Le rôle de communication, avec votre charte. Essai sans publier.
10. **Options** (facultatif) : Plugins, sous-agent relecteur, règles par chemin, sessions parallèles. Rien d'imposé.
11. **Bilan** : Le vérificateur repasse. Ce qui reste en échec se corrige tout de suite.
