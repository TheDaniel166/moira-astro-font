# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see ../../../OFL.txt.
"""Generate declared, non-ephemeris review fixtures and the file:// script copy."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
registry=json.loads((ROOT/'entry-map.json').read_text('utf-8'))
entries=registry['family_entries']+registry['extra_entries']+registry['batch_entries']
by_token={e['token']:e for e in entries}
satellites=json.loads((ROOT/'inventory/satellite-layouts.json').read_text('utf-8'))['entries']
core=[('sun','Sun','☉'),('moon','Moon','☽'),('mercury','Mercury','☿'),('venus','Venus','♀'),('mars','Mars','♂'),('jupiter','Jupiter','♃'),('saturn','Saturn','♄'),('uranus','Uranus','♅'),('neptune','Neptune','♆'),('pluto','Pluto','♇'),('north-node','North Node · mean','☊'),('lilith','Lilith · mean apogee','[astro:lilith]')]
longitudes={'balanced':[15,75.5,16.2,105,195.5,135,255.5,285,345,225.5,45,165],
            'crowded':[63,69,64.2,65.1,66.3,67.8,190,260,315,348,100,220]}
fixtures=[]
for n,key in enumerate(['balanced','crowded']):
    positions=[]
    for i,((id,name,symbol),longitude) in enumerate(zip(core,longitudes[key])):
        motion='retrograde' if id in ['saturn','pluto'] else 'stationary' if id=='uranus' else 'direct'
        positions.append(dict(id=id,name=name,symbol=symbol,longitude=longitude,motion=motion,
            model='mean ascending node' if id=='north-node' else 'mean lunar apogee' if id=='lilith' else None,
            short_name='N. Node · mean' if id=='north-node' else name))
    lots=[]
    for i,token in enumerate(['[lot:Fo]','[lot:Sp]','[lot:Acc]','[lot:Lcm]','[lot:Lvm]','[lot:Parc]']):
        e=by_token[token];lots.append(dict(id=e['family_id'],name=e['name'],symbol=token,
            longitude=round((24.7+i*43.2+n*17.4)%360,1),meaning=e.get('accessible_label') or 'Lot of '+e['name'],formula_selected=False))
    minors=[]
    for i,token in enumerate(['[astro:fortuna]','[astro:makemake]','[astro:quaoar]','[astro:asteroid-1181-lilith]']):
        e=by_token[token];minors.append(dict(id=e.get('id') or token,name=e['name'],symbol=token,
            longitude=round((49.3+i*71.8+n*12.5)%360,1),em=24))
    fixtures.append(dict(id=key,name='Fixture A · distributed' if n==0 else 'Fixture B · crowded',
        description='Twelve declared positions distributed around the circle.' if n==0 else 'Six bodies occupy a six-degree span; leader callouts retain their exact angle anchors.',
        sector_origin=15,sector_geometry='Twelve equal 30-degree demonstration sectors; no computed house system.',positions=positions,lots=lots,minorBodies=minors))
stars=[]
for token in ['[astro:star-sirius-1533-historical]','[astro:star-regulus-1533-historical]','[astro:star-vega-1533-historical]','[astro:star-regulus-1533-chart]']:
    e=by_token[token];stars.append(dict(id=e['glyph_name'],name=e['name'],symbol=token,witness=e['witness'],variant=e['variant'],em=32 if e['variant']=='historical' else 24))
data=dict(schema_version=1,project='Moira Astro',font_version='0.14.0-alpha.1',license='OFL-1.1',
    copyright='Copyright 2026 Moira Astro contributors. Original glyph designs.',
    notice='Declared layout fixtures. No ephemeris, natal-chart, native-model or lot-formula calculation.',
    signs=[dict(name=n,symbol=s) for n,s in zip(['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces'],'♈♉♊♋♌♍♎♏♐♑♒♓')],
    motions={key:dict(label=key.title(),symbol='[astro:motion-'+key+']') for key in ['direct','retrograde','stationary']},
    aspectDefinitions=[dict(id=id,name=name,symbol=symbol,angle=angle) for id,name,symbol,angle in [('conjunction','Conjunction','☌',0),('sextile','Sextile','⚹',60),('square','Square','□',90),('trine','Trine','△',120),('opposition','Opposition','☍',180)]],
    aspect_rule=dict(orb_limit=2,separation='min(abs(a-b),360-abs(a-b))',selection='At most two closest examples per aspect family; diagram shows the same selected pairs.'),
    fixtures=fixtures,fixedStars=stars,
    satellites=[{k:e[k] for k in ['id','name','parent','roman','parent_text','parent_em','label_em','gap_px','accessible_label']} for e in satellites if e['id'] in ['satellite.mars.phobos','satellite.jupiter.callisto','satellite.saturn.iapetus','satellite.neptune.proteus']],
    specialistLegend=[dict(name='Tao',symbol='[astro:tao]',angle=165,description='Original Moira symbol · distinct from the existing 24-degree Quindecile.')],
    sizeSamples=[dict(label='14 px · stress',em=14,symbol='♑'),dict(label='18 px · general',em=18,symbol='♑'),dict(label='24 px · dense form',em=24,symbol='[astro:quaoar]'),dict(label='32 px · historical',em=32,symbol='[astro:star-sirius-1533-historical]')])
text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
(HERE/'fixtures.json').write_text(text,encoding='utf-8',newline='\n')
(HERE/'fixtures.js').write_text('// Copyright 2026 Moira Astro contributors. SIL OFL 1.1. Generated from fixtures.json by build-fixtures.py.\nwindow.MOIRA_FIXTURES = '+text.rstrip()+';\n',encoding='utf-8',newline='\n')
print('Generated both declared review fixtures and exact file:// script copy')
