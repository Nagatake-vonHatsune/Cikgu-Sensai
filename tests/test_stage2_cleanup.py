"""Stage 2 clean-up (14 Nov 2026): the 31 words Sam approved are in the units, the lines the builders had rewritten are back to the natural
wording, the six practice-pool rows stay out of every core list, and Sam's chapter 17 fixes are in.

Reads the unit sources (suite/ms_c*.py, suite/fast.py), so it does not depend on a built dist/."""
import csv
import re
import unittest
from pathlib import Path

from suite import ms_c10a, ms_c10b, ms_c11a, ms_c11b, ms_c12a, ms_c12b, ms_c13, ms_c14, ms_c15, ms_c16, ms_c17, fast

ROOT = Path(__file__).resolve().parents[1]
UNITS = {'10A': ms_c10a, '11A': ms_c11a, '11B': ms_c11b, '12B': ms_c12b, '13': ms_c13, '14': ms_c14, '15': ms_c15, '16': ms_c16, '17': ms_c17}
ALL_UNITS = [ms_c10a, ms_c10b, ms_c11a, ms_c11b, ms_c12a, ms_c12b, ms_c13, ms_c14, ms_c15, ms_c16, ms_c17]
# ledger row -> (unit, fast pack word list)
NEW = {
    'L-1273': '10A', 'L-1274': '10A', 'L-1275': '10A', 'L-1276': '10A',
    'L-1277': '11A', 'L-1278': '11B', 'L-1279': '11B', 'L-1280': '11B',
    'L-1281': '12B', 'L-1282': '12B', 'L-1283': '12B', 'L-1284': '12B',
    'L-1285': '13', 'L-1286': '13', 'L-1287': '13', 'L-1288': '13',
    'L-1289': '14', 'L-1290': '14', 'L-1291': '14', 'L-1292': '14', 'L-1293': '14', 'L-1294': '14', 'L-1295': '14',
    'L-1296': '15', 'L-1297': '15', 'L-1298': '16', 'L-1299': '16', 'L-1300': '16', 'L-1301': '16', 'L-1302': '17',
}
# L-1303 «minggu depan» was the 31st word; Kata-Kata step 3f retired it (chapter 4 teaches it), so it is revision in unit 17.
RETIRED = ['L-1303']
FAST = {'10A': fast.C10_WORDS, '11A': fast.C11_WORDS, '11B': fast.C11_WORDS, '12B': fast.C12_WORDS, '13': fast.C13_WORDS, '14': fast.C14_WORDS,
        '15': fast.C15_WORDS, '16': fast.C16_WORDS, '17': fast.C17_WORDS}
POOL = ['L-1304', 'L-1305', 'L-1306', 'L-1307', 'L-1308', 'L-1309']


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from strings(v)


def teaching_text(mod, skip_vocab=True):
    """Every string in a unit's config except the vocabulary example list (the entries a word has just for being taught)."""
    cfg = dict(mod.CFG)
    if skip_vocab:
        cfg.pop('examples', None)
        cfg.pop('vocab_opts', None)
    extra = cfg.get('extra')
    return ' \n'.join(strings(cfg)) + ' \n' + ' \n'.join(strings(extra) if extra else [])


class Cleanup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / 'curriculum/reference/katakata/malay-ledger.csv').open(encoding='utf-8', newline='') as f:
            cls.rows = {r['ID']: r for r in csv.DictReader(f)}

    def test_the_30_words_are_core_in_their_unit_and_in_the_fast_pack(self):
        self.assertEqual(len(NEW), 30)
        for lid, unit in NEW.items():
            self.assertIn(lid, UNITS[unit].CFG['core'], (lid, unit))
            self.assertIn(lid, UNITS[unit].CFG['examples'], lid)
            self.assertIn(lid, FAST[unit], lid)
            self.assertRegex(self.rows[lid]['Kata-Kata place'], r'^Ch1[0-7] \(unit ', lid)

    def test_each_new_word_is_used_in_a_pattern_dialogue_or_task_line(self):
        for lid, unit in NEW.items():
            form = self.rows[lid]['Malay'].lower()
            text = teaching_text(UNITS[unit]).lower()
            self.assertRegex(text, r'(?<![a-z])' + re.escape(form) + r'(?![a-z])', (lid, form))

    def test_minggu_depan_is_retired_and_taught_at_chapter_4(self):
        """Kata-Kata step 3f (ledger Journal row 200): L-1303 is Retired; the phrase is chapter 4 («minggu» L-0167, «depan» L-0173, card ms-c04-019),
        so no exception file is needed and the unit 17 line stays."""
        self.assertEqual(self.rows['L-1303']['Review status'], 'Retired')
        self.assertEqual(self.rows['L-1303']['Kata-Kata place'], '')
        self.assertFalse((ROOT / 'curriculum/phrases-taught-earlier.json').exists())
        self.assertNotIn('earlier_phrases', (ROOT / 'language_checks.py').read_text())
        for lid in RETIRED:
            self.assertNotIn(lid, ms_c17.CFG['core'])
            self.assertNotIn(lid, fast.C17_WORDS)
        from language_checks import Checker
        checker = Checker(ROOT)
        for ch, line in ((4, 'Saya cuti minggu depan.'), (10, 'Saya bercuti minggu depan.'), (17, 'Saya belanja minggu depan.'), (18, 'Saya belanja minggu depan.')):
            r = checker.inspect([{'unit': 'check', 'chapter': ch, 'source': 'span', 'source_text': line, 'kind': 'model', 'text': line}])
            self.assertEqual((r['violations'], r['ledger_gaps']), ({}, {}), (ch, line))

    def test_practice_pool_is_not_core(self):
        """L-1304 to L-1309 (menyapu, disemak, disimpan, bersukan, hidup, giliran) are Dunia practice words: in no unit core list, fast pack or coverage count."""
        self.assertEqual([self.rows[i]['Malay'] for i in POOL], ['menyapu', 'disemak', 'disimpan', 'bersukan', 'hidup', 'giliran'])
        in_units = {lid for m in ALL_UNITS for lid in m.CFG['core']}
        in_fast = {lid for words in (fast.C10_WORDS, fast.C11_WORDS, fast.C12_WORDS, fast.C13_WORDS, fast.C14_WORDS, fast.C15_WORDS,
                                     fast.C16_WORDS, fast.C17_WORDS) for lid in words}
        for lid in POOL:
            self.assertIn('practice pool', self.rows[lid]['Kata-Kata place'])
            self.assertNotIn(lid, in_units)
            self.assertNotIn(lid, in_fast)
        # No core row of Stage 2 is a pool row, and the core count is 270 (L-1303 Retired).
        core = {lid for lid, r in self.rows.items() if r['Review status'] != 'Retired' and re.match(r'Ch1[0-7] \(unit \w+\)(?:;|$)', r['Kata-Kata place'])}
        self.assertEqual(len(core), 270)
        self.assertFalse(core & set(POOL))

    def test_the_rewritten_lines_are_back(self):
        """The natural line with the new word, where the HANDOFF backlog said the builder had rewritten it."""
        want = {
            ms_c10a: ['tiga kali seminggu', 'Kereta api selalu penuh.', 'kolam renang', 'di taman'],
            ms_c11a: ['Saya menghantar emel kepada pengurus.'],
            ms_c11b: ['Seratus ringgit sehari.', 'Kami menempah kereta', 'mendaki bukit'],
            ms_c12b: ['melaporkan kebocoran', 'Tolong simpankan salinan borang itu', 'Juruteknik sudah dihubungi.', 'Paip itu sudah dibaiki'],
            ms_c13: ['Saya tidak sihat.', 'Saya akan beritahu doktor.', 'ahli farmasi', 'Boleh saya tinggalkan beg di sini?'],
            ms_c14: ['Baiklah, kita buat begini.', 'Puan Aini mahu ikut?', 'Apa kata Puan Aini?', 'PENGUMUMAN',
                     'Mei Ling menangguhkan rancangan mendaki kerana dia bekerja.'],
            ms_c15: ['Kakitangan stesen', 'Bulat, seperti bola.'],
            ms_c16: ['Encik tidak apa-apa?', 'Ada masalah?', 'Apa yang berlaku?', 'Boleh saya pinjam telefon encik?'],
            ms_c17: ['Sila balas sebelum hari Rabu.', 'Saya belanja minggu depan.'],
        }
        for mod, lines in want.items():
            text = teaching_text(mod)
            for line in lines:
                self.assertIn(line, text, (mod.__name__, line))

    def test_the_old_rewritten_lines_are_gone(self):
        gone = {
            ms_c10a: ['Kereta api selalu sesak', 'setiap hari Isnin, Rabu dan Jumaat'],
            ms_c13: ['Saya cakap dengan doktor nanti', 'Boleh saya letak beg di sini?'],
            ms_c17: ['Lain kali saya belanja.'],
        }
        for mod, lines in gone.items():
            text = teaching_text(mod)
            for line in lines:
                self.assertNotIn(line, text, (mod.__name__, line))

    def test_third_person_takes_the_standard_form(self):
        """Sam, 14 Nov 2026: «Mei Ling menangguhkan …»; the bare «tangguhkan» and «batalkan» stay for requests, offers and «kita» plans."""
        text = teaching_text(ms_c14)
        self.assertNotRegex(text, r'(?:Mei Ling|Puan Aini|Aini|Encik \w+|Cik \w+) (?:tangguhkan|batalkan)(?![a-z])')
        self.assertIn('Boleh kita tangguhkan ke hari Ahad?', text)
        self.assertIn('Kita batalkan rancangan mendaki', text)
        self.assertIn('membatalkan', text)

    def test_chapter_17_fixes(self):
        """Sam, 14 Nov 2026."""
        cfg = ms_c17.CFG
        text = teaching_text(ms_c17)
        # «Lain kali, ya?» is a soft no: not in the reading or the test reading where the writer offers a new day.
        for reading in cfg['reading'] + cfg['test_reading']:
            if 'Bagaimana kalau hari' in reading:
                self.assertNotIn('Lain kali, ya?', reading)
        self.assertIn('is a soft no', ' '.join(cfg['teacher_notes']))
        self.assertIn('また今度', ' '.join(cfg['teacher_notes']))
        self.assertIn('Saya mahu ajak encik makan malam. Sudikah encik datang?', text)
        self.assertNotIn('Saya ajak Encik Tanaka makan malam. Sudikah', text)
        self.assertIn('Boleh cik singgah di pejabat dulu?', text)
        self.assertNotIn('Sudikah cik singgah', text)
        self.assertIn('very polite', ' '.join(cfg['teacher_notes']))
        self.assertNotRegex(text, r'(?<![a-z])Kafe itu pedas')
        self.assertNotRegex(text, r'Tetapi kafe itu pedas')
        self.assertIn('Makanan di kafe itu pedas.', text)
        self.assertIn('Terima kasih. Kita cari hari lain.', text)
        self.assertNotIn('Saya ada hari lain', text)
        self.assertIn('Terima kasih atas jemputan puan. Saya akan datang.', text)
        self.assertNotIn('jemputan puan. Saya datang.', text)

    def test_backlog_is_empty_in_the_handoff(self):
        handoff = (ROOT / 'HANDOFF.md').read_text(encoding='utf-8')
        self.assertIn('## Word proposals backlog', handoff)
        section = handoff.split('## Word proposals backlog', 1)[1].split('\n## ', 1)[0]
        self.assertNotRegex(section, r'^\| «', 'the backlog table must have no rows left')
        self.assertIn('empty', section.lower())


if __name__ == '__main__':
    unittest.main()
