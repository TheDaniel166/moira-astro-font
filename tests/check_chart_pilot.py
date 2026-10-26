# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
"""Independent fixture, source-generation, model-label and font-access checks."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from io import BytesIO
import hashlib,itertools,json,math,re,shutil,subprocess,tempfile
from fontTools.ttLib import TTFont
import uharfbuzz as hb

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'demo/chart-pilot/assets'
def read(p):return json.loads(Path(p).read_text('utf-8-sig'))

def run():
    checks=[]
    def check(name,ok):
        checks.append(dict(name=name,passed=bool(ok)))
        if not ok:raise AssertionError(name)
    data=read(ASSETS/'fixtures.json');registry=read(ROOT/'entry-map.json')
    tokens={e['token']:e for group in ['family_entries','extra_entries','batch_entries'] for e in registry[group]}
    check('Declared fixture notice',all(s in data['notice'].lower() for s in ['declared','no ephemeris','lot-formula']))
    check('Current source font version',data['font_version']==registry['version'])
    check('Two declared layouts',{f['id'] for f in data['fixtures']}=={'balanced','crowded'})
    check('Twelve zodiac reference characters',len(data['signs'])==12 and ''.join(s['symbol'] for s in data['signs'])=='♈♉♊♋♌♍♎♏♐♑♒♓')
    match=re.search(r'window\.MOIRA_FIXTURES\s*=\s*(\{.*\})\s*;', (ASSETS/'fixtures.js').read_text('utf-8'),re.S)
    check('Classic script payload equals canonical JSON',bool(match) and json.loads(match.group(1))==data)
    with tempfile.TemporaryDirectory(prefix='moira-chart-fixture-source-') as tmp:
        fresh=Path(tmp);target=fresh/'demo/chart-pilot/assets';target.mkdir(parents=True)
        shutil.copyfile(ASSETS/'build-fixtures.py',target/'build-fixtures.py')
        shutil.copyfile(ROOT/'entry-map.json',fresh/'entry-map.json')
        (fresh/'inventory').mkdir();shutil.copyfile(ROOT/'inventory/satellite-layouts.json',fresh/'inventory/satellite-layouts.json')
        subprocess.run([sys.executable,'-B',str(target/'build-fixtures.py')],check=True,capture_output=True,text=True)
        for name in ['fixtures.json','fixtures.js']:
            check('Deterministic fixture generator '+name,(target/name).read_bytes()==(ASSETS/name).read_bytes())
    core={'sun','moon','mercury','venus','mars','jupiter','saturn','uranus','neptune','pluto'}
    defs={a['id']:a for a in data['aspectDefinitions']}
    check('Major aspect angles',{k:v['angle'] for k,v in defs.items()}==dict(conjunction=0,sextile=60,square=90,trine=120,opposition=180))
    for fixture in data['fixtures']:
        fid=fixture['id'];positions=fixture['positions'];ids=[p['id'] for p in positions]
        check(fid+' full body set',len(ids)==len(set(ids))==12 and core<=set(ids))
        check(fid+' sectors declared as display geometry','demonstration' in fixture['sector_geometry'] and 'no computed house system' in fixture['sector_geometry'])
        for group in ['positions','lots','minorBodies']:
            for item in fixture[group]:
                x=item['longitude'];check(fid+' valid longitude '+item['id'],isinstance(x,(int,float)) and math.isfinite(x) and 0<=x<360)
        for p in positions:
            check(fid+' motion identity '+p['id'],p['motion'] in data['motions'])
            if p['id'] in {'north-node','lilith'}:check(fid+' explicit lunar model '+p['id'],bool(p['model']) and 'mean' in p['name'].lower())
        lots={e['symbol']:e for e in fixture['lots']}
        check(fid+' Fortune and circled-S Spirit routes',{'[lot:Fo]','[lot:Sp]'}<=set(lots))
        check(fid+' longer lot abbreviation',any(len(tokens[t].get('code',''))>=4 for t in lots))
        check(fid+' long readable lot label',any(len(e['name'])>=24 for e in lots.values()))
        for token,e in lots.items():
            check(fid+' lot definition '+token,e['formula_selected'] is False and e['meaning']==tokens[token]['accessible_label'] and e['name']==tokens[token]['name'])
        check(fid+' dense minor-body family',len(fixture['minorBodies'])>=4 and all(e['em']==24 for e in fixture['minorBodies']))
        pairs=[]
        for a,b in itertools.combinations(positions,2):
            delta=abs(a['longitude']-b['longitude']);sep=min(delta,360-delta)
            for aspect in data['aspectDefinitions']:
                if abs(sep-aspect['angle'])<=data['aspect_rule']['orb_limit']:
                    pairs.append(dict(a=a['id'],b=b['id'],aspect=aspect['id'],separation=sep,orb=abs(sep-aspect['angle'])))
        check(fid+' aspect examples exist',bool(pairs))
        if fid=='balanced':check('Distributed fixture exercises all major aspects',{p['aspect'] for p in pairs}==set(defs))
        if fid=='crowded':check('Crowded fixture has six bodies within six degrees',max(sum(0<=((p['longitude']-a['longitude'])%360)<=6 for p in positions) for a in positions)>=6)
    historical=[s for s in data['fixedStars'] if s['variant']=='historical']
    check('Three historical stars and a chart variant',len(historical)>=3 and any(s['variant']=='chart' for s in data['fixedStars']))
    for star in data['fixedStars']:
        entry=tokens[star['symbol']]
        check('Fixed-star witness '+star['symbol'],star['witness']==entry['witness'] and star['variant']==entry['variant'] and star['name']==entry['name'])
        check('Fixed-star size '+star['symbol'],star['em']==(32 if star['variant']=='historical' else 24))
    satellites={s['id']:s for s in read(ROOT/'inventory/satellite-layouts.json')['entries']}
    check('Four composed satellites',len(data['satellites'])>=4 and max(len(s['roman']) for s in data['satellites'])>=4)
    for sat in data['satellites']:
        check('Satellite identity and unchanged layout '+sat['id'],all(sat[k]==satellites[sat['id']][k] for k in sat) and sat['parent_em']==24 and sat['label_em']==14 and sat['gap_px']==4)
    check('Review/stress size strip',{s['em'] for s in data['sizeSamples']}=={14,18,24,32} and any(s['em']==14 and 'stress' in s['label'] for s in data['sizeSamples']))
    check('Tao qualifier',any(s['symbol']=='[astro:tao]' and s['angle']==165 and '24-degree Quindecile' in s['description'] for s in data['specialistLegend']))
    symbols=[]
    def collect(obj,path='fixture'):
        if isinstance(obj,dict):
            for k,v in obj.items():
                if k in {'symbol','parent_text'}:symbols.append((path+'.'+k,v))
                else:collect(v,path+'.'+k)
        elif isinstance(obj,list):
            for i,v in enumerate(obj):collect(v,path+'.'+str(i))
    collect(data)
    for fmt in ['ttf','woff2']:
        f=TTFont(ROOT/f'fonts/MoiraAstro-Regular.{fmt}',recalcTimestamp=False);f.flavor=None;sfnt=BytesIO();f.save(sfnt)
        font=hb.Font(hb.Face(sfnt.getvalue()));font.scale=(1000,1000);cmap=f.getBestCmap()
        for path,text in symbols:
            buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(font,buf,{'dlig':True})
            ids=[g.codepoint for g in buf.glyph_infos]
            check(fmt+' no missing glyph '+path,bool(ids) and 0 not in ids)
            expected=[f.getGlyphID(tokens[text]['glyph_name'])] if text in tokens else [f.getGlyphID(cmap[ord(c)]) for c in text]
            check(fmt+' exact route '+path,ids==expected)
        f.close()
    result=dict(status='PASS',checks=len(checks),fixture_symbol_cases=len(symbols),fixture_ids=[f['id'] for f in data['fixtures']],results=checks)
    dest=ROOT/'build/chart-pilot/fixture-checks.json';dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks):,} chart fixture checks; {len(symbols)} symbol cases in both containers; deterministic fixture source')
    return result

if __name__=='__main__':run()
