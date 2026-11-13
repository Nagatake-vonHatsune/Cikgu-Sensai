"""Stage 2 build step 2: stage-aware Malay checks driven by curriculum/stage-rules.json.

The cases in curriculum/stage-rules-fixtures.json are shared with Kata-Kata's affix guard (build step 3)."""
import csv,io,json,re,unittest
from pathlib import Path
from language_checks import Checker,ROOT,placed_chapter,GATES
RULES=json.loads((ROOT/'curriculum/stage-rules.json').read_text())
FIXTURES=json.loads((ROOT/'curriculum/stage-rules-fixtures.json').read_text())['cases']

def run_case(checker,case):
 segments=[];mentions=dict(checker.mentions)
 for i,s in enumerate(case['segments']):
  ch=s['chapter'];kind=s.get('kind','model')
  source=f'test:{case["id"]}-{i}|{s["field"]}' if kind=='test' else f'fixture|{i}'
  if kind=='mention':mentions[' '.join(re.findall(r"[a-z]+(?:[-'][a-z]+)*",s['text'].lower()))]=s['mention_source']
  segments.append({'unit':s.get('unit',f'fixture-c{ch:02}'),'chapter':ch,'source':source,'text':s['text'],'source_text':s.get('source_text',s['text']),'kind':kind})
 saved=checker.mentions;checker.mentions=mentions
 try:return checker.inspect(segments)['violations']
 finally:checker.mentions=saved

class StageRulesFixtures(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.checker=Checker()
 def test_shared_fixtures(self):
  self.assertGreaterEqual(len(FIXTURES),60)
  for case in FIXTURES:
   with self.subTest(case=case['id']):
    v=run_case(self.checker,case)
    if case['expect']=='pass':self.assertEqual(v,{},case['why'])
    else:self.assertTrue(any(e['check']==case['check'] for e in v.values()),f"{case['why']}: {sorted(v)}")
 def test_required_gate_fixtures_present(self):
  ids={c['id'] for c in FIXTURES}
  for i in ['bercakap-9-fails','bercakap-10-passes','menulis-10B-fails','menulis-11A-passes','kan-suffix-11B-fails','kan-suffix-12A-passes',
            'tertinggal-15-fails','tertinggal-16-passes','whole-word-bekerja-10','whole-word-belajar-2','indonesian-berbicara-fails',
            'indonesian-in-do-not-use-note-passes','spoken-before-standard-fails','termurah-does-not-unlock-terjatuh','lah-in-answer-key-fails']:
   self.assertIn(i,ids)

class StageRulesFile(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.checker=Checker()
  cls.ledger={r['ID']:r for r in csv.DictReader(io.StringIO((ROOT/'curriculum/reference/katakata/malay-ledger.csv').read_text()))}
 def test_gates(self):
  self.assertEqual({f:GATES[f] for f in ['ber-','meN-','-kan','-i','ter- accident','ter- superlative','di-','se- + classifier']},
                   {'ber-':10,'meN-':11,'-kan':12,'-i':12,'ter- accident':16,'ter- superlative':6,'di-':9,'se- + classifier':8})
  self.assertTrue(RULES['format']['stage_aware_rule'])
 def test_whole_words_match_the_ledger(self):
  for w in RULES['whole_words']:
   row=self.ledger[w['ledger_id']]
   self.assertEqual(self.checker.entries[w['form']][0]['ID'],w['ledger_id'],w['form'])
   self.assertEqual(placed_chapter(row['Kata-Kata place']),w['chapter'],w['form'])
  self.assertTrue(set(RULES['ter_superlatives'])<={w['form'] for w in RULES['whole_words'] if w['chapter']==6})
 def test_local_roots_are_shared(self):
  local=json.loads((ROOT/'curriculum/malay-roots.json').read_text())['roots']
  self.assertEqual(set(local),set(RULES['lookalike_roots']['sam_local']))
 def test_disallowed_forms_are_not_ledger_forms(self):
  for form in RULES['disallowed_forms']:
   self.assertNotIn(form,self.checker.entries,form)
  for form in ['berbicara','perbaiki','musik','film','olahraga','apotek','kantor','mobil','uang']:self.assertIn(form,RULES['disallowed_forms'])
 def test_register_pairs(self):
  pairs={(p['spoken'],p['standard']) for p in RULES['register_pairs']}
  # Sam, 13 Nov 2026: «tidak mengapa» is not used, so «tak apa» has no standard partner.
  self.assertNotIn('tak apa',{p['spoken'] for p in RULES['register_pairs']})
  for pair in [('tak tahan','tidak tahan'),('set','setuju'),('macam tu','seperti itu'),('ni','ini'),('tu','itu'),('kat','di')]:
   self.assertIn(pair,pairs)
  self.assertEqual({p['form'] for p in RULES['particles']},{'lah','kan'})
 def test_strict_placement(self):
  self.assertEqual(placed_chapter('Ch1 (moved from Ch2; reviewed in Ch2)'),1)
  self.assertEqual(placed_chapter('Ch12 (unit 12A); Jambatan · Daily life'),12)
  self.assertEqual(placed_chapter('Dunia · Rumah terbuka (primes Ch9)'),9)
  self.assertEqual(placed_chapter('Ch15 (waits for Ch10)'),15)
  self.assertIsNone(placed_chapter('Retired: duplicate of L-0330'))
  self.assertIsNone(placed_chapter(''))
 def test_every_pinned_chapter_file_is_loaded(self):
  files=sorted((ROOT/'curriculum/reference/katakata').glob('c[0-9][0-9].json'))
  ids={c['id'] for p in files for c in json.loads(p.read_text())['cards']}
  loaded={c['id'] for cards in self.checker.cards.values() for c in cards}
  self.assertEqual(ids,loaded)
 def test_ter_rows_tagged_root_are_still_accident_ter(self):
  # L-0619, L-0621 and L-0644 carry the tag 'root' in the ledger; the shape test still gates them at 16.
  for w in ['tertinggal','terlepas','terlupa']:
   self.assertEqual(self.checker.families(w,15),{'ter- accident'},w)
  self.assertEqual(self.checker.families('termurah',6),set())
  self.assertEqual(self.checker.families('masakan',2),set())  # ledger tag -an decides, not the -kan shape

if __name__=='__main__':unittest.main()
