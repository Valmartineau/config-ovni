#!/usr/bin/env python3
"""
depuis_le_site.py — recopie dans ce dépôt tout le contenu de la page Config OVNI
(ovniconseil.fr, page à code), pour que le Claude Code des membres en sache autant qu'eux.

    python3 outils/depuis_le_site.py <dépôt du site ovniconseil>

Le dépôt du site doit avoir ses node_modules (l'export lit les données TypeScript de la page).
Produit : manuel/ (fiches), etape-2-ia-locale/, etape-3-construire/, exercices/boucle-voix/.

Les données (commandes, catalogue, pannes, parcours de NOVI, grilles) sont lues dans la page :
elles suivent le site à chaque relance. Le texte rédigé des chapitres est recopié ici.
ponytail: plafond = un texte rédigé modifié sur la page n'est pas repris tout seul ; le test
test_depuis_le_site.py vérifie les données, pas la prose. Upgrade : faire lire la prose
de la page dans un fichier commun aux deux dépôts.
"""
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PAGE = "app/l/config-ovni-k7m2xq9tfd"
PUBLIC = "public/l/config-ovni-k7m2xq9tfd"
ENTETE = ("<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI "
          "(site {commit}). Ne pas modifier à la main : relancer le script. -->\n\n")
NOMS = {"mac": "Mac", "windows": "Windows", "linux": "Linux"}

# Les commandes de la page supposent les fichiers dans Téléchargements. Dans le dépôt, ils sont ici.
CHEMINS = [
    ("~/Downloads/config-ovni-mods/", "etape-3-construire/mods/"),
    ("$HOME\\Downloads\\config-ovni-mods\\", "etape-3-construire\\mods\\"),
    ("~/Downloads/choisir-modele.py", "etape-2-ia-locale/choisir-modele.py"),
    ("$HOME\\Downloads\\choisir-modele.py", "etape-2-ia-locale\\choisir-modele.py"),
]


def chemins(c: str) -> str:
    for a, b in CHEMINS:
        c = c.replace(a, b)
    return c


def bloc(cmd: dict, systemes=("mac", "windows", "linux"), note_vide="") -> str:
    """Une commande par système, regroupée quand elle est identique."""
    groupes: dict[str, list[str]] = {}
    for s in systemes:
        c = chemins(cmd.get(s) or "")
        if c:
            groupes.setdefault(c, []).append(NOMS[s])
    sortie = []
    for c, qui in groupes.items():
        etiquette = " et ".join([", ".join(qui[:-1]), qui[-1]] if len(qui) > 1 else qui)
        if len(groupes) > 1 or len(qui) < len(systemes):
            sortie.append(f"{etiquette} :\n")
        sortie.append("```\n" + c + "\n```\n")
    manquants = [NOMS[s] for s in systemes if not chemins(cmd.get(s) or "")]
    if manquants and note_vide:
        sortie.append(f"{' et '.join(manquants)} : {note_vide}\n")
    return "\n".join(sortie)


def ecrire(chemin: Path, texte: str, commit: str) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(ENTETE.format(commit=commit) + texte.strip() + "\n", encoding="utf-8")


def tableau(entetes, lignes) -> str:
    net = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
    t = "| " + " | ".join(entetes) + " |\n|" + "---|" * len(entetes) + "\n"
    return t + "".join("| " + " | ".join(net(x) for x in l) + " |\n" for l in lignes)


# ---------------------------------------------------------------- manuel/
def notions(d) -> str:
    t = ["# 1. Les notions\n",
         "Claude Code est un agent dans votre terminal. Il repart de zéro à chaque session. "
         "Une configuration lui donne une mémoire, des savoir-faire et des limites.\n",
         "## Les briques d'une configuration\n"]
    for g in d["GROUPES"]:
        t.append(f"### {g['nom']}\n")
        for b in [b for b in d["BRIQUES"] if b["groupe"] == g["id"]]:
            t.append(f"- **{b['nom']}** ({b['role']}) : {b['texte']} Où : `{b['ou']}`.")
        t.append("")
    t.append("## Ce qui est lu, selon le dossier où l'on lance `claude`\n")
    t.append(tableau(["Fichier", "Pour qui"], [(f"`{f['chemin']}`", f["pour"]) for f in d["FICHIERS_CASCADE"]]))
    t.append("Lancé depuis le dossier personnel : seul `~/.claude/CLAUDE.md` est lu. Depuis le projet : "
             "les trois premiers au démarrage, celui du module à la demande. Depuis le module : tous.\n")
    t.append("## L'ordre des hooks pendant un tour\n")
    t.append(" → ".join(d["EVENEMENTS"]) + "\n")
    t.append("Un hook `PreToolUse` peut bloquer l'outil avant qu'il agisse (code de sortie 2).\n")
    t.append("## Ce qui sort de votre machine\n")
    for s in d["SCENARIOS"]:
        t.append(f"- **{s['nom']}** : " + " ".join(s["sort"]))
    t.append("\n## Où ranger une consigne : les questions, dans l'ordre\n")
    t += [f"{i}. {q['texte']} → **{q['brique']}**" for i, q in enumerate(d["QUESTIONS"], 1)]
    t.append("\nExemples :\n")
    t.append(tableau(["Situation", "Brique", "Pourquoi"], [(s["texte"], s["brique"], s["pourquoi"]) for s in d["SITUATIONS"]]))
    return "\n".join(t)


METHODE = """# 2. La méthode

L'outil compte moins que la façon de s'en servir. Vous êtes le pilote : l'agent propose, vous décidez.

## Le pipeline, dans l'ordre

1. **Comprendre d'abord.** Tracer le flux réel avant de toucher à quoi que ce soit.
2. **Cause racine.** Un rapport nomme un symptôme. Corriger une seule fois, au bon endroit.
3. **Simplicité.** Le minimum qui résout le problème.
4. **Changements chirurgicaux.** Ne toucher que ce que la demande exige.
5. **Tracer les raccourcis.** Dire le plafond et le chemin d'amélioration.
6. **Ne jamais simplifier** la sécurité, l'accessibilité, la protection des données.
7. **Vérifier avant de dire fini.** Exercer le vrai flux, annoncer les échecs.
8. **État visible égale état réel.** Ce qui n'est pas validé est affiché comme tel.

## Les règles du collectif

- **Rien ne sort sans votre accord :** mail, publication, push et paiement restent vos gestes.
- **Aucun secret** dans un fichier du kit ni dans `settings.json`.
- **Votre propre compte Google,** jamais celui d'un autre.
- **Ce que Claude lit part au modèle.** Réfléchissez avant de lui montrer des données de client.
- **Aucun nom de client ou de concurrent** dans ce qui sort.

## Avant de brancher un outil

1. Où vont mes données ?
2. Qui les garde ?
3. Comment je repars sans lui ?

Sans ces trois réponses, on ne branche pas encore.
"""


def installer(d) -> str:
    t = ["# 3. Installer pas à pas\n",
         "Il faut une offre Claude Pro, Max, Team ou Enterprise. Le plan gratuit ne donne pas accès à Claude Code.\n",
         "1. **Installer Claude Code.** Ouvrez un terminal (Mac : Commande + Espace, « terminal » ; "
         "Windows : menu Démarrer, « PowerShell »).\n",
         "   macOS, Linux : `curl -fsSL https://claude.ai/install.sh | bash`",
         "   Windows, PowerShell : `irm https://claude.ai/install.ps1 | iex`",
         "   Windows, CMD : `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`\n",
         "2. **Vérifier :** `claude --version` puis `claude doctor`.",
         "3. **Récupérer le kit et lancer Claude dedans :** `git clone https://github.com/Valmartineau/config-ovni.git`, "
         "`cd config-ovni`, `claude`. La première fois, connectez-vous dans le navigateur.",
         "4. **Lui demander de conduire :** « installe le kit ». Une étape à la fois, avec votre accord.",
         "5. **Contrôler :** `python3 outils/verifier.py` (Windows : `python`).\n",
         "**Sur Windows :** installez Git for Windows, dont Claude Code se sert pour les hooks et la status line. "
         "La commande CMD ne marche pas dans PowerShell. Si `claude` n'est pas reconnu, fermez et rouvrez le terminal.\n",
         "## Les stations de l'installation\n"]
    t += [f"{i}. **{s['nom']}**{' (facultatif)' if s['option'] else ''} : {s['texte']}" for i, s in enumerate(d["STATIONS"], 1)]
    return "\n".join(t)


TUTOS = """# 4. Six tutos

Chaque tuto se termine par un résultat que vous pouvez vérifier seul.

## Écrire votre CLAUDE.md

1. Dans une session, tapez `/memory` et ouvrez `~/.claude/CLAUDE.md`.
2. Écrivez votre langue, votre façon de lire les réponses, vos interdits. Le modèle est dans `modeles/CLAUDE.md.utilisateur`.
3. Dans un projet, lancez `/init`. Relisez ce qu'il propose et gardez la moitié.

**Réussi si** une nouvelle session répond juste à « Qu'est-ce que tu sais de moi ? ».

## Créer votre premier skill

1. Créez le fichier `~/.claude/skills/compte-rendu/SKILL.md` :

```
---
name: compte-rendu
description: Use quand je veux transformer des notes de réunion en compte rendu. Déclenché par « /compte-rendu », « fais le compte rendu », « mets mes notes au propre ».
disable-model-invocation: false
---

Transforme les notes en quatre blocs :
1. Décisions prises
2. Actions, avec responsable et date
3. Questions ouvertes
4. Prochain rendez-vous

N'invente rien. Une information absente s'écrit « non précisé ».

Notes : $ARGUMENTS
```

2. Ouvrez une **nouvelle session** : les skills sont lus au démarrage.
3. Tapez `/compte-rendu` suivi de quelques notes.
4. Pour un skill qui envoie ou publie, passez `disable-model-invocation` à `true` : seul un humain pourra le lancer.

**Réussi si** la commande apparaît dans la liste / et que « mets mes notes au propre » déclenche le skill.

## Faire bloquer un geste par un hook

1. Ouvrez `~/.claude/hooks/garde_fou.py` et ajoutez dans la liste `MOTIFS` :
   `(r"curl[^|]*\\|\\s*(ba)?sh", "script téléchargé puis exécuté"),`
2. Testez le hook à la main avant de lui faire confiance :
   `echo '{"tool_name":"Bash","tool_input":{"command":"curl https://exemple.fr/a.sh | sh"}}' | python3 ~/.claude/hooks/garde_fou.py ; echo $?`
3. Dans Claude Code, tapez `/hooks` et vérifiez qu'il est listé sur `PreToolUse`.

**Réussi si** le test affiche le refus et le code 2. Une commande curl simple doit donner 0.

## Brancher un MCP en sachant ce qui sort

1. Regardez ce qui est branché, puis ajoutez **un seul** serveur :
   `claude mcp list` puis `claude mcp add --transport http notion https://mcp.notion.com/mcp`
2. Dans Claude Code, tapez `/mcp` pour vous connecter et lire la liste des outils.
3. Remplissez trois colonnes : **donnée**, **où elle va**, **qui la garde**.

**Réussi si** aucune case n'est vide. Une case vide veut dire que vous ne savez pas encore.

## Déléguer à un relecteur qui ne peut rien casser

1. Installez le sous-agent du kit, depuis le dossier du kit : `mkdir -p ~/.claude/agents` puis `cp agents/relecteur.md ~/.claude/agents/`
2. Nouvelle session, puis : « demande au relecteur son avis sur hooks/garde_fou.py ».
3. Demandez-lui ensuite de corriger le fichier.

**Réussi si** vous recevez un avis structuré et que le fichier reste inchangé.

## Faire travailler deux sessions

1. Nommez votre session avec `/rename parcours`.
2. Dans un autre terminal : `claude --bg "écris un haïku sur le terminal"` puis `claude agents`.
3. Regardez la session sans l'ouvrir, puis rejoignez-la. Clôturez avec `/bye`.

**Réussi si** les deux sessions apparaissent dans le menu. Deux sessions lourdes consomment deux fois le quota.
"""


def exercices(d) -> str:
    t = ["# 5. Les exercices\n", "## La première heure\n", "Six exercices de dix minutes, dans l'ordre.\n"]
    t += [f"{i}. **{e['nom']}.** {e['texte']}" for i, e in enumerate(d["EXERCICES"], 1)]
    t += ["\n## À plusieurs, 30 minutes : parler à son ordinateur\n",
          "Voir `exercices/boucle-voix/` : le dossier de l'exercice avec son coach (`claude` puis `/commencer`), "
          "et `exercices/boucle-voix-en-groupe.md` pour le déroulé en groupe.\n",
          "## À faire à plusieurs\n",
          "- **La carte des données.** Chacun choisit un outil de son quotidien et remplit les trois colonnes. Comparez les cases vides.",
          "- **Relire un skill d'un autre.** Lisez la description seule et devinez quand il se déclenche. Puis lisez le corps. L'écart dit ce qu'il faut réécrire.",
          "- **Auditer un plugin.** Avant de l'installer, listez ses hooks, ses serveurs et sa licence. Décidez ensemble : on prend, on réécrit ou on laisse.",
          "- **Le ménage du mois.** Chacun supprime un skill, en améliore un et relit sa mémoire. Une mémoire fausse coûte plus cher qu'une mémoire absente."]
    return "\n".join(t)


def bibliotheque(d) -> str:
    t = ["# 6. Notre bibliothèque\n",
         "Peu d'éléments, tous audités. Chaque fiche dit ce qui sort de votre machine, en plus de ce que Claude lit. "
         "Pour aller plus loin : `manuel/07_catalogue-par-metier.md`.\n",
         tableau(["Commande", "Ce qu'il fait", "Ce qui sort, en plus"], [(f"`/{s['nom']}`", s["role"], s["sort"]) for s in d["SKILLS"]]),
         "\n## Comment un élément entre dans la bibliothèque\n"]
    t += [f"{i}. **{c['nom']}.** {c['texte']}" for i, c in enumerate(d["CHAINE"], 1)]
    t += ["\n## Proposer un élément\n",
          "1. Retirez chemins, noms, comptes et clés.", "2. Vérifiez la licence de chaque élément repris.",
          "3. Écrivez ce qui sort de la machine, sans enjoliver.", "4. Faites-le tester par quelqu'un d'autre, sur une autre machine.\n",
          "## La licence\n",
          "Le kit est sous **CC BY-NC 4.0** : copier, modifier et partager en citant OVNI Conseil, sans usage commercial. "
          "Le skill `lisible` reste sous MIT. Détails dans `NOTICE` et `LICENSE`."]
    return "\n".join(t)


def catalogue(d) -> str:
    metiers = {m["id"]: m["nom"] for m in d["METIERS"]}
    t = ["# 7. Le catalogue selon votre métier\n",
         f"Des skills d'autres auteurs, installés depuis leur source d'origine : rien n'est recopié ici. "
         f"{len(d['CATALOGUE'])} entrées. Relecture par OVNI le {d['DATE_RELECTURE']} : consignes principales et scripts lus, "
         "aucun skill exécuté. Une mise à jour d'un skill annule sa relecture. "
         "**Les commandes d'installation n'ont pas été lancées par OVNI : lisez avant.**\n",
         "## Par métier\n"]
    for mid, nom in metiers.items():
        noms = [e["nom"] for e in d["CATALOGUE"] if mid in e["metiers"]]
        t.append(f"- **{nom}** : " + ", ".join(noms))
    t.append("\n## Les fiches\n")
    for e in d["CATALOGUE"]:
        t.append(f"### {e['nom']}\n")
        t.append(e["role"] + "\n")
        meta = [f"Source : https://github.com/{e['depot']}", f"licence {e['licence']}"]
        if e.get("version"): meta.append(f"version {e['version']}")
        meta.append(f"relu le {e['relu']}" if e.get("relu") else "**non relu**")
        t.append(" · ".join(meta) + "  ")
        t.append("Métiers : " + ", ".join(metiers.get(m, m) for m in e["metiers"]) + "  ")
        drapeaux = []
        if e.get("paquet"): drapeaux.append(f"installe {e['paquet']} skills d'un coup" + (f" ({e['contient']})" if e.get("contient") else ""))
        if e.get("scripts"): drapeaux.append("exécute du code sur votre machine")
        if e.get("services"): drapeaux.append("se branche à des services extérieurs")
        if e.get("compte"): drapeaux.append(f"compte nécessaire : {e['compte']}")
        if drapeaux: t.append("À noter : " + " ; ".join(drapeaux) + ".")
        if e.get("vigilance"):
            t.append("\nÀ savoir :\n")
            t += [f"- {v}" for v in e["vigilance"]]
        t.append("\nInstaller :\n\n```\n" + e["install"] + "\n```\n\nRetirer :\n\n```\n" + e["retrait"] + "\n```\n")
    return "\n".join(t)


def pannes(d) -> str:
    return "\n".join([
        "# 8. En cas de panne\n",
        "Premier réflexe : `python3 outils/verifier.py` puis `claude doctor`. Si vous demandez de l'aide, "
        "envoyez la sortie brute de la commande. Fiche détaillée : `tuto/11_pannes.md`.\n",
        "## Claude Code et le kit\n", tableau(["Ce que vous voyez", "Ce qu'il faut faire"], d["PANNES"]),
        "\n## L'IA locale (étape 2)\n", tableau(["Ce que vous voyez", "Ce qu'il faut faire"], d["IA_PANNES"])])


def parcours(d) -> str:
    t = ["# 9. Le parcours guidé de NOVI, en texte\n",
         "Sur la page, NOVI lit ce parcours à voix haute. Le voici à lire, avec ses commandes.\n"]
    for ch in d["PROGRAMME"]:
        t.append(f"## {ch['nom']}\n")
        for tp in ch["temps"]:
            titre = tp.get("mot", "") + (f" : {tp['sous']}" if tp.get("sous") else "")
            if titre: t.append(f"**{titre}**\n")
            if tp.get("texte"): t.append(tp["texte"] + "\n")
            for ch_ in tp.get("question") or []:  # quiz : chaque choix et la réponse de NOVI
                t.append(f"- {ch_['l']}{' (la bonne réponse)' if ch_.get('bon') else ''} : {ch_['rep']}")
            if tp.get("question"): t.append("")
            for k in ("commande", "autre"):
                if tp.get(k):
                    if k == "autre" and tp[k].get("titre"): t.append(f"{tp[k]['titre']} :\n")
                    t.append(bloc(tp[k]))
            for k in ("note", "noteTous"):
                if tp.get(k): t.append(tp[k] + "\n")
    return "\n".join(t)


# ---------------------------------------------------------------- étapes
def etape2(d) -> str:
    c = d["IA_CMD"]
    grille = tableau(["Mémoire", "Modèle", "À télécharger", "Pour qui"],
                     [((f"moins de {d['PALIERS'][1]['min']} Go" if i == 0 else f"{p['min']} Go et plus"), f"`{p['modele']}`", p["taille"], p["note"])
                      for i, p in enumerate(d["PALIERS"])])
    A, X = d["AGENT"], d["CONTEXTE"]
    return f"""# Étape 2 : votre IA locale

Un modèle qui tourne sur votre ordinateur (Ollama), et un agent qui s'en sert (Hermes).
Vos questions ne quittent plus la machine. La taille du modèle suit la puissance de chacun.

Avant de commencer : l'étape 1 faite, un terminal ouvert, et **de 10 à 30 Go libres**.
Il faut macOS 14 ou plus récent, ou Windows 10 22H2 ou plus récent.
Les commandes ci-dessous prennent le modèle `qwen3.5:9b` (16 Go) : remplacez-le par celui de votre ligne.

## Choisir le modèle

**Avec la grille.** Mac : menu Pomme, « À propos de ce Mac », ligne Mémoire. Windows : Paramètres, Système,
Informations système (avec une carte NVIDIA, regardez plutôt sa mémoire, Gestionnaire des tâches, Performance).
Linux : `free -h`, ou `nvidia-smi` avec une carte NVIDIA. Sur un Mac à puce Apple, toute la mémoire sert au modèle.
Sur un PC, c'est celle de la carte NVIDIA qui compte. Sans carte graphique, restez sur 8 Go.

{grille}
**Avec le script qui mesure** (`etape-2-ia-locale/choisir-modele.py`, il ne télécharge et n'envoie rien), depuis le dossier du kit :

{bloc(c['script'])}
## Installer pas à pas

1. **Installer Ollama**, qui fait tourner les modèles. Sur Mac et Windows, l'application Ollama doit rester ouverte
   (installateurs : https://ollama.com/download/Ollama.dmg , https://ollama.com/download/OllamaSetup.exe).

{bloc(c['ollama'])}
{bloc(c['ollamaVerif'])}
2. **Télécharger le modèle.** Quelques minutes. C'est la seule fois où le modèle passe par internet.

{bloc(c['pull'])}
3. **Lui donner de la place pour travailler.** Par défaut, Ollama ne garde que 4 000 jetons en tête sur une machine
   de moins de 24 Go. Un agent en demande au moins 64 000. Ces lignes créent une copie du modèle, nommée `{A}`, réglée à {X}.

{bloc(c['contexte'])}
{bloc(c['liste'])}
4. **Installer Hermes**, l'agent. Si l'installation ouvre un assistant, choisissez « Custom endpoint », ou quittez-le.

{bloc(c['hermes'])}
   Fermez et rouvrez le terminal, puis :

{bloc(c['hermesVerif'])}
5. **Brancher Hermes sur votre modèle.**

{bloc(c['brancher'])}
6. **Le premier bonjour.** `ollama ps` doit montrer `{A}`, **100% GPU** et un contexte de {X}. Si le processeur
   apparaît, le modèle est trop gros : prenez le palier du dessous. Patience : sur un portable de 16 Go,
   de 2 à 4 minutes par réponse ; bien plus vite à partir de 32 Go.

{bloc(c['tester'])}
7. **Lui parler.** Pour quitter : `/exit`.

{bloc(c['parler'])}
## Ce qui reste chez vous

- **Vos questions et les réponses :** le modèle tourne sur votre machine, à l'adresse `localhost`.
- **La mémoire de Hermes** et ses réglages, dans le dossier `.hermes` de votre compte.
- **Le modèle lui-même,** une fois téléchargé : il marche sans internet.

## Ce qui peut encore sortir

- **Les téléchargements :** Ollama, Hermes, le modèle et leurs mises à jour.
- **Un modèle dont le nom finit par `cloud`** tourne chez Ollama, pas chez vous. Il n'y en a aucun dans la grille.
- **Les outils de Hermes** qui vont sur le web, ou une messagerie que vous lui branchez. Posez les trois questions avant.

## Si ça coince

{tableau(["Ce que vous voyez", "Ce qu'il faut faire"], d['IA_PANNES'])}
## Tout retirer

La ligne `--dry-run` montre ce qui partira, sans rien effacer. Puis retirez l'application Ollama comme toute application.

{bloc(c['retirer'])}
## Ce qui est vérifié

**Fait, le 12 novembre 2026 :** les étapes 2 à 6 sur un Mac à puce Apple de 16 Go avec qwen3.5:9b ; le script
sur deux Mac, de 16 et 48 Go. **Pas encore essayé :** Windows et Linux complets, les paliers 8, 24 et 32 Go.
"""


def etape3(d) -> str:
    c = d["CONSTRUIRE_CMD"]
    w = "ce mod fonctionne sur Mac et Linux ; sous Windows, prenez Handy."
    return f"""# Étape 3 : construire votre interface

Voir son contexte et ses quotas, dicter, écouter, garder certaines questions chez soi.
Chaque geste en deux versions : avec Claude, puis souverain.

**Avant chaque brique, trois questions :** où vont mes données ? qui les garde ? comment je repars sans lui ?

Les deux mods sont dans `etape-3-construire/mods/` (`ma-jauge`, `ma-dictee`) : lisez leur fichier
`hooks/register.tsx` avant de les charger. Les mods sont en accès anticipé chez Anthropic : leur
fonctionnement peut changer d'une version à l'autre. Les commandes se lancent depuis le dossier du kit.

## Niveau 3, version Claude

### Lire la barre d'état : contexte et quotas
*Ce qui sort : rien.* Elle est installée depuis l'étape 1 : le contexte, le quota de 5 heures et celui de 7 jours.

{bloc(c['legende'])}
Au-delà de 80 % de contexte, tapez `/compact`. **Réussi si** vous savez dire s'il vous reste de quoi finir la tâche.

### Dicter avec /voice
*Ce qui sort : votre voix, envoyée en direct chez Anthropic pour être transcrite. Il faut un compte Claude.ai.*
Dans Claude Code : `/voice`. Tenez la barre d'espace, parlez, relâchez. Langue : `/config`. Sur Linux, il faut SoX.

### Votre premier mod : la jauge
*Ce qui sort : rien.* Lancez Claude avec la jauge, pour cette session :

{bloc(c['essayer'])}
Pour la garder : demandez à Claude « ajoute le dossier de ma-jauge à CLAUDE_CODE_PLUGIN_DIRS dans l'env de mes réglages ».
**Réussi si** une ligne « Contexte ▰▰▱▱… » apparaît au-dessus de l'invite, avec une alerte à 85 %.

### Construire votre propre mod
*Ce qui sort : ce que votre mod lancera. Lisez-le.* Décrivez à Claude ce que vous voulez voir, par exemple
« un mod qui affiche le nom de la branche git et le nombre de fichiers modifiés ». Puis demandez-lui ce que le mod
lance et ce qu'il envoie. **Réussi si** il apparaît et que `claude plugin validate` ne signale rien.

## Niveau 3, version souveraine

### Dicter partout avec Handy
*Ce qui sort : rien, une fois le modèle téléchargé.* Handy (libre, MIT, Mac, Windows, Linux) :
https://github.com/cjpais/Handy/releases/latest . Choisissez un modèle, autorisez le micro (et l'accessibilité sur Mac),
choisissez un raccourci, puis dans Claude Code : tenez-le, parlez, relâchez. Coupez le Wi-Fi pour vérifier.

### Le bouton Dicter dans Claude Code (mod ma-dictee)
*Ce qui sort : rien. L'audio est transcrit par whisper.cpp et effacé aussitôt.*

Mac et Linux seulement. Sous Windows, prenez Handy, juste au-dessus.

1. SoX et whisper.cpp. Linux : SoX par votre gestionnaire de paquets, whisper.cpp depuis https://github.com/ggml-org/whisper.cpp . Mac :

{bloc(c['outilsVoix'], ('mac',))}
2. Le modèle de transcription, 574 Mo, une seule fois :

{bloc(c['modeleVoix'], ('mac', 'linux'), w)}
3. Rangez les deux mods à demeure, puis lancez Claude avec eux :

{bloc(c['ranger'], ('mac', 'linux'), w)}
{bloc(c['dictee'], ('mac', 'linux'))}
4. Cliquez sur **● Dicter** ou tapez `/dicter`, parlez, taisez-vous deux secondes. Relisez avant Entrée.

### Écouter les réponses
*Ce qui sort : rien.* Avec ma-dictee : **▶ Lire** ou `/lire`. Les blocs de code ne sont pas lus.

### Le bouton Local : votre agent de l'étape 2
*Ce qui sort : rien.* Écrivez votre question, puis **⌂ Local** ou `/local` au lieu d'Entrée : elle part à Hermes,
la réponse s'affiche dans un panneau à part, jamais envoyé à Claude. Si vous la recopiez dans l'invite, elle partira
chez Anthropic. Pour contrôler les mods :

{bloc(c['verifier'], ('mac', 'linux'))}
## Ce qui sort, brique par brique

{tableau(["Brique", "Ce qui sort", "La version souveraine"], [(l['brique'], l['sort'], l['souverain']) for l in d['SOUVERAINETE']])}
## Ce qui est vérifié

**Fait, le 12 novembre 2026 :** les deux mods passent la validation et les tests de Claude Code 2.1.322 ; whisper.cpp a
rendu une phrase exacte en 3,4 secondes sur un Mac à puce Apple. **Pas encore essayé :** les boutons cliqués dans une
vraie session, le micro, Linux, Handy sous Windows et Linux.
"""


def boucle_groupe(d) -> str:
    c = d["CONSTRUIRE_CMD"]
    return f"""# À plusieurs, 30 minutes : parler à son ordinateur

Parler à Claude Code au lieu de taper, avec une transcription qui se fait sur votre machine. Deux outils suffisent,
Handy et whisper.cpp. Aucun modèle d'IA à installer chez vous : le cerveau reste Claude.
Seul, à votre rythme : `cd exercices/boucle-voix`, `claude`, puis `/commencer` (le coach est dans son `CLAUDE.md`).

- **Votre voix :** Handy ou whisper.cpp la transcrivent sur votre machine. L'audio ne sort pas.
- **Votre question :** le texte transcrit part chez Anthropic, comme une question tapée.
- **La réponse lue :** la voix de votre système (`say` sur Mac, `espeak-ng` sur Linux). Rien ne sort.

1. **5 min. Comprendre.** Chacun redit ce qui sort de sa machine et ce qui y reste. Lancez les téléchargements tout de suite.
2. **10 min. Voie 1, Handy : dicter dans Claude Code.** https://github.com/cjpais/Handy/releases/latest . Modèle, micro,
   accessibilité sur Mac, un raccourci. Dans Claude Code : tenez-le, parlez, relâchez, relisez, Entrée.
3. **10 min. Voie 2, whisper.cpp : la boucle parlée** (Mac et Linux ; sous Windows, en binôme avec un Mac).
   L'oreille (passez si l'étape 3 est faite). Linux : SoX par le gestionnaire de paquets, whisper.cpp depuis https://github.com/ggml-org/whisper.cpp . Mac :

{bloc(c['outilsVoix'], ('mac',))}
{bloc(c['modeleVoix'], ('mac', 'linux'))}
   Le script est dans le kit, lisez-le d'abord :

```
cd exercices/boucle-voix
chmod +x boucle-voix.sh
```

   Testez sans micro, l'ordinateur pose la question à sa propre oreille :

{bloc(c['boucleTest'], ('mac', 'linux'))}
   Puis parlez : Entrée, votre question, silence (coupure après 1,5 seconde). Ctrl-C pour quitter.

{bloc(c['boucleClaude'], ('mac', 'linux'))}
4. **5 min. Le test du Wi-Fi.** Coupez-le et dictez avec Handy : le texte apparaît, la transcription est locale.
   Claude, lui, ne répond plus : c'est la seule pièce qui sort.
5. **5 min. Tour de table.** Chacun dit quelle voie il garde, et pourquoi.

**Réussi si** vous dictez dans Claude Code Wi-Fi coupé, et, sur Mac ou Linux, si Claude vous répond à voix haute.
"""


SOMMAIRE = """# Le manuel Config OVNI, dans le dépôt

Tout ce que montre la page Config OVNI (à code) est ici, pour que votre Claude Code en sache autant que vous.
Demandez-lui simplement : « lis manuel/ et dis-moi par où commencer ».

| Chapitre de la page | Dans le dépôt |
|---|---|
| 1. Les notions | `manuel/01_notions.md` |
| 2. La méthode | `manuel/02_methode.md`, `tuto/09_methode.md` |
| 3. Installer pas à pas | `manuel/03_installer.md`, `CLAUDE.md` (le pilote) |
| 4. Six tutos | `manuel/04_six-tutos.md` |
| 5. Les exercices | `manuel/05_exercices.md`, `exercices/` |
| 6. Notre bibliothèque | `manuel/06_bibliotheque.md`, `skills/` |
| Le catalogue selon votre métier | `manuel/07_catalogue-par-metier.md` |
| 7. En cas de panne | `manuel/08_pannes.md`, `tuto/11_pannes.md` |
| 8. Les ressources | `README.md`, `tuto/` (18 fiches) |
| 9. La version Codex | `codex/` |
| 10. Étape 2 : votre IA locale | `etape-2-ia-locale/` |
| 11. Étape 3 : construire votre interface | `etape-3-construire/` |
| Le parcours guidé de NOVI | `manuel/09_parcours-novi.md` |

Restent sur la page seulement : les schémas interactifs, la voix de NOVI et le chat réservé aux membres.
Leur contenu est dans les fiches ci-dessus.

Documentation officielle : https://code.claude.com/docs/en/overview
"""


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    site = Path(sys.argv[1]).expanduser().resolve()
    brut = subprocess.run(["node", str(RACINE / "outils" / "exporter_site.mjs"), str(site)],
                          capture_output=True, text=True, check=True).stdout
    d = json.loads(brut)
    commit = subprocess.run(["git", "-C", str(site), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip() or "?"
    pub = site / PUBLIC

    m = RACINE / "manuel"
    for nom, texte in [("01_notions.md", notions(d)), ("02_methode.md", METHODE), ("03_installer.md", installer(d)),
                       ("04_six-tutos.md", TUTOS), ("05_exercices.md", exercices(d)), ("06_bibliotheque.md", bibliotheque(d)),
                       ("07_catalogue-par-metier.md", catalogue(d)), ("08_pannes.md", pannes(d)),
                       ("09_parcours-novi.md", parcours(d)), ("README.md", SOMMAIRE)]:
        ecrire(m / nom, texte, commit)

    e2 = RACINE / "etape-2-ia-locale"
    ecrire(e2 / "LISEZ-MOI.md", etape2(d), commit)
    shutil.copy2(pub / "choisir-modele.py", e2 / "choisir-modele.py")

    e3 = RACINE / "etape-3-construire"
    ecrire(e3 / "LISEZ-MOI.md", etape3(d), commit)
    for zip_nom, cible, racine_zip in [("config-ovni-mods.zip", e3 / "mods", "config-ovni-mods/"),
                                       ("exercice-boucle-voix.zip", RACINE / "exercices" / "boucle-voix", "exercice-boucle-voix/")]:
        shutil.rmtree(cible, ignore_errors=True)
        with zipfile.ZipFile(pub / zip_nom) as z:
            for info in z.infolist():
                rel = info.filename.removeprefix(racine_zip)
                if info.is_dir() or not rel or ".." in Path(rel).parts or rel.startswith("/"):
                    continue  # frontière de confiance : jamais d'écriture hors du dossier cible
                dest = cible / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(z.read(info))
                if rel.endswith(".sh"):
                    dest.chmod(0o755)
    ecrire(RACINE / "exercices" / "boucle-voix-en-groupe.md", boucle_groupe(d), commit)
    print(f"✅ manuel/ (10 fiches, {len(d['CATALOGUE'])} entrées de catalogue), étapes 2 et 3, exercices, depuis le site {commit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
