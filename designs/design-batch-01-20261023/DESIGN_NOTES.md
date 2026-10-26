# Moira Astro — Batch 01 design record

Draft 01 · 23 October 2026 · Ten new concepts, proposed for the P1 everyday toolkit.

## Direction

Continue the approved Alpha 2 language: open counters, monoline construction, round terminals and joins, and familiar semantic structures. Nine drawings use 60-unit source strokes; Juno uses a 56-unit optical stroke because its eight-ray head is denser. These are new drawings for established identities.

Review the [overview](overview-light.svg), [dark overview](overview-dark.svg), [construction sheet](construction-sheet.svg) and [chart-size proof](chart-size-proof-light.svg). Names and mappings stay visible so a well-rendered wrong symbol is not mistaken for a successful design.

| Design | Intended identity | Construction and review focus |
|---|---|---|
| [Ceres](masters/ceres.svg) | U+26B3 — CERES | Open crook above a lower cross. Keep the upper hook open and distinguish the crook from Saturn's lower hook. |
| [Pallas](masters/pallas.svg) | U+26B4 — PALLAS | Open diamond above a lower cross. The diamond counter stays large; round joins belong to the existing Moira family. |
| [Juno](masters/juno.svg) | U+26B5 — JUNO | Eight-rayed head above a lower cross. Eight rays distinguish Juno from the six-ray sextile. The 56-unit optical stroke gives the center more space. |
| [Vesta](masters/vesta.svg) | U+26B6 — VESTA | Detached flame stroke above two open, winged downward chevrons. Preserve the angular flame/altar construction of the U+26B6 form. The historical U+1F777 form remains a separate future alternate. |
| [Chiron](masters/chiron.svg) | U+26B7 — CHIRON | K-like key head rising from an open oval. Separate the arms from the base loop; keep the right branch open and the oval legible. |
| [Pholus](masters/pholus.svg) | U+2BDB — PHOLUS | P-like head rising from an open oval. Two open counters distinguish this form. The lower oval and tall stem align with Chiron, while the closed head remains distinct. |
| [Semisextile](masters/semisextile.svg) | U+26BA — SEMISEXTILE | Open upward arms meeting a horizontal baseline. Keep this exact vertical reflection relationship with quincunx; do not rotate the glyph in text. |
| [Semisquare](masters/semisquare.svg) | U+2220 — ANGLE | Open angle: diagonal meeting a horizontal baseline. U+2220 retains its ANGLE identity. Its semisquare use is contextual and annotated by Unicode. |
| [Sesquiquadrate](masters/sesquiquadrate.svg) | U+26BC — SESQUIQUADRATE | Open square with an attached lower-right elbow. Use the square/elbow structure of the assigned U+26BC reference form. Retain a large square counter and a clear projecting elbow. |
| [Quincunx](masters/quincunx.svg) | U+26BB — QUINCUNX | Horizontal cap with open downward arms. A vertical reflection of semisextile, with the cap explicitly at the top. |

## Source use

The final Unicode 17 assignments and character names come from the master inventory. Charts establish recognizable structures; they do not prescribe Moira proportions. The 2016 proposal is consulted only for Pholus usage examples, never for its obsolete proposed code position. External outlines are not imported or traced.

- **ucd17-misc** — [Unicode 17.0 Miscellaneous Symbols chart, PDF page 2, U+26B3–26BC](https://www.unicode.org/Public/17.0.0/charts/PDF/U2600.pdf). Identity and structural reference only; no prescriptive proportions or imported outlines.
- **ucd17-arrows** — [Unicode 17.0 Miscellaneous Symbols and Arrows chart, PDF page 2, U+2BDB](https://www.unicode.org/Public/17.0.0/charts/PDF/U2B00.pdf). Final Pholus character identity and structural reference.
- **ucd17-math** — [Unicode 17.0 Mathematical Operators chart, U+2220](https://www.unicode.org/Public/17.0.0/charts/PDF/U2200.pdf). Assigned ANGLE character, not a dedicated differently named semisquare codepoint.
- **ucd17-names** — [Unicode 17.0 NamesList: U+2220 astrological semisquare annotation](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt). Explicit evidence of contextual semisquare usage.
- **faulks2016-p19** — [David Faulks, Additional Symbols for Astrology, page 19](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf#page=19). Usage examples for P-over-loop Pholus. Draft proposed code positions are not encoding authority.
- **alpha2** — [Existing Moira Astro 0.1.0-alpha.2 original master registry](C:/dev/outputs/moira-astro-pilot-20261023/font-v0.1.0/glyphs.json). Read-only family proportions, stroke and comparison artwork.
- **inventory** — [Moira Astro master character inventory, 1.0.0-planning](C:/dev/outputs/moira-astro-character-inventory-20261023/inventory.json). Stable semantic IDs, meanings, priorities and intended mappings.

## Review limits

The sheets render SVG source vectors, with a 1.08 scale matching the Alpha 2 source-to-font scale in a 1000-unit em cell. Both new and existing comparison vectors receive the same preview transform. The labels 14/18/24/32 refer to nominal CSS em-cell size. They do not represent actual TTF rasterization, finalized side bearings, baseline placement or hinting.

All ten remain owner-review drafts. No ssXX/cvXX slots, private-use values or product mappings are introduced. The existing 30 masters, font binaries, specimens and inventory remain unchanged. Source PDFs retained under references/ are internal research copies with their full notices, separate from the original Moira artwork.

## Owner review priorities

1. Do Ceres, Pallas, Juno and Vesta read as their named symbols without guessing?
2. Do Chiron and Pholus remain distinct from each other and the existing PL Pluto?
3. At 14/18 px, do Juno's rays, Pholus's two counters and the sesquiquadrate elbow remain clear?
4. Is the upper/lower orientation of semisextile and quincunx immediately recognizable?
5. Does the new group feel the same weight as the existing family in both themes?

After feedback on this bounded batch, revise the named forms, then proceed to Lilith/Fortune and coherent angle/motion labels from P1. Font integration follows approval of the drawings.
