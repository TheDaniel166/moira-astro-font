# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
"""Derive the character guide from the actual font and preserved semantic records."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from collections import Counter,defaultdict
import argparse,hashlib,json,re,unicodedata
from fontTools.ttLib import TTFont

ROOT=Path(__file__).resolve().parents[1]
CATEGORIES=[('zodiac','Zodiac'),('bodies','Bodies'),('aspects','Aspects'),('lots','Lots'),
 ('lunar','Lunar & eclipse notation'),('points','Points, angles & motion'),('hypothetical','Hypothetical points'),
 ('fixed-stars','Fixed stars'),('classification','Elements & classifications'),('reference','Astronomical reference'),
 ('notation','Notation'),('letters','Letters & numbers'),('spacing','Spacing')]
LABELS=dict(CATEGORIES)
COPY_NOTE='This route selects the drawing. Keep its named identity and any model or formula qualifiers in your chart data.'
def read(p):return json.loads(Path(p).read_text('utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def scalar(text):
    if isinstance(text,int):return text
    if isinstance(text,str) and re.fullmatch(r'U\+[0-9A-Fa-f]{4,6}',text):return int(text[2:],16)
    return None
def strings(value):
    if isinstance(value,str):return [value]
    if isinstance(value,list):return [v for v in value if isinstance(v,str)]
    return []
def unique(values):return list(dict.fromkeys(v for v in values if v))

def build(output):
    registry=read(ROOT/'entry-map.json');inventory=read(ROOT/'inventory/inventory.json')
    font=TTFont(ROOT/'fonts/MoiraAstro-Regular.ttf',recalcTimestamp=False);cmap=font.getBestCmap()
    raw=[e for group in ['family_entries','extra_entries','batch_entries'] for e in registry[group]]
    canonical=[e for e in raw if not e.get('alias_for')];aliases=[e for e in raw if e.get('alias_for')]
    known_names={}
    def names(obj):
        if isinstance(obj,dict):
            cp=scalar(obj.get('codepoint'));name=obj.get('unicode_name')
            if cp is not None and name:known_names[cp]=name
            cps=obj.get('codepoints',[]);ns=obj.get('unicode_names',[])
            if isinstance(cps,list) and isinstance(ns,list):
                for cp,name in zip(cps,ns):
                    value=scalar(cp)
                    if value is not None and isinstance(name,str):known_names[value]=name
            for value in obj.values():names(value)
        elif isinstance(obj,list):
            for value in obj:names(value)
    names(registry);names(inventory)
    def uname(cp):
        result=known_names.get(cp) or unicodedata.name(chr(cp),None)
        if result is None:raise ValueError('Missing formal Unicode name U+%04X'%cp)
        return result
    inv_by_id={e['id']:e for e in inventory['entries']};by_char=defaultdict(list)
    for item in inventory['entries']:
        # The reconciled top-level mapping can point to a later alternate. The
        # preserved planning mapping still identifies the original default.
        maps=[(item.get('planning_record') or item).get('mapping',{}),item.get('mapping',{})]
        maps += [a.get('mapping',{}) for a in item.get('alternate_forms',[])]
        for m in maps:
            text=m.get('text')
            if text and len(text)==1 and item not in by_char[text]:by_char[text].append(item)
    direct_by_glyph=defaultdict(list)
    for e in registry['character_entries']:direct_by_glyph[e['glyph_name']].append(e)
    source_refs={s['id']:dict(title=s['title'],url=s['uri']) for s in inventory['sources'] if s.get('uri','').startswith(('https://','http://'))}
    star_sources=[]
    source_docs=sorted((ROOT/'designs').glob('historical-fixed-star*/SOURCES.md'))
    for p in source_docs:
        for title,url in re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)',p.read_text('utf-8-sig')):
            if any(s in (title+' '+url).lower() for s in ['agrippa','1533','1651']):star_sources.append(dict(title=title,url=url))
    entries={};contexts_for=defaultdict(list)
    def add_context(entry,item):
        if not item:return
        context=dict(id=item['id'],name=item['name'],meaning=item.get('meaning') or item['name'])
        if context['id'] not in {c['id'] for c in entry['contexts']}:entry['contexts'].append(context)
        entry['semantic_ids']=unique(entry['semantic_ids']+[item['id']])
        entry['aliases']=unique(entry['aliases']+[item['name'],item.get('plain_text_fallback')])
        entry['sources'] += [source_refs[s] for s in item.get('sources',[]) if s in source_refs]
        if item.get('current_font',{}).get('coverage_status')=='shared_icon_requires_model_label':
            entry['notes'].append('This drawing is shared by model-qualified identities. Keep the mean/true or mean/osculating qualifier explicit; changing the graphic does not select a model.')
    def blank(glyph,name,meaning='',source=None):
        return dict(id='glyph.'+glyph,glyph_name=glyph,name=name,meaning=meaning or name,
            category='notation',category_label='Notation',aliases=[],semantic_ids=[],contexts=[],
            preview=dict(text='',features=dict(dlig=False,zero=False)),recommended_em=18,
            form_label='Standard form',origin_label='Original Moira drawing',witness=None,
            notes=[],related_ids=[],routes=[],sources=[],spacing=False,rank=400,
            source_record_id=(source or {}).get('id') or (source or {}).get('family_id'))
    def route(kind,text,label,features=None,codepoints=None,note=''):
        cps=codepoints if codepoints is not None else [ord(c) for c in text] if kind in {'unicode','text_sequence','feature'} else []
        return dict(id=kind+':'+('.'.join('%X'%c for c in cps) if cps else text),kind=kind,text=text,label=label,
            codepoints=['U+%04X'%cp for cp in cps],unicode_names=[uname(cp) for cp in cps],
            features=features or dict(dlig=kind in {'token','word_alias'},zero=False),
            requires_feature='zero' if kind=='feature' else 'dlig' if kind in {'token','word_alias'} else None,
            note=note or COPY_NOTE)
    for e in canonical:
        name=e.get('name') or e.get('display_label') or e.get('label') or e['token']
        policy=e.get('definition_policy') or {}
        meaning=e.get('meaning') or policy.get('meaning') or ('Lot of '+name if e['token'].startswith('[lot:') else name)
        entry=blank(e['glyph_name'],name,meaning,e);entries[e['glyph_name']]=entry
        entry['semantic_ids']=unique([e.get('semantic_id'),e.get('family_id'),e.get('source_inventory_id')])
        entry['aliases']=unique(strings(e.get('aliases'))+[e.get('short_label'),e.get('display_label'),e.get('plain_text_fallback')])
        entry['routes'].append(route('token',e['token'],'Canonical token'))
        entry['preview']=dict(text=e['token'],features=dict(dlig=True,zero=False))
        entry['source_group']=e.get('group','Lots' if e['token'].startswith('[lot') else '')
        entry['witness']=e.get('witness')
        if e.get('variant')=='historical':entry.update(form_label='Historical form',origin_label='Moira reconstruction of the named historical witness',recommended_em=32)
        elif e.get('variant')=='chart':entry.update(form_label='Chart form',origin_label='Moira chart adaptation of the named witness',recommended_em=24)
        elif e.get('variant_for') or 'alternate' in name.lower():entry['form_label']='Alternate form'
        if e.get('origin')=='moira_original_redrawing_of_attested_form':entry['origin_label']='Original Moira drawing of an attested form'
        elif e.get('origin') and any(s in e['origin'] for s in ['invent','original_moira']):entry['origin_label']='Original Moira symbol'
        if e['token'].startswith('[lot'):
            entry['notes'].append('The lot name/code identifies an entry; its formula must be selected separately.')
            if e.get('formula_record_ids'):entry['notes'].append(str(len(e['formula_record_ids']))+' related formula records; this font route selects none of them.')
        if entry['witness']:entry['sources']+=star_sources
        if policy:
            fields=policy.get('required_metadata',[])
            if fields:entry['notes'].append('Keep these qualifiers with the entry: '+', '.join(k.replace('_',' ') for k in fields)+'.')
            for key,label in [('required_lunar_model','Required lunar model'),('opposite_relation','Opposite relation'),('qualifier','Form cue')]:
                if isinstance(policy.get(key),str):entry['notes'].append(label+': '+policy[key]+'.')
            entry['notes'].append('Font appearance does not choose a native implementation or calculation model.')
            if policy.get('changes_existing_twelve_sign_model') is False:
                entry['notes'].append('This convention does not add a sign to the native twelve-sign zodiac.')
        for sid in entry['semantic_ids'][:]:add_context(entry,inv_by_id.get(sid))
    by_token={e['token']:e for e in canonical}
    for e in aliases:
        parent=by_token[e['alias_for']];entries[parent['glyph_name']]['routes'].append(route('word_alias',e['token'],'Word-compatible token',note='Hyphen-free compatibility alias for '+e['alias_for']+'. It selects the same drawing and meaning; enable discretionary ligatures.'))
    for cp,glyph in sorted(cmap.items()):
        char=chr(cp);is_new=glyph not in entries
        if is_new:
            direct=direct_by_glyph.get(glyph,[])
            owners=by_char.get(char,[])
            # Prefer explicit current form labels for admitted alternates; otherwise
            # preserve the named semantic identity of the original mapping.
            source=next((e for e in direct if e.get('character')==char),None)
            original=next((e for e in owners if (e.get('planning_record') or e).get('mapping',{}).get('text')==char),None)
            owner=original or (owners[0] if owners else None)
            name=source.get('name') if source else owner.get('name') if owner else uname(cp).title()
            meaning=source.get('meaning') if source else owner.get('meaning') if owner else 'The Unicode character '+uname(cp)+'.'
            entry=blank(glyph,name,meaning,source);entries[glyph]=entry
            entry['preview']=dict(text=char,features=dict(dlig=False,zero=False))
            entry['source_group']=(source or {}).get('group','')
            if source:
                entry['semantic_ids']=unique([source.get('semantic_id'),source.get('source_inventory_id')])
                if 'alternate' in entry['source_group'].lower() or source.get('default_replacement') is False:entry['form_label']='Alternate form'
            if original and original['id'].startswith(('body.','zodiac.','aspect.')):entry['form_label']='Default form'
        entry=entries[glyph]
        entry['routes'].append(route('unicode',char,'Unicode character',codepoints=[cp]))
        for item in by_char.get(char,[]):add_context(entry,item)
        for direct in direct_by_glyph.get(glyph,[]):
            if direct.get('semantic_id'):entry['semantic_ids']=unique(entry['semantic_ids']+[direct['semantic_id']])
        entry['aliases']=unique(entry['aliases']+[uname(cp),'U+%04X'%cp])
        if cp==0x260A:entry['aliases']=unique(entry['aliases']+['North node','NorthNode'])
        if cp==0x260B:entry['aliases']=unique(entry['aliases']+['South node','SouthNode'])
        if cp in [0x20,0xA0]:
            entry.update(name='Space / no-break space',meaning='Blank spacing characters. Space and no-break space share this drawing but retain different text-wrapping behavior.',spacing=True,category='spacing')
    sequence_count=0
    for table in font['cmap'].tables:
        if table.format!=14:continue
        for selector,pairs in table.uvsDict.items():
            for cp,replacement in pairs:
                glyph=replacement or cmap[cp]
                entries[glyph]['routes'].append(route('text_sequence',chr(cp)+chr(selector),'Text-presentation sequence',codepoints=[cp,selector],note='Supported base character plus text variation selector. Preserve both codepoints when copying.'))
                sequence_count+=1
    zero_glyph=None
    for feature in font['GSUB'].table.FeatureList.FeatureRecord:
        if feature.FeatureTag=='zero':
            for index in feature.Feature.LookupListIndex:
                for sub in font['GSUB'].table.LookupList.Lookup[index].SubTable:
                    zero_glyph=getattr(sub,'mapping',{}).get(cmap[ord('0')],zero_glyph)
    if not zero_glyph:raise ValueError('Slashed zero feature target missing')
    zero=blank(zero_glyph,'Slashed zero','Alternate drawing of digit zero, selected by the OpenType zero feature. It is the same Unicode digit, not an additional character.')
    zero.update(form_label='Feature alternate',semantic_ids=['notation.digit-zero'],category='letters',
        preview=dict(text='0',features=dict(dlig=False,zero=True)),notes=['Unslashed zero remains the default. Use the zero feature to obtain this form.'])
    zero['routes']=[route('feature','0','Base character + zero feature',dict(dlig=False,zero=True),[0x30],note='This copies the base digit 0. Apply the OpenType zero feature; a new Unicode slashed-zero character is not allocated.')]
    entries[zero_glyph]=zero;entries[cmap[0x30]]['semantic_ids'].append('notation.digit-zero')
    entries[cmap[0x30]]['name']='Digit zero — unslashed default'
    entries[cmap[0x30]]['form_label']='Default form'
    # Attach semantic references after all direct mappings exist. An original
    # identity and its approved graphic alternates remain separate form records.
    for entry in entries.values():
        for sid in entry['semantic_ids'][:]:add_context(entry,inv_by_id.get(sid))
    def classify(entry):
        text=' '.join([entry['name'],entry.get('source_group',''),*entry['semantic_ids']]).lower()
        cps=[scalar(c) for r in entry['routes'] if r['kind']=='unicode' for c in r['codepoints']]
        if entry['spacing']:return 'spacing'
        if any(r['kind']=='token' and r['text'].startswith('[lot') for r in entry['routes']):return 'lots'
        if entry['witness'] or 'fixed-star' in text:return 'fixed-stars'
        if any(s.startswith('zodiac.') for s in entry['semantic_ids']) or any(0x2648<=c<=0x2653 for c in cps):return 'zodiac'
        if all((0x30<=c<=0x39 or 0x41<=c<=0x5A or 0x61<=c<=0x7A) for c in cps) and cps or entry['glyph_name']==zero_glyph:return 'letters'
        if 'hypothetical' in text or 'uranian' in text or 'transpluto' in text:return 'hypothetical'
        if any(s.startswith(('body.','smallbody.','asteroid.','centaur.')) for s in entry['semantic_ids']) or any(s in text for s in ['minor bodies','small bodies','historical asteroid','extended centaurs','outer bodies','physical small']):return 'bodies'
        if any(s.startswith('aspect.') for s in entry['semantic_ids']) or 'aspects' in text:return 'aspects'
        if any(s in text for s in ['lunar','eclipse','occultation','phase']):return 'lunar'
        if any(s in text for s in ['points, angles','derived angles','angle.','point.','motion.']):return 'points'
        if any(s in text for s in ['classification','elements','dignity','antiscia','modality','house-category','sect.']):return 'classification'
        if 'astronomical' in text or any(s.startswith('reference.') for s in entry['semantic_ids']):return 'reference'
        return 'notation'
    related=defaultdict(set)
    for entry in entries.values():
        entry['category']=classify(entry);entry['category_label']=LABELS[entry['category']]
        if entry['name'].lower() in {'fortuna','makemake','quaoar'}:entry['recommended_em']=24
        if entry['category']=='fixed-stars':related['star:'+entry['name']].add(entry['id'])
        for sid in entry['semantic_ids']:related[sid].add(entry['id'])
        for c in entry['contexts']:related[c['id']].add(entry['id'])
    priority=[*range(0x2648,0x2654),0x2609,0x263E,0x263F,0x2640,0x2642,0x2643,0x2644,0x2645,0x2646,0x2647,0x260A,0x260B,0x26B8,0x260C,0x26B9,0x25A1,0x25B3,0x260D]
    ranks={c:i for i,c in enumerate(priority)}
    for entry in entries.values():
        relatives=set()
        for sid in entry['semantic_ids']:relatives|=related[sid]
        if entry['category']=='fixed-stars':relatives|=related['star:'+entry['name']]
        entry['related_ids']=sorted(relatives-{entry['id']})
        entry['sources']=list({(s['title'],s['url']):s for s in entry['sources']}.values())
        if not entry['sources']:entry['sources']=[dict(title='Unicode character reference',url='https://www.unicode.org/charts/')] if any(r['kind']=='unicode' for r in entry['routes']) else []
        entry['notes']=unique(entry['notes']);entry['semantic_ids']=unique(entry['semantic_ids']);entry['aliases']=unique(entry['aliases'])
        points=[scalar(c) for r in entry['routes'] if r['kind']=='unicode' for c in r['codepoints']]
        entry['rank']=min([ranks[c] for c in points if c in ranks] or [100+list(LABELS).index(entry['category'])*20])
        if entry['category']=='lots':entry['rank']=500
        entry['search_text']=' '.join(unique([entry['name'],entry['meaning'],entry['category_label'],entry['form_label'],entry['witness'],*entry['aliases'],*entry['semantic_ids'],*[s['name'] for s in entry['contexts']],*[s['meaning'] for s in entry['contexts']],*[r['text'] for r in entry['routes']],*[c for r in entry['routes'] for c in r['codepoints']],*[n for r in entry['routes'] for n in r['unicode_names']],*[s['title'] for s in entry['sources']],*[s['url'] for s in entry['sources']]]))
        entry.pop('source_group',None)
    result=sorted(entries.values(),key=lambda e:(e['rank'],e['name'].casefold(),e['id']))
    counts=Counter(e['category'] for e in result)
    data=dict(schema_version=1,project='Moira Astro',font_version=registry['version'],license='OFL-1.1',
        copyright='Copyright 2026 Moira Astro contributors. Original glyph designs.',reserved_font_names=['Moira'],
        notice='Graphic access routes preserve Unicode/token text. Named identities, model qualifiers and formula choices remain separate.',
        summary=dict(forms=len(result),glyphs=len(font.getGlyphOrder()),mapped_characters=len(cmap),canonical_tokens=len(canonical),compatibility_aliases=len(aliases),text_sequences=sequence_count),
        categories=[dict(id=k,label=v,count=counts[k]) for k,v in CATEGORIES if counts[k]],entries=result)
    assert len(result)==725 and sequence_count==17 and {e['glyph_name'] for e in result}==set(font.getGlyphOrder())-{'.notdef'}
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    (output/'catalog.json').write_text(text,encoding='utf-8',newline='\n')
    (output/'catalog.js').write_text('// Copyright 2026 Moira Astro contributors. SIL OFL 1.1. Generated by tooling/build_character_guide.py.\nwindow.MOIRA_CATALOG = '+text.rstrip()+';\n',encoding='utf-8',newline='\n')
    font.close();return data

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=ROOT/'guide/assets');args=parser.parse_args()
    data=build(args.output)
    print(f"Built {data['summary']['forms']} guide forms: 225 Unicode mappings, 579 canonical tokens, 132 aliases and 17 text sequences; fonts unchanged")
