// Copyright 2026 Moira Astro contributors. SIL OFL 1.1. Generated from fixtures.json by build-fixtures.py.
window.MOIRA_FIXTURES = {
  "schema_version": 1,
  "project": "Moira Astro",
  "font_version": "0.13.2-alpha.1",
  "license": "OFL-1.1",
  "copyright": "Copyright 2026 Moira Astro contributors. Original glyph designs.",
  "notice": "Declared layout fixtures. No ephemeris, natal-chart, native-model or lot-formula calculation.",
  "signs": [
    {
      "name": "Aries",
      "symbol": "♈"
    },
    {
      "name": "Taurus",
      "symbol": "♉"
    },
    {
      "name": "Gemini",
      "symbol": "♊"
    },
    {
      "name": "Cancer",
      "symbol": "♋"
    },
    {
      "name": "Leo",
      "symbol": "♌"
    },
    {
      "name": "Virgo",
      "symbol": "♍"
    },
    {
      "name": "Libra",
      "symbol": "♎"
    },
    {
      "name": "Scorpio",
      "symbol": "♏"
    },
    {
      "name": "Sagittarius",
      "symbol": "♐"
    },
    {
      "name": "Capricorn",
      "symbol": "♑"
    },
    {
      "name": "Aquarius",
      "symbol": "♒"
    },
    {
      "name": "Pisces",
      "symbol": "♓"
    }
  ],
  "motions": {
    "direct": {
      "label": "Direct",
      "symbol": "[astro:motion-direct]"
    },
    "retrograde": {
      "label": "Retrograde",
      "symbol": "[astro:motion-retrograde]"
    },
    "stationary": {
      "label": "Stationary",
      "symbol": "[astro:motion-stationary]"
    }
  },
  "aspectDefinitions": [
    {
      "id": "conjunction",
      "name": "Conjunction",
      "symbol": "☌",
      "angle": 0
    },
    {
      "id": "sextile",
      "name": "Sextile",
      "symbol": "⚹",
      "angle": 60
    },
    {
      "id": "square",
      "name": "Square",
      "symbol": "□",
      "angle": 90
    },
    {
      "id": "trine",
      "name": "Trine",
      "symbol": "△",
      "angle": 120
    },
    {
      "id": "opposition",
      "name": "Opposition",
      "symbol": "☍",
      "angle": 180
    }
  ],
  "aspect_rule": {
    "orb_limit": 2,
    "separation": "min(abs(a-b),360-abs(a-b))",
    "selection": "At most two closest examples per aspect family; diagram shows the same selected pairs."
  },
  "fixtures": [
    {
      "id": "balanced",
      "name": "Fixture A · distributed",
      "description": "Twelve declared positions distributed around the circle.",
      "sector_origin": 15,
      "sector_geometry": "Twelve equal 30-degree demonstration sectors; no computed house system.",
      "positions": [
        {
          "id": "sun",
          "name": "Sun",
          "symbol": "☉",
          "longitude": 15,
          "motion": "direct",
          "model": null,
          "short_name": "Sun"
        },
        {
          "id": "moon",
          "name": "Moon",
          "symbol": "☽",
          "longitude": 75.5,
          "motion": "direct",
          "model": null,
          "short_name": "Moon"
        },
        {
          "id": "mercury",
          "name": "Mercury",
          "symbol": "☿",
          "longitude": 16.2,
          "motion": "direct",
          "model": null,
          "short_name": "Mercury"
        },
        {
          "id": "venus",
          "name": "Venus",
          "symbol": "♀",
          "longitude": 105,
          "motion": "direct",
          "model": null,
          "short_name": "Venus"
        },
        {
          "id": "mars",
          "name": "Mars",
          "symbol": "♂",
          "longitude": 195.5,
          "motion": "direct",
          "model": null,
          "short_name": "Mars"
        },
        {
          "id": "jupiter",
          "name": "Jupiter",
          "symbol": "♃",
          "longitude": 135,
          "motion": "direct",
          "model": null,
          "short_name": "Jupiter"
        },
        {
          "id": "saturn",
          "name": "Saturn",
          "symbol": "♄",
          "longitude": 255.5,
          "motion": "retrograde",
          "model": null,
          "short_name": "Saturn"
        },
        {
          "id": "uranus",
          "name": "Uranus",
          "symbol": "♅",
          "longitude": 285,
          "motion": "stationary",
          "model": null,
          "short_name": "Uranus"
        },
        {
          "id": "neptune",
          "name": "Neptune",
          "symbol": "♆",
          "longitude": 345,
          "motion": "direct",
          "model": null,
          "short_name": "Neptune"
        },
        {
          "id": "pluto",
          "name": "Pluto",
          "symbol": "♇",
          "longitude": 225.5,
          "motion": "retrograde",
          "model": null,
          "short_name": "Pluto"
        },
        {
          "id": "north-node",
          "name": "North Node · mean",
          "symbol": "☊",
          "longitude": 45,
          "motion": "direct",
          "model": "mean ascending node",
          "short_name": "N. Node · mean"
        },
        {
          "id": "lilith",
          "name": "Lilith · mean apogee",
          "symbol": "[astro:lilith]",
          "longitude": 165,
          "motion": "direct",
          "model": "mean lunar apogee",
          "short_name": "Lilith · mean apogee"
        }
      ],
      "lots": [
        {
          "id": "lot.fortune",
          "name": "Fortune",
          "symbol": "[lot:Fo]",
          "longitude": 24.7,
          "meaning": "Lot of Fortune",
          "formula_selected": false
        },
        {
          "id": "lot.spirit",
          "name": "Spirit",
          "symbol": "[lot:Sp]",
          "longitude": 67.9,
          "meaning": "Lot of Spirit",
          "formula_selected": false
        },
        {
          "id": "lot.accomplishment",
          "name": "Accomplishment",
          "symbol": "[lot:Acc]",
          "longitude": 111.1,
          "meaning": "Lot of Accomplishment",
          "formula_selected": false
        },
        {
          "id": "lot.legalizing-contracts-marriage",
          "name": "Legalizing Contracts/Marriage",
          "symbol": "[lot:Lcm]",
          "longitude": 154.3,
          "meaning": "Lot of Legalizing Contracts/Marriage",
          "formula_selected": false
        },
        {
          "id": "lot.love-and-marriage",
          "name": "Love & Marriage",
          "symbol": "[lot:Lvm]",
          "longitude": 197.5,
          "meaning": "Lot of Love & Marriage",
          "formula_selected": false
        },
        {
          "id": "lot.play-activity-rapid-change",
          "name": "Play, Activity, Rapid Change",
          "symbol": "[lot:Parc]",
          "longitude": 240.7,
          "meaning": "Lot of Play, Activity, Rapid Change",
          "formula_selected": false
        }
      ],
      "minorBodies": [
        {
          "id": "fortuna",
          "name": "Fortuna",
          "symbol": "[astro:fortuna]",
          "longitude": 49.3,
          "em": 24
        },
        {
          "id": "makemake",
          "name": "Makemake",
          "symbol": "[astro:makemake]",
          "longitude": 121.1,
          "em": 24
        },
        {
          "id": "quaoar",
          "name": "Quaoar",
          "symbol": "[astro:quaoar]",
          "longitude": 192.9,
          "em": 24
        },
        {
          "id": "smallbody.lilith",
          "name": "(1181) Lilith",
          "symbol": "[astro:asteroid-1181-lilith]",
          "longitude": 264.7,
          "em": 24
        }
      ]
    },
    {
      "id": "crowded",
      "name": "Fixture B · crowded",
      "description": "Six bodies occupy a six-degree span; leader callouts retain their exact angle anchors.",
      "sector_origin": 15,
      "sector_geometry": "Twelve equal 30-degree demonstration sectors; no computed house system.",
      "positions": [
        {
          "id": "sun",
          "name": "Sun",
          "symbol": "☉",
          "longitude": 63,
          "motion": "direct",
          "model": null,
          "short_name": "Sun"
        },
        {
          "id": "moon",
          "name": "Moon",
          "symbol": "☽",
          "longitude": 69,
          "motion": "direct",
          "model": null,
          "short_name": "Moon"
        },
        {
          "id": "mercury",
          "name": "Mercury",
          "symbol": "☿",
          "longitude": 64.2,
          "motion": "direct",
          "model": null,
          "short_name": "Mercury"
        },
        {
          "id": "venus",
          "name": "Venus",
          "symbol": "♀",
          "longitude": 65.1,
          "motion": "direct",
          "model": null,
          "short_name": "Venus"
        },
        {
          "id": "mars",
          "name": "Mars",
          "symbol": "♂",
          "longitude": 66.3,
          "motion": "direct",
          "model": null,
          "short_name": "Mars"
        },
        {
          "id": "jupiter",
          "name": "Jupiter",
          "symbol": "♃",
          "longitude": 67.8,
          "motion": "direct",
          "model": null,
          "short_name": "Jupiter"
        },
        {
          "id": "saturn",
          "name": "Saturn",
          "symbol": "♄",
          "longitude": 190,
          "motion": "retrograde",
          "model": null,
          "short_name": "Saturn"
        },
        {
          "id": "uranus",
          "name": "Uranus",
          "symbol": "♅",
          "longitude": 260,
          "motion": "stationary",
          "model": null,
          "short_name": "Uranus"
        },
        {
          "id": "neptune",
          "name": "Neptune",
          "symbol": "♆",
          "longitude": 315,
          "motion": "direct",
          "model": null,
          "short_name": "Neptune"
        },
        {
          "id": "pluto",
          "name": "Pluto",
          "symbol": "♇",
          "longitude": 348,
          "motion": "retrograde",
          "model": null,
          "short_name": "Pluto"
        },
        {
          "id": "north-node",
          "name": "North Node · mean",
          "symbol": "☊",
          "longitude": 100,
          "motion": "direct",
          "model": "mean ascending node",
          "short_name": "N. Node · mean"
        },
        {
          "id": "lilith",
          "name": "Lilith · mean apogee",
          "symbol": "[astro:lilith]",
          "longitude": 220,
          "motion": "direct",
          "model": "mean lunar apogee",
          "short_name": "Lilith · mean apogee"
        }
      ],
      "lots": [
        {
          "id": "lot.fortune",
          "name": "Fortune",
          "symbol": "[lot:Fo]",
          "longitude": 42.1,
          "meaning": "Lot of Fortune",
          "formula_selected": false
        },
        {
          "id": "lot.spirit",
          "name": "Spirit",
          "symbol": "[lot:Sp]",
          "longitude": 85.3,
          "meaning": "Lot of Spirit",
          "formula_selected": false
        },
        {
          "id": "lot.accomplishment",
          "name": "Accomplishment",
          "symbol": "[lot:Acc]",
          "longitude": 128.5,
          "meaning": "Lot of Accomplishment",
          "formula_selected": false
        },
        {
          "id": "lot.legalizing-contracts-marriage",
          "name": "Legalizing Contracts/Marriage",
          "symbol": "[lot:Lcm]",
          "longitude": 171.7,
          "meaning": "Lot of Legalizing Contracts/Marriage",
          "formula_selected": false
        },
        {
          "id": "lot.love-and-marriage",
          "name": "Love & Marriage",
          "symbol": "[lot:Lvm]",
          "longitude": 214.9,
          "meaning": "Lot of Love & Marriage",
          "formula_selected": false
        },
        {
          "id": "lot.play-activity-rapid-change",
          "name": "Play, Activity, Rapid Change",
          "symbol": "[lot:Parc]",
          "longitude": 258.1,
          "meaning": "Lot of Play, Activity, Rapid Change",
          "formula_selected": false
        }
      ],
      "minorBodies": [
        {
          "id": "fortuna",
          "name": "Fortuna",
          "symbol": "[astro:fortuna]",
          "longitude": 61.8,
          "em": 24
        },
        {
          "id": "makemake",
          "name": "Makemake",
          "symbol": "[astro:makemake]",
          "longitude": 133.6,
          "em": 24
        },
        {
          "id": "quaoar",
          "name": "Quaoar",
          "symbol": "[astro:quaoar]",
          "longitude": 205.4,
          "em": 24
        },
        {
          "id": "smallbody.lilith",
          "name": "(1181) Lilith",
          "symbol": "[astro:asteroid-1181-lilith]",
          "longitude": 277.2,
          "em": 24
        }
      ]
    }
  ],
  "fixedStars": [
    {
      "id": "astro.star-sirius-1533-historical",
      "name": "Sirius",
      "symbol": "[astro:star-sirius-1533-historical]",
      "witness": "Agrippa 1533, II.52, printed p. CXCVII (197)",
      "variant": "historical",
      "em": 32
    },
    {
      "id": "astro.star-regulus-1533-historical",
      "name": "Regulus",
      "symbol": "[astro:star-regulus-1533-historical]",
      "witness": "Agrippa 1533, II.52, printed p. CXCVII (197)",
      "variant": "historical",
      "em": 32
    },
    {
      "id": "astro.star-vega-1533-historical",
      "name": "Vega",
      "symbol": "[astro:star-vega-1533-historical]",
      "witness": "Agrippa 1533, II.52, printed p. CXCVII (197)",
      "variant": "historical",
      "em": 32
    },
    {
      "id": "astro.star-regulus-1533-chart",
      "name": "Regulus",
      "symbol": "[astro:star-regulus-1533-chart]",
      "witness": "Agrippa 1533, II.52, printed p. CXCVII (197)",
      "variant": "chart",
      "em": 24
    }
  ],
  "satellites": [
    {
      "id": "satellite.mars.phobos",
      "name": "Phobos (Mars I)",
      "parent": "Mars",
      "roman": "I",
      "parent_text": "♂",
      "parent_em": 24,
      "label_em": 14,
      "gap_px": 4,
      "accessible_label": "Phobos (Mars I)"
    },
    {
      "id": "satellite.jupiter.callisto",
      "name": "Callisto (Jupiter IV)",
      "parent": "Jupiter",
      "roman": "IV",
      "parent_text": "♃",
      "parent_em": 24,
      "label_em": 14,
      "gap_px": 4,
      "accessible_label": "Callisto (Jupiter IV)"
    },
    {
      "id": "satellite.saturn.iapetus",
      "name": "Iapetus (Saturn VIII)",
      "parent": "Saturn",
      "roman": "VIII",
      "parent_text": "♄",
      "parent_em": 24,
      "label_em": 14,
      "gap_px": 4,
      "accessible_label": "Iapetus (Saturn VIII)"
    },
    {
      "id": "satellite.neptune.proteus",
      "name": "Proteus (Neptune VIII)",
      "parent": "Neptune",
      "roman": "VIII",
      "parent_text": "♆",
      "parent_em": 24,
      "label_em": 14,
      "gap_px": 4,
      "accessible_label": "Proteus (Neptune VIII)"
    }
  ],
  "specialistLegend": [
    {
      "name": "Tao",
      "symbol": "[astro:tao]",
      "angle": 165,
      "description": "Original Moira symbol · distinct from the existing 24-degree Quindecile."
    }
  ],
  "sizeSamples": [
    {
      "label": "14 px · stress",
      "em": 14,
      "symbol": "♑"
    },
    {
      "label": "18 px · general",
      "em": 18,
      "symbol": "♑"
    },
    {
      "label": "24 px · dense form",
      "em": 24,
      "symbol": "[astro:quaoar]"
    },
    {
      "label": "32 px · historical",
      "em": 32,
      "symbol": "[astro:star-sirius-1533-historical]"
    }
  ]
};
