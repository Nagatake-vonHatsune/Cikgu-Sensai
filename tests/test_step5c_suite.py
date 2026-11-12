"""Step 5c chapter 5: charter section 6 and 14 minimums for unit 5, its writing block and the fast pack.

Checks the authored source and the built page bank: the ledger partition (core, Dunia
recognition by scene, revision), the component minimums, the cumulative question words
with «bagaimana» and «kenapa», real item-by-item answer keys, word tags on every test
item, the chapter 5 register rules (spoken forms labelled; no comparatives; nothing
religious; no medicines or doses) and retirement of the legacy chapter 5 packs.
"""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c05
from catalogue import make_catalogue

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
SCENES = {'Masak nasi goreng': 15, 'Di klinik': 12, 'Gambar bayi': 12, 'Lepak di kedai mamak': 11}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch5_core_ids(rows):
    """Ledger rows placed in chapter 5 as taught words (a 'Ch5' part, even after a Dunia part)."""
    out = set()
    for lid, r in rows.items():
        if r['Review status'] == 'Retired':
            continue
        parts = [p.strip() for p in r['Kata-Kata place'].split(';')]
        if any(re.fullmatch(r'Ch ?5( \(pending\))?', p) for p in parts):
            out.add(lid)
    return out


class Chapter5Minimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.cfg = ms_c05.CFG
        cls.u = 'ms-c05'

    def comp(self, typ, sub=None, unit=None):
        found = [l for l in self.by_unit[unit or self.u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)]
        self.assertTrue(found, f'missing {typ}/{sub}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def test_ledger_partition(self):
        rows = self.ledger.rows
        core_all = ch5_core_ids(rows)
        # 58 entries are placed in chapter 5 and nowhere earlier; «seronok» (L-0455) and «tawar» (L-0520) are
        # also placed in chapter 5 but were only Dunia recognition words in 4A and 3B, so they are taught here.
        self.assertEqual(len(core_all), 60)
        self.assertEqual(len([l for l in core_all if re.match(r'(Ch ?5|Dunia)', rows[l]['Kata-Kata place'])
                              and rows[l]['Kata-Kata place'].startswith('Ch')]), 58)
        self.assertEqual({'L-0455', 'L-0520'}, {l for l in core_all if rows[l]['Kata-Kata place'].startswith('Dunia')})
        rec_all = {lid for lid, r in rows.items() if r['Kata-Kata place'].startswith('Dunia')
                   and 'primes Ch5' in r['Kata-Kata place']} - core_all
        self.assertEqual(len(rec_all), 50)
        core = self.cfg['core']
        rec = [lid for _, ids in self.cfg['recognition'] for lid in ids]
        self.assertEqual(len(core), len(set(core)))
        self.assertEqual(set(core), core_all)
        self.assertEqual(len(rec), len(set(rec)))
        self.assertEqual(set(rec), rec_all)
        # Recognition by scene, with the counts Sam gave.
        self.assertEqual({s: len(ids) for s, ids in self.cfg['recognition']}, SCENES)
        for scene, ids in self.cfg['recognition']:
            for lid in ids:
                self.assertIn(f'Dunia · {scene} (primes Ch5)', rows[lid]['Kata-Kata place'])
        # Core words come in six themed groups and nothing is lost between groups.
        groups = dict(self.cfg['core_groups'])
        self.assertEqual(list(groups), ['Tastes', 'Colours', 'Size and shape', 'Feelings and states',
                                        'Hot, cold, food and drink', 'Question and linking words'])
        self.assertEqual([lid for ids in groups.values() for lid in ids], core)
        # Revision: taught in chapters 1 to 4, never counted as new core or recognition.
        rev = {lid for _, ids in self.cfg['revision'] for lid in ids}
        self.assertFalse(rev & set(core))
        self.assertFalse(rev & set(rec))
        for lid in rev:
            self.assertTrue(any(r['ID'] == lid and r['_chapter'] is not None and r['_chapter'] <= 4
                                for rs in self.ledger.checker.entries.values() for r in rs), lid)
        # «sedikit» (chapter 2) and «kosong» (chapter 3) are revision, not new.
        self.assertIn('L-0216', rev)
        self.assertIn('L-0099', rev)
        self.assertFalse({'L-0216', 'L-0099'} & set(core))

    def test_components_and_vocabulary(self):
        required = {'Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                    'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan'}
        self.assertTrue(required <= {l['suite']['component_type'] for l in self.by_unit[self.u]})
        v = self.comp('Vocabulary')
        txt = ' '.join(self.lines(v))
        for label in ('Core words', 'Dunia · To recognise', 'Revision · 復習'):
            self.assertIn(label, txt)
        cfg = self.cfg
        ids = cfg['core'] + [i for _, x in cfg['recognition'] for i in x] + [i for _, x in cfg['revision'] for i in x]
        for lid in ids:
            self.assertIn('[' + lid + ']', txt, lid)
        entries = [x for x in self.lines(v) if re.search(r'\[L-\d{4}\]$', x)]
        examples = [x for x in self.lines(v) if x.strip().startswith('e.g.')]
        self.assertEqual(len(entries), len(examples))
        self.assertEqual(len(entries), len(ids))
        for scene in SCENES:
            self.assertIn(f'"{scene}"', txt)
        for l in self.by_unit[self.u]:
            self.assertIn('Japanese awaiting native review', l['header'])
            self.assertTrue(l['suite']['grammar_points'], l['title'])

    def test_patterns(self):
        l = self.comp('Pattern and grammar')
        self.assertTrue(3 <= len(l['sections']) <= 5)
        for title, lines, _ in l['sections']:
            self.assertTrue(any(x.startswith('Pattern box:') for x in lines), title)
            self.assertTrue(4 <= sum(bool(re.match(r'\d+\. A:', x)) for x in lines) <= 6, title)
            for label in ('Explanation:', '説明：', 'Japanese helps or misleads:', '日本語との比較：'):
                self.assertTrue(any(x.startswith(label) for x in lines), (title, label))
        ids = [t.split(' · ')[1] for t, _, _ in l['sections']]
        self.assertEqual(ids, ['ms-c05-f01', 'ms-c05-f02', 'ms-c05-f03', 'ms-c05-f04', 'ms-c05-f05'])
        body = ' '.join(self.lines(l))
        for w in ('«yang»', '«atau»', '«tetapi»', '«bagaimana»', '«macam mana»', '«kenapa»', '«sebab»', '«mahu»'):
            self.assertIn(w, body, w)

    def test_drills_keys_and_question_words(self):
        total = 0
        for sub in ('repeat', 'substitute', 'transform', 'question and answer', 'question-word choice'):
            l = self.comp('Drill', sub)
            n = sum(bool(NUMBERED.match(x)) for x in self.lines(l))
            self.assertGreaterEqual(n, 6, sub)
            total += n
            if sub != 'repeat':
                key = ' '.join(l['key'])
                for i in range(1, n + 1):
                    self.assertRegex(key, rf'(^|\s){i} «', (sub, i))
        self.assertGreaterEqual(total, 30)
        self.assertGreaterEqual(sum(x.startswith('Dialogue ') for x in self.lines(self.comp('Drill', 'free'))), 3)
        full = ' '.join(self.lines(self.comp('Drill', 'question-word set')))
        for w in ('«apa»', '«siapa»', '«di mana»', '«Siapakah»', '«Apakah»', '«di manakah»', '«Adakah»',
                  '«Bolehkah»', '«berapa»', '«bila»', '«pukul berapa»', '«hari apa»',
                  '«bagaimana»', '«macam mana»', '«kenapa»', '«sebab»'):
            self.assertIn(w, full, w)
        key = ' '.join(self.comp('Drill', 'question-word set')['key'])
        self.assertIn('«Bagaimana', key)
        self.assertIn('«Kenapa', key)
        self.assertIn('«Sebab', key)
        # The question-word choice drill uses the new words alongside earlier ones.
        choice = ' '.join(self.comp('Drill', 'question-word choice')['key'])
        for w in ('«Bagaimana»', '«Kenapa»', '«Berapa»', '«Bila»', '«Siapa»', '«Di mana»', '«Apa»'):
            self.assertIn(w, choice, w)

    def test_markers_return(self):
        """Charter section 14: the tense and aspect markers come back in every later chapter."""
        l = self.comp('Drill', 'markers')
        txt = ' '.join(self.lines(l))
        for m in ('«belum»', '«sudah»', '«masih»', '«akan»'):
            self.assertIn(m, txt, m)
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(l)), 6)
        self.assertIn('8 «', ' '.join(l['key']))

    def test_conversation_listening_reading_task_culture(self):
        cfg = self.cfg
        d = self.comp('Model conversation')
        self.assertTrue(10 <= len(self.lines(d, 'Model ·')) <= 16)
        self.assertTrue(any('____' in x for x in self.lines(d, 'Gapped')))
        self.assertEqual(len(self.lines(d, 'Changed facts')), len(cfg['variant']))
        self.assertTrue(120 <= malay_words([f'«{s}»' for _, s in cfg['listening']]) <= 250)
        lis = self.comp('Listening')
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(lis, 'While')), 6)
        self.assertEqual(len(cfg['listen_questions']), len(cfg['listen_answers']))
        self.assertTrue(self.lines(lis, 'Before') and self.lines(lis, 'After'))
        rw = self.comp('Reading and writing')
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(rw, 'Questions')), 5)
        self.assertEqual(len(cfg['read_questions']), len(cfg['read_answers']))
        self.assertTrue(any(x.startswith('Model writing') for x in rw['key']))
        task = self.comp('Task')
        for part in ('Role card A', 'Role card B', 'Change of plan', 'Success criteria'):
            self.assertIn(part, ' '.join(n for n, _, _ in task['sections']))
        words = english_words(self.lines(self.comp('Culture note'), 'English'))
        self.assertTrue(150 <= words <= 300, words)
        self.assertEqual(len(cfg['culture']), len(cfg['culture_ja']))
        self.assertFalse(any(re.search(r'[A-Za-z]{4,}', re.sub(
            r'«[^»]*»|‹[^›]*›|ms-c\d\d-\d+|UTC|Kata-Kata|Jalur Gemilang|Jalur|Gemilang', '', x)) for x in cfg['culture_ja']))

    def test_japanese_has_no_leftover_english(self):
        """Japanese cells are full translations: Latin letters appear only inside marked Malay, ids or product names."""
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Dunia|Jalur Gemilang|Sedia Kelas|Tanya Cikgu|Susun Ayat|UTC|RM'
                           r'|Masak nasi goreng|Di klinik|Gambar bayi|Lepak di kedai mamak')
        cfg = self.cfg
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja'], cfg['extra']['explain'][0]]
        cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
        for part in (cfg['role_a'], cfg['role_b'], cfg['change'], cfg['markers']['bridge'], cfg['extra']['task']):
            cells.append(part[-1].split(' / ')[-1] if part is cfg['markers']['bridge'] else part[-1])
        for l in self.by_unit[self.u]:
            for _, items, _ in l['sections']:
                cells += [x for x in items if x.startswith(('説明：', '日本語との比較：'))]
        for ja in cells:
            self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
            self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_tests_and_plans(self):
        l = self.comp('Test')
        tests = l['suite']['tests']
        scored = [t for t in tests if t['sub_type'] != 'speaking']
        self.assertTrue(15 <= len(scored) <= 20)
        self.assertEqual(sum(t['sub_type'] == 'speaking' for t in tests), 1)
        self.assertTrue({'listening', 'reading', 'words', 'grammar'} <= {t['sub_type'] for t in tests})
        # Every item is tagged with grammar points and ledger word ids.
        self.assertTrue(all(t['grammar_points'] and t['word_ids'] for t in tests))
        # Word items test new core words only.
        core_cards = {self.ledger.word_id(self.ledger.row(lid)) for lid in self.cfg['core']}
        for t in tests:
            if t['sub_type'] == 'words':
                self.assertTrue(set(t['word_ids']) <= core_cards, t['id'])
        plan = self.comp('Teaching plan')
        names = ' '.join(n for n, _, _ in plan['sections'])
        self.assertTrue(all('Block ' + b in names for b in 'ABCDE'))
        body = ' '.join(self.lines(plan))
        self.assertIn('Sedia Kelas c05', body)
        self.assertIn('0–5', body)
        self.assertTrue(any(l['suite']['id'] == 'ms-c05-writing-block' for l in self.by_unit[self.u]))
        wb = self.comp('Reading and writing', 'composition')
        self.assertEqual(wb['suite']['block'], 'Skills')
        self.assertEqual(wb['suite']['time_minutes'], 45)

    def test_chapter5_malay_rules(self):
        label = re.compile(r'spoken|speech|話し言葉|口語', re.I)
        spoken_words = {'nak', 'tapi', 'sikit', 'dah', 'tak', 'oren', 'macam', 'tengah'}
        everything = [l for l in self.by_unit[self.u] + self.by_unit.get('ms-c05-fast', [])]
        for l in everything:
            lines = [x for _, items, _ in l['sections'] for x in items] + l['key']
            for line in lines:
                # Comparatives and superlatives wait for chapter 6; «kurang manis» is the only «kurang».
                for span in re.findall(r'«([^»]*)»', line):
                    words = re.findall(r'[a-z]+', span.lower())
                    self.assertNotIn('lebih', words, line)
                    self.assertNotIn('paling', words, line)
                    self.assertNotIn('daripada', words, line)
                    for i, w in enumerate(words):
                        if w == 'kurang':
                            self.assertEqual(words[i:i + 2], ['kurang', 'manis'], line)
                    # Spoken forms sit on a line that labels them spoken.
                    for i, w in enumerate(words):
                        if w in spoken_words and not (w == 'tengah' and words[i + 1:i + 2] == ['hari']) \
                                and not (w == 'macam' and words[i + 1:i + 2] == ['mana'] and False):
                            self.assertRegex(line, label, (l['title'], line))
                # No religious expressions and no medicine instructions.
                self.assertNotRegex(line.lower(), r'assalam|waalaikum|insya|alhamdulillah|bismillah|halal|haram|doa\b|puasa')
                self.assertNotRegex(line.lower(), r'\b\d+\s*(mg|ml|tablet|pil)\b')

    def test_legacy_retirement_and_catalogue(self):
        built = {x['title'] for x in bank()}
        for name in ('Taste and colour', 'Size and shape'):
            self.assertFalse(any(t == name or t.startswith(name + ' ·') for t in built), name)
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch5 = next(c for c in chapters if c['title'].startswith('Chapter 5'))
        self.assertEqual([u['label'] for u in ch5['units']], ['5'])
        self.assertEqual(ch5['status'], 'Step 5c chapter 5 suite · draft for pilot')
        catalogue = make_catalogue(bank(), chapters)
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('check_unit') == self.u]
        self.assertTrue(mine)
        self.assertTrue(all(c['chapter_id'] == 'ms-c05' and c['review_status'] == 'draft' for c in mine))
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage1-writing-5')
        self.assertEqual(block['component_ids'], ['ms-c05-writing-block'])
        self.assertEqual(block['status'], 'pilot draft')
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertFalse([k for k, e in exceptions.items() if e['unit'] == self.u])
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        self.assertIn(self.u, reauthored)


if __name__ == '__main__':
    unittest.main()
