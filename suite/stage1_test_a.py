"""A1 stage test, version A. Data only; suite/stage1.py builds the components.

Every item carries its marks, the chapters whose can-do goals it tests, and the ledger words it tests. All names, shops,
prices, times and places are fictional. Japanese is a draft awaiting native review.
"""

VERSION = dict(
    label='A',
    listening=[
        dict(title='Two announcements · 二つのお知らせ',
             context='You hear an announcement in a clothes shop, then one in your office. / 洋服店のお知らせと、事務所のお知らせを聞きます。',
             script=[('Shop announcement', 'Selamat petang. Kedai ini akan ditutup pada pukul sepuluh malam. Hari ini ada diskaun dua puluh peratus untuk semua baju.'),
                     ('Office announcement', 'Selamat pagi, semua. Mesyuarat hari ini mula pukul dua petang, bukan pukul sepuluh pagi. Mesyuarat di bilik mesyuarat di tingkat tiga.')],
             items=[dict(q='When does the shop close, and what is the discount today?', ja='店は何時に閉まりますか。今日の割引は何ですか。',
                         a='at ten at night (1); twenty per cent off all clothes (1)', marks=2, ch=[3, 4, 9],
                         words=['ditutup', 'pukul', 'diskaun', 'peratus']),
                    dict(q='When does the meeting start now, and where is it?', ja='会議は何時に始まることになりましたか。場所はどこですか。',
                         a='at two in the afternoon, not ten in the morning (1); in the meeting room on the third floor (1)', marks=2, ch=[4, 7],
                         words=['mula', 'pukul', 'mesyuarat', 'tingkat'])]),
        dict(title='Meeting a new colleague · 新しい同僚に会う',
             context='«Encik» Tanaka meets a new colleague in the office pantry. / 田中さんが事務所の給湯室で新しい同僚に会います。',
             script=[('Tanaka', 'Selamat pagi. Saya Tanaka. Apa khabar?'),
                     ('Farah', 'Khabar baik, terima kasih. Nama saya Farah. Encik orang Jepun?'),
                     ('Tanaka', 'Ya, saya orang Jepun. Asal puan dari mana?'),
                     ('Farah', 'Asal saya dari Ipoh. Saya kerja di sini. Saya jurutera.'),
                     ('Tanaka', 'Puan tinggal di mana?'),
                     ('Farah', 'Saya tinggal di Subang Jaya. Hobi saya main badminton. Encik pula?'),
                     ('Tanaka', 'Hobi saya karaoke. Jumpa lagi, Puan Farah!')],
             items=[dict(q='What is her name, and where is she from?', ja='女性の名前は何ですか。出身はどこですか。',
                         a='Farah (1); Ipoh (1)', marks=2, ch=[1, 2], words=['nama', 'asal']),
                    dict(q='What is her job, and what is her hobby?', ja='女性の仕事と趣味は何ですか。',
                         a='an engineer («jurutera») (1); «badminton» (1)', marks=2, ch=[2], words=['jurutera', 'hobi', 'badminton']),
                    dict(q='Is it morning, afternoon or evening? Where does she live?', ja='朝ですか、午後ですか、夜ですか。女性はどこに住んでいますか。',
                         a='morning («Selamat pagi») (1); Subang Jaya (1)', marks=2, ch=[1, 2], words=['selamat pagi', 'tinggal'])]),
        dict(title='At a food stall · 屋台で',
             context='A man orders lunch at a «gerai». / 男性が屋台で昼ごはんを注文します。',
             script=[('Stall holder', 'Selamat tengah hari, encik. Mahu makan apa?'),
                     ('Kumar', 'Saya mahu dua keping roti canai dan sebiji telur.'),
                     ('Stall holder', 'Minum apa?'),
                     ('Kumar', 'Secawan teh tarik, kurang manis.'),
                     ('Stall holder', 'Makan sini atau bungkus?'),
                     ('Kumar', 'Makan sini. Berapa harga semua?'),
                     ('Stall holder', 'Roti canai satu ringgit lima puluh sen sekeping. Semua enam ringgit.'),
                     ('Kumar', 'Ini sepuluh ringgit.'),
                     ('Stall holder', 'Baki empat ringgit. Terima kasih!')],
             items=[dict(q='What food does he order? Write each number and counter in Malay.', ja='何を注文しましたか。数と助数詞をマレー語で書きましょう。',
                         a='«dua keping roti canai» (1); «sebiji telur» (1)', marks=2, ch=[8], words=['keping', 'biji', 'roti canai', 'telur']),
                    dict(q='How does he want his tea? Does he eat there or take the food away?', ja='お茶はどのように頼みましたか。店で食べますか、持ち帰りですか。',
                         a='less sweet («kurang manis») (1); he eats there («makan sini») (1)', marks=2, ch=[5, 8],
                         words=['kurang manis', 'makan sini atau bungkus?']),
                    dict(q='How much is everything, and how much change does he get?', ja='全部でいくらですか。おつりはいくらですか。',
                         a='RM6 («enam ringgit») (1); RM4 change («baki empat ringgit») (1)', marks=2, ch=[3], words=['harga', 'ringgit', 'baki'])]),
        dict(title='Directions on the phone · 電話で道案内',
             context='«Puan» Aini phones «Encik» Tanaka, who is on his way to a café. / アイニさんが、カフェに向かう田中さんに電話します。',
             script=[('Aini', 'Encik Tanaka, encik di mana sekarang?'),
                     ('Tanaka', 'Saya di stesen. Kafe itu di mana?'),
                     ('Aini', 'Keluar dari stesen, jalan terus, kemudian belok kanan di lampu isyarat. Kafe di sebelah bank.'),
                     ('Tanaka', 'Berapa jauh dari stesen?'),
                     ('Aini', 'Dekat. Lebih kurang lima minit jalan kaki. Jumpa pukul tiga, ya!')],
             items=[dict(q='How does he get from the station to the café?', ja='駅からカフェまでどう行きますか。',
                         a='straight on (1); then right at the traffic lights (1)', marks=2, ch=[7], words=['terus', 'belok', 'kanan', 'lampu isyarat']),
                    dict(q='Where is the café, and how long is the walk?', ja='カフェはどこにありますか。歩いて何分ですか。',
                         a='next to the bank (1); about five minutes on foot (1)', marks=2, ch=[7, 4], words=['sebelah', 'lebih kurang', 'minit', 'jalan kaki'])]),
    ],
    reading=[
        dict(title='Signs in an office building · ビルの掲示',
             text=['Fictional signs (A to F):', 'A «Dilarang masuk»', 'B «Tandas»', 'C «Dilarang merokok»', 'D «Sila tunggu di sini»',
                   'E «Keluar»', 'F «Lif»'],
             items=[dict(q='You need the toilet, then you want to leave the building. Which two signs do you look for?',
                         ja='トイレに行き、そのあと建物を出たいです。どの二つの掲示を探しますか。',
                         a='B «Tandas» (1); E «Keluar» (1)', marks=2, ch=[7], words=['tandas', 'keluar']),
                    dict(q='Which sign tells you not to go in, and which one asks you to wait?',
                         ja='入ってはいけないという掲示はどれですか。待つように頼んでいる掲示はどれですか。',
                         a='A «Dilarang masuk» (1); D «Sila tunggu di sini» (1)', marks=2, ch=[9], words=['dilarang masuk', 'sila', 'tunggu'])]),
        dict(title='A price board · 屋台の値段表',
             text=['Fictional price board at «Gerai Siti»:', '«Nasi lemak · RM3.50 sebungkus»', '«Mi goreng · RM5.00 sepinggan»',
                   '«Roti canai · RM1.50 sekeping»', '«Pisang goreng · RM0.50 sekeping»', '«Teh tarik · RM2.00 secawan»',
                   '«Kopi · RM1.80 secawan»', '«Air kosong · RM1.00 sebotol»'],
             items=[dict(q='You buy two pieces of «roti canai» and a cup of «teh tarik». How much do you pay?',
                         ja='«roti canai» を2枚と «teh tarik» を1杯買います。いくら払いますか。',
                         a='RM5.00 (2 × RM1.50 + RM2.00) (2; 1 if the working is right but the total is wrong)', marks=2, ch=[3, 8],
                         words=['keping', 'cawan', 'ringgit']),
                    dict(q='Which drink is the cheapest? Is «mi goreng» more expensive than «nasi lemak»?',
                         ja='一番安い飲み物はどれですか。«mi goreng» は «nasi lemak» より高いですか。',
                         a='«air kosong» (RM1.00) (1); yes, RM5.00 against RM3.50 (1)', marks=2, ch=[6], words=['paling', 'murah', 'mahal']),
                    dict(q='You have RM10. You buy a plate of «mi goreng» and a cup of «kopi». How much change do you get?',
                         ja='10リンギ持っています。«mi goreng» を1皿と «kopi» を1杯買います。おつりはいくらですか。',
                         a='RM3.20 (RM10.00 − RM6.80) (2; 1 if the working is right but the answer is wrong)', marks=2, ch=[3],
                         words=['baki', 'sen'])]),
        dict(title='A message from a colleague · 同僚からのメッセージ',
             text=['A fictional WhatsApp message:',
                   '«Selamat pagi, Encik Tanaka. Esok kita jumpa di bank pukul sepuluh pagi, ya. Bank itu di sebelah pejabat pos. '
                   'Dari stesen, jalan terus, kemudian belok kiri. Tolong bawa pasport encik. Terima kasih! Aini»'],
             items=[dict(q='When and where do you meet Aini?', ja='いつ、どこでアイニさんに会いますか。',
                         a='tomorrow at ten in the morning (1); at the bank next to the post office (1)', marks=2, ch=[4, 7],
                         words=['esok', 'pukul', 'sebelah', 'pejabat pos']),
                    dict(q='How do you get there from the station, and what must you bring?', ja='駅からどう行きますか。何を持っていく必要がありますか。',
                         a='straight on, then left (1); your passport (1)', marks=2, ch=[7, 3], words=['terus', 'belok', 'kiri', 'pasport']),
                    dict(q='Who wrote the message, and at what time of day?', ja='誰がメッセージを書きましたか。一日のいつごろですか。',
                         a='Aini (1); in the morning («Selamat pagi») (1)', marks=2, ch=[1], words=['selamat pagi'])]),
        dict(title='A notice on a clinic door · クリニックの掲示',
             text=['A fictional notice:', '«Klinik dibuka pada pukul lapan pagi dan ditutup pada pukul sepuluh malam.»',
                   '«Pada hari Ahad, klinik ditutup.»', '«Dilarang makan dan minum di dalam klinik.»', '«Sila ambil nombor dan tunggu.»'],
             items=[dict(q='Can you see the doctor at nine at night on Sunday? Why?', ja='日曜日の夜9時に診てもらえますか。なぜですか。',
                         a='No (1); the clinic is closed on Sunday («Pada hari Ahad, klinik ditutup») (1)', marks=2, ch=[4, 9],
                         words=['dibuka', 'ditutup', 'pada', 'ahad']),
                    dict(q='What is not allowed inside the clinic, and what do you do when you arrive?',
                         ja='クリニックの中で禁止されていることは何ですか。着いたら何をしますか。',
                         a='eating and drinking (1); take a number and wait (1)', marks=2, ch=[9], words=['dilarang', 'sila', 'ambil', 'nombor'])]),
    ],
    writing=[
        dict(title='A form · 申込書',
             intro='You are joining a Malay class at a community centre (fictional). Fill in the form in Malay about yourself. If you '
                   'prefer, use this card: Kimura Kenji, 35, from Osaka, engineer, works in Bangsar, lives in Mont Kiara, phone '
                   '012-345 6789, hobby golf, class on Wednesday evening. / 地域センターのマレー語クラス（架空）に申し込みます。'
                   '自分のことをマレー語で書きましょう。このカードを使ってもかまいません：木村健二、35歳、大阪出身、エンジニア、'
                   'バンサーで勤務、モントキアラ在住、電話 012-345 6789、趣味はゴルフ、クラスは水曜日の夜。',
             form=['«Borang kelas bahasa Melayu»', '«Nama»', '«Asal»', '«Umur»', '«Nombor telefon»', '«Tinggal di»', '«Kerja»',
                   '«Tempat kerja»', '«Hobi»', '«Hari kelas: Isnin / Rabu / Sabtu»', '«Masa kelas: pagi / petang / malam»'],
             items=[dict(q='Fill in the ten fields of the form.', ja='申込書の10の欄を記入しましょう。',
                         a='One mark per field when the answer is true for the learner (or the card) and in Malay where a Malay word '
                           'is needed; a spelling slip that does not change the word is not penalised. Card answers: 1 «Kimura Kenji»; '
                           '2 «Jepun» (or «Osaka, Jepun»); 3 «35 tahun»; 4 «012-345 6789»; 5 «Mont Kiara»; 6 «jurutera»; 7 «Bangsar»; '
                           '8 «golf»; 9 «Rabu»; 10 «malam».', marks=10, ch=[2, 3, 4],
                         words=['nama', 'asal', 'umur', 'nombor telefon', 'tinggal', 'kerja', 'hobi'])]),
        dict(title='A message · メッセージ',
             intro='Write a WhatsApp message of five to seven sentences to your colleague «Encik» Rahman. Invite him to lunch on '
                   'Friday: greet him; say the day and the time; say where the «gerai» is (a position word or a short route); say '
                   'what you will buy for him, with a counter; ask him one question; and take leave. / 同僚のラーマンさんに '
                   'WhatsApp のメッセージを5〜7文で書きましょう。金曜日の昼ごはんに誘います：あいさつ、曜日と時刻、屋台の場所'
                   '（位置のことばか短い道順）、助数詞を使ってラーマンさんに買うもの、質問を一つ、結びのあいさつ。',
             form=[],
             items=[dict(q='Write the message.', ja='メッセージを書きましょう。',
                         a='Content 4: day and time 1; the place 1; what you will buy, with a counter 1; a greeting and taking leave 1. '
                           'Language 4: «pukul» with the time 1; «di» + a position word, or «jalan terus» / «belok» 1; a number + '
                           'counter + noun, or ‹se-› + counter 1; one more Stage 1 pattern used correctly (a question word or -kah, '
                           '«yang», «lebih … daripada», «sudah» / «belum», a «di-» verb) 1. Accuracy 2: 2 = Malaysian standard forms '
                           'and the meaning always clear; 1 = a few slips, the meaning clear; 0 = the meaning often unclear. '
                           'Model: «Selamat pagi, Encik Rahman. Hari Jumaat ini, kita makan tengah hari di gerai dekat stesen, pukul '
                           'satu? Gerai itu di sebelah bank. Saya beli sebungkus nasi lemak untuk encik. Encik suka teh tarik yang '
                           'kurang manis? Jumpa hari Jumaat!»', marks=10, ch=[1, 4, 7, 8],
                         words=['pukul', 'sebelah', 'bungkus', 'jumpa'])]),
    ],
    speaking=dict(
        intro=dict(q='Self-introduction (about one minute). Introduce yourself to a new colleague: greet, your name, where you are '
                     'from, your work or study, where you live, your hobby; then take leave. The examiner then asks two questions.',
                   ja='自己紹介（約1分）。新しい同僚に自己紹介しましょう：あいさつ、名前、出身、仕事か勉強、住んでいる所、趣味、'
                      '最後に別れのあいさつ。そのあと試験官が二つ質問します。',
                   examiner=['«Selamat pagi. Siapa nama encik?» (or «puan», «cik»)', 'Follow-up 1: «Encik suka makan apa?»',
                             'Follow-up 2: «Encik pergi kerja naik apa?»'],
                   a='Content 4: greeting and taking leave 1; name and origin 1; work or study, and home 1; hobby 1. Language 2: 2 = '
                     '«Nama saya …», «Saya orang …» / «Asal saya dari …», «Saya tinggal di …» said correctly; 1 = some slips; 0 = '
                     'mostly single words. Interaction and delivery 2: both follow-up questions answered in a sentence 1; '
                     'pronunciation and pace easy to follow 1. Model: «Selamat pagi. Nama saya Kimura. Saya orang Jepun. Asal saya '
                     'dari Osaka. Saya kerja di Bangsar. Saya jurutera. Saya tinggal di Mont Kiara. Hobi saya golf. Saya minta diri '
                     'dulu. Jumpa lagi!» Follow-ups: «Saya suka makan nasi lemak.» «Saya pergi kerja naik bas.»',
                   marks=8, ch=[1, 2, 4, 5], words=['nama', 'orang', 'asal', 'tinggal', 'hobi']),
        cards=[
            dict(title='Card 1 · At a «gerai»', ja_title='カード1・屋台で',
                 tasks=['Order lunch for yourself and a colleague: two dishes, each with a number and a counter.',
                        'Ask for a drink «kurang manis» or «ais sedikit».', 'Ask the total and pay.'],
                 tasks_ja=['自分と同僚の昼ごはんを注文しましょう：料理二つを、それぞれ数と助数詞で。',
                           '飲み物を «kurang manis» か «ais sedikit» で頼みましょう。', '合計をたずねて払いましょう。'],
                 examiner=['You are the stall holder: «Selamat tengah hari. Mahu makan apa?»',
                           'Change of plan: «Maaf, nasi lemak sudah habis.» (the learner chooses something else)',
                           'Total: any fictional price that adds up, e.g. «Semua sembilan ringgit.»'],
                 a='Task 3: two dishes with number + counter 1; the drink as asked 1; asks the price and pays 1. Language 2: counters '
                   'and ‹se-› right every time 2, partly 1. Change of plan 1: chooses another dish in a sentence. Model: «Saya mahu '
                   'sepinggan mi goreng dan dua keping roti canai. Secawan teh tarik, kurang manis. Berapa harga semua?»',
                 marks=6, ch=[3, 5, 8], words=['pinggan', 'keping', 'kurang manis', 'harga']),
            dict(title='Card 2 · Buying fruit', ja_title='カード2・果物を買う',
                 tasks=['Ask the price of one kind of fruit for one piece.', 'Compare two fruits and ask which is sweeter.',
                        'Buy some with a number and a counter, and check your change.'],
                 tasks_ja=['果物一つの値段をたずねましょう。', '二つの果物を比べ、どちらが甘いかたずねましょう。',
                           '数と助数詞で買い、おつりを確かめましょう。'],
                 examiner=['You are the fruit seller: «Epal dan oren, encik?»', 'Prices: «Epal satu ringgit lima puluh sen sebiji. '
                           'Oren satu ringgit sebiji.»', 'Change of plan: «Maaf, epal sudah habis. Oren ada.»'],
                 a='Task 3: asks the price per piece («Berapa harga sebiji?») 1; compares («Yang mana lebih manis?») 1; buys with a '
                   'number + «biji» and checks the change 1. Language 2: «sebiji» / «… biji» and the price right 2, partly 1. Change '
                   'of plan 1: buys oranges instead. Model: «Berapa harga epal sebiji?» «Yang mana lebih manis, epal atau oren?» '
                   '«Saya mahu empat biji oren.»', marks=6, ch=[3, 6, 8], words=['biji', 'harga', 'lebih', 'manis']),
            dict(title='Card 3 · Asking the way', ja_title='カード3・道をたずねる',
                 tasks=['Stop someone politely.', 'Ask where the post office is and how far it is.', 'Repeat the route to check it.'],
                 tasks_ja=['ていねいに声をかけましょう。', '郵便局がどこにあるか、どのくらい遠いかをたずねましょう。',
                           '道順を繰り返して確かめましょう。'],
                 examiner=['You are a passer-by: «Pejabat pos di sebelah bank. Jalan terus, kemudian belok kiri di simpang kedua. '
                           'Lebih kurang tiga ratus meter.»', 'Change of plan: «Tetapi pejabat pos ditutup hari ini. Bank dibuka.»'],
                 a='Task 3: «Maaf, tumpang tanya.» 1; «Pejabat pos di mana?» and «Berapa jauh …?» 1; repeats «jalan terus, kemudian '
                   'belok kiri di simpang kedua» 1. Language 2: position and route words right 2, partly 1. Change of plan 1: thanks '
                   'the passer-by and says what he or she will do («Saya pergi ke bank.»). Model: «Maaf, tumpang tanya. Pejabat pos di mana? '
                   'Berapa jauh dari sini?» «Jalan terus, kemudian belok kiri di simpang kedua, ya? Terima kasih.»', marks=6, ch=[1, 3, 7],
                 words=['tumpang tanya', 'berapa jauh', 'belok', 'simpang']),
            dict(title='Card 4 · At the office «jamuan»', ja_title='カード4・事務所の «jamuan»',
                 tasks=['Ask who made one dish and where another was bought.', 'Say how something tastes.',
                        'Offer to help after the party.'],
                 tasks_ja=['料理を誰が作ったか、別の料理をどこで買ったかをたずねましょう。', '何かの味を言いましょう。',
                           '会のあと、手伝いを申し出ましょう。'],
                 examiner=['You are the organiser: «Kek ini dibuat oleh Mei Ling. Kuih dibeli di pasar pagi tadi.»',
                           'Change of plan: «Maaf, jamuan habis pukul lima, bukan pukul enam.»'],
                 a='Task 3: «Kek ini dibuat oleh siapa?» and «Kuih dibeli di mana?» 1; a taste sentence («Kek ini sedap, tetapi '
                   'manis sekali.») 1; offers help («Pinggan saya bawa ke dapur.») 1. Language 2: the «di-» verb with «oleh» or «di» '
                   'right 2, partly 1. Change of plan 1: says what he or she will do with «akan» («Baik, saya akan cuci pinggan dulu.»). '
                   'Model: «Kek ini dibuat oleh siapa? Kuih dibeli di mana?» «Kek ini sedap, tetapi manis sekali.» «Pinggan saya bawa ke dapur.»',
                 marks=6, ch=[4, 5, 9], words=['dibuat', 'oleh', 'dibeli', 'sedap']),
        ]),
)
