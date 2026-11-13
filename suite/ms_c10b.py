"""Unit 10B: ber- verbs of background, states and relationships; meeting a new neighbour (Saya berasal dari ___. Saya
bekerja di ___.; Saya sudah / belum ___.; Saya bercakap / berbual dengan ___.; Saya suka / berminat untuk ___.).

20 core ledger entries, the rows the ledger places in "Ch10 (unit 10B)" (L-1107 to L-1122, and the existing rows L-0660
«jiran», L-0714 «sepupu», L-0779 «berjiran», L-0781 «berkenalan»), in three groups, and one recognition entry: L-0667
«pindah», the spoken partner of «berpindah» (ledger: "Ch10 (unit 10B, recognition)"; Kata-Kata card ms-c10-041,
recognise only). «pengalaman» is a whole word: pe-...-an is a Stage 3 family. ber- has no nasal sound changes; the unit
recycles the 10A verbs. No meN- (chapter 11), no -kan or -i (chapter 12). The scene follows Kata-Kata c10 (scenario lines
ms-c10-s10 to s19: the new neighbour Puan Siti) and goes further in class: a gathering at Siti's home, a residents' chat
message, a role-play at the lift and the writing block after the unit. Personal details are fictional; learners may use
an invented persona. Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

WHO = ['L-1110', 'L-1111', 'L-1107', 'L-1108', 'L-1109', 'L-1112', 'L-1122', 'L-0714']
NEIGHBOURS = ['L-0660', 'L-0779', 'L-0781', 'L-1113', 'L-1118', 'L-1114']
LIFE = ['L-1115', 'L-1116', 'L-1117', 'L-1119', 'L-1120', 'L-1121']
CORE = WHO + NEIGHBOURS + LIFE
RECOGNITION = ['L-0667']

# Revision: words placed in chapters 1 to 9 that the unit really uses (a test fails if one is not used).
REV_ROOTS = ['L-0062', 'L-0048', 'L-0131', 'L-0067', 'L-0079', 'L-0534', 'L-0101', 'L-0028']
REV_PEOPLE = ['L-0080', 'L-0081', 'L-0082', 'L-0407', 'L-0071', 'L-0331', 'L-0310', 'L-0006', 'L-0046', 'L-0281']
REV_TIME = ['L-0193', 'L-0194', 'L-0191', 'L-0192', 'L-0195', 'L-0168', 'L-0132', 'L-0174', 'L-0173', 'L-0374']
REV_MORE = ['L-0066', 'L-0335', 'L-0512', 'L-0403', 'L-0069', 'L-1023', 'L-0486']

EXAMPLES = {
    # Who I am
    'L-1110': '«Saya berasal dari Osaka.» (everyday: «Asal saya dari Osaka.»)',
    'L-1111': '«Anak saya bernama Yuki.» (formal or written; everyday: «Nama dia Yuki.»)',
    'L-1107': '«Anak saya berumur lapan tahun.» (formal; everyday: «Umur dia lapan tahun.»)',
    'L-1108': '«Saya sudah berkahwin.»',
    'L-1109': '«Puan Siti sudah berkeluarga.»',
    'L-1112': '«Dua orang anak saya masih bersekolah.»',
    'L-1122': '«Saya tinggal berdua dengan isteri saya.»',
    'L-0714': '«Sepupu saya tinggal di Osaka.»',
    # Neighbours and friends
    'L-0660': '«Jiran saya baik.»',
    'L-0779': '«Kami berjiran. Rumah dia di sebelah rumah saya.»',
    'L-0781': '«Saya mahu berkenalan dengan jiran baru.»',
    'L-1113': '«Kami sudah lama berkawan.»',
    'L-1118': '«Pada hari Ahad, kami berkumpul di rumah saya.»',
    'L-1114': '«Saya baru berpindah ke sini.» (spoken: «Saya baru pindah.»)',
    # Life and interests
    'L-1115': '«Saya bercuti minggu depan.»',
    'L-1116': '«Puan Siti berniaga. Dia ada kedai kek.»',
    'L-1117': '«Saya suka berbelanja di pasar.»',
    'L-1119': '«Isteri saya berminat untuk belajar masak.»',
    'L-1120': '«Di pejabat kami berpakaian kemas.»',
    'L-1121': '«Ini pengalaman pertama saya di Malaysia.»',
    # To recognise
    'L-0667': '«Saya baru pindah.» (spoken; standard: «Saya baru berpindah.»)',
    # Revision · roots and set phrases
    'L-0062': '«asal» → «berasal»: «Asal saya dari Osaka.»',
    'L-0048': '«nama» → «bernama»: «Nama saya Tanaka.»',
    'L-0131': '«umur» → «berumur»: «Umur saya tiga puluh tahun.»',
    'L-0067': '«sekolah» → «bersekolah»: «Anak saya pergi ke sekolah.»',
    'L-0079': '«keluarga» → «berkeluarga»: «Keluarga saya di Osaka.»',
    'L-0534': '«cuti» → «bercuti»: «Minggu depan saya cuti.»',
    'L-0101': '«dua» → «berdua»: «Saya ada dua orang anak.»',
    'L-0028': '«Selamat berkenalan!» (chapter 1)',
    # Revision · people and places
    'L-0080': '«Saya tinggal berdua dengan isteri saya.»',
    'L-0081': '«Anak saya masih bersekolah.»',
    'L-0082': '«Saya guru.»',
    'L-0407': '«Encik Rashid doktor.»',
    'L-0071': '«Puan sudah lama tinggal di sini?»',
    'L-0331': '«Encik Lim tinggal di tingkat lima.»',
    'L-0310': '«Rumah dia di sebelah rumah saya.»',
    'L-0006': '«Selamat datang, jiran baru!»',
    'L-0046': '«Saya mahu berkenalan dengan mereka.»',
    'L-0281': '«Kita boleh berkenalan dengan jiran lain.»',
    # Revision · time and markers
    'L-0193': '«Saya sudah berkahwin.»',
    'L-0194': '«Saya belum berkahwin.»',
    'L-0191': '«Anak saya masih bersekolah.»',
    'L-0192': '«Bulan depan kami akan bercuti.»',
    'L-0195': '«Saya baru berpindah.»',
    'L-0168': '«Kita berkumpul lagi bulan depan.»',
    'L-0132': '«Dia berumur sembilan tahun.»',
    'L-0174': '«Saya berpindah minggu lepas.»',
    'L-0173': '«Saya bercuti minggu depan.»',
    'L-0374': '«Selamat petang semua.»',
    # Revision · work, shops and interests
    'L-0066': '«Saya bekerja di sebuah syarikat Jepun.»',
    'L-0335': '«Rina bekerja di sebuah bank.»',
    'L-0512': '«Farah berniaga di pasar pagi.»',
    'L-0403': '«Puan Siti ada kedai kek.»',
    'L-0069': '«Isteri saya belajar bahasa Melayu.»',
    'L-1023': '«Dia berminat untuk belajar masak.»',
    'L-0486': '«Kami berpakaian kemas di pejabat.»',
}

ROOTS = {'L-1110': '«asal»', 'L-1111': '«nama»', 'L-1107': '«umur»', 'L-1108': '‹kahwin›', 'L-1109': '«keluarga»',
         'L-1112': '«sekolah»', 'L-1122': '«dua»', 'L-0779': '«jiran»', 'L-0781': '‹kenalan›', 'L-1113': '«kawan»',
         'L-1118': '‹kumpul›', 'L-1114': '«pindah»', 'L-1115': '«cuti»', 'L-1116': '‹niaga›', 'L-1117': '‹belanja›',
         'L-1119': '‹minat›', 'L-1120': '‹pakaian›'}
_EN = {'L-1110': 'to come from, to be from («berasal dari»)', 'L-1111': 'to be named (formal or written; everyday «Nama saya …»)',
       'L-1107': 'to be (a certain age) (formal; everyday «Umur saya …»)', 'L-1108': 'to be married; to get married («sudah berkahwin»)',
       'L-1109': 'to have a family (of one\'s own)', 'L-1112': 'to go to school, to be at school', 'L-1122': 'the two together, as a pair',
       'L-0779': 'to be neighbours («Kami berjiran.»)', 'L-0781': 'to get to know someone («berkenalan dengan»)',
       'L-1113': 'to be friends («Kami berkawan.»)', 'L-1118': 'to gather, to get together', 'L-1114': 'to move (home) (standard; spoken «pindah»)',
       'L-1115': 'to be on leave or on holiday', 'L-1116': 'to run a business, to trade',
       'L-1117': 'to shop, to spend money (not ‹belanja› alone, which is "treat someone": chapter 17)',
       'L-1119': 'to be interested («berminat untuk» + a verb)', 'L-1120': 'to be dressed («berpakaian kemas» = neatly dressed)'}
_JA = {'L-1110': '〜の出身である（«berasal dari»）', 'L-1111': '〜という名前である（改まった言い方・書き言葉；日常は «Nama saya …»）',
       'L-1107': '〜歳である（改まった言い方；日常は «Umur saya …»）', 'L-1108': '結婚している・結婚する（«sudah berkahwin»）',
       'L-1109': '家庭を持つ', 'L-1112': '学校に通う', 'L-1122': '二人で・二人一緒に', 'L-0779': '隣同士である（«Kami berjiran.»）',
       'L-0781': '知り合いになる（«berkenalan dengan»）', 'L-1113': '友達である（«Kami berkawan.»）', 'L-1118': '集まる',
       'L-1114': '引っ越す（標準；話し言葉は «pindah»）', 'L-1115': '休暇をとる・休暇中である', 'L-1116': '商売をする',
       'L-1117': '買い物をする・お金を使う（‹belanja› だけだと「おごる」：第17章）', 'L-1119': '興味がある（«berminat untuk» ＋動詞）',
       'L-1120': '（〜な）服装をしている（«berpakaian kemas»＝きちんとした服装）'}
VOCAB_OPTS = {lid: {'en': f'{_EN[lid]} (‹ber-› + {ROOTS[lid]})', 'ja': f'{_JA[lid]}（‹ber-› ＋ {ROOTS[lid]}）'} for lid in ROOTS}
VOCAB_OPTS.update({
    'L-0660': {'en': 'neighbour («jiran baru» = a new neighbour)', 'ja': '隣人・近所の人（«jiran baru»＝新しいお隣さん）'},
    'L-0714': {'en': 'cousin', 'ja': 'いとこ'},
    'L-1121': {'en': 'experience («pengalaman pertama» = a first experience; learn it as a whole word: ‹pe-› … ‹-an› words come in Stage 3; root ‹alam›)',
               'ja': '経験（«pengalaman pertama»＝初めての経験；一語まるごと覚える：‹pe-› … ‹-an› の語は第3段階；語根 ‹alam›）'},
    'L-0667': {'en': 'to move (home) (spoken; standard «berpindah»): recognise it, say «berpindah»',
               'ja': '引っ越す（話し言葉；標準は «berpindah»）：聞いて分かればよい、言うときは «berpindah»'},
})

P = [
    ('ms-c10-f05', '«Saya berasal dari» ___. «Saya bekerja di» ___.', [
        'A: «Encik berasal dari mana?» B: «Saya berasal dari Osaka. Saya bekerja di Kuala Lumpur.»',
        'A: «Encik bekerja di mana?» B: «Saya bekerja di sebuah syarikat Jepun di Kuala Lumpur.»',
        'A: «Puan berasal dari Kuala Lumpur?» B: «Tidak. Saya berasal dari Ipoh.»',
        'A: «Siapa nama anak encik?» B: «Anak saya bernama Yuki. Dia berumur lapan tahun.»',
        'A: «Puan bekerja di mana?» B: «Saya berniaga. Saya ada kedai kek dekat stesen.»',
        'A: «Sepupu encik pun bekerja di Malaysia?» B: «Tidak. Sepupu saya bekerja di Tokyo.»'],
     "Background in standard Malay uses ber- verbs: «Saya berasal dari Osaka.» (I am from Osaka.) «Saya bekerja di …» (I work at …). "
     "Chapter 2 gave you the everyday forms, and they are still right in speech: «Asal saya dari Osaka», «Nama saya …», «Umur saya …». "
     "«bernama» and «berumur» are formal: you will meet them in writing, on forms and when someone introduces a third person: «Anak saya "
     "bernama Yuki. Dia berumur lapan tahun.» For yourself, «Nama saya Tanaka» is the natural spoken line. «berniaga» is to run a "
     "business; the answer to «Bekerja di mana?» can be «Saya berniaga».",
     "標準のマレー語では、背景を ber- の動詞で言います：«Saya berasal dari Osaka.»（大阪の出身です）、«Saya bekerja di …»（〜で働いています）。"
     "第2章で学んだ日常の形（«Asal saya dari Osaka»・«Nama saya …»・«Umur saya …»）も、話すときはそのまま正しい言い方です。«bernama» と «berumur» "
     "は改まった言い方で、書き言葉や書類、ほかの人を紹介するときに出てきます：«Anak saya bernama Yuki. Dia berumur lapan tahun.» 自分のことは "
     "«Nama saya Tanaka» と言うのが自然です。«berniaga» は商売をすることで、«Bekerja di mana?» に «Saya berniaga» と答えることもできます。",
     'Japanese 〜出身です and 〜で働いています give the same order: «berasal dari» + place, «bekerja di» + place. Watch the little word: '
     '出身 takes «dari» (from), work takes «di» (at). Japanese 〜という名前です sounds formal too, so «bernama» is a good match for it.',
     '日本語の「〜出身です」「〜で働いています」と語順は同じです：«berasal dari» ＋場所、«bekerja di» ＋場所。小さな語に注意：'
     '出身は «dari»（〜から）、働く場所は «di»（〜で）です。日本語の「〜という名前です」も改まった響きなので、«bernama» によく合います。'),
    ('ms-c10-f06', '«Saya sudah / belum» (ber- verb).', [
        'A: «Encik sudah berkahwin?» B: «Sudah. Saya tinggal berdua dengan isteri saya.»',
        'A: «Puan sudah berkeluarga?» B: «Sudah. Saya ada dua orang anak.»',
        'A: «Anak puan masih bersekolah?» B: «Ya. Dua orang anak saya masih bersekolah.»',
        'A: «Encik baru berpindah ke sini?» B: «Ya. Saya baru berpindah minggu lepas.»',
        'A: «Encik sudah bercuti tahun ini?» B: «Belum. Saya bercuti bulan Disember.»',
        'A: «Encik sudah berkenalan dengan jiran?» B: «Belum. Saya mahu berkenalan dengan mereka.»'],
     "Life events and states take the chapter 4 markers: «sudah berkahwin» (married), «belum berkahwin» (not married yet), «masih "
     "bersekolah» (still at school), «baru berpindah» (have just moved). To the question «Sudah berkahwin?» the usual short answers are "
     "«Sudah.» and «Belum.»; you do not have to say more. «berdua» means the two of you together: «Saya tinggal berdua dengan isteri "
     "saya.» (My wife and I live here, just the two of us.) In speech you will hear «pindah» for «berpindah»: recognise it, but say "
     "«berpindah».",
     "人生のできごとや状態には第4章のマーカーを使います：«sudah berkahwin»（結婚している）、«belum berkahwin»（まだ結婚していない）、«masih bersekolah»"
     "（まだ学校に通っている）、«baru berpindah»（引っ越してきたばかり）。«Sudah berkahwin?» への短い答えは «Sudah.»・«Belum.» がふつうで、"
     "それ以上言う必要はありません。«berdua» は二人一緒にという意味です：«Saya tinggal berdua dengan isteri saya.»（妻と二人で住んでいます）。"
     "話し言葉では «berpindah» の代わりに «pindah» も聞きます。聞いて分かればよく、言うときは «berpindah» を使います。",
     'Japanese 結婚しています is a state, and «sudah berkahwin» is the same idea: «sudah» marks that the event has happened. まだ… '
     'ていない is «belum»; do not answer «Tidak berkahwin», which sounds like a firm "I don\'t marry". 二人で is «berdua», not «dua orang».',
     '日本語の「結婚しています」は状態を表し、«sudah berkahwin» も同じ考え方です。«sudah» はできごとがすでに起きたことを表します。'
     '「まだ〜ていない」は «belum» です。«Tidak berkahwin» と答えると「結婚しない」ときっぱり言う響きになります。「二人で」は «berdua» で、«dua orang» ではありません。'),
    ('ms-c10-f04', '«Saya bercakap / berbual dengan» ___. / «Kami berjiran / berkawan.»', [
        'A: «Encik selalu berbual dengan jiran?» B: «Ya. Saya berbual dengan Puan Siti setiap petang.»',
        'A: «Encik berkawan dengan Encik Lim?» B: «Ya. Kami sudah lama berkawan.»',
        'A: «Puan Siti jiran encik?» B: «Ya, kami berjiran. Rumah dia di sebelah rumah saya.»',
        'A: «Pada hari Ahad kita berkumpul di mana?» B: «Kita berkumpul di rumah saya pukul empat.»',
        'A: «Encik bercakap bahasa Melayu dengan jiran?» B: «Ya. Saya bercakap bahasa Melayu dengan jiran saya.»',
        'A: «Encik sudah berkenalan dengan Encik Lim?» B: «Sudah. Kami berkenalan di rumah Puan Siti.»'],
     "Some ber- verbs need two people: «berkawan» (be friends), «berjiran» (be neighbours), «berkenalan» (get to know each other), "
     "«berkumpul» (gather). Put both people before the verb («Kami berkawan.», «Saya dan Puan Siti berjiran.») or one person and «dengan» "
     "the other («Saya berkenalan dengan Encik Lim.»). You know «Selamat berkenalan!» from chapter 1: it is the same verb. ‹hidup berjiran› "
     "(living as neighbours) is the ledger's phrase for good neighbourly life. «bercakap» and «berbual» come back from unit 10A.",
     "二人以上を必要とする ber- の動詞があります：«berkawan»（友達である）、«berjiran»（隣同士である）、«berkenalan»（知り合いになる）、«berkumpul»（集まる）。"
     "二人とも動詞の前に置く（«Kami berkawan.»・«Saya dan Puan Siti berjiran.»）か、一人を前に、もう一人を «dengan» のあとに置きます"
     "（«Saya berkenalan dengan Encik Lim.»）。第1章の «Selamat berkenalan!» も同じ動詞です。‹hidup berjiran›（隣同士として暮らすこと）は、"
     "台帳にある近所付き合いの言い方です。«bercakap»・«berbual» はユニット10Aから戻ってきます。",
     'Japanese says 友達です or 隣同士です with a noun; Malay uses a verb: «Kami berkawan.», «Kami berjiran.» Japanese と in 田中さんと知り合う '
     'is «dengan» in Malay, the same as 〜と話す.',
     '日本語は「友達です」「隣同士です」と名詞で言いますが、マレー語は動詞を使います：«Kami berkawan.»、«Kami berjiran.» 「田中さんと知り合う」の「と」は、'
     '「〜と話す」と同じく «dengan» です。'),
    ('ms-c10-f03', '«Saya suka» (ber- verb). / «Saya berminat untuk» (verb).', [
        'A: «Pada hujung minggu puan buat apa?» B: «Saya suka berbelanja di pasar.»',
        'A: «Isteri encik berminat untuk belajar apa?» B: «Dia berminat untuk belajar masak.»',
        'A: «Encik bercuti bila?» B: «Saya bercuti minggu depan. Saya balik ke Jepun.»',
        'A: «Puan suka berbelanja di mana?» B: «Saya suka berbelanja di pasar pagi.»',
        'A: «Di pejabat encik berpakaian bagaimana?» B: «Kami berpakaian kemas.»',
        'A: «Ini pengalaman pertama encik di Malaysia?» B: «Ya. Ini pengalaman pertama saya.»'],
     "Frame f03 from unit 10A comes back with the 10B verbs: «Saya suka berbelanja.» «berminat untuk» + a verb says what you are "
     "interested in doing: «Saya berminat untuk belajar bahasa Melayu.» «berbelanja» is to shop or spend money; ‹belanja› alone means "
     "to treat someone (chapter 17), so do not shorten it. «bercuti» is to be on leave or on holiday; «cuti» (chapter 2) is the "
     "noun. «berpakaian» is mostly heard in «berpakaian kemas» (neatly dressed). «pengalaman» (experience) is one whole word.",
     "ユニット10Aの文型 f03 が10Bの動詞で戻ってきます：«Saya suka berbelanja.» «berminat untuk» ＋動詞で、したいと興味を持っていることを言います："
     "«Saya berminat untuk belajar bahasa Melayu.» «berbelanja» は買い物をする・お金を使うことです。‹belanja› だけだと「おごる」（第17章）なので、"
     "短くしないでください。«bercuti» は休暇をとる・休暇中であることで、«cuti»（第2章）は名詞です。«berpakaian» はたいてい «berpakaian kemas»"
     "（きちんとした服装）で聞きます。«pengalaman»（経験）は一語まるごと覚えます。",
     'Japanese 休む is «berehat» (rest, unit 10A) and also 休みを取る, which is «bercuti». Ask yourself which one you mean. 〜に興味が'
     'あります with a noun is harder in Malay; at this stage use «berminat untuk» + a verb, or «suka» + a verb.',
     '日本語の「休む」は «berehat»（休憩、ユニット10A）にも「休みを取る」にもなり、後者は «bercuti» です。どちらの意味か考えましょう。'
     '「〜に興味があります」を名詞で言うのはマレー語では難しいので、この段階では «berminat untuk» ＋動詞か、«suka» ＋動詞を使います。'),
]

DIALOGUE = [
    ('Siti', 'Selamat petang. Encik jiran baru, ya?'),
    ('Tanaka', 'Ya, saya baru berpindah minggu lepas. Nama saya Tanaka. Saya berasal dari Osaka.'),
    ('Siti', 'Selamat berkenalan! Saya Siti. Encik bekerja di mana?'),
    ('Tanaka', 'Saya bekerja di sebuah syarikat Jepun di Kuala Lumpur. Puan pula?'),
    ('Siti', 'Saya berniaga. Saya ada kedai kek dekat stesen.'),
    ('Tanaka', 'Wah, bagus! Puan sudah lama tinggal di sini?'),
    ('Siti', 'Sudah sepuluh tahun. Saya sudah berkahwin. Dua orang anak saya masih bersekolah.'),
    ('Tanaka', 'Saya pula tinggal berdua dengan isteri saya.'),
    ('Siti', 'Isteri encik pun bekerja?'),
    ('Tanaka', 'Tidak. Dia belajar bahasa Melayu di kelas dekat sini.'),
    ('Siti', 'Bagus! Pada hari Ahad, kami berkumpul di rumah saya. Encik dan isteri datang, ya!'),
    ('Tanaka', 'Terima kasih! Pukul berapa?'),
    ('Siti', 'Pukul empat petang. Kita boleh berbual dan berkenalan dengan jiran lain.'),
    ('Tanaka', 'Baik, terima kasih! Nanti kita berbual lagi.'),
]
VARIANT = [
    ('Kumar', 'Selamat pagi. Cik jiran baru, ya?'),
    ('Rina', 'Ya, saya baru berpindah ke sini. Nama saya Rina. Saya berasal dari Fukuoka.'),
    ('Kumar', 'Selamat berkenalan! Saya Kumar. Cik bekerja di mana?'),
    ('Rina', 'Saya bekerja di sebuah bank di Petaling Jaya. Encik pula?'),
    ('Kumar', 'Saya guru. Saya sudah berkahwin. Anak saya berumur tujuh tahun. Dia baru bersekolah.'),
    ('Rina', 'Saya pula tinggal berdua dengan kakak saya.'),
    ('Kumar', 'Pada hari Sabtu, kami berkumpul di rumah saya. Cik datang, ya!'),
    ('Rina', 'Terima kasih! Pukul berapa?'),
    ('Kumar', 'Pukul lima petang.'),
    ('Rina', 'Baik. Nanti kita berbual lagi.'),
]
LISTENING = [
    ('Siti', 'Encik Tanaka, mari berkenalan dengan keluarga saya. Ini suami saya, Encik Rashid.'),
    ('Rashid', 'Selamat berkenalan. Saya berasal dari Johor Bahru. Saya bekerja di hospital.'),
    ('Tanaka', 'Selamat berkenalan. Encik doktor?'),
    ('Rashid', 'Ya, saya doktor. Kadang-kadang saya bekerja pada waktu malam.'),
    ('Siti', 'Ini sepupu saya, Farah. Dia berniaga di pasar pagi.'),
    ('Farah', 'Ya, saya berniaga baju di pasar. Encik Tanaka berasal dari mana?'),
    ('Tanaka', 'Saya berasal dari Osaka. Saya baru berpindah ke sini dengan isteri saya.'),
    ('Farah', 'Encik sudah lama di Malaysia?'),
    ('Tanaka', 'Belum. Ini pengalaman pertama saya di Malaysia. Baru enam bulan.'),
    ('Siti', 'Itu Encik Lim, jiran kita di tingkat lima. Kami sudah lama berjiran.'),
    ('Lim', 'Selamat petang. Saya sudah berkeluarga. Anak saya bernama Ken. Dia berumur sembilan tahun dan masih bersekolah.'),
    ('Tanaka', 'Encik suka bersenam?'),
    ('Lim', 'Suka. Pada hujung minggu saya berbasikal dengan anak saya.'),
    ('Farah', 'Wah, seronok! Kita berkumpul lagi bulan depan, ya!'),
]

CULTURE = [
    'Many Japanese professionals in Malaysia live in a condominium or a terrace house, with neighbours from several communities. The '
    'ledger\'s phrase ‹hidup berjiran› means living as good neighbours, and the Kata-Kata card gives «Kami berjiran» for "we are '
    'neighbours". A short introduction at the lift or the door is a good start: «Selamat berkenalan! Saya baru berpindah ke sini.»',
    'In chapter 9 you met the «rumah terbuka»: during a festival, families welcome friends and neighbours from other communities. '
    '«Puan» Siti\'s Sunday gathering is smaller, but it is the same spirit: «Pada hari Ahad, kami berkumpul di rumah saya. Encik datang, ya!»',
    'Standard and everyday forms again: a form or a letter says «Saya berasal dari Osaka», «Anak saya bernama Yuki» and «Dia berumur '
    'lapan tahun»; in speech people usually say «Asal saya dari Osaka», «Nama dia Yuki», «Umur dia lapan tahun». «berpindah» is standard; '
    '«pindah» is spoken. «berbelanja» is to shop; ‹belanja› alone means to treat someone (chapter 17).',
    'New neighbours may ask about your family. «Sudah.» or «Belum.» is a complete answer, and in class you may use an invented persona.',
]
CULTURE_JA = [
    'マレーシアに住む日本人の多くは、コンドミニアムやテラスハウスに住み、いろいろな民族の隣人がいます。台帳にある ‹hidup berjiran› は、よい隣人として'
    '暮らすことを表し、Kata-Kata のカードは「隣同士です」を «Kami berjiran» としています。エレベーターや玄関での短いあいさつは、よい始まりです：'
    '«Selamat berkenalan! Saya baru berpindah ke sini.»',
    '第9章で «rumah terbuka» を学びました。行事のとき、家族が別の民族の友人や隣人を迎えます。シティさんの日曜日の集まりはもっと小さなものですが、'
    '同じ気持ちから来ています：«Pada hari Ahad, kami berkumpul di rumah saya. Encik datang, ya!»',
    'ここでも標準の形と日常の形があります。書類や手紙では «Saya berasal dari Osaka»・«Anak saya bernama Yuki»・«Dia berumur lapan tahun» と書き、'
    '話すときはふつう «Asal saya dari Osaka»・«Nama dia Yuki»・«Umur dia lapan tahun» と言います。«berpindah» は標準、«pindah» は話し言葉です。'
    '«berbelanja» は買い物をすること、‹belanja› だけだと「おごる」（第17章）です。',
    '新しい隣人に家族のことをたずねられることがあります。«Sudah.» や «Belum.» だけで十分な答えで、授業では架空の人物になって答えてもかまいません。',
]

EXTRA = dict(
    slug='writing-block', type='Reading and writing', sub_type='composition', kind='writing',
    title='Writing block · My background and my week',
    goal='I can write a short personal background and my weekly routine in six to eight sentences with ber- verbs.',
    grammar=['ms-c10-g02', 'ms-c10-g03', 'ms-c10-g04', 'ms-c10-g06', 'ms-c10-g07', 'ms-c10-g08'],
    patterns=['ms-c10-f01', 'ms-c10-f03', 'ms-c10-f05', 'ms-c10-f06'],
    model=['Fictional model: a message to the residents\' chat group of a condominium (all details invented):',
           '«Selamat petang semua. Nama saya Yamada Emi. Saya berasal dari Nagoya. Saya baru berpindah ke tingkat sembilan minggu lepas. '
           'Saya tinggal berdua dengan suami saya.»',
           '«Saya bekerja di sebuah bank di Kuala Lumpur. Setiap pagi saya bertolak pukul tujuh setengah. Pada hari Rabu saya berlatih '
           'badminton selepas kerja. Pada hujung minggu saya suka berenang dan berbelanja di pasar.»',
           '«Saya berminat untuk belajar masak makanan Malaysia. Selamat berkenalan!»',
           'Notice: background first (from, home, who you live with), then the week (times and days), then one interest and a greeting. '
           'Standard ‹ber-› forms in writing: «berasal», «bekerja», «bertolak». / 気づくこと：最初に背景（出身・住まい・同居の人）、次に一週間（時刻と曜日）、'
           '最後に興味と一言のあいさつ。書くときは標準の ‹ber-› の形：«berasal»・«bekerja»・«bertolak»。'],
    plan=['0–5 Recall: say your name, where you are from and when you set off in the morning (units 10A and 10B).',
          '5–15 Model and notice: read the model; underline every ber- verb and its root; compare «Asal saya dari …» (spoken) with «Saya berasal dari …» (written).',
          '15–30 Guided draft: write your own message with the checklist below (a real or an invented persona).',
          '30–40 Peer or teacher feedback with the peer check.',
          '40–45 Rewrite one sentence and read the message aloud.',
          '0–5 復習・5–15 例文を読んで気づく・15–30 下書き・30–40 ペアまたは先生の確認・40–45 一文を書き直して音読。'],
    task=['Write six to eight sentences for your own residents\' chat or a new colleague. Include:',
          '☐ where you are from, where you live and who you live with («berasal dari», «tinggal», «berdua» or «sudah / belum berkahwin», if you wish)',
          '☐ where you work and two things from your week with times («bekerja di», «Setiap pagi saya … pukul …», «Pada hari … saya …»)',
          '☐ one interest («Saya suka …» or «Saya berminat untuk …») and a greeting («Selamat berkenalan!»)',
          '________________________________________', '________________________________________',
          '________________________________________', '________________________________________',
          '自分のコンドミニアムのグループ、または新しい同僚へのメッセージを6〜8文で書きましょう。出身・住まい・同居の人、仕事と一週間のこと二つ（時刻つき）、'
          '興味一つとあいさつを入れます。家族のことは書かなくても、架空の人物でもかまいません。'],
    check=['☐ Every ber- verb is spelt as on its card (be- in «berehat», «berenang», «bekerja»).',
           '☐ «dari» after «berasal», «di» after «bekerja» and «tinggal», «dengan» before a person.',
           '☐ Times have «pukul»; days have «pada hari».',
           '☐ No spoken form, no meN- verb; the partner can answer one question about the message.',
           '☐ ber- の動詞のつづり、«berasal dari»・«bekerja di»・«dengan» ＋人、«pukul»・«pada hari» を確認し、パートナーが質問を一つします。'],
    answer='Any six to eight correct sentences that cover the checklist. Model: «Selamat petang semua. Nama saya Yamada Emi. Saya berasal dari Nagoya. '
           'Saya baru berpindah ke tingkat sembilan minggu lepas. Saya tinggal berdua dengan suami saya. Saya bekerja di sebuah bank di Kuala Lumpur. '
           'Setiap pagi saya bertolak pukul tujuh setengah. Pada hujung minggu saya suka berenang. Selamat berkenalan!»',
    key_extra=['Mark for the task first (background, week, interest, greeting), then for form (ber- spelling, «dari» / «di» / «dengan», «pukul»). '
               'Accept the spoken forms a learner knows («Asal saya dari …») but ask for the standard form once in the rewrite.',
               'Personal details are optional: a learner may write as an invented persona. Do not ask anyone to share marital or family details.'],
    explain=('ユニット10Bのあとの書く練習（45分）：自分の背景と一週間を、ber- の動詞を使って6〜8文で書きます。架空の人物で書いてもかまいません。',
             'The writing block after unit 10B (45 minutes): write your background and your week in six to eight sentences with ber- verbs; an invented persona is fine.'),
)

CFG = dict(
    chapter=10, label='10B', unit_id='ms-c10b',
    menu_title='Chapter 10 · ber- verbs', genre='Daily routines',
    prerequisite_units=['ms-c10a'], prereq_grammar=['ms-c02-g05', 'ms-c02-g14', 'ms-c03-g03', 'ms-c04-g06'],
    unit_goal='Give and ask for background details with ber- verbs, meet a new neighbour, and accept an invitation to a gathering.',
    core=CORE,
    recognition=[('Spoken partner of «berpindah»', RECOGNITION)],
    revision=[('Roots of the ber- verbs, and «Selamat berkenalan»', REV_ROOTS), ('People and places', REV_PEOPLE),
              ('Time and markers', REV_TIME), ('Work, shops and interests', REV_MORE)],
    core_groups=[('Who I am', WHO), ('Neighbours and friends', NEIGHBOURS), ('Life and interests', LIFE)],
    grammar_ids={'routine': 'ms-c10-g02', 'start': 'ms-c10-g03', 'free': 'ms-c10-g04', 'with': 'ms-c10-g05',
                 'background': 'ms-c10-g06', 'events': 'ms-c10-g07', 'spelling': 'ms-c10-g08'},
    grammar=['background', 'events', 'with', 'free', 'spelling'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 21 cards ms-c10-021 to ms-c10-041; ms-c10-041 «pindah» is recognise only', frame_list='ms-c10-f03 to ms-c10-f06',
    frame_list_ja='f03〜f06',
    goals={'A': 'I can give two background details with ber- verbs («berasal dari», «bekerja di», «sudah / belum berkahwin»).',
           'B': 'I can exchange background questions with a new neighbour and say who I live with.',
           'C': 'I can identify neighbours from a short introduction and a residents\' message, and introduce myself in a role-play.',
           'D': 'I can check my own introduction: ber- forms, «dari» / «di» / «dengan», and the standard and everyday forms.',
           'E': 'I can introduce myself to a different neighbour and accept an invitation to a gathering.'},
    goals_ja={'A': 'ber- の動詞（«berasal dari»・«bekerja di»・«sudah / belum berkahwin»）で、自分の背景を二つ言える。',
              'B': '新しい隣人と背景についてたずね合い、誰と住んでいるかを言える。',
              'C': '短い紹介と住民へのメッセージから隣人が誰か分かり、ロールプレイで自己紹介できる。',
              'D': '自分の自己紹介を確認できる：ber- の形、«dari»・«di»・«dengan»、標準の形と日常の形。',
              'E': '別の隣人に自己紹介し、集まりへの招待を受けられる。'},
    setting='A Friday evening at a fictional condominium in Kuala Lumpur: «Encik» Tanaka has just moved in and meets his neighbour «Puan» Siti '
            'at the lift; on Sunday she invites the neighbours to her home. All names, floors, jobs and family details are fictional.',
    setting_ja='金曜の夕方、クアラルンプールの架空のコンドミニアム。引っ越してきたばかりの田中さんが、エレベーターで隣人のシティさんに会います。日曜日には、'
               'シティさんが近所の人を家に招きます。名前・階・仕事・家族のことはすべて架空です。',
    recall=['Without notes, from chapter 2 and unit 10A: introduce yourself in three lines (name, where you are from, where you work) and say when '
            'you set off in the morning. / 第2章とユニット10Aの復習：名前・出身・勤め先の3行で自己紹介し、朝何時に出発するかを言いましょう。',
            'Recall prompt: «Nama saya …» «Asal saya dari …» «Saya bekerja di …» «Setiap pagi saya bertolak pukul …»'],
    recall_key='e.g. «Nama saya Tanaka.» «Asal saya dari Osaka.» «Saya bekerja di sebuah syarikat Jepun.» «Setiap pagi saya bertolak pukul tujuh.» '
               'Then show the standard forms: «Saya berasal dari Osaka.» «Anak saya bernama …»',
    patterns=P, pattern_ids=['ms-c10-f05', 'ms-c10-f06', 'ms-c10-f04', 'ms-c10-f03'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 10 frames f05 and f06, with f04 and f03 from unit 10A returning with the 10B verbs.',
    pattern_keys=['Pattern 1: «berasal dari» and «bekerja di». Accept the chapter 2 forms in speech («Asal saya dari …», «Nama saya …»); '
                  'use «bernama» and «berumur» when introducing someone else or in writing.',
                  'Pattern 2: «sudah» / «belum» + a ber- verb. «Belum.» is the natural "not yet" for marriage; a learner never has to give '
                  'personal details. Offer the persona cards on the task page.',
                  'Pattern 3: two-person verbs. Check that both people come before the verb, or one before and one after «dengan».',
                  'Pattern 4: «suka» + ber- verb, «berminat untuk» + verb. Do not teach «berminat» + a noun at this stage (see the report).'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 6, 7, 10, 12),
    drills={
        'repeat_frame': 'Frame: «Saya berasal dari» [«Osaka» / «Ipoh» / «Fukuoka»]. «Saya bekerja di» [«sebuah syarikat Jepun» / «sebuah bank» / «hospital»].',
        'repeat': ['«Saya berasal dari Osaka.»', '«Saya bekerja di sebuah syarikat Jepun.»', '«Saya sudah berkahwin.»',
                   '«Saya tinggal berdua dengan isteri saya.»', '«Anak saya masih bersekolah.»', '«Saya baru berpindah ke sini.»',
                   '«Kami berjiran.»', '«Pada hari Ahad kami berkumpul di rumah saya.»'],
        'substitute': ['«Saya berasal dari Osaka.» (cue: «Fukuoka»)', '«Saya bekerja di sebuah syarikat Jepun.» (cue: «sebuah bank»)',
                       '«Saya tinggal berdua dengan isteri saya.» (cue: «kakak saya»)', '«Anak saya masih bersekolah.» (cue: «sepupu saya»)',
                       '«Saya baru berpindah ke sini.» (cue: «Puan Siti»)', '«Kami berjiran.» (cue: «berkawan»)',
                       '«Pada hari Ahad kami berkumpul di rumah saya.» (cue: «hari Sabtu», «rumah Encik Lim»)',
                       '«Saya suka berbelanja di pasar.» (cue: «isteri saya»)'],
        'transform': ['Everyday to standard: «Asal saya dari Osaka.»', 'Spoken to standard: «Saya baru pindah.»',
                      'Make it formal (introducing someone): «Nama anak saya Yuki.»', 'Make it formal: «Umur dia lapan tahun.»',
                      'Answer "not yet" with «belum»: «Encik sudah berkahwin?»', 'Make it a question with «Adakah»: «Puan Siti sudah berkeluarga.»',
                      'Put both people before the verb: «Saya berkawan dengan Rahman.»', 'Time cue «bulan depan» (marker «akan»): «Kami bercuti.»',
                      'Marker «baru»: «Saya berkenalan dengan Encik Lim.»', 'Make it negative: «Saya bercuti minggu ini.»'],
        'question and answer': ['«Encik berasal dari mana?» (cue: Nagoya)', '«Encik tinggal dengan siapa?» (cue: with your wife, just the two of you)',
                                '«Anak puan berumur berapa tahun?» (cue: nine)', '«Encik sudah lama tinggal di sini?» (cue: no, you have just moved)',
                                'You hear: «Saya bekerja di sebuah bank.» Ask the question («di mana»).',
                                'You hear: «Kami berkumpul pukul empat.» Ask the question.',
                                'You hear: «Anak saya bernama Ken.» Ask the question («siapa»).',
                                'You hear: «Saya bercuti bulan Disember.» Ask the question («bila»).'],
        'question-word choice': ['«Encik berasal ___?» → «Dari Osaka.»', '«Encik bekerja ___?» → «Di sebuah bank.»',
                                 '«Encik tinggal dengan ___?» → «Dengan isteri saya.»', '«Anak puan berumur ___ tahun?» → «Lapan tahun.»',
                                 '«___ kita berkumpul?» → «Hari Ahad.»', '«___ encik berpindah ke sini?» → «Sebab pejabat saya dekat.»',
                                 '«Rumah Puan Siti ___?» → «Yang di sebelah lif.»', '«Encik bercuti ___?» → «Ke Jepun.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. «berasal» takes «dari»; «bekerja» and «tinggal» take «di»; a person takes «dengan».',
                   'Cover the line and say it from the English: I am from Osaka; I work at a Japanese company; I am married; I live with my wife, '
                   'just the two of us; my child is still at school; I have just moved here; we are neighbours; on Sunday we get together at my home.'],
        'substitute': ['1 «Saya berasal dari Fukuoka.» 2 «Saya bekerja di sebuah bank.» 3 «Saya tinggal berdua dengan kakak saya.» '
                       '4 «Sepupu saya masih bersekolah.»',
                       '5 «Puan Siti baru berpindah ke sini.» 6 «Kami berkawan.» 7 «Pada hari Sabtu kami berkumpul di rumah Encik Lim.» '
                       '8 «Isteri saya suka berbelanja di pasar.»'],
        'transform': ['1 «Saya berasal dari Osaka.» 2 «Saya baru berpindah.» 3 «Anak saya bernama Yuki.» 4 «Dia berumur lapan tahun.» '
                      '5 «Belum.» (or «Saya belum berkahwin.»)',
                      '6 «Adakah Puan Siti sudah berkeluarga?» 7 «Saya dan Rahman berkawan.» (or «Kami berkawan.») '
                      '8 «Bulan depan kami akan bercuti.» 9 «Saya baru berkenalan dengan Encik Lim.» 10 «Saya tidak bercuti minggu ini.»'],
        'question and answer': ['1 «Saya berasal dari Nagoya.» 2 «Saya tinggal berdua dengan isteri saya.» 3 «Dia berumur sembilan tahun.» '
                                '4 «Belum. Saya baru berpindah ke sini.»',
                                '5 «Encik bekerja di mana?» 6 «Pukul berapa kita berkumpul?» 7 «Siapa nama anak encik?» 8 «Bila encik bercuti?»'],
        'question-word choice': ['1 «dari mana» 2 «di mana» 3 «siapa» 4 «berapa» 5 «Bila» (or «Hari apa») '
                                 '6 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 7 «yang mana» 8 «ke mana»'],
    },
    short_dialogues=[
        ('Encik jiran baru, ya?', 'Ya, saya baru berpindah ke sini.', 'at the lift'),
        ('Encik berasal dari mana?', 'Saya berasal dari Osaka.', 'at a gathering'),
        ('Puan sudah lama tinggal di sini?', 'Sudah sepuluh tahun. Kami sudah lama berjiran.', 'at the door'),
        ('Pada hari Ahad, kami berkumpul di rumah saya.', 'Terima kasih! Pukul berapa?', 'an invitation'),
        ('Di pejabat encik berpakaian bagaimana?', 'Kami berpakaian kemas.', 'talking about work')],
    short_keys=['1 «Selamat berkenalan! Saya Siti.» 2 «Wah! Encik bekerja di mana?» (or «Selamat berkenalan.»)',
                '3 «Bagus! Nanti kita berbual lagi.» 4 «Pukul empat petang. Datang, ya!» 5 «Pada hujung minggu pula?» (or «Di kedai saya pun sama.»)'],
    markers=dict(
        title='Markers with ber- verbs: life events', grammar='events',
        instructions=['Say each sentence again with the marker or time cue in brackets. The ber- verb never changes; only the marker does. / '
                      'かっこ内のマーカーか時の言葉を付けて言い直します。ber- の動詞は変わらず、前に付く語だけが変わります。'],
        items=['«Saya berpindah ke sini.» (marker: «baru»)', '«Anak saya bersekolah.» (marker: «masih»)', '«Puan Siti berkahwin.» (marker: «sudah»)',
               '«Kami bercuti ke Jepun.» (time cue: «bulan depan», marker: «akan»)', '«Saya berkenalan dengan jiran baru.» (marker: «belum»)',
               '«Farah berniaga di pasar.» (marker: «masih»)', 'Answer «Sudah berkahwin?» (marker: «belum»)',
               '«Mereka berkumpul di rumah Puan Siti.» (time cue: «sekarang», marker: «sedang»)'],
        bridge=['«baru berpindah» ≈ 引っ越してきたばかり · «masih bersekolah» ≈ まだ学校に通っている · «sudah berkahwin» ≈ 結婚している · '
                '«belum berkahwin» ≈ まだ結婚していない',
                'Japanese uses ている for a state (結婚している); Malay uses «sudah» for an event that has happened, and the verb stays the same. / '
                '日本語は状態を「ている」で表しますが、マレー語はできごとが起きたことを «sudah» で表し、動詞はそのままです。'],
        key=['1 «Saya baru berpindah ke sini.» 2 «Anak saya masih bersekolah.» 3 «Puan Siti sudah berkahwin.» 4 «Bulan depan kami akan bercuti ke Jepun.»',
             '5 «Saya belum berkenalan dengan jiran baru.» 6 «Farah masih berniaga di pasar.» 7 «Belum. Saya belum berkahwin.» '
             '8 «Sekarang mereka sedang berkumpul di rumah Puan Siti.»'],
        explain=('第4章のマーカーを、人生のできごとを表す ber- の動詞（«berkahwin»・«berpindah»・«bersekolah» など）と組み合わせて言います。',
                 'Combine the chapter 4 markers with the ber- verbs of life events: the verb never changes, only the marker does.')),
    question_note='Chapter 10 adds no new question word. Background questions use the ones you know: «Encik berasal dari mana?», «Encik bekerja '
                  'di mana?», «Encik tinggal dengan siapa?», «Anak encik berumur berapa tahun?», «Bila encik berpindah ke sini?» / '
                  '第10章で新しい疑問語は増えません。背景についての質問も知っている疑問語でできます：«Encik berasal dari mana?»、«Encik bekerja di mana?»、'
                  '«Encik tinggal dengan siapa?»、«Anak encik berumur berapa tahun?»、«Bila encik berpindah ke sini?»',
    question_tasks=['Greet your new neighbour and ask how they are. («apa»)', 'Ask who lives next door. («siapa»)',
                    'Ask where your neighbour works. («di mana»)', 'Ask formally whether your neighbour is married. («Adakah»)',
                    'Ask politely whether you may come on Sunday. («Bolehkah»)', 'Ask how old your neighbour\'s child is. («berapa»)',
                    'Ask when your neighbour moved here. («bila»)', 'Ask what time the gathering starts. («pukul berapa»)',
                    'Ask on what day the neighbours get together. («hari apa»)', 'Ask how the new home is. («bagaimana»; spoken «macam mana»)',
                    'Ask why your neighbour moved here. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which house is «Puan» Siti\'s. («yang mana»)', 'Ask where your neighbour is going on holiday. («ke mana»)',
                    'Ask where your neighbour is from. («dari mana»)', 'Ask how far the school is. («berapa jauh»)',
                    'Ask how long your neighbour has lived here. («berapa lama»)', 'Ask how many children your neighbour has. («berapa» with a counter)',
                    'Ask who made the cake. («siapa» with «oleh»)'],
    question_keys=['1 «Apa khabar?» 2 «Siapa tinggal di sebelah?» 3 «Encik bekerja di mana?»',
                   '4 «Adakah encik sudah berkahwin?» 5 «Bolehkah saya datang pada hari Ahad?» 6 «Anak puan berumur berapa tahun?»',
                   '7 «Bila encik berpindah ke sini?» 8 «Pukul berapa kita berkumpul?» 9 «Pada hari apa kita berkumpul?»',
                   '10 «Bagaimana rumah baru encik?» (spoken: «Macam mana rumah baru encik?») 11 «Kenapa encik berpindah ke sini?» / «Mengapa …?» / '
                   '«Apa sebab …?» «Sebab pejabat saya dekat.» / «Kerana pejabat saya dekat.»',
                   '12 «Rumah Puan Siti yang mana?» 13 «Encik bercuti ke mana?» 14 «Encik berasal dari mana?»',
                   '15 «Berapa jauh sekolah itu dari sini?» 16 «Berapa lama encik tinggal di sini?» 17 «Berapa orang anak puan?»',
                   '18 «Kek ini dibuat oleh siapa?»'],
    listening=LISTENING,
    listening_context='On Sunday afternoon «Encik» Tanaka goes to «Puan» Siti\'s gathering. She introduces her family and a neighbour. / '
                      '日曜の午後、田中さんがシティさんの集まりに行きます。シティさんが家族と隣人を紹介します。',
    listening_before=['Predict: which background words will you hear? Write three guesses (for example «berasal», «bekerja», «berumur»). / '
                      '聞こえそうな背景の言葉を三つ予想しましょう。',
                      'Draw three boxes, one for each person (Rashid, Farah, «Encik» Lim), and read the eight questions below. / '
                      '三人（ラシッドさん、ファラさん、リムさん）の欄を作り、下の8つの質問を読みます。'],
    listen_questions=['Where is «Encik» Rashid from?', 'Where does he work, and what is his job?', 'Who is Farah, and what does she do?',
                      'How long has Tanaka been in Malaysia?', 'Where does «Encik» Lim live?', 'What is the name of «Encik» Lim\'s child, and how old is the child?',
                      'What does «Encik» Lim do at the weekend?', 'When will they get together again?'],
    listen_answers=['Johor Bahru', 'at a hospital; he is a doctor', 'Siti\'s cousin; she sells clothes (runs a business) at the morning market',
                    'six months (it is his first time in Malaysia)', 'on the fifth floor', 'Ken; nine years old', 'he cycles with his child', 'next month'],
    listening_after=['Compare your boxes, then shadow lines 2, 9 and 11 after the teacher. / 欄を比べ、2・9・11行目をシャドーイングします。',
                     'Introduce one person from the listening to your partner in three sentences («Dia berasal dari …», «Dia bekerja di …»). / '
                     '聞いた中の一人を、3文でパートナーに紹介しましょう。'],
    test_listen=[(1, 'Johor Bahru', ['berasal', 'dari']),
                 (4, 'Siti\'s cousin; she runs a business at the morning market', ['sepupu', 'berniaga']),
                 (8, 'six months; it is his first time in Malaysia', ['pengalaman', 'belum']),
                 (9, 'on the fifth floor; they have been neighbours a long time', ['jiran', 'berjiran']),
                 (10, 'Ken, nine years old, still at school', ['bernama', 'berumur', 'bersekolah']),
                 (13, 'next month', ['berkumpul', 'bulan'])],
    test_listen_prompts=['Where is «Encik» Rashid from?', 'Who is Farah, and what does she do?', 'How long has Tanaka been in Malaysia?',
                         'Where does «Encik» Lim live, and what does Siti say about him?', 'Tell three things about «Encik» Lim\'s child.',
                         'When will they get together again?'],
    reading_title='Reading and writing · A welcome in the residents\' chat',
    reading=['Fictional message in the chat group of a condominium (all names, floors and times are invented):',
             '«Selamat datang, jiran baru! Encik Tanaka berasal dari Osaka.»',
             '«Dia bekerja di sebuah syarikat Jepun di Kuala Lumpur. Dia dan isteri tinggal berdua di tingkat tujuh.»',
             '«Isteri dia berminat untuk belajar masak makanan Malaysia.»',
             '«Pada hari Ahad, kita berkumpul di rumah Puan Siti, tingkat tiga, pukul empat petang. Sila datang dan berkenalan!»'],
    read_questions=['Where is «Encik» Tanaka from?', 'Where does he work?', 'Who does he live with, and on which floor?',
                    'What is his wife interested in?', 'When and where is the gathering?', 'What does the message ask the neighbours to do?',
                    'Say in Malay: "We are neighbours."'],
    read_answers=['Osaka', 'at a Japanese company in Kuala Lumpur', 'with his wife, just the two of them; on the seventh floor',
                  'learning to cook Malaysian food', 'on Sunday at 4 p.m., at «Puan» Siti\'s home on the third floor', 'to come and get to know each other',
                  '«Kami berjiran.»'],
    write_instruction='Write a short message to introduce yourself to the residents\' chat in four or five sentences, with ber- verbs. / '
                      'ber- の動詞を使って、住民のグループへの自己紹介メッセージを4〜5文で書きましょう。',
    write_model='«Selamat petang semua. Nama saya Tanaka. Saya berasal dari Osaka. Saya baru berpindah ke tingkat tujuh. '
                'Saya tinggal berdua dengan isteri saya. Selamat berkenalan!»',
    writing_type='message',
    task_title='Task · Meeting a neighbour at the lift',
    role_a=['You (or your persona) have just moved in. Persona card (fictional): from Sapporo, works at a Japanese company in Mont Kiara, lives with '
            'a cousin on the eighth floor, likes swimming.',
            'Introduce yourself, ask B two background questions, and find one thing you both like.',
            'Aは引っ越してきたばかりです（本人か架空の人物）。人物カード（架空）：札幌出身、モントキアラの日本企業で働く、8階でいとこと住んでいる、泳ぐのが好き。'
            '自己紹介をし、Bに背景について二つ質問し、二人とも好きなことを一つ見つけます。'],
    role_b=['You have lived here for ten years. Persona card (fictional): from Penang, runs a shop near the station, married, two children at '
            'school, likes cycling and swimming.',
            'Answer A, ask where A is from and who A lives with, and invite A to the neighbours\' gathering on Saturday.',
            'Bはここに10年住んでいます。人物カード（架空）：ペナン出身、駅の近くで店を営む、結婚していて子どもが二人学校に通っている、自転車と水泳が好き。'
            'Aに答え、出身と同居の人をたずね、土曜日の近所の集まりにAを招きます。'],
    change=['Halfway, B says: «Tetapi bulan depan kami akan berpindah ke Penang.» A asks why and when, and they agree to get together before then.',
            '途中でBが «Tetapi bulan depan kami akan berpindah ke Penang.» と言います。Aは理由と時期をたずね、その前に集まる約束をします。'],
    success=['☐ Both partners use at least three different ber- verbs from unit 10B.',
             '☐ A asks with «dari mana», «di mana» or «dengan siapa», and B answers with a full sentence.',
             '☐ After the change, A asks «Kenapa …?» or «Bila …?», and they agree a day and a time to get together.'],
    task_key='«Selamat petang. Saya baru berpindah ke tingkat lapan.» — «Selamat berkenalan! Encik berasal dari mana?» — «Saya berasal dari Sapporo. '
             'Saya bekerja di Mont Kiara. Puan pula?» — «Saya berniaga. Saya ada kedai dekat stesen.» — «Saya suka berenang.» — «Saya pun suka berenang!» — '
             'Change: «Tetapi bulan depan kami akan berpindah ke Penang.» — «Kenapa puan berpindah?» — «Sebab keluarga saya di Penang.» — «Pada hari Sabtu kita berkumpul, ya!»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Ledger L-0779 gloss (‹hidup berjiran› = neighbourly living) and Kata-Kata card ms-c10-028 note («Kami berjiran»); Kata-Kata '
                    'card notes ms-c10-021 («berumur» standard, «Umur saya …» everyday), -024 («Asal saya dari Osaka» = «Saya berasal dari Osaka»), '
                    '-025 («bernama» written or formal), -029 and -041 («berpindah» standard, «pindah» spoken), -032 (‹belanja› alone comes in Ch17); '
                    'open houses that welcome neighbours and friends from other communities: the chapter 9 festival note and its sources (EMGS '
                    'Connect, Arab News, Malay Mail, seen in search summaries only). That Japanese residents often live in condominiums or terrace '
                    'houses is general knowledge, no source retrieved; the note gives no figure. «Puan» Siti\'s gathering, the floors and the people are fictional.',
    culture_prompt='In Japan, do you greet a new neighbour (引っ越しのあいさつ)? What do you say, and what would you say in Malay?',
    culture_explain=('マレーシアの近所付き合い、標準の形と日常の形、新しい隣人への自己紹介について読みます。',
                     'Read about neighbours in Malaysia, standard and everyday forms, and introducing yourself to a new neighbour.'),
    quiz_words=['L-1110', 'L-1108', 'L-1114', 'L-1118', 'L-0660', 'L-1121'],
    quiz_meanings=['to come from (a place)', 'to be married', 'to move (home) (standard)', 'to gather, to get together', 'neighbour', 'experience'],
    grammar_quiz=[('Write the standard form: «Asal saya dari Osaka.»', '«Saya berasal dari Osaka.»', ['berasal', 'dari']),
                  ('Answer "not yet" to: «Encik sudah berkahwin?»', '«Belum.» (or «Saya belum berkahwin.»)', ['belum', 'berkahwin']),
                  ('Say in Malay: "I live with my wife, just the two of us."', '«Saya tinggal berdua dengan isteri saya.»', ['tinggal', 'berdua', 'isteri']),
                  ('Correct the sentence: «Saya berkenalan di Encik Lim.»', '«Saya berkenalan dengan Encik Lim.»', ['berkenalan', 'dengan'])],
    test_reading=['Fictional message: «Selamat datang, jiran baru! Cik Rina berasal dari Fukuoka. Dia bekerja di sebuah bank. Dia tinggal berdua '
                  'dengan kakak dia di tingkat sembilan. Pada hari Sabtu, kita berkumpul di rumah Encik Kumar.»'],
    reading_quiz=[('Where is «Cik» Rina from?', 'Fukuoka', ['berasal', 'dari']),
                  ('Where does she work?', 'at a bank', ['bekerja', 'bank']),
                  ('Who does she live with?', 'with her older sister, just the two of them', ['tinggal', 'berdua', 'kakak']),
                  ('What happens on Saturday?', 'the neighbours get together at «Encik» Kumar\'s home', ['berkumpul', 'rumah'])],
    speaking_test='Introduce yourself (or a persona) to a new neighbour in four sentences with ber- verbs, then answer one question about who you live with.',
    speaking_key='Check: «berasal dari» and «bekerja di» used correctly; one of «sudah / belum» + a ber- verb, «baru berpindah» or «tinggal berdua dengan»; '
                 'a full-sentence answer. Never require real family details; «Belum.» is a complete answer.',
    speaking_words=['berasal', 'bekerja', 'berpindah', 'berdua', 'berkenalan'],
    plan={'A_recall': 'chapter 2 and unit 10A (a three-line introduction and the morning routine) from the opener prompts.',
          'A_patterns': 'patterns 1 and 2, question and answer first, rule second; then the vocabulary in three groups with each root (who I am 8, '
                        'neighbours and friends 6, life and interests 6) and «pindah» as the spoken form to recognise.',
          'B_recall': 'introduce the person next to you in two sentences: «Dia berasal dari …» «Dia bekerja di …»',
          'B_drills': 'pattern table, substitution, transformation (everyday and spoken to standard first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill with life events.',
          'C_recall': 'each learner says one thing they have just done or not yet done with «baru» or «belum» + a ber- verb.',
          'D_review': 'cumulative question-word drill (chapters 1 to 10), then the markers drill and a check of «dari», «di» and «dengan».',
          'D_preview': 'the writing block (background and week), then chapter 11 (meN- verbs: Kata-Kata c11).',
          'E_recall': 'say where you are from, where you work and who you live with.',
          'E_listening': 'read the Kata-Kata scenario lines ms-c10-s10 to ms-c10-s19 (Tanaka meets «Puan» Siti) twice; learners note three facts about Siti.',
          'E_roleplay': 'pairs play the meeting at the lift without the script, with their own details or a persona card.',
          'E_variation': 'a different neighbour: B is a student who has just moved in with a cousin and is interested in learning Japanese; A '
                         'introduces A and invites B to the Sunday gathering.'},
    hanashishou_note='Hanashishou (Stage 2): the plan links unit 10B to the daily-life scene grab_ride_chat («Awak dari mana?» small talk) and the '
                     'home-condo scene new_neighbour. Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet; the '
                     'classroom role-play stands in for them.',
    next_note='Next: the writing block after unit 10B (45 minutes, below), then chapter 11.',
    teacher_notes=['Load: 20 core words in three groups (who I am 8; neighbours and friends 6; life and interests 6), one word to recognise '
                   '(«pindah», the spoken partner of «berpindah»), and revision of the roots and the chapter 2 introduction. Suggested order: '
                   'Block A who I am with patterns 1 and 2; Block B neighbours and friends with pattern 3; life and interests with pattern 4 in '
                   'Block B or C. If the pilot shows 20 is too many, the natural cut is A/B: «berasal», «berkahwin», «berpindah», «bersekolah», '
                   '«berdua», «jiran», «berjiran», «berkenalan», «berkumpul», «bercuti» first; the rest second.',
                   'ber- rule as in unit 10A: no nasal sound changes; every ber- word here is its own ledger row. «pengalaman» is a whole word '
                   '(the pe- … -an family is Stage 3); do not build other words from it. No meN- verb (chapter 11).',
                   'Common traps from the Kata-Kata cards: «berbelanja» (shop, spend) is not ‹belanja› (treat someone, chapter 17; card ms-c10-032); '
                   '«bernama» and «berumur» are formal (cards ms-c10-021 and -025): for yourself, «Nama saya …» is natural; «pindah» is spoken '
                   '(card ms-c10-041, recognise only). Unit 10A traps still apply: «berhenti kerja» = quit a job, «bertolak» = set off, not push.',
                   'Where Japanese learners usually slip: (1) *«berasal di Osaka» from 出身 + で: the origin takes «dari»; (2) «Tidak berkahwin» for '
                   'まだ結婚していない: the natural answer is «Belum.»; (3) *«dua orang» for 二人で: say «berdua»; (4) *«berkenalan di» + person: '
                   'the person takes «dengan»; (5) 休む for taking a day off: «bercuti», not «berehat»; (6) leaving out both people with '
                   '«berkawan» or «berjiran»: say «Kami berkawan» or «Saya berkawan dengan …».',
                   'Personal questions: a learner never has to give real marital or family details. Persona cards are on the task page; «Belum.» '
                   'and «Sudah.» are complete answers. «berminat» is taught with «untuk» + a verb only (the noun pattern is a question for the native reader).',
                   'The scene follows Kata-Kata c10 (scenario lines ms-c10-s10 to s19, frames f05 and f06, with f03 and f04 returning). All names, '
                   'floors, jobs and families are fictional.',
                   'Cumulative question words: chapters 1 to 10. Chapter 10 adds no new question word.'],
    extra=EXTRA,
)

UNIT = unit_dict(CFG)
