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
