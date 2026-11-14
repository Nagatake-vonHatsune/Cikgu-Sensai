"""Stage 2 build step 5: chapter 18, the Stage 2 close (unit 18: blocks 18A, 18B, 18E and the teaching plan; the A2 stage test
for blocks 18C and 18D, versions A and B, with scripts and an administration sheet; the chapter 18 fast pack; the Stage 2
record in the catalogue).

Checks: the five block timings; the Kata-Kata c18 spine word for word; every chapter 10 to 17 pattern returns (the late
chapters 16 and 17 twice); the item map covers every chapter 10 to 17 in both versions; no word outside chapters 1 to 17; no
«lah» or «kan» in any key; no practice-pool or recognition-only word in a key; parallel versions; the pass rule; the hours
check; the standing rules.
"""
import csv
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, fast, ms_c18, stage2
from catalogue import make_catalogue, GOALS

ROOT = Path(__file__).resolve().parents[1]
POOL = ['L-1304', 'L-1305', 'L-1306', 'L-1307', 'L-1308', 'L-1309']
RECOGNITION = ['L-0667', 'L-0604', 'L-0678', 'L-0608']  # pindah, tukar, deadline, nombor tracking
SECTIONS = ('listening', 'reading', 'writing', 'speaking')
# The one practice-pool recognition line (18A reading), allowed only there and never in a key.
POOL_LINE = 'Semua bungkusan disimpan di pondok pengawal.'


def bank():
    raw = (ROOT / 'dist/bank.js').read_text()
    return json.loads(raw.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


def chapters_js():
    return json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1])


def kk(n):
    return json.loads((ROOT / f'curriculum/reference/katakata/c{n:02}.json').read_text())


def strip_mentions(s):
    return re.sub(r'‹[^›]*›', ' ', s)


class Chapter18(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.c18 = [l for l in cls.lessons if l['suite']['chapter_id'] == 'ms-c18']
        cls.by_id = {l['suite']['id']: l for l in cls.c18}
        with (ROOT / 'curriculum/reference/katakata/malay-ledger.csv').open(encoding='utf-8', newline='') as f:
            cls.rows = {r['ID']: r for r in csv.DictReader(f)}

    def lines(self, l, part=None):
        return [x for name, items, _ in l['sections'] if part is None or part in name for x in items]

    def text(self, l):
        return ' '.join(self.lines(l) + l['key'])

    # --- blocks and timings ------------------------------------------------------------------------------------------

    def test_five_blocks_and_timings(self):
        for cid, block in (('ms-c18-review', '18A'), ('ms-c18-rehearsal', '18B'), ('ms-c18-feedback', '18E')):
            l = self.by_id[cid]
            self.assertEqual(l['suite']['time_minutes'], 45, cid)
            self.assertEqual(l['suite']['block'], block)
            minutes = [int(m) for n, _, _ in l['sections'] for m in re.findall(r'\((\d+) min\)', n)]
            self.assertEqual(sum(minutes), 45, (cid, minutes))
        self.assertEqual(stage2.TIMING, {'listening': 12, 'reading': 15, 'writing': 18, 'speaking': 7})
        self.assertEqual(sum(stage2.TIMING[s] for s in ('listening', 'reading', 'writing')), 45)
        for v in 'ab':
            for sec in SECTIONS:
                l = self.by_id[f'ms-stage2-test-{v}-{sec}']
                self.assertEqual(l['suite']['block'], '18D' if sec == 'speaking' else '18C')
        plan = self.text(self.by_id['ms-c18-teaching-plan'])
        for b in ('18A', '18B', '18C', '18D', '18E'):
            self.assertIn(b + ' ·', plan)
        self.assertIn('six learners', plan)
        self.assertEqual(set(ms_c18.GOALS), set('ABCDE'))

    def test_kata_kata_c18_is_the_spine(self):
        """All 22 scenario lines and the six frames, word for word, in 18A."""
        pack = kk(18)
        self.assertEqual(len(pack['scenario']['lines']), 22)
        self.assertEqual(len(pack['frames']), 6)
        self.assertEqual(pack['cards'], [])
        body = ' '.join(self.lines(self.by_id['ms-c18-review']))
        for line in pack['scenario']['lines']:
            self.assertIn('«' + line['ms'] + '»', body, line['id'])
        for f in pack['frames']:
            self.assertIn('«' + f['example'] + '»', body, f['id'])
        # Spoken forms in the Kata-Kata lines are labelled beside them.
        model = self.lines(self.by_id['ms-c18-review'], 'Model')
        for form in ('«Set! Hari Ahad, pukul tujuh.»', '«Baik. Jumpa kat pejabat dulu, ya?»'):
            line = next(x for x in model if form in x)
            self.assertIn('spoken', line)
        # Speaker labels are English names without a Malay title.
        for x in model:
            if ': «' in x:
                self.assertNotRegex(x.split(': «')[0], r'\b(Cik|Puan|Encik)\b', x)

    def test_every_chapter_10_to_17_pattern_returns(self):
        frames = [f['id'] for n in range(10, 18) for f in kk(n)['frames']]
        self.assertEqual(len(frames), 48)
        self.assertEqual(set(ms_c18.FRAME_RETURNS), set(frames))
        review = self.by_id['ms-c18-review']
        body = ' '.join(self.lines(review))
        for fid, line in ms_c18.FRAME_RETURNS.items():
            self.assertIn('«' + line + '»', body, fid)
        self.assertTrue(set(frames) <= set(review['suite']['pattern_ids']))
        key = ' '.join(review['key'])
        for fid in frames:
            self.assertIn(fid[-3:] + ' «', key)

    def test_late_chapters_return_twice_and_carry_forward(self):
        late = [f['id'] for n in (16, 17) for f in kk(n)['frames']]
        self.assertEqual(set(ms_c18.LATE_RETURNS), set(late))
        body = ' '.join(self.lines(self.by_id['ms-c18-rehearsal']))
        for fid, line in ms_c18.LATE_RETURNS.items():
            self.assertIn(line, body, fid)
            self.assertNotEqual(line, ms_c18.FRAME_RETURNS[fid], fid)  # a second, different return
        rec = self.catalogue()['stages'][1]
        self.assertEqual(rec['stage3_carry_forward'], ['ms-c16', 'ms-c17'])
        ch = {c['id']: c for c in self.catalogue()['chapters']}
        for n in (16, 17):
            for r in ch[f'ms-c{n}']['recycled_items']['planned_pattern_returns']:
                self.assertIn('ms-c18', r['destinations'])
                self.assertIn('ms-stage3 (carried forward)', r['destinations'])

    def test_rehearsals_are_the_plans_three_scenes(self):
        names = [n for n, _, _ in self.by_id['ms-c18-rehearsal']['sections']]
        for scene in ("A new colleague's day", 'The parcel problem', 'The changed invitation', 'Targeted repair'):
            self.assertTrue(any(scene in n for n in names), scene)
        self.assertGreaterEqual(len(ms_c18.REPAIR), 8)

    # --- words -------------------------------------------------------------------------------------------------------

    def all_spans(self, lessons, with_tests=True):
        out = []
        for l in lessons:
            for line in self.lines(l) + l['key'] + ([t['prompt'] + ' ' + t['answer_key'] for t in l['suite']['tests']] if with_tests else []):
                out += [(span, line) for span in re.findall(r'«([^«»]*)»', line)]
        return out

    def test_only_words_from_chapters_1_to_17(self):
        """Every Malay span of chapter 18 (unit, test, fast pack) checked at chapter 17: no gap, no affix or placement violation.
        The one practice-pool line of the 18A reading is the only exception."""
        segs = [{'unit': 'ms-c18', 'chapter': 17, 'source': line[:40], 'source_text': 'spoken ' + line, 'kind': 'model', 'text': span}
                for span, line in self.all_spans(self.c18) if span != POOL_LINE]
        self.assertGreater(len(segs), 600)
        result = self.ledger.checker.inspect(segs)
        self.assertFalse(result['ledger_gaps'], list(result['ledger_gaps'])[:5])
        bad = [k for k, e in result['violations'].items() if e['check'] != 'register']
        self.assertFalse(bad, bad[:5])
        # The pool line is in the 18A reading only, with its note.
        where = [l['suite']['id'] for l in self.c18 if POOL_LINE in self.text(l)]
        self.assertEqual(where, ['ms-c18-review'])
        self.assertIn('practice word', next(x for x in self.lines(self.by_id['ms-c18-review'], 'Read') if POOL_LINE in x))

    def test_no_new_word(self):
        """Chapter 18 places nothing: no ledger row is core at chapter 18, and the test words are placed at chapters 1 to 17."""
        placed18 = [i for i, r in self.rows.items() if r['Review status'] != 'Retired' and re.match(r'Ch18\b', r['Kata-Kata place'])]
        self.assertEqual(placed18, [])
        for v in stage2.VERSIONS:
            for code, words in stage2.item_words(v).items():
                for w in words:
                    ids = self.ledger.ids_for([w])
                    rows = [r for r in self.rows.values() if self.ledger.word_id(r) in ids]
                    nums = [int(x) for r in rows for x in re.findall(r'Ch\s*(\d+)', r['Kata-Kata place'])] + \
                           [int(x) for r in rows for x in re.findall(r'ms-c(\d+)-\d', r['Kata-Kata (card IDs)'])]
                    self.assertTrue(nums and min(nums) <= 17, (code, w))
                    self.assertFalse({r['ID'] for r in rows} & set(POOL + RECOGNITION), (code, w))

    def test_no_lah_or_kan_and_no_pool_word_in_any_key(self):
        pool_forms = {self.rows[i]['Malay'] for i in POOL}
        recog_forms = {'pindah', 'tukar', 'deadline', 'nombor tracking'}
        tests = [l for l in self.c18 if l['suite']['check_unit'] == 'ms-stage2']
        keys = []
        for l in tests:
            keys += l['key'] + [t['answer_key'] for t in l['suite']['tests']]
        keys += self.by_id['ms-c18-fast-pack']['key']
        self.assertGreater(len(keys), 40)
        for k in keys:
            for span in re.findall(r'«([^«»]*)»', strip_mentions(k)):
                words = re.findall(r"[a-z]+(?:-[a-z]+)*", span.lower())
                self.assertNotIn('lah', words, k)
                self.assertNotIn('kan', words, k)
                for w in words:
                    self.assertFalse(w.endswith('lah') and w not in ('sekolah', 'masalah', 'adalah') and w[:-3] in self.ledger.checker.known, (w, k))
                for f in pool_forms | recog_forms:
                    self.assertNotRegex(span.lower(), r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', (f, k))
        # No practice-pool word anywhere in the test papers.
        for l in tests:
            for span, line in self.all_spans([l]):
                for f in pool_forms:
                    self.assertNotRegex(span.lower(), r'(?<![a-z])' + re.escape(f) + r'(?![a-z])', line)
        # The build's own R4 check: no test answer key requires a particle.
        segs = [{'unit': 'ms-stage2', 'chapter': 18, 'source': 'x|answer_key', 'source_text': k, 'kind': 'test', 'text': span}
                for k in keys for span in re.findall(r'«([^«»]*)»', k)]
        result = self.ledger.checker.inspect(segs)
        self.assertFalse([e for e in result['violations'].values() if e['term'] in ('lah', 'kan')])

    # --- the A2 stage test -------------------------------------------------------------------------------------------

    def test_item_map_covers_every_chapter_10_to_17(self):
        for v in stage2.VERSIONS:
            imap = stage2.item_map(v)
            covered = {c for _, _, _, ch in imap for c in ch}
            self.assertTrue(set(range(10, 18)) <= covered, v['label'])
            self.assertTrue(covered <= set(range(1, 18)), v['label'])
            for n in range(10, 18):
                self.assertGreaterEqual(sum(n in ch for _, _, _, ch in imap), 2, (v['label'], n))
            for code, _, _, ch in imap:
                self.assertTrue(set(ch) & set(range(10, 18)), code)
            # Every item names the Kata-Kata patterns it tests, and they exist.
            known = {f['id'] for n in range(10, 19) for f in kk(n)['frames']}
            frames = stage2.item_frames(v)
            for code, fl in frames.items():
                self.assertTrue(fl, code)
                self.assertTrue(set(fl) <= known, (code, fl))
            tested = {f for fl in frames.values() for f in fl}
            for n in range(10, 18):
                self.assertTrue(any(f.startswith(f'ms-c{n}-') for f in tested), (v['label'], n))
        admin = self.text(self.by_id['ms-stage2-test-admin'])
        for v in stage2.VERSIONS:
            for code, _, m, ch in stage2.item_map(v):
                self.assertIn(f'{code} · {m} · ch ', admin)
            for n in range(10, 18):
                self.assertIn(f'Ch {n} · ', admin)
        for n in range(10, 18):
            self.assertEqual(stage2.CHARTER_GOALS[n].replace('«', '').replace('»', '').replace('‹', '').replace('›', ''), GOALS[n - 1])

    def test_sections_carry_twenty_marks(self):
        for v in stage2.VERSIONS:
            marks = {}
            for code, sub, m, ch in stage2.item_map(v):
                marks.setdefault(sub, []).append((code, m))
            for sub in ('listening', 'reading', 'writing'):
                self.assertEqual(sum(m for _, m in marks[sub]), 20, (v['label'], sub))
            self.assertEqual(len(marks['listening']), 10)
            self.assertEqual(len(marks['reading']), 10)
            sp = dict(marks['speaking'])
            self.assertEqual(sp[f'{v["label"]}-S1'], 8)
            cards = [m for c, m in sp.items() if '-S2.' in c]
            self.assertEqual((len(cards), set(cards)), (4, {6}))
            for sec in SECTIONS:
                l = self.by_id[f'ms-stage2-test-{v["label"].lower()}-{sec}']
                self.assertEqual(l['suite']['component_type'], 'Test')
                self.assertEqual({t['sub_type'] for t in l['suite']['tests']}, {sec})
                for t in l['suite']['tests']:
                    self.assertRegex(t['prompt'], r'\[\d+ marks?\]$')
                    self.assertRegex(t['prompt'], r'[ぁ-んァ-ン一-龥]')
                    self.assertTrue(t['word_ids'])

    def test_compulsory_request_and_mishap_cards(self):
        """Sam's decision A2: a request card (chapter 12) and a mishap card (chapter 16) are always used."""
        self.assertEqual(stage2.COMPULSORY_PAIRS, {'request (chapter 12)': (1, 2), 'mishap report (chapter 16)': (3, 4)})
        for v in stage2.VERSIONS:
            cards = v['speaking']['cards']
            for c in (1, 2):
                self.assertIn(12, cards[c - 1]['ch'])
                self.assertIn('(request)', cards[c - 1]['title'])
            for c in (3, 4):
                self.assertIn(16, cards[c - 1]['ch'])
                self.assertIn('(mishap)', cards[c - 1]['title'])
            sheet = self.text(self.by_id[f'ms-stage2-test-{v["label"].lower()}-speaking'])
            self.assertIn('One request card (card 1 or 2) and one mishap card (card 3 or 4) are always used', sheet)
            # The invitation in Part 1 brings chapter 17 into speaking.
            self.assertIn(17, v['speaking']['intro']['ch'])
            self.assertIn('Sudikah', ' '.join(v['speaking']['intro']['examiner']))

    def test_answer_keys_are_complete(self):
        for v in stage2.VERSIONS:
            low = v['label'].lower()
            for sec in SECTIONS:
                l = self.by_id[f'ms-stage2-test-{low}-{sec}']
                key = ' '.join(l['key'])
                for t in l['suite']['tests']:
                    code = t['prompt'].split(' ')[0].rstrip('.')
                    self.assertIn(code + (':' if sec != 'speaking' else ''), key)
                    marks = int(re.search(r'\[(\d+) marks?\]', t['prompt'])[1])
                    if sec in ('listening', 'reading'):
                        ones = t['answer_key'].count('(1)')
                        self.assertTrue(ones == marks or f'({marks}' in t['answer_key'], (code, t['answer_key']))
                    elif 'One mark per field' in t['answer_key']:
                        form = next(p for p in v['writing'] if p['form'])['form']
                        self.assertEqual(len(form) - 1, marks)
                        for i in range(1, marks + 1):
                            self.assertRegex(t['answer_key'], rf'(^|\s){i} «', (code, i))
                    else:
                        parts = [int(x) for x in re.findall(r'(?:Content|Task|Language|Accuracy|Interaction|Change of plan) (\d)', t['answer_key'])]
                        self.assertEqual(sum(parts), marks, (code, parts))
                        self.assertIn('Model', t['answer_key'])
            key = ' '.join(self.by_id[f'ms-stage2-test-{low}-listening']['key'])
            for task in v['listening']:
                script = ' '.join(line for _, line in task['script'])
                for _, line in task['script']:
                    self.assertIn(f'«{line}»', key)
                for it in task['items']:
                    for quoted in re.findall(r'«([^»]*)»', it['a']):
                        if '…' not in quoted:
                            self.assertIn(quoted.lower(), script.lower(), quoted)
            sk = ' '.join(self.by_id[f'ms-stage2-test-{low}-speaking']['key'])
            for n in range(1, 5):
                self.assertIn(f'S2.{n} examiner:', sk)
                self.assertIn(f'S2.{n} rubric (6):', sk)
            self.assertIn('S1 rubric (8):', sk)

    def test_writing_keys_list_natural_variants(self):
        for v in stage2.VERSIONS:
            msg = next(p for p in v['writing'] if not p['form'])['items'][0]['a']
            for pair in ('«kalau» / «jika»', '«kerana» / «sebab»', '«kemudian» / «selepas itu»'):
                self.assertIn(pair, msg)
            self.assertIn('standard written forms are always right', msg)
            model = msg.split('Model: ')[1]
            self.assertIn('kita', model)
            self.assertNotIn('kami', model)
            self.assertIn('tangguhkan rancangan', model)  # a noun object

    def test_versions_are_parallel(self):
        a, b = stage2.VERSION_A, stage2.VERSION_B
        ma, mb = stage2.item_map(a), stage2.item_map(b)
        self.assertEqual([(c[2:], s, m) for c, s, m, _ in ma], [(c[2:], s, m) for c, s, m, _ in mb])
        for (ca, _, _, cha), (cb, _, _, chb) in zip(ma, mb):
            self.assertEqual(set(cha) & set(range(10, 18)), set(chb) & set(range(10, 18)), (ca, cb))
        fa, fb = stage2.item_frames(a), stage2.item_frames(b)
        for ca, cb in zip(fa, fb):
            self.assertTrue(set(fa[ca]) & set(fb[cb]), (ca, cb))
        sa = {line for t in a['listening'] for _, line in t['script'] if len(line) > 25}
        sb = {line for t in b['listening'] for _, line in t['script'] if len(line) > 25}
        self.assertFalse(sa & sb)
        self.assertFalse(set(' '.join(p['text']) for p in a['reading']) & set(' '.join(p['text']) for p in b['reading']))
        self.assertNotEqual(a['writing'][0]['intro'], b['writing'][0]['intro'])

    def test_pass_rule_admin_and_scripts(self):
        admin = self.text(self.by_id['ms-stage2-test-admin'])
        self.assertIn('48 or more out of 80 (60 per cent), and at least 10 out of 20 in every section', admin)
        self.assertIn("Sam's decision A1", admin)
        self.assertIn('the charter gives no A2 rule', admin)
        self.assertIn('not an official CEFR certificate', admin)
        self.assertIn('keeps no learner records', admin)
        self.assertIn('Malay A2 · Stage 2 complete', admin)
        self.assertIn('outside the 67 blocks', admin)
        for part in ('Timing', 'Materials', 'Running the test', 'Scoring and pass rule', 'Item map · Version A', 'Item map · Version B'):
            self.assertIn(part, ' '.join(n for n, _, _ in self.by_id['ms-stage2-test-admin']['sections']))
        self.assertIn('Result sheet', admin)
        scripts = self.text(self.by_id['ms-stage2-test-scripts'])
        for v in stage2.VERSIONS:
            for task in v['listening']:
                for _, line in task['script']:
                    self.assertIn(f'«{line}»', scripts)

    # --- record, hours and registration ------------------------------------------------------------------------------

    def catalogue(self):
        if not hasattr(self, '_cat'):
            self._cat = make_catalogue(bank(), chapters_js())
        return self._cat

    def test_stage2_record_and_hours(self):
        cat = self.catalogue()
        rec = next(s for s in cat['stages'] if s['id'] == 'ms-stage2')
        self.assertEqual(rec['cefr'], 'A2')
        self.assertEqual(rec['chapter_ids'], [f'ms-c{n}' for n in range(10, 19)])
        self.assertEqual(rec['review_block_id'], 'ms-c18-review')
        self.assertEqual(rec['cando_review_id'], 'ms-c18-feedback')
        self.assertEqual(set(rec['cando_goals']), {f'ms-c{n}' for n in range(10, 18)})
        self.assertEqual(rec['completion']['label'], 'Malay A2 · Stage 2 complete')
        st = rec['stage_test']
        self.assertEqual(st['pass_rule']['total_min'], 48)
        self.assertEqual(st['pass_rule']['section_min'], 10)
        self.assertEqual(st['total_marks'], 80)
        ids = {c['id'] for c in cat['components']}
        for v in ('A', 'B'):
            self.assertEqual(len(st['versions'][v]), 4)
            self.assertTrue(set(st['versions'][v]) <= ids)
        self.assertIn(st['scripts_id'], ids)
        self.assertIn(st['administration_id'], ids)
        items = {t['id'] for t in cat['test_items'] if t['id'].startswith('ms-stage2-test-')}
        self.assertEqual(items, set(st['item_chapters']))
        self.assertEqual(items, set(st['item_patterns']))
        # Hours check (plan section 1): 55 + 3 + 4 + 5 = 67 blocks of 45 minutes = 50.25 hours, counted from the catalogue.
        self.assertEqual((rec['hours']['total_blocks'], rec['hours']['total_hours']), (67, 50.25))
        chapters = {c['id']: c for c in cat['chapters']}
        teaching = sum(len(chapters[f'ms-c{n}']['block_plan']) for n in range(10, 18))
        extra = [b for b in cat['additional_blocks'] if b['id'].startswith('ms-stage2-') and b['component_ids']]
        c18 = chapters['ms-c18']['block_plan']
        self.assertEqual((teaching, len(extra), len(c18)), (55, 7, 5))
        self.assertEqual(teaching + len(extra) + len(c18), 67)
        self.assertEqual([b['label'] for b in c18], list('ABCDE'))
        for b in c18:
            self.assertEqual(sum(a['minutes'] for a in b['activities']), 45)
        self.assertEqual([a['minutes'] for a in c18[2]['activities']], [12, 15, 18])

    def test_can_do_review_sheet(self):
        fb = self.by_id['ms-c18-feedback']
        check = self.lines(fb, 'Can-do review')
        for n in range(10, 18):
            self.assertTrue(any(x.startswith(f'■ Chapter {n} · ') for x in check), n)
            self.assertGreaterEqual(len(stage2.CANDO[n]), 2)
            for en, ja in stage2.CANDO[n]:
                self.assertIn(f'☐ I can · ☐ again · {en} / {ja}', check)
                self.assertRegex(ja, r'[ぁ-んァ-ン一-龥]')

    def test_hanashishou_scenes_named_only(self):
        fb = self.by_id['ms-c18-feedback']
        body = self.text(fb)
        for _, names in ms_c18.HANASHISHOU:
            for n in names:
                self.assertIn(n, body)
        self.assertIn('build step 6', body)
        self.assertEqual(fb['suite'].get('word_ids_override'), None)
        self.assertNotRegex(body, r'(?:grab_ride_chat|lost_wallet|guardhouse_parcel)[^.]*\bchapter 1\d\b')
        self.assertEqual(len([n for _, ns in ms_c18.HANASHISHOU for n in ns]), 12)

    def test_registration(self):
        units = json.loads((ROOT / 'curriculum/reauthored-units.json').read_text())
        for u in ('ms-c18', 'ms-c18-fast', 'ms-stage2'):
            self.assertIn(u, units)
        ch18 = next(c for c in chapters_js() if c['title'].startswith('Chapter 18'))
        self.assertEqual([u['label'] for u in ch18['units']], ['18'])
        self.assertEqual(ch18['level'], 'A2')
        page = {x['title'] for x in bank()}
        for t in ('Stage 2 · A2 stage test · Version A · Listening', 'Stage 2 · A2 stage test · Version B · Speaking',
                  'Stage 2 · A2 stage test · Listening scripts (teacher)', 'Stage 2 · A2 stage test · Administration sheet (teacher)'):
            self.assertIn(t, ch18['stage_items'])
            self.assertIn(t, page)
        self.assertEqual(ch18['fast_items'], ['Chapter 18 · Fast-course summary pack'])
        self.assertIn('Unit 18 · 18A · Integrated review · A working week', ch18['units'][0]['items'])
        # Order in the chapter: the unit, then the fast pack, then the test.
        items = ch18['items']
        self.assertLess(items.index('Unit 18 · 18E · Feedback, can-do review and next steps'), items.index('Chapter 18 · Fast-course summary pack'))
        self.assertLess(items.index('Chapter 18 · Fast-course summary pack'), items.index('Stage 2 · A2 stage test · Version A · Listening'))

    def test_fast_pack(self):
        l = self.by_id['ms-c18-fast-pack']
        self.assertEqual(l['suite']['course_path'], 'fast')
        self.assertEqual(l['level'], 'A2')
        self.assertEqual(l['suite']['time_minutes'], 45)
        words = [x for x in self.lines(l, 'Review words') if re.search(r'\[L-\d{4}\]$', x)]
        self.assertTrue(15 <= len(words) <= 20)
        self.assertEqual(len(fast.C18_WORDS), len(words))
        chapters = set()
        for lid in fast.C18_WORDS:
            place = self.rows[lid]['Kata-Kata place']
            m = re.match(r'Ch1([0-7]) \(unit ', place)
            self.assertTrue(m, (lid, place))
            chapters.add(int('1' + m[1]))
            self.assertNotIn(lid, POOL + RECOGNITION)
        self.assertEqual(chapters, set(range(10, 18)))
        patterns = [x for x in self.lines(l, 'Key patterns') if re.match(r'^\d · ', x)]
        self.assertEqual(len(patterns), 5)
        for line in patterns:
            self.assertEqual(line.split('e.g.')[1].count(' / '), 1, line)
        self.assertTrue(10 <= len(self.lines(l, 'Model conversation')) <= 16)
        self.assertEqual(sum(x.startswith('☐') for x in self.lines(l, 'Self-check')), 5)
        self.assertIn('This pack is not the test', self.text(l))
        self.assertIn('A2 stage test', self.text(l))
        scenario = {x['ms'] for x in kk(18)['scenario']['lines']}
        for x in self.lines(l, 'Model conversation'):
            self.assertIn(re.search(r'«(.*)»', x)[1], scenario)

    # --- standing rules ----------------------------------------------------------------------------------------------

    def test_standing_rules(self):
        repair = {s for q in ms_c18.REPAIR for s in (q[1], q[2])}  # the choose-the-better items show a wrong line on purpose
        spans = [(s, line) for s, line in self.all_spans(self.c18) if s not in repair]
        # «dari» for places, times and directions («balik dari pejabat»); «daripada» for people and senders («mesej daripada kedai itu»).
        dmw = re.compile(r'(?<![a-z])dari (encik|puan|cik|doktor|bos|pengurus|kawan|pengawal|juruteknik)\b|(mesej|surat|emel|cuti sakit|jemputan) dari\b')
        aspect_kan = re.compile(r'\b(sudah|sedang|belum|akan|baru|masih) (simpankan|hantarkan|tunjukkan|tangguhkan|batalkan|bukakan|tinggalkan|bersihkan|hubungi|baiki)\b')
        menkan = re.compile(r'\bme[a-z]+kan\b')
        for s, line in spans:
            low = s.lower()
            self.assertNotRegex(low, dmw, line)
            self.assertNotRegex(low, aspect_kan, line)
            for w in menkan.findall(low):
                self.assertIn(w, ('menangguhkan', 'membatalkan'), line)
            # «Lain kali, ya?» is a soft no: never in the same span after a new day is offered.
            if 'lain kali' in low:
                self.assertNotIn('bagaimana kalau', low.split('lain kali')[0], line)
            # «tangguhkan» / «batalkan» take a noun object (a short spoken reply «… tangguhkan ke hari …» may drop it).
            self.assertNotRegex(low, r'\b(tangguhkan|batalkan) (mendaki|makan|pergi|datang)\b', line)
            if len(low.split()) > 1:  # the teaching plan names the rule with the bare word
                self.assertNotIn('keputusan', low, line)
            # «sudi» is for invitations only.
            self.assertNotRegex(low, r'\bsudi\w* (encik|puan|cik|awak) (singgah|tolong|hantar|simpan|semak|hubungi|tunjuk)', line)
        text = ' '.join(self.text(l) for l in self.c18).lower()
        self.assertNotRegex(text, r'assalam|waalaikum|insya|alhamdulillah|bismillah|halal|haram|solat|\bdoa\b|raya')
        # Clinic safety (chapter 13 limits): no medicine, dose or treatment advice in Malay.
        for s, line in spans:
            self.assertNotRegex(s.lower(), r'\b(ubat|dos|pil|ambil ubat|sehari dua kali|antibiotik|panadol)\b', line)
        # Repair items: the wrong line is one of the two choices and the key names the rule.
        key = ' '.join(self.by_id['ms-c18-rehearsal']['key'])
        for i, (_, a, b, ans, rule) in enumerate(ms_c18.REPAIR, 1):
            self.assertIn(ans, ('a', 'b', 'both'))
            self.assertIn(f'{i} {ans}:', key)

    def test_spoken_forms_are_labelled(self):
        spoken = re.compile(r'(?<![a-z])(nak|tak|dah|kat|ni|tu|sikit|takpe|set|tengok|macam tu)(?![a-z])')
        for l in self.c18:
            for s, line in self.all_spans([l]):
                if spoken.search(s.lower()) and s not in ('Set!',):
                    self.assertRegex(line, r'(?i)spoken|話し言葉', (l['title'], line))


if __name__ == '__main__':
    unittest.main()
