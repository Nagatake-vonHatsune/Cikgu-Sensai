"""Stage 2 (Malay A2) close: the A2 stage test (blocks 18C and 18D of chapter 18) and the Stage 2 record.

The A2 stage test mirrors the A1 stage test (suite/stage1.py): tasks with real outcomes in four sections (listening, reading,
writing, speaking), 20 marks each, in two parallel versions (suite/stage2_test_a.py and stage2_test_b.py), with the listening
scripts, the administration sheet (timing, materials, scoring, the pass rule and the item map) and the Stage 2 record for the
catalogue (CEFR A2, the completion label, the hours check). The review and rehearsal blocks 18A and 18B and the feedback
block 18E are unit 18 (suite/ms_c18.py).

Sam's decisions (docs/stage-2-decisions.md, 13 Nov 2026): A1, the A2 test is like the A1 test: versions A and B, four
sections of 20 marks, pass 48 of 80 with at least 10 of 20 in each, writing items allowed; A2, two compulsory speaking cards,
a request (chapter 12) and a mishap report (chapter 16); A3, about 7 minutes a learner, six learners per examiner per block,
each further six learners adds a block outside the 67; A4, the local completion label "Malay A2 · Stage 2 complete", not a
certificate. The charter gives no A2 pass rule: the rule is Sam's decision A1, carried over from Stage 1, and it is not a
validated CEFR cut score.

Assessment rules (plan section 3 and 4): standard production is always accepted; spoken forms are recognised, never
required; «lah» and «kan» are never required in any key; writing keys accept and list natural variants (kalau / jika,
kerana / sebab, kemudian / selepas itu). Only ledger words placed in chapters 1 to 17 are used; the practice-pool rows
L-1304 to L-1309 and the recognition rows («pindah», «tukar», «deadline», «nombor tracking») are never tested. All names,
places, prices, numbers and times are fictional. All Japanese is a draft awaiting native review.
"""

from .stage2_test_a import VERSION as VERSION_A
from .stage2_test_b import VERSION as VERSION_B

UNIT_ID = 'ms-stage2'
CHAPTERS = [f'ms-c{n:02}' for n in range(10, 19)]
TESTED = list(range(10, 18))
FOCUS = {n: f'ms-c{n:02}-g01' for n in range(1, 19)}

# The charter's Stage 2 chapter goals as the catalogue states them (catalogue.GOALS, chapters 10 to 17).
CHARTER_GOALS = {
    10: 'Retell your day and your background in full sentences',
    11: 'Say who did what at the office, check a draft and a deadline, and say your weekend plan',
    12: 'Ask for a favour, collect a parcel, and report a problem such as a leak to the management office',
    13: 'Say what is not done yet, ask permission, say what you need and understand advice and rules at a clinic and a pharmacy',
    14: 'Give a reason, a condition, a purpose and a contrast, put a plan in order, and put off or cancel a plan with a reason',
    15: 'Say that something is lost, describe a thing or a person with «yang», colour, shape and what they wear, and say which one',
    16: 'Say what happened by accident with ter-, apologise for a small slip, report a locked door, a spill or a minor fall in plain facts, and keep ter- (the most) apart from ter- (by accident)',
    17: 'Understand and use the taught spoken forms with friends and colleagues, write the standard forms, recognise ‹lah› and ‹kan›, and invite, accept or decline politely with a reason or another time',
}
# The Stage 2 can-do review (block 18E): the plan's learner-facing goals (section 4), each split into the checks a learner ticks.
CANDO = {
    10: [('I can describe my usual working day in four to six connected sentences, with times («Setiap pagi saya bertolak pukul …»).',
          '普段の仕事の日を、時刻を入れて4〜6文のつながった文で話せる（«Setiap pagi saya bertolak pukul …»）。'),
         ('I can give my background («berasal dari», «bekerja di», «sudah / belum berkahwin») and answer two follow-up questions.',
          '自分の背景（«berasal dari»・«bekerja di»・«sudah / belum berkahwin»）を言い、追加の質問二つに答えられる。')],
    11: [('I can say who does an office task with a meN- verb, and ask «Siapa yang …?».',
          '職場の作業を誰がするかを meN- の動詞で言い、«Siapa yang …?» とたずねられる。'),
         ('I can switch between the active and the «di-» passive for the same task («Rahman menulis draf itu» / «Draf itu ditulis oleh Rahman»).',
          '同じ作業を能動文と «di-» の受け身で言い換えられる（«Rahman menulis draf itu» / «Draf itu ditulis oleh Rahman»）。')],
    12: [('I can make a clear request about a parcel or a repair with ‹-kan› or ‹-i› («Tolong simpankan …», «Boleh hubungi …?»).',
          '荷物や修理について、‹-kan›・‹-i› を使って明確に頼める（«Tolong simpankan …»・«Boleh hubungi …?»）。'),
         ('I can give the place and the time and confirm the agreed next step.', '場所と時間を伝え、合意した次の対応を確認できる。')],
    13: [('I can ask permission («Bolehkah saya …?») and say what I need («Saya perlu …»).',
          '許可を求め（«Bolehkah saya …?»）、必要なことを言える（«Saya perlu …»）。'),
         ('I can tell a rule («wajib», «tidak dibenarkan») from advice («patut») and from "not yet" («belum»).',
          '規則（«wajib»・«tidak dibenarkan»）を助言（«patut»）や「まだ」（«belum»）と区別できる。')],
    14: [('I can give a reason and set one condition («kerana», «kalau»).', '理由を述べ、条件を一つ示せる（«kerana»・«kalau»）。'),
         ('I can describe three steps of a plan («mula-mula», «kemudian», «akhirnya») and put off a plan with «tangguhkan».',
          '計画の三つの手順を言い（«mula-mula»・«kemudian»・«akhirnya»）、«tangguhkan» で予定を延期できる。')],
    15: [('I can say something is lost and describe it with two useful details and a short «yang» clause.',
          '物をなくしたと言い、役に立つ特徴二つと短い «yang» の節で説明できる。'),
         ('I can ask a question that tells it from another one («Yang mana satu?»).', '別のものと区別する質問ができる（«Yang mana satu?»）。')],
    16: [('I can explain a small mishap with ‹ter-› (what happened and where) and apologise when it is my fault.',
          '小さなトラブルを ‹ter-› で説明し（何がどこで起きたか）、自分のせいならあやまれる。'),
         ('I can ask for one practical next step, and I keep ‹ter-› "by accident" apart from ‹ter-› "the most".',
          '具体的な次の対応を一つ頼め、「うっかり」の ‹ter-› と「いちばん」の ‹ter-› を区別できる。')],
    17: [('I can invite with «Sudikah …?», and accept or decline with a reason or another time («Sayangnya …», «Bagaimana kalau …?»).',
          '«Sudikah …?» で誘い、理由や別の機会を添えて受けたり断ったりできる（«Sayangnya …»・«Bagaimana kalau …?»）。'),
         ('I can understand the taught spoken forms, choose standard or spoken Malay for the person, and recognise «lah» and «kan».',
          '学んだ話し言葉を聞いて分かり、相手に合わせて標準形か話し言葉を選べ、«lah» と «kan» を聞き取れる。')],
}

SECTION_MARKS = 20
TIMING = {'listening': 12, 'reading': 15, 'writing': 18, 'speaking': 7}
# Sam's decision A2 (13 Nov 2026): a request card (chapter 12) and a mishap card (chapter 16) are compulsory. Each has two
# parallel cards, so the examiner can change the card from learner to learner: one request card (1 or 2) and one mishap card
# (3 or 4) are always used.
COMPULSORY_PAIRS = {'request (chapter 12)': (1, 2), 'mishap report (chapter 16)': (3, 4)}
TEST_GOALS = {
    'listening': ('I can understand announcements and everyday conversations about routines, office tasks, parcels, clinics, '
                  'mishaps and invitations, and note the facts I need.',
                  '日課、職場の作業、荷物、クリニック、トラブル、招待についてのお知らせや日常会話を聞いて分かり、必要な情報を書き取れる。'),
    'reading': ('I can read a notice, a message, a form, an invitation and a short incident note, and act on them.',
                '掲示、メッセージ、届け、招待、短い事故のメモを読んで、その内容どおりに行動できる。'),
    'writing': ('I can fill in a lost-property form and write a short message that explains and rearranges a plan.',
                '遺失物の届けに記入し、予定の説明と変更を伝える短いメッセージを書ける。'),
    'speaking': ('I can introduce myself and my working day, answer an invitation, make a request and report a small mishap, '
                 'including a change of plan.',
                 '自己紹介と仕事の一日を話し、招待に答え、依頼をし、小さなトラブルを報告でき、予定変更にも対応できる。'),
}
PASS_TOTAL, PASS_SECTION, TOTAL = 48, 10, 4 * SECTION_MARKS
PASS_STATUS = "Sam's decision A1 (docs/stage-2-decisions.md, 13 Nov 2026): the Stage 1 rule carried over; the charter gives no A2 rule"
COMPLETION_LABEL = 'Malay A2 · Stage 2 complete'

# The Stage 2 hours check (plan section 1): 11 teaching units of five blocks, three review blocks, four writing blocks and the
# five chapter 18 blocks. Every block is 45 minutes.
HOURS = dict(teaching_units=55, reviews=3, writing=4, chapter18=5)
TOTAL_BLOCKS = sum(HOURS.values())
TOTAL_HOURS = TOTAL_BLOCKS * 45 / 60


def _marks(n):
    return f'[{n} mark{"s" if n != 1 else ""}]'


def _test_item(code, sub, it):
    return dict(sub_type=sub, prompt=f'{code}. {it["q"]} / {it["ja"]} {_marks(it["marks"])}',
                answer=it['a'], words=it['words'], grammar=[FOCUS[c] for c in sorted(set(it['ch']))])


def _items(v):
    """[(code, sub_type, item)] for one version, in paper order."""
    out = []
    n = 0
    for task in v['listening']:
        for it in task['items']:
            n += 1; out.append((f'{v["label"]}-L{n}', 'listening', it))
    n = 0
    for part in v['reading']:
        for it in part['items']:
            n += 1; out.append((f'{v["label"]}-R{n}', 'reading', it))
    for n, part in enumerate(v['writing'], 1):
        out.append((f'{v["label"]}-W{n}', 'writing', part['items'][0]))
    out.append((f'{v["label"]}-S1', 'speaking', v['speaking']['intro']))
    for n, card in enumerate(v['speaking']['cards'], 1):
        out.append((f'{v["label"]}-S2.{n}', 'speaking', card))
    return out


def item_map(version):
    """[(item code, sub_type, marks, chapters)] for one version, in paper order (the Stage 1 shape)."""
    return [(code, sub, it['marks'], it['ch']) for code, sub, it in _items(version)]


def item_frames(version):
    """{item code: [Kata-Kata frame IDs the item tests]}."""
    return {code: it['frames'] for code, _, it in _items(version)}


def item_words(version):
    """{item code: [ledger headwords the item tests]}."""
    return {code: it['words'] for code, _, it in _items(version)}


def compulsory_codes(version):
    """{function: [the two parallel card codes]}: one card of each pair is always used."""
    return {name: [f'{version["label"]}-S2.{c}' for c in cards] for name, cards in COMPULSORY_PAIRS.items()}


def _chapters(ch):
    return ', '.join(str(c) for c in sorted(set(ch)))


def test_components(v):
    V = v['label']; low = V.lower(); out = []
    fiction = ('All names, shops, prices, times, units and places are fictional.', '名前、店、値段、時刻、部屋番号、場所はすべて架空です。')
    rules = {'listening': (f'Version {V}. Answer in English or Japanese unless a question asks for Malay. {fiction[0]} / '
                           f'バージョン{V}。マレー語で書くよう指示がある問題以外は、英語か日本語で答えます。{fiction[1]}'),
             'writing': f'Version {V}. Write in Malay. {fiction[0]} / バージョン{V}。マレー語で書きます。{fiction[1]}',
             'speaking': f'Version {V}. Speak in Malay. {fiction[0]} / バージョン{V}。マレー語で話します。{fiction[1]}'}
    rules['reading'] = rules['listening']

    def comp(slug, sub, title, minutes, sections, key, explain, tests, skills, block):
        goal, goal_ja = TEST_GOALS[sub]
        sections = [('Can-do and instructions · できることと指示', [f'Can-do: {goal} / {goal_ja}', rules[sub]] + sections[0][1])] + sections[1:]
        out.append(dict(slug=f'test-{low}-{slug}', type='Test', title=f'A2 stage test · Version {V} · {title}', block=block,
                        minutes=minutes, sections=sections, key=key + [
                            f'Section total: {SECTION_MARKS} marks. The pass rule and the item map are on the administration sheet. '
                            'Standard Malay is always accepted; spoken forms are accepted where the meaning is clear but are never required; '
                            '‹lah› and ‹kan› are never required.'],
                        explain=explain, sub_type=sub, tests=tests, patterns=sorted({f for code, s, it in _items(v) if s == sub for f in it['frames']}),
                        grammar=[FOCUS[n] for n in TESTED], goal=goal, skills=skills))

    # Listening
    sections = [('Before you listen', [f'{TIMING["listening"]} minutes, {SECTION_MARKS} marks. The teacher reads each text twice. '
                                       'Read the questions first. / 12分、20点。先生が各文を2回読みます。先に質問を読みましょう。'])]
    tests, key, n = [], [], 0
    for t, task in enumerate(v['listening'], 1):
        lines = [task['context']]
        key.append(f'Task {t} · {task["title"]} · the teacher reads twice:')
        key.extend(f'{sp}: «{line}»' for sp, line in task['script'])
        for it in task['items']:
            n += 1; code = f'L{n}'
            item = _test_item(code, 'listening', it); tests.append(item)
            lines.append(item['prompt']); lines.append('________________________________________')
            key.append(f'{code}: {it["a"]}')
        sections.append((f'Task {t} · {task["title"]}', lines))
    comp('listening', 'listening', 'Listening', TIMING['listening'], sections, key,
         ('A2 段階テストの聞く問題です（ブロック18C）。先生が台本を2回読みます。台本は先生用キーにあります。日本語は未監修です。',
          'The listening paper of the A2 stage test (block 18C). The teacher reads each script twice; the scripts are in the teacher key.'),
         tests, ['listening'], '18C')

    # Reading
    sections = [('Before you read', [f'{TIMING["reading"]} minutes, {SECTION_MARKS} marks. / 15分、20点。'])]
    tests, key, n = [], [], 0
    for t, part in enumerate(v['reading'], 1):
        lines = list(part['text'])
        for it in part['items']:
            n += 1; code = f'R{n}'
            item = _test_item(code, 'reading', it); tests.append(item)
            lines.append(item['prompt']); lines.append('________________________________________')
            key.append(f'{code}: {it["a"]}')
        sections.append((f'Part {t} · {part["title"]}', lines))
    comp('reading', 'reading', 'Reading', TIMING['reading'], sections, key,
         ('A2 段階テストの読む問題です（ブロック18C）：掲示、メッセージ、届け、招待、事故のメモ。日本語は未監修です。',
          'The reading paper of the A2 stage test (block 18C): a notice, a message, a form, an invitation and an incident note.'),
         tests, ['reading'], '18C')

    # Writing
    sections = [('Before you write', [f'{TIMING["writing"]} minutes, {SECTION_MARKS} marks. / 18分、20点。'])]
    tests, key = [], []
    for t, part in enumerate(v['writing'], 1):
        code = f'W{t}'
        it = part['items'][0]
        item = _test_item(code, 'writing', it); tests.append(item)
        lines = [part['intro'], item['prompt']]
        lines += [f'{field}: ______________________' for field in part['form'][1:]] if part['form'] else [
            '________________________________________'] * 6
        if part['form']:
            lines.insert(1, part['form'][0])
        key.append(f'{code}: {it["a"]}')
        sections.append((f'Part {t} · {part["title"]}', lines))
    comp('writing', 'writing', 'Writing', TIMING['writing'], sections, key,
         ('A2 段階テストの書く問題です（ブロック18C）：遺失物の届けと予定変更のメッセージ。採点基準は先生用キーにあります。日本語は未監修です。',
          'The writing paper of the A2 stage test (block 18C): a lost-property form and a message that rearranges a plan. The '
          'marking rubric and the accepted variants are in the teacher key.'),
         tests, ['writing'], '18C')

    # Speaking
    sp = v['speaking']
    tests, key = [], []
    intro = _test_item('S1', 'speaking', sp['intro']); tests.append(intro)
    sections = [('Before you speak', [
        f'About {TIMING["speaking"]} minutes for each learner, {SECTION_MARKS} marks: the self-introduction and invitation (8) and two '
        'role-play cards (6 each). One request card (card 1 or 2) and one mishap card (card 3 or 4) are always used. / '
        '一人約7分、20点：自己紹介と招待への返事（8点）とロールカード二枚（各6点）。依頼のカード（1か2）とトラブルのカード（3か4）を必ず一枚ずつ使います。']),
        ('Part 1 · Self-introduction and an invitation · 自己紹介と招待', [intro['prompt']])]
    key.append('S1 examiner: ' + ' '.join(sp['intro']['examiner']))
    key.append('S1 rubric (8): ' + sp['intro']['a'])
    cards = []
    pair_of = {c: name for name, pair in COMPULSORY_PAIRS.items() for c in pair}
    for c, card in enumerate(sp['cards'], 1):
        code = f'S2.{c}'
        it = dict(q=f'{card["title"]}: ' + ' '.join(f'({i}) {x}' for i, x in enumerate(card['tasks'], 1)),
                  ja=f'{card["ja_title"]}：' + ''.join(f'（{i}）{x}' for i, x in enumerate(card['tasks_ja'], 1)),
                  a=card['a'], marks=card['marks'], ch=card['ch'], words=card['words'])
        item = _test_item(code, 'speaking', it); tests.append(item)
        cards.append('■ ' + card['title'] + ' · ' + card['ja_title'] + f' (compulsory: {pair_of[c]}, one of cards '
                     f'{" or ".join(str(x) for x in COMPULSORY_PAIRS[pair_of[c]])} · 必須)')
        cards.extend(f'☐ {en} / {ja}' for en, ja in zip(card['tasks'], card['tasks_ja']))
        key.append(f'{code} examiner: ' + ' '.join(card['examiner']))
        key.append(f'{code} rubric (6): ' + card['a'] + f' [Compulsory {pair_of[c]}: the examiner always uses card '
                   f'{" or ".join(str(x) for x in COMPULSORY_PAIRS[pair_of[c]])}.]')
    sections.append(('Part 2 · Role-play cards · ロールカード', [
        'Read your card, then talk with the examiner without a script. The examiner will change one thing. / カードを読み、'
        '台本なしで試験官と話します。試験官が途中で一つ変更します。', *cards]))
    comp('speaking', 'speaking', 'Speaking', TIMING['speaking'], sections, key,
         ('A2 段階テストの話す問題です（ブロック18D）：自己紹介と招待への返事、依頼とトラブルのロールカード。試験官の台詞と採点基準は先生用キーにあります。日本語は未監修です。',
          'The speaking test of the A2 stage test (block 18D): a self-introduction with an invitation, and a request card and a '
          'mishap card. The examiner\'s lines and the rubric are in the teacher key.'), tests, ['speaking'], '18D')
    return out


def item_ids(version):
    """[(catalogue test-item id, item code, chapters)] in component order, matching suite.build_suite's numbering."""
    low = version['label'].lower(); counters = {}; out = []
    for code, sub, _, ch in item_map(version):
        counters[sub] = counters.get(sub, 0) + 1
        out.append((f'ms-stage2-test-{low}-{sub}-{counters[sub]:02}', code, sorted(set(ch))))
    return out


def scripts_component():
    sections = []
    for v in VERSIONS:
        lines = []
        for t, task in enumerate(v['listening'], 1):
            lines.append(f'■ Version {v["label"]} · Task {t} · {task["title"]}')
            lines.append(task['context'])
            lines.extend(f'{sp}: «{line}»' for sp, line in task['script'])
        sections.append((f'Version {v["label"]} · バージョン{v["label"]}', lines))
    return dict(slug='test-scripts', type='Teaching plan', title='A2 stage test · Listening scripts (teacher)', block='18C',
                minutes=None, sections=sections,
                key=['Read each text twice at a natural speed, with a short pause between the two readings. Say the speaker\'s '
                     'name before each line. Read the standard forms as written; do not add ‹lah› or ‹kan›. Do not hand out this '
                     'sheet. The answers are in the keys of the two listening papers.',
                     'All names, shops, prices, times, units and places are fictional.'],
                explain=('A2 段階テストの聞く問題の台本（先生用、バージョンAとB）です。学習者には配りません。日本語は未監修です。',
                         'The teacher-read scripts for the A2 stage test listening papers, versions A and B. Not for learners.'),
                sub_type='listening scripts', tests=[], patterns=[], grammar=[FOCUS[n] for n in TESTED],
                goal=TEST_GOALS['listening'][0], skills=['listening'])


def admin_component():
    maps = []
    for v in VERSIONS:
        frames = item_frames(v)
        lines = [f'■ Version {v["label"]}: item, marks, chapters whose can-do goals it tests, Kata-Kata patterns']
        comp = {c for codes in compulsory_codes(v).values() for c in codes}
        lines += [f'{code} · {m} · ch {_chapters(ch)} · ' + ' '.join(f[-7:] for f in frames[code])
                  + (' · compulsory pair' if code in comp else '') for code, _, m, ch in item_map(v)]
        lines.append(f'■ Version {v["label"]}: chapter, its can-do goal, the items that test it')
        for n in TESTED:
            codes = [code for code, _, _, ch in item_map(v) if n in ch]
            lines.append(f'Ch {n} · {CHARTER_GOALS[n]}: ' + ', '.join(codes))
        maps.append((f'Item map · Version {v["label"]} · 問題と章の対応', lines))
    sections = [
        ('What the test is · テストについて', [
            'The A2 stage test closes Stage 2 (chapters 10 to 17; chapter 18 is the review). It checks the Stage 2 can-do goals at '
            'CEFR A2 with tasks that have a real outcome: understand an announcement, act on a notice or a message, fill in a '
            'lost-property form, rearrange a plan, make a request, report a mishap, answer an invitation. / A2 段階テストは'
            '第2段階（第10〜17章）のまとめのテストです。第2段階の「できること」を CEFR A2 で、実際の目的のある課題で確かめます。',
            'Every chapter from 10 to 17 is tested in both versions, by at least two items (item maps below). Only words taught in '
            'chapters 1 to 17 are used; the Kata-Kata practice words and the words taught to recognise only are never tested. / '
            '第10〜17章はどちらのバージョンでも2問以上で確かめます。使う語は第1〜17章で習った語だけです。',
            'Compulsory in both versions (Sam\'s decision A2, 13 Nov 2026): one request card (chapter 12: card 1 or 2) and one '
            'mishap card (chapter 16: card 3 or 4). Change the card of each pair from learner to learner. / 必須（Samの決定 A2）：'
            '依頼のカード（第12章：1か2）とトラブルのカード（第16章：3か4）を一枚ずつ。',
            'Two parallel versions, A and B, with the same sections, tasks, marks and chapter spread and different fictional details. '
            'Use A for the main sitting; use B for a second group, a re-sit or the next course. Do not give both versions to one '
            'learner in the same week. / 同じ構成で細部の違うバージョンAとBがあります。本試験はA、別のグループ・再試験・次の講座はBを使います。',
            'The test is summative but low-stakes in spirit (charter rule 9): the result tells the learner which can-do goals to '
            'revisit. A pass means the learner has met the Stage 2 goals at A2 as this course defines them; it is not an official '
            'CEFR certificate. / 合格は、この講座の定める A2 の第2段階の目標を達成したという意味で、公式の CEFR 証明ではありません。']),
        ('Timing · 時間', [
            f'Block 18C, the written papers: listening {TIMING["listening"]} minutes, reading {TIMING["reading"]}, writing '
            f'{TIMING["writing"]} (45 minutes in all). Collect each paper before the next one.',
            f'Block 18D, speaking: about {TIMING["speaking"]} minutes for each learner, one at a time; one examiner can assess six '
            'learners in the block. Each further six learners needs another speaking block (or a second examiner), outside the '
            f'{TOTAL_BLOCKS} blocks of Stage 2 (Sam\'s decision A3). The others work on their 18A self-check or Kata-Kata meanwhile.',
            'Do the review (18A) and the rehearsal (18B) before the test; go over the results in 18E.']),
        ('Materials · 準備するもの', [
            'For each learner: the listening, reading and writing papers of the version you use (without the teacher keys).',
            'For the speaking test: the speaking sheet, with the four role-play cards cut apart; the teacher key with the examiner\'s '
            'lines and the rubric.',
            'For the teacher: the listening scripts sheet, the four teacher keys, this sheet and one result sheet per learner. No '
            'audio is needed: the teacher reads the scripts.']),
        ('Running the test · 実施の手順', [
            'Listening: read the instructions, give one minute to read the questions, then read each text twice at a natural speed. '
            'Learners answer in English or Japanese, or in Malay where the question asks for it.',
            'Reading and writing: learners work alone without notes or dictionaries. Answer questions about the instructions only.',
            'Speaking: greet the learner first (not marked). Part 1, the self-introduction, the follow-up question and the '
            'invitation. Part 2: one request card (1 or 2) and one mishap card (3 or 4); give 30 seconds to read the card; play '
            'your part from the key and bring in the change of plan halfway. Mark with the rubric straight after each part.']),
        ('Scoring and pass rule · 採点と合格基準', [
            f'Four sections of {SECTION_MARKS} marks: {TOTAL} in all. Listening and reading: one mark for each fact in the key. '
            'Writing and speaking: the rubric in each key (content, language, accuracy or interaction).',
            f'Pass: {PASS_TOTAL} or more out of {TOTAL} (60 per cent), and at least {PASS_SECTION} out of {SECTION_MARKS} in every '
            'section. This is Sam\'s decision A1 of 13 Nov 2026 (the Stage 1 rule carried over); the charter gives no A2 rule, and '
            'it is not taken from a JF, Irodori or CEFR document. / 合格：80点中48点以上（60％）、かつ各セクション20点中10点以上。'
            'これはSamの決定 A1（2026年11月13日、第1段階の基準を引き継いだもの）で、憲章・JF・いろどり・CEFRの基準ではありません。',
            f'A pass is recorded as "{COMPLETION_LABEL}" (CEFR A2). "Not yet": go back to the chapters of the items that were '
            'missed (item map below), then sit the other version.',
            'Standard production is always accepted. Spoken forms («tak», «nak», «dah», «kat», «set», «takpe») are recognised and '
            'accepted where the meaning is clear, never required. ‹lah› and ‹kan› are never required and never cost a mark. '
            'Accept any natural answer with the same meaning (the writing keys list the variants: «kalau» / «jika», «kerana» / '
            '«sebab», «kemudian» / «selepas itu»). In listening and reading, a spelling slip that does not change the meaning '
            'loses no mark. No half marks.']),
        *maps,
        ('After the test · テストのあと', [
            'Go over the answers in 18E. Errors return as practice, not as red crosses (charter rule 9).',
            'Fill in a result sheet for each learner on paper. Cikgu Sensai keeps no learner records.',
            '■ Result sheet', 'Name: ______________________   Version: A / B   Date: __________',
            f'Listening __ / {SECTION_MARKS}   Reading __ / {SECTION_MARKS}   Writing __ / {SECTION_MARKS}   Speaking __ / {SECTION_MARKS}',
            f'Total __ / {TOTAL}   ☐ {COMPLETION_LABEL} (pass)   ☐ Not yet',
            'Speaking cards used: request 1 / 2   mishap 3 / 4',
            'Chapters to revisit: ______________________']),
    ]
    return dict(slug='test-admin', type='Teaching plan', title='A2 stage test · Administration sheet (teacher)', block='18C',
                minutes=None, sections=sections,
                key=['The pass rule (60 per cent overall, half of each section) is Sam\'s decision A1 of 13 Nov 2026, carried over '
                     'from Stage 1; the charter gives no A2 rule. The item maps are generated from the item data, so they always '
                     'match the papers.',
                     'Answer keys: on each paper. Listening scripts: on the scripts sheet and in the listening keys.'],
                explain=('A2 段階テストの実施要領（先生用）：時間、準備、手順、採点と合格基準、問題と章・文型の対応表、結果記入表。日本語は未監修です。',
                         'How to run the A2 stage test: timing, materials, procedure, scoring and the pass rule, the item maps (chapter '
                         'and pattern for every item) and a result sheet.'),
                sub_type='administration', tests=[], patterns=[], grammar=[FOCUS[n] for n in TESTED],
                goal='I can run and mark the A2 stage test and tell each learner which can-do goals to revisit.', skills=[])


def stage_record(components):
    """The Stage 2 record for the catalogue: the CEFR label, the chapter 18 blocks, the A2 test, the can-do review sheet and the
    hours check. A definition only; Cikgu Sensai stores no learner results."""
    ids = {c['id'] for c in components}
    test_ids = {v['label']: [f'ms-stage2-test-{v["label"].lower()}-{s}' for s in ('listening', 'reading', 'writing', 'speaking')]
                for v in VERSIONS}
    return dict(
        id='ms-stage2', language='Malay', title='Stage 2', cefr='A2', chapter_ids=CHAPTERS,
        review_block_id='ms-c18-review' if 'ms-c18-review' in ids else None,
        chapter18_blocks={'18A': 'ms-c18-review', '18B': 'ms-c18-rehearsal', '18C': [i for v in VERSIONS for i in test_ids[v['label']][:3]],
                          '18D': [test_ids[v['label']][3] for v in VERSIONS], '18E': 'ms-c18-feedback'},
        cando_review_id='ms-c18-feedback' if 'ms-c18-feedback' in ids else None,
        cando_goals={f'ms-c{n:02}': [en for en, _ in CANDO[n]] for n in TESTED},
        stage_test=dict(
            versions={k: [i for i in v if i in ids] for k, v in test_ids.items()},
            scripts_id='ms-stage2-test-scripts' if 'ms-stage2-test-scripts' in ids else None,
            administration_id='ms-stage2-test-admin' if 'ms-stage2-test-admin' in ids else None,
            section_marks=SECTION_MARKS, total_marks=TOTAL, timing_minutes=TIMING,
            pass_rule=dict(total_min=PASS_TOTAL, section_min=PASS_SECTION, status=PASS_STATUS),
            compulsory_items={v['label']: compulsory_codes(v) for v in VERSIONS},
            item_chapters={iid: [f'ms-c{c:02}' for c in ch] for v in VERSIONS for iid, _, ch in item_ids(v)},
            item_patterns={iid: item_frames(v)[code] for v in VERSIONS for iid, code, _ in item_ids(v)}),
        completion=dict(flag='stage2_complete', label=COMPLETION_LABEL, cefr='A2',
                        rule='pass the A2 stage test (either version) by the pass rule',
                        evaluator_note='Hanashishou band 1 (Foundation) is roughly A2 (charter section 7); a learner who completes '
                                       'Stage 2 starts band 1 scenes. Scenes get chapter tags in build step 6; nothing is built in Hanashishou here.'),
        hours=dict(blocks=dict(HOURS), total_blocks=TOTAL_BLOCKS, block_minutes=45, total_hours=TOTAL_HOURS,
                   note='Plan section 1: 11 teaching units x 5 blocks, 3 reviews, 4 writing blocks, 5 chapter 18 blocks. Each further '
                        'six learners adds a speaking block outside this total (Sam, A3).'),
        stage3_carry_forward=['ms-c16', 'ms-c17'],
        learner_records='none: the result sheet is paper; Cikgu Sensai stores no learner data', review_status='draft')


VERSIONS = [VERSION_A, VERSION_B]


def components(ledger):
    return [*[c for v in VERSIONS for c in test_components(v)], scripts_component(), admin_component()]


UNIT = dict(unit_id=UNIT_ID, label=None, stage='stage2', chapter_id='ms-c18', check_unit=UNIT_ID, id_prefix=UNIT_ID, level='A2',
            title_prefix='Stage 2', header='Stage 2 A2 stage test (ms-stage2)', menu_title='Stage 2 · A2 stage test',
            genre='Social', goal='I can complete the A2 stage test tasks: listening, reading, writing and speaking.',
            blocks={'C': 'I can complete the written A2 check (listening, reading, writing).',
                    'D': 'I can introduce myself, answer an invitation, make a request and report a mishap.'},
            prerequisites=[f'ms-c{n:02}' for n in range(1, 18)], prerequisite_units=['ms-c18'],
            prereq_grammar=[FOCUS[n] for n in TESTED], word_scope=None, components=components)
