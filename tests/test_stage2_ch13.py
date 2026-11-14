"""Stage 2 build step 4: chapter 13 (unit 13, health: belum, permission, need and advice) and the chapter 13 fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (25 core rows placed
"Ch13 (unit 13)", no recognition row), every core word used outside the vocabulary list, the chapter 12 ‹-kan› rule kept, alignment
with Kata-Kata c13 (frames f01 to f06, all 18 scenario lines, card IDs), the charter section 6 and 14 minimums, the traps the
Kata-Kata cards name («mesti» is a root; «kebenaran» means permission only), the safety rule (no diagnosis, no treatment advice, no
medicine with a dose, no dosing instruction; the doctor and the pharmacist say only what the brief allows), the spoken «MC» kept
to recognition, «lah» and «kan» never in a key, and the registration of the unit. Copied from tests/test_stage2_ch12.py.
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c13, fast
from catalogue import make_catalogue
from language_checks import placed_chapter

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
UNITS = ('ms-c13',)
CFGS = {'ms-c13': ms_c13.CFG}
# Marked words that look like ber- or meN- forms but are roots or Stage 1 whole words.
LOOKALIKE = {'berapa', 'bersih', 'besar', 'berat', 'belum', 'belajar', 'bekas', 'beli', 'bengkak', 'beg', 'bekerja', 'berehat',
             'merah', 'meter', 'mengapa', 'menu', 'melayu', 'mesyuarat', 'mereka', 'mesej', 'mesti', 'mei', 'meja', 'merokok', 'menang',
             'memang', 'mewah', 'menit', 'mentah', 'mereka', 'mel'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch13_rows(rows):
    """Core rows the ledger places in unit 13 (not the recognition rows)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(r'Ch13 \(unit 13\)(?:;|$)', r['Kata-Kata place'])}


NAMES = {w.lower() for n in json.loads((ROOT / 'curriculum/malay-proper-nouns.json').read_text())['names'] for w in n.split()}


def malay_words_of(text):
    return [w for sp in re.findall(r'«([^»]*)»', f'«{text}»') for w in re.findall(r'[a-z]+', sp.lower())]


def spans(lines):
    return [s for line in lines for s in re.findall(r'«([^»]*)»', line)]


class Chapter13(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.pack = json.loads((ROOT / 'curriculum/reference/katakata/c13.json').read_text())

    def comp(self, u, typ, sub=None, slug=None):
        found = [l for l in self.by_unit[u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {u} {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=UNITS + ('ms-c13-fast',), skip_vocab=False):
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
        cfg = ms_c13.CFG
        out = [s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']]
        for v in cfg['drills'].values():
            out += v if isinstance(v, list) else [v]
        for v in cfg['drill_keys'].values():
            out += v
        out += [ex for p in cfg['patterns'] for ex in p[2]]
        out += cfg['reading'] + [cfg['write_model'], cfg['task_key']] + cfg['markers']['items'] + cfg['markers']['key']
        out += self.lines(self.by_unit['ms-c13-fast'][0], 'Model conversation')
        return out

    def test_ledger_partition(self):
        rows = self.ledger.rows
        cfg = ms_c13.CFG
        self.assertEqual(len(cfg['core']), len(set(cfg['core'])))
        self.assertEqual(set(cfg['core']), ch13_rows(rows))
        self.assertEqual(len(cfg['core']), 29)  # 25 + L-1285 to L-1288 (14 Nov 2026)
        self.assertIn('L-1268', cfg['core'])
        self.assertEqual([lid for _, ids in cfg['core_groups'] for lid in ids], cfg['core'])
        for _, ids in cfg['revision']:
            for lid in ids:
                self.assertLessEqual(placed_chapter(rows[lid]['Kata-Kata place']), 12, lid)
                self.assertNotIn(lid, cfg['core'])
        stage2 = {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
                  and re.match(r'Ch1[0-7] \(unit \w+\)(?:;|$)', r['Kata-Kata place'])}
        self.assertEqual(len(stage2), 270)  # 240 + the 31 words approved on 13 and 14 Nov 2026 (L-1273 to L-1303), less L-1303 «minggu depan», Retired (Kata-Kata step 3f); the six practice-pool rows are not core
        # No ledger row carries a recognition place for chapter 13.
        self.assertFalse([lid for lid, r in rows.items() if re.match(r'Ch13 \(unit 13, recognition', r['Kata-Kata place'])])
        self.assertEqual(cfg['recognition'], [])
        cards = {c['id'] for c in self.pack['cards']}
        for lid in ms_c13.CORE:
            self.assertIn(rows[lid]['Kata-Kata (card IDs)'].split(',')[0].strip(), cards, lid)  # the class card is listed first; a Dunia twin may follow
        self.assertEqual(len(cards), 29)  # 25 core + 4 new (L-1285 to L-1288)

    def test_every_core_word_is_used(self):
        """All 25 chapter 13 core words (including L-1268 «mendaftar») appear outside the vocabulary list."""
        text = ' | '.join(s.lower() for s in spans(self.all_lines(('ms-c13',), skip_vocab=True)))
        for lid in ms_c13.CFG['core']:
            form = self.ledger.row(lid)['Malay'].lower().split(' / ')[0]
            self.assertRegex(text, r'(?<![a-z])' + re.escape(form) + r'(?![a-z])', (lid, form))

    def test_revision_words_really_return(self):
        text = ' '.join(' '.join(re.findall(r'[a-z]+(?:-[a-z]+)*', s.lower())) for s in spans(self.all_lines(('ms-c13',), skip_vocab=True)))
        for _, ids in ms_c13.CFG['revision']:
            for lid in ids:
                forms = [re.sub(r'\([^)]*\)', '', f).strip().lower() for f in self.ledger.row(lid)['Malay'].split('/')]
                self.assertTrue(any(re.search(r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', text) for f in forms), (lid, forms))

    def test_whole_words_and_traps(self):
        """Kata-Kata card notes: «mesti» is a root; «kebenaran» is permission only; the ke-an and -an words are whole words."""
        v = ' '.join(self.lines(self.comp('ms-c13', 'Vocabulary')))
        self.assertIn('‹me-› + ‹sti›', v)
        self.assertIn('permission, taught only in this sense', v)
        for w in ('‹benar›', '«sihat»', '‹cemas›', '‹arah›', '‹rawat›', '‹alah›', '‹suai›', '‹elak›'):
            self.assertIn(w, v, w)
        # Every use of «kebenaran» outside the vocabulary list is «minta kebenaran» (permission).
        for line in self.pupil_malay():
            for sp in re.findall(r'«([^»]*)»', f'«{line}»') if '«' not in line else spans([line]):
                if 'kebenaran' in sp.lower():
                    self.assertIn('minta kebenaran', sp.lower(), sp)
        notes = ' '.join(ms_c13.CFG['teacher_notes'])
        for w in ('ms-c13-021', 'ms-c13-005', 'permission only', 'secular', 'tidak perlu', 'tidak boleh', 'dilarang'):
            self.assertIn(w, notes, w)
        # The teacher notes carry the three contrasts and the Japanese slip the brief asks for.
        for w in ('«belum» against «tidak»', '«perlu» (need: a step) against «patut»', 'Where Japanese learners usually slip', '入ってもいいですか'):
            self.assertIn(w, notes, w)

    def test_kan_rule_in_statements(self):
        """Chapter 12 rule (Sam): bare -kan for requests and first-person replies; meN- (or a rephrase) after an aspect word or a third-person doer."""
        kan = r'(?:simpankan|hantarkan|ambilkan|belikan|bawakan|tutupkan|bukakan|letakkan|pulangkan|berikan|tunjukkan|pastikan|matikan|hidupkan|' \
              r'perlahankan|bersihkan|kosongkan|isikan|gantikan|elakkan|hubungi|baiki)'
        bad = re.compile(rf'\b(?:sudah|sedang|belum|akan|baru|masih|doktor|penyambut tetamu|pengawal)\s+{kan}\b', re.I)
        for sp in spans(self.all_lines()):
            self.assertIsNone(bad.search(sp), sp)
        text = ' '.join(self.all_lines())
        pupil = ' '.join(line.lower() for line in self.pupil_malay())
        for gone in ('ialah', 'keputusan', 'menyimpankan', 'menghantarkan'):
            self.assertNotRegex(pupil, r'(?<![a-z])' + gone + r'(?![a-z])')
        self.assertIn('Tolong elakkan lif itu', text)
        # Sam (13 Nov): no «elakkan bising»; «jangan bising» instead. «dari» is for places, «daripada» for people and organisations.
        self.assertNotIn('elakkan bising', text)
        self.assertIn('Sila jangan bising', text)
        self.assertNotRegex(text, r'(?<![a-z])dari (?:doktor|kedai|bank|bos)')
        self.assertIn('cuti sakit satu hari daripada doktor', text.lower())
        self.assertNotRegex(text, r'Pelawat|pelawat')

    def test_katakata_alignment(self):
        """Same frames f01 to f06, same scene (the panel clinic and the pharmacy), every scenario line word for word, card IDs cited."""
        frames = {f['id']: f for f in self.pack['frames']}
        self.assertEqual(sorted(frames), [f'ms-c13-f0{n}' for n in range(1, 7)])
        self.assertEqual(ms_c13.CFG['pattern_ids'], [f'ms-c13-f0{n}' for n in range(1, 7)])
        text = ' '.join(self.all_lines(('ms-c13',)))
        for f in frames.values():
            self.assertIn(f['example'], text, f['id'])
        lines = self.pack['scenario']['lines']
        self.assertEqual(len(lines), 18)
        for line in lines:
            self.assertIn(line['ms'], text, line['id'])
        plan = ' '.join(self.lines(self.comp('ms-c13', 'Teaching plan')))
        self.assertIn('ms-c13-s01', plan)
        self.assertIn('ms-c13-s18', plan)
        self.assertEqual({sp for sp, _ in ms_c13.DIALOGUE}, {'Receptionist', 'Tanaka', 'Doctor'})
        # The model conversation is the clinic scene s01 to s14, in order.
        self.assertEqual([s for _, s in ms_c13.DIALOGUE], [l['ms'] for l in lines[:14]])

    def test_safety_no_diagnosis_no_treatment_no_dose(self):
        """No diagnosis, no treatment advice, no medicine name with a dose, no dosing instruction. The doctor only says «patut berehat»
        and gives sick leave; the pharmacist only points to the label and says «tanya saya lagi»."""
        malay = ' '.join(spans(self.all_lines()) + [s for cfg in CFGS.values() for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']]).lower()
        for banned in ('ubat', 'pil', 'sebutir', 'sehari', 'kali sehari', 'tablet', 'kapsul', 'paracetamol', 'antibiotik', 'ibuprofen', 'sirap',
                       'diagnosis', 'jangkitan', 'virus', 'selesema', 'selsema', 'mg', 'ml', 'suntikan'):
            self.assertNotRegex(malay, r'(?<![a-z])' + banned + r'(?![a-z])', banned)
        self.assertNotRegex(malay, r'\d+\s*(mg|ml)')
        allowed_doctor = {'Encik patut berehat di rumah. Encik tidak perlu datang ke pejabat esok.', 'Boleh. Saya berikan cuti sakit satu hari.',
                          'Encik patut berehat.'}
        for cfg in CFGS.values():
            for sp, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']:
                if sp == 'Doctor':
                    self.assertIn(s, allowed_doctor, s)
                if sp == 'Pharmacist':
                    self.assertTrue('label' in s or 'tanya saya' in s.lower(), s)
                    self.assertNotRegex(s, r'\d')
        # The doctor's and the pharmacist's lines in the fast pack follow the same rule.
        fast_text = ' '.join(self.lines(self.by_unit['ms-c13-fast'][0], 'Model conversation'))
        for line in re.findall(r'(?:Doctor|Pharmacist): «([^»]*)»', fast_text):
            self.assertTrue(line in allowed_doctor or 'label' in line or 'tanya saya' in line, line)
        notes = ' '.join(ms_c13.CFG['teacher_notes'])
        for w in ('no diagnosis', 'no treatment advice', 'no dosing instruction', 'follow their own doctor and pharmacist', '«tanya saya lagi»', '«patut berehat»'):
            self.assertIn(w, notes, w)
        cult = ' '.join(ms_c13.CULTURE)
        self.assertIn('follow your own doctor and pharmacist', cult)
        # «dos» is for reading a label only.
        for line in self.pupil_malay():
            for sp in re.findall(r'«([^»]*)»', f'«{line}»') if '«' not in line else spans([line]):
                if re.search(r'(?<![a-z])dos(?![a-z])', sp.lower()):
                    self.assertTrue('label' in sp.lower() or sp.endswith('?'), sp)
        # The notice about an emergency door is a sign about a door, not emergency advice.
        self.assertIn('Pintu kecemasan ada di sebelah kiri', ' '.join(ms_c13.CFG['reading']))

    def test_spoken_mc_is_recognition_only(self):
        """«MC» is the spoken partner of «cuti sakit»: recognised, labelled spoken, never produced in a key or a test."""
        pat = r'(?<![a-z])mc(?![a-z])'
        for u in UNITS + ('ms-c13-fast',):
            for l in self.by_unit[u]:
                for t in l['suite']['tests']:
                    self.assertNotRegex(t['answer_key'].lower(), pat, t['id'])
                    self.assertNotRegex(t['prompt'].lower(), r'«[^»]*' + pat, t['id'])
                for line in self.lines(l) + l['key']:
                    for sp in re.findall(r'«([^»]*)»', line):
                        if re.search(pat, sp.lower()):
                            self.assertRegex(line, r'(?i)spoken|speech|everyday|話し言葉|日常|recognise|recognition|聞いて分か', (l['title'], line))
        cfg = ms_c13.CFG
        for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']:
            self.assertNotRegex(s.lower(), pat)
        for key in cfg['drill_keys'].values():
            for line in key:
                self.assertNotRegex(line.lower(), pat)
        self.assertNotRegex(' '.join(cfg['reading'] + [cfg['write_model'], cfg['task_key']]).lower(), pat)

    def test_register_particles_and_scope(self):
        text = ' '.join(self.all_lines())
        words = self.words(self.all_lines(skip_vocab=True))
        for w in ('lah', 'kan', 'tak', 'dah', 'tapi', 'takpe', 'ni', 'tu', 'kat', 'jom', 'nak'):
            self.assertNotIn(w, words, w)
        for w in ('apotek', 'darurat', 'kantor', 'berbicara', 'olahraga', 'rumah sakit'):
            self.assertNotIn(w, words, w)
        self.assertNotRegex(text.lower(), r'assalam|waalaikum|insya|alhamdulillah|bismillah')
        # «wajib» is secular: the notes say so and no Malay line mentions religion.
        self.assertNotRegex(' '.join(spans(self.all_lines())).lower(), r'agama|tuhan|solat|puasa|haram|halal')

    def test_components_patterns_and_minimums(self):
        required = {'Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                    'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan'}
        u = 'ms-c13'
        cfg = ms_c13.CFG
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
                  '«berapa lama»', '«siapa» with «oleh»', 'Chapters 1 to 13', 'Chapter 13 adds no new question word'):
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
        for w in ('Block E · Scene transfer', 'Sedia Kelas c13', 'not yet tagged by chapter', '0–5'):
            self.assertIn(w, plan + ' '.join(n for n, _, _ in self.comp(u, 'Teaching plan')['sections']), (u, w))
        # No extra block after unit 13 (the plan gives chapter 13 none).
        self.assertIsNone(cfg['extra'])
        self.assertFalse([l for l in self.by_unit[u] if l['suite']['block'] == 'Skills'])

    def test_openers(self):
        opener = self.comp('ms-c13', 'Opener')
        body = ' '.join(self.lines(opener))
        self.assertIn(f'Sedia Kelas c13 ({katakata_ref.sedia_count(13)} cards, frames ms-c13-f01 and ms-c13-f02)', body)
        self.assertIn(f'（カード{katakata_ref.sedia_count(13)}枚、文型 f01・f02）', body)
        self.assertIn('ms-c13-001 to ms-c13-029', body)

    def test_culture_note_general_knowledge_labelled(self):
        cult = ' '.join(ms_c13.CULTURE)
        self.assertEqual(len(re.findall(r'General knowledge, not a rule and not a checked fact', cult)), 1)
        self.assertNotRegex(cult, r'RM|\bringgit\b|\d')
        notes = ' '.join(ms_c13.CFG['teacher_notes'])
        self.assertIn('general knowledge, not a rule and not source-checked; no figure', notes)
        self.assertIn('Panel clinics and «cuti sakit» / «MC»', notes)
        self.assertNotRegex(notes, r'RM\s?\d')

    def test_japanese_has_no_leftover_english(self):
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Sedia Kelas|Tanya Cikgu|Susun Ayat|Dunia|\bber-|\bmeN-|\*[a-z]+')
        cfg = ms_c13.CFG
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
        cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
        cells += [cfg['role_a'][-1], cfg['role_b'][-1], cfg['change'][-1], cfg['markers']['bridge'][-1].split(' / ')[-1]]
        cells += [o['ja'] for o in cfg['vocab_opts'].values() if 'ja' in o]
        for ja in cells:
            self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
            self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_fast_pack(self):
        l = self.by_unit['ms-c13-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertEqual(len(core), 29)  # all chapter 13 core words (Sam's rule from chapter 15, widened in the chapter 18 prep)
        self.assertEqual(set(fast.C13_WORDS), set(ms_c13.CORE))
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
        self.assertIn(f'all {katakata_ref.card_count(13)} Kata-Kata chapter 13 cards (ms-c13-001 to ms-c13-{katakata_ref.last_own_card(13):03}', guide)

    def test_registration_and_catalogue(self):
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in UNITS + ('ms-c13-fast',):
            self.assertIn(u, reauthored)
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 20)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'].startswith(('ms-c13', 'ms-c13-fast'))])
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch = next(c for c in chapters if c['title'].startswith('Chapter 13'))
        self.assertEqual([u['label'] for u in ch['units']], ['13'])
        self.assertEqual((ch['level'], ch['sequence']), ('A2', 'stage2'))
        self.assertTrue(ch['fast_items'])
        # The old chapter 12 placeholder is retired: nothing is listed as "future".
        self.assertFalse([c for c in chapters if c.get('sequence') == 'future'])
        catalogue = make_catalogue(bank(), chapters)
        c13 = next(c for c in catalogue['chapters'] if c['id'] == 'ms-c13')
        self.assertEqual((c13['level'], c13['stage_id']), ('A2', 'ms-stage2'))
        self.assertEqual([u['id'] for u in c13['units']], ['ms-c13'])
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('chapter_id') == 'ms-c13']
        self.assertTrue(mine and all(c['level'] == 'A2' for c in mine))
        self.assertFalse([b for b in catalogue['additional_blocks'] if 'c13' in b['id'] or '13' in b['id'].split('-')[-1]])
        self.assertEqual(catalogue['future_chapters'], [])


if __name__ == '__main__':
    unittest.main()
