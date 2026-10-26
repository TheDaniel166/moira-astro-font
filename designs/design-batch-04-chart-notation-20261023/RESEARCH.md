# Chart-notation research and design rationale

Accessed 23 October 2026. Character identities remain pinned to Unicode 17.0.0 to match the master inventory.

## Scope selection

The existing [release plan](../moira-astro-character-inventory-20261023/RELEASE_PLAN.md) lists 27 P1 numeral/punctuation/spacing characters separately from Latin support. This batch addresses that bounded set so complete angular labels and tables can be reviewed. The [frozen inventory records](references/planned-notation.json) preserve the source registry hash. No P2 body or model is admitted by this typography work.

## Units and decimal notation

The BIPM's [current SI Brochure landing page](https://www.bipm.org/en/publications/si-brochure) supplies the 2026 English text, version 4.01. Its [sections 5.4.3-5.4.4, printed pages 144-145](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0#page=34) identify degree, minute and second as angular unit symbols that directly follow their numerical values. The document allows sexagesimal forms in astronomy and permits a decimal point or comma according to context. Section 5.4.7 addresses spacing before percent.

Accordingly, these drawings keep the degree ring and primes raised and leave spacing, decimal convention and precision in the source text. The decimal comma comparison illustrates a separate literal string; it does not reformat existing Moira output. Colon examples supply ordinary notation, without treating a clock-style separator as an angular unit or choosing a timescale.

## Character identities

The pinned [UnicodeData](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt) and [NamesList](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt) distinguish PRIME / DOUBLE PRIME from quotation characters, and MINUS SIGN from HYPHEN-MINUS. The [retained character records](references/unicode17-records.json) include formal names, categories, decomposition fields and the original data file's hash.

The resulting choices preserve U+00B0, U+2032, U+2033, U+2212 and U+002D as their actual characters. There is no replacement of typed ASCII quotes or hyphens. The slashed zero is an alternate outline of U+0030, not a new Unicode value. No OpenType feature is assigned here.

## Spacing

Unicode [Chapter 23, section 23.2.1](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/) specifies the ordinary-space width for NO-BREAK SPACE and describes the line-break distinction. [Chapter 6, section 6.2.3](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-6/) describes NARROW NO-BREAK SPACE as a narrower counterpart.

The unchanged alpha font's source specifies a 300-unit ordinary space. This packet proposes the same 300 units for NBSP and 180 for NNBSP. These are blank advances; guides in the proof matrix are separate annotations. The font supplies metrics, while a text-layout system applies breaking behavior. The vector compositor demonstrates width only and does not validate line breaking.

## Original design choices

Lining numerals use a common 680-unit advance to align repeated decimal and angular fields. This is a Moira chart-typography proposal, not a historical astrological requirement. Round terminals and a 60-unit source stroke continue the existing family; denser percent/primes use 54 units. A flagged, footed 1 distinguishes it from the earlier barred I. Zero stays unslashed by default, with a slashed study for review.

Coordinates are authored here. The slash, existing letters, zodiac controls and Spirit outlines are retained exactly from frozen Moira sources. No third-party font outline is extracted, traced or imported. Context advances and baseline placement remain provisional, and the vector placement of FE0E-qualified signs is explicitly not a shaping implementation.

## Spirit acceptance

The source-backed Spirit conventions were researched in [Batch 03](../moira-astro-design-batch-03-points-labels-20261023/RESEARCH.md). This task records the owner's explicit choice of circled S and circled vertical bar in [DECISIONS.md](DECISIONS.md), preserving the previous source-model and semantic distinctions.

All web sources were read through the research reader. Full local HTML/PDF copies are not claimed; no font or glyph contours from those documents enter the drawing generator.

## Metadata source IDs

| ID | Evidence role |
|---|---|
| `inventory` | Frozen master inventory entries: meanings, priorities and proposed scope |
| `unicode17` | Pinned UnicodeData/NamesList and the cited core chapters: assigned identities and spacing semantics |
| `bipm2026` | SI Brochure version 4.01, sections 5.4.3, 5.4.4 and 5.4.7: angular, decimal and percent notation |
