"""Unit 13: belum, permission, need, advice and rules in health situations: the panel clinic and the pharmacy
(Saya belum ___; Bolehkah saya ___?; Saya perlu ___; Encik patut ___; Tidak dibenarkan ___ di sini; Borang ini wajib ___).

25 core ledger entries, the rows the ledger places in "Ch13 (unit 13)": the existing rows L-0627 «penyambut tetamu», L-0630
«klinik panel», L-0631 «sakit tekak», L-0633 «alahan», L-0634 «simptom», L-0636 «bila perlu», L-0638 «temu janji» and L-0648
«daftar»; the new rows L-1185 to L-1200 (including L-1200 «cuti sakit / MC»); and L-1268 «mendaftar» (added by Sam in the Kata-Kata
step 3c, Journal row 184). They come in three groups: need, advice and rules (10), the panel clinic (11) and the pharmacy (4). No
recognition word: «MC» is the spoken form inside the headword of L-1200 and is labelled spoken wherever it appears. The ke-an,
-an and lexicalised words («kebenaran», «kesihatan», «kecemasan», «arahan», «rawatan», «alahan», «sesuai») are taught as whole
words, and «mesti» as a root (it is not me- + sti), as the Kata-Kata chapter 13 card notes say. The scene follows Kata-Kata c13
(scenario lines ms-c13-s01 to s18: the panel clinic and the pharmacy) word for word, and goes further in class: a second
patient, a form, a rule on a sign and a changed time. All names, clinics and times are fictional.

Safety: the unit writes no diagnosis, no treatment advice, no medicine name with a dose and no dosing instruction. The doctor only
says «patut berehat» and gives sick leave; the pharmacist only points to the label and says «tanya saya lagi». «dos» is taught for
reading a label only. The teacher notes tell learners to follow their own doctor and pharmacist. Japanese is a draft awaiting native
review.
"""
from .chapter10_common import unit_dict

RULES = ['L-1185', 'L-1186', 'L-1199', 'L-1187', 'L-1188', 'L-1189', 'L-1190', 'L-1196', 'L-1197', 'L-0636']
CLINIC = ['L-0627', 'L-0630', 'L-0638', 'L-0648', 'L-1268', 'L-1200', 'L-0634', 'L-0631', 'L-0633', 'L-1194', 'L-1195']
PHARMACY = ['L-1191', 'L-1193', 'L-1192', 'L-1198']
CORE = RULES + CLINIC + PHARMACY

# Revision: words placed in chapters 1 to 12 that the unit really uses (a test fails if one is not used).
REV_NOT = ['L-0030', 'L-0130', 'L-0194', 'L-1062', 'L-0076', 'L-0783', 'L-0193', 'L-0192', 'L-0189', 'L-0191', 'L-0195']
REV_HEALTH = ['L-0407', 'L-0406', 'L-0409', 'L-0410', 'L-0255', 'L-1093', 'L-1098', 'L-0534']
REV_FORM = ['L-0419', 'L-0420', 'L-1147', 'L-0423', 'L-0124', 'L-0421', 'L-0532', 'L-0066', 'L-1141', 'L-1135', 'L-1155', 'L-0451', 'L-0127']
REV_RULES = ['L-0397', 'L-0401', 'L-0197', 'L-0198', 'L-0325', 'L-0471', 'L-0574', 'L-0368']
REV_ASK = ['L-0018', 'L-0375', 'L-0020', 'L-0535', 'L-0476', 'L-0473', 'L-0024', 'L-1175', 'L-1168', 'L-0188', 'L-1050', 'L-0688']

EXAMPLES = {
    # Need, advice and rules
    'L-1185': '«Saya perlu berjumpa doktor.»',
    'L-1186': '«Encik patut berehat.»',
    'L-1199': '«Encik mesti baca arahan di label.» («mesti» is a root, not ‹me-› + ‹sti›)',
    'L-1187': '«Borang ini wajib diisi.»',
    'L-1188': '«Tidak dibenarkan minum di sini.»',
    'L-1189': '«Awak mesti minta kebenaran bos dulu.» (permission only)',
    'L-1190': '«Itu nasihat doktor.»',
    'L-1196': '«Tolong elakkan lif itu. Lif itu rosak.»',
    'L-1197': '«Pukul empat petang sesuai?»',
    'L-0636': '«Tanya penyambut tetamu bila perlu.»',
    # The panel clinic
    'L-0627': '«Penyambut tetamu ada di kaunter.»',
    'L-0630': '«Ini klinik panel syarikat encik?»',
    'L-0638': '«Ada temu janji?»',
    'L-0648': '«Encik perlu daftar dulu.»',
    'L-1268': '«Saya belum mendaftar.» (standard form of «daftar»)',
    'L-1200': '«Saya berikan cuti sakit satu hari.» (spoken: «MC»)',
    'L-0634': '«Apa simptom encik?»',
    'L-0631': '«Saya demam dan sakit tekak.»',
    'L-0633': '«Encik ada alahan?»',
    'L-1194': '«Borang kesihatan ini wajib diisi.»',
    'L-1195': '«Kad ini untuk rawatan di klinik panel.»',
    # The pharmacy
    'L-1191': '«Farmasi ada di sebelah klinik.»',
    'L-1193': '«Saya tidak faham arahan itu.»',
    'L-1192': '«Dos ada di label itu.»',
    'L-1198': '«Pintu kecemasan ada di sebelah kiri.»',
    # Revision · not, not yet and the markers
    'L-0030': '«Tidak ada. Saya tidak ada alahan.»',
    'L-0130': '«Ini bukan klinik panel.»',
    'L-0194': '«Saya belum makan.»',
    'L-1062': '«Jangan masuk. Doktor belum ada.»',
    'L-0076': '«Boleh. Sila masuk.»',
    'L-0783': '«Bolehkah saya masuk?»',
    'L-0193': '«Saya sudah mendaftar.»',
    'L-0192': '«Saya akan menelefon klinik.»',
    'L-0189': '«Saya sedang berjumpa doktor.»',
    'L-0191': '«Saya masih menunggu.»',
    'L-0195': '«Penyambut tetamu baru memanggil nombor saya.»',
    # Revision · health and the clinic
    'L-0407': '«Doktor, boleh saya minta cuti sakit?»',
    'L-0406': '«Klinik ada di tingkat satu.»',
    'L-0409': '«Saya demam dan sakit tekak.»',
    'L-0410': '«Saya batuk juga.»',
    'L-0255': '«Saya demam dan sakit tekak.»',
    'L-1093': '«Encik patut berehat di rumah.»',
    'L-1098': '«Saya perlu berjumpa doktor.»',
    'L-0534': '«Saya minta cuti esok.»',
    # Revision · forms and the counter
    'L-0419': '«Sila isi borang ini.»',
    'L-0420': '«Saya belum isi borang.»',
    'L-1147': '«Saya sedang mengisi borang kesihatan.»',
    'L-0423': '«Daftar di kaunter.»',
    'L-0124': '«Cik perlu bawa kad syarikat.»',
    'L-0421': '«Saya perlu bawa pasport.»',
    'L-0532': '«Saya perlu minta kebenaran bos.»',
    'L-0066': '«Ini klinik panel syarikat encik?»',
    'L-1141': '«Tolong tunggu di bilik menunggu.»',
    'L-1135': '«Doktor akan panggil cik.» (formal: «memanggil»)',
    'L-1155': '«Saya akan menelefon bos dulu.»',
    'L-0451': '«Saya belum tempah.»',
    'L-0127': '«Saya belum bayar.»',
    # Revision · signs and rules
    'L-0397': '«Dilarang makan dan minum di bilik menunggu.»',
    'L-0401': '«Sila isi borang ini.»',
    'L-0197': '«Boleh saya makan di sini?»',
    'L-0198': '«Boleh saya minum air di sini?»',
    'L-0325': '«Bolehkah saya masuk?»',
    'L-0471': '«Boleh saya duduk di sini?»',
    'L-0574': '«Boleh saya letak beg di sini?»',
    'L-0368': '«Tidak dibenarkan ambil gambar di sini.»',
    # Revision · asking and thanking
    'L-0018': '«Maaf, tidak dibenarkan minum di sini.»',
    'L-0375': '«Tolong jangan bising di bilik menunggu.»',
    'L-0020': '«Doktor, boleh saya minta cuti sakit untuk esok?»',
    'L-0535': '«Tanya penyambut tetamu bila perlu.»',
    'L-0476': '«Baik, saya faham.»',
    'L-0473': '«Maaf, boleh cakap lagi sekali?»',
    'L-0024': '«Kalau ada soalan, tanya saya lagi.»',
    'L-1175': '«Hubungi saya bila perlu.»',
    'L-1168': '«Dos ada di label itu.»',
    'L-0188': '«Maaf, boleh cakap lagi sekali?»',
    'L-1050': '«Kenapa tidak dibenarkan minum di sini?» «Kerana ini bilik menunggu.»',
    'L-0688': '«Sebab ini bilik menunggu.»',
}

# For the whole words and the suffixed forms: the root as the Kata-Kata card note gives it, and the teaching point.
# (what the entry shows in English, in Japanese)
VOCAB_OPTS = {
    'L-1188': {'en': 'allowed (‹di-› + ‹benar› + ‹-kan›: learn the whole word; the opposite of «dilarang», chapter 9; usually «tidak dibenarkan» on a sign)',
               'ja': '許可されている（‹di-› ＋ ‹benar› ＋ ‹-kan›：一語まるごと覚える；«dilarang»（第9章）の反対；掲示では «tidak dibenarkan» がふつう）'},
    'L-1189': {'en': 'permission, taught only in this sense: «minta kebenaran» (learn the whole word; ‹ke-an› words come in Stage 3; the root is ‹benar›)',
               'ja': '許可（この意味だけを教える）：«minta kebenaran»（一語まるごと覚える；‹ke-an› の語は第3段階；語根は ‹benar›）'},
    'L-1194': {'en': 'health (learn the whole word; ‹ke-an› words come in Stage 3; the root is ‹sihat›)',
               'ja': '健康（一語まるごと覚える；‹ke-an› の語は第3段階；語根は ‹sihat›）'},
    'L-1198': {'en': 'emergency (learn the whole word; ‹ke-an› words come in Stage 3; the root is ‹cemas›)',
               'ja': '緊急事態（一語まるごと覚える；‹ke-an› の語は第3段階；語根は ‹cemas›）'},
    'L-1193': {'en': 'instruction, as on a label (learn the whole word; the root is ‹arah›)',
               'ja': '指示（ラベルなどの）（一語まるごと覚える；語根は ‹arah›）'},
    'L-1195': {'en': 'treatment (learn the whole word; the root is ‹rawat›); a word for reading a notice, not for giving advice',
               'ja': '治療（一語まるごと覚える；語根は ‹rawat›）；掲示を読むための語で、助言をするための語ではない'},
    'L-0633': {'en': 'allergy (learn the whole word; the root is ‹alah›)',
               'ja': 'アレルギー（一語まるごと覚える；語根は ‹alah›）'},
    'L-1196': {'en': 'avoid (a request or an instruction; ‹elak› + ‹-kan›, two k, as in chapter 12): «Tolong elakkan …»',
               'ja': '避けてください（依頼や指示；‹elak› ＋ ‹-kan›、第12章と同じく k が二つ）：«Tolong elakkan …»'},
    'L-1197': {'en': 'suitable; a time or a place that suits you (learn the whole word; the root is ‹suai›)',
               'ja': '都合がよい・適している（一語まるごと覚える；語根は ‹suai›）'},
    'L-1199': {'en': 'must; a root, so it is not ‹me-› + ‹sti›',
               'ja': '〜しなければならない；語根で、‹me-› ＋ ‹sti› ではない'},
    'L-1268': {'en': 'to register (standard form of «daftar», ‹meN-› + «daftar»; «daftar» is the everyday word, «mendaftar» is written and careful speech)',
               'ja': '登録する・受付をする（«daftar» の標準形、‹meN-› ＋ «daftar»；«daftar» は日常の語、«mendaftar» は書き言葉・ていねいな話し言葉）'},
    'L-1200': {'en': 'sick leave (standard «cuti sakit»; spoken «MC», from "medical certificate": recognise it, say «cuti sakit»)',
               'ja': '病気休暇（標準 «cuti sakit»；話し言葉 «MC»、英語由来：聞いて分かればよい。言うときは «cuti sakit»）'},
}

P = [
    ('ms-c13-f01', '«Saya belum» ___ «.»  (not yet: «belum» + a verb)', [
        'A: «Awak sudah makan?» B: «Belum. Saya belum makan.»',
        'A: «Encik sudah mendaftar?» B: «Belum. Saya belum mendaftar.»',
        'A: «Awak sudah isi borang ini?» B: «Belum. Saya belum isi borang.»',
        'A: «Awak sudah berjumpa doktor?» B: «Belum. Saya belum berjumpa doktor.»',
        'A: «Apa simptom awak?» B: «Saya demam. Saya tidak batuk.»',
        'A: «Ada temu janji?» B: «Tidak ada. Saya belum tempah.»'],
     "«belum» goes in front of the verb and means not yet, so it also says that you expect to do it later: «Saya belum makan.» (the Kata-Kata frame) is "
     "\"I haven't eaten yet\". The verb does not change. «Belum.» alone is a full answer to «Sudah …?» (chapter 4). «tidak» is a plain no or not, with no \"yet\": "
     "«Saya tidak demam.» says that you do not have a fever. For a noun use «bukan» (chapter 3). After «belum» the standard verb is «mendaftar» "
     "(‹meN-› + «daftar», chapter 11), and everyday speech also drops the prefix: «Saya belum isi borang.» Both are correct; this course teaches the ‹meN-› form first.",
     "«belum» は動詞の前に置いて「まだ〜ていない」を表し、あとでする予定があることも示します：«Saya belum makan.»（Kata-Kata の文型）は「まだ食べていません」。動詞の形は変わりません。"
     "«Belum.» だけで «Sudah …?»（第4章）への答えになります。«tidak» は「いいえ・〜ない」で、「まだ」の意味がありません：«Saya tidak demam.» は「熱がない」という意味です。"
     "名詞には «bukan»（第3章）を使います。«belum» のあとの標準形は «mendaftar»（‹meN-› ＋ «daftar»、第11章）で、日常会話では接頭辞を落として «Saya belum isi borang.» とも言います。"
     "どちらも正しく、このコースでは ‹meN-› の形を先に教えます。",
     'Japanese まだ〜ていません is one pattern and 〜ません is another. Malay matches them: «belum» is まだ〜ていません, «tidak» is 〜ません. The verb ending does not change in Malay.',
     '日本語の「まだ〜ていません」と「〜ません」は別の型で、マレー語では «belum» と «tidak» が対応します。マレー語の動詞は形が変わりません。'),
    ('ms-c13-f02', '«Bolehkah saya» ___ «?»  (asking permission; also «Boleh saya» ___ «?»)', [
        'A: «Bolehkah saya masuk?» B: «Boleh. Sila masuk.»',
        'A: «Boleh saya duduk di sini?» B: «Boleh. Sila duduk.»',
        'A: «Bolehkah saya isi borang di sini?» B: «Boleh. Ini pen.»',
        'A: «Boleh saya cuti esok?» B: «Awak mesti minta kebenaran bos dulu.»',
        'A: «Bolehkah saya minum air di sini?» B: «Maaf, tidak boleh.»',
        'A: «Boleh saya ambil gambar di sini?» B: «Maaf, tidak boleh. Tidak dibenarkan ambil gambar di sini.»'],
     "To ask permission put «Bolehkah saya» or «Boleh saya» in front of the verb: «Bolehkah saya masuk?» (the Kata-Kata frame). «Bolehkah» is the careful, polite form (chapter 2); "
     "«Boleh saya …?» is just as correct in everyday speech, and the course teaches the first and recognises the second. The answer is «Boleh.» or «Maaf, tidak boleh.», "
     "and a short extra word makes it friendly: «Boleh. Sila masuk.» «kebenaran» means permission and nothing else here: «minta kebenaran bos» is to ask the boss for permission. "
     "No little word for \"to\" or \"if\" goes between «saya» and the verb.",
     "許可を求めるときは、動詞の前に «Bolehkah saya» か «Boleh saya» を置きます：«Bolehkah saya masuk?»（Kata-Kata の文型）。«Bolehkah» はていねいな言い方（第2章）で、"
     "«Boleh saya …?» も日常会話で正しい言い方です。このコースでは前者を教え、後者は聞いて分かるようにします。答えは «Boleh.» か «Maaf, tidak boleh.» で、"
     "ひとこと足すと親しみやすくなります：«Boleh. Sila masuk.» «kebenaran» はここでは「許可」の意味だけです：«minta kebenaran bos» は「上司に許可をもらう」。"
     "«saya» と動詞の間に「〜ても」にあたる語は入りません。",
     'Japanese asks permission with the て-form: 入ってもいいですか, 座ってもいいですか. Malay has no て-form and no もいい: put «Boleh saya» before the plain verb, «Boleh saya masuk?». Answer 〜てもいいです with «Boleh.»',
     '日本語は「入ってもいいですか」のように て形で許可を求めます。マレー語には て形も「〜てもいい」にあたる語もなく、«Boleh saya» を素の動詞の前に置いて «Boleh saya masuk?» と言います。「〜てもいいです」への答えは «Boleh.» です。'),
    ('ms-c13-f03', '«Saya perlu» ___ «.»  (need: a step you have to take)', [
        'A: «Apa saya perlu buat?» B: «Awak perlu mendaftar dulu.»',
        'A: «Saya perlu berjumpa doktor.» B: «Ada temu janji?»',
        'A: «Saya perlu bawa apa?» B: «Awak perlu bawa kad syarikat dan pasport.»',
        'A: «Saya perlu tunggu lama?» B: «Tidak perlu. Nombor giliran awak sudah dekat.»',
        'A: «Encik perlu daftar dulu.» B: «Baik. Di mana kaunter?»',
        'A: «Saya perlu isi semua borang ini?» B: «Tidak perlu. Borang kesihatan sahaja wajib diisi.»'],
     "«perlu» + a verb says what you need to do or what is needed: «Saya perlu berjumpa doktor.» (the Kata-Kata frame). It is a plain fact about a step, not a threat and not advice. "
     "«Tidak perlu» means you do not have to: «Tidak perlu tunggu lama.» It does not mean it is forbidden. The standard verb after «perlu» can be «mendaftar» or the everyday «daftar»: "
     "«Encik perlu daftar dulu.» (the Kata-Kata line). The fixed phrase «bila perlu» (when needed) is learned whole: «Tanya penyambut tetamu bila perlu.» "
     "A short answer is «Perlu.» or «Tidak perlu.»",
     "«perlu» ＋ 動詞は、しなければならないこと・必要なことを表します：«Saya perlu berjumpa doktor.»（Kata-Kata の文型）。これは手順についての事実で、おどしでも助言でもありません。"
     "«Tidak perlu» は「しなくてよい」で、禁止ではありません：«Tidak perlu tunggu lama.» «perlu» のあとの標準形は «mendaftar» ですが、日常の «daftar» も使います："
     "«Encik perlu daftar dulu.»（Kata-Kata の文）。決まり文句 «bila perlu»（必要なときに）は一まとまりで覚えます：«Tanya penyambut tetamu bila perlu.» 短い答えは «Perlu.» か «Tidak perlu.» です。",
     'Japanese 〜なければならない (must) and 必要がある (need) are close, and 〜なくてもいい is the opposite. Malay uses «perlu» for the need and «tidak perlu» for 〜なくてもいい. Do not say «tidak boleh» for 〜なくてもいい: that means 〜てはいけません.',
     '日本語の「〜なければならない」と「必要がある」は近く、「〜なくてもいい」はその反対です。マレー語は必要に «perlu»、「〜なくてもいい」に «tidak perlu» を使います。「〜なくてもいい」に «tidak boleh» を使わないでください。それは「〜てはいけません」です。'),
    ('ms-c13-f04', '«Encik patut» ___ «.»  (advice) and «mesti» (must)', [
        'A: «Encik patut berehat.» B: «Baik, doktor. Terima kasih.»',
        'A: «Saya mahu cuti esok. Apa saya patut buat?» B: «Awak patut tanya bos dulu.»',
        'A: «Kita patut sampai pukul berapa?» B: «Kita patut sampai pukul sembilan.»',
        'A: «Itu nasihat siapa?» B: «Itu nasihat doktor.»',
        'A: «Saya mesti isi borang ini?» B: «Mesti. Borang ini wajib diisi.»',
        'A: «Saya mesti daftar dulu?» B: «Ya, awak mesti daftar dulu.»'],
     "«patut» + a verb is advice: it says what is a good idea, and you may choose: «Encik patut berehat.» (the Kata-Kata frame, said by the doctor). «nasihat» is the advice itself. "
     "«mesti» is must, with no choice: «Encik mesti baca arahan di label.» «mesti» is a root, not ‹me-› + ‹sti›. «wajib» is must on a form or a notice: «Borang ini wajib diisi.» "
     "So the three steps are: «perlu» (a step you take), «patut» (advice) and «mesti» or «wajib» (must). This course teaches the language of advice only; for your health follow your own doctor and pharmacist. "
     "«Elakkan» (avoid) belongs to notices and requests: «Tolong elakkan lif itu.» To tell someone not to make a noise, say «Tolong jangan bising.»",
     "«patut» ＋ 動詞は助言で、よいことを言うだけで、選ぶのは本人です：«Encik patut berehat.»（Kata-Kata の文型、医者の言葉）。«nasihat» は助言そのものです。"
     "«mesti» は「しなければならない」で選べません：«Encik mesti baca arahan di label.» «mesti» は語根で、‹me-› ＋ ‹sti› ではありません。«wajib» は用紙や掲示での「必須」です：«Borang ini wajib diisi.» "
     "つまり三つの段階は «perlu»（する手順）、«patut»（助言）、«mesti»・«wajib»（義務）です。このコースが教えるのは助言のことばだけで、健康については自分の医者と薬剤師の指示に従ってください。"
     "«Elakkan»（避ける）は掲示や依頼に使います：«Tolong elakkan lif itu.» 音を立てないでと言うときは «Tolong jangan bising.» です。",
     'Japanese 〜たほうがいい is advice and 〜なければならない is must. Malay keeps them apart: «patut» is 〜たほうがいい, «mesti» and «wajib» are 〜なければならない, «perlu» is 必要がある. Do not use «mesti» for advice: it sounds like an order.',
     '日本語の「〜たほうがいい」は助言、「〜なければならない」は義務です。マレー語も分けます：«patut» が「〜たほうがいい」、«mesti»・«wajib» が「〜なければならない」、«perlu» が「必要がある」です。助言に «mesti» を使わないでください。命令のように聞こえます。'),
    ('ms-c13-f05 and f06', '«Tidak dibenarkan» ___ «di sini.» / «Borang ini wajib» ___ «.»  (signs and forms)', [
        'A: «Boleh saya minum air di sini?» B: «Maaf, tidak dibenarkan minum di sini.»',
        'A: «Boleh saya makan di sini?» B: «Maaf, tidak boleh. Dilarang makan dan minum di bilik menunggu.»',
        'A: «Boleh saya masuk bilik doktor?» B: «Maaf, dilarang masuk. Sila tunggu di bilik menunggu.»',
        'A: «Apa yang tidak dibenarkan di sini?» B: «Tidak dibenarkan ambil gambar dan minum di sini.»',
        'A: «Borang ini wajib diisi?» B: «Ya, borang ini wajib diisi.»',
        'A: «Borang yang mana wajib diisi?» B: «Borang kesihatan wajib diisi.»'],
     "On a sign or a rule, «tidak dibenarkan» + a verb says that something is not allowed: «Tidak dibenarkan minum di sini.» (the Kata-Kata frame). «dibenarkan» is ‹di-› + ‹benar› + ‹-kan›, "
     "the opposite of «dilarang» (chapter 9): «Dilarang makan dan minum di bilik menunggu.» Both are written, rather formal words; in speech people say «tidak boleh». "
     "A notice about a form says «Borang ini wajib diisi.» (the Kata-Kata frame): «wajib» + the passive «diisi» says that it must be filled in, and the thing comes first. "
     "«wajib» is used here for forms and notices only, a plain rule of the place and nothing about religion. The notices in this course are fictional.",
     "掲示や決まりでは、«tidak dibenarkan» ＋ 動詞で「〜は許可されていない」を表します：«Tidak dibenarkan minum di sini.»（Kata-Kata の文型）。«dibenarkan» は ‹di-› ＋ ‹benar› ＋ ‹-kan› で、"
     "«dilarang»（第9章）の反対です：«Dilarang makan dan minum di bilik menunggu.» どちらも書き言葉でやや改まった語で、話すときは «tidak boleh» と言います。"
     "用紙についての掲示は «Borang ini wajib diisi.»（Kata-Kata の文型）：«wajib» ＋ 受け身の «diisi» で「記入が必須」を表し、物が先に来ます。"
     "ここでの «wajib» は用紙や掲示の決まりだけで、宗教とは関係ありません。このコースの掲示は架空です。",
     'Japanese 〜てはいけません and 禁止 cover both the sign «dilarang» and the spoken «tidak boleh». Malay chooses by place: «dilarang» and «tidak dibenarkan» on signs, «tidak boleh» in speech, «jangan» for a command to a person. 記入必須 on a form is «wajib diisi».',
     '日本語の「〜てはいけません」「禁止」は、掲示の «dilarang» と話し言葉の «tidak boleh» の両方にあたります。マレー語は場所で選びます：掲示では «dilarang»・«tidak dibenarkan»、話すときは «tidak boleh»、人への命令は «jangan» です。用紙の「記入必須」は «wajib diisi» です。'),
]

# The Kata-Kata scenario lines ms-c13-s01 to s14 are the model conversation (the panel clinic); s15 to s18 (the pharmacy) are in the task.
DIALOGUE = [
    ('Receptionist', 'Selamat pagi, encik. Ada temu janji?'),
    ('Tanaka', 'Tidak ada. Saya demam dan sakit tekak. Saya batuk juga.'),
    ('Receptionist', 'Encik perlu daftar dulu. Sila isi borang ini.'),
    ('Tanaka', 'Baik. Saya belum isi borang. Bolehkah saya isi borang di sini?'),
    ('Receptionist', 'Boleh. Ini klinik panel syarikat encik?'),
    ('Tanaka', 'Ya. Boleh saya minum air di sini?'),
    ('Receptionist', 'Maaf, tidak dibenarkan minum di sini. Dilarang makan dan minum di bilik menunggu.'),
    ('Tanaka', 'Baik, saya faham. Terima kasih.'),
    ('Receptionist', 'Encik ada alahan?'),
    ('Tanaka', 'Tidak. Saya tidak ada alahan.'),
    ('Doctor', 'Encik patut berehat di rumah. Encik tidak perlu datang ke pejabat esok.'),
    ('Tanaka', 'Doktor, boleh saya minta cuti sakit untuk esok?'),
    ('Doctor', 'Boleh. Saya berikan cuti sakit satu hari.'),
    ('Tanaka', 'Terima kasih, doktor.'),
]
VARIANT = [
    ('Receptionist', 'Selamat petang, cik. Ada temu janji?'),
    ('Mei Ling', 'Ada. Pukul tiga petang. Saya belum mendaftar.'),
    ('Receptionist', 'Cik perlu mendaftar dulu. Borang kesihatan ini wajib diisi.'),
    ('Mei Ling', 'Baik. Boleh saya isi borang di sini?'),
    ('Receptionist', 'Boleh. Sila duduk. Cik ada alahan?'),
    ('Mei Ling', 'Ada. Saya cakap dengan doktor nanti.'),
    ('Receptionist', 'Baik. Tolong tunggu di bilik menunggu. Tidak dibenarkan makan di sini.'),
    ('Mei Ling', 'Boleh saya letak beg di sini?'),
    ('Receptionist', 'Boleh. Doktor akan panggil cik.'),
    ('Mei Ling', 'Terima kasih.'),
]
LISTENING = [
    ('Mei Ling', 'Selamat pagi. Saya Mei Ling. Bolehkah saya berjumpa doktor hari ini? Saya demam dan batuk.'),
    ('Receptionist', 'Selamat pagi, cik. Cik perlu mendaftar dulu. Ada slot pukul empat petang. Sesuai?'),
    ('Mei Ling', 'Pukul empat sesuai. Saya perlu bawa apa?'),
    ('Receptionist', 'Cik perlu bawa kad syarikat. Borang kesihatan wajib diisi, tetapi cik boleh isi borang di klinik.'),
    ('Mei Ling', 'Baik. Saya belum minta kebenaran bos. Saya mesti menelefon bos dulu.'),
    ('Receptionist', 'Boleh. Kalau cik ada alahan, tulis di borang itu. Satu lagi, cik tidak perlu bawa duit sekarang.'),
    ('Mei Ling', 'Baik. Bolehkah saya makan di bilik menunggu?'),
    ('Receptionist', 'Maaf, dilarang makan di bilik menunggu. Cik boleh tunggu di luar.'),
    ('Mei Ling', 'Terima kasih. Nanti saya sampai pukul empat. Sekarang saya pergi ke farmasi.'),
    ('Mei Ling', 'Maaf, boleh cakap lagi sekali? Saya tidak faham arahan itu.'),
    ('Pharmacist', 'Boleh. Cik mesti baca arahan di label. Tanya saya bila perlu.'),
    ('Mei Ling', 'Baik, saya baca label itu. Terima kasih.'),
]

CULTURE = [
    'Need, advice and must are three different strengths. «perlu» is a step you have to take («Encik perlu daftar dulu»), «patut» is advice that leaves the choice to you («Encik patut berehat»), '
    'and «mesti» or «wajib» is a must with no choice («Encik mesti baca arahan di label», «Borang ini wajib diisi»). A doctor in this course only says «patut berehat» and gives sick leave; a pharmacist only points '
    'to the label and says «tanya saya lagi». The course teaches language, not medical knowledge: for your health follow your own doctor and pharmacist.',
    'Signs and speech differ. «Tidak dibenarkan» and «dilarang» are written words for signs and rules; in speech people say «tidak boleh», and «jangan» is a command to a person. To ask permission, '
    'say «Bolehkah saya masuk?» or «Boleh saya masuk?» with the plain verb after «saya». In this course «kebenaran» means permission and nothing else («minta kebenaran bos»), and «wajib» is a plain rule about a form or a notice.',
    'General knowledge, not a rule and not a checked fact: many Malaysian employers have an agreement with a panel clinic, and staff may be asked for a company card or letter. '
    'A doctor may give sick leave, called «cuti sakit» (everyday: «MC»), but who accepts it and how differs by employer, so ask your own company.',
    'Japanese learners ask permission with the て-form (入ってもいいですか). Malay has none: put «Boleh saya» before the plain verb. They also say «tidak boleh» when they mean 〜なくてもいい; that is «tidak perlu».',
]
CULTURE_JA = [
    '必要・助言・義務は強さが違います。«perlu» はしなければならない手順（«Encik perlu daftar dulu»）、«patut» は選ぶのは本人に任せる助言（«Encik patut berehat»）、'
    '«mesti» と «wajib» は選べない義務（«Encik mesti baca arahan di label»、«Borang ini wajib diisi»）です。このコースの医者は «patut berehat» と言って病気休暇を出すだけで、薬剤師はラベルを指して '
    '«tanya saya lagi» と言うだけです。このコースが教えるのは医学の知識ではなくことばです。健康については自分の医者と薬剤師の指示に従ってください。',
    '掲示と話し言葉は違います。«Tidak dibenarkan» と «dilarang» は掲示や決まりの書き言葉で、話すときは «tidak boleh»、«jangan» は人への命令です。許可を求めるときは、«saya» のあとに素の動詞を置いて '
    '«Bolehkah saya masuk?» か «Boleh saya masuk?» と言います。このコースの «kebenaran» は「許可」の意味だけ（«minta kebenaran bos»）で、«wajib» は用紙や掲示についての単なる決まりです。',
    '一般的な知識であり、規則でも確認済みの事実でもありません：マレーシアの多くの雇用主はパネルクリニックと契約しており、会社のカードや書類を求められることがあります。'
    '医者は病気休暇（«cuti sakit»、日常は «MC»）を出すことがありますが、受け付けるかどうかは雇用主によって違うので、自分の会社に聞いてください。',
    '日本人の学習者は て形で許可を求めがちです（入ってもいいですか）。マレー語には て形がなく、素の動詞の前に «Boleh saya» を置きます。また「〜なくてもいい」の意味で «tidak boleh» と言いがちですが、それは «tidak perlu» です。',
]

CFG = dict(
    chapter=13, label='13', unit_id='ms-c13',
    menu_title='Chapter 13 · Health: may, need, should', genre='Health',
    prerequisite_units=['ms-c12b'], prereq_grammar=['ms-c12-g02', 'ms-c12-g03', 'ms-c11-g02', 'ms-c08-g02'],
    unit_goal='Ask permission, say what you need and what you have not yet done, understand advice and rules on signs and forms, and ask for clarification at a panel clinic and a pharmacy.',
    core=CORE,
    recognition=[],
    revision=[('Not, not yet and markers', REV_NOT), ('Health and the clinic', REV_HEALTH), ('Forms and the counter', REV_FORM),
              ('Signs and rules', REV_RULES), ('Asking and thanking', REV_ASK)],
    core_groups=[('Need, advice and rules', RULES), ('The panel clinic', CLINIC), ('The pharmacy', PHARMACY)],
    grammar_ids={'belum': 'ms-c13-g02', 'boleh': 'ms-c13-g03', 'perlu': 'ms-c13-g04', 'patut': 'ms-c13-g05', 'sign': 'ms-c13-g06',
                 'wajib': 'ms-c13-g07', 'words': 'ms-c13-g08'},
    grammar=['belum', 'boleh', 'perlu', 'patut', 'sign', 'wajib'], examples=EXAMPLES, vocab_opts=VOCAB_OPTS,
    card_range='the 25 cards ms-c13-001 to ms-c13-025', frame_list='ms-c13-f01 to f06', frame_list_ja='f01〜f06',
    extra=None,
    goals={'A': 'I can say what I have not done yet with «belum», ask permission with «Bolehkah saya …?» and say what I need with «perlu».',
           'B': 'I can register at a panel clinic, answer the receptionist and ask the doctor for sick leave.',
           'C': 'I can follow a call to a panel clinic, read a clinic notice and a message about sick leave, and ask a pharmacist to repeat an instruction.',
           'D': 'I can choose between «belum» and «tidak», and between «perlu», «patut» and «mesti», and correct a short sentence.',
           'E': 'I can handle a short role-play at a panel clinic and a pharmacy, including a change of time.'},
    goals_ja={'A': '«belum» でまだしていないことを言い、«Bolehkah saya …?» で許可を求め、«perlu» で必要なことを言える。',
              'B': 'パネルクリニックで受付をして受付係に答え、医者に病気休暇をお願いできる。',
              'C': 'パネルクリニックへの電話が分かり、クリニックの掲示と病気休暇のメッセージを読め、薬剤師に指示をもう一度言ってもらえる。',
              'D': '«belum» と «tidak»、«perlu»・«patut»・«mesti» を使い分け、短い文を直せる。',
              'E': 'パネルクリニックと薬局での短いロールプレイができ、時間の変更にも対応できる。'},
    setting='A weekday morning at a fictional panel clinic in Kuala Lumpur: «Encik» Tanaka has a fever and a sore throat, registers at the counter, sees the doctor and then asks the pharmacist to repeat an instruction. '
            'All names, clinics, times and rules are fictional; the unit gives no medical advice.',
    setting_ja='平日の朝、クアラルンプールの架空のパネルクリニック。田中さんは熱とのどの痛みがあり、受付をして医者に会い、そのあと薬剤師に指示をもう一度言ってもらいます。'
               '名前・クリニック・時刻・決まりはすべて架空で、このユニットは医学的な助言をしません。',
    recall=['Without notes, from chapters 2, 4 and 12: say «Boleh» + a question you could ask at a counter, one thing you have already done with «sudah» and one request with «Tolong» + a ‹-kan› verb. / '
            '第2章・第4章・第12章の復習：カウンターでできる «Boleh» の質問を一つ、«sudah» で済んだことを一つ、«Tolong» ＋ ‹-kan› の動詞の依頼を一つ言いましょう。',
            'Recall prompt: «Boleh …?» «Saya sudah …» «Tolong simpankan …»'],
    recall_key='e.g. «Boleh tunjukkan mesej itu?» «Saya sudah hantar fail itu.» «Tolong simpankan bungkusan ini.» Then show the new step: «belum» for not yet, «Bolehkah saya …?» for permission, and «perlu» for need.',
    patterns=P, pattern_ids=['ms-c13-f01', 'ms-c13-f02', 'ms-c13-f03', 'ms-c13-f04', 'ms-c13-f05', 'ms-c13-f06'],
    pattern_ids_note='Pattern IDs are the Kata-Kata chapter 13 frames f01 to f06 (pattern 5 shows f05 and f06 together, the two kinds of notice).',
    pattern_keys=['Pattern 1: «belum» + a verb. If a learner says «Saya tidak makan» for not yet, give the situation (I will eat later) and ask which word fits; «belum» is not yet, «tidak» is not. '
                  'Accept «Saya belum isi borang» (the Kata-Kata line) as the everyday form of «mengisi».',
                  'Pattern 2: «Bolehkah saya» or «Boleh saya» + the plain verb. Check that nothing comes between «saya» and the verb and that the answer is «Boleh.» or «Maaf, tidak boleh.» '
                  'Accept «Boleh saya …?» in speech.',
                  'Pattern 3: «perlu» + a verb. Check «tidak perlu» for not having to, and do not let «tidak boleh» stand in for it.',
                  'Pattern 4: «patut» for advice, «mesti» and «wajib» for must. Ask which strength fits: a step («perlu»), advice («patut») or a must («mesti»).',
                  'Pattern 5: «tidak dibenarkan» and «dilarang» on a sign, «tidak boleh» in speech, and «wajib diisi» on a form. Check the thing comes first with «diisi».'],
    dialogue=DIALOGUE, variant=VARIANT, gap_turns=(1, 3, 5, 7, 11, 13),
    drills={
        'repeat_frame': 'Frame: «Saya» [«belum» / «perlu»] [«mendaftar» / «berjumpa doktor» / «isi borang»].',
        'repeat': ['«Saya belum makan.»', '«Bolehkah saya masuk?»', '«Saya perlu berjumpa doktor.»', '«Encik patut berehat.»',
                   '«Tidak dibenarkan minum di sini.»', '«Borang ini wajib diisi.»', '«Encik perlu daftar dulu. Sila isi borang ini.»',
                   '«Dilarang makan dan minum di bilik menunggu.»'],
        'substitute': ['«Saya belum makan.» (cue: «mendaftar»)',
                       '«Bolehkah saya masuk?» (cue: «duduk», «di sini»)',
                       '«Saya perlu berjumpa doktor.» (cue: «bos»)',
                       '«Encik patut berehat.» (cue: «tanya bos»)',
                       '«Tidak dibenarkan minum di sini.» (cue: «ambil gambar»)',
                       '«Borang ini wajib diisi.» (cue: «borang kesihatan»)',
                       '«Awak mesti minta kebenaran bos.» (cue: «Encik Tanaka»)',
                       '«Saya belum isi borang.» (cue: «bayar»)'],
        'transform': ['Not yet («belum»): «Saya sudah mendaftar.»', 'Make a permission question with «Boleh saya»: «Saya masuk.»',
                      'Say you do not need to («tidak perlu»): «Saya perlu tunggu.»', 'Advice with «patut»: «Awak berehat.»',
                      'Standard to everyday: «Saya belum mengisi borang.»',
                      'Sign to speech («tidak boleh»): «Tidak dibenarkan minum di sini.»',
                      'Must on a form («wajib») and passive: «Isi borang ini.»', 'Change the answer to not yet («belum»): «Sudah. Saya sudah mendaftar.»'],
        'question and answer': ['«Ada temu janji?» (cue: «tidak ada»)', '«Encik sudah mendaftar?» (cue: «belum»)',
                                '«Boleh saya minum air di sini?» (cue: «maaf, tidak dibenarkan»)', '«Encik ada alahan?» (cue: «tidak ada»)',
                                'You hear: «Saya perlu daftar dulu.» Ask the question («di mana»).',
                                'You hear: «Cuti sakit satu hari daripada doktor.» Ask the question («berapa hari»).',
                                'You hear: «Borang ini wajib diisi.» Ask the question («yang mana»).',
                                'You hear: «Dos ada di label itu.» Ask the question («di mana»).'],
        'question-word choice': ['«___ sudah mendaftar?» → «Encik Tanaka.»', '«Saya perlu bawa ___?» → «Kad syarikat.»',
                                 '«Kaunter ___?» → «Di sebelah kiri.»', '«___ temu janji saya?» → «Pukul empat.»',
                                 '«___ tidak dibenarkan minum di sini?» → «Sebab ini bilik menunggu.»', '«Borang ___ wajib diisi?» → «Borang kesihatan.»',
                                 '«___ lama saya tunggu?» → «Setengah jam.»', '«Ini ___?» → «Ini klinik panel.»'],
    },
    drill_keys={
        'repeat': ['Read each line twice. «belum», «perlu» and «patut» go in front of the verb; «Bolehkah saya» goes in front of the plain verb; a sign says «tidak dibenarkan» or «dilarang».',
                   'Cover the line and say it from the English: I have not eaten yet; may I come in?; I need to see a doctor; you should rest; drinking is not allowed here; this form must be filled in; '
                   'you need to register first, please fill in this form; no eating or drinking in the waiting room.'],
        'substitute': ['1 «Saya belum mendaftar.» 2 «Bolehkah saya duduk di sini?» 3 «Saya perlu berjumpa bos.» 4 «Encik patut tanya bos.»',
                       '5 «Tidak dibenarkan ambil gambar di sini.» 6 «Borang kesihatan wajib diisi.» 7 «Encik Tanaka mesti minta kebenaran bos.» 8 «Saya belum bayar.»'],
        'transform': ['1 «Saya belum mendaftar.» 2 «Boleh saya masuk?» 3 «Saya tidak perlu tunggu.» 4 «Awak patut berehat.»',
                      '5 «Saya belum isi borang.» 6 «Tidak boleh minum di sini.» 7 «Borang ini wajib diisi.» 8 «Belum. Saya belum mendaftar.»'],
        'question and answer': ['1 «Tidak ada. Saya belum tempah.» 2 «Belum. Saya belum mendaftar.» 3 «Maaf, tidak dibenarkan minum di sini.» 4 «Tidak ada. Saya tidak ada alahan.»',
                                '5 «Daftar di mana?» 6 «Berapa hari cuti sakit daripada doktor?» 7 «Borang yang mana wajib diisi?» 8 «Dos ada di mana?»'],
        'question-word choice': ['1 «Siapa» 2 «apa» 3 «di mana» 4 «Pukul berapa» 5 «Kenapa» (also «Mengapa», «Apa sebab»; the answer starts with «sebab» or «kerana») 6 «yang mana» 7 «Berapa» 8 «apa»'],
    },
    short_dialogues=[
        ('Bolehkah saya masuk?', 'Boleh. Sila masuk.', 'at the doctor\'s door'),
        ('Encik sudah mendaftar?', 'Belum. Saya belum mendaftar.', 'at the counter'),
        ('Maaf, tidak dibenarkan minum di sini.', 'Oh, saya tidak tahu.', 'in the waiting room'),
        ('Maaf, saya tidak faham arahan itu.', 'Boleh. Baca arahan di label.', 'at the pharmacy')],
    short_keys=['1 «Terima kasih, doktor.» 2 «Baik. Di mana kaunter?»',
                '3 «Baik, saya faham. Terima kasih.» 4 «Baik. Terima kasih. Nanti saya tanya lagi.»'],
    markers=dict(
        title='Markers with the clinic verbs and «belum»', grammar='belum',
        instructions=['Say each sentence again with the marker in brackets. Keep the verb as the course teaches it (the meN- or ber- verb: «mendaftar», «mengisi», «berjumpa»); only the marker is added in front. / '
                      'かっこ内のマーカーを付けて言い直します。動詞はこのコースで教えた形（meN-・ber- の動詞：«mendaftar»・«mengisi»・«berjumpa»）のままで、前にマーカーを足すだけです。'],
        items=['«Saya mendaftar di klinik.» (marker: «sudah»)', '«Saya mengisi borang kesihatan.» (marker: «belum»)',
               '«Saya berjumpa doktor.» (marker: «sedang»)', '«Saya menelefon klinik.» (marker: «akan»)',
               '«Saya menunggu di bilik menunggu.» (marker: «masih»)', '«Penyambut tetamu memanggil nombor saya.» (marker: «baru»)',
               'Answer «Encik sudah mendaftar?» (marker: «belum»)', '«Saya berehat di rumah.» (marker: «akan»)'],
        bridge=['«sudah mendaftar» ≈ もう受付した · «belum mengisi» ≈ まだ記入していない · «sedang berjumpa» ≈ 診察を受けているところ · '
                '«akan menelefon» ≈ 電話する予定 · «masih menunggu» ≈ まだ待っている · «baru memanggil» ≈ 呼んだばかり',
                'Japanese changes the verb ending (登録した / 登録していない); Malay puts the marker in front and keeps the verb («mendaftar»). «belum» is まだ〜ていない, «sudah» is もう〜た. / '
                '日本語は動詞の語尾が変わります。マレー語はマーカーを前に置き、動詞（«mendaftar»）はそのままです。«belum» は「まだ〜ていない」、«sudah» は「もう〜た」です。'],
        key=['1 «Saya sudah mendaftar di klinik.» 2 «Saya belum mengisi borang kesihatan.» 3 «Saya sedang berjumpa doktor.» '
             '4 «Saya akan menelefon klinik.»',
             '5 «Saya masih menunggu di bilik menunggu.» 6 «Penyambut tetamu baru memanggil nombor saya.» 7 «Belum. Saya belum mendaftar.» '
             '8 «Saya akan berehat di rumah.»'],
        explain=('第4章の «sudah»・«belum»・«sedang»・«masih»・«akan»・«baru» を、第13章の動詞と組み合わせて言います。«belum» が「まだ〜ていない」です。',
                 'Combine the chapter 4 markers with the chapter 13 verbs: «belum» is not yet, and the verb does not change.')),
    question_note='Chapter 13 adds no new question word. The clinic sentences fit every question you know: «Siapa yang sudah mendaftar?», '
                  '«Saya perlu bawa apa?», «Kaunter di mana?», «Pukul berapa temu janji saya?», «Berapa lama saya tunggu?» / '
                  '第13章で新しい疑問語は増えません。クリニックの文は知っている疑問語すべてと使えます：'
                  '«Siapa yang sudah mendaftar?»、«Saya perlu bawa apa?»、«Kaunter di mana?»、«Pukul berapa temu janji saya?»、'
                  '«Berapa lama saya tunggu?»',
    question_tasks=['Ask what you need to bring. («apa»)', 'Ask who must register. («siapa»)',
                    'Ask where the counter is. («di mana»)', 'Ask formally whether the patient has an appointment. («Adakah»)',
                    'Ask politely whether you may sit here. («Bolehkah»)', 'Ask how many forms there are. («berapa»)',
                    'Ask when the clinic closes. («bila»)', 'Ask what time the appointment is. («pukul berapa»)',
                    'Ask on what day the clinic is closed. («hari apa»)', 'Ask how you register. («bagaimana»; spoken «macam mana»)',
                    'Ask why drinking is not allowed. («kenapa»; also «mengapa» or «apa sebab»; the answer starts with «sebab» or «kerana»)',
                    'Ask which form is compulsory. («yang mana»)', 'Ask where you go after registering. («ke mana»)',
                    'Ask where this card is from. («dari mana»)', 'Ask how far the pharmacy is. («berapa jauh»)',
                    'Ask how long you wait. («berapa lama»)', 'Ask how many chairs are in the waiting room. («berapa» with a counter)',
                    'Ask who filled in the form. («siapa» with «oleh»)'],
    question_keys=['1 «Saya perlu bawa apa?» 2 «Siapa yang perlu mendaftar?» 3 «Kaunter di mana?»',
                   '4 «Adakah encik ada temu janji?» 5 «Bolehkah saya duduk di sini?» 6 «Ada berapa borang?»',
                   '7 «Bila klinik tutup?» 8 «Pukul berapa temu janji saya?» 9 «Pada hari apa klinik tutup?»',
                   '10 «Bagaimana saya mendaftar?» (spoken: «Macam mana saya mendaftar?») 11 «Kenapa tidak dibenarkan minum di sini?» / '
                   '«Mengapa …?» / «Apa sebab …?» «Sebab ini bilik menunggu.» / «Kerana ini bilik menunggu.»',
                   '12 «Borang yang mana wajib diisi?» 13 «Saya pergi ke mana selepas mendaftar?» 14 «Kad ini dari mana?»',
                   '15 «Berapa jauh farmasi?» 16 «Berapa lama saya tunggu?» 17 «Ada berapa buah kerusi di bilik menunggu?»',
                   '18 «Borang ini diisi oleh siapa?»'],
    listening=LISTENING,
    listening_context='In the morning «Cik» Mei Ling telephones a panel clinic, then speaks to a pharmacist. / 朝、メイリンさんがパネルクリニックに電話し、そのあと薬剤師と話します。',
    listening_before=['Predict: which of «belum», «perlu», «patut», «mesti», «boleh» and «dilarang» will you hear? Write three guesses. / «belum»・«perlu»・«patut»・«mesti»・«boleh»・«dilarang» のうち聞こえそうなものを三つ予想しましょう。',
                      'Read the nine questions below before the first listening. / 1回目の前に下の9つの質問を読みます。'],
    listen_questions=['What does Mei Ling ask at the start?', 'What must she do first, according to the receptionist?', 'What time is the slot?',
                      'What must she bring?', 'Whose permission has she not asked for yet?', 'Why can she not eat in the waiting room?',
                      'Where can she wait instead?', 'What does she ask at the pharmacy?', 'What does the pharmacist tell her to read?'],
    listen_answers=['whether she can see the doctor today', 'register', 'four in the afternoon', 'a company card', 'her boss\'s',
                    'eating is forbidden there', 'outside', 'to say it once more, because she does not understand the instruction', 'the instructions on the label'],
    listening_after=['Compare answers, then shadow lines 2, 5 and 8 after the teacher. / 答えを比べ、2・5・8行目をシャドーイングします。',
                     'Tell your partner in four sentences what you must do before a visit to a clinic, with «perlu», «mesti» and «belum». / クリニックに行く前にしなければならないことを、«perlu»・«mesti»・«belum» を使って4文でパートナーに話しましょう。'],
    test_listen=[(0, 'whether she can see the doctor today', ['bolehkah', 'berjumpa', 'doktor']),
                 (1, 'register', ['perlu', 'mendaftar']),
                 (3, 'a company card', ['perlu', 'bawa', 'kad']),
                 (4, 'her boss\'s permission', ['belum', 'kebenaran', 'bos']),
                 (7, 'eating is forbidden in the waiting room', ['dilarang', 'makan', 'menunggu']),
                 (10, 'read the instructions on the label', ['mesti', 'baca', 'arahan'])],
    test_listen_prompts=['What does Mei Ling ask at the start?', 'What must she do first?', 'What must she bring?',
                         'What has she not yet asked for?', 'Why can she not eat in the waiting room?', 'What does the pharmacist tell her to do?'],
    reading_title='Reading and writing · A clinic notice and a message about sick leave',
    reading=['Fictional notice at a panel clinic and message from a boss (all names are invented):',
             '«KLINIK PANEL. Sila daftar di kaunter. Untuk rawatan, tunjukkan kad syarikat. Borang kesihatan wajib diisi. Dilarang makan dan minum di bilik menunggu. Tidak dibenarkan ambil gambar. Bila perlu, tanya penyambut tetamu.»',
             '«Encik Tanaka, terima kasih atas mesej itu. Cuti sakit satu hari daripada doktor. Awak tidak perlu datang ke pejabat esok. Awak patut berehat di rumah. Hubungi saya bila perlu.»',
             'Sign in the clinic corridor: «Pintu kecemasan ada di sebelah kiri. Sila jangan bising.»'],
    read_questions=['Where do you register?', 'Which form is compulsory?', 'What is forbidden in the waiting room?', 'What is not allowed?',
                    'How many days of sick leave did the doctor give?', 'Does Tanaka have to come to the office tomorrow?',
                    'Where is the emergency door?', 'Say in Malay: "May I come in?"'],
    read_answers=['at the counter', 'the health form', 'eating and drinking', 'taking photographs', 'one day', 'no',
                  'on the left', '«Bolehkah saya masuk?»'],
    write_instruction='Write four or five sentences to your boss: say that you saw the doctor, that you have sick leave, that you do not need to come to the office and what you will do. / '
                      '上司にあてて4〜5文を書きましょう：医者に会ったこと、病気休暇があること、出社しなくてよいこと、これからすることを書きます。',
    write_model='«Selamat pagi, bos. Saya berjumpa doktor pagi ini. Cuti sakit satu hari daripada doktor. Saya tidak perlu datang ke pejabat esok. Saya akan menghubungi bos hari Isnin. Terima kasih.»',
    writing_type='message',
    task_title='Task · Register at the clinic and ask the pharmacist to repeat',
    role_a=['Your information (fictional): you are the receptionist, and later the pharmacist. The patient has no appointment and has not registered. The form is compulsory. Drinking is not allowed in the waiting room.',
            'As the receptionist: ask about an appointment, say the patient must register and fill in the form, and answer the permission questions. As the pharmacist: if B does not understand the instruction, '
            'point to the label and say to ask you again. Do not name any medicine, any dose or any time to take it.',
            'Aの情報（架空）：あなたは受付係で、あとで薬剤師にもなります。患者は予約がなく、まだ受付をしていません。用紙は必須で、待合室では飲んではいけません。'
            '受付係として予約をたずね、受付をして用紙に記入するよう言い、許可の質問に答えます。薬剤師としては、Bが指示を分からないときにラベルを指して、もう一度聞くように言います。薬の名前・用量・飲む時間は言いません。'],
    role_b=['You are the patient (fictional). You have a fever and a sore throat and no appointment. Register, ask whether you may fill in the form here and whether you may drink water.',
            'At the pharmacy you do not understand the instruction: ask the pharmacist to say it once more, then say you will read the label.',
            'Bは患者です（架空）。熱とのどの痛みがあり、予約はありません。受付をし、ここで用紙に記入してよいか、水を飲んでよいかをたずねます。'
            '薬局では指示が分からないので、薬剤師にもう一度言ってもらい、ラベルを読むと言います。'],
    change=['Halfway, A says: «Maaf, doktor belum ada. Encik boleh tunggu, atau datang pukul empat. Sesuai?» B decides, says what is suitable and asks whether B may leave a bag here: «Pukul empat sesuai. Boleh saya letak beg di sini?»',
            '途中でAが «Maaf, doktor belum ada. Encik boleh tunggu, atau datang pukul empat. Sesuai?» と言います。Bは決めて、都合のよい時間を言い、ここにかばんを置いてよいかをたずねます：«Pukul empat sesuai. Boleh saya letak beg di sini?»'],
    success=['☐ B says what has not been done yet with «belum» and what B needs with «perlu».',
             '☐ B asks permission twice with «Bolehkah saya …?» or «Boleh saya …?».',
             '☐ At the pharmacy B asks for the instruction again and A only points to the label; after the change B says the time suits.'],
    task_key='«Selamat pagi, encik. Ada temu janji?» — «Tidak ada. Saya demam dan sakit tekak. Saya batuk juga.» — «Encik perlu daftar dulu. Sila isi borang ini.» — '
             '«Baik. Saya belum isi borang. Bolehkah saya isi borang di sini?» — «Boleh. Ini klinik panel syarikat encik?» — «Ya. Boleh saya minum air di sini?» — '
             '«Maaf, tidak dibenarkan minum di sini. Dilarang makan dan minum di bilik menunggu.» — The pharmacy: «Maaf, boleh cakap lagi sekali? Saya tidak faham arahan itu.» — '
             '«Boleh. Encik mesti baca arahan di label. Dos ada di label itu.» — «Baik, saya baca label itu. Terima kasih.» — «Sama-sama. Kalau ada soalan, tanya saya lagi.» — '
             'Change: «Maaf, doktor belum ada. Encik boleh tunggu, atau datang pukul empat. Sesuai?» — «Pukul empat sesuai. Boleh saya letak beg di sini?»',
    culture=CULTURE, culture_ja=CULTURE_JA,
    culture_sources='Kata-Kata chapter 13 card notes ms-c13-001 to -003 («perlu», «patut», «wajib»; «mesti» is a root, card -021), -004 («dibenarkan» is ‹di-› + ‹benar› + ‹-kan›, the opposite of «dilarang»), '
                    '-005 («kebenaran» taught only as permission), -012 («dos» for reading a label only), -023 to -025 («daftar», «cuti sakit / MC» with spoken «MC», «mendaftar»); stage 2 plan sections 2 and 3 and the chapter 13 row '
                    '(no diagnosis and no dosage advice; «wajib» is secular). The sentence on panel clinics and sick leave is general knowledge of working in Malaysia, labelled as such and not source-checked; '
                    'the note states no figure or rule.',
    culture_prompt='In Japanese, how do you ask permission (〜てもいいですか) and say that something is advice or a must (〜たほうがいい, 〜なければならない)? Which Malay word fits each?',
    culture_explain=('必要・助言・義務の強さの違い、掲示と話し言葉、許可の求め方、パネルクリニックと病気休暇の一般的な知識を読みます。日本語は未監修です。',
                     'Read about the difference between need, advice and must, signs against speech, how to ask permission, and the general custom of panel clinics and sick leave.'),
    quiz_words=['L-1185', 'L-1186', 'L-1187', 'L-1199', 'L-1188', 'L-1191'],
    quiz_meanings=['need, necessary', 'should, advisable', 'compulsory', 'must', 'allowed', 'pharmacy'],
    grammar_quiz=[('Say in Malay: "I haven\'t registered yet."', '«Saya belum mendaftar.»', ['belum', 'mendaftar']),
                  ('Say in Malay: "May I come in?"', '«Bolehkah saya masuk?»', ['bolehkah', 'masuk']),
                  ('Write the sign: "No eating or drinking in the waiting room."', '«Dilarang makan dan minum di bilik menunggu.»', ['dilarang', 'menunggu']),
                  ('Say in Malay to a man: "You should rest."', '«Encik patut berehat.»', ['patut', 'berehat'])],
    test_reading=['Fictional notice at another panel clinic: «KLINIK PANEL. Sila daftar dulu. Borang kesihatan wajib diisi. Tidak dibenarkan minum di bilik menunggu. '
                  'Bila perlu, tanya penyambut tetamu.»'],
    reading_quiz=[('What must you do first?', 'register', ['daftar']),
                  ('Which form must be filled in?', 'the health form', ['borang', 'kesihatan', 'wajib']),
                  ('What is not allowed in the waiting room?', 'drinking', ['dibenarkan', 'minum']),
                  ('Whom do you ask when you need to?', 'the receptionist', ['bila perlu', 'penyambut tetamu'])],
    speaking_test='At the clinic counter: say you have not registered yet («belum»), say what you need to do («perlu»), ask permission twice («Bolehkah saya …?») and ask the pharmacist to say an instruction once more.',
    speaking_key='Check: «belum» + a verb for not yet (not «tidak»); «perlu» + a verb; «Bolehkah saya» or «Boleh saya» + the plain verb with nothing in between; and «Maaf, boleh cakap lagi sekali?» '
                 'for the pharmacist. The unit scores the language only: no medicine, dose or advice is needed or marked. Accept «daftar» and «isi borang» in speech.',
    speaking_words=['belum', 'perlu', 'bolehkah', 'mendaftar', 'arahan'],
    plan={'A_recall': 'chapters 2, 4 and 12 («Boleh …?», «sudah», «Tolong» + a ‹-kan› verb) from the opener prompts.',
          'A_patterns': 'patterns 1 and 2 first («belum», «Bolehkah saya …?»), question and answer before the rule; then the vocabulary in three groups with each whole word and its root '
                        '(need, advice and rules 10, the panel clinic 11, the pharmacy 4). Draw the ladder «perlu» (a step), «patut» (advice), «mesti» / «wajib» (must) and the pair «tidak perlu» against «tidak boleh».',
          'B_recall': 'say one thing you have not done yet with «belum» and one permission question.',
          'B_drills': 'pattern table, substitution, transformation («sudah» to «belum» first), question and answer, question-word choice, '
                      'short dialogues, then the markers drill.',
          'C_recall': 'each learner says one thing they must do before a visit to a clinic.',
          'D_review': 'cumulative question-word drill (chapters 1 to 13), then the markers drill with new cues and a check of «belum» against «tidak» and «perlu» against «patut».',
          'D_preview': 'unit 14: reasons, conditions and sequence (Kata-Kata c14 cards ms-c14-001 onward and its frames).',
          'E_recall': 'say three permission questions you could ask in a clinic.',
          'E_listening': 'read the Kata-Kata scenario lines ms-c13-s01 to ms-c13-s18 (Tanaka at the panel clinic, with the doctor and at the pharmacy) twice; '
                         'learners tick «belum», «perlu», «patut», «mesti», «dibenarkan» and «dilarang» when they hear them.',
          'E_roleplay': 'pairs play the same scene with their own fictional symptom, form and name, without the script; A never names a medicine or a dose.',
          'E_variation': 'a changed time: the doctor is not in yet; B chooses to wait or to come at four, says the time suits and asks permission to leave a bag.'},
    hanashishou_note='Hanashishou (Stage 2): the plan links chapter 13 to the clinic scenes (clinic_visit, pharmacy_advice, clinic_registration). '
                     'Their Malay is not yet tagged by chapter (build step 6), so do not assign them yet.',
    next_note='Next: unit 14 (reasons, conditions and sequence; Kata-Kata c14), with its writing block.',
    teacher_notes=['Load: 25 core words in three groups (need, advice and rules 10; the panel clinic 11; the pharmacy 4), no recognition word, and revision of not and not yet, health and the clinic, forms and the counter, '
                   'signs and rules, and asking and thanking. Suggested order: Block A the first group with patterns 1 to 3; Block B the second group with patterns 4 and 5; the third group in Block B or C. '
                   'If the pilot shows 25 is too many, the natural cut is: «perlu», «patut», «mesti», «wajib», «dibenarkan», «daftar», «mendaftar», «temu janji», «klinik panel», «cuti sakit» first; the rest second.',
                   'Safety (read first): the unit writes no diagnosis, no treatment advice, no medicine name with a dose and no dosing instruction. The doctor only says «patut berehat» and gives sick leave; the pharmacist only '
                   'points to the label and says «tanya saya lagi». «dos» is taught for reading a label. Tell learners to follow their own doctor and pharmacist, and do not answer medical questions in class. '
                   'Use fictional names and symptoms; assess the language, not medical knowledge.',
                   '«belum» against «tidak»: «belum» is not yet (it will happen); «tidak» is not, a plain no; «bukan» is for nouns. «Saya belum makan» means I have not eaten yet; «Saya tidak makan» means I do not eat. '
                   'The answer to «Sudah …?» is «Sudah.» or «Belum.», not «Tidak.» The verb does not change after «belum».',
                   '«perlu» (need: a step) against «patut» (should: advice, you choose) against «mesti» or «wajib» (must: no choice; «wajib» is secular here, on forms and notices, with no reference to religion). '
                   '«tidak perlu» is not having to; «tidak boleh» is not allowed; «jangan» is a command; «dilarang» and «tidak dibenarkan» are for signs. «mesti» is a root, not ‹me-› + ‹sti› (card ms-c13-021). '
                   '«kebenaran» is permission only (card ms-c13-005); the other meaning is not taught.',
                   'Where Japanese learners usually slip: (1) asking permission with the て-form idea (入ってもいいですか): there is no て-form, say «Boleh saya masuk?»; (2) «tidak boleh» for 〜なくてもいい (it is «tidak perlu»); '
                   '(3) «patut» or «mesti» for every 〜ほうがいい or 〜なければならない: «patut» is advice, «mesti» an order; (4) «tidak» for まだ〜ていない (it is «belum»); (5) a particle or a word for "to" between «saya» and the verb; '
                   '(6) putting the sentence-final particles of speech into an answer: they are recognition only, never in a key.',
                   'Panel clinics and «cuti sakit» / «MC» (general knowledge, not a rule and not source-checked; no figure): many Malaysian employers have an agreement with a panel clinic, and a doctor may give sick leave, '
                   'called «cuti sakit» or, in speech, «MC». Employers differ, so tell learners to ask their own company.',
                   'The ‹-kan› rule from chapter 12 (Sam): «Tolong elakkan …» is a request, so the bare ‹-kan› verb is right. No ‹meN-› + ‹-kan› form is taught. Standard first: «mendaftar» in careful speech and writing, «daftar» and «isi borang» in everyday speech; '
                   'the course teaches «mendaftar» first and never marks the everyday form wrong. «MC» is spoken, recognition only, never in a key.',
                   'Natural speech: «Boleh saya …?» and «tidak boleh» in conversation; «tidak dibenarkan», «dilarang» and «wajib diisi» on signs and forms. Keep «ialah», «di-» … «oleh» and rulings out of casual turns. '
                   'The scene follows Kata-Kata c13 (scenario lines ms-c13-s01 to s18, frames f01 to f06). All names, clinics and times are fictional; learners may use an invented clinic.',
                   'Cumulative question words: chapters 1 to 13. Chapter 13 adds no new question word.'],
)

UNIT = unit_dict(CFG)
