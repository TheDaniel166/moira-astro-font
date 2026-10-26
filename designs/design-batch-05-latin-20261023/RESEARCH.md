# Basic Latin letter design and provenance

23 October 2026. Unicode identities remain pinned to 17.0.0, matching the master inventory.

## Repertoire and character identity

The [original inventory](../moira-astro-character-inventory-20261023/MASTER_INVENTORY.md) plans the 26 uppercase letters and lowercase x at P1, with the other 25 lowercase letters at P2. The [frozen entries](references/planned-latin.json) preserve all 52 identities and the inventory hash. The task draws the remaining forms together to make the basic notation alphabet coherent.

Unicode's [Chapter 7, sections 7.1 and 7.1.1](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-7/) identifies the 26 basic case pairs and distinguishes glyph variation from character identity. Its discussion includes open/closed a and g forms in ordinary Latin text. The proposed single-storey g therefore remains U+0067 LATIN SMALL LETTER G; no IPA/script-g replacement is introduced. The chapter also explains that this basic set alone does not cover most languages using Latin script.

Formal names and categories come from the pinned [UnicodeData](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt), retained as [selected records](references/unicode17-records.json) with the source-file hash. No ASCII character gains an astrological semantic through this font work. Meaning remains in the surrounding text/data.

## Original sources and reuse

| Source | Role in this packet |
|---|---|
| [Batch 03 components](references/prior-letter-components.json) | Eighteen standalone letters: ten uppercase and eight lowercase. Their geometry and advances remain unchanged |
| [Batch 02 aspect letters](references/prior-aspect-letters.json) | Exact Q/N/U standalone paths, plus the original compact Qd comparison. Translation into a provisional text cell does not redraw their paths |
| [Batch 04 notation](references/prior-notation.json) | Unchanged numerical, punctuation and unit controls; exact accepted zero/alternate drawings |
| [Earlier decision record](references/prior-decisions.json) | Accepted Spirit default/alternate and prior minor-aspect direction |
| [Master inventory](references/planned-latin.json) | IDs, meanings and release priorities; it does not establish historical letterform doctrine |

The compact Qd contains a small context-specific d at a different scale. Promoting it directly to a full-size ordinary letter would conflate composition with character design. It remains frozen while a new d is authored around the existing p/a bowl family. The two renderings are shown separately; neither is a new codepoint and no global Qd ligature is implemented.

## Design rationale

- Round terminals, 60-unit source strokes and the established 1.08 preview scale continue the family.
- New capitals share the existing cap rhythm. B/P/G open their counters and apertures; W receives its own wider advance rather than being compressed.
- New lowercase ascenders follow the existing t/p/i neighborhood. The b/d/q bowl family complements p; g and y use curved descending tails. No earlier shape is adjusted to force a match.
- A curved foot on l separates it from the already barred I and flagged digit 1. O is wider than the existing tabular zero. The unslashed zero remains the accepted default.
- rn/m and cl/d receive explicit comparison proofs. Word spacing and 40-unit letter tracking are provisional composition choices, not measured kerning or a validated reading-performance claim.

Every new coordinate is authored here. Sources establish identities and the existing Moira design language; they do not supply external font outlines. No third-party glyph is extracted, traced, imported or raster-converted. The web chapter was read through the research reader; no full local HTML copy is claimed.

## Metadata source IDs

| ID | Evidence role |
|---|---|
| `inventory` | Frozen planned character entries and priorities |
| `unicode17` | Formal identities and the cited Basic Latin/glyph-variation discussion |
| `original-moira-artwork` | Frozen source components and newly authored coordinates with explicit origins |

The [decision register](DECISIONS.md) records acceptance independently of the new review drawings. No feature slots, private-use values, font binary coverage, model selection or distribution license is decided by this batch.
