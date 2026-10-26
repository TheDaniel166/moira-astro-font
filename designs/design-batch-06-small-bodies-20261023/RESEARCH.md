# Small-body symbol research

23 October 2026. The repertoire remains pinned to Unicode 17.0.0 to match the master inventory.

## 1. Identity before form

The [master inventory snapshot](references/planned-small-bodies.json) supplies semantic IDs and physical minor-planet numbers. Independent [NASA/JPL identity snapshots](references/jpl-identities.json) confirm the ten name/number pairs using the [SBDB API](https://ssd-api.jpl.nasa.gov/doc/sbdb.html), with orbit output suppressed. These requests establish identity, not glyph authority or engine/kernel availability.

The live API returns eight-digit SPK IDs that differ from the older `native_catalog_naif_id` fields retained in the planning inventory. Metadata keeps those fields separate. This font task does not investigate or migrate engine catalogs, and a symbol choice cannot select an SPK ID or ephemeris.

Final character names come from the [pinned UnicodeData](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt), retained as [selected records](references/unicode17-records.json) with the original file hash. The final charts were inspected visually, including the [archived Alchemical Symbols chart](https://www.unicode.org/charts/PDF/Unicode-17.0/U170-1F700.pdf#page=5). Proposal-era positions and private-use examples are not used as mappings.

## 2. Astraea and Hygiea: preserve competing conventions

Faulks's [2016 study, section 5](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf#page=13) documents the modern astrological forms. Bala and Miller's [2023 proposal, pages 5-7](https://www.unicode.org/L2/L2023/23207-historical-asteroids.pdf#page=5) distinguishes those forms from historical astronomical symbols and reproduces source examples.

The default Astraea study uses the U+2BD9 percent-derived construction with ring terminals and caps; it is not an ASCII-percent substitution. Its historical U+1F778 alternative is an inverted anchor. The default Hygiea study uses U+2BDA's staff and loops; U+1F779 retains the historical serpent and star. The latter is not the staff-of-Asclepius character.

The proposals' usage and authorship opinions are not treated as independent historical collation. The uncertain inventor attribution for the modern Astraea/Hygiea forms is left unresolved. Both conventions are reviewable without changing the numbered bodies.

## 3. Nessus: continue the centaur family

Faulks's [2016 centaur discussion, section 6](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf#page=19) documents the usual Nessus form and attributes it to Robert von Heeren, while acknowledging other variants. The final U+2BDC reference form has an N-like head above an oval. Moira's new outline keeps that structure and uses the established round-terminal family treatment. The unchanged Chiron and Pholus controls make the K/P/N distinctions visible.

No alternate Nessus convention is invented or admitted here, and the proposal's claims about relative popularity are not adopted.

## 4. Eris and Sedna

Faulks's [Eris/Sedna proposal, section 3](https://www.unicode.org/L2/L2016/16173-eris-sedna.pdf#page=3) documents the Hand of Eris, the circle/down-arrow form attributed to Henry Seltzer, and the Sedna form. Its tentative codepoints differ from the final UCD.

The proposed Eris default is U+2BF0 ERIS FORM ONE, with opposed curves and a central staff. U+2BF1 ERIS FORM TWO remains an alternative for the same body. The latter's arrow stays downward; an open arrowhead is a Moira outline treatment.

Sedna retains U+2BF2's upper loop/crossbar and curved descending leg. Its modern symbol concept is attributed to Denis Moskowitz. The packet preserves the creator's provenance explanation without claiming to validate a language tradition independently.

## 5. Haumea, Makemake, Gonggong, Quaoar and Orcus

Miller's [2021 encoding request](https://www.unicode.org/L2/L2021/21224-dwarf-planet-syms.pdf) documents use of the five forms. The final chart supplies their U+1F77B-U+1F77F assignments. The proposal title and chart heading do not make every object in this packet an IAU-designated dwarf planet; the specimens use numbered physical identities.

The [Unicode Consortium's account](https://blog.unicode.org/2022/05/out-of-this-world-new-astronomy-symbols.html) credits Denis Moskowitz, with John T. Whelan collaborating on Makemake. Its form descriptions support the ring/arch Haumea, curled face-like Makemake, crossbar/serpentine Gonggong, angular-Q/canoe Quaoar, and enclosed O/R Orcus structures used here. These are modern symbol concepts; Moira authors its own outline coordinates and records the attribution.

Moskowitz's [own page](https://www.suberic.net/~dmm/astro/tno.html) offers his symbols to the public domain and asks that others not claim their invention. That statement is recorded for these attributed concepts; it is not presented as a license declaration for every source document, every other symbol, or the Moira font itself.

## 6. Design and evidence limits

The new drawings use 60-unit strokes for open forms and 54/56-unit optical strokes for denser constructions, all at the established 1.08 preview scale. Quaoar's narrow tail counter was widened during review. Permanent body numbers accompany the gallery and context rows. A glyph is never the sole stored identity of a physical body.

The small-size matrices expose Hygiea's stacked counters, Makemake's curls, Gonggong's joins and Quaoar's tail at 14/18/24/32 px. Those are source-vector studies; they do not establish final font rasterization or hinting. Earlier letter, number, unit and glyph controls are copied read-only. Synthetic positions are literal type examples, not calculations.

PDF pages were rendered with Poppler and visually inspected. The bundled installation lacks `pdftotext`; source prose was read through the web PDF reader instead. Full documentary PDFs are retained with their notices. No PDF font contours are extracted or used as drawing inputs. The two HTML source pages were read through the web research reader; full local HTML copies are not claimed.
