# Lilith, Fortune, Spirit, angle and motion notation

23 October 2026 - Research supporting original Moira Astro design proposals

## 1. Lilith: keep the mark and the computational model separate

U+26B8 BLACK MOON LILITH supplies the familiar crescent/cross identity. Faulks's [symbol study](https://www.unicode.org/L2/L2016/16080-add-astrology.pdf#page=22) documents multiple traditions, including a diamond-on-cross form associated with true Lilith in some software. The final [Unicode 17 NamesList](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt) assigns U+2BDE BLACK DIAMOND ON CROSS and annotates that usage.

That is form evidence, not a definition of Moira's mathematical reduction. The native source defines mean Lilith from IERS 2003 mean lunar arguments and osculating Lilith from the geocentric eccentricity vector derived from DE441 states. See the [frozen native excerpt](references/native-nodes.txt). No engine is executed here, and osculating apogee is not silently equated with an interpolated sequence of actual apogee events.

**Design proposal:** use one generic crescent/cross with explicit mean or osculating labels. Keep the diamond/cross as a model-convention study pending compatibility review. Its selection must never change a model or the calculated value. The existing generic Moon icon, asteroid (1181) Lilith, and hypothetical second-moon conventions remain separate identities.

## 2. Fortune: use the dedicated identity, preserve the physical distinction

The final UCD assigns **U+1F774 LOT OF FORTUNE**. Miller's [encoding request, page 1](https://www.unicode.org/L2/L2022/22005-fortune-eclipse.pdf#page=1) documents the circle-and-X form. Moira's original Fortune drawing uses that structure and remains visibly distinct from the unchanged U+2641 physical Earth drawing.

U+2297 CIRCLED TIMES is retained only as a documented legacy mapping option. It does not require a second invented outline or a silent migration of any existing product data. U+1F774 is above the BMP; an eventual font build needs supplementary-plane mapping support. This packet provides no such font implementation.

## 3. Spirit: a sourced convention, with an honest character name

Miller reports both a circled S and a circle with a vertical bar, without a fixed universal Spirit sign. The proposal has opinions about the prevalence of lots and simplifies some formula choices; those claims are not adopted as Moira doctrine.

**New encoding lead:** U+24C8 is CIRCLED LATIN CAPITAL LETTER S. It can represent the proposed circled-S convention contextually. It is not a newly discovered dedicated LOT OF SPIRIT assignment. U+29B6 CIRCLED VERTICAL BAR provides the alternate geometric convention. Both formal names were checked against the pinned UCD.

The circled-S proposal reuses the accepted S construction with an optical stroke adjustment inside an original ring. Its full text fallback is **Spirit**. Unicode compatibility normalization can reduce a circled letter to its ordinary letter; therefore neither normalized S nor a glyph outline can serve as the stored identity of the lot. Keep semantic ID `lot.spirit` and source/formula metadata independently.

The review packet proposes circled S as the default icon for discussion, alongside the vertical-bar and text alternatives. It allocates no private-use codepoint or final font mapping.

## 4. Fortune/Spirit formulas remain source-specific data

The [native lot definitions](references/native-lots.txt) store Fortune with day operands Moon minus Sun and Spirit with Sun minus Moon, both with night reversal enabled and the default Asc projector/directed policy. In ordinary shorthand:

| Lot | Day expression | Night expression |
|---|---|---|
| Fortune | Asc + Moon - Sun | Asc + Sun - Moon |
| Spirit | Asc + Sun - Moon | Asc + Moon - Sun |

This table describes those literal native definitions; it is not independent historical collation or a computation performed by this font task. A symbol or font alternate cannot choose the night rule, projector, arc policy, tradition, timescale or coordinate model.

## 5. Angle labels: preserve words and geometry

The planned default labels remain **ASC, DSC, MC, IC, VX, AVX**. They are ordinary text sequences rather than dedicated astrological scalars. Pullen's [own manual](https://www.astrolog.org/ftp/astrolog.htm), in its Vertex discussion, documents Vx and another graphical tradition. Vx is therefore included as a case alternative. AVx is a Moira case-pair proposal derived from AVX; it is not claimed to be a universally attested historical abbreviation.

The native [house/angle excerpt](references/native-houses.txt) keeps Vertex as the western prime-vertical/ecliptic intersection and Anti-Vertex as the opposite point, with explicit branch/polar conventions. ASC/DSC and MC/IC remain the declared point pairs; the lettering does not claim that every house system assigns them to the same cusps. This task does not revalidate or modify native geometry.

Labels are composed at natural widths. Each ordinary character receives its own proportional proof advance, with the common source scale applied per component. Multi-letter words are not horizontally squeezed into a single-symbol em square. These are proof-layout advances, not finalized font metrics.

## 6. Motion labels: readable text, explicit state policy

| Proposed label | Meaning retained from the inventory/native vocabulary | Source role |
|---|---|---|
| Rx | Negative longitudinal rate in a stated frame | Native rate semantics; ordinary Rx usage also documented by the author's [Starzology article](https://www.starzology.com/retrograde-planets/) |
| D | Positive longitudinal rate in a stated frame | Planned label; native semantics, not a claimed exclusive historical character |
| S | Stationary state under a declared policy | Planned label and documented usage in Pullen's manual |
| SR / SD | Station transition into retrograde/direct | Planned labels; native event semantics |
| A / Sep / Exact | Applying, separating, or exact under the selected aspect policy | Planned labels and native aspect vocabulary |

Pullen's manual explicitly documents **R**, **S/R** and **S/D**, which are included as alternatives. Its station threshold settings are evidence of that program's notation, not a threshold imported into Moira. See the [native station excerpt](references/native-stations.txt) and [native aspect-state excerpt](references/native-aspects.txt).

The crossed-R study is an explicit contextual use of U+211E, formally **PRESCRIPTION TAKE**. Ordinary Rx remains the proposed default. Neither character access nor a glyph substitution changes the station threshold, frame, aspect tolerance, applying/separating algorithm or event definition.

## 7. Reuse shapes without conflating meanings

The accepted S, D and V geometry is reused read-only. D can label a Decile or direct motion, and S can label a Septile or stationary state; context and semantic data distinguish them. They remain ordinary Latin characters. A special font mode must not secretly choose a calculation or reinterpret every occurrence of a letter.

The [context proof](meaning-context.svg) makes the model labels, Fortune/Earth distinction, repeated letter contexts and opposite angle labels visible. No calculated chart positions are invented for those illustrations.

## Limits of the evidence

The primary symbol/encoding documents establish character identities or observed forms, not empirical astrological interpretation. Native source defines Moira's current vocabulary and policy, not historical authority. Public source fonts may have substitution notices when rendered; the Fortune construction and Lilith structures were checked against the final assigned identities and retained charts. No external font outline is extracted or traced.

The new drawings remain review proposals. The owner's accepted minor-aspect direction is recorded separately in [DECISIONS.md](DECISIONS.md); old packets are not rewritten to manufacture a new approval record.
