"""Unit 3C: ordinals, fractions, percentages, weights and sizes.

Scenes: the morning market (fractions of a kilo, a discount) and the post office
(sending a parcel: weight, length, width, height). In speech, sizes use the
adjectives panjang, lebar, tinggi and berat; the ke- ... -an nouns from the
Kata-Kata cards are taught as written labels. Rewritten by Claude on
12 Nov 2026 after review (natural scenes, real culture note, answer keys).
"""
from .chapter3_common import unit_dict

CORE=[f'L-{i:04d}' for i in range(133,154)]+['L-0999','L-1001','L-1002']
RECOG=[f'L-{i:04d}' for i in range(423,431)]
REV=['L-0100','L-0101','L-0105','L-0113','L-0116','L-0117','L-0118',
     'L-0126','L-0990']
EXAMPLES={
'L-0133':'«Ini kali kedua saya di Malaysia.»',
'L-0134':'«Ini kali pertama saya di Malaysia.»',
'L-0135':'«Ini kali kedua saya di pasar ini.»',
'L-0136':'«Ini kali ketiga saya di pejabat pos ini.»',
'L-0137':'«Ini kali kesepuluh saya di Malaysia!»',
'L-0138':'«Saya beli setengah kilo.» («separuh» also means half)',
'L-0139':'«Saya beli suku kilo pisang.»',
'L-0140':'«Saya beli tiga suku kilo mangga.»',
'L-0141':'«Satu per tiga untuk saya.» («sepertiga» is the same fraction)',
'L-0142':'«Berat bungkusan ini satu perpuluhan lima kilo.»',
'L-0143':'«Diskaun dua puluh peratus.»',
'L-0144':'«Kawan saya tinggi.»',
'L-0145':'«Berat bungkusan ini dua kilo.»',
'L-0146':'«Panjang bungkusan ini tiga puluh sentimeter.»',
'L-0147':'«Lebar bungkusan ini dua puluh sentimeter.»',
'L-0148':'On a form: «Ketinggian: seratus tujuh puluh lima sentimeter.» (in speech: «tinggi»)',
'L-0149':'On a label: «Kepanjangan: tiga puluh sentimeter.» (in speech: «panjang»)',
'L-0150':'On a label: «Kelebaran: dua puluh sentimeter.» (in speech: «lebar»)',
'L-0151':'On a label: «Kedalaman: lima belas sentimeter.»',
'L-0152':'«Seratus sentimeter ialah satu meter.»',
'L-0153':'«Saya beli satu kilo mangga.»',
'L-0999':'«Jumlah ialah sepuluh ringgit.»',
'L-1001':'«Harga selepas diskaun lapan ringgit.»',
'L-1002':'«Harga sebelum diskaun sepuluh ringgit.»',
'L-0423':'Post office or bank: «Kaunter tiga.»',
'L-0424':'«Saya tarik duit dulu.» (spoken)',
'L-0425':'«Pejabat pos di mana?»',
'L-0426':'«Ini surat untuk encik.»',
'L-0427':'«Berapa harga setem ini?»',
'L-0428':'«Ini alamat kawan saya.»',
'L-0429':'«Berapa poskod pejabat encik?»',
'L-0430':'«Bungkusan ini untuk kawan saya di Osaka.»',
'L-0100':'«Satu kilo.»',
'L-0101':'«Dua kilo.»',
'L-0105':'«Enam ringgit.»',
'L-0113':'«Seratus sentimeter.»',
'L-0116':'«Berapa harga ini?»',
'L-0117':'«Berapa harga mangga ini?»',
'L-0118':'«Harganya lapan ringgit.»',
'L-0126':'«Diskaun sepuluh peratus.»',
'L-0990':'«Dua puluh peratus.»',
}
P=[
('ms-c03-f04','«Ini kali» [«pertama» / «kedua» / «ketiga»] «saya di» ___.',[
'A: «Ini kali pertama encik di Malaysia?» B: «Ya, kali pertama.»',
'A: «Ini kali kedua encik di pasar ini?» B: «Ya, kali kedua.»',
'A: «Ini kali ketiga encik di pejabat pos ini?» B: «Bukan, kali kedua.»',
'A: «Ini kali kesepuluh encik di Malaysia?» B: «Ya, kali kesepuluh!»'],
'«kali» counts occasions. First is «pertama» (irregular); from two onwards the ordinal is built on the number: «dua» → «kedua», «tiga» → «ketiga», «sepuluh» → «kesepuluh».',
'«kali» は回数です。「1回目」は不規則な «pertama»。2以降は数字から作ります：«dua»→«kedua»、«tiga»→«ketiga»、«sepuluh»→«kesepuluh»。',
'Japanese 〜回目 attaches to every number, including 1回目. Malay first is a separate word, «pertama».',
'日本語の「〜回目」は1にも付きますが、マレー語の「1回目」は別の語 «pertama» です。'),
('ms-c03-f05','«Diskaun» ___ «peratus».',[
'A: «Diskaun berapa peratus?» B: «Sepuluh peratus.»',
'A: «Diskaun dua puluh peratus?» B: «Ya, dua puluh peratus.»',
'A: «Diskaun lima puluh peratus?» B: «Bukan, sepuluh peratus.»',
'A: «Harga sebelum diskaun sepuluh ringgit. Selepas diskaun?» B: «Lapan ringgit.»'],
'«peratus» follows the number: «dua puluh peratus» (20%). Use «sebelum» and «selepas» for the price before and after the discount.',
'«peratus» は数字の後ろです：«dua puluh peratus»（20%）。割引前・割引後の値段は «sebelum»・«selepas» で言います。',
'Japanese signs often say 2割引 as well as 20%OFF. Malay signs use the percentage.',
'日本では「2割引」とも書きますが、マレー語の表示はパーセントです。'),
('ms-c03-f06','«Berapa» [«panjang» / «lebar» / «tinggi» / «berat»] ___? — ___ «sentimeter» / «kilo».',[
'A: «Berapa panjang bungkusan ini?» B: «Tiga puluh sentimeter.»',
'A: «Berapa lebar bungkusan ini?» B: «Dua puluh sentimeter.»',
'A: «Berapa tinggi bungkusan ini?» B: «Sepuluh sentimeter.»',
'A: «Berapa berat bungkusan ini?» B: «Dua kilo.»'],
'In speech, ask with «berapa» plus the adjective, and answer with the number and unit («Panjang tiga puluh sentimeter»). '
'The nouns «ketinggian», «kepanjangan», «kelebaran» and «kedalaman» are the written forms you see on forms and labels.',
'会話では «berapa» ＋形容詞でたずね、数字と単位で答えます（«Panjang tiga puluh sentimeter»）。'
'«ketinggian»・«kepanjangan»・«kelebaran»・«kedalaman» は書類やラベルで見る書き言葉の名詞です。',
'Japanese 長さ・幅・高さ are everyday words, but «kepanjangan» and «kelebaran» are formal. For 長さは？ in conversation say «Berapa panjang?»',
'日本語の「長さ・幅・高さ」は会話でも使いますが、«kepanjangan»・«kelebaran» は改まった語です。会話の「長さは？」は «Berapa panjang?» です。'),
('ms-c03-f06','Fractions and decimals: «setengah», «suku», «perpuluhan».',[
'A: «Berapa kilo?» B: «Setengah kilo.»',
'A: «Berapa kilo?» B: «Suku kilo.»',
'A: «Berapa kilo?» B: «Tiga suku kilo.»',
'A: «Berat satu perpuluhan lima kilo?» B: «Ya, satu perpuluhan lima kilo.»'],
'«setengah» (or «separuh») is a half, «suku» a quarter, «tiga suku» three quarters. «perpuluhan» reads the decimal point: 1.5 = «satu perpuluhan lima».',
'«setengah»（または «separuh»）＝半分、«suku»＝4分の1、«tiga suku»＝4分の3。«perpuluhan» は小数点の読み方です：1.5＝«satu perpuluhan lima»。',
'Japanese reads 1.5 as いってんご. Malay reads the point as a word, «perpuluhan».',
'日本語の「いってんご」の「てん」に当たるのが «perpuluhan» です。'),
]
DIALOGUE=[
('Tanaka','Selamat pagi, puan. Ini kali pertama saya di pejabat pos ini.'),
('Aini','Selamat pagi, encik. Bungkusan ini untuk siapa?'),
('Tanaka','Untuk kawan saya di Osaka.'),
('Aini','Baik. Saya timbang dulu. Berat dua kilo.'),
('Tanaka','Dua kilo. Berapa harganya?'),
('Aini','Sebelum itu, berapa panjang dan lebar bungkusan ini?'),
('Tanaka','Panjang tiga puluh sentimeter, lebar dua puluh sentimeter.'),
('Aini','Tinggi pula?'),
('Tanaka','Tinggi sepuluh sentimeter.'),
('Aini','Baik. Jumlah empat puluh lima ringgit.'),
('Tanaka','Boleh bayar dengan kad?'),
('Aini','Boleh. Sebelum bayar, encik isi borang ini, ya.')]
VARIANT=[
('Yuki','Selamat petang, encik. Ini kali kedua saya di pejabat pos ini.'),
('Hafiz','Selamat petang, cik. Bungkusan ini untuk siapa?'),
('Yuki','Untuk keluarga saya di Kyoto.'),
('Hafiz','Baik. Saya timbang dulu. Berat satu perpuluhan lima kilo.'),
('Yuki','Satu perpuluhan lima kilo. Berapa harganya?'),
('Hafiz','Sebelum itu, berapa panjang dan lebar bungkusan ini?'),
('Yuki','Panjang empat puluh sentimeter, lebar tiga puluh sentimeter.'),
('Hafiz','Tinggi pula?'),
('Yuki','Tinggi dua puluh sentimeter.'),
('Hafiz','Baik. Jumlah tiga puluh lima ringgit.'),
('Yuki','Saya bayar tunai. Ini lima puluh ringgit.'),
('Hafiz','Terima kasih, cik. Baki lima belas ringgit.')]
LISTENING=[
('Aini','Selamat pagi, encik. Mangga ini segar. Harganya sepuluh ringgit satu kilo.'),
('Tanaka','Selamat pagi, mak cik. Ini kali kedua saya di pasar ini. Saya beli setengah kilo, ya.'),
('Aini','Baik. Setengah kilo, lima ringgit. Pagi ini ada diskaun dua puluh peratus.'),
('Tanaka','Dua puluh peratus? Harga selepas diskaun empat ringgit, betul?'),
('Aini','Ya, betul. Sebelum diskaun lima ringgit, selepas diskaun empat ringgit.'),
('Tanaka','Saya beli pisang juga. Suku kilo sahaja.'),
('Aini','Suku kilo pisang, dua ringgit. Jumlah enam ringgit.'),
('Tanaka','Ini sepuluh ringgit.'),
('Aini','Terima kasih. Baki empat ringgit. Jumpa lagi!'),
('Farah','Selamat pagi, encik. Bungkusan ini untuk siapa?'),
('Tanaka','Untuk kawan saya di Osaka. Ini alamat dan poskod dia.'),
('Farah','Baik. Saya timbang dulu. Berat satu perpuluhan lima kilo.'),
('Tanaka','Satu perpuluhan lima kilo. Berapa harganya?'),
('Farah','Sebelum itu, berapa panjang, lebar dan tinggi bungkusan ini?'),
('Tanaka','Panjang empat puluh sentimeter, lebar tiga puluh sentimeter dan tinggi dua puluh sentimeter.'),
('Farah','Baik. Jumlah tiga puluh lima ringgit. Encik bayar dengan kad?'),
('Tanaka','Ya, dengan kad. Terima kasih, puan.')]
CULTURE=[
'Malaysia uses the metric system. At a «pasar» (a wet market or morning market), fruit, vegetables and fish are sold by weight, '
'and the seller weighs your order on a scale. Asking for «setengah kilo» or «suku kilo» is normal; you do not have to buy a whole kilo. '
'Shop signs show discounts as percentages, such as «Diskaun 20%», read aloud as «diskaun dua puluh peratus». '
'Decimals are read with «perpuluhan»: 1.5 kilo is «satu perpuluhan lima kilo» (Kata-Kata card ms-c03-044).',
'For sizes, everyday speech uses the adjective itself: «Berapa panjang bungkusan ini?» «Panjang tiga puluh sentimeter.» '
'The nouns «ketinggian», «kepanjangan», «kelebaran» and «kedalaman» are built from «tinggi», «panjang», «lebar» and ‹dalam› '
'(Kata-Kata cards ms-c03-050 to ms-c03-053). You meet them mostly in writing: on forms, labels and product descriptions. '
'«kepanjangan» can also mean the full form of an abbreviation, so in conversation «panjang» is the safer choice.',
'For ordinals, «pertama» is irregular: everyday Malay does not say ‹kesatu› (Kata-Kata card ms-c03-036). '
'From two onwards the ordinal is built on the number: «dua» → «kedua», «tiga» → «ketiga». '
'«Ini kali pertama saya di Malaysia» is a natural thing to say when you meet someone new, and a Malaysian may well ask '
'«Ini kali pertama encik di Malaysia?» when you arrive.']
CULTURE_JA=[
'マレーシアはメートル法を使います。«pasar»（ウェットマーケットや朝市）では果物・野菜・魚を重さで売り、店の人がはかりで量ってくれます。'
'«setengah kilo»（500グラム）や «suku kilo»（250グラム）を頼むのは普通で、1キロ単位で買う必要はありません。'
'店の割引表示は «Diskaun 20%» のようにパーセントで書かれ、«diskaun dua puluh peratus» と読みます。'
'小数は «perpuluhan» で読みます：1.5キロは «satu perpuluhan lima kilo»（Kata-Kata カード ms-c03-044）。',
'大きさを言うとき、日常の会話では形容詞をそのまま使います：«Berapa panjang bungkusan ini?»（この小包の長さは？）«Panjang tiga puluh sentimeter.»（長さ30センチです）。'
'«ketinggian»・«kepanjangan»・«kelebaran»・«kedalaman» は «tinggi»・«panjang»・«lebar»・‹dalam› から作られた名詞です（Kata-Kata カード ms-c03-050〜053）。'
'主に書類・ラベル・商品説明などの書き言葉で見かけます。«kepanjangan» は略語の「正式名称」の意味でも使われるので、会話では «panjang» を使うほうが無難です。',
'序数では «pertama»（1番目）が不規則で、日常では ‹kesatu› とは言いません（Kata-Kata カード ms-c03-036）。'
'2以降は数字から作ります：«dua»→«kedua»、«tiga»→«ketiga»。'
'«Ini kali pertama saya di Malaysia»（マレーシアは初めてです）は初対面でよく使う自然な一言で、'
'到着したときに «Ini kali pertama encik di Malaysia?»（マレーシアは初めてですか）と聞かれることもよくあります。']
CFG=dict(
 label='3C',unit_goal='Use ordinals, fractions and percentages; ask and give the weight and size of a parcel.',
 core=CORE,recognition=RECOG,revision=REV,grammar=['ordinals','fractions','measures'],
 examples=EXAMPLES,core_heading='Ordinals, fractions, percent and measures',
 dunia_title='Ke bank dan pejabat pos',
 goals={'A':'I can say ordinal positions, common fractions and percentages.',
        'B':'I can ask and answer about quantities and the size of a parcel.',
        'C':'I can read a receipt and a parcel label, and write a label.',
        'D':'I can distinguish ordinal, fraction, percent and size forms.',
        'E':'I can recognise remaining bank and post-office words.'},
 goals_ja={'A':'序数・分数・割合が言える。',
           'B':'量と小包の大きさをたずねて答えられる。',
           'C':'レシートと小包のラベルを読み、ラベルを書ける。',
           'D':'序数・分数・割合・大きさの表現を区別できる。',
           'E':'銀行・郵便局の場面語を聞いて分かる。'},
 setting='Saturday morning errands: the morning market, then the post office. All prices, weights and sizes are fictional.',
 patterns=P,pattern_ids=['ms-c03-f04','ms-c03-f05','ms-c03-f06'],dialogue=DIALOGUE,variant=VARIANT,
 drills={
 'repeat':['«Kali pertama.»','«Kali kedua.»','«Kali ketiga.»','«Setengah kilo.»',
           '«Suku kilo.»','«Tiga suku kilo.»','«Dua puluh peratus.»',
           '«Panjang tiga puluh sentimeter.»'],
 'substitute':['«Ini kali pertama.» (cue: kedua)','«Ini kali kedua.» (cue: ketiga)',
               '«Setengah kilo.» (cue: suku)','«Suku kilo.» (cue: tiga suku)',
               '«Diskaun sepuluh peratus.» (cue: dua puluh)',
               '«Panjang bungkusan ini tiga puluh sentimeter.» (cue: lebar)',
               '«Lebar bungkusan ini tiga puluh sentimeter.» (cue: tinggi, sepuluh)',
               '«Berat bungkusan ini dua kilo.» (cue: setengah kilo)'],
 'transform':['Make ordinal: «dua» → ___.',
              'Make ordinal: «tiga» → ___.',
              'Say one half in Malay.',
              'Say one quarter in Malay.',
              'Say three quarters in Malay.',
              'Read 2.5 with «perpuluhan».',
              'Say 50% with «peratus».',
              'Say this label the spoken way: «Kelebaran: dua puluh sentimeter.»'],
 'qa':['«Ini kali kedua?» (yes)','«Ini kali ketiga?» (no, second)',
       '«Berapa kilo?» (half)','«Berapa kilo?» (quarter)',
       '«Diskaun berapa peratus?» (20)','«Berapa tinggi bungkusan ini?» (10 cm)',
       'Answer: «Empat puluh sentimeter.» Ask the length.',
       'Answer: «Tiga puluh sentimeter.» Ask the width.'],
 'choice':['___ harga selepas diskaun? → «Lapan ringgit.»',
           '___ nama encik? → «Tanaka.»',
           '___ khabar? → «Baik.»',
           '«Pejabat pos ___?» → «Di Bangsar.»',
           '___ saya tanya? → «Boleh.»',
           '___ encik orang Jepun? → «Ya.»',
           '___ nama puan? (formal -kah) → «Aini.»',
           '___ kilo mangga? → «Setengah kilo.»']},
 drill_keys={
 'repeat':['Read each line twice. Check «pertama» (never ‹kesatu›) and that every number has its unit.'],
 'substitute':['1 «Ini kali kedua.» 2 «Ini kali ketiga.» 3 «Suku kilo.» 4 «Tiga suku kilo.»',
               '5 «Diskaun dua puluh peratus.» 6 «Lebar bungkusan ini tiga puluh sentimeter.»',
               '7 «Tinggi bungkusan ini sepuluh sentimeter.» 8 «Berat bungkusan ini setengah kilo.»'],
 'transform':['1 «kedua» 2 «ketiga» 3 «setengah» (or «separuh») 4 «suku» 5 «tiga suku»',
              '6 «dua perpuluhan lima» 7 «lima puluh peratus» 8 «Lebar dua puluh sentimeter.»'],
 'question and answer':['1 «Ya, kali kedua.» 2 «Bukan, kali kedua.» 3 «Setengah kilo.» 4 «Suku kilo.»',
                        '5 «Dua puluh peratus.» 6 «Sepuluh sentimeter.» 7 «Berapa panjang bungkusan ini?» 8 «Berapa lebar bungkusan ini?»'],
 'question-word choice':['1 «Berapa» 2 «Siapa» 3 «Apa» 4 «di mana» 5 «Bolehkah» 6 «Adakah» 7 «Siapakah» 8 «Berapa»']},
 short_dialogues=[
 ('Ini kali pertama encik di Malaysia?','Bukan, kali kedua.','meeting someone new'),
 ('Berapa kilo mangga?','Setengah kilo.','at the morning market'),
 ('Diskaun berapa peratus?','Dua puluh peratus.','a discount sign'),
 ('Berapa berat bungkusan ini?','Dua kilo.','a parcel at the post office')],
 short_keys=['1 «Oh, kali kedua! Selamat datang lagi.» 2 «Baik. Berapa harganya?»',
             '3 «Harga selepas diskaun berapa?» 4 «Berapa panjang bungkusan ini?»'],
 question_tasks=['Ask how someone is.','Ask who the parcel is for.','Ask where the post office is.',
                 'Ask the clerk’s name with the formal -kah form.',
                 'Ask whether this is the customer’s first visit with «Adakah».',
                 'Ask whether you can pay by card with «Bolehkah».',
                 'Ask the width of a parcel with «berapa».'],
 listening=LISTENING,
 listening_context='Saturday morning: fruit at the morning market, then a parcel at the post office (fictional prices)',
 listen_questions=['Which visit to this market is it for Tanaka?','How much mango does he buy?',
                   'What discount is there this morning?','What does his mango cost after the discount?',
                   'How many bananas does he buy?','How much change does he get at the market?',
                   'How heavy is the parcel?','What are the length, width and height of the parcel?'],
 listen_answers=['the second («kali kedua»)','half a kilo','20%','RM4','a quarter kilo','RM4',
                 '1.5 kg','40 cm, 30 cm, 20 cm'],
 test_listen_lines=[1,2,3,11,15],
 test_listen_answers=['second visit; half a kilo','RM5; 20% discount','RM4 after the discount','1.5 kg','RM35'],
 reading_title='Reading and writing · A market receipt and a parcel label',
 reading=['Fictional market receipt: «Mangga» «setengah kilo» RM5.00 · «Diskaun» «dua puluh peratus» -RM1.00 · '
          '«Pisang» «suku kilo» RM2.00 · «Jumlah» RM6.00 · «Tunai» RM10.00 · «Baki» RM4.00.',
          'Fictional parcel label: «Berat» 1.5 «kilo» · «Kepanjangan» 40 «sentimeter» · «Kelebaran» 30 «sentimeter» · «Ketinggian» 20 «sentimeter».'],
 read_questions=['How much mango was bought?','What discount is shown?',
                 'What is the total?','How much change was given?',
                 'How long is the parcel?','Say the width of the parcel the spoken way.'],
 read_answers=['«setengah kilo»','20%','RM6','RM4','40 cm','«Lebar tiga puluh sentimeter.»'],
 write_instruction='Write a fictional label for a parcel to a friend: weight, length, width and height, each with a unit. Then say it aloud the spoken way.',
 write_model='«Berat» 2 «kilo» · «Kepanjangan» 30 «sentimeter» · «Kelebaran» 20 «sentimeter» · «Ketinggian» 10 «sentimeter». '
             'Spoken: «Berat dua kilo. Panjang tiga puluh sentimeter, lebar dua puluh sentimeter, tinggi sepuluh sentimeter.»',
 writing_type='composition',
 task_title='Task · Send a parcel at the post office',
 role_a=['Customer: you have a fictional parcel for a friend in Osaka: 2 kg, 30 cm long, 20 cm wide, 10 cm high.',
         'Say whether this is your first or second visit, answer the clerk, then ask the price and pay.'],
 role_b=['Post-office clerk: ask who the parcel is for, then its weight, length, width and height.',
         'Give a fictional total between RM40 and RM60 and ask how the customer will pay.'],
 change=['The customer adds a second parcel: half a kilo, 20 cm × 15 cm × 5 cm. B asks the sizes again and gives a new total.'],
 success=['☐ B asks «Berapa berat», «Berapa panjang», «Berapa lebar» and «Berapa tinggi».',
          '☐ A answers every size with a unit.',
          '☐ «kali pertama» or «kali kedua», the fraction and the total are said correctly.'],
 task_key='«Berapa berat bungkusan ini?» — «Dua kilo.» «Berapa panjang?» — «Tiga puluh sentimeter.» «Jumlah empat puluh lima ringgit.»',
 culture=CULTURE,culture_ja=CULTURE_JA,
 quiz_words=['L-0134','L-0135','L-0138','L-0142','L-0143','L-0148'],
 grammar_quiz=[('Write the second occurrence as an ordinal.','«kedua»'),
               ('Write 2.5 using «perpuluhan».','«dua perpuluhan lima»')],
 speaking_test='At the post office: say which visit it is, then ask and answer the weight, length and width of a parcel, with units.',
 speaking_key='Check «kali pertama» or «kedua», «Berapa berat / panjang / lebar …?», and a unit after every number.',
 teacher_notes=['Do not introduce chapter 8 classifiers.',
                'In speech use «panjang», «lebar», «tinggi» and «berat» directly. Teach the four measurement nouns as written labels only; do not ask learners to build new ones.',
                'All prices, weights and sizes are fictional.'],
 extra=dict(slug='writing-block',title='Writing block · Receipt and parcel label',
            goal='I can write a simple receipt and a parcel label with quantities and units.',
            model=['Receipt: «Mangga» «setengah kilo» RM5.00 · «Diskaun» «dua puluh peratus» -RM1.00 · «Jumlah» RM4.00.',
                   'Label: «Berat» 2 «kilo» · «Kepanjangan» 30 «sentimeter» · «Kelebaran» 20 «sentimeter» · «Ketinggian» 10 «sentimeter».'],
            task=['Write a fictional market receipt with a fraction of a kilo, a percentage discount, the total and the change.',
                  'Write a label for a fictional parcel: weight, length, width and height, with units. Read it aloud the spoken way.'],
            check=['☐ Every number has its unit.','☐ The percentage is labelled.',
                   '☐ Your partner can say the label the spoken way («panjang», «lebar», «tinggi»).'],
            answer='«Berat» 2 «kilo» · «Kepanjangan» 30 «sentimeter» · «Kelebaran» 20 «sentimeter» · «Ketinggian» 10 «sentimeter».'))
UNIT=unit_dict(CFG)
