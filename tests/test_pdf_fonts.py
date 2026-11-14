"""The page bank's fonts must draw the glyphs the text asks for.

Until 14 Nov 2026 the build embedded a subset of Noto Sans CJK as a CID-keyed CFF font. Subsetting renumbers the glyphs
but keeps their old CIDs, while MuPDF writes the new glyph numbers into the page text, so every viewer drew the wrong
glyphs (Sam's chapter 1 download was unreadable, though text extraction still looked right). build.py now converts the
subset to TrueType outlines, where the glyph number is the glyph. This test fails if a CID-keyed CFF font whose CIDs
do not match its glyph numbers ever comes back.

The second problem (copying text out of a page gave odd characters: «A1» copied as «A=», «file» as «6le») is a missing ToUnicode entry. The
font's liga and locl features made the shaper draw fi, fl, ff, ffi and the digits 0 to 9 as alternate glyphs that have no Unicode value of
their own. build.py now keeps only the ccmp, vert and vrt2 features in the subset; the test below fails if any glyph the pages draw has no
ToUnicode entry."""
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

def to_unicode(doc,xref):
 """glyph id -> Unicode value from the font's ToUnicode CMap."""
 ref=doc.xref_get_key(xref,'ToUnicode')
 cmap=doc.xref_stream(int(ref[1].split()[0])).decode('latin1')
 out={}
 for block in re.findall(r'beginbfrange(.*?)endbfrange',cmap,re.S):
  for a,b,c in re.findall(r'<([0-9a-f]{4})>\s*<([0-9a-f]{4})>\s*<([0-9a-f]{4,})>',block):
   for g in range(int(a,16),int(b,16)+1):out[g]=int(c,16)+g-int(a,16)
 for block in re.findall(r'beginbfchar(.*?)endbfchar',cmap,re.S):
  for a,c in re.findall(r'<([0-9a-f]{4})>\s*<([0-9a-f]{4,})>',block):out[int(a,16)]=int(c,16)
 return out

class CopyText(unittest.TestCase):
 def test_build_keeps_no_substituting_layout_features(self):
  source=(ROOT/'build.py').read_text(encoding='utf-8')
  self.assertIn('opts.layout_features=["ccmp","vert","vrt2"]',source)
  self.assertNotIn('"liga"',source.split('opts.layout_features=',1)[1].split('\n',1)[0])
  self.assertNotIn('"locl"',source.split('opts.layout_features=',1)[1].split('\n',1)[0])

 def test_every_drawn_glyph_has_a_unicode_value(self):
  doc=bank_pdf()
  checked=0
  for number in range(0,len(doc),25):
   page=doc[number]
   fonts=[f for f in page.get_fonts(full=True) if 'CJK' in f[3]]
   if not fonts:continue
   xref=fonts[0][0]
   mapping=to_unicode(doc,xref)
   for form in [x[0] for x in page.get_xobjects() if x[1]=='fullpage']:
    stream=doc.xref_stream(form).decode('latin1')
    for hexstring in re.findall(r'<([0-9a-f]+)>',stream):
     for i in range(0,len(hexstring),4):
      gid=int(hexstring[i:i+4],16)
      self.assertIn(gid,mapping,f'page {number+1}: glyph {gid} has no ToUnicode entry')
      checked+=1
  self.assertGreater(checked,1000)

 def test_digits_and_ligature_words_extract_as_written(self):
  doc=bank_pdf()
  text=' '.join(page.get_text() for page in doc[:60])
  self.assertRegex(text,r'A1')
  self.assertRegex(text,r'(?i)different|office|file')
  self.assertNotRegex(text,r'o8ce|di5erent|6le\b')

if __name__=='__main__':unittest.main()
