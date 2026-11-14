"""Offline Malay checks with an explicit scope and a shrinking legacy baseline.

Missing ledger entries are gaps, never waivable lesson violations. No reference
or lesson text is modified. Structural/scope errors cannot be waived.

Stage-aware rules (Stage 2 build step 2): affix gates, whole-word exemptions,
look-alike roots, register pairs, particles and disallowed forms come from
curriculum/stage-rules.json, which Kata-Kata's affix guard reads too. A ber-,
meN-, -kan, -i or accident ter- form passes only when every gate of its families
is open in the unit's chapter and its own ledger row is placed at or before it.
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
RULES_FILE='curriculum/stage-rules.json'
PROPER=set('a b c d emi farah osaka jepun pj shah alam kl sentral pasar seni aki mei qr rm am pm'.split())
NUMBERS=set('sifar kosong satu dua tiga empat lima enam tujuh lapan sembilan sepuluh sebelas belas puluh ratus ribu juta'.split())
PROPER_FILE='curriculum/malay-proper-nouns.json'
MENTIONS_FILE='curriculum/malay-mentions.json'
def tokens(s):return re.findall(r"[a-z]+(?:[-'][a-z]+)*",s.lower())
def norm(s):return ' '.join(tokens(s))
def read_json(path):return json.loads(Path(path).read_text())
def key(unit,check,term):return '|'.join((unit,check,term))
def chapter_id(s):
 m=re.search(r'ms-c(\d+)',s or '');return int(m[1]) if m else None
# Gates, whole words, look-alike roots, register pairs and disallowed forms are shared with Kata-Kata's
# affix guard through one data file (its "format" key documents it).
RULES=read_json(ROOT/RULES_FILE)
GATES={g['family']:g['chapter'] for g in RULES['affix_gates']}
INDONESIAN=dict(RULES['disallowed_forms'])
REGISTER={p['spoken']:p['standard'] for p in RULES['register_pairs']}
ROOTS=set(RULES['lookalike_roots']['kata_kata_allow_list'].split())|set(RULES['lookalike_roots']['sam_local'])
# Ledger "Affix tag" tokens that name a gated family ('ter-' is split into superlative or accident later).
TAG_FAMILY={'ber-':'ber-','meN-':'meN-','-kan':'-kan','-i':'-i','ter-':'ter-','di-':'di-'}
# Notes in the place column that never place a row ("moved from Ch2", "reviewed in Ch7", ...).
PLACE_NOTE=re.compile(r'(?:moved from|reviewed in|reused|was|waits for)\s+Ch\s*\d+',re.I)
def placed_chapter(place):
 """Chapter from the ledger place column only; notes and retired rows never place a row."""
 if place.strip().lower().startswith('retired'):return None
 found=[int(x) for x in re.findall(r'Ch\s*(\d+)',PLACE_NOTE.sub('',place))]
 return min(found) if found else None
# Reverse meN- and other prefixes (nasal changes undone) to find a candidate base.
UNPREFIX=[('menge',['']),('meny',['s']),('meng',['','k']),('mem',['','p']),('men',['','t']),('me',['']),('di',['']),('ber',['']),('be',['']),('ter',[''])]

class Checker:
 def __init__(self,root=ROOT):
  self.root=Path(root);self.entries=defaultdict(list);self.cards={};self.chunks=[]
  for row in csv.DictReader(io.StringIO((self.root/'curriculum/reference/katakata/malay-ledger.csv').read_text())):
   # Placement is read strictly from the place column (stage-rules.json, "stage_aware_rule").
   row['_chapter']=placed_chapter(row['Kata-Kata place'])
   for form in re.sub(r'\([^)]*\)','',row['Malay']).split('/'):
    if norm(form):self.entries[norm(form)].append(row)
  # Every pinned Kata-Kata chapter file, not a fixed c01-c09 range.
  for path in sorted((self.root/'curriculum/reference/katakata').glob('c[0-9][0-9].json')):
   n=int(path.stem[1:]);pack=read_json(path)
   for c in pack['cards']:
    for v in c['term'].split(' / '):
     self.cards.setdefault(norm(v),[]).append(c)
     if c['affix_tag'] in ['chunk','chunk*','lex'] or c.get('recognise_only'):self.chunks.append((norm(v),n))
  # Ledger rows tagged chunk, chunk* or lex are whole words or phrases at their own chapter, like chunk cards.
  self.chunks+=sorted({(t,r['_chapter']) for t,rows in self.entries.items() for r in rows
                       if r['Affix tag'] in ['chunk','chunk*','lex'] and r['_chapter'] is not None and r['Review status']!='Retired'})
  rules=read_json(self.root/RULES_FILE)
  self.gates={g['family']:g['chapter'] for g in rules['affix_gates']}
  self.disallowed=dict(rules['disallowed_forms'])
  self.pairs=[(p['spoken'],p['standard'],p['from_chapter']) for p in rules['register_pairs']]
  self.particles=[p['form'] for p in rules['particles']]
  self.not_particle={w for p in rules['particles'] for w in p.get('not_particle',[])}
  self.whole_words=[(w['form'],w['chapter']) for w in rules['whole_words']]
  self.superlatives=set(rules['ter_superlatives'])
  lookalike=rules['lookalike_roots']
  self.roots=set(lookalike['kata_kata_allow_list'].split())|set(lookalike['sam_local'])|set(read_json(self.root/'curriculum/malay-roots.json')['roots'])
  mentions=self.root/MENTIONS_FILE
  self.mentions={norm(k):v for k,v in read_json(mentions)['mentions'].items()} if mentions.exists() else {}
  # Names of people, places and organisations are not vocabulary (step 4 list).
  names=read_json(self.root/PROPER_FILE)['names'] if (self.root/PROPER_FILE).exists() else []
  self.proper=PROPER|{t for name in names for t in tokens(name)}
  self.maxlen=max(len(t.split()) for t in self.entries)
  self.known=set(self.entries)|set(self.cards)|self.roots
 def compositional(self,term,parts):
  return all(r['_chapter'] is None for r in self.entries[term]) and all(t in self.entries for t in parts)
 def known_by(self,term,ch):
  return any(r['_chapter'] is not None and r['_chapter']<=ch for r in self.entries.get(term,[]))
 def noun(self,t):return any(c['pos'] in ['n','noun','counter','num'] for c in self.cards.get(t,[])) or any(r['POS'] in ['n','noun','counter'] for r in self.entries.get(t,[]))
 def derivation(self,w,ch):
  """Productive forms only after their rule; root is checked separately."""
  if ch is None:return None
  g=self.gates
  if w.startswith('ke') and w[2:] in NUMBERS and ch>=g['ke- ordinal']:return (w[2:],'ke- ordinal')
  if w.endswith('nya') and len(w)>4 and ch>=g['-nya'] and (w[:-3] in self.entries or w[:-3] in self.cards or w=='ceritanya'):return (w[:-3],'-nya')
  if w.endswith('kah') and len(w)>4 and ch>=g['-kah']:return (w[:-3],'-kah')
  # Written particle «lah» joins the word (takpelah, tidak mengapalah), like -kah, once the particle's own ledger row is placed (chapter 17).
  # Never a ledger word (sekolah) or a listed non-particle (adalah, masalah); the rest must be a known form.
  if w.endswith('lah') and len(w)>5 and w not in self.entries and w not in self.not_particle and self.placed_by('lah',ch) and w[:-3] in self.known:return (w[:-3],'-lah')
  if w.startswith('se') and len(w)>3:
   base=w[2:]
   # Chapter 4 time nouns and chapter 8 counters follow their own base placement.
   if self.noun(base):return (base,'se- noun; base chapter checked separately')
   if ch>=g['se- comparison'] and self.known_by(base,ch) and any(c['pos']=='adj' for c in self.cards.get(base,[])):return (base,'se- comparison')
  if w.startswith('di') and ch>=g['di-'] and self.known_by(w[2:],ch):return (w[2:],'di- passive')
  if w.startswith('ter') and ch>=g['ter- superlative'] and self.superlative(w) and self.known_by(w[3:],ch):return (w[3:],'ter- superlative')
  if w.endswith('an') and ch>=g['-an'] and self.known_by(w[:-2],ch) and any(c['pos']=='v' for c in self.cards.get(w[:-2],[])):return (w[:-2],'-an nominalisation')
  return None
 def superlative(self,w):
  """Chapter 6 superlative: a listed whole word, or ter- + an adjective with no ledger row of its own.
  Any other ter- word (tertinggal, terlepas) is the chapter 16 accident family."""
  if w in self.superlatives:return True
  return w.startswith('ter') and w not in self.entries and any(c['pos']=='adj' for c in self.cards.get(w[3:],[]))
 def bases(self,w):
  out={w}
  for p,adds in UNPREFIX:
   if w.startswith(p) and len(w)-len(p)>=3:out.update(a+w[len(p):] for a in adds)
  return out
 def is_base(self,b):return len(b)>=3 and b in self.known
 def shape_families(self,w):
  """Families read from spelling alone (stage-rules.json, format.shape_tests)."""
  f=set()
  if w.startswith('ber') or re.match(r'^be[kl]',w):f.add('ber-')
  if re.match(r'^me[^aeiou\W]',w):f.add('meN-')
  if w.endswith('kan') and len(w)>5 and any(self.is_base(b) for b in self.bases(w[:-3])):f.add('-kan')
  if w.endswith('i') and len(w)>4 and re.match(r'^(me|di)',w) and any(self.is_base(b[:-1]) for b in self.bases(w)-{w} if b.endswith('i')):f.add('-i')
  if w.startswith('ter') and len(w)>5 and self.is_base(w[3:]):f.add('ter-')
  return f
 def families(self,w,ch):
  """Gated Stage 2 families of one word (stage-rules.json, format.family_resolution)."""
  if w in self.roots or any(form==w and (ch is None or ch>=first) for form,first in self.whole_words):return set()
  tags=[t for r in self.entries.get(w,[]) for t in r['Affix tag'].split()]
  if any(t!='root' for t in tags):fam={TAG_FAMILY[t] for t in tags if t in TAG_FAMILY}
  else:fam=self.shape_families(w)
  if 'ter-' in fam:
   fam.discard('ter-')
   if not self.superlative(w):fam.add('ter- accident')
  return fam
 def placed_by(self,w,ch):
  return any(r['_chapter'] is not None and r['_chapter']<=ch and r['Review status']!='Retired' for r in self.entries.get(w,[]))
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
   # Disallowed (Indonesian) forms, as whole words and inside hyphenated words. A ‹…› mention may quote
   # one only as a "do not use" note listed with its source in malay-mentions.json.
   parts=set(ts)|{p for t in ts for p in t.split('-')}
   note=s['kind']=='mention' and 'do not use' in self.mentions.get(text,'').lower()
   for bad,good in self.disallowed.items():
    # A form of two words («tanda tangan») is matched as the two words in that order, not as its parts.
    found=bad in parts or (' ' in bad and re.search(r'(?<![\w-])'+re.escape(bad)+r'(?![\w-])',text))
    if found and not note:add(violations,s,'malaysian-form',bad,'Disallowed (Indonesian) form; use '+good)
   # A mention (root or standard form quoted from a Kata-Kata note) is not taught
   # vocabulary: only the Malaysian-form check applies; its allow-list is checked by the suite builder.
   if s['kind']=='mention':continue
   for spoken,standard,first in self.pairs:
    if ch is not None and ch<first:continue
    if re.search(r'(?<!\w)'+re.escape(spoken)+r'(?!\w)',text):
     if (seq,standard) not in seen_standard:add(violations,s,'register',spoken,'Standard '+standard+' has no earlier target-language teaching occurrence.')
     if (seq,spoken) not in labelled and not re.search(r'\bspoken\b',s.get('source_text',''),re.I):add(violations,s,'register',spoken,'Spoken form lacks an explicit spoken label in prior teaching.')
   # R4: «lah» and «kan» are recognition and optional production, so no answer key may require them.
   if s['kind']=='test' and s['source'].endswith('|answer_key'):
    for w in ts:
     for particle in self.particles:
      if w==particle or (particle=='lah' and w.endswith('lah') and w not in self.entries and w not in self.not_particle and w[:-3] in self.known):
       add(violations,s,'register',particle,'Particle «'+particle+'» is optional production (R4); a test answer key must not require it.')
   # Do not turn a phrase exemption into a global exemption for its individual words.
   exempt=set();g=self.gates
   for phrase,first in self.chunks+self.whole_words:
    if ch is not None and first<=ch and re.search(r'(?<!\w)'+re.escape(phrase)+r'(?!\w)',text):exempt.update(tokens(phrase))
   for w in set(ts)-self.proper:
    if ch is not None and w not in exempt:
     early=[]
     if ch<g['ke- ordinal'] and w.startswith('ke') and w[2:] in NUMBERS:early.append(f"ke- ordinal before chapter {g['ke- ordinal']}")
     if ch<g['-nya'] and w.endswith('nya') and (w[:-3] in self.entries or w=='ceritanya'):early.append(f"-nya before chapter {g['-nya']}")
     if ch<g['-kah'] and w.endswith('kah') and w[:-3] in self.entries:early.append(f"-kah before chapter {g['-kah']}")
     if ch<g['di-'] and w.startswith('di') and w[2:] in self.entries and any(c['pos']=='v' for c in self.cards.get(w[2:],[])):early.append(f"di- passive before chapter {g['di-']}")
     if ch<g['ter- superlative'] and w.startswith('ter') and any(c['pos']=='adj' for c in self.cards.get(w[3:],[])):early.append(f"ter- superlative before chapter {g['ter- superlative']}")
     for reason in early:add(violations,s,'affix',w,reason)
    derived_form=self.derivation(w,ch)
    affix_base=derived_form[0] if derived_form else w
    if affix_base not in self.roots and affix_base not in exempt:
     if ch is not None and ch<g['ber-'] and (affix_base.startswith('ber') or re.match(r'^be[kl]',affix_base)):add(violations,s,'affix',w,f"ber-/be- shaped form before chapter {g['ber-']}; no taught chunk or root exemption.")
     if ch is not None and ch<g['meN-'] and re.match(r'^me[^aeiou\W]',affix_base):add(violations,s,'affix',w,f"me- shaped form before chapter {g['meN-']}; no taught chunk or root exemption.")
    # Stage-aware rule (stage-rules.json): every gate of the word's families is open, and the form's own
    # ledger row (or, for a Stage 1 derivation, its base's row) is placed at or before this chapter.
    if ch is not None and w not in exempt and affix_base not in exempt:
     fam=self.families(affix_base,ch)
     for f in sorted(fam):
      if ch<g[f]:add(violations,s,'affix',w,f'{f} form before chapter {g[f]}.')
     if fam and all(ch>=g[f] for f in fam) and not (self.placed_by(w,ch) or (derived_form and self.placed_by(affix_base,ch))):
      add(violations,s,'affix',w,f'{"/".join(sorted(fam))} form has no ledger row placed at or before chapter {ch}.')
   i=0
   while i<len(ts):
    if ts[i] in self.proper:i+=1;continue
    matched=None
    for size in range(min(self.maxlen,len(ts)-i),0,-1):
     term=' '.join(ts[i:i+size])
     # An unplaced multi-word row (e.g. a Hanashishou phrase "encik pula") does not
     # override placed single words it is built from; match the words instead.
     if term in self.entries and size>1 and self.compositional(term,ts[i:i+size]):continue
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
    for spoken,standard,first in self.pairs:
     if re.search(r'(?<!\w)'+re.escape(standard)+r'(?!\w)',text):seen_standard.add((seq,standard))
     if spoken in text and re.search(r'\bspoken\b',s.get('source_text',''),re.I):labelled.add((seq,spoken))
  return {'violations':violations,'ledger_gaps':gaps,'derivations':list({json.dumps(x,sort_keys=True):x for x in derived}.values()),'unplaced_units':sorted(unplaced)}

def collect_segments(lessons,catalogue,scope):
 by_title={l['title']:l for l in lessons};segments=[];seen=set();scope_errors=[]
 for c in catalogue['components']:
  if c['language']!='Malay' or (c['component_type']=='Teaching plan' and not c.get('authored')):continue
  # A2 extension stays separate from the Stage 1 sequence in both linked chapters.
  unit='ms-extension-a2-lunch' if c['source_title']=='Lunch at a Malaysian stall' else c.get('check_unit') or c['unit_id'] or c['chapter_id'] or 'ms-supplementary-'+c['level'].lower()
  chapter=None if unit=='ms-extension-a2-lunch' else chapter_id(c['chapter_id'])
  l=by_title[c['source_title']]
  # Step 4 suites mark every Malay span, so their explainers, keys and plans are checked too.
  for pi in c.get('check_indices',c['page_indices']):
   for li,line in enumerate(l['pages'][pi]['lines']):
    source=f'{l["title"]}|{pi}|{li}'
    if (unit,source) in seen:continue
    seen.add((unit,source));entry=scope['lines'].get(source)
    if not entry or entry['source_text']!=line:scope_errors.append(source);continue
    for t in entry['target_spans']:
     if t not in line:raise ValueError('Target span not in source: '+source)
     segments.append({'unit':unit,'chapter':chapter,'source':source,'source_text':line,'kind':entry['kind'],'text':t})
    for t in entry.get('mention_spans',[]):
     if t not in line:raise ValueError('Mention span not in source: '+source)
     segments.append({'unit':unit,'chapter':chapter,'source':source,'source_text':line,'kind':'mention','text':t})
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
    segments.append({'unit':c.get('check_unit') or c['unit_id'] or c['chapter_id'],'chapter':chapter_id(c['chapter_id']),'source':source,'source_text':value,'kind':'test','text':t})
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

def run_checks(lessons,catalogue,root=ROOT,authored_scope=None):
 """authored_scope: scope entries generated from step 4 markup (every Malay span marked)."""
 root=Path(root);scope=read_json(root/'curriculum/malay-text-scope.json')
 if authored_scope:
  clash=scope['lines'].keys()&authored_scope.keys()
  if clash:raise ValueError('Authored scope collides with the reviewed scope file: '+', '.join(sorted(clash)))
  scope={**scope,'lines':{**scope['lines'],**authored_scope}}
 result=Checker(root).inspect(collect_segments(lessons,catalogue,scope))
 baseline=read_json(root/EXCEPTIONS);remaining=ratchet(baseline,root)
 missing=sorted(result['violations'].keys()-baseline.keys())
 print(f'Malay checks: {remaining} legacy exceptions remaining; {len(result["violations"])} current unit/check/term violations; {len(result["ledger_gaps"])} unit/term ledger gaps (non-blocking outside re-authored units).')
 if missing:raise ValueError('New Malay violations:\n'+'\n'.join(missing))
 # Re-authored units are ledger-only: a word missing from the ledger blocks them.
 retired=set(read_json(root/'curriculum/reauthored-units.json'))
 blocked=sorted(k for k,e in result['ledger_gaps'].items() if e['unit'] in retired)
 if blocked:raise ValueError('Re-authored units use words that are not in the ledger:\n'+'\n'.join(blocked))
 return result
