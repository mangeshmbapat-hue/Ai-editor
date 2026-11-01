# Pattachitra — Style Prompt

> Odisha cloth painting brought to life: opaque colour on a chalk-coated cloth, flat red grounds, figures in held dance-like poses, borders band inside band, sealed by a sure black outline and a lacquer sheen that catches a passing light.
> References (grammar only): the Pattachitra of Odisha, painted by chitrakar families (notably the village of Raghurajpur near Puri) on cloth prepared with tamarind-seed paste and chalk, in colours from natural sources (conch-shell white, lamp-black, red and yellow minerals), and its palm-leaf cousin *tala pattachitra*, incised with a stylus. Take the border-first order, the flat grounds, the pose language and the outline; never copy a specific painting or its subject, and never name them in the film.

## 1. Essence, and what it is not

- **Borders inside borders.** Two to four ornamental bands (creeper, lotus petals, dot rows, zigzag) frame every panel; the border is painted first and is part of the picture.
- **Flat opaque grounds**, most often red, sometimes yellow, black or green: no sky, no horizon, no depth.
- **Figures in held poses**: elongated eyes, profile or three-quarter faces, bodies bent in graceful stances, hands in clear gestures, rich costume and jewellery.
- **A black outline drawn last** over every colour area, fine and sure, with white dot ornament on jewellery, borders and costume.
- **Stylised nature**: trees as decorative forms with patterned leaves, animals and birds as emblems, water as rows of waves.

Not Kalamkari (that is transparent dye soaked into the weave; here colour is opaque paint on a smooth chalk ground with a lacquer gloss), not Kalighat Pat (no shading, no blank paper background, no satire), not Ukiyo-e (no woodblock, no paper, no bokashi), not Stained Glass (front-lit opaque paint, no transmitted light, no lead).

## 2. Materials & rendering

- **Ground (patta)**: chalk-and-gum coated cloth burnished smooth: cream, faint weave (5 % multiply), burnish streaks, fine craquelure (thin Voronoi edges 4–8 % darker); seeded, cached, world-anchored.
- **Paint**: opaque flat fills with a fine brush-direction texture (directional noise at 2–3 % value) and pigment grain; edges slightly soft (1 px) because the black line covers them later.
- **Layer order** (also the animation order): borders → ground colour → base colours of figures → secondary colours and patterns → white ornament → black outline → lacquer.
- **Outline brush**: tapered strokes 1.5–3.5 px at 1080p, thicker on contours, finer inside (eyes, fingers, folds); stroke ends taper. Each contour is one or two strokes, never sketchy.
- **White ornament**: dot rows (2–3 px dots at regular spacing with ±0.5 px jitter), tiny flowers, scallops along hems and borders.
- **Lacquer**: build a height map from the paint layers (each layer +1 step, outline slightly raised), derive normals, and add a soft specular term from a moving light (a broad lobe, 10–20 % intensity, warm). The sheen is the only light effect.
- **Palm-leaf variant**: narrow leaf strips with incised lines filled with soot and wiped, leaf fibres, a cord hole; strips fold like an accordion.
- Panels cache as sprites; everything is a pure function of t under fixed seeds.

## 3. Colour logic

- **4–6 opaque colours**: red, yellow, white, black as the core; one blue or green at most as a guest. Nothing transparent, nothing blended.
- **The ground is one colour per panel**, usually red; figures stand on it with no cast shadow.
- **Black outlines everything**; white is reserved for ornament, eyes and the brightest garments.
- Volume is never shaded; it is shown by pattern and outline.
- A sequence of panels can rotate ground colours (red, yellow, black) to mark chapters.
- Example: ground red `#b8321f`, yellow `#e8b331`, white `#f3ead6`, black `#191512`, guest green `#2f6b4a`, cream ground `#eadcbc`.

## 4. Type & subtitles

- Text sits in a **cartouche** built like a border band: a cream strip with a dot-row frame, at the bottom of the panel.
- Titles: **Rozha One** (Latin and Devanagari, 70–120 px), black with a white dot-row underline. Subtitles: **Noto Serif Devanagari** or **Hind** for Hindi, **Cormorant Garamond** semibold for Latin (36–44 px); Odia captions in **Noto Sans Oriya**. Hindi subtitles are supported.
- Text is painted, not typed: a quick fill, then the black outline pass on titles only. Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps** for painting and camera; figures on twos (12 fps), **pose to pose**: a figure holds a stance, moves through 2–4 in-betweens and lands in the next stance, like a dancer settling into a pose.
- Hands carry the acting: gestures change on accents while the body holds.
- **Painting-in follows the layer order**: borders run around the panel (0.6–1.2 s), the ground floods, colours fill, ornament dots appear in quick rows, the black outline sweeps last and makes everything sharp.
- Water and leaves loop as 3–4 drawing cycles. Nothing tweens smoothly through space except the camera and the lacquer light.
- Never moves: borders once painted, the ground colour within a panel.

## 6. Camera grammar

A painted cloth hung square to the camera; panels are rooms to enter.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked panel inside its borders | a held tableau | a ceremony; a statement; a portrait |
| Push from the whole cloth into one panel | choosing one episode | a case study; a detail of a plan |
| Grid of panels read in order | a sequence at a glance | stages; options; a week |
| Pan along a border band | ornament as time or path | a route; a countdown; a transition |
| Light sweep across the lacquer, camera still | the object is precious and finished | a reveal; a final state; a product of work |
| Close on hands and white ornament | care, gesture | a craft; a promise; a greeting |
| Palm-leaf strips unfolding, top-down | a book opening | a list; a manual; a chronicle |

Framing: figures fill 60–80 % of their panel's height; symmetry is common; borders stay visible except in a deep push. Transitions: a border painted around the next panel; a move to a neighbouring cell; a lacquer flare for a few frames. Forbidden: dissolves, depth of field, perspective, grading drifts.

## 7. Sound palette

- **Instruments as options**, in the manner of Odisha's classical and folk music: a barrel drum (the synthesised tabla model tuned lower and rounder, like a mardala), tiny cymbals (`nepal_bells`, `triangle` damped), bamboo flute (`flute`), harmonium (`accordion`), a plucked drone (`pluck('shamisen', …)`, long t60, buzz). Never imitate temple ritual music or a specific song.
- Pose changes land on drum strokes; ornament rows tick softly (`glockenspiel`, very low velocity).
- **Foley by material**: brush on a smooth chalk ground (short soft swishes), burnishing stone (low rub), stylus scratching palm leaf (dry, high), leaves rustling, cloth unrolled, a distant sea for a coastal setting.
- **Silence**: the outline pass in near silence, one brush sound per stroke.
- **Voice**: a calm, rhythmic storyteller; Hindi or Odia narration fits. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Border first.** The frame paints itself before any content. *Fits content like:* setting rules before a game; a site boundary before building; a budget before spending.
- **The outline locks it.** Soft colour blocks become sharp and final when the black line sweeps over them. *Fits content like:* a decision taken; a design finalised; a law passed.
- **Panel grid.** Many small panels in a grid, each an episode, read in order or all at once. *Fits content like:* the days of a festival; ten steps; a family of products.
- **Held pose.** Figures settle into clear stances and gesture with the hands. *Fits content like:* a greeting; an instruction; a negotiation.
- **Lacquer sheen.** A warm light slides across the finished panel and makes it an object. *Fits content like:* a reveal; a heritage piece; a result worth keeping.
- **Palm-leaf book.** Narrow incised strips unfold one by one. *Fits content like:* a list of rules; a genealogy; an old record.

## 9. Pitfalls of the medium

- Gradient shading or drop shadows → flat only; outline and pattern carry volume.
- Outline drawn first and coloured inside reads as a colouring book → colour first, black outline last and slightly over the edges.
- Missing borders → every panel has two or more bands.
- Too many colours → core four plus one guest.
- Sheen everywhere all the time reads as plastic → one moving light, 10–20 %, only when the panel is finished.
- Figures stiff in straight-on stances → curved, dance-like stances with clear hand gestures.
- **Sacred iconography as decoration.** Much Pattachitra depicts deities and temple stories; do not use deities or their emblems as ornament, for a product or in jest. Do not present a code-made film as authentic handmade Pattachitra; for commercial work, credit or consult chitrakar artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `patta.js`: `chalkGround(seed)` with weave, burnish and craquelure; `heightFromLayers`; `lacquer(light, t)` normal-map sheen.
- `paint.js`: `fillOpaque(shape, colour, dir)`, `outline(path, {w, taper})`, `dotRow(path, spacing)`, `ornament(kind, path)`.
- `border.js`: `bands(rect, [creeper, petals, dots, zigzag])`, painted with progress.
- `pose.js`: flat rig, `stance(name)`, `poseToPose(a, b, p)`, hand gesture swaps.
- `palmleaf.js`: incised strips, `unfold(n, t)`.

Start from `styles/ukiyoe/demo/print.js` (`buildTextures`, `fibers`, `fillPath`, `line`, `cartouche`), `styles/papercut-red/demo/rig.js` (`solveRig`), `styles/stained-glass/demo/glass.js` (`voronoi` for craquelure, `brush`, `line`), `core/three/post.js` (grade, if the sheen moves to WebGL), `core/lib.js`, `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`.

## 11. Variation space

You decide the panels, the ground colours, the figures and their stances, the border bands, whether to use palm leaf, the opening, the ending, the camera path and the pacing.

- Structures: **a grid read in order** (each panel an episode, the camera hopping from cell to cell); **one panel, many states** (the same tableau repainted as conditions change); **cloth and leaf** (a painted cloth for the big picture, palm-leaf strips for the details).
- Openings: **the border painting itself** around an empty red ground; **a chalk ground being burnished** before any paint; **a finished panel under a passing light**, then back to its first stroke.
- Endings: **the outline locks** the last panel; **the lacquer sweep** across the whole cloth; **the palm-leaf book folds** and the cord is tied.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
