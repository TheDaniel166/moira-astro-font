# Batch 14 design decisions

Draft 01, 24 October 2026. Nine original source-vector proposals, with existing glyphs unchanged.

| Study | Selected draft form | Small-size focus |
|---|---|---|
| Cupido | Curved hook, right ring, shared bar and lower cross | Keep ring open and separate both bar levels |
| Hades | Right-opening C curve and lower cross | Preserve mouth and descending stem |
| Zeus | Upright arrow terminating in crossed lower arms | Keep diagonal spaces open; no extra lower stem |
| Kronos | Detached domed cap above cross | Preserve the gap; do not join it into an umbrella |
| Apollon | Curved hook, common bar and twin joined posts | Open both windows and retain lower bar |
| Admetos | Upper cup, quartered ring, lower stem | Keep all four fields unfilled |
| Vulkanus | Arrow from outlined triangle | Open triangle counter and distinct upright arrow |
| Poseidon | Opposed horizontal arcs with vertical stem | Keep spacing and orientation clear beside Pisces |
| Transpluto | Arrow, ring and curved internal bowl | Keep both fields open; distinguish it from Uranus's central point |

All strokes are 60 source units with rounded caps and joins. Every new form has a 1,000-unit source proof advance; those cells are not final font metrics. The established 1.08 preview scale is retained.

The Transpluto horizontal-divider variant is retained in the source research images rather than added as an unrequested tenth master. All nine selected forms preserve their own assigned characters. No PUA, feature or token allocation is made.

Hypothetical Cupido is separate from asteroid (763) Cupido and similarly named lots. Vulkanus/VULCANUS is separate from intramercurial Vulcan. Transpluto is a separate convention, not a ninth Hamburg point. The drawings select no orbit or model.

## Review and later integration

Review all nine at 14/18/24/32 px in both themes, with names and current-glyph controls. Fourteen pixels is a stress case for the dense ring/post constructions. The supplied checks include geometry bounds, source-space positive/negative witnesses, actual-size raster presence and 24/32 px counter/gap witnesses. Source-vector checks do not certify later TTF/WOFF2 rasterization.

If the designs are approved, a separate font integration can append U+2BE0-U+2BE7 and U+2BD7 while preserving all current 667 glyphs, 212 mappings, 529 tokens, historical variants and lot families. It should verify exact identities, text access, final metrics, TTF/WOFF2 parity and actual font-size proofs. No global substitution of similarly shaped body/letter glyphs is implied.
