---
name: statusline-aide
description: Traduit la status line — que veut dire chaque segment affiché en bas de l'écran. Déclenché par "/statusline-aide", "c'est quoi la ligne du bas", "que veut dire quota 5h".
argument-hint: "[segment précis, optionnel]"
---

Voici la légende de la status line, produite par `~/.claude/statusline.py --legende` :

!`python3 ~/.claude/statusline.py --legende 2>/dev/null || python ~/.claude/statusline.py --legende`

Affiche cette légende **telle quelle** : ne la reformule pas, ne la résume pas.
Si `$ARGUMENTS` nomme un segment précis (« contexte », « quota », « notes »…),
n'affiche que la ou les lignes correspondantes et développe-les en une ou deux phrases.

Si le bloc ci-dessus est vide ou en erreur, dis-le franchement et vérifie que
`~/.claude/statusline.py` existe, puis que la clé `statusLine` de
`~/.claude/settings.json` pointe bien dessus.
