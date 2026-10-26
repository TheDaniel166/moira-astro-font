# Source register

Retrieved or frozen on 24 October 2026. Exact paths, URLs and SHA-256 receipts: [input-provenance.json](input-provenance.json).

| ID | Primary source | Use and limit |
|---|---|---|
| unicode17-2600 | [Unicode 17 Miscellaneous Symbols](https://www.unicode.org/Public/17.0.0/charts/PDF/U2600.pdf) | Final Sun, Moon and Uranus identities and reference forms. No font data extracted. |
| unicode17-2b00 | [Unicode 17 Miscellaneous Symbols and Arrows](https://www.unicode.org/Public/17.0.0/charts/PDF/U2B00.pdf) | Final four Pluto mappings and reference forms. The archived chart is pinned to version 17. |
| unicode17-data | [Final Unicode 17 character data](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt) | Exact scalar/name checks; frozen existing source and license. |
| unicode17-names | [Unicode 17 NamesList](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt) | Character identity cross-references; copied from the prior inventory sources. |
| unicode17-emoji | [Unicode 17 emoji variation data](https://www.unicode.org/Public/17.0.0/ucd/emoji/emoji-variation-sequences.txt) | Registered U+2600 FE0E text presentation. No other text-presentation sequence is invented. |
| uranus-proposal | [Anderson, Iancu and Sargent, L2/09-300](https://www.unicode.org/L2/L2009/09300-uranus.pdf) | Contrastive-use rationale; p. 5 reference construction and supporting examples. Historical encoding context. |
| pluto-proposal | [David Faulks, L2/16-067R](https://www.unicode.org/L2/L2016/16067r-astrological-plutos.pdf) | Four construction families and visual usage evidence. Draft positions differ from final assignments; historical/region claims are attributed rather than independently certified. |
| nasa-symbols | [NASA Solar System Symbols](https://science.nasa.gov/resource/solar-system-symbols/) | Context for astronomical Uranus and the existing Moon/Pluto defaults. Not authority for every alternate. |
| inventory | `references/ALTERNATE_FORMS.md`, `references/alternate-coverage.json` | Exactly seven core-body forms left pending by the 0.4 inventory comparison. |
| own-controls | `references/pilot-font-glyphs.json`, `references/batch04-glyphs.json`, `references/batch05-glyphs.json` | Original Moira defaults, numerals, units and Latin comparison geometry. Frozen; no source edits. |
| own-geometry | `references/geometry_expander.py` | Copied SVG checking helper. It expands original vectors for validation without building a font. |

Rendered primary-reference pages are under `references/renders/`: Pluto proposal pp. 1, 8, 12, 14; Uranus proposal p. 5; and the two final version 17 grids. They are local research references, separate from Moira's specimen artwork.

The initial new-characters-only chart URL for the 2600 block returned 404. Research resumed with the archived full version 17 charts above. The preservation baseline was retained, not recaptured. Unversioned current charts can point at a later edition; they are not used as this packet's mapping authority.
