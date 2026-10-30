---
name: souverainete-check
description: Use quand l'utilisateur veut passer une application au crible de la souveraineté — cartographier ce qui sort du périmètre, classer les dépendances externes et tester la réversibilité avant de brancher (ou de garder) un service. Déclenché par "/souverainete-check", "où vont mes données", "qu'est-ce qui sort quand je branche X", "test de réversibilité", "de quoi dépend cette appli". Produit un tableau de flux de données + un classement de dépendances par douleur + une porte de sortie.
---

# /souverainete-check — Où vont mes données, et qu'est-ce qui me tient ?

Trois prompts en un geste, pour répondre à une seule question : **« qu'est-ce qui
sort de mon périmètre, et de quoi suis-je prisonnier ? »**. C'est une version
auto-service d'un contrôle RGPD : on vérifie soi-même, sans jargon juridique.

## Quand l'utiliser

- Avant de brancher un service externe (IA, e-mail, paiement, analyse, cartes…).
- Sur une appli existante, pour dresser l'ossature d'un registre de traitement.
- Quand on demande « suis-je dépendant ? », « et si le fournisseur ferme ? ».
- En amont d'un audit RGPD, comme matière brute.

## Garde-fous (non négociables)

- **Ne rien coder, ne rien modifier.** Chaque prompt commence par « ne modifie
  rien » / « ne code rien pour l'instant » : ce skill produit un diagnostic, pas
  un correctif. Toute mise en œuvre attend une validation humaine explicite.
- **Ne jamais opposer local et cloud français.** On compare honnêtement les
  options, on ne condamne pas le cloud : un service hébergé en Europe est une
  réponse légitime. Le prompt demande une comparaison, pas un verdict.
- **Le RGPD n'impose PAS l'Europe.** Argumenter la *simplicité de conformité* du
  local ou de l'européen, jamais une interdiction du reste.
- **Ne jamais nommer un concurrent** dans le livrable rendu :
  conception et réserve défensive, pas dénigrement.
- **Honnêteté du constat** : une donnée dont l'usage n'a pas été trouvé se dit
  telle quelle (« aucun usage identifié »), on ne l'invente pas.

## Les prompts intégrés

### 1 · Où vivent mes données ? (carte des flux)

```text
Ne modifie rien.

Dresse la carte des données de cette application. Pour chaque donnée collectée :

| Donnée | À quoi elle sert | Où elle est stockée | Qui y a accès | Qui la traite en dehors de chez moi | Combien de temps on la garde |

Marque d'un signe distinct : les données personnelles, les données sensibles
(santé, opinions, données de mineurs), et celles dont aucun usage réel
n'a pu être identifié.

Pour chaque donnée qui sort de mon périmètre, nomme le service qui la reçoit
et dis s'il existe une alternative qui garderait la donnée chez moi.

Termine par : les trois données que je devrais cesser de collecter dès demain,
et pourquoi.
```

### 2 · Ce que je saurais faire sans le service (test de réversibilité)

```text
Ne modifie rien.

Liste tous les services externes dont dépend cette application (hébergement,
base de données, envoi d'e-mails, authentification, paiement, intelligence
artificielle, analyse d'audience, polices de caractères, cartes).

Pour chacun : ce qui cesse de fonctionner s'il disparaît demain, combien
de temps il me faudrait pour le remplacer, si mes données sont récupérables
dans un format ouvert, et s'il existe une option auto-hébergée ou européenne.

Classe-les par « douleur en cas de disparition ».
Dis-moi lequel je devrais découpler en premier, et pourquoi.
```

### 3 · Faire sortir des données vers un service externe (avant de brancher)

```text
Ne code rien pour l'instant.

Je veux relier [FONCTION] à [FOURNISSEUR]. Avant toute chose, réponds à ceci :

1. Quelles données précises sortent de mon périmètre ? Liste les champs, un par un.
2. Où sont-elles traitées et stockées, et par qui ?
3. Ce service est-il indispensable, ou existe-t-il une option qui garde
   la donnée chez moi (traitement local, service hébergé en Europe,
   simple calcul sans appel externe) ? Compare-les honnêtement.
4. Que se passe-t-il le jour où ce fournisseur ferme, double son prix
   ou change ses conditions ? Quelle est ma porte de sortie ?

Puis seulement, propose la mise en œuvre la plus simple qui soit sûre :
identifiants stockés côté serveur et jamais transmis au navigateur,
validation des entrées côté serveur, contrôle du rôle appelant,
gestion des délais d'attente et des limites de débit, relances rejouables
sans dégât, journal contenant l'issue mais aucune donnée personnelle.

Montre-moi le flux et les tests avant d'implémenter.
```

## Sortie attendue

1. **Tableau de flux de données** (prompt 1) : une ligne par donnée, colonnes
   usage / stockage / accès / sous-traitant / durée. Les données personnelles,
   sensibles et « sans usage » sont marquées. C'est l'ossature d'un registre de
   traitement, produit sans employer le mot.
2. **Classement de dépendances** (prompt 2) : services externes triés par
   « douleur en cas de disparition », avec réversibilité (format ouvert ?
   alternative auto-hébergée / européenne ?) et le premier à découpler.
3. **Test de réversibilité au branchement** (prompt 3) : les quatre questions de
   souveraineté (quoi sort, où, alternative locale, porte de sortie) répondues
   AVANT toute implémentation, puis le schéma de mise en œuvre sûre.

Trois données à cesser de collecter et un service à découpler en priorité :
ce sont les deux recommandations actionnables à mettre en tête du rendu.
