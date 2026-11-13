"""Step 5f and 5g chapter 8: charter section 6 and 14 minimums for unit 8 (penjodoh bilangan) and the chapter 8 fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (41 core
entries, including the six rows Sam approved on 12 Nov 2026, and 11 Dunia "Beli baju" recognition entries; the counter
cards placed in earlier chapters are revision), the component minimums, the cumulative question words with «berapa»
and a counter, real item-by-item answer keys, word tags on every test item, and the chapter 8 Malay rules («se-» with
every counter beside «satu» + counter; the counter dropped in everyday speech marked as such; spoken forms labelled;
the register Sam confirmed on 12 Nov 2026; no faith-specific expressions; nothing placed after chapter 8).
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c08, fast
from catalogue import make_catalogue

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
CLOTHES = 'Beli baju'
WHOLE = {'seekor', 'sebiji', 'sebuah'}
COUNTERS = ['ekor', 'biji', 'batang', 'helai', 'keping', 'pucuk', 'kuntum', 'pasang', 'ulas', 'naskhah', 'bungkus', 'cawan',
            'pinggan', 'mangkuk', 'botol', 'tin', 'kotak', 'orang', 'buah', 'kaki']


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def first_chapter(r):
    nums = [int(x) for x in re.findall(r'Ch\s*(\d+)', r['Kata-Kata place'])]
    nums += [int(x) for x in re.findall(r'ms-c(\d+)-', r['Kata-Kata (card IDs)'])]
    return min(nums) if nums else None


def has_c08_card(r):
    return 'ms-c08-' in r['Kata-Kata (card IDs)']


def ch8_placed(rows):
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired' and re.search(r'Ch\s*8\b', r['Kata-Kata place'])}


def ch8_core(rows):
    """First placed in chapter 8 and carrying a chapter 8 card. Since the Kata-Kata clean-up (34710c6) every row added
    on 12 Nov 2026 (L-1064 to L-1069) has its card, and no place cell says "(pending)" any more."""
    return {lid for lid in ch8_placed(rows) if first_chapter(rows[lid]) == 8 and has_c08_card(rows[lid])}


def ch8_recognition(rows):
    """Dunia rows that prime chapter 8, are first placed there and have no chapter 8 card."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired' and 'primes Ch8' in r['Kata-Kata place']
            and first_chapter(r) == 8 and not has_c08_card(r)}


class Chapter8Minimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.cfg = ms_c08.CFG
        cls.u = 'ms-c08'

    def comp(self, typ, sub=None, unit=None):
        found = [l for l in self.by_unit[unit or self.u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)]
        self.assertTrue(found, f'missing {typ}/{sub}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=None):
        out = []
        for u in units or [self.u, 'ms-c08-fast']:
            for l in self.by_unit[u]:
                out += [x for _, items, _ in l['sections'] for x in items] + l['key']
                for t in l['suite']['tests']:
                    out += [t['prompt'], t['answer_key']]
        return out

    def marked_words(self, units=None):
        words = []
        for line in self.all_lines(units):
            for span in re.findall(r'«([^»]*)»', line):
                words += re.findall(r'[a-z]+', span.lower())
        return words

    def test_ledger_partition(self):
        rows = self.ledger.rows
        placed = ch8_placed(rows)
        # The ledger copy (Kata-Kata 34710c6) places 58 rows in chapter 8: 41 first-placed core (35 with a chapter 8 card,
        # plus the six rows Sam approved on 12 Nov 2026: L-1064 to L-1069, now with their cards), 11 Dunia "Beli baju" words
        # (primes Ch8) whose only chapter is 8 and carry no chapter 8 card, and 6 rows placed in earlier chapters that also
        # have a chapter 8 card (orang, surat, payung, buku, ikan, kertas). It was 60 before the clean-up: «kaki» (L-0488)
        # lost its counter card (Sam: not a counter) and the fruit «buah» (L-0514) lost its card, which was re-pointed to the
        # counter row L-1067, so neither is placed in chapter 8 any more.
        self.assertEqual(len(placed), 58)
        core_all = ch8_core(rows)
        self.assertEqual(len(core_all), 41)
        self.assertEqual({rows[x]['Malay'] for x in core_all if int(x[2:]) >= 1064},
                         {'nasi lemak', 'gerai', 'tambah', 'buah (penjodoh bilangan)', 'pisang goreng / goreng pisang', 'keropok lekor'})
        rec_all = ch8_recognition(rows)
        self.assertEqual(len(rec_all), 11)
        carried = placed - core_all - rec_all
        self.assertEqual({rows[x]['Malay'] for x in carried},
                         {'orang', 'surat', 'payung', 'buku', 'ikan', 'kertas'})
        self.assertNotIn('L-0488', placed)
        self.assertNotIn('L-0514', placed)
        core = self.cfg['core']
        self.assertEqual(len(core), len(set(core)))
        self.assertEqual(set(core), core_all)
        rec = [lid for _, ids in self.cfg['recognition'] for lid in ids]
        self.assertEqual(len(rec), len(set(rec)))
        self.assertEqual(set(rec), rec_all)
        self.assertEqual({s: len(ids) for s, ids in self.cfg['recognition']}, {CLOTHES: 11})
        for lid in rec:
            self.assertIn('Dunia · Beli baju (primes Ch8)', rows[lid]['Kata-Kata place'])
        groups = dict(self.cfg['core_groups'])
        self.assertEqual(list(groups), ['Classifiers', 'Containers and portions', 'The things counted', 'At the «gerai»',
                                        'All, please and takeaway'])
        self.assertEqual({k: len(v) for k, v in groups.items()},
                         {'Classifiers': 14, 'Containers and portions': 7, 'The things counted': 12, 'At the «gerai»': 5,
                          'All, please and takeaway': 3})
        self.assertEqual([lid for ids in groups.values() for lid in ids], core)
        # «baju» is both a Dunia word and a chapter 8 card: core, not recognition.
        self.assertIn('L-0500', core)
        self.assertNotIn('L-0500', rec)
        # Revision: placed in chapters 1 to 7, never counted as new core or recognition.
        rev = {lid for _, ids in self.cfg['revision'] for lid in ids}
        self.assertFalse(rev & set(core))
        self.assertFalse(rev & set(rec))
        for lid in rev:
            r = rows[lid]
            self.assertLessEqual(first_chapter(r), 7, lid)
        # «orang» (counter) is revision with a new use; «buah» as a counter is now its own core row (L-1067), «buah» as fruit
        # (L-0514) stays revision.
        for lid in ('L-0058', 'L-0514'):
            self.assertIn(lid, rev)
        self.assertEqual(rows['L-0058']['Malay'], 'orang')
        self.assertEqual(rows['L-0514']['Malay'], 'buah')
        self.assertEqual(rows['L-1067']['Malay'], 'buah (penjodoh bilangan)')
        self.assertEqual(rows['L-1067']['POS'], 'classifier')
        self.assertIn('L-1067', core)
        self.assertNotIn('L-0514', core)
        # «kaki» as a counter is not added (Sam, 12 Nov 2026: too rare): it is not core and is not used as a counter.
        self.assertNotIn('L-0488', core)
        self.assertEqual(rows['L-0488']['Meaning (EN)'], 'foot, leg')
        mw = self.marked_words()
        self.assertFalse([1 for a, b in zip(mw, mw[1:]) if b == 'kaki' and a in ('satu', 'dua', 'tiga', 'seekor', 'sekaki')])
        # Sam's other answers of 12 Nov 2026, as they stand in the ledger copy.
        self.assertEqual(rows['L-0592']['Review status'], 'Retired')
        self.assertTrue(rows['L-0931']['Meaning (JA)'].startswith('ママック（'))
        self.assertIn('pisang goreng follows', rows['L-1068']['Sam\'s notes'] if False else rows['L-1068']["Sam's notes"])
        # The whole ledger words.
        for lid, word in (('L-0360', 'seekor'), ('L-0361', 'sebiji'), ('L-0362', 'sebuah')):
            self.assertEqual(rows[lid]['Malay'], word)
            self.assertIn(lid, core)

    def test_revision_words_really_return(self):
        """Revision words must be used in the unit (outside the vocabulary list), not listed to fill a count."""
        used = set()
        for l in self.by_unit[self.u]:
            if l['suite']['component_type'] == 'Vocabulary':
                continue
            for line in [x for _, items, _ in l['sections'] for x in items] + l['key']:
                for span in re.findall(r'«([^»]*)»', line):
                    toks = re.findall(r'[a-z]+(?:-[a-z]+)*', span.lower())
                    used.add(' '.join(toks))
                    used.update(toks)
        text = ' '.join(used)
        for _, ids in self.cfg['revision']:
            for lid in ids:
                forms = [re.sub(r'\([^)]*\)', '', f).strip().lower() for f in self.ledger.row(lid)['Malay'].split('/')]
                self.assertTrue(any(re.search(r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', text) for f in forms), (lid, forms))

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
        self.assertIn(f'"{CLOTHES}"', txt)
        for lid in ('L-0937', 'L-0213'):
            self.assertIn('spoken', next(x for x in entries if f'[{lid}]' in x))
        orang = next(x for x in entries if '[L-0058]' in x)
        buah = next(x for x in entries if '[L-1067]' in x)
        self.assertIn('counter', orang)
        self.assertIn('counter', buah)
        self.assertIn('«seorang»', orang)
        self.assertIn('At the «gerai»', txt)
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
        self.assertEqual(ids, [f'ms-c08-f0{n}' for n in range(1, 6)])
        self.assertEqual(l['suite']['pattern_ids'], ids)
        body = ' '.join(self.lines(l))
        for w in ('«Saya mahu»', 'number', 'counter', '«seekor»', '«sebiji»', '«sebuah»', '‹se-›', '«sehelai»', '«satu»', '«Berapa»',
                  '«berapa»', '«semua»', '«Tolong bungkus»', '«Tambah»', '«Makan sini atau bungkus?»', '«tapau»', '«ekor»',
                  '«biji»', '«batang»', '«helai»', '«kuntum»', '«pasang»', '«orang»', '«buah»', '«gerai»', '«goreng pisang»',
                  'everyday speech'):
            self.assertIn(w, body, w)
        # Pattern 3 asks with «berapa» + a counter and the Japanese bridge names 何 + counter.
        p3 = ' '.join(self.lines(l, 'Pattern 3'))
        self.assertIn('Berapa biji telur?', p3)
        self.assertIn('何個', p3)

    def test_se_with_every_counter(self):
        """Sam, 12 Nov 2026: ‹se-› + any counter is normal Malay and is the chapter 8 pattern. Every counter is taught with
        its ‹se-› form beside «satu» + counter."""
        words = self.marked_words()
        fused = {'seekor', 'sebiji', 'sebuah', 'sebatang', 'sehelai', 'sekeping', 'sepucuk', 'sekuntum', 'sepasang', 'seulas',
                 'senaskhah', 'sebungkus', 'secawan', 'sepinggan', 'semangkuk', 'sebotol', 'setin', 'sekotak', 'seorang'}
        for w in sorted(fused):
            self.assertIn(w, words, f'«{w}» is never used as Malay')
        # Every ledger counter taught here (ekor ... kotak, orang) has its fused form used in the unit and its form named
        # in its vocabulary entry.
        v = self.lines(self.comp('Vocabulary'))
        for lid, se in ms_c08.SE.items():
            entry = next(x for x in v if f'[{lid}]' in x)
            self.assertIn(f'«{se}»', entry, lid)
        # Fused forms of the counters, and no other fused form, appear; none comes from a word that is not a counter.
        for w in set(words):
            m = re.fullmatch(r'se(' + '|'.join(COUNTERS) + ')', w)
            if m:
                self.assertIn(w, fused, w)
        # «satu» + counter is used just as much.
        n = sum(1 for a, b in zip(words, words[1:]) if a == 'satu' and b in COUNTERS)
        self.assertGreaterEqual(n, 10)
        # The three whole ledger words are used at least three times each.
        for w in WHOLE:
            self.assertGreaterEqual(words.count(w), 3, w)
        # ‹se-› is shown with a drill for each direction: «satu» + counter -> ‹se-› + counter and back.
        tr = ' '.join(self.lines(self.comp('Drill', 'transform')))
        self.assertIn('Say it with ‹se-›', tr)
        self.assertIn('Say it with «satu» and the counter', tr)
        # «sebatang» and «sehelai» are no longer mentions: they are taught forms.
        mentions = json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']
        self.assertNotIn('sebatang', mentions)
        self.assertNotIn('sehelai', mentions)
        self.assertIn('ms-c08-f02', mentions['se'])
        text = ' '.join(self.all_lines())
        self.assertNotIn('‹sebatang›', text)
        self.assertNotIn('‹sehelai›', text)
        notes = ' '.join(self.cfg['teacher_notes'])
        self.assertIn('«se-»' if False else '‹se-› + any counter is normal Malay', notes)

    def test_se_forms_pass_the_language_checks(self):
        """No ledger gap or violation for ‹se-› + a ledger counter: the existing derivation rule covers them (see the 5g report)."""
        from language_checks import Checker
        checker = Checker()
        forms = sorted(self.cfg['vocab_opts'] and {ms_c08.SE[k] for k in ms_c08.SE} | {'seorang', 'seekor', 'sebiji', 'sebuah'})
        segs = [{'unit': 'x', 'source': 'x', 'text': f, 'chapter': 8, 'kind': 'model', 'source_text': f} for f in forms]
        result = checker.inspect(segs)
        self.assertFalse(result['violations'])
        self.assertFalse(result['ledger_gaps'])
        derived = {d['term'] for d in result['derivations']}
        self.assertTrue({'sehelai', 'sebatang', 'secawan', 'sebungkus', 'sekotak', 'seorang'} <= derived)

    def test_gerai_scene_and_register(self):
        """The gerai scene Sam suggested, and the register he confirmed on 12 Nov 2026."""
        text = ' '.join(self.all_lines())
        for frag in ('Sebungkus nasi lemak', 'dua keping pisang goreng', 'Tambah satu lagi', 'Ada keropok lekor?'):
            self.assertIn(frag, text, frag)
        self.assertGreaterEqual(text.count('goreng pisang'), 3)
        v = self.lines(self.comp('Vocabulary'))
        pisang = next(x for x in v if '[L-1068]' in x)
        self.assertIn('standard', pisang)
        self.assertIn('everyday', pisang)
        for lid in ('L-0348', 'L-0352'):
            entry = next(x for x in v if f'[{lid}]' in x)
            self.assertIn('formal counter, mostly seen in writing', entry, lid)
        self.assertIn('everyday speech', next(x for x in v if '[L-0937]' in x))
        notes = ' '.join(self.cfg['teacher_notes'])
        self.assertIn('«pucuk» and «naskhah» are formal counters, mostly seen in writing', notes)
        self.assertIn('«tapau» is everyday speech', notes)
        # Unit 7: «sesak» is standard, «jam» is everyday speech.
        from suite import ms_c07
        self.assertIn('standard', ms_c07.VOCAB_OPTS['L-0620']['en'])
        self.assertIn('«sesak» is standard and «jam» is everyday speech', ' '.join(ms_c07.CFG['teacher_notes']))
        # «kaki» as a counter and "nasi lemak" are handled as Sam decided.
        self.assertNotIn('‹nasi lemak›', text)

    def test_counter_dropped_is_everyday_speech(self):
        """Earlier units say «dua epal» and «Mi goreng satu»; this unit shows the counter form beside them."""
        v = self.lines(self.comp('Vocabulary'))
        ent = {lid: v[v.index(next(x for x in v if f'[{lid}]' in x)) + 1] for lid in ('L-1003', 'L-0934', 'L-0102')}
        for lid, ex in ent.items():
            self.assertRegex(ex, r'everyday speech', (lid, ex))
        p5 = ' '.join(self.lines(self.comp('Pattern and grammar'), 'Pattern 5'))
        self.assertRegex(p5, r'everyday speech')
        self.assertIn('dua cawan teh tarik', p5)
        self.assertIn('dua teh tarik', p5)
        culture = ' '.join(self.lines(self.comp('Culture note'), 'English'))
        self.assertIn('everyday speech', culture)
        self.assertIn('Both forms are right', culture)
        # The careful form is what the task and the writing model use.
        self.assertIn('Sepinggan mi goreng', self.cfg['task_key'])
        notes = ' '.join(self.cfg['teacher_notes'])
        self.assertIn('«dua epal»', notes)
        self.assertIn('«Mi goreng satu»', notes)

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
        qset = self.comp('Drill', 'question-word set')
        full = ' '.join(self.lines(qset))
        for w in ('«apa»', '«siapa»', '«di mana»', '«Siapakah»', '«Apakah»', '«di manakah»', '«Adakah»',
                  '«Bolehkah»', '«berapa»', '«bila»', '«pukul berapa»', '«hari apa»',
                  '«bagaimana»', '«macam mana»', '«kenapa»', '«mengapa»', '«apa sebab»', '«sebab»', '«kerana»',
                  '«yang mana»', '«pilih»', '«ke mana»', '«dari mana»', '«berapa jauh»', '«berapa lama»',
                  '«berapa» with a counter', '«Berapa biji?»', '«Berapa ekor?»', '«Berapa orang?»'):
            self.assertIn(w, full, w)
        key = ' '.join(qset['key'])
        for q in ('«Awak mahu berapa biji telur?»', '«Telur ini dari mana?»', '«Berapa jauh pasar dari sini?»',
                  '«Berapa lama jalan kaki ke pasar?»', '«Awak pergi ke mana?»'):
            self.assertIn(q, key, q)
        self.assertEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(qset)), 17)
        for i in range(1, 18):
            self.assertRegex(key, rf'(^|\s){i} «', i)
        choice = ' '.join(self.comp('Drill', 'question-word choice')['key'])
        for w in ('«Berapa»', '«Di mana»', '«Bila»', '«Yang mana»', '«Kenapa»', '«Bagaimana»'):
            self.assertIn(w, choice, w)
        # The Q&A drill asks «Berapa biji telur?» / «Berapa orang?» with a counter.
        qa = ' '.join(self.lines(self.comp('Drill', 'question and answer')))
        self.assertIn('Berapa biji telur?', qa)
        self.assertIn('Berapa orang?', qa)

    def test_markers_return(self):
        """Charter section 14: the tense and aspect markers come back in every later chapter."""
        l = self.comp('Drill', 'markers')
        txt = ' '.join(self.lines(l))
        for m in ('«belum»', '«sudah»', '«masih»', '«akan»', '«baru»'):
            self.assertIn(m, txt, m)
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(l)), 6)
        key = ' '.join(l['key'])
        for i in range(1, 9):
            self.assertRegex(key, rf'(^|\s){i} «', i)

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

    def test_prices_add_up(self):
        """The invented prices in the model conversations, the listening and the task add up."""
        # Market: 2 fish at 8, 10 eggs at 0.50, 1 chicken at 14 = 35; paid 50, change 15.
        self.assertEqual(2 * 8 + 10 * 0.5 + 14, 35)
        dlg = ' '.join(s for _, s in self.cfg['dialogue'])
        for frag in ('lapan ringgit seekor', 'lima puluh sen sebiji', 'empat belas ringgit seekor', 'tiga puluh lima ringgit',
                     'lima puluh ringgit', 'lima belas ringgit'):
            self.assertIn(frag, dlg, frag)
        # Stationery: 3 pens at 2, 2 boxes of tissues at 4, 10 sheets at 0.50 = 19; paid 20, change 1.
        self.assertEqual(3 * 2 + 2 * 4 + 10 * 0.5, 19)
        var = ' '.join(s for _, s in self.cfg['variant'])
        for frag in ('Dua ringgit sebatang', 'empat ringgit sekotak', 'lima puluh sen sehelai', 'sembilan belas ringgit',
                     'satu ringgit'):
            self.assertIn(frag, var, frag)
        # Flowers: 8 at 5 = 40; paid 50, change 10. Mamak: 3 roti canai + 2 teh tarik = 14.50; paid 20, change 5.50.
        self.assertEqual(8 * 5, 40)
        self.assertEqual(20 - 14.5, 5.5)
        lis = ' '.join(s for _, s in self.cfg['listening'])
        # Gerai: 1 nasi lemak at 3, then 2 + 1 pisang goreng at 1 each, 1 keropok lekor at 5, 1 teh tarik at 3.50 = 14.50.
        self.assertEqual(3 + 3 * 1 + 5 + 3.5, 14.5)
        for frag in ('empat puluh ringgit', 'sepuluh ringgit', 'empat belas ringgit lima puluh sen', 'lima ringgit lima puluh sen',
                     'tiga ringgit sebungkus', 'satu ringgit sekeping', 'Lima ringgit sebungkus'):
            self.assertIn(frag, lis, frag)
        # Task: 1 mi goreng 6 + 1 teh tarik 3.50 + 3 roti canai at 2.50 = 17; two more teh tarik = 24; paid 30, change 6.
        self.assertEqual(6 + 3.5 + 3 * 2.5, 17)
        self.assertEqual(17 + 2 * 3.5, 24)
        key = self.cfg['task_key']
        for frag in ('tujuh belas ringgit', 'dua puluh empat ringgit', 'Baki enam ringgit'):
            self.assertIn(frag, key, frag)
        # Price board at the gerai: 4 pisang goreng = 4; 2 nasi lemak + 1 teh tarik = 9.50.
        self.assertEqual(4 * 1, 4)
        self.assertEqual(2 * 3 + 3.5, 9.5)
        board = ' '.join(self.cfg['reading'])
        for frag in ('RM3 sebungkus', 'RM1 sekeping', 'RM5 sebungkus', 'RM3.50 secawan'):
            self.assertIn(frag, board, frag)

    def test_japanese_has_no_leftover_english(self):
        """Japanese cells are full translations: Latin letters appear only inside marked Malay, ids or product names."""
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Dunia|Sedia Kelas|Tanya Cikgu|Susun Ayat|UTC|RM')
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
        for opts in cfg['vocab_opts'].values():
            if 'ja' in opts:
                self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', opts['ja'])), opts['ja'])

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
        self.assertIn('Sedia Kelas c08', body)
        self.assertIn('0–5', body)
        # Unit 8 has no extra block in the Stage 1 plan.
        self.assertFalse(any(l['suite']['block'] == 'Skills' for l in self.by_unit[self.u]))

    def test_chapter8_malay_rules(self):
        label = re.compile(r'spoken|speech|話し言葉|口語', re.I)
        everything = self.by_unit[self.u] + self.by_unit.get('ms-c08-fast', [])
        for l in everything:
            lines = [x for _, items, _ in l['sections'] for x in items] + l['key']
            for line in lines:
                for span in re.findall(r'«([^»]*)»', line):
                    words = re.findall(r'[a-z]+', span.lower())
                    # Indonesian look-alikes are never used.
                    for w in ('toko', 'bis', 'mobil', 'toilet', 'koran', 'apel', 'kantong'):
                        self.assertNotIn(w, words, line)
                    for w in words:
                        if w in ('nak', 'tapi', 'sikit', 'dah', 'tak', 'senang', 'saja', 'tapau'):
                            self.assertRegex(line, label, (l['title'], line))
                # Nothing faith-specific, no food rules.
                self.assertNotRegex(line.lower(), r'assalam|waalaikum|insya|alhamdulillah|bismillah|halal|haram|puasa|solat|sembahyang|azan|khutbah|ibadat|doa\b')
        # «nasi lemak» is a ledger word since 12 Nov 2026 (L-1064) and is used as Malay.
        self.assertTrue([line for line in self.all_lines() if re.search(r'«[^»]*nasi lemak[^»]*»', line)])

    def test_sam_rules_and_scene_facts(self):
        """Practice stalls and prices are fictional; the culture note names its sources."""
        everything = ' '.join(self.all_lines())
        self.assertIn('fictional', everything)
        notes = self.comp('Culture note')
        sources = ' '.join(self.lines(notes) + notes['key'])
        for name in ('ms-c08-043', '-005 («batang»', "Sam's brief", 'L-0937', 'L-1068', 'L-1069', 'fictional'):
            self.assertIn(name, sources, name)
        culture = ' '.join(self.lines(notes, 'English'))
        # No law, price list or percentage is stated as a fact about the real country.
        self.assertNotRegex(culture, r'\d+\.?\d*\s*(%|per cent|RM|ringgit)')
        # Each etymology comes from a Kata-Kata card note (the "lit." glosses on the cards) and none from Sam's corrected notes.
        for lit in ('tail', 'seed', 'stem', 'strand', 'bud', 'shoot'):
            self.assertIn(lit, culture, lit)

    def test_dunia_scene_is_recognition_only(self):
        rec = [lid for _, ids in self.cfg['recognition'] for lid in ids]
        core_cards = {self.ledger.word_id(self.ledger.row(lid)) for lid in self.cfg['core']}
        for t in self.comp('Test')['suite']['tests']:
            if t['sub_type'] == 'words':
                for lid in rec:
                    self.assertNotIn(self.ledger.word_id(self.ledger.row(lid)), t['word_ids'])
        self.assertTrue(core_cards)
        plan = ' '.join(self.lines(self.comp('Teaching plan')))
        self.assertIn('Beli baju', plan)

    def test_openers_have_no_leftover_english(self):
        for unit in ('ms-c07', 'ms-c08'):
            opener = next(l for l in self.by_unit[unit] if l['suite']['component_type'] == 'Opener')
            for line in self.lines(opener):
                if line.startswith('After class'):
                    ja = line.split(' / ')[-1]
                    self.assertNotRegex(ja, r'\band\b', (unit, ja))
        opener = next(l for l in self.by_unit[self.u] if l['suite']['component_type'] == 'Opener')
        self.assertIn(f'Sedia Kelas c08 ({katakata_ref.sedia_count(8)} cards, frames ms-c08-f01 and ms-c08-f02)', ' '.join(self.lines(opener)))
        # Every chapter's opener count is the real Sedia Kelas size in the pinned file, in English and Japanese.
        self.assertIn(f'（カード{katakata_ref.sedia_count(8)}枚、文型 f01・f02）', ' '.join(self.lines(opener)))

    def test_fast_pack(self):
        self.assertIn('ms-c08-fast', self.by_unit)
        l = self.by_unit['ms-c08-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertTrue(15 <= len(core) <= 20)
        self.assertTrue(set(fast.C8_WORDS) <= set(self.cfg['core']))
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
        ch8 = next(c for c in chapters if c['title'].startswith('Chapter 8'))
        self.assertIn(l['title'], ch8['fast_items'])
        self.assertEqual(ch8['status'], 'Step 5f chapter 8 suite · draft for pilot')
        guide = ' '.join(self.lines(l, 'Self-study'))
        self.assertIn('Sedia Kelas c08', guide)
        self.assertIn(CLOTHES, guide)
        self.assertIn(f'all {katakata_ref.card_count(8)} Kata-Kata chapter 8 cards (ms-c08-001 to ms-c08-{katakata_ref.last_own_card(8):03}', guide)

    def test_catalogue_and_registration(self):
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch8 = next(c for c in chapters if c['title'].startswith('Chapter 8'))
        self.assertEqual([u['label'] for u in ch8['units']], ['8'])
        catalogue = make_catalogue(bank(), chapters)
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('check_unit') == self.u]
        self.assertTrue(mine)
        self.assertTrue(all(c['chapter_id'] == 'ms-c08' and c['review_status'] == 'draft' for c in mine))
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 20)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'] in (self.u, 'ms-c08-fast')])
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for unit in (self.u, 'ms-c08-fast'):
            self.assertIn(unit, reauthored)
        # Chapter 7 is untouched: its writing block is registered.
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage1-writing-7')
        self.assertEqual(block['component_ids'], ['ms-c07-writing-block'])


if __name__ == '__main__':
    unittest.main()
