# Batch 13 research: core-body alternate characters

24 October 2026. Seven design studies for visual review, following the existing master inventory. This packet changes no default, existing outline or font binary.

## Identity and form evidence

The final [Unicode 17 Miscellaneous Symbols chart](https://www.unicode.org/Public/17.0.0/charts/PDF/U2600.pdf), [Miscellaneous Symbols and Arrows chart](https://www.unicode.org/Public/17.0.0/charts/PDF/U2B00.pdf), character data and NamesList establish the seven assigned identities below. The charts' reference shapes guide recognition; they do not prescribe a font's exact contours. The final data are frozen here with the existing Unicode license.

| Character | Final identity | Moira construction selected for review |
|---|---|---|
| ☀ | U+2600 BLACK SUN WITH RAYS | Solid disc and eight separated rays |
| ☽ | U+263D FIRST QUARTER MOON | Right-hand filled crescent, opening left; mirror of Moira's existing Moon geometry |
| ⛢ | U+26E2 ASTRONOMICAL SYMBOL FOR URANUS | Circled central point and upright arrow |
| ⯓ | U+2BD3 PLUTO FORM TWO | Orb over open cup, stem and lower cross |
| ⯔ | U+2BD4 PLUTO FORM THREE | Double arched head, cross and lower ring |
| ⯕ | U+2BD5 PLUTO FORM FOUR | Orb over outlined upward crescent bowl |
| ⯖ | U+2BD6 PLUTO FORM FIVE | Unfilled circle with bowed inner division |

## Uranus

[L2/09-300, Proposal to Encode the Astronomical Symbol for Uranus](https://www.unicode.org/L2/L2009/09300-uranus.pdf), pp. 3-6, documents contrastive use of the astronomical and H-based forms. Page 5, Figure 4 supplies a clear circle/dot/upward-arrow reference. This supports retaining U+26E2 separately from U+2645. The proposal's 2009 description of an encoding gap is historical; the final version 17 assignment governs this packet.

[NASA's Solar System Symbols](https://science.nasa.gov/resource/solar-system-symbols/) also describes the Uranus construction as a combination of Sun and Mars devices. Its Moon crescent and Pluto monogram descriptions provide context for the existing defaults, not a ranking of all astrological alternatives. NASA's text is not used as authority for the ray Sun or the four Pluto alternates.

## Pluto

[David Faulks, Astrological Plutos, L2/16-067R](https://www.unicode.org/L2/L2016/16067r-astrological-plutos.pdf), p. 1 and pp. 8-15, provides visual evidence for all four forms and their variation in chart/text use. We inspected the rendered pages rather than trusting extracted symbol text, which loses shapes in this PDF. The selected constructions follow the final chart's recognisable forms; the proposal's other head, ring and orientation variants remain references.

The proposal associates form four with Hamburg/Uranian practice and attributes it to Hermann Lefeldt in 1946. That attribution is recorded as the proposal's account, not independently verified here. Regional popularity and possible orbital symbolism are not treated as established facts or universal design rules.

The revised proposal lists draft positions **2BD4-2BD7**. The final assignments are **2BD3-2BD6**. The latter, not the proposal's positions, are recorded in every new master and registry entry. Form five stays an outlined Pluto character; its two unfilled fields are not a Moon phase or a physical orbital diagram.

## Sun and Moon

The ray Sun follows **BLACK SUN WITH RAYS U+2600**: a solid disc, not the circled central point already used for Sun U+2609. Its eight rays are a design convention, not physical modelling. The final Unicode 17 emoji variation data register **U+2600 FE0E** for text presentation. This packet records that sequence for later integration; it implements no cmap/variation table.

The opposite crescent follows **U+263D FIRST QUARTER MOON** and retains that exact identity. The default is **U+263E LAST QUARTER MOON**. A product may offer either as a generic Moon-body icon, but must not globally substitute one character for the other in phase text. The separate lunar-phase characters and Batch 10 designs are untouched. The Moira drawing mirrors its own accepted filled crescent, keeping the established weight and silhouette.

## Original artwork and review method

Six new geometric constructions were authored in source coordinates. The seventh study mirrors original Moira artwork; the source remains unchanged. No external font paths were extracted or traced. Reference PDFs and their rendered pages are local research material; only the original Moira masters are candidate glyph assets for a later font build.

All seven proposals use the existing rounded family and 60-unit source stroke. The ray Sun has a solid disc with separated round-ended rays. Pluto two opens the orb/cup gap; three keeps the lower ring; four retains a white crescent interior; five keeps both internal fields unfilled. The new Sun disc uses a closed cubic path after the browser review exposed faint raster seams in its initial circle primitive.

Specimens use 1,000-unit em coordinates and the existing 1.08 preview scale, with light and inverse proofs at 14/18/24/32 px em. Body controls retain their own original 1,000-unit source cell. Those cells are not claims about final font advances or kerning. Larger context proofs use invented values, and all four Pluto rows deliberately use the same value.

These are source-vector studies. Their pixel checks do not certify TTF/WOFF2 shaping, hinting or platform rasterization. No PUA, feature slot or token is allocated, and no existing character is remapped.
