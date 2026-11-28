#!/usr/bin/env node
/* Vox kit QC: text over text and text over image, sampled over the whole timeline.
 *   node overlap_all.cjs <page.html> [--size 1920x1080] [--step 0.2]
 * Text = visible .tag boxes; images = img, svg.im, .cardx, .tablet, .cover. Nested boxes are ignored. */
'use strict';
const { chromium } = require('playwright'); const path = require('path');
const opt = { size: '1920x1080', step: '0.2' }, pos = [];
const a = process.argv.slice(2); for (let i = 0; i < a.length; i++) { if (a[i].startsWith('--')) opt[a[i].slice(2)] = a[++i]; else pos.push(a[i]); }
const [W, H] = opt.size.split('x').map(Number);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto('file://' + path.resolve(pos[0])); await p.waitForFunction(() => window.READY === true);
  const dur = await p.evaluate(() => window.DUR); const hits = {};
  for (let t = 0; t <= dur; t += +opt.step) {
    const r = await p.evaluate(([t, W, H]) => {
      window.__timelines.main.seek(t, false);
      const vis = n => { let o = 1; for (let e = n; e && e !== document.body; e = e.parentElement) { const c = getComputedStyle(e); if (c.visibility === 'hidden' || c.display === 'none') return 0; o *= +c.opacity; } return o; };
      const box = n => n.getBoundingClientRect();
      const on = r => r.right > 0 && r.left < W && r.bottom > 0 && r.top < H && r.width > 2 && r.height > 2;
      const texts = [...document.querySelectorAll('.tag')].filter(n => vis(n) > 0.3 && n.textContent.trim() && on(box(n)));
      const imgs = [...document.querySelectorAll('img, svg.im, .cardx, .tablet, .cover')].filter(n => vis(n) > 0.3 && on(box(n)));
      const out = [];
      const ov = (a, c) => Math.max(0, Math.min(a.right, c.right) - Math.max(a.left, c.left)) * Math.max(0, Math.min(a.bottom, c.bottom) - Math.max(a.top, c.top));
      // measure glyph extents through a range (inline text), not the block box
      const tb = n => { const kids = [...n.querySelectorAll('span')].filter(k => !k.querySelector('span') && k.textContent.trim());
        if (kids.length) { const vk = kids.filter(k => vis(k) > 0.3).map(k => k.getBoundingClientRect()); if (!vk.length) return null;
          return { left: Math.min(...vk.map(r => r.left)), top: Math.min(...vk.map(r => r.top)), right: Math.max(...vk.map(r => r.right)), bottom: Math.max(...vk.map(r => r.bottom)), get width() { return this.right - this.left; }, get height() { return this.bottom - this.top; } }; }
        const rg = document.createRange(); rg.selectNodeContents(n); const r = rg.getBoundingClientRect(); return r.width ? r : box(n); };
      // skip anything covered by a later scene (its own opaque ground): the top element at its centre must share its scene
      const sceneOf = n => n.closest('.scene');
      const shown = (n, r) => { const e = document.elementFromPoint(Math.min(W - 1, Math.max(0, (r.left + r.right) / 2)), Math.min(H - 1, Math.max(0, (r.top + r.bottom) / 2))); return !e || sceneOf(e) === sceneOf(n); };
      const TB = texts.map(tb);
      for (let i = 0; i < texts.length; i++) { const A = TB[i]; if (!A || !shown(texts[i], A)) continue; const area = A.width * A.height;
        for (let j = i + 1; j < texts.length; j++) { if (texts[i].contains(texts[j]) || texts[j].contains(texts[i])) continue; const B = TB[j]; if (!B || !shown(texts[j], B)) continue;
          if (ov(A, B) > Math.min(area, B.width * B.height) * 0.03) out.push('TEXT ' + texts[i].textContent.trim().slice(0, 24) + ' x ' + texts[j].textContent.trim().slice(0, 24)); }
        for (const im of imgs) { if (im.contains(texts[i]) || texts[i].contains(im) || !shown(im, box(im))) continue;
          if (ov(A, box(im)) > area * 0.04) out.push('IMG  ' + texts[i].textContent.trim().slice(0, 24) + ' on ' + (im.getAttribute('src') || im.className.baseVal || im.className)); } }
      return out; }, [t, W, H]);
    r.forEach(k => { (hits[k] = hits[k] || []).push(+t.toFixed(2)); });
  }
  const keys = Object.keys(hits);
  keys.forEach(k => console.log(k.padEnd(70), hits[k][0] + '-' + hits[k][hits[k].length - 1] + ' s (' + hits[k].length + ')'));
  console.log(keys.length ? keys.length + ' overlaps' : 'no text overlaps text or an image');
  await b.close(); process.exit(keys.length ? 1 : 0);
})();
