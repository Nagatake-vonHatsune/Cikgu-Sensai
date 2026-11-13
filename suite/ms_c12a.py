"""Unit 12A: -kan requests and actions for someone: parcels at the guardhouse (Tolong ___ bungkusan ini; Boleh ___ mesej itu?;
Saya mahu ambil ___. Sudah sampai?).

23 core ledger entries, the rows the ledger places in "Ch12 (unit 12A)" (L-1157 to L-1172 and the existing rows L-0595
«pengawal», L-0650 «pejabat pengurusan», L-0653 «blok», L-0654 «unit», L-0658 «pondok pengawal», L-0662 «pemilik» and L-0743
«pastikan»), in three groups, and one recognition entry: L-0608 «nombor tracking» (spoken partner of «nombor penjejakan»), ledger
"Ch12 (unit 12A, recognition ...)"; Kata-Kata card ms-c12-024, recognise only. Each -kan verb is taught as a whole ledger form,
with its root, the chapter of the root and what the suffix adds (for someone, or to make it happen), as the Kata-Kata chapter
12 card notes give them. The pe- and ke-an words («pengawal», «pemilik», «penerima») are taught as whole words. The scene follows
Kata-Kata c12 (scenario lines ms-c12-s01 to s10: collecting a parcel at the guardhouse) and goes further in class: a message for
a guard, a parcel role-play and a parcel that was left in the wrong place. All names, blocks, units and times are fictional.
No Dunia scene primes chapter 12. Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

FORSOMEONE = ['L-1157', 'L-1158', 'L-1159', 'L-1160', 'L-1161', 'L-1162', 'L-1163', 'L-1164', 'L-1165', 'L-1166', 'L-1167', 'L-0743']
GUARDHOUSE = ['L-0595', 'L-0658', 'L-0650', 'L-0662', 'L-0654', 'L-0653']
PARCEL = ['L-1168', 'L-1169', 'L-1170', 'L-1171', 'L-1172']
CORE = FORSOMEONE + GUARDHOUSE + PARCEL
RECOGNITION = ['L-0608']

# Revision: words placed in chapters 1 to 11 that the unit really uses (a test fails if one is not used).
REV_ROOTS = ['L-0528', 'L-0529', 'L-0481', 'L-0483', 'L-0484', 'L-0485', 'L-0574', 'L-0482']
REV_PARCEL = ['L-0430', 'L-1154', 'L-0359', 'L-0426', 'L-0203', 'L-0238', 'L-0237', 'L-0565', 'L-0332']
REV_ASK = ['L-0375', 'L-0076', 'L-0401', 'L-0215', 'L-0026', 'L-0023', 'L-1046', 'L-0016', 'L-0018']
REV_TIME = ['L-0193', 'L-0194', 'L-0189', 'L-0192', 'L-0195', 'L-0191', 'L-0161']

EXAMPLES = {
    # For someone, or to make it happen
    'L-1157': '«Tolong hantarkan bungkusan kecil itu ke unit 8-1.»',
    'L-1158': '«Tolong simpankan bungkusan ini.» (everyday: «Tolong simpan bungkusan ini.»)',
    'L-1159': '«Boleh ambilkan fail itu?»',
    'L-1160': '«Boleh belikan kopi untuk saya?»',
    'L-1161': '«Boleh bawakan beg saya ke lif?»',
    'L-1162': '«Tolong tutupkan pintu itu.»',
    'L-1163': '«Boleh bukakan pintu itu?»',
    'L-1164': '«Tolong letakkan beg di sini.»',
    'L-1165': '«Tolong pulangkan buku itu.»',
    'L-1166': '«Boleh berikan nombor telefon puan?» (everyday: «Boleh bagi nombor telefon puan?»)',
    'L-1167': '«Boleh tunjukkan mesej itu?»',
    'L-0743': '«Tolong pastikan bungkusan itu tidak basah.»',
    # The guardhouse
    'L-0595': '«Pengawal menyimpan bungkusan di pondok pengawal.»',
    'L-0658': '«Bungkusan kecil itu ada di pondok pengawal.»',
    'L-0650': '«Pejabat pengurusan ada di tingkat satu.»',
    'L-0662': '«Pemilik unit itu belum ada di rumah.»',
    'L-0654': '«Blok B, unit 12-3.»',
    'L-0653': '«Blok A, unit 8-1.»',
    # The parcel
    'L-1168': '«Label ini koyak, tetapi nombor unit ada di sini.»',
    'L-1169': '«Penerima Encik Tanaka.»',
    'L-1170': '«Nombor penjejakan ada dalam mesej ini.» (spoken: «nombor tracking»)',
    'L-1171': '«Bungkusan besar itu ada di lobi.»',
    'L-1172': '«Kotak itu koyak.»',
    # Recognise
    'L-0608': '«Nombor tracking ada dalam mesej ini.» (spoken; written and formal: «nombor penjejakan»)',
    # Revision · the roots
    'L-0528': '«hantar» → «hantarkan»: «Saya hantarkan bungkusan itu sekarang.»',
    'L-0529': '«simpan» → «simpankan»: «Saya simpankan bungkusan itu di pondok pengawal.»',
    'L-0481': '«ambil» → «ambilkan»: «Saya mahu ambil bungkusan.»',
    'L-0483': '«bawa» → «bawakan»: «Saya bawa bungkusan besar ini ke atas.»',
    'L-0484': '«buka» → «bukakan»: «Tolong buka pintu itu.»',
    'L-0485': '«tutup» → «tutupkan»: «Tolong tutup pintu itu.»',
    'L-0574': '«letak» → «letakkan»: «Letak beg di sini.»',
    'L-0482': '«bagi» (everyday) = «berikan»: «Boleh bagi nombor telefon puan?»',
    # Revision · the parcel and the building
    'L-0430': '«Ada dua bungkusan di pondok pengawal.»',
    'L-1154': '«Nombor penjejakan ada dalam mesej ini.»',
    'L-0359': '«Kotak besar itu berat.»',
    'L-0426': '«Surat itu untuk Puan Siti.»',
    'L-0203': '«Bungkusan saya sudah sampai?»',
    'L-0238': '«Bungkusan kecil itu bukan untuk encik.»',
    'L-0237': '«Bungkusan besar ini untuk encik.»',
    'L-0565': '«Tolong bukakan pintu itu.»',
    'L-0332': '«Lif di sebelah kiri.»',
    # Revision · asking politely
    'L-0375': '«Tolong simpankan bungkusan ini.»',
    'L-0076': '«Boleh tunjukkan mesej itu?»',
    'L-0401': '«Sila tunjukkan mesej dan nombor penjejakan.»',
    'L-0215': '«Label ini koyak, tetapi nombor unit ada di sini.»',
    'L-0026': '«Tolong hubungi pemilik unit itu nanti.»',
    'L-0023': '«Saya simpankan bungkusan itu di pondok pengawal dulu.»',
    'L-1046': '«Tolong tunggu sekejap.»',
    'L-0016': '«Terima kasih, encik.»',
    'L-0018': '«Maaf, label itu koyak.»',
    # Revision · time and markers
    'L-0193': '«Saya sudah menyimpan bungkusan itu.»',
    'L-0194': '«Saya belum membuka pintu itu.»',
    'L-0189': '«Saya sedang membawa bungkusan itu ke lif.»',
    'L-0192': '«Saya akan menghantar bungkusan itu petang ini.»',
    'L-0195': '«Pengawal baru membuka pintu itu.»',
    'L-0191': '«Saya masih tunggu bungkusan itu.»',
    'L-0161': '«Sekarang saya hantarkan bungkusan itu.»',
}

# For each -kan verb: the root as the Kata-Kata card note gives it, the chapter of the root, what ‹-kan› adds.
# (root, where the root sits in English, in Japanese, what the suffix adds in English, in Japanese)
ROOTS = {
    'L-1157': ('«hantar»', 'Dunia, chapter 2', 'Dunia・第2章', 'send or deliver it for someone', '誰かのために送る・届ける'),
    'L-1158': ('«simpan»', 'Dunia, chapter 2', 'Dunia・第2章', 'keep it for someone', '誰かのために預かる'),
    'L-1159': ('«ambil»', 'Dunia, chapter 4', 'Dunia・第4章', 'get it for someone', '誰かのために取ってくる'),
    'L-1160': ('«beli»', 'chapter 3', '第3章', 'buy it for someone', '誰かのために買ってくる'),
    'L-1161': ('«bawa»', 'Dunia, chapter 4', 'Dunia・第4章', 'bring it for someone', '誰かのために持ってくる'),
    'L-1162': ('«tutup»', 'Dunia, chapter 4', 'Dunia・第4章', 'close it for someone', '誰かのために閉める'),
    'L-1163': ('«buka»', 'Dunia, chapter 4', 'Dunia・第4章', 'open it for someone', '誰かのために開ける'),
    'L-1164': ('«letak»', 'Dunia, chapter 7', 'Dunia・第7章', 'put it somewhere; double k', 'どこかに置く；k が二つ'),
    'L-1165': ('«pulang»', 'chapter 4', '第4章', 'give it back', '返す'),
    'L-1166': ('‹beri›', None, None, 'give; ‹beri› + ‹-kan›, not ‹ber-› + «ikan»; everyday «bagi»', '渡す；‹beri› ＋ ‹-kan› で、‹ber-› ＋ «ikan» ではない；日常は «bagi»'),
    'L-1167': ('‹tunjuk›', None, None, 'show; double k', '見せる；k が二つ'),
    'L-0743': ('‹pasti›', None, None, 'make sure', '確かめる'),
}
_EN = {'L-1157': 'send or deliver for someone (a request)', 'L-1158': 'keep for someone (a request)', 'L-1159': 'get for someone (a request)',
       'L-1160': 'buy for someone (a request)', 'L-1161': 'bring for someone (a request)', 'L-1162': 'close for someone (a request)',
       'L-1163': 'open for someone (a request)', 'L-1164': 'put, place (a request)', 'L-1165': 'return something (a request)',
       'L-1166': 'give (a request)', 'L-1167': 'show (a request)', 'L-0743': 'to make sure'}
_JA = {'L-1157': '送ってあげる・届けてください', 'L-1158': '預かってください', 'L-1159': '取ってきてください', 'L-1160': '買ってきてください',
       'L-1161': '持ってきてください', 'L-1162': '閉めてください', 'L-1163': '開けてください', 'L-1164': '置いてください', 'L-1165': '返してください',
       'L-1166': '渡してください', 'L-1167': '見せてください', 'L-0743': '確かめる・必ず〜するようにする'}


def _opts(lid):
    root, where, where_ja, adds, adds_ja = ROOTS[lid]
    if root.startswith('‹'):
        en_root = f'{root} + ‹-kan› (learn the whole word; the root has no class card of its own)'
        ja_root = f'{root} ＋ ‹-kan›（一語まるごと覚える）'
    else:
        en_root = f'{root} ({where}) + ‹-kan›'
        ja_root = f'{root}（{where_ja}）＋ ‹-kan›'
    return {'en': f'{_EN[lid]} ({en_root}: {adds})', 'ja': f'{_JA[lid]}（{ja_root}：{adds_ja}）'}


VOCAB_OPTS = {lid: _opts(lid) for lid in ROOTS}
VOCAB_OPTS.update({
    'L-0595': {'en': 'security guard (learn the whole word; ‹pe-› words come in Stage 3; the root is ‹kawal›)',
               'ja': '警備員（一語まるごと覚える；‹pe-› の語は第3段階；語根は ‹kawal›）'},
    'L-0662': {'en': 'owner (learn the whole word; ‹pe-› words come in Stage 3; the root is ‹milik›)',
               'ja': '所有者・オーナー（一語まるごと覚える；‹pe-› の語は第3段階；語根は ‹milik›）'},
    'L-1169': {'en': 'recipient, the name on a parcel label (learn the whole word; the root is ‹terima›)',
               'ja': '受取人（荷物のラベルの宛名）（一語まるごと覚える；語根は ‹terima›）'},
    'L-1170': {'en': 'tracking number (the written label; spoken «nombor tracking»)',
               'ja': '追跡番号（書き言葉・ラベル表記；話し言葉は «nombor tracking»）'},
    'L-0608': {'en': 'tracking number (spoken; the written label is «nombor penjejakan»): recognise it, write «nombor penjejakan»',
               'ja': '追跡番号（話し言葉；書き言葉は «nombor penjejakan»）：聞いて分かればよい。書くときは «nombor penjejakan»'},
})

P = [
    ('ms-c12-f01', '«Tolong» ___ «bungkusan ini.»  (a request: ‹-kan› verb + the thing)', [
        'A: «Tolong simpankan bungkusan ini.» B: «Baik, encik. Saya simpankan di pondok pengawal.»',
        'A: «Tolong hantarkan bungkusan kecil itu ke unit 8-1.» B: «Baik. Saya hantarkan sekarang.»',
        'A: «Tolong bukakan pintu itu.» B: «Baik. Pintu sudah dibuka.»',
        'A: «Tolong tutupkan pintu itu.» B: «Baik, saya tutupkan.»',
        'A: «Tolong letakkan kotak itu di sini.» B: «Di sini, ya? Baik.»',
        'A: «Tolong pastikan bungkusan itu tidak basah.» B: «Baik. Saya letakkan di atas meja.»'],
     "‹-kan› goes on the end of a root and gives the verb a new job: do it for someone, or make it happen. «hantar» (send, Dunia, chapter 2) "
     "becomes «hantarkan» (send it for me); «simpan» (keep) becomes «simpankan» (keep it for me); «letak» becomes «letakkan" "» (put it there). "
     "A request has «Tolong» first, then the ‹-kan› verb, then the thing: «Tolong simpankan bungkusan ini.» (the Kata-Kata frame). "
     "Everyday speech often drops the suffix: «Tolong simpan bungkusan ini», «Tolong tutup pintu itu». Both are correct. This course teaches "
     "the ‹-kan› form first, because it shows who the action is for, and you will understand the short form when you hear it. "
     "Watch the spelling: two k in «letakkan» and «tunjukkan» (the root ends in k and ‹-kan› starts with k), and «berikan» is ‹beri› + ‹-kan›, "
     "not ‹ber-› + «ikan». «Pastikan» means to make sure. The thing follows the verb with no little word for it.",
     "‹-kan› は語根の終わりに付いて、動詞に「誰かのためにする」「そうなるようにする」という働きを加えます。«hantar»（送る、Dunia・第2章）は "
     "«hantarkan»（送ってあげる）、«simpan»（預かる）は «simpankan»（預かってあげる）、«letak» は «letakkan»（そこに置く）になります。依頼は «Tolong» が先で、"
     "次に ‹-kan› の動詞、最後に物：«Tolong simpankan bungkusan ini.»（Kata-Kata の文型）。日常会話では接尾辞を落とすことも多いです：«Tolong simpan bungkusan ini.»、"
     "«Tolong tutup pintu itu.» どちらも正しい言い方です。このコースでは、誰のための動作かが分かるので ‹-kan› の形を先に教え、短い形は聞いて分かるようにします。"
     "つづりに注意：«letakkan» と «tunjukkan» は k が二つ（語根の終わりの k と ‹-kan› の k）で、«berikan» は ‹beri› ＋ ‹-kan›（‹ber-› ＋ «ikan» ではありません）。"
     "«Pastikan» は「確かめる」です。物は動詞のすぐあとに置き、「を」にあたる語はありません。",
     'Japanese 〜てください is one pattern for every verb, and 〜てあげる / 〜てくれる says who the action is for. ‹-kan› is closer to 〜てあげる, but it is part of '
     'the verb, not a separate word. It is not a politeness ending, so do not put it on every verb: «Tolong baca emel ini» (read this email) takes no ‹-kan›.',
     '日本語の「〜てください」はどの動詞にも使える一つの型で、「〜てあげる」「〜てくれる」は誰のための動作かを表します。‹-kan› は「〜てあげる」に近いですが、'
     '別の語ではなく動詞の一部です。ていねいさを表す語尾ではないので、どの動詞にも付けてはいけません：«Tolong baca emel ini»（このメールを読んでください）に ‹-kan› は付きません。'),
    ('ms-c12-f02', '«Boleh» ___ «mesej itu?»  (a polite question: ‹-kan› verb + the thing)', [
        'A: «Boleh tunjukkan mesej itu?» B: «Boleh. Ini mesej saya.»',
        'A: «Boleh ambilkan fail itu?» B: «Boleh. Fail yang mana?»',
        'A: «Boleh belikan kopi untuk saya?» B: «Boleh. Satu atau dua?»',
        'A: «Boleh bawakan beg saya ke lif?» B: «Boleh. Beg yang kecil ini?»',
        'A: «Boleh berikan nombor telefon puan?» B: «Boleh. Saya tulis di kertas ini.»',
        'A: «Boleh pulangkan pen saya?» B: «Maaf, saya lupa. Ini pen encik.»'],
     "«Boleh» + a ‹-kan› verb + the thing is the polite question for the same idea: «Boleh tunjukkan mesej itu?» (the Kata-Kata frame) asks for a favour. "
     "The answer is «Boleh.» or «Maaf, tidak boleh.», and a short extra word is natural. The suffix says that the favour is for the speaker: "
     "«ambilkan» (get it for me), «belikan» (buy it for me), «bawakan» (bring it for me), «berikan» (give it to me), «pulangkan» (give it back). "
     "Everyday speech often has the root: «Boleh bagi nombor telefon puan?» («bagi» is the everyday word for «berikan», Dunia, chapter 4). "
     "You can put «Tolong» in front for a softer request: «Boleh tolong hantarkan bungkusan kecil itu ke unit 8-1?»",
     "«Boleh» ＋ ‹-kan› の動詞 ＋ 物は、同じ内容のていねいな質問です：«Boleh tunjukkan mesej itu?»（Kata-Kata の文型）でお願いをします。答えは «Boleh.» か "
     "«Maaf, tidak boleh.» で、短いひとことを足すと自然です。接尾辞は「話し手のために」を表します：«ambilkan»（取ってきて）、«belikan»（買ってきて）、"
     "«bawakan»（持ってきて）、«berikan»（渡して）、«pulangkan»（返して）。日常会話では語根だけのこともあります：«Boleh bagi nombor telefon puan?»"
     "（«bagi» は «berikan» の日常語、Dunia・第4章）。前に «Tolong» を付けるとやわらかい依頼になります：«Boleh tolong hantarkan bungkusan kecil itu ke unit 8-1?»",
     'Japanese 〜てもらえますか is one pattern for every verb. In Malay the favour is in the verb: «tunjukkan» already means 見せてもらえますか in this question. '
     'Say «Boleh tunjukkan mesej itu?» and do not add anything for 〜てもらえますか.',
     '日本語の「〜てもらえますか」はどの動詞にも使える一つの型です。マレー語ではお願いの気持ちが動詞の中にあります：この質問の «tunjukkan» が「見せて」にあたります。'
     '«Boleh tunjukkan mesej itu?» と言い、「〜てもらえますか」にあたる語を足さないでください。'),
    ('ms-c12-f03', '«Saya mahu ambil» ___ «. Sudah sampai?»  (collecting a parcel: the root for yourself)', [
        'A: «Saya mahu ambil bungkusan. Sudah sampai?» B: «Sudah, encik. Unit berapa?»',
        'A: «Blok B, unit 12-3.» B: «Ada dua bungkusan di pondok pengawal.»',
        'A: «Siapa penerima bungkusan ini?» B: «Penerima Encik Tanaka.»',
        'A: «Bungkusan kecil itu bukan untuk saya.» B: «Label itu koyak, tetapi nombor unit ada di sini: Blok A, unit 8-1.»',
        'A: «Saya tidak ada di rumah. Boleh ambilkan bungkusan saya?» B: «Boleh. Saya ambilkan petang ini.»',
        'A: «Bungkusan saya sudah sampai di lobi?» B: «Belum. Tolong tunggu sekejap.»'],
     "To collect something yourself, use the plain root: «Saya mahu ambil bungkusan.» (the Kata-Kata frame). The root is enough because the action is for you and "
     "nobody does it on your behalf. When the guard does it for you, the verb takes ‹-kan›: «Boleh ambilkan bungkusan saya?» This is the whole idea of the unit: the same root, "
     "with ‹-kan› when the action is for someone else or makes something happen. «Sudah sampai?» asks whether it has arrived. On the label you will read «penerima» "
     "(recipient), «nombor penjejakan» (tracking number; spoken «nombor tracking») and the block and unit: «Blok B, unit 12-3.» «Pengawal», «pemilik» and «penerima» are learned "
     "as whole words; ‹pe-› words as a family come in Stage 3.",
     "自分で受け取るときは語根のままです：«Saya mahu ambil bungkusan.»（Kata-Kata の文型）。動作が自分のためで、誰かが代わりにするわけではないので、語根で十分です。"
     "守衛さんがしてくれるときは動詞に ‹-kan› が付きます：«Boleh ambilkan bungkusan saya?» これがこのユニットの中心です：同じ語根に、他の人のための動作やそうなるようにする動作のとき "
     "‹-kan› が付きます。«Sudah sampai?» は「もう届いていますか」とたずねます。ラベルでは «penerima»（受取人）、«nombor penjejakan»（追跡番号、話し言葉は «nombor tracking»）、"
     "棟と部屋番号を読みます：«Blok B, unit 12-3.» «Pengawal»・«pemilik»・«penerima» は一語として覚えます。‹pe-› の語を仲間として習うのは第3段階です。",
     'Japanese 受け取りたいのですが and 取ってきてください both use 取る. Malay separates them: «ambil» when you do it, «ambilkan» when you ask someone to do it for you.',
     '日本語では「受け取りたいのですが」も「取ってきてください」も「取る」を使います。マレー語は分けます：自分でするなら «ambil»、誰かにしてもらうなら «ambilkan» です。'),
]

# Kata-Kata scenario lines ms-c12-s01 to s10, extended to 12 turns.
DIALOGUE = [
    ('Tanaka', 'Selamat petang. Saya mahu ambil bungkusan. Sudah sampai?'),
    ('Guard', 'Sudah, encik. Unit berapa?'),
    ('Tanaka', 'Blok B, unit 12-3.'),
    ('Guard', 'Ada dua bungkusan. Boleh tunjukkan mesej itu?'),
    ('Tanaka', 'Boleh. Nombor penjejakan ada dalam mesej ini.'),
    ('Guard', 'Terima kasih. Bungkusan besar ini untuk encik. Bungkusan kecil itu bukan untuk encik. Label ini koyak, tetapi nombor unit ada di sini: Blok A, unit 8-1.'),
    ('Tanaka', 'Oh, bukan untuk saya. Boleh tolong hantarkan bungkusan kecil itu ke unit 8-1?'),
    ('Guard', 'Pemilik unit itu belum ada di rumah. Saya simpankan bungkusan itu di pondok pengawal dulu.'),
    ('Tanaka', 'Baik. Tolong hubungi pemilik unit itu nanti. Saya bawa bungkusan besar ini ke atas.'),
    ('Guard', 'Ya, encik. Saya letakkan bungkusan kecil itu di atas meja dan pastikan pintu pondok pengawal ditutup.'),
    ('Tanaka', 'Terima kasih, encik. Saya naik dulu.'),
    ('Guard', 'Baik, encik. Selamat petang!'),
]
VARIANT = [
    ('Siti', 'Selamat pagi, encik. Saya mahu ambil bungkusan saya. Sudah sampai?'),
    ('Guard', 'Sudah, puan. Unit berapa?'),
    ('Siti', 'Blok A, unit 8-1.'),
    ('Guard', 'Penerima Puan Siti, ya? Boleh tunjukkan mesej daripada kedai itu?'),
    ('Siti', 'Boleh. Ini nombor penjejakan saya.'),
    ('Guard', 'Terima kasih. Bungkusan ini berat. Saya bawakan ke lif.'),
    ('Siti', 'Terima kasih banyak. Satu lagi: boleh simpankan bungkusan suami saya? Dia sampai petang nanti.'),
    ('Guard', 'Boleh, puan. Saya simpankan di pondok pengawal.'),
    ('Siti', 'Baik. Tolong letakkan di atas meja, bukan di lantai.'),
    ('Guard', 'Baik, puan. Selamat pagi!'),
]
LISTENING = [
    ('Mei Ling', 'Selamat petang, encik. Ada bungkusan untuk saya?'),
    ('Guard', 'Ada, cik. Unit berapa?'),
    ('Mei Ling', 'Blok C, unit 5-2.'),
    ('Guard', 'Boleh tunjukkan mesej daripada kedai itu? Nombor penjejakan ada dalam mesej.'),
    ('Mei Ling', 'Boleh. Ini mesej saya.'),
    ('Guard', 'Terima kasih. Penerima Cik Mei Ling. Ada dua kotak, satu besar dan satu kecil.'),
    ('Mei Ling', 'Kotak besar itu berat. Boleh bawakan kotak itu ke lif?'),
    ('Guard', 'Boleh, cik. Saya bawakan kotak besar itu dan saya letakkan di depan lif.'),
    ('Mei Ling', 'Terima kasih banyak. Satu lagi: tolong simpankan kotak kecil itu di pondok pengawal. Suami saya akan ambil kotak itu petang nanti.'),
    ('Guard', 'Baik, cik. Saya simpankan kotak kecil itu di sini. Tolong minta suami cik tunjukkan mesej itu juga.'),
    ('Mei Ling', 'Baik. Nombor telefon saya ada di label. Pastikan label itu tidak koyak, ya?'),
    ('Guard', 'Baik, cik. Saya pastikan. Selamat petang!'),
]

CULTURE = [
    'Most of these ‹-kan› words have an everyday partner without the suffix. In a careful or written request you hear «Tolong simpankan bungkusan ini.» In a quick chat '
    'many people say the root: «Tolong simpan bungkusan ini.» Both are correct Malaysian Malay. This course teaches the ‹-kan› form first, because it shows who the action '
    'is for, and you will understand the short form when you hear it. «Berikan» works the same way: everyday speech says «bagi».',
    'Two points of spelling matter. «letakkan» and «tunjukkan» have two k, because the root ends in k and the suffix begins with k. And «berikan» is ‹beri› + ‹-kan›, '
    'not ‹ber-› + «ikan». Japanese learners often put ‹-kan› on every verb, as if it were a polite ending. It is not: «Tolong baca emel ini» takes the root.',
    'General knowledge, not a rule and not a checked fact: in many Malaysian condominiums a guard keeps parcels at a guardhouse and may ask to see the delivery message. '
    'Arrangements differ from one building to another, so ask at your own guardhouse.',
    'A short, plain request with «Tolong» or «Boleh» is polite and clear. Address the guard as «Encik» (or «Cik»), say «Terima kasih» when you have your parcel, and expect a '
    'short, friendly answer.',
]
CULTURE_JA = [
    'この ‹-kan› の語の多くには、接尾辞のない日常の形があります。ていねいな依頼や書き言葉では «Tolong simpankan bungkusan ini.» を使い、気軽なおしゃべりでは語根だけの '
    '«Tolong simpan bungkusan ini.» と言う人が多いです。どちらも正しいマレーシアのマレー語です。このコースでは、誰のための動作かが分かるので ‹-kan› の形を先に教え、'
    '短い形は聞いて分かるようにします。«Berikan» も同じで、日常では «bagi» と言います。',
    'つづりには二つ注意があります。«letakkan» と «tunjukkan» は、語根の終わりが k で接尾辞の初めも k なので k が二つになります。また «berikan» は ‹beri› ＋ ‹-kan› で、'
    '‹ber-› ＋ «ikan» ではありません。日本人の学習者は ‹-kan› をていねいな語尾のようにどの動詞にも付けがちですが、そうではありません：«Tolong baca emel ini» は語根のままです。',
    '一般的な知識であり、規則でも確認済みの事実でもありません：マレーシアの多くのコンドミニアムでは、守衛さんが守衛所で荷物を預かり、配達のメッセージを見せるように言われることがあります。'
    '建物によって違うので、自分の建物の守衛所で聞きましょう。',
    '«Tolong» か «Boleh» を使った短くて簡単な依頼で、ていねいさは十分です。守衛さんには «Encik»（女性なら «Cik»）と呼びかけ、荷物を受け取ったら «Terima kasih» と言いましょう。短くて親しみのある返事が返ってきます。',
]

EXTRA = dict(
    slug='writing-block', type='Reading and writing', sub_type='composition', kind='writing',
    title='Writing block · Collecting a parcel',
    goal='I can write short instructions and a message about collecting a parcel at the guardhouse, in six to eight sentences with ‹-kan› requests.',
    grammar=['ms-c12-g02', 'ms-c12-g03', 'ms-c12-g05'],
    patterns=['ms-c12-f01', 'ms-c12-f02', 'ms-c12-f03'],
    model=['Fictional model: a message from a resident to the residents\' chat of a condominium, and a note for the guard (all names, blocks and units are invented):',
           '«Selamat malam semua. Ada bungkusan kecil di pondok pengawal. Label itu koyak, tetapi nombor unit ada di sini: Blok A, unit 8-1. Penerima: Puan Siti. '
           'Puan Siti, tolong ambil bungkusan itu esok pagi. Terima kasih. Tanaka, Blok B, unit 12-3»',
           '«Encik, tolong simpankan bungkusan saya di pondok pengawal. Boleh bawakan kotak besar itu ke lif? Saya ambil bungkusan itu petang nanti. Terima kasih.»',
           'Notice: who the parcel is for, where it is and what to do, then the requests in the order of the day. Standard ‹-kan› forms in writing: «simpankan», «bawakan». / '
           '気づくこと：荷物が誰あてか、どこにあるか、何をすればよいかを書き、そのあとに頼みごとを順番に書きます。書くときは標準の ‹-kan› の形：«simpankan»・«bawakan»。'],
    plan=['0–5 Recall: say three requests with «Tolong …» and two with «Boleh …?» (unit 12A).',
          '5–15 Model and notice: read the model; underline every ‹-kan› verb and its root; compare «Tolong simpan bungkusan ini» (everyday) with «Tolong simpankan bungkusan ini».',
          '15–30 Guided draft: write your own message to the residents\' chat and a note for the guard with the checklist below.',
          '30–40 Peer or teacher feedback with the peer check.',
          '40–45 Rewrite one sentence and read the note aloud.',
          '0–5 復習・5–15 例文を読んで気づく・15–30 下書き・30–40 ペアまたは先生の確認・40–45 一文を書き直して音読。'],
    task=['Write six to eight sentences: a message to your residents\' chat about a parcel, and a note asking the guard to do two things. Include:',
          '☐ where the parcel is and who it is for («di pondok pengawal», «Penerima: …», «Blok …, unit …»)',
          '☐ one request to the neighbour with «Tolong …» («Tolong ambil bungkusan itu …»)',
          '☐ two requests to the guard with a ‹-kan› verb («Tolong simpankan …», «Boleh bawakan …?», «Tolong letakkan …»)',
          '☐ a greeting and «Terima kasih»',
          '________________________________________', '________________________________________',
          '________________________________________', '________________________________________',
          '住民グループへの荷物のお知らせと、守衛さんに二つのことを頼むメモを6〜8文で書きましょう。荷物の場所と宛先、隣人への «Tolong …»、守衛さんへの ‹-kan› の依頼二つ、あいさつと «Terima kasih» を入れます。'
          '名前・棟・部屋番号は架空でかまいません。'],
    check=['☐ Every ‹-kan› verb is spelt as on its card (two k in «letakkan» and «tunjukkan»; «berikan» is ‹beri› + ‹-kan›).',
           '☐ The thing follows the verb with no little word for it («Tolong simpankan bungkusan ini»).',
           '☐ «Blok» and «unit» come before the numbers.',
           '☐ No ‹-kan› on verbs that do not take it («Tolong ambil bungkusan itu» for yourself); the partner can answer one question about the message.',
           '☐ ‹-kan› の動詞のつづり、物が動詞のすぐあとにあること、«Blok»・«unit» ＋番号を確認し、パートナーが質問を一つします。'],
    answer='Any six to eight correct sentences that cover the checklist. Model: «Selamat malam semua. Ada bungkusan kecil di pondok pengawal. Penerima: Puan Siti, Blok A, unit 8-1. '
           'Puan Siti, tolong ambil bungkusan itu esok pagi. Encik, tolong simpankan bungkusan saya di pondok pengawal. Boleh bawakan kotak besar itu ke lif? Terima kasih.»',
    key_extra=['Mark for the task first (the parcel, the place, the recipient, one request to the neighbour and two to the guard), then for form (‹-kan› spelling, «Blok» and «unit», '
               'the thing after the verb). Accept the everyday root in a learner\'s first draft («Tolong simpan …») but ask for the ‹-kan› form once in the rewrite.',
               'Names, blocks and units are fictional. Do not ask anyone to share a real address or phone number.'],
    explain=('ユニット12Aのあとの書く練習（45分）：荷物の受け取りについて、住民グループへのお知らせと守衛さんへのメモを、‹-kan› の依頼を使って6〜8文で書きます。名前や部屋番号は架空でかまいません。',
             'The writing block after unit 12A (45 minutes): write a message to the residents\' chat and a note for the guard about a parcel in six to eight sentences with ‹-kan› requests; names and units may be invented.'),
)

CFG = dict(
    chapter=12, label='12A', unit_id='ms-c12a',
    menu_title='Chapter 12 · -kan and -i verbs', genre='Housing',
    prerequisite_units=['ms-c11b'], prereq_grammar=['ms-c11-g02', 'ms-c11-g06', 'ms-c08-g02'],
    unit_goal='Ask a guard to keep, bring, show or deliver something with a ‹-kan› request, collect a parcel, and read a parcel label.',
    core=CORE,
    recognition=[('Spoken partner of «nombor penjejakan»', RECOGNITION)],
    revision=[('The roots of the ‹-kan› verbs', REV_ROOTS), ('The parcel and the building', REV_PARCEL),
              ('Asking politely', REV_ASK), ('Time and markers', REV_TIME)],
    core_groups=[('For someone, or to make it happen', FORSOMEONE), ('The guardhouse', GUARDHOUSE), ('The parcel', PARCEL)],
    grammar_ids={'kan': 'ms-c12-g02', 'boleh': 'ms-c12-g03', 'i': 'ms-c12-g04', 'collect': 'ms-c12-g05', 'repair': 'ms-c12-g06',
                 'leak': 'ms-c12-g07', 'spelling': 'ms-c12-g08'},
    grammar=['kan', 'boleh', 'collect', 'spelling'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 24 cards ms-c12-001 to ms-c12-024 (the card ms-c12-024 «nombor tracking» is recognise only)', frame_list='ms-c12-f01, f02 and f03', frame_list_ja='f01・f02・f03',
    extra=EXTRA,
    goals={'A': 'I can ask for a favour with «Tolong» or «Boleh» and a ‹-kan› verb: «Tolong simpankan bungkusan ini.», «Boleh tunjukkan mesej itu?»',
           'B': 'I can ask and answer about a parcel at the guardhouse, and choose between the root («ambil») and the ‹-kan› form («ambilkan»).',
           'C': 'I can follow a guard\'s questions about a parcel and read a notice and a message about a parcel on a label.',
           'D': 'I can check the spelling of the ‹-kan› verbs (two k in «letakkan» and «tunjukkan») and correct a short request.',
           'E': 'I can collect a parcel in a short role-play and handle a torn label.'},
    goals_ja={'A': '«Tolong» か «Boleh» と ‹-kan› の動詞でお願いができる：«Tolong simpankan bungkusan ini.»、«Boleh tunjukkan mesej itu?»',
              'B': '守衛所の荷物についてたずね、答えられる。語根（«ambil»）と ‹-kan› の形（«ambilkan»）を使い分けられる。',
              'C': '荷物についての守衛さんの質問が分かり、荷物のラベルについての掲示とメッセージを読める。',
              'D': '‹-kan› の動詞のつづり（«letakkan»・«tunjukkan» は k が二つ）を確認し、短い依頼を直せる。',
              'E': '短いロールプレイで荷物を受け取り、ラベルが破れている場合にも対応できる。'},
    setting='A Wednesday afternoon at a fictional condominium in Kuala Lumpur: «Encik» Tanaka, Block B, unit 12-3, collects a parcel at the guardhouse. The guard keeps '
            'the small parcel that is not his. All names, blocks, units and times are fictional.',
    setting_ja='水曜日の午後、クアラルンプールの架空のコンドミニアム。田中さん（B棟12-3号室）が守衛所で荷物を受け取ります。自分のものではない小さな荷物は守衛さんが預かります。'
               '名前・棟・部屋番号・時刻はすべて架空です。',
    recall=['Without notes, from chapters 8 and 11: say two requests with «Tolong» and the plain root (for example «Tolong semak draf ini»), and two things you do with a meN- verb at the office. / '
            '第8章と第11章の復習：語根を使った «Tolong» の依頼を二つ、meN- の動詞で職場でしていることを二つ言いましょう（例：«Tolong semak draf ini»）。',
            'Recall prompt: «Tolong …» (check this draft) «Siapa yang menghantar fail itu?» «Saya mahu menyewa …»'],
    recall_key='e.g. «Tolong semak draf ini.» «Tolong buka pintu.» «Puan Aini membaca emel itu.» «Saya menghantar fail itu ke Osaka.» Then show the new step: the same roots with ‹-kan› '
               'when the favour is for someone («Tolong bukakan pintu»).',
    patterns=P, pattern_ids=['ms-c12-f01', 'ms-c12-f02', 'ms-c12-f03'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 12 frames f01, f02 and f03 (f04, f05 and f06 are unit 12B; f01 returns there).',
    pattern_keys=['Pattern 1: «Tolong» + a ‹-kan› verb + the thing. If a learner says «Tolong simpan bungkusan ini», accept it as everyday speech and model «simpankan». '
                  'Write the root and the suffix side by side on the board («hantar» + ‹-kan›) and let the class find the double k in «letakkan» and «tunjukkan».',
                  'Pattern 2: «Boleh» + a ‹-kan› verb + the thing. Check that the thing follows the verb with nothing between them. The answer «Boleh.» or '
                  '«Maaf, tidak boleh.» is enough.',
                  'Pattern 3: «ambil» (for yourself) against «ambilkan» (for someone). Check that learners do not put ‹-kan› on «Saya mahu ambil bungkusan».'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 7, 9, 11),
    drills={
        'repeat_frame': 'Frame: «Tolong» [«simpankan» / «hantarkan» / «bukakan»] [«bungkusan ini» / «pintu itu» / «fail itu»].',
        'repeat': ['«Tolong simpankan bungkusan ini.»', '«Boleh tunjukkan mesej itu?»', '«Saya mahu ambil bungkusan. Sudah sampai?»',
                   '«Tolong hantarkan bungkusan kecil itu ke unit 8-1.»', '«Saya simpankan bungkusan itu di pondok pengawal dulu.»',
                   '«Tolong letakkan kotak itu di sini.»', '«Boleh bawakan beg saya ke lif?»', '«Pemilik unit itu belum ada di rumah.»'],
        'substitute': ['«Tolong simpankan bungkusan ini.» (cue: «hantarkan», «surat»)',
                       '«Boleh tunjukkan mesej itu?» (cue: «berikan», «nombor telefon»)',
                       '«Tolong bukakan pintu itu.» (cue: «tutupkan»)',
                       '«Boleh belikan kopi?» (cue: «bawakan», «beg»)',
                       '«Saya mahu ambil bungkusan.» (cue: «surat»)',
                       '«Pemilik unit itu belum ada di rumah.» (cue: «jiran saya»)',
                       '«Tolong letakkan kotak itu di sini.» (cue: «beg», «di lobi»)',
                       '«Tolong pulangkan pen saya.» (cue: «buku»)'],
        'transform': ['Root to the ‹-kan› form, for someone: «Tolong simpan bungkusan ini.»', 'Root to the ‹-kan› form: «Tolong buka pintu itu.»',
                      'Root to the ‹-kan› form: «Tolong ambil fail itu.»', 'Back to the everyday root: «Tolong tutupkan pintu itu.»',
                      'Make it a polite question with «Boleh»: «Tunjukkan mesej itu.»', 'Not yet («belum»; change the verb): «Saya simpankan bungkusan itu.»',
                      'Add «sedang» (and change the verb): «Saya bawakan bungkusan itu ke lif.»', 'Make the question with «Siapa yang»: «Pengawal menyimpan bungkusan itu.»'],
        'question and answer': ['«Bungkusan itu untuk siapa?» (cue: «Encik» Tanaka)', '«Bungkusan kecil itu di mana?» (cue: «pondok pengawal»)',
                                '«Unit berapa?» (cue: «Blok B, unit 12-3»)', '«Label itu bagaimana?» (cue: «koyak»)',
                                'You hear: «Pengawal menyimpan bungkusan itu di pondok pengawal.» Ask the question («di mana»).',
                                'You hear: «Saya hantarkan bungkusan itu pukul tiga.» Ask the question («pukul berapa»).',
                                'You hear: «Bungkusan besar itu untuk Encik Tanaka.» Ask the question («untuk siapa»).',
                                'You hear: «Ada dua bungkusan di lobi.» Ask the question («berapa»).'],
        'question-word choice': ['«Bungkusan ini untuk ___?» → «Untuk Encik Tanaka.»', '«Boleh tunjukkan ___?» → «Mesej ini.»',
                                 '«Unit ___?» → «Unit 12-3.»', '«Pengawal menyimpan bungkusan itu di ___?» → «Di pondok pengawal.»',
                                 '«___ bungkusan itu sampai?» → «Pagi tadi.»', '«___ label ini koyak?» → «Sebab hujan.»',
                                 '«Bungkusan ___ untuk encik?» → «Yang besar.»', '«___ lama awak tunggu di lobi?» → «Lima belas minit.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. The root comes first, then ‹-kan›, then the thing; «Tolong» or «Boleh» is in front.',
                   'Cover the line and say it from the English: please keep this parcel; can you show me the message?; I would like to collect a parcel, has it arrived?; please '
                   'deliver the small parcel to unit 8-1; I will keep the parcel in the guardhouse for now; please put the box here; can you bring my bag to the lift?; the '
                   'owner of that unit is not home yet.'],
        'substitute': ['1 «Tolong hantarkan surat ini.» 2 «Boleh berikan nombor telefon itu?» 3 «Tolong tutupkan pintu itu.» 4 «Boleh bawakan beg?»',
                       '5 «Saya mahu ambil surat.» 6 «Jiran saya belum ada di rumah.» 7 «Tolong letakkan beg itu di lobi.» 8 «Tolong pulangkan buku saya.»'],
        'transform': ['1 «Tolong simpankan bungkusan ini.» 2 «Tolong bukakan pintu itu.» 3 «Tolong ambilkan fail itu.» 4 «Tolong tutup pintu itu.» '
                      '5 «Boleh tunjukkan mesej itu?»',
                      '6 «Saya belum menyimpan bungkusan itu.» 7 «Saya sedang membawa bungkusan itu ke lif.» 8 «Siapa yang menyimpan bungkusan itu?»'],
        'question and answer': ['1 «Bungkusan itu untuk Encik Tanaka.» 2 «Bungkusan kecil itu di pondok pengawal.» 3 «Blok B, unit 12-3.» 4 «Label itu koyak.»',
                                '5 «Pengawal menyimpan bungkusan itu di mana?» 6 «Pukul berapa awak menghantar bungkusan itu?» 7 «Bungkusan besar itu untuk siapa?» '
                                '8 «Berapa bungkusan di lobi?»'],
        'question-word choice': ['1 «siapa» 2 «apa» 3 «berapa» 4 «di mana» 5 «Bila» '
                                 '6 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 7 «yang mana» 8 «Berapa»'],
    },
    short_dialogues=[
        ('Boleh tunjukkan mesej itu?', 'Boleh. Ini nombor penjejakan saya.', 'at the guardhouse'),
        ('Tolong simpankan bungkusan ini.', 'Baik. Saya simpankan di pondok pengawal.', 'in the lobby'),
        ('Bungkusan ini untuk siapa?', 'Untuk Puan Siti, Blok A, unit 8-1.', 'reading a label'),
        ('Boleh bawakan beg saya ke lif?', 'Boleh. Lif di sebelah kiri.', 'at the entrance')],
    short_keys=['1 «Terima kasih. Saya ada nombor itu di sini.» 2 «Terima kasih, encik.»',
                '3 «Baik. Saya hantarkan ke unit itu.» 4 «Terima kasih banyak.»'],
    markers=dict(
        title='Markers with ‹-kan› verbs', grammar='collect',
        instructions=['Say each sentence again with the marker in brackets. After «sudah», «sedang», «belum», «akan», «baru» or «masih», or with a third-person doer, the bare ‹-kan› verb becomes the meN- verb: «simpankan» → «menyimpan», «hantarkan» → «menghantar». / '
                      'かっこ内のマーカーを付けて言い直します。«sudah»・«sedang»・«belum»・«akan»・«baru»・«masih» のあと、または三人称の動作主のときは、素の ‹-kan› の動詞が meN- の動詞になります：«simpankan» → «menyimpan»、«hantarkan» → «menghantar»。'],
        items=['«Saya simpankan bungkusan itu.» (marker: «sudah»)', '«Pengawal menghantar bungkusan itu.» (marker: «belum»)',
               '«Saya bawakan bungkusan itu ke lif.» (marker: «sedang»)', '«Saya hantarkan bungkusan itu petang ini.» (marker: «akan»)',
               '«Pengawal membuka pintu itu.» (marker: «baru»)', '«Saya tunggu bungkusan itu.» (marker: «masih»)',
               'Answer «Bungkusan itu sudah sampai?» (marker: «belum»)', '«Pengawal menyimpan bungkusan itu.» (marker: «masih»)'],
        bridge=['«sudah menyimpan» ≈ もう預かった · «belum menghantar» ≈ まだ届けていない · «sedang membawa» ≈ 持っていくところ · '
                '«akan menghantar» ≈ 届ける予定 · «baru membuka» ≈ 開けたばかり',
                'Japanese changes the verb ending (預かった / 預かっていない); Malay puts the marker in front and uses the meN- verb («menyimpan»), not «simpankan». / '
                '日本語は動詞の語尾が変わります。マレー語はマーカーを前に置き、«simpankan» ではなく meN- の動詞（«menyimpan»）を使います。'],
        key=['1 «Saya sudah menyimpan bungkusan itu.» 2 «Pengawal belum menghantar bungkusan itu.» 3 «Saya sedang membawa bungkusan itu ke lif.» '
             '4 «Saya akan menghantar bungkusan itu petang ini.»',
             '5 «Pengawal baru membuka pintu itu.» 6 «Saya masih tunggu bungkusan itu.» 7 «Belum. Bungkusan itu belum sampai.» '
             '8 «Pengawal masih menyimpan bungkusan itu.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を言い、‹-kan› の動詞を meN- の動詞（«menyimpan»・«menghantar»・«membawa»・«membuka»）に直します。',
                 'Say the chapter 4 markers and change the bare ‹-kan› verb to the meN- verb («menyimpan», «menghantar», «membawa», «membuka») after a marker.')),
    question_note='Chapter 12 adds no new question word. The ‹-kan› verbs fit every question you know: «Siapa yang menyimpan bungkusan itu?», '
                  '«Bungkusan itu untuk siapa?», «Unit berapa?», «Bila bungkusan itu sampai?», «Berapa lama awak tunggu?» / '
                  '第12章で新しい疑問語は増えません。‹-kan› の動詞は知っている疑問語すべてと使えます：'
                  '«Siapa yang menyimpan bungkusan itu?»、«Bungkusan itu untuk siapa?»、«Unit berapa?»、«Bila bungkusan itu sampai?»、'
                  '«Berapa lama awak tunggu?»',
    question_tasks=['Ask a neighbour what he is bringing to the lobby. («apa»)', 'Ask who keeps the parcels. («siapa»)',
                    'Ask where the guardhouse is. («di mana»)', 'Ask formally whether your parcel has arrived. («Adakah»)',
                    'Ask politely whether you may leave a bag here. («Bolehkah»)', 'Ask how many parcels there are. («berapa»)',
                    'Ask when the parcel arrived. («bila»)', 'Ask what time the parcel arrived. («pukul berapa»)',
                    'Ask on what day the parcel arrives. («hari apa»)', 'Ask how you collect a parcel. («bagaimana»; spoken «macam mana»)',
                    'Ask why the label is torn. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which parcel is for you. («yang mana»)', 'Ask where the guard takes the small parcel. («ke mana»)',
                    'Ask where the parcel came from. («dari mana»)', 'Ask how far the lobby is from the guardhouse. («berapa jauh»)',
                    'Ask how long you wait for the parcel. («berapa lama»)', 'Ask how many boxes are in the lobby. («berapa»)',
                    'Ask who brought the parcel. («siapa» with «oleh»)'],
    question_keys=['1 «Awak bawa apa ke lobi?» 2 «Siapa yang menyimpan bungkusan?» 3 «Pondok pengawal di mana?»',
                   '4 «Adakah bungkusan saya sudah sampai?» 5 «Bolehkah saya letakkan beg di sini?» 6 «Ada berapa bungkusan?»',
                   '7 «Bila bungkusan itu sampai?» 8 «Pukul berapa bungkusan itu sampai?» 9 «Pada hari apa bungkusan itu sampai?»',
                   '10 «Bagaimana saya ambil bungkusan?» (spoken: «Macam mana saya ambil bungkusan?») 11 «Kenapa label itu koyak?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab hujan.» / «Kerana hujan.»',
                   '12 «Bungkusan yang mana untuk saya?» 13 «Pengawal bawa bungkusan kecil itu ke mana?» 14 «Bungkusan ini datang dari mana?»',
                   '15 «Berapa jauh lobi dari pondok pengawal?» 16 «Berapa lama saya tunggu bungkusan itu?» 17 «Ada berapa kotak di lobi?»',
                   '18 «Bungkusan itu dibawa oleh siapa?»'],
    listening=LISTENING,
    listening_context='In the afternoon «Cik» Mei Ling collects two boxes at the guardhouse. / 午後、メイリンさんが守衛所で二つの箱を受け取ります。',
    listening_before=['Predict: which ‹-kan› verbs will you hear? Write three guesses (for example «simpankan», «bawakan», «tunjukkan»). / 聞こえそうな ‹-kan› の動詞を三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['What does Mei Ling ask about at the start?', 'Which block and unit does she live in?', 'What does the guard ask her to show?',
                      'Who is the recipient?', 'How many boxes are there?', 'Why does she ask the guard to bring the big box?',
                      'Where does the guard put the big box?', 'Who will collect the small box, and when?', 'What does she ask the guard to make sure of?'],
    listen_answers=['a parcel for her', 'Block C, unit 5-2', 'the message from the shop (with the tracking number)', 'Mei Ling',
                    'two: one big and one small', 'it is heavy', 'in front of the lift', 'her husband, in the evening',
                    'that the label does not tear'],
    listening_after=['Compare answers, then shadow lines 4, 8 and 9 after the teacher. / 答えを比べ、4・8・9行目をシャドーイングします。',
                     'Tell your partner what you would ask a guard to do for you in four sentences with ‹-kan› verbs. / 守衛さんに頼みたいことを、‹-kan› の動詞を使って4文でパートナーに話しましょう。'],
    test_listen=[(2, 'Block C, unit 5-2', ['blok', 'unit']),
                 (3, 'the message from the shop', ['tunjukkan', 'mesej']),
                 (5, 'two boxes: one big and one small', ['dua', 'kotak']),
                 (7, 'in front of the lift', ['bawakan', 'letakkan', 'depan']),
                 (8, 'her husband, in the evening', ['simpankan', 'suami', 'petang']),
                 (10, 'that the label does not tear', ['pastikan', 'label', 'koyak'])],
    test_listen_prompts=['Which block and unit does Mei Ling live in?', 'What does the guard ask her to show?', 'How many boxes are there?',
                         'Where does the guard put the big box?', 'Who will collect the small box, and when?', 'What does she ask the guard to make sure of?'],
    reading_title='Reading and writing · A notice and a message about a parcel',
    reading=['Fictional notice at the guardhouse and message in the residents\' chat (all names, blocks and units are invented):',
             '«PERHATIAN: Pengawal menyimpan bungkusan di pondok pengawal. Sila tunjukkan mesej dan nombor penjejakan.»',
             '«Selamat malam semua. Ada bungkusan kecil di pondok pengawal. Label itu koyak, tetapi nombor unit ada di sini: Blok A, unit 8-1. Penerima: Puan Siti. '
             'Puan Siti, tolong ambil bungkusan itu esok pagi. Terima kasih. Tanaka, Blok B, unit 12-3»',
             'Sign in the lobby: «Sila letakkan kotak di sini.» Sign on the lift: «Pejabat pengurusan ada di tingkat satu.»'],
    read_questions=['Where does the guard keep the parcels?', 'What must you show?', 'Whose parcel is in the guardhouse?', 'What is wrong with the label?',
                    'Which block and unit are on the label?', 'When should «Puan» Siti collect the parcel?',
                    'Say in Malay: "Please keep this parcel."'],
    read_answers=['in the guardhouse', 'the message and the tracking number', '«Puan» Siti', 'it is torn', 'Block A, unit 8-1', 'tomorrow morning',
                  '«Tolong simpankan bungkusan ini.»'],
    write_instruction='Write four or five sentences asking a guard to do things for you (keep, bring, put or show), each with a ‹-kan› verb. / '
                      '守衛さんに頼みたいこと（預かる・持っていく・置く・見せる）を、‹-kan› の動詞を使って4〜5文で書きましょう。',
    write_model='«Selamat petang, encik. Tolong simpankan bungkusan saya di pondok pengawal. Boleh bawakan kotak besar itu ke lif? '
                'Tolong letakkan kotak kecil itu di lobi. Terima kasih, encik.»',
    writing_type='message',
    task_title='Task · Collect a parcel at the guardhouse',
    role_a=['Your information (fictional): you are the guard. Two parcels are in the guardhouse: a big one for Block B, unit 12-3 (recipient «Encik» Tanaka) and a small one with a torn label '
            '(the unit number is Block A, unit 8-1). The owner of unit 8-1 is not home yet.',
            'Ask B the unit, ask B to show the message and say which parcel is for B. Offer to keep the small parcel in the guardhouse.',
            'Aの情報（架空）：あなたは守衛です。守衛所にはB棟12-3号室（受取人は田中さん）の大きな荷物と、ラベルが破れた小さな荷物（部屋番号はA棟8-1）があります。8-1の所有者はまだ帰宅していません。'
            'Bに部屋番号をたずね、メッセージを見せてもらい、どちらがBの荷物か伝えます。小さな荷物は守衛所で預かると言います。'],
    role_b=['You want to collect your parcel (Block B, unit 12-3). Say what you want, give your unit, show the message and thank the guard.',
            'The small parcel is not yours: ask the guard to deliver it or keep it. Ask the guard to bring the big parcel to the lift.',
            'Bは荷物を受け取りに来ました（B棟12-3号室）。用件を言い、部屋番号を伝え、メッセージを見せ、守衛にお礼を言います。小さな荷物は自分のものではないので、'
            '守衛に届けるか預かってもらうよう頼みます。大きな荷物をエレベーターまで持っていってもらうよう頼みます。'],
    change=['Halfway, A says: «Maaf, encik. Pemilik unit 8-1 sudah ada di rumah. Boleh encik bawakan bungkusan kecil itu ke atas?» B agrees and asks A to give the parcel: «Boleh. Tolong berikan bungkusan itu.»',
            '途中でAが «Maaf, encik. Pemilik unit 8-1 sudah ada di rumah. Boleh encik bawakan bungkusan kecil itu ke atas?» と言います。Bは引き受け、«Boleh. Tolong berikan bungkusan itu.» と頼みます。'],
    success=['☐ B asks for the parcel with «Saya mahu ambil bungkusan» and shows the message.',
             '☐ B makes at least two requests with a ‹-kan› verb («Tolong …», «Boleh …?»).',
             '☐ After the change, B takes the small parcel and asks A to give it («Tolong berikan …»).'],
    task_key='«Saya mahu ambil bungkusan. Sudah sampai?» — «Sudah, encik. Unit berapa?» — «Blok B, unit 12-3.» — «Boleh tunjukkan mesej itu?» — «Boleh. Nombor penjejakan ada dalam mesej ini.» — '
             '«Bungkusan besar ini untuk encik. Bungkusan kecil itu bukan untuk encik.» — «Tolong simpankan bungkusan kecil itu di pondok pengawal.» — «Boleh bawakan bungkusan besar ini ke lif?» — '
             'Change: «Maaf, encik. Pemilik unit 8-1 sudah ada di rumah. Boleh encik bawakan bungkusan kecil itu ke atas?» — «Boleh. Tolong berikan bungkusan itu.»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 12 card notes ms-c12-001 and -002 («hantarkan», «simpankan»; the roots «hantar» and «simpan»), -008 and -011 (double k in «letakkan» and «tunjukkan»), '
                    '-010 («berikan» is ‹beri› + ‹-kan›; everyday «bagi»), -013, -017 and -019 (whole words) and -020 and -024 («nombor penjejakan» written, «nombor tracking» spoken); stage 2 plan section 3 '
                    '(‹-kan› is not a universal politeness ending). The paragraph on guardhouses is general knowledge of condominium life in Malaysia, labelled as such and not source-checked; '
                    'the note states no figure or rule.',
    culture_prompt='In Japanese, how do you ask someone to do something for you (〜てください / 〜てもらえますか)? When would you say «Tolong simpankan …» and when «Tolong simpan …»?',
    culture_explain=('マレーシアで同じお願いを ‹-kan› の形と語根だけの形で聞くこと、つづり（k が二つ、«berikan»）、日本人学習者がしがちな間違い、守衛所の一般的な習慣を読みます。',
                     'Read about hearing the same request with ‹-kan› and with the bare root, the spelling points, the usual slip of Japanese learners, and the general custom of a guardhouse.'),
    quiz_words=['L-1157', 'L-1158', 'L-1167', 'L-1164', 'L-0595', 'L-1172'],
    quiz_meanings=['send or deliver for someone', 'keep for someone', 'show', 'put, place', 'security guard', 'torn'],
    grammar_quiz=[('Write the request: please keep this parcel.', '«Tolong simpankan bungkusan ini.»', ['tolong', 'simpankan', 'bungkusan']),
                  ('Say in Malay: "Can you show me the message?"', '«Boleh tunjukkan mesej itu?»', ['boleh', 'tunjukkan', 'mesej']),
                  ('Write the ‹-kan› form of «letak» and use it in a request.', '«letakkan»: for example «Tolong letakkan beg di sini.»', ['letakkan', 'beg']),
                  ('Say in Malay: "Could you please deliver the small parcel to unit 8-1?"', '«Boleh tolong hantarkan bungkusan kecil itu ke unit 8-1?»', ['hantarkan', 'bungkusan', 'unit'])],
    test_reading=['Fictional notice at the guardhouse: «PERHATIAN: Pengawal menyimpan bungkusan di pondok pengawal. Sila tunjukkan mesej dan nombor penjejakan. '
                  'Bungkusan kecil: label koyak. Penerima: Puan Siti, Blok A, unit 8-1.»'],
    reading_quiz=[('Where does the guard keep the parcels?', 'in the guardhouse', ['pondok pengawal']),
                  ('What must you show?', 'the message and the tracking number', ['tunjukkan', 'nombor penjejakan']),
                  ('What is wrong with the label of the small parcel?', 'it is torn', ['label', 'koyak']),
                  ('Who is the recipient?', '«Puan» Siti', ['penerima'])],
    speaking_test='Ask the guard for your parcel: give your block and unit, show the message and make two requests with a ‹-kan› verb («Tolong simpankan …», «Boleh bawakan …?»).',
    speaking_key='Check: «Saya mahu ambil bungkusan» (the root, not ‹-kan›); the unit said with «Blok» and «unit»; at least two different ‹-kan› verbs spelt and said correctly '
                 '(«simpankan», «bawakan», «tunjukkan», «letakkan»). Accept the everyday root in speech if the ‹-kan› form was also used once.',
    speaking_words=['tolong', 'boleh', 'simpankan', 'bawakan', 'unit'],
    plan={'A_recall': 'chapters 8 and 11 («Tolong» + the root; meN- verbs at the office) from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first (the request and the polite question), question and answer before the rule; then the vocabulary in three groups with each root, its chapter and '
                        'what ‹-kan› adds (for someone, or to make it happen 12, the guardhouse 6, the parcel 5 and the spoken «nombor tracking»). Write the root and the suffix side by side '
                        '(«hantar» + ‹-kan›) and point out the two k in «letakkan» and «tunjukkan».',
          'B_recall': 'say one request with «Tolong» and one with «Boleh», first with the ‹-kan› form and then with the everyday root.',
          'B_drills': 'pattern table, substitution, transformation (root to ‹-kan› first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner says one thing they would ask a guard to keep, bring or show.',
          'D_review': 'cumulative question-word drill (chapters 1 to 12), then the markers drill with new cues and a spelling check of '
                      '«letakkan», «tunjukkan», «berikan», «simpankan», «bawakan».',
          'D_preview': 'unit 12B: the leak and the repair (Kata-Kata c12 cards ms-c12-025 to ms-c12-045 and frames f04, f05 and f06).',
          'E_recall': 'say three requests with a ‹-kan› verb that you could make in a building.',
          'E_listening': 'read the Kata-Kata scenario lines ms-c12-s01 to ms-c12-s10 (Tanaka and the guard: the parcel, the torn label) twice; '
                         'learners tick the ‹-kan› verbs they hear.',
          'E_roleplay': 'pairs play the same scene with their own block, unit and parcel, without the script.',
          'E_variation': 'a parcel in the wrong place: the big parcel is at the lobby and the small one is still in the guardhouse; B asks A to bring one and keep the other, '
                         'and A confirms with «Saya bawakan …» and «Saya simpankan …».'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 12 to the home-condo scenes (parcel, guardhouse, management office). '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: the writing block after 12A, then unit 12B (the leak and the repair).',
    teacher_notes=['Load: 23 core words in three groups (for someone, or to make it happen 12; the guardhouse 6; the parcel 5), one recognition word («nombor tracking»), and revision of the roots, '
                   'the parcel and the building, asking politely and the markers. Suggested order: Block A the first group with patterns 1 and 2; Block B the second group with pattern 3; '
                   'the third group in Block B or C. If the pilot shows 23 is too many, the natural cut is: «simpankan», «hantarkan», «tunjukkan», «bawakan», «ambilkan», «letakkan», '
                   '«pengawal», «pondok pengawal», «unit», «penerima» first; the rest second.',
                   'The scene lines ms-c12-s09 (and s14 and s17 in unit 12B) use «hubungi», a unit 12B core word (card ms-c12-027). Gloss it as "contact" and treat it as recognition here; '
                   'it is taught in 12B with the other ‹-i› verb.',
                   'The ‹-kan› choice (plan section 3, Sam 13 Nov 2026): ‹-kan› means to do it for someone or to make it happen («simpankan», «hantarkan», «tunjukkan», «matikan», «bersihkan»); '
                   '‹-i› means to or at a person or place (unit 12B). Show the root, its chapter and what the suffix adds in every vocabulary entry. Spelling: two k in «letakkan» and «tunjukkan» '
                   '(card ms-c12-008 and -011); «berikan» is ‹beri› + ‹-kan›, not ‹ber-› + «ikan» (card ms-c12-010). The pe- and ke-an words («pengawal», «pemilik», «penerima», «kebocoran», «kerosakan») '
                   'are whole words: their roots (‹kawal›, ‹milik›, ‹terima›) are not taught alone (cards ms-c12-013, -017, -019).',
                   'Where Japanese learners usually slip: (1) putting ‹-kan› on every verb as if it were a polite ending: «Tolong baca emel ini» takes the root, and so does «Saya mahu ambil bungkusan» '
                   '(card ms-c12-003 is for another person); (2) forgetting the double k: *letakan, *tunjukan; (3) hearing «berikan» as ‹ber-› + «ikan»; (4) a '
                   'full ‹meN-› + ‹-kan› form (*menyimpankan, *menghantarkan) is not natural and is not taught: see the ‹-kan› rule below; (5) 〜てください covering both «Tolong» + root and '
                   '«Tolong» + ‹-kan›: ask for whom the action is.',
                   'the ‹-kan› rule (Sam, 13 Nov 2026): use the bare ‹-kan› verb for a request («Tolong simpankan …», «Boleh bawakan …?») and for a first-person offer or reply («Saya hantarkan sekarang.», «Baik, saya matikan sekarang.»); in a statement with a third-person doer or with «sudah», «sedang», «belum», «akan», «baru» or «masih», use the meN- verb the course has («Pengawal menyimpan bungkusan itu.», «Pengawal menghantar bungkusan itu.», «Pengawal membuka pintu itu.», «Saya sedang membawa bungkusan itu ke lif.»); where the course has no meN- verb («letakkan», «bukakan», «matikan», «bersihkan»), rephrase: «Saya letakkan bungkusan itu di sini sekarang.», «Saya bersihkan lantai itu sekarang.» Do not teach forms such as *menyimpankan or *menghantarkan: they are not natural.',
                   'Guardhouse (general knowledge, not a rule and not source-checked; no figure): in many Malaysian condominiums the guard keeps parcels and may ask to see the delivery message. '
                   'Buildings differ, so tell learners to ask at their own guardhouse.',
                   'Standard first: teach the ‹-kan› form, accept the everyday root in speech («simpan», «hantar», «tutup», «buka»), and never mark it wrong in a speaking task. '
                   '«nombor tracking» is spoken; the written label is «nombor penjejakan» (recognition only, never in a key).',
                   'The scene follows Kata-Kata c12 (scenario lines ms-c12-s01 to s10, frames f01, f02 and f03). All names, blocks, units and times are fictional; learners may use their real building or an invented one.',
                   'Cumulative question words: chapters 1 to 12. Chapter 12 adds no new question word.'],
)

UNIT = unit_dict(CFG)
