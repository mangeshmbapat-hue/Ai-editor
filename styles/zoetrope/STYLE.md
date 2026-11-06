# Zoetrope — Style Prompt

> A Victorian motion toy: a strip of sequential drawings inside a spinning slotted drum, seen through the passing slits so the figures come alive in a short endless loop, with the apparatus, the slit flicker and the parlour around it always part of the picture.
> References (grammar only): the 19th-century optical toys (phenakistiscope discs of the 1830s, the daedaleum and zoetrope drums of the 1830s–60s, the praxinoscope's mirrors of the 1870s) for loops of 8–16 phases and printed, hand-coloured strips; Eadweard Muybridge's motion studies for loops of real movement; contemporary strobe-lit sculptural zoetropes for figures on a turntable. Never copy a historical strip, disc or museum piece, and never name them in the film.

## 1. Essence, and what it is not

- **Loops.** Every animation is a cycle of a few phases (typically 12), repeating; repetition is the content.
- **The apparatus is on screen**: a lacquered drum, slits, the strip inside, a stand, a crank or a spin of the hand, the room around it.
- **Seen through slits**: moving dark bars, flicker, a figure sharp only through the gaps; figures look slightly narrower than drawn.
- **Printed strips**: engraved-style ink line on cream paper with a few hand-coloured washes; when the drum stops, the frames sit side by side.
- **Spin-up and spin-down**: stills blur into life at the right speed and fall back into a row of drawings.

Not 1920s Silent Film (projected film frames, intertitles, a picture house), not 1930s Rubber Hose Cartoon (inked cels with a band), not Copperplate Engraving (one plate building itself), not a flipbook (pages in a pad; the zoetrope is a closed circle with no end).

## 2. Materials & rendering

- **three.js drum**: an open cylinder (Ø 25–30 cm, real units) with N slits (12–13) cut by an alpha-tested texture, black or red lacquer outside with gilt lines (original ornament), the strip mapped on the inner wall below the slits, a turned wooden stand.
- **Angle law**: `θ(t)` with spin-up (`eio`), steady speed, spin-down (friction decay). **Sync rule**: at steady speed the drum turns exactly one slit pitch (360°/N) per output frame, so each frame sees the next phase in the same place. Detuning by ±δ is a deliberate move.
- **Render the illusion, do not fake it**: accumulate K sub-frame renders (16–32) across a persistence window of about one frame into a float target, the drum advancing between samples. The slits mask naturally; glimpses of the strip align into a stable figure; the outer wall blurs into a band. Bars, flicker and narrowing all emerge from the geometry.
- **Strip painter** (Canvas 2D): phases drawn as engraved line (swelling, tapering strokes with hatching) and laid over with 2–3 transparent washes that spill a little past the line; cream paper with grain; phase numbers and a printed border. The strip is printed once: it never boils.
- **Disc variant** (phenakistiscope): a flat disc with radial slits seen in a mirror, same sync rule per slit.
- **Sculptural variant**: N small figures on a turntable, each a slightly different pose, rendered with a short strobe exposure synced to one figure pitch per frame; strobe off reveals the many still figures as a blur.
- **Room**: warm parlour light (gas or lamp), a table surface, soft shadows; DOF and grade from `core/three/post.js`.

## 3. Colour logic

- **Two worlds**: the dim warm room and the drum (lacquer black or deep red, gilt) frame a bright cream strip, which is the brightest thing in the frame.
- The strip: ink line plus 2–3 washes (a red, an ochre, a blue-green) at most, laid flat and transparent.
- **One accent** reserved for the loop's hero (a red coat, a yellow bird).
- No neon, no digital gradients; light is lamp-warm.
- Example: room `#2a1f17`, lacquer `#1a1614`, gilt `#c9a457`, strip paper `#efe3c8`, ink `#2a221b`, washes `#c4553a` / `#d9a74a` / `#6f9a88`.

## 4. Type & subtitles

- **Titles are printed toy labels**: IM Fell English or Playfair Display on a cream paper band around the drum or on a strip header, framed by a printed rule; Devanagari titles in Rozha One or Tiro Devanagari Hindi on the same band.
- **Subtitles**: EB Garamond or IM Fell English 34–40 px in cream with a soft dark halo, below the drum in the dark room, no box; Devanagari in Tiro Devanagari Hindi. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output.** The loop's phase advances once per slit passage; under the sync rule that is one phase per frame (12 phases ≈ two loops per second).
- For calmer loops use more phases per cycle (16–24 strip drawings) rather than slowing the drum below sync.
- Loops must close: phase N flows into phase 1 with the same spacing as any other pair.
- The drum has weight: spin-up 1–3 s, spin-down 3–6 s with a slight eccentric wobble; the crank or hand moves on ones.
- **Appear**: a new strip is inserted while the drum is still; **disappear**: the drum slows and the loop freezes into a row of drawings.
- **Never moves**: the stand, the room, the strip's printing (no boil).

## 6. Camera grammar

A parlour camera at table height. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Eye-level through the slits | The illusion, being inside the toy | a loop of work; a dance; a heartbeat |
| Pull back to the whole drum and room | The trick revealed | a frame story; a museum; a childhood memory |
| Overhead into the drum (the strip as a ring) | The whole cycle at once | a life cycle; seasons; a process |
| Slow orbit around a stopped drum | Inspection, nostalgia | a collection; an archive; a heirloom |
| Macro on a slit edge passing | Time slicing | a deadline; a heartbeat; a clock |
| Low angle with the crank turning | The labour behind the motion | a factory; effort; a machine |

Framing: the loop's figure sits at the centre of a slit band; keep the drum's top rim and a slice of room in view to keep the toy present. Transitions: spin-down to stills, strip swap, a slit-wipe (the camera passes behind the drum wall), a lamp dimming; no crossfades or digital wipes.

## 7. Sound palette

- **Victorian parlour**: music box via `pluck('music_box', …)`, a barrel-organ colour from `organ` with `accordion` (harmonium = `accordion`), `harp`, upright `piano`, `glockenspiel`, `tubular_bells`, `violin`. Ostinatos whose phrase length matches the loop length.
- **The mechanism**: a drum whirr (filtered noise amplitude-modulated at the slit-passage rate, rising in pitch with spin-up), crank ratchet clicks, a wooden creak, the soft clack of a strip inserted, a bell when the drum stops.
- **Silence**: the drum at rest, a clock ticking in the room.
- **Voice**: a showman's patter or a quiet parlour narrator; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Spin-up to life.** A row of still drawings blurs and locks into motion as the drum reaches sync. *Fits content like:* an invention starting; a child's first steps; a city waking.
- **Strobe drift.** Detuning makes the loop crawl forward, backward or freeze. *Fits content like:* time slowing in shock; going back over a memory; a system stalling.
- **Strip swap.** The drum stops, a new strip goes in, a new loop begins. *Fits content like:* chapters of a life; shifts in a factory; seasons.
- **The ring of phases.** Overhead, every phase is visible at once around the circle. *Fits content like:* a life cycle; a production line; a daily routine.
- **Strobe off.** On a sculptural turntable the strobe stops and the animated figure becomes many still ones. *Fits content like:* one person revealed as a crowd; the frames behind a performance; repetition exposed.
- **Loop break.** A figure leaves the cycle on a phase that is not in the loop. *Fits content like:* escaping a routine; a strike; a change of habit.

## 9. Pitfalls of the medium

- A 2D loop with black bars painted over it → render the drum and slits and accumulate sub-frames so the illusion is physical.
- Unintended wagon-wheel crawl → obey the sync rule; detune only as a move.
- Loops that pop at the wrap → design cycles so phase N → 1 has normal spacing; test the strip flat.
- Photosensitive flicker → no full-frame flashes; slit bands keep average brightness steady; strobe on/off changes are eased over ≥ 0.5 s.
- Boiling strip art → the strip is printed once; only the apparatus moves.
- Copying a historical strip → draw original phases; real motion may come from the film's own renders.
- Figures squeezed thin by the slits → draw phases 1.2–1.4× wider or accept the narrowing as part of the look.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `drum.js`: three.js drum, slit texture, strip texture on the inner wall, stand and crank; `angle(t, {N, spinUp, steady, detune})`.
- `shutter.js`: sub-frame accumulation into a float target (`accumulate(renderFn, t, K, window)`), plus the strobe exposure for the sculptural variant.
- `strip.js`: phase painter with engraved line and washes; start from the burin line in `styles/engraving/demo/engine/burin.js` and the wash in `styles/watercolor/demo/engine.js`.
- `parlour.js`: room, table, lamp and HDRI after `styles/brick-toy/demo/set.js`; DOF, bloom and grade from `core/three/post.js`.
- `mix.py`: whirr modulated at the slit rate and mechanism foley via `core/audio/sfx.py`, music via `core/audio/pluck.py` / `core/audio/sampler.py`, voice via `core/tts/tts.py`.
Easing and seeds from `core/lib.js` (`eio`, `ei`, `mulberry`); render with `core/render/video.mjs`, `srt.py`, `mux.sh`.

## 11. Variation space

You decide the device (drum, disc, sculptural turntable), the loops and how many phases each has, the strip palette, how often the drum stops, the opening and the ending.

- Structures: **a cabinet of loops** (strip after strip, each a short idea, linked by spin-downs); **one loop that changes** (the same cycle redrawn on new strips until it becomes something else); **a turntable reveal** (an animated scene that is shown, mid-film, to be dozens of still figures).
- Openings: **a still strip** laid flat on the table, frames side by side; **a hand spinning the drum** in silence until the figure locks in; **an overhead ring** of phases that the camera descends into.
- Endings: **spin-down** to a row of drawings; **the lamp turned down** while the loop keeps running in the dark; **one figure steps out** of the loop and the drum spins empty.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
