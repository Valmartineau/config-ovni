<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site a9c0064). Ne pas modifier à la main : relancer le script. -->

# 9. Le parcours guidé de NOVI, en texte

Sur la page, NOVI lit ce parcours à voix haute. Le voici à lire, avec ses commandes.

## Accueil

**NOVI**

Bonjour, je suis NOVI. Je vais vous présenter la configuration OVNI, et rester à côté de vous pendant l'installation.

**Le curseur : Montrez, je raconte**

Promenez votre curseur sur l'écran, je vous dis ce qu'il y a à chaque endroit. Ou ne touchez à rien, et je commence.

## Notions

**Claude Code : Un agent dans votre terminal**

Claude Code est un agent qui travaille dans votre terminal. Il lit vos fichiers, il lance des commandes, et il vous demande la permission.

**Zéro : Il repart de rien à chaque session**

Mais il repart de zéro à chaque session. Sans configuration, il ne sait ni qui vous êtes, ni comment vous travaillez.

**Configuration : Mémoire, savoir-faire, limites**

Une configuration lui donne trois choses. Une mémoire, des savoir-faire, et des limites.

**CLAUDE.md : Lu à chaque session**

D'abord, le fichier CLAUDE.md. C'est le texte qu'il lit au démarrage : votre langue, votre méthode, vos interdits.

**Skill : Chargé à la demande**

Le skill, c'est un savoir-faire. Il n'est chargé que quand il sert.

**Hook : Un automatisme garanti**

Le hook est différent. Ce n'est pas le modèle qui décide, c'est le programme. Il ne peut pas l'oublier.

**MCP : Une porte vers un outil**

Le MCP ouvre une porte vers un outil extérieur.

**Sous-agent : Un Claude contraint**

Et le sous-agent est un Claude à qui on retire des droits. Un relecteur sans droit d'écriture ne peut rien modifier.

**Cascade : Du plus large au plus précis**

Les consignes s'empilent : les vôtres, celles du projet, celles du module. Regardez ce qui se charge selon l'endroit où vous lancez Claude.

**À vous : Bloquer à coup sûr tout push forcé sur main**

À vous. Je veux bloquer à coup sûr tout push forcé sur la branche principale. Je le mets où ?

- CLAUDE.md : Pas tout à fait. Un texte, le modèle peut l'oublier. Une interdiction, c'est un hook.
- Hook (la bonne réponse) : Exactement. Une interdiction doit être exécutée par le programme, pas confiée à la mémoire du modèle.
- Skill : Pas tout à fait. Un skill n'est chargé que quand il sert. Une interdiction, c'est un hook.

**Exit 2 : Le geste est refusé avant d'être exécuté**

Regardez. Claude veut effacer votre dossier personnel. Le hook passe avant l'outil, et il refuse.

**Ce qui sort : Ce que Claude lit part au modèle**

Une chose à garder en tête. Ce que Claude lit part au modèle. Et un service distant reçoit aussi vos requêtes.

**Avant de brancher : Quelle question d'abord ?**

Vous voulez brancher un nouvel outil. Quelle est la première question à vous poser ?

- Où vont mes données ? (la bonne réponse) : Oui. Où elles vont, qui les garde, et comment repartir sans lui. Sans ces trois réponses, on ne branche pas encore.
- Combien ça coûte ? : C'est utile, mais il y a plus urgent : où vont vos données, qui les garde, et comment repartir sans lui.

## Méthode

**Vous pilotez : L'agent propose, vous décidez**

L'outil compte moins que la façon de s'en servir. L'agent propose. Vous décidez.

**Comprendre : Avant de toucher à quoi que ce soit**

Première règle : comprendre d'abord. Un petit changement au mauvais endroit, c'est un deuxième problème.

**Vérifier : Exercer le vrai flux**

Dernière règle : vérifier avant de dire fini, et annoncer les échecs tels quels.

**Le go : Rien ne sort sans votre accord**

Claude peut coder seul dans une copie isolée. Mais la fusion attend votre feu vert.

## Installer

**Installer : Cinq gestes, puis Claude conduit**

L'installation tient en cinq gestes. Ensuite, c'est Claude qui conduit les onze étapes du kit.

**Avant tout : Un abonnement Claude Pro, Max, Team ou Enterprise**

Il vous faut un abonnement Claude payant : Pro, Max, Team ou Enterprise. Le plan gratuit ne donne pas accès à Claude Code.

**Votre machine : Pour vous donner la bonne commande**

Vous êtes sur quel ordinateur ?

- Mac ou Linux : Très bien. Pour ouvrir le terminal sur Mac : appuyez sur Commande et Espace, écrivez terminal, puis entrée.
- Windows : Très bien. Ouvrez le menu Démarrer, écrivez PowerShell, et appuyez sur entrée. Il vous faudra aussi Git for Windows : le lien arrive à l'étape 1.

**Je reste là : Un problème ? Un bouton**

Si quelque chose bloque, cliquez sur J'ai un problème. Je vous montre quoi essayer.

**Geste 1 : Installer Claude Code**

Ouvrez votre terminal. Copiez cette commande, collez-la, puis appuyez sur entrée. Dites-moi quand c'est fait.

Mac :

```
curl -fsSL https://claude.ai/install.sh | bash
```

Windows :

```
irm https://claude.ai/install.ps1 | iex
```

**Geste 2 : Vérifier**

Vérifions. La première commande doit vous donner un numéro de version.

Mac :

```
claude --version
claude doctor
```

**Geste 3 : Récupérer le kit, se connecter**

Maintenant, le kit. Ces commandes le récupèrent, et lancent Claude dedans. La première fois, votre navigateur s'ouvre : connectez-vous avec votre compte Claude, puis revenez au terminal.

Mac :

```
git clone https://github.com/Valmartineau/config-ovni.git
cd config-ovni
claude
```

J'ai téléchargé le zip :

Mac :

```
cd ~/Downloads/config-ovni-main
claude
```

Windows :

```
cd $HOME\Downloads\config-ovni-main
claude
```

Sur Mac, si le système propose d'installer des outils de développement, acceptez, puis relancez la commande.

**Geste 4 : Lui demander de conduire**

Dans Claude, écrivez simplement : installe le kit. Il fait une étape à la fois, et il attend votre accord. Prenez le temps, je vous attends.

Mac :

```
installe le kit
```

**Geste 5 : Contrôler**

Pour finir, le vérificateur. Tout doit être validé, sauf les lignes facultatives.

Mac :

```
python3 outils/verifier.py
```

Windows :

```
python outils/verifier.py
```

## Construire

**Où ranger : Cinq questions, dans l'ordre**

Quand vous voulez ajouter quelque chose, posez-vous quelques questions dans l'ordre. Est-ce que cela doit arriver à coup sûr ? Si oui, c'est un hook.

**Un skill : Une description, un corps**

Un skill, c'est un dossier et un fichier. Claude le charge quand sa description correspond à votre demande.

**Le vault : Vos sessions deviennent des notes**

Chaque session terminée peut devenir une note dans votre vault Obsidian. Votre travail reste chez vous.

## Bibliothèque

**12 skills : 3 hooks, 1 sous-agent, tous audités**

Notre bibliothèque est petite. Douze skills, trois hooks, un sous-agent. Tous audités.

**Nettoyer : Chemins, noms, comptes et clés**

Avant d'y entrer, chaque élément est nettoyé, et un contrôle automatique doit donner zéro alerte.

## La suite

**La suite : Six exercices, puis les étapes 2 à 5**

Pour finir l'étape 1, six exercices de dix minutes vous attendent dans le manuel. Ensuite, quatre étapes suivent : votre persona, une intelligence artificielle sur votre machine, votre interface, et un RAG pour interroger vos documents. Le menu du manuel vous montre où vous en êtes : cochez chaque étape quand elle est faite. À vous de jouer.

## IA locale

**IA locale : Un modèle qui tourne chez vous**

Troisième étape : une intelligence artificielle qui tourne sur votre ordinateur. Vos questions ne quittent plus la machine.

**Deux pièces : Ollama fait tourner, Hermes agit**

Il faut deux pièces. Ollama fait tourner le modèle. Hermes est l'agent qui s'en sert : il lit, il écrit, il utilise des outils.

**Votre mémoire : La taille du modèle suit la machine**

Le bon modèle dépend de la mémoire de votre ordinateur. Trop gros, il rame. Trop petit, il se trompe. Le manuel propose aussi un petit programme qui mesure pour vous.

**Votre machine : Pour vous donner les bonnes commandes**

Vous êtes sur quel ordinateur ?

- Mac : Très bien. Ouvrez le menu Pomme, puis À propos de ce Mac. Regardez la ligne Mémoire.
- Windows : Très bien. Ouvrez les Paramètres, puis Système, puis Informations système. Regardez la mémoire installée. Si vous avez une carte graphique NVIDIA, c'est sa mémoire à elle qui compte.
- Linux : Très bien. Dans un terminal, la commande free tiret h affiche la mémoire. Avec une carte NVIDIA, c'est sa mémoire à elle qui compte.

**Combien ? : La mémoire de votre ordinateur**

Combien de mémoire avez-vous ? Je vous donne le modèle qui va avec.

- Moins de 8 Go : Ce sera un petit modèle, pour essayer. Pour un vrai agent, il faudra une machine plus grande.
- 8 Go : Un petit modèle tiendra. Il sera lent sur les longues tâches.
- 16 Go : C'est le bon point de départ. Le modèle est affiché à l'écran.
- 24 Go : Vous pouvez prendre un modèle plus solide. Il est affiché à l'écran.
- 32 Go : Vous pouvez prendre le modèle de notre serveur de référence. Il est affiché à l'écran.
- 48 Go ou plus : Vous pouvez prendre le plus capable de la grille. Il est affiché à l'écran.

**Geste 1 : Installer Ollama**

Ouvrez votre terminal, copiez cette commande, puis appuyez sur entrée. Dites-moi quand c'est fait.

Mac et Linux :

```
curl -fsSL https://ollama.com/install.sh | sh
```

Windows :

```
irm https://ollama.com/install.ps1 | iex
```

Sur Mac et Windows, Ollama s'ouvre ensuite comme une application. Elle doit rester ouverte.

**Geste 2 : Télécharger le modèle**

Maintenant, le modèle. Le téléchargement prend quelques minutes. C'est la seule fois où il passe par internet.

Mac :

```
ollama pull {m}
```

**Geste 3 : Lui donner de la place pour travailler**

L'étape importante. Par défaut, le modèle garde très peu de texte en tête, et un agent en a besoin de beaucoup. Ces deux lignes créent une copie du modèle, avec assez de mémoire de travail.

Mac :

```
printf 'FROM {m}\nPARAMETER num_ctx 65536\n' > Modelfile
ollama create agent-local -f Modelfile
```

Windows :

```
"FROM {m}", "PARAMETER num_ctx 65536" | Set-Content -Encoding ascii Modelfile
ollama create agent-local -f Modelfile
```

Vérifiez avec ollama list : agent-local doit apparaître.

**Geste 4 : Installer Hermes**

Place à l'agent. Copiez cette commande. Si l'installation vous pose des questions, choisissez un point d'accès personnalisé. Puis fermez et rouvrez le terminal.

Mac et Linux :

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Windows :

```
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

**Geste 5 : Brancher Hermes sur votre modèle**

Ces quatre lignes disent à Hermes de parler à votre modèle, sur votre machine, et à personne d'autre.

Mac :

```
hermes config set model.provider custom
hermes config set model.base_url http://localhost:11434/v1
hermes config set model.default agent-local
hermes config set model.context_length 65536
```

**Geste 6 : Le premier bonjour**

Testons. Hermes doit se présenter en une phrase. La deuxième commande doit montrer votre modèle en mémoire.

Mac :

```
hermes -z "Présente-toi en une phrase."
ollama ps
```

**Votre agent : Tapez hermes pour lui parler**

Votre agent tourne chez vous. Tapez hermes pour lui parler. L'étape 3 est faite. La suite, c'est l'étape 4 : construire votre interface, juste après dans le manuel.
