"""Unit 10A: ber- verbs of the working day, movement and free time (Setiap pagi saya ___ pukul ___; Pukul berapa ___
bermula / kita bertolak?; Pada hujung minggu saya suka ___; Saya bercakap / berbual dengan ___).

20 core ledger entries, the rows the ledger places in "Ch10 (unit 10A)" (L-1089 to L-1106 except the 10B rows, plus
L-0807 «bersiap» and L-0916 «bersedia»), in three groups. Each ber- verb is taught as a whole ledger form with its root,
as the Kata-Kata card note gives it: ber- has no nasal sound changes; its only spelling variants are be- (berehat,
berenang, bekerja) and bel- (belajar, revision from chapter 2). No meN- (chapter 11), no -kan or -i (chapter 12), and no
ber- word that is not its own ledger row. The scene follows Kata-Kata c10 (scenario lines ms-c10-s01 to s09: a working
day with Puan Aini) and goes further in class: a team message, a routine role-play and a changed workday. No Dunia scene
primes chapter 10, so there is no recognition word in this unit. All names, times and routines are fictional.
Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

DAY = ['L-0807', 'L-1101', 'L-1106', 'L-1090', 'L-1100', 'L-1102', 'L-1089', 'L-1093', 'L-1103', 'L-1105']
TALK = ['L-1091', 'L-1099', 'L-1098', 'L-0916']
FREE = ['L-1092', 'L-1094', 'L-1095', 'L-1096', 'L-1097', 'L-1104']
CORE = DAY + TALK + FREE

# Revision: words placed in chapters 1 to 9 that the unit really uses (a test fails if one is not used).
REV_ROOTS = ['L-0065', 'L-0473', 'L-0074', 'L-0614', 'L-0204', 'L-1087', 'L-0576', 'L-0417',
             'L-0069']
REV_TIME = ['L-0157', 'L-0182', 'L-0184', 'L-0183', 'L-0185', 'L-0186', 'L-0702', 'L-0193', 'L-0194', 'L-0189', 'L-0191',
            'L-0192', 'L-0195', 'L-1046', 'L-1001', 'L-1002']
REV_WORK = ['L-0064', 'L-0208', 'L-0090', 'L-0066', 'L-0295', 'L-0339', 'L-0340', 'L-0531', 'L-0968', 'L-1025']

EXAMPLES = {
    # A working day
    'L-0807': '«Saya bersiap untuk ke pejabat.»',
    'L-1101': '«Saya bersarapan di rumah pukul tujuh.» (everyday: «Saya sarapan di rumah.»)',
    'L-1106': '«Pukul berapa kita bertolak?»',
    'L-1090': '«Saya berjalan kaki ke stesen.»',
    'L-1100': '«Waktu pagi, ramai orang beratur di stesen.»',
    'L-1102': '«Mesyuarat bermula pukul sembilan.»',
    'L-1089': '«Saya bekerja di Kuala Lumpur.» (everyday: «Saya kerja di KL.»)',
    'L-1093': '«Selepas makan tengah hari, kami berehat sekejap.»',
    'L-1103': '«Bas itu berhenti di depan pejabat.»',
    'L-1105': '«Itu rutin saya setiap hari.»',
    # Talking and meeting
    'L-1091': '«Saya bercakap bahasa Melayu dengan Puan Aini.»',
    'L-1099': '«Kami berbual di kedai mamak.»',
    'L-1098': '«Saya berjumpa dengan pengurus pukul sepuluh.»',
    'L-0916': '«Encik sudah bersedia untuk mesyuarat?»',
    # Exercise and free time
    'L-1092': '«Pada hari Sabtu saya bermain badminton.»',
    'L-1094': '«Saya bersenam setiap pagi.»',
    'L-1095': '«Pada hari Ahad saya berenang.»',
    'L-1096': '«Saya berlari selepas kerja.»',
    'L-1097': '«Kami berbasikal pada hari Ahad.»',
    'L-1104': '«Saya berlatih bercakap bahasa Melayu setiap malam.»',
    # Revision · roots and belajar
    'L-0065': '«kerja» → «bekerja»: «Saya bekerja di pejabat.»',
    'L-0473': '«cakap» → «bercakap»: «Saya bercakap bahasa Melayu.»',
    'L-0074': '«main» → «bermain»: «Saya bermain badminton.»',
    'L-0614': '«sarapan» → «bersarapan»: «Sudah sarapan?»',
    'L-0204': '«mula» → «bermula»: «Mesyuarat bermula pukul sembilan.»',
    'L-1087': '«tolak» (push, the door sign) → «bertolak» (set off): «Kita bertolak pukul dua.»',
    'L-0576': '«jumpa» → «berjumpa»: «Jumpa lagi!»',
    'L-0417': '«rehat» → «berehat»: «Waktu rehat pukul satu.»',
    'L-0069': '«belajar» (chapter 2, the only bel- word): «Saya belajar bahasa Melayu.»',
    # Revision · time and markers
    'L-0157': '«Mesyuarat bermula pukul sembilan.»',
    'L-0182': '«Setiap pagi saya bersenam.»',
    'L-0184': '«Biasanya saya bertolak pukul tujuh.»',
    'L-0183': '«Kami selalu berbual pada waktu rehat.»',
    'L-0185': '«Kadang-kadang saya berjalan kaki ke pejabat.»',
    'L-0186': '«Saya jarang berenang.»',
    'L-0702': '«Pada hujung minggu saya suka berenang.»',
    'L-0193': '«Mesyuarat sudah bermula.»',
    'L-0194': '«Saya belum bersarapan.»',
    'L-0191': '«Saya masih bekerja.»',
    'L-0192': '«Esok kami akan bertolak pukul tujuh.»',
    'L-0189': '«Encik Tanaka sedang bersiap.»',
    'L-0195': '«Bas baru berhenti di depan pejabat.»',
    'L-1046': '«Kami berehat sekejap.»',
    'L-1001': '«Saya berlari selepas kerja.»',
    'L-1002': '«Saya bersenam sebelum bersarapan.»',
    # Revision · the office and free time
    'L-0064': '«Saya bertolak ke pejabat pukul tujuh.»',
    'L-0208': '«Mesyuarat bermula pukul sembilan.»',
    'L-0090': '«Saya berjumpa dengan pengurus.»',
    'L-0066': '«Saya bekerja di sebuah syarikat Jepun.»',
    'L-0295': '«Bas berhenti di depan stesen.»',
    'L-0339': '«Saya naik bas ke pejabat.»',
    'L-0340': '«Puan Aini naik kereta api.»',
    'L-0531': '«Saya berbual dengan rakan sekerja.»',
    'L-0968': '«Saya bermain badminton dengan kawan.»',
    'L-1025': '«Rahman bermain golf pada hari Sabtu.»',
}

# Roots as the Kata-Kata card notes give them: «…» where the root is a ledger word placed in chapters 1 to 10,
# ‹…› where it is not a ledger word (or is placed later), so it is quoted, not taught.
ROOTS = {'L-0807': '«siap»', 'L-1101': '«sarapan»', 'L-1106': '«tolak»', 'L-1090': '«jalan»', 'L-1100': '‹atur›',
         'L-1102': '«mula»', 'L-1089': '«kerja»', 'L-1093': '«rehat»', 'L-1103': '‹henti›', 'L-1091': '«cakap»',
         'L-1099': '‹bual›', 'L-1098': '«jumpa»', 'L-0916': '‹sedia›', 'L-1092': '«main»', 'L-1094': '‹senam›',
         'L-1095': '‹renang›', 'L-1096': '‹lari›', 'L-1097': '«basikal»', 'L-1104': '‹latih›'}
_EN = {'L-0807': 'to get ready (the action)', 'L-1101': 'to have breakfast (standard; everyday «sarapan»)',
       'L-1106': 'to set off, to depart (not "push")', 'L-1090': 'to walk («berjalan kaki» = to go on foot)',
       'L-1100': 'to queue', 'L-1102': 'to begin, to start (an event: a meeting, a class)',
       'L-1089': 'to work (standard; everyday «kerja»)', 'L-1093': 'to rest, to take a break',
       'L-1103': 'to stop (careful: «berhenti kerja» = to quit a job)', 'L-1091': 'to speak (a language; «dengan» a person)',
       'L-1099': 'to chat', 'L-1098': 'to meet («berjumpa dengan» a person)', 'L-0916': 'to be ready (the state)',
       'L-1092': 'to play (a game or sport)', 'L-1094': 'to exercise, to work out', 'L-1095': 'to swim', 'L-1096': 'to run',
       'L-1097': 'to cycle', 'L-1104': 'to practise'}
_JA = {'L-0807': '準備する・したくする（動作）', 'L-1101': '朝食をとる（標準；日常は «sarapan»）',
       'L-1106': '出発する（「押す」ではない）', 'L-1090': '歩く（«berjalan kaki»＝歩いて行く）', 'L-1100': '列に並ぶ',
       'L-1102': '始まる（会議・授業などが）', 'L-1089': '働く（標準；日常は «kerja»）', 'L-1093': '休む・休憩する',
       'L-1103': '止まる・やめる（注意：«berhenti kerja»＝仕事を辞める）', 'L-1091': '話す（言語はそのまま、人は «dengan»）',
       'L-1099': 'おしゃべりする', 'L-1098': '会う（人には «berjumpa dengan»）', 'L-0916': '準備ができている（状態）',
       'L-1092': '（遊び・スポーツを）する', 'L-1094': '運動する', 'L-1095': '泳ぐ', 'L-1096': '走る', 'L-1097': '自転車に乗る',
       'L-1104': '練習する'}
VOCAB_OPTS = {lid: {'en': f'{_EN[lid]} (‹ber-› + {ROOTS[lid]})', 'ja': f'{_JA[lid]}（‹ber-› ＋ {ROOTS[lid]}）'} for lid in ROOTS}
VOCAB_OPTS.update({
    'L-1087': {'en': 'push (the door sign «TOLAK», chapter 9)', 'ja': '押す（ドアの表示 «TOLAK»、第9章）'},
    'L-1105': {'en': 'routine («rutin saya setiap hari» = my daily routine)', 'ja': '日課（«rutin saya setiap hari»＝毎日の日課）'},
    'L-1093': {'en': 'to rest, to take a break (‹ber-› + «rehat»; spelt ‹be-› before r)',
               'ja': '休む・休憩する（‹ber-› ＋ «rehat»；r の前では ‹be-› と書く）'},
    'L-1095': {'en': 'to swim (‹ber-› + ‹renang›; spelt ‹be-› before r)', 'ja': '泳ぐ（‹ber-› ＋ ‹renang›；r の前では ‹be-› と書く）'},
    'L-1089': {'en': 'to work (‹ber-› + «kerja»; spelt ‹be-› because the first syllable of «kerja» ends in -er; everyday «kerja»)',
               'ja': '働く（‹ber-› ＋ «kerja»；«kerja» の最初の音節が -er で終わるので ‹be-› と書く；日常は «kerja»）'},
    'L-1103': {'en': 'to stop (‹ber-› + ‹henti›; careful: «berhenti kerja» = to quit a job)',
               'ja': '止まる・やめる（‹ber-› ＋ ‹henti›；注意：«berhenti kerja»＝仕事を辞める）'},
    'L-1106': {'en': 'to set off, to depart (‹ber-› + «tolak»: «tolak» alone means push; with ‹ber-› the meaning changes)',
               'ja': '出発する（‹ber-› ＋ «tolak»：«tolak» だけなら「押す」；‹ber-› が付くと意味が変わる）'},
})

P = [
    ('ms-c10-f01', '«Setiap pagi saya» (ber- verb) «pukul» ___.', [
        'A: «Pukul berapa encik bersarapan?» B: «Setiap pagi saya bersarapan pukul tujuh.»',
        'A: «Pukul berapa encik bertolak ke pejabat?» B: «Setiap pagi saya bertolak pukul tujuh setengah.»',
        'A: «Encik bersenam setiap pagi?» B: «Ya. Setiap pagi saya bersenam pukul enam.»',
        'A: «Encik bekerja dari pukul berapa?» B: «Saya bekerja dari pukul sembilan sampai pukul enam.»',
        'A: «Pukul berapa encik berehat?» B: «Saya berehat sekejap pukul satu, selepas makan tengah hari.»',
        'A: «Pukul berapa encik habis kerja?» B: «Biasanya pukul enam. Kemudian saya berjalan kaki ke stesen.»'],
     "A ber- verb is a root with ‹ber-› in front: «sarapan» → «bersarapan», «kerja» → «bekerja», «tolak» → «bertolak». "
     "These verbs have no object: say what you do, then when («pukul tujuh») or where («di rumah»). Like every Malay verb, a "
     "ber- verb never changes for who or when; the time words of chapter 4 do that job. ‹ber-› has no nasal sound changes: "
     "only ‹be-› before a root that starts with r («berehat», «berenang») and in «bekerja», and ‹bel-› in «belajar» (chapter 2). "
     "In everyday talk people often use the bare root («Saya kerja di KL», «Sudah sarapan?»); the ‹ber-› form is the standard "
     "one, so learn it first. Finishing work for the day is «habis kerja».",
     "ber- の動詞は、語根の前に ‹ber-› を付けた形です：«sarapan» → «bersarapan»、«kerja» → «bekerja»、«tolak» → «bertolak»。"
     "目的語をとらないので、何をするかを言い、そのあとにいつ（«pukul tujuh»）やどこで（«di rumah»）を続けます。マレー語の動詞と同じく、"
     "ber- の動詞も人や時で形が変わりません。時は第4章の時の言葉で表します。‹ber-› には鼻音の変化がありません。r で始まる語根の前"
     "（«berehat»・«berenang»）と «bekerja» で ‹be-› になり、«belajar»（第2章）だけが ‹bel-› です。日常会話では語根だけを使うことも多い"
     "（«Saya kerja di KL»・«Sudah sarapan?»）ですが、‹ber-› の形が標準なので、まずこちらを覚えます。その日の仕事が終わることは «habis kerja» です。",
     'Many ber- verbs match Japanese する verbs («bersenam» 運動する, «berlatih» 練習する), which helps. But ‹ber-› is not ます: it '
     'does not make a verb polite or past, and you cannot add it to any word you like. Learn each ber- verb as a whole word.',
     '多くの ber- の動詞は日本語の「〜する」動詞にあたります（«bersenam» 運動する、«berlatih» 練習する）。ただし ‹ber-› は「ます」ではなく、'
     'ていねいさや過去を表しません。また、どの語にでも付けられるわけではありません。ber- の動詞は一語ずつ覚えましょう。'),
    ('ms-c10-f02', '«Pukul berapa» ___ «bermula»? / «Pukul berapa kita bertolak?»', [
        'A: «Pukul berapa mesyuarat bermula?» B: «Mesyuarat bermula pukul sembilan.»',
        'A: «Pukul berapa kita bertolak?» B: «Kita bertolak pukul dua.»',
        'A: «Kelas bahasa Melayu bermula pukul berapa?» B: «Pukul tujuh malam.»',
        'A: «Bas ini berhenti di stesen?» B: «Ya. Bas ini berhenti di depan stesen.»',
        'A: «Encik sudah bersedia?» B: «Sudah. Kita boleh bertolak sekarang.»',
        'A: «Mesyuarat sudah bermula?» B: «Belum. Mesyuarat bermula pukul sepuluh.»'],
     "«bermula» is what an event does: «Mesyuarat bermula pukul sembilan.» «bertolak» is setting off on a trip or for work: "
     "«Pukul berapa kita bertolak?» Its root «tolak» is the door sign PUSH from chapter 9, but with ‹ber-› the meaning changes, "
     "so never use «bertolak» for pushing. «berhenti» is to stop («Bas berhenti di depan pejabat.»); careful: «berhenti kerja» "
     "means to quit a job, not to stop work for the day («habis kerja»). «bersiap» is getting ready (the action); «bersedia» is "
     "being ready (the state): «Saya sedang bersiap.» → «Saya sudah bersedia.»",
     "«bermula» は行事が始まることです：«Mesyuarat bermula pukul sembilan.» «bertolak» は旅行や仕事に出発することです："
     "«Pukul berapa kita bertolak?» 語根の «tolak» は第9章のドアの表示「押す」ですが、‹ber-› が付くと意味が変わるので、押す意味では使いません。"
     "«berhenti» は止まることです（«Bas berhenti di depan pejabat.»）。注意：«berhenti kerja» は仕事を辞めることで、その日の仕事が終わること"
     "（«habis kerja»）ではありません。«bersiap» は準備をすること（動作）、«bersedia» は準備ができていること（状態）です："
     "«Saya sedang bersiap.» → «Saya sudah bersedia.»",
     'Japanese 始まる and 出発する are the same kind of verb as «bermula» and «bertolak», so the word order is easy. Two Japanese '
     'words mislead: やめる covers both stopping and quitting, but «berhenti kerja» is only quitting; 準備する / 準備ができた is the '
     'same pair as «bersiap» / «sudah bersedia».',
     '日本語の「始まる」「出発する」は «bermula»・«bertolak» と同じ種類の動詞なので、語順はやさしいです。ただし二つの日本語に注意：'
     '「やめる」は止めることにも辞めることにも使いますが、«berhenti kerja» は「辞める」だけです。「準備する／準備ができた」は '
     '«bersiap» と «sudah bersedia» の組み合わせにあたります。'),
    ('ms-c10-f03', '«Pada hujung minggu saya suka» (ber- verb).', [
        'A: «Pada hujung minggu encik buat apa?» B: «Pada hujung minggu saya suka berenang.»',
        'A: «Encik suka bermain badminton?» B: «Suka. Saya bermain badminton pada hari Sabtu.»',
        'A: «Puan suka berlari?» B: «Tidak juga. Saya lebih suka berbasikal.»',
        'A: «Encik selalu bersenam?» B: «Ya. Saya bersenam setiap hari Isnin, Rabu dan Jumaat.»',
        'A: «Apa hobi encik?» B: «Pada hujung minggu saya suka berenang dan berbasikal.»',
        'A: «Encik berlatih apa pada hari Ahad?» B: «Saya berlatih badminton dengan kawan.»'],
     "«suka» goes straight in front of the verb, with nothing in between: «Saya suka berenang.» (I like swimming.) «bermain» "
     "takes the game: «bermain badminton», «bermain golf»; in everyday talk «main badminton» is just as common. «Tidak juga» is the natural, gentle \"not really\"; «lebih suka» means prefer (\"I like cycling more\"). Say how often with "
     "the chapter 4 words: «selalu», «biasanya», «kadang-kadang», «jarang», «setiap hari Sabtu». «berlatih» is practising a skill "
     "or a sport, and it can take a verb: «berlatih bercakap bahasa Melayu».",
     "«suka» は動詞の直前に置き、間に何も入れません：«Saya suka berenang.»（泳ぐのが好きです）。«bermain» のあとに競技名を置きます："
     "«bermain badminton»・«bermain golf»。日常会話では «main badminton» もよく使います。«Tidak juga» は「そうでもない」にあたる自然なやわらかい言い方で、«lebih suka» は「〜のほうが好き」です。頻度は第4章の言葉で言います："
     "«selalu»・«biasanya»・«kadang-kadang»・«jarang»・«setiap hari Sabtu»。«berlatih» は技術やスポーツを練習することで、動詞を続けることも"
     "できます：«berlatih bercakap bahasa Melayu»。",
     'Japanese needs 〜するのが好き or 〜することが好き; Malay needs no の or こと: «suka» + verb. Japanese 遊ぶ is for children and '
     'fun, but «bermain» is also the normal verb for sports and games (ゴルフをする = «bermain golf»).',
     '日本語は「〜するのが好き」「〜することが好き」と言いますが、マレー語は「の」や「こと」にあたる語がいらず、«suka» ＋動詞です。'
     '日本語の「遊ぶ」は子どもや楽しみに使いますが、«bermain» はスポーツやゲームを「する」ときのふつうの動詞でもあります。'),
    ('ms-c10-f04', '«Saya bercakap / berbual dengan» ___.', [
        'A: «Encik bercakap bahasa Melayu di pejabat?» B: «Ya. Saya bercakap bahasa Melayu dengan Puan Aini.»',
        'A: «Encik berbual dengan siapa pada waktu rehat?» B: «Saya berbual dengan rakan sekerja.»',
        'A: «Pukul berapa encik berjumpa dengan pengurus?» B: «Saya berjumpa dengan pengurus pukul sepuluh.»',
        'A: «Encik bercakap bahasa apa dengan isteri?» B: «Saya bercakap bahasa Jepun dengan isteri saya.»',
        'A: «Boleh kita berjumpa esok?» B: «Boleh. Kita berjumpa di kedai mamak pukul lapan.»',
        'A: «Encik selalu berbual dengan Puan Aini?» B: «Ya. Kami berbual setiap pagi.»'],
     "«bercakap» is to speak: the language follows straight after it («bercakap bahasa Melayu»), and the person comes after "
     "«dengan» («bercakap dengan Puan Aini»). «berbual» is a relaxed chat. «berjumpa dengan» is to meet someone. In everyday "
     "talk you will hear the roots: «cakap», «jumpa» («Jumpa lagi!» is the fixed goodbye from chapter 1). Use «kita» when the "
     "listener is included («Kita berjumpa esok.») and «kami» when not («Kami berbual setiap pagi.»).",
     "«bercakap» は話すことで、言語はすぐあとに置き（«bercakap bahasa Melayu»）、話す相手は «dengan» のあとに置きます（«bercakap dengan Puan Aini»）。"
     "«berbual» は気軽なおしゃべりです。«berjumpa dengan» は人に会うことです。日常会話では語根の «cakap»・«jumpa» も聞きます"
     "（«Jumpa lagi!» は第1章の決まった別れの言葉）。聞き手を含むときは «kita»（«Kita berjumpa esok.»）、含まないときは «kami»"
     "（«Kami berbual setiap pagi.»）です。",
     'Japanese 〜と話す matches «bercakap dengan». But 〜に会う uses に, and learners often say *«berjumpa di pengurus»: the person '
     'always takes «dengan», never «di» (which is only for places). 〜語を話す: no word for を, the language follows the verb.',
     '日本語の「〜と話す」は «bercakap dengan» にあたります。ところが「〜に会う」は「に」を使うので、*«berjumpa di pengurus» と言いがちです。'
     '人には必ず «dengan» を使い、«di» は場所だけです。「〜語を話す」の「を」にあたる語はなく、言語は動詞のすぐあとに来ます。'),
]

DIALOGUE = [
    ('Aini', 'Selamat pagi, Encik Tanaka! Biasanya pukul berapa encik bertolak ke pejabat?'),
    ('Tanaka', 'Saya bertolak pukul tujuh. Saya naik bas. Bas itu berhenti di depan pejabat.'),
    ('Aini', 'Encik bersarapan di rumah?'),
    ('Tanaka', 'Tidak. Saya bersarapan di kedai mamak dekat pejabat.'),
    ('Aini', 'Pada hujung minggu pula, encik buat apa?'),
    ('Tanaka', 'Pada hari Sabtu saya berenang. Pada hari Ahad saya berbasikal dengan kawan.'),
    ('Aini', 'Wah, encik selalu bersenam! Saya pula suka berehat di rumah.'),
    ('Tanaka', 'Itu pun bagus! Puan bermain badminton?'),
    ('Aini', 'Kadang-kadang. Saya berlatih dengan anak saya pada hari Sabtu.'),
    ('Tanaka', 'Seronok! Puan, mesyuarat kita bermula pukul berapa?'),
    ('Aini', 'Pukul sembilan. Encik sudah bersedia?'),
    ('Tanaka', 'Sudah. Kita berjumpa di bilik mesyuarat, ya?'),
    ('Aini', 'Ya. Oh, sudah pukul sembilan. Mesyuarat kita bermula sekarang!'),
    ('Tanaka', 'Baik, mari kita pergi.'),
]
VARIANT = [
    ('Rahman', 'Selamat pagi, Mei Ling! Pukul berapa awak bertolak dari rumah?'),
    ('Mei Ling', 'Saya bertolak pukul tujuh setengah. Saya berjalan kaki ke stesen.'),
    ('Rahman', 'Awak bersarapan di mana?'),
    ('Mei Ling', 'Di rumah. Saya bersarapan dengan suami saya.'),
    ('Rahman', 'Pada hujung minggu awak buat apa?'),
    ('Mei Ling', 'Pada hari Sabtu saya berlari. Pada hari Ahad saya berehat sahaja.'),
    ('Rahman', 'Saya pula bermain golf dengan kawan.'),
    ('Mei Ling', 'Mesyuarat kita bermula pukul berapa?'),
    ('Rahman', 'Pukul sepuluh. Awak sudah bersedia?'),
    ('Mei Ling', 'Belum! Saya bersiap sekarang.'),
]
LISTENING = [
    ('Tanaka', 'Puan Aini, bagaimana rutin puan setiap hari?'),
    ('Aini', 'Setiap pagi saya bangun pukul lima setengah. Saya bersenam di rumah sebelum bersarapan.'),
    ('Tanaka', 'Wah, awal! Pukul berapa puan bertolak ke pejabat?'),
    ('Aini', 'Pukul tujuh. Saya hantar anak ke sekolah dulu. Kemudian saya beratur di stesen.'),
    ('Tanaka', 'Puan naik kereta api?'),
    ('Aini', 'Ya. Waktu pagi, ramai orang beratur di stesen. Kereta api selalu sesak.'),
    ('Tanaka', 'Puan sampai di pejabat pukul berapa?'),
    ('Aini', 'Pukul lapan setengah. Saya bersarapan di pejabat, kemudian saya bekerja.'),
    ('Tanaka', 'Puan berehat pukul berapa?'),
    ('Aini', 'Pukul satu. Saya makan tengah hari dan berbual dengan Mei Ling.'),
    ('Tanaka', 'Pukul berapa puan habis kerja?'),
    ('Aini', 'Pukul enam. Tetapi pada hari Rabu saya berlatih badminton selepas kerja.'),
    ('Tanaka', 'Puan bermain badminton di mana?'),
    ('Aini', 'Dekat rumah saya. Saya bermain dengan kawan dari pejabat.'),
    ('Tanaka', 'Pada hujung minggu pula?'),
    ('Aini', 'Pada hari Sabtu saya berjalan kaki dengan keluarga. Pada hari Ahad saya berehat sahaja!'),
]

CULTURE = [
    'In Malaysia you will hear the same verb in two forms. News, forms, notices and polite speech use the ‹ber-› form: '
    '«Saya bekerja di Kuala Lumpur», «Encik sudah bersarapan?» In a relaxed chat many people use the root alone: «Saya kerja '
    'di KL», «Sudah sarapan?», «Saya cakap bahasa Melayu». Both are correct Malaysian Malay. This course teaches the ‹ber-› form '
    'first, as the standard, and you will understand the short form when you hear it.',
    '‹ber-› is the easiest Malay verb prefix: it has no nasal sound changes. Its only spelling variants are ‹be-› before a root '
    'that starts with r («berehat», «berenang») and in «bekerja», and ‹bel-› in «belajar», the one exception. Learners from Japan '
    'often write *berrehat or *berkerja: say the word aloud and you hear only one r.',
    'Two verbs change their meaning with ‹ber-›. «tolak» on a door means push, but «bertolak» means set off: «Pukul berapa kita '
    'bertolak?» «berhenti» means stop, so «Bas berhenti di sini», but «berhenti kerja» means to quit your job. To say that you '
    'finish work for the day, use «habis kerja»: «Saya habis kerja pukul enam.»',
    'Malaysian colleagues often chat about breakfast and the weekend. «Sudah sarapan?» is a friendly greeting, not a real '
    'question about food, as in chapter 4.',
]
CULTURE_JA = [
    'マレーシアでは、同じ動詞を二つの形で耳にします。ニュース、書類、掲示、ていねいな会話では ‹ber-› の形を使います：«Saya bekerja di Kuala Lumpur»、'
    '«Encik sudah bersarapan?» くだけたおしゃべりでは、語根だけを使う人も多いです：«Saya kerja di KL»、«Sudah sarapan?»、«Saya cakap bahasa Melayu»。'
    'どちらも正しいマレーシアのマレー語です。このコースでは標準として ‹ber-› の形を先に教え、短い形は聞いて分かるようにします。',
    '‹ber-› はマレー語の動詞の接頭辞でいちばんやさしいもので、鼻音の変化がありません。つづりの違いは、r で始まる語根の前（«berehat»・«berenang»）と '
    '«bekerja» の ‹be-›、そして例外の «belajar» の ‹bel-› だけです。日本の学習者は *berrehat や *berkerja と書きがちですが、声に出すと r は一つしか聞こえません。',
    '‹ber-› が付くと意味が変わる動詞が二つあります。ドアの «tolak» は「押す」ですが、«bertolak» は「出発する」です：«Pukul berapa kita bertolak?» '
    '«berhenti» は「止まる」なので «Bas berhenti di sini» と言いますが、«berhenti kerja» は「仕事を辞める」です。その日の仕事が終わることは «habis kerja» '
    'と言います：«Saya habis kerja pukul enam.»',
    'マレーシアの同僚は、朝ごはんや週末の話をよくします。第4章と同じく、«Sudah sarapan?» は食べ物について本当にたずねる質問ではなく、親しみのこもったあいさつです。',
]

CFG = dict(
    chapter=10, label='10A', unit_id='ms-c10a',
    menu_title='Chapter 10 · ber- verbs', genre='Daily routines',
    prerequisite_units=['ms-c09'], prereq_grammar=['ms-c02-g08', 'ms-c04-g06', 'ms-c04-g08'],
    unit_goal='Describe a working day and the weekend with ber- verbs: when you set off, when things start, what you do and with whom.',
    core=CORE,
    recognition=[],
    revision=[('Roots of the ber- verbs, and «belajar»', REV_ROOTS), ('Time, frequency and markers', REV_TIME),
              ('The office and free time', REV_WORK)],
    core_groups=[('A working day', DAY), ('Talking and meeting', TALK), ('Exercise and free time', FREE)],
    grammar_ids={'routine': 'ms-c10-g02', 'start': 'ms-c10-g03', 'free': 'ms-c10-g04', 'with': 'ms-c10-g05',
                 'background': 'ms-c10-g06', 'events': 'ms-c10-g07', 'spelling': 'ms-c10-g08'},
    grammar=['routine', 'start', 'free', 'with', 'spelling'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 20 cards ms-c10-001 to ms-c10-020', frame_list='ms-c10-f01 to ms-c10-f04', frame_list_ja='f01〜f04',
    goals={'A': 'I can say when I do things on a working day with a taught ber- verb and «pukul».',
           'B': 'I can ask and answer about routines: «Pukul berapa …?», «… bermula», «… bertolak», «suka» + a ber- verb.',
           'C': "I can follow a colleague's day and a team message, and plan a time that fits two routines.",
           'D': 'I can check the ber- verbs, their roots and their spelling, and correct a routine description.',
           'E': 'I can explain a changed workday in a short role-play.'},
    goals_ja={'A': '習った ber- の動詞と «pukul» で、仕事の日にいつ何をするかを言える。',
              'B': '«Pukul berapa …?»・«… bermula»・«… bertolak»・«suka» ＋ ber- の動詞で、日課についてたずね、答えられる。',
              'C': '同僚の一日とチームへのメッセージが分かり、二人の日課に合う時間を決められる。',
              'D': 'ber- の動詞・語根・つづりを確認し、日課の説明を直せる。',
              'E': '短いロールプレイで、いつもと違う仕事の日について説明できる。'},
    setting='A Monday morning at a fictional Japanese company in Kuala Lumpur: «Encik» Tanaka and his colleague «Puan» Aini talk about '
            'their usual working day and the weekend before a meeting. All names, times and routines are fictional.',
    setting_ja='月曜の朝、クアラルンプールの架空の日本企業。田中さんと同僚のアイニさんが、会議の前にいつもの仕事の日と週末について話します。'
               '名前・時刻・日課はすべて架空です。',
    recall=['Without notes, from chapters 4 and 9: say three things you do every morning with root verbs and the time, and read '
            'the door signs «TOLAK» and «TARIK». / 第4章と第9章の復習：毎朝することを三つ、語根の動詞と時刻で言い、ドアの表示 «TOLAK»・«TARIK» を読みましょう。',
            'Recall prompt: «Pukul berapa awak bangun?» «Sudah sarapan?» «Pukul berapa mesyuarat mula?»'],
    recall_key='e.g. «Saya bangun pukul enam.» «Saya sarapan pukul tujuh.» «Saya pergi kerja pukul tujuh setengah.» «Mesyuarat mula '
               'pukul sembilan.» «TOLAK» = push, «TARIK» = pull. Then show the new standard forms: «bersarapan», «bekerja», «bermula».',
    patterns=P, pattern_ids=['ms-c10-f01', 'ms-c10-f02', 'ms-c10-f03', 'ms-c10-f04'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 10 frames f01 to f04 (f04 returns in unit 10B with neighbours; f05 and f06 are unit 10B).',
    pattern_keys=['Pattern 1: one ber- verb, then the time. If a learner adds an object («Saya bersarapan roti»), accept the meaning and model '
                  '«Saya makan roti untuk sarapan» or «Saya bersarapan di rumah»; ber- verbs here take no object. Accept the everyday roots '
                  '(«kerja», «sarapan») in speech, but write the ‹ber-› form on the board.',
                  'Pattern 2: «bermula» for events, «bertolak» for people setting off. Ask the class what «tolak» means on a door before '
                  'you show «bertolak». Contrast «berhenti» (stop) and «berhenti kerja» (quit a job) with «habis kerja» (finish for the day).',
                  'Pattern 3: «suka» + verb, nothing in between. ‹bersukan› (to do sport) is a practice-pool word (ledger L-1307, not taught in class): say «bersenam» or «bermain» + the sport. '
                  'Practise the frequency words from chapter 4 with each answer.',
                  'Pattern 4: «dengan» for the person, nothing before the language. Listen for *«berjumpa di» + person and *«bercakap dengan bahasa Melayu».'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 8, 10, 12),
    drills={
        'repeat_frame': 'Frame: «Setiap pagi saya» [«bersenam» / «bersarapan» / «bertolak»] «pukul» [«enam» / «tujuh» / «tujuh setengah»]',
        'repeat': ['«Setiap pagi saya bersenam pukul enam.»', '«Setiap pagi saya bersarapan pukul tujuh.»',
                   '«Setiap pagi saya bertolak pukul tujuh setengah.»', '«Mesyuarat bermula pukul sembilan.»',
                   '«Saya berehat pukul satu.»', '«Pada hujung minggu saya suka berenang.»',
                   '«Saya bercakap bahasa Melayu dengan Puan Aini.»', '«Pukul berapa kita bertolak?»'],
        'substitute': ['«Setiap pagi saya bersenam pukul enam.» (cue: «bersarapan», «tujuh»)',
                       '«Mesyuarat bermula pukul sembilan.» (cue: «kelas», «tujuh malam»)',
                       '«Saya berehat pukul satu.» (cue: «Puan Aini»)',
                       '«Pada hujung minggu saya suka berenang.» (cue: «berbasikal»)',
                       '«Saya bermain badminton pada hari Sabtu.» (cue: «golf»)',
                       '«Saya bercakap bahasa Melayu dengan Puan Aini.» (cue: «bahasa Inggeris», «pengurus»)',
                       '«Bas itu berhenti di depan pejabat.» (cue: «stesen»)',
                       '«Saya berjumpa dengan pengurus pukul sepuluh.» (cue: «Rahman», «dua petang»)'],
        'transform': ['Everyday to standard: «Saya kerja di Kuala Lumpur.»', 'Everyday to standard: «Saya sarapan di rumah.»',
                      'Everyday to standard: «Saya cakap bahasa Melayu.»', 'Everyday to standard: «Kita jumpa di stesen.»',
                      'Everyday to standard: «Saya main badminton.»', 'Make it a question with «Adakah»: «Encik bersenam setiap pagi.»',
                      'Make it negative: «Saya berehat pukul satu.»', 'Time cue «esok» (marker «akan»): «Kami bertolak pukul tujuh.»',
                      'Time cue «sekarang» (marker «sedang»): «Encik Tanaka bersiap.»', 'Marker «sudah»: «Mesyuarat bermula.»'],
        'question and answer': ['«Pukul berapa encik bertolak ke pejabat?» (cue: half past seven)',
                                '«Mesyuarat bermula pukul berapa?» (cue: ten)', '«Encik suka berenang?» (cue: no, cycling)',
                                '«Encik bercakap bahasa apa dengan isteri?» (cue: Japanese)',
                                'You hear: «Saya bersarapan di kedai mamak.» Ask the question («di mana»).',
                                'You hear: «Kita bertolak pukul dua.» Ask the question.',
                                'You hear: «Saya berbual dengan Mei Ling.» Ask the question («siapa»).',
                                'You hear: «Pada hujung minggu saya bermain golf.» Ask the question («apa»).'],
        'question-word choice': ['«___ kita bertolak?» → «Pukul dua.»', '«Encik bersarapan ___?» → «Di kedai mamak.»',
                                 '«Encik berbual dengan ___?» → «Dengan Mei Ling.»', '«Pada hujung minggu encik buat ___?» → «Saya berenang.»',
                                 '«Mesyuarat bermula pada hari ___?» → «Hari Isnin.»', '«___ encik tidak bersenam hari ini?» → «Sebab hujan.»',
                                 '«Encik bertolak ___ ?» → «Dari rumah.»', '«___ encik berjalan kaki ke stesen?» → «Sepuluh minit.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. The ber- verb comes straight after the person; the time follows with «pukul».',
                   'Cover the line and say it from the English: every morning I exercise at six; I have breakfast at seven; I set off at '
                   'half past seven; the meeting starts at nine; I take a break at one; at the weekend I like swimming; I speak Malay '
                   'with «Puan» Aini; what time do we set off?'],
        'substitute': ['1 «Setiap pagi saya bersarapan pukul tujuh.» 2 «Kelas bermula pukul tujuh malam.» 3 «Puan Aini berehat pukul satu.» '
                       '4 «Pada hujung minggu saya suka berbasikal.»',
                       '5 «Saya bermain golf pada hari Sabtu.» 6 «Saya bercakap bahasa Inggeris dengan pengurus.» 7 «Bas itu berhenti di depan stesen.» '
                       '8 «Saya berjumpa dengan Rahman pukul dua petang.»'],
        'transform': ['1 «Saya bekerja di Kuala Lumpur.» 2 «Saya bersarapan di rumah.» 3 «Saya bercakap bahasa Melayu.» 4 «Kita berjumpa di stesen.» '
                      '5 «Saya bermain badminton.»',
                      '6 «Adakah encik bersenam setiap pagi?» 7 «Saya tidak berehat pukul satu.» 8 «Esok kami akan bertolak pukul tujuh.» '
                      '9 «Encik Tanaka sedang bersiap sekarang.» 10 «Mesyuarat sudah bermula.»'],
        'question and answer': ['1 «Saya bertolak pukul tujuh setengah.» 2 «Pukul sepuluh.» (or «Mesyuarat bermula pukul sepuluh.») '
                                '3 «Tidak. Saya suka berbasikal.» 4 «Saya bercakap bahasa Jepun dengan isteri saya.»',
                                '5 «Encik bersarapan di mana?» 6 «Pukul berapa kita bertolak?» 7 «Encik berbual dengan siapa?» '
                                '8 «Pada hujung minggu encik buat apa?»'],
        'question-word choice': ['1 «Pukul berapa» 2 «di mana» 3 «siapa» 4 «apa» 5 «apa» (with «hari») '
                                 '6 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 7 «dari mana» 8 «Berapa lama»'],
    },
    short_dialogues=[
        ('Pukul berapa kita bertolak?', 'Pukul dua. Bas berhenti di depan pejabat.', 'before a site visit'),
        ('Encik sudah bersarapan?', 'Belum. Saya bersiap sekarang.', 'early in the morning'),
        ('Pada hujung minggu encik buat apa?', 'Saya suka berenang.', 'on a Monday'),
        ('Mesyuarat sudah bermula?', 'Belum. Mesyuarat bermula pukul sepuluh.', 'in the corridor')],
    short_keys=['1 «Baik. Saya tunggu di depan pejabat.» 2 «Mari kita bersarapan di kedai mamak.» (or «Saya tunggu, ya.»)',
                '3 «Seronok! Saya pula suka berbasikal.» 4 «Baik. Saya bersedia sekarang.» (or «Terima kasih.»)'],
    markers=dict(
        title='Markers with ber- verbs', grammar='routine',
        instructions=['Say each sentence again with the marker or time cue in brackets. The ber- verb never changes; only the marker does. / '
                      'かっこ内のマーカーか時の言葉を付けて言い直します。ber- の動詞は変わらず、前に付く語だけが変わります。'],
        items=['«Mesyuarat bermula.» (marker: «sudah»)', '«Saya bersarapan.» (marker: «belum»)', '«Encik Tanaka bersiap.» (marker: «sedang»)',
               '«Kami bertolak pukul tujuh.» (time cue: «esok», marker: «akan»)', '«Bas berhenti di depan pejabat.» (marker: «baru»)',
               '«Saya berlatih bercakap bahasa Melayu.» (marker: «masih»)', 'Answer «Sudah bersedia?» (marker: «belum»)',
               '«Puan Aini bekerja.» (time cue: «sekarang», marker: «masih»)'],
        bridge=['«sudah bermula» ≈ もう始まった · «belum bersarapan» ≈ まだ朝ごはんを食べていない · «sedang bersiap» ≈ 準備している · '
                '«akan bertolak» ≈ 出発する予定',
                'Japanese changes the verb ending (始まった / 始まっていない); Malay keeps «bermula» and changes only the marker. / '
                '日本語は動詞の語尾が変わりますが、マレー語は «bermula» のままで、前の語だけが変わります。'],
        key=['1 «Mesyuarat sudah bermula.» 2 «Saya belum bersarapan.» 3 «Encik Tanaka sedang bersiap.» 4 «Esok kami akan bertolak pukul tujuh.»',
             '5 «Bas baru berhenti di depan pejabat.» 6 «Saya masih berlatih bercakap bahasa Melayu.» 7 «Belum. Saya belum bersedia.» '
             '8 «Sekarang Puan Aini masih bekerja.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、第10章の ber- の動詞と組み合わせて言います。',
                 'Combine the chapter 4 markers with the ber- verbs: the verb never changes, only the marker does.')),
    question_note='Chapter 10 adds no new question word. The ber- verbs fit every question you know: «Pukul berapa kita bertolak?», '
                  '«Mesyuarat bermula pada hari apa?», «Encik berbual dengan siapa?», «Encik bersarapan di mana?», «Berapa lama encik '
                  'berjalan kaki ke stesen?» / 第10章で新しい疑問語は増えません。ber- の動詞は知っている疑問語すべてと使えます：'
                  '«Pukul berapa kita bertolak?»、«Mesyuarat bermula pada hari apa?»、«Encik berbual dengan siapa?»、«Encik bersarapan di mana?»、'
                  '«Berapa lama encik berjalan kaki ke stesen?»',
    question_tasks=['Ask a colleague how they are. («apa»)', 'Ask who your colleague chats with at break time. («siapa»)',
                    'Ask where your colleague has breakfast. («di mana»)', 'Ask formally whether the meeting has started. («Adakah»)',
                    'Ask politely whether you may set off now. («Bolehkah»)', 'Ask how many people are queuing. («berapa»)',
                    'Ask when the class starts. («bila»)', 'Ask what time we set off. («pukul berapa»)',
                    'Ask on what day your colleague swims. («hari apa»)', 'Ask how your colleague goes to the office. («bagaimana»; spoken «macam mana»)',
                    'Ask why your colleague did not exercise today. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which bus stops in front of the office. («yang mana»)', 'Ask where your colleague cycles to on Sunday. («ke mana»)',
                    'Ask where the bus sets off from. («dari mana»)', 'Ask how far your colleague runs. («berapa jauh»)',
                    'Ask how long your colleague walks to the station. («berapa lama»)', 'Ask how many cups of coffee your colleague drinks. («berapa» with a counter)',
                    'Ask who made the coffee. («siapa» with «oleh»)'],
    question_keys=['1 «Apa khabar?» 2 «Encik berbual dengan siapa pada waktu rehat?» 3 «Encik bersarapan di mana?»',
                   '4 «Adakah mesyuarat sudah bermula?» 5 «Bolehkah saya bertolak sekarang?» 6 «Berapa orang beratur?»',
                   '7 «Bila kelas bermula?» 8 «Pukul berapa kita bertolak?» 9 «Pada hari apa encik berenang?»',
                   '10 «Bagaimana encik pergi ke pejabat?» (spoken: «Macam mana encik pergi ke pejabat?») 11 «Kenapa encik tidak bersenam hari ini?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab hujan.» / «Kerana hujan.»',
                   '12 «Bas yang mana berhenti di depan pejabat?» 13 «Pada hari Ahad encik berbasikal ke mana?» 14 «Bas itu bertolak dari mana?»',
                   '15 «Berapa jauh encik berlari?» 16 «Berapa lama encik berjalan kaki ke stesen?» 17 «Berapa cawan kopi encik minum?»',
                   '18 «Kopi ini dibuat oleh siapa?»'],
    listening=LISTENING,
    listening_context='During the afternoon break «Encik» Tanaka asks «Puan» Aini about her daily routine. / 午後の休憩時間に、田中さんがアイニさんに毎日の日課をたずねます。',
    listening_before=['Predict: which ber- verbs will you hear? Write three guesses (for example «bersenam», «bersarapan», «berehat»). / 聞こえそうな ber- の動詞を三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['What time does Aini get up?', 'What does she do before breakfast?', 'What does she do before she queues at the station?',
                      'How does she travel, and what is the train like in the morning?', 'Where does she have breakfast?', 'When does she take a break, and with whom does she chat?',
                      'What time does she finish work?', 'What does she do on Wednesdays after work?', 'What does she do on Saturday and on Sunday?'],
    listen_answers=['5.30 a.m.', 'she exercises at home', 'she takes her child to school', 'by train; it is always crowded',
                    'at the office', 'at 1 p.m.; with Mei Ling', '6 p.m.', 'she practises badminton', 'Saturday: she walks with her family; Sunday: she just rests'],
    listening_after=['Compare answers, then shadow lines 2, 6 and 12 after the teacher. / 答えを比べ、2・6・12行目をシャドーイングします。',
                     'Tell your partner your own routine in four sentences with ber- verbs and «pukul». / 自分の日課を ber- の動詞と «pukul» を使って4文でパートナーに話しましょう。'],
    test_listen=[(1, 'she exercises at home', ['bersenam', 'sebelum', 'bersarapan']),
                 (3, 'she queues at the station', ['beratur', 'stesen']),
                 (7, 'at the office', ['bersarapan', 'bekerja']),
                 (9, 'with Mei Ling', ['berbual', 'dengan']),
                 (11, 'she practises badminton', ['berlatih', 'badminton']),
                 (15, 'she just rests', ['berjalan', 'berehat'])],
    test_listen_prompts=['What does Aini do before breakfast?', 'What does she do at the station?', 'Where does she have breakfast?',
                         'With whom does she chat at lunch?', 'What does she do on Wednesdays after work?', 'What does she do on Sunday?'],
    reading_title='Reading and writing · A message to the team',
    reading=['Fictional message in the team chat (all names, places and times are invented):',
             '«Selamat pagi semua. Esok mesyuarat bermula pukul sembilan, bukan pukul sepuluh. Sila bersedia.»',
             '«Selepas mesyuarat, kita berjumpa dengan pengurus dari Osaka.»',
             '«Pukul dua kita bertolak ke Shah Alam. Bas berhenti di depan pejabat pukul satu setengah.»',
             '«Kita balik ke pejabat pukul lima. Terima kasih. Aini»',
             'Sign at the bus stop: «Bas berhenti di sini.»'],
    read_questions=['What time does the meeting start tomorrow?', 'What does Aini ask everyone to do?', 'Whom do they meet after the meeting?',
                    'What time do they set off, and where to?', 'Where and when does the bus stop?', 'What time do they come back?',
                    'Say in Malay: "The class starts at seven."'],
    read_answers=['at nine (not ten)', 'to be ready («Sila bersedia»)', 'the manager from Osaka', 'at two, to Shah Alam',
                  'in front of the office at half past one', 'at five', '«Kelas bermula pukul tujuh.»'],
    write_instruction='Write your own working day in four or five sentences, each with a ber- verb and a time. / '
                      'ber- の動詞と時刻を使って、自分の仕事の日を4〜5文で書きましょう。',
    write_model='«Setiap pagi saya bersenam pukul enam. Saya bersarapan di rumah pukul tujuh. Saya bertolak ke pejabat pukul tujuh '
                'setengah. Mesyuarat bermula pukul sembilan. Saya berehat pukul satu. Itu rutin saya setiap hari.»',
    writing_type='message',
    task_title='Task · Find a time to play badminton',
    role_a=['Your week (fictional): Monday you run after work; Wednesday you practise badminton at 7 p.m.; Thursday you meet a friend '
            'after work; Saturday morning you are free.',
            'Ask B about B\'s week and find an evening to play badminton together. Say when you finish work and when you can set off.',
            'Aの一週間（架空）：月曜は仕事のあと走る、水曜は午後7時にバドミントンの練習、木曜は仕事のあと友達に会う、土曜の朝は空いている。'
            'Bの一週間をたずね、一緒にバドミントンをする夕方を決めます。仕事が終わる時刻と出発できる時刻を言います。'],
    role_b=['Your week (fictional): Tuesday you swim after work; Wednesday your meeting starts at 5 p.m.; Thursday you are free after 6 p.m.; '
            'Saturday you cycle with your family in the morning.',
            'Answer A with ber- verbs and times, and agree on a day, a time and where you meet.',
            'Bの一週間（架空）：火曜は仕事のあと泳ぐ、水曜は午後5時から会議、木曜は午後6時以降空いている、土曜の朝は家族と自転車に乗る。'
            'ber- の動詞と時刻でAに答え、日・時刻・待ち合わせ場所を決めます。'],
    change=['Halfway, B says: «Maaf, hari Khamis saya bekerja sampai pukul lapan.» A and B choose another day and ask «Pukul berapa kita bertolak?»',
            '途中でBが «Maaf, hari Khamis saya bekerja sampai pukul lapan.» と言います。AとBは別の日を選び、«Pukul berapa kita bertolak?» とたずねます。'],
    success=['☐ Both partners say at least three things about their week with ber- verbs and «pukul».',
             '☐ A asks with «Pukul berapa …?» or «Pada hari apa …?», and B answers with a full sentence.',
             '☐ After the change, they agree a new day, a time to set off and a place to meet.'],
    task_key='«Encik bekerja sampai pukul berapa hari Rabu?» — «Mesyuarat saya bermula pukul lima.» — «Hari Khamis pula?» — «Hari Khamis '
             'saya habis kerja pukul enam.» — «Bagus. Kita bermain badminton hari Khamis.» — Change: «Maaf, hari Khamis saya bekerja sampai pukul lapan.» — '
             '«Hari Sabtu pula? Pagi saya berbasikal, tetapi petang saya ada masa.» — «Baik. Pukul berapa kita bertolak?» — «Pukul tiga. Kita berjumpa di stesen.»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Charter section 5 (ber- before meN-; ber- has no nasal sound changes, only be- and bel-: Sam, 13 Nov 2026) and plan '
                    'section 3 (secondary grammar sources, [INFERRED] until the end-of-project Kamus Dewan check); Kata-Kata chapter 10 '
                    'card notes ms-c10-001 («bekerja»: spelt be-, standard for «Saya kerja di …»), -005 and -007 (be- before r), -013 '
                    '(«bersarapan»: everyday speech often just says «sarapan»), -015 («berhenti kerja» = to quit a job), -020 («bertolak»: '
                    '«tolak» (push) changes meaning with ber-); ledger L-0473 Sam\'s notes («bercakap» is the standard written form of «cakap»); '
                    'chapter 4 unit 4B culture note («Sudah makan?» as a greeting). The note states no figure or rule about Malaysia.',
    culture_prompt='Does Japanese have a formal and a casual form of the same verb (働く / 勤務する, 朝食をとる / 朝ごはんを食べる)? When do you use each?',
    culture_explain=('マレーシアで同じ動詞を標準の ‹ber-› の形と日常の短い形で聞くこと、‹ber-› のつづり、意味が変わる動詞について読みます。',
                     'Read about hearing the standard ‹ber-› form and the everyday root, the spelling of ‹ber-›, and two verbs whose meaning changes.'),
    quiz_words=['L-1106', 'L-1102', 'L-1093', 'L-1100', 'L-1099', 'L-1095'],
    quiz_meanings=['to set off, to depart', 'to begin (a meeting)', 'to rest, to take a break', 'to queue', 'to chat', 'to swim'],
    grammar_quiz=[('Write the standard form: «Saya kerja di sebuah syarikat Jepun.»', '«Saya bekerja di sebuah syarikat Jepun.»', ['bekerja', 'syarikat']),
                  ('Say in Malay: "What time does the meeting start?"', '«Pukul berapa mesyuarat bermula?» (or «Mesyuarat bermula pukul berapa?»)', ['pukul', 'berapa', 'mesyuarat', 'bermula']),
                  ('Correct the sentence: «Saya berjumpa di pengurus.»', '«Saya berjumpa dengan pengurus.»', ['berjumpa', 'dengan']),
                  ('Add «sudah» and say it: «Encik Tanaka bersedia.»', '«Encik Tanaka sudah bersedia.»', ['sudah', 'bersedia'])],
    test_reading=['Fictional notice: «PERHATIAN: Mesyuarat hari Isnin bermula pukul sepuluh. Kita bertolak ke Shah Alam pukul dua. '
                  'Bas berhenti di depan pejabat. Sila bersedia pukul satu setengah.»'],
    reading_quiz=[('What time does Monday\'s meeting start?', 'at ten', ['bermula', 'mesyuarat']),
                  ('What time do they set off?', 'at two', ['bertolak']),
                  ('Where does the bus stop?', 'in front of the office', ['berhenti', 'depan', 'pejabat']),
                  ('When should everyone be ready?', 'at half past one', ['bersedia', 'setengah'])],
    speaking_test='Tell the teacher about your working day in four sentences with ber- verbs and times, then answer one question about your weekend.',
    speaking_key='Check: at least three different ber- verbs spelt and said correctly («bekerja», «berehat»); a time with «pukul»; «suka» + a ber- verb '
                 'for the weekend. Accept the everyday root in speech if the ber- form was also used once.',
    speaking_words=['bekerja', 'bersarapan', 'bertolak', 'bermula', 'suka'],
    plan={'A_recall': 'chapters 4 and 9 (a morning routine with root verbs; the door signs) from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first, question and answer before the rule; then the vocabulary in three groups with each root '
                        '(a working day 10, talking and meeting 4, exercise and free time 6). Write ‹ber-›, ‹be-› and ‹bel-› on the board.',
          'B_recall': 'say the time you do three things with «Setiap pagi saya … pukul …».',
          'B_drills': 'pattern table, substitution, transformation (everyday to standard first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner says when they set off today and one weekend activity.',
          'D_review': 'cumulative question-word drill (chapters 1 to 10), then the markers drill with new cues and a spelling check of '
                      '«berehat», «berenang», «bekerja», «belajar».',
          'D_preview': 'unit 10B: background and neighbours (Kata-Kata c10 cards ms-c10-021 to ms-c10-041 and frames f05, f06).',
          'E_recall': 'say three things from your Monday and one thing from your weekend.',
          'E_listening': 'read the Kata-Kata scenario lines ms-c10-s01 to ms-c10-s09 (Tanaka and «Puan» Aini, the working day) twice; '
                         'learners tick the ber- verbs they hear.',
          'E_roleplay': 'pairs play the same scene with their own routine, without the script.',
          'E_variation': 'a changed workday: today A works from home («Hari ini saya bekerja dari rumah»), the meeting starts at two and the bus '
                         'does not stop at the office; A explains the new day, B asks «Pukul berapa …?»'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 10 to the daily-life scene grab_ride_chat and the home-condo scene '
                     'new_neighbour, both for unit 10B. Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: unit 10B (background and neighbours), then the writing block after 10B.',
    teacher_notes=['Load: 20 core words in three groups (a working day 10; talking and meeting 4; exercise and free time 6), no recognition '
                   'word (no Dunia scene primes chapter 10), and revision of the roots, the time words and the office words. Suggested order: '
                   'Block A the working-day group with patterns 1 and 2; Block B talking and meeting with pattern 4; exercise and free time '
                   'with pattern 3 in Block B or C. If the pilot shows 20 is too many, the natural cut is A/B: «bekerja», «bersarapan», '
                   '«bertolak», «bermula», «berehat», «berhenti», «bercakap», «berjumpa», «bermain», «bersenam» first; the rest second.',
                   'ber- rule (charter section 5, Sam 13 Nov 2026): no nasal sound changes; ‹be-› before r («berehat», «berenang») and in '
                   '«bekerja»; ‹bel-› only in «belajar» (revision, chapter 2). Every ber- word here is its own ledger row; do not let learners '
                   'build new ones (‹bersukan› is a practice-pool word, not taught here; *bermesyuarat is not taught). No meN- verb (chapter 11).',
                   'Common traps from the Kata-Kata cards: «berhenti kerja» means to quit a job (card ms-c10-015); for finishing work for '
                   'the day say «habis kerja». «bertolak» means to set off, not to push (card ms-c10-020): «tolak» alone is the door sign PUSH '
                   'from chapter 9. «bersarapan» is standard; «sarapan» alone is everyday (card ms-c10-013).',
                   'Where Japanese learners usually slip: (1) treating ‹ber-› like ます and adding it to any verb (*bermakan does not exist); '
                   '(2) *«berjumpa di» + a person, from 〜に会う: the person takes «dengan»; (3) *«bercakap dengan bahasa Melayu», from '
                   '〜語で話す: the language follows the verb directly; (4) spelling *berrehat, *berkerja; (5) 休む covers both '
                   '«berehat» (rest) and taking a day off («bercuti», unit 10B): ask which they mean; (6) やめる covers stop and quit.',
                   'Standard first: teach the ‹ber-› form, accept the everyday root in speech («kerja», «sarapan», «cakap», «jumpa», «main»), '
                   'and never mark it wrong in a speaking task. No spoken contraction is needed in this unit.',
                   'The scene follows Kata-Kata c10 (scenario lines ms-c10-s01 to s09, frames f01 to f04). All names, times and routines are '
                   'fictional; learners may use their real week or an invented one.',
                   'Cumulative question words: chapters 1 to 10. Chapter 10 adds no new question word.'],
)

UNIT = unit_dict(CFG)
