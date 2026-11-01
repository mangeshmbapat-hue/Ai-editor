# Mehndi — Style Prompt

> Henna drawing brought to life: a cone squeezes a fine raised line of dark paste over a palm; lines grow into paisleys, vines, lattices and medallions, then dry, crack and flake away, leaving an orange stain that deepens to red-brown.
> References (grammar only): South Asian bridal and festival mehndi (Rajasthan, Gujarat, Punjab and across the subcontinent) for dense full coverage, fingertip caps, paisley (keri), peacocks, lotus and netting (jaal); Gulf-style henna for bold diagonal trails with open skin; North African henna for geometric bands. Never copy a particular artist's design, and never name them in the film.

## 1. Essence, and what it is not

- **The body is the canvas**: a palm, the back of a hand, a foot or a forearm, close, with creases, pores and fingerprint ridges.
- **One raised line of paste**: a cone-fed tube of dark olive-brown paste, glossy while wet, round in section, casting a small shadow on the skin, with a slightly heavier bead where the cone touched down or lifted.
- **A hierarchy of shapes**: a central medallion or lotus, framing paisleys and vines, fields of netting, dots and scallops; fingertips capped solid; bands at the knuckles and wrist.
- **Two lives of one image**: wet paste (dark, raised, glossy) → dry (matte, cracked) → stain (flat orange deepening to red-brown).
- **Bare skin is part of the drawing**: the gaps between lines are designed.

Not One-line (many lines, raised paste, a body as support, a dense ornamental hierarchy), not Engraving (no tonal hatching, no copper; lines are ornament, not shading), not a tattoo (nothing under the skin, no black, no realism), not a mandala generator laid flat on a photo.

## 2. Materials & rendering

- **Hand**: a 2D hand plate (albedo, normal map, procedural creases, fingerprint ridges from a sine of a flow-aligned distance field) or a three.js hand mesh with wrap lighting and a warm, red-shifted shadow edge. Skin tone is a deliberate parameter across the full real range.
- **Pattern space**: motifs are authored in a palm-space mapping (centre, finger axes, wrist) and warped onto the hand, so lines follow its curvature and bend with the fingers.
- **Motif generators**: `paisley(axis, size, curl)` with echo lines and a filled core; `medallion(rings, petals)`; `jaal(diamond | hex | scale)`; `vine(path, leafRate)`; dot rows; scallops; fingertip caps.
- **The paste line** is a tube: a shadow pass (offset away from the light, 2–3 px blur, multiply ~35 %) → body (1.2–3 px at 1080p for fine work, 4–6 px for bold trails) → a thin specular line along the top (40–60 % white, broken where the tube flattens) → start and end beads. Width follows squeeze speed: slower is thicker (w ∝ 1/√speed, clamped).
- **Solid areas** (caps, filled cores) are raised flat paste with a few specular streaks.
- **Curing**: each line gets a dryness clock from its draw time; dry paste loses its highlight and lightens, then cracks along seeded Voronoi cells inside the line mask, then flakes (cells fall as small tumbling particles), revealing the stain.
- **Stain**: the same mask, multiplied into the skin; a ramp from pale orange through orange to red-brown over compressed hours; darker where paste was thick, on palms and fingertips; a 0.5 px bleed.
- Patterns are built once at init; everything else is a pure function of `t`.

## 3. Colour logic

- **Only henna on the skin**: olive-brown wet paste, orange-to-maroon stain. No rainbow colours, no glitter, never black.
- **Skin is the neutral and the light**: choose the tone deliberately and keep it; stain contrast changes with skin tone, so test each.
- **The occasion's colours** (bridal red, marigold, green silks, gold jewellery) live in the soft background, a step less saturated than life, so the line reads.
- **Value order**: paste darkest → skin → highlights, which belong to wet paste only.
- Example: paste `#3a2d1a`, highlight `#f0e6d0`; stain ramp `#e08a3c` → `#b5532a` → `#6b2a1a`; skin `#c68e64` or `#8d5a3b`; background silk `#8e1b2b`, marigold `#f2a20c`.

## 4. Type & subtitles

- **Titles are drawn in paste**: letter centrelines from Kalam or Caveat skeletons (Kalam also covers Devanagari) rendered as henna tubes, or revealed later as stain.
- **Subtitles never sit on the skin**: lower third over the soft background, Cormorant Garamond Italic or Kalam 34–40 px in warm ivory with a soft dark halo; Hindi in Kalam or Tiro Devanagari Hindi; Urdu in Noto Nastaliq Urdu, only for text checked by a reader.
- **A hidden name** worked into the pattern is a native device; use invented names only.
- Hold ≥ max(1.8 s, speech + 0.6 s); two lines max.

## 5. Motion quality

- **24 fps on ones** for the cone: steady on long vines, quick flicks for leaf strokes, a stop for each dot; the line appears exactly at the tip, never ahead of it.
- **The hand is held**: a breathing drift ≤ 2 px, slow turns to present another face; fingers may flex, and the lines bend with them.
- **Cure in time-lapse**: drying, cracking and flaking compress into seconds; flakes fall with gravity and tumble.
- **The stain deepens** as a slow ramp, cued by a clock, a change of light or a change of place.
- Never moving: the pattern relative to the skin. Lines never wobble or boil.

## 6. Camera grammar

A macro camera close to a hand that is being worked on. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Macro following the cone tip | concentration, craft | a skill; patience; a delicate negotiation |
| Locked top-down on the palm | the whole pattern as a plan | a map; a family; a schedule |
| Slow turn of the hand | another side | a secret; a second meaning; layers |
| Rack focus from line to background | the person behind | a guest; a memory; a crowd |
| Pull back to two hands side by side | pairing | a partnership; two families; a comparison |
| Locked time-lapse as paste dries | waiting | anticipation; healing; ageing |
| Follow a vine up the forearm | a journey | a lineage; a road; growth |

Framing: the hand fills 60–90 % of the frame; the central motif on a third; creases and finger gaps visible; never crop fingertips during a reveal. Transitions: flakes brushed away reveal the next scene in stain; the hand turns over; a new hand slides in; a match cut on a motif shape. Forbidden: dissolves through skin, morphing hands.

## 7. Sound palette

- **The gathering**: dholak played by hand with a spoon tapped on its shell (dholak recipe: a bass head with upward glide, a sharp treble slap, plus a metallic click from `claves` and a `glass` ping), `claps`, harmonium (`accordion`), a sitar recipe line. Don't fake group singing with synthesis.
- **Close foley**: the cone squeeze (a soft wet squelch: low-passed noise with a short pitch drop), a dot's "pip", a faint drying crackle, flakes brushed off (dry rustle), glass bangles (`glass`, `hand_chimes`), silk rustle, a cotton dab of lemon-sugar on drying paste.
- **Ambience**: room tone with festivities in the next room.
- **Silence**: the artist's breath and the cone alone.
- **Voice**: intimate, close-miked; music ducked ~10 dB under voice; −14 LUFS.

## 8. Native moves

- **The line finds the shape.** One continuous line grows into a paisley, then its echo lines. *Fits content like:* a plan taking form; a signature; a design process.
- **Netting spreads.** A lattice fills a region cell by cell. *Fits content like:* a network growing; a crowd forming; a city grid.
- **The hidden name.** A word appears inside the ornament only when you look for it. *Fits content like:* a puzzle; a clue; a message to someone loved.
- **Wet, dry, stain.** The same drawing changes material over time. *Fits content like:* a promise kept; a memory deepening; healing.
- **Fingertip caps.** Five tips fill on five beats. *Fits content like:* a five-step checklist; five friends; a countdown.
- **Two hands meet.** The pattern continues across both palms only when they join. *Fits content like:* a partnership; a trade agreement; a reunion.

## 9. Pitfalls of the medium

- Flat vector strokes → tube shadow and highlight, speed-driven width, beads at the ends.
- Sticker look → palm-space warp; creases nudge lines; fingers bend them.
- Machine symmetry → add hand irregularity (±1.5 % spacing, a slight tremor) after construction.
- Wrong colours → henna palette only; never present black "henna" as normal: it contains PPD and injures skin.
- Default skin → choose the tone on purpose, test stain contrast, never lighten skin.
- Hand anatomy errors → a constrained rig; check contact sheets for finger count and joint bends.
- **Ritual and identity**: mehndi marks weddings and religious festivals across many communities. Don't scatter religious symbols or deity figures as ornament, don't present the film as real henna work, credit henna artists, and consult or commission them for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `hand.js`: hand plate or mesh (albedo, normal, creases, ridges); `toHand(u, v)` palm-space mapping; finger flex.
- `motifs.js`: `paisley`, `medallion`, `jaal`, `vine`, `dots`, `scallop`, `cap`.
- `paste.js`: `drawPaste(path, p, widthFn, light)`, beads, solid fills.
- `cure.js`: dryness clock, crack cells, flake particles, `stain(t)` ramp.
- `cone.js` (cone sprite or mesh, squeeze), `mix.py`.

Start from: `styles/one-line/demo/ink.js` (`prepare`, `drawLine`: a line drawn to a progress) and `styles/one-line/demo/geom.js` (`buildPath`, `posAt`, `headAt`); `styles/engraving/demo/engine/burin.js` (`offsetRing`, `contourHatch`, `resample`, `inPoly`) for echo lines and lattice fills; `styles/stained-glass/demo/glass.js` (`voronoi`) for crack cells; `styles/paper-popup/demo/cutmesh.js` (`particles`) for flakes; `core/three/post.js` (DOF for macro); `core/audio/sfx.py`, `core/audio/sampler.py`.

## 11. Variation space

You decide the subject, the style family (dense, open-trail or geometric), whose hands, the skin tone, how far time runs, the opening, the ending and the camera.

- Structures: **a family on two hands** (each motif a generation); **one evening, many guests** (different hands, each pattern a personality); **the lesson** (an artist's method step by step: centre, frame, fill, caps).
- Openings: **a cone twisted shut**; **an empty palm** lit by a lamp; **an old stain fading**, then the new line begins.
- Endings: **flakes brushed away** to reveal the stain; **two hands placed side by side**; **a week later**, the stain faint.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
