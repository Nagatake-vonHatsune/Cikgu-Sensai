import copy,json,subprocess,unittest
from pathlib import Path
from language_checks import Checker,collect_segments,validate_baseline,ratchet,ROOT,INDONESIAN
from catalogue import make_catalogue
from unittest.mock import patch
from language_checks import run_checks
class LanguageChecksTests(unittest.TestCase):
 def setUp(self):self.checker=Checker()
 def seg(self,text,ch=3,unit=None,kind='model',source_text=None):return {'unit':unit or f'ms-c{ch:02}','chapter':ch,'source':'fixture','text':text,'source_text':source_text or text,'kind':kind}
 def test_all_known_indonesian_forms(self):
  r=self.checker.inspect([self.seg(' '.join(INDONESIAN))]);self.assertEqual({x['term'] for x in r['violations'].values() if x['check']=='malaysian-form'},set(INDONESIAN))
 def test_root_and_chunk_affix_rules(self):
  for term in ['beri','mesej','memang','mesti','beritahu','besar','merah','Selamat berkenalan']:
   r=self.checker.inspect([self.seg(term,1)]);self.assertFalse(any(x['check']=='affix' for x in r['violations'].values()),term)
  for term,ch in [('berjalan',9),('membeli',10),('berjalanlah',1)]:
   self.assertTrue(any(x['check']=='affix' for x in self.checker.inspect([self.seg(term,ch)])['violations'].values()))
  for term,ch in [('berjalan',10),('membeli',11)]:self.assertFalse(any(x['check']=='affix' for x in self.checker.inspect([self.seg(term,ch)])['violations'].values()))
 def test_derivations_and_base_gap(self):
  for term,ch in [('keempat',3),('seminggu',4)]:
   r=self.checker.inspect([self.seg(term,ch)]);self.assertFalse(r['violations']);self.assertFalse(r['ledger_gaps'])
  self.assertTrue(any(e['check']=='affix' for e in self.checker.inspect([self.seg('keempat',2)])['violations'].values()));self.assertIsNone(self.checker.derivation('keempat',2));self.assertIsNone(self.checker.derivation('ceritanya',1))
  r=self.checker.inspect([self.seg('ceritanya',6)]);self.assertEqual({x['term'] for x in r['ledger_gaps'].values()},{'cerita'})
  r=self.checker.inspect([self.seg('sebiji',3)]);self.assertTrue(any(x['check']=='ledger' and x['term']=='biji' for x in r['violations'].values()))
 def test_gap_is_not_ledger_violation(self):
  r=self.checker.inspect([self.seg('lucu',3)]);self.assertTrue(r['ledger_gaps']);self.assertFalse(r['violations'])
  r=self.checker.inspect([self.seg('biji',3)]);self.assertTrue(r['violations']);self.assertFalse(r['ledger_gaps'])
 def test_register_requires_order_and_label(self):
  r=self.checker.inspect([self.seg('nak'),self.seg('mahu',kind='vocabulary')]);self.assertTrue(any(x['check']=='register' for x in r['violations'].values()))
  r=self.checker.inspect([self.seg('mahu',kind='vocabulary'),self.seg('nak',kind='vocabulary',source_text='nak [spoken]'),self.seg('Saya nak')]);self.assertFalse(any(x['check']=='register' for x in r['violations'].values()))
  r=self.checker.inspect([self.seg('mahu',kind='task'),self.seg('nak')]);self.assertTrue(any(x['check']=='register' for x in r['violations'].values()))
 def test_scope_and_test_items(self):
  lesson={'title':'fixture','pages':[{'lines':['explainer nomor']}]*3+[{'lines':['Pilih nomor. Saya beli epal.']}]+[{'lines':['key mobil']}]}
  c={'id':'c','source_title':'fixture','language':'Malay','component_type':'Task','unit_id':'ms-c03b','chapter_id':'ms-c03','page_indices':[3]}
  cat={'components':[c],'test_items':[]};scope={'lines':{'fixture|3|0':{'source_text':'Pilih nomor. Saya beli epal.','target_spans':['Saya beli epal.'],'kind':'task'}}}
  ss=collect_segments([lesson],cat,scope);self.assertFalse(any(x['check']=='malaysian-form' for x in self.checker.inspect(ss)['violations'].values()))
  changed=copy.deepcopy(lesson);changed['pages'][3]['lines'][0]+=' mobil'
  with self.assertRaises(ValueError):collect_segments([changed],cat,scope)
  cat['test_items']=[{'id':'t','component_id':'c','prompt':'nomor','answer_key':'epal'}]
  scope['lines'].update({'test:t|prompt':{'source_text':'nomor','target_spans':['nomor']},'test:t|answer_key':{'source_text':'epal','target_spans':['epal']}})
  self.assertTrue(any(x['check']=='malaysian-form' for x in self.checker.inspect(collect_segments([lesson],cat,scope))['violations'].values()))
 def test_baseline_shrink_only(self):
  old=json.loads((ROOT/'curriculum/legacy-exceptions.json').read_text());small=dict(list(old.items())[1:]);validate_baseline(small,old)
  with self.assertRaises(ValueError):validate_baseline(old,small)
  with self.assertRaises(ValueError):validate_baseline(old,old,[next(iter(old.values()))['unit']])
  modified=copy.deepcopy(old);next(iter(modified.values()))['reasons'].append('changed')
  with self.assertRaises(ValueError):validate_baseline(modified,old)
  self.assertEqual(ratchet(old),len(old))
 def test_build_gate_rejects_unlisted_violation(self):
  with patch('language_checks.collect_segments',return_value=[self.seg('nomor',1)]):
   with self.assertRaisesRegex(ValueError,'New Malay violations'):
    run_checks([],{'components':[],'test_items':[]})
  # A new missing word is deliberately non-blocking under Sam's step 3 policy.
  with patch('language_checks.collect_segments',return_value=[self.seg('lucu',7,unit='ms-c07')]):
   result=run_checks([],{'components':[],'test_items':[]})
   self.assertTrue(result['ledger_gaps'])
 def test_no_content_or_reference_edits(self):
  # Legacy lesson sources and the Kata-Kata chapter files are unchanged. Step 4
  # changed exactly one legacy line (3B, ledger L-1006) and refreshed the ledger.
  files=['curriculum/malay-course.txt','curriculum/foundation.txt','curriculum/advanced.txt','curriculum/guided.txt','conversations.py','curriculum.py']
  files += [str(p.relative_to(ROOT)) for p in (ROOT/'curriculum/reference/katakata').glob('*.json')]
  for f in files:
   original=subprocess.check_output(['git','show','c067e225eabe51e3bfc7020bd2800f9bdaf5a5b4:'+f],cwd=ROOT)
   self.assertEqual(original,(ROOT/f).read_bytes(),f)
  original=subprocess.check_output(['git','show','c067e225eabe51e3bfc7020bd2800f9bdaf5a5b4:curriculum/foundation-guided.txt'],cwd=ROOT,text=True).splitlines()
  changed=[(a,b) for a,b in zip(original,(ROOT/'curriculum/foundation-guided.txt').read_text().splitlines()) if a!=b]
  self.assertEqual(changed,[('Pukul lapan. Nak datang lagi?|Ya, saya nak beli untuk kawan.','Pukul lapan. Nak beli lagi?|Ya, saya nak beli untuk kawan.')])
 def test_unplaced_phrase_does_not_hide_placed_words(self):
  # 'encik pula' is an unplaced Hanashishou row; Encik and pula are chapter 1 words.
  r=self.checker.inspect([self.seg('Khabar baik. Encik pula?',1)]);self.assertFalse(r['violations']);self.assertFalse(r['ledger_gaps'])
 def test_mentions_skip_ledger_but_not_malaysian_form(self):
  s=self.seg('makan',2,kind='mention');self.assertFalse(self.checker.inspect([s])['violations'])
  s=self.seg('nomor',2,kind='mention');self.assertTrue(self.checker.inspect([s])['violations'])
 def test_reauthored_units_block_gaps(self):
  with patch('language_checks.collect_segments',return_value=[self.seg('lucu',1,unit='ms-c01')]):
   with self.assertRaisesRegex(ValueError,'not in the ledger'):
    run_checks([],{'components':[],'test_items':[]})
if __name__=='__main__':unittest.main()
