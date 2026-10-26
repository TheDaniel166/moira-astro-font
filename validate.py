# Copyright 2026 Moira Astro contributors. Original glyph designs.
# with Reserved Font Name Moira.
# Licensed under SIL Open Font License 1.1. See OFL.txt and https://openfontlicense.org/
"""Rebuild, check licensing, and verify the complete frozen font contract."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from io import BytesIO
import argparse, hashlib, json, tempfile
from fontTools.ttLib import TTFont
import uharfbuzz as hb
from build import build, ROOT

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text('utf-8-sig'))
def glyph_digest(font, name):
    g = font['glyf'][name]; points, ends, flags = g.getCoordinates(font['glyf'])
    program = getattr(g, 'program', None)
    data = [list(points), list(ends), list(flags),
            list(program.getBytecode()) if program else [], list(font['hmtx'].metrics[name])]
    return hashlib.sha256(json.dumps(data, separators=(',', ':')).encode()).hexdigest()

def validate():
    checks = []
    def check(name, ok):
        checks.append(dict(name=name, passed=bool(ok)))
        if not ok: raise AssertionError(name)
    with tempfile.TemporaryDirectory(prefix='moira-ofl-check-') as tmp:
        a = build(Path(tmp)/'one'); b = build(Path(tmp)/'two')
        check('Two byte-identical source builds', a == b)
        check('Distributed binaries equal source builds', a == {n:sha(ROOT/'fonts'/n) for n in a})
    contract = read(ROOT/'source/baseline-contract.json')
    registry = read(ROOT/'entry-map.json')
    tokens = registry['family_entries']+registry['extra_entries']+registry['batch_entries']
    check('Exactly 711 unique optional routes', len(tokens)==len({e['token'] for e in tokens})==711)
    check('35 direct registry routes', len(registry['character_entries'])==35)
    check('OFL registry declaration', registry['license']=='OFL-1.1' and registry['reserved_font_names']==['Moira'])
    ofl = (ROOT/'OFL.txt').read_text('utf-8')
    check('Customized OFL header without placeholders', ofl.startswith(contract['copyright']+'\nwith Reserved Font Name Moira.\n\nThis Font Software') and '<Copyright Holder>' not in ofl)
    check('Full OFL text included', all(t in ofl for t in ['26 February 2007','PREAMBLE','DEFINITIONS','PERMISSION & CONDITIONS','TERMINATION','DISCLAIMER']))
    for fmt in ['ttf','woff2']:
        f = TTFont(ROOT/f'fonts/MoiraAstro-Regular.{fmt}', recalcTimestamp=False)
        check(fmt+' glyph order', f.getGlyphOrder()==contract['glyph_order'] and len(f.getGlyphOrder())==726)
        check(fmt+' cmap count', len(f.getBestCmap())==225)
        for name,digest in contract['glyphs'].items():
            check(fmt+' frozen outline, hinting and metrics '+name, glyph_digest(f,name)==digest)
        for tag,digest in contract['tables'].items():
            check(fmt+' exact stable table '+tag, hashlib.sha256(f.getTableData(tag)).hexdigest()==digest)
        for attr,value in contract['head'].items():
            # WOFF2 sets the lossless-transform flag when reconstructing sfnt.
            actual=getattr(f['head'], attr)
            if attr=='flags' and fmt=='woff2': actual &= ~0x800; value &= ~0x800
            check(fmt+' stable head '+attr, actual==value)
        check(fmt+' revision', abs(f['head'].fontRevision-.942)<1/65536)
        check(fmt+' embedding unrestricted', f['OS/2'].fsType==0)
        check(fmt+' version', f['name'].getDebugName(5)=='Version 0.942; Moira Astro 0.13.2-alpha.1')
        for record in f['name'].names:
            if record.nameID==13: check(fmt+' full embedded OFL '+str((record.platformID,record.platEncID,record.langID)),record.toUnicode().strip()==ofl.strip())
            if record.nameID==14: check(fmt+' license URL '+str((record.platformID,record.platEncID,record.langID)),record.toUnicode()=='https://openfontlicense.org/')
        for name_id in [0,13,14]:
            check(fmt+' required metadata '+str(name_id),bool(f['name'].getDebugName(name_id)))
        check(fmt+' copyright and RFN',f['name'].getDebugName(0)==contract['copyright']+'\nwith Reserved Font Name Moira.')
        check(fmt+' pending-license text removed',all('license has not been selected' not in r.toUnicode() for r in f['name'].names))
        f.flavor=None; data=BytesIO(); f.save(data)
        face=hb.Font(hb.Face(data.getvalue())); face.scale=(1000,1000)
        def shape(text,features):
            buf=hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(face,buf,features)
            return [(i.codepoint,p.x_advance,p.x_offset,p.y_offset) for i,p in zip(buf.glyph_infos,buf.glyph_positions)]
        def gids(text,on):return [g[0] for g in shape(text,{'dlig':on})]
        cmap=f.getBestCmap()
        for e in tokens:
            check(fmt+' enabled '+e['token'],gids(e['token'],True)==[f.getGlyphID(e['glyph_name'])])
            check(fmt+' disabled '+e['token'],gids(e['token'],False)==[f.getGlyphID(cmap[ord(c)]) for c in e['token']])
            bad=e['token'][:-1]
            check(fmt+' incomplete token '+e['token'],gids(bad,True)==[f.getGlyphID(cmap[ord(c)]) for c in bad])
        for cp,name in cmap.items():
            if cp in [0xFE0E,0xFE0F]:continue
            check(fmt+' direct '+hex(cp),gids(chr(cp),False)==[f.getGlyphID(name)])
        check(fmt+' unslashed zero remains default',gids('0',False)==[f.getGlyphID(cmap[ord('0')])])
        check(fmt+' zero feature still selects alternate',shape('0',{'zero':True})!=shape('0',{'zero':False}))
        f.close()
    result=dict(status='PASS',version='0.13.2-alpha.1',checks=len(checks),results=checks,
                glyphs=726,mapped_characters=225,optional_tokens=711,direct_registry_routes=35,
                byte_identical_rebuilds=True,
                inputs={p:sha(ROOT/p) for p in ['source/MoiraAstro-Regular.ttx','source/baseline-contract.json','entry-map.json','aliases.json','OFL.txt','build.py','validate.py']},
                artifacts={f'fonts/{n}':sha(ROOT/'fonts'/n) for n in a})
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',type=Path,default=ROOT/'build/checks.json'); args=parser.parse_args()
    result=validate(); args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"PASS: {result['checks']:,} checks; full OFL metadata; reproducible TTF/WOFF2; all prior glyphs and routes preserved")
