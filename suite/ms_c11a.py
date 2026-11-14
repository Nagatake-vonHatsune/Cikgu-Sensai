"""Unit 11A: meN- verbs at the office: reading, writing, sending, receiving, buying and paying (Aini ___ buku itu; Buku itu
___ oleh Aini; Siapa yang ___ fail itu?; Awak sedang ___ apa?).

21 core ledger entries, the rows the ledger places in "Ch11 (unit 11A)" (L-1123 to L-1142, and L-1277 «kepada», approved by Sam on 14 Nov 2026), in three groups. Each meN- verb is
taught as a whole ledger form, with its root, the chapter of the root, the nasal change and its chapter 9 «di-» partner where
one exists, as the Kata-Kata chapter 11 card notes give them. This unit teaches the spelling of meN- before b, c, d, h, j, l,
m, t, p and a vowel; unit 11B adds s, k and the one-syllable roots (menyewa, mengira, mengecas). No meN-...-kan or meN-...-i
form (chapter 12). The scene follows Kata-Kata c11 (scenario lines ms-c11-s01 to s08: emails and files with Puan Aini,
Encik Rahman and Cik Mei Ling) and goes further in class: a team message, a "who did what" role-play and a changed
morning. No Dunia scene primes chapter 11, so the unit has no recognition word. All names, times and files are fictional.
Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

DOC = ['L-1124', 'L-1125', 'L-1136', 'L-1137', 'L-1129', 'L-1130', 'L-1138', 'L-1277']
BUY = ['L-1123', 'L-1142', 'L-1132', 'L-1131', 'L-1127', 'L-1133']
DAILY = ['L-1139', 'L-1140', 'L-1135', 'L-1141', 'L-1126', 'L-1134', 'L-1128']
CORE = DOC + BUY + DAILY

# Revision: words placed in chapters 1 to 10 that the unit really uses (a test fails if one is not used).
REV_ROOTS = ['L-0474', 'L-0475', 'L-0528', 'L-0481', 'L-0484', 'L-0485', 'L-0128',              'L-0496', 'L-1023', 'L-1077']
REV_PASSIVE = ['L-0385', 'L-0381', 'L-0386', 'L-0390', 'L-0387', 'L-0380', 'L-0377']
REV_OFFICE = ['L-0526', 'L-0525', 'L-0097', 'L-0096', 'L-0064', 'L-0090', 'L-0208', 'L-0581', 'L-0577']
REV_TIME = ['L-0189', 'L-0193', 'L-0194', 'L-0192', 'L-0195', 'L-0191', 'L-0379', 'L-0161', 'L-0320', 'L-1001', 'L-1002', 'L-0182']

EXAMPLES = {
    # Reading, writing and files
    'L-1124': '«Puan Aini membaca emel itu.» (spoken: «Puan Aini baca emel itu.»)',
    'L-1125': '«Encik Rahman sedang menulis jawapan.»',
    'L-1136': '«Siapa yang menghantar fail itu?» (also: «Saya menghantar anak ke sekolah.»)',
    'L-1277': '«Saya menghantar emel kepada pengurus.» («kepada» for a person, «ke» for a place: «Saya pergi ke pejabat.»)',
    'L-1137': '«Encik Rahman menerima fail itu.»',
    'L-1129': '«Sekarang dia sedang membuka fail itu.»',
    'L-1130': '«Tolong tutup pintu.» → «Dia menutup pintu bilik mesyuarat.»',
    'L-1138': '«Saya menjawab soalan itu.»',
    # Buying, paying and carrying
    'L-1123': '«Saya membeli nasi lemak di gerai.»',
    'L-1142': '«Kedai itu menjual baju dan kasut.»',
    'L-1132': '«Siapa yang membayar kopi ini?»',
    'L-1131': '«Saya membawa payung hari ini.»',
    'L-1127': '«Saya mengambil fail itu dari atas meja.»',
    'L-1133': '«Saya mencari bilik mesyuarat.»',
    # Senses, calling and everyday tasks
    'L-1139': '«Saya melihat jam. Sudah pukul sembilan.» (spoken: «tengok»)',
    'L-1140': '«Saya mendengar lagu di rumah.»',
    'L-1135': '«Pengurus memanggil Encik Tanaka.»',
    'L-1141': '«Saya menunggu bas di stesen.»',
    'L-1126': '«Isteri saya memasak nasi lemak.»',
    'L-1134': '«Dia mencuci pinggan di dapur.»',
    'L-1128': '«Siapa yang membuat kek ini?»',
    # Revision · roots and their «di-» partners
    'L-0474': '«baca» → «membaca» / «dibaca»: «Fail itu dibaca oleh Encik Rahman.»',
    'L-0475': '«tulis» → «menulis» / «ditulis»: «Surat itu ditulis oleh Cik Mei Ling.»',
    'L-0528': '«hantar» → «menghantar» / «dihantar»: «Fail itu dihantar oleh Puan Aini.»',
    'L-0481': '«ambil» → «mengambil» / «diambil»: «Fail itu diambil oleh Encik Rahman.»',
    'L-0484': '«buka» → «membuka» / «dibuka»: «Pintu itu dibuka oleh Encik Rahman.»',
    'L-0485': '«tutup» → «menutup» / «ditutup»: «Pintu itu ditutup oleh Cik Mei Ling.»',
    'L-0128': '«beli» → «membeli» / «dibeli»: «Kopi ini dibeli oleh Encik Tanaka.»',
    'L-0496': '«tunggu» → «menunggu»: «Saya menunggu jawapan itu.»',
    'L-1023': '«masak» → «memasak» / «dimasak»: «Kuih itu dimasak oleh isteri saya.»',
    'L-1077': '«panggil» → «memanggil» / «dipanggil»: «Encik Tanaka dipanggil oleh pengurus.»',
    # Revision · the «di-» partners and the object
    'L-0385': '«Emel itu dibaca oleh Puan Aini.»',
    'L-0381': '«Kopi ini dibeli oleh Encik Tanaka.»',
    'L-0386': '«Jawapan itu ditulis oleh Encik Rahman.»',
    'L-0390': '«Fail itu dihantar oleh Puan Aini.»',
    'L-0387': '«Pintu itu dibuka oleh Encik Rahman.»',
    'L-0380': '«Kek ini dibuat oleh isteri saya.»',
    'L-0377': '«Fail itu dihantar oleh Puan Aini.»',
    # Revision · the office
    'L-0526': '«Saya membaca emel itu pagi tadi.»',
    'L-0525': '«Saya menghantar fail itu.»',
    'L-0097': '«Saya menunggu jawapan itu.»',
    'L-0096': '«Saya menjawab soalan itu.»',
    'L-0064': '«Saya sampai di pejabat pukul sembilan.»',
    'L-0090': '«Pengurus memanggil Encik Tanaka.»',
    'L-0208': '«Mesyuarat bermula pukul sebelas.»',
    'L-0581': '«Saya mencari kata laluan.»',
    'L-0577': '«Saya tengok jam.» (spoken for «melihat»)',
    # Revision · time and markers
    'L-0189': '«Saya sedang menulis emel.»',
    'L-0193': '«Saya sudah membuka fail itu.»',
    'L-0194': '«Saya belum membaca emel itu.»',
    'L-0192': '«Saya akan menelefon mereka petang ini.»',
    'L-0195': '«Saya baru menerima fail itu.»',
    'L-0191': '«Saya masih menunggu jawapan itu.»',
    'L-0379': '«Saya membaca emel itu pagi tadi.»',
    'L-0161': '«Sekarang dia sedang membuka fail itu.»',
    'L-0320': '«Saya membaca emel itu, kemudian saya menghantar fail itu.»',
    'L-1001': '«Saya membaca emel itu selepas makan tengah hari.»',
    'L-1002': '«Saya membaca emel itu sebelum mesyuarat.»',
    'L-0182': '«Setiap pagi saya membaca emel.»',
}

# For each meN- verb: the root as the Kata-Kata card note gives it, the chapter of the root, the nasal change, the chapter 9
# «di-» partner. «…» where the root is a ledger word placed by chapter 11, ‹…› where it is not (the whole-word verbs).
# (root, where the root sits, English change, Japanese change, passive)
ROOTS = {
    'L-1123': ('«beli»', 'chapter 3', '‹mem-› before b', '‹mem-›（b の前）', '«dibeli»'),
    'L-1124': ('«baca»', 'Dunia, chapter 4', '‹mem-› before b', '‹mem-›（b の前）', '«dibaca»'),
    'L-1125': ('«tulis»', 'Dunia, chapter 4', 'the t drops: «menulis»', 't が落ちる', '«ditulis»'),
    'L-1126': ('«masak»', 'chapter 2', '‹me-› before m: the root keeps its m', '‹me-›（m の前：語根の m は残る）', '«dimasak»'),
    'L-1127': ('«ambil»', 'Dunia, chapter 4', '‹meng-› before a vowel', '‹meng-›（母音の前）', '«diambil»'),
    'L-1128': ('«buat»', 'chapter 9', '‹mem-› before b', '‹mem-›（b の前）', '«dibuat»'),
    'L-1129': ('«buka»', 'Dunia, chapter 4', '‹mem-› before b', '‹mem-›（b の前）', '«dibuka»'),
    'L-1130': ('«tutup»', 'Dunia, chapter 4', 'the t drops: «menutup»', 't が落ちる', '«ditutup»'),
    'L-1131': ('«bawa»', 'Dunia, chapter 4', '‹mem-› before b', '‹mem-›（b の前）', '«dibawa»'),
    'L-1132': ('«bayar»', 'chapter 3', '‹mem-› before b', '‹mem-›（b の前）', '«dibayar»'),
    'L-1133': ('«cari»', 'Dunia, chapter 7', '‹men-› before c', '‹men-›（c の前）', None),
    'L-1134': ('«cuci»', 'chapter 9', '‹men-› before c', '‹men-›（c の前）', '«dicuci»'),
    'L-1135': ('«panggil»', 'chapter 9', 'the p drops: «memanggil»', 'p が落ちる', '«dipanggil»'),
    'L-1136': ('«hantar»', 'Dunia, chapter 2', '‹meng-› before h', '‹meng-›（h の前）', '«dihantar»'),
    'L-1137': ('‹terima›', 'learn the whole word', 'the t drops: «menerima»', 't が落ちる', None),
    'L-1138': ('«jawab»', 'Dunia, chapter 2', '‹men-› before j', '‹men-›（j の前）', None),
    'L-1139': ('‹lihat›', 'learn the whole word', '‹me-› before l', '‹me-›（l の前）', None),
    'L-1140': ('«dengar»', 'Dunia, chapter 4', '‹men-› before d', '‹men-›（d の前）', None),
    'L-1141': ('«tunggu»', 'chapter 4', 'the t drops: «menunggu»', 't が落ちる', None),
    'L-1142': ('«jual»', 'chapter 3', '‹men-› before j', '‹men-›（j の前）', '«dijual»'),
}
_EN = {'L-1123': 'to buy', 'L-1124': 'to read', 'L-1125': 'to write', 'L-1126': 'to cook', 'L-1127': 'to take, to collect',
       'L-1128': 'to make, to do', 'L-1129': 'to open', 'L-1130': 'to close, to shut', 'L-1131': 'to bring, to carry',
       'L-1132': 'to pay', 'L-1133': 'to look for', 'L-1134': 'to wash', 'L-1135': 'to call someone',
       'L-1136': 'to send, to deliver (also: to take or drop someone off)', 'L-1137': 'to receive', 'L-1138': 'to answer',
       'L-1139': 'to see (everyday speech says «tengok»)', 'L-1140': 'to hear, to listen to', 'L-1141': 'to wait',
       'L-1142': 'to sell'}
_JA = {'L-1123': '買う', 'L-1124': '読む', 'L-1125': '書く', 'L-1126': '料理する', 'L-1127': '取る・受け取る', 'L-1128': '作る・する',
       'L-1129': '開ける', 'L-1130': '閉める', 'L-1131': '持ってくる・運ぶ', 'L-1132': '支払う', 'L-1133': '探す', 'L-1134': '洗う',
       'L-1135': '人を呼ぶ', 'L-1136': '送る・届ける（人を送り届ける意味もある）', 'L-1137': '受け取る', 'L-1138': '答える',
       'L-1139': '見る（日常の話し言葉は «tengok»）', 'L-1140': '聞く（耳に入る・耳を傾ける）', 'L-1141': '待つ', 'L-1142': '売る'}


def _where_ja(where):
    import re
    if where is None:
        return None
    if where == 'this chapter':
        return '本章'
    if where == 'this chapter, spoken':
        return '本章・話し言葉'
    m = re.fullmatch(r'(Dunia, )?chapter (\d+)', where)
    return ('Dunia・' if m.group(1) else '') + f'第{m.group(2)}章'


def _opts(lid):
    root, where, change, change_ja, passive = ROOTS[lid]
    if root.startswith('‹'):
        en_root = f'‹meN-› + {root} (learn the whole word; the root has no class card of its own)'
        ja_root = f'‹meN-› ＋ {root}（一語まるごと覚える）'
    else:
        en_root = f'‹meN-› + {root} ({where})'
        ja_root = f'‹meN-› ＋ {root}（{_where_ja(where)}）'
    en = f'{_EN[lid]} ({en_root}; {change}' + (f'; passive {passive}, chapter 9)' if passive else '; no taught «di-» partner)')
    ja = f'{_JA[lid]}（{ja_root}；{change_ja}' + (f'；受け身 {passive}、第9章）' if passive else '；受け身は習わない）')
    return {'en': en, 'ja': ja}


VOCAB_OPTS = {lid: _opts(lid) for lid in ROOTS}
VOCAB_OPTS['L-1277'] = {'en': 'to (a person): «menghantar emel kepada pengurus» («kepada» for a person, «ke» for a place, chapter 7)',
                        'ja': '（人）に：«menghantar emel kepada pengurus»（人には «kepada»、場所には «ke»、第7章）'}

P = [
    ('ms-c11-f01', '«Aini» ___ «buku itu.»  (doer + meN- verb + the thing)', [
        'A: «Puan Aini membaca emel itu?» B: «Ya. Puan Aini membaca emel itu pagi tadi.»',
        'A: «Encik Rahman membuka fail itu?» B: «Ya. Dia membuka fail itu sekarang.»',
        'A: «Encik Tanaka menulis jawapan itu?» B: «Tidak. Encik Rahman menulis jawapan itu.»',
        'A: «Awak membeli apa di gerai?» B: «Saya membeli nasi lemak dan teh tarik.»',
        'A: «Cik Mei Ling membawa payung?» B: «Ya. Dia membawa payung kerana hari hujan.»',
        'A: «Awak menghantar apa kepada pengurus?» B: «Saya menghantar emel kepada pengurus.»'],
     "A meN- verb is a root with ‹meN-› in front: «baca» → «membaca», «tulis» → «menulis». The doer comes first, then the verb, "
     "then the thing, with no little word for it: «Aini membaca buku itu.» (the Kata-Kata frame) or «Puan Aini membaca emel itu.» Only the front changes shape, and the first sound of "
     "the root decides how. ‹mem-› before b («membeli», «membaca», «membuat», «membuka», «membawa», «membayar»); ‹men-› before c, d "
     "and j («mencari», «mencuci», «mendengar», «menjawab», «menjual»); ‹meng-› before h or a vowel («menghantar», «mengambil»); "
     "‹me-› before l and m («melihat», «memasak»: the m of «masak» stays). With t and p the first sound drops out: «tulis» → "
     "«menulis», «tutup» → «menutup», «tunggu» → «menunggu», «panggil» → «memanggil». Unit 11B adds s, k and one-syllable roots. "
     "In everyday speech people often leave meN- off: «Puan Aini baca emel itu» (spoken). The meN- form is the standard, so say it "
     "first; the verb never changes for who or when («sedang», «sudah» and «akan» do that job).",
     "meN- の動詞は、語根の前に ‹meN-› を付けた形です：«baca» → «membaca»、«tulis» → «menulis»。動作主が先、次に動詞、最後に物が来て、"
     "「を」にあたる語はありません：«Puan Aini membaca emel itu.» 形が変わるのは前の部分だけで、語根の最初の音で決まります。b の前は ‹mem-›"
     "（«membeli»・«membaca»・«membuat»・«membuka»・«membawa»・«membayar»）、c・d・j の前は ‹men-›（«mencari»・«mencuci»・«mendengar»・«menjawab»・«menjual»）、"
     "h か母音の前は ‹meng-›（«menghantar»・«mengambil»）、l と m の前は ‹me-›（«melihat»・«memasak»：«masak» の m は残ります）。t と p は最初の音が落ちます："
     "«tulis» → «menulis»、«tutup» → «menutup»、«tunggu» → «menunggu»、«panggil» → «memanggil»。s・k・一音節の語根は11Bで習います。"
     "日常会話では meN- を付けないこともよくあります：«Puan Aini baca emel itu»（話し言葉）。標準は meN- の形なので、まずこちらを言います。"
     "動詞は人や時で形が変わらず、«sedang»・«sudah»・«akan» が時を表します。",
     'Japanese verbs have no prefix, so the nasal change is new, but the order doer + verb + thing matches 〜が〜を〜する. Two things '
     'mislead: ‹meN-› is not ます (it adds no politeness and no past), and there is no を: the thing follows the verb directly.',
     '日本語の動詞には接頭辞がないので鼻音の変化は初めてですが、動作主＋動詞＋物の順は「〜が〜を〜する」と同じです。ただし二点に注意：‹meN-› は「ます」では'
     'なく（ていねいさも過去も表しません）、「を」にあたる語もないので、物は動詞のすぐあとに置きます。'),
    ('ms-c11-f02', '«Buku itu» ___ «oleh Aini.»  (the thing + «di-» verb + «oleh» + the doer)', [
        'A: «Siapa yang membaca emel itu?» B: «Emel itu dibaca oleh Puan Aini.»',
        'A: «Fail itu dihantar oleh siapa?» B: «Fail itu dihantar oleh Puan Aini.»',
        'A: «Kek ini dibuat oleh siapa?» B: «Kek ini dibuat oleh isteri saya.»',
        'A: «Pintu itu dibuka oleh siapa?» B: «Pintu itu dibuka oleh Encik Rahman.»',
        'A: «Kopi ini dibayar oleh siapa?» B: «Kopi ini dibayar oleh Cik Mei Ling.»',
        'A: «Surat itu ditulis oleh Encik Tanaka?» B: «Ya. Surat itu ditulis oleh Encik Tanaka.»'],
     "Chapter 9 gave you the «di-» verb: the thing comes first and «oleh» introduces the doer. It is the same event as the meN- line: "
     "«Aini membaca buku itu.» = «Buku itu dibaca oleh Aini.» and «Puan Aini membaca emel itu.» = «Emel itu dibaca oleh Puan Aini.» Choose by what you want to talk about: the doer first "
     "(meN-) or the thing first («di-»). Notice that the nasal change disappears in the «di-» form because «di-» is added to the plain "
     "root: «baca» → «membaca» but «dibaca»; «tulis» → «menulis» but «ditulis»; «panggil» → «memanggil» but «dipanggil». Not every "
     "meN- verb has a «di-» partner in this course: «mencari», «menjawab», «melihat», «mendengar», «menunggu» and «menerima» stay "
     "active here.",
     "第9章で習った «di-» の動詞は、物が先に来て、«oleh» のあとに動作主を置きます。meN- の文と同じできごとです："
     "«Puan Aini membaca emel itu.» ＝ «Emel itu dibaca oleh Puan Aini.» 何について話したいかで選びます：動作主が先なら meN-、物が先なら «di-» です。"
     "«di-» の形では鼻音の変化がなくなることに注意してください。«di-» は元の語根に付くからです：«baca» → «membaca» ですが «dibaca»、«tulis» → «menulis» ですが "
     "«ditulis»、«panggil» → «memanggil» ですが «dipanggil»。このコースでは、すべての meN- の動詞に «di-» の相手があるわけではありません："
     "«mencari»・«menjawab»・«melihat»・«mendengar»・«menunggu»・«menerima» は、ここでは能動のまま使います。",
     'Japanese passive (〜に読まれる) is the nearest idea, but the Japanese passive often suggests that something was done to you. '
     'The Malay «di-» form is neutral: «Fail itu dihantar oleh Puan Aini» only says who sent the file. Do not hear a complaint in it.',
     '日本語の受け身（〜に読まれる）がいちばん近い考え方ですが、日本語の受け身は「迷惑を受けた」という意味になることがあります。マレー語の «di-» の形は中立で、'
     '«Fail itu dihantar oleh Puan Aini» は誰が送ったかを言うだけです。不満の気持ちを読み取らないでください。'),
    ('ms-c11-f03', '«Siapa yang» ___ «fail itu?»  (who did it)', [
        'A: «Siapa yang menghantar fail itu?» B: «Puan Aini yang menghantar fail itu.»',
        'A: «Siapa yang menerima fail itu?» B: «Encik Rahman yang menerima fail itu.»',
        'A: «Siapa yang membuka pintu?» B: «Cik Mei Ling yang membuka pintu.»',
        'A: «Siapa yang memanggil Encik Tanaka?» B: «Pengurus yang memanggil Encik Tanaka.»',
        'A: «Siapa yang menjawab soalan itu?» B: «Saya yang menjawab soalan itu.»',
        'A: «Siapa yang menunggu di luar?» B: «Encik Rahman yang menunggu di luar.»'],
     "«Siapa yang» + a meN- verb asks who did something: «Siapa yang menghantar fail itu?» The answer repeats the pattern with the "
     "doer in front of «yang»: «Puan Aini yang menghantar fail itu.» (It was «Puan» Aini who sent the file.) This puts the weight on "
     "the person, which is what the question asks about. A short answer is fine too: «Puan Aini.» You can use the same "
     "frame for «Siapa yang menelefon?» in unit 11B.",
     "«Siapa yang» ＋ meN- の動詞で、誰がしたかをたずねます：«Siapa yang menghantar fail itu?» 答えも同じ形で、«yang» の前に動作主を置きます："
     "«Puan Aini yang menghantar fail itu.»（そのファイルを送ったのはアイニさんです。）人に重点を置く言い方で、質問がたずねている点と合います。"
     "«Puan Aini.» だけの短い答えもかまいません。同じ型は11Bの «Siapa yang menelefon?» にも使えます。",
     'Japanese 誰が〜しましたか and 〜したのはアイニさんです match closely, and the «yang» is the の of 送ったのは. The word order is the '
     'same, so this pattern is easy for Japanese speakers.',
     '日本語の「誰が〜しましたか」と「〜したのはアイニさんです」はよく対応し、«yang» は「送ったのは」の「の」にあたります。語順も同じなので、この型は日本語話者に'
     'とってやさしいです。'),
    ('ms-c11-f05', '«Awak sedang» ___ «apa?»  (what are you doing?)', [
        'A: «Awak sedang menulis apa?» B: «Saya sedang menulis emel.»',
        'A: «Encik sedang membaca apa?» B: «Saya sedang membaca surat khabar.»',
        'A: «Puan Aini sedang mencari apa?» B: «Dia sedang mencari fail itu.»',
        'A: «Awak sedang memasak apa?» B: «Saya sedang memasak nasi dan sup.»',
        'A: «Awak sedang membeli apa?» B: «Saya sedang membeli buah di pasar.»',
        'A: «Awak sedang mendengar apa?» B: «Saya sedang mendengar lagu Melayu.»'],
     "«sedang» (chapter 4) says that the action is happening now, and it goes in front of the meN- verb: «Saya sedang menulis "
     "emel.» The question word «apa» goes at the end and asks about the thing: «Awak sedang menulis apa?» The answer replaces «apa» "
     "with the thing. The other markers work the same way: «Saya sudah menulis emel» (done), «Saya belum menulis emel» (not yet), "
     "«Saya akan menulis emel» (will). The verb never changes.",
     "«sedang»（第4章）は今その動作が進行中であることを表し、meN- の動詞の前に置きます：«Saya sedang menulis emel.» 疑問語 «apa» は最後に置いて物をたずね、"
     "答えでは «apa» を物に置き換えます：«Awak sedang menulis apa?» ほかのマーカーも同じです：«Saya sudah menulis emel»（済み）、"
     "«Saya belum menulis emel»（まだ）、«Saya akan menulis emel»（これから）。動詞は変わりません。",
     'Japanese 〜ている (書いている) is the same idea as «sedang menulis», and the question 何を書いていますか puts the question word '
     'before the verb, but Malay puts «apa» at the end. Say the whole sentence first, then add «apa».',
     '日本語の「〜ている」（書いている）は «sedang menulis» と同じ考え方です。ただし「何を書いていますか」は疑問語が動詞の前に来ますが、マレー語では «apa» が最後に来ます。'
     'まず文全体を言い、そのあとに «apa» を付けましょう。'),
]

# Kata-Kata scenario lines ms-c11-s01 to s08, extended to 14 turns.
DIALOGUE = [
    ('Tanaka', 'Puan Aini, emel dari Jepun itu sudah dibaca?'),
    ('Aini', 'Sudah. Saya membaca emel itu pagi tadi, kemudian saya menghantar fail itu.'),
    ('Tanaka', 'Oh, Encik Rahman yang menerima fail itu?'),
    ('Aini', 'Ya. Sekarang dia sedang membuka fail itu.'),
    ('Rahman', 'Selamat pagi, Encik Tanaka. Saya sudah membuka fail itu. Sekarang saya sedang menulis jawapan.'),
    ('Tanaka', 'Baik. Siapa yang akan menelefon pejabat di Jepun?'),
    ('Rahman', 'Saya akan menelefon mereka petang ini.'),
    ('Aini', 'Baik, encik. Saya menunggu jawapan itu.'),
    ('Tanaka', 'Encik Rahman, siapa yang membuka pintu bilik mesyuarat tadi?'),
    ('Rahman', 'Cik Mei Ling yang membuka pintu itu. Dia juga membawa kopi untuk kita.'),
    ('Aini', 'Siapa yang membeli kopi itu?'),
    ('Rahman', 'Encik Tanaka yang membeli kopi itu. Saya yang membayar kuih.'),
    ('Tanaka', 'Terima kasih, Encik Rahman. Mari kita minum kopi dulu.'),
    ('Aini', 'Baik. Selepas itu saya menghantar jawapan itu ke Jepun.'),
]
VARIANT = [
    ('Rahman', 'Cik Mei Ling, surat daripada bank itu sudah dibaca?'),
    ('Mei Ling', 'Sudah. Saya membaca surat itu semalam, kemudian saya menulis jawapan.'),
    ('Rahman', 'Siapa yang menghantar jawapan itu?'),
    ('Mei Ling', 'Puan Aini yang menghantar jawapan itu. Sekarang bank sedang menerima fail kita.'),
    ('Rahman', 'Baik. Awak sedang mencari apa?'),
    ('Mei Ling', 'Saya mencari pen saya. Awak membawa pen?'),
    ('Rahman', 'Ada. Ambil pen ini.'),
    ('Mei Ling', 'Terima kasih. Nanti saya menjawab emel bank.'),
    ('Rahman', 'Baik. Saya menunggu di bilik mesyuarat.'),
    ('Mei Ling', 'Saya datang sekejap lagi.'),
]
LISTENING = [
    ('Tanaka', 'Encik Rahman, fail dari Osaka itu sudah sampai?'),
    ('Rahman', 'Sudah. Puan Aini menghantar fail itu pukul sembilan, dan saya menerima fail itu pukul sembilan setengah.'),
    ('Tanaka', 'Encik sudah membaca fail itu?'),
    ('Rahman', 'Belum. Fail itu tidak boleh dibuka. Saya sedang mencari kata laluan.'),
    ('Tanaka', 'Siapa yang tahu kata laluan itu?'),
    ('Rahman', 'Cik Mei Ling tahu. Saya memanggil dia sekarang.'),
    ('Tanaka', 'Baik. Kemudian encik menulis jawapan, ya?'),
    ('Rahman', 'Ya. Saya menulis jawapan sebelum makan tengah hari. Selepas itu saya menghantar jawapan itu ke Osaka.'),
    ('Tanaka', 'Pukul berapa mereka menerima jawapan itu?'),
    ('Rahman', 'Lebih kurang pukul dua petang. Selepas itu saya menunggu jawapan mereka.'),
    ('Tanaka', 'Bagus. Siapa yang membuat kopi pagi ini? Kopi itu sedap!'),
    ('Rahman', 'Kopi itu dibuat oleh Puan Aini. Saya membawa kuih dari rumah.'),
    ('Tanaka', 'Wah, isteri encik memasak kuih itu?'),
    ('Rahman', 'Ya. Isteri saya memasak kuih itu semalam.'),
]

CULTURE = [
    'In Malaysia you will hear most of these verbs in two forms. Writing, notices, meetings and polite speech use the meN- form: '
    '«Puan Aini membaca emel itu.» In a relaxed chat many people drop the front and say the root: «Puan Aini baca emel itu», '
    '«Saya tengok jam» for «Saya melihat jam». Both are correct Malaysian Malay. This course teaches the meN- form first, as the '
    'standard, and you will understand the short form when you hear it.',
    'Two verbs need a word of warning. «menerima» and «melihat» are learned as whole words, because their roots ‹terima› and '
    '‹lihat› are not taught on their own in this course (you already know «terima kasih»). And «menghantar» has two everyday uses: '
    'to send a file, and to take someone to a place: «Saya menghantar anak ke sekolah» means that you take your child to school.',
    'In an office, who did what often matters, so you will hear both lines of a pair: the doer first («Puan Aini menghantar fail '
    'itu») when you ask or say who acted, and the thing first («Fail itu dihantar oleh Puan Aini») when the file is what you are '
    'talking about. Neither sounds rude or critical. Choose the one that fits the sentence you want to say.',
    'Japanese colleagues often ask «Sudah dibaca?» or «Sudah dihantar?» to check progress. A short, plain answer such as «Sudah.» '
    'or «Belum.» is polite and clear.',
]
CULTURE_JA = [
    'マレーシアでは、これらの動詞の多くを二つの形で耳にします。書き言葉、掲示、会議、ていねいな会話では meN- の形を使います：«Puan Aini membaca emel itu.»'
    'くだけたおしゃべりでは、前の部分を落として語根だけを言う人も多いです：«Puan Aini baca emel itu»、«Saya melihat jam»の代わりに«Saya tengok jam»。'
    'どちらも正しいマレーシアのマレー語です。このコースでは標準として meN- の形を先に教え、短い形は聞いて分かるようにします。',
    '注意が必要な動詞が二つあります。«menerima» と «melihat» は一語として覚えます。語根の ‹terima› と ‹lihat› は、このコースでは単独では教えないからです'
    '（«terima kasih» はすでに知っています）。また «menghantar» には日常で二つの使い方があります：ファイルを送ることと、人をある場所に連れて行くことです：'
    '«Saya menghantar anak ke sekolah» は、子どもを学校に送っていくという意味です。',
    '職場では、誰が何をしたかが大切なことがよくあるので、ペアの両方の文を耳にします。誰が動いたかをたずねたり言ったりするときは動作主が先'
    '（«Puan Aini menghantar fail itu»）、ファイルについて話すときは物が先（«Fail itu dihantar oleh Puan Aini»）です。どちらも失礼でも批判的でもありません。'
    '言いたい文に合うほうを選びます。',
    '日本人の同僚は、進み具合を確かめるために «Sudah dibaca?» や «Sudah dihantar?» とよくたずねます。«Sudah.» か «Belum.» の短くはっきりした答えで、ていねいで十分です。',
]

CFG = dict(
    chapter=11, label='11A', unit_id='ms-c11a',
    menu_title='Chapter 11 · meN- verbs', genre='Work',
    prerequisite_units=['ms-c10b'], prereq_grammar=['ms-c09-g02', 'ms-c04-g06', 'ms-c10-g02'],
    unit_goal='Say who did what at the office with meN- verbs, ask who sent or received a file, and turn a meN- line into its «di-» partner.',
    core=CORE,
    recognition=[],
    revision=[('Roots of the meN- verbs and «masak», «buat», «panggil», «cuci»', REV_ROOTS), ('The «di-» partners (chapter 9)', REV_PASSIVE),
              ('The office', REV_OFFICE), ('Time and markers', REV_TIME)],
    core_groups=[('Reading, writing and files', DOC), ('Buying, paying and carrying', BUY),
                 ('Senses, calling and everyday tasks', DAILY)],
    grammar_ids={'active': 'ms-c11-g02', 'passive': 'ms-c11-g03', 'who': 'ms-c11-g04', 'now': 'ms-c11-g05',
                 'request': 'ms-c11-g06', 'plans': 'ms-c11-g07', 'spelling': 'ms-c11-g08'},
    grammar=['active', 'passive', 'who', 'now', 'spelling'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 21 cards ms-c11-001 to ms-c11-020 and ms-c11-044', frame_list='ms-c11-f01, f02, f03 and f05', frame_list_ja='f01・f02・f03・f05',
    goals={'A': 'I can say who did what with a taught meN- verb and a thing: «Puan Aini membaca emel itu.»',
           'B': 'I can ask and answer «Siapa yang …?» and «Awak sedang … apa?» with meN- verbs, and turn a meN- line into its «di-» partner.',
           'C': "I can follow a colleague's morning with files and emails, and report who sent, received and opened what.",
           'D': 'I can check the meN- spelling of each verb and its «di-» partner, and correct a short report.',
           'E': 'I can explain who read, sent and received a file in a short role-play, and change one fact.'},
    goals_ja={'A': '習った meN- の動詞と物で、誰が何をしたかを言える。',
              'B': 'meN- の動詞で «Siapa yang …?» と «Awak sedang … apa?» をたずね、答えられる。meN- の文を «di-» の文に言い換えられる。',
              'C': '同僚の朝のファイルやメールの話が分かり、誰が何を送り、受け取り、開けたかを伝えられる。',
              'D': '各 meN- の動詞のつづりと «di-» の相手を確認し、短い報告を直せる。',
              'E': '短いロールプレイで、誰がファイルを読み、送り、受け取ったかを説明し、事実を一つ変えられる。'},
    setting='A Tuesday morning at a fictional Japanese company in Kuala Lumpur: «Encik» Tanaka asks «Puan» Aini and «Encik» Rahman who has '
            'read, sent, received and opened the email and the file from Japan. All names, times and files are fictional.',
    setting_ja='火曜日の朝、クアラルンプールの架空の日本企業。田中さんが、アイニさんとラーマンさんに、日本から来たメールとファイルを誰が読み、送り、受け取り、'
               '開けたかをたずねます。名前・時刻・ファイルはすべて架空です。',
    recall=['Without notes, from chapters 9 and 10: say three things with «di-» (what was made, bought and sent) and three things you do in '
            'the morning with ber- verbs. / 第9章と第10章の復習：«di-» で、作られたもの・買われたもの・送られたものを三つ、ber- の動詞で毎朝することを三つ言いましょう。',
            'Recall prompt: «Kek ini dibuat oleh siapa?» «Fail itu dihantar oleh siapa?» «Pukul berapa encik bersarapan?»'],
    recall_key='e.g. «Kek ini dibuat oleh isteri saya.» «Kopi ini dibeli oleh Encik Tanaka.» «Fail itu dihantar oleh Puan Aini.» «Setiap pagi saya '
               'bersarapan pukul tujuh.» Then show the new standard forms behind «dibuat», «dibeli» and «dihantar»: «membuat», «membeli», «menghantar».',
    patterns=P, pattern_ids=['ms-c11-f01', 'ms-c11-f02', 'ms-c11-f03', 'ms-c11-f05'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 11 frames f01, f02, f03 and f05 (f04 and f06 are unit 11B; f03 and f01 return there).',
    pattern_keys=['Pattern 1: doer + meN- verb + the thing. If a learner says «Puan Aini baca emel itu», accept it as everyday speech and '
                  'model «membaca». Write the front of each verb on the board and let the class find the rule from the first sound of the root.',
                  'Pattern 2: the «di-» partner of the same line. Check that «oleh» comes before the doer and that the nasal change is gone: '
                  '«dibaca», not *dimembaca. Verbs without a taught partner («mencari», «menjawab», «melihat», «mendengar», «menunggu», '
                  '«menerima») stay active.',
                  'Pattern 3: «Siapa yang» + meN- verb. Accept the short answer «Puan Aini.» and the full «Puan Aini yang menghantar fail itu.»',
                  'Pattern 4: «sedang» + meN- verb + «apa» at the end. Combine with «sudah», «belum» and «akan» in the markers drill.'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 6, 9, 11, 13),
    drills={
        'repeat_frame': 'Frame: «Puan Aini» [«membaca» / «menghantar» / «menulis»] [«emel itu» / «fail itu» / «jawapan itu»].',
        'repeat': ['«Puan Aini membaca emel itu.»', '«Emel itu dibaca oleh Puan Aini.»', '«Siapa yang menghantar fail itu?»',
                   '«Encik Rahman yang menerima fail itu.»', '«Sekarang dia sedang membuka fail itu.»',
                   '«Awak sedang menulis apa?»', '«Saya membeli nasi lemak di gerai.»', '«Saya menunggu jawapan itu.»'],
        'substitute': ['«Puan Aini membaca emel itu.» (cue: «menghantar», «fail»)',
                       '«Saya membeli nasi lemak.» (cue: «memasak»)',
                       '«Encik Rahman membuka pintu.» (cue: «menutup», «tingkap»)',
                       '«Saya menunggu bas.» (cue: «mencari», «bilik mesyuarat»)',
                       '«Saya sedang menulis emel.» (cue: «membaca», «surat»)',
                       '«Fail itu dihantar oleh Puan Aini.» (cue: «dibuka», «Encik Rahman»)',
                       '«Siapa yang menerima fail itu?» (cue: «menjawab», «soalan»)',
                       '«Kedai itu menjual baju.» (cue: «kasut»)'],
        'transform': ['Spoken to standard: «Saya baca emel itu.»', 'Spoken to standard: «Dia hantar fail itu.»',
                      'Spoken to standard: «Kami beli nasi lemak.»', 'Active to «di-»: «Puan Aini membaca emel itu.»',
                      'Active to «di-»: «Encik Rahman membuka fail itu.»', '«Di-» to active: «Kek ini dibuat oleh isteri saya.»',
                      'Make the question with «Siapa yang»: «Puan Aini menghantar fail itu.»', 'Marker «sedang»: «Saya menulis emel.»',
                      'Make it negative: «Saya menerima fail itu.»', 'Marker «belum»: «Encik Rahman membaca emel itu.»'],
        'question and answer': ['«Siapa yang membaca emel itu?» (cue: Aini)', '«Encik Rahman sedang membuka apa?» (cue: the file)',
                                '«Awak membeli apa di gerai?» (cue: «nasi lemak» and «teh tarik»)', '«Kopi ini dibayar oleh siapa?» (cue: Mei Ling)',
                                'You hear: «Saya menghantar fail itu pagi tadi.» Ask the question («bila»).',
                                'You hear: «Encik Rahman menerima fail itu.» Ask the question («Siapa yang …?»).',
                                'You hear: «Saya sedang menunggu bas.» Ask the question («Awak sedang … apa?»).',
                                'You hear: «Kuih itu dibeli di pasar.» Ask the question («di mana»).'],
        'question-word choice': ['«___ yang menghantar fail itu?» → «Puan Aini.»', '«Encik Rahman sedang membuka ___?» → «Fail itu.»',
                                 '«Awak menunggu bas di ___?» → «Di stesen.»', '«___ awak menulis emel itu?» → «Pagi tadi.»',
                                 '«Kek ini dibuat oleh ___?» → «Isteri saya.»', '«___ awak tidak membaca emel itu?» → «Sebab saya sibuk.»',
                                 '«Awak membeli ___ cawan kopi?» → «Tiga cawan.»', '«Awak mencari bilik ___?» → «Bilik mesyuarat.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. The doer comes first, then the meN- verb, then the thing; in the «di-» line the thing comes first.',
                   'Cover the line and say it from the English: Aini reads the email; the email is read by Aini; who sent the file?; it is '
                   '«Encik» Rahman who received the file; now he is opening the file; what are you writing?; I buy «nasi lemak» at the stall; I am '
                   'waiting for the answer.'],
        'substitute': ['1 «Puan Aini menghantar fail itu.» 2 «Saya memasak nasi lemak.» 3 «Encik Rahman menutup tingkap.» '
                       '4 «Saya mencari bilik mesyuarat.»',
                       '5 «Saya sedang membaca surat.» 6 «Fail itu dibuka oleh Encik Rahman.» 7 «Siapa yang menjawab soalan itu?» '
                       '8 «Kedai itu menjual kasut.»'],
        'transform': ['1 «Saya membaca emel itu.» 2 «Dia menghantar fail itu.» 3 «Kami membeli nasi lemak.» 4 «Emel itu dibaca oleh Puan Aini.» '
                      '5 «Fail itu dibuka oleh Encik Rahman.»',
                      '6 «Isteri saya membuat kek ini.» 7 «Siapa yang menghantar fail itu?» 8 «Saya sedang menulis emel.» '
                      '9 «Saya tidak menerima fail itu.» 10 «Encik Rahman belum membaca emel itu.»'],
        'question and answer': ['1 «Puan Aini yang membaca emel itu.» (or «Puan Aini.») 2 «Dia sedang membuka fail itu.» '
                                '3 «Saya membeli nasi lemak dan teh tarik.» 4 «Kopi ini dibayar oleh Cik Mei Ling.»',
                                '5 «Bila awak menghantar fail itu?» 6 «Siapa yang menerima fail itu?» 7 «Awak sedang menunggu apa?» '
                                '8 «Kuih itu dibeli di mana?»'],
        'question-word choice': ['1 «Siapa» 2 «apa» 3 «di mana» 4 «Bila» 5 «siapa» '
                                 '6 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 7 «berapa» '
                                 '8 «yang mana»'],
    },
    short_dialogues=[
        ('Siapa yang menghantar fail itu?', 'Puan Aini yang menghantar fail itu.', 'in the office'),
        ('Awak sedang menulis apa?', 'Saya sedang menulis emel.', 'at a desk'),
        ('Emel itu sudah dibaca?', 'Belum. Saya sedang membaca emel itu.', 'in the corridor'),
        ('Awak membeli apa di gerai?', 'Saya membeli kuih dan kopi.', 'after lunch')],
    short_keys=['1 «Terima kasih. Dia menghantar fail itu pagi tadi.» 2 «Emel untuk pengurus?» (or «Banyak emel hari ini.»)',
                '3 «Baik. Saya tunggu.» 4 «Sedap! Saya pun mahu membeli kuih itu.»'],
    markers=dict(
        title='Markers with meN- verbs', grammar='now',
        instructions=['Say each sentence again with the marker or time cue in brackets. The meN- verb never changes; only the marker does. / '
                      'かっこ内のマーカーか時の言葉を付けて言い直します。meN- の動詞は変わらず、前に付く語だけが変わります。'],
        items=['«Encik Rahman membuka fail itu.» (marker: «sudah»)', '«Saya membaca emel itu.» (marker: «belum»)',
               '«Puan Aini menulis jawapan.» (marker: «sedang»)', '«Saya menghantar fail itu petang ini.» (marker: «akan»)',
               '«Kami menerima fail itu.» (marker: «baru»)', '«Saya menunggu jawapan itu.» (marker: «masih»)',
               'Answer «Emel itu sudah dibaca?» (marker: «belum»)', '«Cik Mei Ling mencari fail itu.» (time cue: «sekarang», marker: «masih»)'],
        bridge=['«sudah membuka» ≈ もう開けた · «belum membaca» ≈ まだ読んでいない · «sedang menulis» ≈ 書いている · '
                '«akan menghantar» ≈ 送る予定 · «baru menerima» ≈ 受け取ったばかり',
                'Japanese changes the verb ending (読んだ / 読んでいない); Malay keeps «membaca» and changes only the marker. / '
                '日本語は動詞の語尾が変わりますが、マレー語は «membaca» のままで、前の語だけが変わります。'],
        key=['1 «Encik Rahman sudah membuka fail itu.» 2 «Saya belum membaca emel itu.» 3 «Puan Aini sedang menulis jawapan.» '
             '4 «Saya akan menghantar fail itu petang ini.»',
             '5 «Kami baru menerima fail itu.» 6 «Saya masih menunggu jawapan itu.» 7 «Belum. Saya belum membaca emel itu.» '
             '8 «Sekarang Cik Mei Ling masih mencari fail itu.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、第11章の meN- の動詞と組み合わせて言います。',
                 'Combine the chapter 4 markers with the meN- verbs: the verb never changes, only the marker does.')),
    question_note='Chapter 11 adds no new question word. The meN- verbs fit every question you know: «Siapa yang menghantar fail itu?», '
                  '«Awak sedang menulis apa?», «Awak menunggu bas di mana?», «Bila awak membaca emel itu?», «Berapa lama awak menunggu?» / '
                  '第11章で新しい疑問語は増えません。meN- の動詞は知っている疑問語すべてと使えます：'
                  '«Siapa yang menghantar fail itu?»、«Awak sedang menulis apa?»、«Awak menunggu bas di mana?»、«Bila awak membaca emel itu?»、'
                  '«Berapa lama awak menunggu?»',
    question_tasks=['Ask a colleague what they are reading. («apa»)', 'Ask who sent the file. («siapa»)',
                    'Ask where your colleague waits for the bus. («di mana»)', 'Ask formally whether the email has been read. («Adakah»)',
                    'Ask politely whether you may open the window. («Bolehkah»)', 'Ask how many cups of coffee your colleague buys. («berapa»)',
                    'Ask when your colleague sent the file. («bila»)', 'Ask what time the file arrived. («pukul berapa»)',
                    'Ask on what day your colleague writes the reply. («hari apa»)', 'Ask how your colleague opens the file. («bagaimana»; spoken «macam mana»)',
                    'Ask why your colleague did not read the email. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which file Aini sent. («yang mana»)', 'Ask where your colleague takes the parcel. («ke mana»)',
                    'Ask where the file came from. («dari mana»)', 'Ask how far your colleague walks to buy coffee. («berapa jauh»)',
                    'Ask how long your colleague waits for the answer. («berapa lama»)', 'Ask how many pens your colleague brings. («berapa» with a counter)',
                    'Ask who wrote the reply. («siapa» with «oleh»)'],
    question_keys=['1 «Awak sedang membaca apa?» 2 «Siapa yang menghantar fail itu?» 3 «Awak menunggu bas di mana?»',
                   '4 «Adakah emel itu sudah dibaca?» 5 «Bolehkah saya membuka tingkap?» 6 «Berapa cawan kopi awak beli?»',
                   '7 «Bila awak menghantar fail itu?» 8 «Pukul berapa fail itu sampai?» 9 «Pada hari apa awak menulis jawapan itu?»',
                   '10 «Bagaimana awak membuka fail itu?» (spoken: «Macam mana awak buka fail itu?») 11 «Kenapa awak tidak membaca emel itu?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab saya sibuk.» / «Kerana saya sibuk.»',
                   '12 «Fail yang mana dihantar oleh Puan Aini?» 13 «Awak membawa bungkusan itu ke mana?» 14 «Fail itu datang dari mana?»',
                   '15 «Berapa jauh awak berjalan untuk membeli kopi?» 16 «Berapa lama awak menunggu jawapan itu?» 17 «Awak membawa berapa batang pen?»',
                   '18 «Jawapan itu ditulis oleh siapa?»'],
    listening=LISTENING,
    listening_context='In the afternoon «Encik» Tanaka asks «Encik» Rahman what happened with the file from Osaka. / 午後、田中さんがラーマンさんに、大阪から来たファイルがどうなったかをたずねます。',
    listening_before=['Predict: which meN- verbs will you hear? Write three guesses (for example «menghantar», «menerima», «membuka»). / 聞こえそうな meN- の動詞を三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['What time did Aini send the file, and when did Rahman receive it?', 'Has Rahman read the file? Why not?',
                      'Whom does he call?', 'What does he write before lunch?', 'Where does he send the reply?',
                      'Roughly when will they receive the reply?', 'What does he do after sending it?', 'Who made the coffee?',
                      'Who cooked the «kuih», and when?'],
    listen_answers=['sent at nine; received at half past nine', 'no; the file cannot be opened and he is looking for the password',
                    'Mei Ling', 'the reply', 'to Osaka', 'about two in the afternoon', 'he waits for their answer', 'Aini',
                    'his wife; yesterday'],
    listening_after=['Compare answers, then shadow lines 2, 4 and 8 after the teacher. / 答えを比べ、2・4・8行目をシャドーイングします。',
                     'Tell your partner what you did with a file or an email this morning in four sentences with meN- verbs. / 今朝ファイルかメールにしたことを、meN- の動詞を使って4文でパートナーに話しましょう。'],
    test_listen=[(1, 'sent at nine; received at half past nine', ['menghantar', 'menerima', 'pukul']),
                 (3, 'no; the file cannot be opened', ['membaca', 'dibuka', 'mencari']),
                 (5, 'Mei Ling', ['memanggil', 'sekarang']),
                 (7, 'to Osaka', ['menulis', 'menghantar']),
                 (9, 'about two in the afternoon', ['menerima', 'pukul']),
                 (11, 'Aini', ['dibuat', 'oleh'])],
    test_listen_prompts=['When did Aini send the file, and when did Rahman receive it?', 'Has Rahman read the file?',
                         'Whom does Rahman call?', 'Where does he send the reply?', 'When will they receive the reply?',
                         'Who made the coffee?'],
    reading_title='Reading and writing · A message to the team',
    reading=['Fictional message in the team chat (all names, files and times are invented):',
             '«Selamat pagi semua. Fail dari Osaka sudah sampai. Saya membuka fail itu pukul sepuluh.»',
             '«Jawapan ditulis oleh Cik Mei Ling dan dihantar oleh Puan Aini.»',
             '«Kopi dan kuih dibeli oleh Encik Tanaka. Saya sudah membayar.»',
             '«Sila tunggu di bilik mesyuarat. Mesyuarat bermula pukul sebelas. Terima kasih. Rahman»',
             'Sign on the meeting-room door: «Sila tutup pintu.»'],
    read_questions=['What time did Rahman open the file?', 'Who wrote the reply?', 'Who sent it?', 'Who bought the coffee and the «kuih»?',
                    'Where should everyone wait?', 'What time does the meeting start?',
                    'Say in Malay: "The file was sent by Aini."'],
    read_answers=['at ten', 'Mei Ling', 'Aini', 'Tanaka', 'in the meeting room', 'at eleven', '«Fail itu dihantar oleh Puan Aini.»'],
    write_instruction='Write four or five sentences about what you did with a file or an email yesterday, each with a meN- verb. / '
                      '昨日、ファイルかメールにしたことを、meN- の動詞を使って4〜5文で書きましょう。',
    write_model='«Semalam saya membaca emel dari Osaka. Saya menulis jawapan, kemudian saya menghantar jawapan itu pukul lima. '
                'Puan Aini menerima jawapan itu. Saya menunggu jawapan mereka hari ini.»',
    writing_type='message',
    task_title='Task · Who did what with the file?',
    role_a=['Your information (fictional): «Puan» Aini read the email at nine; «Cik» Mei Ling wrote the reply; «Encik» Rahman sent the reply at ten; '
            '«Encik» Tanaka bought the coffee.',
            'B asks you who did what. Answer with the doer first, and once with the thing first.',
            'Aの情報（架空）：アイニさんが9時にメールを読んだ、メイリンさんが返事を書いた、ラーマンさんが10時に返事を送った、田中さんがコーヒーを買った。'
            'Bの質問に答えます。動作主が先の文で答え、一回は物が先の文でも答えます。'],
    role_b=['You were out of the office this morning. Ask A «Siapa yang …?» and «… sedang … apa?» to find out who read the email, who wrote '
            'and sent the reply, and who bought the coffee.',
            'Report back to your partner in the «di-» form (for example «Jawapan itu ditulis oleh …»).',
            'Bは今朝席を外していました。Aに «Siapa yang …?» と «… sedang … apa?» でたずね、誰がメールを読み、返事を書いて送り、コーヒーを買ったかを調べます。'
            'そのあと、«di-» の形でパートナーに報告します（例：«Jawapan itu ditulis oleh …»）。'],
    change=['Halfway, A says: «Maaf, bukan Encik Rahman. Puan Aini yang menghantar jawapan itu pukul sebelas.» B changes the report.',
            '途中でAが «Maaf, bukan Encik Rahman. Puan Aini yang menghantar jawapan itu pukul sebelas.» と言います。Bは報告を直します。'],
    success=['☐ B asks at least three questions with «Siapa yang …?» or «… sedang … apa?».',
             '☐ A answers with a full sentence and uses both the meN- form and the «di-» form once.',
             '☐ After the change, B corrects the report with the right doer and time.'],
    task_key='«Siapa yang membaca emel itu?» — «Puan Aini yang membaca emel itu pukul sembilan.» — «Siapa yang menulis jawapan?» — «Cik Mei Ling '
             'menulis jawapan itu. Jawapan itu dihantar oleh Encik Rahman pukul sepuluh.» — «Kopi itu dibeli oleh siapa?» — «Kopi itu dibeli oleh Encik '
             'Tanaka.» — Change: «Maaf, bukan Encik Rahman. Puan Aini yang menghantar jawapan itu pukul sebelas.» — «Oh, jawapan itu dihantar oleh '
             'Puan Aini pukul sebelas.»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 11 card notes ms-c11-002 («Aini membaca buku itu» = «Buku itu dibaca oleh Aini»; «dibaca», chapter 9), -003 and -008 (the '
                    't drops), -013 (the p drops), -014 («menghantar»), -015 and -017 («menerima» and «melihat» as whole words; everyday '
                    '«tengok», chapter 7); stage 2 plan section 3 (meN- from chapter 11; «menghantar» also means to drop someone off: the audit '
                    'note on the unit 11A table) and section 5 (Japanese passive is not the Malay «di-»: potential adversative reading); charter '
                    'section 5 (ber- before meN-). The note states no figure or rule about Malaysia.',
    culture_prompt='In Japanese, who gets named when a file is sent: the sender (送りました) or the file (送られました)? When do you use each?',
    culture_explain=('マレーシアで同じ動詞を標準の meN- の形と日常の短い形で聞くこと、«menerima»・«melihat»・«menghantar» の使い方、職場での「誰が」と「何が」の言い方を読みます。',
                     'Read about hearing the standard meN- form and the everyday short form, three verbs that need a word of warning, and how to put the doer or the thing first at work.'),
    quiz_words=['L-1136', 'L-1137', 'L-1129', 'L-1142', 'L-1133', 'L-1141'],
    quiz_meanings=['to send, to deliver', 'to receive', 'to open', 'to sell', 'to look for', 'to wait'],
    grammar_quiz=[('Write the standard form: «Saya baca surat itu.»', '«Saya membaca surat itu.»', ['membaca', 'surat']),
                  ('Make it a «di-» sentence: «Puan Aini menghantar fail itu.»', '«Fail itu dihantar oleh Puan Aini.»', ['dihantar', 'oleh', 'fail']),
                  ('Say in Malay: "Who sent the file?"', '«Siapa yang menghantar fail itu?»', ['siapa', 'menghantar', 'fail']),
                  ('Write the meN- form of «tulis» and use it in a sentence about a reply.', '«menulis»: for example «Saya menulis jawapan.»', ['menulis', 'jawapan'])],
    test_reading=['Fictional notice on the office door: «PERHATIAN: Fail dari Osaka dihantar oleh Puan Aini pukul sembilan. Encik Rahman menerima fail itu. '
                  'Mesyuarat bermula pukul sebelas. Sila tunggu di bilik mesyuarat.»'],
    reading_quiz=[('Who sent the file?', '«Puan» Aini', ['dihantar', 'oleh']),
                  ('Who received the file?', '«Encik» Rahman', ['menerima']),
                  ('What time does the meeting start?', 'at eleven', ['bermula', 'pukul']),
                  ('Where should people wait?', 'in the meeting room', ['tunggu', 'bilik'])],
    speaking_test='Tell the teacher what you did with a file or an email this morning in four sentences with meN- verbs, then answer one question with «Siapa yang …?».',
    speaking_key='Check: at least three different meN- verbs spelt and said correctly («membaca», «menghantar», «menulis»); one sentence with a marker; one '
                 'answer to «Siapa yang …?». Accept the everyday root in speech if the meN- form was also used once.',
    speaking_words=['membaca', 'menghantar', 'menulis', 'siapa', 'yang'],
    plan={'A_recall': 'chapters 9 and 10 («di-» partners; ber- routines) from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first (the active line and its «di-» partner), question and answer before the rule; then the vocabulary in three '
                        'groups with each root, its chapter and the nasal change (reading, writing and files 7, buying, paying and carrying 6, senses, calling '
                        'and everyday tasks 7). Write the six fronts ‹mem-›, ‹men-›, ‹meng-›, ‹me-› and the dropped t and p on the board.',
          'B_recall': 'say who sent the file, with the doer first and then with the thing first.',
          'B_drills': 'pattern table, substitution, transformation (spoken to standard first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner says one thing they sent and one thing they received.',
          'D_review': 'cumulative question-word drill (chapters 1 to 11), then the markers drill with new cues and a spelling check of '
                      '«membeli», «menulis», «memanggil», «mencari», «menghantar».',
          'D_preview': 'unit 11B: the draft, the deadline and the weekend (Kata-Kata c11 cards ms-c11-021 to ms-c11-043 and frames f04, f06).',
          'E_recall': 'say three things you did at work yesterday with meN- verbs.',
          'E_listening': 'read the Kata-Kata scenario lines ms-c11-s01 to ms-c11-s08 (Tanaka, «Puan» Aini and «Encik» Rahman, the email and the file) twice; '
                         'learners tick the meN- verbs they hear.',
          'E_roleplay': 'pairs play the same scene with their own files and names, without the script.',
          'E_variation': 'a changed morning: the file cannot be opened, so A explains who sent it, who received it and who is looking for the password; '
                         'B asks «Siapa yang …?» and «Awak sedang … apa?»'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 11 to the office scene report_deadline for unit 11B, with «mendaki» from the social pack. '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: unit 11B (the draft, the deadline and the weekend), then the review block after 11B.',
    teacher_notes=['Load: 21 core words in three groups (reading, writing and files 8; buying, paying and carrying 6; senses, calling and everyday tasks 7), no '
                   'recognition word (no Dunia scene primes chapter 11), and revision of the roots, the «di-» partners, the office words and the markers. '
                   'Suggested order: Block A the first group with patterns 1 and 2; Block B the second group with pattern 3; the third group with pattern 4 '
                   'in Block B or C. If the pilot shows 21 is too many, the natural cut is: «membaca», «menulis», «menghantar», «menerima», «membuka», '
                   '«membeli», «membayar», «mencari», «menunggu», «memanggil» first; the rest second.',
                   'The scene lines ms-c11-s06 and ms-c11-s07 use «menelefon», a unit 11B core word (card ms-c11-040). Gloss it as "to phone" and '
                   'treat it as recognition here; it is taught in 11B.',
                   'meN- rule (plan section 3, Sam 13 Nov 2026): ‹mem-› before b; ‹men-› before c, d, j; ‹meng-› before h or a vowel; ‹me-› before l and m; '
                   't and p drop («menulis», «memanggil»). The nasal-change traps from the Kata-Kata cards: «memanggil», not *mempanggil (card ms-c11-013); '
                   '«menulis», not *mentulis (ms-c11-003); «menutup», not *mentutup (ms-c11-008); «menunggu», not *mentunggu (ms-c11-019). «memasak» keeps '
                   'its m (ms-c11-004): not *memmasak. Unit 11B adds s and k and the one-syllable roots («menyewa», ‹menyapu› as a mention only, «mengira», '
                   '«mengecas»).',
                   'Common traps from the cards: «menerima» (ms-c11-015) and «melihat» (ms-c11-017) are whole words; their roots are not taught alone. '
                   '«melihat» is standard, everyday speech says «tengok» (ms-c11-017). «menghantar» (ms-c11-014) also means to take someone to a place. '
                   'The «di-» partner appears only where the card names one (chapter 9); do not make a «di-» form for «mencari», «menjawab», «melihat», «mendengar», '
                   '«menunggu» or «menerima».',
                   'Where Japanese learners usually slip: (1) treating ‹meN-› like ます or like the past, and so adding it to every verb; (2) a requested action takes the '
                   'plain root («Tolong baca emel ini»), not the meN- form: *«Tolong membaca emel ini» is wrong; (3) 聞く covers «mendengar» (hear, listen to) and asking a '
                   'question («tanya», chapter 2): ask which they mean; (4) spelling: dropping the first sound of b, c, d, j («membeli» is right, *meli is wrong) or keeping it '
                   'for t and p (*mentulis, *mempanggil); (5) reading the «di-» form as a complaint because the Japanese passive often is one; (6) 見る covers «melihat» and '
                   '«tengok»: teach «melihat» first, accept «tengok» in speech.',
                   'In conversation, focus the doer with «yang» («Encik Tanaka yang membeli kopi itu», «Siapa yang membaca emel itu?»); the model conversation does this. Keep '
                   '«di-» … «oleh» for the drills and for written notices (Sam, 13 Nov 2026: in speech people focus with «yang»).',
                   'Standard first: teach the meN- form, accept the everyday root in speech («baca», «hantar», «beli», «tengok»), and never mark it wrong in a speaking task. '
                   'No other spoken contraction is needed in this unit.',
                   'The scene follows Kata-Kata c11 (scenario lines ms-c11-s01 to s08, frames f01, f02, f03 and f05). All names, times and files are fictional; '
                   'learners may use their real office or an invented one.',
                   'Cumulative question words: chapters 1 to 11. Chapter 11 adds no new question word.'],
)

UNIT = unit_dict(CFG)
