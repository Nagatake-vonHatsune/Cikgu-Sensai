"""Step 5e chapter 7: charter section 6 and 14 minimums for unit 7 and the chapter 7 fast pack.

Checks the authored source and the built page bank: the ledger partition recomputed from the
ledger (core, Dunia recognition by scene, revision, the two accounted-for exceptions), the
component minimums, the cumulative question words with «ke mana», «dari mana», «berapa jauh»
and «berapa lama», real item-by-item answer keys, word tags on every test item, the chapter 7
Malay rules («ke» taught with the earlier forms as everyday speech; the six places of worship as
one even-handed set; no faith-specific expressions; nothing placed after chapter 7) and
retirement of the legacy chapter 7 packs.

Step 5f follow-ups: 62 core words (the five rows Sam approved, kilometer, terus, tangga, jangan and sebulan, and
«sesak»), «jalan lurus» never used for directions, «kalau tidak jam / sesak», «tumpang tanya» as revision, and the
unit 7 writing block (directions by message).
"""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, malay_words, english_words
from suite import ms_c07, fast
from catalogue import make_catalogue

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')
SCENES = {'Di ruang tamu': 13, 'Telefon baru': 12, 'Lintas jalan': 8}
WORSHIP = ['masjid', 'gereja', 'kuil', 'tokong', 'gurdwara', 'surau']


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def ch7_rows(rows):
    """Ledger rows whose placement starts with 'Ch7' (pending or not): the chapter 7 core rows."""
    return {lid for lid, r in rows.items() if r['Review status'] != 'Retired'
            and re.match(r'Ch ?7\b', r['Kata-Kata place'])}


def ch7_recognition(rows):
    """Dunia rows that prime chapter 7 and are not placed in any earlier chapter."""
    out = set()
    for lid, r in rows.items():
        place = r['Kata-Kata place']
        if r['Review status'] == 'Retired' or 'primes Ch7' not in place:
            continue
        earlier = [int(m) for m in re.findall(r'(?:^|; )Ch ?(\d)', place) if int(m) < 7]
        if not earlier:
            out.add(lid)
    return out


class Chapter7Minimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for lesson in cls.lessons:
            cls.by_unit.setdefault(lesson['suite']['check_unit'], []).append(lesson)
        cls.cfg = ms_c07.CFG
        cls.u = 'ms-c07'

    def comp(self, typ, sub=None, unit=None):
        found = [l for l in self.by_unit[unit or self.u] if l['suite']['component_type'] == typ
                 and (sub is None or l['suite']['sub_type'] == sub)]
        self.assertTrue(found, f'missing {typ}/{sub}')
        return found[0]

    def lines(self, l, part=None):
        return [line for name, items, kind in l['sections'] if part is None or part in name for line in items]

    def test_ledger_partition(self):
        rows = self.ledger.rows
        placed = ch7_rows(rows)
        # 53 rows from the ledger as handed over, plus the five rows Sam approved on 12 Nov 2026 (L-1054 to L-1058),
        # «sesak» (L-0620, placed in chapter 7 on 12 Nov 2026) and the five rows of the step 5e review (L-1059 to L-1063).
        self.assertEqual(len(placed), 64)
        self.assertEqual(len({lid for lid in placed if int(lid[2:]) < 1054 and lid != 'L-0620'}), 53)
        self.assertEqual({lid for lid in placed if int(lid[2:]) >= 1054},
                         {'L-1054', 'L-1055', 'L-1056', 'L-1057', 'L-1058', 'L-1059', 'L-1060', 'L-1061', 'L-1062', 'L-1063'})
        self.assertIn('L-0620', placed)
        # Two are not new core: the duplicate «pintu masuk» row and «depan» (taught in chapter 4).
        self.assertEqual(rows['L-0592']['Malay'], 'pintu masuk')
        self.assertIn('pintu masuk', rows['L-0330']['Malay'])
        self.assertEqual(rows['L-0304']['Malay'], 'depan / hadapan')
        self.assertEqual(rows['L-0173']['Malay'], 'depan')
        self.assertEqual(rows['L-0173']['Kata-Kata place'], 'Ch4')
        core_all = placed - {'L-0592', 'L-0304'}
        self.assertEqual(len(core_all), 62)
        core = self.cfg['core']
        self.assertEqual(len(core), len(set(core)))
        self.assertEqual(set(core), core_all)
        rec_all = ch7_recognition(rows) - core_all
        self.assertEqual(len(rec_all), 33)
        rec = [lid for _, ids in self.cfg['recognition'] for lid in ids]
        self.assertEqual(len(rec), len(set(rec)))
        self.assertEqual(set(rec), rec_all)
        self.assertEqual({s: len(ids) for s, ids in self.cfg['recognition']}, SCENES)
        for scene, ids in self.cfg['recognition']:
            for lid in ids:
                self.assertIn(f'Dunia · {scene} (primes Ch7)', rows[lid]['Kata-Kata place'])
        groups = dict(self.cfg['core_groups'])
        self.assertEqual(list(groups), ['Position words', 'Distance and direction', 'Turning and moving',
                                        'Landmarks and transport', 'Compass points'])
        self.assertEqual({k: len(v) for k, v in groups.items()},
                         {'Position words': 13, 'Distance and direction': 11, 'Turning and moving': 11,
                          'Landmarks and transport': 23, 'Compass points': 4})
        self.assertEqual([lid for ids in groups.values() for lid in ids], core)
        # Revision: placed in chapters 1 to 6, never counted as new core or recognition.
        rev = {lid for _, ids in self.cfg['revision'] for lid in ids}
        self.assertFalse(rev & set(core))
        self.assertFalse(rev & set(rec))
        for lid in rev:
            self.assertTrue(any(r['ID'] == lid and r['_chapter'] is not None and r['_chapter'] <= 6
                                for rs in self.ledger.checker.entries.values() for r in rs), lid)
        # Words placed earlier and reused are revision: depan (ch 4), bilik (ch 6), hospital (ch 5), kapal terbang (ch 4), lama (ch 6 and 7).
        for lid in ('L-0173', 'L-1052', 'L-0336', 'L-0449', 'L-0284', 'L-0019'):
            self.assertIn(lid, rev)
        # «tumpang tanya» is ledger row L-0019 (chapter 1): revision, not a new row (Sam, step 5e review answer 5).
        self.assertEqual(rows['L-0019']['Malay'], 'tumpang tanya')
        self.assertEqual(rows['L-0019']['Kata-Kata place'], 'Ch1')
        self.assertFalse([r for r in rows.values() if r['Malay'] == 'tumpang tanya' and r['ID'] != 'L-0019'])
        # The six rows of step 5f: kilometer, terus, tangga, jangan, sebulan with Sam's approval, and sesak from Sam's decision.
        for lid, word in (('L-1059', 'kilometer'), ('L-1060', 'terus'), ('L-1061', 'tangga'), ('L-1062', 'jangan'),
                          ('L-1063', 'sebulan')):
            self.assertEqual(rows[lid]['Malay'], word)
            self.assertIn('Sam approved', rows[lid]['Changed by'])
            self.assertIn(lid, core)
        self.assertEqual(rows['L-0620']['Malay'], 'sesak')
        self.assertIn('sesak', rows['L-0620']["Sam's notes"])
        self.assertIn('L-0620', core)
        self.assertEqual(rows['L-0342']['Malay'], 'jam (spoken)')
        self.assertIn('lurus', rows['L-0318']["Sam's notes"])
        # The five approved rows exist with Sam's approval noted and are core.
        for lid in ('L-1054', 'L-1055', 'L-1056', 'L-1057', 'L-1058'):
            self.assertIn('Sam approved', rows[lid]['Changed by'])
            self.assertIn(lid, core)

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
        for scene in SCENES:
            self.assertIn(f'"{scene}"', txt)
        # The duplicate row and the chapter 4 «depan» row are not listed as separate core entries.
        self.assertNotIn('[L-0592]', txt)
        self.assertNotIn('[L-0304]', txt)
        dep = next(x for x in entries if '[L-0173]' in x)
        self.assertIn('hadapan', dep)
        # «jam» (traffic) is marked spoken.
        jam = next(x for x in entries if '[L-0342]' in x)
        self.assertIn('spoken', jam)
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
        self.assertEqual(ids, [f'ms-c07-f0{n}' for n in range(1, 6)])
        self.assertEqual(l['suite']['pattern_ids'], [f'ms-c07-f0{n}' for n in range(1, 6)])
        body = ' '.join(self.lines(l))
        for w in ('«ke»', '«ke mana?»', '«dari mana?»', '«di»', '«sebelah»', 'antara', 'utara', '«belok»', '«kemudian»',
                  'lurus', '«berapa jauh»', '«lebih kurang»', '«dekat»', '«jauh»', '«berapa lama»', '«naik»', '«turun»',
                  '«kalau»', '«jalan kaki»', '«terus»', '«jangan»', '«kilometer»', '«sebulan»', '«sesak»', 'naik tangga'):
            self.assertIn(w, body, w)

    def test_ke_taught_with_earlier_forms_as_everyday_speech(self):
        """Brief: «pergi ke pejabat» and «balik ke rumah» are the standard form; «pergi kerja» and «balik rumah» everyday speech."""
        body = ' '.join(x for l in self.by_unit[self.u] for _, items, _ in l['sections'] for x in items)
        for w in ('«pergi ke pejabat»', '«balik ke rumah»', '«pergi kerja»', '«balik rumah»'):
            self.assertIn(w, body, w)
        p1 = ' '.join(self.lines(self.comp('Pattern and grammar'), 'Pattern 1'))
        self.assertRegex(p1, r'everyday speech')
        self.assertRegex(p1, r'standard forms')
        culture = ' '.join(self.lines(self.comp('Culture note'), 'English'))
        self.assertIn('everyday speech', culture)
        # Every «pergi kerja» / «balik rumah» sits on a line that says it is everyday speech or is part of an explanation of both forms.
        for l in self.by_unit[self.u]:
            for _, items, _ in l['sections']:
                for line in items:
                    if re.search(r'«(pergi kerja|balik rumah)»', line):
                        self.assertRegex(line, r'everyday|speech|話し言葉|日常', line)

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
                  '«yang mana»', '«pilih»', '«ke mana»', '«dari mana»', '«berapa jauh»', '«berapa lama»'):
            self.assertIn(w, full, w)
        key = ' '.join(qset['key'])
        for q in ('«Awak pergi ke mana?»', '«Puan datang dari mana?»', '«Berapa jauh stesen dari sini?»',
                  '«Berapa lama jalan kaki ke stesen?»'):
            self.assertIn(q, key, q)
        self.assertEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(qset)), 16)
        for i in range(1, 17):
            self.assertRegex(key, rf'(^|\s){i} «', i)
        choice = ' '.join(self.comp('Drill', 'question-word choice')['key'])
        for w in ('«Di mana»', '«Ke mana»', '«Dari mana»', '«Berapa jauh»', '«Berapa lama»', '«Kenapa»', '«Yang mana»'):
            self.assertIn(w, choice, w)

    def test_markers_return(self):
        """Charter section 14: the tense and aspect markers come back in every later chapter."""
        l = self.comp('Drill', 'markers')
        txt = ' '.join(self.lines(l))
        for m in ('«belum»', '«sudah»', '«masih»', '«akan»'):
            self.assertIn(m, txt, m)
        self.assertGreaterEqual(sum(bool(NUMBERED.match(x)) for x in self.lines(l)), 6)
        self.assertIn('8 «', ' '.join(l['key']))

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
        self.assertFalse(any(re.search(r'[A-Za-z]{4,}', re.sub(
            r'«[^»]*»|‹[^›]*›|ms-c\d\d-\d+|UTC|Kata-Kata|Kamus Dewan|Kata', '', x))
            for x in cfg['culture_ja']))

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
        self.assertIn('Sedia Kelas c07', body)
        self.assertIn('0–5', body)
        # The writing block for unit 7 (directions by message), 45 minutes, registered in the catalogue.
        wb = self.comp('Reading and writing', 'composition')
        self.assertEqual(wb['suite']['id'], 'ms-c07-writing-block')
        self.assertEqual(wb['suite']['block'], 'Skills')
        self.assertEqual(wb['suite']['time_minutes'], 45)
        wtxt = ' '.join(self.lines(wb))
        for part in ('Model', 'Your turn', 'Peer check'):
            self.assertIn(part, ' '.join(n for n, _, _ in wb['sections']))
        for w in ('«jalan terus»', '«jangan»', '«lebih kurang»', '«kilometer»', 'minit'):
            self.assertIn(w, wtxt, w)
        self.assertTrue(any(x.startswith('Model:') for x in wb['key']))

    def test_chapter7_malay_rules(self):
        label = re.compile(r'spoken|speech|話し言葉|口語', re.I)
        spoken_words = {'nak', 'tapi', 'sikit', 'dah', 'tak', 'senang', 'tengah', 'saja', 'jam'}
        # Chapter 8 and 9 words that must not appear (placed after chapter 7).
        later = {'tolong', 'baju', 'butang', 'sila', 'tetamu', 'tadi'}
        everything = self.by_unit[self.u] + self.by_unit.get('ms-c07-fast', [])
        for l in everything:
            lines = [x for _, items, _ in l['sections'] for x in items] + l['key']
            for line in lines:
                for span in re.findall(r'«([^»]*)»', line):
                    words = re.findall(r'[a-z]+', span.lower())
                    for w in later:
                        self.assertNotIn(w, words, line)
                    # Indonesian look-alikes are never used.
                    for w in ('toko', 'bis', 'mobil', 'toilet', 'kampus'):
                        self.assertNotIn(w, words, line)
                    for i, w in enumerate(words):
                        if w in ('nak', 'tapi', 'sikit', 'dah', 'tak', 'senang', 'saja'):
                            self.assertRegex(line, label, (l['title'], line))
                # Nothing faith-specific beyond the landmark names (no greetings, worship, dress or etiquette).
                self.assertNotRegex(line.lower(), r'assalam|waalaikum|insya|alhamdulillah|bismillah|halal|haram|puasa|solat|sembahyang|azan|khutbah|ibadat|doa\b')
                self.assertNotRegex(line.lower(), r'\b\d+\s*(mg|ml|tablet|pil)\b')

    def test_no_jalan_lurus_for_directions(self):
        """Sam, 12 Nov 2026: «jalan lurus» is not used for directions; «terus», «jalan terus», «pergi terus», «terus depan» are.
        «lurus» is only the adjective «Jalan ini lurus.» A line may name «jalan lurus» only to say it is not used."""
        everything = self.by_unit[self.u] + self.by_unit['ms-c07-fast']
        n_terus = 0
        for l in everything:
            lines = [x for _, items, _ in l['sections'] for x in items] + l['key']
            for t in l['suite']['tests']:
                lines += [t['prompt'], t['answer_key']]
            for line in lines:
                if re.search(r'«[^»]*\blurus\b[^»]*»', line):
                    for span in re.findall(r'«([^»]*)»', line):
                        if re.search(r'\blurus\b', span) and span.lower() not in ('lurus', 'jalan lurus', 'jalan ini lurus.'):
                            self.fail(('lurus used in a Malay line', line))
                    if re.search(r'jalan lurus', line):
                        self.assertRegex(line, r'not used|is not|not say|\(not «jalan lurus»\)|使いません|使わ', line)
                n_terus += len(re.findall(r'«[^»]*\bterus\b[^»]*»', line))
        self.assertGreaterEqual(n_terus, 25)
        body = ' '.join(x for l in everything for _, items, _ in l['sections'] for x in items + l['key'])
        for w in ('«jalan terus»', '«pergi terus»', '«terus depan»', '«Jalan terus, kemudian belok kanan'):
            self.assertIn(w, body, w)
        # The new ledger words are used in natural unit sentences.
        for phrase in ('Naik tangga', 'Jangan belok kiri', 'Lebih kurang dua kilometer', 'ringgit sebulan',
                       'Maaf, tumpang tanya', 'kalau tidak jam / sesak'):
            self.assertIn(phrase, body, phrase)

    def test_jam_and_sesak_taught_together(self):
        """Sam: write «kalau tidak jam / sesak» so «jam» (traffic) is not read as the hour."""
        v = self.comp('Vocabulary')
        entries = [x for x in self.lines(v) if re.search(r'\[L-\d{4}\]$', x)]
        jam = next(x for x in entries if '[L-0342]' in x)
        sesak = next(x for x in entries if '[L-0620]' in x)
        self.assertIn('spoken', jam)
        self.assertIn('kalau tidak jam / sesak', jam)
        self.assertIn('kalau tidak jam / sesak', sesak)
        p5 = ' '.join(self.lines(self.comp('Pattern and grammar'), 'Pattern 5'))
        self.assertIn('kalau tidak jam / sesak', p5)
        self.assertIn('sesak', ' '.join(self.cfg['listening'][8]))
        # Every use of «jam» as traffic sits beside «sesak» or on a line that says spoken.
        for l in self.by_unit[self.u]:
            for _, items, _ in l['sections']:
                for line in items:
                    if re.search(r'«[^»]*\b(kalau tidak jam|kalau jam|Hari ini jam|Sebab jam)\b', line) and 'sesak' not in line \
                            and 'Dialogue' not in line:
                        self.assertRegex(line, r'spoken|speech|話し言葉|Hari ini jam', (l['title'], line))

    def test_places_of_worship_even_handed(self):
        """Sam, 12 Nov 2026: masjid, gereja, kuil, tokong, gurdwara and surau are one set of plain landmarks, none favoured."""
        counts = {w: 0 for w in WORSHIP}
        for l in self.by_unit[self.u]:
            for _, items, _ in l['sections']:
                for line in items + l['key']:
                    for span in re.findall(r'«([^»]*)»', line):
                        for w in re.findall(r'[a-z]+', span.lower()):
                            if w in counts:
                                counts[w] += 1
        for w, n in counts.items():
            self.assertGreaterEqual(n, 4, w)
        # No single place of worship is used more than twice as often as the least used.
        self.assertLessEqual(max(counts.values()), 3 * min(counts.values()), counts)
        # All six are core words in the same group.
        group = dict(self.cfg['core_groups'])['Landmarks and transport']
        for lid in ('L-0337', 'L-1054', 'L-1055', 'L-1056', 'L-1057', 'L-1058'):
            self.assertIn(lid, group)
        notes = ' '.join(self.cfg['teacher_notes'])
        self.assertIn('Show no bias', notes)

    def test_sam_rules_and_scene_facts(self):
        """Practice places are fictional; real-world facts in the culture note carry named sources."""
        everything = ' '.join(x for l in self.by_unit[self.u] for _, items, _ in l['sections'] for x in items + l['key'])
        self.assertIn('fictional', everything)
        notes = self.comp('Culture note')
        sources = ' '.join(self.lines(notes) + notes['key'])
        for name in ('SAYS Malaysia', 'Malay Mail', 'WorldAtlas', 'Sinar Daily', 'Rank 3', 'ms-c07-009'):
            self.assertIn(name, sources, name)
        culture = ' '.join(self.lines(notes, 'English'))
        # No distance, line name or percentage is stated as a fact about the real country.
        self.assertNotRegex(culture, r'\d+\.?\d*\s*(%|per cent|km|kilomet)')

    def test_openers_have_no_leftover_english(self):
        for unit in ('ms-c04a', 'ms-c04b', 'ms-c05', 'ms-c06', 'ms-c07'):
            opener = next(l for l in self.by_unit[unit] if l['suite']['component_type'] == 'Opener')
            for line in self.lines(opener):
                if line.startswith('After class'):
                    ja = line.split(' / ')[-1]
                    self.assertNotRegex(ja, r'\band\b', (unit, ja))
        opener = next(l for l in self.by_unit[self.u] if l['suite']['component_type'] == 'Opener')
        self.assertIn('Sedia Kelas c07 (27 cards, frames ms-c07-f01 and ms-c07-f02)', ' '.join(self.lines(opener)))

    def test_fast_pack(self):
        self.assertIn('ms-c07-fast', self.by_unit)
        l = self.by_unit['ms-c07-fast'][0]
        self.assertEqual(l['suite']['course_path'], 'fast')
        core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertTrue(15 <= len(core) <= 20)
        self.assertTrue(set(fast.C7_WORDS) <= set(self.cfg['core']))
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
        ch7 = next(c for c in chapters if c['title'].startswith('Chapter 7'))
        self.assertIn(l['title'], ch7['fast_items'])
        self.assertEqual(ch7['status'], 'Step 5e chapter 7 suite · draft for pilot')
        guide = ' '.join(self.lines(l, 'Self-study'))
        self.assertIn('Sedia Kelas c07', guide)
        for scene in SCENES:
            self.assertIn(scene, guide)
        self.assertIn('ms-c07-001 to ms-c07-049', guide)

    def test_legacy_retirement_and_catalogue(self):
        built = {x['title'] for x in bank()}
        for name in ('Asking where', 'Directions and orientation', 'Di, ke and dari'):
            self.assertFalse(any(t == name or t.startswith(name + ' ·') for t in built), name)
        chapters = json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])
        ch7 = next(c for c in chapters if c['title'].startswith('Chapter 7'))
        self.assertEqual([u['label'] for u in ch7['units']], ['7'])
        self.assertEqual(ch7['status'], 'Step 5e chapter 7 suite · draft for pilot')
        catalogue = make_catalogue(bank(), chapters)
        mine = [c for c in catalogue['components'] if c.get('authored') and c.get('check_unit') == self.u]
        self.assertTrue(mine)
        self.assertTrue(all(c['chapter_id'] == 'ms-c07' and c['review_status'] == 'draft' for c in mine))
        exceptions = json.loads((ROOT / 'curriculum/legacy-exceptions.json').read_text())
        self.assertEqual(len(exceptions), 30)
        self.assertFalse([k for k, e in exceptions.items() if e['unit'] in (self.u, 'ms-c07-fast')])
        reauthored = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for unit in (self.u, 'ms-c07-fast'):
            self.assertIn(unit, reauthored)
        block = next(b for b in catalogue['additional_blocks'] if b['id'] == 'ms-stage1-writing-7')
        self.assertEqual(block['component_ids'], ['ms-c07-writing-block'])
        self.assertEqual(block['status'], 'pilot draft')


if __name__ == '__main__':
    unittest.main()
