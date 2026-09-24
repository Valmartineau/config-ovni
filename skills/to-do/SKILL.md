---
name: to-do
description: Use quand l'utilisateur verse une idée ou une tâche dans sa file — capture, transformation en objectif exécutable sans lui, notation ICE, classement dans ~/todo/todo.md. Déclenché par "/to-do", "ajoute à ma to-do", "note cette idée", "j'ai une idée pour X", "mets ça dans la file".
argument-hint: "<l'idée, telle qu'elle vient>"
---

# /to-do — capture, transformation, classement

L'utilisateur te donne une idée telle qu'elle lui vient. Tu la rends **exécutable par
quelqu'un qui n'aura pas accès à cette conversation**, tu la notes, tu la classes.
Puis tu te tais.

## Préalable — la boussole doit exister

Lis `~/todo/objectifs.md`. S'il est absent ou vide : **arrête-toi**. Dis que la
boussole n'est pas posée et que sans elle le classement est arbitraire. Propose de la
créer avec trois questions : objectifs mesurables du trimestre · indicateurs ·
anti-signaux (ce qu'on refuse de faire même si c'est tentant). N'écris rien dans
`todo.md` avant.

## 1. Questionner, si nécessaire

Il te faut, avant d'écrire :

| Info | Pourquoi elle bloque |
|---|---|
| **Ce qui doit exister à la fin** | Sinon l'exécutant optimise dans le vide. |
| **Le dépôt ou le dossier concerné** | Sans lieu, pas d'action. |
| **Comment on saura que c'est fait** | Sans critère vérifiable, l'exécutant s'auto-valide. |
| **Ce qu'il ne faut surtout pas toucher** | Le garde-fou rend l'autonomie tenable. |

Questions fermées, une à la fois. Ne pose une question que si la réponse change ce
que tu écris.

## 2. Transformer l'idée en objectif

Chaque entrée contient :

- **OBJECTIF** — ce qui doit exister à la fin, constatable, pas une intention.
- **GARDE-FOUS** — ce que l'exécution ne fait pas pour y arriver.
- **CRITÈRES D'ACCOMPLISSEMENT** — vérifiables **sans l'utilisateur**.
- **MICRO-TÂCHES** — dans l'ordre.

Un critère acceptable est **exécutable** : une commande et sa sortie attendue.
- ✅ `npm test 2>&1 | tail -1` → `Tests: 14 passed`
- ✅ `test -f app/api/route.ts && echo present` → `present`
- ❌ « le formulaire marche » — invérifiable sans un humain.
- ❌ « le code est propre » — invérifiable tout court.

Si tu ne trouves pas de critère exécutable, l'objectif est mal découpé : repose une
question ou découpe en deux entrées.

## 3. Noter (ICE)

Impact (1-5) × Confiance (1-5) × Facilité (1-5). Recoupe avec `objectifs.md` :
une idée hors boussole reçoit Impact ≤ 2, et tu le dis.

## 4. Classer

Ajoute l'entrée dans `~/todo/todo.md`, section `## File` triée par score décroissant.
Format :

```markdown
### [ICE 60] <titre court>  — ajouté <AAAA-MM-JJ>
**Objectif** : …
**Garde-fous** : …
**Critères** :
- `<commande>` → `<sortie attendue>`
**Micro-tâches** :
1. …
```

## 5. Confirmer

Une ligne : titre, score, position dans la file. Rien d'autre.
