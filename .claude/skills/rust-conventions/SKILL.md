---
name: rust-conventions
description: The Rust rules of this repo. Error handling with context, no unwrap outside tests, integer math in core, clippy pedantic, crate boundaries, test shape, and dependency policy. Load before you write or review Rust.
---

# Rust conventions skill

Load this skill before you write or review Rust in this repo (D-21). It applies the tenets to Rust. The scaffold PR, PR-1, creates the workspace, and this skill needs a revision pass after it merges.

## Crate boundaries

- `core` is the simulation. It has no dependency on ratatui, crossterm, the file system, the network, the clock, or the OS (G-1). It takes a seed, content, and inputs, and it returns state.
- `tui` is the front end and the binary. It reads `core` state, draws it, and turns key presses into inputs.
- `tools` holds the STE checker, the determinism lint, the review gate, and every other repository tool.
- A test that asserts the dependency list of `core` lives in `core`. A new dependency in any crate needs a decision entry (G-13).

## Determinism in core (T-7)

- No `f32` and no `f64`. Percentages, multipliers, and rates use fixed-point integers. Name the scale in the type or the constant, for example `Permille` or `BASIS_POINTS`.
- No `std::time`, `Instant`, `SystemTime`, or `rand::thread_rng`. The seed and the tick are the only sources of randomness and time (G-3).
- One random stream per subsystem, split from the run seed. A subsystem never borrows another stream.
- Iterate in a fixed order. Use `BTreeMap` and `Vec`, and never `HashMap`, where the order reaches the state (G-4).
- Every `core` behavior change bumps the simulation version constant (G-17).
- Saturate or check every arithmetic operation that a content value can drive. An overflow is an error with context, never a wrap.

## Errors (T-2)

- No `unwrap`, `expect`, `panic!`, `unreachable!`, or `todo!` outside test code and the assertion helper. A clippy lint refuses them.
- No `let _ = fallible()`. Handle the `Result` or return it.
- Every error type carries its context. Inside a run that is the seed, the tick, and the entity ids. Outside one it is the file path and the field.
- Use `thiserror` for error types in library crates, once a decision approves the dependency. Use an `enum` per crate boundary.
- An absent value is an error, never a default. `Option::unwrap_or_default` on a content field is a finding.
- Assertions stay on in release builds. Use `assert!`, never `debug_assert!`, for an invariant of the simulation.

## Content (D-7)

- Content types derive `serde::Deserialize` with `#[serde(deny_unknown_fields)]`. Every field is mandatory unless a decision names a default.
- A load error names the file, the field, and the reason.
- One test loads every file under `content/` and fails on the first error.
- Player-visible text is a string id, never a `String` literal in code (G-7).

## Style

- `cargo fmt` clean. Clippy at `pedantic` with `-D warnings`. Allow a lint only with a comment that names the reason, next to the allow.
- Explicit over implicit. No trait magic for a single use (T-1). Two concrete cases before a trait or a generic.
- Helpers go one level deep. A reader understands a function from the function and the signatures of its helpers.
- Name a function for what it does. Name a type for what it is. Avoid a `Manager`, a `Handler`, or a `Util`.
- Prefer `impl` blocks that read top to bottom: constructors, then queries, then mutations.
- Public items have a doc comment that states the contract, not the implementation.
- Comments explain a decision or a trap, and they cite a D-# id when one applies. Never a comment that repeats the code.

## Tests (T-3)

- Unit tests sit in a `tests` module next to the code. Integration tests sit in `tests/` of the crate.
- A property test is a seed loop: iterate a fixed seed range, assert the property, and name the seed in the failure message.
- A bug fix ships with a regression test that fails on the old code. The PR description names the test.
- A test asserts the contract, not a copy of the implementation.
- Use `#[should_panic]` never. Assert on the returned error instead.

## Commands

The Makefile is the entry point after PR-1 (D-3). The raw commands:

```
cargo build --locked --workspace
cargo test --locked --workspace
cargo clippy --locked --workspace --all-targets -- -D warnings
cargo fmt --all --check
```

Pin the toolchain in `rust-toolchain.toml`. Commit `Cargo.lock`. Run every command with `--locked`, so a lock drift fails instead of a silent update.
