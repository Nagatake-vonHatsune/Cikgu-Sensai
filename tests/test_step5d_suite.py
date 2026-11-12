"""Step 5d chapter 6: charter section 6 and 14 minimums for unit 6 and the chapter 6 fast pack.

Checks the authored source and the built page bank: the ledger partition (core, Dunia
recognition, revision), the component minimums, the cumulative question words with
«yang mana», real item-by-item answer keys, word tags on every test item, the chapter 6
Malay rules (whole ter- and se- words only; spoken forms labelled; nothing religious; no
medicines or doses; nothing placed after chapter 6) and retirement of the legacy chapter 6 pack.
"""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c06, fast
from catalogue import make_catalogue

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
SCENES = {'Main badminton': 14}
WHOLE_WORDS = {'termurah', 'terbesar', 'terbaik', 'tercantik', 'setinggi', 'semahal'}
ADJECTIVES = {'murah', 'besar', 'baik', 'cantik', 'tinggi', 'mahal', 'kecil', 'bersih', 'sunyi', 'ramai', 'selesa',
              'bagus', 'panjang', 'pendek', 'berat', 'ringan', 'cepat', 'lama', 'baru', 'manis', 'pedas', 'panas',
              'sejuk', 'kotor', 'bising', 'susah', 'mudah', 'lambat', 'awal', 'sedap', 'tebal', 'nipis'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch_parts(row):
    """Chapter numbers of the plain 'ChN' parts of a ledger row's placement."""
    return [int(m.group(1)) for p in row['Kata-Kata place'].split(';')
            for m in [re.fullmatch(r'\s*Ch ?(\d)( \(pending\))?\s*', p)] if m]


def ch6_core_ids(rows):
    """Rows placed in chapter 6 and in no earlier chapter (chapters 4 and 6 for «sekali» and «baru" are revision)."""
    out = set()
    for lid, r in rows.items():
        if r['Review status'] == 'Retired':
            continue
        parts = ch_parts(r)
        if 6 in parts and not any(c < 6 for c in parts):
            out.add(lid)
    return out


class Chapter6Minimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.cfg = ms_c06.CFG
        cls.u = 'ms-c06'

    def comp(self, typ, sub=None, unit=None):
        found = [l for l in self.by_unit[unit or self.u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)]
        self.assertTrue(found, f'missing {typ}/{sub}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def test_ledger_partition(self):
        rows = self.ledger.rows
        placed = {lid for lid, r in rows.items() if r['Review status'] != 'Retired' and 6 in ch_parts(r)}
        # 34 rows from the original ledger plus «sewa», «bilik» and «luas» (L-1051 to L-1053, added 12 Nov 2026).
        self.assertEqual(len(placed), 37)
        core_all = ch6_core_ids(rows)
        # «sekali» (L-0188) and «baru» (L-0195) are placed in chapters 4 and 6; chapter 6 adds a second meaning.
        self.assertEqual(placed - core_all, {'L-0188', 'L-0195'})
        self.assertEqual(len(core_all), 35)
        self.assertTrue({'L-1051', 'L-1052', 'L-1053'} <= core_all)
        rec_all = {lid for lid, r in rows.items() if r['Kata-Kata place'].startswith('Dunia')
                   and 'primes Ch6' in r['Kata-Kata place']} - core_all
        self.assertEqual(len(rec_all), 14)
        core = self.cfg['core']
        rec = [lid for _, ids in self.cfg['recognition'] for lid in ids]
        self.assertEqual(len(core), len(set(core)))
        self.assertEqual(set(core), core_all)
        self.assertEqual(len(rec), len(set(rec)))
        self.assertEqual(set(rec), rec_all)
        self.assertEqual({s: len(ids) for s, ids in self.cfg['recognition']}, SCENES)
        for scene, ids in self.cfg['recognition']:
            for lid in ids:
                self.assertIn(f'Dunia · {scene} (primes Ch6)', rows[lid]['Kata-Kata place'])
        groups = dict(self.cfg['core_groups'])
        self.assertEqual(list(groups), ['Comparing and equal', 'The most', 'Very and too', 'Choosing',
                                        'Describing places and things', 'Places'])
        self.assertEqual([lid for ids in groups.values() for lid in ids], core)
        # The six whole words are core ledger entries, taught as whole words.
        for lid in ('L-0269', 'L-0270', 'L-0275', 'L-0276', 'L-0277', 'L-0278'):
            self.assertIn(lid, groups['Comparing and equal'] + groups['The most'])
        # Revision: taught in chapters 1 to 5 (chapter 4 for «sekali» and «baru»), never counted as new core or recognition.
        rev = {lid for _, ids in self.cfg['revision'] for lid in ids}
        self.assertFalse(rev & set(core))
        self.assertFalse(rev & set(rec))
        for lid in rev:
            self.assertTrue(any(r['ID'] == lid and r['_chapter'] is not None and r['_chapter'] <= 5
                                for rs in self.ledger.checker.entries.values() for r in rs), lid)
        self.assertTrue({'L-0188', 'L-0195'} <= rev)

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
        self.assertIn('"Main badminton"', txt)
        # The new meanings of «sekali» and «baru» are said in the vocabulary note.
        sek = next(x for x in entries if '[L-0188]' in x)
        bar = next(x for x in entries if '[L-0195]' in x)
        self.assertIn('very', sek)
        self.assertIn('once', sek)
        self.assertIn('new', bar)
        self.assertIn('just', bar)
        # «mudah» first, «senang» marked spoken.
        self.assertIn('«mudah» / «senang» (spoken)', txt)
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
        self.assertEqual(ids, ['ms-c06-f01, ms-c06-f02', 'ms-c06-f03', 'ms-c06-f04', 'ms-c06-f05', 'ms-c06-f06'])
        # All six Kata-Kata frames are covered.
        self.assertEqual(l['suite']['pattern_ids'], [f'ms-c06-f0{n}' for n in range(1, 7)])
        body = ' '.join(self.lines(l))
        for w in ('«lebih»', '«kurang»', '«daripada»', '«sama»', '«dengan»', '«setinggi»', '«semahal»', '«paling»', '«termurah»',
                  '«terbesar»', '«terbaik»', '«tercantik»', '«yang mana»', '«pilih»', '«sangat»', '«amat»', '«terlalu»', '«sekali»'):
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
                  '«bagaimana»', '«macam mana»', '«kenapa»', '«mengapa»', '«apa sebab»', '«sebab»', '«kerana»',
                  '«yang mana»', '«pilih»'):
            self.assertIn(w, full, w)
        qset = self.comp('Drill', 'question-word set')
        key = ' '.join(qset['key'])
        self.assertIn('«Awak suka kondo yang mana?»', key)
        self.assertRegex(key, r'12 «')
        n_tasks = sum(bool(NUMBERED.match(x)) for x in self.lines(qset))
        self.assertEqual(n_tasks, 12)
        choice = ' '.join(self.comp('Drill', 'question-word choice')['key'])
        for w in ('«Yang mana»', '«Berapa»', '«Di mana»', '«Bila»', '«Bagaimana»', '«Kenapa»', '«Siapa»', '«Apa»'):
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
            r'«[^»]*»|‹[^›]*›|ms-c\d\d-\d+|UTC|Kata-Kata|Kamus Dewan|Strata Management Act|LRT|MRT|KTM|Komuter|Kata|Kuala Lumpur', '', x))
            for x in cfg['culture_ja']))

    def test_japanese_has_no_leftover_english(self):
        """Japanese cells are full translations: Latin letters appear only inside marked Malay, ids or product names."""
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Dunia|Jalur Gemilang|Sedia Kelas|Tanya Cikgu|Susun Ayat|UTC|RM'
                           r'|Kamus Dewan|Strata Management Act|LRT|MRT|KTM Komuter|Main badminton')
        cfg = self.cfg
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
        cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
        for part in (cfg['role_a'], cfg['role_b'], cfg['change'], cfg['markers']['bridge']):
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
        self.assertTrue(all(t['grammar_points'] and t['word_ids'] for t in tests))
        core_cards = {self.ledger.word_id(self.ledger.row(lid)) for lid in self.cfg['core']}
        for t in tests:
            if t['sub_type'] == 'words':
                self.assertTrue(set(t['word_ids']) <= core_cards, t['id'])
        plan = self.comp('Teaching plan')
        names = ' '.join(n for n, _, _ in plan['sections'])
        self.assertTrue(all('Block ' + b in names for b in 'ABCDE'))
        body = ' '.join(self.lines(plan))
        self.assertIn('Sedia Kelas c06', body)
        self.assertIn('0–5', body)
        # The review block after unit 6 (Stage 1 plan) is written in step 5e Part 1: 'ms-c06-review-block'.
        blocks = [l for l in self.by_unit[self.u] if l['suite']['block'] == 'Skills']
        self.assertEqual([l['suite']['id'] for l in blocks], ['ms-c06-review-block'])

    def test_chapter6_malay_rules(self):
        label = re.compile(r'spoken|speech|話し言葉|口語', re.I)
        spoken_words = {'nak', 'tapi', 'sikit', 'dah', 'tak', 'senang', 'tengah'}
        everything = [l for l in self.by_unit[self.u] + self.by_unit.get('ms-c06-fast', [])]
        for l in everything:
            lines = [x for _, items, _ in l['sections'] for x in items] + l['key']
            for line in lines:
                for span in re.findall(r'«([^»]*)»', line):
                    words = re.findall(r'[a-z]+', span.lower())
                    # Only the six whole ter- and se- words are taught: no new ones are built.
                    for w in words:
                        for pre in ('ter', 'se'):
                            if w.startswith(pre) and w[len(pre):] in ADJECTIVES:
                                self.assertIn(w, WHOLE_WORDS, (l['title'], line))
                    # Spoken forms sit on a line that labels them spoken.
                    for i, w in enumerate(words):
                        if w in spoken_words and not (w == 'tengah' and words[i + 1:i + 2] == ['hari']):
                            self.assertRegex(line, label, (l['title'], line))
                    # Words placed after chapter 6 are not used.
                    for w in ('dekat', 'jauh', 'kedai', 'sini', 'sana', 'tolong', 'baju', 'kerusi', 'lif'):
                        self.assertNotIn(w, words, line)
                self.assertNotRegex(line.lower(), r'assalam|waalaikum|insya|alhamdulillah|bismillah|halal|haram|doa\b|puasa')
                self.assertNotRegex(line.lower(), r'\b\d+\s*(mg|ml|tablet|pil)\b')
        # The explanations name the one rule: «sama … dengan» and «paling» are the productive forms.
        pat = ' '.join(self.lines(self.comp('Pattern and grammar')))
        self.assertIn('Building new words like these is a later chapter', pat)
        notes = ' '.join(self.cfg['teacher_notes'])
        self.assertIn('productive ‹ter-› is chapter 16', notes)

    def test_sam_rules_and_scene_facts(self):
        """Brief rules for chapter 6: the condo scene uses only words from chapters 1 to 6; places and prices are fictional."""
        everything = ' '.join(x for l in self.by_unit[self.u] for _, items, _ in l['sections'] for x in items + l['key'])
        self.assertIn('Orang lain sudah ambil kondo B', everything)
        self.assertIn('setiap bulan', everything)
        # Sam's follow-up (12 Nov 2026): rent, rooms and spacious are used in the condo scenes.
        for w in ('«Berapa sewa kondo A?»', 'ada tiga bilik', 'luas'):
            self.assertIn(w, everything, w)
        cfg = self.cfg
        scene = ' '.join(s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening'])
        for w in ('sewa', 'bilik', 'luas'):
            self.assertIn(w, scene.lower(), w)
        self.assertEqual({lid for _, ids in cfg['core_groups'] for lid in ids} & {'L-1051', 'L-1052', 'L-1053'},
                         {'L-1051', 'L-1052', 'L-1053'})
        self.assertIn('fictional', everything)
        sources = ' '.join(self.lines(self.comp('Culture note')) + self.comp('Culture note')['key'])
        for name in ('Strata Management Act 2013', 'Klang Valley', 'Wikipedia'):
            self.assertIn(name, sources, name)
        # The note names no price, rent or neighbourhood.
        culture = ' '.join(self.lines(self.comp('Culture note'), 'English'))
        self.assertNotRegex(culture, r'RM|ringgit')

    def test_openers_have_no_leftover_english(self):
        for unit in ('ms-c04a', 'ms-c04b', 'ms-c05', 'ms-c06'):
            opener = next(l for l in self.by_unit[unit] if l['suite']['component_type'] == 'Opener')
            for line in self.lines(opener):
                if line.startswith('After class'):
                    ja = line.split(' / ')[-1]
                    self.assertNotRegex(ja, r'\band\b', (unit, ja))
        opener = next(l for l in self.by_unit[self.u] if l['suite']['component_type'] == 'Opener')
        self.assertIn('Sedia Kelas c06 (16 cards, frames ms-c06-f01 and ms-c06-f02)', ' '.join(self.lines(opener)))

    def test_fast_pack(self):
        self.assertIn('ms-c06-fast', self.by_unit)
        l = self.by_unit['ms-c06-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertTrue(15 <= len(core) <= 20)
        # Fast words are a digest of the unit core words, never new ones.
        self.assertTrue(set(fast.C6_WORDS) <= set(self.cfg['core']))
        labels = ' '.join(n for n, _, _ in l['sections'])
        for part in ('Can-do', 'Core words', 'Key patterns', 'Model conversation', 'Task', 'Self-check', 'Self-study'):
            self.assertIn(part, labels)
        for line in self.lines(l, 'Key patterns'):
            if re.match(r'^\d · ', line):
                self.assertEqual(line.split('e.g.')[1].count(' / '), 1, line)
        self.assertTrue(10 <= len(self.lines(l, 'Model conversation')) <= 16)
        n_check = sum(x.startswith('☐') for x in self.lines(l, 'Self-check'))
        self.assertEqual(n_check, 5)
        self.assertTrue(all(f'{i} «' in l['key'][0] for i in range(1, n_check + 1)))
        page = {x['title']: x for x in bank()}[l['title']]
        count = len(page['pages']) - 3 - page.get('key_pages', 1)
        self.assertTrue(2 <= count <= 4, count)
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch6 = next(c for c in chapters if c['title'].startswith('Chapter 6'))
        self.assertIn(l['title'], ch6['fast_items'])
        self.assertEqual(ch6['status'], 'Step 5d chapter 6 suite · draft for pilot')
        # The self-study guide names the Sedia Kelas set and the Dunia scene.
        guide = ' '.join(self.lines(l, 'Self-study'))
        self.assertIn('Sedia Kelas c06', guide)
        self.assertIn('Main badminton', guide)
        self.assertIn('ms-c06-001 to ms-c06-034', guide)
        # The whole-word note and the two re-used chapter 4 words are in the core list.
        core_text = ' '.join(self.lines(l, 'Core words'))
        self.assertIn('Whole words to learn as they are', core_text)
        self.assertIn('«sekali»', core_text)

    def test_review_block_after_unit_6(self):
        """Stage 1 plan: a 45-minute review block after unit 6, covering chapters 1 to 6, registered in the catalogue."""
        l = next(x for x in self.by_unit[self.u] if x['suite']['id'] == 'ms-c06-review-block')
        self.assertIn('Chapters 1 to 6', l['title'])
        self.assertEqual(l['suite']['time_minutes'], 45)
        self.assertEqual(l['suite']['block'], 'Skills')
        txt = ' '.join(self.lines(l))
        # One question or sentence for every chapter from 1 to 6, and a peer check for each.
        for w in ('Selamat pagi', 'tinggal di mana', 'Berapa sewa', 'pukul berapa', 'Kenapa', 'pilih yang mana'):
            self.assertIn(w, txt, w)
        for ch in ('chapter 3', 'chapter 4', 'chapter 5', 'chapter 6', 'chapters 1 and 2'):
            self.assertIn(ch, txt, ch)
        self.assertNotRegex(txt.lower(), r'kurang suku')
        self.assertTrue(any(x.startswith('Model:') for x in l['key']))
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        catalogue = make_catalogue(bank(), chapters)
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage1-review-6')
        self.assertEqual(block['component_ids'], ['ms-c06-review-block'])
        self.assertEqual(block['status'], 'pilot draft')

    def test_legacy_retirement_and_catalogue(self):
        built = {x['title'] for x in bank()}
        self.assertFalse(any(t == 'Comparisons and superlatives' or t.startswith('Comparisons and superlatives ·') for t in built))
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch6 = next(c for c in chapters if c['title'].startswith('Chapter 6'))
        self.assertEqual([u['label'] for u in ch6['units']], ['6'])
        self.assertEqual(ch6['status'], 'Step 5d chapter 6 suite · draft for pilot')
        catalogue = make_catalogue(bank(), chapters)
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('check_unit') == self.u]
        self.assertTrue(mine)
        self.assertTrue(all(c['chapter_id'] == 'ms-c06' and c['review_status'] == 'draft' for c in mine))
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertFalse([k for k, e in exceptions.items() if e['unit'] in (self.u, 'ms-c06-fast')])
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        self.assertIn(self.u, reauthored)


if __name__ == '__main__':
    unittest.main()
