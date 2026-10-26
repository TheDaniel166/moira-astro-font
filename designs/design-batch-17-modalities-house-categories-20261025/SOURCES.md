# Source roles and limitations

25 October 2026. [SHA-256 receipts](input-provenance.json) identify the ten frozen inputs. A source for a category is not automatically a source for its pictogram.

| Witness | Inspected location | Role |
|---|---|---|
| [Ptolemy / Robbins](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ptolemy/Tetrabiblos/1b%2A.html) | Book I.11, saved HTML | Historical terminology and sign membership. Translated text is distinguished from modern editorial notes. No six-symbol set is inferred. |
| [Lilly digital reproduction](https://maestrosdelsaber.com/wp-content/uploads/ftp-files/Astrologia/Astro%20y%20Religion/Astro%20Lilly%2C%20William%20-%20Christian%20Astrology%20Vol%201%201647.pdf) | Book I Ch.VI, physical p.72; Ch.XVI, physical p.112, printed 88 | House-category and sign-group vocabulary/membership. Physical page numbers are one-based and avoid retype pagination ambiguities. |
| [Houlding / STA, Aspectual Relationships](https://sta.co/portal/pluginfile.php/1745/mod_glossary/entry/413/aspects_STA.pdf) | Authored 2021 teaching sheet, p.1 | Modern vocabulary crosswalk and sign-group diagram. Its artwork and lettering are not copied as font contours. |
| [Original inventory](references/master-inventory.json) and [accepted audit brief](references/approved-brief.json) | Exact six records | Meaning, fallback, unresolved mappings and P4 research gates. No source inventory edit. |
| [Previous comparison controls](references/old-controls.json) | 125 source drawings and advances | Own original signs, planets, aspects and Latin. Comparison geometry only. |
| [Batch 16 source records](references/batch16-glyphs.json) | Eleven approved concepts, already integrated in 0.8 | Own category/relation comparisons. Their archival review fields remain unchanged. |
| [Unicode 17 data](references/UnicodeData-17.0.0.txt) and [license](references/UNICODE-LICENSE.txt) | Frozen reference files | No character assignment is selected. No assertion that the simple component shapes are absent from Unicode. |
| [Own geometry helper](references/geometry_expander.py) | Frozen helper copy | Local outline expansion and checks, not a font build or engine calculation. |

The Lilly file is a retyped reproduction. Its added cover/filename say 1647; its internal title says second edition 1659. It is not presented as a verified original facsimile. Poppler reports unavailable Symbol/ArialUnicode display fonts. The inspected category prose remains readable; missing symbol renderings are not evidence of historical absence.

All three reference images were inspected: [house passage](references/renders/lilly-houses-072.png), [modality passage](references/renders/lilly-modalities-112.png) and [STA teaching sheet](references/renders/sta-aspects.png). The latter visibly contains familiar sign/aspect glyphs and a coloured class diagram; no colour legend is adopted as a standalone glyph assignment.

The secondary alchemical lead and inaccessible Astrodienst pages are described in [the research note](RESEARCH.md); they are not positive primary form witnesses. Source documents remain local research snapshots and retain their authors' rights. This packet grants no redistribution rights over third-party references.

[Rendering method](references/RENDERING.md) · [Research](RESEARCH.md).
