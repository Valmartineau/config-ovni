# 06 — Google : agenda, Drive, Gmail, Sheets depuis Claude Code

## Le choix de l'outil

Deux voies pour parler à Google depuis Claude Code :

1. **Les connecteurs MCP de claude.ai** (Gmail, Drive, Calendar). Simples, mais
   authentifiés sur le compte connecté à votre navigateur, souvent en lecture seule,
   et vous ne voyez pas ce qui transite.
2. **La CLI `gws`** (Google Workspace CLI, publiée par Google, Apache-2.0). Un programme
   local, avec **votre** projet Google Cloud et **vos** identifiants OAuth. Vous savez
   exactement quel compte est branché et avec quels droits (scopes).

Le kit enseigne la voie 2. Leçon de fond : quand un outil touche vos données, préférez
celui dont vous tenez les clés.

## Installer gws

```bash
brew install googleworkspace-cli        # macOS / Linux
npm install -g @googleworkspace/cli     # toutes plateformes (télécharge le binaire)
```
Ou le binaire pour votre système (Windows compris) sur
https://github.com/googleworkspace/cli/releases.

Vérifier : `gws --version`.

## Authentifier (votre compte, vos clés)

Il faut un projet Google Cloud et un client OAuth. Deux chemins :

**Automatique**, si `gcloud` est installé :
```bash
gws auth setup          # crée le projet, active les API, lance la connexion
```

**Manuel** (recommandé pour comprendre) :
1. https://console.cloud.google.com → créer un projet.
2. « API et services » → activer Calendar, Drive, Gmail, Sheets (celles dont vous avez besoin).
3. « Écran de consentement OAuth » → type externe → **ajoutez-vous comme utilisateur test**
   (sinon Google bloque l'accès).
4. « Identifiants » → créer un identifiant OAuth → type **Application de bureau** →
   télécharger le JSON.
5. Enregistrez-le en `~/.config/gws/client_secret.json`.
6. Connexion, en limitant les droits à ce qu'il faut :
   ```bash
   gws auth login -s calendar,drive
   gws auth status
   ```

Le jeton est gardé dans le trousseau du système. Ne lancez **jamais** `gws auth export`
dans une session Claude : ça affiche vos identifiants en clair dans la conversation.

## Premiers appels (lecture seule)

```bash
gws calendar +agenda                                   # mes prochains événements
gws calendar calendarList list                         # quel compte ? doit afficher le vôtre
gws drive files list --params '{"pageSize":10}'
gws sheets +read --spreadsheet <ID> --range 'Feuille1!A1:C20'
```

Syntaxe générale : `gws <service> <ressource> <méthode> --params '<JSON>' [--json '<corps>']`.
Les raccourcis `+agenda`, `+read`, `+append`, `+send`, `+upload` couvrent le courant.

## Écrire (avec garde-fou)

```bash
gws sheets +append --spreadsheet <ID> --values 'a,b,c'
gws calendar +insert --help
gws gmail +send --to x@y.z --subject "…" --body "…"     # part AUSSITÔT
```

Règle à inscrire dans votre `CLAUDE.md` : **confirmation humaine avant tout envoi
de mail ou toute écriture dans Drive/Agenda.** Claude prépare, montre, et vous dites
« go ». Un `+send` n'a pas de brouillon : il part.

## Pièges vécus (Sheets par l'API)

- Locale française : le séparateur de formule est `;`, pas `,`. Une formule avec des
  virgules donne `#ERROR!` partout, sans dire pourquoi.
- Un texte comme « Septembre 2026 » est converti en date si la cellule est en format
  automatique. Forcez le format TEXTE avant d'écrire.
- `QUERY` renvoie `#REF!` si sa plage ne commence pas en colonne A.
- Après un changement de structure, **rejouez le flux**, ne relisez pas seulement les formules.

## Exercice

1. Installez, authentifiez avec **lecture seule** (`gws auth login --readonly`).
2. Demandez à Claude : « montre-moi mon agenda de la semaine avec gws ».
3. Faites-lui écrire dans votre `CLAUDE.md` la règle de confirmation avant écriture.
4. Seulement ensuite : ré-authentifiez avec les scopes d'écriture nécessaires.

## Retirer

`gws auth logout`, puis supprimez le client OAuth dans la console Google Cloud.
