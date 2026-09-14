# PR-2 review

Date: 2026-09-14

## Identity

- PR: 2
- Target: `main`
- Base: `9dd80da`
- Merge base: `9dd80da`
- Head: `6586c7c`
- Branch: `docs/pr-2-world-building`

## Provider gate

The handoff identifies the PR author as Claude Code. The active reviewer is Codex. The providers differ, so the gate passes under T-4 and D-17.

## Intended behavior and scope

The PR records the plan through the systems block, the world files, the decision and question registers, and the project guidance that follows the new decisions. The repeat review inspected the new effective diff at `6586c7c`, the response file, the complete original scope, the decision effects, the design roadmap, the PR description, and the refreshed automated pass.

The review covers document consistency, roadmap exit tests, decision revisions, provider and attribution rules, and the interim STE check. No code, content asset, or executable build exists in this PR.

## Findings

### P1-1: The PR-9 exit test contradicts the persistent status rule

Status: fixed in `6586c7c`.

File: `docs/design.md:283`.

Trigger: Read the PR-9 gate with D-390, then implement a battle that ends with Poison, Blind, or Silence active.

Expected: PR-9 must test that transient statuses end while Poison, Blind, and Silence persist past battle, as D-390 requires. The persistent effects then need their map and menu behavior from D-392 and D-393.

Actual: The PR-9 gate requires property tests to assert that “every status ends,” while D-390 requires three statuses to last past battle.

Consequence: A future PR-9 implementation cannot pass its stated gate and obey the approved status contract at the same time. The roadmap can force either a false test or an implementation that removes the persistence rule.

Correction: Replace the blanket assertion with separate assertions for transient status expiry and persistence of Poison, Blind, and Silence. Keep the map and menu checks in PR-16, where the roadmap already places them.

Regression check: Run the interim STE check and review the PR-9 gate against D-390, D-392, and D-393. The gate must name both expiry classes and must not require every status to end.

### P3-1: The effective diff contains trailing whitespace

Status: fixed in `6586c7c`.

File: `docs/design.md:50`, `docs/design.md:228`, `docs/design.md:261`.

Trigger: Run `git diff --check main...4b3d04e`.

Expected: The documentation diff has no trailing whitespace.

Actual: The command reports trailing whitespace on three added lines.

Consequence: The documentation diff fails the repository's normal whitespace check and creates avoidable noise in later patches.

Correction: Remove the trailing spaces from the three added lines.

Regression check: Run `git diff --check main...4b3d04e` after the correction.

## Out of scope

- The C# STE checker belongs to PR-2, which creates the tool after this plan PR.
- The review-gate command and workflow belong to PR-3, which creates that check.
- The audio, release, and focused roadmap blocks belong to the follow-up docs PRs named by D-399.
- The Deck test belongs before PR-1, as D-160 and the handoff state.

## PR comments

- The first automated pass approved the original effective head with no issue. The repeat pass approved `6586c7c` with no issue after the owner posted `Gitar review`.
- The automated reviewer reported that automatic reviews were paused for the period. The owner used the documented on-demand comment for both passes, and no automated comment remains unanswered.

## Description edits

None.

## Verification

- `git diff --check origin/main`: passed with no output after the correction.
- `cmp -s AGENTS.md CLAUDE.md`: passed. The files are identical.
- `python3 docs/tools/ste-check.py $(git ls-files '*.md' | grep -v -e '^docs/reviews/' -e '^docs/session-handoff' -e '^docs/archive/')`: passed with 0 findings.
- `grep -n "every status ends" docs/design.md`: passed. It returned no line.
- `rg -n "Every status but poison, blind, and silence" docs/design.md`: passed. It found the corrected PR-9 gate at line 283.
- `gh pr view 2 --json ...`: passed. It verified base `9dd80da`, tip `6586c7c`, no formal review records, and the refreshed automated approval comment.
- `gh pr checks 2`: no checks reported. CI and the review gate do not exist until later PRs, so no existing required check was skipped.
- `git status --short --branch`: passed before review edits. The checkout was on `docs/pr-2-world-building` with no unrelated changes.
- Push: pending. The repeat review record and handoff entry must be committed and pushed together.

## Open questions and accepted risks

OQ-3 remains open for PR-3. No accepted risk changes the finding above.

## Earlier verdicts

- `Changes required` at `4b3d04e`. P1-1 and P3-1 were open.

## Verdict

**Ready for owner merge.** This verdict applies to head `6586c7c`. The earlier findings are fixed, the focused checks pass, and the refreshed automated pass found no new issue.
