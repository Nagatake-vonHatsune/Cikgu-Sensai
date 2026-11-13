"""Unit 15: describing things and people with «yang»: the lost wallet at the station counter and the Japanese visitors Encik Rahman has to find
(___ saya hilang; Saya mencari ___ yang ada ___; Lelaki yang memakai ___; Beg itu berwarna ___ dan ada ___; Bentuknya ___, seperti ___;
Yang mana satu? Yang ___ atau yang ___?).

21 core ledger entries, the rows the ledger places in "Ch15 (unit 15)": the existing rows L-0591 «nombor plat», L-0618 «kulit» and L-0623 «beg tangan»,
the new rows L-1219 to L-1234, and L-1271 «memakai» and L-1272 «berwarna» (added by Sam, Journal row 184). They come in four groups: lost things (6),
parts and materials (5), colour, shape and likeness (6) and people and what they wear (4). No recognition word. The ber-, meN- and lexicalised words
(«berjalur», «berwarna», «memakai», «seperti», «bentuk», «jenama») are taught whole, each with its root as the Kata-Kata chapter 15 card notes give it.
The scene follows Kata-Kata c15 (scenario lines ms-c15-s01 to s17: Tanaka at the lost-property counter, then Tanaka describing the visitors to Encik Rahman)
word for word, and goes further in class: a second item, a second visitor, a form in written Malay. All names, items and times are fictional.

«hilang» (lost, cannot be found) is the chapter 15 word; ‹tertinggal› (left behind by accident) belongs to chapter 16 and is only named in a note.
«yang» is the connector Japanese does not need («dompet yang hitam» and «dompet hitam»); «memakai» covers glasses, clothes, a hat and shoes.
Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

LOST = ['L-1219', 'L-1233', 'L-1224', 'L-0623', 'L-0591', 'L-1234']
PARTS = ['L-0618', 'L-1223', 'L-1228', 'L-1222', 'L-1220']
LOOK = ['L-1272', 'L-1221', 'L-1225', 'L-1226', 'L-1227', 'L-1229']
PEOPLE = ['L-1230', 'L-1231', 'L-1232', 'L-1271']
CORE = LOST + PARTS + LOOK + PEOPLE

# Revision: words placed in chapters 1 to 14 that the unit really uses (a test fails if one is not used).
REV_DESCRIBE = ['L-0212', 'L-0279', 'L-0225', 'L-0234', 'L-0235', 'L-0226', 'L-0230', 'L-0237', 'L-0238', 'L-0146', 'L-0239', 'L-0144', 'L-0927']
REV_WEAR = ['L-0500', 'L-0501', 'L-0503', 'L-0371', 'L-0504', 'L-0563', 'L-0124', 'L-0421']
REV_PLACE = ['L-0295', 'L-0423', 'L-0332', 'L-0310', 'L-0313', 'L-0542', 'L-0060', 'L-0338']
REV_TALK = ['L-1133', 'L-1131', 'L-0478', 'L-0576', 'L-0379', 'L-0057', 'L-1009', 'L-1007']

EXAMPLES = {
    # Lost things
    'L-1219': '«Dompet saya hilang.»',
    'L-1233': '«Barang saya hilang di stesen.»',
    'L-1224': '«Saya mencari dompet saya.»',
    'L-0623': '«Beg tangan saya berwarna merah.»',
    'L-0591': '«Apa nombor plat kereta itu?»',
    'L-1234': '«Ada jenama?»',
    # Parts and materials
    'L-0618': '«Ini dompet kulit.»',
    'L-1223': '«Dompet itu ada satu poket kecil.»',
    'L-1228': '«Beg itu ada zip.»',
    'L-1222': '«Beg itu ada tali panjang.»',
    'L-1220': '«Apa ciri dompet itu?»',
    # Colour, shape and likeness
    'L-1272': '«Beg itu berwarna hitam.»',
    'L-1221': '«Dia memakai baju berjalur.»',
    'L-1225': '«Bentuknya segi empat.»',
    'L-1226': '«Cermin mata itu bulat.»',
    'L-1227': '«Dompet itu segi empat.»',
    'L-1229': '«Bentuknya segi empat, seperti kotak.»',
    # People and what they wear
    'L-1230': '«Lelaki itu memakai topi.»',
    'L-1231': '«Perempuan itu membawa beg tangan.»',
    'L-1232': '«Lelaki itu memakai cermin mata.»',
    'L-1271': '«Perempuan itu memakai baju berjalur.»',
    # Revision · describing
    'L-0212': '«Saya mencari beg yang ada zip.»',
    'L-0279': '«Dompet yang mana?»',
    'L-0225': '«Apa warna dompet itu?»',
    'L-0234': '«Dompet saya hitam.»',
    'L-0235': '«Lelaki itu memakai baju putih.»',
    'L-0226': '«Beg tangan perempuan itu merah.»',
    'L-0230': '«Beg itu berwarna biru.»',
    'L-0237': '«Beg itu besar.»',
    'L-0238': '«Dompet itu ada satu poket kecil.»',
    'L-0146': '«Beg itu ada tali panjang.»',
    'L-0239': '«Tali beg itu pendek.»',
    'L-0144': '«Lelaki itu tinggi.»',
    'L-0927': '«Rambut perempuan itu pendek.»',
    # Revision · clothes and papers
    'L-0500': '«Lelaki itu memakai baju putih.»',
    'L-0501': '«Dia memakai seluar hitam.»',
    'L-0503': '«Dia dengan seorang perempuan yang memakai topi.»',
    'L-0371': '«Dia memakai kasut putih.»',
    'L-0504': '«Mereka membawa beg yang ada tali panjang.»',
    'L-0563': '«Dia pakai topi.» (everyday; standard «memakai»)',
    'L-0124': '«Kad saya ada di dalam.»',
    'L-0421': '«Pasport saya tidak ada.»',
    # Revision · place and people
    'L-0295': '«Tetamu dari Jepun sudah sampai di stesen.»',
    'L-0423': '«Maaf, ini kaunter barang hilang?»',
    'L-0332': '«Dia di sebelah lif.»',
    'L-0310': '«Dia di sebelah lif.»',
    'L-0313': '«Dia dekat kaunter.»',
    'L-0542': '«Tetamu dari Jepun sudah sampai.»',
    'L-0060': '«Tetamu dari Jepun sudah sampai.»',
    'L-0338': '«Kereta itu berwarna putih.»',
    # Revision · talking
    'L-1133': '«Saya mencari dompet saya.»',
    'L-1131': '«Mereka membawa beg yang ada tali panjang.»',
    'L-0478': '«Saya tidak ingat jenamanya.»',
    'L-0576': '«Oh, saya sudah jumpa dia.»',
    'L-0379': '«Dompet saya hilang tadi.»',
    'L-0057': '«Ada zip dan satu poket kecil.»',
    'L-1009': '«Kenapa awak mencari beg itu?»',
    'L-1007': '«Bila dompet itu hilang?»',
}

# For the whole words and the affixed forms: the root as the Kata-Kata card note gives it, and the teaching point.
VOCAB_OPTS = {
    'L-1219': {'en': 'lost, missing: you cannot find it (for something left behind by accident chapter 16 teaches ‹tertinggal›); «Dompet saya hilang.» = my wallet is lost',
               'ja': 'なくなった・見つからない（うっかり置き忘れたときの ‹tertinggal› は第16章）；«Dompet saya hilang.»＝財布をなくした'},
    'L-1233': {'en': 'thing(s), belongings: «barang hilang» = lost property',
               'ja': '物・持ち物：«barang hilang»＝遺失物'},
    'L-0623': {'en': 'handbag («beg», chapter 8, + «tangan», chapter 6: learn it as a phrase)',
               'ja': 'ハンドバッグ（«beg»（第8章）＋ «tangan»（第6章）：一つの句として覚える）'},
    'L-0591': {'en': 'car number plate («nombor», chapter 3, + a second word: learn it as a phrase); useful for finding an e-hailing car',
               'ja': '車のナンバー（«nombor»（第3章）＋もう一語：一つの句として覚える）；配車アプリの車を探すときに役立つ'},
    'L-1234': {'en': 'brand («Ada jenama?» is what the counter asks)',
               'ja': 'ブランド（窓口で «Ada jenama?» とたずねられる）'},
    'L-0618': {'en': 'leather; also skin: «dompet kulit» = a leather wallet',
               'ja': '革；皮膚：«dompet kulit»＝革の財布'},
    'L-1220': {'en': 'feature, characteristic; forms often print it doubled, ‹ciri-ciri›: recognise both (repeated words come in Stage 3)',
               'ja': '特徴；書類では ‹ciri-ciri› と重ねて印刷されることが多い：どちらも分かればよい（重ね語は第3段階）'},
    'L-1272': {'en': 'coloured; to be (a colour) (‹ber-› + «warna», chapter 5): «berwarna hitam» = black; everyday «warna hitam» or «hitam» alone',
               'ja': '〜色の・〜色をしている（‹ber-›＋«warna»（第5章））：«berwarna hitam»＝黒い；日常は «warna hitam» や «hitam» だけでもよい'},
    'L-1221': {'en': 'striped (‹ber-› + ‹jalur›; the root is not taught alone): «baju berjalur» = a striped shirt',
               'ja': 'しま模様の（‹ber-›＋‹jalur›；語根は単独では教えない）：«baju berjalur»＝しまのシャツ'},
    'L-1225': {'en': 'shape; «bentuknya» = its shape (‹-nya›, chapter 2)',
               'ja': '形；«bentuknya»＝その形（‹-nya›、第2章）'},
    'L-1227': {'en': 'square or rectangular (four-sided); learn it as a phrase',
               'ja': '四角形（正方形も長方形も）；一つの句として覚える'},
    'L-1229': {'en': 'like, such as (standard; the everyday word is «macam», chapter 5, spoken): «seperti itu» = like that, «seperti ini» = like this; the spoken ‹macam tu› comes in chapter 17',
               'ja': '〜のような（標準；日常は «macam»（第5章、話し言葉））：«seperti itu»＝そのような、«seperti ini»＝このような；話し言葉の ‹macam tu› は第17章'},
    'L-1232': {'en': 'glasses («cermin», chapter 4, + «mata», chapter 4: learn it as a phrase)',
               'ja': 'めがね（«cermin»（第4章）＋«mata»（第4章）：一つの句として覚える）'},
    'L-1271': {'en': 'to wear; to use (‹me-› + «pakai», chapter 4: the p drops); one verb for glasses, clothes, a hat and shoes; everyday «pakai»',
               'ja': '着る・身につける・使う（‹me-›＋«pakai»（第4章）：pが落ちる）；めがね・服・帽子・靴に一つの動詞；日常は «pakai»'},
    'L-0563': {'en': 'to wear; to use (the everyday form from chapter 4: the standard form is «memakai»)',
               'ja': '着る・使う（第4章の日常の形：標準形は «memakai»）'},
}

P = [
    ('ms-c15-f02', '___ «saya hilang.»  (something of mine is lost)', [
        'A: «Maaf, apa yang hilang?» B: «Dompet saya hilang.»',
        'A: «Beg tangan awak hilang di mana?» B: «Beg tangan saya hilang di stesen.»',
        'A: «Kad awak pun hilang?» B: «Tidak. Kad saya ada, tetapi pasport saya hilang.»',
        'A: «Bila barang awak hilang?» B: «Barang saya hilang tadi.»',
        'A: «Maaf, ini kaunter barang hilang?» B: «Ya. Barang apa yang hilang, encik?»',
        'A: «Telefon awak hilang?» B: «Ya, telefon saya hilang. Tolong cari telefon saya.»'],
     "«___ saya hilang.» says that something of mine is lost: the thing first, then «saya» (my), then «hilang» (the Kata-Kata frame): «Dompet saya hilang.» «hilang» means you cannot find it. "
     "The thing is the subject: you do not say «saya hilang dompet». «barang hilang» is lost property, and «kaunter barang hilang» is the lost-property counter. "
     "Add where and when after the thing: «Beg tangan saya hilang di stesen.» «Barang saya hilang tadi.» Do not use «hilang» for something you left behind by accident; chapter 16 teaches that.",
     "«___ saya hilang.» は私の〜がなくなった、という意味です：物が先、次に «saya»（私の）、最後に «hilang»（Kata-Kata の文型）：«Dompet saya hilang.» «hilang» は見つからないことです。"
     "なくなった物が主語で、«saya hilang dompet» とは言いません。«barang hilang» は遺失物、«kaunter barang hilang» は遺失物の窓口です。"
     "場所や時はあとに足します：«Beg tangan saya hilang di stesen.» «Barang saya hilang tadi.» うっかり置き忘れたときには «hilang» を使いません。それは第16章で学びます。",
     'Japanese says 財布をなくした with a doer who loses it. Malay makes the wallet the subject: the wallet is lost. 私の財布 puts the owner first; Malay puts it after the thing: «dompet saya». A learner who says «saya hilang» has said that "I" am missing.',
     '日本語は「財布をなくした」と、なくした人を主語にして言います。マレー語は財布を主語にして「財布がなくなった」と言います。「私の財布」は持ち主が先ですが、マレー語は物のあとに «saya» を置きます：«dompet saya»。«saya hilang» と言うと、「私が行方不明だ」という意味になります。'),
    ('ms-c15-f01 and f03', '«Saya mencari» ___ «yang ada» ___ «.» / «Lelaki yang memakai» ___ «.»  (the thing or person that has / wears)', [
        'A: «Awak mencari apa?» B: «Saya mencari beg yang ada zip.»',
        'A: «Beg yang mana?» B: «Beg yang ada tali panjang.»',
        'A: «Siapa lelaki itu?» B: «Lelaki yang memakai cermin mata.»',
        'A: «Perempuan yang mana?» B: «Perempuan yang memakai topi.»',
        'A: «Awak mencari dompet yang mana?» B: «Dompet yang ada satu poket kecil.»',
        'A: «Tetamu kita yang mana?» B: «Lelaki yang memakai baju berjalur.»'],
     "Say the thing or the person first, then «yang», then a short clause that tells which one: «Saya mencari beg yang ada zip.» (the Kata-Kata frame) and «Lelaki yang memakai cermin mata.» (the Kata-Kata frame). "
     "«yang ada ___» says what the thing has, and «yang memakai ___» says what the person wears. «yang» is one word for \"who\", \"which\" and \"that\", for things and for people, and it stands between the noun and the description. "
     "The clause is short and has its own verb: «ada», «memakai», «membawa». Without «yang», «beg ada zip» is a whole sentence (the bag has a zip), not a description of the bag.",
     "まず物か人を言い、次に «yang»、そのあとに、どれかを示す短い節を置きます：«Saya mencari beg yang ada zip.»（Kata-Kata の文型）、«Lelaki yang memakai cermin mata.»（Kata-Kata の文型）。"
     "«yang ada ___» は持っているもの、«yang memakai ___» は身につけているものを言います。«yang» は「〜する（人・物）」にあたる一語で、物にも人にも使い、名詞と説明のあいだに置きます。"
     "節は短く、«ada»・«memakai»・«membawa» のような動詞を持ちます。«yang» がないと «beg ada zip» は「そのバッグはファスナーがある」という一つの文になり、バッグの説明にはなりません。",
     'Japanese puts the whole description before the noun: ファスナーが付いているバッグ, 眼鏡をかけている男性. Malay reverses it: the noun first, then «yang» and the clause: «beg yang ada zip», «lelaki yang memakai cermin mata». Japanese needs no linking word, so «yang» is the word learners forget.',
     '日本語は説明全体を名詞の前に置きます：「ファスナーが付いているバッグ」「眼鏡をかけている男性」。マレー語は逆で、名詞が先、次に «yang» と節：«beg yang ada zip»、«lelaki yang memakai cermin mata»。日本語には結ぶ語が要らないので、«yang» は忘れやすい語です。'),
    ('ms-c15-f04', '«Beg itu berwarna» ___ «dan ada» ___ «.»  (colour and features)', [
        'A: «Apa warna beg itu?» B: «Beg itu berwarna hitam dan ada tali panjang.»',
        'A: «Apa warna dompet itu?» B: «Hitam. Dompet kulit. Ada zip dan satu poket kecil.»',
        'A: «Baju lelaki itu berwarna apa?» B: «Baju itu putih dan berjalur.»',
        'A: «Topi perempuan itu berwarna apa?» B: «Topi itu berwarna merah.»',
        'A: «Beg itu besar atau kecil?» B: «Beg itu kecil dan berwarna biru.»',
        'A: «Apa lagi ciri beg itu?» B: «Ada zip dan dua poket.»'],
     "«berwarna» + a colour word gives the colour: «Beg itu berwarna hitam.» «dan ada ___» adds what it has: «Beg itu berwarna hitam dan ada tali panjang.» (the Kata-Kata frame). "
     "Ask the colour with «Apa warna ___ itu?» or «berwarna apa?». The colour word alone also works in everyday speech («Hitam.», «Beg itu hitam.», «warna hitam»). "
     "«berjalur» (striped) is learned whole. «ciri» is a feature: «Apa ciri beg itu?» «ada» names a feature the thing has: «ada zip», «ada satu poket kecil», «ada tali panjang». Two features are usually enough to find one bag.",
     "«berwarna» ＋色の語で色を言います：«Beg itu berwarna hitam.» «dan ada ___» で持っているものを足します：«Beg itu berwarna hitam dan ada tali panjang.»（Kata-Kata の文型）。"
     "色は «Apa warna ___ itu?» か «berwarna apa?» でたずねます。日常では色の語だけでもかまいません（«Hitam.»・«Beg itu hitam.»・«warna hitam»）。"
     "«berjalur»（しま模様の）は一語として覚えます。«ciri» は特徴です：«Apa ciri beg itu?» «ada» はその物が持つ特徴を言います：«ada zip»・«ada satu poket kecil»・«ada tali panjang»。バッグを見つけるには、特徴が二つあればたいてい十分です。",
     'Japanese has the adjective 黒い and the noun 黒色, and says バッグは黒で、ひもが長い with に・で・が. Malay says «berwarna hitam» (is black-coloured) and uses «ada» (has) for every feature where Japanese says 付き or 〜がある: ファスナー付き is «ada zip».',
     '日本語には形容詞の「黒い」と名詞の「黒色」があり、「バッグは黒で、ひもが長い」と言います。マレー語は «berwarna hitam» と言い、持っている特徴は日本語の「〜付き」「〜がある」にあたる «ada» で言います：「ファスナー付き」は «ada zip»。'),
    ('ms-c15-f06', '«Bentuknya» ___ «, seperti» ___ «.»  (shape and likeness; «seperti itu» and «seperti ini»)', [
        'A: «Bagaimana bentuk dompet itu?» B: «Bentuknya segi empat, seperti kotak.»',
        'A: «Bagaimana bentuk cermin mata itu?» B: «Bentuknya bulat, seperti jam.»',
        'A: «Seperti ini?» B: «Ya, seperti itu, tetapi ada zip.»',
        'A: «Dompet awak seperti ini?» B: «Tidak, bukan seperti ini. Dompet saya segi empat.»',
        'A: «Bagaimana bentuk meja di kafe itu?» B: «Bulat. Seperti pinggan besar.»',
        'A: «Beg itu seperti beg awak?» B: «Ya, seperti beg saya. Warna beg itu pun sama.»'],
     "«bentuk» is shape, and «bentuknya» (‹-nya›, chapter 2) is \"its shape\": «Bentuknya segi empat, seperti kotak.» (the Kata-Kata frame). «seperti» + a noun says what it looks like: «seperti kotak», «seperti jam». "
     "«seperti ini» is \"like this one\" (the thing is near the speaker or in the hand), and «seperti itu» is \"like that one\": «Seperti ini?» «Ya, seperti itu, tetapi ada zip.» (Kata-Kata lines). "
     "«seperti» is the standard word. In speech people say «macam» (chapter 5); the spoken ‹macam tu› for «seperti itu» comes in chapter 17, so this unit only names it. «segi empat» and «bulat» tell the shape: four-sided or round.",
     "«bentuk» は形、«bentuknya»（‹-nya›、第2章）は「その形」です：«Bentuknya segi empat, seperti kotak.»（Kata-Kata の文型）。«seperti» ＋名詞で何に似ているかを言います：«seperti kotak»・«seperti jam»。"
     "«seperti ini» は「これのような」（話し手の近くや手にある物）、«seperti itu» は「それのような」です：«Seperti ini?» «Ya, seperti itu, tetapi ada zip.»（Kata-Kata の文）。"
     "«seperti» は標準の語です。話すときは «macam»（第5章）を使い、«seperti itu» にあたる話し言葉の ‹macam tu› は第17章なので、このユニットでは名前だけ出します。«segi empat» と «bulat» は形を言います：四角か丸です。",
     'Japanese 〜のような and 〜みたい both mean «seperti»; そのような is «seperti itu» and このような is «seperti ini». Japanese says 形は四角で、箱のようです with a ような that changes form; Malay keeps «seperti» as it is and puts the noun after it.',
     '日本語の「〜のような」「〜みたい」はどちらも «seperti» です。「そのような」は «seperti itu»、「このような」は «seperti ini»。日本語は「箱のようです」と「ような」が形を変えますが、マレー語は «seperti» の形を変えず、あとに名詞を置きます。'),
    ('ms-c15-f05', '«Yang mana satu? Yang» ___ «atau yang» ___ «?»  (which one of two)', [
        'A: «Yang mana satu? Yang ada zip atau yang tidak ada zip?» B: «Yang ada zip.»',
        'A: «Beg yang mana? Yang besar atau yang kecil?» B: «Yang kecil.»',
        'A: «Lelaki yang mana? Yang memakai topi atau yang memakai cermin mata?» B: «Yang memakai cermin mata.»',
        'A: «Yang mana satu? Yang berwarna hitam atau yang berwarna biru?» B: «Yang berwarna biru. Yang itu!»',
        'A: «Perempuan yang mana? Yang tinggi atau yang pendek?» B: «Yang tinggi.»',
        'A: «Yang mana satu, encik?» B: «Yang itu! Yang ada zip.»'],
     "«Yang mana satu?» asks which one of two or more things or people. Offer the choice with «Yang ___ atau yang ___?» (the Kata-Kata frame): «Yang ada zip atau yang tidak ada zip?» "
     "The answer is «Yang» + the feature, and the noun is left out because it is already clear: «Yang ada zip.» «Yang itu!» points at the one. «tidak ada» is the opposite of «ada»: «yang tidak ada zip». "
     "«yang mana» was taught in chapter 6; now it picks one by its description.",
     "«Yang mana satu?» は、二つ以上の中からどれかをたずねます。«Yang ___ atau yang ___?»（Kata-Kata の文型）で選択肢を出します：«Yang ada zip atau yang tidak ada zip?» "
     "答えは «Yang» ＋特徴で、名詞は分かっているので省きます：«Yang ada zip.» «Yang itu!» はその一つを指します。«tidak ada» は «ada» の反対です：«yang tidak ada zip»。"
     "«yang mana» は第6章で学びました。ここでは特徴で一つを選びます。",
     'Japanese asks どれ? and answers with の: 黒いの, ファスナー付きのやつ. Malay does the same with «yang»: «yang hitam», «yang ada zip». The Japanese の (the one) is «yang», and the noun can be dropped after it.',
     '日本語は「どれ？」とたずね、「の」で答えます：「黒いの」「ファスナー付きのやつ」。マレー語も «yang» で同じことをします：«yang hitam»・«yang ada zip»。日本語の「の」（その物）にあたるのが «yang» で、そのあとの名詞は省けます。'),
]

# The Kata-Kata scenario lines ms-c15-s01 to s17 are the model conversation. Turn 11 joins s11 and s12 (Tanaka thanks the staff, then rings Encik Rahman),
# so the whole scene fits the 16 turns the charter allows.
DIALOGUE = [
    ('Tanaka', 'Maaf, ini kaunter barang hilang? Saya mencari dompet saya.'),
    ('Staff', 'Ya, encik. Dompet yang mana? Apa warna dompet itu?'),
    ('Tanaka', 'Hitam. Dompet kulit. Ada zip dan satu poket kecil.'),
    ('Staff', 'Ada jenama?'),
    ('Tanaka', 'Saya tidak ingat jenamanya. Bentuknya segi empat, seperti kotak kecil.'),
    ('Staff', 'Seperti ini?'),
    ('Tanaka', 'Ya, seperti itu, tetapi ada zip.'),
    ('Staff', 'Ada dua dompet hitam di sini. Yang mana satu? Yang ada zip atau yang tidak ada zip?'),
    ('Tanaka', 'Yang ada zip. Yang itu! Kad saya ada di dalam, tetapi pasport saya tidak ada.'),
    ('Staff', 'Betul, ada kad encik di dalam. Ini dompet encik.'),
    ('Tanaka', 'Terima kasih banyak! Encik Rahman, tetamu dari Jepun sudah sampai di stesen.'),
    ('Rahman', 'Saya tidak tahu siapa dia. Lelaki yang mana?'),
    ('Tanaka', 'Lelaki yang memakai cermin mata dan baju berjalur. Dia dengan seorang perempuan yang memakai topi. Mereka membawa beg yang ada tali panjang.'),
    ('Rahman', 'Dia di mana sekarang?'),
    ('Tanaka', 'Dia dekat kaunter, di sebelah lif.'),
    ('Rahman', 'Oh, saya sudah jumpa dia.'),
]
# Changed facts: Mei Ling has lost a handbag; the counter has two red bags.
VARIANT = [
    ('Mei Ling', 'Maaf, ini kaunter barang hilang? Beg tangan saya hilang.'),
    ('Staff', 'Beg tangan yang mana? Apa warna beg itu?'),
    ('Mei Ling', 'Merah. Beg tangan kulit. Ada dua poket dan tali panjang.'),
    ('Staff', 'Ada jenama?'),
    ('Mei Ling', 'Ada, tetapi saya tidak ingat jenamanya. Bentuknya segi empat, seperti kotak besar.'),
    ('Staff', 'Seperti ini?'),
    ('Mei Ling', 'Ya, seperti itu, tetapi tidak ada zip.'),
    ('Staff', 'Ada dua beg merah di sini. Yang mana satu? Yang ada poket atau yang ada tali panjang?'),
    ('Mei Ling', 'Yang ada tali panjang. Yang itu!'),
    ('Staff', 'Betul. Ini beg tangan puan.'),
]
LISTENING = [
    ('Rahman', 'Encik Tanaka, saya sudah di stesen. Tetamu yang mana satu?'),
    ('Tanaka', 'Ada dua orang, seorang lelaki dan seorang perempuan. Lelaki itu tinggi. Dia memakai baju putih, seluar hitam dan kasut hitam.'),
    ('Rahman', 'Lelaki yang memakai cermin mata?'),
    ('Tanaka', 'Bukan. Dia tidak memakai cermin mata. Dia memakai topi.'),
    ('Rahman', 'Perempuan itu pula?'),
    ('Tanaka', 'Perempuan itu memakai baju berjalur. Rambut perempuan itu pendek. Dia membawa beg tangan yang berwarna merah.'),
    ('Rahman', 'Beg tangan itu bulat atau segi empat?'),
    ('Tanaka', 'Bentuknya segi empat, seperti kotak kecil. Ada zip dan satu poket.'),
    ('Rahman', 'Mereka naik kereta?'),
    ('Tanaka', 'Ya. Kereta itu berwarna putih. Saya tidak ingat nombor plat kereta itu, tetapi nombor plat ada dalam mesej saya.'),
    ('Rahman', 'Baik. Ada dua lelaki dekat lif. Yang mana satu? Yang memakai topi atau yang memakai cermin mata?'),
    ('Tanaka', 'Yang memakai topi. Dia dengan perempuan yang memakai baju berjalur.'),
    ('Rahman', 'Oh, saya sudah jumpa mereka. Terima kasih, encik.'),
]

CULTURE = [
    'In Japanese the description comes before the noun: 黒い財布, 眼鏡をかけている男性. Malay puts the noun first and the description after it: «dompet hitam», «lelaki yang memakai cermin mata». '
    'A single adjective can follow the noun by itself, while a clause with a verb or «ada» needs «yang» («beg yang ada zip»). «yang» also stands for "the one" when the noun is left out: «Yang ada zip.»',
    'At a lost-property counter people start with what can be seen, not with a brand: the colour, the material, the shape and one small feature such as a zip or a pocket. '
    'Staff often hold something up and ask «Seperti ini?» A good answer says «Ya, seperti itu, tetapi …» and names the difference. One clear difference helps the counter more than a plain "no".',
    'General knowledge, not a rule and not a checked fact: stations, offices and shopping centres in Malaysia often have a counter for lost property, and staff may ask for a description and a form before they hand something back. '
    'What each place asks for differs, so ask at the counter. The items, places and times in this course are fictional.',
    'Japanese learners often drop «yang» before «ada» or a verb, or put the description before the noun as in Japanese. They may also add «yang» to every adjective. «dompet hitam» and «dompet yang hitam» are both heard, '
    'but «beg yang ada zip» needs «yang». And one verb, «memakai», covers glasses, clothes, a hat and shoes, where Japanese changes the verb each time.',
]
CULTURE_JA = [
    '日本語では説明が名詞の前に来ます：「黒い財布」「眼鏡をかけている男性」。マレー語は名詞が先で、説明があとに来ます：«dompet hitam»、«lelaki yang memakai cermin mata»。'
    '形容詞が一つなら名詞のすぐあとに置けますが、動詞や «ada» のある節には «yang» が要ります（«beg yang ada zip»）。名詞を省くと、«yang» は「その一つ」にもなります：«Yang ada zip.»',
    '遺失物の窓口では、ブランドからではなく、目に見えること、つまり色・材料・形、そしてファスナーやポケットのような小さな特徴から話します。'
    '窓口の人が物を見せて «Seperti ini?» とたずねることもよくあります。良い答えは «Ya, seperti itu, tetapi …» と違いを言うことです。はっきりした違いを一つ言うほうが、ただ「違います」と言うより窓口の助けになります。',
    '一般的な知識であり、規則でも確認済みの事実でもありません：マレーシアの駅・会社・ショッピングセンターには遺失物の窓口があることが多く、物を返す前に、特徴をたずねたり書類を書かせたりすることがあります。'
    '場所によって違うので、窓口で聞いてください。このコースの物・場所・時刻はすべて架空です。',
    '日本人の学習者は、«ada» や動詞の前の «yang» を落としたり、日本語のように説明を名詞の前に置いたりしがちです。形容詞ごとに «yang» を付けすぎることもあります。«dompet hitam» も «dompet yang hitam» も聞かれますが、'
    '«beg yang ada zip» には «yang» が要ります。また、めがね・服・帽子・靴のどれにも、日本語は動詞を変えますが、マレー語は «memakai» の一語です。',
]

CFG = dict(
    chapter=15, label='15', unit_id='ms-c15',
    menu_title='Chapter 15 · Describing things and people', genre='Lost property',
    prerequisite_units=['ms-c14'], prereq_grammar=['ms-c14-g02', 'ms-c14-g03', 'ms-c13-g02', 'ms-c06-g02'],
    unit_goal='Say that something of yours is lost, describe it by colour, shape and features, say which one with «yang», and describe a person by what they wear, at a lost-property counter and at a station.',
    core=CORE,
    recognition=[],
    revision=[('Describing: colour, size and which one', REV_DESCRIBE), ('Clothes and papers', REV_WEAR), ('Places and people', REV_PLACE), ('Talking', REV_TALK)],
    core_groups=[('Lost things', LOST), ('Parts and materials', PARTS), ('Colour, shape and likeness', LOOK), ('People and what they wear', PEOPLE)],
    grammar_ids={'hilang': 'ms-c15-g02', 'yang': 'ms-c15-g03', 'warna': 'ms-c15-g04', 'bentuk': 'ms-c15-g05', 'mana': 'ms-c15-g06',
                 'memakai': 'ms-c15-g07', 'drop': 'ms-c15-g08', 'words': 'ms-c15-g09'},
    grammar=['hilang', 'yang', 'warna', 'bentuk', 'mana', 'memakai'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 21 cards ms-c15-001 to ms-c15-021', frame_list='ms-c15-f01 to f06', frame_list_ja='f01〜f06',
    extra=None,
    goals={'A': 'I can say that something of mine is lost and describe it with «yang», a colour and a feature.',
           'B': 'I can describe a wallet or a bag by colour, shape and features, and say which one with «Yang mana satu?».',
           'C': 'I can follow a call that describes two visitors, read a lost-property form and tell a person by what they wear.',
           'D': 'I can decide when «yang» is needed, use «memakai» for what people wear, and correct a short description.',
           'E': 'I can handle a short role-play at a lost-property counter or at a station, including a second item that looks the same.'},
    goals_ja={'A': '自分の物がなくなったことを言い、«yang»・色・特徴で説明できる。',
              'B': '財布やバッグを色・形・特徴で説明し、«Yang mana satu?» でどれかを言える。',
              'C': '訪問客を二人説明する電話が分かり、遺失物の書類を読み、身につけているもので人を見分けられる。',
              'D': '«yang» が要るかどうかを判断し、身につけるものに «memakai» を使い、短い説明を直せる。',
              'E': '遺失物の窓口や駅での短いロールプレイができ、よく似た二つ目の物にも対応できる。'},
    setting='A weekday at the station in Kuala Lumpur: «Encik» Tanaka has lost his wallet and describes it at the lost-property counter. Then he tells «Encik» Rahman which of the Japanese visitors to look for, '
            'by what they wear and carry. All names, items and times are fictional.',
    setting_ja='クアラルンプールの駅の平日。田中さんは財布をなくし、遺失物の窓口で特徴を説明します。そのあと、日本からの訪問客のうちどの人を迎えればよいかを、身につけているものや持ち物でラーマンさんに伝えます。'
               '名前・物・時刻はすべて架空です。',
    recall=['Without notes, from chapters 5, 8 and 14: name a colour and a piece of clothing («Baju saya …»), say one thing with a counter («Ada dua …») and give one reason with «kerana». / '
            '第5章・第8章・第14章の復習：色と服を一つ言い（«Baju saya …»）、助数詞を使った文を一つ言い（«Ada dua …»）、«kerana» で理由を一つ言いましょう。',
            'Recall prompt: «Baju saya berwarna …» «Ada dua …» «Saya … kerana …»'],
    recall_key='e.g. «Baju saya berwarna biru.» «Ada dua beg.» «Saya tidak datang kerana saya bekerja.» Then show the new step: «hilang» for lost, «yang» for which one, «berwarna» for colour and «seperti» for likeness.',
    patterns=P, pattern_ids=['ms-c15-f01', 'ms-c15-f02', 'ms-c15-f03', 'ms-c15-f04', 'ms-c15-f05', 'ms-c15-f06'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 15 frames f01 to f06 (pattern 2 shows f01 and f03 together, the thing or person that has or wears; the patterns run f02, f01 and f03, f04, f06, f05).',
    pattern_keys=['Pattern 1: the thing comes first, then «saya», then «hilang». If a learner says «saya hilang dompet», give the situation (a wallet that cannot be found) and ask who or what is lost. '
                  'Accept «hilang» for something you cannot find; if a learner means something left behind by accident, say that chapter 16 has a word for it.',
                  'Pattern 2: the noun, then «yang», then a short clause with «ada», «memakai» or «membawa». Check that «yang» is not left out before «ada» or a verb, and that the description is not put before the noun.',
                  'Pattern 3: «berwarna» + a colour, then «dan ada» + a feature. Accept «hitam» or «warna hitam» in a quick answer. Check «apa warna» for the question.',
                  'Pattern 4: «bentuknya» + «segi empat» or «bulat», then «seperti» + a noun; «seperti ini» for the thing in front of you and «seperti itu» for the one that is not. Accept «macam» in speech; do not teach ‹macam tu› yet.',
                  'Pattern 5: «Yang mana satu?» then «Yang ___ atau yang ___?». The answer is «Yang» + a feature, with no noun. Check that «tidak ada» is the opposite of «ada».'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 7, 11, 13),
    drills={
        'repeat_frame': 'Frame: «Saya mencari» [«beg» / «dompet»] «yang ada» [«zip» / «tali panjang»] «.»',
        'repeat': ['«Dompet saya hilang.»', '«Saya mencari beg yang ada zip.»', '«Lelaki yang memakai cermin mata.»',
                   '«Beg itu berwarna hitam dan ada tali panjang.»', '«Yang mana satu? Yang ada zip atau yang tidak ada zip?»',
                   '«Bentuknya segi empat, seperti kotak.»', '«Ya, seperti itu, tetapi ada zip.»',
                   '«Dia dengan seorang perempuan yang memakai topi.»'],
        'substitute': ['«Saya mencari beg yang ada zip.» (cue: «dompet», «satu poket kecil»)',
                       '«Dompet saya hilang.» (cue: «beg tangan»)',
                       '«Lelaki yang memakai cermin mata.» (cue: «perempuan», «topi»)',
                       '«Beg itu berwarna hitam dan ada tali panjang.» (cue: «dompet», «biru», «zip»)',
                       '«Bentuknya segi empat, seperti kotak.» (cue: «bulat», «jam»)',
                       '«Yang ada zip atau yang tidak ada zip?» (cue: «yang besar», «yang kecil»)',
                       '«Dia memakai baju berjalur.» (cue: «seluar hitam», «kasut putih»)',
                       '«Saya tidak ingat jenamanya.» (cue: «warna»)'],
        'transform': ['Join with «yang»: «Saya mencari beg. Beg itu ada tali panjang.»',
                      'Join with «yang»: «Saya jumpa seorang perempuan. Perempuan itu memakai topi.»',
                      'Join with «yang»: «Lelaki itu tinggi. Lelaki itu memakai cermin mata.» (say who: the tall one)',
                      'Say it with «berwarna»: «Beg itu hitam.»',
                      'Say it with «seperti»: «Bentuk dompet itu segi empat. Kotak pun segi empat.»',
                      'Say the opposite: «Beg itu ada zip.» (use «tidak ada»)',
                      'Say only the one you mean: «Dompet yang ada zip.» (leave out the noun)',
                      'Make it a question: «Dompet itu berwarna hitam.» (ask the colour)',
                      'Make it a question: «Ada dua dompet hitam di sini.» (ask which one)',
                      'Say it with «sudah»: «Dompet saya hilang.»'],
        'question and answer': ['«Apa warna dompet itu?» (cue: «hitam»)',
                                '«Dompet itu ada apa?» (cue: «zip», «satu poket kecil»)',
                                '«Ada jenama?» (cue: «tidak ingat»)',
                                '«Bagaimana bentuknya?» (cue: «segi empat», «kotak»)',
                                'You hear: «Dia memakai baju berjalur.» Ask the question («siapa»).',
                                'You hear: «Lelaki yang memakai cermin mata ada di sebelah lif.» Ask the question («di mana»).',
                                'You hear: «Beg itu berwarna biru.» Ask the question («apa warna»).',
                                'You hear: «Ada dua dompet hitam di sini.» Ask the question («yang mana»).'],
        'question-word choice': ['«___ warna dompet itu?» → «Hitam.»', '«___ satu? Yang ada zip atau yang tidak ada zip?» → «Yang ada zip.»',
                                 '«Dompet itu hilang ___?» → «Di stesen.»', '«___ dompet itu hilang?» → «Tadi pagi.»',
                                 '«Ada ___ dompet hitam di sini?» → «Dua.»', '«___ yang memakai topi?» → «Perempuan itu.»',
                                 '«Tetamu itu dari ___?» → «Dari Jepun.»', '«___ awak mencari beg itu?» → «Sebab kad saya ada di dalam.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. «yang» comes after the noun and before the clause; «hilang» comes last in «___ saya hilang»; «berwarna» is followed by the colour; «seperti» is followed by a noun.',
                   'Cover the line and say it from the English: my wallet is lost; I am looking for a bag that has a zip; the man who wears glasses; the bag is black and has a long strap; which one, the one with a zip or the one without; '
                   'its shape is rectangular, like a box; yes, like that one, but it has a zip; he is with a woman who wears a hat.'],
        'substitute': ['1 «Saya mencari dompet yang ada satu poket kecil.» 2 «Beg tangan saya hilang.» 3 «Perempuan yang memakai topi.» 4 «Dompet itu berwarna biru dan ada zip.»',
                       '5 «Bentuknya bulat, seperti jam.» 6 «Yang besar atau yang kecil?» 7 «Dia memakai seluar hitam.» (and «Dia memakai kasut putih.») 8 «Saya tidak ingat warnanya.»'],
        'transform': ['1 «Saya mencari beg yang ada tali panjang.» 2 «Saya jumpa seorang perempuan yang memakai topi.» 3 «Lelaki yang tinggi memakai cermin mata.» (or «Lelaki yang memakai cermin mata itu tinggi.») '
                      '4 «Beg itu berwarna hitam.» 5 «Bentuk dompet itu segi empat, seperti kotak.»',
                      '6 «Beg itu tidak ada zip.» 7 «Yang ada zip.» 8 «Apa warna dompet itu?» 9 «Yang mana satu?» 10 «Dompet saya sudah hilang.»'],
        'question and answer': ['1 «Hitam.» 2 «Ada zip dan satu poket kecil.» 3 «Saya tidak ingat jenamanya.» 4 «Bentuknya segi empat, seperti kotak.»',
                                '5 «Siapa yang memakai baju berjalur?» 6 «Lelaki yang memakai cermin mata ada di mana?» 7 «Apa warna beg itu?» 8 «Yang mana satu?»'],
        'question-word choice': ['1 «Apa» 2 «Yang mana» 3 «di mana» 4 «Bila» 5 «berapa» 6 «Siapa» 7 «dari mana» 8 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana»)'],
    },
    short_dialogues=[
        ('Maaf, ini kaunter barang hilang?', 'Ya. Apa yang hilang?', 'at the counter'),
        ('Apa warna beg itu?', 'Beg itu berwarna biru.', 'describing a bag'),
        ('Seperti ini?', 'Ya, seperti itu, tetapi ada zip.', 'checking an item'),
        ('Lelaki yang mana?', 'Lelaki yang memakai cermin mata.', 'finding a visitor')],
    short_keys=['1 «Dompet saya hilang. Saya mencari dompet saya.» 2 «Ada tali panjang dan satu poket.»',
                '3 «Betul. Ini beg saya.» 4 «Dia dekat kaunter, di sebelah lif.»'],
    markers=dict(
        title='Markers with the lost-property verbs', grammar='hilang',
        instructions=['Say each sentence again with the marker in brackets. Keep the verb as the course teaches it; only the marker is added in front. / '
                      'かっこ内のマーカーを付けて言い直します。動詞はこのコースで教えた形のままで、前にマーカーを足すだけです。'],
        items=['«Dompet saya hilang.» (marker: «sudah»)', '«Dia memakai cermin mata.» (marker: «sedang»)',
               '«Saya mencari beg tangan itu.» (marker: «masih»)', '«Encik Rahman menunggu tetamu.» (marker: «akan»)',
               '«Encik Tanaka mengambil dompet itu.» (marker: «baru»)', 'Answer «Awak sudah jumpa beg awak?» (marker: «belum»)',
               '«Mereka membawa beg yang ada tali panjang.» (marker: «sedang»)', '«Perempuan itu memakai topi.» (marker: «masih»)'],
        bridge=['«sudah hilang» ≈ もうなくなった · «sedang memakai» ≈ 身につけているところ · «masih mencari» ≈ まだ探している · '
                '«akan menunggu» ≈ 待つ予定 · «baru mengambil» ≈ 取ったばかり · «belum jumpa» ≈ まだ見つかっていない',
                'Japanese changes the verb ending (なくなった / まだ見つかっていない); Malay puts the marker in front and keeps the verb («memakai»). «belum» is まだ〜ていない, «sudah» is もう〜た. / '
                '日本語は動詞の語尾が変わります。マレー語はマーカーを前に置き、動詞（«memakai»）はそのままです。«belum» は「まだ〜ていない」、«sudah» は「もう〜た」です。'],
        key=['1 «Dompet saya sudah hilang.» 2 «Dia sedang memakai cermin mata.» 3 «Saya masih mencari beg tangan itu.» '
             '4 «Encik Rahman akan menunggu tetamu.»',
             '5 «Encik Tanaka baru mengambil dompet itu.» 6 «Belum. Saya belum jumpa beg saya.» 7 «Mereka sedang membawa beg yang ada tali panjang.» '
             '8 «Perempuan itu masih memakai topi.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、第15章の動詞と組み合わせて言います。«hilang» の前にも «sudah» を置けます。',
                 'Combine the chapter 4 markers with the chapter 15 verbs. «sudah» also goes in front of «hilang».')),
    question_note='Chapter 15 adds no new question word. The description questions use the ones you know: «Apa warna dompet itu?», «Yang mana satu?», '
                  '«Dompet itu hilang di mana?», «Bila dompet itu hilang?», «Siapa yang memakai topi?», «Kenapa awak mencari beg itu?» / '
                  '第15章で新しい疑問語は増えません。説明の質問は知っている疑問語で作ります：'
                  '«Apa warna dompet itu?»、«Yang mana satu?»、«Dompet itu hilang di mana?»、«Bila dompet itu hilang?»、«Siapa yang memakai topi?»、«Kenapa awak mencari beg itu?»',
    question_tasks=['Ask what is lost. («apa»)', 'Ask who wears the hat. («siapa»)',
                    'Ask where the wallet was lost. («di mana»)', 'Ask formally whether this is the lost-property counter. («Adakah»)',
                    'Ask politely whether you may see the wallet. («Bolehkah»)', 'Ask how many wallets there are. («berapa»)',
                    'Ask when the wallet was lost. («bila»)', 'Ask what time the visitors arrive. («pukul berapa»)',
                    'Ask on what day the wallet was lost. («hari apa»)', 'Ask how the wallet looks. («bagaimana»; spoken «macam mana»)',
                    'Ask why the owner is looking for the bag. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which wallet it is. («yang mana»)', 'Ask where the visitors go next. («ke mana»)',
                    'Ask where the visitors are from. («dari mana»)', 'Ask how far the lift is. («berapa jauh»)',
                    'Ask how long the visitors wait. («berapa lama»)', 'Ask how many cards are inside. («berapa» with a counter)',
                    'Ask who made the form. («siapa» with «oleh»)'],
    question_keys=['1 «Apa yang hilang?» 2 «Siapa yang memakai topi?» 3 «Dompet itu hilang di mana?»',
                   '4 «Adakah ini kaunter barang hilang?» 5 «Bolehkah saya melihat dompet itu?» 6 «Ada berapa dompet?»',
                   '7 «Bila dompet itu hilang?» 8 «Pukul berapa tetamu sampai?» 9 «Pada hari apa dompet itu hilang?»',
                   '10 «Bagaimana dompet itu?» (spoken: «Macam mana dompet itu?») 11 «Kenapa awak mencari beg itu?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab kad saya ada di dalam.» / «Kerana kad saya ada di dalam.»',
                   '12 «Dompet yang mana?» 13 «Selepas stesen, tetamu pergi ke mana?» 14 «Tetamu itu dari mana?»',
                   '15 «Berapa jauh lif?» 16 «Berapa lama tetamu menunggu?» 17 «Ada berapa keping kad di dalam?»',
                   '18 «Borang ini dibuat oleh siapa?»'],
    listening=LISTENING,
    listening_context='On a weekday «Encik» Rahman waits at the station and telephones «Encik» Tanaka to ask which visitors he should look for. / 平日、ラーマンさんが駅で待ちながら田中さんに電話し、どの訪問客を探せばよいかをたずねます。',
    listening_before=['Predict: which of «yang», «memakai», «berwarna» and «seperti» will you hear? Write three guesses. / «yang»・«memakai»・«berwarna»・«seperti» のうち聞こえそうなものを三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['How many visitors are there, and who are they?', 'What does the man wear?', 'Does the man wear glasses?',
                      'What does the woman wear, and how is her hair?', 'What colour is her handbag, and what shape?',
                      'What does the handbag have?', 'What colour is the car?', 'Where are the two men Rahman sees?',
                      'Which man is the guest, and who is he with?'],
    listen_answers=['two: a man and a woman', 'a white shirt, black trousers and black shoes', 'no, he wears a hat', 'a striped shirt; short hair',
                    'red; rectangular, like a small box', 'a zip and one pocket', 'white', 'near the lift',
                    'the one in the hat; the woman in the striped shirt'],
    listening_after=['Compare answers, then shadow lines 2, 6 and 8 after the teacher. / 答えを比べ、2・6・8行目をシャドーイングします。',
                     'Describe one classmate to your partner in four sentences with «yang», «memakai» and «berwarna», and let your partner guess who it is. / クラスメートを一人、«yang»・«memakai»・«berwarna» を使って4文で説明し、パートナーにだれか当ててもらいましょう。'],
    test_listen=[(1, 'a white shirt, black trousers and black shoes', ['baju', 'seluar', 'hitam']),
                 (3, 'a hat, not glasses', ['topi', 'cermin mata', 'memakai']),
                 (5, 'a striped shirt, short hair, a red handbag', ['berjalur', 'rambut', 'merah']),
                 (7, 'rectangular, like a small box; a zip and a pocket', ['segi empat', 'zip', 'poket']),
                 (9, 'a white car; the number plate is in the message', ['kereta', 'nombor plat', 'mesej']),
                 (11, 'the man in the hat, with the woman in the striped shirt', ['yang', 'topi', 'berjalur'])],
    test_listen_prompts=['What does the man wear?', 'What does the man not wear, and what does he wear instead?', 'What does the woman wear, and what colour is her handbag?',
                         'What shape is the handbag, and what does it have?', 'What colour is the car, and where is the number plate?', 'Which man is the guest?'],
    reading_title='Reading and writing · A lost-property form',
    reading=['Fictional lost-property form and a reply from the counter (written Malay; all names are invented):',
             '«Nama: Encik Tanaka. Barang: dompet. Ciri: dompet kulit, berwarna hitam, ada zip dan satu poket kecil. Bentuk: segi empat, seperti kotak kecil. Jenama: tidak ingat. '
             'Tempat: stesen. Kad ada di dalam dompet, tetapi pasport tidak ada.»',
             'Reply from the counter: «Dompet yang ada zip sudah ada di kaunter. Sila ambil dompet itu pada hari Selasa.»'],
    read_questions=['What is lost?', 'What colour is it, and what is it made of?', 'What does it have?', 'What shape is it?',
                    'What is inside, and what is not?', 'Which wallet is at the counter?', 'On which day can he collect it?',
                    'Which word on the form means the features of the wallet?'],
    read_answers=['a wallet', 'black; leather', 'a zip and one small pocket', 'rectangular, like a small box', 'a card is inside, a passport is not',
                  'the one with a zip', 'Tuesday', '«ciri» (forms often print it doubled, ‹ciri-ciri›)'],
    write_instruction='Write four or five sentences about something you have lost (fictional): say what is lost, its colour, its shape, one feature and where it was lost. / '
                      '架空でよいので、なくした物について4〜5文を書きましょう：何がなくなったか、色、形、特徴を一つ、どこでなくしたかを書きます。',
    write_model='«Beg saya hilang di stesen. Beg itu berwarna biru dan ada tali panjang. Bentuknya segi empat, seperti kotak. Ada satu poket kecil. Saya tidak ingat jenamanya.»',
    writing_type='message',
    task_title='Task · At the lost-property counter',
    role_a=['Your information (fictional): you lost a bag, a wallet or a phone at the station. You know its colour, one feature and its shape, but you do not remember the brand. Something inside is still there, and something is not.',
            'Say what is lost with «___ saya hilang», describe it with «yang», «berwarna» and «seperti», answer «Seperti ini?» with «Ya, seperti itu, tetapi …», and choose with «Yang ___.».',
            'Aの情報（架空）：駅でバッグ・財布・携帯電話のどれかをなくしました。色・特徴・形は分かりますが、ブランドは覚えていません。中に残っている物と、ない物があります。'
            '«___ saya hilang» でなくした物を言い、«yang»・«berwarna»・«seperti» で説明し、«Seperti ini?» には «Ya, seperti itu, tetapi …» と答え、«Yang ___.» で選びます。'],
    role_b=['You are B, the counter staff (fictional). Ask the colour, the brand and what it has, and show an item with «Seperti ini?».',
            'Say that there are two items that look the same, and ask «Yang mana satu? Yang ___ atau yang ___?». When A chooses, check one thing inside and hand it over.',
            'Bは窓口の係員です（架空）。色・ブランド・特徴をたずね、«Seperti ini?» と言って物を見せます。'
            'よく似た物が二つあると言い、«Yang mana satu? Yang ___ atau yang ___?» とたずねます。Aが選んだら、中身を一つ確かめて渡します。'],
    change=['Halfway, B says: «Maaf, ada dua beg seperti itu. Yang mana satu? Yang ada poket atau yang ada tali panjang?» A chooses by one feature and says what is inside: «Yang ada tali panjang. Kad saya ada di dalam.»',
            '途中でBが «Maaf, ada dua beg seperti itu. Yang mana satu? Yang ada poket atau yang ada tali panjang?» と言います。Aは特徴を一つ言って選び、中身を言います：«Yang ada tali panjang. Kad saya ada di dalam.»'],
    success=['☐ A says what is lost with «___ saya hilang» and gives a colour, a shape and one feature.',
             '☐ B asks about the colour and the brand and shows an item with «Seperti ini?»; A answers with «seperti itu».',
             '☐ After the change B asks «Yang mana satu?» and A chooses with «Yang ___.» and names something inside.'],
    task_key='«Maaf, ini kaunter barang hilang? Beg saya hilang.» — «Beg yang mana? Apa warna beg itu?» — «Biru. Ada zip dan tali panjang. Bentuknya segi empat, seperti kotak.» — «Ada jenama?» — '
             '«Saya tidak ingat jenamanya.» — «Seperti ini?» — «Ya, seperti itu, tetapi ada zip.» — Change: «Maaf, ada dua beg seperti itu. Yang mana satu? Yang ada poket atau yang ada tali panjang?» — '
             '«Yang ada tali panjang. Kad saya ada di dalam.» — «Betul. Ini beg encik.»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 15 card notes ms-c15-001 («hilang», «barang hilang»), -002 («ciri» and ‹ciri-ciri›), -007 («beg tangan»), -009 («nombor plat»), -014 («seperti», «seperti itu», the spoken ‹macam tu› in chapter 17), '
                    '-020 («memakai» and «pakai»), -021 («berwarna»); scenario lines ms-c15-s01 to s17 (the lost-property counter and the visitors); the plan, chapter 15 («hilang» rather than ‹tertinggal›; handbag; Japanese '
                    'modifiers before the noun). The sentence about lost-property counters is general knowledge of life in Malaysia, labelled as such and not source-checked.',
    culture_prompt='In Japanese, how do you describe a lost bag to a station clerk, and where does the description go in the sentence? Which Malay words carry colour, shape and features?',
    culture_explain=('名詞の前の説明と名詞のあとの «yang»、遺失物の窓口での話し方、一般的な知識、日本人学習者が «yang» でつまずく点を読みます。日本語は未監修です。',
                     'Read about the description before the noun against «yang» after it, how to talk at a lost-property counter, the general knowledge sentence, and where Japanese learners slip with «yang».'),
    quiz_words=['L-1219', 'L-1224', 'L-1272', 'L-1271', 'L-1229', 'L-1228'],
    quiz_meanings=['lost, missing', 'wallet', 'coloured; to be (a colour)', 'to wear (standard form)', 'like, such as (standard)', 'zip'],
    grammar_quiz=[('Say in Malay: "My wallet is lost."', '«Dompet saya hilang.»', ['dompet', 'hilang']),
                  ('Say in Malay: "I am looking for a bag that has a zip."', '«Saya mencari beg yang ada zip.»', ['yang', 'zip']),
                  ('Say in Malay: "The man who wears glasses."', '«Lelaki yang memakai cermin mata.»', ['lelaki', 'memakai', 'cermin mata']),
                  ('Say in Malay: "Which one? The one with a zip or the one without?"', '«Yang mana satu? Yang ada zip atau yang tidak ada zip?»', ['yang mana', 'zip'])],
    test_reading=['Fictional lost-property form: «Barang: beg tangan. Ciri: berwarna merah, kulit, ada dua poket dan tali panjang. Bentuk: bulat, seperti jam besar. '
                  'Tempat: stesen. Kad ada di dalam beg tangan.»'],
    reading_quiz=[('What is lost?', 'a handbag', ['beg tangan', 'hilang']),
                  ('What colour is it, and what is it made of?', 'red; leather', ['berwarna', 'kulit']),
                  ('What shape is it?', 'round, like a big clock', ['bulat', 'seperti']),
                  ('What does it have?', 'two pockets and a long strap', ['poket', 'tali'])],
    speaking_test='Describe something you have lost (fictional) at a counter: say what is lost, its colour and shape with «berwarna» and «seperti», one feature with «yang ada», and choose between two with «Yang ___.»',
    speaking_key='Check: «___ saya hilang»; «berwarna» + a colour; «bentuknya» + «segi empat» or «bulat» with «seperti»; «yang ada» + a feature; a choice with «Yang ___.». '
                 'Accept «hitam» for «berwarna hitam» in a quick answer, and the everyday «macam» for «seperti». Do not mark «dompet hitam» without «yang» wrong.',
    speaking_words=['hilang', 'yang', 'berwarna', 'seperti', 'zip'],
    plan={'A_recall': 'chapters 5, 8 and 14 (a colour, a piece of clothing, a counter, «kerana») from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first («___ saya hilang», «yang ada» and «yang memakai»), question and answer before the rule; then the vocabulary in four groups with each whole word and its root '
                        '(lost things 6, parts and materials 5, colour, shape and likeness 6, people and what they wear 4). Draw the order: Japanese 黒い財布 against Malay «dompet hitam» and «dompet yang hitam».',
          'B_recall': 'say what is lost and give one colour.',
          'B_drills': 'pattern table, substitution, transformation (join with «yang» first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner describes one thing in the room in two sentences without naming it.',
          'D_review': 'cumulative question-word drill (chapters 1 to 15), then the markers drill with new cues and a check of «yang» against no «yang».',
          'D_preview': 'the review block after chapter 15 (chapters 13 to 15 and earlier verb contrasts), then unit 16 (accidents and complaints; Kata-Kata c16).',
          'E_recall': 'say three sentences that describe a bag or a person with «yang», «berwarna» and «seperti».',
          'E_listening': 'read the Kata-Kata scenario lines ms-c15-s01 to ms-c15-s17 (the lost-property counter, then the visitors) twice; '
                         'learners tick «hilang», «yang», «memakai», «berwarna» and «seperti» when they hear them, and listen for «Yang itu!» in line 9.',
          'E_roleplay': 'pairs play the counter scene with their own fictional item, colour and features, without the script; then swap and describe a visitor at a station.',
          'E_variation': 'a changed item: a second bag looks the same; one asks «Yang mana satu?», the other chooses by one feature and names something inside.'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 15 to the lost-property and station scenes. '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: the review block after chapter 15 (chapters 13 to 15 and earlier verb contrasts), then unit 16 (Kata-Kata c16).',
    teacher_notes=['Load: 21 core words in four groups (lost things 6, parts and materials 5, colour, shape and likeness 6, people and what they wear 4), no recognition word, and revision of describing, clothes and papers, places and people, and talking. '
                   'Suggested order: Block A the first two groups with patterns 1 and 2; Block B the last two groups with patterns 3 to 5. '
                   'If the pilot shows 21 is too many, the natural cut is: «hilang», «dompet», «beg tangan», «zip», «berwarna», «bentuk», «seperti», «lelaki», «perempuan», «memakai» first; the rest second.',
                   '«yang» is the connector Japanese does not need. Japanese puts the whole description before the noun and links it with nothing: 黒い財布, 眼鏡をかけている男性. Malay puts the noun first and joins the description with «yang»: '
                   '«dompet yang hitam» and «dompet hitam» both exist (the first stresses "the black one" against another), and «lelaki yang memakai cermin mata» needs «yang» because the description has a verb. '
                   '«yang» is one word for "who", "which" and "that", for people and things.',
                   'When «yang» can be dropped: a single adjective straight after the noun («dompet hitam», «beg besar», «lelaki tinggi»). When it cannot: a clause with a verb or «ada» («beg yang ada zip», «perempuan yang memakai topi»), '
                   'because «beg ada zip» is a whole sentence ("the bag has a zip"). «yang» stays when the noun is left out («Yang ada zip.», «Yang itu!») and after «yang mana» when one of two is chosen. A learner who drops «yang» before an adjective is understood; a learner who drops it before «ada» is not.',
                   '«memakai» covers glasses, clothes, a hat and shoes («memakai cermin mata», «memakai baju», «memakai topi», «memakai kasut»), where Japanese changes the verb: かける for glasses, 着る for clothes, かぶる for a hat and はく for shoes and trousers. '
                   'It is the standard form of the everyday «pakai» (chapter 4): a dialogue may use «pakai», and the pattern examples and keys use «memakai». «memakai» also means "to use", which this unit does not drill.',
                   '«hilang» (lost) against ‹tertinggal› (left behind), which chapter 16 teaches: «Dompet saya hilang.» means you cannot find the wallet; ‹tertinggal› is for something you left somewhere by accident. '
                   'Keep to «hilang» in this unit (the plan asks for «hilang» here and ‹tertinggal› in chapter 16). If a learner says ‹tertinggal›, accept it and say the word comes next chapter.',
                   '«seperti» and «seperti itu» / «seperti ini»: «seperti» is the standard word, and everyday speech says «macam» (chapter 5). «seperti itu» is the standard form of the spoken ‹macam tu›, which chapter 17 teaches, so it is only named here. '
                   '«ini» is the thing near the speaker or in the hand, «itu» the one that is not.',
                   'Whole words and roots: «berjalur» (‹ber-› + ‹jalur›) and «berwarna» (‹ber-› + «warna») are each learned whole; «memakai» is ‹me-› + «pakai» with the p dropped; «bentuknya» is «bentuk» + ‹-nya›. '
                   '«ciri» may be printed doubled, ‹ciri-ciri›, on forms: recognise both (repeated words come in Stage 3). «beg tangan», «cermin mata», «nombor plat» and «segi empat» are learned as phrases (cards ms-c15-007, -017, -009, -012).',
                   'The ‹-kan› and bare-root rules from chapters 12 to 14 still hold: a dialogue line may keep Kata-Kata\'s everyday bare root («Saya sudah jumpa dia.»), and the pattern examples, keys and written forms use the meN- form («mencari», «membawa», «memakai»). '
                   'A request takes the plain root («Tolong cari telefon saya.»). «dari» is for places («dari Jepun») and «daripada» for people and organisations.',
                   'Where Japanese learners usually slip: (1) leaving out «yang» before «ada» or a verb; (2) putting the description before the noun; (3) «saya hilang» for "I lost it" (it says "I am missing"); '
                   '(4) one verb for each kind of clothing instead of «memakai»; (5) «seperti» followed by a clause instead of a noun; (6) answering «Yang mana satu?» with the noun again instead of «Yang ___.»',
                   'Natural speech: «Yang itu!», «Seperti ini?» and «Ya, seperti itu, tetapi …» at the counter; «memakai», «yang» and «berwarna» in a description; the form says «Ciri» (often printed doubled, ‹ciri-ciri›) and «Sila ambil …». '
                   'The scene follows Kata-Kata c15 (scenario lines ms-c15-s01 to s17, frames f01 to f06); turn 11 of the model joins s11 and s12. All names, items and times are fictional; learners may use an invented item.',
                   'Cumulative question words: chapters 1 to 15. Chapter 15 adds no new question word; «yang mana» (chapter 6) now picks one by its description.'],
)

EXTRA = dict(
    slug='review-block', type='Reading and writing', sub_type='composition', kind='review',
    title='Review block · Chapters 13 to 15: a lost bag at the clinic',
    goal='I can use «belum», permission and need, a reason or a condition, and a description with «yang» in one exchange, and keep ber-, meN-, ‹-kan› and ‹-i› verbs apart, without notes.',
    grammar=['ms-c11-g02', 'ms-c12-g02', 'ms-c12-g04', 'ms-c13-g02', 'ms-c13-g04', 'ms-c14-g02', 'ms-c14-g04', 'ms-c15-g03'],
    patterns=['ms-c13-f01', 'ms-c13-f03', 'ms-c14-f01', 'ms-c14-f04', 'ms-c15-f01', 'ms-c15-f05'],
    model=['Chapters 13 to 15 and the verb families in one exchange at a clinic reception (all names and times are fictional):',
           'A: «Selamat pagi. Saya belum mendaftar, tetapi beg saya hilang di klinik ini.» B: «Beg yang mana? Apa warna beg itu?»',
           'A: «Beg itu berwarna biru dan ada tali panjang. Bentuknya segi empat, seperti kotak.» B: «Ada dua beg biru di sini. Yang mana satu? Yang ada zip atau yang tidak ada zip?»',
           'A: «Yang ada zip. Boleh saya ambil beg itu sekarang?» B: «Boleh. Tetapi encik perlu mendaftar dulu supaya doktor boleh berjumpa encik.»',
           'A: «Baik. Walaupun saya sibuk, saya menunggu doktor di sini. Tolong hubungi pejabat saya, ya? Saya bekerja di sana.» B: «Baik. Kalau doktor sudah ada, kami panggil encik.»',
           'Notice: «belum» and «sudah» stand in front of the verb; «perlu» says what you must do and «supaya» why; «yang» opens a description after the noun; a ber- verb has no object («bekerja», «berjumpa»), a meN- verb takes the thing («mendaftar», «menunggu doktor»), '
           'a request takes the plain root («Tolong hubungi …») and ‹-i› points at a person or place. / '
           '気づくこと：«belum»・«sudah» は動詞の前、«perlu» はすべきこと、«supaya» は目的、«yang» は名詞のあとの説明を始めます。ber- の動詞は目的語をとらず（«bekerja»・«berjumpa»）、meN- の動詞は物をすぐあとに置き（«mendaftar»・«menunggu doktor»）、依頼は素の語根（«Tolong hubungi …»）、‹-i› は人や場所へ向かう動作です。'],
    plan=['0–5 Recall: say one thing you have not done yet with «belum» and describe one thing in the room with «yang».',
          '5–15 Mixed input: read the model; underline every «yang» clause, every ber- verb, meN- verb and ‹-i› verb, and say why each marker or connector is there.',
          '15–30 Alternating role task: in pairs, one is a visitor who has lost a bag and one is the receptionist; swap after seven minutes (task below).',
          '30–40 Changed situation: the receptionist says the doctor comes later and there are two choices; the visitor chooses with a reason and describes a second item.',
          '40–45 Self-check against the list below, then one thing to practise at home.',
          '0–5 復習・5–15 混合の入力・15–30 役割交代のタスク・30–40 状況の変更・40–45 自己チェック。'],
    task=['Part 1 (15 min, alternating): A is a visitor at a clinic reception who has lost a bag («Beg saya hilang.»), describes it with «yang», «berwarna» and «seperti», says what A has not done yet («Saya belum mendaftar.») and asks permission («Boleh saya …?»). '
          'B is the receptionist and asks the colour, asks «Yang mana satu?», says what A needs to do and gives a reason. After seven minutes swap.',
          'Part 2 (10 min, changed situation): B says «Maaf, doktor datang pukul empat. Ada dua pilihan: tunggu atau datang esok.» A chooses with «kerana» or «kalau» and says one more thing about the bag.',
          'Part 3 (5 min): write three sentences about a lost item of your own: one with «yang», one with «belum» and one with a meN- verb.',
          'パート1：交代で来院者と受付を演じます。パート2：状況が変わり、来院者は理由か条件をつけて選び、バッグについてもう一つ言います。パート3：なくした物について、«yang»・«belum»・meN- の動詞を一つずつ使った3文を書きます。'],
    check=['☐ «yang» is in front of «ada» or a verb («beg yang ada zip»), and the description comes after the noun.',
           '☐ «belum» stands in front of the verb, and the verb keeps its form («belum mendaftar»).',
           '☐ A ber- verb has no object, and a meN- verb has the thing right after it («mencari beg», «menunggu doktor»).',
           '☐ A request takes the plain root («Tolong hubungi …»), and «perlu» or «supaya» gives the need or the purpose.',
           '☐ «Yang mana satu?» is answered with «Yang ___.» and one feature.'],
    answer='Any natural exchange that follows the checklist. Model: «Beg saya hilang. Saya mencari beg yang berwarna biru dan ada tali panjang. Saya belum mendaftar, jadi saya perlu mendaftar dulu. '
           'Kalau doktor sibuk, saya menunggu di sini. Yang ada zip, ya.»',
    key_extra=['Mark for the task first (the lost item described with «yang», a «belum» sentence, a permission question, a reason or a condition), then for form (the position of «yang», the marker in front of the verb, the right kind of verb). '
               'Accept the everyday bare root in speech («daftar», «panggil»), but ask for the standard form once in the written part.',
               'A review block has no new words. Every word is from chapters 1 to 15; the core groups of 13, 14 and 15 all return.'],
    explain=('ユニット15のあとの復習（45分）：第13〜15章の «belum»・許可・必要、理由や条件、«yang» での説明を、ber-・meN-・‹-kan›・‹-i› の動詞の使い分けと一緒に、ノートなしで一つのやりとりの中で使います。日本語は未監修です。',
             'The review block after chapter 15 (45 minutes): use «belum», permission and need, a reason or a condition and a description with «yang» in one exchange, and keep ber-, meN-, ‹-kan› and ‹-i› verbs apart, without notes, then cope with a changed situation.'),
)

CFG['extra'] = EXTRA
UNIT = unit_dict(CFG)
