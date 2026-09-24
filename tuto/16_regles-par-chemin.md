# 16 — Règles par chemin : des instructions qui ne se chargent qu'au besoin

## Le problème

Le `CLAUDE.md` d'un projet grossit. À 300 lignes, Claude suit moins bien, et chaque
session paie ces lignes en contexte, même pour une tâche qui n'en touche que 10.

## La solution : `.claude/rules/`

Des fichiers markdown, un sujet par fichier, dans `<projet>/.claude/rules/` :

```
mon-projet/
├── CLAUDE.md               ← court : lancer, tester, les 5 règles universelles
└── .claude/rules/
    ├── style.md            ← chargé toujours (pas de paths)
    ├── api.md              ← chargé seulement quand Claude touche src/api/
    └── tests.md            ← chargé seulement sur les fichiers de test
```

Sans frontmatter, une règle est chargée au démarrage, comme le CLAUDE.md.
Avec `paths:`, elle ne se charge que **quand Claude lit un fichier qui correspond** :

```markdown
---
paths:
  - "src/api/**/*.ts"
---
# Règles API
- Toute route valide ses entrées.
- Format d'erreur standard : { code, message }.
- Un commentaire OpenAPI par route.
```

Motifs : `**/*.py` (tous les Python), `src/**/*` (tout sous src), `*.md` (racine),
`src/**/*.{ts,tsx}` (plusieurs extensions), plusieurs lignes possibles.

Niveau utilisateur : `~/.claude/rules/` fonctionne pareil, pour tous vos projets.

## Quand découper

| Contenu | Où |
|---|---|
| « toujours faire X », commandes de build | `CLAUDE.md` |
| règle valable pour un seul dossier ou type de fichier | `.claude/rules/x.md` avec `paths` |
| procédure en plusieurs étapes | un **skill** |
| ce qui doit arriver à coup sûr | un **hook** |

## Vérifier

`/context` dans une session liste les fichiers de mémoire chargés. Ouvrez un fichier
de `src/api/`, relancez `/context` : la règle `api.md` apparaît.

## Le kit fournit

`modeles/rules/exemple-tests.md` : une règle scoped sur les fichiers de test, à
adapter. Copiez-la dans `.claude/rules/` d'un projet et vérifiez avec `/context`.

## Exercice

1. Prenez un projet avec un `CLAUDE.md` de plus de 80 lignes.
2. Sortez tout ce qui ne concerne qu'un dossier dans une règle avec `paths`.
3. Le `CLAUDE.md` doit tenir sous 60 lignes. Vérifiez avec `/context` que la règle
   n'apparaît qu'en touchant le bon dossier.
