# Moira Astro

An original astrology symbol font, licensed under the [SIL Open Font License 1.1](OFL.txt), with **Moira** as the Reserved Font Name.

Current development baseline: **0.13.2-alpha.1** — 726 glyphs, 225 mapped characters, 711 optional tokens and 35 direct-character registry routes. The standalone project includes a complete-chart presentation pilot. Public beta publication remains a separate milestone.

## Try the font

- [TrueType font](fonts/MoiraAstro-Regular.ttf)
- [WOFF2 webfont](fonts/MoiraAstro-Regular.woff2)
- [Browser specimen](index.html) — open this file locally after cloning, or serve the repository with `python -m http.server 8000` and visit `http://localhost:8000/`.
- [Complete-chart pilot](demo/chart-pilot/index.html) — distributed/crowded fixtures, light/dark themes, TTF/WOFF2 comparison and a three-page print folio. See [the pilot guide](docs/CHART_PILOT.md).
- [Entry registry](entry-map.csv) and [compatibility aliases](aliases.csv)
- [Usage guide](docs/USAGE.md) and [chart presentation contract](docs/PRESENTATION.md)

The repertoire covers the selected master inventory through Batch 21: zodiac and body symbols, aspects, lots, notation, lunar/eclipse forms, fixed-star sigils, hypothetical points and astronomical reference markers. This is coverage of the agreed inventory, not a claim of exhaustive historical coverage.

## Build and verify

Use Python 3.13 and a virtual environment:

```text
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` on PowerShell or `source .venv/bin/activate` on macOS/Linux, then:

```text
python -m pip install -r requirements.txt
python -B validate.py
python -B tests/check_project.py
python -B tests/check_chart_pilot.py
```

`validate.py` builds twice from source in temporary directories and compares both builds with the shipped TTF/WOFF2. It checks licensing, outlines, glyph order, hinting, metrics, mappings, OpenType tables, all token routes and default behavior. Run this before rebuilding committed binaries so a stale font cannot be silently hidden by a build.

To rebuild intentionally:

```text
python -B build.py
```

For a separate output directory, use `python -B build.py --output build/fonts`. On Windows, `python -B native_smoke.py` additionally tests process-private font intake and removes the font resource afterward. Reports go into ignored `build/`.

GitHub Actions runs font/source, chart-fixture and JavaScript syntax checks on Windows and Linux for pushes and pull requests. Windows also runs the native intake check. Local browser/PDF review commands are documented in the pilot guide. The workflow does not publish releases or deploy a website.

## Source of truth

`source/MoiraAstro-Regular.ttx` is the complete editable source used by the reproducible build. It includes every outline, instruction, metric, mapping, layout rule and license record. The committed fonts are generated artifacts for convenient use.

`designs/` retains original review-stage SVG masters and design/research records. `masters/` retains the font-stage SVG masters, including optical refinements. These are historical inputs, not automatically rebuilt dependencies. Editing an archived SVG does not update the font: changes must be admitted into the active TTX, registry and regression contract together. See [the design archive](docs/DESIGN_ARCHIVE.md).

`entry-map.json` is the active font access and semantic-policy registry. `inventory/inventory.json` is the reconciled 327-record coverage snapshot, with original planning records retained verbatim. `sources/` holds admitted batch data and the Unicode variation reference. `provenance/imports.json` records the original import paths and hashes; the earlier packets are not runtime dependencies.

## Meaning and model boundaries

Glyph appearance does not select a native calculation, a lunar model, a zodiac scheme or a lot formula. Keep explicit model labels where icons are shared. Retain fixed-star witness labels and distinctions between attested forms, original redrawings and invented Moira symbols. Fortune, circled-S Spirit, 24-degree Quindecile, Tao at 165 degrees and the historical alternatives retain their established routes. The font has no dependency on the Moira engine.

## License and next steps

Copyright 2026 Moira Astro contributors. Original glyph designs. With Reserved Font Name Moira. Font Software is licensed under [SIL OFL 1.1](OFL.txt); see [NOTICE.md](NOTICE.md) for source-data and dependency boundaries. Licensing is embedded in both font containers.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CHECKS.md](CHECKS.md) and [the roadmap](docs/ROADMAP.md). Review the chart pilot's presentation choices and findings before preparing a documented public beta.
