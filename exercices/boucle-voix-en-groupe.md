<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site a9c0064). Ne pas modifier à la main : relancer le script. -->

# À plusieurs, 30 minutes : parler à son ordinateur

Parler à Claude Code au lieu de taper, avec une transcription qui se fait sur votre machine. Deux outils suffisent,
Handy et whisper.cpp. Aucun modèle d'IA à installer chez vous : le cerveau reste Claude.
Seul, à votre rythme : `cd exercices/boucle-voix`, `claude`, puis `/commencer` (le coach est dans son `CLAUDE.md`).

- **Votre voix :** Handy ou whisper.cpp la transcrivent sur votre machine. L'audio ne sort pas.
- **Votre question :** le texte transcrit part chez Anthropic, comme une question tapée.
- **La réponse lue :** la voix de votre système (`say` sur Mac, `espeak-ng` sur Linux). Rien ne sort.

1. **5 min. Comprendre.** Chacun redit ce qui sort de sa machine et ce qui y reste. Lancez les téléchargements tout de suite.
2. **10 min. Voie 1, Handy : dicter dans Claude Code.** https://github.com/cjpais/Handy/releases/latest . Modèle, micro,
   accessibilité sur Mac, un raccourci. Dans Claude Code : tenez-le, parlez, relâchez, relisez, Entrée.
3. **10 min. Voie 2, whisper.cpp : la boucle parlée** (Mac et Linux ; sous Windows, en binôme avec un Mac).
   L'oreille (passez si l'étape 3 est faite). Linux : SoX par le gestionnaire de paquets, whisper.cpp depuis https://github.com/ggml-org/whisper.cpp . Mac :

```
brew install sox whisper-cpp
```

```
mkdir -p ~/.ma-dictee
curl -L -o ~/.ma-dictee/ggml-large-v3-turbo-q5_0.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q5_0.bin
```

   Le script est dans le kit, lisez-le d'abord :

```
cd exercices/boucle-voix
chmod +x boucle-voix.sh
```

   Testez sans micro, l'ordinateur pose la question à sa propre oreille :

Mac :

```
say -v Thomas -o test.aiff "Quelle est la capitale de la France ?"
sox test.aiff -r 16000 -c 1 -b 16 test.wav
./boucle-voix.sh test.wav
```

Linux :

```
espeak-ng -v fr -w test-brut.wav "Quelle est la capitale de la France ?"
sox test-brut.wav -r 16000 -c 1 -b 16 test.wav
./boucle-voix.sh test.wav
```

   Puis parlez : Entrée, votre question, silence (coupure après 1,5 seconde). Ctrl-C pour quitter.

```
./boucle-voix.sh
```

4. **5 min. Le test du Wi-Fi.** Coupez-le et dictez avec Handy : le texte apparaît, la transcription est locale.
   Claude, lui, ne répond plus : c'est la seule pièce qui sort.
5. **5 min. Tour de table.** Chacun dit quelle voie il garde, et pourquoi.

**Réussi si** vous dictez dans Claude Code Wi-Fi coupé, et, sur Mac ou Linux, si Claude vous répond à voix haute.
