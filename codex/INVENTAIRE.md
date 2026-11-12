# Inventaire : la Config OVNI, de Claude Code à Codex

Établi le 12 novembre 2026 à partir de la documentation de Codex (version 0.167).
Chaque élément du kit Claude Code, et ce qu'il devient chez Codex.

**Légende.** ✅ passe tel quel · 🔧 adapté · ❌ ne passe pas

| Élément du kit Claude | Chez Codex | État | Ce qui change |
|---|---|---|---|
| `~/.claude/CLAUDE.md` | `~/.codex/AGENTS.md` | ✅ | Même rôle, même cascade (dossier personnel, projet, module). Limite de 32 Ko. Pas d'import `@fichier`. |
| `CLAUDE.md` d'un projet | `AGENTS.md` du projet | ✅ | Ou `project_doc_fallback_filenames = ["CLAUDE.md"]` pour un seul fichier commun. |
| 9 skills : `porte`, `lisible`, `session-note`, `bye`, `to-do`, `micom`, `audit-acces`, `souverainete-check`, `animejs` | `~/.agents/skills/` | 🔧 | Même `SKILL.md`. Appel par `$nom` au lieu de `/nom`. `$ARGUMENTS` réécrit. « Seulement à la demande » passe dans `agents/openai.yaml`. |
| Skill `fermer-sessions` | — | ❌ | Il pilote les sessions d'arrière-plan de Claude Code, qui n'existent pas chez Codex. |
| Skill `statusline-aide` | — | ❌ | Il explique la status line par script, que Codex n'accepte pas. |
| Hook `garde_fou.py` (avant une commande) | `PreToolUse`, outil `Bash` | ✅ | Même entrée JSON, même code 2 pour bloquer. Codex demande d'approuver le hook dans `/hooks`. |
| Hook `obsidian_session_start.py` | `SessionStart` | ✅ | Même `additionalContext`. Chemin du réglage : `~/.codex/kit.json`. |
| Hook `obsidian_daily.py` (fin de tour) | `Stop` | 🔧 | La ligne de la note du jour dit « Codex ». Codex exige du JSON en sortie : déjà le cas. |
| Bloc `hooks` de `settings.json` | `~/.codex/hooks.json` | 🔧 | Même structure. Chemins complets conseillés à la place de `~`. |
| Permissions `allow` / `deny` | `approval_policy`, `sandbox_mode`, fichiers `.rules` | 🔧 | Autre logique : un bac à sable + des règles par début de commande (`allow`, `prompt`, `forbidden`). Modèle : `modeles/rules/garde-fou.rules`. |
| Status line `statusline.py` | `/statusline` | ❌ | Codex propose une liste d'éléments à choisir (modèle, contexte, limites, git). Pas de script personnel. |
| Sous-agent `relecteur.md` | `~/.codex/agents/relecteur.toml` | 🔧 | Format TOML. **Il hérite des droits de la session** : l'interdiction d'écrire n'est plus garantie par l'outil. Relire en `codex --sandbox read-only`. |
| MCP (`claude mcp add`, `.mcp.json`) | `codex mcp add`, `[mcp_servers.<nom>]` dans `config.toml` | 🔧 | Mêmes serveurs. Recopier `command`, `args`, `env` ou `url`. |
| Mémoire automatique | `[features] memories = true` | 🔧 | Coupée par défaut chez Codex. Fichiers locaux dans `~/.codex/`. |
| Vault Obsidian, notes de session | Identique | ✅ | Le même vault sert aux deux outils. La note du jour reçoit une rubrique « Sessions Codex ». |
| Charte Micom | `~/.codex/micom/charte.md` | ✅ | Même gabarit. |
| `outils/verifier.py` | `outils/verifier.py` (version Codex) | 🔧 | Vérifie `~/.codex` et `~/.agents/skills`. |
| Plugins (`/plugin`, `superpowers`) | — | ❌ | Pas repris dans cette version. Les skills d'un plugin passent un par un, s'ils n'utilisent pas d'outil propre à Claude Code. |
| `claude -p`, `claude agents`, sessions d'arrière-plan | — | ❌ | Non couverts par ce kit. |

## Bilan

- **Passe tel quel : 6.** Les consignes, deux hooks sur trois, le vault, la charte.
- **Adapté : 8.** Les skills, le journal Obsidian, les réglages, le sous-agent, les MCP, la mémoire.
- **Ne passe pas : 5.** Deux skills, la status line par script, les plugins, les sessions d'arrière-plan.

## Ce qui est vérifié, et ce qui ne l'est pas

- **Fait ici** : la conversion automatique (aucun reste propre à Claude Code),
  les hooks exercés avec des entrées au format Codex, les fichiers TOML et JSON relus
  par un programme.
- **Pas encore validé dans un vrai Codex** : le chargement des skills, l'approbation
  des hooks, le fichier de règles, le sous-agent, et l'installation sous Windows.
  À confirmer au premier essai, avec `outils/verifier.py`.
