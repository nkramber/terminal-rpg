# Decisions

Status: active register. Owner: Nate. Started 2026-09-12. Written in ASD-STE100.

This file records each owner decision. Each decision has an id (D-#). The numbers never change. A reversed decision stays in this file with a dated note in the "Effect" column. These decisions are the source of the design doc (`docs/design.md`).

How to read this file:

- The "Decision" column gives the answer.
- The "Effect" column gives what the decision changes, binds, or supersedes.
- A date in the "Effect" column marks a later revision.
- The owner answered D-1 to D-24 in the first interview on 2026-09-12. The interview asked each question with options, pros and cons, and a recommended option.
- Three answers, D-5, D-6, and D-7, came as "recommend what is best for this project", and the session chose. The "Decision" column names that.

## Repository and language

| Id | Date | Topic | Decision | Effect |
|---|---|---|---|---|
| D-1 | 2026-09-12 | Implementation language | Rust, with ratatui and crossterm for the terminal front end. The session recommended Go, and the owner chose Rust. | Every tool in the repository is Rust too. Rust is not installed on the dev machine (OQ-2). |
| D-2 | 2026-09-12 | Platforms and CI | macOS, Linux, and Windows terminals at launch. CI runs on hosted GitHub runners for all three. No self-hosted runner. | Three legs per PR. Windows console color and Unicode set the UI floor. |
| D-3 | 2026-09-12 | Build entry | One Makefile with `verify`, `where`, `hooks`, `test`, `lint`, `ste-check`, and `run`. | PR-1 creates it. CLAUDE.md names the raw cargo commands too. |
| D-4 | 2026-09-12 | Repository visibility | The repository stays public. Branch protection on `main` requires the checks. | No personal information in any file, issue, or PR. The `review-gate` check blocks a merge once it exists (OQ-3). |
| D-5 | 2026-09-12 | Tenets | The six what-you-carry tenets verbatim, plus T-7, deterministic simulation. Conflict order: T-5, T-2, T-3, T-4, T-7, T-1. T-6 is absolute. The owner asked for the best choice, and the session chose T-7, because a replay of any seed makes every combat bug reproducible. | T-7 sits above T-1, so a float convenience never beats determinism. |
| D-6 | 2026-09-12 | Determinism guardrails | All five: integer math only in `core`, one seeded random stream per subsystem, a run record with replay, no clock or OS random in `core`, and a cross-platform state hash job in CI. The owner asked for the best choice, and the session chose all five, because a turn-based game needs no float and the cost is low. | G-2 to G-5. Percentages use fixed-point integers. PR-4 creates the lint and the `replay-identity` job. |
| D-7 | 2026-09-12 | Content format and strings | Content files are RON, read by serde with unknown fields refused and an absent field as an error. A test loads every content file. Every player-visible string lives in an id-keyed string table, and a lint refuses an inline player string. The owner asked for the best choice, and the session chose RON, because Rust enums map to it directly and it permits comments for balance notes. | G-6, G-7. A JSON export can come later if an external tool needs one. |
| D-8 | 2026-09-12 | Git rules | Trunk is `main`. Every change starts on a short branch named `<prefix>/pr-<n>-<slug>`. The owner squash-merges. Commit subjects use `feat`, `fix`, `docs`, `test`, or `chore`. A pre-commit hook refuses a commit on `main` and a document that fails the STE check. | G-8, G-15. PR-1 adds the hook and `make hooks`. |

## Language and documents

| Id | Date | Topic | Decision | Effect |
|---|---|---|---|---|
| D-9 | 2026-09-12 | Name | The working title `terminal-rpg` stands until a decision. | The crate, the binary, and the repository use it. A rename is one PR (OQ-7). |
| D-10 | 2026-09-12 | Writing standard | ASD-STE100 for every document, skill, and agent file, checked in CI on every PR. Dated records are exempt. The interim checker is the Python script from decktome at `docs/tools/ste-check.py`. PR-2 ports it to Rust and retires the script. | G-12. The one Python exception to D-1, until PR-2. |
| D-11 | 2026-09-12 | Game text voice | The text the player reads has its own voice. STE does not bind it. A `game-text-style` skill records the voice after the owner sets the tone in the roadmap interview. | The string table (D-7) is the place the voice rules apply. |
| D-12 | 2026-09-12 | Terminology | One term per concept. The glossary lives in the `ste-writing` skill. The roadmap interview fills the first entries. | The Rust checker can flag a refused synonym later. |
| D-13 | 2026-09-12 | Id scheme | D-# decisions, OQ-# open questions, F-# findings, G-# guardrails, L-# lessons, T-# tenets, PR-# code changes, M-# measurements. A number never changes and is never reused. | G-10. A PR-# roadmap id and a GitHub PR number differ. |

## Review and process

| Id | Date | Topic | Decision | Effect |
|---|---|---|---|---|
| D-14 | 2026-09-12 | Automated review pass | gitar comments on every PR after a push, before the Codex review. The author answers every comment. When gitar reports a pause, the comment `Gitar review` runs the pass on demand. | The owner installs the gitar app on this repository (OQ-1). Until then the pass does not run. |
| D-15 | 2026-09-12 | Review gate check | A `review-gate` CI check reads `docs/reviews/pr-<number>.md` and verifies the verdict and the effective head. It is a Rust tool in its own early PR, PR-3, and the workflow runs on `pull_request_target` with the head as data only. | Enforced from the start under D-4, once the check exists and the owner requires it (OQ-3). |
| D-16 | 2026-09-12 | Documentation PR override | A PR that changes only documentation merges without a Codex review when the owner adds the `review-override` label. The eligible set that this session applied is `docs/`, `CLAUDE.md`, `AGENTS.md`, `.claude/`, and `.github/pull_request_template.md` (OQ-4 asks the owner to confirm the set). | Narrows T-4 for documentation only. A workflow, a Makefile, or a schema always needs the review. |
| D-17 | 2026-09-12 | Review skill and record | The what-you-carry `pr-review` skill, adapted to Rust and this project: the provider gate, one review file per PR with a machine-read head and verdict, a response file, and P0 to P3 severity. | `.claude/skills/pr-review/SKILL.md`. Exempt from D-22. |
| D-18 | 2026-09-12 | Session model | One harness invocation is one code PR plus one handoff entry. A documentation PR can follow the merge of that code PR in the same session, with its own entry. The handoff keeps the 10 newest entries with six parts. Older entries move to `docs/session-handoff-archive.md`. The author field reads `Claude Code` or `Codex`. | Every session ends with a push and a check of the remote. |
| D-19 | 2026-09-12 | Open questions | Strict: every open question stops the session. A session files the question in `docs/questions.md` with options and a recommendation, and it picks no default. The session recommended a split rule, and the owner chose strict. | G-9. Drain the questions file before each session. |
| D-20 | 2026-09-12 | Document layout | `docs/design.md` holds the tenets, the guardrails, the finding register, and the high-level roadmap. Focused roadmaps live in `docs/roadmaps/`. `docs/decisions.md`, `docs/questions.md`, `docs/session-handoff.md` with its archive, `docs/reviews/`, and `docs/runbooks/` complete the set. File names in `docs/` are lowercase. `CLAUDE.md` and `AGENTS.md` are identical. | The read order in `CLAUDE.md`. |
| D-21 | 2026-09-12 | Skills and agents on day one | Skills: `ste-writing`, `design-doc-style`, `pr-review`, and `rust-conventions`. Agents: `design-critic` now, and `playtest-bot` once a headless runner exists. | All under `.claude/`. The `playtest-bot` file states that it waits on the runner PR. |
| D-22 | 2026-09-12 | Attribution | No agent, harness, or model is named as the source of work in code, game text, commits, PR descriptions, or GitHub comments. Two exemptions: the author field in the session handoff, and the files in `docs/reviews/`. `.claude/settings.json` sets the commit and PR attribution to empty strings. | Absolute, T-6. The harness reminder asks for a trailer in every session, and this rule wins. |
| D-23 | 2026-09-12 | Write scope | This repository takes writes. `/Users/nate/Repos/decktome` and `/Volumes/SSD-1TB/what-you-carry` are read-only references. No other source. | Binds every session. |
| D-24 | 2026-09-12 | Question format | Ask questions the moment they arise, in small batches, with `AskUserQuestion`. Each question gives its options, the pros and cons of each, and one recommended option marked as such. | Owner instruction, 2026-09-12. Binds every interview. |
| D-25 | 2026-09-12 | Root commit | The repository had no commit at the start of the session. The owner made the root commit on `main` at 14:40 local time, `6b899dd`, with an empty `CLAUDE.md`. Every later change follows D-8. | No session ever commits on `main`. The session put every file on the branch `docs/foundation`. |

## Game design

The roadmap interview started on 2026-09-12. Each answer is one row.

| Id | Date | Topic | Decision | Effect |
|---|---|---|---|---|
| D-26 | 2026-09-12 | Push policy (OQ-5) | The foundation documents and the design wait for the end of the roadmap interview, then one PR. After that first PR, a session pushes its branch and opens its PR. | Resolves OQ-5. The first PR is large by design. |
| D-27 | 2026-09-12 | Setting and tone | Dark fantasy. Grim and lethal. | Game text voice (D-11) follows this. Death and loss are part of the design. |
| D-28 | 2026-09-12 | Game structure | Hub settlements, plural, plus branching hand-authored dungeons and a main story. A hub is not always a town: a castle town, a cave community, a boat, an airship. Imagination is key. | Content ships one region at a time. Each hub has its own shape and services. |
| D-29 | 2026-09-12 | Combat model | Turn-based with a visible turn order. Speed decides the order, and haste, slow, and heavy actions shift it. | The timeline is a tactical decision space and a UI element. Fully deterministic (T-7). |
| D-30 | 2026-09-12 | Scope and length | 20 to 40 hours for a full play. The game ships in slices, and the first slice is one region. | The roadmap has region-level gates. The first playable proves the loop in one region. |
| D-31 | 2026-09-12 | Party size | Three characters in battle. The session recommended four, and the owner chose three. | Faster turns and a tighter UI. One death hurts more, which fits D-27. |
| D-32 | 2026-09-12 | Job model | FF5 style. A character changes jobs freely at a hub. Job levels earn abilities that the character keeps. A character equips one secondary ability set from another job. | The deepest content surface of the game. Balance across combinations is the hardest tuning problem. |
| D-33 | 2026-09-12 | Party members | A fixed cast of story characters. The session recommended a created leader plus recruits, and the owner chose the fixed cast. | The strongest story and the most text. The cast is fixed content. Jobs, not characters, carry the build decision. |
| D-34 | 2026-09-12 | Levels | A character level for stats, from experience. A job level per job for abilities, from ability points. A character keeps every learned ability across job changes. | Two progress bars. A rule for a low-level job on a high-level character is an open question. |
| D-35 | 2026-09-12 | Sources of challenge | Two: enemies with real tactics (focus fire, buffs, interrupts, formations), and scarce resources across a dungeon (limited healing, no free rest). Not chosen: lethal numbers alone, and puzzle bosses as a requirement. | Enemy AI is a large system with its own tests. The retreat decision is real. |
| D-36 | 2026-09-12 | Death and saves | A fallen character stays down until a hub or a rare item revives them. A party wipe reloads the last save point. | A death costs the rest of the dungeon. Save points are content. A short-handed party needs balance. |
| D-37 | 2026-09-12 | Encounters | Visible enemies on the map. Some are fixed, some patrol. No random encounters. | The map needs enemy movement and sight. Avoidance and ambush are decisions. |
| D-38 | 2026-09-12 | Map view | A top-down tile map drawn with glyphs. The party moves tile by tile. A side panel shows status. | Every dungeon and hub needs a tile layout. Glyph readability sets the terminal size floor. |
| D-39 | 2026-09-12 | Dungeon authorship | Hand-authored layouts in content files, with seeded variation in enemies, loot, and some rooms. | A text format for layouts. Each dungeon is a content PR. Revised in part by D-47 on 2026-09-12: the seeded variation is gone, and the hand-authored layout stands. |
| D-40 | 2026-09-12 | Decisions | All four kinds. Story branches with permanent consequences. Tactical decisions in dungeons. Moral choices with a reputation or faction system. Dialogue choices with character relationships. | Four systems: branch flags, resource tension, a reputation model with hub reactions, and a relationship model per character. The text volume is the largest cost of the game. |
| D-41 | 2026-09-12 | Dungeon parts | All four kinds. Treasure, locked doors and keys, and save points. Traps and hazards. Environmental puzzles: switches, pushable blocks, light and dark. Optional secrets: hidden rooms, secret bosses, lore. | A hazard system, a puzzle mechanic set, and a secret marker in the layout format. |
| D-42 | 2026-09-12 | Magic cost | MP per character. Recovery at hubs, at save points, and by scarce items. | Every cast is a budget decision (D-35). A caster with empty MP needs a no-MP fallback in the job design. |
| D-43 | 2026-09-12 | Elements and status | Six to eight elements with weakness, resist, and absorb. A curated status list of about ten. | Every enemy and item has an affinity row. Each status has its rule in the simulation. The exact lists are open questions. |
| D-44 | 2026-09-12 | Equipment | Six slots: weapon, shield or off-hand, head, body, and two accessories. Job restrictions apply. | Restriction tables are content. A job change can leave a slot empty, and the UI must show it. |
| D-45 | 2026-09-12 | Loot | Fixed hand-authored items with a few rarity tiers. No random affixes. No crafting. Consumables were not chosen. | The loot table is finite. The economy is tunable by hand. |
| D-46 | 2026-09-12 | Replayability | Replayability is not a concern for any part of the game. | Owner statement with D-45. Conflicts with the seeded variation of D-39, see OQ-8. Determinism (T-7) stays, because it serves bug reproduction, not replay. |
| D-47 | 2026-09-12 | Dungeon variation (OQ-8) | No seeded variation. Every enemy, chest, and room is placed by hand. The seed drives combat rolls alone. | Resolves the conflict between D-39 and D-46. Revises D-39 in part. The playtest bot varies its inputs, not the layout. |
| D-48 | 2026-09-12 | Terminal size | 120 columns by 40 rows is the floor. Below it the game shows a clear message and no broken screen. The session recommended 80 by 24, and the owner chose 120 by 40. | Every screen designs to 120 by 40. A default macOS Terminal window shows the message on first launch, and the runbook tells the player to resize. |
| D-49 | 2026-09-12 | Color and glyphs | A 256-color palette with a 16-color fallback. Unicode box drawing and a few glyphs with an ASCII fallback. | Two glyph sets and two palettes in content. A test per screen for each. |
| D-50 | 2026-09-12 | Input | Arrow keys and vi keys both. Enter and Escape for menus. Letter hotkeys in battle. No mouse. | The input record holds key presses alone (T-7). Diagonal moves use vi keys. |
| D-51 | 2026-09-12 | First playable | One hub and one dungeon, with job change and a shop. The session recommended a battle arena alone, and the owner chose the full small loop. | Phase 2 holds the map, the tile format, patrols, battle, the hub screens, and the job screen. It is the largest phase before content. |
| D-52 | 2026-09-12 | Phase gates | A written exit test per phase, and the owner plays the build and signs off on feel. | Each phase gate has a sign-off note in the roadmap with the date. |
| D-53 | 2026-09-12 | Distribution | GitHub Releases with a binary per platform, built by CI on a tag. | A release workflow. The runbook explains the macOS Gatekeeper warning on an unsigned binary. |
| D-54 | 2026-09-12 | License | Public repository, all rights reserved. A `LICENSE` file grants nothing. The session offered a private repository on GitHub Pro, and the owner chose public with no grant. | D-4 stands. Anyone can read the code, and a copy is a copyright violation. |
| D-55 | 2026-09-12 | Jobs at launch | Four jobs at the first playable, eight at the first release. The session proposes the names, and the owner approves. The session recommended six and twelve, and the owner chose four and eight. | Each job is a content PR with abilities, gear rules, and text. |
| D-56 | 2026-09-12 | Region one | Two hubs, four dungeons, one story arc, six to eight hours of play. | About eight content PRs after the systems exist. Region one is the first release (D-30). |
| D-57 | 2026-09-12 | Story text | Sessions draft the dialogue, the lore, and the item text under the `game-text-style` skill. The owner approves each batch. | The skill needs the voice rules (D-11, D-27). A wrong tone costs a rewrite PR. |
| D-58 | 2026-09-12 | Cast size | Five characters by the end of region one. Three fight, and two wait in reserve. The party swaps at hubs and at save points. | A downed character (D-36) has a replacement. The reserve needs an experience rule (OQ-9). |
| D-59 | 2026-09-12 | Hub services | All four: rest to full, save, change jobs, and swap the party. A shop that buys and sells. Story scenes, dialogue, and decisions. Side quests and a rumor board. | A quest state system joins the branch flags of D-40. Every hub has a shape of its own (D-28), so not every hub offers every service. |
| D-60 | 2026-09-12 | Economy | Gold from enemies and treasure both. Gold buys gear, items, and rest. The session recommended treasure alone, and the owner chose both. | Every fight pays. The retreat decision (D-35) trades gold for safety. |
| D-61 | 2026-09-12 | Difficulty | One difficulty, tuned by play. No options and no assists. | One tuning target. The playtest sign-off (D-52) is the dial. |
| D-62 | 2026-09-12 | Save files | One slot and one autosave, in the platform config directory. A save holds the run record, so it replays (T-7). The session recommended three slots, and the owner chose one. | The record grows with play, so the format needs a compaction rule. |
| D-63 | 2026-09-12 | Prose voice | Terse and concrete. Short sentences, physical detail, no purple prose, dry understatement. | The `game-text-style` skill records it. OQ-15 asks the owner to approve that skill. |
| D-64 | 2026-09-12 | Bot runner | The headless runner lands right after the battle system, with a random policy and a greedy policy. A few hundred runs per PR, and ten thousand each night. | A nightly workflow and a night gate, as in what-you-carry. The `playtest-bot` agent reads the runner. |
| D-65 | 2026-09-12 | Enemy AI | Three layers. A tactical evaluator in `core` scores every legal action by its simulated outcome: damage, kills, threat, healing, and timeline shift. A personality profile per enemy in content reweights those terms and adds traits. Bosses add scripted phases and signature moves. | The evaluator is the largest single system in `core`. The profile format needs a validator, so a bad profile fails loudly (T-2). Deterministic under T-7. |
