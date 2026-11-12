# 01 — AGENTS.md : ce que Codex lit à chaque session

`AGENTS.md` joue le rôle de `CLAUDE.md` : un texte que l'agent lit au démarrage.
Mettez-y ce qu'il ne peut pas deviner : langue, méthode, interdits, commandes.

## Où il est lu

| Fichier | Pour qui |
|---|---|
| `~/.codex/AGENTS.md` | Vous, dans toutes vos sessions |
| `<projet>/AGENTS.md` | Le projet, partagé avec l'équipe |
| `<projet>/<module>/AGENTS.md` | Le module |

Codex part de la racine du projet et descend jusqu'au dossier où vous l'avez lancé.
Il assemble les fichiers dans cet ordre : **le plus proche parle en dernier** et l'emporte.
Un `AGENTS.override.md` remplace l'`AGENTS.md` du même dossier.

**Limite : 32 Ko au total** par défaut (`project_doc_max_bytes`). Au-delà, la fin
est coupée sans prévenir. Restez court.

## Faire

1. Copiez `modeles/AGENTS.md.utilisateur` vers `~/.codex/AGENTS.md`.
2. Remplissez les `<...>`.
3. Nouvelle session : « qu'est-ce que tu sais de moi ? ».

## Vous avez déjà un CLAUDE.md ?

Le contenu passe tel quel. Deux choix :
- **copier** : `cp ~/.claude/CLAUDE.md ~/.codex/AGENTS.md`, puis adapter les chemins ;
- **un seul fichier pour les deux** dans un projet : ajoutez dans `~/.codex/config.toml`
  `project_doc_fallback_filenames = ["CLAUDE.md"]`. Codex lira `CLAUDE.md` quand
  `AGENTS.md` manque.

Les imports `@fichier` de Claude Code ne sont **pas** compris par Codex : recopiez
le contenu importé.

## Réussi si

Une nouvelle session répond juste à « qu'est-ce que tu sais de moi ? ».

## Retirer

Supprimez `~/.codex/AGENTS.md`.
