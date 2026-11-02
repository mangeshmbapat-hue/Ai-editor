# Viral studio

A team of four agents (plus Mann, the editor) that finds what people want to watch, researches it, writes a script built to hold attention, and makes the film. Each agent is defined in `.claude/agents/`; the pipeline and the gates are in `.claude/skills/viral-studio/SKILL.md`.

| Agent | Kaam (job) | Writes |
|---|---|---|
| **social** | Trending topics dhoondhna (with dated sources), virality score, competition gap, hook critique, publishing kit, performance review | `01-trend-board.md`, `07-publish-kit.md` |
| **researcher** | Unique angle aur detailing: verified facts, wow details, era-accurate visual and sound details, myth vs record | `02-research.md`, `FACTS.md` |
| **writer** | Viral script: hooks, holds, open loops, suspense, cliffhangers, loop endings, A/B hooks, retention map | `04-script/SCRIPT_vN.md`, `dialogue-lock.md` |
| **director** | Style, aspect, duration, flow; then production from style frame to edit, mix, QC and final files | `03-format.md`, the film, `06-qc.md`, `final/` |
| **mann** | Editor for the owner's raw footage: storyboard first, then cut, motion graphics, sound design, colour, VFX, QC; style lab and learned rules (`/mann-edit`, `/mann-style-lab`) | `edit/edl.json`, `edit/storyboard/`, `edit/renders/`, `editor/styles/` |

The orchestrator (the main session, running `/viral-studio`) runs the agents, passes the files between them and stops at the owner's gates.

## Flow

```
owner's ask ─► social: trend board + 3 pitches ─► [Gate 1: pick, or "khud chuno"]
                         │
         ┌───────────────┴───────────────┐
   researcher: research + FACTS     director: format brief (style, 9:16/16:9, duration)
         └───────────────┬───────────────┘
                writer: script v1 (hooks, retention map)
                         │
         director (flow) + social (hooks) critique ─► writer: v2
                         │
            [Gate 2: owner approves script + format]   ◄── nothing is produced before this
                         │
   director: 3 frames at 3 timecodes + a 20–30 s music sketch
                         │
            [Gate 3: owner approves look + music]       ◄── full production only after this
                         │
   director: voice → music → SFX → picture → edit → mix → QC → final/
                         │
            [Gate 4: owner approves the final cut] ─► social: publishing kit
                         │
            studio-learn: owner feedback → studio/LEARNINGS.md
```

## Use it

- `/viral-studio`: scan what is trending and pitch three ideas.
- `/viral-studio <topic>`: skip the scan and make a film on the topic.
- `/viral-studio khud chuno`: the team picks the top pitch and goes as far as the script gate.
- Call one agent directly when you need only that job ("social se trending topics nikalo", "director se is script ka flow check karao").
- Feedback of any kind ("ye hook weak hai", "aisa SFX mat lagana") is recorded by `/studio-learn` in `studio/LEARNINGS.md`, and every agent reads it before it works.

## Rules that never bend
- No production before the owner approves the script (Gate 2), and none before the owner approves 3 timecode frames and the music sketch (Gate 3).
- Music gets special attention at every stage.
- Out-of-the-box experiments are allowed: every brief and script carries one bold option labelled `experiment`.
- Every night about 10:40 PM IST a scheduled task suggests 10 trending topics with a style for each (`studio/NIGHTLY.md`).
- No posting, scheduling or messaging on any platform. The owner publishes.
- No invented facts, trend numbers or sources.
- At most 3 agents run in parallel.

Project work lives in `projects/<slug>/` (git-ignored); the templates are in `studio/templates/`.
