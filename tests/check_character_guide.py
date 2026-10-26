# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
"""Check every public form and route independently against the compiled font."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from io import BytesIO
from collections import Counter
import hashlib,json,re,subprocess,tempfile
from fontTools.ttLib import TTFont
import uharfbuzz as hb

ROOT=Path(__file__).resolve().parents[1];ASSETS=ROOT/'guide/assets'
def read(p):return json.loads(Path(p).read_text('utf-8-sig'))

def run():
    checks=[]
    def check(name,ok):
        checks.append(dict(name=name,passed=bool(ok)))
        if not ok:raise AssertionError(name)
    data=read(ASSETS/'catalog.json');registry=read(ROOT/'entry-map.json')
    entries=data['entries'];by_id={e['id']:e for e in entries};by_glyph={e['glyph_name']:e for e in entries}
    check('725 unique public forms',len(entries)==len(by_id)==len(by_glyph)==725)
    check('Active font version',data['font_version']==registry['version'])
    check('Current OFL/RFN',data['license']=='OFL-1.1' and data['reserved_font_names']==['Moira'])
    check('Summary',data['summary']==dict(forms=725,glyphs=726,mapped_characters=225,canonical_tokens=579,compatibility_aliases=132,text_sequences=17))
    match=re.search(r'window\.MOIRA_CATALOG\s*=\s*(\{.*\})\s*;', (ASSETS/'catalog.js').read_text('utf-8'),re.S)
    check('Classic script payload equals JSON',bool(match) and json.loads(match.group(1))==data)
    with tempfile.TemporaryDirectory(prefix='moira-guide-build-') as tmp:
        subprocess.run([sys.executable,'-B',str(ROOT/'tooling/build_character_guide.py'),'--output',tmp],check=True,capture_output=True,text=True)
        for name in ['catalog.json','catalog.js']:check('Deterministic generated source '+name,(Path(tmp)/name).read_bytes()==(ASSETS/name).read_bytes())
    raw=[e for group in ['family_entries','extra_entries','batch_entries'] for e in registry[group]]
    canonical={e['token']:e['glyph_name'] for e in raw if not e.get('alias_for')}
    aliases={e['token']:e for e in raw if e.get('alias_for')}
    actual_tokens={r['text']:e['glyph_name'] for e in entries for r in e['routes'] if r['kind']=='token'}
    actual_aliases={r['text']:e['glyph_name'] for e in entries for r in e['routes'] if r['kind']=='word_alias'}
    check('All 579 canonical spellings preserved',actual_tokens==canonical)
    check('All 132 aliases preserved',actual_aliases=={k:v['glyph_name'] for k,v in aliases.items()})
    categories={c['id']:c for c in data['categories']};counts=Counter(e['category'] for e in entries)
    check('Category counts reflect forms',{k:v['count'] for k,v in categories.items()}==dict(counts))
    check('Core forms lead the default catalog',[e['name'] for e in entries[:14]]==['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces','Sun','Moon'])
    for entry in entries:
        name=entry['id']
        check(name+' readable identity',all(isinstance(entry[k],str) and entry[k].strip() for k in ['name','meaning','category_label','form_label','origin_label','search_text']))
        check(name+' category',entry['category'] in categories and entry['category_label']==categories[entry['category']]['label'])
        check(name+' valid related forms',len(entry['related_ids'])==len(set(entry['related_ids'])) and all(i in by_id and i!=name for i in entry['related_ids']))
        for related in entry['related_ids']:check(name+' symmetric relation '+related,name in by_id[related]['related_ids'])
        check(name+' no machine paths in user data',not re.search(r'\b[A-Za-z]:[/\\]',json.dumps(entry)))
        check(name+' sources are navigable web references',all(s['title'] and s['url'].startswith(('https://','http://')) for s in entry['sources']))
        check(name+' source titles are searchable',all(s['title'] in entry['search_text'] for s in entry['sources']))
        if entry['form_label']=='Historical form':check(name+' labelled historical witness',bool(entry['witness']) and entry['recommended_em']==32)
        if entry['form_label']=='Chart form':check(name+' distinct chart witness',bool(entry['witness']) and entry['recommended_em']==24)
        check(name+' at least one actual route',bool(entry['routes']))
        for route in entry['routes']:
            check(name+' route '+route['id']+' has readable context',bool(route['label']) and bool(route['note']))
            if route['kind'] in {'unicode','text_sequence','feature'}:
                check(name+' exact codepoint labels '+route['id'],route['codepoints']==['U+%04X'%ord(c) for c in route['text']] and len(route['unicode_names'])==len(route['text']))
                check(name+' no PUA allocation '+route['id'],all(not (0xE000<=ord(c)<=0xF8FF or 0xF0000<=ord(c)<=0xFFFFD or 0x100000<=ord(c)<=0x10FFFD) for c in route['text']))
    routes_checked=previews_checked=0
    for fmt in ['ttf','woff2']:
        f=TTFont(ROOT/f'fonts/MoiraAstro-Regular.{fmt}',recalcTimestamp=False)
        cmap=f.getBestCmap()
        check(fmt+' all font forms represented',set(by_glyph)==set(f.getGlyphOrder())-{'.notdef'})
        unicode_routes={ord(r['text']):e['glyph_name'] for e in entries for r in e['routes'] if r['kind']=='unicode'}
        check(fmt+' all 225 actual cmap routes',unicode_routes==cmap)
        expected_sequences={(chr(cp)+chr(sel),replacement or cmap[cp]) for table in f['cmap'].tables if table.format==14 for sel,pairs in table.uvsDict.items() for cp,replacement in pairs}
        actual_sequences={(r['text'],e['glyph_name']) for e in entries for r in e['routes'] if r['kind']=='text_sequence'}
        check(fmt+' all supported text sequences',actual_sequences==expected_sequences and len(actual_sequences)==17)
        f.flavor=None;buffer=BytesIO();f.save(buffer);font=hb.Font(hb.Face(buffer.getvalue()));font.scale=(1000,1000)
        def shape(text,features):
            b=hb.Buffer();b.add_str(text);b.guess_segment_properties();hb.shape(font,b,features)
            return [g.codepoint for g in b.glyph_infos]
        for e in entries:
            gid=f.getGlyphID(e['glyph_name'])
            check(fmt+' preview '+e['id'],shape(e['preview']['text'],e['preview']['features'])==[gid]);previews_checked+=1
            for route in e['routes']:
                check(fmt+' exact route '+e['id']+' '+route['id'],shape(route['text'],route['features'])==[gid]);routes_checked+=1
                if route['kind'] in {'token','word_alias'}:check(fmt+' opt-in ligature '+route['id'],shape(route['text'],{'dlig':False,'zero':False})!=[gid] and route['requires_feature']=='dlig')
        sun=by_glyph[cmap[0x2609]];moon=by_glyph[cmap[0x263E]]
        check(fmt+' original Sun default',sun['name']=='Sun' and sun['form_label']=='Default form' and any(by_id[i]['name']=='Ray Sun' for i in sun['related_ids']))
        check(fmt+' original Moon default',moon['name']=='Moon' and moon['form_label']=='Default form' and any('crescent' in by_id[i]['name'].lower() for i in moon['related_ids']))
        spirit=next(e for e in entries if any(r['text']=='[lot:Sp]' for r in e['routes']))
        check(fmt+' circled-S Spirit preserved',shape('[lot:Sp]',{'dlig':True})==[f.getGlyphID(cmap[0x24C8])])
        slashed=by_glyph['zero.slashed'];check(fmt+' zero feature is not a new Unicode identity',all(r['kind']=='feature' and r['text']=='0' and r['requires_feature']=='zero' for r in slashed['routes']) and slashed['form_label']=='Feature alternate')
        for char in ['☊','☋','⚸']:
            entry=by_glyph[cmap[ord(char)]]
            check(fmt+' shared lunar contexts '+char,len(entry['contexts'])>=2 and any('shared' in n.lower() and 'model' in n.lower() for n in entry['notes']))
        f.close()
    tao=next(e for e in entries if any(r['text']=='[astro:tao]' for r in e['routes']))
    check('Tao remains an original qualified 165-degree symbol','Original Moira symbol'==tao['origin_label'] and '165' in tao['search_text'])
    result=dict(status='PASS',checks=len(checks),forms=len(entries),preview_checks=previews_checked,route_shaping_checks=routes_checked,
        inputs={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['guide/assets/catalog.json','guide/assets/catalog.js','tooling/build_character_guide.py','entry-map.json','inventory/inventory.json','fonts/MoiraAstro-Regular.ttf','fonts/MoiraAstro-Regular.woff2']},results=checks)
    target=ROOT/'build/character-guide/catalog-checks.json';target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'PASS: {len(checks):,} guide checks; {previews_checked:,} previews and {routes_checked:,} route shapes; all 725 forms preserved')
    return result

if __name__=='__main__':run()
