# Source register

Retrieved or frozen on 24 October 2026. Exact source paths, URLs and SHA-256 receipts are in [input-provenance.json](input-provenance.json).

| ID | Source | Evidence role and limit |
|---|---|---|
| unicode17-data | [Unicode 17 character data](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt) | Final names and scalar identities. Frozen from the current font sources; Unicode license retained. |
| unicode17-2b00 | [Final Unicode 17 Miscellaneous Symbols and Arrows chart](https://www.unicode.org/Public/17.0.0/charts/PDF/U2B00.pdf) | Reference forms and final U+2BE0-U+2BE7/U+2BD7 assignments. Local archived copy from prior research, not an unversioned latest chart. No font data extracted. |
| uranian-proposal | [David Faulks, L2/16-064R](https://www.unicode.org/L2/L2016/16064r-uranian-planets.pdf) | Labelled eight-symbol reference, p. 1; text/chart examples, pp. 3-8. Rendered images used because extracted glyph text is unreliable. |
| feist-early-years | [Michael Feist, The Hamburg School: The Early Years](https://uraniansociety.com/USIG_articles/article_history_of_uranian_astrology_michael_feist.pdf) | Printed p. 13 / PDF page 6 reproduces 1935/1939 rulebook p. 42. First-four form/label evidence, not original-volume access or physical/model certification. |
| additional-astrology | [David Faulks, L2/16-080](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf) | Transpluto forms and usage examples, pp. 3-5. Draft codepoint is superseded by final Unicode data. No definitive glyph-origin claim adopted. |
| prior-brief | `references/NEXT_BATCH.json` | Exact nine-record Batch 14 scope and permanent semantic identities from the 0.5 audit. |
| own-controls | `references/pilot-font-glyphs.json`, `references/batch13-glyphs.json`, `references/batch04-glyphs.json`, `references/batch05-glyphs.json` | Original Moira body/sign, alternate, numeral, unit and Latin geometry. Frozen comparisons, with source and drawing hashes. |
| own-geometry | `references/geometry_expander.py` | New local copy of the established vector-checking helper. No font compiler is run. |

Rendered references are under `references/renders/`: final grid, labelled eight-point forms, usage samples, Transpluto examples and Feist's reproduced rulebook page. Detail crops aid visual inspection only; no reference bitmap or embedded font path enters a new master.

NamesList is a frozen supplementary identity reference. Browser specimens use the original Moira SVG paths; interface annotations use system text. No pricing, current popularity or model implementation claim is inferred from external material.
