#!/usr/bin/env python3
"""Test sans framework : python3 outils/test_depuis_le_site.py <dépôt du site ovniconseil>

Vérifie que le dépôt contient bien tout ce que la page montre : chaque commande, chaque
entrée du catalogue, chaque panne, et des fichiers identiques à ceux servis par le site.
"""
import json
import subprocess
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import depuis_le_site as g  # noqa: E402

site = Path(sys.argv[1]).expanduser().resolve()
R = g.RACINE
d = json.loads(subprocess.run(["node", str(R / "outils" / "exporter_site.mjs"), str(site)],
                              capture_output=True, text=True, check=True).stdout)
subprocess.run([sys.executable, str(R / "outils" / "depuis_le_site.py"), str(site)], check=True, capture_output=True)

fiches = "\n".join(p.read_text(encoding="utf-8") for p in
                   [*R.glob("manuel/*.md"), *R.glob("etape-*/LISEZ-MOI.md"), R / "exercices" / "boucle-voix-en-groupe.md"])

# 1. Chaque commande de la page (étapes 2 et 3, boucle vocale) est dans une fiche, au chemin du dépôt.
absentes = []
for table in ("IA_CMD", "CONSTRUIRE_CMD"):
    for cle, par_systeme in d[table].items():
        if cle in ("boucleRecuperer", "voix"):  # remplacée par le script du dépôt ; /voice est cité dans le texte
            continue
        for s, c in par_systeme.items():
            for ligne in g.chemins(c).splitlines():
                if ligne and ligne not in fiches:
                    absentes.append(f"{table}.{cle}.{s} : {ligne}")
assert not absentes, "commandes absentes :\n" + "\n".join(absentes)
assert "Downloads/config-ovni-mods" not in fiches and "Downloads\\config-ovni-mods" not in fiches

# 2. Catalogue, pannes, exercices, parcours : tout y est.
cat = (R / "manuel" / "07_catalogue-par-metier.md").read_text(encoding="utf-8")
assert cat.count("\n### ") == len(d["CATALOGUE"]) == 83, cat.count("\n### ")
for e in d["CATALOGUE"]:
    assert e["install"] in cat and e["retrait"] in cat, e["nom"]
    for v in e.get("vigilance") or []:
        assert v in cat, (e["nom"], v)
for a, b in d["PANNES"] + d["IA_PANNES"]:
    assert a.replace("|", "\\|") in fiches and b.replace("|", "\\|") in fiches, a
for e in d["EXERCICES"]:
    assert e["texte"] in fiches, e["nom"]
parcours = (R / "manuel" / "09_parcours-novi.md").read_text(encoding="utf-8")
for ch in d["PROGRAMME"]:
    for t in ch["temps"]:
        assert not t.get("texte") or t["texte"] in parcours, t["id"]

# 3. Les fichiers copiés sont ceux du site, octet pour octet.
pub = site / g.PUBLIC
assert (R / "etape-2-ia-locale" / "choisir-modele.py").read_bytes() == (pub / "choisir-modele.py").read_bytes()
for nom, cible, racine in [("config-ovni-mods.zip", R / "etape-3-construire" / "mods", "config-ovni-mods/"),
                           ("exercice-boucle-voix.zip", R / "exercices" / "boucle-voix", "exercice-boucle-voix/")]:
    with zipfile.ZipFile(pub / nom) as z:
        for i in z.infolist():
            if not i.is_dir():
                assert (cible / i.filename.removeprefix(racine)).read_bytes() == z.read(i), i.filename
assert (R / "exercices" / "boucle-voix" / "boucle-voix.sh").read_bytes() == (pub / "boucle-voix.sh").read_bytes()

# 4. Relancer ne change rien.
avant = subprocess.run(["git", "-C", str(R), "status", "--porcelain"], capture_output=True, text=True).stdout
subprocess.run([sys.executable, str(R / "outils" / "depuis_le_site.py"), str(site)], check=True, capture_output=True)
assert avant == subprocess.run(["git", "-C", str(R), "status", "--porcelain"], capture_output=True, text=True).stdout
print(f"✅ test_depuis_le_site : toutes les commandes, {len(d['CATALOGUE'])} fiches de catalogue, "
      f"{len(d['PANNES']) + len(d['IA_PANNES'])} pannes, parcours complet, fichiers identiques au site")
