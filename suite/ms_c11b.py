"""Unit 11B: meN- verbs for the draft, the deadline and the weekend: checking, phoning, charging, renting, ordering, hiking
(Tolong semak ___ ini; Hujung minggu ini saya mahu ___; Aini ___ buku itu; Siapa yang ___ fail itu?).

21 core ledger entries, the rows the ledger places in "Ch11 (unit 11B)" (L-1143 to L-1156, and the existing rows L-0680 «draf»,
L-0684 «rancangan», L-0696 «slaid», L-0792 «menyimpan», L-0819 «menyemak», L-0849 «tarikh akhir» and L-0865 «mendaki»), in three
groups, and two recognition entries: L-0604 «tukar» (spoken partner of «menukar») and L-0678 «deadline» (spoken partner of
«tarikh akhir»), ledger "Ch11 (unit 11B, recognition ...)"; Kata-Kata cards ms-c11-042 and -043, recognise only. This unit teaches
the rest of the meN- spelling: s drops and meny- is used, k drops and meng- is used, and the one-syllable root takes menge-
(«mengecas»). No meN-...-kan or -i form (chapter 12). The scene follows Kata-Kata c11 (scenario lines ms-c11-s09 to s18: the draft,
the deadline and the weekend with Cik Mei Ling) and goes further in class: a draft message, a check-and-confirm role-play and a
moved deadline. All names, times and plans are fictional. Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

DRAFT = ['L-0819', 'L-1153', 'L-0680', 'L-0696', 'L-0849', 'L-0684']
THINGS = ['L-1154', 'L-1155', 'L-1156', 'L-1145', 'L-1146', 'L-1147', 'L-1148']
LIFE = ['L-0865', 'L-1144', 'L-1143', 'L-1149', 'L-1150', 'L-1151', 'L-1152', 'L-0792']
CORE = DRAFT + THINGS + LIFE
RECOGNITION = ['L-0604', 'L-0678']

# Revision: words placed in chapters 1 to 10 that the unit really uses (a test fails if one is not used).
REV_ROOTS = ['L-0529', 'L-0941', 'L-0375', 'L-0573', 'L-0583', 'L-1051', 'L-1023', 'L-0396']
REV_WORK = ['L-0526', 'L-0525', 'L-0995', 'L-0419', 'L-0208', 'L-0064', 'L-0523', 'L-0567']
REV_FREE = ['L-0702', 'L-0030', 'L-0078', 'L-0079', 'L-0262', 'L-0934', 'L-0935', 'L-0936']
REV_TIME = ['L-0189', 'L-0193', 'L-0194', 'L-0192', 'L-0191', 'L-0161', 'L-0179', 'L-0178', 'L-0213']

EXAMPLES = {
    # The draft and the deadline
    'L-0819': '«Cik Mei Ling sedang menyemak draf itu.»',
    'L-1153': '«Tolong semak draf ini.»',
    'L-0680': '«Draf slaid itu belum siap.»',
    'L-0696': '«Saya membuat slaid untuk mesyuarat.»',
    'L-0849': '«Tarikh akhir draf itu hari Jumaat.» (spoken: «Deadline hari Jumaat.»)',
    'L-0684': '«Apa rancangan awak pada hujung minggu?»',
    # Messages, phones, money and choices
    'L-1154': '«Nanti saya menghantar mesej.»',
    'L-1155': '«Saya akan menelefon mereka petang ini.»',
    'L-1156': '«Boleh saya mengecas telefon saya di sini?»',
    'L-1145': '«Saya menukar duit di bank.» (spoken: «tukar»)',
    'L-1146': '«Saya mengira jumlah itu semalam.»',
    'L-1147': '«Saya mengisi borang di pejabat pos.»',
    'L-1148': '«Saya memilih slaid yang pertama.»',
    # Free time, help and renting
    'L-0865': '«Hujung minggu ini saya mahu mendaki dengan kawan saya.»',
    'L-1144': '«Kami suka melancong pada hujung minggu.»',
    'L-1143': '«Kami menyewa rumah dekat stesen.»',
    'L-1149': '«Boleh saya meminjam pen awak?»',
    'L-1150': '«Saya memesan teh tarik dan roti canai.»',
    'L-1151': '«Cik Mei Ling menolong saya.»',
    'L-1152': '«Isteri saya mengajar saya memasak.»',
    'L-0792': '«Saya menyimpan fail itu di komputer saya.»',
    # Recognition
    'L-0604': '«Saya mahu tukar bilik.» (spoken; standard: «Saya mahu menukar bilik.»)',
    'L-0678': '«Deadline hari Jumaat.» (spoken; formal and written: «Tarikh akhir hari Jumaat.»)',
    # Revision · roots
    'L-0529': '«simpan» → «menyimpan»: «Simpan fail itu di sini.»',
    'L-0941': '«kira» → «mengira»: «Tolong kira jumlah ini.»',
    'L-0375': '«tolong» → «menolong»: «Tolong semak draf ini.»',
    'L-0573': '«telefon» → «menelefon»: «Saya akan telefon mereka.» (spoken)',
    'L-0583': '«cas» → «mengecas»: «Saya mahu cas telefon saya.» (spoken)',
    'L-1051': '«sewa» → «menyewa»: «Sewa rumah itu tiga ratus ringgit sebulan.»',
    'L-1023': '«masak» → «memasak»: «Saya mahu memasak nasi lemak.»',
    'L-0396': '«sewa» → «disewa» (chapter 9): «Bilik itu disewa oleh kawan saya.»',
    # Revision · the office
    'L-0526': '«Tolong semak emel ini.»',
    'L-0525': '«Fail itu sudah siap.»',
    'L-0995': '«Tolong semak jumlah itu sekali lagi.»',
    'L-0419': '«Borang itu belum diisi.»',
    'L-0208': '«Mesyuarat bermula pukul sebelas.»',
    'L-0064': '«Saya sampai di pejabat pukul sembilan.»',
    'L-0523': '«Saya menyimpan fail itu di komputer saya.»',
    'L-0567': '«Letak telefon itu di atas meja.»',
    # Revision · free time and food
    'L-0702': '«Hujung minggu ini saya mahu mendaki.»',
    'L-0030': '«Tidak, hujung minggu ini saya sibuk.»',
    'L-0078': '«Saya mahu mendaki dengan kawan saya.»',
    'L-0079': '«Saya mahu melancong dengan keluarga saya.»',
    'L-0262': '«Saya mahu memasak nasi lemak.»',
    'L-0934': '«Saya mahu memesan teh tarik.»',
    'L-0935': '«Saya memesan roti canai.»',
    'L-0936': '«Saya memesan kopi O.»',
    # Revision · time and markers
    'L-0189': '«Saya sedang menyemak draf itu.»',
    'L-0193': '«Saya sudah menyemak draf itu.»',
    'L-0194': '«Draf itu belum siap.»',
    'L-0192': '«Saya akan menelefon mereka petang ini.»',
    'L-0191': '«Saya masih menyemak draf itu.»',
    'L-0161': '«Sekarang saya mahu mengecas telefon saya.»',
    'L-0179': '«Tarikh akhir hari Jumaat.»',
    'L-0178': '«Mesyuarat hari Khamis.»',
    'L-0213': '«Saya mahu memasak.» (spoken: «Saya nak masak.»)',
}

# (root, where the root sits, English change, Japanese change, passive)
ROOTS = {
    'L-0819': ('«semak»', 'this chapter', 'the s drops and ‹meny-› is used: «menyemak»', 's が落ちて ‹meny-› になる', None),
    'L-0792': ('«simpan»', 'Dunia, chapter 2', 'the s drops and ‹meny-› is used: «menyimpan»', 's が落ちて ‹meny-› になる', None),
    'L-0865': ('‹daki›', None, '‹men-› before d', '‹men-›（d の前）', None),
    'L-1143': ('«sewa»', 'chapter 6', 'the s drops and ‹meny-› is used: «menyewa»', 's が落ちて ‹meny-› になる', '«disewa»'),
    'L-1144': ('‹lancong›', None, '‹me-› before l; it takes no object, so it has no «di-» partner', '‹me-›（l の前）；目的語をとらない', None),
    'L-1145': ('«tukar»', 'this chapter, spoken', 'the t drops: «menukar»', 't が落ちる', None),
    'L-1146': ('«kira»', 'Dunia, chapter 5', 'the k drops and ‹meng-› is used: «mengira»', 'k が落ちて ‹meng-› になる', None),
    'L-1147': ('«isi»', 'Dunia, chapter 3', '‹meng-› before a vowel', '‹meng-›（母音の前）', None),
    'L-1148': ('«pilih»', 'chapter 6', 'the p drops: «memilih»', 'p が落ちる', None),
    'L-1149': ('‹pinjam›', None, 'the p drops: «meminjam»', 'p が落ちる', None),
    'L-1150': ('‹pesan›', None, 'the p drops: «memesan»', 'p が落ちる', None),
    'L-1151': ('«tolong»', 'chapter 8', 'the t drops: «menolong»', 't が落ちる', None),
    'L-1152': ('‹ajar›', None, '‹meng-› before a vowel', '‹meng-›（母音の前）', None),
    'L-1155': ('«telefon»', 'Dunia, chapter 7', 'the t drops: «menelefon»', 't が落ちる', None),
    'L-1156': ('«cas»', 'Dunia, chapter 7', '‹menge-› before a one-syllable root: «mengecas»', '‹menge-›（一音節の語根の前）', None),
}
_EN = {'L-0819': 'to check, to review', 'L-0792': 'to keep, to store (standard; everyday «simpan»)', 'L-0865': 'to hike, to climb a hill',
       'L-1143': 'to rent as a tenant', 'L-1144': 'to travel for leisure', 'L-1145': 'to change, to exchange (standard; everyday «tukar»)',
       'L-1146': 'to count, to calculate', 'L-1147': 'to fill (in), to put in', 'L-1148': 'to choose', 'L-1149': 'to borrow',
       'L-1150': 'to order (goods, food)', 'L-1151': 'to help', 'L-1152': 'to teach', 'L-1155': 'to phone',
       'L-1156': 'to charge (a phone, a battery)'}
_JA = {'L-0819': '確認する・目を通す', 'L-0792': '保管する・取っておく（標準；日常は «simpan»）', 'L-0865': '（山を）登る・ハイキングする',
       'L-1143': '（家・部屋を）借りる（賃借する）', 'L-1144': '旅行する', 'L-1145': '替える・交換する（標準；日常は «tukar»）',
       'L-1146': '数える・計算する', 'L-1147': '記入する・入れる', 'L-1148': '選ぶ', 'L-1149': '（一時的に）借りる',
       'L-1150': '注文する', 'L-1151': '手伝う・助ける', 'L-1152': '教える', 'L-1155': '電話をかける', 'L-1156': '充電する'}


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
    if where is None:
        en_root, ja_root = f'‹meN-› + {root}', f'‹meN-› ＋ {root}'
    else:
        en_root, ja_root = f'‹meN-› + {root} ({where})', f'‹meN-› ＋ {root}（{_where_ja(where)}）'
    en = f'{_EN[lid]} ({en_root}; {change}' + (f'; passive {passive}, chapter 9)' if passive else ')')
    ja = f'{_JA[lid]}（{ja_root}；{change_ja}' + (f'；受け身 {passive}、第9章）' if passive else '）')
    return {'en': en, 'ja': ja}


VOCAB_OPTS = {lid: _opts(lid) for lid in ROOTS}
VOCAB_OPTS.update({
    'L-1153': {'en': 'check, review (the root of «menyemak», used as a request: «Tolong semak draf ini.»)',
               'ja': '確認してください（«menyemak» の語根；依頼で使う：«Tolong semak draf ini.»）'},
    'L-0680': {'en': 'a draft', 'ja': '下書き'},
    'L-0696': {'en': 'a slide (in a presentation)', 'ja': 'スライド（プレゼンテーションの）'},
    'L-0849': {'en': 'deadline (formal and written; everyday speech says «deadline»)',
               'ja': '締め切り（あらたまった書き言葉；日常の話し言葉は «deadline»）'},
    'L-0684': {'en': 'a plan (learn it as a whole word; «rancangan» is not made by you from a root)',
               'ja': '計画・予定（一語まるごと覚える）'},
    'L-1154': {'en': 'a message («mesej» in a chat or a text)', 'ja': 'メッセージ（チャットやショートメッセージの）'},
    'L-0604': {'en': 'to change, to exchange (spoken; standard «menukar»): recognise it, say «menukar»',
               'ja': '替える・交換する（話し言葉；標準は «menukar»）：聞いて分かればよい、言うときは «menukar»'},
    'L-0678': {'en': 'deadline (spoken, borrowed from English; formal and written «tarikh akhir»): recognise it, say «tarikh akhir»',
               'ja': '締め切り（話し言葉、英語から；あらたまった書き言葉は «tarikh akhir»）：聞いて分かればよい、書くときは «tarikh akhir»'},
})

P = [
    ('ms-c11-f04', '«Tolong semak» ___ «ini.»  (please check this ___)', [
        'A: «Tolong semak draf ini.» B: «Baik. Tarikh akhir draf ini bila?»',
        'A: «Tolong semak slaid ini.» B: «Boleh. Saya semak sekarang.»',
        'A: «Tolong semak jumlah ini.» B: «Baik. Saya mengira sekali lagi.»',
        'A: «Tolong semak borang ini.» B: «Sudah betul. Tolong tanda tangan di sini.»',
        'A: «Tolong semak mesej ini dulu.» B: «Boleh. Mesej ini sudah baik.»',
        'A: «Tolong semak emel ini, ya.» B: «Baik. Saya menyemak emel itu petang ini.»'],
     "«Tolong semak» + the thing is the everyday request: «Tolong semak draf ini.» (Please check this draft.) A request takes the plain root, "
     "not the meN- form: «semak», not «menyemak». The same root becomes «menyemak» when you say what someone is doing: «Cik Mei Ling sedang "
     "menyemak draf itu.» The deadline is «tarikh akhir» in a notice or a message; in speech you will hear «deadline» (spoken), so the "
     "answer to «Tarikh akhir bila?» can be «Hari Jumaat.» or «Deadline hari Jumaat.» Say it in writing with «tarikh akhir».",
     "«Tolong semak» ＋ 物は、日常のいちばん使う依頼の言い方です：«Tolong semak draf ini.»（この下書きを確認してください。）依頼には meN- の形ではなく、"
     "語根をそのまま使います：«semak» で、«menyemak» ではありません。同じ語根でも、誰かがしていることを言うときは «menyemak» になります："
     "«Cik Mei Ling sedang menyemak draf itu.» 締め切りは、掲示やメッセージでは «tarikh akhir» で、話し言葉では «deadline»（話し言葉）も聞きます。"
     "«Tarikh akhir bila?» への答えは «Hari Jumaat.» でも «Deadline hari Jumaat.» でもよいですが、書くときは «tarikh akhir» を使います。",
     'Japanese 〜してください (確認してください) matches «Tolong semak …», and the Japanese verb stem is used without a polite ending in the '
     'plain request, much as Malay uses the bare root. The mistake is to copy a polite verb into Malay: *«Tolong menyemak draf ini» sounds odd; use the root.',
     '日本語の「〜してください」（確認してください）は «Tolong semak …» にあたります。丁寧な語尾を付けずに語根をそのまま使うところも、マレー語の語根のままの依頼に似ています。'
     '間違いやすいのは丁寧な動詞形をそのままマレー語にすることです：*«Tolong menyemak draf ini» は不自然なので、語根を使います。'),
    ('ms-c11-f06', '«Hujung minggu ini saya mahu» ___.  (this weekend I want to ___)', [
        'A: «Hujung minggu ini awak buat apa?» B: «Hujung minggu ini saya mahu memasak.»',
        'A: «Awak mahu memasak apa?» B: «Saya mahu memasak nasi lemak.»',
        'A: «Encik mahu melancong ke mana?» B: «Hujung minggu ini saya mahu melancong ke Johor Bahru.»',
        'A: «Puan mahu memesan apa?» B: «Saya mahu memesan teh tarik.»',
        'A: «Awak mahu meminjam apa?» B: «Saya mahu meminjam buku itu.»',
        'A: «Awak mahu menyewa rumah di mana?» B: «Saya mahu menyewa rumah dekat stesen.»'],
     "«mahu» + a meN- verb says what you plan to do: «Hujung minggu ini saya mahu mendaki.» Nothing comes between «mahu» and the verb, "
     "and the verb keeps its meN- form after «mahu». «Rancangan» is the plan itself: «Apa rancangan awak?» (What are your plans?). In everyday talk "
     "people say «nak» for «mahu» (spoken); say «mahu» first. «melancong» is a trip for pleasure and takes no object, so «melancong ke "
     "Johor Bahru» uses «ke» for the place and has no «di-» form. «menyewa» is to rent as a tenant, «meminjam» to borrow for a while: the two are "
     "not the same word.",
     "«mahu» ＋ meN- の動詞で、したいことを言います：«Hujung minggu ini saya mahu mendaki.» «mahu» と動詞の間には何も入れず、動詞は «mahu» のあとでも meN- の形のままです。"
     "«Rancangan» は計画そのものです：«Apa rancangan awak?»（ご予定は？）日常会話では «mahu» の代わりに «nak»（話し言葉）とも言いますが、まず «mahu» を言います。"
     "«melancong» は楽しみの旅行で目的語をとらないので、«melancong ke Johor Bahru» のように場所には «ke» を使い、«di-» の形はありません。"
     "«menyewa» は借り手として賃借すること、«meminjam» は一時的に借りることで、同じ語ではありません。",
     'Japanese 借りる covers both «menyewa» (rent a flat) and «meminjam» (borrow a pen): ask which one is meant. 〜したい (料理したい) matches «mahu memasak'
     '», but Japanese puts a の/こと after the verb in some patterns; Malay never does.',
     '日本語の「借りる」は «menyewa»（部屋を借りる）と «meminjam»（ペンを借りる）の両方にあたります。どちらの意味かを確かめましょう。「〜したい」（料理したい）は '
     '«mahu memasak» にあたります。日本語では動詞のあとに「の・こと」が付く型がありますが、マレー語では付けません。'),
    ('ms-c11-f01', '«Aini» ___ «buku itu.»  (doer + meN- verb + the thing, with the new verbs)', [
        'A: «Cik Mei Ling menyemak draf itu?» B: «Ya. Dia menyemak draf itu pagi tadi.»',
        'A: «Encik Rahman mengira jumlah itu?» B: «Ya. Dia mengira jumlah itu semalam.»',
        'A: «Puan Aini memilih slaid yang mana?» B: «Dia memilih slaid yang pertama.»',
        'A: «Isteri encik mengajar apa?» B: «Isteri saya mengajar saya memasak.»',
        'A: «Awak mengisi borang itu?» B: «Sudah. Saya mengisi borang itu di pejabat.»',
        'A: «Awak menyimpan fail itu di mana?» B: «Saya menyimpan fail itu di komputer saya.»'],
     "These are the rest of the spelling changes. s drops and ‹meny-› is used: «sewa» → «menyewa», «simpan» → «menyimpan», «semak» → «menyemak». "
     "k drops and ‹meng-› is used: «kira» → «mengira». p and t drop: «memilih», «meminjam», «memesan», «menukar», «menolong», «menelefon». ‹meng-› "
     "before a vowel: «mengisi», «mengajar». A root of one syllable takes ‹menge-›: «cas» → «mengecas». All the cases together: ‹mem-› before b; "
     "t, p, s and k drop; ‹meng-› before h or a vowel; ‹men-› before c, d and j; ‹me-› before l, m, n, r, w and y; ‹menge-› before a one-syllable "
     "root. The word ‹menyapu› (to sweep) is spelt the same way, with ‹meny-›, not *mensapu.",
     "残りのつづりの変化です。s は落ちて ‹meny-› になります：«sewa» → «menyewa»、«simpan» → «menyimpan»、«semak» → «menyemak»。k は落ちて ‹meng-› になります："
     "«kira» → «mengira»。p と t は落ちます：«memilih»・«meminjam»・«memesan»・«menukar»・«menolong»・«menelefon»。母音の前は ‹meng-›：«mengisi»・«mengajar»。"
     "一音節の語根には ‹menge-› を付けます：«cas» → «mengecas»。まとめると、b の前は ‹mem-›、t・p・s・k は落ちる、h か母音の前は ‹meng-›、c・d・j の前は ‹men-›、"
     "l・m・n・r・w・y の前は ‹me-›、一音節の語根は ‹menge-› です。‹menyapu›（掃く）も同じで、‹meny-› を使い、*mensapu とは書きません。",
     'Japanese has no sound change like this, so the spelling has to be practised aloud: say the root, say the front, then the verb. Two traps for a '
     'reader of English or Japanese: the first sound of a root such as «sewa» or «kira» is not repeated (*mensewa, *mengkira are wrong), and «cas» '
     'needs ‹menge-›, not ‹meng-› alone.',
     '日本語にはこのような音の変化がないので、声に出して練習しましょう：語根を言い、前の部分を言い、そのあと動詞を言います。英語や日本語を読む人が陥りやすい二つの落とし穴：'
     '«sewa» や «kira» のような語根の最初の音は残さず（*mensewa や *mengkira は間違い）、«cas» には ‹meng-› だけでなく ‹menge-› が必要です。'),
    ('ms-c11-f03', '«Siapa yang» ___ «fail itu?»  (who did it, with the new verbs)', [
        'A: «Siapa yang menyemak draf itu?» B: «Cik Mei Ling yang menyemak draf itu.»',
        'A: «Siapa yang menelefon pejabat di Jepun?» B: «Encik Rahman yang menelefon mereka.»',
        'A: «Siapa yang menyewa rumah itu?» B: «Kawan saya yang menyewa rumah itu.»',
        'A: «Siapa yang memesan kopi ini?» B: «Puan Aini yang memesan kopi ini.»',
        'A: «Siapa yang meminjam pen saya?» B: «Encik Tanaka yang meminjam pen itu.»',
        'A: «Siapa yang menolong awak?» B: «Cik Mei Ling yang menolong saya.»'],
     "The frame from unit 11A returns with the new verbs: «Siapa yang menyemak draf itu?» The answer puts the doer in front of «yang»: «Cik Mei "
     "Ling yang menyemak draf itu.» The same frame asks about the plan: «Siapa yang akan menelefon?» (Who will phone?) with «akan». For «menolong», "
     "remember the difference between asking for help and talking about it: «Tolong!» or «Tolong semak draf ini» is the request (chapter 8), "
     "and «Cik Mei Ling menolong saya» says that she helped.",
     "11Aの型が新しい動詞で戻ってきます：«Siapa yang menyemak draf itu?» 答えでは «yang» の前に動作主を置きます：«Cik Mei Ling yang menyemak draf itu.» "
     "同じ型で予定もたずねられます：«Siapa yang akan menelefon?»（誰が電話しますか。）«akan» を使います。«menolong» は、頼むことと話すことの違いを覚えてください："
     "«Tolong!» や «Tolong semak draf ini» が依頼（第8章）で、«Cik Mei Ling menolong saya» は助けてくれたという報告です。",
     'Japanese 誰が〜しますか and 〜するのは◯◯さんです match closely, just as in unit 11A. 助ける and 手伝う both fit «menolong», and the request '
     '手伝ってください is «Tolong …» with the root.',
     '日本語の「誰が〜しますか」と「〜するのは◯◯さんです」は、11Aと同じようによく対応します。「助ける」も「手伝う」も «menolong» にあたり、依頼の「手伝ってください」は語根を使った '
     '«Tolong …» です。'),
]

# Kata-Kata scenario lines ms-c11-s09 to s18, extended to 12 turns.
DIALOGUE = [
    ('Tanaka', 'Cik Mei Ling, draf slaid itu sudah siap?'),
    ('Mei Ling', 'Belum. Saya masih menyemak draf itu. Tarikh akhir hari Jumaat, ya?'),
    ('Tanaka', 'Ya, hari Jumaat. Saya mengira jumlah itu semalam, tetapi tolong semak sekali lagi.'),
    ('Mei Ling', 'Baik. Draf itu akan siap petang ini. Nanti saya menghantar mesej.'),
    ('Tanaka', 'Terima kasih. Hujung minggu ini cik buat apa?'),
    ('Mei Ling', 'Saya mahu mendaki dengan kawan saya. Encik pula?'),
    ('Tanaka', 'Saya mahu memasak. Isteri saya mengajar saya memasak nasi lemak.'),
    ('Mei Ling', 'Wah, bagus! Boleh saya mengecas telefon saya di sini? Bateri sudah habis.'),
    ('Tanaka', 'Boleh. Letak telefon itu di atas meja.'),
    ('Mei Ling', 'Terima kasih! Mari kita minum kopi. Saya yang membayar.'),
    ('Tanaka', 'Terima kasih, cik. Saya mahu memesan kopi O.'),
    ('Mei Ling', 'Saya pula mahu memesan teh tarik dan roti canai.'),
]
VARIANT = [
    ('Rahman', 'Puan Aini, slaid itu sudah dihantar?'),
    ('Aini', 'Belum. Saya masih memilih gambar untuk slaid itu. Tarikh akhir hari Khamis, ya?'),
    ('Rahman', 'Ya, hari Khamis. Tolong semak jumlah itu sekali lagi.'),
    ('Aini', 'Baik. Slaid itu akan siap esok. Nanti saya menghantar mesej.'),
    ('Rahman', 'Terima kasih. Hujung minggu ini puan buat apa?'),
    ('Aini', 'Saya mahu melancong ke Johor Bahru dengan keluarga saya. Encik pula?'),
    ('Rahman', 'Saya mahu menyewa basikal dan berbasikal dengan kawan.'),
    ('Aini', 'Seronok! Boleh saya meminjam pen encik? Pen saya rosak.'),
    ('Rahman', 'Boleh. Ambil pen ini.'),
    ('Aini', 'Terima kasih! Mari kita minum teh. Saya yang membayar.'),
]
LISTENING = [
    ('Tanaka', 'Cik Mei Ling, apa rancangan cik pada hujung minggu?'),
    ('Mei Ling', 'Pada hari Sabtu saya mahu mendaki dengan kawan saya. Kami bertolak pukul enam pagi.'),
    ('Tanaka', 'Cik membawa apa?'),
    ('Mei Ling', 'Saya membawa air dan roti. Malam ini saya juga mahu mengecas telefon saya.'),
    ('Tanaka', 'Pada hari Ahad pula?'),
    ('Mei Ling', 'Saya mahu melancong ke Johor Bahru dengan keluarga saya. Kami menyewa kereta di sana.'),
    ('Tanaka', 'Wah! Berapa sewa kereta itu?'),
    ('Mei Ling', 'Seratus ringgit untuk satu hari. Kawan saya membayar dulu.'),
    ('Tanaka', 'Seronok! Tetapi draf slaid itu bagaimana? Tarikh akhir hari Isnin, ya?'),
    ('Mei Ling', 'Ya. Saya menyemak draf itu hari Jumaat. Selepas itu saya menghantar draf itu ke Osaka.'),
    ('Tanaka', 'Baik. Siapa yang akan menelefon Osaka?'),
    ('Mei Ling', 'Encik Rahman yang akan menelefon mereka hari Isnin pagi.'),
    ('Tanaka', 'Terima kasih, cik. Selamat bercuti!'),
    ('Mei Ling', 'Terima kasih, encik. Saya pergi dulu, kawan saya sedang menunggu di lif.'),
]

CULTURE = [
    'In the office you will meet «tarikh akhir» in a notice, a form or an email, and «deadline» in a chat or at a meeting: «Tarikh akhir hari Jumaat» '
    'and «Deadline hari Jumaat» mean the same. This course teaches «tarikh akhir» first, as the formal and written word, and you will '
    'understand «deadline» when you hear it. In the same way «menukar» (to change, to exchange) is the standard word and «tukar» is what '
    'people usually say: «Saya mahu tukar bilik.»',
    'Japanese learners are often caught by 借りる. Malay has two verbs: «menyewa» is to rent as a tenant, for a longer time and for money, '
    'and «meminjam» is to borrow something for a while: «Kami menyewa rumah» but «Saya meminjam pen awak.» Likewise 聞く and 見る each have '
    'several Malay verbs, so decide which meaning you want before you pick the verb.',
    'A request to a colleague is short and plain. «Tolong semak draf ini» uses the bare root «semak», and the colleague answers «Baik» or «Boleh». '
    'You do not add a long polite phrase. When you say what someone is doing, use the meN- form: «Cik Mei Ling sedang menyemak draf itu.»',
    '«mengecas telefon» is the ordinary Malaysian way to say that you are charging a phone, and asking «Boleh saya mengecas telefon saya di sini?» is '
    'polite and normal in an office. Weekend plans such as «mendaki» (hiking) and «melancong» (travelling for pleasure) are a friendly topic: ask «Hujung minggu ini awak buat apa?» '
    'and listen for the plan.',
]
CULTURE_JA = [
    '職場では、掲示・書類・メールでは «tarikh akhir»、チャットや会議では «deadline» を目にします。«Tarikh akhir hari Jumaat»と«Deadline hari Jumaat»は同じ意味です。'
    'このコースでは、あらたまった書き言葉として «tarikh akhir» を先に教え、«deadline» は聞いて分かるようにします。同じように、«menukar»（替える・交換する）が標準の語で、'
    'ふだんは «tukar» と言う人が多いです：«Saya mahu tukar bilik.»',
    '日本人の学習者は「借りる」でつまずきがちです。マレー語には二つの動詞があります。«menyewa» は借り手として、長い期間、お金を払って借りること、'
    '«meminjam» は物を一時的に借りることです：«Kami menyewa rumah»ですが«Saya meminjam pen awak»です。同じように「聞く」と「見る」にも、それぞれいくつかのマレー語の動詞があるので、'
    '言いたい意味を決めてから動詞を選びましょう。',
    '同僚への依頼は短くシンプルです。«Tolong semak draf ini» は語根の «semak» をそのまま使い、同僚は «Baik» か «Boleh» と答えます。長いていねいな言い方を付け足す必要はありません。'
    '誰かがしていることを言うときは meN- の形を使います：«Cik Mei Ling sedang menyemak draf itu.»',
    '«mengecas telefon» は、携帯電話を充電するときのふつうのマレーシアの言い方で、«Boleh saya mengecas telefon saya di sini?» と頼むのは職場でもていねいで自然です。'
    '«mendaki»（ハイキング）や «melancong»（楽しみの旅行）のような週末の予定は親しみのある話題です：«Hujung minggu ini awak buat apa?»とたずね、予定を聞きましょう。',
]

# The review block after unit 11B (plan section 1: Review 1, chapters 10 to 11 with the Stage 1 passive and aspect).
EXTRA = dict(
    slug='review-block', type='Reading and writing', sub_type='composition', kind='review',
    title='Review block · Chapters 10 and 11 with the passive and the markers',
    goal='I can use ber- verbs, meN- verbs, «di-» verbs and the markers «sudah», «belum», «sedang», «akan» together in one office exchange without notes.',
    grammar=['ms-c10-g02', 'ms-c10-g03', 'ms-c11-g02', 'ms-c11-g03', 'ms-c11-g04', 'ms-c11-g05', 'ms-c11-g08'],
    patterns=['ms-c10-f01', 'ms-c10-f02', 'ms-c11-f01', 'ms-c11-f02', 'ms-c11-f03', 'ms-c11-f04'],
    model=['Chapters 10 and 11 in one exchange (all names and times are fictional):',
           'A: «Selamat pagi, Puan Aini. Pukul berapa mesyuarat bermula?» B: «Pukul sepuluh. Encik Rahman sudah membaca emel itu.»',
           'A: «Siapa yang menghantar fail itu?» B: «Fail itu dihantar oleh Cik Mei Ling. Dia bekerja dari rumah hari ini.»',
           'A: «Saya sedang menulis jawapan. Puan sudah bersarapan?» B: «Belum. Saya membeli kopi dan kuih di gerai.»',
           'A: «Pukul berapa kita bertolak ke Shah Alam?» B: «Pukul dua. Saya akan menunggu encik di lif.»',
           'A: «Kenapa Encik Rahman tidak berehat?» B: «Sebab dia masih menyemak draf itu.»',
           'Notice: ber- verbs have no object («bermula», «bekerja», «bertolak»); meN- verbs take the thing directly («membaca emel»); the «di-» partner puts the '
           'thing first («Fail itu dihantar oleh …»); the markers go in front of any of them. / 気づくこと：ber- の動詞は目的語をとらず、meN- の動詞は物をすぐあとに置き、'
           '«di-» の相手は物が先に来て、マーカーはどれの前にも付きます。'],
    plan=['0–5 Recall: say three things you do every morning (ber-) and three things you did with a file (meN-).',
          '5–15 Mixed input: read the model; underline every ber- verb, meN- verb and «di-» verb and name the marker in front of each.',
          '15–30 Alternating role task: in pairs, one is a manager who asks and one is the colleague who answers; swap after seven minutes (task below).',
          '30–40 Changed situation: the manager says the meeting now starts earlier and the file has not arrived; the colleague explains who is doing what.',
          '40–45 Self-check against the list below, then one thing to practise at home.',
          '0–5 復習・5–15 混合の入力・15–30 役割交代のタスク・30–40 状況の変更・40–45 自己チェック。'],
    task=['Part 1 (15 min, alternating): A is the manager and asks about the morning: «Pukul berapa mesyuarat bermula?», «Siapa yang menghantar fail itu?», '
          '«Awak sedang menulis apa?», «Awak sudah bersarapan?» B answers with at least one ber- verb, one meN- verb and one «di-» sentence. After seven minutes swap.',
          'Part 2 (10 min, changed situation): A says «Maaf, mesyuarat bermula pukul sembilan dan fail itu belum sampai.» B says who will phone, who is checking the draft '
          'and who is waiting, using «akan», «sedang» and «belum».',
          'Part 3 (5 min): write three sentences about your own morning, one with each kind of verb.',
          'パート1：交代でマネージャーと同僚を演じます。パート2：状況が変わり、同僚は誰が電話し、誰が下書きを確認し、誰が待っているかを説明します。パート3：自分の朝について、'
          '三種類の動詞を一つずつ使った3文を書きます。'],
    check=['☐ ber- verbs have no object and keep the spelling of their card (be- in «bekerja», «berehat»).',
           '☐ meN- verbs have the right front for the first sound of the root («membaca», «menulis», «memanggil», «menyemak», «mengecas»).',
           '☐ The «di-» sentence puts the thing first and «oleh» before the doer.',
           '☐ A request uses the plain root («Tolong semak draf ini»).',
           '☐ The marker («sudah», «belum», «sedang», «akan») stands in front of the verb and the verb does not change.'],
    answer='Any natural exchange that follows the checklist. Model: «Mesyuarat bermula pukul sembilan. Saya sudah membaca emel itu. Fail itu dihantar oleh Cik '
           'Mei Ling. Encik Rahman akan menelefon Osaka. Saya sedang menyemak draf itu, dan Puan Aini sedang menunggu di lif.»',
    key_extra=['Mark for the task first (the right kind of verb in each answer, a marker, one «di-» sentence), then for form (the spelling of the front, «oleh»). '
               'Accept the everyday root in speech, but ask for the standard form once in the written part.',
               'A review block has no new words. Every word is from chapters 1 to 11; the three core groups of 10A, 10B, 11A and 11B all return.'],
    explain=('ユニット11Bのあとの復習（45分）：ber-・meN-・«di-» の動詞とマーカーを一つの会話でノートなしで使い、状況の変更にも対応します。日本語は未監修です。',
             'The review block after unit 11B (45 minutes): use ber- verbs, meN- verbs, «di-» verbs and the markers in one exchange without notes, then cope with a changed situation.'),
)

CFG = dict(
    chapter=11, label='11B', unit_id='ms-c11b',
    menu_title='Chapter 11 · meN- verbs', genre='Work',
    prerequisite_units=['ms-c11a'], prereq_grammar=['ms-c11-g02', 'ms-c11-g08', 'ms-c04-g06', 'ms-c08-g02'],
    unit_goal='Check a draft and confirm a deadline, say what you will do at the weekend, and use the rest of the meN- spelling: meny-, meng- for k, menge-.',
    core=CORE,
    recognition=[('Spoken partners of «menukar» and «tarikh akhir»', RECOGNITION)],
    revision=[('Roots of the meN- verbs', REV_ROOTS), ('The office and the draft', REV_WORK), ('Free time and food', REV_FREE),
              ('Time and markers', REV_TIME)],
    core_groups=[('The draft and the deadline', DRAFT), ('Messages, phones, money and choices', THINGS),
                 ('Free time, help and renting', LIFE)],
    grammar_ids={'active': 'ms-c11-g02', 'passive': 'ms-c11-g03', 'who': 'ms-c11-g04', 'now': 'ms-c11-g05',
                 'request': 'ms-c11-g06', 'plans': 'ms-c11-g07', 'spelling': 'ms-c11-g08'},
    grammar=['request', 'plans', 'active', 'who', 'spelling'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 23 cards ms-c11-021 to ms-c11-043 (the cards ms-c11-042 «tukar» and ms-c11-043 «deadline» are recognise only)',
    frame_list='ms-c11-f04, f06, f01 and f03', frame_list_ja='f04・f06・f01・f03', extra=EXTRA,
    goals={'A': 'I can request a check with «Tolong semak …» and say what I want to do this weekend with «mahu» and a meN- verb.',
           'B': 'I can ask and answer about a draft, a deadline and the weekend, and spell the meN- verbs with s, k and one-syllable roots.',
           'C': 'I can follow a colleague\'s weekend plans and a message about a draft, and agree when the draft will be ready.',
           'D': 'I can check the spelling of the meN- verbs and correct a short message about a draft.',
           'E': 'I can confirm a deadline and chat about the weekend in a short role-play, and handle a moved deadline.'},
    goals_ja={'A': '«Tolong semak …» で確認を頼み、«mahu» ＋ meN- の動詞で今週末したいことを言える。',
              'B': '下書き・締め切り・週末についてたずね、答えられる。s・k・一音節の語根の meN- の動詞をつづれる。',
              'C': '同僚の週末の予定と下書きについてのメッセージが分かり、下書きがいつできるかを決められる。',
              'D': 'meN- の動詞のつづりを確認し、下書きについての短いメッセージを直せる。',
              'E': '短いロールプレイで締め切りを確認して週末の話をし、締め切りの変更にも対応できる。'},
    setting='A Tuesday afternoon at a fictional Japanese company in Kuala Lumpur: «Encik» Tanaka and «Cik» Mei Ling check a slide draft and its deadline, '
            'then talk about the weekend over coffee. All names, times and plans are fictional.',
    setting_ja='火曜日の午後、クアラルンプールの架空の日本企業。田中さんとメイリンさんが、スライドの下書きと締め切りを確認し、そのあとコーヒーを飲みながら週末の話をします。'
               '名前・時刻・予定はすべて架空です。',
    recall=['Without notes, from unit 11A: say who sent a file, who received it and what you are doing now, with the doer first. / ユニット11Aの復習：誰がファイルを送り、'
            '誰が受け取ったか、今何をしているかを、動作主を先にして言いましょう。',
            'Recall prompt: «Siapa yang menghantar fail itu?» «Siapa yang menerima fail itu?» «Awak sedang menulis apa?»'],
    recall_key='e.g. «Puan Aini yang menghantar fail itu.» «Encik Rahman yang menerima fail itu.» «Saya sedang menulis emel.» Then show the new request '
               'form: «Tolong semak draf ini.»',
    patterns=P, pattern_ids=['ms-c11-f04', 'ms-c11-f06', 'ms-c11-f01', 'ms-c11-f03'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 11 frames f04 and f06, with f01 and f03 from unit 11A returning with the 11B verbs (f02 and f05 are unit 11A).',
    pattern_keys=['Pattern 1: the request takes the plain root («Tolong semak draf ini»). If a learner says *«Tolong menyemak draf ini», accept the meaning and '
                  'model the root. Teach «tarikh akhir» in writing and accept «deadline» in speech.',
                  'Pattern 2: «mahu» + a meN- verb. Contrast «menyewa» (rent) and «meminjam» (borrow). «melancong» takes «ke» + a place and no object.',
                  'Pattern 3: the spelling session. Use the full table: ‹mem-› before b; t, p, s, k drop; ‹meng-› before h or a vowel; ‹men-› before c, d, j; '
                  '‹me-› before l, m, n, r, w, y; ‹menge-› before a one-syllable root. Say the root aloud first. Do not drill a verb that is not in the ledger.',
                  'Pattern 4: «Siapa yang» + a meN- verb, answered with the doer in front of «yang» or with a short name.'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 7, 9, 11),
    drills={
        'repeat_frame': 'Frame: «Tolong semak» [«draf» / «slaid» / «jumlah»] «ini.» «Hujung minggu ini saya mahu» [«mendaki» / «memasak» / «melancong»].',
        'repeat': ['«Tolong semak draf ini.»', '«Cik Mei Ling sedang menyemak draf itu.»', '«Tarikh akhir draf itu hari Jumaat.»',
                   '«Hujung minggu ini saya mahu mendaki dengan kawan saya.»', '«Boleh saya mengecas telefon saya di sini?»',
                   '«Isteri saya mengajar saya memasak nasi lemak.»', '«Siapa yang akan menelefon pejabat di Jepun?»',
                   '«Saya yang membayar.»'],
        'substitute': ['«Tolong semak draf ini.» (cue: «slaid»)', '«Hujung minggu ini saya mahu mendaki.» (cue: «melancong», «ke Johor Bahru»)',
                       '«Saya memesan teh tarik.» (cue: «kopi O»)', '«Cik Mei Ling menyemak draf itu.» (cue: «Encik Rahman», «mengira», «jumlah»)',
                       '«Kami menyewa rumah dekat stesen.» (cue: «bilik», «dekat pejabat»)',
                       '«Boleh saya meminjam pen awak?» (cue: «mengecas», «telefon saya»)',
                       '«Siapa yang menyemak draf itu?» (cue: «menyimpan», «fail»)', '«Isteri saya mengajar saya memasak.» (cue: «kawan saya»)'],
        'transform': ['Spoken to standard: «Saya tukar bilik.»', 'Spoken to standard: «Deadline hari Jumaat.»',
                      'Spoken to standard: «Saya nak masak nasi lemak.»', 'Request to statement with «sedang»: «Tolong semak draf ini.» («Cik» Mei Ling)',
                      'Statement to request: «Saya menyemak slaid itu.»', 'Make it a question with «Siapa yang»: «Encik Rahman menelefon mereka.»',
                      'Make it negative: «Saya menyewa rumah itu.»', 'Marker «akan»: «Saya menghantar mesej.»',
                      'Marker «sudah»: «Mei Ling menyemak draf itu.»', 'Add «hujung minggu ini» and «mahu»: «Saya mendaki dengan kawan saya.»'],
        'question and answer': ['«Tarikh akhir draf itu bila?» (cue: Friday)', '«Hujung minggu ini awak buat apa?» (cue: hiking with a friend)',
                                '«Awak mahu memesan apa?» (cue: «teh tarik»)', '«Siapa yang membayar?» (cue: I do)',
                                'You hear: «Saya menyewa rumah dekat stesen.» Ask the question («di mana»).',
                                'You hear: «Cik Mei Ling menyemak draf itu.» Ask the question («Siapa yang …?»).',
                                'You hear: «Saya mahu melancong ke Johor Bahru.» Ask the question («ke mana»).',
                                'You hear: «Draf itu akan siap petang ini.» Ask the question («bila»).'],
        'question-word choice': ['«___ yang menyemak draf itu?» → «Cik Mei Ling.»', '«Tarikh akhir draf itu ___?» → «Hari Jumaat.»',
                                 '«Hujung minggu ini awak buat ___?» → «Saya mahu mendaki.»', '«Awak mahu melancong ___?» → «Ke Johor Bahru.»',
                                 '«___ awak tidak menelefon mereka?» → «Sebab saya sibuk.»', '«Awak menyewa rumah di ___?» → «Dekat stesen.»',
                                 '«Draf itu siap ___?» → «Pukul lima.»', '«Sewa rumah itu ___ sebulan?» → «Tiga ratus ringgit.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. The request takes the plain root; the statement takes the meN- verb.',
                   'Cover the line and say it from the English: please check this draft; Mei Ling is checking the draft; the deadline of the draft is '
                   'Friday; this weekend I want to go hiking with my friend; may I charge my phone here?; my wife is teaching me to cook «nasi lemak»; '
                   'who will phone the office in Japan?; I am the one who pays.'],
        'substitute': ['1 «Tolong semak slaid ini.» 2 «Hujung minggu ini saya mahu melancong ke Johor Bahru.» 3 «Saya memesan kopi O.» '
                       '4 «Encik Rahman mengira jumlah itu.»',
                       '5 «Kami menyewa bilik dekat pejabat.» 6 «Boleh saya mengecas telefon saya?» 7 «Siapa yang menyimpan fail itu?» '
                       '8 «Kawan saya mengajar saya memasak.»'],
        'transform': ['1 «Saya menukar bilik.» 2 «Tarikh akhir hari Jumaat.» 3 «Saya mahu memasak nasi lemak.» 4 «Cik Mei Ling sedang menyemak draf itu.» '
                      '5 «Tolong semak slaid itu.»',
                      '6 «Siapa yang menelefon mereka?» 7 «Saya tidak menyewa rumah itu.» 8 «Saya akan menghantar mesej.» '
                      '9 «Mei Ling sudah menyemak draf itu.» 10 «Hujung minggu ini saya mahu mendaki dengan kawan saya.»'],
        'question and answer': ['1 «Tarikh akhir draf itu hari Jumaat.» 2 «Hujung minggu ini saya mahu mendaki dengan kawan saya.» 3 «Saya mahu memesan teh tarik.» '
                                '4 «Saya yang membayar.»',
                                '5 «Awak menyewa rumah di mana?» 6 «Siapa yang menyemak draf itu?» 7 «Awak mahu melancong ke mana?» '
                                '8 «Bila draf itu akan siap?»'],
        'question-word choice': ['1 «Siapa» 2 «bila» 3 «apa» 4 «ke mana» '
                                 '5 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 6 «di mana» 7 «pukul berapa» '
                                 '8 «berapa»'],
    },
    short_dialogues=[
        ('Draf itu sudah siap?', 'Belum. Saya masih menyemak draf itu.', 'at the desk'),
        ('Hujung minggu ini awak buat apa?', 'Saya mahu mendaki dengan kawan saya.', 'on a Friday'),
        ('Boleh saya mengecas telefon saya di sini?', 'Boleh. Letak telefon itu di atas meja.', 'in the office'),
        ('Awak mahu memesan apa?', 'Saya mahu memesan teh tarik.', 'at the cafe')],
    short_keys=['1 «Tarikh akhir hari Jumaat, ya?» 2 «Baik. Nanti saya menghantar mesej.» (or «Tolong semak sekali lagi.»)',
                '3 «Seronok! Saya pun suka mendaki.» 4 «Terima kasih. Bateri saya sudah habis.»'],
    markers=dict(
        title='Markers and the request with meN- verbs', grammar='now',
        instructions=['Say each sentence again with the marker or time cue in brackets. The meN- verb never changes; only the marker does. A request uses the plain root. / '
                      'かっこ内のマーカーか時の言葉を付けて言い直します。meN- の動詞は変わらず、前に付く語だけが変わります。依頼は語根をそのまま使います。'],
        items=['«Cik Mei Ling menyemak draf itu.» (marker: «sudah»)', '«Saya menghantar mesej.» (marker: «belum»)',
               '«Encik Rahman menelefon mereka.» (marker: «akan»)', '«Saya mengira jumlah itu.» (marker: «sedang»)',
               '«Saya menyewa rumah itu.» (marker: «baru»)', '«Kami memilih slaid itu.» (marker: «masih»)',
               'Answer «Draf itu sudah disemak?» (marker: «belum»)', 'Make a request about the slide: «semak»'],
        bridge=['«sudah menyemak» ≈ もう確認した · «belum menghantar» ≈ まだ送っていない · «akan menelefon» ≈ 電話する予定 · '
                '«sedang mengira» ≈ 計算している · «baru menyewa» ≈ 借りたばかり',
                'Japanese changes the verb ending (確認した / 確認していない); Malay keeps «menyemak» and changes only the marker. / '
                '日本語は動詞の語尾が変わりますが、マレー語は «menyemak» のままで、前の語だけが変わります。'],
        key=['1 «Cik Mei Ling sudah menyemak draf itu.» 2 «Saya belum menghantar mesej.» 3 «Encik Rahman akan menelefon mereka.» '
             '4 «Saya sedang mengira jumlah itu.»',
             '5 «Saya baru menyewa rumah itu.» 6 «Kami masih memilih slaid itu.» 7 «Belum. Draf itu belum disemak.» (or «Belum. Saya belum menyemak draf itu.») '
             '8 «Tolong semak slaid ini.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、第11章の meN- の動詞と組み合わせて言い、依頼の «Tolong semak …» も練習します。',
                 'Combine the chapter 4 markers with the meN- verbs and practise the request «Tolong semak …»: the verb never changes, only the marker does.')),
    question_note='Chapter 11 adds no new question word. The meN- verbs fit every question you know: «Siapa yang menyemak draf itu?», '
                  '«Tarikh akhir draf itu bila?», «Awak mahu melancong ke mana?», «Awak menyewa rumah di mana?», «Berapa sewa rumah itu?» / '
                  '第11章で新しい疑問語は増えません。meN- の動詞は知っている疑問語すべてと使えます：'
                  '«Siapa yang menyemak draf itu?»、«Tarikh akhir draf itu bila?»、«Awak mahu melancong ke mana?»、«Awak menyewa rumah di mana?»、'
                  '«Berapa sewa rumah itu?»',
    question_tasks=['Ask a colleague what they are checking. («apa»)', 'Ask who is checking the draft. («siapa»)',
                    'Ask where your colleague rents a flat. («di mana»)', 'Ask formally whether the slide is ready. («Adakah»)',
                    'Ask politely whether you may charge your phone. («Bolehkah»)', 'Ask how many slides there are. («berapa»)',
                    'Ask when the deadline is. («bila»)', 'Ask what time the draft will be ready. («pukul berapa»)',
                    'Ask on what day your colleague goes hiking. («hari apa»)', 'Ask how your colleague counts the total. («bagaimana»; spoken «macam mana»)',
                    'Ask why your colleague did not phone Japan. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which slide your colleague chose. («yang mana»)', 'Ask where your colleague travels at the weekend. («ke mana»)',
                    'Ask where the message came from. («dari mana»)', 'Ask how far the station is from the office. («berapa jauh»)',
                    'Ask how long your colleague waits for the draft. («berapa lama»)', 'Ask how many cups of tea your colleague orders. («berapa» with a counter)',
                    'Ask who made the coffee. («siapa» with «oleh»)'],
    question_keys=['1 «Awak sedang menyemak apa?» 2 «Siapa yang menyemak draf itu?» 3 «Awak menyewa rumah di mana?»',
                   '4 «Adakah slaid itu sudah siap?» 5 «Bolehkah saya mengecas telefon saya?» 6 «Berapa slaid ada?»',
                   '7 «Tarikh akhir bila?» 8 «Pukul berapa draf itu akan siap?» 9 «Pada hari apa awak mendaki?»',
                   '10 «Bagaimana awak mengira jumlah itu?» (spoken: «Macam mana awak kira jumlah itu?») 11 «Kenapa awak tidak menelefon Jepun?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab saya sibuk.» / «Kerana saya sibuk.»',
                   '12 «Awak memilih slaid yang mana?» 13 «Hujung minggu ini awak melancong ke mana?» 14 «Mesej itu datang dari mana?»',
                   '15 «Berapa jauh stesen dari pejabat?» 16 «Berapa lama awak menunggu draf itu?» 17 «Awak memesan berapa cawan teh?»',
                   '18 «Kopi ini dibuat oleh siapa?»'],
    listening=LISTENING,
    listening_context='On Friday afternoon «Encik» Tanaka asks «Cik» Mei Ling about her weekend plans and about the draft. / 金曜日の午後、田中さんがメイリンさんに週末の予定と下書きのことをたずねます。',
    listening_before=['Predict: which meN- verbs will you hear? Write three guesses (for example «mendaki», «mengecas», «menyemak»). / 聞こえそうな meN- の動詞を三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['What does Mei Ling want to do on Saturday, and when do they set off?', 'What does she bring?', 'What does she want to do tonight?',
                      'Where does she want to travel on Sunday?', 'What do they rent there, and for how much?', 'When is the deadline of the draft?',
                      'When does she check the draft?', 'Where does she send the draft?', 'Who will phone Osaka, and when?'],
    listen_answers=['go hiking with a friend; at six in the morning', 'water and bread', 'charge her phone', 'Johor Bahru', 'a car (a hundred «ringgit» a day)', 'Monday',
                    'on Friday', 'to Osaka', 'Rahman; Monday morning'],
    listening_after=['Compare answers, then shadow lines 2, 4 and 8 after the teacher. / 答えを比べ、2・4・8行目をシャドーイングします。',
                     'Tell your partner your plans for this weekend in four sentences with «mahu» and a meN- verb. / 今週末の予定を、«mahu» と meN- の動詞を使って4文でパートナーに話しましょう。'],
    test_listen=[(1, 'go hiking with a friend; at six', ['mendaki', 'bertolak', 'pukul']),
                 (3, 'water and bread; charge her phone', ['membawa', 'mengecas', 'telefon']),
                 (5, 'she travels to Johor Bahru and they rent a car', ['melancong', 'menyewa']),
                 (8, 'on Monday', ['tarikh akhir', 'hari']),
                 (9, 'on Friday; to Osaka', ['menyemak', 'menghantar']),
                 (11, 'Rahman, on Monday morning', ['menelefon', 'hari', 'pagi'])],
    test_listen_prompts=['What does Mei Ling want to do on Saturday, and when do they set off?', 'What does she bring, and what does she want to do tonight?',
                         'Where does she travel on Sunday, and what do they rent?', 'When is the deadline of the draft?',
                         'When does she check the draft, and where does she send it?', 'Who will phone Osaka, and when?'],
    reading_title='Reading and writing · A message about a draft',
    reading=['Fictional message in the team chat (all names, places and times are invented):',
             '«Selamat petang, Encik Tanaka. Draf slaid sudah siap. Saya sudah menyemak draf itu dua kali.»',
             '«Tarikh akhir hari Jumaat. Saya akan menghantar slaid itu pukul lima.»',
             '«Tolong semak jumlah di slaid kedua. Terima kasih. Mei Ling»',
             'Notice on the board: «BILIK DISEWA. Dekat stesen. Sewa tiga ratus ringgit sebulan. Sila telefon Encik Lim.»'],
    read_questions=['What is ready?', 'How many times has Mei Ling checked the draft?', 'When is the deadline?', 'What time will she send the slides?',
                    'What should Tanaka check?', 'What is for rent, and what does it cost a month?',
                    'Say in Malay: "Please check this message."'],
    read_answers=['the slide draft', 'twice', 'Friday', 'at five', 'the total on the second slide', 'a room; three hundred «ringgit»',
                  '«Tolong semak mesej ini.»'],
    write_instruction='Write a short message to a colleague about a draft: say that you checked it, give the deadline and ask the colleague to check one thing. / '
                      '同僚に下書きについての短いメッセージを書きましょう。確認したこと、締め切り、同僚に確認してほしいことを一つ入れます。',
    write_model='«Selamat pagi, Puan Aini. Saya sudah menyemak draf itu. Tarikh akhir hari Jumaat. Tolong semak slaid kedua, ya. Terima kasih.»',
    writing_type='message',
    task_title='Task · Check a draft and confirm when it will be ready',
    role_a=['Your information (fictional): you wrote a slide draft. You are still checking it; you will finish this afternoon; the deadline is Friday; at the '
            'weekend you want to go hiking.',
            'B asks about the draft. Answer, and ask B about the weekend.',
            'Aの情報（架空）：スライドの下書きを書きました。まだ確認中で、今日の午後に終わります。締め切りは金曜日で、週末はハイキングに行きたいです。'
            'Bの質問に答え、Bに週末のことをたずねます。'],
    role_b=['You are the manager. Ask A whether the draft is ready, who is checking it, when the deadline is, and ask A to check the total once more.',
            'Then say what you want to do at the weekend, and offer to pay for the coffee.',
            'Bはマネージャーです。Aに下書きができたか、誰が確認しているか、締め切りはいつかをたずね、合計をもう一度確認してほしいと頼みます。'
            'そのあと、週末にしたいことを言い、コーヒーをおごると申し出ます。'],
    change=['Halfway, B says: «Maaf, tarikh akhir sudah hari Khamis.» A says when the draft will be ready and what A will do.',
            '途中でBが «Maaf, tarikh akhir sudah hari Khamis.» と言います。Aは下書きがいつできるか、何をするかを言います。'],
    success=['☐ B uses «Tolong semak …» for the request and «Siapa yang …?» or «… sedang … apa?» once.',
             '☐ A answers with a meN- verb and a marker («masih», «sedang», «akan»).',
             '☐ After the change, A gives a new time and a plan, and they agree.'],
    task_key='«Draf itu sudah siap?» — «Belum. Saya masih menyemak draf itu. Tarikh akhir hari Jumaat, ya?» — «Ya. Tolong semak jumlah itu sekali lagi.» — «Baik. Draf itu '
             'akan siap petang ini.» — «Hujung minggu ini awak buat apa?» — «Saya mahu mendaki dengan kawan saya.» — Change: «Maaf, tarikh akhir sudah hari Khamis.» — «Baik. '
             'Saya akan menghantar draf itu esok.»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 11 card notes ms-c11-021 («menyewa»: rent) and -030 («meminjam»: borrow for a while), -036 («tarikh akhir»: formal and written), '
                    '-041 («mengecas»: menge- before a one-syllable root), -042 («tukar»: spoken for «menukar», recognise only) and -043 («deadline»: spoken for «tarikh akhir», '
                    'recognise only); stage 2 plan section 2 (unit 11B table: the Japanese for «menyewa» and «meminjam» made specific) and decisions W6 (Sam, 13 Nov 2026: '
                    '«mengecas telefon» is normal Malaysian Malay). The note states no figure or rule about Malaysia.',
    culture_prompt='Does Japanese have two words for borrowing like 借りる (rent, borrow)? When do you say 借りる, and when 賃借する?',
    culture_explain=('マレーシアの職場で «tarikh akhir» と «deadline»、«menukar» と «tukar» を聞くこと、「借りる」の二つのマレー語、短い依頼、充電と週末の話題について読みます。',
                     'Read about hearing «tarikh akhir» and «deadline», «menukar» and «tukar» at work, the two Malay verbs for borrowing, the short request, and charging a phone and weekend talk.'),
    quiz_words=['L-0819', 'L-1155', 'L-1156', 'L-1143', 'L-1149', 'L-0849'],
    quiz_meanings=['to check, to review', 'to phone', 'to charge (a phone)', 'to rent as a tenant', 'to borrow', 'deadline (formal, written)'],
    grammar_quiz=[('Write the request: please check this draft.', '«Tolong semak draf ini.»', ['tolong', 'semak', 'draf']),
                  ('Say in Malay: "This weekend I want to go hiking."', '«Hujung minggu ini saya mahu mendaki.»', ['hujung minggu', 'mahu', 'mendaki']),
                  ('Write the standard form: «Saya nak masak nasi lemak.» (spoken «nak»)', '«Saya mahu memasak nasi lemak.»', ['mahu', 'memasak']),
                  ('Write the meN- form of «sewa» in a sentence about a flat.', '«menyewa»: for example «Kami menyewa rumah dekat stesen.»', ['menyewa', 'rumah'])],
    test_reading=['Fictional notice: «BILIK DISEWA. Dekat stesen. Sewa tiga ratus ringgit sebulan. Tarikh akhir: hari Jumaat. Sila telefon Encik Lim.»'],
    reading_quiz=[('What is for rent?', 'a room', ['disewa', 'bilik']),
                  ('How much is the rent a month?', 'three hundred «ringgit»', ['sewa', 'ringgit']),
                  ('When is the deadline?', 'Friday', ['tarikh akhir', 'hari']),
                  ('Whom should you phone?', '«Encik» Lim', ['telefon'])],
    speaking_test='Tell the teacher what you want to do this weekend in three sentences with «mahu» and a meN- verb, then ask for a check: «Tolong semak …».',
    speaking_key='Check: three different meN- verbs spelt and said correctly («mendaki», «memasak», «melancong», «menyewa»); «mahu» in front of the verb; one request with the plain root '
                 '(«Tolong semak …»). Accept «nak» or the everyday root in speech if the standard form was also used once.',
    speaking_words=['mahu', 'mendaki', 'memasak', 'tolong', 'semak'],
    plan={'A_recall': 'unit 11A (who sent and received the file) from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first (the request and the weekend plan), question and answer before the rule; then the vocabulary in three groups with each '
                        'root and the nasal change (the draft and the deadline 6, messages, phones, money and choices 7, free time, help and renting 8). '
                        'Write the full spelling table on the board.',
          'B_recall': 'say your weekend plan with «Hujung minggu ini saya mahu …».',
          'B_drills': 'pattern table, substitution, transformation (spoken to standard first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner says one thing they asked a colleague to check.',
          'D_review': 'cumulative question-word drill (chapters 1 to 11), then the markers drill with new cues and a spelling check of '
                      '«menyewa», «mengira», «mengecas», «memesan», «meminjam».',
          'D_preview': 'the review block for chapters 10 and 11 (45 minutes), then chapter 12 (suffixed verb forms).',
          'E_recall': 'say three things you do for work and one thing you want to do this weekend.',
          'E_listening': 'read the Kata-Kata scenario lines ms-c11-s09 to ms-c11-s18 (Tanaka and «Cik» Mei Ling: the draft, the deadline, the weekend, the coffee) twice; '
                         'learners tick the meN- verbs they hear.',
          'E_roleplay': 'pairs play the same scene with their own draft and weekend plan, without the script.',
          'E_variation': 'a moved deadline: B says the deadline is now Thursday; A says when the draft will be ready, who will check it and who will send it.'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 11 to the office scene report_deadline for this unit, with «mendaki» from the social pack. '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet. The full story already contains later words and suffixes.',
    next_note='Next: the review block after 11B (chapters 10 and 11), then chapter 12 (suffixed verb forms).',
    teacher_notes=['Load: 21 core words in three groups (the draft and the deadline 6; messages, phones, money and choices 7; free time, help and renting 8), two '
                   'recognition entries («tukar» and «deadline»), and revision of the roots, the office, free time and the markers. Suggested order: Block A the '
                   'first group with patterns 1 and 2; Block B the second group with pattern 3 (the spelling table); the third group with pattern 4 in Block B or C. '
                   'If the pilot shows 21 is too many, the natural cut is: «menyemak», «semak», «draf», «tarikh akhir», «mesej», «menelefon», «mendaki», '
                   '«memesan», «menyewa», «mengecas» first; the rest second.',
                   'The nasal-change traps from the Kata-Kata cards: «menyewa», not *mensewa (card ms-c11-021); «mengira», not *mengkira (ms-c11-027); «mengecas», not '
                   '*mengcas (ms-c11-041); «memilih», «meminjam» and «memesan» drop the p (ms-c11-029 to -031); «menolong» drops the t (ms-c11-032). The same rule for ‹menyapu› '
                   '(to sweep, not a ledger word, quoted only): ‹meny-›, not *mensapu. Say the root aloud first, then the front, then the whole verb.',
                   'Other traps: «semak» as a request takes the plain root (card ms-c11-038: «Tolong semak draf ini»), not the meN- form. «menyewa» is to rent and «meminjam» '
                   'to borrow for a while (ms-c11-030); 借りる covers both. «menolong» is a verb ("to help"); «tolong» is the request (chapter 8, ms-c11-032). «melancong» takes no '
                   'object and has no «di-» form (ms-c11-022). «rancangan» is learned as a whole word (ms-c11-037).',
                   'Spoken forms (recognition only): «tukar» for «menukar» (ms-c11-042) and «deadline» for «tarikh akhir» (ms-c11-043). Both are labelled spoken wherever they appear and '
                   'never in a key, a dialogue or the listening. «nak» (spoken «mahu») is a Stage 1 pair: accept it in speech.',
                   'Where Japanese learners usually slip: (1) 借りる for both «menyewa» and «meminjam»; (2) using the meN- form in a request: *«Tolong menyemak draf ini»; '
                   '(3) repeating the first sound of the root: *mensewa, *mengkira; (4) forgetting ‹menge-› for a one-syllable root (*mengcas); (5) hearing «mahu» + a meN- verb as '
                   'a polite future: «mahu» is "want", and «akan» is "will"; (6) 聞く, 見る and 払う have more than one Malay verb: decide the meaning first.',
                   'Standard first: teach the meN- form, accept the everyday root in speech («semak», «tukar», «cas», «telefon»), and never mark it wrong in a speaking task. '
                   'The review block after this unit has no new words.',
                   'The scene follows Kata-Kata c11 (scenario lines ms-c11-s09 to s18, frames f04 and f06, with f01 and f03 returning). All names, times and plans are fictional; '
                   'learners may use their real week or an invented one.',
                   'Cumulative question words: chapters 1 to 11. Chapter 11 adds no new question word.'],
)

UNIT = unit_dict(CFG)
