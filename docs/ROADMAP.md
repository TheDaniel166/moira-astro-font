# Roadmap

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](../OFL.txt).

## Standalone project foundation

The 0.13.2-alpha.1 baseline has complete TTX source, preserved SVG design history, reconciled inventory, embedded OFL licensing and source/encoding regression checks. The repository adds a dedicated home and Windows/Linux CI. Public beta publication remains a separate step.

## Complete-chart pilot

The [pilot](../demo/chart-pilot/index.html) presents a complete wheel and companion tables using the existing font. It includes distributed and crowded positions, aspect/motion context, lots and a four-letter abbreviation, dense minor bodies, historical fixed-star forms with witnesses, and satellite compositions. It uses declared construction fixtures and has no engine dependency.

The implementation provides light/dark themes, font-format selection, keyboard-accessible scrolling and a three-page Letter-landscape print folio. Independent fixture, browser and PDF checks are documented in [the pilot guide](CHART_PILOT.md). The pilot exposes presentation conventions for owner review; it does not change approved drawings. Keep that review distinct from automated validation.

## Character guide and picker

The [guide](../guide/index.html) covers all 725 usable forms with name/alias/category/source searches, Unicode and exact-token copying, Word aliases, variant links and model/witness notes. Feature-only slashed zero and blank spacing retain their actual encoding behavior. The font binaries, drawing history and native model remain unchanged. Generation and regression commands are recorded in [the guide documentation](CHARACTER_GUIDE.md).

## Next: website symbol-font adoption

The owner has confirmed Moira Astro should become the primary font for astrological symbols and notation, while the website retains its prose typography. [The adoption plan](WEBSITE_ADOPTION_PLAN.md) records a read-only consumer/export audit, legacy-code collisions, ownership boundaries and a staged migration. Implement the identity-aware route adapter and one public chart with its SVG/PNG/PDF lane before expanding to the remaining public surfaces and Workspace authoring source.

## Public beta preparation

Prepare a versioned release with TTF/WOFF2, editable source, OFL/Unicode notices, reproducible build instructions, a searchable character guide and copyable token examples. Publish the tested-application matrix and known limitations. Tagging, release uploads, hosted specimens and a visibility change are maintainer publication actions.

Further glyph expansion should follow documented requests and source evidence. The covered master inventory is the starting repertoire, not a claim that every historical or contemporary convention has been exhausted.
