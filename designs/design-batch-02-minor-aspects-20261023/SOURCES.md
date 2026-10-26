# Sources and evidence roles

Accessed 23 October 2026. Character assignments are pinned to Unicode 17.0.0. New drawings are original Moira geometry; reference fonts or PDF outlines are not extracted, traced or imported.

| Source ID | Primary source and location | What it supports / limit |
|---|---|---|
| `moira` | [Native constants excerpt](references/native-aspect-definitions.txt), from [constants.py](C:/dev/moira/moira/constants.py:475) | Exact current longitude identities, angles and abbreviations; not independent historical form attestation |
| `moira-declination` | [declination_aspects.py](C:/dev/moira/moira/declination_aspects.py), [frozen source excerpt](references/native-declination-definitions.txt) and [inventory metadata](references/inventory-aspects.json) | Native declination vocabulary, signed-hemisphere and equator policy; no glyph default or P/CP abbreviation is inferred from engine code |
| `ucd17` | [UnicodeData](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt), [NamesList](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt), [assigned-form chart](https://www.unicode.org/Public/17.0.0/charts/PDF/U2B00.pdf), U+2BF3-U+2BF8 | Final names/assignments and explicit usage annotations; does not prescribe Moira outlines or a computational model |
| `suignard2017` | [Michel Suignard, L2/17-020R2 / WG2 N4811](https://www.unicode.org/wg2/docs/n4811-fdbk-extra-aspect-sym.pdf), table 1 on PDF p.2; table 3 on pp.3-4 | Letter, raised-figure and geometric notation evidence; rounded angle labels and contradictory Sentagon ratios are not engine authority |
| `faulks2016` | [David Faulks, L2/16-174R](https://www.unicode.org/L2/L2016/16174r-astrology-aspects.pdf), revised 11 November 2016 | Regional form/context evidence. Proposal-era names and positions are superseded by the final UCD |
| `faulks-letter` | [David Faulks, Variations and Unifications?, 16 March 2016](https://unicode.org/mail-arch/unicode-ml/y2016-m03/0075.html) | A researcher's direct report of parallel/contra-parallel form variants; exploratory encoding discussion, not proof of a universal symbol convention |
| `astrolog-aspects` | [Walter Pullen, Astrolog: Distance Aspects](https://www.astrolog.org/astrolog/astdist.htm), Standard Aspects table | The author's description of Astrolog's own glyph conventions; no source code, outlines or computational defaults imported |
| `astrolog-manual` | [Astrolog 8.00 manual](https://www.astrolog.org/ftp/astrolog.htm), `-gp` section | Explicit two-line and grid structures for that program's parallel/contra-parallel glyphs; not a dedicated Unicode grid assignment |

## Frozen inputs

`references/` contains full documentary PDFs, Unicode data with its accompanying license, the source excerpt, the prior original Moira aspect artwork and inventory aspect metadata. Existing font/inventory/Batch 01 files remain read-only. The original native constants SHA-256 is printed in the excerpt.

The two Astrolog pages were read successfully using the web research reader. Direct local HTTP copying returned 406, so no full HTML copies of those two pages are claimed. [Retrieval record](references/html-source-retrieval.json) records this limit. The source URLs and relevant sections remain usable citations.

Some old proposal PDF fonts are not embedded. Poppler emitted substitution notices while rendering N4811; the Latin/raised-figure structure was inspected and checked against the document text and final NamesList annotations. The regional glyph structures were independently inspected in the archived Unicode chart, rather than relying on proposal font substitution.

## Provenance of the new artwork

All new paths are authored in [build_designs.py](build_designs.py), using explicit coordinates and Moira's existing stroke/terminal language. The metadata records source IDs for each form. Final glyph/feature admission remains pending owner review. No outside font license is inferred from a Unicode assignment or from a historical form's appearance in a document.
