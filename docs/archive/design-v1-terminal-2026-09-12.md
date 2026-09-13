# terminal-rpg: Design and Roadmap

Status: **archived 2026-09-12. Superseded by `docs/design.md` v2 under D-98 and D-99.** The terminal plan of v1 stays here unchanged as the refuted plan. Original status: design document v1, pre-production. Its source is the decision register `docs/decisions.md`, entries D-1 onward. The owner recorded D-1 to D-25 in the repository interview and D-26 to D-65 in the roadmap interview, both on 2026-09-12. Nothing in this file is code. Each plan item ships as one pull request.

External facts, verified 2026-09-12:

- The GitHub repository `nkramber/terminal-rpg` is public and holds no commit. Source: `gh repo view`, run 2026-09-12.
- Branch protection with required status checks is free on a public repository. Source: docs.github.com, "About protected branches", read 2026-09-12.
- The development machine has no Rust toolchain. Source: `command -v cargo`, run 2026-09-12 (OQ-2).

Text rules: this file follows ASD-STE100 (D-10). Tables are exempt from sentence-length counts.

## 1. Thesis

terminal-rpg is a dark fantasy role-playing game in the terminal (D-27). A fixed cast of five (D-33, D-58) travels between hubs of every shape, a castle town, a cave community, a boat, an airship (D-28). Between the hubs lie hand-authored dungeons with visible enemies, traps, puzzles, and secrets (D-37, D-39, D-41). Three fight at a time on a visible timeline where speed decides the order (D-29, D-31). Every character changes jobs at a hub, keeps every ability learned, and carries one secondary set (D-32).

Combat is hard because enemies think and resources run out (D-35), and a fallen character stays down until a hub (D-36). Decisions close routes, lose allies, and change hubs (D-40).

The plan puts the foundations first, because every later system depends on them. Those are a deterministic core, a run record with replay, the content loader, and the document gates. The first playable is one hub and one dungeon with job change and a shop (D-51), because the owner judges feel there. The story systems come third, because they need the loop. Region one, two hubs and four dungeons in one arc, is the first release (D-56). Five gated phases hold that order.

## 2. Lessons learned (carry into every PR)

From the two reference repositories, decktome and what-you-carry:

1. **L-1. One concern per PR.** A bundled PR froze behind one review objection.
2. **L-2. Commit the evidence.** An uncommitted script hid its gaps from reviewers.
3. **L-3. Audit design claims before you trust them.** A first draft carried refutable claims, and an audit found nine defects in one pass.
4. **L-4. Verify a platform claim before you build on it.** A documented cap that nobody enforced, and a machine that lost its power margin once a new target arrived.
5. **L-5. A plan entry is a claim, and it ages.** A fix shape survived three weeks unexamined because it read as one `if` statement.
6. **L-6. A new decision can remove the premise of an old one.** Re-check the old one when a related answer arrives.
7. **L-7. Ask about what the document does not say.** The gap in a design doc is where the next contradiction lives.
8. **L-8. Two answers can conflict when neither one is wrong.** Quote both and settle it at once.
9. **L-9. An exploit hides in every convenience.** A resume feature became a free heal.
10. **L-10. One language, one format, one term.** A second tool language, a second content format, and a borrowed skill with foreign names each cost a correction PR.
11. **L-11. A gate that names an absent check cannot pass.** Name the PR that creates each check, and a PR that creates a check passes it (G-16).
12. **L-12. Two writers need a serialization point.** Two providers picked the same session number on the same day. Fetch and re-read before the handoff commit (D-18).

From the roadmap interview of 2026-09-12:

13. **L-13. A recommendation carries its reason, and the reason can be the wrong one.** D-39 took seeded variation for replay value. D-46 said replay has no value. D-47 dropped the variation (F-6).

## 3. System map

| Component | Crate | Reads | Writes | Sensitivity |
|---|---|---|---|---|
| Simulation loop | core | input stream, seed, content | state, run record | Total. Every replay depends on it |
| Random streams | core | seed | numbers | Total. Cross-platform identity |
| Content loader | core | RON files | typed content, content hash | High. A silent default here breaks the economy |
| String table | core | RON files | text by id | Medium |
| Run record and replay | core | state, inputs | record file, save file | Total. The crash report and the save (D-62) |
| Tile map and movement | core | layout content, inputs | party position, sight | High. Patrols and ambushes (D-37) |
| Battle and timeline | core | party, enemies, abilities | turn order, damage, statuses | Total. The design risk (D-29, D-35) |
| Evaluator and profiles | core | battle state, enemy profile | enemy actions | High. The largest single system (D-65) |
| Jobs, levels, abilities | core | job content, experience, ability points | character state | High. The build decision (D-32, D-34) |
| Gear and items | core | item content, inventory | equipment state | Medium (D-44, D-45) |
| Story flags, quests, reputation, relationships | core | decision content, choices | flags, hub state | High. Branches multiply (D-40, D-59) |
| Hub services | core | hub content, gold | party, saves, jobs | Medium (D-59) |
| Terminal front end | tui | state, string table | screen, inputs | Medium. Cosmetic by design (D-48, D-49, D-50) |
| STE checker, det-lint, review gate | tools | source, docs | pass or fail | Gate |
| Headless runner and bots | tools | policies, seeds | run records | High. The night gate (D-64) |
| Release build | CI | tag | three binaries | Low (D-53) |

## 4. Cost model (what we pay, what we do not know)

What we pay:

- Owner time: the interviews, the approvals of every text batch (D-57), and the play sign-off of every phase (D-52).
- Tokens: two harnesses, Claude Code and Codex, on every PR (D-14, D-17). The amount per PR is unknown until M-1.
- CI: GitHub-hosted minutes on three platforms per PR (D-2), plus a nightly bot run (D-64). Free on a public repository (D-4). Wall time per PR is unknown until M-2.
- Purchases: none. No engine, no store fee, no asset license, no signing certificate (D-53).

Measurements that answer the unknowns:

- M-1: tokens per PR from the harness usage reports, over the first ten PRs.
- M-2: CI wall time per PR, per platform, over the first ten PRs.
- M-3: the night run wall time and the crash and softlock counts, over the first seven nights (D-64).
- M-4: turns per encounter and party deaths per dungeon by bot policy, on the first dungeon. Binds the resource numbers of D-35.

## 5. Defect and finding register

Status: ✅ done (code merged, or "doc" for a document-only correction) · 🔧 planned (item listed) · ⚠ constraint (binds a pull request) · ❓ needs owner input · ⏸ out of scope · 🅿 parked.

| # | Finding | Date | Status |
|---|---|---|---|
| F-1 | The harness default adds a co-author trailer to commits, and the reminder repeats in every session. D-22 forbids it | 2026-09-12 | ✅ doc. `.claude/settings.json` sets empty strings. The rule sits at the top of `CLAUDE.md` |
| F-2 | The what-you-carry review gate and STE checker are C# tools, and D-1 chose Rust. Neither tool runs here | 2026-09-12 | 🔧 D-10 and D-15. PR-2 and PR-3 port them. The Python script is the interim checker |
| F-3 | Rust is absent from the development machine | 2026-09-12 | ❓ OQ-2. Owner action before PR-1 |
| F-4 | The repository had no commit, so no branch and no PR could exist | 2026-09-12 | ✅ D-25. The owner made the root commit `6b899dd` with an empty `CLAUDE.md` |
| F-5 | The Python checker applies the 20-word limit to every numbered item, and the C# tool applied it under a Sequence or Procedure heading alone | 2026-09-12 | ⚠ Binds PR-2. The Rust port picks one rule, and the skill text follows it |
| F-6 | D-39 took seeded dungeon variation on a replay premise, and D-46 removed the premise | 2026-09-12 | ✅ D-47. No variation. L-13 |
| F-7 | D-36 leaves a fallen character down until a hub, and a three-character party (D-31) then fights with two. No decision balances the short-handed party | 2026-09-12 | ⚠ D-58 gives a reserve and a swap at save points. Binds PR-16 and M-4 |
| F-8 | D-42 empties a caster's MP across a dungeon, and no decision gives a job a no-MP action | 2026-09-12 | ⚠ Binds the job content of PR-12: every job has at least one ability with no MP cost |
| F-9 | D-48 sets the floor at 120 by 40, and a default macOS Terminal window is 80 by 24 | 2026-09-12 | ⚠ Binds PR-7: the size message names the floor and how to resize |
| F-10 | D-62 puts the run record in the save, and a record grows without bound over 20 to 40 hours (D-30) | 2026-09-12 | ⚠ Binds PR-6: the record format needs a compaction rule, a snapshot plus the inputs since it |
| F-11 | The interim checker read an HTML comment as prose. A fixture comment with a semicolon, a modal, a passive, and 30 words raised four findings. The automated pass of PR #1 found it | 2026-09-12 | ✅ doc. The script removes a one-line comment. ⚠ Binds PR-2: the Rust port carries the rule |
| F-12 | The session wrote in `CLAUDE.md`, the PR template, the skill, and OQ-1 that gitar was absent, on no evidence. The pass ran on PR #1 within a minute | 2026-09-12 | ✅ doc. D-66. Every claim about a tool needs a check |

## 6. Guardrails (the safety contract for every PR)

### 6.1 Tenets

The tenets are the constitution. When a tenet conflicts with speed or convenience, the tenet wins. When two tenets conflict, the earlier one in this order wins (D-5): T-5, T-2, T-3, T-4, T-7, T-1. T-6 is absolute and never conflicts.

- **T-1. Readable, simple, not wasteful.** Explicit over implicit. A fresh model must understand a function from the function and its helper signatures. Helpers go one level deep. Two concrete cases before any abstraction. No clever one-liners. Tune only on measurement.
- **T-2. Zero silent failures.** No swallowed error. An absent value is an error, never a zero. Every error carries its context. Assertions stay on in shipped builds.
- **T-3. Tests cover everything.** No merge without tests. A bug fix ships with a regression test that fails on the old code.
- **T-4. Cross-provider review before merge.** The provider that wrote the code does not review it. The review file records the findings (D-17).
- **T-5. Document everything.** Continuity is the first duty. Each session adds its handoff entry. The other documents update when intent, a decision, or a plan changes.
- **T-6. No attribution.** No code, game text, commit, PR description, or GitHub comment names an agent, harness, or model as the source of work (D-22). Two places are exempt: the author field in the session handoff, and the review files.
- **T-7. Deterministic simulation.** Every run replays from a seed and an input record. The core uses integer math, seeded random streams, and no clock. A replay gives the same state hash on every platform (D-6).

### 6.2 Guardrails

1. **G-1.** The `core` crate has no terminal, file, network, clock, or OS dependency. A test asserts the dependency list.
2. **G-2.** No `f32` or `f64` in `core`. Fixed-point integers carry every rate. The lint tool enforces it (D-6).
3. **G-3.** No `std::time`, `Instant`, `SystemTime`, or OS-seeded random in `core`. The seed and the tick are the only sources of randomness and time (D-6).
4. **G-4.** One seeded stream per subsystem, and a fixed iteration order wherever the order reaches the state (D-6).
5. **G-5.** Every run records its seed, content hash, versions, and inputs from the first tick. A replay reproduces the state hash, and the `replay-identity` job proves it on three platforms before merge (D-6).
6. **G-6.** Every content file refuses an unknown field and fails on an absent field, at load and in a test (D-7).
7. **G-7.** No inline string that the player sees. Every player string has an id in the string table (D-7).
8. **G-8.** One concern per PR (L-1).
9. **G-9.** No unowned decision. A session that hits an open question files it and stops (D-19).
10. **G-10.** Ids in this file and in the registers never change (D-13).
11. **G-11.** No co-author trailer, generation line, or model name in a commit, PR, or comment (T-6).
12. **G-12.** Every document follows ASD-STE100. The `ste-check` job runs the checker in the PR gate (D-10).
13. **G-13.** Every dependency has a decision entry that justifies it.
14. **G-14.** Every optimization has a profile before it and a measurement after it.
15. **G-15.** Squash merge by the owner, from a short branch, with a conventional commit subject (D-8).
16. **G-16.** A PR that creates a check passes that check. A PR names any check that does not exist yet, with the PR that creates it (L-11).
17. **G-17.** Every `core` behavior change bumps the simulation version constant, and the review confirms it.
18. **G-18.** No `unwrap`, `expect`, or `panic!` outside tests. No `let _ =` on a `Result` (T-2).
19. **G-19.** Every screen designs to 120 by 40 in 16 colors and ASCII. The 256-color Unicode set is the upgrade (D-48, D-49). A screen test renders both sets.
20. **G-20.** Every player string follows the `game-text-style` skill, and the owner approves each text batch in its PR (D-57, D-63).
21. **G-21.** Every enemy profile validates at load, and a profile that can never act fails the load (D-65, T-2).
22. **G-22.** The night gate is green before merge, once PR-15 creates it. It needs a success record from a night inside 48 hours (D-64).

## 7. Roadmap

Five phases. Gate 1 is a foundation gate with no play. Gates 2 to 5 are builds that the owner plays and signs off on feel, each with a written exit test (D-52). Ids: PR-# code changes, M-# measurements. Focused roadmaps in `docs/roadmaps/` expand each phase with per-PR exit tests, once a phase starts. Each entry cites its decisions and never restates them.

### Phase 1: Foundations (gate: CI green on three platforms with an identical state hash, docs and PR gate live, no play)

**PR-1: Repository scaffold.**
Create the cargo workspace with the `core`, `tui`, and `tools` crates (OQ-6). Pin the toolchain in `rust-toolchain.toml`. Add the Makefile with `verify`, `where`, `hooks`, `test`, `lint`, `ste-check`, and `run` (D-3). Add the pre-commit hook (D-8).

Add the CI workflow that builds, tests, runs clippy, and checks the format on Linux, macOS, and Windows (D-2). Add the `ste-check` workflow on the interim Python script (D-10). Add a test that asserts `CLAUDE.md` and `AGENTS.md` are identical (D-20). No game code.
Gate: `make verify` passes on this machine, and the three CI legs and `ste-check` pass on the PR.
> *In plain English:* this makes the empty project with its three parts and the checks that every future change must pass. It adds nothing that plays. It is safe because it changes no behavior.

**PR-2: STE checker in Rust.**
Port `docs/tools/ste-check.py` to the `tools` crate as the `ste-check` command (D-10). Add the reference check that flags a citation of a superseded decision without its successor. Add the session number check that flags a duplicate session heading. Retire the Python script and move the `ste-check` workflow to the Rust tool. Settle F-5.
Gate: the checker passes on itself, on this file, and on the skills, and it fails a fixture file for each rule.
> *In plain English:* this replaces the borrowed script with a tool in the project language. Documents are the project's memory, so the tool guards that memory.

**PR-3: Review gate.**
Add the `review-gate` command to the `tools` crate and its workflow on `pull_request_target` (D-15). The workflow runs the tool from the base branch and fetches the PR head as data. The tool applies the three rules of the `pr-review` skill and the override rules of D-16, and it publishes a check run.
Gate: the job gives success on a fixture PR with an approved record, and failure on a stale head. It gives success on a documentation PR with the label.
> *In plain English:* this adds a check that turns red when a change has no approved review from the other provider. The owner then requires it on `main` (OQ-3).

**PR-4: Random streams, fixed-point math, det-lint, and replay identity.**
Implement the seeded streams, one per subsystem, split from the run seed (G-4). Implement the fixed-point types. Implement the `det-lint` command that refuses a float, a clock, an OS random, or an inline player string in `core` (G-2, G-3, G-7). Implement the state hash and the `replay-identity` job that runs a fixed seed set on three platforms and compares the hashes (G-5).
Gate: this PR passes its own lint and its own identity job, and the lint fails a fixture that uses `f32`.
> *In plain English:* different computers can give different answers for decimal math. This adds our own integer math and a check that proves the same result everywhere on every change.

**PR-5: Content loader and string table.**
Implement the RON loader with unknown fields refused and an absent field as an error (D-7, G-6). A load failure names the file, the field, and the reason. A test loads every content file. Implement the id-keyed string table with the two glyph sets and the two palettes as content (D-49, G-7).
Gate: a content file with an absent field fails the load test with the field name.
> *In plain English:* every job, spell, and item lives in a data file with a strict shape. A file with a gap fails loudly instead of a silent zero.

**PR-6: Simulation loop, input record, replay, and save.**
Implement the loop, the input record, and the run record. The record header holds the format version, the simulation version, the content hash, the seed, and the initial state (G-5). Implement the recorder, the replay, and the compaction rule: a snapshot plus the inputs since it (F-10).

Implement the save file as a record in the platform config directory, one slot and one autosave (D-62). Property tests over one thousand seeds assert that a replay reproduces the end-state hash and that a version mismatch produces a contextual report.
Gate: the replay of a recorded run gives the same hash on all three platforms, and a save reloads to the same hash.
> *In plain English:* the game writes down its start state and every input. That record then plays any run again, so every bug becomes repeatable, and the save file is that record.

**M-1: Tokens per PR.** Record the harness usage per PR for the first ten PRs.

**M-2: CI wall time per PR.** Record the wall time of each CI job per platform for the first ten PRs.

### Phase 2: First playable (gate: the owner plays one hub and one dungeon with a job change and a shop, D-51)

**PR-7: Tile map, movement, sight, and the map screen.**
Define the layout content format: a grid of glyph ids per tile, doors, chests, save points, spawn points, and markers for secrets (D-38, D-39, D-41). Implement movement with arrow keys and vi keys (D-50), sight, and the fog over tiles the party never saw. Draw the map screen in `tui` at 120 by 40 with the side panel, and the size message below the floor (D-48, F-9, G-19).
Gate: the party walks a fixture dungeon on all three platforms, and a window below the floor shows the message and no broken screen.
> *In plain English:* this is the first thing you can open and move in. The dungeon is a grid of glyphs, and the party walks it one tile at a time.

**PR-8: Enemies on the map.**
Implement fixed enemies and patrols with sight (D-37). A patrol that sees the party starts an encounter, and a party that reaches an enemy from behind gets the first turn. No random encounters.
Gate: property tests over one thousand seeds assert that a patrol never leaves its route and never sees through a wall.
> *In plain English:* enemies stand and walk in the dungeon where you can see them. You choose the fight, or you sneak past, or they catch you.

**PR-9: Battle core and timeline.**
Implement the encounter state, the timeline, and the speed rule that orders it (D-29). Implement actions, damage in fixed-point, the six to eight elements with weakness, resist, and absorb, and the ten statuses (D-43, OQ-12, OQ-13). Implement haste, slow, and heavy actions as timeline shifts. Three characters and up to six enemies. Down and party wipe (D-36).
Gate: property tests over one thousand seeds assert that the timeline never stalls and that every status ends.
> *In plain English:* this is the fight itself, with the order of turns visible and shaped by speed. Nothing draws it yet.

**PR-10: Battle screen.**
Draw the timeline, the party panel, the enemy panel, the action menu with letter hotkeys, and the message log (D-50, G-19). Every message comes from the string table in the game voice (G-7, G-20). Both glyph sets and both palettes render.
Gate: a screen test renders a fixture battle in both sets, and the owner reads a fight from the screen alone.
> *In plain English:* the fight appears on screen: who acts next, who is low, what you can do. Every line reads in the voice of the game.

**PR-11: Evaluator and enemy profiles.**
Implement the tactical evaluator that scores every legal action by its simulated outcome: damage, kills, threat, healing, and timeline shift (D-65). Define the profile content format with the term weights and the traits, and its validator (G-21). Four profiles for the first dungeon. Boss phases come in PR-20.
Gate: a fixture enemy with a protector profile heals its ally before it attacks, and a profile with no legal action fails the load.
> *In plain English:* enemies think. Each one weighs what a move does before it acts, and each kind of enemy weighs it differently.

**PR-12: Jobs, levels, and abilities.**
Implement the character level from experience and the job level from ability points (D-34, OQ-16). Implement the ability list per job, the learned set that a character keeps, and the secondary set (D-32). Implement MP and its recovery rule (D-42). Four jobs as content, each with one no-MP ability, and reserve experience per OQ-9 (D-55, OQ-11, F-8).
Gate: a character learns an ability, changes job, and keeps it. A test proves that every job has a no-MP ability.
> *In plain English:* each character has a job, gets better at it, and keeps what they learned when they switch. Four jobs exist.

**PR-13: Gear, items, and inventory.**
Implement the six equipment slots, the job restrictions, and the inventory (D-44). Fixed items with rarity tiers as content (D-45). The equip screen shows an empty slot after a job change.
Gate: a job change that forbids the current weapon leaves the slot empty and the screen shows it.
> *In plain English:* weapons, armor, and accessories go on the characters, and each job wears what it can.

**PR-14: Hub services and the hub screen.**
Implement rest, save, job change, party swap, and the shop with gold (D-59, D-60, D-62). Define the hub content format with the services each hub offers (D-28). Draw the hub screen and the shop screen.
Gate: the party rests, buys, changes jobs, swaps a reserve character, and saves, and the save reloads to the same hash.
> *In plain English:* the hub is where the party recovers, trades, and reshapes itself before the next dungeon.

**PR-15: Headless runner, bots, and the night gate.**
Implement the headless runner in `tools` with a random policy and a greedy policy (D-64). A few hundred runs per PR and ten thousand each night. The night job writes a result record, and the `night-gate` job reads it (G-22). Each run ends as complete, softlock, crash, or budget, and each failure names its seed.
Gate: ten thousand night runs of the two policies on the fixture dungeon complete with zero crashes and zero softlocks.
> *In plain English:* simple robots play thousands of runs every night without a screen. They find crashes and dead ends before a person ever sees them.

**PR-16: Dungeon parts, death, and save points.**
Implement treasure, locked doors and keys, traps and hazards, and save points with the party swap (D-36, D-41, D-58). A wipe reloads the autosave. The dungeon exit returns the party to the hub.
Gate: a bot run that wipes reloads and continues, and a two-character party after a down can still reach the exit in the fixture.
> *In plain English:* the dungeon gains its chests, doors, traps, and resting places, and death now costs what the design says it costs.

**PR-17: The first hub and the first dungeon.**
Author the first hub and the first dungeon as content (D-28, D-39). That is the layout, the enemies with their profiles, the treasure, the shop stock, and a placeholder scene. The four jobs and the first three cast members have their text in the voice (G-20).
Gate: the owner plays from the hub through the dungeon and back, and signs off on feel (D-52). The M-4 numbers land inside the band the sign-off sets.
> *In plain English:* the first real place to play. Everything before this was machinery.

**M-3: Night run wall time.** Record the night duration and the crash and softlock counts for seven nights.

**M-4: Encounter numbers.** Record turns per encounter and party downs per dungeon by bot policy on the first dungeon. Binds the resource numbers of D-35.

### Phase 3: Story systems (gate: the owner plays a branch that closes a route and a scene that changes a relationship)

**PR-18: Story flags, branches, and scenes.**
Implement the flag set, the branch conditions in content, and the scene format with dialogue choices (D-40). A closed route, a lost ally, and a changed hub are three flag effects.
Gate: a fixture branch closes a route, and a replay reproduces the branch.

**PR-19: Reputation, relationships, quests, and the rumor board.**
Implement the faction reputation model, the relationship value per cast member, the quest state, and the rumor board in the hub (D-40, D-59).
Gate: a fixture quest completes, and a hub line changes with reputation.

**PR-20: Boss phases and signature moves.**
Implement the scripted phase layer over the evaluator (D-65). A phase changes the profile and adds a move. One boss for the first dungeon.
Gate: the boss changes phase at the scripted threshold in every one of one thousand seeds.

**PR-21: Puzzles and secrets.**
Implement switches, pushable blocks, light and dark, hidden rooms, and secret markers (D-41).
Gate: a fixture puzzle opens a door, and a hidden room stays hidden until found.

**PR-22: Jobs five to eight.**
Four more jobs as content, with their text (D-55, OQ-11).
Gate: every job has a no-MP ability, and the M-4 band holds with the new jobs.

> *In plain English for Phase 3:* the game learns to remember what you chose and to answer it. Bosses gain their set pieces, dungeons gain their puzzles, and the job list doubles.

### Phase 4: Region one content (gate: the owner plays region one end to end and signs off, D-56)

**PR-23 to PR-26: Dungeons two to four.** One content PR per dungeon, with enemies, profiles, a boss, treasure, puzzles, and secrets.

**PR-27: The second hub.** A hub of another shape than the first (D-28), with its services and scenes.

**PR-28 and PR-29: The arc.** The scenes, the branches, the decisions, and the cast text of region one, in two batches (D-56, D-57, OQ-14).

**PR-30: Balance pass.** Tune the numbers of D-35 and D-60 on the M-4 band and the night runs. Every change reports the number before and after (G-14).

**M-5: Region one play time.** The owner's play time from the first hub to the end of the arc, against the six to eight hours of D-56.

> *In plain English for Phase 4:* the first release takes shape. Four dungeons, two hubs, one story, and the numbers tuned by robots and by play.

### Phase 5: First release (gate: a tagged release with three binaries that a fresh machine runs)

**PR-31: Release workflow.** Build a binary per platform on a tag and publish a GitHub Release (D-53). The runbook explains the macOS warning.

**PR-32: Terminal fallback pass.** Verify every screen in 16 colors and ASCII on Windows console and over SSH (D-49, G-19).

**PR-33: The title screen, the size check, and the exit.** The first screen, the message below 120 by 40 (F-9), and a clean exit that saves.

> *In plain English for Phase 5:* the game becomes something a person downloads and runs.

### Phase 6: Region two and later

Parked until Gate 5. Each later region repeats Phase 4 with its own roadmap.

## 8. Sequence (strict order, single owner)

1. Owner: install Rust (OQ-2), install gitar (OQ-1), create the `review-override` label.
2. Owner: answer OQ-6 and approve the voice skill (OQ-15).
3. PR-1, PR-2, PR-3.
4. Owner: require the checks on `main` (OQ-3).
5. PR-4, PR-5, PR-6.
6. M-1, M-2.
7. **← GATE 1 (foundation).** The identity job, `cargo test`, and `ste-check` are green on three platforms.
8. Owner: answer OQ-9, OQ-11, OQ-12, OQ-13, OQ-16.
9. PR-7, PR-8, PR-9, PR-10.
10. PR-11, PR-12, PR-13, PR-14.
11. PR-15. One night runs, then the `night-gate` job joins the PR gate.
12. PR-16, PR-17.
13. M-3, M-4.
14. **← GATE 2 (first playable).** The owner plays one hub and one dungeon and signs off on feel.
15. Owner: answer OQ-14.
16. PR-18, PR-19, PR-20, PR-21, PR-22.
17. **← GATE 3 (story systems).** The owner plays a branch and a relationship scene.
18. PR-23 to PR-26, PR-27.
19. PR-28, PR-29, PR-30.
20. M-5.
21. **← GATE 4 (region one).** The owner plays region one end to end.
22. PR-31, PR-32, PR-33.
23. **← GATE 5 (first release).** A fresh machine runs the tagged binary.
24. Phase 6 stays parked.

## 9. Open questions

The open questions register is `docs/questions.md` (D-19). It holds OQ-1 onward with options, recommendations, what each blocks, and the date and decision that resolve each one. File a new question there, not here. Ids never change.
