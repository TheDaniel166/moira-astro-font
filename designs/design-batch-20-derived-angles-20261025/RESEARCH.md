# Batch 20 research

25 October 2026 · Source-qualified notation studies

## The naming problem

The inventory's East Point label needs a geometric qualifier. The adopted identity is **equatorial Ascendant**: an ecliptic direction with right ascension ARMC + 90°, in a declared frame and equinox, with the intended branch retained. It is the zero-latitude Ascendant convention. A 90° separation in right ascension does not generally produce a 90° separation in ecliptic longitude. The due-east horizon direction is a separate spatial point; the shared name is insufficient to identify a calculation. [Astrodienst, section 6.3](https://www.astro.com/swisseph/swisseph.htm).

Michael P. Munkasey's original *An Astrological House Formulary* distinguishes the equatorial Ascendant name from East Point and pairs Equatorial ASC with Equatorial DES. Its construction table assigns Polar ASC to the co-polar axis circle and the western intersection; this packet therefore retains a **Munkasey-qualified** Polar Ascendant identity. The article also distinguishes the polar-axis and co-polar-axis constructions. Printed pages 53 and 61–62 are the relevant evidence. [Author article in the NCGR archive](https://ncgrastrology.org/wp-content/uploads/publications/geocosmic-journal-archive/2006_NCGR_Journal_Spring_2006.pdf).

The Matrix dictionary's attributed entries were research leads. Its polar entry combines descriptions whose axis terminology can be read ambiguously. The original author article governs the qualified identity here; the dictionary is not substituted for it. [East entry](https://www.astrologysoftware.com/m/community/learn/dictionary/east.html), [Polar entry](https://astrologysoftware.com/community/learn/dictionary/polar.html).

## Selected identities

| Semantic ID | Selected notation identity | Metadata required with calculated use |
| --- | --- | --- |
| `point.east-point` | Equatorial Ascendant, ecliptic direction at RA = ARMC + 90° | Definition ID, frame, equinox/epoch and branch convention |
| `point.west-point` | Equatorial Descendant, selected EP + 180° modulo 360° | Same definition/frame/branch policy as its EP partner |
| `point.polar-ascendant` | Munkasey's co-polar axis circle, selected western ecliptic intersection | Qualified definition ID, frame, equinox/epoch and branch convention |

The western Polar Ascendant branch is a definition choice, not the page-right location of the dot in the drawing. Polar Ascendant is not the north celestial pole, north ecliptic pole, ordinary Ascendant, Vertex, or an Ascendant calculated at a geographic pole. Astrodienst separately describes a Polar Ascendant relationship to the **Koch** co-Ascendant; that is an implementation witness and does not make every use of “co-Ascendant” interchangeable. [Astrodienst, section 6.3](https://www.astro.com/swisseph/swisseph.htm).

## What the form research established

Kerykeion's own chart-glyph atlas supplies a directly observable modern East Point mark: a circled cross with a split arm. We inspected the publisher-linked source image, rather than inferring a symbol from a text abbreviation. Moira's master uses independently constructed coordinates, round terminals and its own proportions. This establishes a modern form precedent, not historical antiquity or universal usage. [Kerykeion chart-glyph atlas](https://kerykeion.net/python-library/docs/v6/chart-glyphs).

An independently established primary nonletter form for West Point or Polar Ascendant was not verified in the inspected sources. That is a bounded research result, not a claim that none exists. West Point is an original Moira half-turn partner of the new EP drawing. Polar Ascendant is an original open-loop crossing with a selected knot. Neither is presented as a reproduced historical sigil.

The diagrams are schematic notation. They do not encode obliquity, geographic latitude or a chart's actual sky orientation. Font artwork cannot select an engine model. The source-level native East Point difference is recorded separately in [NATIVE_ALIGNMENT.md](NATIVE_ALIGNMENT.md); no native calculation was executed or changed.

[Source snapshots and page references](SOURCES.md) · [Design decisions](DECISIONS.md) · [Symbol records](glyphs.json)
