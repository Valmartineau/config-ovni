# 12 — Parcours : la première heure

Six exercices, dix minutes chacun. Chaque exercice a un **résultat vérifiable** :
vous savez si vous avez réussi sans demander à personne. Faites-les dans l'ordre.

Prérequis : `claude --version` répond, et vous avez lancé `claude` dans le dossier
du kit au moins jusqu'à l'étape 2 (skills copiés).

## 1. Le contrat de permission (10 min)

Dans un dossier vide : `mkdir essai && cd essai && claude`.
Demandez : « crée un fichier bonjour.txt qui contient la date du jour ».

- Claude **demande** avant d'écrire. Répondez oui pour cette fois.
- Vérifiez : `cat bonjour.txt` contient une date.
- Demandez : « supprime-le ». Claude demande encore. Répondez non.
- ✅ Réussi si le fichier existe toujours et que Claude a respecté votre non.

Ce que vous avez appris : Claude ne fait rien sans vous, et un non est un non.

## 2. Votre mémoire utilisateur (10 min)

`/memory`, ouvrez `~/.claude/CLAUDE.md`. Ajoutez une ligne visible, par exemple
« Termine chaque réponse par le mot MERCI. » Fermez, **nouvelle session**, dites bonjour.

- ✅ Réussi si la réponse finit par MERCI.
- Retirez la ligne ensuite. Nouvelle session. ✅ Réussi si MERCI a disparu.

Ce que vous avez appris : le CLAUDE.md est lu au démarrage, pas en cours de session.

## 3. Un skill se déclenche (10 min)

Tapez `/lisible`. Puis posez une question longue, par exemple « explique-moi la
différence entre un hook et un skill ».

- ✅ Réussi si la réponse tient en phrases courtes, une par ligne, sans sigle non expliqué.
- Tapez « stop lisible ». Reposez la même question. ✅ Réussi si la forme a changé.

Ouvrez `~/.claude/skills/lisible/SKILL.md` et lisez la `description`. C'est elle qui
décide quand le skill se charge.

## 4. Un hook s'exécute (10 min)

Dans Claude Code, tapez `/hooks`. Vous devez voir SessionStart, Stop, PreToolUse.
Demandez : « exécute `git push --force origin main` » dans un dossier sans dépôt git.

- ✅ Réussi si Claude rapporte un refus du **garde-fou** avant d'avoir lancé quoi que ce soit.
- Ouvrez votre vault Obsidian, `03_Journal/`, la note du jour. ✅ Réussi si une ligne
  « HH:00 — Claude Code » est apparue.

Ce que vous avez appris : un hook est exécuté par le programme, pas par le modèle.
Le garde-fou aurait bloqué même si Claude avait « voulu » pousser.

## 5. Archiver une session (10 min)

Tapez `/session-note "mon premier parcours"`.

- ✅ Réussi si une note apparaît dans `06_Claude/sessions/` avec un bloc **Résumé**
  en prose et au moins un `[[wikilink]]`.
- Dans Obsidian, cliquez sur le wikilink : il pointe vers une note de projet qui
  n'existe pas encore. Créez-la. ✅ Réussi si la note de session apparaît dans ses
  **backlinks**.

Ce que vous avez appris : Claude écrit, vous reliez, Obsidian maille.

## 6. Le menu des sessions (10 min)

Dans votre session : `/rename parcours`. Puis touche **←** sur une invite vide.

- ✅ Réussi si le menu **agent view** s'ouvre avec votre session « parcours » listée.
- Dans la zone de saisie du menu, tapez : « écris un haïku sur le terminal » et Entrée.
  Une deuxième ligne apparaît. `Espace` dessus pour lire. `Ctrl+X` pour l'arrêter.
- `Entrée` sur « parcours » pour la rejoindre. `/bye`.

Ce que vous avez appris : plusieurs Claude, un seul écran, et vous restez le pilote.

## Après l'heure

Lancez `python3 outils/verifier.py`. Tout doit être ✅ sauf les lignes optionnelles.
Puis lisez `09_methode.md` : c'est le mode d'emploi de tout le reste.
