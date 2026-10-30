---
name: fermer-sessions
disable-model-invocation: true
description: Use quand l'utilisateur veut fermer, clore, ranger ou faire le ménage dans ses sessions Claude Code ouvertes en arrière-plan (jobs, sessions bg, sessions sœurs) — déclenché par "/fermer-sessions", "ferme mes sessions", "clos les sessions", "aide-moi à fermer mes sessions", "je vois encore les sessions", "range les jobs". Pas pour clore UNIQUEMENT la session en cours : ça, c'est /bye.
---

# /fermer-sessions — clore les sessions arrivées au bout de leur raisonnement

Une session se ferme quand **plus rien n'y est en suspens**. Jamais sur son âge,
jamais parce qu'elle est « au repos » : au repos veut dire « attend », pas « fini ».
Une vieille session peut être finie ; une récente peut encore porter des scripts
restés dans son dossier temporaire.

Tu ne lis pas l'état d'une session de l'extérieur : **tu le lui demandes**.

## 1. Lister

Deux familles, toutes deux visibles dans la liste de l'utilisateur :
- **vivantes** : `ListAgents` (écarte ta propre session) ;
- **terminées** (`"status": "done"` dans `~/.claude/jobs/<id>/state.json`) : `ListAgents`
  ne les montre PAS, et elles ne répondent plus. Leur bilan se fait **par les fichiers**
  (agent en lecture seule) : fin de `timeline.jsonl` (fini ou interrompu ?), note dans
  `<vault>/06_Claude/sessions/` (là où `/session-note` écrit), livrables seulement
  dans `tmp/` sans copie ailleurs. Puis étapes 3-4.
- Dossier sans `state.json` : jetable si son `tmp/` ne contient que des profils navigateur.

Si rien dans les deux familles : dis-le, propose `/bye` pour celle-ci, arrête-toi.

## 2. Demander le bilan à chacune (SendMessage, en parallèle)

Message identique pour toutes, première ligne explicite :

```
Bilan d'état demandé par l'utilisateur avant de fermer les sessions :
ne lance rien, ne ferme rien, réponds juste.
Réponds-moi (SendMessage vers « <nom de ta session> ») en 4 lignes max :
1. FINI / EN ATTENTE DE L'UTILISATEUR / INACHEVÉ
2. Ce qui reste en suspens (modifs non commitées, question sans réponse,
   livrable partiel) — ou « rien »
3. Une note de session a-t-elle déjà été écrite (oui/non) ?
4. Peut-on la clore avec /bye sans rien perdre (oui/non + pourquoi) ?
   Signale tout fichier qui ne vit que dans le tmp du job.
```

Annonce à l'utilisateur chaque réponse au fil de l'eau, en une ligne. N'agis qu'une
fois **toutes** les réponses reçues (ou une session muette signalée comme telle).

## 3. Sélectionner (ta proposition)

| Réponse | Proposition |
|---|---|
| /bye déjà fait, rien en suspens | ✅ à fermer |
| Sûre, pas de note | ✅ à fermer, après /bye |
| Un fichier ne vit que dans `$CLAUDE_JOB_DIR/tmp` | ✅ à fermer, après copie puis /bye |
| INACHEVÉ (travail en cours, non commité) | ⛔ à garder, dire ce qui manque |

Montre à l'utilisateur un tableau court : session · état · ta proposition · ce qu'il
lui restera à faire.

## 4. Demander à l'utilisateur — rien ne se ferme sans son choix

`AskUserQuestion`, `multiSelect: true` : une option par session proposée ✅
(nom + état en une ligne). 4 options maximum par question : au-delà, découpe en
plusieurs questions. Les sessions ⛔ ne sont pas proposées ; s'il en réclame une,
rappelle ce qui serait perdu et attends un oui explicite.

Ne ferme **que** les sessions qu'il a cochées.

## 5. Préparer les sessions choisies

| Cas | Action |
|---|---|
| /bye déjà fait | rien |
| Pas de note | SendMessage « lance /bye » + gestes de l'utilisateur pour « À faire » |
| Fichier dans le tmp du job | le faire **COPIER** vers un dossier de projet durable, puis /bye |

Dans tout ordre de /bye, écrire : **n'envoie aucun mail, ne fusionne rien, ne
lance aucun sudo** — ce sont les gestes de l'utilisateur.

Attends la confirmation de chaque /bye (chemin de la note), puis vérifie sur disque :
la présence de la note dans `<vault>/06_Claude/sessions/` et des copies.

## 6. Fermer

Trouver les ids : chaque `~/.claude/jobs/<id>/state.json` porte le nom de la session.

```bash
for d in ~/.claude/jobs/*/; do id=$(basename "$d"); n=$(python3 -c "import json;print(json.load(open('$d/state.json')).get('name',''))" 2>/dev/null); echo "$id  $n"; done
```

Deux noms proches (« pdf text extraction » et « … debugging ») : prendre celui qui
correspond exactement à la ligne `ListAgents`.

- `claude stop <id>` : arrête, garde la conversation (`claude attach <id>` pour reprendre).
  **La session reste visible dans la liste.**
- `claude rm <id>` : retire de la liste, **définitif**. Le garde-fou de permissions
  le refuse depuis une session : donne la boucle à l'utilisateur, à lancer avec `!` :

```
! for id in <id1> <id2> …; do claude rm $id; done
```

Sans option, `rm` refuse de jeter un worktree aux commits non poussés : ne
**jamais** ajouter `--discard-unpushed` ni `--force-remove-worktree` de toi-même.

## 7. Finir

Vérifie (`ls ~/.claude/jobs | grep -c <ids>` = 0, livrables présents), puis donne
à l'utilisateur **la liste regroupée de ses gestes**, le plus urgent en premier
(échéance datée), et propose `/bye` pour la session en cours.

## Pièges

| Piège | Réalité |
|---|---|
| « Elle est vieille / au repos, je ferme » | Seul le bilan dit si c'est fini. |
| « Évident, je ferme sans demander » | L'utilisateur coche, toi tu proposes. Toujours. |
| `claude ps` | N'existe pas : la CLI le prend pour un prompt et répond à côté. |
| `TaskStop <nom>` | Ne voit que tes propres tâches, pas les sessions sœurs. |
| « stop a suffi » | Non : stop laisse la session dans la liste. Il faut rm. |
| Contourner le refus de `rm` | Interdit : c'est le geste de l'utilisateur, donne-lui la commande. |
| Supprimer avant la fin des /bye | Le tmp du job part avec la session. |
