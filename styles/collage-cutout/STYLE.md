# Cut-paper Collage — Style Prompt

> A tabletop of printed scraps (magazine-like cuttings, torn newsprint, kraft paper, tape, staples, handwriting) animated as cut-outs a frame at a time: mismatched materials and scales meet in one picture, and every edge shows how it was cut or torn.
> References (grammar only): Dada photomontage and Merz collage of the 1910s–20s (clashing sources, cut type, scale mismatch); mid-century cut-out collage animation for jointed paper figures moved under a rostrum camera; DIY zine and scrapbook culture for tape, staples and photocopy grain. Never reuse real magazine pages, photographs, logos or artworks, and never name the references in the film.

## 1. Essence, and what it is not

- **Many materials in one frame.** Each scrap has its own print process (halftone photo, flat offset colour, newsprint, kraft, tracing paper, coloured card) and its own edge.
- **Edges tell the making.** Scissor cuts are straight runs with small angle errors; torn edges show a white fibrous core where the print layer tore beyond the paper.
- **Visible craft**: tape strips, staples, pins, pencil marks, glue sheen, a shadow under every piece.
- **Clash is the meaning**: a head from one source on a body from another, a diagram hand holding a photo cup, a tiny figure on a giant ticket.
- **Cut-out animation**: rigid flats moved on twos or threes with a slight hand jitter; shape changes by replacement.

Not Red Paper-cut (one red paper, folk cutting patterns), not 60s Spy Title Sequence (four flat screen-print colours, clean graphic geometry), not Halftone Dossier (one printed sheet with stamps and a case-file frame), not Paper Pop-up Book (three-dimensional folds on a book in a room).

## 2. Materials & rendering

- **Scrap builder** (Canvas 2D, cached as sprites): an image source + a print process + a cut. Processes: `halftone` (dots at a screen angle with paper show-through), `offset` (flat ink with slight misregistration), `newsprint` (grey-yellowed paper, coarse dots, faint show-through of a reversed page behind), `photocopy` (high contrast, toner speckle), `card` (flat colour with fibre).
- **Image sources must be original**: procedural pictures, the film's own three.js renders printed through the halftone process, generated pseudo-text columns, or rights-cleared material recorded in the project. No real publications, brands, logos or photos of real people.
- **Cuts**: `scissor(poly, err)` straight segments with ±1–2° angle error and tiny overcuts at corners; `tear(poly, seed)` fractal-noise edge plus a 2–6 px white fibre band on the torn side (paper-white outer polygon with fibre noise, print inner polygon offset inward).
- **Table**: one ground (kraft board, cork, cutting mat or a big newsprint sheet) lit by one overhead lamp; each scrap casts a soft drop shadow offset by its layer height, always in one direction; a slight curl gradient across large scraps.
- **Tape**: semi-transparent matte strips with creases, dust and zig-zag torn ends; staples as two metal dots with a shadow; pencil marks and handwriting as graphite strokes.
- **Rigs**: jointed cut-outs with paper pivots (brads) at joints; mouths and eyes as replacement scraps from different sources.
- Halftone and grain belong to the scrap (world-anchored), cached at the scrap's resolution; all placement jitter seeded per drawing.

## 3. Colour logic

- **One paper neutral rules the ground** (kraft, newsprint grey-yellow, or cream); scraps sit on it.
- 2–3 strong print colours across the frame plus black; each source may carry its own palette but the frame obeys the limit.
- **One accent** reserved for meaning: a fluorescent sticker, a red marker circle, a highlighter stroke.
- Value: the hero scrap contrasts with the ground; background scraps are lighter or greyer.
- Everything looks printed: dots, misregistration, yellowing. No raw digital gradients, no glow.
- Example: kraft `#c8a77a`, newsprint `#e7e0cc`, ink `#1d1b19`, print red `#d0402f`, print blue `#2f5f9a`, accent fluorescent `#ff4fa3`.

## 4. Type & subtitles

- **Headlines are ransom lettering**: each letter cut from a different "source", built from OFL faces (Bebas Neue, Anton, Playfair Display, Special Elite, Rubik Mono One, Oswald) printed through different processes and slightly rotated. Devanagari headlines: letters from Rozha One, Yatra One and Mukta mixed. Only for short words.
- **Subtitles** are typed on a paper strip taped across the bottom: Special Elite or IBM Plex Mono 32–38 px, ink on off-white strip; Devanagari: Mukta or Hind on the same strip. Two lines max; the strip slaps on and peels off.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output, pieces on twos**, threes for a rougher handmade feel; the camera moves on twos too.
- Every drawing re-places each moving piece with seeded jitter (0.5–1.5 px, ±0.3°); held pieces do not jitter.
- **Arrivals** slap down (a few frames large and with a wide shadow, then flat), slide in from the frame edge, or are taped on. **Exits** are peeled off, torn away, or swept off by a hand-shaped scrap.
- Shape changes by replacement, never by morphing; speech by swapping mouth scraps.
- Paper flutter only for loose pieces in wind: a 2–3 drawing flap.
- **Never moves**: the ground and the lamp.

## 6. Camera grammar

A rostrum camera over a table. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked top-down board | The page being made | a manifesto; a list; a news week |
| Truck along a long collage strip | A sequence, a timeline | a commute; a history; a supply chain |
| Push into a halftone dot until it is a world | Scale break, going deeper | a statistic becoming a person; a planet; a memory in a photo |
| Pull back to reveal a larger collage | Context, irony | a face made of headlines; a city made of tickets |
| Jump cut on the beat between boards | Energy, argument | a montage; a rant; a playlist |
| Low tilted view across stacked scraps | Depth and mess | a desk at midnight; an archive; a crime wall |

Framing: one hero scrap per beat, layered clutter around the edges, a strip of calmer ground where subtitles go. Transitions: a new sheet slapped over, a scrap torn away to reveal the next board, a hand-sweep, tape pulled, a cut on a beat; no crossfades.

## 7. Sound palette

- **Collage music**: short loops and found-sound gestures: `drum_kit`, `upright` piano or `honky_tonk`, `upright_bass_pizz` (pluck), `ukulele`, `glockenspiel`, `trumpet_mute`, `claps`, `kalimba`, a music box; a synthesised vinyl scratch (pitch-swept filtered noise) and tape-stop effects for cuts.
- **Foley of paper**: scissors snip, paper tear (long, crackling, filtered noise with sparse clicks), tape pulled off the roll and slapped, stapler clunk, glue stick squeak, crumple, a slap of a scrap landing (`sfx.thump` high-passed).
- **Silence**: a full stop where only a scrap's flutter is heard.
- **Voice**: lines may be cut up and re-ordered like the pictures; a dry, ironic narrator or several voices; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Tear reveal.** A scrap is ripped away and the board underneath shows the next idea. *Fits content like:* a promise and its fine print; a renovated street; a before and after.
- **Head swap.** A body part is replaced with a scrap from another source. *Fits content like:* a job that changes a person; an identity question; a bureaucrat becoming a machine.
- **Dot zoom.** The camera enters a halftone dot that opens into a new board. *Fits content like:* one person in a crowd statistic; a pixel in a news photo; a seed in a field.
- **Ransom headline.** A sentence assembles letter by letter from clashing sources. *Fits content like:* a protest slogan; a deadline; a recipe title.
- **Tape-down.** A piece slaps down and a strip of tape fixes it. *Fits content like:* a decision made; a fact pinned; an appointment.
- **Scale clash.** A giant cut-out hand or object enters a tiny world. *Fits content like:* a market force; a parent; a new technology.

## 9. Pitfalls of the medium

- Copyright: real magazine pages, logos, celebrity faces → generate every source or use the film's own renders and rights-cleared material; label synthetic sources.
- Clean vector look → torn edges with white fibre cores, scissor angle errors, shadows, tape.
- Visual noise → 3–5 sources per frame and one hero scrap.
- Smooth tweened motion → twos or threes with seeded placement jitter.
- Halftone moiré when scaling → render dots at scrap resolution, keep dot pitch ≥ 3 px on screen, let it fall to flat tone when smaller.
- Unreadable subtitles over clutter → the taped paper strip, always.
- Shadows in different directions → one lamp, one shadow direction.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `scrap.js`: `print(img, process)`, `scissor(poly, err)`, `tear(poly, seed, core)`, sprite cache; start from rough edges, pieces and paper shadows in `styles/spy-titles/demo/paper.js` and grain/alpha handling in `styles/papercut-red/demo/paper.js`.
- `halftone.js`: process passes for own images; adapt the halftone plates of `styles/risograph/demo/riso.js`; paper textures after `styles/printed-long-take/demo/textures.js`.
- `rig.js`: jointed cut-outs and replacement mouths; start from `styles/papercut-red/demo/rig.js`.
- `table.js`: ground, lamp shadows, tape, staples, slap and peel timings (`slap(t0)`, `peel(t0, dir)`).
- `ransom.js`: mixed-source letters for headlines.
- `mix.py`: paper foley via `core/audio/sfx.py`, music via `core/audio/sampler.py` / `core/audio/pluck.py`, voice via `core/tts/tts.py`.
Seeds and easing from `core/lib.js`; render with `core/render/video.mjs`, `srt.py`, `mux.sh`.

## 11. Variation space

You decide the subject, the ground, which print processes appear, the accent, the stepping, whether the voice is cut up, the opening and the ending.

- Structures: **a week in boards** (one board per day, each torn away to reveal the next); **an argument** (two collages answer each other, cut on the beat); **one long strip** (a single truck across a collage that is history, route or process).
- Openings: **an empty board** and scissors' snip before the first scrap lands; **a dense finished collage** that we enter through one dot; **a ransom headline** assembling over silence.
- Endings: **everything swept off** to bare ground; **the final board photographed and pinned** to a wall of other boards; **one scrap left**, taped down, the rest gone.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
