# PR-4 review

Date: 2026-09-14

## Identity

- PR: 4
- Target: `main`
- Base: `d29921d92c66f6dd03432b526b07cdafa382f902`
- Merge base: `d29921d92c66f6dd03432b526b07cdafa382f902`
- Head: `cb6e96e`
- Branch: `docs/pr-4-docs-audit`

## Provider gate

The handoff identifies Claude Code as the author of the substantive PR commit. Codex is the reviewer. The providers differ, so the gate passes under T-4 and D-17.

## Intended behavior and scope

The PR updates the design, decision and question registers, world files, agent guidance, skills, runbooks, and configuration before the repository rename. The review inspected the complete diff, every changed file in context, the applicable design roadmap, the decision and question registers, existing review records, the PR description and comments, and the file references outside the diff.

The review covers document consistency, decision traceability, process instructions, external-fact sourcing, agent guidance, STE compliance, and the effect of removing the Rust ignore block. No code, build solution, workflow, or roadmap file exists in this checkout.

## Findings

### P2-1: The design-doc skill contradicts the design sections

Status: open.

File: `.claude/skills/design-doc-style/SKILL.md:14-17`.

Trigger: A session follows the changed design-doc template when it edits `docs/design.md` or a focused roadmap.

Expected: The design-doc skill describes the section order that its users must follow. The audit must leave the skill and the current design structure consistent (T-1, T-5, D-20).

Actual: The changed skill says the defect register is section 6, guardrails are section 7, and the roadmap is section 8. The current design doc uses section 5 for the defect register, section 6 for guardrails, and section 7 for the roadmap. The focused-roadmap list also says section 6 is the guardrails section, which conflicts with its own numbered template.

Consequence: A session can write a roadmap with the wrong headings or look for the design roadmap in the wrong section. The skill no longer gives one usable document structure.

Correction: Make the skill's numbered template match `docs/design.md`, or update the design doc and all navigation instructions together. Keep the focused-roadmap section list consistent with the chosen template.

Regression check: Compare the skill's numbered template and focused-roadmap list with the headings in `docs/design.md`. Run `cmp -s AGENTS.md CLAUDE.md`. The sections and the byte-identity check must agree.

### P2-2: The name-search record lacks primary sources

Status: open.

File: `docs/design.md:23-27`, `docs/decisions.md:520`, and `docs/runbooks/rename-and-move.md:21`.

Trigger: A later session must verify the decision to proceed with `The Thing Below` or understand why the name remains tentative.

Expected: Every material external fact has a dated source, and a runbook records enough information to repeat a risk-sensitive check (the `design-doc-style` skill, D-408, D-215).

Actual: The new design entry says that the search found no conflict, and the decision says that Steam and United States searches found no matching game or mark. The files name no Steam search URL, USPTO search URL, query, or result date. They only state that the EU and WIPO searches did not answer. The PR description contains search details, but the repository documents do not preserve those sources.

Consequence: The rename decision cannot be independently reproduced from the repository. A later reader cannot distinguish an exact-title search from a broad text search, or identify the records that the unresolved register check must revisit.

Correction: Add dated primary-source links and the exact search terms or result references to the design and rename records. Keep the unresolved EUIPO and WIPO follow-up explicit until PR-40 verifies it.

Regression check: Review the changed external-fact entries and confirm that each claim has a dated primary source and repeatable query or result reference. Run the STE checker after the correction.

## Out of scope

- The missing build, replay-identity, and det-lint checks belong to PR-1 and PR-4, as the roadmap states. No solution exists in this checkout.
- The final EUIPO, TMview, and WIPO trademark verification belongs to PR-40, as `docs/design.md` states.

## PR comments

- The owner posted `Gitar review` twice. The second request produced the automated pass result, which approved the PR with no issue comments.
- The automated pass reported that reviews were paused for the period. The owner used the documented on-demand comment, and the resulting pass approved the head.

## Description edits

None.

## Verification

- `git status --short --branch`: passed before the review; the tree matched `origin/docs/pr-4-docs-audit`.
- `git diff --check origin/main...cb6e96e`: passed with no whitespace errors.
- `cmp -s AGENTS.md CLAUDE.md`: passed.
- `python3 docs/tools/ste-check.py $(git ls-files '*.md' | grep -v -e '^docs/reviews/' -e '^docs/session-handoff' -e '^docs/archive/')`: passed with 0 findings at `cb6e96e`.
- `gh pr view 4`: passed. It confirmed base `d29921d`, head `cb6e96e`, branch `docs/pr-4-docs-audit`, the single substantive commit, and the existing comments.
- `gh pr checks 4`: passed for the available Gitar check. No repository CI, review-gate, or other build checks exist yet.
- `make verify`: not run because PR-1 has not created a Makefile or solution.
- `dotnet build`, `dotnet test`, and `dotnet format`: not run because PR-1 has not created the solution.
- Godot build and smoke session: not run because PR-1 has not created the Game project.
- Push: `cb6e96e` is the head of `origin/docs/pr-4-docs-audit`, verified with `gh pr view`.

## Open questions and accepted risks

- OQ-3 remains open for branch protection. It does not block this docs review because the required checks do not exist until later PRs.
- The EUIPO, TMview, and WIPO searches remain unresolved under D-408 and are accepted only as a later PR-40 check, not as evidence for the current name decision.

## Verdict

**Changes required.** The provider gate passes, but the audit leaves a contradictory design-doc skill and an unsourced material name-search record. The required document corrections and their focused checks remain outstanding.
