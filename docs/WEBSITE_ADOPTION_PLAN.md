# Plan: Moira Astro as the website's primary astrological font

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](../OFL.txt).

This is an implementation plan based on a read-only source audit on 2026-10-26. The character guide is implemented in the font project first. Website code, Workspace code, native calculations and live services are unchanged by this task.

## Target and ownership

The owner-confirmed target is all astrological symbols and notation: zodiac, bodies, aspects, points, lots, historical marks and appropriate chart labels. Existing prose/headline typography is retained. The wider typography notes below describe a separate future possibility, outside this adoption scope.

The public website owns its consumer UI and shared presentation code in the `moira-website` repository. Workspace UI is authored in `MoiraWeb/frontend/src`; `moira-website/client/src/workspace` is generated publish output. Migrate the authoring source and use the established Workspace train. The native engine is not a font dependency and requires no change for this plan.

## First gate: identity before styling

An adapter must resolve the stable native identity/kind, catalog number or explicit point identity, model qualifier and approved form preference to a Moira route. Its result should carry route text, required OpenType features, accessible name, minimum review size and pinned font version. Graphic selection must preserve the original native payload, positions, model IDs and lot-formula choice.

The current public `shared/astroSymbols.ts` stores some historical display substitutes. A direct CSS substitution would change their rendered identities in Moira Astro:

| Website identity | Current codepoint | That codepoint's form in Moira Astro | Preferred Moira token |
| --- | --- | --- | --- |
| Haumea | U+2BD7 | Transpluto | `[astro:haumea]` |
| Makemake | U+2BD8 | Hypothetical Proserpina | `[astro:makemake]` |
| Quaoar | U+2BDE | Model-qualified Lilith diamond | `[astro:quaoar]` |
| Gonggong | U+2BE0 | Hypothetical Cupido | `[astro:gonggong]` |
| Orcus | U+2BDD | White Moon Selena | `[astro:orcus]` |

The existing Fortune and Spirit substitutes also coincide. Preserve their separate Moira routes `[lot:Fo]` and `[lot:Sp]`, including the circled-S Spirit default. Test asteroid (26) Proserpina versus hypothetical Proserpina; asteroid (1181) Lilith versus apogee Lilith; and intramercurial Vulcan versus the Hamburg point. Resolve by native identity, not the displayed name alone. If the consumer payload lacks enough identity information, retain a named fallback until it can be resolved reliably.

Suggested adapter location: a new shared presentation module beside `shared/astroSymbols.ts`, with an explicit legacy compatibility path during migration. Keep the legacy map for unmigrated consumers. Do not globally reinterpret its old codepoints as new native identifiers. Use the [guide](../guide/index.html) and [entry registry](../entry-map.json) as the route reference; style variants never choose a physical model.

## Current rendering and export seams

Source locations below are audit pointers, not proof of implementation. Line numbers can move as unrelated work proceeds.

| Area | Source pointer | Adoption work |
| --- | --- | --- |
| Public font loading | `client/src/index.css:26–46`; `client/public/fonts/` | Add pinned, versioned Moira assets and OFL notice; preserve existing consumers during migration. |
| Public prose | `client/src/site/tokens.css:47–48`; `client/src/main.tsx:17–39` | Keep Inter/Cormorant and other intentional prose styles separate from symbol runs. |
| Native identity-to-mark resolution | `shared/astroSymbols.ts:19–163`; `client/src/chart/modelToEngine.ts:62` | Introduce the identity-aware route adapter before changing defaults. |
| Chart appearance variants | `client/src/components/engine/engineWheel.css:28,143,259`; `client/src/chart/designs/` | Update the shared symbol contract and every design override. |
| Legacy wheel substitutes | `client/src/components/wheel/wheelData.ts:4–8,140` | Audit the wheel-specific map; preserve its documented distinction until this consumer migrates. |
| Other public surfaces | transits, shadbala, home, Craft and poster styles | Inventory explicit stacks and migrate by bounded consumer coverage. |
| Workspace identity/model labels | `src/features/chart/engine/natalToEngine.ts:74–85` | Preserve mean/true qualifiers, accessible names and original payload. |
| Workspace symbol selection | `src/features/chart/astrologicalSymbols.ts`; `src/features/chart/bodyGlyphs.ts` | Replace resolved graphic routes while retaining explicit unsupported-identity fallback. |
| Workspace SVG primitives | `src/shared/chart-engine/primitives/BodyRing.tsx:119–128`; `ZodiacRing.tsx:17–24` | Apply the font/features on symbol runs; maintain semantic equivalents. |
| Workspace styles | `src/styles/wheel.css:517,727,818` | Reset symbols to regular weight 400 and normal style; avoid inherited italics/synthetic bold. |
| Canvas and cached labels | `src/shared/chart-engine/runtime/ChartSurface.tsx:726–775`; `src/features/celestial-sphere/CelestialSphere.tsx:364–388,1991–1994` | Await the pinned font and regenerate measured layouts/sprite textures after readiness. |

Workspace pointers in the table are relative to `MoiraWeb/frontend`. Consumer pointers are relative to `moira-website`.

Exports are part of the same adoption milestone as the screen renderer:

- `client/src/lib/natalChartExport.ts:16–38` copies several text styles but currently omits `font-feature-settings`. Preserve required features and the exact text runs in standalone SVG. Its embedding list is at lines 41–48; its SVG feeds PNG and raster PDF paths at 313–347.
- `client/src/lib/posterExport.ts:47–61,125–135,201–239` embeds old symbol fonts and rasterizes the resulting SVG. Include the pinned Moira face and verify feature/measurement parity.
- `server/posterPdf.ts:89–95,270–285` loads/registers the old fonts. Its character-by-character Noto rewrite at 343–365 must handle complete Moira runs rather than split ligature tokens. Prove `dlig` and `zero` shaping in the actual PDF stack; registration alone is insufficient. If that stack cannot shape the required runs, introduce an explicit shaped-glyph export path with preserved labels/text mapping.
- `shared/posterWheel/constants.ts:545–553` mixes text/symbol stacks; `composition.ts:7,91–100` consumes shipped-font advance data. Update the measurements together with the font.
- `pages/craft/ephemerisPrintFonts.ts:5–16` preloads print fonts. Include it in the print validation lane.
- `server/_core/vite.ts:124–131` caches `/fonts/` for a year. Use versioned or content-hashed filenames and retain the matching adapter/font pair for rollback.

## Staged implementation

1. **Pin the package and build the route adapter.** Record the exact TTF/WOFF2 SHA-256 and license from the font release. Keep `font-style: normal`, weight 400 and font synthesis disabled on symbol runs. Enable `dlig` only where the selected route requires it; the slashed zero requires `zero`. Preserve readable identity labels during loading/failure.
2. **Pilot one public chart surface with its export lane.** Cover the core planets, zodiac, aspects, mean/true node and apogee labels, Fortune/Spirit, the five colliding TNO substitutes and ambiguous hypothetical/asteroid names. Measure full advances after font readiness and rerun collision layout. Validate SVG, PNG and PDF at the same time.
3. **Expand public consumers.** Migrate each chart appearance, wheel variant, relevant table, transit view, Craft/ephemeris and poster renderer. Record which consumers still need legacy assets. Covered identities use Moira first; unresolved identities keep explicit text/monogram fallback.
4. **Migrate Workspace authoring source.** Reuse the identity contract, reset inherited glyph styles, update canvas textures and ensure layout invalidates after the new font becomes ready. Use the Workspace publish train rather than editing generated website copies.
5. **Promote an exact staged artifact.** Run the existing owner build/readable-UI checks, verify real screen/export output, record source/font hashes and promote the tested staged artifact. Retain a rollback to the previous adapter plus font assets. Repository pushes alone are not live deployments.

The first implementation request should be bounded to steps 1–2. It should not include a blanket font-family replacement or unrelated calculator/catalog work already in progress.

## Acceptance and rollout evidence

- Recorded native chart payloads retain every identity, longitude, motion/model qualifier and lot-formula reference before/after rendering changes.
- Every supported adapter route shapes to the intended glyph in the pinned font. Regression cases include the five TNO collisions, Fortune versus Spirit, all named Lilith/Proserpina/Vulcan identities, historical/chart star forms and the zero feature.
- Loading, ready, missing-font and unsupported-identity states show readable labels and meaningful status. No raw JSON/errors appear in ordinary UI or disclosures.
- All appearance variants retain full glyph/label advances, actual chart sizes and non-overlapping callouts at supported widths and export scales. Font readiness changes trigger layout/texture invalidation.
- Standalone SVG retains text, feature settings and font embedding. PNG/PDF show the same intended marks and qualifiers; actual PDF output proves shaping and readable text mapping.
- Public checks include `pnpm check:readable-ui` and the normal build/check gates. Workspace checks include `npm run check:readable-ui` and its normal TypeScript/Vite build. Do not waive either owner standard or claim live readiness from source scanning alone.
- Publish a consumer/appearance/export coverage matrix before retiring compatibility fonts. Record the exact staged artifact and rollback pair.

## Wider prose/headline typography

The current font is Regular/400 and specialized for symbols and notation. It includes all 52 Latin letters but 77 of 95 printable ASCII characters; current probes lack `!`, `&`, `?`, `@`, `_`, braces, accented Latin examples, curly quotes, en/em dashes and euro. The font has no `GPOS` or `kern` table. These are observed scope facts, not a request to alter the approved symbol glyphs.

Site-wide prose adoption would need a separately planned typography family: complete site/language text coverage, spacing and kerning, required weights/styles, extended punctuation/currencies/diacritics, shaping/accessibility tests and editorial review. That can accompany the symbolic family while preserving its existing forms and routes. It must be treated as a new font-design milestone rather than a CSS setting.
