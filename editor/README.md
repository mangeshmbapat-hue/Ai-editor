# Mann: AI video editor

Mann is the studio's editor agent (`.claude/agents/mann.md`). Give it raw footage plus a script or direction; it cuts the film with motion graphics, sound design, colour and VFX, shows a storyboard first, and renders only after you approve it. It also studies reference videos and AI-video styles, writes style sheets, and turns every correction you give into a rule it checks next time.

| Ask | Skill |
|---|---|
| "Ye raw clips hain, is script pe edit karo" | `/mann-edit` |
| "Is reel ka style samjho, style sheet banao" | `/mann-style-lab` |
| "Ye cut late hai / music loud hai" (any correction) | `/studio-learn` → `studio/LEARNINGS.md` (Editor) + `editor/rules.json` |

## Toolchain (open source)

| Tool | Used for | Install |
|---|---|---|
| [FFmpeg](https://ffmpeg.org) | trim, speed, crop/reframe, grade, LUTs, transitions (xfade), titles (drawtext with Devanagari shaping), burned subtitles (libass), music ducking, SFX, two-pass loudness, QC measurements | system package |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (or openai-whisper) | transcripts, word-timed phone captions | `pip install faster-whisper` |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | downloading reference videos for the style lab | `pip install yt-dlp` |
| [Hyperframes](https://github.com/heygen-com/hyperframes) | HTML + GSAP motion graphics rendered to ProRes 4444 with alpha, laid over the cut | `npm i -g hyperframes@0.8.230` (Node ≥ 22) |

`bash editor/install.sh` installs all of them; `python3 -m aifilm.editor doctor` reports what is present.

## Commands (`python3 -m aifilm.editor …`, or `mann …` after `pip install -e .`)

| Command | What it does |
|---|---|
| `doctor` | Which tools are installed |
| `ingest <edit> <files…> [--link]` | Copy (or symlink) raw files into `<edit>/raw/`, record probe + sha256 in `media.json` |
| `transcribe <media> <out> [--language hi] [--model small]` | `<stem>.json`, `<stem>.srt`, `<stem>.captions.srt` (≤ 4 words per cue) |
| `scenes <video>` | Detected cut times |
| `validate <edit>` | Check `edl.json`, print the timeline and pace |
| `storyboard <edit> [--two]` | Numbered frames from the full edit graph + `STORYBOARD.md` (pace, sound plan, changes since the previous storyboard) |
| `approve <edit> --words "…" [--final]` | Record the owner's exact approval, tied to the EDL and source fingerprints |
| `render <edit>` | Refuses without a matching storyboard approval; writes `renders/master.mp4` (−14 LUFS, two-pass) and `preview_720p.mp4` |
| `qc <edit> [--frames 1.5]` | Measures the master against the EDL, `editor/rules.json` and the style target; `renders/QC.md`; exit 1 on failure |
| `fetch <url> <dir>` | yt-dlp download for study |
| `analyze-style <video> <workdir> --name …` | Cut rhythm, pace curve, palette, tone, loudness, silences, one frame per shot, draft style sheet |
| `publish-style <workdir> <slug>` | Save a finished sheet + targets to `editor/styles/<slug>/` |
| `mg-new <edit> <name>` / `mg-render <edit> <name>` | Hyperframes composition in `<edit>/mg/<name>/` → `mg/<name>.mov` with alpha |

## Edit folder (`projects/<slug>/edit/`, git-ignored)

```
BRIEF.md        the owner's script/direction, verbatim
raw/            the owner's media (never modified)
media.json      probe + sha256 per file
transcripts/    Whisper output
LOG.md          Mann's footage log: best takes and moments
edl.json        the cut
mg/             Hyperframes compositions and their .mov renders
storyboard/     F01_<clip>_<timecode>.jpg …, STORYBOARD.md, storyboard.json
approvals.json  the owner's approvals (storyboard, final) with their words
renders/        master.mp4, preview_720p.mp4, QC.md, qc.json, qc-frames/
```

## EDL (`edl.json`)

See `edl.example.json`. Fields:

- `format`: `width`, `height` (even), `fps`, `fit` (`cover` crops to fill, `contain` letterboxes).
- `sources`: id → file inside the edit folder.
- `clips[]`: `id`, `source`, `in`, `out` (source seconds), `speed` (0.25–4, audio pitch kept), `beat` (why the shot is there), `transition_in` (`cut`, `dissolve`, `fade`, `fadeblack`, `fadewhite`, `wipeleft|right|up|down`, `slideleft|right|up|down`, `smoothleft|right`, `circleopen|close`, `radial`, `pixelize`, `zoomin`, `hblur`, `distance`, `squeezeh|v`, with `duration`), `zoom` (`from`/`to`, punch-in or Ken Burns), `grade` (per-clip preset), `audio` (false mutes the clip), `text` (one or a list: `value`, `position` top/center/bottom, `size`, `color`, `box`, `start`, `end`, `font`).
- `grade`: `preset` (`neutral`, `punchy-social`, `teal-orange`, `warm-film`, `cool-night`, `bw-contrast`, `faded-vintage`, `moody-dark`, `bright-clean`), `exposure`, `contrast`, `saturation`, `temperature` (K), `lut` (.cube), `grain`, `vignette`.
- `audio`: `keep_source`, `source_gain_db`, `music` (`file`, `gain_db`, `start`, `duck`, `fade_out`; looped to length), `sfx[]` (`file`, `at`, `gain_db`).
- `overlays[]`: `file` (Hyperframes .mov with alpha, or any video), `at`.
- `subtitles`: `file` (.srt), `burn`, optional `force_style`, `margin_v`.
- `style`: a slug in `editor/styles/`. `deliberate_silences`: timeline seconds where silence is intended. `master`: `lufs`, `true_peak`.

## What is verified and what is not

`tests/test_editor.py` builds synthetic FFmpeg fixtures (test patterns and tones, labelled as such) and checks: EDL validation, timeline maths, the storyboard frames and change list, the approval gate (no approval, stale approval), render duration/resolution/loudness, QC failures, style analysis cut detection and Hyperframes GSAP vendoring. These prove the pipeline's mechanics, not the creative quality of an edit, which is why the owner's storyboard and final-cut approvals exist.

Not built yet: automatic best-take selection, beat detection for music sync (Mann places cuts from the music file's timings by hand), and audio judged by ear. In this cloud environment `youtube.com`, `huggingface.co` / `openaipublic.azureedge.net` (Whisper models) and `cdn.jsdelivr.net` are blocked; `mg-new` and `mg-render` copy GSAP from npm instead of the CDN.
