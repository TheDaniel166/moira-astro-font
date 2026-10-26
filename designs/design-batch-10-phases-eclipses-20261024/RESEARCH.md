# Research: lunar phases and eclipse/occultation notation

## Phase identities

The final [Unicode 17 NamesList](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt), entries U+1F311–U+1F318, identifies the eight phase characters. Its moon-symbol note qualifies the orientation convention, including hemisphere differences. U+263E, the existing Moon-body crescent, is a separate character from the eight disk characters. Unicode names and reference forms establish character identity, not a timing algorithm or a unique view of the sky.

[NASA's phase overview](https://science.nasa.gov/moon/moon-phases/), sections “All Moon Phases” and the eight named phases, describes the sequence through changing visible sunlight and explicitly uses a Northern Hemisphere viewpoint. New Moon alone does not imply a solar eclipse. For this design packet, the named sequence and broad crescent/quarter/gibbous distinctions are relevant; no NASA image is used as outline input.

**Design interpretation:** fixed monochrome disks, without faces or surface texture. Waxing shapes have their negative-space opening on the right; waning shapes mirror that structure. This is labeled symbolic notation, not a location-aware apparent Moon image. Neither hemisphere nor phase meaning is selected by an OpenType style feature.

## Event-form evidence

[Kirk Miller's 2022 Unicode request](https://www.unicode.org/L2/L2022/22005-fortune-eclipse.pdf), PDF pages 1–2 and Figures 7–11 on pages 8–9, documents filled counterparts of conjunction and opposition used for occultations and lunar eclipses. Figure 7 also shows the Moon–occultation–Sun composition for a solar eclipse. These examples support the event distinctions and composition structure; they do not supply Moira's path coordinates.

The final Unicode identities are U+1F775 OCCULTATION and U+1F776 LUNAR ECLIPSE. The proposal's mistaken U+206C/U+206D references on its first page must not override the final UCD or the existing conjunction/opposition U+260C/U+260D characters.

**Design interpretation:** retain the existing own-family round stems and open aspect marks. New event disks match the outer extents of their open counterparts. The solar composition uses the unchanged Moon and Sun source drawings with the new occultation mark between them.

## Theme, orientation and meaning

Monochrome type is ink and negative space. Changing foreground color in an inverse theme changes apparent luminance but must not swap the named glyphs. The inverse sheets therefore show identical geometry with explicit phase names. A product that wants a physically bright/dark lunar visualization needs a separate presentation layer; it should not silently rewrite character identity.

The 145-by-285-unit terminator ellipse is an original optical choice that keeps narrow regions useful at small sizes. It is not a claim of a specific illuminated percentage or exact 45° phase sampling. The common rim relates the eight disks to the existing Sun outline while the central dot continues to distinguish the Sun from Full Moon.

## Contacts and native models

The inventory already treats C1–C4, P1/P4 and U1–U4 as ordinary labels. The context specimens show notation examples, with C2/C3 and U2/U3 bracketed to emphasize conditional availability. The application must use the contacts actually supplied by its event data. A font cannot infer totality, centrality, contact presence, umbral enlargement or a phase-timing convention.

No engine code, ephemeris model, native lunar model or eclipse calculation was imported, executed or changed. Invented typography examples are labeled as such.
