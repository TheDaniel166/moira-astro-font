# Design decisions and visual review

## Preferred geometry

The new open marker is one path in a 1100 × 1000 source frame:

```svg
<path d="M610 350 L460 200 L160 500 L460 800 L760 500 H940"/>
```

It has a 60-unit stroke, rounded caps and rounded joins. Its three main corners make an angular head. The missing upper-right section prevents a closed circular silhouette. The rightmost horizontal segment provides a common ending before every short label.

At the established 1.08 preview scale, the nominal stroke is about 0.91 px at 14 px em and 1.17 px at 18 px em. The exposed opening has approximately 2.3 px of cap-to-cap clearance at 14 px em. These are geometric scale estimates; actual coverage depends on rasterization and pixel position.

## Why retain the opening

The closed comparison already separates the marker from round O/zero forms by silhouette. The opening adds another recognition cue, and the horizontal ending points toward the adjacent label. The open version is the preferred refinement after inspecting both themes and all four sizes.

The head and ending remain visible in the small source-vector proofs. At 14 px the line is thin and the terminal is short, so no claim of universal small-font readability is made. The preferred geometry is offered for owner review before any font integration.

## Comparisons

The sheets use frozen Moira artwork rather than substitutes from a system font:

| Control | Reason for comparison |
|---|---|
| Previous circular lot prefix | Shows the ambiguity being addressed |
| Capital O | Existing letter with a closed round shape |
| Default unslashed zero | Preserves the selected numeral default |
| Slashed-zero alternate | Preserves the existing alternate |
| Pallas | Existing outlined diamond above a lower cross |
| Diamond Lilith form | Existing filled diamond above a lower cross |
| Fortune and Spirit | Preserve their selected designs and exception status |

At the shown sizes the new prefix extends rightward; Pallas and diamond Lilith extend downward into crosses. This review does not establish distinction from every character, alchemical sign, mathematical symbol, icon or other font.

The similar-name proof retains the earlier pairs Eros/Exaltation, Necessity/Nemesis and Mother/Marriage. The codes remain `Er/Ex`, `Nc/Nm` and `Mo/Ma`. There are no small dots, superscripts or stroke-count differences carrying family identity.

## Typography and identity

The letter-component drawing strings and natural advances are retained. The only composition change besides the marker is the label origin, moved 200 units right. No letters are scaled down to fit the marker. At 18 px em the complete examples occupy about 43–51 px horizontally, depending on the alias. This width is visible in the chart/table examples and remains a layout tradeoff of direction C.

The design is a Moira-original convention proposal grounded in the previous direction C packet. It has no asserted ancient meaning. The aliases name lot families; no marker, alternate or code chooses a formula. The frozen 512-record formula appendix is copied unchanged as context, without recalculation or new historical admission.

## Scope and next review boundary

This packet completes the requested marker refinement and chart-size specimens. The old circular packet and all earlier assets stay intact. The new preferred design is ready for visual feedback. Encoding, broader alias design and font integration require their own implementation scope; no feature slot or font default is silently changed here.
