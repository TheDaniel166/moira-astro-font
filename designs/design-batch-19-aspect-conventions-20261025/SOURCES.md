# Sources and evidence

Retrieved or copied 25 October 2026. The [input receipt file](input-provenance.json) contains 20 SHA-256 receipts. External sources are research references, not a license to redistribute their drawings as font outlines. All four proposed compositions use Moira's own existing letters.

| Primary source | Inspected location and role | Retained local evidence |
|---|---|---|
| [C. J. Krap, Planet Figures](https://astrologyplanetfigures.wordpress.com/) | Telescope discussion; contemporary use of Tao at 165°. No origin claim. | [HTML snapshot](references/krap-planet-figures.html) |
| [Astro Gold macOS manual, Aspects](https://www.astrogold.io/AG-MacOS-Help/aspects.html) | Publisher's minor-aspect table explicitly labels its ordinary letter glyphs. | [HTML snapshot](references/astrogold-aspects.html) |
| [Aureas news / version 12](https://www.aureas-astrology.com/contents/en-us/d1_News.html) | New-minor-aspects list; independent angle and alias usage. | [HTML snapshot](references/aureas-news.html) |
| [Fei Cochrane, Basic Alphabet of Astrology](https://www.astrosoftware.com/Pub/Tech/FeisBlog/BasicAlphabetOfAstrology.pdf) | Physical PDF p5, table; numerical and visual convention witness. | [PDF](references/fei-basic-alphabet.pdf), [rendered p5](references/fei-p5.png) |
| [Suignard, N4811 / L2/17-020R2](https://www.unicode.org/wg2/docs/n4811-fdbk-extra-aspect-sym.pdf), 24 January 2017 | Physical p2 Table 1, checked visually by column; naming/fraction evidence and the Batch 02 correction. | [PDF](references/suignard-n4811.pdf), [p1](references/suignard-p1.png), [p2](references/suignard-p2.png) |
| [Wharton, collected works (1683), printed p92](https://books.google.com/books?id=LBroWVBBY2oC&pg=PA92) | Original printed page; historical word witness, with limits in the research notes. Adjacent pp91 and 93 inspected. | [p92 scan](references/wharton1683-p92-image), [p91 scan](references/wharton1683-PA91-image), [p93 scan](references/wharton1683-PA93-image), [viewer HTML](references/wharton-google-page.html) |

The exact observed Google page-image address is retained in [p92 retrieval provenance](references/wharton-p92-source-url.txt). [Adjacent-page retrievals](references/wharton-extra-pages.json) retain the other observed image addresses. The scan files contain the original image bytes even though their filenames lack an image extension.

## Own frozen inputs

The other receipts cover unchanged planning records, current font registry/manifest, existing glyph outlines, the geometry helper, Unicode 17 data/license and the earlier native-aspect excerpt. [Original planning records](BATCH_BRIEF.json) are preserved verbatim. [Naming decision](NAMING_DECISION.json) records the user's current Tao choice separately.

The control bank contains 144 earlier comparison drawings, nine Batch 18 drawings and 25 Batch 02 forms. Duplicated visual forms can occur in that bank; **178 is the number of preserved control records**, not a claim of 178 unique characters or font glyphs.

## Access limitations

The first urllib download of Cochrane's PDF failed certificate-chain verification. Windows `Invoke-WebRequest` then retrieved the PDF using the operating system trust store. The [original error](download-limitations.json) is retained; no TLS verification was disabled.

Unavailable Tyl pages and a redirected Wade PDF were excluded as primary evidence. Astrowiki and Wiktionary were discovery leads only; their assertions were not substituted for inspected originals. Historical publications cited by the Tao encyclopedia lead were not inspected, so this packet gives no earliest-use date or inventor.

Research findings and exclusions are also recorded in [source-observations.json](source-observations.json). Local source snapshots preserve retrieval evidence; they are not linked as executable specimen resources.
