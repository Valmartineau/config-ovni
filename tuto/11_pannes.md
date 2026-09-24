# 11 — Pannes courantes

Chaque entrée : ce que vous voyez → ce que ça veut dire → ce qui répare.
Premier réflexe, toujours : `python3 outils/verifier.py` (ou `python` sur Windows)
depuis le dossier du kit, puis `claude doctor`.

## Installation

**`claude : Le terme «claude» n'est pas reconnu…`** (PowerShell) ou
**`command not found: claude`** (Mac/Linux)
→ le dossier d'installation n'est pas dans le PATH de cette fenêtre, ou l'installation
n'est pas allée au bout.
1. Fermer et rouvrir le terminal. Souvent ça suffit.
2. Le fichier existe-t-il ?
   ```powershell
   Test-Path "$env:USERPROFILE\.local\bin\claude.exe"      # Windows → True / False
   ```
   ```bash
   ls ~/.local/bin/claude                                    # Mac / Linux
   ```
3. Il existe → ajouter au PATH :
   ```powershell
   $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
   [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
   ```
   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc    # ou ~/.bashrc
   ```
   puis rouvrir le terminal.
4. Il n'existe pas → réinstaller (`tuto/00_demarrer.md`). Sur Windows, dans
   **PowerShell**, pas CMD.

**`Jeton inattendu « \.local\bin\claude.exe »`** (PowerShell)
→ vous avez tapé un chemin avec `$env:` sans guillemets ni commande devant.
Mettez le chemin entre guillemets, derrière `Test-Path`.

**`'irm' n'est pas reconnu`** → vous êtes dans CMD, pas PowerShell. L'invite
PowerShell commence par `PS`. Ouvrez PowerShell depuis le menu Démarrer.

**`Could not establish trust relationship for the SSL/TLS`** (Windows)
→ TLS 1.2 non activé dans cette session PowerShell :
```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
irm https://claude.ai/install.ps1 | iex
```
Réseau d'école qui bloque le téléchargement → `winget install Anthropic.ClaudeCode`.

**`Not logged in · Please run /login`** → lancez `claude` sans argument et suivez
le navigateur. Le plan gratuit de claude.ai ne donne pas accès à Claude Code.

## Hooks

**Un hook ne fait rien, aucun message.**
→ `/hooks` dans Claude Code : est-il listé ? Sinon, le JSON de `settings.json` a une
erreur (virgule en trop) ou le bloc est au mauvais niveau. `claude doctor` signale
un settings invalide.
→ Testez-le à la main : `echo '{}' | python3 ~/.claude/hooks/obsidian_session_start.py`.
S'il plante ici, il plante dans Claude Code, en silence.

**`hook error` avec `python3: command not found`** (Windows)
→ remplacer `python3` par `python` dans les commandes des hooks et de la status line.

**Le hook tourne mais rien n'apparaît dans Obsidian.**
→ `~/.claude/kit.json` pointe-t-il sur le bon vault ? `cat ~/.claude/kit.json`.
Chemin avec des `/`, jamais des `\`, même sur Windows.

**Claude Code est devenu lent à chaque commande.**
→ un hook `PreToolUse` ou `PostToolUse` synchrone. Mesurez-le en isolation
(`time echo '{}' | python3 monhook.py`). Passez-le en `"async": true` s'il ne fait
qu'observer.

**Un hook bloque tout, même ce qui est légitime.**
→ `"disableAllHooks": true` dans `settings.json` pour respirer, puis corrigez le hook.

## Skills

**`/mon-skill` n'apparaît pas dans la liste.**
→ Les skills sont lus au démarrage : ouvrez une **nouvelle session**.
→ Le fichier s'appelle bien `SKILL.md` (majuscules), dans `~/.claude/skills/<nom>/` ?
→ Le frontmatter a bien `---` en première ligne et une `description:` ?

**Claude ne déclenche jamais le skill tout seul.**
→ La `description` ne contient pas les mots que vous tapez vraiment. Réécrivez-la
comme un déclencheur : « Use quand … — déclenché par "…", "…" ».

**Claude déclenche le skill quand il ne faut pas.**
→ Description trop large. Ou ajoutez `disable-model-invocation: true` : seul `/nom` le lance.

**`/statusline-aide` ne répond rien.**
→ `~/.claude/statusline.py` n'existe pas. `cp statusline/statusline.py ~/.claude/`.

## Status line

**Rien en bas de l'écran.**
→ `settings.json` : la clé `statusLine` existe ? La commande marche à la main ?
```bash
echo '{"model":{"display_name":"Test"},"workspace":{"current_dir":"'$HOME'"}}' | python3 ~/.claude/statusline.py
```

**`contexte inconnu`** → normal avant la première réponse. Persiste ? Le JSON reçu
ne contient pas `context_window` : version de Claude Code trop ancienne, `claude update`.

**Le segment quota manque** → votre offre ne renvoie pas ces compteurs. Pas une panne.

## Sessions

**`Ambiguous ←, press again to detach`** (Windows) → appuyez une deuxième fois. C'est
le terminal qui relit la touche, pas une erreur.

**`Your most recent conversation is running in the background`** avec `--continue`
→ elle tourne encore. `claude agents` puis `Entrée` dessus pour la rejoindre.

**Le contexte est plein, Claude oublie le début.**
→ `/context` pour voir ce qui pèse. `/compact` pour résumer. `/clear` pour repartir
(la conversation reste dans `/resume`).

## Google (gws)

**`access_denied` ou « application non vérifiée »** → vous n'êtes pas ajouté comme
**utilisateur test** dans l'écran de consentement OAuth de votre projet Google Cloud.

**`insufficient scopes`** → réauthentifiez avec le service manquant :
`gws auth login -s calendar,drive,sheets`.

**Une formule Sheets écrite par l'API donne `#ERROR!` partout** → locale française,
séparateur `;` et pas `,`.

## Quand rien ne marche

1. `claude doctor` : lisez tout, pas juste la première ligne.
2. `claude --settings '{"disableAllHooks":true}'` : si ça remarche, c'est un hook.
3. `mv ~/.claude/settings.json ~/.claude/settings.json.bak` et relancez : si ça
   remarche, c'est le settings. Remettez-le ensuite morceau par morceau.
4. Envoyez à votre formateur **la sortie brute** de la commande, pas une description.
