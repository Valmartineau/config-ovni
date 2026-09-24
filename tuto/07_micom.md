# 07 — Micom : un rôle de communication avec des garde-fous

## L'idée

**Micom** est un *rôle* que Claude endosse : votre chargé de communication. Il ne
sait rien de vous par défaut. Il lit une **charte** que vous écrivez (ton, cibles,
positionnement, interdits), puis déroule une **chaîne** : brief → rédaction → visuel →
programmation. À chaque étape, un garde-fou ✋ : rien ne passe à la suivante sans
votre validation. Et **jamais de publication directe**.

Ce que ça enseigne :

- Un rôle = une charte (le fond) + une chaîne (la forme) + des garde-fous (la sécurité).
- Le modèle rédige bien quand la charte est précise. Le travail, c'est la charte.
- Un pipeline avec des points d'arrêt vaut mieux qu'une IA « qui publie toute seule ».

## Installer

1. Le skill est dans `skills/micom/` → `~/.claude/skills/micom/`.
2. La charte : copiez `modeles/charte-micom.md` vers `~/.claude/micom/charte.md`
   et remplissez-la. Elle est **à vous** ; le skill la lit, ne la modifie jamais.
3. Optionnel : une config (créneaux de publication, chemin d'archive) dans
   `~/.claude/micom/config.md`.

## La chaîne

| Étape | Livrable | Garde-fou |
|---|---|---|
| 1. Brief | cible, angle, message-clé, date — en 4 lignes | ✋ valider le brief |
| 2. Rédaction | le texte, prêt à copier, conforme à la charte | ✋ valider le texte |
| 3. Visuel | une proposition (titre incrusté, image, ou rien) | ✋ valider le visuel |
| 4. Programmation | copie dans l'outil de votre choix, ou brouillon | ✋ votre geste |
| 5. Archive | le post et sa date dans votre vault | — |

Lancement : `/micom "sujet"` ou « appel Micom, écris un post sur … ».

## La charte (le vrai travail)

`modeles/charte-micom.md` a des trous à remplir :

- **Qui parle** : vous, en une phrase. Ce que vous faites, pour qui.
- **Ton** : trois adjectifs et trois interdits (« pas d'emoji », « pas de jargon »…).
- **Cibles** : trois profils, avec ce qui les préoccupe.
- **Formats** : longueur, signature, appel à l'action, hashtags oui/non.
- **Interdits absolus** : ne jamais nommer un client, un concurrent ; pas de promesse
  chiffrée non sourcée ; pas de témoignage inventé.
- **Preuves autorisées** : ce que vous acceptez de citer.

Testez la charte en faisant écrire trois posts sur trois sujets différents. Si les
trois se ressemblent trop, la charte est floue. Si l'un sort du cadre, il manque
un interdit.

## Aller plus loin

- Un visuel généré **en local** (ffmpeg + un gabarit HTML) plutôt qu'un service en ligne.
- Programmer via l'API de votre outil de publication, **avec** le garde-fou 4.
- Une rubrique récurrente : même chaîne, charte enrichie d'un gabarit de rubrique.

## Retirer

`rm -rf ~/.claude/skills/micom ~/.claude/micom`.
