<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site a9c0064). Ne pas modifier à la main : relancer le script. -->

# 6. Notre bibliothèque

Peu d'éléments, tous audités. Chaque fiche dit ce qui sort de votre machine, en plus de ce que Claude lit. Pour aller plus loin : `manuel/07_catalogue-par-metier.md`.

| Commande | Ce qu'il fait | Ce qui sort, en plus |
|---|---|---|
| `/porte` | Laisse Claude coder seul sur une tâche bornée, dans une copie isolée, jusqu'à votre feu vert. | Aucun accès web demandé : une consigne, pas un verrou. |
| `/lisible` | Fait écrire Claude court et simple, pour une lecture dyslexique ou pressée. | Aucun autre service. |
| `/session-note` | Archive la session dans une note de votre vault. | La note reste sur votre machine. |
| `/bye` | Clôt la session : l'archive, puis au revoir. | L'archive reste sur votre machine. |
| `/to-do` | Transforme une idée en tâche exécutable, la note et la classe. | La file est un fichier local. |
| `/micom` | Transforme un sujet en post, selon votre charte. | Ne publie jamais : la publication reste votre geste. |
| `/statusline-aide` | Explique chaque segment de la ligne d'état. | La légende vient d'un script local. |
| `/audit-acces` | Audite qui peut créer, lire, modifier ou supprimer quoi. | Le code montré part chez Anthropic : choisissez. |
| `/souverainete-check` | Cartographie ce qui sort quand vous branchez un service. | Le descriptif donné part chez Anthropic. |
| `/fermer-sessions` | Aide à fermer les sessions en arrière-plan. | Agit sur les sessions locales. |
| `/animejs` | Écrit et relit des animations anime.js version 4. | Un CDN serait un appel tiers : préférez le local. |
| `/boussole` | Passe un projet à la boussole : ce qui est conçu, ce qui est reçu, les angles morts. | La description du projet part chez Anthropic. |


## Comment un élément entre dans la bibliothèque

1. **Repérer.** Un élément entre par la veille, ou un membre le propose.
2. **Évaluer.** Utilité, effort, risque. La plupart s'arrêtent ici.
3. **Licence.** Vérifiée élément par élément, pas seulement à la racine du dépôt.
4. **Nettoyer.** On retire chemins, noms, comptes et clés.
5. **Contrôler.** Un contrôle automatique cherche ce qui aurait échappé. Il faut zéro alerte.
6. **Publier.** Le push reste un geste humain.
7. **Exposer.** Une fiche dit ce qu'il fait et ce qui sort de votre machine.

## Proposer un élément

1. Retirez chemins, noms, comptes et clés.
2. Vérifiez la licence de chaque élément repris.
3. Écrivez ce qui sort de la machine, sans enjoliver.
4. Faites-le tester par quelqu'un d'autre, sur une autre machine.

## La licence

Le kit est sous **CC BY-NC 4.0** : copier, modifier et partager en citant OVNI Conseil, sans usage commercial. Le skill `lisible` reste sous MIT. Détails dans `NOTICE` et `LICENSE`.
