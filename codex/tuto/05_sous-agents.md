# 05 — Sous-agents : un relecteur à part

Codex peut confier une tâche à un **sous-agent** : une session enfant avec ses
propres consignes. Chez Codex, un sous-agent est un fichier **TOML**, pas Markdown.

## Où

| Dossier | Portée |
|---|---|
| `~/.codex/agents/<nom>.toml` | Vous |
| `<projet>/.codex/agents/<nom>.toml` | Le projet |

Champs obligatoires : `name`, `description`, `developer_instructions`.

## Le relecteur du kit

```bash
mkdir -p ~/.codex/agents
cp agents/relecteur.toml ~/.codex/agents/
```

Nouvelle session, puis : « demande au relecteur son avis sur hooks/garde_fou.py ».

## La différence qui compte

Dans Claude Code, le relecteur **n'a pas le droit d'écrire** : la ligne `tools: Read, Grep, Glob`
le lui interdit. Chez Codex, un sous-agent **hérite des permissions** de la session
qui l'appelle. Sa consigne lui demande de ne rien modifier, mais rien ne l'en
empêche. Pour une vraie garantie, lancez la relecture dans une session en lecture seule :

```bash
codex --sandbox read-only
```

## Réussi si

Vous recevez un avis structuré et le fichier reste inchangé.

## Retirer

`rm ~/.codex/agents/relecteur.toml`
