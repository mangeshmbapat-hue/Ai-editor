# Phad Scroll — Style Prompt

> A long painted cloth scroll performed at night: the whole story is laid out at once across metres of cloth in flat yellow, red and green, and a storyteller's lamp moves along it, lighting one episode at a time while a bowed fiddle and a voice tell it.
> References (grammar only): the *phad* of Rajasthan (around Bhilwara and Shahpura), long cloth scrolls painted by the Joshi families with the epics of regional folk deities, unrolled at dusk and performed through the night by *bhopa* singer-priests who sing, play the *ravanhatta* fiddle and light each episode with a lamp. Take the all-at-once layout, scale by importance and the lamp as the reader's cursor; never copy a scroll's figures or episodes, and never name them in the film.

## 1. Essence, and what it is not

- **One very wide cloth** (8:1 to 15:1) holds the entire story; nothing is cut into frames or panels with borders. Episodes sit side by side, grouped by place and time.
- **Scale by importance.** The central figure is several times larger than the rest; groups of small figures in profile face each other or face the centre.
- **Flat, bright, crowded**: saturated yellow, orange-red, green, brown, a little blue, all held by black outlines; every area filled.
- **The lamp is the reader.** At night only a warm pool of light shows the episode being told; the rest of the cloth waits in near darkness.
- **Performance is part of the image**: the scroll's rolled ends, its support poles, the ground in front, the singer's shadow and the audience may be seen.

Not Shadow Puppetry (light falls *on* painted cloth from the front; nothing is cut, carved or backlit), not Ukiyo-e or Printed Long Take (no woodblock, no print lines, no layered depth: the cloth is flat and the camera travels along it), not Pattachitra (no panel borders, no lacquer; one continuous field read by lamplight).

## 2. Materials & rendering

- **Cloth**: coarse starch-sized cotton: weave, slubs, a faint gloss, faded edges, roll creases, a few stains. One large world canvas (e.g. 16000 × 1600 px) cached in tiles, world-anchored.
- **Painting**: flat opaque fills with faint brush direction; black outlines 2–4 px at 1080p; figure faces in profile with a large eye; horses, camels, trees and architecture as flat emblems; hierarchical scale computed from an `importance` value per figure.
- **Lamp light**: `image = paint × (ambient + lamp(x, y, t))`. Ambient 6–12 % in a cool brown; lamp a warm lobe (radius 15–30 % of frame height) plus a tight hot core, falloff `1/(1 + (d/r)²)`, flicker from 6–9 Hz value noise at 3–6 %, and a hand sway of a few px. Paint gains a faint sheen inside the lobe (sized cloth). Tonemap `1 − exp(−k·x)`.
- **The lamp itself** may be in frame: a small flame (additive, layered gradients), a brass bowl, a hand; smoke wisps rise dark.
- **Lit things live**: figures inside the pool animate subtly (a horse's leg, a raised hand, flags), outside it they are still paint. Use `litness(x)` to scale animation.
- **Scroll geometry**: ends rolled on poles (shaded cylinders with cloth texture wrapping), slight sag between poles (a gentle vertical displacement), an unroll offset per end.
- Optional **audience**: dark seated silhouettes, rim-lit by the lamp. Everything is a pure function of t under fixed seeds.

## 3. Colour logic

- **Day palette**: yellow-ochre and orange-red dominate, green and brown support, blue and pink are small accents, black outlines everything; the cloth's cream shows rarely.
- **Night is the grade**: the lamp warms and saturates what it touches; outside the pool colours drop to dim brown-blue, never pure black.
- No shading on figures; light comes only from the lamp field.
- The brightest value is the flame; then paint in the lamp core.
- Example: ochre `#d9a227`, orange-red `#c84b23`, green `#4c7a3a`, brown `#7a4a2a`, blue `#3a5f8f`, black `#1a1410`, cloth `#e6d4ac`; ambient `#2a2230`, lamp `#ffb35a`.

## 4. Type & subtitles

- Subtitles live **below the scroll in the dark**, warm cream, as if touched by the lamp's spill; no box. **Tiro Devanagari Hindi** or **Noto Serif Devanagari** for Hindi, **Cormorant Garamond** semibold for Latin (36–46 px). Hindi and Rajasthani-flavoured narration subtitles are supported.
- Titles: **Yatra One** or **Rozha One** (70–120 px), painted onto the cloth in black and red, revealed when the lamp reaches them.
- Episode labels may appear as small painted words on the cloth, lit in turn. Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps** for camera and lamp; lit figures on twos (12 fps), 2–4 drawing loops; the flame on ones.
- **The lamp moves like a hand**: eased travel (`eio`) with a small overshoot and settle, a tremor of 1–3 px, a pause on each episode while it is told.
- **Unrolling**: an end pole rolls back and cloth comes into view with a slight wave; rolling up runs it in reverse.
- Lit animation fades in and out with `litness`; nothing outside the pool moves except flame flicker on the edges.
- Never moves: the painted layout itself. The story advances only by light and camera.

## 6. Camera grammar

A cloth stretched between poles at night; the camera stands among the audience or travels along the cloth.

| Move | What it expresses | Can serve |
|---|---|---|
| Lateral track that follows the lamp | being told the story | a journey; a timeline; a process |
| Locked wide, lamp travelling across | the whole and the part at once | an overview; a map; a history |
| Push into the lit episode | the moment that matters | a decision; a witness; a detail |
| Pull back to the whole cloth and audience | the tale as an event | a community; a tradition; an ending of a chapter |
| Unrolling reveal | more to come | a list; a sequence; a long route |
| Two lamps, two pools, cut between them | parallel places | comparison; two sides; then and now |
| Low view past audience silhouettes | listening together | a shared memory; a lesson; a debate |

Framing: the scroll's horizontal band fills 50–70 % of the frame height; lamp pool and lit episode near the centre; the dark is kept, never lifted to see everything. Transitions: the lamp leaves and darkness takes the frame; the lamp is carried to the next episode; the scroll rolls. Forbidden: dissolves, digital wipes, daylight cuts mid-performance, blue night grading.

## 7. Sound palette

- **The bowed fiddle**: a ravanhatta-like voice from `erhu` pitched down slightly, nasal formant, slides and ornaments; small bells on the bow as `sleighbells` / soft `nepal_bells` following each bow stroke.
- **Voice is music**: a singer-narrator, often answered by a second voice repeating or completing lines; two TTS voices in call and response, small outdoor reverb. Never imitate a recorded epic or its melodies.
- **Rhythm**: ankle bells (`sleighbells`) when the storyteller steps; a frame drum (`frame_drum`) for arrivals.
- **Night foley**: lamp flame flutter (filtered noise), wick crackle, oil sizzle, cloth flap in wind, crickets, a distant dog, the audience's murmur and a cough.
- **Silence**: the fiddle stops; only flame and crickets.
- Voice and fiddle lead; any extra music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The lamp as cursor.** Light selects what is being told; the rest waits in the dark. *Fits content like:* a guided tour of a system; a timeline explained point by point; a dashboard walked through.
- **Everything at once.** The whole story is on screen from the start; the film is the order of reading. *Fits content like:* a project plan; a city map; a family tree.
- **Scale by importance.** Size encodes significance, not distance. *Fits content like:* who holds power; the biggest cost; the main character among many.
- **Lit things move.** Painted figures stir only in the lamp's pool. *Fits content like:* memories that wake when recalled; dormant data brought to life; a museum at night.
- **Unroll and roll.** The cloth opens at dusk and closes at dawn. *Fits content like:* a season; a long journey; a night's work.
- **Call and answer.** Two voices trade lines over the same lit episode. *Fits content like:* a dialogue; questions and answers; two witnesses.

## 9. Pitfalls of the medium

- A bright, evenly lit scroll loses the performance → keep the night; ambient ≤ 12 %.
- Panels with borders turn it into a comic → one continuous field.
- Perspective or overlapping depth → flat, scale by importance only.
- A steady, robotic lamp → hand easing, tremor, flicker, pauses.
- Animating the whole cloth → only what the lamp touches moves.
- Blue-tinted night → warm lamp against brown dark.
- **Sacred objects as decoration.** A phad is treated as a portable shrine of a deity, and its performance is a ritual: do not use deity figures or episodes as ornament, and do not stage a fake ritual. Do not present a code-made film as an authentic phad; for commercial work, credit or consult phad painters and performers.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `scroll.js`: world canvas in tiles, `cloth(seed)`, `rolls(leftOpen, rightOpen)`, `sag(x)`, the painted layout from a figure list with `importance`.
- `lamp.js`: `lamp(x, y, t)` field with flicker and sway, `litness(x, y)`, flame and smoke sprites, ambient grade, tonemap.
- `figures.js`: flat profile figures, horses, camels; 2–4 drawing loops gated by `litness`.
- `stage.js`: poles, ground, audience silhouettes with rim light, subtitles in the dark band, `render(t)`.

Start from `styles/shadow-puppet/demo/gl.js` (`makeGL`: lamp field, flicker, warm vignette, bloom), `styles/ukiyoe/demo/print.js` (`fibers`, `fillPath`, `line`), `styles/printed-long-take/demo/textures.js` (large tiled textures), `core/lib.js` (`mulberry`, `vnoise`, `eio`, `spring`), `core/render/`, `core/audio/sampler.py`, `core/audio/sfx.py`, `core/tts/tts.py`.

## 11. Variation space

You decide the story's layout on the cloth, who holds the lamp, how many voices, whether the audience is seen, the opening, the ending, the camera path and the pacing.

- Structures: **left to right** (the lamp reads in order, like a timeline); **centre outward** (the lamp starts at the great figure, then visits the episodes around it); **back and forth** (the lamp jumps between two distant episodes as the voices argue).
- Openings: **dusk unrolling**, the cloth opened in failing daylight before the lamp is lit; **a single flame** in darkness, then the first painted face; **the audience settling**, the cloth unseen until the lamp turns.
- Endings: **dawn**, daylight washes in and the magic flattens; **the lamp blown out**, one wisp of smoke; **the scroll rolled up** and carried away.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
