<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site a9c0064). Ne pas modifier à la main : relancer le script. -->

# Étape 2 : votre IA locale

Un modèle qui tourne sur votre ordinateur (Ollama), et un agent qui s'en sert (Hermes).
Vos questions ne quittent plus la machine. La taille du modèle suit la puissance de chacun.

Avant de commencer : l'étape 1 faite, un terminal ouvert, et **de 10 à 30 Go libres**.
Il faut macOS 14 ou plus récent, ou Windows 10 22H2 ou plus récent.
Les commandes ci-dessous prennent le modèle `qwen3.5:9b` (16 Go) : remplacez-le par celui de votre ligne.

## Choisir le modèle

**Avec la grille.** Mac : menu Pomme, « À propos de ce Mac », ligne Mémoire. Windows : Paramètres, Système,
Informations système (avec une carte NVIDIA, regardez plutôt sa mémoire, Gestionnaire des tâches, Performance).
Linux : `free -h`, ou `nvidia-smi` avec une carte NVIDIA. Sur un Mac à puce Apple, toute la mémoire sert au modèle.
Sur un PC, c'est celle de la carte NVIDIA qui compte. Sans carte graphique, restez sur 8 Go.

| Mémoire | Modèle | À télécharger | Pour qui |
|---|---|---|---|
| moins de 8 Go | `qwen3.5:2b` | 3 Go | Pour essayer seulement : trop juste pour un agent fiable. |
| 8 Go et plus | `qwen3.5:4b` | 4 Go | Un petit agent, lent sur les longues tâches. |
| 16 Go et plus | `qwen3.5:9b` | 7 Go | Le bon point de départ pour la plupart des portables. |
| 24 Go et plus | `gpt-oss:20b` | 14 Go | Plus solide sur le raisonnement. |
| 32 Go et plus | `gemma4:26b` | 17 Go | Le modèle de notre serveur de référence. |
| 48 Go et plus | `qwen3.6:35b-a3b` | 23 Go | Le plus capable de la grille, et rapide. |

**Avec le script qui mesure** (`etape-2-ia-locale/choisir-modele.py`, il ne télécharge et n'envoie rien), depuis le dossier du kit :

Mac et Linux :

```
python3 etape-2-ia-locale/choisir-modele.py
```

Windows :

```
python etape-2-ia-locale\choisir-modele.py
```

## Installer pas à pas

1. **Installer Ollama**, qui fait tourner les modèles. Sur Mac et Windows, l'application Ollama doit rester ouverte
   (installateurs : https://ollama.com/download/Ollama.dmg , https://ollama.com/download/OllamaSetup.exe).

Mac et Linux :

```
curl -fsSL https://ollama.com/install.sh | sh
```

Windows :

```
irm https://ollama.com/install.ps1 | iex
```

```
ollama --version
```

2. **Télécharger le modèle.** Quelques minutes. C'est la seule fois où le modèle passe par internet.

```
ollama pull qwen3.5:9b
```

3. **Lui donner de la place pour travailler.** Par défaut, Ollama ne garde que 4 000 jetons en tête sur une machine
   de moins de 24 Go. Un agent en demande au moins 64 000. Ces lignes créent une copie du modèle, nommée `agent-local`, réglée à 65536.

Mac et Linux :

```
printf 'FROM qwen3.5:9b\nPARAMETER num_ctx 65536\n' > Modelfile
ollama create agent-local -f Modelfile
```

Windows :

```
"FROM qwen3.5:9b", "PARAMETER num_ctx 65536" | Set-Content -Encoding ascii Modelfile
ollama create agent-local -f Modelfile
```

```
ollama list
```

4. **Installer Hermes**, l'agent. Si l'installation ouvre un assistant, choisissez « Custom endpoint », ou quittez-le.

Mac et Linux :

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Windows :

```
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

   Fermez et rouvrez le terminal, puis :

```
hermes --version
```

5. **Brancher Hermes sur votre modèle.**

```
hermes config set model.provider custom
hermes config set model.base_url http://localhost:11434/v1
hermes config set model.default agent-local
hermes config set model.context_length 65536
```

6. **Le premier bonjour.** `ollama ps` doit montrer `agent-local`, **100% GPU** et un contexte de 65536. Si le processeur
   apparaît, le modèle est trop gros : prenez le palier du dessous. Patience : sur un portable de 16 Go,
   de 2 à 4 minutes par réponse ; bien plus vite à partir de 32 Go.

```
hermes -z "Présente-toi en une phrase."
ollama ps
```

7. **Lui parler.** Pour quitter : `/exit`.

```
hermes
```

## Ce qui reste chez vous

- **Vos questions et les réponses :** le modèle tourne sur votre machine, à l'adresse `localhost`.
- **La mémoire de Hermes** et ses réglages, dans le dossier `.hermes` de votre compte.
- **Le modèle lui-même,** une fois téléchargé : il marche sans internet.

## Ce qui peut encore sortir

- **Les téléchargements :** Ollama, Hermes, le modèle et leurs mises à jour.
- **Un modèle dont le nom finit par `cloud`** tourne chez Ollama, pas chez vous. Il n'y en a aucun dans la grille.
- **Les outils de Hermes** qui vont sur le web, ou une messagerie que vous lui branchez. Posez les trois questions avant.

## Si ça coince

| Ce que vous voyez | Ce qu'il faut faire |
|---|---|
| Hermes répond « context too small » ou coupe ses réponses | Le modèle n'a pas reçu ses 65536 jetons de mémoire de travail. Refaites le geste 3 (lui donner de la place), puis vérifiez que model.default vaut agent-local. |
| « connection refused » sur localhost:11434 | Ollama ne tourne pas. Sur Mac et Windows, ouvrez l'application Ollama. Sur Linux : ollama serve dans un autre terminal. |
| Tout est très lent, le ventilateur souffle | Le modèle est trop gros pour la machine. ollama ps doit afficher 100% GPU. Sinon, prenez le palier du dessous. |
| hermes : commande introuvable | Fermez et rouvrez le terminal. Sur Mac et Linux, vérifiez que ~/.local/bin est dans le PATH, comme pour Claude Code. |
| L'assistant de Hermes s'ouvre à l'installation | Choisissez « Custom endpoint », adresse http://localhost:11434/v1, modèle agent-local. Ou quittez-le : le geste 5 (brancher Hermes) fait le même réglage. |

## Tout retirer

La ligne `--dry-run` montre ce qui partira, sans rien effacer. Puis retirez l'application Ollama comme toute application.

```
ollama rm agent-local
ollama rm qwen3.5:9b
hermes uninstall --dry-run
hermes uninstall
```

## Ce qui est vérifié

**Fait, le 12 novembre 2026 :** les étapes 2 à 6 sur un Mac à puce Apple de 16 Go avec qwen3.5:9b ; le script
sur deux Mac, de 16 et 48 Go. **Pas encore essayé :** Windows et Linux complets, les paliers 8, 24 et 32 Go.
