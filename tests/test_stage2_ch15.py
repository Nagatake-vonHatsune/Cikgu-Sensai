"""Stage 2 build step 4: chapter 15 (unit 15, describing things and people with «yang»), the review block after chapter 15 (Review 3)
and the chapter 15 fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (21 core rows placed
"Ch15 (unit 15)", no recognition row), every core word used outside the vocabulary list, «yang» as the connector Japanese does not need and
when it can be dropped, «memakai» for glasses, clothes, a hat and shoes, «hilang» against the chapter 16 ‹tertinggal›, «seperti itu» and
«seperti ini» with the spoken ‹macam tu› only named, «dari» for places and «daripada» for people and organisations, the -kan rule and the noun
objects of chapter 14, «kami» against «kita», alignment with Kata-Kata c15 (frames f01 to f06, all 17 scenario lines word for word, card IDs),
the charter section 6 and 14 minimums, the review block after chapter 15, «lah» and «kan» never in a key, and the registration of the unit.
Copied from tests/test_stage2_ch14.py.
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c15, fast
from catalogue import make_catalogue
from language_checks import placed_chapter

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
UNITS = ('ms-c15',)
# Marked words that look like ber- or meN- forms but are roots or Stage 1 whole words.
LOOKALIKE = {'berapa', 'bersih', 'besar', 'berat', 'belum', 'belajar', 'bekas', 'beli', 'bengkak', 'beg', 'bekerja', 'berehat',
             'merah', 'meter', 'mengapa', 'menu', 'melayu', 'mesyuarat', 'mereka', 'mesej', 'mesti', 'mei', 'meja', 'merokok', 'menang',
             'memang', 'mewah', 'menit', 'mentah', 'mereka', 'mel'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch15_rows(rows):
    """Core rows the ledger places in unit 15 (not the recognition rows)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(r'Ch15 \(unit 15\)$', r['Kata-Kata place'])}


NAMES = {w.lower() for n in json.loads((ROOT / 'curriculum/malay-proper-nouns.json').read_text())['names'] for w in n.split()}


def spans(lines):
    return [s for line in lines for s in re.findall(r'«([^»]*)»', line)]


class Chapter15(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.pack = json.loads((ROOT / 'curriculum/reference/katakata/c15.json').read_text())

    def comp(self, u, typ, sub=None, slug=None):
        found = [l for l in self.by_unit[u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {u} {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=UNITS + ('ms-c15-fast',), skip_vocab=False):
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
        cfg = ms_c15.CFG
        out = [s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']]
        for v in cfg['drills'].values():
            out += v if isinstance(v, list) else [v]
        for v in cfg['drill_keys'].values():
            out += v
        out += [ex for p in cfg['patterns'] for ex in p[2]]
        out += cfg['reading'] + [cfg['write_model'], cfg['task_key']] + cfg['markers']['items'] + cfg['markers']['key']
        out += self.lines(self.by_unit['ms-c15-fast'][0], 'Model conversation')
        return out

    def test_ledger_partition(self):
        rows = self.ledger.rows
        cfg = ms_c15.CFG
        self.assertEqual(len(cfg['core']), len(set(cfg['core'])))
        self.assertEqual(set(cfg['core']), ch15_rows(rows))
        self.assertEqual(len(cfg['core']), 21)
        for lid in ('L-1271', 'L-1272', 'L-0591', 'L-0618', 'L-0623'):
            self.assertIn(lid, cfg['core'])
        self.assertEqual([lid for _, ids in cfg['core_groups'] for lid in ids], cfg['core'])
        for _, ids in cfg['revision']:
            for lid in ids:
                self.assertLessEqual(placed_chapter(rows[lid]['Kata-Kata place']), 14, lid)
                self.assertNotIn(lid, cfg['core'])
        stage2 = {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
                  and re.match(r'Ch1[0-7] \(unit \w+\)$', r['Kata-Kata place'])}
        self.assertEqual(len(stage2), 240)
        self.assertFalse([lid for lid, r in rows.items() if re.match(r'Ch15 \(unit 15, recognition', r['Kata-Kata place'])])
        self.assertEqual(cfg['recognition'], [])
        cards = {c['id'] for c in self.pack['cards']}
        for lid in ms_c15.CORE:
            self.assertIn(rows[lid]['Kata-Kata (card IDs)'], cards, lid)
        self.assertEqual(len(cards), 21)

    def test_every_core_word_is_used(self):
        """All 21 chapter 15 core words (including L-1271 «memakai» and L-1272 «berwarna») appear outside the vocabulary list."""
        text = ' | '.join(s.lower() for s in spans(self.all_lines(('ms-c15',), skip_vocab=True)))
        for lid in ms_c15.CFG['core']:
            form = self.ledger.row(lid)['Malay'].lower().split(' / ')[0]
            self.assertRegex(text, r'(?<![a-z-])' + re.escape(form) + r'(?![a-z-])', (lid, form))

    def test_revision_words_really_return(self):
        text = ' '.join(' '.join(re.findall(r'[a-z]+(?:-[a-z]+)*', s.lower())) for s in spans(self.all_lines(('ms-c15',), skip_vocab=True)))
        for _, ids in ms_c15.CFG['revision']:
            for lid in ids:
                forms = [re.sub(r'\([^)]*\)', '', f).strip().lower() for f in self.ledger.row(lid)['Malay'].split('/')]
                self.assertTrue(any(re.search(r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', text) for f in forms), (lid, forms))

    def test_whole_words_and_roots(self):
        """Kata-Kata card notes: the ber-, meN-, -nya and lexicalised words are whole words, with their roots shown."""
        v = ' '.join(self.lines(self.comp('ms-c15', 'Vocabulary')))
        for w in ('‹jalur›', '‹ber-›', '‹me-›', '«pakai»', '«warna»', '‹-nya›', '‹ciri-ciri›', '‹macam tu›', '‹tertinggal›', '«macam»'):
            self.assertIn(w, v, w)
        mentions = json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']
        for w in ('jalur', 'ciri-ciri', 'macam tu', 'tertinggal', '-nya'):
            self.assertIn(w, mentions, w)
        notes = ' '.join(ms_c15.CFG['teacher_notes'])
        for w in ('Whole words and roots', 'Where Japanese learners usually slip', 'ms-c15-007, -017, -009, -012'):
            self.assertIn(w, notes, w)

    def test_teacher_notes_yang_memakai_hilang(self):
        """The four notes the brief asks for: «yang» as the connector Japanese does not need, when «yang» can be dropped, «memakai» against
        かける / 着る / かぶる / はく, and «hilang» against the chapter 16 ‹tertinggal›."""
        notes = ' '.join(ms_c15.CFG['teacher_notes'])
        for w in ('«yang» is the connector Japanese does not need', '黒い財布', '«dompet yang hitam» and «dompet hitam»',
                  'When «yang» can be dropped', '«beg ada zip» is a whole sentence',
                  '«memakai» covers glasses, clothes, a hat and shoes', 'かける', '着る', 'かぶる', 'はく',
                  '«hilang» (lost) against ‹tertinggal› (left behind)', 'chapter 16'):
            self.assertIn(w, notes, w)
        # «tertinggal» is never taught or used in a sentence: only the ‹…› mention is allowed.
        self.assertNotRegex(' '.join(spans(self.all_lines())).lower(), r'tertinggal')
        for p in ms_c15.CFG['patterns']:
            self.assertNotIn('tertinggal', ' '.join(p[2]).lower())

    def test_seperti_and_macam(self):
        """«seperti» is the standard word; «macam» is the spoken partner (chapter 5); ‹macam tu› is chapter 17 and is only a mention."""
        v = ' '.join(self.lines(self.comp('ms-c15', 'Vocabulary')))
        row = next(x for x in v.split('[L-') if '«seperti»' in x)
        self.assertIn('«macam»', row)
        self.assertIn('‹macam tu›', row)
        self.assertNotRegex(' '.join(spans(self.all_lines())).lower(), r'macam tu')
        self.assertRegex(' '.join(self.lines(self.comp('ms-c15', 'Pattern and grammar'))), r'seperti ini.*seperti itu|seperti itu.*seperti ini')

    def test_yang_kept_and_dropped(self):
        """A «yang» clause carries «ada» or a verb after «yang»; the adjective-only form keeps no «yang» in the Kata-Kata lines."""
        text = ' '.join(self.pupil_malay())
        self.assertIn('dompet yang hitam', ' '.join(ms_c15.CFG['teacher_notes']))
        # No description before the noun, and no «ada» clause without «yang» after a noun in a pattern answer.
        self.assertNotRegex(text, r'(?<![a-z])(?:beg|dompet) ada zip(?![a-z])')
        self.assertIn('Yang ada zip.', text)
        # «memakai» covers glasses, clothes, a hat and shoes in the unit.
        for thing in ('cermin mata', 'baju', 'topi', 'kasut'):
            self.assertRegex(text, rf'memakai [^.?!]*{thing}')

    def test_casual_turns_and_no_ruling_style(self):
        cfg = ms_c15.CFG
        casual = ' '.join(s for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']).lower()
        for banned in ('ialah', 'keputusan', 'baiklah', 'begini', 'tertinggal'):
            self.assertNotRegex(casual, r'(?<![a-z])' + banned + r'(?![a-z])', banned)

    def test_kan_rule_noun_objects_and_dari(self):
        """Chapter 12 -kan rule and the chapter 14 fix: «tangguhkan» and «batalkan» are not used in this unit's Malay at all; no meN-…-kan form;
        «dari» for places, «daripada» for people and organisations."""
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
        self.assertIn('Oh, saya sudah jumpa dia.', ' '.join(s for _, s in ms_c15.CFG['dialogue']))
        self.assertIn('Saya mencari', ' '.join(ex for p in ms_c15.CFG['patterns'] for ex in p[2]))

    def test_katakata_alignment(self):
        """Same frames f01 to f06, same scene (the lost wallet and the visitors), every scenario line word for word, card IDs cited."""
        frames = {f['id']: f for f in self.pack['frames']}
        self.assertEqual(sorted(frames), [f'ms-c15-f0{n}' for n in range(1, 7)])
        self.assertEqual(ms_c15.CFG['pattern_ids'], [f'ms-c15-f0{n}' for n in range(1, 7)])
        text = ' '.join(self.all_lines(('ms-c15',)))
        for f in frames.values():
            self.assertIn(f['example'], text, f['id'])
        lines = self.pack['scenario']['lines']
        self.assertEqual(len(lines), 17)
        for line in lines:
            self.assertIn(line['ms'], text, line['id'])
        # The rebuilt Kata-Kata lines (7fbe173), word for word in the model conversation.
        model = ' '.join(s for _, s in ms_c15.DIALOGUE)
        for line in lines:
            self.assertIn(line['ms'], model, line['id'])
        for exact in ('Seperti ini?', 'Ya, seperti itu, tetapi ada zip.', 'Yang ada zip. Yang itu!'):
            self.assertIn(exact, model)
        self.assertEqual(model.count('yang memakai'), 2)
        self.assertIn('membawa', model)
        plan = ' '.join(self.lines(self.comp('ms-c15', 'Teaching plan')))
        self.assertIn('ms-c15-s01', plan)
        self.assertIn('ms-c15-s17', plan)
        self.assertEqual({sp for sp, _ in ms_c15.DIALOGUE}, {'Tanaka', 'Staff', 'Rahman'})
        self.assertEqual(len(ms_c15.DIALOGUE), 16)
        # Turn 11 joins s11 and s12; the rest follow one to one.
        self.assertEqual(ms_c15.DIALOGUE[10][1], lines[10]['ms'] + ' ' + lines[11]['ms'])
        self.assertEqual([s for _, s in ms_c15.DIALOGUE[:10]], [l['ms'] for l in lines[:10]])
        self.assertEqual([s for _, s in ms_c15.DIALOGUE[11:]], [l['ms'] for l in lines[12:]])
        terms = {c['id']: c['term'] for c in self.pack['cards']}
        self.assertEqual((terms['ms-c15-020'], terms['ms-c15-021']), ('memakai', 'berwarna'))
        self.assertEqual((ms_c15.EXTRA['patterns'][-1], ms_c15.EXTRA['slug']), ('ms-c15-f05', 'review-block'))

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
        u = 'ms-c15'
        cfg = ms_c15.CFG
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
                  '«berapa lama»', '«siapa» with «oleh»', 'Chapters 1 to 15', 'Chapter 15 adds no new question word'):
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
        for w in ('Block E · Scene transfer', 'Sedia Kelas c15', 'not yet tagged by chapter', '0–5'):
            self.assertIn(w, plan + ' '.join(n for n, _, _ in self.comp(u, 'Teaching plan')['sections']), (u, w))
        # «lah» and «kan» (the particles) are never in an answer key.
        keys = ' '.join(' '.join(l['key']) for l in self.by_unit[u]).lower()
        self.assertNotRegex(keys, r'(?<![a-z-])(lah|kan)(?![a-z])')

    def test_review_block(self):
        """Review 3 after chapter 15 (plan section 1): chapters 13 to 15 plus the earlier verb contrasts; no new word."""
        l = self.comp('ms-c15', 'Reading and writing', slug='review-block')
        self.assertEqual(l['suite']['block'], 'Skills')
        self.assertEqual(l['suite']['time_minutes'], 45)
        names = ' '.join(n for n, _, _ in l['sections'])
        for part in ('Model', 'Plan', 'Your turn', 'Peer check'):
            self.assertIn(part, names)
        plan = ' '.join(self.lines(l, 'Plan'))
        for t in ('0–5', '5–15', '15–30', '30–40', '40–45'):
            self.assertIn(t, plan)
        self.assertIn('review block after unit 15', ' '.join(l['key']))
        self.assertEqual(ms_c15.EXTRA['kind'], 'review')
        # The review has no new word: every Malay word in it is in a ledger row placed at or before chapter 15.
        words = self.words(self.lines(l) + l['key'])
        checker = self.ledger.checker
        for w in set(words):
            if w in LOOKALIKE or w in NAMES or len(w) == 1:
                continue
            ch = [r['_chapter'] for r in checker.entries.get(w, []) if r['_chapter'] is not None]
            if not ch:
                ch = [r['_chapter'] for k, rs in checker.entries.items() if w in k.split() for r in rs if r['_chapter'] is not None]
            if not ch and w.endswith('nya'):  # -nya (chapter 2) on a placed root
                ch = [r['_chapter'] for r in checker.entries.get(w[:-3], []) if r['_chapter'] is not None]
            self.assertTrue(ch and min(ch) <= 15, w)
        # It covers chapters 13, 14 and 15 and the earlier verb contrasts.
        text = ' '.join(self.lines(l)).lower()
        for w in ('belum', 'perlu', 'supaya', 'walaupun', 'yang mana', 'hilang', 'berwarna', 'hubungi', 'mendaftar', 'bekerja', 'menunggu'):
            self.assertIn(w, text, w)

    def test_openers(self):
        opener = self.comp('ms-c15', 'Opener')
        body = ' '.join(self.lines(opener))
        self.assertIn(f'Sedia Kelas c15 ({katakata_ref.sedia_count(15)} cards, frames ms-c15-f01 and ms-c15-f02)', body)
        self.assertIn(f'（カード{katakata_ref.sedia_count(15)}枚、文型 f01・f02）', body)
        self.assertIn('ms-c15-001 to ms-c15-021', body)

    def test_culture_note_general_knowledge_labelled(self):
        cult = ' '.join(ms_c15.CULTURE)
        self.assertEqual(len(re.findall(r'General knowledge, not a rule and not a checked fact', cult)), 1)
        self.assertNotRegex(cult, r'RM|\bringgit\b|\d')

    def test_japanese_has_no_leftover_english(self):
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Sedia Kelas|Tanya Cikgu|Susun Ayat|Dunia|\bber-|\bmeN-|\*[a-z]+')
        cfg = ms_c15.CFG
        cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
        cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
        cells += [cfg['role_a'][-1], cfg['role_b'][-1], cfg['change'][-1], cfg['markers']['bridge'][-1].split(' / ')[-1]]
        cells += [o['ja'] for o in cfg['vocab_opts'].values() if 'ja' in o]
        cells += [ms_c15.EXTRA['explain'][0]]
        for ja in cells:
            self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
            self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_fast_pack(self):
        l = self.by_unit['ms-c15-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertEqual(len(core), 21)
        self.assertEqual(set(fast.C15_WORDS), set(ms_c15.CORE))  # as in chapter 14 (Sam, 13 Nov): the fast pack holds every core word
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
        self.assertIn(f'all {katakata_ref.card_count(15)} Kata-Kata chapter 15 cards (ms-c15-001 to ms-c15-{katakata_ref.last_own_card(15):03}', guide)

    def test_registration_and_catalogue(self):
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in UNITS + ('ms-c15-fast',):
            self.assertIn(u, reauthored)
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 20)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'].startswith(('ms-c15', 'ms-c15-fast'))])
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch = next(c for c in chapters if c['title'].startswith('Chapter 15'))
        self.assertEqual([u['label'] for u in ch['units']], ['15'])
        self.assertEqual((ch['level'], ch['sequence']), ('A2', 'stage2'))
        self.assertTrue(ch['fast_items'])
        self.assertFalse([c for c in chapters if c.get('sequence') == 'future'])
        catalogue = make_catalogue(bank(), chapters)
        c15 = next(c for c in catalogue['chapters'] if c['id'] == 'ms-c15')
        self.assertEqual((c15['level'], c15['stage_id']), ('A2', 'ms-stage2'))
        self.assertEqual([u['id'] for u in c15['units']], ['ms-c15'])
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('chapter_id') == 'ms-c15']
        self.assertTrue(mine and all(c['level'] == 'A2' for c in mine))
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage2-review-15')
        self.assertEqual((block['after_unit'], block['component_ids']), ('ms-c15', ['ms-c15-review-block']))
        self.assertEqual(catalogue['future_chapters'], [])


if __name__ == '__main__':
    unittest.main()
