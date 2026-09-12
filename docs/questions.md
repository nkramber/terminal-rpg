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
2. **OQ-2. Install Rust.** The dev machine has no `rustc` or `cargo`. Owner action: install rustup, then run `rustup default stable`. The runbook `docs/runbooks/dev-machine.md` gives the steps. Blocks PR-1 (D-1).
3. **OQ-3. Branch protection.** Owner action after PR-3 merges: require the CI, `ste-check`, and `review-gate` checks on `main` (D-4, D-15). A check must run once before GitHub lists it as required. Blocks the enforced gate, not the code.
4. **OQ-4. The eligible set for `review-override`.** D-16 applied `docs/`, `CLAUDE.md`, `AGENTS.md`, `.claude/`, and `.github/pull_request_template.md`. Confirm or change the set. Recommendation: keep it, because each path holds text and no executable check. Blocks PR-3, which encodes the set.
5. **OQ-5. Push policy.** Does a session push its branch and open the PR, or does the owner push? Recommendation: the session pushes and opens the PR, as in both reference repositories. The gate and gitar then read the head. Blocks the first PR of this repository. Resolved 2026-09-12: D-26, one PR after the interview, then the session pushes.
6. **OQ-6. Crate layout for PR-1.** Recommendation: one workspace with `crates/core` (the simulation, no terminal dependency), `crates/tui` (ratatui front end and the binary), and `crates/tools` (the STE checker, the lint, and the review gate). Content files live under `content/`. Blocks PR-1.
7. **OQ-7. The name.** The working title stands (D-9). A rename touches the crate, the binary, the Makefile, CI, and the docs. Blocks nothing until the owner names the game.
8. **OQ-8. D-39 against D-46.** Seeded variation in dungeons, or no concern for replay? Resolved 2026-09-12: D-47, no variation.
9. **OQ-9. Reserve experience.** Does a reserve character earn experience, and at what rate (D-58)? Recommendation: full experience, so a swap never feels like a loss. Blocks the party PR of Phase 2.
10. **OQ-10. Audio.** A terminal has the bell alone. Recommendation: no audio in region one. Blocks nothing.
11. **OQ-11. Job names.** The first four jobs and the next four (D-55). The session proposes a list in the Phase 2 roadmap, and the owner approves. Blocks the job content PRs.
12. **OQ-12. Element list.** The six to eight elements (D-43). Recommendation: fire, ice, lightning, earth, wind, water, holy, dark. Blocks the affinity PR.
13. **OQ-13. Status list.** The ten statuses (D-43). Recommendation: poison, blind, silence, sleep, slow, haste, stun, bleed, regen, shell. Blocks the status PR.
14. **OQ-14. The cast.** Five names, roles, and the story arc of region one (D-33, D-58). The session drafts, and the owner approves (D-57). Blocks the story PRs.
15. **OQ-15. The voice skill.** Approve `.claude/skills/game-text-style/SKILL.md` as the voice (D-63). Blocks the first text PR.
16. **OQ-16. A low job on a high character.** How do stats combine when a level 30 character takes a level 1 job (D-34)? Recommendation: base stats from the character level, and the job gives multipliers that grow with job level. Blocks the job PR.
17. **OQ-17. The name.** Same as OQ-7, kept as one row. See OQ-7.
