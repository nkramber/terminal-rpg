# PR-4 response

Date: 2026-09-14

This file answers the review in `docs/reviews/pr-4.md` at head `cb6e96e` (D-17). The verdict there was `Changes required`, with two findings.

## P2-1: The design-doc skill contradicts the design sections

Disposition: full merit.

Evidence: the template in `.claude/skills/design-doc-style/SKILL.md` numbered the status header as item 1, so each section item sat one number above its heading in `docs/design.md`. The register was item 6, the guardrails item 7, and the roadmap item 8, against the headings `## 5.`, `## 6.`, and `## 7.`. The offset was older than this PR. The audit swapped the register and the guardrails into the right order, and it kept the offset.

Correction: the status header is now an unnumbered paragraph above the list, and the list numbers 1 to 9 match the headings of `docs/design.md`. The focused-roadmap sentence now reads "the status header and the same sections 1, 5, 7, 8, and 9". `CLAUDE.md` and `AGENTS.md` cite the guardrails as section 6 and the roadmap as section 7, and D-142 and D-399 cite sections 7 and 8 of the design, so no other text changes.

Regression check: a script compares each numbered item of the skill template with the headings `## N. Title` of `docs/design.md`. All nine numbers and titles match. The focused-roadmap sections resolve to the thesis, the register, the roadmap, the sequence, and the open questions. `cmp -s AGENTS.md CLAUDE.md` returns 0.

## P2-2: The name-search record lacks primary sources

Disposition: full merit.

Evidence: D-408, the dated line of the status header, and the rename runbook stated the result of the search with no URL, query, or date of a check. Only the PR description held details, and the repository does not keep it.

Correction: the session ran each check again on 2026-09-14 and wrote the results into the external facts of `docs/design.md`:

- Steam: the store search API URL, one query for each of four terms, with 0 results, and the store search page, with 50 titles and no match of the phrase.
- itch.io: the game page and the devlog of "The Thing Beneath", with the count of each title, and the search URL.
- USPTO: the endpoint and the POST body, 0 hits for five terms, and two controls: 11 hits for "below deck" and 1,125 for "below". The controls prove that the query reads the word mark.
- EUIPO, TMview, and WIPO: the URLs, and the reason that no script check exists. PR-40 keeps that check (D-408).
- The film of 2004, with its source.

The heading of the list now says that each fact carries the date of its check, because the list holds checks of 2026-09-12 and of 2026-09-14. The Effect column of D-408 and the name search bullet of `docs/runbooks/rename-and-move.md` point to the external facts. The runbook keeps the EU and WIPO check explicit.

Regression check: each new external fact names a URL or an endpoint, its query or its count, and the date of the check. The interim STE check passes with 0 findings.

## New ids

No new D-#, OQ-#, or F-# id.

## Final head

The corrections, this file, and the handoff entry land in one commit on `docs/pr-4-docs-audit`. That commit changes `docs/design.md`, `docs/decisions.md`, the skill, and the runbook, so it is the new effective head, and the review needs a repeat pass on it (the `pr-review` skill, "Repeat review procedure").
