"""Offline Malay checks with an explicit scope and a shrinking legacy baseline.

Missing ledger entries are gaps, never waivable lesson violations. No reference
or lesson text is modified. Structural/scope errors cannot be waived.
"""
import csv
import io
import hashlib
import json
import re
import subprocess
from collections import defaultdict,Counter
from pathlib import Path
ROOT=Path(__file__).parent
EXCEPTIONS='curriculum/legacy-exceptions.json'
INDONESIAN={'nomor':'nombor','bis':'bas','apel':'epal','setelah':'selepas','beda':'beza','mobil':'kereta','toilet':'tandas','wc':'tandas','karcis':'tiket','toko':'kedai','uang':'wang / duit'}
REGISTER={'nak':'mahu','tak':'tidak','dah':'sudah','ni':'ini','tu':'itu','sikit':'sedikit','saja':'sahaja','tapi':'tetapi','macam mana':'bagaimana','macam tu':'seperti itu'}
# Exact copy of the pinned upstream guard's root allow-list, plus Sam's local file.
ROOTS=set('berat bersih belok belakang belas belum beli besar bebas beliau berus merah meja meter mesyuarat mereka mendung menu belanja menang'.split())
PROPER=set('a b c d emi farah osaka jepun pj shah alam kl sentral pasar seni aki mei qr rm am pm'.split())
NUMBERS=set('sifar kosong satu dua tiga empat lima enam tujuh lapan sembilan sepuluh sebelas belas puluh ratus ribu juta'.split())
def tokens(s):return re.findall(r"[a-z]+(?:[-'][a-z]+)*",s.lower())
def norm(s):return ' '.join(tokens(s))
def read_json(path):return json.loads(Path(path).read_text())
def key(unit,check,term):return '|'.join((unit,check,term))
def chapter_id(s):
 m=re.search(r'ms-c(\d+)',s or '');return int(m[1]) if m else None

class Checker:
 def __init__(self,root=ROOT):
  self.root=Path(root);self.entries=defaultdict(list);self.cards={};self.chunks=[]
  for row in csv.DictReader(io.StringIO((self.root/'curriculum/reference/katakata/malay-ledger.csv').read_text())):
   chapters=[int(x) for x in re.findall(r'ms-c(\d+)-',row['Kata-Kata (card IDs)'])]
   places=[int(x) for x in re.findall(r'Ch\s*(\d+)',row['Kata-Kata place'])]
   row['_chapter']=min(chapters+places) if chapters+places else None
   for form in re.sub(r'\([^)]*\)','',row['Malay']).split('/'):
    if norm(form):self.entries[norm(form)].append(row)
  for n in range(1,10):
   pack=read_json(self.root/f'curriculum/reference/katakata/c{n:02}.json')
   for c in pack['cards']:
    for v in c['term'].split(' / '):
     self.cards.setdefault(norm(v),[]).append(c)
     if c['affix_tag'] in ['chunk','chunk*','lex'] or c.get('recognise_only'):self.chunks.append((norm(v),n))
  self.roots=ROOTS|set(read_json(self.root/'curriculum/malay-roots.json')['roots'])
  self.maxlen=max(len(t.split()) for t in self.entries)
 def known_by(self,term,ch):
  return any(r['_chapter'] is not None and r['_chapter']<=ch for r in self.entries.get(term,[]))
 def noun(self,t):return any(c['pos'] in ['n','noun','counter','num'] for c in self.cards.get(t,[])) or any(r['POS'] in ['n','noun','counter'] for r in self.entries.get(t,[]))
 def derivation(self,w,ch):
  """Productive forms only after their rule; root is checked separately."""
  if ch is None:return None
  if w.startswith('ke') and w[2:] in NUMBERS and ch>=3:return (w[2:],'ke- ordinal')
  if w.endswith('nya') and len(w)>4 and ch>=2 and (w[:-3] in self.entries or w[:-3] in self.cards or w=='ceritanya'):return (w[:-3],'-nya')
  if w.endswith('kah') and len(w)>4 and ch>=2:return (w[:-3],'-kah')
  if w.startswith('se') and len(w)>3:
   base=w[2:]
   # Chapter 4 time nouns and chapter 8 counters follow their own base placement.
   if self.noun(base):return (base,'se- noun; base chapter checked separately')
   if ch>=6 and self.known_by(base,ch) and any(c['pos']=='adj' for c in self.cards.get(base,[])):return (base,'se- comparison')
  if w.startswith('di') and ch>=9 and self.known_by(w[2:],ch):return (w[2:],'di- passive')
  if w.startswith('ter') and ch>=6 and self.known_by(w[3:],ch) and any(c['pos']=='adj' for c in self.cards.get(w[3:],[])):return (w[3:],'ter- superlative')
  if w.endswith('an') and ch>=2 and self.known_by(w[:-2],ch) and any(c['pos']=='v' for c in self.cards.get(w[:-2],[])):return (w[:-2],'-an nominalisation')
  return None
 def inspect(self,segments):
  violations={};gaps={};derived=[];unplaced=set();seen_standard=set();labelled=set()
  def add(dst,s,check,term,reason):
   k=key(s['unit'],check,term)
   entry=dst.setdefault(k,{'unit':s['unit'],'check':check,'term':term,'reasons':[], 'evidence':[]})
   if reason not in entry['reasons']:entry['reasons'].append(reason)
   ev={'source':s['source'],'text':s['text']}
   if ev not in entry['evidence']:entry['evidence'].append(ev)
  for s in segments:
   text=norm(s['text']);ts=tokens(s['text']);ch=s['chapter'];seq=s['unit'] if ch is None else 'stage'
   if ch is None:unplaced.add(s['unit'])
   for bad,good in INDONESIAN.items():
    if bad in ts:add(violations,s,'malaysian-form',bad,'Charter-listed form; use '+good)
   for spoken,standard in REGISTER.items():
    if re.search(r'(?<!\w)'+re.escape(spoken)+r'(?!\w)',text):
     if (seq,standard) not in seen_standard:add(violations,s,'register',spoken,'Standard '+standard+' has no earlier target-language teaching occurrence.')
     if (seq,spoken) not in labelled and not re.search(r'\bspoken\b',s.get('source_text',''),re.I):add(violations,s,'register',spoken,'Spoken form lacks an explicit spoken label in prior teaching.')
   # Do not turn a phrase exemption into a global exemption for its individual words.
   exempt=set()
   for phrase,first in self.chunks:
    if ch is not None and first<=ch and re.search(r'(?<!\w)'+re.escape(phrase)+r'(?!\w)',text):exempt.update(tokens(phrase))
   for w in set(ts)-PROPER:
    if ch is not None and w not in exempt:
     early=[]
     if ch<3 and w.startswith('ke') and w[2:] in NUMBERS:early.append('ke- ordinal before chapter 3')
     if ch<2 and w.endswith('nya') and (w[:-3] in self.entries or w=='ceritanya'):early.append('-nya before chapter 2')
     if ch<2 and w.endswith('kah') and w[:-3] in self.entries:early.append('-kah before chapter 2')
     if ch<9 and w.startswith('di') and w[2:] in self.entries and any(c['pos']=='v' for c in self.cards.get(w[2:],[])):early.append('di- passive before chapter 9')
     if ch<6 and w.startswith('ter') and any(c['pos']=='adj' for c in self.cards.get(w[3:],[])):early.append('ter- superlative before chapter 6')
     for reason in early:add(violations,s,'affix',w,reason)
    derived_form=self.derivation(w,ch)
    affix_base=derived_form[0] if derived_form else w
    if affix_base not in self.roots and affix_base not in exempt:
     if ch is not None and ch<10 and (affix_base.startswith('ber') or re.match(r'^be[kl]',affix_base)):add(violations,s,'affix',w,'ber-/be- shaped form before chapter 10; no taught chunk or root exemption.')
     if ch is not None and ch<11 and re.match(r'^me[^aeiou\W]',affix_base):add(violations,s,'affix',w,'me- shaped form before chapter 11; no taught chunk or root exemption.')
   i=0
   while i<len(ts):
    if ts[i] in PROPER:i+=1;continue
    matched=None
    for size in range(min(self.maxlen,len(ts)-i),0,-1):
     term=' '.join(ts[i:i+size])
     if term in self.entries:matched=(term,size);break
    term,size=matched if matched else (ts[i],1)
    deriv=self.derivation(term,ch) if size==1 else None
    # A regular derivation may be absent as a surface form, but its base still
    # needs ledger coverage and chapter placement.
    if deriv:
     base,rule=deriv;derived.append({'unit':s['unit'],'term':term,'base':base,'rule':rule})
     term=base
    rows=self.entries.get(term,[])
    if not rows:add(gaps,s,'ledger gap',term,'No exact ledger entry for this term/base; not a lesson violation.')
    elif ch is not None:
     taught=[r['_chapter'] for r in rows if r['_chapter'] is not None]
     if not taught:add(violations,s,'ledger',term,'Ledger entry exists but has no chapter assignment.')
     elif min(taught)>ch:add(violations,s,'ledger',term,f'First assigned chapter {min(taught)}; used in chapter {ch}.')
    i+=size
   # Only vocabulary/pattern/model teaching counts, never rubric or a task.
   if s['kind'] in ['vocabulary','model']:
    for spoken,standard in REGISTER.items():
     if re.search(r'(?<!\w)'+re.escape(standard)+r'(?!\w)',text):seen_standard.add((seq,standard))
     if spoken in text and re.search(r'\bspoken\b',s.get('source_text',''),re.I):labelled.add((seq,spoken))
  return {'violations':violations,'ledger_gaps':gaps,'derivations':list({json.dumps(x,sort_keys=True):x for x in derived}.values()),'unplaced_units':sorted(unplaced)}

def collect_segments(lessons,catalogue,scope):
 by_title={l['title']:l for l in lessons};segments=[];seen=set();scope_errors=[]
 for c in catalogue['components']:
  if c['language']!='Malay' or c['component_type']=='Teaching plan':continue
  # A2 extension stays separate from the Stage 1 sequence in both linked chapters.
  unit='ms-extension-a2-lunch' if c['source_title']=='Lunch at a Malaysian stall' else c['unit_id'] or c['chapter_id'] or 'ms-supplementary-'+c['level'].lower()
  chapter=None if unit=='ms-extension-a2-lunch' else chapter_id(c['chapter_id'])
  l=by_title[c['source_title']]
  for pi in c['page_indices']:
   for li,line in enumerate(l['pages'][pi]['lines']):
    source=f'{l["title"]}|{pi}|{li}'
    if (unit,source) in seen:continue
    seen.add((unit,source));entry=scope['lines'].get(source)
    if not entry or entry['source_text']!=line:scope_errors.append(source);continue
    for t in entry['target_spans']:
     if t not in line:raise ValueError('Target span not in source: '+source)
     segments.append({'unit':unit,'chapter':chapter,'source':source,'source_text':line,'kind':entry['kind'],'text':t})
 for item in catalogue['test_items']:
  c=next(c for c in catalogue['components'] if c['id']==item['component_id'])
  if c['language']!='Malay':continue
  for field in ['prompt','answer_key']:
   value=item[field]
   if not isinstance(value,str):raise ValueError('Test target text must be a string')
   # New tests have explicit target/rubric scope too; answer language is tested.
   source=f'test:{item["id"]}|{field}';entry=scope['lines'].get(source)
   if not entry or entry['source_text']!=value:scope_errors.append(source);continue
   for t in entry['target_spans']:
    if t not in value:raise ValueError('Invalid test target span')
    segments.append({'unit':c['unit_id'] or c['chapter_id'],'chapter':chapter_id(c['chapter_id']),'source':source,'source_text':value,'kind':'test','text':t})
 if scope_errors:raise ValueError('Unreviewed Malay target/rubric scope: '+', '.join(scope_errors))
 return segments

def validate_baseline(current,previous,retired=()):
 if not isinstance(current,dict):raise ValueError('Exception file must be keyed by unit|check|term')
 for k,e in current.items():
  if k!=key(e['unit'],e['check'],e['term']):raise ValueError('Exception key mismatch')
  if e['check'] not in ['ledger','register','affix','malaysian-form']:raise ValueError('Ledger gaps cannot be legacy exceptions')
  if e['unit'] in retired:raise ValueError('Re-authored unit cannot retain exceptions: '+e['unit'])
  if k not in previous or e!=previous[k]:raise ValueError('Legacy exceptions may only shrink; added/edited: '+k)

def ratchet(current,root=ROOT):
 root=Path(root);lock=read_json(root/'curriculum/legacy-baseline-lock.json')
 for k,e in current.items():
  digest=hashlib.sha256(json.dumps(e,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
  if lock['entry_sha256'].get(k)!=digest:raise ValueError('Not in frozen baseline: '+k)
 def git(*args):return subprocess.run(['git',*args],cwd=root,capture_output=True,text=True)
 if git('rev-parse','--is-shallow-repository').stdout.strip()=='true':raise ValueError('Full Git history is required for the shrink-only check')
 head=git('show','HEAD:'+EXCEPTIONS)
 if head.returncode==0:
  previous=json.loads(head.stdout);validate_baseline(current,previous)
  # On clean CI HEAD already contains this change; compare its previous version.
  revs=git('log','-2','--format=%H','HEAD','--',EXCEPTIONS).stdout.splitlines()
  if len(revs)>1:
   older=git('show',revs[1]+':'+EXCEPTIONS)
   if older.returncode:raise ValueError('Fetch baseline history to enforce shrink-only policy')
   validate_baseline(previous,json.loads(older.stdout))
 elif git('rev-parse','--is-inside-work-tree').returncode:
  raise ValueError('Build requires Git history for the shrink-only baseline check')
 retired=read_json(root/'curriculum/reauthored-units.json')
 old_retired=git('show','HEAD:curriculum/reauthored-units.json')
 if old_retired.returncode==0 and not set(json.loads(old_retired.stdout))<=set(retired):raise ValueError('Re-authored units cannot return to legacy status')
 validate_baseline(current,current,retired)
 return len(current)

def run_checks(lessons,catalogue,root=ROOT):
 root=Path(root);scope=read_json(root/'curriculum/malay-text-scope.json')
 result=Checker(root).inspect(collect_segments(lessons,catalogue,scope))
 baseline=read_json(root/EXCEPTIONS);remaining=ratchet(baseline,root)
 missing=sorted(result['violations'].keys()-baseline.keys())
 print(f'Malay checks: {remaining} legacy exceptions remaining; {len(result["violations"])} current unit/check/term violations; {len(result["ledger_gaps"])} unit/term ledger gaps (non-blocking).')
 if missing:raise ValueError('New Malay violations:\n'+'\n'.join(missing))
 return result
