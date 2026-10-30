---
name: audit-acces
description: Use quand l'utilisateur veut auditer les droits d'accès d'une application — qui a le droit de créer, lire, modifier, supprimer quoi. Bâtit la matrice CRUD visiteur/utilisateur/admin, débusque les fuites (URL directe, recherche, export, identifiant deviné), applique le principe « cacher n'est pas protéger » et rend un plan de test croisé A/B/Admin. Déclenché par "/audit-acces", "qui a le droit de voir quoi", "audite les permissions", "un client peut-il voir les données d'un autre", "formulaire public enregistrements privés". Preuve de posture RGPD sans jargon juridique.
---

# /audit-acces — Qui a le droit de voir quoi ?

Quatre facettes d'un même geste : la **matrice CRUD** (Créer / Lire / Modifier /
Supprimer) pour trois profils, la distinction **propriété vs visibilité**, le motif
**formulaire public / enregistrements privés**, et la règle **cacher n'est pas
protéger**. Sortie : une matrice par table + un plan de test croisé
Utilisateur A / Utilisateur B / Admin. C'est le prompt qui prouve la posture RGPD
sans employer un mot de droit.

## Quand l'utiliser

- Sur toute appli qui distingue visiteur, utilisateur connecté et administrateur.
- Formulaire de contact / candidature / demande de devis : n'importe qui écrit,
  personne d'autre ne lit.
- Espace où « chacun ne voit que ses données ».
- Avant une mise en ligne, ou au moindre doute « un client peut-il voir les
  données d'un autre ? ».

## Garde-fous (non négociables)

- **Ne change aucun droit tant que la matrice n'est pas validée.** L'audit
  produit un diagnostic + une proposition de règles ; l'application des règles
  attend un « go » humain explicite.
- **Cacher ≠ protéger.** Un lien masqué, une page absente du menu, un bouton grisé
  ne sont PAS des autorisations. Les mêmes règles doivent tenir sur les routes ET
  sur les données. Ce qui est visible doit refléter ce qui est réellement autorisé.
- **Tester pour de vrai, annoncer ce qu'on a observé.** Ne jamais affirmer qu'une
  règle tient sans avoir joué le test croisé. Séparer ce qui a été vérifié de ce
  qui est supposé.
- **Chemins de fuite obligatoires à sonder** : URL directe, recherche, export,
  identifiant deviné, code de la page publique. Une donnée privée ne doit fuiter
  par aucun.

## Les prompts intégrés

### 1 · Auditer les droits d'accès (la matrice, le prompt-socle)

```text
Ne change aucun droit pour l'instant.

Audite chaque table pour trois profils : visiteur non identifié, utilisateur
connecté ordinaire, administrateur. Rends une matrice Créer / Lire / Modifier /
Supprimer.

Signale tout chemin par lequel un utilisateur pourrait lire ou modifier
les données privées d'un autre — y compris par une URL directe, une recherche,
un export ou un identifiant deviné.

Propose les règles les plus restrictives qui laissent le vrai usage fonctionner,
puis un plan de test croisé (Utilisateur A / Utilisateur B / Admin).

Attends ma validation avant d'appliquer quoi que ce soit.
```

### 2 · Formulaire public, enregistrements privés

```text
Configure [TABLE] ainsi : un visiteur non identifié peut Créer un enregistrement,
mais ne peut jamais le Lire, le Modifier ni le Supprimer. Seuls les administrateurs
peuvent Lire, Modifier et Supprimer.

Aucun champ interne ne doit apparaître dans une réponse publique ni sur une page
publique — y compris dans le code de la page.

Montre-moi la matrice exacte, puis teste-la réellement en visiteur puis en admin,
et dis-moi ce que tu as observé.
```

### 3 · Chaque utilisateur ne voit que ses propres données (propriété)

```text
Pour [TABLE], exige la connexion. Chaque utilisateur peut Créer, et peut Lire,
Modifier ou Supprimer uniquement les enregistrements qui lui appartiennent.
L'accès administrateur doit être explicite, jamais implicite.

Explique quel champ ou quelle règle établit précisément la propriété.
Teste avec Utilisateur A, Utilisateur B et Admin, et montre-moi les résultats.
```

### 4 · Navigation par rôle — cacher n'est pas protéger

```text
Adapte la navigation : [RÔLE A] voit [ÉLÉMENTS], [RÔLE B] voit [ÉLÉMENTS].

Cacher un lien n'est pas une autorisation. Applique les mêmes règles sur les
routes et sur les données elles-mêmes. Taper directement l'adresse d'une page
interdite ne doit révéler ni son contenu, ni ses enregistrements, ni leur existence.

Teste les trois cas : déconnecté, Rôle A, Rôle B. Dis-moi ce que tu as observé
dans chacun.
```

## Sortie attendue

1. **Matrice CRUD par table** — trois colonnes de profil (visiteur / utilisateur
   ordinaire / admin), quatre lignes d'action (Créer / Lire / Modifier /
   Supprimer), pour chaque table sensible. Deux motifs récurrents documentés :
   *public en écriture, privé en lecture* (prompt 2) et *propriété par
   utilisateur* (prompt 3).
2. **Liste des chemins de fuite** — chaque voie testée (URL directe, recherche,
   export, identifiant deviné, code de page) avec le verdict : bloqué / à corriger.
3. **Règles proposées** — les plus restrictives qui laissent le vrai usage
   fonctionner, appliquées AUX routes ET aux données (jamais seulement à
   l'affichage). En attente de validation.
4. **Plan de test croisé A / B / Admin** — un script manuel, rôle par rôle, que
   l'utilisateur (ou son client) peut rejouer : Utilisateur A ne doit rien atteindre de
   l'Utilisateur B, même par URL directe ; l'accès admin est explicite.

> Règle d'or du rendu : ce qui n'a pas été réellement testé est annoncé comme
> « non vérifié », jamais comme « conforme ».
