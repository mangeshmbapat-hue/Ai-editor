# Liquid Glass UI — Style Prompt

> A fictional interface made of floating glass: panes and lenses refract the colourful content beneath them, bend it strongly at their rounded edges, catch a moving specular rim, frost and clear, and merge or split like droplets of liquid.
> References (grammar only): the refractive, layered interface design of the mid-2020s (glass over content, adaptive tint, gooey shape transitions); optical lens physics (edge refraction, total internal reflection at rims, chromatic fringe); water droplets on a window. Never copy a real operating system's layouts, icons, controls, wallpapers, sounds or system fonts, and never name a product or brand in the film.

## 1. Essence, and what it is not

- **Two layers, one idea**: vivid content underneath and clear glass above. All meaning comes from what the glass does to what is behind it.
- **Edge lensing**: a rounded pane is nearly flat in the middle and bends the content strongly in a band near its rim, magnifying or compressing it, with a faint colour fringe.
- **A live specular rim**: a thin bright edge on the side facing the light, sliding as the "device" tilts.
- **Liquid behaviour**: panes stretch, wobble when they stop, merge into one shape when close and split like droplets.
- **Frost and tint**: clear → frosted → milky; the glass picks up the average colour beneath; glyphs on it switch between white and black for contrast.

Not Glass Product Render (a physical object in a dark studio; here a flat interface layer over content), not Frutiger Aero (gel shapes with a painted shine, nature motifs), not Y2K Chrome (reflective metal), not Living Screencast (no real product), not Dark Tech Keynote (no black stage and single accent; the glass itself is the star).

## 2. Materials & rendering

- **Content pass**: any scene rendered to a texture: a painted city, gradient blobs, a photo-like illustration, a scrolling feed made in code. It must be colourful and detailed, or the glass is invisible.
- **Glass shapes**: 2D signed distance functions (rounded rect, capsule, circle) combined with smooth union (`smin`, k = 8–24 px) for merges.
- **Lens shader** (WebGL2, per pixel inside a shape):
  - height profile from the SDF: flat centre, circular bevel of width `b` (6–15 % of the shape's short side) at the rim;
  - normal from the height gradient; refraction offset = `n.xy × strength`, strength scaled by an IOR-like factor (1.3–1.5 feel);
  - chromatic fringe: R, G, B sampled at offsets ×0.985, ×1, ×1.015;
  - frost: sample a pre-blurred pyramid (dual-Kawase levels) by `frost` 0–1;
  - tint: mix 5–15 % with the mean content colour under the shape;
  - lighting: Fresnel rim + a directional highlight from a light vector that rotates with tilt; inner shadow 1–2 px at the far rim; soft drop shadow on the content.
- **Analytic anti-aliasing** at every SDF edge (`fwidth`); render 2× and downsample.
- **Springs**: every size or position change is a damped spring evaluated in closed form from its start time (`x(t) = target + A·e^(−ζωt)·cos(ω_d t)`), so the wobble is deterministic.
- **UI glyphs**: flat line icons and text drawn above the glass with adaptive colour from the measured luminance beneath.

## 3. Colour logic

- **The glass has no colour of its own**; all colour comes from the content.
- **Content is rich**: 4–6 saturated hues with real detail (light, texture, faces of buildings, leaves).
- **Glyphs are white or near-black**, chosen per pane by the luminance beneath (threshold with hysteresis so they do not flicker).
- **One invented accent** (e.g. coral or mint) reserved for the active or selected state.
- Never opaque coloured cards, heavy drop shadows, or gradients painted onto the glass.
- Example content: dusk city `#ff7a59`, `#ffc15e`, `#5b8def`, `#2c2a4a`, `#9be7c4`; accent `#ff5a6e`.

## 4. Type & subtitles

- **Titles**: Inter 600–800 at 96–180 px, placed *in the content layer* so passing glass bends them; or on glass, white, when they must stay fixed.
- **Labels**: Inter 500 at 22–30 px, Space Grotesk for numbers.
- **Subtitles**: on a capsule pane (frost 0.6, tint 10 %) centred at the bottom, Inter 600 at 36–42 px, adaptive white/black. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Mukta 600 or Noto Sans Devanagari 600 in the same capsule.
- Contrast of subtitle text against the frosted pane ≥ 4.5:1, checked on rendered frames.

## 5. Motion quality

- Interface springs judder at 24 fps: master at 30 or 60 fps when the delivery allows; at 24 fps add short motion blur (4–6 sub-frames) to fast moves.
- **Springs, never linear slides**: under-damped for playful moves (ζ 0.5–0.7), near-critical for calm ones (ζ 0.85–1).
- Appear: a droplet buds off an existing pane and grows into its shape, or a pane condenses from frost. Disappear: merge back into a pane or shrink to a bead that fades.
- **Content moves under fixed glass** (scroll, pan, parallax) more often than glass moves.
- **Never**: 3D rotation of panes, opacity-only fades, rubbery panes that never settle to clean geometry.

## 6. Camera grammar

The "screen" is usually fixed; content and glass move. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Content scrolls beneath fixed glass | Flow, time passing | a day; a feed; a journey |
| A lens travels across fixed content | Searching, noticing | a detail in a document; a face in a crowd; a key figure |
| Push through a pane until it fills the frame | Entering a layer | opening a message; a deeper level; a chapter |
| Tilt (specular sweep + slight parallax) | Presence, premium | a reveal; a pause; a new product |
| Two panes side by side | Comparison | before/after; two options; two people |
| Pull back to show the glass floating over a whole world | Context | an overview; a city; a system |
| Locked frame, glass at rest | Calm, reading time | a statement; a quote; a number |

Framing: glass covers ≤ 40 % of the frame so content stays visible; panes on a soft grid with consistent corner radii; subtitles in the bottom capsule only. Transitions: lens wipe (a pane slides across and the next scene appears inside it, then spreads), merge/split, frost-up to milk and clear on new content; no hard glitch, no plain cross-dissolve.

## 7. Sound palette

- **Minimal and tactile**: short glass taps (glass, hand_chimes), droplet blips (sine with a fast pitch drop), soft sub thumps on merges, gentle airy pads (numpy), kalimba and marimba plucks, felt-like piano.
- **Liquid foley**: stretch = filtered noise with an upward bend; merge = a low "bloop" (two sines gliding together); split = a high pluck; frost = a soft breath of noise.
- **Silence**: room tone with a single tap.
- **Voice**: calm, close product narrator, dry. Music ducked ~6 dB; −14 LUFS. All interface sounds invented; never a real system sound.

## 8. Native moves

- **Lens over content.** A pane slides over a word or image and magnifies it at its rim. *Fits content like:* a clause in a contract; a highlight in a photo; a single price.
- **Merge and split.** Two panes melt into one and divide again. *Fits content like:* combining accounts; teamwork; a path forking.
- **Frost reveal.** A frosted pane clears to show what is beneath. *Fits content like:* privacy; a surprise; uncertainty resolving.
- **Tilt shine.** A specular sweep crosses every pane at once. *Fits content like:* a premium moment; a reveal; a breath before a statement.
- **The world flows beneath.** A long scroll of content under a fixed glass bar. *Fits content like:* a timeline; a train ride; a feed of news.
- **Droplet birth.** A bead buds off a pane and becomes a new control or notification. *Fits content like:* a message arriving; a new idea; an alert.

## 9. Pitfalls of the medium

- **Nothing beneath the glass** → it vanishes; always place busy, colourful content behind it.
- **Funhouse refraction** → keep strong bending in the rim band; centre nearly clear.
- **Illegible text on glass** → frost, tint and adaptive colour; check contrast per frame.
- **Copying a real OS** → invent layouts, icons and type; no control-centre clones, no system fonts.
- **Random sheen** → one light vector for all speculars, tied to tilt.
- **Jagged SDF edges** → analytic anti-aliasing and supersampling.
- **Spring judder at 24 fps** → higher frame rate or motion blur.
- **Blobby merges that never settle** → small merge radius, panes return to clean geometry.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `content.js`: renders the scene under the glass to a texture each frame.
- `sdf.js`: shape SDFs, `smin`, layout; shape parameters driven by `springs.js`.
- `springs.js`: closed-form damped springs keyed by start time.
- `lens.js`: WebGL2 refraction, fringe, frost pyramid, tint, rim light, shadows.
- `ui.js`: icons, labels, adaptive contrast, subtitle capsule.

Start from `styles/microgame/demo/glpass.js` (2D shader pass helper), `core/three/post.js` (blur and bloom techniques), `styles/glass-product/demo/product.js` (glass parameters), `core/lib.js` (`spring`, `eio`, `mulberry`). Sounds from `core/audio/sampler.py` (glass, hand_chimes, kalimba, marimba, piano) and numpy synthesis.

## 11. Variation space

The agent decides the content world, the number and shape of panes, the frost levels, the accent, the frame rate, the pacing and the motion of the content.

- Structures: **a commuter's day** scrolling under a few glass drops; **one document read through a lens** (each clause magnified in turn); **a conversation** (two panes that answer, merge and part).
- Openings: **frosted milk** clearing to reveal the world; **one bead** of glass falling onto the content and spreading into a pane; **content alone**, then a pane slides in and the first word bends.
- Endings: **all panes merge** into one and shrink to a dot; **the glass lifts away** and the content stands bare; **frost returns** over a final frozen frame.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
