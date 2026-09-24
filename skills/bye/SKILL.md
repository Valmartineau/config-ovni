---
name: bye
description: Clôture de session — archive la session (skill session-note) puis dit au revoir. Déclenché par "/bye", "on arrête là", "à demain".
disable-model-invocation: true
argument-hint: "[titre court optionnel]"
---

L'utilisateur clôt sa session de travail. Avant de saluer, **archive la session**.

1. Invoque le skill **`session-note`** (outil Skill) — suis sa procédure. Si
   `$ARGUMENTS` est fourni, passe-le comme titre court. Finalise la note en statut
   `termine`.

2. Conclus par un court message d'au revoir (1 phrase) qui rappelle le chemin de la
   note créée.
   **La salutation suit l'horloge système, pas la fin de session** : lis `date` et
   salue en conséquence (« bonne fin de journée », « bon week-end », « bonne soirée »
   après ~20 h, « bonne nuit » seulement passé minuit). Clore une session à 16 h n'est
   pas clore la journée.

Si la session n'a rien produit d'archivable (aucune action ni décision), ne force pas
la note : dis-le et salue simplement.
