# Session handoff

Rule (D-18): this file keeps the 10 newest sessions, newest first. At the end of a session, add a new entry at the top. Move any entry beyond the tenth to the top of `docs/session-handoff-archive.md`. Read the first entry first.

## Session 1: 2026-09-12, Claude Code

Author: Claude Code
Session: establish the documents, the skills, the agents, the registers, and the design, through two pivots. Branch `docs/foundation`, PR #1.

### What this session did, and why

- Read both reference repositories in full: the agent files, the skills, the review workflow, the handoff, the registers, and a review pair (D-23).
- Ran the repository interview, D-1 to D-25, and the roadmap interview, D-26 to D-65. Found one conflict, D-39 against D-46, and the owner settled it as D-47 (F-6, L-13).
- Wrote `CLAUDE.md` and `AGENTS.md` as identical files (D-20), five skills, two agents, the PR template, the runbook, the `LICENSE` file (D-54), and the registers.
- The gitar pass on PR #1 left two comments, both with merit. The checker now removes a one-line HTML comment (F-11), and the PR description count reads 15 files. One commit answered both, `0b2539a`, and the reply on each thread names it. The second pass approved that head. The session had claimed gitar was absent without a check (F-12), and D-66 records the owner's instruction that every PR answers the pass.
- The owner set two process rules: the session applies the `review-override` label itself after the pass approves (D-67), and asks every open question before a docs PR (D-68). The session created the label.
- The first pivot, D-78: a terminal look in a window, not a terminal. The second pivot, D-98: a sprite-based game with no terminal look at all, and the language reopened. The engine interview chose Godot 4 with C#, an engine-free Core, and the what-you-carry tool ports (D-99 to D-118). L-14 records the lesson: ask the medium question first.
- Made the sprite feasibility test (D-94): a palette and four 16 by 16 sprites as text grids. The owner said sprites are in (D-97). The grids, the 48-color palette (D-121), and the atlas landed under `content/sprites/` with the interim atlas tool at `docs/tools/make-atlas.py` (D-119).
- Archived the terminal design as `docs/archive/design-v1-terminal-2026-09-12.md` and wrote `docs/design.md` v2: the Godot shape, findings F-1 to F-18, guardrails G-1 to G-25, five phases with PR-1 to PR-40, and the sequence. PR-32 is retired.
- Replaced the `rust-conventions` skill with `csharp-conventions`, and rewrote the code rules, the build commands, the runbook, the PR template, and the glossary for Godot and C#.

### State of the build

- No code exists. The machine has .NET 10.0.400 and Godot 4.7.2 .NET at `/Applications/Godot_mono.app`.
- `main` holds the owner's root commit `6b899dd` alone, an empty `CLAUDE.md` (D-25).
- Branch `docs/foundation` holds everything else, as PR #1 (D-26, D-79). The remote head is the commit that holds this entry, checked with the session end gate before the session ended.
- The interim STE check passes on every non-exempt `.md` file. The interim atlas tool reproduces `content/sprites/atlas.png`.
- No CI exists. PR-1 creates it. The review gate does not exist. PR-3 creates it. The `review-override` label applies once the pass approves the head (D-67).

### In flight

PR #1. After each push the session posts `Gitar review`, answers the pass, and applies the label on approval. The owner then merges.

### Traps and gotchas

- The harness reminder asks for a co-author trailer in every session. D-22 forbids it, and `.claude/settings.json` sets empty strings.
- The Python checker applies the 20-word limit to every numbered list item (F-5). Keep numbered items short, or use bullets.
- Every command in `CLAUDE.md` except the interim STE check and the atlas tool waits on PR-1. Do not run `make` before it exists.
- gitar's trial quota pauses the automatic pass, so post `Gitar review` on the PR after each push and wait for the result. A push after the label removes the approval, so wait for the next pass before the label goes back on (D-67).
- The `playtest-bot` agent has no runner until PR-15. It stops and says so.
- The atlas holds the grids in file name order: cutpurse, hexer, mender, warden. The test sheet of D-94 held them in another order, and the pixels are the same.
- Thirty decisions changed in one day through D-78 and D-98. Read the `Effect` column before you cite any decision under D-99.
- The next ids are D-123, OQ-26, F-19, L-16, G-26, PR-41, M-7, and Session 2.

### Open questions that block progress

OQ-18, the world-building interview, blocks the rename (D-102) and Phase 4. OQ-3 blocks the enforced gate after PR-3. OQ-14 folds into OQ-18. Nothing blocks PR-1.

### Next concrete action

The owner merges PR #1. The next session runs the world-building interview (OQ-18) as a docs PR under D-68, then the rename PR (D-102). Then a session starts PR-1 from `main` per the Phase 1 roadmap, and writes `docs/roadmaps/phase-1-foundations.md` first with the exit tests of PR-1 to PR-6 and PR-34 and the three font candidates (D-122), under the `design-doc-style` skill.
