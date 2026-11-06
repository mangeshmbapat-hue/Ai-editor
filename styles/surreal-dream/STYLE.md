# Surreal Dreamscape — Style Prompt

> A painted dream rendered with total conviction: an empty plain under a deep graduated sky, a low sun throwing impossibly long shadows, and ordinary objects that are the wrong size, the wrong softness or in the wrong place, moving slowly and inevitably.
> References (grammar only): the "metaphysical" painted piazzas of the 1910s (empty arcades, raking light, long shadows); 1920s–30s Surrealist oil painting (smooth glazing, deep plains, soft hard objects, floating heavy objects, words that contradict images); mid-century dream sequences in cinema (one wrong thing in a still world). Never restage a known painting or its signature objects (no draped pocket watches, no bowler hat with an apple), and never name works or painters in the film.

## 1. Essence, and what it is not

- **The plain**: a ground running to a low, dead-level horizon; empty space is ≥ 60 % of most frames.
- **The low sun.** One raking light 4–12° above the horizon; every object casts a long, hard-edged shadow, and shadows may disobey their objects.
- **Ordinary things, one rule broken**: a chair the size of a mountain, a soft staircase, a door with no wall. Everything else is rendered with academic conviction.
- **Invisible brushwork.** Smooth glazed oil: no visible strokes, soft gradations, a faint canvas weave and varnish warmth.
- **Time slowed.** Motion is slow, silent and inevitable: drips, sags, drifts, a figure walking very far away.

Not Impasto Oil Painting (no knife planes or raked paint ridges: the surface is smooth glaze), not Low-poly Isometric Island (perspective to a real horizon, smooth shading, no facets), not the crooked painted sets and angst of an Expressionist set, not a psychedelic kaleidoscope (colour is restrained and calm), not a fantasy matte painting (no castles, no lens flares, no epic crowds).

## 2. Materials & rendering

- **three.js world**, real perspective, camera low (eye 0.3–1.6 m) on a 24–35 mm-equivalent lens to stretch the plain.
- **Sun**: one low `DirectionalLight`, 4096² shadow map with the frustum fitted to each shot's objects, small PCF radius: crisp shadows, thin penumbra. A sky-tinted hemisphere fill keeps shadow sides blue.
- **Ground**: a huge plane, sand value-noise albedo (±6 %), faint undulation, fog toward the horizon colour; the horizon stays a sharp line.
- **Sky**: full-screen gradient shader (deep zenith → pale warm horizon band), optional stretched-noise strata; float render, dither before 8 bit.
- **Objects**: `MeshStandardMaterial`, roughness 0.45–0.8, low specular: painted, not plastic; low-strength GTAO from `core/three/post.js`.
- **Soft objects**: a vertex-shader drape: each vertex sags by `softness × m(t) × distanceFromSupport`, clamped onto the support's height field, folding over edges; `m(t)` is closed-form, never a live simulation. Drips are necking SDF capsules.
- **Glaze pass** (screen space: it is the canvas): linen weave at ±2–3 %, sparse craquelure (Voronoi edges, 2–4 % darker), warm varnish in highlights, mild vignette, reduced micro-contrast.
- **Determinism**: every shape, drip and drift is a function of `t` with seeded randomness; nothing integrates over frames.

## 3. Colour logic

- **The sky owns the hue.** One family from zenith to horizon (ultramarine → turquoise → pale lemon, or violet → rose → ochre); the ground echoes it in earth tones.
- **Shadows are cool and deep**: ultramarine-umber, never neutral grey or black.
- **3–4 hues per frame** plus the sky gradient. Value order: horizon band brightest, sky and lit ground middle, shadows darkest.
- **One accent** (a red cloth, an orange, a yellow door) reserved for the key object of the dream; never on two things at once.
- Never neon, never rainbow, never saturated greens.
- Example: `#1d3b6e` zenith, `#5fa3b8` mid sky, `#f2e2a8` horizon, `#c9a46a` sand, `#3a3550` shadow, accent `#c8372d`.

## 4. Type & subtitles

- Words belong to the painting: a quiet classical serif painted onto the canvas surface, under the glaze pass, so craquelure crosses it.
- **Titles**: Cormorant Garamond or Playfair Display italic, 72–140 px, cream on sky or ink on sand; a title can be a painted label that contradicts its object.
- **Subtitles**: Cormorant Garamond 500 italic, 38–46 px, cream `#f5ecd6` with a soft dark halo, centred low, two lines max. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Tiro Devanagari Hindi at the same visual size; same halo.
- Small labels in Cormorant Garamond small caps, 22–26 px.

## 5. Motion quality

- 24 fps on ones; long `eio` and `ss` curves; nothing snaps, nothing bounces.
- **Weight is slow**: drips accelerate (`ei`), drapes settle with one tiny overshoot, floating things bob ≤ 0.5 % of frame height on periods of 6–10 s.
- Appear: walk in from the horizon, rise out of their own shadow, or are simply *there* after a cut. Disappear: shrink toward the vanishing point, sink into the plain, or the shadow leaves first.
- Figures walk far away and small; no close-up acting.
- **Never moves**: the horizon line and the sun's direction, unless the move is about time itself.

## 6. Camera grammar

A slow, low, contemplative camera on a still world. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal tableau, horizon in the lower third | The world is a painting; look closely | an inventory; a still decision; a portrait of one object |
| Slow dolly at ground level toward a distant object | It is bigger than you thought | a looming problem; ambition; a memory that grows |
| Lateral track along a row of arches or repeated objects | Endless sameness | routine; bureaucracy; a waiting line |
| Crane up from an object until the plain becomes a tabletop or a page | Scale is a lie | a model world; a child's imagination; a plan |
| Dolly-zoom on one object | Space itself bending | panic; a sudden realisation; vertigo of choice |
| Follow a long shadow to its owner | Cause found late | a consequence; a secret; a footprint of the past |
| Push into a door, window or opening | Passing into another logic | a new chapter; a different time; a dream within a dream |

Framing: horizon level and low; one hero per tableau; a tiny figure for scale. Transitions: through a free-standing door, match-shape, shadow wipe (a long shadow crosses and the world changes behind it), slow dissolve between two skies; no whip pans, glitches or flash cuts.

## 7. Sound palette

- **Sparse and suspended**: bowed vibraphone, glass, harp harmonics, low clarinet, soft glockenspiel, very quiet violin tremolo, soft organ drones; a reversed piano note marks dream logic.
- **Foley from the plain**: wind (band-passed noise, slow gusts), sand footsteps, a single drip with long pre-delayed reverb, the creak of something soft stretching (filtered noise bending down), a distant synthesised bell.
- **Ambience**: wide, quiet, enormous reverb with long pre-delay so near sounds feel far away.
- **Silence**: windless; one sound inside it at most.
- **Voice**: close, dry, intimate, a dream spoken aloud. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Impossible scale.** An everyday object stands on the horizon at mountain size; a tiny walker passes its foot (true perspective, matching fog). *Fits content like:* a rent bill over a family; a notification over a city; a teacher remembered as a giant.
- **The soft object.** Something rigid droops and drapes over an edge. Closed-form drape shader driven by one progress value. *Fits content like:* a deadline losing shape; a rule bending; a building plan collapsing.
- **The disobedient shadow.** A shadow shows another object, time or person, cast by a hidden proxy mesh. *Fits content like:* a child's shadow as an adult; a factory throwing a forest's shadow; a promise and its broken version.
- **Sky inside.** An object's opening shows the sky, the sea or another place (stencil portal or render target). *Fits content like:* a suitcase holding home; a head full of weather; a window that opens onto noon at midnight.
- **The free-standing door.** A frame alone on the plain; through it, a different hour or landscape. *Fits content like:* a migration; a career change; a first day.
- **Endless repetition.** One object instanced to the horizon in perfect rows. *Fits content like:* identical days; a population; a backlog.

## 9. Pitfalls of the medium

- **Random weirdness reads as clip-art collage** → one broken rule per image, ≥ 60 % empty plain and sky, everything else ordinary and fully rendered.
- **CG plastic look** → painted roughness, low specular, glaze pass, softened micro-contrast, cool deep shadows.
- **Noise-based melting looks like a glitch** → gravity drape on a support with folds and necking drips.
- **Sky banding** → float render targets plus blue-noise dither.
- **Low-sun shadows alias and swim** → fit the shadow frustum per shot, tune normal bias.
- **Quoting famous paintings** → invent objects; borrow only grammar (light, emptiness, scale).
- **Camera roll and fast moves break the trance** → keep the horizon level unless tilting it is the point.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `plain.js`: ground plane, sky gradient shader, low sun, fog, `fitShadow(camera, objects)`.
- `soft.js`: `drape(mesh, support, m, softness)` vertex shader, `drip(path, t)` SDF capsules.
- `portal.js`: stencil "sky inside" and door portals via a second camera's render target.
- `glaze.js`: weave, craquelure, varnish, dither, after `core/three/post.js`.
- `shadowproxy.js`: hidden shadow-only meshes.

Start from `core/three/post.js`, `core/lib.js`, `styles/glass-product/demo/studio.js` (one-light staging), `styles/lowpoly-island/demo/post.js` (sky blend by depth). Sound from `core/audio/sampler.py` (vibraphone_bowed, glass, harp, clarinet, organ_soft) and `core/audio/sfx.py`.

## 11. Variation space

The agent decides the objects, the rule each image breaks, the sky family, the accent, whether a figure appears, the pacing and the camera path.

- Structures: **an inventory** (one object per tableau, each wrong differently); **a walk toward a horizon** that never gets closer; **a day compressed** (the sun moves, shadows swing round).
- Openings: **a horizon drawn by light** on black; **a close-up of an ordinary thing**, pulled back to mountain size on the plain; **a dark room** whose window opens onto the plain.
- Endings: **the shadow walks away** and its object stays; **the plain is lifted** like a canvas off its stretcher; **the sun sets** and every shadow points back at the viewer.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
