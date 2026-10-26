# Validation and preservation

Copyright 2026 Moira Astro contributors. Original glyph designs.
with Reserved Font Name Moira.
Licensed under SIL Open Font License 1.1. See OFL.txt and https://openfontlicense.org/

Version **0.13.2-alpha.1** passes **6,251 font/source regression checks**. Two independent builds from the complete editable TTX source are byte-identical and match both distributed containers. Only the `head` and `name` tables differ from the preceding 0.13.1 TTF; the complete remaining sfnt tables, including glyf/loca, cmap and GSUB, are byte-identical.

All 726 glyphs retain their order, outlines, instruction bytes and horizontal metrics. All 225 character mappings, variation maps, historical forms, unslashed/slashed zero behavior, 711 optional token spellings and 35 direct registry routes are preserved. Registry changes are limited to version/licensing metadata; all semantic/model policies and 132 compatibility aliases are unchanged. No new PUA allocations or glyph forms are introduced.

The entire official OFL body is verified unchanged after the customized copyright and Reserved Font Name header. Every embedded license record contains the full OFL text; license URLs and embedding flags agree. No pending-license message remains in either font.

Private Windows GDI intake verified the exact new name table, 726 glyph metrics and 184 BMP mappings. The font resource was removed afterward.

The fresh 13-row browser smoke specimen passes 104 measured advances and 52 TTF/WOFF2 advance comparisons across 1360 px and 390 px viewports. Both complete-page captures were manually inspected. The comparison table scrolls within its region on mobile; there is no body overflow. These checks cover this metadata build. The full design, raster and actual Word export reviews remain dated evidence from the preceding stabilization packet, rather than fresh claims for every application.

The ZIP is hash-checked member by member, extracted into an isolated temporary folder, and its standalone `validate.py` rerun from there. It contains the complete editable source and build tooling; it does not depend on any earlier packet or include private baseline binaries, Word QA documents, host fonts or internal working-tree observations.

All earlier Moira Astro artifacts are compared to the one-time SHA-256 baseline after packaging. The engine HEAD and full working-tree/index observations are compared without importing or editing engine modules. Exact local evidence is retained outside the distribution ZIP. The included release manifest records the file hashes; the local package report records the final archive details.

No global font installation or public publication took place. No native computation or unrelated research was changed.
