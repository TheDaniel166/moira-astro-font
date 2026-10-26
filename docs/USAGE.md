# Using Moira Astro

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](../OFL.txt).

Use the [TTF](../fonts/MoiraAstro-Regular.ttf) in desktop applications or the [WOFF2](../fonts/MoiraAstro-Regular.woff2) on the web. Direct Unicode characters work without discretionary ligatures. Use exact, case-sensitive tokens from [the registry](../entry-map.csv) when a form has no direct character or an alternate is required.

```css
@font-face {
  font-family: "Moira Astro";
  src: url("fonts/MoiraAstro-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
}
.astro-symbol {
  font-family: "Moira Astro";
  font-feature-settings: "dlig" 1;
}
```

For example, `[lot:Fo]` produces Fortune and `[lot:Sp]` produces the default circled-S Spirit. `[astro:tao]` selects the original 165-degree Tao design. `[astro:east-point]` selects East Point/equatorial Ascendant. Apply `dlig` to symbol runs; leave surrounding prose in its text font.

Microsoft Word requires discretionary or all ligatures. The 132 optional hyphen-free aliases in [aliases.csv](../aliases.csv) address observed Word token behavior; canonical spellings remain available. Each alias selects the same glyph as its canonical token. The current font preserves the layout rules tested in the preceding native Word export. No alias changes the underlying model or meaning.

Unslashed zero remains the default; enable OpenType `zero` for its slashed alternate. Historical and specialist forms may require explicit definition/model labels. Keep readable semantic text or accessible labels with the symbol: a glyph's visual form cannot replace those definitions. See [the presentation contract](PRESENTATION.md).

The font's selected repertoire has no new PUA allocation. Existing Unicode mappings retain their reference identities. The font does not calculate astronomical positions or choose a zodiac, lunar model or lot formula.
