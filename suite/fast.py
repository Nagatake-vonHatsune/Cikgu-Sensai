"""Fast-course summary packs for chapters 1 and 2 (charter section 6: one
45-minute session per chapter, then self-study in Kata-Kata). Same chapter
content and ledger limits as the full-course units. Japanese is a draft.
"""
from . import core, turns

C1_WORDS = ['L-0002', 'L-0003', 'L-0004', 'L-0005', 'L-0006', 'L-0028', 'L-0012', 'L-0014', 'L-0015', 'L-0983',
            'L-0016', 'L-0017', 'L-0018', 'L-0019', 'L-0031', 'L-0032', 'L-0033', 'L-0022', 'L-0672', 'L-0025']
C2_WORDS = ['L-0048', 'L-0049', 'L-0052', 'L-0058', 'L-0059', 'L-0062', 'L-0063', 'L-0038', 'L-0042', 'L-0044',
            'L-0045', 'L-0985', 'L-0986', 'L-0065', 'L-0071', 'L-0073', 'L-0079', 'L-0084', 'L-0988', 'L-0783']


def chapter1(ledger):
    model = [('Aini', '«Selamat pagi! Selamat datang.»'), ('Tanaka', '«Selamat pagi, Puan. Saya Tanaka.»'),
             ('Aini', '«Oh, Encik Tanaka! Apa khabar?»'), ('Tanaka', '«Khabar baik, terima kasih. Puan pula?»'),
             ('Aini', '«Saya pun baik. Selamat berkenalan.»'), ('Tanaka', '«Selamat berkenalan, Puan Aini.»'),
             (None, '6 pm · 午後6時'),
             ('Tanaka', '«Maaf, Puan Aini. Saya minta diri dulu.»'), ('Aini', '«Ya, ya. Jumpa esok, Encik Tanaka.»'),
             ('Tanaka', '«Jumpa esok. Terima kasih, Puan.»'), ('Aini', '«Sama-sama. Selamat jalan!»')]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack', block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06'],
        patterns=['ms-c01-f01', 'ms-c01-f02', 'ms-c01-f03', 'ms-c01-f04', 'ms-c01-f05'],
        goal='Greet by time of day, use titles, ask after someone and take leave.',
        explain=('速習コース用：第1章を45分1回で学び、残りは Kata-Kata で自習します。目標、基本の20語、文型、会話、タスク、チェック、自習ガイドがあります。',
                 'Fast course: chapter 1 in one 45-minute session, then self-study in Kata-Kata. Goals, 20 core words, patterns, a conversation, a task, a self-check and a self-study guide.'),
        sections=[
            ('Can-do goals · できること', [
                'I can greet people at the right time of day and use the right title. / 時間帯に合ったあいさつと敬称が使える。',
                'I can ask how someone is, answer, and return the question. / 様子をたずね、答え、質問を返せる。',
                'I can thank, apologise and politely ask for attention. / お礼・おわび・呼びかけができる。',
                'I can take my leave politely. / 丁寧に別れのあいさつができる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C1_WORDS) + ['Spoken form: «tak» is the spoken form of «tidak» (no, not).'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Selamat» ___ , (title) ___ .  e.g. «Selamat pagi, Puan Aini.» / «Selamat malam, Pak cik.»',
                '2 · «Apa khabar,» (title)?  e.g. «Apa khabar, Encik Tanaka?» / «Apa khabar, Cik Mei Ling?»',
                '3 · «Khabar baik, terima kasih.» (title) «pula»?  e.g. «Khabar baik, terima kasih. Puan pula?» / «Saya pun baik.»',
                '4 · «Maaf, tumpang tanya.»  e.g. «Maaf, tumpang tanya. Encik Tanaka?» / «Ya, saya Tanaka.»',
                '5 · «Saya minta diri dulu. Jumpa» ___ !  e.g. «Saya minta diri dulu. Jumpa esok!» / «Jumpa lagi!»',
                'Remember: the title comes before the name; «pun» comes after the word; «Selamat jalan» is said to the person leaving.',
                '敬称は名前の前、«pun» は語のあと、«Selamat jalan» は出かける人に言います。'], 'model'),
            ('Model conversation · 会話', turns(model), 'model'),
            ('Task · タスク', [
                'A: It is your first morning at a new office. Greet the receptionist, say your name, ask how they are.',
                'B: Welcome A, answer and return the question, say "nice to meet you".',
                'Change of plan: it is 6 pm and A leaves first. Then play it again with an older B («Pak cik» / «Mak cik»).',
                'A：新しい会社の初日の朝。受付にあいさつし、名前を言い、様子をたずねます。B：歓迎し、答えて質問を返し、「よろしく」と言います。',
                '変更：午後6時、Aが先に帰ります。次に、Bを年上の人にしてもう一度。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. It is 9 pm. Greet «Puan» Aini. ____________________',
                '☐ 2. Return the question: «Khabar baik, terima kasih. Encik ___ ?»',
                '☐ 3. Someone says «Terima kasih.» You answer: ____________',
                '☐ 4. Take your leave until tomorrow: ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before the session: Kata-Kata Sedia Kelas c01 (23 cards, frames ms-c01-f01 and f02).',
                'After the session: the whole Kata-Kata chapter 1 deck with daily spaced review; frames ms-c01-f01 to f05 in the frame drill and Susun Ayat; '
                'the chapter 1 scenario "First day at the office".',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Chapter 1 has no Dunia scene yet. Hanashishou starts at A2.',
                'Optional take-home sheets from unit 1: vocabulary focus, drills 1 to 6, the listening focus (with a partner reading the script).',
                '授業前：Sedia Kelas c01。授業後：第1章のカード全部を毎日復習し、文型を Susun Ayat で練習。自習の目安は約9〜10時間。'], 'opener')],
        key=['Self-check: 1 «Selamat malam, Puan Aini.» 2 «pula» 3 «Sama-sama.» 4 «Saya minta diri dulu. Jumpa esok!»',
             'Session plan (45 min): 0–5 recall greetings learners know; 5–15 core words (times and titles); 15–25 patterns 1 to 5; '
             '25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 1. All Japanese is a draft awaiting native review.'])]


def chapter2(ledger):
    model = [('Farah', '«Selamat pagi. Siapa nama encik?»'), ('Tanaka', '«Nama saya Tanaka. Cik pula?»'),
             ('Farah', '«Nama saya Farah. Encik orang Jepun?»'), ('Tanaka', '«Ya, saya orang Jepun. Kampung saya di Osaka.»'),
             ('Farah', '«Encik kerja di mana?»'), ('Tanaka', '«Saya kerja di syarikat Sakura. Saya jurutera.»'),
             ('Farah', '«Encik tinggal di mana?»'), ('Tanaka', '«Di Mont Kiara, dengan keluarga saya. Cik pula?»'),
             ('Farah', '«Saya tinggal di Bangsar. Kampung saya di Ipoh. Itu Kumar, kawan saya.»'),
             ('Tanaka', '«Selamat berkenalan, Encik Kumar. Encik suka masakan Malaysia?»'),
             ('Kumar', '«Suka! Encik pula?»'), ('Tanaka', '«Saya pun suka. Jom, kita jumpa lagi nanti!»')]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack', block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c02-g02', 'ms-c02-g03', 'ms-c02-g04', 'ms-c02-g05', 'ms-c02-g06', 'ms-c02-g08', 'ms-c02-g09', 'ms-c02-g10', 'ms-c02-g12'],
        patterns=['ms-c02-f01', 'ms-c02-f02', 'ms-c02-f03', 'ms-c02-f04', 'ms-c02-f06', 'ms-c02-f07', 'ms-c02-f08'],
        goal='Introduce yourself (name, origin, work, home, likes) and ask the same of others.',
        explain=('速習コース用：第2章（ユニット2Aと2B）を45分1回で学び、残りは Kata-Kata で自習します。',
                 'Fast course: chapter 2 (units 2A and 2B) in one 45-minute session, then self-study in Kata-Kata.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say my name, nationality and hometown and ask other people theirs. / 名前・国籍・出身地を言い、たずねられる。',
                'I can say where I work or study, where I live and who with. / 仕事・勉強の場所、住んでいる所、だれと住んでいるかが言える。',
                'I can say what I like and ask formal questions with -kah, «adakah» and «bolehkah». / 好きなことを言い、-kah・«adakah»・«bolehkah» で丁寧にたずねられる。',
                'I can choose the right word for "you". / 「あなた」にあたる正しい語を選べる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C2_WORDS), 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Nama saya» ___ .  e.g. «Nama saya Tanaka.» / «Ini kawan saya. Namanya Ali.»',
                '2 · «Siapa nama» (title)?  e.g. «Siapa nama encik?» / «Itu siapa?»',
                '3 · «Saya orang» ___ . «Asal saya dari» ___ .  e.g. «Saya orang Jepun. Asal saya dari Osaka.» / «Saya boleh cakap bahasa Melayu sedikit.»',
                '4 · «Saya kerja di» ___ .  e.g. «Saya kerja di syarikat Jepun. Saya jurutera.» / «Saya belajar di Universiti Malaya.»',
                '5 · «Saya tinggal di» ___ .  e.g. «Saya tinggal di Mont Kiara.» / «Saya tinggal dengan keluarga saya.»',
                '6 · «Saya suka» ___ .  e.g. «Saya suka masakan Malaysia.» / «Apa hobi encik?» — «Hobi saya karaoke.» (hobby words: pick your own)',
                '7 · «Di manakah» / «Adakah» / «Bolehkah» ___ ?  e.g. «Di manakah pejabat encik?» / «Bolehkah saya tanya?»',
                'Remember: two nouns make a sentence (no "is"); the owner comes after the thing («nama saya»); use a title, not «awak», with seniors.',
                '名詞を並べるだけで文になります。持ち主はもののあと（«nama saya»）。目上の人には «awak» ではなく敬称を使います。'], 'model'),
            ('Model conversation · 会話', turns(model), 'model'),
            ('Task · タスク', [
                'A and B meet at a welcome event. Ask and answer: name, country, hometown, work, home, likes. Find two things in common.',
                'Change of plan: B is now the manager of a language school. B asks the same questions formally, with -kah, «Adakah» and «Bolehkah».',
                '歓迎会でAとBが会います。名前・国・出身地・仕事・家・好きなことをたずね合い、共通点を二つ見つけます。変更：Bは語学学校の責任者になり、丁寧な質問で同じことをたずねます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Ask a manager his name politely: ____________________',
                '☐ 2. Say you are Japanese and your hometown is Kyoto: ____________________',
                '☐ 3. Formal: «___ encik tinggal di Bangsar?» — «Ya.»',
                '☐ 4. "We", including the listener: ________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before the session: Kata-Kata Sedia Kelas c02 (27 cards, frames ms-c02-f01 and f02).',
                'After the session: the whole Kata-Kata chapter 2 deck with daily spaced review; frames ms-c02-f01 to f08 in the frame drill and Susun Ayat; '
                'the Dunia scenes "Sembang di pantri" and "Pagi di pejabat".',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                'Optional take-home sheets from units 2A and 2B: vocabulary focus, drills 1 to 6, the writing block (self-introduction form).',
                '授業前：Sedia Kelas c02。授業後：第2章のカード全部を毎日復習し、Dunia の二つの場面を練習。自習の目安は約9〜10時間。'], 'opener')],
        key=['Self-check: 1 «Siapa nama encik?» 2 «Saya orang Jepun. Kampung saya di Kyoto.» 3 «Adakah» 4 «kita»',
             'Session plan (45 min): 0–5 recall chapter 1 greetings; 5–15 core words; 15–25 patterns 1 to 7; 25–35 model conversation; '
             '35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as units 2A and 2B. All Japanese is a draft awaiting native review.'])]


PACKS = [
    dict(chapter_id='ms-c01', check_unit='ms-c01-fast', id_prefix='ms-c01-fast', title_prefix='Chapter 1',
         header='Chapter 1 fast course (ms-c01)', menu_title='Chapter 1 · Greetings', genre='Social life', course_path='fast',
         prerequisites=[], prerequisite_units=[], word_scope=C1_WORDS, components=chapter1),
    dict(chapter_id='ms-c02', check_unit='ms-c02-fast', id_prefix='ms-c02-fast', title_prefix='Chapter 2',
         header='Chapter 2 fast course (ms-c02)', menu_title='Chapter 2 · Pronouns and self-introduction', genre='Social life',
         course_path='fast', prerequisites=['ms-c01'], prerequisite_units=[], prereq_grammar=['ms-c01-g02', 'ms-c01-g04'],
         word_scope=C2_WORDS, components=chapter2),
]


# Step 5a: chapter 3 fast course (single 45-minute class).
# Only a digest of the same chapter 3 words and patterns, not an extra word set.
C3_WORDS = ['L-0099', 'L-0100', 'L-0101', 'L-0109', 'L-0116', 'L-0117',
            'L-0118', 'L-0119', 'L-0120', 'L-0123', 'L-0125', 'L-0127',
            'L-0131', 'L-0132', 'L-0134', 'L-0135', 'L-0138', 'L-0143',
            'L-0148', 'L-0154']


def chapter3(ledger):
    dialogue = [
        ('Aini', '«Selamat pagi, encik. Ini kali pertama encik di pasar ini?»'),
        ('Tanaka', '«Bukan, kali kedua. Berapa harga mangga ini?»'),
        ('Aini', '«Satu mangga lapan ringgit lima puluh sen.»'),
        ('Tanaka', '«Pisang pula?»'),
        ('Aini', '«Pisang empat ringgit. Pagi ini ada diskaun dua puluh peratus.»'),
        ('Tanaka', '«Saya beli satu mangga sahaja. Ini sepuluh ringgit.»'),
        ('Aini', '«Terima kasih. Baki satu ringgit lima puluh sen.»'),
        ('Tanaka', '«Satu ringgit lima puluh sen. Betul.»'),
        ('Aini', '«Jumpa lagi, encik!»'),
        ('Tanaka', '«Terima kasih. Jumpa lagi!»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c03-g02','ms-c03-g03','ms-c03-g04','ms-c03-g05','ms-c03-g06','ms-c03-g07'],
        patterns=['ms-c03-f01','ms-c03-f02','ms-c03-f03','ms-c03-f04','ms-c03-f05','ms-c03-f06','ms-c03-f07'],
        goal='Use numbers for ages, phone digits, fictional prices, ordinal positions and basic fractions or measures.',
        explain=('第3章速習：45分で主要20語と文型を練習します。価格と電話番号は架空のものです。日本語は未監修です。',
                 'Chapter 3 in one 45-minute lesson: 20 priority words, key patterns, a conversation, a practical task and self-study. All numerical practice prices and phone numbers are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can ask and give an age and a fictional telephone number.',
                'I can ask and pay a fictional price in ringgit and sen, and verify change.',
                'I can distinguish first, second, and third, and recognise fractions and percentages.',
                'I can recognise basic measurements in metres or kilograms.'], 'opener'),
            ('Core words · 基本の20語', core(ledger,C3_WORDS), 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Berapa harga» ___ ?  e.g. «Berapa harga epal?» / «Berapa harga pisang?»',
                '2 · «Harganya» ___ «ringgit» ___ «sen».  e.g. «Harganya dua ringgit lima puluh sen.» / «Harganya lapan ringgit.»',
                '3 · «Berapa umur» ___ ?  e.g. «Berapa umur encik?» / «Berapa umur puan?»',
                '4 · «Nombor telefon saya» ___ .  e.g. «Nombor telefon saya kosong satu dua.» / «Nombor telefon saya kosong satu tiga.»',
                '5 · «Ini kali» ___ .  e.g. «Ini kali pertama saya di Malaysia.» / «Ini kali kedua saya di Malaysia.»',
                '6 · «Diskaun» ___ «peratus».  e.g. «Diskaun sepuluh peratus.» / «Diskaun dua puluh peratus.»',
                '7 · «Berapa» [«panjang» / «berat»] ___ ?  e.g. «Berapa panjang bungkusan ini?» — «Tiga puluh sentimeter.» / «Berapa berat bungkusan ini?» — «Dua kilo.»',
                'Fraction reminder: «setengah» (half), «suku» (quarter), «tiga suku» (three quarters).',
                'Price amounts, ordinal forms, fractions and measurement nouns are part of the full chapter.'], 'model'),
            ('Model conversation · 会話 (fictional figures)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: A customer. Ask the fictional mango price (RM8.50), pay RM10 cash and confirm the change.',
                'B: A seller. Answer, calculate change and ask A to repeat the amount.',
                'Change of plan: A asks about a different fruit priced at RM4.00 and pays with a card.',
                'Extra pair prompt: ask a fictional age and fictitious telephone digits; read them back.',
                '目標：値段をたずね、支払い、お釣りを確認。途中で品物と支払方法を変えます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say 35 years old: ____________________',
                '☐ 2. Ask the price of «mangga»: ____________________',
                '☐ 3. Pay RM10 for RM8.50. State the change: ____________________',
                '☐ 4. Say a 20 percent discount: ____________________',
                '☐ 5. Say the second visit: ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before class: Kata-Kata Sedia Kelas c03; prioritise cards ms-c03-001 to ms-c03-018.',
                'After class: complete all 56 Kata-Kata chapter 3 cards (ms-c03-001 to ms-c03-056), plus 17 approved Ch3 ledger entries without cards.',
                'Practise Kata-Kata frames ms-c03-f01 to f07 in the frame drill and Susun Ayat.',
                'Dunia scenes: "Pasar pagi" (11 recognise-only words) and "Ke bank dan pejabat pos" (13 recognise-only words).',
                'Optional full-course Cikgu Sensai units 3A (numbers, age, digits), 3B (money), and 3C (ordinals and measures).',
                'Expected independent study: about 9 to 10 hours, a provisional planning figure. Hanashishou starts at A2.',
                '授業後：第3章のカードと二つのDunia場面を復習してください。自習約9〜10時間（目安）。'], 'opener')],
        key=['Self-check: 1 «Umur saya tiga puluh lima tahun.» 2 «Berapa harga mangga?» '
             '3 «Satu ringgit lima puluh sen.» 4 «Diskaun dua puluh peratus.» 5 «Ini kali kedua saya di Malaysia.»',
             '45-minute session: 0–5 review, 5–15 words, 15–25 patterns, 25–35 conversation, 35–45 task and self-check.',
             'All practice amounts and phone numbers are invented. Japanese awaits native speaker review.'])]


PACKS.append(dict(
    chapter_id='ms-c03', check_unit='ms-c03-fast', id_prefix='ms-c03-fast',
    title_prefix='Chapter 3', header='Chapter 3 fast course (ms-c03)',
    menu_title='Chapter 3 · Numbers and money', genre='Shopping and money',
    course_path='fast', prerequisites=['ms-c01','ms-c02'], prerequisite_units=[],
    prereq_grammar=['ms-c02-g03','ms-c02-g04','ms-c02-g12'],
    word_scope=C3_WORDS, components=chapter3))


# Step 5b: chapter 4 fast course (single 45-minute class), a digest of units 4A and 4B.
C4_WORDS = ['L-0157', 'L-0158', 'L-0159', 'L-0161', 'L-0166', 'L-0167', 'L-0169', 'L-0170',
            'L-0182', 'L-0184', 'L-0185', 'L-1007', 'L-0193', 'L-0194', 'L-0189', 'L-0192',
            'L-0196', 'L-0197', 'L-0202', 'L-0208']


def chapter4(ledger):
    dialogue = [
        ('Rahman', '«Encik Tanaka, sudah makan?»'),
        ('Tanaka', '«Belum. Saya masih ada kerja. Pukul berapa sekarang?»'),
        ('Rahman', '«Sekarang pukul satu suku. Jom makan!»'),
        ('Tanaka', '«Baik. Mesyuarat kita pukul berapa?»'),
        ('Rahman', '«Mesyuarat akan mula pukul tiga dan habis pukul lima.»'),
        ('Tanaka', '«Encik biasanya makan pukul satu?»'),
        ('Rahman', '«Ya, setiap hari. Encik pula?»'),
        ('Tanaka', '«Kadang-kadang pukul dua. Saya selalu lambat!»'),
        ('Rahman', '«Hari Sabtu ini encik sibuk? Kami main badminton pukul lapan pagi.»'),
        ('Tanaka', '«Saya belum pernah main badminton di Malaysia. Jom!»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c04-g02', 'ms-c04-g03', 'ms-c04-g04', 'ms-c04-g05', 'ms-c04-g06', 'ms-c04-g07', 'ms-c04-g08'],
        patterns=['ms-c04-f01', 'ms-c04-f02', 'ms-c04-f03', 'ms-c04-f04', 'ms-c04-f05', 'ms-c04-f06', 'ms-c04-f07'],
        goal='Tell the time and day, describe a routine, and say what is done, not yet done, under way or planned.',
        explain=('第4章速習：45分で基本の20語、時刻・曜日・頻度、«sudah»・«belum»・«sedang»・«akan»・«pernah» を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 4 in one 45-minute session: 20 core words, time, days and frequency, and the markers «sudah», «belum», «sedang», «akan» and «pernah»; then self-study in Kata-Kata. All times are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can tell the time and the day, and ask «Bila …?» / 時刻と曜日が言え、«Bila …?» とたずねられる。',
                'I can say how often I do something. / 何かをする頻度が言える。',
                'I can answer «Sudah …?» with «Sudah» or «Belum». / «Sudah …?» に «Sudah» か «Belum» で答えられる。',
                'I can describe my day: what I have done, am doing and will do. / 一日について、したこと・していること・することが言える。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C4_WORDS) +
             ['Spoken forms: «dah» for «sudah», «tengah» for «sedang». Revision: «pagi», «tengah hari», «petang», «malam» (chapter 1); «suku», «setengah» (chapter 3).'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Pukul berapa sekarang?» «Sekarang pukul» ___ .  e.g. «Sekarang pukul empat suku petang.» / «Sekarang pukul dua setengah.»',
                '2 · «Hari ini hari apa?» «Hari ini hari bulan berapa?»  e.g. «Hari ini hari Khamis.» / «Hari bulan sebelas.»',
                '3 · «Saya» ___ «setiap» ___ .  e.g. «Saya main badminton setiap hari Sabtu.» / «Kadang-kadang saya masak.»',
                '4 · «Bila» ___ ?  e.g. «Bila kelas encik?» «Hari Selasa.» / «Kelas berapa jam?» «Dua jam.»',
                '5 · «Sudah» ___ ? «Sudah.» «Belum.»  e.g. «Sudah makan?» «Belum.» / «Bos sudah datang?» «Sudah.»',
                '6 · «Saya sedang» ___ . «Saya akan» ___ .  e.g. «Saya sedang makan.» / «Saya akan balik pukul tujuh.»',
                '7 · «Saya pernah» ___ .  e.g. «Saya pernah main golf.» / «Saya belum pernah main badminton.»',
                '8 · ___ «mula pukul» ___ «dan habis pukul» ___ .  e.g. «Mesyuarat mula pukul tiga dan habis pukul lima.» / «Kelas mula pukul tujuh setengah.»',
                'Remember: «pukul» + number for the clock, number + «jam» for how long. For :45 say the minutes («pukul empat empat puluh lima minit»). The verb never changes; the marker in front shows the time.',
                '時刻は «pukul»＋数、かかる時間は 数＋«jam»。45分は分の数で言います。動詞は変わらず、前の語が時を表します。'], 'model'),
            ('Model conversation · 会話 (fictional times)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: It is 12.30 p.m. Ask B whether B has eaten, what time B\'s meeting is, and invite B to lunch.',
                'B: Your fictional day: got up at 6, arrived at 8.15, have not eaten, meeting from 3 to 5. Answer with «sudah», «belum», «masih» and «akan».',
                'Change of plan: the meeting moves to 1.30 p.m. Agree a new plan, then arrange a weekly game: day, time and how long.',
                'A：Bに、もう食べたか、会議は何時かをたずね、昼ごはんに誘います。変更：会議が1時半に変わります。新しい予定と、毎週のスポーツの曜日・時刻を決めます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say 4.15 p.m.: ____________________',
                '☐ 2. Ask what day it is today: ____________________',
                '☐ 3. «Sudah makan?» Answer "not yet": ____________',
                '☐ 4. Say you will go home at 7: ____________________',
                '☐ 5. Say you play «badminton» every Saturday: ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before the session: Kata-Kata Sedia Kelas c04 (24 cards, frames ms-c04-f01 and ms-c04-f02).',
                'After the session: all 56 Kata-Kata chapter 4 cards (ms-c04-001 to ms-c04-056; «pagi», «tengah hari», «petang» and «malam» are chapter 1 revision) plus the ledger words «datang» and «bila», which have no card yet; frames ms-c04-f01 to ms-c04-f07 in the frame drill and Susun Ayat.',
                'Dunia scenes (recognise only): "Hujan petang" and "Cuti ke pantai" (unit 4A), "Satu hari Encik Tanaka" and "Bangun pagi" (unit 4B).',
                'Optional full-course Cikgu Sensai units: 4A (time, days, frequency) and 4B (routine and tense markers, timeline drill).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                '授業後：第4章のカードと Dunia の4場面を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «pukul empat suku petang» 2 «Hari ini hari apa?» 3 «Belum.» 4 «Saya akan balik pukul tujuh.» '
             '5 «Saya main badminton setiap hari Sabtu.»',
             'Session plan (45 min): 0–5 recall chapter 3 numbers; 5–15 core words and clock times; 15–25 patterns 1 to 8; '
             '25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as units 4A and 4B. All Japanese is a draft awaiting native review.'])]


PACKS.append(dict(
    chapter_id='ms-c04', check_unit='ms-c04-fast', id_prefix='ms-c04-fast',
    title_prefix='Chapter 4', header='Chapter 4 fast course (ms-c04)',
    menu_title='Chapter 4 · Time and routines', genre='Time and routines',
    course_path='fast', prerequisites=['ms-c01', 'ms-c02', 'ms-c03'], prerequisite_units=[],
    prereq_grammar=['ms-c01-g02', 'ms-c03-g02', 'ms-c03-g06'],
    word_scope=C4_WORDS, components=chapter4))


# Step 5c: chapter 5 fast course (single 45-minute class), a digest of unit 5.
C5_WORDS = ['L-0209', 'L-0210', 'L-1009', 'L-0688', 'L-0212', 'L-0214', 'L-0215', 'L-0213',
            'L-0218', 'L-0221', 'L-0223', 'L-0224', 'L-0226', 'L-0230', 'L-0237', 'L-0238',
            'L-0249', 'L-0250', 'L-0256', 'L-0257']


def chapter5(ledger):
    dialogue = [
        ('Aini', '«Encik Tanaka, encik rasa bagaimana hari ini?»'),
        ('Tanaka', '«Saya penat, tetapi gembira.»'),
        ('Aini', '«Kenapa encik penat?»'),
        ('Tanaka', '«Sebab semalam saya balik lewat. Saya belum makan. Saya lapar!»'),
        ('Aini', '«Jom makan di mamak!»'),
        ('Tanaka', '«Baik! Puan Aini mahu makan apa?»'),
        ('Aini', '«Roti canai. Encik mahu teh atau kopi?»'),
        ('Tanaka', '«Teh tarik, kurang manis. Sejuk, ais sedikit.»'),
        ('Aini', '«Mi goreng di mamak itu pedas, tetapi sedap.»'),
        ('Tanaka', '«Saya mahu mi goreng yang tidak pedas.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c05-g02', 'ms-c05-g03', 'ms-c05-g04', 'ms-c05-g05', 'ms-c05-g06'],
        patterns=['ms-c05-f01', 'ms-c05-f02', 'ms-c05-f03', 'ms-c05-f04', 'ms-c05-f05'],
        goal='Describe food, drink and feelings with adjectives, ask how and why, and order a drink the way you like it.',
        explain=('第5章速習：45分で基本の20語、形容詞の使い方、«Bagaimana …?»・«Kenapa …?»、飲み物の注文を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 5 in one 45-minute session: 20 core words, adjectives after the noun, «Bagaimana …?» and «Kenapa …?» with «sebab», and ordering a drink; then self-study in Kata-Kata. All prices and situations are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can describe food, drink, colours and sizes with an adjective after the noun. / 名詞のあとに形容詞を置いて、食べ物・飲み物・色・大きさを描写できる。',
                'I can say how I feel and ask «Kenapa …?» and answer with «Sebab …». / 気分を言い、«Kenapa …?» とたずね、«Sebab …» で答えられる。',
                'I can ask «Bagaimana rasa …?» and answer with «…, tetapi …». / «Bagaimana rasa …?» とたずね、«…, tetapi …» で答えられる。',
                'I can order a drink: how sweet, hot or cold, and ice. / 飲み物の甘さ・温度・氷を言って注文できる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C5_WORDS) +
             ['Spoken forms: «nak» for «mahu», «tapi» for «tetapi», «macam mana» for «bagaimana». Revision: «sedikit» (chapter 2), «kosong» in «air kosong» (chapter 3).'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · (noun) «ini» (adjective).  e.g. «Teh ini manis.» / «Cili itu merah.»',
                '2 · «Bagaimana rasa» ___ ? ___ , «tetapi» ___ .  e.g. «Bagaimana rasa mi goreng ini?» «Sedap, tetapi pedas.» / «Bagaimana rasa kopi ini?» «Pahit.»',
                '3 · «Saya mahu» ___ «yang» ___ .  e.g. «Saya mahu payung yang biru.» / «Panas atau sejuk?» «Sejuk.»',
                '4 · «Saya rasa» ___ . «Kenapa» ___ ? «Sebab» ___ .  e.g. «Saya rasa penat.» / «Kenapa lambat?» «Sebab hujan.»',
                '5 · «Saya mahu» ___ , «kurang manis», «ais sedikit».  e.g. «Saya mahu teh tarik, kurang manis.» / «Air kosong satu, ya.»',
                'Remember: the adjective comes after the noun and never changes; «tidak» goes before an adjective, «bukan» before a noun. «sebab» (or «kerana») comes before the reason; «kenapa», «mengapa» and «apa sebab» all mean "why". «kurang manis» is a fixed ordering phrase; comparing things comes in chapter 6.',
                '形容詞は名詞のあとに置き、形は変わりません。否定は形容詞の前に «tidak»、名詞の前に «bukan»。«sebab»（または «kerana»）は理由の前に置き、«kenapa»・«mengapa»・«apa sebab» はどれも「なぜ」です。«kurang manis» は注文の決まった言い方で、比べる言い方は第6章で学びます。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are at a «mamak» stall. Order a cold drink, less sweet, with a little ice, and ask how the «mi goreng» tastes.',
                'B: You work at the stall. Ask hot or cold, answer about taste, and say the total (invented price).',
                'Change of plan: the «mi goreng» is finished. Choose «roti canai» or «nasi», then order for a friend who wants a hot drink.',
                'A：«mamak» の店で、甘さ控えめ・氷少なめの冷たい飲み物を注文し、«mi goreng» の味をたずねます。変更：«mi goreng» が売り切れ。別の料理を選び、友達の熱い飲み物も頼みます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "This tea is sweet.": ____________________',
                '☐ 2. Ask how this coffee tastes: ____________________',
                '☐ 3. Say you are tired because you got home late yesterday: ____________________',
                '☐ 4. Say you want the blue umbrella: ____________________',
                '☐ 5. Order a tea, less sweet, cold, with a little ice: ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before the session: Kata-Kata Sedia Kelas c05 (23 cards, frames ms-c05-f01 and ms-c05-f02).',
                'After the session: all 58 Kata-Kata chapter 5 cards (ms-c05-001 to ms-c05-058; ms-c05-008 «sedikit» is chapter 2 revision) plus the ledger words «kenapa», «mengapa», «sebab», «kerana», «kuah» and «kelakar», which have no chapter 5 card yet; frames ms-c05-f01 to ms-c05-f05 in the frame drill and Susun Ayat.',
                'Dunia scenes (recognise only): "Masak nasi goreng", "Di klinik", "Gambar bayi" and "Lepak di kedai mamak".',
                'Optional full-course Cikgu Sensai unit: unit 5 (adjectives, with its writing block).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                '授業後：第5章のカードと Dunia の4場面を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Teh ini manis.» 2 «Bagaimana rasa kopi ini?» 3 «Saya penat sebab semalam saya balik lewat.» '
             '4 «Saya mahu payung yang biru.» 5 «Saya mahu teh, kurang manis. Sejuk, ais sedikit.»',
             'Session plan (45 min): 0–5 recall chapter 4 («Sudah makan?», the time); 5–15 core words by theme; 15–25 patterns 1 to 5; '
             '25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 5. All Japanese is a draft awaiting native review.'])]


PACKS.append(dict(
    chapter_id='ms-c05', check_unit='ms-c05-fast', id_prefix='ms-c05-fast',
    title_prefix='Chapter 5', header='Chapter 5 fast course (ms-c05)',
    menu_title='Chapter 5 · Adjectives', genre='Describing and choosing',
    course_path='fast', prerequisites=['ms-c01', 'ms-c02', 'ms-c03', 'ms-c04'], prerequisite_units=[],
    prereq_grammar=['ms-c02-g03', 'ms-c02-g04', 'ms-c04-g06'],
    word_scope=C5_WORDS, components=chapter5))


# Step 5d: chapter 6 fast course (single 45-minute class), a digest of unit 6.
C6_WORDS = ['L-0265', 'L-0266', 'L-0267', 'L-0268', 'L-0274', 'L-0275', 'L-0277', 'L-0271', 'L-0273', 'L-0279',
            'L-0280', 'L-0288', 'L-0289', 'L-0290', 'L-0291', 'L-0292', 'L-0294', 'L-1051', 'L-1052', 'L-1053']


def chapter6(ledger):
    dialogue = [
        ('Mei Ling', '«Encik Tanaka, encik suka kondo yang mana?»'),
        ('Tanaka', '«Kondo A lebih besar daripada kondo B, tetapi kondo A lebih mahal. Berapa sewa kondo A?»'),
        ('Mei Ling', '«Tiga ribu dua ratus ringgit setiap bulan. Kondo A ada tiga bilik.»'),
        ('Tanaka', '«Kondo B ada berapa bilik?»'),
        ('Mei Ling', '«Kondo B ada dua bilik, kurang luas, tetapi sunyi. Kondo C paling murah, tetapi terlalu bising.»'),
        ('Tanaka', '«Kondo D bagaimana?»'),
        ('Mei Ling', '«Kondo D sama mahal dengan kondo A, tetapi luas, sangat selesa dan bersih.»'),
        ('Tanaka', '«Kondo D yang terbaik! Saya pilih kondo D.»'),
        ('Mei Ling', '«Baik, encik.»'),
        ('Tanaka', '«Terima kasih, Cik Mei Ling!»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c06-g02', 'ms-c06-g03', 'ms-c06-g04', 'ms-c06-g05', 'ms-c06-g06'],
        patterns=['ms-c06-f01', 'ms-c06-f02', 'ms-c06-f03', 'ms-c06-f04', 'ms-c06-f05', 'ms-c06-f06'],
        goal='Compare places and things, say which is the most, choose between them and describe a place.',
        explain=('第6章速習：45分で基本の20語、«lebih … daripada»・«sama … dengan»・«paling»、«sangat»・«terlalu»、«Yang mana …?» と «pilih» を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 6 in one 45-minute session: 20 core words, comparing with «lebih … daripada», «sama … dengan» and «paling», «sangat» and «terlalu», and «Yang mana …?» with «pilih»; then self-study in Kata-Kata. All prices and situations are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can compare two things with «lebih» or «kurang» and «daripada», and say they are the same with «sama … dengan». / «lebih»・«kurang» と «daripada» で二つを比べ、«sama … dengan» で同じだと言える。',
                'I can say which is the most with «paling» and use «sangat» and «terlalu». / «paling» で一番を言い、«sangat»・«terlalu» を使える。',
                'I can ask «Yang mana …?» and answer with «Saya pilih …». / «Yang mana …?» とたずね、«Saya pilih …» で答えられる。',
                'I can describe a place and a home: comfortable, spacious, quiet, noisy, crowded, clean, the rent and the rooms. / 場所と住まいを描写できる：快適、広い、静か、うるさい、混んでいる、清潔、家賃と部屋数。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C6_WORDS) +
             ['Whole words to learn as they are: «termurah», «terbesar», «terbaik», «tercantik», «setinggi», «semahal». «sekali» (very, after an adjective) and «baru» (new) are chapter 4 words with a new meaning.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · (A) «lebih» / «kurang» (adjective) «daripada» (B).  e.g. «Kondo A lebih besar daripada kondo B.» / «Kondo B kurang mahal daripada kondo A.»',
                '2 · (A) «sama» (adjective) «dengan» (B).  e.g. «Kondo D sama mahal dengan kondo A.» / «Kondo B sama besar dengan kondo C.»',
                '3 · (A) «paling» (adjective).  e.g. «Kondo C paling murah.» / «Kondo D yang terbaik.»',
                '4 · (noun) «sangat» / «terlalu» (adjective).  e.g. «Kondo D sangat selesa.» / «Kondo C terlalu bising.»',
                '5 · «Yang mana» ___ ?  «Saya pilih» ___ .  e.g. «Yang mana lebih selesa?» «Kondo D.» / «Encik pilih yang mana?» «Saya pilih kondo D.»',
                'Remember: the adjective never changes. «lebih», «kurang», «paling», «sangat» and «terlalu» go before it; «sekali» (very) goes after it. «daripada» comes after the adjective, before the thing you compare with. «terlalu» means too much; «sangat» means very. «termurah», «terbaik» and the other whole words are learned as they are; for other adjectives use «paling» and «sama … dengan».',
                '形容詞は変わりません。«lebih»・«kurang»・«paling»・«sangat»・«terlalu» は形容詞の前、«sekali»（とても）はあとに置きます。«daripada» は形容詞のあと、比べる相手の前に置きます。«terlalu» は「〜すぎる」、«sangat» は「とても」です。«termurah»・«terbaik» などの一語はそのまま覚え、ほかの形容詞には «paling» と «sama … dengan» を使います。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are looking for a condo (fictional). Ask B the rent and the number of rooms, which condo is the cheapest and which is the most expensive, then choose one.',
                'B: You are the agent. Compare the condos with «lebih», «paling» and «sangat» (invented prices); say when one is too noisy or too small.',
                'Change of plan: the condo A chose has been taken (B says «Orang lain sudah ambil kondo itu.»). A asks «Yang mana …?» and chooses again.',
                'A：コンドを探しているお客さん。家賃と部屋数、一番安いものと一番高いものをたずね、一つ選びます。変更：選んだコンドはすでに他の人に取られてしまい、もう一度 «Yang mana …?» で選びます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "Condo A is bigger than condo B.": ____________________',
                '☐ 2. Say "Condo D is as expensive as condo A.": ____________________',
                '☐ 3. Say "Condo C is the cheapest.": ____________________',
                '☐ 4. Say "This condo is too noisy.": ____________________',
                '☐ 5. Ask "Which condo do you choose?": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before the session: Kata-Kata Sedia Kelas c06 (16 cards, frames ms-c06-f01 and ms-c06-f02).',
                'After the session: all 34 Kata-Kata chapter 6 cards (ms-c06-001 to ms-c06-034; «sewa», «bilik» and «luas» have no card yet; ms-c06-008 «sekali» and ms-c06-021 «baru» are chapter 4 words with new meanings) and frames ms-c06-f01 to ms-c06-f06 in the frame drill and Susun Ayat.',
                'Dunia scene (recognise only): "Main badminton" (14 words).',
                'Optional full-course Cikgu Sensai unit: unit 6 (comparing and choosing).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                '授業後：第6章のカードと Dunia の場面を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Kondo A lebih besar daripada kondo B.» 2 «Kondo D sama mahal dengan kondo A.» (or «semahal») '
             '3 «Kondo C paling murah.» (or «termurah») 4 «Kondo ini terlalu bising.» 5 «Encik pilih kondo yang mana?» (or «Kondo yang mana encik pilih?»)',
             'Session plan (45 min): 0–5 recall chapter 5 (taste, hot or cold, «Kenapa …?»); 5–15 core words by theme; 15–25 patterns 1 to 5; '
             '25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 6. All Japanese is a draft awaiting native review.'])]


PACKS.append(dict(
    chapter_id='ms-c06', check_unit='ms-c06-fast', id_prefix='ms-c06-fast',
    title_prefix='Chapter 6', header='Chapter 6 fast course (ms-c06)',
    menu_title='Chapter 6 · Comparatives and superlatives', genre='Describing and choosing',
    course_path='fast', prerequisites=['ms-c01', 'ms-c02', 'ms-c03', 'ms-c04', 'ms-c05'], prerequisite_units=[],
    prereq_grammar=['ms-c03-g04', 'ms-c04-g06', 'ms-c05-g02'],
    word_scope=C6_WORDS, components=chapter6))


# Step 5e: chapter 7 fast course (single 45-minute class), a digest of unit 7.
C7_WORDS = ['L-0296', 'L-0297', 'L-0298', 'L-0302', 'L-0303', 'L-0305', 'L-0310', 'L-0312', 'L-0313', 'L-0314',
            'L-0315', 'L-0316', 'L-0317', 'L-1060', 'L-0319', 'L-0320', 'L-0322', 'L-0323', 'L-0328', 'L-0331']


def chapter7(ledger):
    dialogue = [
        ('Tanaka', '«Maaf, tumpang tanya, bank di mana?»'),
        ('Siti', '«Jalan terus, kemudian belok kanan di lampu isyarat.»'),
        ('Tanaka', '«Berapa jauh dari sini?»'),
        ('Siti', '«Tidak jauh. Lebih kurang lima ratus meter.»'),
        ('Tanaka', '«Bank di sebelah kiri atau kanan?»'),
        ('Siti', '«Di sebelah kanan, di seberang kedai.»'),
        ('Tanaka', '«Pejabat saya jauh. Berapa lama ke sana naik bas?»'),
        ('Siti', '«Lebih kurang dua puluh minit.»'),
        ('Tanaka', '«Terima kasih banyak, cik!»'),
        ('Siti', '«Sama-sama, encik.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c07-g02', 'ms-c07-g03', 'ms-c07-g04', 'ms-c07-g05', 'ms-c07-g06'],
        patterns=['ms-c07-f01', 'ms-c07-f02', 'ms-c07-f03', 'ms-c07-f04', 'ms-c07-f05'],
        goal='Say where places are, ask for and give directions, and talk about distance, time and transport.',
        explain=('第7章速習：45分で基本の20語、«ke»・«dari»、«di» と位置の語、«jalan terus, kemudian belok»、«Berapa jauh?»・«Berapa lama?» を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 7 in one 45-minute session: 20 core words, «ke» and «dari», «di» with position words, «jalan terus, kemudian belok», «Berapa jauh?» and «Berapa lama?»; then self-study in Kata-Kata. All places, routes and times are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say where I am going and where I come from with «ke» and «dari». / «ke»・«dari» で行き先と出発点を言える。',
                'I can say where something is with «di» and a position word. / «di» と位置の語でものの場所を言える。',
                'I can give and follow a route with «jalan terus», «kemudian belok kiri» or «kanan». / «jalan terus»・«kemudian belok kiri/kanan» で道順を言ったり聞いたりできる。',
                'I can ask «Berapa jauh?» and «Berapa lama?» and answer with «lebih kurang». / «Berapa jauh?»・«Berapa lama?» とたずね、«lebih kurang» で答えられる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C7_WORDS) +
             ['«depan» (front) is a chapter 4 word; «hadapan» is its formal form. The full unit also teaches the landmarks, transport and compass words.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Saya pergi ke» (place). / «pergi ke mana?» / «datang dari mana?»  e.g. «Saya pergi ke pejabat.» / «Puan datang dari mana?»',
                '2 · (place) «di» (position word) (landmark).  e.g. «Bank di depan stesen.» / «Tandas di sebelah lif.»',
                '3 · «Jalan terus, kemudian belok» «kiri» / «kanan» «di» (landmark).  e.g. «Jalan terus, kemudian belok kanan di lampu isyarat.» / «Belok kiri di simpang.»',
                '4 · «Berapa jauh» (place) «dari sini?» / «Lebih kurang» (distance).  e.g. «Berapa jauh stesen dari sini?» / «Lebih kurang lima ratus meter.»',
                '5 · «Berapa lama ke» (place)? / «Lebih kurang» (number) «minit naik» (transport).  e.g. «Berapa lama ke pejabat?» / «Lebih kurang dua puluh minit naik bas.»',
                'Remember: «ke» goes before the place you go to, «di» before the place you are at, «dari» before the place you come from. The position word comes straight after «di». «pergi kerja» and «balik rumah» are everyday speech; «pergi ke pejabat» and «balik ke rumah» are the standard forms.',
                '«ke» は行き先の前、«di» はいる場所の前、«dari» は出発点の前に置きます。位置の語は «di» のすぐあとに来ます。«pergi kerja»・«balik rumah» は日常の話し言葉で、«pergi ke pejabat»・«balik ke rumah» が標準の形です。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are at the station (fictional). Ask B the way to the hospital: where it is, how far and how long on foot.',
                'B: You live nearby. Give the route with «jalan terus», «kemudian belok» and a landmark (invented distances).',
                'Change of plan: B says «Hari ini jam. Bas lambat.» A asks «Kalau jalan kaki, berapa lama?» and decides.',
                'A：駅にいる旅行者。病院への道、距離、歩いて何分かをたずねます。変更：Bが «Hari ini jam. Bas lambat.» と言い、Aは «Kalau jalan kaki, berapa lama?» とたずねて決めます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "I am going to the bank.": ____________________',
                '☐ 2. Say "The bank is in front of the station.": ____________________',
                '☐ 3. Say "Go straight, then turn left at the traffic lights.": ____________________',
                '☐ 4. Ask "How far is the station from here?": ____________________',
                '☐ 5. Ask "How long does it take to the office by bus?": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before the session: Kata-Kata Sedia Kelas c07 (27 cards, frames ms-c07-f01 and ms-c07-f02).',
                'After the session: all 49 Kata-Kata chapter 7 cards (ms-c07-001 to ms-c07-049) and frames ms-c07-f01 to ms-c07-f05 in the frame drill and Susun Ayat; the words for the places of worship («gereja», «kuil», «tokong», «gurdwara», «surau») and the words added in step 5f («kilometer», «terus», «tangga», «jangan», «sebulan») have no card yet; card ms-c07-024 still teaches «jalan lurus», which is not used for directions.',
                'Dunia scenes (recognise only): "Di ruang tamu", "Telefon baru" and "Lintas jalan" (33 words).',
                'Optional full-course Cikgu Sensai unit: unit 7 (locations and directions).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                '授業後：第7章のカードと Dunia の場面を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Saya pergi ke bank.» 2 «Bank di depan stesen.» 3 «Jalan terus, kemudian belok kiri di lampu isyarat.» '
             '4 «Berapa jauh stesen dari sini?» 5 «Berapa lama ke pejabat naik bas?»',
             'Session plan (45 min): 0–5 recall chapter 6 (compare two homes, «Yang mana …?»); 5–15 core words by theme; 15–25 patterns 1 to 5; '
             '25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 7. All Japanese is a draft awaiting native review.'])]


PACKS.append(dict(
    chapter_id='ms-c07', check_unit='ms-c07-fast', id_prefix='ms-c07-fast',
    title_prefix='Chapter 7', header='Chapter 7 fast course (ms-c07)',
    menu_title='Chapter 7 · Locations and directions', genre='Wayfinding',
    course_path='fast', prerequisites=['ms-c01', 'ms-c02', 'ms-c03', 'ms-c04', 'ms-c05', 'ms-c06'], prerequisite_units=[],
    prereq_grammar=['ms-c02-g08', 'ms-c04-g06', 'ms-c06-g02'],
    word_scope=C7_WORDS, components=chapter7))


# Step 5f: chapter 8 fast course (single 45-minute class), a digest of unit 8.
C8_WORDS = ['L-0343', 'L-0344', 'L-0345', 'L-0346', 'L-0350', 'L-0353', 'L-0354', 'L-0355', 'L-0357', 'L-0359',
            'L-0360', 'L-0361', 'L-0362', 'L-0364', 'L-0365', 'L-0366', 'L-0370', 'L-0374', 'L-0375', 'L-0376']


def chapter8(ledger):
    dialogue = [
        ('Ali', '«Selamat pagi, encik. Encik mahu apa?»'),
        ('Tanaka', '«Ikan ini berapa seekor?»'),
        ('Ali', '«Lapan ringgit seekor. Telur lima puluh sen sebiji.»'),
        ('Tanaka', '«Saya mahu dua ekor ikan dan sepuluh biji telur.»'),
        ('Ali', '«Ayam juga? Ayam besar, empat belas ringgit seekor.»'),
        ('Tanaka', '«Ya, seekor ayam. Berapa harga semua?»'),
        ('Ali', '«Semua tiga puluh lima ringgit.»'),
        ('Tanaka', '«Tolong bungkus ikan dan ayam, ya.»'),
        ('Ali', '«Baik. Terima kasih, encik.»'),
        ('Tanaka', '«Sama-sama, Pak cik.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c08-g02', 'ms-c08-g03', 'ms-c08-g04', 'ms-c08-g05', 'ms-c08-g06'],
        patterns=['ms-c08-f01', 'ms-c08-f02', 'ms-c08-f03', 'ms-c08-f04', 'ms-c08-f05'],
        goal='Order and count things with the right classifier, ask how many and how much, and order food to eat here or take away.',
        explain=('第8章速習：45分で基本の20語、数＋助数詞＋名詞、«seekor»・«sebiji»・«sebuah»、«Berapa biji?»、«Tolong bungkus»・«Makan sini atau bungkus?» を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 8 in one 45-minute session: 20 core words, number + counter + noun, «seekor», «sebiji» and «sebuah», «Berapa biji?», «Tolong bungkus» and «Makan sini atau bungkus?»; then self-study in Kata-Kata. All stalls, prices and names are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say how many of something I want with a number, a counter and the noun. / 数・助数詞・名詞でほしい数が言える。',
                'I can use «seekor», «sebiji» and «sebuah», and «satu» + counter for the rest. / «seekor»・«sebiji»・«sebuah» と、ほかは «satu» ＋ 助数詞が使える。',
                'I can ask «Berapa biji?» and the price of one and of everything. / «Berapa biji?» と、1つと全部の値段がたずねられる。',
                'I can order «Tolong bungkus …» and answer «Makan sini atau bungkus?». / «Tolong bungkus …» と注文し、«Makan sini atau bungkus?» に答えられる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C8_WORDS) +
             ['The full unit also teaches the other counters («keping», «pucuk», «kuntum», «ulas», «naskhah»), the bowls, tins and boxes, and the things counted.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Saya mahu» (number) (counter) (noun).  e.g. «Saya mahu dua ekor ikan.» / «Saya mahu tiga batang pen.»',
                '2 · «seekor» / «sebiji» / «sebuah» (noun). / «satu» (counter) (noun).  e.g. «Saya ada seekor kucing.» / «Satu helai baju, tolong.»',
                '3 · «Berapa» (counter) (noun)?  e.g. «Berapa biji telur?» / «Sepuluh biji.»',
                '4 · (price) «ringgit» «satu» (counter).  e.g. «Berapa harga semua?» / «Lima ringgit satu kuntum.»',
                '5 · «Tolong bungkus» (number) (food). / «Makan sini atau bungkus?»  e.g. «Makan sini atau bungkus?» / «Tolong bungkus dua roti canai.»',
                'Remember: the counter sits between the number and the noun and never changes. Only «seekor», «sebiji» and «sebuah» are fused with «satu»; use «satu» + counter for every other. At a stall people often drop the counter («dua teh tarik»): that is everyday speech.',
                '助数詞は数と名詞のあいだに置き、形は変わりません。«satu» とひとつになるのは «seekor»・«sebiji»・«sebuah» だけで、ほかは «satu» ＋ 助数詞です。屋台では助数詞を落として «dua teh tarik» と言うこともあり、これは日常の話し言葉です。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are at a «mamak» stall (fictional). Order one plate of «mi goreng» and one «teh tarik» to eat here and three «roti canai» to take away. Ask the total.',
                'B: You work at the stall. Ask «Makan sini atau bungkus?», repeat the order and give the total (invented prices).',
                'Change of plan: A says «Dua orang kawan datang. Dua cawan teh tarik lagi, tolong.» B gives the new total.',
                'A：ママックの店で、ミー・ゴレン1皿とテ・タリック1杯は店内、ロティ・チャナイ3枚は持ち帰りで注文し、合計をたずねます。変更：Aが «Dua orang kawan datang. Dua cawan teh tarik lagi, tolong.» と言い、Bが新しい合計を言います。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "I want two fish.": ____________________',
                '☐ 2. Say "One cat.": ____________________',
                '☐ 3. Ask "How many eggs?": ____________________',
                '☐ 4. Ask "How much for everything?": ____________________',
                '☐ 5. Say "Please wrap three «roti canai».": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                'Before the session: Kata-Kata Sedia Kelas c08 (13 cards, frames ms-c08-f01 and ms-c08-f02).',
                'After the session: all 43 Kata-Kata chapter 8 cards (ms-c08-001 to ms-c08-043) and frames ms-c08-f01 to ms-c08-f05 in the frame drill and Susun Ayat; the Kata-Kata scenario uses ‹nasi lemak›, which is not in the ledger, so the fast pack uses «roti canai».',
                'Dunia scene (recognise only): "Beli baju" (11 words).',
                'Optional full-course Cikgu Sensai unit: unit 8 (counters).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                '授業後：第8章のカードと Dunia の場面を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Saya mahu dua ekor ikan.» 2 «Seekor kucing.» (or «Satu ekor kucing.») 3 «Berapa biji telur?» '
             '4 «Berapa harga semua?» 5 «Tolong bungkus tiga roti canai.»',
             'Session plan (45 min): 0–5 recall chapter 7 (ask the way to the market); 5–15 core words by theme; 15–25 patterns 1 to 5; '
             '25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 8. All Japanese is a draft awaiting native review.'])]


PACKS.append(dict(
    chapter_id='ms-c08', check_unit='ms-c08-fast', id_prefix='ms-c08-fast',
    title_prefix='Chapter 8', header='Chapter 8 fast course (ms-c08)',
    menu_title='Chapter 8 · Counters', genre='Shopping and ordering',
    course_path='fast', prerequisites=['ms-c01', 'ms-c02', 'ms-c03', 'ms-c04', 'ms-c05', 'ms-c06', 'ms-c07'], prerequisite_units=[],
    prereq_grammar=['ms-c03-g04', 'ms-c04-g06', 'ms-c05-g06'],
    word_scope=C8_WORDS, components=chapter8))
