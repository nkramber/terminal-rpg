# Session handoff

Rule (D-18): this file keeps the 10 newest sessions, newest first. At the end of a session, add a new entry at the top. Move any entry beyond the tenth to the top of `docs/session-handoff-archive.md`. Read the first entry first.

## Session 23: 2026-09-14, Claude Code

Author: Claude Code
Session: the shape of the roadmaps after PR #9 merged, as docs PR #10 on branch `docs/pr-10-roadmaps`.

### What this session did, and why

- Session 22 (Codex) reviewed PR #9 at `5097e8a` with no finding. The owner merged PR #9 as `4f37c99`.
- The same harness run as Session 21 started the roadmaps docs PR (D-399). It asked OQ-56 first, and the owner chose no change to the sequence (D-483).
- The session read every text that sends work to the roadmaps. The list holds PR ids for the export job, the store page work, the credits roll, the trailer capture, the debug assembly, the sound room, and the mood cues. It also holds the items of the technical, graphics, UI, and systems roadmaps.
- The owner set the shape of the work:
  - Two docs PRs for the roadmaps work: one for the roadmaps and the rebuild of sections 7 and 8, and a later one for the design-critic pass (D-484).
  - Twelve area files and five phase files in `docs/roadmaps/`, with the names in D-485.
  - One new PR id per system or tool, about 20, from PR-43 (D-486).
  - The roadmaps ask contract questions, and they file detail questions with the PR they block (D-487).
  - Areas first, then phases, then the rebuild (D-488). The roadmaps PR opens when its work is complete (D-489).
- The owner asked whether every document was current, and why no PR was open. The session quoted D-489, and the owner chose to merge the shape now as PR #10 (D-490). The roadmaps move to PR #11, and the critic pass to PR #12.
- The session brought the design current: a dated line, the file set in section 7, and step 2 of section 8. Notes on D-399, D-484, D-488, and D-489 record the later answers. No roadmap file exists yet, and the area files wait for a fresh context.
- The gitar pass on `05dd81a` approved with one suggestion, which had merit: the D-485 row sat after D-487. The commit that holds this revision of the entry moves the row between D-484 and D-486, and the reply on the thread names it.
- The handoff held eleven entries before this one, because Session 22 added its entry and moved none. Sessions 13 and 12 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `4f37c99` (PR #9).
- PR #10 is open on `docs/pr-10-roadmaps` with D-483 to D-490. The remote head is the commit that holds this entry.
- The interim STE check passes with 0 findings.

### In flight

PR #10 answers the gitar pass. It adds decision rows, so a Codex session reviews it, and no `review-override` label applies (D-401). The owner merges. Then PR #11 starts the roadmaps on a new branch (D-488, D-490).

### Traps and gotchas

- D-484 and D-490 put the design-critic pass in PR #12. Do not run it in PR #10 or PR #11.
- D-487: in PR #11, ask a question only when it changes the order, a gate, or a contract between PRs. File each detail question in `docs/questions.md` with the PR it blocks.
- New PR ids start at PR-43 (D-486). PR-22 and PR-32 stay retired (G-10).
- Each file follows the focused roadmap template of the `design-doc-style` skill: the status header and sections 1, 5, 7, 8, and 9. Each phase entry lists its scope, exit tests, review focus, filed questions, and area file (D-144).
- The owner chose finer shapes than the session recommended twice in this block: two PRs, and twelve area files. Show running counts of files and PR ids in each batch.
- D-489 now binds PR #11: push its branch at each session end, and open it when the roadmaps and the rebuild are complete (D-490). PR #11 needs a branch of its own, such as `docs/pr-11-roadmaps`.
- The next ids are D-491, OQ-60, F-35, L-16, G-26, PR-43, M-7, and Session 24.

### Open questions that block progress

None for PR #10. OQ-57 and OQ-59 block the store page at Gate 2, OQ-58 blocks PR-40, and OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on PR #10. Then a Codex session reviews PR #10 under the `pr-review` skill and writes `docs/reviews/pr-10.md` (D-401). The owner merges. Then a session starts PR #11 on a new branch. It reads D-144, D-145, D-484 to D-490, the `design-doc-style` skill, and section 7 of `docs/design.md`, and it writes `docs/roadmaps/area-core.md` first (D-488).

## Session 22: 2026-09-14, Codex

Author: Codex
Session: cross-provider review of PR #9 at effective head `5097e8a`.

### What this session did, and why

- Verified the PR target, base, merge base, branch, effective head, changed paths, provider gate, and all existing PR comments.
- Read the complete diff, the release entries of the design and decision documents, the questions register, the changed skills and guidance, the runbook, the world note, the handoff archive, the PR description, and prior review records.
- Checked D-480, D-481, and D-482 against their revision notes. The release facts, the aspect ratios, the supported targets, the macOS export form, and the sequence agree.
- Found no in-scope finding. The review record is `docs/reviews/pr-9.md` with the verdict `Ready for owner merge` for `5097e8a`.

### State of the build

- No code exists. `main` is `f4a1c6b` (PR #8).
- PR #9 is open on `docs/pr-9-release-block`. The effective head is `5097e8a`. This entry and the review record are metadata.
- The interim STE check passes with 0 findings, `git diff --check` is clean, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #9 waits for the owner to merge. The roadmaps docs PR follows (D-399).

### Traps and gotchas

- D-184 excludes only `docs/reviews/`, `docs/session-handoff.md`, and `docs/session-handoff-archive.md`. The effective head is `5097e8a`, not this metadata commit.
- D-481 supersedes the arm64 Windows and Linux exports and their five CI legs. D-482 keeps a universal macOS export while supporting Apple silicon alone.
- GitHub API calls and `git fetch origin` hit environment errors during this review. The PR metadata and existing remote-tracking refs still identified the reviewed commits and Gitar result.
- The build, test, format, det-lint, replay-identity, smoke, night-gate, and review-gate checks do not exist until the PRs named in `AGENTS.md` create them.
- The next ids are D-483, OQ-60, F-35, L-16, G-26, PR-43, M-7, and Session 23.

### Open questions that block progress

None for PR #9. OQ-56 waits for the roadmaps PR. OQ-57 and OQ-59 block the store page at Gate 2. OQ-58 blocks PR-40. OQ-3 waits for PR-3.

### Next concrete action

Push this review record and handoff entry. Then the owner can merge PR #9. The next session starts the roadmaps docs PR and asks OQ-56 first.

## Session 21: 2026-09-14, Claude Code

Author: Claude Code
Session: the release block of the full plan, and two aspect ratios, on branch `docs/pr-9-release-block`.

### What this session did, and why

- Session 20 (Codex) reviewed PR #8 at `511203c` with no finding. The owner merged PR #8 as `f4a1c6b` and asked what comes next.
- The handoff and D-399 put the release block docs PR next. The first lever of OQ-56 moves that PR after the first playable, so the session asked first. The owner kept the order (D-447).
- Three read-only research agents read Steamworks, Apple, Microsoft, GitHub, and Godot pages. The session fetched each key page again and checked the quotes before a fact entered a document.
- The release block ran in twelve batches, D-447 to D-480:
  - Versions and builds: 0.MINOR.PATCH until 1.0.0, and exports on every merge from PR-7 (D-448, D-449). The owner first added arm64 builds and arm64 CI legs (D-464, D-474).
  - Signing: macOS notarized on Steam from PR-40, and Windows unsigned (D-455, D-463). F-32 records the Apple fee that the cost model lacked.
  - GitHub: prologue tags alone on GitHub Releases, until the Steam demo (D-457, D-470). The repository goes private before paid content (D-456).
  - Steam: the native Linux build on the Deck, the rating Verified, engine input with one Steamworks call for glyphs, and Auto-Cloud on the folder `the-thing-below` (D-458 to D-461, D-465). PR-40 picks the binding (D-462, OQ-58).
  - Store: the store page at Gate 2, store text and capsule grids by sessions, a trailer from replays, one Next Fest, and the demo name "The Thing Below: Prologue" (D-452, D-471, D-472, D-475, D-476, D-478).
  - Studio and players: a studio name picked before the store page (OQ-57), a studio mark on the splash, credits in three places, crash files to a studio email, and trusted players after Gate 4 (D-450, D-451, D-467 to D-469, D-473). Achievements come with the full game alone (D-466).
  - The AI disclosure of the Steam content survey waits for OQ-59, before the store page review at Gate 2 (D-477).
- Mid-block, the owner asked for a variety of aspect ratios and a revision of D-229. After four answers in a few minutes, the game supports 16:10 and 16:9 alone, with black bars on every other shape (D-480). The answer lands in this PR, and `CLAUDE.md` and `AGENTS.md` no longer list exceptions to G-8 (D-479).
- After gitar approved `980e96c` with 0 comments, the owner cut the scope to four targets: Windows and Linux on x86_64, macOS on Apple silicon, and the Steam Deck (D-481). D-481 supersedes D-464 and D-474. The macOS build stays the official universal build, and the game supports Apple silicon alone (D-482).
- F-33 records five gaps that the block closed, and F-34 records the screenshot format of Steam.
- The session updated `docs/design.md`, `docs/questions.md`, `CLAUDE.md`, `AGENTS.md`, the PR template, three skills, the dev-machine runbook, and `docs/world/setting.md`.
- The handoff held eleven entries before this one, because Session 20 added its entry and moved none. Sessions 11 and 10 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `f4a1c6b` (PR #8).
- PR #9 is open on `docs/pr-9-release-block`. The remote head is the commit that holds this entry.
- The interim STE check passes with 0 findings, `git diff --check` is clean, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #9 answers the gitar pass. It adds decision rows, so a Codex session reviews it, and no `review-override` label applies (D-401). The owner merges. Then the roadmaps docs PR starts (D-399).

### Traps and gotchas

- The PR holds two concerns on owner instruction (D-479). The description names the second concern, so a reviewer does not read it as a break of G-8.
- D-480 took several answers: a wider view, a limit at 16:9, a crop of narrow screens, then 16:9 alone, then 16:9 and 16:10. Only the last answer is a row. Any text that names 21:9, 4:3, or a crop is stale.
- D-471 moves the Steam Direct fee, the EU and WIPO name checks, the store text, and the capsule art to Gate 2. OQ-57 and OQ-59 now block the store page at Gate 2, and OQ-57 also blocks the crash address of D-473.
- The roadmaps PR gives PR ids to the export job after PR-7, the store page work after Gate 2, the credits roll, and the trailer capture.
- The Steamworks pages do not say how Auto-Cloud settles a conflict or whether a demo app needs a fee. PR-40 checks both.
- D-464 and D-474 are superseded inside this PR. Any text that names arm64 builds for Windows or Linux, five exports, or five CI legs is stale.
- The owner often gives a custom answer that widens the scope. Ask the limits in the next batch, and confirm the final state before the rows.
- Gitar runs one pass by itself on a new PR. After a later push, post `Gitar review`, and count a pass only from a `Gitar` check run on the head.
- The next ids are D-483, OQ-60, F-35, L-16, G-26, PR-43, M-7, and Session 22.

### Open questions that block progress

None for PR #9. OQ-57 and OQ-59 block the store page at Gate 2, and OQ-58 blocks PR-40. OQ-56 waits for the roadmaps PR, and OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on PR #9. Then a Codex session reviews PR #9 under the `pr-review` skill and writes `docs/reviews/pr-9.md` (D-401). The owner merges. Then a session starts the roadmaps docs PR, asks OQ-56 first, and rebuilds sections 7 and 8 of `docs/design.md` (D-399).

## Session 20: 2026-09-14, Codex

Author: Codex
Session: cross-provider review of PR #8 at effective head `511203c`, on branch `docs/pr-8-docs-current`.

### What this session did, and why

- Verified the PR target, base, merge base, branch, effective head, changed paths, author provider, and the automated pass.
- Confirmed the provider gate. Session 19 identifies Claude Code as the author of the substantive changes, and Codex is the eligible reviewer.
- Read the complete diff, the design sequence, the decision and question registers, the project guidance, the handoff archive, and the PR description.
- Checked D-446 against D-442 and D-193. The partial revision leaves the other time rules of D-442 current.
- Confirmed that `AGENTS.md` and `CLAUDE.md` stay identical, the handoff has ten current sessions, and Sessions 9 and 8 moved word for word to the archive.
- Wrote `docs/reviews/pr-8.md` with no finding and the verdict `Ready for owner merge` for `511203c`.

### State of the build

- No code exists. `main` is `cf2b197` (PR #7).
- PR #8 is open on `docs/pr-8-docs-current`. The remote head is the review commit that holds this entry and `docs/reviews/pr-8.md`.
- The interim STE check passes with 0 findings, `git diff --check` is clean, and `AGENTS.md` and `CLAUDE.md` are identical.

### In flight

PR #8 is ready for the owner to merge. OQ-56 blocks only the roadmaps PR's rebuild of section 8. The release block docs PR follows this PR (D-399).

### Traps and gotchas

- The effective head is `511203c`, not the later metadata commit that publishes the review record (D-184).
- D-446 revises the rule for wrong things only. D-442 still sets the time of day for maps, and D-443 still governs night versions of place music.
- The build, test, format, det-lint, replay-identity, smoke, night-gate, and review-gate checks do not exist yet. The PRs named in `AGENTS.md` create them.
- OQ-3 remains open for branch protection and does not block this documentation PR.

### Open questions that block progress

OQ-56 waits for the roadmaps PR. OQ-3 waits for PR-3.

### Next concrete action

The owner merges PR #8. Then a session starts the release block docs PR and reads D-53, D-85, D-93, D-143, and the Phase 5 entries of `docs/design.md` before it asks the release questions.

## Session 19: 2026-09-14, Claude Code

Author: Claude Code
Session: the audit of every document before a context reset, after PR #7 merged, on branch `docs/pr-8-docs-current`.

### What this session did, and why

- Session 18 (Codex) reviewed PR #7 at `138e5cf` with no finding and the verdict `Ready for owner merge`. The owner merged PR #7 as `cf2b197`.
- The owner asked: "Ensure ALL docs are up to date in preparation for context reset."
- A search of the live documents for the old clock, the old audio rules, and the state of PR #7 found two stale texts:
  - `CLAUDE.md` and `AGENTS.md` named PR #2 as the one exception to G-8, but D-437 made PR #7 a second exception.
  - Step 2 of section 8 in `docs/design.md` did not show PR #6 and PR #7 as merged.
- Two owner items lived only in the conversation, and a reset would lose them. The session asked both:
  - The reading of D-442 on the wrong things. The owner chose placement by the story, at any time of day (D-446). D-442, D-193, and the effect of D-414 gained notes.
  - The levers for an earlier playable build. The owner filed them as OQ-56 for the roadmaps PR.
- The skills, the agents, the runbooks, the README, the PR template, and the world files hold no stale text. There, "clock" means the wall clock, and "phase" means a roadmap phase or a boss phase.
- `docs/design.md` gained a dated line for this pass.
- The handoff held eleven entries before this one, because Session 18 added its entry and moved none. Sessions 9 and 8 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `cf2b197` (PR #7).
- PR #8 is open on `docs/pr-8-docs-current`. The remote head is the commit that holds this entry.
- The interim STE check passes with 0 findings, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #8 answers the gitar pass. It adds D-446, so it takes a Codex review, and no `review-override` label applies (D-401). The owner merges. Then the release block docs PR starts (D-399).

### Traps and gotchas

- The push line of `docs/reviews/pr-7.md` keeps the placeholder `<review metadata sha>`. The review commit is `a0cf252`. The record belongs to the reviewer, so this session left it as it is.
- The wrong things have no time rule now (D-446). Outside the dated records and the superseded rows, a text that says they walk after dusk or at night is stale.
- OQ-56 blocks only the rebuild of section 8 in the roadmaps PR. The release block docs PR comes first, unless the owner answers OQ-56 sooner.
- Gitar runs one pass by itself on a new PR. After a later push, post `Gitar review`. When a new dashboard appears with no `Gitar` check run on the head, post the second request within a minute.
- In the audio block, the owner often picked the fullest option, then cut scope for cost. Show the running count of tracks, light setups, or tests in each batch.
- The next ids are D-447, OQ-57, F-32, L-16, G-26, PR-43, M-7, and Session 20.

### Open questions that block progress

None for PR #8. OQ-3 waits for PR-3. OQ-56 waits for the roadmaps PR.

### Next concrete action

This session answers the gitar pass on PR #8. Then a Codex session reviews PR #8 under the `pr-review` skill and writes `docs/reviews/pr-8.md` (D-401). The owner merges. Then a session starts the release block as its own docs PR (D-262, D-399). It reads D-53, D-85, D-93, D-143, and the Phase 5 entries of `docs/design.md`, then asks the owner the release questions in batches.

## Session 18: 2026-09-14, Codex

Author: Codex
Session: review of PR #7 at effective head `138e5cf`, on branch `docs/pr-7-audio-block`.

### What this session did, and why

- Read the handoff, the project instructions, the `pr-review` and `ste-writing` skills, the design, decisions, questions, world, review, and PR documents.
- Verified the provider gate: Claude Code authored the substantive PR changes, and Codex reviewed them.
- Reviewed the complete PR diff. The audio decisions, the time-of-day supersession chain, the roadmap entries, the glossary, and the document dispositions agree at `138e5cf`.
- Verified the Gitar comment. The added D-190 note in `138e5cf` completes the back-reference to D-436.
- The effective head is `138e5cf`, not `f8ca3c3`, because `138e5cf` changes `docs/decisions.md`, which is outside the metadata set.
- The review record is `docs/reviews/pr-7.md`. It has no finding and gives the verdict `Ready for owner merge` for `138e5cf`.

### State of the build

- No code exists. `main` is `11498f1` (PR #6).
- PR #7 is open on `docs/pr-7-audio-block`. The remote head is the review commit that holds this entry and `docs/reviews/pr-7.md`.
- The interim STE check passes with 0 findings, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #7 waits for the owner to merge. Then the release block docs PR starts, followed by the roadmaps docs PR (D-399).

### Traps and gotchas

- A commit that changes `docs/decisions.md` is substantive. The effective head rule excludes only `docs/reviews/`, `docs/session-handoff.md`, and `docs/session-handoff-archive.md`.
- The Gitar dashboard comment is not the only evidence of a pass. The Gitar check passed, but `gh pr checks` also reported a GitHub API connection error.
- The build, test, format, Godot, and later gate checks do not exist until the PRs named in `docs/design.md` create them.

### Open questions that block progress

None for PR #7. OQ-3 waits for PR-3. The EUIPO, TMview, and WIPO checks wait for PR-40.

### Next concrete action

The owner merges PR #7. Then a session starts the release block docs PR.

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
