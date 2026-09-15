# Session handoff

Rule (D-18): this file keeps the 10 newest sessions, newest first. At the end of a session, add a new entry at the top. Move any entry beyond the tenth to the top of `docs/session-handoff-archive.md`. Read the first entry first.

## Session 28: 2026-09-14, Claude Code

Author: Claude Code
Session: the second area file of PR #11, `docs/roadmaps/area-tools.md`, on branch `docs/pr-11-roadmaps`.

### What this session did, and why

- The session resumed PR #11 from the handoff of Session 27. The remote head was `4e16d05`, and no other session pushed after it.
- The session read the design, the whole decision register, the questions register, `area-core.md`, the skills, the agent files, the interim tools, the PR template, and the runbook of the machine.
- The session asked seven contract questions in two batches (D-487), and the owner took each recommendation:
  - Four tools leave the PRs that they share: det-lint becomes PR-46, the PNG code PR-47, the normal maps PR-48, and the night gate PR-49 (D-496).
  - Four tools with no PR take ids and land right before their first user: the screenplay tool PR-50, the PNG import PR-51, the map preview PR-52, and the tile-edge tool PR-53 (D-497).
  - det-lint reads code through the Roslyn compiler library, and the row of D-498 is the decision entry of the package (G-13).
  - Game shows player text through one text helper, and det-lint fails a Godot text property outside it (D-499).
  - GitHub starts `pull_request_target` and `schedule` only from `main`, so PR-3 and PR-49 prove their commands in Tests, and G-16 gains a note (D-500, F-37).
  - The tile-edge tool writes one edge file per map outside the rule files (D-501).
  - A tool whose output a test compares on every CI leg uses integer math (D-502).
- The session read thirteen sources before a fact entered a document: the GitHub trigger rules, two NuGet pages and the NuGet API, eight .NET and C# pages, and the PNG standard. A page summary of NuGet named xunit.v3 4.0.0 as the latest version, and the NuGet API lists 4.0.1, so no xUnit version entered a document.
- F-38 records two float facts of .NET. F-39 records that the default string order of .NET follows the culture and the ICU version of the machine.
- F-39 corrects `area-core.md`: its section 7.5 named `SortedDictionary` for a fixed order and named no comparer. G-4 already asks for a fixed order, and among the built-in comparers only an ordinal comparison stays fixed across machines. So the session added the rule with no question. The owner can still ask for another rule.
- The session filed eight detail questions for PR-2, PR-3, PR-46, PR-47, PR-48, and PR-15 (OQ-67 to OQ-74), as D-487 asks. None blocks PR #11.
- The session updated `docs/design.md`: a dated line, the system map, F-35 to F-39, and a note on G-16. It updated `area-core.md`, the `csharp-conventions`, `pr-review`, and `ste-writing` skills, and 14 earlier decision rows with notes.
- The handoff held ten entries before this one, so Session 18 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `63803d9` (PR #10).
- The branch `docs/pr-11-roadmaps` holds two commits on `main`, and its remote head is the commit that holds this entry. No PR is open, because PR #11 opens when the roadmaps and the rebuild are complete (D-489).
- The interim STE check passes with 0 findings, `git diff --check` is clean, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #11: two of twelve area files are done. Next comes `area-ci.md`, then the other nine area files in the order of D-485. Then come the five phase files and the rebuild of sections 7 and 8 (D-488).

### Traps and gotchas

- The rebuild changes more than sections 7 and 8, because D-496 moves det-lint to PR-46 and the night gate to PR-49. These texts still name the old PRs: G-22 in `docs/design.md`, lines 130, 145, and 147 of `CLAUDE.md` and `AGENTS.md`, and lines 12 and 15 of the PR template. Change them in the rebuild, not before.
- Sections 7 and 8 of `docs/design.md` still show PR-6 whole, PR-4 with det-lint, PR-15 with the night gate, and PR-34 with the PNG code and the normal maps.
- New PR ids so far: PR-43 to PR-53, eleven of about 20 (D-486). The next id is PR-54. The owner took every split in this block, so the count can pass 20. Show running counts in each batch.
- Contract questions for `area-ci.md`, from Session 27 and this session:
  - Where the exported Game reads its content files, and where the host code that reads content files lives.
  - The PR id of the export job of D-449, which PR-45 follows (D-492).
  - The PR and the package of the coverage report of D-174 (G-13).
  - How the `replay-identity` job compares the CI legs: committed hashes, or a compare across legs.
  - Where the night record lives, and how the `night-gate` check finds it (D-500).
  - The job for the few hundred bot runs on each PR (D-64).
- A detail question for PR-1 belongs in `area-ci.md`: `CLAUDE.md` names xUnit, and no decision row justifies a test package (G-13). On 2026-09-14 the NuGet API listed xunit.v3 4.0.1 under Apache-2.0.
- `area-art.md` must settle how the owner sees an image batch in a PR (G-25). The swatch sheet, the atlas, the map preview, and the normal-map preview are PNG files. Check whether `gh` can put an image in a PR description before a question assumes it.
- `area-audio.md` must settle how the listen command of D-439 plays sound from a console program.
- OQ-70: det-lint needs the Godot assembly to read Game types, so PR-46 needs a Game build or the Godot package.
- A page summary can misstate a version. Check each package fact against the NuGet API at `api.nuget.org/v3-flatcontainer/<id>/index.json`.
- The next ids are D-503, OQ-75, F-40, L-16, G-26, PR-54, M-7, and Session 29.

### Open questions that block progress

None for PR #11. OQ-67 to OQ-74 block PR-2, PR-3, PR-46, PR-47, PR-48, and PR-15. OQ-60 to OQ-66 block PR-4, PR-5, PR-6, and PR-43. OQ-57 and OQ-59 block the store page at Gate 2, OQ-58 blocks PR-40, and OQ-3 waits for PR-3.

### Next concrete action

A session continues PR #11 on `docs/pr-11-roadmaps`. It reads `docs/roadmaps/area-core.md`, `docs/roadmaps/area-tools.md`, D-491 to D-502, and the Phase 1 entries of `docs/design.md`. Then it writes `docs/roadmaps/area-ci.md`, asks the contract questions above, and files detail questions with their PRs (D-487, D-488).

## Session 27: 2026-09-14, Claude Code

Author: Claude Code
Session: the first area file of PR #11, `docs/roadmaps/area-core.md`, on branch `docs/pr-11-roadmaps`.

### What this session did, and why

- Session 26 (Codex) gave PR #10 the verdict `Ready for owner merge` at `7eb2abc`. The owner merged PR #10 as `63803d9`.
- The session started PR #11 on the new branch `docs/pr-11-roadmaps` from `63803d9`, and it wrote an area file first (D-488).
- The session read the design, the whole decision register, the questions register, the skills, and one focused roadmap of what-you-carry, for its document shape alone (D-277).
- The session asked four contract questions (D-487), and the owner took each recommendation:
  - PR-6 splits into three PRs. PR-6 keeps the loop, the intents, the run record, and replay. PR-43 takes the save files, and PR-44 takes crash files and log files (D-491).
  - PR-6 adds the debug seam, and PR-45 creates the debug assembly right after PR-7 (D-492).
  - The run record holds intents, with no device kind (D-493).
  - A sixth project, `TheThingBelow.Storage`, holds the file code (D-494).
- A fifth question came up while the file took shape, and the owner took the recommendation: the content hash covers the rule files alone (D-495).
- The session read eight sources on .NET, Git for Windows, the GitHub runner image, and git before a fact entered a document. F-35 records that the .NET hash classes call OS libraries and that a string hash code can change between runs. F-36 records that System.Text.Json uses reflection by default.
- A check found that `.gitattributes` already sets `eol=lf` from PR #1, so the Windows CI leg needs no finding for line ends. The area file cites the rule beside the default of Git for Windows.
- The session filed seven detail questions for PR-4, PR-5, PR-6, and PR-43 (OQ-60 to OQ-66), as D-487 asks. None blocks PR #11.
- The session wrote `docs/roadmaps/area-core.md` and added 18 revision notes to earlier rows. It updated the system map, the finding register, and a dated line in `docs/design.md`, and the `csharp-conventions` and `pr-review` skills.
- The handoff held ten entries before this one, so Session 17 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `63803d9` (PR #10).
- The branch `docs/pr-11-roadmaps` holds one commit on `main`, and its remote head is the commit that holds this entry. No PR is open, because PR #11 opens when the roadmaps and the rebuild are complete (D-489).
- The interim STE check passes with 0 findings, `git diff --check` is clean, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #11: one of twelve area files is done. Next come `area-tools.md` and `area-ci.md`, then the other nine area files in the order of D-485. Then come the five phase files and the rebuild of sections 7 and 8 (D-488).

### Traps and gotchas

- Sections 7 and 8 of `docs/design.md` still show PR-6 whole, with no PR-43, PR-44, or PR-45. The rebuild at the end of PR #11 changes them (D-488, D-491, D-492). Do not edit them before the phase files exist.
- New PR ids so far: PR-43, PR-44, and PR-45, three of about 20 (D-486). The next id is PR-46.
- The export job of D-449 still needs its PR id in `area-ci.md`, and PR-45 comes after that job (D-492).
- Where the exported Game reads its content files is open. Godot exports a JSON file only through the filter for non-resource files, and `content/` sits outside the Game project folder (D-118). The session did not check whether an export can take a file from outside that folder. Ask it as a contract question in `area-ci.md` (D-487).
- Storage holds the file code for saves, records, crash files, and logs (D-494). The reader of content files for Tools and Tests has no home yet. Settle it with the content question above.
- D-495 keeps the string text out of the content hash. A rule file that names a string id still needs the id test of section 7.7 of the area file.
- The system map now splits the snapshot bytes of Core from the files of Storage. A later area file keeps that split.
- Every later Core PR carries the seven steps of section 7.14 of the area file. The phase files turn them into exit tests.
- The owner took every recommendation in this block. Still show running counts of PR ids and files in each batch (Session 23).
- The next ids are D-496, OQ-67, F-37, L-16, G-26, PR-46, M-7, and Session 28.

### Open questions that block progress

None for PR #11. OQ-60 to OQ-66 block PR-4, PR-5, PR-6, and PR-43. OQ-57 and OQ-59 block the store page at Gate 2, OQ-58 blocks PR-40, and OQ-3 waits for PR-3.

### Next concrete action

A session continues PR #11 on `docs/pr-11-roadmaps`. It reads `docs/roadmaps/area-core.md`, D-491 to D-495, and the Phase 1 entries of `docs/design.md`. Then it writes `docs/roadmaps/area-tools.md`, asks contract questions alone, and files detail questions with their PRs (D-487, D-488).

## Session 26: 2026-09-14, Codex

Author: Codex
Session: repeat review of PR #10 at effective head `7eb2abc`.

### What this session did, and why

- Verified the new base, effective head, changed paths, provider gate, response file, and existing PR comments.
- Read the correction diff, the complete PR diff, the design and decision contracts, the question register, the skills, the agent guidance, the handoff archive, and the PR description.
- Reproduced P2-1. D-488 now uses `Revised in part by D-490`, names PR #11 as the changed part, and keeps the writing order.
- Confirmed D-490 names D-488 among the revised decisions and that the design and handoff identify PR #11.
- Confirmed the repeat Gitar check passed on `7eb2abc` with no new comment.
- Updated `docs/reviews/pr-10.md`, preserved P2-1 with its earlier evidence, and set the verdict to `Ready for owner merge` for `7eb2abc`.
- Ran the interim STE check with 0 findings, `git diff --check`, and the guidance identity check.

### State of the build

- No code exists. `main` is `4f37c99` (PR #9).
- PR #10 is open on `docs/pr-10-roadmaps`. Its effective head is `7eb2abc`.
- The interim STE check passes with 0 findings. The repeat review metadata and handoff are pushed in `e8cc765`.

### In flight

PR #10 is ready for owner merge. Then PR #11 starts the roadmaps on a new branch.

### Traps and gotchas

- D-488 and D-489 keep `PR #10` in their topic columns as dated text. Their revision notes carry the current PR number.
- The build, test, format, det-lint, replay-identity, smoke, night-gate, and review-gate checks do not exist until the PRs named in `AGENTS.md` create them.
- The next ids are D-491, OQ-60, F-35, L-16, G-26, PR-43, M-7, and Session 27.

### Open questions that block progress

None for PR #10. OQ-57 and OQ-59 block the store page at Gate 2, OQ-58 blocks PR-40, and OQ-3 waits for PR-3.

### Next concrete action

The owner can merge PR #10. Then a fresh session starts PR #11 with `docs/roadmaps/area-core.md`.

## Session 25: 2026-09-14, Claude Code

Author: Claude Code
Session: the answer to the review of PR #10, on branch `docs/pr-10-roadmaps`.

### What this session did, and why

- Session 24 (Codex) reviewed PR #10 at `9355d62` and gave `Changes required` with P2-1: D-488 kept the PR number that D-490 changed, and D-490 did not mark D-488 as revised in part.
- The owner asked the session to address the feedback. The session fetched the branch at `571e39e`, read the review record, and found no other open comment or thread.
- P2-1, full merit: the Effect column of D-490 now revises D-484, D-488, and D-489 in part. The note on D-488 now uses the marker `Revised in part by D-490`, names the PR number as the changed part, and keeps the order of the work.
- A search of the live documents found PR #11 as the PR of the roadmaps and the rebuild in D-484, D-488, D-489, D-490, the dated line and step 2 of section 8 in `docs/design.md`, and the handoff.
- `docs/reviews/pr-10-response.md` records the disposition.
- The handoff held ten entries before this one, because Session 24 moved Session 14 to the archive. Session 15 moved word for word to the top of `docs/session-handoff-archive.md` (D-18).

### State of the build

- No code exists. `main` is `4f37c99` (PR #9).
- PR #10 is open on `docs/pr-10-roadmaps`. The commit that holds this entry is the new effective head, because it changes `docs/decisions.md`.
- The interim STE check passes with 0 findings, and `CLAUDE.md` and `AGENTS.md` stay identical.

### In flight

PR #10 answers a new gitar pass on the new head. Then a Codex session runs the repeat review of PR #10 and updates `docs/reviews/pr-10.md`. The owner merges. Then PR #11 starts the roadmaps on a new branch (D-488, D-490).

### Traps and gotchas

- After a push, the first `Gitar review` request re-runs the previous head, and it can complete an existing check run again rather than start a new one. Send the second request when the dashboard updates or an old run completes again with no run on the new head.
- A reviewer session can move an old entry to the archive. Count the handoff entries before a rotation, and never assume the count.
- D-488 and D-489 keep "PR #10" in their topic column as dated text. Their revision notes carry the current PR number.
- The next ids are D-491, OQ-60, F-35, L-16, G-26, PR-43, M-7, and Session 26.

### Open questions that block progress

None for PR #10. OQ-57 and OQ-59 block the store page at Gate 2, OQ-58 blocks PR-40, and OQ-3 waits for PR-3.

### Next concrete action

This session answers the gitar pass on the new head and records it in the PR description. Then a Codex session runs the repeat review of PR #10 under the `pr-review` skill. The owner merges. Then a fresh session starts PR #11 with `docs/roadmaps/area-core.md`.

## Session 24: 2026-09-14, Codex

Author: Codex
Session: cross-provider review of PR #10 at effective head `9355d62`.

### What this session did, and why

- Verified the PR target, base, merge base, branch, effective head, changed paths, provider gate, and existing PR comments.
- Read the complete diff, the design and decision contracts, the questions register, the skills, the agent guidance, the handoff archive, and the PR description.
- Confirmed the final Gitar check passed on `9355d62` and that its one suggestion was fixed in that commit.
- Found P2-1: D-488 still names PR #10, while D-490 says D-488 binds PR #11 without a revision note for D-488.
- Ran the interim STE check with 0 findings, `git diff --check`, and the guidance identity check.
- Added `docs/reviews/pr-10.md` with the verdict `Changes required` for `9355d62`.

### State of the build

- No code exists. `main` is `4f37c99` (PR #9).
- PR #10 is open on `docs/pr-10-roadmaps`. Its effective head is `9355d62`.
- The interim STE check passes with 0 findings. The review record and handoff are pushed in `95fd404`.

### In flight

PR #10 needs the D-488 revision note and a repeat review. The owner merges after the verdict covers the new effective head.

### Traps and gotchas

- D-490 must revise D-488 in part, not only D-484 and D-489. The writing order stays unchanged, and only the PR number changes to PR #11.
- The build, test, format, det-lint, replay-identity, smoke, night-gate, and review-gate checks do not exist until the PRs named in `AGENTS.md` create them.
- The next ids are D-491, OQ-60, F-35, L-16, G-26, PR-43, M-7, and Session 25.

### Open questions that block progress

None for PR #10. OQ-57 and OQ-59 block the store page at Gate 2, OQ-58 blocks PR-40, and OQ-3 waits for PR-3.

### Next concrete action

The author adds the D-488 revision note and runs a repeat Gitar pass. Then a Codex session updates `docs/reviews/pr-10.md` for the new effective head.

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
