# PR-3 review

Date: 2026-09-14

## Identity

- PR: 3
- Target: `main`
- Base: `7375310828b435fd6d2819accf3e52e6158a3d3c`
- Merge base: `7375310828b435fd6d2819accf3e52e6158a3d3c`
- Head: `f684ed5090966905b78eee39c087f6e86ba4f2e3`
- Branch: `docs/pr-3-sprite-sample`

## Provider gate

The handoff identifies the PR author as Claude Code. The active reviewer is Codex. The providers differ, so the gate passes under T-4 and D-17.

## Intended behavior and scope

The PR saves the approved 32 by 32 cast sprites as a dated sample, records the related decisions, removes the obsolete 16 by 16 content, and marks the interim atlas script as out of date. The review inspected the complete effective diff, the design roadmap, the decision and question registers, the cast file, the project guidance, the atlas script, both sample sheets, all five grids, and the automated pass.

The review covers sample structure, palette and grid validity, deleted-content references, decision effects, guidance-file identity, failure behavior of the retained script, STE text, and the required PR gate evidence. No code or existing build check applies to this PR.

## Findings

No finding.

## Out of scope

- The C# atlas command, the 32 by 32 content import, and the pixel test belong to PR-34, as the design roadmap states.
- The `review-gate` check belongs to roadmap PR-3. It does not exist on this PR yet.
- Branch protection remains an owner action after PR-3 merges, as OQ-3 states.

## PR comments

- The owner requested three on-demand automated passes with `Gitar review`. The final pass approved `f684ed5` with zero issues. The earlier pass approvals and the final approval match the three pushed revisions.
- The progress comments from the automated reviewer contain no claim to verify. No automated finding remains unanswered.

## Description edits

None.

## Verification

- `git merge-base origin/main HEAD`: passed. The merge base is `7375310828b435fd6d2819accf3e52e6158a3d3c`.
- `git diff --check origin/main...HEAD`: passed with no output.
- `cmp -s AGENTS.md CLAUDE.md`: passed. The files are identical.
- `python3 docs/tools/ste-check.py $(git ls-files '*.md' | grep -v -e '^docs/reviews/' -e '^docs/session-handoff' -e '^docs/archive/')`: passed with 0 findings.
- Palette and grid probe: passed. The palette has 48 unique keys, and all five 32 by 32 grids have 32 rows of 32 characters with no unknown key.
- `python3 docs/tools/make-atlas.py`: exited 1 with `make-atlas: no .grid file under .../content/sprites`, as D-406 documents after D-405.
- Visual inspection of `cast-front.png` and `redraw-compare.png`: passed. The sheets show the five named cast members, the stated front views, and the 1x and 6x presentations.
- `gh pr view 3 --json ...`: passed. It verified the target, base, tip, changed paths, three commits, and the final automated approval comment. The reported status-check list is empty because this repository has no existing CI checks before PR-1.
- `gh pr checks 3`: not completed because the GitHub API connection failed during the final read. The successful PR read reported no checks, so no existing required check was skipped.
- Build, test, format, smoke, det-lint, replay-identity, night-gate, and review-gate checks: not run because the repository has no code yet, and the project instructions assign these checks to PR-1, PR-4, PR-15, or roadmap PR-3.
- `git status --short --branch`: passed before review edits. The checkout had no unrelated changes.
- Push: `429ff2f40d83963e388994dc11c9e53216e49877` is the review record and handoff commit on `origin/docs/pr-3-sprite-sample`, verified with `git push`.

## Open questions and accepted risks

OQ-3 remains open for branch protection after PR-3 merges. No accepted risk blocks this PR.

## Verdict

**Ready for owner merge.** This verdict applies to head `f684ed5090966905b78eee39c087f6e86ba4f2e3`. The complete scope is consistent, the focused checks pass, and the automated pass found no issue.
