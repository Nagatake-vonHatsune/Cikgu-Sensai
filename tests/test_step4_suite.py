"""Step 4 pilot: charter section 6 content minimums and section 14 drills,
checked from the authored source (suite/) and the built bank."""
import json
import re
import unittest
from pathlib import Path

from suite import Ledger, build_suite, malay_words, english_words, strip, guard, TARGET
from catalogue import make_catalogue, validate_test_item

ROOT = Path(__file__).resolve().parents[1]
UNITS = ['ms-c01', 'ms-c02a', 'ms-c02b']
NUMBERED = re.compile(r'^(?:☐ )?\d+\. ')


def bank():
    text = (ROOT / 'dist/bank.js').read_text()
    return json.loads(text.split('const lessons=')[1].split(';\nconst bankPDF=')[0])


class SuiteMinimums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = Ledger()
        cls.lessons, cls.units = build_suite(cls.ledger)
        cls.by_unit = {}
        for l in cls.lessons:
            cls.by_unit.setdefault(l['suite']['check_unit'], []).append(l)

    def comp(self, unit, ctype, sub=None):
        found = [l for l in self.by_unit[unit] if l['suite']['component_type'] == ctype and (sub is None or l['suite']['sub_type'] == sub)]
        self.assertTrue(found, f'{unit}: missing {ctype} {sub or ""}')
        return found[0]

    def lines(self, lesson, label=None):
        return [x for name, ls, kind in lesson['sections'] if label is None or label in name for x in ls]

    def test_all_eleven_components_per_unit(self):
        types = ['Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation', 'Listening',
                 'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan']
        for unit in UNITS:
            self.assertEqual({l['suite']['component_type'] for l in self.by_unit[unit]} >= set(types), True, unit)

    def test_vocabulary_lists_every_unit_ledger_word(self):
        for u in self.units:
            # Unit 18 (the Stage 2 close) teaches no new word, so it has no word scope and no vocabulary component.
            if not u.get('label') or u.get('word_scope') is None:
                continue
            text = ' '.join(self.lines(self.comp(u['check_unit'], 'Vocabulary')))
            for lid in u['word_scope']:
                self.assertIn(f'[{lid}]', text, f'{u["unit_id"]} vocabulary misses {lid}')
            entries = [x for x in self.lines(self.comp(u['check_unit'], 'Vocabulary')) if re.search(r'\[L-\d{4}\]$', x)]
            examples = [x for x in self.lines(self.comp(u['check_unit'], 'Vocabulary')) if x.strip().startswith('e.g.')]
            self.assertEqual(len(entries), len(examples), 'one example per word')
            self.assertTrue(all(re.search(r' — .+ · .+', x) for x in entries), 'EN and JA meaning on every word')

    def test_patterns(self):
        for unit in UNITS:
            sections = [(n, ls) for n, ls, k in self.comp(unit, 'Pattern and grammar')['sections']]
            self.assertTrue(3 <= len(sections) <= 5, unit)
            for name, ls in sections:
                self.assertTrue(any(x.startswith('Pattern box') for x in ls), name)
                self.assertTrue(4 <= sum(1 for x in ls if re.match(r'^\d+\. A: ', x)) <= 6, f'{unit} {name}: 4 to 6 Q&A examples')
                for prefix in ('Explanation: ', '説明：', 'Japanese helps or misleads: ', '日本語との比較：'):
                    self.assertTrue(any(x.startswith(prefix) for x in ls), f'{unit} {name}: {prefix}')

    def test_drills_section_14(self):
        for unit in UNITS:
            for sub in ['repeat', 'substitute', 'transform', 'question and answer', 'question-word choice']:
                items = [x for x in self.lines(self.comp(unit, 'Drill', sub)) if NUMBERED.match(x)]
                self.assertGreaterEqual(len(items), 6, f'{unit} {sub}')
            dialogues = [x for x in self.lines(self.comp(unit, 'Drill', 'free')) if x.startswith('Dialogue ')]
            self.assertGreaterEqual(len(dialogues), 3, unit)
            self.comp(unit, 'Drill', 'question-word set')
            total = sum(len([x for x in self.lines(self.comp(unit, 'Drill', s)) if NUMBERED.match(x)])
                        for s in ['repeat', 'substitute', 'transform', 'question and answer', 'question-word choice'])
            self.assertGreaterEqual(total, 30, unit)

    def test_question_word_set_is_cumulative(self):
        expected = {'ms-c01': ['apa'], 'ms-c02a': ['apa', 'siapa', 'di mana'],
                    'ms-c02b': ['apa', 'siapa', 'di mana', 'Siapakah', 'Apakah', 'di manakah', 'Adakah', 'Bolehkah']}
        for unit, words in expected.items():
            box = ' '.join(self.lines(self.comp(unit, 'Drill', 'question-word choice')))
            for w in words:
                self.assertIn('«' + w, box, f'{unit}: {w}')

    def test_model_conversation(self):
        for unit in UNITS:
            l = self.comp(unit, 'Model conversation')
            names = [n for n, ls, k in l['sections']]
            self.assertEqual(len(names), 3, 'model, gapped, variant')
            turns = [x for x in l['sections'][0][1] if not x.startswith('— ')]
            self.assertTrue(10 <= len(turns) <= 16, f'{unit}: {len(turns)} turns')
            self.assertTrue(any('___' in x for x in l['sections'][1][1]))

    def test_listening(self):
        for unit in UNITS:
            l = self.comp(unit, 'Listening')
            n = malay_words([x for x in l['key'] if ':' in x and not x.startswith(('Teacher', 'Answers', 'Table'))])
            self.assertTrue(120 <= n <= 250, f'{unit}: {n} Malay words')
            self.assertGreaterEqual(len([x for x in self.lines(l, 'While') if NUMBERED.match(x)]), 6)
            self.assertTrue(self.lines(l, 'Before') and self.lines(l, 'After'))

    def test_reading_writing_task_culture(self):
        for unit in UNITS:
            rw = self.comp(unit, 'Reading and writing')
            self.assertGreaterEqual(len([x for x in self.lines(rw, 'Questions') if NUMBERED.match(x)]), 5)
            self.assertTrue(self.lines(rw, 'Write') and any('Model' in x or 'model' in x for x in rw['key']))
            task = ' '.join(n for n, ls, k in self.comp(unit, 'Task')['sections'])
            for part in ('Role card A', 'Role card B', 'Change of plan', 'Success criteria'):
                self.assertIn(part, task)
            words = english_words(self.lines(self.comp(unit, 'Culture note'), 'English'))
            self.assertTrue(150 <= words <= 300, f'{unit}: culture note {words} words')

    def test_tests_and_plans(self):
        for unit in UNITS:
            items = self.comp(unit, 'Test')['suite']['tests']
            scored = [t for t in items if t['sub_type'] != 'speaking']
            self.assertTrue(15 <= len(scored) <= 20, unit)
            self.assertEqual(len([t for t in items if t['sub_type'] == 'speaking']), 1)
            self.assertTrue({'listening', 'reading'} <= {t['sub_type'] for t in items})
            self.assertTrue({'words', 'grammar'} & {t['sub_type'] for t in items})
            for t in items:
                self.assertTrue(t['grammar_points'] or t['word_ids'], t['id'])
            plan = ' '.join(n for n, ls, k in self.comp(unit, 'Teaching plan')['sections'])
            for block in 'ABCDE':
                self.assertIn(f'Block {block}', plan)
            text = ' '.join(self.lines(self.comp(unit, 'Teaching plan')))
            self.assertIn('Kata-Kata', text)
            self.assertTrue(re.search(r'\d+–\d+ ', text), 'timings')

    def test_skills_blocks(self):
        self.assertEqual(self.comp('ms-c01', 'Drill', 'repeat')['suite']['component_type'], 'Drill')
        self.assertTrue(any(l['suite']['id'] == 'ms-c01-pronunciation-block' for l in self.by_unit['ms-c01']))
        self.assertTrue(any(l['suite']['id'] == 'ms-c02b-writing-block' for l in self.by_unit['ms-c02b']))

    def test_fast_packs(self):
        built = {l['title']: l for l in bank()}
        for unit in ['ms-c01-fast', 'ms-c02-fast']:
            l = self.by_unit[unit][0]
            core = [x for x in self.lines(l, 'Core words') if re.search(r'\[L-\d{4}\]$', x)]
            self.assertTrue(15 <= len(core) <= 20, unit)
            names = ' '.join(n for n, ls, k in l['sections'])
            for part in ('Can-do', 'Core words', 'Key patterns', 'Model conversation', 'Task', 'Self-check', 'Self-study'):
                self.assertIn(part, names)
            for line in self.lines(l, 'Key patterns'):
                if re.match(r'^\d · ', line):
                    self.assertEqual(line.split('e.g.')[1].count(' / '), 1, 'two examples per pattern')
            b = built[l['title']]
            body = len(b['pages']) - 3 - b.get('key_pages', 1)
            self.assertTrue(2 <= body <= 4, f'{unit}: {body} pages')

    def test_japanese_flagged_and_explainers_not_malay(self):
        for l in self.lessons:
            self.assertIn('Japanese awaiting native review', l['header'])
            self.assertIn('ネイティブ', ' '.join(l['explainers'][0][1]))
            self.assertNotIn('«', ' '.join(l['explainers'][1][1]), 'no Malay explainer at A1')

    def test_guard_rejects_unmarked_malay_and_unsourced_mentions(self):
        with self.assertRaises(ValueError):
            guard('fixture', 'Say Selamat pagi to Puan Aini.', self.ledger, set())
        with self.assertRaises(ValueError):
            guard('fixture', 'Root ‹invented›.', self.ledger, set())
        guard('fixture', 'Say «Selamat pagi» to «Puan» Aini.', self.ledger, set())

    def test_catalogue_tags_and_traces(self):
        data = make_catalogue(bank(), json.loads((ROOT / 'dist/chapters.js').read_text()[len('const chapters='):-1]))
        authored = [c for c in data['components'] if c.get('authored')]
        self.assertEqual(len(authored), len(self.lessons))
        for c in authored:
            for k in ('sub_type', 'time_minutes', 'block'):
                self.assertIn(k, c)
            self.assertTrue(c['word_ids'], c['id'])
            self.assertTrue(set(c['word_ids']) <= data['word_registry'].keys(), c['id'])
            self.assertTrue(c['grammar_points'], c['id'])
        for slot in data['component_slots']:
            if slot['unit_id'] in UNITS:
                self.assertEqual(slot['status'], 'complete (pilot draft)', slot['id'])
        for item in data['test_items']:
            validate_test_item(item, data)
        ch2 = next(c for c in authored if c['id'] == 'ms-c02b-drill-3-transformation')
        self.assertEqual(ch2['prerequisites']['chapters'], ['ms-c01'])
        self.assertEqual(ch2['prerequisites']['units'], ['ms-c02a'])


if __name__ == '__main__':
    unittest.main()
