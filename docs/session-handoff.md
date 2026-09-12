# Session handoff

Rule (D-18): this file keeps the 10 newest sessions, newest first. At the end of a session, add a new entry at the top. Move any entry beyond the tenth to the top of `docs/session-handoff-archive.md`. Read the first entry first.

## Session 1: 2026-09-12, Claude Code

Author: Claude Code
Session: establish the documents, the skills, the agents, the registers, and the design. Branch `docs/foundation`.

### What this session did, and why

- Read both reference repositories in full: the agent files, the skills, the review workflow, the handoff, the registers, and a review pair (D-23).
- Ran the repository interview: rules, language, and process. The answers are D-1 to D-25. Three answers came as "recommend the best", and the session chose T-7, the five determinism guardrails, and RON (D-5, D-6, D-7).
- Ran the roadmap interview: setting, structure, combat, party, jobs, progression, death, exploration, decisions, magic, gear, loot, screen, input, gates, license, distribution, content scale, cast, hubs, economy, difficulty, enemy AI, saves, voice, and bots. The answers are D-26 to D-65.
- Found one conflict, D-39 against D-46, quoted both, and the owner settled it as D-47 (F-6, L-13).
- Wrote `CLAUDE.md` and `AGENTS.md` as identical files (D-20), five skills, two agents, the PR template, the runbook, the `LICENSE` file (D-54), and the registers.
- Copied the decktome STE checker to `docs/tools/ste-check.py` as the interim checker (D-10). The MtG names left its allow list, and game names entered it.
- Wrote `docs/design.md` v1: thesis, lessons, system map, cost model, findings F-1 to F-10, tenets, guardrails G-1 to G-22, five phases with PR-1 to PR-33, and the sequence.
- Ran the checker over every document, skill, and agent file, and corrected each finding.
- The gitar pass on PR #1 left two comments, both with merit. The checker now removes a one-line HTML comment (F-11), and the PR description count reads 15 files. One commit answered both, and the reply on each thread names it. The session had claimed gitar was absent without a check (F-12), and D-66 records the owner's instruction that every PR answers the pass.

### State of the build

- No Rust code exists. Rust is absent from the machine (OQ-2).
- `main` holds the owner's root commit `6b899dd` alone, an empty `CLAUDE.md` (D-25).
- Branch `docs/foundation` holds everything else, as one PR (D-26). The remote head is the commit that holds this entry, checked with the session end gate before the session ended.
- The interim STE check passes on every non-exempt `.md` file.
- No CI exists. PR-1 creates it. The review gate does not exist. PR-3 creates it. The owner reads this PR by hand and merges with the `review-override` label, or asks for a Codex review of the documents.

### In flight

The docs PR. The owner reads it, answers the owner actions in `docs/questions.md`, and merges.

### Traps and gotchas

- The harness reminder asks for a co-author trailer in every session. D-22 forbids it, and `.claude/settings.json` sets empty strings.
- The Python checker applies the 20-word limit to every numbered list item (F-5). Keep numbered items short, or use bullets.
- Every command in `CLAUDE.md` except the interim STE check waits on PR-1. Do not run `make` before it exists.
- The `review-gate` check does not exist yet (PR-3). gitar is installed. Its trial quota pauses the automatic pass, so post `Gitar review` on the PR after each push and wait for the result.
- The `playtest-bot` agent has no runner until PR-15. It stops and says so.
- Every roadmap entry after PR-6 assumes the crate layout of OQ-6. A different answer renames the crates in `CLAUDE.md`, the skills, and this file.
- The next ids are D-67, OQ-18, F-13, L-14, G-23, and Session 2.

### Open questions that block progress

OQ-2 and OQ-6 block PR-1. OQ-15 blocks the first text PR. OQ-9, OQ-11, OQ-12, OQ-13, and OQ-16 block Phase 2 PRs. OQ-14 blocks Phase 4. OQ-3, OQ-4, OQ-7, and OQ-10 block nothing today.

### Next concrete action

The owner merges the docs PR, installs Rust, creates the `review-override` label, and answers OQ-6. A fresh session then starts PR-1 from `main` per the Phase 1 roadmap. That session writes `docs/roadmaps/phase-1-foundations.md` first, with the exit tests of PR-1 to PR-6, under the `design-doc-style` skill.
