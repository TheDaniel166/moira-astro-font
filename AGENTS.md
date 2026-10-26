# Repository Guidelines

## Project Structure & Module Organization

This is a standalone font project. The active build reads `source/MoiraAstro-Regular.ttx`, a complete editable FontTools XML font. `fonts/` holds its generated TTF/WOFF2. The entry map controls token access and preserves per-form semantic/source policies; the reconciled inventory is a dated coverage snapshot.

`designs/` and `masters/` retain original review and font-stage SVGs. They are archival inputs, not automatically compiled dependencies. `provenance/imports.json` records their original hashes and lineage. Dated “draft” or “not integrated” statements must remain historical; the current TTX, entry map and root license define the active font. See `docs/DESIGN_ARCHIVE.md`.

## Build, Test, and Development Commands

Use Python 3.13 with `python -m pip install -r requirements.txt`.

- `python -B validate.py`: two temporary source builds, shipped-byte equality, glyph preservation, encoding/shaping and license checks; report in `build/checks.json`.
- `python -B tests/check_project.py`: frozen-import integrity, SVG parsing, current links and portable project structure.
- `python -B build.py`: intentionally regenerate committed fonts. Use `--output build/fonts` for scratch output.
- `python -B native_smoke.py`: Windows-only, process-private GDI intake; no global installation.

Run validation before regeneration so stale committed binaries remain visible. CI runs on Linux and Windows, with native intake on Windows. Generated reports and virtual environments are ignored.

## Glyph, Source and License Boundaries

Keep existing mappings, optional tokens, historical variants and the default unslashed zero. Discretionary ligatures remain opt-in. Intentional repertoire changes require version, TTX, registry and baseline-contract updates together; never reset the contract merely to silence checks. Preserve archived records and add new design records for refinements.

Font appearance never chooses a native model, lunar calculation, zodiac scheme or lot formula. Historical fixed-star forms require witness labels; shared icons require explicit context/model labels. No Moira engine checkout is a build dependency.

Retain SIL OFL 1.1, Reserved Font Name Moira, embedded licensing and the separate Unicode notice. External font contours and proprietary reference fonts are not project sources. Publication, release tags and visibility changes are separate from source validation.
