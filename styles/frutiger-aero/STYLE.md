# Frutiger Aero — Style Prompt

> Glossy, sunlit tech optimism: sky-blue skies, lush green hills and clear aqua water, translucent gel shapes with a crisp white shine, bubbles and droplets that refract the world, soft light swooshes and bokeh. Nature and gadget in harmony.
> References (grammar only): mid-2000s consumer-electronics and telecom advertising (eco-tech optimism, nature with devices); glossy "gel" interface buttons and reflective floors of mid-2000s web design; underwater and macro nature photography (droplets, caustics, light rays). Never recreate a real operating system's wallpaper, icons, start-up sounds, brands or fonts, and never name them in the film.

## 1. Essence, and what it is not

- **High-key nature**: sky blue with fluffy clouds, saturated grass green, clear aqua water, bright sun; clean and fresh.
- **Gloss**: rounded "gel" shapes with a crisp white top highlight, a soft glow at the bottom, a 1 px white inner edge, a soft shadow and a mirror reflection on a white or water floor.
- **Bubbles and droplets** refract what is behind them, with a thin-film rim and two highlights.
- **Light**: aurora-like translucent swooshes, bokeh dots, god rays under water, a restrained lens flare.
- **Humanist sans and white space**: friendly, rounded, optimistic.

Not Glass Product Render (one serious object in a dark studio; here the world is sunny and playful), not a liquid-glass interface (that bends the content behind thin panes; here shapes are gel-gloss with a painted shine), not Y2K Chrome (silver liquid metal; here aqua water and grass), not Low-poly Isometric Island (no facets, no orthographic model), not Memphis Diorama (no flat patterns, everything glossy).

## 2. Materials & rendering

- **Backdrop** (Canvas 2D or shader, cached): sky gradient (`#2a8ff0` top → `#bfe8ff` horizon), cumulus clouds from layered soft noise blobs with bright tops, rolling hills as smooth curves filled with a green gradient (light crest → saturated base) plus fine grass noise, a sun glow.
- **Gel shapes** (Canvas 2D, per object): rounded-rect or circle filled with a vertical gradient (light top → saturated bottom); top gloss = an ellipse clipped to the upper half, white 65 % → 5 %; bottom inner glow in a lighter tint; 1 px white inner stroke at 40 %; drop shadow; floor reflection = the shape flipped, alpha 30 % → 0 over 40 % of its height.
- **3D variant** (three.js): `MeshPhysicalMaterial` with `clearcoat: 1`, low roughness, an environment baked from the sunny backdrop; reflective floor via a `Reflector`.
- **Bubbles** (WebGL 2D pass): inside each circle, sample the backdrop with a radial lens offset (stronger at the rim, inverted image in the centre for droplets); rim thin-film hue shifting with angle (pink → green → blue, narrow band); top-left crescent highlight and a small bottom-right glint; pop = a ring of 6–10 droplets flying out and fading.
- **Water**: a surface line with soft sine waves; below it caustic light (warped Voronoi, additive), god rays (additive gradients with noise), particles drifting.
- **Light**: additive ribbon swooshes (Catmull-Rom bands, 10–25 % opacity, soft edges), bokeh discs, one flare per shot at most.
- **Post**: gentle bloom, high-key grade, slight saturation boost; text drawn after bloom. Everything a function of `t`.

## 3. Colour logic

- **Blue, green and aqua** are the three dominant hues; white is the neutral and the light.
- **Gradients run light-on-top to saturated-on-bottom**, always; one global light from the upper left.
- **No black.** The darkest value is deep navy or teal, used for text and shadows.
- **One warm accent** (orange, sunny yellow or a coral fish) reserved for the focal object or call to action.
- Gloss belongs to interactive or hero objects; backgrounds stay soft and unglossed.
- Example: sky `#2a8ff0` → `#bfe8ff`, grass `#7ed957` → `#2f9e3a`, aqua `#00c2d1`, white `#ffffff`, text `#0b2a4a`, accent `#ff9f1c`.

## 4. Type & subtitles

- **Titles**: Nunito 800 or Varela Round, 90–170 px, white with a soft blue glow, or navy on a gel plate; may carry a gloss highlight and a floor reflection.
- **Body and labels**: Open Sans or Nunito, 24–32 px, navy.
- **Subtitles**: on a translucent white rounded plate (alpha 70 %, top gloss, soft shadow), centred low, Nunito 700 at 36–42 px in navy `#0b2a4a`. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Baloo 2 600 (rounded, matches the friendly sans) or Hind; same plate.
- Never a system font of any real operating system.

## 5. Motion quality

- 24 fps on ones; smooth and floaty. UI-like pop-ins use `back` with a small overshoot (s ≈ 1.2); scene moves use `eio`.
- **Bubbles rise** with a sideways sine wobble and slight squash; droplets fall with gravity and splash in a ring.
- Appear: bubble up, swell from a droplet, or slide in with a shine sweep across the surface. Disappear: pop into droplets, or sink below the water line.
- Clouds drift slowly; grass sways in long waves; fish swim in smooth arcs.
- **Never moves**: the sun's position and the light direction; nothing is fast or jerky.

## 6. Camera grammar

A gentle, floating camera in a clean, bright world. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow crane over green hills toward the sky | Optimism, openness | a new beginning; a launch; a promise |
| Dip through the water surface | Going deeper, calm | how something works; ocean data; relaxation |
| Push into a bubble (its world fills the frame) | An idea held inside | a product feature; a dream; a plan |
| Orbit around a gel object on a reflective floor | Presenting, pride | a gadget; an award; a new service |
| Lateral glide with parallax bokeh | Flow, ease | a day in a life; a journey; a process |
| Locked "wallpaper" frame | Calm, clarity | a statement; a title; a pause |
| Split level, half above and half below water | Two worlds, connection | surface and depth; online and offline; cause and effect |

Framing: generous white and sky space, hero centred or on a third, one light direction, nothing touching the frame edge abruptly. Transitions: bubble wipe (bubbles fill the frame and pop), shine sweep, water-surface crossing, droplet ripple, soft cross-fade with a bloom lift; no hard glitch, no black frames.

## 7. Sound palette

- **Bright and clean**: marimba, vibraphone, glockenspiel, kalimba, harp, piano, acoustic and nylon guitar plucks (`pluck.py`), soft sine and triangle pads (numpy), light claps and shaker, hand chimes.
- **Foley**: water drops (sine with a fast pitch drop), bubble pops (short resonant blips), streams and gentle waves, birdsong, wind in grass, a soft glassy "tink" for gel taps, a shimmering chord swell for reveals (invented, never a real start-up sound).
- **Ambience**: open air or soft underwater (low-passed, slow bubbles).
- **Silence**: a held breath of water ambience with one drop.
- **Voice**: friendly, optimistic, clear presenter. Music ducked ~6 dB under voice, airy reverb, −14 LUFS.

## 8. Native moves

- **Bubble world.** A bubble rises, the camera enters it, a small world lives inside. *Fits content like:* an idea; a holiday dream; a product feature.
- **Gel press.** A glossy button presses, shines, and a ripple spreads into the landscape. *Fits content like:* a decision; booking a ticket; switching to clean power.
- **Leaf to panel.** A leaf unfurls into a glossy information panel. *Fits content like:* green energy; a health app; a farm report.
- **Water crossing.** The camera slips under the surface into rays, fish and bubbles. *Fits content like:* a deeper look; ocean science; a calm-down moment.
- **Light swoosh.** A translucent ribbon sweeps through, carrying a word. *Fits content like:* a transition; connection between places; a network.
- **Droplet lens.** A water droplet magnifies a word or object behind it. *Fits content like:* a detail to notice; a key number; a small print.

## 9. Pitfalls of the medium

- **Recreating real OS wallpapers, icons or sounds** → invent landscapes, glyphs and chimes.
- **Gloss everywhere flattens hierarchy** → gloss only on hero and interactive shapes; soft backgrounds.
- **Washed-out high key** → keep saturated gradient bottoms, navy text, value contrast ≥ 4.5:1 for words.
- **Flat-circle bubbles** → refraction, thin-film rim and two highlights.
- **Inconsistent highlights** → one global light; all gloss and glints obey it.
- **Generic stock-image collage** → one coherent world with depth and parallax.
- **Bloom halos on text** → render text after bloom.
- **Banding in skies** → float targets and dither.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `sky.js`: sky gradient, procedural clouds, hills, sun glow, cached layers.
- `gel.js`: `gel(ctx, shape, colour, {gloss, glow, reflection})`, pop-in timing.
- `bubble.js`: WebGL refraction pass, thin-film rim, highlights, `pop(t0, seed)`.
- `water.js`: surface waves, caustics, god rays, particles.
- `swoosh.js`: additive ribbons and bokeh.

Start from `styles/glass-product/demo/studio.js` (environment baking, reflective floor), `styles/glass-product/demo/product.js` (glass and frosted materials), `styles/microgame/demo/glpass.js` (2D shader pass helper), `styles/lowpoly-island/demo/sea.js` (wave function), `core/three/post.js` (bloom, grade), `core/lib.js`. Instruments from `core/audio/sampler.py` (marimba, vibraphone, glockenspiel, kalimba, harp, hand_chimes) and `core/audio/pluck.py`.

## 11. Variation space

The agent decides the landscape, the gadgets or ideas inside the bubbles, the accent, how much water, the pacing and the camera path.

- Structures: **a raindrop's journey** (cloud to spring to tap, each stage a glossy scene); **a day of one clean machine** (sunrise to dusk on a hill); **a catalogue of bubbles** (each bubble one idea, entered and left).
- Openings: **a single droplet** lands and the ripple paints the hills; **a gel button glows** on white and is pressed; **underwater looking up** at the sun, rising through the surface.
- Endings: **all bubbles pop** into a fine spray that becomes clouds; **crane up** into a clean sky; **the scene shrinks into a droplet** on a leaf.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
