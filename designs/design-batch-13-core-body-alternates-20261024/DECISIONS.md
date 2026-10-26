# Batch 13 design decisions

Draft 01, 24 October 2026. Seven alternate-character studies, leaving all existing defaults intact.

| Study | Chosen construction | Review focus |
|---|---|---|
| Ray Sun | Solid disc, eight separated rays | Ray/disc separation and a clean solid interior |
| Opposite Moon | Mirror of Moira's original filled crescent | Matching weight and opposite opening; identity remains U+263D |
| Astronomical Uranus | Ring, central point, upright arrow | Dot survives; arrow is upright rather than Mars's diagonal |
| Pluto two | Orb, open cup, stem and cross | Open orb/cup gap; distinct from Mercury's construction |
| Pluto three | Double arch, cross, lower ring | Recognisable head and an open lower counter |
| Pluto four | Orb over outlined crescent bowl | Both the orb counter and white bowl interior remain open |
| Pluto five | Ring with bowed internal division | Both fields unfilled; visibly different from zero, O and a filled Moon crescent |

Each retains its separate assigned Unicode scalar. The mapping plan is additive: U+2600, U+263D, U+26E2 and U+2BD3-2BD6. This packet does not replace U+2609, U+263E, U+2645 or U+2647, rewrite source text, assign a PUA value or choose an `ssXX`/`cvXX` slot. A later explicit body-icon preference can select characters at the product layer without changing the astronomical model.

The Moon study is deliberately a mirror of the accepted own geometry rather than an unrelated new silhouette. It is a generic body-icon alternative; global stylistic substitution in phase text is excluded. No new lunar model or phase calculation is involved.

Pluto three uses the ring-bearing reference form. Other proposal variants are documented as research evidence and receive no additional drawings or access routes here. Pluto five's bowed divider is a graphic convention; no physical orbit is implied.

All new source advances are 1,000-unit proof cells with 60-unit strokes, rounded caps and joins. The existing 1.08 scale and y-offset -50 are used in the 1,000-unit em previews. Frozen body controls use their original source cell; ordinary text controls retain their original source advances. Final font metrics remain a later design/build decision.

The enlarged Sun disc is an explicit closed cubic path. This removes a browser raster seam observed with the initial SVG circle primitive while preserving the solid circular construction. No existing Sun drawing was changed.

## Review and later integration

Review the 14/18/24/32 px proof in both themes, along with the family and identity comparisons. Fourteen pixels is a stress case for the Uranus point, Pluto orb counters and crescent details. The packet separately checks 24/32 px counter/gap witnesses and actual-size raster presence at every size.

A later approved font build should add assigned characters and the registered Sun text-presentation sequence, check TTF/WOFF2 parity and copy/paste, review final optical advances, and prove preservation of every existing outline/mapping/token/variant. Batch 12 is approved in the conversation but remains a separate design packet; no integration or master-inventory update is performed by Batch 13.
