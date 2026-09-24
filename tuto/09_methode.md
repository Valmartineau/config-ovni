# 09 — Méthode de travail avec un agent

Ce chapitre est le plus important et le plus court. C'est le bloc à copier dans
votre `CLAUDE.md` utilisateur (il y est déjà dans `modeles/CLAUDE.md.utilisateur`).

## Le pipeline, dans l'ordre

1. **Comprendre d'abord.** Tracer le flux réel de bout en bout avant de toucher au
   code. Un petit diff au mauvais endroit n'est pas de la paresse, c'est un deuxième bug.
2. **Cause racine, pas symptôme.** Un rapport nomme un symptôme. Chercher tous les
   appelants, corriger **une** fois la fonction partagée.
3. **Simplicité ensuite.** Le minimum qui résout le problème, rien de spéculatif.
   Test : « un dev senior dirait-il que c'est sur-compliqué ? » Si oui, réécrire.
4. **Changements chirurgicaux.** Ne toucher que ce qui trace vers la demande.
   Signaler le code mort, ne pas le supprimer sans accord.
5. **Tracer les raccourcis.** Tout raccourci assumé porte un commentaire qui nomme
   le plafond **et** le chemin d'upgrade. (Convention du kit : `ponytail:`.)
6. **Ne jamais simplifier** : validation aux frontières de confiance, gestion d'erreur
   anti-perte de données, sécurité, accessibilité, et tout ce qui est explicitement demandé.
7. **Vérifier avant de dire fini.** Logique non triviale = un check exécutable
   (assert ou petit test) + exercer le vrai flux, pas juste compiler. Annoncer les
   résultats tels quels, échecs compris.
8. **État visible = état réel.** Toute fonctionnalité non validée bout en bout est
   grisée « en cours » et inerte.

## Ce que ça change avec un agent

- **Vous êtes le pilote.** L'agent propose, vous décidez. Les gestes sortants (mail,
  push, publication, paiement) sont les vôtres.
- **Un doute > 10 % = une question**, pas une improvisation. Surtout avant d'armer
  une autonomie (`/porte`).
- **Annoncer le coût** avant un gros chantier : « ~20 min, gros contexte ». Le
  parallélisme vide le quota : deux sessions lourdes en même temps, c'est deux fois
  la facture.
- **Sourcer chaque fait.** Un chiffre sans source est un trou visible, pas une
  estimation confiante. Dater depuis l'horloge système, jamais depuis une API tierce.
- **Ne jamais nommer un client ou un concurrent** dans un livrable qui sort.
- **Une indisponibilité a une valeur fermée**, jamais zéro : « inconnu » ≠ « 0 ».

## Souveraineté, en une phrase

Avant de brancher un outil : *où vont mes données, qui les garde, et comment je
repars sans lui ?* Si vous ne pouvez pas répondre aux trois, vous ne le branchez pas
encore. Ce n'est pas une position militante ; c'est de l'ingénierie : une dépendance
qu'on ne peut pas retirer est un risque qu'on n'a pas chiffré.

## Rituel de session

- Début : Claude lit vos `CLAUDE.md`, le hook SessionStart lui dit l'état du vault.
- Fin de phase : `/session-note`. Fin de journée : `/bye`.
- Chaque mois : relire ses skills, en supprimer un, en améliorer un.
