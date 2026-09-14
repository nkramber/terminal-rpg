# Session handoff

Rule (D-18): this file keeps the 10 newest sessions, newest first. At the end of a session, add a new entry at the top. Move any entry beyond the tenth to the top of `docs/session-handoff-archive.md`. Read the first entry first.

## Session 17: 2026-09-14, Claude Code

Author: Claude Code
Session: the audio block of the full plan, and the change to a time of day that the story sets, on branch `docs/pr-7-audio-block`.

### What this session did, and why

- PR #6 merged as `11498f1`. On the owner instruction "continue work", the same harness run started the audio block, the next docs PR of D-399.
- The owner asked when a build to play and feel comes. From section 7 of `docs/design.md`: PR-7 is the first build to walk in, PR-10 and PR-11 give fights, and PR-17 is the first playable.
- PR-17 comes after three docs PRs and 23 code PRs. At 2 to 4 sessions per reviewed PR, that is about 50 to 100 sessions.
- The session named three levers for the roadmaps PR: the release docs PR later, PR-2 and PR-3 after PR-7, or a throwaway feel prototype. The owner chose none yet.
- The audio block ran in eight batches:
  - Style: 16-bit synthesized instrument voices for the music and the sound effects (D-412, D-423). D-87 keeps our own tool and no licensed sound.
  - Music everywhere: place tracks, three battle tracks per region, mood cues and key cues for scenes, and ten themes in region one (D-413, D-415, D-418, D-419).
  - Stings for a wipe, a level up, a victory, and a key find. Ambience under the music, map sounds, a sound family per kind, and soft menu sounds (D-422, D-424 to D-426, D-431).
  - The main theme on the title screen and at the end of region one (D-427). The place music plays on under menus, and after a battle the ambience plays alone before the track resumes (D-421, D-429).
  - The build renders the audio, and the repository commits a hash list, not WAV files (D-432, F-31). Sessions write the music as tracker rows, and the owner hears each batch with a listen command, and later in a sound room (D-433, D-438, D-439).
  - Vibration at heavy moments alone, and four more audio settings (D-434, D-435).
- Mid-block, the owner stopped time in dungeons, and set rest and travel rules (D-436, D-440, D-441). Minutes later, the owner removed the day clock: the story sets the time of day of each map (D-442).
- D-442 supersedes D-190, D-192, D-197, D-198, D-436, D-440, and D-441. D-443 and D-444 cut the night versions of the music, and D-445 removes the sun or moon mark from the HUD.
- The owner put the clock answer in this PR, so the PR holds two concerns (D-437, G-8).
- The session stated three readings. The owner kept two: ambush and elite fights play the common battle track (D-415), and the refuge counts as a cave and the sealed gallery as a mine (D-417). The third has no answer yet: the wrong things walk only on a map set to dusk or night (D-442).
- The session updated `docs/design.md`: a dated line, the system map, F-31, the cost model, PR-7, PR-8, PR-18, PR-33, PR-36, PR-38, and step 2 of section 8.
- It also updated the glossary of the `ste-writing` skill, the open items of `docs/world/setting.md`, and OQ-10 in `docs/questions.md`, and it added revision notes to 14 earlier rows.
- The handoff held ten entries before this one, so Session 7 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).
- The gitar pass on `f8ca3c3` approved with one suggestion: 1 comment, with merit. D-190 lacked its note for D-436, and the commit that holds this revision of the entry adds it. A script check found no other target row of D-412 to D-445 without its note.

### State of the build

- No code exists. `main` is `11498f1` (PR #6).
- PR #7 is open on `docs/pr-7-audio-block`. The remote head is the commit that holds this entry.
- The interim STE check passes with 0 findings, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #7 answers the gitar pass. It adds decision rows, so no `review-override` label applies, and a Codex session reviews it (D-401). The owner merges. Then the release block docs PR, then the roadmaps docs PR (D-399).

### Traps and gotchas

- The PR holds two concerns on owner instruction (D-437). The PR description cites D-437, so a reviewer does not read the second concern as a break of G-8.
- D-442 ends the day clock. Outside the dated records, a text that names a phase of the day, the day clock, or a wait at a save point is now stale. Roadmap phases and boss phases stay. The glossary sets "time of day".
- Five rows of this PR are superseded inside the same PR: D-416, D-420, D-436, D-440, and D-441. They stay as a dated record, as D-395 and D-396 did.
- Region one needs about 20 tracks. Each night beat that the arc adds can need a night version of a place track (D-443).
- The synthesizer must render the same bytes on all three platforms, so it needs integer math (D-432). The PR-38 text carries that.
- The roadmaps PR gives PR ids to the rest of the audio player, the first music, and the sound room (PR-38, D-399).
- In this block, the owner often picked the fullest option, then cut scope for cost. Show the running count of tracks, light setups, or tests in each batch.
- The next ids are D-446, OQ-56, F-32, L-16, G-26, PR-43, M-7, and Session 18.

### Open questions that block progress

None for PR #7. OQ-3 waits for PR-3. The levers for an earlier playable build wait for the owner, and the roadmaps PR is their place.

### Next concrete action

This session answers the gitar pass on PR #7. Then a Codex session reviews PR #7 under the `pr-review` skill and writes `docs/reviews/pr-7.md` (D-401). The owner merges. Then a session starts the release block as its own docs PR (D-399).

## Session 16: 2026-09-14, Claude Code

Author: Claude Code
Session: the first session in the new checkout `/Volumes/SSD-1TB/the-thing-below`, and a docs PR that closes `docs/runbooks/rename-and-move.md`, on branch `docs/pr-6-close-move`.

### What this session did, and why

- PR #5 merged as `aee6f35` at 17:09:52Z, with the `review-override` label. The Session 15 entry went in before the merge, so it does not record what came after.
- After the merge, Session 15 ran two steps of the runbook:
  - Step 9: the clone to `/Volumes/SSD-1TB/the-thing-below`, clean at `aee6f35`.
  - Step 10: the copy of the local session notes from `~/.claude/projects/-Users-nate-Repos-terminal-rpg/memory/` to `~/.claude/projects/-Volumes-SSD-1TB-the-thing-below/memory/`.
- Step 11: this session opened in the new checkout. The interim STE check passed with 0 findings. `diff -r` of the two notes folders found no difference, and the session read its notes from the new folder.
- Before step 12, the session checked that the old checkout `~/Repos/terminal-rpg` held nothing that GitHub lacks:
  - The tree of its last branch tip `152fa62` is the tree of `aee6f35`.
  - `git ls-remote` shows each of its five local branch tips on GitHub, as `refs/pull/1/head` to `refs/pull/5/head`.
  - It had no stash, no untracked or ignored file, no `.claude/settings.local.json`, and no hook.
- Step 12: the owner deleted the old checkout. A check at 17:24:12Z found no folder at that path.
- The docs PR makes the documents show the move as complete:
  - `docs/runbooks/rename-and-move.md`: the status is complete, and steps 7 to 12 are marked done.
  - `docs/design.md`: a dated line for the move pass, and step 2 of section 8 shows PR #5 merged and the checkout on the SSD.
  - `docs/runbooks/dev-machine.md`: a dated fact for the checkout path.
- The PR changes no decision row. The owner answer on step 12 carries out a step that D-216 and D-400 already set, so it adds no row (D-68).
- The handoff held ten entries before this one, so Session 6 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `aee6f35` (PR #5).
- The checkout is `/Volumes/SSD-1TB/the-thing-below`. The old checkout no longer exists.
- PR #6 is open on `docs/pr-6-close-move`. The remote head is the commit that holds this entry.
- The interim STE check passes with 0 findings, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #6 answers the gitar pass. It changes no decision row, and every path is in the override set, so the session applies the `review-override` label after the pass approves the head (D-67, D-401). The owner merges. Then the audio block docs PR starts (D-399).

### Traps and gotchas

- The checkout is on the external SSD. A session cannot open it when the Mac does not show `/Volumes/SSD-1TB`.
- The local session notes key on the checkout path, now `~/.claude/projects/-Volumes-SSD-1TB-the-thing-below/memory/`. The old folder `-Users-nate-Repos-terminal-rpg` still exists, and no session reads it now.
- Gitar runs one pass by itself when a new PR opens, even while the automatic passes are paused (PR #5).
- After a later push, post `Gitar review` two times. The first request runs the pass on the older head again, and the second runs it on the new head (Session 13).
- Count a pass only when a `Gitar` check run on the head commit ends. The dashboard comment is not proof.
- The dated records keep `terminal-rpg` and `~/Repos/terminal-rpg` on purpose.
- The next ids are D-412, OQ-56, F-31, L-16, G-26, PR-43, M-7, and Session 17.

### Open questions that block progress

None for PR #6. OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on PR #6, and applies the `review-override` label when the pass approves the head. The owner merges. Then a session starts the audio block, the next docs PR (D-262, D-399). It reads the audio rows first: D-87, D-115, D-223, D-226, and PR-38 in `docs/design.md`. Then it asks the owner the audio questions in batches and records each answer. That PR adds decision rows, so the other provider reviews it (D-401).

## Session 15: 2026-09-14, Claude Code

Author: Claude Code
Session: the rename PR, steps 4 to 7 of `docs/runbooks/rename-and-move.md`, on branch `docs/pr-5-rename`.

### What this session did, and why

- PR #4 merged as `a16a83e` after the repeat review of Session 14. No other PR was open, so step 4 of the runbook started (D-411).
- The session started `docs/pr-5-rename` from `main`. The next GitHub number was 5.
- A search of every tracked file found 41 mentions of the working title. The dated records keep theirs: `docs/archive/`, the handoff, and the rows of D-9, D-72, and D-102 (step 6).
- The live documents now use the tentative name The Thing Below, and the commands use the names of D-217:
  - `CLAUDE.md` and `AGENTS.md`: the title, the sentence on the project names, and 10 command names each. The two files stay identical.
  - `README.md`: the title, and "The name is tentative."
  - `docs/design.md`: the title, the thesis, step 2 of section 8, and a dated line for the rename pass.
  - The `csharp-conventions` and `ste-writing` skills: the command names, and the technical name of the game.
  - `docs/runbooks/rename-and-move.md`: the status, and steps 4 to 6 marked done.
- The runbook keeps the old names in its table of names and in step 1, because those lines record the change.
- OQ-7 already names D-215, D-217, and D-410, so the questions register needs no note. No owner question came up for this PR (D-68), and the PR changes no decision row.
- The handoff held eleven entries before this one, because Session 14 added its entry and moved none. Sessions 5 and 4 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `a16a83e` (PR #4).
- PR #5 is open on `docs/pr-5-rename`. The remote head is the commit that holds this entry.
- The interim STE check passes with 0 findings, and `CLAUDE.md` and `AGENTS.md` stay identical.
- The local checkout is still `~/Repos/terminal-rpg`.

### In flight

PR #5 answers the gitar pass. It changes no decision row, and every path is in the override set, so the session applies the `review-override` label after the pass approves the head (D-67, D-401). The owner merges. Then steps 9 to 12 of the runbook follow: the clone to the SSD, the copy of the session notes, a new session in the new checkout, and the removal of the old checkout by the owner.

### Traps and gotchas

- Post `Gitar review` after each push, and count the pass only from a `Gitar` check run on the head (Session 13). A request runs the pass on the PR head at the previous request, so a second request can be necessary.
- The label needs a new approval after each push (D-67).
- Step 10 copies `~/.claude/projects/-Users-nate-Repos-terminal-rpg/memory/` to the folder of the new path, probably `-Volumes-SSD-1TB-the-thing-below`. Check the folder name after the first session in the new checkout.
- The dated records and the table of names in the runbook keep `terminal-rpg` on purpose. A search for the old name finds them.
- The next ids are D-412, OQ-56, F-31, L-16, G-26, PR-43, M-7, and Session 16.

### Open questions that block progress

None for PR #5. OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on PR #5 and applies the `review-override` label when the pass approves the head. The owner merges. Then a session runs steps 9 to 12 of `docs/runbooks/rename-and-move.md`.

## Session 14: 2026-09-14, Codex

Author: Codex
Session: repeat review of PR #4 at effective head `919a865`.

### What this session did, and why

- Read the current handoff, the prior review, the response file, the new substantive diff, and the current PR metadata.
- Verified the provider gate remains eligible. Claude Code authored the changes, and Codex reviewed them.
- Reproduced both prior corrections. The design-doc skill now matches the numbered sections of `docs/design.md`, and the name-search facts now include sources, queries, results, and dates.
- Confirmed the automated pass completed successfully on `919a865` with no issue comments.
- Updated `docs/reviews/pr-4.md`, preserved P2-1 and P2-2 with their earlier evidence, and set the verdict to `Ready for owner merge` for `919a865`.

### State of the build

- No code exists. `main` is `d29921d` (PR #3).
- PR #4 is open. Its effective head is `919a865`; later commits contain metadata only.
- The interim STE check passes with 0 findings, `git diff --check` is clean, and `AGENTS.md` and `CLAUDE.md` remain identical.

### In flight

PR #4 is ready for owner merge. After merge, step 4 of the rename runbook starts the rename PR (D-411).

### Traps and gotchas

- The live `gh pr checks` call returned a GitHub API connection error during this review. The handoff records the successful Gitar check run on `919a865`.
- The review applies to `919a865`, not the later handoff-only tip `09ace6c`.
- OQ-3 remains open for branch protection.

### Open questions that block progress

None for PR #4.

### Next concrete action

The owner can merge PR #4. Then run step 4 onward of `docs/runbooks/rename-and-move.md`.

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
- The session pushed that revision as `4ce3138` at 16:08:16Z. It waited 5 minutes, then requested a pass at 16:13:17Z.
- Gitar ran the pass on `92926a6`, not on `4ce3138`. The check run on `92926a6` started at 16:13:22Z and ended with `success` at 16:13:58Z.
- The poll saw the new dashboard comment with no check run on `4ce3138`, and it reported that at once.
- The check runs of every request fit one rule: a request runs the pass on the commit that was the PR head at the request before it.
- This third revision of the entry records that rule in the traps.

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
- The dashboard comment is not proof. Requests 3 seconds, 41 seconds, and 5 minutes after a push ran the pass on the older commits `cb6e96e`, `919a865`, and `92926a6`. Each dashboard said approved.
- A request runs the pass on the PR head at the previous request, so a wait after a push does not help. After a push, post `Gitar review` and wait for its check run.
- Then post `Gitar review` again. That second request runs the pass on the new head.
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
