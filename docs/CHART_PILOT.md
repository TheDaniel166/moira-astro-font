# Complete-chart presentation pilot

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](../OFL.txt).

Open [the demonstration](../demo/chart-pilot/index.html) locally, or serve the repository with `python -m http.server 8000` and visit `http://localhost:8000/demo/chart-pilot/`. Its scripts and fonts are local; it also works under `file://`.

## Review content

The pilot uses the unchanged 0.13.2 font in two deliberately constructed fixtures. The distributed fixture exercises the major aspect families. The crowded fixture places six bodies at 63–69 degrees. Actual angle anchors remain fixed; exterior callout lanes separate labels without changing the positions. Twelve equal 30-degree display sectors and a 15-degree origin are explicit fixture geometry. All displayed positions and motion states are fixture data.

The companion tables include full position/model labels, aspect angles/separations/orbs, Fortune, circled-S Spirit, longer lot names and the four-letter `Parc` abbreviation. Dense minor-body marks use 24 px. Historical Sirius, Regulus and Vega forms retain their full Agrippa 1533 witness at 32 px; the separate Regulus chart form uses 24 px. Four satellite compositions retain their names, 24 px parent, 14 px ordinary Roman designation, 4 px gap and common baseline. The size strip distinguishes 14 px stress from reviewed 18/24/32 px use.

The UI switches fixtures, themes and font formats through the same renderer. The chart remains 860 by 690 screen pixels with actual 18 px font symbols. On narrow screens, contained regions scroll rather than shrinking the symbols. Overflow-aware instructions identify the hidden table columns. Keyboard focus is visible. If fonts fail to load, symbol marks are hidden and the named positions remain readable with a recovery message.

## Fixture source and independent checks

The fixture authoring generator is `demo/chart-pilot/assets/build-fixtures.py`. It produces the canonical `fixtures.json` and a byte-consistent classic-script payload in `fixtures.js` for local-file operation. Regenerate deliberately after changing fixture definitions, then run:

```text
python -B tests/check_chart_pilot.py
```

This test regenerates both files in an isolated temporary tree, verifies equality, checks semantic/model boundaries, and independently shapes every fixture symbol in both font formats. It also validates the six-body cluster, major aspect angles, longer lot code, historical witnesses and satellite identity/layout records. Core font regression checks remain `python -B validate.py`.

Optional local visual-review dependencies:

```text
python -m pip install -r requirements-review.txt
```

With agent-browser installed and its matching Chromium runtime available, run these PowerShell scripts from the repository:

```text
./tooling/Capture-ChartPilot.ps1
python -B tooling/check_chart_browser.py
./tooling/Test-ChartInteractions.ps1
python -B tooling/check_chart_pdf.py
```

The capture script freezes source fingerprints, checks them again afterward, and records both fixtures/themes/formats at 1360, 768 and 390 px. The independent audit compares actual glyph advances with HarfBuzz, checks cell and callout bounds, detects label collisions, verifies every anchor against the declared longitude, recomputes aspect rows and compares TTF/WOFF2 glyph pixels. Satellite geometry is measured directly from DOM boxes.

The interaction script uses native controls, keyboard focus and horizontal scrolling, verifies the print action calls browser printing, and loads an isolated demo copy with no fonts to exercise a real failure state. It also exports the crowded fixture while an aspect table retains keyboard focus after horizontal scrolling. The PDF checker requires that export to match all three unfocused crowded pages pixel for pixel, preventing screen focus outlines from leaking into print. It does not claim a physical touch-device test.

## Print and review findings

The browser print layout targets **three Letter-landscape pages**: wheel/positions, relationships/points, and historical forms/compositions. The vector wheel is 700 px wide in print; its symbol text is approximately 10.99 pt. Table symbols are 13.5 pt or larger, dense symbols 18 pt, and historical forms 24 pt. Screen size labels describe CSS sizes; the print-wheel caption states its separate scale.

Both fixtures export to `build/chart-pilot/MoiraAstro-*-chart-pilot.pdf`. The PDF checker verifies page size/count, named data/model/witness labels, text bounds, embedded font programs and glyph raster presence through MuPDF, then renders all six pages to PNG. The font subsets and host text fonts in these QA PDFs are separate from the distributed font binaries. Reports, screenshots and PDFs stay under ignored `build/chart-pilot/`.

The review found that the mobile wheel and tables need scrolling to preserve the established glyph sizes. The final interface makes that explicit for every overflowing table. Tiny screen longitude/model annotations were enlarged to 11 px. Screen focus rings retain 8 px clearance; print suppresses them. No glyph changes were needed. Letter-landscape geometry was reviewed directly instead of assuming the browser exporter would honor an A3 page setting.

The review covers Chromium and MuPDF output. It does not certify physical printers, physical touch devices, every application/rasterizer, or astronomical accuracy of constructed fixtures. An independent agent also reviewed the final design; all available agents used the same provider, so no second-provider review is claimed. Owner review of these presentation conventions remains separate from the completed technical checks.
