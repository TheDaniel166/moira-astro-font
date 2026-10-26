# Design archive and provenance

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](../OFL.txt).

The repository preserves two kinds of original SVG source:

- `designs/` contains review-stage originals, variants, later refinements and design/research records from 29 packets. Packet names retain their dates. Superseded variants and earlier approval statements remain visible as historical records.
- `masters/` contains the font-stage SVG inputs retained by successive alpha builds, including the corrected pilot and later optical refinements. Generated lot/label constructions and all final outlines also exist in the active TTX.

These SVGs are historical design inputs. The active reproducible build reads only `source/MoiraAstro-Regular.ttx`. An archived SVG edit is not automatically compiled. An intentional refinement needs a new design record, an explicit active-source update and regression/visual review.

[provenance/imports.json](../provenance/imports.json) lists every initially copied file, its SHA-256, role and original path relative to the frozen output archive. It identifies lineage without making the old folders runtime dependencies. The source archives and earlier output packets remain separate; the latter are preserved locally in full.

Hash checks freeze the archived design, font-stage master, admitted batch-source, planning and dated evidence files. Active scripts and registries can evolve under ordinary version control; their recorded import hashes describe the initial copied version rather than an immutable future state.

Research notes can link to retained PDFs, images or HTML from the original local packets. Those external reference assets are not redistributed in this repository. Use the cited source URLs and the source descriptions; a local citation filename is an archive locator, not a promised bundled file. No third-party font, reference PDF, historical scan or host-font subset is included.

Dated JSON may state “draft”, “not integrated”, “license undecided” or no Unicode assignment because that was the correct status at its creation. Current font admission is defined by the active TTX and entry map. Current licensing is [OFL.txt](../OFL.txt) and [NOTICE.md](../NOTICE.md). Preserve dated records rather than rewriting their historical meaning.

`inventory/planning/` preserves the original planning records, while `inventory/inventory.json` holds the later 327-record reconciliation. Per-record source and definition limits remain available; visual similarity is not a declaration that two native models or meanings are interchangeable.
