# Batch 23 design decisions

9 November 2026 · twenty new compositions · integrated in 0.14.0-alpha.1

1. **Extend the notation already in the font.** Batch 02 established a base letter with a raised figure naming the multiple (Q², S³, N⁴). Seventeen of these twenty forms apply that rule to an existing base.
2. **Count from the base the angle actually divides.** Trivigintile is three vigintiles, V³. Squile and Squine are five and seven untions. Sesquioctile, Quinsemioctile and Septsemioctile are three, five and seven hexadeciles of 22.5°.
3. **Add one new base.** The font had no 25.71° form. Semiseptile is a small s before S, the same reading as the label sS. A slashed S was rejected because it reads as a dollar sign. Its multiples take a raised 3 and 5.
4. **Keep Quinseminovile separate from Russian Sentagon.** Both are 100°. The existing Russian Sentagon form is unchanged, and Quinseminovile stays with the seminovile family it counts from.
5. **Add raised 5, 7 and 9.** They follow the stroke, height and position of the existing raised 2, 3 and 4.
6. **Offer token access only.** Each form has an `[astro:name]` discretionary token. No Unicode or private-use mapping is allocated, and nothing is selected by default.

## Geometry

Masters use the 1,000-unit box with round caps and joins. Bases keep the stroke of the form they extend (60 or 64). Raised figures use 58. Bases sit further left than their standalone forms, so the figure has its own space, as in Q². Font outlines use the same scale as earlier forms: 1.08 × master units, with 900 as the master-to-font vertical origin and optical side bearings of 80 and 81.

## Chart use

Qd with a raised figure is the densest form in this batch and is the first to close up at small sizes. Keep the full name and angle available wherever these marks appear.
