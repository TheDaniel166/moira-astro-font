# Copyright 2026 Moira Astro contributors. Original glyph designs.
# with Reserved Font Name Moira.
# Licensed under SIL Open Font License 1.1. See OFL.txt and https://openfontlicense.org/
"""Windows process-private font intake; never installs a font globally."""
import sys
sys.dont_write_bytecode=True
import ctypes as C
from ctypes import wintypes as W
from pathlib import Path
import hashlib,json
from fontTools.ttLib import TTFont

ROOT=Path(__file__).resolve().parent
G=C.WinDLL('gdi32',use_last_error=True)
def api(name,result,args):
    f=getattr(G,name);f.restype=result;f.argtypes=args;return f
handle=C.c_void_p;integer=C.c_int;dword=W.DWORD;uint=W.UINT
add=api('AddFontMemResourceEx',handle,[handle,dword,handle,C.POINTER(dword)])
remove=api('RemoveFontMemResourceEx',W.BOOL,[handle])
createdc=api('CreateCompatibleDC',handle,[handle]);deletedc=api('DeleteDC',W.BOOL,[handle])
select=api('SelectObject',handle,[handle,handle]);delete=api('DeleteObject',W.BOOL,[handle])
createfont=api('CreateFontW',handle,[integer]*5+[dword]*8+[W.LPCWSTR])
fontdata=api('GetFontData',dword,[handle,dword,dword,handle,dword])
indices=api('GetGlyphIndicesW',dword,[handle,W.LPCWSTR,integer,C.POINTER(W.WORD),dword])
class FIXED(C.Structure):_fields_=[('fract',W.WORD),('value',C.c_short)]
class MAT2(C.Structure):_fields_=[('eM11',FIXED),('eM12',FIXED),('eM21',FIXED),('eM22',FIXED)]
class POINT(C.Structure):_fields_=[('x',W.LONG),('y',W.LONG)]
class METRICS(C.Structure):_fields_=[('w',uint),('h',uint),('origin',POINT),('dx',C.c_short),('dy',C.c_short)]
outline=api('GetGlyphOutlineW',dword,[handle,uint,uint,C.POINTER(METRICS),dword,handle,C.POINTER(MAT2)])

if __name__=='__main__':
    path=ROOT/'fonts/MoiraAstro-Regular.ttf';raw=path.read_bytes();buffer=C.create_string_buffer(raw);count=dword()
    resource=dc=font_handle=old=None
    glyph_count=char_count=0
    try:
        resource=add(buffer,len(raw),None,C.byref(count));assert resource and count.value==1
        font=TTFont(path,recalcTimestamp=False);dc=createdc(None);assert dc
        font_handle=createfont(-64,0,0,0,400,0,0,0,1,0,0,4,0,font['name'].getDebugName(1));assert font_handle
        old=select(dc,font_handle)
        tag=int.from_bytes(b'name','little');n=fontdata(dc,tag,0,None,0);assert n!=0xFFFFFFFF
        table=C.create_string_buffer(n);assert fontdata(dc,tag,0,table,n)==n
        assert table.raw==font.getTableData('name'),'Unexpected font substitution or changed name table'
        matrix=MAT2(FIXED(0,1),FIXED(0,0),FIXED(0,0),FIXED(0,1))
        for gid,name in enumerate(font.getGlyphOrder()):
            m=METRICS();result=outline(dc,gid,0x80,C.byref(m),0,None,C.byref(matrix))
            assert result!=0xFFFFFFFF,(gid,name)
            if font['glyf'][name].numberOfContours:assert m.w>0 and m.h>0,(gid,name)
            glyph_count+=1
        for cp,name in font.getBestCmap().items():
            if cp>0xFFFF:continue
            ids=(W.WORD*1)();assert indices(dc,chr(cp),1,ids,1)!=0xFFFFFFFF
            assert ids[0]==font.getGlyphID(name),(cp,name)
            char_count+=1
        font.close()
    finally:
        if old and dc:select(dc,old)
        if font_handle:assert delete(font_handle)
        if dc:assert deletedc(dc)
        if resource:assert remove(resource)
    result=dict(status='PASS',font_sha256=hashlib.sha256(raw).hexdigest(),
                exact_name_table=True,glyph_metrics=glyph_count,bmp_mappings=char_count,
                process_private=True,resource_removed=True,global_install=False,
                limitation='Native GDI intake and metrics; no claim of GDI OpenType shaping, Word export or universal rasterizer certification for this metadata-only build.')
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build/native-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: private Windows intake, exact OFL metadata, {glyph_count} glyph metrics and {char_count} BMP mappings; font resource removed')
