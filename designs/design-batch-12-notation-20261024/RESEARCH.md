# Batch 12 research — coordinate letters and notation

24 October 2026. Research supports character identities and notation choices. The fifteen drawings are original Moira source vectors, written in this packet; no third-party font outlines were extracted or traced.

## Greek identities and the phi decision

The [Unicode 17 Greek chapter, §7.2](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-7/) distinguishes ordinary Greek letters from separately encoded symbol forms. It allows Greek-block letters as mathematical variables. In technical fonts, it recommends the loopy form for U+03C6, maintaining contrast with the straight U+03D5 phi symbol. That is the basis for this packet's loopy **φ**. The six studies retain their ordinary Greek identities; Latin lookalikes and dedicated beta/phi/lunate-epsilon symbols are separate characters.

This is notation support, not a complete Greek text face: no additional Greek alphabet, accents, language shaping or polytonic coverage is claimed. The formal Unicode name for λ is **GREEK SMALL LETTER LAMDA**; “Lambda” is the familiar display label.

## Assigned characters

Exact names and scalars were checked against the frozen final [Unicode 17.0.0 character data](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt), copied into `references/UnicodeData-17.0.0.txt` with its license. The seven new raised digits complete the decimal family alongside unchanged Moira ² ³ ⁴.

| Character | Assigned identity | Context in this packet |
|---|---|---|
| λ | U+03BB GREEK SMALL LETTER LAMDA | Ecliptic longitude label |
| β | U+03B2 GREEK SMALL LETTER BETA | Ecliptic latitude label |
| δ | U+03B4 GREEK SMALL LETTER DELTA | Declination label |
| α | U+03B1 GREEK SMALL LETTER ALPHA | Right ascension label |
| φ | U+03C6 GREEK SMALL LETTER PHI | Observer latitude label; loopy letter form |
| ε | U+03B5 GREEK SMALL LETTER EPSILON | Obliquity label |
| ⁰ | U+2070 SUPERSCRIPT ZERO | Raised digit; unslashed default |
| ¹ | U+00B9 SUPERSCRIPT ONE | Raised digit; inventory omission filled here |
| ⁵ | U+2075 SUPERSCRIPT FIVE | Raised digit |
| ⁶ | U+2076 SUPERSCRIPT SIX | Raised digit |
| ⁷ | U+2077 SUPERSCRIPT SEVEN | Raised digit |
| ⁸ | U+2078 SUPERSCRIPT EIGHT | Raised digit |
| ⁹ | U+2079 SUPERSCRIPT NINE | Raised digit |
| ' | U+0027 APOSTROPHE | Literal straight single quote / apostrophe |
| " | U+0022 QUOTATION MARK | Literal straight double quote |

## Raised characters and layout

The [Unicode superscript FAQ](https://unicode.org/faq/ligature_digraph.html) explains why encoded superscripts are a limited set rather than a general layout mechanism. This batch supplies the requested assigned plain-text digits. Arbitrary expressions, nested scripts and typography on ordinary digits require a layout system; this packet does not add an OpenType `sups` feature or substitute ordinary digits globally.

The frozen character records show compatibility decompositions for raised digits. NFC preserves their identities; compatibility normalization such as NFKC can reduce them to ordinary digits. A future integration must retain the intended plain-text stream rather than normalize away the raised presentation unintentionally. `H⁰ … H⁹` is a typography stress string, not a declaration of a valid zero-th harmonic or a calculation.

## Quotes and angular units

The [Unicode 17 punctuation chapter, §§6.2.6–6.2.7](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-6/) documents the straight keyboard quotation characters and the overloaded ASCII apostrophe. These studies use vertical marks. They do not merge the ASCII characters with the already drawn slanted **PRIME U+2032** and **DOUBLE PRIME U+2033**. The latter retain the angular-unit role in the coordinate specimens. Curly quotation characters remain outside this batch.

## Coordinate examples and scope of evidence

[NASA LAMBDA's coordinate-entry documentation](https://lambda.gsfc.nasa.gov/data/interfaces/iras/coordinates.html) supports right ascension in hours, declination in degrees, and ecliptic longitude/latitude in degrees, with sexagesimal or decimal input. It is an application-specific guide; its epoch/obliquity assumptions are not adopted here.

The Greek-to-label associations above are the explicit Moira specimen convention, not claims that a scalar universally fixes a meaning. Every value is invented for typography review. The letters select neither a coordinate frame nor apparent/mean quantities, epoch, equinox, geocentric/topocentric origin or geodetic/geocentric latitude. Real product labels must supply those distinctions where relevant.

## Design method and evidence boundary

The source style follows Moira's own rounded monoline strokes: 60 source units for Greek and quotes; 58 for raised digits. New digits use the existing 300-unit source advance. Own earlier Latin letters, numerals, units and ² ³ ⁴ are frozen comparison controls. The registry records their source snapshots and exact drawing hashes.

Each proposal has a standalone editable SVG and appears at 14/18/24/32 px em in both themes. Context proofs use the original vector geometry, not substitute system-font glyphs. Interface titles and annotations use system text. The preview applies the existing 1.08 scale in a 1,000-unit em; browser SVG captures do not certify later font rasterization or hinting.
