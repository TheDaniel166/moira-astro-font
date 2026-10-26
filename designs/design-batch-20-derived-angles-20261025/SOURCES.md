# Sources and retained evidence

Researched 25 October 2026. [input-provenance.json](input-provenance.json) records 15 SHA-256 input receipts. [download-limitations.json](download-limitations.json) records no failed downloads in the final input preparation. Source snapshots are evidence, not new glyph masters or a permission to reuse source contours.

| Source | Purpose | Local evidence |
| --- | --- | --- |
| [Munkasey, An Astrological House Formulary, NCGR Spring 2006](https://ncgrastrology.org/wp-content/uploads/publications/geocosmic-journal-archive/2006_NCGR_Journal_Spring_2006.pdf) | Author's geometric terminology and paired/intersection table | [Publisher PDF](references/munkasey-ncgr-2006.pdf); printed p53 = [physical p54](references/munkasey-physical-p54.png); printed p61 = [physical p62](references/munkasey-physical-p62.png); printed p62 = [physical p63](references/munkasey-physical-p63.png) |
| [Kerykeion chart-glyph atlas](https://kerykeion.net/python-library/docs/v6/chart-glyphs) | Modern nonletter East Point form witness | [Page](references/kerykeion-glyphs.html), [publisher-linked atlas SVG](references/kerykeion-chart-glyphs.svg), [inspected axes crop](references/kerykeion-source-axes.png), [observed image URLs](references/kerykeion-observed-image-urls.json) |
| [Astrodienst Swiss Ephemeris general documentation](https://www.astro.com/swisseph/swisseph.htm), section 6.3 | Definition and naming witness from an implementation's own documentation | [Snapshot](references/swiss-general.html) |
| [Matrix Astro*Dictionary East entry](https://www.astrologysoftware.com/m/community/learn/dictionary/east.html) | Attributed naming distinction; research lead | [Snapshot](references/matrix-east.html) |
| [Matrix Astro*Dictionary Polar entry](https://astrologysoftware.com/community/learn/dictionary/polar.html) | Attributed terminology and ambiguity; original article takes precedence | [Snapshot](references/matrix-polar.html) |

The Munkasey article spans printed pages 51–62. Its concluding note identifies an earlier appearance in the NCGR Winter 1988–89 issue, pages 37–45. Physical page numbers above are one-based PDF positions; printed numbers are the journal's page labels. An additional physical-p53 render is retained as research material but is outside the four source images listed in the final visual review receipt.

The Kerykeion SVG URL was observed in the fetched publisher page. The rendering is a visual source witness; its exact contours were not inserted into the new masters. West Point and Polar Ascendant remain explicitly original proposals. This packet neither adopts an external font license nor makes a legal clearance claim for a future distribution.

## Local inputs

The remaining eight receipts are local project inputs: the Batch 20 brief, master inventory, 189 frozen controls, Batch 19 symbols, Batch 03 angle labels, the current geometry helper, current entry map and font manifest. Their snapshots are all in [references](references). The ninth local receipt is a read-only [native source excerpt](references/native-east-point-excerpt.txt), with original file SHA-256 and line ranges in the provenance receipt.

All three original brief records are preserved verbatim within [glyphs.json](glyphs.json). The 201 comparison records comprise 189 preceding controls, four Batch 19 symbol drawings and eight angle-label forms. This is a source-record count, not a claim about the number of unique characters in the font.

[Research interpretation](RESEARCH.md) · [Native source note](NATIVE_ALIGNMENT.md) · [Preservation](PRESERVATION.md)
