"""Unit 1 (chapter 1): greetings, titles, asking after someone, leave-taking.

Malay is limited to ledger rows placed in chapter 1 (45 rows, ledger refreshed
11 Nov 2026). Kata-Kata frames ms-c01-f01 to f05 are the patterns. Japanese is
a draft awaiting native review.
"""
from . import vocab, malay_words, english_words, pattern, turns

GOALS = {
    'A': 'I can greet people at the right time of day and use the right title.',
    'B': 'I can ask how someone is, answer, and return the question.',
    'C': 'I can follow short greetings when I hear them and read greeting messages.',
    'D': 'I can check my greetings and leave-taking in a short test and say what I can do.',
    'E': 'I can act out a first-day greeting scene and handle a change of plan.',
}
GOALS_JA = {
    'A': '時間帯に合ったあいさつをして、正しい敬称が使える。',
    'B': '相手の様子をたずね、答え、同じ質問を返せる。',
    'C': '短いあいさつを聞いて分かり、あいさつのメッセージが読める。',
    'D': '小テストであいさつと別れの表現を確かめ、できることが言える。',
    'E': '初出勤のあいさつ場面を演じ、予定の変更に対応できる。',
}
WORDS = ['L-0001', 'L-0162', 'L-0002', 'L-0163', 'L-0003', 'L-0164', 'L-0004', 'L-0165', 'L-0005',
         'L-0006', 'L-0028', 'L-0036', 'L-0010', 'L-0011', 'L-0012', 'L-0013', 'L-0014',
         'L-0015', 'L-0983', 'L-0031', 'L-0032', 'L-0033', 'L-0034', 'L-0035', 'L-0016', 'L-0017',
         'L-0018', 'L-0019', 'L-0029', 'L-0030', 'L-0984', 'L-0020', 'L-0021', 'L-0022', 'L-0023',
         'L-0576', 'L-0024', 'L-0672', 'L-0025', 'L-0026', 'L-0007', 'L-0008', 'L-0027', 'L-0499']


def components(ledger):
    C = []
    # 1 · Opener ------------------------------------------------------------
    C.append(dict(
        slug='opener', type='Opener', title='Chapter opener', block='A', minutes=5,
        grammar=['ms-c01-g02', 'ms-c01-g03'], goal=GOALS['A'],
        explain=('この課の目標と場面を確認し、知っているあいさつを思い出します。',
                 'Read the goals and the scene, then recall any Malay greetings you already know.'),
        sections=[
            ('Can-do goals · できること', [
                *[f'Block {b}: {GOALS[b]}' for b in 'ABCDE'],
                *[f'ブロック{b}：{GOALS_JA[b]}' for b in 'ABCDE'],
                'Pronunciation block: I can read greetings aloud using Malay spelling rules. / 発音ブロック：つづりのルールを使ってあいさつを音読できる。']),
            ('The scene · 場面', [
                '«Encik» Tanaka starts work at an office in Kuala Lumpur. On his first day he greets «Puan» Aini at reception, '
                'meets «Cik» Mei Ling and «Encik» Rahman, thanks a «Kakak» at the food stall and says goodbye to the «Pak cik» at the door.',
                '田中さんはクアラルンプールの会社で働き始めます。初日、受付のアイニさんにあいさつし、メイリンさんとラーマンさんに会い、'
                '屋台の店員さんにお礼を言い、帰りに門の警備員さんにあいさつします。',
                'Genre: Social life · ジャンル：社会生活']),
            ('Recall · 思い出そう (5 min)', [
                'There is no earlier chapter. Before class you met this chapter in Kata-Kata (Sedia Kelas set c01).',
                '1. Close your notes. Say every Malay greeting you remember. Your partner counts them.',
                '2. Which greeting fits 8 am? Which fits 9 pm? Say them.',
                '3. Write one question you want to ask (Tanya Cikgu): ____________________',
                '前のレッスンはありません。授業前に Kata-Kata（Sedia Kelas c01）でこの課の単語を見ています。',
                'ノートを閉じて、覚えているあいさつを全部言いましょう。朝8時と夜9時のあいさつはどれですか。']),
            ('Self-study · 自習', [
                'Before class: Kata-Kata Sedia Kelas set c01 (23 cards, frames ms-c01-f01 and f02).',
                'After class: the whole Kata-Kata chapter 1 deck with spaced review. Planning figure: about 3 hours of Kata-Kata per unit.',
                '授業前：Kata-Kata の Sedia Kelas c01。授業後：第1章のカード全部を復習。目安は1ユニット約3時間。']),
        ],
        key=['No fixed answers. Expected recall: «Selamat pagi» (8 am), «Selamat malam» (9 pm); possibly «Apa khabar?», «Terima kasih».',
             'Collect Tanya Cikgu questions for Block A, minutes 5 to 10.']))

    # 2 · Vocabulary --------------------------------------------------------
    C.append(dict(
        slug='vocabulary', type='Vocabulary', title='Vocabulary focus', block='A', minutes=10,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06', 'ms-c01-g08'], goal=GOALS['A'],
        explain=('第1章の台帳の単語45語を、使う場面ごとにまとめました。意味を確認し、例文を声に出して読みましょう。話し言葉の形には spoken と書いてあります。',
                 'All 45 ledger words for chapter 1, grouped by use, each with its meaning and one example. '
                 'Read every example aloud. Spoken forms are marked "spoken".'),
        sections=[('Words by group · 場面別の単語', vocab(ledger, [
            ('Greetings by time of day · 時間帯のあいさつ', [
                ('L-0001', '«Selamat datang, Encik Tanaka.»'),
                ('L-0162', '«Selamat pagi, Puan.»'),
                ('L-0002', '«Selamat pagi, Pak cik!»'),
                ('L-0163', '«Selamat tengah hari, Cik Mei Ling.»'),
                ('L-0003', '«Selamat tengah hari, Abang.»'),
                ('L-0164', '«Selamat petang, Mak cik.»'),
                ('L-0004', '«Selamat petang, Encik Rahman.»'),
                ('L-0165', '«Selamat malam, Kakak.»'),
                ('L-0005', '«Selamat malam, Puan Aini. Jumpa esok.»')]),
            ('Meeting and welcome · 出会いと歓迎', [
                ('L-0006', '«Selamat datang, Encik Kimura!»'),
                ('L-0028', '«Saya Tanaka. Selamat berkenalan.»', dict(display='«Selamat berkenalan» (fixed phrase)')),
                ('L-0036', '«Saya Yamada.»')]),
            ('Asking after someone · 様子をたずねる', [
                ('L-0010', '«Apa khabar, Puan?»'),
                ('L-0011', '«Apa khabar, Cik Mei Ling?»'),
                ('L-0012', '«Apa khabar, Encik Tanaka?»'),
                ('L-0013', '«Saya baik, terima kasih.»'),
                ('L-0014', '«Khabar baik, terima kasih.»'),
                ('L-0015', '«Khabar baik. Encik pula?»'),
                ('L-0983', '«Saya pun baik.»', dict(en='also, too (after the word)'))]),
            ('Titles · 敬称・呼びかけ', [
                ('L-0031', '«Selamat pagi, Encik Rahman.»'),
                ('L-0032', '«Apa khabar, Puan Aini?»'),
                ('L-0033', '«Terima kasih, Cik Mei Ling.»'),
                ('L-0034', '«Terima kasih, Kakak.»', dict(display='«Abang» / «Kakak» (spoken short form: ‹Kak›)')),
                ('L-0035', '«Selamat malam, Pak cik.»', dict(display='«Pak cik» / «Mak cik»'))]),
            ('Thanks, sorry, yes and no · お礼・おわび・はい・いいえ', [
                ('L-0016', '«Terima kasih, Puan.»'),
                ('L-0017', '«Sama-sama, Encik.»'),
                ('L-0018', '«Maaf, Encik Tanaka.»'),
                ('L-0019', '«Maaf, Pak cik, tumpang tanya.»'),
                ('L-0029', '«Ya, saya Tanaka.»'),
                ('L-0030', '«Tidak, saya Kimura.»', dict(display='«tidak»', en='no, not (standard)', ja='いいえ・〜ない（標準形）')),
                ('L-0030', '«Tak, saya Kimura.» (spoken)', dict(display='«tak» (spoken form of «tidak»)', en='no, not (spoken)', ja='いいえ・〜ない（話し言葉）')),
                ('L-0984', '«Oh, Encik Tanaka! Selamat datang.»')]),
            ('Taking leave · 別れのあいさつ', [
                ('L-0020', '«Saya minta diri dulu.»'),
                ('L-0021', '«Jaga diri, Puan.»'),
                ('L-0022', '«Maaf, saya minta diri dulu.»'),
                ('L-0023', '«Saya minta diri dulu, Encik.» (standard form: ‹dahulu›)'),
                ('L-0576', '«Jumpa esok, Cik Mei Ling.»'),
                ('L-0024', '«Jumpa lagi, Abang!»'),
                ('L-0672', '«Terima kasih. Jumpa lagi!»'),
                ('L-0025', '«Selamat malam. Jumpa esok!»'),
                ('L-0026', '«Jumpa nanti, Encik Rahman.»'),
                ('L-0007', '«Selamat jalan, Encik Tanaka!»'),
                ('L-0008', '«Selamat tinggal, Puan Aini.»'),
                ('L-0027', '«Jaga diri, Mak cik.»'),
                ('L-0499', '«Hati-hati, Encik!»')]),
        ]))],
        key=['Kata-Kata cards: ms-c01-001 to ms-c01-038. «saya» is card ms-c02-001; «pagi», «tengah hari», «petang», «malam» are cards ms-c04-008 to 011. '
             'All five were placed in chapter 1 on 11 Nov 2026; the Kata-Kata move is pending.',
             '«pun» (L-0983) and «oh» (L-0984) have no Kata-Kata card yet (pending).',
             'Check in class: say a time (8 am, 1 pm, 5 pm, 9 pm); learners answer with the greeting. Say a person (young woman, older man); learners give the title.',
             'Expected: 8 am «Selamat pagi»; 1 pm «Selamat tengah hari»; 5 pm «Selamat petang»; 9 pm «Selamat malam»; young woman «Cik»; older man «Pak cik».']))

    # 3 · Pattern and grammar -----------------------------------------------
    C.append(dict(
        slug='pattern-grammar', type='Pattern and grammar', title='Pattern and grammar focus', block='A', minutes=20,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06'],
        patterns=['ms-c01-f01', 'ms-c01-f02', 'ms-c01-f03', 'ms-c01-f04', 'ms-c01-f05'], goal=GOALS['A'],
        explain=('五つの文型を、例の質問と答えで練習します。先にペアで例を読み、そのあと説明を読みましょう。',
                 'Five sentence patterns from Kata-Kata, each with question-and-answer examples. Read the examples in pairs first, then the explanation.'),
        sections=[
            pattern(1, 'ms-c01-f01', '«Selamat» ___ , (title) ___ .', [
                'A: «Selamat pagi, Puan Aini.»  B: «Selamat pagi, Encik Tanaka.»',
                'A: «Selamat tengah hari, Cik Mei Ling.»  B: «Selamat tengah hari, Encik Rahman.»',
                'A: «Selamat petang, Pak cik.»  B: «Selamat petang, Encik.»',
                'A: «Selamat malam, Mak cik.»  B: «Selamat malam.»',
                'A: «Selamat datang, Encik Tanaka!»  B: «Terima kasih, Puan.»'],
                '«Selamat» plus a time word makes a greeting: «pagi» (morning), «tengah hari» (around midday), «petang» (mid-afternoon to dusk), «malam» (night). '
                'Add a title and then the name. A title alone is also polite: «Selamat pagi, Puan.»',
                '«Selamat» に時間帯の語をつけるとあいさつになります。«pagi»（朝）、«tengah hari»（昼ごろ）、«petang»（午後〜夕方）、«malam»（夜）。'
                'そのあとに敬称と名前を言います。敬称だけでも丁寧です：«Selamat pagi, Puan.»',
                'Titles work like さん, but they come before the name: «Encik» Tanaka. «Selamat malam» covers both こんばんは and おやすみなさい. '
                'こんにちは is split in two: «Selamat tengah hari» around midday, «Selamat petang» later.',
                '敬称はさんに似ていますが、名前の前に来ます。«Selamat malam» は「こんばんは」と「おやすみなさい」の両方です。'
                '「こんにちは」は二つに分かれます：昼ごろは «Selamat tengah hari»、午後は «Selamat petang»。'),
            pattern(2, 'ms-c01-f02', '«Apa khabar,» (title)?', [
                'A: «Apa khabar, Encik Tanaka?»  B: «Khabar baik, terima kasih.»',
                'A: «Apa khabar, Puan Aini?»  B: «Baik, terima kasih.»',
                'A: «Apa khabar, Pak cik?»  B: «Baik. Terima kasih.»',
                'A: «Selamat pagi, Kakak. Apa khabar?»  B: «Khabar baik.»'],
                '«Apa khabar?» (literally "what news?") asks how someone is. Answer «Khabar baik» ("good news") or just «Baik». '
                'Add the title at the end to make it personal.',
                '«Apa khabar?»（直訳「どんな便り？」）は相手の様子をたずねます。答えは «Khabar baik»（よい便り）か «Baik» だけでも大丈夫です。最後に敬称をつけると丁寧です。',
                'It is close to お元気ですか, but Malaysians use it more widely, for example with someone they have just met.',
                '「お元気ですか」に近いですが、初めて会った人にも使えるなど、もっと広く使われます。'),
            pattern(3, 'ms-c01-f03', '«Khabar baik, terima kasih.» (title) «pula»?', [
                'A: «Khabar baik, terima kasih. Puan pula?»  B: «Saya pun baik.»',
                'A: «Baik, terima kasih. Encik pula?»  B: «Baik, terima kasih.»',
                'A: «Khabar baik. Cik Mei Ling pula?»  B: «Saya pun baik, terima kasih.»',
                'A: «Saya baik. Pak cik pula?»  B: «Pak cik pun baik.»'],
                '«pula» turns the question back to the other person ("and you?"). «pun» after a word means "too": «Saya pun baik» = I am fine too. '
                'Use the person\'s title, not a word for "you". Older speakers often call themselves «Pak cik» or «Mak cik».',
                '«pula» は質問を相手に返します（「あなたは？」）。«pun» は語のあとについて「〜も」の意味です：«Saya pun baik»＝私も元気です。'
                '「あなた」ではなく相手の敬称を使います。年配の人は自分を «Pak cik»・«Mak cik» と呼ぶことがよくあります。',
                '«pun» comes after the word it adds to, just like も: «Saya pun» ≈ 私も. «pula?» ≈ 〜は？ in あなたは？',
                '«pun» は「も」と同じく語のあとに来ます：«Saya pun»≈私も。«pula?» は「あなたは？」の「は？」に近いです。'),
            pattern(4, 'ms-c01-f04', '«Maaf, tumpang tanya.»', [
                'A: «Maaf, tumpang tanya. Encik Tanaka?»  B: «Ya, saya Tanaka.»',
                'A: «Maaf, tumpang tanya. Puan Aini?»  B: «Tidak. Saya Mei Ling.»',
                'A: «Maaf, Pak cik. Tumpang tanya.»  B: «Ya?»',
                'A: «Maaf, Encik Rahman?»  B: «Ya, saya.»',
                'A: «Terima kasih, Kakak.»  B: «Sama-sama.»'],
                '«Maaf» is "sorry" or "excuse me". «Tumpang tanya» politely asks to ask something. Confirm with «ya» or deny with «tidak» '
                '(spoken: «tak»). Answer thanks with «Sama-sama».',
                '«Maaf» は「すみません・ごめんなさい」。«Tumpang tanya» は「ちょっとお尋ねします」。確認は «ya»、否定は «tidak»（話し言葉では «tak»）。お礼には «Sama-sama» で答えます。',
                '«Maaf, tumpang tanya» ≈ すみません、ちょっとお尋ねします. But Japanese すみません can also mean thank you; in Malay, thanks is always «terima kasih».',
                '«Maaf, tumpang tanya» は「すみません、ちょっとお尋ねします」に近いです。ただし日本語の「すみません」はお礼にも使いますが、マレー語のお礼は必ず «terima kasih» です。'),
            pattern(5, 'ms-c01-f05', '«Saya minta diri dulu. Jumpa» ___ !', [
                'A: «Saya minta diri dulu. Jumpa esok!»  B: «Jumpa esok. Selamat jalan!»',
                'A: «Maaf, saya minta diri dulu.»  B: «Ya. Jumpa lagi!»',
                'A: «Jumpa nanti, Cik Mei Ling.»  B: «Jumpa nanti.»',
                'A: «Selamat malam, Puan. Jumpa esok.»  B: «Selamat malam. Jaga diri!»',
                'A: «Terima kasih, Pak cik. Jumpa lagi!»  B: «Hati-hati, Encik!»'],
                '«Saya minta diri dulu» means "I will take my leave first". «Jumpa» + «esok» / «lagi» / «nanti» = see you tomorrow / again / later. '
                '«Selamat jalan» is said to the person leaving; «Selamat tinggal» to the person staying, and it sounds final.',
                '«Saya minta diri dulu» は「お先に失礼します」。«Jumpa» ＋ «esok»・«lagi»・«nanti»＝また明日・またね・あとで。'
                '«Selamat jalan» は出かける人に、«Selamat tinggal» は残る人に言います。«Selamat tinggal» は別れの響きが強い言葉です。',
                '«Saya minta diri dulu» ≈ お先に失礼します. Careful: «Selamat jalan» is said by the person staying (≈ いってらっしゃい), not by the one who leaves.',
                '«Saya minta diri dulu»≈お先に失礼します。注意：«Selamat jalan» は残る人が言う言葉（≈いってらっしゃい）で、帰る本人は言いません。'),
        ],
        key=['Patterns are Kata-Kata frames ms-c01-f01 to f05, unchanged.',
             'Teacher prompts: read each A line; the class answers with the B line, then swap. Then change the time or the title and ask again.',
             'Check: pattern 1 time words in order of the day: «pagi», «tengah hari», «petang», «malam».',
             'Check: «Saya pun baik» (not «Pun saya baik»); the title, not a pronoun, returns the question: «Puan pula?»']))

    # 4 · Drills (charter section 14, types 1 to 6, plus the question-word set) --
    C.append(dict(
        slug='drill-1-pattern-table', type='Drill', sub_type='repeat', title='Drill 1 · Pattern table', block='B', minutes=3,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g06'], patterns=['ms-c01-f01', 'ms-c01-f05'], goal=GOALS['B'],
        explain=('表の言葉を組み合わせて、全部の文を声に出して読みます。', 'Combine the words in the table and read every sentence aloud.'),
        sections=[('Read every combination · 全部の組み合わせを読む', [
            'Table 1: «Selamat» [ «pagi» / «tengah hari» / «petang» / «malam» ] , [ «Encik» / «Puan» / «Cik» ] (name).',
            'Names: Tanaka, Aini, Mei Ling.',
            '1. «Selamat pagi, Encik Tanaka.»', '2. «Selamat tengah hari, Puan Aini.»', '3. «Selamat petang, Cik Mei Ling.»',
            '4. «Selamat malam, Encik Tanaka.»', '5. «Selamat pagi, Puan Aini.»', '6. «Selamat petang, Encik Tanaka.»',
            'Table 2: «Jumpa» [ «esok» / «lagi» / «nanti» ] , [ «Pak cik» / «Mak cik» / «Abang» / «Kakak» ] .',
            '7. «Jumpa esok, Pak cik.»', '8. «Jumpa lagi, Kakak.»', '9. «Jumpa nanti, Abang.»', '10. «Jumpa lagi, Mak cik.»',
            'Now read the combinations that are not printed. Your partner points at the table.'])],
        key=['Twelve combinations in table 1 and twelve in table 2 are all correct. Listen for the title before the name.']))
    C.append(dict(
        slug='drill-2-substitution', type='Drill', sub_type='substitute', title='Drill 2 · Substitution', block='B', minutes=3,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g06'], patterns=['ms-c01-f01', 'ms-c01-f05'], goal=GOALS['B'],
        explain=('（　）の言葉を入れて、文を言いかえます。前の答えを次の文のもとにします。',
                 'Replace one part with the cue. Each answer becomes the next starting sentence.'),
        sections=[('Change one part · 一つだけ変える', [
            'Start: «Selamat pagi, Puan Aini.»',
            '1. ( «petang» ) → ____________________', '2. ( «Encik» Rahman ) → ____________________',
            '3. ( «malam» ) → ____________________', '4. ( «Mak cik» ) → ____________________',
            '5. ( «tengah hari» ) → ____________________', '6. ( «Cik» Mei Ling ) → ____________________',
            '7. ( «pagi» ) → ____________________', '8. ( «Pak cik» ) → ____________________',
            'Start: «Saya minta diri dulu. Jumpa esok!»',
            '9. ( «lagi» ) → ____________________', '10. ( «nanti» ) → ____________________'])],
        key=['1 «Selamat petang, Puan Aini.» 2 «Selamat petang, Encik Rahman.» 3 «Selamat malam, Encik Rahman.» 4 «Selamat malam, Mak cik.»',
             '5 «Selamat tengah hari, Mak cik.» 6 «Selamat tengah hari, Cik Mei Ling.» 7 «Selamat pagi, Cik Mei Ling.» 8 «Selamat pagi, Pak cik.»',
             '9 «Saya minta diri dulu. Jumpa lagi!» 10 «Saya minta diri dulu. Jumpa nanti!»']))
    C.append(dict(
        slug='drill-3-transformation', type='Drill', sub_type='transform', title='Drill 3 · Transformation', block='B', minutes=4,
        grammar=['ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06', 'ms-c01-g08'], patterns=['ms-c01-f03', 'ms-c01-f04'], goal=GOALS['B'],
        explain=('指示どおりに文の形を変えます（質問を返す・「も」・肯定と否定・標準形と話し言葉）。',
                 'Change the form as the cue says: return the question, add "too", yes to no, standard to spoken.'),
        sections=[('Change the form · 形を変える', [
            '1. Return the question to «Puan»: «Khabar baik, terima kasih.» → ____________________',
            '2. Return the question to «Encik»: «Baik, terima kasih.» → ____________________',
            '3. Say "me too": «Saya baik.» → ____________________',
            '4. He is leaving now, not arriving: «Selamat datang, Encik Tanaka.» → ____________________',
            '5. Answer no; you are Kimura: «Ya, saya Tanaka.» → ____________________',
            '6. Make number 5 spoken: ____________________ (spoken)',
            '7. Friendly title for a waiter about your age: «Terima kasih, Encik.» → ____________________',
            '8. Add an apology first: «Tumpang tanya.» → ____________________'])],
        key=['1 «Khabar baik, terima kasih. Puan pula?» 2 «Baik, terima kasih. Encik pula?» 3 «Saya pun baik.» 4 «Selamat jalan, Encik Tanaka.»',
             '5 «Tidak, saya Kimura.» 6 «Tak, saya Kimura.» (spoken) 7 «Terima kasih, Abang.» 8 «Maaf, tumpang tanya.»']))
    C.append(dict(
        slug='drill-4-question-answer', type='Drill', sub_type='question and answer', title='Drill 4 · Question and answer', block='B', minutes=4,
        grammar=['ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06'], patterns=['ms-c01-f02', 'ms-c01-f03', 'ms-c01-f04', 'ms-c01-f05'], goal=GOALS['B'],
        explain=('前半は質問に答えます。後半は答えを聞いて、それに合う質問やあいさつを言います。',
                 'Part 1: answer. Part 2: hear the answer and say the question or line that fits before it.'),
        sections=[('Part 1 · Answer · 答える', [
            '1. «Apa khabar, Encik?» → ____________________', '2. «Terima kasih, Puan.» → ____________________',
            '3. «Maaf, tumpang tanya.» → ____________________', '4. «Encik Tanaka?» (You are Tanaka.) → ____________________']),
            ('Part 2 · Reverse · 前の文を言う', [
            '5. ____________________ → «Khabar baik.»', '6. ____________________ → «Sama-sama.»',
            '7. ____________________ → «Saya pun baik.»', '8. ____________________ → «Jumpa esok, Encik!»'])],
        key=['1 «Khabar baik, terima kasih.» 2 «Sama-sama.» 3 «Ya?» 4 «Ya, saya Tanaka.»',
             '5 «Apa khabar?» 6 «Terima kasih.» 7 «Khabar baik. Puan pula?» (any title) 8 «Saya minta diri dulu.» (or «Jumpa esok!»)',
             'Accept any title that suits the cue.']))
    C.append(dict(
        slug='drill-5-question-word-choice', type='Drill', sub_type='question-word choice', title='Drill 5 · Question-word choice', block='B', minutes=3,
        grammar=['ms-c01-g04'], patterns=['ms-c01-f02', 'ms-c01-f03'], goal=GOALS['B'],
        explain=('第1章の疑問詞は «apa» だけです。空欄に «apa» が入るか、ほかの語が入るかを選びます。',
                 'The only question word so far is «apa». Decide whether each gap needs «apa» or another word from the box.'),
        sections=[('Choose · 選ぶ', [
            'Box: «apa» / «pula» / «pun» / «baik»',
            '1. «___ khabar, Puan?»', '2. «Khabar ___, terima kasih.»', '3. «Baik. Encik ___ ?»', '4. «Saya ___ baik.»',
            '5. «Selamat pagi, Pak cik. ___ khabar?»', '6. «Khabar baik. Cik Mei Ling ___ ?»', '7. «Saya Tanaka. ___ khabar?»',
            '8. «Mak cik ___ baik.»',
            'Question-word set to date (charter section 14): chapter 1 «apa».'])],
        key=['1 «Apa» 2 «baik» 3 «pula» 4 «pun» 5 «Apa» 6 «pula» 7 «Apa» 8 «pun»']))
    C.append(dict(
        slug='drill-6-short-dialogue', type='Drill', sub_type='free', title='Drill 6 · Short dialogues', block='B', minutes=3,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g06'], patterns=['ms-c01-f01', 'ms-c01-f02', 'ms-c01-f03', 'ms-c01-f05'], goal=GOALS['B'],
        explain=('ヒントの場面で二行の会話を読み、もう一行を自分で足します。役を交代しましょう。',
                 'Read the two lines in the cued situation, then add one more line of your own. Swap roles.'),
        sections=[('Two turns, then add one · 二行＋一行', [
            'Dialogue 1 · 8 am, office door, «Puan» Aini',
            'A: «Selamat pagi, Puan Aini.»  B: «Selamat pagi. Apa khabar?»  A: ____________________',
            'Dialogue 2 · 6 pm, you leave before «Encik» Rahman',
            'A: «Maaf, saya minta diri dulu.»  B: «Ya. Jumpa esok!»  A: ____________________',
            'Dialogue 3 · 1 pm, a food stall, the waiter is about your age',
            'A: «Terima kasih, Abang.»  B: «Sama-sama.»  A: ____________________',
            'Dialogue 4 · 9 pm, the lift at your condo, an older woman',
            'A: «Selamat malam, Mak cik.»  B: «Selamat malam. Apa khabar?»  A: ____________________'])],
        key=['Possible third lines: 1 «Khabar baik, terima kasih. Puan pula?» 2 «Jumpa esok, Encik Rahman.» 3 «Jumpa lagi!» 4 «Khabar baik, terima kasih. Mak cik pula?»',
             'Accept any third line that fits the time, the person and the turn before it.']))
    C.append(dict(
        slug='drill-question-word-set', type='Drill', sub_type='question-word set', title='Cumulative question-word drill', block='D', minutes=5,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04'], patterns=['ms-c01-f01', 'ms-c01-f02'], goal=GOALS['D'],
        explain=('これまでの疑問詞（第1章は «apa»）を使って、時間と相手に合わせて質問します。ブロックDの復習で使います。',
                 'Use every question word so far (chapter 1: «apa») with the right greeting and title. For the Block D review.'),
        sections=[('Greet and ask · あいさつして、たずねる', [
            'Set to date: «apa» (chapter 1). Chapter 2 adds the words for who and where, and the -kah forms.',
            '1. 8 am · «Puan» Aini → ____________________', '2. 1 pm · «Cik» Mei Ling → ____________________',
            '3. 5 pm · an older man at the gate → ____________________', '4. 9 pm · an older woman in the lift → ____________________',
            '5. 12.30 pm · a waiter about your age → ____________________', '6. 7 pm · «Encik» Rahman, leaving the office → ____________________',
            'Then answer your partner and return the question.'])],
        key=['1 «Selamat pagi, Puan Aini. Apa khabar?» 2 «Selamat tengah hari, Cik Mei Ling. Apa khabar?» 3 «Selamat petang, Pak cik. Apa khabar?»',
             '4 «Selamat malam, Mak cik. Apa khabar?» 5 «Selamat tengah hari, Abang. Apa khabar?» 6 «Selamat petang, Encik Rahman. Apa khabar?» (7 pm: «petang» or «malam»)']))

    # 5 · Model conversation --------------------------------------------------
    model = [('Aini', '«Selamat pagi! Selamat datang.»'), ('Tanaka', '«Selamat pagi, Puan. Saya Tanaka.»'),
             ('Aini', '«Oh, Encik Tanaka! Apa khabar?»'), ('Tanaka', '«Khabar baik, terima kasih. Puan pula?»'),
             ('Aini', '«Saya pun baik. Selamat berkenalan.»'), ('Tanaka', '«Selamat berkenalan, Puan Aini.»'),
             (None, '6 pm · 午後6時'),
             ('Tanaka', '«Maaf, Puan Aini. Saya minta diri dulu.»'), ('Aini', '«Ya, ya. Jumpa esok, Encik Tanaka.»'),
             ('Tanaka', '«Jumpa esok. Terima kasih, Puan.»'), ('Aini', '«Sama-sama. Selamat jalan!»'),
             (None, 'At the door · 門で'),
             ('Tanaka', '«Selamat petang, Pak cik.»'), ('Guard', '«Selamat petang, Encik. Hati-hati!»')]
    gapped = [('Aini', '«Selamat ___ ! Selamat ___ .»'), ('Tanaka', '«Selamat pagi, ___ . Saya Tanaka.»'),
              ('Aini', '«Oh, Encik Tanaka! ___ khabar?»'), ('Tanaka', '«Khabar ___ , terima kasih. Puan ___ ?»'),
              ('Aini', '«Saya ___ baik. Selamat berkenalan.»'), ('Tanaka', '«Selamat berkenalan, Puan Aini.»'),
              (None, '6 pm'),
              ('Tanaka', '«Maaf, Puan Aini. Saya minta ___ dulu.»'), ('Aini', '«Ya, ya. Jumpa ___ , Encik Tanaka.»'),
              ('Tanaka', '«Jumpa esok. Terima kasih, Puan.»'), ('Aini', '«___ . Selamat jalan!»'),
              (None, 'At the door'),
              ('Tanaka', '«Selamat ___ , Pak cik.»'), ('Guard', '«Selamat petang, Encik. Hati-hati!»')]
    variant = [('Mei Ling', '«Selamat tengah hari! Selamat datang.»'), ('Kimura', '«Selamat tengah hari, Cik. Saya Kimura.»'),
               ('Mei Ling', '«Oh, Encik Kimura! Apa khabar?»'), ('Kimura', '«Baik, terima kasih. Cik pula?»'),
               ('Mei Ling', '«Saya pun baik. Selamat berkenalan.»'), ('Kimura', '«Selamat berkenalan, Cik Mei Ling.»'),
               (None, '9 pm · 午後9時'),
               ('Kimura', '«Maaf, Cik Mei Ling. Saya minta diri dulu.»'), ('Mei Ling', '«Ya. Jumpa lagi, Encik Kimura.»'),
               ('Kimura', '«Jumpa lagi. Jaga diri!»'), ('Mei Ling', '«Terima kasih. Selamat jalan!»'),
               (None, 'At the lift · エレベーターで'),
               ('Kimura', '«Selamat malam, Mak cik.»'), ('Cleaner', '«Selamat malam, Encik.»')]
    C.append(dict(
        slug='model-conversation', type='Model conversation', title='Model conversation', block='B', minutes=15,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g06'], patterns=['ms-c01-f01', 'ms-c01-f02', 'ms-c01-f03', 'ms-c01-f05'], goal=GOALS['B'],
        explain=('田中さんの初出勤の会話（12ターン）です。ペアで読み、次に空欄版、最後に事実を変えた版を演じます。',
                 '«Encik» Tanaka\'s first day, in 12 turns. Read it in pairs, then do the gapped version, then the variant with changed facts.'),
        sections=[('1 · Model: first day, 8 am · 初出勤 朝8時', turns(model)),
                  ('2 · Gapped version · 空欄版', turns(gapped)),
                  ('3 · Variant: changed facts · 事実を変えた版', ['Now it is 12.30 pm. «Cik» Mei Ling welcomes «Encik» Kimura. He leaves at 9 pm.', *turns(variant),
                    'Change two more facts yourselves (the time, a person) and play it again.'])],
        key=['Gaps in order: «pagi», «Selamat datang», «Puan», «Apa», «baik», «pula», «pun», «diri», «esok», «Sama-sama», «petang».',
             'Variant check: «Selamat tengah hari» at 12.30 pm; «Cik» for Mei Ling; «Selamat malam» at 9 pm.',
             'At 6 pm «Selamat petang» fits («petang» runs to dusk). Accept «Jumpa lagi» for «Jumpa esok» if the learner explains the change.']))

    # 6 · Listening -----------------------------------------------------------
    script = ['Scene 1',
              'Woman: «Selamat pagi, Encik Tanaka!»', 'Tanaka: «Oh, selamat pagi, Mak cik. Apa khabar?»',
              'Woman: «Khabar baik, terima kasih. Encik pula?»', 'Tanaka: «Saya pun baik. Maaf, Mak cik, saya minta diri dulu.»',
              'Woman: «Ya, ya. Jumpa nanti, Encik!»',
              'Scene 2',
              'Man: «Selamat pagi! Maaf, tumpang tanya. Encik Tanaka?»', 'Tanaka: «Ya, saya Tanaka.»',
              'Man: «Saya Rahman. Selamat datang, Encik Tanaka. Selamat berkenalan.»',
              'Tanaka: «Terima kasih. Selamat berkenalan, Encik Rahman.»', 'Man: «Apa khabar?»',
              'Tanaka: «Khabar baik, terima kasih. Encik pula?»', 'Man: «Baik, terima kasih.»',
              'Scene 3',
              'Tanaka: «Selamat tengah hari, Kakak.»', 'Woman: «Selamat tengah hari, Encik.»',
              'Tanaka: «Terima kasih, Kakak.»', 'Woman: «Sama-sama. Jumpa lagi!»',
              'Scene 4',
              'Mei Ling: «Maaf, Encik Tanaka. Saya minta diri dulu.»', 'Tanaka: «Oh, ya. Jumpa esok, Cik Mei Ling.»',
              'Mei Ling: «Jumpa esok! Jaga diri, Encik.»', 'Tanaka: «Terima kasih. Selamat jalan!»',
              'Scene 5',
              'Man: «Selamat malam, Encik.»', 'Tanaka: «Selamat malam, Pak cik. Terima kasih.»',
              'Man: «Sama-sama. Hati-hati, Encik!»', 'Tanaka: «Terima kasih, Pak cik. Jumpa esok!»']
    C.append(dict(
        slug='listening', type='Listening', title='Listening focus · Tanaka\'s first day', block='C', minutes=15,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06'], goal=GOALS['C'],
        explain=('先生が田中さんの一日の五つの場面を読みます。場面ごとに時間帯と相手を聞き取りましょう。台本は先生用のページにあります。',
                 'Your teacher reads five short scenes from «Encik» Tanaka\'s day. Listen for the time of day and the person. The script is on the teacher page.'),
        sections=[('Before listening · 聞く前に', [
            'The five places: the condo lobby, the office reception, a food stall, the office, the condo gate.',
            'Which greeting do you expect in each place? Write one: ____________________',
            '五つの場所でどのあいさつが聞こえると思いますか。']),
            ('While listening · 聞きながら', [
            '1. Scene 1: What time of day is it? ( «pagi» / «tengah hari» / «petang» / «malam» )',
            '2. Scene 1: Who greets Tanaka? ( a young woman / an older woman / a man )',
            '3. Scene 2: What is the man\'s name? ____________',
            '4. Scene 2: Is this their first meeting? Which phrase tells you? ____________',
            '5. Scene 3: Who does Tanaka thank? What does she answer? ____________',
            '6. Scene 4: Who leaves first? When will they meet again? ____________',
            '7. Scene 5: What time of day is it? What does the man wish Tanaka? ____________',
            '8. Which scene has «Saya pun baik»? ____________']),
            ('After listening · 聞いたあとで', [
            'Retell «Encik» Tanaka\'s day: say one Malay line for each scene, without the script.',
            'Then act out scene 4 with your own names and a new time.',
            '場面ごとに一文ずつ言って、田中さんの一日を話しましょう。'])],
        key=[f'Teacher script (read each scene twice; say only "Scene 1" etc.). Malay words: {malay_words(script)}.', *script,
             'Answers: 1 «pagi» 2 an older woman («Mak cik») 3 Rahman 4 yes: «Selamat berkenalan» / «Selamat datang» 5 the waiter («Kakak»); «Sama-sama» '
             '6 Mei Ling; tomorrow («esok») 7 «malam»; «Jaga diri» 8 Scene 1']))

    # 7 · Reading and writing -------------------------------------------------
    C.append(dict(
        slug='reading-writing', type='Reading and writing', title='Reading and writing · Messages on Tanaka\'s phone', sub_type='message',
        block='C', minutes=10, grammar=['ms-c01-g02', 'ms-c01-g04', 'ms-c01-g06'], goal=GOALS['C'],
        explain=('田中さんのスマートフォンに届いたメッセージを読み、質問に答えます。次に、返信と自分のメッセージを書きます。',
                 'Read the messages on Tanaka\'s phone and answer the questions. Then write a reply and a message of your own.'),
        sections=[('Read · 読む', [
            'Sign on the office door: «SELAMAT DATANG»',
            '7.50 am · Aini: «Selamat pagi, Encik Tanaka. Selamat datang!»',
            '10.15 am · Rahman: «Selamat pagi, Encik Tanaka. Apa khabar?»',
            '10.20 am · Tanaka: «Khabar baik, terima kasih. Encik Rahman pula?»',
            '10.21 am · Rahman: «Saya pun baik. Jumpa nanti!»',
            '5.40 pm · Mei Ling: «Maaf, Encik Tanaka, saya minta diri dulu. Jumpa esok!»',
            '9.30 pm · Aini: «Selamat malam. Jaga diri!»']),
            ('Questions · 質問', [
            '1. Who welcomes Tanaka, and at what time?', '2. Who asks how Tanaka is?',
            '3. How does Tanaka return the question?', '4. Who leaves the office first?',
            '5. When will Mei Ling see Tanaka again?', '6. Which message is sent at night, and what does it wish him?']),
            ('Write · 書く', [
            'Task 1: Reply to Mei Ling\'s message at 5.40 pm. Thank her and say see you tomorrow.',
            '____________________________________________',
            'Task 2: It is 8 pm. Write to «Encik» Rahman: greet him, ask how he is and say see you tomorrow.',
            '____________________________________________', '____________________________________________',
            'Model answer for task 2 is on the teacher page. Check: right greeting for the time? title before the name?'])],
        key=['1 Aini, at 7.50 am. 2 Rahman. 3 «Khabar baik, terima kasih. Encik Rahman pula?» 4 Mei Ling. 5 Tomorrow («esok»). 6 Aini at 9.30 pm: «Jaga diri» (take care).',
             'Task 1 model: «Baik, Cik Mei Ling. Terima kasih. Jumpa esok!»',
             'Task 2 model: «Selamat malam, Encik Rahman. Apa khabar? Jumpa esok!»',
             'Accept «Jumpa lagi» or «Jumpa nanti» if the learner explains when they meet.']))

    # 8 · Task --------------------------------------------------------------
    C.append(dict(
        slug='task', type='Task', title='Task · First day at reception', sub_type='role-play', block='C', minutes=15,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g06'], goal=GOALS['C'],
        explain=('役割カードを使って、台本なしで受付のあいさつをします。途中で先生が予定の変更を伝えます。',
                 'Use the role cards to play the reception greeting with no script. Your teacher will announce a change of plan.'),
        sections=[('Role card A · 新入社員', [
            'You are a new employee. It is 8.30 am on your first day.',
            'Greet the receptionist with the right greeting and title. Say your name. Ask how they are and answer when they ask you.',
            'あなたは新入社員です。初日の朝8時半。受付の人にあいさつし、名前を言い、様子をたずねましょう。']),
            ('Role card B · 受付', [
            'You are the receptionist. A new employee arrives.',
            'Welcome them. Check their name. Answer when they ask how you are, then return the question. Say "nice to meet you".',
            'あなたは受付です。新入社員を歓迎し、名前を確かめ、様子をたずね合い、「よろしく」と言いましょう。']),
            ('Change of plan · 予定の変更', [
            'It is now 6 pm. A must leave before B. Take your leave politely and agree when you will meet again.',
            'Then: B is much older than A. Play the morning greeting again with the right title.',
            '午後6時になりました。Aが先に帰ります。丁寧に別れ、次に会う時を決めましょう。次に、Bをずっと年上の人にして、朝のあいさつをやり直します。']),
            ('Success criteria · 先生が確認すること', [
            '☐ The greeting fits the time of day.', '☐ The title comes before the name, and a title replaces "you".',
            '☐ «Apa khabar?» is asked and returned with «pula», or answered with «pun».',
            '☐ Leave-taking uses «minta diri dulu» and «Jumpa» + a time word.', '☐ Thanks get «Sama-sama».',
            '☐ After the change, the title changes («Pak cik» / «Mak cik»).'])],
        key=['Sample run: A «Selamat pagi, Puan. Saya Tanaka.» B «Oh, Encik Tanaka! Selamat datang. Apa khabar?» A «Khabar baik, terima kasih. Puan pula?» B «Saya pun baik. Selamat berkenalan.»',
             'Change: A «Maaf, Puan. Saya minta diri dulu. Jumpa esok!» B «Jumpa esok. Selamat jalan!» Older B: «Selamat pagi, Pak cik.» / «Mak cik».',
             'For one-to-one classes the teacher plays B.']))

    # 9 · Culture and word-origin note ---------------------------------------
    culture_en = [
            '«Selamat», the first word of most greetings, comes from Arabic salāma, "wellbeing". «Selamat pagi» is a wish: may your morning be well. '
                        '«Khabar» is also Arabic and means "news", so «Apa khabar?» asks "what news?" and «Khabar baik» answers "good news".',
            '«Terima kasih» joins ‹terima›, "receive", and ‹kasih›, "affection": you receive someone\'s kindness. '
            '«Tumpang tanya» pairs ‹tumpang›, "ride along", with ‹tanya›, "ask": you borrow a moment of someone\'s time.',
            'Two goodbyes depend on who moves. «Selamat jalan», "safe going", is said to the person leaving; «Selamat tinggal», "safe staying", '
            'to the person who stays. «Selamat tinggal» sounds final, so everyday partings use «Jumpa lagi» or «Jumpa esok».',
            'Titles matter. Use «Encik» for a man, «Puan» for a married or senior woman and «Cik» for a young woman, before the name. '
            'A title on its own is the polite "you": «Puan pula?» «Abang» and «Kakak», "older brother" and "older sister", are friendly titles '
            'for waiters, drivers and shop staff of about your age; «Pak cik» and «Mak cik», "uncle" and "auntie", are for older people.']
    C.append(dict(
        slug='culture-note', type='Culture note', title='Culture and word-origin note', block='E', minutes=10,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g06'], goal=GOALS['E'],
        explain=('あいさつの言葉の由来と使い方を読みます（英語と日本語）。', 'Read where the greeting words come from and how they are used (English and Japanese).'),
        sections=[('English', culture_en),
            ('日本語', [
            'あいさつの最初の語 «Selamat» は、アラビア語の salāma（無事・平安）から来ています。«Selamat pagi» は「よい朝でありますように」という願いです。'
                        '«Khabar» もアラビア語で「便り」の意味なので、«Apa khabar?» は「どんな便り？」、«Khabar baik» は「よい便り」です。',
            '«Terima kasih» は ‹terima›（受け取る）と ‹kasih›（愛情）から成り、相手の好意を受け取るという意味です。'
            '«Tumpang tanya» は ‹tumpang›（相乗りする）と ‹tanya›（たずねる）で、相手の時間を少し借りる表現です。',
            '別れのあいさつは、だれが動くかで変わります。«Selamat jalan»（無事に行って）は出かける人に、«Selamat tinggal»（無事に残って）は残る人に言います。'
            '«Selamat tinggal» は別れの響きが強いので、ふだんは «Jumpa lagi» や «Jumpa esok» を使います。',
            '敬称も大切です。男性には «Encik»、既婚・年上の女性には «Puan»、若い女性には «Cik» を名前の前につけます。'
            '敬称だけで丁寧な「あなた」になります：«Puan pula?»。«Abang»・«Kakak»（兄・姉）は同年代の店員や運転手への親しい呼びかけ、'
            '«Pak cik»・«Mak cik»（おじさん・おばさん）は年上の人への呼びかけです。'])],
        key=['Sources: Kata-Kata card notes ms-c01-001, 007, 008, 011, 016, 019, 037 and the ledger meanings. Sam\'s own etymology notes were not available to the builder; add them here when supplied.',
             f'English text: {english_words(culture_en)} words. Discussion prompt: which Malay greeting has no single Japanese equivalent? (Expected: «Selamat tengah hari» / «Selamat petang» split こんにちは.)']))

    # 10 · Chapter test and self-check ---------------------------------------
    tests = [
        dict(sub_type='listening', prompt='L1. Listen. What time of day is it? ( morning / around midday / afternoon to dusk / night )',
             answer='Teacher reads: «Selamat petang, Encik.» Answer: afternoon to dusk', words=['Selamat petang'], grammar=['ms-c01-g02']),
        dict(sub_type='listening', prompt='L2. Listen. What time of day is it? ( morning / around midday / afternoon to dusk / night )',
             answer='Teacher reads: «Selamat malam, Puan.» Answer: night', words=['Selamat malam'], grammar=['ms-c01-g02']),
        dict(sub_type='listening', prompt='L3. Listen. Is the speaker arriving or leaving?',
             answer='Teacher reads: «Saya minta diri dulu. Jumpa esok!» Answer: leaving', words=['minta diri', 'jumpa', 'esok'], grammar=['ms-c01-g06']),
        dict(sub_type='listening', prompt='L4. Listen. Who is being asked: a man, a young woman or an older woman?',
             answer='Teacher reads: «Apa khabar, Cik Mei Ling?» Answer: a young woman', words=['Cik', 'Apa khabar?'], grammar=['ms-c01-g03']),
        dict(sub_type='listening', prompt='L5. Listen and choose the reply: a «Sama-sama.» b «Selamat datang.» c «Maaf.»',
             answer='Teacher reads: «Terima kasih, Pak cik.» Answer: a «Sama-sama.»', words=['terima kasih', 'sama-sama'], grammar=['ms-c01-g05']),
        dict(sub_type='words', prompt='V1. It is 8 am. «Selamat ___ , Puan.»', answer='«pagi»', words=['pagi', 'Selamat pagi'], grammar=['ms-c01-g02']),
        dict(sub_type='words', prompt='V2. Greet Mr Rahman politely: «Selamat pagi, ___ Rahman.»', answer='«Encik»', words=['Encik'], grammar=['ms-c01-g03']),
        dict(sub_type='grammar', prompt='V3. Return the question: «Khabar baik, terima kasih. Encik ___ ?»', answer='«pula»', words=['pula'], grammar=['ms-c01-g04']),
        dict(sub_type='grammar', prompt='V4. Say "I am fine too": «Saya ___ baik.»', answer='«pun»', words=['pun'], grammar=['ms-c01-g04']),
        dict(sub_type='grammar', prompt='V5. Put in order: «dulu / saya / diri / minta»', answer='«Saya minta diri dulu.»', words=['minta diri', 'dulu'], grammar=['ms-c01-g06']),
        dict(sub_type='words', prompt='V6. Someone says «Terima kasih.» You answer: ____________', answer='«Sama-sama.»', words=['sama-sama'], grammar=['ms-c01-g05']),
        dict(sub_type='words', prompt='V7. Politely get a stranger\'s attention to ask something: ____________', answer='«Maaf, tumpang tanya.»', words=['maaf', 'tumpang tanya'], grammar=['ms-c01-g05']),
        dict(sub_type='words', prompt='V8. Write the spoken form of «tidak»: ____________', answer='«tak» (spoken)', words=['tak'], grammar=['ms-c01-g08']),
        dict(sub_type='reading', prompt='R1. Read the message above. When was it sent: morning or night?', answer='night («Selamat malam»)', words=['Selamat malam'], grammar=['ms-c01-g02']),
        dict(sub_type='reading', prompt='R2. Who wrote it?', answer='Mei Ling', words=['Cik'], grammar=['ms-c01-g03']),
        dict(sub_type='reading', prompt='R3. What is she doing: arriving, or leaving first?', answer='leaving first («minta diri dulu»)', words=['minta diri', 'dulu'], grammar=['ms-c01-g06']),
        dict(sub_type='reading', prompt='R4. When will they meet again?', answer='tomorrow («esok»)', words=['esok'], grammar=['ms-c01-g06']),
        dict(sub_type='speaking', prompt='S1. Speaking: it is 6 pm. Your teacher is a colleague. Greet them, ask how they are, answer, and take your leave.',
             answer='Check: «Selamat petang» + title; «Apa khabar?»; «Khabar baik ... pula?»; «Saya minta diri dulu. Jumpa esok!»',
             words=['Selamat petang', 'Apa khabar?', 'minta diri'], grammar=['ms-c01-g02', 'ms-c01-g04', 'ms-c01-g06']),
    ]
    C.append(dict(
        slug='test', type='Test', title='Chapter test and self-check', block='D', minutes=20,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06', 'ms-c01-g08'], goal=GOALS['D'], tests=tests,
        explain=('10分の小テストです（点数より確認のため）。聞く・単語と文法・読む、そして話す課題が一つあります。最後に「できる」チェックをします。',
                 'A ten-minute, low-stakes check: listening, words and grammar, reading, and one speaking task. Then tick the "I can" list.'),
        sections=[('Listening · 聞く (teacher reads each line twice)', [t['prompt'] for t in tests if t['sub_type'] == 'listening']),
                  ('Words and grammar · 単語と文法', [t['prompt'] for t in tests if t['sub_type'] in ('words', 'grammar')]),
                  ('Reading · 読む', ['Message: «Selamat malam, Encik Tanaka. Maaf, saya minta diri dulu. Jumpa esok! — Mei Ling»',
                                      *[t['prompt'] for t in tests if t['sub_type'] == 'reading']]),
                  ('Speaking · 話す', [t['prompt'] for t in tests if t['sub_type'] == 'speaking']),
                  ('Self-check · できるチェック', [f'☐ {GOALS[b]} / {GOALS_JA[b]}' for b in 'ABCE'] + [
                      'One thing I will practise in Kata-Kata this week: ____________________'])],
        key=[f'{t["prompt"].split(".")[0]}: {t["answer"]}' for t in tests] + ['Low-stakes: record items to recycle in the chapter 2 recall, not a score.']))

    # 11 · Teaching plan ------------------------------------------------------
    C.append(dict(
        slug='teaching-plan', type='Teaching plan', title='Teaching plan and answer key', block='All', minutes=None,
        grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04', 'ms-c01-g05', 'ms-c01-g06', 'ms-c01-g07', 'ms-c01-g08'],
        patterns=['ms-c01-f01', 'ms-c01-f02', 'ms-c01-f03', 'ms-c01-f04', 'ms-c01-f05'],
        explain=('先生用：五つのブロック（各45分）と発音ブロックの時間配分、指示、予想される答え、Kata-Kata の宿題。',
                 'For the teacher: timings for the five 45-minute blocks and the pronunciation block, prompts, expected answers and Kata-Kata homework.'),
        sections=[
            ('Before and after · 授業の前後', [
                'Before Block A: learners do Kata-Kata Sedia Kelas c01 (23 cards; frames ms-c01-f01, f02) and send Tanya Cikgu questions.',
                'After Block B: the whole chapter 1 deck with spaced review. After Block D: preview Sedia Kelas c02 (chapter 2).',
                'Self-study planning figure: about 3 hours of Kata-Kata for this unit. Hanashishou starts at A2; there is no A1 scene yet.',
                'Audio: teacher-read scripts only (charter section 11).']),
            ('Block A · Words and patterns (45 min)', [
                'Goal: ' + GOALS['A'],
                '0–5 Recall (Opener): "Say every Malay greeting you know." Expected: «Selamat pagi», «Terima kasih».',
                '5–10 Tanya Cikgu: answer the questions sent from Kata-Kata.',
                '10–20 Vocabulary: say a time or a person; learners answer with the greeting or title (key on the vocabulary sheet).',
                '20–40 Patterns 1 to 5: model each A line; the class gives the B line; then pairs. Ask "Who says «Selamat jalan»?" Expected: the one who stays.',
                '40–45 First substitutions: Drill 2, items 1 to 4, orally.']),
            ('Block B · Drills and conversation (45 min)', [
                'Goal: ' + GOALS['B'],
                '0–5 Recall: "It is 1 pm. Greet «Cik» Mei Ling." Expected: «Selamat tengah hari, Cik Mei Ling.»',
                '5–25 Drill ladder in order: 1 pattern table, 2 substitution, 3 transformation, 4 question and answer, 5 question-word choice, 6 short dialogues.',
                '25–40 Model conversation: read, then the gapped version with books closed on the model, then the variant.',
                '40–45 Pair rehearsal: play the model with your own names.']),
            ('Block C · Listening and task (45 min)', [
                'Goal: ' + GOALS['C'],
                '0–5 Recall: "Return the question to «Puan» Aini." Expected: «Khabar baik, terima kasih. Puan pula?»',
                '5–20 Listening: before task; read each scene twice (script on the listening key); while task; after task.',
                '20–30 Reading and writing: messages, six questions, then the reply and the 8 pm message.',
                '30–45 Task: role cards A and B; announce the change at minute 38; check the success criteria.']),
            ('Block D · Review and test (45 min)', [
                'Goal: ' + GOALS['D'],
                '0–15 Mixed review: cumulative question-word drill (all six items); then pairs greet at four times of day.',
                '15–25 Chapter test, items L1 to R4 (read listening items twice).',
                '25–35 Self-check and feedback: go through the key together; learners note one item to recycle.',
                '35–45 Preview Kata-Kata Sedia Kelas c02 (pronouns, names, who and where).']),
            ('Block E · Scene (45 min)', [
                'Goal: ' + GOALS['E'],
                '0–5 Recall: "Take your leave from «Puan» Aini." Expected: «Maaf, Puan. Saya minta diri dulu. Jumpa esok!»',
                '5–15 Scene listening: chapter 1 has no Kata-Kata Dunia scene yet (charter section 6). Read the Kata-Kata chapter 1 scenario "First day at the office" '
                '(lines ms-c01-s01 to s10) aloud as the scene.',
                '15–30 Role-play the scene in threes (Tanaka, «Puan» Aini, narrator for the time change).',
                '30–40 Free variation: change the time, the people and the reason for leaving.',
                '40–45 Culture note (or set it as homework). No Hanashishou link at A1.']),
            ('Pronunciation block (45 min)', [
                'Goal: I can read greetings aloud using Malay spelling rules.',
                '0–5 Recall greetings. 5–15 Vowels, including the two sounds of e. 15–25 Consonants: c, ng, kh, final k, r and l.',
                '25–35 Read-aloud lists in pairs. 35–45 Dictation of eight words (key on the pronunciation sheet).']),
            ('What to listen for · 注意点', [
                'Title before the name; no «Tanaka Encik». «pun» after the word. «Selamat jalan» from the person staying.',
                'Final k as a catch, not a full く: «baik», «tidak». No vowel added after final consonants: «Encik», not "enchiku".',
                'Spoken «tak» only after «tidak» has been taught, and always labelled spoken.'])],
        key=['Answer keys are on each component\'s teacher page. This plan follows the block timings in charter section 6.',
             'All Japanese in this unit is a draft awaiting native review.']))

    # Pronunciation and spelling block (Stage 1 skills block) -----------------
    C.append(dict(
        slug='pronunciation-block', type='Drill', sub_type='repeat', title='Pronunciation and spelling block', block='Skills', minutes=45,
        grammar=['ms-c01-g07'], goal='I can read greetings aloud using Malay spelling rules.',
        skills=['speaking', 'listening', 'writing'],
        explain=('マレー語のつづりと発音はほぼ規則的です。日本語話者が注意したい音を練習し、最後に書き取りをします。',
                 'Malay spelling is close to regular. Practise the sounds Japanese speakers find tricky, then take a short dictation.'),
        sections=[
            ('1 · Vowels · 母音', [
                'a, i, o are close to Japanese あ, い, お. u is rounder than う: «Jumpa», «Puan».',
                'e has two sounds and the spelling does not show which. Weak e (like the a in "about"): «selamat», «petang», «terima kasih», «Encik».',
                'Clear e (like え): «esok». Learn each word with its sound.',
                'e には二つの音があり、つづりでは区別しません。弱い e（あいまい母音）：«selamat»、«petang»。はっきりした e（え）：«esok»。']),
            ('2 · Consonants · 子音', [
                'c sounds like ち: «Cik», «Encik», «Pak cik».',
                'ng is one sound, as in "sing" (no ぐ after it): «petang», «tengah hari».',
                'kh, from Arabic, is a soft sound from the back of the throat: «khabar».',
                'Final k is a catch in the throat, not a full く: «baik», «tidak», «Pak cik», «Mak cik».',
                'r and l are different sounds: «terima kasih», «diri» (tap the r); «selamat», «lagi», «malam» (tongue touches for l).',
                'No extra vowel after a final consonant: «maaf», not "maafu"; «malam», not "maramu". Double aa in «maaf» is two syllables: ma-af.',
                'ち・ん・のどの音などに注意。語末に母音を足さないこと。r と l は別の音です。']),
            ('3 · Read aloud in pairs · ペアで音読', [
                '«pagi» · «petang» · «malam» · «esok»', '«Encik» · «Cik» · «Pak cik» · «Mak cik»', '«baik» · «tidak» · «maaf»',
                '«terima kasih» · «selamat» · «lagi» · «diri»', '«sama-sama» · «hati-hati» (a repeated word is written with a hyphen)',
                '«Selamat berkenalan» · «khabar» · «Apa khabar?»']),
            ('4 · Dictation · 書き取り', [
                'Your teacher reads eight words. Write them.',
                '1 ________  2 ________  3 ________  4 ________', '5 ________  6 ________  7 ________  8 ________',
                'Check: is there a hyphen in a repeated word? Did you write ng, c and kh correctly?'])],
        key=['Dictation (read twice): 1 «pagi» 2 «malam» 3 «esok» 4 «baik» 5 «Encik» 6 «khabar» 7 «petang» 8 «sama-sama».',
             'Unverified: these pronunciation notes are from general knowledge of standard Malaysian Malay, not checked against a reference. Sam to confirm before teaching.']))
    return C


UNIT = dict(
    unit_id='ms-c01', label='1', chapter_id='ms-c01', check_unit='ms-c01', id_prefix='ms-c01', title_prefix='Unit 1',
    header='Unit 1 (ms-c01)', menu_title='Chapter 1 · Greetings', genre='Social life',
    goal='Greet by time of day, use titles, ask after someone and take leave.',
    blocks=GOALS, prerequisites=[], prerequisite_units=[], prereq_grammar=[], word_scope=WORDS,
    components=components)
