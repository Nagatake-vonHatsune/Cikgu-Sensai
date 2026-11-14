"""Step 5h: the Stage 1 close. The unit 9 follow-ups are tested in test_step5g_suite; this file tests the stage review block
(after unit 9) and the A1 stage test.

Stage review: one integrated scenario that needs all nine chapters, all 56 Kata-Kata frames of chapters 1 to 9 back in the block
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
        # 54 before the Kata-Kata clean-up (34710c6); the clean-up added ms-c05-f06 (Kenapa / Mengapa) and ms-c06-f07 (Saya pilih).
        self.assertEqual(len(frames), 56)
        self.assertIn('ms-c05-f06', frames)
        self.assertIn('ms-c06-f07', frames)
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
        self.assertEqual([stage1.CHARTER_GOALS[n] for n in range(1, 10)], GOALS[:9])  # GOALS[9] is chapter 10 (Stage 2)
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
        script = ' '.join(line for t in a['listening'] if 'food stall' in t['title'] for _, line in t['script'])
        self.assertIn('Semua enam ringgit', script)
        self.assertIn('Baki empat ringgit', script)

    def test_version_b_prices_add_up(self):
        b = stage1.VERSION_B
        self.assertAlmostEqual(5.50 + 2 * 0.50 + 2.00, 8.50)   # B-L8: nasi goreng, two pisang goreng, a kopi
        self.assertAlmostEqual(10.00 - 8.50, 1.50)
        self.assertAlmostEqual(3 * 1.50, 4.50)                  # B-R3
        self.assertAlmostEqual(20.00 - (2 * 3.00 + 5 * 1.20), 8.00)  # B-R5
        board = ' '.join(b['reading'][1]['text'])
        for price in ('Epal · RM1.50 sebiji', 'Oren · RM1.20 sebiji', 'Mangga · RM3.00 sebiji'):
            self.assertIn(price, board)
        script = ' '.join(line for t in b['listening'] if 'food stall' in t['title'] for _, line in t['script'])
        self.assertIn('Semua lapan ringgit lima puluh sen', script)
        self.assertIn('Baki satu ringgit lima puluh sen', script)

    def test_chapter_6_is_compulsory_in_both_versions(self):
        """Sam, 12 Nov 2026 (step 5h question 4): one compulsory comparison item in both versions (listening L5, «lebih …
        daripada» and «paling»), and speaking card 2 is always used."""
        for version in stage1.VERSIONS:
            v = version['label']
            flagged = [(t['title'], it) for t in version['listening'] for it in t['items'] if it.get('compulsory')]
            self.assertEqual(len(flagged), 1, v)
            title, item = flagged[0]
            self.assertEqual(item['ch'], [6])
            self.assertEqual(item['marks'], 2)
            self.assertEqual(stage1.compulsory_codes(version), [f'{v}-L5', f'{v}-S2.2'])
            # The item sits in the listening paper, its script has both forms, and the key gives both facts.
            task = next(t for t in version['listening'] if any(i.get('compulsory') for i in t['items']))
            script = ' '.join(line for _, line in task['script'])
            self.assertIn(' lebih ', script); self.assertIn(' daripada ', script); self.assertIn(' paling ', script)
            self.assertEqual(len(task['items']), 1)
            self.assertEqual(item['a'].count('(1)'), 2)
            self.assertIn('«lebih', item['a']); self.assertIn('paling', item['a'])
            listening = self.comp(v, 'listening')
            self.assertIn(f'{v}-L5'.split('-')[1] + ': ', ' '.join(listening['key']))
            self.assertIn('Compulsory comparison item', ' '.join(listening['key']))
            # Item-to-chapter mapping: chapter 6 is tested by L5, R4 and card 2 (S2.2) in both versions.
            imap = {code: ch for code, _, _, ch in stage1.item_map(version)}
            self.assertEqual({c for c, ch in imap.items() if 6 in ch}, {f'{v}-L5', f'{v}-R4', f'{v}-S2.2'})
            # Section totals stay at 20 marks with ten listening items.
            self.assertEqual(sum(1 for c in imap if '-L' in c), 10)
            # Speaking card 2 is the comparison card and is marked compulsory on the sheet and in the key.
            card2 = version['speaking']['cards'][stage1.CARD_COMPULSORY - 1]
            self.assertIn(6, card2['ch'])
            sheet = ' '.join(self.lines(self.comp(v, 'speaking')))
            self.assertIn('always used', sheet)
            self.assertIn('Compulsory card', ' '.join(self.comp(v, 'speaking')['key']))
            self.assertIn('Card 2 (comparing) is always used', sheet)
        admin = ' '.join(self.lines(self.mine['ms-stage1-test-admin']))
        self.assertIn('Chapter 6 (comparing) is compulsory in both versions', admin)
        self.assertIn('A-L5 · 2 · ch 6 · compulsory (chapter 6)', admin)
        self.assertIn('B-S2.2 ', admin)

    def test_pass_mark_and_blocks_are_sams_decisions(self):
        rec = make_catalogue(bank(), chapters_js())['stages'][0]
        self.assertEqual(rec['stage_test']['pass_rule'], dict(total_min=48, section_min=10, status="Sam's decision, 12 Nov 2026"))
        self.assertEqual(rec['stage_test']['compulsory_items'], {'A': ['A-L5', 'A-S2.2'], 'B': ['B-L5', 'B-S2.2']})
        admin = ' '.join(self.lines(self.mine['ms-stage1-test-admin']))
        self.assertIn('two extra 45-minute blocks', admin)
        self.assertIn('76 blocks', admin)
        self.assertIn('Block 1, the written papers', admin)
        self.assertIn('Block 2, speaking', admin)
        import catalogue as cat
        self.assertIn("'class_blocks':76", Path(cat.__file__).read_text())
        self.assertNotIn("'class_blocks':74", Path(cat.__file__).read_text())

    def test_signs_and_notices_in_the_reading_paper(self):
        """Sam, 12 Nov 2026: «tolak», «tarik», «perhatian», «hingga» and «Selamat Pesta Kaamatan» are used in the reading
        section (the Gawai greeting is the parallel in version B)."""
        for version in stage1.VERSIONS:
            text = ' '.join(' '.join(p['text']) for p in version['reading'])
            for sign in ('«TOLAK»', '«TARIK»', '«PERHATIAN:', ' hingga '):
                self.assertIn(sign, text, (version['label'], sign))
            questions = ' '.join(it['q'] + ' ' + it['a'] for p in version['reading'] for it in p['items'])
            self.assertTrue('TOLAK' in questions or 'TARIK' in questions, version['label'])
            self.assertIn('hingga', questions)
        self.assertIn('Selamat Pesta Kaamatan', ' '.join(' '.join(p['text']) for p in stage1.VERSION_A['reading']))
        self.assertIn('Selamat Hari Gawai', ' '.join(' '.join(p['text']) for p in stage1.VERSION_B['reading']))

    def test_versions_are_parallel(self):
        a, b = stage1.VERSION_A, stage1.VERSION_B
        ma, mb = stage1.item_map(a), stage1.item_map(b)
        self.assertEqual([(c[2:], s, m) for c, s, m, _ in ma], [(c[2:], s, m) for c, s, m, _ in mb])
        for (ca, _, _, cha), (cb, _, _, chb) in zip(ma, mb):
            # The same chapters are tested in the same place, give or take one supporting chapter.
            self.assertTrue(set(cha) & set(chb), (ca, cb))
        # Different facts: no listening line that carries a fact, and no reading text, is shared (stock phrases such as
        # «Makan sini atau bungkus?» may recur).
        sa = {line for t in a['listening'] for _, line in t['script'] if len(line) > 25}
        sb = {line for t in b['listening'] for _, line in t['script'] if len(line) > 25}
        self.assertFalse(sa & sb)
        self.assertFalse(set(' '.join(p['text']) for p in a['reading']) & set(' '.join(p['text']) for p in b['reading']))

    def test_scripts_and_administration_sheet(self):
        scripts = self.mine['ms-stage1-test-scripts']
        text = ' '.join(self.lines(scripts))
        for version in stage1.VERSIONS:
            for task in version['listening']:
                for _, line in task['script']:
                    self.assertIn(f'«{line}»', text)
        admin = self.mine['ms-stage1-test-admin']
        self.assertEqual(admin['suite']['component_type'], 'Teaching plan')
        body = ' '.join(self.lines(admin) + admin['key'])
        for part in ('Timing', 'Materials', 'Running the test', 'Scoring and pass mark', 'Item map · Version A',
                     'Item map · Version B', 'Result sheet'):
            self.assertIn(part, ' '.join(n for n, _, _ in admin['sections']) + body, part)
        self.assertIn('48 or more out of 80 (60 per cent), and at least 10 out of 20 in every section', body)
        self.assertIn('Sam\'s decision of 12 Nov 2026', body)
        self.assertNotIn('proposal for Sam', body)
        self.assertIn('not an official CEFR certificate', body)
        self.assertIn('keeps no learner records', body)
        # The item map lists every item and every chapter with its can-do goal, for both versions.
        for version in stage1.VERSIONS:
            for code, _, m, ch in stage1.item_map(version):
                self.assertIn(f'{code} · {m} · ch ', body)
            for n in range(1, 10):
                self.assertIn(f'Ch {n} · {GOALS[n - 1]}: {version["label"]}-', body)
        minutes = sum(stage1.TIMING[s] for s in ('listening', 'reading', 'writing'))
        self.assertEqual(minutes, 45)

    def test_catalogue_stage_record(self):
        """The charter's "CEFR label shown in the Evaluator" (section 10, phase 3): the catalogue carries a Stage 1 record with
        its CEFR level and the completion flag and label. No learner data."""
        catalogue = make_catalogue(bank(), chapters_js())
        stage = next(s for s in catalogue['stages'] if s['id'] == 'ms-stage1')
        self.assertEqual(stage['cefr'], 'A1')
        self.assertEqual(stage['chapter_ids'], [f'ms-c{n:02}' for n in range(1, 10)])
        self.assertEqual(stage['review_block_id'], 'ms-stage1-review')
        self.assertEqual(stage['completion']['flag'], 'stage1_complete')
        self.assertEqual(stage['completion']['cefr'], 'A1')
        self.assertIn('Nothing is built in Hanashishou', stage['completion']['evaluator_note'])
        self.assertIn('none', stage['learner_records'])
        st = stage['stage_test']
        self.assertEqual(st['pass_rule']['total_min'], 48)
        self.assertEqual(st['total_marks'], 80)
        ids = {c['id'] for c in catalogue['components']}
        for v in ('A', 'B'):
            self.assertEqual(len(st['versions'][v]), 4)
            self.assertTrue(set(st['versions'][v]) <= ids)
        self.assertIn(st['scripts_id'], ids)
        self.assertIn(st['administration_id'], ids)
        # Every stage-test item in the catalogue has its chapters, and the ids match the generated test items.
        items = {t['id'] for t in catalogue['test_items'] if t['id'].startswith('ms-stage1-test-')}
        self.assertEqual(items, set(st['item_chapters']))
        for chapters in st['item_chapters'].values():
            self.assertTrue(chapters and all(c in stage['chapter_ids'] for c in chapters))
        for c in catalogue['chapters']:
            # Chapters 1 to 9 are Stage 1 (A1); chapter 10 onward is Stage 2 (A2), built from Stage 2 build step 4.
            stage1_chapter = int(c['id'][-2:]) <= 9
            self.assertEqual(c['level'], 'A1' if stage1_chapter else 'A2')
            self.assertEqual(c['stage_id'], 'ms-stage1' if stage1_chapter else 'ms-stage2')
        ch9 = next(c for c in chapters_js() if c['title'].startswith('Chapter 9'))
        for title in ('Stage 1 · A1 stage test · Version A · Listening', 'Stage 1 · A1 stage test · Version B · Speaking',
                      'Stage 1 · A1 stage test · Administration sheet (teacher)'):
            self.assertIn(title, ch9['stage_items'])


class KataKataCleanup(unittest.TestCase):
    """The Kata-Kata clean-up brief (docs/kata-kata-cleanup.md) was carried out in the Kata-Kata repository and ended at
    Kata-Kata 34710c6 (report docs/CLEANUP-2026-11-12.md there). The ledger copy synced from the sheet at the end of the
    clean-up shows the result: the actions are done, so this test now checks that nothing is left open for Kata-Kata,
    apart from the items the Kata-Kata report itself leaves open."""

    # Open actions that remain in the ledger after the clean-up, none of them a Kata-Kata change (Kata-Kata report,
    # "Not done, unverified or for another session"): Kamus Dewan checks, "refresh Cikgu Sensai snapshot" (this sync does it;
    # the sheet cells are Sam's to clear), Hanashishou work, and rows Sam retired.
    ALLOWED_OPEN = [
        r'KD4 check( \([^)]*\))?(; refresh Cikgu Sensai snapshot)?',
        r'refresh Cikgu Sensai snapshot',
        r'KD4 check; refresh Kata-Kata Dunia card',  # L-0530 only: stale, Kata-Kata did it in step 3e (see the comment in the test)
        r'KD4 check; Cikgu Sensai: rewrite the 3B line that uses it',
        r'remove from Cikgu Sensai unit 1 \(vocabulary, culture note, pronunciation, teaching plan\)',
        r'Hanashishou: map the daily-life card to L-0330',
        r'Hanashishou root-word rule: .*',
        r'Retired: use L-0336 hospital \(Sam 12 Nov\)',
        r'Duplicate of L-0702 \(hujung minggu\); use L-0702',
    ]

    def rows(self):
        import csv
        return list(csv.DictReader((ROOT / 'curriculum/reference/katakata/malay-ledger.csv').open(encoding='utf-8', newline='')))

    def test_no_open_kata_kata_action_is_left(self):
        import re
        rows = self.rows()
        self.assertEqual(len(rows), 1309)  # L-0001 to L-1088 (Stage 1), L-1089 to L-1265 (Stage 2 build step 1, Sam approved 13 Nov 2026), L-1266 to L-1272 (takpe, tidak boleh tahan, mendaftar, tangguhkan, batalkan, memakai, berwarna; Sam, synced from Kata-Kata 7fbe173), L-1273 to L-1309 (37 rows from Kata-Kata step 3e, 907946f: 31 core, 6 practice pool)
        # L-0530 «tandatangan» still says "refresh Kata-Kata Dunia card" in the sheet: Kata-Kata did that in its step 3e
        # (ms-d-pejabat-pagi-08 rebuilt) and the Cikgu Sensai session may not edit the sheet, so the stale cell is
        # allowed here until a ledger session clears it (Stage 2 clean-up report, questions).
        self.assertEqual([r['ID'] for r in rows if 'kata-kata' in r['Action (open)'].lower()], ['L-0530'])
        # Every remaining open action is one of the known kinds; a new kind (for example "Add ... card" without the words
        # Kata-Kata) fails here and has to be looked at.
        for r in rows:
            action = r['Action (open)'].strip()
            if action:
                self.assertTrue(any(re.fullmatch(p, action) for p in self.ALLOWED_OPEN), (r['ID'], action))
        # No place cell says "(pending)" any more, and the scene rename (Sam, Journal row 80) is in the place column.
        self.assertFalse([r['ID'] for r in rows if 'pending' in r['Kata-Kata place'].lower()])
        self.assertFalse([r['ID'] for r in rows if 'Hari Raya' in r['Kata-Kata place']])

    def test_every_card_listed_in_the_brief_now_exists(self):
        import re
        doc = (ROOT / 'docs/kata-kata-cleanup.md').read_text()
        rows = {r['ID']: r for r in self.rows()}
        new = re.findall(r'^\| (L-\d{4}) \|', doc, re.M)
        self.assertEqual(len(new), 112)  # the brief's "New cards" tables
        # Every pinned chapter file (c01 to c18 since the Stage 2 build step 4 refresh).
        cards = {c['id'] for n in range(1, 19)
                 for c in json.loads((ROOT / f'curriculum/reference/katakata/c{n:02}.json').read_text())['cards']}
        for lid in new:
            ids = [x.strip() for x in rows[lid]['Kata-Kata (card IDs)'].split(',') if x.strip()]
            self.assertTrue(ids, lid)
            for card in ids:
                if card.startswith('ms-c'):
                    self.assertIn(card, cards, (lid, card))
        # Every chapter card the ledger points at is in the pinned files.
        for lid, r in rows.items():
            for card in re.findall(r'ms-c\d\d-\d{3}', r['Kata-Kata (card IDs)']):
                self.assertIn(card, cards, (lid, card))

    def test_the_brief_still_names_the_decisions(self):
        doc = (ROOT / 'docs/kata-kata-cleanup.md').read_text()
        for must in ('ms-c01-009', 'L-0592', 'L-0330', 'ms-c07-024', 'jalan terus', 'kurang suku', 'Rumah terbuka Hari Raya',
                     'Hanashishou mappings', 'Do not edit the Kata-Kata repository', 'Kata-Kata 34710c6'):
            self.assertIn(must, doc, must)
