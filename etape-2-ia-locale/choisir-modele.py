#!/usr/bin/env python3
"""Config OVNI, étape 2 : quel modèle local pour cet ordinateur ?

Lit la mémoire de la machine (et celle d'une carte NVIDIA s'il y en a une),
puis affiche le modèle conseillé et la commande pour le télécharger.
Ne télécharge rien, n'envoie rien, ne modifie rien. Python 3.8 ou plus, sans dépendance.

    python3 choisir-modele.py                 # lit la machine
    python3 choisir-modele.py --memoire 16    # simule 16 Go (sans rien lire)

Licence CC BY-NC 4.0, OVNI Conseil. La même grille est affichée dans le manuel.
"""
import json, platform, shutil, subprocess, sys

# (mémoire minimale en Go, modèle Ollama, taille du téléchargement, note) ; même tableau que PALIERS dans contenu.ts
PALIERS = [
    (0, "qwen3.5:2b", "3 Go", "Pour essayer seulement : trop juste pour un agent fiable."),
    (8, "qwen3.5:4b", "4 Go", "Un petit agent, lent sur les longues tâches."),
    (16, "qwen3.5:9b", "7 Go", "Le bon point de départ pour la plupart des portables."),
    (24, "gpt-oss:20b", "14 Go", "Plus solide sur le raisonnement."),
    (32, "gemma4:26b", "17 Go", "Le modèle de notre serveur de référence."),
    (48, "qwen3.6:35b-a3b", "23 Go", "Le plus capable de la grille, et rapide."),
]
SANS_CARTE_MAX = 8  # sans puce Apple ni carte NVIDIA, le modèle tourne sur le processeur : on reste petit
GO = 1024 ** 3


def palier(memoire_go: float, acceleree: bool = True):
    """Le palier conseillé pour une mémoire donnée (en Go)."""
    plafond = memoire_go if acceleree else min(memoire_go, SANS_CARTE_MAX)
    choisi = PALIERS[0]
    for p in PALIERS:
        # 1 Go de tolérance : un « 16 Go » s'affiche souvent 15,6
        if plafond + 1 >= p[0]:
            choisi = p
    return choisi


def _sortie(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def memoire_vive() -> float:
    s = platform.system()
    if s == "Darwin":
        v = _sortie(["sysctl", "-n", "hw.memsize"])
        return int(v) / GO if v.isdigit() else 0
    if s == "Linux":
        try:
            with open("/proc/meminfo") as f:
                for ligne in f:
                    if ligne.startswith("MemTotal:"):
                        return int(ligne.split()[1]) * 1024 / GO
        except OSError:
            pass
        return 0
    if s == "Windows":
        import ctypes

        class Etat(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                        ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                        ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                        ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
        e = Etat()
        e.dwLength = ctypes.sizeof(Etat)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(e))
        return e.ullTotalPhys / GO
    return 0


def carte_nvidia() -> float:
    """Mémoire de la plus grande carte NVIDIA, en Go (0 si aucune)."""
    if not shutil.which("nvidia-smi"):
        return 0
    v = _sortie(["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"])
    tailles = [int(x) for x in v.split() if x.isdigit()]
    return max(tailles) / 1024 if tailles else 0


def lire_machine():
    s, m = platform.system(), platform.machine().lower()
    ram = memoire_vive()
    if s == "Darwin" and m in ("arm64", "aarch64"):
        return {"systeme": "Mac à puce Apple", "memoire": ram, "acceleree": True, "detail": "mémoire unifiée, partagée avec le modèle"}
    vram = carte_nvidia()
    if vram:
        return {"systeme": s, "memoire": vram, "acceleree": True, "detail": f"carte NVIDIA de {vram:.0f} Go (mémoire vive : {ram:.0f} Go)"}
    nom = "Mac Intel" if s == "Darwin" else s
    return {"systeme": nom, "memoire": ram, "acceleree": False, "detail": "aucune carte NVIDIA vue : le modèle tournera sur le processeur"}


def main(argv):
    if "--memoire" in argv:
        i = argv.index("--memoire")
        try:
            go = float(argv[i + 1].replace(",", "."))
        except (IndexError, ValueError):
            print("Usage : --memoire <nombre de Go>, par exemple --memoire 16")
            return 2
        machine = {"systeme": "simulé", "memoire": go, "acceleree": "--sans-carte" not in argv, "detail": "valeur donnée à la main"}
    else:
        machine = lire_machine()
    p = palier(machine["memoire"], machine["acceleree"])
    if "--json" in argv:
        print(json.dumps({"memoire": round(machine["memoire"], 1), "acceleree": machine["acceleree"], "modele": p[1]}))
        return 0
    libre = shutil.disk_usage(".").free / GO
    print(f"Ordinateur : {machine['systeme']}, {machine['memoire']:.0f} Go ({machine['detail']}).")
    print(f"Modèle conseillé : {p[1]}, téléchargement d'environ {p[2]}.")
    print(f"Pourquoi : {p[3]}")
    if not machine["acceleree"]:
        print("Attention : sans carte graphique reconnue, comptez plusieurs secondes par mot.")
    if libre < 30:
        print(f"Disque : {libre:.0f} Go libres. Vérifiez qu'il en reste assez pour le modèle, avec de la marge.")
    print("\nCommande suivante :")
    print(f"  ollama pull {p[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
