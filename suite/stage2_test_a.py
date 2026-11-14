"""A2 stage test, version A. Data only; suite/stage2.py builds the components.

Every item carries its marks, the chapters whose can-do goals it tests (10 to 17), the patterns (Kata-Kata frame IDs) it
tests and the ledger words it tests. Every Malay line uses only ledger words placed in chapters 1 to 17; no practice-pool
word (L-1304 to L-1309) and no recognition-only word («pindah», «tukar», «deadline», «nombor tracking») is tested. No key
requires «lah» or «kan». All names, shops, prices, times, units and places are fictional. Japanese is a draft awaiting
native review.
"""

VERSION = dict(
    label='A',
    listening=[
        dict(title='Two announcements · 二つのお知らせ',
             context='You hear an announcement from the management office of your condominium, then one at a clinic. / '
                     'コンドミニアムの管理事務所のお知らせと、クリニックのお知らせを聞きます。',
             script=[('Management office', 'Selamat pagi. Ini pengumuman daripada pejabat pengurusan. Esok air akan dipotong dari pukul sepuluh pagi '
                                           'hingga pukul dua petang, kerana juruteknik akan membaiki paip di Blok B.'),
                     ('Clinic', 'Selamat petang. Klinik ini dibuka hingga pukul sembilan malam. Kalau ini kali pertama anda di sini, '
                                'anda perlu mendaftar di kaunter dulu. Tidak dibenarkan makan di bilik menunggu.')],
             items=[dict(q='When is the water off tomorrow, and why?', ja='明日、水が止まるのは何時から何時までですか。理由は何ですか。',
                         a='from ten in the morning until two in the afternoon (1); a technician will repair the pipes in Block B (1)',
                         marks=2, ch=[12, 14], frames=['ms-c12-f04'], words=['potong', 'juruteknik', 'membaiki', 'paip', 'kerana']),
                    dict(q='What must a first-time patient do first? What is not allowed in the waiting room?',
                         ja='初めての人はまず何をしなければなりませんか。待合室で禁止されていることは何ですか。',
                         a='register at the counter (1); eating (1)', marks=2, ch=[13], frames=['ms-c13-f03', 'ms-c13-f05'],
                         words=['perlu', 'mendaftar', 'dibenarkan', 'menunggu', 'bilik'])]),
        dict(title='A new colleague · 新しい同僚',
             context='«Encik» Tanaka meets a new colleague in the office pantry. / 田中さんが事務所の給湯室で新しい同僚に会います。',
             script=[('Farah', 'Selamat pagi. Saya Farah. Saya baru bekerja di sini.'),
                     ('Tanaka', 'Selamat datang, Cik Farah! Cik berasal dari mana?'),
                     ('Farah', 'Saya berasal dari Ipoh, tetapi sekarang saya tinggal di Subang Jaya. Setiap pagi saya bertolak pukul tujuh.'),
                     ('Tanaka', 'Pada hujung minggu cik suka buat apa?'),
                     ('Farah', 'Saya suka berenang. Pada hari Ahad saya berbasikal di taman.')],
             items=[dict(q='Where is she from, and where does she live now?', ja='女性の出身はどこですか。今はどこに住んでいますか。',
                         a='from Ipoh («berasal dari Ipoh») (1); in Subang Jaya (1)', marks=2, ch=[10], frames=['ms-c10-f05'],
                         words=['berasal', 'tinggal']),
                    dict(q='What time does she set off every morning? What does she do on Sundays?',
                         ja='毎朝何時に出発しますか。日曜日には何をしますか。',
                         a='at seven («bertolak pukul tujuh») (1); she cycles in the park («berbasikal di taman») (1)', marks=2, ch=[10],
                         frames=['ms-c10-f01', 'ms-c10-f03'], words=['bertolak', 'berbasikal', 'taman'])]),
        dict(title='Who did what? · 誰が何をした？',
             context='«Puan» Aini asks «Encik» Tanaka about a draft. / アイニさんが田中さんに下書きについてたずねます。',
             script=[('Aini', 'Encik Tanaka, siapa yang menulis draf ini?'),
                     ('Tanaka', 'Encik Rahman yang menulis draf itu. Cik Mei Ling sedang menyemak draf itu sekarang.'),
                     ('Aini', 'Bila draf itu dihantar kepada pengurus?'),
                     ('Tanaka', 'Draf itu akan dihantar oleh Cik Mei Ling petang ini. Tarikh akhir hari Khamis.')],
             items=[dict(q='Who wrote the draft, and who is checking it now?', ja='下書きを書いたのは誰ですか。今、確認しているのは誰ですか。',
                         a='«Encik» Rahman (1); «Cik» Mei Ling (1)', marks=2, ch=[11], frames=['ms-c11-f03', 'ms-c11-f05'],
                         words=['menulis', 'menyemak', 'draf']),
                    dict(q='When will the draft be sent to the manager, and when is the deadline?',
                         ja='下書きはいつマネージャーに送られますか。締め切りはいつですか。',
                         a='this afternoon (1); Thursday («tarikh akhir hari Khamis») (1)', marks=2, ch=[11], frames=['ms-c11-f02'],
                         words=['dihantar', 'oleh', 'tarikh akhir'])]),
        dict(title='At the guardhouse · 守衛所で',
             context='«Encik» Tanaka goes to the condominium guardhouse for a parcel. / 田中さんがコンドミニアムの守衛所へ荷物を取りに行きます。',
             script=[('Tanaka', 'Selamat petang. Saya mahu ambil bungkusan. Sudah sampai?'),
                     ('Guard', 'Sudah. Ada dua kotak. Encik tinggal di unit berapa?'),
                     ('Tanaka', 'Blok B, unit 12-3.'),
                     ('Guard', 'Kotak besar ini untuk encik. Kotak kecil itu untuk unit 12-5. Boleh tunjukkan mesej encik?'),
                     ('Tanaka', 'Maaf, telefon saya tertinggal di pejabat.'),
                     ('Guard', 'Tidak mengapa. Nama encik ada pada label kotak ini.')],
             items=[dict(q='How many boxes are there, and which one is his?', ja='箱はいくつありますか。田中さんのはどれですか。',
                         a='two (1); the big box (1)', marks=2, ch=[12], frames=['ms-c12-f03'], words=['bungkusan', 'kotak', 'unit']),
                    dict(q='Why can he not show the message? What does the guard check instead?',
                         ja='なぜメッセージを見せられないのですか。守衛は代わりに何を確かめますか。',
                         a='he left his phone at the office («tertinggal di pejabat») (1); his name on the label (1)', marks=2,
                         ch=[16, 12], frames=['ms-c12-f02', 'ms-c16-f01'], words=['tertinggal', 'tunjukkan', 'label'])]),
        dict(title='An invitation · 招待',
             context='«Puan» Aini invites «Encik» Tanaka to dinner. / アイニさんが田中さんを夕食に招きます。',
             script=[('Aini', 'Encik Tanaka, sudikah encik datang makan malam di rumah saya hari Sabtu?'),
                     ('Tanaka', 'Terima kasih, puan. Sayangnya hari Sabtu saya tidak lapang, kerana kawan saya datang dari Jepun.'),
                     ('Aini', 'Tidak mengapa. Bagaimana kalau hari Ahad, pukul tujuh?'),
                     ('Tanaka', 'Setuju! Hari Ahad, pukul tujuh. Saya bawa kek.')],
             items=[dict(q='Can he come on Saturday? Why or why not?', ja='土曜日に行けますか。理由は何ですか。',
                         a='no («Sayangnya … tidak lapang») (1); a friend is coming from Japan (1)', marks=2, ch=[17, 14],
                         frames=['ms-c17-f01', 'ms-c17-f02', 'ms-c14-f02'], words=['sudi', 'sayangnya', 'lapang', 'kerana']),
                    dict(q='What do they agree on, and what will he bring?', ja='何を決めましたか。田中さんは何を持っていきますか。',
                         a='Sunday at seven (1); a cake (1)', marks=2, ch=[17], frames=['ms-c17-f03', 'ms-c17-f04', 'ms-c17-f05'],
                         words=['tidak mengapa', 'setuju', 'bagaimana', 'kalau'])]),
    ],
    reading=[
        dict(title='A notice at a panel clinic · パネルクリニックの掲示',
             text=['A fictional notice:', '«KLINIK PANEL · PERHATIAN»', '«Kalau ini kali pertama anda di sini, anda wajib mendaftar di kaunter.»',
                   '«Borang kesihatan wajib diisi.»', '«Tidak dibenarkan makan dan minum di bilik menunggu.»',
                   '«Klinik dibuka dari pukul lapan pagi hingga pukul sepuluh malam. Pada hari Ahad, klinik ditutup.»'],
             items=[dict(q='It is your first visit. What must you do at the counter, and what must you fill in?',
                         ja='初めての来院です。受付で何をしなければなりませんか。何に記入しなければなりませんか。',
                         a='register («mendaftar») (1); the health form («borang kesihatan») (1)', marks=2, ch=[13],
                         frames=['ms-c13-f06'], words=['wajib', 'mendaftar', 'borang', 'kesihatan', 'isi']),
                    dict(q='It is Sunday evening. Can you see a doctor here? Where are food and drink not allowed?',
                         ja='日曜日の夜です。ここで診てもらえますか。飲食が禁止されているのはどこですか。',
                         a='no, the clinic is closed on Sunday (1); in the waiting room (1)', marks=2, ch=[13], frames=['ms-c13-f05'],
                         words=['dibenarkan', 'ditutup', 'menunggu', 'bilik'])]),
        dict(title='A message from the management office · 管理事務所からのメッセージ',
             text=['A fictional WhatsApp message:',
                   '«Selamat pagi, Encik Tanaka. Bungkusan encik sudah sampai di pondok pengawal. Label bungkusan itu koyak, jadi sila bawa mesej ini. '
                   'Juruteknik akan datang ke unit encik esok pukul sepuluh pagi untuk membaiki paip yang rosak. Kalau encik tidak ada di rumah, '
                   'sila tinggalkan kunci di pejabat pengurusan. Terima kasih. Pejabat Pengurusan»'],
             items=[dict(q='Where is your parcel? What must you bring, and why?', ja='荷物はどこにありますか。何を持っていく必要がありますか。なぜですか。',
                         a='at the guardhouse («pondok pengawal») (1); this message, because the label is torn (1)', marks=2,
                         ch=[12, 14], frames=['ms-c12-f03'], words=['bungkusan', 'pondok pengawal', 'koyak', 'jadi']),
                    dict(q='When will the technician come, and what will he do? What do you do if you are out?',
                         ja='技術者はいつ来て、何をしますか。留守のときはどうしますか。',
                         a='tomorrow at ten in the morning, to repair the broken pipe (1); leave the key at the management office (1)',
                         marks=2, ch=[12, 14], frames=['ms-c12-f04', 'ms-c14-f01'], words=['juruteknik', 'membaiki', 'kalau', 'tinggalkan'])]),
        dict(title='A lost-property form · 遺失物の届け',
             text=['A fictional lost-property form at a station counter:',
                   '«Barang: beg tangan. Ciri: berwarna biru, kulit, ada zip dan dua poket. Bentuk: segi empat, seperti kotak kecil. '
                   'Hilang di: kereta api, pukul enam petang.»',
                   'Three bags at the counter:', '«Beg A: beg tangan merah yang ada tali panjang.»',
                   '«Beg B: beg tangan biru yang ada zip dan dua poket.»', '«Beg C: beg besar berwarna biru yang ada zip.»'],
             items=[dict(q='Which bag, A, B or C, is the one on the form?', ja='届けのかばんはA・B・Cのどれですか。',
                         a='B (2: the handbag that is blue and has a zip and two pockets)', marks=2, ch=[15],
                         frames=['ms-c15-f01', 'ms-c15-f04', 'ms-c15-f05'], words=['yang', 'berwarna', 'beg tangan', 'zip']),
                    dict(q='Where and when was the bag lost? What shape is it?', ja='かばんはどこで、何時になくなりましたか。形はどうですか。',
                         a='on the train, at six in the evening (1); square, like a small box (1)', marks=2, ch=[15],
                         frames=['ms-c15-f02', 'ms-c15-f06'], words=['hilang', 'bentuk', 'segi empat', 'seperti'])]),
        dict(title='An invitation and a reply · 招待と返事',
             text=['A fictional invitation and reply by email:',
                   '«Jemputan makan malam pejabat: hari Jumaat, pukul tujuh malam, di kafe Sakura. Bos belanja. Sila balas sebelum hari Rabu. '
                   'Puan Aini»',
                   '«Terima kasih atas jemputan puan. Sayangnya hari Jumaat saya tidak lapang, kerana saya ada kelas. '
                   'Bagaimana kalau kita makan tengah hari pada hari Isnin? Mei Ling»'],
             items=[dict(q='When and where is the dinner? Who pays?', ja='夕食会はいつ、どこですか。誰が払いますか。',
                         a='Friday at seven in the evening, at the Sakura café (1); the boss («Bos belanja») (1)', marks=2, ch=[17],
                         frames=['ms-c17-f01'], words=['jemputan', 'belanja', 'balas']),
                    dict(q='Does Mei Ling accept? Why or why not? What does she suggest?',
                         ja='メイリンさんは受けますか。理由は何ですか。何を提案していますか。',
                         a='no, because she has a class («kerana saya ada kelas») (1); lunch together on Monday (1)', marks=2, ch=[17, 14],
                         frames=['ms-c17-f02', 'ms-c17-f03', 'ms-c14-f02'], words=['sayangnya', 'lapang', 'kerana', 'bagaimana', 'kalau'])]),
        dict(title='A note about a small accident · 小さな事故のメモ',
             text=['A fictional note on the office board:',
                   '«Pagi tadi air kopi tertumpah di meja Encik Rahman. Cawan itu terjatuh ke lantai dan pecah. Lantai itu sudah dicuci oleh '
                   'Cik Mei Ling, tetapi lantai masih licin. Sila hati-hati. Encik Rahman tidak apa-apa.»'],
             items=[dict(q='What happened to the coffee, and to the cup?', ja='コーヒーとカップはどうなりましたか。',
                         a='it spilt on «Encik» Rahman\'s desk («tertumpah di meja») (1); it fell to the floor and broke (1)', marks=2,
                         ch=[16], frames=['ms-c16-f03'], words=['tertumpah', 'terjatuh', 'pecah']),
                    dict(q='Who cleaned the floor? Is the floor safe now?', ja='床を拭いたのは誰ですか。床はもう安全ですか。',
                         a='«Cik» Mei Ling («dicuci oleh Cik Mei Ling») (1); no, it is still slippery (1)', marks=2, ch=[11, 16],
                         frames=['ms-c11-f02'], words=['dicuci', 'oleh', 'licin'])]),
    ],
    writing=[
        dict(title='A lost-property form · 遺失物の届け',
             intro='You lost something on the way to work. Fill in the station\'s lost-property form in Malay (fictional). If you prefer, '
                   'use this card: Kimura Kenji, phone 012-345 6789, a black leather wallet, square, with a zip, brand Sakura, lost on '
                   '12 March at about eight in the morning, on the train. / 通勤中に物をなくしました。駅の遺失物の届け（架空）を'
                   'マレー語で記入しましょう。このカードを使ってもかまいません：木村健二、電話 012-345 6789、黒い革の財布、四角、'
                   'ファスナー付き、ブランドはサクラ、3月12日の朝8時ごろ、電車の中でなくした。',
             form=['«Borang barang hilang»', '«Nama»', '«Nombor telefon»', '«Barang»', '«Warna»', '«Bentuk»', '«Ciri»',
                   '«Jenama»', '«Tarikh»', '«Masa»', '«Hilang di»'],
             items=[dict(q='Fill in the ten fields of the form.', ja='届けの10の欄を記入しましょう。',
                         a='One mark per field when the answer is true for the learner (or the card) and in Malay where a Malay word '
                           'is needed; a spelling slip that does not change the word is not penalised; any natural Malaysian answer '
                           'with the same meaning is accepted. Card answers: 1 «Kimura Kenji»; 2 «012-345 6789»; 3 «dompet»; '
                           '4 «hitam»; 5 «segi empat»; 6 «kulit, ada zip» (or «dompet kulit yang ada zip»); 7 «Sakura»; '
                           '8 «12 Mac»; 9 «pukul lapan pagi» (or «lebih kurang pukul lapan pagi»); 10 «kereta api» (or «di dalam kereta api»).',
                         marks=10, ch=[15, 3, 4], frames=['ms-c15-f04', 'ms-c15-f06'],
                         words=['barang', 'hilang', 'warna', 'bentuk', 'ciri', 'jenama', 'tarikh'])]),
        dict(title='A message to change a plan · 予定を変えるメッセージ',
             intro='You and two colleagues planned to go hiking on Saturday. Write a WhatsApp message of five to seven sentences to the '
                   'group: say why you cannot go on Saturday; ask to put the plan off to Sunday; give one condition (if it rains); '
                   'put the Sunday plan in order (first, then, finally) with a time and a meeting place; and close. / 同僚二人と'
                   '土曜日にハイキングに行く予定でした。グループに WhatsApp のメッセージを5〜7文で書きましょう：土曜日に行けない理由、'
                   '日曜日への延期の提案、条件を一つ（雨なら）、日曜日の予定を順番に（まず・それから・最後に）時刻と集合場所を'
                   '入れて、結びのあいさつ。',
             form=[],
             items=[dict(q='Write the message.', ja='メッセージを書きましょう。',
                         a='Content 4: the reason 1; the new day 1; the condition 1; the plan in order with a time and a place 1. '
                           'Language 4: a reason with «kerana» or «sebab» 1; a condition with «kalau» or «jika» 1; putting off with '
                           '«tangguhkan» (or «Boleh kita … ke hari Ahad?») 1; the order with «mula-mula», «kemudian» (or «selepas itu») and '
                           '«akhirnya» 1. Accuracy 2: 2 = Malaysian standard forms, inclusive «kita» for the group and the meaning always '
                           'clear; 1 = a few slips, the meaning clear; 0 = the meaning often unclear. Accept the natural variants '
                           '«kalau» / «jika», «kerana» / «sebab», «kemudian» / «selepas itu», «tangguhkan» / «menangguhkan» '
                           '(after a third-person doer); standard written forms are always right; spoken forms are accepted where the '
                           'meaning is clear but are not needed. Model: «Selamat petang, semua. Maaf, hari Sabtu saya tidak boleh mendaki '
                           'kerana saya bekerja. Boleh kita tangguhkan rancangan mendaki ke hari Ahad? Kalau hujan, kita makan di kafe. '
                           'Mula-mula kita berjumpa di stesen pukul tujuh pagi, kemudian kita mendaki bukit, akhirnya kita makan tengah '
                           'hari di kafe. Jumpa hari Ahad!»', marks=10, ch=[14, 10, 17],
                         frames=['ms-c14-f01', 'ms-c14-f02', 'ms-c14-f06', 'ms-c18-f04'],
                         words=['kerana', 'kalau', 'tangguhkan', 'mula-mula', 'kemudian', 'akhirnya'])]),
    ],
    speaking=dict(
        intro=dict(q='Self-introduction and a working day (about two minutes). Introduce yourself to a new colleague: greet; where you are '
                     'from and where you work; what you do on a working day, with two times; and one thing you like doing at the weekend. '
                     'The examiner then asks one question and invites you to something: accept or decline with a reason.',
                   ja='自己紹介と仕事の一日（約2分）。新しい同僚に自己紹介しましょう：あいさつ、出身と勤め先、仕事の日にすること（時刻を'
                      '二つ入れて）、週末に好きなことを一つ。そのあと試験官が質問を一つして、何かに誘います。理由を言って受けるか断りましょう。',
                   examiner=['«Selamat pagi. Saya Aini. Encik berasal dari mana?» (or «puan», «cik»)',
                             'Follow-up: «Pukul berapa encik bertolak ke pejabat?»',
                             'Invitation: «Sudikah encik datang makan malam pejabat hari Jumaat ini?»'],
                   a='Content 4: greeting, origin and workplace 1; a working day with two times 1; a weekend activity 1; the follow-up '
                     'answered in a sentence 1. Language 2: 2 = ber- and meN- verbs right («berasal», «bekerja», «bertolak», '
                     '«membaca»), «pukul» with the times; 1 = some slips; 0 = mostly single words. Interaction 2: accepts or declines '
                     'the invitation clearly 1; gives a reason («kerana» / «sebab») or another time 1. ‹lah› and ‹kan› are not needed; '
                     'a declined invitation with «Sayangnya …» or «Maaf, …» is as good as an accepted one. Model: «Selamat pagi. Saya '
                     'Kimura. Saya berasal dari Osaka. Saya bekerja di Kuala Lumpur. Setiap pagi saya bertolak pukul tujuh, kemudian saya '
                     'membaca emel. Mesyuarat bermula pukul sepuluh. Pada hujung minggu saya suka berenang.» Follow-up: «Saya bertolak '
                     'pukul tujuh.» Invitation: «Terima kasih. Sayangnya hari Jumaat saya tidak lapang, kerana saya ada kelas. Lain kali, ya?» '
                     'or «Terima kasih, saya akan datang.»',
                   marks=8, ch=[10, 11, 14, 17], frames=['ms-c10-f01', 'ms-c10-f05', 'ms-c18-f01', 'ms-c17-f02'],
                   words=['berasal', 'bekerja', 'bertolak', 'sudi', 'sayangnya', 'kerana']),
        cards=[
            dict(title='Card 1 · A parcel at the guardhouse (request)', ja_title='カード1・守衛所の荷物（依頼）',
                 tasks=['Say you have come for a parcel and give your block and unit.', 'Ask whether it has arrived and show a message.',
                        'Ask the guard to keep a second parcel for your neighbour.'],
                 tasks_ja=['荷物を取りに来たと言い、ブロックと部屋番号を伝えましょう。', '届いているかたずね、メッセージを見せましょう。',
                           'もう一つの荷物を隣人のために預かってくれるよう守衛に頼みましょう。'],
                 examiner=['You are the guard: «Selamat petang. Ada apa, encik?»', '«Ada dua bungkusan. Boleh tunjukkan mesej?»',
                           'Change of plan: «Maaf, label bungkusan ini koyak. Encik tinggal di unit berapa?» (the learner gives the unit again and asks for the right parcel)'],
                 a='Task 3: «Saya mahu ambil bungkusan …» with the block and unit 1; asks «Sudah sampai?» and offers the message 1; the '
                   'request with ‹-kan› («Tolong simpankan …») 1. Language 2: the ‹-kan› request and «Boleh …?» right 2, partly 1. '
                   'Change of plan 1: gives the unit again and checks the parcel. Model: «Saya mahu ambil bungkusan. Sudah sampai? Saya '
                   'tinggal di Blok B, unit 12-3. Ini mesej saya. Tolong simpankan bungkusan kecil itu untuk jiran saya.»',
                 marks=6, ch=[12], frames=['ms-c12-f01', 'ms-c12-f03', 'ms-c18-f02'], words=['bungkusan', 'simpankan', 'unit']),
            dict(title='Card 2 · A leak in the ceiling (request)', ja_title='カード2・天井の水漏れ（依頼）',
                 tasks=['Report a leak in your kitchen ceiling to the management office.', 'Ask them to contact a technician.',
                        'Agree a day and a time for the visit.'],
                 tasks_ja=['台所の天井の水漏れを管理事務所に伝えましょう。', '技術者に連絡してくれるよう頼みましょう。',
                           '来てもらう日と時刻を決めましょう。'],
                 examiner=['You are the management office: «Pejabat pengurusan. Boleh saya tolong?»',
                           '«Baik. Juruteknik boleh datang esok pukul sepuluh pagi.»',
                           'Change of plan: «Maaf, esok juruteknik tidak boleh datang. Bagaimana kalau hari Khamis?» (the learner agrees or gives another time)'],
                 a='Task 3: «Ada kebocoran di siling dapur saya.» 1; «Boleh hubungi juruteknik?» or «Tolong hubungi …» 1; agrees a day and '
                   'a time 1. Language 2: the ‹-i› request and the place right 2, partly 1. Change of plan 1: accepts the new day or '
                   'gives another time with a reason. Model: «Ada kebocoran di siling dapur saya. Boleh hubungi juruteknik? Esok pukul '
                   'sepuluh, boleh.» After the change: «Hari Khamis boleh. Pukul berapa?»',
                 marks=6, ch=[12, 14], frames=['ms-c12-f05', 'ms-c12-f06'], words=['kebocoran', 'siling', 'hubungi', 'juruteknik']),
            dict(title='Card 3 · Locked out (mishap)', ja_title='カード3・締め出された（トラブル）',
                 tasks=['Tell the guard that your door is locked and your key is inside.', 'Say what happened (you forgot it).',
                        'Ask for one practical next step.'],
                 tasks_ja=['ドアがロックされて鍵が中にあると守衛に伝えましょう。', '何が起きたか言いましょう（うっかり忘れた）。',
                           '具体的な次の対応を一つ頼みましょう。'],
                 examiner=['You are the guard: «Ya, encik? Ada masalah?»', '«Encik tinggal di unit berapa?»',
                           'Change of plan: «Maaf, pejabat pengurusan sudah ditutup.» (the learner asks for another step, for example to borrow a phone)'],
                 a='Task 3: «Pintu saya terkunci.» and the key inside 1; «Maaf, saya terlupa.» or «Kunci saya tertinggal di dalam rumah.» 1; '
                   'a clear request («Boleh tolong hubungi pejabat pengurusan?») 1. Language 2: accident ‹ter-› forms right 2, partly 1. '
                   'Change of plan 1: asks another step («Boleh saya pinjam telefon encik?»). Model: «Maaf, pintu saya terkunci. Kunci saya '
                   'tertinggal di dalam rumah. Saya terlupa. Boleh tolong hubungi pejabat pengurusan?»',
                 marks=6, ch=[16], frames=['ms-c16-f01', 'ms-c16-f02', 'ms-c16-f06', 'ms-c18-f06'], words=['terkunci', 'tertinggal', 'terlupa']),
            dict(title='Card 4 · Coffee on a colleague\'s desk (mishap)', ja_title='カード4・同僚の机にコーヒー（トラブル）',
                 tasks=['Tell your colleague what happened: your coffee spilt on his desk by accident.', 'Apologise.',
                        'Offer one thing you will do now.'],
                 tasks_ja=['何が起きたか同僚に言いましょう：あなたのコーヒーが誤って同僚の机にこぼれました。', 'あやまりましょう。',
                           '今からすることを一つ申し出ましょう。'],
                 examiner=['You are the colleague: «Apa yang berlaku?»', '«Fail saya basah?»',
                           'Change of plan: «Telefon saya pun terjatuh ke lantai!» (the learner checks and offers help)'],
                 a='Task 3: «Air kopi saya tertumpah di meja encik.» 1; «Maaf, saya tidak sengaja.» 1; offers a step with a first-person '
                   'form («Saya bersihkan meja ini sekarang.» or «Saya ambil tisu.») 1. Language 2: ‹ter-› and «tidak sengaja» right 2, partly 1. '
                   'Change of plan 1: asks «Telefon encik tidak apa-apa?» or picks it up. Model: «Maaf, air kopi saya tertumpah di meja '
                   'encik. Saya tidak sengaja. Saya bersihkan meja ini sekarang.»',
                 marks=6, ch=[16], frames=['ms-c16-f03', 'ms-c16-f04'], words=['tertumpah', 'tidak sengaja', 'terjatuh']),
        ]),
)
