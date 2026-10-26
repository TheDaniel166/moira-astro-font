# Sources and research limits

26 October 2026 · Author/publisher sources · Original Moira coordinates

The source files are frozen with URL, role and SHA-256 in [input provenance](input-provenance.json). An observed form is evidence of that author's convention; it does not establish a universal meaning or select a calculation. No external font binary or outline was imported.

| Source | Use and inspected evidence | Frozen copy |
| --- | --- | --- |
| [David Faulks, L2/16-080, 15 April 2016](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf) | Documentary samples for Proserpina, Black/White Moon, Priapus and Arta. Physical pages 6, 22, 23, 29, 30 and 31 inspected. Proposed allocations are obsolete. | [PDF](references/faulks-16080.pdf) |
| [Unicode 17.0 U2B00 chart](https://www.unicode.org/charts/PDF/Unicode-17.0/U170-2B00.pdf) | Assigned reference forms; physical page 2 inspected. | [Pinned PDF](references/unicode17-U2B00.pdf) |
| [Unicode current U2B00 chart](https://www.unicode.org/charts/PDF/U2B00.pdf), [current U2600 chart](https://www.unicode.org/charts/PDF/U2600.pdf) | Both downloaded charts identify version 18.0; physical page 2 of each inspected. Current URLs are moving references, not our character-data authority. | [U2B00 PDF](references/unicode-U2B00.pdf), [U2600 PDF](references/unicode-U2600.pdf) |
| Unicode 17.0 character data from the existing font packet | Exact names for U+2BD8 PROSERPINA, U+2BDD WHITE MOON SELENA, U+2BDF TRUE LIGHT MOON ARTA and U+26CE OPHIUCHUS checked programmatically. All remain unallocated in these proposals. | [Data](references/UnicodeData-17.0.0.txt) |
| [Jan Kampherbeek, Enigma Astrology 2 manual, 20 December 2024](https://radixpro.com/dl/EnigmaAstrology2_en.pdf) | Author-published lunar and Vulcan form witnesses; physical pages 8 and 9 inspected. Distinguishes intramercurial forms from Hamburg Vulkanus and Carteret Vulcan. | [PDF](references/enigma-manual.pdf) |
| [Albert Timashev, Light Moon article](https://astrologer.ru/book/light_moon/index.html.en), [history](https://astrologer.ru/book/light_moon/history.html.en) | Original author's definitions and discussion of competing constructions and phase/branch ambiguity. Text consulted; no formula implemented. | [Article](references/timashev-index.html), [history](references/timashev-history.html) |
| [Astrodienst, Swiss Ephemeris general documentation](https://www.astro.com/swisseph/swisseph.htm) | Sections 2.2.1–2.2.4 and 2.7.5–2.7.7: one implementation witness for apsides, Vulcan, Selena and Waldemath. Its calculations are not adopted as authority. | [Snapshot](references/swiss-general.html) |
| [Astrolog author Vulcan note](https://www.astrolog.org/ftp/updat600.htm) | Additional author-owned evidence of a distinct Vulcan element convention. | [Snapshot](references/astrolog-vulcan.html) |
| [NASA constellation terminology](https://spaceplace.nasa.gov/constellations/en/) | Terminology only; does not establish a thirteen-sign scheme. | [Snapshot](references/nasa-constellations.html) |

Additional leads are retained for traceability: [Faulks's Vulcan mailing-list discussion](https://www.unicode.org/mail-arch/unicode-ml/y2016-m02/0026.html) and [Kerykeion's own glyph atlas](https://kerykeion.net/python-library/docs/v6/chart-glyphs). The linked atlas SVG was fetched but not visually inspected for this review, and supplies no contours to our drawings.

## Inspected source pages

- Faulks: [6](references/faulks-16080-physical-p6.png), [22](references/faulks-16080-physical-p22.png), [23](references/faulks-16080-physical-p23.png), [29](references/faulks-16080-physical-p29.png), [30](references/faulks-16080-physical-p30.png), [31](references/faulks-16080-physical-p31.png).
- Unicode: [17.0 U2B00 page 2](references/unicode17-U2B00-physical-p2.png), [current U2B00 page 2](references/unicode-U2B00-physical-p2.png), [current U2600 page 2](references/unicode-U2600-physical-p2.png).
- Enigma: [8](references/enigma-manual-physical-p8.png), [9](references/enigma-manual-physical-p9.png).

Eleven source-page images were inspected. Other rendered pages are research aids and are not counted as visual-review evidence.

## Limits

The attempted pinned Unicode 17.0 U2600 PDF returned HTTP 404. Its character identity is checked against the frozen 17.0 data; the current chart supplies the visual reference. Timashev's bilingual/legacy-encoded pages are not fully translated here; the formula is also visible in the Faulks documentary sample. The original Waldemath 1898 report was not retrieved. No unique nonletter Waldemath form was verified in the inspected sources; our emblem is expressly invented. This is a bounded review, not a claim that no other symbol exists.

[Access record](research-access.json) · [Findings](RESEARCH.md) · [Design decisions](DECISIONS.md).
