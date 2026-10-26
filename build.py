# Copyright 2026 Moira Astro contributors. Original glyph designs.
# with Reserved Font Name Moira.
# Licensed under SIL Open Font License 1.1. See OFL.txt and https://openfontlicense.org/
"""Build both containers from the complete, editable FontTools XML source."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import argparse, hashlib, json
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent

def build(output):
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    font = TTFont(recalcTimestamp=False)
    font.importXML(ROOT/'source/MoiraAstro-Regular.ttx')
    assert font['name'].getDebugName(13).strip() == (ROOT/'OFL.txt').read_text('utf-8').strip()
    assert font['name'].getDebugName(14) == 'https://openfontlicense.org/'
    assert font['OS/2'].fsType == 0
    target = output/'MoiraAstro-Regular.ttf'
    font.save(target); font.close()
    web = TTFont(target, recalcTimestamp=False); web.flavor = 'woff2'
    web.save(target.with_suffix('.woff2')); web.close()
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [target,target.with_suffix('.woff2')]}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'fonts')
    args = parser.parse_args()
    result = build(args.output)
    print('Built TTF and WOFF2 from editable TTX source')
    for name,digest in result.items(): print(name+': '+digest)
