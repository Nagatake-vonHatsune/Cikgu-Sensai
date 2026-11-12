"""Step 5g chapter 9: charter section 6 and 14 minimums for unit 9 (the passive di-, signs and notices) and the chapter 9
fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (42 core entries;
33 Dunia recognition entries in two scenes, the general «rumah terbuka» scene with Sam's six festival words and the
"Simpulan bahasa harian" idioms, which are never drilled), the component minimums, the cumulative question words with
«siapa» + «oleh», real item-by-item answer keys, word tags on every test item, the «di-» rule (the ledger forms plus
«di-» + a ledger verb root, no ber- or me-), the festival notes (each festival's own words inside its note, a named source,
no faith-specific greeting) and the registration of the unit.
"""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c09, fast
from catalogue import make_catalogue

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
RUMAH = 'Rumah terbuka'
IDIOMS = 'Simpulan bahasa harian'
SECTION_VERBS = ['dibuat', 'dibeli', 'dijual', 'dimakan', 'diminum', 'dibaca', 'ditulis', 'dibuka', 'ditutup', 'dibayar',
                 'dihantar', 'diambil', 'dipanggil', 'dimasak', 'dicuci', 'dibawa', 'disewa', 'dilarang']


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def first_chapter(r):
    nums = [int(x) for x in re.findall(r'Ch\s*(\d+)', r['Kata-Kata place'])]
    nums += [int(x) for x in re.findall(r'ms-c(\d+)-', r['Kata-Kata (card IDs)'])]
    return min(nums) if nums else None


def has_c09_card(r):
    return 'ms-c09-' in r['Kata-Kata (card IDs)']


def ch9_placed(rows):
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired' and re.search(r'Ch\s*9\b', r['Kata-Kata place'])}


NEW_CH9 = {f'L-{i:04d}' for i in range(1076, 1089)}


def ch9_core(rows):
    """First placed in chapter 9 and carrying a chapter 9 card, or one of the chapter 9 rows Sam approved on 12 Nov 2026
    (L-1076 to L-1083, and L-1084 to L-1088 from step 5i, placed "Ch9 (pending)" until Kata-Kata adds their cards)."""
    return {lid for lid in ch9_placed(rows) if first_chapter(rows[lid]) == 9 and 'primes Ch9' not in rows[lid]['Kata-Kata place']
            and (has_c09_card(rows[lid]) or rows[lid]['Kata-Kata place'] == 'Ch9 (pending)')}


def ch9_recognition(rows):
    """Dunia rows that prime chapter 9 and carry no chapter 9 card (the Raya words, Sam's six festival words, the idioms)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired' and 'primes Ch9' in r['Kata-Kata place']
            and first_chapter(r) == 9 and not has_c09_card(r)}


class Chapter9Minimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.cfg = ms_c09.CFG
        cls.u = 'ms-c09'

    def comp(self, typ, sub=None, unit=None, slug=None):
        found = [l for l in self.by_unit[unit or self.u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=None):
        out = []
        for u in units or [self.u, 'ms-c09-fast']:
            for l in self.by_unit.get(u, []):
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
        placed = ch9_placed(rows)
        core_all = ch9_core(rows)
        # 42 core entries: L-0377 to L-0405, Sam's eight rows L-1076 to L-1083 and his five rows L-1084 to L-1088 (step 5i). «pinggan» (L-0355) carries a chapter 9 card
        # but was placed in chapter 8.
        self.assertEqual(len(core_all), 42)
        self.assertEqual(core_all, {f'L-{i:04d}' for i in range(377, 406)} | NEW_CH9)
        self.assertEqual({rows[x]['Malay'] for x in NEW_CH9},
                         {'buat', 'panggil', 'cuci', 'larang', 'tuan rumah', 'mari', 'ibu', 'adik',
                          'pesta', 'perhatian', 'hingga', 'tolak', 'tarik'})
        rec_all = ch9_recognition(rows)
        # 27 Dunia entries in the ledger as handed over (Rumah terbuka Hari Raya 13, Simpulan bahasa harian 14) plus Sam's six
        # festival words of 12 Nov 2026 (L-1070 to L-1075).
        self.assertEqual(len(rec_all), 33)
        raya = {lid for lid in rec_all if 'Rumah terbuka Hari Raya' in rows[lid]['Kata-Kata place']}
        simpulan = {lid for lid in rec_all if 'Simpulan bahasa harian' in rows[lid]['Kata-Kata place']}
        festival = {lid for lid in rec_all if 'Rumah terbuka (primes Ch9; pending)' in rows[lid]['Kata-Kata place']}
        self.assertEqual((len(raya), len(simpulan), len(festival)), (13, 14, 6))
        self.assertEqual({rows[x]['Malay'] for x in festival},
                         {'Tahun Baru Cina / Tahun Baharu Cina', 'Deepavali', 'Krismas', 'Gawai', 'Kaamatan', 'angpau'})
        carried = placed - core_all - rec_all
        self.assertEqual({rows[x]['Malay'] for x in carried}, {'pinggan'})
        core = self.cfg['core']
        self.assertEqual(len(core), len(set(core)))
        self.assertEqual(set(core), core_all)
        rec = [lid for _, ids in self.cfg['recognition'] for lid in ids]
        self.assertEqual(len(rec), len(set(rec)))
        self.assertEqual(set(rec), rec_all)
        self.assertEqual({s: len(ids) for s, ids in self.cfg['recognition']}, {RUMAH: 19, IDIOMS: 14})
        groups = dict(self.cfg['core_groups'])
        self.assertEqual(list(groups), ['«di-» verbs', 'Roots for the «di-» rule', '«oleh», «pada», «tadi», «siap»',
                                        'Signs and notices', 'A party and an open house', 'Family'])
        self.assertEqual([len(v) for v in groups.values()], [18, 4, 4, 9, 5, 2])
        self.assertEqual([lid for ids in groups.values() for lid in ids], core)
        # The 18 «di-» rows are the ledger's di- forms.
        self.assertEqual([rows[x]['Malay'] for x in ms_c09.DI_VERBS], SECTION_VERBS)
        # Revision: placed in chapters 1 to 8, never counted as new core or recognition.
        rev = {lid for _, ids in self.cfg['revision'] for lid in ids}
        self.assertFalse(rev & set(core))
        self.assertFalse(rev & set(rec))
        for lid in rev:
            self.assertLessEqual(first_chapter(rows[lid]), 8, lid)
        self.assertIn('L-0355', rev)

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
        self.assertIn(f'"{RUMAH}"', txt)
        self.assertIn(f'"{IDIOMS}"', txt)
        # Each «di-» verb shows its root, and every root is now a ledger word marked as Malay (L-1076 to L-1079 since 12 Nov).
        for lid, root in ms_c09.ROOTS.items():
            entry = next(x for x in entries if f'[{lid}]' in x)
            self.assertIn(root, entry, lid)
            self.assertTrue(root.startswith('«'), lid)
        mentions = json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']
        for m, card in (('jamu', 'ms-c09-029'), ('me', 'ms-c09-024')):
            self.assertIn(card, mentions[m], m)
        for m in ('buat', 'panggil', 'cuci', 'larang'):
            self.assertNotIn(m, mentions, m)
        # «Dilarang merokok» is a sign to recognise only.
        self.assertIn('recognise only', next(x for x in entries if '[L-0400]' in x))
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
        self.assertEqual(ids, [f'ms-c09-f0{n}' for n in range(1, 6)])
        self.assertEqual(l['suite']['pattern_ids'], ids)
        body = ' '.join(self.lines(l))
        for w in ('«dibuat oleh»', '«oleh»', '«siapa»', '«sudah»', '«belum»', '«pada»', '«tadi»', '«Dilarang»', '«Sila»',
                  '«papan tanda»', '«dibuka»', '«ditutup»', '«digoreng»', '«dipilih»', '«ditunggu»', 'Pinggan saya bawa ke dapur',
                  'Kata-Kata frame f06', '受身'):
            self.assertIn(w, body, w)
        p1 = ' '.join(self.lines(l, 'Pattern 1'))
        self.assertIn('Kek ini dibuat oleh siapa?', p1)
        self.assertIn('neutral', p1)

    def test_di_rule(self):
        """«di-» + a root verb the learner already knows. The language checks accept «di-» + any ledger word placed in chapters
        1 to 9 without looking at its part of speech, so this test is stricter: the ledger «di-» forms, and «di-» + a ledger
        verb. No ber- or me- verbs, and no «di-» form of a noun."""
        rows = self.ledger.rows
        ledger_di = {rows[x]['Malay'].lower() for x in ms_c09.DI_VERBS}
        verbs = set()
        for r in rows.values():
            if r['Review status'] != 'Retired' and r['POS'].startswith('verb') and first_chapter(r) is not None and first_chapter(r) <= 9:
                for f in r['Malay'].split('/'):
                    verbs.add(re.sub(r'\([^)]*\)', '', f).strip().lower())
        found = set()
        for w in set(self.marked_words()):
            if w in ('di', 'dia', 'dapur', 'dalam', 'dengan', 'dari', 'dekat', 'datang', 'depan', 'dan', 'dua', 'dulu', 'dilarang'):
                continue
            if re.fullmatch(r'di[a-z]+', w):
                if w in ledger_di:
                    continue
                self.assertIn(w[2:], verbs, f'«{w}»: the root is not a ledger verb')
                found.add(w)
        # The productive forms are taught and used.
        for w in ('digoreng', 'dipilih', 'ditunggu', 'dijemput', 'ditanya'):
            self.assertIn(w, ' '.join(self.lines(self.comp('Pattern and grammar'), 'Pattern 2')).lower(), w)
        self.assertTrue(found & {'digoreng', 'ditunggu'}, found)
        # No ber- / me- verbs anywhere in marked Malay (the sign «Dilarang merokok» is the one recognised chunk).
        for w in set(self.marked_words()):
            self.assertFalse(re.fullmatch(r'ber[a-z]{3,}', w) and w not in ('berapa', 'bersih', 'besar', 'berat'), w)
            self.assertFalse(re.fullmatch(r'me[a-z]{4,}', w) and w not in ('merokok', 'mesyuarat', 'merah', 'meter', 'mengapa', 'menu', 'melayu'), w)
        # The roots «buat», «panggil», «cuci», «larang» (L-1076 to L-1079) are ledger words now and are used as Malay.
        for w in ('buat', 'panggil', 'cuci', 'larang'):
            self.assertIn(w, set(self.marked_words([self.u])), w)
        transform = ' '.join(self.comp('Drill', 'transform')['key'])
        self.assertIn('«Kuih ini dibuat oleh ibu saya.»', transform)
        self.assertIn('«Encik Tanaka dipanggil oleh Puan Aini.»', transform)

    def test_step5h_new_words_in_use(self):
        """Sam, 12 Nov 2026: L-1076 to L-1083 are used naturally in the unit (outside the vocabulary list), and tested."""
        used = []
        for l in self.by_unit[self.u]:
            if l['suite']['component_type'] == 'Vocabulary':
                continue
            used += [x for _, items, _ in l['sections'] for x in items] + l['key']
            used += [t['prompt'] + ' ' + t['answer_key'] for t in l['suite']['tests']]
        spans = ' | '.join(span.lower() for line in used for span in re.findall(r'«([^»]*)»', line))
        for w in ('buat', 'panggil', 'cuci', 'tuan rumah', 'mari', 'ibu', 'adik'):
            self.assertRegex(spans, r'(?<![a-z])' + w + r'(?![a-z])', w)
        self.assertIn('Mari makan', spans.replace('mari makan', 'Mari makan'))
        tests = self.comp('Test')['suite']['tests']
        tagged = {w for t in tests for w in t['word_ids']}
        for lid in ('L-1076', 'L-1082'):
            self.assertIn(self.ledger.word_id(self.ledger.row(lid)), tagged, lid)
        # «jom» is the spoken equivalent of «mari», and is labelled.
        self.assertIn('«Jom makan»', ' '.join(self.cfg['festival_notes']['en']))

    def test_step5i_signs_and_notices_in_use(self):
        """Sam, 12 Nov 2026: «pesta», «perhatian», «hingga», «tolak», «tarik» are core and used naturally: door signs, a
        PERHATIAN notice, «Ditutup hingga …» and «Selamat Pesta Kaamatan»."""
        used = []
        for l in self.by_unit[self.u]:
            if l['suite']['component_type'] == 'Vocabulary':
                continue
            used += [x for _, items, _ in l['sections'] for x in items] + l['key']
            used += [t['prompt'] + ' ' + t['answer_key'] for t in l['suite']['tests']]
        text = ' | '.join(used)
        spans = ' | '.join(span for line in used for span in re.findall(r'«([^»]*)»', line))
        for sign in ('«TOLAK»', '«TARIK»', '«PERHATIAN: Bilik mesyuarat ditutup hingga hari Isnin.»', 'Ditutup hingga hari Isnin.',
                     'Dibuka Isnin hingga Jumaat', 'Selamat Pesta Kaamatan'):
            self.assertIn(sign, text, sign)
        for w in ('pesta', 'perhatian', 'hingga', 'tolak', 'tarik'):
            self.assertRegex(spans.lower(), r'(?<![a-z])' + w + r'(?![a-z])', w)
        # The test reading item asks about «hingga» and is tagged with the notice words.
        tests = self.comp('Test')['suite']['tests']
        tagged = {w for t in tests for w in t['word_ids']}
        for lid in ('L-1085', 'L-1086'):
            self.assertIn(self.ledger.word_id(self.ledger.row(lid)), tagged, lid)
        # «hingga» is the written word, «sampai» the spoken one, and the pattern page says so.
        pat = ' '.join(self.lines(self.comp('Pattern and grammar')))
        self.assertIn('in speech say «sampai»', pat)
        # No other word is built from «perhatian» (the per-…-an pattern is not taught).
        self.assertNotRegex(text.lower(), r'memperhatikan|perhatikan|diperhatikan')

    def test_idioms_are_recognition_only(self):
        """Sam: the idioms are for recognition; list them with plain meanings and do not drill them as core."""
        idioms = [self.ledger.row(lid)['Malay'] for lid in ms_c09.SIMPULAN]
        self.assertEqual(len(idioms), 14)
        for typ in ('Drill', 'Task', 'Listening', 'Model conversation', 'Reading and writing', 'Test', 'Pattern and grammar'):
            for l in self.by_unit[self.u]:
                if l['suite']['component_type'] != typ:
                    continue
                text = ' '.join([x for _, items, _ in l['sections'] for x in items] + l['key']
                                + [t['prompt'] + ' ' + t['answer_key'] for t in l['suite']['tests']]).lower()
                for idiom in idioms:
                    self.assertNotIn(idiom.lower(), text, (typ, idiom))
        notes = ' '.join(self.cfg['teacher_notes'])
        self.assertIn('do not drill them', notes)
        v = self.lines(self.comp('Vocabulary'))
        for lid in ms_c09.SIMPULAN:
            self.assertIn('[' + lid + ']', ' '.join(v))
        for t in self.comp('Test')['suite']['tests']:
            if t['sub_type'] == 'words':
                for lid in ms_c09.SIMPULAN + ms_c09.RUMAH_TERBUKA:
                    self.assertNotIn(self.ledger.word_id(self.ledger.row(lid)), t['word_ids'])

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
                  '«berapa» with a counter', '«siapa» with «oleh»', '«Kek ini dibuat oleh siapa?»'):
            self.assertIn(w, full, w)
        key = ' '.join(qset['key'])
        for q in ('«Kek ini dibuat oleh siapa?»', '«Nasi lemak ini dibeli di mana?»', '«Surat itu dihantar ke mana?»',
                  '«Surat itu ditulis oleh siapa?»', '«Berapa cawan teh?»'):
            self.assertIn(q, key, q)
        self.assertEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(qset)), 18)
        for i in range(1, 19):
            self.assertRegex(key, rf'(^|\s){i} «', i)
        # «siapa» + «oleh» practice is in the question and answer drill and the choice drill.
        qa = ' '.join(self.lines(self.comp('Drill', 'question and answer')))
        self.assertIn('Kek ini dibuat oleh siapa?', qa)
        choice = ' '.join(self.lines(self.comp('Drill', 'question-word choice')))
        self.assertIn('dibuat oleh ___?', choice)
        ck = ' '.join(self.comp('Drill', 'question-word choice')['key'])
        for w in ('«Siapa»', '«Di mana»', '«Ke mana»', '«Berapa»', '«Bila»', '«Kenapa»', '«Yang mana»', '«Bagaimana»'):
            self.assertIn(w, ck, w)

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
        self.assertTrue(120 <= malay_words([f'«{s}»' for _, s in cfg['listening']]) <= 250, malay_words([f'«{s}»' for _, s in cfg['listening']]))
        lis = self.comp('Listening')
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(lis, 'While')), 6)
        self.assertEqual(len(cfg['listen_questions']), len(cfg['listen_answers']))
        self.assertTrue(self.lines(lis, 'Before') and self.lines(lis, 'After'))
        rw = self.comp('Reading and writing')
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(rw, 'Questions')), 5)
        self.assertEqual(len(cfg['read_questions']), len(cfg['read_answers']))
        self.assertTrue(any(x.startswith('Model writing') for x in rw['key']))
        self.assertEqual(rw['suite']['sub_type'], 'notice')
        task = self.comp('Task')
        for part in ('Role card A', 'Role card B', 'Change of plan', 'Success criteria'):
            self.assertIn(part, ' '.join(n for n, _, _ in task['sections']))
        words = english_words(self.lines(self.comp('Culture note', slug='culture-note'), 'English'))
        self.assertTrue(150 <= words <= 300, words)
        self.assertEqual(len(cfg['culture']), len(cfg['culture_ja']))
        self.assertIn('neutral', ' '.join(cfg['culture']))
        self.assertIn('受身', ' '.join(cfg['culture']))
        # The reading text is a fictional notice board.
        self.assertIn('Fictional notice board', ' '.join(cfg['reading']))

    def test_festival_notes(self):
        """Sam, 12 Nov 2026: a general «rumah terbuka» scene, with a short culture note for each festival. Festival-specific words
        sit inside that festival's note; every note is culture, not a religious lesson; the sources are named."""
        fn = self.cfg['festival_notes']
        comp = self.comp('Culture note', slug='culture-open-houses')
        self.assertEqual(comp['suite']['sub_type'], 'scene')
        en = fn['en']
        words = english_words(self.lines(comp, 'English'))
        self.assertTrue(150 <= words <= 300, words)
        self.assertEqual(len(fn['en']), len(fn['ja']))
        self.assertEqual(len(en), 6)
        intro, raya, cny, deepavali, xmas, borneo = en
        self.assertIn('rumah terbuka', intro)
        self.assertIn('culture, not a lesson in belief', intro)
        # The festival-specific words sit in their own note.
        for w in ('maaf zahir dan batin', 'duit raya', 'ketupat', 'pelita'):
            self.assertIn(w, raya.lower())
            for other in (intro, cny, deepavali, xmas, borneo):
                self.assertNotIn(w, other.lower())
        self.assertIn('Tahun Baru Cina', cny)
        self.assertIn('angpau', cny)
        self.assertIn('Deepavali', deepavali)
        self.assertIn('Krismas', xmas)
        self.assertIn('Gawai', borneo)
        self.assertIn('Kaamatan', borneo)
        self.assertIn('not Malay', borneo)
        # Greetings are built from ledger words; there are no new greeting rows and no faith-specific greeting.
        for g in ('Selamat Hari Raya', '«Selamat Tahun Baru Cina» (no «Hari»)', 'Selamat Hari Deepavali', 'Selamat Hari Krismas',
                  'Selamat Hari Gawai', '«Selamat Pesta Kaamatan»'):
            self.assertIn(g, intro)
        # Step 5i: «Selamat Pesta Kaamatan» is sourced (Bernama, 30 May 2026); the formal form is only a quotation.
        self.assertIn('‹Selamat Menyambut Pesta Kaamatan›', intro)
        self.assertIn('Bernama, 30 May 2026', intro)
        self.assertNotIn('not yet sourced', ' '.join(self.all_lines()))
        self.assertNotIn('‹Selamat Pesta Kaamatan›', ' '.join(self.all_lines()))
        self.assertNotIn('Selamat Hari Tahun', ' '.join(self.all_lines()))
        self.assertNotIn('Selamat Hari Kaamatan', ' '.join(self.all_lines()))
        # Sam, 12 Nov 2026: both spellings, Labuan, the Gawai dates, «angpau» as the Malay spelling, one Christmas sentence.
        for w in ('«Tahun Baru Cina» (Chinese New Year) is the everyday name', '«Tahun Baharu Cina» is the official one'):
            self.assertIn(w, cny)
        self.assertIn('"ang pow"', cny)
        self.assertIn('Sabah and Labuan, 30 and 31 May', borneo)
        self.assertIn('gazetted as a holiday on 25 September 1964 and first celebrated on 1 June 1965', borneo)
        self.assertEqual(xmas.count('.'), 1)
        text = ' '.join(self.all_lines()).lower()
        self.assertNotRegex(text, r'assalam|waalaikum|kotobian|gayu guru|insya|alhamdulillah|bismillah|halal|haram|puasa|solat|sembahyang|azan|khutbah|ibadat|doa\b')
        # Sources are named, honestly.
        src = fn['sources']
        for name in ('EMGS Connect', 'Arab News', 'Malay Mail', 'The Borneo Post', 'search summaries only', 'New Straits Times',
                     'Free Malaysia Today', 'officeholidays.com', 'ecentral.my', 'Bernama radio news, 30 May 2026',
                     'Wikipedia pages could not be fetched', 'no source retrieved', 'L-1070 to L-1075'):
            self.assertIn(name, src, name)
        # No figure, price or percentage is stated about the real country.
        self.assertNotRegex(' '.join(en), r'\d+\.?\d*\s*(%|per cent|RM|ringgit)')
        # The scene is in the vocabulary as one recognition group of 19, and the plan sends the festival notes to Block E.
        plan = ' '.join(self.lines(self.comp('Teaching plan')))
        self.assertIn('Culture note · Open houses', plan)
        self.assertIn('general «rumah terbuka» scene', ' '.join(self.cfg['teacher_notes']))

    def test_japanese_has_no_leftover_english(self):
        """Japanese cells are full translations: Latin letters appear only inside marked Malay, ids or product names."""
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Dunia|Sedia Kelas|Tanya Cikgu|Susun Ayat|Rumah terbuka Hari Raya|Rumah terbuka|Simpulan bahasa harian|UTC|RM')
        cfg = self.cfg
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']] + cfg['festival_notes']['ja']
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
        self.assertIn('Sedia Kelas c09', body)
        self.assertIn('0–5', body)
        self.assertIn('stage review and the A1 test', body)
        self.assertFalse(any(l['suite']['block'] == 'Skills' for l in self.by_unit[self.u]))

    def test_chapter9_malay_rules(self):
        label = re.compile(r'spoken|speech|話し言葉|口語', re.I)
        everything = self.by_unit[self.u] + self.by_unit.get('ms-c09-fast', [])
        for l in everything:
            lines = [x for _, items, _ in l['sections'] for x in items] + l['key']
            for line in lines:
                for span in re.findall(r'«([^»]*)»', line):
                    words = re.findall(r'[a-z]+', span.lower())
                    for w in ('toko', 'bis', 'mobil', 'toilet', 'koran', 'apel', 'kantong', 'dilarang parkir'):
                        self.assertNotIn(w, words, line)
                    for w in words:
                        if w in ('nak', 'tapi', 'sikit', 'dah', 'tak', 'senang', 'saja', 'tapau', 'jom'):
                            self.assertRegex(line, label, (l['title'], line))

    def test_sam_rules_and_scene_facts(self):
        everything = ' '.join(self.all_lines())
        self.assertIn('fictional', everything)
        notes = self.comp('Culture note', slug='culture-note')
        sources = ' '.join(self.lines(notes) + notes['key'])
        for name in ('ms-c09-004', '-024', '-029', 'f06', 'fictional'):
            self.assertIn(name, sources, name)
        culture = ' '.join(self.lines(notes, 'English'))
        self.assertNotRegex(culture, r'\d+\.?\d*\s*(%|per cent|RM|ringgit)')
        # Etymology comes only from Kata-Kata card notes: «jamuan» ← ‹jamu›.
        self.assertIn('‹jamu›', culture)
        row = self.ledger.rows
        for lid in ms_c09.CORE:
            self.assertNotIn('etymology', row[lid]["Sam's notes"].lower())

    def test_openers_have_no_leftover_english(self):
        opener = next(l for l in self.by_unit[self.u] if l['suite']['component_type'] == 'Opener')
        for line in self.lines(opener):
            if line.startswith('After class'):
                ja = line.split(' / ')[-1]
                self.assertNotRegex(ja, r'\band\b', ja)
        self.assertIn('Sedia Kelas c09 (12 cards, frames ms-c09-f01 and ms-c09-f02)', ' '.join(self.lines(opener)))
        sk = json.loads((ROOT / 'curriculum/reference/katakata/c09.json').read_text())['sedia_kelas']
        self.assertEqual(len(sk['cards']), 12)
        self.assertEqual(sk['frames'], ['ms-c09-f01', 'ms-c09-f02'])

    def test_fast_pack(self):
        self.assertIn('ms-c09-fast', self.by_unit)
        l = self.by_unit['ms-c09-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertTrue(15 <= len(core) <= 20)
        self.assertEqual(len(fast.C9_WORDS), len(set(fast.C9_WORDS)))
        self.assertTrue(set(fast.C9_WORDS) <= set(self.cfg['core']))
        labels = ' '.join(n for n, _, _ in l['sections'])
        for part in ('Can-do', 'Core words', 'Key patterns', 'Model conversation', 'Task', 'Self-check', 'Self-study'):
            self.assertIn(part, labels)
        patterns = [x for x in self.lines(l, 'Key patterns') if re.match(r'^\d · ', x)]
        self.assertEqual(len(patterns), 5)
        for line in patterns:
            self.assertEqual(line.split('e.g.')[1].count(' / '), 1, line)
        self.assertTrue(10 <= len(self.lines(l, 'Model conversation')) <= 16)
        n_check = sum(x.startswith('☐') for x in self.lines(l, 'Self-check'))
        self.assertEqual(n_check, 5)
        self.assertTrue(all(f'{i} «' in l['key'][0] for i in range(1, n_check + 1)))
        page = {x['title']: x for x in bank()}[l['title']]
        count = len(page['pages']) - 3 - page.get('key_pages', 1)
        self.assertTrue(2 <= count <= 4, count)
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch9 = next(c for c in chapters if c['title'].startswith('Chapter 9'))
        self.assertIn(l['title'], ch9['fast_items'])
        guide = ' '.join(self.lines(l, 'Self-study'))
        self.assertIn('Sedia Kelas c09', guide)
        self.assertIn('Rumah terbuka', guide)
        self.assertIn('Simpulan bahasa harian', guide)
        self.assertIn('never drilled', guide)
        self.assertIn('ms-c09-001 to ms-c09-030', guide)
        # The fast pack keeps the same di- rule: only the two productive examples, both from ledger verbs.
        body = ' '.join(self.lines(l, 'Key patterns'))
        self.assertIn('«digoreng»', body)
        self.assertIn('Pinggan saya bawa ke dapur', body)

    def test_catalogue_and_registration(self):
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch9 = next(c for c in chapters if c['title'].startswith('Chapter 9'))
        self.assertEqual([u['label'] for u in ch9['units']], ['9'])
        self.assertEqual(ch9['status'], 'Step 5g chapter 9 suite · draft for pilot')
        catalogue = make_catalogue(bank(), chapters)
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('check_unit') == self.u]
        self.assertTrue(mine)
        self.assertTrue(all(c['chapter_id'] == 'ms-c09' and c['review_status'] == 'draft' for c in mine))
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 30)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'] in (self.u, 'ms-c09-fast')])
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for unit in (self.u, 'ms-c09-fast'):
            self.assertIn(unit, reauthored)
        # Chapter 8 is untouched by registration.
        self.assertIn('ms-c08', reauthored)


if __name__ == '__main__':
    unittest.main()
