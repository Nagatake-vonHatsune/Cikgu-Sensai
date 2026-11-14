"""Unit 18: the Stage 2 close. Chapter 18 is review and assessment, with no new word (plan section 2, "Chapter 18: no new core
list"), in five 45-minute blocks (plan section 1):

  18A  integrated review across the five pack themes and every chapter 10 to 17 pattern (this file, component «review»);
  18B  rehearsal and targeted repair: a new colleague's day, the parcel problem and the changed invitation («rehearsal»);
  18C  the A2 written check: listening 12, reading 15, writing 18 minutes (suite/stage2.py, versions A and B);
  18D  speaking: about 7 minutes per learner, one examiner, six learners (suite/stage2.py);
  18E  feedback, the can-do review, a demonstration of Hanashishou band 1 scenes (named only; chapter tags come in build
       step 6) and a personal practice plan («feedback»).

Kata-Kata c18 ("Stage 2 review") is the review spine: its six frames and all 22 scenario lines (ms-c18-s01 to s22,
"A working week") are used word for word in the 18A model. The spaced returns (plan section 6): every Kata-Kata frame of
chapters 10 to 17 comes back in the 18A pattern round (FRAME_RETURNS); the late chapters 16 and 17 come back a second time in
their own 18B tasks (LATE_RETURNS), and their further return is carried forward to Stage 3 (the Stage 2 record).

Rules: only ledger words placed in chapters 1 to 17 (the build checks the unit at chapter 18, and tests/test_stage2_ch18.py
re-checks every line at chapter 17); the practice-pool row «disimpan» (L-1306) appears once, in the 18A reading, as a word to
recognise, never in a key; standard forms first and every spoken form labelled; «lah» and «kan» never required; dari /
daripada, the -kan rule, the bare-root rule, noun objects for «tangguhkan» / «batalkan», «kita» against «kami», «Lain kali,
ya?» only where no new day is offered, «sudi» for invitations and «boleh» for everyday requests; no faith-specific
expression; the clinic lines keep the chapter 13 safety limits (no diagnosis, no medicine, no treatment advice). All names,
places and times are fictional. Japanese is a draft awaiting native review.
"""
import json
from pathlib import Path

from .stage2 import CANDO, CHARTER_GOALS, TESTED, FOCUS

ROOT = Path(__file__).resolve().parents[1]
UNIT_ID = 'ms-c18'
C18 = json.loads((ROOT / 'curriculum/reference/katakata/c18.json').read_text())
SCENARIO = [(l['id'], l['speaker'].replace('Cik ', '').replace('Puan ', ''), l['ms']) for l in C18['scenario']['lines']]
C18_FRAMES = {f['id']: f['example'] for f in C18['frames']}
# Spoken forms in the Kata-Kata lines get a label beside the line (standard form first, chapter 17).
SPOKEN_NOTE = {'ms-c18-s09': ' (spoken «tengok» = standard «melihat»)', 'ms-c18-s10': ' (spoken «tengok» = standard «melihat»)',
               'ms-c18-s21': ' (spoken «set» = standard «setuju»)', 'ms-c18-s22': ' (spoken «kat» = standard «di»)'}
SCENES = [
    ('Monday · the office (chapters 10 and 11) / 月曜日・事務所（第10・11章）', 'ms-c18-s01', 'ms-c18-s05'),
    ('Tuesday · the meeting room ceiling (chapter 12) / 火曜日・会議室の天井（第12章）', 'ms-c18-s06', 'ms-c18-s08'),
    ('Tuesday · a parcel at the guardhouse (chapter 12) / 火曜日・守衛所の荷物（第12章）', 'ms-c18-s09', 'ms-c18-s10'),
    ('Wednesday · not well (chapter 13) / 水曜日・体調が悪い（第13章）', 'ms-c18-s11', 'ms-c18-s14'),
    ('Thursday · a phone and a wallet (chapters 15 and 16) / 木曜日・電話と財布（第15・16章）', 'ms-c18-s15', 'ms-c18-s16'),
    ('Friday · the dinner invitation (chapters 14 and 17) / 金曜日・夕食の招待（第14・17章）', 'ms-c18-s17', 'ms-c18-s22'),
]

THEMES = [
    'Daily life: your day, your background, a lost thing (chapters 10 and 15). / 日常生活：一日、自分の背景、なくし物（第10・15章）。',
    'Office: who did what, a draft and its deadline, plans with reasons (chapters 11 and 14). / 職場：誰が何をしたか、下書きと締め切り、理由のある予定（第11・14章）。',
    'Home and condo: a parcel, a leak, a locked door, a spill (chapters 12 and 16). / 住まい：荷物、水漏れ、閉まったドア、こぼれた飲み物（第12・16章）。',
    'Health: not yet, may I, need and should, clinic rules (chapter 13). / 健康：まだ、〜してもいいか、必要・助言、クリニックの規則（第13章）。',
    'Social: invitations, a soft no, another day, standard and spoken Malay (chapters 14 and 17). / 交流：誘い、やわらかい断り、別の日、標準形と話し言葉（第14・17章）。',
]

RECALL = [
    'Ch 10: say what time you set off for work and one thing you do at the weekend. / 仕事に出発する時刻と、週末にすることを一つ言いましょう。',
    'Ch 11: say who in this class wrote something today, with a meN- verb. / 今日このクラスで何かを書いた人を meN- の動詞で言いましょう。',
    'Ch 12: ask your partner to keep something for you, with ‹-kan›. / ‹-kan› を使って、何かを預かってくれるよう相手に頼みましょう。',
    'Ch 13: ask permission to sit here; say one thing you have not done yet today. / ここに座る許可を求め、今日まだしていないことを一つ言いましょう。',
    'Ch 14: give a reason with «kerana» and a condition with «kalau». / «kerana» で理由を、«kalau» で条件を言いましょう。',
    'Ch 15: describe your bag with «yang» and a colour. / «yang» と色を使って自分のかばんを説明しましょう。',
    'Ch 16: say you left something somewhere by accident. / うっかりどこかに何かを置き忘れたと言いましょう。',
    'Ch 17: invite your partner politely, then decline your partner\'s invitation kindly. / ていねいに相手を誘い、次に相手の誘いをやさしく断りましょう。',
]
RECALL_KEY = ('e.g. 10 «Setiap pagi saya bertolak pukul tujuh. Pada hujung minggu saya suka berenang.» 11 «Cik Farah menulis emel.» '
              '12 «Tolong simpankan beg saya.» 13 «Bolehkah saya duduk di sini?» «Saya belum makan.» '
              '14 «Saya datang awal kerana saya ada mesyuarat. Kalau hujan, kita makan di kafe.» '
              '15 «Beg saya beg yang berwarna hitam dan ada zip.» 16 «Saya tertinggal telefon di pejabat.» '
              '17 «Sudikah encik datang makan malam?» «Terima kasih. Sayangnya saya tidak lapang. Lain kali, ya?»')

# Spaced return (plan section 6): every Kata-Kata frame of chapters 10 to 17, and the 18A line that brings it back.
FRAME_RETURNS = {
    'ms-c10-f01': 'Setiap pagi saya bersarapan pukul tujuh setengah.', 'ms-c10-f02': 'Pukul berapa mesyuarat bermula?',
    'ms-c10-f03': 'Pada hujung minggu saya suka berbasikal di taman.', 'ms-c10-f04': 'Saya bercakap bahasa Melayu dengan pengawal.',
    'ms-c10-f05': 'Saya berasal dari Nagoya. Saya bekerja di Petaling Jaya.', 'ms-c10-f06': 'Saya sudah berkenalan dengan Cik Mei Ling.',
    'ms-c11-f01': 'Encik Rahman menulis draf itu.', 'ms-c11-f02': 'Draf itu ditulis oleh Encik Rahman.',
    'ms-c11-f03': 'Siapa yang menyemak slaid itu?', 'ms-c11-f04': 'Tolong semak emel ini.',
    'ms-c11-f05': 'Awak sedang membaca apa?', 'ms-c11-f06': 'Hujung minggu ini saya mahu mendaki bukit.',
    'ms-c12-f01': 'Tolong simpankan kotak ini di pejabat.', 'ms-c12-f02': 'Boleh tunjukkan nombor penjejakan itu?',
    'ms-c12-f03': 'Saya mahu ambil kotak saya. Sudah sampai?', 'ms-c12-f04': 'Juruteknik sedang membaiki lampu dapur.',
    'ms-c12-f05': 'Boleh hubungi pejabat pengurusan?', 'ms-c12-f06': 'Ada kebocoran di bilik air saya.',
    'ms-c13-f01': 'Saya belum mendaftar.', 'ms-c13-f02': 'Bolehkah saya duduk di sini?',
    'ms-c13-f03': 'Saya perlu minta cuti sakit.', 'ms-c13-f04': 'Encik patut tanya doktor dulu.',
    'ms-c13-f05': 'Tidak dibenarkan makan di bilik menunggu.', 'ms-c13-f06': 'Borang ini wajib diisi.',
    'ms-c14-f01': 'Kalau lif rosak, kita guna tangga.', 'ms-c14-f02': 'Saya tidak datang kerana saya demam.',
    'ms-c14-f03': 'Saya bertolak awal supaya saya tidak lewat.', 'ms-c14-f04': 'Walaupun saya penat, saya mahu ikut.',
    'ms-c14-f05': 'Dia makan sambil membaca emel.',
    'ms-c14-f06': 'Mula-mula kita mendaftar, kemudian kita menunggu, akhirnya kita berjumpa doktor.',
    'ms-c15-f01': 'Saya mencari beg yang ada dua poket.', 'ms-c15-f02': 'Telefon saya hilang.',
    'ms-c15-f03': 'Lelaki yang memakai topi itu Encik Rahman.', 'ms-c15-f04': 'Dompet itu berwarna hitam dan ada zip.',
    'ms-c15-f05': 'Yang mana satu? Yang besar atau yang kecil?', 'ms-c15-f06': 'Bentuknya bulat, seperti bola.',
    'ms-c16-f01': 'Saya tertinggal kunci di pejabat.', 'ms-c16-f02': 'Maaf, saya terlupa.',
    'ms-c16-f03': 'Air teh tertumpah di lantai.', 'ms-c16-f04': 'Saya tidak sengaja terlanggar meja.',
    'ms-c16-f05': 'Yang ini terbaik, tetapi dompet saya tertinggal di rumah.',
    'ms-c16-f06': 'Pintu terkunci. Boleh tolong hubungi pengawal?',
    'ms-c17-f01': 'Sudikah puan datang ke rumah saya?', 'ms-c17-f02': 'Sayangnya hari Jumaat saya tidak lapang. Lain kali, ya?',
    'ms-c17-f03': 'Bagaimana kalau hari Isnin?', 'ms-c17-f04': 'Setuju! Hari Isnin, pukul satu.',
    'ms-c17-f05': 'Tidak mengapa. Kita cari hari lain.', 'ms-c17-f06': 'Jom makan kat kedai mamak tu!',
}
FRAME_NOTE = {'ms-c17-f06': ' (spoken: «kat» = «di», «tu» = «itu»; with friends)'}
# The five stations of the pattern round: (heading, chapters).
STATIONS = [
    ('Station 1 · Daily life (chapters 10 and 15) · 日常生活', [10, 15]),
    ('Station 2 · Office (chapters 11 and 14) · 職場', [11, 14]),
    ('Station 3 · Home and condo (chapters 12 and 16) · 住まい', [12, 16]),
    ('Station 4 · Health (chapter 13) · 健康', [13]),
    ('Station 5 · Social (chapter 17) · 交流', [17]),
]

NOTICE = [
    'Fictional notice board for the week in the office lobby (all times and places are invented):',
    '«PENGUMUMAN · Minggu ini»',
    '«Isnin: Cik Mei Ling mula bekerja di pejabat ini. Selamat datang!»',
    '«Selasa: Ada kebocoran di siling bilik mesyuarat. Juruteknik akan membaiki siling itu pada hari Rabu. Sila guna bilik kecil.»',
    '«Semua bungkusan disimpan di pondok pengawal.» («disimpan» is a Kata-Kata practice word: recognise it from «simpan»; it is not tested.)',
    '«Khamis: Kaunter barang hilang di stesen dibuka hingga pukul sembilan malam.»',
    '«Jumaat: Makan malam pejabat ditangguhkan ke hari Ahad, pukul tujuh, kerana bos tidak lapang. Sila balas sebelum hari Khamis.»',
]
NOTICE_Q = [
    ('Who starts work this week, and on which day? / 今週、誰がいつ働き始めますか。', '«Cik» Mei Ling, on Monday'),
    ('What is wrong in the meeting room, and when will it be repaired? Which room do you use? / 会議室の何が問題ですか。いつ直りますか。どの部屋を使いますか。',
     'a leak in the ceiling; on Wednesday; the small room'),
    ('Where are the parcels kept? / 荷物はどこに保管されていますか。', 'at the guardhouse («pondok pengawal»)'),
    ('Until what time is the lost-property counter open on Thursday? / 木曜日、遺失物の窓口は何時まで開いていますか。', 'until nine at night'),
    ('What happened to the office dinner, and why? / 夕食会はどうなりましたか。なぜですか。', 'it is put off to Sunday at seven, because the boss is not free'),
    ('By when must you reply? / いつまでに返事をしますか。', 'before Thursday'),
]


def _line(sid, speaker, ms):
    return f'{speaker}: «{ms}»' + SPOKEN_NOTE.get(sid, '')


def model_lines():
    ids = [sid for sid, _, _ in SCENARIO]
    out = []
    for heading, first, last in SCENES:
        out.append('■ ' + heading)
        out.extend(_line(*SCENARIO[i]) for i in range(ids.index(first), ids.index(last) + 1))
    return out


def review_component():
    stations = []
    for heading, chapters in STATIONS:
        stations.append('■ ' + heading)
        for n in chapters:
            stations.extend(f'{fid[-3:]} ({n}) · «{FRAME_RETURNS[fid]}»' + FRAME_NOTE.get(fid, '') for fid in FRAME_RETURNS if fid.startswith(f'ms-c{n}-'))
    returns = []
    for n in TESTED:
        returns.append(f'Ch {n}: ' + ' · '.join(f'{k[-3:]} «{v}»' + FRAME_NOTE.get(k, '') for k, v in FRAME_RETURNS.items() if k.startswith(f'ms-c{n}-')))
    sections = [
        ('Goal and the five themes · 目標と五つのテーマ', [
            'Can-do goal: I can use the language of chapters 10 to 17 together, without notes, in a working week that touches '
            'daily life, the office, the home, health and social life. / 第10〜17章の表現をノートなしで組み合わせ、日常生活・'
            '職場・住まい・健康・交流にわたる一週間の仕事を乗り切れる。',
            'Scene (Kata-Kata c18, fictional): «Cik» Mei Ling starts work in «Encik» Tanaka\'s office in Kuala Lumpur. In one week '
            'she meets her colleagues, finds a leak, collects a parcel, feels unwell, loses her wallet and gets a dinner invitation. '
            '/ 場面（Kata-Kata c18、架空）：メイリンさんがクアラルンプールの田中さんの事務所で働き始めます。一週間で同僚に会い、'
            '水漏れを見つけ、荷物を受け取り、体調をくずし、財布をなくし、夕食に招かれます。',
            *THEMES]),
        ('Recall without notes (5 min) · ノートなしで復習（5分）', RECALL),
        ('Model · A working week, read in pairs (10 min) · モデル会話「ある一週間」（ペアで読む、10分）', [
            *model_lines(),
            '■ The six review frames of Kata-Kata c18 · Kata-Kata c18 の六つの復習文型',
            *[f'{fid[-3:]} · «{ex}»' for fid, ex in C18_FRAMES.items()]]),
        ('Pattern round · Every chapter 10 to 17 pattern (15 min) · 文型ラウンド（15分）', [
            'In pairs, go round the five stations. A says the line; B changes one detail (a time, a person, a place, a thing) and '
            'says it back; then swap. / ペアで五つのステーションを回ります。Aが文を言い、Bが一つ（時刻・人・場所・物）を変えて'
            '言い返します。次に交代します。', *stations]),
        ('Read (10 min) · 読む（10分）', [*NOTICE, *[f'{i}. {q}' for i, (q, _) in enumerate(NOTICE_Q, 1)],
                                         '________________________________________']),
        ('Self-check · What to repair in 18B (5 min) · 自己チェック（5分）', [
            'Tick each station: ☐ easy ☐ again. Circle one pattern you want to repair in 18B. / 各ステーションに「簡単」か「もう一度」の'
            'チェックを付け、18Bで直したい文型を一つ丸で囲みましょう。',
            *[f'☐ {h}' for h, _ in STATIONS]]),
    ]
    key = [
        'Timing: recall 5, model 10, pattern round 15, read 10, self-check 5 (45 minutes). Block 18A comes before the rehearsal '
        '(18B) and the A2 stage test (18C, 18D); it is not marked.',
        'Recall answers: ' + RECALL_KEY,
        'Reading: ' + ' / '.join(f'{i}. {a}' for i, (_, a) in enumerate(NOTICE_Q, 1)),
        'The model is the Kata-Kata c18 scenario, lines ms-c18-s01 to s22, word for word. Spoken forms in it are labelled: '
        '«tengok» (s09, s10), «set» (s21), «kat» (s22); learners may answer with the standard forms («melihat», «setuju», «di»). '
        '«Pergi dulu.» (s10) is the everyday way to send someone ahead.',
        'Spaced return (plan section 6): every Kata-Kata frame of chapters 10 to 17 comes back in the pattern round. Where each one is:',
        *returns,
        'Chapters 16 and 17 come back a second time in 18B (the parcel problem and the changed invitation), and once more in '
        'Stage 3 (carried forward in the Stage 2 record).',
        'Health lines are about language only: «Encik patut tanya doktor dulu.» is the advice; Cikgu Sensai gives no medical '
        'advice, diagnosis or medicine. «disimpan» in the reading is a Kata-Kata practice word: explain it from «simpan» (chapter '
        '12) and the chapter 9 «di-»; it is never tested.',
        'What to listen for: the ber- and meN- verbs (no ‹ber-› on «makan»; «menulis», not «tulis», in a statement about '
        'someone); ‹-kan› only in requests and offers; «dari» for places and times, «daripada» for people; noun + «yang» + '
        'description; accident ‹ter-› without «sudah». Spoken forms are fine; say the standard form back. Errors go on the board '
        'for 18B, not as red crosses.',
    ]
    return dict(slug='review', type='Task', title='18A · Integrated review · A working week', block='18A', minutes=45,
                sections=sections, key=key,
                explain=('第10〜17章をまとめて復習する45分のブロック（18A）です。Kata-Kata c18 の「ある一週間」を読み、第10〜17章の'
                         'すべての文型を五つのテーマで練習し、掲示を読み、18Bで直したいことを選びます。日本語は未監修です。',
                         'A 45-minute block (18A) reviewing chapters 10 to 17: the Kata-Kata c18 working week, every chapter 10 to 17 '
                         'pattern in five theme stations, a notice board and a self-check that chooses what to repair in 18B.'),
                sub_type='review', tests=[], patterns=list(FRAME_RETURNS) + list(C18_FRAMES), grammar=[FOCUS[n] for n in TESTED] + [FOCUS[18]],
                goal=GOALS['A'], skills=['speaking', 'listening', 'reading'])


# --- 18B ------------------------------------------------------------------------------------------------------------------

# The late chapters 16 and 17 return a second time in 18B (plan section 6): every frame, in the rehearsal that brings it back.
LATE_RETURNS = {
    'ms-c16-f01': 'Saya tertinggal telefon di pejabat.', 'ms-c16-f02': 'Maaf, saya terlupa nombor penjejakan itu.',
    'ms-c16-f03': 'Air dari siling tertumpah di atas kotak itu.', 'ms-c16-f04': 'Saya tidak sengaja terlanggar kotak itu.',
    'ms-c16-f05': 'Kotak saya yang terbesar, tetapi telefon saya tertinggal di pejabat.',
    'ms-c16-f06': 'Pintu bilik itu terkunci. Boleh tolong bukakan?',
    'ms-c17-f01': 'Sudikah cik datang makan malam pada hari Sabtu?',
    'ms-c17-f02': 'Sayangnya hari Sabtu saya tidak lapang. Lain kali, ya?',
    'ms-c17-f03': 'Bagaimana kalau hari Ahad, pukul tujuh?', 'ms-c17-f04': 'Setuju! Hari Ahad, pukul tujuh.',
    'ms-c17-f05': 'Tidak mengapa. Kita cuba lain kali.', 'ms-c17-f06': 'Jom minum kat kafe ni!',
}

REHEARSALS = [
    ('Rehearsal 1 · A new colleague\'s day (10 min) · 新しい同僚の一日（10分）', [10, 11, 13, 14], [
        '■ Role card A: you are new in the office (your own name or «Cik» Farah\'s). Greet B, say where you are from and where '
        'you worked before, ask what time the meeting starts, and ask who wrote the draft you must check. / Aのカード：事務所の'
        '新人です。Bにあいさつし、出身と前の勤め先を言い、会議の開始時刻と、確認する下書きを誰が書いたかをたずねます。',
        '■ Role card B: you are «Encik» Tanaka. Answer A, give the deadline, and say one rule (with «perlu» or «wajib»). / Bの'
        'カード：田中さんです。Aに答え、締め切りを伝え、規則を一つ（«perlu» か «wajib» で）言います。',
        '■ Change of plan: B says «Maaf, mesyuarat ditangguhkan ke pukul tiga, kerana bos lewat.» A says what he or she will do '
        'first, with «Mula-mula saya …, kemudian saya …». / 変更：Bが «Maaf, mesyuarat ditangguhkan ke pukul tiga, kerana bos '
        'lewat.» と言い、Aは «Mula-mula saya …, kemudian saya …» で先にすることを言います。',
        'Model: A «Selamat pagi. Saya Farah. Saya berasal dari Ipoh. Dulu saya bekerja di Penang.» «Pukul berapa mesyuarat '
        'bermula?» «Siapa yang menulis draf ini?» B «Encik Rahman yang menulis draf itu. Tarikh akhir hari Jumaat. Cik perlu '
        'menyemak draf itu dulu.» After the change: A «Mula-mula saya membaca emel, kemudian saya menyemak draf itu.»']),
    ('Rehearsal 2 · The parcel problem (10 min) · 荷物のトラブル（10分）', [12, 15, 16], [
        '■ Role card A: you collect a parcel at the guardhouse. Give your block and unit, describe the box with «yang» and a '
        'colour, and ask the guard to keep a second box. You left your phone at the office, so you cannot show the message. / '
        'Aのカード：守衛所で荷物を受け取ります。ブロックと部屋番号を言い、«yang» と色で箱を説明し、もう一つの箱を預かって'
        'くれるよう頼みます。電話を事務所に置き忘れたので、メッセージを見せられません。',
        '■ Role card B: you are the guard. Ask for the unit and the message; say which box is A\'s. / Bのカード：守衛です。'
        '部屋番号とメッセージをたずね、どの箱がAのものか言います。',
        '■ Change of plan: B says «Maaf, air dari siling tertumpah di atas kotak itu. Kotak itu basah.» A asks B to contact the '
        'management office. / 変更：Bが «Maaf, air dari siling tertumpah di atas kotak itu. Kotak itu basah.» と言い、Aは管理'
        '事務所に連絡してくれるよう頼みます。',
        f'Model: A «Saya mahu ambil kotak saya. Sudah sampai? Saya tinggal di Blok B, unit 12-3.» «Kotak saya berwarna coklat. '
        f'{LATE_RETURNS["ms-c16-f05"]}» B «Boleh tunjukkan mesej?» A «{LATE_RETURNS["ms-c16-f01"]} {LATE_RETURNS["ms-c16-f02"]}» '
        f'B «Tidak mengapa. Nama encik ada pada label.» A «Tolong simpankan kotak kecil itu untuk jiran saya.» After the change: '
        f'B «{LATE_RETURNS["ms-c16-f03"]}» A «Boleh hubungi pejabat pengurusan?» Then A goes to the store room with the guard: '
        f'A «{LATE_RETURNS["ms-c16-f04"]} Maaf.» B «{LATE_RETURNS["ms-c16-f06"]}» (B asks the office to open the store room).']),
    ('Rehearsal 3 · The changed invitation (10 min) · 変わった招待（10分）', [14, 17], [
        '■ Role card A: you are «Puan» Aini. Invite B to the office dinner on Saturday at seven; the boss pays. / Aのカード：'
        'アイニさんです。土曜日7時の職場の夕食会にBを誘います。ボスがおごります。',
        '■ Role card B: you are not free on Saturday. Decline kindly with a reason. If A offers another day, accept it; if A '
        'offers no day, close kindly with «Lain kali, ya?». / Bのカード：土曜日は空いていません。理由を言ってやさしく断ります。'
        'Aが別の日を出したら受け、出さなければ «Lain kali, ya?» でやさしく締めます。',
        '■ Change of plan: A says «Bos menukar hari: hari Ahad, pukul tujuh.» B answers twice: first to A, a senior colleague, '
        'in standard Malay; then to a friend in spoken Malay («Set!», «kat», «ni»). / 変更：Aが「ボスが日を変えた：日曜日7時」'
        'と言います。Bは二回答えます：まず先輩のAに標準形で、次に友人に話し言葉で。',
        f'Model: A «{LATE_RETURNS["ms-c17-f01"]}» B «Terima kasih, puan. {LATE_RETURNS["ms-c17-f02"]}» (no day offered, so '
        f'«Lain kali, ya?») A «{LATE_RETURNS["ms-c17-f05"]}» After the change: A «{LATE_RETURNS["ms-c17-f03"]}» B (standard) '
        f'«{LATE_RETURNS["ms-c17-f04"]}» B to a friend (spoken: «set» = «setuju», «kat» = «di», «ni» = «ini») «Set! Jumpa kat '
        f'pejabat dulu.» «{LATE_RETURNS["ms-c17-f06"]}»']),
]

# Targeted repair (plan section 4, D outcomes): the standing rules of Stage 2. Each item: (question, choice a, choice b, answer, rule).
REPAIR = [
    ('A message from a shop', 'Mesej dari kedai itu sudah sampai.', 'Mesej daripada kedai itu sudah sampai.', 'b',
     '«daripada» for people and organisations; «dari» for places and times («dari Osaka», «dari pukul sembilan»).'),
    ('Asking the guard to keep a parcel', 'Tolong simpankan bungkusan ini.', 'Tolong menyimpan bungkusan ini.', 'a',
     'A request takes the bare ‹-kan› form; a statement about someone takes the meN- verb («Pengawal menyimpan bungkusan itu.»).'),
    ('Reporting what the guard did', 'Pengawal sudah simpankan bungkusan itu.', 'Pengawal sudah menyimpan bungkusan itu.', 'b',
     'After a third-person doer and an aspect word, use the meN- verb the ledger has; never a meN- form with ‹-kan›.'),
    ('Putting a plan off', 'Kita tangguhkan rancangan mendaki ke hari Ahad.', 'Kita tangguhkan mendaki ke hari Ahad.', 'a',
     '«tangguhkan» and «batalkan» take a noun object («rancangan …»), not a verb.'),
    ('Telling a colleague about Mei Ling', 'Cik Mei Ling menangguhkan rancangan itu kerana dia sibuk.',
     'Cik Mei Ling tangguhkan rancangan itu kerana dia sibuk.', 'a',
     'A third-person statement takes «menangguhkan» / «membatalkan» (Sam, 14 Nov 2026).'),
    ('A message to the whole group, you included', 'Esok kami makan di kafe. Jumpa di sana!', 'Esok kita makan di kafe. Jumpa di sana!', 'b',
     '«kita» includes the listener; «kami» leaves the listener out.'),
    ('Declining when you offer no new day', 'Sayangnya saya tidak lapang. Lain kali, ya?',
     'Sayangnya saya tidak lapang. Bagaimana kalau hari Isnin? Lain kali, ya?', 'a',
     '«Lain kali, ya?» is a soft no, like また今度: never after you offer a new day (Sam, 14 Nov 2026).'),
    ('Asking a colleague to drop by the office', 'Sudikah cik singgah di pejabat dulu?', 'Boleh cik singgah di pejabat dulu?', 'b',
     '«sudi» is very polite and belongs to invitations; «boleh» is the everyday request.'),
    ('The most, or by accident', 'Cawan itu terjatuh ke lantai.', 'Cawan itu yang terbesar.', 'both',
     'Both are right: «terjatuh» is ‹ter-› by accident (chapter 16); «yang terbesar» is ‹ter-› the most (chapter 6).'),
    ('Describing a lost bag', 'Saya mencari beg yang berwarna merah.', 'Saya mencari merah yang beg.', 'a',
     'Noun + «yang» + description: the thing comes first, unlike Japanese.'),
]


def rehearsal_component():
    parts = []
    for heading, _, lines in REHEARSALS:
        parts.append((heading, lines))
    repair = ['Choose the better line, a or b, and say the rule in your own words. / より良い文をaかbで選び、規則を自分のことばで言いましょう。']
    repair += [f'{i}. {q}: (a) «{a}» (b) «{b}»' for i, (q, a, b, _, _) in enumerate(REPAIR, 1)]
    returns = ['Ch 16 and 17, second return: ' + ' · '.join(f'{k[-7:]} «{v}»' for k, v in LATE_RETURNS.items())
               + ' (c17-f06 is spoken: «kat» = «di», «ni» = «ini»)']
    sections = [
        ('Goal and recall (5 min) · 目標と復習（5分）', [
            'Can-do goal: I can handle a new colleague\'s day, a parcel problem and a changed invitation without notes, and repair '
            'the patterns I circled in 18A. / 新しい同僚の一日、荷物のトラブル、変わった招待にノートなしで対応し、18Aで丸を付けた'
            '文型を直せる。',
            'Recall: tell your partner the pattern you circled in 18A and say one line with it. / 18Aで丸を付けた文型を相手に伝え、'
            'それを使って一文言いましょう。']),
        *parts,
        ('Targeted repair (10 min) · 弱点の練習（10分）', repair),
    ]
    key = [
        'Timing: goal and recall 5, three rehearsals of 10, targeted repair 10 (45 minutes). Swap roles halfway through each '
        'rehearsal if time allows. Not marked.',
        'Repair answers: ' + ' '.join(f'{i} {ans}: {rule}' for i, (_, _, _, ans, rule) in enumerate(REPAIR, 1)),
        'Late chapters (plan section 6): chapters 16 and 17 return a second time here, every frame:', *returns,
        'Their next return is carried forward to Stage 3 (Stage 2 record, `stage3_carry_forward`).',
        'In the spoken answer of rehearsal 3, «Set!», «kat» and «ni» are optional: the standard answer is always right, and '
        '‹lah› or ‹kan› are never needed.',
        'What to listen for: «Saya mahu ambil …» and a ‹-kan› request (12); «yang» + colour (15); ‹ter-› by accident without '
        '«sudah» (16); «sudi» for the invitation, «Sayangnya …» with a reason, «Lain kali, ya?» only when no day is offered (17); '
        '«kerana», «kalau», «mula-mula … kemudian» (14). Note each learner\'s slips for 18E.',
    ]
    return dict(slug='rehearsal', type='Task', title='18B · Rehearsal and targeted repair', block='18B', minutes=45,
                sections=sections, key=key,
                explain=('練習と弱点の手直しの45分のブロック（18B）です。新しい同僚の一日、荷物のトラブル、変わった招待の三つの場面を'
                         'ロールプレイし、第2段階の規則を選択問題で直します。日本語は未監修です。',
                         'A 45-minute block (18B): three rehearsals (a new colleague\'s day, the parcel problem, the changed invitation) '
                         'and a targeted repair of the Stage 2 rules.'),
                sub_type='rehearsal', tests=[], patterns=list(LATE_RETURNS), grammar=[FOCUS[n] for n in TESTED],
                goal=GOALS['B'], skills=['speaking', 'listening'])


# --- 18E ------------------------------------------------------------------------------------------------------------------

# Hanashishou band 1 scenes to demonstrate, by pack (named only: chapter tags come in build step 6). Files are
# content/packs/<pack>/targets/ms/story/<scene>.ink at Hanashishou 55fd4ed; each has band 1 («#lvl: 1») choices.
HANASHISHOU = [
    ('Daily life', ['grab_ride_chat', 'lost_wallet']),
    ('Home and condo', ['new_neighbour', 'guardhouse_parcel', 'ceiling_leak', 'aircon_repair']),
    ('Office', ['report_deadline', 'team_dinner']),
    ('Health', ['clinic_registration', 'clinic_visit', 'pharmacy_advice']),
    ('Social', ['weekend_plans']),
]
HANASHISHOU_COMMIT = '55fd4ed'


def feedback_component():
    checks = []
    for n in TESTED:
        checks.append(f'■ Chapter {n} · {CHARTER_GOALS[n]}')
        checks.extend(f'☐ I can · ☐ again · {en} / {ja}' for en, ja in CANDO[n])
    scenes = [f'{pack}: ' + ', '.join(names) for pack, names in HANASHISHOU]
    sections = [
        ('Results and feedback (10 min) · 結果とフィードバック（10分）', [
            'Can-do goal: I can see what I can do at A2, choose what to practise, and start a band 1 scene in Hanashishou. / A2 で'
            '何ができるかを確かめ、練習することを選び、Hanashishou のバンド1の場面を始められる。',
            'Your result: Listening __ / 20   Reading __ / 20   Writing __ / 20   Speaking __ / 20   Total __ / 80 / '
            'あなたの結果',
            'Two things I did well: ______________________   One thing to repair: ______________________ / よくできたこと二つ・'
            '直すこと一つ']),
        ('Can-do review · Stage 2 (15 min) · 第2段階の「できること」の確認（15分）', [
            'Tick "I can" or "again" for each line, without notes. Your teacher brings the "again" lines back in class or in your plan. / '
            'ノートなしで各行に「できる」か「もう一度」のチェックを付けましょう。', *checks]),
        ('Hanashishou band 1 · A demonstration (10 min) · Hanashishou バンド1の実演（10分）', [
            'The teacher opens one band 1 scene in Hanashishou and plays it with the class, then shows the others. These scenes '
            'fit the Stage 2 themes; they are named here only, because Hanashishou gives its scenes chapter tags in build step 6. '
            '/ 先生が Hanashishou のバンド1の場面を一つ開いてクラスで進め、ほかの場面も見せます。場面名だけを挙げています（章の'
            'タグは build step 6 で付きます）。',
            *scenes,
            'Hanashishou\'s self-rating after a scene is practice, not proof of spoken accuracy. / 場面のあとの自己評価は練習であり、'
            '話す力の証明ではありません。']),
        ('My practice plan (10 min) · 自分の練習計画（10分）', [
            '1. Three can-do lines I ticked "again": ______________________ / 「もう一度」に付けた三行',
            '2. Kata-Kata: the chapter sets for those lines, and the c18 review set (frames ms-c18-f01 to f06): ______________ / '
            'Kata-Kata：その章のセットと c18 の復習セット',
            '3. One Hanashishou band 1 scene from the list above, once a week: ______________________ / 週に一回、上の一覧から'
            'バンド1の場面を一つ',
            '4. Time: about 3 hours of home practice for chapter 18 (planning figure); when and where: ______________ / 時間：'
            '第18章の家庭学習は約3時間（目安）。いつ、どこで',
            '5. My next step: Stage 3 (B1), when the course offers it, starts from chapters 16 and 17 again. / 次の一歩：第3段階'
            '（B1）は第16・17章の復習から始まります。']),
    ]
    key = [
        'Timing: results and feedback 10, can-do review 15, Hanashishou demonstration 10, practice plan 10 (45 minutes). Give '
        'back the marked papers of 18C and 18D; use the item maps on the administration sheet to show each learner the chapters '
        'of the items they missed.',
        'A learner who passed the A2 stage test has "Malay A2 · Stage 2 complete" (Sam\'s decision A4; a local completion label, '
        'not a certificate). "Not yet": the practice plan names the chapters to revisit, then the learner sits the other version.',
        f'Hanashishou scenes (Hanashishou {HANASHISHOU_COMMIT}): every scene named has band 1 choices, but its Malay is not yet '
        'tagged by chapter (build step 6), so no scene is assigned to a chapter here. Some band 1 lines still use words a learner '
        'has not met (the plan, section 5: «tertinggal» in lost_wallet, «perlu» in guardhouse_parcel); play them with the class '
        'first.',
        'The learner keeps the can-do sheet and the plan. Cikgu Sensai keeps no learner records.',
    ]
    return dict(slug='feedback', type='Task', title='18E · Feedback, can-do review and next steps', block='18E', minutes=45,
                sections=sections, key=key,
                explain=('フィードバックと次の一歩の45分のブロック（18E）です。テストの結果を返し、第2段階の「できること」を確認し、'
                         'Hanashishou のバンド1の場面を実演し、自分の練習計画を立てます。日本語は未監修です。',
                         'A 45-minute block (18E): the A2 test results, the Stage 2 can-do review, a demonstration of Hanashishou band 1 '
                         'scenes and a personal practice plan.'),
                sub_type='feedback', tests=[], patterns=[], grammar=[FOCUS[n] for n in TESTED],
                goal=GOALS['E'], skills=['reading', 'speaking'])


# --- The chapter 18 teaching plan -----------------------------------------------------------------------------------------

SPACED = [  # plan section 6: chapter -> where its patterns return
    (10, '11, 13 and 18'), (11, '12, 14 and 18'), (12, '13, 15 and 18'), (13, '14, 16 and 18'), (14, '15, 17 and 18'),
    (15, '16 and 18'), (16, '17 and 18 (18A and 18B), then Stage 3'), (17, '18 (18A and 18B), then Stage 3'),
]


def plan_component():
    from .stage2 import TOTAL_BLOCKS, TOTAL_HOURS, HOURS, TIMING
    blocks = [
        f'18A · Integrated review (45): recall 5, the Kata-Kata c18 working week 10, the pattern round (every chapter 10 to 17 '
        f'frame, five theme stations) 15, the notice board 10, self-check 5. Goal: {GOALS["A"]}',
        f'18B · Rehearsal and targeted repair (45): recall 5, a new colleague\'s day 10, the parcel problem 10, the changed '
        f'invitation 10, targeted repair of the Stage 2 rules 10. Goal: {GOALS["B"]}',
        f'18C · The A2 written check (45): listening {TIMING["listening"]}, reading {TIMING["reading"]}, writing '
        f'{TIMING["writing"]} minutes; version A or B (A2 stage test papers and the administration sheet). Goal: {GOALS["C"]}',
        f'18D · Speaking (45): about {TIMING["speaking"]} minutes per learner, one examiner, six learners; a self-introduction '
        f'with an invitation, one request card and one mishap card. Goal: {GOALS["D"]}',
        f'18E · Feedback, the can-do review, a Hanashishou band 1 demonstration and a personal practice plan (45). Goal: {GOALS["E"]}',
    ]
    sections = [
        ('Chapter 18 at a glance · 第18章の概要', [
            'Chapter 18 closes Stage 2 (A2). It adds no new word: every Malay line uses the words of chapters 1 to 17. Kata-Kata '
            'c18 ("Stage 2 review") is the review spine: its six frames and its 22 scenario lines are used word for word '
            'in 18A. / 第18章は第2段階（A2）のまとめです。新しい語はありません。',
            *blocks]),
        ('Spaced returns · 間隔をあけた復習', [
            'Plan section 6: each pattern returns in chapter n+1, n+3 and chapter 18. / 各文型は第n+1章、第n+3章、第18章で戻ります。',
            *[f'Chapter {n} → chapters {where}' for n, where in SPACED],
            'Chapters 16 and 17 have their own chapter 18 tasks: every one of their frames returns in the 18A pattern round and '
            'again in the 18B rehearsals (the parcel problem, the changed invitation). Their third return falls after chapter 18, '
            'so it is carried forward to Stage 3 (the Stage 2 record lists it).']),
        ('Fast course · 速習コース', [
            'The fast course has one 45-minute chapter 18 pack: 20 review words from chapters 10 to 17, the six c18 frames, one '
            'conversation from the working week, a review task and a self-check. The pack is not the test: a fast-course learner '
            'sits the same A2 stage test (18C and 18D) to complete Stage 2.']),
        ('Hours check · 時間の確認', [
            f'Stage 2: {HOURS["teaching_units"]} teaching-unit blocks (11 units × 5), {HOURS["reviews"]} review blocks (after 11B, '
            f'12B, 15), {HOURS["writing"]} writing blocks (after 10B, 12A, 14, 16) and {HOURS["chapter18"]} chapter 18 blocks: '
            f'{TOTAL_BLOCKS} blocks of 45 minutes = {TOTAL_HOURS:g} class hours (plan section 1). Each further six learners adds '
            'one speaking block outside this total (Sam\'s decision A3).',
            'Home practice for chapter 18: about 3 hours (planning figure).']),
    ]
    key = [
        'Before 18A: print the 18A and 18B sheets for each learner; choose version A or B of the A2 stage test; read the '
        'administration sheet.',
        'Standing rules for every chapter 18 line: «dari» / «daripada»; the ‹-kan› rule; the bare root only in dialogue; noun '
        'objects for «tangguhkan» and «batalkan»; «kita» against «kami»; «Lain kali, ya?» only when no new day is offered; '
        '«sudi» for invitations, «boleh» for everyday requests; no ruling words («keputusan») in casual turns; no faith-specific '
        'expressions; the clinic lines give no diagnosis, medicine or treatment advice.',
        'All names, places and times are fictional. All Japanese is a draft awaiting native review.',
    ]
    return dict(slug='teaching-plan', type='Teaching plan', title='Teaching plan · Chapter 18 (18A to 18E)', block=None, minutes=None,
                sections=sections, key=key,
                explain=('第18章（18A〜18E）の指導計画です：各ブロックの時間配分、間隔をあけた復習、速習コース、時間の確認。日本語は未監修です。',
                         'The chapter 18 teaching plan: the five blocks and their timings, the spaced returns, the fast course and '
                         'the Stage 2 hours check.'),
                sub_type='plan', tests=[], patterns=list(C18_FRAMES), grammar=[FOCUS[n] for n in TESTED] + [FOCUS[18]],
                goal='I can run chapter 18 in five blocks and close Stage 2.', skills=[])


GOALS = {
    'A': 'I can use the language of chapters 10 to 17 together, without notes, across the five themes.',
    'B': 'I can handle a new colleague\'s day, a parcel problem and a changed invitation, and repair my weak patterns.',
    'C': 'I can complete the written A2 check: listening, reading and writing.',
    'D': 'I can introduce myself, answer an invitation, make a request and report a small mishap.',
    'E': 'I can review my Stage 2 can-do goals, choose what to practise and start a Hanashishou band 1 scene.',
}


def components(ledger):
    return [plan_component(), review_component(), rehearsal_component(), feedback_component()]


UNIT = dict(unit_id=UNIT_ID, label='18', chapter_id='ms-c18', check_unit=UNIT_ID, id_prefix=UNIT_ID, level='A2',
            title_prefix='Unit 18', header='Unit 18 (ms-c18)', menu_title='Chapter 18 · Stage 2 review and A2 check', genre='Review',
            goal='I can complete the course\'s integrated daily-life, office, home, health and social tasks, identify what I need to '
                 'practise, and start an appropriately tagged band 1 scene.',
            blocks=GOALS, prerequisites=[f'ms-c{k:02}' for k in range(1, 18)], prerequisite_units=['ms-c17'],
            prereq_grammar=[FOCUS[n] for n in TESTED], word_scope=None, components=components)
