"""Unit 16: accidents with ter-: a key left inside the flat, a spilt coffee and a broken cup, a slip on the stairs
(Saya tertinggal ___ di ___; Maaf, saya ___; ___ tertumpah di ___; Saya tidak sengaja ___ ___; Pintu terkunci. Boleh tolong ___?;
Yang ini ___, tetapi dompet saya ___ di rumah).

23 core ledger entries, the rows the ledger places in "Ch16 (unit 16)": the existing rows L-0619 «tertinggal», L-0621 «terlepas», L-0644 «terlupa»,
L-0752 «tersilap», L-0758 «tidak sengaja» and L-0875 «tersangkut», and the new rows L-1235 to L-1251. They come in four groups: ter- accidents (9),
ter- states and results (5), by accident, an accident, the key and the spill (4) and what you see (5). No recognition word. Each ter- word is learned whole,
with its root as the Kata-Kata chapter 16 card notes give it. The scene follows Kata-Kata c16 (scenario lines ms-c16-s01 to s17: Tanaka locked out of the flat,
Mei Ling late and the spilt coffee, then Tanaka at the clinic reception) word for word, and goes further in class: a second locked-out case, a late colleague,
a clinic form. All names, items and times are fictional.

The chapter 6 superlative ter- («termurah», «terbesar», «terbaik», "the most") and the accident ter- (this chapter, "by accident, without meaning to") are shown side
by side, as the first Kata-Kata cards do. «terkunci», «tercedera», «terbakar» and «terputus» name a state that lasts, not an action. The clinic scene describes the
injury only as Kata-Kata does («bengkak», «luka kecil», «lebam»): the receptionist registers Mr Tanaka and asks him to wait; the unit gives no diagnosis,
no treatment advice and no medicine. Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

ACCIDENT = ['L-1235', 'L-0619', 'L-0644', 'L-1236', 'L-0621', 'L-0752', 'L-1237', 'L-1238', 'L-1241']
STATE = ['L-1239', 'L-1240', 'L-1242', 'L-1243', 'L-0875']
WHOLE = ['L-0758', 'L-1244', 'L-1251', 'L-1250']
SEE = ['L-1245', 'L-1246', 'L-1247', 'L-1248', 'L-1249']
CORE = ACCIDENT + STATE + WHOLE + SEE

# Revision: words placed in chapters 1 to 15 that the unit really uses (a test fails if one is not used).
REV_TER6 = ['L-0275', 'L-0276', 'L-0277']
REV_SORRY = ['L-0018', 'L-1062', 'L-0254', 'L-0401', 'L-0375', 'L-0997']
REV_THINGS = ['L-0565', 'L-0571', 'L-1061', 'L-0567', 'L-0568', 'L-0354', 'L-0261', 'L-0259', 'L-0373', 'L-0525', 'L-0504', 'L-0573', 'L-0070', 'L-0064', 'L-1052', 'L-0332']
REV_MOVE = ['L-0339', 'L-0321', 'L-0620', 'L-0207', 'L-0379', 'L-0170', 'L-0587']
REV_OFFICE = ['L-0595', 'L-1175', 'L-0648', 'L-0419', 'L-0407', 'L-0406', 'L-0496', 'L-1046', 'L-0654', 'L-0653', 'L-1171']

EXAMPLES = {
    # ter- accidents
    'L-1235': '«Telefon saya terjatuh di lantai.»',
    'L-0619': '«Saya tertinggal telefon di pejabat.»',
    'L-0644': '«Maaf, saya terlupa.»',
    'L-1236': '«Maaf, saya tertidur di dalam bas.»',
    'L-0621': '«Saya terlepas bas.»',
    'L-0752': '«Maaf, saya tersilap nombor.»',
    'L-1237': '«Air kopi tertumpah di meja.»',
    'L-1238': '«Saya tidak sengaja terlanggar kerusi.»',
    'L-1241': '«Saya tergelincir di tangga tadi.»',
    # ter- states and results
    'L-1239': '«Pintu terkunci.»',
    'L-1240': '«Dia tercedera di tangga.»',
    'L-1242': '«Roti itu terbakar.»',
    'L-1243': '«Talian telefon terputus.»',
    'L-0875': '«Saya tersangkut di jalan yang sesak.»',
    # by accident, an accident, the key and the spill
    'L-0758': '«Awak tidak sengaja.»',
    'L-1244': '«Ada kemalangan di jalan itu.»',
    'L-1251': '«Kunci saya tertinggal di dalam rumah.»',
    'L-1250': '«Air tumpah di lantai.»',
    # what you see
    'L-1245': '«Ada luka kecil di tangan saya.»',
    'L-1246': '«Lutut saya lebam.»',
    'L-1247': '«Tangan saya bengkak.»',
    'L-1248': '«Hati-hati, lantai licin.»',
    'L-1249': '«Cawan saya pecah.»',
    # Revision · the ter- of chapter 6
    'L-0275': '«Yang ini termurah.»',
    'L-0276': '«Beg ini terbesar.»',
    'L-0277': '«Yang ini terbaik.»',
    # Revision · sorry and reply
    'L-0018': '«Maaf, saya lambat.»',
    'L-1062': '«Jangan risau.»',
    'L-0254': '«Jangan risau. Mesyuarat belum bermula.»',
    'L-0401': '«Sila tunggu sekejap.»',
    'L-0375': '«Tolong hubungi pejabat pengurusan.»',
    'L-0997': '«Betul, kunci saya ada di dalam.»',
    # Revision · things and places
    'L-0565': '«Pintu itu terkunci.»',
    'L-0571': '«Lantai itu licin.»',
    'L-1061': '«Saya tergelincir di tangga.»',
    'L-0567': '«Air kopi tertumpah di meja.»',
    'L-0568': '«Kerusi itu ada di sebelah meja.»',
    'L-0354': '«Cawan saya pecah.»',
    'L-0261': '«Air kopi saya tertumpah.»',
    'L-0259': '«Air tumpah di lantai.»',
    'L-0373': '«Saya ambil tisu.»',
    'L-0525': '«Fail encik sedikit basah.»',
    'L-0504': '«Beg saya tertinggal di dalam kereta.»',
    'L-0573': '«Telefon saya tertinggal di rumah.»',
    'L-0070': '«Kunci saya tertinggal di dalam rumah.»',
    'L-0064': '«Saya tertinggal fail di pejabat.»',
    'L-1052': '«Kunci tertinggal di dalam bilik.»',
    'L-0332': '«Saya tergelincir di sebelah lif.»',
    # Revision · moving about and time
    'L-0339': '«Saya naik teksi, bukan bas.»',
    'L-0321': '«Saya tersangkut di jalan yang sesak.»',
    'L-0620': '«Jalan itu sesak.»',
    'L-0207': '«Maaf, saya lambat.»',
    'L-0379': '«Saya tergelincir di tangga tadi.»',
    'L-0170': '«Semalam saya terlupa kunci.»',
    'L-0587': '«Talian terputus.»',
    # Revision · office and clinic
    'L-0595': '«Pengawal itu menghubungi pejabat pengurusan.»',
    'L-1175': '«Boleh tolong hubungi pejabat pengurusan?»',
    'L-0648': '«Encik perlu mendaftar dulu.»',
    'L-0419': '«Ini borang.»',
    'L-0407': '«Doktor ada di klinik.»',
    'L-0406': '«Saya pergi ke klinik.»',
    'L-0496': '«Encik menunggu di sini.»',
    'L-1046': '«Sila tunggu sekejap.»',
    'L-0654': '«Unit berapa, encik?»',
    'L-0653': '«Blok B, unit 12-3.»',
    'L-1171': '«Saya menunggu di lobi.»',
}

# For the ter- words and the whole words: the root as the Kata-Kata card note gives it, with its chapter, and the meaning "by accident, without meaning to".
VOCAB_OPTS = {
    'L-1235': {'en': 'to fall, by accident, without meaning to (‹ter-› + ‹jatuh›; the root is not taught alone)',
               'ja': 'うっかり落ちる・転ぶ（‹ter-›＋‹jatuh›；語根は単独では教えない）'},
    'L-0619': {'en': 'to be left behind, by accident, without meaning to (‹ter-› + «tinggal», chapter 2); not «hilang» (lost, chapter 15)',
               'ja': '（うっかり）置き忘れる（‹ter-›＋«tinggal»（第2章））；«hilang»（第15章、なくした）とは違う'},
    'L-0644': {'en': 'to forget, by accident, without meaning to (‹ter-› + «lupa», chapter 4)',
               'ja': 'うっかり忘れる（‹ter-›＋«lupa»（第4章））'},
    'L-1236': {'en': 'to fall asleep, by accident, without meaning to (‹ter-› + «tidur», chapter 4)',
               'ja': 'うっかり寝てしまう（‹ter-›＋«tidur»（第4章））'},
    'L-0621': {'en': 'to miss (a bus, a chance), without meaning to (‹ter-› + «lepas», chapter 4)',
               'ja': '（バスやチャンスを）逃す・乗り遅れる（‹ter-›＋«lepas»（第4章））'},
    'L-0752': {'en': 'to get something wrong, by mistake, without meaning to (‹ter-› + ‹silap›; the root is not taught alone)',
               'ja': 'うっかり間違える（‹ter-›＋‹silap›；語根は単独では教えない）'},
    'L-1237': {'en': 'to spill, by accident, without meaning to (‹ter-› + «tumpah», this chapter)',
               'ja': 'うっかりこぼれる（‹ter-›＋«tumpah»（この章））'},
    'L-1238': {'en': 'to bump into, by accident, without meaning to (‹ter-› + ‹langgar›; the root is not taught alone)',
               'ja': 'うっかりぶつかる（‹ter-›＋‹langgar›；語根は単独では教えない）'},
    'L-1241': {'en': 'to slip, without meaning to (‹ter-› + ‹gelincir›; the root is not taught alone)',
               'ja': '滑る・足をとられる（‹ter-›＋‹gelincir›；語根は単独では教えない）'},
    'L-1239': {'en': 'locked: a state, not an action (‹ter-› + «kunci», this chapter): «Pintu terkunci.» = the door is locked',
               'ja': '鍵がかかっている：動作ではなく状態（‹ter-›＋«kunci»（この章））；«Pintu terkunci.»＝ドアに鍵がかかっている'},
    'L-1240': {'en': 'injured, hurt: a state, not an action (‹ter-› + ‹cedera›; the root is not taught alone)',
               'ja': 'けがをしている：動作ではなく状態（‹ter-›＋‹cedera›；語根は単独では教えない）'},
    'L-1242': {'en': 'burnt, on fire: a state (‹ter-› + ‹bakar›; the root is not taught alone): «Roti itu terbakar.» = the bread is burnt',
               'ja': '焼けている・燃えている：状態（‹ter-›＋‹bakar›；語根は単独では教えない）；«Roti itu terbakar.»＝パンが焦げた'},
    'L-1243': {'en': 'cut off, disconnected: a state (‹ter-› + ‹putus›; the root is not taught alone): a call or a line',
               'ja': '切れている：状態（‹ter-›＋‹putus›；語根は単独では教えない）：電話や回線'},
    'L-0875': {'en': 'stuck, caught (in traffic or somewhere) (‹ter-› + ‹sangkut›; the root is not taught alone)',
               'ja': '（渋滞などで）身動きがとれない（‹ter-›＋‹sangkut›；語根は単独では教えない）'},
    'L-0758': {'en': 'by accident, not on purpose; with a ‹ter-› verb it adds emphasis: «Saya tidak sengaja terlanggar kerusi.»; spoken ‹tak sengaja›',
               'ja': 'うっかり・わざとではなく；‹ter-› の動詞と一緒に使うと強調になる：«Saya tidak sengaja terlanggar kerusi.»；話し言葉は ‹tak sengaja›'},
    'L-1244': {'en': 'accident: learn it as a whole word (‹ke-an› words come in Stage 3; the root ‹malang› is not taught alone); Malaysian «kemalangan»',
               'ja': '事故：一語として覚える（‹ke-an› の語は第3段階；語根 ‹malang› は単独では教えない）；マレーシアでは «kemalangan»'},
    'L-1251': {'en': 'key; the root of «terkunci»: «Kunci saya tertinggal di dalam rumah.»',
               'ja': '鍵；«terkunci» の語根：«Kunci saya tertinggal di dalam rumah.»'},
    'L-1250': {'en': 'to spill; spilled; the root of «tertumpah»; everyday «Air tumpah!»',
               'ja': 'こぼれる；«tertumpah» の語根；日常は «Air tumpah!»'},
    'L-0275': {'en': 'the cheapest: the chapter 6 ‹ter-› + «murah», "the most" (not an accident)',
               'ja': '一番安い：第6章の ‹ter-›＋«murah»、「最も」の意味（うっかりではない）'},
    'L-0276': {'en': 'the biggest: the chapter 6 ‹ter-› + «besar», "the most" (not an accident)',
               'ja': '一番大きい：第6章の ‹ter-›＋«besar»、「最も」の意味（うっかりではない）'},
    'L-0277': {'en': 'the best: the chapter 6 ‹ter-› + «baik», "the most" (not an accident)',
               'ja': '一番よい：第6章の ‹ter-›＋«baik»、「最も」の意味（うっかりではない）'},
}

P = [
    ('ms-c16-f01', '«Saya tertinggal» ___ «di» ___ «.»  (left behind by accident)', [
        'A: «Awak mencari apa?» B: «Saya mencari telefon saya. Saya tertinggal telefon di pejabat.»',
        'A: «Kenapa awak balik ke rumah?» B: «Saya tertinggal dompet di rumah.»',
        'A: «Beg awak di mana?» B: «Maaf, saya tertinggal beg di dalam kereta.»',
        'A: «Awak tertinggal apa di bilik mesyuarat?» B: «Saya tertinggal fail saya di bilik mesyuarat.»',
        'A: «Kunci awak tertinggal di dalam?» B: «Betul, kunci saya tertinggal di dalam bilik.»',
        'A: «Bila awak tertinggal kunci itu?» B: «Tadi pagi. Kunci saya tertinggal di dalam rumah.»'],
     "«tertinggal» is ‹ter-› + «tinggal» (chapter 2): to be left behind, by accident, without meaning to. «Saya tertinggal ___ di ___.» (the Kata-Kata frame): you are the one who left it, and you say what and where: «Saya tertinggal telefon di pejabat.» "
     "The thing can also be the subject: «Kunci saya tertinggal di dalam rumah.» (Kata-Kata line s01): my key was left inside the flat. «tertinggal» is not «hilang» (chapter 15): «hilang» means you cannot find it; «tertinggal» means you know where you left it, but you did not mean to.",
     "«tertinggal» は ‹ter-›＋«tinggal»（第2章）で、うっかり、そのつもりなく置いてきた、という意味です。«Saya tertinggal ___ di ___.»（Kata-Kata の文型）：自分が置き忘れた人で、何をどこに、と言います：«Saya tertinggal telefon di pejabat.» "
     "物を主語にもできます：«Kunci saya tertinggal di dalam rumah.»（Kata-Kata の s01）：私の鍵が家の中に残っている。«tertinggal» は «hilang»（第15章）とは違います：«hilang» は見つからないこと、«tertinggal» はどこに置いたか分かっていて、わざとではないことです。",
     'Japanese 〜を置き忘れた and 〜が家に残っている are two sentences with two different shapes. Malay says both with «tertinggal»: «Saya tertinggal telefon di pejabat.» and «Kunci saya tertinggal di dalam rumah.» There is no word for しまった: ‹ter-› carries "by accident, without meaning to".',
     '日本語の「〜を置き忘れた」と「〜が家に残っている」は形の違う二つの文ですが、マレー語はどちらも «tertinggal» で言います：«Saya tertinggal telefon di pejabat.»・«Kunci saya tertinggal di dalam rumah.» 「しまった」にあたる語はなく、‹ter-› が「うっかり、そのつもりなく」を表します。'),
    ('ms-c16-f02', '«Maaf, saya» ___ «.»  (an apology with a ter- verb)', [
        'A: «Awak lambat!» B: «Maaf, saya terlepas bas.»',
        'A: «Fail itu di mana?» B: «Maaf, saya terlupa.»',
        'A: «Nombor ini bukan nombor Encik Tanaka.» B: «Maaf, saya tersilap nombor.»',
        'A: «Kenapa awak tidak datang tadi?» B: «Maaf, saya tertidur.»',
        'A: «Awak sudah menghantar mesej itu?» B: «Maaf, saya terlupa. Saya hantar sekarang.»',
        'A: «Jangan risau.» B: «Terima kasih. Maaf, saya tersangkut di jalan yang sesak.»'],
     "To say sorry for a small accident, say «Maaf,» and then «saya» and the ‹ter-› verb: «Maaf, saya terlupa.» (the Kata-Kata frame). The ‹ter-› verb already says \"by accident, without meaning to\", so you need no more. "
     "The usual answer is short and kind: «Jangan risau.» (Kata-Kata line s07). The verbs for this pattern: «terlupa» (forgot), «terlepas» (missed), «tersilap» (got it wrong), «tertidur» (fell asleep), «tersangkut» (got stuck). "
     "Add what you will do next if you can: «Maaf, saya terlupa. Saya hantar sekarang.»",
     "小さな失敗を謝るときは、«Maaf,» のあとに «saya» と ‹ter-› の動詞を言います：«Maaf, saya terlupa.»（Kata-Kata の文型）。‹ter-› の動詞がすでに「うっかり、そのつもりなく」を表すので、それ以上は要りません。"
     "返事は短くやさしく：«Jangan risau.»（Kata-Kata の s07）。この文型の動詞：«terlupa»（忘れた）・«terlepas»（逃した）・«tersilap»（間違えた）・«tertidur»（寝てしまった）・«tersangkut»（動けなくなった）。"
     "できれば次にすることも足します：«Maaf, saya terlupa. Saya hantar sekarang.»",
     'Japanese says すみません、うっかり忘れてしまいました, with うっかり and てしまう both marking the slip. Malay needs neither: «Maaf, saya terlupa.» is the whole apology. ‹ter-› takes the place of うっかり〜てしまう, and a long apology is not expected for a small slip.',
     '日本語は「すみません、うっかり忘れてしまいました」と、「うっかり」と「〜てしまう」の両方で失敗を示します。マレー語はどちらも要らず、«Maaf, saya terlupa.» で謝罪は十分です。‹ter-› が「うっかり〜てしまう」の代わりをし、小さな失敗に長い謝罪は求められません。'),
    ('ms-c16-f04', '«Saya tidak sengaja» ___ ___ «.»  (by accident, with emphasis)', [
        'A: «Awak terlanggar kerusi?» B: «Ya, saya tidak sengaja terlanggar kerusi itu.»',
        'A: «Cawan awak pecah?» B: «Ya, saya tidak sengaja. Cawan itu terjatuh di lantai.»',
        'A: «Kenapa awak tidak datang?» B: «Maaf, saya tidak sengaja tertidur.»',
        'A: «Lantai ini basah.» B: «Maaf, saya tidak sengaja. Air kopi saya tertumpah.»',
        'A: «Awak terlupa kunci lagi?» B: «Ya, saya tidak sengaja terlupa kunci tadi.»',
        'A: «Awak tidak sengaja?» B: «Ya, saya tidak sengaja. Maaf.»'],
     "«tidak sengaja» means \"by accident, not on purpose\" (the spoken form is ‹tak sengaja›). With a ‹ter-› verb it adds emphasis: «Saya tidak sengaja terlanggar kerusi.» (the Kata-Kata frame). "
     "‹ter-› already says it was not meant; «tidak sengaja» says it once more, which helps when someone might think you did it on purpose. «Awak tidak sengaja.» (Kata-Kata line s09) is how the other person says: \"I know it was not on purpose.\" "
     "«tidak sengaja» can also stand alone: «Ya, saya tidak sengaja.»",
     "«tidak sengaja» は「うっかり・わざとではなく」という意味です（話し言葉は ‹tak sengaja›）。‹ter-› の動詞と一緒に使うと強調になります：«Saya tidak sengaja terlanggar kerusi.»（Kata-Kata の文型）。"
     "‹ter-› がすでに「そのつもりはなかった」を表しますが、«tidak sengaja» はそれをもう一度言うので、わざとだと思われそうなときに役に立ちます。«Awak tidak sengaja.»（Kata-Kata の s09）は、相手が「わざとではないと分かっています」と言う言い方です。"
     "«tidak sengaja» だけでも言えます：«Ya, saya tidak sengaja.»",
     'Japanese 〜するつもりはなかった and うっかり are both near «tidak sengaja». Malay does not need it with ‹ter-›, but a learner who adds it is not wrong: it is a polite way to say that nothing was meant.',
     '日本語の「〜するつもりはなかった」「うっかり」はどちらも «tidak sengaja» に近い言い方です。マレー語では ‹ter-› と一緒なら要りませんが、足しても間違いではなく、悪気がなかったことを丁寧に伝える言い方です。'),
    ('ms-c16-f03 and f06', '___ «tertumpah di» ___ «. / Pintu terkunci. Boleh tolong» ___ «?»  (a thing is the subject: what happened, and what you ask for)', [
        'A: «Kenapa meja itu basah?» B: «Air kopi tertumpah di meja.»',
        'A: «Pintu terkunci. Boleh tolong hubungi pejabat pengurusan?» B: «Boleh. Unit berapa, encik?»',
        'A: «Kenapa awak tidak masuk?» B: «Pintu terkunci, dan kunci saya tertinggal di dalam.»',
        'A: «Kenapa awak tidak menelefon saya?» B: «Maaf, talian terputus.»',
        'A: «Kenapa awak di tangga?» B: «Lif itu rosak. Saya tergelincir di tangga.»',
        'A: «Cawan itu kenapa?» B: «Cawan saya pecah. Air kopi tertumpah di lantai.»'],
     "When a thing is the subject, ‹ter-› says what happened to it: «Air kopi tertumpah di meja.» (the Kata-Kata frame). The same ‹ter-› can name a state that lasts: «Pintu terkunci.» (the door is locked), «Talian terputus.» (the line is cut off), «tercedera» (hurt), «terbakar» (burnt). "
     "A state is not an action: nobody is locking the door now. After the state you can ask for help: «Pintu terkunci. Boleh tolong hubungi pejabat pengurusan?» (the Kata-Kata frame). «tolong» + the plain root is the request.",
     "物が主語のとき、‹ter-› はその物に何が起きたかを言います：«Air kopi tertumpah di meja.»（Kata-Kata の文型）。同じ ‹ter-› が、続いている状態も言えます：«Pintu terkunci.»（ドアに鍵がかかっている）・«Talian terputus.»（回線が切れている）・«tercedera»（けがをしている）・«terbakar»（焼けている）。"
     "状態は動作ではありません。いま鍵をかけている人はいません。状態を言ったあとで助けを頼めます：«Pintu terkunci. Boleh tolong hubungi pejabat pengurusan?»（Kata-Kata の文型）。«tolong»＋素の語根が依頼です。",
     'Japanese 鍵がかかっている (a state, with ている) and 鍵をかけてしまった (an action, with てしまう) are two forms. Malay «terkunci» can be either: «Pintu terkunci.» is the state. Compare the 〜ている feeling of «terkunci», «terputus» and «tercedera» with the 〜てしまった feeling of «terlupa» and «terlepas».',
     '日本語の「鍵がかかっている」（状態、ている）と「鍵をかけてしまった」（動作、てしまう）は別の形です。マレー語の «terkunci» はどちらにもなれますが、«Pintu terkunci.» は状態です。«terkunci»・«terputus»・«tercedera» の「〜ている」の感じと、«terlupa»・«terlepas» の「〜てしまった」の感じを比べましょう。'),
    ('ms-c16-f05', '«Yang ini» ___ «, tetapi dompet saya» ___ «di rumah.»  (the two ter-: the most, and by accident)', [
        'A: «Telefon ini murah?» B: «Yang ini termurah, tetapi dompet saya tertinggal di rumah.»',
        'A: «Yang mana terbesar?» B: «Yang ini terbesar, tetapi beg saya tertinggal di pejabat.»',
        'A: «Telefon ini terbaik?» B: «Ya, yang ini terbaik, tetapi kad saya tertinggal di rumah.»',
        'A: «Kenapa awak tidak membeli telefon itu?» B: «Telefon itu termurah, tetapi dompet saya tertinggal di rumah.»',
        'A: «Bas ini yang terbaik.» B: «Maaf, saya terlepas bas itu.»',
        'A: «Saya mahu cawan yang termurah.» B: «Yang ini termurah. Yang itu pecah.»'],
     "‹ter-› has two meanings. In front of an adjective it means \"the most\": «termurah» (the cheapest), «terbesar» (the biggest), «terbaik» (the best): chapter 6. In front of a verb it means \"by accident, without meaning to\": «tertinggal», «terlupa», «terlepas»: this chapter. "
     "The Kata-Kata frame puts both in one sentence: «Yang ini termurah, tetapi dompet saya tertinggal di rumah.» Look at the root: «murah», «besar» and «baik» describe things (adjectives), so ‹ter-› means \"the most\"; «tinggal», «lupa» and «lepas» are actions, so ‹ter-› means \"by accident\". "
     "Learn each ‹ter-› word as a word: not every ‹ter-› form is on this list, and the prefix alone does not tell you the meaning.",
     "‹ter-› には二つの意味があります。形容詞の前では「最も」：«termurah»（一番安い）・«terbesar»（一番大きい）・«terbaik»（一番よい）：第6章。動詞の前では「うっかり、そのつもりなく」：«tertinggal»・«terlupa»・«terlepas»：この章です。"
     "Kata-Kata の文型は両方を一つの文に入れます：«Yang ini termurah, tetapi dompet saya tertinggal di rumah.» 語根を見ましょう：«murah»・«besar»・«baik» は物の様子（形容詞）なので ‹ter-› は「最も」、«tinggal»・«lupa»・«lepas» は動作なので ‹ter-› は「うっかり」です。"
     "‹ter-› の語は一つずつ覚えます：‹ter-› の形がすべてこの表にあるわけではなく、接頭辞だけでは意味は決まりません。",
     'Japanese keeps the two ideas apart: 一番〜 (the most) and うっかり〜てしまう (by accident). Malay uses one prefix for both, so the root decides. A learner who reads «terbesar» as "accidentally big" or «tertinggal» as "the most left" has mixed them.',
     '日本語は「一番〜」（最も）と「うっかり〜てしまう」（偶然）をはっきり分けます。マレー語は一つの接頭辞で両方を言うので、語根が決め手になります。«terbesar» を「うっかり大きい」、«tertinggal» を「一番残っている」と読むと、二つを混ぜています。'),
]

# The Kata-Kata scenario lines ms-c16-s01 to s17 are the model conversation. Turn 11 joins s11 and s12 (Tanaka thanks Mei Ling and warns about the floor, then,
# next morning, tells the clinic receptionist he slipped), so the whole scene fits the 16 turns the charter allows. The clinic turns only register him and ask him to wait.
DIALOGUE = [
    ('Tanaka', 'Selamat malam. Maaf, kunci saya tertinggal di dalam rumah. Pintu terkunci.'),
    ('Guard', 'Unit berapa, encik?'),
    ('Tanaka', 'Blok B, unit 12-3. Saya terlupa kunci tadi.'),
    ('Guard', 'Encik tunggu di sini. Saya hubungi pejabat pengurusan.'),
    ('Tanaka', 'Baik. Terima kasih banyak.'),
    ('Mei Ling', 'Maaf, saya lambat. Saya terlepas bas, kemudian saya tersangkut di jalan yang sesak.'),
    ('Tanaka', 'Jangan risau. Mesyuarat belum bermula.'),
    ('Mei Ling', 'Maaf, Encik Tanaka! Air kopi saya tertumpah di meja. Cawan saya pun pecah.'),
    ('Tanaka', 'Awak tidak sengaja. Jangan risau.'),
    ('Mei Ling', 'Saya ambil tisu. Fail encik sedikit basah.'),
    ('Tanaka', 'Terima kasih. Hati-hati, lantai licin. Selamat pagi. Saya tergelincir di tangga tadi.'),
    ('Receptionist', 'Encik tercedera? Di mana yang sakit?'),
    ('Tanaka', 'Tangan saya bengkak dan ada luka kecil. Lutut saya pun lebam.'),
    ('Receptionist', 'Encik perlu daftar dulu. Ini borang.'),
    ('Tanaka', 'Baik. Boleh doktor melihat tangan saya sekarang?'),
    ('Receptionist', 'Boleh. Sila tunggu sekejap.'),
]
# Changed facts: Mei Ling is locked out of unit 8-5 and the management office is not open yet.
VARIANT = [
    ('Mei Ling', 'Selamat petang. Maaf, kunci saya tertinggal di dalam bilik. Pintu terkunci.'),
    ('Guard', 'Unit berapa, cik?'),
    ('Mei Ling', 'Blok A, unit 8-5. Saya terlupa kunci tadi.'),
    ('Guard', 'Cik tunggu di sini. Saya hubungi pejabat pengurusan.'),
    ('Mei Ling', 'Baik. Terima kasih banyak.'),
    ('Guard', 'Maaf, pejabat pengurusan belum buka. Cik tunggu sekejap.'),
    ('Mei Ling', 'Boleh saya duduk di lobi?'),
    ('Guard', 'Boleh. Sila duduk.'),
    ('Mei Ling', 'Terima kasih. Saya tidak sengaja terlupa kunci itu.'),
    ('Guard', 'Jangan risau, cik.'),
]
LISTENING = [
    ('Rahman', 'Selamat pagi, Puan Aini. Awak lambat hari ini. Kenapa?'),
    ('Aini', 'Maaf, encik. Pagi tadi saya tertidur. Kemudian saya terlepas bas.'),
    ('Rahman', 'Awak naik apa ke pejabat?'),
    ('Aini', 'Saya naik teksi. Tetapi teksi itu tersangkut di jalan yang sesak. Ada kemalangan di jalan itu.'),
    ('Rahman', 'Awak sudah menghubungi saya?'),
    ('Aini', 'Belum, encik. Telefon saya tertinggal di rumah. Pemandu teksi menelefon pejabat untuk saya, tetapi talian terputus.'),
    ('Rahman', 'Jangan risau. Mesyuarat belum bermula.'),
    ('Aini', 'Terima kasih, encik. Maaf, saya juga tersilap hari. Saya ingat mesyuarat hari Khamis.'),
    ('Rahman', 'Mesyuarat hari ini. Fail awak ada di bilik saya. Awak tertinggal fail itu semalam.'),
    ('Aini', 'Oh, maaf. Saya tidak sengaja terlupa fail itu. Saya ambil fail itu sekarang.'),
    ('Rahman', 'Baik. Sila minum kopi dulu.'),
    ('Aini', 'Terima kasih, encik. Hari ini saya tidak mahu terlupa lagi.'),
]

CULTURE = [
    'Japanese marks a slip twice: うっかり before the verb and 〜てしまった after it. Malay marks it once, inside the verb: ‹ter-› says "by accident, without meaning to". '
    'So «Maaf, saya terlupa.» is a complete apology. A long, formal apology for a small slip can even sound too heavy; the other person usually answers «Jangan risau.»',
    'The apology depends on who is responsible. A short «Maaf, saya terlupa.» is right for your own slip. When it is not your fault, say what happened without blame: «Pintu terkunci.» or «Talian terputus.» '
    'These sentences state a fact and leave the doer out, which is the polite way to report a problem to a guard or an office: first what happened, then what you ask for.',
    'General knowledge, not a rule and not a checked fact: condominiums in Malaysia often have a guardhouse and a management office, and a resident who is locked out usually tells the guard first, who then contacts the office. '
    'Practice differs from place to place, so ask at the guardhouse. The names, units and times in this course are fictional.',
    'Japanese learners often use «tertinggal» where Japanese says なくした, or put ‹ter-› on any adjective to mean "too much". The two ‹ter-› meanings of this chapter are only these: "the most" before an adjective («termurah») '
    'and "by accident" before a verb («tertinggal»). When you report an injury at a clinic counter, name only what you can see, as Mr Tanaka does, and let the staff do the rest.',
]
CULTURE_JA = [
    '日本語は失敗を二回示します：動詞の前の「うっかり」と、あとの「〜てしまった」。マレー語は一回で、動詞の中に示します：‹ter-› が「うっかり、そのつもりなく」を表します。'
    'ですから «Maaf, saya terlupa.» だけで謝罪は十分です。小さな失敗に長く改まった謝罪をすると、かえって重く聞こえることがあり、相手はたいてい «Jangan risau.» と答えます。',
    '謝り方は、だれに責任があるかで変わります。自分の失敗なら短く «Maaf, saya terlupa.» で十分です。自分のせいではないときは、責めずに起きたことを言います：«Pintu terkunci.»・«Talian terputus.» '
    'これらは事実を述べるだけで、した人を言いません。警備員や事務所に問題を伝える丁寧な言い方です：まず何が起きたか、次に何を頼みたいかを言います。',
    '一般的な知識であり、規則でも確認済みの事実でもありません：マレーシアのコンドミニアムには警備員室と管理事務所があることが多く、鍵を中に残して入れなくなった住人は、まず警備員に話し、警備員が事務所に連絡するのが普通です。'
    'やり方は場所によって違うので、警備員室で聞いてください。このコースの名前・部屋・時刻はすべて架空です。',
    '日本人の学習者は、日本語で「なくした」と言うところに «tertinggal» を使ったり、形容詞に ‹ter-› を付けて「〜すぎる」の意味にしたりしがちです。この章の ‹ter-› の意味は二つだけです：形容詞の前では「最も」（«termurah»）、'
    '動詞の前では「うっかり」（«tertinggal»）。クリニックの受付でけがを伝えるときは、田中さんのように見えることだけを言い、あとはスタッフに任せます。',
]

CFG = dict(
    chapter=16, label='16', unit_id='ms-c16',
    menu_title='Chapter 16 · Accidents with ter-', genre='Accidents',
    prerequisite_units=['ms-c15'], prereq_grammar=['ms-c15-g02', 'ms-c15-g03', 'ms-c06-g02', 'ms-c12-g02'],
    unit_goal='Say what happened by accident with ter- («tertinggal», «terlupa», «terlepas», «tertumpah», «tergelincir»), apologise for a small slip, report a locked door or a spill to a guard or a colleague, '
              'and tell a clinic receptionist what you can see on your hand and knee, and keep the two ter- of chapters 6 and 16 apart.',
    core=CORE,
    recognition=[],
    revision=[('The ter- of chapter 6 (the most)', REV_TER6), ('Sorry and the reply', REV_SORRY), ('Things and places', REV_THINGS),
              ('Moving about and time', REV_MOVE), ('Office and clinic', REV_OFFICE)],
    core_groups=[('ter- accidents', ACCIDENT), ('ter- states and results', STATE), ('By accident, an accident, the key and the spill', WHOLE), ('What you see', SEE)],
    grammar_ids={'tertinggal': 'ms-c16-g02', 'maaf': 'ms-c16-g03', 'sengaja': 'ms-c16-g04', 'thing': 'ms-c16-g05', 'contrast': 'ms-c16-g06',
                 'state': 'ms-c16-g07', 'hilang': 'ms-c16-g08', 'words': 'ms-c16-g09'},
    grammar=['tertinggal', 'maaf', 'sengaja', 'thing', 'contrast', 'state'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 23 cards ms-c16-001 to ms-c16-023', frame_list='ms-c16-f01 to f06', frame_list_ja='f01〜f06',
    extra=None,
    goals={'A': 'I can say what I left behind or forgot by accident with «tertinggal» and «terlupa», and apologise with «Maaf, saya ___.».',
           'B': 'I can say what spilt, slipped, broke or was cut off with a ‹ter-› verb, say «tidak sengaja» for emphasis, and tell «termurah» from «tertinggal».',
           'C': 'I can follow a call that explains why a colleague is late, read a clinic form and tell a guard a door is locked.',
           'D': 'I can choose between the two ‹ter-› meanings, between «tertinggal» and «hilang», and between a state («terkunci») and an action.',
           'E': 'I can handle a short role-play at a guardhouse or a clinic counter, including a change such as an office that is not open.'},
    goals_ja={'A': '«tertinggal»・«terlupa» でうっかり置き忘れたことや忘れたことを言い、«Maaf, saya ___.» で謝れる。',
              'B': '‹ter-› の動詞でこぼれた・滑った・割れた・切れたことを言い、«tidak sengaja» で強調し、«termurah» と «tertinggal» を区別できる。',
              'C': '同僚が遅れた理由の電話が分かり、クリニックの書類を読み、警備員にドアに鍵がかかっていると言える。',
              'D': '二つの ‹ter-› の意味、«tertinggal» と «hilang»、状態（«terkunci»）と動作を使い分けられる。',
              'E': '警備員室やクリニックの受付での短いロールプレイができ、管理事務所がまだ開いていないといった変更にも対応できる。'},
    setting='An evening and a morning at a condominium and an office in Kuala Lumpur: «Encik» Tanaka is locked out because his key is inside the flat, «Cik» Mei Ling arrives late and spills her coffee, '
            'and the next morning Mr Tanaka slips on the stairs and registers at a clinic. All names, units and times are fictional.',
    setting_ja='クアラルンプールのコンドミニアムと会社の、ある夜と翌朝。田中さんは鍵を家の中に置き忘れて入れなくなり、メイリンさんは遅れてコーヒーをこぼし、'
               '翌朝、田中さんは階段で滑ってクリニックで受付をします。名前・部屋・時刻はすべて架空です。',
    recall=['Without notes, from chapters 6, 9 and 15: say one thing with «termurah» or «terbaik» (chapter 6), one thing you have lost with «hilang» (chapter 15) and one «Maaf, …» sentence (chapter 1). / '
            '第6章・第9章・第15章の復習：«termurah» か «terbaik» で一文（第6章）、«hilang» でなくした物を一文（第15章）、«Maaf, …» の文を一文（第1章）言いましょう。',
            'Recall prompt: «Yang ini termurah.» «Dompet saya hilang.» «Maaf, saya …»'],
    recall_key='e.g. «Yang ini terbaik.» «Beg tangan saya hilang.» «Maaf, saya lambat.» Then show the new step: «tertinggal» for left behind by accident, «terlupa» for forgot, «tidak sengaja» for by accident, and «terkunci» for a state.',
    patterns=P, pattern_ids=['ms-c16-f01', 'ms-c16-f02', 'ms-c16-f03', 'ms-c16-f04', 'ms-c16-f05', 'ms-c16-f06'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 16 frames f01 to f06 (pattern 4 shows f03 and f06 together, a thing as the subject; the patterns run f01, f02, f04, f03 and f06, f05).',
    pattern_keys=['Pattern 1: «tertinggal» + the thing + «di» + the place; the thing can also be the subject («Kunci saya tertinggal …»). If a learner says «hilang» for something left at home, give the situation (you know where it is) and say that «hilang» is for something you cannot find.',
                  'Pattern 2: «Maaf, saya» + a ‹ter-› verb. Accept a short «Maaf.» as a first try, then ask for the verb. Check that the verb is a ‹ter-› verb for a small slip («terlupa», «terlepas», «tersilap», «tertidur», «tersangkut»).',
                  'Pattern 3: «Saya tidak sengaja» + a ‹ter-› verb. Accept the spoken ‹tak sengaja› in a quick answer; ask for «tidak sengaja» once in the written part. Do not mark the sentence without «tidak sengaja» wrong: ‹ter-› already says "by accident".',
                  'Pattern 4: a thing + «tertumpah» or another ‹ter-› word (a result or a state), then a request with «Boleh tolong». Check that «terkunci» and «terputus» are used for a state, with no doer. Accept «Boleh tolong hubungi …?» with the plain root after «tolong».',
                  'Pattern 5: «Yang ini» + «termurah», «terbesar» or «terbaik», then «tetapi» + the thing + «tertinggal» + the place. Ask the learner which ‹ter-› says "the most" and which says "by accident", and why (the root).'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 7, 11, 13),
    drills={
        'repeat_frame': 'Frame: «Saya tertinggal» [«telefon» / «dompet»] «di» [«pejabat» / «rumah»] «.»',
        'repeat': ['«Saya tertinggal telefon di pejabat.»', '«Maaf, saya terlupa.»', '«Air kopi tertumpah di meja.»',
                   '«Saya tidak sengaja terlanggar kerusi.»', '«Pintu terkunci. Boleh tolong hubungi pejabat pengurusan?»',
                   '«Yang ini termurah, tetapi dompet saya tertinggal di rumah.»', '«Saya terlepas bas, kemudian saya tersangkut di jalan yang sesak.»',
                   '«Tangan saya bengkak dan ada luka kecil. Lutut saya pun lebam.»'],
        'substitute': ['«Saya tertinggal telefon di pejabat.» (cue: «dompet», «rumah»)',
                       '«Maaf, saya terlupa.» (cue: «terlepas bas»)',
                       '«Air kopi tertumpah di meja.» (cue: «air», «lantai»)',
                       '«Saya tidak sengaja terlanggar kerusi.» (cue: «meja»)',
                       '«Pintu terkunci.» (cue: «bilik»)',
                       '«Yang ini termurah, tetapi dompet saya tertinggal di rumah.» (cue: «terbaik», «kad», «pejabat»)',
                       '«Saya tergelincir di tangga tadi.» (cue: «lantai»)',
                       '«Lutut saya lebam.» (cue: «tangan», «bengkak»)'],
        'transform': ['Say it with ‹ter-›: «Saya lupa kunci tadi.» (a small slip)',
                      'Say it with «tertinggal»: «Telefon saya ada di pejabat.» (you did not mean to leave it there)',
                      'Add «tidak sengaja»: «Saya terlanggar kerusi.»',
                      'Say that the door is locked, with «terkunci»: «Pintu itu tidak boleh dibuka.»',
                      'Put the thing first, as the subject: «Saya tertinggal kunci di dalam rumah.»',
                      'Say which ‹ter-› means "the most" and which means "by accident": «termurah», «tertinggal».',
                      'Choose «hilang» or «tertinggal»: you know that the key is at home. Say it.',
                      'Say it with «Maaf»: «Saya terlepas bas.»',
                      'Reply kindly to «Maaf, saya terlupa.»',
                      'Say it with «belum»: «Saya jumpa kunci saya.»'],
        'question and answer': ['«Kunci awak di mana?» (cue: «tertinggal», «rumah»)',
                                '«Kenapa awak lambat?» (cue: «terlepas bas»)',
                                '«Kenapa lantai basah?» (cue: «air kopi», «tertumpah»)',
                                '«Telefon awak kenapa?» (cue: «terjatuh», «lantai»)',
                                'You hear: «Saya tergelincir di tangga.» Ask the question («di mana»).',
                                'You hear: «Pintu terkunci.» Ask the question («kenapa»).',
                                'You hear: «Saya terlepas bas tadi.» Ask the question («bila»).',
                                'You hear: «Awak tidak sengaja.» Say the reply («Jangan risau.»).'],
        'question-word choice': ['«___ kunci awak?» → «Tertinggal di dalam rumah.»', '«___ awak lambat?» → «Sebab saya terlepas bas.»',
                                 '«Awak tergelincir di ___?» → «Di tangga.»', '«___ awak tergelincir?» → «Tadi pagi.»',
                                 '«Ada ___ cawan yang pecah?» → «Satu.»', '«___ yang tercedera?» → «Encik Tanaka.»',
                                 '«Pintu itu terkunci. Unit ___?» → «Blok B, unit 12-3.»', '«___ satu yang termurah?» → «Yang ini.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. ‹ter-› + a verb = "by accident"; «tertinggal» goes with «di» and a place; «tidak sengaja» stands in front of the ‹ter-› verb; «tetapi» joins the two sentences in the last frame.',
                   'Cover the line and say it from the English: I left my phone at the office; sorry, I forgot; the coffee spilled on the table; I bumped into the chair by accident; the door is locked, could you contact the management office; '
                   'this one is the cheapest, but my wallet is left at home; I missed the bus, then I got stuck on a congested road; my hand is swollen and there is a small wound, my knee is bruised too.'],
        'substitute': ['1 «Saya tertinggal dompet di rumah.» 2 «Maaf, saya terlepas bas.» 3 «Air tertumpah di lantai.» 4 «Saya tidak sengaja terlanggar meja.»',
                       '5 «Bilik terkunci.» 6 «Yang ini terbaik, tetapi kad saya tertinggal di pejabat.» 7 «Saya tergelincir di lantai tadi.» 8 «Tangan saya bengkak.»'],
        'transform': ['1 «Saya terlupa kunci tadi.» 2 «Telefon saya tertinggal di pejabat.» 3 «Saya tidak sengaja terlanggar kerusi.» 4 «Pintu itu terkunci.» 5 «Kunci saya tertinggal di dalam rumah.»',
                      '6 «termurah» = "the most" (the adjective «murah»); «tertinggal» = "by accident" (the verb «tinggal»). 7 «Kunci saya tertinggal di rumah.» («hilang» is for what you cannot find.) '
                      '8 «Maaf, saya terlepas bas.» 9 «Jangan risau.» 10 «Saya belum jumpa kunci saya.»'],
        'question and answer': ['1 «Kunci saya tertinggal di rumah.» 2 «Saya lambat kerana saya terlepas bas.» 3 «Air kopi tertumpah di lantai.» 4 «Telefon saya terjatuh di lantai.»',
                                '5 «Awak tergelincir di mana?» 6 «Kenapa pintu terkunci?» 7 «Bila awak terlepas bas?» 8 «Jangan risau.»'],
        'question-word choice': ['1 «Di mana» 2 «Kenapa» 3 «di mana» 4 «Bila» 5 «berapa» 6 «Siapa» 7 «berapa» 8 «Yang mana» (also «Mengapa» for 2; the answer starts with «sebab» or «kerana»)'],
    },
    short_dialogues=[
        ('Maaf, saya terlupa.', 'Jangan risau.', 'a small slip'),
        ('Pintu terkunci. Boleh tolong hubungi pejabat pengurusan?', 'Boleh. Unit berapa?', 'at the guardhouse'),
        ('Air kopi tertumpah di meja.', 'Awak tidak sengaja. Saya ambil tisu.', 'a spill'),
        ('Saya tergelincir di tangga tadi.', 'Encik perlu daftar dulu.', 'at the clinic counter')],
    short_keys=['1 «Terima kasih. Saya hantar sekarang.» 2 «Blok B, unit 12-3. Kunci saya tertinggal di dalam.»',
                '3 «Terima kasih. Hati-hati, lantai licin.» 4 «Baik. Boleh doktor melihat tangan saya sekarang?»'],
    markers=dict(
        title='Markers with the ter- verbs', grammar='tertinggal',
        instructions=['Say each sentence again with the marker in brackets. Keep the verb as the course teaches it; only the marker is added in front. / '
                      'かっこ内のマーカーを付けて言い直します。動詞はこのコースで教えた形のままで、前にマーカーを足すだけです。'],
        items=['«Kunci saya tertinggal di rumah.» (marker: «sudah»)', '«Encik Tanaka tergelincir di tangga.» (marker: «baru»)',
               '«Pintu itu terkunci.» (marker: «masih»)', '«Mei Ling tersangkut di jalan yang sesak.» (marker: «sedang»)',
               '«Air kopi tertumpah di meja.» (marker: «baru»)', '«Tangan saya bengkak.» (marker: «masih»)',
               'Answer «Awak sudah jumpa kunci awak?» (marker: «belum»)', '«Pengawal menghubungi pejabat pengurusan.» (marker: «akan»)'],
        bridge=['«sudah tertinggal» ≈ もう置き忘れた · «baru tergelincir» ≈ 滑ったばかり · «masih terkunci» ≈ まだ鍵がかかっている · '
                '«sedang tersangkut» ≈ 動けなくなっている · «belum jumpa» ≈ まだ見つかっていない · «akan menghubungi» ≈ 連絡する予定',
                'Japanese changes the verb ending (置き忘れた / 滑ったばかり); Malay puts the marker in front and keeps the verb («tertinggal», «tergelincir»). «belum» is まだ〜ていない, «sudah» is もう〜た, «masih» is まだ〜ている. / '
                '日本語は動詞の語尾が変わります。マレー語はマーカーを前に置き、動詞（«tertinggal»・«tergelincir»）はそのままです。«belum» は「まだ〜ていない」、«sudah» は「もう〜た」、«masih» は「まだ〜ている」です。'],
        key=['1 «Kunci saya sudah tertinggal di rumah.» 2 «Encik Tanaka baru tergelincir di tangga.» 3 «Pintu itu masih terkunci.» '
             '4 «Mei Ling sedang tersangkut di jalan yang sesak.»',
             '5 «Air kopi baru tertumpah di meja.» 6 «Tangan saya masih bengkak.» 7 «Belum. Saya belum jumpa kunci saya.» '
             '8 «Pengawal akan menghubungi pejabat pengurusan.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、第16章の ‹ter-› の動詞と組み合わせて言います。«terkunci»・«bengkak» のような状態には «masih» がよく合います。',
                 'Combine the chapter 4 markers with the chapter 16 ter- verbs. «masih» goes well with a state such as «terkunci» or «bengkak».')),
    question_note='Chapter 16 adds no new question word. The accident questions use the ones you know: «Kunci awak di mana?», «Kenapa awak lambat?», «Bila awak tergelincir?», «Awak tercedera?», '
                  '«Unit berapa?», «Yang mana satu?» / '
                  '第16章で新しい疑問語は増えません。事故の質問は知っている疑問語で作ります：'
                  '«Kunci awak di mana?»、«Kenapa awak lambat?»、«Bila awak tergelincir?»、«Awak tercedera?»、«Unit berapa?»、«Yang mana satu?»',
    question_tasks=['Ask what the person forgot. («apa»)', 'Ask who slipped on the stairs. («siapa»)',
                    'Ask where the key was left. («di mana»)', 'Ask formally whether the door is locked. («Adakah»)',
                    'Ask politely whether you may sit in the lobby. («Bolehkah»)', 'Ask how many cups are broken. («berapa»)',
                    'Ask when the coffee spilled. («bila»)', 'Ask what time the meeting starts. («pukul berapa»)',
                    'Ask on what day the person missed the bus. («hari apa»)', 'Ask how the hand looks. («bagaimana»; spoken «macam mana»)',
                    'Ask why the person is late. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which cup is broken. («yang mana»)', 'Ask where the guard goes next. («ke mana»)',
                    'Ask where the receptionist is from. («dari mana»)', 'Ask how far the clinic is. («berapa jauh»)',
                    'Ask how long the person waits. («berapa lama»)', 'Ask how many forms there are. («berapa» with a counter)',
                    'Ask who filled in the form. («siapa» with «oleh»)'],
    question_keys=['1 «Awak terlupa apa?» 2 «Siapa yang tergelincir di tangga?» 3 «Kunci itu tertinggal di mana?»',
                   '4 «Adakah pintu itu terkunci?» 5 «Bolehkah saya duduk di lobi?» 6 «Berapa cawan yang pecah?»',
                   '7 «Bila air kopi itu tertumpah?» 8 «Mesyuarat bermula pukul berapa?» 9 «Pada hari apa awak terlepas bas?»',
                   '10 «Bagaimana tangan awak?» (spoken: «Macam mana tangan awak?») 11 «Kenapa awak lambat?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab saya terlepas bas.» / «Kerana saya terlepas bas.»',
                   '12 «Cawan yang mana pecah?» 13 «Selepas ini, pengawal pergi ke mana?» 14 «Penyambut tetamu itu dari mana?»',
                   '15 «Berapa jauh klinik itu?» 16 «Berapa lama awak menunggu?» 17 «Ada berapa keping borang?»',
                   '18 «Borang ini diisi oleh siapa?»'],
    listening=LISTENING,
    listening_context='On a weekday morning «Puan» Aini arrives late and explains to «Encik» Rahman what went wrong on the way. / 平日の朝、アイニさんが遅れて着き、途中で何があったかをラーマンさんに説明します。',
    listening_before=['Predict: which of «terlupa», «terlepas», «tertinggal», «tersangkut» and «tidak sengaja» will you hear? Write three guesses. / «terlupa»・«terlepas»・«tertinggal»・«tersangkut»・«tidak sengaja» のうち聞こえそうなものを三つ予想しましょう。',
                      'Read the seven questions below before the first listening. / 1回目の前に下の7つの質問を読みます。'],
    listen_questions=['What happened first, and what happened next?', 'How did she travel, and what stopped the trip?', 'Why did she not telephone Mr Rahman?',
                      'What happened to the driver\'s telephone call?', 'What did she get wrong?', 'Where was her file, and who left it there?',
                      'What does she say about the file?'],
    listen_answers=['she fell asleep, then missed the bus', 'a taxi; it got stuck on a congested road and there was an accident', 'her telephone was left at home',
                    'the line was cut off', 'the day of the meeting (she thought Thursday)', 'in Mr Rahman\'s room; she left it there yesterday',
                    'she did not do it on purpose; she will fetch it now'],
    listening_after=['Compare answers, then shadow lines 2, 4 and 6 after the teacher. / 答えを比べ、2・4・6行目をシャドーイングします。',
                     'Tell your partner about a small slip you made this week (fictional) in three sentences with ‹ter-› and «Maaf», and let your partner answer «Jangan risau.» / 今週の小さな失敗（架空でよい）について ‹ter-› と «Maaf» を使って3文で話し、パートナーは «Jangan risau.» と答えます。'],
    test_listen=[(1, 'she fell asleep, then missed the bus', ['tertidur', 'terlepas', 'bas']),
                 (3, 'a taxi stuck on a congested road; an accident', ['teksi', 'tersangkut', 'kemalangan']),
                 (5, 'her phone was left at home; the line was cut off', ['telefon', 'tertinggal', 'terputus']),
                 (7, 'she got the day wrong: she thought the meeting was on Thursday', ['tersilap', 'mesyuarat', 'Khamis']),
                 (8, 'her file is in his room; she left it yesterday', ['fail', 'tertinggal', 'semalam']),
                 (9, 'she did not do it on purpose', ['tidak sengaja', 'terlupa', 'fail'])],
    test_listen_prompts=['What happened first, and what happened next?', 'What stopped the taxi?', 'What was left at home, and what happened to the call?',
                         'What did she get wrong?', 'Where is her file, and since when?', 'What does she say about the file?'],
    reading_title='Reading and writing · A clinic reception form',
    reading=['Fictional clinic reception form and a note from the counter (written Malay; all names are invented):',
             '«Nama: Encik Tanaka. Sebab: tergelincir di tangga. Bila: pagi tadi. Tangan: bengkak dan ada luka kecil. Lutut: lebam.»',
             'Note from the counter: «Encik sudah mendaftar. Sila tunggu sekejap.»'],
    read_questions=['What is the form for, and whose name is on it?', 'Why is the person at the clinic?', 'Where did it happen?', 'When did it happen?',
                    'What does the form say about the hand?', 'What does it say about the knee?', 'What does the counter ask him to do?'],
    read_answers=['a form for a person at the clinic counter; Mr Tanaka', 'he slipped («tergelincir»)', 'on the stairs', 'this morning',
                  'it is swollen and has a small wound', 'it is bruised', 'to wait a moment'],
    write_instruction='Write four or five sentences about a small accident (fictional): say what happened, where, when and what you can see or what broke. Do not say what the doctor should do. / '
                      '架空でよいので、小さな事故について4〜5文を書きましょう：何が起きたか、どこで、いつ、見えること、壊れた物を書きます。医者が何をすべきかは書きません。',
    write_model='«Saya tergelincir di tangga pagi tadi. Tangan saya bengkak dan ada luka kecil. Lutut saya pun lebam. Saya sudah mendaftar di klinik. Saya menunggu di sini.»',
    writing_type='message',
    task_title='Task · Locked out at the guardhouse',
    role_a=['Your information (fictional): you live in Block B, unit 12-3. Your key is left inside the flat and the door is locked. You forgot the key by accident.',
            'Tell the guard what happened with «tertinggal» and «terkunci», say «Maaf, saya terlupa.», answer the unit question and ask the guard to contact the management office with «Boleh tolong hubungi …?».',
            'Aの情報（架空）：Bブロック12-3号室に住んでいます。鍵を家の中に置き忘れ、ドアに鍵がかかっています。うっかり鍵を忘れました。'
            '警備員に «tertinggal»・«terkunci» で何が起きたかを言い、«Maaf, saya terlupa.» と言い、部屋番号の質問に答え、«Boleh tolong hubungi …?» で管理事務所への連絡を頼みます。'],
    role_b=['You are B, the guard (fictional). Ask the unit, say you will contact the management office, and say where A should wait.',
            'Then say that the management office is not open yet, and tell A to wait a moment. Answer A\'s apology kindly.',
            'Bは警備員です（架空）。部屋をたずね、管理事務所に連絡すると言い、Aに待つ場所を伝えます。'
            'そのあと、管理事務所がまだ開いていないと言い、Aにしばらく待つように言います。Aの謝罪にはやさしく答えます。'],
    change=['Halfway, B says: «Maaf, pejabat pengurusan belum buka. Encik tunggu sekejap.» A answers politely, asks to wait in the lobby («Boleh saya duduk di lobi?») and says once more that it was not on purpose («Saya tidak sengaja terlupa kunci itu.»).',
            '途中でBが «Maaf, pejabat pengurusan belum buka. Encik tunggu sekejap.» と言います。Aは丁寧に答え、ロビーで待ってよいかをたずね（«Boleh saya duduk di lobi?»）、わざとではなかったことをもう一度言います（«Saya tidak sengaja terlupa kunci itu.»）。'],
    success=['☐ A says what happened with «tertinggal» and «terkunci» and apologises with «Maaf, saya terlupa.».',
             '☐ A gives the unit and asks for the management office with «Boleh tolong hubungi …?»; B asks the unit and says who will contact whom.',
             '☐ After the change A asks to wait in the lobby and says «tidak sengaja»; B answers kindly («Jangan risau.»).'],
    task_key='«Selamat malam. Maaf, kunci saya tertinggal di dalam rumah. Pintu terkunci.» — «Unit berapa, encik?» — «Blok B, unit 12-3. Saya terlupa kunci tadi.» — «Encik tunggu di sini. Saya hubungi pejabat pengurusan.» — '
             '«Baik. Terima kasih banyak.» — Change: «Maaf, pejabat pengurusan belum buka. Encik tunggu sekejap.» — «Boleh saya duduk di lobi? Saya tidak sengaja terlupa kunci itu.» — «Boleh. Jangan risau.»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 16 card notes ms-c16-002 («tertinggal»; not the ter- of «termurah» and «terbaik», chapter 6), -003 («terlupa»), -009 («terkunci» as a state), -010 («tercedera»), -013 («terputus»), '
                    '-015 («tidak sengaja», spoken ‹tak sengaja›); scenario lines ms-c16-s01 to s17 (the locked door, the spilt coffee and the slip); the plan, chapter 16 (superlatives against event and state ter-; apologies depend on '
                    'responsibility and context). The sentence about condominiums, guardhouses and management offices is general knowledge of life in Malaysia, labelled as such and not source-checked.',
    culture_prompt='In Japanese, how do you apologise for a small slip, and which words show it was not on purpose? Which Malay word does the same work, and where does it stand in the sentence?',
    culture_explain=('うっかり〜てしまったと ‹ter-› の違い、責任によって変わる謝り方、一般的な知識の文、日本人学習者が ‹ter-› でつまずく点を読みます。日本語は未監修です。',
                     'Read about うっかり〜てしまった against ‹ter-›, how an apology depends on who is responsible, the general knowledge sentence, and where Japanese learners slip with ‹ter-›.'),
    quiz_words=['L-0619', 'L-0644', 'L-0621', 'L-1237', 'L-1239', 'L-1248'],
    quiz_meanings=['to be left behind by accident', 'to forget (by accident)', 'to miss (a bus)', 'to spill by accident', 'locked (a state)', 'slippery'],
    grammar_quiz=[('Say in Malay: "I left my phone at the office."', '«Saya tertinggal telefon di pejabat.»', ['tertinggal', 'telefon']),
                  ('Say in Malay: "Sorry, I forgot."', '«Maaf, saya terlupa.»', ['maaf', 'terlupa']),
                  ('Say in Malay: "I bumped into the chair by accident."', '«Saya tidak sengaja terlanggar kerusi.»', ['tidak sengaja', 'terlanggar']),
                  ('Say in Malay: "This one is the cheapest, but my wallet is left at home."', '«Yang ini termurah, tetapi dompet saya tertinggal di rumah.»', ['termurah', 'tertinggal'])],
    test_reading=['Fictional clinic form: «Nama: Cik Mei Ling. Sebab: tergelincir di lantai licin. Bila: petang tadi. Tangan: luka kecil. Kaki: bengkak.»'],
    reading_quiz=[('Why is the person at the clinic?', 'she slipped on a slippery floor', ['tergelincir', 'licin']),
                  ('When did it happen?', 'this afternoon', ['petang', 'tadi']),
                  ('What does the form say about the hand?', 'a small wound', ['luka', 'kecil']),
                  ('What does it say about the foot?', 'it is swollen', ['kaki', 'bengkak'])],
    speaking_test='Tell a guard that your door is locked and your key is left inside (fictional): say what happened with «tertinggal» and «terkunci», apologise with «Maaf, saya terlupa.», and ask him to contact the management office with «Boleh tolong hubungi …?».',
    speaking_key='Check: «tertinggal» + the thing + «di» + the place; «terkunci» for the state; «Maaf, saya terlupa.»; «Boleh tolong hubungi …?». '
                 'Accept the spoken ‹tak sengaja› for «tidak sengaja», and a short «Maaf.» as a first try. Do not mark a sentence without «tidak sengaja» wrong.',
    speaking_words=['tertinggal', 'terkunci', 'maaf', 'terlupa', 'kunci'],
    plan={'A_recall': 'chapters 1, 6 and 15 (an apology, «termurah», «hilang») from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first («Saya tertinggal ___ di ___», «Maaf, saya ___»), question and answer before the rule; then the vocabulary in four groups with each ter- word and its root and the root\'s chapter '
                        '(ter- accidents 9, ter- states and results 5, by accident, an accident, the key and the spill 4, what you see 5). Draw the two ter- side by side: «termurah» (the most) against «tertinggal» (by accident).',
          'B_recall': 'say one thing you forgot or left behind with ‹ter-›.',
          'B_drills': 'pattern table, substitution, transformation (the state, the thing as the subject, the two ‹ter-› first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner tells a partner one small slip of this week in two sentences with «Maaf» and a ‹ter-› verb.',
          'D_review': 'cumulative question-word drill (chapters 1 to 16), then the markers drill with new cues and a check of the two ‹ter-› meanings.',
          'D_preview': 'the writing block after chapter 16 (a brief factual incident message), then unit 17 (standard and spoken choices, particles, invitations and refusals; Kata-Kata c17).',
          'E_recall': 'say three sentences: one «tertinggal», one «Maaf, saya …» and one «Pintu terkunci.»',
          'E_listening': 'read the Kata-Kata scenario lines ms-c16-s01 to ms-c16-s17 (the locked door, the spilt coffee, then the clinic) twice; '
                         'learners tick «tertinggal», «terlupa», «terlepas», «tersangkut», «tertumpah», «tergelincir» and «tidak sengaja» when they hear them, and listen for «Jangan risau.» in lines 7 and 9.',
          'E_roleplay': 'pairs play the guardhouse scene with their own unit and key, without the script; then swap and play a spill with a colleague. Do not role-play any medical advice: the clinic part stops at the receptionist\'s «Sila tunggu sekejap.»',
          'E_variation': 'a changed fact: the management office is not open yet; A asks to wait in the lobby and says «tidak sengaja» once more.'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 16 to the guardhouse, lost-wallet and clinic-visit scenes, and offers a missed-bus scene as optional recycling. '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: the writing block after chapter 16 (a brief factual incident message), then unit 17 (Kata-Kata c17).',
    teacher_notes=['Load: 23 core words in four groups (ter- accidents 9, ter- states and results 5, by accident, an accident, the key and the spill 4, what you see 5), no recognition word, and revision of the chapter 6 ter-, sorry and the reply, things and places, moving about and time, and office and clinic. '
                   'Suggested order: Block A the first two groups with patterns 1 and 2; Block B the last two groups with patterns 3 to 5. '
                   'If the pilot shows 23 is too many, the natural cut is: «tertinggal», «terlupa», «terlepas», «tertumpah», «terkunci», «tidak sengaja», «kunci», «bengkak», «luka», «lebam» first; the rest second.',
                   'ter- accident against ter- superlative: ‹ter-› + an adjective (chapter 6: «termurah», «terbesar», «terbaik») means "the most"; ‹ter-› + a verb (this chapter: «tertinggal», «terlupa», «terlepas») means "by accident, without meaning to". '
                   'The Kata-Kata cards for this chapter say it on the first card: not the ‹ter-› of «termurah» and «terbaik». Teach the two side by side with «Yang ini termurah, tetapi dompet saya tertinggal di rumah.» '
                   'Do not tell learners to guess the meaning of any other ‹ter-› word from the prefix: the plan says to learn each form as a word. Ability and idiom readings of ‹ter-› are outside this chapter.',
                   '«tertinggal» (left behind) against «hilang» (lost, chapter 15): «Dompet saya hilang.» means you cannot find the wallet; «Saya tertinggal dompet di rumah.» means you know where it is and you did not mean to leave it. '
                   'The chapter 15 unit used «hilang» and only named ‹tertinggal›; from here learners choose between them by one question: "do I know where it is?"',
                   'Apologising in Malay against Japanese うっかり〜てしまいました: Japanese marks the slip twice (うっかり, 〜てしまう). Malay marks it once, in the verb: «Maaf, saya terlupa.» is the whole apology, and the answer is «Jangan risau.» '
                   'Do not ask for a longer apology for a small slip, and do not teach a formula for blame: if it is not your fault, state what happened («Pintu terkunci.», «Talian terputus.») and make the request.',
                   '«terkunci» as a state, not an action: «Pintu terkunci.» means the door is locked now; nobody is locking it. «terputus», «tercedera» and «terbakar» are the same: a state that lasts. '
                   'The Japanese 〜ている feeling is close («鍵がかかっている», «切れている», «けがをしている»), while «terlupa» and «terlepas» feel like 〜てしまった. A state can take «masih» («Pintu itu masih terkunci.»); an accident takes «baru» or «sudah».',
                   '«tidak sengaja» with a ter- verb adds emphasis, and does not change the meaning: «Saya tidak sengaja terlanggar kerusi.» The spoken form is ‹tak sengaja›. Do not mark a ter- sentence without it wrong. '
                   '«Awak tidak sengaja.» is also what you say to someone else who did something small (Kata-Kata s09).',
                   'Whole words and roots: each ter- word is learned whole, with its root as the card note gives it: «tertinggal» (ter- + «tinggal», chapter 2), «terlupa» («lupa», chapter 4), «tertidur» («tidur», chapter 4), «terlepas» («lepas», chapter 4), '
                   '«tertumpah» («tumpah», this chapter), «terkunci» («kunci», this chapter); ‹jatuh›, ‹silap›, ‹langgar›, ‹gelincir›, ‹cedera›, ‹bakar›, ‹putus› and ‹sangkut› are not class cards. «kemalangan» is a whole word (‹ke-an› words come in Stage 3; the root ‹malang› is not taught alone); '
                   'Malaysian Malay says «kemalangan», not the Indonesian word.',
                   'The clinic scene (safety): learners say only what they can see: «bengkak», «luka kecil», «lebam». The receptionist registers Mr Tanaka («Encik perlu daftar dulu. Ini borang.») and asks him to wait («Sila tunggu sekejap.»). '
                   'The unit gives no diagnosis, no treatment advice and no medicine, and learners must not be asked to name a cause or a remedy. If a learner asks what to do for an injury, say that it is a question for the doctor.',
                   'The ‹-kan› and bare-root rules from chapters 12 to 15 still hold: a dialogue line may keep Kata-Kata\'s everyday bare root («Saya hubungi pejabat pengurusan.», «Encik perlu daftar dulu.»), and the pattern examples, keys and written forms '
                   'use the meN- form («menunggu», «mendaftar», «menghubungi»). A request takes the plain root («Boleh tolong hubungi …?»). «tangguhkan» and «batalkan» take a noun object («tangguhkan rancangan»); this unit does not use them. '
                   '«dari» is for places and «daripada» for people and organisations.',
                   'Where Japanese learners usually slip: (1) «hilang» for something left behind; (2) ‹ter-› on an adjective to mean "too" or "very"; (3) reading «terbesar» as accidental; (4) an apology that is too long for a small slip; (5) putting a doer into a state sentence («Saya terkunci» means "I am locked in"); '
                   '(6) «tidak sengaja» without a verb («Saya tidak sengaja kunci»).',
                   'Natural speech: «Maaf, saya terlupa.» and «Jangan risau.»; «Pintu terkunci.»; «Hati-hati, lantai licin.»; «Awak tidak sengaja.»; the spoken ‹tak sengaja›. The scene follows Kata-Kata c16 (scenario lines ms-c16-s01 to s17, frames f01 to f06); '
                   'turn 11 of the model joins s11 and s12, the move from the office to the clinic the next morning. All names, units and times are fictional; learners may use an invented flat or an invented cup.',
                   'Cumulative question words: chapters 1 to 16. Chapter 16 adds no new question word.'],
)

EXTRA = dict(
    slug='writing-block', type='Reading and writing', sub_type='composition', kind='writing',
    title='Writing block · A brief factual incident message',
    goal='I can write a short factual message about a small incident: what happened, where, when, what I can see, and one practical request, in four to six sentences, with no blame and no advice.',
    grammar=['ms-c16-g02', 'ms-c16-g03', 'ms-c16-g04', 'ms-c16-g05', 'ms-c16-g07'],
    patterns=['ms-c16-f01', 'ms-c16-f02', 'ms-c16-f03', 'ms-c16-f06'],
    model=['Fictional model: two short factual messages about small incidents, one to the management office (a key left inside) and one to a colleague (a spill). All names and units are invented:',
           '«Selamat petang. Saya Mei Ling dari Blok B, unit 12-3. Kunci saya tertinggal di dalam rumah dan pintu terkunci. Saya tidak sengaja terlupa kunci tadi. Boleh tolong hubungi pengawal? Saya menunggu di lobi. Terima kasih.»',
           '«Encik Tanaka, maaf. Air kopi saya tertumpah di meja dan cawan saya pecah. Saya tidak sengaja. Lantai licin. Boleh tolong ambil tisu? Terima kasih.»',
           'Notice: who and where first, then what happened with a ‹ter-› verb, then «tidak sengaja» if it matters, then one request with «Boleh tolong». The message states facts; it does not blame anyone and gives no advice. / '
           '気づくこと：まずだれがどこで、次に ‹ter-› の動詞で何が起きたか、必要なら «tidak sengaja»、最後に «Boleh tolong» で頼みを一つ書きます。事実だけを書き、だれも責めず、助言もしません。'],
    plan=['0–5 Recall: say one thing you left behind with «tertinggal» and one «Maaf, saya …» (unit 16).',
          '5–15 Model and notice: read the two messages; underline every ‹ter-› verb and say which is an action and which is a state; rewrite «Pintu terkunci» as «Saya terlupa kunci» and say how the meaning changes.',
          '15–30 Guided draft: write your own message about a small incident (a key, a spill, a missed bus) with the checklist below.',
          '30–40 Peer or teacher feedback with the peer check.',
          '40–45 Rewrite one sentence to remove any blame or advice, and read the message aloud.',
          '0–5 復習・5–15 例文を読んで気づく・15–30 下書き・30–40 ペアまたは先生の確認・40–45 一文を書き直して音読。'],
    task=['Write four to six sentences: a message to the management office or to a colleague about a small incident (fictional). Include:',
          '☐ who you are and where («Saya …, Blok B, unit …»)',
          '☐ what happened, with a ‹ter-› verb or state («tertinggal», «terkunci», «tertumpah», «tergelincir», «pecah»)',
          '☐ «tidak sengaja» if you want to say it was not on purpose, and one thing you can see («bengkak», «luka kecil», «lebam», «licin»)',
          '☐ one practical request with «Boleh tolong …?», and «Terima kasih.»',
          '________________________________________', '________________________________________',
          '________________________________________', '________________________________________',
          '小さな出来事について、管理事務所か同僚あての短い事実のメッセージを4〜6文で書きましょう。だれがどこで、何が起きたか、見えること、頼みを一つ入れます。'
          '名前・部屋・場所は架空でかまいません。医者の診断や助言は書きません。'],
    check=['☐ The message says what happened with a ‹ter-› verb or a state, and does not use «hilang» for something left behind.',
           '☐ «tidak sengaja» stands in front of the ‹ter-› verb, or the message does without it.',
           '☐ It states facts only: no blame, no guess about a cause, no advice; an injury is described only by what you can see.',
           '☐ One request with «Boleh tolong …?» and the plain root after «tolong»; the partner can say what is asked of whom.',
           '☐ 事実だけか、責めていないか、頼みが一つか、«hilang» と «tertinggal» の使い分けを確認し、パートナーが質問を一つします。'],
    answer='Any four to six correct sentences that cover the checklist. Model: «Selamat petang. Saya Mei Ling dari Blok B, unit 12-3. Kunci saya tertinggal di dalam rumah dan pintu terkunci. '
           'Saya tidak sengaja terlupa kunci tadi. Boleh tolong hubungi pengawal? Saya menunggu di lobi. Terima kasih.»',
    key_extra=['Mark for the task first (who and where, what happened, a request), then for form (the ‹ter-› verb, «tidak sengaja» in front of it, «tertinggal» against «hilang», the plain root after «tolong»). '
               'Accept a short «Maaf.» in a first draft but ask for the ‹ter-› verb once in the rewrite; accept the everyday bare root in a first draft («Saya hubungi pengawal») but ask for the written form in the message.',
               'Names, units and places are fictional. Do not ask anyone to share a real address, flat number or phone number. Do not mark or comment on any medical content: the message may only say what is visible («bengkak», «luka kecil», «lebam»).'],
    explain=('ユニット16のあとの書く練習（45分）：小さな出来事を、だれがどこで・何が起きたか・見えること・頼みを一つ入れて4〜6文の事実のメッセージに書きます。責めたり助言したりしません。名前や部屋は架空でかまいません。',
             'The writing block after unit 16 (45 minutes): write a brief factual incident message in four to six sentences with who and where, what happened with a ‹ter-› verb, what you can see and one request; no blame and no advice; names and units may be invented.'),
)

CFG['extra'] = EXTRA
UNIT = unit_dict(CFG)
