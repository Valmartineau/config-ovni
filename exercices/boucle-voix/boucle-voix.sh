#!/bin/bash
# Boucle vocale Config OVNI : micro → transcription locale → Claude → voix du système.
# L'oreille (whisper.cpp) et la voix (say ou espeak-ng) restent sur la machine.
# Seul le TEXTE de la question part chez Anthropic, comme une question tapée.
# Mac et Linux. Pas Windows (sous Windows : dicter avec Handy).
# Besoins : sox, whisper.cpp (whisper-cli) et le modèle de transcription.
# ponytail: un enregistrement par tour, pas de flux continu ni d'interruption pendant
#   la réponse ; upgrade = whisper-server en flux + détection de voix, ou VoiceMode
#   branché sur un Whisper et une voix locaux.

MODELE=${MODELE:-$HOME/.ma-dictee/ggml-large-v3-turbo-q5_0.bin}
WHISPER=${WHISPER:-$(command -v whisper-cli)}
VOIX=${VOIX:-Thomas}
CONSIGNE="Tu réponds à l'oral, en français, en deux phrases courtes, sans liste ni markdown."

[ -x "$WHISPER" ] || { echo "whisper-cli introuvable : installez whisper.cpp"; exit 1; }
[ -f "$MODELE" ]  || { echo "Modèle introuvable : $MODELE"; exit 1; }
command -v rec >/dev/null || { echo "rec introuvable : installez sox"; exit 1; }

DOSSIER=$(mktemp -d); trap 'rm -rf "$DOSSIER"' EXIT   # l'audio est effacé à la sortie

ecouter() { # enregistre jusqu'à 1,5 s de silence
  rec -q -r 16000 -c 1 -b 16 "$DOSSIER/q.wav" silence 1 0.1 2% 1 1.5 2% 2>/dev/null
}
transcrire() { "$WHISPER" -m "$MODELE" -l fr -nt -np -f "$1" 2>/dev/null | tr -s "\n" " " | sed "s/^ *//"; }
penser() { claude -p "$CONSIGNE Question : $1"; }   # la seule pièce qui sort : le texte
parler() {
  if command -v say >/dev/null; then say -v "$VOIX" "$1"; else espeak-ng -v fr "$1"; fi
}

# Mode test : ./boucle-voix.sh fichier.wav → un seul tour, chronométré, sans micro
if [ -n "$1" ]; then
  t0=$(date +%s); texte=$(transcrire "$1"); t1=$(date +%s)
  rep=$(penser "$texte"); t2=$(date +%s)
  echo "Vous : $texte"; echo "Claude : $rep"
  echo "Oreille : $((t1-t0)) s · Claude : $((t2-t1)) s"
  parler "$rep"; exit 0
fi

echo "Entrée = parler · Ctrl-C = quitter"
while read -r -p "▶ " _; do
  echo "● J'écoute (je coupe après 1,5 s de silence)…"
  ecouter
  texte=$(transcrire "$DOSSIER/q.wav")
  [ -z "$texte" ] && { echo "(rien entendu)"; continue; }
  echo "Vous : $texte"
  t1=$(date +%s); rep=$(penser "$texte"); t2=$(date +%s)
  echo "Claude ($((t2-t1)) s) : $rep"
  parler "$rep"
done
