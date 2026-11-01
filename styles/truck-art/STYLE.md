# Indian Truck Art — Style Prompt

> The painted goods truck of Indian highways as a moving canvas: enamel panels crowded with folk motifs, slogans and borders, reflective tape and chrome that flare in headlights, tassels and chains swinging with every pothole.
> References (grammar only): the truck-painting workshops of North and West Indian highway towns (Punjab, Haryana, Rajasthan and beyond) for panel layout, sign-painter lettering and the stock tailgate phrases; the wider South Asian truck-decoration tradition for density and ornament. Never copy a vehicle maker's badge, a brand, a particular painter's panel or a real registration, and never name them in the film.

## 1. Essence, and what it is not

- **The truck is the frame**: tailgate, side boards, mud flaps and the crown above the cab are bordered panels, each holding one picture or one slogan.
- **Sign-painter enamel**: flat, glossy, saturated colour; pinstripe borders, dot rows, scallops; lettering with block shadows.
- **Stock motifs and phrases**: lotus, parrots, peacocks, fish, a pair of eyes, a mountain lake; the "HORN OK PLEASE" / "USE DIPPER AT NIGHT" tailgate grammar; a protective charm (a black face, lemon and chillies) hung for luck.
- **Night light**: reflective tape and chrome come alive only when a headlight sweeps them.
- **It moves**: tassels, chains, bells and mud flaps answer every bump.

Not Silkscreen Poster (enamel is brushed and glossy, and the panels ride on a vehicle in space), not Memphis Diorama (folk emblems and hand lettering, weathered by the road, not designer geometry), not the sibling draft Bollywood Hand-painted Poster (no modelled faces or collage; truck art is emblem, border and repetition).

## 2. Materials & rendering

- **Truck** in three.js: a low-detail body (cargo box, cab, crown, bumpers, mud flaps), each surface UV-mapped into a 4K panel atlas painted in Canvas 2D at init; a panel that paints itself re-uploads only its dirty rectangle.
- **Enamel**: `MeshPhysicalMaterial`, roughness 0.2–0.35, clearcoat, a faint orange-peel normal noise; brush marks as slight roughness variation.
- **Panel painter**: borders (pinstripes 2–4 px, dot rows, scallops) → flat fills → motifs (Bézier shapes, flat colour, one darker tone or stripes for shading, black or white outline) → lettering (face, block shadow, highlight).
- **Reflective tape**: separate strips (red/white, yellow) with a retroreflective term `base + k·max(0, dot(V, L))^n`, n ≈ 30–80, plus per-cell sparkle from `hash`; dull in daylight.
- **Chrome and mirror-work**: env-mapped from a simple procedural street; small mirror discs with jittered normals for glints.
- **Hanging things**: tassels and chains as 6–10-segment spring chains, mud flaps as hinged plates, bells ringing on impulses; pre-simulated at 240 Hz from a seeded bump profile into a frame cache, so `render(t)` stays pure.
- **Weathering** in UV masks: dust from below, mud splatter, sun-fade, chipped edges, rust runs.
- **Flat mode**: a tailgate dead-on in Canvas 2D, same panel painter.

## 3. Colour logic

- **6–10 saturated enamels at once is native**; order comes from borders: every colour field is separated by a contrasting pinstripe (white, black or yellow).
- **The body colour** (deep red, mustard, sky blue or green) is the truck's neutral.
- **Black and white are structural** (outlines, letter shadows); greys appear only in dust and chrome.
- **Tape red/white is reserved for night light**; don't use that red for decoration next to it.
- **Motifs keep conventional colours** (green parrots, blue peacock necks, pink lotus) so they read at distance.
- Example (tailgate): body `#d81f26`, panel `#ffd400`, borders `#1a7f3c` + `#ffffff` pinstripe, motif blue `#1f4fbf`, pink `#f2559a`, lettering `#111111` with `#ffffff` shadow.
- Example (dusk): body `#f2b705`, panels `#0f6e8c`, `#e4572e`, `#3c9d4e`.

## 4. Type & subtitles

- **Lettering is sign-painting**: Devanagari skeletons from Yatra One or Rozha One (Kalam for casual lines), Latin from Bungee, Righteous or Oswald, Gurmukhi from Baloo Paaji 2; only text checked by a reader. One face colour, a block shadow down-right in a darker contrasting colour, a thin highlight; baseline jitter ±2 %, per-letter tilt ±1.5°.
- Stock phrases ("HORN OK PLEASE", "USE DIPPER AT NIGHT") are generic; never brand names.
- **Subtitles** on a painted strip in the lower third: body-colour band with a pinstripe border, Baloo 2 or Mukta Bold 34–44 px (Hindi in Baloo 2 or Hind), yellow or white with a dark block shadow; screen-space but styled as a panel. Hold ≥ max(1.8 s, speech + 0.6 s).
- Per-letter reveals split by grapheme cluster so matras stay attached.

## 5. Motion quality

- **24 fps**, camera on ones. The truck always lives: suspension bob (1–3 Hz roll from road noise plus bump impulses), idle shudder of a fraction of a pixel when parked; tassels and chains lag and settle.
- **Panels paint themselves on twos**: the pinstripe runs around the panel like a racing line, then fill, motif, lettering, shadow.
- **Motifs live inside their borders**: a parrot flaps in 2–3 drawings, painted eyes blink; flat, limited animation.
- **Headlight sweeps**: tape flares within 3–5 frames and decays.
- Never moving: lettering and borders on a panel once painted.

## 6. Camera grammar

The camera rides the highway and leans in to read. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Tail-chase on the highway | following someone's life | a journey; a delay; a slogan read |
| Locked tailgate, panels animating | reading a page | a list; a message; a family motto |
| Slow orbit round a parked truck | the truck as portrait | a worker's pride; a profile; an inventory |
| Macro on brush lettering | craft | a making-of; a signature; wear |
| Headlight sweep at night | sudden attention | a warning; a memory flash; a reveal |
| Overtake along the side boards | moving past a story | time passing; rivalry; farewell |
| Top-down convoy | a system | logistics; migration; a trade route |
| Low angle under the mud flaps | the road's view | danger; humour; a child's view |

Framing: text panels read head-on or ≤ 30° off-axis; motion blur on the road, never on a panel being read. Transitions: a passing truck wipes the frame with its side board; a dust cloud; a headlight flare to white; the tailgate drops open like a door. Forbidden: generic crossfades, digital glitch.

## 7. Sound palette

- **The road as instrument**: diesel engine (synthesised: low fundamental 25–40 Hz with harmonics, combustion pulses, noise, pitch following an rpm curve), gear changes, air-brake hiss, tyre roar, pothole thumps, chain jingle (`sleighbells`, `triangle`), bumper bells (`nepal_bells`).
- **Musical air horns**: 3–5-note horn phrases (detuned sawtooth or square through a 400–1200 Hz band-pass with a pitch scoop); a horn phrase can be the film's motif.
- **Music**: dhol recipe with a stick crack (`snare2` rim, `claves`), a one-string pluck for tumbi (`pluck('shamisen')`, high, short), harmonium (`accordion`), dholak, chimta jingles (`tambourine` + `claves`); a cab radio playing an original tune through `sfx.radio`.
- **Ambience**: a roadside eatery, night crickets, rain on a tarpaulin.
- **Silence**: engine off; cooling metal ticks and crickets.
- **Voice**: a driver's warm conversational voice or a roadside narrator; music ducked ~8 dB, engine bed ~20 dB under voice; −14 LUFS.

## 8. Native moves

- **Tailgate as a page.** Each panel animates in turn. *Fits content like:* the rules of a game; a family's motto; a menu.
- **Headlight reveal.** At night only tape and chrome flare as light sweeps, revealing hidden shapes. *Fits content like:* a road-safety warning; a ghost story; a hidden route.
- **Border run.** A pinstripe races around a panel and closes on a new motif. *Fits content like:* a timeline; a race result; a delivery loop.
- **The motif leaves its panel.** A painted parrot flies to the next truck. *Fits content like:* a message passed on; gossip; migration.
- **Convoy of tailgates.** Each passing truck carries the next idea. *Fits content like:* a list of tips; regions of a country; a series of portraits.
- **Road wear.** Fresh paint gathers dust, chips and fade over a journey, then is repainted. *Fits content like:* years of work; a business's history; restoration.

## 9. Pitfalls of the medium

- Brand badges, maker names, real registrations → generic body, a blank or clearly fictional plate.
- Everything equally loud → one hero motif per panel, text panels separate, borders between all fields.
- Clean vector look → enamel gloss, orange peel, brush irregularity, weathering.
- Tape glowing in daylight → retroreflection only when view and light align.
- Tassels and chains popping → fixed-step pre-simulation, damping, clamped segment stretch.
- Text unreadable at an angle → read panels head-on; check Devanagari and Gurmukhi shaping.
- **Devotional and protective motifs**: for many drivers, deity images, religious symbols, scripture and evil-eye charms are faith, not decoration. Don't scatter them or make jokes of them; keep secular motifs unless the content is about that faith and reviewed by its people. Don't present the film as real painted trucks; credit truck painters, and commission or consult them for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `truck.js`: body meshes, UV atlas, materials, suspension from a seeded road profile.
- `panel.js`: `paintPanel(ctx, spec, p)` (borders, fills, motifs, lettering, shadow), dirty-rect upload.
- `motifs.js`: parrot, peacock, lotus, fish, eyes, mountain lake, flower rows.
- `tape.js`: retroreflective and mirror-glint shaders. `hang.js`: tassels, chains, flaps; `presim(bumps, hz=240)`.
- `road.js`, `mix.py` (diesel, air horns).

Start from: `styles/brick-toy/demo/set.js` (`buildSet`: three.js set and lights); `core/three/post.js` (`makePost`: bloom for tape and chrome, grade, DOF); `styles/paper-popup/demo/cutmesh.js` (`thread`, `particles` for chains and dust); `styles/silkscreen-poster/demo/engine/silk.js` (`polyPath`, `ringPath`, `rectPath` for borders); `styles/art-deco/demo/engine/deco.js` (`sparkle`, `glow`, `beam`); `core/lib.js` (`hash`, `spring`); `core/audio/sfx.py` (`rumble`, `creak`, `thump`, `radio`), `core/audio/sampler.py`.

## 11. Variation space

You decide the route, the truck (or trucks), what the panels say, day or night, the opening, the ending and the camera.

- Structures: **one truck, one journey** (loading to unloading, panels changing with mood); **a convoy** (each truck a chapter); **the paint shop** (a bare truck painted panel by panel).
- Openings: **a mud flap** splashing through a puddle; **a blank steel tailgate** taking its first pinstripe; **a night highway** where only tape glows.
- Endings: **the truck drives into dust**, tail lights fading; **parked at dawn**, engine ticking; **the tailgate drops** to reveal the cargo.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
