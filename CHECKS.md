# Validation

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](OFL.txt).

Run `python -B validate.py` to verify the active font. The imported 0.13.2 baseline passes 6,251 checks: two byte-identical builds from complete TTX source, both distributed containers, exact frozen outlines/hints/metrics, stable cmap/layout tables, full embedded OFL metadata, token enable/disable behavior and direct mappings. The report is written to `build/checks.json`.

Run `python -B tests/check_project.py` for archive hash integrity, SVG parsing, current documentation links, source presence and project layout. The report is written to `build/project-checks.json`.

On Windows, `python -B native_smoke.py` checks the exact loaded name table, all 726 glyph metrics and 184 BMP mappings using a process-private font resource. The resource is removed afterward. The report goes to `build/native-checks.json`.

GitHub Actions runs the source/encoding/project checks on Windows and Linux. Windows additionally runs GDI intake. A clean tracked-tree check catches accidental changes made by validation.

The original dated font release report and manifest are retained under `provenance/`. They document the source release before repository adaptation. The preceding stabilization run also included browser, native Word export and PDF reviews. Those are dated evidence for unchanged font data; this repository's CI does not claim fresh Word, macOS/Linux desktop, Adobe, physical-printer or universal rasterizer certification.

The preserved SVG/research material is not the active build pipeline. Complete editable font source and shaping logic are in [the TTX](source/MoiraAstro-Regular.ttx); see [the archive guide](docs/DESIGN_ARCHIVE.md) and [contribution rules](CONTRIBUTING.md).
