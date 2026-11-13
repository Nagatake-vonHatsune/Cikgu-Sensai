"""Unit 17: standard and spoken Malay, the particles «lah» and «kan», invitations and polite refusals: an office dinner invitation moved to Friday,
a café that is too spicy and the mamak near the office
(Sudikah encik ___?; Sayangnya saya tidak ___. Lain kali, ya?; Bagaimana kalau ___?; ___! Hari Jumaat, pukul tujuh. / Tidak mengapa. ___.; Jom makan kat ___ ni!).

24 core ledger entries, the rows the ledger places in "Ch17 (unit 17)": the existing rows L-0656 «lapang», L-0689 «ajak», L-0690 «tak tahan», L-0703 «set», L-0717 «belanja»,
L-0748 «singgah», L-0787 «malangnya» and L-0828 «sudi», and the new rows L-1252 to L-1267. They come in four groups: invitations (8), accepting and declining (6),
standard and spoken pairs (8) and the two particles «lah» and «kan» (2). No recognition word. Standard first, always: every spoken form is taught after its standard form
and labelled "spoken" («takpe», «tak apa» after «tidak mengapa»; «tak tahan» after «tidak boleh tahan»; «set» after «setuju»; «kat», «ni», «tu», «macam tu» after «di», «ini», «itu», «seperti itu»).
«lah» (joined in writing: «Takpelah.») and «kan» are for recognition: no key and no task requires them. The scene follows Kata-Kata c17 (scenario lines ms-c17-s01 to s20: the dinner
invitation, the café and the mamak) word for word, and goes further in class: a second invitation, a colleague's lunch, a written reply. All names, places and times are fictional.
Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

INVITE = ['L-1265', 'L-0689', 'L-0828', 'L-0656', 'L-0717', 'L-0748', 'L-1257', 'L-1260']
ANSWER = ['L-1255', 'L-1256', 'L-1258', 'L-1259', 'L-0787', 'L-1261']
PAIRS = ['L-1267', 'L-0690', 'L-0703', 'L-1252', 'L-1263', 'L-1264', 'L-1262', 'L-1266']
PARTICLES = ['L-1254', 'L-1253']
CORE = INVITE + ANSWER + PAIRS + PARTICLES

# Revision: words placed in chapters 1 to 16 that the unit really uses (a test fails if one is not used).
REV_SPOKEN = ['L-0030', 'L-0213', 'L-0211', 'L-0075', 'L-1081', 'L-0541', 'L-0940', 'L-0930', 'L-0215', 'L-0193']
REV_FOOD = ['L-0931', 'L-1026', 'L-0221', 'L-0250', 'L-1064', 'L-0334', 'L-0091', 'L-0198', 'L-0261']
REV_PLAN = ['L-0341', 'L-0180', 'L-0179', 'L-0178', 'L-0175', 'L-0025', 'L-0702', 'L-0532', 'L-0208', 'L-0064', 'L-0078', 'L-1009', 'L-0688']
REV_OTHER = ['L-0016', 'L-0017', 'L-0401', 'L-1175', 'L-0044', 'L-0045', 'L-0267', 'L-0535', 'L-0507', 'L-0575', 'L-0473', 'L-0476', 'L-1087', 'L-0983', 'L-0073']

EXAMPLES = {
    # invitations
    'L-1265': '«Ini jemputan makan malam.»',
    'L-0689': '«Saya ajak Encik Tanaka makan malam.»',
    'L-0828': '«Sudikah encik datang?»',
    'L-0656': '«Hari Sabtu saya tidak lapang.»',
    'L-0717': '«Bos belanja.»',
    'L-0748': '«Encik singgah di pejabat dulu, ya?»',
    'L-1257': '«Itu cadangan yang bagus.»',
    'L-1260': '«Lain kali, ya?»',
    # accepting and declining
    'L-1255': '«Bos setuju.»',
    'L-1256': '«Saya segan untuk menolak jemputan puan.»',
    'L-1258': '«Saya segan untuk menolak jemputan puan.»',
    'L-1259': '«Sayangnya hari Sabtu saya tidak lapang.»',
    'L-0787': '«Malangnya saya ada mesyuarat.»',
    'L-1261': '«Tidak mengapa. Kita cuba lain kali.»',
    # standard and spoken pairs
    'L-1267': '«Saya tidak boleh tahan pedas.»',
    'L-0690': '«Saya tak tahan pedas.»',
    'L-0703': '«Set! Hari Jumaat, pukul tujuh.»',
    'L-1252': '«Jom makan kat kafe ni!»',
    'L-1263': '«Kafe ni dekat pejabat.»',
    'L-1264': '«Kedai mamak tu dekat sahaja.»',
    'L-1262': '«Macam tu boleh?»',
    'L-1266': '«Takpe. Kita cari kedai lain.»',
    # particles
    'L-1254': '«Takpelah. Kita cari kedai lain.»',
    'L-1253': '«Cakap seperti itu pun bagus, kan?»',
    # Revision · spoken forms and chunks from Stage 1
    'L-0030': '«Saya tak nak pedas.»',
    'L-0213': '«Saya tak nak pedas.»',
    'L-0211': '«Macam mana kalau hari Jumaat?»',
    'L-0075': '«Jom makan kat kafe ni!»',
    'L-1081': '«Mari kita pergi.»',
    'L-0541': '«Ini jemputan daripada Puan Aini.»',
    'L-0940': '«Tak apa. Lain kali, ya?»',
    'L-0930': '«Macam tu boleh?»',
    'L-0215': '«Terima kasih, tapi saya tidak lapang.»',
    'L-0193': '«Saya dah makan.»',
    # Revision · food and the café
    'L-0931': '«Ada kedai mamak dekat pejabat?»',
    'L-1026': '«Jom makan kat kafe ni!»',
    'L-0221': '«Saya tidak boleh tahan pedas.»',
    'L-0250': '«Saya lapar. Jom makan!»',
    'L-1064': '«Ada nasi lemak yang tidak pedas.»',
    'L-0334': '«Kita cari kedai lain.»',
    'L-0091': '«Makanan di kafe itu pedas.»',
    'L-0198': '«Jom minum kat kafe ni!»',
    'L-0261': '«Saya minum teh.»',
    # Revision · plans, days and the office
    'L-0341': '«Bagaimana kalau hari Jumaat?»',
    'L-0180': '«Hari Sabtu saya tidak lapang.»',
    'L-0179': '«Bos setuju. Hari Jumaat, pukul tujuh.»',
    'L-0178': '«Bagaimana kalau hari Khamis?»',
    'L-0175': '«Bagaimana kalau hari Isnin?»',
    'L-0025': '«Esok saya lapang.»',
    'L-0702': '«Hujung minggu ini saya tidak lapang.»',
    'L-0532': '«Bos belanja.»',
    'L-0208': '«Malangnya saya ada mesyuarat.»',
    'L-0064': '«Encik singgah di pejabat dulu, ya?»',
    'L-0078': '«Saya ajak kawan saya makan.»',
    'L-1009': '«Kenapa encik tidak boleh datang?»',
    'L-0688': '«Sebab saya ada mesyuarat.»',
    # Revision · other
    'L-0016': '«Terima kasih atas jemputan puan.»',
    'L-0017': '«Terima kasih.» «Sama-sama.»',
    'L-0401': '«Sila hubungi Puan Aini.»',
    'L-1175': '«Sila hubungi Puan Aini.»',
    'L-0044': '«Sudikah puan makan dengan kami?»',
    'L-0045': '«Kita pergi sama-sama.»',
    'L-0267': '«Ini jemputan daripada Puan Aini.»',
    'L-0535': '«Saya tanya bos dulu.»',
    'L-0507': '«Kita cuba lain kali.»',
    'L-0575': '«Kita cari kedai lain.»',
    'L-0473': '«Tadi cik cakap takpe.»',
    'L-0476': '«Saya faham.»',
    'L-1087': '«Saya segan untuk menolak jemputan puan.»',
    'L-0983': '«Cakap seperti itu pun bagus.»',
    'L-0073': '«Saya tidak suka pedas.»',
}

VOCAB_OPTS = {
    'L-1265': {'en': 'invitation (the root «jemput», chapter 9, + ‹-an›): the thing you are invited to; written «Ini jemputan daripada Puan Aini.»',
               'ja': '招待・招待状（語根 «jemput»（第9章）＋‹-an›）；書くときは «Ini jemputan daripada Puan Aini.»'},
    'L-0689': {'en': 'to ask someone along (informal): friendlier than «jemput», less formal than «sudi»',
               'ja': '（気軽に）誘う：«jemput» よりくだけた言い方'},
    'L-1087': {'en': 'to push (on a door); the root of «menolak» (chapter 17), to decline', 'ja': '押す（ドア）；«menolak»（第17章、断る）の語根'},
    'L-0828': {'en': 'to be willing, glad to (polite): you ask the other person, never about yourself: «Sudikah encik …?»',
               'ja': '喜んで〜する（ていねい）：相手にたずねるときに使い、自分のことには使わない：«Sudikah encik …?»'},
    'L-0717': {'en': 'to treat someone, to pay for them (not «berbelanja», to spend money or shop, chapter 10): «Bos belanja.»',
               'ja': 'おごる・ごちそうする（«berbelanja»（お金を使う・買い物をする、第10章）とは別）：«Bos belanja.»'},
    'L-1257': {'en': 'suggestion (‹cadang› + ‹-an›; the root is not taught alone)',
               'ja': '提案（‹cadang›＋‹-an›；語根は単独では教えない）'},
    'L-1255': {'en': 'to agree: the standard form; the spoken partner «set» comes below; learn «setuju» as a whole word',
               'ja': '賛成する：標準形。話し言葉の «set» は下にある；«setuju» は一語として覚える'},
    'L-1256': {'en': 'to decline, to turn down (meN- + «tolak», chapter 9; the t drops): a new meaning of «tolak», "to push"',
               'ja': '断る（meN-＋«tolak»（第9章）、t が落ちる）：«tolak»（押す）の新しい意味'},
    'L-1258': {'en': 'hesitant, reluctant, shy about doing something: «Saya segan untuk …»',
               'ja': '遠慮する・気が引ける：«Saya segan untuk …»'},
    'L-1259': {'en': 'what a pity, unfortunately (‹sayang› + ‹-nya›; the root is not taught alone)',
               'ja': '残念なことに（‹sayang›＋«-nya»；語根は単独では教えない）'},
    'L-0787': {'en': 'unfortunately (‹malang› + ‹-nya›; the root is not taught alone)',
               'ja': '残念ながら・あいにく（‹malang›＋«-nya»；語根は単独では教えない）'},
    'L-1261': {'en': 'never mind, it is all right (standard); spoken: «takpe» / «tak apa», both below',
               'ja': '大丈夫・かまわない（標準形）；話し言葉は «takpe» / «tak apa»（下にある）'},
    'L-1267': {'en': 'can\'t stand, can\'t handle (the standard form), for example spicy food; not the same as «boleh tahan» (not bad, chapter 5); spoken «tak tahan»',
               'ja': '耐えられない・苦手だ（標準形）、例えば辛いもの；«boleh tahan»（悪くない、第5章）とは別の表現；話し言葉は «tak tahan»'},
    'L-0690': {'en': 'can\'t stand, can\'t handle (spoken, informal), for «tidak boleh tahan»; also spoken: «Saya tak nak pedas.», «Saya tak suka pedas.»',
               'ja': '耐えられない・苦手だ（話し言葉、くだけた言い方）、«tidak boleh tahan» の代わり；ほかに話し言葉で «Saya tak nak pedas.»・«Saya tak suka pedas.»'},
    'L-0703': {'en': '"Deal!", "Agreed!" (spoken, everyday), for the standard «setuju» above',
               'ja': '「決まり！」（日常の話し言葉）、上の標準形 «setuju» の代わり'},
    'L-1252': {'en': 'at, in (spoken), for the standard «di» (chapter 2)',
               'ja': '〜で・〜に（話し言葉）、標準形 «di»（第2章）の代わり'},
    'L-1263': {'en': 'this (spoken), for the standard «ini» (chapter 2); it stands after the noun: «kafe ni»',
               'ja': 'これ・この（話し言葉）、標準形 «ini»（第2章）の代わり；名詞のあとに置く：«kafe ni»'},
    'L-1264': {'en': 'that (spoken), for the standard «itu» (chapter 2); it stands after the noun: «kedai mamak tu»',
               'ja': 'それ・その（話し言葉）、標準形 «itu»（第2章）の代わり；名詞のあとに置く：«kedai mamak tu»'},
    'L-1262': {'en': 'like that (spoken), for the standard «seperti itu» (chapter 15)',
               'ja': 'そんなふうに（話し言葉）、標準形 «seperti itu»（第15章）の代わり'},
    'L-1266': {'en': 'never mind (spoken, a slang short form of «tak apa»), for the standard «tidak mengapa» above',
               'ja': '大丈夫（話し言葉、«tak apa» のくだけた短縮形）、上の標準形 «tidak mengapa» の代わり',
               'display': '«takpe» / «tak apa»'},
    'L-1254': {'en': 'a spoken particle that softens or stresses what is said; the meaning depends on the tone. Written joined to the word («Takpelah.», «Tidak mengapalah.»). Recognition only: you never have to say it',
               'ja': '話し言葉の助詞：語調をやわらげたり強めたりする；意味は語調による。書くときは語に続ける（«Takpelah.»・«Tidak mengapalah.»）。聞いて分かればよく、自分で言わなくてよい'},
    'L-1253': {'en': '"right?", "isn\'t it?": a spoken confirmation particle, not the suffix ‹-kan› (chapter 12). Recognition only: you never have to say it',
               'ja': '「〜でしょう？」「〜よね？」：確認の話し言葉の助詞で、接尾辞 ‹-kan›（第12章）ではない。聞いて分かればよく、自分で言わなくてよい'},
    'L-0030': {'en': 'not: standard «tidak», spoken «tak» (chapter 1); the same in the everyday answers «Saya tak nak pedas.»',
               'ja': '〜ない：標準形 «tidak»、話し言葉 «tak»（第1章）；日常の返事 «Saya tak nak pedas.» でも同じ'},
    'L-0213': {'en': 'to want: standard «mahu», spoken «nak» (chapter 5)',
               'ja': '〜したい：標準形 «mahu»、話し言葉 «nak»（第5章）'},
    'L-0075': {'en': 'let\'s (friendly, spoken tone): «Jom makan!» is for friends and colleagues; «Mari kita pergi.» is the polite form',
               'ja': '〜しよう（親しい話し言葉の調子）：«Jom makan!» は友人や同僚に；ていねいには «Mari kita pergi.»'},
    'L-1081': {'en': 'come; let\'s (the polite, standard invitation, chapter 9): «Mari kita pergi.»',
               'ja': 'さあ・〜しましょう（ていねいな標準の誘い、第9章）：«Mari kita pergi.»'},
    'L-0940': {'en': 'never mind (spoken, chapter 5): the spoken partner of «tidak mengapa»',
               'ja': '大丈夫（話し言葉、第5章）：«tidak mengapa» の話し言葉'},
    'L-0930': {'en': 'like, in the manner of (spoken, chapter 5): «macam tu» is «macam» + «tu»',
               'ja': '〜のように（話し言葉、第5章）：«macam tu» は «macam»＋«tu»'},
    'L-0215': {'en': 'but: standard «tetapi», spoken «tapi» (chapter 5)',
               'ja': 'しかし：標準形 «tetapi»、話し言葉 «tapi»（第5章）'},
    'L-0193': {'en': 'already: standard «sudah», spoken «dah» (chapter 4)',
               'ja': 'もう：標準形 «sudah»、話し言葉 «dah»（第4章）'},
    'L-0211': {'en': 'how: spoken «macam mana», standard «bagaimana» (chapter 5)',
               'ja': 'どう：話し言葉 «macam mana»、標準形 «bagaimana»（第5章）'},
}

P = [
    ('ms-c17-f01', '«Sudikah encik» ___ «?»  (a polite invitation)', [
        'A: «Ini jemputan makan malam pejabat. Sudikah encik datang?» B: «Terima kasih, Puan Aini. Pukul berapa?»',
        'A: «Sudikah puan makan dengan kami hari Jumaat?» B: «Terima kasih. Saya lapang pada hari Jumaat.»',
        'A: «Sudikah cik singgah di pejabat dulu?» B: «Boleh. Saya singgah pukul enam.»',
        'A: «Sudikah encik datang ke rumah saya hujung minggu ini?» B: «Terima kasih atas jemputan puan. Saya datang.»',
        'A: «Bos belanja. Sudikah encik datang?» B: «Siapa lagi yang datang?»',
        'A: «Saya ajak Encik Tanaka makan malam. Sudikah encik datang?» B: «Terima kasih. Saya setuju.»'],
     "«sudi» is polite: you ask the other person, never about yourself. «Sudikah encik datang?» (the Kata-Kata frame) means \"would you be willing to come?\" and is for someone senior, a client or someone you do not know well. "
     "The same invitation can be written on a card as a «jemputan». With «kami» (we, not you) the host speaks for a group: «Sudikah puan makan dengan kami?»; «kita» (we, with you) comes after the answer: «Kita pergi sama-sama.» "
     "«ajak» is friendlier: «Saya ajak encik makan malam.» A written invitation from a person is «jemputan daripada Puan Aini» («daripada» for people and offices, never «dari»).",
     "«sudi» はていねいな言い方で、相手にたずねるときに使い、自分のことには使いません。«Sudikah encik datang?»（Kata-Kata の文型）は「いらっしゃいませんか」で、目上の人・お客・あまり親しくない人に使います。"
     "同じ誘いをカードに書いたものが «jemputan» です。«kami»（相手を含まない私たち）はホストが仲間を代表して言うとき：«Sudikah puan makan dengan kami?»；«kita»（相手を含む私たち）は返事のあとで：«Kita pergi sama-sama.» "
     "«ajak» はもっとくだけた言い方：«Saya ajak encik makan malam.» 人からの書いた招待は «jemputan daripada Puan Aini»（人や事務所には «daripada»、«dari» は使わない）。",
     'Japanese いらっしゃいませんか and 来ませんか are two politeness levels in one verb. Malay shows the level with the word: «sudi» (polite), «mari» (standard), «jom» (friends), «ajak» (friendly). A learner who says «Saya sudi datang» about themselves has used it the wrong way round.',
     '日本語の「いらっしゃいませんか」と「来ませんか」は一つの動詞の中の二つの丁寧さです。マレー語は言葉でレベルを示します：«sudi»（ていねい）・«mari»（標準）・«jom»（友人）・«ajak»（親しい）。«Saya sudi datang» と自分のことに使うと、逆の使い方になります。'),
    ('ms-c17-f02', '«Sayangnya saya tidak» ___ «. Lain kali, ya?»  (declining softly, with a reason)', [
        'A: «Sudikah encik datang pada hari Sabtu?» B: «Sayangnya hari Sabtu saya tidak lapang. Lain kali, ya?»',
        'A: «Sudikah cik makan malam dengan kami?» B: «Malangnya saya ada mesyuarat. Lain kali, ya?»',
        'A: «Mari kita makan di kafe itu.» B: «Terima kasih. Sayangnya saya tidak boleh tahan pedas.»',
        'A: «Sudikah puan datang?» B: «Saya segan untuk menolak jemputan encik, tetapi saya tidak lapang.»',
        'A: «Sudikah encik datang hari Sabtu atau hari Ahad?» B: «Sayangnya saya tidak lapang hari Sabtu dan hari Ahad.»',
        'A: «Sayangnya saya tidak lapang hari ini.» B: «Tidak mengapa. Lain kali, ya?»'],
     "To decline kindly, do three things: soften the start with «Sayangnya» or «Malangnya» (a pity, unfortunately), give a reason («saya tidak lapang», «saya ada mesyuarat», «saya tidak boleh tahan pedas»), and offer another time: «Lain kali, ya?» (the Kata-Kata frame). "
     "«Saya segan untuk menolak jemputan puan.» (Kata-Kata line s04) says that you are reluctant to say no, which shows that you value the invitation. «menolak» is «tolak» (chapter 9, push) with meN-: here it means to decline. "
     "Say the reason plainly; do not leave the sentence unfinished.",
     "親切に断るには三つのことをします：«Sayangnya»・«Malangnya»（残念ながら）で始めてやわらげ、理由を言い（«saya tidak lapang»・«saya ada mesyuarat»・«saya tidak boleh tahan pedas»）、別の機会を示す：«Lain kali, ya?»（Kata-Kata の文型）。"
     "«Saya segan untuk menolak jemputan puan.»（Kata-Kata の s04）は、断りにくいと伝え、お誘いを大切に思っていることを示します。«menolak» は «tolak»（第9章、押す）に meN- が付いた形で、ここでは「断る」です。"
     "理由ははっきり言い、文を途中でやめません。",
     'Japanese ちょっと… leaves the refusal unsaid and trusts the listener to understand. Malay softens but still says it: «Sayangnya …» and a reason, then another time. A reply that is only «Susah» or silence can leave the host unsure; a clear reason and «Lain kali, ya?» is both polite and understood.',
     '日本語の「ちょっと…」は断りを言わずに相手の察しに任せます。マレー語はやわらげても断りを言います：«Sayangnya …» と理由、そのあと別の機会。«Susah» だけの返事や沈黙では主催者が分からないことがあり、はっきりした理由と «Lain kali, ya?» が、ていねいで伝わる言い方です。'),
    ('ms-c17-f03', '«Bagaimana kalau» ___ «?»  (suggesting another time or place)', [
        'A: «Hari Sabtu saya tidak lapang.» B: «Bagaimana kalau hari Jumaat?»',
        'A: «Kafe itu pedas.» B: «Bagaimana kalau kita makan di kedai lain?»',
        'A: «Kita makan pukul tujuh?» B: «Bagaimana kalau pukul lapan?»',
        'A: «Hari Jumaat saya tidak boleh datang.» B: «Bagaimana kalau hari Isnin?»',
        'A: «Bagaimana kalau kita makan di rumah saya?» B: «Itu cadangan yang bagus.»',
        'A: «Tempat itu jauh.» B: «Bagaimana kalau kita naik teksi?»'],
     "«Bagaimana kalau …?» (the Kata-Kata frame) offers an alternative: how about …? The spoken form is «Macam mana kalau …?». The suggestion is a «cadangan», and the answer can praise it: «Itu cadangan yang bagus.» "
     "After a refusal, a suggestion keeps the plan alive: «Hari Sabtu saya tidak lapang. Bagaimana kalau hari Jumaat?» The host answers either way; a suggestion is not a promise.",
     "«Bagaimana kalau …?»（Kata-Kata の文型）は代案を出す言い方で、「〜はいかがですか」です。話し言葉は «Macam mana kalau …?»。提案は «cadangan» で、答えでほめられます：«Itu cadangan yang bagus.» "
     "断ったあとに提案すると、話が続きます：«Hari Sabtu saya tidak lapang. Bagaimana kalau hari Jumaat?» 主催者はどちらの答えもでき、提案は約束ではありません。",
     'Japanese 〜はどうですか and 〜でもいいですか are close to «Bagaimana kalau …?». Malay keeps «kalau» (if) in the question, so the suggestion is "what if we …?". The same «kalau» is the condition of chapter 14.',
     '日本語の「〜はどうですか」「〜でもいいですか」が «Bagaimana kalau …?» に近い言い方です。マレー語は質問の中に «kalau»（もし）を残すので、「〜したらどうか」という提案になります。この «kalau» は第14章の条件と同じです。'),
    ('ms-c17-f04 and f05', '___ «! Hari Jumaat, pukul tujuh. / Tidak mengapa.» ___  (saying yes, and taking a no kindly)', [
        'A: «Bos setuju. Hari Jumaat, pukul tujuh.» B: «Setuju! Hari Jumaat, pukul tujuh.»',
        'A: «Kita makan di kedai mamak?» B: «Setuju! Mari kita pergi.»',
        'A: «Sayangnya saya tidak lapang hari ini.» B: «Tidak mengapa. Kita cuba lain kali.»',
        'A: «Maaf, saya tidak boleh datang.» B: «Tidak mengapa. Lain kali, ya?»',
        'A: «Hari Jumaat, pukul tujuh. Setuju?» B: «Set!»',
        'A: «Maaf, saya tidak lapang.» B: «Takpe. Kita cari hari lain.»'],
     "To say yes, say «Setuju!» (the Kata-Kata frame) and repeat the day and the time, so that both people know the plan: «Setuju! Hari Jumaat, pukul tujuh.» "
     "To take a no kindly, say «Tidak mengapa.» and add one thing: «Kita cuba lain kali.» (the Kata-Kata frame). In everyday speech with friends and colleagues, «Setuju!» becomes «Set!» and «Tidak mengapa.» becomes «Takpe.» or «Tak apa.» "
     "The standard forms are for writing and for people you do not know well; the spoken forms are for friends, colleagues and the mamak. Learn to hear both, say the one that fits, and write the standard form.",
     "賛成するときは «Setuju!»（Kata-Kata の文型）と言い、日と時刻をくり返して二人の予定を確かめます：«Setuju! Hari Jumaat, pukul tujuh.» "
     "断りを快く受けるときは «Tidak mengapa.» と言い、もう一言足します：«Kita cuba lain kali.»（Kata-Kata の文型）。友人や同僚との日常の会話では、«Setuju!» が «Set!»、«Tidak mengapa.» が «Takpe.» や «Tak apa.» になります。"
     "標準形は書くときと、あまり親しくない人に使い、話し言葉は友人・同僚・マミ屋台で使います。両方を聞き取れるようにし、場面に合う方を言い、書くときは標準形を書きます。",
     'Japanese switches between ですます and くだけた形 without changing the words much. Malay changes the words themselves: «Tidak mengapa.» and «Takpe.» are not the same register. Japanese 大丈夫です and いいよ are the nearest, but a learner should choose the Malay form by the listener, not by the Japanese.',
     '日本語は言葉をあまり変えずに「ですます」と「くだけた形」を切り替えます。マレー語は言葉そのものが変わります：«Tidak mengapa.» と «Takpe.» は同じ場面の言い方ではありません。「大丈夫です」と「いいよ」が近い訳ですが、日本語ではなく聞き手によってマレー語の形を選びます。'),
    ('ms-c17-f06', '«Jom makan kat» ___ «ni!»  (friends and colleagues, spoken)', [
        'A: «Jom makan kat kafe ni!» B: «Jom! Saya lapar.»',
        'A: «Jom makan kat kedai mamak tu!» B: «Set!»',
        'A: «Kedai mamak tu di mana?» B: «Kat depan pejabat tu. Dekat sahaja.»',
        'A: «Jom minum kat kafe ni! Saya belanja!» B: «Terima kasih! Saya minum teh. Lain kali saya belanja.»',
        'A: «Makanan kat sini pedas.» B: «Saya tak tahan pedas. Saya tak nak pedas.»',
        'A: «Macam tu boleh?» B: «Boleh. Takpe.»'],
     "This pattern is spoken Malay for friends and colleagues (the Kata-Kata frame): «jom» (let's), «kat» for the standard «di», and «ni» or «tu» after the noun for «ini» or «itu»: «kafe ni», «kedai mamak tu». "
     "The standard version is «Mari makan di kafe ini.» The spoken pairs of this chapter are: «tidak mengapa» / «takpe», «tidak boleh tahan» / «tak tahan», «setuju» / «set», «seperti itu» / «macam tu», «di» / «kat», «ini» / «ni», «itu» / «tu». "
     "«Saya belanja!» says that you pay. For a dislike, the everyday ways are «Saya tak nak pedas.» and «Saya tak suka pedas.»; «Saya tidak boleh tahan pedas.» is the standard form.",
     "この文型は友人や同僚との話し言葉です（Kata-Kata の文型）：«jom»（〜しよう）、標準形 «di» の代わりの «kat»、«ini»・«itu» の代わりに名詞のあとに置く «ni»・«tu»：«kafe ni»・«kedai mamak tu»。"
     "標準形は «Mari makan di kafe ini.» です。この章の話し言葉の組は：«tidak mengapa» / «takpe»、«tidak boleh tahan» / «tak tahan»、«setuju» / «set»、«seperti itu» / «macam tu»、«di» / «kat»、«ini» / «ni»、«itu» / «tu»。"
     "«Saya belanja!» は自分が払うという意味です。苦手なものを言う日常の言い方は «Saya tak nak pedas.»・«Saya tak suka pedas.»、標準形は «Saya tidak boleh tahan pedas.» です。",
     'Japanese friends say 行こうよ, ここで食べよう with a casual ending. Malay changes three small words: «di» to «kat», «ini» to «ni», «itu» to «tu». They are easy to hear but easy to over-use: in an email, a form or a client meeting, write «di», «ini», «itu».',
     '日本語では友人どうし「行こうよ」「ここで食べよう」とくだけた語尾にします。マレー語は三つの小さな語が変わります：«di» が «kat»、«ini» が «ni»、«itu» が «tu»。聞き取りやすい反面、使いすぎやすく、メール・書類・お客様との会議では «di»・«ini»・«itu» と書きます。'),
]

# The Kata-Kata scenario lines ms-c17-s01 to s16 (the office dinner invitation, the café, «takpe», «lah» and «kan») are the model conversation, one line to a turn.
# Sam (13 Nov 2026): turns are never joined across a scene change, so the lines are not joined: s07 and s08 are both Puan Aini (she asks the boss between them).
# The mamak scene (s17 to s20) is its own short dialogue in Block E (MAMAK, below). The inner «…» of Kata-Kata's lines s13 and s15 are shown as ‘…’.
DIALOGUE = [
    ('Aini', 'Encik Tanaka, ini jemputan makan malam pejabat. Hari Sabtu, pukul tujuh.'),
    ('Tanaka', 'Terima kasih, Puan Aini. Siapa yang belanja?'),
    ('Aini', 'Bos belanja. Sudikah encik datang?'),
    ('Tanaka', 'Sayangnya hari Sabtu saya tidak lapang. Saya segan untuk menolak jemputan puan.'),
    ('Aini', 'Tidak mengapa. Ada cadangan lain?'),
    ('Tanaka', 'Bagaimana kalau hari Jumaat?'),
    ('Aini', 'Itu cadangan yang bagus. Saya tanya bos dulu.'),
    ('Aini', 'Bos setuju. Hari Jumaat, pukul tujuh. Encik singgah di pejabat dulu, ya? Kita pergi sama-sama.'),
    ('Tanaka', 'Baik. Terima kasih!'),
    ('Mei Ling', 'Encik Tanaka, jom makan kat kafe ni! Saya belanja!'),
    ('Tanaka', 'Terima kasih. Tetapi makanan di kafe itu pedas. Saya tidak boleh tahan pedas.'),
    ('Mei Ling', 'Takpelah. Kita cari kedai lain. Macam tu boleh?'),
    ('Tanaka', 'Tadi cik cakap ‘takpe’. Itu sama dengan ‘tidak mengapa’, ya?'),
    ('Mei Ling', 'Ya! Orang selalu cakap ‘tak apa’ atau ‘takpe’.'),
    ('Tanaka', 'Dan ‘lah’ dan ‘kan’? Saya faham, tetapi saya tidak perlu cakap ‘lah’, ya?'),
    ('Mei Ling', 'Betul. Cakap seperti itu pun bagus, kan?'),
]
# Block E: the mamak (Kata-Kata s17 to s20), its own short dialogue.
MAMAK = [
    ('Tanaka', 'Ada kedai mamak dekat pejabat?'),
    ('Mei Ling', 'Ada, kedai mamak kat depan pejabat tu. Dekat sahaja.'),
    ('Tanaka', 'Setuju! Mari kita pergi.'),
    ('Mei Ling', 'Set!'),
]
# Changed facts: Puan Aini invites Mei Ling; Mei Ling has a meeting on Friday and suggests Thursday; the whole exchange stays standard.
VARIANT = [
    ('Aini', 'Cik Mei Ling, ini jemputan makan malam pejabat. Hari Jumaat, pukul tujuh.'),
    ('Mei Ling', 'Terima kasih, Puan Aini. Siapa yang belanja?'),
    ('Aini', 'Bos belanja. Sudikah cik datang?'),
    ('Mei Ling', 'Malangnya hari Jumaat saya ada mesyuarat. Saya segan untuk menolak jemputan puan.'),
    ('Aini', 'Tidak mengapa. Ada cadangan lain?'),
    ('Mei Ling', 'Bagaimana kalau hari Khamis?'),
    ('Aini', 'Itu cadangan yang bagus. Saya tanya bos dulu.'),
    ('Mei Ling', 'Terima kasih, puan. Saya tunggu.'),
    ('Aini', 'Bos setuju. Hari Khamis, pukul tujuh. Cik singgah di pejabat dulu, ya?'),
    ('Mei Ling', 'Setuju. Terima kasih, Puan Aini.'),
]
LISTENING = [
    ('Rahman', 'Mei Ling, jom makan kat kedai mamak tu! Saya belanja hari ini.'),
    ('Mei Ling', 'Wah, terima kasih! Tetapi hari ini saya tidak lapang. Saya ada mesyuarat pukul satu.'),
    ('Rahman', 'Takpe. Bagaimana kalau esok?'),
    ('Mei Ling', 'Esok boleh. Pukul berapa?'),
    ('Rahman', 'Pukul dua belas. Encik Tanaka pun mahu datang?'),
    ('Tanaka', 'Terima kasih, Encik Rahman. Tetapi makanan kat situ pedas, kan? Saya tak tahan pedas.'),
    ('Rahman', 'Ada makanan yang tidak pedas. Nasi lemak pun ada.'),
    ('Tanaka', 'Kalau macam tu, saya setuju. Esok saya lapang.'),
    ('Mei Ling', 'Set! Esok pukul dua belas. Encik Rahman belanja, ya?'),
    ('Rahman', 'Ya, esok saya belanja. Lain kali, Mei Ling belanja pula, ya?'),
    ('Mei Ling', 'Bolehlah. Lain kali saya belanja.'),
    ('Rahman', 'Kedai itu dekat sahaja. Kita jalan kaki dari pejabat.'),
    ('Mei Ling', 'Bagus! Saya suka jalan kaki.'),
    ('Tanaka', 'Pukul dua belas, saya tunggu di depan pejabat. Terima kasih, semua.'),
]

CULTURE = [
    'Malay speakers move between two registers. With friends and colleagues, and at an everyday stall, people say «takpe», «kat», «ni», «tu» and «Set!». In emails, forms, notices and meetings with clients, '
    'the standard forms are used: «tidak mengapa», «di», «ini», «itu», «setuju». A learner should understand the spoken forms, use them with friends and colleagues, and write the standard forms.',
    'Japanese ちょっと… leaves a refusal unsaid and trusts the listener to guess. Malay softens a refusal but still says it: «Sayangnya …», a reason, and then another time: «Lain kali, ya?» '
    'A reply that gives no reason can leave the host unsure; «Saya segan untuk menolak jemputan puan.» shows that you value the invitation.',
    '«lah» and «kan» are everyday particles. «lah» softens or stresses what is said, and its meaning depends on the tone; «kan» asks the listener to agree. Japanese learners often add «lah» to every sentence, which sounds odd, '
    'and neither is a copy of よ or ね. You must understand them but never need to say them: a sentence without them is correct. In writing, «lah» joins the word: «Takpelah.»',
    'General knowledge, not a rule and not a checked fact: colleagues in Malaysia often eat together at casual stalls near the office, and the person who invites often says «Saya belanja!» '
    '«belanja» means to treat someone, not to spend money (that is «berbelanja»). Accept kindly, and offer «Lain kali saya belanja.» Names and places in this course are fictional.',
]
CULTURE_JA = [
    'マレー語の話し手は二つのレジスターを使い分けます。友人や同僚と、また日常の屋台では «takpe»・«kat»・«ni»・«tu»・«Set!» と言います。メール・書類・お知らせ・お客様との会議では標準形 «tidak mengapa»・«di»・«ini»・«itu»・«setuju» を使います。'
    '学習者は、話し言葉を聞いて分かり、友人や同僚には使い、書くときは標準形を書きます。',
    '日本語の「ちょっと…」は断りを言わずに相手の察しに任せます。マレー語は断りをやわらげても、断りは言います：«Sayangnya …»、理由、そして別の機会：«Lain kali, ya?» '
    '理由のない返事では主催者が分からないことがあります。«Saya segan untuk menolak jemputan puan.» は、お誘いを大切に思っていることを示します。',
    '«lah» と «kan» は日常の助詞です。«lah» は語調をやわらげたり強めたりし、意味は語調によります。«kan» は聞き手に同意を求めます。日本人の学習者はすべての文に «lah» を付けがちで、不自然に聞こえます。'
    'どちらも「よ」や「ね」の写しではありません。聞いて分かる必要はあっても、自分で言う必要はなく、なくても文は正しいです。書くときは «lah» は語に続けます：«Takpelah.»',
    '一般的な知識であり、規則でも確認済みの事実でもありません：マレーシアの同僚は、職場の近くの気軽な屋台で一緒に食べることがよくあり、誘った人は «Saya belanja!» とよく言います。'
    '«belanja» は「おごる」で、「お金を使う」ではありません（それは «berbelanja»）。快く受け、«Lain kali saya belanja.» と返します。このコースの名前と場所はすべて架空です。',
]

CFG = dict(
    chapter=17, label='17', unit_id='ms-c17',
    menu_title='Chapter 17 · Spoken Malay and invitations', genre='Invitations',
    prerequisite_units=['ms-c16'], prereq_grammar=['ms-c16-g02', 'ms-c15-g05', 'ms-c14-g02', 'ms-c05-g04'],
    unit_goal='Understand and use the taught spoken forms with friends and colleagues («takpe», «tak tahan», «set», «kat», «ni», «tu», «macam tu») and write the standard forms, '
              'recognise «lah» and «kan», invite someone politely, accept, or decline with a reason and another time.',
    core=CORE,
    recognition=[],
    revision=[('Spoken forms and chunks from Stage 1', REV_SPOKEN), ('Food and the café', REV_FOOD), ('Plans, days and the office', REV_PLAN), ('Other words that return', REV_OTHER)],
    core_groups=[('Invitations', INVITE), ('Accepting and declining', ANSWER), ('Standard and spoken pairs', PAIRS), ('Two particles you hear', PARTICLES)],
    grammar_ids={'invite': 'ms-c17-g02', 'decline': 'ms-c17-g03', 'suggest': 'ms-c17-g04', 'pairs': 'ms-c17-g05', 'particles': 'ms-c17-g06',
                 'register': 'ms-c17-g07', 'tahan': 'ms-c17-g08', 'words': 'ms-c17-g09'},
    grammar=['invite', 'decline', 'suggest', 'pairs', 'particles', 'register'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 24 cards ms-c17-001 to ms-c17-024', frame_list='ms-c17-f01 to f06', frame_list_ja='f01〜f06',
    extra=None,
    goals={'A': 'I can invite someone politely with «Sudikah encik …?», and say yes («Setuju!») or no («Sayangnya saya tidak …») with a reason.',
           'B': 'I can suggest another time with «Bagaimana kalau …?», take a refusal kindly, and tell the standard forms from the spoken ones, such as «tidak mengapa» and its spoken partner.',
           'C': 'I can follow a lunch invitation that is moved, read a written invitation and reply to it in standard Malay, and invite a colleague and answer a refusal.',
           'D': 'I can choose the standard or the spoken form to suit the listener, tell «belanja» from «berbelanja», and recognise «lah» and «kan» without having to say them.',
           'E': 'I can play an invitation, a refusal and a new plan in two registers, with a friend and with a senior colleague, including a change of day.'},
    goals_ja={'A': '«Sudikah encik …?» でていねいに誘い、«Setuju!» で受け、«Sayangnya saya tidak …» で理由を添えて断れる。',
              'B': '«Bagaimana kalau …?» で別の機会を提案し、断りを快く受け、«tidak mengapa» とその話し言葉のように、標準形と話し言葉を区別できる。',
              'C': '日程が変わる昼食の誘いが聞き取れ、書いた招待を読んで標準語で返事を書き、同僚を誘って断りに答えられる。',
              'D': '相手に合わせて標準形か話し言葉かを選び、«belanja» と «berbelanja» を区別し、«lah» と «kan» を自分で言わなくても聞いて分かる。',
              'E': '友人と目上の同僚という二つの場面で、誘い・断り・新しい予定を演じられ、日にちの変更にも対応できる。'},
    setting='A week at an office in Kuala Lumpur: «Puan» Aini invites «Encik» Tanaka to the office dinner, he cannot come on Saturday and suggests Friday; «Cik» Mei Ling invites him to a café that is too spicy, '
            'and they choose the mamak near the office. All names, places and times are fictional.',
    setting_ja='クアラルンプールの職場の一週間。アイニさんが田中さんを職場の夕食会に誘い、田中さんは土曜日は無理なので金曜日を提案します。メイリンさんが辛すぎるカフェに誘い、'
               '二人は職場の近くのママク（屋台）に決めます。名前・場所・時刻はすべて架空です。',
    recall=['Without notes, from chapters 5, 14 and 15: say one thing you do not want with «tidak» or «tak» (chapter 1), one plan with «kalau» (chapter 14) and one «seperti itu» (chapter 15). / '
            '第5章・第14章・第15章の復習：«tidak» か «tak» で一文（第1章）、«kalau» で予定を一文（第14章）、«seperti itu» を一文（第15章）言いましょう。',
            'Recall prompt: «Saya tidak suka pedas.» «Kalau hujan, kita makan di kafe.» «Seperti itu.»'],
    recall_key='e.g. «Saya tidak mahu pedas.» «Kalau hujan, kita makan di kafe.» «Cawan seperti itu.» Then show the new step: the standard form first, then the spoken one, and the invitation «Sudikah encik …?».',
    patterns=P, pattern_ids=['ms-c17-f01', 'ms-c17-f02', 'ms-c17-f03', 'ms-c17-f04', 'ms-c17-f05', 'ms-c17-f06'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 17 frames f01 to f06 (pattern 4 shows f04 and f05 together, saying yes and taking a no kindly; the patterns run f01, f02, f03, f04 and f05, f06).',
    pattern_keys=['Pattern 1: «Sudikah encik» + a verb + «?». Check that «sudi» is used to ask the other person, and that «kami» is used for a group that does not include the listener. Accept «Jom» or «Mari» in a friendly invitation and say that «Sudikah» is for a senior person.',
                  'Pattern 2: «Sayangnya» or «Malangnya» + «saya tidak» or «saya ada» + a reason, then «Lain kali, ya?». Check that the reason is given and the sentence is finished. Accept a short «Maaf, saya tidak lapang.» as a first try.',
                  'Pattern 3: «Bagaimana kalau» + a day, a time or a place. Accept the spoken «Macam mana kalau …?» in a quick answer and ask for «Bagaimana» in the written part.',
                  'Pattern 4: «Setuju!» + the day and the time, or «Tidak mengapa.» + one more sentence. Accept the spoken «Set!», «Takpe.» and «Tak apa.» in a quick answer; ask for the standard form once in the written part. Do not ask for ‹lah› or ‹kan›.',
                  'Pattern 5: «Jom makan kat» + the place + «ni» or «tu». Say that this pattern is spoken, for friends and colleagues, and ask learners to say the standard version («Mari makan di kafe ini.») once.'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 7, 9),
    scene_e=dict(title='the mamak near the office (Kata-Kata s17 to s20)', lines=MAMAK),
    drills={
        'repeat_frame': 'Frame: «Sudikah encik» [«datang» / «singgah»] «?»',
        'repeat': ['«Sudikah encik datang?»', '«Sayangnya saya tidak lapang. Lain kali, ya?»', '«Bagaimana kalau hari Jumaat?»',
                   '«Setuju! Hari Jumaat, pukul tujuh.»', '«Tidak mengapa. Kita cuba lain kali.»', '«Jom makan kat kafe ni! Saya belanja!»',
                   '«Saya tidak boleh tahan pedas.»', '«Takpe. Kita cari kedai lain. Macam tu boleh?»'],
        'substitute': ['«Sudikah encik datang?» (cue: «puan», «singgah»)',
                       '«Sayangnya hari Sabtu saya tidak lapang.» (cue: «hari Ahad»)',
                       '«Malangnya saya ada mesyuarat.» (cue: «hari Jumaat»)',
                       '«Bagaimana kalau hari Jumaat?» (cue: «pukul lapan», «kedai lain»)',
                       '«Bos setuju.» (cue: «Puan Aini»)',
                       '«Jom makan kat kafe ni!» (cue: «minum», «kedai mamak tu»)',
                       '«Saya tidak boleh tahan pedas.» (cue: spoken «tak tahan»)',
                       '«Bos belanja.» (cue: «Mei Ling»)'],
        'transform': ['Say it in standard Malay: «Takpe.»',
                      'Say it the spoken way: «Kita makan di kafe ini.»',
                      'Say it in standard Malay: «Macam tu boleh?»',
                      'Say it the spoken way: «Saya tidak boleh tahan pedas.»',
                      'Say it in standard Malay: «Set!»',
                      'Invite a senior colleague politely: «Awak datang?»',
                      'Refuse softly, with a reason: «Saya tidak datang.» (you have a meeting)',
                      'Suggest another day: «Hari Sabtu saya tidak lapang.» (Friday)',
                      'Write it for an email: «Jom makan kat kafe tu!»',
                      'Say which one means "to treat": «Bos belanja.» or «Saya berbelanja di pasar.»'],
        'question and answer': ['«Siapa yang belanja?» (cue: «bos»)',
                                '«Sudikah encik datang?» (cue: refuse, «lapang», «Sabtu»)',
                                '«Bagaimana kalau hari Jumaat?» (cue: agree, «Setuju»)',
                                '«Kenapa encik tidak makan?» (cue: «pedas», «tidak boleh tahan»)',
                                'You hear: «Bos belanja.» Ask the question («siapa»).',
                                'You hear: «Hari Jumaat, pukul tujuh.» Ask the question («bila»).',
                                'You hear: «Ada, kat depan pejabat tu.» Ask the question («di mana»).',
                                'You hear: «Takpe. Lain kali, ya?» Say the reply («Terima kasih.»).'],
        'question-word choice': ['«Siapa ___ belanja?» → «Bos belanja.»', '«Makan malam itu di ___?» → «Di kafe.»',
                                 '«___ encik tidak boleh datang?» → «Sebab saya ada mesyuarat.»', '«Hari ___ makan malam itu?» → «Hari Jumaat.»',
                                 '«Pukul ___?» → «Pukul tujuh.»', '«Yang ___ pedas, kafe ini atau kafe itu?» → «Kafe itu.»',
                                 '«___ kalau hari Jumaat?» → «Setuju!»', '«Ada ___ orang yang datang?» → «Lima orang.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. «Sudikah» asks the other person; «Sayangnya» softens; «Setuju!» and «Tidak mengapa.» are the standard forms; «kat» and «ni» are spoken.',
                   'Cover the line and say it from the English: would you like to come; unfortunately I am not free, another time?; how about Friday; agreed, Friday at seven; never mind, we will try another time; '
                   'let\'s eat at this café, my treat; I can\'t stand spicy food; never mind, we will find another place, is that all right?'],
        'substitute': ['1 «Sudikah puan singgah?» 2 «Sayangnya hari Ahad saya tidak lapang.» 3 «Malangnya hari Jumaat saya ada mesyuarat.» 4 «Bagaimana kalau pukul lapan?» / «Bagaimana kalau kedai lain?»',
                       '5 «Puan Aini setuju.» 6 «Jom minum kat kedai mamak tu!» 7 «Saya tak tahan pedas.» 8 «Mei Ling belanja.»'],
        'transform': ['1 «Tidak mengapa.» 2 «Kita makan kat kafe ni.» 3 «Seperti itu boleh?» 4 «Saya tak tahan pedas.» 5 «Setuju!» 6 «Sudikah encik datang?» '
                      '7 «Sayangnya saya ada mesyuarat. Lain kali, ya?»',
                      '8 «Bagaimana kalau hari Jumaat?» 9 «Mari makan di kafe itu.» 10 «Bos belanja.» ("to treat"; «berbelanja» is to spend money or shop.)'],
        'question and answer': ['1 «Bos belanja.» 2 «Sayangnya hari Sabtu saya tidak lapang.» 3 «Setuju!» 4 «Saya tidak boleh tahan pedas.»',
                                '5 «Siapa yang belanja?» 6 «Bila makan malam itu?» 7 «Kedai mamak itu di mana?» 8 «Terima kasih.»'],
        'question-word choice': ['1 «yang» 2 «di mana» 3 «Kenapa» 4 «apa» 5 «berapa» 6 «Yang mana» 7 «Bagaimana» 8 «berapa» (the answer for 3 starts with «sebab» or «kerana»; also «Mengapa»)'],
    },
    short_dialogues=[
        ('Sudikah encik datang hari Jumaat?', 'Terima kasih. Setuju!', 'a polite invitation'),
        ('Sayangnya saya tidak lapang hari ini.', 'Tidak mengapa. Lain kali, ya?', 'a refusal'),
        ('Jom makan kat kafe ni!', 'Terima kasih. Tetapi kafe itu pedas.', 'friends'),
        ('Bagaimana kalau hari Isnin?', 'Itu cadangan yang bagus.', 'a suggestion')],
    short_keys=['1 «Pukul berapa?» 2 «Terima kasih. Saya ada hari lain.»',
                '3 «Takpe. Kita cari kedai lain.» 4 «Setuju! Hari Isnin, pukul tujuh.»'],
    markers=dict(
        title='Markers in invitations', grammar='invite',
        instructions=['Say each sentence again with the marker in brackets. Keep the verb as the course teaches it; only the marker is added in front. / '
                      'かっこ内のマーカーを付けて言い直します。動詞はこのコースで教えた形のままで、前にマーカーを足すだけです。'],
        items=['«Bos setuju.» (marker: «sudah»)', '«Saya lapang pada hari Jumaat.» (marker: «masih»)',
               '«Mei Ling belanja.» (marker: «akan»)', '«Encik Tanaka menerima jemputan itu.» (marker: «belum»)',
               '«Mei Ling dan Tanaka makan di kedai mamak.» (marker: «sedang»)', '«Puan Aini menghantar jemputan itu.» (marker: «baru»)',
               'Answer «Awak sudah setuju?» (marker: «belum»)', '«Kita singgah di pejabat.» (marker: «akan»)'],
        bridge=['«sudah setuju» ≈ もう賛成した · «masih lapang» ≈ まだ空いている · «akan belanja» ≈ おごる予定 · «belum menerima» ≈ まだ受けていない · '
                '«sedang makan» ≈ 食べているところ · «baru menghantar» ≈ 送ったばかり',
                'Japanese changes the verb ending (賛成した / 食べているところ); Malay puts the marker in front and keeps the verb. «belum» is まだ〜ていない, «sudah» is もう〜た, «sedang» is 〜ているところ. / '
                '日本語は動詞の語尾が変わります。マレー語はマーカーを前に置き、動詞はそのままです。«belum» は「まだ〜ていない」、«sudah» は「もう〜た」、«sedang» は「〜ているところ」です。'],
        key=['1 «Bos sudah setuju.» 2 «Saya masih lapang pada hari Jumaat.» 3 «Mei Ling akan belanja.» 4 «Encik Tanaka belum menerima jemputan itu.»',
             '5 «Mei Ling dan Tanaka sedang makan di kedai mamak.» 6 «Puan Aini baru menghantar jemputan itu.» 7 «Belum. Saya belum setuju.» 8 «Kita akan singgah di pejabat.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、誘いの文と組み合わせて言います。「〜ている」の感じは «sedang»、「まだ」は «belum» と «masih» です。',
                 'Combine the chapter 4 markers with invitations. «sedang» is the 〜ている feeling; «belum» and «masih» are both まだ, one for "not yet" and one for "still".')),
    question_note='Chapter 17 adds no new question word. The invitation questions use the ones you know: «Siapa yang belanja?», «Makan malam itu di mana?», «Pukul berapa?», «Kenapa encik tidak boleh datang?», '
                  '«Bagaimana kalau hari Jumaat?» (spoken «Macam mana kalau …?») / '
                  '第17章で新しい疑問語は増えません。誘いの質問は知っている疑問語で作ります：'
                  '«Siapa yang belanja?»、«Makan malam itu di mana?»、«Pukul berapa?»、«Kenapa encik tidak boleh datang?»、«Bagaimana kalau hari Jumaat?»（話し言葉は «Macam mana kalau …?»）',
    question_tasks=['Ask what the invitation is for. («apa»)', 'Ask who is treating. («siapa»)',
                    'Ask where the dinner is. («di mana»)', 'Ask formally whether the boss agrees. («Adakah»)',
                    'Ask politely whether you may bring a friend. («Bolehkah»)', 'Ask how many people are coming. («berapa»)',
                    'Ask when the dinner is. («bila»)', 'Ask what time the dinner starts. («pukul berapa»)',
                    'Ask on what day the dinner is. («hari apa»)', 'Ask how about Friday. («bagaimana»; spoken «macam mana»)',
                    'Ask why the person cannot come. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which café. («yang mana»)', 'Ask where everyone goes after dinner. («ke mana»)',
                    'Ask where Mr Tanaka comes from. («dari mana»)', 'Ask how far the mamak stall is. («berapa jauh»)',
                    'Ask how long the dinner lasts. («berapa lama»)', 'Ask how many dishes of «nasi lemak». («berapa» with a counter)',
                    'Ask who made the food. («siapa» with «oleh»)'],
    question_keys=['1 «Jemputan itu untuk apa?» 2 «Siapa yang belanja?» 3 «Makan malam itu di mana?»',
                   '4 «Adakah bos setuju?» 5 «Bolehkah saya bawa kawan saya?» 6 «Berapa orang yang datang?»',
                   '7 «Bila makan malam itu?» 8 «Makan malam itu pukul berapa?» 9 «Makan malam itu pada hari apa?»',
                   '10 «Bagaimana kalau hari Jumaat?» (spoken: «Macam mana kalau hari Jumaat?») 11 «Kenapa encik tidak boleh datang?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab saya ada mesyuarat.» / «Kerana saya ada mesyuarat.»',
                   '12 «Kafe yang mana?» 13 «Selepas makan malam, kita pergi ke mana?» 14 «Encik Tanaka dari mana?»',
                   '15 «Berapa jauh kedai mamak itu?» 16 «Berapa lama makan malam itu?» 17 «Berapa pinggan nasi lemak?»',
                   '18 «Makanan itu dibuat oleh siapa?»'],
    listening=LISTENING,
    listening_context='On a weekday morning «Encik» Rahman asks «Cik» Mei Ling and «Encik» Tanaka to lunch at the mamak near the office. / 平日の朝、ラーマンさんがメイリンさんと田中さんを職場の近くのママクでの昼食に誘います。',
    listening_before=['Predict: which of «takpe», «tak tahan», «set», «kat», «tu» and «belanja» will you hear? Write three guesses. / «takpe»・«tak tahan»・«set»・«kat»・«tu»・«belanja» のうち聞こえそうなものを三つ予想しましょう。',
                      'Read the eight questions below before the first listening. Listen once for «lah» and «kan» too: you only need to notice them. / 1回目の前に下の8つの質問を読みます。«lah» と «kan» にも気づくように聞きますが、気づくだけでかまいません。'],
    listen_questions=['What does Mr Rahman ask, and who pays?', 'Why can Mei Ling not come today?', 'What does he suggest instead?', 'What time is the lunch?',
                      'Why does Mr Tanaka hesitate?', 'What does Mr Rahman say about the food?', 'What are the answers of Mr Tanaka and Mei Ling?', 'How do they get there, and where do they meet?'],
    listen_answers=['to eat at the mamak stall; he pays', 'she has a meeting at one o\'clock', 'tomorrow', 'twelve o\'clock',
                    'the food is spicy and he can\'t stand spicy food', 'some food is not spicy; there is «nasi lemak»', 'Mr Tanaka agrees; Mei Ling says «Set!» and the next treat is hers', 'on foot from the office; Mr Tanaka waits in front of the office'],
    listening_after=['Compare answers, then shadow lines 1, 3 and 9 after the teacher. / 答えを比べ、1・3・9行目をシャドーイングします。',
                     'Invite your partner to eat somewhere (fictional) in three sentences, with «Jom» or «Sudikah», and let your partner refuse kindly with a reason and another time. / パートナーを食事に誘う（架空）3文を «Jom» か «Sudikah» で言い、パートナーは理由と別の機会を添えてやさしく断ります。'],
    test_listen=[(0, 'he asks her to eat at the mamak stall; he pays', ['jom', 'kedai', 'belanja']),
                 (1, 'she is not free today; she has a meeting', ['lapang', 'mesyuarat', 'terima kasih']),
                 (2, 'tomorrow', ['bagaimana', 'kalau', 'esok']),
                 (6, 'some food is not spicy; there is «nasi lemak»', ['makanan', 'pedas', 'nasi lemak']),
                 (7, 'he agrees; he is free tomorrow', ['setuju', 'lapang', 'esok']),
                 (8, 'she agrees (spoken «Set!»); tomorrow at twelve', ['set', 'esok', 'belanja'])],
    test_listen_prompts=['What does Mr Rahman ask?', 'Why can Mei Ling not come today?', 'What does he suggest instead?',
                         'What does he say about the food?', 'What does Mr Tanaka answer?', 'What does Mei Ling answer, and when is the lunch?'],
    reading_title='Reading and writing · A written invitation and a reply',
    reading=['A fictional message from the office and a written reply (standard Malay; all names are invented):',
             '«Encik Tanaka, ini jemputan makan malam pejabat. Hari: Jumaat. Pukul: tujuh malam. Tempat: kedai makan dekat pejabat. Bos belanja. Sudikah encik datang? Sila hubungi Puan Aini. Terima kasih.»',
             'Reply: «Terima kasih, Puan Aini. Saya segan untuk menolak jemputan puan, tetapi hari Jumaat saya tidak lapang. Bagaimana kalau hari Khamis? Lain kali, ya?»'],
    read_questions=['What is the message, and who is it for?', 'On what day and at what time?', 'Where is it?', 'Who pays?', 'What does the reply say about the invitation?',
                    'Why can the person not come?', 'What does he suggest?'],
    read_answers=['an invitation to the office dinner; Mr Tanaka', 'on Friday at seven in the evening', 'at a restaurant near the office', 'the boss',
                  'he is reluctant to turn it down', 'he is not free on Friday', 'Thursday; and another time'],
    write_instruction='Write three or four sentences in standard Malay (no spoken forms) to reply to the invitation (fictional): thank, say yes or no, give a reason, suggest a day. / '
                      '標準のマレー語（話し言葉は使わない）で、この招待への返事を3〜4文で書きましょう（架空でよい）：お礼、賛成か断りか、理由、別の日の提案を入れます。',
    write_model='«Terima kasih, Puan Aini. Saya setuju. Hari Jumaat saya lapang. Saya singgah di pejabat pukul enam.»',
    writing_type='message',
    task_title='Task · An invitation, a refusal and a new day',
    role_a=['Your information (fictional): you are «Puan» Aini. You invite your colleague to the team dinner on Saturday at seven; the boss pays.',
            'Invite politely with «Sudikah encik …?», listen to B, answer kindly («Tidak mengapa.») and ask «Ada cadangan lain?» After the change, ask B for the answer.',
            'Aの情報（架空）：あなたはアイニさんです。同僚を土曜日7時の職場の夕食会に誘います。ボスがおごります。'
            '«Sudikah encik …?» でていねいに誘い、Bの返事を聞き、«Tidak mengapa.» とやさしく答え、«Ada cadangan lain?» とたずねます。変更のあとはBに返事を求めます。'],
    role_b=['You are B, a colleague (fictional). On Saturday you are not free. Thank A, say «Sayangnya …» and a reason, and suggest another day with «Bagaimana kalau …?».',
            'Then switch registers: after the dinner you and A walk to a stall. Say the last two turns again as friends, in spoken Malay («Jom», «kat», «ni», «Set!»).',
            'Bは同僚です（架空）。土曜日は空いていません。Aにお礼を言い、«Sayangnya …» と理由を言って、«Bagaimana kalau …?» で別の日を提案します。'
            'そのあと場面を切り替え、夕食のあと二人で屋台まで歩きます。最後の二つのやり取りを友人として、話し言葉（«Jom»・«kat»・«ni»・«Set!»）で言い直します。'],
    change=['Halfway, A says: «Maaf, hari Jumaat bos tidak lapang. Hari Khamis boleh?» B decides: accept («Setuju!») or decline again with a reason and «Lain kali, ya?».',
            '途中でAが «Maaf, hari Jumaat bos tidak lapang. Hari Khamis boleh?» と言います。Bは «Setuju!» で受けるか、もう一度理由と «Lain kali, ya?» で断ります。'],
    success=['☐ A invites politely with «Sudikah …?» and says who pays; B thanks A and refuses with «Sayangnya …» and a reason.',
             '☐ B suggests another day with «Bagaimana kalau …?»; A takes it kindly («Tidak mengapa.») and asks for the answer after the change.',
             '☐ B answers the change clearly (a yes or a no with a reason), and the last turns are said in spoken Malay with friends («Jom», «kat», «ni», «Set!»).'],
    task_key='«Encik Tanaka, sudikah encik datang makan malam pejabat hari Sabtu, pukul tujuh? Bos belanja.» — «Terima kasih, Puan Aini. Sayangnya hari Sabtu saya tidak lapang. Bagaimana kalau hari Jumaat?» — '
             '«Tidak mengapa. Ada cadangan lain?» — Change: «Maaf, hari Jumaat bos tidak lapang. Hari Khamis boleh?» — «Setuju! Hari Khamis, pukul tujuh.» (or «Saya segan untuk menolak, tetapi hari Khamis saya ada mesyuarat. Lain kali, ya?») — '
             'Friends: «Jom makan kat kedai mamak tu!» — «Set!»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 17 card notes ms-c17-014 («tidak mengapa», spoken «tak apa» and «takpe»), -015 («macam tu»), -016 («set»), -017 («belanja», not «berbelanja», chapter 10), -022 («takpe»), -023 («tidak boleh tahan», not «boleh tahan») and -024 («tak tahan»), '
                    '-002 and -003 (‹kan›, ‹lah›: recognition only); scenario lines ms-c17-s01 to s20 (the dinner invitation, the café and the mamak); the plan, chapter 17 (standard first, spoken forms marked; ‹lah› needs tone examples; '
                    'no requirement to imitate slang or to add ‹lah›). The sentence about colleagues eating together is general knowledge, labelled as such and not source-checked.',
    culture_prompt='In Japanese, how do you refuse an invitation without saying no? In Malay, what three things do you add to a refusal, and when would you use the spoken form of «tidak mengapa»?',
    culture_explain=('標準形と話し言葉の使い分け、ちょっと…と «Sayangnya …» の違い、«lah» と «kan»、一般的な知識の文を読みます。日本語は未監修です。',
                     'Read about when to use the standard and the spoken form, ちょっと… against «Sayangnya …», «lah» and «kan», and the general knowledge sentence.'),
    quiz_words=['L-1265', 'L-1257', 'L-0717', 'L-1255', 'L-1256', 'L-0748'],
    quiz_meanings=['invitation', 'suggestion', 'to treat someone', 'to agree (the standard form of «set»)', 'to decline', 'to drop in'],
    grammar_quiz=[('Say in Malay: "Would you like to come, sir?" (polite)', '«Sudikah encik datang?»', ['sudi', 'datang']),
                  ('Say in Malay: "Unfortunately I am not free on Saturday. Another time?"', '«Sayangnya hari Sabtu saya tidak lapang. Lain kali, ya?»', ['sayangnya', 'lapang', 'lain kali']),
                  ('Say in Malay: "How about Friday?"', '«Bagaimana kalau hari Jumaat?»', ['bagaimana', 'kalau', 'Jumaat']),
                  ('Say in Malay, in the standard form: "I can\'t stand spicy food."', '«Saya tidak boleh tahan pedas.» (the spoken «Saya tak tahan pedas.» is also right in conversation)', ['tidak boleh tahan', 'pedas'])],
    test_reading=['Fictional message: «Puan Aini, terima kasih atas jemputan puan. Sayangnya hari Sabtu saya ada mesyuarat. Bagaimana kalau hari Jumaat? Lain kali, ya?»'],
    reading_quiz=[('What is the writer doing?', 'thanking for an invitation and declining it', ['terima kasih', 'jemputan']),
                  ('Why can the writer not come?', 'a meeting on Saturday', ['mesyuarat', 'Sabtu']),
                  ('What does the writer suggest?', 'Friday', ['bagaimana', 'kalau', 'Jumaat']),
                  ('What does the writer ask at the end?', 'another time', ['lain kali'])],
    speaking_test='Invite a colleague to eat at a stall near the office (fictional), say that you pay, and, when he refuses, take it kindly and suggest another day.',
    speaking_key='Check: an invitation («Jom …» to a friend, «Sudikah …?» to a senior person) with «belanja»; a kind answer to the refusal («Tidak mengapa.» or the spoken «Takpe.»); «Bagaimana kalau …?» and a day. '
                 'Accept the spoken forms in conversation and the standard forms always. Particles are never part of the answer.',
    speaking_words=['jom', 'sudi', 'belanja', 'tidak mengapa', 'bagaimana', 'kalau'],
    plan={'A_recall': 'chapters 1, 14 and 15 («tidak» / «tak», «kalau», «seperti itu») from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first («Sudikah encik ___?», «Sayangnya saya tidak ___. Lain kali, ya?»), question and answer before the rule; then the vocabulary in four groups, the standard form always before the spoken one '
                        '(invitations 8, accepting and declining 6, standard and spoken pairs 8, two particles 2). Put the pairs on the board in two columns, standard on the left, spoken on the right.',
          'B_recall': 'say one invitation and one polite refusal with a reason.',
          'B_drills': 'pattern table, substitution, transformation (standard to spoken and back, then refuse softly), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner invites a partner to eat somewhere (fictional) and the partner refuses kindly in two sentences.',
          'D_review': 'cumulative question-word drill (chapters 1 to 17), then the markers drill with new cues and a check of the standard and spoken pairs.',
          'D_preview': 'chapter 18 (the integrated review of chapters 10 to 17; there is no new word), then the fast course for chapter 17 if needed.',
          'E_recall': 'say three sentences: one «Sudikah …?», one «Sayangnya …» and one «Bagaimana kalau …?»',
          'E_listening': 'read the Kata-Kata scenario lines ms-c17-s01 to ms-c17-s16 (the dinner invitation, the café and the talk about «takpe», «lah» and «kan») and then the mamak scene ms-c17-s17 to s20 (the Block E dialogue below) twice; '
                         'learners tick «takpe», «kat», «ni», «tu», «macam tu», «tidak boleh tahan» and «Set!» when they hear them, and notice «lah» and «kan» without having to say them.',
          'E_roleplay': 'pairs play the invitation twice: first to a senior colleague in standard Malay, then to a friend in spoken Malay; then swap. Do not ask learners to use «lah» or «kan», and do not ask for a medical reason for a refusal.',
          'E_variation': 'a changed fact: the day moves from Friday to Thursday and the boss changes the plan; B accepts or declines again with a reason and «Lain kali, ya?».'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 17 to the weekend-plans and team-dinner scenes. Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: chapter 18 (the integrated review, rehearsal and the A2 check; no new word).',
    teacher_notes=['Load: 24 core words in four groups (invitations 8, accepting and declining 6, standard and spoken pairs 8, two particles 2), no recognition word, and revision of the Stage 1 spoken forms, food and the café, plans, days and the office. '
                   'Suggested order: Block A the first two groups with patterns 1 and 2; Block B the pairs and the particles with patterns 3 to 5. '
                   'If the pilot shows 24 is too many, the natural cut is: «sudi», «lapang», «setuju», «menolak», «sayangnya», «lain kali», «tidak mengapa», «tidak boleh tahan», «jemputan» first; the rest second.',
                   'Standard first, always: the standard form is taught before its spoken form, and the spoken form is labelled "spoken". The pairs of this chapter: «tidak mengapa» / «takpe» or «tak apa»; «tidak boleh tahan» / «tak tahan»; «seperti itu» / «macam tu»; «di» / «kat»; «ini» / «ni»; «itu» / «tu»; «setuju» / «set»; and «jom» against «mari». '
                   'Learners must understand the spoken forms, may use them with friends and colleagues, and write the standard forms. The spoken form is never marked wrong in conversation and the standard form is always right.',
                   'When to use the spoken forms and when not: use them with friends, with colleagues you know and at the mamak; do not use them in emails, forms, notices or meetings with clients, or with someone you meet for the first time. '
                   'When in doubt, use the standard form: nobody is offended by it. «takpe» is a slang short form of «tak apa», which is the spoken form of «tidak mengapa» (the Kata-Kata card says "recognise only" for «takpe»).',
                   '«tidak boleh tahan» against «boleh tahan»: «Saya tidak boleh tahan pedas.» means "I can\'t stand spicy food"; «boleh tahan» (chapter 5) means "not bad": a different expression. The spoken form is «tak tahan»; for a plain dislike say «Saya tak nak pedas.» or «Saya tak suka pedas.» '
                   'Learners give only a taste or a plain reason; do not ask for or discuss a medical reason for refusing food.',
                   '«lah» and «kan» are recognition only (Sam, R4): you hear them, you may say them, and no key, task or test requires them. «lah» softens or stresses, and its meaning depends on the tone («Takpelah.» is softer, «Bolehlah.» is a reluctant yes); in writing it joins the word. '
                   '«kan» asks the listener to agree, and it is not the suffix ‹-kan› (chapter 12). Japanese learners over-use «lah», often on every sentence; tell them that a sentence without «lah» is correct and that it is not a copy of よ or ね. Do not mark a sentence without them wrong.',
                   'Polite refusal in Malaysia against Japanese ちょっと…: soften («Sayangnya …», «Malangnya …»), give a reason, and offer another time («Lain kali, ya?»). Saying only «Susah» or nothing leaves the host unsure; a clear but soft no is both polite and understood. '
                   '«Saya segan untuk menolak jemputan puan.» is a polite way to say that you are reluctant. The teacher stays with this teaching hypothesis: it is not a rule of Malaysian manners and is not source-checked.',
                   '«belanja» means to treat someone (to pay for them), not to spend money: «Bos belanja.» «Saya belanja!» The chapter 10 word «berbelanja» is to spend money or shop. A learner who says «Saya belanja di pasar» for shopping has mixed them. '
                   '«Lain kali saya belanja.» is the kind answer to a treat. «menolak» is «tolak» (chapter 9, push) with meN-; here it means to decline.',
                   '«jom», «mari», «ajak», «jemput» and «sudi» are different tones, not shortenings of one another: «Sudikah encik datang?» (polite, to a senior person), «Mari kita pergi.» (standard), «Jom makan!» (friends), «Saya ajak encik.» (friendly), «Ini jemputan daripada Puan Aini.» (a written invitation). '
                   '«sudi» asks the other person and is not used about yourself.',
                   '«kami» against «kita» in invitations: «Sudikah puan makan dengan kami?» (the host speaks for a group; «kami» does not include the listener) and «Kita pergi sama-sama.» (all of us together; «kita» includes the listener).',
                   'The ‹-kan› and bare-root rules from chapters 12 to 16 still hold: a dialogue line may keep Kata-Kata\'s everyday bare root («Saya tanya bos dulu.», «Kita pergi sama-sama.»), and a request takes the plain root; the written reply and the pattern examples use «menerima» and «menghantar». '
                   '«tangguhkan» and «batalkan» are not used in this unit. «dari» is for places and «daripada» for people and offices («jemputan daripada Puan Aini»).',
                   'The Kata-Kata Sedia Kelas list for this chapter also names a Dunia card about a festival open house; this unit teaches no festival and no faith-specific expression, and the only invitations are to an office dinner, a café and the mamak. '
                   'The unit uses no religious greeting or reply.',
                   'Where Japanese learners usually slip: (1) «sudi» about themselves; (2) «lah» on every sentence; (3) «belanja» for spending; (4) the spoken form with a client or in an email; (5) a refusal with no reason («Susah»); '
                   '(6) «boleh tahan» for "can\'t stand"; (7) «kami» for "all of us".',
                   'Natural speech: «Jom makan kat kafe ni!», «Takpe.», «Set!», «Saya tak tahan pedas.», «Macam tu boleh?»; and in standard speech «Sudikah encik datang?», «Tidak mengapa.», «Setuju!», «Lain kali, ya?» '
                   'The scene follows Kata-Kata c17 (scenario lines ms-c17-s01 to s20, frames f01 to f06). The model is s01 to s16, one line to a turn, with no turn joined across a scene change (s07 and s08 are both «Puan» Aini, who asks the boss in between); '
                   'the mamak scene (s17 to s20) is the Block E dialogue. The inner «…» of lines s13 and s15 are shown as ‘…’. All names, places and times are fictional.',
                   'Cumulative question words: chapters 1 to 17. Chapter 17 adds no new question word.'],
)

CFG['extra'] = None
UNIT = unit_dict(CFG)
