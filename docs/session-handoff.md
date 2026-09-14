# Session handoff

Rule (D-18): this file keeps the 10 newest sessions, newest first. At the end of a session, add a new entry at the top. Move any entry beyond the tenth to the top of `docs/session-handoff-archive.md`. Read the first entry first.

## Session 13: 2026-09-14, Claude Code

Author: Claude Code
Session: the gitar pass on the answer to the review of PR #4, on branch `docs/pr-4-docs-audit`.

### What this session did, and why

- Session 12 pushed `919a865` at 15:02:16Z. The pass on that head had no result when that session stopped, so this session read the result on GitHub.
- The repository activity API shows no push after `919a865`. Three `Gitar review` requests came after that push, the last at 15:36:57Z.
- Gitar edited its dashboard comment at 15:37:15Z. The comment says approved, with no issue found. The `Gitar` check run on `919a865` ended with `success` at 15:37:22Z.
- The PR holds 0 review threads, 0 line comments, and 0 reviews. The pass on `919a865` has 0 comments, 0 with merit, and no fix commit.
- The pass is complete (the `pr-review` skill, "The automated pass"). The PR adds decisions, so no `review-override` label applies (D-401).
- The handoff held ten entries, so Session 3 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).
- After the first push of this entry as `92926a6`, the session requested a pass with `Gitar review` at 15:46:41Z, 41 seconds after the push.
- Gitar ran the pass on `919a865` again, not on `92926a6`. The check run on `919a865` started at 15:46:46Z and ended with `success` at 15:47:22Z.
- Gitar deleted its dashboard comment and posted a new one at 15:47:20Z. The new comment says approved and repeats the old summary word for word.
- The check suite of gitar on `92926a6` stayed `queued`, with 0 check runs. The poll of the session waited for a check run on `92926a6`, and it failed at its time limit.
- The owner saw the new dashboard comment first. The session at first read it as a pass on `92926a6`, then the check runs showed the old head.
- This revision of the entry corrects the traps on the result of a pass. The PR description records the result of each pass on the tip.

### State of the build

- No code exists. `main` is `d29921d` (PR #3).
- PR #4 is open. The remote head is the commit that holds this entry, above `919a865`.
- The effective head stays `919a865`, because the commit that holds this entry changes the handoff files alone (the `pr-review` skill).
- The gitar pass on `919a865` is complete. The PR description records the pass on the tip that holds this entry.
- The interim STE check passes with 0 findings.

### In flight

PR #4 waits for a gitar pass on the tip that holds this entry. Then a Codex session runs the repeat review of `919a865` (the `pr-review` skill, "Repeat review procedure"). The owner merges. Then step 4 of the rename runbook starts the rename PR (D-411).

### Traps and gotchas

- Count a gitar pass only when a `Gitar` check run on the head commit starts after the request and ends. `gh api repos/{owner}/{repo}/commits/<sha>/check-runs` reads it.
- The dashboard comment is not proof. A request 3 seconds after a push ran the pass on `cb6e96e`, and a request 41 seconds after a push ran it on `919a865`.
- Each of those two dashboard comments said approved. A request 35 minutes after the push of `919a865` ran the pass on `919a865`. The shortest safe wait after a push is not known.
- A check suite of gitar in the state `queued`, with 0 check runs, means that no pass ran on that commit. `2072219`, `c73c19f`, and `92926a6` show that state.
- Gitar can edit its dashboard comment or replace it with a new one. Read the newest gitar comment that contains "Code Review".
- The REST API names the bot `gitar-bot[bot]`, and `gh pr view` names it `gitar-bot`. A filter on one exact login finds nothing in the other form.
- Automatic passes of gitar are paused for the period. Post `Gitar review` after each push, and wait for the check run on the head.
- The next ids are D-412, OQ-56, F-31, L-16, G-26, PR-43, M-7, and Session 14.

### Open questions that block progress

None for PR #4. OQ-3 waits for PR-3.

### Next concrete action

This session gets a `Gitar` check run on the tip that holds this entry, and the PR description records it. Then a Codex session runs the repeat review of PR #4 at `919a865` and updates `docs/reviews/pr-4.md`. The owner merges. Then a session runs step 4 onward of `docs/runbooks/rename-and-move.md`.

## Session 12: 2026-09-14, Claude Code

Author: Claude Code
Session: the answer to the review of PR #4, on branch `docs/pr-4-docs-audit`.

### What this session did, and why

- The review in `docs/reviews/pr-4.md` gave `Changes required` at `cb6e96e`, with P2-1 and P2-2. The session pulled the two review commits first.
- P2-1, full merit: the template of the `design-doc-style` skill numbered the status header as item 1, so every section number sat one above the headings of `docs/design.md`. The status header is now unnumbered, and the list numbers 1 to 9 match the headings.
- P2-2, full merit: the name search had no dated source in the repository. The session ran each check again and wrote the URLs, the queries, the results, and the controls into the external facts of `docs/design.md`. D-408 and the rename runbook point there.
- `docs/reviews/pr-4-response.md` records both dispositions.
- The handoff held eleven entries before this one, so Sessions 1 and 2 moved to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `d29921d` (PR #3).
- PR #4 is open. The commit that holds this entry is the new effective head, above the review commits `2072219` and `c73c19f`.
- The interim STE check passes with 0 findings, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #4 answers a new gitar pass, then takes a repeat review on the new effective head (the `pr-review` skill). The owner merges. Then step 4 of the rename runbook starts the rename PR (D-411).

### Traps and gotchas

- The USPTO search service has no public documentation. The POST body in the external facts worked on 2026-09-14, and its controls prove the `WM` field. A later change of the service can break the query.
- The EUIPO, TMview, and WIPO checks stay open for PR-40 (D-408).
- Automatic passes of gitar are paused for the period. Post `Gitar review` after each push.
- The next ids are D-412, OQ-56, F-31, L-16, G-26, PR-43, M-7, and Session 13.

### Open questions that block progress

None for PR #4. OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on the new head. Then a Codex session runs the repeat review of PR #4 and updates `docs/reviews/pr-4.md`. The owner merges.

## Session 11: 2026-09-14, Codex

Author: Codex
Session: cross-provider review of PR #4 at effective head `cb6e96e`.

### What this session did, and why

- Verified the PR target, base, merge base, branch, effective head, changed paths, provider gate, and existing PR comments.
- Read the complete diff, the design roadmap, the decision and question registers, the changed skills and agent files, the runbooks, the world files, and the PR description.
- Confirmed the automated pass approved the head with no issue comments. The local interim STE check passes with 0 findings, `git diff --check` is clean, and `AGENTS.md` and `CLAUDE.md` remain identical.
- Found P2-1: the changed `design-doc-style` skill gives section numbers that do not match `docs/design.md`.
- Found P2-2: the material name-search record has no dated primary-source links or repeatable query record in the repository documents.
- Wrote `docs/reviews/pr-4.md` with the verdict `Changes required` for `cb6e96e`.

### State of the build

- No code exists. `main` is `d29921d` (PR #3).
- PR #4 is open at `cb6e96e` on `docs/pr-4-docs-audit`.
- The interim STE check passes with 0 findings. No solution, Makefile, CI, review-gate, or Godot project exists yet.

### In flight

PR #4 waits for the author to correct P2-1 and P2-2, push the changes, request the automated pass, and take a repeat review at the new effective head.

### Traps and gotchas

- `docs/design.md` uses section 5 for the defect register, section 6 for guardrails, and section 7 for the roadmap. The changed design-doc skill says 6, 7, and 8.
- The repository name search remains tentative because EUIPO, TMview, and WIPO did not answer. PR-40 owns the later verification.
- The review record is metadata. A later metadata commit does not change the effective implementation head, but a substantive correction does.

### Open questions that block progress

None. OQ-3 remains open for branch protection and does not block this review.

### Next concrete action

Correct P2-1 and P2-2, run the focused checks and the interim STE check, then repeat the review on the new effective head.

## Session 10: 2026-09-14, Claude Code

Author: Claude Code
Session: the start of the rename runbook after PR #3 merged, then a docs PR that makes every document current before the rename PR, on branch `docs/pr-4-docs-audit`.

### What this session did, and why

- PR #3 merged as `d29921d`. The preconditions of `docs/runbooks/rename-and-move.md` held: no open PR, the SSD mounted, and the target path and the GitHub name free.
- A search for "The Thing Below" found no game on Steam and no United States mark. A free jam game on itch.io is called "The Thing Beneath", and its devlog once says "The Thing Below". The EU and WIPO registers did not answer. The owner chose to go ahead and to start now (D-408, D-409).
- Steps 1 to 3 of the runbook ran: the GitHub repository is `nkramber/the-thing-below`, and the local `origin` points at it. The owner's instruction "Ensure ALL docs are up to date before you rename/move repo" arrived after those steps. The owner kept the new name (D-410) and chose a current-state audit in its own docs PR before the rename PR (D-411).
- Three read-only audit agents read the design, the world files with the questions register, and the process files. Two scripts checked the revision notes of the decision register and the file paths in the documents. The session verified each finding against its source before a change.
- The fixes cover these files:
  - `docs/design.md`: the status header, the system map, F-2, F-3, F-9, T-4, PR-1, PR-6, PR-10, PR-14, PR-17, PR-34, PR-37, PR-40, the Phase 2 gate, and section 8.
  - `docs/questions.md`: nine notes.
  - `docs/world/`: three items.
  - `CLAUDE.md` and `AGENTS.md`: the override set and the Python exceptions.
  - The PR template, four skills, and one agent file.
  - Both runbooks, the docstring of `docs/tools/ste-check.py`, and the Rust block of `.gitignore`.
- D-78 gained its note for D-98. F-30 records the audit.
- Findings the session did not change: the open item on the two months after region one in `places.md` already defers to region two (D-353). PR-35 keeps "one hub and one dungeon" as the first nodes, because no decision says whether the village is a node.

### State of the build

- No code exists. `main` is `d29921d` (PR #3) on `nkramber/the-thing-below`.
- Branch `docs/pr-4-docs-audit` holds one commit above `main`, the commit that holds this entry.
- The interim STE check passes with 0 findings.
- The local checkout is still `~/Repos/terminal-rpg`. The documents keep the working title until the rename PR.

### In flight

PR #4, the docs audit, answers the gitar pass, then takes a Codex review, because it adds D-408 to D-411 (D-401). The owner merges. Then step 4 of the runbook starts the rename PR, and the clone to the SSD and the copy of the session notes follow (D-400, D-411).

### Traps and gotchas

- The GitHub repository has a new name. The old URL redirects, but set `origin` to `git@github.com:nkramber/the-thing-below.git` in any other checkout.
- The rename PR swaps the title and the project names alone. This PR already changed the facts about the GitHub repository in `docs/design.md` and `docs/runbooks/dev-machine.md`.
- The session notes of Claude Code key on the checkout path. Step 10 of the runbook copies the memory folder after the clone.
- Do not renumber the steps of `docs/runbooks/rename-and-move.md`: D-400 cites step 10 by number.
- `grep` on this machine is `ugrep`, which rejects a long bounded repeat such as `.{0,120}`. Use Python for a context search.
- Automatic passes of gitar are paused for the period. Post `Gitar review` after each push.
- The next ids are D-412, OQ-56, F-31, L-16, G-26, PR-43, M-7, and Session 11.

### Open questions that block progress

None for PR #4. OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on PR #4. Then a Codex session reviews PR #4 under the `pr-review` skill and writes `docs/reviews/pr-4.md` (D-401). The owner merges. Then a session runs step 4 onward of `docs/runbooks/rename-and-move.md`.

## Session 9: 2026-09-14, Codex

Author: Codex
Session: cross-provider review of PR #3 at effective head `f684ed5`.

### What this session did, and why

- Verified the PR target, base, merge base, branch, effective head, changed paths, and all three substantive commits.
- Confirmed the provider gate. The handoff identifies Claude Code as the author, and Codex is the reviewer.
- Read the complete diff, the design roadmap, the decision and question registers, the cast file, the project guidance, the atlas script, the sample readme, the five grids, and both review sheets.
- Confirmed that the sample grids have 32 rows of 32 characters, all keys exist in the 48-color palette, and the visual sheets match the stated sample.
- Confirmed that the deleted 16 by 16 files have no broken current consumer. The retained atlas script fails with the documented contextual error until PR-34 ports it.
- Wrote `docs/reviews/pr-3.md` with the verdict `Ready for owner merge`.

### State of the build

- No code exists. `main` is `7375310` (PR #2).
- The effective head is `f684ed5`. The review commit and this handoff entry are metadata commits and do not change that head.
- The interim STE check passes with 0 findings. `git diff --check origin/main...HEAD` is clean.
- PR #3 is open. The automated pass approved the final head with zero issues. No CI or review-gate checks exist yet.

### In flight

PR #3 is ready for owner merge. After merge, the next work is the rename and move in `docs/runbooks/rename-and-move.md` (D-400).

### Traps and gotchas

- Skip `docs/samples/` during automatic exploration (D-403), except when the owner or the handoff points to it.
- PR #3 is the GitHub PR number for the sprite sample. Roadmap PR-3 is the later review-gate item.
- The interim atlas tool now fails with `no .grid file` because D-405 removed the old content. PR-34 ports the tool to 32 by 32 grids.
- Automatic passes are paused for the period. The owner posted `Gitar review` after each push.

### Open questions that block progress

OQ-3 remains open for branch protection after PR-3 merges. It does not block the owner merge of this documentation PR.

### Next concrete action

Commit and push this review record and handoff. Then the owner can merge PR #3. The next session runs `docs/runbooks/rename-and-move.md` after the merge.

## Session 8: 2026-09-14, Claude Code

Author: Claude Code
Session: draft 32 by 32 cast sprites for owner review, then a small docs PR that saves the approved look as a sample and removes the 16 by 16 test sprites, on branch `docs/pr-3-sprite-sample`.

### What this session did, and why

- While PR #2 waited for its repeat review, the owner asked for new sprite sheets to review. The session drew front sprites of Marrek, Bergit, Dagvar, Ottild, and Elio at 32 by 32 in the test style (D-201, D-233, D-237, D-289), on the 48-color palette, as material maps that a scratchpad script shaded and rendered. A second draft fixed banded faces, the pick of Marrek, and the cloak of Ottild.
- The owner said that the look works and asked to save it as a sample in a small PR (D-402). The owner chose `docs/samples/`, with a rule that sessions skip the folder during automatic exploration (D-403), and the sheets and grids without the script (D-404).
- Added `docs/samples/readme.md` and `docs/samples/2026-09-14-cast-sprites/` (two sheets and five grids), the skip rule in `CLAUDE.md` and `AGENTS.md`, revision notes on D-20 and D-233, and pointers in PR-34 and `docs/world/cast.md`.
- PR #2 merged before this branch started, so the branch starts from `main` at `7375310`.
- The owner asked whether the rest of `content/sprites/` was out of date. The four 16 by 16 grids and `atlas.png` were, and the palette was not: its 48 colors stay the first 48 of the palette, and the sample uses them. The owner chose to remove the grids and the atlas in PR #3 (D-405, D-407) and to keep `docs/tools/make-atlas.py` as a reference with an out-of-date notice (D-406). The session had recommended the removal of the tool. The change adds revision notes on D-119, D-233, and D-402, and updates PR-34, `docs/samples/readme.md`, and `docs/world/cast.md`.

### State of the build

- No code exists. `main` is `7375310` (PR #2).
- Branch `docs/pr-3-sprite-sample` holds three commits above `main`: `e4a937e`, which opened PR #3, `6d8b5a7`, which splits one long sentence in `docs/samples/readme.md` that the STE check flagged, and the commit that holds this revision of the entry (D-405 to D-407).
- The interim STE check passes with 0 findings. The interim atlas tool finds no grid to read, and it carries an out-of-date notice until PR-34 ports it (D-406).

### In flight

PR #3 answers the gitar pass, then takes a Codex review, because it adds decisions (D-401). Then the owner merges. After that, the plan of Session 4 stands: the rename and the move (D-400), then the audio, release, and roadmaps docs PRs (D-399).

### Traps and gotchas

- Skip `docs/samples/` during automatic exploration (D-403).
- The branch name carries the GitHub number 3. Roadmap PR-3, the review gate, is a different item (D-13).
- Two untracked concept images sat in `content/sprites/`: `party-characters-32.png` and `party-sample-sheet-concept.png`. This session did not make them, they never entered a commit, and they are not part of D-402. The owner asked to delete them. After D-405, `content/sprites/` holds `palette.json` alone.
- The sample grids use the 48-color palette. PR-34 grows the palette to 64 (D-181, D-185), so the sample can change there.
- Automatic passes of gitar are paused for the period. Post `Gitar review` after each push.
- A multi-line guard with `set -e` did not stop at the failed STE check in this shell, so `e4a937e` went out with one STE finding. Test the exit code of each check on its own before a commit.
- `python3 docs/tools/make-atlas.py` now exits with code 1 and the message "no .grid file". That result is expected (D-405, D-406). Do not restore the 16 by 16 grids to make the tool pass.
- The next ids are D-408, OQ-56, F-30, L-16, G-26, PR-43, M-7, and Session 9.

### Open questions that block progress

None for PR #3. OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on PR #3. Then a Codex session reviews PR #3 under the `pr-review` skill and writes `docs/reviews/pr-3.md` (D-401). The owner merges. The next Claude Code session runs `docs/runbooks/rename-and-move.md` (D-400).

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
