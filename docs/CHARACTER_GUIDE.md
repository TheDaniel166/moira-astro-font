# Character guide and symbol picker

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](../OFL.txt).

Open [the guide](../guide/index.html) locally or serve the repository with `python -m http.server 8000` and visit `/guide/`. The guide uses local fonts and a classic script payload, so it also works with `file://`.

## Coverage and use

The catalog describes **745 usable forms**, including spacing and the slashed-zero feature alternate. The unencoded missing-glyph marker is excluded. It retains all **225 Unicode mappings, 599 canonical tokens, 132 compatibility aliases and 17 supported text-presentation sequences**. One drawing can carry more than one named/model-qualified context; those contexts remain explicit.

Search by name, alias, meaning, category, source title, codepoint, character or exact token. The index starts with the default zodiac/body forms and paginates its results. Choose a form to read its definition, witness, context, related graphics and copy routes. Detail navigation supports deep links and browser history. Mobile dialogs retain a clear heading, restore focus to the originating result, and preserve the reading position when closed.

Unicode copy preserves the actual character. Token and Word-alias copy preserves the exact case-sensitive text and requires discretionary ligatures. Text-presentation copy retains its variation selector. Slashed zero copies the base `0` and requires `zero`; it does not receive a new Unicode identity. Space and no-break space have separate labels/codepoints and copy their exact invisible values. If clipboard APIs fail, the guide presents a focused, selected readonly value for manual copying.

Preview sizes are 18/24/32/48 px. Forms with a larger review size show a stress notice when previewed smaller. Historical witnesses remain visible. Web examples carry the selected route's `dlig`/`zero` settings, regular style/weight, disabled synthesis and preserved whitespace. The copied text carries no automatic native model or lot-formula selection; keep those fields in chart data and accessible labels.

## Source derivation

`tooling/build_character_guide.py` reads the actual TTF, active entry/alias registry, reconciled inventory and archived source citations. It writes `guide/assets/catalog.json` and the equivalent `catalog.js` payload with explicit LF newlines. It does not write fonts or archival inputs. Rebuild deliberately with:

```text
python -B tooling/build_character_guide.py
python -B tests/check_character_guide.py
```

The generator uses preserved original mappings to identify core defaults where the reconciliation's top-level mapping lists a later alternate. Thus the original Sun/Moon forms and their ray/opposite-crescent alternatives remain separate, linked records. Formal Unicode names and assigned character identities remain separate from astrological meanings. Current form admissions come from the compiled font and active registry; archived planning status does not silently admit or replace glyphs.

The regression test regenerates both outputs in a temporary directory, verifies full glyph/route coverage and relationships, and independently shapes all previews and routes in TTF and WOFF2. It checks shared lunar contexts, circled-S Spirit, historical/chart witnesses, default Sun/Moon, opt-in ligatures and the zero feature. It runs on Windows and Linux CI.

## Browser review

Optional visual tooling uses `requirements-review.txt` and agent-browser with its matching Chromium runtime. From PowerShell:

```text
./tooling/Capture-CharacterGuide.ps1
python -B tooling/check_guide_browser.py
./tooling/Test-CharacterGuide.ps1
```

The capture records 48 combinations of desktop/tablet/phone width, theme, font format and representative edge cases. It also opens all 745 detail forms and activates all 974 copy routes against a recorded clipboard API, preserving the user's system clipboard. The independent validator checks actual advances and glyph features, exact payloads/receipts, source-preserving HTML/CSS examples, complete results and visible TTF/WOFF2 glyph pixels. Fingerprints reject source changes during a capture.

Native-control checks cover pagination, searches/categories, format/size/theme, feature-only and Word routes, rapid-copy feedback, denied-copy manual visibility/selection, real history/deep-link recovery, mobile focus return/heading reset, and isolated missing-font/missing-data states. Review reports and screenshots stay under ignored `build/character-guide/`.

The design was independently reviewed by an available agent; no second-provider review is claimed. Chromium review and recorded clipboard calls are not universal browser, OS clipboard or assistive-technology certification. The technical checks do not select models or publish the guide to a live website.

## Website adoption

The confirmed next target is [Moira Astro as the primary website font for astrological symbols and notation](WEBSITE_ADOPTION_PLAN.md). A semantic route adapter must precede the font-stack change because several legacy display codepoints select different identities in this font. Existing prose typography and native calculations remain outside this migration.
