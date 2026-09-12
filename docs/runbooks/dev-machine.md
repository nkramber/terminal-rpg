# Runbook: the development machine

Status: procedure, written 2026-09-12 for the owner's Mac (D-1, OQ-2). Written in ASD-STE100.

Facts checked on 2026-09-12:

- The machine is arm64 on macOS 26.5.
- `rustc` and `cargo` are absent from the command path.
- `gh` has a login as the owner, and `git` has the `origin` remote for `nkramber/terminal-rpg`.
- Python 3.9.6 is present. The interim STE checker needs it until PR-2 (D-10).
- The repository on GitHub is public (D-4), and it holds no commit.

## Install Rust

1. Run the rustup installer from https://rustup.rs and accept the default profile.
2. Open a new shell, then run `rustc --version` and `cargo --version`.
3. Run `rustup component add clippy rustfmt`.
4. After PR-1 merges, the file `rust-toolchain.toml` pins the version, and rustup installs it on the first `cargo` command.

## Prepare a checkout

1. Clone the repository: `git clone git@github.com:nkramber/terminal-rpg.git`.
2. After PR-1 merges, run `make hooks` once. The pre-commit hook then refuses a commit on `main` (D-8).
3. Run `make verify` before every PR. Until PR-1, run the interim STE check from `CLAUDE.md` by hand.

## Owner actions on GitHub

1. Install the gitar app on the repository (OQ-1, D-14).
2. Create the label `review-override` on the repository (D-16).
3. After PR-3 merges, require the `ci`, `ste-check`, and `review-gate` checks on `main` (OQ-3, D-4). GitHub lists a check as a choice only after it ran once.
4. Turn off "Allow merge commits" and "Allow rebase merging", and keep "Allow squash merging" (D-8).

## Session start

1. Run `git fetch origin` and `git status --short --branch`.
2. Read `docs/session-handoff.md`, then `CLAUDE.md`.
3. Start a branch from `main` for the PR of this session (D-18).
