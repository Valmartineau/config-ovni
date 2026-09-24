# 10 — Sessions : plusieurs Claude en même temps, et le menu pour les piloter

## Une session, c'est quoi

Une session = une conversation, liée à un dossier, sauvegardée en continu dans
`~/.claude/projects/<projet>/<id>.jsonl`. On peut la quitter, la reprendre, la
nommer, la dupliquer. Et on peut en faire tourner **plusieurs à la fois**.

## Reprendre et nommer

| Commande | Effet |
|---|---|
| `claude --continue` | reprend la dernière conversation de ce dossier |
| `claude --resume` | ouvre le **sélecteur de sessions** (liste, recherche, aperçu) |
| `claude --resume <nom>` | reprend une session par son nom |
| `/resume` | même sélecteur, depuis une session ouverte |
| `claude -n mon-nom` ou `/rename mon-nom` | nomme la session (visible dans la barre du bas) |
| `/branch essai-b` | duplique la conversation pour tenter une autre voie |
| `/clear` · `/compact` · `/context` | vider · résumer · voir ce qui occupe le contexte |

Dans le sélecteur : `↑↓` naviguer, `Espace` aperçu, `Entrée` reprendre, `Ctrl+R`
renommer, `Ctrl+A` toutes les sessions de la machine, `Ctrl+B` la branche git courante.

Nommez vos sessions dès que vous en avez deux. Sinon vous les confondez.

## Le menu des sessions : **agent view**

C'est l'écran qui montre **toutes les sessions en cours** : ce qui tourne, ce qui
attend votre réponse, ce qui est fini. On lance des tâches depuis là, on regarde
sans ouvrir, on répond, on bascule.

Ouvrir :
```bash
claude agents
```
Ou, dans une session ouverte : touche **←** sur une invite vide → la session passe
en arrière-plan et le menu s'affiche. `Échap` revient.

Ce qu'on y voit, groupé par état : **Épinglées** · **À relire** (PR ouverte) ·
**Besoin de vous** (question, permission) · **En cours** · **Terminées**.
Chaque ligne : icône d'état, nom, résumé d'une ligne, âge.

Touches utiles :

| Touche | Action |
|---|---|
| `↑` / `↓` | choisir une session |
| `Espace` | aperçu (dernière ligne + question en attente) ; on peut répondre directement |
| `Entrée` ou `→` | s'attacher : la conversation complète prend l'écran |
| `←` sur invite vide, ou `/exit` | se détacher, revenir au menu (la session continue) |
| `Ctrl+T` | épingler (garde le processus vivant) |
| `Ctrl+R` | renommer |
| `Ctrl+X` | arrêter ; deux fois = supprimer de la liste |
| `Ctrl+S` | grouper par état ou par dossier |
| `?` | tous les raccourcis |

Lancer une tâche **depuis le menu** : tapez la demande dans la zone de saisie,
`Entrée`. Une ligne apparaît et se met à jour. Filtrer plutôt que lancer :
`s:working`, `s:blocked`, `a:<agent>`.

Depuis le shell, sans ouvrir le menu :
```bash
claude --bg "corrige le test qui échoue"            # lance en arrière-plan
claude --bg --name "fix-test" "corrige le test"     # nommée
claude agents --json                                 # liste en JSON
claude attach <id> · claude logs <id> · claude stop <id>
```
Depuis une session : `/bg <tâche>` envoie une tâche en arrière-plan sans quitter.

Sur Windows : si `←` juste après l'attache affiche « Ambiguous ←, press again »,
appuyez une seconde fois. C'est un artefact du terminal, pas une erreur.

Réglages liés (`settings.json`) :
```json
"agents": { "leftArrowOpensAgents": true },
"worktree": { "bgIsolation": "none" }
```
`bgIsolation` : par défaut, une session lancée en arrière-plan travaille dans un
**worktree git séparé** pour ne pas entrer en collision avec vous. `"none"` la fait
travailler dans le dossier courant. Choisissez en connaissance de cause : l'isolation
protège, mais elle surprend la première fois (« où sont mes fichiers ? »).

## Le plein écran (`tui: fullscreen`)

Par défaut, Claude Code dessine dans le défilement normal du terminal. Le mode
**fullscreen** utilise l'écran alternatif du terminal, sans scintillement, avec un
défilement virtuel. Plus lisible sur les longues sessions et avec le menu agent view.

```json
"tui": "fullscreen"
```
dans `~/.claude/settings.json` (ou `/config` → interface). Valeurs : `"fullscreen"`,
`"default"`. Si l'affichage se dérègle sur un terminal exotique, revenez à `"default"`.

## Le coût du parallélisme

Deux sessions lourdes en même temps = deux fois le quota consommé, dans la même
fenêtre de 5 h. La status line du kit affiche ce quota : regardez-la avant de
lancer une troisième session. Le parallélisme est un outil, pas un réflexe.

## Exercice

1. Ouvrez une session, nommez-la avec `/rename`.
2. `←` sur invite vide : elle passe au menu. `Espace` pour l'aperçu. `Entrée` pour revenir.
3. Depuis le menu, lancez une deuxième tâche courte. Regardez les deux lignes vivre.
4. `Ctrl+X` sur la deuxième pour l'arrêter. `claude agents --json` dans un autre terminal.
