"""Stage 2 build step 4: chapter 17 (unit 17, standard and spoken Malay, «lah» and «kan», invitations and polite refusals) and the chapter 17 fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (24 core rows placed "Ch17 (unit 17)", no recognition row), every core word used
outside the vocabulary list, the standard form always before the spoken form and the spoken form labelled, «lah» and «kan» as recognition only (never in a key or a task), «tidak boleh tahan»
against «boleh tahan», «belanja» against «berbelanja», «sudi» for the other person, «dari» for places and «daripada» for people and offices, the -kan rule, «kami» against «kita»,
alignment with Kata-Kata c17 (frames f01 to f06, all 20 scenario lines word for word, no turn joined across a scene change), the charter section 6 and 14 minimums and the registration.
Copied from tests/test_stage2_ch16.py.
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c17, fast
from catalogue import make_catalogue
from language_checks import placed_chapter

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
UNITS = ('ms-c17',)
# Marked words that look like ber- or meN- forms but are roots or Stage 1 whole words.
LOOKALIKE = {'berapa', 'bersih', 'besar', 'berat', 'belum', 'belajar', 'bekas', 'beli', 'bengkak', 'beg', 'bekerja', 'berehat',
             'merah', 'meter', 'mengapa', 'menu', 'melayu', 'mesyuarat', 'mereka', 'mesej', 'mesti', 'mei', 'meja', 'merokok', 'menang',
             'memang', 'mewah', 'menit', 'mentah', 'mereka', 'mel'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch17_rows(rows):
    """Core rows the ledger places in unit 17 (not the recognition rows)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(r'Ch17 \(unit 17\)(?:;|$)', r['Kata-Kata place'])}


NAMES = {w.lower() for n in json.loads((ROOT / 'curriculum/malay-proper-nouns.json').read_text())['names'] for w in n.split()}


def spans(lines):
    return [s for line in lines for s in re.findall(r'«([^»]*)»', line)]


class Chapter17(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.pack = json.loads((ROOT / 'curriculum/reference/katakata/c17.json').read_text())

    def comp(self, u, typ, sub=None, slug=None):
        found = [l for l in self.by_unit[u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {u} {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=UNITS + ('ms-c17-fast',), skip_vocab=False):
        out = []
        for u in units:
            for l in self.by_unit.get(u, []):
                if skip_vocab and l['suite']['component_type'] == 'Vocabulary':
                    continue
                out += [x for _, items, _ in l['sections'] for x in items] + l['key']
                for t in l['suite']['tests']:
                    out += [t['prompt'], t['answer_key']]
        return out

    def words(self, lines):
        return [w for s in spans(lines) for w in re.findall(r'[a-z]+(?:-[a-z]+)*', s.lower())]

    def pupil_malay(self):
        """Malay lines a learner reads or says: dialogues, listening, drills and keys, pattern examples, reading, writing model, task key and the fast-pack conversation."""
        cfg = ms_c17.CFG
        out = [s for _, s in cfg['dialogue'] + cfg['scene_e']['lines'] + cfg['variant'] + cfg['listening']]
        for v in cfg['drills'].values():
            out += v if isinstance(v, list) else [v]
        for v in cfg['drill_keys'].values():
            out += v
        out += [ex for p in cfg['patterns'] for ex in p[2]]
        out += cfg['reading'] + [cfg['write_model'], cfg['task_key']] + cfg['markers']['items'] + cfg['markers']['key']
        out += self.lines(self.by_unit['ms-c17-fast'][0], 'Model conversation')
        return out

    def test_ledger_partition(self):
        rows = self.ledger.rows
        cfg = ms_c17.CFG
        self.assertEqual(len(cfg['core']), len(set(cfg['core'])))
        self.assertEqual(set(cfg['core']), ch17_rows(rows))
        self.assertEqual(len(cfg['core']), 26)  # 24 + L-1302, L-1303 (14 Nov 2026)
        for lid in ('L-1266', 'L-1267', 'L-0690', 'L-0703', 'L-0717', 'L-1254', 'L-1253'):  # takpe and tidak boleh tahan are core words
            self.assertIn(lid, cfg['core'])
        self.assertEqual([lid for _, ids in cfg['core_groups'] for lid in ids], cfg['core'])
        for _, ids in cfg['revision']:
            for lid in ids:
                self.assertLessEqual(placed_chapter(rows[lid]['Kata-Kata place']), 16, lid)
                self.assertNotIn(lid, cfg['core'])
        stage2 = {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
                  and re.match(r'Ch1[0-7] \(unit \w+\)(?:;|$)', r['Kata-Kata place'])}
        self.assertEqual(len(stage2), 271)  # 240 + the 31 words approved on 13 and 14 Nov 2026 (L-1273 to L-1303); the six practice-pool rows are not core
        self.assertFalse([lid for lid, r in rows.items() if re.match(r'Ch17 \(unit 17, recognition', r['Kata-Kata place'])])
        self.assertEqual(cfg['recognition'], [])
        cards = {c['id'] for c in self.pack['cards']}
        for lid in ms_c17.CORE:
            self.assertIn(rows[lid]['Kata-Kata (card IDs)'].split(',')[0].strip(), cards, lid)  # the class card is listed first; a Dunia twin may follow
        self.assertEqual(len(cards), 26)  # 24 core + 2 new (L-1302, L-1303)

    def test_every_core_word_is_used(self):
        """All 26 chapter 17 core words appear outside the vocabulary list (including «takpe», «tidak boleh tahan», «lah» and «kan»)."""
        text = ' | '.join(s.lower() for s in spans(self.all_lines(('ms-c17',), skip_vocab=True)))
        for lid in ms_c17.CFG['core']:
            form = self.ledger.row(lid)['Malay'].lower().split(' / ')[0]
            self.assertRegex(text, r'(?<![a-z-])' + re.escape(form) + r'(?![a-z-])', (lid, form))

    def test_revision_words_really_return(self):
        text = ' '.join(' '.join(re.findall(r'[a-z]+(?:-[a-z]+)*', s.lower())) for s in spans(self.all_lines(('ms-c17',), skip_vocab=True)))
        for _, ids in ms_c17.CFG['revision']:
            for lid in ids:
                forms = [re.sub(r'\([^)]*\)', '', f).strip().lower() for f in self.ledger.row(lid)['Malay'].split('/')]
                self.assertTrue(any(re.search(r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', text) for f in forms), (lid, forms))


    def test_components_patterns_and_minimums(self):
        required = {'Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                    'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan'}
        u = 'ms-c17'
        cfg = ms_c17.CFG
        self.assertTrue(required <= {l['suite']['component_type'] for l in self.by_unit[u]}, u)
        for l in self.by_unit[u]:
            self.assertIn('Malay · A2', l['header'])
            self.assertIn('Japanese awaiting native review', l['header'])
            self.assertEqual(l['level'], 'A2')
        v = self.comp(u, 'Vocabulary')
        entries = [x for x in self.lines(v) if re.search(r'\[L-\d{4}\]$', x)]
        examples = [x for x in self.lines(v) if x.strip().startswith('e.g.')]
        n = len(cfg['core']) + sum(len(x) for _, x in cfg['recognition']) + sum(len(x) for _, x in cfg['revision'])
        self.assertEqual((len(entries), len(examples)), (n, n), u)
        pat = self.comp(u, 'Pattern and grammar')
        self.assertTrue(3 <= len(pat['sections']) <= 5)
        self.assertEqual(len(pat['sections']), 5)
        for title, lines, _ in pat['sections']:
            self.assertTrue(4 <= sum(bool(re.match(r'\d+\. A:', x)) for x in lines) <= 6, title)
            for label in ('Explanation:', '説明：', 'Japanese helps or misleads:', '日本語との比較：'):
                self.assertTrue(any(x.startswith(label) for x in lines), (title, label))
        total = 0
        for sub in ('repeat', 'substitute', 'transform', 'question and answer', 'question-word choice'):
            l = self.comp(u, 'Drill', sub)
            n = sum(bool(NUMBERED.match(x)) for x in self.lines(l))
            self.assertGreaterEqual(n, 6, (u, sub))
            total += n
            if sub != 'repeat':
                key = ' '.join(l['key'])
                for i in range(1, n + 1):
                    self.assertRegex(key, rf'(^|\s){i} «', (u, sub, i))
        self.assertGreaterEqual(total, 30)
        self.assertGreaterEqual(sum(x.startswith('Dialogue ') for x in self.lines(self.comp(u, 'Drill', 'free'))), 3)
        qset = self.comp(u, 'Drill', 'question-word set')
        full = ' '.join(self.lines(qset))
        for w in ('«apa»', '«siapa»', '«di mana»', '«Adakah»', '«Bolehkah»', '«berapa»', '«bila»', '«pukul berapa»', '«hari apa»',
                  '«bagaimana»', '«macam mana»', '«kenapa»', '«yang mana»', '«ke mana»', '«dari mana»', '«berapa jauh»',
                  '«berapa lama»', '«siapa» with «oleh»', 'Chapters 1 to 17', 'Chapter 17 adds no new question word'):
            self.assertIn(w, full, (u, w))
        self.assertEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(qset)), 18)
        for i in range(1, 19):
            self.assertRegex(' '.join(qset['key']), rf'(^|\s){i} «', (u, i))
        m = self.comp(u, 'Drill', 'markers')
        for w in ('«sudah»', '«belum»', '«masih»', '«akan»', '«baru»'):
            self.assertIn(w, ' '.join(self.lines(m)), (u, w))
        for i in range(1, 9):
            self.assertRegex(' '.join(m['key']), rf'(^|\s){i} «', (u, i))
        d = self.comp(u, 'Model conversation')
        self.assertTrue(10 <= len(self.lines(d, 'Model ·')) <= 16)
        self.assertTrue(any('____' in x for x in self.lines(d, 'Gapped')))
        self.assertEqual(len(self.lines(d, 'Changed facts')), len(cfg['variant']))
        words = malay_words([f'«{s}»' for _, s in cfg['listening']])
        self.assertTrue(120 <= words <= 250, (u, words))
        lis = self.comp(u, 'Listening')
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(lis, 'While')), 6)
        self.assertEqual(len(cfg['listen_questions']), len(cfg['listen_answers']))
        rw = self.comp(u, 'Reading and writing', slug='reading-writing')
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(rw, 'Questions')), 5)
        self.assertEqual(len(cfg['read_questions']), len(cfg['read_answers']))
        task = self.comp(u, 'Task')
        for part in ('Role card A', 'Role card B', 'Change of plan', 'Success criteria'):
            self.assertIn(part, ' '.join(n for n, _, _ in task['sections']))
        cw = english_words(cfg['culture'])
        self.assertTrue(150 <= cw <= 300, (u, cw))
        self.assertEqual(len(cfg['culture']), len(cfg['culture_ja']))
        test = self.comp(u, 'Test')
        tests = test['suite']['tests']
        scored = [t for t in tests if t['sub_type'] != 'speaking']
        self.assertTrue(15 <= len(scored) <= 20)
        self.assertEqual(sum(t['sub_type'] == 'speaking' for t in tests), 1)
        self.assertTrue({'listening', 'reading', 'words', 'grammar'} <= {t['sub_type'] for t in tests})
        self.assertTrue(all(t['grammar_points'] and t['word_ids'] for t in tests))
        core_cards = {self.ledger.word_id(self.ledger.row(lid)) for lid in cfg['core']}
        for t in tests:
            if t['sub_type'] == 'words':
                self.assertTrue(set(t['word_ids']) <= core_cards, t['id'])
        plan = ' '.join(self.lines(self.comp(u, 'Teaching plan')))
        for w in ('Block E · Scene transfer', 'Sedia Kelas c17', 'not yet tagged by chapter', '0–5'):
            self.assertIn(w, plan + ' '.join(n for n, _, _ in self.comp(u, 'Teaching plan')['sections']), (u, w))
        # «lah» and «kan» (the particles) are never in an answer key.
        # (the teacher-read listening script is recognition input, not a required answer: its lines start with a speaker label)
        script = tuple(f'{sp}: ' for sp, _ in cfg['listening'])
        keys = re.sub(r'‹[^›]*›', '', ' '.join(x for l in self.by_unit[u] for x in l['key'] if not x.startswith(script))).lower()  # a key that names a particle quotes it as a ‹…› mention
        self.assertNotRegex(keys, r'(?<![a-z-])(lah|kan)(?![a-z])')

    # ---- chapter 17 specific -------------------------------------------------------------------------------------------
    PAIRS = [('L-1261', 'L-1266'), ('L-1267', 'L-0690'), ('L-1255', 'L-0703')]

    def test_standard_first_and_spoken_labelled(self):
        """Standard first: in the vocabulary list every spoken form comes after its standard form and carries the label "spoken"."""
        entries = [x for x in self.lines(self.comp('ms-c17', 'Vocabulary')) if re.search(r'\[L-\d{4}\]$', x)]
        order = {re.search(r'\[(L-\d{4})\]$', x).group(1): (i, x) for i, x in enumerate(entries)}
        for std, spoken in self.PAIRS:
            self.assertLess(order[std][0], order[spoken][0], (std, spoken))
        for lid in ('L-1266', 'L-0690', 'L-0703', 'L-1252', 'L-1263', 'L-1264', 'L-1262'):
            self.assertIn('spoken', order[lid][1], lid)
        self.assertIn('«takpe» / «tak apa»', order['L-1266'][1])
        self.assertIn('standard «ini»', ' '.join(ms_c17.VOCAB_OPTS['L-1263']['en'].split('for the ')))
        notes = ' '.join(ms_c17.CFG['teacher_notes'])
        for w in ('Standard first, always', '«tidak mengapa» / «takpe» or «tak apa»', '«tidak boleh tahan» / «tak tahan»', '«seperti itu» / «macam tu»', '«di» / «kat»', '«ini» / «ni»',
                  '«itu» / «tu»', '«setuju» / «set»', '«jom» against «mari»', 'understand the spoken forms, may use them with friends and colleagues, and write the standard forms'):
            self.assertIn(w, notes, w)
        # the standard forms are written in the pattern for writing, and the spoken pattern 5 is labelled spoken
        self.assertIn('spoken', ms_c17.P[4][1] + ms_c17.P[4][3])
        self.assertIn('Mari makan di kafe ini.', ' '.join(ms_c17.P[4][3:]))

    def test_four_teacher_notes_of_the_brief(self):
        notes = ' '.join(ms_c17.CFG['teacher_notes'])
        for w in ('When to use the spoken forms and when not', 'friends, with colleagues you know and at the mamak',
                  'emails, forms, notices or meetings with clients', 'Japanese learners over-use «lah»',
                  'Polite refusal in Malaysia against Japanese ちょっと…', 'soften', 'give a reason', 'offer another time',
                  '«belanja» means to treat someone (to pay for them), not to spend money', '«berbelanja»',
                  '«tidak boleh tahan» against «boleh tahan»', 'not bad'):
            self.assertIn(w, notes, w)
        self.assertIn('Saya tak nak pedas.', notes)
        self.assertIn('Saya tak suka pedas.', notes)
        # culture note: the same four points, one general knowledge sentence
        cult = ' '.join(ms_c17.CULTURE)
        for w in ('Japanese ちょっと…', '«Lain kali, ya?»', '«belanja» means to treat someone, not to spend money', 'emails, forms, notices and meetings with clients', 'never need to say them'):
            self.assertIn(w, cult, w)

    def test_particles_are_recognition_only(self):
        """«lah» (joined in writing) and «kan» are never required: not in any key, task card, test answer or speaking key."""
        cfg = ms_c17.CFG
        pat = re.compile(r'(?<![a-z-])(?:lah|kan)(?![a-z])|[a-z]+lah(?![a-z])', re.I)
        required = [cfg['task_key'], cfg['speaking_key'], *cfg['role_a'], *cfg['role_b'], *cfg['change'], *cfg['success'], *cfg['write_model'].split('. ')]
        required += [a for _, a, _ in cfg['grammar_quiz']] + [a for _, a, _ in cfg['reading_quiz']] + [a for _, a, _ in cfg['test_listen']] + cfg['short_keys']
        required += sum(cfg['drill_keys'].values(), []) + cfg['markers']['key'] + cfg['question_keys']
        for line in required:
            self.assertIsNone(pat.search(' '.join(re.findall(r'«([^»]*)»', line)) or ''), line)
        test = self.comp('ms-c17', 'Test')
        for t in test['suite']['tests']:
            self.assertIsNone(pat.search(t['answer_key']), t['id'])
        notes = ' '.join(cfg['teacher_notes'])
        for w in ('recognition only', 'no key, task or test requires them', 'in writing it joins the word', 'is not the suffix ‹-kan› (chapter 12)', 'a sentence without «lah» is correct', 'or ね'):
            self.assertIn(w, notes, w)
        # taught as recognition: they are heard in the model and the listening, and written joined («Takpelah.», «Bolehlah.»)
        text = ' '.join(s for _, s in cfg['dialogue'] + cfg['listening'])
        for w in ('Takpelah.', 'Bolehlah.', ', kan?'):
            self.assertIn(w, text, w)
        for lid in ('L-1254', 'L-1253'):
            self.assertIn('Recognition only', ms_c17.VOCAB_OPTS[lid]['en'])
        self.assertIn('Takpelah.', ms_c17.EXAMPLES['L-1254'])
        # no separately written «lah» after a word in the pupil-facing Malay (it is joined)
        self.assertNotRegex(' '.join(s for _, s in cfg['dialogue'] + cfg['scene_e']['lines'] + cfg['variant'] + cfg['listening']), r'(?<![‘a-z])\s lah\b|[a-z] lah[ .,!?]')

    def test_tahan_belanja_sudi(self):
        opts = ms_c17.VOCAB_OPTS
        self.assertIn('not the same as «boleh tahan» (not bad, chapter 5)', opts['L-1267']['en'])
        self.assertIn('«Saya tak nak pedas.»', opts['L-0690']['en'] + ' ' + ms_c17.EXAMPLES['L-0030'])
        self.assertIn('«Saya tak suka pedas.»', opts['L-0690']['en'])
        self.assertIn('not «berbelanja»', opts['L-0717']['en'])
        self.assertIn('never about yourself', opts['L-0828']['en'])
        text = ' '.join(self.pupil_malay())
        self.assertNotRegex(text, r'(?<![a-z])[Ss]aya sudi')
        self.assertNotRegex(text, r'(?<!ber)belanja di (?:pasar|kedai)')
        self.assertNotRegex(text, r'(?<!tidak )(?<!tak )(?<![a-z-])boleh tahan')
        self.assertNotRegex(text, r'Saya tak tahan[^.]*Saya tidak boleh tahan')

    def test_kan_rule_noun_objects_and_dari(self):
        """«dari» for places, «daripada» for people and offices; no meN-…-kan form; «kami» does not include the listener, «kita» does."""
        kan = r'(?:tangguhkan|batalkan|simpankan|hantarkan|bawakan|letakkan|elakkan|hubungi|baiki)'
        bad = re.compile(rf'\b(?:sudah|sedang|belum|akan|baru|masih)\s+{kan}\b', re.I)
        for sp in spans(self.all_lines()):
            self.assertIsNone(bad.search(sp), sp)
        pupil = ' '.join(line.lower() for line in self.pupil_malay())
        for gone in ('menyimpankan', 'menghantarkan', 'ditangguhkan', 'dibatalkan', 'menangguhkan', 'membatalkan', 'tangguhkan', 'batalkan'):
            self.assertNotRegex(pupil, r'(?<![a-z])' + gone + r'(?![a-z])')
        text = ' '.join(self.all_lines())
        self.assertNotRegex(text, r'(?<![a-z])dari (?:doktor|kedai|bank|bos|syarikat|kawan|pengurus|Puan|Encik|Cik)')
        self.assertIn('jemputan daripada Puan Aini', text)
        self.assertNotRegex(text, r'jemputan dari ')
        self.assertIn('Saya tanya bos dulu.', ' '.join(s for _, s in ms_c17.CFG['dialogue']))  # Kata-Kata's everyday bare root
        notes = ' '.join(ms_c17.CFG['teacher_notes'])
        for w in ('«kami» against «kita» in invitations', '«kami» does not include the listener', '«kita» includes the listener', '«daripada» for people and offices'):
            self.assertIn(w, notes, w)
        self.assertIn('Sudikah puan makan dengan kami hari Jumaat?', ' '.join(ex for p in ms_c17.CFG['patterns'] for ex in p[2]))

    def test_katakata_alignment(self):
        """Same frames f01 to f06, same scene, every scenario line word for word (Kata-Kata's inner «…» of s13 and s15 shown as ‘…’), no turn joined across a scene change."""
        frames = {f['id']: f for f in self.pack['frames']}
        self.assertEqual(sorted(frames), [f'ms-c17-f0{n}' for n in range(1, 7)])
        self.assertEqual(ms_c17.CFG['pattern_ids'], [f'ms-c17-f0{n}' for n in range(1, 7)])
        text = ' '.join(self.all_lines(('ms-c17',)))
        for f in frames.values():
            self.assertIn(f['example'], text, f['id'])
        lines = self.pack['scenario']['lines']
        self.assertEqual(len(lines), 20)
        shown = [re.sub(r'«([^»]*)»', r'‘\1’', l['ms']) for l in lines]
        for line, sh in zip(lines, shown):
            self.assertIn(sh, text, line['id'])
        # Sam (13 Nov 2026): no join across a scene change: the model is s01 to s16, one line to a turn; the mamak scene s17 to s20 is the Block E dialogue.
        self.assertEqual([s for _, s in ms_c17.DIALOGUE], shown[:16])
        self.assertEqual([s for _, s in ms_c17.MAMAK], shown[16:])
        self.assertEqual(ms_c17.CFG['scene_e']['lines'], ms_c17.MAMAK)
        self.assertEqual(len(ms_c17.DIALOGUE), 16)
        self.assertEqual({sp for sp, _ in ms_c17.DIALOGUE + ms_c17.MAMAK}, {'Aini', 'Tanaka', 'Mei Ling'})
        plan = ' '.join(n + ' ' + ' '.join(items) for n, items, _ in self.comp('ms-c17', 'Teaching plan')['sections'])
        self.assertIn('ms-c17-s01 to ms-c17-s16', plan)
        self.assertIn('ms-c17-s17 to s20', plan)
        self.assertIn('Block E scene dialogue', plan)
        self.assertIn('Set!', plan)
        # the scenes of the brief
        model = ' '.join(s for _, s in ms_c17.DIALOGUE + ms_c17.MAMAK)
        for w in ('jemputan makan malam pejabat', 'Hari Jumaat, pukul tujuh', 'jom makan kat kafe ni! Saya belanja!', 'Saya tidak boleh tahan pedas', 'Takpelah.', 'kedai mamak', 'Set!'):
            self.assertIn(w, model, w)
        terms = {c['id']: c['term'] for c in self.pack['cards']}
        self.assertEqual((terms['ms-c17-014'], terms['ms-c17-022'], terms['ms-c17-023'], terms['ms-c17-024']), ('tidak mengapa', 'takpe / tak apa', 'tidak boleh tahan', 'tak tahan'))
        cites = ' '.join([ms_c17.CFG['culture_sources']] + ms_c17.CFG['teacher_notes'])
        for cid in ('014', '015', '016', '017', '022', '023', '024', '002', '003'):
            self.assertIn(cid, ms_c17.CFG['culture_sources'], cid)
        self.assertIn('ms-c17-s01 to s20', cites)

    def test_register_and_scope(self):
        pupil = ' '.join(line.lower() for line in self.pupil_malay())
        self.assertNotRegex(pupil, r'assalam|waalaikum|insya|alhamdulillah|bismillah')
        self.assertNotRegex(' '.join(spans(self.all_lines())).lower(), r'agama|tuhan|solat|puasa|haram|halal|raya|perayaan|rumah terbuka')
        cfg = ms_c17.CFG
        casual = ' '.join(s for _, s in cfg['dialogue'] + cfg['scene_e']['lines'] + cfg['variant'] + cfg['listening']).lower()
        for banned in ('ialah', 'keputusan', 'baiklah', 'begini', 'ikut', 'beritahu'):
            self.assertNotRegex(casual, r'(?<![a-z])' + banned + r'(?![a-z])', banned)
        # no medical reason for refusing food
        self.assertNotRegex(' '.join(spans(self.all_lines())).lower(), r'alergi|doktor|ubat|sakit')
        self.assertIn('do not ask for or discuss a medical reason', ' '.join(cfg['teacher_notes']))
        # the festival card of the Sedia Kelas list is not used, and a teacher note says so
        self.assertIn('teaches no festival and no faith-specific expression', ' '.join(cfg['teacher_notes']))

    def test_no_review_or_writing_block_and_mentions(self):
        """The plan gives chapter 17 no review or writing block (chapter 18 is the integrated review): none was built."""
        self.assertIsNone(ms_c17.CFG['extra'])
        self.assertFalse([l for l in self.by_unit['ms-c17'] if l['suite']['block'] == 'Skills'])
        mentions = json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']
        for w in ('cadang', 'sayang', 'malang'):
            self.assertIn(w, mentions, w)

    def test_openers(self):
        opener = self.comp('ms-c17', 'Opener')
        body = ' '.join(self.lines(opener))
        self.assertIn(f'Sedia Kelas c17 ({katakata_ref.sedia_count(17)} cards, frames ms-c17-f01 and ms-c17-f02)', body)
        self.assertIn(f'（カード{katakata_ref.sedia_count(17)}枚、文型 f01・f02）', body)
        self.assertIn('ms-c17-001 to ms-c17-026', body)

    def test_culture_note_general_knowledge_labelled(self):
        cult = ' '.join(ms_c17.CULTURE)
        self.assertEqual(len(re.findall(r'General knowledge, not a rule and not a checked fact', cult)), 1)
        self.assertNotRegex(cult, r'RM|\bringgit\b|\d')

    def test_japanese_has_no_leftover_english(self):
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Sedia Kelas|Tanya Cikgu|Susun Ayat|Dunia|\bber-|\bmeN-|\*[a-z]+')
        cfg = ms_c17.CFG
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
        cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
        cells += [cfg['role_a'][-1], cfg['role_b'][-1], cfg['change'][-1], cfg['markers']['bridge'][-1].split(' / ')[-1]]
        cells += [o['ja'] for o in cfg['vocab_opts'].values() if 'ja' in o]
        for ja in cells:
            self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
            self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_fast_pack(self):
        l = self.by_unit['ms-c17-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertEqual(len(core), 26)  # 24 + L-1302, L-1303
        self.assertEqual(set(fast.C17_WORDS), set(ms_c17.CORE))  # the fast pack holds every core word (Sam, 13 Nov)
        patterns = [x for x in self.lines(l, 'Key patterns') if re.match(r'^\d · ', x)]
        self.assertEqual(len(patterns), 5)
        for line in patterns:
            self.assertEqual(line.split('e.g.')[1].count(' / '), 1, line)
        self.assertTrue(10 <= len(self.lines(l, 'Model conversation')) <= 16)
        self.assertEqual(sum(x.startswith('☐') for x in self.lines(l, 'Self-check')), 5)
        self.assertTrue(all(f'{i} «' in l['key'][0] for i in range(1, 6)))
        page = {x['title']: x for x in bank()}[l['title']]
        count = len(page['pages']) - 3 - page.get('key_pages', 1)
        self.assertTrue(2 <= count <= 4, count)
        guide = ' '.join(self.lines(l, 'Self-study'))
        self.assertIn(f'all {katakata_ref.card_count(17)} Kata-Kata chapter 17 cards (ms-c17-001 to ms-c17-{katakata_ref.last_own_card(17):03}', guide)

    def test_registration_and_catalogue(self):
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in UNITS + ('ms-c17-fast',):
            self.assertIn(u, reauthored)
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 20)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'].startswith('ms-c17')])
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch = next(c for c in chapters if c['title'].startswith('Chapter 17'))
        self.assertEqual([u['label'] for u in ch['units']], ['17'])
        self.assertEqual((ch['level'], ch['sequence']), ('A2', 'stage2'))
        self.assertTrue(ch['fast_items'])
        self.assertFalse([c for c in chapters if c.get('sequence') == 'future'])
        catalogue = make_catalogue(bank(), chapters)
        c17 = next(c for c in catalogue['chapters'] if c['id'] == 'ms-c17')
        self.assertEqual((c17['level'], c17['stage_id']), ('A2', 'ms-stage2'))
        self.assertEqual([u['id'] for u in c17['units']], ['ms-c17'])
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('chapter_id') == 'ms-c17']
        self.assertTrue(mine and all(c['level'] == 'A2' for c in mine))
        self.assertFalse([b for b in catalogue['additional_blocks'] if '17' in b['id']])
        self.assertEqual(catalogue['future_chapters'], [])


if __name__ == '__main__':
    unittest.main()
