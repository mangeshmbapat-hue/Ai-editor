# Cel-shaded 3D — Style Prompt

> Three-dimensional models rendered to look hand-drawn: flat colour bands from a stepped light ramp, ink outlines of constant weight, hard shadow shapes, and characters held on twos, so a 3D camera moves through a drawing.
> References (grammar only): early-2000s cel-shaded console games for inverted-hull outlines and two-band shading; 2D/3D hybrid TV anime (3DCG vehicles, crowds and later whole casts matched to hand-drawn cels) for stepped animation and hand-drawn effects over 3D; mid-century painted animation backgrounds for flat skies behind toon geometry. Never copy a game's or show's characters, vehicles, weapons or logo.

## 1. Essence, and what it is not

- **Light in bands, not gradients**: 2–3 hard-edged tone bands per material (lit, shadow, optional deep shadow) and a narrow rim band.
- **Ink lines of constant screen weight** on silhouettes, creases and intersections; thinner on interior detail.
- **Shadow is a colour**: each shadow band is a hand-picked hue, not the lit colour darkened.
- **The volume is real**: the camera orbits and dollies, and lines and bands hold at every angle; that is the reason to use 3D.
- **Drawn timing**: characters stepped on twos or threes, camera on ones; smoke, impacts and sparks are drawn 2D cards.

Not 1980s Cel Anime (2D cels, airbrushed backgrounds, CRT), not Sci-fi Toon (2D vector with boiling lines), not Low-poly Island (faceted flat shading, no outlines), not Brick Toy (photoreal plastic), and not a toon filter over PBR: no gloss, no ambient occlusion, no soft shadows.

## 2. Materials & rendering

- **Shading**: three.js `MeshToonMaterial` with a `gradientMap` (a 3–4 texel `DataTexture`, `NearestFilter` for min and mag, no mipmaps), or a custom shader: `band = step(k, NdotL × shadow)`, colour = mix(shadeCol, litCol, band), plus rim `step(.72, 1 − NdotV) × step(.2, NdotL)`.
- **Outlines, two kinds, take the maximum**: (1) inverted hull — a back-face copy in ink colour pushed out along **smoothed normals** (stored as a separate attribute so hard edges don't split), offset scaled by view depth so the width stays 2–4 px on screen; (2) a screen-space edge pass (Sobel on depth, normals and object ID) for creases and intersections, 1–2 px. Ink is a dark version of the fill or near-black, per material.
- **Faces**: transfer normals from an ellipsoid proxy so the face shadow is one clean designed shape; nose and cheek shadows as authored masks if needed. Eyes and mouths may be 2D textures swapped per expression.
- **Shadows**: shadow map thresholded (`step(.5, pcf)`), cast shadows tinted with the shadow colour; simple proxy casters to avoid jagged self-shadowing.
- **Highlights**: hard specular shapes `step(.96, NdotH)` only on hair, eyes and metal. No environment maps.
- **Backgrounds**: painted skies as cached canvases; distant toon geometry lifted toward the sky colour in 2–3 discrete steps (stepped fog) with thinner lines.
- **2D effects**: camera-facing cards with flat two-tone smoke, impact stars, speed lines, stepped on twos.
- Render at 2× and downsample for clean lines. Character clips are sampled at quantised time (`floor(t·12)/12`), so everything stays deterministic.

## 3. Colour logic

- Every material is a pair: lit colour + shadow colour (hue shifted 15–30° toward the scene's shadow tint, saturation slightly up, value down 25–40 %), with an optional highlight.
- One drawn sun per shot: its direction sets the bands. Time of day swaps the whole palette set (day, dusk, night), never the renderer.
- 5–7 hues per scene, saturated mid-values; the sky is the lightest large area; the ink is the darkest.
- The accent hue belongs to the hero's key object or costume detail and appears nowhere else.
- Never: gradients on characters, grey shadows on colour, white specular on skin.
- Example (day): sky `#8ec9f0`, grass `#7cc46a` / `#3f8f6b`, skin `#f6d2b8` / `#d99a8f`, cloth `#e24a3b` / `#a2305a`, ink `#2a2433`. Example (dusk): lit colours warmed toward `#f4a46a`, shadows toward `#5b4a8c`.

## 4. Type & subtitles

- **Titles**: Bungee or Righteous (Latin), Baloo 2 ExtraBold (Devanagari), as extruded 3D text with the same toon material and outline, or flat with a 6 px ink outline and one inner shadow band.
- **Subtitles**: game-dialogue style: white text with a 4 px ink outline, or inside a rounded box with an ink border; Baloo 2 SemiBold 38–44 px for both Latin and Devanagari. Bottom centre, never animated. Hold ≥ max(1.8 s, speech + 0.6 s).
- Small labels and UI: Space Grotesk or Inter 24–30 px.

## 5. Motion quality

- 24 fps. **Characters on twos** for normal action, threes for quiet acting, ones only for fast action; **camera always on ones** (a stepped camera judders).
- Pose-to-pose keys with strong silhouettes; a 1-frame smear (mesh stretched along velocity, or a 2D smear card) between fast keys.
- Squash and stretch by non-uniform bone scale is allowed; overlapping action (hair, cloth) by spring chains pre-simulated at a fixed rate and sampled on twos.
- Holds are moving holds: blinks, breath, eye darts.
- Effects appear on twos and dissipate in 6–12 drawings; objects enter by action, not by fading.
- Never moves: line weight, band thresholds, the painted sky (apart from slow parallax).

## 6. Camera grammar

A 3D camera that respects drawing. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Orbit around a held pose | the volume is real; a hero moment | a reveal; a transformation; a victory |
| Low-angle dolly, wide lens | power, speed | a launch; a sprint; a vehicle passing |
| Tracking alongside (character on twos, world on ones) | travelling together | a chase; a commute; a ride |
| Crash zoom, ≤ 6 frames | surprise | a realisation; a hit; a gag |
| Long-lens near-orthographic frame | a flat graphic layout like a drawing | a dialogue; a comic beat; a tableau |
| Fly-through of a toon set | the world as a place | an arrival; a tour; a map |
| Over-the-shoulder with layered depth | relationship | a confrontation; a negotiation |
| Dutch angle | unease | a threat; a dream; a fall |

Framing: favour three-quarter views; avoid angles where a silhouette collapses (looking straight down a cylinder or a limb). Long lens for acting, wide lens for action. Transitions: cuts on action, whip pans, shape or iris wipes; no crossfades (doubled outlines).

## 7. Sound palette

- Adventure orchestra: violins, cellos_spic, horn, trumpet, timpani, piano, glockenspiel, flute; or pop-rock with electric_guitar, electric_bass and drum_kit; or numpy chiptune for a game-like edge.
- Foley grounded in the material but a notch larger: whooshes on swings (noise sweeps), layered impacts, footsteps by surface, small UI blips for interfaces.
- A stinger on each hard cut or smear peak; a held pose before a big move gets only wind or room tone.
- Voice: expressive, dry character voices; music ducked 8 dB under voice; −14 LUFS.

## 8. Native moves

- **Orbit the drawing.** The camera circles a held pose while lines and bands stay clean. *Fits content like:* a new product turning on a stand; a mascot's debut; a statue in a square.
- **Smear frame.** A single stretched drawing sells a fast action. *Fits content like:* a goalkeeper's dive; a chef's knife; a frog catching a fly.
- **Light as palette swap.** The sun moves and the bands slide across faces, then the palette set changes. *Fits content like:* a day in a shop; a mood turning; a planet's night side.
- **Drawn effects over 3D.** Flat smoke, sparks and impact stars burst from solid geometry. *Fits content like:* a train departing; a firework show; a kitchen fire.
- **Ink-only frame.** For 2–4 frames shading drops away and only lines on white remain. *Fits content like:* a lightning strike; a shock realisation; a camera flash.
- **Freeze into a drawing.** A 3D frame holds and the camera pans across it like a 2D still. *Fits content like:* a group portrait; a memory; a cliffhanger.

## 9. Pitfalls of the medium

- **Broken outlines at hard edges** → push the hull along smoothed normals, not face normals.
- **Line width changing with distance** → scale the hull offset by view depth; cap it for distant objects.
- **Flickering terminator** on faces → proxy normals, a small bias on N·L, simpler geometry.
- **Posterised-PBR look** (too many bands, specular everywhere) → 2–3 bands, no environment light.
- **Game-cutscene feel** (everything on ones) → characters on twos or threes, camera on ones.
- **Grey, dirty shadows** → hand-picked shadow colours per material.
- **Jagged cast shadows** → higher shadow-map resolution, proxy casters, thresholded result.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `toon.js`: `toonMat({lit, shade, rim, steps})`, gradient-map builder, palette sets.
- `outline.js`: `addHull(mesh, px)` with a smoothed-normal attribute; `EdgePass({depth, normal, id, px})`.
- `stepper.js`: `stepTime(t, fps)` per object group (ones, twos, threes); smear helpers.
- `fx2d.js`: card sprites for smoke, impacts, speed lines.
- `sky.js`: painted backdrops, stepped fog.
- `post.js`: SSAA, edge pass, grade. Start from `core/three/post.js` (composer and supersampling; drop GTAO; keep depth of field only for far backgrounds) and the stylised composer in `styles/lowpoly-island/demo/post.js`.
- Also reuse: `styles/brick-toy/demo/set.js` (three.js set building), `styles/cel-anime-80s/demo/cel.js` (hand-picked shadow/highlight logic for 2D effect cards), `styles/scifi-toon/demo/toon.js` (2D ink for effect cards), `core/lib.js` (`mulberry`, `spring`); render with `core/render/still.mjs` / `video.mjs`; music via `core/audio/sampler.py`.

## 11. Variation space

The agent decides the world, the cast, the stepping per character, the palette sets, the lens language and how much of the frame is 2D.

- Structures: **one continuous journey** across a toon world, the camera on ones the whole way; **a day in four lights** (the same place, four palette sets, four small events); **a duel** (two characters, alternating long-lens dialogue and wide-lens action).
- Openings: **a flat painted frame** that turns out to be 3D as the camera starts to orbit; **ink only**, then bands fill in shape by shape; **a crash zoom** onto a character already mid-action.
- Endings: **freeze into a drawing** and pan away across it; **the sun sets** and the bands collapse to one shadow colour; **a long pull back** until the set reads as a small toy world.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
