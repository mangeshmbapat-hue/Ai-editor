# 70s Grindhouse — Style Prompt

> A worn 1970s colour release print run through a tired projector at a double-feature house: faded, scratched and spliced, cut with crash zooms, split screens and freeze frames, and sometimes missing a reel.
> References (grammar only): 1970s exploitation and drive-in cinema (garish titles, trailer hype, crash zooms, freeze-frame introductions); late-60s and 70s split-screen films; projectionist practice (cue marks, reel changes, splices, burn-through); a 2007 double-feature revival that faked worn prints; 1970s funk and soul scores. Never copy a film's titles, characters, logos, theatre idents or music, and never name them in the film.

## 1. Essence, and what it is not

- **The print is a character**: dye fade toward magenta-red, lifted brown blacks, scratches, dirt, hairs, splices and frame-line slips that change reel by reel.
- **The decade's edit grammar**: crash zooms, split screens, freeze frames with name titles, slow motion, whip pans, jump cuts.
- **Garish production colour** under the fade: orange, mustard, avocado, brown, blood-red titles.
- **The show around the film**: cue marks, a "reel missing" card, a burn-through, the projector heard.
- **Loud, cheap and sincere**: hype narration, funk or library music.

Not 1920s Silent Film or 1930s Rubber Hose Cartoon (silver damage in black and white; here colour dyes), not 1920s Newsreel (no news or announcer), not Liminal Found Footage (tape, not film), not Live Countdown Split-screen (a modern clock-driven split; here optical mattes on a fading print), not a uniform "vintage filter".

## 2. Materials & rendering

- **Source picture** (three.js or Canvas 2D) shot like the 70s: soft zoom-lens corners, focus breathing, hexagonal flares; hot overexposed daylight, warm tungsten interiors. Places and figures are stylised and original; no real people.
- **Print pipeline** (WebGL pass chain; every parameter read from a `reels` table):
  1. *Dye fade*: cyan dye fails first, so reds take over; per-reel matrix and curves, blacks lifted to brown-maroon, greens and blues muted.
  2. *Grain and halation*: dye-cloud grain from three seeded per-channel noise fields, strongest in mid-tones; a red-orange glow round highlights.
  3. *Gate*: weave (±1–2 px), flicker (±3–6 %), an occasional frame-line slip (the picture rides up, showing the frame line for 2–12 frames, then snaps back).
  4. *Damage* (2D overlay from a seeded event list): long vertical scratches that **persist across frames** with slow drift (`x0 + A·vnoise(0.3t)`), dark on the base side, green, cyan or white where they cut the dye layers; print dirt dark, negative dirt white; a hair at the gate edge; splices (tape edge, jump, audio pop); missing frames (2–12 dropped).
  5. *Cue marks*: a circle top-right for 4 frames, twice (about 8 s and 1 s before a reel's end).
  6. *Burn-through*: the frame freezes; a blister (noisy radial edge, bubbling brown-orange rim, projector-white centre) fills it in 1–2 s, then white, then black.
- **Optical effects** as an optical printer made them: split screens with soft or hard mattes (2–4 panels, 0.5–1 px misregistration), freeze frames (a dupe: more contrast, frozen grain under live grain), overcranked slow motion, superimposed titles.
- Frame 1.85:1 or 2.39:1 letterboxed in 1920×1080. Seeds from the frame index; the reel table and damage events are baked.

## 3. Colour logic

- **Production palette first**: 4–6 period hues (orange, mustard, avocado, brown, teal, red), warm skin; then the fade pulls everything toward magenta-red. Each reel has its own fade, so a cut across reels jumps.
- Blacks are never pure (brown-maroon); whites are creamy. Title red and yellow are the accents, chosen to survive the fade.
- Damage has colour rules: emulsion scratches green or cyan, base scratches dark, negative dirt white.
- Never: a modern teal-and-orange grade, crushed digital black, neon.
- Example production: `#d9572a` orange, `#d7a93a` mustard, `#6b7a33` avocado, `#5a3a24` brown, `#2f6f73` teal, title red `#d8261b`.
- Example faded print: shadows `#2a1410`, mids `#a4574c`, highlights `#f4d9b8`.

## 4. Type & subtitles

- **Titles** are big and heavy, outlined, with a hard offset shadow in a second colour: Anton, Alfa Slab One, Righteous or Bungee, 140–300 px; they slam in on a crash zoom or sit on a freeze. Name titles in caps with a descriptor below (Oswald 500, 40–56 px).
- **Theatre cards** ("Feature presentation", "Reel missing"): plain, Righteous or Bungee on flat colour, with their own damage.
- **Subtitles are burned into the print**: Oswald 500 or Inter 700, 36–44 px, white or pale yellow with a 2 px dark edge, slightly soft; they weave, flicker and fade with the picture. Devanagari: Hind 600 or Mukta 700, same treatment. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps on ones; dirt and flicker per frame; scratches per track.
- **Crash zoom**: 6–10 frames, hard ease-in, 2–4 % overshoot, a focus hunt, radial blur while moving.
- **Whip pan**: 4–8 frames of directional blur, the cut hidden inside it.
- **Slow motion**: 2–4×, the music dropping out or holding one chord.
- **Freeze frame**: 1.5–3 s with a title.
- Never moves: the letterbox.

## 6. Camera grammar

A camera that pushes, snaps and splits. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Crash zoom | sudden attention | a realisation; an entrance; a punchline |
| Split screen, 2–4 panels | simultaneity | a phone call; a race; two kitchens at rush hour |
| Freeze frame with a name title | an introduction; a roster | a team; a product line-up; a cast of ingredients |
| Slow motion | the moment stretched | a leap; a fall; a toast |
| Whip pan | speed; connection | a chase; a reaction; a hand-off |
| Extreme close-up on eyes | a stare-down | a duel; a dare; a decision |
| Low wide angle from the ground | swagger | a hero walk; a car; a big arrival |

Framing: bold, centred subjects; split panels share eye lines and horizons. Transitions: hard cut, splice jump, freeze, reel change (cue marks, then a different fade), burn-through, a "reel missing" card, split panels sliding; no digital wipes, no soft modern dissolves (a cheap optical dissolve with a density bump is allowed).

## 7. Sound palette

- **Score**: funk and soul: jazz_bass with slides, electric_guitar through a wah (a resonant band-pass swept by envelope or LFO in numpy), muted guitar scratches, a tight drum_kit break, congas, cowbell, unison horn stabs (trumpet, trombone, tenor_sax), organ with rotary tremolo, string stabs. Or library suspense: fuzz bass, timpani, violins_trem, a saw synth through a sweeping resonant low-pass.
- **Foley, exaggerated**: punches (`sfx.thump` + `whoosh`), tyre squeals (filtered noise sweeps), a whoosh on every crash zoom, a stinger on freeze frames.
- **Print and projector**: optical-track character (100 Hz–7 kHz, saturation, wow), crackle and hiss, a pop at every splice, sound jumping where frames are missing, projector clatter at reel changes and as the only sound inside a silence; a burn-through ends with the sound slowing and dying.
- **Voice**: a trailer-hype narrator (deep, compressed, short lines) or dubbed dialogue (loose sync is a declared choice, never a default). Music ducked 6–8 dB; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Crash zoom.** A snap into a face or an object, with a whoosh. *Fits content like:* a chef spotting the burnt pan; a referee's whistle; a sales figure doubling.
- **Split-screen montage.** Panels slide in to show parallel action. *Fits content like:* a wedding prepared in four rooms; two delivery bikes racing; a plan carried out by a crew.
- **Freeze-frame roster.** Each member freezes mid-action under a slammed name. *Fits content like:* a team introduction; the stalls of a food festival; a band's line-up.
- **Reel missing.** A plain card, then the story resumes much later. *Fits content like:* skipping the paperwork; a comic cover-up; a jump of years.
- **Burn-through.** The film melts in the gate at the peak. *Fits content like:* a dish too spicy; a climax; a twist that "breaks" the film.
- **Reel change.** Cue marks, then a print with a different fade. *Fits content like:* a new chapter; a flashback; a change of town.

## 9. Pitfalls of the medium

- **Uniform damage** → tie it to reels and events: worst at reel heads and tails, splices on cuts.
- **Scratches that jump every frame** → persistent tracks with slow drift.
- **Unreadable picture** → heavy damage on ≤ 20 % of screen time; story beats and subtitles on cleaner frames.
- **Exploitation content** → keep the grammar, drop the exploitation: no gratuitous gore, sexualisation or caricature; violence as cartoon impact.
- **A crash zoom that is only scaling** → focus breathing, radial blur, overshoot and a little operator drift.
- **Clean split screens** → soft mattes, misregistration, density bumps at matte edges.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `reels.js`: reel table `{start, fade, damage, seed}`, cue-mark timing, changeovers.
- `print.js`: dye fade, dye-cloud grain, halation, weave, flicker, frame-line slip (WebGL).
- `damage.js`: scratch tracks, dirt events, hairs, splices, missing frames, burn-through blister.
- `optical.js`: crash zoom (scale + radial blur + focus breathing + overshoot), whip pans, split mattes, freeze frames with dupe grain, superimposed titles.
- `titles.js`, `mix.py`: slam titles, theatre cards; optical-track chain, splice pops, clatter, wah.

Start from `styles/rubber-hose/demo/film.js` (gate, weave, scratches, dust: move from silver to dye colours), `styles/silent-film/demo/engine/film.js` (`FilmPost` ageing with burn; `damage()` for splices and hairs), `styles/cel-anime-80s/demo/post.js` (halation), `core/three/post.js` (DOF for focus breathing), `core/render/events.mjs`, `core/audio/sfx.py`, `core/audio/sampler.py`.

## 11. Variation space

You decide the genre played with (or none), the reels and their fades, the damage level, the optical tricks and the score.

- Structures: **a double feature in miniature** (two short features with a trailer between, each on its own print); **a trailer for a film that does not exist** (hype narration and slammed titles, no plot); **one feature with a missing reel** (the gap is the joke or the mystery).
- Openings: **a theatre card** under crackle; **a head leader counting down** to the first frame; **a freeze frame** of the hero mid-leap with the title slammed on.
- Endings: **burn-through** to white; **the tail flapping on the take-up reel**, white light and clatter; **a reel change into nothing**: cue marks, then black.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
