# Tanjore — Style Prompt

> Thanjavur painting as a lit object: flat bright colour on a gessoed board, raised relief built up under gold foil, inlaid stones that flash, a dark carved frame, and a lamp or raking light that moves across it so the gold breathes and the stones wake.
> References (grammar only): Thanjavur painting of Tamil Nadu, which flourished under the Maratha rulers of Thanjavur (17th–19th centuries): cloth pasted on a wooden board, a chalk-and-glue ground, raised ornament modelled in paste and covered with gold foil, inlaid glass or semi-precious stones, bright flat colours and a large central figure under an arch with curtains. Take the relief, the foil, the stones and the framing; never copy a specific painting or create a devotional image, and never name them in the film.

## 1. Essence, and what it is not

- **Flat paint, raised gold.** The figures and grounds are flat, opaque colour with dark outlines; everything ornamental (crowns, jewellery, pillars, arches, borders) stands in low relief under gold foil.
- **Stones catch the light**: red, green and clear cabochons and cut glass set into the gold, each with its own glint.
- **Frontal and framed**: a large central subject faces out, under an arch with drawn-back curtains and pillars; the board sits in a dark carved frame.
- **Light is the motion.** The painted world does not move; a lamp, a raking sun or the camera moves, and the gold and stones answer.
- **Rich, warm, dense**: gold covers a third or more of the surface.

Not Art Deco (no geometric airbrush or engraved line; gold is crinkled foil over modelled relief, with stones), not Glass Product (not a studio product render; a painted panel with matte colour), not Paper Pop-up (relief is modelled paste, not folded paper), not Pichwai (that is gold paint on dyed cloth; here gold is foil on raised gesso).

## 2. Materials & rendering

- **Board model (three.js)**: a `PlaneGeometry` (≥ 1024 × 1024 segments, or a displacement map in the shader) with maps generated in Canvas 2D from masks: `albedo` (flat paint, dark outlines), `height` (relief), `metalness` (1 under foil, 0 on paint), `roughness` (foil 0.25–0.4 with crinkle noise, paint 0.75–0.9), `normal` (from height + foil crinkle).
- **Relief**: height from ornament masks by repeated dilate-and-blur (beads along paths, ridged borders, pillar flutes), 1–4 mm equivalent; low enough that raking light reveals it and frontal light flattens it.
- **Foil**: warm gold base (`#d4a347`-ish), micro-crinkle normals (ridged noise, 0.2–0.6 mm), slight cracks where foil broke over sharp relief showing the red-brown bole below.
- **Stones**: `InstancedMesh` cabochons and facets in sockets, `MeshPhysicalMaterial` (`transmission`, `ior` 1.5–1.6, attenuation colour), a gold socket rim, a small RGB offset in the glint for dispersion.
- **Light**: one warm point light (lamp, 1800–2400 K) or a raking directional light; low ambient; a PMREM environment from a warm gradient room so gold reflects something; flicker 3–5 % value noise.
- **Frame**: dark wood with carved mouldings and a thin gilt inner edge.
- **Post**: `core/three/post.js` bloom (glints only), warm grade, gentle DOF for macro. Maps are baked once; everything is a function of t under fixed seeds.

## 3. Colour logic

- **Paint**: 4–6 flat, saturated colours (red, green, blue, white, a skin tone, a dark outline colour). No gradients or shading on paint.
- **Gold is the light colour**; unlit, it reads ochre-brown, lit, near white-yellow.
- **Stones**: red, green, clear; one stone colour can carry the film's accent.
- Grounds are flat red, green or blue fields behind the central subject.
- Value order under light: glints > lit gold > white paint > colours > outlines > frame.
- Example: red `#b3262d`, green `#1f6b4a`, blue `#2a4a9a`, white `#f2ece0`, skin `#e2b48a`, outline `#2a1a12`, gold `#d4a347`, bole `#7a2f1e`, frame `#2b1d14`.

## 4. Type & subtitles

- Titles are **gilded relief letters**: text rendered to a mask, raised in the height map, foiled, revealed by light. **Cinzel** or **Playfair Display** for Latin (80–130 px); **Tiro Devanagari Hindi** for Hindi; **Noto Serif Tamil** for Tamil.
- Subtitles sit on a **dark plinth band** below the panel or within the frame's lower moulding: cream **Cormorant Garamond** semibold 36–44 px, Hindi in Tiro Devanagari Hindi (Hindi subtitles are supported). No glow.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s); fade 0.25 s.

## 5. Motion quality

- **24 fps.** Painted figures never animate. What moves: light, camera, and the making process.
- **Light moves slowly**: a lamp carried across (eased, a slight sway), a raking light rotating 10–40°, a flicker. Glints bloom and fade as normals align (they must, by the physics, not by keyframes).
- **Making moves**: relief rises (height from 0 with `eo`, 1–2 s), foil drapes and its crinkle drops as it is pressed, stones drop into sockets with a tiny settle (`back`).
- Camera moves are slow dolly and orbit (±25° maximum off-axis), macro slides across relief like a landscape.
- Never moves: the paint, the figures, the frame.

## 6. Camera grammar

A precious panel on a wall in a dim room; the camera handles it like a conservator with a lamp.

| Move | What it expresses | Can serve |
|---|---|---|
| Frontal, locked, lamp crossing | the object revealed by light | an unveiling; a summary; a heritage moment |
| Raking orbit, ±25° | the relief and its depth | craft; detail; value |
| Macro slide across relief | a landscape of gold | a journey in miniature; a material study; texture |
| Push into one stone | the one precious thing | a key insight; a gift; a promise |
| Pull back to the framed panel on a wall | the object in the world | a collection; an ending; a place |
| Locked macro, process step | making as meaning | building something; layers of effort; a step-by-step |
| Lamp held still, camera breathing | contemplation | a pause; reverence; reading time |

Framing: frontal wides keep the arch centred; macro shots keep one stone or ornament as hero. Transitions: the lamp leaves and darkness takes the frame; a glint flares white for a few frames; a pull back through the moulding. Forbidden: crossfades, lens flares, whip moves, spinning the panel.

## 7. Sound palette

- **Instruments as options**, in the manner of South Indian classical music: a plucked lute with deep glides (`pluck('koto', …)` with bend, like a veena), a tuned barrel drum (synthesised tabla model, tighter), a drone (`pluck('shamisen', …)`, long t60, buzz), a double reed (`oboe` + 1.2–3 kHz formant + saturation), clay-pot strokes (synthesised). Never imitate temple music or a specific composition.
- **Glints** sound as soft high shimmers (`glass`, `glockenspiel`, `hand_chimes`), only when a stone or a ridge lights.
- **Foley**: spatula on gesso paste, foil crinkle, burnishing rub, a stone clicking into its socket, a frame knock, lamp flame flutter.
- **Silence**: the lamp still, only flame flutter.
- **Voice**: calm and close, like a guide in a quiet hall; Hindi or Tamil narration fits. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The light sweep.** A lamp or raking light crosses and gold answers in a travelling band. *Fits content like:* a reveal of a result; attention moving through a plan; dawn on something valued.
- **Relief rises.** Flat painted ornament swells into gold relief. *Fits content like:* effort adding value; a skill maturing; a plan becoming real.
- **Foil press.** A crinkled sheet laid and burnished smooth. *Fits content like:* finishing; polishing a pitch; healing.
- **Stone setting.** Stones drop into sockets one by one, each with a glint. *Fits content like:* milestones; team members; awards.
- **The arch frame.** Whatever sits under the gilded arch reads as honoured. *Fits content like:* a founder's portrait; an award; a heritage object.
- **Macro landscape.** The camera crosses relief as if over hills of gold. *Fits content like:* the inside of a process; a tiny world; data as terrain.

## 9. Pitfalls of the medium

- Chrome-smooth gold reads as CGI → warm tint, crinkle normals, roughness 0.25–0.4, cracks to bole.
- Plastic stones → transmission, IOR, attenuation, a gold socket rim, tiny dispersion.
- Everything shiny → paint stays matte; metal only under foil.
- Relief too high reads as sculpture → 1–4 mm equivalent; show it with raking light.
- Bloom halos everywhere → threshold high, glints only.
- Animated figures break the object → animate light, camera and process only.
- **Sacred icons.** Thanjavur paintings are largely devotional images of deities: never create a deity image for a product, never place a logo, product or person in the deity's place under the arch, and keep the arch for what is honoured with care. Do not present a code-made film as an authentic Tanjore painting; for commercial work, credit or consult Thanjavur artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `maps.js`: Canvas 2D bakes from masks: `albedo`, `height` (`dilateBlur`, `beads(path)`), `metal`, `rough`, `normalFromHeight`, `foilCrinkle(seed)`.
- `board.js`: three.js board mesh, `MeshStandardMaterial` with the maps, frame mouldings, `reliefRise(p)`, `foilPress(p)`.
- `stones.js`: `InstancedMesh` cabochons and facets, `MeshPhysicalMaterial`, sockets, `setStone(i, p)`.
- `light.js`: lamp with flicker, raking rig, PMREM room; `film.js` for camera paths, post, subtitles, `render(t)`.

Start from `styles/glass-product/demo/studio.js` (`makeStudio`: lights, environment, renderer) and `styles/glass-product/demo/product.js` (`glass`, `metal` materials, `canvasTex`), `styles/paper-popup/demo/cutmesh.js` (meshes from 2D cut paths), `core/three/post.js` (bloom, DOF, grade), `core/lib.js`, `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`.

## 11. Variation space

You decide the subject under the arch (never a deity used casually), the colours, the stones, how light travels, whether the making is shown, the opening, the ending, the camera path and the pacing.

- Structures: **the making** (board, ground, drawing, relief, foil, stones, paint, frame: one step per idea); **one panel, many lights** (the same finished panel under dawn, lamp and dusk, each revealing different detail); **a wall of panels** (several small panels, each a chapter, joined by a passing lamp).
- Openings: **darkness and one glint**; **a bare wooden board** receiving its cloth and ground; **an extreme macro** of foil crinkle, pulled back until it is a crown.
- Endings: **the lamp set down**, the panel glowing still; **the last stone set**; **the frame closes** around the panel and the camera retreats into the dim room.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
