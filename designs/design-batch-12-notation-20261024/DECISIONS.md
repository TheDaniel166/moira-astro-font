# Batch 12 design decisions

Draft 01 for visual review, 24 October 2026. Fifteen new proposals; no prior glyph revision and no font integration.

| Family | Selected construction | Small-size purpose |
|---|---|---|
| λ | Curved ascender, diverging feet | Keep the upper entry visible and avoid a Latin l silhouette |
| β | Rounded upper entry, two bowls, descending stem | Separate it from Latin B/b while opening both counters |
| δ | Lower loop and curling upper stroke | Preserve delta's structure instead of reusing Latin d |
| α | Open crossing exit beside a rounded loop | Distinguish it from the approved single-storey Latin a |
| φ | Loopy small-letter form, descending return | Preserve U+03C6's technical contrast with the separate straight phi symbol |
| ε | Two open lobes and a short middle arm | Keep it separate from Latin e and a lunate-epsilon symbol |
| ⁰ | Unslashed oval | Follow the approved ordinary-zero default; no new slashed alternate |
| ¹ | Angled flag and foot | Stay recognisable beside a straight quote or lowercase l |
| ⁵ | Wide top, open neck, rounded lower bowl | Match the existing raised-digit weight |
| ⁶ / ⁹ | Open hooks with enlarged counters | Maintain the shared six/nine construction already used for ordinary numerals |
| ⁷ | Unbarred diagonal | Follow the approved ordinary-seven family |
| ⁸ | Two counters, fuller lower bowl | Retain two distinct holes in the larger chart-size proofs |
| ' / " | One / two vertical strokes | Contrast with the existing slanted prime and double-prime marks |

All seven new raised digits use the same 300-unit source advance and 58-unit stroke as existing ² ³ ⁴. They occupy the established raised zone; slight optical overshoots remain. Greek and quotes use 60-unit strokes with rounded caps and joins. These are original coordinate drawings, not mechanically reduced external outlines.

Greek advances are 600–700 source units; quotes are 220/360. These are design proposals for later font integration, not edits to current `hmtx`, cmap or shaping tables. The preview uses the established 1.08 transformation and a source-to-preview y offset of −50 in a 1,000-unit em.

The ordinary Greek characters are not aliases to Latin letters, dedicated Greek symbol variants or astrological points. No PUA, token or stylistic-set slot is allocated. A future straight-phi or other variant would require its own identity review and specimen.

Superscript ¹ is recorded as an inventory addition inside this packet only. The master inventory, 0.4 font build, previous drawings, Fortune/Spirit, lot codes and historical fixed-star variants remain untouched.

## Review and later integration

Review the complete family, identity comparisons and coordinate contexts in light and inverse. Fourteen pixels is a stress case: raised digits occupy only a small part of the em. The 24/32 px raster checks include background witnesses inside the enclosed counters; smaller samples remain available for visual comparison. No font rendering certification is inferred from those SVG checks.

After visual approval, a separate font build can add the fifteen assigned mappings while preserving all existing glyph outlines, mappings, tokens and variants. That build should check TTF and WOFF2 parity, character copy/paste, normalization expectations, advance/baseline behaviour, shaping preservation and actual chart-size font rasterization. It should not silently add unrelated Greek coverage, a generic `sups` feature or a slashed raised-zero alternate.
