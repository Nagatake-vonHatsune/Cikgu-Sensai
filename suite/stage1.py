"""Stage 1 (Malay A1) close: the stage review block and the A1 stage test.

The stage review (45 minutes, after unit 9) follows the review-block model of units 3A, 4B and 6: one integrated real-life
scenario that needs all nine chapters (a new colleague's first week in Kuala Lumpur), learned without notes, and a can-do
self-check covering every Stage 1 goal. The charter's spaced-return rule says every pattern comes back in the stage review,
so the model uses every Kata-Kata frame of chapters 1 to 9 (ms-c07-f03 in Sam's corrected form «jalan terus», not «jalan
lurus»); the key lists where each frame appears and a test checks it.

The A1 stage test is a summative test in the Irodori / JF Standard style: tasks with real outcomes, in four sections
(listening, reading, writing, speaking), 20 marks each, in two parallel versions (suite/stage1_test_a.py and
stage1_test_b.py), with the listening scripts, the administration sheet (timing, materials, scoring, the pass mark and
the item map) and the Stage 1 record for the catalogue (CEFR A1, the completion label).

Rules (as in every unit): Malaysian standard Malay, standard forms first; only ledger words placed in chapters 1 to 9 (the
build fails on anything else because ms-stage1 is a re-authored unit); no productive ber- or me-; no faith-specific
greeting. All names, places, prices, numbers and times are fictional. All Japanese is a draft awaiting native review.
"""

from .stage1_test_a import VERSION as VERSION_A
from .stage1_test_b import VERSION as VERSION_B

UNIT_ID = 'ms-stage1'
CHAPTERS = [f'ms-c{n:02}' for n in range(1, 10)]
FOCUS = {n: f'ms-c{n:02}-g01' for n in range(1, 10)}

# The Stage 1 can-do goals: the charter's nine chapter goals (section 4), each split into the checks a learner ticks.
CHARTER_GOALS = {
    1: 'Greet by time of day, use titles, ask after someone, take leave',
    2: 'Introduce yourself (name, origin, work, home, hobby) and ask the same of others',
    3: 'Ask and pay a price, check change, give age and phone number, say which one in a sequence',
    4: 'Tell the time and day, describe a routine, say what is done, not yet done or under way',
    5: 'Describe food, objects and feelings, and choose between items',
    6: 'Compare two options, say two things are equal, pick the best of three',
    7: 'Ask where something is, follow and give a route, name transport',
    8: 'Order and count things with the right classifier',
    9: 'Read signs and notices, say what was done and by whom',
}
CANDO = {
    1: [('I can greet someone by the time of day and put a title («Encik», «Puan», «Cik») before the name.',
         '時間帯に合ったあいさつをし、名前の前に敬称（«Encik»・«Puan»・«Cik»）を付けられる。'),
        ('I can ask how someone is and answer («Apa khabar?» «Khabar baik.»).',
         '相手の調子をたずね、答えられる（«Apa khabar?» «Khabar baik.»）。'),
        ('I can say sorry, ask politely for attention («Maaf, tumpang tanya.») and take leave.',
         'あやまり、ていねいに声をかけ（«Maaf, tumpang tanya.»）、別れのあいさつができる。')],
    2: [('I can say my name, where I am from, where I work or study, where I live and my hobby.',
         '名前、出身、仕事や勉強の場所、住んでいる所、趣味を言える。'),
        ('I can ask someone the same things («Siapa nama …?», «di mana», -kah).',
         '同じことを相手にたずねられる（«Siapa nama …?»・«di mana»・-kah）。')],
    3: [('I can ask a price, pay, and check my change.', '値段をたずね、払い、おつりを確かめられる。'),
        ('I can give my age and my phone number.', '年齢と電話番号を言える。'),
        ('I can say which one in a sequence («pertama», «kedua») and read a discount or a measurement on a sign.',
         '順番（«pertama»・«kedua»）を言い、掲示の割引や寸法を読める。')],
    4: [('I can tell the time and the day, and say when something starts and ends.',
         '時刻と曜日を言い、何かが始まる時刻と終わる時刻を言える。'),
        ('I can describe my routine and say how often I do things.', '日課と、どのくらいの頻度でするかを言える。'),
        ('I can say what is done, not yet done, under way or planned («sudah», «belum», «sedang», «akan»).',
         'もう済んだこと、まだのこと、している最中のこと、予定を言える（«sudah»・«belum»・«sedang»・«akan»）。')],
    5: [('I can describe food, things and how I feel.', '食べ物や物、自分の気持ちを説明できる。'),
        ('I can ask how something is and choose the one I want with «yang».',
         'どうかをたずね、«yang» を使ってほしいものを選べる。')],
    6: [('I can compare two options and say that two things are the same.', '二つを比べ、二つが同じだと言える。'),
        ('I can pick the best of three and say that something is too much.', '三つの中から一番を選び、「〜すぎる」と言える。')],
    7: [('I can ask where something is and say where it is.', '物や場所がどこにあるかをたずね、答えられる。'),
        ('I can follow and give a short route, and ask how far and how long.',
         '短い道順を聞いて分かり、説明でき、距離と時間をたずねられる。'),
        ('I can say how I get somewhere (by bus, by taxi, on foot).', '交通手段（バス、タクシー、徒歩）を言える。')],
    8: [('I can order and count things with the right counter, and say ‹se-› + counter for "one".',
         '正しい助数詞で注文し数えられ、「一つ」を ‹se-›＋助数詞で言える。'),
        ('I can ask how many and say a price per item.', 'いくつかをたずね、一つあたりの値段を言える。')],
    9: [('I can read common signs and notices («Dilarang …», «Sila …», opening hours).',
         'よくある掲示や案内（«Dilarang …»・«Sila …»・営業時間）を読める。'),
        ('I can say what was done and by whom («dibuat oleh …»), and what is done or not yet done.',
         '何がされたか、誰がしたか（«dibuat oleh …»）、もう済んだかまだかを言える。')],
}

# --- The stage review block -------------------------------------------------------------------------------------------

REVIEW_GOAL = ('I can use the language of chapters 1 to 9 together, without notes, to get through a real first week at work '
               'in Kuala Lumpur.')
REVIEW_GOAL_JA = '第1〜9章の表現をノートなしで組み合わせ、クアラルンプールでの仕事の最初の一週間を乗り切れる。'

WEEK = [
    'Monday: greetings, introductions and a staff form (chapters 1, 2 and 3). / 月曜日：あいさつ、自己紹介、職員用の書類（第1・2・3章）。',
    'Tuesday: lunch at a «gerai» — choosing, comparing, ordering with counters and paying (chapters 3, 5, 6 and 8). / 火曜日：«gerai»（屋台）で昼食。選ぶ、比べる、助数詞で注文する、払う（第3・5・6・8章）。',
    'Wednesday: the meeting day — times, routines, done and not yet done (chapter 4). / 水曜日：会議の日。時刻、日課、済んだこと・まだのこと（第4章）。',
    'Thursday: the way to the bank (chapter 7). / 木曜日：銀行への道（第7章）。',
    'Friday: the office «jamuan», the notices, and taking leave for the weekend (chapters 9 and 1). / 金曜日：事務所の «jamuan»（会食）、掲示、週末前のあいさつ（第9・1章）。',
]

RECALL = [
    'Ch 1: greet your partner for this time of day, with a title. / 今の時間帯のあいさつを、敬称を付けてしましょう。',
    'Ch 2: say where you live and what your hobby is. / 住んでいる所と趣味を言いましょう。',
    'Ch 3: say your phone number in Malay digits. / 電話番号をマレー語で言いましょう。',
    'Ch 4: say what time you start work and one thing you do every day. / 仕事を始める時刻と、毎日することを一つ言いましょう。',
    'Ch 5: describe the food you had yesterday. / きのう食べたものを説明しましょう。',
    'Ch 6: compare two drinks with «lebih … daripada». / 飲み物二つを «lebih … daripada» で比べましょう。',
    'Ch 7: say where the nearest station is from here. / ここからいちばん近い駅がどこにあるかを言いましょう。',
    'Ch 8: order two cups of tea and one plate of fried noodles. / お茶を2杯と焼きそばを1皿注文しましょう。',
    'Ch 9: read one sign in this building aloud, or make one with «Dilarang». / この建物の掲示を一つ読み上げるか、«Dilarang» で一つ作りましょう。',
]
RECALL_KEY = ('e.g. 1 «Selamat petang, Encik Tanaka.» 2 «Saya tinggal di Bangsar. Hobi saya masak.» '
              '3 «Nombor telefon saya kosong satu dua, tiga empat lima, enam tujuh lapan sembilan.» '
              '4 «Saya mula kerja pukul sembilan. Saya minum kopi setiap pagi.» 5 «Nasi goreng itu sedap, tetapi pedas.» '
              '6 «Teh tarik lebih manis daripada kopi.» 7 «Stesen di sebelah bank.» 8 «Dua cawan teh dan sepinggan mi goreng, tolong.» '
              '9 «Dilarang merokok.» / «Dilarang makan dan minum.»')

# The model week. Speakers: Kimura (the new colleague, fictional), Aini and Rahman (colleagues), Siti (the office manager),
# a stall holder. Each scene is (heading, [(speaker, Malay)]).
SCENES = [
    ('Monday · 8.45 a.m. · the office lobby (chapters 1 and 2) / 月曜日・午前8時45分・事務所のロビー（第1・2章）', [
        ('Aini', 'Selamat pagi, Encik Kimura. Selamat datang!'),
        ('Kimura', 'Selamat pagi, Puan Aini. Apa khabar?'),
        ('Aini', 'Khabar baik, terima kasih. Encik pula?'),
        ('Kimura', 'Khabar baik. Nama saya Kimura Kenji. Saya orang Jepun. Asal saya dari Osaka.'),
        ('Aini', 'Encik tinggal di mana?'),
        ('Kimura', 'Saya tinggal di Mont Kiara. Hobi saya golf. Saya juga suka masak.'),
        ('Kimura', 'Maaf, siapa nama puan?'),
        ('Siti', 'Nama saya Siti. Saya kerja di sini. Saya pengurus pejabat ini.'),
        ('Kimura', 'Saya belajar bahasa Melayu di Bangsar, setiap hari Sabtu.'),
        ('Kimura', 'Maaf, tumpang tanya. Di manakah tandas?'),
        ('Siti', 'Tandas di sebelah lif.')]),
    ('Monday · 10 a.m. · a staff form (chapter 3) / 月曜日・午前10時・職員用の書類（第3章）', [
        ('Siti', 'Berapa umur encik?'),
        ('Kimura', 'Umur saya tiga puluh lima tahun.'),
        ('Siti', 'Nombor telefon encik?'),
        ('Kimura', 'Nombor telefon saya kosong satu dua, tiga empat lima, enam tujuh lapan sembilan.'),
        ('Siti', 'Ini kali pertama encik di Malaysia?'),
        ('Kimura', 'Ya. Ini kali pertama saya di Malaysia.')]),
    ('Tuesday · 1 p.m. · lunch at a «gerai» (chapters 3, 5, 6 and 8) / 火曜日・午後1時・«gerai» で昼食（第3・5・6・8章）', [
        ('Kimura', 'Saya rasa lapar.'),
        ('Aini', 'Mari kita makan. Nasi lemak di gerai ini paling sedap.'),
        ('Kimura', 'Bagaimana rasa nasi lemak di sini?'),
        ('Aini', 'Sedap, tetapi pedas sedikit.'),
        ('Kimura', 'Saya mahu yang tidak pedas. Mi goreng lebih murah daripada nasi lemak?'),
        ('Aini', 'Ya, mi goreng lebih murah. Mi goreng di sini juga sedap.'),
        ('Stall holder', 'Makan sini atau bungkus?'),
        ('Kimura', 'Makan sini. Saya mahu sepinggan mi goreng dan secawan teh tarik.'),
        ('Aini', 'Saya mahu nasi lemak dan teh tarik, kurang manis, ais sedikit. Kami mahu dua keping pisang goreng juga.'),
        ('Aini', 'Tolong bungkus pisang goreng untuk Encik Rahman juga.'),
        ('Stall holder', 'Berapa keping, puan?'),
        ('Aini', 'Tiga keping.'),
        ('Stall holder', 'Baik. Pisang goreng lima puluh sen sekeping.'),
        ('Kimura', 'Mi goreng ini sedap. Tetapi teh tarik ini terlalu manis!'),
        ('Aini', 'Kopi kurang manis daripada teh tarik. Kopi di sini sama sedap dengan teh tarik.'),
        ('Kimura', 'Yang mana lebih murah, kopi atau teh tarik?'),
        ('Aini', 'Kopi. Kopi di gerai ini yang termurah.'),
        ('Kimura', 'Berapa harga semua?'),
        ('Stall holder', 'Harganya tujuh belas ringgit lima puluh sen.'),
        ('Kimura', 'Ini dua puluh ringgit.'),
        ('Stall holder', 'Baki dua ringgit lima puluh sen. Terima kasih!')]),
    ('Wednesday · 9.30 a.m. · the meeting day (chapter 4) / 水曜日・午前9時30分・会議の日（第4章）', [
        ('Kimura', 'Pukul berapa sekarang?'),
        ('Aini', 'Sekarang pukul sembilan setengah. Mesyuarat mula pukul sepuluh dan habis pukul sebelas.'),
        ('Kimura', 'Encik Rahman di mana?'),
        ('Aini', 'Dia masih di stesen. Dia lambat sedikit hari ini.'),
        ('Aini', 'Encik sudah sarapan?'),
        ('Kimura', 'Belum. Saya sedang tulis e-mel. Saya akan makan selepas mesyuarat.'),
        ('Aini', 'Encik pergi kerja naik apa?'),
        ('Kimura', 'Saya pergi kerja naik bas setiap hari.'),
        ('Aini', 'Encik pernah pergi ke Penang?'),
        ('Kimura', 'Belum pernah. Saya akan pergi ke Penang pada bulan depan.')]),
    ('Thursday · 2 p.m. · the way to the bank (chapter 7) / 木曜日・午後2時・銀行への道（第7章）', [
        ('Rahman', 'Encik mahu pergi ke mana?'),
        ('Kimura', 'Saya mahu pergi ke bank. Bank di mana?'),
        ('Rahman', 'Bank di sebelah pejabat pos. Jalan terus, kemudian belok kiri di lampu isyarat.'),
        ('Kimura', 'Berapa jauh bank dari sini?'),
        ('Rahman', 'Lebih kurang lima ratus meter.'),
        ('Kimura', 'Berapa lama ke bank?'),
        ('Rahman', 'Lebih kurang lima minit jalan kaki.'),
        ('Kimura', 'Stesen pula? Berapa lama ke stesen?'),
        ('Rahman', 'Stesen jauh. Lebih kurang sepuluh minit naik teksi.')]),
    ('Friday · 5 p.m. · the office «jamuan» (chapters 9 and 1) / 金曜日・午後5時・事務所の «jamuan»（第9・1章）', [
        ('Kimura', 'Wah, banyak makanan! Kek ini dibuat oleh siapa?'),
        ('Aini', 'Kek itu dibuat oleh isteri Encik Rahman.'),
        ('Kimura', 'Nasi lemak ini dibeli di mana?'),
        ('Aini', 'Dibeli di gerai dekat stesen.'),
        ('Rahman', 'Pinggan sudah dicuci?'),
        ('Aini', 'Belum.'),
        ('Kimura', 'Baik. Pinggan saya bawa ke dapur.'),
        ('Aini', 'Terima kasih. Pejabat ditutup pada pukul enam.'),
        ('Kimura', 'Papan tanda itu apa?'),
        ('Aini', 'Dilarang makan dan minum di bilik mesyuarat.'),
        ('Kimura', 'Baik. Saya minta diri dulu. Jumpa hari Isnin!'),
        ('Aini', 'Selamat jalan, Encik Kimura. Selamat hujung minggu!')]),
]

NOTICE = [
    'Fictional notice board in the lobby of the office building (all times and places are invented):',
    '«Pejabat dibuka pada pukul sembilan pagi dan ditutup pada pukul enam petang.»',
    '«Pada hari Sabtu dan Ahad, pejabat ditutup.»',
    '«Tandas di tingkat dua, di sebelah lif.»',
    '«Tempat letak kereta di tingkat bawah. Ketinggian dua meter.»',
    '«Kedai di tingkat bawah: diskaun sepuluh peratus pada hari Jumaat.»',
    '«Dilarang merokok.»',
    '«Jamuan pada hari Jumaat, pukul lima petang, di dapur.»',
]
NOTICE_Q = [
    ('When does the office open and close? / 事務所は何時に開き、何時に閉まりますか。', 'at nine in the morning; at six in the evening'),
    ('Can you go to the office on Saturday? / 土曜日に事務所へ行けますか。', 'No: it is closed on Saturday and Sunday («ditutup»)'),
    ('Where is the toilet? / トイレはどこですか。', 'on the second floor, next to the lift'),
    ('Your car is 2.5 metres tall. Can you use the car park? / 車の高さは2.5メートルです。駐車場を使えますか。',
     'No: the height is two metres («Ketinggian dua meter»)'),
    ('What does the shop offer, and on which day? / 店は何曜日に何をしていますか。', 'ten per cent off, on Friday'),
    ('When and where is the «jamuan»? / «jamuan» はいつ、どこですか。', 'Friday, five in the afternoon, in the kitchen'),
]
MESSAGE_TASK = ('Friday, 4.45 p.m. You are «Encik» Kimura and you are still at the bank. Write a WhatsApp message to «Puan» Aini in '
                'four to six sentences: greet her, say where you are, say what time you will arrive, say what you will bring '
                'with a counter, ask one question in the passive, and sign off. / 金曜日の午後4時45分。あなたは木村さんで、'
                'まだ銀行にいます。アイニさんに WhatsApp のメッセージを4〜6文で書きましょう：あいさつ、今いる場所、着く時刻、'
                '助数詞を使って持っていくもの、受け身の質問を一つ、結びのあいさつ。')
MESSAGE_MODEL = ('«Selamat petang, Puan Aini. Maaf, saya masih di bank. Saya akan sampai pukul lima suku. Saya bawa sekotak kuih '
                 'untuk jamuan. Kek sudah dipotong? Jumpa nanti!»')

ROLE_A = ['You are a new colleague in your first week (use your own name or «Encik» Kimura\'s). With your partner, go through '
          'the five days without the script, one day at a time: / あなたは最初の週の新しい同僚です（自分の名前か木村さんの名前で）。'
          '台本なしで、一日ずつ五日間を進めます：',
          'Monday: greet B, introduce yourself and ask one question about B; give your age and phone number for the form. / '
          '月曜日：Bにあいさつして自己紹介し、Bに一つ質問します。書類のために年齢と電話番号を言います。',
          'Tuesday: ask how a dish tastes, compare two dishes, order for two people with counters, and check the total. / '
          '火曜日：料理の味をたずね、二つを比べ、二人分を助数詞で注文し、合計を確かめます。',
          'Wednesday: ask the time and when the meeting starts and ends; say one thing you have not done yet. / '
          '水曜日：時刻と会議の開始・終了時刻をたずね、まだしていないことを一つ言います。',
          'Thursday: ask the way to the bank, how far it is and how long it takes; repeat the route. / '
          '木曜日：銀行への道、距離、かかる時間をたずね、道順を繰り返します。',
          'Friday: ask who made one dish and where one was bought, offer to help, read a sign, and take leave. / '
          '金曜日：料理を誰が作ったか、どこで買ったかをたずね、手伝いを申し出て、掲示を読み、別れのあいさつをします。']
ROLE_B = ['You are a colleague who has worked here for a year. Answer A in full sentences, using fictional details of your '
          'own (names, prices, times, places). Ask A at least one question each day. / あなたはここで一年働いている同僚です。'
          '架空の情報（名前、値段、時刻、場所）を使って、Aに完全な文で答えます。毎日少なくとも一つAに質問します。',
          'Tuesday: you are also the stall holder: ask «Makan sini atau bungkus?» and give the total. / '
          '火曜日：屋台の人の役もします。«Makan sini atau bungkus?» とたずね、合計を言います。',
          'Friday: you organised the «jamuan»: say who made, bought and brought the food. / '
          '金曜日：あなたは «jamuan» の幹事です。誰が作り、買い、持ってきたかを言います。']
CHANGE = ['On Wednesday, B says: «Maaf, mesyuarat mula pukul dua petang, bukan pukul sepuluh.» A asks where the meeting is '
          'and says what he or she will do in the morning instead (with «akan»). / 水曜日にBが «Maaf, mesyuarat mula pukul dua '
          'petang, bukan pukul sepuluh.» と言います。Aは会議の場所をたずね、代わりに午前中にすることを «akan» で言います。']
SUCCESS = ['☐ Every day has at least one question and one full answer, with no notes.',
           '☐ Titles come before names; the greeting fits the time of day (chapters 1 and 2).',
           '☐ Prices, the age and the phone number are said correctly (chapter 3).',
           '☐ «pukul» for clock times; «sudah», «belum», «akan» fit the time (chapter 4).',
           '☐ Adjectives follow the noun; one comparison with «lebih», «sama … dengan» or «paling» (chapters 5 and 6).',
           '☐ The route uses «jalan terus», «belok kiri / kanan di …» and a position word (chapter 7).',
           '☐ Every order has a number and a counter, or ‹se-› + counter (chapter 8).',
           '☐ One sentence with a «di-» verb and «oleh», and one sign read correctly (chapter 9).']

# Spaced return (charter rule 7): every Kata-Kata frame of chapters 1 to 9 and where it comes back in this block.
# Each entry: frame id -> a Malay string that must appear in the block (the test checks it).
FRAME_RETURNS = {
    'ms-c01-f01': 'Selamat pagi, Puan Aini', 'ms-c01-f02': 'Apa khabar?', 'ms-c01-f03': 'Khabar baik, terima kasih. Encik pula?',
    'ms-c01-f04': 'Maaf, tumpang tanya.', 'ms-c01-f05': 'Saya minta diri dulu. Jumpa hari Isnin!',
    'ms-c02-f01': 'Nama saya Kimura Kenji.', 'ms-c02-f02': 'Maaf, siapa nama puan?',
    'ms-c02-f03': 'Saya orang Jepun. Asal saya dari Osaka.', 'ms-c02-f04': 'Saya kerja di sini. Saya pengurus pejabat ini.',
    'ms-c02-f05': 'Saya belajar bahasa Melayu di Bangsar', 'ms-c02-f06': 'Saya tinggal di Mont Kiara.',
    'ms-c02-f07': 'Hobi saya golf. Saya juga suka masak.', 'ms-c02-f08': 'Di manakah tandas?',
    'ms-c03-f01': 'Berapa harga semua?', 'ms-c03-f02': 'Harganya tujuh belas ringgit lima puluh sen.',
    'ms-c03-f03': 'Umur saya tiga puluh lima tahun.', 'ms-c03-f04': 'Ini kali pertama saya di Malaysia.',
    'ms-c03-f05': 'diskaun sepuluh peratus', 'ms-c03-f06': 'Ketinggian dua meter.',
    'ms-c03-f07': 'Nombor telefon saya kosong satu dua',
    'ms-c04-f01': 'Sekarang pukul sembilan setengah.', 'ms-c04-f02': 'Saya pergi kerja naik bas setiap hari.',
    'ms-c04-f03': 'Dia masih di stesen.', 'ms-c04-f04': 'Saya akan makan selepas mesyuarat.',
    'ms-c04-f05': 'Encik sudah sarapan?', 'ms-c04-f06': 'Belum pernah.',
    'ms-c04-f07': 'Mesyuarat mula pukul sepuluh dan habis pukul sebelas.',
    'ms-c05-f01': 'Mi goreng ini sedap.', 'ms-c05-f02': 'Sedap, tetapi pedas sedikit.',
    'ms-c05-f03': 'Saya mahu yang tidak pedas.', 'ms-c05-f04': 'Saya rasa lapar.',
    'ms-c05-f05': 'teh tarik, kurang manis, ais sedikit',
    'ms-c06-f01': 'Mi goreng lebih murah daripada nasi lemak', 'ms-c06-f02': 'Kopi kurang manis daripada teh tarik.',
    'ms-c06-f03': 'Kopi di sini sama sedap dengan teh tarik.', 'ms-c06-f04': 'Nasi lemak di gerai ini paling sedap.',
    'ms-c06-f05': 'Yang mana lebih murah, kopi atau teh tarik?', 'ms-c06-f06': 'teh tarik ini terlalu manis!',
    'ms-c07-f01': 'Encik mahu pergi ke mana?', 'ms-c07-f02': 'Bank di sebelah pejabat pos.',
    'ms-c07-f03': 'Jalan terus, kemudian belok kiri di lampu isyarat.', 'ms-c07-f04': 'Berapa jauh bank dari sini?',
    'ms-c07-f05': 'Lebih kurang sepuluh minit naik teksi.',
    'ms-c08-f01': 'Kami mahu dua keping pisang goreng juga.', 'ms-c08-f02': 'sepinggan mi goreng dan secawan teh tarik',
    'ms-c08-f03': 'Berapa keping, puan?', 'ms-c08-f04': 'Pisang goreng lima puluh sen sekeping.',
    'ms-c08-f05': 'Tolong bungkus pisang goreng',
    'ms-c09-f01': 'Kek itu dibuat oleh isteri Encik Rahman.', 'ms-c09-f02': 'Dibeli di gerai dekat stesen.',
    'ms-c09-f03': 'Pinggan sudah dicuci?', 'ms-c09-f04': 'Pejabat ditutup pada pukul enam.',
    'ms-c09-f05': 'Dilarang makan dan minum di bilik mesyuarat.', 'ms-c09-f06': 'Pinggan saya bawa ke dapur.',
}


def _speaker(sp):
    return {'Stall holder': 'Stall holder (屋台の人)'}.get(sp, sp)


def review_component():
    model = []
    for heading, lines in SCENES:
        model.append('■ ' + heading)
        model.extend(f'{_speaker(sp)}: «{line}»' for sp, line in lines)
    checks = []
    for n in range(1, 10):
        checks.append(f'■ Chapter {n} · {CHARTER_GOALS[n]}')
        checks.extend(f'☐ {en} / {ja}' for en, ja in CANDO[n])
    returns = []
    for n in range(1, 10):
        ids = [k for k in FRAME_RETURNS if k.startswith(f'ms-c{n:02}-')]
        returns.append(f'Ch {n}: ' + ' · '.join(f'{k[-3:]} «{FRAME_RETURNS[k]}»' for k in ids))
    sections = [
        ('Goal and the week · 目標と一週間', [
            f'Can-do goal: {REVIEW_GOAL} / {REVIEW_GOAL_JA}',
            'Scene (fictional): «Encik» Kimura Kenji from Osaka starts work at an office in Kuala Lumpur. «Puan» Aini and «Encik» '
            'Rahman, his colleagues, and «Puan» Siti, the office manager, help him through his first week. All names, prices, '
            'numbers, times and places are invented. / 場面（架空）：大阪出身の木村健二さんがクアラルンプールの事務所で働き'
            '始めます。同僚のアイニさんとラーマンさん、事務所長のシティさんが最初の一週間を手伝います。名前、値段、番号、'
            '時刻、場所はすべて架空です。',
            *WEEK]),
        ('Recall without notes (5 min) · ノートなしで復習（5分）', RECALL),
        ('Model · Read in pairs (10 min) · モデル会話（ペアで読む、10分）', model),
        ('Your turn · Role cards (15 min) · ロールカード（15分）', [
            '■ Role card A · Aのカード', *ROLE_A,
            '■ Role card B · Bのカード', *ROLE_B,
            '■ Change of plan · 予定変更', *CHANGE,
            '■ Success criteria · できる基準', *SUCCESS]),
        ('Read and write (10 min) · 読む・書く（10分）', [
            *NOTICE, *[f'{i}. {q}' for i, (q, _) in enumerate(NOTICE_Q, 1)],
            MESSAGE_TASK, '________________________________________', '________________________________________',
            '________________________________________']),
        ('Can-do self-check · Stage 1 (5 min) · 第1段階の自己評価（5分）', [
            'Tick what you can do now without notes. Circle anything you want to practise again; your teacher will bring it '
            'back. / ノートなしで今できることにチェックしましょう。もう一度練習したいものには丸を付けましょう。先生があとで'
            '取り上げます。', *checks]),
    ]
    key = [
        'Timing: recall 5, model 10, role cards 15, read and write 10, self-check 5 (45 minutes). The block comes after '
        'unit 9 and before the A1 stage test; it is not marked.',
        'Recall answers: ' + RECALL_KEY,
        'Reading: ' + ' / '.join(f'{i}. {a}' for i, (_, a) in enumerate(NOTICE_Q, 1)),
        'Model message: ' + MESSAGE_MODEL,
        'Possible role-card exchange (Wednesday, after the change of plan): «Maaf, mesyuarat mula pukul dua petang, bukan pukul '
        'sepuluh.» — «Mesyuarat di mana?» — «Di bilik mesyuarat di tingkat tiga.» — «Baik. Pagi ini saya akan pergi ke bank.»',
        'Tuesday prices add up: «mi goreng» RM5.00, «nasi lemak» RM6.00, two «teh tarik» RM4.00, five pieces of «pisang goreng» RM2.50 '
        '= RM17.50; RM20.00 − RM17.50 = RM2.50 change. All prices are fictional.',
        'Spaced return (charter rule 7): every Kata-Kata frame of chapters 1 to 9 comes back in this block. Where each one is:',
        *returns,
        'ms-c07-f03 is said «Jalan terus, kemudian belok …» (Sam, 12 Nov 2026: the old wording of the frame is not used). «Ketinggian» and '
        '«diskaun … peratus» appear as written labels on the notice board, as in unit 3C.',
        'What to listen for: titles before names; «pukul» for the clock; the adjective after the noun; a counter with every '
        'number; «oleh» after a «di-» verb. Spoken forms are not needed; if a learner says «nak», «tak» or «dah», accept them '
        'and say the standard form back. Errors go on the board as practice for the A1 test preparation, not as red crosses.',
        'Use the self-check to choose what to revise before the A1 stage test. No marks or learner records are kept by Cikgu '
        'Sensai; the learner keeps the sheet.',
    ]
    return dict(slug='review', type='Task', title='Stage review · A new colleague\'s first week in Kuala Lumpur',
                block='Review', minutes=45, sections=sections, key=key,
                explain=('第1〜9章をまとめて復習する45分のブロックです。クアラルンプールで働き始めた同僚の一週間を、ノートなしで'
                         '会話し、読み、書き、最後に第1段階のすべての「できること」を自己評価します。日本語は未監修です。',
                         'A 45-minute block reviewing chapters 1 to 9 through one real week: a new colleague\'s first week in '
                         'Kuala Lumpur, spoken, read and written without notes, then a self-check of every Stage 1 can-do goal.'),
                sub_type='review', tests=[], patterns=list(FRAME_RETURNS), grammar=list(FOCUS.values()),
                goal=REVIEW_GOAL, skills=['speaking', 'listening', 'reading', 'writing'])


# --- The A1 stage test ------------------------------------------------------------------------------------------------

SECTION_MARKS = 20
TIMING = {'listening': 12, 'reading': 15, 'writing': 18, 'speaking': 7}
TEST_GOALS = {
    'listening': ('I can understand short announcements and everyday conversations about people, food, prices, times and '
                  'places, and note the facts I need.',
                  '人、食べ物、値段、時刻、場所についての短いお知らせや日常会話を聞いて分かり、必要な情報を書き取れる。'),
    'reading': ('I can read signs, a price board, a short message and a notice, and act on them.',
                '掲示、値段表、短いメッセージ、案内を読んで、その内容どおりに行動できる。'),
    'writing': ('I can fill in a simple form about myself and write a short message that arranges a meeting.',
                '自分についての簡単な書類に記入し、待ち合わせを決める短いメッセージを書ける。'),
    'speaking': ('I can introduce myself and handle short everyday exchanges: ordering, buying, asking the way and talking '
                 'at a party, including a change of plan.',
                 '自己紹介ができ、注文、買い物、道をたずねる、パーティーでの会話など、予定変更を含む短いやりとりができる。'),
}


def _marks(n):
    return f'[{n} mark{"s" if n != 1 else ""}]'


def _test_item(code, sub, it):
    return dict(sub_type=sub, prompt=f'{code}. {it["q"]} / {it["ja"]} {_marks(it["marks"])}',
                answer=it['a'], words=it['words'], grammar=[FOCUS[c] for c in sorted(set(it['ch']))])


def item_map(version):
    """[(item code, sub_type, marks, chapters)] for one version, in paper order."""
    v = version; out = []
    n = 0
    for task in v['listening']:
        for it in task['items']:
            n += 1; out.append((f'{v["label"]}-L{n}', 'listening', it['marks'], it['ch']))
    n = 0
    for part in v['reading']:
        for it in part['items']:
            n += 1; out.append((f'{v["label"]}-R{n}', 'reading', it['marks'], it['ch']))
    for n, part in enumerate(v['writing'], 1):
        it = part['items'][0]; out.append((f'{v["label"]}-W{n}', 'writing', it['marks'], it['ch']))
    sp = v['speaking']
    out.append((f'{v["label"]}-S1', 'speaking', sp['intro']['marks'], sp['intro']['ch']))
    for n, card in enumerate(sp['cards'], 1):
        out.append((f'{v["label"]}-S2.{n}', 'speaking', card['marks'], card['ch']))
    return out


def test_components(v):
    V = v['label']; low = V.lower(); out = []
    fiction = ('All names, shops, prices, times and places are fictional.', '名前、店、値段、時刻、場所はすべて架空です。')
    rules = {'listening': (f'Version {V}. Answer in English or Japanese unless a question asks for Malay. {fiction[0]} / '
                           f'バージョン{V}。マレー語で書くよう指示がある問題以外は、英語か日本語で答えます。{fiction[1]}'),
             'writing': f'Version {V}. Write in Malay. {fiction[0]} / バージョン{V}。マレー語で書きます。{fiction[1]}',
             'speaking': f'Version {V}. Speak in Malay. {fiction[0]} / バージョン{V}。マレー語で話します。{fiction[1]}'}
    rules['reading'] = rules['listening']

    def comp(slug, sub, title, minutes, sections, key, explain, tests, skills):
        goal, goal_ja = TEST_GOALS[sub]
        sections = [('Can-do and instructions · できることと指示', [f'Can-do: {goal} / {goal_ja}', rules[sub]] + sections[0][1])] + sections[1:]
        out.append(dict(slug=f'test-{low}-{slug}', type='Test', title=f'A1 stage test · Version {V} · {title}', block='Stage test',
                        minutes=minutes, sections=sections, key=key + [
                            f'Section total: {SECTION_MARKS} marks. The pass mark and the item map are on the administration sheet.'],
                        explain=explain, sub_type=sub, tests=tests, patterns=[], grammar=list(FOCUS.values()), goal=goal,
                        skills=skills))

    # Listening
    sections = [('Before you listen', [f'{TIMING["listening"]} minutes, {SECTION_MARKS} marks. The teacher reads each text twice. '
                                       'Read the questions first. / 12分、20点。先生が各文を2回読みます。先に質問を読みましょう。'])]
    tests, key, n = [], [], 0
    for t, task in enumerate(v['listening'], 1):
        lines = [task['context']]
        key.append(f'Task {t} · {task["title"]} · the teacher reads twice:')
        key.extend(f'{sp}: «{line}»' for sp, line in task['script'])
        for it in task['items']:
            n += 1; code = f'L{n}'
            item = _test_item(code, 'listening', it); tests.append(item)
            lines.append(item['prompt']); lines.append('________________________________________')
            key.append(f'{code}: {it["a"]}')
        sections.append((f'Task {t} · {task["title"]}', lines))
    comp('listening', 'listening', 'Listening', TIMING['listening'], sections, key,
         ('A1 段階テストの聞く問題です。先生が台本を2回読みます。台本は先生用キーにあります。日本語は未監修です。',
          'The listening paper of the A1 stage test. The teacher reads each script twice; the scripts are in the teacher key.'),
         tests, ['listening'])

    # Reading
    sections = [('Before you read', [f'{TIMING["reading"]} minutes, {SECTION_MARKS} marks. / 15分、20点。'])]
    tests, key, n = [], [], 0
    for t, part in enumerate(v['reading'], 1):
        lines = list(part['text'])
        for it in part['items']:
            n += 1; code = f'R{n}'
            item = _test_item(code, 'reading', it); tests.append(item)
            lines.append(item['prompt']); lines.append('________________________________________')
            key.append(f'{code}: {it["a"]}')
        sections.append((f'Part {t} · {part["title"]}', lines))
    comp('reading', 'reading', 'Reading', TIMING['reading'], sections, key,
         ('A1 段階テストの読む問題です：掲示、値段表、メッセージ、案内。日本語は未監修です。',
          'The reading paper of the A1 stage test: signs, a price board, a message and a notice.'), tests, ['reading'])

    # Writing
    sections = [('Before you write', [f'{TIMING["writing"]} minutes, {SECTION_MARKS} marks. / 18分、20点。'])]
    tests, key = [], []
    for t, part in enumerate(v['writing'], 1):
        code = f'W{t}'
        it = part['items'][0]
        item = _test_item(code, 'writing', it); tests.append(item)
        lines = [part['intro'], item['prompt']]
        lines += [f'{field}: ______________________' for field in part['form'][1:]] if part['form'] else [
            '________________________________________'] * 5
        if part['form']:
            lines.insert(1, part['form'][0])
        key.append(f'{code}: {it["a"]}')
        sections.append((f'Part {t} · {part["title"]}', lines))
    comp('writing', 'writing', 'Writing', TIMING['writing'], sections, key,
         ('A1 段階テストの書く問題です：申込書とメッセージ。採点基準は先生用キーにあります。日本語は未監修です。',
          'The writing paper of the A1 stage test: a form and a message. The marking rubric is in the teacher key.'),
         tests, ['writing'])

    # Speaking
    sp = v['speaking']
    tests, key = [], []
    intro = _test_item('S1', 'speaking', sp['intro']); tests.append(intro)
    sections = [('Before you speak', [
        f'About {TIMING["speaking"]} minutes for each learner, {SECTION_MARKS} marks: the self-introduction (8) and two role-play '
        'cards (6 each). The examiner chooses card 1 or 2, and card 3 or 4. / 一人約7分、20点：自己紹介（8点）と'
        'ロールカード二枚（各6点）。試験官がカード1か2、カード3か4を選びます。']),
        ('Part 1 · Self-introduction · 自己紹介', [intro['prompt']])]
    key.append('S1 examiner: ' + ' '.join(sp['intro']['examiner']))
    key.append('S1 rubric (8): ' + sp['intro']['a'])
    cards = []
    for c, card in enumerate(sp['cards'], 1):
        code = f'S2.{c}'
        it = dict(q=f'{card["title"]}: ' + ' '.join(f'({i}) {x}' for i, x in enumerate(card['tasks'], 1)),
                  ja=f'{card["ja_title"]}：' + ''.join(f'（{i}）{x}' for i, x in enumerate(card['tasks_ja'], 1)),
                  a=card['a'], marks=card['marks'], ch=card['ch'], words=card['words'])
        item = _test_item(code, 'speaking', it); tests.append(item)
        cards.append('■ ' + card['title'] + ' · ' + card['ja_title'])
        cards.extend(f'☐ {en} / {ja}' for en, ja in zip(card['tasks'], card['tasks_ja']))
        key.append(f'{code} examiner: ' + ' '.join(card['examiner']))
        key.append(f'{code} rubric (6): ' + card['a'])
    sections.append(('Part 2 · Role-play cards · ロールカード', [
        'Read your card, then talk with the examiner without a script. The examiner will change one thing. / カードを読み、'
        '台本なしで試験官と話します。試験官が途中で一つ変更します。', *cards]))
    comp('speaking', 'speaking', 'Speaking', TIMING['speaking'], sections, key,
         ('A1 段階テストの話す問題です：自己紹介とロールカード。試験官の台詞と採点基準は先生用キーにあります。日本語は未監修です。',
          'The speaking test of the A1 stage test: a self-introduction and role-play cards. The examiner\'s lines and the '
          'rubric are in the teacher key.'), tests, ['speaking'])
    return out


PASS_TOTAL, PASS_SECTION, TOTAL = 48, 10, 4 * SECTION_MARKS
COMPLETION_LABEL = 'Malay A1 · Stage 1 complete'


def _chapters(ch):
    return ', '.join(str(c) for c in sorted(set(ch)))


def item_ids(version):
    """[(catalogue test-item id, item code, chapters)] in component order, matching suite.build_suite's numbering."""
    low = version['label'].lower(); counters = {}; out = []
    for code, sub, _, ch in item_map(version):
        counters[sub] = counters.get(sub, 0) + 1
        out.append((f'ms-stage1-test-{low}-{sub}-{counters[sub]:02}', code, sorted(set(ch))))
    return out


def scripts_component():
    sections = []
    for v in VERSIONS:
        lines = []
        for t, task in enumerate(v['listening'], 1):
            lines.append(f'■ Version {v["label"]} · Task {t} · {task["title"]}')
            lines.append(task['context'])
            lines.extend(f'{sp}: «{line}»' for sp, line in task['script'])
        sections.append((f'Version {v["label"]} · バージョン{v["label"]}', lines))
    return dict(slug='test-scripts', type='Teaching plan', title='A1 stage test · Listening scripts (teacher)', block='Stage test',
                minutes=None, sections=sections,
                key=['Read each text twice at a natural speed, with a short pause between the two readings. Say the speaker\'s '
                     'name before each line. Do not hand out this sheet. The answers are in the keys of the two listening papers.',
                     'All names, shops, prices, times and places are fictional.'],
                explain=('A1 段階テストの聞く問題の台本（先生用、バージョンAとB）です。学習者には配りません。日本語は未監修です。',
                         'The teacher-read scripts for the A1 stage test listening papers, versions A and B. Not for learners.'),
                sub_type='listening scripts', tests=[], patterns=[], grammar=list(FOCUS.values()),
                goal=TEST_GOALS['listening'][0], skills=['listening'])


def admin_component():
    maps = []
    for v in VERSIONS:
        lines = [f'■ Version {v["label"]}: item, marks, chapters whose can-do goals it tests']
        lines += [f'{code} · {m} · ch {_chapters(ch)}' for code, _, m, ch in item_map(v)]
        lines.append(f'■ Version {v["label"]}: chapter, its can-do goal, the items that test it')
        for n in range(1, 10):
            codes = [code for code, _, _, ch in item_map(v) if n in ch]
            lines.append(f'Ch {n} · {CHARTER_GOALS[n]}: ' + ', '.join(codes))
        maps.append((f'Item map · Version {v["label"]} · 問題と章の対応', lines))
    sections = [
        ('What the test is · テストについて', [
            'The A1 stage test closes Stage 1 (chapters 1 to 9). It checks the charter\'s Stage 1 can-do goals at CEFR A1 '
            'with tasks that have a real outcome, in the Irodori and JF Standard way: understand an announcement, act on a '
            'sign, fill in a form, order and pay, ask the way. / A1 段階テストは第1段階（第1〜9章）のまとめのテストです。'
            '憲章の「できること」を CEFR A1 で、実際の目的のある課題で確かめます（いろどり・JF スタンダードの方法）。',
            'Two parallel versions, A and B, with the same sections, tasks, marks and chapter spread. Use A for the main sitting; '
            'use B for a second group, a re-sit or the next course. Do not give both versions to one learner in the same week. / '
            '同じ構成のバージョンAとBがあります。本試験はA、別のグループ・再試験・次の講座はBを使います。',
            'The test is summative but kept low-stakes in spirit (charter rule 9): the result tells the learner which can-do goals '
            'to revisit. A pass means the learner has met the Stage 1 goals at A1 as this course defines them; it is not an '
            'official CEFR certificate. / 合格は、この講座の定める A1 の第1段階の目標を達成したという意味で、公式の CEFR 証明ではありません。']),
        ('Timing · 時間', [
            f'Written paper, one 45-minute block: listening {TIMING["listening"]} minutes, reading {TIMING["reading"]}, writing '
            f'{TIMING["writing"]}. Collect each paper before the next one.',
            f'Speaking: about {TIMING["speaking"]} minutes for each learner, one at a time or in pairs, in a second block (six '
            'learners fill about 45 minutes). The others can do the stage review self-check or Kata-Kata review meanwhile.',
            'Do the stage review block before the test, in an earlier class.']),
        ('Materials · 準備するもの', [
            'For each learner: the listening, reading and writing papers of the version you use (without the teacher keys).',
            'For the speaking test: the speaking sheet, with the four role-play cards cut apart; the teacher key with the '
            'examiner\'s lines and the rubric.',
            'For the teacher: the listening scripts sheet, the four teacher keys, this sheet and one result sheet per learner. '
            'No audio is needed: the teacher reads the scripts.']),
        ('Running the test · 実施の手順', [
            'Listening: read the instructions, give one minute to read the questions, then read each text twice at a natural '
            'speed. Learners answer in English or Japanese, or in Malay where the question asks for it.',
            'Reading and writing: learners work alone without notes or dictionaries. Answer questions about the instructions only.',
            'Speaking: greet the learner first («Selamat pagi. Apa khabar?»; not marked). Part 1, the self-introduction, then the two follow-up questions. '
            'Part 2: choose card 1 or 2, then card 3 or 4; give 30 seconds to read the card; play your part from the key and '
            'bring in the change of plan halfway. Mark with the rubric straight after each part.']),
        ('Scoring and pass mark · 採点と合格基準', [
            f'Four sections of {SECTION_MARKS} marks: {TOTAL} in all. Listening and reading: one mark for each fact in the key. '
            'Writing and speaking: the rubric in each key (content, language, accuracy or interaction).',
            f'Pass: {PASS_TOTAL} or more out of {TOTAL} (60 per cent), and at least {PASS_SECTION} out of {SECTION_MARKS} in every '
            'section. / 合格：80点中48点以上（60％）、かつ各セクション20点中10点以上。',
            f'A pass is recorded as "{COMPLETION_LABEL}" (CEFR A1). "Not yet": go back to the chapters of the items that were '
            'missed (item map below), then sit the other version.',
            'Accept any natural answer with the same meaning. In listening and reading, a spelling slip that does not change the '
            'meaning loses no mark. No half marks.']),
        *maps,
        ('After the test · テストのあと', [
            'Go over the answers in the next class. Errors return as practice, not as red crosses (charter rule 9).',
            'Fill in a result sheet for each learner on paper. Cikgu Sensai keeps no learner records.',
            '■ Result sheet', 'Name: ______________________   Version: A / B   Date: __________',
            f'Listening __ / {SECTION_MARKS}   Reading __ / {SECTION_MARKS}   Writing __ / {SECTION_MARKS}   Speaking __ / {SECTION_MARKS}',
            f'Total __ / {TOTAL}   ☐ {COMPLETION_LABEL} (pass)   ☐ Not yet',
            'Chapters to revisit: ______________________']),
    ]
    return dict(slug='test-admin', type='Teaching plan', title='A1 stage test · Administration sheet (teacher)', block='Stage test',
                minutes=None, sections=sections,
                key=['The pass mark (60 per cent overall, half of each section) is a proposal for Sam; it is not taken from a JF or '
                     'CEFR document. The item maps are generated from the item data, so they always match the papers.',
                     'Answer keys: on each paper. Listening scripts: on the scripts sheet and in the listening keys.'],
                explain=('A1 段階テストの実施要領（先生用）：時間、準備、手順、採点と合格基準、問題と章の対応表、結果記入表。日本語は未監修です。',
                         'How to run the A1 stage test: timing, materials, procedure, scoring and the pass mark, the item maps and a '
                         'result sheet.'),
                sub_type='administration', tests=[], patterns=[], grammar=list(FOCUS.values()),
                goal='I can run and mark the A1 stage test and tell each learner which can-do goals to revisit.', skills=[])


def stage_record(components):
    """The Stage 1 record for the catalogue. It carries the CEFR label that the charter (section 10, phase 3) wants shown in
    Hanashishou's Evaluator: a learner who passes the A1 stage test has completed Stage 1 at A1. The record is a definition
    only; Cikgu Sensai stores no learner results."""
    ids = {c['id'] for c in components}
    return dict(
        id='ms-stage1', language='Malay', title='Stage 1', cefr='A1', chapter_ids=CHAPTERS,
        review_block_id='ms-stage1-review' if 'ms-stage1-review' in ids else None,
        stage_test=dict(
            versions={v['label']: [f'ms-stage1-test-{v["label"].lower()}-{s}' for s in ('listening', 'reading', 'writing', 'speaking')
                                   if f'ms-stage1-test-{v["label"].lower()}-{s}' in ids] for v in VERSIONS},
            scripts_id='ms-stage1-test-scripts' if 'ms-stage1-test-scripts' in ids else None,
            administration_id='ms-stage1-test-admin' if 'ms-stage1-test-admin' in ids else None,
            section_marks=SECTION_MARKS, total_marks=TOTAL, timing_minutes=TIMING,
            pass_rule=dict(total_min=PASS_TOTAL, section_min=PASS_SECTION, status='proposal for Sam'),
            item_chapters={iid: [f'ms-c{c:02}' for c in ch] for v in VERSIONS for iid, _, ch in item_ids(v)}),
        completion=dict(flag='stage1_complete', label=COMPLETION_LABEL, cefr='A1',
                        rule='pass the A1 stage test (either version) by the pass rule',
                        evaluator_note='Hanashishou shows this CEFR label for a learner who has completed Stage 1; its band 1 '
                                       '(Foundation) starts at A2 (charter section 7). Nothing is built in Hanashishou here.'),
        learner_records='none: the result sheet is paper; Cikgu Sensai stores no learner data', review_status='draft')


VERSIONS = [VERSION_A, VERSION_B]


def components(ledger):
    return [review_component(), *[c for v in VERSIONS for c in test_components(v)], scripts_component(), admin_component()]



UNIT = dict(unit_id=UNIT_ID, label=None, stage='stage1', chapter_id='ms-c09', check_unit=UNIT_ID, id_prefix=UNIT_ID,
            title_prefix='Stage 1', header='Stage 1 review and A1 test (ms-stage1)', menu_title='Stage 1 · Review and A1 test',
            genre='Social life', goal=REVIEW_GOAL, blocks={'Review': REVIEW_GOAL},
            prerequisites=CHAPTERS, prerequisite_units=['ms-c09'], prereq_grammar=list(FOCUS.values()),
            word_scope=None, components=components)
