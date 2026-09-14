# PR-2 response

Date: 2026-09-14

This file answers the review in `docs/reviews/pr-2.md` at head `4b3d04e` (D-17). The verdict there was `Changes required`, with two findings.

## P1-1: The PR-9 exit test contradicts the persistent status rule

Disposition: full merit.

Evidence: `docs/design.md:283` asserted that "every status ends". D-390 keeps poison, blind, and silence past the end of a battle, until a cure or a rest at a hub. The Effect column of D-390 carries no revision note, so the rule stands, and the gate could not pass under it.

Correction: the PR-9 gate in `docs/design.md` now asserts two classes. Every status but poison, blind, and silence ends with its battle, and those three remain after it (D-390). The map and menu rules of the three stay in PR-16, which already cites D-390, D-392, D-393, and D-397.

Regression check: `grep -n "every status ends" docs/design.md` returns no line, and line 283 names both classes. The interim STE check passes with 0 findings.

## P3-1: The effective diff contains trailing whitespace

Disposition: full merit.

Evidence: `git diff --check origin/main..HEAD -- docs/design.md` reported trailing whitespace at lines 50, 228, and 261 before the correction. The same check on every other file of the diff reported nothing.

Correction: the trailing space is gone from the three lines of `docs/design.md`: the thesis paragraph, the body of PR-4, and the body of PR-7.

Regression check: `git diff --check origin/main` returns exit code 0 with no output on the corrected tree.

## New ids

No new D-#, OQ-#, or F-# id.

## Final head

The corrections, this file, and the handoff entry land in one commit on `docs/pr-2-world-building`. That commit changes `docs/design.md`, so it is the new effective head, and the review needs a repeat pass on it (the `pr-review` skill, "Repeat review procedure").
