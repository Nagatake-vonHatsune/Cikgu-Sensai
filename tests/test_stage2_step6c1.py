"""Stage 2 step 6c-1 (14 Nov 2026): the ledger holds rows with no chapter (184 Hanashishou bridge-batch rows, Kata-Kata e4e294d), and the shared
checker treats words that have their own ledger row as whole words.

Rule (Sam and Claude): 1. A form that is itself a live ledger row with a chapter is checked at that row's chapter, as a whole word (never split from the
row's chapter on). 2. A row with no chapter never serves as a root; it makes no form legal and no placed form illegal. 3. Practice-pool rows keep «primes Ch18».
The shared fixtures (curriculum/stage-rules-fixtures.json) are run in tests/test_stage_rules.py; the tests here pin the facts they rest on."""
import csv
import re
import unittest
from pathlib import Path

from language_checks import Checker
from suite import ms_c10a, ms_c10b, ms_c11a, ms_c11b, ms_c12a, ms_c12b, ms_c13, ms_c14, ms_c15, ms_c16, ms_c17, fast

ROOT = Path(__file__).resolve().parents[1]
ALL_UNITS = [ms_c10a, ms_c10b, ms_c11a, ms_c11b, ms_c12a, ms_c12b, ms_c13, ms_c14, ms_c15, ms_c16, ms_c17]
CORE_PLACE = re.compile(r'Ch1[0-7] \(unit \w+\)(?:;|$)')


class BridgeRows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / 'curriculum/reference/katakata/malay-ledger.csv').open(encoding='utf-8', newline='') as f:
            cls.rows = {r['ID']: r for r in csv.DictReader(f)}
        cls.checker = Checker()

    def test_the_184_bridge_rows_have_no_chapter(self):
        ids = [f'L-{n}' for n in range(1310, 1494)]
        self.assertEqual(len(self.rows), 1493)
        for lid in ids:
            r = self.rows[lid]
            self.assertTrue(r['Origin'].startswith('Hanashishou bridge batch 1'), lid)
            self.assertTrue(r['Kata-Kata place'].startswith('Jambatan'), lid)
            self.assertTrue(r['Hanashishou (pack · band)'].strip(), lid)
            self.assertNotEqual(r['Review status'], 'Retired', lid)
        self.assertEqual({r['_chapter'] for r in (x for rows in self.checker.entries.values() for x in rows) if r['ID'] in ids}, {None})

    def test_no_row_added_or_carded_in_step_6b_is_stage_2_core(self):
        """Stage 2 core stays 270: the bridge rows and the 80 group (a) rows (cards ms-j-*, place «Jambatan · …») are in no unit, no fast pack, no core count."""
        core = {lid for lid, r in self.rows.items() if r['Review status'] != 'Retired' and CORE_PLACE.match(r['Kata-Kata place'])}
        self.assertEqual(len(core), 270)
        jambatan = {lid for lid, r in self.rows.items() if 'Jambatan' in r['Kata-Kata place']}
        self.assertGreaterEqual(len(jambatan), 184 + 78)
        self.assertFalse(core & jambatan)
        in_units = {lid for m in ALL_UNITS for lid in m.CFG['core']}
        in_fast = {lid for words in (fast.C10_WORDS, fast.C11_WORDS, fast.C12_WORDS, fast.C13_WORDS, fast.C14_WORDS, fast.C15_WORDS,
                                     fast.C16_WORDS, fast.C17_WORDS) for lid in words}
        self.assertFalse(jambatan & in_units)
        self.assertFalse(jambatan & in_fast)
        # The rows with a chapter are exactly the ones before the refresh: no Jambatan row gained one.
        self.assertFalse([lid for lid in jambatan if lid not in ('L-1308', 'L-1309') and re.search(r'Ch\s*\d', self.rows[lid]['Kata-Kata place'])])
        # The two practice-pool rows that also got a Jambatan card keep «primes Ch18».
        for lid in ('L-1308', 'L-1309'):
            self.assertIn('primes Ch18', self.rows[lid]['Kata-Kata place'])
            self.assertEqual(self.checker.entries[self.rows[lid]['Malay']][0]['_chapter'], 18)

    def test_l0195_cards_read_baru_baharu(self):
        import json
        for n, cid in (('04', 'ms-c04-041'), ('06', 'ms-c06-021')):
            cards = {c['id']: c for c in json.loads((ROOT / f'curriculum/reference/katakata/c{n}.json').read_text())['cards']}
            self.assertEqual(cards[cid]['term'], 'baru / baharu')
        self.assertEqual(self.rows['L-0195']['Malay'], 'baru / baharu')


class WholeWordsAndRoots(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checker = Checker()

    def seg(self, text, ch):
        return {'unit': f'fixture-c{ch:02}', 'chapter': ch, 'source': 'fixture', 'text': text, 'source_text': text, 'kind': 'model'}

    def test_whole_words_are_never_split_from_their_own_chapter(self):
        for word, own in (('biasanya', 4), ('akhirnya', 14), ('terlalu', 6), ('selalu', 4), ('adakah', 2)):
            for ch in (own, 17):
                self.assertIsNone(self.checker.derivation(word, ch), (word, ch))
            r = self.checker.inspect([self.seg(word, own)])
            self.assertEqual((r['violations'], r['ledger_gaps']), ({}, {}), word)
            self.assertEqual(self.checker.inspect([self.seg(word, own)])['derivations'], [], word)

    def test_a_root_with_no_chapter_never_opens_a_derived_form(self):
        for root in ('salah', 'biasa', 'akhir', 'lalu', 'cerita'):
            self.assertNotIn(root, self.checker.placed, root)
            self.assertIn(root, self.checker.entries, root)
        for form in ('salahnya', 'ceritanya', 'biasakah'):
            self.assertIsNone(self.checker.derivation(form, 17), form)
            r = self.checker.inspect([self.seg(form, 17)])
            self.assertEqual(r['violations'], {}, form)
            self.assertEqual({e['term'] for e in r['ledger_gaps'].values()}, {form}, form)

    def test_a_row_with_no_chapter_is_a_gap_in_a_unit_with_a_chapter(self):
        r = self.checker.inspect([self.seg('salah', 17)])
        self.assertEqual(r['violations'], {})
        self.assertEqual({e['term'] for e in r['ledger_gaps'].values()}, {'salah'})

    def test_derivation_before_the_row_chapter_still_applies(self):
        # «seminggu» (L-1275) is placed at 10; the Stage 1 units use it at chapter 4 as se- + the placed «minggu».
        self.assertEqual(self.checker.derivation('seminggu', 4)[0], 'minggu')
        self.assertIsNone(self.checker.derivation('seminggu', 10))
        # The practice-pool row «disemak» (placed 18) is still di- + «semak» (11) in unit 11B.
        self.assertEqual(self.checker.derivation('disemak', 11), ('semak', 'di- passive'))
        self.assertEqual(self.checker.inspect([self.seg('disemak', 11)])['violations'], {})


if __name__ == '__main__':
    unittest.main()
