"""A2 stage test, version B: parallel to version A (same sections, tasks, marks and chapter spread) with different fictional
details. Data only; suite/stage2.py builds the components.

Every Malay line uses only ledger words placed in chapters 1 to 17; no practice-pool word and no recognition-only word is
tested; no key requires «lah» or «kan». All names, shops, prices, times, units and places are fictional. Japanese is a
draft awaiting native review.
"""

VERSION = dict(
    label='B',
    listening=[
        dict(title='Two announcements · 二つのお知らせ',
             context='You hear an announcement in your office building, then one at a clinic. / 事務所ビルのお知らせと、クリニックのお知らせを聞きます。',
             script=[('Building office', 'Selamat petang, semua. Lif di Blok A rosak. Juruteknik sedang membaiki lif itu, jadi sila guna '
                                         'tangga hingga pukul lima petang.'),
                     ('Clinic', 'Perhatian kepada semua. Sila ambil nombor dan tunggu di bilik menunggu. Anda perlu mengisi borang '
                                'kesihatan dulu. Tidak dibenarkan minum di bilik doktor.')],
             items=[dict(q='What is wrong in Block A, and what must you use until five?', ja='Aブロックで何が故障していますか。5時まで何を使いますか。',
                         a='the lift is broken; a technician is repairing it (1); the stairs, until five in the afternoon (1)',
                         marks=2, ch=[12, 14], frames=['ms-c12-f04'], words=['rosak', 'juruteknik', 'membaiki', 'jadi', 'tangga']),
                    dict(q='What must you fill in first? What is not allowed in the doctor\'s room?',
                         ja='まず何に記入しなければなりませんか。診察室で禁止されていることは何ですか。',
                         a='the health form («borang kesihatan») (1); drinking (1)', marks=2, ch=[13], frames=['ms-c13-f03', 'ms-c13-f05'],
                         words=['perlu', 'mengisi', 'borang', 'dibenarkan'])]),
        dict(title='A new neighbour · 新しい隣人',
             context='«Encik» Kimura meets a new neighbour at the lift. / 木村さんがエレベーターの前で新しい隣人に会います。',
             script=[('Hafiz', 'Selamat pagi. Nama saya Hafiz. Saya baru berpindah ke unit 9-2.'),
                     ('Kimura', 'Selamat berkenalan, Encik Hafiz! Encik berasal dari mana?'),
                     ('Hafiz', 'Saya berasal dari Penang. Saya bekerja di sebuah bank di Bangsar. Setiap pagi saya bertolak pukul lapan.'),
                     ('Kimura', 'Pada hujung minggu encik suka buat apa?'),
                     ('Hafiz', 'Saya suka bermain badminton. Pada hari Sabtu saya berlari di taman.')],
             items=[dict(q='Where is he from, and where does he work?', ja='男性の出身はどこですか。どこで働いていますか。',
                         a='from Penang («berasal dari Penang») (1); at a bank in Bangsar (1)', marks=2, ch=[10], frames=['ms-c10-f05'],
                         words=['berasal', 'bekerja']),
                    dict(q='What time does he set off every morning? What does he do on Saturdays?',
                         ja='毎朝何時に出発しますか。土曜日には何をしますか。',
                         a='at eight («bertolak pukul lapan») (1); he runs in the park («berlari di taman») (1)', marks=2, ch=[10],
                         frames=['ms-c10-f01', 'ms-c10-f03'], words=['bertolak', 'berlari', 'taman'])]),
        dict(title='Who did what? · 誰が何をした？',
             context='«Puan» Aini asks «Encik» Kimura about some slides. / アイニさんが木村さんにスライドについてたずねます。',
             script=[('Aini', 'Encik Kimura, siapa yang membuat slaid ini?'),
                     ('Kimura', 'Cik Devi yang membuat slaid itu. Encik Lim sedang membaca slaid itu sekarang.'),
                     ('Aini', 'Bila slaid itu dihantar kepada bos?'),
                     ('Kimura', 'Slaid itu akan dihantar oleh Encik Lim esok pagi. Tarikh akhir hari Jumaat.')],
             items=[dict(q='Who made the slides, and who is reading them now?', ja='スライドを作ったのは誰ですか。今、読んでいるのは誰ですか。',
                         a='«Cik» Devi (1); «Encik» Lim (1)', marks=2, ch=[11], frames=['ms-c11-f03', 'ms-c11-f05'],
                         words=['membuat', 'membaca', 'slaid']),
                    dict(q='When will the slides be sent to the boss, and when is the deadline?',
                         ja='スライドはいつ上司に送られますか。締め切りはいつですか。',
                         a='tomorrow morning (1); Friday («tarikh akhir hari Jumaat») (1)', marks=2, ch=[11], frames=['ms-c11-f02'],
                         words=['dihantar', 'oleh', 'tarikh akhir'])]),
        dict(title='At the guardhouse · 守衛所で',
             context='«Encik» Kimura goes to the guardhouse for a parcel. / 木村さんが守衛所へ荷物を取りに行きます。',
             script=[('Kimura', 'Selamat malam. Saya mahu ambil bungkusan. Sudah sampai?'),
                     ('Guard', 'Sudah. Ada tiga bungkusan. Encik tinggal di unit berapa?'),
                     ('Kimura', 'Blok C, unit 7-4.'),
                     ('Guard', 'Bungkusan kecil ini untuk encik. Dua bungkusan besar itu untuk unit 7-1. Boleh tunjukkan mesej encik?'),
                     ('Kimura', 'Maaf, saya terlupa nombor penjejakan itu.'),
                     ('Guard', 'Tidak mengapa. Nama dan nombor unit encik ada pada label bungkusan ini.')],
             items=[dict(q='How many parcels are there, and which one is his?', ja='荷物はいくつありますか。木村さんのはどれですか。',
                         a='three (1); the small parcel (1)', marks=2, ch=[12], frames=['ms-c12-f03'], words=['bungkusan', 'unit']),
                    dict(q='What did he forget? What does the guard check instead?', ja='木村さんは何を忘れましたか。守衛は代わりに何を確かめますか。',
                         a='the tracking number («terlupa nombor penjejakan») (1); his name and unit number on the label (1)', marks=2,
                         ch=[16, 12], frames=['ms-c12-f02', 'ms-c16-f02'], words=['terlupa', 'nombor penjejakan', 'label'])]),
        dict(title='An invitation · 招待',
             context='«Cik» Mei Ling invites «Encik» Kimura to lunch. / メイリンさんが木村さんを昼食に招きます。',
             script=[('Mei Ling', 'Encik Kimura, sudikah encik makan tengah hari dengan kami hari Khamis?'),
                     ('Kimura', 'Terima kasih, cik. Sayangnya hari Khamis saya tidak lapang, kerana saya ada mesyuarat.'),
                     ('Mei Ling', 'Tidak mengapa. Bagaimana kalau hari Jumaat, pukul satu?'),
                     ('Kimura', 'Setuju! Hari Jumaat, pukul satu. Saya belanja kopi.')],
             items=[dict(q='Can he come on Thursday? Why or why not?', ja='木曜日に行けますか。理由は何ですか。',
                         a='no («Sayangnya … tidak lapang») (1); he has a meeting (1)', marks=2, ch=[17, 14],
                         frames=['ms-c17-f01', 'ms-c17-f02', 'ms-c14-f02'], words=['sudi', 'sayangnya', 'lapang', 'kerana']),
                    dict(q='What do they agree on, and what will he do?', ja='何を決めましたか。木村さんは何をしますか。',
                         a='Friday at one (1); he will treat them to coffee («Saya belanja kopi») (1)', marks=2, ch=[17],
                         frames=['ms-c17-f03', 'ms-c17-f04', 'ms-c17-f05'], words=['tidak mengapa', 'setuju', 'belanja'])]),
    ],
    reading=[
        dict(title='A notice at a pharmacy · 薬局の掲示',
             text=['A fictional notice:', '«FARMASI · PERHATIAN»', '«Sila ambil nombor dan tunggu. Anda perlu tunjukkan kad klinik.»',
                   '«Borang ini wajib diisi sebelum anda berjumpa ahli farmasi.»', '«Tidak dibenarkan makan dan minum di dalam farmasi.»',
                   '«Farmasi dibuka dari pukul sembilan pagi hingga pukul sembilan malam. Pada hari Sabtu, farmasi ditutup pada pukul satu.»'],
             items=[dict(q='What must you show, and what must you fill in before you see the pharmacist?',
                         ja='何を見せる必要がありますか。薬剤師に会う前に何に記入しなければなりませんか。',
                         a='the clinic card («kad klinik») (1); the form («Borang ini wajib diisi») (1)', marks=2, ch=[13],
                         frames=['ms-c13-f06'], words=['perlu', 'wajib', 'borang', 'isi', 'ahli farmasi']),
                    dict(q='It is Saturday at three in the afternoon. Is the pharmacy open? What is not allowed inside?',
                         ja='土曜日の午後3時です。薬局は開いていますか。中で禁止されていることは何ですか。',
                         a='no, it closes at one on Saturday (1); eating and drinking (1)', marks=2, ch=[13], frames=['ms-c13-f05'],
                         words=['dibenarkan', 'ditutup'])]),
        dict(title='A message from the guardhouse · 守衛所からのメッセージ',
             text=['A fictional WhatsApp message:',
                   '«Selamat petang, Encik Kimura. Ada dua bungkusan untuk encik di pondok pengawal. Satu kotak basah, jadi kami menyimpan kotak '
                   'itu di pejabat. Juruteknik akan datang ke unit encik hari Selasa pukul tiga petang untuk membaiki lampu dapur. Kalau encik '
                   'pulang lewat, sila hubungi pondok pengawal. Terima kasih. Pengawal»'],
             items=[dict(q='Where is the wet box, and why is it there?', ja='濡れた箱はどこにありますか。なぜそこにあるのですか。',
                         a='in the office (1); because it is wet («Satu kotak basah, jadi …») (1)', marks=2,
                         ch=[12, 14], frames=['ms-c12-f03'], words=['bungkusan', 'pondok pengawal', 'basah', 'jadi']),
                    dict(q='When will the technician come, and what will he do? What do you do if you come home late?',
                         ja='技術者はいつ来て、何をしますか。帰りが遅くなるときはどうしますか。',
                         a='Tuesday at three in the afternoon, to repair the kitchen light (1); contact the guardhouse (1)',
                         marks=2, ch=[12, 14], frames=['ms-c12-f04', 'ms-c14-f01', 'ms-c12-f05'], words=['juruteknik', 'membaiki', 'kalau', 'hubungi'])]),
        dict(title='A lost-property form · 遺失物の届け',
             text=['A fictional lost-property form at a shopping centre counter:',
                   '«Barang: payung. Ciri: berwarna hijau, panjang, ada tali hitam. Bentuk: bulat di atas, seperti bola. '
                   'Hilang di: kafe, pukul dua petang.»',
                   'Three umbrellas at the counter:', '«Payung A: payung hijau yang ada tali hitam.»',
                   '«Payung B: payung kecil berwarna hijau yang tidak ada tali.»', '«Payung C: payung hitam yang ada tali hijau.»'],
             items=[dict(q='Which umbrella, A, B or C, is the one on the form?', ja='届けの傘はA・B・Cのどれですか。',
                         a='A (2: the green umbrella that has a black strap)', marks=2, ch=[15],
                         frames=['ms-c15-f01', 'ms-c15-f04', 'ms-c15-f05'], words=['yang', 'berwarna', 'payung', 'tali']),
                    dict(q='Where and when was the umbrella lost? What does its shape look like?', ja='傘はどこで、何時になくなりましたか。形は何のようですか。',
                         a='at the café, at two in the afternoon (1); round at the top, like a ball (1)', marks=2, ch=[15],
                         frames=['ms-c15-f02', 'ms-c15-f06'], words=['hilang', 'bentuk', 'bulat', 'seperti'])]),
        dict(title='An invitation and a reply · 招待と返事',
             text=['A fictional invitation and reply by email:',
                   '«Jemputan makan tengah hari pejabat: hari Rabu, pukul dua belas, di kedai mamak dekat pejabat. Encik Rahman belanja. '
                   'Sila balas sebelum hari Isnin. Cik Mei Ling»',
                   '«Terima kasih atas jemputan cik. Sayangnya hari Rabu saya tidak lapang, kerana saya ke Penang. '
                   'Bagaimana kalau kita minum kopi pada hari Khamis? Kimura»'],
             items=[dict(q='When and where is the lunch? Who pays?', ja='昼食会はいつ、どこですか。誰が払いますか。',
                         a='Wednesday at twelve, at the «kedai mamak» near the office (1); «Encik» Rahman («Encik Rahman belanja») (1)',
                         marks=2, ch=[17], frames=['ms-c17-f01'], words=['jemputan', 'belanja', 'balas']),
                    dict(q='Does Kimura accept? Why or why not? What does he suggest?', ja='木村さんは受けますか。理由は何ですか。何を提案していますか。',
                         a='no, because he is going to Penang («kerana saya ke Penang») (1); coffee on Thursday (1)', marks=2, ch=[17, 14],
                         frames=['ms-c17-f02', 'ms-c17-f03', 'ms-c14-f02'], words=['sayangnya', 'lapang', 'kerana', 'bagaimana', 'kalau'])]),
        dict(title='A note about a small accident · 小さな事故のメモ',
             text=['A fictional note on the office board:',
                   '«Semalam air teh tertumpah di lantai dapur. Puan Aini tergelincir, tetapi dia tidak apa-apa. Lantai itu sudah '
                   'dibersihkan oleh Encik Lim. Hati-hati di dapur.»'],
             items=[dict(q='What spilt, and what happened to «Puan» Aini?', ja='何がこぼれましたか。アイニさんはどうなりましたか。',
                         a='tea, on the kitchen floor («tertumpah di lantai dapur») (1); she slipped but is all right (1)', marks=2,
                         ch=[16], frames=['ms-c16-f03'], words=['tertumpah', 'tergelincir', 'tidak apa-apa']),
                    dict(q='Who cleaned the floor? What does the note ask you to do?', ja='床をきれいにしたのは誰ですか。メモは何をするように言っていますか。',
                         a='«Encik» Lim («dibersihkan oleh Encik Lim») (1); be careful in the kitchen («Sila hati-hati») (1)', marks=2, ch=[11, 16],
                         frames=['ms-c11-f02'], words=['bersihkan', 'oleh'])]),
    ],
    writing=[
        dict(title='A lost-property form · 遺失物の届け',
             intro='You left something in a taxi. Fill in the taxi company\'s lost-property form in Malay (fictional). If you prefer, use '
                   'this card: Yamada Yuki, phone 017-222 3344, a red bag, round, with a long strap, brand Sakura, lost on 3 June at '
                   'about nine at night, in a taxi from KL Sentral. / タクシーに物を忘れました。タクシー会社の遺失物の届け（架空）を'
                   'マレー語で記入しましょう。このカードを使ってもかまいません：山田ゆき、電話 017-222 3344、赤いかばん、丸い、長い'
                   'ひも付き、ブランドはサクラ、6月3日の夜9時ごろ、KLセントラルからのタクシーでなくした。',
             form=['«Borang barang hilang»', '«Nama»', '«Nombor telefon»', '«Barang»', '«Warna»', '«Bentuk»', '«Ciri»',
                   '«Jenama»', '«Tarikh»', '«Masa»', '«Hilang di»'],
             items=[dict(q='Fill in the ten fields of the form.', ja='届けの10の欄を記入しましょう。',
                         a='One mark per field when the answer is true for the learner (or the card) and in Malay where a Malay word '
                           'is needed; a spelling slip that does not change the word is not penalised; any natural Malaysian answer '
                           'with the same meaning is accepted. Card answers: 1 «Yamada Yuki»; 2 «017-222 3344»; 3 «beg»; '
                           '4 «merah»; 5 «bulat»; 6 «ada tali panjang» (or «beg yang ada tali panjang»); 7 «Sakura»; '
                           '8 «3 Jun»; 9 «pukul sembilan malam» (or «lebih kurang pukul sembilan malam»); 10 «teksi» (or «di dalam teksi dari KL Sentral»).',
                         marks=10, ch=[15, 3, 4], frames=['ms-c15-f04', 'ms-c15-f06'],
                         words=['barang', 'hilang', 'warna', 'bentuk', 'ciri', 'jenama', 'tarikh'])]),
        dict(title='A message to change a plan · 予定を変えるメッセージ',
             intro='You and two friends planned to have dinner at a café on Friday. Write a WhatsApp message of five to seven sentences '
                   'to the group: say why you cannot come on Friday; ask to put the dinner off to Saturday; give one condition (if the '
                   'café is full); put the Saturday plan in order (first, then, finally) with a time and a meeting place; and close. / '
                   '友人二人と金曜日にカフェで夕食の予定でした。グループに WhatsApp のメッセージを5〜7文で書きましょう：金曜日に'
                   '行けない理由、土曜日への延期の提案、条件を一つ（カフェが満席なら）、土曜日の予定を順番に（まず・それから・最後に）'
                   '時刻と集合場所を入れて、結びのあいさつ。',
             form=[],
             items=[dict(q='Write the message.', ja='メッセージを書きましょう。',
                         a='Content 4: the reason 1; the new day 1; the condition 1; the plan in order with a time and a place 1. '
                           'Language 4: a reason with «kerana» or «sebab» 1; a condition with «kalau» or «jika» 1; putting off with '
                           '«tangguhkan» (or «Boleh kita … ke hari Sabtu?») 1; the order with «mula-mula», «kemudian» (or «selepas itu») and '
                           '«akhirnya» 1. Accuracy 2: 2 = Malaysian standard forms, inclusive «kita» for the group and the meaning always '
                           'clear; 1 = a few slips, the meaning clear; 0 = the meaning often unclear. Accept the natural variants '
                           '«kalau» / «jika», «kerana» / «sebab», «kemudian» / «selepas itu», «tangguhkan» / «menangguhkan» '
                           '(after a third-person doer); standard written forms are always right; spoken forms are accepted where the '
                           'meaning is clear but are not needed. Model: «Selamat pagi, semua. Maaf, hari Jumaat saya tidak boleh datang '
                           'kerana saya ada mesyuarat. Boleh kita tangguhkan rancangan makan malam ke hari Sabtu? Kalau kafe itu penuh, kita makan di '
                           'kedai mamak. Mula-mula kita berjumpa di stesen pukul tujuh, kemudian kita makan, akhirnya kita minum teh tarik. '
                           'Jumpa hari Sabtu!»', marks=10, ch=[14, 10, 17],
                         frames=['ms-c14-f01', 'ms-c14-f02', 'ms-c14-f06', 'ms-c18-f04'],
                         words=['kerana', 'kalau', 'tangguhkan', 'mula-mula', 'kemudian', 'akhirnya'])]),
    ],
    speaking=dict(
        intro=dict(q='Self-introduction and a working day (about two minutes). Introduce yourself to a new neighbour: greet; where you '
                     'are from and where you work; what you do on a working day, with two times; and one thing you like doing at the '
                     'weekend. The examiner then asks one question and invites you to something: accept or decline with a reason.',
                   ja='自己紹介と仕事の一日（約2分）。新しい隣人に自己紹介しましょう：あいさつ、出身と勤め先、仕事の日にすること（時刻を'
                      '二つ入れて）、週末に好きなことを一つ。そのあと試験官が質問を一つして、何かに誘います。理由を言って受けるか断りましょう。',
                   examiner=['«Selamat petang. Saya Siti, jiran baru. Encik berasal dari mana?» (or «puan», «cik»)',
                             'Follow-up: «Pukul berapa encik balik dari pejabat?»',
                             'Invitation: «Sudikah encik datang ke rumah saya hari Ahad? Kami berkumpul pukul empat.»'],
                   a='Content 4: greeting, origin and workplace 1; a working day with two times 1; a weekend activity 1; the follow-up '
                     'answered in a sentence 1. Language 2: 2 = ber- and meN- verbs right («berasal», «bekerja», «bertolak», '
                     '«menulis»), «pukul» with the times; 1 = some slips; 0 = mostly single words. Interaction 2: accepts or declines '
                     'the invitation clearly 1; gives a reason («kerana» / «sebab») or another time 1. ‹lah› and ‹kan› are not needed; '
                     'a declined invitation with «Sayangnya …» or «Maaf, …» is as good as an accepted one. Model: «Selamat petang. Saya '
                     'Yamada. Saya berasal dari Kyoto. Saya bekerja di Cyberjaya. Setiap pagi saya bertolak pukul lapan, kemudian saya '
                     'menulis emel. Saya balik pukul enam. Pada hujung minggu saya suka berbasikal.» Follow-up: «Saya balik pukul enam.» '
                     'Invitation: «Terima kasih. Sayangnya hari Ahad saya tidak lapang, kerana kawan saya datang. Lain kali, ya?» '
                     'or «Terima kasih, saya akan datang.»',
                   marks=8, ch=[10, 11, 14, 17], frames=['ms-c10-f01', 'ms-c10-f05', 'ms-c18-f01', 'ms-c17-f02'],
                   words=['berasal', 'bekerja', 'bertolak', 'sudi', 'sayangnya', 'kerana']),
        cards=[
            dict(title='Card 1 · A parcel for a neighbour (request)', ja_title='カード1・隣人の荷物（依頼）',
                 tasks=['Tell the guard you have come for your parcel and give your block and unit.',
                        'Ask whether it has arrived and show a message.', 'Ask the guard to send a second parcel to your neighbour\'s unit.'],
                 tasks_ja=['荷物を取りに来たと守衛に言い、ブロックと部屋番号を伝えましょう。', '届いているかたずね、メッセージを見せましょう。',
                           'もう一つの荷物を隣人の部屋に届けてくれるよう頼みましょう。'],
                 examiner=['You are the guard: «Selamat malam. Ada apa, cik?»', '«Ada tiga bungkusan. Boleh tunjukkan mesej?»',
                           'Change of plan: «Maaf, nama pada label ini bukan nama cik.» (the learner gives the unit again and asks the guard to check)'],
                 a='Task 3: «Saya mahu ambil bungkusan …» with the block and unit 1; asks «Sudah sampai?» and offers the message 1; the '
                   'request with ‹-kan› («Tolong hantarkan …») 1. Language 2: the ‹-kan› request and «Boleh …?» right 2, partly 1. '
                   'Change of plan 1: gives the unit again and asks the guard to check. Model: «Saya mahu ambil bungkusan. Sudah sampai? '
                   'Saya tinggal di Blok C, unit 7-4. Ini mesej saya. Tolong hantarkan bungkusan besar itu ke unit 7-1.»',
                 marks=6, ch=[12], frames=['ms-c12-f01', 'ms-c12-f03', 'ms-c18-f02'], words=['bungkusan', 'hantarkan', 'unit']),
            dict(title='Card 2 · Water on the bathroom floor (request)', ja_title='カード2・浴室の床の水（依頼）',
                 tasks=['Report a leak in your bathroom to the management office.', 'Ask them to contact a technician.',
                        'Agree a day and a time for the visit.'],
                 tasks_ja=['浴室の水漏れを管理事務所に伝えましょう。', '技術者に連絡してくれるよう頼みましょう。', '来てもらう日と時刻を決めましょう。'],
                 examiner=['You are the management office: «Pejabat pengurusan. Ada masalah?»',
                           '«Baik. Juruteknik boleh datang hari Isnin pukul dua petang.»',
                           'Change of plan: «Maaf, hari Isnin juruteknik tidak boleh datang. Bagaimana kalau hari Selasa?» (the learner agrees or gives another time)'],
                 a='Task 3: «Ada kebocoran di bilik air saya.» 1; «Boleh hubungi juruteknik?» or «Tolong hubungi …» 1; agrees a day and a '
                   'time 1. Language 2: the ‹-i› request and the place right 2, partly 1. Change of plan 1: accepts the new day or gives '
                   'another time with a reason. Model: «Ada kebocoran di bilik air saya. Boleh hubungi juruteknik? Hari Isnin pukul dua, '
                   'boleh.» After the change: «Hari Selasa boleh. Pukul berapa?»',
                 marks=6, ch=[12, 14], frames=['ms-c12-f05', 'ms-c12-f06'], words=['kebocoran', 'bilik air', 'hubungi', 'juruteknik']),
            dict(title='Card 3 · A phone left at the office (mishap)', ja_title='カード3・事務所に置き忘れた電話（トラブル）',
                 tasks=['Tell the office guard that you left your phone in the office.', 'Say what happened (you forgot it on your desk).',
                        'Ask for one practical next step.'],
                 tasks_ja=['事務所に電話を置き忘れたと警備員に伝えましょう。', '何が起きたか言いましょう（机の上にうっかり忘れた）。',
                           '具体的な次の対応を一つ頼みましょう。'],
                 examiner=['You are the guard: «Ya, cik? Ada masalah?»', '«Pejabat cik di tingkat berapa?»',
                           'Change of plan: «Maaf, pintu pejabat itu sudah terkunci.» (the learner asks for another step, for example to call a colleague)'],
                 a='Task 3: «Saya tertinggal telefon di pejabat.» 1; «Maaf, saya terlupa.» and where it is 1; a clear request («Boleh '
                   'tolong bukakan pintu pejabat?») 1. Language 2: accident ‹ter-› forms right 2, partly 1. Change of plan 1: asks '
                   'another step («Boleh saya pinjam telefon encik?»). Model: «Maaf, saya tertinggal telefon di pejabat, di atas meja saya. '
                   'Saya terlupa. Boleh tolong bukakan pintu pejabat?»',
                 marks=6, ch=[16], frames=['ms-c16-f01', 'ms-c16-f02', 'ms-c16-f06', 'ms-c18-f06'], words=['tertinggal', 'terlupa', 'terkunci']),
            dict(title='Card 4 · A broken cup at a café (mishap)', ja_title='カード4・カフェで割れたカップ（トラブル）',
                 tasks=['Tell the café worker what happened: you knocked a cup off the table by accident.', 'Apologise.',
                        'Offer one thing you will do now.'],
                 tasks_ja=['何が起きたかカフェの店員に言いましょう：誤ってカップをテーブルから落としました。', 'あやまりましょう。',
                           '今からすることを一つ申し出ましょう。'],
                 examiner=['You are the café worker: «Apa yang berlaku, cik?»', '«Cik tidak apa-apa?»',
                           'Change of plan: «Air kopi itu pun tertumpah di beg cik!» (the learner checks the bag and asks for help)'],
                 a='Task 3: «Cawan itu terjatuh ke lantai.» or «Saya terlanggar cawan itu.» 1; «Maaf, saya tidak sengaja.» 1; offers a '
                   'step with a first-person form («Saya bayar cawan itu.» or «Saya bersihkan meja ini.») 1. Language 2: ‹ter-› and '
                   '«tidak sengaja» right 2, partly 1. Change of plan 1: asks for help («Boleh saya ambil tisu?»). Model: «Maaf, saya '
                   'tidak sengaja terlanggar cawan itu. Cawan itu terjatuh ke lantai dan pecah. Saya bayar cawan itu.»',
                 marks=6, ch=[16], frames=['ms-c16-f03', 'ms-c16-f04'], words=['terjatuh', 'tidak sengaja', 'terlanggar']),
        ]),
)
