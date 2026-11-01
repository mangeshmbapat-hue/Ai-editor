# Paint-on-Glass — Style Prompt

> Slow-drying oil paint pushed around on a lit glass sheet under the camera, repainted for every frame: light glows through thin paint, motion is paint dragged by a finger, and every shot melts into the next.
> References (grammar only): the under-camera paint-on-glass tradition of Soviet, Russian and Canadian studio shorts (1970s–2000s): oil on glass, multiplane sheets, painted camera moves; Impressionist plein-air painting for broken colour and light on water. Never copy a film's images, compositions or music, and never name them in the film.

## 1. Essence, and what it is not

- **A painting that never holds still.** Each frame is the previous frame wiped and repainted, so the surface lives; motion is paint *dragged*, leaving smears along its path.
- **Light through paint.** A backlit sheet: thin paint glows like stained glass, thick paint goes opaque and dark. Skies, water and faces are lit from within.
- **Metamorphosis instead of cuts.** One scene is smeared into the next: a wave becomes a mane, a window becomes a moon, a face turns into a field.
- **Painted camera.** Perspective changes are repainted, not computed: flights, turns and dives bend space like memory.
- **Visible fingers and brush**: wiped-thin streaks, finger smears with ridges, bristle tracks.

Not Impasto Oil Painting (thick knife paint under raking light; here paint is thin, backlit and flowing), not Watercolor Brush (no paper, no white of paper, no transparent washes that dry), not a painterly filter over 3D (strokes are designed and dragged, not sampled every frame from noise), not optical-flow morphing (no rubber warping of a picture).

## 2. Materials & rendering

- **Two layers per glass sheet**: pigment colour (RGB) and paint thickness `d`. Display: `out = light · T + top · albedo · (1 − T)`, with transmission `T = exp(−σ·d·(1 − albedo))` per channel. Thin paint glows tinted, thick paint shows its body colour lit from above, dark where both are low.
- **Target, then paint.** Each scene is designed as a value-planned painting (Canvas 2D strokes or a three.js render with object IDs and motion vectors). The paint layer is never the target itself: it is built from strokes that chase it.
- **Smear–advect–repaint, as a finite history** so every frame is a pure function of `t`: frame(t) = fresh strokes toward target(t) laid over the last 3–5 drawings, each advected forward along motion vectors, smeared along the motion direction (anisotropic blur 6–30 px) and faded. Nothing depends on a long simulation.
- **Strokes**: instanced finger smears (wide, ridged, lifting paint thin: `d` drops along the centre, rises at the edges), brush strokes (bristle tracks, ±15 % width noise), fingertip dabs, a wiping rag (broad, streaky, opens light). Seeded per drawing.
- **Boil only where things move**: static regions keep their strokes; moving regions are re-stroked every drawing. Boil amplitude follows motion magnitude.
- **Multiplane**: 2–3 glass sheets at different depths; the camera's focus softens the off-sheets; parallax only between sheets, never inside one.
- **Glass**: fixed dust specks and fingerprint haze anchored to each sheet.
- Colour mixing happens in pigment space (log or subtractive mix), never a linear RGB average, so complements darken instead of going grey.

## 3. Colour logic

- **Light is transmitted**: the brightest values are thin warm paint over the light; nothing is brighter than the lightbox.
- **Dark ground**: thick umber or blue-black paint is the neutral, where shadows and night live.
- 2–3 colour families per scene, value structure first: dark warm shadows, glowing mid-lights, one hottest light.
- **One accent** (a vermilion, a cobalt) reserved for a recurring element: a coat, a lantern, a boat.
- Smears mix neighbours; keep complements apart so drags stay luminous.
- Examples: *dusk harbour* — ground `#1c1a24`, water `#3e5f7a`, glow `#e8b45a`, accent `#c23b22`; *wheat and storm* — ground `#2b2116`, field `#c7a24a`, sky `#6f7f86`, light `#f2d99a`.

## 4. Type & subtitles

- **Titles are painted**: set in Cormorant Garamond or Playfair Display, rasterised as a target, then laid in with brush strokes and smeared away. Devanagari titles: Rozha One or Tiro Devanagari Hindi as the target.
- **Subtitles** sit on the darkest region in warm off-white: Cormorant Garamond 34–42 px, a soft dark halo, no box, never smeared. Devanagari: Tiro Devanagari Hindi or Noto Serif Devanagari. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output, paint redrawn on twos** (12 drawings/s); fast action may go to ones for a few beats.
- **Motion is smear**: a moving object leaves a short tail of dragged paint in its wake, length ∝ speed, that is repainted away over 2–4 drawings.
- Easing is fluid and slow (`ss`, `eio`); weight comes from the drag, not from squash.
- **Appear** by being painted out of the dark ground or wiped out of a thick area; **disappear** by being smeared into the next shape or buried under a wash of ground colour.
- **Never moves**: dust on the glass, the light behind it, static paint. If nothing in a region moves, its strokes hold.

## 6. Camera grammar

The camera is painted, so it can do what a lens cannot. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Painted dolly through a window, a door or an eye | Entering the next world | a memory; a dream; a story within a story |
| Painted turn (the room rotates around the viewer) | Disorientation, change of mind | a decision; a fever; a homecoming |
| Flight low over water or fields | Freedom, distance, longing | a journey; a flight; a season passing |
| Slow push on a face, features repainted | Inner life | a confession; recognition; grief |
| Multiplane drift (sheets slide at different speeds) | Depth, quiet travel | a forest; a crowd; a market at night |
| Locked frame, light wiped open | Revelation | sunrise; an idea; a truth admitted |
| Match-smear (a curve dragged into another curve) | Continuity of feeling | cause and effect; one life into another |

Framing: one luminous centre of interest per frame, darks around it. Transitions are metamorphoses (smear, wipe-to-light, bury-in-ground, dolly-through); never a hard cut between unrelated pictures, a crossfade or a digital wipe.

## 7. Sound palette

- **Romantic chamber or small orchestra**: `cellos`, `violins`, `violin`, `piano`, `harp`, `flute`, `clarinet`, `horn`, `vibraphone_bowed`; a solo line that carries a metamorphosis across the smear. An `accordion` or `guitar_nylon` for folk colour.
- **Foley belongs to the world, softened**: sea, wind, rain, footsteps, bells, low-passed and with a longer tail, as if remembered. The paint itself is near-silent; at most a soft wet swish (low-passed noise sweep) under big smears.
- **Silence**: a held painting with only room air, then one sound returning.
- **Voice**: a literary narrator or a character's inner voice, sparse; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Metamorphosis smear.** Shot A is dragged into shot B along a shared motion direction. Build: target(t) cross-weights two scenes along a stroke-shaped front, history advected along a designed flow. *Fits content like:* a ship becoming a whale; a city street becoming a riverbank; a mother's face becoming her daughter's.
- **Wipe to light.** A rag or finger clears thick paint, letting the backlight through. *Fits content like:* dawn over a village; a window opening in a prison cell; a diagnosis lifting.
- **Dolly through.** The painted camera enters an opening and the next scene is built around it. *Fits content like:* into a photograph; into a child's drawing; into a lit train window.
- **Drag of motion.** Fast movement leaves paint trails that fade. *Fits content like:* a horse at gallop; a crowd running for a bus; a dancer's turn.
- **Rain of strokes.** Vertical smears wash a picture downward into the next. *Fits content like:* a monsoon; tears; years passing.
- **Multiplane memory.** A foreground sheet (blurred) slides past a sharp middle. *Fits content like:* looking through reeds; a crowd remembered; a train window journey.

## 9. Pitfalls of the medium

- Boil everywhere reads as a swirl filter → boil only where motion is; static strokes hold.
- Smears turning everything to mud → keep the value plan; repaint key edges with clean strokes every drawing; mix in pigment space.
- Warping that looks like optical-flow morphing → every transformation is made of strokes and drags, never a mesh warp of the picture.
- Detail overload → minimum stroke size ~1/120 of frame width except eyes and highlights.
- Flat, unlit look → backlit transmission model; thin paint must glow.
- Long history simulations break parallel rendering → finite history of 3–5 drawings, seeded strokes.
- Faces drifting off-model in close-ups → keep a stable target; re-stroke only expression areas.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `glass.js`: per-sheet pigment and thickness buffers, the transmission/top-light compositor, dust and haze, multiplane focus; start from the WebGL2 compositor in `styles/shadow-puppet/demo/gl.js`.
- `strokes.js`: instanced finger smears, brush strokes, dabs and rag wipes into colour and thickness targets; start from the instanced stroke layout in `styles/impasto/demo/engine/impasto.js` and the ribbon and bristle model in `styles/watercolor/demo/engine.js`.
- `smear.js`: finite-history advection along motion vectors, anisotropic smear, motion-scaled boil (`history(t, n)`, `advect(buf, flow)`, `smear(buf, dir, len)`).
- `target.js`: scene targets in Canvas 2D or three.js (beauty, IDs, motion vectors), graded with `core/three/post.js`.
- `mix.py`: `core/audio/sampler.py`, softened `core/audio/sfx.py` foley, `core/tts/tts.py`.
Use `core/lib.js` (`mulberry`, `vnoise`, `ss`, `eio`); render with `core/render/video.mjs`, `srt.py`, `mux.sh`.

## 11. Variation space

You decide the subject, the number of glass sheets, the palette families and accent, how often scenes melt, whether there is a narrator, the opening, the ending and the painted camera path.

- Structures: **one unbroken metamorphosis** (a whole life or a day as one shot); **three seasons of one place** (the same view repainted, each season smeared out of the last); **a letter read aloud** (each sentence becomes a picture that melts into the next).
- Openings: **thick dark ground** wiped open by one finger to reveal a light; **a still painting** that suddenly starts to flow; **a close-up of wet paint** pulled back to show what it is.
- Endings: **buried in ground colour** until only one glow remains; **the light behind the glass switched off** and the paint seen opaque by room light; **a painted dolly out** through the same window we entered.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
