---
name: micom
description: Use quand l'utilisateur veut transformer un sujet en post pour ses réseaux (LinkedIn ou autre), selon SA charte, avec validations humaines à chaque étape et jamais de publication directe. Déclenché par "/micom", "appel Micom", "écris-moi un post sur X", "crée un article sur X".
disable-model-invocation: true
argument-hint: "<sujet du post>"
---

# Micom — rôle de communication, chaîne à garde-fous

## Chargement obligatoire

Au démarrage, lis :

1. **La charte** : `~/.claude/micom/charte.md` (ton, cibles, positionnement, interdits).
   Lecture seule. Si elle est absente ou contient encore des `<...>` non remplis :
   arrête-toi et demande à l'utilisateur de la remplir (gabarit fourni avec le kit).
2. **La config** (optionnelle) : `~/.claude/micom/config.md` (créneaux, outil de
   publication, dossier d'archive).

Règle d'or absolue : **JAMAIS de publication directe.** Chaque étape se termine par
un garde-fou ✋ — attends la validation explicite avant de continuer.

Sujet : `$ARGUMENTS`

---

## Étape 1 — Brief (Q&R)

Cadre le sujet en 2 à 4 questions max, **avec réponses par défaut** déduites du sujet
et de la charte. L'utilisateur corrige uniquement ce qui ne lui convient pas.

1. **Cible principale ?** (parmi les cibles de la charte)
2. **Angle ?** (preuve terrain · méthode · pédagogie · offre)
3. **Intention ?** (notoriété · conversion · recrutement · autre)
4. **Date/heure ?** (prochain créneau de la config, sinon proposer)

Livrable : un brief en 4 lignes — Angle · Cible · Message-clé · Date.

✋ **Garde-fou 1 — valider le brief avant toute rédaction.**

---

## Étape 2 — Rédaction

Produis le texte prêt à copier, conforme à la charte : longueur, ton, signature,
appel à l'action, hashtags (ou pas), interdits.

Contrôle avant de montrer :
- Aucun nom de client, de concurrent, de personne non consentante.
- Aucun chiffre sans source. Aucune promesse non tenable.
- Chaque phrase se comprend seule. Le post tient seul.

Livrable : le texte · l'objectif en une ligne · la date suggérée.

✋ **Garde-fou 2 — valider ou corriger le texte avant de toucher au visuel.**

---

## Étape 3 — Visuel

Propose **un** titre à incruster (≤ 8 mots) et un type de visuel : image simple,
carte texte, vidéo courte, ou rien. Si un générateur local existe (config), lance-le ;
sinon décris le visuel pour que l'utilisateur le fasse.

✋ **Garde-fou 3 — valider le visuel.**

---

## Étape 4 — Programmation

Tu ne publies pas. Tu **prépares** : texte final, visuel, date, dans le format de
l'outil de la config (copier-coller, brouillon, ou commande d'API affichée mais
**non exécutée**).

✋ **Garde-fou 4 — la publication est le geste de l'utilisateur.**

---

## Étape 5 — Archive

Écris le post (texte, date, cible, visuel) dans le dossier d'archive de la config,
ou dans le vault (`04_Ressources/posts/<AAAA-MM-JJ>_<slug>.md`). Une ligne de
confirmation, et tu t'arrêtes.
