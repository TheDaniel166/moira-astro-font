# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
"""Verify independent browser measurements and exact TTF/WOFF2 glyph pixels."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from io import BytesIO
import hashlib,itertools,json,math
from PIL import Image,ImageChops
from fontTools.ttLib import TTFont
import uharfbuzz as hb

ROOT=Path(__file__).resolve().parents[1];REVIEW=ROOT/'build/chart-pilot'
def read(p):return json.loads(Path(p).read_text('utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def inside(a,b,tolerance=.1):return a['x']>=b['x']-tolerance and a['y']>=b['y']-tolerance and a['x']+a['width']<=b['x']+b['width']+tolerance and a['y']+a['height']<=b['y']+b['height']+tolerance
def overlap(a,b):return min(a['x']+a['width'],b['x']+b['width'])-max(a['x'],b['x'])>.1 and min(a['y']+a['height'],b['y']+b['height'])-max(a['y'],b['y'])>.1

def run():
    checks=[]
    def check(name,ok):
        checks.append(dict(name=name,passed=bool(ok)))
        if not ok:raise AssertionError(name)
    evidence=read(REVIEW/'browser-captures.json');fixtures=read(ROOT/'demo/chart-pilot/assets/fixtures.json')
    by_fixture={f['id']:f for f in fixtures['fixtures']}
    for item in evidence['inputs']:check('Fresh browser input '+item['path'],sha(ROOT/item['path'])==item['sha256'])
    captures=evidence['captures']
    check('Complete 24-state matrix',{(c['width'],c['fixture'],c['theme'],c['format']) for c in captures}==set(itertools.product([1360,768,390],['balanced','crowded'],['light','dark'],['ttf','woff2'])))
    font=TTFont(ROOT/'fonts/MoiraAstro-Regular.ttf',recalcTimestamp=False);buf=BytesIO();font.save(buf)
    hbfont=hb.Font(hb.Face(buf.getvalue()));hbfont.scale=(1000,1000);cache={}
    def shape(text):
        if text not in cache:
            b=hb.Buffer();b.add_str(text);b.guess_segment_properties();hb.shape(hbfont,b,{'dlig':True})
            cache[text]=([i.codepoint for i in b.glyph_infos],sum(p.x_advance for p in b.glyph_positions))
        return cache[text]
    advances=anchors=aspect_rows=callout_pairs=satellite_cases=0
    for capture in captures:
        key=f"{capture['width']}/{capture['fixture']}/{capture['theme']}/{capture['format']}";proof=capture['proof']
        check(key+' screenshot fingerprint',sha(ROOT/capture['capture'])==capture['captureSha256'])
        check(key+' ready with no body overflow',proof['ready'] and not proof['bodyOverflow'] and proof['viewport']['width']==capture['width'])
        check(key+' controls/state match',all(proof['state'][k]==capture[k] for k in ['fixture','theme','format']))
        check(key+' both font containers loaded',len(proof['fonts'])==2 and all(f['status']=='loaded' for f in proof['fonts']))
        check(key+' fixture provenance visible','declared layout fixtures' in proof['visibleText'].lower() and 'no ephemeris' in proof['visibleText'].lower())
        check(key+' model and context labels visible',all(t in proof['visibleText'] for t in ['mean ascending node','mean lunar apogee','Direct','Retrograde','Stationary','24-degree Quindecile']))
        for s in proof['symbols']:
            tag=key+' symbol '+str(s['index'])+' '+s['source'];ids,width=shape(s['source'])
            check(tag+' source retained',s['text']==s['source'])
            check(tag+' no .notdef',bool(ids) and 0 not in ids)
            check(tag+' real selected font',s['family']=='MoiraTTF' if capture['format']=='ttf' else s['family']=='MoiraWOFF')
            check(tag+' advance',abs(s['advance']-width*s['actualFontSize']/1000)<.04);advances+=1
            check(tag+' reviewed screen size',s['actualFontSize']>=17.99 or (s['role']=='size-sample' and abs(s['actualFontSize']-14)<.01))
            if s['cell']:
                check(tag+' complete run fits cell',s['box']['x']>=s['cell']['x']-.1 and s['box']['x']+s['box']['width']<=s['cell']['x']+s['cell']['width']+.1)
        check(key+' full chart labels',len(proof['labels'])==len(proof['callouts'])==12 and len(proof['charts'])==1)
        for label in proof['labels']:check(key+' chart label within SVG '+label['id'],inside(label['box'],proof['charts'][0]['box']))
        for a,b in itertools.combinations(proof['labels'],2):
            check(key+' separated labels '+a['id']+'/'+b['id'],not overlap(a['box'],b['box']));callout_pairs+=1
        fixture=by_fixture[capture['fixture']];positions={p['id']:p for p in fixture['positions']};wheel=proof['wheel']
        check(key+' complete true-angle anchors',{a['id'] for a in proof['anchors']}==set(positions))
        for anchor in proof['anchors']:
            value=positions[anchor['id']]['longitude'];angle=math.radians(180-(value-fixture['sector_origin']))
            check(key+' declared anchor '+anchor['id'],anchor['longitude']==value and abs(anchor['x']-(wheel['centerX']+wheel['radius']*math.cos(angle)))<1e-8 and abs(anchor['y']-(wheel['centerY']+wheel['radius']*math.sin(angle)))<1e-8);anchors+=1
        expected=[]
        for definition in fixtures['aspectDefinitions']:
            found=[]
            for a,b in itertools.combinations(fixture['positions'],2):
                d=abs(a['longitude']-b['longitude']);sep=min(d,360-d);orb=abs(sep-definition['angle'])
                if orb<=fixtures['aspect_rule']['orb_limit']+1e-9:found.append((orb,a['id'],b['id'],definition['id'],sep))
            expected.extend(sorted(found)[:2])
        actual={(r['aspect'],r['a'],r['b']) for r in proof['aspectRows']}
        check(key+' selected aspect families/pairs',actual=={(a[3],a[1],a[2]) for a in expected})
        check(key+' wheel/table same aspect pairs',set(proof['aspectLines'])=={r['a']+':'+r['b'] for r in proof['aspectRows']})
        for row in proof['aspectRows']:
            a,b=positions[row['a']]['longitude'],positions[row['b']]['longitude'];d=abs(a-b);sep=min(d,360-d)
            angle=next(v['angle'] for v in fixtures['aspectDefinitions'] if v['id']==row['aspect'])
            check(key+' displayed aspect arithmetic '+row['a']+'/'+row['b'],abs(row['separation']-sep)<1e-8 and abs(row['orb']-abs(sep-angle))<1e-8);aspect_rows+=1
        for sat in proof['satellites']:
            original=next(s for s in fixtures['satellites'] if s['id']==sat['id'])
            check(key+' satellite composition '+sat['id'],sat['label']==original['accessible_label'] and sat['romanText']==original['roman'] and sat['align']=='baseline' and sat['parentSize']==24 and sat['romanSize']==14 and sat['gap']==4 and abs(sat['roman']['x']-sat['parent']['x']-sat['parent']['width']-4)<.03);satellite_cases+=1
    pairs={}
    for capture in captures:pairs.setdefault((capture['width'],capture['fixture'],capture['theme']),{})[capture['format']]=capture
    pixel_cases=0
    for key,pair in pairs.items():
        a,b=pair['ttf'],pair['woff2'];aa,bb=a['proof']['symbols'],b['proof']['symbols']
        check(str(key)+' format coverage',len(aa)==len(bb))
        with Image.open(ROOT/a['capture']) as im_a,Image.open(ROOT/b['capture']) as im_b:
            for x,y in zip(aa,bb):
                label=str(key)+' parity '+str(x['index'])+' '+x['source']
                check(label+' same run',x['source']==y['source'] and x['role']==y['role'] and abs(x['advance']-y['advance'])<.001)
                check(label+' same placement',all(abs(x['box'][k]-y['box'][k])<.01 for k in ['x','y','width','height']))
                box=x['box'];crop=(math.floor(box['x'])-2,math.floor(box['y'])-2,math.ceil(box['x']+box['width'])+2,math.ceil(box['y']+box['height'])+2)
                check(label+' exact Chromium pixels',ImageChops.difference(im_a.crop(crop).convert('RGB'),im_b.crop(crop).convert('RGB')).getbbox() is None);pixel_cases+=1
    result=dict(status='PASS',checks=len(checks),browser_states=len(captures),glyph_advance_checks=advances,
        true_angle_anchors=anchors,aspect_arithmetic_rows=aspect_rows,label_pair_collision_checks=callout_pairs,
        satellite_compositions=satellite_cases,exact_container_pixel_cases=pixel_cases,
        inputs=evidence['inputs'],results=checks)
    (REVIEW/'browser-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(captures)} browser states, {advances:,} advances, {anchors} true anchors, {pixel_cases:,} exact glyph-pixel comparisons')
    return result

if __name__=='__main__':run()
