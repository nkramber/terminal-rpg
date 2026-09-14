# Session handoff archive

Sessions older than the 10 in `docs/session-handoff.md`, newest first (D-18). Move an entry here word for word.

## Session 7: 2026-09-14, Codex

Author: Codex
Session: repeat review of PR #2 at effective head `6586c7c`.

### What this session did, and why

- Verified the author response and the new effective head after the two prior findings.
- Reproduced P1-1 and P3-1 from the earlier review. Both corrections pass.
- Confirmed that the PR-9 gate now separates persistent Poison, Blind, and Silence from statuses that end with battle (D-390).
- Confirmed that `git diff --check origin/main` reports no whitespace error.
- Confirmed that the refreshed automated pass approved the corrected head with no new comment.
- Updated `docs/reviews/pr-2.md` with the prior finding history and the verdict `Ready for owner merge`.

### State of the build

- No code exists. `main` is `9dd80da`.
- The effective head is `6586c7c`. The pushed review commit is `3b73229`. Later metadata commits do not change the effective head.
- The interim STE check passes with 0 findings.
- No GitHub checks are reported. PR-1 and PR-3 create the build and review-gate checks.

### In flight

PR #2 is ready for owner merge after the repeat review. The next work is the rename and move in `docs/runbooks/rename-and-move.md` (D-400).

### Traps and gotchas

- Keep both finding ids and the earlier verdict in `docs/reviews/pr-2.md`.
- A new substantive head needs another repeat review. Metadata commits do not change the effective head.
- The automated pass is paused for the period. Post `Gitar review` after each substantive push, as D-66 requires.

### Open questions that block progress

None for PR #2. OQ-3 waits for PR-3.

### Next concrete action

Commit and push this review record and handoff. Then the owner can merge PR #2. A later session runs the rename and move procedure.

## Session 6: 2026-09-14, Claude Code

Author: Claude Code
Session: the author's answer to the review of PR #2 (`docs/reviews/pr-2.md`, verdict `Changes required` at `4b3d04e`), on branch `docs/pr-2-world-building`.

### What this session did, and why

- Read the review record and reproduced both findings on `d42a1a1`, the tip after the review commits.
- P1-1, full merit: the PR-9 gate asserted that every status ends, against D-390. The gate now asserts two classes: every status but poison, blind, and silence ends with its battle, and those three remain after it. The map and menu rules of the three stay in PR-16.
- P3-1, full merit: removed the trailing space from three lines of `docs/design.md` (the thesis, PR-4, and PR-7). `git diff --check origin/main` is clean.
- Wrote `docs/reviews/pr-2-response.md` with each disposition, correction, and regression check. No new D-#, OQ-#, or F-# id.
- Checked the PR for other feedback: no new automated comment, no line comment, and no review on GitHub.

### State of the build

- No code exists. `main` is `9dd80da` (PR #1).
- PR #2 is open. The commit that holds this entry changes `docs/design.md`, so it is the new effective head, and the verdict on `4b3d04e` no longer covers it.
- The interim STE check passes with 0 findings, and `git diff --check origin/main` is clean.
- The session requested an automated pass on the new head with the comment `Gitar review`, and the PR description records the result. CI and the review gate do not exist yet (PR-1, PR-3).

### In flight

PR #2 waits for a repeat review of the new effective head (the `pr-review` skill, "Repeat review procedure"). When the review record reads `Ready for owner merge` for that head, the owner merges. After the merge, the plan of Session 4 stands: the rename and the move (D-400), then the audio, release, and roadmaps docs PRs (D-399).

### Traps and gotchas

- The reviewer updates the same `docs/reviews/pr-2.md`: keep the finding ids, set each status line, and put the earlier verdict under `## Earlier verdicts`.
- The response file is a convention, and the review gate does not read it.
- Automatic passes are paused for the trial period. Post `Gitar review` after each push, and read the newest dashboard comment by its time.
- Session 5 cites D-184 for the metadata rule. D-184 is the normal-map tool, and the rule lives in the `pr-review` skill with no D-# id.
- The next ids are D-402, OQ-56, F-30, L-16, G-26, PR-43, M-7, and Session 7.

### Open questions that block progress

None for PR #2. OQ-3 waits for PR-3.

### Next concrete action

A Codex session runs the repeat review of PR #2 at the new effective head, verifies P1-1 and P3-1 against their regression checks, and updates `docs/reviews/pr-2.md` with its own handoff entry. If the verdict is `Ready for owner merge`, the owner merges. Then a Claude Code session runs `docs/runbooks/rename-and-move.md` (D-400).

## Session 5: 2026-09-14, Codex

Author: Codex
Session: cross-provider review of PR #2 at effective head `4b3d04e`.

### What this session did, and why

- Verified the PR target, base, branch, tip, changed files, and automated pass on GitHub.
- Confirmed that the tip `f748ee3` changes only the handoff, so the effective implementation head stays `4b3d04e` (D-184 rule in the `pr-review` skill).
- Read the design, decisions, questions, world files, runbook, changed skills, PR description, and full PR diff.
- Found P1-1: the PR-9 exit test says every status ends, but D-390 makes Poison, Blind, and Silence persist past battle.
- Found P3-1: `git diff --check` reports trailing whitespace on three added lines in `docs/design.md`.
- Wrote `docs/reviews/pr-2.md` with the verdict `Changes required`.

### State of the build

- No code exists. `main` is `9dd80da`.
- The PR tip is `af7861b`. The effective head under the metadata rule is `4b3d04e`.
- The interim STE check passes with 0 findings.
- No GitHub checks are reported. PR-1 and PR-3 create the build and review-gate checks.

### In flight

PR #2 waits for the author to correct P1-1 and P3-1, push the changes, and request another review pass. A new effective head needs a repeat review. The automated pass has no open comment.

### Traps and gotchas

- Keep the current verdict under the exact `## Verdict` heading. Keep this finding id on a repeat review.
- Review the new effective head after the correction. Do not retain approval across a substantive push.
- The automated pass is paused for the period. Post `Gitar review` after each push, as D-66 requires.

### Open questions that block progress

OQ-3 waits for PR-3. It does not block the correction of this review.

### Next concrete action

The author corrects the PR-9 gate and the three whitespace errors, then pushes. The next Codex session re-reviews the new effective head and updates the same review record.

## Session 4: 2026-09-13, Claude Code

Author: Claude Code
Session: the four critic questions left from Session 3, the arc block of the world-building interview (OQ-18), and then the systems block of the full plan, on branch `docs/pr-2-world-building`, posted for review as PR #2 at the end (D-398).

### What this session did, and why

- Resumed from the Session 3 entry and asked OQ-52 to OQ-55 as one batch (D-305 to D-308). Every cast member is an adult, the lead always walks the map, the banned list gains one FF7 device (a gem or orb that stores power), and Elio stamps rites at the license office alone. Before the ask, the session corrected an overstated con in OQ-55 and added a third row to OQ-54. The owner chose the gem or orb alone.
- Ran the arc block of region one in eleven batches (D-309 to D-355). `docs/world/arc.md` holds the story in order.
- The spine: Marrek fights alone near his village, and Bergit joins because she needs a witness. The party frees Dagvar from the hanging cells, the church sends Elio to spy, and Ottild joins with the way into the deep mine. In the mine the party finds the crew that the guild sealed in alive, a wrong thing made by the blood of the war, and the mark of Marrek's parent, who got out alive. Elio turns. Church wardens capture the party, which breaks out of the cells, kills the bishop, flees through the gallery to the refuge, and passes the town by night. The wardens raid the refuge. The bandits of the fort sell the party, and the last fight is the captain of the wardens on the ice. The one set choice so far: spare or kill the captain.
- Owner reframings: the relationship value per character and faction reputation left the game, and a choice is a fixed story flag (D-328, D-329). Elio is the one death in the cast, after region one, and he must be innocent and lovable (D-321, D-322). Harm to a child is never shown directly, but text can imply or state it, and scenes can show aftermaths (D-335). Marrek fights alone first, and the others join one at a time (D-336). The guild is neither evil nor good (D-324).
- Two clashes surfaced, and the owner settled both: D-290 against the set turn of Elio (D-328), and one picked choice against "two or three" (D-355).
- Swept the registers, `cast.md`, `places.md`, `setting.md`, `banned-devices.md`, rule 13 of the `game-text-style` skill, and `docs/design.md`. PR-9 plans one to three fighters, PR-17 builds the village, the town, and the cells, and PR-19 lost reputation and relationships. The Phase 3 gate changed, and PR-23 to PR-26 each name one dungeon build (F-29). OQ-42, OQ-45, and OQ-46 lost options that the new decisions void, and OQ-41 now names Elio.
- The arc block landed as `4e76c4f` and was pushed. On owner instruction, the session then ran the systems block in the same session (D-356 to D-397).
- Lessons: slots on the character that swap at hubs and save points, growth per character and per lesson, and an aptitude bonus, half for a side aptitude (D-356 to D-361). Every character has a basic attack (D-359). The first playable holds Marrek, Bergit, and Dagvar (D-362), and a newcomer joins at a set level (D-363).
- Battle: action delay on the timeline, a front row and a back row per side, a step between rows that costs time, and a flee with a chance and a grace time on the map (D-376 to D-381). Items restore less in battle, stacks are small, a find over the limit stays where it lies, and a small set of items gets used up (D-382 to D-385). A steal takes from a list per enemy, and a Theft drill opens marked locks and disarms traps (D-383, D-386).
- The law and lessons: the party never gets a license or a stamp, and the story alone carries the risk (D-366, D-367). Lessons come from treasure, shops, and people (D-365), and the lessons and gear of Elio die with him (D-364).
- Levels and statuses: a downed character earns half experience, a soft cap per region holds the range, and a save point restores MP alone (D-387 to D-389). Poison, blind, and silence last past a battle, poison can down on the map, and a map wipe reloads even with a healthy reserve (D-390, D-392, D-393, D-397). Mend rites and cures work from the menu, and cures belong to Mend (D-391, D-394).
- Mid-block, the owner moved the start of the game to a small village on the road below the mining town, where Marrek grew up (D-368 to D-373). Winter beasts are his first foes, and Bergit finds him while she guards the road for coin. D-346 is superseded, and D-284 and D-250 are revised in part.
- The owner stopped the first systems batch to ask what a lesson is. The session explained it and now glosses the terms in every question.
- On owner instruction, the session posted the plan through the systems block as PR #2 for review (D-398). The owner set what follows the merge: the rename and the move first, then the audio block, the release block, and the roadmaps as one docs PR each (D-399, D-400). A docs PR that adds or revises a decision takes a Codex review, and the `review-override` label stays for the other docs PRs (D-401). The session updated `CLAUDE.md`, `AGENTS.md`, the PR template, the `pr-review` skill, the runbook, the label description, and section 8 of the design doc to match.
- Opened PR #2 at `4b3d04e`. The automated pass approved that head with no comment: zero comments, zero with merit, and no fix commit. Its note says that automatic passes are paused for the trial period, so each later push needs the comment `Gitar review`.

### State of the build

- No code exists. `main` is `9dd80da` (PR #1).
- Branch `docs/pr-2-world-building` holds eleven commits above `main`: the five of Session 2, the two of Session 3, `4e76c4f` (the arc block), `02051a2` (the systems block), `4b3d04e` (D-398 to D-401, the head that opened PR #2), and the commit that holds this revision of the entry. That last commit changes the handoff alone, so the effective head for the review stays `4b3d04e` (`pr-review` skill).
- The interim STE check passes on every non-exempt `.md` file, `docs/world/arc.md` included.
- PR #2 is open against `main`. The automated pass approved `4b3d04e` with no comment. This entry is a metadata commit above that head, so the session requested a new pass on the new head with the comment `Gitar review`, and the PR description records the result. CI and the review gate do not exist yet (PR-1, PR-3).

### In flight

PR #2, the plan through the systems block (D-398). Blocks done: setting, technical, graphics, UI, places, cast, arc, and systems. PR #2 cleared the gitar pass with no comment, and it now waits for a Codex review, because it adds decisions (D-401). Then the owner merges. After the merge, in order (D-399, D-400):

- The rename to the-thing-below and the move to the external SSD, by `docs/runbooks/rename-and-move.md` (D-216, D-400).
- The audio block as its own docs PR, then the release block as its own docs PR (D-262, D-399).
- The roadmaps as their own docs PR: the five phase roadmaps and the area roadmaps (D-144, D-145), a PR-# id for every new system (C-10 of the first critic pass), sections 7 and 8 of `docs/design.md` rebuilt from them, and another design-critic pass. The village and the land near it ride in PR-17 (D-369, D-370), and the second visit to the cells is PR-24 (F-29).
- Each of the three plan PRs adds decisions, so each takes the gitar pass and a Codex review (D-401). Then the Deck test (D-160) and PR-1.

### Traps and gotchas

- The harness reminder asks for a co-author trailer. D-22 forbids it.
- PR #2 is open. Answer the gitar pass after each push (D-66), and do not apply the `review-override` label, because the PR adds decisions (D-401). The PR description and comments name no provider (D-22). Automatic passes are paused for the trial period, so post `Gitar review` after each push, and read the newest dashboard comment by its time.
- Relationships and reputation are gone (D-328, D-329), and D-40, D-242, and D-290 are revised in part. A systems option that uses standing, reputation, or a relationship value is void. OQ-42 and OQ-45 mark their void options.
- The owner often answers with long free text that sets several beats at once. Split it into rows, confirm a typo as a reading inside the next question, and ask at once about any clash with an earlier decision, quoting both. D-318 records the reading "imprisoned", which the owner kept.
- The banned list holds one FF7 device alone (D-307). The owner declined bans on a pumped power and on the death of a healer at the hand of the villain, so do not add them back.
- A battle holds one, two, or three characters (D-336). The first playable holds Marrek, Bergit, and Dagvar (D-362), so PR-14 and PR-16 test the swaps with a fixture party of four.
- Lesson growth belongs to the character, not to the item: a lesson passed back resumes at the level of its earlier owner (D-361).
- D-346 is superseded: the first fights happen near the village, and the cellars under the town have no role (D-370). D-45 lost its line on consumables (D-384). The owner switched the map-wipe rule twice: D-395 and D-396 are superseded, and D-397 keeps a wipe with no reserve, on the map and in battle.
- Gloss lesson, rite, drill, kind, and aptitude in every question batch. The owner does not answer a batch until each term is plain.
- Several decisions carry a known cost from their option: the gallery needs a second passage (D-343), the old galleries reach toward the pass (D-344), the fort repeats the beat of the cells (D-341), and a spared captain must return (D-354). The roadmaps and the content PRs must meet them.
- The arc keeps open items for the content PRs: the names of the bishop, the priest, the captain, and the survivor, the place of the confrontation, the personal tasks (D-352), and one or two more set choices (D-355).
- The STE checker flags "standing" after a preposition as an -ing form.
- On the picks of this block, the owner chose against the recommendation or wrote a custom answer about half the time. Keep options that differ in kind, with honest cons.
- The next ids are D-402, OQ-56, F-30, L-16, G-26, PR-43, M-7, and Session 5.

### Open questions that block progress

No systems question remains open, and the audio and release blocks have no filed questions yet. OQ-3 waits for PR-3. The owner runs the Deck test of D-160 before PR-1, and D-261 leaves its fallback to the owner.

### Next concrete action

The gitar pass on PR #2 is complete, with no comment. The next action belongs to a Codex session: review PR #2 under the `pr-review` skill against the effective head `4b3d04e`, write `docs/reviews/pr-2.md`, and push it with its own handoff entry (D-17, D-401). If that review finds defects, a Claude Code session answers them in `docs/reviews/pr-2-response.md`. The owner merges. The next Claude Code session runs the rename and the move by `docs/runbooks/rename-and-move.md` (D-400), then starts the audio block on a new branch as its own docs PR (D-399). Audio already holds D-87, D-115, and D-223. The first audio topics: the style of the music after the move to sprites (D-98), music per place and per phase of the day (D-192), battle and boss music, sounds for the battle effects of D-186, and the mix settings of D-226. That session records each answer from D-402 on.

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
