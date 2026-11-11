import copy
import hashlib
import json
import subprocess
import unittest
from pathlib import Path
from zipfile import ZipFile
from catalogue import make_catalogue, prerequisite_items, validate_test_item
ROOT=Path(__file__).resolve().parents[1]
def bank(text): return json.loads(text.split('const lessons=')[1].split(';\nconst bankPDF=')[0])
class CatalogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lessons=bank((ROOT/'dist/bank.js').read_text())
        cls.groups=json.loads((ROOT/'dist/chapters.js').read_text()[len('const chapters='):-1])
        cls.data=make_catalogue(cls.lessons,cls.groups)
    def test_preserved_content(self):
        old=subprocess.check_output(['git','show','b42e307f6f1594f7e15e68536ee2bb60bc7b1a4b:dist/bank.js'],cwd=ROOT,text=True)
        self.assertEqual(bank(old),self.lessons)
    def test_pinned_sources(self):
        manifest=json.loads((ROOT/'docs/restructure-sources.json').read_text())
        for p in (ROOT/'curriculum/reference/katakata').iterdir():
            key='content/ledger/'+p.name if p.suffix=='.csv' else 'content/ms/kelas/'+p.name
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),manifest['files'][key])
    def test_structure(self):
        d=self.data;self.assertEqual(len(d['chapters']),9)
        self.assertEqual(sum(len(c['units']) for c in d['chapters']),13)
        self.assertEqual(sum(len(c['block_plan']) for c in d['chapters']),65)
        self.assertEqual(len(d['component_slots']),143)
        self.assertEqual(len({c['id'] for c in d['components']}),len(d['components']))
        for c in d['chapters']:
            for b in c['block_plan']:self.assertEqual(sum(a['minutes'] for a in b['activities']),45)
        fields={'language','level','chapter_id','unit_id','component_type','sub_type','skills','genre','grammar_points','time_minutes','prerequisites','course_path','external_textbook_links','review_status'}
        for c in d['components']:
            self.assertTrue(fields<=c.keys());self.assertTrue(set(c['word_ids'])<=d['word_registry'].keys())
            if c['language']=='Japanese':self.assertIsNone(c['chapter_id'])
            source=next(l for l in self.lessons if l['title']==c['source_title'])
            for index in c['page_indices']:self.assertTrue(3<=index<len(source['pages'])-1)
        self.assertEqual(d['test_items'],[]) # No tests invented in step 2.
    def test_test_item_contract_and_prerequisite_selection(self):
        d=copy.deepcopy(self.data)
        d['components'].append({'id':'fixture-test','component_type':'Test','chapter_id':'ms-c01'})
        item={'id':'fixture','chapter_id':'ms-c01','component_id':'fixture-test','sub_type':'words','grammar_points':[],
              'word_ids':['ms-c01-001'],'prompt':'fixture only','answer_key':'fixture only','review_status':'draft'}
        validate_test_item(item,d)
        d['test_items']=[item]
        component={'prerequisites':{'chapters':['ms-c01'],'grammar_points':[],'word_ids':['ms-c01-001']}}
        self.assertEqual(prerequisite_items(component,d),[item])
        component['prerequisites']['word_ids']=['ms-c01-002']
        self.assertEqual(prerequisite_items(component,d),[])
        for patch in [{'word_ids':['invented']},{'word_ids':[]},{'grammar_points':['invented']},{'component_id':'absent'}]:
            with self.assertRaises(ValueError):validate_test_item(item|patch,d)
    def test_audits_not_published(self):
        self.assertFalse(list((ROOT/'dist').glob('restructure-issues.*')))
        self.assertNotIn('restructure-issues',(ROOT/'dist/index.html').read_text())
        with ZipFile(ROOT/'dist/Cikgu-Sensai-offline.zip') as z:
            self.assertFalse(any('restructure-issues.' in n for n in z.namelist()))
        roots=json.loads((ROOT/'curriculum/malay-roots.json').read_text())['roots']
        self.assertEqual(set(roots),{'beri','mesej','memang','mesti','beritahu'})
if __name__=='__main__': unittest.main()
