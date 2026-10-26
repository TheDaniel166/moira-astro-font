# Moira Astro / Pilot 01 — design record

Date: October 23, 2026. Status: draft, awaiting owner review.

## Geometry and authorship

The geometry is authored directly as coordinates, Bézier curves, circles and line segments in `build_glyphs.py`. There are no input fonts, downloaded SVGs, traced images or external contour dependencies. The script is the editable source of record; edit it and rebuild rather than hand-editing generated copies.

The design reinterprets established symbol identities. Original drawing does not mean Moira invented Aries, the planetary signs or the aspect conventions. No new astrological meaning is introduced by this pilot.

| Property | Pilot decision |
|---|---|
| Canvas | 1000 × 1000 units |
| Stroke | 44 units, centered on each path |
| Terminals / joins | Round / round |
| Color | `currentColor`; one ink, transparent background |
| Circular vocabulary | True circles; differing radii according to visual role |
| Nominal advance | 1000 units for the SVG review grid only |
| Outline status | Editable stroked drawings; font contour expansion deferred |
| Review status | All 30 draft |

Most drawings occupy approximately 180–830 units vertically. Symbols with several components are optically adjusted rather than mechanically forced to the same bounds. Stroke weight is mathematically shared, but apparent weight and rasterization still need human review. At 14 px a 44-unit stroke is only 0.616 CSS px; at 18 px it is 0.792 CSS px. This makes the smallest samples useful stress cases. A future optical-size treatment or slightly heavier small-size master may be appropriate after feedback.

## Coverage and intended mapping

| Family | Meaning | Intended character |
|---|---|---|
| Zodiac | Aries through Pisces, in zodiac order | U+2648–U+2653 |
| Body | Sun | U+2609 |
| Body | Moon, default left crescent | U+263E |
| Body | Mercury | U+263F |
| Body | Venus | U+2640 |
| Body | Earth | U+2641 |
| Body | Mars through Pluto | U+2642–U+2647 |
| Node | Ascending / descending node | U+260A / U+260B |
| Aspect | Conjunction / opposition | U+260C / U+260D |
| Aspect | Trine | U+25B3 |
| Aspect | Square | U+25A1 |
| Aspect | Sextile | U+26B9 |

The [Unicode Miscellaneous Symbols chart](https://www.unicode.org/charts/PDF/U2600.pdf) and [Geometric Shapes chart](https://www.unicode.org/charts/PDF/U25A0.pdf) were consulted for character identities. The chart artwork was not an outline source. Mapping does not establish a universal choice of astrological convention. U+25B3 and U+25A1 are general geometric characters used here in the familiar aspect context.

Every glyph has a stable semantic ID, accessible name, plain-word fallback, form description and source asset in `glyphs.json`. The registry's character strings are metadata; the specimen renders the new SVGs. Text copying from an SVG is not an implemented Unicode/font export feature.

## Explicit default forms

- **Moon:** left crescent opening right, U+263E (Unicode name LAST QUARTER MOON). In a generic body label it represents Moon identity, not a calculated lunar phase. The opposite crescent, U+263D, is a future alternate candidate; do not silently remap one to the other.
- **Earth:** cross inside a circle, U+2641; distinct from a Lot of Fortune entry or other circle-and-cross meanings.
- **Uranus:** H form with a lower circle, U+2645. The alternate astronomical form is not silently substituted.
- **Pluto:** PL monogram, U+2647. A separate orb/crescent/cross variant can be drawn and cataloged later.
- **Nodes:** circular terminals, with the arch up for ascending and down for descending. The drawing itself does not encode mean versus true node or a separate object model.
- **Aspects:** plain stem for conjunction; arrowhead for Mars. Keeping these distinct matters at small sizes. Sextile uses six equally spaced rays.

## Optical review priorities

| Area | What to review |
|---|---|
| Aries / Taurus / Mercury | Do their horns and top joins retain enough air? |
| Virgo / Scorpio | Do their stem rhythms match while their tails remain unmistakable? |
| Capricorn | Is the horned entrance and crossing loop immediately recognizable? |
| Moon | Is the open outlined crescent balanced beside filled Sun dot and open planetary bowls? |
| Jupiter / Saturn | Do the asymmetric curves feel related to the circular vocabulary? |
| Neptune | Are three arrowheads too busy at chart size? |
| Nodes | Do small terminal circles remain open and distinct from body circles? |
| Aspect row | Do the triangle, square and sextile feel equally strong? |

The pilot intentionally exposes these decisions. It does not assert that one browser rendering proves final font quality across operating systems, printers or shaping engines.

## Next bounded stage after feedback

Refine approved drawings, settle defaults and alternates, expand strokes into clean filled contours, remove overlaps, set real font metrics and optical spacing, and build a properly named test font. Then review actual Unicode mapping, fallback, copy/export, light/dark rasterization and print rendering. Keep semantic identities separate from visual variants. Add breadth only after this core family has a coherent approved voice.

## Workspace boundary

All pilot writes are under `C:/dev/outputs/moira-astro-pilot-20261023`. The specimen uses local files and no external network dependencies. No engine, wiki, product font map, installed font, shared Python environment or research file is an input to the geometry build or an edit target. No software test suites, release or CI work are part of this design pilot.
