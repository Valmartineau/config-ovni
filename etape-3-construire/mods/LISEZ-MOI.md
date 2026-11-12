# Config OVNI, étape 3 : deux mods pour Claude Code

Deux petits modules qui changent l'interface de Claude Code. Lisez-les avant de les charger :
chaque fichier `hooks/register.tsx` tient sur une page.

- **ma-jauge** : le contexte et vos quotas de 5 heures et de 7 jours, au-dessus de l'invite.
  Une alerte à 85 % de contexte. Elle lit les chiffres de Claude Code : rien ne sort.
- **ma-dictee** : trois boutons au-dessus de l'invite, et aucun n'envoie quoi que ce soit.
  - **● Dicter** (ou `/dicter`) : micro, puis whisper.cpp sur votre machine. Le texte arrive dans l'invite, à relire avant Entrée. L'audio est effacé aussitôt.
  - **▶ Lire** (ou `/lire`) : la dernière réponse, avec la voix de votre système.
  - **⌂ Local** (ou `/local`) : ce que vous avez écrit dans l'invite part à votre agent Hermes (étape 2), jamais à Claude. La réponse reste dans un panneau à part.
  - Mac et Linux. Il faut SoX, whisper.cpp et un modèle Whisper. Sous Windows, prenez Handy pour la dictée.

## Essayer pour une session

    claude --plugin-dir ~/Downloads/config-ovni-mods/ma-jauge --plugin-dir ~/Downloads/config-ovni-mods/ma-dictee

## Réglages de ma-dictee (facultatif)

- `MA_DICTEE_WHISPER` : le programme whisper.cpp (par défaut `whisper-cli`).
- `MA_DICTEE_MODELE` : le modèle (par défaut `~/.ma-dictee/ggml-large-v3-turbo-q5_0.bin`).

## Tester

    claude plugin validate ma-dictee
    claude plugin test ma-dictee

Les mods de Claude Code sont en accès anticipé : leur interface peut changer d'une version à l'autre.
Écrits et testés avec Claude Code 2.1.322. Licence CC BY-NC 4.0, OVNI Conseil.
