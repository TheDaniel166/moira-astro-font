# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
"""Independently check guide rendering, exact route copying and usage examples."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from io import BytesIO
from html.parser import HTMLParser
from PIL import Image,ImageChops
import hashlib,itertools,json,math,unicodedata
from fontTools.ttLib import TTFont
import uharfbuzz as hb

ROOT=Path(__file__).resolve().parents[1];REVIEW=ROOT/'build/character-guide'
def read(p):return json.loads(Path(p).read_text('utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fold(text):return ''.join(c for c in unicodedata.normalize('NFKD',text).lower() if not unicodedata.combining(c))

def run():
    checks=[]
    def check(name,ok):
        checks.append(dict(name=name,passed=bool(ok)))
        if not ok:raise AssertionError(name)
    evidence=read(REVIEW/'browser-captures.json');catalog=read(ROOT/'guide/assets/catalog.json');by_id={e['id']:e for e in catalog['entries']}
    for item in evidence['inputs']:check('Fresh browser input '+item['path'],sha(ROOT/item['path'])==item['sha256'])
    captures=evidence['captures']
    check('48 complete browser states',{(c['width'],c['scene'],c['theme'],c['format']) for c in captures}==set(itertools.product([1360,768,390],['index','long-lot','historical','zero'],['light','dark'],['ttf','woff2'])))
    f=TTFont(ROOT/'fonts/MoiraAstro-Regular.ttf',recalcTimestamp=False);sfnt=BytesIO();f.save(sfnt)
    font=hb.Font(hb.Face(sfnt.getvalue()));font.scale=(1000,1000);cache={}
    def shape(text,dlig,zero):
        key=(text,dlig,zero)
        if key not in cache:
            b=hb.Buffer();b.add_str(text);b.guess_segment_properties();hb.shape(font,b,{'dlig':dlig,'zero':zero})
            cache[key]=([g.codepoint for g in b.glyph_infos],sum(p.x_advance for p in b.glyph_positions))
        return cache[key]
    advances=0
    for capture in captures:
        key=f"{capture['width']}/{capture['scene']}/{capture['theme']}/{capture['format']}";proof=capture['proof'];state=proof['state']
        check(key+' screenshot hash',sha(ROOT/capture['capture'])==capture['sha256'])
        check(key+' real fonts/data ready',proof['ready'] and len(proof['fonts'])==2 and all(x['status']=='loaded' for x in proof['fonts']))
        check(key+' contained layout',not proof['bodyOverflow'] and proof['viewport']['width']==capture['width'])
        check(key+' selected controls match',state['selected']==capture['selected'] and state['theme']==capture['theme'] and state['format']==capture['format'] and state['size']==capture['size'])
        terms=fold(state['query']).split()
        expected=[e['id'] for e in catalog['entries'] if (state['category']=='all' or e['category']==state['category']) and all(t in fold(e['search_text']) for t in terms)]
        check(key+' result identities/order',state['resultIds']==expected)
        check(key+' pagination',state['visibleIds']==expected[:state['limit']])
        check(key+' detail has named identity',by_id[state['selected']]['name'] in proof['detailText'])
        if capture['width']<1000:check(key+' accessible contained dialog',proof['dialog']['open'] and proof['dialog']['box']['x']>=0 and proof['dialog']['box']['x']+proof['dialog']['box']['width']<=capture['width']+.1)
        for s in proof['symbols']:
            tag=key+' '+s['entry']+'/'+s['role'];entry=by_id[s['entry']];ids,width=shape(s['text'],s['dlig'],s['zero'])
            check(tag+' exact form',ids==[f.getGlyphID(entry['glyph_name'])])
            check(tag+' actual selected face',s['family']==('MoiraTTF' if capture['format']=='ttf' else 'MoiraWOFF'))
            check(tag+' advance',abs(s['advance']-width*s['size']/1000)<.045);advances+=1
            if s['surface']:check(tag+' complete horizontal run',s['box']['x']>=s['surface']['x']-.1 and s['box']['x']+s['box']['width']<=s['surface']['x']+s['surface']['width']+.1)
            if s['role']=='detail':check(tag+' correct source/features',s['text']==entry['preview']['text'] and s['dlig']==entry['preview']['features']['dlig'] and s['zero']==entry['preview']['features']['zero'] and s['size']==state['size'])
        if capture['scene']=='historical':check(key+' historical witness and stress label',by_id[state['selected']]['witness'] in proof['detailText'] and 'stress' in proof['detailText'].lower())
        if capture['scene']=='zero':check(key+' feature-only explanation','base character' in proof['detailText'].lower() and 'zero' in proof['cssExample'])
    pairs={}
    for c in captures:pairs.setdefault((c['width'],c['scene'],c['theme']),{})[c['format']]=c
    pixel_cases=0
    for key,pair in pairs.items():
        a,b=pair['ttf'],pair['woff2'];aa,bb=a['proof']['symbols'],b['proof']['symbols']
        check(str(key)+' equal symbol coverage',len(aa)==len(bb))
        with Image.open(ROOT/a['capture']) as ia,Image.open(ROOT/b['capture']) as ib:
            for index,(x,y) in enumerate(zip(aa,bb)):
                tag=str(key)+' '+str(index)+' '+x['entry']+'/'+x['role']
                check(tag+' identical source',all(x[k]==y[k] for k in ['text','entry','role','dlig','zero','size']))
                check(tag+' identical advance',abs(x['advance']-y['advance'])<.001)
                if x['clipped'] or y['clipped'] or x['occludedByDialog'] or y['occludedByDialog']:continue
                check(tag+' identical placement',all(abs(x['box'][k]-y['box'][k])<.02 for k in ['x','y','width','height']))
                box=x['box'];crop=(math.floor(box['x'])-1,math.floor(box['y'])-1,math.ceil(box['x']+box['width'])+1,math.ceil(box['y']+box['height'])+1)
                check(tag+' exact Chromium pixels',ImageChops.difference(ia.crop(crop).convert('RGB'),ib.crop(crop).convert('RGB')).getbbox() is None);pixel_cases+=1
    class Example(HTMLParser):
        def __init__(self):super().__init__();self.text=[];self.label=None
        def handle_data(self,data):self.text.append(data)
        def handle_starttag(self,tag,attrs):
            if tag=='span':self.label=dict(attrs).get('aria-label')
    bulk=evidence['bulk'];check('All 725 browser detail flows',{r['id'] for r in bulk}==set(by_id) and len(bulk)==725)
    copy_count=0
    for row in bulk:
        entry=by_id[row['id']];preview=entry['preview'];tag='Bulk '+entry['id']
        ids,width=shape(row['text'],row['dlig'],row['zero'])
        check(tag+' detail source/features',row['text']==preview['text'] and row['dlig']==preview['features']['dlig'] and row['zero']==preview['features']['zero'])
        check(tag+' actual font and glyph',row['family']=='MoiraWOFF' and ids==[f.getGlyphID(entry['glyph_name'])])
        check(tag+' browser advance',abs(row['advance']-width*row['size']/1000)<.045)
        routes={r['id']:r for r in entry['routes']};check(tag+' complete copy coverage',{c['route'] for c in row['copies']}==set(routes) and len(row['copies'])==len(routes))
        for copy in row['copies']:
            route=routes[copy['route']];receipt=copy['receipt']
            check(tag+' exact copied text '+route['id'],copy['value']==route['text'] and receipt['text']==route['text'] and receipt['routeId']==route['id'] and receipt['success'] is True and receipt['method']=='clipboard');copy_count+=1
        route=next((r for r in entry['routes'] if r['kind']=='unicode'),None) or next((r for r in entry['routes'] if r['kind']=='token'),None) or entry['routes'][0]
        parsed=Example();parsed.feed(row['htmlExample'])
        check(tag+' HTML preserves exact text/name',''.join(parsed.text)==route['text'] and parsed.label==entry['name'])
        css=row['cssExample']
        check(tag+' CSS preserves features',f'"dlig" {int(route["features"]["dlig"])}' in css and f'"zero" {int(route["features"]["zero"])}' in css)
        check(tag+' CSS preserves font style/whitespace',all(value in css for value in ['font-style: normal','font-weight: 400','font-synthesis: none','white-space: pre']))
    result=dict(status='PASS',checks=len(checks),browser_states=len(captures),visible_advance_checks=advances,exact_container_pixel_cases=pixel_cases,
        all_form_browser_previews=len(bulk),exact_copy_routes=copy_count,verified_html_css_examples=len(bulk),inputs=evidence['inputs'],results=checks)
    (REVIEW/'browser-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'PASS: 48 guide states, {len(bulk)} detail previews, {copy_count} exact copy routes, {pixel_cases} glyph-pixel comparisons')
    return result

if __name__=='__main__':run()
