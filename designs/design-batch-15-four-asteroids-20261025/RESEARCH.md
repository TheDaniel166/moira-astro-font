# Batch 15 research: four physical asteroids

25 October 2026 · Draft 01 · Four original Moira vector studies

Batch 15 completes a focused design study for the four physical asteroid records still pending after the previous inventory audit: **(1181) Lilith, (763) Cupido, (433) Eros and (128) Nemesis**. Batch 14's Hamburg Cupido is already integrated in 0.6 and is a separate identity. This packet does not edit the master inventory or integrate a font.

## Identity and encoding

NASA/JPL [SBDB API](https://ssd-api.jpl.nasa.gov/doc/sbdb.html) responses independently confirm all four number/name pairs. The queries use `no-orbit=1`, and their exact responses are retained. These are identity witnesses, not evidence for a glyph, kernel availability or native runtime admission.

| Physical body | Permanent number | Live JPL SPK ID |
|---|---:|---|
| Lilith | 1181 | 20001181 |
| Cupido | 763 | 20000763 |
| Eros | 433 | 20000433 |
| Nemesis | 128 | 20000128 |

The planning inventory's older `native_catalog_naif_id` values are retained separately, unchanged. No catalogue or kernel migration is performed. The reviewed Unicode 17 inventory selects no dedicated scalar for these four physical identities. Every proposed glyph's character, codepoint, token, feature and PUA fields therefore remain null. U+2BE0 CUPIDO continues to represent the Hamburg point; U+26B8 continues to provide the existing lunar-apogee mark. Neither is reassigned to an asteroid.

## Form witnesses

[Zane B. Stein's Centaur Font reference](https://zanestein.com/CentaursFontGlyphs.pdf), PDF pp. 2-3, provides labelled Eros, asteroid Lilith and Nemesis specimens. It identifies the font compiler and distinguishes three Lilith entries. This is direct evidence of the compiler's selected forms, not proof that he invented every symbol. Its legacy keyboard values are font-specific access instructions, not Unicode assignments for the asteroids.

The [Solar Fire 9 User Guide](https://alabe.com/ProgramDocs/SolarFire_v9.pdf), printed/PDF p. 492, shows a labelled asteroid-glyph grid covering all four. Its prepared artwork is a supplied software convention. The surrounding manual discusses glyph preparation, but does not independently establish an inventor for each concept. Poppler reported fallback-font warnings elsewhere in the manual; the inspected raster grid remains legible. No embedded font path or vendor outline is extracted.

The first-party [Astro Gold provenance table](https://www.astrogold.io/AG-MacOS-Help/minor-body-glyphs.html) lists Lilith with a 1980 CAO Times ephemeris and J. Lee Lehman; Eros with a 1980 CAO Times ephemeris; and Cupido/Nemesis with Martha Lang-Wescott's *Mechanics of the Future: Asteroids*. Those original ephemerides and the complete book were not inspected. These are qualified vendor attributions, not independently verified invention dates or universal standards.

### (1181) Lilith

The labelled specimens show four upright finger strokes, a shared palm and a lower-right angled thumb. Moira keeps this hand-like structure and opens three finger slots. It is distinct from the unchanged crescent-and-cross lunar-apogee Lilith and from Neptune's three-pronged head. No piano-key synthesis, lunar crescent or hypothetical Dark Moon variant is substituted.

### (763) Cupido

Martha Lang Wescott's bylined *Cupido-A* excerpt in the [AstroAmerica newsletter, 1 December 2009](https://astroamerica.com/newsletters/2009-december01.pdf), PDF p. 3, calls its construction a "shielded Venus" and explicitly separates the asteroid from Uranian Cupido. The newsletter attributes the excerpt to her book; it does not establish a first invention date. The software grid supplies a matching visible C-shaped shield around the Venus ring/cross. Moira opens the shield and ring while preserving that construction. The large Jupiter-like hook of Hamburg Cupido is absent.

### (433) Eros

Both inspected font/vendor specimens show a heart pierced by a diagonal shaft with a down-left arrow tip. [Cafe Astrology's own Eros page](https://cafeastrology.com/eros.html) independently describes its heart-and-arrow usage; it is not an inventor attribution. Moira uses new heart curves and round joins, preserving two unfilled fields and a protruding arrow tip. It is a physical asteroid symbol proposal, not a remapping of an ordinary heart or heart-with-arrow emoji.

### (128) Nemesis

The inspected references show two projecting uprights, an upper arch and a divided lower bowl. The Centaur reference has a more angular lower ending than the small Solar Fire grid. Moira selects a flat lower rim with diagonal shoulders, preserving two unfilled fields; the rounder witness remains in the source archive. It is distinct from Admetos's quartered ring and Nessus's N-like head. No tenth-planet, hypothetical stellar companion or fictional-body identity is attached to the asteroid.

## Original drawing and optical choices

All four outlines were newly authored in Moira's 60-unit round-cap/round-join language, within 1,000-unit source cells. References determine recognisable constructions; their coordinate data, bitmaps and font outlines do not enter the masters. Previews use the established 1.08 scale and -50 y offset.

The chart-size sheets show actual 14/18/24/32 px source-vector samples in light and inverse, with existing-glyph comparisons and named/numbered contexts. Positions are invented typography examples. Fourteen pixels is a stress case; the automated negative-space and stroke witnesses are sampled at 24/32 px. These proofs establish neither final font metrics nor hinting or other-platform behaviour.

Unchanged reference controls are copied into the packet. Existing glyphs, fonts, source research, lot conventions and native models remain outside this task's writes.
