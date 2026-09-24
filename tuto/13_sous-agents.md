# 13 — Sous-agents : déléguer à un agent contraint

## C'est quoi

Un **sous-agent** est une session enfant que Claude lance pour une sous-tâche, avec
son **propre contexte**, ses **propres outils**, éventuellement son **propre modèle**.
Il rend un résumé à la conversation principale et disparaît.

Deux raisons de s'en servir :
1. **Isoler le bruit** : une recherche dans 200 fichiers ne doit pas remplir votre contexte.
2. **Contraindre** : un relecteur qui n'a que `Read` et `Grep` ne peut pas modifier le code,
   quoi qu'il « décide ».

Claude Code en a des intégrés (exploration, planification). Vous pouvez écrire les vôtres.

## Où ça vit

| Emplacement | Portée |
|---|---|
| `~/.claude/agents/<nom>.md` | vous, tous vos projets |
| `<projet>/.claude/agents/<nom>.md` | ce projet, toute l'équipe (commité) |

## Anatomie

```markdown
---
name: relecteur
description: Relit un diff ou un fichier et rend un avis structuré sans rien modifier. Use proactively après une modification importante.
tools: Read, Grep, Glob
model: sonnet
maxTurns: 8
---

Tu es relecteur. Tu ne modifies jamais rien. Pour chaque point : fichier:ligne,
le problème en une phrase, la gravité (bloquant / à corriger / suggestion).
Termine par un verdict en une ligne.
```

| Champ | Rôle |
|---|---|
| `name`, `description` | obligatoires ; la description dit **quand** déléguer |
| `tools` | liste blanche d'outils. Pas de `Edit`, pas de `Write` = lecture seule garantie |
| `disallowedTools` | l'inverse : tout sauf ceux-là |
| `model` | `haiku`, `sonnet`, `opus`… un relecteur n'a pas besoin du plus gros |
| `maxTurns` | plafond de tours : un agent qui boucle s'arrête |
| `permissionMode` | `plan` pour un agent qui ne doit rien toucher |
| `isolation: worktree` | il travaille dans une copie git isolée |
| `memory` | `project` pour qu'il garde ses propres notes entre sessions |

Le corps du fichier est son **prompt système**. Écrivez-le comme une fiche de poste.

## Invoquer

- Claude délègue **seul** quand la tâche correspond à la `description`. Le mot
  « proactively » dans la description l'y encourage.
- Explicitement : « utilise le sous-agent relecteur sur mes changements », ou
  `@relecteur regarde le module auth`.
- Toute la session : `claude --agent relecteur`.
- `/agents` liste ceux qui sont disponibles.

## Le kit fournit

`agents/relecteur.md` : lecture seule, Sonnet, 8 tours, verdict structuré.
Copiez-le dans `~/.claude/agents/` et essayez : « demande au relecteur son avis sur
`hooks/garde_fou.py` ». Il ne pourra pas le modifier, même si vous le lui demandez.

## Ce que ça enseigne

La sécurité par **construction** : on ne demande pas à l'agent d'être sage, on lui
retire les outils. C'est la même logique que le hook garde-fou, un cran plus haut.

Limite : la somme des descriptions de vos sous-agents doit rester courte (le plafond
est de 15 000 tokens). Description brève, détail dans le corps.

## Retirer

Supprimez le fichier. Effet à la prochaine session.
