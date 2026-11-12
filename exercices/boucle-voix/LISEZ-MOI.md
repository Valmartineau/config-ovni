# Exercice « Parler à son ordinateur » — Config OVNI

Une brique vocale sur votre machine : vous parlez, elle transcrit, un cerveau
répond, elle vous répond à voix haute. Claude Code vous accompagne pas à pas.

## Démarrer

1. Décompressez ce zip (par exemple dans Téléchargements).
2. Ouvrez un terminal dans le dossier :
   ```
   cd ~/Downloads/exercice-boucle-voix
   ```
3. Lancez Claude Code, puis tapez `/commencer` :
   ```
   claude
   ```

Le coach vous demande votre niveau, vérifie votre machine et vous guide.
Vous pouvez vous arrêter quand vous voulez : il note où vous en êtes dans
`progression.md` et reprend au prochain `/commencer`.

## Dans le dossier

- `CLAUDE.md` : les consignes du coach. Lisez-les : rien n'est caché.
- `boucle-voix.sh` : le script de la boucle, une page à lire avant de le lancer.
- `.claude/commands/commencer.md` : la commande `/commencer`.

## Ce qui sort de votre machine

- Votre conversation avec le coach part chez Anthropic, comme toute session Claude Code.
- Handy et whisper.cpp transcrivent chez vous : l'audio ne sort pas. Le texte
  de votre question part chez Anthropic, comme une question tapée.

Handy : Mac, Windows, Linux. La boucle parlée : Mac et Linux.

OVNI · ovniconseil.fr · CC BY-NC 4.0
