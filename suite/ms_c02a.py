"""Unit 2A (chapter 2, first half): pronouns, names, origin; siapa, apa, di mana.

Malay is limited to ledger rows placed in chapters 1 and 2. Patterns are
Kata-Kata frames ms-c02-f01, f02, f03 and f08 (f08 in its plain form; the -kah
form follows in unit 2B). Japanese is a draft awaiting native review.
"""
from . import vocab, malay_words, english_words, pattern, turns

GOALS = {
    'A': 'I can say my name and nationality and ask other people theirs.',
    'B': 'I can ask who someone is and where they are from, and introduce a friend.',
    'C': 'I can follow a short round of introductions and read name tags.',
    'D': 'I can check my introductions in a short test and say what I can do.',
    'E': 'I can join a chat in the office pantry and choose the right word for "you".',
}
GOALS_JA = {
    'A': '自分の名前と国籍を言い、相手にもたずねられる。',
    'B': 'だれか・どこの出身かをたずね、友達を紹介できる。',
    'C': '短い自己紹介の流れを聞いて分かり、名札が読める。',
    'D': '小テストで自己紹介の表現を確かめ、できることが言える。',
    'E': 'オフィスの給湯室での雑談に加わり、「あなた」にあたる正しい語を選べる。',
}
WORDS = ['L-0037', 'L-0038', 'L-0039', 'L-0040', 'L-0041', 'L-0042', 'L-0043', 'L-0044', 'L-0045', 'L-0046',
         'L-0047', 'L-0048', 'L-0049', 'L-0052', 'L-0053', 'L-0054', 'L-0055', 'L-0056', 'L-0058', 'L-0059',
         'L-0060', 'L-0061', 'L-0062', 'L-0063', 'L-0985', 'L-0986', 'L-0078', 'L-0075', 'L-0076',
         'L-0942', 'L-0943', 'L-0944', 'L-0945', 'L-0946', 'L-0947', 'L-0949', 'L-0950', 'L-0951', 'L-0952', 'L-0953']
G = dict(pron='ms-c02-g02', nn='ms-c02-g03', qw='ms-c02-g04', origin='ms-c02-g05', demo='ms-c02-g06', nya='ms-c02-g07',
         also='ms-c02-g13')


def components(ledger):
    C = []
    C.append(dict(
        slug='opener', type='Opener', title='Chapter opener', block='A', minutes=5,
        grammar=[G['nn'], G['qw']], goal=GOALS['A'], prereq_grammar=['ms-c01-g02', 'ms-c01-g04'],
        explain=('この課の目標と場面を確認し、第1章のあいさつを思い出します。',
                 'Read the goals and the scene, then recall the chapter 1 greetings.'),
        sections=[
            ('Can-do goals · できること', [
                *[f'Block {b}: {GOALS[b]}' for b in 'ABCDE'],
                *[f'ブロック{b}：{GOALS_JA[b]}' for b in 'ABCDE']]),
            ('The scene · 場面', [
                'In his second week, «Encik» Tanaka meets new colleagues in the office pantry: Farah and Kumar from Ipoh, and «Cik» Mei Ling. '
                'They ask each other\'s names and where they are from, and introduce their friends.',
                '2週目、田中さんは給湯室で新しい同僚に会います。イポー出身のファラさんとクマールさん、そしてメイリンさんです。'
                '名前や出身をたずね合い、友達を紹介します。', 'Genre: Social life · ジャンル：社会生活']),
            ('Recall from chapter 1 · 第1章の復習 (5 min)', [
                'Without notes, greet your partner for each time and ask how they are. Your partner answers and returns the question.',
                '1. 8 am · «Puan» Aini   2. 1 pm · «Encik» Rahman   3. 5 pm · a young woman   4. 9 pm · an older man',
                'ノートを見ずに、時間に合ったあいさつをして様子をたずねましょう。相手は答えて質問を返します。',
                'Then: write one Tanya Cikgu question about chapter 2: ____________________']),
            ('Self-study · 自習', [
                'Before class: Kata-Kata Sedia Kelas set c02 (27 cards, frames ms-c02-f01 and f02).',
                'After class: the chapter 2 cards for this unit and the Dunia scene "Sembang di pantri". Planning figure: about 3 hours per unit.',
                '授業前：Sedia Kelas c02。授業後：このユニットのカードと Dunia「Sembang di pantri」。目安は1ユニット約3時間。'])],
        key=['Expected recall: 1 «Selamat pagi, Puan Aini. Apa khabar?» 2 «Selamat tengah hari, Encik Rahman. Apa khabar?» '
             '3 «Selamat petang, Cik. Apa khabar?» 4 «Selamat malam, Pak cik. Apa khabar?» Answers: «Khabar baik, terima kasih. … pula?»',
             'Recycle any chapter 1 test items learners missed.']))

    C.append(dict(
        slug='vocabulary', type='Vocabulary', title='Vocabulary focus', block='A', minutes=10,
        grammar=[G['pron'], G['nn'], G['qw'], G['origin'], G['demo'], G['nya'], G['also']], goal=GOALS['A'],
        explain=('ユニット2Aの台帳の単語40語です。代名詞、名前と質問、出身、つなぐ言葉、友達、そして Kata-Kata の場面「Sembang di pantri」の雑談のことば。'
                 '例文を声に出して読みましょう。話し言葉には spoken と書いてあります。',
                 'The 40 ledger words for unit 2A: pronouns, names and questions, origin, linking words, friends, and the chat words from the Kata-Kata scene '
                 '"Sembang di pantri". Read every example aloud. Spoken forms are marked "spoken".'),
        sections=[('Words by group · 場面別の単語', vocab(ledger, [
            ('People: pronouns · 人を表す言葉', [
                ('L-0037', '«Aku pun orang Jepun.» (spoken, close friends only)', dict(en='I, me (casual, close friends; spoken)')),
                ('L-0038', '«Awak orang Jepun?»'),
                ('L-0039', '«Siapa nama kamu?» (to a child)'),
                ('L-0040', '«Selamat datang. Siapa nama anda?» (forms, signs, adverts)'),
                ('L-0041', '«Engkau orang Jepun?» (very casual; avoid with strangers)'),
                ('L-0042', '«Dia kawan saya.»'),
                ('L-0043', '«Ini Puan Aini. Beliau dari Ipoh.»'),
                ('L-0044', '«Kami orang Jepun.» (we, not you)'),
                ('L-0045', '«Kita kawan!» (we, including you)'),
                ('L-0046', '«Mereka orang Malaysia.»')]),
            ('Names and questions · 名前と質問', [
                ('L-0048', '«Nama saya Tanaka.»'),
                ('L-0047', '«Ini kawan saya. Namanya Ali.»', dict(display='«-nya»')),
                ('L-0049', '«Siapa nama encik?»'),
                ('L-0052', '«Kampung encik di mana?» (the -kah form comes in unit 2B)', dict(display='«di mana»', en='where')),
                ('L-0053', '«Kampung saya di Osaka.»'),
                ('L-0985', '«Ini Cik Mei Ling.»'),
                ('L-0986', '«Itu Encik Rahman.»')]),
            ('Where you are from · 出身', [
                ('L-0058', '«Dia orang Malaysia.»'),
                ('L-0059', '«Saya orang Jepun.»'),
                ('L-0060', '«Kampung saya di Jepun.»'),
                ('L-0061', '«Apa negara asal awak?»'),
                ('L-0062', '«Asal saya dari Osaka.»'),
                ('L-0063', '«Kampung saya di Kyoto.»'),
                ('L-0054', '«Saya dari Tokyo.»')]),
            ('Linking words · つなぐ言葉', [
                ('L-0055', '«Encik Rahman dan Puan Aini orang Malaysia.»'),
                ('L-0056', '«Saya juga orang Jepun.»')]),
            ('Friends · 友達', [
                ('L-0078', '«Ini kawan saya, Ali.»'),
                ('L-0075', '«Jom, kita jumpa nanti!» (spoken)', dict(en="let's (spoken)")),
                ('L-0076', '«Jom! — Boleh!»')]),
            ('Chat words from "Sembang di pantri" (recognise) · 雑談のことば', [
                ('L-0942', '«Alamak! Maaf, Encik.»'),
                ('L-0943', '«Wah, encik orang Jepun?»'),
                ('L-0944', '«Kampung awak di Osaka? Betul ke?» (spoken)', dict(display='«betul ke?»', en='really? (spoken)')),
                ('L-0945', '«Encik orang Jepun?» — «Mana ada! Saya orang Malaysia.» (spoken)', dict(en='not at all, no way (spoken)')),
                ('L-0946', '«Jangan risau, Encik.»'),
                ('L-0947', '«Lama tak jumpa! Apa khabar?» (spoken)', dict(en='long time no see (spoken)')),
                ('L-0949', '«Dia orang Jepun, kot.» (spoken)', dict(display='«kot» / «kut»', en='maybe, I think (end of a sentence; spoken)')),
                ('L-0950', '«Wah, best!» (spoken)', dict(en='great, awesome (spoken)')),
                ('L-0951', '«Wah, syok!» (spoken)', dict(en='really fun, enjoyable (spoken)')),
                ('L-0952', '«Ini geng saya.» (spoken)', dict(en='group of friends, crew (spoken)')),
                ('L-0953', '«Maaf, tumpang lalu.»')]),
        ]))],
        key=['Kata-Kata cards ms-c02-002 to ms-c02-028 (pronouns, names, origin), ms-c02-040 to 043, and Dunia cards ms-d-pejabat-sembang-01 to 12.',
             '«ini» (L-0985) and «itu» (L-0986) have no Kata-Kata card yet (pending). «saya» was taught in unit 1.',
             'Not listed: L-0948 ‹sikit je›. Its standard form ‹sedikit› is a chapter 5 word, and the register rule does not allow a spoken form before its standard form. Raised with Sam.',
             'Check in class: point at people (I, you, he or she, we, they); learners answer with the pronoun. Ask "Which "you" for your manager?" Expected: the title («Encik», «Puan»), not «awak».']))

    C.append(dict(
        slug='pattern-grammar', type='Pattern and grammar', title='Pattern and grammar focus', block='A', minutes=20,
        grammar=[G['pron'], G['nn'], G['qw'], G['origin'], G['demo'], G['nya']],
        patterns=['ms-c02-f01', 'ms-c02-f02', 'ms-c02-f03', 'ms-c02-f08'], goal=GOALS['A'],
        explain=('四つの文型を例の質問と答えで練習します。先にペアで例を読み、そのあと説明を読みましょう。',
                 'Four Kata-Kata patterns with question-and-answer examples. Read the examples in pairs first, then the explanation.'),
        sections=[
            pattern(1, 'ms-c02-f01', '«Nama saya» ___ . / «Ini» ___ . «Namanya» ___ .', [
                'A: «Nama saya Rahman. Encik pula?»  B: «Nama saya Tanaka.»',
                'A: «Ini kawan saya. Namanya Ali.»  B: «Selamat berkenalan, Ali.»',
                'A: «Itu Cik Mei Ling?»  B: «Ya, itu Cik Mei Ling.»',
                'A: «Nama awak Yuki?»  B: «Ya, nama saya Yuki.»',
                'A: «Ini Encik Kumar. Namanya Kumar.»  B: «Selamat berkenalan, Encik Kumar.»'],
                'Two nouns side by side make a sentence: «Nama saya Tanaka» (my name, Tanaka). There is no word for "is". «saya» after «nama» means "my". '
                '«ini» (this) is near you, «itu» (that) is further away. «-nya» on a noun means his, her or its: «namanya» = his or her name.',
                '名詞を二つ並べると文になります：«Nama saya Tanaka»。「〜です」にあたる語はありません。«nama» のあとの «saya» は「私の」。'
                '«ini»（これ・この）は近く、«itu»（それ・あれ）は遠く。名詞に «-nya» をつけると「彼の・彼女の・その」：«namanya»＝その人の名前。',
                'Japanese also puts the owner first in 私の名前, but Malay puts it last: «nama saya» = name + me. No は, の or です are needed.',
                '日本語の「私の名前」とは逆に、マレー語は持ち主が後ろに来ます：«nama saya»＝名前＋私。「は」「の」「です」はいりません。'),
            pattern(2, 'ms-c02-f02', '«Siapa nama» (title)? / ___ «siapa»?', [
                'A: «Siapa nama encik?»  B: «Nama saya Kimura.»',
                'A: «Siapa nama puan?»  B: «Nama saya Aini.»',
                'A: «Itu siapa?»  B: «Itu Encik Rahman.»',
                'A: «Siapa nama kawan awak?»  B: «Namanya Mei Ling.»',
                'A: «Dia siapa?»  B: «Dia kawan saya.»'],
                '«siapa» means "who". Malay asks for a name with "who": «Siapa nama encik?» The question word can also stay where the answer goes: '
                '«Itu siapa?» (that is who?). Use the title as "you" with people you do not know well.',
                '«siapa» は「だれ」。名前をたずねる時も「だれ」を使います：«Siapa nama encik?»。疑問詞を答えの位置に置いたままでもかまいません：«Itu siapa?»（あれはだれ？）。'
                'よく知らない相手には「あなた」の代わりに敬称を使います。',
                'お名前は何ですか uses 何 (what), but Malay uses «siapa» (who). Like Japanese, the question word can stay in place: «Itu siapa?» ≈ あれはだれ？',
                '「お名前は何ですか」は「何」ですが、マレー語は «siapa»（だれ）です。日本語と同じく、疑問詞をそのままの位置に置けます：«Itu siapa?»≈あれはだれ？'),
            pattern(3, 'ms-c02-f03', '«Saya orang» ___ . «Asal saya dari» ___ .', [
                'A: «Encik orang Jepun?»  B: «Ya, saya orang Jepun. Asal saya dari Osaka.»',
                'A: «Puan orang Malaysia?»  B: «Ya. Asal saya dari Ipoh.»',
                'A: «Kampung encik di mana?»  B: «Kampung saya di Sapporo.»',
                'A: «Mereka orang Jepun?»  B: «Tidak, mereka orang Malaysia.»',
                'A: «Apa negara asal awak?»  B: «Negara asal saya Jepun.»'],
                '«orang» (person) + a country = nationality: «orang Jepun», «orang Malaysia». «asal» is origin and «dari» is "from". '
                'A yes/no question can be a statement said with a rising voice: «Encik orang Jepun?»',
                '«orang»（人）＋国名で国籍になります：«orang Jepun»、«orang Malaysia»。«asal» は出身、«dari» は「〜から」。'
                'はい・いいえの質問は、文の終わりを上げて言うだけでもできます：«Encik orang Jepun?»',
                '«orang Jepun» is built like 日本人 (Japan + person), but in the opposite order: person + Japan. A rising voice works like か.',
                '«orang Jepun» は「日本人」と同じ作りですが、順番が逆です（人＋日本）。文末を上げるのは「か」と同じ働きです。'),
            pattern(4, 'ms-c02-f08', '___ «di mana»? / «Di mana» ___ ?  (unit 2B adds «di manakah»)', [
                'A: «Kampung encik di mana?»  B: «Di Osaka.»',
                'A: «Encik Rahman di mana?»  B: «Dia di Kuala Lumpur.»',
                'A: «Di mana Cik Mei Ling?»  B: «Dia di Bangsar.»',
                'A: «Kampung dia di mana?»  B: «Kampung dia di Johor Bahru.»',
                'A: «Osaka di mana?»  B: «Osaka di Jepun.»'],
                '«di mana» is "where": «di» (at) + ‹mana› (which place). Put it at the end, where the answer goes, or at the front. '
                '«di» is written as a separate word before a place: «di Osaka».',
                '«di mana» は「どこ」：«di»（〜に）＋ ‹mana›。答えが入る文末に置いても、文頭に置いてもかまいません。«di» は場所の前に離して書きます：«di Osaka»。',
                'Like どこ, «di mana» can sit where the answer goes. But «di» comes before the place (in Osaka), the reverse of 大阪に.',
                '「どこ」と同じく、答えの位置に置けます。ただし «di» は場所の前に来ます（«di Osaka»）。「大阪に」とは逆です。'),
        ],
        key=['Patterns are Kata-Kata frames ms-c02-f01, f02, f03 and f08 (taught here in its plain form «di mana»).',
             'Teacher prompts: read each A line; the class gives the B line with their own facts.',
             'Check: «Nama saya …», not «Saya nama …»; «orang Jepun», not «Jepun orang»; «di Osaka» with «di» before the place.',
             'Negating a noun (‹bukan›) is a chapter 3 word: for now learners answer «Tidak, saya orang Malaysia.»']))

    # Drills -------------------------------------------------------------
    C.append(dict(
        slug='drill-1-pattern-table', type='Drill', sub_type='repeat', title='Drill 1 · Pattern table', block='B', minutes=3,
        grammar=[G['pron'], G['nn'], G['origin'], G['nya']], patterns=['ms-c02-f01', 'ms-c02-f03'], goal=GOALS['B'],
        explain=('表の言葉を組み合わせて、全部の文を声に出して読みます。', 'Combine the words in the table and read every sentence aloud.'),
        sections=[('Read every combination · 全部の組み合わせを読む', [
            'Table 1: [ «Saya» / «Dia» / «Kami» / «Mereka» ] «orang» [ «Jepun» / «Malaysia» ] .',
            '1. «Saya orang Jepun.»', '2. «Dia orang Malaysia.»', '3. «Kami orang Jepun.»', '4. «Mereka orang Malaysia.»',
            'Table 2: [ «Nama saya» / «Namanya» ] [ Tanaka / Aini / Mei Ling ] .',
            '5. «Nama saya Tanaka.»', '6. «Namanya Aini.»', '7. «Nama saya Mei Ling.»',
            'Table 3: «Asal» [ «saya» / «dia» / «mereka» ] «dari» [ Osaka / Ipoh / Penang ] .',
            '8. «Asal saya dari Osaka.»', '9. «Asal dia dari Ipoh.»', '10. «Asal mereka dari Penang.»',
            'Now read the combinations that are not printed.'])],
        key=['All combinations are correct. Listen for «orang» before the country and «Nama saya», not «Saya nama».']))
    C.append(dict(
        slug='drill-2-substitution', type='Drill', sub_type='substitute', title='Drill 2 · Substitution', block='B', minutes=3,
        grammar=[G['pron'], G['nn'], G['origin']], patterns=['ms-c02-f03'], goal=GOALS['B'],
        explain=('（　）の言葉を入れて言いかえます。前の答えが次の文のもとになります。',
                 'Replace one part with the cue. Each answer becomes the next starting sentence.'),
        sections=[('Change one part · 一つだけ変える', [
            'Start: «Saya orang Jepun. Asal saya dari Osaka.»',
            '1. ( Kyoto ) → ____________________', '2. ( «dia» ) → ____________________',
            '3. ( Malaysia, Ipoh ) → ____________________', '4. ( «mereka» ) → ____________________',
            '5. ( «kami», «Jepun», Sapporo ) → ____________________', '6. ( «Encik» Kimura ) → ____________________',
            'Start: «Siapa nama encik?»',
            '7. ( «puan» ) → ____________________', '8. ( «kawan awak» ) → ____________________'])],
        key=['1 «Saya orang Jepun. Asal saya dari Kyoto.» 2 «Dia orang Jepun. Asal dia dari Kyoto.» 3 «Dia orang Malaysia. Asal dia dari Ipoh.»',
             '4 «Mereka orang Malaysia. Asal mereka dari Ipoh.» 5 «Kami orang Jepun. Asal kami dari Sapporo.» 6 «Encik Kimura orang Jepun. Asal dia dari Sapporo.»',
             '7 «Siapa nama puan?» 8 «Siapa nama kawan awak?»']))
    C.append(dict(
        slug='drill-3-transformation', type='Drill', sub_type='transform', title='Drill 3 · Transformation', block='B', minutes=4,
        grammar=[G['pron'], G['qw'], G['demo'], G['nya'], G['also']], patterns=['ms-c02-f01', 'ms-c02-f02', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('指示どおりに形を変えます（文から質問へ、«-nya»、「あなた」の言いかえ、«kami» と «kita»、«ini» と «itu»）。',
                 'Change the form as the cue says: statement to question, «-nya», a different "you", «kami» or «kita», «ini» or «itu».'),
        sections=[('Change the form · 形を変える', [
            '1. Make it a yes/no question: «Encik orang Jepun.» → ____________________',
            '2. Ask for the name: «Nama dia Ali.» → ____________________',
            '3. Ask where: «Kampung dia di Ipoh.» → ____________________',
            '4. Use «-nya»: «Nama dia Ali.» → ____________________',
            '5. Ask a friend your age, not a manager: «Siapa nama encik?» → ____________________',
            '6. The listener is Japanese too: «Kami orang Jepun.» → ____________________',
            '7. Add "also": «Saya orang Jepun.» → ____________________',
            '8. He is far away now: «Ini Encik Rahman.» → ____________________'])],
        key=['1 «Encik orang Jepun?» (rising voice) 2 «Siapa nama dia?» 3 «Kampung dia di mana?» 4 «Namanya Ali.»',
             '5 «Siapa nama awak?» 6 «Kita orang Jepun.» 7 «Saya juga orang Jepun.» (or «Saya pun orang Jepun.») 8 «Itu Encik Rahman.»',
             'Positive to negative with nouns needs ‹bukan› (chapter 3), so it is not drilled yet.']))
    C.append(dict(
        slug='drill-4-question-answer', type='Drill', sub_type='question and answer', title='Drill 4 · Question and answer', block='B', minutes=4,
        grammar=[G['nn'], G['qw'], G['origin']], patterns=['ms-c02-f01', 'ms-c02-f02', 'ms-c02-f03', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('前半は自分のことで答えます。後半は答えを聞いて、それに合う質問を言います。',
                 'Part 1: answer about yourself. Part 2: hear the answer and ask the question that fits.'),
        sections=[('Part 1 · Answer · 答える', [
            '1. «Siapa nama encik?» → ____________________', '2. «Encik orang Jepun?» → ____________________',
            '3. «Kampung encik di mana?» → ____________________', '4. «Itu siapa?» (Mei Ling) → ____________________']),
            ('Part 2 · Reverse · 質問を言う', [
            '5. ____________________ → «Nama saya Rahman.»', '6. ____________________ → «Kampung saya di Kyoto.»',
            '7. ____________________ → «Dia kawan saya.»', '8. ____________________ → «Tidak, saya orang Malaysia.»'])],
        key=['1 «Nama saya …» 2 «Ya, saya orang Jepun.» 3 «Kampung saya di …» 4 «Itu Cik Mei Ling.»',
             '5 «Siapa nama encik?» 6 «Kampung encik di mana?» 7 «Dia siapa?» 8 «Encik orang Jepun?» (any title or «awak»)']))
    C.append(dict(
        slug='drill-5-question-word-choice', type='Drill', sub_type='question-word choice', title='Drill 5 · Question-word choice', block='B', minutes=3,
        grammar=[G['qw']], patterns=['ms-c02-f02', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('これまでの疑問詞（«apa»・«siapa»・«di mana»）から、答えに合うものを選びます。',
                 'Choose from every question word so far («apa», «siapa», «di mana») to fit the answer.'),
        sections=[('Choose · 選ぶ', [
            'Box: «apa» / «siapa» / «di mana»',
            '1. «___ khabar, Puan?» — «Khabar baik.»', '2. «___ nama encik?» — «Nama saya Kimura.»',
            '3. «Kampung awak ___ ?» — «Di Fukuoka.»', '4. «Itu ___ ?» — «Itu kawan saya, Ali.»',
            '5. «Encik Rahman ___ ?» — «Dia di Bangsar.»', '6. «___ negara asal awak?» — «Jepun.»',
            '7. «Dia ___ ?» — «Dia Puan Aini.»', '8. «Osaka ___ ?» — «Osaka di Jepun.»',
            'Question-word set to date: chapter 1 «apa»; unit 2A «siapa», «di mana». Unit 2B adds the -kah forms, «adakah» and «bolehkah».'])],
        key=['1 «Apa» 2 «Siapa» 3 «di mana» 4 «siapa» 5 «di mana» 6 «Apa» 7 «siapa» 8 «di mana»']))
    C.append(dict(
        slug='drill-6-short-dialogue', type='Drill', sub_type='free', title='Drill 6 · Short dialogues', block='B', minutes=3,
        grammar=[G['pron'], G['nn'], G['qw'], G['origin'], G['nya']], patterns=['ms-c02-f01', 'ms-c02-f02', 'ms-c02-f03'], goal=GOALS['B'],
        explain=('場面のヒントで二行の会話を読み、もう一行を自分で足します。役を交代しましょう。',
                 'Read the two lines in the cued situation, then add one more line of your own. Swap roles.'),
        sections=[('Two turns, then add one · 二行＋一行', [
            'Dialogue 1 · the pantry, a new colleague about your age',
            'A: «Selamat pagi. Siapa nama awak?»  B: «Nama saya Farah. Awak pula?»  A: ____________________',
            'Dialogue 2 · you introduce your friend Kenji to «Puan» Aini',
            'A: «Puan Aini, ini kawan saya.»  B: «Oh! Siapa namanya?»  A: ____________________',
            'Dialogue 3 · someone thinks you are from Tokyo',
            'A: «Encik dari Tokyo?»  B: «Tidak, saya dari Osaka.»  A: ____________________',
            'Dialogue 4 · an old friend you have not seen for a long time',
            'A: «Lama tak jumpa! Apa khabar?» (spoken)  B: «Khabar baik! Awak pula?»  A: ____________________'])],
        key=['Possible third lines: 1 «Nama saya Yuki. Selamat berkenalan.» 2 «Namanya Kenji. Dia orang Jepun.» '
             '3 «Oh, kampung saya pun di Osaka!» 4 «Saya pun baik. Jom, kita jumpa nanti!»',
             'Accept any third line that fits the person and the turn before it.']))
    C.append(dict(
        slug='drill-question-word-set', type='Drill', sub_type='question-word set', title='Cumulative question-word drill', block='D', minutes=5,
        grammar=[G['qw'], 'ms-c01-g04'], patterns=['ms-c01-f02', 'ms-c02-f02', 'ms-c02-f08'], goal=GOALS['D'],
        explain=('これまでの疑問詞をすべて使って、新しい同僚にたずねます。相手はプロフィールカードを見て答えます。',
                 'Use every question word so far to interview a new colleague. Your partner answers from the profile card.'),
        sections=[('Interview · インタビュー', [
            'Set to date: «apa» (chapter 1), «siapa», «di mana» (unit 2A).',
            'Profile card (partner B): Kenji · Japan · hometown Fukuoka · now at the Bangsar office · fine today',
            '1. how they are → ____________________', '2. their name → ____________________',
            '3. their country → ____________________', '4. their hometown → ____________________',
            '5. where they are now → ____________________', '6. who the person at the door is (Mei Ling) → ____________________'])],
        key=['1 «Apa khabar?» 2 «Siapa nama awak?» (or a title) 3 «Apa negara asal awak?» / «Awak orang Jepun?» 4 «Kampung awak di mana?» '
             '5 «Awak di mana?» — «Saya di Bangsar.» 6 «Itu siapa?» — «Itu Cik Mei Ling.»']))

    # Model conversation ----------------------------------------------------
    model = [('Farah', '«Selamat pagi, Encik. Siapa nama encik?»'), ('Tanaka', '«Selamat pagi. Nama saya Tanaka. Cik pula?»'),
             ('Farah', '«Nama saya Farah. Selamat berkenalan.»'), ('Tanaka', '«Selamat berkenalan, Cik Farah.»'),
             ('Farah', '«Encik orang Jepun?»'), ('Tanaka', '«Ya, saya orang Jepun. Asal saya dari Osaka.»'),
             ('Farah', '«Wah, Osaka! Itu Kumar. Dia kawan saya.»'), ('Kumar', '«Selamat pagi. Apa khabar?»'),
             ('Tanaka', '«Khabar baik, terima kasih. Selamat berkenalan, Encik Kumar.»'), ('Kumar', '«Selamat berkenalan. Kampung encik di mana?»'),
             ('Tanaka', '«Di Osaka. Encik pula?»'), ('Kumar', '«Kampung saya di Ipoh. Farah juga dari Ipoh.»'),
             ('Tanaka', '«Oh, Cik Farah pun dari Ipoh?»'), ('Farah', '«Ya! Jom, kita jumpa lagi nanti.»')]
    gapped = [('Farah', '«Selamat pagi, Encik. ___ nama encik?»'), ('Tanaka', '«Selamat pagi. ___ saya Tanaka. Cik pula?»'),
              ('Farah', '«Nama saya Farah. Selamat berkenalan.»'), ('Tanaka', '«Selamat berkenalan, Cik Farah.»'),
              ('Farah', '«Encik ___ Jepun?»'), ('Tanaka', '«Ya, saya orang Jepun. ___ saya dari Osaka.»'),
              ('Farah', '«Wah, Osaka! ___ Kumar. ___ kawan saya.»'), ('Kumar', '«Selamat pagi. Apa khabar?»'),
              ('Tanaka', '«Khabar baik, terima kasih. Selamat berkenalan, Encik Kumar.»'), ('Kumar', '«Selamat berkenalan. Kampung encik di ___ ?»'),
              ('Tanaka', '«Di Osaka. Encik pula?»'), ('Kumar', '«Kampung saya di Ipoh. Farah ___ dari Ipoh.»'),
              ('Tanaka', '«Oh, Cik Farah ___ dari Ipoh?»'), ('Farah', '«Ya! ___ , kita jumpa lagi nanti.»')]
    variant = [('Hafiz', '«Selamat petang, Cik. Siapa nama cik?»'), ('Yuki', '«Selamat petang. Nama saya Yuki. Encik pula?»'),
               ('Hafiz', '«Nama saya Hafiz. Selamat berkenalan.»'), ('Yuki', '«Selamat berkenalan, Encik Hafiz.»'),
               ('Hafiz', '«Cik orang Jepun?»'), ('Yuki', '«Ya, saya orang Jepun. Asal saya dari Sapporo.»'),
               ('Hafiz', '«Wah, Sapporo! Itu Mei Ling. Dia kawan saya.»'), ('Mei Ling', '«Selamat petang. Apa khabar?»'),
               ('Yuki', '«Baik, terima kasih. Selamat berkenalan, Cik Mei Ling.»'), ('Mei Ling', '«Selamat berkenalan. Kampung cik di mana?»'),
               ('Yuki', '«Di Sapporo. Cik pula?»'), ('Mei Ling', '«Kampung saya di Penang. Hafiz juga dari Penang.»'),
               ('Yuki', '«Oh, Encik Hafiz pun dari Penang?»'), ('Hafiz', '«Ya! Jom, kita jumpa lagi esok.»')]
    C.append(dict(
        slug='model-conversation', type='Model conversation', title='Model conversation', block='B', minutes=15,
        grammar=[G['pron'], G['nn'], G['qw'], G['origin'], G['demo'], G['also']],
        patterns=['ms-c02-f01', 'ms-c02-f02', 'ms-c02-f03', 'ms-c02-f08'], goal=GOALS['B'],
        explain=('給湯室での自己紹介（14ターン）です。ペアで読み、次に空欄版、最後に事実を変えた版を演じます。',
                 'Introductions in the pantry, in 14 turns. Read it in pairs, then the gapped version, then the variant with changed facts.'),
        sections=[('1 · Model: the office pantry · 給湯室で', turns(model)),
                  ('2 · Gapped version · 空欄版', turns(gapped)),
                  ('3 · Variant: changed facts · 事実を変えた版', ['Now it is 4 pm. Yuki from Sapporo meets Hafiz and Mei Ling from Penang.', *turns(variant),
                    'Change two more facts yourselves (a name, a hometown) and play it again.'])],
        key=['Gaps in order: «Siapa», «Nama», «orang», «Asal», «Itu», «Dia», «di mana», «juga», «pun», «Jom».',
             'Variant check: «Selamat petang» at 4 pm; «Cik» for Yuki; «Encik» for Hafiz.',
             'Point out «juga» and «pun» (both "also") and «kita» (including the listener) in «Jom, kita jumpa lagi».']))

    # Listening -----------------------------------------------------------
    script = ['Rahman: «Selamat pagi. Ini Encik Tanaka.»',
              'Tanaka: «Selamat pagi. Nama saya Tanaka. Saya orang Jepun. Asal saya dari Jepun. Kampung saya di Osaka. Selamat berkenalan.»',
              'Rahman: «Terima kasih, Encik Tanaka. Nama saya Rahman. Saya orang Malaysia. Kampung saya di Johor Bahru.»',
              'Aini: «Nama saya Aini. Kampung saya di Ipoh. Itu Cik Mei Ling. Dia kawan saya.»',
              'Mei Ling: «Selamat berkenalan, Encik Tanaka. Saya juga orang Malaysia. Kampung saya di Penang.»',
              'Tanaka: «Selamat berkenalan, Cik Mei Ling. Maaf, tumpang tanya. Encik Kimura di mana?»',
              'Aini: «Encik Kimura? Dia di Bangsar.»',
              'Tanaka: «Oh. Encik Kimura orang Jepun?»',
              'Aini: «Ya, dia orang Jepun. Kampung dia di Kyoto.»',
              'Tanaka: «Wah, betul ke? Kampung isteri saya pun di Kyoto!»',
              'Mei Ling: «Wah! Jom, kita jumpa Encik Kimura nanti.»',
              'Tanaka: «Boleh! Terima kasih, Cik Mei Ling. Jumpa nanti!»',
              'Rahman: «Terima kasih. Selamat datang, Encik Tanaka!»']
    C.append(dict(
        slug='listening', type='Listening', title='Listening focus · Introductions at the morning meeting', block='C', minutes=15,
        grammar=[G['nn'], G['qw'], G['origin'], G['demo'], G['also']], goal=GOALS['C'],
        explain=('朝のミーティングで、田中さんと同僚が自己紹介をします。名前と出身を聞き取りましょう。台本は先生用のページにあります。',
                 'At the morning meeting, «Encik» Tanaka and his colleagues introduce themselves. Listen for names and hometowns. The script is on the teacher page.'),
        sections=[('Before listening · 聞く前に', [
            'You will hear four people: Tanaka, Rahman, Aini and Mei Ling. Copy this table. Guess: who is from Japan?',
            'Name | country | hometown', 'Tanaka | ________ | ________', 'Rahman | ________ | ________',
            'Aini | ________ | ________', 'Mei Ling | ________ | ________']),
            ('While listening · 聞きながら', [
            '1. Fill in the table as you listen.',
            '2. Where is Tanaka\'s hometown?', '3. Where is Rahman\'s hometown?', '4. Who is Mei Ling to Aini?',
            '5. Is Mei Ling Japanese or Malaysian? How do you know?', '6. Where is «Encik» Kimura today?',
            '7. Where is Kimura\'s hometown, and why is Tanaka surprised?', '8. What does Mei Ling suggest at the end?']),
            ('After listening · 聞いたあとで', [
            'Close the table. Introduce one person from the meeting to your partner: «Ini …» Then use «Dia …» twice.',
            'Then introduce yourself in the same way to the class.',
            '表を閉じて、ミーティングの人を一人紹介しましょう。そのあと自分も同じように自己紹介します。'])],
        key=[f'Teacher script (read twice). Malay words: {malay_words(script)}.', *script,
             'Answers: Tanaka Japan, Osaka; Rahman Malaysia, Johor Bahru; Aini (Malaysia), Ipoh; Mei Ling Malaysia, Penang.',
             '2 Osaka 3 Johor Bahru 4 her friend («kawan») 5 Malaysian: «Saya juga orang Malaysia» 6 in Bangsar 7 Kyoto; his wife\'s hometown is also Kyoto 8 to meet Kimura later']))

    # Reading and writing ----------------------------------------------------
    C.append(dict(
        slug='reading-writing', type='Reading and writing', title='Reading and writing · Name tags at a welcome event', sub_type='form',
        block='C', minutes=10, grammar=[G['nn'], G['origin'], G['pron']], goal=GOALS['C'],
        explain=('歓迎会の名札を読み、質問に答えます。次に自分の名札を書き、自分とクラスメートについて文を書きます。',
                 'Read the name tags from a welcome event and answer the questions. Then fill in your own tag and write about yourself and a classmate.'),
        sections=[('Read · 読む', [
            'Sign: «SELAMAT DATANG, KAWAN!»',
            'Tag 1 · «Nama:» Tanaka Kenji · «Negara:» «Jepun» · «Kampung:» Osaka',
            'Tag 2 · «Nama:» Siti · «Negara:» Malaysia · «Kampung:» Kuala Lumpur',
            'Tag 3 · «Nama:» Kumar · «Negara:» Malaysia · «Kampung:» Ipoh',
            'Tag 4 · «Nama:» Yamada Yuki · «Negara:» «Jepun» · «Kampung:» Sapporo',
            'Tag 5 · «Nama:» Lim Mei Ling · «Negara:» Malaysia · «Kampung:» Penang']),
            ('Questions · 質問', [
            '1. Who is from Japan?', '2. Whose hometown is Ipoh?', '3. Is Siti Japanese or Malaysian?',
            '4. Where is Yuki\'s hometown?', '5. Write a sentence about Mei Ling with «Dia …»: ____________________',
            '6. Write a sentence about Tanaka and Yuki together with «Mereka …»: ____________________']),
            ('Write · 書く', [
            'Your tag · «Nama:» ________ · «Negara:» ________ · «Kampung:» ________',
            'Write three sentences about yourself and two about a classmate.',
            '____________________________________________', '____________________________________________',
            '____________________________________________', 'Check: «Nama saya …»; «orang» before the country; «di» before the place.'])],
        key=['1 Tanaka and Yamada Yuki. 2 Kumar. 3 Malaysian. 4 Sapporo. 5 «Dia orang Malaysia. Kampung dia di Penang.» 6 «Mereka orang Jepun.»',
             'Model (self): «Nama saya Yamada Yuki. Saya orang Jepun. Kampung saya di Sapporo.»',
             'Model (classmate): «Namanya Kumar. Dia orang Malaysia. Kampung dia di Ipoh.»']))

    C.append(dict(
        slug='task', type='Task', title='Task · Meet people at a welcome event', sub_type='role-play', block='C', minutes=15,
        grammar=[G['pron'], G['nn'], G['qw'], G['origin'], G['demo'], G['nya']], goal=GOALS['C'],
        explain=('役割カードを使って、歓迎会で台本なしで自己紹介をします。途中で予定の変更があります。',
                 'Use the role cards to introduce yourselves at a welcome event with no script. A change of plan follows.'),
        sections=[('Role card A · 新しく来た人', [
            'You are new at the company. Find out B\'s name, country and hometown. Tell B yours.',
            'Then introduce your friend: Ken, Japanese, hometown Nagoya.',
            'あなたは新入社員です。Bの名前・国・出身地をたずね、自分のことも話します。そのあと友達のケン（日本人、名古屋出身）を紹介します。']),
            ('Role card B · 社員', [
            'You work here. Your name: choose one. Country: Malaysia. Hometown: Ipoh or Penang.',
            'Answer A\'s questions and ask the same back. Ask who A\'s friend is.',
            'あなたは社員です。名前を一つ選びます。国はマレーシア、出身はイポーかペナン。Aの質問に答え、同じ質問を返し、Aの友達がだれかたずねます。']),
            ('Change of plan · 予定の変更', [
            'Your manager arrives. A introduces B to the manager using «ini» and «-nya», with the right title.',
            'Then B thinks A is from Tokyo. A corrects it politely.',
            'マネージャーが来ました。Aは «ini» と «-nya» を使って、正しい敬称でBを紹介します。次に、BはAを東京出身だと思っています。Aは丁寧に訂正します。']),
            ('Success criteria · 先生が確認すること', [
            '☐ «Nama saya …» and «Siapa nama …?» are used correctly.', '☐ Nationality with «orang» + country; hometown with «di».',
            '☐ «di mana» and «siapa» questions are understood and answered.', '☐ The friend is introduced with «ini» and «-nya» or «Dia».',
            '☐ The right "you": a title for the manager, «awak» only for a peer.', '☐ The correction uses «Tidak, …» and the right place.'])],
        key=['Sample: A «Selamat pagi. Nama saya Tanaka. Siapa nama awak?» B «Nama saya Siti. Awak orang Jepun?» A «Ya. Kampung saya di Osaka. Kampung awak di mana?» B «Di Ipoh.»',
             'Friend: A «Ini kawan saya. Namanya Ken. Dia orang Jepun. Kampung dia di Nagoya.»',
             'Change: A «Encik Rahman, ini Siti. Dia dari Ipoh.» / A «Tidak, saya dari Osaka.»']))

    culture_en = [
        'Malay has several words for "you", and choosing one is a social decision. With someone senior or someone you have just met, '
        'avoid a pronoun and use the title: «Encik pula?», «Puan orang Malaysia?» «Awak» is the everyday "you" between colleagues of a similar age. '
        '«Anda» is formal and impersonal: you see it on signs, forms and adverts. «Kamu» is for children and juniors, and «engkau» or «kau» '
        'only for very close friends; it can sound rude to a stranger. «Aku», the casual "I", goes with «kau».',
        'Two words mean "we". «Kami» leaves the listener out; «kita» takes the listener in. «Kami orang Jepun» tells a Malaysian that you and your '
        'friends are Japanese; «Jom, kita jumpa nanti» includes the person you are talking to. Japanese 私たち covers both.',
        '«Dia» means both "he" and "she". For a respected person, such as a manager or a minister, Malaysians often say «beliau».',
        'Names follow their own customs. In most Malay names the second part is the father\'s name, not a family name, '
        'so the title goes with the person\'s own name: «Encik» Rahman. Chinese Malaysian names put the family name first, as Japanese names do.']
    C.append(dict(
        slug='culture-note', type='Culture note', title='Culture and usage note · Choosing "you"', block='E', minutes=10,
        grammar=[G['pron'], G['also']], goal=GOALS['E'],
        explain=('「あなた」の選び方、«kami» と «kita»、名前の習慣について読みます（英語と日本語）。',
                 'Read how to choose "you", the difference between «kami» and «kita», and name customs (English and Japanese).'),
        sections=[('English', culture_en),
                  ('日本語', [
                      'マレー語には「あなた」にあたる語がいくつもあり、どれを選ぶかは人間関係の問題です。目上の人や初対面の人には代名詞を避け、敬称を使います：'
                      '«Encik pula?»、«Puan orang Malaysia?»。«Awak» は同年代の同僚どうしのふだんの「あなた」。«Anda» は改まった、相手を特定しない言い方で、'
                      '看板・書類・広告で見かけます。«Kamu» は子どもや目下の人に、«engkau»・«kau» はごく親しい友達だけに使い、知らない人には失礼に聞こえます。'
                      'くだけた「私」の «Aku» は «kau» とセットです。',
                      '「私たち」も二つあります。«Kami» は聞き手を含まず、«kita» は聞き手を含みます。«Kami orang Jepun» はマレーシア人に「私たちは日本人です」と伝え、'
                      '«Jom, kita jumpa nanti» は話している相手も含みます。日本語の「私たち」は両方を表します。',
                      '«Dia» は「彼」と「彼女」の両方です。マネージャーや大臣など敬意を払う人には «beliau» がよく使われます。',
                      '名前の習慣もさまざまです。マレー系の名前の多くは、後半が父親の名前で家族の姓ではありません。そのため敬称は本人の名前につけます：«Encik» Rahman。'
                      '中華系マレーシア人の名前は、日本人と同じく姓が先です。'])],
        key=['Sources: Kata-Kata card notes ms-c02-006 (avoid «engkau» with strangers) and ms-c02-007 («dia» has no gender); ledger meanings L-0037 to L-0046.',
             'Unverified: the name-custom paragraph is general knowledge, not from Sam\'s notes or a cited source. Sam to confirm.',
             f'English text: {english_words(culture_en)} words. Discussion: which "you" would you use with «Encik» Rahman, with a friend, on a form?']))

    tests = [
        dict(sub_type='listening', prompt='L1. Listen. What is the person\'s name?', answer='Teacher reads: «Nama saya Kumar.» Answer: Kumar',
             words=['nama', 'saya'], grammar=[G['nn']]),
        dict(sub_type='listening', prompt='L2. Listen. Is the person Japanese or Malaysian?', answer='Teacher reads: «Saya orang Malaysia.» Answer: Malaysian',
             words=['orang'], grammar=[G['origin']]),
        dict(sub_type='listening', prompt='L3. Listen. Where is the hometown?', answer='Teacher reads: «Kampung saya di Sapporo.» Answer: Sapporo',
             words=['kampung', 'di'], grammar=[G['origin']]),
        dict(sub_type='listening', prompt='L4. Listen. Who is Ali to the speaker?', answer='Teacher reads: «Ini Ali. Dia kawan saya.» Answer: a friend',
             words=['ini', 'dia', 'kawan'], grammar=[G['demo'], G['pron']]),
        dict(sub_type='listening', prompt='L5. Listen and choose the answer: a «Nama saya Yuki.» b «Kampung saya di Kyoto.» c «Khabar baik.»',
             answer='Teacher reads: «Kampung awak di mana?» Answer: b', words=['di mana', 'kampung'], grammar=[G['qw']]),
        dict(sub_type='grammar', prompt='V1. Ask a new colleague\'s name politely (a man): «___ nama encik?»', answer='«Siapa»', words=['siapa'], grammar=[G['qw']]),
        dict(sub_type='grammar', prompt='V2. Put in order: «Jepun / saya / orang»', answer='«Saya orang Jepun.»', words=['orang Jepun'], grammar=[G['nn'], G['origin']]),
        dict(sub_type='words', prompt='V3. "We" including the listener: ____ ', answer='«kita»', words=['kita'], grammar=['ms-c02-g13']),
        dict(sub_type='words', prompt='V4. "We" not including the listener: ____ ', answer='«kami»', words=['kami'], grammar=['ms-c02-g13']),
        dict(sub_type='grammar', prompt='V5. His name: «nama dia» = «nama___»', answer='«namanya»', words=['-nya', 'nama'], grammar=[G['nya']]),
        dict(sub_type='grammar', prompt='V6. That person is far away: «___ Encik Rahman.»', answer='«Itu»', words=['itu'], grammar=[G['demo']]),
        dict(sub_type='words', prompt='V7. Which "you" do you see on forms and adverts? ( «awak» / «anda» / «kau» )', answer='«anda»', words=['anda'], grammar=[G['pron']]),
        dict(sub_type='grammar', prompt='V8. «Kampung puan ___ ?» — «Di Ipoh.»', answer='«di mana»', words=['di mana'], grammar=[G['qw']]),
        dict(sub_type='reading', prompt='R1. Read the tag above. What is this person\'s name?', answer='Hiro', words=['nama'], grammar=[G['nn']]),
        dict(sub_type='reading', prompt='R2. Which country is he from?', answer='Japan («Jepun»)', words=['negara', 'Jepun'], grammar=[G['origin']]),
        dict(sub_type='reading', prompt='R3. Where is his hometown?', answer='Fukuoka', words=['kampung'], grammar=[G['origin']]),
        dict(sub_type='reading', prompt='R4. Write one sentence about him with «Dia»: ____________________', answer='«Dia orang Jepun.» or «Kampung dia di Fukuoka.»',
             words=['dia', 'orang Jepun'], grammar=[G['pron'], G['nn']]),
        dict(sub_type='speaking', prompt='S1. Speaking: your teacher is a new colleague. Ask their name, country and hometown, answer the same questions, and introduce a classmate.',
             answer='Check: «Siapa nama …?»; «… orang …?»; «Kampung … di mana?»; «Ini … Namanya …»', words=['siapa', 'orang', 'di mana', 'ini'],
             grammar=[G['qw'], G['origin'], G['demo']]),
    ]
    C.append(dict(
        slug='test', type='Test', title='Unit test and self-check', block='D', minutes=20,
        grammar=[G['pron'], G['nn'], G['qw'], G['origin'], G['demo'], G['nya'], 'ms-c02-g13'], goal=GOALS['D'], tests=tests,
        explain=('10分の小テストです（点数より確認のため）。聞く・単語と文法・読む、そして話す課題が一つあります。最後に「できる」チェックをします。',
                 'A ten-minute, low-stakes check: listening, words and grammar, reading, and one speaking task. Then tick the "I can" list.'),
        sections=[('Listening · 聞く (teacher reads each line twice)', [t['prompt'] for t in tests if t['sub_type'] == 'listening']),
                  ('Words and grammar · 単語と文法', [t['prompt'] for t in tests if t['sub_type'] in ('words', 'grammar')]),
                  ('Reading · 読む', ['Name tag: «Nama:» Hiro · «Negara:» «Jepun» · «Kampung:» Fukuoka',
                                      *[t['prompt'] for t in tests if t['sub_type'] == 'reading']]),
                  ('Speaking · 話す', [t['prompt'] for t in tests if t['sub_type'] == 'speaking']),
                  ('Self-check · できるチェック', [f'☐ {GOALS[b]} / {GOALS_JA[b]}' for b in 'ABCE'] + [
                      'One thing I will practise in Kata-Kata this week: ____________________'])],
        key=[f'{t["prompt"].split(".")[0]}: {t["answer"]}' for t in tests] + ['Low-stakes: note missed items for the unit 2B recall.']))

    C.append(dict(
        slug='teaching-plan', type='Teaching plan', title='Teaching plan and answer key', block='All', minutes=None,
        grammar=[G['pron'], G['nn'], G['qw'], G['origin'], G['demo'], G['nya'], 'ms-c02-g13'],
        patterns=['ms-c02-f01', 'ms-c02-f02', 'ms-c02-f03', 'ms-c02-f08'],
        explain=('先生用：五つのブロック（各45分）の時間配分、指示、予想される答え、Kata-Kata の宿題。',
                 'For the teacher: timings for the five 45-minute blocks, prompts, expected answers and Kata-Kata homework.'),
        sections=[
            ('Before and after · 授業の前後', [
                'Before Block A: Kata-Kata Sedia Kelas c02 (27 cards; frames ms-c02-f01, f02). Collect Tanya Cikgu questions.',
                'After Block B: the unit 2A cards with spaced review. Before Block E: the Dunia scene "Sembang di pantri".',
                'After Block D: Kata-Kata cards for unit 2B (work, home, family, pe- and -an). Planning figure: about 3 hours of Kata-Kata for this unit.',
                'Hanashishou starts at A2: no link yet. Audio: teacher-read scripts only.']),
            ('Block A · Words and patterns (45 min)', [
                'Goal: ' + GOALS['A'],
                '0–5 Recall (Opener): greetings at four times. Expected: «Selamat pagi …», «Apa khabar?», «… pula?»',
                '5–10 Tanya Cikgu. 10–20 Vocabulary: point at people for pronouns; ask which "you" for a manager (expected: the title).',
                '20–40 Patterns 1 to 4: model the A lines; the class answers with their own facts. Prompt: "Is it «Saya nama» or «Nama saya»?" Expected: «Nama saya».',
                '40–45 First substitutions: Drill 2, items 1 to 3.']),
            ('Block B · Drills and conversation (45 min)', [
                'Goal: ' + GOALS['B'],
                '0–5 Recall: "Ask my name." Expected: «Siapa nama puan?» / «Siapa nama encik?»',
                '5–25 Drill ladder in order, types 1 to 6. In drill 3, stress «kami» against «kita».',
                '25–40 Model conversation, gapped version, variant. 40–45 Pair rehearsal with real facts.']),
            ('Block C · Listening and task (45 min)', [
                'Goal: ' + GOALS['C'],
                '0–5 Recall: "Introduce your partner." Expected: «Ini … Namanya … Dia orang …»',
                '5–20 Listening: the table first, the script twice (on the listening key), then the questions.',
                '20–30 Name tags: six questions, then the learner\'s own tag and sentences.',
                '30–45 Task: role cards; announce the manager\'s arrival at minute 38.']),
            ('Block D · Review and test (45 min)', [
                'Goal: ' + GOALS['D'],
                '0–15 Mixed review: cumulative question-word drill, then chapter 1 greetings with the new questions.',
                '15–25 Unit test. 25–35 Self-check and feedback. 35–45 Preview the Kata-Kata unit 2B cards (work, home, family).']),
            ('Block E · Scene (45 min)', [
                'Goal: ' + GOALS['E'],
                '0–5 Recall: "Which "you" on a form?" Expected: «anda».',
                '5–15 Scene listening: play or read the Kata-Kata Dunia scene "Sembang di pantri" (cards ms-d-pejabat-sembang-01 to 12).',
                '15–30 Role-play the pantry chat in threes. 30–40 Free variation: an old friend arrives («Lama tak jumpa!»).',
                '40–45 Culture note on choosing "you". No Hanashishou link at A1.']),
            ('What to listen for · 注意点', [
                '«Nama saya» (not «Saya nama»); «orang Jepun» (not «Jepun orang»); «di» before the place.',
                'A title, not «awak», with seniors. «kami» against «kita». Spoken scene words are recognised first, then used only in chat.',
                'Not taught: ‹dari mana› (chapter 7 in the ledger) and ‹bukan› (chapter 3); use «Kampung … di mana?» and «Tidak, …» instead.'])],
        key=['Answer keys are on each component\'s teacher page. This plan follows the block timings in charter section 6.',
             'All Japanese in this unit is a draft awaiting native review.']))
    return C


UNIT = dict(
    unit_id='ms-c02a', label='2A', chapter_id='ms-c02', check_unit='ms-c02a', id_prefix='ms-c02a', title_prefix='Unit 2A',
    header='Unit 2A (ms-c02a)', menu_title='Chapter 2 · Pronouns and self-introduction', genre='Social life',
    goal='Introduce yourself (name, nationality, hometown), ask the same of others and introduce a friend.',
    blocks=GOALS, prerequisites=['ms-c01'], prerequisite_units=[], prereq_grammar=['ms-c01-g02', 'ms-c01-g03', 'ms-c01-g04'],
    word_scope=WORDS, components=components)
