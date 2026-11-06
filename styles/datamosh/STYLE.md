# Datamosh — Style Prompt

> Compressed video that has lost its key frames: the pixels of one picture are dragged by the motion of the next, macroblocks smear and swell, and a fresh key frame snaps everything clean again.
> References (grammar only): the late-2000s glitch-art practice of I-frame removal and P-frame duplication in music videos and net art (one scene "wearing" another, blooms of streaming pixels); the mechanics of block-based video codecs (groups of pictures, macroblocks, motion vectors, residuals, 8×8 transforms, 4:2:0 chroma). Never copy a specific music video or artwork, and never name them in the film.

## 1. Essence, and what it is not

- **Motion without its image**: at a moshed cut the old picture stays and moves with the new shot's motion vectors until the codec refreshes; one scene wears another.
- **Blocks**: 16×16 macroblocks and 8×8 transform blocks show in smears, steps and ringing; chroma lags in coarser blocks than luma.
- **Bloom**: one frame's motion vectors repeated, so pixels keep streaming and swelling in one direction.
- **Clean anchors**: long stretches of clean, ordinary, motion-rich footage; the glitch reads only against them, and a new key frame resets everything instantly.
- **The source is clean**: every scene is rendered cleanly in code first; the mosh is a codec process applied to it.

Not Liminal Found Footage (analog tape and lens damage; here purely digital codec logic), not ASCII / CRT Terminal (no characters, no phosphor), not Constructivist Montage (collision by cuts; here a cut that fails to happen), not a generic "glitch pack" (no RGB split, no scanlines, no random slice displacement, no fake error text).

## 2. Materials & rendering

- **Source layer**: clean scenes (three.js or 2D) plus a **motion-vector buffer** per frame. Because the engine knows every transform, write true screen-space velocity per pixel (a velocity material using previous and current matrices; 2D layers write their own displacement).
- **Codec layer** (WebGL2 float ping-pong at half resolution, then upscaled with nearest filtering on block edges):
  - **Block motion**: reduce the velocity buffer to one vector per 16×16 block (median), quantise to quarter pixels;
  - **Decode step**: `D(f) = warp(D(f−1), blockMV(f)) + r(f)·residual(f)`, where `residual = source(f) − warp(D(f−1))` and `r` is 1 for normal decoding, 0 for moshing; warp copies whole blocks with integer-plus-quarter offsets, not smooth per-pixel flow;
  - **I-frame**: `D = quantise(source)`; dropping one at a cut is the mosh;
  - **Bloom**: hold one frame's `blockMV` for N frames;
  - **Intra-refresh heal**: `r` ramps to 1 band by band (rows or columns of blocks) over 6–24 frames;
  - **Quantisation look**: per 8×8 block keep the mean plus a few low-frequency terms (a cheap DCT approximation), stronger in moshed areas; chroma at half resolution in blocks.
- **Determinism**: decoding depends on previous frames. Each mosh episode starts at a known I-frame; to render frame `f`, re-run the decode from that I-frame (≤ 96 steps at half resolution is cheap). Episodes are bounded; parallel workers agree because nothing reads wall-clock state.
- **A real-codec path** (splicing encoded packets so a P-frame chain runs over the wrong I-frame) depends on encoder details; verify it on the exact encoder first. The simulator is the default.
- **Clean overlays** (subtitles, labels) are composited after the codec layer.

## 3. Colour logic

- **Colour comes from the source scenes**: design each scene with a distinct palette and value key, so a mosh visibly drags one world into another (warm interior over cool street, day over night).
- **Never add colour**: no RGB split, no neon tint, no rainbow banding.
- **The codec's own colour** (green and magenta blocks where chroma data is "missing") is the rare accent, reserved for the most violent break.
- Clean anchors are graded naturally; moshed passages keep their source grade.
- Example: interior `#d9a066`, `#8c4b2f`, `#f2e3c6` against street `#2e4a62`, `#6fa3c7`, `#c7d3dd`; codec accent `#00c853` / `#d500f9`.

## 4. Type & subtitles

- **Titles** live in the source layer, so they can be moshed: Space Grotesk 700 or Inter 800 at 120–220 px; a title can melt into the first image of the next shot.
- **Labels and timecode**: IBM Plex Mono or Space Mono, 18–24 px, frame numbers, block grids, "I" and "P" markers when the film explains itself.
- **Subtitles** never mosh: Inter 600 at 36–44 px, white with a 2 px dark outline, bottom centre, composited after the codec layer. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Noto Sans Devanagari 600 or Mukta 600, same treatment.
- A word may be deliberately moshed only in a passage with no speech.

## 5. Motion quality

- 24 fps on ones (25 or 30 fps also feel native to codecs).
- **The mosh's character is chosen by the source motion**: a pan smears sideways, a push-in streams radially, a head turn melts a face, handheld shake makes jittery crumbs, a locked shot freezes the ghost in place.
- **Bloom** 6–48 frames; longer blooms read as overload.
- **Snap back** on an accent: a new I-frame is instant; a heal takes 6–24 frames as bands refresh.
- **Clean anchors ≥ 50 % of runtime**; one idea per mosh.
- **Never moves**: subtitles and labels.

## 6. Camera grammar

Source-camera moves are chosen for the motion they will donate to the mosh. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Whip pan (source) | Time ripped sideways | a sudden change; a missed moment; a jump between places |
| Push-in (source) | Being pulled into something | obsession; a memory taking over; focus |
| A subject turning its head (source) | Identity smearing | ageing; forgetting a face; a change of heart |
| Locked shot over a moshed ghost | The past refuses to leave | grief; a building that was demolished; a habit |
| Orbit around a subject | The world wrapping around | fame; pressure; a dance |
| Handheld walk | Restless crumbling | anxiety; a crowd; a search |
| Static clean frame after a mosh | Clarity returning | a decision; a fact; recovery |
| Slow dolly with parallax | Layers peeling apart | depth of history; a city's eras; a family |

Framing: give moshed motion a clear subject so the smear has shape; never mosh text-heavy frames. Transitions: the dropped I-frame cut (the mosh itself), the intra-refresh heal, freeze-and-bloom, a hard I-frame cut; no dissolves, no wipes.

## 7. Sound palette

- **Electronic with acoustic sources to break**: kicks, sub bass, chopped hats, plus piano and string phrases (`sampler.py` piano, violins) that get mangled.
- **Audio moshing** in sync with the picture: buffer stutter (repeat a 20–80 ms grain while the picture blooms), bit-crush and sample-rate reduction, low-bitrate smear (STFT with coarse magnitude quantisation and phase smearing), spectral freeze over a held ghost.
- **Foley** from the source scenes, smeared during moshes, clean in anchors.
- **Silence** is a digital dropout: true zero, cut with 2–5 ms fades to avoid clicks.
- **Voice**: close and clean; it may stutter only in passages without subtitles. Music ducked ~6 dB; −14 LUFS.

## 8. Native moves

- **Scene wears scene.** A cut without an I-frame: the old image moves with the new motion until refreshed. *Fits content like:* a memory haunting the present; one company absorbing another; a neighbourhood changing over decades.
- **Bloom.** Pixels stream and swell in one direction. *Fits content like:* information overload; a burst of anger; a flood.
- **Melt by turning.** A portrait melted by the motion of a head turning. *Fits content like:* identity change; forgetting someone; a mask dropping.
- **Intra-refresh heal.** The true image returns band by band. *Fits content like:* recovery; truth emerging; waking up.
- **Vectors shown.** The block grid and motion arrows drawn over the picture. *Fits content like:* how video compression works; traffic flow; wind over a field.
- **Still moved by life.** One still image carried by the motion of a live subject. *Fits content like:* a dancer carving a landscape; a runner through an old map; a family walking through a photo album.

## 9. Pitfalls of the medium

- **Glitch salad** (RGB split, scanlines, slice displacement) → only codec logic: dropped I-frames, block vectors, residuals, blocks.
- **No source motion, no mosh** → plan the donor motion of every moshed cut.
- **Continuous moshing** → anchors ≥ 50 % of runtime.
- **Workers disagree** → re-decode from the episode's I-frame, fixed step, seeded noise.
- **Everything softens** after many bilinear warps → block copies at quarter-pixel precision with nearest sampling inside blocks.
- **Smeared subtitles** → separate clean layer.
- **Photosensitivity** → no full-frame block flashing above 3 Hz; check before release.
- **Platform re-encoding destroys fine blocks** → block detail ≥ 16 px at 1080p, high bitrate master.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `source.js`: clean scenes plus a velocity buffer (three.js velocity material; 2D layers report their displacement).
- `codec.js`: WebGL2 ping-pong decode (`blockMV`, `warpBlocks`, `residual`, `iframe`, `dctLite`, chroma 4:2:0).
- `gop.js`: the schedule of I-frames, dropped I-frames, blooms and heals; `decodeAt(f)` re-runs from the episode start.
- `overlay.js`: subtitles, labels, optional vector visualisation.
- `mosh.py`: grain stutter, bit-crush, spectral smear and freeze aligned to the GOP schedule.

Start from `styles/microgame/demo/glpass.js` (shader pass helper), `core/three/post.js` (render targets and passes), `styles/backrooms/demo/vhs.js` (how a medium-damage pass is structured, though analog), `core/lib.js` (`mulberry`, `hash`), `core/render/video.mjs` (parallel frame rendering, which the per-episode re-decode must respect). Audio built on `core/audio/sampler.py` and `core/audio/sfx.py`.

## 11. Variation space

The agent decides the source scenes and their motion, which cuts mosh, bloom lengths, the heal style, the ratio of clean to moshed, the pacing and the music.

- Structures: **two worlds alternating** (each cut carries the last place into the next); **one portrait through a lifetime** (a single face moved by the motions of many years); **a clean film with three breaks** (each mosh marks one turning point).
- Openings: **a clean, calm long shot** that holds before the first broken cut; **a frozen frame** that begins to stream; **a block grid** assembling into the first image.
- Endings: **one last key frame** snaps everything clean and still; **an endless bloom** that dissolves into a single colour; **the heal stops halfway**, half past and half present.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
