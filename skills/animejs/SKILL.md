---
name: animejs
description: Use quand il faut écrire, corriger ou relire du code d'animation avec anime.js (v4, animejs.com) — pages HTML/JS pur (sites vitrines, artefacts, pages de présentation), tracé ou morphing SVG, animation au scroll, texte découpé lettre par lettre, glisser-lâcher à ressort, timelines. Déclenché par "anime.js", "animejs", "anime ça avec anime", "fais tracer ce SVG", "anime au scroll", "morph de forme". Empêche la syntaxe v3 (anime({targets})) et impose prefers-reduced-motion. PAS pour un site React déjà équipé de framer-motion.
---

# anime.js v4 — animer le web sans syntaxe fantôme

Vérifié sur le paquet npm **animejs 4.5.0** (MIT, 26/09/2026) : exports, types
`.d.ts` et valeurs par défaut lus dans le code, pas dans la mémoire du modèle.

## Quand l'utiliser (et quand non)

| Contexte | Choix |
|---|---|
| Page HTML/JS pur, artefact, page de présentation | **anime.js** |
| Tracé SVG, morphing, objet qui suit un chemin | **anime.js** (`svg`) |
| Texte animé lettre/mot/ligne, effet « scramble » | **anime.js** (`splitText`, `scrambleText`) |
| Site React déjà équipé de framer-motion | **framer-motion** — ne pas ajouter une 2ᵉ lib |
| Simple fondu/hover | **CSS** `transition` — aucune lib |

Pour le *pourquoi* du mouvement (durées, courbes, retenue) : skills
`design-motion-principles` et `apple-design`. Ce skill-ci couvre le *comment*.

## Piège n° 1 : la syntaxe v3 est morte

Le modèle a surtout vu la v3. **Tout ce qui commence par `anime(` ou `anime.` est faux en v4.**

| v3 (NE PLUS ÉCRIRE) | v4 |
|---|---|
| `anime({ targets: '.a', translateX: 250 })` | `animate('.a', { x: 250 })` |
| `easing: 'easeInOutQuad'` | `ease: 'inOutQuad'` |
| `easing: 'spring(1, 80, 10, 0)'` | `ease: createSpring({ stiffness: 80, damping: 10 })` |
| `direction: 'alternate'` | `alternate: true` |
| `direction: 'reverse'` | `reversed: true` |
| `endDelay: 500` | `loopDelay: 500` (entre boucles) |
| `begin / update / complete` | `onBegin / onUpdate / onComplete` |
| `loopBegin / loopComplete` | `onLoop` |
| `anime.timeline({...})` | `createTimeline({...})` |
| `tl.add({ targets, ... }, '-=200')` | `tl.add('.a', {...}, '-=200')` |
| `anime.stagger(100)` | `stagger(100)` |
| `anime.set / anime.random` | `utils.set / utils.random` (ou `set`, `random` importés) |
| `anime.path('path')` | `...svg.createMotionPath('path')` |
| `anime.setDashoffset` + `strokeDashoffset` | `animate(svg.createDrawable('path'), { draw: '0 1' })` |
| `anime.remove('.a')` | `utils.remove('.a')` |
| `.finished.then()` | `.then()` directement sur l'animation |
| `value: 100` dans un objet propriété | `to: 100` (et `from`, `fromTo`) |

Défauts réels v4 : `duration: 1000`, `ease: 'out(2)'`, `autoplay: true`, `loop: 0`.

## Installer — souverain d'abord

- **Projet avec bundler** : `npm i animejs`, puis imports nommés
  (seul ce qui sert part dans le bundle).
- **HTML pur en production (sans bundler)** : copier
  `node_modules/animejs/dist/bundles/anime.esm.min.js`
  dans le projet et l'importer en local. Pas de CDN en prod : aucune requête vers un tiers.
- **Prototype / artefact jetable** : CDN toléré
  `import { animate } from 'https://cdn.jsdelivr.net/npm/animejs@4.5.0/+esm';`
- Épingler la version (`@4.5.0`), jamais `@latest`.

```js
import { animate, createTimeline, createScope, createDraggable, createAnimatable,
  createSpring, stagger, onScroll, splitText, scrambleText, svg, utils, engine } from 'animejs';
// sous-modules pour alléger : 'animejs/animation', 'animejs/svg', 'animejs/text'…
```

## Accessibilité — NON NÉGOCIABLE

anime.js **ne lit pas** `prefers-reduced-motion` (0 occurrence dans son code).
Toute page produite avec ce skill l'impose elle-même :

```js
const calme = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (calme) engine.defaults.duration = 0;  // états finaux immédiats, pas de disparition
```

Mieux, par média-requête vivante avec `createScope` :

```js
createScope({ mediaQueries: { calme: '(prefers-reduced-motion: reduce)' } })
  .add(({ matches }) => {
    if (matches.calme) { utils.set('.carte', { opacity: 1, y: 0 }); return; }
    animate('.carte', { opacity: [0, 1], y: [20, 0], delay: stagger(60) });
  });
```

Règles : jamais de contenu qui n'existe qu'après une animation (texte lisible sans JS) ;
pas de clignotement > 3 fois/s ; boucles infinies décoratives stoppables ;
`splitText` garde `accessible: true` (défaut) pour que le lecteur d'écran lise la phrase entière.

## Recettes vérifiées

**Entrée en cascade**
```js
animate('.item', { opacity: [0, 1], y: [16, 0], delay: stagger(50), ease: 'out(3)', duration: 600 });
```

**Grille qui ondule depuis le centre**
```js
animate('.dot', { scale: [1, 1.4, 1], delay: stagger(40, { grid: [13, 13], from: 'center' }) });
```

**Timeline**
```js
createTimeline({ defaults: { duration: 500, ease: 'out(3)' } })
  .add('.titre', { opacity: [0, 1] })
  .add('.sous-titre', { y: [10, 0], opacity: [0, 1] }, '-=250')   // chevauche
  .add('.bouton', { scale: [0.9, 1] }, '<<');                     // même départ que le précédent
```
Positions : `500`, `'+=100'`, `'-=100'`, `'*=.5'`, `'<'` (fin du précédent),
`'<<'` (début du précédent), `'<<+=250'`, un label, ou `stagger(…)`.

**Tracer un SVG, suivre un chemin, morpher**
```js
animate(svg.createDrawable('.trait'), { draw: ['0 0', '0 1'], duration: 1500 });
animate('.bille', { ...svg.createMotionPath('.circuit'), duration: 4000, loop: true });
animate('.forme-a', { d: svg.morphTo('.forme-b') });
```

**Au scroll**
```js
animate('.bloc', {
  opacity: [0, 1], y: [40, 0],
  autoplay: onScroll({ enter: 'end start', leave: 'start end', sync: true }),
});
```
Seuil en chaîne = **« conteneur cible »** : `'end start'` = le bas du conteneur touche
le haut de l'élément (valeurs par défaut). Aussi `{ container: 'end', target: 'start' }`.
`sync: true` lie la progression au défilement ; sans `sync`, l'animation
se déclenche à l'entrée.
Callbacks : `onEnter`, `onLeave`, `onEnterForward`, `onLeaveBackward`…
`debug: true` montre les seuils.

**Texte**
```js
const { chars } = splitText('.titre', { chars: true });   // aussi words, lines
animate(chars, { opacity: [0, 1], y: ['100%', '0%'], delay: stagger(20) });
animate('.code', { innerHTML: scrambleText({ text: 'HELLO', chars: 'uppercase', cursor: true }) });
```

**Glisser avec ressort**
```js
createDraggable('.pastille', {
  container: '.zone',
  releaseEase: createSpring({ stiffness: 120, damping: 6 }),
});
```
Ressort : `mass` (1), `stiffness` (100), `damping` (10), `velocity` (0), `bounce`,
`duration` perçue.

**Suivi fluide (curseur, capteur)** — pas une animation par événement :
```js
const suiveur = createAnimatable('.oeil', { x: 400, y: 400, ease: 'out(3)' });
addEventListener('pointermove', e => { suiveur.x(e.clientX); suiveur.y(e.clientY); });
```

**Contrôle** : chaque `animate`/`createTimeline` renvoie un objet avec
`play() pause() restart() reverse() seek(ms) cancel() revert()` et `then()`.

## Nettoyage (fuites = page qui rame)

- Dans une SPA ou un composant : tout mettre dans `createScope({ root })` et appeler
  `scope.revert()` au démontage (React : dans le `return` du `useEffect`, `root: useRef()`).
- `splitText(...).revert()` rend le texte d'origine.
- Animation hors écran en boucle : la mettre en pause (`onScroll` ou `IntersectionObserver`).

## Perf

- Animer `x`, `y`, `scale`, `rotate`, `opacity` (composités). Éviter `width`, `top`, `left`.
- `composition: 'blend'` pour empiler deux animations sur la même propriété sans saut.
- Beaucoup d'éléments simples : `waapi.animate(...)` (moteur natif du navigateur, même API).
- `createLayout` / `AutoLayout` pour animer un changement de mise en page (FLIP).

## Vérifier avant de dire fini

1. Ouvrir la vraie page au navigateur, regarder l'animation jouer (pas seulement « ça compile »).
2. Console sans erreur (`anime is not defined` = syntaxe v3 restée).
3. Activer « Réduire les animations » (Réglages macOS › Accessibilité › Affichage)
   et recharger : tout le contenu doit être visible, immobile.
4. `grep -nE "anime\(|anime\.|easing:|targets:" <fichiers>` doit ne rien renvoyer.

## Sources

Doc : https://animejs.com/documentation · Types : `node_modules/animejs/dist/modules/types/index.d.ts`
(référence quand un doute subsiste — la lire plutôt que deviner).
