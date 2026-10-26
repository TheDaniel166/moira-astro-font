# Batch 19 design decisions

25 October 2026 · four proposed compositions · no font integration

1. **Name the 165° study Tao.** The user selected this name. Use Tao in display names and legends; preserve Quindecile (165°) only as a qualified alias when documenting that source convention. Existing Quindecile at 24° keeps its name, Qd outline and exact token.
2. **Continue the letter family.** Proposed companions are Ta, Hx, Sn and Ut. Each is an original optical composition of unchanged approved Latin outlines. No historical glyph attribution is attached to these abbreviations.
3. **Keep source letters contextual.** q/O/n/d reuse ordinary Moira letters. Their aspect meanings require a named convention and legend; they are not new alternate outlines or global text replacements.
4. **Keep four exact identities.** Tao is 165° or 11/24 circle; Hexadecile is 22.5° or 1/16; Seminovile is 20° or 1/18; Untion is 15° or 1/24. Include the angle with the name, particularly where terminology varies.
5. **Preserve nearby family members.** Comparisons include Qd, N, N², U, D, Quintile Q, ordinary H, O and unslashed zero. No existing form is modified to create a difference.
6. **Treat this as design review.** `default_selected` is false. No Unicode, PUA, token, feature or variation allocation is made. A later integration can create the Tao route and connect it to the archival inventory record without retargeting the native Quindecile route.

## Geometry

The construction uses a 1,000-unit vertical em and existing 60-unit strokes. Variable advances allow the components to retain their outlines and useful separation.

| Mark | Components and x offsets | Advance |
|---|---|---:|
| Ta | T at 0; a at 660 | 1280 |
| Hx | H at 0; x at 660 | 1210 |
| Sn | S at 0; n at 660 | 1280 |
| Ut | U at 0; t at 670 | 1100 |

These are multi-letter compositions, so they are wider than a single symbol. The original source drawing coordinates are retained in each component, and the validator reconstructs each composition from frozen controls. Masters are standalone path-based SVGs with no external resources.

## Chart use

The proof sheets show 14, 18, 24 and 32 px em. At 14 px the strokes are delicate: retain a complete name/angle legend and review the actual target chart density. Passing pixel-presence checks does not establish user recognition. The source letter O also resembles ordinary zero, so it is a qualified compatibility choice rather than the proposed Hx default.

The new registry retains each full original planning record under `source_record`; its old inventory ID is an archival key. **Tao is the current primary display name**, and Ta is the proposed mark. Historical naming uncertainty for Hexadecile and Untion is recorded in [research](RESEARCH.md), rather than hidden by a new glyph.

Native models, orbs, aspect admission, interpretation, glyph installation and publication are outside this packet. Current font binaries and all earlier output packets remain covered by the original preservation baseline.
