# Film Noir — Style Prompt

> Black-and-white crime-film lighting built in code: one hard light per shot, shadows sharper and larger than the people who cast them, wet streets that mirror the lamps, smoke that makes the beams solid, and a tired voice telling it in the past tense.
> References (grammar only): 1940s–50s Hollywood crime films (low-key light, blind shadows, voice-over, flashback); John Alton's book *Painting with Light* (1949) for light as the set; 1920s German Expressionist cinema for slanted shadows; 1940s night press photography (flash on wet pavement). Never copy a film's shots, characters, dialogue or music, and never name them in the film.

## 1. Essence, and what it is not

- **Low key, one hard source**: 30–60 % of the frame is black; light arrives in shapes (slats, a window cross, a doorway).
- **Shadows act**: cast shadows are larger than life, reach the wall before their owners, and can play a scene alone.
- **The wet night city**: rain visible only where backlit; asphalt and cobbles mirror lamps and signs.
- **Smoke and haze** that turn beams of light into solid objects.
- **Fatalistic voice-over and flashback**: the story is already over.

Not 1920s Silent Film (drawn comedy, intertitles, piano; no hard-shadow mood, no voice), not 60s Spy Title Sequence (flat coloured paper, brass stabs), not Halftone Dossier (newsprint dots; this is projected silver), not Liminal Found Footage (no camcorder), not a desaturation filter over modern colour.

## 2. Materials & rendering

- **A three.js set** of simple lit geometry: offices, stairwells, alleys, a lamp-lit street. Figures are low-detail mannequins in period silhouettes (long coat, brimmed hat, suit); a lit face is a simple sculpted head with no likeness.
- **Hard light**: one key per shot, a `SpotLight` with a 4096 shadow map, `shadow.radius` ≤ 1, penumbra 0–0.1; fill ≤ 1/8 of the key (key:fill ≥ 8:1); practicals (desk lamp, street lamp, neon) as emissive surfaces with small point lights.
- **Gobos** via `SpotLight.map`: venetian blinds (10–20 slats; tilting them changes the stripe duty cycle), a window cross, a turning ceiling fan, a banister. **Eye light**: a narrow rectangular band across the eyes, the rest of the face in black.
- **Atmosphere**: beams raymarched through the spotlight cone (16–32 steps with shadow lookups, so blinds stripe the beam) over 3D-noise density; smoke as curl-noise sheets; low street fog.
- **Wet surfaces**: a reflective ground (`Reflector` or SSR) with ripple rings from a seeded event list, roughness varying puddle to asphalt, lamp reflections stretched into vertical streaks. **Rain** streaks are as bright as the backlight behind them, so rain shows only against a lamp.
- **Monochrome film**: luminance with a panchromatic response (a yellow or red filter darkens skies), a deep-toed curve, fine 35 mm grain strongest in mid-tones (seeded per frame), slight halation, gate weave ≤ 0.3 px; the print is new, no scratches. Frame 1.37:1 Academy pillarboxed (1.85:1 for a later look).

## 3. Colour logic

- Black and white only: 5–7 working values with black as the dominant field.
- Value order: light sources > lit faces > lit walls > smoke in a beam > wet reflections > mid shadows > black. Pure white only on practicals, a shirt in a beam, rain against a lamp.
- The grey ramp may be cool (silver) or neutral; no sepia, no tints.
- No colour accents by default. A declared neo-noir variant may give one hue to one object for the whole film, never more.
- Never: flat grey frames, soft wrap light, uniform ambient.
- Example ramp: `#050505 #1a1a1a #3a3a3a #6b6b6b #a4a4a4 #d8d8d8 #f8f8f6`.

## 4. Type & subtitles

- **Main titles** in period: a tall condensed sans (Bebas Neue, Oswald 600) or an expressive serif (Playfair Display 800 italic), white, revealed by the light falling on a wall or a street rather than animated in.
- **In-world type does most of the work**: frosted-glass door lettering (reversed from inside), a headline (Playfair Display Black), a neon sign (Monoton as white tubes), a typed report (Special Elite or Courier Prime).
- **Subtitles**: white, slightly soft, no box, a 1.5–2 px dark edge, Libre Baskerville or EB Garamond 500, 34–40 px, bottom-centre inside the Academy frame; voice-over lines in italic. Devanagari: Tiro Devanagari Hindi. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps on ones, unhurried. Camera moves are dolly and crane, eased (`eio`), 3–8 s long; no handheld.
- Figures move deliberately: a pause before a turn, a head turning into the eye light.
- **Light moves**: a swinging bulb, headlights sweeping a ceiling, slats tilting, seeded neon flicker, a train's windows strobing across a wall.
- Appear: step out of the dark into a shape of light, shadow first. Disappear: step back into black, or a lamp clicked off.
- Never moves: the hardness of the key, the frame.

## 6. Camera grammar

A camera that waits in the dark and lets the light do the cutting. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Low angle, wide lens, ceiling in frame | pressure; fate looming | a confrontation; an office of power; a staircase |
| Dutch tilt (10–25°) | a world off balance | a lie; dizziness; a betrayal |
| Slow dolly in to the eye light | an inner decision | a confession; a choice; a realisation |
| Only the shadow on the wall | the act seen indirectly | an arrival; a threat; a memory |
| Overhead crane down a stairwell | a spiral; no way out | a pursuit; a descent; a search |
| Through the blinds from outside | watching; secrets | a waiting room; a late meeting; an observer |
| Reflection in a puddle or mirror | two versions | a double life; a mistake; identity |
| Long track along a wet street | the city's indifference | a walk home; a search; a sleepless night |

Framing: one figure, one shape of light; ≥ 30 % of the frame in black; silhouettes against lit doorways, windows and fog. Transitions: period dissolves, a ripple dissolve into a flashback, fade to black, a cut on a slammed door or a passing train; no wipes, no zooms, no flash frames.

## 7. Sound palette

- **Score**: a 1940s studio orchestra: tremolo strings (violins_trem) for unease, low brass (trombone, horn, tuba), a lone trumpet_mute or tenor sax for the city at night, walking contrabass_pizz and brushed snare in a club, honky_tonk piano in a bar, harp and vibraphone for memory, timpani for doom. Diegetic jazz via `sfx.radio`.
- **Foley**: rain by surface (pavement hiss, gutters, an awning, glass); footsteps on wet pavement with slapback between buildings; a match strike; a typewriter; a telephone bell; neon buzz (60 Hz with odd harmonics, crackling as it flickers); an elevated train; a distant mechanical siren.
- **Silence**: rain alone, or a clock.
- **Voice-over**: low, close, dry, deadpan, past tense, short sentences; a period chain (band-limit 90 Hz–7 kHz, mild saturation, a small dry room). Score ducked 8–10 dB under it; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Blinds.** Slat shadows across a face and a room, tilting as the slats turn. *Fits content like:* a job interview; an office at dawn; a secret being kept.
- **The shadow arrives first.** A shadow climbs the wall before its owner, or plays the scene alone. *Fits content like:* a visitor; a warning; the memory of someone gone.
- **Eye light.** A slash of light across the eyes, the rest of the face in black. *Fits content like:* a confession; a lie; a decision.
- **Wet-street mirror.** A step breaks the reflection of a sign. *Fits content like:* a city at night; a homecoming; a choice at a crossroads.
- **Smoke in the beam.** A hard beam made solid by smoke or steam. *Fits content like:* a jazz club; a projection booth; a late office.
- **Voice-over flashback.** A ripple dissolve into the past, the voice in past tense, a hard return. *Fits content like:* a confession; a company's history; how a family recipe was lost.

## 9. Pitfalls of the medium

- **Grey mush** → design light for monochrome; check each frame's histogram: ≥ 30 % below 10 % luminance.
- **Soft shadows** from wide penumbras, area lights or blurred maps → small radius, high-resolution maps; inspect shadow edges at 1080p.
- **Rain everywhere at equal brightness** → only backlit drops show.
- **Cliché stacking** (blinds, hats, sax, rain and smoke in every shot) → two or three signs per scene.
- **Period stereotypes** (the woman as villain by gender, caricatured minorities) → archetypes of light and position, written with present-day care.
- **Glamorised smoking and weapons** → for children's or brand work use coffee steam, cold breath or a vent; imply weapons through sound and shadow, never as a lingering insert.
- **CG cleanliness or a damaged print** → grain, halation and slight edge softness, but no scratches or burns (those belong to other styles).

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `set.js`: modular rooms and streets, period props, `figure(coat, hat, pose)` mannequins.
- `light.js`: `hardKey(pos, target, penumbra)`, `gobo(type, params)` (blinds `slats, duty, angle`; window cross; fan), `eyeLight(band)`, practicals, headlight sweeps.
- `atmos.js`: raymarched beams with shadow lookups, curl-noise smoke, ground fog.
- `wet.js`: reflective ground, ripple rings from a seeded event list, lamp streaks, backlit rain, glass drops.
- `bw.js`, `dissolve.js`: luminance with filter, curve, grain, halation, Academy mask; ripple dissolve.

Start from `core/three/post.js` (DOF, GTAO, bloom; swap its grade for `bw.js`), `styles/glass-product/demo/studio.js` (studio lights, mirrored floor), `styles/backrooms/demo/world.js` (fog following local light), `styles/silent-film/demo/engine/film.js` (`FilmPost` at low strength: grain and weave only), `core/audio/sfx.py` (`radio`, `step`, `rumble`), `core/audio/sampler.py`, `core/tts/tts.py`.

## 11. Variation space

You decide the city (or one room), the year (1940s–50s), the light motifs, whether there is a voice-over, the frame and the orchestra.

- Structures: **one night told backwards** (the voice at dawn; flashbacks walk back to the first light switched on); **a single room** (an office or stairwell; the whole story in how the light through one window changes); **a walk across the city** (one route, each block a different light: lamp, neon, train, doorway).
- Openings: **black, then a match struck**, one face lit; **a wet street** whose reflection breaks under the first step; **a shadow climbing the stairs** before anyone appears.
- Endings: **a lamp clicked off**; **dawn greying the blinds** until the hard light is gone; **a crane up** from the street into rain and darkness.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
