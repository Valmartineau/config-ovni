---
paths:
  - "tests/**/*"
  - "**/*.test.*"
  - "**/*_test.py"
---
# Règles pour les fichiers de test

- Un test vérifie **une** chose et son nom la dit : `test_refuse_un_montant_negatif`.
- Pas de dépendance réseau dans un test : on simule (mock) la frontière, pas l'intérieur.
- Un test qui échoue doit dire **pourquoi** dans son message d'assertion.
- Ne jamais désactiver un test pour faire passer la suite : le signaler.
