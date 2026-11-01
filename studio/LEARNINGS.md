# Studio learnings

The owner's standing rules for the studio agents (social, researcher, writer, director) and the orchestrator. Every agent reads this file before working. **The newest explicit rule wins.** Entries are added with the `studio-learn` skill.

Format: `- YYYY-MM-DD · kind · rule. Why: … Source: "<owner's words>" (project)`. The kind is `owner` (the owner said it), `result` (real performance numbers) or `observed` (a check we ran).

## Global
- 2026-11-01 · owner · The director/orchestrator never writes the script. A separate writer agent writes it, it is critiqued, and the owner approves it before any voice, music, picture or render work. Why: earlier scripts were weak. Source: "tumhari script bhut bekar hoti h ... ai writer agent se likhvao ... phle script approval le. fir kaam kre" (studio)
- 2026-11-01 · owner · Work as a coordinated team: viral topics → research → script → style, format and duration → making. Agents coordinate through the project files, not in isolation. Source: "ye sab agent ek dusre se cordinate kreke hi kaam kre" (studio)
- 2026-11-01 · owner · Record every piece of owner feedback in this file and apply it from then on (the `studio-learn` skill). Source: "jo jo chije batata jau usko update krte jao" (studio)
- 2026-11-01 · owner · Talk to the owner in Hinglish. Execute clear tasks without asking permission for routine choices; ask only when the answer changes the result. The script and final-cut gates are the owner's rules, not optional questions. Source: owner preferences (all)
- 2026-11-01 · owner · For a big batch (many styles, many videos), show the list or plan first, then build. Source: "phle list niklao" (style library)
- 2026-11-01 · observed · Run at most 3 agents in parallel. Why: seven parallel agents exhausted the owner's 5-hour usage limit. (style library)
- 2026-11-01 · observed · In the cloud environment, `api.elevenlabs.io`, Hugging Face (Whisper models), Microsoft edge-tts and en.wikipedia.org (WebFetch) are blocked unless the owner allows them in the environment's network settings. WebSearch works. (all)

## Social
- 2026-11-01 · owner · Never publish, schedule, comment, DM or edit a profile. Drafts only. Source: owner's AI Socials rules (all)
- 2026-11-01 · owner · Caption voice: Hinglish by default on Instagram and Facebook; no em dashes; avoid AI clichés ("game-changer", "unlock", "delve", "seamless", "let's dive in", "it's not just X, it's Y"). Source: owner's voice anchor (all)

## Research
- 2026-11-01 · owner · Real-event and myth videos need every on-screen and spoken claim sourced; label myth or tradition variants (for example, "popular Diwali retelling" vs Valmiki). Source: owner's projects (Azaadi 1947, Ramayana)

## Writer
- 2026-11-01 · owner · Scripts must use hooks, holds, open loops, suspense, cliffhangers or loop endings, everything a video needs to go viral. No plot-summary narration, and never narrate what is already on screen. Why: the Ramayana narration read like a synopsis. Source: "jisko hooks, hold, cliffagnger, suspense sab trike ki jo viral hone k liye jruri sab aaye" (studio)

## Director
- 2026-11-01 · owner · The director handles the whole creative and art direction and keeps the video in flow, from edit to final product. Source: "ek director agent jo puri video ka creative art direction dekhe ... edit se lekr final product" (studio)
- 2026-11-01 · owner · For "preview dikhao", show individual numbered frames, not one dense contact sheet. Source: owner's director overrides (all)
- 2026-11-01 · owner · The owner liked the Tholu Bommalata (Indian leather shadow puppet) look for the Ramayana preview. Source: "badiya h ye to" (ramayana)

## Production
- 2026-11-01 · owner · BGM, voice, SFX and foley must be top quality. Source: "make sure ki ... bgm or voice sfx foiley vo top quality ka ho" (ramayana)
- 2026-11-01 · owner · Synthetic sound effects felt odd (noise-based crowd, synthesised bells, beeping crickets). Prefer recorded samples; avoid synthetic crowd, insects and beeps. Source: "isme sound effect thode odd h" (azaadi-1947)
- 2026-11-01 · owner · Use ElevenLabs for voice and SFX when it is reachable. The key lives only in the environment variable `ELEVENLABS_API_KEY`, never in chat or files. Source: "isko use krke sound or voice over banaya kro" (all)
