"""Step 5b chapter 4: charter section 6 and 14 minimums for units 4A, 4B and the fast pack.

Checks the authored source and the built page bank: the ledger partition (core,
Dunia recognition by scene, revision), the component minimums, the cumulative
question words with «bila», the tense timeline drill, answer keys, the register
rules for chapter 4 (no «kurang suku»; spoken forms marked) and retirement of the
legacy chapter 4 packs.
"""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c04a
from catalogue import make_catalogue

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')


def unit_modules():
    mods = [ms_c04a]
    try:
        from suite import ms_c04b
        if 'ms-c04b' in json.loads((ROOT / 'curriculum/reauthored-units.json').read_text()):
            mods.append(ms_c04b)
    except ImportError:
        pass
    return mods


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch4_core_ids(rows):
    """Ledger rows placed in chapter 4 as taught words (not 'reused in Ch4', not Dunia-only)."""
    out = set()
    for lid, r in rows.items():
        parts = [p.strip() for p in r['Kata-Kata place'].split(';')]
        if any(re.fullmatch(r'Ch ?4( \(pending\))?', p) for p in parts):
            out.add(lid)
    return out


class Chapter4Minimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.mods = unit_modules()
        cls.cfg = [m.CFG for m in cls.mods]
        cls.new = ['ms-c04' + c['label'][-1].lower() for c in cls.cfg]

    def comp(self, unit, typ, sub=None):
        found = [l for l in self.by_unit[unit] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)]
        self.assertTrue(found, f'{unit} missing {typ}/{sub}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def test_ledger_partition(self):
        rows = self.ledger.rows
        core_all = ch4_core_ids(rows)
        rec_all = {lid for lid, r in rows.items() if r['Kata-Kata place'].startswith('Dunia')
                   and 'primes Ch4' in r['Kata-Kata place']} - core_all
        self.assertEqual(len(core_all), 54)
        self.assertEqual(len(rec_all), 55)
        reused = {'L-0162', 'L-0163', 'L-0164', 'L-0165', 'L-1001', 'L-1002'}
        self.assertFalse(core_all & reused)
        core = [lid for c in self.cfg for lid in c['core']]
        rec = [lid for c in self.cfg for _, ids in c['recognition'] for lid in ids]
        self.assertEqual(len(core), len(set(core)))
        self.assertEqual(len(rec), len(set(rec)))
        self.assertTrue(set(core) <= core_all)
        self.assertTrue(set(rec) <= rec_all)
        self.assertEqual(len(self.cfg[0]['core']), 27)
        self.assertEqual(sum(len(ids) for _, ids in self.cfg[0]['recognition']), 25)
        if len(self.cfg) == 2:
            self.assertEqual(len(self.cfg[1]['core']), 27)
            self.assertEqual(set(core), core_all)
            self.assertEqual(set(rec), rec_all)
        for c in self.cfg:
            rev = {lid for _, ids in c['revision'] for lid in ids}
            self.assertFalse(rev & set(c['core']))
            self.assertFalse(rev & {lid for _, ids in c['recognition'] for lid in ids})
            for lid in rev:
                placed = self.ledger.checker.entries  # revision words are taught no later than this unit
                self.assertTrue(any(r['ID'] == lid and r['_chapter'] is not None and r['_chapter'] <= 4
                                    for rs in placed.values() for r in rs), lid)
            # Words reused from chapters 1 and 3 are revision, never new core.
            self.assertFalse(set(c['core']) & reused)
            for scene, _ in c['recognition']:
                self.assertIn(scene, ('Hujan petang', 'Cuti ke pantai', 'Satu hari Encik Tanaka', 'Bangun pagi'))

    def test_components_and_vocabulary(self):
        required = {'Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                    'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan'}
        for cfg, u in zip(self.cfg, self.new):
            self.assertTrue(required <= {l['suite']['component_type'] for l in self.by_unit[u]})
            v = self.comp(u, 'Vocabulary')
            txt = ' '.join(self.lines(v))
            for label in ('Core words', 'Dunia · To recognise', 'Revision · 復習'):
                self.assertIn(label, txt, u)
            ids = cfg['core'] + [i for _, x in cfg['recognition'] for i in x] + [i for _, x in cfg['revision'] for i in x]
            for lid in ids:
                self.assertIn('[' + lid + ']', txt, (u, lid))
            entries = [x for x in self.lines(v) if re.search(r'\[L-\d{4}\]$', x)]
            examples = [x for x in self.lines(v) if x.strip().startswith('e.g.')]
            self.assertEqual(len(entries), len(examples))
            self.assertEqual(len(entries), len(ids))
            for l in self.by_unit[u]:
                self.assertIn('Japanese awaiting native review', l['header'])
                self.assertTrue(l['suite']['grammar_points'], l['title'])

    def test_patterns(self):
        for u in self.new:
            l = self.comp(u, 'Pattern and grammar')
            self.assertTrue(3 <= len(l['sections']) <= 5)
            for title, lines, _ in l['sections']:
                self.assertTrue(any(x.startswith('Pattern box:') for x in lines), title)
                self.assertTrue(4 <= sum(bool(re.match(r'\d+\. A:', x)) for x in lines) <= 6, title)
                for label in ('Explanation:', '説明：', 'Japanese helps or misleads:', '日本語との比較：'):
                    self.assertTrue(any(x.startswith(label) for x in lines), (u, title, label))

    def test_drills_keys_and_question_words(self):
        for cfg, u in zip(self.cfg, self.new):
            total = 0
            for sub in ('repeat', 'substitute', 'transform', 'question and answer', 'question-word choice'):
                l = self.comp(u, 'Drill', sub)
                n = sum(bool(NUMBERED.match(x)) for x in self.lines(l))
                self.assertGreaterEqual(n, 6, (u, sub))
                total += n
                # Real answer keys: every numbered item has its own answer in the key.
                if sub not in ('repeat',):
                    key = ' '.join(l['key'])
                    for i in range(1, n + 1):
                        self.assertRegex(key, rf'(^|\s){i} «', (u, sub, i))
            self.assertGreaterEqual(total, 30, u)
            self.assertGreaterEqual(sum(x.startswith('Dialogue ') for x in self.lines(self.comp(u, 'Drill', 'free'))), 3)
            full = ' '.join(self.lines(self.comp(u, 'Drill', 'question-word set')))
            for w in ('«apa»', '«siapa»', '«di mana»', '«Siapakah»', '«Apakah»', '«di manakah»', '«Adakah»',
                      '«Bolehkah»', '«berapa»', '«bila»', '«pukul berapa»', '«hari apa»'):
                self.assertIn(w, full, (u, w))
            key = ' '.join(self.comp(u, 'Drill', 'question-word set')['key'])
            self.assertIn('«Bila', key)

    def test_timeline_drill(self):
        units = [u for u in self.new if u == 'ms-c04b']
        for u in units:
            l = self.comp(u, 'Drill', 'timeline')
            txt = ' '.join(self.lines(l))
            for m in ('«sudah»', '«sedang»', '«tengah»', '«belum»', '«akan»', '«masih»', '«baru»', '«pernah»'):
                self.assertIn(m, txt, m)
            self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(l)), 6)
            self.assertIn('8 «', ' '.join(l['key']))

    def test_conversation_listening_reading_task_culture(self):
        for cfg, u in zip(self.cfg, self.new):
            d = self.comp(u, 'Model conversation')
            self.assertTrue(10 <= len(self.lines(d, 'Model ·')) <= 16)
            self.assertTrue(any('____' in x for x in self.lines(d, 'Gapped')))
            self.assertEqual(len(self.lines(d, 'Changed facts')), len(cfg['variant']))
            self.assertTrue(120 <= malay_words([f'«{s}»' for _, s in cfg['listening']]) <= 250, u)
            lis = self.comp(u, 'Listening')
            self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(lis, 'While')), 6)
            self.assertEqual(len(cfg['listen_questions']), len(cfg['listen_answers']))
            self.assertTrue(self.lines(lis, 'Before') and self.lines(lis, 'After'))
            rw = self.comp(u, 'Reading and writing')
            self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(rw, 'Questions')), 5)
            self.assertEqual(len(cfg['read_questions']), len(cfg['read_answers']))
            self.assertTrue(any(x.startswith('Model writing') for x in rw['key']))
            task = self.comp(u, 'Task')
            for part in ('Role card A', 'Role card B', 'Change of plan', 'Success criteria'):
                self.assertIn(part, ' '.join(n for n, _, _ in task['sections']))
            words = english_words(self.lines(self.comp(u, 'Culture note'), 'English'))
            self.assertTrue(150 <= words <= 300, (u, words))
            self.assertEqual(len(cfg['culture']), len(cfg['culture_ja']))
            self.assertFalse(any(re.search(r'[A-Za-z]{4,}', re.sub(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\d+|UTC|Kata-Kata', '', x))
                                 for x in cfg['culture_ja']), u)

    def test_tests_and_plans(self):
        for cfg, u in zip(self.cfg, self.new):
            tests = self.comp(u, 'Test')['suite']['tests']
            scored = [t for t in tests if t['sub_type'] != 'speaking']
            self.assertTrue(15 <= len(scored) <= 20)
            self.assertEqual(sum(t['sub_type'] == 'speaking' for t in tests), 1)
            self.assertTrue({'listening', 'reading', 'words', 'grammar'} <= {t['sub_type'] for t in tests})
            self.assertTrue(all(t['grammar_points'] and t['word_ids'] for t in tests))
            plan = self.comp(u, 'Teaching plan')
            names = ' '.join(n for n, _, _ in plan['sections'])
            self.assertTrue(all('Block ' + b in names for b in 'ABCDE'))
            body = ' '.join(self.lines(plan))
            self.assertIn('Sedia Kelas c04', body)
            self.assertIn('0–5', body)
        if 'ms-c04b' in self.new:
            self.assertTrue(any(l['suite']['id'] == 'ms-c04b-review-block' for l in self.by_unit['ms-c04b']))

    def test_chapter4_malay_rules(self):
        """No «kurang suku»; every «dah» or «tengah» (not «tengah hari») sits on a line that labels it spoken."""
        label = re.compile(r'spoken|speech|話し言葉|口語', re.I)
        for u in self.new + (['ms-c04-fast'] if 'ms-c04-fast' in self.by_unit else []):
            for l in self.by_unit[u]:
                lines = [x for _, items, _ in l['sections'] for x in items] + l['key']
                for line in lines:
                    self.assertNotIn('«kurang suku', line, l['title'])
                    for span in re.findall(r'«([^»]*)»', line):
                        words = re.findall(r"[a-z]+", span.lower())
                        spoken = 'dah' in words or any(w == 'tengah' and (i + 1 == len(words) or words[i + 1] != 'hari')
                                                       for i, w in enumerate(words))
                        if spoken:
                            self.assertRegex(line, label, (l['title'], line))

    def test_legacy_retirement_and_catalogue(self):
        built = {x['title'] for x in bank()}
        retired = ['Clock time', 'Dates and days'] + (['Frequency and routines'] if 'ms-c04b' in self.new else [])
        for name in retired:
            self.assertFalse(any(t == name or t.startswith(name + ' ·') for t in built), name)
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch4 = next(c for c in chapters if c['title'].startswith('Chapter 4'))
        self.assertEqual([u['label'] for u in ch4['units']], ['4A', '4B'])
        catalogue = make_catalogue(bank(), chapters)
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('check_unit') in self.new]
        self.assertTrue(mine)
        self.assertTrue(all(c['chapter_id'] == 'ms-c04' and c['review_status'] == 'draft' for c in mine))
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertFalse([k for k, e in exceptions.items() if e['unit'] in self.new])


if __name__ == '__main__':
    unittest.main()
