# Sources and limitations

25 October 2026. [Frozen input receipts](input-provenance.json) retain source hashes. Meaning evidence, notation witnesses and new artwork are distinct.

| Source | Inspected location | Role and limit |
|---|---|---|
| [Gordon, de Witt and Jacobs (2022)](https://arxiv.org/abs/2212.00632) | Abstract; saved authored HTML | Sgr A* astrometry with frame/reference epoch. No coordinates are implemented or etched into a symbol. |
| [Faulks (2016), Additional Symbols for Astrology](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf) | Physical PDF p.32, Sample 7.04; rendered and visually inspected | The reproduced Astrology Weekly table visibly labels a spiral-like GC mark. This is incidental image evidence, not a GC encoding proposal. It does not attest the other eight proposals. Original webpage not independently verified. |
| [Sedgwick, The Super Galactic Center](https://www.philipsedgwick.com/Galactic/ZS.htm) | Opening identity list | Primary evidence of the author's M87/NGC 4486 usage. Only an original short observation is retained; the article itself is not copied. Its scientific/interpretive narratives and tabulated positions are outside the adopted evidence. |
| [IVOA Reference Frames, 2022 vocabulary](https://www.ivoa.net/rdf/refframe/2022-02-22/refframe.html) | SUPER_GALACTIC entry | Formal frame, pole and longitude-origin definition. This is not an M87 point definition or a glyph standard. |
| [IAU OAE Celestial Pole](https://www.astro4edu.org/resources/glossary/term/52/r217/) | Description and NCP redirect | Introductory pole definitions. IAU OAE attribution retained; CC BY 4.0 text license noted in source. No diagram traced. |
| [IAU NFA glossary](https://syrte.obspm.fr/iau/iauWGnfa/NFA_Glossary.html) | CIP, ecliptic, fixed ecliptic, epoch and geocentric entries; revision 20 Nov 2007 | Technical meaning evidence. HTML has legacy character-decoding artifacts; no glyph absence conclusion is based on that encoding. |
| [IAU Commission A3 resolution text](https://iau-a3.gitlab.io/res.html) | 2006 B1, item 4 | Adopted ecliptic pole-definition text in the responsible commission's presentation. Used after the archive PDF returned 502. |
| [IVOA Reference Positions, 2019 vocabulary](https://www.ivoa.net/rdf/refposition/2019-03-15/refposition.html) | GEOCENTER, HELIOCENTER, BARYCENTER, EMBARYCENTER | Origin distinctions. BARYCENTER in this vocabulary means SSB; generic Bar still needs a named system. Saved HTML was available although a web-tool direct open failed. |
| [NAIF Integer ID codes](https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/naif_ids.html) | Barycenters and Planets/Satellites tables | Separate Earth, Sun, SSB and EMB identities. IDs here are explanatory data, not font character codes. |
| [Original master](references/master-inventory.json) | All nine complete records | Original meanings, priorities, mappings, fallbacks and holds retained verbatim. |
| [Previous controls](references/old-controls.json), [Batch 17](references/batch17-glyphs.json), [Fortune](references/batch03-points.json), [Spirit revision](references/spirit-revision.json) | 144 distinct source drawings/advances | Own unchanged comparison controls. No claim that every retained control appears on a sheet. These source studies are not current compiled-font metrics. |
| [Unicode 17 data](references/UnicodeData-17.0.0.txt), [license](references/UNICODE-LICENSE.txt) | Pinned character names | Used for reference only. No new assignment is made; common component shapes may already have geometric encodings. |

The direct ESO archive PDF for IAU 2006 B1 returned HTTP 502 and was not saved. Its text is supported by the NFA glossary and the Commission A3 page. [Download limitations](download-limitations.json) records that attempt. USNO and the Starlink site also had web-tool access failures; neither supplies required proof for these proposals. A live Glyph Glossary page listed GC but its image fetch was unavailable; no image-form claim rests on that page.

The generic current Unicode chart URL returned a chart labelled Version 18.0 during research. It was not adopted: this project still uses its frozen Unicode 17 names/data. The 2016 proposal's old candidate codepoints are not treated as current allocations.

No third-party font files, contours or page artwork were used as design assets. Frozen reference pages/PDF are retained for this internal research packet, with their attribution and restrictions. They are not a blanket grant to redistribute third-party content in a public font release.
