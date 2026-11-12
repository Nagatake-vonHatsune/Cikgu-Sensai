"""A1 stage test, version B: parallel to version A (same sections, tasks, marks and chapter spread; different facts), so the
test can be reused, for a second group or a re-sit. Data only; suite/stage1.py builds the components.

All names, shops, prices, times and places are fictional. Japanese is a draft awaiting native review.
"""

VERSION = dict(
    label='B',
    listening=[
        dict(title='Two announcements · 二つのお知らせ',
             context='You hear an announcement in a bookshop, then one in your office. / 本屋のお知らせと、事務所のお知らせを聞きます。',
             script=[('Shop announcement', 'Selamat malam. Kedai buku ini akan ditutup pada pukul sembilan setengah malam. Hari ini ada diskaun lima belas peratus untuk semua buku.'),
                     ('Office announcement', 'Selamat petang, semua. Jamuan hari Jumaat mula pukul empat petang, bukan pukul lima. Jamuan di dapur di tingkat dua.')],
             items=[dict(q='When does the shop close, and what is the discount today?', ja='店は何時に閉まりますか。今日の割引は何ですか。',
                         a='at half past nine at night (1); fifteen per cent off all books (1)', marks=2, ch=[3, 4, 9],
                         words=['ditutup', 'pukul', 'setengah', 'diskaun', 'peratus']),
                    dict(q='When does Friday\'s party start now, and where is it?', ja='金曜日の会は何時に始まることになりましたか。場所はどこですか。',
                         a='at four in the afternoon, not five (1); in the kitchen on the second floor (1)', marks=2, ch=[4, 7],
                         words=['jamuan', 'mula', 'pukul', 'tingkat'])]),
        dict(title='Meeting a new neighbour · 新しい隣人に会う',
             context='«Encik» Yamada meets a new neighbour in the lobby of his condo. / 山田さんがコンドミニアムのロビーで新しい隣人に会います。',
             script=[('Yamada', 'Selamat petang. Nama saya Yamada. Siapa nama cik?'),
                     ('Devi', 'Nama saya Devi. Saya orang Malaysia. Asal saya dari Penang.'),
                     ('Yamada', 'Cik kerja di mana?'),
                     ('Devi', 'Saya guru. Saya kerja di sekolah di Petaling Jaya.'),
                     ('Yamada', 'Cik tinggal di kondo ini?'),
                     ('Devi', 'Ya, di tingkat lima. Hobi saya masak. Encik pula?'),
                     ('Yamada', 'Hobi saya golf. Jumpa lagi, Cik Devi!')],
             items=[dict(q='What is her name, and where is she from?', ja='女性の名前は何ですか。出身はどこですか。',
                         a='Devi (1); Penang (1)', marks=2, ch=[1, 2], words=['nama', 'asal']),
                    dict(q='What is her job, and where does she work?', ja='女性の仕事は何ですか。どこで働いていますか。',
                         a='a teacher («guru») (1); at a school in Petaling Jaya (1)', marks=2, ch=[2], words=['guru', 'kerja', 'sekolah']),
                    ]),
        dict(title='Choosing how to go · 行き方選び',
             context='Two colleagues decide how to get to the bank. / 二人の同僚が銀行への行き方を決めます。',
             script=[('Mei Ling', 'Kita pergi ke bank naik bas, naik teksi atau jalan kaki?'),
                     ('Yamada', 'Teksi lebih cepat daripada bas.'),
                     ('Mei Ling', 'Tetapi jalan kaki paling murah. Bank dekat.'),
                     ('Yamada', 'Baik. Kita jalan kaki.')],
             items=[dict(q='Which is quicker, the taxi or the bus? Which way of going does Mei Ling say is the cheapest?',
                         ja='タクシーとバスではどちらが速いですか。メイリンさんはどの行き方が一番安いと言っていますか。',
                         a='the taxi is quicker than the bus («lebih cepat daripada») (1); on foot is the cheapest («jalan kaki paling murah») (1)',
                         marks=2, ch=[6], words=['lebih', 'daripada', 'cepat', 'paling', 'murah'], compulsory='comparison')]),
        dict(title='At a food stall · 屋台で',
             context='A woman orders breakfast at a «gerai». / 女性が屋台で朝ごはんを注文します。',
             script=[('Stall holder', 'Selamat pagi, puan. Mahu makan apa?'),
                     ('Nora', 'Saya mahu sepinggan nasi goreng dan dua keping pisang goreng.'),
                     ('Stall holder', 'Minum apa?'),
                     ('Nora', 'Secawan kopi, ais sedikit.'),
                     ('Stall holder', 'Makan sini atau bungkus?'),
                     ('Nora', 'Bungkus. Berapa harga semua?'),
                     ('Stall holder', 'Nasi goreng lima ringgit lima puluh sen. Semua lapan ringgit lima puluh sen.'),
                     ('Nora', 'Ini sepuluh ringgit.'),
                     ('Stall holder', 'Baki satu ringgit lima puluh sen. Terima kasih!')],
             items=[dict(q='What food does she order? Write each number and counter in Malay.', ja='何を注文しましたか。数と助数詞をマレー語で書きましょう。',
                         a='«sepinggan nasi goreng» (1); «dua keping pisang goreng» (1)', marks=2, ch=[8],
                         words=['pinggan', 'keping', 'nasi', 'goreng', 'pisang goreng']),
                    dict(q='How does she want her coffee? Does she eat there or take the food away?', ja='コーヒーはどのように頼みましたか。店で食べますか、持ち帰りですか。',
                         a='with a little ice («ais sedikit») (1); she takes it away («bungkus») (1)', marks=2, ch=[5, 8],
                         words=['ais', 'sedikit', 'makan sini atau bungkus?']),
                    dict(q='How much is everything, and how much change does she get?', ja='全部でいくらですか。おつりはいくらですか。',
                         a='RM8.50 («lapan ringgit lima puluh sen») (1); RM1.50 change («baki satu ringgit lima puluh sen») (1)', marks=2,
                         ch=[3], words=['harga', 'ringgit', 'sen', 'baki'])]),
        dict(title='Directions on the phone · 電話で道案内',
             context='Mei Ling phones «Encik» Yamada, who is on his way to a «kedai mamak». / メイリンさんが、ママックの店に向かう山田さんに電話します。',
             script=[('Mei Ling', 'Encik Yamada, encik di mana sekarang?'),
                     ('Yamada', 'Saya di pejabat pos. Kedai mamak itu di mana?'),
                     ('Mei Ling', 'Dari pejabat pos, jalan terus, kemudian belok kiri di simpang kedua. Kedai mamak di antara bank dan klinik.'),
                     ('Yamada', 'Berapa jauh dari sini?'),
                     ('Mei Ling', 'Lebih kurang tiga ratus meter. Jumpa pukul satu, ya!')],
             items=[dict(q='How does he get from the post office to the «kedai mamak»?', ja='郵便局からママックの店までどう行きますか。',
                         a='straight on (1); then left at the second junction (1)', marks=2, ch=[7, 3], words=['terus', 'belok', 'kiri', 'simpang', 'kedua']),
                    dict(q='Where is the «kedai mamak», and how far is it?', ja='ママックの店はどこにありますか。どのくらい遠いですか。',
                         a='between the bank and the clinic (1); about three hundred metres (1)', marks=2, ch=[7, 3],
                         words=['antara', 'lebih kurang', 'meter'])]),
    ],
    reading=[
        dict(title='Signs in a shopping centre · ショッピングセンターの掲示',
             text=['Fictional signs (A to G):', 'A «Keluar»', 'B «Dilarang makan dan minum»', 'C «Tandas»', 'D «Sila ambil nombor»',
                   'E «TOLAK»', 'F «Tangga»', 'G «TARIK»'],
             items=[dict(q='Which sign shows the stairs, and which one shows the toilet?', ja='階段を示す掲示はどれですか。トイレを示す掲示はどれですか。',
                         a='F «Tangga» (1); C «Tandas» (1)', marks=2, ch=[7], words=['tangga', 'tandas']),
                    dict(q='You want to have a drink here. Which sign says you may not? Which sign is on a door that you push?',
                         ja='ここで飲み物を飲みたいです。それができないという掲示はどれですか。押して開けるドアの表示はどれですか。',
                         a='B «Dilarang makan dan minum» (1); E «TOLAK» (1)', marks=2, ch=[9], words=['dilarang', 'tolak', 'tarik'])]),
        dict(title='A price board · 果物屋の値段表',
             text=['Fictional price board at «Gerai buah Ali»:', '«Epal · RM1.50 sebiji»', '«Oren · RM1.20 sebiji»', '«Mangga · RM3.00 sebiji»'],
             items=[dict(q='You buy three apples. How much do you pay?', ja='りんごを3個買います。いくら払いますか。',
                         a='RM4.50 (3 × RM1.50) (2; 1 if the working is right but the total is wrong)', marks=2, ch=[3, 8],
                         words=['biji', 'ringgit']),
                    dict(q='Which fruit is the most expensive for one piece? Is an orange cheaper than an apple?',
                         ja='一つあたり一番高い果物はどれですか。オレンジはりんごより安いですか。',
                         a='«mangga» (RM3.00) (1); yes, RM1.20 against RM1.50 (1)', marks=2, ch=[6], words=['paling', 'mahal', 'murah']),
                    dict(q='You have RM20. You buy two mangoes and five oranges. How much change do you get?',
                         ja='20リンギ持っています。マンゴーを2個、オレンジを5個買います。おつりはいくらですか。',
                         a='RM8.00 (RM20.00 − (2 × RM3.00 + 5 × RM1.20) = RM20.00 − RM12.00) (2; 1 if the working is right but the answer is wrong)',
                         marks=2, ch=[3, 8], words=['baki', 'biji'])]),
        dict(title='A message from a friend · 友人からのメッセージ',
             text=['A fictional WhatsApp message:',
                   '«Selamat petang, Encik Yamada, dan Selamat Hari Gawai! Jamuan hari Jumaat di rumah saya, pukul tujuh malam. Rumah saya di Bangsar, di '
                   'belakang sekolah. Dari stesen, lebih kurang sepuluh minit naik teksi. Tolong bawa dua botol air. Jumpa hari '
                   'Jumaat! Mei Ling»'],
             items=[dict(q='When and where is the party?', ja='会はいつ、どこですか。',
                         a='Friday at seven in the evening (1); at Mei Ling\'s home in Bangsar, behind the school (1)', marks=2, ch=[4, 7],
                         words=['jamuan', 'pukul', 'belakang']),
                    dict(q='How do you get there from the station, and what must you bring?', ja='駅からどう行きますか。何を持っていく必要がありますか。',
                         a='about ten minutes by taxi (1); two bottles of water (1)', marks=2, ch=[7, 8], words=['naik', 'teksi', 'botol']),
                    dict(q='At what time of day was the message written? Which festival does the greeting mention?',
                         ja='メッセージは一日のいつごろ書かれましたか。挨拶はどのお祭りについてですか。',
                         a='in the afternoon («Selamat petang») (1); the «Gawai» festival («Selamat Hari Gawai») (1)', marks=2, ch=[1, 9],
                         words=['selamat petang', 'selamat', 'hari', 'gawai'])]),
        dict(title='A notice at a bank · 銀行の掲示',
             text=['A fictional notice:', '«PERHATIAN: Bank ditutup hingga hari Isnin.»',
                   '«Bank dibuka dari pukul sembilan setengah pagi hingga pukul empat petang.»', '«Dilarang merokok.»', '«Sila tunggu di sini.»'],
             items=[dict(q='It is Saturday. When can you next go to the bank, and until what time is it open on that day?',
                         ja='今日は土曜日です。次に銀行へ行けるのはいつですか。その日は何時まで開いていますか。',
                         a='on Monday («ditutup hingga hari Isnin») (1); until four in the afternoon («hingga pukul empat petang») (1)', marks=2,
                         ch=[4, 9], words=['perhatian', 'ditutup', 'hingga', 'dibuka', 'pukul']),
                    dict(q='What is not allowed, and what are you asked to do?', ja='禁止されていることは何ですか。何をするように言われていますか。',
                         a='smoking (1); wait here (1)', marks=2, ch=[9], words=['dilarang merokok', 'sila', 'tunggu'])]),
    ],
    writing=[
        dict(title='A form · 職員用の書類',
             intro='You are starting work at a new office (fictional). Fill in the staff form in Malay about yourself. If you prefer, '
                   'use this card: Sato Yuki, 29, from Tokyo, manager, lives in Petaling Jaya, phone 017-246 8135, speaks Japanese, '
                   'English and a little Malay, hobby «badminton», starts on Monday at nine in the morning. / 新しい事務所（架空）で'
                   '働き始めます。職員用の書類に自分のことをマレー語で書きましょう。このカードを使ってもかまいません：佐藤由紀、'
                   '29歳、東京出身、マネージャー、ペタリンジャヤ在住、電話 017-246 8135、日本語・英語・少しマレー語を話す、趣味は'
                   'バドミントン、月曜日の午前9時から勤務。',
             form=['«Borang pejabat»', '«Nama»', '«Asal»', '«Umur»', '«Nombor telefon»', '«Tinggal di»', '«Kerja»',
                   '«Bahasa: Melayu / Inggeris / Jepun»', '«Hobi»', '«Hari mula kerja»', '«Pukul mula kerja»'],
             items=[dict(q='Fill in the ten fields of the form.', ja='書類の10の欄を記入しましょう。',
                         a='One mark per field when the answer is true for the learner (or the card) and in Malay where a Malay word '
                           'is needed; a spelling slip that does not change the word is not penalised. Card answers: 1 «Sato Yuki»; '
                           '2 «Jepun» (or «Tokyo, Jepun»); 3 «29 tahun»; 4 «017-246 8135»; 5 «Petaling Jaya»; 6 «pengurus»; '
                           '7 «bahasa Jepun, bahasa Inggeris dan bahasa Melayu sedikit»; 8 «badminton»; 9 «Isnin»; 10 «pukul sembilan pagi».',
                         marks=10, ch=[2, 3, 4], words=['nama', 'asal', 'umur', 'nombor', 'tinggal', 'kerja', 'bahasa', 'hobi'])]),
        dict(title='A message · メッセージ',
             intro='You will be late for the Friday «jamuan». Write a WhatsApp message of five to seven sentences to «Puan» Aini: '
                   'greet her; say where you are now; say what time you will arrive; say what you are bringing, with a counter; ask '
                   'one question about the food with a «di-» verb; and take leave. / 金曜日の «jamuan» に遅れます。アイニさんに '
                   'WhatsApp のメッセージを5〜7文で書きましょう：あいさつ、今いる場所、着く時刻、助数詞を使って持っていくもの、'
                   '«di-» の動詞を使った料理についての質問を一つ、結びのあいさつ。',
             form=[],
             items=[dict(q='Write the message.', ja='メッセージを書きましょう。',
                         a='Content 4: where you are now 1; the time you will arrive 1; what you are bringing, with a counter 1; a '
                           'greeting and taking leave 1. Language 4: «pukul» with the time and «akan» or «masih» 1; «di» + a place 1; '
                           'a number + counter + noun, or ‹se-› + counter 1; a question with a «di-» verb («sudah dibeli?», «dibuat '
                           'oleh siapa?») 1. Accuracy 2: 2 = Malaysian standard forms and the meaning always clear; 1 = a few slips, '
                           'the meaning clear; 0 = the meaning often unclear. Model: «Selamat petang, Puan Aini. Maaf, saya masih di '
                           'stesen. Kereta api lambat. Saya akan sampai pukul lima setengah. Saya bawa sekotak kuih dan dua botol air. '
                           'Nasi lemak sudah dibeli? Jumpa nanti!»', marks=10, ch=[1, 4, 8, 9],
                         words=['masih', 'akan', 'kotak', 'dibeli'])]),
    ],
    speaking=dict(
        intro=dict(q='Self-introduction (about one minute). Introduce yourself to a new neighbour: greet, your name, where you are '
                     'from, your work or study, where you live, your hobby; then take leave. The examiner then asks two questions.',
                   ja='自己紹介（約1分）。新しい隣人に自己紹介しましょう：あいさつ、名前、出身、仕事か勉強、住んでいる所、趣味、'
                      '最後に別れのあいさつ。そのあと試験官が二つ質問します。',
                   examiner=['«Selamat petang. Siapa nama encik?» (or «puan», «cik»)', 'Follow-up 1: «Encik suka minum apa?»',
                             'Follow-up 2: «Encik mula kerja pukul berapa?»'],
                   a='Content 4: greeting and taking leave 1; name and origin 1; work or study, and home 1; hobby 1. Language 2: 2 = '
                     '«Nama saya …», «Saya orang …» / «Asal saya dari …», «Saya tinggal di …» said correctly; 1 = some slips; 0 = '
                     'mostly single words. Interaction and delivery 2: both follow-up questions answered in a sentence 1; '
                     'pronunciation and pace easy to follow 1. Model: «Selamat petang. Nama saya Sato Yuki. Saya orang Jepun. Asal '
                     'saya dari Tokyo. Saya pengurus. Saya kerja di Petaling Jaya. Saya tinggal di kondo ini, di tingkat lima. Hobi '
                     'saya badminton. Jumpa lagi!» Follow-ups: «Saya suka minum teh tarik.» «Saya mula kerja pukul sembilan pagi.»',
                   marks=8, ch=[1, 2, 4, 5], words=['nama', 'orang', 'asal', 'tinggal', 'hobi']),
        cards=[
            dict(title='Card 1 · At a «kedai mamak»', ja_title='カード1・ママックの店で',
                 tasks=['Order drinks for three people, with a counter; one of them «kurang manis».',
                        'Ask if there is «roti canai».', 'Ask the total and pay.'],
                 tasks_ja=['三人分の飲み物を助数詞を使って注文しましょう。一つは «kurang manis» で。',
                           '«roti canai» があるかたずねましょう。', '合計をたずねて払いましょう。'],
                 examiner=['You are the waiter: «Selamat pagi. Minum apa?»', 'Change of plan: «Maaf, teh tarik sudah habis. Kopi ada.»',
                           'Total: any fictional price that adds up, e.g. «Semua tujuh ringgit.»'],
                 a='Task 3: three drinks with a number + counter, one «kurang manis» 1; asks about «roti canai» («Ada roti canai?») 1; '
                   'asks the price and pays 1. Language 2: counters and the order right every time 2, partly 1. Change of plan 1: '
                   'orders coffee instead in a sentence. Model: «Tiga cawan teh tarik, satu kurang manis.» «Ada roti canai?» '
                   '«Berapa harga semua?» After the change: «Tiga cawan kopi, tolong.»',
                 marks=6, ch=[3, 5, 8], words=['cawan', 'kurang manis', 'harga']),
            dict(title='Card 2 · Buying a shirt', ja_title='カード2・シャツを買う',
                 tasks=['Ask the price of one shirt.', 'Say it is too big and ask for a smaller one.', 'Buy two with a counter.'],
                 tasks_ja=['シャツ1枚の値段をたずねましょう。', '大きすぎると言い、もっと小さいものがあるかたずねましょう。',
                           '助数詞を使って2枚買いましょう。'],
                 examiner=['You are the shop assistant: «Baju ini empat puluh ringgit sehelai.»',
                           'Change of plan: «Yang kecil warna merah sahaja.» (the learner says whether he or she will buy it)'],
                 a='Task 3: «Berapa harga baju ini sehelai?» 1; «Baju ini terlalu besar. Ada yang lebih kecil?» 1; «Saya mahu dua '
                   'helai.» 1. Language 2: «terlalu», «lebih» and the counter «helai» right 2, partly 1. Change of plan 1: answers '
                   'in a sentence («Baik, saya mahu yang merah.» or «Tidak, terima kasih.»). Model: as in the task lines.',
                 marks=6, ch=[3, 5, 6, 8], words=['helai', 'terlalu', 'lebih', 'kecil']),
            dict(title='Card 3 · Arranging to meet', ja_title='カード3・待ち合わせを決める',
                 tasks=['On the phone, suggest a day and a time to meet.', 'Say where to meet and how to get there.',
                        'Agree a new time and repeat it.'],
                 tasks_ja=['電話で、会う曜日と時刻を提案しましょう。', '会う場所と行き方を言いましょう。',
                           '新しい時刻を決め、繰り返して確かめましょう。'],
                 examiner=['You are a colleague: «Hari Rabu boleh. Kita jumpa di mana?»',
                           'Change of plan: «Maaf, saya ada mesyuarat pukul tiga.»'],
                 a='Task 3: a day and a time («Kita jumpa hari Rabu, pukul dua petang?») 1; the place and the way («Kita jumpa di kafe '
                   'di sebelah stesen. Naik bas, lebih kurang sepuluh minit.») 1; repeats the new time («Pukul empat, boleh?») 1. '
                   'Language 2: «pukul», the day, and a position or route right 2, partly 1. Change of plan 1: offers another time. '
                   'Model: as in the task lines.', marks=6, ch=[4, 7], words=['pukul', 'jumpa', 'sebelah', 'naik']),
            dict(title='Card 4 · Monday at the office', ja_title='カード4・月曜日の事務所',
                 tasks=['Ask who wrote a letter on your desk.', 'Ask whether the parcel has been sent.',
                        'Say that you will send it yourself, and when.'],
                 tasks_ja=['机の上の手紙を誰が書いたかたずねましょう。', '小包がもう送られたかたずねましょう。',
                           '自分で送ると言い、いつ送るかを言いましょう。'],
                 examiner=['You are a colleague: «Surat ini ditulis oleh Encik Rahman. Bungkusan belum dihantar.»',
                           'Change of plan: «Pejabat pos ditutup pada pukul empat hari ini.»'],
                 a='Task 3: «Surat ini ditulis oleh siapa?» 1; «Bungkusan sudah dihantar?» 1; «Bungkusan saya hantar petang ini.» 1. '
                   'Language 2: the «di-» verb with «oleh», «sudah» / «belum» right 2, partly 1. Change of plan 1: says when he or '
                   'she will go instead («Baik, saya akan hantar esok pagi.»). Model: as in the task lines.',
                 marks=6, ch=[4, 9], words=['ditulis', 'oleh', 'dihantar', 'bungkusan']),
        ]),
)
