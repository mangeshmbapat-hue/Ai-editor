# Y2K Chrome — Style Prompt

> Millennium futurism in liquid metal: mercury blobs that merge and split, inflated bubble lettering, iridescent and candy-translucent plastics, sparkle glints and lens flares on silver or electric-blue grounds.
> References (grammar only): late-1990s and early-2000s club-flyer, CD-cover and magazine design (chrome type, starbursts, silver gradients); early 3D metaball and environment-mapping experiments; the translucent candy-coloured consumer plastics of 1998–2002 as a material, not a product. Never copy a real gadget silhouette, brand, logo or cover, and never name them in the film.

## 1. Essence, and what it is not

- **Liquid chrome**: smooth metaball forms with mirror reflections of a high-contrast studio (black and white bands, a horizon), merging, splitting, dripping.
- **Inflated type**: puffy, pillow-extruded letters in chrome or candy plastic.
- **Iridescence**: thin-film hue sweeps (pink → cyan → lime) across holographic surfaces.
- **Candy translucency**: tangerine, grape, lime or aqua plastic with frosted interiors and visible inner parts.
- **Sparkle**: 4-point star glints on specular hot spots, starbursts, restrained lens flares; silver-white or electric-blue backgrounds.

Not Glass Product Render (sober black studio and one realistic product; here excess, play and chrome type), not a liquid-glass interface (refraction of content; here reflection of metal), not Frutiger Aero (water, grass, sky), not Synthwave (night neon and grids), not Vaporwave (pastel, slowed, ironic).

## 2. Materials & rendering

- **Environment first**: chrome is only as good as what it reflects. Bake a procedural studio into an equirect texture (black ground, white sky gradient, 3–6 bright softbox strips, a sharp horizon, one coloured gel strip), PMREM it, and keep it consistent within a scene.
- **Chrome**: `MeshStandardMaterial` metalness 1, roughness 0.02–0.1, tinted silver; or a raymarched SDF shaded with the same env map.
- **Metaballs**: SDF spheres and capsules combined with smooth-min (`smin`, k = 0.1–0.4 of radius); raymarched in a full-screen shader, normals from the SDF gradient. (three.js `MarchingCubes` at ≥ 64³ is a fallback; low resolutions facet.)
- **Inflated type**: glyph → 2D signed distance field → height `h = r·sqrt(1 − (1 − d/r)²)` inside the stroke → displaced grid mesh or raymarched height field; inflate radius ≤ 25 % of stroke width so counters stay open.
- **Iridescent plastic**: `MeshPhysicalMaterial` with `iridescence: 1`, a narrow `iridescenceThicknessRange` so only 2–3 hues sweep.
- **Candy plastic**: `transmission` 0.9, `thickness`, `attenuationColor`, roughness 0.15–0.3, inner parts visible.
- **Background**: silver gradient with a faint grid, or electric blue fading to black; floor optionally mirror.
- **Sparkles**: additive 4-point stars placed at known specular points (computed from the light, normal and view, never random), living 6–10 frames.
- **Post** (`core/three/post.js`): bloom on speculars, slight chromatic aberration at the edges, optional wide-angle barrel distortion. Everything a function of `t`.

## 3. Colour logic

- **Silver and white are the neutral**; chrome takes its colour from the environment, so colour the env strips, not the metal.
- **One or two candy hues per scene** (tangerine, grape, lime, aqua, bubblegum).
- **Iridescence is the accent**, reserved for the hero object or the title.
- Backgrounds: silver-white high key, or electric blue to black low key; pick one per sequence.
- Never matte earth tones; everything has sheen. Shadows are cool blue-grey.
- Example: silver `#d9dde3`, steel `#7d8794`, electric blue `#1032ff`, candy `#ff7a00` and `#9b30ff`, iridescent range pink `#ff6ad5` → cyan `#5ce1ff` → lime `#b8ff3c`.

## 4. Type & subtitles

- **Titles**: inflated or chrome-bevelled Rubik Mono One, Bungee or Righteous, 120–240 px; techno labels in Orbitron, Michroma or Audiowide.
- **Micro labels**: Press Start 2P at 14–18 px or VT323 at 22–28 px (stickers, version numbers, "file" names).
- **Subtitles**: Space Grotesk 600 or Inter 600, 36–44 px, white with a thin dark outline, on a silver pill with a chrome edge when the background is busy. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Baloo 2 700 (rounded, inflates well) for titles; Noto Sans Devanagari 600 for subtitles.
- Inflated words must pass a readability check at thumbnail size.

## 5. Motion quality

- 24 fps on ones; springy and liquid: `spring` and `back` easing, damped jiggle on arrival (amplitude 3–6 %, decay ~0.4 s).
- **Merge and split**: smin blending animates blob radii and positions; necks thin before a split, bulge before a merge.
- Appear: inflate from flat (scale z from 0 with overshoot), condense from a mercury pool, drip upward into shape. Disappear: melt into a puddle, deflate, or pop into chrome droplets.
- Turntables rotate at 10–25°/s; glints flash on the beat.
- **Never moves**: the environment's light strips within a shot (moving them changes every reflection; move them only as a deliberate light sweep).

## 6. Camera grammar

A playful product-shoot camera with a taste for wide lenses. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Turntable orbit around the hero | Showing off | a new product; a trophy; a character |
| Macro slide across a chrome surface | Luxury, sensation | a material; a texture; a close detail |
| Fisheye close-up (barrel distortion) | Cheek, curiosity | a selfie moment; a greeting; a joke |
| Crash zoom with a glint | Emphasis | a price; a name; a reveal |
| Top-down on a mercury pool | Creation from nothing | manufacturing; an idea forming; a recipe |
| Float through a cloud of orbs | Excess, celebration | a party; a sale; a release day |
| Low hero angle on inflated type | Pride, a headline | a title; a slogan; a winner |

Framing: hero centred, big; a clear silhouette against the background; reflections planned. Transitions: a chrome sheet flows across the frame, a white sparkle flash, a blob morphs into the next shape, a spin wipe; no plain dissolves.

## 7. Sound palette

- **Turn-of-the-millennium electronic**: FM bells, supersaw pads (detuned saws), sliced breakbeats from the drum_kit samples, two-step shuffle hats, sub bass, a pluck lead; vocal chops made by slicing and pitching TTS syllables.
- **Foley of the materials**: liquid-metal glugs (resonant band-passed noise with pitch sweeps), rubbery inflate squeaks and boings, glass and glockenspiel sparkles with shimmer reverb, plastic clicks, whooshes.
- **Silence**: a high shimmering tone fading; then a single glint.
- **Voice**: upbeat futurist presenter, close, with light doubling or a subtle vocoder on single words. Music ducked ~6 dB; −14 LUFS.

## 8. Native moves

- **Mercury merge.** Two chrome blobs meet, neck and fuse into one form. *Fits content like:* a merger; two ideas combining; a partnership.
- **Inflate.** A flat word or icon puffs into 3D with a boing. *Fits content like:* a title; a price; a launch date.
- **Iridescent turn.** The hero turns and its colour sweeps through the thin-film spectrum. *Fits content like:* a special edition; a mood change; a new material.
- **Drip to form.** Chrome drips upward and condenses into an object. *Fits content like:* manufacturing; a future product; a wish coming true.
- **Fisheye peer.** An object leans into a wide lens and fills it. *Fits content like:* a hello; curiosity; a mascot's entrance.
- **Candy x-ray.** Translucent plastic reveals its inner parts as it turns. *Fits content like:* how something works; a gadget teardown; inside a creature.

## 9. Pitfalls of the medium

- **Grey, dead chrome** → a high-contrast environment with black and white bands; roughness ≤ 0.1.
- **Faceted metaballs** → raymarch the SDF or raise grid resolution; SDF normals.
- **Real gadget silhouettes and brands** → invent forms; no famous translucent shells or music players.
- **Rainbow kitsch** → narrow iridescence range, one iridescent object per shot.
- **Random sparkles** → only on specular hot spots, following the light.
- **Unreadable inflated type** → limit inflate radius, keep counters open, flatter at small sizes.
- **Excess on every object** → one hero material per shot; supporting objects simpler.
- **Bloom fog** → threshold high, bloom only speculars.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `env.js`: procedural studio env (strips, horizon, gels) → PMREM; `sweep(t)` for light passes.
- `blob.js`: SDF metaball raymarcher, `smin`, merge/split timelines, drips.
- `inflate.js`: glyph → SDF → inflated mesh or height field.
- `materials.js`: chrome, candy plastic, iridescent presets.
- `sparkle.js`: specular-point glints, starbursts, flares.

Start from `styles/glass-product/demo/studio.js` (env-map regeneration, mirror floor), `styles/glass-product/demo/product.js` (glass and metal materials), `styles/microgame/demo/glpass.js` (full-screen shader pass for the raymarcher), `core/three/post.js` (bloom, grade), `core/lib.js` (`spring`, `back`). Drums from `core/audio/sampler.py` (drum_kit, claps, glockenspiel, glass); synths in numpy.

## 11. Variation space

The agent decides the hero objects, the candy hues, the background key, the words that inflate, the pacing and the camera path.

- Structures: **a shape-shifter** (one chrome drop becomes a sequence of objects); **a countdown to a new year** (each digit inflates, melts and becomes the next); **a catalogue of the future** (imagined gadgets presented one per turntable).
- Openings: **a drop falls** onto a silver floor and ripples; **a flat word** on white inflates with a boing; **a fisheye face-off** with a chrome blob that leans in.
- Endings: **everything merges** into one sphere that reflects the viewer's side of the studio; **the title deflates** and slides away; **a final glint** on black.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
