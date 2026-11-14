"""Unit 2B (chapter 2, second half): work, study, home, family, likes;
pe- and -an; the -kah forms, adakah and bolehkah. Includes the writing block
(a self-introduction form).

Malay is limited to ledger rows placed in chapters 1 and 2. Patterns are
Kata-Kata frames ms-c02-f04 to f08, plus a word-building box for pe- and -an
(grammar points ms-c02-g10 and g11; not a Kata-Kata frame). Since 11 Nov 2026 the
unit has a hobby word bank (L-0968 badminton and L-1019 to L-1031, Sam's list):
each learner picks the words that are true for them; it is not tested as core.
«dengan» moved to unit 2A, so 2A and 2B carry a similar core load (35 and 37).
Japanese is a draft awaiting native review.
"""
from . import vocab, malay_words, english_words, pattern, turns

GOALS = {
    'A': 'I can say where I work or study, where I live and who I live with.',
    'B': 'I can ask about someone\'s work, home, family and likes, formally and informally.',
    'C': 'I can follow a self-introduction about work and family and read a self-introduction message.',
    'D': 'I can check my self-introduction in a short test and say what I can do.',
    'E': 'I can talk about work in an office scene and ask polite questions with «bolehkah» and «adakah».',
}
GOALS_JA = {
    'A': '仕事・勉強している所、住んでいる所、だれと住んでいるかが言える。',
    'B': '相手の仕事・家・家族・好きなことを、丁寧にもくだけた形でもたずねられる。',
    'C': '仕事と家族についての自己紹介を聞いて分かり、自己紹介のメッセージが読める。',
    'D': '小テストで自己紹介の表現を確かめ、できることが言える。',
    'E': 'オフィスの場面で仕事の話をし、«bolehkah»・«adakah» で丁寧にたずねられる。',
}
WRITING_GOAL = 'I can fill in a self-introduction form and write a short self-introduction.'
WORDS = ['L-0050', 'L-0051', 'L-0988', 'L-0783', 'L-0057', 'L-0064', 'L-0065', 'L-0066', 'L-0067', 'L-0068',
         'L-0069', 'L-0070', 'L-0071', 'L-0072', 'L-0073', 'L-0074', 'L-0079', 'L-0080', 'L-0081',
         'L-0082', 'L-0083', 'L-0084', 'L-0085', 'L-0086', 'L-0087', 'L-0088', 'L-0089', 'L-0090', 'L-0091',
         'L-0092', 'L-0093', 'L-0094', 'L-0095', 'L-0096', 'L-0097', 'L-0098', 'L-0987',
         'L-0523', 'L-0524', 'L-0525', 'L-0526', 'L-0527', 'L-0528', 'L-0529', 'L-0530', 'L-0531', 'L-0532',
         'L-0533', 'L-0534', 'L-0535', 'L-0536',
         'L-0968', 'L-1019', 'L-1020', 'L-1021', 'L-1022', 'L-1023', 'L-1024', 'L-1025', 'L-1026', 'L-1027',
         'L-1028', 'L-1029', 'L-1030', 'L-1031']
G = dict(place='ms-c02-g08', like='ms-c02-g09', pe='ms-c02-g10', an='ms-c02-g11', kah='ms-c02-g12', fam='ms-c02-g14',
         nn='ms-c02-g03', qw='ms-c02-g04', pron='ms-c02-g02', nya='ms-c02-g07')
ALL = [G['place'], G['like'], G['pe'], G['an'], G['kah'], G['fam']]


def components(ledger):
    C = []
    C.append(dict(
        slug='opener', type='Opener', title='Chapter opener', block='A', minutes=5,
        grammar=[G['place'], G['fam']], goal=GOALS['A'], prereq_grammar=['ms-c02-g03', 'ms-c02-g04', 'ms-c02-g05'],
        explain=('このユニットの目標と場面を確認し、ユニット2Aの自己紹介を思い出します。',
                 'Read the goals and the scene, then recall the unit 2A introductions.'),
        sections=[
            ('Can-do goals · できること', [
                *[f'Block {b}: {GOALS[b]}' for b in 'ABCDE'],
                *[f'ブロック{b}：{GOALS_JA[b]}' for b in 'ABCDE'],
                'Writing block: ' + WRITING_GOAL + ' / 書くブロック：自己紹介の用紙に記入し、短い自己紹介文が書ける。']),
            ('The scene · 場面', [
                '«Encik» Tanaka joins a Malay class after work. «Cikgu» Siti asks the class about their work, home, family and likes. '
                'At the office, a new colleague, «Puan» Sato, introduces herself in the team chat.',
                '田中さんは仕事のあとマレー語クラスに参加します。シティ先生がクラスのみんなに仕事・家・家族・好きなことをたずねます。'
                'オフィスでは新しい同僚の佐藤さんがチームのチャットで自己紹介をします。', 'Genre: Work and study · ジャンル：仕事と勉強']),
            ('Recall from unit 2A · 2Aの復習 (5 min)', [
                'Without notes, ask your partner three questions: name, nationality, hometown. Then introduce your partner to the class.',
                'Expected: «Siapa nama awak?» «Awak orang Jepun?» «Kampung awak di mana?» «Ini … Namanya … Dia …»',
                'ノートを見ずに、名前・国籍・出身地の三つをたずね、相手をクラスに紹介しましょう。']),
            ('Self-study · 自習', [
                'Before class: the Kata-Kata chapter 2 cards for work, home and family (ms-c02-029 to ms-c02-063) and the Dunia scene "Pagi di pejabat".',
                'After class: spaced review of all chapter 2 cards. Planning figure: about 3 hours per unit.',
                '授業前：第2章の仕事・家・家族のカードと Dunia「Pagi di pejabat」。授業後：第2章のカード全部を復習。目安は1ユニット約3時間。'])],
        key=['Expected recall as printed. Recycle any unit 2A test items learners missed.']))

    C.append(dict(
        slug='vocabulary', type='Vocabulary', title='Vocabulary focus', block='A', minutes=10,
        grammar=ALL, goal=GOALS['A'],
        explain=('ユニット2Bの台帳の単語です：-kah の質問、仕事と勉強、家と家族、好きなこと、pe- の語（人）、-an の語（もの）、'
                 'そして Kata-Kata の場面「Pagi di pejabat」のオフィスのことば（聞いて分かればよい）と、自分で選ぶ趣味のことば。例文を声に出して読みましょう。',
                 'The ledger words for unit 2B: -kah questions, work and study, home and family, likes, pe- words (people), -an words (things), '
                 'the office words from the Kata-Kata scene "Pagi di pejabat" (recognise), and a hobby word bank to choose from. '
                 'Core: 37 words. Read every example aloud.'),
        sections=[('Words by group · 場面別の単語', vocab(ledger, [
            ('Formal and polite questions · 丁寧な質問', [
                ('L-0050', '«Siapakah nama encik?»', dict(display='«Siapakah»')),
                ('L-0051', '«Apakah nama syarikat puan?»', dict(display='«Apakah»')),
                ('L-0052', '«Di manakah pejabat encik?» (review: the -kah form of «di mana»)', dict(display='«di manakah»', en='where (formal)')),
                ('L-0988', '«Adakah encik orang Jepun?»', dict(en='yes/no question opener (Is it …?)')),
                ('L-0783', '«Bolehkah saya tanya?»', dict(en='Can …? / May I …? (polite)', ja='「〜できますか・〜してもいいですか」（«boleh» のていねいな形）'))]),
            ('Work and study · 仕事と勉強', [
                ('L-0065', '«Saya kerja di syarikat Jepun.» (formal written form: ‹bekerja›)'),
                ('L-0064', '«Pejabat saya di Kuala Lumpur.»'),
                ('L-0066', '«Saya kerja di syarikat Sakura.»'),
                ('L-0083', '«Saya jurutera.»'),
                ('L-0082', '«Isteri saya cikgu.» («cikgu» is the everyday form)', dict(display='«guru» / «cikgu»')),
                ('L-0067', '«Anak saya belajar di sekolah Jepun.»'),
                ('L-0068', '«Dia belajar di Universiti Malaya.»'),
                ('L-0069', '«Saya belajar di kelas ini.»'),
                ('L-0987', '«Saya suka kelas ini.»')]),
            ('Home and family · 家と家族', [
                ('L-0070', '«Rumah saya di Bangsar.»'),
                ('L-0071', '«Saya tinggal di Mont Kiara dengan keluarga saya.» («dengan»: unit 2A)'),
                ('L-0079', '«Keluarga saya di Jepun.»'),
                ('L-0080', '«Isteri saya orang Malaysia.» / «Suami saya jurutera.»', dict(display='«isteri» / «suami»')),
                ('L-0081', '«Encik ada anak?» — «Ada.»'),
                ('L-0057', '«Saya ada anak.»')]),
            ('Likes · 好きなこと', [
                ('L-0072', '«Apa hobi encik?»'),
                ('L-0073', '«Saya suka masakan Malaysia.»'),
                ('L-0074', '«Anak saya suka main dengan kawan.»')]),
            ('Hobby word bank: pick your own · 趣味のことば（自分で選ぶ）', [
                ('L-1019', '«Saya suka muzik Jepun.»'),
                ('L-1022', '«Saya suka lagu ini.»'),
                ('L-1024', '«Hobi saya karaoke.»'),
                ('L-1020', '«Saya suka filem Jepun.»'),
                ('L-1021', '«Apa sukan encik?»'),
                ('L-1025', '«Bos saya suka main golf.»'),
                ('L-0968', '«Saya suka main badminton dengan kawan.»'),
                ('L-1023', '«Isteri saya suka masak.»'),
                ('L-1026', '«Kafe ini best!» (also spelt ‹cafe›; spoken)'),
                ('L-1027', '«Hobi saya cafe hopping.» (spoken)'),
                ('L-1028', '«Saya suka jalan-jalan.»'),
                ('L-1029', '«Saya suka travel.» (spoken; standard ‹melancong› comes in chapter 11)'),
                ('L-1030', '«Hobi saya hiking.» (spoken; standard ‹mendaki› comes in chapter 11)'),
                ('L-1031', '«Hobi saya oshikatsu.» (Japanese loan: supporting a favourite idol or character)')]),
            ('pe- words: people · pe- の語（人）', [
                ('L-0084', '«Dia pekerja syarikat Sakura.» (‹kerja› → «pekerja»)'),
                ('L-0085', '«Saya pelajar.» (‹ajar› → «pelajar»)'),
                ('L-0086', '«Dia pelawat dari Jepun.» (‹lawat› → «pelawat»)'),
                ('L-0087', '«Mereka pelancong Jepun.» (‹lancong› → «pelancong»)'),
                ('L-0088', '«Keluarga dia petani.» (‹tani› → «petani»)'),
                ('L-0089', '«Dia pemandu syarikat.» (recognise only; ‹pandu› → «pemandu»)'),
                ('L-0090', '«Encik Rahman pengurus.» (recognise only; ‹urus› → «pengurus»)')]),
            ('-an words: things · -an の語（もの）', [
                ('L-0091', '«Saya suka makanan Malaysia.» (‹makan› → «makanan»)'),
                ('L-0092', '«Apa minuman encik?» (‹minum› → «minuman»)'),
                ('L-0093', '«Isteri saya suka masakan Jepun.» (‹masak› → «masakan»)'),
                ('L-0094', '«Ini bacaan kelas kita.» (‹baca› → «bacaan»)'),
                ('L-0095', '«Ini tulisan anak saya.» (‹tulis› → «tulisan»)'),
                ('L-0096', '«Ada soalan?» (‹soal› → «soalan»)'),
                ('L-0097', '«Ini jawapan saya.» (‹jawab› → «jawapan»: b becomes p)'),
                ('L-0098', '«Ini latihan kita.» (‹latih› → «latihan»)')]),
            ('Office words from "Pagi di pejabat" (recognise) · オフィスのことば', [
                ('L-0523', '«Ini komputer saya.»'),
                ('L-0524', '«Ini kertas encik?»'),
                ('L-0525', '«Fail itu di mana?»'),
                ('L-0526', '«Encik ada emel?» (both spellings are used)', dict(display='«emel» / «e-mel»')),
                ('L-0527', '«Bolehkah saya cetak?»'),
                ('L-0528', '«Boleh hantar emel?»'),
                ('L-0529', '«Jangan risau, saya simpan fail itu.»'),
                ('L-0530', '«Ini tandatangan saya.»'),
                ('L-0531', '«Dia rakan sekerja saya.»'),
                ('L-0532', '«Bos saya orang Jepun.» (informal)', dict(en='boss (informal)')),
                ('L-0533', '«Maaf, saya sibuk.»'),
                ('L-0534', '«Encik Rahman cuti.»'),
                ('L-0535', '«Bolehkah saya tanya?»'),
                ('L-0536', '«Jawab soalan ini.»')]),
        ]))],
        key=['Kata-Kata cards ms-c02-015 to 017, 022, 029 to 039, 041 to 063; Dunia cards ms-d-pejabat-pagi-01 to 14.',
             '«adakah» (L-0988), «bolehkah» (L-0783) and «kelas» (L-0987) now have Kata-Kata chapter 2 cards (ms-c02-070, -065, -069). '
             'Roots shown as quoted roots come from Kata-Kata card notes; some (‹makan›, ‹baca›) are chapter 4 words and are not taught here.',
             'Load: 37 core words (plus the -kah review of «di manakah»), 14 office words to recognise, and 14 hobby words of which each learner keeps the few that are true for them. '
             '«dengan» is now taught in unit 2A. Hobby words L-1019 to L-1031 now have Kata-Kata chapter 2 cards (ms-c02-074 to ms-c02-086); test only the hobby words a learner chose.',
             'Malaysian forms: «muzik», «filem», «sukan», «kafe».',
             'Check in class: say a root; learners give the pe- person or the -an thing. Expected: ‹makan› → «makanan»; ‹ajar› → «pelajar».']))

    C.append(dict(
        slug='pattern-grammar', type='Pattern and grammar', title='Pattern and grammar focus', block='A', minutes=20,
        grammar=ALL, patterns=['ms-c02-f04', 'ms-c02-f05', 'ms-c02-f06', 'ms-c02-f07', 'ms-c02-f08'], goal=GOALS['A'],
        explain=('四つの文型と、pe-・-an の語の作り方を、例の質問と答えで練習します。',
                 'Four Kata-Kata patterns and one word-building box (pe- and -an), each with question-and-answer examples.'),
        sections=[
            pattern(1, 'ms-c02-f04, f05', '«Saya kerja di» ___ . «Saya» (job) . / «Saya belajar di» ___ .', [
                'A: «Encik kerja di mana?»  B: «Saya kerja di syarikat Jepun. Saya jurutera.»',
                'A: «Puan kerja di mana?»  B: «Saya kerja di sekolah. Saya guru.»',
                'A: «Cik pelajar?»  B: «Ya, saya belajar di Universiti Malaya.»',
                'A: «Apa kerja dia?»  B: «Dia pemandu.»',
                'A: «Encik Rahman pengurus?»  B: «Ya, dia pengurus pejabat kami.»'],
                '«kerja di» + a place says where you work; «belajar di» + a place, where you study. A job is just a noun after the person: «Saya jurutera». '
                '«Apa kerja …?» asks someone\'s job. «kerja» is everyday speech; the formal written form is ‹bekerja› (a later chapter).',
                '«kerja di»＋場所で働いている所、«belajar di»＋場所で勉強している所を言います。職業は人のあとに名詞を置くだけです：«Saya jurutera»。'
                '«Apa kerja …?» で職業をたずねます。«kerja» は話し言葉で、書き言葉では ‹bekerja›（後の章）です。',
                '«di» works like で in 会社で働いています. But Malay verbs never change: «kerja» covers 働く, 働いている and 働きます.',
                '«di» は「会社で働いています」の「で」に近いです。ただしマレー語の動詞は形が変わりません：«kerja» で「働く・働いている・働きます」を表します。'),
            pattern(2, 'ms-c02-f06', '«Saya tinggal di» ___ ( «dengan» ___ ).', [
                'A: «Encik tinggal di mana?»  B: «Saya tinggal di Mont Kiara.»',
                'A: «Puan tinggal dengan siapa?»  B: «Saya tinggal dengan suami dan anak saya.»',
                'A: «Rumah cik di mana?»  B: «Rumah saya di Petaling Jaya.»',
                'A: «Encik ada anak?»  B: «Ada. Anak saya belajar di sekolah Jepun.»',
                'A: «Keluarga awak di mana?»  B: «Keluarga saya di Jepun.»'],
                '«tinggal di» = live in. «dengan» = with. «ada» = have or there is; answer a yes/no question with «Ada» (yes) or «Tidak ada» (no). '
                'The owner comes after the thing: «anak saya» = my child, «rumah cik» = your house.',
                '«tinggal di»＝〜に住んでいる。«dengan»＝〜と一緒に。«ada»＝ある・いる・持っている。答えは «Ada»（はい）か «Tidak ada»（いいえ）。'
                '持ち主はもののあとに来ます：«anak saya»＝私の子ども、«rumah cik»＝あなたの家。',
                '«dengan» is close to と in 夫と住んでいます. «ada» covers ある, いる and 持っている.',
                '«dengan» は「夫と住んでいます」の「と」に近いです。«ada» は「ある」「いる」「持っている」をまとめて表します。'),
            pattern(3, 'ms-c02-f07', '«Hobi saya» ___ . / «Saya suka» ___ .', [
                'A: «Apa hobi encik?»  B: «Saya suka masakan Malaysia.»',
                'A: «Puan suka makanan Jepun?»  B: «Ya, saya suka makanan Jepun.»',
                'A: «Anak encik suka main?»  B: «Ya, dia suka main dengan kawan.»',
                'A: «Awak suka kelas ini?»  B: «Ya, saya suka kelas ini!»',
                'A: «Isteri encik suka minuman Malaysia?»  B: «Tidak, dia tidak suka.»',
                'A: «Apa hobi cik?»  B: «Hobi saya karaoke dan jalan-jalan.»'],
                '«suka» (like) comes before a noun or a verb: «suka masakan Malaysia», «suka main». «tidak suka» = do not like. '
                'For «Hobi saya ___», pick a word from the hobby word bank («karaoke», «golf», «hiking», «oshikatsu» …) or ask your teacher.',
                '«suka»（好き）は名詞や動詞の前に来ます：«suka masakan Malaysia»、«suka main»。«tidak suka»＝好きではない。'
                '«Hobi saya ___» には趣味のことば（«karaoke»、«golf»、«hiking»、«oshikatsu» など）から選ぶか、先生に聞きましょう。',
                'In Japanese the thing you like comes first (料理が好き); in Malay it comes after «suka»: «suka masakan». No が is needed.',
                '日本語は「料理が好き」と好きなものが先ですが、マレー語は «suka» のあとです：«suka masakan»。「が」はいりません。'),
            pattern(4, 'ms-c02-f08', '«Di manakah» ___ ? / «Adakah» ___ ? / «Bolehkah» ___ ?', [
                'A: «Di manakah pejabat encik?»  B: «Pejabat saya di Kuala Lumpur.»',
                'A: «Siapakah nama encik?»  B: «Nama saya Tanaka.»',
                'A: «Apakah nama syarikat puan?»  B: «Nama syarikat saya Sakura.»',
                'A: «Adakah encik orang Jepun?»  B: «Ya, saya orang Jepun.»',
                'A: «Bolehkah saya tanya?»  B: «Boleh.»',
                'A: «Adakah Cik Mei Ling pelajar?»  B: «Tidak, dia jurutera.»'],
                '-kah on a question word makes a formal question, used in writing, forms and announcements: «Siapakah», «Apakah», «di manakah». '
                '«Adakah» opens a formal yes/no question; answer «Ya» or «Tidak». «Bolehkah» asks politely if something is possible; answer «Boleh» or «Tidak boleh». '
                'In everyday speech a rising voice is enough: «Encik orang Jepun?»',
                '疑問詞に -kah をつけると、書き言葉・書類・アナウンスで使う改まった質問になります：«Siapakah»、«Apakah»、«di manakah»。'
                '«Adakah» は改まった「はい・いいえ」の質問を始め、答えは «Ya» か «Tidak»。«Bolehkah» は「〜してもいいですか・できますか」と丁寧にたずね、答えは «Boleh» か «Tidak boleh»。'
                'ふだんの会話では文末を上げるだけで十分です：«Encik orang Jepun?»',
                '-kah works like か, but it sits on the word being asked about, not at the end. «Bolehkah saya …?» ≈ 〜してもいいですか.',
                '-kah は「か」に似ていますが、文末ではなく、たずねたい語につきます。«Bolehkah saya …?»≈「〜してもいいですか」。'),
            pattern(5, 'grammar ms-c02-g10, g11', 'pe- + root = a person · root + -an = a thing', [
                'A: «Dia pelajar?»  B: «Ya, dia belajar di universiti.»',
                'A: «Encik pekerja syarikat ini?»  B: «Ya, saya pekerja syarikat ini.»',
                'A: «Ada soalan?»  B: «Ada. Bolehkah saya tanya?»',
                'A: «Ini jawapan awak?»  B: «Ya, ini jawapan saya.»',
                'A: «Encik suka makanan Malaysia?»  B: «Ya, dan minuman Malaysia juga.»'],
                'pe- turns a root into the person who does it: ‹kerja› → «pekerja», ‹ajar› → «pelajar», ‹lawat› → «pelawat». With some roots the sound changes '
                '(‹pandu› → «pemandu», ‹urus› → «pengurus»): recognise these for now. -an turns a root into a thing: ‹makan› → «makanan» (food), '
                '‹soal› → «soalan» (question), ‹jawab› → «jawapan» (b becomes p).',
                'pe- は語根を「それをする人」にします：‹kerja›→«pekerja»、‹ajar›→«pelajar»、‹lawat›→«pelawat»。音が変わる語（‹pandu›→«pemandu»、‹urus›→«pengurus»）は今は見て分かれば十分です。'
                '-an は語根を「もの」にします：‹makan›→«makanan»（食べ物）、‹soal›→«soalan»（質問）、‹jawab›→«jawapan»（b が p に）。',
                'This is like 〜者 or 〜手 (運転手) for people and 〜物 for things: «makanan» ≈ 食べ物, «minuman» ≈ 飲み物.',
                '人を表す「〜者・〜手」（運転手）、ものを表す「〜物」に似ています：«makanan»≈食べ物、«minuman»≈飲み物。'),
        ],
        key=['Patterns 1 to 4 are Kata-Kata frames ms-c02-f04 to f08. Box 5 is a grammar point (pe- and -an), not a frame.',
             'Teacher prompts: model the A lines; the class answers with their own facts; then pairs swap.',
             'Check: «kerja di» / «tinggal di» with «di»; owner after the thing («anak saya»); «suka» before what is liked; -kah on the question word.']))

    # Drills ------------------------------------------------------------
    C.append(dict(
        slug='drill-1-pattern-table', type='Drill', sub_type='repeat', title='Drill 1 · Pattern table', block='B', minutes=3,
        grammar=[G['place'], G['fam']], patterns=['ms-c02-f04', 'ms-c02-f05', 'ms-c02-f06'], goal=GOALS['B'],
        explain=('表の言葉を組み合わせて、全部の文を声に出して読みます。', 'Combine the words in the table and read every sentence aloud.'),
        sections=[('Read every combination · 全部の組み合わせを読む', [
            'Table 1: [ «Saya» / «Dia» / «Kami» ] «kerja di» [ «pejabat» / «sekolah» / «syarikat Jepun» ] .',
            '1. «Saya kerja di pejabat.»', '2. «Dia kerja di sekolah.»', '3. «Kami kerja di syarikat Jepun.»',
            'Table 2: [ «Saya» / «Anak saya» / «Mereka» ] «belajar di» [ «sekolah» / «universiti» / «kelas ini» ] .',
            '4. «Saya belajar di kelas ini.»', '5. «Anak saya belajar di sekolah.»', '6. «Mereka belajar di universiti.»',
            'Table 3: [ «Saya» / «Kami» ] «tinggal di» [ Mont Kiara / Bangsar ] «dengan» [ «isteri» / «suami» / «keluarga» ] «saya» .',
            '7. «Saya tinggal di Mont Kiara dengan isteri saya.»', '8. «Saya tinggal di Bangsar dengan suami saya.»',
            '9. «Kami tinggal di Bangsar dengan keluarga kami.»',
            '10. «Saya tinggal di Mont Kiara dengan keluarga saya.»',
            'Now read the combinations that are not printed. In table 3, use «kami» with «keluarga kami».'])],
        key=['All combinations are correct. In table 3 the owner word follows the subject: «Kami … keluarga kami».']))
    C.append(dict(
        slug='drill-2-substitution', type='Drill', sub_type='substitute', title='Drill 2 · Substitution', block='B', minutes=3,
        grammar=[G['place'], G['fam'], G['like'], G['an']], patterns=['ms-c02-f06', 'ms-c02-f07'], goal=GOALS['B'],
        explain=('（　）の言葉を入れて言いかえます。前の答えが次の文のもとになります。',
                 'Replace one part with the cue. Each answer becomes the next starting sentence.'),
        sections=[('Change one part · 一つだけ変える', [
            'Start: «Saya tinggal di Mont Kiara dengan isteri saya.»',
            '1. ( Bangsar ) → ____________________', '2. ( «suami» ) → ____________________',
            '3. ( «keluarga» ) → ____________________', '4. ( «anak» ) → ____________________',
            '5. ( «dia» ) → ____________________', '6. ( «mereka» ) → ____________________',
            'Start: «Saya suka masakan Malaysia.»',
            '7. ( «makanan» ) → ____________________', '8. ( «Jepun» ) → ____________________',
            '9. ( «minuman» ) → ____________________', '10. ( «dia» ) → ____________________',
            'Start: «Hobi saya karaoke.»',
            '11. ( «golf» ) → ____________________', '12. ( your own hobby word ) → ____________________'])],
        key=['1 «Saya tinggal di Bangsar dengan isteri saya.» 2 «… dengan suami saya.» 3 «… dengan keluarga saya.» 4 «… dengan anak saya.»',
             '5 «Dia tinggal di Bangsar dengan anaknya.» (or «anak dia») 6 «Mereka tinggal di Bangsar dengan anak mereka.»',
             '7 «Saya suka makanan Malaysia.» 8 «Saya suka makanan Jepun.» 9 «Saya suka minuman Jepun.» 10 «Dia suka minuman Jepun.»',
             '11 «Hobi saya golf.» 12 «Hobi saya …» with any word from the hobby word bank.']))
    C.append(dict(
        slug='drill-3-transformation', type='Drill', sub_type='transform', title='Drill 3 · Transformation', block='B', minutes=4,
        grammar=[G['kah'], G['pe'], G['nya'], G['like']], patterns=['ms-c02-f04', 'ms-c02-f07', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('指示どおりに形を変えます（文から «Adakah» の質問へ、-kah、«Bolehkah»、«-nya»、pe- の語、肯定から否定へ）。',
                 'Change the form as the cue says: statement to an «Adakah» question, -kah, «Bolehkah», «-nya», a pe- word, positive to negative.'),
        sections=[('Change the form · 形を変える', [
            '1. Formal yes/no question: «Encik orang Jepun.» → ____________________',
            '2. Formal yes/no question: «Dia pelajar.» → ____________________',
            '3. Formal: «Siapa nama encik?» → ____________________',
            '4. Formal: «Apa nama syarikat puan?» → ____________________',
            '5. Formal: «Pejabat encik di mana?» → ____________________',
            '6. Ask permission: «Saya tanya.» → ____________________',
            '7. Use «-nya»: «Isteri dia orang Malaysia.» → ____________________',
            '8. Say what he is (a pe- word): «Dia belajar di universiti.» → ____________________',
            '9. Make it negative: «Saya suka makanan ini.» → ____________________'])],
        key=['1 «Adakah encik orang Jepun?» 2 «Adakah dia pelajar?» 3 «Siapakah nama encik?» 4 «Apakah nama syarikat puan?» 5 «Di manakah pejabat encik?»',
             '6 «Bolehkah saya tanya?» 7 «Isterinya orang Malaysia.» 8 «Dia pelajar.» 9 «Saya tidak suka makanan ini.»',
             '«tidak» negates verbs and adjectives; nouns take ‹bukan› (chapter 3).']))
    C.append(dict(
        slug='drill-4-question-answer', type='Drill', sub_type='question and answer', title='Drill 4 · Question and answer', block='B', minutes=4,
        grammar=[G['place'], G['fam'], G['like'], G['kah']], patterns=['ms-c02-f04', 'ms-c02-f06', 'ms-c02-f07', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('前半は自分のことで答えます。後半は答えを聞いて、それに合う質問を言います。',
                 'Part 1: answer about yourself. Part 2: hear the answer and ask the question that fits.'),
        sections=[('Part 1 · Answer · 答える', [
            '1. «Encik kerja di mana?» → ____________________', '2. «Encik tinggal di mana?» → ____________________',
            '3. «Encik ada anak?» → ____________________', '4. «Apa hobi encik?» → ____________________']),
            ('Part 2 · Reverse · 質問を言う', [
            '5. ____________________ → «Saya jurutera.»', '6. ____________________ → «Saya tinggal dengan keluarga saya.»',
            '7. ____________________ → «Boleh.»', '8. ____________________ → «Ya, saya pelajar.»'])],
        key=['1 «Saya kerja di …» 2 «Saya tinggal di …» 3 «Ada.» / «Tidak ada.» 4 «Saya suka …» / «Hobi saya …»',
             '5 «Apa kerja encik?» 6 «Encik tinggal dengan siapa?» 7 «Bolehkah saya tanya?» (any «Bolehkah» question) 8 «Adakah cik pelajar?» (or «Cik pelajar?»)']))
    C.append(dict(
        slug='drill-5-question-word-choice', type='Drill', sub_type='question-word choice', title='Drill 5 · Question-word choice', block='B', minutes=3,
        grammar=[G['kah'], 'ms-c02-g04'], patterns=['ms-c02-f08'], goal=GOALS['B'],
        explain=('第2章までのすべての疑問詞から、答えに合うものを選びます。',
                 'Choose from every question word so far to fit the answer.'),
        sections=[('Choose · 選ぶ', [
            'Box: «apa» / «siapa» / «di mana» / «Apakah» / «Siapakah» / «di manakah» / «Adakah» / «Bolehkah»',
            '1. «___ nama syarikat encik?» — «Sakura.» (formal)', '2. «___ encik orang Jepun?» — «Ya.»',
            '3. «___ saya tanya?» — «Boleh.»', '4. «Encik tinggal ___ ?» — «Di Bangsar.»',
            '5. «Puan tinggal dengan ___ ?» — «Dengan suami saya.»', '6. «___ pejabat cik?» — «Di Kuala Lumpur.» (formal)',
            '7. «___ nama guru awak?» — «Puan Siti.» (formal)', '8. «___ hobi dia?» — «Dia suka masakan Jepun.»',
            '9. «___ khabar?» — «Baik.»',
            'Question-word set for chapter 2 (charter section 14): «siapa», «apa», «di mana», the -kah forms, «adakah», «bolehkah»; with «apa» from chapter 1.'])],
        key=['1 «Apakah» 2 «Adakah» 3 «Bolehkah» 4 «di mana» 5 «siapa» 6 «Di manakah» 7 «Siapakah» 8 «Apa» (or «Apakah») 9 «Apa»']))
    C.append(dict(
        slug='drill-6-short-dialogue', type='Drill', sub_type='free', title='Drill 6 · Short dialogues', block='B', minutes=3,
        grammar=[G['place'], G['fam'], G['like'], G['kah']], patterns=['ms-c02-f04', 'ms-c02-f06', 'ms-c02-f07', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('場面のヒントで二行の会話を読み、もう一行を自分で足します。役を交代しましょう。',
                 'Read the two lines in the cued situation, then add one more line of your own. Swap roles.'),
        sections=[('Two turns, then add one · 二行＋一行', [
            'Dialogue 1 · a networking event, a man you have just met',
            'A: «Encik kerja di mana?»  B: «Saya kerja di syarikat Sakura. Encik pula?»  A: ____________________',
            'Dialogue 2 · a new neighbour at the lift',
            'A: «Puan tinggal dengan siapa?»  B: «Dengan suami dan anak saya.»  A: ____________________',
            'Dialogue 3 · in class, you have a question',
            'A: «Bolehkah saya tanya, Cikgu?»  B: «Boleh. Apa soalan awak?»  A: ____________________',
            'Dialogue 4 · lunch with a colleague your age',
            'A: «Awak suka masakan Malaysia?»  B: «Suka! Awak pula?»  A: ____________________'])],
        key=['Possible third lines: 1 «Saya kerja di syarikat Jepun. Saya jurutera.» 2 «Oh, saya pun tinggal dengan keluarga saya.» '
             '3 «Apakah jawapan soalan ini?» 4 «Saya pun suka masakan Malaysia!»',
             'Accept any third line that fits the person and the turn before it.']))
    C.append(dict(
        slug='drill-question-word-set', type='Drill', sub_type='question-word set', title='Cumulative question-word drill', block='D', minutes=5,
        grammar=[G['kah'], 'ms-c02-g04', 'ms-c01-g04'], patterns=['ms-c01-f02', 'ms-c02-f02', 'ms-c02-f08'], goal=GOALS['D'],
        explain=('第1章と第2章のすべての疑問詞を使って、まず丁寧に、次にくだけた形でインタビューします。',
                 'Interview your partner with every question word from chapters 1 and 2: first formally, then informally.'),
        sections=[('Formal, then informal · 丁寧に、次にくだけて', [
            'Set to date: «apa»; «siapa», «di mana»; «Siapakah», «Apakah», «di manakah»; «adakah», «bolehkah».',
            '1. permission to ask → ____________________', '2. their name (formal) → ____________________',
            '3. their company (formal) → ____________________', '4. where their office is (formal) → ____________________',
            '5. whether they are Japanese (formal) → ____________________', '6. who they live with → ____________________',
            '7. where they live → ____________________', '8. how they are → ____________________',
            'Now ask the same questions informally, to a classmate your age, with «awak» and no -kah.'])],
        key=['1 «Bolehkah saya tanya?» 2 «Siapakah nama encik?» 3 «Apakah nama syarikat encik?» 4 «Di manakah pejabat encik?»',
             '5 «Adakah encik orang Jepun?» 6 «Encik tinggal dengan siapa?» 7 «Encik tinggal di mana?» 8 «Apa khabar?»',
             'Informal: «Siapa nama awak?» «Pejabat awak di mana?» «Awak orang Jepun?»']))

    # Model conversation ------------------------------------------------
    model = [('Siti', '«Selamat petang, kelas! Encik Tanaka, encik kerja di mana?»'), ('Tanaka', '«Saya kerja di syarikat Sakura. Saya jurutera.»'),
             ('Siti', '«Di manakah pejabat encik?»'), ('Tanaka', '«Pejabat saya di Kuala Lumpur.»'),
             ('Siti', '«Encik tinggal di mana?»'), ('Tanaka', '«Saya tinggal di Mont Kiara dengan isteri dan anak saya.»'),
             ('Siti', '«Wah! Adakah anak encik pelajar?»'), ('Tanaka', '«Ya. Dia belajar di sekolah Jepun.»'),
             ('Siti', '«Apa hobi encik?»'), ('Tanaka', '«Saya suka masakan Malaysia. Saya juga suka main dengan anak saya.»'),
             ('Siti', '«Terima kasih, Encik Tanaka. Cik Yuki pula?»'), ('Yuki', '«Saya pelajar. Saya belajar di Universiti Malaya.»'),
             ('Tanaka', '«Bolehkah saya tanya, Cik Yuki? Cik tinggal dengan siapa?»'), ('Yuki', '«Saya tinggal dengan kawan saya di Bangsar.»')]
    gapped = [('Siti', '«Selamat petang, kelas! Encik Tanaka, encik ___ di mana?»'), ('Tanaka', '«Saya kerja di ___ Sakura. Saya jurutera.»'),
              ('Siti', '«___ pejabat encik?»'), ('Tanaka', '«Pejabat saya di Kuala Lumpur.»'),
              ('Siti', '«Encik ___ di mana?»'), ('Tanaka', '«Saya tinggal di Mont Kiara ___ isteri dan anak saya.»'),
              ('Siti', '«Wah! ___ anak encik pelajar?»'), ('Tanaka', '«Ya. Dia ___ di sekolah Jepun.»'),
              ('Siti', '«Apa ___ encik?»'), ('Tanaka', '«Saya ___ masakan Malaysia. Saya juga suka main dengan anak saya.»'),
              ('Siti', '«Terima kasih, Encik Tanaka. Cik Yuki pula?»'), ('Yuki', '«Saya ___ . Saya belajar di Universiti Malaya.»'),
              ('Tanaka', '«___ saya tanya, Cik Yuki? Cik tinggal dengan siapa?»'), ('Yuki', '«Saya tinggal dengan kawan saya di Bangsar.»')]
    variant = [('Rahman', '«Selamat pagi, Puan Sato. Puan kerja di mana?»'),
               ('Sato', '«Saya kerja di syarikat Jepun di Petaling Jaya. Saya jurutera.»'),
               ('Rahman', '«Di manakah rumah puan?»'), ('Sato', '«Rumah saya di Subang Jaya.»'),
               ('Rahman', '«Puan tinggal dengan siapa?»'), ('Sato', '«Saya tinggal dengan suami saya.»'),
               ('Rahman', '«Adakah suami puan orang Jepun?»'), ('Sato', '«Ya. Dia guru di sekolah Jepun.»'),
               ('Rahman', '«Apa hobi puan?»'), ('Sato', '«Saya suka makanan Malaysia. Suami saya suka bacaan Jepun.»'),
               ('Rahman', '«Terima kasih, Puan Sato. Ada soalan?»'), ('Sato', '«Ada. Bolehkah saya tanya? Di manakah pejabat encik?»'),
               ('Rahman', '«Pejabat saya di Cyberjaya.»'), ('Sato', '«Terima kasih, Encik Rahman.»')]
    C.append(dict(
        slug='model-conversation', type='Model conversation', title='Model conversation', block='B', minutes=15,
        grammar=ALL, patterns=['ms-c02-f04', 'ms-c02-f05', 'ms-c02-f06', 'ms-c02-f07', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('マレー語クラスでの会話（14ターン）です。ペアで読み、次に空欄版、最後に事実を変えた版（ビジネスの交流会）を演じます。',
                 'A Malay class, in 14 turns. Read it in pairs, then the gapped version, then the variant with changed facts (a business event).'),
        sections=[('1 · Model: the Malay class · マレー語クラスで', turns(model)),
                  ('2 · Gapped version · 空欄版', turns(gapped)),
                  ('3 · Variant: changed facts · 事実を変えた版', ['Now «Encik» Rahman meets «Puan» Sato, an engineer from another company, at a business event. He asks formal questions.', *turns(variant),
                    'Change two more facts yourselves (a job, a home) and play it again.'])],
        key=['Gaps in order: «kerja», «syarikat», «Di manakah», «tinggal», «dengan», «Adakah», «belajar», «hobi», «suka», «pelajar», «Bolehkah».',
             'Variant check: formal questions with -kah and «Adakah» suit a first business meeting; «Puan» as "you" throughout.']))

    script = ['Tanaka: «Selamat petang. Nama saya Tanaka Kenji. Saya orang Jepun. Kampung saya di Osaka.»',
              'Tanaka: «Saya kerja di syarikat Sakura di Kuala Lumpur. Saya jurutera.»',
              'Tanaka: «Saya tinggal di Mont Kiara dengan keluarga saya. Ini isteri saya. Namanya Emi. Dia guru. Dia kerja di sekolah Jepun.»',
              'Tanaka: «Ini anak kami, Hiro. Dia pelajar. Dia belajar di sekolah Jepun juga.»',
              'Tanaka: «Saya suka makanan Malaysia. Isteri saya suka masakan Malaysia. Hiro suka main dengan kawan. Terima kasih.»',
              'Aini: «Terima kasih, Encik Tanaka. Bolehkah saya tanya? Adakah Puan Emi orang Jepun juga?»',
              'Tanaka: «Ya, dia orang Jepun. Kampung dia di Kyoto.»',
              'Aini: «Hiro suka sekolah dia?»', 'Tanaka: «Ya, dia suka. Dia ada kawan di sekolah.»',
              'Aini: «Encik suka kerja di Kuala Lumpur?»', 'Tanaka: «Ya, saya suka. Rakan sekerja saya baik.»',
              'Aini: «Wah! Selamat datang, keluarga Tanaka. Selamat berkenalan.»']
    C.append(dict(
        slug='listening', type='Listening', title='Listening focus · The Tanaka family', block='C', minutes=15,
        grammar=[G['place'], G['fam'], G['like'], G['kah'], G['pe']], goal=GOALS['C'],
        explain=('コンドミニアムの住民の集まりで、田中さんが自分と家族を紹介します。仕事・家・家族・好きなことを聞き取りましょう。台本は先生用のページにあります。',
                 'At a residents\' get-together at his condo, «Encik» Tanaka introduces himself and his family. Listen for work, home, family and likes. '
                 'The script is on the teacher page.'),
        sections=[('Before listening · 聞く前に', [
            'Copy the table. Guess one thing about each person before you listen.',
            'Person | job | where | likes', 'Tanaka | ________ | ________ | ________', 'Emi | ________ | ________ | ________',
            'Hiro | ________ | ________ | ________']),
            ('While listening · 聞きながら', [
            '1. Fill in the table.', '2. Where is Tanaka\'s company?', '3. Where does the family live?',
            '4. What is Emi\'s job, and where does she work?', '5. What is Hiro, and where does he study?',
            '6. Who likes Malaysian cooking?', '7. What does Aini ask permission for, and what does she ask?',
            '8. Where is Emi\'s hometown?', '9. Does Tanaka like working in Kuala Lumpur? Why?']),
            ('After listening · 聞いたあとで', [
            'Close the table. Tell your partner about the Tanaka family in four sentences: «Encik Tanaka …», «Isterinya …», «Anak mereka …»',
            'Then introduce your own family, or a family you know, in the same way.',
            '表を閉じて、田中さん一家について四文で話しましょう。次に自分の家族（または知っている家族）を同じように紹介します。'])],
        key=[f'Teacher script (read twice). Malay words: {malay_words(script)}.', *script,
             'Table: Tanaka: engineer, Sakura company in Kuala Lumpur, Malaysian food; Emi: teacher, Japanese school, Malaysian cooking; Hiro: student, Japanese school, playing with friends.',
             '2 Kuala Lumpur 3 Mont Kiara 4 teacher («guru»), at a Japanese school 5 a student («pelajar»), at a Japanese school 6 Emi '
             '7 to ask a question («Bolehkah saya tanya?»); whether Emi is Japanese too 8 Kyoto 9 yes; his colleagues are nice («Rakan sekerja saya baik»)']))

    C.append(dict(
        slug='reading-writing', type='Reading and writing', title='Reading and writing · A new colleague\'s message', sub_type='message',
        block='C', minutes=10, grammar=[G['place'], G['fam'], G['like'], G['kah']], goal=GOALS['C'],
        explain=('新しい同僚がチームのチャットに書いた自己紹介と返信を読み、質問に答えます。次に、自分の自己紹介の返信を書きます。',
                 'Read a new colleague\'s self-introduction in the team chat and two replies. Answer the questions, then write your own reply.'),
        sections=[('Read · 読む', [
            'Sato: «Selamat pagi! Nama saya Sato Yuki. Saya orang Jepun. Asal saya dari Nagoya. Saya jurutera di pejabat Kuala Lumpur. '
            'Saya tinggal di Subang Jaya dengan suami saya. Suami saya guru. Dia kerja di sekolah Jepun. Kami suka masakan Malaysia! '
            'Bolehkah kita jumpa di pejabat nanti? Terima kasih.»',
            'Rahman: «Selamat datang, Puan Sato! Saya Rahman. Saya pengurus pejabat ini.»',
            'Mei Ling: «Selamat berkenalan! Saya pun suka masakan Malaysia. Jom!»']),
            ('Questions · 質問', [
            '1. Where is Sato from?', '2. What is her job?', '3. Where does she live, and with whom?',
            '4. What is her husband\'s job?', '5. What do Sato and her husband like?', '6. What does Sato ask at the end?',
            '7. Who is Rahman?']),
            ('Write · 書く', [
            'Reply to Sato. Greet her, then say your name, where you work or study, where you live and with whom, and what you like.',
            '____________________________________________', '____________________________________________',
            '____________________________________________',
            'Check: «kerja di» or «belajar di»; «tinggal di … dengan …»; «suka» before what you like.'])],
        key=['1 Nagoya, Japan. 2 an engineer («jurutera»). 3 in Subang Jaya, with her husband. 4 a teacher («guru») at a Japanese school. 5 Malaysian cooking.',
             '6 whether they can meet at the office later («Bolehkah kita jumpa …»). 7 the office manager («pengurus»).',
             'Model reply: «Selamat pagi, Puan Sato! Nama saya Kimura. Saya kerja di syarikat Sakura. Saya tinggal di Bangsar dengan isteri saya. '
             'Saya suka makanan Jepun dan masakan Malaysia. Selamat berkenalan!»']))

    C.append(dict(
        slug='task', type='Task', title='Task · Find two things in common', sub_type='role-play', block='C', minutes=15,
        grammar=ALL, goal=GOALS['C'],
        explain=('役割カードを使って、共通点を二つ見つけます。途中で予定の変更があり、丁寧な質問に切りかえます。',
                 'Use the role cards to find two things you have in common. A change of plan moves you to formal questions.'),
        sections=[('Role card A · 日本人の会社員', [
            'You: an engineer at a Japanese company in Kuala Lumpur. You live in Mont Kiara with your family. You like Malaysian cooking.',
            'Ask B about work, home, family and likes. Find two things you have in common.',
            'あなた：クアラルンプールの日本の会社のエンジニア。家族とモントキアラに住んでいて、マレーシア料理が好き。Bに仕事・家・家族・好きなことをたずね、共通点を二つ見つけます。']),
            ('Role card B · マレーシア人の同僚', [
            'You: a teacher at a school in Mont Kiara. You live with your husband or wife and your child. You like Japanese food and Malaysian cooking.',
            'Answer A\'s questions and ask the same back. Say which things you have in common.',
            'あなた：モントキアラの学校の先生。配偶者と子どもと住んでいて、日本料理とマレーシア料理が好き。Aの質問に答え、同じ質問を返し、共通点を言います。']),
            ('Change of plan · 予定の変更', [
            'Now B is the manager of a language school and A is applying for the Malay class. B asks the same questions formally, with -kah, «Adakah» and «Bolehkah».',
            'Bは語学学校の責任者、Aはマレー語クラスの申込者になりました。Bは -kah・«Adakah»・«Bolehkah» を使って丁寧に同じ質問をします。']),
            ('Success criteria · 先生が確認すること', [
            '☐ Work, home, family and likes are asked and answered.', '☐ «kerja di», «tinggal di … dengan …», «suka …» are correct.',
            '☐ Two things in common are found and said with «pun» or «juga».',
            '☐ After the change, B uses at least three formal questions (-kah, «Adakah», «Bolehkah»).', '☐ The right "you" throughout.'])],
        key=['Sample: A «Awak kerja di mana?» B «Saya kerja di sekolah. Saya guru.» A «Awak tinggal di mana?» B «Di Mont Kiara.» A «Saya pun tinggal di Mont Kiara!»',
             'Formal: B «Siapakah nama encik?» «Di manakah pejabat encik?» «Adakah encik tinggal dengan keluarga encik?» «Bolehkah saya tanya, apakah hobi encik?»']))

    culture_en = [
        'Malay builds new words from roots, and two of the first patterns are pe- and -an. pe- names the person who does something: '
        '‹kerja› (work) gives «pekerja» (worker), ‹ajar› (teach) gives «pelajar» (student), ‹lawat› (visit) gives «pelawat» (visitor), '
        '‹lancong› (tour) gives «pelancong» (tourist) and ‹tani› (farming) gives «petani» (farmer). With some roots the sound changes: '
        '‹pandu› gives «pemandu» (driver) and ‹urus› gives «pengurus» (manager).',
        '-an names the thing: ‹makan› gives «makanan» (food), ‹minum› «minuman» (drink), ‹masak› «masakan» (cooking), ‹baca› «bacaan» '
        '(reading material) and ‹tulis› «tulisan» (writing). ‹jawab› becomes «jawapan», with b turning into p.',
        'Learn these as words first; the rule helps you guess new ones on signs. «Pelawat», for example, appears on visitor badges.',
        'Two words have an everyday and a formal partner. «Cikgu» is the everyday word for teacher and «guru» the more formal one. '
        '«Kerja» is natural in speech; in formal writing it becomes ‹bekerja›, which you will meet with the ber- verbs in chapter 10.',
        'The -kah questions sound formal. You will see «Siapakah», «Apakah» and «Adakah» on forms and hear them in announcements and interviews. '
        'In conversation, a rising voice is enough.']
    C.append(dict(
        slug='culture-note', type='Culture note', title='Culture and word-origin note · Building words', block='E', minutes=10,
        grammar=[G['pe'], G['an'], G['kah']], goal=GOALS['E'],
        explain=('pe- と -an による語の作り方、日常語と改まった語、-kah の使われ方を読みます（英語と日本語）。',
                 'Read how pe- and -an build words, which words are everyday and which formal, and where -kah questions are used (English and Japanese).'),
        sections=[('English', culture_en),
                  ('日本語', [
                      'マレー語は語根から新しい語を作ります。最初に学ぶ形が pe- と -an です。pe- は「それをする人」を表します：‹kerja›（仕事）→«pekerja»（従業員）、'
                      '‹ajar›（教える）→«pelajar»（学生）、‹lawat›（訪ねる）→«pelawat»（訪問者）、‹lancong›（旅行）→«pelancong»（観光客）、‹tani›（農業）→«petani»（農家）。'
                      '音が変わる語もあります：‹pandu›→«pemandu»（運転手）、‹urus›→«pengurus»（マネージャー）。',
                      '-an は「もの」を表します：‹makan›→«makanan»（食べ物）、‹minum›→«minuman»（飲み物）、‹masak›→«masakan»（料理）、‹baca›→«bacaan»（読み物）、'
                      '‹tulis›→«tulisan»（書いたもの）。‹jawab› は b が p に変わって «jawapan» になります。',
                      'まずは単語として覚えましょう。ルールを知っていると、看板の新しい語も推測できます。たとえば «Pelawat» は来客用の名札に書かれています。',
                      '日常語と改まった語の組もあります。先生は日常では «Cikgu»、改まると «guru»。«Kerja» は会話では自然ですが、改まった書き言葉では ‹bekerja› になり、'
                      '第10章の ber- 動詞で学びます。',
                      '-kah の質問は改まって聞こえます。«Siapakah»・«Apakah»・«Adakah» は書類で見たり、アナウンスや面接で聞いたりします。会話では文末を上げるだけで十分です。'])],
        key=['Sources: Kata-Kata card notes ms-c02-030 and 047 to 063, and the ledger meanings. Sam\'s own etymology notes were not available to the builder; add them here when supplied.',
             f'English text: {english_words(culture_en)} words. Discussion: guess the meaning of a new -an word from its root, e.g. «latihan» from ‹latih›.']))

    tests = [
        dict(sub_type='listening', prompt='L1. Listen. What is the person\'s job?', answer='Teacher reads: «Saya jurutera.» Answer: engineer',
             words=['jurutera'], grammar=[G['place']]),
        dict(sub_type='listening', prompt='L2. Listen. Where does the person live?', answer='Teacher reads: «Saya tinggal di Bangsar.» Answer: Bangsar',
             words=['tinggal', 'di'], grammar=[G['place']]),
        dict(sub_type='listening', prompt='L3. Listen. Who does the person live with?', answer='Teacher reads: «Saya tinggal dengan suami saya.» Answer: her husband',
             words=['dengan', 'suami'], grammar=[G['fam']]),
        dict(sub_type='listening', prompt='L4. Listen. What does the person like?', answer='Teacher reads: «Saya suka makanan Jepun.» Answer: Japanese food',
             words=['suka', 'makanan'], grammar=[G['like'], G['an']]),
        dict(sub_type='listening', prompt='L5. Listen and choose the answer: a «Boleh.» b «Di Kuala Lumpur.» c «Nama saya Siti.»',
             answer='Teacher reads: «Bolehkah saya tanya?» Answer: a', words=['bolehkah', 'boleh'], grammar=[G['kah']]),
        dict(sub_type='grammar', prompt='V1. Formal: «___ encik orang Jepun?» — «Ya.»', answer='«Adakah»', words=['adakah'], grammar=[G['kah']]),
        dict(sub_type='grammar', prompt='V2. Formal: «___ pejabat puan?» — «Di Kuala Lumpur.»', answer='«Di manakah»', words=['di manakah'], grammar=[G['kah']]),
        dict(sub_type='words', prompt='V3. A person who studies: ‹ajar› → ________', answer='«pelajar»', words=['pelajar'], grammar=[G['pe']]),
        dict(sub_type='words', prompt='V4. Something you drink: ‹minum› → ________', answer='«minuman»', words=['minuman'], grammar=[G['an']]),
        dict(sub_type='grammar', prompt='V5. Put in order: «di / kerja / saya / syarikat Jepun»', answer='«Saya kerja di syarikat Jepun.»',
             words=['kerja', 'syarikat'], grammar=[G['place']]),
        dict(sub_type='grammar', prompt='V6. "My child": ________', answer='«anak saya»', words=['anak'], grammar=[G['fam']]),
        dict(sub_type='grammar', prompt='V7. Make it negative: «Saya suka minuman ini.»', answer='«Saya tidak suka minuman ini.»',
             words=['suka', 'tidak'], grammar=[G['like']]),
        dict(sub_type='words', prompt='V8. Everyday word for teacher: ________', answer='«cikgu»', words=['cikgu'], grammar=[G['pe']]),
        dict(sub_type='reading', prompt='R1. Read the message above. What is Ali\'s job?', answer='a driver («pemandu»)', words=['pemandu'], grammar=[G['pe']]),
        dict(sub_type='reading', prompt='R2. Where does he live, and with whom?', answer='in Ipoh, with his wife and child', words=['tinggal', 'dengan', 'isteri', 'anak'],
             grammar=[G['place'], G['fam']]),
        dict(sub_type='reading', prompt='R3. What is his wife\'s job?', answer='a teacher («guru»)', words=['guru'], grammar=[G['place']]),
        dict(sub_type='reading', prompt='R4. What does he ask at the end?', answer='whether he can ask a question («Bolehkah saya tanya?»)', words=['bolehkah'],
             grammar=[G['kah']]),
        dict(sub_type='speaking', prompt='S1. Speaking: your teacher interviews you for a Malay class. Answer about your work, home, family and likes, then ask two formal questions back.',
             answer='Check: «Saya kerja di …»; «Saya tinggal di … dengan …»; «Saya suka …»; two of «Siapakah», «Apakah», «di manakah», «Adakah», «Bolehkah».',
             words=['kerja', 'tinggal', 'suka', 'adakah'], grammar=[G['place'], G['fam'], G['like'], G['kah']]),
    ]
    C.append(dict(
        slug='test', type='Test', title='Unit test and self-check', block='D', minutes=20, grammar=ALL, goal=GOALS['D'], tests=tests,
        explain=('10分の小テストです（点数より確認のため）。聞く・単語と文法・読む、そして話す課題が一つあります。最後に「できる」チェックをします。',
                 'A ten-minute, low-stakes check: listening, words and grammar, reading, and one speaking task. Then tick the "I can" list.'),
        sections=[('Listening · 聞く (teacher reads each line twice)', [t['prompt'] for t in tests if t['sub_type'] == 'listening']),
                  ('Words and grammar · 単語と文法', [t['prompt'] for t in tests if t['sub_type'] in ('words', 'grammar')]),
                  ('Reading · 読む', ['Message: «Selamat petang. Nama saya Ali. Saya pemandu. Saya tinggal di Ipoh dengan isteri dan anak saya. '
                                      'Isteri saya guru. Bolehkah saya tanya? — Ali»',
                                      *[t['prompt'] for t in tests if t['sub_type'] == 'reading']]),
                  ('Speaking · 話す', [t['prompt'] for t in tests if t['sub_type'] == 'speaking']),
                  ('Self-check · できるチェック', [f'☐ {GOALS[b]} / {GOALS_JA[b]}' for b in 'ABCE'] + [
                      '☐ ' + WRITING_GOAL, 'One thing I will practise in Kata-Kata this week: ____________________'])],
        key=[f'{t["prompt"].split(".")[0]}: {t["answer"]}' for t in tests] + ['Low-stakes: note missed items for the chapter 3 recall.']))

    C.append(dict(
        slug='teaching-plan', type='Teaching plan', title='Teaching plan and answer key', block='All', minutes=None, grammar=ALL,
        patterns=['ms-c02-f04', 'ms-c02-f05', 'ms-c02-f06', 'ms-c02-f07', 'ms-c02-f08'],
        explain=('先生用：五つのブロック（各45分）と書くブロックの時間配分、指示、予想される答え、Kata-Kata の宿題。',
                 'For the teacher: timings for the five 45-minute blocks and the writing block, prompts, expected answers and Kata-Kata homework.'),
        sections=[
            ('Before and after · 授業の前後', [
                'Before Block A: the Kata-Kata chapter 2 cards for work, home and family (ms-c02-029 to 063); collect Tanya Cikgu questions.',
                'Before Block E: the Dunia scene "Pagi di pejabat" (cards ms-d-pejabat-pagi-01 to 14).',
                'After Block D: spaced review of all chapter 2 cards; preview Sedia Kelas c03 (numbers). Planning figure: about 3 hours of Kata-Kata for this unit.',
                'Hanashishou starts at A2: no link yet. Audio: teacher-read scripts only.']),
            ('Block A · Words and patterns (45 min)', [
                'Goal: ' + GOALS['A'],
                '0–5 Recall (Opener): name, nationality, hometown, then introduce a partner.',
                '5–10 Tanya Cikgu. 10–20 Vocabulary: say a root, learners give the pe- or -an word. Expected: ‹tulis› → «tulisan».',
                '20–40 Patterns 1 to 5. Prompt: "Where do you work?" Expected: «Saya kerja di …». Ask for a hobby word each learner needs and write it on the board as a personal word.',
                '40–45 First substitutions: Drill 2, items 1 to 4.']),
            ('Block B · Drills and conversation (45 min)', [
                'Goal: ' + GOALS['B'],
                '0–5 Recall: "Ask me formally where my office is." Expected: «Di manakah pejabat puan?»',
                '5–25 Drill ladder, types 1 to 6. 25–40 Model conversation, gapped version, business-event variant. 40–45 Pair rehearsal.']),
            ('Block C · Listening and task (45 min)', [
                'Goal: ' + GOALS['C'],
                '0–5 Recall: "Who do you live with?" Expected: «Saya tinggal dengan …».',
                '5–20 Listening: table, script twice (on the listening key), questions. 20–30 Reading: Sato\'s message and the reply.',
                '30–45 Task: role cards; switch to the formal interview at minute 37.']),
            ('Block D · Review and test (45 min)', [
                'Goal: ' + GOALS['D'],
                '0–15 Mixed review: cumulative question-word drill, formal then informal; recycle chapter 1 greetings at the start of each interview.',
                '15–25 Unit test. 25–35 Self-check and feedback. 35–45 Preview Sedia Kelas c03.']),
            ('Block E · Scene (45 min)', [
                'Goal: ' + GOALS['E'],
                '0–5 Recall: "Ask permission to print." Expected: «Bolehkah saya cetak?»',
                '5–15 Scene listening: play or read the Kata-Kata Dunia scene "Pagi di pejabat". 15–30 Role-play it in pairs.',
                '30–40 Free variation: the boss is on leave («cuti») and a colleague is busy («sibuk»). 40–45 Culture note. No Hanashishou link at A1.']),
            ('Writing block (45 min)', [
                'Goal: ' + WRITING_GOAL,
                '0–5 Recall the four questions (work, home, family, likes). 5–15 Read the model form and paragraph.',
                '15–30 Learners fill in the form, then write five or six sentences. 30–40 Pairs swap and check with the checklist. 40–45 Read aloud.']),
            ('What to listen for · 注意点', [
                '«di» before places; the owner after the thing; «suka» before what is liked; -kah on the question word, not at the end.',
                'Hobby words are the learner\'s own: write them on the board as personal words, not as chapter vocabulary. Raised with Sam for the ledger.',
                '«pemandu» and «pengurus» are recognise-only. The office words from "Pagi di pejabat" are for recognition first.'])],
        key=['Answer keys are on each component\'s teacher page. This plan follows the block timings in charter section 6.',
             'All Japanese in this unit is a draft awaiting native review.']))

    C.append(dict(
        slug='writing-block', type='Reading and writing', sub_type='form', title='Writing block · Self-introduction form', block='Skills', minutes=45,
        grammar=[G['place'], G['fam'], G['like'], 'ms-c02-g03', 'ms-c02-g05'], goal=WRITING_GOAL, skills=['writing', 'reading'],
        explain=('自己紹介の用紙を読んで記入し、それをもとに短い自己紹介文を書きます。最後にペアで確認します。',
                 'Read a model self-introduction form, fill in your own, then turn it into a short self-introduction. Check it with a partner.'),
        sections=[
            ('1 · Model form · 記入例', [
                '«Nama:» Sato Yuki', '«Negara:» «Jepun»', '«Kampung:» Nagoya', '«Tinggal di:» Subang Jaya',
                '«Kerja / belajar di:» «syarikat» Sakura («jurutera»)',
                '«Keluarga:» «suami»', '«Suka:» «masakan Malaysia»']),
            ('2 · Model paragraph · 例文', [
                '«Nama saya Sato Yuki. Saya orang Jepun. Kampung saya di Nagoya. Saya tinggal di Subang Jaya dengan suami saya. '
                'Saya kerja di syarikat Sakura. Saya jurutera. Saya suka masakan Malaysia.»']),
            ('3 · Your form · 自分の用紙', [
                '«Nama:» ______________________', '«Negara:» ______________________', '«Kampung:» ______________________',
                '«Tinggal di:» ______________________', '«Kerja / belajar di:» ______________________',
                '«Keluarga:» ______________________', '«Suka:» ______________________']),
            ('4 · Your paragraph · 自分の文', [
                'Write five or six sentences from your form.', '____________________________________________',
                '____________________________________________', '____________________________________________',
                '____________________________________________']),
            ('5 · Partner check · ペアで確認', [
                '☐ «Nama saya …» (not «Saya nama …»).', '☐ «orang» before the country.', '☐ «di» before every place.',
                '☐ «dengan» before the people you live with.', '☐ The owner after the thing: «suami saya».', '☐ «suka» before what you like.'])],
        key=['Model answers are on the sheet. Personal hobby words are allowed in the paragraph; mark them as the learner\'s own.',
             'Common slips: «Saya nama …»; «Jepun orang»; a missing «di»; «saya suami» for "my husband".']))
    return C


UNIT = dict(
    unit_id='ms-c02b', label='2B', chapter_id='ms-c02', check_unit='ms-c02b', id_prefix='ms-c02b', title_prefix='Unit 2B',
    header='Unit 2B (ms-c02b)', menu_title='Chapter 2 · Pronouns and self-introduction', genre='Work and study',
    goal='Talk about work, study, home, family and likes; build pe- and -an words; ask formal questions with -kah, adakah and bolehkah.',
    blocks=GOALS, prerequisites=['ms-c01'], prerequisite_units=['ms-c02a'],
    prereq_grammar=['ms-c02-g03', 'ms-c02-g04', 'ms-c02-g05'], word_scope=WORDS, components=components)
