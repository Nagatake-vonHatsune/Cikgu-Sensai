"""Stage 2 build step 4: chapter 16 (unit 16, accidents with «ter-»), the writing block after chapter 16 (a brief factual incident message)
and the chapter 16 fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (23 core rows placed
"Ch16 (unit 16)", no recognition row), every core word used outside the vocabulary list, the accident ‹ter-› against the chapter 6 superlative ‹ter-›,
«tertinggal» against «hilang», «terkunci» as a state, «Maaf, saya terlupa.» against Japanese うっかり〜てしまいました, «tidak sengaja» as emphasis,
the clinic safety rule (only bengkak, luka kecil, lebam; no diagnosis, advice or medicine), «dari» for places and «daripada» for people and organisations,
the -kan rule, «kami» against «kita», alignment with Kata-Kata c16 (frames f01 to f06, all 17 scenario lines word for word, card IDs),
the charter section 6 and 14 minimums, the writing block after chapter 16, «lah» and «kan» never in a key, and the registration of the unit.
Copied from tests/test_stage2_ch15.py.
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c16, fast
from catalogue import make_catalogue
from language_checks import placed_chapter

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
UNITS = ('ms-c16',)
# Marked words that look like ber- or meN- forms but are roots or Stage 1 whole words.
LOOKALIKE = {'berapa', 'bersih', 'besar', 'berat', 'belum', 'belajar', 'bekas', 'beli', 'bengkak', 'beg', 'bekerja', 'berehat',
             'merah', 'meter', 'mengapa', 'menu', 'melayu', 'mesyuarat', 'mereka', 'mesej', 'mesti', 'mei', 'meja', 'merokok', 'menang',
             'memang', 'mewah', 'menit', 'mentah', 'mereka', 'mel'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch16_rows(rows):
    """Core rows the ledger places in unit 16 (not the recognition rows)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(r'Ch16 \(unit 16\)$', r['Kata-Kata place'])}


NAMES = {w.lower() for n in json.loads((ROOT / 'curriculum/malay-proper-nouns.json').read_text())['names'] for w in n.split()}


def spans(lines):
    return [s for line in lines for s in re.findall(r'«([^»]*)»', line)]


class Chapter16(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.pack = json.loads((ROOT / 'curriculum/reference/katakata/c16.json').read_text())

    def comp(self, u, typ, sub=None, slug=None):
        found = [l for l in self.by_unit[u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {u} {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=UNITS + ('ms-c16-fast',), skip_vocab=False):
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
        cfg = ms_c16.CFG
        out = [s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']]
        for v in cfg['drills'].values():
            out += v if isinstance(v, list) else [v]
        for v in cfg['drill_keys'].values():
            out += v
        out += [ex for p in cfg['patterns'] for ex in p[2]]
        out += cfg['reading'] + [cfg['write_model'], cfg['task_key']] + cfg['markers']['items'] + cfg['markers']['key']
        out += self.lines(self.by_unit['ms-c16-fast'][0], 'Model conversation')
        return out

    def test_ledger_partition(self):
        rows = self.ledger.rows
        cfg = ms_c16.CFG
        self.assertEqual(len(cfg['core']), len(set(cfg['core'])))
        self.assertEqual(set(cfg['core']), ch16_rows(rows))
        self.assertEqual(len(cfg['core']), 23)
        for lid in ('L-0619', 'L-0621', 'L-0644', 'L-0752', 'L-0758', 'L-0875', 'L-1251'):
            self.assertIn(lid, cfg['core'])
        self.assertEqual([lid for _, ids in cfg['core_groups'] for lid in ids], cfg['core'])
        for _, ids in cfg['revision']:
            for lid in ids:
                self.assertLessEqual(placed_chapter(rows[lid]['Kata-Kata place']), 15, lid)
                self.assertNotIn(lid, cfg['core'])
        stage2 = {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
                  and re.match(r'Ch1[0-7] \(unit \w+\)$', r['Kata-Kata place'])}
        self.assertEqual(len(stage2), 240)
        self.assertFalse([lid for lid, r in rows.items() if re.match(r'Ch16 \(unit 16, recognition', r['Kata-Kata place'])])
        self.assertEqual(cfg['recognition'], [])
        cards = {c['id'] for c in self.pack['cards']}
        for lid in ms_c16.CORE:
            self.assertIn(rows[lid]['Kata-Kata (card IDs)'], cards, lid)
        self.assertEqual(len(cards), 23)

    def test_every_core_word_is_used(self):
        """All 23 chapter 16 core words appear outside the vocabulary list (the brief names 11 ter- words; terjatuh, tertidur and terbakar are core too)."""
        text = ' | '.join(s.lower() for s in spans(self.all_lines(('ms-c16',), skip_vocab=True)))
        for lid in ms_c16.CFG['core']:
            form = self.ledger.row(lid)['Malay'].lower().split(' / ')[0]
            self.assertRegex(text, r'(?<![a-z-])' + re.escape(form) + r'(?![a-z-])', (lid, form))

    def test_revision_words_really_return(self):
        text = ' '.join(' '.join(re.findall(r'[a-z]+(?:-[a-z]+)*', s.lower())) for s in spans(self.all_lines(('ms-c16',), skip_vocab=True)))
        for _, ids in ms_c16.CFG['revision']:
            for lid in ids:
                forms = [re.sub(r'\([^)]*\)', '', f).strip().lower() for f in self.ledger.row(lid)['Malay'].split('/')]
                self.assertTrue(any(re.search(r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', text) for f in forms), (lid, forms))

    def test_whole_words_and_roots(self):
        """Each ter- word is shown with its root and the root's chapter, and glossed as "by accident, without meaning to" (or as a state)."""
        v = ' '.join(self.lines(self.comp('ms-c16', 'Vocabulary')))
        for w in ('‹jatuh›', '‹silap›', '‹langgar›', '‹gelincir›', '‹cedera›', '‹bakar›', '‹putus›', '‹sangkut›', '‹malang›', '‹ter-›', '‹ke-an›',
                  '«tinggal», chapter 2', '«lupa», chapter 4', '«tidur», chapter 4', '«lepas», chapter 4', '«tumpah», this chapter', '«kunci», this chapter',
                  'by accident, without meaning to', '‹tak sengaja›'):
            self.assertIn(w, v, w)
        mentions = json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']
        for w in ('jatuh', 'silap', 'langgar', 'gelincir', 'cedera', 'bakar', 'putus', 'sangkut', 'malang', 'tak sengaja', 'ter-'):
            self.assertIn(w, mentions, w)
        opts = ms_c16.VOCAB_OPTS
        for lid in ms_c16.ACCIDENT + ms_c16.STATE:
            self.assertIn('‹ter-› +', opts[lid]['en'], lid)
            self.assertIn('‹ter-›＋', opts[lid]['ja'], lid)
        for lid in ms_c16.ACCIDENT:
            self.assertRegex(opts[lid]['en'], r'by accident|without meaning to|by mistake|to slip|to miss', lid)
        for lid in ('L-1239', 'L-1240', 'L-1242', 'L-1243'):
            self.assertIn('state', opts[lid]['en'], lid)
        notes = ' '.join(ms_c16.CFG['teacher_notes'])
        for w in ('Whole words and roots', 'Where Japanese learners usually slip'):
            self.assertIn(w, notes, w)
        # the roots that are not ledger words are not taught alone: no «jatuh», «silap», «langgar» ... in a «…» span
        taught = ' '.join(spans(self.all_lines())).lower()
        for root in ('jatuh', 'silap', 'langgar', 'gelincir', 'cedera', 'bakar', 'putus', 'sangkut', 'malang'):
            self.assertNotRegex(taught, r'(?<![a-z-])' + root + r'(?![a-z-])', root)

    def test_two_ter_side_by_side(self):
        """Teacher note and patterns: the chapter 6 superlative ter- ("the most") against the accident ter- ("by accident"), shown side by side as the first Kata-Kata cards do."""
        notes = ' '.join(ms_c16.CFG['teacher_notes'])
        for w in ('ter- accident against ter- superlative', '«termurah», «terbesar», «terbaik»', '"the most"', '"by accident, without meaning to"',
                  'the first card', 'learn each form as a word', 'Yang ini termurah, tetapi dompet saya tertinggal di rumah.'):
            self.assertIn(w, notes, w)
        pat = ' '.join(self.lines(self.comp('ms-c16', 'Pattern and grammar')))
        for w in ('"the most"', '"by accident, without meaning to"', 'termurah', 'terbesar', 'terbaik', 'tertinggal', 'the root'):
            self.assertIn(w, pat, w)
        v = ' '.join(self.lines(self.comp('ms-c16', 'Vocabulary')))
        for lid in ms_c16.REV_TER6:
            self.assertIn('"the most" (not an accident)', ms_c16.VOCAB_OPTS[lid]['en'])
        self.assertIn('Revision · 復習 · The ter- of chapter 6 (the most)', v)
        # «termurah» is the superlative, never an accident word in the unit's models
        text = ' '.join(self.pupil_malay())
        self.assertNotRegex(text, r'(?<![a-z])(?:saya|dia) termurah')

    def test_tertinggal_against_hilang(self):
        notes = ' '.join(ms_c16.CFG['teacher_notes'])
        for w in ('«tertinggal» (left behind) against «hilang» (lost, chapter 15)', 'do I know where it is'):
            self.assertIn(w, notes, w)
        # «hilang» never stands for a left-behind thing in a pupil line of this unit
        text = ' '.join(self.pupil_malay())
        self.assertNotRegex(text, r'(?:kunci|dompet|telefon) (?:saya )?(?:tertinggal)[^.]*hilang')
        self.assertIn('Kunci saya tertinggal di dalam rumah.', text)

    def test_apology_and_state_notes(self):
        notes = ' '.join(ms_c16.CFG['teacher_notes'])
        for w in ('Apologising in Malay against Japanese うっかり〜てしまいました', '«Maaf, saya terlupa.» is the whole apology',
                  '«Jangan risau.»', '«terkunci» as a state, not an action', '«Pintu terkunci.»', 'nobody is locking it'):
            self.assertIn(w, notes, w)
        self.assertIn('Maaf, saya terlupa.', ' '.join(self.pupil_malay()))
        # «terkunci», «terputus», «tercedera» and «terbakar» are states: no doer in the sentence
        text = ' '.join(self.pupil_malay())
        self.assertNotRegex(text, r'(?:saya|awak|dia|kami) (?:terkunci|terputus|terbakar)(?![a-z])')
        # «tidak sengaja» adds emphasis to a ter- verb
        self.assertIn('adds emphasis', ' '.join(ms_c16.CFG['patterns'][2][3:5]))
        self.assertRegex(' '.join(ms_c16.CFG['teacher_notes']), r'«tidak sengaja» with a ter- verb adds emphasis')

    def test_clinic_safety(self):
        """The clinic scene describes the injury only as Kata-Kata does (bengkak, luka kecil, lebam). No diagnosis, no treatment advice and no medicine;
        the receptionist only registers Mr Tanaka and asks him to wait."""
        spoken = ' '.join(spans(self.all_lines())).lower()
        for banned in ('ubat', 'rawat', 'patah', 'retak', 'balut', 'ais', 'krim', 'sapu', 'antibiotik', 'pil', 'suntik', 'x-ray', 'diagnos', 'sprain', 'terseliuh', 'terkehel'):
            self.assertNotRegex(spoken, r'(?<![a-z-])' + banned + r'(?![a-z-])', banned)
        english = ' '.join(self.all_lines(('ms-c16',))).lower()
        for banned in ('take medicine', 'painkiller', 'ibuprofen', 'paracetamol', 'put ice', 'apply ', 'you should rest', 'it is a sprain', 'it is broken bone'):
            self.assertNotIn(banned, english, banned)
        d = ms_c16.DIALOGUE
        clinic = [(sp, s) for sp, s in d[10:] ]
        receptionist = [s for sp, s in clinic if sp == 'Receptionist']
        self.assertEqual(receptionist, ['Encik tercedera? Di mana yang sakit?', 'Encik perlu daftar dulu. Ini borang.', 'Boleh. Sila tunggu sekejap.'])
        self.assertIn('Tangan saya bengkak dan ada luka kecil. Lutut saya pun lebam.', [s for _, s in d])
        notes = ' '.join(ms_c16.CFG['teacher_notes'])
        for w in ('The clinic scene (safety)', 'no diagnosis, no treatment advice and no medicine', 'a question for the doctor'):
            self.assertIn(w, notes, w)
        self.assertIn('Do not role-play any medical advice', ms_c16.CFG['plan']['E_roleplay'])

    def test_casual_turns_and_no_ruling_style(self):
        cfg = ms_c16.CFG
        casual = ' '.join(s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']).lower()
        for banned in ('ialah', 'keputusan', 'baiklah', 'begini'):
            self.assertNotRegex(casual, r'(?<![a-z])' + banned + r'(?![a-z])', banned)

    def test_kan_rule_noun_objects_and_dari(self):
        """Chapter 12 -kan rule and the chapter 14 fix: «tangguhkan» and «batalkan» are not used in this unit's Malay at all; no meN-…-kan form;
        «dari» for places, «daripada» for people and organisations; «kita» includes the listener, «kami» does not."""
        kan = r'(?:tangguhkan|batalkan|simpankan|hantarkan|bawakan|letakkan|elakkan|hubungi|baiki)'
        bad = re.compile(rf'\b(?:sudah|sedang|belum|akan|baru|masih)\s+{kan}\b', re.I)
        for sp in spans(self.all_lines()):
            self.assertIsNone(bad.search(sp), sp)
        pupil = ' '.join(line.lower() for line in self.pupil_malay())
        for gone in ('menyimpankan', 'menghantarkan', 'ditangguhkan', 'dibatalkan', 'menangguhkan', 'membatalkan'):
            self.assertNotRegex(pupil, r'(?<![a-z])' + gone + r'(?![a-z])')
        text = ' '.join(self.all_lines())
        self.assertNotRegex(text, r'(?<![a-z])dari (?:doktor|kedai|bank|bos|syarikat|kawan|pengurus|Puan|Encik|Cik)')
        # The bare root in the dialogue (Kata-Kata's own line) and the meN- form in the pattern models, drills and keys.
        self.assertIn('Saya hubungi pejabat pengurusan.', ' '.join(s for _, s in ms_c16.CFG['dialogue']))
        self.assertIn('Encik perlu daftar dulu.', ' '.join(s for _, s in ms_c16.CFG['dialogue']))
        self.assertIn('Saya mencari', ' '.join(ex for p in ms_c16.CFG['patterns'] for ex in p[2]))
        self.assertNotRegex(pupil, r'(?<![a-z])(?:tangguhkan|batalkan)(?![a-z])')
        # the written reading and the writing model use the meN- form
        self.assertIn('mendaftar', ' '.join(ms_c16.CFG['reading']))

    def test_katakata_alignment(self):
        """Same frames f01 to f06, same scene (the locked door, the spilt coffee and the slip), every scenario line word for word, card IDs cited."""
        frames = {f['id']: f for f in self.pack['frames']}
        self.assertEqual(sorted(frames), [f'ms-c16-f0{n}' for n in range(1, 7)])
        self.assertEqual(ms_c16.CFG['pattern_ids'], [f'ms-c16-f0{n}' for n in range(1, 7)])
        text = ' '.join(self.all_lines(('ms-c16',)))
        for f in frames.values():
            self.assertIn(f['example'], text, f['id'])
        lines = self.pack['scenario']['lines']
        self.assertEqual(len(lines), 17)
        for line in lines:
            self.assertIn(line['ms'], text, line['id'])
        model = ' '.join(s for _, s in ms_c16.DIALOGUE)
        for line in lines:
            self.assertIn(line['ms'], model, line['id'])
        plan = ' '.join(self.lines(self.comp('ms-c16', 'Teaching plan')))
        self.assertIn('ms-c16-s01', plan)
        self.assertIn('ms-c16-s17', plan)
        self.assertEqual({sp for sp, _ in ms_c16.DIALOGUE}, {'Tanaka', 'Guard', 'Mei Ling', 'Receptionist'})
        self.assertEqual(len(ms_c16.DIALOGUE), 16)
        # Turn 11 joins s11 and s12 (both Tanaka); the rest follow one to one.
        self.assertEqual(ms_c16.DIALOGUE[10][1], lines[10]['ms'] + ' ' + lines[11]['ms'])
        self.assertEqual([s for _, s in ms_c16.DIALOGUE[:10]], [l['ms'] for l in lines[:10]])
        self.assertEqual([s for _, s in ms_c16.DIALOGUE[11:]], [l['ms'] for l in lines[12:]])
        # The three scenes of the brief: locked out with the key inside, Mei Ling late with the spill and the cup, Tanaka's slip and the clinic.
        for w in ('kunci saya tertinggal di dalam rumah', 'pintu terkunci', 'terlepas bas', 'tersangkut', 'tertumpah', 'pecah', 'tergelincir', 'tercedera', 'bengkak', 'luka kecil', 'lebam'):
            self.assertIn(w, model.lower(), w)
        terms = {c['id']: c['term'] for c in self.pack['cards']}
        self.assertEqual((terms['ms-c16-002'], terms['ms-c16-009'], terms['ms-c16-015']), ('tertinggal', 'terkunci', 'tidak sengaja'))
        self.assertEqual((ms_c16.EXTRA['patterns'][-1], ms_c16.EXTRA['slug']), ('ms-c16-f06', 'writing-block'))
        cites = ' '.join([ms_c16.CFG['culture_sources']] + ms_c16.CFG['teacher_notes'])
        for cid in ('ms-c16-002', 'ms-c16-003', 'ms-c16-009', 'ms-c16-015'):
            self.assertIn(cid[-3:], ms_c16.CFG['culture_sources'] if cid[-3:] != '002' else cites)

    def test_register_particles_and_scope(self):
        pupil = ' '.join(line.lower() for line in self.pupil_malay())
        words = re.findall(r'[a-z]+(?:-[a-z]+)*', ' '.join(spans([l for l in self.pupil_malay()] + ['«' + l + '»' for l in self.pupil_malay() if '«' not in l])).lower())
        for w in ('lah', 'kan', 'tak', 'dah', 'tapi', 'takpe', 'ni', 'tu', 'kat', 'jom', 'nak', 'macam'):
            self.assertNotIn(w, words, w)
        self.assertNotRegex(pupil, r'assalam|waalaikum|insya|alhamdulillah|bismillah')
        self.assertNotRegex(' '.join(spans(self.all_lines())).lower(), r'agama|tuhan|solat|puasa|haram|halal')

    def test_components_patterns_and_minimums(self):
        required = {'Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                    'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan'}
        u = 'ms-c16'
        cfg = ms_c16.CFG
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
                  '«berapa lama»', '«siapa» with «oleh»', 'Chapters 1 to 16', 'Chapter 16 adds no new question word'):
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
        for w in ('Block E · Scene transfer', 'Sedia Kelas c16', 'not yet tagged by chapter', '0–5'):
            self.assertIn(w, plan + ' '.join(n for n, _, _ in self.comp(u, 'Teaching plan')['sections']), (u, w))
        # «lah» and «kan» (the particles) are never in an answer key.
        keys = ' '.join(' '.join(l['key']) for l in self.by_unit[u]).lower()
        self.assertNotRegex(keys, r'(?<![a-z-])(lah|kan)(?![a-z])')

    def test_writing_block(self):
        """The writing block after unit 16 (plan section 1): a brief factual incident message; no new word."""
        l = self.comp('ms-c16', 'Reading and writing', slug='writing-block')
        self.assertEqual(l['suite']['block'], 'Skills')
        self.assertEqual(l['suite']['time_minutes'], 45)
        names = ' '.join(n for n, _, _ in l['sections'])
        for part in ('Model', 'Plan', 'Your turn', 'Peer check'):
            self.assertIn(part, names)
        plan = ' '.join(self.lines(l, 'Plan'))
        for t in ('0–5', '5–15', '15–30', '30–40', '40–45'):
            self.assertIn(t, plan)
        self.assertIn('writing block after unit 16', ' '.join(l['key']))
        self.assertEqual(ms_c16.EXTRA['kind'], 'writing')
        # The block uses no new word: every Malay word in it is in a ledger row placed at or before chapter 16.
        words = self.words(self.lines(l) + l['key'])
        checker = self.ledger.checker
        for w in set(words):
            if w in LOOKALIKE or w in NAMES or len(w) == 1:
                continue
            ch = [r['_chapter'] for r in checker.entries.get(w, []) if r['_chapter'] is not None]
            if not ch:
                ch = [r['_chapter'] for k, rs in checker.entries.items() if w in k.split() for r in rs if r['_chapter'] is not None]
            self.assertTrue(ch and min(ch) <= 16, w)
        # Factual: ter- verbs and states, tidak sengaja, one request, only what can be seen; no blame and no advice.
        text = ' '.join(self.lines(l)).lower()
        for w in ('tertinggal', 'terkunci', 'tertumpah', 'tidak sengaja', 'boleh tolong', 'bengkak', 'luka kecil', 'lebam', 'no blame', 'no advice'):
            self.assertIn(w, text, w)

    def test_openers(self):
        opener = self.comp('ms-c16', 'Opener')
        body = ' '.join(self.lines(opener))
        self.assertIn(f'Sedia Kelas c16 ({katakata_ref.sedia_count(16)} cards, frames ms-c16-f01 and ms-c16-f02)', body)
        self.assertIn(f'（カード{katakata_ref.sedia_count(16)}枚、文型 f01・f02）', body)
        self.assertIn('ms-c16-001 to ms-c16-023', body)

    def test_culture_note_general_knowledge_labelled(self):
        cult = ' '.join(ms_c16.CULTURE)
        self.assertEqual(len(re.findall(r'General knowledge, not a rule and not a checked fact', cult)), 1)
        self.assertNotRegex(cult, r'RM|\bringgit\b|\d')

    def test_japanese_has_no_leftover_english(self):
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Sedia Kelas|Tanya Cikgu|Susun Ayat|Dunia|\bber-|\bmeN-|\*[a-z]+')
        cfg = ms_c16.CFG
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
        cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
        cells += [cfg['role_a'][-1], cfg['role_b'][-1], cfg['change'][-1], cfg['markers']['bridge'][-1].split(' / ')[-1]]
        cells += [o['ja'] for o in cfg['vocab_opts'].values() if 'ja' in o]
        cells += [ms_c16.EXTRA['explain'][0]]
        for ja in cells:
            self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
            self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_fast_pack(self):
        l = self.by_unit['ms-c16-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertEqual(len(core), 23)
        self.assertEqual(set(fast.C16_WORDS), set(ms_c16.CORE))  # as in chapter 14 (Sam, 13 Nov): the fast pack holds every core word
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
        self.assertIn(f'all {katakata_ref.card_count(16)} Kata-Kata chapter 16 cards (ms-c16-001 to ms-c16-{katakata_ref.last_own_card(16):03}', guide)

    def test_registration_and_catalogue(self):
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in UNITS + ('ms-c16-fast',):
            self.assertIn(u, reauthored)
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 20)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'].startswith(('ms-c16', 'ms-c16-fast'))])
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch = next(c for c in chapters if c['title'].startswith('Chapter 16'))
        self.assertEqual([u['label'] for u in ch['units']], ['16'])
        self.assertEqual((ch['level'], ch['sequence']), ('A2', 'stage2'))
        self.assertTrue(ch['fast_items'])
        self.assertFalse([c for c in chapters if c.get('sequence') == 'future'])
        catalogue = make_catalogue(bank(), chapters)
        c16 = next(c for c in catalogue['chapters'] if c['id'] == 'ms-c16')
        self.assertEqual((c16['level'], c16['stage_id']), ('A2', 'ms-stage2'))
        self.assertEqual([u['id'] for u in c16['units']], ['ms-c16'])
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('chapter_id') == 'ms-c16']
        self.assertTrue(mine and all(c['level'] == 'A2' for c in mine))
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage2-writing-16')
        self.assertEqual((block['after_unit'], block['component_ids']), ('ms-c16', ['ms-c16-writing-block']))
        self.assertEqual(catalogue['future_chapters'], [])


if __name__ == '__main__':
    unittest.main()
