# PR-2 review

Date: 2026-09-14

## Identity

- PR: 2
- Target: `main`
- Base: `9dd80da`
- Merge base: `9dd80da`
- Head: `4b3d04e`
- Branch: `docs/pr-2-world-building`

## Provider gate

The handoff identifies the PR author as Claude Code. The active reviewer is Codex. The providers differ, so the gate passes under T-4 and D-17.

## Intended behavior and scope

The PR records the plan through the systems block, the world files, the decision and question registers, and the project guidance that follows the new decisions. The review inspected the complete diff from `9dd80da` to `4b3d04e`, the later metadata tip `f748ee3`, the design roadmap, the decision effects, the questions register, the world files, the runbook, the changed skills, the PR description, and the automated pass.

The review covers document consistency, roadmap exit tests, decision revisions, provider and attribution rules, and the interim STE check. No code, content asset, or executable build exists in this PR.

## Findings

### P1-1: The PR-9 exit test contradicts the persistent status rule

Status: open.

File: `docs/design.md:283`.

Trigger: Read the PR-9 gate with D-390, then implement a battle that ends with Poison, Blind, or Silence active.

Expected: PR-9 must test that transient statuses end while Poison, Blind, and Silence persist past battle, as D-390 requires. The persistent effects then need their map and menu behavior from D-392 and D-393.

Actual: The PR-9 gate requires property tests to assert that “every status ends,” while D-390 requires three statuses to last past battle.

Consequence: A future PR-9 implementation cannot pass its stated gate and obey the approved status contract at the same time. The roadmap can force either a false test or an implementation that removes the persistence rule.

Correction: Replace the blanket assertion with separate assertions for transient status expiry and persistence of Poison, Blind, and Silence. Keep the map and menu checks in PR-16, where the roadmap already places them.

Regression check: Run the interim STE check and review the PR-9 gate against D-390, D-392, and D-393. The gate must name both expiry classes and must not require every status to end.

### P3-1: The effective diff contains trailing whitespace

Status: open.

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

- The owner posted `Gitar review`; the automated reviewer ran on demand and reported approval with no issues. The review verified the comment sequence and found no unanswered automated comment.
- The automated reviewer reported that automatic reviews were paused for the period. The owner used the documented on-demand comment, and the resulting pass approved the PR tip `f748ee3`.

## Description edits

None.

## Verification

- `git diff --check main...4b3d04e`: failed because it reported trailing whitespace at `docs/design.md:50`, `docs/design.md:228`, and `docs/design.md:261`.
- `cmp -s AGENTS.md CLAUDE.md`: passed. The files are identical.
- `python3 docs/tools/ste-check.py $(git ls-files '*.md' | grep -v -e '^docs/reviews/' -e '^docs/session-handoff' -e '^docs/archive/')`: passed with 0 findings.
- `gh pr view 2 --json ...`: passed. It verified base `9dd80da`, tip `f748ee3`, effective head `4b3d04e` from the PR description, no review records, and the automated approval comment.
- `gh pr checks 2`: no checks reported. CI and the review gate do not exist until later PRs, so no existing required check was skipped.
- `git status --short --branch`: passed before review edits. The checkout was on `docs/pr-2-world-building` with no unrelated changes.
- Push: `af7861b` is the head of `origin/docs/pr-2-world-building`, verified with `gh pr view`.

## Open questions and accepted risks

OQ-3 remains open for PR-3. No accepted risk changes the finding above.

## Verdict

**Changes required.** This verdict applies to head `4b3d04e`. The PR-9 exit test conflicts with the approved persistent-status rule, and the effective diff has three trailing-whitespace errors.
