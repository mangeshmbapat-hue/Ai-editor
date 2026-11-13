#!/usr/bin/env node
/*
 * Render an Animation Editor composition (DOM + GSAP, window.__timelines.main) frame by frame in the
 * pre-installed headless Chromium and encode it with FFmpeg. Needs nothing from the network.
 *
 *   node render.cjs <index.html> <out.mp4> --size 1080x1080 [--fps 30] [--audio bed.wav] [--crf 16]
 *   node render.cjs <index.html> <out-prefix> --size 1080x1080 --stills 0.5,3,9.2   -> <out-prefix>_01.png, _02.png ...
 */
'use strict';
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const pos = [], opt = { fps: '30', size: '1080x1080', crf: '16' };
const argv = process.argv.slice(2);
for (let i = 0; i < argv.length; i++) { if (argv[i].startsWith('--')) opt[argv[i].slice(2)] = argv[++i]; else pos.push(argv[i]); }
if (pos.length !== 2) { console.error('usage: node render.cjs <index.html> <out.mp4|prefix> --size WxH [--fps 30] [--audio a.wav] [--stills 1,2]'); process.exit(2); }
const [W, H] = opt.size.split('x').map(Number), fps = +opt.fps;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H } });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  await page.goto('file://' + path.resolve(pos[0]));
  try {
    await page.waitForFunction(() => window.READY === true && document.fonts.status === 'loaded', null, { timeout: 60000 });
  } catch (e) { console.error('page did not get ready: ' + (errors.join('\n') || e)); process.exit(1); }
  const dur = await page.evaluate(() => window.DUR);
  const shot = async t => { await page.evaluate(t => { window.__timelines.main.seek(t, false); }, t); return page.screenshot({ type: 'png' }); };
  if (opt.stills) {
    const ts = opt.stills.split(',').map(Number);
    for (let i = 0; i < ts.length; i++) { const f = pos[1] + '_' + String(i + 1).padStart(2, '0') + '.png'; fs.writeFileSync(f, await shot(ts[i])); console.log(f); }
  } else {
    const n = Math.round(dur * fps);
    const args = ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-'];
    if (opt.audio) args.push('-i', opt.audio);
    args.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', opt.crf, '-preset', 'medium', '-r', String(fps));
    if (opt.audio) args.push('-c:a', 'aac', '-b:a', '256k', '-t', String(dur));
    args.push('-movflags', '+faststart', pos[1]);
    const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let i = 0; i < n; i++) { const buf = await shot(i / fps); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
    ff.stdin.end();
    const code = await new Promise(r => ff.on('close', r));
    if (code !== 0) { console.error('ffmpeg failed'); process.exit(1); }
    console.log(pos[1] + ' ' + n + ' frames');
  }
  if (errors.length) { console.error(errors.join('\n')); process.exit(1); }
  await browser.close();
})();
