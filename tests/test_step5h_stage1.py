"""Step 5h: the Stage 1 close. The unit 9 follow-ups are tested in test_step5g_suite; this file tests the stage review block
(after unit 9) and the A1 stage test.

Stage review: one integrated scenario that needs all nine chapters, all 54 Kata-Kata frames of chapters 1 to 9 back in the block
(charter rule 7, spaced return), a can-do self-check for every Stage 1 goal, registration in the catalogue, natural standard
Malay with no spoken forms unlabelled and «jalan terus» (not «jalan lurus»).
"""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite
from suite import stage1
from catalogue import make_catalogue, GOALS

ROOT = Path(__file__).resolve().parents[1]


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def chapters_js():
    return json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])


class StageReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.mine = [l for l in cls.lessons if l['suite']['check_unit'] == 'ms-stage1']
        cls.review = next(l for l in cls.mine if l['suite']['id'] == 'ms-stage1-review')

    def lines(self, l, part=None):
        return [x for name, items, _ in l['sections'] if part is None or part in name for x in items]

    def text(self, l):
        return ' '.join(self.lines(l) + l['key'])

    def test_shape_and_timing(self):
        r = self.review
        self.assertEqual(r['suite']['component_type'], 'Task')
        self.assertEqual(r['suite']['sub_type'], 'review')
        self.assertEqual(r['suite']['time_minutes'], 45)
        names = [n for n, _, _ in r['sections']]
        minutes = [int(m) for n in names for m in re.findall(r'\((\d+) min\)', n)]
        self.assertEqual(sum(minutes), 45, names)
        for part in ('Recall', 'Model', 'Role cards', 'Read and write', 'Can-do self-check'):
            self.assertTrue(any(part in n for n in names), part)
        self.assertEqual(r['suite']['prerequisite_chapters'], [f'ms-c{n:02}' for n in range(1, 10)])
        self.assertIn('Japanese awaiting native review', r['header'])

    def test_one_scenario_needs_all_nine_chapters(self):
        week = ' '.join(stage1.WEEK)
        for n in range(1, 10):
            self.assertRegex(week, rf'chapters? [^)]*\b{n}\b', n)
        model = self.lines(self.review, 'Model')
        days = [x for x in model if x.startswith('■ ')]
        self.assertEqual([d.split(' ')[1] for d in days], ['Monday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        self.assertIn('fictional', ' '.join(self.lines(self.review, 'Goal')))
        # Recall: one prompt per chapter.
        self.assertEqual([x.split(':')[0] for x in stage1.RECALL], [f'Ch {n}' for n in range(1, 10)])

    def test_every_frame_returns(self):
        """Charter rule 7: each pattern reappears in the stage review. Every Kata-Kata frame of chapters 1 to 9 is used."""
        frames = []
        for n in range(1, 10):
            frames += [f['id'] for f in json.loads((ROOT / f'curriculum/reference/katakata/c{n:02}.json').read_text())['frames']]
        self.assertEqual(len(frames), 54)
        self.assertEqual(set(stage1.FRAME_RETURNS), set(frames))
        self.assertEqual(set(self.review['suite']['pattern_ids']), set(frames))
        body = ' '.join(self.lines(self.review))
        for fid, where in stage1.FRAME_RETURNS.items():
            self.assertIn(where, body, fid)
        key = ' '.join(self.review['key'])
        for fid in frames:
            self.assertIn(fid[-3:] + ' «', key, fid)
        # Sam's correction (12 Nov 2026): «jalan terus», never «jalan lurus».
        self.assertNotIn('jalan lurus', self.text(self.review).lower())
        self.assertIn('Jalan terus, kemudian belok kiri', body)

    def test_can_do_self_check_covers_every_stage1_goal(self):
        self.assertEqual([stage1.CHARTER_GOALS[n] for n in range(1, 10)], GOALS)
        check = self.lines(self.review, 'Can-do self-check')
        for n in range(1, 10):
            self.assertIn(f'■ Chapter {n} · {GOALS[n - 1]}', check)
            self.assertGreaterEqual(len(stage1.CANDO[n]), 2)
            for en, ja in stage1.CANDO[n]:
                self.assertIn(f'☐ {en} / {ja}', check)
                self.assertRegex(ja, r'[ぁ-んァ-ン一-龥]')
        # The charter goal's parts are all ticked somewhere.
        cando = ' '.join(en for n in stage1.CANDO for en, _ in stage1.CANDO[n]).lower()
        for part in ('greet', 'title', 'how someone is', 'take leave', 'name', 'from', 'work', 'live', 'hobby', 'price',
                     'change', 'age', 'phone number', 'sequence', 'time', 'day', 'routine', 'done', 'not yet', 'describe',
                     'feel', 'choose', 'compare', 'same', 'best', 'where', 'route', 'bus', 'counter', 'how many', 'signs',
                     'notices', 'by whom'):
            self.assertIn(part, cando, part)

    def test_reading_and_prices(self):
        self.assertEqual(len(stage1.NOTICE_Q), 6)
        key = ' '.join(self.review['key'])
        for i in range(1, 7):
            self.assertIn(f'{i}. ', key)
        self.assertIn('Model message: «', key)
        # Tuesday: 5.00 + 6.00 + 2 × 2.00 + 5 × 0.50 = 17.50; change from 20 is 2.50.
        self.assertAlmostEqual(5.00 + 6.00 + 2 * 2.00 + 5 * 0.50, 17.50)
        body = ' '.join(self.lines(self.review, 'Model'))
        self.assertIn('tujuh belas ringgit lima puluh sen', body)
        self.assertIn('Baki dua ringgit lima puluh sen', body)
        self.assertIn('Pisang goreng lima puluh sen sekeping', body)

    def test_malay_rules(self):
        everything = []
        for l in self.mine:
            everything += self.lines(l) + l['key'] + [t['prompt'] + ' ' + t['answer_key'] for t in l['suite']['tests']]
        label = re.compile(r'spoken|speech|話し言葉|口語', re.I)
        for line in everything:
            for span in re.findall(r'«([^»]*)»', line):
                words = re.findall(r'[a-z]+', span.lower())
                for w in ('toko', 'bis', 'mobil', 'toilet', 'karcis', 'apel', 'lurus'):
                    self.assertNotIn(w, words, line)
                for w in ('nak', 'tapi', 'sikit', 'dah', 'tak', 'senang', 'saja', 'tapau', 'jom', 'tengok'):
                    if w in words:
                        self.assertRegex(line, label, line)
                # No productive ber- or me- (the sign «Dilarang merokok» is the one recognised chunk).
                for w in words:
                    self.assertFalse(re.fullmatch(r'ber[a-z]{3,}', w) and w not in ('berapa', 'bersih', 'besar', 'berat'), w)
                    self.assertFalse(re.fullmatch(r'me[a-z]{4,}', w) and w not in ('merokok', 'mesyuarat', 'merah', 'meter', 'mengapa', 'menu', 'melayu'), w)
        text = ' '.join(everything).lower()
        self.assertNotRegex(text, r'assalam|waalaikum|insya|alhamdulillah|bismillah|halal|haram|solat|doa\b')

    def test_registration(self):
        self.assertIn('ms-stage1', json.loads((ROOT / 'curriculum/reauthored-units.json').read_text()))
        ch9 = next(c for c in chapters_js() if c['title'].startswith('Chapter 9'))
        page = {x['title']: x for x in bank()}
        self.assertIn(self.review['title'], ch9['stage_items'])
        self.assertIn(self.review['title'], ch9['items'])
        self.assertGreater(ch9['items'].index(self.review['title']), max(ch9['items'].index(t) for t in ch9['units'][0]['items']))
        self.assertEqual([u['label'] for u in ch9['units']], ['9'])
        self.assertIn(self.review['title'], page)
        catalogue = make_catalogue(bank(), chapters_js())
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage1-review')
        self.assertEqual(block['after_unit'], 'ms-c09')
        self.assertEqual(block['component_ids'], ['ms-stage1-review'])
        self.assertEqual(block['status'], 'pilot draft')
        comp = next(c for c in catalogue['components'] if c['id'] == 'ms-stage1-review')
        self.assertTrue(comp['authored'])
        self.assertEqual(comp['level'], 'A1')
        self.assertEqual(comp['chapter_id'], 'ms-c09')
        self.assertEqual(set(comp['pattern_ids']), set(stage1.FRAME_RETURNS))


if __name__ == '__main__':
    unittest.main()


class StageTest(unittest.TestCase):
    """The A1 stage test: four sections per version, 20 marks each, every chapter represented, ledger words from chapters 1
    to 9 only, complete item-by-item keys."""
    SECTIONS = ('listening', 'reading', 'writing', 'speaking')

    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.mine = {l['suite']['id']: l for l in cls.lessons if l['suite']['check_unit'] == 'ms-stage1'}

    def comp(self, v, sec):
        return self.mine[f'ms-stage1-test-{v.lower()}-{sec}']

    def lines(self, l):
        return [x for _, items, _ in l['sections'] for x in items]

    def test_sections_exist_and_carry_twenty_marks(self):
        for version in stage1.VERSIONS:
            v = version['label']
            for sec in self.SECTIONS:
                l = self.comp(v, sec)
                self.assertEqual(l['suite']['component_type'], 'Test')
                self.assertEqual(l['suite']['sub_type'], sec)
                self.assertEqual({t['sub_type'] for t in l['suite']['tests']}, {sec})
                self.assertEqual(l['suite']['time_minutes'], stage1.TIMING[sec])
                self.assertIn(f'Version {v}', l['title'])
            marks = {}
            for code, sub, m, ch in stage1.item_map(version):
                marks.setdefault(sub, []).append((code, m))
            self.assertEqual(sum(m for _, m in marks['listening']), 20)
            self.assertEqual(sum(m for _, m in marks['reading']), 20)
            self.assertEqual(sum(m for _, m in marks['writing']), 20)
            sp = dict(marks['speaking'])
            self.assertEqual(sp[f'{v}-S1'], 8)
            cards = [m for c, m in sp.items() if '-S2.' in c]
            self.assertEqual((len(cards), set(cards)), (4, {6}))
            self.assertEqual(sp[f'{v}-S1'] + 2 * 6, 20)
            self.assertGreaterEqual(len(marks['listening']), 8)
            self.assertGreaterEqual(len(marks['reading']), 8)

    def test_every_chapter_is_represented(self):
        for version in stage1.VERSIONS:
            imap = stage1.item_map(version)
            covered = {c for _, _, _, ch in imap for c in ch}
            self.assertEqual(covered, set(range(1, 10)), version['label'])
            # Each chapter is tested by at least two items, and in the written paper or the speaking test both.
            for n in range(1, 10):
                self.assertGreaterEqual(sum(n in ch for _, _, _, ch in imap), 2, (version['label'], n))
            # Real tasks for the four strands: announcements and conversations; signs, a price board, a message and a notice
            # with «Dilarang»; a form and a message; a self-introduction and role-play cards.
            r = ' '.join(' '.join(p['text']) for p in version['reading'])
            self.assertIn('«Dilarang', r)
            self.assertRegex(r, r'RM\d')
            self.assertIn('WhatsApp', r)
            self.assertTrue(any(p['form'] for p in version['writing']))
            self.assertTrue(any('message' in p['title'].lower() for p in version['writing']))
            self.assertTrue(any('announcement' in t['title'].lower() for t in version['listening']))
            self.assertEqual(len(version['speaking']['cards']), 4)

    def test_tags_match_the_item_map(self):
        for version in stage1.VERSIONS:
            v = version['label']
            imap = {code: ch for code, _, _, ch in stage1.item_map(version)}
            for sec in self.SECTIONS:
                for t in self.comp(v, sec)['suite']['tests']:
                    code = f"{v}-{t['prompt'].split(' ')[0].rstrip('.')}"
                    self.assertIn(code, imap)
                    self.assertEqual(set(t['grammar_points']), {f'ms-c{c:02}-g01' for c in imap[code]}, code)
                    self.assertTrue(t['word_ids'], code)
                    self.assertRegex(t['prompt'], r'\[\d+ marks?\]$')
                    self.assertRegex(t['prompt'], r'[ぁ-んァ-ン一-龥]')

    def test_only_ledger_words_from_chapters_1_to_9(self):
        """The build blocks ledger gaps in re-authored units; this re-checks every marked span at chapter 9 directly."""
        checker = self.ledger.checker
        segs = []
        for l in self.mine.values():
            for line in self.lines(l) + l['key'] + [t['prompt'] + ' ' + t['answer_key'] for t in l['suite']['tests']]:
                for span in re.findall(r'«([^«»]*)»', line):
                    segs.append({'unit': 'ms-stage1', 'chapter': 9, 'source': line[:40], 'source_text': line, 'kind': 'test', 'text': span})
        self.assertGreater(len(segs), 200)
        result = checker.inspect(segs)
        self.assertFalse(result['ledger_gaps'], list(result['ledger_gaps'])[:5])
        bad = [k for k, e in result['violations'].items() if e['check'] != 'register']
        self.assertFalse(bad, bad[:5])
        rows = self.ledger.rows
        for l in [x for x in bank() if x.get('suite', {}).get('check_unit') == 'ms-stage1']:
            self.assertTrue(l['suite']['word_ids'], l['title'])
            for wid in l['suite']['word_ids']:
                lid = wid if wid.startswith('L-') else next(r['ID'] for r in rows.values() if wid in r['Kata-Kata (card IDs)'])
                nums = [int(x) for x in re.findall(r'Ch\s*(\d+)', rows[lid]['Kata-Kata place'])] + \
                       [int(x) for x in re.findall(r'ms-c(\d+)-', rows[lid]['Kata-Kata (card IDs)'])]
                self.assertTrue(nums and min(nums) <= 9, (wid, lid))

    def test_answer_keys_are_complete(self):
        for version in stage1.VERSIONS:
            v = version['label']
            for sec in self.SECTIONS:
                l = self.comp(v, sec)
                key = ' '.join(l['key'])
                for t in l['suite']['tests']:
                    code = t['prompt'].split(' ')[0].rstrip('.')
                    self.assertTrue(t['answer_key'].strip(), code)
                    self.assertIn(code + (':' if sec != 'speaking' else ''), key, code)
                    marks = int(re.search(r'\[(\d+) marks?\]', t['prompt'])[1])
                    if sec in ('listening', 'reading'):
                        # Every mark has its own answer: "(1)" per fact, or the full marks on one answer.
                        ones = t['answer_key'].count('(1)')
                        self.assertTrue(ones == marks or f'({marks}' in t['answer_key'], (code, t['answer_key']))
                    elif 'One mark per field' in t['answer_key']:
                        form = next(p for p in version['writing'] if p['form'])['form']
                        self.assertEqual(len(form) - 1, marks, code)
                        for i in range(1, marks + 1):
                            self.assertRegex(t['answer_key'], rf'(^|\s){i} «', (code, i))
                    else:
                        parts = [int(x) for x in re.findall(r'(?:Content|Task|Language|Accuracy|Interaction and delivery|Change of plan) (\d)', t['answer_key'])]
                        self.assertEqual(sum(parts), marks, (code, parts))
                        self.assertIn('Model', t['answer_key'], code)
            # Listening: the teacher key carries the full script of every task, and every Malay answer is in its script.
            key = ' '.join(self.comp(v, 'listening')['key'])
            for task in version['listening']:
                script = ' '.join(line for _, line in task['script'])
                for _, line in task['script']:
                    self.assertIn(f'«{line}»', key)
                for it in task['items']:
                    for quoted in re.findall(r'«([^»]*)»', it['a']):
                        self.assertIn(quoted.lower(), script.lower(), quoted)
            # Speaking: examiner lines and a rubric for every card.
            sk = ' '.join(self.comp(v, 'speaking')['key'])
            for n in range(1, 5):
                self.assertIn(f'S2.{n} examiner:', sk)
                self.assertIn(f'S2.{n} rubric (6):', sk)
            self.assertIn('S1 rubric (8):', sk)

    def test_prices_add_up(self):
        a = stage1.VERSION_A
        self.assertAlmostEqual(2 * 1.50 + 1.00 + 2.00, 6.00)   # A-L8: two roti canai, an egg, a teh tarik
        self.assertAlmostEqual(10.00 - 6.00, 4.00)
        self.assertAlmostEqual(2 * 1.50 + 2.00, 5.00)          # A-R3
        self.assertAlmostEqual(10.00 - (5.00 + 1.80), 3.20)     # A-R5
        board = ' '.join(a['reading'][1]['text'])
        for price in ('RM1.50 sekeping', 'RM2.00 secawan', 'RM5.00 sepinggan', 'RM1.80 secawan', 'RM1.00 sebotol', 'RM3.50 sebungkus'):
            self.assertIn(price, board)
        script = ' '.join(line for _, line in a['listening'][2]['script'])
        self.assertIn('Semua enam ringgit', script)
        self.assertIn('Baki empat ringgit', script)
