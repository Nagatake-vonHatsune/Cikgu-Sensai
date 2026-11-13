"""Unit 14: reasons, conditions, purpose, contrast and sequence: planning the weekend hike, the rain plan and the change to Sunday
(Kalau ___, kita ___; Saya tidak datang kerana ___; Saya ___ supaya ___; Walaupun ___, saya ___; Dia ___ sambil ___; Mula-mula ___, kemudian ___, akhirnya ___).

22 core ledger entries, the rows the ledger places in "Ch14 (unit 14)": the existing rows L-0641 «tangguh» and L-0710 «janji», the new rows
L-1201 to L-1218, and L-1269 «tangguhkan» and L-1270 «batalkan» (added by Sam, Journal row 184, with their roots «tangguh» and «batal»). They come in
three groups: joining ideas (10: the formal connectors «jika», «apabila», «namun», «oleh itu» beside the everyday «kalau», «bila», «tetapi», «jadi»),
the order of a plan (3) and plans and changes (9). No recognition word. The ke-an, per-an, -an, -nya and lexicalised words («keputusan», «perubahan»,
«tujuan», «pilihan», «akhirnya», «seterusnya», «semasa», «walaupun», «mula-mula») are taught as whole words, as the Kata-Kata chapter 14 card notes say.
The scene follows Kata-Kata c14 (scenario lines ms-c14-s01 to s15: Tanaka and Cik Mei Ling plan the hike, the rain plan and the change to Sunday)
word for word, and goes further in class: a second friend, a message in written Malay, a changed day. All names and plans are fictional.

Register (Sam, 13 Nov 2026): «kalau» and «bila» are everyday and are what people say; «jika» and «apabila» are standard and written. The
casual turns use no ruling-style words («keputusan», «ialah»); «keputusan» is taught as a word for a written notice or a result.
The -kan rule of chapter 12 holds: «tangguhkan» and «batalkan» appear in «kita» sentences and requests, never after an aspect word or with a
aspect word; with a third-person doer the bare form is allowed for now (Sam, 13 Nov 2026: «Mei Ling tangguhkan …»; the meN- forms come in a later chapter), and «Rancangan mendaki batal.» is the intransitive. Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

JOIN = ['L-1201', 'L-1202', 'L-1203', 'L-1204', 'L-1205', 'L-1206', 'L-1207', 'L-1217', 'L-1211', 'L-1212']
ORDER = ['L-1209', 'L-1210', 'L-1208']
PLANS = ['L-1213', 'L-1214', 'L-1215', 'L-1216', 'L-0710', 'L-0641', 'L-1269', 'L-1218', 'L-1270']
CORE = JOIN + ORDER + PLANS

# Revision: words placed in chapters 1 to 13 that the unit really uses (a test fails if one is not used).
REV_IDS = {}
REV_JOIN = ['L-0341', 'L-1007', 'L-1050', 'L-0688', 'L-0215', 'L-1009', 'L-0030', 'L-0076', 'L-1185', 'L-0194']
REV_WEATHER = ['L-0434', 'L-0433', 'L-0432', 'L-0431', 'L-0865', 'L-1090', 'L-1093', 'L-0249']
REV_PLAN = ['L-0684', 'L-0295', 'L-1026', 'L-1098', 'L-1154', 'L-0475', 'L-0078', 'L-0206', 'L-0207', 'L-1006', 'L-0550', 'L-1089', 'L-0534']
REV_TALK = ['L-0320', 'L-1091', 'L-1124', 'L-0197', 'L-0198', 'L-0259', 'L-0283', 'L-0013', 'L-0997', 'L-0191', 'L-0480']

EXAMPLES = {
    # Joining ideas
    'L-1201': '«Saya bangun awal supaya saya tidak lambat.»',
    'L-1202': '«Walaupun saya penat, saya suka mendaki.»',
    'L-1203': '«Jika hujan, kita tangguhkan.» (written; everyday «Kalau hujan, kita tangguhkan.»)',
    'L-1204': '«Apabila cuaca cerah, kita mendaki.» (written; everyday «Bila cuaca cerah, kita mendaki.»)',
    'L-1205': '«Kita boleh bercakap sambil berjalan.»',
    'L-1206': '«Cuaca mendung. Namun kita masih mahu mendaki.» (written; everyday «tetapi»)',
    'L-1207': '«Saya bekerja pada hari Sabtu. Oleh itu, kita tangguhkan rancangan itu ke hari Ahad.» (formal; everyday «jadi»)',
    'L-1217': '«Jadi, boleh kita tangguhkan ke hari Ahad?»',
    'L-1211': '«Semasa mendaki, kita minum air.»',
    'L-1212': '«Sejak bulan lepas saya suka mendaki.»',
    # The order of a plan
    'L-1209': '«Mula-mula kita berjumpa di stesen pukul tujuh.»',
    'L-1210': '«Seterusnya kita mendaki.» (written; everyday «Kemudian kita mendaki.»)',
    'L-1208': '«Akhirnya kita makan di kafe.»',
    # Plans and changes
    'L-1213': '«Tujuan kita sama: berehat dan berjalan.»',
    'L-1214': '«Ada dua pilihan.»',
    'L-1215': '«Keputusan: kita mendaki pada hari Ahad.» (a written notice)',
    'L-1216': '«Ada perubahan rancangan.»',
    'L-0710': '«Hari Ahad saya cuti. Janji!»',
    'L-0641': '«Tangguh dulu, ya?» (the root of «tangguhkan»)',
    'L-1269': '«Boleh kita tangguhkan ke hari Ahad?»',
    'L-1218': '«Rancangan mendaki batal kerana hujan.»',
    'L-1270': '«Kita batalkan rancangan mendaki.»',
    # Revision · if, because, but
    'L-0341': '«Kalau hujan, kita makan di kafe.»',
    'L-1007': '«Bila cuaca cerah, kita mendaki.»',
    'L-1050': '«Saya tidak datang kerana saya bekerja.»',
    'L-0688': '«Sebab saya bekerja.»',
    'L-0215': '«Cuaca mendung, tetapi kita masih mahu mendaki.»',
    'L-1009': '«Kenapa awak tidak datang?»',
    'L-0030': '«Kalau tidak hujan, kita mendaki.»',
    'L-0076': '«Kita boleh bercakap sambil berjalan.»',
    'L-1185': '«Kita perlu tulis mesej untuk kawan kita.»',
    'L-0194': '«Saya belum tulis mesej itu.»',
    # Revision · weather and the hike
    'L-0434': '«Kalau hujan, kita makan di kafe.»',
    'L-0433': '«Cuaca mendung.»',
    'L-0432': '«Apabila cuaca cerah, kita mendaki.»',
    'L-0431': '«Cuaca hari Ahad bagus.»',
    'L-0865': '«Kalau tidak hujan, kita mendaki.»',
    'L-1090': '«Walaupun hujan, saya mahu berjalan kaki.»',
    'L-1093': '«Tujuan kita sama: berehat dan berjalan.»',
    'L-0249': '«Walaupun saya penat, saya suka mendaki.»',
    # Revision · the plan
    'L-0684': '«Kita batalkan rancangan mendaki.»',
    'L-0295': '«Kita berjumpa di stesen pukul tujuh.»',
    'L-1026': '«Akhirnya kita makan di kafe.»',
    'L-1098': '«Mula-mula kita berjumpa di stesen.»',
    'L-1154': '«Saya sudah tulis mesej untuk kawan kita.»',
    'L-0475': '«Saya sudah tulis mesej itu.»',
    'L-0078': '«Saya sudah tulis mesej untuk kawan kita.»',
    'L-0206': '«Saya akan datang awal supaya kita tidak lambat.»',
    'L-0207': '«Saya akan datang awal supaya kita tidak lambat.»',
    'L-1006': '«Saya tidak boleh datang pada hari Sabtu.»',
    'L-0550': '«Saya bangun awal supaya saya tidak lambat.»',
    'L-1089': '«Saya tidak datang kerana saya bekerja.»',
    'L-0534': '«Hari Ahad saya cuti.»',
    # Revision · talking
    'L-0320': '«Kemudian kita mendaki.»',
    'L-1091': '«Kita boleh bercakap sambil berjalan.»',
    'L-1124': '«Dia makan sambil membaca surat khabar.»',
    'L-0197': '«Kita makan di kafe.»',
    'L-0198': '«Semasa mendaki, kita minum air.»',
    'L-0259': '«Semasa mendaki, kita minum air.»',
    'L-0283': '«Bagus! Kita mendaki hari Ahad.»',
    'L-0013': '«Baik. Ini rancangan kita.»',
    'L-0997': '«Ya, betul!»',
    'L-0191': '«Masih. Kita masih mahu mendaki.»',
    'L-0480': '«Kita guna kalau dan bila, ya?»',
}

# For the whole words and the suffixed forms: the root as the Kata-Kata card note gives it, and the teaching point.
VOCAB_OPTS = {
    'L-1202': {'en': 'although, even though (learn the whole word; the root ‹walau› is not taught alone)',
               'ja': '〜だけれども・〜のに（一語まるごと覚える；語根 ‹walau› は単独では教えない）'},
    'L-1203': {'en': 'if; standard and written (the everyday partner is «kalau», chapter 7: people say «kalau»; a message or a notice may say «jika»)',
               'ja': 'もし〜なら；標準・書き言葉（日常の相手は «kalau»（第7章）：話すときは «kalau»、メッセージや掲示では «jika» も使う）'},
    'L-1204': {'en': 'when; standard and written (the everyday partner is «bila», chapter 4: «bila» for "when" is everyday, «apabila» is standard)',
               'ja': '〜するとき；標準・書き言葉（日常の相手は «bila»（第4章）：「〜するとき」の «bila» は日常語、«apabila» は標準語）'},
    'L-1206': {'en': 'however; written only (the everyday partner is «tetapi», chapter 5; spoken «tapi»)',
               'ja': 'しかし；書き言葉のみ（日常の相手は «tetapi»（第5章）；話し言葉は «tapi»）'},
    'L-1207': {'en': 'therefore; formal (the everyday partner is «jadi», below; a fixed phrase: «oleh» chapter 9 + «itu»)',
               'ja': 'そのため；改まった語（日常の相手は下の «jadi»；決まった言い方：«oleh»（第9章）＋ «itu»）'},
    'L-1210': {'en': 'next, after that; formal and written (the everyday partner is «kemudian», chapter 7; spoken ‹lepas tu›, recognise only; learn the whole word, the root is «terus», chapter 7)',
               'ja': '次に；改まった書き言葉（日常の相手は «kemudian»（第7章）；話し言葉の ‹lepas tu› は聞いて分かればよい；一語まるごと覚える、語根は «terus»（第7章））'},
    'L-1208': {'en': 'finally, at last (‹akhir› + ‹-nya›: learn the whole word)',
               'ja': '最後に・ついに（‹akhir› ＋ ‹-nya›：一語まるごと覚える）'},
    'L-1209': {'en': 'first, at first (learn the whole word; repeated words come in Stage 3; the root is «mula», chapter 4)',
               'ja': '最初に（一語まるごと覚える；重ね語は第3段階；語根は «mula»（第4章））'},
    'L-1211': {'en': 'during, when (learn the whole word; the root is «masa», chapter 4)',
               'ja': '〜の間に（一語まるごと覚える；語根は «masa»（第4章））'},
    'L-1213': {'en': 'purpose (‹tuju› + ‹-an›: learn the whole word)',
               'ja': '目的（‹tuju› ＋ ‹-an›：一語まるごと覚える）'},
    'L-1214': {'en': 'choice («pilih», chapter 6, + ‹-an›: learn the whole word)',
               'ja': '選択肢（«pilih»（第6章）＋ ‹-an›：一語まるごと覚える）'},
    'L-1215': {'en': 'decision, or result; here a word for a written notice (learn the whole word; ‹ke-an› words come in Stage 3; the root is ‹putus›)',
               'ja': '決定・結果；ここでは書かれた掲示の語（一語まるごと覚える；‹ke-an› の語は第3段階；語根は ‹putus›）'},
    'L-1216': {'en': 'change (learn the whole word; ‹per-an› words come in Stage 3; the root is ‹ubah›): «perubahan rancangan» = a change of plan',
               'ja': '変更・変化（一語まるごと覚える；‹per-an› の語は第3段階；語根は ‹ubah›）：«perubahan rancangan»＝予定の変更'},
    'L-0641': {'en': 'to put off, to pause for a while; the root of «tangguhkan»',
               'ja': '延期する・しばらく休む；«tangguhkan» の語根'},
    'L-1269': {'en': 'to postpone, to put something off («tangguh» + ‹-kan›): for a request or a "we" sentence, as in chapter 12',
               'ja': '延期する・先に延ばす（«tangguh» ＋ ‹-kan›）：第12章と同じく依頼や «kita» の文に使う'},
    'L-1218': {'en': 'to cancel; cancelled (the root of «batalkan»; «Rancangan mendaki batal.» = the hike is off)',
               'ja': '取り消す・中止になる（«batalkan» の語根；«Rancangan mendaki batal.»＝ハイキングは中止）'},
    'L-1270': {'en': 'to cancel something («batal» + ‹-kan›): for a request or a "we" sentence, as in chapter 12',
               'ja': '取り消す（«batal» ＋ ‹-kan›）：第12章と同じく依頼や «kita» の文に使う'},
}

P = [
    ('ms-c14-f01', '«Kalau» ___ «, kita makan di kafe.»  (condition: «kalau», written «jika»)', [
        'A: «Kalau hujan, apa kita buat?» B: «Kalau hujan, kita makan di kafe.»',
        'A: «Kalau tidak hujan, kita buat apa?» B: «Kalau tidak hujan, kita mendaki.»',
        'A: «Kalau awak penat, awak buat apa?» B: «Kalau saya penat, saya berehat.»',
        'A: «Bila kita makan di kafe?» B: «Kalau hujan.»',
        'A: «Bila awak mendaki?» B: «Bila cuaca cerah.»',
        'A: «Apa dalam mesej itu?» B: «Jika hujan, kita tangguhkan. Apabila cuaca cerah, kita mendaki.»'],
     "«Kalau» + a clause says the condition, then a comma, then what follows: «Kalau hujan, kita makan di kafe.» (the Kata-Kata frame). Nothing like \"then\" comes after the comma. "
     "«Kalau tidak hujan» is the opposite condition. «kalau» is what people say, and «jika» is the standard word for a message or a notice: «Jika hujan, kita tangguhkan.» "
     "Both mean \"if\". Compare «bila» and «apabila»: «bila» (chapter 4) is \"when\" in everyday speech («Bila cuaca cerah, kita mendaki.»), and «apabila» is the standard word for writing. "
     "«Kalau» is if (it may or may not happen); «bila» and «apabila» are when (it will happen at some point). At the start of a question «Bila …?» still asks \"when?\"",
     "«Kalau» ＋ 節で条件を言い、コンマのあとに結果を続けます：«Kalau hujan, kita makan di kafe.»（Kata-Kata の文型）。コンマのあとに「それなら」にあたる語は入りません。"
     "«Kalau tidak hujan» は反対の条件です。«kalau» は話すときの語で、«jika» はメッセージや掲示の標準語です：«Jika hujan, kita tangguhkan.» どちらも「もし」です。"
     "«bila» と «apabila» も同じです：«bila»（第4章）は日常の「〜するとき」（«Bila cuaca cerah, kita mendaki.»）、«apabila» は書くときの標準語です。"
     "«Kalau» は起こるかどうか分からない「もし」、«bila»・«apabila» はいつか起こる「〜するとき」です。文頭の «Bila …?» は「いつ？」のままです。",
     'Japanese has four ways to say if: 〜たら, 〜ば, 〜なら and 〜と. Malay uses «kalau» for all of them, and the result comes after a comma with no extra word. Keep «bila» (when it happens) apart from «kalau» (if it happens): 雨が降ったら is «kalau hujan», 晴れたとき is «bila cuaca cerah».',
     '日本語には「もし」を表す形が四つあります（〜たら・〜ば・〜なら・〜と）。マレー語はすべて «kalau» で言い、結果はコンマのあとに余計な語なしで続けます。«bila»（起こるとき）と «kalau»（起こるなら）を分けてください：「雨が降ったら」は «kalau hujan»、「晴れたとき」は «bila cuaca cerah» です。'),
    ('ms-c14-f02 and f03', '«Saya tidak datang kerana saya» ___ «.» / «Saya bangun awal supaya saya tidak» ___ «.»  (reason and purpose)', [
        'A: «Kenapa awak tidak datang?» B: «Saya tidak datang kerana saya bekerja.»',
        'A: «Kenapa cik tidak boleh datang pada hari Sabtu?» B: «Sebab saya bekerja.»',
        'A: «Kenapa awak bangun awal?» B: «Saya bangun awal supaya saya tidak lambat.»',
        'A: «Kenapa awak datang awal?» B: «Saya datang awal supaya kita tidak lambat.»',
        'A: «Kenapa Mei Ling tangguhkan rancangan mendaki?» B: «Mei Ling tangguhkan rancangan mendaki kerana dia bekerja.»',
        'A: «Apa tujuan mesej ini?» B: «Supaya kawan kita tahu rancangan itu.»'],
     "«kerana» (chapter 5) and «sebab» (chapter 5) both give the reason: the main clause comes first and the reason after it, «Saya tidak datang kerana saya bekerja.» (the Kata-Kata frame). "
     "«kerana» is the standard word, «sebab» is just as common in speech, and the answer to «Kenapa …?» can start with either. "
     "«supaya» gives the purpose, \"so that\": «Saya bangun awal supaya saya tidak lambat.» (the Kata-Kata frame). The clause after «supaya» has its own subject («saya», «kita») and is often negative. "
     "«tujuan» is the purpose as a noun: «Apa tujuan mesej ini?» Do not use «supaya» for a reason, and do not use «kerana» for a purpose.",
     "«kerana»（第5章）と «sebab»（第5章）はどちらも理由を言います。主節が先で、理由があとに来ます：«Saya tidak datang kerana saya bekerja.»（Kata-Kata の文型）。"
     "«kerana» は標準語、«sebab» は話し言葉でも同じようによく使い、«Kenapa …?» への答えはどちらで始めてもかまいません。"
     "«supaya» は目的の「〜ように」です：«Saya bangun awal supaya saya tidak lambat.»（Kata-Kata の文型）。«supaya» のあとの節には自分の主語（«saya»・«kita»）があり、否定になることがよくあります。"
     "«tujuan» は名詞の「目的」です：«Apa tujuan mesej ini?» 理由に «supaya» を、目的に «kerana» を使わないでください。",
     'Japanese ので and から give a reason; ために and ように give a purpose. Malay keeps the pairs apart: «kerana» and «sebab» are ので・から, «supaya» is ように. A learner who says «Saya tidak datang supaya saya bekerja» has said the purpose by mistake.',
     '日本語の「ので」「から」は理由、「ために」「ように」は目的です。マレー語も分けます：«kerana»・«sebab» が「ので・から」、«supaya» が「ように」。«Saya tidak datang supaya saya bekerja» と言うと、うっかり目的を言ってしまいます。'),
    ('ms-c14-f04', '«Walaupun» ___ «, saya mahu» ___ «.»  (contrast)', [
        'A: «Hujan. Awak masih mahu berjalan kaki?» B: «Ya. Walaupun hujan, saya mahu berjalan kaki.»',
        'A: «Awak penat. Awak masih mahu mendaki?» B: «Ya. Walaupun saya penat, saya suka mendaki.»',
        'A: «Hari ini panas. Awak masih mahu pergi?» B: «Ya. Walaupun panas, saya mahu pergi.»',
        'A: «Walaupun hujan, kita mendaki?» B: «Tidak. Kalau hujan, kita makan di kafe.»',
        'A: «Awak penat. Awak mahu balik?» B: «Tidak. Walaupun penat, saya mahu makan di kafe dengan kawan.»',
        'A: «Apa dalam mesej itu?» B: «Rancangan mendaki batal kerana hujan. Namun kita masih makan di kafe.»'],
     "«walaupun» + a clause says what is true although something else is true: «Walaupun hujan, saya mahu berjalan kaki.» (the Kata-Kata frame). The comma comes after the first clause and the surprising part follows. "
     "Do not add «tetapi» in the second clause, because «walaupun» already carries the contrast. For two separate sentences, «tetapi» (chapter 5; spoken «tapi») is the everyday word and «namun» is the written one: "
     "«Rancangan mendaki batal. Namun kita masih makan di kafe.» «Kalau» is not the same as «walaupun»: «kalau hujan» is a condition, «walaupun hujan» says the rain is no obstacle.",
     "«walaupun» ＋ 節で、別のことが事実であってもこうだ、という対比を言います：«Walaupun hujan, saya mahu berjalan kaki.»（Kata-Kata の文型）。最初の節のあとにコンマを置き、意外な部分が続きます。"
     "後ろの節に «tetapi» は足しません。«walaupun» がすでに対比を表しているからです。二つの別々の文では、日常語は «tetapi»（第5章；話し言葉は «tapi»）、書き言葉は «namun» です："
     "«Rancangan mendaki batal. Namun kita masih makan di kafe.» «Kalau» と «walaupun» は違います。«kalau hujan» は条件、«walaupun hujan» は「雨でも関係ない」です。",
     'Japanese のに, けれども and 〜ても all point at contrast. In Malay «walaupun» opens the first clause and there is no «tetapi» in the second: 雨なのに歩く is «Walaupun hujan, saya berjalan». For 雨が降っても use «walaupun hujan» too, but 雨が降ったら is «kalau hujan».',
     '日本語の「のに」「けれども」「〜ても」はどれも対比を示します。マレー語では «walaupun» が最初の節を始め、後ろの節に «tetapi» は入りません：「雨なのに歩く」は «Walaupun hujan, saya berjalan»。「雨が降っても」も «walaupun hujan» ですが、「雨が降ったら」は «kalau hujan» です。'),
    ('ms-c14-f05', '«Dia makan sambil» ___ «.»  (two things at once; also «semasa» and «sejak»)', [
        'A: «Dia makan sambil buat apa?» B: «Dia makan sambil membaca surat khabar.»',
        'A: «Awak minum teh sambil buat apa?» B: «Saya minum teh sambil bercakap dengan kawan.»',
        'A: «Boleh kita bercakap sambil berjalan?» B: «Boleh. Kita boleh bercakap sambil berjalan.»',
        'A: «Awak makan sambil bekerja?» B: «Tidak. Saya makan dulu, kemudian saya bekerja.»',
        'A: «Semasa mendaki, awak buat apa?» B: «Semasa mendaki, saya minum air dan berehat.»',
        'A: «Sejak bila awak suka mendaki?» B: «Sejak bulan lepas.»'],
     "«sambil» + a verb says that one person does two things at the same time, and the person is the same for both: «Dia makan sambil membaca surat khabar.» (the Kata-Kata frame). "
     "«semasa» (during, when) is for a period or an event: «Semasa mendaki, kita minum air.» «sejak» (since) names the point where something started: «Sejak bulan lepas saya suka mendaki.» "
     "All three are learned as they are. When two people do two different things, say two sentences, not «sambil».",
     "«sambil» ＋ 動詞は、同じ人が同時に二つのことをする、という意味です：«Dia makan sambil membaca surat khabar.»（Kata-Kata の文型）。"
     "«semasa»（〜の間に）は期間や出来事に使います：«Semasa mendaki, kita minum air.» «sejak»（〜以来）は始まりの時点を言います：«Sejak bulan lepas saya suka mendaki.» "
     "三つともそのまま覚えます。二人が別々のことをするときは «sambil» ではなく、文を二つにします。",
     'Japanese 〜ながら is one verb form. Malay puts «sambil» between the two actions and keeps both verbs plain: 食べながら読む is «makan sambil membaca». 〜の間に is «semasa» and 〜以来 is «sejak».',
     '日本語の「〜ながら」は動詞の形です。マレー語は二つの動作のあいだに «sambil» を置き、どちらの動詞も形を変えません：「食べながら読む」は «makan sambil membaca»。「〜の間に」は «semasa»、「〜以来」は «sejak» です。'),
    ('ms-c14-f06', '«Mula-mula kita» ___ «, kemudian kita» ___ «, akhirnya kita» ___ «.»  (sequence)', [
        'A: «Apa rancangan kita?» B: «Mula-mula kita berjumpa di stesen. Kemudian kita mendaki. Akhirnya kita makan di kafe.»',
        'A: «Awak buat apa pagi ini?» B: «Mula-mula saya bangun, kemudian saya makan, akhirnya saya pergi bekerja.»',
        'A: «Apa dalam mesej itu?» B: «Mula-mula berjumpa di stesen. Seterusnya mendaki. Akhirnya makan di kafe.»',
        'A: «Akhirnya awak sampai!» B: «Ya, akhirnya saya sampai. Maaf, saya lambat.»',
        'A: «Kita tangguhkan rancangan mendaki, ya?» B: «Ya. Mula-mula kita tangguhkan, kemudian kita tulis mesej untuk kawan kita.»',
        'A: «Mula-mula kita buat apa?» B: «Mula-mula kita berjumpa di stesen pukul tujuh.»'],
     "«mula-mula», «kemudian» and «akhirnya» give the order: first, then, finally. «Mula-mula kita berjumpa di stesen. Kemudian kita mendaki. Akhirnya kita makan di kafe.» "
     "(Kata-Kata lines). «mula-mula» is learned as a whole word, and «akhirnya» is ‹akhir› + ‹-nya›, also a whole word. «kemudian» (chapter 7) is the everyday \"then\"; "
     "in a formal message or a notice the word is «seterusnya» (next). In speech you may also hear ‹lepas tu›, which this course only asks you to recognise. "
     "Each step is a short sentence with the same subject, so say it again or leave it out when it is clear.",
     "«mula-mula»・«kemudian»・«akhirnya» は順序を言います：まず・それから・最後に。«Mula-mula kita berjumpa di stesen. Kemudian kita mendaki. Akhirnya kita makan di kafe.»（Kata-Kata の文）。"
     "«mula-mula» は一語として、«akhirnya» は ‹akhir› ＋ ‹-nya› ですがやはり一語として覚えます。«kemudian»（第7章）は日常の「それから」で、"
     "改まったメッセージや掲示では «seterusnya»（次に）を使います。話し言葉では ‹lepas tu› も聞こえますが、このコースでは聞いて分かればよい語です。"
     "各段階は主語が同じ短い文で、分かるときは主語を繰り返すか省きます。",
     'Japanese まず, それから and 最後に are the same three steps. Malay needs no connecting verb form: each step is a plain sentence. Do not use «kemudian» for 〜のあとで when another event comes first («selepas» is for that).',
     '日本語の「まず」「それから」「最後に」と同じ三つの段階です。マレー語は動詞の形をつなぎ変えず、各段階を素の文にします。ほかの出来事が先にあるときの「〜のあとで」には «kemudian» ではなく «selepas» を使います。'),
]

# The Kata-Kata scenario lines ms-c14-s01 to s15 are the model conversation (the hike, the rain plan and the change to Sunday).
DIALOGUE = [
    ('Tanaka', 'Cik Mei Ling, hujung minggu ini kita masih mahu mendaki?'),
    ('Mei Ling', 'Masih. Tetapi cuaca mendung. Kalau hujan pada hari Sabtu, kita tidak boleh mendaki.'),
    ('Tanaka', 'Kalau hujan, kita makan di kafe. Kalau tidak hujan, kita mendaki.'),
    ('Mei Ling', 'Bagus! Tetapi saya tidak boleh datang pada hari Sabtu kerana saya bekerja.'),
    ('Tanaka', 'Ada dua pilihan: kita tangguhkan ke hari Ahad atau ke hari Sabtu depan.'),
    ('Mei Ling', 'Hari Ahad lebih baik. Hari Ahad saya cuti. Janji!'),
    ('Tanaka', 'Ada perubahan rancangan, tetapi tujuan kita sama: berehat dan berjalan.'),
    ('Tanaka', 'Baik. Ini rancangan kita. Mula-mula kita berjumpa di stesen pukul tujuh. Kemudian kita mendaki. Akhirnya kita makan di kafe.'),
    ('Mei Ling', 'Saya akan datang awal supaya kita tidak lambat.'),
    ('Tanaka', 'Bagus. Walaupun saya penat, saya suka mendaki. Kita boleh bercakap sambil berjalan.'),
    ('Mei Ling', 'Kalau hujan lagi pada hari Ahad, bagaimana?'),
    ('Tanaka', 'Kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.'),
    ('Mei Ling', 'Baik. Saya sudah tulis mesej untuk kawan kita. Jika hujan, kita tangguhkan. Apabila cuaca cerah, kita mendaki.'),
    ('Tanaka', 'Oh, itu bahasa mesej. Kalau kita bercakap, kita guna kalau dan bila, ya?'),
    ('Mei Ling', 'Ya, betul!'),
]
VARIANT = [
    ('Tanaka', 'Cik Mei Ling, hari Ahad saya ada mesyuarat. Saya tidak boleh mendaki.'),
    ('Mei Ling', 'Oh. Jadi, kita tangguhkan ke hari Sabtu depan?'),
    ('Tanaka', 'Boleh. Walaupun lama, Sabtu depan lebih baik. Awak janji datang awal?'),
    ('Mei Ling', 'Janji! Saya datang awal supaya kita tidak lambat.'),
    ('Tanaka', 'Bagus. Kalau hujan, bagaimana?'),
    ('Mei Ling', 'Kalau hujan, kita batalkan rancangan mendaki. Kita makan di kafe sahaja.'),
    ('Tanaka', 'Baik. Mula-mula kita berjumpa di stesen. Kemudian kita berjalan. Akhirnya kita makan.'),
    ('Mei Ling', 'Bagus. Kita boleh minum teh sambil bercakap.'),
    ('Tanaka', 'Baik. Kita boleh tulis mesej untuk kawan kita sekarang?'),
    ('Mei Ling', 'Tangguh dulu, ya? Kita tunggu cuaca hari Jumaat.'),
]
LISTENING = [
    ('Tanaka', 'Selamat petang, Puan Aini. Hujung minggu ini kami mahu mendaki. Puan Aini mahu datang?'),
    ('Aini', 'Mahu! Tetapi kenapa hari Ahad? Bukan hari Sabtu?'),
    ('Tanaka', 'Cik Mei Ling bekerja pada hari Sabtu. Jadi, kita tangguhkan ke hari Ahad.'),
    ('Aini', 'Baik. Kalau hujan pada hari Ahad, bagaimana?'),
    ('Tanaka', 'Kalau hujan, rancangan mendaki batal. Tetapi kita masih berjumpa dan makan di kafe.'),
    ('Aini', 'Bagus. Mula-mula kita berjumpa di mana?'),
    ('Tanaka', 'Di stesen, pukul tujuh. Kemudian kita mendaki. Akhirnya kita makan di kafe.'),
    ('Aini', 'Pukul tujuh? Walaupun saya penat pada hari Ahad, saya akan datang. Saya datang awal supaya kita tidak lambat. Janji!'),
    ('Tanaka', 'Terima kasih. Kita boleh bercakap sambil berjalan.'),
    ('Aini', 'Seronok! Sejak bulan lepas saya tidak mendaki. Saya perlu bawa apa?'),
    ('Tanaka', 'Bawa air dan payung. Semasa mendaki, kita minum air. Kalau hujan, kita guna payung.'),
    ('Aini', 'Baik, saya bawa. Nanti saya tulis mesej untuk Cik Mei Ling.'),
]

CULTURE = [
    'There are two Malays for "if" and "when", and both are right. People say «kalau» and «bila» when they talk; a message, a notice or a letter may say «jika» and «apabila». '
    'The same goes for «tetapi» and «namun», «jadi» and «oleh itu», «kemudian» and «seterusnya». In the scene Tanaka hears the difference himself: Mei Ling writes «Jika hujan, kita tangguhkan», and in speech they say «Kalau hujan, kita tangguhkan». '
    'Use the everyday word to speak and the standard word to write something formal.',
    'A plan can change in two ways, and Malay names them separately. «Tangguhkan» puts the plan off to another day (the hike moves to Sunday), and «batalkan» cancels it (the hike is off). '
    'A change of plan is easier to accept when you give the reason with «kerana» or «sebab» and a new choice: «Ada dua pilihan.» A «Janji!» is a light promise between friends, and the other person takes it seriously.',
    'General knowledge, not a rule and not a checked fact: friends and colleagues in Malaysia often arrange an outing in a group chat, and a message about a change usually gives the reason and the new plan in a few short lines. '
    'The plans in this course are fictional.',
    'Japanese learners often use one word for every reason. Keep them apart: «kerana» and «sebab» for ので・から, «supaya» for ように, and «walaupun» for のに. And a Japanese 〜たら, 〜ば, 〜なら and 〜と are all «kalau» in Malay.',
]
CULTURE_JA = [
    '「もし」と「〜するとき」にはマレー語が二通りあり、どちらも正しい言い方です。話すときは «kalau» と «bila»、メッセージ・掲示・手紙では «jika» と «apabila» を使うことがあります。'
    '«tetapi» と «namun»、«jadi» と «oleh itu»、«kemudian» と «seterusnya» も同じです。場面の中で田中さんもその違いに気づきます：メイリンさんは «Jika hujan, kita tangguhkan» と書き、話すときは «Kalau hujan, kita tangguhkan» と言います。'
    '話すときは日常の語を、改まって書くときは標準の語を使います。',
    '予定の変更には二通りあり、マレー語は別々の語で言います。«Tangguhkan» は別の日に延ばすこと（ハイキングを日曜日に延ばす）、«batalkan» は取りやめること（ハイキングは中止）です。'
    '予定を変えるときは、«kerana» か «sebab» で理由を言い、新しい選択肢を出すと受け入れられやすくなります：«Ada dua pilihan.» «Janji!» は友だち同士の軽い約束ですが、相手は本気で受け取ります。',
    '一般的な知識であり、規則でも確認済みの事実でもありません：マレーシアでは、友人や同僚がグループチャットで外出の約束をすることがよくあり、変更のメッセージは、理由と新しい予定を短い数行で伝えるのがふつうです。'
    'このコースの予定はすべて架空です。',
    '日本人の学習者は、理由をどれも同じ語で言いがちです。«kerana»・«sebab» は「ので・から」、«supaya» は「ように」、«walaupun» は「のに」と分けてください。また、日本語の「〜たら」「〜ば」「〜なら」「〜と」は、マレー語ではどれも «kalau» です。',
]

CFG = dict(
    chapter=14, label='14', unit_id='ms-c14',
    menu_title='Chapter 14 · Reasons, conditions and plans', genre='Plans',
    prerequisite_units=['ms-c13'], prereq_grammar=['ms-c13-g02', 'ms-c13-g04', 'ms-c11-g02', 'ms-c08-g02'],
    unit_goal='Give a reason, a condition, a purpose and a contrast, put a plan in order, and change a plan (put it off or cancel it) with a reason, in speech and in a short message.',
    core=CORE,
    recognition=[],
    revision=[('If, because, but', REV_JOIN), ('Weather and the hike', REV_WEATHER), ('The plan', REV_PLAN), ('Talking', REV_TALK)],
    core_groups=[('Joining ideas', JOIN), ('The order of a plan', ORDER), ('Plans and changes', PLANS)],
    grammar_ids={'kalau': 'ms-c14-g02', 'kerana': 'ms-c14-g03', 'supaya': 'ms-c14-g04', 'walaupun': 'ms-c14-g05', 'sambil': 'ms-c14-g06',
                 'urutan': 'ms-c14-g07', 'register': 'ms-c14-g08', 'words': 'ms-c14-g09'},
    grammar=['kalau', 'kerana', 'supaya', 'walaupun', 'sambil', 'urutan'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 22 cards ms-c14-001 to ms-c14-022', frame_list='ms-c14-f01 to f06', frame_list_ja='f01〜f06',
    extra=None,
    goals={'A': 'I can say a condition with «kalau», a reason with «kerana» or «sebab», a purpose with «supaya» and a contrast with «walaupun».',
           'B': 'I can plan a weekend outing with a friend: a rain plan, a reason I cannot come, a choice of two days and the order of the day.',
           'C': 'I can follow a phone call about a changed plan, read a message in written Malay, and put a plan off or cancel it with a reason.',
           'D': 'I can choose between «kalau» and «walaupun», «kerana» and «supaya», and between the everyday and the written words, and correct a short sentence.',
           'E': 'I can handle a short role-play about a changed outing, including a second change of plan.'},
    goals_ja={'A': '«kalau» で条件を、«kerana» か «sebab» で理由を、«supaya» で目的を、«walaupun» で対比を言える。',
              'B': '友だちと週末の外出の計画を立てられる：雨の日の計画、行けない理由、二つの日からの選択、一日の順序。',
              'C': '予定変更の電話が分かり、書き言葉のメッセージを読め、理由をつけて予定を延期・中止できる。',
              'D': '«kalau» と «walaupun»、«kerana» と «supaya»、日常の語と書き言葉の語を使い分け、短い文を直せる。',
              'E': '外出の変更についての短いロールプレイができ、もう一度の変更にも対応できる。'},
    setting='A weekday at the office in Kuala Lumpur: «Encik» Tanaka and «Cik» Mei Ling plan the weekend hike. The weather is cloudy, Mei Ling has to work on Saturday, so they move the hike to Sunday, agree a rain plan '
            'and write a message to their friends. All names, plans and times are fictional.',
    setting_ja='クアラルンプールの平日のオフィス。田中さんとメイリンさんが週末のハイキングの計画を立てます。空は曇りで、メイリンさんは土曜日に仕事があるので日曜日に延ばし、雨の日の計画を決めて友だちにメッセージを書きます。'
               '名前・計画・時刻はすべて架空です。',
    recall=['Without notes, from chapters 5, 7 and 13: say one thing you must do with «perlu», one question with «Kenapa …?» and its answer with «sebab», and one thing you have not done yet with «belum». / '
            '第5章・第7章・第13章の復習：«perlu» でしなければならないことを一つ、«Kenapa …?» の質問と «sebab» の答えを一組、«belum» でまだしていないことを一つ言いましょう。',
            'Recall prompt: «Saya perlu …» «Kenapa …?» «Sebab …» «Saya belum …»'],
    recall_key='e.g. «Saya perlu tulis mesej.» «Kenapa awak tidak datang?» «Sebab saya bekerja.» «Saya belum makan.» Then show the new step: «kalau» for if, «kerana» for because, «supaya» for so that and «walaupun» for although.',
    patterns=P, pattern_ids=['ms-c14-f01', 'ms-c14-f02', 'ms-c14-f03', 'ms-c14-f04', 'ms-c14-f05', 'ms-c14-f06'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 14 frames f01 to f06 (pattern 2 shows f02 and f03 together, reason and purpose).',
    pattern_keys=['Pattern 1: «kalau» + a clause, a comma, then the result. Check that no word for "then" follows the comma, that «tidak hujan» is the opposite condition, and that «bila» is "when" in speech. '
                  'Accept «jika» and «apabila» in a written line, and ask for «kalau» and «bila» when the learner speaks.',
                  'Pattern 2: «kerana» and «sebab» for the reason, «supaya» for the purpose. If a learner says «supaya» for a reason, give the situation (the reason for staying away) and ask which word fits. Accept «sebab» in speech.',
                  'Pattern 3: «walaupun» + a clause, a comma, then the surprising part, with no «tetapi» in the second clause. Check «walaupun hujan» (rain is no obstacle) against «kalau hujan» (a condition).',
                  'Pattern 4: «sambil» for two actions by one person at once; «semasa» and «sejak» as whole words. Check that both verbs stay plain.',
                  'Pattern 5: «mula-mula», «kemudian», «akhirnya» in order. Accept «seterusnya» in a written line and ask for «kemudian» in speech.'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 8, 11, 13),
    drills={
        'repeat_frame': 'Frame: «Kalau» [«hujan» / «tidak hujan»] «, kita» [«makan di kafe» / «mendaki»].',
        'repeat': ['«Kalau hujan, kita makan di kafe.»', '«Saya tidak datang kerana saya bekerja.»', '«Saya bangun awal supaya saya tidak lambat.»',
                   '«Walaupun hujan, saya mahu berjalan kaki.»', '«Dia makan sambil membaca surat khabar.»',
                   '«Mula-mula kita makan, kemudian kita berjalan kaki, akhirnya kita balik.»',
                   '«Jika hujan, kita tangguhkan. Apabila cuaca cerah, kita mendaki.»',
                   '«Kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.»'],
        'substitute': ['«Kalau hujan, kita makan di kafe.» (cue: «cuaca mendung», «berehat di rumah»)',
                       '«Saya tidak datang kerana saya bekerja.» (cue: «penat»)',
                       '«Saya datang awal supaya kita tidak lambat.» (cue: «bangun»)',
                       '«Walaupun hujan, saya mahu berjalan kaki.» (cue: «saya penat», «mendaki»)',
                       '«Dia makan sambil membaca surat khabar.» (cue: «bercakap dengan kawan»)',
                       '«Mula-mula kita berjumpa di stesen.» (cue: «makan»)',
                       '«Kita tangguhkan ke hari Ahad.» (cue: «hari Sabtu depan»)',
                       '«Saya janji saya datang awal.» (cue: «tulis mesej»)'],
        'transform': ['Written to everyday: «Jika hujan, kita tangguhkan.»', 'Written to everyday: «Apabila cuaca cerah, kita mendaki.»',
                      'Written to everyday: «Namun kita masih makan di kafe.»', 'Formal to everyday: «Oleh itu, kita tangguhkan rancangan itu ke hari Ahad.»',
                      'Formal to everyday: «Seterusnya kita mendaki.»',
                      'Join with «kerana»: «Saya tidak datang. Saya bekerja.»', 'Join with «supaya»: «Saya datang awal. Kita tidak lambat.»',
                      'Join with «walaupun»: «Hujan. Saya mahu berjalan kaki.»', 'Join with «sambil»: «Dia makan. Dia membaca surat khabar.»',
                      'Say the opposite condition with «kalau»: «Kalau hujan, kita makan di kafe.»'],
        'question and answer': ['«Kalau hujan, apa kita buat?» (cue: «makan di kafe»)', '«Kenapa awak tidak datang?» (cue: «bekerja»)',
                                '«Kenapa awak bangun awal?» (cue: «tidak lambat»)', '«Hujan. Awak masih mahu berjalan kaki?» (cue: «ya»)',
                                'You hear: «Dia makan sambil membaca surat khabar.» Ask the question («buat apa»).',
                                'You hear: «Mula-mula kita berjumpa di stesen pukul tujuh.» Ask the question («pukul berapa»).',
                                'You hear: «Ada dua pilihan: hari Ahad atau hari Sabtu depan.» Ask the question («berapa»).',
                                'You hear: «Kita tangguhkan ke hari Ahad.» Ask the question («hari apa»).'],
        'question-word choice': ['«___ awak tidak datang?» → «Sebab saya bekerja.»', '«Kita tangguhkan rancangan mendaki ke ___?» → «Ke hari Ahad.»',
                                 '«Ada ___ pilihan?» → «Dua pilihan.»', '«Kita berjumpa ___?» → «Di stesen.»',
                                 '«___ kita berjumpa?» → «Pukul tujuh.»', '«___ yang menulis mesej itu?» → «Cik Mei Ling.»',
                                 '«___ rancangan kita kalau hujan?» → «Kita makan di kafe.»', '«___ awak mendaki?» → «Bila cuaca cerah.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. After «kalau», «walaupun» and «jika» comes a clause and a comma; «kerana» and «supaya» come after the main clause; «sambil» joins two actions of one person; the sequence words come in order.',
                   'Cover the line and say it from the English: if it rains we eat at the cafe; I am not coming because I am working; I get up early so that I am not late; even though it is raining I want to walk; '
                   'he eats while reading the newspaper; first we eat, then we walk, finally we go home; if it rains we put it off, when the weather is clear we hike; we cancel the hike but we still eat at the cafe.'],
        'substitute': ['1 «Kalau cuaca mendung, kita berehat di rumah.» 2 «Saya tidak datang kerana saya penat.» 3 «Saya bangun awal supaya kita tidak lambat.» 4 «Walaupun saya penat, saya mahu mendaki.»',
                       '5 «Dia makan sambil bercakap dengan kawan.» 6 «Mula-mula kita makan.» 7 «Kita tangguhkan ke hari Sabtu depan.» 8 «Saya janji saya tulis mesej.»'],
        'transform': ['1 «Kalau hujan, kita tangguhkan.» 2 «Bila cuaca cerah, kita mendaki.» 3 «Tetapi kita masih makan di kafe.» 4 «Jadi, kita tangguhkan ke hari Ahad.» 5 «Kemudian kita mendaki.»',
                      '6 «Saya tidak datang kerana saya bekerja.» 7 «Saya datang awal supaya kita tidak lambat.» 8 «Walaupun hujan, saya mahu berjalan kaki.» '
                      '9 «Dia makan sambil membaca surat khabar.» 10 «Kalau tidak hujan, kita mendaki.»'],
        'question and answer': ['1 «Kalau hujan, kita makan di kafe.» 2 «Saya tidak datang kerana saya bekerja.» 3 «Saya bangun awal supaya saya tidak lambat.» 4 «Ya. Walaupun hujan, saya mahu berjalan kaki.»',
                                '5 «Dia makan sambil buat apa?» 6 «Mula-mula kita berjumpa di stesen pukul berapa?» 7 «Ada berapa pilihan?» 8 «Kita tangguhkan ke hari apa?»'],
        'question-word choice': ['1 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 2 «hari apa» 3 «berapa» 4 «di mana» 5 «Pukul berapa» 6 «Siapa» 7 «Apa» 8 «Bila»'],
    },
    short_dialogues=[
        ('Kalau hujan, kita buat apa?', 'Kalau hujan, kita makan di kafe.', 'planning the weekend'),
        ('Kenapa awak tidak datang?', 'Saya tidak datang kerana saya bekerja.', 'on the phone'),
        ('Boleh kita tangguhkan ke hari Ahad?', 'Boleh. Janji!', 'changing a plan'),
        ('Walaupun hujan, awak masih mahu mendaki?', 'Tidak. Kita batalkan rancangan mendaki, tetapi kita makan di kafe.', 'a second change')],
    short_keys=['1 «Baik. Kalau tidak hujan, kita mendaki.» 2 «Baik, terima kasih.»',
                '3 «Terima kasih. Saya tulis mesej untuk kawan kita.» 4 «Baik. Kita berjumpa di kafe pukul dua belas.»'],
    markers=dict(
        title='Markers with the plan verbs', grammar='kalau',
        instructions=['Say each sentence again with the marker in brackets. Keep the verb as the course teaches it; only the marker is added in front. / '
                      'かっこ内のマーカーを付けて言い直します。動詞はこのコースで教えた形のままで、前にマーカーを足すだけです。'],
        items=['«Saya menulis mesej itu.» (marker: «sudah»)', '«Kami berjumpa di stesen.» (marker: «akan»)',
               '«Dia membaca surat khabar.» (marker: «sedang»)', '«Kami mendaki.» (marker: «belum»)',
               '«Saya bekerja pada hari Sabtu.» (marker: «masih»)', '«Cik Mei Ling menulis mesej.» (marker: «baru»)',
               'Answer «Awak sudah menulis mesej?» (marker: «belum»)', '«Kami makan di kafe.» (marker: «akan»)'],
        bridge=['«sudah menulis» ≈ もう書いた · «akan berjumpa» ≈ 会う予定 · «sedang membaca» ≈ 読んでいるところ · '
                '«belum mendaki» ≈ まだ登っていない · «masih bekerja» ≈ まだ働いている · «baru menulis» ≈ 書いたばかり',
                'Japanese changes the verb ending (書いた / 書いていない); Malay puts the marker in front and keeps the verb («menulis»). «belum» is まだ〜ていない, «sudah» is もう〜た. / '
                '日本語は動詞の語尾が変わります。マレー語はマーカーを前に置き、動詞（«menulis»）はそのままです。«belum» は「まだ〜ていない」、«sudah» は「もう〜た」です。'],
        key=['1 «Saya sudah menulis mesej itu.» 2 «Kami akan berjumpa di stesen.» 3 «Dia sedang membaca surat khabar.» '
             '4 «Kami belum mendaki.»',
             '5 «Saya masih bekerja pada hari Sabtu.» 6 «Cik Mei Ling baru menulis mesej.» 7 «Belum. Saya belum menulis mesej.» '
             '8 «Kami akan makan di kafe.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、第14章の動詞と組み合わせて言います。«tangguhkan» と «batalkan» は、マーカーのあとには使わず、«kita» の文と依頼で使います。',
                 'Combine the chapter 4 markers with the chapter 14 verbs. «tangguhkan» and «batalkan» are not used after a marker; they stay in «kita» sentences and requests.')),
    question_note='Chapter 14 adds no new question word. The plan sentences fit every question you know: «Siapa yang menulis mesej itu?», '
                  '«Kita berjumpa di mana?», «Pukul berapa kita berjumpa?», «Ada berapa pilihan?», «Kenapa kita tangguhkan rancangan mendaki?» / '
                  '第14章で新しい疑問語は増えません。計画の文は知っている疑問語すべてと使えます：'
                  '«Siapa yang menulis mesej itu?»、«Kita berjumpa di mana?»、«Pukul berapa kita berjumpa?»、«Ada berapa pilihan?»、'
                  '«Kenapa kita tangguhkan rancangan mendaki?»',
    question_tasks=['Ask what you do if it rains. («apa»)', 'Ask who wrote the message. («siapa»)',
                    'Ask where you meet. («di mana»)', 'Ask formally whether the hike is still on. («Adakah»)',
                    'Ask politely whether you may move it to Sunday. («Bolehkah»)', 'Ask how many choices there are. («berapa»)',
                    'Ask when the hike starts. («bila»)', 'Ask what time you meet. («pukul berapa»)',
                    'Ask on what day you hike. («hari apa»)', 'Ask how you get to the station. («bagaimana»; spoken «macam mana»)',
                    'Ask why the hike is put off. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which day is better. («yang mana»)', 'Ask where you go after the hike. («ke mana»)',
                    'Ask where your friend is from. («dari mana»)', 'Ask how far the station is. («berapa jauh»)',
                    'Ask how long the hike is. («berapa lama»)', 'Ask how many cups of tea there are. («berapa» with a counter)',
                    'Ask who made the plan. («siapa» with «oleh»)'],
    question_keys=['1 «Kalau hujan, apa kita buat?» 2 «Siapa yang menulis mesej itu?» 3 «Kita berjumpa di mana?»',
                   '4 «Adakah kita masih mahu mendaki?» 5 «Bolehkah kita tangguhkan ke hari Ahad?» 6 «Ada berapa pilihan?»',
                   '7 «Bila kita mendaki?» 8 «Pukul berapa kita berjumpa?» 9 «Pada hari apa kita mendaki?»',
                   '10 «Bagaimana kita ke stesen?» (spoken: «Macam mana kita ke stesen?») 11 «Kenapa kita tangguhkan rancangan mendaki?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab hujan.» / «Kerana hujan.»',
                   '12 «Hari yang mana lebih baik?» 13 «Selepas mendaki, kita pergi ke mana?» 14 «Kawan awak dari mana?»',
                   '15 «Berapa jauh stesen?» 16 «Berapa lama mendaki?» 17 «Ada berapa cawan teh?»',
                   '18 «Rancangan ini dibuat oleh siapa?»'],
    listening=LISTENING,
    listening_context='On Friday «Encik» Tanaka telephones «Puan» Aini about the hike. / 金曜日、田中さんがアイニさんにハイキングについて電話します。',
    listening_before=['Predict: which of «kalau», «kerana», «supaya», «walaupun», «sambil» and «tangguhkan» will you hear? Write three guesses. / «kalau»・«kerana»・«supaya»・«walaupun»・«sambil»・«tangguhkan» のうち聞こえそうなものを三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['Why is the hike not on Saturday?', 'On which day is it now?', 'What do they do if it rains on that day?',
                      'Where do they meet, and when?', 'What do they do last?', 'Why does Aini come early?',
                      'What do they do while walking?', 'What does Aini ask at the end of the call, and what does Tanaka say to bring?', 'Who will Aini write to?'],
    listen_answers=['Mei Ling works on Saturday', 'Sunday', 'the hike is cancelled and they still eat at the cafe', 'at the station, at seven o\'clock',
                    'eat at the cafe', 'so that they are not late', 'talk', 'what to bring; water and an umbrella', 'Mei Ling'],
    listening_after=['Compare answers, then shadow lines 3, 5 and 8 after the teacher. / 答えを比べ、3・5・8行目をシャドーイングします。',
                     'Tell your partner in four sentences your own rain plan for the weekend, with «kalau», «kerana» and «supaya». / 週末の雨の日の計画を、«kalau»・«kerana»・«supaya» を使って4文でパートナーに話しましょう。'],
    test_listen=[(2, 'Mei Ling works on Saturday', ['bekerja', 'jadi', 'tangguhkan']),
                 (4, 'the hike is cancelled but they still eat at the cafe', ['kalau', 'batal', 'kafe']),
                 (6, 'at the station at seven, then hike, finally eat at the cafe', ['mula-mula', 'kemudian', 'akhirnya']),
                 (7, 'so that they are not late', ['supaya', 'awal', 'lambat']),
                 (8, 'they talk while walking', ['sambil', 'bercakap', 'berjalan']),
                 (10, 'water and an umbrella', ['bawa', 'air', 'payung'])],
    test_listen_prompts=['Why is the hike moved?', 'What happens if it rains?', 'What is the order of the day?',
                         'Why does Aini come early?', 'What do they do while walking?', 'What does Tanaka say to bring?'],
    reading_title='Reading and writing · A message about the hike',
    reading=['Fictional message from Mei Ling to the hiking group (written Malay; all names are invented):',
             '«Selamat pagi semua. Ada perubahan rancangan. Rancangan mendaki pada hari Sabtu batal kerana saya bekerja. Oleh itu, kita tangguhkan rancangan itu ke hari Ahad. '
             'Jika hujan pada hari Ahad, kita batalkan rancangan mendaki. Namun kita masih makan di kafe. Apabila cuaca cerah, kita mendaki. '
             'Mula-mula berjumpa di stesen pukul tujuh. Seterusnya mendaki. Akhirnya makan di kafe. Tujuan kita sama: berehat dan berjalan. Keputusan: hari Ahad. Janji!»',
             'Reply from a friend: «Baik. Saya datang awal supaya kita tidak lambat.»'],
    read_questions=['Why is the hike not on Saturday?', 'What is the new day?', 'What happens if it rains on that day?',
                    'What happens when the weather is clear?', 'Where do they meet first, and when?', 'What is the purpose of the day?',
                    'Which words in the message are the written words for "if", "when" and "however"?',
                    'Say in everyday Malay: "If it rains, we put it off."'],
    read_answers=['Mei Ling is working', 'Sunday', 'the hike is cancelled', 'they hike', 'at the station at seven o\'clock', 'to rest and to walk',
                  '«jika», «apabila», «namun»', '«Kalau hujan, kita tangguhkan.»'],
    write_instruction='Write four or five sentences to a friend: say that the plan has changed, give the reason, say the new day, say what you do if it rains and the order of the day. / '
                      '友だちにあてて4〜5文を書きましょう：予定が変わったこと、その理由、新しい日、雨の日の計画、一日の順序を書きます。',
    write_model='«Selamat petang. Ada perubahan rancangan. Kita tangguhkan makan malam ke hari Jumaat kerana saya bekerja pada hari Khamis. Kalau hujan, kita makan di rumah. Mula-mula kita berjumpa, kemudian kita makan, akhirnya kita berjalan. Janji!»',
    writing_type='message',
    task_title='Task · A changed outing',
    role_a=['Your information (fictional): you and B plan a Saturday outing (a hike, a picnic or a meal). You can come on Sunday, not on Saturday, because you work. You are afraid it will rain on Sunday.',
            'Say your reason with «kerana», give two choices, ask «Boleh kita tangguhkan ke hari …?», make a rain plan with «kalau», say the order with «mula-mula», «kemudian», «akhirnya» and make a promise with «Janji!».',
            'Aの情報（架空）：Bさんと土曜日の外出（ハイキング・ピクニック・食事）を計画します。仕事があるので土曜日は行けず、日曜日なら行けます。日曜日の雨が心配です。'
            '«kerana» で理由を言い、二つの選択肢を出し、«Boleh kita tangguhkan ke hari …?» とたずね、«kalau» で雨の日の計画を立て、«mula-mula»・«kemudian»・«akhirnya» で順序を言い、«Janji!» と約束します。'],
    role_b=['You are B (fictional). You like the plan. Ask why A cannot come, choose a day, ask what you do if it rains, and say you will write a message to your friends.',
            'Say what you will do «supaya» you are not late.',
            'Bです（架空）。計画が気に入っています。Aがなぜ来られないかをたずね、日を選び、雨が降ったらどうするかをたずね、友だちにメッセージを書くと言います。'
            '«supaya» を使って、遅れないために何をするかを言います。'],
    change=['Halfway, A says: «Maaf, hari Ahad pun hujan. Jadi, kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.» B answers with a reason or a promise and asks what time they meet: «Baik. Pukul berapa kita berjumpa di kafe?»',
            '途中でAが «Maaf, hari Ahad pun hujan. Jadi, kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.» と言います。Bは理由か約束で答え、何時に会うかをたずねます：«Baik. Pukul berapa kita berjumpa di kafe?»'],
    success=['☐ A gives a reason with «kerana» or «sebab» and a condition with «kalau».',
             '☐ B asks about the rain plan, and the two put the day in order with «mula-mula», «kemudian» and «akhirnya».',
             '☐ After the change A cancels with «batalkan», B asks the time, and one of them says «Janji!».'],
    task_key='«Kita ada dua pilihan: hari Sabtu atau hari Ahad.» — «Saya tidak boleh datang pada hari Sabtu kerana saya bekerja. Boleh kita tangguhkan ke hari Ahad?» — '
             '«Boleh. Tetapi kalau hujan, bagaimana?» — «Kalau hujan, kita makan di kafe.» — «Bagus. Mula-mula kita berjumpa di stesen. Kemudian kita berjalan. Akhirnya kita makan di kafe.» — '
             '«Saya datang awal supaya kita tidak lambat. Janji!» — Change: «Maaf, hari Ahad pun hujan. Jadi, kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.» — «Baik. Pukul berapa kita berjumpa di kafe?»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 14 card notes ms-c14-003 and -004 («jika» and «apabila» are formal or written, «kalau» and «bila» everyday), -006 («namun», written; «tapi» everyday), -007 («oleh itu», formal; «jadi» everyday), '
                    '-010 («seterusnya», formal; ‹lepas tu› everyday), -009 and -011 to -016 (whole words and roots), -018 to -022 («tangguh», «batal» and their ‹-kan› forms); scenario lines ms-c14-s13 and s14 (message language against speech); '
                    'Sam, 13 Nov 2026 («bila» for "when" is everyday, «apabila» is standard; no «keputusan» in casual turns). The sentence about group chats is general knowledge of working in Malaysia, labelled as such and not source-checked.',
    culture_prompt='In Japanese, how do you say the same plan to a friend and in a formal mail (たら, ので, ように)? Which Malay word fits each, and which is for speech and which for a message?',
    culture_explain=('「もし」「〜するとき」の日常の語と書き言葉の語、予定の延期と中止の違い、グループチャットの一般的な知識を読みます。日本語は未監修です。',
                     'Read about the everyday and the written words for if and when, the difference between putting a plan off and cancelling it, and the general custom of arranging outings in a group chat.'),
    quiz_words=['L-1201', 'L-1202', 'L-1209', 'L-1208', 'L-1213', 'L-1217'],
    quiz_meanings=['so that', 'although', 'first, at first', 'finally', 'purpose', 'so, therefore (everyday)'],
    grammar_quiz=[('Say in Malay: "If it rains, we eat at the cafe."', '«Kalau hujan, kita makan di kafe.»', ['kalau', 'hujan', 'kafe']),
                  ('Say in Malay: "I am not coming because I am working."', '«Saya tidak datang kerana saya bekerja.»', ['kerana', 'bekerja']),
                  ('Say in Malay: "I get up early so that I am not late."', '«Saya bangun awal supaya saya tidak lambat.»', ['supaya', 'lambat']),
                  ('Say in Malay: "First we meet, then we hike, finally we eat."', '«Mula-mula kita berjumpa, kemudian kita mendaki, akhirnya kita makan.»', ['mula-mula', 'akhirnya'])],
    test_reading=['Fictional message to the hiking group: «Jika hujan pada hari Ahad, kita batalkan rancangan mendaki. Namun kita masih makan di kafe. Apabila cuaca cerah, kita mendaki. '
                  'Mula-mula berjumpa di stesen. Seterusnya mendaki. Akhirnya makan di kafe.»'],
    reading_quiz=[('What happens if it rains?', 'the hike is cancelled', ['jika', 'batalkan']),
                  ('What do they do in any case?', 'eat at the cafe', ['namun', 'kafe']),
                  ('What do they do when the weather is clear?', 'hike', ['apabila', 'mendaki']),
                  ('What do they do last?', 'eat at the cafe', ['akhirnya', 'kafe'])],
    speaking_test='Plan an outing with a friend: give a reason with «kerana», make a rain plan with «kalau», say the order with «mula-mula», «kemudian» and «akhirnya», and put the plan off with «Boleh kita tangguhkan ke …?»',
    speaking_key='Check: «kalau» + a clause for the rain plan; «kerana» or «sebab» for the reason; the three sequence words in order; «tangguhkan» in a «kita» sentence or a question. '
                 'Accept «jika» and «apabila» only when the learner is reading a message aloud. Do not mark the everyday «kalau» and «bila» wrong in speech.',
    speaking_words=['kalau', 'kerana', 'mula-mula', 'akhirnya', 'tangguhkan'],
    plan={'A_recall': 'chapters 5, 7 and 13 («Kenapa …?» with «sebab», «perlu», «belum») from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first («kalau», «kerana» / «supaya»), question and answer before the rule; then the vocabulary in three groups with each whole word and its root '
                        '(joining ideas 10, the order of a plan 3, plans and changes 9). Draw the ladder: everyday «kalau», «bila», «tetapi», «jadi», «kemudian» beside the written «jika», «apabila», «namun», «oleh itu», «seterusnya».',
          'B_recall': 'say one reason with «kerana» and one condition with «kalau».',
          'B_drills': 'pattern table, substitution, transformation (written to everyday first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner says one rain plan and one reason for staying away.',
          'D_review': 'cumulative question-word drill (chapters 1 to 14), then the markers drill with new cues and a check of «kerana» against «supaya» and «kalau» against «walaupun».',
          'D_preview': 'the writing block after unit 14 (explain and rearrange a plan), then unit 15 (lost and found; Kata-Kata c15).',
          'E_recall': 'say three sentences about a weekend plan with «kalau», «kerana» and «supaya».',
          'E_listening': 'read the Kata-Kata scenario lines ms-c14-s01 to ms-c14-s15 (Tanaka and «Cik» Mei Ling plan the hike) twice; '
                         'learners tick «kalau», «kerana», «supaya», «walaupun», «sambil», «tangguhkan» and «batalkan» when they hear them, and listen for the message language in lines 13 and 14.',
          'E_roleplay': 'pairs play the same scene with their own fictional outing, reason and day, without the script.',
          'E_variation': 'a changed day: it rains on Sunday too; one cancels the outing, the other asks the time of the meal and makes a promise.'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 14 to the work and social scenes with plans and changes. '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: the writing block after unit 14 (explain and rearrange a plan), then the review block after chapter 15 and unit 15 (Kata-Kata c15).',
    teacher_notes=['Load: 22 core words in three groups (joining ideas 10, the order of a plan 3, plans and changes 9), no recognition word, and revision of if, because and but, weather and the hike, the plan and talking. '
                   'Suggested order: Block A the first group with patterns 1 and 2; Block B the second and third groups with patterns 3 to 5. '
                   'If the pilot shows 22 is too many, the natural cut is: «kalau» / «jika», «kerana», «supaya», «walaupun», «sambil», «mula-mula», «akhirnya», «tangguhkan», «batalkan», «pilihan» first; the rest second.',
                   'Written against spoken (Sam, 13 Nov 2026): the everyday words are what people say: «kalau», «bila» (for "when"), «tetapi» or spoken «tapi», «jadi», «kemudian» (spoken ‹lepas tu›, recognition only). The standard words are for a message or a notice: '
                   '«jika», «apabila», «namun», «oleh itu», «seterusnya». «bila» as "when" is everyday and «apabila» is standard. The scene models it in lines s13 and s14: do not correct «Kalau» or «bila» in speech and do not ask for «jika» in a conversation.',
                   '«kerana» (standard) or «sebab» (everyday) for the reason and «supaya» for the purpose; do not swap them. «walaupun» opens the first clause and takes no «tetapi» in the second; '
                   '«kalau hujan» (a condition) is not «walaupun hujan» (rain is no obstacle). «sambil» is two actions by one person; «semasa» and «sejak» are whole words.',
                   'Whole words and roots: «walaupun» (‹walau›), «akhirnya» (‹akhir› + ‹-nya›), «mula-mula» (repeated words come in Stage 3), «seterusnya» («terus»), «semasa» («masa»), «tujuan» (‹tuju›), «pilihan» («pilih»), '
                   '«keputusan» (‹putus›) and «perubahan» (‹ubah›) are each learned whole. «tangguh» and «batal» are the roots of «tangguhkan» and «batalkan» (cards ms-c14-018 to -022).',
                   'The ‹-kan› rule from chapter 12 (Sam): «tangguhkan» and «batalkan» appear in «kita» sentences and requests («Kita batalkan rancangan mendaki.», «Boleh kita tangguhkan ke hari Ahad?»), never after «sudah», «sedang», «belum», «akan», «baru» or «masih». '
                   'With a third-person doer the bare form is allowed for now (Sam, 13 Nov 2026): «Mei Ling tangguhkan rancangan mendaki ke hari Ahad.» A later chapter teaches the ‹meN-› forms (‹menangguhkan›, ‹membatalkan›) as the standard; do not teach them here. «Rancangan mendaki batal.» stays for the intransitive. No ‹meN-› + ‹-kan› form is taught.',
                   '«tangguhkan» and «batalkan» take a noun object, not a verb: «tangguhkan rancangan mendaki», «batalkan rancangan mendaki» (a verb such as «mendaki» does not follow them), and «Rancangan mendaki batal.» for the intransitive. '
                   'A written notice gives the object («Oleh itu, kita tangguhkan rancangan itu ke hari Ahad.»); a short spoken reply may drop it («Jika hujan, kita tangguhkan.», «Kita tangguhkan ke hari Ahad.»).',
                   '«kami» against «kita» (a common trap): «kami» leaves the listener out, «kita» includes the listener. A group-chat message or a notice goes to people who are going too, so it says «kita» («Kita tangguhkan ke hari Ahad. Namun kita masih makan di kafe.»). '
                   '«kami» fits an invitation to someone who has not yet said yes («Hujung minggu ini kami mahu mendaki. Puan Aini mahu datang?»); once she says yes, the plan is «kita». Japanese has one «私たち» for both, so learners mix them: the question is whether the listener goes too.',
                   '«keputusan» is a word for a written notice or a result («Keputusan: hari Ahad.»). The casual turns do not use ruling-style words: no «keputusan» in conversation. '
                   'The casual dialogue lines may use the everyday bare root after an aspect word, as Kata-Kata does («Saya sudah tulis mesej.»); the pattern examples, keys, notices and written texts use the ‹meN-› form («menulis»).',
                   'Where Japanese learners usually slip: (1) «supaya» for a reason, or «kerana» for a purpose (ので against ように); (2) «tetapi» in the second clause after «walaupun»; (3) a word for "then" after the comma of «kalau»; '
                   '(4) «bila» for "if" and «kalau» for "when"; (5) «jika» and «apabila» in speech, which sounds like a notice; (6) one verb in the «sambil» sentence given to two different people.',
                   'Natural speech: «Kalau», «bila», «tetapi», «jadi», «Janji!» and «Baik» in conversation; «jika», «apabila», «namun», «oleh itu», «seterusnya» in messages and notices. The casual lines keep «kita» and a short second sentence. '
                   'The scene follows Kata-Kata c14 (scenario lines ms-c14-s01 to s15, frames f01 to f06). All names, plans and times are fictional; learners may use an invented outing.',
                   'Cumulative question words: chapters 1 to 14. Chapter 14 adds no new question word.'],
)

EXTRA = dict(
    slug='writing-block', type='Reading and writing', sub_type='composition', kind='writing',
    title='Writing block · Explain and rearrange a plan',
    goal='I can write a short message that changes a plan: the reason, the new day, a rain plan and the order of the day, in six to eight sentences, in written Malay and then in speech.',
    grammar=['ms-c14-g02', 'ms-c14-g03', 'ms-c14-g04', 'ms-c14-g07', 'ms-c14-g08'],
    patterns=['ms-c14-f01', 'ms-c14-f02', 'ms-c14-f03', 'ms-c14-f06'],
    model=['Fictional model: two messages about the same change, one for a group chat (everyday) and one for a notice at the office (written). All names and plans are invented:',
           '«Selamat petang semua. Kita tangguhkan rancangan mendaki ke hari Ahad kerana saya bekerja pada hari Sabtu. Kalau hujan, kita makan di kafe. Mula-mula kita berjumpa di stesen pukul tujuh, kemudian kita mendaki, akhirnya kita makan di kafe. '
           'Saya datang awal supaya kita tidak lambat. Janji!»',
           '«Ada perubahan rancangan. Oleh itu, kita tangguhkan rancangan itu ke hari Ahad. Jika hujan, kita batalkan rancangan itu. Namun kita masih makan di kafe. Apabila cuaca cerah, kita mendaki. Keputusan: hari Ahad.»',
           'Notice: the reason first, then the new day, the rain plan and the order. The group chat says «kalau» and «bila»; the notice says «jika», «apabila», «namun» and «oleh itu». / '
           '気づくこと：理由、新しい日、雨の日の計画、順序の順に書きます。グループチャットは «kalau»・«bila»、掲示は «jika»・«apabila»・«namun»・«oleh itu» を使います。'],
    plan=['0–5 Recall: say a reason with «kerana», a condition with «kalau» and a purpose with «supaya» (unit 14).',
          '5–15 Model and notice: read the two messages; underline every connector and say which is everyday and which is written; rewrite «Jika hujan, kita batalkan rancangan itu» as speech.',
          '15–30 Guided draft: write your own message about a changed outing, first for a group chat, then as a short notice, with the checklist below.',
          '30–40 Peer or teacher feedback with the peer check.',
          '40–45 Rewrite one sentence from the group chat into the written style, and read the group-chat message aloud.',
          '0–5 復習・5–15 例文を読んで気づく・15–30 下書き・30–40 ペアまたは先生の確認・40–45 一文を書き直して音読。'],
    task=['Write six to eight sentences: a message to your group chat about a changed outing, then two sentences of the same news as a notice. Include:',
          '☐ the reason for the change («kerana» or «sebab»), and «Ada perubahan rancangan.»',
          '☐ the new day, with «tangguhkan» in a «kita» sentence («Kita tangguhkan … ke hari …»)',
          '☐ a rain plan with «kalau» («Kalau hujan, kita …»), and in the notice «jika»',
          '☐ the order of the day with «mula-mula», «kemudian» and «akhirnya», and a purpose with «supaya»',
          '________________________________________', '________________________________________',
          '________________________________________', '________________________________________',
          '予定が変わったことを知らせるグループチャットのメッセージと、同じ知らせを短い掲示にした二文を、6〜8文で書きましょう。変更の理由、新しい日、雨の日の計画、一日の順序、目的を入れます。'
          '名前・日・場所は架空でかまいません。'],
    check=['☐ «kerana» or «sebab» gives a reason, «supaya» a purpose (not the other way round).',
           '☐ A comma follows the «kalau», «jika» and «walaupun» clause, and no word for "then" follows it.',
           '☐ The group chat uses «kalau» and «bila»; the notice uses «jika», «apabila», «namun» or «oleh itu» (and not both in one text).',
           '☐ «tangguhkan» and «batalkan» are in «kita» sentences or a request, not after «sudah», «sedang», «belum» or «akan»; the partner can answer one question about the message.',
           '☐ 理由と目的の語、コンマ、日常の語と書き言葉の語の使い分け、«tangguhkan»・«batalkan» の使い方を確認し、パートナーが質問を一つします。'],
    answer='Any six to eight correct sentences that cover the checklist. Model: «Selamat petang semua. Kita tangguhkan rancangan mendaki ke hari Ahad kerana saya bekerja pada hari Sabtu. Kalau hujan, kita makan di kafe. '
           'Mula-mula kita berjumpa di stesen, kemudian kita mendaki, akhirnya kita makan di kafe. Saya datang awal supaya kita tidak lambat. Janji!» Notice: «Ada perubahan rancangan. Oleh itu, kita tangguhkan rancangan itu ke hari Ahad. Jika hujan, kita batalkan rancangan itu.»',
    key_extra=['Mark for the task first (the reason, the new day, the rain plan, the order, the purpose), then for form (the comma, the choice of everyday or written words, «tangguhkan» and «batalkan» in a «kita» sentence). '
               'Accept «jika» in the group chat in a first draft but ask for «kalau» once in the rewrite; accept the everyday bare root in a first draft («Kita tulis mesej») but ask for the ‹meN-› form in the notice.',
               'Names, days and places are fictional. Do not ask anyone to share a real address or phone number.'],
    explain=('ユニット14のあとの書く練習（45分）：予定の変更を、理由・新しい日・雨の日の計画・順序・目的を入れて6〜8文で書きます。グループチャットは日常の語、掲示は書き言葉の語で書き分けます。名前や日は架空でかまいません。',
             'The writing block after unit 14 (45 minutes): write a message that changes a plan in six to eight sentences, with a reason, the new day, a rain plan, the order of the day and a purpose, in everyday words for a group chat and in written words for a notice; names and days may be invented.'),
)

CFG['extra'] = EXTRA
UNIT = unit_dict(CFG)
