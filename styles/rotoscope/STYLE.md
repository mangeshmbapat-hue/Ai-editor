# Rotoscope — Style Prompt

> Drawings traced over real motion: hand-wobbly contour lines and flat colour shapes that ride on the true weight and timing of a moving body, so the surface is drawn but the movement is lived.
> References (grammar only): the rotoscope as patented in 1915 (tracing projected motion frame by frame); Eadweard Muybridge's motion studies (1870s–80s) for how real bodies move; 2000s interpolated-rotoscope features for floating flat-colour shapes over traced performance. Never copy a film's frames, characters or designs, and never name them in the film. **The source motion comes only from this film's own 3D or rig renders, or from footage the user owns or has the rights to; never trace someone else's film.**

## 1. Essence, and what it is not

- **Real motion, drawn surface.** Weight shifts, overlapping action and micro-gestures are true to life; the image is lines and flat colour. That tension is the style.
- **Chosen lines.** A contour around each figure and a few inner lines (jaw, fold, hand), slightly wobbly, variable width. Not every edge is traced.
- **Flat fills in 2–3 bands** (base, shadow, sometimes highlight) whose borders are traced too and shimmer a little from drawing to drawing.
- **Drawn on twos, traced fresh each drawing**: a light line boil that is part of the look.
- Backgrounds are simpler than figures: held paintings, or traced with fewer lines.

Not 80s Cel Anime (designed characters, model sheets, stylised timing with holds and smears; rotoscope keeps real proportions and timing), not 1920s Silent Film (ink and hatching through the Redraw pass on an engraved world; here contour plus flat colour), not a cartoon filter over footage (a filter traces every edge every frame; rotoscope selects lines and keeps fills stable), not cel-shaded 3D (no clean geometric outlines).

## 2. Materials & rendering

- **Source** (the film's own): a three.js scene with rigged characters animated by keyframes or by motion capture the user owns; or footage the user shot or licensed, with its licence recorded in the project. Render passes per source frame: beauty, object/material ID, normals, depth, motion vectors; render without motion blur (shutter 0).
- **Sample on twos**: trace source frames at 12 per second and hold each drawing for 2 frames. Fast action may go to ones for a few beats; slow drifts to threes.
- **Trace**: silhouettes from ID boundaries, inner lines from depth breaks and normal creases above a threshold; for footage, use user-painted or tracked mattes as IDs and XDoG edges only as a guide. Vectorise with marching squares, simplify (Douglas–Peucker), drop segments shorter than ~1/80 of frame height, smooth with Catmull-Rom.
- **Redraw as a hand line**: width 1.5–4 px with ±20 % noise along the arc, tapered ends, open gaps where light hits; per-drawing seeded jitter of 0.5–2 px (line boil), consistent within a drawing.
- **Fills**: one flat colour per region from stable IDs (never per-frame clustering); shading bands from posterised N·L (3D) or posterised luminance inside the matte (footage), band borders jittered like lines.
- **Line-free variant**: only colour shapes, slightly offset and drifting (a dream register).
- **Backgrounds**: painted once and held while the camera holds; traced on twos when it moves.
- All jitter and boil seeded by drawing index: every frame is a pure function of `t`.

## 3. Colour logic

- 5–8 flat colours per scene; each base colour has one shadow step (darker, slightly cooler) and at most one highlight.
- Figures more saturated than backgrounds; backgrounds one value step quieter.
- **Line colour** is a dark coloured ink (deep blue-brown, aubergine), never pure black; or no line at all in the line-free variant.
- **One accent** reserved for a recurring element (a jacket, a lamp, a bicycle).
- Colour may shift with mood by scene, never by drawing: fills must not flicker.
- Example: *monsoon street* — ground `#2f3b44`, skin `#c98b6b` / `#a0644d`, shirt `#e6d6b0` / `#b8a37f`, line `#1f1a2b`, accent `#d8452f`.

## 4. Type & subtitles

- **Titles are traced lettering**: set in Bebas Neue, Oswald or Permanent Marker, then traced like the figures (wobble, boil, flat fill); Devanagari titles traced from Yatra One or Rozha One.
- **Subtitles stay steady** (boiling text tires the eye): Inter or Hind 34–40 px, warm off-white with a 2 px dark-ink outline, lower third, no box. Devanagari: Hind or Mukta. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output, drawings on twos** by default; ones for fast action, threes for drift. One stepping rule per shot for figures and camera together.
- Timing is the source's. Do not add squash and stretch; exaggerate only by selection (holding a drawing on a key pose a little longer).
- **Boil**: 0.5–2 px on lines, 0.5–1 px on fill borders; less on faces in close-up; held shots may use 2–3 cycling drawings.
- **Appear** by tracing on (the line layer draws over the moving figure, then fills drop in) or by fills floating into place; **disappear** by lines dropping out and fills drifting off.
- **Never moves**: held backgrounds while the camera is locked; a fill's colour within a scene.

## 6. Camera grammar

The source camera is a real camera, so the film can move like documentary or drama. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Handheld medium on a talking face | Presence, candour | an interview; a confession; an argument |
| Long tracking shot beside a moving body | Real effort and rhythm | a cyclist; a dancer warming up; a porter climbing stairs |
| Locked wide with a performer crossing | Weight in space | a craft at work; a sport; a daily routine |
| Slow push on hands | Skill and intent | cooking; repairing; playing an instrument |
| Whip pan traced through | Energy, a jump in attention | a goal; a near miss; a sudden sound |
| Layer peel on a locked frame (source → lines → fills) | The making visible | a reveal; reality slipping; a memory forming |

Framing: faces and hands get the most lines; keep a quiet band for subtitles. Transitions: trace-on, lines dropping out, fills drifting to the next scene, a hard cut on action; avoid crossfades between traced shots (doubled lines).

## 7. Sound palette

- **Naturalistic sound design first**: real-feeling foley and ambience under the drawn picture (footsteps by surface, cloth, breath, room tone, traffic, rain), built from `core/audio/sfx.py` and filtered noise.
- **Music**: small and contemporary: `guitar_nylon` or `pluck('acoustic_guitar', …)`, `upright_bass_pizz`, `electric_bass`, brushed `drum_kit`, `piano`, `vibraphone`, numpy pads; detuned pads and reversed swells for a dream register.
- **Silence** is real room tone, never digital zero.
- **Voice**: natural and conversational, often the person we see (recorded by the user with consent) or a TTS voice for a fictional character; music ducked ~10 dB under voice; final −14 LUFS.

## 8. Native moves

- **Trace-on.** Lines draw over the moving figure, then flat colour drops in. *Fits content like:* a person being introduced; an athlete before a race; a worker starting a shift.
- **Reality slip.** Lines thin out and colour shapes drift loose from their source, then snap back. *Fits content like:* a memory; exhaustion; falling asleep on a train.
- **Layer peel.** Source render, line layer and fills are revealed one at a time on a locked frame. *Fits content like:* how an animation is made; seeing through a pose; a change of perspective.
- **True weight.** One unbroken traced performance where real timing is the point. *Fits content like:* a dancer's turn; a potter centring clay; a climber on a wall.
- **Line-to-world.** A traced contour continues past the figure into an impossible shape. *Fits content like:* a thought taking form; music made visible; a road unrolling.
- **Talking colour.** An interview where face colour shapes shift slowly with feeling. *Fits content like:* a testimony; a debate; a late-night conversation.

## 9. Pitfalls of the medium

- Using someone else's film or footage as the source → trace only the film's own renders or footage the user owns or has licensed, with the licence and any performer consent recorded.
- Auto edge detection on every edge looks like a filter → select lines: silhouette plus a few inner lines; drop texture edges and short segments.
- Fills that flicker → colour by stable IDs or tracked mattes, never by per-frame clustering.
- Boil too strong → cap at 2 px; less on faces; steady subtitles.
- Uncanny faces from tracing every detail → eyes, brows, mouth and one jaw line; nothing more.
- Doubled lines from motion blur in the source → render the source with shutter 0.
- Robotic 3D source motion → owned mocap or keyed acting with overlap and settle; handheld camera noise.
- Mixed stepping (camera on ones, figures on twos) judders → one stepping rule per shot.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `source.js`: three.js scene and rig with passes (beauty, ID, normal, depth, motion), shutter 0; scene and light setup after `styles/brick-toy/demo/set.js`, grade with `core/three/post.js`.
- `trace.js`: ID-boundary and crease extraction, marching squares, simplification, Catmull-Rom, selection rules (`traceFrame(passes, {minLen, crease, depthBreak})`); hand-line drawing with constant screen width and boil after `styles/rubber-hose/demo/toon.js`; XDoG guide edges for footage from `styles/silent-film/demo/engine/redraw.js`.
- `fill.js`: flat fills and jittered shading bands by ID (`fillFrame(ids, bands, palette)`), after `styles/cel-anime-80s/demo/cel.js`.
- `matte.js`: footage mattes plus the licence record.
- `mix.py`: foley via `core/audio/sfx.py`, music via `core/audio/sampler.py` / `core/audio/pluck.py`, voice via `core/tts/tts.py`.
Step time with `seg` and seeds with `mulberry` from `core/lib.js`; render with `core/render/video.mjs`, `srt.py`, `mux.sh`.

## 11. Variation space

You decide the subject, the source (rig, owned mocap or owned footage), lines or line-free, the palette and accent, the stepping, the opening, the ending and how often reality slips.

- Structures: **a portrait interview** (one person talking, cut with traced scenes of their work); **one day of a body at work** (shift start to shift end, each task a long traced take); **two realities** (a traced everyday routine that keeps slipping into floating colour as a daydream grows).
- Openings: **the raw render** of a moving figure, traced over as we watch; **floating colour shapes** that gather into a person; **a black frame** with only a line drawing breathing in it.
- Endings: **lines drop out** and the colour shapes drift apart; **the trace stops** on one held drawing while the world keeps moving; **a layer peel back** to the source render, then to an empty set.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
