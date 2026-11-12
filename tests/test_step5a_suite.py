"""Step 5a chapter 3: reproducible charter section 6 and 14 minimums.

The tests check the authored source, generated PDF-bank pages, vocabulary split,
ledger coverage, cumulative question words and retirement of legacy packs.
"""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c03a, ms_c03b, ms_c03c
from catalogue import make_catalogue

ROOT=Path(__file__).resolve().parents[1]
NEW=['ms-c03a','ms-c03b','ms-c03c']
NUMBERED=re.compile(r'^(?:☐ )?\d+\. ')


def bank():
    raw=(ROOT/'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


class Chapter3Minimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger=Ledger()
        cls.lessons,cls.units=build_suite(cls.ledger)
        cls.by_unit={}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'],[]).append(lesson)
        cls.cfg=[ms_c03a.CFG,ms_c03b.CFG,ms_c03c.CFG]

    def comp(self,unit,typ,sub=None):
        found=[l for l in self.by_unit[unit]
               if l['suite']['component_type']==typ
               and (sub is None or l['suite']['sub_type']==sub)]
        self.assertTrue(found,f'{unit} missing {typ}/{sub}')
        return found[0]

    def lines(self,l,part=None):
        return [line for name,items,kind in l['sections']
                if part is None or part in name for line in items]

    def test_exact_ledger_partition(self):
        core=[lid for c in self.cfg for lid in c['core']]
        rec=[lid for c in self.cfg for lid in c['recognition']]
        self.assertEqual([len(c['core']) for c in self.cfg],[25,24,24])
        self.assertEqual([len(c['recognition']) for c in self.cfg],[5,11,8])
        self.assertEqual(len(core),73)
        self.assertEqual(len(rec),24)
        self.assertEqual(len(set(core)),73)
        self.assertEqual(len(set(rec)),24)
        self.assertFalse(set(core)&set(rec))
        rows=self.ledger.rows
        expected_core={lid for lid,r in rows.items()
                       if re.search(r'\bCh3\b|\bCh 3\b',r['Kata-Kata place'])
                       and 'Dunia' not in r['Kata-Kata place']}
        expected_rec={lid for lid,r in rows.items()
                      if r['Kata-Kata place'].startswith('Dunia')
                      and 'primes Ch3' in r['Kata-Kata place']}
        self.assertEqual(set(core),expected_core)
        self.assertEqual(set(rec),expected_rec)
        for c in self.cfg:
            self.assertFalse(set(c['core'])&set(c['revision']))
            self.assertFalse(set(c['recognition'])&set(c['revision']))

    def test_components_vocabulary_and_independent_headers(self):
        required={'Opener','Vocabulary','Pattern and grammar','Drill',
                  'Model conversation','Listening','Reading and writing',
                  'Task','Culture note','Test','Teaching plan'}
        for cfg in self.cfg:
            u='ms-c03'+cfg['label'][-1].lower()
            self.assertTrue(required <= {l['suite']['component_type'] for l in self.by_unit[u]})
            v=self.comp(u,'Vocabulary')
            txt=' '.join(self.lines(v))
            for label in ('Core words','To recognise','Revision · 復習'):
                self.assertIn(label,txt,u)
            for lid in cfg['core']+cfg['recognition']+cfg['revision']:
                self.assertIn('['+lid+']',txt,(u,lid))
            ent=[line for line in self.lines(v) if re.search(r'\[L-\d{4}\]$',line)]
            example=[line for line in self.lines(v) if line.strip().startswith('e.g.')]
            self.assertEqual(len(ent),len(example))
            self.assertTrue(all(' — ' in x and ' · ' in x for x in ent))
            for l in self.by_unit[u]:
                self.assertIn('Japanese awaiting native review',l['header'])
                self.assertTrue(l['suite']['grammar_points'],l['title'])

    def test_patterns_question_answers(self):
        for u in NEW:
            l=self.comp(u,'Pattern and grammar')
            self.assertTrue(3<=len(l['sections'])<=5)
            for title,lines,_ in l['sections']:
                self.assertTrue(any(x.startswith('Pattern box:') for x in lines),title)
                self.assertTrue(4<=sum(bool(re.match(r'\d+\. A:',x)) for x in lines)<=6,title)
                for label in ('Explanation:','説明：','Japanese helps or misleads:','日本語との比較：'):
                    self.assertTrue(any(x.startswith(label) for x in lines),(u,title,label))

    def test_drill_ladder_and_cumulative_questions(self):
        for u in NEW:
            total=0
            for sub in ('repeat','substitute','transform','question and answer','question-word choice'):
                l=self.comp(u,'Drill',sub)
                n=sum(bool(NUMBERED.match(x)) for x in self.lines(l))
                self.assertGreaterEqual(n,6,(u,sub,n))
                total+=n
            self.assertGreaterEqual(total,30,u)
            l=self.comp(u,'Drill','free')
            self.assertGreaterEqual(sum(x.startswith('Dialogue ') for x in self.lines(l)),3)
            full=' '.join(self.lines(self.comp(u,'Drill','question-word set')))
            for w in ('«apa»','«siapa»','«di mana»','«Siapakah»',
                      '«Apakah»','«di manakah»','«Adakah»','«Bolehkah»','«berapa»'):
                self.assertIn(w,full,(u,w))

    def test_model_listening_reading_and_culture(self):
        for u in NEW:
            d=self.comp(u,'Model conversation')
            self.assertEqual(len(d['sections']),3)
            turns=self.lines(d,'Model ·')
            self.assertTrue(10<=len(turns)<=16,(u,len(turns)))
            self.assertTrue(any('___' in x for x in self.lines(d,'Gapped')))
            self.assertTrue(self.lines(d,'Changed facts'))
            listening=self.comp(u,'Listening')
            script=[x for x in listening['key'] if ':' in x and
                    not x.startswith(('Teacher','Answers','Table'))]
            words=malay_words(script)
            self.assertTrue(120<=words<=250,(u,words))
            self.assertGreaterEqual(sum(bool(NUMBERED.match(x))
                   for x in self.lines(listening,'While')),6)
            self.assertTrue(self.lines(listening,'Before'))
            self.assertTrue(self.lines(listening,'After'))
            rw=self.comp(u,'Reading and writing')
            self.assertGreaterEqual(sum(bool(NUMBERED.match(x))
                    for x in self.lines(rw,'Questions')),5)
            self.assertTrue(self.lines(rw,'Write'))
            self.assertTrue(any('Model writing' in x for x in rw['key']))
            task=self.comp(u,'Task')
            for part in ('Role card A','Role card B','Change of plan','Success criteria'):
                self.assertIn(part,' '.join(n for n,_,_ in task['sections']))
            culture_words=english_words(self.lines(self.comp(u,'Culture note'),'English'))
            self.assertTrue(150<=culture_words<=300,(u,culture_words))

    def test_tests_plans_and_extra_blocks(self):
        for cfg in self.cfg:
            u='ms-c03'+cfg['label'][-1].lower()
            l=self.comp(u,'Test')
            tests=l['suite']['tests']
            scored=[t for t in tests if t['sub_type']!='speaking']
            self.assertTrue(15<=len(scored)<=20,(u,len(scored)))
            self.assertEqual(sum(t['sub_type']=='speaking' for t in tests),1)
            self.assertTrue({'listening','reading','words','grammar'} <=
                            {t['sub_type'] for t in tests})
            self.assertTrue(all(t['grammar_points'] or t['word_ids'] for t in tests))
            plan=self.comp(u,'Teaching plan')
            names=' '.join(name for name,_,_ in plan['sections'])
            self.assertTrue(all('Block '+b in names for b in 'ABCDE'))
            self.assertIn('Kata-Kata',' '.join(self.lines(plan)))
            self.assertIn('0–5',' '.join(self.lines(plan)))
        self.assertTrue(any(l['suite']['id']=='ms-c03a-review-block' for l in self.by_unit['ms-c03a']))
        self.assertTrue(any(l['suite']['id']=='ms-c03c-writing-block' for l in self.by_unit['ms-c03c']))

    def test_fast_and_legacy_retirement(self):
        l=self.by_unit['ms-c03-fast'][0]
        self.assertEqual(l['suite']['course_path'],'fast')
        core=[x for x in self.lines(l,'Core words') if re.search(r'\[L-\d{4}\]$',x)]
        self.assertTrue(15<=len(core)<=20)
        labels=' '.join(n for n,_,_ in l['sections'])
        for part in ('Can-do','Core words','Key patterns','Model conversation',
                     'Task','Self-check','Self-study'):
            self.assertIn(part,labels)
        for line in self.lines(l,'Key patterns'):
            if re.match(r'^\d · ',line):
                self.assertEqual(line.split('e.g.')[1].count(' / '),1)
        built={x['title']:x for x in bank()}
        page=built[l['title']]
        count=len(page['pages'])-3-page.get('key_pages',1)
        self.assertTrue(2<=count<=4,(l['title'],count))
        excluded=['Counting and quantities','Ringgit and sen','Order and floors',
                  'Beli buah di pasar']
        self.assertTrue(all(not any(x['title'].startswith(z+' ·') or x['title']==z
                     for z in excluded) for x in built.values()))
        lessons=bank()
        chapters=json.loads((ROOT/'dist/chapters.js').read_text()[len('const chapters='):-1])
        catalogue=make_catalogue(lessons,chapters)
        ch3=next(c for c in chapters if c['title'].startswith('Chapter 3'))
        self.assertEqual([u['label'] for u in ch3['units']],['3A','3B','3C'])
        self.assertIn(l['title'],ch3['fast_items'])
        self.assertTrue(all(c['chapter_id']=='ms-c03' and c['review_status']=='draft'
                       for c in catalogue['components'] if c.get('authored') and
                       c.get('check_unit') in NEW+['ms-c03-fast']))


if __name__=='__main__':
    unittest.main()
