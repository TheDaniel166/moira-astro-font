# Batch 18 research

25 October 2026 - astronomical reference meanings, notation evidence and nine original design studies

## Galactic and supergalactic references

[Gordon, de Witt and Jacobs, 2022](https://arxiv.org/abs/2212.00632), report VLBI astrometry for Sgr A* in ICRF3 and state a proper-motion reference epoch. This supports a catalog-qualified reference, rather than freezing a tropical longitude into the glyph. A GC label must distinguish the intended center definition or catalog proxy and retain its frame and epoch. The source paper is not a glyph specification.

The [2016 Faulks proposal](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf), physical PDF p.32, Sample 7.04 in the section about Lilith/Priapus, reproduces an Astrology Weekly glyph table. A spiral-like mark is visibly labelled Galactic Center. It is incidental evidence in an image; its name is absent from the extracted PDF text. This is a witness to usage, not a proposed/accepted Galactic Center character assignment. The original webpage was not independently verified through this reproduction. Moira's open spiral is drawn from new coordinates, without tracing that small image or copying font contours.

[Philip Sedgwick's authored page](https://www.philipsedgwick.com/Galactic/ZS.htm) identifies his astrological Super Galactic Center usage with M87 / NGC 4486. Only that identification informs this packet. Its physical narratives, interpretive claims and numerical positions are not adopted. The page's article-copy restriction is respected: the packet retains a short observation in our own words and the link, not a copy of the article.

[IVOA's reference-frame vocabulary](https://www.ivoa.net/rdf/refframe/2022-02-22/refframe.html) specifies the SUPER_GALACTIC axes through a pole and a zero-longitude direction. That is a coordinate-frame definition. **Our distinction** is to keep that definition separate from an astrological M87 reference. Neither the frame name nor an unqualified SGC label resolves which point a chart means. The original inventory's generic supergalactic-reference entry therefore remains generic: **SGref** is the proposed companion, with **SGref / M87** shown only as a qualified example. No automatic M87 selection, fixed degree, new Great Attractor identity or extra supergalactic pole is introduced.

## Four pole directions

The [IAU OAE Celestial Pole entry](https://www.astro4edu.org/resources/glossary/term/52/r217/) gives the introductory north/south meanings and declinations. The [IAU NFA glossary](https://syrte.obspm.fr/iau/iauWGnfa/NFA_Glossary.html) supplies the technical distinction between a declared equatorial pole, the CIP and other reference concepts. It defines the ecliptic through the Earth-Moon barycenter's mean orbital angular momentum, and distinguishes a fixed ecliptic from a time-dependent choice. The [IAU Commission A3 resolution text](https://iau-a3.gitlab.io/res.html), 2006 B1 item 4, gives the adopted pole-definition requirement.

The drawings use a plane bar with a normal stem and a solid selected endpoint. Celestial bars are horizontal; ecliptic bars are sloped. North and south are exact 180-degree counterpart constructions. The slope is a graphic family cue, not Earth's obliquity, a projected sky geometry, a zodiac frame or a calculation method. NCP/SCP and NEP/SEP identify the poles of the declared plane; the font does not select the epoch, mean/true/intermediate definition or ephemeris. A celestial pole is not the star Polaris.

These inspected sources use names, abbreviations and technical notation. They do not establish this four-pictogram family. Its drawings are explicitly Moira-original; this is not a claim that no other pole notation exists.

## Three coordinate origins

[IVOA's reference-position vocabulary](https://www.ivoa.net/rdf/refposition/2019-03-15/refposition.html) distinguishes geocenter, heliocenter, solar-system barycenter and Earth-Moon barycenter. Its BARYCENTER term specifically names the solar-system barycenter; the more general Moira barycentric inventory concept still needs a named system. The [NAIF identity list](https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/naif_ids.html) makes the separate origin identities concrete: Earth 399, Sun 10, SSB 0, EMB 3. These are research/example identifiers, not character allocations or engine configuration.

The origin family adds a common pair of open corner brackets around a circle-cross Earth motif, circle-dot Sun motif, or original three-spoke barycenter hub. This distinguishes annotation from the existing body glyphs. The bracket convention and hub are Moira-original; the Earth/Sun component motifs are established and already present in the project. The construction does not assign axes, aberration corrections, a time scale or a reference epoch. The hub's lengths and dots do not calculate masses or locate a physical barycenter.

## Labels and character access

GC, NCP and the other uppercase pole companions follow familiar source terminology; SGref and the Geo/Hel/Bar companions are proposed product labels. All compose unchanged Latin outlines and preserve full-name fallbacks. The short labels are not new ligatures or semantic substitutes for the original records. They are scoped chart labels, not a globally collision-free abbreviation registry: NEP can resemble a planet abbreviation in another context, SEP a month, and Bar a text word. Keep the full name, family heading or legend when needed.

The pinned Unicode 17 data names the existing Sun, Earth, circled-S and Fortune characters. A drawing resembling a geometric character is not enough to allocate a new astronomical meaning to it. This packet assigns no Unicode, PUA, variation selector, token or OpenType feature. The source inventory's unresolved mappings, text-first defaults and P4 priorities remain verbatim in [the brief](BATCH_BRIEF.json).

## Review finding

An initial double-whorl GC study resembled a solar circle at small sizes. The final proposal uses a single open spiral, with the Sun and zero shown as controls. The pole endpoint and origin-corner details become subtle at 14 px; retain readable companions while readers learn the shapes. The source-vector proofs are not a claim of universal recognition or a font rasterizer certification.

[Sources and access limitations](SOURCES.md) · [Design decisions](DECISIONS.md) · [Final proof](chart-size-proof-light.html)
