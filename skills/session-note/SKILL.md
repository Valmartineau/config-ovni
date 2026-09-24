---
name: session-note
description: Use quand l'utilisateur veut archiver la session Claude Code en cours dans son vault Obsidian — déclenché par "/session-note", "archive la session", "note de session", et à chaque fin de phase de travail (merge, livraison, décision actée).
argument-hint: "[titre court optionnel]"
---

# /session-note — archiver la session dans le vault

Chemin du vault : lis `~/.claude/kit.json` (clé `vault`). S'il manque, demande-le
une fois et propose de l'écrire dans ce fichier.

Une seule note par session, **mise à jour** au fil des phases (statut `en_cours`),
finalisée `termine` en fin de session. Procède dans l'ordre.

## 1. Détecter les projets concernés

Liste les noms de notes de `<vault>/02_Projets/*.md`. Repère ceux que CETTE session
a réellement touchés : ils servent au frontmatter `projets` ET aux `[[wikilinks]]`.
Si un sujet n'a pas encore de note projet, mets quand même le `[[wikilink]]`
(lien orphelin = projet à créer, c'est voulu).

## 2. Composer la note (format optimisé pour la relecture et la recherche)

Gabarit : `<vault>/Templates/Session.md`. Format exact :

```markdown
---
type: session
date: <AAAA-MM-JJ>
heure: "<HH:MM>"
outil: claude-code
projets: [<...>]
statut: <en_cours|termine>
tags: [session, <...>]
---

# Session <AAAA-MM-JJ> <HH>h<MM> — <titre court qui NOMME le sujet>

**Résumé.** <2 à 4 phrases en prose qui nomment explicitement les projets et sujets.>

## Ce qui a été fait
- ✅ **<Projet>** : <phrase auto-portante : sujet + résultat>.
- 🔄 **<Projet>** : <en cours>.

## Décisions
- **<sujet>** : <décision qui se comprend seule>.

## Fichiers / artefacts
- `<chemin>` — <ce que c'est>.

## À faire (utilisateur)
- ⏳ <action explicite>.

## Liens
[[<Note_Projet>]]
```

**Règles d'or :**
1. Le bloc `**Résumé.**` en prose est OBLIGATOIRE (c'est le meilleur passage pour une
   recherche sémantique, qui indexe le corps, pas le frontmatter).
2. Chaque ligne nomme son sujet (projet en gras) → compréhensible hors contexte.
3. Statut visible : ✅ fait · 🔄 en cours · ⏳ à faire.
4. Frontmatter = filtrage ; prose = sens.
5. Omets entièrement une section vide.
Si `$ARGUMENTS` est fourni, utilise-le comme titre court.

## 3. Écrire la note

`<vault>/06_Claude/sessions/<AAAA-MM-JJ>_<HH>h<MM>_<slug>.md`
(`<slug>` = kebab-case court dérivé du titre). Crée le dossier s'il manque.
Si une note de cette session existe déjà : **mets-la à jour**, n'en crée pas une deuxième.

## 4. Relier à la daily note

Daily : `<vault>/03_Journal/<AAAA-MM-JJ>.md`.
- Si elle existe : sous le titre `## Sessions Claude Code` (sans dupliquer), ajoute :
  `- **<HH>h<MM>** — [[<AAAA-MM-JJ>_<HH>h<MM>_<slug>|<titre court>]] — <une ligne>`
- Sinon : crée-la en miroir d'une daily récente de `03_Journal/` (lis-en une pour
  copier la structure), puis insère la ligne.

## 5. Confirmer

Affiche : le chemin de la note, la ligne daily ajoutée, les wikilinks posés.

## 6. Optionnel — agenda

Si `gws` est installé et authentifié, propose (sans l'exécuter) la commande qui
journaliserait la session dans l'agenda de l'utilisateur. **Toute écriture externe
attend son accord explicite.**

## Interdits

- Ne modifie JAMAIS une note de `02_Projets/` (le maillage se fait par les wikilinks
  → backlinks Obsidian).
- N'écris jamais hors du vault.
