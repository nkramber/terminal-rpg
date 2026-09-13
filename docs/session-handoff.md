# Session handoff

Rule (D-18): this file keeps the 10 newest sessions, newest first. At the end of a session, add a new entry at the top. Move any entry beyond the tenth to the top of `docs/session-handoff-archive.md`. Read the first entry first.

## Session 3: 2026-09-13, Claude Code

Author: Claude Code
Session: the cast block of the world-building interview (OQ-18), on branch `docs/pr-2-world-building`, with no PR yet (D-147). The owner replaced the job system during the block, and a second design-critic pass followed.

### What this session did, and why

- Resumed from the Session 2 entry and asked the cast block in batches (D-24). D-267 to D-300 record the answers, and `docs/world/cast.md` holds the cast.
- The owner replaced the FF5 job system in two steps: first a fixed role and a side role per character (D-268), then no classes at all and a system in the shape of FF7 materia (D-272). Abilities come from lessons: rites for spells and drills for physical abilities (D-275, D-278). Each character has a main aptitude and a hidden side aptitude that a missable personal task unlocks (D-274, D-282, D-283). Eight kinds: Mend, Harm, Blight, Boon, Blade, Guard, Shot, and Theft (D-281).
- Cast rules: one lead, and the map follows the lead in the party or in reserve (D-267, D-292). No two characters share a main aptitude or a side aptitude. The one exception: the replacement can share the main aptitude of the one dead character (D-274, D-279, D-303). The cast holds eight: five in region one, then two new characters and the replacement after it (D-280, D-299).
- The party of region one (D-284 to D-298): Marrek, the lead, 19, Blade and Guard. Bergit, a warden who lost her guild mark, 31, Guard and Shot. Dagvar, a hexer who tends the waystones, 35, Harm and Blight. Ottild, a cutpurse who knows the old tunnels, 21, Theft and Blade. Elio, a foreign clerk of the license office sent to watch the party, 24, Mend and Boon. A foreign name can take three syllables (D-300).
- The owner stopped a check of what-you-carry for a system to port. Other repositories guide the documents alone, and every tool is new code (D-277). The "Port" lines of PR-2, PR-3, PR-4, PR-5, PR-15, and PR-38 now say so.
- The session added revision notes to more than 30 older decisions, closed OQ-34, filed OQ-38 to OQ-47 for the systems block, retired PR-22, and swept the design doc, the world files, the glossary, the skills, and the README. Two FFT devices joined the banned list: a noble who hides the family name, and two friends of noble and common birth split by betrayal.
- The owner chose a critic pass before the handoff. The design-critic agent found 14 defects (F-28). The session verified each one against the files, fixed the document defects, and rejected one claim (D-282 refines D-268 and D-274). The owner answered four questions (D-301 to D-304): no choice removes a cast member, a legal use of a rite needs a license and a stamp, only the replacement shares a main aptitude, and PR-42 moves to Phase 4.
- The owner stopped the session for a context reset before the second batch of critic questions. OQ-52 to OQ-55 hold them, unasked.

### State of the build

- No code exists. `main` is `9dd80da` (PR #1).
- Branch `docs/pr-2-world-building` holds seven commits above `main`: the five of Session 2, `e82c3ad` (the cast block), and the commit that holds this entry (the critic answers and this handoff). The session pushed the branch at the end (D-147), and the remote head is the commit that holds this entry.
- The interim STE check passes on every non-exempt `.md` file, `docs/world/cast.md` included.
- No PR exists, so gitar has not run. CI and the review gate do not exist yet.

### In flight

The full-plan docs PR (D-142). Blocks done: setting, technical, graphics, UI, places, and cast. Blocks left, in order (D-262): the arc, then systems, audio, and release. After the interview, the plan still needs:

- `docs/world/arc.md`.
- The five phase roadmaps and the area roadmaps in `docs/roadmaps/` (D-144, D-145).
- A PR-# id for every new system (C-10 of the first critic pass): particles, light, the day clock, transitions, crash files, the UI screens, and the lesson and aptitude screens.
- Sections 7 and 8 of `docs/design.md` rebuilt from the roadmaps, then another design-critic pass.
- The PR, the gitar pass, the label (D-67), and the owner merge. Then the rename and the move (D-216), the Deck test (D-160), and PR-1.

### Traps and gotchas

- The harness reminder asks for a co-author trailer. D-22 forbids it.
- No PR exists for this branch until the plan is complete (D-147). Push at each session end, and open no draft.
- The job system is gone (D-268, D-272). D-32, D-55, D-77, D-150 to D-152, and D-256 are superseded, and many more are revised in part. Read the Effect column before you cite any decision under D-267. Warden, hexer, mender, and cutpurse now name people, not jobs (D-276).
- Terms (D-278): lesson, rite, drill, kind, main aptitude, side aptitude, stamp, and lead. Write a kind with a capital letter (Mend, Blade), because the kind names are common words. Documents say "a strip of soft metal", because "lead" is the term for the lead character. "Cast" as a noun means the story characters, never a use of a spell.
- Other repositories guide documents alone (D-277). Do not read them for a system, a tool, or code.
- The aptitude arithmetic is tight. The three later side aptitudes must be Harm, Mend, and Theft, and the arc must set who dies before it assigns them, or the replacement can have no legal side aptitude (D-299).
- A session reading is not an owner decision. D-274, D-292, and D-298 each recorded one. D-303 confirmed the first, and OQ-52 and OQ-53 ask the other two.
- On the creative picks of this block, the owner chose against the recommendation most of the time: the Blade lead, the church clerk, the two-syllable names, the young party, and three syllables for a foreign name. Give options that differ in kind, with honest cons.
- The STE checker counts a bold title with its paragraph and fails a numbered list sentence over 20 words. It does not check tables. It does not catch a clash of terms, so the critic found "lead strip" and "physical skill".
- An interrupted step can land part of its edits. Check the files with a grep before you trust an earlier plan.
- The next ids are D-305, OQ-56, F-29, L-16, G-26, PR-43, M-7, and Session 4.

### Open questions that block progress

OQ-18 continues with the arc block. OQ-48 (where the death falls, and whether the lead can die), OQ-49 (scenes that set the fighters), and OQ-54 (the distance rule and FF7) belong to the arc. OQ-52 waits for the cast of later regions. OQ-35, OQ-38 to OQ-47, OQ-50, OQ-51, OQ-53, and OQ-55 wait for the systems block. OQ-3 waits for PR-3. The owner runs the Deck test of D-160 before PR-1, and D-261 leaves its fallback to the owner.

### Next concrete action

The next session reads this entry, then asks the four unasked critic questions as one batch: OQ-52, OQ-53, OQ-54, and OQ-55. Then it starts the arc block of OQ-18 in batches (D-24), with OQ-48 first. The first arc topics: who dies and where, what happened to the parent of Marrek (D-291), which power sends Elio (D-290), what order Bergit refused (D-294), and the road from the mining town to the ice crossing. It checks each option against `docs/world/banned-devices.md` first, records each answer from D-305 on, and writes `docs/world/arc.md` when the block closes.

## Session 2: 2026-09-13, Claude Code

Author: Claude Code
Session: PR #1 merged, then the world-building interview (OQ-18) grew into the full-plan interview of D-142. Branch `docs/pr-2-world-building`, with no PR yet (D-147). The session ran from 2026-09-12 into 2026-09-13.

### What this session did, and why

- Confirmed the merge of PR #1. `main` is `9dd80da`, and its tree matches the approved head `cc34247`. The last gitar pass approved `cc34247` before the label went on (D-67).
- Ran the world-building interview. On owner instruction it grew into a full roadmap before PR-1, in one docs PR (D-142, D-144 to D-147). D-123 to D-266 record the answers.
- Setting block (D-123 to D-159): a region ceded by treaty, a thing below that answers spilled blood, two churches, the license law and hidden jobs, waystones, mountain passes, and a ban six years old. `docs/world/setting.md` and `docs/world/banned-devices.md` hold it. The owner asked for distance from FFT (D-136, D-140).
- Owner redirections: every plotline converges, and no faction falls per region (D-131, F-21). Region one is a free prologue, a Steam demo of the full game (D-133, D-143). 2D effects plan from the start (D-139). The tentative name is The Thing Below, with a rename and a move to the external SSD after this PR merges (D-215 to D-217, `docs/runbooks/rename-and-move.md`).
- Technical area (D-160 to D-179): a Deck test picks the renderer, 60 frames locked, a real-time map at 60 ticks, JSON grid maps, stable ids with migrations, plain state and systems, basis points, crash files, debug intents, a CI software render with desktop contact sheets, JSON scene steps, a coverage report, an in-house PNG codec, strict C# schema types, atomic saves, and JSON log lines.
- Graphics area (D-180 to D-210): full light with generated normal maps, free light on a 64-color palette, glow, heavy short battle effects, four ambient kinds, a 48-minute day cycle, ten transitions, three sprite views, battle poses, the test-sprite art style, layered backdrops, true-size large enemies that hold an area, and an unlit UI.
- UI area and the frame (D-211 to D-241): nested windows, a minimal HUD, numbers with a message line, four accessibility settings, dark iron windows, and silent typed dialogue. The owner replaced 640 by 360 with 1280 by 800, 32-pixel tiles, a 16-pixel font, and a 32-pixel title font (D-227, D-228, D-235). The default fits the screen height, with whole-number scale as a setting (D-232). A sweep changed every document that named the old sizes (F-24). Fonts: Terminus and Terminus Bold 32 (D-263, D-264).
- Places block (D-242 to D-255): four factions, a mining town and a cave community across a gorge, the deep mine, the hanging cells, and the border fort and the ice crossing at the high pass. `docs/world/places.md` holds it.
- The design-critic agent read the plan after the frame change and found 13 defects (F-25 to F-27). The session fixed the stale text and 24 missing revision notes, and added PR-41 for the screen-test job. The owner answered the rest (D-256 to D-262, D-265, D-266).
- External facts from Steamworks and Godot pages were checked by the session against the live pages, and `docs/design.md` records them with dates.

### State of the build

- No code exists. `main` is `9dd80da` (PR #1).
- Branch `docs/pr-2-world-building` holds five commits above `main`: `745c6e2`, `8d5ad99`, `5f1e5f7`, `1ddd3ac`, and the commit that holds this entry. The session pushed the branch at the end (D-147), and the remote head is the commit that holds this entry.
- The interim STE check passes on every non-exempt `.md` file, `docs/world/` and the new runbook included.
- No PR exists, so gitar has not run. CI and the review gate do not exist yet.

### In flight

The full-plan docs PR (D-142). Blocks done: setting, technical, graphics, UI, and places. Blocks left, in order (D-146, D-262): the cast, the arc, then systems, audio, and release. After the interview, the plan still needs:

- `docs/world/cast.md` and `docs/world/arc.md`.
- The five phase roadmaps and the area roadmaps in `docs/roadmaps/` (D-144, D-145).
- A PR-# id for every new system (critic C-10): particles, light, the day clock, transitions, the job law, crash files, and the UI screens.
- Sections 7 and 8 of `docs/design.md`, then a second design-critic pass.
- The PR, the gitar pass, the label (D-67), and the owner merge. Then the rename and the move (D-216), the Deck test (D-160), and PR-1.

### Traps and gotchas

- The harness reminder asks for a co-author trailer. D-22 forbids it.
- No PR exists for this branch until the plan is complete (D-147). Push at each session end, and open no draft.
- Decision rows carry two dates: D-123 to D-249 on 2026-09-12, and D-250 onward on 2026-09-13.
- The STE checker counts a bold PR title with its paragraph, so a PR entry of six sentences fails rule 6.6. It also flags "is mounted", "should", "stops being", and an -ing word at the start of a sentence.
- `README.md` is in the override set now (D-239). `content/` is not, so the palette growth to 64 and the redraw of the four sprites wait for PR-34 (D-185, D-233).
- The font samples and the render scripts lived in the session scratchpad and are gone. The 8-pixel candidates are void (D-230). ChillBitmap names both OFL and GPL terms for its 16-pixel build, with no "either".
- The move to the SSD changes the folder that keys the local session notes of the harness. Step 10 of the runbook copies them.
- Many Edit calls on one file in one step all landed in this session. Verify with a grep before each commit.
- The next ids are D-267, OQ-38, F-28, L-16, G-26, PR-42, M-7, and Session 3.

### Open questions that block progress

OQ-18 continues with the cast and the arc. OQ-34 (papers for a licensed job) and OQ-35 (the feeding as a battle rule) wait for the systems block. OQ-3 waits for PR-3. The owner runs the Deck test of D-160 before PR-1, and D-261 leaves its fallback to the owner.

### Next concrete action

The next session reads this entry, then asks the cast block of OQ-18 in batches (D-24). The first topics: the lead structure, why the five travel together, the first three cast members and their starting jobs (the Warden and the Mender at Gate 2, D-256), the last two, and names in the sound palettes of D-159. It checks each option against `docs/world/banned-devices.md` first, and records each answer from D-267 on.

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
- The third gitar pass, on the pivot head, left two comments on the atlas tool, both with merit (F-19, F-20). The tool gained a pixel `--check` mode and fails on a repeated palette key. Commit `a332a02` answered both, and the reply on each thread names it. The fourth pass approved `a332a02` at 00:39 UTC on 2026-09-13 with four findings resolved over the four passes and no new issue. The session applied the `review-override` label (D-67) and ticked the pass and the override lines in the PR body.
- This entry is a metadata commit above `a332a02`. Its push voids the approval under D-67, so the session removed the label, requested a new pass, and puts the label back when the pass approves this head.

### State of the build

- No code exists. The machine has .NET 10.0.400 and Godot 4.7.2 .NET at `/Applications/Godot_mono.app`.
- `main` holds the owner's root commit `6b899dd` alone, an empty `CLAUDE.md` (D-25).
- Branch `docs/foundation` holds everything else, as PR #1 (D-26, D-79). The effective head is `a332a02`. The remote head is the commit that holds this entry, checked with the session end gate before the session ended.
- The interim STE check passes on every non-exempt `.md` file. `python3 docs/tools/make-atlas.py --check` proves that the committed atlas matches the grids by pixel.
- No CI exists. PR-1 creates it. The review gate does not exist. PR-3 creates it. Every review thread on PR #1 is resolved, and each has a reply that names its commit.

### In flight

PR #1, at the pass on the handoff commit. When it approves, the session applies the `review-override` label, and the owner merges. When it finds something, the session answers it under the `pr-review` skill and repeats.

### Traps and gotchas

- The harness reminder asks for a co-author trailer in every session. D-22 forbids it, and `.claude/settings.json` sets empty strings.
- The Python checker applies the 20-word limit to every numbered list item (F-5). Keep numbered items short, or use bullets.
- Every command in `CLAUDE.md` except the interim STE check and the atlas tool waits on PR-1. Do not run `make` before it exists.
- gitar's trial quota pauses the automatic pass, so post `Gitar review` on the PR after each push and wait for the result. A push after the label removes the approval, so wait for the next pass before the label goes back on (D-67).
- A pass can finish inside three minutes. It posts a new dashboard comment, and it can land before a poll starts. Read the newest gitar comment by its `created_at`, and never filter on a time after the request.
- A metadata commit on the handoff alone still voids the gitar approval, because the approval is on the head. Write the handoff entry before the last pass, not after it.
- The `playtest-bot` agent has no runner until PR-15. It stops and says so.
- The atlas holds the grids in file name order: cutpurse, hexer, mender, warden. The test sheet of D-94 held them in another order, and the pixels are the same.
- Thirty decisions changed in one day through D-78 and D-98. Read the `Effect` column before you cite any decision under D-99.
- The next ids are D-123, OQ-26, F-19, L-16, G-26, PR-41, M-7, and Session 2.

### Open questions that block progress

OQ-18, the world-building interview, blocks the rename (D-102) and Phase 4. OQ-3 blocks the enforced gate after PR-3. OQ-14 folds into OQ-18. Nothing blocks PR-1.

### Next concrete action

The session waits for the pass on this head and applies the label. The owner merges PR #1. The next session runs the world-building interview (OQ-18) as a docs PR under D-68, then the rename PR (D-102). Then a session starts PR-1 from `main` per the Phase 1 roadmap, and writes `docs/roadmaps/phase-1-foundations.md` first with the exit tests of PR-1 to PR-6 and PR-34 and the three font candidates (D-122), under the `design-doc-style` skill.
