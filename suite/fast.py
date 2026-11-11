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
                '3 · «Saya orang» ___ . «Asal saya dari» ___ .  e.g. «Saya orang Jepun. Asal saya dari Osaka.» / «Kampung encik di mana?»',
                '4 · «Saya kerja di» ___ .  e.g. «Saya kerja di syarikat Jepun. Saya jurutera.» / «Saya belajar di Universiti Malaya.»',
                '5 · «Saya tinggal di» ___ .  e.g. «Saya tinggal di Mont Kiara.» / «Saya tinggal dengan keluarga saya.»',
                '6 · «Saya suka» ___ .  e.g. «Saya suka masakan Malaysia.» / «Apa hobi encik?»',
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
