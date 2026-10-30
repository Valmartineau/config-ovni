# 02 — Skills : apprendre un savoir-faire à Claude

## C'est quoi

Un **skill** est un dossier avec un fichier `SKILL.md` : des instructions en
markdown que Claude charge **quand il en a besoin** (ou quand vous tapez `/nom`).

Différence avec `CLAUDE.md` : le CLAUDE.md est lu à chaque session, en entier.
Un skill n'est chargé que **si la tâche le réclame**. C'est ce qui permet d'avoir
50 savoir-faire sans saturer le contexte : Claude ne voit que la ligne `description`
de chacun, et ouvre le bon au bon moment.

## Où ça vit

| Emplacement | Portée |
|---|---|
| `~/.claude/skills/<nom>/SKILL.md` | Vous, tous vos projets |
| `<projet>/.claude/skills/<nom>/SKILL.md` | Ce projet, toute l'équipe (commité) |
| plugin | Distribué, versionné (voir `08_plugins.md`) |

Le nom du dossier devient la commande : `~/.claude/skills/bye/` → `/bye`.

(L'ancien format `~/.claude/commands/nom.md` marche toujours. Préférez les skills :
ils acceptent des fichiers annexes.)

## Anatomie d'un SKILL.md

```markdown
---
name: session-note
description: Use quand l'utilisateur veut archiver la session en cours dans son vault — déclenché par « /session-note », « archive la session », « note de session ».
argument-hint: "[titre court optionnel]"
disable-model-invocation: false
---

# Ce que tu fais quand ce skill est chargé

1. …
2. …
```

Les champs qui comptent :

- **`description`** : la phrase la plus importante du fichier. C'est **elle** que
  Claude lit pour décider de charger le skill. Écrivez-la comme un déclencheur :
  « Use quand … — déclenché par "…", "…" ». Concrète, avec les mots que vous
  taperez vraiment.
- **`disable-model-invocation: true`** : seul l'humain peut lancer le skill (`/nom`).
  Indispensable pour tout ce qui a un effet de bord (envoyer, publier, supprimer).
- **`user-invocable: false`** : l'inverse, seul Claude peut le charger.
- **`argument-hint`** : ce qui s'affiche dans l'autocomplétion.
- **`allowed-tools`** : outils pré-autorisés pendant le skill, ex. `Bash(git *)`.

Dans le corps, `$ARGUMENTS` est remplacé par ce que vous avez tapé après `/nom`.
`${CLAUDE_SKILL_DIR}` donne le dossier du skill (pour des fichiers annexes).

## Les 11 skills du kit

| Skill | Ce qu'il fait | Qui le lance |
|---|---|---|
| `/lisible` | Réponses courtes et lisibles pour un lecteur dyslexique ou pressé | vous |
| `/session-note` | Archive la session dans votre vault Obsidian + lien daily | vous ou Claude |
| `/bye` | Clôt la session : session-note puis au revoir | vous |
| `/porte` | Autonomie bornée : Claude code seul dans un worktree, sans jamais sortir | vous seul |
| `/to-do` | Transforme une idée en objectif exécutable, avec critères vérifiables | vous |
| `/micom` | Rôle de communication : sujet → post, avec votre charte et des garde-fous | vous |
| `/statusline-aide` | Explique chaque segment de la status line | vous |
| `/audit-acces` | Audite qui peut créer, lire, modifier, supprimer quoi : matrice et test croisé | vous |
| `/souverainete-check` | Cartographie ce qui sort de votre périmètre et ce dont l'appli dépend | vous |
| `/fermer-sessions` | Ferme les sessions en arrière-plan après un bilan d'état de chacune | vous seul |
| `/animejs` | Écrit du code anime.js v4 sans syntaxe v3, avec prefers-reduced-motion | vous ou Claude |

Lisez-les. Ils sont courts, et ce sont des **exemples de ce qu'un bon skill contient** :
un déclencheur clair, un déroulé numéroté, des garde-fous, un self-check.

## Écrire le vôtre

1. Trouvez une tâche que vous répétez et que vous ré-expliquez à chaque fois.
2. `mkdir -p ~/.claude/skills/ma-tache && $EDITOR ~/.claude/skills/ma-tache/SKILL.md`
3. Écrivez la `description` en premier, avec les mots déclencheurs.
4. Déroulé numéroté. Une action par ligne. Ce qui est interdit, dites-le.
5. Testez dans une **nouvelle session** (les skills sont lus au démarrage) :
   `/ma-tache` puis, sans le nommer, une phrase qui devrait le déclencher.
6. Corrigez la description jusqu'à ce qu'il se déclenche quand il faut, et pas ailleurs.

Un skill se lit comme une fiche de poste : si un stagiaire compétent peut l'exécuter
sans vous poser de question, il est bon.

## Les skills tiers qui valent le détour

À installer vous-même, après lecture :

- **obsidian-skills** (kepano, l'auteur d'Obsidian) : `obsidian-markdown`, `obsidian-bases`,
  `json-canvas`, `obsidian-cli`. https://github.com/kepano/obsidian-skills
- **superpowers** (plugin officiel) : brainstorming, TDD, debugging systématique,
  plans, worktrees. Voir `08_plugins.md`.

## Retirer

`rm -rf ~/.claude/skills/<nom>`. Effet à la prochaine session.
