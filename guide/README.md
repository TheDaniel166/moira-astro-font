# Character guide and picker

Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see [OFL.txt](../OFL.txt).

Open [index.html](index.html) locally, or serve the repository and visit `/guide/`. The guide uses local fonts and an exact classic-script copy of the generated catalog, so it works under `file://` without fetching JSON.

Search by name, meaning, Unicode notation, character or exact token. Filter by category, choose a preview size, compare TTF/WOFF2 and switch themes. Results are paginated. Select a form to read the meaning, model/context notes, witness, related forms and available copy routes. Desktop details remain beside the index; narrower layouts use an accessible native dialog with Escape and focus return.

The picker copies the exact route value. Unicode characters, discretionary-ligature tokens, Word aliases, text-presentation sequences and feature-only routes are labelled separately. If automatic copying is denied, a readonly selected value supports manual copying. Character identity and drawing do not select a native model or lot formula. The zero alternate retains its required feature, and blank spacing routes retain explicit names/codepoints.

The data generator and catalog tests are maintained by the project. `assets/catalog.json` is canonical; `assets/catalog.js` supplies the same data as `window.MOIRA_CATALOG`. No glyph drawing, Unicode allocation or native model changes are made by this guide.

Browser verification uses `window.MOIRA_GUIDE.ready`, `getState()`, async `setState()` and `measure()`. The state helper calls the same rendering logic as the native controls. Exact font runs expose `data-font-symbol`, `data-entry-id`, `data-role`, `data-dlig` and `data-zero`. The selected preview has `data-role="detail"`; encoded route displays use separate `route-*` roles. Route-copy controls expose `data-copy-route`; the manual field is `#manual-copy-value`.

State includes visible/result ids, dialog state, copy status and a local `lastCopy` receipt containing the route id, value, method and success flag. That receipt records only a value supplied by the guide; it never reads the user's clipboard. Copy success appears beside the action, while denied copying exposes the selected readonly value. A selected form outside the current filters has an explicit notice and a return-to-results action. URL fragments identify selected forms, and browser history restores them.
