"""The page bank's fonts must draw the glyphs the text asks for.

Until 14 Nov 2026 the build embedded a subset of Noto Sans CJK as a CID-keyed CFF font. Subsetting renumbers the glyphs
but keeps their old CIDs, while MuPDF writes the new glyph numbers into the page text, so every viewer drew the wrong
glyphs (Sam's chapter 1 download was unreadable, though text extraction still looked right). build.py now converts the
subset to TrueType outlines, where the glyph number is the glyph. This test fails if a CID-keyed CFF font whose CIDs
do not match its glyph numbers ever comes back."""
import base64,io,re,unittest
from pathlib import Path
import pymupdf
from fontTools.cffLib import CFFFontSet
from fontTools.ttLib import TTFont

ROOT=Path(__file__).resolve().parents[1]

def bank_pdf():
 text=(ROOT/'dist/bank.js').read_text()
 return pymupdf.open('pdf',base64.b64decode(re.search(r"const bankPDF='([^']+)'",text).group(1)))

def cid_mismatches(cff):
 # In a CID-keyed CFF font, glyph names are cidNNNNN; a viewer finds glyph N by its CID, so CID N must be glyph N.
 top=cff[cff.fontNames[0]]
 if not hasattr(top,'ROS'):return []
 order=top.charset
 return [name for gid,name in enumerate(order) if name.startswith('cid') and int(name[3:])!=gid]

class PdfFonts(unittest.TestCase):
 def test_body_font_is_truetype(self):
  doc=bank_pdf()
  names={}
  for page in doc:
   for xref,ext,ftype,basefont,*_ in page.get_fonts():names[xref]=(ext,basefont)
  body=[x for x,(ext,base) in names.items() if 'CJK' in base]
  self.assertTrue(body,'no Noto Sans CJK body font in the page bank')
  for xref in body:self.assertEqual(names[xref][0],'ttf',f'body font {names[xref][1]} is embedded as {names[xref][0]}, not TrueType')

 def test_no_cff_font_with_shifted_cids(self):
  doc=bank_pdf()
  seen=set()
  for page in doc:
   for xref,ext,*_ in page.get_fonts():
    if xref in seen or ext!='cff' and ext!='otf':continue
    seen.add(xref)
    name,ext,_,buffer=doc.extract_font(xref)
    if not buffer:continue
    try:
     cff=CFFFontSet();cff.decompile(io.BytesIO(buffer),None)
    except Exception:
     font=TTFont(io.BytesIO(buffer))
     if 'CFF ' not in font:continue
     cff=font['CFF '].cff
    self.assertEqual(cid_mismatches(cff)[:5],[],f'font {name} (xref {xref}) has CIDs that do not match its glyph numbers')

if __name__=='__main__':unittest.main()
