# Skill map

Read [film-production](../skills/film-production/SKILL.md) to coordinate the whole workflow. It routes to these specialist skills. Phase 0 runs only when the owner has not supplied a screenplay, and its approval gate must pass before any later phase starts:

| Phase | Skill | Persistent output |
|---|---|---|
| 0 | [ai-writer](../skills/ai-writer/SKILL.md) | Approved script packet (`script/SCRIPT_vN.md`) and `dialogue-lock.md` |
| 1 | [screenplay-breakdown](../skills/screenplay-breakdown/SKILL.md) | Source-linked beats and asset requirements |
| 2 | [creative-direction](../skills/creative-direction/SKILL.md) | Treatment and labelled decisions |
| 3 | [character-costume-design](../skills/character-costume-design/SKILL.md) | Canonical identity/look images and scene mapping |
| 4 | [location-prop-design](../skills/location-prop-design/SKILL.md) | Spatial/prop references and state notes |
| 5 | [shot-continuity](../skills/shot-continuity/SKILL.md) | Ordered shots, timing, dependencies and boundaries |
| 6 | [storyboard-keyframes](../skills/storyboard-keyframes/SKILL.md) | Reviewed panels and clean frame assets |
| 7 | [video-tool-handoff](../skills/video-tool-handoff/SKILL.md) | Tool-adapted bundle and actual imported takes |
| 8 | [coverage-quality-audit](../skills/coverage-quality-audit/SKILL.md) | Breakdown/clip review evidence and completion report |

These files add domain instructions; they do not supply model subscriptions, image generation, video playback or provider APIs. Use the capabilities of the host assistant, preserve user authorization and report missing capabilities accurately. Reading a skill does not install it globally. Keep this repository available so linked contracts resolve.

## Viral studio

For trend-led films, `/viral-studio` ([pipeline](../.claude/skills/viral-studio/SKILL.md)) coordinates four project agents in `.claude/agents/`: **social** (trends, virality, publishing kit), **researcher** (unique angle, verified detail), **writer** (hooks, retention, the script packet for [ai-writer](../skills/ai-writer/SKILL.md)'s approval gate) and **director** (style, format, duration, production, QC). The owner's feedback is recorded by `/studio-learn` in [studio/LEARNINGS.md](../studio/LEARNINGS.md). An overview is in [studio/README.md](../studio/README.md).
