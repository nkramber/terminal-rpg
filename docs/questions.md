# Open questions

Status: active register. Owner: Nate. Started 2026-09-12 (D-19). Written in ASD-STE100.

This file holds every open question for the owner. Each question has an id (OQ-#). The numbers never change. A resolved question stays in this file with its date and the D-# id that resolved it. The design doc (`docs/design.md`) section 9 links here.

How to file a question (D-19, D-24):

- State the question plainly.
- Give the options with their tradeoffs.
- Give a recommendation and its reason.
- Name what the question blocks.
- If the question blocks the current work, stop the session after you file it.

## Register

1. **OQ-1. Install gitar.** The session claimed the app was absent, on no check. Resolved 2026-09-12: gitar is installed, and its pass ran on PR #1 at 22:49 UTC (F-12, D-66). The trial quota pauses the automatic pass, and the comment `Gitar review` runs it (D-14).
2. **OQ-2. Install Rust.** The dev machine has no `rustc` or `cargo`. Owner action: install rustup, then run `rustup default stable`. The runbook `docs/runbooks/dev-machine.md` gives the steps. Blocks PR-1 (D-1). Closed 2026-09-12: D-99 removes Rust. The machine has .NET 10 and needs Godot 4.7.2 .NET, which what-you-carry already uses at `/Applications/Godot_mono.app`.
3. **OQ-3. Branch protection.** Owner action after PR-3 merges: require the CI, `ste-check`, and `review-gate` checks on `main` (D-4, D-15). A check must run once before GitHub lists it as required. Blocks the enforced gate, not the code.
4. **OQ-4. The eligible set for `review-override`.** D-16 applied `docs/`, `CLAUDE.md`, `AGENTS.md`, `.claude/`, and `.github/pull_request_template.md`. Confirm or change the set. Recommendation: keep it, because each path holds text and no executable check. Blocks PR-3, which encodes the set. Resolved 2026-09-12: D-71, with `.github/workflows/` added.
5. **OQ-5. Push policy.** Does a session push its branch and open the PR, or does the owner push? Recommendation: the session pushes and opens the PR, as in both reference repositories. The gate and gitar then read the head. Blocks the first PR of this repository. Resolved 2026-09-12: D-26, one PR after the interview, then the session pushes.
6. **OQ-6. Crate layout for PR-1.** Recommendation: one workspace with `crates/core` (the simulation, no terminal dependency), `crates/tui` (ratatui front end and the binary), and `crates/tools` (the STE checker, the lint, and the review gate). Content files live under `content/`. Blocks PR-1. Resolved 2026-09-12: D-69, as recommended. Superseded the same day by D-118: four C# projects.
7. **OQ-7. The name.** The working title stands (D-9). A rename touches the crate, the binary, the Makefile, CI, and the docs. Blocks nothing until the owner names the game. Resolved for now 2026-09-12: D-72, the working title stands until region one.
8. **OQ-8. D-39 against D-46.** Seeded variation in dungeons, or no concern for replay? Resolved 2026-09-12: D-47, no variation.
9. **OQ-9. Reserve experience.** Does a reserve character earn experience, and at what rate (D-58)? Recommendation: full experience, so a swap never feels like a loss. Blocks the party PR of Phase 2. Resolved 2026-09-12: D-73, half.
10. **OQ-10. Audio.** A terminal has the bell alone. Recommendation: no audio in region one. Blocks nothing. Answered 2026-09-12 with a pivot, D-78: the game leaves the terminal. Audio reopens in the pivot interview.
11. **OQ-11. Job names.** The first four jobs and the next four (D-55). The session proposes a list in the Phase 2 roadmap, and the owner approves. Blocks the job content PRs. Resolved 2026-09-12: D-76, Warden, Hexer, Mender, Cutpurse.
12. **OQ-12. Element list.** The six to eight elements (D-43). Recommendation: fire, ice, lightning, earth, wind, water, holy, dark. Blocks the affinity PR. Resolved 2026-09-12: D-74, as recommended.
13. **OQ-13. Status list.** The ten statuses (D-43). Recommendation: poison, blind, silence, sleep, slow, haste, stun, bleed, regen, shell. Blocks the status PR. Resolved 2026-09-12: D-75, as recommended.
14. **OQ-14. The cast.** Five names, roles, and the story arc of region one (D-33, D-58). The session drafts, and the owner approves (D-57). Blocks the story PRs.
15. **OQ-15. The voice skill.** Approve `.claude/skills/game-text-style/SKILL.md` as the voice (D-63). Blocks the first text PR. Resolved 2026-09-12: D-70, approved as written.
16. **OQ-16. A low job on a high character.** How do stats combine when a level 30 character takes a level 1 job (D-34)? Recommendation: base stats from the character level, and the job gives multipliers that grow with job level. Blocks the job PR. Resolved 2026-09-12: D-77, as recommended.
17. **OQ-17. The name.** Same as OQ-7, kept as one row. See OQ-7.
18. **OQ-18. The world-building interview.** The owner wants a long interview on the world, the cast, and the arc, far past fifteen questions (OQ-14). It follows the pivot interview of D-78. Blocks Phase 4 and the cast text. The setting block closed on 2026-09-12 with D-123 to D-159.
19. **OQ-19. The CRT pass against the SDL2 renderer.** D-88 wants curvature, bleed, and flicker. The SDL2 2D renderer draws textured quads and runs no shader. Asked 2026-09-12 in the pivot interview.
20. **OQ-20. Motion.** Cell-locked glyph changes, two-frame sprite flips, or sub-cell movement? The owner asked for the sprite test of D-94 first. Blocks PR-7 and the renderer design. Resolved 2026-09-12: D-97, sprites are in, and D-96 stands.
21. **OQ-21. The engine interview.** D-98 reopens the language, the engine, the presentation, the art pipeline, and the roadmap. Asked 2026-09-12 in batches.
22. **OQ-22. CRT default on the Deck.** D-105 keeps the full CRT with a toggle. Is the toggle on or off by default, and on the Deck? Recommendation: off by default everywhere, until the Deck play of Gate 2 says otherwise. Blocks PR-37. Resolved 2026-09-12: D-120, on by default.
23. **OQ-23. The pixel font.** Which OFL pixel font at 8 pixels, with a 16-pixel display variant (D-104)? Recommendation: the session proposes three candidates with their licenses in the PR-1 roadmap, and the owner picks. Blocks PR-10. Resolved in process 2026-09-12: D-122.
24. **OQ-24. The palette.** Is the 32-color test palette of D-94 the palette of D-89, as the start? Blocks PR-34. Resolved 2026-09-12: D-121, yes, grown to 48.
25. **OQ-25. The sprite test files.** Where do the script, the grids, and the PNG files of D-94 land? Blocks PR-34. Resolved 2026-09-12: D-119, under `content/sprites/`.
26. **OQ-26. The first release under D-131.** Region one is still the first release, the Steam build included (D-30, D-56). It now ends with the main story open. What form does that release take? Blocks Phase 5 and the arc block of OQ-18. Resolved 2026-09-12: D-133, a free prologue.
    - Steam Early Access, the recommendation. A buyer knows the story is not whole, and the game already ships one region at a time (D-30). Reviews judge an open story.
    - A paid first episode. It earns money at once. A buyer pays for part of a story that ends open.
    - A free prologue. It finds players early and earns nothing. Six to eight hours is a long free sample.
    - No public release until the last region. The story lands whole at launch. Phase 5 becomes a private build, and the first player waits for every region.
27. **OQ-27. The store form of the prologue.** Region one is a free prologue on Steam (D-133). Is it a demo on the store page of the full game, or a free app of its own? No recommendation until the session verifies the Steamworks rules and the fee for each form. Blocks PR-40 and the cost model. Resolved 2026-09-12: D-143, a demo of the full game.
28. **OQ-28. A prologue save in the full game.** Does a save from the free prologue load in the full game (D-62, D-133)? A save holds the run record, and a record from other content fails the version check of PR-6. Steam Cloud can share a save between a demo and its full game (D-143). Blocks PR-40, and binds the save format of PR-6. Resolved 2026-09-12: D-163, the save carries over.
    - The save carries over, the recommendation. A prologue player keeps the party and every choice. The full game needs a snapshot import with its own tests, and it builds on the snapshot of F-10.
    - The save does not carry over. The replay rule stays simple. A player plays region one again to continue.
    - The choices carry, and the party starts fresh. The full game imports the story flags alone (D-40). The import is smaller, and the party loses its levels and gear.
29. **OQ-29. The home of the effects plan.** D-139 puts 2D effects in the plan from the beginning. PR-1 creates the Godot project and its render settings, so the plan comes first. Options: this interview PR, a docs PR of its own before PR-1, or the Phase 1 roadmap. Recommendation: a docs PR of its own, because of one concern per PR (G-8). Blocks PR-1 and the effects questions. Resolved 2026-09-12: D-142, one docs PR with a full roadmap before PR-1.
30. **OQ-30. Effect motion against D-96.** D-96 says "No sub-cell movement", and D-106 locks movement to tiles. A particle or a screen shake moves by the pixel, between tiles. Does the rule bind effects? Blocks the effects plan.
    - The rule binds sprites alone, the recommendation. Sprites keep tile-locked movement, and effects move by the pixel inside the 640 by 360 frame. The pixels stay crisp, and effects gain smooth motion.
    - The rule binds every effect. Effects snap to tiles or step by frames of animation. The look stays strict, and particles look stiff.
    - The rule leaves the plan. Sprites can glide between tiles too. Motion feels smooth everywhere, and D-96 and D-106 change in part.
31. **OQ-31. Light against the palette.** D-89 says every screen picks from one palette, and D-121 sets it at 48 colors. A 2D light changes the color of a pixel, and the result leaves the palette. How does a light stay inside the palette? Blocks the effects plan.
    - Palette-locked light, the recommendation. A shader moves each lit pixel to the nearest of the 48 colors, or to a darker color on a palette ramp. The look stays authored, and M-6 measures the cost on the Deck.
    - Free light. Light blends to any color, and D-89 changes in part. The light is smooth, and the palette is no longer a rule.
    - Light through the palette alone. No 2D lights. A dark area is a darker palette index in the grid. The cost is lowest, and dynamic light is gone.
32. **OQ-32. Where an effect is defined.** D-116 makes content JSON, and G-6 bans `.tres` files. Godot keeps particle and material settings in resources. Where does an effect definition live? Blocks the effects plan.
    - JSON content, the recommendation. Game code builds the Godot objects from a schema at load (G-6). A change to an effect shows as a clean diff in review, and a bad field fails loudly. No visual editor tunes it.
    - Godot resources in Game. The editor tunes each effect by eye. G-6 and D-116 change in part, and a review reads long resource text.
    - C# code alone. Each effect is a class in Game. No schema to keep. A new effect needs a code change and a code review.
33. **OQ-33. The Godot renderer.** PR-1 sets the rendering method of the Game project. The Godot 4.7 docs mark 2D rendering as supported on Forward+, Mobile, and Compatibility. Compatibility lacks particle trails, 2D MSAA, HDR 2D, and `emit_particle()`. No official page gives advice for the Steam Deck (D-92). Blocks PR-1. Resolved in process 2026-09-12: D-160, a Deck test decides.
    - A Deck test decides, the recommendation. A small scene with particles, 2D lights, and the CRT runs on the Deck under Forward+ and under Mobile, and M-6 records the frame time. G-14 wants a measurement, and no source gives one. The test needs the owner and the Deck before PR-1.
    - Forward+. The docs show the full feature set. It targets desktop hardware, and no Deck number exists.
    - Mobile. The docs show no 2D gap. It targets weaker hardware, and no Deck number exists either.
    - Compatibility. It targets older hardware. It loses particle trails and HDR 2D, which the effects of D-139 can need.
34. **OQ-34. Papers for a licensed job.** A Mender needs a church license, and a Warden needs a guild mark (D-138, D-150). How does a character get the papers? Blocks the systems roadmap and PR-12.
    - Gold at a hub office, the recommendation. The papers cost gold once per character at a hub. Gold gains a use (D-60), and the law shows at a counter. A poor party waits for its second job.
    - Free with the job change. The papers are story texture, and no rule prices them. The simplest rule. The law has no weight in play.
    - Standing with the church or a guild. A low standing refuses the papers (D-40). The law and the factions meet in play. A bad standing can lock a party out of its healer.
35. **OQ-35. The feeding as a battle rule.** Every caster feeds the thing below a little (D-148). Does a battle rule track it? Blocks the systems roadmap.
    - No rule, the recommendation. The feeding is a story fact alone, as a down is a battle fact alone (D-135). No new system, and every spell stays a budget choice (D-42). A player never feels the cost in play.
    - A region count. Each cast adds to a hidden count per region, and a high count wakes more wrong things (D-155). The cost reaches play. A new system with balance work, and the bots must test it (D-64).
    - A cost per caster. A character who casts often gains a mark or a status. A personal cost, strong for the cast. A new rule on every caster, and it punishes the casting jobs (D-76).
36. **OQ-36. Why the bandits still roam.** The war ended six years ago, and the unpaid soldiers of D-127 still roam as bandits (D-154). What keeps them on the roads? Blocks the arc block of OQ-18.
    - Somebody pays them, the recommendation. A power hires bandits to keep the passes unsafe, and nobody can say who. It ties to the few who use the thing below (D-128), and the blood does not stop. It stays clear of the rebel brigade in `docs/world/banned-devices.md`.
    - The passes pay. Tolls, ore trains, and travelers make banditry a trade. Grounded, with no plot needed. Less weight for the story.
    - The new crown refuses them. Veterans of the old crown have no place under the treaty. It serves the class war (D-125). It sits close to a rebel cause, so it needs care against the banned brigade.
