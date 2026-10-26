# Native model and semantic boundaries

This packet defines graphic proposals. It does not import or execute the engine, select an ephemeris, modify a lunar model or settle the earlier East Point projection question.

Every record retains `native_model_modified: false`, `model_selected_by_font: false` and a complete `definition_policy`. Required metadata is definition ID, tradition/model, frame, equinox/epoch and provider/source version. Interpolated apsides additionally require a stated method. Timashev-qualified Arta additionally retains the lunar-apogee model, lunar-node model, solar-apogee definition and phase/branch choice. No formula or branch is implemented here.

The lunar bar/diamond/bridge are original notation cues for separate semantic records. A font-style selection cannot turn one calculation into another. A mean/osculating opposition relation applies only within the selected common model or ellipse; no universal opposition relation is assumed for interpolated apsides.

White Moon Selena, Timashev's Arta, hypothetical Proserpina, Waldemath's Moon and intramercurial Vulcan retain qualified identities. No physical body or native computation is admitted by drawing one. Physical asteroid Proserpina, asteroid Lilith, lunar-apogee Lilith and Hamburg Vulkanus keep their existing identities and routes. Ophiuchus changes no twelve-sign model.

Current 0.12.0 TTF/WOFF2 are opened read-only for fingerprints, existing maps and relevant route checks. They remain 713 glyphs with 221 cmap characters. No new Unicode, PUA, token, feature, installation or publication occurs. [Preservation evidence](PRESERVATION.md).
