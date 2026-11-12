// Exporte en JSON les données du manuel Config OVNI (site ovniconseil.fr), pour outils/depuis_le_site.py.
// Usage : node outils/exporter_site.mjs <dépôt du site>   (le dépôt du site doit avoir ses node_modules)
import { createRequire } from "node:module";
import path from "node:path";

const site = path.resolve(process.argv[2]);
const jitiPkg = createRequire(path.join(site, "package.json"))("jiti");
const charger = (jitiPkg.createJiti ?? jitiPkg)(path.join(site, "package.json"));
const req = typeof charger === "function" ? charger : (f) => charger(f);
const d = path.join(site, "app/l/config-ovni-k7m2xq9tfd");
const c = req(path.join(d, "contenu.ts"));
const cat = req(path.join(d, "catalogue-donnees.ts"));
const p = req(path.join(d, "programme.ts"));
const S = ["mac", "windows", "linux"];
const cmds = (table, f) => Object.fromEntries(Object.keys(table).map((k) => [k, Object.fromEntries(S.map((s) => [s, f(k, s)]))]));
const CLES = ["GROUPES", "BRIQUES", "FICHIERS_CASCADE", "EVENEMENTS", "SCENARIOS", "QUESTIONS", "SITUATIONS", "STATIONS",
  "CHAINE", "SKILLS", "PANNES", "FICHES", "EXERCICES", "PALIERS", "IA_PANNES", "SOUVERAINETE", "AGENT", "CONTEXTE"];
console.log(JSON.stringify({
  ...Object.fromEntries(CLES.map((k) => [k, c[k]])),
  IA_CMD: cmds(c.IA, (k, s) => c.cmdIA(k, s)),
  CONSTRUIRE_CMD: cmds(c.CONSTRUIRE, (k, s) => c.cmdConstruire(k, s)),
  METIERS: cat.METIERS, CATALOGUE: cat.CATALOGUE, DATE_RELECTURE: cat.DATE_RELECTURE,
  PROGRAMME: p.PROGRAMME,
}, null, 1));
