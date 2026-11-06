# Bollywood Hand-painted Poster — Style Prompt

> The hand-painted cinema hoarding brought to life: giant brushed faces lit in two impossible colours, collaged action vignettes and a fat hand-lettered title, in enamel on a board above a busy street.
> References (grammar only): the banner-painting studios of Mumbai and the hand-painted posters and hoardings of Hindi cinema (c. 1950s–1980s) for colour-lit faces, collage hierarchy and extruded hand lettering; the giant painted cut-outs of South Indian cinema for scale. Never reproduce a real film title, actor's likeness, studio name, logo, layout or song, and never name them in the film.

## 1. Essence, and what it is not

- **A painted face is the hero**: a head filling 1/3–1/2 of the board, lit by two colours at once (warm orange, yellow or pink on one side, cool green, blue or violet on the other), built from visible strokes.
- **Collage hierarchy**: the hero face, a second face, then 3–6 small vignettes (a chase, a couple, a fist, an explosion) on a hot sky with no shared perspective. Size is importance.
- **Hand-lettered title**: fat Devanagari and Latin letters with an outline, an extruded block in a darker shade and a drop shadow; a tagline and credits in smaller hand lettering.
- **Enamel, not airbrush**: wet-into-wet blends, crisp highlight dabs, the odd drip; the board shows (weave, seams, the chalk enlarging grid).
- Tone: melodrama, every feeling at full volume, the street as gallery.

Not Impasto (no knife relief; enamel lies flat and glossy), not Silkscreen Poster (no registered flat inks; colour is brush-blended), not Art Deco (no gold line, no centre axis), not a photo under a "painterly" filter: every face is painted up from blocks of colour.

## 2. Materials & rendering

- **Board** (cached, world-anchored): primed cloth or tin panels with seams, noise-warped weave, the chalk squaring grid faint under thin paint, sun-fade, rust runs, rain streaks.
- **Stroke model**: Catmull-Rom ribbons, 0.6–4 % of face height, ±15 % width noise, a colour gradient *across* the width (wet blend) and bristle texture *along* it; enamel gloss as a faint specular streak sliding with the camera.
- **Paint order** (slices of an element's progress): chalk grid → charcoal outline → block-in (6–12 big strokes per region) → modelling strokes along the form → low-opacity blends on value edges → highlight dabs → dark accents.
- **Faces**: an invented head (ellipsoid SDFs plus feature curves) gives a value map, split by light direction into a warm ramp (lit) and a cool ramp (shadow), posterised to 5–7 steps and rebuilt as strokes along the iso-lines: painted, not filtered. Faces come from parameters (jaw, brow, nose, hair), never from a photo.
- **Lettering**: font outline → hand wobble (±1 % cap height) → 2–3 flat bands → outline → darker extrusion (stepped offsets toward a vanishing point) → drop shadow; one sprite per grapheme cluster.
- **Collage**: each vignette is a painted plane with a feathered halo or hard cut edge, stacked in z for parallax. **Night**: bulbs along the frame (additive glow), warm spill. Stroke lists are seeded once; progress is a pure function of `t`.

## 3. Colour logic

- **6–9 saturated enamels**; neutrals only in primer, street and scaffold.
- **Two-colour face light is the rule**: warm key + cool shadow, chosen per character (hero gold-orange, rival green-violet, lover pink-magenta) and kept for the film.
- **Skies**: 2–3 hot bands in horizontal strokes; behind a face, its complement.
- **The title owns the brightest value**, extruded in a darker same hue, never the sky's hue.
- **Black** only for outlines and hair; **white** only for highlights, teeth, eyes.
- Example (action): sky `#e0471b` → `#7a1a5c`, hero key `#f5b04a` / shadow `#2d6f8f`, rival key `#6dbd4b` / shadow `#3a1f5c`, title `#ffd21a` extruded `#b0161b`, outline `#111111`.
- Example (romance): sky `#f4a0b8` → `#6fc6d8`, key `#ffcf9e`, shadow `#9a5fc0`, title `#e6233c`.

## 4. Type & subtitles

- **Titles are lettering, not type**: skeletons from Rozha One or Yatra One (Devanagari), Shrikhand or Anton (Latin), Noto Nastaliq Urdu for an Urdu line (only text checked by a reader), then wobbled, extruded, outlined. Titles and names are invented.
- **Taglines and credits**: Hind or Mukta Bold, Oswald, in painted strips.
- **Subtitles** sit in the painted credit band: Baloo 2 or Mukta SemiBold 34–44 px (Hindi in Baloo 2 or Hind), yellow or white, dark outline (10–14 % of x-height), 2–3 px offset shadow, no box; in street shots, a small painted placard.
- Per-letter animation splits by grapheme cluster (`Intl.Segmenter`) so matras stay with their base. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps**, camera on ones. Paintings are still: life comes from camera, plane parallax, light changes and a few cut-out parts on twos (hair, a dupatta, smoke).
- **Painting-in**: each stroke lands in 2–4 frames; the hand's rhythm shows.
- **The melodrama zoom**: a fast push (0.25–0.4 s, `ei`, hard stop) onto a face, then a hold.
- **Vignettes** slide in with a small `back` overshoot or are painted in; **letters slam** one by one (scale 1.4 → 1), then the extrusion grows. Holds matter; no constant drift.
- Never moving: the board frame, the chalk grid, a landed title (except a gloss sweep).

## 6. Camera grammar

The camera stands in the street, climbs the scaffold or dives into the paint. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Street-level wide, hoarding above traffic | a public promise; scale | an announcement; a town's talk; a launch |
| Melodrama zoom into a face | the feeling at full volume | a vow; a shock; a betrayal |
| Pan from vignette to vignette | many threads at once | a summary; parallel lives; a list |
| Tilt up the scaffold to the painter | craft and scale | a making-of; a dream being built |
| Dutch tilt on the rival's plane | menace | a threat; a deadline; a storm |
| Parallax dolly between collage planes | entering the poster world | backstory; a memory; a flashback |
| Locked whole board | the full promise | a choice; a summary; reading credits |

Framing: never crop a face through the eyes; titles legible ≥ 2 s; planes never collide with the title. Transitions: whip pan to the next board; a paint-over rolled across the old poster; a peel; a flash cut on a stinger. Forbidden: glitches, 3D cube flips, soft dissolves between faces.

## 7. Sound palette

- **The period film orchestra**: `violins` (swells, `violins_trem`, `violins_spic` runs), brass stabs, `conga` and bongos, `drum_kit` and `toms`, `electric_guitar` through a swept band-pass (wah), `electric_bass`, `organ`, `harmonica`; tabla and sitar recipes; a dulcimer shimmer from `dan_tranh_trem`.
- **Techniques, as options**: a string stinger on each zoom; tremolo under suspense; brass and toms for action; a hard stop on a slap.
- **Foley**: brush on canvas, paint-tin lid, ladder creak; street (horns, a synthesised two-stroke putter, crowd, a projector whir); vignette action (punch = `thump` + `whoosh` + cloth snap, ricochet = falling sine glide).
- **Silence**: the street drops out under one painted stare; one far bell.
- **Voice**: an emphatic trailer announcer or stagey dialogue, short lines, hall reverb, optional 150 Hz–7 kHz band-limit. Music ducked 8–10 dB; −14 LUFS. Never reuse a real song, melody or dialogue.

## 8. Native moves

- **Painted up from the grid.** A squared reference card is scaled onto the board; strokes build the face. *Fits content like:* a design going from sketch to billboard; a child's drawing becoming a mural; a plan scaled to a city.
- **Two-colour light.** Swapping warm and cool flips a character's meaning. *Fits content like:* a hero's doubt; a product by day and by night; a public figure's two sides.
- **Collage cascade.** Vignettes appear around the hero face by importance. *Fits content like:* a festival's highlights; a recipe's ingredients; a neighbourhood's characters.
- **Title slam.** The extruded title lands letter by letter. *Fits content like:* a launch; a chapter heading; a slogan.
- **Repainted hoarding.** A new poster painted over the old, its edges still showing. *Fits content like:* news changing weekly; a shop's reinvention; an election season.
- **Street-scale reveal.** From a painted eye out to the hoarding above traffic. *Fits content like:* a local hero celebrated; a public notice; a neighbourhood's pride.

## 9. Pitfalls of the medium

- **Likeness and IP**: never real actors, titles, studios, logos or lyrics. Generate faces from parameters and check they don't resemble a celebrity; invent every name.
- Airbrushed smoothness → visible strokes, posterised values, dabs.
- Realistic single-colour light → the warm/cool split.
- Broken Devanagari (detached matras) → shape whole words, split by grapheme cluster, have a reader check.
- Equal-sized vignettes → one hero, one or two seconds, the rest small. Title lost in the sky → outline, extrusion, contrast check.
- **Living craft**: hand-painted banners are a living and shrinking livelihood. Don't present the film as authentic hand-painted work; credit the tradition, and for commercial work commission or consult banner painters. Keep religious figures out of decoration.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `board.js` (panels, weave, chalk grid, weathering, bulbs); `brush.js`: `stroke(path, w, colA, colB, bristle)` with wet blend, drips and progress.
- `face.js`: `head(params)` → value map; `splitLight(warmRamp, coolRamp, steps)`; `strokesFromIso(map)`.
- `letter.js`: `segment(text)` by grapheme; `letter(glyph, wobble, bands, extrude, outline, shadow)`; `collage.js` (planes, halos, parallax); `mix.py`.

Start from: `styles/watercolor/demo/engine.js` (`mk`, `drawS`, `sprite`, `withSeed`); `styles/impasto/demo/engine/impasto.js` (painted planes and post defaults); `styles/art-deco/demo/engine/bulbs.js` (`buildSign`, `litSequence`) and `styles/art-deco/demo/engine/type.js` (layered title lettering); `styles/silkscreen-poster/demo/engine/silk.js` (`bandSteps`, `paperSheet`); `core/lib.js`; `core/render/still.mjs`; `core/audio/sampler.py`, `core/audio/sfx.py` (`thump`, `whoosh`, `crash`).

## 11. Variation space

You decide the subject, genre colours, number of boards, whether street and painter are seen, the opening, the ending and the camera.

- Structures: **a week of hoardings** (one board repainted daily as the story moves); **one poster, many planes** (each vignette entered as a scene); **the painter's day** (squaring, faces, title, the street's reaction).
- Openings: **a tiny reference card** squared in pencil; **a painted eye** in extreme close-up; **a blank whitewashed board** over a loud street.
- Endings: **the bulbs come on** and the street walks past; **a new board is hoisted over it**; **the last letter dries** and the painter climbs down.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
