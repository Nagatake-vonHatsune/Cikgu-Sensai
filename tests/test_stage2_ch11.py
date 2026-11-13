"""Stage 2 build step 4: chapter 11 (units 11A and 11B, meN- verbs), the review block after 11B and the chapter 11 fast
pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (41 core rows placed
"Ch11 (unit 11A)" or "Ch11 (unit 11B)", L-0604 «tukar» and L-0678 «deadline» as the two recognition rows), every core word
used outside the vocabulary list, the meN- rule (every meN-shaped word is its own ledger row placed at or before chapter 11;
no suffixed -kan or -i form), alignment with Kata-Kata c11 (frames f01 to f06, the scenario lines s01 to s18, card IDs), the
charter section 6 and 14 minimums, the traps the Kata-Kata cards name, the spoken partners kept to recognition, «lah» and
«kan» never in a key, and the registration of the units. Copied from tests/test_stage2_ch10.py.
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c11a, ms_c11b, fast
from catalogue import make_catalogue
from language_checks import placed_chapter

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
UNITS = ('ms-c11a', 'ms-c11b')
CFGS = {'ms-c11a': ms_c11a.CFG, 'ms-c11b': ms_c11b.CFG}
# Marked words that look like ber- or meN- forms but are roots or Stage 1 whole words.
LOOKALIKE = {'berapa', 'bersih', 'besar', 'berat', 'belum', 'belajar', 'bekas', 'beli', 'bengkak', 'beg', 'bekerja', 'berehat',
             'merah', 'meter', 'mengapa', 'menu', 'melayu', 'mesyuarat', 'mereka', 'mesej', 'mesti', 'mei', 'meja', 'merokok', 'menang',
             'memang', 'mewah', 'menit', 'mentah', 'mereka', 'mel'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch11_rows(rows, unit):
    """Core rows the ledger places in the unit (not the recognition rows)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(rf'Ch11 \(unit {unit}\)$', r['Kata-Kata place'])}


NAMES = {w.lower() for n in json.loads((ROOT / 'curriculum/malay-proper-nouns.json').read_text())['names'] for w in n.split()}


def malay_words_of(text):
    return [w for sp in re.findall(r'«([^»]*)»', f'«{text}»') for w in re.findall(r'[a-z]+', sp.lower())]


def spans(lines):
    return [s for line in lines for s in re.findall(r'«([^»]*)»', line)]


class Chapter11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.pack = json.loads((ROOT / 'curriculum/reference/katakata/c11.json').read_text())

    def comp(self, u, typ, sub=None, slug=None):
        found = [l for l in self.by_unit[u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {u} {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=UNITS + ('ms-c11-fast',), skip_vocab=False):
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

    def test_ledger_partition(self):
        rows = self.ledger.rows
        for u, label in (('ms-c11a', '11A'), ('ms-c11b', '11B')):
            cfg = CFGS[u]
            self.assertEqual(len(cfg['core']), len(set(cfg['core'])))
            self.assertEqual(set(cfg['core']), ch11_rows(rows, label), u)
            self.assertEqual(len(cfg['core']), 20 if u == 'ms-c11a' else 21)
            self.assertEqual([lid for _, ids in cfg['core_groups'] for lid in ids], cfg['core'])
            for _, ids in cfg['revision']:
                for lid in ids:
                    self.assertLessEqual(placed_chapter(rows[lid]['Kata-Kata place']), 10, (u, lid))
                    self.assertNotIn(lid, cfg['core'])
        # 41 core rows for chapter 11 (plan section 2), 240 across Stage 2 (build step 4 refresh).
        self.assertEqual(len(ch11_rows(rows, '11A') | ch11_rows(rows, '11B')), 41)
        stage2 = {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
                  and re.match(r'Ch1[0-7] \(unit \w+\)$', r['Kata-Kata place'])}
        self.assertEqual(len(stage2), 240)
        # The recognition rows are «tukar» and «deadline», the spoken partners of «menukar» and «tarikh akhir».
        rec = [lid for _, ids in ms_c11b.CFG['recognition'] for lid in ids]
        self.assertEqual(rec, ['L-0604', 'L-0678'])
        for lid in rec:
            self.assertIn('recognition', rows[lid]['Kata-Kata place'])
        self.assertEqual(ms_c11a.CFG['recognition'], [])
        # Every core row carries its Kata-Kata chapter 11 card.
        cards = {c['id'] for c in self.pack['cards']}
        for lid in ms_c11a.CORE + ms_c11b.CORE + rec:
            self.assertIn(rows[lid]['Kata-Kata (card IDs)'], cards, lid)

    def test_every_core_word_is_used(self):
        """All 41 chapter 11 core words appear in their unit outside the vocabulary list, and each is tested or practised."""
        for u in UNITS:
            text = ' | '.join(s.lower() for s in spans(self.all_lines((u,), skip_vocab=True)))
            for lid in CFGS[u]['core']:
                form = self.ledger.row(lid)['Malay'].lower()
                self.assertRegex(text, r'(?<![a-z])' + re.escape(form) + r'(?![a-z])', (u, lid, form))

    def test_revision_words_really_return(self):
        for u in UNITS:
            text = ' '.join(' '.join(re.findall(r'[a-z]+(?:-[a-z]+)*', s.lower())) for s in spans(self.all_lines((u,), skip_vocab=True)))
            for _, ids in CFGS[u]['revision']:
                for lid in ids:
                    forms = [re.sub(r'\([^)]*\)', '', f).strip().lower() for f in self.ledger.row(lid)['Malay'].split('/')]
                    self.assertTrue(any(re.search(r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', text) for f in forms), (u, lid, forms))

    def test_men_rule(self):
        """meN- verbs: each is its own ledger row placed at or before chapter 11 and shown with its root; no suffixed form."""
        checker = self.ledger.checker
        for w in set(self.words(self.all_lines())):
            if w in LOOKALIKE:
                continue
            if re.match(r'^me(m|n|ng|ny|nge)?[a-z]{3,}', w) and not re.match(r'^(mesyuarat|mereka|melayu)', w):
                ch = [r['_chapter'] for r in checker.entries.get(w, []) if r['_chapter'] is not None]
                self.assertTrue(ch and min(ch) <= 11, f'«{w}» is not a ledger row placed by chapter 11')
            self.assertFalse(re.fullmatch(r'[a-z]{3,}kan', w) and w not in ('makan', 'ikan', 'bukan', 'akan', 'jangan'), w)
            self.assertFalse(re.fullmatch(r'ber[a-z]{3,}', w) and w not in LOOKALIKE and
                             not [r for r in checker.entries.get(w, []) if r['_chapter'] is not None and r['_chapter'] <= 10], w)
        for u in UNITS:
            mod = ms_c11a if u == 'ms-c11a' else ms_c11b
            entries = self.lines(self.comp(u, 'Vocabulary'))
            for lid, (root, where, change, change_ja, passive) in mod.ROOTS.items():
                entry = next(x for x in entries if x.endswith(f'[{lid}]'))
                self.assertIn('‹meN-› + ' + root, entry, lid)
                self.assertIn(change, entry, lid)
                if passive:
                    self.assertIn('passive ' + passive, entry, lid)
                else:
                    self.assertNotIn('passive', entry, lid)
        # The spelling rule is taught in 11A (P1) and completed in 11B (P3), and summarised in the fast pack.
        p1 = ' '.join(self.lines(self.comp('ms-c11a', 'Pattern and grammar'), 'Pattern 1'))
        for w in ('‹mem-› before b', '‹men-› before c, d', '‹meng-› before h or a vowel', '‹me-› before l and m', 'With t and p the first sound drops out'):
            self.assertIn(w, p1, w)
        p3 = ' '.join(self.lines(self.comp('ms-c11b', 'Pattern and grammar'), 'Pattern 3'))
        for w in ('s drops and ‹meny-› is used', 'k drops and ‹meng-› is used', '‹menge-›', '‹me-› before l, m, n, r, w and y', 'mem-'):
            self.assertIn(w, p3, w)
        self.assertIn('‹menge-› before a one-syllable root', ' '.join(self.lines(self.by_unit['ms-c11-fast'][0])))
        # The nasal-change traps from the cards are in the teacher notes as starred plain text, never as taught Malay.
        notes = ' '.join(ms_c11a.CFG['teacher_notes'] + ms_c11b.CFG['teacher_notes'])
        for w in ('*mempanggil', '*mensewa', '*mengcas', '*mensapu', '‹menyapu›', 'ms-c11-013', 'ms-c11-021', 'ms-c11-041', 'ms-c11-027'):
            self.assertIn(w, notes, w)
        # Requests take the plain root: «Tolong semak draf ini», never «Tolong menyemak».
        all_text = ' '.join(self.all_lines())
        self.assertNotRegex(all_text, r'(?<!\*)«[^»]*[Tt]olong (menyemak|membaca|menulis|menghantar)')

    def test_katakata_alignment(self):
        """Same frames f01 to f06, same scenes (emails and files; the draft and the weekend), card IDs cited."""
        frames = {f['id']: f for f in self.pack['frames']}
        self.assertEqual(sorted(frames), [f'ms-c11-f0{n}' for n in range(1, 7)])
        self.assertEqual(ms_c11a.CFG['pattern_ids'], ['ms-c11-f01', 'ms-c11-f02', 'ms-c11-f03', 'ms-c11-f05'])
        self.assertEqual(ms_c11b.CFG['pattern_ids'], ['ms-c11-f04', 'ms-c11-f06', 'ms-c11-f01', 'ms-c11-f03'])
        text = ' '.join(self.all_lines())
        for f in frames.values():
            self.assertIn(f['example'], text, f['id'])
        # Every Kata-Kata scenario line, word for word, in the units (11A: s01 to s08; 11B: s09 to s18).
        a = ' '.join(self.all_lines(('ms-c11a',)))
        b = ' '.join(self.all_lines(('ms-c11b',)))
        lines = self.pack['scenario']['lines']
        self.assertEqual(len(lines), 18)
        for line in lines:
            n = int(line['id'][-2:])
            self.assertIn(line['ms'], a if n <= 8 else b, line['id'])
        for u, first, last in (('ms-c11a', 's01', 's08'), ('ms-c11b', 's09', 's18')):
            plan = ' '.join(self.lines(self.comp(u, 'Teaching plan')))
            self.assertIn(f'ms-c11-{first}', plan)
            self.assertIn(f'ms-c11-{last}', plan)
        self.assertEqual({sp for sp, _ in ms_c11a.DIALOGUE}, {'Aini', 'Tanaka', 'Rahman'})
        self.assertEqual({sp for sp, _ in ms_c11b.DIALOGUE}, {'Mei Ling', 'Tanaka'})
        # The traps the Kata-Kata cards name are in the teacher notes, with the card IDs.
        notes_a = ' '.join(ms_c11a.CFG['teacher_notes'])
        notes_b = ' '.join(ms_c11b.CFG['teacher_notes'])
        for w in ('«memanggil», not *mempanggil (card ms-c11-013)', 'ms-c11-015', 'ms-c11-017', 'ms-c11-014', 'ms-c11-003'):
            self.assertIn(w, notes_a, w)
        for w in ('«menyewa», not *mensewa (card ms-c11-021)', 'ms-c11-030', 'ms-c11-038', 'ms-c11-032', 'ms-c11-022', 'ms-c11-042', 'ms-c11-043'):
            self.assertIn(w, notes_b, w)
        self.assertIn('Where Japanese learners usually slip', notes_a)
        self.assertIn('Where Japanese learners usually slip', notes_b)

    def test_spoken_partners_are_recognition_only(self):
        """«tukar» and «deadline» are spoken partners: recognised, labelled spoken, never produced in a key or a test."""
        pat = r'(?<![a-z])(tukar|deadline)(?![a-z])'
        for u in UNITS + ('ms-c11-fast',):
            for l in self.by_unit[u]:
                for t in l['suite']['tests']:
                    self.assertNotRegex(t['answer_key'].lower(), pat, t['id'])
                    self.assertNotRegex(t['prompt'].lower(), r'«[^»]*' + pat, t['id'])
                for line in self.lines(l) + l['key']:
                    for s in re.findall(r'«([^»]*)»', line):
                        if re.search(pat, s.lower()):
                            self.assertRegex(line, r'(?i)spoken|speech|話し言葉|recognise|recognition|聞いて分か|chat|チャット', (l['title'], line))
        for cfg in CFGS.values():
            for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']:
                self.assertNotRegex(s.lower(), pat)
            for key in cfg['drill_keys'].values():
                for line in key:
                    for sp in re.findall(r'«([^»]*)»', line):
                        self.assertNotRegex(sp.lower(), pat)

    def test_register_particles_and_scope(self):
        text = ' '.join(self.all_lines())
        # The vocabulary lists show ledger headwords such as «sudah / dah» (spoken, labelled); everything else is checked.
        words = self.words(self.all_lines(skip_vocab=True))
        for w in ('lah', 'kan', 'tak', 'dah', 'tapi', 'takpe', 'ni', 'tu', 'kat', 'jom'):
            self.assertNotIn(w, words, w)
        for w in ('bersepeda', 'antre', 'berwisata', 'berbicara', 'kantor', 'olahraga'):
            self.assertNotIn(w, words, w)
        self.assertNotRegex(text.lower(), r'assalam|waalaikum|insya|alhamdulillah|bismillah')
        # «nak» (spoken «mahu») appears only where it is labelled spoken, and never in a key or a dialogue.
        for cfg in CFGS.values():
            for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']:
                self.assertNotIn('nak', malay_words_of(s))

    def test_components_patterns_and_minimums(self):
        required = {'Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                    'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan'}
        for u in UNITS:
            cfg = CFGS[u]
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
                      '«berapa lama»', '«siapa» with «oleh»', 'Chapters 1 to 11', 'Chapter 11 adds no new question word'):
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
            for w in ('Block E · Scene transfer', 'Sedia Kelas c11', 'not yet tagged by chapter', '0–5'):
                self.assertIn(w, plan + ' '.join(n for n, _, _ in self.comp(u, 'Teaching plan')['sections']), (u, w))

    def test_openers(self):
        for u in UNITS:
            opener = self.comp(u, 'Opener')
            body = ' '.join(self.lines(opener))
            self.assertIn(f'Sedia Kelas c11 ({katakata_ref.sedia_count(11)} cards, frames ms-c11-f01 and ms-c11-f02)', body)
            self.assertIn(f'（カード{katakata_ref.sedia_count(11)}枚、文型 f01・f02）', body)
        self.assertIn('ms-c11-001 to ms-c11-020', ' '.join(self.lines(self.comp('ms-c11a', 'Opener'))))
        self.assertIn('ms-c11-021 to ms-c11-043', ' '.join(self.lines(self.comp('ms-c11b', 'Opener'))))

    def test_japanese_has_no_leftover_english(self):
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Sedia Kelas|Tanya Cikgu|Susun Ayat|Dunia|\bber-|\bmeN-|\*[a-z]+')
        for cfg in CFGS.values():
            cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
            cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
            cells += [cfg['role_a'][-1], cfg['role_b'][-1], cfg['change'][-1], cfg['markers']['bridge'][-1].split(' / ')[-1]]
            cells += [o['ja'] for o in cfg['vocab_opts'].values() if 'ja' in o]
            for ja in cells:
                self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
                self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_review_block(self):
        """Review 1 after unit 11B (plan section 1): chapters 10 and 11 with the Stage 1 passive and the markers; no new word."""
        l = self.comp('ms-c11b', 'Reading and writing', slug='review-block')
        self.assertEqual(l['suite']['block'], 'Skills')
        self.assertEqual(l['suite']['time_minutes'], 45)
        names = ' '.join(n for n, _, _ in l['sections'])
        for part in ('Model', 'Plan', 'Your turn', 'Peer check'):
            self.assertIn(part, names)
        plan = ' '.join(self.lines(l, 'Plan'))
        for t in ('0–5', '5–15', '15–30', '30–40', '40–45'):
            self.assertIn(t, plan)
        self.assertIn('review block after unit 11B', ' '.join(l['key']))
        # The review has no new word: every Malay word in it is in a ledger row placed at or before chapter 11.
        words = self.words(self.lines(l) + l['key'])
        checker = self.ledger.checker
        for w in set(words):
            if w in LOOKALIKE or w in NAMES:
                continue
            ch = [r['_chapter'] for r in checker.entries.get(w, []) if r['_chapter'] is not None]
            self.assertTrue(ch and min(ch) <= 11, w)

    def test_fast_pack(self):
        l = self.by_unit['ms-c11-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertEqual(len(core), 20)
        self.assertTrue(set(fast.C11_WORDS) <= set(ms_c11a.CORE + ms_c11b.CORE))
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
        self.assertIn(f'all {katakata_ref.card_count(11)} Kata-Kata chapter 11 cards (ms-c11-001 to ms-c11-{katakata_ref.last_own_card(11):03}', guide)

    def test_registration_and_catalogue(self):
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in UNITS + ('ms-c11-fast',):
            self.assertIn(u, reauthored)
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 30)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'].startswith('ms-c11')])
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch11 = next(c for c in chapters if c['title'].startswith('Chapter 11'))
        self.assertEqual([u['label'] for u in ch11['units']], ['11A', '11B'])
        self.assertEqual((ch11['level'], ch11['sequence']), ('A2', 'stage2'))
        self.assertTrue(ch11['fast_items'])
        catalogue = make_catalogue(bank(), chapters)
        c11 = next(c for c in catalogue['chapters'] if c['id'] == 'ms-c11')
        self.assertEqual((c11['level'], c11['stage_id']), ('A2', 'ms-stage2'))
        self.assertEqual([u['id'] for u in c11['units']], ['ms-c11a', 'ms-c11b'])
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('chapter_id') == 'ms-c11']
        self.assertTrue(mine and all(c['level'] == 'A2' for c in mine))
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage2-review-11b')
        self.assertEqual(block['component_ids'], ['ms-c11b-review-block'])
        old = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage2-writing-10b')
        self.assertEqual(old['component_ids'], ['ms-c10b-writing-block'])


if __name__ == '__main__':
    unittest.main()
