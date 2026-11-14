"""Stage 2 build step 4: chapter 14 (unit 14, reasons, conditions, purpose, contrast and sequence), the writing block after unit 14
and the chapter 14 fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (22 core rows placed
"Ch14 (unit 14)", no recognition row), every core word used outside the vocabulary list, the chapter 12 ‹-kan› rule kept («tangguhkan» and
«batalkan» only in «kita» sentences and requests), the written and everyday words side by side («jika» / «kalau», «apabila» / «bila», «namun» /
«tetapi», «oleh itu» / «jadi», «seterusnya» / «kemudian») with the spoken lines using the everyday ones, the casual turns free of ruling-style
words, «dari» for places and «daripada» for people and organisations, alignment with Kata-Kata c14 (frames f01 to f06, all 15 scenario lines,
card IDs), the charter section 6 and 14 minimums, the writing block after unit 14, «lah» and «kan» never in a key, and the registration of the
unit. Copied from tests/test_stage2_ch13.py.
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c14, fast
from catalogue import make_catalogue
from language_checks import placed_chapter

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
UNITS = ('ms-c14',)
# Marked words that look like ber- or meN- forms but are roots or Stage 1 whole words.
LOOKALIKE = {'berapa', 'bersih', 'besar', 'berat', 'belum', 'belajar', 'bekas', 'beli', 'bengkak', 'beg', 'bekerja', 'berehat',
             'merah', 'meter', 'mengapa', 'menu', 'melayu', 'mesyuarat', 'mereka', 'mesej', 'mesti', 'mei', 'meja', 'merokok', 'menang',
             'memang', 'mewah', 'menit', 'mentah', 'mereka', 'mel'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch14_rows(rows):
    """Core rows the ledger places in unit 14 (not the recognition rows)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(r'Ch14 \(unit 14\)(?:;|$)', r['Kata-Kata place'])}


NAMES = {w.lower() for n in json.loads((ROOT / 'curriculum/malay-proper-nouns.json').read_text())['names'] for w in n.split()}


def spans(lines):
    return [s for line in lines for s in re.findall(r'«([^»]*)»', line)]


class Chapter14(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.pack = json.loads((ROOT / 'curriculum/reference/katakata/c14.json').read_text())

    def comp(self, u, typ, sub=None, slug=None):
        found = [l for l in self.by_unit[u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {u} {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=UNITS + ('ms-c14-fast',), skip_vocab=False):
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
        cfg = ms_c14.CFG
        out = [s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']]
        for v in cfg['drills'].values():
            out += v if isinstance(v, list) else [v]
        for v in cfg['drill_keys'].values():
            out += v
        out += [ex for p in cfg['patterns'] for ex in p[2]]
        out += cfg['reading'] + [cfg['write_model'], cfg['task_key']] + cfg['markers']['items'] + cfg['markers']['key']
        out += self.lines(self.by_unit['ms-c14-fast'][0], 'Model conversation')
        return out

    def test_ledger_partition(self):
        rows = self.ledger.rows
        cfg = ms_c14.CFG
        self.assertEqual(len(cfg['core']), len(set(cfg['core'])))
        self.assertEqual(set(cfg['core']), ch14_rows(rows))
        self.assertEqual(len(cfg['core']), 29)  # 22 + L-1289 to L-1295 (14 Nov 2026)
        for lid in ('L-1269', 'L-1270', 'L-0641', 'L-0710'):
            self.assertIn(lid, cfg['core'])
        self.assertEqual([lid for _, ids in cfg['core_groups'] for lid in ids], cfg['core'])
        for _, ids in cfg['revision']:
            for lid in ids:
                self.assertLessEqual(placed_chapter(rows[lid]['Kata-Kata place']), 13, lid)
                self.assertNotIn(lid, cfg['core'])
        stage2 = {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
                  and re.match(r'Ch1[0-7] \(unit \w+\)(?:;|$)', r['Kata-Kata place'])}
        self.assertEqual(len(stage2), 271)  # 240 + the 31 words approved on 13 and 14 Nov 2026 (L-1273 to L-1303); the six practice-pool rows are not core
        self.assertFalse([lid for lid, r in rows.items() if re.match(r'Ch14 \(unit 14, recognition', r['Kata-Kata place'])])
        self.assertEqual(cfg['recognition'], [])
        cards = {c['id'] for c in self.pack['cards']}
        for lid in ms_c14.CORE:
            self.assertIn(rows[lid]['Kata-Kata (card IDs)'].split(',')[0].strip(), cards, lid)  # the class card is listed first; a Dunia twin may follow
        self.assertEqual(len(cards), 29)  # 22 core + 7 new (L-1289 to L-1295)

    def test_every_core_word_is_used(self):
        """All 29 chapter 14 core words (including L-1269 «tangguhkan» and L-1270 «batalkan») appear outside the vocabulary list."""
        text = ' | '.join(s.lower() for s in spans(self.all_lines(('ms-c14',), skip_vocab=True)))
        for lid in ms_c14.CFG['core']:
            form = self.ledger.row(lid)['Malay'].lower().split(' / ')[0]
            self.assertRegex(text, r'(?<![a-z-])' + re.escape(form) + r'(?![a-z-])', (lid, form))
        # Both roots are shown beside their -kan forms in the vocabulary list.
        v = ' '.join(self.lines(self.comp('ms-c14', 'Vocabulary')))
        self.assertIn('«tangguh» + ‹-kan›', v)
        self.assertIn('«batal» + ‹-kan›', v)

    def test_revision_words_really_return(self):
        text = ' '.join(' '.join(re.findall(r'[a-z]+(?:-[a-z]+)*', s.lower())) for s in spans(self.all_lines(('ms-c14',), skip_vocab=True)))
        for _, ids in ms_c14.CFG['revision']:
            for lid in ids:
                forms = [re.sub(r'\([^)]*\)', '', f).strip().lower() for f in self.ledger.row(lid)['Malay'].split('/')]
                self.assertTrue(any(re.search(r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', text) for f in forms), (lid, forms))

    def test_whole_words_and_roots(self):
        """Kata-Kata card notes: the ke-an, per-an, -an, -nya and lexicalised words are whole words, with their roots shown."""
        v = ' '.join(self.lines(self.comp('ms-c14', 'Vocabulary')))
        for w in ('‹walau›', '‹akhir›', '‹tuju›', '‹putus›', '‹ubah›', '‹lepas tu›', '«mula»', '«terus»', '«masa»', '«pilih»'):
            self.assertIn(w, v, w)
        mentions = json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']
        for w in ('walau', 'akhir', 'tuju', 'putus', 'ubah', 'lepas tu', '-nya', 'per-an'):
            self.assertIn(w, mentions, w)
        notes = ' '.join(ms_c14.CFG['teacher_notes'])
        for w in ('ms-c14-018 to -022', 'Whole words and roots', 'Where Japanese learners usually slip'):
            self.assertIn(w, notes, w)

    def test_written_and_everyday_words(self):
        """Sam: the formal connectors sit beside their everyday partners; «bila» for "when" is everyday, «apabila» is standard.
        The spoken lines (dialogue except the message lines, variant, listening, task key) use the everyday words."""
        v = ' '.join(self.lines(self.comp('ms-c14', 'Vocabulary')))
        for formal, everyday in (('jika', 'kalau'), ('apabila', 'bila'), ('namun', 'tetapi'), ('oleh itu', 'jadi'), ('seterusnya', 'kemudian')):
            row = next(x for x in v.split('[L-') if f'«{formal}»' in x)
            self.assertIn(f'«{everyday}»', row, (formal, everyday))
        notes = ' '.join(ms_c14.CFG['teacher_notes'])
        self.assertIn('«bila» as "when" is everyday and «apabila» is standard', notes)
        cfg = ms_c14.CFG
        # The Kata-Kata message lines s13 and s14 are the one place the dialogue shows the written words.
        spoken = [s for _, s in cfg['dialogue'][:12] + cfg['dialogue'][13:] + cfg['variant'] + cfg['listening']] + [cfg['task_key']]
        text = ' '.join(spoken).lower()
        for formal in ('jika', 'apabila', 'namun', 'oleh itu', 'seterusnya'):
            self.assertNotRegex(text, r'(?<![a-z])' + formal + r'(?![a-z])', formal)
        # The written message uses the written words and the notice test reading too.
        written = ' '.join(cfg['reading'] + cfg['test_reading']).lower()
        for formal in ('jika', 'apabila', 'namun', 'oleh itu', 'seterusnya'):
            self.assertRegex(written, r'(?<![a-z])' + formal + r'(?![a-z])', formal)
        self.assertTrue(ms_c14.CFG['dialogue'][12][1].startswith('Baik. Saya sudah tulis mesej untuk'))

    def test_casual_turns_no_ruling_style(self):
        """Sam: casual turns do not use ruling-style phrasing («keputusan»); «keputusan» is a word for a written notice or a result."""
        cfg = ms_c14.CFG
        casual = ' '.join(s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']).lower()
        for banned in ('keputusan', 'ialah', 'itu keputusan kita'):
            self.assertNotRegex(casual, r'(?<![a-z])' + banned + r'(?![a-z])', banned)
        # Sam's natural casual phrase is back (14 Nov 2026, L-1289 «baiklah» and L-1290 «begini»).
        self.assertIn('Baiklah, kita buat begini.', ' '.join(s for _, s in cfg['listening']))
        for sp in spans(self.lines(self.comp('ms-c14', 'Pattern and grammar'))):
            self.assertNotIn('keputusan', sp.lower(), sp)
        # «keputusan» is used in a written notice (the reading and the writing block).
        self.assertIn('Keputusan:', ' '.join(cfg['reading']))
        self.assertNotIn('Itu keputusan kita', ' '.join(self.all_lines()))
        # «baiklah» and «begini» are ledger rows now (L-1289, L-1290; 14 Nov 2026) and are in the unit.
        self.assertRegex(' '.join(spans(self.all_lines())).lower(), r'(?<![a-z])baiklah(?![a-z])')
        self.assertRegex(' '.join(spans(self.all_lines())).lower(), r'(?<![a-z])begini(?![a-z])')

    def test_kan_rule_and_dari(self):
        """Chapter 12 -kan rule (Sam): «tangguhkan» and «batalkan» only in «kita» sentences and requests, never after an aspect word or with a
        third-person doer. «dari» for places, «daripada» for people and organisations."""
        kan = r'(?:tangguhkan|batalkan|simpankan|hantarkan|bawakan|letakkan|elakkan|hubungi|baiki)'
        bad = re.compile(rf'\b(?:sudah|sedang|belum|akan|baru|masih)\s+{kan}\b', re.I)
        for sp in spans(self.all_lines()):
            self.assertIsNone(bad.search(sp), sp)
        pupil = ' '.join(line.lower() for line in self.pupil_malay())
        for gone in ('menyimpankan', 'menghantarkan', 'ditangguhkan', 'dibatalkan'):
            self.assertNotRegex(pupil, r'(?<![a-z])' + gone + r'(?![a-z])')
        text = ' '.join(self.all_lines())
        self.assertNotRegex(text, r'(?<![a-z])dari (?:doktor|kedai|bank|bos|syarikat|kawan|pengurus|Puan|Encik|Cik)')
        # The bare root in the dialogue (Kata-Kata's own line) and the meN- form in the pattern models and drills.
        self.assertIn('Saya sudah tulis mesej untuk kawan kita', ' '.join(s for _, s in ms_c14.CFG['dialogue']))
        self.assertIn('Saya menulis mesej itu', ' '.join(ms_c14.CFG['markers']['items']))

    def test_noun_object_and_kita(self):
        """Claude's review fixes: «tangguhkan» and «batalkan» take a noun object («rancangan»), not a verb; the group-chat messages and
        writing models use inclusive «kita» (not «kami»); a teacher note sets «kami» against «kita»."""
        text = ' '.join(self.all_lines())
        self.assertNotRegex(text, r'(?<![a-z])(?:tangguhkan|batalkan) mendaki')
        self.assertNotRegex(text, r'(?<![a-z])Mendaki (?:pada hari Sabtu )?batal')
        self.assertNotRegex(text, r'(?<!ancangan )(?<![a-z])mendaki batal')
        self.assertIn('Rancangan mendaki batal kerana hujan', text)
        # Third-person statements take the standard form (Sam, 14 Nov 2026); the bare form stays for requests, offers and «kita» plans.
        self.assertIn('Mei Ling menangguhkan rancangan mendaki kerana dia bekerja', text)
        self.assertNotRegex(text, r'(?:Mei Ling|Puan Aini|Aini|Encik \w+|Cik \w+) (?:tangguhkan|batalkan)(?![a-z])')
        self.assertIn('Oleh itu, kita tangguhkan rancangan itu ke hari Ahad', text)
        for sp in spans(self.all_lines()):
            if re.search(r'(?<![a-z])(?:tangguhkan|batalkan)(?![a-z])', sp) and re.search(r'(?<![a-z])kita masih(?![a-z])', sp):
                self.assertNotRegex(sp, r'(?<![a-z])[Kk]ami(?![a-z])', sp)
        notes = ' '.join(ms_c14.CFG['teacher_notes'])
        self.assertIn('«kami» against «kita»', notes)
        self.assertIn('leaves the listener out', notes)

    def test_katakata_alignment(self):
        """Same frames f01 to f06, same scene (the weekend hike), every scenario line word for word, card IDs cited."""
        frames = {f['id']: f for f in self.pack['frames']}
        self.assertEqual(sorted(frames), [f'ms-c14-f0{n}' for n in range(1, 7)])
        self.assertEqual(ms_c14.CFG['pattern_ids'], [f'ms-c14-f0{n}' for n in range(1, 7)])
        text = ' '.join(self.all_lines(('ms-c14',)))
        for f in frames.values():
            self.assertIn(f['example'], text, f['id'])
        lines = self.pack['scenario']['lines']
        self.assertEqual(len(lines), 15)
        for line in lines:
            self.assertIn(line['ms'], text, line['id'])
        # The rebuilt Kata-Kata line (7fbe173): «Kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.» and no «Itu keputusan kita».
        self.assertEqual(lines[11]['ms'], 'Kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.')
        plan = ' '.join(self.lines(self.comp('ms-c14', 'Teaching plan')))
        self.assertIn('ms-c14-s01', plan)
        self.assertIn('ms-c14-s15', plan)
        self.assertEqual({sp for sp, _ in ms_c14.DIALOGUE}, {'Tanaka', 'Mei Ling'})
        # The model conversation is the whole scene s01 to s15, in order.
        self.assertEqual([s for _, s in ms_c14.DIALOGUE], [l['ms'] for l in lines])
        self.assertEqual(len(ms_c14.DIALOGUE), 15)
        # The cards: 001 to 022, with the two -kan cards and their roots.
        terms = {c['id']: c['term'] for c in self.pack['cards']}
        self.assertEqual((terms['ms-c14-021'], terms['ms-c14-022']), ('tangguhkan', 'batalkan'))
        self.assertEqual((terms['ms-c14-018'], terms['ms-c14-020']), ('tangguh', 'batal'))

    def test_register_particles_and_scope(self):
        pupil = ' '.join(line.lower() for line in self.pupil_malay())
        words = re.findall(r'[a-z]+(?:-[a-z]+)*', ' '.join(spans([l for l in self.pupil_malay()] + ['«' + l + '»' for l in self.pupil_malay() if '«' not in l])).lower())
        for w in ('lah', 'kan', 'tak', 'dah', 'tapi', 'takpe', 'ni', 'tu', 'kat', 'jom', 'nak'):
            self.assertNotIn(w, words, w)
        self.assertNotRegex(pupil, r'assalam|waalaikum|insya|alhamdulillah|bismillah')
        self.assertNotRegex(' '.join(spans(self.all_lines())).lower(), r'agama|tuhan|solat|puasa|haram|halal')

    def test_components_patterns_and_minimums(self):
        required = {'Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                    'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan'}
        u = 'ms-c14'
        cfg = ms_c14.CFG
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
                  '«berapa lama»', '«siapa» with «oleh»', 'Chapters 1 to 14', 'Chapter 14 adds no new question word'):
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
        for w in ('Block E · Scene transfer', 'Sedia Kelas c14', 'not yet tagged by chapter', '0–5'):
            self.assertIn(w, plan + ' '.join(n for n, _, _ in self.comp(u, 'Teaching plan')['sections']), (u, w))
        # «lah» and «kan» (the particles) are never in an answer key; the plan row for the writing block is in the unit.
        keys = ' '.join(' '.join(l['key']) for l in self.by_unit[u]).lower()
        self.assertNotRegex(keys, r'(?<![a-z-])(lah|kan)(?![a-z])')

    def test_writing_block(self):
        """The writing block after unit 14 (plan section 1): explain and rearrange a plan; no new word."""
        l = self.comp('ms-c14', 'Reading and writing', slug='writing-block')
        self.assertEqual(l['suite']['block'], 'Skills')
        self.assertEqual(l['suite']['time_minutes'], 45)
        names = ' '.join(n for n, _, _ in l['sections'])
        for part in ('Model', 'Plan', 'Your turn', 'Peer check'):
            self.assertIn(part, names)
        plan = ' '.join(self.lines(l, 'Plan'))
        for t in ('0–5', '5–15', '15–30', '30–40', '40–45'):
            self.assertIn(t, plan)
        self.assertIn('writing block after unit 14', ' '.join(l['key']))
        self.assertEqual(ms_c14.EXTRA['patterns'][-1], 'ms-c14-f06')
        # The block uses no new word: every Malay word in it is in a ledger row placed at or before chapter 14.
        words = self.words(self.lines(l) + l['key'])
        checker = self.ledger.checker
        for w in set(words):
            if w in LOOKALIKE or w in NAMES or len(w) == 1:
                continue
            ch = [r['_chapter'] for r in checker.entries.get(w, []) if r['_chapter'] is not None]
            if not ch:
                ch = [r['_chapter'] for k, rs in checker.entries.items() if w in k.split() for r in rs if r['_chapter'] is not None]
            self.assertTrue(ch and min(ch) <= 14, w)

    def test_openers(self):
        opener = self.comp('ms-c14', 'Opener')
        body = ' '.join(self.lines(opener))
        self.assertIn(f'Sedia Kelas c14 ({katakata_ref.sedia_count(14)} cards, frames ms-c14-f01 and ms-c14-f02)', body)
        self.assertIn(f'（カード{katakata_ref.sedia_count(14)}枚、文型 f01・f02）', body)
        self.assertIn('ms-c14-001 to ms-c14-029', body)

    def test_culture_note_general_knowledge_labelled(self):
        cult = ' '.join(ms_c14.CULTURE)
        self.assertEqual(len(re.findall(r'General knowledge, not a rule and not a checked fact', cult)), 1)
        self.assertNotRegex(cult, r'RM|\bringgit\b|\d')

    def test_japanese_has_no_leftover_english(self):
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Sedia Kelas|Tanya Cikgu|Susun Ayat|Dunia|\bber-|\bmeN-|\*[a-z]+')
        cfg = ms_c14.CFG
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
        cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
        cells += [cfg['role_a'][-1], cfg['role_b'][-1], cfg['change'][-1], cfg['markers']['bridge'][-1].split(' / ')[-1]]
        cells += [o['ja'] for o in cfg['vocab_opts'].values() if 'ja' in o]
        cells += [ms_c14.EXTRA['explain'][0]]
        for ja in cells:
            self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
            self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_fast_pack(self):
        l = self.by_unit['ms-c14-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertEqual(len(core), 29)  # 22 + L-1289 to L-1295 (14 Nov 2026)
        self.assertEqual(set(fast.C14_WORDS), set(ms_c14.CORE))  # Sam, 13 Nov: «semasa» and «sejak» are in the fast pack
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
        self.assertIn(f'all {katakata_ref.card_count(14)} Kata-Kata chapter 14 cards (ms-c14-001 to ms-c14-{katakata_ref.last_own_card(14):03}', guide)

    def test_registration_and_catalogue(self):
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in UNITS + ('ms-c14-fast',):
            self.assertIn(u, reauthored)
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 20)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'].startswith(('ms-c14', 'ms-c14-fast'))])
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch = next(c for c in chapters if c['title'].startswith('Chapter 14'))
        self.assertEqual([u['label'] for u in ch['units']], ['14'])
        self.assertEqual((ch['level'], ch['sequence']), ('A2', 'stage2'))
        self.assertTrue(ch['fast_items'])
        self.assertFalse([c for c in chapters if c.get('sequence') == 'future'])
        catalogue = make_catalogue(bank(), chapters)
        c14 = next(c for c in catalogue['chapters'] if c['id'] == 'ms-c14')
        self.assertEqual((c14['level'], c14['stage_id']), ('A2', 'ms-stage2'))
        self.assertEqual([u['id'] for u in c14['units']], ['ms-c14'])
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('chapter_id') == 'ms-c14']
        self.assertTrue(mine and all(c['level'] == 'A2' for c in mine))
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage2-writing-14')
        self.assertEqual((block['after_unit'], block['component_ids']), ('ms-c14', ['ms-c14-writing-block']))
        self.assertEqual(catalogue['future_chapters'], [])


if __name__ == '__main__':
    unittest.main()
