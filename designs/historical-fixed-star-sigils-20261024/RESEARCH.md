# Historical fixed-star characters for Moira Astro

Research and manual reconstruction studies, 24 October 2026. These are a new, isolated packet. Existing glyphs, the generic fixed-star marker, the compiled font and engine research were not edited.

## Finding

Yes: there is a concrete historical family we can reproduce. Agrippa prints fifteen named-star characters in *De occulta philosophia*, Book II, chapter LII (52), printed p. CXCVII (197) of the 1533 Latin edition. We inspected the original diagrams in a Library of Congress copy distributed through Internet Archive, and cross-checked the same plate in an Augsburg copy served by MDZ. Those two copies corroborate one printed edition; they are not two independent manuscript traditions. [1533 facsimile](https://archive.org/details/DeOccultaPhilosophiaLoc1533/page/n212/mode/1up), [MDZ catalogue](https://www.digitale-sammlungen.de/en/details/bsb11193457).

Chapter II.47 describes talismanic *images*, such as figurative heads and animals. Chapter II.52 supplies the compact *characters* relevant to this project. The surrounding text on printed p. 196 introduces the fixed-star characters attributed there to Hermes; p. 197 labels each drawing. Attribution in a historical work does not establish that a historical Hermes designed them.

These are a selected family in a talismanic tradition. They do not supply an emblem for every fixed star in an astronomical catalogue, and this packet does not establish a single universal historical fixed-star notation. The generic marker from Batch 11 therefore remains useful alongside named-star sigils.

## Two printed witnesses

We also inspected the 1651 English edition in the Wellcome Collection, Book II, chapter LII, printed pp. 321-323. Its diagrams follow the same fifteen-item sequence: three on p. 321, seven on p. 322, and five on p. 323. This is a later printed witness of Agrippa, not independent proof of a separate ancient tradition. [Wellcome catalogue and viewer](https://wellcomecollection.org/works/ftahuupv).

One explicit variant is useful for the font research: **Bear-tail ends in a ring in the 1533 plate; the 1651 Wellcome copy ends in a plain horizontal line.** Both readings are shown. The extra 1651 vector changes that terminal on the common comparative scaffold; it is not advertised as an exact tracing of every 1651 proportion. Other differences in proportions, ink and terminal treatment remain visible in the reference pages and have not been silently merged into the 1533 set.

## The fifteen records

The historical labels are the evidence-bearing identities. Modern names below are conventional reader aids, not verified catalogue IDs. In particular, this work does not resolve manuscript-specific star identification or change any Moira astronomical object binding.

| Printed 1533 label | Reader label in this study | Graphic detail to retain |
| --- | --- | --- |
| Caput Algol | Algol | Curved bracket, ring-ended upright, inline ring, three bars and short end foot |
| Pleiades | Pleiades cluster | Three bars, stepped bowl and one upward foot |
| Aldebaram | Aldebaran | Compact saltire with four ring ends |
| Hircus | Capella / Goat | Broader, shallower saltire with the same four ring ends |
| Canis maior | Sirius | Crossed diamond, four rings, three bars and an open C terminal |
| Canis minor | Procyon | Three three-prong crowns, bowl, stem and bottom arc |
| Cor leonis | Regulus | Left hook, narrow bottom return and upper-right ring |
| Cauda ursae | Bear-tail | Three curved brackets and a ring at the right end |
| Ala corvi | Crow-wing | Two curved brackets, larger dotted head and short rectangular extension |
| Spica | Spica | Opposed curves, horizontal stem and terminal ring |
| Alchameth | Arcturus | Ring-ended L, upright flag and an upward foot |
| Elpheia | Alphecca | Five rings and two inward ticks on the long descending arm |
| Cor Scorpii | Antares | Upper bridge, four rings, two short feet and two longer legs |
| Vultur cadens | Vega | Ring-ended saltire with a central circle |
| Cauda capricorni | Deneb Algedi | Crossed arms, six rings, three-sided enclosure and two downward feet |

For Bear-tail and Crow-wing the display keeps the historical label, rather than pretending this graphic study has settled a catalogue binding. Alkaid and Algorab are familiar modern associations, recorded provisionally in the machine-readable register. Pleiades remains a cluster: it is not automatically collapsed to Alcyone. These reader names require an identity review against the relevant catalogue and textual witness before software integration.

## What has been reproduced

Fifteen new SVG structural reconstructions use the 1533 plate as their primary graphic source. A sixteenth SVG records the observed 1651 Bear-tail terminal variant. Every coordinate was manually authored; no modern redraw, external font outline or contemporary sigil font was imported.

The drawings preserve the observed arrangement and counts of rings, branches, bars, flags and feet. Curves are smoothed, ring sizes, stroke weight and spacing are regularized, and printing damage is omitted. Consequently **these are normalized structural studies, not exact facsimiles, diplomatic transcriptions or final font outlines**. The historical motifs are not new inventions; Moira's contribution here is the new digital geometry and documented adaptation.

`source-comparisons.html` and the three source-comparison sheets place unretouched crops next to all sixteen studies. `glyph-studies.json` stores the source label, witness, crop rectangle, detail counts, adaptation notes and hashes for each drawing. Complete reference pages remain available to inspect context and distinguish neighboring ink from a sigil detail.

## Legibility findings

- Aldebaran and Capella have the same topology in these printed witnesses. Their proportions differ; adding a new distinguishing branch would create a modern adaptation. Keep their names visible and do not claim the sigils are reliable standalone identifiers.
- Natural width matters. Compressing Algol, Bear-tail, Crow-wing or Deneb Algedi to a square would distort their structure. The SVG studies retain different advances on a common 1000-unit em.
- The 14-18 px columns are stress proofs. Ring counters, small feet, the Crow-wing dot, and bars become fragile at that scale. The 24-32 px columns improve recognition, but do not establish a production minimum size or font hinting quality.
- A chart adaptation should have its own weight and spacing study, with every enlargement or simplification logged. Preserve a source-qualified historical form separately if a chart version changes a meaningful graphic detail.
- No meaning has been invented for an individual dot, bar, loop or branch. The inspected evidence establishes their drawn presence, not a complete symbolic grammar.

## Medieval research boundary

The university-hosted Bibliotheca Philosophica Virtualis catalogue identifies a medieval *Liber de quindecim stellis* tradition attributed to Hermes Abhaidimon, and supplies a Crawford witness. We downloaded the linked 14-page PDF and visually inspected its rendered pages. It is a useful textual witness, including a star list, but we did not establish a complete, legible fifteen-character graphic set from this scan. We have therefore **not** labelled invented alternatives as medieval transcriptions. [Scholarly catalogue and manuscript list](https://www.bphv.eu/en/content/liber-de-quindecim-stellis).

The catalogue also points to other manuscripts and Louis Delatte's 1942 edition. A manuscript-specific comparison would be the next historical research step. It should record a shelfmark and folio for each actual drawing before any alternate is added. The inspected printed family is enough for the present reproduction feasibility study; this is not a comprehensive survey of all fixed-star sigils.

## Proposed font direction

Keep the generic fixed-star marker, and offer the fifteen historical characters as an explicitly named family, for example **Behenian characters / Agrippa 1533**. Keep witness, star identity, and chart adaptation as separate metadata. Names should remain available in charts and accessible text.

No encoding, PUA range, OpenType stylistic-set slot or ligature token is allocated by this packet. No assertion is made here about exhaustive Unicode coverage. Future encoding work must check the pinned Unicode data and existing Moira token registry rather than reuse visually similar characters for convenience.

Before integration: review these source forms; decide whether a separate heavier chart version is wanted; verify catalogue identities; then choose encoding and test actual TTF/WOFF2 shaping and rendering. This packet ends at the visual research checkpoint.
