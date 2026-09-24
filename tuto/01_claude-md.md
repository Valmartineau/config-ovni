# 01 — CLAUDE.md : la mémoire de Claude Code

## Le problème

Chaque session démarre **vide**. Claude ne se souvient ni de vous, ni de votre
projet, ni de la façon dont vous aimez travailler. Le fichier `CLAUDE.md` est la
réponse : un texte que Claude lit **au démarrage de chaque session**.

## La cascade

Claude Code charge tous les `CLAUDE.md` qu'il trouve du dossier racine jusqu'au
dossier courant, et les **concatène**. Le plus proche de vous est lu en dernier.

```
~/.claude/CLAUDE.md          ← VOUS (toutes les sessions, toutes les machines… la vôtre)
~/CLAUDE.md                  ← votre machine (si vous lancez claude depuis ~)
~/projets/monprojet/CLAUDE.md  ← LE PROJET (commité, partagé avec l'équipe)
~/projets/monprojet/CLAUDE.local.md  ← vous, sur ce projet (gitignoré)
~/projets/monprojet/sousdossier/CLAUDE.md  ← chargé à la demande
```

Règle d'or : **chaque information vit au niveau le plus précis qui couvre tous ses
usages, jamais en double.** Votre langue et vos préférences de lecture : niveau
utilisateur. Les commandes de build du projet : niveau projet. Les particularités
d'un module : niveau module.

## Quoi mettre dedans

Ce que Claude **ne peut pas deviner** en lisant le code :

- Langue de réponse, ton, format (phrases courtes, tableau ou pas…).
- Votre méthode de travail (voir `09_methode.md`).
- Les interdits absolus (dossiers à ne jamais lire, comptes à ne jamais utiliser).
- Les commandes de test, de lancement, de déploiement.
- Les pièges connus du projet.

Ce qu'il ne faut **pas** mettre : ce que Claude voit déjà dans le code, l'historique
git, la documentation. Visez **moins de 200 lignes** par fichier. Plus c'est long,
moins c'est suivi.

## Les imports

Une ligne `@chemin/vers/fichier.md` dans un `CLAUDE.md` insère ce fichier au
chargement. Chemins relatifs (au fichier qui importe) ou absolus (`@~/.claude/x.md`).
Profondeur maximale : 4 niveaux. Un `@` entre backticks n'est pas un import.

Piège vérifié : les imports de `~/CLAUDE.md` (racine de votre home) ne sont **pas**
résolus quand vous lancez `claude` dans un projet. Ce qui doit être lu partout
s'importe depuis `~/.claude/CLAUDE.md`.

## Commandes utiles

- `/init` : Claude analyse le projet et propose un `CLAUDE.md` de départ.
- `/memory` : voir et éditer les fichiers de mémoire chargés.
- `#` en début de message : « retiens ça » → Claude propose de l'ajouter au CLAUDE.md.

## Exercice

1. Copiez `modeles/CLAUDE.md.utilisateur` vers `~/.claude/CLAUDE.md`.
2. Remplissez les `<...>`. Gardez-le court.
3. Ouvrez une nouvelle session dans n'importe quel dossier et demandez :
   « Qu'est-ce que tu sais de moi ? ». Claude doit citer votre fichier.
4. Dans un projet, lancez `/init`, relisez ce qu'il propose, gardez la moitié.

## Retirer

Supprimez le fichier. Rien d'autre n'en dépend.
