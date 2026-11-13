"""Fast-course summary packs for chapters 1 and 2 (charter section 6: one
45-minute session per chapter, then self-study in Kata-Kata). Same chapter
content and ledger limits as the full-course units. Japanese is a draft.
"""
from . import core, turns, sedia_cards, pack_cards, last_card

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
                f'Before the session: Kata-Kata Sedia Kelas c01 ({sedia_cards(1)} cards, frames ms-c01-f01 and f02).',
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
                f'Before the session: Kata-Kata Sedia Kelas c02 ({sedia_cards(2)} cards, frames ms-c02-f01 and f02).',
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
                f'After class: complete all {pack_cards(3)} Kata-Kata chapter 3 cards (ms-c03-001 to ms-c03-{last_card(3):03}), including the 17 new cards for the approved Ch3 ledger entries.',
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
                f'Before the session: Kata-Kata Sedia Kelas c04 ({sedia_cards(4)} cards, frames ms-c04-f01 and ms-c04-f02).',
                f'After the session: all {pack_cards(4)} Kata-Kata chapter 4 cards (ms-c04-001 to ms-c04-{last_card(4):03}; cards ms-c04-008 to -011, «pagi», «tengah hari», «petang» and «malam», now belong to chapter 1 and are revision here), including the new cards for «datang» and «bila»; frames ms-c04-f01 to ms-c04-f07 in the frame drill and Susun Ayat.',
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
        patterns=['ms-c05-f01', 'ms-c05-f02', 'ms-c05-f03', 'ms-c05-f04', 'ms-c05-f05', 'ms-c05-f06'],
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
                f'Before the session: Kata-Kata Sedia Kelas c05 ({sedia_cards(5)} cards, frames ms-c05-f01 and ms-c05-f02).',
                f'After the session: all {pack_cards(5)} Kata-Kata chapter 5 cards (ms-c05-001 to ms-c05-{last_card(5):03}; ms-c05-008 «sedikit» now belongs to chapter 2 and is revision here), including the new cards for «kenapa», «mengapa», «sebab», «kerana», «kuah» and «kelakar»; frames ms-c05-f01 to ms-c05-f06 in the frame drill and Susun Ayat (f06 is the «kenapa» / «mengapa» frame).',
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
        patterns=['ms-c06-f01', 'ms-c06-f02', 'ms-c06-f03', 'ms-c06-f04', 'ms-c06-f05', 'ms-c06-f06', 'ms-c06-f07'],
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
                f'Before the session: Kata-Kata Sedia Kelas c06 ({sedia_cards(6)} cards, frames ms-c06-f01 and ms-c06-f02).',
                f'After the session: all {pack_cards(6)} Kata-Kata chapter 6 cards (ms-c06-001 to ms-c06-{last_card(6):03}, including the new cards for «sewa», «bilik» and «luas»; ms-c06-008 «sekali» and ms-c06-021 «baru» are chapter 4 words with new meanings) and frames ms-c06-f01 to ms-c06-f07 in the frame drill and Susun Ayat (f07 is «Saya pilih ___»).',
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
                f'Before the session: Kata-Kata Sedia Kelas c07 ({sedia_cards(7)} cards, frames ms-c07-f01 and ms-c07-f02).',
                f'After the session: all {pack_cards(7)} Kata-Kata chapter 7 cards (ms-c07-001 to ms-c07-{last_card(7):03}; ms-c07-009 «depan» is now one card with chapter 4, ms-c04-019) and frames ms-c07-f01 to ms-c07-f05 in the frame drill and Susun Ayat; the places of worship («gereja», «kuil», «tokong», «gurdwara», «surau») and the words added in step 5f («kilometer», «terus», «tangga», «jangan», «sebulan») now have their cards, and directions are «jalan terus», «pergi terus» and «terus depan».',
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
C8_WORDS = ['L-0343', 'L-0344', 'L-0345', 'L-0346', 'L-0347', 'L-0350', 'L-0353', 'L-0354', 'L-0357', 'L-0359',
            'L-0360', 'L-0361', 'L-0362', 'L-1064', 'L-1065', 'L-1066', 'L-1068', 'L-0374', 'L-0375', 'L-0376']


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
        explain=('第8章速習：45分で基本の20語、数＋助数詞＋名詞、‹se-› ＋助数詞（«sehelai»・«secawan»）、«Berapa biji?»、«Tolong bungkus»・«Makan sini atau bungkus?»・«Tambah satu lagi» を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 8 in one 45-minute session: 20 core words, number + counter + noun, ‹se-› + counter («sehelai», «secawan»), «Berapa biji?», «Tolong bungkus», «Makan sini atau bungkus?» and «Tambah satu lagi»; then self-study in Kata-Kata. All stalls, prices and names are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say how many of something I want with a number, a counter and the noun. / 数・助数詞・名詞でほしい数が言える。',
                'I can say "one" with ‹se-› and a counter («sehelai», «secawan») or with «satu» and the counter. / 「1」を ‹se-› ＋助数詞（«sehelai»・«secawan»）か «satu» ＋助数詞で言える。',
                'I can ask «Berapa biji?» and the price of one and of everything. / «Berapa biji?» と、1つと全部の値段がたずねられる。',
                'I can order «Tolong bungkus …», add «Tambah satu lagi» and answer «Makan sini atau bungkus?». / «Tolong bungkus …» と注文し、«Tambah satu lagi» で追加し、«Makan sini atau bungkus?» に答えられる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C8_WORDS) +
             ['The full unit also teaches the other counters («pucuk», «kuntum», «ulas», «naskhah»), the plates, bowls and tins, «keropok lekor», and the things counted. Every counter has a ‹se-› form: «sehelai», «sebatang», «sekeping», «sepasang», «sebungkus», «secawan», «sebotol», «sekotak».'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Saya mahu» (number) (counter) (noun).  e.g. «Saya mahu dua ekor ikan.» / «Saya mahu tiga batang pen.»',
                '2 · ‹se-› + (counter) (noun). / «satu» (counter) (noun).  e.g. «Sehelai baju, tolong.» / «Satu helai baju, tolong.»',
                '3 · «Berapa» (counter) (noun)?  e.g. «Berapa biji telur?» / «Sepuluh biji.»',
                '4 · (price) «ringgit» ‹se-› (counter).  e.g. «Bunga ini berapa sekuntum?» / «Lima ringgit sekuntum.»',
                '5 · «Tolong bungkus» (number) (food). / «Makan sini atau bungkus?» / «Tambah satu lagi.»  e.g. «Makan sini atau bungkus?» / «Sebungkus nasi lemak, tolong. Tambah satu lagi.»',
                'Remember: the counter sits between the number and the noun and never changes. For "one", ‹se-› + counter and «satu» + counter are both right: «sehelai baju» = «satu helai baju». At a stall people often drop the counter («dua teh tarik»): that is everyday speech.',
                '助数詞は数と名詞のあいだに置き、形は変わりません。「1」は ‹se-› ＋助数詞でも «satu» ＋助数詞でも正しく、«sehelai baju» = «satu helai baju» です。屋台では助数詞を落として «dua teh tarik» と言うこともあり、これは日常の話し言葉です。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are at a «mamak» stall (fictional). Order one plate of «mi goreng» and one «teh tarik» to eat here and three «roti canai» to take away. Ask the total.',
                'B: You work at the stall. Ask «Makan sini atau bungkus?», repeat the order and give the total (invented prices).',
                'Change of plan: A says «Dua orang kawan datang. Tambah dua cawan teh tarik, tolong.» B gives the new total.',
                'A：ママックの店で、ミー・ゴレン1皿とテ・タリック1杯は店内、ロティ・チャナイ3枚は持ち帰りで注文し、合計をたずねます。変更：Aが «Dua orang kawan datang. Tambah dua cawan teh tarik, tolong.» と言い、Bが新しい合計を言います。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "I want two fish.": ____________________',
                '☐ 2. Say "One shirt." with ‹se-›: ____________________',
                '☐ 3. Ask "How many eggs?": ____________________',
                '☐ 4. Ask "How much for everything?": ____________________',
                '☐ 5. Say "Please wrap three «roti canai».": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c08 ({sedia_cards(8)} cards, frames ms-c08-f01 and ms-c08-f02).',
                f'After the session: all {pack_cards(8)} Kata-Kata chapter 8 cards (ms-c08-001 to ms-c08-{last_card(8):03}; ms-c08-010 was removed in the Kata-Kata clean-up) and frames ms-c08-f01 to ms-c08-f05 in the frame drill and Susun Ayat; the Kata-Kata scenario "Morning market and takeaway" uses «nasi lemak», which is a chapter 8 ledger word (L-1064) with its own card.',
                'Dunia scene (recognise only): "Beli baju" (11 words).',
                'Optional full-course Cikgu Sensai unit: unit 8 (counters).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                '授業後：第8章のカードと Dunia の場面を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Saya mahu dua ekor ikan.» 2 «Sehelai baju.» (or «Satu helai baju.») 3 «Berapa biji telur?» '
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


# Step 5g: chapter 9 fast course (single 45-minute class), a digest of unit 9.
C9_WORDS = ['L-0377', 'L-0378', 'L-0379', 'L-0405', 'L-0380', 'L-0381', 'L-0383', 'L-0384', 'L-0387', 'L-0388',
            'L-0389', 'L-0390', 'L-0395', 'L-0397', 'L-0398', 'L-0399', 'L-0401', 'L-0402', 'L-0403', 'L-0404']


def chapter9(ledger):
    dialogue = [
        ('Aini', '«Kek ini dibuat oleh siapa?»'),
        ('Tanaka', '«Dibuat oleh isteri saya.»'),
        ('Aini', '«Sedap sekali! Nasi lemak ini dibeli di mana?»'),
        ('Rahman', '«Dibeli di gerai pagi tadi.»'),
        ('Mei Ling', '«Teh tarik sudah diminum semua.»'),
        ('Tanaka', '«Pinggan sudah dicuci?»'),
        ('Aini', '«Belum. Pejabat ditutup pada pukul enam.»'),
        ('Tanaka', '«Pinggan saya bawa ke dapur.»'),
        ('Aini', '«Terima kasih, Encik Tanaka.»'),
        ('Tanaka', '«Sama-sama.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c09-g02', 'ms-c09-g03', 'ms-c09-g04', 'ms-c09-g05', 'ms-c09-g06'],
        patterns=['ms-c09-f01', 'ms-c09-f02', 'ms-c09-f03', 'ms-c09-f04', 'ms-c09-f05'],
        goal='Read signs and notices, and say what was done and by whom with the passive «di-».',
        explain=('第9章速習：45分で基本の20語、«di-» の受け身と «oleh»、«sudah»・«belum» ＋ «di-»、«dibuka»・«ditutup» ＋ «pada pukul»、«Dilarang …»・«Sila …» を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 9 in one 45-minute session: 20 core words, the passive «di-» and «oleh», «sudah» / «belum» + a «di-» verb, «dibuka» / «ditutup» + «pada pukul», «Dilarang …» and «Sila …»; then self-study in Kata-Kata. All names, notices and times are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say what was done with a «di-» verb and say who did it with «oleh». / «di-» の動詞で「されたこと」を言い、«oleh» で誰がしたかを言える。',
                'I can say a thing is «sudah» or «belum» done. / «sudah»・«belum» でもう・まだを言える。',
                'I can say when a shop or office is «dibuka» or «ditutup» with «pada pukul». / «pada pukul» で店や事務所の開く・閉まる時刻を言える。',
                'I can read «Dilarang …» and «Sila …» on signs and notices. / 掲示の «Dilarang …»・«Sila …» が読める。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C9_WORDS) +
             ['The full unit also teaches the other «di-» verbs («dijual», «dibaca», «ditulis», «diambil», «dipanggil», «dimasak», «dicuci», «disewa»), the sign «Dilarang merokok» (to recognise only), the door signs «TOLAK» and «TARIK», the notice words «PERHATIAN» and «hingga», the greeting «Selamat Pesta Kaamatan», the general «rumah terbuka» scene with a note for each festival, and 14 idioms to recognise.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · ___ «dibuat oleh» ___.  e.g. «Kek ini dibuat oleh isteri saya.» / «Kek ini dibuat oleh siapa?»',
                '2 · ___ «di-»(verb) «di» ___.  e.g. «Nasi lemak ini dibeli di gerai.» / «Dibeli di mana?»',
                '3 · ___ «sudah» / «belum» «di-»(verb).  e.g. «Teh tarik sudah diminum.» / «Harga belum dibayar.»',
                '4 · «Kedai ini» «dibuka» / «ditutup» «pada» «pukul» ___.  e.g. «Pejabat dibuka pada pukul sembilan.» / «Pejabat ditutup pada pukul enam.»',
                '5 · «Dilarang» ___. / «Sila» ___.  e.g. «Dilarang masuk.» / «Sila masuk.»',
                'Remember: a «di-» verb is the root with «di-» in front, and the thing comes first. You can make one from any root verb you know: «digoreng», «dipilih». If you did it yourself, drop «di-» and put the doer in front of the verb: «Pinggan saya bawa ke dapur.» A sign leaves out the doer.',
                '«di-» の動詞は語根の前に «di-» を付けた形で、物が先に来ます。知っている動詞の語根なら何にでも付けられます：«digoreng»・«dipilih»。自分でするときは «di-» をはずして、動作主を動詞の前に置きます：«Pinggan saya bawa ke dapur.» 掲示は動作主を言いません。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You organise an office «jamuan» (fictional). The cake was made by Mei Ling, the «nasi lemak» was bought by Rahman, the «teh tarik» was brought by Tanaka and the plates are not washed yet. Answer B in the passive.',
                'B: You are a guest. Ask who made the cake, where the «nasi lemak» was bought, who brought the «teh tarik» and whether the plates are washed.',
                'Change of plan: A says «Maaf, teh tarik belum dibuat. Pejabat ditutup pada pukul enam.» B asks about the time and offers to buy it.',
                'A：事務所の «jamuan»（架空）の幹事で、ケーキはメイリンが作り、«nasi lemak» はラーマンが買い、«teh tarik» は田中さんが持ってきて、お皿はまだ洗っていません。受け身で答えます。B：客として、ケーキ・«nasi lemak»・«teh tarik»・お皿について受け身でたずねます。変更：Aが «Maaf, teh tarik belum dibuat. Pejabat ditutup pada pukul enam.» と言い、Bは時刻をたずねて、買ってくると申し出ます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "This cake was made by my wife.": ____________________',
                '☐ 2. Ask "Who made this cake?": ____________________',
                '☐ 3. Say "The tea has been drunk.": ____________________',
                '☐ 4. Say "The office is closed at six.": ____________________',
                '☐ 5. Read the sign "No entry.": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c09 ({sedia_cards(9)} cards, frames ms-c09-f01 and ms-c09-f02).',
                f'After the session: all {pack_cards(9)} Kata-Kata chapter 9 cards (ms-c09-001 to ms-c09-{last_card(9):03}; ms-c09-028 «pinggan» was merged into ms-c08-016) and frames ms-c09-f01 to ms-c09-f06 in the frame drill and Susun Ayat; the Kata-Kata scenario "The office «jamuan»" matches this pack.',
                'Dunia scenes (recognise only): "Rumah terbuka" (19 words, a general open house with festival words) and "Simpulan bahasa harian" (14 idioms; never drilled).',
                'Optional full-course Cikgu Sensai unit: unit 9 (the passive «di-», signs and notices), with a culture note for each festival. The stage review and the A1 test come next and wait for Sam.',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure). Hanashishou starts at A2.',
                '授業後：第9章のカードと Dunia の場面を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Kek ini dibuat oleh isteri saya.» 2 «Kek ini dibuat oleh siapa?» 3 «Teh tarik sudah diminum.» '
             '4 «Pejabat ditutup pada pukul enam.» 5 «Dilarang masuk.»',
             'Session plan (45 min): 0–5 recall chapter 8 (order at a «gerai»); 5–15 core words by theme; 15–25 patterns 1 to 5; '
             '25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 9. All Japanese is a draft awaiting native review.'])]


PACKS.append(dict(
    chapter_id='ms-c09', check_unit='ms-c09-fast', id_prefix='ms-c09-fast',
    title_prefix='Chapter 9', header='Chapter 9 fast course (ms-c09)',
    menu_title='Chapter 9 · Passive di-', genre='Social life',
    course_path='fast', prerequisites=['ms-c01', 'ms-c02', 'ms-c03', 'ms-c04', 'ms-c05', 'ms-c06', 'ms-c07', 'ms-c08'], prerequisite_units=[],
    prereq_grammar=['ms-c03-g04', 'ms-c04-g06', 'ms-c05-g06'],
    word_scope=C9_WORDS, components=chapter9))


# Stage 2 (A2) fast packs: one 45-minute pack per chapter, from chapter 10 (plan section 1, "Fast course").
STAGE2_PACKS = []

C10_WORDS = ['L-1089', 'L-1091', 'L-1093', 'L-1094', 'L-1095', 'L-1098', 'L-1101', 'L-1102', 'L-1103', 'L-1106',
             'L-1110', 'L-1108', 'L-1112', 'L-1114', 'L-1122', 'L-0660', 'L-0779', 'L-0781', 'L-1118', 'L-1115']


def chapter10(ledger):
    dialogue = [
        ('Siti', '«Selamat petang. Encik jiran baru, ya?»'),
        ('Tanaka', '«Ya, saya baru berpindah minggu lepas. Saya berasal dari Osaka.»'),
        ('Siti', '«Selamat berkenalan! Saya Siti. Encik bekerja di mana?»'),
        ('Tanaka', '«Saya bekerja di sebuah syarikat Jepun di Kuala Lumpur.»'),
        ('Siti', '«Pukul berapa encik bertolak ke pejabat?»'),
        ('Tanaka', '«Setiap pagi saya bertolak pukul tujuh. Saya bersarapan di kedai mamak.»'),
        ('Siti', '«Pada hujung minggu encik buat apa?»'),
        ('Tanaka', '«Saya suka berenang. Puan pula?»'),
        ('Siti', '«Saya suka berehat di rumah. Pada hari Ahad, kami berkumpul di rumah saya. Encik datang, ya!»'),
        ('Tanaka', '«Terima kasih! Nanti kita berbual lagi.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c10-g02', 'ms-c10-g03', 'ms-c10-g04', 'ms-c10-g05', 'ms-c10-g06', 'ms-c10-g07', 'ms-c10-g08'],
        patterns=['ms-c10-f01', 'ms-c10-f02', 'ms-c10-f03', 'ms-c10-f05', 'ms-c10-f06'],
        goal='Describe a working day and your background with ber- verbs, and meet a new neighbour.',
        explain=('第10章速習：45分で基本の20語、ber- の動詞（つづりは ‹be-›・‹bel-› だけ）、日課と時刻、週末にすること、出身・仕事・人生のできごと '
                 '«sudah»・«belum» を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 10 in one 45-minute session: 20 core words, ber- verbs (spelling variants ‹be-› and ‹bel-› only), a routine with times, '
                 'weekend activities, background and life events with «sudah» / «belum»; then self-study in Kata-Kata. All names and details are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say when I do things on a working day with ber- verbs and «pukul». / ber- の動詞と «pukul» で、仕事の日にいつ何をするかを言える。',
                'I can ask what time something starts or when we set off. / 何時に始まるか、何時に出発するかをたずねられる。',
                'I can give my background with «berasal dari» and «bekerja di». / «berasal dari»・«bekerja di» で自分の背景を言える。',
                'I can introduce myself to a new neighbour and accept an invitation. / 新しい隣人に自己紹介し、招待を受けられる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C10_WORDS) +
             ['The full course also teaches «berjalan», «bermain», «berlari», «berbasikal», «berbual», «beratur», «bersiap», «bersedia», «berlatih», '
              '«rutin», «bernama», «berumur», «berkeluarga», «berkawan», «berniaga», «berbelanja», «berminat», «berpakaian», «sepupu», '
              '«pengalaman», and «pindah» as the spoken form of «berpindah» (to recognise only).'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Setiap pagi saya» (ber- verb) «pukul» ___.  e.g. «Setiap pagi saya bersarapan pukul tujuh.» / «Setiap pagi saya bertolak pukul tujuh setengah.»',
                '2 · «Pukul berapa» ___ «bermula» / «kita bertolak»?  e.g. «Pukul berapa mesyuarat bermula?» / «Pukul berapa kita bertolak?»',
                '3 · «Pada hujung minggu saya suka» (ber- verb).  e.g. «Pada hujung minggu saya suka berenang.» / «Saya suka bermain badminton.»',
                '4 · «Saya berasal dari» ___. «Saya bekerja di» ___.  e.g. «Saya berasal dari Osaka.» / «Saya bekerja di Kuala Lumpur.»',
                '5 · «Saya sudah / belum» (ber- verb).  e.g. «Saya sudah berkahwin.» / «Saya belum berkenalan dengan jiran.»',
                'Remember: ‹ber-› has no nasal sound changes; it is spelt ‹be-› before r and in «bekerja», and ‹bel-› only in «belajar». A ber- verb '
                'never changes; the markers do the work. «bertolak» is set off (not push); «berhenti kerja» is quit a job. In speech you will hear '
                'the root («kerja», «sarapan», «pindah»); write the ‹ber-› form.',
                '‹ber-› には鼻音の変化がなく、r の前と «bekerja» で ‹be-›、«belajar» だけ ‹bel-› になります。ber- の動詞は形が変わらず、マーカーが時を表します。'
                '«bertolak» は「出発する」（「押す」ではない）、«berhenti kerja» は「仕事を辞める」です。話し言葉では語根（«kerja»・«sarapan»・«pindah»）も聞きますが、'
                '書くときは ‹ber-› の形を使います。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You have just moved into a condominium (a real or invented persona). Introduce yourself, say where you work and when you set off in the morning.',
                'B: You are a neighbour. Ask where A is from and what A does at the weekend, say one thing about yourself, and invite A to a gathering on Sunday.',
                'Change of plan: B says «Maaf, hari Ahad saya bercuti. Kita berkumpul hari Sabtu, ya?» A asks the time.',
                'A：コンドミニアムに引っ越してきたばかりです（本人か架空の人物）。自己紹介し、勤め先と朝の出発時刻を言います。B：隣人として、Aの出身と週末にすることをたずね、'
                '自分のことを一つ話し、日曜日の集まりに招きます。変更：Bが «Maaf, hari Ahad saya bercuti. Kita berkumpul hari Sabtu, ya?» と言い、Aは時刻をたずねます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "Every morning I set off at seven.": ____________________',
                '☐ 2. Ask "What time does the meeting start?": ____________________',
                '☐ 3. Say "I am from Osaka.": ____________________',
                '☐ 4. Say "I have just moved here.": ____________________',
                '☐ 5. Answer "not yet" to «Sudah berkahwin?»: ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c10 ({sedia_cards(10)} cards, frames ms-c10-f01 and ms-c10-f02).',
                f'After the session: all {pack_cards(10)} Kata-Kata chapter 10 cards (ms-c10-001 to ms-c10-{last_card(10):03}; ms-c10-041 «pindah» '
                'is recognise only) and frames ms-c10-f01 to ms-c10-f06 in the frame drill and Susun Ayat; the Kata-Kata scenario "A working day and '
                'a new neighbour" matches this pack.',
                'No Dunia scene primes chapter 10. Hanashishou scenes for chapter 10 (grab_ride_chat, new_neighbour) are not yet tagged by chapter, '
                'so they are not assigned yet.',
                'Optional full-course Cikgu Sensai units: unit 10A (the working day) and unit 10B (background and neighbours), with a writing block.',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure).',
                '授業後：第10章のカードと文型を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Setiap pagi saya bertolak pukul tujuh.» 2 «Pukul berapa mesyuarat bermula?» 3 «Saya berasal dari Osaka.» '
             '4 «Saya baru berpindah ke sini.» 5 «Belum.» (or «Saya belum berkahwin.»)',
             'Session plan (45 min): 0–5 recall chapter 9 (the door signs; «tolak» before «bertolak»); 5–15 core words with their roots; '
             '15–25 patterns 1 to 5; 25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as units 10A and 10B. Personal details are optional. All Japanese is a draft awaiting native review.'])]


STAGE2_PACKS.append(dict(
    chapter_id='ms-c10', check_unit='ms-c10-fast', id_prefix='ms-c10-fast', level='A2',
    title_prefix='Chapter 10', header='Chapter 10 fast course (ms-c10)',
    menu_title='Chapter 10 · ber- verbs', genre='Daily routines',
    course_path='fast', prerequisites=[f'ms-c{k:02}' for k in range(1, 10)], prerequisite_units=[],
    prereq_grammar=['ms-c02-g08', 'ms-c04-g06', 'ms-c04-g08'],
    word_scope=C10_WORDS, components=chapter10))


C11_WORDS = ['L-1124', 'L-1125', 'L-1123', 'L-1126', 'L-1127', 'L-1129', 'L-1132', 'L-1133', 'L-1136', 'L-1137',
             'L-1141', 'L-1138', 'L-0819', 'L-0865', 'L-1155', 'L-1156', 'L-1146', 'L-1143', 'L-1150', 'L-1152']


def chapter11(ledger):
    dialogue = [
        ('Tanaka', '«Puan Aini, emel dari Jepun itu sudah dibaca?»'),
        ('Aini', '«Sudah. Saya membaca emel itu pagi tadi, kemudian saya menghantar fail itu.»'),
        ('Tanaka', '«Oh, Encik Rahman yang menerima fail itu?»'),
        ('Aini', '«Ya. Sekarang dia sedang membuka fail itu.»'),
        ('Tanaka', '«Cik Mei Ling, draf slaid itu sudah siap?»'),
        ('Mei Ling', '«Belum. Saya masih menyemak draf itu. Tarikh akhir hari Jumaat, ya?»'),
        ('Tanaka', '«Ya, hari Jumaat. Tolong semak sekali lagi.»'),
        ('Mei Ling', '«Baik. Nanti saya menghantar mesej. Hujung minggu ini encik buat apa?»'),
        ('Tanaka', '«Saya mahu memasak. Isteri saya mengajar saya memasak nasi lemak.»'),
        ('Mei Ling', '«Wah, bagus! Saya mahu mendaki dengan kawan saya. Boleh saya mengecas telefon saya di sini?»'),
        ('Tanaka', '«Boleh. Mari kita minum kopi. Saya yang membayar.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c11-g02', 'ms-c11-g03', 'ms-c11-g04', 'ms-c11-g05', 'ms-c11-g06', 'ms-c11-g07', 'ms-c11-g08'],
        patterns=['ms-c11-f01', 'ms-c11-f02', 'ms-c11-f03', 'ms-c11-f04', 'ms-c11-f06'],
        goal='Say who did what at the office with meN- verbs, check a draft, and say your weekend plan.',
        explain=('第11章速習：45分で基本の20語、meN- の動詞（語根・つづりの変化・«di-» の相手）、「誰が」の質問、依頼 «Tolong semak …»、週末の予定 «mahu» を練習し、'
                 '残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 11 in one 45-minute session: 20 core words, meN- verbs (the root, the spelling change and the «di-» partner), the question «Siapa yang …?», '
                 'the request «Tolong semak …» and weekend plans with «mahu»; then self-study in Kata-Kata. All names and details are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say who did what with a meN- verb and its «di-» partner. / meN- の動詞とその «di-» の相手で、誰が何をしたかを言える。',
                'I can ask who sent or received a file. / 誰がファイルを送ったか、受け取ったかをたずねられる。',
                'I can ask a colleague to check a draft. / 同僚に下書きの確認を頼める。',
                'I can say what I want to do this weekend. / 今週末にしたいことを言える。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C11_WORDS) +
             ['The full course also teaches «membuat», «menutup», «membawa», «mencuci», «memanggil», «melihat», «mendengar», «menjual», «menyimpan», «melancong», '
              '«menukar», «memilih», «meminjam», «menolong», «mengisi», «semak», «mesej», «draf», «slaid», «tarikh akhir», «rancangan», and «tukar» and «deadline» '
              'as spoken forms (to recognise only).'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Aini» ___ «buku itu.»  e.g. «Puan Aini membaca emel itu.» / «Encik Rahman menerima fail itu.»',
                '2 · «Buku itu» («di-» verb) «oleh Aini.»  e.g. «Emel itu dibaca oleh Puan Aini.» / «Fail itu dihantar oleh Puan Aini.»',
                '3 · «Siapa yang» ___ «fail itu?»  e.g. «Siapa yang menghantar fail itu?» / «Puan Aini yang menghantar fail itu.»',
                '4 · «Tolong semak» ___ «ini.»  e.g. «Tolong semak draf ini.» / «Tolong semak slaid ini.»',
                '5 · «Hujung minggu ini saya mahu» ___.  e.g. «Hujung minggu ini saya mahu mendaki.» / «Hujung minggu ini saya mahu memasak.»',
                'Remember: a meN- verb is a root with ‹meN-› in front, and the first sound of the root decides the front: ‹mem-› before b; t, p, s and k drop; ‹meng-› before h or a '
                'vowel; ‹men-› before c, d and j; ‹me-› before l, m, n, r, w and y; ‹menge-› before a one-syllable root («cas» → «mengecas»). A request takes the plain root '
                '(«Tolong semak …»), not the meN- form. In speech you will hear the root alone («baca», «tukar»); say the meN- form.',
                'meN- の動詞は語根の前に ‹meN-› を付けた形で、語根の最初の音で前の部分が決まります：b の前は ‹mem-›、t・p・s・k は落ちる、h か母音の前は ‹meng-›、c・d・j の前は ‹men-›、'
                'l・m・n・r・w・y の前は ‹me-›、一音節の語根は ‹menge-› です（«cas» → «mengecas»）。依頼は meN- の形ではなく語根をそのまま使います（«Tolong semak …»）。'
                '話し言葉では語根だけも聞きますが、言うときは meN- の形を使います。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are a colleague who knows the morning (fictional): Aini read the email, Mei Ling checked the draft, Rahman sent the reply. Answer B with the doer first.',
                'B: You were out. Ask A who read the email, who checked the draft and who sent the reply, ask A to check one thing, and ask what A wants to do at the weekend.',
                'Change of plan: A says «Maaf, bukan Encik Rahman. Puan Aini yang menghantar jawapan itu.» B corrects the report with the «di-» form.',
                'A：今朝のことを知っている同僚です（架空）：アイニさんがメールを読み、メイリンさんが下書きを確認し、ラーマンさんが返事を送りました。Bに動作主を先にして答えます。'
                'B：席を外していました。誰がメールを読み、下書きを確認し、返事を送ったかをたずね、確認してほしいことを一つ頼み、週末にしたいことをたずねます。'
                '変更：Aが «Maaf, bukan Encik Rahman. Puan Aini yang menghantar jawapan itu.» と言い、Bは «di-» の形で報告を直します。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "Aini reads the email.": ____________________',
                '☐ 2. Say "The email is read by Aini.": ____________________',
                '☐ 3. Ask "Who sent the file?": ____________________',
                '☐ 4. Say "Please check this draft.": ____________________',
                '☐ 5. Say "This weekend I want to go hiking.": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c11 ({sedia_cards(11)} cards, frames ms-c11-f01 and ms-c11-f02).',
                f'After the session: all {pack_cards(11)} Kata-Kata chapter 11 cards (ms-c11-001 to ms-c11-{last_card(11):03}; ms-c11-042 «tukar» and ms-c11-043 «deadline» '
                'are recognise only) and frames ms-c11-f01 to ms-c11-f06 in the frame drill and Susun Ayat; the Kata-Kata scenario "Who did what in the office" '
                'matches this pack.',
                'No Dunia scene primes chapter 11. The Hanashishou office scene for chapter 11 (report_deadline) is not yet tagged by chapter, so it is not assigned yet.',
                'Optional full-course Cikgu Sensai units: unit 11A (who did what at the office) and unit 11B (the draft, the deadline and the weekend), with a review block.',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure).',
                '授業後：第11章のカードと文型を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Puan Aini membaca emel itu.» 2 «Emel itu dibaca oleh Puan Aini.» 3 «Siapa yang menghantar fail itu?» '
             '4 «Tolong semak draf ini.» 5 «Hujung minggu ini saya mahu mendaki.»',
             'Session plan (45 min): 0–5 recall chapter 10 (ber- verbs have no object) and chapter 9 («dibaca», «dihantar»); 5–15 core words with their roots; '
             '15–25 patterns 1 to 5; 25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as units 11A and 11B. All Japanese is a draft awaiting native review.'])]


STAGE2_PACKS.append(dict(
    chapter_id='ms-c11', check_unit='ms-c11-fast', id_prefix='ms-c11-fast', level='A2',
    title_prefix='Chapter 11', header='Chapter 11 fast course (ms-c11)',
    menu_title='Chapter 11 · meN- verbs', genre='Work',
    course_path='fast', prerequisites=[f'ms-c{k:02}' for k in range(1, 11)], prerequisite_units=[],
    prereq_grammar=['ms-c09-g02', 'ms-c04-g06', 'ms-c10-g02'],
    word_scope=C11_WORDS, components=chapter11))


C12_WORDS = ['L-1157', 'L-1158', 'L-1159', 'L-1161', 'L-1162', 'L-1164', 'L-1167', 'L-0595', 'L-0658', 'L-0654',
             'L-1168', 'L-1172', 'L-0651', 'L-0649', 'L-0652', 'L-1174', 'L-1175', 'L-1180', 'L-1181', 'L-0655']


def chapter12(ledger):
    dialogue = [
        ('Tanaka', '«Selamat petang. Saya mahu ambil bungkusan. Sudah sampai?»'),
        ('Guard', '«Sudah, encik. Unit berapa?»'),
        ('Tanaka', '«Blok B, unit 12-3.»'),
        ('Guard', '«Ada dua bungkusan. Boleh tunjukkan mesej itu?»'),
        ('Tanaka', '«Boleh. Nombor penjejakan ada dalam mesej ini.»'),
        ('Guard', '«Bungkusan kecil itu bukan untuk encik. Label ini koyak.»'),
        ('Tanaka', '«Oh, bukan untuk saya. Tolong simpankan bungkusan kecil itu di pondok pengawal.»'),
        ('Guard', '«Baik, encik.»'),
        ('Tanaka', '«Selamat pagi. Ada kebocoran di siling bilik air saya.»'),
        ('Office', '«Tolong matikan lampu itu dulu. Kami akan menghubungi juruteknik.»'),
        ('Tanaka', '«Baik, saya matikan lampu itu sekarang. Bila juruteknik boleh datang?»'),
        ('Office', '«Ada slot petang ini, pukul tiga. Boleh?»'),
        ('Tanaka', '«Boleh. Tolong hubungi saya sebelum juruteknik sampai.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c12-g02', 'ms-c12-g03', 'ms-c12-g04', 'ms-c12-g05', 'ms-c12-g06', 'ms-c12-g07', 'ms-c12-g08'],
        patterns=['ms-c12-f01', 'ms-c12-f02', 'ms-c12-f03', 'ms-c12-f04', 'ms-c12-f05', 'ms-c12-f06'],
        goal='Ask for a favour with a -kan verb, collect a parcel, and report a leak and ask for a repair.',
        explain=('第12章速習：45分で基本の20語、‹-kan› と ‹-i› の動詞（語根・接尾辞の働き・つづり）、依頼 «Tolong simpankan …»、荷物の受け取り、水漏れの連絡 «Ada kebocoran di … saya» を練習し、'
                 '残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 12 in one 45-minute session: 20 core words, the ‹-kan› and ‹-i› verbs (the root, what the suffix adds and the spelling), the request «Tolong simpankan …», '
                 'collecting a parcel and reporting a leak; then self-study in Kata-Kata. All names and details are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can ask a guard to keep, bring or show something with a ‹-kan› verb. / ‹-kan› の動詞で守衛さんに預かる・持ってくる・見せるよう頼める。',
                'I can collect a parcel and read a parcel label. / 荷物を受け取り、荷物のラベルを読める。',
                'I can report a leak to the management office. / 管理事務所に水漏れを連絡できる。',
                'I can ask the office to contact me and say that a technician is repairing something. / 事務所に連絡を頼み、技術者が修理中だと言える。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C12_WORDS) +
             ['The full course also teaches «bukakan», «belikan», «pulangkan», «berikan», «pastikan», «pemilik», «pejabat pengurusan», «blok», «penerima», «nombor penjejakan», «lobi», '
              '«baiki», «menghubungi», «ganti», «gantikan», «isikan», «kosongkan», «hidupkan», «perlahankan», «kerosakan», «aduan», «kontraktor», «paip», «tempahan», and «nombor tracking» '
              'as a spoken form (to recognise only).'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Tolong» ___ «bungkusan ini.»  e.g. «Tolong simpankan bungkusan ini.» / «Tolong hantarkan bungkusan itu.»',
                '2 · «Boleh» ___ «mesej itu?»  e.g. «Boleh tunjukkan mesej itu?» / «Boleh bawakan beg saya?»',
                '3 · «Saya mahu ambil» ___.  e.g. «Saya mahu ambil bungkusan.» / «Boleh ambilkan bungkusan saya?»',
                '4 · «Boleh hubungi» ___ «?»  e.g. «Boleh hubungi juruteknik?» / «Juruteknik sedang membaiki paip.»',
                '5 · «Ada kebocoran di» ___ «saya.»  e.g. «Ada kebocoran di siling saya.» / «Tolong matikan lampu itu dulu.»',
                'Remember: ‹-kan› on a root means do it for someone or make it happen («simpan» → «simpankan», ‹mati› → «matikan»); ‹-i› points at a person or place («hubungi»). '
                'Two k in «letakkan» and «tunjukkan»; «berikan» is ‹beri› + ‹-kan›, not ‹ber-› + «ikan»; «bersihkan» is «bersih» + ‹-kan›. In speech you will hear the root alone («simpan», «tutup»); say the ‹-kan› form. After «sudah», «sedang», «belum» or «akan», or with a third-person doer, use the meN- verb: «menyimpan», «menghantar».',
                '‹-kan› は語根に付いて「誰かのためにする」「そうなるようにする」を表し（«simpan» → «simpankan»、‹mati› → «matikan»）、‹-i› は人や場所へ向かう動作です（«hubungi»）。'
                '«letakkan» と «tunjukkan» は k が二つで、«berikan» は ‹beri› ＋ ‹-kan›（‹ber-› ＋ «ikan» ではありません）、«bersihkan» は «bersih» ＋ ‹-kan› です。'
                '話し言葉では語根だけも聞きますが、言うときは ‹-kan› の形を使います。«sudah»・«sedang»・«belum»・«akan» のあと、または三人称の動作主のときは meN- の動詞（«menyimpan»・«menghantar»）を使います。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are the guard or the office (fictional). Two parcels are in the guardhouse; the small one has a torn label. Later the resident reports a leak.',
                'B: You are the resident. Collect your parcel, ask the guard to keep the small one, then report a leak in your ceiling, switch off the light and ask to be contacted.',
                'Change of plan: A says «Maaf, juruteknik datang pukul dua, bukan pukul tiga.» B agrees and asks to be contacted before the technician arrives.',
                'A：守衛または管理事務所の担当です（架空）。守衛所に荷物が二つあり、小さい方はラベルが破れています。あとで住民が水漏れを連絡します。'
                'B：住民です。荷物を受け取り、小さい荷物を預かってもらい、天井の水漏れを連絡し、電灯を消し、連絡を頼みます。'
                '変更：Aが «Maaf, juruteknik datang pukul dua, bukan pukul tiga.» と言い、Bは了承して技術者が着く前の連絡を頼みます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "Please keep this parcel.": ____________________',
                '☐ 2. Say "Can you show me the message?": ____________________',
                '☐ 3. Say "Can you contact the technician?": ____________________',
                '☐ 4. Say "There is a leak in my ceiling.": ____________________',
                '☐ 5. Say "Please switch that light off first.": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c12 ({sedia_cards(12)} cards, frames ms-c12-f01 and ms-c12-f02).',
                f'After the session: all {pack_cards(12)} Kata-Kata chapter 12 cards (ms-c12-001 to ms-c12-{last_card(12):03}; ms-c12-024 «nombor tracking» '
                'is recognise only) and frames ms-c12-f01 to ms-c12-f06 in the frame drill and Susun Ayat; the Kata-Kata scenario "Parcels and a leak" '
                'matches this pack.',
                'No Dunia scene primes chapter 12. The Hanashishou home-condo scenes for chapter 12 are not yet tagged by chapter, so they are not assigned yet.',
                'Optional full-course Cikgu Sensai units: unit 12A (parcels and ‹-kan› requests, with a writing block) and unit 12B (the leak and the repair, with a review block).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure).',
                '授業後：第12章のカードと文型を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Tolong simpankan bungkusan ini.» 2 «Boleh tunjukkan mesej itu?» 3 «Boleh hubungi juruteknik?» '
             '4 «Ada kebocoran di siling saya.» 5 «Tolong matikan lampu itu dulu.»',
             'Session plan (45 min): 0–5 recall chapter 11 (meN- verbs) and the request «Tolong» + root; 5–15 core words with their roots; '
             '15–25 patterns 1 to 5; 25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as units 12A and 12B. All Japanese is a draft awaiting native review.'])]


STAGE2_PACKS.append(dict(
    chapter_id='ms-c12', check_unit='ms-c12-fast', id_prefix='ms-c12-fast', level='A2',
    title_prefix='Chapter 12', header='Chapter 12 fast course (ms-c12)',
    menu_title='Chapter 12 · -kan and -i verbs', genre='Housing',
    course_path='fast', prerequisites=[f'ms-c{k:02}' for k in range(1, 12)], prerequisite_units=[],
    prereq_grammar=['ms-c11-g02', 'ms-c11-g06', 'ms-c08-g02'],
    word_scope=C12_WORDS, components=chapter12))


C13_WORDS = ['L-1185', 'L-1186', 'L-1199', 'L-1187', 'L-1188', 'L-1189', 'L-1190', 'L-1196', 'L-0627', 'L-0630',
             'L-0638', 'L-0648', 'L-1268', 'L-1200', 'L-0631', 'L-0633', 'L-1191', 'L-1193', 'L-1192', 'L-0636']


def chapter13(ledger):
    dialogue = [
        ('Receptionist', '«Selamat pagi, encik. Ada temu janji?»'),
        ('Tanaka', '«Tidak ada. Saya demam dan sakit tekak. Saya batuk juga.»'),
        ('Receptionist', '«Encik perlu daftar dulu. Sila isi borang ini.»'),
        ('Tanaka', '«Baik. Saya belum isi borang. Bolehkah saya isi borang di sini?»'),
        ('Receptionist', '«Boleh. Ini klinik panel syarikat encik?»'),
        ('Tanaka', '«Ya. Boleh saya minum air di sini?»'),
        ('Receptionist', '«Maaf, tidak dibenarkan minum di sini. Dilarang makan dan minum di bilik menunggu.»'),
        ('Tanaka', '«Baik, saya faham. Terima kasih.»'),
        ('Doctor', '«Encik patut berehat di rumah. Encik tidak perlu datang ke pejabat esok.»'),
        ('Tanaka', '«Doktor, boleh saya minta cuti sakit untuk esok?»'),
        ('Doctor', '«Boleh. Saya berikan cuti sakit satu hari.»'),
        ('Tanaka', '«Maaf, boleh cakap lagi sekali? Saya tidak faham arahan itu.»'),
        ('Pharmacist', '«Boleh. Encik mesti baca arahan di label. Dos ada di label itu.»'),
        ('Pharmacist', '«Kalau ada soalan, tanya saya lagi.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c13-g02', 'ms-c13-g03', 'ms-c13-g04', 'ms-c13-g05', 'ms-c13-g06', 'ms-c13-g07', 'ms-c13-g08'],
        patterns=['ms-c13-f01', 'ms-c13-f02', 'ms-c13-f03', 'ms-c13-f04', 'ms-c13-f05', 'ms-c13-f06'],
        goal='Say what you have not done yet, ask permission, say what you need, and read advice and rules at a clinic and a pharmacy.',
        explain=('第13章速習：45分で基本の20語、«belum»・«Bolehkah saya …?»・«perlu»・«patut»・«mesti»・«wajib»、掲示の «tidak dibenarkan»・«dilarang»、パネルクリニックと薬局の場面を練習し、'
                 '残りは Kata-Kata で自習します。日本語は未監修です。このパックは医学的な助言をしません。',
                 'Chapter 13 in one 45-minute session: 20 core words, «belum», «Bolehkah saya …?», «perlu», «patut», «mesti» and «wajib», the signs «tidak dibenarkan» and «dilarang», and the panel clinic and pharmacy scene; '
                 'then self-study in Kata-Kata. All names and details are fictional and the pack gives no medical advice.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say what I have not done yet with «belum». / «belum» でまだしていないことを言える。',
                'I can ask permission with «Bolehkah saya …?». / «Bolehkah saya …?» で許可を求められる。',
                'I can say what I need («perlu»), and tell advice («patut») from a must («mesti», «wajib»). / «perlu» で必要なことを言い、助言（«patut»）と義務（«mesti»・«wajib»）を区別できる。',
                'I can read «tidak dibenarkan» and «dilarang» on a sign and ask a pharmacist to say an instruction once more. / 掲示の «tidak dibenarkan»・«dilarang» が読め、薬剤師に指示をもう一度言ってもらえる。'], 'opener'),
            ('Core words · 基本の20語', core(ledger, C13_WORDS) +
             ['The full course also teaches «sesuai», «simptom», «kesihatan», «rawatan» and «kecemasan», with the revision words of the whole unit.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Saya belum» ___ «.»  e.g. «Saya belum makan.» / «Saya belum mendaftar.»',
                '2 · «Bolehkah saya» ___ «?»  e.g. «Bolehkah saya masuk?» / «Boleh saya duduk di sini?»',
                '3 · «Saya perlu» ___ «.»  e.g. «Saya perlu berjumpa doktor.» / «Encik perlu daftar dulu.»',
                '4 · «Encik patut» ___ «.»  e.g. «Encik patut berehat.» / «Encik mesti baca arahan di label.»',
                '5 · «Tidak dibenarkan» ___ «di sini.»  e.g. «Tidak dibenarkan minum di sini.» / «Borang ini wajib diisi.»',
                'Remember: «belum» is not yet, «tidak» is not; «perlu» is a step you take, «patut» is advice and «mesti» or «wajib» is a must; «tidak perlu» is not having to and «tidak boleh» is not allowed. '
                'On a sign you read «tidak dibenarkan» or «dilarang»; in speech you say «tidak boleh». For your health follow your own doctor and pharmacist.',
                '«belum» は「まだ〜ていない」、«tidak» は「〜ない」。«perlu» は手順、«patut» は助言、«mesti»・«wajib» は義務。«tidak perlu» は「しなくてよい」、«tidak boleh» は「してはいけない」。'
                '掲示では «tidak dibenarkan»・«dilarang»、話し言葉では «tidak boleh» です。健康については自分の医者と薬剤師の指示に従ってください。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You are the receptionist, and later the pharmacist (fictional). The patient has no appointment and has not registered. Never name a medicine, a dose or a time to take it: point to the label.',
                'B: You are the patient. Register, ask permission twice, say what you need, and ask the pharmacist to say an instruction once more.',
                'Change of plan: A says «Maaf, doktor belum ada. Encik boleh tunggu, atau datang pukul empat. Sesuai?» B decides and says the time suits.',
                'A：受付係で、あとで薬剤師にもなります（架空）。患者は予約がなく、まだ受付をしていません。薬の名前・用量・飲む時間は言わず、ラベルを指します。'
                'B：患者です。受付をし、許可を二回たずね、必要なことを言い、薬剤師に指示をもう一度言ってもらいます。'
                '変更：Aが «Maaf, doktor belum ada. Encik boleh tunggu, atau datang pukul empat. Sesuai?» と言い、Bは決めて、その時間でよいと言います。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "I haven\'t registered yet.": ____________________',
                '☐ 2. Say "May I come in?": ____________________',
                '☐ 3. Say "I need to see a doctor.": ____________________',
                '☐ 4. Say "You should rest." to a man: ____________________',
                '☐ 5. Write the sign "Drinking is not allowed here.": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c13 ({sedia_cards(13)} cards, frames ms-c13-f01 and ms-c13-f02).',
                f'After the session: all {pack_cards(13)} Kata-Kata chapter 13 cards (ms-c13-001 to ms-c13-{last_card(13):03}) and frames ms-c13-f01 to ms-c13-f06 in the frame drill and Susun Ayat; '
                'the Kata-Kata scenario "At the clinic and the pharmacy" matches this pack.',
                'No Dunia scene primes chapter 13. The Hanashishou clinic scenes for chapter 13 are not yet tagged by chapter, so they are not assigned yet.',
                'Optional full-course Cikgu Sensai unit: unit 13 (the panel clinic and the pharmacy).',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure).',
                '授業後：第13章のカードと文型を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Saya belum mendaftar.» 2 «Bolehkah saya masuk?» 3 «Saya perlu berjumpa doktor.» '
             '4 «Encik patut berehat.» 5 «Tidak dibenarkan minum di sini.» (or «Dilarang minum di sini.»)',
             'Session plan (45 min): 0–5 recall chapters 2 and 12 («Boleh …?», «Tolong» + a request); 5–15 core words; '
             '15–25 patterns 1 to 5; 25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 13. The pack and the unit give no diagnosis, no treatment advice and no dosing instruction. All Japanese is a draft awaiting native review.'])]


STAGE2_PACKS.append(dict(
    chapter_id='ms-c13', check_unit='ms-c13-fast', id_prefix='ms-c13-fast', level='A2',
    title_prefix='Chapter 13', header='Chapter 13 fast course (ms-c13)',
    menu_title='Chapter 13 · Health: may, need, should', genre='Health',
    course_path='fast', prerequisites=[f'ms-c{k:02}' for k in range(1, 13)], prerequisite_units=[],
    prereq_grammar=['ms-c12-g02', 'ms-c12-g03', 'ms-c11-g02', 'ms-c08-g02'],
    word_scope=C13_WORDS, components=chapter13))


C14_WORDS = ['L-1201', 'L-1202', 'L-1203', 'L-1204', 'L-1205', 'L-1206', 'L-1207', 'L-1217', 'L-1209', 'L-1210', 'L-1208',
             'L-1213', 'L-1214', 'L-1215', 'L-1216', 'L-0710', 'L-0641', 'L-1269', 'L-1218', 'L-1270', 'L-1211', 'L-1212']


def chapter14(ledger):
    dialogue = [
        ('Tanaka', '«Cik Mei Ling, hujung minggu ini kita masih mahu mendaki?»'),
        ('Mei Ling', '«Masih. Tetapi cuaca mendung. Kalau hujan pada hari Sabtu, kita tidak boleh mendaki.»'),
        ('Tanaka', '«Kalau hujan, kita makan di kafe. Kalau tidak hujan, kita mendaki.»'),
        ('Mei Ling', '«Bagus! Tetapi saya tidak boleh datang pada hari Sabtu kerana saya bekerja.»'),
        ('Tanaka', '«Ada dua pilihan: kita tangguhkan ke hari Ahad atau ke hari Sabtu depan.»'),
        ('Mei Ling', '«Hari Ahad lebih baik. Hari Ahad saya cuti. Janji!»'),
        ('Tanaka', '«Ada perubahan rancangan, tetapi tujuan kita sama: berehat dan berjalan.»'),
        ('Tanaka', '«Baik. Ini rancangan kita. Mula-mula kita berjumpa di stesen pukul tujuh. Kemudian kita mendaki. Akhirnya kita makan di kafe.»'),
        ('Mei Ling', '«Saya akan datang awal supaya kita tidak lambat.»'),
        ('Tanaka', '«Bagus. Walaupun saya penat, saya suka mendaki. Kita boleh bercakap sambil berjalan.»'),
        ('Mei Ling', '«Kalau hujan lagi pada hari Ahad, bagaimana?»'),
        ('Tanaka', '«Kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c14-g02', 'ms-c14-g03', 'ms-c14-g04', 'ms-c14-g05', 'ms-c14-g06', 'ms-c14-g07', 'ms-c14-g08', 'ms-c14-g09'],
        patterns=['ms-c14-f01', 'ms-c14-f02', 'ms-c14-f03', 'ms-c14-f04', 'ms-c14-f05', 'ms-c14-f06'],
        goal='Give a condition, a reason, a purpose and a contrast, put a plan in order, and put off or cancel a plan.',
        explain=('第14章速習：45分で基本の22語、«kalau»・«kerana»・«supaya»・«walaupun»・«sambil»、«mula-mula»・«kemudian»・«akhirnya»、日常の語と書き言葉の語（«kalau» と «jika» など）、'
                 '週末のハイキングの延期と中止の場面を練習し、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 14 in one 45-minute session: 22 core words, «kalau», «kerana», «supaya», «walaupun» and «sambil», «mula-mula», «kemudian» and «akhirnya», the everyday and written pairs («kalau» and «jika», and so on), '
                 'and the scene of putting off and cancelling a weekend hike; then self-study in Kata-Kata. All names and plans are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say a condition with «kalau» and a reason with «kerana». / «kalau» で条件を、«kerana» で理由を言える。',
                'I can say a purpose with «supaya» and a contrast with «walaupun». / «supaya» で目的を、«walaupun» で対比を言える。',
                'I can put a plan in order with «mula-mula», «kemudian» and «akhirnya». / «mula-mula»・«kemudian»・«akhirnya» で計画を順序立てられる。',
                'I can put off or cancel a plan with «tangguhkan» and «batalkan», and tell the written «jika» from the everyday «kalau». / «tangguhkan»・«batalkan» で予定を延期・中止でき、書き言葉の «jika» と日常の «kalau» を区別できる。'], 'opener'),
            ('Core words · 基本の22語', core(ledger, C14_WORDS) +
             ['The full course adds the revision words of the whole unit.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Kalau» ___ «, kita» ___ «.»  e.g. «Kalau hujan, kita makan di kafe.» / «Kalau tidak hujan, kita mendaki.»',
                '2 · «Saya tidak datang kerana saya» ___ «.»  e.g. «Saya tidak datang kerana saya bekerja.» / «Saya bangun awal supaya saya tidak lambat.»',
                '3 · «Walaupun» ___ «, saya mahu» ___ «.»  e.g. «Walaupun hujan, saya mahu berjalan kaki.» / «Walaupun saya penat, saya suka mendaki.»',
                '4 · «Dia makan sambil» ___ «.»  e.g. «Dia makan sambil membaca surat khabar.» / «Kita boleh bercakap sambil berjalan.»',
                '5 · «Mula-mula kita» ___ «, kemudian kita» ___ «, akhirnya kita» ___ «.»  e.g. «Mula-mula kita makan, kemudian kita berjalan kaki, akhirnya kita balik.» / «Mula-mula kita berjumpa di stesen. Kemudian kita mendaki. Akhirnya kita makan di kafe.»',
                'Remember: people say «kalau» and «bila» and write «jika» and «apabila»; «tetapi» and «jadi» in speech, «namun» and «oleh itu» in a message. «kerana» and «sebab» give the reason, «supaya» the purpose. '
                '«tangguhkan» and «batalkan» go in «kita» sentences and requests.',
                '話すときは «kalau»・«bila»、書くときは «jika»・«apabila»；話し言葉は «tetapi»・«jadi»、メッセージでは «namun»・«oleh itu»。«kerana»・«sebab» は理由、«supaya» は目的。'
                '«tangguhkan»・«batalkan» は «kita» の文と依頼で使います。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You and B plan a Saturday outing (fictional). You can come on Sunday, not on Saturday, because you work. Give your reason, two choices and a rain plan.',
                'B: Ask why A cannot come, choose a day, ask what you do if it rains, and say the order of the day with «mula-mula», «kemudian» and «akhirnya».',
                'Change of plan: A says «Maaf, hari Ahad pun hujan. Jadi, kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.» B asks the time they meet at the cafe.',
                'A：Bさんと土曜日の外出を計画します（架空）。仕事があるので土曜日は行けず、日曜日なら行けます。理由・二つの選択肢・雨の日の計画を言います。'
                'B：Aがなぜ来られないかをたずね、日を選び、雨が降ったらどうするかをたずね、«mula-mula»・«kemudian»・«akhirnya» で一日の順序を言います。'
                '変更：Aが «Maaf, hari Ahad pun hujan. Jadi, kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.» と言い、Bはカフェで会う時刻をたずねます。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "If it rains, we eat at the cafe.": ____________________',
                '☐ 2. Say "I am not coming because I am working.": ____________________',
                '☐ 3. Say "I get up early so that I am not late.": ____________________',
                '☐ 4. Say "Even though it is raining, I want to walk.": ____________________',
                '☐ 5. Say "First we meet, then we hike, finally we eat.": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c14 ({sedia_cards(14)} cards, frames ms-c14-f01 and ms-c14-f02).',
                f'After the session: all {pack_cards(14)} Kata-Kata chapter 14 cards (ms-c14-001 to ms-c14-{last_card(14):03}) and frames ms-c14-f01 to ms-c14-f06 in the frame drill and Susun Ayat; '
                'the Kata-Kata scenario "The weekend hike" matches this pack.',
                'No Dunia scene primes chapter 14. The Hanashishou scenes with plans and changes are not yet tagged by chapter, so they are not assigned yet.',
                'Optional full-course Cikgu Sensai unit: unit 14 (reasons, conditions and plans), with its writing block.',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure).',
                '授業後：第14章のカードと文型を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Kalau hujan, kita makan di kafe.» 2 «Saya tidak datang kerana saya bekerja.» 3 «Saya bangun awal supaya saya tidak lambat.» '
             '4 «Walaupun hujan, saya mahu berjalan kaki.» 5 «Mula-mula kita berjumpa, kemudian kita mendaki, akhirnya kita makan.»',
             'Session plan (45 min): 0–5 recall chapters 5 and 13 («Kenapa …?» with «sebab», «perlu»); 5–15 core words; '
             '15–25 patterns 1 to 5; 25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 14. All Japanese is a draft awaiting native review.'])]


STAGE2_PACKS.append(dict(
    chapter_id='ms-c14', check_unit='ms-c14-fast', id_prefix='ms-c14-fast', level='A2',
    title_prefix='Chapter 14', header='Chapter 14 fast course (ms-c14)',
    menu_title='Chapter 14 · Reasons, conditions and plans', genre='Plans',
    course_path='fast', prerequisites=[f'ms-c{k:02}' for k in range(1, 14)], prerequisite_units=[],
    prereq_grammar=['ms-c13-g02', 'ms-c13-g04', 'ms-c11-g02', 'ms-c08-g02'],
    word_scope=C14_WORDS, components=chapter14))


C15_WORDS = ['L-1219', 'L-1233', 'L-1224', 'L-0623', 'L-0591', 'L-1234', 'L-0618', 'L-1223', 'L-1228', 'L-1222', 'L-1220',
             'L-1272', 'L-1221', 'L-1225', 'L-1226', 'L-1227', 'L-1229', 'L-1230', 'L-1231', 'L-1232', 'L-1271']


def chapter15(ledger):
    dialogue = [
        ('Tanaka', '«Maaf, ini kaunter barang hilang? Saya mencari dompet saya.»'),
        ('Staff', '«Ya, encik. Dompet yang mana? Apa warna dompet itu?»'),
        ('Tanaka', '«Hitam. Dompet kulit. Ada zip dan satu poket kecil.»'),
        ('Staff', '«Ada jenama?»'),
        ('Tanaka', '«Saya tidak ingat jenamanya. Bentuknya segi empat, seperti kotak kecil.»'),
        ('Staff', '«Seperti ini?»'),
        ('Tanaka', '«Ya, seperti itu, tetapi ada zip.»'),
        ('Staff', '«Ada dua dompet hitam di sini. Yang mana satu? Yang ada zip atau yang tidak ada zip?»'),
        ('Tanaka', '«Yang ada zip. Yang itu! Kad saya ada di dalam, tetapi pasport saya tidak ada.»'),
        ('Staff', '«Betul, ada kad encik di dalam. Ini dompet encik.»'),
        ('Tanaka', '«Terima kasih banyak! Encik Rahman, tetamu dari Jepun sudah sampai di stesen.»'),
        ('Rahman', '«Saya tidak tahu siapa dia. Lelaki yang mana?»'),
        ('Tanaka', '«Lelaki yang memakai cermin mata dan baju berjalur. Dia dengan seorang perempuan yang memakai topi. Mereka membawa beg yang ada tali panjang.»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c15-g02', 'ms-c15-g03', 'ms-c15-g04', 'ms-c15-g05', 'ms-c15-g06', 'ms-c15-g07', 'ms-c15-g08', 'ms-c15-g09'],
        patterns=['ms-c15-f01', 'ms-c15-f02', 'ms-c15-f03', 'ms-c15-f04', 'ms-c15-f05', 'ms-c15-f06'],
        goal='Say that something is lost, describe a thing or a person with «yang», colour and shape, and say which one.',
        explain=('第15章速習：45分で基本の21語、«___ saya hilang»、«yang» での説明、«berwarna»・«seperti»・«Yang mana satu?»、«memakai» を練習し、遺失物の窓口と駅の場面を演じ、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 15 in one 45-minute session: 21 core words, «___ saya hilang», descriptions with «yang», «berwarna», «seperti» and «Yang mana satu?», and «memakai»; '
                 'then the scene at the lost-property counter and the station, and self-study in Kata-Kata. All names and items are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say that something of mine is lost with «___ saya hilang». / «___ saya hilang» で自分の物がなくなったと言える。',
                'I can describe a thing or a person with «yang», «ada» and «memakai». / «yang»・«ada»・«memakai» で物や人を説明できる。',
                'I can give a colour and a shape with «berwarna», «bentuknya» and «seperti». / «berwarna»・«bentuknya»・«seperti» で色と形を言える。',
                'I can say which one with «Yang mana satu? Yang ___ atau yang ___?». / «Yang mana satu? Yang ___ atau yang ___?» でどれかを言える。'], 'opener'),
            ('Core words · 基本の21語', core(ledger, C15_WORDS) +
             ['The full course adds the revision words of the whole unit and the review block after chapter 15.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · ___ «saya hilang.»  e.g. «Dompet saya hilang.» / «Beg tangan saya hilang di stesen.»',
                '2 · «Saya mencari» ___ «yang ada» ___ «.»  e.g. «Saya mencari beg yang ada zip.» / «Lelaki yang memakai cermin mata.»',
                '3 · «Beg itu berwarna» ___ «dan ada» ___ «.»  e.g. «Beg itu berwarna hitam dan ada tali panjang.» / «Dompet kulit. Ada zip dan satu poket kecil.»',
                '4 · «Bentuknya» ___ «, seperti» ___ «.»  e.g. «Bentuknya segi empat, seperti kotak.» / «Ya, seperti itu, tetapi ada zip.»',
                '5 · «Yang mana satu? Yang» ___ «atau yang» ___ «?»  e.g. «Yang mana satu? Yang ada zip atau yang tidak ada zip?» / «Yang itu! Yang ada zip.»',
                'Remember: say the noun first and the description after it: «beg yang ada zip» (a clause needs «yang»); one adjective can follow the noun by itself («dompet hitam»). '
                '«hilang» is lost (you cannot find it), and «memakai» covers glasses, clothes, a hat and shoes. «seperti» is standard; everyday speech says «macam».',
                '名詞が先、説明があと：«beg yang ada zip»（節には «yang» が要ります）。形容詞一つなら名詞のすぐあとに置けます（«dompet hitam»）。'
                '«hilang» は見つからないこと、«memakai» はめがね・服・帽子・靴に使います。«seperti» は標準語で、日常は «macam» です。'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You lost a bag at the station (fictional). Say what is lost, its colour, its shape and one feature, and answer «Seperti ini?».',
                'B: You are the counter staff. Ask the colour and the brand, show an item, and ask «Yang mana satu? Yang ___ atau yang ___?».',
                'Change of plan: B says «Maaf, ada dua beg seperti itu. Yang mana satu? Yang ada poket atau yang ada tali panjang?» A chooses by one feature and says what is inside.',
                'A：駅でバッグをなくしました（架空）。なくした物・色・形・特徴を一つ言い、«Seperti ini?» に答えます。'
                'B：窓口の係員です。色とブランドをたずね、物を見せ、«Yang mana satu? Yang ___ atau yang ___?» とたずねます。'
                '変更：Bが «Maaf, ada dua beg seperti itu. Yang mana satu? Yang ada poket atau yang ada tali panjang?» と言い、Aは特徴を一つ言って選び、中身を言います。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "My wallet is lost.": ____________________',
                '☐ 2. Say "I am looking for a bag that has a zip.": ____________________',
                '☐ 3. Say "The man who wears glasses.": ____________________',
                '☐ 4. Say "The bag is black and has a long strap.": ____________________',
                '☐ 5. Say "Which one? The one with a zip or the one without?": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c15 ({sedia_cards(15)} cards, frames ms-c15-f01 and ms-c15-f02).',
                f'After the session: all {pack_cards(15)} Kata-Kata chapter 15 cards (ms-c15-001 to ms-c15-{last_card(15):03}) and frames ms-c15-f01 to ms-c15-f06 in the frame drill and Susun Ayat; '
                'the Kata-Kata scenario "A lost wallet and a visitor" matches this pack.',
                'No Dunia scene primes chapter 15. The Hanashishou scenes with lost property and stations are not yet tagged by chapter, so they are not assigned yet.',
                'Optional full-course Cikgu Sensai unit: unit 15 (describing things and people), with the review block after chapter 15.',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure).',
                '授業後：第15章のカードと文型を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Dompet saya hilang.» 2 «Saya mencari beg yang ada zip.» 3 «Lelaki yang memakai cermin mata.» '
             '4 «Beg itu berwarna hitam dan ada tali panjang.» 5 «Yang mana satu? Yang ada zip atau yang tidak ada zip?»',
             'Session plan (45 min): 0–5 recall chapters 5, 8 and 14 (a colour, clothes, «kerana»); 5–15 core words; '
             '15–25 patterns 1 to 5; 25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 15. All Japanese is a draft awaiting native review.'])]


STAGE2_PACKS.append(dict(
    chapter_id='ms-c15', check_unit='ms-c15-fast', id_prefix='ms-c15-fast', level='A2',
    title_prefix='Chapter 15', header='Chapter 15 fast course (ms-c15)',
    menu_title='Chapter 15 · Describing things and people', genre='Lost property',
    course_path='fast', prerequisites=[f'ms-c{k:02}' for k in range(1, 15)], prerequisite_units=[],
    prereq_grammar=['ms-c14-g02', 'ms-c14-g03', 'ms-c13-g02', 'ms-c06-g02'],
    word_scope=C15_WORDS, components=chapter15))


C16_WORDS = ['L-1235', 'L-0619', 'L-0644', 'L-1236', 'L-0621', 'L-0752', 'L-1237', 'L-1238', 'L-1241',
             'L-1239', 'L-1240', 'L-1242', 'L-1243', 'L-0875', 'L-0758', 'L-1244', 'L-1251', 'L-1250',
             'L-1245', 'L-1246', 'L-1247', 'L-1248', 'L-1249']


def chapter16(ledger):
    dialogue = [
        ('Tanaka', '«Selamat malam. Maaf, kunci saya tertinggal di dalam rumah. Pintu terkunci.»'),
        ('Guard', '«Unit berapa, encik?»'),
        ('Tanaka', '«Blok B, unit 12-3. Saya terlupa kunci tadi.»'),
        ('Guard', '«Encik tunggu di sini. Saya hubungi pejabat pengurusan.»'),
        ('Tanaka', '«Baik. Terima kasih banyak.»'),
        ('Mei Ling', '«Maaf, saya lambat. Saya terlepas bas, kemudian saya tersangkut di jalan yang sesak.»'),
        ('Tanaka', '«Jangan risau. Mesyuarat belum bermula.»'),
        ('Mei Ling', '«Maaf, Encik Tanaka! Air kopi saya tertumpah di meja. Cawan saya pun pecah.»'),
        ('Tanaka', '«Awak tidak sengaja. Jangan risau.»'),
        ('Mei Ling', '«Saya ambil tisu. Fail encik sedikit basah.»'),
        ('Tanaka', '«Terima kasih. Hati-hati, lantai licin.»'),
        ('Tanaka', '«Selamat pagi. Saya tergelincir di tangga tadi.»'),
        ('Receptionist', '«Encik tercedera? Di mana yang sakit?»'),
    ]
    return [dict(
        slug='pack', type='Fast-course pack', title='Fast-course summary pack',
        block='Fast', minutes=45, course_path='fast',
        grammar=['ms-c16-g02', 'ms-c16-g03', 'ms-c16-g04', 'ms-c16-g05', 'ms-c16-g06', 'ms-c16-g07', 'ms-c16-g08', 'ms-c16-g09'],
        patterns=['ms-c16-f01', 'ms-c16-f02', 'ms-c16-f03', 'ms-c16-f04', 'ms-c16-f05', 'ms-c16-f06'],
        goal='Say what happened by accident with ‹ter-›, apologise for a small slip, report a locked door or a spill, and keep ‹ter-› (the most) apart from ‹ter-› (by accident).',
        explain=('第16章速習：45分で基本の23語、«Saya tertinggal ___ di ___»、«Maaf, saya ___»、«tidak sengaja»、«Pintu terkunci.»、«termurah» と «tertinggal» の違いを練習し、鍵・こぼれたコーヒー・クリニックの場面を演じ、残りは Kata-Kata で自習します。日本語は未監修です。',
                 'Chapter 16 in one 45-minute session: 23 core words, «Saya tertinggal ___ di ___», «Maaf, saya ___», «tidak sengaja», «Pintu terkunci.» and the two ‹ter-› («termurah» against «tertinggal»); '
                 'then the scene at the locked door, the spilt coffee and the clinic counter, and self-study in Kata-Kata. All names and items are fictional.'),
        sections=[
            ('Can-do goals · できること', [
                'I can say what I left behind or forgot by accident with «tertinggal» and «terlupa». / «tertinggal»・«terlupa» でうっかり置き忘れたことや忘れたことを言える。',
                'I can apologise for a small slip with «Maaf, saya ___.». / «Maaf, saya ___.» で小さな失敗を謝れる。',
                'I can say what spilt, slipped, broke or was locked with a ‹ter-› verb and «tidak sengaja». / ‹ter-› の動詞と «tidak sengaja» で、こぼれた・滑った・割れた・鍵がかかったことを言える。',
                'I can tell «termurah» (the most) from «tertinggal» (by accident). / «termurah»（最も）と «tertinggal»（うっかり）を区別できる。'], 'opener'),
            ('Core words · 基本の23語', core(ledger, C16_WORDS) +
             ['The full course adds the revision words of the whole unit and the writing block after chapter 16.'], 'vocabulary'),
            ('Key patterns · 文型', [
                '1 · «Saya tertinggal» ___ «di» ___ «.»  e.g. «Saya tertinggal telefon di pejabat.» / «Kunci saya tertinggal di dalam rumah.»',
                '2 · «Maaf, saya» ___ «.»  e.g. «Maaf, saya terlupa.» / «Maaf, saya terlepas bas.»',
                '3 · «Saya tidak sengaja» ___ ___ «.»  e.g. «Saya tidak sengaja terlanggar kerusi.» / «Awak tidak sengaja. Jangan risau.»',
                '4 · ___ «tertumpah di» ___ «. / Pintu terkunci. Boleh tolong» ___ «?»  e.g. «Air kopi tertumpah di meja.» / «Pintu terkunci. Boleh tolong hubungi pejabat pengurusan?»',
                '5 · «Yang ini» ___ «, tetapi dompet saya» ___ «di rumah.»  e.g. «Yang ini termurah, tetapi dompet saya tertinggal di rumah.» / «Yang ini terbaik, tetapi kad saya tertinggal di rumah.»',
                'Remember: ‹ter-› + a verb means "by accident, without meaning to"; ‹ter-› + an adjective («termurah», «terbesar», «terbaik») means "the most". '
                '«tertinggal» is left behind (you know where it is); «hilang» is lost (you cannot find it). «terkunci» is a state: «Pintu terkunci.»',
                '‹ter-›＋動詞は「うっかり、そのつもりなく」、‹ter-›＋形容詞（«termurah»・«terbesar»・«terbaik»）は「最も」。'
                '«tertinggal» は置き忘れ（どこか分かっている）、«hilang» はなくしたこと（見つからない）。«terkunci» は状態です：«Pintu terkunci.»'], 'model'),
            ('Model conversation · 会話 (fictional)', turns(dialogue), 'model'),
            ('Task · タスク', [
                'A: You live in Block B, unit 12-3 (fictional). Your key is left inside the flat. Tell the guard with «tertinggal» and «terkunci», say «Maaf, saya terlupa.» and ask him to contact the management office.',
                'B: You are the guard. Ask the unit, say you will contact the management office, and answer kindly.',
                'Change of plan: B says «Maaf, pejabat pengurusan belum buka. Encik tunggu sekejap.» A asks to wait in the lobby and says «Saya tidak sengaja terlupa kunci itu.»',
                'A：Bブロック12-3号室に住んでいます（架空）。鍵が家の中にあります。«tertinggal»・«terkunci» で警備員に伝え、«Maaf, saya terlupa.» と言い、管理事務所への連絡を頼みます。'
                'B：警備員です。部屋をたずね、管理事務所に連絡すると言い、やさしく答えます。'
                '変更：Bが «Maaf, pejabat pengurusan belum buka. Encik tunggu sekejap.» と言い、Aはロビーで待ってよいかをたずね、«Saya tidak sengaja terlupa kunci itu.» と言います。'], 'task'),
            ('Self-check · できるチェック', [
                '☐ 1. Say "I left my phone at the office.": ____________________',
                '☐ 2. Say "Sorry, I forgot.": ____________________',
                '☐ 3. Say "Coffee spilled on the table.": ____________________',
                '☐ 4. Say "The door is locked.": ____________________',
                '☐ 5. Say "This one is the cheapest, but my wallet is left at home.": ____________________'], 'test'),
            ('Self-study guide · 自習ガイド', [
                f'Before the session: Kata-Kata Sedia Kelas c16 ({sedia_cards(16)} cards, frames ms-c16-f01 and ms-c16-f02).',
                f'After the session: all {pack_cards(16)} Kata-Kata chapter 16 cards (ms-c16-001 to ms-c16-{last_card(16):03}) and frames ms-c16-f01 to ms-c16-f06 in the frame drill and Susun Ayat; '
                'the Kata-Kata scenario "A locked door, a spill and a slip" matches this pack.',
                'No Dunia scene primes chapter 16. The Hanashishou scenes with the guardhouse, a missed bus and the clinic are not yet tagged by chapter, so they are not assigned yet.',
                'Optional full-course Cikgu Sensai unit: unit 16 (accidents with ‹ter-›), with the writing block after chapter 16.',
                'Expected self-study: about 9 to 10 hours for this chapter (planning figure).',
                '授業後：第16章のカードと文型を復習しましょう。自習の目安は約9〜10時間です。'], 'opener')],
        key=['Self-check: 1 «Saya tertinggal telefon di pejabat.» 2 «Maaf, saya terlupa.» 3 «Air kopi tertumpah di meja.» '
             '4 «Pintu terkunci.» 5 «Yang ini termurah, tetapi dompet saya tertinggal di rumah.»',
             'Session plan (45 min): 0–5 recall chapters 1, 6 and 15 («Maaf», «termurah», «hilang»); 5–15 core words; '
             '15–25 patterns 1 to 5; 25–35 model conversation in pairs; 35–45 task with the change of plan, then the self-check.',
             'Same content and ledger limits as unit 16. All Japanese is a draft awaiting native review.'])]


STAGE2_PACKS.append(dict(
    chapter_id='ms-c16', check_unit='ms-c16-fast', id_prefix='ms-c16-fast', level='A2',
    title_prefix='Chapter 16', header='Chapter 16 fast course (ms-c16)',
    menu_title='Chapter 16 · Accidents with ter-', genre='Accidents',
    course_path='fast', prerequisites=[f'ms-c{k:02}' for k in range(1, 16)], prerequisite_units=[],
    prereq_grammar=['ms-c15-g02', 'ms-c15-g03', 'ms-c06-g02', 'ms-c12-g02'],
    word_scope=C16_WORDS, components=chapter16))
