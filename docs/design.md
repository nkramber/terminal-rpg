# terminal-rpg: Design and Roadmap

Status: **design document v2, pre-production.** This file supersedes `docs/archive/design-v1-terminal-2026-09-12.md`, the terminal plan. Its source is the decision register `docs/decisions.md`, entries D-1 onward. The owner recorded every decision on 2026-09-12: D-1 to D-25 in the repository interview, D-26 to D-65 in the roadmap interview. D-66 to D-98 came in the pivot interviews, and D-99 to D-122 in the engine interview. D-123 onward came in the world-building interview, which D-142 widened to a full roadmap before PR-1.

Nothing in this file is code. Each plan item ships as one pull request.

2026-09-12 pivot pass: v2 refutes the terminal premise of v1 twice. D-78 moved the game out of the terminal into a window with a terminal look. D-98 ended the terminal look and made the game sprite-based. D-99 replaced Rust with Godot 4 and C#. The v1 file stays in the archive unchanged. The ids of v1 stand: an item that keeps its purpose keeps its number, PR-32 is retired, and new items start at PR-34 (G-10).

2026-09-12 world and full-plan pass: the world-building interview set the setting (D-123 to D-159) in `docs/world/`. Two owner instructions widened the PR. D-139 plans 2D effects from the start, and D-142 puts a full roadmap before PR-1. Region one became a free prologue, a Steam demo of the full game (D-133, D-143). F-21 and F-22 record two faults of the interview options, and F-23 records a gate that headless CI cannot run. D-227 and D-228 replaced the 640 by 360 frame with 1280 by 800 and 32-pixel tiles.

2026-09-13 critic pass: the design-critic agent read the plan after the frame change and found 13 defects. F-25 to F-27 record them, and D-255 to D-258 close four.

2026-09-13 cast pass: the cast block of the world-building interview replaced the job system (D-267 to D-299). Characters gain abilities from lessons, the rites and drills that any character equips. Each character has a main aptitude and a hidden side aptitude. D-277 ended every port from another repository, so each tool is new work. PR-22 is retired, and PR-42 takes the lessons of region one in Phase 4 (D-304).

2026-09-13 second critic pass: the design-critic agent read the plan after the job system change and found 14 defects. F-28 records them. D-301 to D-308 settle C-1, C-3, C-5, C-7, C-10, and C-14. D-309, D-351, D-356, D-363, and D-375 answer OQ-48, OQ-49, OQ-38, OQ-50, and OQ-51, so no question of the pass remains.

2026-09-13 arc pass: the arc block set the story of region one in `docs/world/arc.md` (D-309 onward). Elio is the one death in the cast, after region one. The relationship value and the faction reputation left the game, and a choice is a story flag (D-328, D-329). F-29 records a count of PR ids that the second visit to the cells settles.

2026-09-13 systems pass: the systems block settled the lessons, the battle rules, the items, the statuses, and the law in play (D-356 to D-397). The owner moved the start of the game to the village of Marrek (D-368 to D-373).

External facts, verified 2026-09-12:

- The GitHub repository `nkramber/terminal-rpg` is public. Source: `gh repo view`, run 2026-09-12.
- Branch protection with required status checks is free on a public repository. Source: docs.github.com, "About protected branches", read 2026-09-12.
- Godot 4.7.2 is the current release for both editions, dated 2026-08-18, and the .NET LTS pin is .NET 10. Source: the what-you-carry design header, verified there on 2026-09-07. PR-1 verifies both again on the Godot download page.
- The development machine has .NET 10.0.400 and Godot 4.7.2 .NET at `/Applications/Godot_mono.app`. Source: `dotnet --version` and the what-you-carry runbook, 2026-09-12.
- The Steam Deck screen is 1280 by 800, a 16 to 10 aspect. Source: the Steam Deck tech specs page, read 2026-09-12.
- A Steam demo is a separate app ID linked to the full game. It can launch while the store page of the full game says "Coming Soon". Source: Steamworks, "Demos", read 2026-09-12.
- A demo save can move to the cloud storage of the full game through the `Shared cloud APP ID` field. Source: Steamworks, "Demos" and "Steam Cloud", read 2026-09-12. No page states whether a demo needs its own Steam Direct fee.
- The Godot 4.7 renderer table marks 2D rendering features as supported on Forward+, Mobile, and Compatibility. Compatibility lacks 2D MSAA, particle trails, and particle SDF collision. Source: Godot docs, "Overview of renderers", read 2026-09-12.
- In Godot, `--headless` "disables all rendering code". Source: godot-proposals issue 5790, open, read 2026-09-12.
- Godot's own CI runs the engine under `xvfb-run` with `--rendering-driver opengl3`. Source: `.github/actions/godot-project-test/action.yml` in the Godot repository, read 2026-09-12.
- In Movie Maker mode, faster hardware renders sooner, "but the visual output remains identical", and "the window size is clamped by your display's resolution". Source: Godot docs, "Creating movies", read 2026-09-12.
- HDR for 2D works "when using the Forward+ and Mobile rendering methods", and "When using the Compatibility rendering method, glow uses a different implementation". Source: Godot docs, "Environment and post-processing", read 2026-09-12.

Text rules: this file follows ASD-STE100 (D-10). Tables are exempt from sentence-length counts.

## 1. Thesis

terminal-rpg, a working title (D-102), is a dark fantasy role-playing game in 32-pixel sprites at 1280 by 800 (D-27, D-107, D-228). Its tentative name is The Thing Below (D-215). A fixed cast (D-33, D-299) travels between hubs of every shape, a castle town, a cave community, a boat, an airship (D-28). Between the hubs lie hand-authored dungeons with visible enemies, traps, puzzles, and secrets (D-37, D-39, D-41). Three fight at a time on a visible timeline where speed decides the order (D-29, D-31). Any character equips lessons, the rites and drills that give abilities, and each character does one kind of ability best (D-272, D-274, D-278).

Combat is hard because enemies think and resources run out (D-35), and a fallen character stays down until a hub (D-36). Decisions close routes, lose allies outside the cast, and change hubs (D-40, D-301).

The game runs on Godot 4 with C# (D-99). The simulation lives in an engine-free Core library that replays any run from a seed and an input record (D-100, T-7). Sprites, tiles, and portraits are text grids in content that a tool renders into an atlas (D-107). A full CRT shader sits over the frame with a toggle (D-105, D-120). Particles, 2D light, and shaders enter the plan from the start (D-139).

The goal is a Steam release, and the Steam Deck is the readability and performance floor (D-85, D-92).

A full roadmap comes before any code (D-142). The plan puts the foundations first, because every later system depends on them. Those are a deterministic core, a run record with replay, the content loader, the atlas tool, and the document gates. The first playable is the village, one hub, and one dungeon, with lessons and a shop (D-51, D-268, D-362, D-369). The owner judges feel there, on the desktop and on the Deck. 

The story systems come third, because they need the loop. Region one, two hubs and four dungeons in one arc, is the first release (D-56). It ships free, as a Steam demo of the full game (D-133, D-143). Every plotline converges at the end of the game (D-131). Five gated phases hold that order.

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
14. **L-14. Ask the medium question first.** The first interview asked about the language before it asked what the player sees. Two pivots followed in one day (D-78, D-98). The next project asks about the screen before the stack.
15. **L-15. Never claim a tool is absent without a check.** Six files said gitar was not installed. It was (F-12).

## 3. System map

| Component | Project | Reads | Writes | Sensitivity |
|---|---|---|---|---|
| Simulation loop | Core | intent stream, seed, content | state, run record | Total. Every replay depends on it |
| Random streams | Core | seed | numbers | Total. Cross-platform identity |
| Content loader and schemas | Core | JSON files | typed content, content hash | High. A silent default here breaks the economy |
| String table | Core | JSON files | text by id | Medium |
| Run record, replay, and save | Core | state, intents | record file, save file | Total. The crash report and the save (D-62) |
| Tile map, movement, and sight | Core | layout content, intents | party position, sight | High. Patrols and ambushes (D-37) |
| Battle and timeline | Core | party, enemies, abilities | turn order, damage, statuses | Total. The design risk (D-29, D-35) |
| Evaluator and profiles | Core | battle state, enemy profile | enemy actions | High. The largest single system (D-65) |
| Lessons, aptitudes, and levels | Core | lesson content, experience | character state | High. The build decision (D-34, D-272, D-274) |
| Gear and items | Core | item content, inventory | equipment state | Medium (D-44, D-45) |
| Story flags and quests | Core | scene and decision content, choices | flags, hub state | High. Branches multiply (D-40, D-59, D-329) |
| Hub services and the region map | Core | hub content, route content, gold | party, saves, position | Medium (D-59, D-113) |
| Map scene, battle scene, hub scene, scene runner | Game | Core state, atlas, string table | screen, intents | Medium. Cosmetic by design (D-106, D-111, D-114) |
| Dialogue box and portraits | Game | scene content, string table | screen | Medium (D-109) |
| CRT shader and the frame | Game | settings | screen | Medium. The Deck floor (D-105, D-228) |
| Audio player | Game | WAV files | sound | Low (D-115) |
| Atlas tool, audio synthesizer | Tools | grids, palette, parameter files | atlas PNG, WAV files | Medium. Committed artifacts with a match test (D-107) |
| STE checker, det-lint, review gate, night gate | Tools | source, docs, records | pass or fail | Gate |
| Headless runner and bots | Tools | policies, seeds | run records | High. The night gate (D-64) |
| Export and release | CI | tag | three builds | Low (D-53, D-85) |

## 4. Cost model (what we pay, what we do not know)

What we pay:

- Owner time: the interviews, the approvals of every text batch (D-57), and the play sign-off of every phase (D-52).
- Tokens: two harnesses, Claude Code and Codex, on every PR (D-14, D-17). The amount per PR is unknown until M-1.
- CI: GitHub-hosted minutes on three platforms per PR (D-2), plus a nightly bot run (D-64). Free on a public repository (D-4). Wall time per PR is unknown until M-2.
- Purchases: the Steam Direct fee, 100 USD, before the Steam release (D-85). No asset license and no font fee: every font is OFL (D-104, D-122). Godot is free.

Measurements that answer the unknowns:

- M-1: tokens per PR from the harness usage reports, over the first ten PRs.
- M-2: CI wall time per PR, per platform, over the first ten PRs.
- M-3: the night run wall time and the crash and softlock counts, over the first seven nights (D-64).
- M-4: turns per encounter and party downs per dungeon by bot policy, on the first dungeon. Binds the resource numbers of D-35.
- M-5: the owner's play time from the first hub to the end of the arc, against D-56.
- M-6: the Deck frame time on the first playable, against 60 frames per second (D-161). The readability of the 16-pixel font and the 32-pixel sprites at 1x, with the CRT on and off (D-92, D-120, D-228).

## 5. Defect and finding register

Status: ✅ done (code merged, or "doc" for a document-only correction) · 🔧 planned (item listed) · ⚠ constraint (binds a pull request) · ❓ needs owner input · ⏸ out of scope · 🅿 parked.

| # | Finding | Date | Status |
|---|---|---|---|
| F-1 | The harness default adds a co-author trailer to commits, and the reminder repeats in every session. D-22 forbids it | 2026-09-12 | ✅ doc. `.claude/settings.json` sets empty strings. The rule sits at the top of `CLAUDE.md` |
| F-2 | The what-you-carry review gate and STE checker are C# tools, and D-1 chose Rust. Neither tool runs here | 2026-09-12 | 🔧 D-10 and D-15. PR-2 and PR-3 write both tools as new code (D-277). The Python script is the interim checker |
| F-3 | Rust is absent from the development machine | 2026-09-12 | ❓ OQ-2. Owner action before PR-1 |
| F-4 | The repository had no commit, so no branch and no PR could exist | 2026-09-12 | ✅ D-25. The owner made the root commit `6b899dd` with an empty `CLAUDE.md` |
| F-5 | The Python checker applies the 20-word limit to every numbered item, and the C# tool applied it under a Sequence or Procedure heading alone | 2026-09-12 | ⚠ Binds PR-2. The new checker picks one rule, and the skill text follows it (D-277) |
| F-6 | D-39 took seeded dungeon variation on a replay premise, and D-46 removed the premise | 2026-09-12 | ✅ D-47. No variation. L-13 |
| F-7 | D-36 leaves a fallen character down until a hub, and a three-character party (D-31) then fights with two. No decision balances the short-handed party | 2026-09-12 | ⚠ D-58 gives a reserve and a swap at save points. Binds PR-16 and M-4 |
| F-8 | D-42 empties a caster's MP across a dungeon, and no decision gives a job a no-MP action | 2026-09-12 | ⚠ Binds PR-9 and PR-12. D-359 gives every character a basic attack with no MP cost |
| F-9 | D-48 sets the floor at 120 by 40, and a default macOS Terminal window is 80 by 24 | 2026-09-12 | ⚠ Binds PR-7: the size message names the floor and how to resize |
| F-10 | D-62 puts the run record in the save, and a record grows without bound over 20 to 40 hours (D-30) | 2026-09-12 | ⚠ Binds PR-6: the record format needs a compaction rule, a snapshot plus the inputs since it |
| F-11 | The interim checker read an HTML comment as prose. A fixture comment with a semicolon, a modal, a passive, and 30 words raised four findings. The automated pass of PR #1 found it | 2026-09-12 | ✅ doc. The script removes a one-line comment. ⚠ Binds PR-2: the new checker carries the rule (D-277) |
| F-12 | The session wrote in `CLAUDE.md`, the PR template, the skill, and OQ-1 that gitar was absent, on no evidence. The pass ran on PR #1 within a minute | 2026-09-12 | ✅ doc. D-66. Every claim about a tool needs a check |
| F-13 | The first interview fixed the language before the medium. Two pivots in one day, D-78 and D-98, reopened 30 decisions | 2026-09-12 | ✅ doc. D-99. L-14 |
| F-14 | D-88 chose curvature and bleed, and the SDL2 2D renderer of D-83 ran no shader | 2026-09-12 | ✅ doc. D-91, then D-99 moved the shader to Godot. OQ-19 |
| F-15 | A 16 by 16 sprite did not divide the 10 by 20 text cell of D-82 | 2026-09-12 | ✅ doc. D-103 sets a 16-pixel tile and a 640 by 360 frame. D-228 later sets a 32-pixel tile and a 1280 by 800 frame |
| F-16 | D-7 chose RON, and C# has no RON reader | 2026-09-12 | ✅ doc. D-116, JSON with a schema |
| F-17 | The 32-color palette (D-89) had 13 free colors for eight elements and ten statuses | 2026-09-12 | ✅ doc. D-121 grows it to 48, and D-181 to 64. Binds PR-34 |
| F-18 | The full CRT (D-105) is on by default on the Deck (D-120) before any Deck measurement | 2026-09-12 | ⚠ Binds M-6 and Gate 2: the Deck play measures readability with it on |
| F-19 | D-119 and PR-34 promised an atlas match byte for byte. The compressed bytes depend on the zlib build and the encoder, so the C# tool of PR-34 cannot reproduce them. The automated pass of PR #1 found it | 2026-09-12 | ✅ doc. The match test compares decoded pixels. The interim tool gained `--check`. Binds PR-34 |
| F-20 | The interim atlas tool kept the last of two palette entries with one key, in silence, against T-2. The automated pass of PR #1 found it | 2026-09-12 | ✅ doc. The tool fails on a repeated key. Binds PR-34 to the same rule |
| F-21 | The plan gives each region one story arc (D-56), and the glossary defined an arc as "the story of one region". No text said how an arc relates to the main story of D-28, or what the first release ends on. An interview option read the gap as a faction that falls inside region one, and the owner refuted it | 2026-09-12 | ✅ doc. D-131: every plotline converges at the end of the game. The glossary now defines an arc as one part of the main story. D-133 resolves OQ-26: region one is a free prologue on Steam. The Phase 4 summary and Phase 5 now name the prologue. Binds the arc block of OQ-18 |
| F-22 | The interview options used Final Fantasy Tactics as a template, not a feel. Three recorded answers sit close to its plot devices: unpaid veterans turned bandit (D-127), a hidden power behind the politics (D-128), and church leaders who know the faith is a lie (D-137). The waystones (D-134) risk a fourth: stones that carry the evil | 2026-09-12 | ⚠ D-136 and D-140: keep the shapes, and ban the devices. The list lives in `docs/world/`. Binds every later option of OQ-18 |
| F-23 | The gates of PR-10 and PR-37 need a rendered screen: a screen test of a fixture battle, and two screenshots of the CRT toggle. The smoke job runs Godot with `--headless` on hosted runners (D-117). Godot proposal 5790 says that `--headless` "disables all rendering code", and the Godot docs name no way to capture an image in that mode. what-you-carry met the same wall: its contact sheet needs a window and runs on a desktop alone (its D-306) | 2026-09-12 | ⚠ D-172: a Linux CI job renders under Xvfb with a pinned Mesa, and desktop contact sheets show the real renderer at milestones. Binds the technical and graphics roadmaps, PR-10, and PR-37. Sources: the Godot 4.7 command line page and proposal 5790, read 2026-09-12 |
| F-24 | D-228 doubles the tile size after the art, effect, and light decisions of this interview. Every grid holds four times the pixels: a 32 by 32 frame is 1,024 characters of text, and a party member has about twelve frames plus normal-map overrides (D-184, D-199, D-200). The Deck lights and fills four times the pixels of a 640 by 400 frame | 2026-09-12 | ⚠ Binds the graphics roadmap, the Deck test of D-160 at 1280 by 800, and M-6. The PNG import of D-107 matters more for hand edits |
| F-25 | The design critic of 2026-09-13 found four holes in play and saves. Gate 2 could not reach the two hidden jobs (C-1), a save point gave endless rest (C-2), a quit autosave could trap a run (C-3), and a Core patch would refuse old saves (C-4) | 2026-09-13 | ✅ doc. D-256, D-257, and D-258 close the first three, and D-268 later supersedes D-256. D-259 closes the fourth: a load reads the snapshot |
| F-26 | The critic found gates that cannot pass. No PR created the screen-test job of D-172, the PR-37 gate relied on a headless run that draws nothing, the PR-7 and PR-8 gates met small maps and routes per phase, and the Deck test of D-160 had no sequence step and no failure branch | 2026-09-13 | ✅ doc. PR-41 creates the job with fixed capture and fit tests at 1080 and 1440 rows. The gates of PR-7, PR-8, and PR-37 changed, and section 8 gains the Deck test. D-261: the owner sets a fallback only if the test misses 60 |
| F-27 | The critic found gaps in the records. 24 earlier rows lacked their revision notes, several lines named superseded values, and D-193 disagreed with D-202 on ambient effects. Four choices had no owner: the first turn from behind, the place of systems, audio, and release in the order, effect timings in frames, and D-171 against the rule of no conditional compilation in Core | 2026-09-13 | ✅ doc for the notes and the stale text. D-260, D-262, D-265, and D-266 settle the four choices |
| F-28 | The second critic pass of 2026-09-13 read the plan after the job system change and found 14 defects. A player choice could remove a cast member (C-1), the PR-12 gate needed the tasks of PR-19 (C-2), PR-42 came before its places (C-3), two notes overstated the aptitude count (C-4), and the law split between a license and a stamp (C-5). Stale text and notes stayed (C-6), and session readings had no owner (C-7). No PR drew the lead or wrote the tasks (C-8), a reserve swap gave fresh MP (C-9), and the watcher could stamp rites (C-10). OQ-41 gave the wrong cost of the death (C-11), three cases had no rule (C-12), words clashed (C-13), and the distance rule covers FFT alone (C-14) | 2026-09-13 | ✅ doc for C-2, C-4, C-6, C-8, C-11, and C-13. The session rejected one claim of C-6: D-282 refines D-268 and D-274 and does not revise them. D-301 to D-304 settle C-1, C-3, C-5, and the reading of D-274 in C-7. D-305 and D-306 settle the other two readings of C-7, D-307 settles C-14, and D-308 settles C-10. D-309 and D-351 settle OQ-48 and OQ-49 of C-12. D-356 settles C-9: a swap at a save point can bring fresh MP, and the balance must hold with it. D-363 and D-375 settle OQ-50 and OQ-51, the rest of C-12 |
| F-29 | PR-23 to PR-26 held four ids for dungeons two to four, which are three dungeons. The count came unchanged from v1, and no text said what the fourth id held | 2026-09-13 | ✅ doc. The second visit to the hanging cells (D-327) makes four dungeon builds after the first, and each id names one in the order of play (D-313) |

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

1. **G-1.** Core has no engine dependency and no file, network, clock, or OS dependency. A test asserts the reference list (D-100).
2. **G-2.** No `float`, `double`, or `decimal` in Core. Fixed-point integers carry every rate. The `det-lint` tool enforces it (D-6).
3. **G-3.** No `System.Random`, `DateTime`, `Stopwatch`, or `Environment.TickCount` in Core. The seed and the tick are the only sources of randomness and time (D-6).
4. **G-4.** One seeded stream per subsystem, and a fixed iteration order wherever the order reaches the state (D-6).
5. **G-5.** Every run records its seed, content hash, versions, and inputs from the first tick. A replay reproduces the state hash, and the `replay-identity` job proves it on three platforms before merge (D-6).
6. **G-6.** Every content file validates against its schema at load and in a test. An absent field is an error. No `.tres` files (D-116).
7. **G-7.** No inline string that the player sees. Every player string has an id in the string table (D-7, D-116).
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
18. **G-18.** No empty `catch` and no silent default. Every error carries its context (T-2).
19. **G-19.** Every screen designs to 1280 by 800 with 32-pixel tiles. The Steam Deck at 1x with the CRT on is the floor (D-92, D-120, D-228). Other screens fit the height, with whole-number scale as a setting (D-232).
20. **G-20.** Every player string follows the `game-text-style` skill, and the owner approves each text batch in its PR (D-57, D-63).
21. **G-21.** Every enemy profile validates at load, and a profile that can never act fails the load (D-65, T-2).
22. **G-22.** The night gate is green before merge, once PR-15 creates it. It needs a success record from a night inside 48 hours (D-64).
23. **G-23.** Godot physics, timers, and navigation never feed the simulation. The camera, the shader, the audio, and the input map live in Game (D-100, D-106).
24. **G-24.** Every sprite, tile, and portrait is a text grid in content. The atlas tool renders the PNG, and a test proves the committed atlas matches (D-107). A normal map comes from the grid, and its atlas gets the same test (D-184).
25. **G-25.** Every content batch the owner approves, sprites and text alike, appears in its PR description in full (D-57, D-107).

## 7. Roadmap

Five phases. Gate 1 is a foundation gate with no play. Gates 2 to 5 are builds that the owner plays on the desktop and on the Deck. Each has a written exit test and a sign-off on feel (D-52, D-92). Ids: PR-# code changes, M-# measurements.

An item that kept its purpose through the pivots kept its number. PR-32 is retired. New items start at PR-34 (G-10). Focused roadmaps in `docs/roadmaps/` expand each phase and each area before PR-1 (D-142, D-144). A phase roadmap gives per-PR scope and exit tests, and an area roadmap says how its area works. Each entry cites its decisions and never restates them.

### Phase 1: Foundations (gate: CI green on three platforms with an identical state hash, the smoke session green, docs and PR gate live, no play)

**PR-1: Repository scaffold.**
Create the solution with the Core, Game, Tools, and Tests projects (D-118). Pin the .NET 10 SDK in `global.json` and Godot 4.7.2 .NET in the runbook and in CI (D-99). Core is a class library with no references. Game is a Godot .NET project that references Core. Tools is a console project. Tests is an xUnit project that references Core and Tools.

Add `Directory.Build.props` with nullable on and warnings as errors. Add the Makefile with `verify`, `where`, `hooks`, `test`, `lint`, `ste-check`, and `run` (D-3). Add the pre-commit hook (D-8).

Add the CI workflow that builds, tests, and checks the format on hosted Linux, Windows, and macOS (D-2, D-117). Add the `smoke` workflow that installs the pinned Godot binary and runs the headless smoke session on each platform. The session boots, starts a run, and quits with no log errors. Add the `ste-check` workflow on the interim Python script (D-10).

Add a test that asserts `CLAUDE.md` and `AGENTS.md` are identical (D-20) and a test that asserts the Core reference list (G-1). The Phase 1 roadmap proposes three OFL pixel fonts with samples (D-122). No game code.
Gate: `make verify` passes on this machine, and the three CI legs, the smoke job, and `ste-check` pass on the PR.
> *In plain English:* this makes the empty project with its four parts and the checks that every future change must pass. It adds nothing that plays. It is safe because it changes no behavior.

**PR-2: STE checker in C#.**
Write the `ste-check` command in Tools as new code (D-101, D-277). It carries the reference check, the session number check, and the HTML comment rule (F-11). Settle F-5 on one rule for numbered items. Retire the Python script and move the `ste-check` workflow to the tool.
Gate: the checker passes on itself, on this file, and on the skills, and it fails a fixture file for each rule.
> *In plain English:* this replaces the borrowed script with a tool in the project language. Documents are the project's memory, so the tool guards that memory.

**PR-3: Review gate.**
Write the `review-gate` command in Tools as new code, with its workflow on `pull_request_target` (D-15, D-101, D-277). The workflow runs the tool from the base branch and fetches the PR head as data. The tool applies the three rules of the `pr-review` skill and the override rules of D-16 with the eligible set of D-71 and D-239. It publishes a check run.
Gate: the job gives success on a fixture PR with an approved record, and failure on a stale head. It gives success on a documentation PR with the label.
> *In plain English:* this adds a check that turns red when a change has no approved review from the other provider. The owner then requires it on `main` (OQ-3).

**PR-4: Random streams, fixed-point math, det-lint, and replay identity.**
Implement the seeded streams, one per subsystem, split from the run seed (G-4). Implement the fixed-point types. Write the `det-lint` command in Tools as new code, with these rules (D-101, D-277). In Core: no float type, no clock, no OS random, no reflection, and no `Dictionary` where order reaches the state (G-2, G-3). In Game: no inline player string (G-7). 
Implement the state hash and the `replay-identity` job that runs a fixed seed set on three platforms and compares the hashes (G-5).

Gate: this PR passes its own lint and its own identity job, and the lint fails a fixture that uses `double`.
> *In plain English:* different computers can give different answers for decimal math. This adds our own integer math and a check that proves the same result everywhere on every change.

**PR-5: Content loader, schemas, and the string table.**
Write the JSON loader as new code, with one schema type per content type (D-116, D-177, D-277, G-6). A load failure names the file, the field, and the reason. A test loads every content file. Implement the id-keyed string table (G-7).
Gate: a content file with an absent field fails the load test with the field name.
> *In plain English:* every lesson, enemy, and item lives in a data file with a strict shape. A file with a gap fails loudly instead of a silent zero.

**PR-6: Simulation loop, intent record, replay, and save.**
Implement the fixed-rate loop, the intent record for keyboard, gamepad, and mouse (D-84), and the run record. The record header holds the format version, the simulation version, the content hash, the seed, and the initial state (G-5). Implement the recorder, the replay, and the compaction rule: a snapshot plus the intents since it (F-10). A load reads the snapshot of the save alone, so a patch never breaks a save (D-259).

Implement the save file as a record in the platform config directory: one slot, one autosave, and a one-use resume file (D-62, D-258). Property tests over one thousand seeds assert that a replay reproduces the end-state hash and that a version mismatch produces a contextual report.
Gate: the replay of a recorded run gives the same hash on all three platforms, and a save reloads to the same hash.
> *In plain English:* the game writes down its start state and every input. That record then plays any run again, so every bug becomes repeatable, and the save file is that record.

**PR-34: Atlas tool, palette, and the grid format.**
Port `docs/tools/make-atlas.py` into Tools as the `atlas` command (D-107, D-119). Define the grid schema (D-108, D-109). A sprite or a tile is a 32 by 32 grid, and a portrait is a 64 by 64 grid (D-228, D-234). The session redraws the four test sprites at 32 by 32 for the owner's approval (D-233). A sprite has a frame list.

The palette is the 64-color file (D-121, D-181). The tool also builds a normal map for each grid, with optional override grids (D-183, D-184). A test decodes the committed atlas and proves that its pixels match the grids. It never compares file bytes, because the compressed bytes depend on the encoder (F-19). Retire the Python script.

Gate: the tool reproduces the pixels of `content/sprites/atlas.png` from the four grids. A grid with an unknown key fails with the file, the line, and the column. A palette with a repeated key fails with the key.
> *In plain English:* every picture in the game is a text file of letters, one per pixel. A tool turns those letters into the image the engine draws, and a test proves the image matches the letters.

**M-1: Tokens per PR.** Record the harness usage per PR for the first ten PRs.

**M-2: CI wall time per PR.** Record the wall time of each CI job per platform for the first ten PRs.

### Phase 2: First playable (gate: the owner plays one hub and one dungeon with lessons and a shop, on the desktop and on the Deck, D-51, D-92, D-268, D-362)

**PR-7: Tile map, movement, sight, and the map scene.**
Define the layout content format: a grid of tile ids, doors, pickable locks, traps, chests, save points, spawn points, and markers for secrets (D-39, D-41, D-386). Implement tile-locked movement, sight, and the fog over tiles the party never saw, in Core. 
Draw the map scene in Game at 1280 by 800, fit to the window (D-232), with the camera on the lead (D-106, D-228, D-292, D-306). Map the arrow keys and the gamepad stick and pad to intents (D-84, D-219).
Gate: the party walks a fixture dungeon on all three platforms with a keyboard and with a gamepad. The camera never scrolls past the edge of a map larger than the view, and a smaller map sits centered.
> *In plain English:* this is the first thing you can open and move in. The dungeon is a grid of tiles, the party walks it one tile at a time, and the view follows.

**PR-41: Screen-test job.**
Add the Linux CI job of D-172. It installs a pinned Mesa and runs Godot under Xvfb with the OpenGL driver. It captures fixture scenes and compares the frames by pixel with a committed CI baseline.

Fix every source of change at capture: the particle seeds, the CRT flicker phase, and the time of day. Capture the fit of D-232 at 1080 and 1440 screen rows, to catch aliasing in the scanlines (D-240). Add the desktop command that makes a contact sheet with the real renderer (D-172).
Gate: the job passes on the map scene of PR-7, and it fails when one pixel of the baseline changes. Two runs give the same frames.
> *In plain English:* the computers that check each change have no screen. This job gives them one with a fixed picture, so a broken screen fails before it merges.

**PR-8: Enemies on the map.**
Implement fixed enemies and patrols with sight (D-37). A patrol that sees the party starts an encounter, and the side that reaches the other from behind acts first (D-265). After a flee, the group returns to its route, and no battle with it starts for a short grace time (D-381). No random encounters. Enemies that move walk with three views, and enemies that stand flip on the tick (D-108, D-207).

Gate: property tests over one thousand seeds assert that a patrol never leaves the route of its phase and never sees through a wall. A large enemy never leaves its area (D-193, D-209). A fled group starts no battle inside its grace time (D-381).
> *In plain English:* enemies stand and walk in the dungeon where you can see them. You choose the fight, or you sneak past, or they catch you.

**PR-9: Battle core and timeline.**
Implement the encounter state and the timeline, where each action pushes its user back by a delay (D-29, D-376). Implement actions, a basic attack for every character, damage in fixed-point, the eight elements with weakness, resist, and absorb, and the ten statuses (D-74, D-75, D-359). Implement haste, slow, and heavy actions as timeline shifts. One to three characters and up to six enemies (D-31, D-336). Down and party wipe (D-36).

Implement a front row and a back row for each side, where melee reaches the front row while anyone stands in it (D-377). Implement a flee command whose chance rises with party speed, with a lost turn on a failure and no flight from a boss (D-378). A step to the other row and the use of an item each cost a delay (D-380, D-382).
Gate: property tests over one thousand seeds assert that the timeline never stalls and that every status ends. Melee never reaches a back row while its front row stands, and no flee starts in a boss fight (D-377, D-378).
> *In plain English:* this is the fight itself, with the order of turns visible and shaped by speed. Nothing draws it yet.

**PR-10: Battle scene.**
Draw the side view with the pixel font the owner picked (D-104, D-111, D-122). Enemies sit on the left and the party on the right, each side in a front row and a back row (D-377). The timeline strip runs across the top, and the command menu and the status sit at the bottom. The attack pose plays on an action, and a color flash on a hit (D-96, D-108). Every message comes from the string table in the game voice (G-7, G-20). A backdrop per place.

Gate: a screen test renders a fixture battle, and the owner reads a fight from the screen alone.
> *In plain English:* the fight appears on screen: who acts next, who is low, what you can do. Every line reads in the voice of the game.

**PR-11: Evaluator and enemy profiles.**
Implement the tactical evaluator that scores every legal action by its simulated outcome: damage, kills, threat, healing, timeline shift, and row placement (D-65, D-377). Define the profile content format with the term weights and the traits, and its validator (G-21). Each profile carries a steal list of items and gold (D-383). Four profiles for the first dungeon. Boss phases come in PR-20.
Gate: a fixture enemy with a protector profile heals its ally before it attacks, and a profile with no legal action fails the load.
> *In plain English:* enemies think. Each one weighs what a move does before it acts, and each kind of enemy weighs it differently.

**PR-12: Lessons, aptitudes, and levels.**
Implement the character level from experience, and half experience for the reserve and for a downed character (D-34, D-73, D-387). Experience from an enemy shrinks as the party outlevels it (D-388). Implement lessons, the rites and drills that any character equips to gain abilities (D-272, D-275, D-278). Implement the main aptitude and the side aptitude of each character, with the side aptitude hidden until its task ends (D-274, D-282, D-283). Implement MP and its recovery rule (D-42).

Lesson slots sit on the character, grow with the character level, and swap at hubs and save points (D-356). An equipped lesson grows for the character who carries it, and each character keeps that growth (D-357, D-361). An aptitude adds a bonus to lessons of its kind, and a side aptitude adds half (D-358, D-360). Mend rites and rites that cure afflictions also work from the menu outside battle (D-391). The first playable holds Marrek, Bergit, and Dagvar (D-362).

Gate: a character equips a lesson and uses its ability in a fixture battle. A fixture flag unlocks a side aptitude, and the menu shows nothing there before the flag (D-283). An equipped lesson gains points from a fixture battle, and a save point swaps lessons (D-356, D-357). A lesson passed back to a character resumes at the level of that character (D-361).
> *In plain English:* abilities come from rites and drills that anyone can carry. Each character is best at one kind, and a hidden second kind opens through a personal task.

**PR-13: Gear, items, and inventory.**
Implement the six equipment slots and the inventory (D-44). Fixed items with rarity tiers as content (D-45). Any character wears any gear (D-374). The pack holds a small, fixed number of each item, and an item restores less in battle (D-382). A small set of items gets used up, and a find over the limit stays where it lies (D-384, D-385).

Gate: a character equips and removes gear in each slot, and the screen shows each empty slot. A find over the stack limit stays in its chest, and the save records what remains (D-385).
> *In plain English:* weapons, armor, and accessories go on the characters, and the screen shows what each one wears.

**PR-14: Hub map, NPCs, and services.**
Implement the hub as a walkable map with NPC sprites (D-112). The services are buildings and NPCs: rest, save, party swap, and the shop with gold (D-59, D-60, D-62, D-268). Define the hub content format with the services each hub offers (D-28). Draw the service screens.
Gate: a fixture party of four walks the hub, rests, buys, swaps the reserve, and saves, and the save reloads to the same hash (D-362). The lead moves to the reserve, and the lead still walks the map with the camera on it (D-292, D-306).
> *In plain English:* the hub is a place you walk through, where the party recovers, trades, and reshapes itself before the next dungeon.

**PR-36: Scene runner, dialogue box, and portraits.**
Define the scene script format (D-109, D-114). Sprites move and face by script. A dialogue box with the portrait and the choices sits at the bottom. Implement the runner in Game and the choice result in Core. Fixture portraits as 64 by 64 grids, because PR-28 and PR-29 draw the portraits of the cast (D-234).
Gate: a fixture scene walks two sprites, shows a line with a portrait, and records a choice in the run record.
> *In plain English:* the story plays out on the map with the characters you already know, and your choices land in the box under them.

**PR-15: Headless runner, bots, and the night gate.**
Implement the headless runner in Tools with a random policy and a greedy policy (D-64). A few hundred runs per PR and ten thousand each night. Write the night job and the `night-gate` command as new code: the night writes a result record, and the `night-gate` job reads it (G-22, D-101, D-277). Each run ends as complete, softlock, crash, or budget, and each failure names its seed.
Gate: ten thousand night runs of the two policies on the fixture dungeon complete with zero crashes and zero softlocks.
> *In plain English:* simple robots play thousands of runs every night without a screen. They find crashes and dead ends before a person ever sees them.

**PR-16: Dungeon parts, death, and save points.**
Implement treasure, locked doors and keys, traps and hazards, and save points with the party swap and the lesson swap (D-36, D-41, D-58, D-356). A Theft drill on one of the three who fight opens a lock marked as pickable, and it reveals and disarms traps (D-386). A wipe reloads the newer of the slot save and the autosave (D-231). A save point restores MP once per visit and no health, and a killed enemy stays dead until the party leaves (D-257, D-389). The dungeon exit returns the party to the region map.

Poison, blind, and silence last past a battle until a cure or a rest at a hub (D-390). Poison ticks on the map and can down a character, and silence stops rites cast from the menu (D-392, D-393). When poison downs all three who fight on the map, the party wipes, even with a healthy reserve (D-397).
Gate: a bot run that wipes reloads and continues, and a two-character party after a down can still reach the exit in the fixture. A fixture party that poison downs on the map wipes and reloads, even with a healthy reserve (D-397).
> *In plain English:* the dungeon gains its chests, doors, traps, and resting places, and death now costs what the design says it costs.

**PR-35: Region map.**
Implement the region map screen with nodes and routes (D-113). The party moves node to node. A route opens and closes with a flag. One hub and one dungeon as the first nodes.
Gate: a closed route refuses the move and the screen shows why, and a replay reproduces the path.
> *In plain English:* between places the party travels on a map of the region, along routes the story opens and closes.

**PR-37: CRT shader and the toggle.**
Implement the full CRT as a Godot screen shader: curvature, bleed, flicker, on by default with a toggle in settings (D-105, D-120).
Gate: the screen-test job of PR-41 captures the toggle on and off, and the two frames differ.
> *In plain English:* the whole screen looks like an old monitor, and one setting turns it off.

**PR-38: Audio synthesizer and the first sounds.**
Write the synthesizer in Tools as new code (D-101, D-115, D-277). Render WAV files from parameter content at build time, with a test that the committed files match. Six effects and one track for the first dungeon.
Gate: the tool reproduces every committed WAV file, and the battle scene plays a hit sound.
> *In plain English:* every sound comes from a small text file that the tool turns into audio. The first fight makes noise.

**PR-17: The village, the first hub, and the first dungeon.**
Author the village and the land near it, the mining town, and the hanging cells as content (D-28, D-39, D-110, D-313, D-369, D-370). That is the tile sets, the layouts, the enemies with their sprites and profiles, and the backdrop. It also holds the treasure, the shop stock, the NPC sprites, the sprite set of Marrek, and a placeholder scene (D-292). Marrek, Bergit, and Dagvar and the lessons of the first playable have their text in the voice (G-20, D-362).
Gate: the owner plays from the hub through the dungeon and back on the desktop and on the Deck, and signs off on feel (D-52, D-92). The M-4 numbers land inside the band the sign-off sets, and M-6 records the Deck.
> *In plain English:* the first real place to play. Everything before this was machinery.

**M-3: Night run wall time.** Record the night duration and the crash and softlock counts for seven nights.

**M-4: Encounter numbers.** Record turns per encounter and party downs per dungeon by bot policy on the first dungeon. Binds the resource numbers of D-35.

**M-6: The Deck.** Record the frame time on the first playable against 60 frames per second (D-161). Record the readability of the font and the sprites at 1x, with the CRT on and off (D-92, D-120, D-228, F-18).

### Phase 3: Story systems (gate: the owner plays a branch that closes a route and a hub that changes with an earlier choice, D-329)

**PR-18: Story flags, branches, and scene choices.**
Implement the flag set, the branch conditions in content, and the choice effects (D-40, D-329). A closed route, a lost ally outside the cast, and a changed hub are three flag effects (D-301).
Gate: a fixture branch closes a route on the region map, and a replay reproduces the branch.

**PR-19: Quests and the rumor board.**
Implement the quest state and the rumor board NPC in the hub (D-59). The quest state carries the personal tasks, and a missed task closes at the end of its region (D-282, D-375). No reputation and no relationship value exist (D-329).
Gate: a fixture quest completes, a hub line changes with a story flag, and a finished task unlocks a side aptitude (D-282).

**PR-20: Boss phases and signature moves.**
Implement the scripted phase layer over the evaluator (D-65). A phase changes the profile and adds a move. One boss for the first dungeon, with its sprite.
Gate: the boss changes phase at the scripted threshold in every one of one thousand seeds.

**PR-21: Puzzles and secrets.**
Implement switches, pushable blocks, light and dark, hidden rooms, and secret markers (D-41).
Gate: a fixture puzzle opens a door, and a hidden room stays hidden until found.

**PR-22: Retired.** Jobs five to eight have no purpose after D-268. No later item takes the id (G-10). PR-42 in Phase 4 takes the lessons of region one (D-304).

> *In plain English for Phase 3:* the game learns to remember what you chose and to answer it. Bosses gain their set pieces, and dungeons gain their puzzles.

### Phase 4: Region one content (gate: the owner plays region one end to end on the desktop and on the Deck and signs off, D-56)

**PR-23 to PR-26: Dungeons two to four, and the return to the cells.** One content PR per dungeon build, in the order of play (D-313). PR-23 is the deep mine, and PR-24 is the second visit to the hanging cells (D-327, F-29). PR-25 is the border fort, and PR-26 is the ice crossing. Each holds a tile set, enemies with sprites and profiles, a boss, a backdrop, treasure, puzzles, and secrets.

**PR-27: The second hub.** A hub of another shape than the first (D-28), with its tile set, its NPC sprites, its services, and its scenes.

**PR-42: The lessons of region one.** The rites and drills of region one as content, across the eight kinds, with icons and text in the voice (D-275, D-281, D-304, G-20). Each lesson has a place in a dungeon, a hub, or a scene. Gate: every lesson has a place, and bot runs of region one with each side aptitude absent in turn stay inside the M-4 band (D-282).

**PR-28 and PR-29: The arc.** The scenes, the set choices, the portraits, the personal tasks, and the cast text of region one, in two batches (D-56, D-57, D-282, D-350). The story follows `docs/world/arc.md`. The PRs propose each personal task and one or two more set choices for approval (D-352, D-355).

**PR-30: Balance pass.** Tune the numbers of D-35, D-60, D-382, and D-388 on the M-4 band and the night runs. Every change reports the number before and after (G-14).

**M-5: Region one play time.** The owner's play time from the first hub to the end of the arc, against the six to eight hours of D-56.

> *In plain English for Phase 4:* the free prologue takes shape. Four dungeons, two hubs, their lessons, the first part of the story, and the numbers tuned by robots and by play.

### Phase 5: First release, the free prologue (gate: a tagged build on GitHub that a fresh machine runs, then the Steam demo on the Deck)

**PR-31: Release workflow.** Export the Game project for the three platforms on a tag and publish a GitHub Release (D-53, D-85). The runbook explains the macOS warning on an unsigned build.

**PR-32: Retired.** The fallback pass of v1 has no purpose after D-98. No later item takes the id (G-10).

**PR-33: The title screen, settings, and the exit.** The first screen, the settings with the CRT toggle and the bindings, and a clean exit that saves.

**PR-39: Deck verification pass.** Walk the Steam Deck verification checklist: gamepad glyphs, default bindings, the 1x frame (D-228), text size, and suspend and resume (D-85, D-92).

**PR-40: Steam integration.** Steamworks initialization, and Steam Cloud for the save directory with the newest-wins prompt (D-85, D-93). The store page of the full game in the "Coming Soon" state, and the prologue as its demo app (D-143). Needs the Steam Direct fee for the full game. PR-40 verifies whether the demo needs a fee of its own.

> *In plain English for Phase 5:* the prologue becomes something a person downloads and runs. Then it becomes a free demo they find on Steam and play on the Deck.

### Phase 6: Region two and later

Parked until Gate 5. Each later region repeats Phase 4 with its own roadmap.

## 8. Sequence (strict order, single owner)

1. Owner: create no label, install no tool. gitar and the label exist (D-66, D-67).
2. The full-plan docs PR: the world, the phase roadmaps, and the area roadmaps (D-142, D-144, D-146). Then the rename to the-thing-below, and the move to the external SSD (D-215 to D-217). The owner runs the Deck test of D-160 before PR-1.
3. PR-1, PR-2, PR-3.
4. Owner: require the checks on `main` (OQ-3).
5. PR-4, PR-5, PR-6, PR-34.
6. M-1, M-2.
7. **← GATE 1 (foundation).** The identity job, `dotnet test`, the smoke job, and `ste-check` are green on three platforms.
8. Owner: pick the font (D-122).
9. PR-7, PR-41, PR-8, PR-9, PR-10.
10. PR-11, PR-12, PR-13, PR-14, PR-36.
11. PR-15. One night runs, then the `night-gate` job joins the PR gate.
12. PR-16, PR-35, PR-37, PR-38.
13. PR-17.
14. M-3, M-4, M-6.
15. **← GATE 2 (first playable).** The owner plays one hub and one dungeon on the desktop and on the Deck and signs off on feel.
16. PR-18, PR-19, PR-20, PR-21.
17. **← GATE 3 (story systems).** The owner plays a branch and a hub that changes with an earlier choice.
18. PR-23 to PR-26, PR-27, PR-42.
19. PR-28, PR-29, PR-30.
20. M-5.
21. **← GATE 4 (region one).** The owner plays region one end to end on both machines.
22. PR-31, PR-33, PR-39.
23. Owner: pay the Steam Direct fee (D-85).
24. PR-40.
25. **← GATE 5 (first release).** A fresh machine runs the tagged build, and the Deck runs the Steam demo.
26. Phase 6 stays parked.

## 9. Open questions

The open questions register is `docs/questions.md` (D-19). It holds OQ-1 onward with options, recommendations, what each blocks, and the date and decision that resolve each one. File a new question there, not here. Ids never change.
