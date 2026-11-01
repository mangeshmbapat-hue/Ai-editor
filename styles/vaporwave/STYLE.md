# Vaporwave — Style Prompt

> A slowed-down, pastel collage of consumer nostalgia: marble busts, columns and palms float in a pink-and-teal void over an endless checkerboard, framed by invented retro desktop windows and full-width text, softened by videotape.
> References (grammar only): early-2010s internet collage and album-cover art built from found consumer imagery; 1990s 3D clip-art, screen savers and early real-time 3D (flat shading, environment-mapped chrome, low polygon counts); shopping-mall atriums, corporate lobbies and muzak culture; classical sculpture casts as found objects. Never copy a real operating system's windows, icons, sounds or fonts, a brand, a logo or a specific album cover, and never name them in the film.

## 1. Essence, and what it is not

- **A pastel void**: a pink → lavender → teal gradient sky or a soft sunset, over a checkerboard or grid plane receding to the horizon.
- **Found icons floating**: a classical bust, a Doric column, a palm, a low-poly dolphin, a mirror sphere, plastic fruit, a generic telephone; each rendered as early real-time 3D (flat shading, vertex colours, chrome).
- **Invented retro windows** frame the scenes: bevelled panels, gradient title bars, dialog boxes, pixel cursors, all designed from scratch.
- **Full-width Latin and katakana** as ornament (Ｗ Ｉ Ｄ Ｅ spacing), short and correct.
- **Everything slowed**: drifting, slow rotation, music pitched down; videotape softness. The mood is ironic melancholy.

Not Synthwave (night neon, energy, chrome type and a driving grid; vaporwave is pastel, slow and wistful), not Memphis Diorama (a lived place; Memphis patterns appear here only as quoted wallpaper), not Liminal Found Footage (no dread, no camcorder), not Desktop Flythrough (no paper cards on a desk), not Living Screencast (no real software).

## 2. Materials & rendering

- **Void** (three.js): a screen-space sky gradient (top pink to horizon teal, or the reverse), an optional sun disc, a checker or grid floor shader with distance fog into the horizon colour.
- **Icons**: low-poly meshes (≤ 600 triangles) built in code (lathe columns, extruded palms, a bust from primitives or a CC0 scan reduced and credited), `flatShading: true`, Lambert or vertex colours; chrome via an equirectangular env map baked from the void itself. Optional vertex snapping to a 320×240 grid for wobble.
- **Marble**: a procedural vein texture (warped noise bands) in off-white and lavender grey, triplanar mapped.
- **Windows** (Canvas 2D, screen space): drawn at half resolution and scaled ×2 with nearest filtering; 2 px bevels (light top-left, dark bottom-right), a pastel gradient title bar, square buttons with simple invented glyphs, scrollbars, a 1 px drop shadow. Content inside is a render target of a 3D scene or an image.
- **Stickers**: sparkle stars, price tags, unmarked discs.
- **Composite order**: void → floor → icons → windows → stickers → videotape pass (`core/post/crt.js`, low scanlines, gentle chroma bleed, faint tracking noise) → subtitles on top, clean.
- **Determinism**: rotations and drifts are functions of `t`; window positions are keyframed; tape noise seeded by frame number.

## 3. Colour logic

- **A pastel trio dominates**: pink, cyan-teal, lavender; plus marble off-white. Everything light and slightly desaturated.
- **The neutral is marble white**, with lavender-grey shadows; black only for window shadows and text.
- **One accent**: hot magenta or "sale" yellow reserved for text and stickers, never on 3D objects.
- Values stay high; the darkest mass is a deep violet horizon or window shadow.
- Never earth tones, grunge or night neon.
- Example: `#ff71ce` pink, `#01cdfe` cyan, `#b967ff` lavender, `#fffb96` pale yellow, `#f4f1ee` marble; dusk variant `#f6c6d8`, `#9fd8df`, `#c3b1e1`, horizon `#3b2a5e`, accent `#ff3fa4`.

## 4. Type & subtitles

- **Titles**: Tinos italic (a free Times-metric serif) or Noto Sans JP for full-width Latin (U+FF01–FF5E) and katakana, 72–160 px, white with a magenta or teal 3–6 px hard drop shadow; optionally chrome-filled.
- **Window UI**: VT323 at 20–28 px (drawn at half size), black on the window grey-pastel.
- **Subtitles**: inside a small invented dialog window centred at the bottom, or white Noto Sans 600 at 34–40 px with a 2 px pink offset shadow; no full-width spacing in subtitles. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Noto Sans Devanagari in the dialog window; never letter-space it (tracking breaks the shirorekha).
- Japanese words must be real and checked by a reader; short ornament only, never invented gibberish.

## 5. Motion quality

- 24 fps on ones, everything at about 0.7 × natural speed: busts turn ≤ 10°/s, palms sway on 6–8 s periods, objects drift in slow sine paths.
- **Windows open in steps**: an outline rectangle grows over 4–6 frames, then the content appears; closing reverses it. No smooth zoom.
- **Stutter**: a moment can repeat 2–4 times (a chopped loop), the repeats slightly blurred with frame blending.
- Easing: `ss` and linear; no springs, no bounce.
- **Never moves**: the horizon and the sun; window title bars never wobble.

## 6. Camera grammar

A slow camera in a void; most staging is frontal collage. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal collage | A shrine of found objects | a memory; a product of the past; an inventory |
| Slow dolly over the checkerboard toward the horizon | An endless plaza, nowhere to arrive | consumer life; waiting; a dream of a holiday |
| Slow orbit around a bust or object | Contemplation, irony | an idea from history; authority; a museum piece |
| Push into a window until its content fills the frame | Entering a screen | a memory; an online world; a document |
| Pull back out of a window into the void | It was only a screen | a reveal; a dream ending; a loading screen |
| Rack between stacked windows | Layers of attention | multitasking; notifications; parallel lives |
| Screen-saver drift (objects bounce at the edges) | Idle time | waiting for a reply; boredom; night shift |
| Tape scrub (rewind or pause with tracking lines) | Memory replayed | a moment revisited; regret; evidence |

Framing: a centred, symmetric composition, 3–5 icons per frame, windows on a loose grid. Transitions: window close/open, tape tracking roll, a slowed cross-fade through white, chopped repeat cut; no whip pans or flashy glitch packs.

## 7. Sound palette

- **Slowed-and-chopped lounge music**: compose a smooth loop (piano or vibraphone chords, jazz bass, soft drum kit, alto sax line, an FM electric-piano voice synthesised in numpy), then slow it to 0.7–0.85 × by resampling (pitch and tempo drop together, like tape), add chorus and a big plate reverb, chop and repeat 1–2 beat fragments.
- **Muffled** option: low-pass the music near 2–3 kHz, as if heard from another shop.
- **Foley**: invented UI blips (sine 1–2 kHz, 40 ms), a soft error chime (two sine partials), fountain water, mall murmur (filtered crowd-like noise), escalator hum, tape hiss and motor wow.
- **Silence**: tape hiss only, with one blip.
- **Voice**: a smooth late-night radio or infomercial announcer, slightly slowed, with reverb; or a flat synthetic voice. Music ducked ~6 dB; −14 LUFS. Never reuse a real operating system's start-up or alert sound.

## 8. Native moves

- **Window as stage.** An invented window opens and its content becomes the scene. *Fits content like:* a memory; the features of a product; a list of choices.
- **Slowed loop.** A short moment repeats, slowed, with a stutter. *Fits content like:* nostalgia; a habit; an advertisement you cannot forget.
- **Bust contemplation.** A marble bust turns in the pastel void as text drifts past. *Fits content like:* an idea from history; a philosopher's quote; an authority questioned.
- **Infinite plaza.** A fountain-and-palm atrium that repeats to the horizon. *Fits content like:* consumerism; a waiting room; online shopping.
- **Screen-saver drift.** Objects bounce and drift while time passes. *Fits content like:* idle time; loading; a long night.
- **Dialog cascade.** Invented dialog boxes multiply and stack across the frame. *Fits content like:* overwhelm; notifications; bureaucracy.

## 9. Pitfalls of the medium

- **Copying real OS chrome, icons, fonts or sounds** → invent bevel colours, glyphs and chimes; no start menus or real wallpapers.
- **Wrong or nonsense Japanese** → short, real words checked by a reader; no random kanji.
- **Meme overload** → 3–5 icons per tableau, one idea per window.
- **Night neon** drifts into synthwave → keep pastel daylight values.
- **Tape pass eats the text** → render subtitles after the tape pass; reduce bleed under UI.
- **Modern PBR makes it a product render** → flat shading, low poly, vertex colours, env-map chrome.
- **Pitched-down music turns to mud** → high-pass below 60 Hz, cut 200–400 Hz, keep one bright element.
- **Irony without content** → each collage must carry the film's subject, not just the aesthetic.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `void.js`: sky gradient, sun, checker floor shader, fog, env-map bake for chrome.
- `icons.js`: low-poly generators (`bust`, `column`, `palm`, `dolphin`, `sphere`), marble texture, vertex snap.
- `window.js`: Canvas 2D bevel panels, title bars, dialogs, cursor; `openWindow(rect, t0)` stepped animation; content from render targets.
- `tape.js`: wraps `core/post/crt.js` with a soft preset; frame-blend stutter.
- `chop.py`: slow-down by resampling, chopped repeats, muffle filter.

Start from `core/post/crt.js`, `styles/backrooms/demo/vhs.js` (tape artefacts), `styles/lowpoly-island/demo/post.js` (sky blend by depth), `styles/glass-product/demo/studio.js` (env bake), `styles/hologram-hud/demo/engine/hud.js` (panel drawing), `core/lib.js`. Instruments from `core/audio/sampler.py` (piano, vibraphone, alto_sax, jazz_bass, drum_kit).

## 11. Variation space

The agent decides the icons, the windows' contents, the pastel trio, the amount of tape damage, the music's slowdown, the pacing and the camera path.

- Structures: **a lost-and-found inventory** (each forgotten object opens in its own window); **a guided tour of a mall that is not there**; **one evening replayed** (the same scene chopped and looped, changing slightly each time).
- Openings: **a cursor clicks an icon** in a pastel void; **a bust turns to face us**; **a tape is paused** on a sunset and starts playing slowed.
- Endings: **every window closes** until only the void remains; **the loop ends on its first frame**; **the screen saver takes over** and drifts forever.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
