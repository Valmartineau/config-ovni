# 00 — Installer Codex

Codex est l'agent de code d'OpenAI. Il travaille dans votre terminal, comme Claude Code.
Ce tuto l'installe, vous connecte, puis lance le kit.

## Ce qu'il faut avant

- **Un compte ChatGPT** avec une offre Plus, Pro, Business, Edu ou Enterprise.
  Autre voie : une **clé API OpenAI**, facturée à l'usage.
- **Git** et **Python 3**. Sur Mac, la première commande `git` propose d'installer
  les outils de développement : acceptez.
- **Sur Windows** : Windows 10 version 1809 ou plus récent, et `winget`.

## 1. Ouvrir un terminal

- **Mac** : Commande + Espace, écrivez « terminal », puis Entrée.
- **Windows** : menu Démarrer, écrivez « PowerShell », puis Entrée.
- **Linux** : votre terminal habituel.

## 2. Installer

macOS, Linux :

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Windows, dans PowerShell :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Autres voies, au choix : `brew install --cask codex` (Mac avec Homebrew) ou
`npm install -g @openai/codex` (si Node est installé).

**Lisez avant de lancer.** Une commande `curl … | sh` exécute un script venu
d'Internet. Ouvrez l'adresse dans votre navigateur pour voir ce qu'il fait.

## 3. Vérifier

Fermez puis rouvrez le terminal, puis :

```bash
codex --version
```

Un numéro de version s'affiche. Sinon : le terminal ne trouve pas `codex`.
Rouvrez le terminal ; si rien ne change, relancez l'installation et lisez son message.

## 4. Se connecter

```bash
codex
```

Au premier lancement, Codex propose **Sign in with ChatGPT** : votre navigateur
s'ouvre, connectez-vous, puis revenez au terminal. Avec une clé API, choisissez
l'autre option. La clé ne va **jamais** dans un fichier du kit.

Pour quitter Codex : `/quit` ou Ctrl + C deux fois.

## 5. Lancer le kit

Dézippez `config-ovni-codex.zip`, puis ouvrez Codex **dans le dossier du kit**.

Mac, Linux (zip dézippé dans Téléchargements) :

```bash
cd ~/Downloads/config-ovni-codex
codex
```

Windows, dans PowerShell :

```powershell
cd $HOME\Downloads\config-ovni-codex
codex
```

Puis écrivez : **installe le kit**. Codex lit le fichier `AGENTS.md` du dossier et
vous guide une étape à la fois.

## Windows : natif ou WSL ?

Codex tourne directement dans PowerShell, avec un bac à sable Windows.
Prenez **WSL** seulement si vous travaillez déjà dans Linux sous Windows.
Dans WSL, suivez les commandes « Linux » de ce tuto.

## Réussi si

`codex --version` répond, et une session ouverte dans le dossier du kit répond
à « que contient ce dossier ? » en citant `AGENTS.md`.

## Retirer

- Installé par script : supprimez le binaire indiqué en fin d'installation.
- Par npm : `npm uninstall -g @openai/codex`. Par Homebrew : `brew uninstall --cask codex`.
- Vos réglages et votre connexion restent dans `~/.codex/` : supprimez ce dossier
  pour tout effacer.
