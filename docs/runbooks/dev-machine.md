# Runbook: the development machine

Status: procedure, written 2026-09-12 for the owner's Mac, revised the same day for D-99, and on 2026-09-14 for the new repository name (D-410). Written in ASD-STE100.

Facts checked on 2026-09-12:

- The machine is arm64 on macOS 26.5.
- The .NET 10 SDK is present: `dotnet --version` gives 10.0.400.
- Godot 4.7.2 .NET is present at `/Applications/Godot_mono.app`, because what-you-carry uses it. The name `Godot` is not on the command path.
- `gh` has a login as the owner, and `git` has the `origin` remote for `nkramber/the-thing-below`, checked 2026-09-14 (D-410).
- Python 3.9.6 is present. The interim STE checker needs it until PR-2 (D-10, D-101).
- The repository on GitHub is public (D-4, D-54).

## Install the tools

1. Install the .NET SDK that `global.json` names, once PR-1 creates it. The current machine already has .NET 10.
2. Install Godot 4.7.2 .NET from https://godotengine.org/download/macos/ when the machine lacks it. Put it at `/Applications/Godot_mono.app`.
3. Run `/Applications/Godot_mono.app/Contents/MacOS/Godot --version` and check the version against the design header.

## Prepare a checkout

1. Clone the repository: `git clone git@github.com:nkramber/the-thing-below.git`.
2. After PR-1 merges, run `make hooks` once. The pre-commit hook then refuses a commit on `main` (D-8).
3. Run `make verify` before every PR. Until PR-1, run the interim STE check from `CLAUDE.md` by hand.

## The Steam Deck

1. Put the Deck in desktop mode and enable SSH, or copy the Linux export by USB.
2. Copy the Linux export of the Game project to the Deck. Run it from a shell until the Steam build exists (D-85, D-92).
3. Record the readability and the frame time under M-6 in `docs/design.md` (D-161).

## Owner actions on GitHub

1. After PR-3 merges, require the `ci`, `smoke`, `ste-check`, and `review-gate` checks on `main` (OQ-3, D-4). GitHub lists a check as a choice only after it ran once.
2. Turn off "Allow merge commits" and "Allow rebase merging", and keep "Allow squash merging" (D-8).

## Session start

1. Run `git fetch origin` and `git status --short --branch`.
2. Read `docs/session-handoff.md`, then `CLAUDE.md`.
3. Start a branch from `main` for the PR of this session (D-18).
