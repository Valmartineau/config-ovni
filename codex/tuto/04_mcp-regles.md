# 04 — Réglages, règles et MCP

Tout se règle dans **un seul fichier** : `~/.codex/config.toml`.
Le modèle commenté est dans `modeles/config.exemple.toml`.

## Ce que Codex peut faire sans demander

| Réglage | Valeurs | Conseil |
|---|---|---|
| `approval_policy` | `on-request`, `never` | `on-request` : Codex demande avant ce qui sort du cadre |
| `sandbox_mode` | `read-only`, `workspace-write`, `danger-full-access` | `workspace-write` : il écrit dans le projet, pas ailleurs |

Ne mettez **jamais** `danger-full-access` avec `never` sur votre machine de travail.

## Les règles de commandes

Un fichier `.rules` dans `~/.codex/rules/` dit, commande par commande :
`allow` (sans demander), `prompt` (demander), `forbidden` (jamais).

```
prefix_rule(
    pattern = ["git", "push", "--force"],
    decision = "forbidden",
    justification = "Le push forcé reste un geste humain.",
)
```

Le kit en propose un : `modeles/rules/garde-fou.rules`. Redémarrez Codex après
l'avoir copié. Quand vous acceptez une commande « pour toujours », Codex l'écrit
dans `~/.codex/rules/default.rules` : relisez ce fichier une fois par mois.

## La status line

Codex n'accepte pas de script personnel. Tapez `/statusline` pour choisir
et ordonner les éléments du bas (modèle, contexte, limites, git…).

## MCP : brancher un outil

Un serveur MCP donne à Codex des outils externes. **Un seul à la fois**,
et seulement après avoir répondu à trois questions :
où vont mes données, qui les garde, comment je repars sans lui.

En ligne de commande :

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

Ou à la main, dans `~/.codex/config.toml` :

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]

[mcp_servers.notion]
url = "https://mcp.notion.com/mcp"
```

Vous avez des serveurs dans Claude Code ? Recopiez chaque entrée de `.mcp.json`
en table `[mcp_servers.<nom>]` : `command`, `args`, `env` ou `url`.

## La mémoire

Codex peut garder des souvenirs entre les sessions. C'est **coupé par défaut**.
Pour l'activer : `[features] memories = true`. Les fichiers restent dans `~/.codex/`.
Relisez-les comme vous relisez votre `AGENTS.md`.

## Réussi si

Vous savez dire, pour chaque ligne de votre `config.toml`, ce qu'elle autorise.

## Retirer

Supprimez la ligne ou la table concernée, ou le fichier `.rules`.
