# Style sheet: Movie trailer cut

`trailer-cut` · family **cinematic** · known from: Hollywood and Bollywood trailers · status **catalog (estimated)**

Best for: announcements, launches, recap promos. Aspect 16:9 or 9:16, duration 30-120 s.

> Pace numbers are estimated starting targets, not measured. Run `/mann-style-lab` on a reference the owner shares to replace them with measured ones.

## Pace (estimated)

- Average shot 1.5s · about 6.5 cuts per 10 s · first cut by 2.0s

## Hook

A quiet line of dialogue in black, then a big image.

## Structure

Three acts: set-up, the rise with title cards, rapid montage, silence, button joke or line, title.

## Cutting

Slow first act, accelerating montage cut to the drum, hard stop to black before the button.

## Camera and framing

Best-of shots only.

## Transitions

Cuts to black, flashes on hits.

## Typography and captions

Big serif or condensed title cards between shots.

## Motion graphics

Title cards with slow push.

## Colour

Teal-orange or the film's grade.

## Sound design

Braams, risers, a slowed cover song, dramatic silence.

## VFX

Flash frames, letterbox.

## Signature moves

- three-act build
- title cards
- drum-cut montage
- silence before the button

## Avoid

- revealing the ending

## Unique twists (experiments)

- A trailer for an ordinary day

## Footage it fits

Speech any, motion mid, orientation any, footage: action, broll, talking.

## Engine defaults (`autocut --style trailer-cut`)

- Grade preset `teal-orange`
- Transition `fadeblack` every 4 cuts, 0.3s
- Zoom: every 3 clip(s), 1.0 -> 1.1
- Silence cut: pauses kept
- Music at -12 dB
- Captions: no burned captions by default
- FX every N clips: flash /6
- FX on all clips: letterbox
