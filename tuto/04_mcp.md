# 04 — MCP : donner des outils à Claude

## C'est quoi

**MCP** = Model Context Protocol. Un standard ouvert pour brancher des **outils
externes** sur un modèle. Un serveur MCP expose des fonctions (« lister mes pages
Notion », « lire ma scène Blender », « chercher dans ma base ») ; Claude Code les voit
comme des outils supplémentaires, à côté de Read, Write, Bash.

Trois briques du kit, trois natures :

| Brique | Qui l'exécute | Ce que c'est |
|---|---|---|
| Skill | le modèle (il lit et suit) | un savoir-faire |
| Hook | le programme Claude Code | un automatisme |
| MCP | un programme tiers | un outil, une porte vers un service |

## Deux transports

- **stdio** : un programme local, lancé par Claude Code, qui parle sur son entrée/sortie.
  Exemple : un script Python sur votre machine.
- **http** : un serveur distant (Notion, Canva, un service maison) auquel Claude Code
  se connecte, souvent avec OAuth.

## Ajouter un serveur

```bash
# distant
claude mcp add --transport http notion https://mcp.notion.com/mcp

# local (le -- sépare les options de Claude de la commande du serveur)
claude mcp add --transport stdio mon-serveur -- python3 /chemin/serveur.py

# avec une variable d'environnement
claude mcp add --env MA_CLE=xxx --transport stdio outil -- npx -y un-paquet-mcp

# depuis un JSON
claude mcp add-json meteo '{"type":"http","url":"https://api.exemple.com/mcp"}'
```

Puis, dans Claude Code : `/mcp` pour voir l'état, se connecter (OAuth), lister les
outils. En ligne de commande : `claude mcp list`, `claude mcp get <nom>`,
`claude mcp remove <nom>`, `claude mcp login <nom>`.

## Les portées

| Portée | Chargé dans | Partagé | Stocké dans |
|---|---|---|---|
| `local` (défaut) | ce projet | non | `~/.claude.json` |
| `user` | tous vos projets | non | `~/.claude.json` |
| `project` | ce projet | **oui, commité** | `.mcp.json` à la racine |

`.mcp.json` est le bon endroit pour un outil d'équipe. Voir `modeles/mcp.exemple.json`.
**Jamais de secret dedans** : utilisez `env` avec des variables, et le `.env` reste
hors git.

## Ce qui sort de la machine

Question à se poser **avant** de brancher un MCP : *qu'est-ce qui part, et où ?*

- Un MCP **http** distant reçoit vos requêtes (et ce que Claude décide de lui envoyer :
  ça peut être le contenu d'un fichier). Lisez la politique du service.
- Un MCP **stdio** local ne sort rien par construction… sauf si le programme
  lui-même appelle Internet. Lisez son code ou son README.
- Le **modèle** voit tout ce que l'outil renvoie. Un MCP qui lit votre messagerie
  envoie vos messages au modèle.

Exercice de cartographie (à refaire pour chaque outil) : trois colonnes,
*donnée* → *où elle va* → *qui la garde*. Si une case est vide, vous ne savez pas.

Règle pratique : **denylist**. Dans `settings.json`, `permissions.deny` peut interdire
un serveur MCP entier (`"mcp__nom_serveur"`) ou un outil précis. Le deny gagne
toujours sur l'allow. C'est votre garde-fou contre un outil branché par erreur.

## Écrire un MCP minimal (pour comprendre)

Le SDK officiel Python ou TypeScript permet un serveur en 20 lignes :
un décorateur `@tool`, une fonction, `run()`. Le skill `mcp-developer` du plugin
`fullstack-dev-skills` (voir `08_plugins.md`) guide l'écriture. L'intérêt pédagogique :
voir de ses yeux que « un outil » = « une fonction avec une description », rien de plus.

## Retirer

`claude mcp remove <nom>`. Pour un serveur OAuth : `claude mcp logout <nom>` d'abord.
