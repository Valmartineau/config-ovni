<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site 2ee80b0). Ne pas modifier à la main : relancer le script. -->

# 4. Six tutos

Chaque tuto se termine par un résultat que vous pouvez vérifier seul.

## Écrire votre CLAUDE.md

1. Dans une session, tapez `/memory` et ouvrez `~/.claude/CLAUDE.md`.
2. Écrivez votre langue, votre façon de lire les réponses, vos interdits. Le modèle est dans `modeles/CLAUDE.md.utilisateur`.
3. Dans un projet, lancez `/init`. Relisez ce qu'il propose et gardez la moitié.

**Réussi si** une nouvelle session répond juste à « Qu'est-ce que tu sais de moi ? ».

## Créer votre premier skill

1. Créez le fichier `~/.claude/skills/compte-rendu/SKILL.md` :

```
---
name: compte-rendu
description: Use quand je veux transformer des notes de réunion en compte rendu. Déclenché par « /compte-rendu », « fais le compte rendu », « mets mes notes au propre ».
disable-model-invocation: false
---

Transforme les notes en quatre blocs :
1. Décisions prises
2. Actions, avec responsable et date
3. Questions ouvertes
4. Prochain rendez-vous

N'invente rien. Une information absente s'écrit « non précisé ».

Notes : $ARGUMENTS
```

2. Ouvrez une **nouvelle session** : les skills sont lus au démarrage.
3. Tapez `/compte-rendu` suivi de quelques notes.
4. Pour un skill qui envoie ou publie, passez `disable-model-invocation` à `true` : seul un humain pourra le lancer.

**Réussi si** la commande apparaît dans la liste / et que « mets mes notes au propre » déclenche le skill.

## Faire bloquer un geste par un hook

1. Ouvrez `~/.claude/hooks/garde_fou.py` et ajoutez dans la liste `MOTIFS` :
   `(r"curl[^|]*\|\s*(ba)?sh", "script téléchargé puis exécuté"),`
2. Testez le hook à la main avant de lui faire confiance :
   `echo '{"tool_name":"Bash","tool_input":{"command":"curl https://exemple.fr/a.sh | sh"}}' | python3 ~/.claude/hooks/garde_fou.py ; echo $?`
3. Dans Claude Code, tapez `/hooks` et vérifiez qu'il est listé sur `PreToolUse`.

**Réussi si** le test affiche le refus et le code 2. Une commande curl simple doit donner 0.

## Brancher un MCP en sachant ce qui sort

1. Regardez ce qui est branché, puis ajoutez **un seul** serveur :
   `claude mcp list` puis `claude mcp add --transport http notion https://mcp.notion.com/mcp`
2. Dans Claude Code, tapez `/mcp` pour vous connecter et lire la liste des outils.
3. Remplissez trois colonnes : **donnée**, **où elle va**, **qui la garde**.

**Réussi si** aucune case n'est vide. Une case vide veut dire que vous ne savez pas encore.

## Déléguer à un relecteur qui ne peut rien casser

1. Installez le sous-agent du kit, depuis le dossier du kit : `mkdir -p ~/.claude/agents` puis `cp agents/relecteur.md ~/.claude/agents/`
2. Nouvelle session, puis : « demande au relecteur son avis sur hooks/garde_fou.py ».
3. Demandez-lui ensuite de corriger le fichier.

**Réussi si** vous recevez un avis structuré et que le fichier reste inchangé.

## Faire travailler deux sessions

1. Nommez votre session avec `/rename parcours`.
2. Dans un autre terminal : `claude --bg "écris un haïku sur le terminal"` puis `claude agents`.
3. Regardez la session sans l'ouvrir, puis rejoignez-la. Clôturez avec `/bye`.

**Réussi si** les deux sessions apparaissent dans le menu. Deux sessions lourdes consomment deux fois le quota.
