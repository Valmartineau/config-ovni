<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site 2ee80b0). Ne pas modifier à la main : relancer le script. -->

# Étape 3 : construire votre interface

Voir son contexte et ses quotas, dicter, écouter, garder certaines questions chez soi.
Chaque geste en deux versions : avec Claude, puis souverain.

**Avant chaque brique, trois questions :** où vont mes données ? qui les garde ? comment je repars sans lui ?

Les deux mods sont dans `etape-3-construire/mods/` (`ma-jauge`, `ma-dictee`) : lisez leur fichier
`hooks/register.tsx` avant de les charger. Les mods sont en accès anticipé chez Anthropic : leur
fonctionnement peut changer d'une version à l'autre. Les commandes se lancent depuis le dossier du kit.

## Niveau 3, version Claude

### Lire la barre d'état : contexte et quotas
*Ce qui sort : rien.* Elle est installée depuis l'étape 1 : le contexte, le quota de 5 heures et celui de 7 jours.

Mac et Linux :

```
python3 ~/.claude/statusline.py --legende
```

Windows :

```
python $HOME\.claude\statusline.py --legende
```

Au-delà de 80 % de contexte, tapez `/compact`. **Réussi si** vous savez dire s'il vous reste de quoi finir la tâche.

### Dicter avec /voice
*Ce qui sort : votre voix, envoyée en direct chez Anthropic pour être transcrite. Il faut un compte Claude.ai.*
Dans Claude Code : `/voice`. Tenez la barre d'espace, parlez, relâchez. Langue : `/config`. Sur Linux, il faut SoX.

### Votre premier mod : la jauge
*Ce qui sort : rien.* Lancez Claude avec la jauge, pour cette session :

Mac et Linux :

```
claude --plugin-dir etape-3-construire/mods/ma-jauge
```

Windows :

```
claude --plugin-dir etape-3-construire\mods\ma-jauge
```

Pour la garder : demandez à Claude « ajoute le dossier de ma-jauge à CLAUDE_CODE_PLUGIN_DIRS dans l'env de mes réglages ».
**Réussi si** une ligne « Contexte ▰▰▱▱… » apparaît au-dessus de l'invite, avec une alerte à 85 %.

### Construire votre propre mod
*Ce qui sort : ce que votre mod lancera. Lisez-le.* Décrivez à Claude ce que vous voulez voir, par exemple
« un mod qui affiche le nom de la branche git et le nombre de fichiers modifiés ». Puis demandez-lui ce que le mod
lance et ce qu'il envoie. **Réussi si** il apparaît et que `claude plugin validate` ne signale rien.

## Niveau 3, version souveraine

### Dicter partout avec Handy
*Ce qui sort : rien, une fois le modèle téléchargé.* Handy (libre, MIT, Mac, Windows, Linux) :
https://github.com/cjpais/Handy/releases/latest . Choisissez un modèle, autorisez le micro (et l'accessibilité sur Mac),
choisissez un raccourci, puis dans Claude Code : tenez-le, parlez, relâchez. Coupez le Wi-Fi pour vérifier.

### Le bouton Dicter dans Claude Code (mod ma-dictee)
*Ce qui sort : rien. L'audio est transcrit par whisper.cpp et effacé aussitôt.*

Mac et Linux seulement. Sous Windows, prenez Handy, juste au-dessus.

1. SoX et whisper.cpp. Linux : SoX par votre gestionnaire de paquets, whisper.cpp depuis https://github.com/ggml-org/whisper.cpp . Mac :

```
brew install sox whisper-cpp
```

2. Le modèle de transcription, 574 Mo, une seule fois :

```
mkdir -p ~/.ma-dictee
curl -L -o ~/.ma-dictee/ggml-large-v3-turbo-q5_0.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q5_0.bin
```

3. Rangez les deux mods à demeure, puis lancez Claude avec eux :

```
mkdir -p ~/.claude/mods
cp -R etape-3-construire/mods/ma-jauge etape-3-construire/mods/ma-dictee ~/.claude/mods/
```

```
claude --plugin-dir ~/.claude/mods/ma-jauge --plugin-dir ~/.claude/mods/ma-dictee
```

4. Cliquez sur **● Dicter** ou tapez `/dicter`, parlez, taisez-vous deux secondes. Relisez avant Entrée.

### Écouter les réponses
*Ce qui sort : rien.* Avec ma-dictee : **▶ Lire** ou `/lire`. Les blocs de code ne sont pas lus.

### Le bouton Local : votre agent de l'étape 2
*Ce qui sort : rien.* Écrivez votre question, puis **⌂ Local** ou `/local` au lieu d'Entrée : elle part à Hermes,
la réponse s'affiche dans un panneau à part, jamais envoyé à Claude. Si vous la recopiez dans l'invite, elle partira
chez Anthropic. Pour contrôler les mods :

```
claude plugin validate ~/.claude/mods/ma-dictee
claude plugin test ~/.claude/mods/ma-dictee
```

## Ce qui sort, brique par brique

| Brique | Ce qui sort | La version souveraine |
|---|---|---|
| La barre d'état | Rien : un script sur votre machine lit ce que Claude Code lui donne. | Déjà souveraine. |
| Dicter avec /voice | Votre voix, envoyée en direct chez Anthropic pour être transcrite. Rien n'est traité sur votre machine. | Handy, ou le bouton Dicter de ma-dictee : la transcription se fait chez vous. |
| Votre message à Claude | Le texte, toujours, même dicté en local. Et tout ce que Claude lit. | Le bouton Local : la question va à votre agent Hermes, jamais à Claude. |
| Lire une réponse à voix haute | Rien : c'est la voix de votre système. | Déjà souverain. |
| Un mod | Ce qu'il lance. Un mod peut lancer des programmes et appeler des services. | Lisez son fichier register.tsx avant de le charger. Ceux d'OVNI tiennent sur une page. |
| Ce qu'affiche une commande de mod | Son texte entre dans la conversation, donc part chez Anthropic au message suivant. | Un panneau à part : ma-dictee y montre la réponse de l'agent local. |

## Ce qui est vérifié

**Fait, le 12 novembre 2026 :** les deux mods passent la validation et les tests de Claude Code 2.1.322 ; whisper.cpp a
rendu une phrase exacte en 3,4 secondes sur un Mac à puce Apple. **Pas encore essayé :** les boutons cliqués dans une
vraie session, le micro, Linux, Handy sous Windows et Linux.
