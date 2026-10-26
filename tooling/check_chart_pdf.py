# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
"""Independently extract, inspect fonts, rasterize and check the chart folio PDFs."""
from pathlib import Path
import hashlib,json,math
import fitz

ROOT=Path(__file__).resolve().parents[1];REVIEW=ROOT/'build/chart-pilot'
def normalized(text):return ' '.join(text.replace('\u00a0',' ').split())
def read(p):return json.loads(Path(p).read_text('utf-8-sig'))

def run():
    checks=[];documents=[]
    def check(name,ok):
        checks.append(dict(name=name,passed=bool(ok)))
        if not ok:raise AssertionError(name)
    fixtures=read(ROOT/'demo/chart-pilot/assets/fixtures.json')
    for fixture in fixtures['fixtures']:
        key=fixture['id'];source=REVIEW/f'MoiraAstro-{key}-chart-pilot.pdf';doc=fitz.open(source)
        check(key+' three deliberate pages',len(doc)==3)
        all_fonts={};pages=[]
        for i,page in enumerate(doc):
            label=f'{key} page {i+1}'
            check(label+' Letter landscape',abs(page.rect.width-792)<.1 and abs(page.rect.height-612)<.1)
            text=normalized(page.get_text())
            check(label+' source/fixture disclaimer','Declared fixture positions, not engine calculations' in text)
            check(label+' page number',f'{i+1} / 3' in text)
            check(label+' readable content',len(text)>300)
            check(label+' no replacement characters','\ufffd' not in text)
            spans=[s for block in page.get_text('dict')['blocks'] if 'lines' in block for line in block['lines'] for s in line['spans']]
            for s in spans:
                x0,y0,x1,y1=s['bbox']
                check(label+' text bounds '+s['text'][:35],x0>=-.5 and y0>=-.5 and x1<=page.rect.width+.5 and y1<=page.rect.height+.5)
            moira=[s for s in spans if 'MoiraAstro' in s['font'].replace(' ','') and s['text'].strip()]
            check(label+' actual Moira glyph spans',len(moira)>=4)
            for font in page.get_fonts(full=True):
                xref=font[0];name=font[3]
                if 'MoiraAstro' in name.replace(' ',''):
                    extracted=doc.extract_font(xref);program=extracted[-1]
                    check(label+' embedded font '+str(xref),bool(program) and len(program)>1000)
                    parsed=fitz.Font(fontbuffer=program)
                    check(label+' readable embedded font '+str(xref),parsed.glyph_count>0)
                    all_fonts[xref]=dict(name=name,bytes=len(program),sha256=hashlib.sha256(program).hexdigest(),glyphs=parsed.glyph_count)
            if i==0:
                for p in fixture['positions']:check(label+' full body name '+p['id'],normalized(p['name']) in text)
                for model in ['mean ascending node','mean lunar apogee']:check(label+' model qualifier '+model,model in text)
                check(label+' minimum wheel symbol point size',min(s['size'] for s in moira)>=10.5)
            elif i==1:
                for item in fixture['lots']+fixture['minorBodies']:check(label+' complete lot/body '+item['name'],normalized(item['name']) in text)
                check(label+' lot formula boundary','do not select or calculate lot formulas' in text)
                check(label+' Tao angle','Tao' in text and '165' in text and '24-degree Quindecile' in text)
            else:
                for item in fixtures['fixedStars']:check(label+' star identity '+item['id'],item['name'] in text and normalized(item['witness']) in text)
                for sat in fixtures['satellites']:check(label+' satellite name '+sat['id'],normalized(sat['name']) in text)
                check(label+' historical and chart sizes',any(abs(s['size']-24)<.1 for s in moira) and any(abs(s['size']-18)<.1 for s in moira))
                check(label+' stress label','14 px' in text and 'stress' in text)
            png=REVIEW/f'{key}-print-page-{i+1}.png';pix=page.get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False);pix.save(png)
            # Pixel presence of each actual-font text span, evaluated by another renderer.
            for n,s in enumerate(moira):
                clip=fitz.Rect(s['bbox']) & page.rect
                crop=page.get_pixmap(matrix=fitz.Matrix(2,2),clip=clip,alpha=False)
                samples=crop.samples
                check(label+' glyph raster '+str(n),bool(samples) and min(samples)<200)
            pages.append(dict(page=i+1,width=page.rect.width,height=page.rect.height,moira_spans=len(moira),
                moira_point_sizes=sorted(set(round(s['size'],3) for s in moira)),png=png.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(png.read_bytes()).hexdigest()))
        check(key+' embedded Moira font present',bool(all_fonts))
        documents.append(dict(fixture=key,pdf=source.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(source.read_bytes()).hexdigest(),embedded_fonts=all_fonts,pages=pages));doc.close()
    focused=REVIEW/'MoiraAstro-focused-crowded-chart-pilot.pdf'
    check('Focused print regression exported',focused.is_file())
    focused_doc=fitz.open(focused);baseline_doc=fitz.open(REVIEW/'MoiraAstro-crowded-chart-pilot.pdf')
    check('Focused print preserves three pages',len(focused_doc)==len(baseline_doc)==3)
    for i in range(3):
        a=baseline_doc[i].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False)
        b=focused_doc[i].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False)
        check('Focused/scrolled print exact pixels page '+str(i+1),a.width==b.width and a.height==b.height and a.samples==b.samples)
    focused_doc.close();baseline_doc.close()
    result=dict(status='PASS',renderer='MuPDF '+fitz.VersionBind,checks=len(checks),documents=documents,results=checks,
        focused_print=dict(path=focused.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(focused.read_bytes()).hexdigest(),exact_page_comparisons=3),
        limitation='Chromium print export and MuPDF raster review; not physical-printer certification. Host text-font subsets are QA artifacts, not part of the Moira font distribution.')
    (REVIEW/'pdf-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks):,} PDF checks; six Letter landscape pages, real embedded font subsets and independent raster proofs')
    return result

if __name__=='__main__':run()
