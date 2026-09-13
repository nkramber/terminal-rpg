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
18. **OQ-18. The world-building interview.** The owner wants a long interview on the world, the cast, and the arc, far past fifteen questions (OQ-14). It follows the pivot interview of D-78. Blocks Phase 4 and the cast text.
19. **OQ-19. The CRT pass against the SDL2 renderer.** D-88 wants curvature, bleed, and flicker. The SDL2 2D renderer draws textured quads and runs no shader. Asked 2026-09-12 in the pivot interview.
20. **OQ-20. Motion.** Cell-locked glyph changes, two-frame sprite flips, or sub-cell movement? The owner asked for the sprite test of D-94 first. Blocks PR-7 and the renderer design. Resolved 2026-09-12: D-97, sprites are in, and D-96 stands.
21. **OQ-21. The engine interview.** D-98 reopens the language, the engine, the presentation, the art pipeline, and the roadmap. Asked 2026-09-12 in batches.
22. **OQ-22. CRT default on the Deck.** D-105 keeps the full CRT with a toggle. Is the toggle on or off by default, and on the Deck? Recommendation: off by default everywhere, until the Deck play of Gate 2 says otherwise. Blocks PR-37. Resolved 2026-09-12: D-120, on by default.
23. **OQ-23. The pixel font.** Which OFL pixel font at 8 pixels, with a 16-pixel display variant (D-104)? Recommendation: the session proposes three candidates with their licenses in the PR-1 roadmap, and the owner picks. Blocks PR-10. Resolved in process 2026-09-12: D-122.
24. **OQ-24. The palette.** Is the 32-color test palette of D-94 the palette of D-89, as the start? Blocks PR-34. Resolved 2026-09-12: D-121, yes, grown to 48.
25. **OQ-25. The sprite test files.** Where do the script, the grids, and the PNG files of D-94 land? Blocks PR-34. Resolved 2026-09-12: D-119, under `content/sprites/`.
