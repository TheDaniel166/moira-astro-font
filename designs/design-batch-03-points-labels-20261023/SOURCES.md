# Sources and evidence roles

Accessed 23 October 2026. Unicode mappings remain pinned to 17.0.0. Original coordinates and source provenance are distinct from symbol meanings.

| ID | Source / relevant location | Supports and limits |
|---|---|---|
| `unicode17` | [UnicodeData](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt), [NamesList](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt), retained Unicode charts | Formal assigned identities: Lilith, Fortune, circled S, circled bar, diamond/cross, prescription character and ordinary text. No model or universal convention is inferred from a name |
| `miller2022` | [Kirk Miller, L2/22-005](https://www.unicode.org/L2/L2022/22005-fortune-eclipse.pdf), PDF page 1 | Fortune structure and competing Spirit forms. Its usage opinions, simplified formula discussion and proposal-era codepoint typos are not imported |
| `faulks2016` | [David Faulks, Additional Symbols for Astrology](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf), PDF pp.22 and 30 | Crescent/cross and model-associated Lilith form evidence. Old proposed positions and broad model/history claims are not final authority |
| `astrolog-manual` | [Walter Pullen, Astrolog 8.00 manual](https://www.astrolog.org/ftp/astrolog.htm), Lilith/Fortune/Vertex discussion; `-d` and `-Yw` sections | Creator's description of Vx, R, S, S/R and S/D usage. Neither source geometry nor computational policies are imported |
| `starzology` | [Alison Price, Retrograde Planets](https://www.starzology.com/retrograde-planets/), notation discussion | Direct published usage of the letters Rx alongside a planet glyph. Not treated as an ephemeris or model authority |
| `native-nodes` | [Frozen excerpt](references/native-nodes.txt), from [nodes.py](C:/dev/moira/moira/nodes.py:347) | Current mean/osculating model definitions; no engine execution or independent validation claim |
| `native-lots` | [Frozen excerpt](references/native-lots.txt), from [lots.py](C:/dev/moira/moira/lots.py:411) | Literal native operands, night flags, projector and arc-policy defaults; no new historical admission |
| `native-houses` | [Frozen excerpt](references/native-houses.txt), from [houses.py](C:/dev/moira/moira/houses.py:1474) | Point names and branch/house conventions; no calculation changes or runtime verification |
| `native-stations` | [Frozen excerpt](references/native-stations.txt), from [stations.py](C:/dev/moira/moira/stations.py:5) | Native signed-rate and event vocabulary; proposed label glyphs do not set thresholds |
| `native-aspects` | [Frozen excerpt](references/native-aspects.txt), from [aspects.py](C:/dev/moira/moira/aspects.py:1160) | Existing aspect-state vocabulary; no applying/exactness policy is chosen by artwork |
| `inventory` | [Frozen plan entries](references/planned-points-labels.json), from the original [master inventory](C:/dev/outputs/moira-astro-character-inventory-20261023/MASTER_INVENTORY.md) | Stable IDs, proposed labels and priorities; a plan entry is not historical glyph attestation |

## Frozen artwork and retrieval limits

[Accepted letter components](references/accepted-letter-components.json) retain S/D/V geometry and the Batch 02 registry hash. [Family controls](references/existing-family-controls.json) retain the existing original Earth/Moon-family artwork for reference. Only original Moira drawing data is reused.

Full documentary PDFs and Unicode data remain under `references/`, with their notices and the Unicode license. No third-party glyph contours are extracted, imported or traced. The symbol charts are visual structural references, not artwork inputs to the generator.

The Astrolog manual and Starzology article were read with the web research reader; full local HTML copies are not claimed. A Skyscript glossary fetch was blocked and is not used as evidence. The PDF renderer issued notices for two missing document fonts; the ordinary text remained readable and the assigned Lilith shape was independently inspected in the archived chart. No source PDF itself was modified.
