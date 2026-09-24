# 08 — Plugins et marketplaces

## C'est quoi

Un **plugin** regroupe skills, hooks, agents et serveurs MCP dans un paquet
versionné, installable en une commande. Une **marketplace** est un catalogue de
plugins (un dépôt git avec un fichier d'index).

Dans Claude Code : `/plugin` ouvre le gestionnaire (parcourir, installer, activer,
désactiver). Les plugins activés sont listés dans `settings.json` sous
`enabledPlugins`, les marketplaces ajoutées sous `extraKnownMarketplaces`.

## Ceux qui ont fait leurs preuves

| Plugin | Marketplace | Pourquoi |
|---|---|---|
| **superpowers** | officielle (`anthropics/claude-plugins-official`) | Méthode : brainstorming avant de coder, TDD, debugging systématique, plans, worktrees. Change la façon de travailler. |
| **code-review** | officielle | Revue de diff ou de PR avec niveaux d'effort. |
| **frontend-design** | officielle | Évite l'interface « générée par IA » générique. |
| **code-simplifier** | officielle | Simplifie sans casser. |
| **fullstack-dev-skills** | `jeffallan/claude-skills` | ~70 skills par techno (python-pro, mcp-developer, security-reviewer…). À trier. |
| **voicemode** | `mbailey/voicemode` | Parler à Claude Code. Curiosité utile. |

Conseil : **un plugin à la fois**, et lisez ce qu'il installe (`/plugin` → détails).
Un plugin peut poser des hooks : vous devez savoir lesquels.

## Le piège du « tout installer »

Chaque skill ajoute une ligne de description au contexte de chaque session. Cent
skills = un contexte alourdi avant même votre première phrase. Gardez ce que vous
utilisez. Le reste se réinstalle en une commande.

Certains dépôts « harness » proposent de remplacer tout votre `~/.claude/`. Ne le
faites pas : **cherry-pick**. Prenez une idée, une gemme, réécrivez-la chez vous.

## Retirer

`/plugin` → désactiver ou désinstaller. Vérifiez `/hooks` après : un hook de plugin
disparaît avec lui.
