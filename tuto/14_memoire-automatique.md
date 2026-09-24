# 14 — Mémoire automatique : ce que Claude note tout seul

## Deux mémoires

| | CLAUDE.md | Mémoire automatique |
|---|---|---|
| Qui écrit | vous | Claude |
| Contenu | instructions, règles | ce qu'il a appris de vous et du projet |
| Où | `~/.claude/CLAUDE.md`, `<projet>/CLAUDE.md` | `~/.claude/projects/<projet>/memory/` |
| Chargé | chaque session, en entier | chaque session, l'index seulement |

La mémoire automatique est **active par défaut**. Quand vous lisez « Saved 2 memories »
ou « Recalled 1 memory », c'est elle.

## Ce que Claude y met

Quatre types, notés en frontmatter :
- `user` : votre rôle, vos préférences de travail ;
- `feedback` : une correction que vous lui avez faite, ou une approche que vous avez validée ;
- `project` : un état d'avancement, une décision, une échéance que le code ne dit pas ;
- `reference` : où trouver une info externe (un tableau de bord, un ticket).

Il **n'y met pas** ce qu'il peut relire dans le code ou dans vos CLAUDE.md.

## La structure qui tient dans le temps

```
~/.claude/projects/<projet>/memory/
├── MEMORY.md            ← l'index : UNE ligne par mémoire, c'est lui qui est chargé
├── user_role.md         ← une mémoire = un fichier = un fait
├── feedback_tests.md
└── project_deploiement.md
```

Règle d'or : **l'index reste court** (200 lignes ou 25 Ko, au-delà c'est coupé). Le
détail va dans les fichiers de sujet, que Claude ouvre à la demande. Un fait par
fichier. Une ligne d'index par fichier, avec un crochet qui dit pourquoi ça compte.

Cette discipline est celle d'un bon carnet : l'index se lit en dix secondes, chaque
page se retrouve.

## Piloter

- `/memory` : voir les fichiers de mémoire, ouvrir le dossier, activer/désactiver.
- « Retiens que les tests demandent un Redis local » → va en mémoire automatique.
- « Ajoute ça au CLAUDE.md » → va dans le CLAUDE.md. Deux destinations différentes.
- Relisez la mémoire **une fois par mois**. Supprimez ce qui est faux ou périmé : un
  fichier, un `rm`. Une mémoire fausse coûte plus cher qu'une mémoire absente.
- Désactiver : `"autoMemoryEnabled": false` dans `settings.json`, ou la variable
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`.

## Piège

La mémoire est **par dépôt git** (tous les worktrees d'un même dépôt la partagent) et
**par machine**. Elle ne suit pas dans le cloud ni sur un autre ordinateur. Ce qui doit
voyager va dans le vault ou dans le CLAUDE.md commité.

## Exercice

1. Dans un projet : « retiens que je préfère les messages de commit en français ».
2. `/memory` → ouvrez le dossier. Lisez `MEMORY.md` et le fichier créé.
3. Nouvelle session, demandez un commit. ✅ Réussi s'il est en français sans le redire.
4. Modifiez le fichier à la main (changez la préférence). Nouvelle session. Vérifiez.
