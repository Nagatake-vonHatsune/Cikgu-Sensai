"""Unit 12B: -i and more -kan verbs: reporting a leak and asking for a repair (Boleh ___ juruteknik?; Juruteknik sedang ___ paip;
Ada kebocoran di ___ saya; Tolong ___ lampu itu).

25 core ledger entries, the rows the ledger places in "Ch12 (unit 12B)" (L-1173 to L-1184, L-1281 «melaporkan», L-1282 «salinan», L-1283 «dihubungi» and L-1284 «dibaiki», approved by Sam on 14 Nov 2026, and the existing rows L-0649 «siling»,
L-0651 «kebocoran», L-0652 «juruteknik», L-0655 «slot», L-0661 «paip», L-0665 «kontraktor», L-0698 «ganti», L-0789 «menghubungi» and
L-0871 «perlahankan»), in three groups. Each -kan or -i verb is taught as a whole ledger form, with its root, the chapter of the
root and what the suffix adds (-i: to or at a person or place; -kan: do it for someone or make it happen), as the Kata-Kata chapter
12 card notes give them. The ke-an and -an words («kebocoran», «kerosakan», «aduan», «tempahan») are whole words. The scene follows
Kata-Kata c12 (scenario lines ms-c12-s11 to s19: reporting a ceiling leak to the management office) and goes further in class:
a second report, a booked slot and a changed time. All names, blocks, units and times are fictional. No recognition word (no Dunia
scene primes chapter 12). Japanese is a draft awaiting native review.
"""
from .chapter10_common import unit_dict

LEAK = ['L-0651', 'L-0649', 'L-0661', 'L-1182', 'L-1183', 'L-0652', 'L-0665', 'L-0655', 'L-1281', 'L-1282']
REPAIR = ['L-1173', 'L-1174', 'L-1175', 'L-0789', 'L-0698', 'L-1184', 'L-1176', 'L-1283', 'L-1284']
SWITCH = ['L-1177', 'L-1178', 'L-1179', 'L-1180', 'L-1181', 'L-0871']
CORE = LEAK + REPAIR + SWITCH

# Revision: words placed in chapters 1 to 11 that the unit really uses (a test fails if one is not used).
REV_ROOTS = ['L-0013', 'L-0420', 'L-0099', 'L-0292', 'L-0287', 'L-0588']
REV_HOME = ['L-0569', 'L-0570', 'L-0555', 'L-0259', 'L-0571', 'L-0566', 'L-0456', 'L-0419']
REV_ASK = ['L-0375', 'L-0076', 'L-0401', 'L-0026', 'L-0023', 'L-0291', 'L-0248', 'L-0313', 'L-1139', 'L-1155']
REV_TIME = ['L-0193', 'L-0194', 'L-0189', 'L-0192', 'L-0161', 'L-1007', 'L-0157']

EXAMPLES = {
    # The leak and the report
    'L-0651': '«Ada kebocoran di siling saya.»',
    'L-1281': '«Saya melaporkan kebocoran itu kepada pengurus.»',
    'L-1282': '«Tolong simpankan salinan borang itu.»',
    'L-1283': '«Juruteknik sudah dihubungi.»',
    'L-1284': '«Paip itu sudah dibaiki.»',
    'L-0649': '«Air turun dari siling.»',
    'L-0661': '«Juruteknik sedang membaiki paip.»',
    'L-1182': '«Ada kerosakan di paip dapur saya.»',
    'L-1183': '«Saya isi borang aduan sekarang.»',
    'L-0652': '«Boleh hubungi juruteknik?»',
    'L-0665': '«Kami akan menghubungi kontraktor.»',
    'L-0655': '«Ada slot petang ini, pukul tiga.»',
    # Repair and contact
    'L-1173': '«Tolong baiki paip ini.» (same spelling as «baik», a different meaning)',
    'L-1174': '«Juruteknik sedang membaiki paip.»',
    'L-1175': '«Boleh hubungi juruteknik?» (everyday on notices: «Sila hubungi pejabat pengurusan.»)',
    'L-0789': '«Kami akan menghubungi juruteknik.»',
    'L-0698': '«Tolong ganti lampu itu.» (also «gantikan»; for a plan: «Kontraktor akan menukar paip itu.»)',
    'L-1184': '«Tolong gantikan lampu itu.»',
    'L-1176': '«Tempahan slot juruteknik ada di pejabat pengurusan.»',
    # Switch, empty, clean
    'L-1177': '«Tolong isikan borang ini.» (everyday: «Sila isi borang ini.»)',
    'L-1178': '«Tolong kosongkan meja itu.»',
    'L-1179': '«Tolong hidupkan lampu itu.» (everyday: «Tolong buka lampu itu.»)',
    'L-1180': '«Tolong matikan lampu itu dulu.» (everyday: «Tolong tutup lampu itu.»)',
    'L-1181': '«Tolong bersihkan lantai itu.»',
    'L-0871': '«Tolong perlahankan muzik itu.»',
    # Revision · roots
    'L-0013': '«baik» → «baiki»: «Baik, saya baiki sekarang.»',
    'L-0420': '«isi» → «isikan»: «Sila isi borang aduan.»',
    'L-0099': '«kosong» → «kosongkan»: «Lantai itu kosong.»',
    'L-0292': '«bersih» → «bersihkan»: «Lantai itu bersih.»',
    'L-0287': '«perlahan» → «perlahankan»: «Tolong bercakap perlahan.»',
    'L-0588': '«rosak» → «kerosakan»: «Lampu itu rosak.»',
    # Revision · the home
    'L-0569': '«Tolong matikan lampu itu dulu.»',
    'L-0570': '«Tolong matikan kipas itu.»',
    'L-0555': '«Ada kebocoran di siling bilik air saya.»',
    'L-0259': '«Air turun dari siling atau dari paip?»',
    'L-0571': '«Lantai itu basah.»',
    'L-0566': '«Tolong bukakan tingkap itu.»',
    'L-0456': '«Paip dapur saya rosak.»',
    'L-0419': '«Saya isi borang aduan sekarang.»',
    # Revision · asking, feelings and place
    'L-0375': '«Tolong matikan lampu itu dulu.»',
    'L-0076': '«Boleh hubungi juruteknik?»',
    'L-0401': '«Sila hubungi pejabat pengurusan.»',
    'L-0026': '«Tolong hubungi pemilik unit itu nanti.»',
    'L-0023': '«Tolong matikan lampu itu dulu.»',
    'L-0291': '«Muzik itu bising.»',
    'L-0248': '«Saya takut lampu itu rosak.»',
    'L-0313': '«Dari siling, dekat lampu.»',
    'L-1139': '«Juruteknik akan melihat siling itu.»',
    'L-1155': '«Saya akan menelefon pejabat pengurusan.»',
    # Revision · time and markers
    'L-0193': '«Saya sudah menghubungi juruteknik.»',
    'L-0194': '«Juruteknik belum membaiki paip itu.»',
    'L-0189': '«Juruteknik sedang membaiki paip.»',
    'L-0192': '«Kami akan menghubungi juruteknik.»',
    'L-0161': '«Saya matikan lampu itu sekarang.»',
    'L-1007': '«Bila juruteknik boleh datang?»',
    'L-0157': '«Juruteknik datang pukul tiga.»',
}

# (root, where, where_ja, what the suffix adds in English, in Japanese). The root as the Kata-Kata card note gives it.
ROOTS = {
    'L-1173': ('«baik»', 'chapter 1', '第1章', '‹-i›: repair, to put right; same spelling as «baik» (good), different meaning', '‹-i›：修理する・直す；«baik»（良い）と同じつづりで意味が違う'),
    'L-1174': ('«baiki»', 'this chapter', '本章', '‹meN-› + «baiki»: ‹mem-› before b; to repair', '‹meN-› ＋ «baiki»：b の前は ‹mem-›；修理する'),
    'L-1175': ('‹hubung›', None, None, '‹-i›: contact a person; the person follows the verb directly', '‹-i›：人に連絡する；人は動詞のすぐあとに置く'),
    'L-0789': ('«hubungi»', 'this chapter', '本章', '‹meN-› + «hubungi»: ‹meng-› before h; to contact', '‹meN-› ＋ «hubungi»：h の前は ‹meng-›；連絡する'),
    'L-0698': ('«ganti»', 'this chapter', '本章', 'the root itself: to replace, to stand in for someone', '語根そのもの：取り替える・代わる'),
    'L-1184': ('«ganti»', 'this chapter', '本章', '‹-kan›: replace something', '‹-kan›：何かを取り替える'),
    'L-1177': ('«isi»', 'Dunia, chapter 3', 'Dunia・第3章', '‹-kan›: fill in, put in; everyday «isi»', '‹-kan›：記入する・入れる；日常は «isi»'),
    'L-1178': ('«kosong»', 'chapter 3', '第3章', '‹-kan›: make empty, clear', '‹-kan›：空にする'),
    'L-1179': ('‹hidup›', None, None, '‹-kan›: switch on; everyday «buka» for lights and aircon', '‹-kan›：つける；照明やエアコンの日常語は «buka»'),
    'L-1180': ('‹mati›', None, None, '‹-kan›: switch off; everyday «tutup» for lights and aircon', '‹-kan›：消す；照明やエアコンの日常語は «tutup»'),
    'L-1181': ('«bersih»', 'chapter 6', '第6章', '‹-kan›: make clean; «bersih» + ‹-kan›, not ‹ber-› + ‹sih›', '‹-kan›：きれいにする；«bersih» ＋ ‹-kan› で、‹ber-› ＋ ‹sih› ではない'),
    'L-0871': ('«perlahan»', 'chapter 6', '第6章', '‹-kan›: make slower or quieter', '‹-kan›：ゆっくり・小さくする'),
}
_EN = {'L-1173': 'repair (a request)', 'L-1174': 'to repair', 'L-1175': 'contact (a request)', 'L-0789': 'to contact',
       'L-0698': 'to replace; to stand in for someone', 'L-1184': 'replace (a request)', 'L-1177': 'fill in, put in (a request; «isi» alone is more common in speech)',
       'L-1178': 'empty, clear (a request)', 'L-1179': 'switch on (a request)', 'L-1180': 'switch off (a request)', 'L-1181': 'clean (a request)',
       'L-0871': 'to lower (the voice), to slow down'}
_JA = {'L-1173': '修理してください', 'L-1174': '修理する', 'L-1175': '連絡してください', 'L-0789': '連絡する', 'L-0698': '取り替える・代わりをする',
       'L-1184': '交換してください', 'L-1177': '記入してください・入れてください（日常は «isi»）', 'L-1178': '空にしてください', 'L-1179': 'つけてください',
       'L-1180': '消してください', 'L-1181': 'きれいにしてください', 'L-0871': '（声を）小さくする・ゆっくりにする'}


def _opts(lid):
    root, where, where_ja, adds, adds_ja = ROOTS[lid]
    if root.startswith('‹'):
        en_root = f'{root} (learn the whole word; the root has no class card of its own)'
        ja_root = f'{root}（一語まるごと覚える）'
    else:
        en_root = f'{root} ({where})'
        ja_root = f'{root}（{where_ja}）'
    return {'en': f'{_EN[lid]} (root {en_root}; {adds})', 'ja': f'{_JA[lid]}（語根 {ja_root}；{adds_ja}）'}


VOCAB_OPTS = {lid: _opts(lid) for lid in ROOTS}
VOCAB_OPTS.update({
    'L-1281': {'en': 'to report something to someone (‹meN-› + ‹lapor› + ‹-kan›: ‹me-› before l; «kepada» for the person, chapter 11)',
               'ja': '（人に）報告する・届け出る（‹meN-› ＋ ‹lapor› ＋ ‹-kan›：l の前は ‹me-›；相手の人は «kepada»、第11章）'},
    'L-1282': {'en': 'a copy (learn the whole word; ‹-an› words come in Stage 3; the root is ‹salin›)',
               'ja': 'コピー・控え（一語まるごと覚える；‹-an› の語は第3段階；語根は ‹salin›）'},
    'L-1283': {'en': 'to be contacted (the «di-» partner of «menghubungi», chapter 9 pattern: «di-» + ‹hubung› + ‹-i›)',
               'ja': '連絡される（«menghubungi» の «di-» の相手、第9章の型：«di-» ＋ ‹hubung› ＋ ‹-i›）'},
    'L-1284': {'en': 'to be repaired (the «di-» partner of «membaiki»: «di-» + «baiki»; «baiki» chapter 12)',
               'ja': '修理される（«membaiki» の «di-» の相手：«di-» ＋ «baiki»）'},
    'L-0651': {'en': 'a leak (learn the whole word; ‹ke-an› words come in Stage 3; the root is ‹bocor›)',
               'ja': '水漏れ（一語まるごと覚える；‹ke-an› の語は第3段階；語根は ‹bocor›）'},
    'L-1182': {'en': 'damage, fault (learn the whole word; the root is «rosak», Dunia, chapter 7)',
               'ja': '故障・破損（一語まるごと覚える；語根は «rosak»、Dunia・第7章）'},
    'L-1183': {'en': 'complaint, problem report (learn the whole word; the root is ‹adu›)',
               'ja': '苦情・問題の報告（一語まるごと覚える；語根は ‹adu›）'},
    'L-1176': {'en': 'booking, reservation (learn the whole word; the root is «tempah», Dunia, chapter 4)',
               'ja': '予約（一語まるごと覚える；語根は «tempah»、Dunia・第4章）'},
})

P = [
    ('ms-c12-f05', '«Boleh» ___ «juruteknik?»  (‹-i›: to a person)', [
        'A: «Boleh hubungi juruteknik?» B: «Boleh. Saya hubungi sekarang.»',
        'A: «Boleh hubungi pejabat pengurusan?» B: «Boleh. Nombor telefon ada di sini.»',
        'A: «Juruteknik sudah dihubungi?» B: «Sudah. Juruteknik sudah dihubungi.»',
        'A: «Tolong hubungi saya sebelum juruteknik sampai.» B: «Baik. Saya hubungi encik.»',
        'A: «Awak sudah menghubungi pemilik unit itu?» B: «Belum. Saya akan menelefon dia petang ini.»',
        'A: «Kami akan menghubungi juruteknik.» B: «Terima kasih. Bila juruteknik boleh datang?»'],
     "‹-i› goes on the end of a root and points the action at a person or a place: «hubungi» is ‹hubung› + ‹-i›, and it means to get in touch with someone. "
     "The person follows the verb directly, with no little word between them: «Boleh hubungi juruteknik?» (the Kata-Kata frame), not a word like «dengan» before the person. "
     "On notices you read «Sila hubungi pejabat pengurusan.» With ‹meN-› in front, «hubungi» becomes «menghubungi» (‹meng-› before h): «Kami akan menghubungi juruteknik.» "
     "Choose the form by the sentence: after «Tolong», «Boleh» or «Sila», and in a first-person reply («Saya hubungi sekarang.»), use «hubungi»; after a doer such as «kami» or «pejabat pengurusan», or after «sudah», «belum», «sedang» or «akan», use «menghubungi». "
     "This is the same rule as for the ‹-kan› verbs. «menelefon» (chapter 11) means to phone, and «hubungi» does not say how you get in touch. The suffix ‹-i› does not mean the same as ‹-kan›: ‹-i› is to or at a person or place, ‹-kan› is for someone or to make it happen.",
     "‹-i› は語根の終わりに付いて、動作を人や場所に向けます：«hubungi» は ‹hubung› ＋ ‹-i› で、誰かと連絡を取るという意味です。人は動詞のすぐあとに置き、間に小さな語は入りません："
     "«Boleh hubungi juruteknik?»（Kata-Kata の文型）。「に」にあたる語は入りません。掲示では «Sila hubungi pejabat pengurusan.» と読みます。前に ‹meN-› が付くと "
     "«hubungi» は «menghubungi»（h の前は ‹meng-›）になります：«Kami akan menghubungi juruteknik.» 使い分けは文で決まります：«Tolong»・«Boleh»・«Sila» のあと、また一人称の返事（«Saya hubungi sekarang.»）では «hubungi»、"
     "«kami» や «pejabat pengurusan» のような動作主のあと、また «sudah»・«belum»・«sedang»・«akan» のあとでは «menghubungi» を使います。‹-kan› の動詞と同じ規則です。«menelefon»（第11章）は電話をかけることで、"
     "«hubungi» は連絡の手段を言いません。‹-i› と ‹-kan› は同じではありません：‹-i› は人や場所へ向かう動作、‹-kan› は誰かのため・そうなるようにする動作です。",
     'Japanese 連絡する takes に: 技術者に連絡する. Malay has no に-word after «hubungi»: the person follows the verb directly. Do not add ‹kepada› or «dengan».',
     '日本語の「連絡する」は「技術者に連絡する」のように「に」を取ります。マレー語の «hubungi» のあとには「に」にあたる語がなく、人は動詞のすぐあとに来ます。‹kepada› や «dengan» を足さないでください。'),
    ('ms-c12-f04', '«Juruteknik sedang» ___ «paip.»  (‹meN-› + ‹-i›: is repairing)', [
        'A: «Juruteknik sedang membaiki paip.» B: «Paip yang mana?»',
        'A: «Juruteknik sedang membaiki apa?» B: «Dia sedang membaiki paip bilik air saya.»',
        'A: «Paip itu sudah dibaiki?» B: «Sudah. Paip itu sudah dibaiki oleh juruteknik.»',
        'A: «Tolong baiki paip ini.» B: «Baik. Saya baiki sekarang.»',
        'A: «Kontraktor sudah membaiki siling itu?» B: «Belum. Kontraktor akan membaiki siling itu esok.»',
        'A: «Bila juruteknik boleh membaiki paip itu?» B: «Ada slot petang ini, pukul tiga.»'],
     "«baiki» is «baik» + ‹-i›. It looks like «baik» (good) but means to repair. With ‹meN-› in front, ‹mem-› before b gives «membaiki»: «Juruteknik sedang membaiki paip.» "
     "(the Kata-Kata frame). «sedang» goes in front of the verb, as in chapter 11. A request uses the root form: «Tolong baiki paip ini.» This course uses «baiki» and «membaiki» "
     "for a repair in Malaysian Malay. «Gantikan» («ganti» + ‹-kan›) means to replace something: «Tolong gantikan lampu itu.», and «ganti» alone means to replace or to stand in for someone. "
     "Notice that the doer comes first and the thing follows the verb: «Juruteknik membaiki paip.»",
     "«baiki» は «baik» ＋ ‹-i› です。«baik»（良い）に似ていますが、修理するという意味です。前に ‹meN-› が付き、b の前は ‹mem-› なので «membaiki» になります："
     "«Juruteknik sedang membaiki paip.»（Kata-Kata の文型）。«sedang» は第11章と同じく動詞の前に置きます。依頼は語根の形です：«Tolong baiki paip ini.» このコースでは、"
     "マレーシアのマレー語として «baiki»・«membaiki» を使います。«Gantikan»（«ganti» ＋ ‹-kan›）は何かを取り替えることで、«Tolong gantikan lampu itu.»、«ganti» だけなら取り替える・誰かの代わりをするです。"
     "動作主が先で、物は動詞のすぐあとに来ることに注意：«Juruteknik membaiki paip.»",
     'Japanese 直す and 修理する both fit «membaiki». But 直す also covers correcting a mistake, and Malay does not use «baiki» for that. Do not mix it up with «baik» (good).',
     '日本語の「直す」「修理する」はどちらも «membaiki» にあたります。ただし「直す」は間違いを直す意味でも使いますが、マレー語ではその意味に «baiki» は使いません。«baik»（良い）と混同しないでください。'),
    ('ms-c12-f06', '«Ada kebocoran di» ___ «saya.»  (reporting a problem)', [
        'A: «Ada kebocoran di siling saya.» B: «Siling bilik air atau siling dapur?»',
        'A: «Ada kebocoran di siling bilik air saya.» B: «Air turun dari siling atau dari paip?»',
        'A: «Ada kerosakan di paip dapur saya.» B: «Kami akan menghubungi juruteknik.»',
        'A: «Saya Tanaka, Blok B, unit 12-3.» B: «Selamat pagi, Encik Tanaka. Apa aduan encik?»',
        'A: «Encik sudah melaporkan kebocoran itu?» B: «Sudah. Saya melaporkan kebocoran itu kepada pengurus.»',
        'A: «Bila juruteknik boleh datang?» B: «Ada slot petang ini, pukul tiga. Boleh?»'],
     "To report a problem in your own home, say what is wrong and where: «Ada kebocoran di siling saya.» (the Kata-Kata frame). «kebocoran» (a leak) and «kerosakan» (damage, a fault) "
     "are learned as whole words, as are «aduan» (a complaint or problem report) and «tempahan» (a booking). Start the call with your name, block and unit, as «Encik» Tanaka does. "
     "The office answers with a question and then a request: «Tolong matikan lampu itu dulu.» and gives you a «slot» with the technician («juruteknik») or the contractor («kontraktor»). "
     "Say the place after «di»: «di siling bilik air saya», «di paip dapur saya».",
     "自分の家の問題を伝えるときは、何がどこでおかしいかを言います：«Ada kebocoran di siling saya.»（Kata-Kata の文型）。«kebocoran»（水漏れ）と «kerosakan»（故障・破損）は一語として覚え、"
     "«aduan»（苦情・問題の報告）と «tempahan»（予約）も同じです。田中さんのように、まず名前・棟・部屋番号を言って電話を始めます。事務所は質問のあとに依頼で答えます："
     "«Tolong matikan lampu itu dulu.» そして技術者（«juruteknik»）か業者（«kontraktor»）の «slot» を教えてくれます。場所は «di» のあとに言います："
     "«di siling bilik air saya»、«di paip dapur saya»。",
     'Japanese 〜が漏れています uses the verb 漏れる. Malay says «Ada kebocoran» (there is a leak), with «ada» and a noun, and «di» for the place. Do not look for a verb meaning to leak.',
     '日本語の「水漏れしています」は動詞を使いますが、マレー語は «Ada kebocoran»（水漏れがある）のように «ada» と名詞を使い、場所は «di» で言います。漏れるという動詞を探さないでください。'),
    ('ms-c12-f01', '«Tolong» ___ «lampu itu.»  (‹-kan› again: switch, clean, fill, replace)', [
        'A: «Tolong matikan lampu itu dulu.» B: «Baik, saya matikan sekarang.»',
        'A: «Tolong hidupkan kipas itu.» B: «Baik. Saya hidupkan kipas sekarang.»',
        'A: «Tolong bersihkan lantai itu.» B: «Baik. Lantai itu basah. Saya bersihkan sekarang.»',
        'A: «Tolong kosongkan meja itu dan bukakan tingkap.» B: «Baik, saya kosongkan dulu.»',
        'A: «Tolong isikan borang aduan ini.» B: «Baik. Saya isi sekarang.»',
        'A: «Tolong perlahankan muzik itu.» B: «Maaf. Saya perlahankan sekarang.»'],
     "These are the ‹-kan› verbs of 12A again, now for things in the home: «matikan» (switch off), «hidupkan» (switch on), «bersihkan» (clean), «kosongkan» (empty), "
     "«isikan» (fill in) and «perlahankan» (lower, slow down). Each is a root with ‹-kan›: ‹mati› + ‹-kan›, ‹hidup› + ‹-kan›, «bersih» (chapter 6) + ‹-kan› (it is «bersih» + ‹-kan›, "
     "not ‹ber-› + ‹sih›), «kosong» (chapter 3) + ‹-kan›, «isi» (Dunia, chapter 3) + ‹-kan›, «perlahan» (chapter 6) + ‹-kan›. "
     "Everyday speech: «tutup lampu» for «matikan lampu» and «buka lampu» for «hidupkan lampu» (also for the aircon); «Sila isi borang ini» for «isikan». "
     "Both forms are correct; teach the ‹-kan› form first and recognise the everyday one.",
     "12A の ‹-kan› の動詞が、今度は家の中の物に使われます：«matikan»（消す）、«hidupkan»（つける）、«bersihkan»（きれいにする）、«kosongkan»（空にする）、«isikan»（記入する）、"
     "«perlahankan»（小さくする・ゆっくりにする）。どれも語根に ‹-kan› が付いた形です：‹mati› ＋ ‹-kan›、‹hidup› ＋ ‹-kan›、«bersih»（第6章）＋ ‹-kan›（«bersih» ＋ ‹-kan› で、‹ber-› ＋ ‹sih› ではありません）、"
     "«kosong»（第3章）＋ ‹-kan›、«isi»（Dunia・第3章）＋ ‹-kan›、«perlahan»（第6章）＋ ‹-kan›。日常会話では «matikan lampu» の代わりに «tutup lampu»、«hidupkan lampu» の代わりに "
     "«buka lampu»（エアコンも同じ）、«isikan» の代わりに «Sila isi borang ini» と言います。どちらも正しいので、‹-kan› の形を先に教え、日常の形は聞いて分かるようにします。",
     'Japanese uses one verb for each: 消す, つける, 掃除する. In Malay the suffix does the work: «matikan» is "make it dead", «hidupkan» is "make it alive". The meaning of ‹-kan› here is cause: you make something happen.',
     '日本語では「消す」「つける」「掃除する」とそれぞれ別の動詞を使います。マレー語では接尾辞が働きます：«matikan» は「死んだ状態にする」、«hidupkan» は「生きた状態にする」です。ここでの ‹-kan› の意味は「そうなるようにする」です。'),
]

# Kata-Kata scenario lines ms-c12-s11 to s19, extended to 11 turns.
DIALOGUE = [
    ('Tanaka', 'Selamat pagi. Saya Tanaka, Blok B, unit 12-3. Ada kebocoran di siling bilik air saya.'),
    ('Office', 'Selamat pagi, Encik Tanaka. Air turun dari siling atau dari paip?'),
    ('Tanaka', 'Dari siling, dekat lampu. Saya takut lampu itu rosak.'),
    ('Office', 'Tolong matikan lampu itu dulu. Kami akan menghubungi juruteknik.'),
    ('Tanaka', 'Baik, saya matikan lampu itu sekarang. Bila juruteknik boleh datang?'),
    ('Office', 'Ada slot petang ini, pukul tiga. Boleh?'),
    ('Tanaka', 'Boleh. Tolong hubungi saya sebelum juruteknik sampai.'),
    ('Office', 'Baik. Juruteknik akan melihat siling itu. Saya isi borang aduan sekarang.'),
    ('Tanaka', 'Boleh saya kosongkan meja dan kerusi di bawah siling itu?'),
    ('Office', 'Boleh, encik. Terima kasih.'),
    ('Tanaka', 'Terima kasih. Saya tunggu di rumah.'),
]
VARIANT = [
    ('Siti', 'Selamat petang. Saya Puan Siti, Blok A, unit 8-1. Ada kerosakan di paip dapur saya.'),
    ('Office', 'Selamat petang, puan. Air keluar dari paip atau dari bawah?'),
    ('Siti', 'Dari bawah. Lantai dapur basah.'),
    ('Office', 'Tolong matikan air dulu. Kami akan menghubungi kontraktor.'),
    ('Siti', 'Baik. Bila kontraktor boleh membaiki paip itu?'),
    ('Office', 'Ada slot esok pagi, pukul sepuluh. Boleh?'),
    ('Siti', 'Boleh. Tolong hubungi saya sebelum kontraktor sampai.'),
    ('Office', 'Baik, puan. Saya isi borang aduan sekarang.'),
    ('Siti', 'Terima kasih. Saya bersihkan lantai dapur dulu.'),
    ('Office', 'Baik, puan. Terima kasih.'),
]
LISTENING = [
    ('Mei Ling', 'Selamat pagi. Saya Mei Ling, Blok C, unit 5-2. Ada kebocoran di paip bilik air saya.'),
    ('Office', 'Selamat pagi, cik. Bila kebocoran itu bermula?'),
    ('Mei Ling', 'Malam tadi. Air banyak di lantai.'),
    ('Office', 'Tolong matikan kipas dan lampu dulu. Kami akan menghubungi juruteknik.'),
    ('Mei Ling', 'Baik, saya matikan sekarang. Bila juruteknik boleh datang?'),
    ('Office', 'Ada dua slot, petang ini pukul empat atau esok pagi.'),
    ('Mei Ling', 'Petang ini, pukul empat. Tolong hubungi saya sebelum juruteknik sampai.'),
    ('Office', 'Baik. Juruteknik akan membaiki paip itu. Kalau paip itu rosak, juruteknik akan menukar paip itu.'),
    ('Mei Ling', 'Satu lagi. Tolong perlahankan muzik di unit sebelah. Bising sangat.'),
    ('Office', 'Baik, cik. Saya hubungi jiran cik itu. Tolong bersihkan lantai dulu, ya?'),
    ('Office', 'Satu lagi, cik. Tolong kosongkan meja dan kerusi di bawah siling itu dulu.'),
    ('Mei Ling', 'Baik, saya kosongkan sekarang. Saya tidak ada di rumah pagi ini, tetapi saya ada di rumah petang ini.'),
    ('Mei Ling', 'Terima kasih banyak.'),
]

CULTURE = [
    'Two suffixes, two jobs. ‹-kan› is for someone or to make it happen («matikan», «bersihkan»); ‹-i› is to or at a person or place («hubungi»). A few roots take either one, '
    'and the meaning changes, so each verb is learned with its object: «hubungi juruteknik», «baiki paip», «matikan lampu». Notices say «Sila hubungi pejabat pengurusan», and '
    'for a repair Malaysian Malay uses «baiki» and «membaiki».',
    'Everyday speech often uses the plain verb: «buka lampu» and «tutup lampu» for «hidupkan lampu» and «matikan lampu» (also for the aircon), and «Sila isi borang ini» for «isikan». '
    'Both are correct. This course teaches the ‹-kan› form first and you will understand the everyday form when you hear it.',
    'General knowledge, not a rule and not a checked fact: in many Malaysian condominiums residents report a problem such as a leak to the management office, which may book a technician for a time slot. '
    'Buildings differ, so ask the office about your own case.',
    'Japanese learners often put ‹-kan› on every verb. Here that is a mistake: «Tolong baca emel ini» and «Saya hubungi juruteknik» do not need it. Start the call with your name and unit, '
    'say plainly what is wrong, and thank the office at the end.',
]
CULTURE_JA = [
    '二つの接尾辞に二つの働きがあります。‹-kan› は誰かのため・そうなるようにする動作（«matikan»・«bersihkan»）、‹-i› は人や場所へ向かう動作（«hubungi»）です。語根によってはどちらも取れて、'
    '意味が変わるので、動詞は目的語と一緒に覚えます：«hubungi juruteknik»・«baiki paip»・«matikan lampu»。掲示では «Sila hubungi pejabat pengurusan» と書かれ、修理にはマレーシアのマレー語で «baiki»・«membaiki» を使います。',
    '日常会話では素の動詞がよく使われます：«hidupkan lampu»・«matikan lampu» の代わりに «buka lampu»・«tutup lampu»（エアコンも同じ）、«isikan» の代わりに «Sila isi borang ini» です。'
    'どちらも正しいので、このコースでは ‹-kan› の形を先に教え、日常の形は聞いて分かるようにします。',
    '一般的な知識であり、規則でも確認済みの事実でもありません：マレーシアの多くのコンドミニアムでは、水漏れなどの問題は管理事務所に連絡し、事務所が技術者を時間帯で予約することがあります。'
    '建物によって違うので、自分の場合は事務所に聞いてください。',
    '日本人の学習者は ‹-kan› をどの動詞にも付けがちですが、ここでは間違いです：«Tolong baca emel ini» や «Saya hubungi juruteknik» には要りません。電話は名前と部屋番号から始め、'
    '何がおかしいかをはっきり言い、最後に事務所にお礼を言いましょう。',
]

EXTRA = dict(
    slug='review-block', type='Reading and writing', sub_type='composition', kind='review',
    title='Review block · Chapters 10 to 12: a request and a reply',
    goal='I can use ber- verbs, meN- verbs, ‹-kan› and ‹-i› verbs and the markers together in one request and reply, without notes.',
    grammar=['ms-c10-g02', 'ms-c11-g02', 'ms-c11-g05', 'ms-c12-g02', 'ms-c12-g04', 'ms-c12-g06'],
    patterns=['ms-c10-f01', 'ms-c11-f01', 'ms-c11-f03', 'ms-c12-f01', 'ms-c12-f02', 'ms-c12-f05'],
    model=['Chapters 10 to 12 in one exchange (all names and times are fictional):',
           'A: «Selamat pagi, Puan Aini. Saya bekerja di rumah hari ini. Boleh hubungi juruteknik?» B: «Boleh. Saya sudah menelefon pejabat pengurusan.»',
           'A: «Siapa yang menghantar borang aduan itu?» B: «Encik Rahman yang menghantar borang itu. Tolong simpankan salinan borang itu di pejabat.»',
           'A: «Juruteknik sedang membaiki paip. Boleh tunjukkan mesej itu?» B: «Boleh. Nombor penjejakan ada dalam mesej ini.»',
           'A: «Pukul berapa juruteknik sampai?» B: «Pukul tiga. Tolong matikan lampu itu dan kosongkan meja dulu.»',
           'Notice: ber- verbs have no object; meN- verbs take the thing directly; ‹-kan› is for someone or makes it happen; ‹-i› points at a person or place; the markers go in front of any of them. / '
           '気づくこと：ber- の動詞は目的語をとらず、meN- の動詞は物をすぐあとに置き、‹-kan› は誰かのため・そうなるようにする動作、‹-i› は人や場所へ向かう動作で、マーカーはどれの前にも付きます。'],
    plan=['0–5 Recall: say one request with «Tolong» + a ‹-kan› verb and one thing you did with a meN- verb at the office.',
          '5–15 Mixed input: read the model; underline every ber- verb, meN- verb, ‹-kan› verb and ‹-i› verb and name the marker in front of each.',
          '15–30 Alternating role task: in pairs, one is a resident who asks and one is the office who answers; swap after seven minutes (task below).',
          '30–40 Changed situation: the office says the technician now comes earlier; the resident explains who contacts whom and what they switch off.',
          '40–45 Self-check against the list below, then one thing to practise at home.',
          '0–5 復習・5–15 混合の入力・15–30 役割交代のタスク・30–40 状況の変更・40–45 自己チェック。'],
    task=['Part 1 (15 min, alternating): A is a resident and reports a problem («Ada kebocoran di siling saya.»), asks the office to do two things («Tolong …», «Boleh hubungi …?») and answers «Bila …?». '
          'B is the office and asks the block and unit, says what to switch off and offers a slot. After seven minutes swap.',
          'Part 2 (10 min, changed situation): B says «Maaf, juruteknik datang pukul dua, bukan pukul tiga.» A says who will contact the technician, what A is switching off and what A is emptying.',
          'Part 3 (5 min): write three sentences about your own home, one with a meN- verb, one with a ‹-kan› verb and one with «hubungi».',
          'パート1：交代で住民と事務所を演じます。パート2：状況が変わり、住民は誰が技術者に連絡し、何を消し、何を空にするかを説明します。パート3：自分の家について、meN- の動詞・‹-kan› の動詞・«hubungi» を一つずつ使った3文を書きます。'],
    check=['☐ meN- verbs have the right front for the first sound of the root («membaiki», «menghubungi», «menyemak»).',
           '☐ ‹-kan› verbs keep the spelling of their card (two k in «letakkan» and «tunjukkan»; «bersihkan», not *berbersih).',
           '☐ The person follows «hubungi» directly, with no extra word.',
           '☐ A request uses «Tolong» or «Boleh» and the thing follows the verb.',
           '☐ The marker («sudah», «belum», «sedang», «akan») stands in front of the verb, and a bare «hubungi» or «baiki» becomes «menghubungi» or «membaiki» after it.'],
    answer='Any natural exchange that follows the checklist. Model: «Ada kebocoran di siling saya. Tolong hubungi juruteknik. Saya matikan lampu itu sekarang dan kosongkan meja dulu. '
           'Juruteknik sedang membaiki paip, dan Encik Rahman akan menelefon saya.»',
    key_extra=['Mark for the task first (the right kind of verb in each answer, a marker, one request), then for form (the spelling of the suffixed verb, the person after «hubungi»). '
               'Accept the everyday root in speech, but ask for the standard form once in the written part.',
               'A review block has no new words. Every word is from chapters 1 to 12; the core groups of 10A to 12B all return.'],
    explain=('ユニット12Bのあとの復習（45分）：ber-・meN-・‹-kan›・‹-i› の動詞とマーカーを一つの依頼と返事でノートなしで使い、状況の変更にも対応します。日本語は未監修です。',
             'The review block after unit 12B (45 minutes): use ber- verbs, meN- verbs, ‹-kan› and ‹-i› verbs and the markers in one request and reply without notes, then cope with a changed situation.'),
)

CFG = dict(
    chapter=12, label='12B', unit_id='ms-c12b',
    menu_title='Chapter 12 · -kan and -i verbs', genre='Housing',
    prerequisite_units=['ms-c12a'], prereq_grammar=['ms-c12-g02', 'ms-c12-g08', 'ms-c11-g02', 'ms-c08-g02'],
    unit_goal='Report a leak to the management office, ask for a repair with «baiki» and «hubungi», and use the ‹-kan› verbs for switching, cleaning and filling.',
    core=CORE,
    recognition=[],
    revision=[('Roots of the ‹-kan› and ‹-i› verbs', REV_ROOTS), ('The home', REV_HOME), ('Asking, feelings and place', REV_ASK),
              ('Time and markers', REV_TIME)],
    core_groups=[('The leak and the report', LEAK), ('Repair and contact', REPAIR), ('Switch, empty, clean, fill', SWITCH)],
    grammar_ids={'kan': 'ms-c12-g02', 'boleh': 'ms-c12-g03', 'i': 'ms-c12-g04', 'collect': 'ms-c12-g05', 'repair': 'ms-c12-g06',
                 'leak': 'ms-c12-g07', 'spelling': 'ms-c12-g08'},
    grammar=['i', 'repair', 'leak', 'kan', 'spelling'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 25 cards ms-c12-025 to ms-c12-045 and ms-c12-046 to ms-c12-049', frame_list='ms-c12-f04, f05, f06 and f01', frame_list_ja='f04・f05・f06・f01',
    extra=EXTRA,
    goals={'A': 'I can ask someone to contact a person with «Boleh hubungi …?» and say that a technician is repairing something with «sedang membaiki».',
           'B': 'I can report a leak with «Ada kebocoran di … saya», answer the office\'s questions and book a slot.',
           'C': 'I can follow a call to the management office and read a complaint form and a notice about a repair.',
           'D': 'I can choose between ‹-kan› and ‹-i› and spell «membaiki», «menghubungi», «bersihkan» correctly.',
           'E': 'I can report a problem and agree a repair time in a short role-play, and handle a changed time.'},
    goals_ja={'A': '«Boleh hubungi …?» で人に連絡してもらうよう頼み、«sedang membaiki» で技術者が修理中だと言える。',
              'B': '«Ada kebocoran di … saya» で水漏れを伝え、事務所の質問に答え、時間帯を決められる。',
              'C': '管理事務所への電話が分かり、苦情の用紙と修理についての掲示を読める。',
              'D': '‹-kan› と ‹-i› を使い分け、«membaiki»・«menghubungi»・«bersihkan» を正しくつづれる。',
              'E': '短いロールプレイで問題を伝えて修理の時間を決め、時間の変更にも対応できる。'},
    setting='A Thursday morning at a fictional condominium in Kuala Lumpur: «Encik» Tanaka, Block B, unit 12-3, telephones the management office about a leak in his bathroom ceiling. '
            'All names, blocks, units and times are fictional.',
    setting_ja='木曜日の朝、クアラルンプールの架空のコンドミニアム。田中さん（B棟12-3号室）が、浴室の天井の水漏れについて管理事務所に電話します。名前・棟・部屋番号・時刻はすべて架空です。',
    recall=['Without notes, from unit 12A: say two requests with a ‹-kan› verb («Tolong simpankan …», «Boleh tunjukkan …?») and one with the plain root. / '
            '12Aの復習：‹-kan› の動詞を使った依頼を二つ、語根だけの依頼を一つ言いましょう。',
            'Recall prompt: «Tolong …» (keep this parcel) «Boleh …?» (show the message) «Saya mahu ambil …»'],
    recall_key='e.g. «Tolong simpankan bungkusan ini.» «Boleh tunjukkan mesej itu?» «Tolong tutup pintu itu.» Then show the new step: the other suffix, ‹-i›, and the same ‹-kan› verbs for things in the home.',
    patterns=P, pattern_ids=['ms-c12-f05', 'ms-c12-f04', 'ms-c12-f06', 'ms-c12-f01'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 12 frames f05, f04, f06 and f01 (f01, f02 and f03 are unit 12A; f01 returns here).',
    pattern_keys=['Pattern 1: «Boleh» or «Tolong» + «hubungi» + the person. Check that nothing comes between the verb and the person (no «dengan» and no ‹kepada›). '
                  'Accept «Saya hubungi» and «Kami menghubungi» in a reply.',
                  'Pattern 2: «sedang membaiki» + the thing. Check ‹mem-› before b. Keep «baiki» for a repair and «baik» for good, and do not use «baiki» for correcting a mistake.',
                  'Pattern 3: «Ada kebocoran / kerosakan di» + the place + «saya». Check «di» before the place.',
                  'Pattern 4: «Tolong» + a ‹-kan› verb + the thing. Check «matikan» and «hidupkan», and the spelling of «bersihkan». Accept «tutup lampu» and «buka lampu» in speech.'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 7, 9),
    drills={
        'repeat_frame': 'Frame: «Boleh» [«hubungi» / «baiki» / «matikan»] [«juruteknik» / «paip itu» / «lampu itu»]?',
        'repeat': ['«Boleh hubungi juruteknik?»', '«Juruteknik sedang membaiki paip.»', '«Ada kebocoran di siling saya.»',
                   '«Tolong matikan lampu itu dulu.»', '«Kami akan menghubungi juruteknik.»', '«Ada slot petang ini, pukul tiga.»',
                   '«Tolong hubungi saya sebelum juruteknik sampai.»', '«Saya isi borang aduan sekarang.»'],
        'substitute': ['«Boleh hubungi juruteknik?» (cue: «kontraktor»)',
                       '«Juruteknik sedang membaiki paip.» (cue: «kontraktor», «siling»)',
                       '«Ada kebocoran di siling saya.» (cue: «kerosakan», «paip dapur»)',
                       '«Tolong matikan lampu itu.» (cue: «hidupkan», «kipas»)',
                       '«Tolong bersihkan lantai itu.» (cue: «kosongkan», «meja»)',
                       '«Kami akan menghubungi juruteknik.» (cue: «pemilik unit itu»)',
                       '«Tolong gantikan lampu itu.» (cue: «perlahankan», «muzik»)',
                       '«Ada slot petang ini.» (cue: «esok pagi»)'],
        'transform': ['Request to question: «Hubungi juruteknik.» (with «Boleh»)', 'Standard to everyday: «Tolong matikan lampu itu.» (with «tutup»)',
                      'Everyday to standard: «Tolong isi borang ini.» (with «isikan»)', 'Add «sudah» (and change the verb): «Saya hubungi juruteknik.»',
                      'Add «sedang»: «Juruteknik membaiki paip.»', 'Not yet («belum»): «Kontraktor membaiki siling itu.»',
                      'Make the question with «Siapa yang»: «Pejabat pengurusan menghubungi juruteknik.»', 'Add «akan»: «Kami menghubungi kontraktor.»'],
        'question and answer': ['«Siapa yang sedang membaiki paip?» (cue: «juruteknik»)', '«Ada kebocoran di mana?» (cue: «siling bilik air saya»)',
                                '«Bila juruteknik boleh datang?» (cue: «petang ini, pukul tiga»)', '«Air turun dari siling atau dari paip?» (cue: «siling»)',
                                'You hear: «Saya Tanaka, Blok B, unit 12-3.» Ask the question («unit berapa»).',
                                'You hear: «Kami akan menghubungi juruteknik.» Ask the question («Bila …?»).',
                                'You hear: «Saya takut lampu itu rosak.» Ask the question («kenapa»).',
                                'You hear: «Ada dua slot.» Ask the question («berapa»).'],
        'question-word choice': ['«___ yang sedang membaiki paip?» → «Juruteknik.»', '«Ada kebocoran di ___?» → «Di siling bilik air saya.»',
                                 '«___ juruteknik boleh datang?» → «Petang ini.»', '«___ pukul juruteknik datang?» → «Pukul tiga.»',
                                 '«Siapa ___ menghubungi kontraktor?» → «Pejabat pengurusan yang menghubungi kontraktor.»',
                                 '«___ lampu itu rosak?» → «Sebab air turun dari siling.»', '«Paip ___ rosak?» → «Paip dapur.»',
                                 '«___ lama awak tunggu juruteknik?» → «Satu jam.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. «Boleh» or «Tolong» first, then the verb, then the person or the thing; «hubungi» takes the person directly.',
                   'Cover the line and say it from the English: can you contact the technician?; the technician is repairing the pipe; there is a leak in my ceiling; please switch that light off first; '
                   'we will contact the technician; there is a slot this afternoon at three; please contact me before the technician arrives; I am filling in the complaint form now.'],
        'substitute': ['1 «Boleh hubungi kontraktor?» 2 «Kontraktor sedang membaiki siling.» 3 «Ada kerosakan di paip dapur saya.» 4 «Tolong hidupkan kipas itu.»',
                       '5 «Tolong kosongkan meja itu.» 6 «Kami akan menghubungi pemilik unit itu.» 7 «Tolong perlahankan muzik itu.» 8 «Ada slot esok pagi.»'],
        'transform': ['1 «Boleh hubungi juruteknik?» 2 «Tolong tutup lampu itu.» 3 «Tolong isikan borang ini.» 4 «Saya sudah menghubungi juruteknik.» '
                      '5 «Juruteknik sedang membaiki paip.»',
                      '6 «Kontraktor belum membaiki siling itu.» 7 «Siapa yang menghubungi juruteknik?» 8 «Kami akan menghubungi kontraktor.»'],
        'question and answer': ['1 «Juruteknik yang sedang membaiki paip.» 2 «Ada kebocoran di siling bilik air saya.» 3 «Juruteknik boleh datang petang ini, pukul tiga.» '
                                '4 «Air turun dari siling.»',
                                '5 «Unit berapa?» 6 «Bila kami akan menghubungi juruteknik?» 7 «Kenapa awak takut?» 8 «Ada berapa slot?»'],
        'question-word choice': ['1 «Siapa» 2 «di mana» 3 «Bila» 4 «Pukul berapa» 5 «yang» '
                                 '6 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 7 «yang mana» 8 «Berapa»'],
    },
    short_dialogues=[
        ('Boleh hubungi juruteknik?', 'Boleh. Saya hubungi sekarang.', 'at the management office'),
        ('Ada kebocoran di siling saya.', 'Air turun dari siling atau dari paip?', 'on the phone'),
        ('Tolong matikan lampu itu dulu.', 'Baik, saya matikan sekarang.', 'in the bathroom'),
        ('Bila juruteknik boleh datang?', 'Ada slot petang ini, pukul tiga.', 'booking a slot')],
    short_keys=['1 «Terima kasih. Nanti saya hubungi encik.» 2 «Dari siling, dekat lampu.»',
                '3 «Terima kasih. Saya takut lampu itu rosak.» 4 «Boleh. Terima kasih.»'],
    markers=dict(
        title='Markers with ‹-kan› and ‹-i› verbs', grammar='i',
        instructions=['Say each sentence again with the marker in brackets. After «sudah», «sedang», «belum», «akan», «baru» or «masih», or with a third-person doer, use «menghubungi» and «membaiki», not the bare «hubungi» and «baiki». / '
                      'かっこ内のマーカーを付けて言い直します。«sudah»・«sedang»・«belum»・«akan»・«baru»・«masih» のあと、または三人称の動作主のときは、«hubungi»・«baiki» ではなく «menghubungi»・«membaiki» を使います。'],
        items=['«Saya hubungi juruteknik.» (marker: «sudah»)', '«Kontraktor membaiki siling itu.» (marker: «belum»)',
               '«Juruteknik membaiki paip.» (marker: «sedang»)', '«Kami menghubungi kontraktor.» (marker: «akan»)',
               '«Saya mengisi borang aduan.» (marker: «baru»)', '«Saya tunggu juruteknik.» (marker: «masih»)',
               'Answer «Juruteknik sudah sampai?» (marker: «belum»)',
               '«Pejabat pengurusan menghubungi juruteknik.» (marker: «sedang»)'],
        bridge=['«sudah menghubungi» ≈ もう連絡した · «belum membaiki» ≈ まだ修理していない · «sedang membaiki» ≈ 修理している · '
                '«akan menghubungi» ≈ 連絡する予定 · «baru mengisi» ≈ 記入したばかり',
                'Japanese changes the verb ending (連絡した / 連絡していない); Malay puts the marker in front and uses the meN- verb («menghubungi»), not the bare «hubungi». / '
                '日本語は動詞の語尾が変わります。マレー語はマーカーを前に置き、素の «hubungi» ではなく meN- の動詞（«menghubungi»）を使います。'],
        key=['1 «Saya sudah menghubungi juruteknik.» 2 «Kontraktor belum membaiki siling itu.» 3 «Juruteknik sedang membaiki paip.» '
             '4 «Kami akan menghubungi kontraktor.»',
             '5 «Saya baru mengisi borang aduan.» 6 «Saya masih tunggu juruteknik.» 7 «Belum. Juruteknik belum sampai.» '
             '8 «Pejabat pengurusan sedang menghubungi juruteknik.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を言い、素の ‹-i› の動詞を meN- の動詞（«menghubungi»・«membaiki»・«mengisi»）に直します。',
                 'Say the chapter 4 markers and change the bare ‹-i› verb to the meN- verb («menghubungi», «membaiki», «mengisi») after a marker.')),
    question_note='Chapter 12 adds no new question word. The ‹-kan› and ‹-i› verbs fit every question you know: «Siapa yang menghubungi juruteknik?», '
                  '«Ada kebocoran di mana?», «Bila juruteknik boleh datang?», «Pukul berapa juruteknik sampai?», «Berapa lama awak tunggu?» / '
                  '第12章で新しい疑問語は増えません。‹-kan›・‹-i› の動詞は知っている疑問語すべてと使えます：'
                  '«Siapa yang menghubungi juruteknik?»、«Ada kebocoran di mana?»、«Bila juruteknik boleh datang?»、«Pukul berapa juruteknik sampai?»、'
                  '«Berapa lama awak tunggu?»',
    question_tasks=['Ask what the technician is repairing. («apa»)', 'Ask who contacts the technician. («siapa»)',
                    'Ask where the leak is. («di mana»)', 'Ask formally whether the technician has arrived. («Adakah»)',
                    'Ask politely whether you may switch the light off. («Bolehkah»)', 'Ask how many slots there are. («berapa»)',
                    'Ask when the technician can come. («bila»)', 'Ask what time the technician arrives. («pukul berapa»)',
                    'Ask on what day the contractor comes. («hari apa»)', 'Ask how you contact the management office. («bagaimana»; spoken «macam mana»)',
                    'Ask why the light is damaged. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which pipe is broken. («yang mana»)', 'Ask where the water goes. («ke mana»)',
                    'Ask where the water comes from. («dari mana»)', 'Ask how far the management office is. («berapa jauh»)',
                    'Ask how long you wait for the technician. («berapa lama»)', 'Ask how many lamps are damaged. («berapa»)',
                    'Ask who wrote the complaint form. («siapa» with «oleh»)'],
    question_keys=['1 «Juruteknik sedang membaiki apa?» 2 «Siapa yang menghubungi juruteknik?» 3 «Ada kebocoran di mana?»',
                   '4 «Adakah juruteknik sudah sampai?» 5 «Bolehkah saya matikan lampu itu?» 6 «Ada berapa slot?»',
                   '7 «Bila juruteknik boleh datang?» 8 «Pukul berapa juruteknik sampai?» 9 «Pada hari apa kontraktor datang?»',
                   '10 «Bagaimana saya menghubungi pejabat pengurusan?» (spoken: «Macam mana saya menghubungi pejabat pengurusan?») 11 «Kenapa lampu itu rosak?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab air turun dari siling.» / «Kerana air turun dari siling.»',
                   '12 «Paip yang mana rosak?» 13 «Air itu turun ke mana?» 14 «Air itu turun dari mana?»',
                   '15 «Berapa jauh pejabat pengurusan?» 16 «Berapa lama saya tunggu juruteknik?» 17 «Ada berapa lampu yang rosak?»',
                   '18 «Borang aduan itu ditulis oleh siapa?»'],
    listening=LISTENING,
    listening_context='In the morning «Cik» Mei Ling telephones the management office about a leak in her bathroom. / 朝、メイリンさんが浴室の水漏れについて管理事務所に電話します。',
    listening_before=['Predict: which ‹-kan› and ‹-i› verbs will you hear? Write three guesses (for example «matikan», «hubungi», «baiki»). / 聞こえそうな ‹-kan›・‹-i› の動詞を三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['Which block and unit is Mei Ling in?', 'When did the leak start?', 'What does the office ask her to switch off?',
                      'Which two slots does the office offer?', 'Which slot does Mei Ling choose?', 'What does she ask the office to do before the technician arrives?',
                      'What will the technician do if the pipe is broken?', 'What is the second problem?', 'Who will the office contact about it?'],
    listen_answers=['Block C, unit 5-2', 'last night', 'the fan and the light', 'this afternoon at four, or tomorrow morning', 'this afternoon at four',
                    'contact her', 'replace the pipe', 'loud music in the next unit', 'the neighbour'],
    listening_after=['Compare answers, then shadow lines 4, 7 and 9 after the teacher. / 答えを比べ、4・7・9行目をシャドーイングします。',
                     'Tell your partner about a problem at home in four sentences with ‹-kan› or ‹-i› verbs. / 家の問題について、‹-kan›・‹-i› の動詞を使って4文でパートナーに話しましょう。'],
    test_listen=[(0, 'Block C, unit 5-2', ['blok', 'unit', 'kebocoran']),
                 (2, 'last night', ['malam', 'lantai']),
                 (3, 'the fan and the light', ['matikan', 'kipas', 'lampu']),
                 (6, 'this afternoon at four', ['petang', 'pukul', 'hubungi']),
                 (7, 'replace the pipe', ['baiki', 'menukar', 'paip']),
                 (8, 'loud music in the next unit', ['perlahankan', 'muzik', 'bising'])],
    test_listen_prompts=['Which block and unit is Mei Ling in?', 'When did the leak start?', 'What does the office ask her to switch off?',
                         'Which slot does she choose?', 'What will the technician do if the pipe is broken?', 'What is the second problem?'],
    reading_title='Reading and writing · A complaint form and a notice',
    reading=['Fictional complaint form and notice (all names, blocks and units are invented):',
             '«BORANG ADUAN. Nama: Mei Ling. Blok C, unit 5-2. Aduan: kebocoran di paip bilik air. Juruteknik datang pukul empat petang. Hubungi saya sebelum juruteknik sampai.»',
             'Sign at the management office: «Sila hubungi pejabat pengurusan. Sila isi borang aduan.»'],
    read_questions=['Who wrote the complaint?', 'Which block and unit?', 'What is the complaint?', 'What time does the technician come?',
                    'What does the writer ask for before the technician arrives?', 'What does the sign ask you to do?',
                    'Say in Malay: "The technician is repairing the pipe."'],
    read_answers=['Mei Ling', 'Block C, unit 5-2', 'a leak at the bathroom pipe', 'at four in the afternoon', 'to be contacted',
                  'to contact the management office and fill in the complaint form', '«Juruteknik sedang membaiki paip.»'],
    write_instruction='Write four or five sentences to the management office about a problem at home: say what is wrong and where, and ask for a repair and a contact. / '
                      '家の問題について管理事務所にあてて4〜5文を書きましょう：何がどこでおかしいかを言い、修理と連絡を頼みます。',
    write_model='«Selamat pagi. Saya Tanaka, Blok B, unit 12-3. Ada kebocoran di siling bilik air saya. Tolong baiki siling itu. Tolong hubungi saya sebelum juruteknik sampai. Terima kasih.»',
    writing_type='message',
    task_title='Task · Report a leak and book a slot',
    role_a=['Your information (fictional): you are a resident, Block B, unit 12-3. There is a leak in your bathroom ceiling, near the light. The light may be damaged.',
            'Telephone the office. Say who you are, what is wrong and where. Switch off what the office asks. Ask when the technician can come, and ask the office to contact you before the technician arrives.',
            'Aの情報（架空）：あなたはB棟12-3号室の住民です。浴室の天井の電灯の近くで水漏れがあり、電灯が壊れているかもしれません。'
            '事務所に電話し、名前・何がどこでおかしいかを伝え、事務所に言われたものを消し、技術者はいつ来られるかをたずね、技術者が着く前に連絡してもらうよう頼みます。'],
    role_b=['You are the management office. Ask the block and unit, whether the water comes from the ceiling or a pipe, and tell A to switch the light off. Offer a slot this afternoon at three.',
            'Say you will contact the technician and fill in the complaint form. Say what the technician will do.',
            'Bは管理事務所です。棟と部屋番号、水が天井から来るのか管などから来るのかをたずね、電灯を消すよう言います。今日の午後3時の時間帯を提案します。'
            '技術者に連絡して苦情の用紙に記入すると言い、技術者が何をするかを伝えます。'],
    change=['Halfway, B says: «Maaf, juruteknik datang pukul dua, bukan pukul tiga. Boleh?» A agrees and asks B to contact A before the technician arrives.',
            '途中でBが «Maaf, juruteknik datang pukul dua, bukan pukul tiga. Boleh?» と言います。Aは了承し、技術者が着く前に連絡してほしいと頼みます。'],
    success=['☐ A reports the problem with «Ada kebocoran di … saya» and gives block and unit.',
             '☐ A uses «hubungi» with the person directly and at least one ‹-kan› verb («matikan», «kosongkan»).',
             '☐ After the change, A agrees to the new time and repeats the request to be contacted.'],
    task_key='«Saya Tanaka, Blok B, unit 12-3. Ada kebocoran di siling bilik air saya.» — «Air turun dari siling atau dari paip?» — «Dari siling, dekat lampu.» — '
             '«Tolong matikan lampu itu dulu. Kami akan menghubungi juruteknik.» — «Baik, saya matikan sekarang. Bila juruteknik boleh datang?» — «Ada slot petang ini, pukul tiga. Boleh?» — '
             '«Boleh. Tolong hubungi saya sebelum juruteknik sampai.» — Change: «Maaf, juruteknik datang pukul dua, bukan pukul tiga. Boleh?» — «Boleh. Tolong hubungi saya sebelum juruteknik sampai.»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 12 card notes ms-c12-025 and -026 («baiki», «membaiki»; same spelling as «baik»), -027 and -028 («hubungi», «menghubungi»; common on notices), '
                    '-030, -032 and -033 (everyday «isi», «buka» and «tutup» for lights and aircon), -034 («bersihkan» is «bersih» + ‹-kan›), -035, -041 and -042 (whole words); stage 2 plan section 3 '
                    '(‹-kan› is not a universal politeness ending; ‹-i› has no one English or Japanese equivalent). The paragraph on the management office is general knowledge of condominium life in Malaysia, '
                    'labelled as such and not source-checked; the note states no figure or rule.',
    culture_prompt='In Japanese, who do you contact when something breaks in your home (管理会社・管理人)? How would you say what is wrong and where, and when the repair can come?',
    culture_explain=('‹-kan› と ‹-i› の違い、日常の言い方（«buka lampu»・«tutup lampu»）、管理事務所への連絡の一般的な流れ、日本人学習者がしがちな間違いを読みます。',
                     'Read about the difference between ‹-kan› and ‹-i›, the everyday forms, the general way of reporting a problem to a management office, and the usual slip of Japanese learners.'),
    quiz_words=['L-1174', 'L-1175', 'L-1180', 'L-0649', 'L-0652', 'L-1183'],
    quiz_meanings=['to repair', 'contact (a request)', 'switch off (a request)', 'ceiling', 'technician', 'complaint, problem report'],
    grammar_quiz=[('Say in Malay: "Can you contact the technician?"', '«Boleh hubungi juruteknik?»', ['boleh', 'hubungi', 'juruteknik']),
                  ('Say in Malay: "The technician is repairing the pipe."', '«Juruteknik sedang membaiki paip.»', ['sedang', 'membaiki', 'paip']),
                  ('Say in Malay: "There is a leak in my ceiling."', '«Ada kebocoran di siling saya.»', ['kebocoran', 'siling']),
                  ('Write the request: please switch that light off first.', '«Tolong matikan lampu itu dulu.»', ['tolong', 'matikan', 'lampu'])],
    test_reading=['Fictional notice at the management office: «Sila hubungi pejabat pengurusan. Sila isi borang aduan. Juruteknik datang petang ini, pukul tiga. '
                  'Ada kebocoran di siling Blok B, unit 12-3.»'],
    reading_quiz=[('Whom should you contact?', 'the management office', ['hubungi', 'pejabat pengurusan']),
                  ('What should you fill in?', 'the complaint form', ['borang', 'aduan']),
                  ('When does the technician come?', 'this afternoon at three', ['juruteknik', 'pukul']),
                  ('Where is the leak?', 'in the ceiling of Block B, unit 12-3', ['kebocoran', 'siling'])],
    speaking_test='Telephone the management office: give your block and unit, report a leak with «Ada kebocoran di … saya», and ask the office to do two things («Tolong matikan …», «Boleh hubungi …?»).',
    speaking_key='Check: «Ada kebocoran di … saya» with «di» and the place; «hubungi» with the person directly; one ‹-kan› verb spelt and said correctly («matikan», «bersihkan», «kosongkan»); '
                 'a time asked with «Bila …?» Accept «tutup lampu» in speech if the ‹-kan› form was also used once.',
    speaking_words=['kebocoran', 'siling', 'hubungi', 'matikan', 'juruteknik'],
    plan={'A_recall': 'unit 12A (‹-kan› requests and the parcel) from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first («hubungi», then «sedang membaiki»), question and answer before the rule; then the vocabulary in three groups with each root, its chapter '
                        'and what the suffix adds (the leak and the report 8, repair and contact 7, switch, empty, clean, fill 6). Write ‹-kan› (for someone, or make it happen) and ‹-i› '
                        '(to or at a person or place) side by side on the board.',
          'B_recall': 'say one request with «Tolong» + a ‹-kan› verb and one with «hubungi».',
          'B_drills': 'pattern table, substitution, transformation (standard to everyday first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner says one problem at home and who they would contact.',
          'D_review': 'cumulative question-word drill (chapters 1 to 12), then the markers drill with new cues and a spelling check of '
                      '«membaiki», «menghubungi», «bersihkan», «hidupkan», «matikan».',
          'D_preview': 'the review block for chapters 10 to 12 (45 minutes), then chapter 13 (negation, permission and advice in health situations).',
          'E_recall': 'say three things you can ask the management office to do.',
          'E_listening': 'read the Kata-Kata scenario lines ms-c12-s11 to ms-c12-s19 (Tanaka and the management office: the ceiling leak, the slot, the complaint form) twice; '
                         'learners tick the ‹-kan› and ‹-i› verbs they hear.',
          'E_roleplay': 'pairs play the same scene with their own block, unit and problem, without the script.',
          'E_variation': 'a changed time: the office says the technician now comes at two; the resident agrees, says what to switch off and asks to be contacted.'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 12 to the home-condo scenes (a leak, the management office, a technician). '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: the review block after 12B (chapters 10 to 12), then chapter 13 (health situations).',
    teacher_notes=['Load: 25 core words in three groups (the leak and the report 10; repair and contact 9; switch, empty, clean, fill 6), no recognition word (no Dunia scene primes chapter 12), '
                   'and revision of the roots, the home, asking and feelings, and the markers. Suggested order: Block A the first group with patterns 1 and 2; Block B the second group with pattern 3; '
                   'the third group with pattern 4 in Block B or C. If the pilot shows 25 is too many, the natural cut is: «hubungi», «membaiki», «baiki», «kebocoran», «siling», «juruteknik», «matikan», '
                   '«hidupkan», «aduan», «slot» first; the rest second.',
                   'The ‹-kan› and ‹-i› choice (plan section 3, Sam 13 Nov 2026): ‹-kan› is to do it for someone or to make it happen («matikan», «bersihkan», «kosongkan»); ‹-i› is to or at a person or '
                   'place («hubungi»). Spelling traps from the cards: «baiki» has the same spelling as «baik» but means to repair (card ms-c12-025); «membaiki» has ‹mem-› before b (ms-c12-026); '
                   '«menghubungi» has ‹meng-› before h (ms-c12-028); «bersihkan» is «bersih» + ‹-kan›, not ‹ber-› + ‹sih› (ms-c12-034). The pe-, ke-an and -an words («pengawal», «kebocoran», '
                   '«kerosakan», «aduan», «tempahan») are whole words (cards ms-c12-029, -035, -041, -042).',
                   'Where Japanese learners usually slip: (1) putting ‹-kan› on every verb as if it were a polite ending; (2) adding a に-word such as «dengan» after «hubungi»; '
                   '(3) *perbaiki for a repair (Indonesian): the course uses «baiki» and «membaiki»; (4) *bersihan or *berbersih for «bersihkan»; (5) treating «baiki» as «baik» (good); '
                   '(6) 直す covers «membaiki» and correcting a mistake: only the first is «baiki».',
                   'the ‹-kan› rule (Sam, 13 Nov 2026): use the bare ‹-kan› verb for a request («Tolong simpankan …», «Boleh bawakan …?») and for a first-person offer or reply («Saya hantarkan sekarang.», «Baik, saya matikan sekarang.»); in a statement with a third-person doer or with «sudah», «sedang», «belum», «akan», «baru» or «masih», use the meN- verb the course has («Pengawal menyimpan bungkusan itu.», «Juruteknik akan membaiki paip itu.», «Kami akan menghubungi juruteknik.», «Saya sedang membawa bungkusan itu ke lif.»); where the course has no meN- verb («letakkan», «bukakan», «matikan», «bersihkan»), rephrase: «Saya letakkan bungkusan itu di sini sekarang.», «Saya bersihkan lantai itu sekarang.» The same goes for ‹-i› verbs: «hubungi» and «baiki» are for requests and first-person replies, «menghubungi» and «membaiki» for the rest. Do not teach forms such as *menyimpankan or *menghantarkan: they are not natural.',
                   'Management office (general knowledge, not a rule and not source-checked; no figure): in many Malaysian condominiums residents report a leak or a fault to the management office, which may book a technician for a time slot. '
                   'Buildings differ, so tell learners to ask the office about their own case.',
                   'Spoken forms: «buka lampu» and «tutup lampu» for «hidupkan» and «matikan» (card notes ms-c12-032 and -033), and «isi» for «isikan» (ms-c12-030). They are everyday words; accept them '
                   'in speech and never mark them wrong. Standard first: teach the ‹-kan› form.',
                   'The scene follows Kata-Kata c12 (scenario lines ms-c12-s11 to s19, frames f04, f05 and f06, with f01 returning). All names, blocks, units and times are fictional; '
                   'learners may use their real building or an invented one.',
                   'Cumulative question words: chapters 1 to 12. Chapter 12 adds no new question word.'],
)

UNIT = unit_dict(CFG)
