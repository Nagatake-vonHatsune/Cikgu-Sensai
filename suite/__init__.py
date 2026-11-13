"""Step 4 pilot: full chapter suites for Malay units 1, 2A and 2B, plus the
fast-course summary packs for chapters 1 and 2.

Authoring rules (enforced at build time):
- Every Malay target span is wrapped in «…». It is checked against the ledger,
  register, affix and Malaysian-form rules like any other learner-facing Malay.
- A Malay word quoted only as the root or standard form named in a Kata-Kata
  card note (for example ‹makan› in makan → makanan) is wrapped in ‹…›. Only the
  Malaysian-form check applies, and the word must be listed with its source in
  curriculum/malay-mentions.json.
- Unmarked text is Japanese or English. If it contains a ledger word, the build
  fails, so Malay cannot slip past the checks unmarked.
- Explainers and rubrics are Japanese or English. All Japanese is a draft
  awaiting native review.
- Lines starting with "■ " print as sub-headings.

Content modules: ms_c01 (unit 1), ms_c02a (unit 2A), ms_c02b (unit 2B), fast.
"""
import csv
import io
import json
import re
from pathlib import Path

from language_checks import Checker, norm, tokens

ROOT = Path(__file__).resolve().parents[1]


def katakata_pack(n):
    """Kata-Kata chapter file n (curriculum/reference/katakata/c0n.json, pinned in docs/step4-sources.json)."""
    return json.loads((ROOT / f'curriculum/reference/katakata/c{n:02}.json').read_text(encoding='utf-8'))


def sedia_cards(n):
    """Number of cards in Kata-Kata's Sedia Kelas list for chapter n. Always read from the pinned file: the clean-up
    (Kata-Kata 34710c6) changed every chapter's count, so a hand-typed number goes stale."""
    return len(katakata_pack(n)['sedia_kelas']['cards'])


def last_card(n):
    """Highest card number of chapter n's own cards (ids ms-c0n-NNN; some numbers are gaps after moves and merges)."""
    return max(int(c['id'][-3:]) for c in katakata_pack(n)['cards'] if c['id'].startswith(f'ms-c{n:02}-'))


def pack_cards(n):
    """Number of cards in the chapter n pack of Kata-Kata (cards of the chapter, not Sedia Kelas)."""
    return len(katakata_pack(n)['cards'])


TARGET = re.compile(r'«([^«»‹›]+)»')
MENTION = re.compile(r'‹([^«»‹›]+)›')
JA_DRAFT = '（日本語は下書きです。ネイティブ・スピーカーの確認待ち）'
BM_NOTE = ('No Malay explainer for Stage 1 units: explainers and rubrics are in Japanese or English '
           '(Sam, 11 Nov 2026). Select 日本語 or English.')
# Stage 2 keeps the Stage 1 rule: Japanese and English explainers only (Sam, 13 Nov 2026, answer to question 1 of docs/STAGE-2-ch10-report.md).
BM_NOTE_STAGE2 = ('No Malay explainer for Stage 2 units: explainers and rubrics are in Japanese or English only, '
                  'as in Stage 1 (Sam, 13 Nov 2026). Select 日本語 or English.')
# English words that are spelt like a ledger entry. Unmarked use of these is
# allowed; anything else in the ledger must be marked «…» or ‹…›.
ENGLISH_HOMOGRAPHS = {'main', 'oh', 'pun', 'best', 'bank', 'hotel', 'menu', 'fail', 'golf', 'set', 'unit',
                      'april', 'september', 'november', 'hospital', 'internet', 'kilometer', 'pen', 'tin', 'batik',
                      'bernama', 'label', 'badminton', 'travel', 'hiking', 'deadline', 'slot'}  # badminton and travel: English words in Stage 2 prose (ledger L-0968, L-1029)  # month names (ledger L-1036, L-1041, L-1043); "Bernama" (the news agency, cited in English source notes) and English "label", since the Stage 2 rows L-1111 «bernama» and L-1168 «label» exist

# Grammar points taught in the pilot (IDs extend the step 2 chapter points).
GRAMMAR = [
    dict(id='ms-c01-g02', chapter_id='ms-c01', label='Time-of-day greetings: Selamat pagi, tengah hari, petang, malam'),
    dict(id='ms-c01-g03', chapter_id='ms-c01', label='Titles before names; a title as polite "you"'),
    dict(id='ms-c01-g04', chapter_id='ms-c01', label='Asking after someone: Apa khabar?, pula, pun'),
    dict(id='ms-c01-g05', chapter_id='ms-c01', label='Thanks, apology and polite attention; ya and tidak'),
    dict(id='ms-c01-g06', chapter_id='ms-c01', label='Taking leave: minta diri dulu, Jumpa ___, Selamat jalan / tinggal'),
    dict(id='ms-c01-g07', chapter_id='ms-c01', label='Malay spelling and sounds'),
    dict(id='ms-c01-g08', chapter_id='ms-c01', label='Standard and spoken forms (tidak / tak)'),
    dict(id='ms-c02-g02', chapter_id='ms-c02', label='Pronouns and choosing a word for "you"'),
    dict(id='ms-c02-g03', chapter_id='ms-c02', label='Noun + noun sentences with no verb "to be"'),
    dict(id='ms-c02-g04', chapter_id='ms-c02', label='Question words siapa, apa, di mana in statement order'),
    dict(id='ms-c02-g05', chapter_id='ms-c02', label='Origin: orang + country, asal, dari, kampung'),
    dict(id='ms-c02-g06', chapter_id='ms-c02', label='ini and itu'),
    dict(id='ms-c02-g07', chapter_id='ms-c02', label='-nya: his, her, its; the'),
    dict(id='ms-c02-g08', chapter_id='ms-c02', label='Place with di: tinggal di, kerja di, belajar di'),
    dict(id='ms-c02-g09', chapter_id='ms-c02', label='suka and hobi'),
    dict(id='ms-c02-g10', chapter_id='ms-c02', label='pe- person nouns'),
    dict(id='ms-c02-g11', chapter_id='ms-c02', label='-an thing nouns'),
    dict(id='ms-c02-g12', chapter_id='ms-c02', label='-kah questions, adakah and bolehkah'),
    dict(id='ms-c02-g13', chapter_id='ms-c02', label='juga and pun; kami and kita'),
    dict(id='ms-c02-g14', chapter_id='ms-c02', label='Family and having: ada, dengan'),
]


GRAMMAR.extend([
    dict(id='ms-c03-g02', chapter_id='ms-c03', label='Numbers through one million: cardinal building blocks'),
    dict(id='ms-c03-g03', chapter_id='ms-c03', label='Age with umur and tahun; telephone digit sequences'),
    dict(id='ms-c03-g04', chapter_id='ms-c03', label='Asking and giving fictional prices in ringgit and sen'),
    dict(id='ms-c03-g05', chapter_id='ms-c03', label='ke- ordinals and kali; irregular first'),
    dict(id='ms-c03-g06', chapter_id='ms-c03', label='Fractions, decimals, percentages'),
    dict(id='ms-c03-g07', chapter_id='ms-c03', label='ke-an measurement nouns and units'),
    dict(id='ms-c03-g08', chapter_id='ms-c03', label='Payments, totals, cash, card and change'),
])

GRAMMAR.extend([
    dict(id='ms-c04-g02', chapter_id='ms-c04', label='Clock time with pukul and the parts of the day; suku and setengah'),
    dict(id='ms-c04-g03', chapter_id='ms-c04', label='Days of the week, days around today and dates (hari apa, hari bulan)'),
    dict(id='ms-c04-g04', chapter_id='ms-c04', label='Frequency: setiap, selalu, biasanya, kadang-kadang, jarang, tidak pernah, sekali'),
    dict(id='ms-c04-g05', chapter_id='ms-c04', label='When: bila, pukul berapa, hari apa; pukul (clock) versus jam (duration)'),
    dict(id='ms-c04-g06', chapter_id='ms-c04', label='Aspect markers: sudah, belum, sedang, masih, akan, baru'),
    dict(id='ms-c04-g07', chapter_id='ms-c04', label='Experience with pernah, belum pernah, tidak pernah'),
    dict(id='ms-c04-g08', chapter_id='ms-c04', label='Daily routine with root verbs; mula, habis, sampai; awal and lambat; sebelum and selepas'),
])

GRAMMAR.extend([
    dict(id='ms-c05-g02', chapter_id='ms-c05', label='Adjectives after the noun with no verb "to be"; tidak with adjectives, bukan with nouns'),
    dict(id='ms-c05-g03', chapter_id='ms-c05', label='Taste and colour words; bagaimana rasa and tetapi'),
    dict(id='ms-c05-g04', chapter_id='ms-c05', label='yang (the one that is) and atau (choosing)'),
    dict(id='ms-c05-g05', chapter_id='ms-c05', label='Feelings with rasa; kenapa and sebab'),
    dict(id='ms-c05-g06', chapter_id='ms-c05', label='Wanting and ordering: mahu, kurang manis, ais sedikit'),
])

GRAMMAR.extend([
    dict(id='ms-c06-g02', chapter_id='ms-c06', label='Comparing with lebih and kurang ... daripada'),
    dict(id='ms-c06-g03', chapter_id='ms-c06', label='Equal with sama ... dengan; the whole words setinggi and semahal'),
    dict(id='ms-c06-g04', chapter_id='ms-c06', label='The most with paling; the whole words termurah, terbesar, terbaik, tercantik'),
    dict(id='ms-c06-g05', chapter_id='ms-c06', label='Very and too: sangat, amat, terlalu, sekali after an adjective'),
    dict(id='ms-c06-g06', chapter_id='ms-c06', label='Choosing: yang mana, pilih, lain; describing places'),
])

GRAMMAR.extend([
    dict(id='ms-c07-g02', chapter_id='ms-c07', label='Going and coming: ke, ke mana, dari mana; pergi ke and balik ke'),
    dict(id='ms-c07-g03', chapter_id='ms-c07', label='Position words with di: di depan, di sebelah, di antara; sini, situ, sana; compass points'),
    dict(id='ms-c07-g04', chapter_id='ms-c07', label='Route directions: jalan terus, kemudian belok kiri or kanan di, jangan belok, naik, turun, masuk, keluar'),
    dict(id='ms-c07-g05', chapter_id='ms-c07', label='Distance: dekat, jauh, berapa jauh, lebih kurang, kilometer; kalau; sebulan'),
    dict(id='ms-c07-g06', chapter_id='ms-c07', label='Duration and transport: berapa lama, naik bas, kereta api, jalan kaki; jam / sesak (traffic)'),
])

GRAMMAR.extend([
    dict(id='ms-c08-g02', chapter_id='ms-c08', label='Number + counter + noun: dua ekor ikan; the counter never changes'),
    dict(id='ms-c08-g03', chapter_id='ms-c08', label='se- + counter for "one" (sehelai, secawan, seekor) beside satu + counter'),
    dict(id='ms-c08-g04', chapter_id='ms-c08', label='Berapa + counter: how many (Berapa biji telur?)'),
    dict(id='ms-c08-g05', chapter_id='ms-c08', label='Price per counter and the total: lima ringgit satu kuntum; semua'),
    dict(id='ms-c08-g06', chapter_id='ms-c08', label='Ordering: tolong, Makan sini atau bungkus?; containers and portions'),
])

GRAMMAR.extend([
    dict(id='ms-c09-g02', chapter_id='ms-c09', label='The passive di- + a root verb: dibuat, dibeli, digoreng; the thing comes first'),
    dict(id='ms-c09-g03', chapter_id='ms-c09', label='The doer with oleh: dibuat oleh siapa?; leaving the doer out'),
    dict(id='ms-c09-g04', chapter_id='ms-c09', label='sudah / belum + di- verb; the doer before the verb without di- (Pinggan saya bawa)'),
    dict(id='ms-c09-g05', chapter_id='ms-c09', label='Hours on signs: dibuka / ditutup pada pukul ___; pada and tadi'),
    dict(id='ms-c09-g06', chapter_id='ms-c09', label='Signs and notices: Dilarang ___, Sila ___, papan tanda'),
])

GRAMMAR.extend([
    dict(id='ms-c10-g02', chapter_id='ms-c10', label='ber- verbs of routine and movement as whole words, each with its root; no nasal sound changes'),
    dict(id='ms-c10-g03', chapter_id='ms-c10', label='When things start and when we set off: bermula / bertolak + pukul; Setiap pagi saya ___'),
    dict(id='ms-c10-g04', chapter_id='ms-c10', label='Free time with ber- verbs: suka + ber- verb, pada hujung minggu'),
    dict(id='ms-c10-g05', chapter_id='ms-c10', label='Speaking and meeting with dengan: bercakap, berbual, berjumpa, berkenalan dengan ___'),
    dict(id='ms-c10-g06', chapter_id='ms-c10', label='Background with ber- verbs: berasal dari, bekerja di, bernama, berumur'),
    dict(id='ms-c10-g07', chapter_id='ms-c10', label='Life events with sudah / belum / masih / baru + ber- verb: berkahwin, berpindah, bersekolah'),
    dict(id='ms-c10-g08', chapter_id='ms-c10', label='Spelling and register of ber-: be- (berehat, bekerja), bel- (belajar); standard ber- form beside the everyday root'),
    dict(id='ms-c11-g02', chapter_id='ms-c11', label='meN- verbs as whole words, each with its root, the nasal change and its di- partner: doer + verb + thing'),
    dict(id='ms-c11-g03', chapter_id='ms-c11', label='The same event with the chapter 9 di- partner: Aini membaca buku itu = Buku itu dibaca oleh Aini'),
    dict(id='ms-c11-g04', chapter_id='ms-c11', label='Siapa yang + meN- verb; the answer with the doer before yang'),
    dict(id='ms-c11-g05', chapter_id='ms-c11', label='sedang / sudah / belum / akan + meN- verb; Awak sedang ___ apa?'),
    dict(id='ms-c11-g06', chapter_id='ms-c11', label='A request takes the plain root: Tolong semak ___ ini; tarikh akhir (spoken deadline)'),
    dict(id='ms-c11-g07', chapter_id='ms-c11', label='Plans with mahu + meN- verb: Hujung minggu ini saya mahu ___'),
    dict(id='ms-c11-g08', chapter_id='ms-c11', label='Spelling of meN-: mem- before b; t, p, s, k drop; meng- before h or a vowel; men- before c, d, j; me- before l, m, n, r, w, y; menge- before a one-syllable root'),
    dict(id='ms-c12-g02', chapter_id='ms-c12', label='-kan: do it for someone or make it happen; Tolong simpankan bungkusan ini; the plain root is the everyday form'),
    dict(id='ms-c12-g03', chapter_id='ms-c12', label='Boleh + -kan verb + the thing: Boleh tunjukkan mesej itu?'),
    dict(id='ms-c12-g04', chapter_id='ms-c12', label='-i: to or at a person or place; Boleh hubungi juruteknik?; meN- + hubungi / baiki'),
    dict(id='ms-c12-g05', chapter_id='ms-c12', label='The root for yourself, -kan for someone else: Saya mahu ambil bungkusan / Boleh ambilkan bungkusan saya?'),
    dict(id='ms-c12-g06', chapter_id='ms-c12', label='Juruteknik sedang membaiki paip; baiki, membaiki and gantikan'),
    dict(id='ms-c12-g07', chapter_id='ms-c12', label='Reporting a problem: Ada kebocoran di siling saya; kebocoran, kerosakan, aduan, slot'),
    dict(id='ms-c12-g08', chapter_id='ms-c12', label='Spelling of -kan: double k in letakkan and tunjukkan; berikan = beri + -kan; bersihkan = bersih + -kan; pe-, ke-an and -an words as whole words'),
])


# Product and feature names, not Malay text (removed before the unmarked-Malay guard only).
PRODUCT_NAMES = ['Cikgu, Sensai!', 'Cikgu Sensai', 'Sedia Kelas', 'Tanya Cikgu', 'Kata-Kata', 'Dunia', 'Jambatan',
                 'Susun Ayat', 'Hanashishou', 'Teacher Desk',
                 # Kata-Kata Dunia scene titles (names of scenes, quoted as titles)
                 'Sembang di pantri', 'Pagi di pejabat', 'Ke bank dan pejabat pos', 'Pasar pagi',
                 'Satu hari Encik Tanaka', 'Hujan petang', 'Cuti ke pantai', 'Bangun pagi',
                 'Masak nasi goreng', 'Di klinik', 'Gambar bayi', 'Lepak di kedai mamak',
                 'Main badminton', 'Di ruang tamu', 'Telefon baru', 'Lintas jalan', 'Beli baju',
                 'Rumah terbuka Hari Raya', 'Rumah terbuka', 'Simpulan bahasa harian']


def strip(s):
    return s.replace('«', '').replace('»', '').replace('‹', '').replace('›', '')

def marked(s):
    return TARGET.findall(s), MENTION.findall(s)


class Ledger:
    def __init__(self, root=ROOT):
        text = (root / 'curriculum/reference/katakata/malay-ledger.csv').read_text()
        self.rows = {r['ID']: r for r in csv.DictReader(io.StringIO(text))}
        self.checker = Checker(root)

    def row(self, lid):
        return self.rows[lid]

    def word_id(self, row):
        """Kata-Kata card ID where one exists (chapter card first), else the ledger ID."""
        cards = [c.strip() for c in row['Kata-Kata (card IDs)'].split(',') if c.strip()]
        kelas = [c for c in cards if re.match(r'ms-c\d\d-\d+$', c)]
        return (kelas or cards or [row['ID']])[0]

    def terms_in(self, text):
        """Ledger rows matched in a Malay span, longest match first (as the checker does)."""
        ts = tokens(text); i = 0; found = []
        while i < len(ts):
            if ts[i] in self.checker.proper:
                i += 1; continue
            for size in range(min(self.checker.maxlen, len(ts) - i), 0, -1):
                term = ' '.join(ts[i:i + size])
                rows = self.checker.entries.get(term)
                if rows and size > 1 and self.checker.compositional(term, ts[i:i + size]):
                    continue
                if not rows and size == 1:
                    d = self.checker.derivation(term, 9)
                    rows = self.checker.entries.get(d[0]) if d else None
                if rows:
                    # A retired row (e.g. a duplicate) is never traced as a taught word.
                    found.extend(r for r in rows if r['Review status'] != 'Retired'); i += size; break
            else:
                i += 1
        return found

    def ids_for(self, terms):
        out = []
        for t in terms:
            rows = self.checker.entries.get(norm(t))
            if not rows:
                raise ValueError('Tagged word not in ledger: ' + t)
            live = [r for r in rows if r['Review status'] != 'Retired'] or rows
            out.append(self.word_id(live[0]))
        return list(dict.fromkeys(out))


def malay_words(lines):
    """Number of Malay words inside «…» spans (for listening-length minimums)."""
    return sum(len(tokens(span)) for line in lines for span in TARGET.findall(line))


def english_words(lines):
    return sum(len(re.findall(r"[A-Za-z0-9āÀ-ÿ'’-]+", strip(line))) for line in lines)


def vocab(ledger, groups):
    """Vocabulary lines from ledger rows: term, EN and JA meanings, ledger ID, example."""
    lines = []
    for heading, entries in groups:
        lines.append('■ ' + heading)
        for entry in entries:
            lid, example = entry[0], entry[1]
            opts = entry[2] if len(entry) > 2 else {}
            r = ledger.row(lid)
            term = opts.get('display') or '«' + r['Malay'] + '»'
            en = opts.get('en') or GLOSS.get(lid, {}).get('en') or r['Meaning (EN)']
            ja = opts.get('ja') or GLOSS.get(lid, {}).get('ja') or r['Meaning (JA)']
            lines.append(f'{term} — {en} · {ja}  [{lid}]')
            lines.append('   e.g. ' + example)
    return lines


# Ledger glosses that contain Malay examples, re-marked so the Malay is checked.
GLOSS = {
    'L-0983': dict(en='also, too (after the word: «Saya pun baik»)'),
    'L-0988': dict(en='yes/no question opener («Adakah …?» = Is it …?)'),
    'L-0783': dict(en='Can …? / May I …? (polite)', ja='「〜できますか・〜してもいいですか」（«boleh» のていねいな形）'),
    'L-1016': dict(en='language («bahasa Melayu» = the Malay language)', ja='言語（«bahasa Melayu»＝マレー語）'),
    'L-1017': dict(en='Malay («bahasa Melayu», «orang Melayu»)', ja='マレー（«bahasa Melayu»＝マレー語）'),
    'L-1018': dict(en='English («bahasa Inggeris»)', ja='英語（«bahasa Inggeris»）'),
    'L-1020': dict(en='film, movie'),
    'L-1023': dict(en='to cook («suka masak» = like cooking)'),
    'L-1025': dict(en='the club-and-ball sport («main golf» = play golf)'),
    'L-1024': dict(en='singing along to recorded music (loan from Japanese)'),
    'L-0968': dict(en='the shuttlecock sport'),
    'L-1029': dict(en='to go on trips (spoken English loan)'),
    'L-1030': dict(en='walking in the hills (spoken English loan)'),
    'L-0193': dict(en='already, done (standard «sudah»; spoken «dah»)'),
    'L-0202': dict(en='to go back, return home («balik» everyday; «pulang» also common in writing)'),
    'L-0213': dict(en='to want (spoken «nak»)'),
    'L-0215': dict(en='but (spoken «tapi»)'),
    'L-1009': dict(en='why'),
    'L-1051': dict(en='rent («sewa … setiap bulan» = rent every month)', ja='家賃・賃貸料（«sewa … setiap bulan»＝毎月の家賃）'),
    'L-1060': dict(en='straight on («jalan terus», «pergi terus», «terus depan»)', ja='まっすぐ（«jalan terus»・«pergi terus»・«terus depan»）'),
    'L-1063': dict(en='per month, a month («tiga ribu ringgit sebulan»)', ja='月に・1か月（«tiga ribu ringgit sebulan»）'),
    'L-1064': dict(en='a rice dish: rice cooked in coconut milk, with sambal and other sides', ja='ナシレマ（ココナッツミルクで炊いたご飯。サンバルなどが付く）'),
    'L-1066': dict(en='to add; more («Tambah satu lagi.» = one more)', ja='追加する・もう一つ（«Tambah satu lagi.»＝もう一つ追加）'),
    'L-1067': dict(en='counter for large objects, buildings, vehicles and books («dua buah kereta»)', ja='大きな物・建物・乗り物・本などを数える助数詞（«dua buah kereta»）'),
    'L-1068': dict(en='banana fritters (standard «pisang goreng»; everyday «goreng pisang»)', ja='揚げバナナ（標準は «pisang goreng»、日常は «goreng pisang»）'),
    'L-1069': dict(en='a chewy fish-sausage snack (a Terengganu speciality)', ja='魚のすり身のソーセージ状のおやつ（トレンガヌ名物）'),
    'L-1052': dict(en='room («bilik tidur» = bedroom, «bilik air» = bathroom)', ja='部屋（«bilik tidur»＝寝室、«bilik air»＝浴室）'),
    'L-1076': dict(en='to make, to do (everyday root; «dibuat» = made)', ja='作る・する（日常の語根；«dibuat»＝作られた）'),
    'L-1077': dict(en='to call («dipanggil» = called)', ja='呼ぶ（«dipanggil»＝呼ばれた）'),
    'L-1078': dict(en='to wash («dicuci» = washed)', ja='洗う（«dicuci»＝洗われた）'),
    'L-1079': dict(en='to forbid («dilarang» = forbidden)', ja='禁じる（«dilarang»＝禁止されている）'),
    'L-1081': dict(en='come; let\'s («Mari makan» = come and eat)', ja='さあ・〜しましょう（«Mari makan»＝どうぞ召し上がれ）'),
    # Chapter 10 (fast pack word list): ledger meanings that contain Malay, re-marked.
    'L-1101': dict(en='to have breakfast (standard; «sarapan» alone is everyday)', ja='朝食をとる（標準；日常は «sarapan»）'),
    'L-0779': dict(en='to be neighbours, to live as neighbours (‹hidup berjiran› = neighbourly living)', ja='隣同士で暮らす（‹hidup berjiran›＝近所付き合い）'),
    'L-0941': dict(en='to count; «Kira!» = the bill, please', ja='数える・（店で）お会計'),
    'L-0935': dict(en='a flaky flatbread eaten with curry', ja='ロティ・チャナイ（カレーで食べる薄焼きパン）'),
    'L-1179': dict(en='switch on (a request; «buka» is everyday for lights and aircon)', ja='つけてください（照明やエアコンの日常語は «buka»）'),
    'L-1180': dict(en='switch off (a request; «tutup» is everyday for lights and aircon)', ja='消してください（照明やエアコンの日常語は «tutup»）'),
    'L-1114': dict(en='to move home (standard; spoken «pindah»)', ja='引っ越す（標準；話し言葉は «pindah»）'),
}


def core(ledger, ids):
    """Compact word list for fast-course packs: term, meanings, ledger ID (no example)."""
    out = []
    for lid in ids:
        r = ledger.row(lid); g = GLOSS.get(lid, {})
        out.append(f'«{r["Malay"]}» — {g.get("en", r["Meaning (EN)"])} · {g.get("ja", r["Meaning (JA)"])}  [{lid}]')
    return out


def pattern(n, fid, box, examples, en, ja, helps_en, helps_ja):
    """A pattern-focus section: box, numbered Q&A examples, explanation (EN, JA), Japanese bridge (EN, JA)."""
    return (f'Pattern {n} · {fid}', [
        'Pattern box: ' + box,
        *[f'{i}. {ex}' for i, ex in enumerate(examples, 1)],
        'Explanation: ' + en, '説明：' + ja,
        'Japanese helps or misleads: ' + helps_en, '日本語との比較：' + helps_ja])


def turns(script):
    """Dialogue lines: (speaker, line); a None speaker is a stage direction."""
    return [f'{s}: {t}' if s else '— ' + t for s, t in script]


def load_units():
    from . import ms_c01, ms_c02a, ms_c02b, ms_c03a, ms_c03b, ms_c03c, ms_c04a, ms_c04b, ms_c05, ms_c06, ms_c07, ms_c08, ms_c09, fast, stage1
    from . import ms_c10a, ms_c10b, ms_c11a, ms_c11b, ms_c12a, ms_c12b
    return [u for u in [ms_c01.UNIT, ms_c02a.UNIT, ms_c02b.UNIT,
                       ms_c03a.UNIT, ms_c03b.UNIT, ms_c03c.UNIT, ms_c04a.UNIT, ms_c04b.UNIT, ms_c05.UNIT, ms_c06.UNIT, ms_c07.UNIT, ms_c08.UNIT, ms_c09.UNIT,
                       *fast.PACKS, stage1.UNIT, ms_c10a.UNIT, ms_c10b.UNIT, ms_c11a.UNIT, ms_c11b.UNIT, ms_c12a.UNIT, ms_c12b.UNIT, *fast.STAGE2_PACKS] if u]


SKILLS = {'Opener': ['speaking'], 'Vocabulary': ['vocabulary'], 'Pattern and grammar': ['grammar'],
          'Drill': ['grammar', 'speaking'], 'Model conversation': ['speaking', 'reading'],
          'Listening': ['listening'], 'Reading and writing': ['reading', 'writing'], 'Task': ['speaking'],
          'Culture note': ['reading'], 'Test': ['listening', 'vocabulary', 'grammar', 'reading', 'speaking'],
          'Teaching plan': [], 'Fast-course pack': ['vocabulary', 'grammar', 'speaking']}
KIND = {'Opener': 'opener', 'Vocabulary': 'vocabulary', 'Pattern and grammar': 'model', 'Drill': 'drill',
        'Model conversation': 'model', 'Listening': 'listening', 'Reading and writing': 'reading',
        'Task': 'task', 'Culture note': 'culture', 'Test': 'test', 'Teaching plan': 'plan', 'Fast-course pack': 'model'}


def build_suite(ledger=None):
    """Return lesson dicts (unpaginated: 'sections') and unit records."""
    ledger = ledger or Ledger()
    lessons = []; units = []
    for unit in load_units():
        unit = dict(unit)
        comps = unit['components'](ledger) if callable(unit['components']) else unit['components']
        if unit['chapter_id'] == 'ms-c03':
            from .chapter3_common import mark_ch3
            for c in comps:
                c['sections'] = [(sec[0], [mark_ch3(line, ledger) for line in sec[1]], *sec[2:])
                                 for sec in c['sections']]
                c['key'] = [mark_ch3(line, ledger) for line in c['key']]
                c['explain'] = tuple(mark_ch3(line, ledger) for line in c['explain'])
                for test in c.get('tests', []):
                    for field in ('prompt', 'answer'):
                        test[field] = mark_ch3(test[field], ledger)
        titles = []
        for comp in comps:
            ctype = comp['type']
            kind_label = ctype
            title = unit['title_prefix'] + ' · ' + comp['title']
            cid = unit['id_prefix'] + '-' + comp['slug']
            meta = dict(
                id=cid, unit_id=unit.get('unit_id'), chapter_id=unit['chapter_id'], unit_label=unit.get('label'),
                check_unit=unit['check_unit'], component_type=ctype, sub_type=comp.get('sub_type'),
                skills=comp.get('skills') or SKILLS[kind_label], block=comp.get('block'),
                time_minutes=comp.get('minutes'), course_path=comp.get('course_path', unit.get('course_path', 'full')),
                grammar_points=comp.get('grammar', []), pattern_ids=comp.get('patterns', []),
                word_ids_override=comp.get('words'), genre=unit['genre'],
                can_do_goal=comp.get('goal'), prerequisite_chapters=unit.get('prerequisites', []),
                prerequisite_units=unit.get('prerequisite_units', []),
                prerequisite_grammar=comp.get('prereq_grammar', unit.get('prereq_grammar', [])),
                unit_word_scope=unit.get('word_scope'), menu_title=unit['menu_title'])
            tests = []
            for n, item in enumerate(comp.get('tests', []), 1):
                tests.append(dict(id=f'{cid}-{n:02}', chapter_id=unit['chapter_id'], component_id=cid,
                                  sub_type=item['sub_type'], grammar_points=item.get('grammar', []),
                                  word_ids=ledger.ids_for(item.get('words', [])),
                                  prompt=item['prompt'], answer_key=item['answer'], review_status='draft'))
            meta['tests'] = tests
            explain = comp['explain']
            level = unit.get('level', 'A1')
            lesson = dict(title=title, lang='Malay', level=level, kind=kind_label, style='compact',
                          header=f'Cikgu, Sensai! / Malay · {level} · {unit["header"]} · {ctype}'
                                 + (f' · {comp["minutes"]} min' if comp.get('minutes') else '')
                                 + ' · Draft (Japanese awaiting native review)',
                          explainers=[('日本語', [explain[0], JA_DRAFT]), ('Bahasa Melayu', [BM_NOTE if level == 'A1' else BM_NOTE_STAGE2]),
                                      ('English', [explain[1]])],
                          sections=[(s[0], s[1], s[2] if len(s) > 2 else KIND.get(ctype, 'model'))
                                    for s in comp['sections']],
                          key=comp['key'], suite=meta)
            lessons.append(lesson); titles.append(title)
        units.append(dict(unit, titles=titles))
    return lessons, units


def paginate(lesson, fits):
    """Pack sections densely onto pages. A section that starts mid-page gets a
    "■" sub-heading; a page that starts mid-section is labelled "(cont.)".
    The raw (marked) text and its scope kind are kept per line."""
    explainers = [(label, [(x, 'explainer') for x in lines]) for label, lines in lesson['explainers']]
    stream = []
    for label, lines, kind in lesson['sections']:
        stream.append((None, label, kind))
        stream.extend((line, label, kind) for line in lines)
    body = []; label = None; current = []; section = None
    def flush():
        if current:
            body.append((label, list(current)))
    for line, sec, kind in stream:
        if line is None:
            section = sec
            item = None if not current else ('■ ' + sec, 'heading')
            if not current:
                label = sec
            if item is None:
                continue
        else:
            item = (line, kind)
        trial = current + [item]
        if fits(lesson, label, [strip(x) for x, k in trial]):
            current.append(item); continue
        # Start a new page; never leave a sub-heading orphaned at the bottom.
        carry = []
        if current and current[-1][1] == 'heading':
            carry = [current.pop()]
        if not current:
            raise ValueError(f'Line too long for one page: {lesson["title"]}: {line}')
        flush()
        if item[1] == 'heading':
            label, current = sec, []
        elif carry:
            label, current = carry[0][0][2:], [item]
        else:
            label, current = sec + ' (cont.)', [item]
        if not fits(lesson, label, [strip(x) for x, k in current]):
            raise ValueError(f'Line too long for one page: {lesson["title"]}: {line}')
    flush()
    keys = []; chunk = []
    for line in lesson['key']:
        if chunk and not fits(lesson, 'Teacher key (9/9)', [strip(x) for x, k in chunk + [(line, 'key')]]):
            keys.append(chunk); chunk = []
        chunk.append((line, 'key'))
    keys.append(chunk)
    keys = [('Teacher key' if len(keys) == 1 else f'Teacher key ({n}/{len(keys)})', c) for n, c in enumerate(keys, 1)]
    lesson['key_pages'] = len(keys)
    pages = explainers + body + keys
    for label, lines in pages:
        if not fits(lesson, label, [strip(x) for x, k in lines]):
            raise ValueError(f'Page overflow: {lesson["title"]} · {label}')
    lesson['pages'] = [dict(label=label, lines=[strip(x) for x, k in lines]) for label, lines in pages]
    lesson['_raw'] = [lines for label, lines in pages]
    del lesson['sections'], lesson['explainers'], lesson['key']


def guard(source, text, ledger, mentions):
    """Fail on Malay that is not marked, and on mentions without an approved source."""
    targets, said = marked(text)
    for m in said:
        if norm(m) not in mentions:
            raise ValueError(f'Mention ‹{m}› is not in curriculum/malay-mentions.json ({source})')
    rest = MENTION.sub(' ', TARGET.sub(' ', text))
    for name in PRODUCT_NAMES:
        rest = rest.replace(name, ' ')
    words = set(tokens(rest)) - ledger.checker.proper
    malay = [w for w in words if w in ledger.checker.entries and w not in ENGLISH_HOMOGRAPHS]
    if malay:
        raise ValueError(f'Unmarked Malay {sorted(malay)} in {source}: {text}')


def authored_scope(lessons, ledger):
    """Scope entries for the checker, generated from the markup. Keys match the bank."""
    mentions = {norm(k) for k in json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']}
    scope = {}; errors = []
    def safe_guard(source, raw):
        try:
            guard(source, raw, ledger, mentions)
        except ValueError as e:
            errors.append(str(e))
    for lesson in lessons:
        for pi, raw_lines in enumerate(lesson['_raw']):
            for li, (raw, kind) in enumerate(raw_lines):
                source = f'{lesson["title"]}|{pi}|{li}'
                safe_guard(source, raw)
                targets, said = marked(raw)
                scope[source] = dict(source_text=strip(raw), target_spans=targets, mention_spans=said,
                                     kind=kind, exclusion=None if targets else 'Japanese/English (marked source)')
        for item in lesson['suite']['tests']:
            for field in ('prompt', 'answer_key'):
                raw = item[field]
                safe_guard('test:' + item['id'], raw)
                targets, said = marked(raw)
                item[field] = strip(raw)
                scope[f'test:{item["id"]}|{field}'] = dict(source_text=item[field], target_spans=targets,
                                                           mention_spans=said, kind='test', exclusion=None)
    if errors:
        raise ValueError('\n'.join(errors))
    return scope


def component_words(lesson, ledger, units):
    """Word IDs traced from the marked Malay of a component (all pages), and the
    subset that earlier chapters or units teach (its prerequisite words)."""
    found = []
    for raw_lines in lesson['_raw']:
        for raw, kind in raw_lines:
            for span in marked(raw)[0]:
                found.extend(ledger.terms_in(span))
    rows = list({r['ID']: r for r in found}.values())
    meta = lesson['suite']
    chapter = int(meta['chapter_id'][-2:])
    earlier_units = {lid for u in units if u.get('unit_id') in meta['prerequisite_units'] for lid in u.get('word_scope', [])}
    def placed(r):
        return min([int(x) for x in re.findall(r'Ch\s*(\d+)', r['Kata-Kata place'])] or [99])
    meta['word_ids'] = list(dict.fromkeys(ledger.word_id(r) for r in rows))
    meta['prereq_word_ids'] = list(dict.fromkeys(ledger.word_id(r) for r in rows
                                                 if placed(r) < chapter or r['ID'] in earlier_units))
