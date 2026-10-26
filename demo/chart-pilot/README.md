# Complete-chart presentation pilot

Copyright 2026 Moira Astro contributors. Licensed under SIL Open Font License 1.1; see [OFL.txt](../../OFL.txt).

Open [index.html](index.html) locally, or serve the repository root with `python -m http.server 8000` and visit `/demo/chart-pilot/`. Both font files are loaded from the repository. There are no external assets or requests.

This is a chart presentation/legibility review, not a calculator. The two fixtures contain deliberately constructed longitudes and motion states. Equal 30-degree sectors are labelled fixture geometry. Native engine models, ephemerides, birth data and lot formulas are not selected or evaluated.

## Data

`assets/fixtures.json` is canonical. Its top level contains `schema_version`, source/license notices, `signs`, `motions`, `aspectDefinitions`, `aspect_rule`, `fixtures`, `fixedStars`, `satellites`, `specialistLegend` and `sizeSamples`. Each fixture contains `id`, `name`, `description`, `sector_origin`, `sector_geometry`, `positions`, `lots` and `minorBodies`.

Position entries have `id`, `name`, `symbol`, `longitude`, `motion`, `model` and `short_name`. Lots explicitly retain `formula_selected:false`. Star entries retain the registry's exact token, witness and variant identity. Satellite entries retain the existing parent/Roman designation composition policy.

`assets/fixtures.js` is an exact JSON payload in the classic assignment `window.MOIRA_FIXTURES = <JSON>;`, so the pilot works under `file://` without fetching JSON. Regenerate both fixture files with `python -B demo/chart-pilot/assets/build-fixtures.py`. The generator reads the existing registries and writes only these two demonstration files.

## Interaction and verification

Controls switch `fixture` (`balanced`/`crowded`), `theme` (`light`/`dark`) and `format` (`woff2`/`ttf`). `window.MOIRA_PILOT` exposes `ready`, `getState()`, async `setState(patch)` and `measure()`. UI controls and the testing helper share one renderer. All actual font runs have `data-font-symbol` and `data-role`; wheel callouts have `data-callout-id`, `data-label-id` and `data-fixture-id`.

The wheel is a fixed 860×690 CSS-pixel schematic to retain 18 px marks. It scrolls within its region on narrow screens. The crowded fixture retains exact-angle anchors while distributing exterior callouts with leaders. The equivalent position table supplies accessible names, models, motion states and longitudes. Aspect examples use shortest circular separation and a 2-degree display orb; up to two closest pairs per major aspect family are shown in both the table and wheel.

Each overflowing companion table shows its own scrolling instruction. Focus the table region and use Left/Right arrow keys, or scroll/pan horizontally to reveal every column. The instruction disappears when the table fits. Chart longitudes, center annotations and screen model qualifiers use 11 px text alongside the unchanged 18 px chart marks.

Print uses three Letter landscape sheets: wheel/positions; aspects/lots/minor bodies; fixed stars/satellite compositions/context and size review. The print wheel is scaled to a declared 700 px width to fit beside the complete position table; the screen wheel remains 860 px with actual 18 px marks. The output stays vector/text based; no screenshot is used for printing. The existing fonts and historical forms are unchanged.
