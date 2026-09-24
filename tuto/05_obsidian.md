# 05 — Obsidian : le second cerveau qui parle avec Claude Code

## L'idée

Claude Code oublie tout à chaque session. Vous aussi, en partie. Un **vault Obsidian**
(un dossier de fichiers markdown) devient la mémoire commune : Claude y écrit ce qu'il
a fait, vous y lisez, vous y écrivez, et la session suivante peut le relire.

Pourquoi Obsidian et pas un outil en ligne : ce sont des **fichiers texte locaux**.
Claude Code les lit avec ses outils de base. Rien ne sort, rien ne dépend d'un service.

## Le squelette du kit

```
Vault/
├── 00_Accueil.md          ← point d'entrée, liens vers le reste
├── 00_Inbox/              ← ce qui n'a pas encore de place
├── 02_Projets/            ← une note par projet (nom = nom du projet)
├── 03_Journal/            ← une daily note par jour : AAAA-MM-JJ.md
├── 04_Ressources/         ← références, docs, liens
├── 06_Claude/sessions/    ← les notes de session écrites par Claude Code
└── Templates/Session.md   ← le gabarit d'une note de session
```

Les numéros trient l'affichage. Les trous (01, 05) sont pour vous.

## Le flux, de bout en bout

1. **SessionStart** : le hook `obsidian_session_start.py` regarde si la daily note
   du jour existe et le dit à Claude, avec la consigne d'archiver la session.
2. Vous travaillez.
3. **Stop** (à chaque réponse) : `obsidian_daily.py` pose ou met à jour une ligne
   « HH:00 — Claude Code (n sessions) » dans la daily note. Anti-spam : une ligne
   par heure, incrémentée.
4. Fin de phase ou `/bye` : le skill `session-note` écrit une **note de session**
   complète dans `06_Claude/sessions/`, et la relie à la daily note par un `[[wikilink]]`.
5. La note cite les projets en `[[Nom_Projet]]` : Obsidian affiche les **backlinks**
   dans la note du projet. Sans jamais modifier la note du projet.

## Le format d'une note de session

Le gabarit `Templates/Session.md` impose : frontmatter (date, projets, statut, tags),
un **Résumé en prose** (la partie la plus utile : c'est ce qu'un moteur de recherche
sémantique indexera le mieux), puis fait / décisions / fichiers / à faire / liens.
Chaque ligne nomme son sujet : elle doit se comprendre **hors contexte**.

## Pour aller plus loin

- **Skills Obsidian** de kepano : markdown Obsidian, Bases (vues type base de données
  sur vos notes), Canvas. https://github.com/kepano/obsidian-skills
- **Rappel sémantique** : indexer le vault (embeddings locaux) et, sur `UserPromptSubmit`,
  injecter les 3 notes les plus proches du message. C'est un hook + un petit index.
  Bonne première « vraie » automatisation à construire soi-même.
- **Synchronisation** entre machines : Syncthing (pair à pair, rien dans le cloud)
  ou un dépôt git privé avec un commit automatique toutes les 15 minutes.

## Exercice

1. Installez Obsidian, ouvrez le dossier `vault/` du kit (copié où vous voulez)
   comme coffre.
2. Écrivez `~/.claude/kit.json` avec le chemin.
3. Branchez les deux hooks (voir `03_hooks.md`). Ouvrez une session, dites bonjour,
   fermez. Vérifiez la daily note.
4. `/session-note` en fin d'une vraie session. Lisez la note. Corrigez le gabarit
   pour qu'il vous ressemble.

## Retirer

Débranchez les hooks. Le vault est à vous, il reste.
