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
        # Step 4 retires the legacy unit 1 and 2A packs and rewrites one 3B line; steps 5a, 5b, 5c, 5d and 5e retire chapter 3, 4, 5, 6 and 7 packs
        # (ledger L-1006 action). Every other legacy page is unchanged.
        old=bank(subprocess.check_output(['git','show','b42e307f6f1594f7e15e68536ee2bb60bc7b1a4b:dist/bank.js'],cwd=ROOT,text=True))
        retired={'Greetings · Learner pack','Greetings · Teaching plan','Introductions · Learner pack','Introductions · Teaching plan',
                 'Counting and quantities · Learner pack','Counting and quantities · Teaching plan',
                 'Ringgit and sen · Learner pack','Ringgit and sen · Teaching plan',
                 'Order and floors · Learner pack','Order and floors · Teaching plan',
                 'Beli buah di pasar','Beli buah di pasar · Learner pack','Beli buah di pasar · Teaching plan','Jumlah buah','Pesanan buah',
                 # Step 5b retires the legacy chapter 4 packs superseded by units 4A and 4B.
                 'Clock time · Learner pack','Clock time · Teaching plan','Dates and days · Learner pack','Dates and days · Teaching plan',
                 'Frequency and routines · Learner pack','Frequency and routines · Teaching plan',
                 # Step 5c retires the legacy chapter 5 packs superseded by unit 5.
                 'Taste and colour · Learner pack','Taste and colour · Teaching plan',
                 'Size and shape · Learner pack','Size and shape · Teaching plan',
                 # Step 5d retires the legacy chapter 6 pack superseded by unit 6.
                 'Comparisons and superlatives · Learner pack','Comparisons and superlatives · Teaching plan',
                 # Step 5e retires the legacy chapter 7 packs superseded by unit 7 (and the grammar pack "Di, ke and dari", whose
                 # words kampus and tren are not in the ledger and whose content unit 7 patterns 1 and 2 replace).
                 'Asking where · Learner pack','Asking where · Teaching plan',
                 'Directions and orientation · Learner pack','Directions and orientation · Teaching plan','Di, ke and dari',
                 # Stage 2 chapter 12 fixes (Sam, 13 Nov 2026) retire the old chapter 12 placeholder, replaced by units 12A and 12B.
                 'Ambil bungkusan di lobi','Ambil bungkusan di lobi · Learner pack','Ambil bungkusan di lobi · Teaching plan','Dah atau belum','Mesej untuk pengawal','A clear pickup message'}
        expected=[l for l in old if l['title'] not in retired]
        # Stage 2 build step 1 (13 Nov 2026): placing «perlu» (Ch13), «jadi» (Ch14), «ni» and «macam tu» (Ch17) in the ledger
        # made them forward references in the legacy chapter 12 pack, so exactly these lines were rewritten (plan section 2,
        # "Existing parcel pack"; the full re-authoring is build step 4).
        edited={'Yang kecil ni untuk unit B-21.':'Yang kecil ini untuk unit B-21.','Oh, jadi kotak saya belum ada?':'Oh, kotak saya belum ada?',
                'Betul, itu nama saya. Perlu tunjuk apa?':'Betul, itu nama saya. Encik mahu tengok apa?',
                'Ya. Di mana saya perlu tulis nama?':'Ya. Di mana saya tulis nama?','Nama dia Mei. Apa dia perlu tunjuk?':'Nama dia Mei. Dia bawa apa?',
                'Kalau macam tu, saya ambil esok. Perlu tulis nama sekarang?':'Baik, saya ambil esok. Saya tulis nama sekarang?',
                'Tak perlu. Semak nama bila ambil nanti.':'Tak. Semak nama bila ambil nanti.'}
        def edit(line):
            for a,b in edited.items():
                if line.endswith(a): return line[:-len(a)]+b
            return line
        for l in expected:
            if l['title']=='Ambil bungkusan di lobi':
                for page in l['pages']: page['lines']=[edit(x) for x in page['lines']]
        legacy=[l for l in self.lessons if not l.get('suite')]
        strip=lambda ls:[{k:v for k,v in l.items()} | {'pages':[{k:v for k,v in p.items() if k!='index'} for p in l['pages']]} for l in ls]
        self.assertEqual(strip(expected),strip(legacy))
    def test_pinned_sources(self):
        # The Kata-Kata chapter files c01 to c18 are the ones at Kata-Kata commit 7fbe173 (end of Kata-Kata step 3d,
        # Stage 2 build step 4 refresh); c01 to c09 are unchanged since 34710c6 (end of the 12 Nov 2026 clean-up).
        # Pinned in docs/step4-sources.json. docs/restructure-sources.json keeps the older Stage 1 baseline (0f78179)
        # as a record only.
        sources=json.loads((ROOT/'docs/step4-sources.json').read_text())
        self.assertEqual(sources['kata_kata_commit'],'7fbe173')
        files=sorted((ROOT/'curriculum/reference/katakata').glob('c*.json'))
        self.assertEqual([p.name for p in files],['c%02d.json'%i for i in range(1,19)])
        for p in files:
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),sources['kata_kata_chapter_sha256']['content/ms/kelas/'+p.name],p.name)
        # The ledger copies are Kata-Kata content/ledger/malay-ledger.csv at 7fbe173 (the snapshot byte for byte, CRLF; the reference copy with LF).
        ledger=ROOT/'curriculum/reference/katakata/malay-ledger.csv'
        self.assertEqual(hashlib.sha256(ledger.read_bytes()).hexdigest(),json.loads((ROOT/'docs/step4-sources.json').read_text())['ledger']['sha256'])
        import csv, io
        self.assertEqual(list(csv.reader(io.StringIO(ledger.read_text()))),list(csv.reader(io.StringIO((ROOT/'docs/handoff/ledger-snapshot.csv').read_text()))))
    def test_structure(self):
        # Stage 1: 9 chapters, 13 units; Stage 2 build step 4 adds chapter 10 (units 10A and 10B) chapter 11 (units 11A and 11B) and chapter 12 (units 12A and 12B) and chapter 13 (unit 13) and chapter 14 (unit 14) and chapter 15 (unit 15) and chapter 16 (unit 16).
        d=self.data;self.assertEqual(len(d['chapters']),16)
        self.assertEqual(sum(len(c['units']) for c in d['chapters']),23)
        self.assertEqual(sum(len(c['block_plan']) for c in d['chapters']),115)
        self.assertEqual(len(d['component_slots']),253)
        self.assertEqual([c['level'] for c in d['chapters']],['A1']*9+['A2']*7)
        self.assertEqual([c['stage_id'] for c in d['chapters']],['ms-stage1']*9+['ms-stage2']*7)
        self.assertEqual(len({c['id'] for c in d['components']}),len(d['components']))
        for c in d['chapters']:
            for b in c['block_plan']:self.assertEqual(sum(a['minutes'] for a in b['activities']),45)
        fields={'language','level','chapter_id','unit_id','component_type','sub_type','skills','genre','grammar_points','time_minutes','prerequisites','course_path','external_textbook_links','review_status'}
        for c in d['components']:
            self.assertTrue(fields<=c.keys());self.assertTrue(set(c['word_ids'])<=d['word_registry'].keys())
            if c['language']=='Japanese':self.assertIsNone(c['chapter_id'])
            source=next(l for l in self.lessons if l['title']==c['source_title'])
            for index in c['page_indices']:self.assertTrue(3<=index<len(source['pages'])-source.get('key_pages',1))
        # Step 4: every test item is tagged and passes the contract.
        self.assertTrue(d['test_items'])
        for item in d['test_items']:validate_test_item(item,d)
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
        self.assertEqual(set(roots),{'beri','mesej','memang','mesti','beritahu','mengapa'})
if __name__=='__main__': unittest.main()
