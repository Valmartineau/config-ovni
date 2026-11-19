# 00 bis — Savoir prompter : une nouvelle façon d'utiliser le langage

C'est la **première brique d'apprentissage**. Tout le reste du kit (CLAUDE.md, skills,
sous-agents) n'est que du prompt rangé quelque part. Si vous ne lisez qu'une fiche
avant d'installer quoi que ce soit, lisez celle-ci.

## L'expérience, en deux minutes

Prenez un mot. N'importe lequel. Disons « chat ».

```
Parle-moi d'un chat.
```
Résultat : générique. Ce que tout le monde aurait obtenu.

```
Tu es un astrophysicien insomniaque qui observe son chat à 3 h du matin
en pensant à la mort thermique de l'univers. Parle-moi de ce chat.
```
Résultat : totalement différent.

**La machine n'est pas devenue plus intelligente. La question est devenue meilleure.**

## Pourquoi : un autre rapport au langage

**Avec un humain, on négocie le sens.** L'autre interprète, comble les manques, pose
des questions, sent quand quelque chose cloche. Vous n'êtes pas seul à travailler.

**Avec une machine, on formule.** Un modèle de langage ne comprend pas : il calcule la
suite la plus probable de votre texte. Il prend vos mots à la lettre.

Conséquence : **les mots ne sont pas des décorations, ce sont des coefficients.**
Chaque mot ajouté déplace le résultat. Une contrainte bien posée élimine des milliers
de mauvaises réponses.

Écrire un prompt, ce n'est donc pas être poli avec la machine. **C'est poser un
problème.** Un énoncé mal posé donne une mauvaise réponse : le calcul n'est pas faux,
c'est la question qui l'était.

Le prompt engineering n'est pas une compétence de code. C'est une **compétence de
pensée**, la même que pour un brief, un cahier des charges, une note de cadrage.
Elle s'apprend.

## Un prompt, c'est un petit cahier des charges

Cinq blocs. Chacun répond à une question.

| Bloc | La question | Exemple |
|---|---|---|
| **Rôle** | Qui parle ? | « Tu es un expert du GIEC. » |
| **Contexte** | Pour qui, dans quelle situation ? | « Je suis maire d'une ville côtière, je dois décider d'un plan d'urbanisme. » |
| **Tâche** | Quoi, exactement ? Une seule demande. | « Explique le lien entre fonte des glaces et montée des océans. » |
| **Contraintes** | Dans quelles limites ? | « Sans jargon. Rien que tu ne puisses pas sourcer. » |
| **Format** | Sous quelle forme ? | « Trois points, une phrase chacun. » |

Comparez avec : « Explique-moi le changement climatique. » Même machine, même sujet.

**La règle qui sert tous les jours :** un bloc que vous ne savez pas remplir, c'est
**une question que vous ne vous êtes pas encore posée**. Ou une question à poser à
votre client.

> Quand on ne sait pas formuler pour la machine, c'est souvent qu'on ne sait pas
> encore exactement ce qu'on veut.

## Le contexte : ce que la machine ne peut pas deviner

C'est le bloc qui manque le plus souvent, et celui qui change le plus le résultat.

- **Pour qui** est le résultat, et ce que cette personne sait déjà.
- **Pour quoi faire** : la décision ou l'usage derrière la demande.
- **Ce qui existe déjà** : le document, le code, le brouillon. Montrez-le, ne le décrivez pas.
- **Ce que vous avez déjà essayé**, et pourquoi ça n'allait pas.
- **Un exemple** de ce que vous trouvez réussi.
- **Ce qu'il ne faut pas toucher.**

À l'inverse, n'ajoutez pas ce qui ne sert pas la demande : le contexte inutile déplace
le résultat lui aussi.

## La question : une seule, et vérifiable

- **Une demande à la fois.** Trois demandes dans un prompt donnent trois réponses moyennes.
- **Un verbe précis** : comparer, résumer, critiquer, réécrire, lister. Pas « regarde ça ».
- **Un critère de réussite** : comment saurez-vous que la réponse est bonne ?

## Le prompt retourné : faire poser les questions

Quand vous ne savez pas par où commencer, inversez les rôles :

```
Je veux <mon objectif>. Avant de répondre, pose-moi les questions qui te
manquent, une seule à la fois. Attends ma réponse avant la suivante.
```

La machine vous fait écrire votre cahier des charges.

## Itérer : corriger la question, pas la réponse

1. **À la main d'abord.** Écrivez en deux lignes ce que vous attendez, avant de demander.
2. **Demandez.**
3. **Lisez l'écart** entre ce que vous attendiez et ce que vous avez reçu.
4. **Corrigez le prompt.** L'écart vous dit quel bloc manquait.

Ce que vous gardez à la fin, ce n'est pas la réponse. C'est **le prompt qui marche**.

## Dans Claude Code : où vont vos prompts

Les briques du kit sont des prompts rangés au bon endroit.

| Ce que vous répétez | Où le ranger | Tuto |
|---|---|---|
| Le contexte valable à chaque session (qui vous êtes, votre méthode, vos interdits) | `CLAUDE.md` | `01_claude-md` |
| Un prompt qui marche, utile de temps en temps | un **skill** | `02_skills` |
| Un rôle contraint (relecteur, critique) | un **sous-agent** | `13_sous-agents` |
| Le contexte d'un seul dossier | une **règle par chemin** | `16_regles-par-chemin` |

Le `CLAUDE.md`, c'est le contexte que vous n'aurez plus jamais à retaper.

## Trois pièges

1. **Croire la réponse.** La machine prédit, elle ne sait pas. Une réponse bien écrite
   peut être fausse. Vérifiez ce qui compte.
2. **Corriger la réponse à la main** au lieu de corriger la question. Vous referez le
   même travail demain.
3. **Tout mettre.** Un prompt long n'est pas un prompt précis.

## Ce qui sort

Tout ce que vous écrivez dans un prompt **part au modèle**, contexte compris. Ne collez
pas de données personnelles d'un tiers, ni de secret, pour « donner du contexte ».

## Exercice

1. Choisissez un mot. Écrivez le prompt nu, puis le prompt en cinq blocs. Comparez.
2. Prenez une vraie demande de votre semaine. Écrivez **à la main** ce que vous attendez.
   Demandez. Notez l'écart en une ligne. Corrigez le prompt, pas la réponse.
3. Essayez le **prompt retourné** sur un sujet flou.
4. Votre meilleur prompt de la semaine : rangez-le dans un skill (`02_skills`).

## D'où ça vient

Cette fiche reprend la conférence gesticulée d'OVNI Conseil, « Penser avec les
machines : langage, responsabilité et créativité ». La conférence se donne en public :
https://ovniconseil.fr/conferences
