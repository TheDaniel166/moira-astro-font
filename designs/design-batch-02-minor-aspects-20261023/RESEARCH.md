# Remaining minor aspects - research and design decisions

23 October 2026 - Primary-source notation study; no engine/model changes

## Scope

Moira defines 22 longitude aspects: five major, six common-minor and eleven extended-minor. Four common-minor forms were drawn in Batch 01. This leaves **13 longitude forms**, including Quintile and Biquintile. The two native declination relations are reviewed separately, giving **15 native entries** here. The [coverage sheet](native-aspect-coverage.svg) represents all 24 native meanings using existing and new artwork.

This study concerns names, exact identities, notation and original drawings. An encoded character or an attested glyph is not evidence for an aspect's interpretive or empirical validity. Orbs and computational policy remain native data.

## 1. There is no single universal pictographic set for this group

Suignard's [2017 encoding analysis, table 3](https://www.unicode.org/wg2/docs/n4811-fdbk-extra-aspect-sym.pdf#page=3) distinguishes familiar basic aspect marks from the more variable harmonic notation. It documents letters and raised figures, as well as alternative geometric and Russian forms. The final [Unicode 17 NamesList](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt) explicitly notes V, N, Q, N² and D³ in annotations for corresponding Russian characters.

**Moira design recommendation:** use a coherent original letter family for the proposed defaults. Raised figures indicate the named multiple in this notation, rather than arithmetic exponentiation. Keep alternative traditions accessible and labeled. This is a design recommendation based on the observed conventions; it is not a claim that every astrologer uses these marks.

## 2. Preserve the native identity and its existing label separately

| Native aspect | Exact nominal angle | Existing native label | Proposed default study |
|---|---:|---|---|
| Quintile | 72° | Q | Q |
| Biquintile | 144° | bQ | Q² |
| Septile | 360/7° | S | S |
| Biseptile | 720/7° | bS | S² |
| Triseptile | 1080/7° | tS | S³ |
| Novile | 40° | N | N |
| Binovile | 80° | bN | N² |
| Quadnovile | 160° | qN | N⁴ |
| Decile | 36° | ⊼ | D |
| Tredecile | 108° | Td | D³ |
| Undecile | 360/11° | U | U |
| Quindecile | 24° | Qd | Qd |
| Vigintile | 18° | V | V |

The exact values and existing labels above are from [the frozen native source excerpt](references/native-aspect-definitions.txt). No original label, angle or orb is edited by a proposed display form. Qd follows that native source; the wider naming convention does not establish a universal Quindecile pictograph.

The source tables sometimes display rounded integers for Septile and Undecile. The artwork instead records the exact native fractions, with explicitly approximate decimal labels for orientation. Those decimals are presentation aids, not a calculation implementation.

## 3. Six Russian characters are separate encoded identities

Faulks's [revised 2016 proposal](https://www.unicode.org/L2/L2016/16174r-astrology-aspects.pdf) supplies chart/context evidence for the regional structures. The **final UCD** supplies the assignments:

| Final codepoint | Meaning | Status in this batch |
|---|---|---|
| U+2BF3 | Vigintile, 18° | Regional alternate study |
| U+2BF4 | Novile, 40° | Regional alternate study |
| U+2BF5 | Quintile, 72° | Regional alternate study |
| U+2BF6 | Binovile, 80° | Regional alternate study |
| U+2BF7 | Sentagon, 100° | Regional comparison; not a native aspect |
| U+2BF8 | Tredecile, 108° | Regional alternate study |

The old proposal's code positions are obsolete. Its six meanings are not six universal replacements for every convention. New paths retain the recognizable structures with Moira proportions, open counters and round terminals. The three denser Novile, Quintile and Binovile designs use a 56-unit optical stroke.

## 4. Sentagon contains a source conflict worth retaining

N4811's early table gives a 5/9 ratio; its later table gives 100° and 5/18. Those are inconsistent. The final NamesList explicitly identifies the encoded Sentagon as **100 degrees**. The regional proof uses that final identity and flags that the native catalog has no such aspect. It is never installed as a stylistic replacement for a differently angled native aspect. [Final annotation](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt), [conflicting proposal tables](https://www.unicode.org/wg2/docs/n4811-fdbk-extra-aspect-sym.pdf).

## 5. Decile needs a mapping distinction

The native label's character **U+22BC is NAND**, a logical operator. It is not a dedicated astrological Decile assignment. Suignard's notation table offers D and a contextual U+22A5 UP TACK form. Both are studied here; no engine label is changed. Mathematical identity and astrological contextual use must remain distinguishable in exported text. [Native excerpt](references/native-aspect-definitions.txt), [formal names](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt), [notation table](https://www.unicode.org/wg2/docs/n4811-fdbk-extra-aspect-sym.pdf#page=3).

## 6. Other useful alternatives also have limits

The comparison sheet includes a quintile pentagon and biquintile plus-over-minus, documented in the notation analysis. Pullen's [own aspect table](https://www.astrolog.org/astrolog/astdist.htm) also identifies Q, a plus/minus form, and numerical harmonic glyphs in Astrolog. Those are evidence of that program's convention, not a source of Moira outline geometry or a mandate for a universal default.

Four additional form studies here are therefore explicitly contextual: quintile pentagon, biquintile ±, decile up-tack and contra-parallel grid. Ordinary PLUS-MINUS, WHITE PENTAGON and UP TACK text must retain their normal character identities. No special mapping is assigned to the grid form.

## 7. Declination has multiple graphic conventions

The proposed pair uses two vertical lines and a slashed pair. Faulks's [2016 first-person encoding discussion](https://unicode.org/mail-arch/unicode-ml/y2016-m03/0075.html) reports this convention and variants. Pullen's [manual, `-gp` section](https://www.astrolog.org/ftp/astrolog.htm) describes a two-line parallel and grid-form contra-parallel. The grid is supplied as an alternate study.

Neither convention defines the calculation. Native Parallel requires the same nonzero hemisphere, except that two exactly equatorial points are also eligible. Native Contra-Parallel requires opposite nonzero hemispheres; one equatorial point is unclassified. The pair then uses the admitted tolerance policy. See the [frozen native declination excerpt](references/native-declination-definitions.txt). No longitude angle, assumed universal orb, NUMBER SIGN alias or box-drawing assignment is invented for them. U+2225/U+2226 remain contextual mathematical characters.

## 8. Other inventory research items remain distinct

N4811 table 1 does attest the names/fractions for Hexadecile (1/16), Seminovile (1/18) and Untion (1/24). That resolves a naming-evidence lead from the inventory, but does not establish unique default drawings or admit those aspects to the native set. The separate 165-degree Quindecile convention also remains outside this design batch. This task preserves native Quindecile at 24°.

The local book database was searched by relevant author/title filenames; no matching harmonic-notation volume was identified in that pass. No uninspected historical book is cited as authority. A Pearce scan link and the old Noel Tyl page could not be retrieved; neither is used as primary evidence in this report.

## Encoding and release consequence

Letters and superscripts are ordinary text components, not newly assigned astrological scalars or registered variation sequences. Composite SVGs study optical placement only; a later font build must decide component advances, optional feature access and shaping without corrupting copied text. Regional characters keep their own assignments. No private-use allocation, ASCII remapping, feature slot, model change or font integration is performed here.

The next decision is the owner's shape/convention review. Inspect the raised figures, Qd counters and dense regional forms at 14/18 px before selecting forms for an actual font proof.
