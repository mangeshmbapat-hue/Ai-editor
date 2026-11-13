#!/usr/bin/env node
/* Animation Editor QC (owner rule 2026-11-13): no text may sit on an image at any moment.
 *   node overlap.cjs <page.html> --size 1920x1080 [--step 0.25]
 * Seeks the timeline every `step` seconds and reports every visible text box (.hl word spans, .chip, .tag, .nlabel)
 * that overlaps a visible image box (img, .badge, .phone, .node, svg drawings except full-frame ones) by more than
 * 4 % of the text's area. Exit code 1 when anything overlaps. */
'use strict';
const { chromium } = require('playwright');
const path = require('path');
const opt = { size: '1920x1080', step: '0.25' }, pos = [];
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
      const texts = [...document.querySelectorAll('.hl span, .chip, .tag, .nlabel')].filter(n => vis(n) > 0.35 && n.textContent.trim());
      const imgs = [...document.querySelectorAll('img, .badge, .phone, .node, svg.line:not(.connector)')].filter(n => {
        if (n.closest('.chip, .tag, .badge') && n.tagName !== 'DIV' && !n.classList.contains('badge')) return false;
        const r = box(n); return vis(n) > 0.35 && r.width * r.height < W * H * 0.6 && r.width > 4; });
      const out = [];
      for (const tx of texts) { const a = box(tx); const A = a.width * a.height; if (!A) continue;
        for (const im of imgs) { if (im.contains(tx) || tx.contains(im)) continue; const c = box(im);
          const ix = Math.max(0, Math.min(a.right, c.right) - Math.max(a.left, c.left)), iy = Math.max(0, Math.min(a.bottom, c.bottom) - Math.max(a.top, c.top));
          if (ix * iy > A * 0.04) out.push(tx.textContent.trim().slice(0, 30) + '  ON  ' + (im.getAttribute('src') || im.className.baseVal || im.className || im.tagName).toString().slice(0, 40)); } }
      return out; }, [t, W, H]);
    r.forEach(k => { (hits[k] = hits[k] || []).push(+t.toFixed(2)); });
  }
  const keys = Object.keys(hits);
  keys.forEach(k => console.log(k.padEnd(80), hits[k][0] + '-' + hits[k][hits[k].length - 1] + ' s'));
  console.log(keys.length ? keys.length + ' overlaps' : 'no text overlaps an image');
  await b.close(); process.exit(keys.length ? 1 : 0);
})();
