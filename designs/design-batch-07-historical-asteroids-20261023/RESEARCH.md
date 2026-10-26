# Historical asteroid research and meanings

23 October 2026

Each row identifies a physical numbered asteroid. The form column describes the symbol structure used for the new Moira drawing, not an interpretation of the body. The first 17 assignments are final in [Unicode 17 Miscellaneous Symbols Supplement](https://www.unicode.org/charts/PDF/Unicode-17.0/U170-1CEC0.pdf); the last two are separately assigned historical alternatives in [Alchemical Symbols](https://www.unicode.org/charts/PDF/Unicode-17.0/U170-1F700.pdf).

| Body identity | Character | Form structure | Historical evidence figures |
|---|---|---|---|
| (6) Hebe | U+1CEC0 | Cup and cross | 19, 20, 26 |
| (7) Iris | U+1CEC1 | Rainbow and interior star | 26, 44 |
| (8) Flora | U+1CEC2 | Flower and cross | 26, 45 |
| (9) Metis | U+1CEC3 | Eye and star | 26, 28 |
| (11) Parthenope | U+1CEC4 | Fish and star | 26, 27, 36 |
| (12) Victoria | U+1CEC5 | Laurel and star | 27, 46 |
| (13) Egeria | U+1CEC6 | Buckler and star | 26, 36 |
| (14) Irene | U+1CEC7 | Dove, branch and star | 35, 36 |
| (15) Eunomia | U+1CEC8 | Heart and star | 26, 47 |
| (16) Psyche | U+1CEC9 | Wing and star | 26, 36 |
| (17) Thetis | U+1CECA | Dolphin and lower star | 21, 26, 48 |
| (18) Melpomene | U+1CECB | Dagger and star | 26 |
| (19) Fortuna | U+1CECC | Wheel and star | 26 |
| (26) Proserpina | U+1CECD | Pomegranate and interior star | 22, 49 |
| (28) Bellona | U+1CECE | Lance and scourge | 23, 49 |
| (29) Amphitrite | U+1CECF | Shell and star | 36 |
| (35) Leukothea | U+1CED0 | Ancient lighthouse | 24, 50 |
| (4) Vesta | U+1F777 | Historical hearth | 14, 15, 26 |
| (11) Parthenope | U+1F77A | Historical lyre | 29, 34, 36 |

Figure numbers refer to [Bala and Miller (2023)](https://www.unicode.org/L2/L2023/23207-historical-asteroids.pdf), which reproduces source publications. Hind's 1852 table is Figure 26; the discovery-era announcements for Thetis, Proserpina, Bellona and Leukothea are Figures 21–24. Those reproductions were visually inspected alongside the final Unicode chart.

## Identity and mapping boundaries

- Fortuna (19) uses U+1CECC. The Lot of Fortune uses U+1F774 and remains a separate concept.
- Proserpina (26) uses U+1CECD ASTRONOMICAL SYMBOL FOR ASTEROID PROSERPINA. U+2BD8 PROSERPINA identifies a hypothetical point, not this asteroid.
- Metis (9) is the numbered asteroid, not the similarly named Jovian satellite.
- Hebe and Flora retain their dedicated characters; wine-glass or flower emoji are not aliases.
- U+1F777 and U+1F77A are separate characters. Future stylistic-set convenience must preserve explicit access to them.

## Historical scope

The remaining dedicated historical assignments in the current master inventory are covered here. The earlier Ceres, Pallas, Juno and Vesta defaults and historical Astraea/Hygiea alternatives remain intact. The historical proposal also discusses generic anchor/cross signs for Massalia (20) and Fides (37); these are outside the current inventory batch and receive no new glyph or identity remapping here. This packet does not assert that every historical variant has been drawn.

The final assignments come from Unicode 17, rather than treating proposed code positions or private-use examples in older publications as final encoding. In particular, form identity is checked against the final chart, not against historical font implementation errors.

## Independent body identity evidence

Eighteen serial JPL SBDB responses confirm number/name identities, with orbit output suppressed. The current SBDB SPK IDs and the master inventory's native catalog IDs are stored in distinct fields. Their differing ID conventions are not migrated, conflated or treated as evidence of kernel coverage. The font design makes no ephemeris/model changes.

[Form registry with exact Unicode names](glyphs.json) · [Pinned UCD records](references/unicode17-records.json) · [JPL snapshots](references/jpl-identities.json) · [Source bibliography](SOURCES.md)
