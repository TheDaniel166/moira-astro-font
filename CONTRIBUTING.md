# Contributing to Moira Astro

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](OFL.txt).

## Setup and checks

Use the pinned dependencies in `requirements.txt`. Run `python -B validate.py` and `python -B tests/check_project.py` before submitting changes. Windows contributors can also run `python -B native_smoke.py`. These commands keep generated reports under ignored `build/`.

The source rebuild uses only the checked-in TTX, license and pinned font libraries. No earlier output packet, engine checkout or downloaded font is required. CI checks both Linux and Windows; the Windows job checks native font intake.

## Glyph and encoding changes

Use `source/MoiraAstro-Regular.ttx` for active font edits. Update `entry-map.json` and its CSV alongside any access change. Preserve existing tokens and mappings unless an explicitly documented versioned change requires otherwise. Discretionary ligatures remain opt-in; the unslashed zero stays the default. New symbols must include a meaning, definition/source limits, accessible label and an explicit distinction between an attested form and an original invention.

The source baseline freezes the current repertoire, mappings, metrics and shaping rules. Intentional additions or changes require a reviewed update to `source/baseline-contract.json`, the version metadata and validation expectations. Do not regenerate the baseline merely to silence a failure.

Keep historical fixed-star variants and witnesses. A visual cue must not select a lunar model, native calculation, zodiac scheme or lot formula. Chart-size review should include complete labels, crowded chart entries, both light/dark themes and PDF output when presentation changes.

## Archive and provenance

`designs/`, `masters/`, admitted `sources/` and `inventory/planning/` are preserved import records. Add a new design record for refinements; retain the original and identify which form is active. `tests/check_project.py` checks frozen imports against `provenance/imports.json` so accidental edits are visible. See [the archive guide](docs/DESIGN_ARCHIVE.md).

Do not add external font contours, proprietary font files, local working-tree observations or personal machine paths as build dependencies. Keep source citations as citations and preserve applicable third-party notices.

## Review and release

Explain the visible behavior, meaning/encoding impact and checks run in change descriptions. This initial repository has no prior commit convention or PR template. Public releases and repository visibility changes are separate maintainer actions. The current next milestone is [the chart pilot](docs/ROADMAP.md).
