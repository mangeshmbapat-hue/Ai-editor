# Reference build: the McDonald's explainer (2026-11-13)

The owner called this explainer "very good kya gajab bnaya h". These files are its **code only**, kept as the pattern for future explainers. The owner's images, VO and the render are not in git; they live in `projects/mcdonalds/` on the machine where it was made.

- `mcdonalds-explainer.html`: the GSAP composition. It has the helpers `pop`, `rise`, `out`, `words`, `draw`, `counter`, `badge`, `scene`, `wipe` and `tap`, and 8 sections timed from `words.json`. It expects `assets/` with the cutouts and `assets/people/*.svg`.
- `mcdonalds-spec.json`: the `spec.json` for `anim-storyboard` and `anim-render` (the composition mode).
- `music-compose.py`: the generator of the original music bed (tonejs-instruments samples, CC BY 3.0).

Reuse the structure and the helpers, not the brand: every new video gets its own theme, words and assets.
