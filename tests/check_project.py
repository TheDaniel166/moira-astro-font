# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
"""Check the portable repository and frozen original archive integrity."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import hashlib,json,re,xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
FROZEN=('designs/','masters/','sources/','inventory/planning/','provenance/font-')

def run():
    results=[]
    def check(name,passed):
        results.append(dict(name=name,passed=bool(passed)))
        if not passed:raise AssertionError(name)
    manifest=json.loads((ROOT/'provenance/imports.json').read_text('utf-8'))
    frozen=0;svg=0
    for entry in manifest['files']:
        name=entry['path']
        check('Safe import path '+name,not Path(name).is_absolute() and '..' not in Path(name).parts)
        if name.startswith(FROZEN):
            path=ROOT/name
            check('Frozen source '+name,path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256']);frozen+=1
            if path.suffix=='.svg':
                tree=ET.parse(path)
                check('Valid SVG '+name,tree.getroot().tag=='{http://www.w3.org/2000/svg}svg');svg+=1
    check('Original master coverage',svg==771)
    check('29 archived design packets',len(manifest['design_groups'])==29)
    for group in manifest['design_groups']:
        check('Archived packet exists '+group['path'],(ROOT/group['path']).is_dir())
    required=['OFL.txt','UNICODE-LICENSE.txt','source/MoiraAstro-Regular.ttx','source/baseline-contract.json',
              'fonts/MoiraAstro-Regular.ttf','fonts/MoiraAstro-Regular.woff2','inventory/inventory.json',
              '.github/workflows/font-checks.yml','entry-map.json','aliases.json','build.py','validate.py',
              'demo/chart-pilot/index.html','demo/chart-pilot/assets/app.js','demo/chart-pilot/assets/fixtures.json',
              'demo/chart-pilot/assets/fixtures.js','tests/check_chart_pilot.py']
    for name in required:check('Required project file '+name,(ROOT/name).is_file())
    registry=json.loads((ROOT/'entry-map.json').read_text('utf-8'))
    check('Current OFL registry',registry['version']=='0.13.2-alpha.1' and registry['license']=='OFL-1.1')
    inventory=json.loads((ROOT/'inventory/inventory.json').read_text('utf-8'))
    check('327 reconciled records',inventory['summary']['inventory_records']==327)
    class Links(HTMLParser):
        def __init__(self):super().__init__();self.links=[]
        def handle_starttag(self,tag,attrs):
            for k,v in attrs:
                if k in {'href','src'}:self.links.append(v)
    documents=[ROOT/n for n in ['README.md','CONTRIBUTING.md','AGENTS.md','NOTICE.md','CHECKS.md','index.html','demo/chart-pilot/index.html','demo/chart-pilot/README.md']]+sorted((ROOT/'docs').glob('*.md'))
    link_count=0
    for doc in documents:
        text=doc.read_text('utf-8')
        if doc.suffix=='.html':
            parser=Links();parser.feed(text);links=parser.links
        else:links=re.findall(r'\[[^\]]*\]\(([^)]+)\)',text)
        for link in links:
            if urlparse(link).scheme or link.startswith('#'):continue
            target=unquote(link.split('#')[0])
            check('Current doc link '+doc.relative_to(ROOT).as_posix()+' -> '+link,(doc.parent/target).is_file());link_count+=1
    for name in ['build.py','validate.py','native_smoke.py']:
        text=(ROOT/name).read_text('utf-8')
        check('Portable active tool '+name,'C:/dev/' not in text and 'C:\\dev\\' not in text)
    result=dict(status='PASS',checks=len(results),frozen_imports=frozen,svg_masters=svg,current_doc_links=link_count,results=results)
    target=ROOT/'build/project-checks.json';target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(results):,} project checks; {frozen} frozen imports, {svg} SVG masters, {link_count} current documentation links')
    return result

if __name__=='__main__':run()
