# AI-film repository conventions

- This is the standalone production project. Do not import code, assets, credentials or data from unrelated workspaces.
- Keep implemented features distinct from roadmap items. Never call templates verified model profiles or synthetic fixtures generated film assets.
- Script gate: a new film without an owner-supplied screenplay starts with `skills/ai-writer`, written by a separate writer agent and critiqued by another. Show the script packet and wait for the owner's explicit approval before any voice, music, picture or render work. Approved words are locked; changes go back through the writer and need approval again.
- Viral studio: the social, researcher, writer and director agents (`.claude/agents/`) work through `/viral-studio` (`.claude/skills/viral-studio/SKILL.md`), coordinated by the main session, which passes their files and stops at the owner's gates. Every agent reads `studio/LEARNINGS.md` first; the newest owner rule wins.
- Editor: Mann (`.claude/agents/mann.md`, `/mann-edit`, `/mann-style-lab`, code in `aifilm/editor/`) edits the owner's footage. The full render is gated on the owner's recorded storyboard approval for the exact EDL; keep that gate in any change. Measurable owner corrections go into `editor/rules.json`.
- Faceless Editor (`.claude/agents/faceless-editor.md`, `/faceless-edit`, code in `aifilm/editor/faceless.py`) edits faceless videos (VO + images/clips) in the house style learned from the owner's 4 samples (`editor/styles/faceless-collage-explainer/`). It uses Mann's engine and the same storyboard approval gate.
- Animation Editor (`.claude/agents/animation-editor.md`, `/animation-edit`, code in `aifilm/editor/animation.py` + `aifilm/editor/anim/`) makes product-promo animation reels in the house style learned from the owner's 4 samples (`editor/styles/animation-product-promo/`). `anim-render` is gated on the owner's recorded `anim-approve` for the exact spec and assets; keep that gate in any change.
- Imported format skills: at the owner's request (2026-11-02), `.claude/skills/` also holds the 47 skills from the owner's Ai-Animation repo, MIT © aansh.ai (`third_party/ai-animation/`). `studio/import_skills.py` generated them and registered them in `studio/IMPORTED_SKILLS.json`. They run inside `studio/SKILL_HARNESS.md`. Change the generator or the harness, never the copies, and re-run the importer to sync.
- Self-learning: whenever the owner corrects, praises, rejects or states a preference, record it with `/studio-learn` in `studio/LEARNINGS.md` in the same turn, then apply it.
- Preserve original screenplay text. Source units, semantic beats, shots, inputs, takes and reviews are separate records.
- Do not mark a shot accepted based on a prompt, successful upload or provider status. Require full-clip review evidence for all assigned beats and criteria.
- Preserve canonical asset versions. Changes must invalidate dependent outputs; do not silently discard references to satisfy model limits.
- Keep portable mode useful without credentials. Tool-specific limits require current official documentation or a dated direct verification.
- Execute routine planning and reversible implementation within user scope. Escalate material creative contradictions with a concrete recommendation, not routine choices.
- The CLI is single-writer per project. Preserve atomic state writes and the project lock in new mutations.
- Run `python3 -m unittest discover -s tests -v` and `python3 -m compileall -q aifilm` for core changes. Media tests need FFmpeg.
- Keep production projects/exports out of commits. Use synthetic fixtures for tests and clearly label them.
