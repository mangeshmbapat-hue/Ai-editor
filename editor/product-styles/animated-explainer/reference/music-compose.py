"""McDonald's explainer bed: an original 108 BPM corporate tune in C major (C-G-Am-F) played with recorded
samples from tonejs-instruments (Nicholas Brosowsky, CC BY 3.0): piano, nylon guitar and electric bass.
It builds with the story's sections and lands a big chord on 'phenomenon' (62.65 s)."""
import subprocess, sys, wave, pathlib, numpy as np
SR = 44100; LIB = pathlib.Path(sys.argv[1]); OUT = sys.argv[2]; T = 66.0
NOTES = "C Cs D Ds E F Fs G Gs A As B".split()
midi = lambda s: 12 * (int(s[-1]) + 1) + NOTES.index(s[:-1])
cache = {}
def load(p):
    if p not in cache:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        cache[p] = np.frombuffer(raw, np.float32).copy()
    return cache[p]
def note(inst, m, dur, vel=1.0, rel=0.3):
    files = {midi(p.stem): p for p in (LIB / inst).glob("*.mp3")}; base = min(files, key=lambda k: abs(k - m))
    x = load(files[base]); idx = np.arange(0, len(x) - 1, 2 ** ((m - base) / 12)); y = np.interp(idx, np.arange(len(x)), x)
    n = int((dur + rel) * SR); y = y[:n] if len(y) >= n else np.pad(y, (0, n - len(y)))
    env = np.ones(n); r = int(rel * SR); env[-r:] = np.linspace(1, 0, r); env[:64] = np.linspace(0, 1, 64); return y * env * vel
mix = np.zeros(int((T + 3) * SR))
def put(y, t, g=1.0):
    i = int(t * SR); j = min(len(mix), i + len(y)); mix[i:j] += y[: j - i] * g
beat = 60 / 108; bar = 4 * beat
CH = [[48, 52, 55, 60], [43, 47, 50, 55], [45, 48, 52, 57], [41, 45, 48, 53]]   # C G Am F
def level(t):  # how full the arrangement is, by section
    if t < 6.6: return 1      # hook: piano only
    if t < 17.0: return 2     # meet McDonald's: + guitar + bass
    if t < 25.7: return 1.5   # 1940 story: softer
    if t < 42.6: return 2.5   # Ray Kroc, global growth
    if t < 59.0: return 3     # the ecosystem: full
    return 3
b = 0
while b * bar < 62.0:
    t0 = b * bar; ch = CH[b % 4]; L = level(t0)
    for k in range(8):  # piano: 8th-note broken chord
        t = t0 + k * beat / 2; put(note("piano", ch[[0, 2, 1, 3, 2, 1, 3, 2][k]] + 12, 0.4, 0.5 if k % 2 else 0.7), t)
    if L >= 2:
        for k in (0, 2):
            put(note("bass-electric", ch[0] - 12, beat * 1.6, 0.9), t0 + k * beat)
    if L >= 1.5:
        put(sum(note("piano", m, bar, 0.22, 0.8) for m in ch[1:]), t0)   # soft pad chord
    if L >= 2.5:
        for k in (1, 3):
            put(note("guitar-nylon", ch[3] + 12, 0.3, 0.6), t0 + k * beat + beat / 2)
    if L >= 3:
        for k, m in enumerate([ch[3] + 12, ch[2] + 24, ch[3] + 24, ch[1] + 24]):
            put(note("piano", m, 0.35, 0.35), t0 + k * beat)
    b += 1
# finale: a full C major chord on "phenomenon", ringing out
put(sum(note("piano", m, 3.0, 0.9, 1.5) for m in (36, 48, 55, 60, 64, 67, 72)), 62.6)
put(note("bass-electric", 36, 2.5, 1.0, 1.0), 62.6)
# soft reversed-piano swells into each wipe (quiet)
for tw in (6.62, 17.02, 25.72, 37.02, 42.62, 52.32, 59.0):
    sw = sum(note("piano", m, 1.0, 0.3, 0.1) for m in (60, 64, 67))[::-1]; sw *= np.linspace(0, 1, len(sw)) ** 2; put(sw, tw - len(sw) / SR, 0.5)
out = mix.copy()
for d, g in ((0.09, 0.16), (0.15, 0.1), (0.23, 0.06)): out[int(d * SR):] += mix[: len(mix) - int(d * SR)] * g
out = out[: int(T * SR)]; fade = int(1.2 * SR); out[-fade:] *= np.linspace(1, 0, fade)
out /= max(1e-6, np.abs(out).max()) / 0.8
with wave.open(OUT, "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
print(OUT)
