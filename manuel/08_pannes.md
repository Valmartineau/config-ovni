<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site a9c0064). Ne pas modifier à la main : relancer le script. -->

# 8. En cas de panne

Premier réflexe : `python3 outils/verifier.py` puis `claude doctor`. Si vous demandez de l'aide, envoyez la sortie brute de la commande. Fiche détaillée : `tuto/11_pannes.md`.

## Claude Code et le kit

| Ce que vous voyez | Ce qu'il faut faire |
|---|---|
| claude n'est pas reconnu | Fermez et rouvrez le terminal. Sinon, vérifiez que .local/bin existe et ajoutez-le au PATH. |
| 'irm' n'est pas reconnu | Vous êtes dans CMD. Ouvrez PowerShell. |
| Not logged in | Lancez claude sans argument et suivez le navigateur. |
| python3: command not found | Sur Windows, remplacez python3 par python dans les hooks et la status line. |
| Un hook ne fait rien | Tapez /hooks pour voir s'il est listé. Testez-le à la main : s'il plante là, il plante en silence dans Claude Code. |
| Rien dans Obsidian | Contrôlez le chemin dans ~/.claude/kit.json. Toujours des /, même sur Windows. |
| Claude est lent à chaque commande | Un hook synchrone pèse. Mesurez-le. Passez-le en "async": true s'il ne fait qu'observer. |
| Un hook bloque tout | "disableAllHooks": true dans settings.json, le temps de corriger. |
| /mon-skill n'apparaît pas | Nouvelle session. Le fichier s'appelle bien SKILL.md, avec --- en première ligne. |
| Le skill ne se déclenche jamais | Réécrivez la description avec les mots que vous tapez vraiment. |
| Le contexte est plein | /context pour voir ce qui pèse, /compact pour résumer, /clear pour repartir. |


## L'IA locale (étape 2)

| Ce que vous voyez | Ce qu'il faut faire |
|---|---|
| Hermes répond « context too small » ou coupe ses réponses | Le modèle n'a pas reçu ses 65536 jetons de mémoire de travail. Refaites le geste 3 (lui donner de la place), puis vérifiez que model.default vaut agent-local. |
| « connection refused » sur localhost:11434 | Ollama ne tourne pas. Sur Mac et Windows, ouvrez l'application Ollama. Sur Linux : ollama serve dans un autre terminal. |
| Tout est très lent, le ventilateur souffle | Le modèle est trop gros pour la machine. ollama ps doit afficher 100% GPU. Sinon, prenez le palier du dessous. |
| hermes : commande introuvable | Fermez et rouvrez le terminal. Sur Mac et Linux, vérifiez que ~/.local/bin est dans le PATH, comme pour Claude Code. |
| L'assistant de Hermes s'ouvre à l'installation | Choisissez « Custom endpoint », adresse http://localhost:11434/v1, modèle agent-local. Ou quittez-le : le geste 5 (brancher Hermes) fait le même réglage. |
