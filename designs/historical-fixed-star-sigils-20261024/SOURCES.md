# Source register

Accessed 24 October 2026. Download URLs, local paths and SHA-256 receipts are in `source-receipts.json`.

1. **Agrippa, *De occulta philosophia libri tres*, 1533, Book II, chapter LII, printed pp. 196-197.** Primary graphic source: Library of Congress copy distributed by Internet Archive. The character plate is PDF page 213 (one-based), scan index 212. The preceding chapter context is PDF page 212. Internet Archive marks the item Public Domain Mark 1.0 and identifies its LOC source. [Item and viewer](https://archive.org/details/DeOccultaPhilosophiaLoc1533), [PDF used](https://archive.org/download/DeOccultaPhilosophiaLoc1533/2009gen12345_text.pdf), [metadata](https://archive.org/metadata/DeOccultaPhilosophiaLoc1533). The DjVu OCR helped locate the page; the diagrams were read visually, not inferred from OCR.

2. **1533 Augsburg copy, MDZ/BSB identifier bsb11193457.** Same printed edition used as a second-copy cross-check. Manifest canvas 0210 is printed p. CXCVI; canvas 0211 is printed p. CXCVII. [Catalogue](https://www.digitale-sammlungen.de/en/details/bsb11193457), [IIIF manifest](https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11193457/manifest). The manifest's scan-use terms differ from its metadata terms. MDZ scans are retained as research references; the delivered source-comparison sheets use the LOC and Wellcome material instead.

3. **Agrippa, *Three books of occult philosophy*, London: printed by R.W. for Gregory Moule, 1651, Book II, chapter LII, printed pp. 321-323.** Primary later printed comparison witness: Wellcome Collection, item b30335231. Page 321 contains Algol, Pleiades and Aldaboram; p. 322 the next seven; p. 323 the final five. Wellcome provides the work under Public Domain Mark. [Catalogue](https://wellcomecollection.org/works/ftahuupv), [IIIF manifest](https://iiif.wellcomecollection.org/presentation/b30335231). The downloaded page image URLs come from its image services. The catalogue discusses uncertainty over the translator's identity; this packet makes no new translator attribution.

4. **Bibliotheca Philosophica Virtualis, *Liber de quindecim stellis*, catalogue entry by Fabio Seller.** University-hosted scholarly finding aid for the medieval text, manuscript locations and bibliography. [Catalogue](https://www.bphv.eu/en/content/liber-de-quindecim-stellis), [linked Crawford PDF](https://www.bphv.eu/sites/default/files/digital_pdf/Liber%20de%20quindecim%20stellis%20crawford%203.pdf). The catalogue lists Edinburgh Royal Observatory Crawford 3.14. The scan's final bookplate reads “CR 3.14 (1-4)”; the download filename abbreviates this as Crawford 3. The PDF has 14 digital pages, not 14 manuscript folios. Inspected as a textual witness; no complete graphic alternate family is asserted from it.

5. **Joseph H. Peterson, digital transcription of Agrippa Book II, part 4, Esoteric Archives.** A finding aid for chapters II.47 and II.52 and their English text. [Transcription](https://www.esotericarchives.com/agrippa/agripp2d.htm). This is a modern copyrighted digital edition. Its figure files and outlines were not downloaded into, traced for, or copied into the master drawings. Original printed facsimiles supplied the graphic evidence.

## Derived reference images

`loc1533-printed-197.png` was rendered from the downloaded searchable PDF with Poppler:

```powershell
pdftoppm -f 213 -l 213 -scale-to 2400 -png -singlefile references/2009gen12345_text.pdf references/loc1533-printed-197
```

Printed p. 196 uses PDF page 212 and `-scale-to 1800`. The Crawford PDF was rendered at a 1100-pixel maximum dimension. Diagram crops are unretouched pixel extracts; their source image paths and exact rectangles are recorded per entry in `glyph-studies.json`. Crops can contain nearby ink when the original figures are closely spaced. Refer to the full pages for context.

The SVG masters are new manual structural drawings. They do not embed scans, use external font outlines, or claim exclusive authorship of historical motifs. This research packet makes no change to the font project's distribution licence.
