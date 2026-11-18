# 17 — Boucles : faire travailler Claude sans le relancer

## L'idée

Par défaut, Claude travaille **un tour à la fois** : vous demandez, il répond, il attend.
Une **boucle**, c'est Claude qui recommence seul : il agit, regarde le résultat, décide
de continuer ou de s'arrêter.

Ce n'est pas une brique de plus. C'est une **façon de faire tourner** les briques que vous
avez déjà (skills, hooks, permissions, sous-agents) **dans le temps**.

Le kit en parle à trois endroits. Ce tuto les relie.

## Trois niveaux

| Niveau | Outil | Claude tourne… | Vous êtes… | Détail |
|---|---|---|---|---|
| 1. Surveiller | `/loop` | dans la session ouverte | devant, ou pas loin | `15_claude-p` |
| 2. Construire | `/porte` | en une traite, dans un worktree | absent, puis juge à la sortie | `02_skills`, skill `porte` |
| 3. Planifier | `claude -p` + cron ou launchd | sans session, à heure fixe | absent, vous lisez le journal | `15_claude-p` |

Montez d'un niveau seulement quand le précédent marche sans surprise.

## Niveau 1 — `/loop` : il revérifie tout seul

```
/loop 5m vérifie si le déploiement est fini et dis-moi ce qui s'est passé
/loop 20m /revue-pr 1234
/loop surveille les tests et corrige ce qui casse
```

- Avec une **durée** (`5m`, `20m`) : Claude relance la demande à cet intervalle.
- **Sans durée** : Claude choisit lui-même son rythme.
- La boucle vit dans la session. Elle s'arrête quand vous le lui dites, ou quand la
  session se ferme.

Bon usage : **attendre quelque chose** (un déploiement, une revue, un test long).
Mauvais usage : une demande floue qui n'a pas de fin.

## Niveau 2 — `/porte` : il construit seul, vous jugez

```
/porte ~/projets/mon-site "ajouter la page contact, avec ses tests"
```

Claude ouvre un worktree, puis boucle seul : coder, tester, commiter, recommencer.
Vous donnez **deux go** : un pour ouvrir, un pour fusionner. Entre les deux, il ne
vous sollicite pas, et **rien ne sort** de la machine.

À la sortie, vous lisez `STATE.md` et le diff. Vous fusionnez, ou vous jetez.

## Niveau 3 — `claude -p` planifié : il tourne sans session

```bash
0 2 * * *  cd ~/projets/x && claude -p "/to-do-nuit" --strict-mcp-config --permission-mode acceptEdits --max-turns 30 >> ~/journal-nuit.log 2>&1
```

Ici, personne ne regarde. Fermez d'abord **les trois portes** de `15_claude-p` :
les MCP, les permissions, le périmètre.

## Quatre questions avant de lancer une boucle

1. **Quand s'arrête-t-elle ?** Une condition claire (« les tests passent », « le
   déploiement est fini ») **et** un plafond (`--max-turns`, une durée, un nombre d'essais).
   Trois échecs de suite sur le même problème : la boucle s'arrête et vous attend.
2. **Où a-t-elle le droit d'agir ?** Un dossier, une branche. Jamais `main`, jamais un
   dossier synchronisé avec un cloud.
3. **Combien coûte-t-elle ?** Chaque tour consomme votre quota, même si rien n'a changé.
   Un `/loop 1m` oublié une nuit, c'est plusieurs centaines de tours. Regardez la status line.
4. **Qu'est-ce qui peut sortir ?** Mail, push, publication, paiement : **jamais dans une
   boucle**. La boucle prépare, vous envoyez.

Une règle pour tout retenir : **l'autonomie va sur le faire, votre accord reste sur le sortir.**

## Ce qui garde la boucle dans ses rails

Une consigne dans le prompt ne suffit pas : au vingtième tour, le modèle peut l'avoir perdue.
Ce qui tient, c'est ce que **le programme** exécute :

| Besoin | Brique | Tuto |
|---|---|---|
| Interdire un geste à coup sûr | hook `PreToolUse`, règle `deny` | `03_hooks` |
| Plafonner les tours | `--max-turns`, `maxTurns` d'un sous-agent | `13_sous-agents`, `15_claude-p` |
| Isoler le travail | worktree | skill `porte` |
| Faire relire par un autre | sous-agent `relecteur`, sans droit d'écriture | `13_sous-agents` |
| Savoir où elle en est | `STATE.md`, un journal | skill `porte` |

Le **mode auto** réduit les questions pendant une boucle. Il ne remplace aucune de ces
protections : voir `00_demarrer`.

## Ce qui sort

Une boucle envoie au modèle la même chose qu'une session normale, **à chaque tour** :
vos fichiers lus, les résultats des commandes. Une boucle sur un dossier sensible
l'envoie donc plusieurs fois. Choisissez le dossier avant de lancer.

## Quand ne pas boucler

- La tâche n'a pas de **critère de fin** vérifiable par une commande.
- Elle touche des données que vous ne confieriez pas à une session normale.
- Vous ne pourriez pas **relire** ce qu'elle a produit : dix commits que personne ne
  lit, ce n'est pas du travail fait.

## Le kit fournit

- le skill `/porte` (niveau 2), avec sa liste de dépôts autorisés à remplir ;
- le hook `garde_fou.py`, qui bloque les commandes destructrices évidentes, même en boucle ;
- le sous-agent `relecteur`, pour faire relire sans laisser modifier.

## Exercice

1. **Niveau 1.** Dans un projet avec des tests : `/loop 2m lance les tests et dis-moi
   seulement s'ils cassent`. Cassez un test à la main. Attendez. Puis dites « arrête la boucle ».
2. Avant de lancer, écrivez en une ligne **la condition d'arrêt**. Si vous n'y arrivez
   pas, la demande n'est pas prête pour une boucle.
3. **Niveau 2**, plus tard : une petite tâche derrière `/porte`, sur un dépôt sans enjeu.
   Lisez `STATE.md` avant le diff.
