# 03 — Hooks : automatiser autour de Claude Code

## C'est quoi

Un **hook** est une commande que Claude Code lance **lui-même** quand un événement
se produit : début de session, fin de réponse, avant ou après chaque outil…

Différence fondamentale avec le CLAUDE.md et les skills : ceux-là sont des
**instructions** que Claude peut suivre ou oublier. Un hook est **exécuté par le
programme**, pas par le modèle. Si vous voulez qu'une chose arrive à coup sûr
(un journal, une interdiction), c'est un hook, pas une phrase dans CLAUDE.md.

## Les événements

Les plus utiles pour commencer :

| Événement | Quand | Usage typique |
|---|---|---|
| `SessionStart` | ouverture d'une session | injecter du contexte (état du vault, date…) |
| `UserPromptSubmit` | vous envoyez un message | enrichir le message, rappeler une mémoire |
| `PreToolUse` | juste avant un outil | **bloquer** (exit 2) une commande dangereuse |
| `PostToolUse` | juste après un outil | journaliser, formater, lancer un lint |
| `Stop` | Claude a fini de répondre | synchroniser, notifier, écrire dans le journal |
| `SessionEnd` | fermeture | archiver |
| `Notification` | Claude attend une permission ou vous appelle | son, notification bureau |
| `PreCompact` / `PostCompact` | résumé de contexte | sauvegarder l'état avant perte |

Il en existe une trentaine (`SubagentStart`, `PermissionRequest`, `FileChanged`…).
`/hooks` dans Claude Code liste ceux qui sont actifs et d'où ils viennent.

## La forme, dans `settings.json`

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/obsidian_daily.py",
            "timeout": 10,
            "statusMessage": "Journal Obsidian..."
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "python3 ~/.claude/hooks/garde_fou.py", "timeout": 5 }
        ]
      }
    ]
  }
}
```

- `matcher` : filtre sur le nom de l'outil (`Bash`, `Write|Edit`, `*`). Absent = tout.
- `timeout` : secondes avant abandon.
- `statusMessage` : ce qui s'affiche pendant l'exécution.
- `async: true` : le hook tourne **en arrière-plan**, sans bloquer Claude. À utiliser
  pour tout hook qui observe ou publie. À **ne pas** utiliser pour un hook qui doit
  bloquer : un `PreToolUse` async perd le droit d'interdire.

Mesure vécue : un hook synchrone sur `PreToolUse` avec `matcher: "*"` qui prenait
1,5 s ralentissait **chaque** appel d'outil de 1,5 s. Sur une session de 200 outils,
5 minutes perdues. Mesurez vos hooks en isolation, pas « à l'œil ».

## Le contrat entrée / sortie

Le hook reçoit un **JSON sur stdin** (événement, session, outil, ses arguments…).
Il répond par son **code de sortie** et, éventuellement, du JSON sur stdout :

- **exit 0** : tout va bien. Sur `SessionStart` et `UserPromptSubmit`, ce que le hook
  imprime est **ajouté au contexte** de Claude. Forme structurée :
  ```json
  {"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"…"}}
  ```
- **exit 2** : **bloque** l'action (l'outil n'est pas lancé, le message est refusé).
  Le texte sur stderr est montré à Claude comme raison.
- autre code : erreur non bloquante, affichée, l'action continue.

## Les 3 hooks du kit

| Fichier | Événement | Ce qu'il fait |
|---|---|---|
| `obsidian_session_start.py` | SessionStart | Dit à Claude si la daily note du jour existe, et lui rappelle d'archiver la session en fin de phase |
| `obsidian_daily.py` | Stop | Ajoute (ou incrémente) une ligne « Claude Code » dans la daily note du jour, une par heure |
| `garde_fou.py` | PreToolUse (Bash) | Refuse (exit 2) les commandes destructrices évidentes : `rm -rf /`, `rm -rf ~`, `git push --force` sur main |

Les deux premiers lisent le chemin du vault dans `~/.claude/kit.json` :
```json
{ "vault": "/Users/vous/Documents/Vault" }
```

**Testez-les à la main avant de les brancher** :
```bash
echo '{}' | python3 ~/.claude/hooks/obsidian_session_start.py
echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}' | python3 ~/.claude/hooks/garde_fou.py ; echo "code de sortie: $?"
```
Le second doit afficher un refus et `code de sortie: 2`.

Sur Windows : `python` à la place de `python3` si `python3` n'existe pas ; chemins
avec des `/`, jamais des `\`.

## La status line (même famille)

La status line est la ligne en bas de l'écran. Comme un hook, c'est **un script que
Claude Code lance** (toutes les 30 s ou à chaque changement) en lui passant un JSON :
modèle, dossier, `context_window.used_percentage`, `rate_limits.five_hour`,
`rate_limits.seven_day`, `transcript_path`…

Le kit fournit `statusline/statusline.py` : dossier, branche git, modèle, jauge de
contexte, quotas 5 h / 7 j avec temps avant remise à zéro, heure d'ouverture de la
session, nombre de notes de session du jour. Tout en toutes lettres : la ligne se lit
sans légende. `/statusline-aide` la traduit quand même.

Réglage dans `settings.json` :
```json
"statusLine": { "type": "command", "command": "python3 ~/.claude/statusline.py", "padding": 0, "refreshInterval": 30 }
```

## Écrire le vôtre

1. Choisissez l'événement. Question test : « est-ce que ça doit arriver **à coup
   sûr**, ou est-ce que Claude peut décider ? » À coup sûr = hook.
2. Écrivez-le en Python (JSON natif, portable Mac/Windows/Linux).
3. Lisez stdin, faites une seule chose, sortez vite. Timeout court.
4. Testez avec `echo '{…}' | python3 monhook.py`.
5. Branchez dans `settings.json`. Vérifiez avec `/hooks`.
6. Mesurez le coût s'il est sur `PreToolUse`/`PostToolUse`.

## Retirer

Supprimez le bloc correspondant dans `settings.json` (ou `"disableAllHooks": true`
pour tout couper d'un coup), puis le fichier dans `~/.claude/hooks/`.
