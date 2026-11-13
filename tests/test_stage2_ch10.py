"""Stage 2 build step 4: chapter 10 (units 10A and 10B, ber- verbs), the writing block after 10B and the chapter 10 fast
pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the ledger (40 core rows placed
"Ch10 (unit 10A)" or "Ch10 (unit 10B)", L-0667 «pindah» as the one recognition row), every core word used outside the
vocabulary list, the ber- rule (every ber-shaped word is its own ledger row placed at or before chapter 10; no meN-, -kan
or -i form), alignment with Kata-Kata c10 (frames f01 to f06, the scenario lines, card IDs), the charter section 6 and 14
minimums, the traps the Kata-Kata cards name, «pindah» kept to recognition, «lah» and «kan» never in a key, and the
registration of the units. The checks are written so that chapters 11 to 17 can copy this file and change the chapter.
"""
import json
import re
import unittest
from pathlib import Path

from tests import katakata_ref
from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c10a, ms_c10b, fast
from catalogue import make_catalogue
from language_checks import placed_chapter

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
UNITS = ('ms-c10a', 'ms-c10b')
CFGS = {'ms-c10a': ms_c10a.CFG, 'ms-c10b': ms_c10b.CFG}
# Marked words that look like ber- or meN- forms but are roots or Stage 1 whole words.
LOOKALIKE = {'berapa', 'bersih', 'besar', 'berat', 'belum', 'belajar', 'bekas', 'beli', 'bengkak', 'beg', 'bekerja', 'berehat',
             'merah', 'meter', 'mengapa', 'menu', 'melayu', 'mesyuarat', 'mereka', 'mesej', 'mesti', 'mei', 'meja', 'merokok'}


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch10_rows(rows, unit):
    """Core rows the ledger places in the unit (not the recognition row)."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(rf'Ch10 \(unit {unit}\)$', r['Kata-Kata place'])}


def spans(lines):
    return [s for line in lines for s in re.findall(r'«([^»]*)»', line)]


class Chapter10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.pack = json.loads((ROOT / 'curriculum/reference/katakata/c10.json').read_text())

    def comp(self, u, typ, sub=None, slug=None):
        found = [l for l in self.by_unit[u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)
                 and (slug is None or l['suite']['id'].endswith('-' + slug))]
        self.assertTrue(found, f'missing {u} {typ}/{sub}/{slug}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def all_lines(self, units=UNITS + ('ms-c10-fast',), skip_vocab=False):
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
        for u, label in (('ms-c10a', '10A'), ('ms-c10b', '10B')):
            cfg = CFGS[u]
            self.assertEqual(len(cfg['core']), len(set(cfg['core'])))
            self.assertEqual(set(cfg['core']), ch10_rows(rows, label), u)
            self.assertEqual(len(cfg['core']), 20)
            self.assertEqual([lid for _, ids in cfg['core_groups'] for lid in ids], cfg['core'])
            for _, ids in cfg['revision']:
                for lid in ids:
                    self.assertLessEqual(placed_chapter(rows[lid]['Kata-Kata place']), 9, (u, lid))
                    self.assertNotIn(lid, cfg['core'])
        # 40 core rows for chapter 10 (plan section 2), the planned 233 + 7 = 240 across Stage 2 (build step 4 refresh).
        self.assertEqual(len(ch10_rows(rows, '10A') | ch10_rows(rows, '10B')), 40)
        stage2 = {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
                  and re.match(r'Ch1[0-7] \(unit \w+\)$', r['Kata-Kata place'])}
        self.assertEqual(len(stage2), 240)
        # The only recognition row is «pindah», the spoken partner of «berpindah».
        rec = [lid for _, ids in ms_c10b.CFG['recognition'] for lid in ids]
        self.assertEqual(rec, ['L-0667'])
        self.assertIn('recognition', rows['L-0667']['Kata-Kata place'])
        self.assertEqual(ms_c10a.CFG['recognition'], [])
        # Every core row carries its Kata-Kata chapter 10 card.
        cards = {c['id'] for c in self.pack['cards']}
        for lid in ms_c10a.CORE + ms_c10b.CORE + ['L-0667']:
            self.assertIn(rows[lid]['Kata-Kata (card IDs)'], cards, lid)

    def test_every_core_word_is_used(self):
        """All 40 chapter 10 core words appear in their unit outside the vocabulary list, and each is tested or practised."""
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

    def test_ber_rule(self):
        """ber- verbs: each is its own ledger row placed at or before chapter 10, shown with its root; no meN-, no -kan or -i."""
        checker = self.ledger.checker
        for w in set(self.words(self.all_lines())):
            if w in LOOKALIKE:
                continue
            if re.match(r'^(ber|be[kr]|bel)[a-z]{2,}', w):
                ch = [r['_chapter'] for r in checker.entries.get(w, []) if r['_chapter'] is not None]
                self.assertTrue(ch and min(ch) <= 10, f'«{w}» is not a ledger row placed by chapter 10')
            self.assertFalse(re.fullmatch(r'me[mnr]?[bcdfghjklmnpqrstvwyz][a-z]{2,}', w) and w not in LOOKALIKE, w)
            self.assertFalse(re.fullmatch(r'[a-z]{3,}kan', w) and w not in ('makan', 'ikan', 'bukan', 'akan', 'jangan'), w)
        for u in UNITS:
            v = ' '.join(self.lines(self.comp(u, 'Vocabulary')))
            mod = ms_c10a if u == 'ms-c10a' else ms_c10b
            for lid, root in mod.ROOTS.items():
                entry = next(x for x in self.lines(self.comp(u, 'Vocabulary')) if x.endswith(f'[{lid}]'))
                self.assertIn('‹ber-› + ' + root, entry, lid)
            self.assertIn('Core words', v)
        # The spelling rule is taught once, the same way in both units and the fast pack.
        p1 = ' '.join(self.lines(self.comp('ms-c10a', 'Pattern and grammar'), 'Pattern 1'))
        for w in ('no nasal sound changes', '‹be-›', '‹bel-›', '«belajar»', '«berehat»', '«bekerja»'):
            self.assertIn(w, p1, w)
        self.assertIn('‹bel-› only in «belajar»', ' '.join(self.lines(self.by_unit['ms-c10-fast'][0])))
        # Misspellings are shown as starred plain text, never as taught Malay.
        notes = ' '.join(ms_c10a.CFG['teacher_notes'])
        self.assertIn('*berrehat', notes)

    def test_katakata_alignment(self):
        """Same frames f01 to f06, same scenes (the working day with Puan Aini; the new neighbour Puan Siti), card IDs cited."""
        frames = {f['id']: f for f in self.pack['frames']}
        self.assertEqual(sorted(frames), [f'ms-c10-f0{n}' for n in range(1, 7)])
        self.assertEqual(ms_c10a.CFG['pattern_ids'], ['ms-c10-f01', 'ms-c10-f02', 'ms-c10-f03', 'ms-c10-f04'])
        self.assertEqual(ms_c10b.CFG['pattern_ids'], ['ms-c10-f05', 'ms-c10-f06', 'ms-c10-f04', 'ms-c10-f03'])
        text = ' '.join(self.all_lines())
        for f in frames.values():
            self.assertIn(f['example'], text, f['id'])
        # Every Kata-Kata scenario line is used in the units (10A: s01 to s09; 10B: s10 to s19).
        a = ' '.join(self.all_lines(('ms-c10a',)))
        b = ' '.join(self.all_lines(('ms-c10b',)))
        for line in self.pack['scenario']['lines']:
            n = int(line['id'][-2:])
            self.assertIn(line['ms'], a if n <= 9 else b, line['id'])
        for u, first, last in (('ms-c10a', 's01', 's09'), ('ms-c10b', 's10', 's19')):
            plan = ' '.join(self.lines(self.comp(u, 'Teaching plan')))
            self.assertIn(f'ms-c10-{first}', plan)
            self.assertIn(f'ms-c10-{last}', plan)
        self.assertEqual({sp for sp, _ in ms_c10a.DIALOGUE}, {'Aini', 'Tanaka'})
        self.assertEqual({sp for sp, _ in ms_c10b.DIALOGUE}, {'Siti', 'Tanaka'})
        # The traps the Kata-Kata cards name are in the teacher notes, with the card IDs.
        notes = ' '.join(ms_c10a.CFG['teacher_notes'])
        for w in ('«berhenti kerja» means to quit a job', 'ms-c10-015', '«bertolak» means to set off, not to push', 'ms-c10-020'):
            self.assertIn(w, notes, w)
        self.assertIn('ms-c10-032', ' '.join(ms_c10b.CFG['teacher_notes']))
        self.assertIn('Where Japanese learners usually slip', notes)
        self.assertIn('Where Japanese learners usually slip', ' '.join(ms_c10b.CFG['teacher_notes']))

    def test_pindah_is_recognition_only(self):
        """«pindah» is the spoken partner of «berpindah»: recognised, labelled spoken, never produced in a key or a test."""
        for u in UNITS + ('ms-c10-fast',):
            for l in self.by_unit[u]:
                for t in l['suite']['tests']:
                    self.assertNotRegex(t['answer_key'].lower(), r'(?<![a-z])pindah', t['id'])
                    self.assertNotRegex(t['prompt'].lower(), r'«[^»]*(?<![a-z])pindah', t['id'])
                for line in self.lines(l) + l['key']:
                    for s in re.findall(r'«([^»]*)»', line):
                        if re.search(r'(?<![a-z])pindah', s.lower()):
                            self.assertRegex(line, r'(?i)spoken|speech|話し言葉|recognise|聞いて分か', (l['title'], line))
        # Never in a dialogue, listening line or drill answer.
        for cfg in CFGS.values():
            for _, s in cfg['dialogue'] + cfg['variant'] + cfg['listening']:
                self.assertNotRegex(s.lower(), r'(?<![a-z])pindah')

    def test_register_particles_and_scope(self):
        text = ' '.join(self.all_lines())
        # The vocabulary lists show ledger headwords such as «sudah / dah» (spoken, labelled); everything else is checked.
        words = self.words(self.all_lines(skip_vocab=True))
        for w in ('lah', 'kan', 'tak', 'dah', 'nak', 'tapi', 'takpe', 'ni', 'tu', 'kat', 'jom'):
            self.assertNotIn(w, words, w)
        for w in ('bersepeda', 'antre', 'berwisata', 'berbicara', 'kantor', 'olahraga'):
            self.assertNotIn(w, words, w)
        self.assertNotRegex(text.lower(), r'assalam|waalaikum|insya|alhamdulillah|bismillah')
        # A learner never has to give real family details.
        notes = ' '.join(ms_c10b.CFG['teacher_notes'])
        self.assertIn('never has to give real marital or family details', notes)
        self.assertIn('persona', ' '.join(ms_c10b.CFG['role_a']))

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
                      '«berapa lama»', '«siapa» with «oleh»', 'Chapters 1 to 10', 'Chapter 10 adds no new question word'):
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
            for w in ('Block E · Scene transfer', 'Sedia Kelas c10', 'not yet tagged by chapter', '0–5'):
                self.assertIn(w, plan + ' '.join(n for n, _, _ in self.comp(u, 'Teaching plan')['sections']), (u, w))

    def test_openers(self):
        for u in UNITS:
            opener = self.comp(u, 'Opener')
            body = ' '.join(self.lines(opener))
            self.assertIn(f'Sedia Kelas c10 ({katakata_ref.sedia_count(10)} cards, frames ms-c10-f01 and ms-c10-f02)', body)
            self.assertIn(f'（カード{katakata_ref.sedia_count(10)}枚、文型 f01・f02）', body)
        self.assertIn('ms-c10-001 to ms-c10-020', ' '.join(self.lines(self.comp('ms-c10a', 'Opener'))))
        self.assertIn('ms-c10-021 to ms-c10-041', ' '.join(self.lines(self.comp('ms-c10b', 'Opener'))))

    def test_japanese_has_no_leftover_english(self):
        strip = re.compile(r'«[^»]*»|‹[^›]*›|ms-c\d\d-\S+|L-\d{4}|Kata-Kata|Sedia Kelas|Tanya Cikgu|Susun Ayat|\bber-|\bmeN-|\*[a-z]+')
        for cfg in CFGS.values():
            cells = list(cfg['goals_ja'].values()) + cfg['culture_ja'] + [cfg['setting_ja']]
            cells += [p[4] for p in cfg['patterns']] + [p[6] for p in cfg['patterns']]
            cells += [cfg['role_a'][-1], cfg['role_b'][-1], cfg['change'][-1], cfg['markers']['bridge'][-1].split(' / ')[-1]]
            cells += [o['ja'] for o in cfg['vocab_opts'].values() if 'ja' in o]
            for ja in cells:
                self.assertTrue(re.search(r'[ぁ-んァ-ン一-龥]', ja), ja)
                self.assertFalse(re.search(r'[A-Za-z]{3,}', strip.sub('', ja)), ja)

    def test_writing_block(self):
        l = self.comp('ms-c10b', 'Reading and writing', slug='writing-block')
        self.assertEqual(l['suite']['block'], 'Skills')
        self.assertEqual(l['suite']['time_minutes'], 45)
        names = ' '.join(n for n, _, _ in l['sections'])
        for part in ('Model', 'Plan', 'Your turn', 'Peer check'):
            self.assertIn(part, names)
        plan = ' '.join(self.lines(l, 'Plan'))
        for t in ('0–5', '5–15', '15–30', '30–40', '40–45'):
            self.assertIn(t, plan)
        self.assertIn('invented persona', ' '.join(l['key']))

    def test_fast_pack(self):
        l = self.by_unit['ms-c10-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertEqual(len(core), 20)
        self.assertTrue(set(fast.C10_WORDS) <= set(ms_c10a.CORE + ms_c10b.CORE))
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
        self.assertIn(f'all {katakata_ref.card_count(10)} Kata-Kata chapter 10 cards (ms-c10-001 to ms-c10-{katakata_ref.last_own_card(10):03}', guide)

    def test_registration_and_catalogue(self):
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in UNITS + ('ms-c10-fast',):
            self.assertIn(u, reauthored)
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 20)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'].startswith('ms-c10')])
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch10 = next(c for c in chapters if c['title'].startswith('Chapter 10'))
        self.assertEqual([u['label'] for u in ch10['units']], ['10A', '10B'])
        self.assertEqual((ch10['level'], ch10['sequence']), ('A2', 'stage2'))
        self.assertTrue(ch10['fast_items'])
        catalogue = make_catalogue(bank(), chapters)
        c10 = next(c for c in catalogue['chapters'] if c['id'] == 'ms-c10')
        self.assertEqual((c10['level'], c10['stage_id']), ('A2', 'ms-stage2'))
        self.assertEqual([u['id'] for u in c10['units']], ['ms-c10a', 'ms-c10b'])
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('chapter_id') == 'ms-c10']
        self.assertTrue(mine and all(c['level'] == 'A2' for c in mine))
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage2-writing-10b')
        self.assertEqual(block['component_ids'], ['ms-c10b-writing-block'])


if __name__ == '__main__':
    unittest.main()
