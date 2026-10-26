# Moira Astro 0.13.2-alpha.1

Copyright 2026 Moira Astro contributors. Original glyph designs.
with Reserved Font Name Moira.
Licensed under SIL Open Font License 1.1. See OFL.txt and https://openfontlicense.org/

Moira Astro is an original astrology symbol font. This OFL package preserves the stabilized repertoire: **726 glyphs, 225 mapped characters, 711 optional tokens and 35 direct-character registry routes**. It adds licensing metadata and a complete editable source export. No glyph drawing, native calculation, historical variant or existing access spelling changes.

- [TTF](fonts/MoiraAstro-Regular.ttf) for desktop applications.
- [WOFF2](fonts/MoiraAstro-Regular.woff2) for the web.
- [Specimen](index.html), [entry map](entry-map.csv), [JSON registry](entry-map.json) and [132 compatibility aliases](aliases.csv).
- [License](OFL.txt), [notices](NOTICE.md), [font log](FONTLOG.txt), [checks](CHECKS.md) and [package checksums](SHA256SUMS.txt).

The license is SIL Open Font License 1.1, with **Moira** declared as the Reserved Font Name. The existing copyright holder string is retained. Modified versions distributed by other parties must respect the OFL's reserved-name condition. The full OFL text is embedded in name ID 13; name ID 14 links to the OFL website. OS/2.fsType remains 0. See the [official license](https://openfontlicense.org/open-font-license-official-text/) and [Reserved Font Name guidance](https://openfontlicense.org/ofl-reserved-font-names/).

## Using the symbols

Direct Unicode characters work without optional ligatures. Exact tokens are case-sensitive and require discretionary ligatures (`dlig`). Enable the feature on the runs intended as symbols. The `zero` feature chooses the existing slashed-zero alternate; unslashed zero remains the default.

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

The 132 optional aliases remove hyphens from their canonical tokens to address the observed Microsoft Word token behavior. Both spellings remain valid; see `aliases.json`. Word requires discretionary ligatures (or all ligatures). These aliases were validated in the preceding 0.13.1 stabilization candidate. This licensing build preserves its exact GSUB data. It does not add another native Word export certification.

Use 18 px as the general reviewed starting size; use 24 px for dense forms and 32 px with the name and witness for historical fixed-star sigils. A 14 px rendering is a stress case. Preserve explicit model labels for shared lunar icons, and context labels where letter-like symbols overlap. Satellite component layouts require the parent symbol plus a Roman designation, rather than implying 27 new satellite emblems. Full semantic and source policies are retained in the entry registry; historical SVG/research packets remain separate frozen design records.

Font appearance never selects a calculation model or a lot formula. Ophiuchus does not alter the native twelve-sign zodiac. Fortune, circled-S Spirit, 24-degree Quindecile and the existing historical variants retain their routes and shapes.

## Editable source and reproducible builds

`source/MoiraAstro-Regular.ttx` is the complete, editable FontTools XML representation of this font: outlines, hinting, metrics, mappings, OpenType rules and name metadata. It is a source export of the compiled masters; it is not a replacement for the archived original SVG design/research history. Every font table can be edited and rebuilt without access to earlier packets or a local binary seed.

Use Python 3 with the pinned dependencies:

```text
python -m pip install -r requirements.txt
python -B build.py
python -B validate.py
```

`build.py --output PATH` writes both containers to another folder. `validate.py` builds twice in temporary directories, checks the shipped bytes, embedded license and frozen glyph/encoding/shaping contract, and writes `checks.json`. The frozen contract is a regression receipt for the original repertoire; update it intentionally when designing a subsequent release. Font changes by other distributors must follow the OFL naming conditions.

This is a prepared alpha distribution package. No public upload, global font installation or repository publication is implied. Existing stabilization results are dated evidence for the unchanged drawings and shaping rules; they do not certify every application, rasterizer or physical printer.
