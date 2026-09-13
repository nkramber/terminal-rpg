# Rename and move the repository

Status: runbook, planned. Owner: Nate. Written 2026-09-12 (D-215 to D-217). Written in ASD-STE100 (D-10).

This runbook renames the repository from the working title to the tentative name, then moves the checkout to the external SSD. The owner and a session do it once, after the full-plan PR merges and before PR-1 starts (D-216).

## Names

| Item | Before | After |
|---|---|---|
| GitHub repository | `nkramber/terminal-rpg` | `nkramber/the-thing-below` |
| Local checkout | `~/Repos/terminal-rpg` | `/Volumes/SSD-1TB/the-thing-below` |
| Title in documents | terminal-rpg | The Thing Below |
| Solution and projects in commands | `TerminalRpg.*` | `TheThingBelow.*` |

## Before you start

- The full-plan PR is merged, and no other PR is open.
- `git fetch` and `git status --short --branch` show no `[ahead N]` on `main`.
- The Mac shows the external SSD at `/Volumes/SSD-1TB`.
- The name is tentative (D-215). Search the Steam store and the trademark registers for "The Thing Below" first. If a conflict shows, file it in `docs/questions.md` and stop.

## Procedure

1. Rename the GitHub repository: `gh repo rename the-thing-below --repo nkramber/terminal-rpg`.
2. Set the local remote: `git remote set-url origin git@github.com:nkramber/the-thing-below.git`.
3. Run `git fetch`, and confirm that the remote answers.
4. Start a short branch from `main` for the rename PR (D-8).
5. Replace the working title with the new names in `README.md`, the documents, the agent files, and the skills (D-217).
6. Keep the dated records as they are: `docs/reviews/`, the handoff entries, and `docs/archive/`.
7. Run the STE check. Open the rename PR, and answer the automated pass (D-66).
8. The owner merges the rename PR.
9. Clone the repository to the SSD: `git clone git@github.com:nkramber/the-thing-below.git /Volumes/SSD-1TB/the-thing-below`.
10. Copy the local session notes that key on the old checkout path to the key of the new path.
11. Open a session in the new checkout, and run the STE check there.
12. The owner deletes the old checkout, only after the new checkout passes.

## Notes

- Claude Code keeps its local project notes under `~/.claude/projects/`, in a folder named from the checkout path. Step 10 copies the `memory/` folder of the old name to the folder of the new name.
- The dated records keep the old name, because a rewrite of a dated record falsifies it (D-10).
