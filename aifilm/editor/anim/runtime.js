/* Animation Editor runtime: builds the product-promo house style (editor/styles/animation-product-promo/)
 * from window.ANIM_SPEC and registers one paused GSAP timeline on window.__timelines.main, so the page is a
 * HyperFrames composition and also renders with aifilm/editor/anim/render.cjs (seek per frame, screenshot).
 * Deterministic: no random numbers, no clock, no network. Every size is a fraction of the frame width (u()).
 * Motion numbers come from the owner's 4 samples (measured at 10 fps); see the style sheet's Motion section. */
(function () {
  'use strict';
  const S = window.ANIM_SPEC, T = S.theme, W = S.width, H = S.height;
  // Sizes were measured on the 1:1 samples as fractions of the width; a tall 9:16 frame scales them up so the
  // UI reads on a phone (K), while positions stay fractions of the frame.
  const K = S.scale || (H / W > 1.5 ? 1.35 : 1);
  const u = v => v * W * K, px = v => u(v) + 'px';
  const root = document.getElementById('root');
  const tl = gsap.timeline({ paused: true });
  window.__timelines = window.__timelines || {};
  window.__timelines.main = tl;

  // ---- tiny DOM helpers ---------------------------------------------------------------------
  function el(tag, cls, parent, css, html) {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (css) Object.assign(n.style, css);
    if (html !== undefined) n.innerHTML = html;
    (parent || root).appendChild(n);
    return n;
  }
  function centre(n, x, y) { // place a node's centre at (x, y) in frame fractions of W / H
    gsap.set(n, { left: (x === undefined ? 0.5 : x) * W, top: (y === undefined ? 0.5 : y) * H, xPercent: -50, yPercent: -50 });
    return n;
  }
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const colour = c => (c && T.accents[c]) || c || T.accents.primary;

  // Built-in line icons (drawn here, no external files). Anything else is a PNG under assets/.
  const GLYPH = {
    search: '<circle cx="10" cy="10" r="6.5"/><path d="M15 15l5 5"/>',
    filter: '<path d="M4 7h16M7 12h10M10 17h4"/>',
    bolt: '<path d="M13 2L5 14h6l-1 8 8-12h-6z" fill="currentColor" stroke="none"/>',
    check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    send: '<path d="M4 12l16-8-6 16-2.5-6.5z" fill="currentColor" stroke="none"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    star: '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" fill="currentColor" stroke="none"/>',
    bike: '<circle cx="6" cy="16" r="3.5"/><circle cx="18" cy="16" r="3.5"/><path d="M6 16l4-7h5l3 7M10 9l-1.5-3H6"/>',
    bell: '<path d="M6 16V11a6 6 0 0112 0v5l2 2H4zM10 20a2 2 0 004 0"/>',
    play: '<path d="M8 5l11 7-11 7z" fill="currentColor" stroke="none"/>',
    heart: '<path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z" fill="currentColor" stroke="none"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4.5 4.5-6.5 8-6.5s7 2 8 6.5"/>',
    cup: '<path d="M5 9h11v5a5 5 0 01-5 5h-1a5 5 0 01-5-5z"/><path d="M16 10.5h1.5a2.5 2.5 0 010 5H16M8 3.5c0 1.5 1.5 1.5 1.5 3M11.5 3.5c0 1.5 1.5 1.5 1.5 3"/>',
    samosa: '<path d="M12 4L3.5 19h17z" fill="currentColor" stroke="none"/><path d="M8 15h8M12 9v3" stroke="#fff" stroke-width="1.4"/>',
    bun: '<path d="M4 15a8 8 0 0116 0z" fill="currentColor" stroke="none"/><path d="M3.5 17.5h17" /><path d="M9 11.5l1.5-1M13 10.5l1.5 1" stroke="#fff" stroke-width="1.4"/>',
    pakoda: '<path d="M6 9c2-4 9-5 12-1 3 4 0 10-5 10S3 15 6 9z" fill="currentColor" stroke="none"/><path d="M9 11l1 1M13 9.5l1 1M12 14l1 1" stroke="#fff" stroke-width="1.4"/>',
    camera: '<rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor"/>',
  };
  function icon(name, size, parent, css) {
    if (!name) return null;
    if (GLYPH[name]) {
      return el('div', 'ico', parent, Object.assign({ width: px(size), height: px(size) }, css || {}),
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' + GLYPH[name] + '</svg>');
    }
    const img = el('img', 'ico', parent, Object.assign({ width: px(size), height: px(size), objectFit: 'contain' }, css || {}));
    img.src = 'assets/' + name;
    return img;
  }

  // ---- shared moves (all durations measured on the samples) ---------------------------------
  const M = {
    popIn(n, at, o) { // blurred, small and faint -> overshoot -> settle (s1 app icon 0.0-0.3 s, cards 0.25-0.35 s)
      o = o || {};
      tl.fromTo(n, { autoAlpha: 0, scale: o.from || 0.6, filter: 'blur(' + (o.blur || 14) + 'px)', y: o.dy ? u(o.dy) : 0, rotation: o.rot || 0 },
        { autoAlpha: 1, scale: 1, filter: 'blur(0px)', y: 0, rotation: 0, duration: o.dur || 0.32, ease: o.ease || 'back.out(1.7)' }, at);
    },
    blurIn(n, at, o) { // soft reveal: faint and blurred -> sharp (text words, glass rows)
      o = o || {};
      tl.fromTo(n, { autoAlpha: 0, filter: 'blur(' + (o.blur || 10) + 'px)', y: u(o.dy === undefined ? 0.025 : o.dy), x: u(o.dx || 0), scale: o.from || 1 },
        { autoAlpha: 1, filter: 'blur(0px)', y: 0, x: 0, scale: 1, duration: o.dur || 0.25, ease: o.ease || 'power3.out' }, at);
    },
    blurOut(n, at, o) { // the house exit: grow a little, blur and fade (s3 card 0.2-0.4 s, s4 text swaps)
      o = o || {};
      tl.to(n, { autoAlpha: 0, scale: o.to || 1.08, filter: 'blur(' + (o.blur || 16) + 'px)', y: u(o.dy || 0), rotation: o.rot || 0, duration: o.dur || 0.25, ease: 'power2.in' }, at);
    },
    ring(layer, at, c) { // the ring pulse that links two UI states (s1 1.6-1.9 s, 7.5 s): a glowing ring grows and fades
      const r = el('div', 'ring', layer, { width: px(0.34), height: px(0.34), borderColor: colour(c), boxShadow: '0 0 ' + px(0.05) + ' ' + colour(c) + ', inset 0 0 ' + px(0.04) + ' ' + colour(c) });
      centre(r);
      tl.fromTo(r, { autoAlpha: 0, scale: 0.35 }, { autoAlpha: 0.85, scale: 1.0, duration: 0.18, ease: 'power2.out' }, at)
        .to(r, { autoAlpha: 0, scale: 1.7, duration: 0.3, ease: 'power1.out' }, at + 0.18);
    },
    tap(at, x, y, target) { // the hand cursor glides in, presses (the target squashes), lifts
      const c = cursor();
      tl.to(c, { autoAlpha: 1, left: x * W, top: y * H, duration: 0.45, ease: 'power3.out' }, at - 0.5)
        .to(c, { scale: 0.82, duration: 0.08, ease: 'power2.in' }, at)
        .to(c, { scale: 1, duration: 0.14, ease: 'power2.out' }, at + 0.08);
      if (target) tl.to(target, { scale: 0.93, duration: 0.08, ease: 'power2.in' }, at).to(target, { scale: 1, duration: 0.2, ease: 'back.out(3)' }, at + 0.08);
    },
    glowText(n, c) { n.classList.add(c ? 'glow-accent' : 'glow'); if (c) n.style.setProperty('--glow', colour(c)); },
  };

  let cursorNode = null;
  function cursor() {
    if (cursorNode) return cursorNode;
    cursorNode = el('div', 'cursor', root, { width: px(0.055), height: px(0.055) },
      '<svg viewBox="0 0 24 24"><path d="M9 11V4.5a1.6 1.6 0 013.2 0V10l.4-.1a1.6 1.6 0 013 .6l.3-.1a1.6 1.6 0 013 .9v4.4c0 3.4-2.4 6.3-6 6.3h-.6c-2 0-3.6-1-4.7-2.6L4.4 14a1.6 1.6 0 012.5-2z" fill="#fff" stroke="#222" stroke-width="1.3" stroke-linejoin="round"/></svg>');
    gsap.set(cursorNode, { left: 0.18 * W, top: 1.05 * H, xPercent: -30, yPercent: -10, autoAlpha: 0 });
    return cursorNode;
  }
  function hideCursor(at) { if (cursorNode) tl.to(cursorNode, { autoAlpha: 0, duration: 0.15 }, at); }

  // ---- scenes ---------------------------------------------------------------------------------
  const SCENES = {
    logo(L, s, t0, d) { // app icon: squircle pops, letters bounce in, a tap, then the ring pulse
      const box = centre(el('div', 'squircle', L, { width: px(s.size || 0.2), height: px(s.size || 0.2), background: colour(s.color) }));
      M.popIn(box, t0, { from: 0.8, blur: 18, dur: 0.3, ease: 'back.out(2.2)' });
      if (s.image) { const im = el('img', '', box, { width: '78%', height: '78%', objectFit: 'contain' }); im.src = 'assets/' + s.image; }
      else if (s.text) {
        const word = el('div', 'logo-word', box, { fontSize: px((s.size || 0.2) * Math.min(0.25, 1.45 / Math.max(s.text.length, 1))) });
        [...s.text].forEach((ch, i) => { const sp = el('span', '', word, null, esc(ch)); M.popIn(sp, t0 + 0.55 + i * 0.05, { from: 0.4, blur: 6, dy: i % 2 ? -0.02 : 0.02, dur: 0.3, ease: 'back.out(3)' }); });
      }
      if (s.tap !== false) M.tap(t0 + Math.min(1.2, d - 0.55), 0.53, 0.53, box);
      M.ring(L, t0 + d - 0.4, s.color);
      tl.to(box, { scale: 0.4, autoAlpha: 0, filter: 'blur(10px)', duration: 0.22, ease: 'power2.in' }, t0 + d - 0.42);
    },
    search(L, s, t0, d) { // a search pill grows from the ring; each phrase types in word by word
      const bar = centre(el('div', 'card pill-bar', L, { width: px(0.68), height: px(0.085) }));
      icon('search', 0.035, bar, { color: T.muted });
      const txt = el('div', 'bar-text', bar, { fontSize: px(0.03) });
      icon('filter', 0.035, bar, { color: T.muted, marginLeft: 'auto' });
      tl.fromTo(bar, { autoAlpha: 0, width: px(0.1), filter: 'blur(8px)' }, { autoAlpha: 1, width: px(0.68), filter: 'blur(0px)', duration: 0.3, ease: 'expo.out' }, t0);
      const phrases = s.phrases || [s.text || ''];
      const span = (d - 0.6) / phrases.length;
      phrases.forEach((p, k) => {
        const line = el('div', 'phrase', txt);
        const at = t0 + 0.3 + k * span;
        p.split(/\s+/).forEach((w, i) => { const sp = el('span', '', line, null, esc(w) + ' '); M.blurIn(sp, at + i * 0.09, { dy: -0.012, blur: 6, from: 1.25, dur: 0.18 }); });
        if (k < phrases.length - 1) M.blurOut(line, at + span - 0.2, { to: 1, dy: -0.02, blur: 8, dur: 0.18 });
      });
      if (s.tap !== false) M.tap(t0 + d * 0.55, 0.55, 0.53, bar);
      M.blurOut(bar, t0 + d - 0.25);
    },
    cards(L, s, t0, d) { // product cards slide in, whip-scroll with motion blur, the hero card zooms to centre
      const items = s.items || [], size = s.size || 0.25, gap = size * 1.12;
      const strip = el('div', 'strip', L); gsap.set(strip, { left: 0, top: 0.5 * H, yPercent: -50 });
      const nodes = items.map((it, i) => {
        const c = el('div', 'card product', strip, { width: px(size), height: px(size * 1.12), left: (0.5 * W - u(size) / 2 + i * u(gap)) + 'px' });
        if (it.image) { const im = el('img', '', c); im.src = 'assets/' + it.image; }
        el('div', 'label', c, { fontSize: px(size * 0.1) }, esc(it.label || ''));
        M.popIn(c, t0 + 0.08 + Math.min(i, 3) * 0.1, { from: 0.85, dx: 0.1, blur: 10, dur: 0.3 });
        return c;
      });
      const hero = Math.min(s.hero === undefined ? items.length - 1 : s.hero, items.length - 1);
      const whip = t0 + Math.max(0.6, d * 0.3);
      tl.to(strip, { x: -hero * u(gap), duration: 0.45, ease: 'power3.inOut' }, whip)
        .fromTo(strip, { filter: 'blur(0px)' }, { filter: 'blur(9px)', duration: 0.22, ease: 'power2.in', yoyo: true, repeat: 1 }, whip);
      if (hero >= 0) {
        nodes.forEach((n, i) => { if (i !== hero) tl.to(n, { autoAlpha: 0, filter: 'blur(8px)', duration: 0.25 }, t0 + d - 0.75); });
        tl.to(nodes[hero], { scale: 1.75, duration: 0.4, ease: 'expo.inOut' }, t0 + d - 0.75);
        M.blurOut(nodes[hero], t0 + d - 0.22, { to: 1.9 });
      }
    },
    button(L, s, t0, d) { // a small tilted chip grows into the accent CTA pill, glow breathing behind it
      const halo = centre(el('div', 'halo', L, { width: px(0.7), height: px(0.36), background: 'radial-gradient(closest-side, ' + colour(s.color) + '55, transparent)' }));
      const b = centre(el('div', 'pill', L, { background: colour(s.color), height: px(0.085), fontSize: px(0.032), padding: '0 ' + px(0.045) }));
      icon(s.icon || 'bolt', 0.032, b, { color: colour(s.color), background: '#fff', borderRadius: '50%', padding: px(0.006), marginRight: px(0.02) });
      el('span', '', b, null, esc(s.label || ''));
      M.popIn(b, t0, { from: 0.3, rot: -10, blur: 10, dur: 0.35, ease: 'back.out(1.6)' });
      tl.fromTo(halo, { autoAlpha: 0, scale: 0.6 }, { autoAlpha: 1, scale: 1, duration: 0.5, ease: 'power2.out' }, t0 + 0.15)
        .to(halo, { scale: 1.12, duration: 0.6, ease: 'sine.inOut', yoyo: true, repeat: 1 }, t0 + 0.65);
      if (s.tap !== false) M.tap(t0 + Math.min(1.0, d - 0.6), 0.56, 0.52, b);
      M.ring(L, t0 + d - 0.4, s.color);
      tl.to([b, halo], { autoAlpha: 0, scale: 0.7, filter: 'blur(10px)', duration: 0.22, ease: 'power2.in' }, t0 + d - 0.42);
    },
    status(L, s, t0, d) { // a white status card: title, grey line, a progress bar that fills in the accent
      const c = centre(el('div', 'card status', L, { width: px(0.66), padding: px(0.035) }));
      const head = el('div', 'status-head', c, { fontSize: px(0.034) });
      icon(s.icon || 'bike', 0.04, head, { color: colour(s.color), marginRight: px(0.015) });
      el('span', '', head, null, esc(s.title || ''));
      if (s.sub) el('div', 'sub', c, { fontSize: px(0.022) }, esc(s.sub));
      const track = el('div', 'track', c, { height: px(0.008), marginTop: px(0.03) });
      const fill = el('div', 'fill', track, { background: colour(s.color) });
      M.popIn(c, t0, { from: 0.92, blur: 12, dur: 0.3, ease: 'power3.out' });
      tl.fromTo(fill, { width: '0%' }, { width: (s.progress || 0.75) * 100 + '%', duration: Math.max(0.6, d - 0.9), ease: 'power1.inOut' }, t0 + 0.35);
      M.blurOut(c, t0 + d - 0.25, { to: 1.04, dy: 0.02 });
    },
    pill(L, s, t0, d) { // an accent pill with icon and line; leaves tilted and blurred (s1 "Arriving in 10 minutes")
      const p = centre(el('div', 'pill', L, { background: colour(s.color), height: px(0.1), fontSize: px(0.036), padding: '0 ' + px(0.05) }));
      icon(s.icon || 'bike', 0.045, p, { color: '#fff', marginRight: px(0.025) });
      el('span', '', p, null, esc(s.label || ''));
      M.popIn(p, t0, { from: 0.7, blur: 12, dur: 0.32 });
      if (s.tap) M.tap(t0 + Math.min(1.0, d - 0.6), 0.6, 0.55, p);
      M.blurOut(p, t0 + d - 0.3, { rot: -8, to: 1.05, dur: 0.3 });
    },
    chips(L, s, t0, d) { // a grid of glass chips / rows staggering in (s2 channels, s3 app dock)
      const items = s.items || [], cols = s.cols || 2, w = s.cols === 1 ? 0.6 : 0.3;
      const grid = centre(el('div', 'grid', L, { gridTemplateColumns: 'repeat(' + cols + ', ' + px(w) + ')', gap: px(0.02) }));
      items.forEach((it, i) => {
        const c = el('div', 'chip ' + (T.dark ? 'glass' : 'card'), grid, { height: px(0.07), fontSize: px(0.024), padding: '0 ' + px(0.018) });
        icon(it.icon || 'plus', 0.035, c, { color: '#fff', background: colour(it.color), borderRadius: px(0.008), padding: px(0.004), marginRight: px(0.015) });
        el('span', '', c, null, esc(it.label || ''));
        M.popIn(c, t0 + 0.1 + i * 0.06, { from: 0.85, blur: 10, dy: 0.02, dur: 0.28, ease: 'back.out(1.4)' });
      });
      M.blurOut(grid, t0 + d - 0.25, { to: 1.06 });
    },
    rows(L, s, t0, d) { // a list of rows that scrolls up with vertical motion blur (s2 "Active now" list)
      const items = s.items || [];
      const list = el('div', 'list', L, { width: px(0.62) }); gsap.set(list, { left: 0.5 * W, top: 0.3 * H, xPercent: -50 });
      items.forEach((it, i) => {
        const r = el('div', 'row ' + (T.dark ? 'glass' : 'card'), list, { height: px(0.1), marginBottom: px(0.018), padding: '0 ' + px(0.022) });
        const av = el('div', 'avatar', r, { width: px(0.06), height: px(0.06), background: colour(it.color) });
        if (it.image) { const im = el('img', '', av); im.src = 'assets/' + it.image; }
        const tx = el('div', 'row-text', r);
        el('div', 'title', tx, { fontSize: px(0.026) }, esc(it.title || ''));
        if (it.sub) el('div', 'sub', tx, { fontSize: px(0.018) }, esc(it.sub));
        M.blurIn(r, t0 + 0.05 + Math.min(i, 3) * 0.08, { dy: 0.05, blur: 10, dur: 0.3 });
      });
      const shift = Math.max(0, items.length - 3) * u(0.118);
      if (shift) {
        const at = t0 + Math.max(0.7, d * 0.4);
        tl.to(list, { y: -shift, duration: 0.5, ease: 'power3.inOut' }, at)
          .fromTo(list, { filter: 'blur(0px)' }, { filter: 'blur(7px)', duration: 0.25, ease: 'power2.in', yoyo: true, repeat: 1 }, at);
      }
      M.blurOut(list, t0 + d - 0.25, { to: 1.04 });
    },
    orbit(L, s, t0, d) { // icons fly in from outside into a ring around a centre pill, the ring turns, then spins away
      const ring = centre(el('div', 'orbit', L, { width: px(0.01), height: px(0.01) }));
      const core = centre(el('div', 'pill dark-pill', L, { height: px(0.06), fontSize: px(0.024), padding: '0 ' + px(0.035) }, esc(s.label || '')));
      M.popIn(core, t0 + 0.05, { from: 0.4, blur: 10, dur: 0.3 });
      const icons = s.icons || [], n = Math.max(icons.length, 1), R = s.radius || 0.3;
      icons.forEach((name, i) => {
        const a = (i / n) * Math.PI * 2 - Math.PI / 2;
        const box = el('div', 'orbit-item', ring, { width: px(0.075), height: px(0.075) });
        icon(name, 0.075, box, { color: colour(['primary', 'secondary', 'tertiary'][i % 3]) });
        gsap.set(box, { xPercent: -50, yPercent: -50 });
        tl.fromTo(box, { x: Math.cos(a) * u(R * 2.4), y: Math.sin(a) * u(R * 2.4), autoAlpha: 0, filter: 'blur(14px)', scale: 0.5 },
          { x: Math.cos(a) * u(R), y: Math.sin(a) * u(R), autoAlpha: 1, filter: 'blur(0px)', scale: 1, duration: 0.6, ease: 'power3.out' }, t0 + 0.15 + i * 0.03);
      });
      tl.fromTo(ring, { rotation: -70 }, { rotation: 0, duration: 0.75, ease: 'power3.out' }, t0 + 0.15)
        .to(ring, { rotation: 12, duration: Math.max(0.2, d - 1.3), ease: 'none' }, t0 + 0.9)
        .to(ring, { rotation: 140, scale: 0.35, autoAlpha: 0, filter: 'blur(10px)', duration: 0.4, ease: 'power2.in' }, t0 + d - 0.4);
      M.blurOut(core, t0 + d - 0.3, { to: 0.7 });
    },
    counter(L, s, t0, d) { // a value card: the number rolls to its value, then the card grows with an accent glow
      const card = centre(el('div', 'card counter', L, { width: px(0.34), padding: px(0.025) }));
      if (s.label) el('div', 'counter-label', card, { fontSize: px(0.022) }, esc(s.label));
      const pill = el('div', 'counter-pill', card, { fontSize: px(0.045), height: px(0.075) });
      el('span', 'pm', pill, null, '−');
      const num = el('span', 'num', pill, null, '');
      el('span', 'pm', pill, null, '+');
      const ends = el('div', 'ends', card, { fontSize: px(0.016) }); el('span', '', ends, null, esc(s.min || '')); el('span', '', ends, null, esc(s.max || ''));
      const val = { v: s.from === undefined ? 0 : s.from }, fmt = v => (s.prefix || '') + Math.round(v).toLocaleString('en-US') + (s.suffix || '');
      num.textContent = fmt(val.v);
      M.blurIn(card, t0, { from: 0.85, blur: 16, dy: 0, dur: 0.25 });
      tl.fromTo(pill, { backgroundColor: T.muted }, { backgroundColor: colour(s.color), duration: 0.2 }, t0 + 0.75)
        .to(val, { v: s.to, duration: 0.65, ease: 'power2.out', onUpdate: () => { num.textContent = fmt(val.v); } }, t0 + 0.1)
        .to(card, { scale: 1.45, boxShadow: '0 0 ' + px(0.12) + ' ' + colour(s.color) + '88', duration: 0.5, ease: 'power3.out' }, t0 + 0.95);
      M.blurOut(card, t0 + d - 0.25, { to: 0.7 });
    },
    words(L, s, t0, d) { // kinetic line: words arrive one by one with blur, accent words in colour (optionally glowing)
      const line = centre(el('div', 'words', L, { fontSize: px(s.size || 0.06), color: s.ink || '', width: (0.88 * W) + 'px' }), 0.5, s.y || 0.5);
        // accent: a list of words (all in s.color) or {word: colour} so each accent word can take its own theme colour
      const accentMap = Array.isArray(s.accent) ? Object.fromEntries((s.accent || []).map(x => [String(x).toLowerCase(), s.color])) :
        Object.fromEntries(Object.entries(s.accent || {}).map(([k, v]) => [k.toLowerCase(), v]));
      const accent = new Set(Object.keys(accentMap));
      // a "\n" in the text is a deliberate line break (balanced lines instead of a lone last word)
      const words = String(s.text || '').replace(/\n/g, ' \n ').split(/[ \t]+/).filter(Boolean);
      const step = s.step || Math.min(0.16, (d * 0.55) / Math.max(words.length, 1));
      words.forEach((w, i) => {
        if (w === '\n') { el('div', '', line, { flexBasis: '100%', height: 0 }); return; }
        const sp = el('span', '', line, null, esc(w));
        const hot = accent.has(w.toLowerCase().replace(/[^\p{L}\p{N}]/gu, ''));
        const key = w.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '');
        if (hot) { sp.style.color = colour(accentMap[key]); sp.style.fontWeight = 800; }
        if (s.glow && hot) M.glowText(sp, accentMap[key] || 'primary'); else if (s.glow === 'all') M.glowText(sp);
        const at = s.at && s.at[i] !== undefined ? t0 + s.at[i] : t0 + 0.05 + i * step;
        M.blurIn(sp, at, { dy: hot ? 0.03 : 0.018, blur: hot ? 12 : 8, from: hot ? 1.35 : 1, dur: hot ? 0.3 : 0.22 });
      });
      M.blurOut(line, t0 + d - 0.25, { to: 1.05, dy: -0.01 });
    },
    swap(L, s, t0, d) { // "Endless <word>": a fixed word, the accent word swaps up through blur, the last one grows
      const line = centre(el('div', 'words swap', L, { fontSize: px(s.size || 0.055), color: s.ink || '' }));
      el('span', 'fixed', line, null, esc(s.fixed || ''));
      const slot = el('span', 'slot', line);
      const list = s.words || [], span = (d - 0.9) / Math.max(list.length, 1);
      M.blurIn(line.firstChild, t0, { dy: 0.03, dx: 0.02, blur: 12, dur: 0.3 });
      list.forEach((w, i) => {
        const sp = el('span', 'swap-word', slot, null, esc(w));
        sp.style.color = colour(s.color);
        if (s.glow !== false) M.glowText(sp, s.color || 'glow');
        const at = t0 + 0.1 + i * span;
        tl.fromTo(sp, { autoAlpha: 0, y: u(0.04), filter: 'blur(10px)' }, { autoAlpha: 1, y: 0, filter: 'blur(0px)', duration: 0.25, ease: 'power3.out' }, at);
        if (i < list.length - 1) tl.to(sp, { autoAlpha: 0, y: -u(0.035), filter: 'blur(10px)', duration: 0.22, ease: 'power2.in' }, at + span - 0.12);
      });
      tl.to(line, { scale: 1.22, duration: 0.7, ease: 'power2.inOut' }, t0 + d - 0.95);
      M.blurOut(line, t0 + d - 0.25, { to: 1.3 });
    },
    endcard(L, s, t0, d) { // black, the white wordmark glows in, then the platform mark and handle take over
      const g = el('div', 'flash', L); tl.fromTo(g, { autoAlpha: 1 }, { autoAlpha: 0, duration: 0.12 }, t0);
      const mark = centre(el('div', 'wordmark glow', L, { fontSize: px(s.size || 0.075) }, esc(s.wordmark || s.handle || '')));
      tl.fromTo(mark, { autoAlpha: 0, scale: 0.9, filter: 'blur(18px)' }, { autoAlpha: 1, scale: 1, filter: 'blur(0px)', duration: 0.3, ease: 'power3.out' }, t0 + 0.08)
        .to(mark, { scale: 1.05, duration: 1.4, ease: 'none' }, t0 + 0.38);
      if (s.platform !== false) {
        const logo = centre(el('div', 'platform', L, { width: px(0.12), height: px(0.12) }));
        logo.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round">' + GLYPH[s.platform || 'camera'] + '</svg>' +
          '<svg class="tint" viewBox="0 0 24 24" fill="none" stroke="url(#ig)" stroke-width="2" stroke-linecap="round"><defs><linearGradient id="ig" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#f9b234"/><stop offset=".45" stop-color="#e1306c"/><stop offset="1" stop-color="#833ab4"/></linearGradient></defs>' + GLYPH[s.platform || 'camera'] + '</svg>';
        const handle = centre(el('div', 'handle', L, { fontSize: px(0.026) }, esc(s.handle || '')), 0.5, 0.5 + 0.12 * K * W / H);
        const at = t0 + Math.min(1.7, d * 0.35);
        tl.to(mark, { autoAlpha: 0.22, filter: 'blur(4px)', duration: 0.3 }, at)
          .fromTo(logo, { autoAlpha: 0, scale: 0.6 }, { autoAlpha: 1, scale: 1, duration: 0.35, ease: 'back.out(2)' }, at)
          .fromTo(logo.querySelector('.tint'), { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4 }, at + 0.6)
          .to(logo.querySelector('.tint'), { autoAlpha: 0, duration: 0.4 }, t0 + d - 0.9);
        M.blurIn(handle, at + 0.15, { dy: 0.01, blur: 6, dur: 0.3 });
      }
    },
  };

  // ---- build: ground, watermark, scenes ---------------------------------------------------------
  const ground = el('div', 'ground', root);
  const grounds = T.grounds;
  let t = 0;
  S.scenes.forEach((s, i) => {
    const d = s.dur, L = el('div', 'layer', root);
    L.dataset.start = t; L.dataset.duration = d; L.classList.add('clip');
    tl.set(L, { autoAlpha: 1 }, t).set(L, { autoAlpha: 0 }, t + d);
    const g = s.type === 'endcard' ? grounds.night || '#000' : (grounds[s.ground] || grounds[T.default_ground]);
    tl.set(ground, { background: g }, t); // grounds change on the scene boundary, never through grey
    L.style.color = /night|dark|deep/.test(s.ground || '') || s.type === 'endcard' || T.dark ? T.ink_dark || '#f2f2f7' : T.ink;
    SCENES[s.type](L, s, t, d);
    if (s.type !== 'logo' && s.type !== 'search' && s.type !== 'button' && s.type !== 'pill') hideCursor(t + 0.05);
    t += d;
  });
  if (S.watermark) { // the owner's own small handle, top right, faint (never the samples' creator mark)
    const wm = el('div', 'watermark', root, { fontSize: px(0.016) }, '<span></span>' + esc(S.watermark));
    wm.firstChild.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">' + GLYPH.camera + '</svg>';
    gsap.set(wm, { left: 0.95 * W, top: 0.06 * W, xPercent: -100 });
    tl.set(wm, { autoAlpha: 0.35 }, 0).set(wm, { autoAlpha: 0 }, t - (S.scenes[S.scenes.length - 1].type === 'endcard' ? S.scenes[S.scenes.length - 1].dur : 0));
  }
  tl.set({}, {}, t); // pin the total length
  window.DUR = t;
  tl.seek(0);
  window.READY = true;
})();
