# Source register

All online sources were retrieved on 24 October 2026. Local receipts and SHA-256 values are in [input-provenance.json](input-provenance.json). The research HTML snapshots are reference documents, not glyph assets.

| ID | Primary source | Use and limit |
|---|---|---|
| unicode17-data | [Final Unicode 17 character data](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt) | Exact character names, scalars and decompositions. Copied from the existing 0.4 source snapshot; frozen hash `2e1efc1dcb59c575eedf5ccae60f95229f706ee6d031835247d843c11d96470c`. License retained. |
| unicode-greek | [Unicode 17 Chapter 7, §7.2](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-7/) | Ordinary Greek identities versus symbol forms; loopy/straight phi distinction. No font outlines copied. |
| unicode-punctuation | [Unicode 17 Chapter 6, §§6.2.6–6.2.7](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-6/) | Straight ASCII quotation mark and overloaded apostrophe. Does not supply a Moira glyph drawing. |
| unicode-superscripts-faq | [Unicode ligatures, digraphs and presentation FAQ](https://unicode.org/faq/ligature_digraph.html) | Limits of encoded superscripts and general layout. Living FAQ; the final version 17 data above governs this packet's identities. |
| nasa-coordinate-units | [NASA LAMBDA coordinate entry](https://lambda.gsfc.nasa.gov/data/interfaces/iras/coordinates.html) | Coordinate unit examples only. Its application-specific epoch/model conventions are not adopted. |
| prior-brief | `references/NEXT_BATCH.json` | Prior inventory comparison's 15-character brief; 14 existing gaps plus the missing superscript-one addition. |
| own-controls | `references/batch04-glyphs.json`, `references/batch05-glyphs.json`, `references/base-glyphs.json` | Original Moira Latin, numeral, punctuation and ² ³ ⁴ geometry. Read-only inputs, with byte-for-byte comparison drawings. |
| own-geometry-helper | `references/geometry_expander.py` | Local copy of the existing SVG outline expansion helper, used only for checking vectors. No font compiler is run. |

The design research separates assigned character identity from Moira's own outline construction and contextual use. No historical star sigil, existing body glyph or alternate is redrawn in this packet.
