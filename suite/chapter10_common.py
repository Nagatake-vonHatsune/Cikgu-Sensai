"""Stage 2 authoring helpers, first used by chapter 10 (units 10A and 10B: ber- verbs).

Generalised from chapter9_common (itself from chapter8_common back to chapter3_common), keeping the three changes the
chapter 3 review asked for:
- every Malay span is marked by hand in the unit files (no automatic marking);
- every test item names the ledger words it tests, so the prerequisite check is exact;
- recognition words are grouped by scene, and revision comes in labelled groups.

What changes for Stage 2 (A2):
- The chapter number, unit id, Kata-Kata pack, grammar points, question-word note and Block E scene all come from the
  unit config, so chapters 11 to 17 can use this module unchanged (pass their own config) instead of copying it.
- Block E is a scene transfer (charter section 6, Stage 2): the classroom scene changes one fact and the pairs play it
  again. Hanashishou scenes are named only as a later link, because they are not yet tagged by chapter (build step 6).
- There is no Kata-Kata Dunia scene that primes a Stage 2 chapter; the "To recognise" group holds the ledger's
  recognition rows (chapter 10: L-0667 «pindah», the spoken partner of «berpindah»), and is left out when empty.
- Pages say A2 and Stage 2.

No ledger word is introduced here. Recognition words are never tested as new vocabulary. All Japanese is a draft
awaiting native review.
"""
from . import vocab, pattern, english_words, sedia_cards

# Charter section 14: the cumulative question-word set to the end of chapter 9. Chapter 10 adds no new question word.
QUESTIONS = ['«apa»', '«siapa»', '«di mana»', '«Siapakah» (-kah)', '«Apakah» (-kah)',
             '«di manakah» (-kah)', '«Adakah»', '«Bolehkah»', '«berapa»',
             '«bila»', '«pukul berapa»', '«hari apa»',
             '«bagaimana» (spoken: «macam mana»)', '«kenapa» (= «mengapa», «apa sebab»; answer: «sebab» or «kerana»)',
             '«yang mana»', '«ke mana»', '«dari mana»', '«berapa jauh»', '«berapa lama»',
             '«berapa» with a counter («Berapa biji?»)', '«siapa» with «oleh» («Kek ini dibuat oleh siapa?»)']


def components(ledger, cfg):
    """All 11 suite component types, the cumulative question-word drill, the markers drill and any extra block."""
    C = []
    n = cfg['chapter']
    G = cfg['grammar_ids']
    gid = [G[x] for x in cfg['grammar']]
    fid = cfg['pattern_ids']
    goals, ja = cfg['goals'], cfg['goals_ja']
    label = cfg['label']
    pack = f'c{n:02}'
    frames_en = f'Kata-Kata Sedia Kelas {pack} ({sedia_cards(n)} cards, frames ms-{pack}-f01 and ms-{pack}-f02)'

    def add(slug, typ, title, block, minutes, sections, key, explain, subtype=None,
            tests=None, patterns=None, grammar=None, goal=None, skills=None):
        C.append(dict(slug=slug, type=typ, title=title, block=block, minutes=minutes,
                      sub_type=subtype, sections=[s for s in sections if s[1]], key=key, explain=explain,
                      tests=tests or [], patterns=patterns if patterns is not None else fid,
                      grammar=grammar if grammar is not None else gid,
                      skills=skills, goal=goal or goals.get(block, goals['A'])))

    def numbered(lines):
        return [f'{i}. {t}' for i, t in enumerate(lines, 1)]

    # 1 · Opener
    add('opener', 'Opener', 'Chapter opener', 'A', 5, [
        ('Can-do goals · できること', [f'Block {b}: {goals[b]} / {ja[b]}' for b in 'ABCDE']),
        ('Setting and recall · 場面と復習', [cfg['setting'], cfg['setting_ja'], *cfg['recall'],
                                            'Write one question for Tanya Cikgu before you look at the new words. / 新しい単語を見る前に、Tanya Cikgu への質問を一つ書きましょう。']),
        ('Classroom and home learning · 授業と自習', [
            f'Before class: {frames_en}. / 授業前：Kata-Kata Sedia Kelas {pack}（カード{sedia_cards(n)}枚、文型 f01・f02）。',
            f'After class: the chapter {n} cards for this unit ({cfg["card_range"]}) and the frames {cfg["frame_list"]}. / '
            f'授業後：このユニットの第{n}章のカード（{cfg["card_range"]}）と文型 {cfg["frame_list_ja"]}。',
            'Self-study planning figure: about three hours for this full-course unit. / 自習の目安：このユニットで約3時間。'])],
        ['Recall is retrieval practice, not a score. Let learners try without notes first, then check together.',
         'Recall answers: ' + cfg['recall_key']],
        ('ユニットの目標と場面を確認し、前の章の表現を思い出してから新しい内容に進みます。',
         'Read the unit goals and the setting, recall earlier language without notes, then move on to the new material.'))

    # 2 · Vocabulary
    ex = cfg['examples']
    opts = cfg.get('vocab_opts', {})

    def entries(ids):
        return [(lid, ex[lid], opts.get(lid, {})) for lid in ids]
    n_rec = sum(len(ids) for _, ids in cfg['recognition'])
    n_rev = sum(len(ids) for _, ids in cfg['revision'])
    add('vocabulary', 'Vocabulary', 'Vocabulary focus', 'A', 10, [
        ('Core words · 新しい基本語', vocab(ledger, [
            (f'Core words · {heading} · 学習する', entries(ids)) for heading, ids in cfg['core_groups']])),
        ('To recognise · 聞いて分かる', vocab(ledger, [
            (f'To recognise · {heading} · 聞いて分かればよい', entries(ids)) for heading, ids in cfg['recognition']])),
        ('Revision · 復習 (not new, not tested as new vocabulary)', vocab(ledger, [
            (f'Revision · 復習 · {heading}', entries(ids)) for heading, ids in cfg['revision']]))],
        [f'{len(cfg["core"])} new core entries, {n_rec} recognition entries and {n_rev} revision entries.',
         'Recognition words are for listening only. The unit test never treats them as new vocabulary.',
         'Revision words were taught earlier; they are listed because this unit really uses them, not counted as new.',
         'Each ber- word shows its root as the Kata-Kata card note gives it. A slash variant under one ledger ID counts as '
         'one entry; spoken forms are marked "spoken", formal or written forms "formal".'],
        ('基本語は覚えて使います。「聞いて分かる」の語は聞いて分かれば十分です。復習語は前の章で学んだ語です。日本語訳は未監修です。',
         'Learn and use the core words; recognise the listening-only words; the revision words come from earlier chapters.'))

    # 3 · Pattern and grammar
    patt = [pattern(i, *p) for i, p in enumerate(cfg['patterns'], 1)]
    add('pattern-grammar', 'Pattern and grammar', 'Pattern and grammar focus', 'A', 20, patt,
        ['Model each A line; learners answer as B, then swap. Explain the rule only after they have used the pattern.',
         cfg['pattern_ids_note'] + ' Explanations and Japanese comparisons are drafts.',
         *cfg['pattern_keys']],
        ('まず質問と答えを声に出して練習し、そのあとで説明を読みます。日本語との比較は未監修です。',
         'Practise the questions and answers aloud first, then read the explanation.'),
        goal=goals['A'])

    # 4 · Drills (section 14 ladder)
    drill = cfg['drills']
    specs = [
        ('drill-1-pattern-table', 'repeat', 'Drill 1 · Pattern table',
         'Read every combination aloud, then cover the line and say it again. / すべての組み合わせを声に出して読み、次に隠して言います。'),
        ('drill-2-substitution', 'substitute', 'Drill 2 · Substitution',
         'Replace one part with the cue and say the whole sentence. / キューで一か所を入れ替え、文全体を言います。'),
        ('drill-3-transformation', 'transform', 'Drill 3 · Transformation',
         'Change the sentence as the cue says. / キューのとおりに文を変えます。'),
        ('drill-4-question-answer', 'question and answer', 'Drill 4 · Question and answer',
         'Items 1 to 4: answer with the cue. Items 5 to 8: you hear the answer; ask the question. / 1〜4はキューで答え、5〜8は答えに合う質問を作ります。'),
        ('drill-5-question-word-choice', 'question-word choice', 'Drill 5 · Question-word choice',
         f'Fill the gap with a question word taught so far (chapters 1 to {n}). / 第1〜{n}章で学んだ疑問語から選んで入れます。'),
    ]
    for slug, sub, title, instruction in specs:
        lines = []
        if drill.get(sub + '_frame'):
            lines.append(drill[sub + '_frame'])
        add(slug, 'Drill', title, 'B', 4, [
            ('Instructions · 指示', [instruction]),
            ('Practice · 練習', lines + numbered(drill[sub]))],
            ['Answers in order:', *cfg['drill_keys'][sub]],
            ('番号順に口で練習し、ペアで役を交代します。答えは先生用キーにあります。',
             'Practise aloud in numbered order and swap roles. Answers are in the teacher key.'),
            subtype=sub, goal=goals['B'])
    dialogues = []
    for i, (a, b, setting) in enumerate(cfg['short_dialogues'], 1):
        dialogues.extend([f'Dialogue {i} · {setting}', f'A: «{a}»  B: «{b}»  A: ____________________'])
    add('drill-6-short-dialogue', 'Drill', 'Drill 6 · Short dialogues', 'B', 3, [
        ('Two lines, then add a third · 二行＋自分の一行', dialogues)],
        ['Any third line that answers B naturally is correct. Possible third lines:', *cfg['short_keys']],
        ('二行の会話を読み、自分で三行目を加えます。役を交代します。',
         'Read the two lines and add a third that fits. Swap roles.'),
        subtype='free', goal=goals['B'])
    t = cfg['markers']
    # Charter section 14: the tense and aspect markers return in every later chapter.
    add('drill-markers', 'Drill', t['title'], 'B', 5, [
        ('Instructions · 指示', t['instructions']),
        ('Say it with the marker · マーカーを付けて言う', numbered(t['items'])),
        ('Japanese bridge · 日本語との橋渡し', t['bridge'])],
        ['Answers in order:', *t['key']],
        t['explain'], subtype='markers', grammar=[G[t['grammar']]], goal=goals['B'])
    add('drill-question-word-set', 'Drill', 'Cumulative question-word drill', 'D', 5, [
        ('Cumulative set · これまでの疑問語', [
            f'Chapters 1 to {n}: ' + ' / '.join(QUESTIONS + cfg.get('questions_added', [])),
            cfg['question_note'],
            *numbered(cfg['question_tasks'])])],
        ['Model questions in order:', *cfg['question_keys']],
        (f'第1章から第{n}章までの疑問語をすべて使って質問します。',
         f'Ask questions with every question word taught so far (chapters 1 to {n}).'),
        subtype='question-word set', grammar=gid, goal=goals['D'])

    # 5 · Model conversation
    base, variant = cfg['dialogue'], cfg['variant']
    gaps = cfg.get('gap_turns', (1, 3, 5, 7, 9))
    gapped = [f'{sp}: {"____________________" if i in gaps else "«" + speech + "»"}'
              for i, (sp, speech) in enumerate(base)]
    add('model-conversation', 'Model conversation', 'Model conversation', 'B', 15, [
        ('Model · 会話', [f'{sp}: «{speech}»' for sp, speech in base]),
        ('Gapped form · 空所', gapped),
        ('Changed facts variant · 情報を変更', [f'{sp}: «{speech}»' for sp, speech in variant])],
        [f'The model has {len(base)} turns. Gaps: turns ' + ', '.join(str(i + 1) for i in gaps) + '.',
         *[f'Turn {i + 1}: «{base[i][1]}»' for i in gaps],
         'Then perform the changed-facts variant without the script, changing one more fact of your own.'],
        ('会話を読み、空所版を埋め、条件を変えた版を台本なしで話します。',
         'Read the model, fill the gaps, then perform the changed-facts version without the script.'),
        goal=goals['B'])

    # 6 · Listening
    script = [f'{sp}: «{speech}»' for sp, speech in cfg['listening']]
    add('listening', 'Listening', 'Listening focus · Encik Tanaka', 'C', 15, [
        ('Before listening · 聞く前', [cfg['listening_context'], *cfg['listening_before']]),
        ('While listening · 聞きながら', numbered(cfg['listen_questions'])),
        ('After listening · 聞いたあと', cfg['listening_after'])],
        ['The teacher reads the script twice at natural speed. No audio file.',
         'Teacher-read script:', *script,
         'Answers: ' + ' / '.join(f'{i}. {a}' for i, a in enumerate(cfg['listen_answers'], 1)),
         'Do not hand out the script before the second listening.'],
        ('先生が台本を2回読みます。音声ファイルはありません。質問を先に読んでから聞きます。',
         'The teacher reads the script twice; read the questions first, listen for the details, then shadow.'),
        goal=goals['C'])

    # 7 · Reading and writing
    add('reading-writing', 'Reading and writing', cfg['reading_title'], 'C', 10, [
        ('Real-world text · 実用文', cfg['reading']),
        ('Questions · 質問', numbered(cfg['read_questions'])),
        ('Write · 書く', [cfg['write_instruction'], '________________________________________',
                         '________________________________________', '________________________________________'])],
        ['Reading: ' + ' / '.join(f'{i}. {a}' for i, a in enumerate(cfg['read_answers'], 1)),
         'Model writing: ' + cfg['write_model'],
         'All times, dates and names in the text are fictional.'],
        ('短い実用文を読んで質問に答え、自分でも短く書きます。',
         'Read a short practical text, answer the questions, then write your own.'),
        subtype=cfg['writing_type'], goal=goals['C'], skills=['reading', 'writing'])

    # 8 · Task
    add('task', 'Task', cfg['task_title'], 'C', 15, [
        ('Role card A · Aのカード', cfg['role_a']),
        ('Role card B · Bのカード', cfg['role_b']),
        ('Change of plan · 予定変更', cfg['change']),
        ('Success criteria · できる基準', cfg['success'])],
        ['Possible exchange: ' + cfg['task_key'],
         'All schedules and personal details on the cards are fictional. Learners may use their real week or an invented persona.'],
        ('役割カードを見て台本なしで話し、途中で予定が変わります。',
         'Use the role cards without a script; deal with the change of plan halfway through.'),
        subtype='role-play', goal=goals['C'])

    # 9 · Culture note
    add('culture-note', 'Culture note', 'Culture and usage note', 'E', 10, [
        ('English', cfg['culture']),
        ('日本語', cfg['culture_ja'])],
        [f'English note: {english_words(cfg["culture"])} words. The Japanese is a full translation (draft).',
         'Sources: ' + cfg['culture_sources'],
         'Discussion prompt for the teacher: ' + cfg['culture_prompt']],
        cfg['culture_explain'], goal=goals['E'])

    # 10 · Test: listening, words, grammar, reading, one speaking task (15 to 20 scored items)
    tests = []
    for i, (idx, answer, words) in enumerate(cfg['test_listen'], 1):
        tests.append(dict(sub_type='listening',
                          prompt=f'L{i}. ' + cfg['test_listen_prompts'][i - 1],
                          answer=f'Teacher reads: «{cfg["listening"][idx][1]}» Answer: {answer}',
                          words=words, grammar=gid))
    for i, lid in enumerate(cfg['quiz_words'], 1):
        row = ledger.row(lid)
        term = row['Malay'].split(' / ')[0]
        tests.append(dict(sub_type='words', prompt=f'V{i}. Write the Malay for: {cfg["quiz_meanings"][i - 1]}',
                          answer='«' + term + '»', words=[term], grammar=gid))
    for i, (q, a, words) in enumerate(cfg['grammar_quiz'], 1):
        tests.append(dict(sub_type='grammar', prompt=f'G{i}. ' + q, answer=a, words=words, grammar=gid))
    for i, (q, a, words) in enumerate(cfg['reading_quiz'], 1):
        tests.append(dict(sub_type='reading', prompt=f'R{i}. ' + q, answer=a, words=words, grammar=gid))
    tests.append(dict(sub_type='speaking', prompt='S1. ' + cfg['speaking_test'], answer=cfg['speaking_key'],
                      words=cfg['speaking_words'], grammar=gid))
    n_scored = len(tests) - 1
    assert 15 <= n_scored <= 20, (label, len(tests))
    add('test', 'Test', 'Unit test and self-check', 'D', 20, [
        ('Listening · 聞く', [f'The teacher reads {len(cfg["test_listen"])} lines from the listening script.'] +
         [t['prompt'] for t in tests if t['sub_type'] == 'listening']),
        ('Words and grammar · 語彙と文型', [t['prompt'] for t in tests if t['sub_type'] in ('words', 'grammar')]),
        ('Reading · 読む', cfg['test_reading'] + [t['prompt'] for t in tests if t['sub_type'] == 'reading']),
        ('Speaking · 話す', [tests[-1]['prompt']]),
        ('I can · 自己評価', [f'☐ {goals[b]} / {ja[b]}' for b in 'ABCE'])],
        [f'{t["prompt"].split(".")[0]}: {t["answer"]}' for t in tests] +
        [f'{n_scored} scored items and one speaking task. Low-stakes: go over mistakes in the next class.',
         'Accept any natural Malaysian answer that does the task; a standard form is always right.'],
        (f'聞く・語彙・文型・読むの{n_scored}問と話す課題1つです。間違いは次の授業で練習します。',
         f'{n_scored} low-stakes items plus one speaking task and an "I can" self-check.'),
        tests=tests, goal=goals['D'])

    # 11 · Teaching plan
    plan = cfg['plan']
    add('teaching-plan', 'Teaching plan', 'Teaching plan and answer key', 'All', None, [
        ('Before and after · 授業の前後', [
            f'Before Block A: {frames_en}.',
            'After Block D: the Kata-Kata chapter ' + str(n) + ' deck with spaced review, frames ' + ', '.join(fid) +
            ' in the frame drill and Susun Ayat; about 3 hours of self-study for this unit (planning figure).',
            cfg['hanashishou_note'],
            cfg['next_note']]),
        ('Block A · Words and patterns (45 min)', [
            'Goal: ' + goals['A'], '0–5 Recall: ' + plan['A_recall'], '5–10 Tanya Cikgu questions from Kata-Kata.',
            '10–20 Vocabulary focus: core words first, with each root; recognition and revision words are only pointed out.',
            '20–40 Pattern focus: ' + plan['A_patterns'], '40–45 First substitutions (Drill 2, items 1 to 3).']),
        ('Block B · Drills and conversation (45 min)', [
            'Goal: ' + goals['B'], '0–5 Recall: ' + plan['B_recall'],
            '5–25 Drill ladder in order: ' + plan['B_drills'],
            '25–40 Model conversation, gapped form, then the changed-facts variant.', '40–45 Pair rehearsal without the script.']),
        ('Block C · Listening and task (45 min)', [
            'Goal: ' + goals['C'], '0–5 Recall: ' + plan['C_recall'],
            '5–20 Listening: read the questions, two readings, check, then shadow three lines.',
            '20–30 Reading and writing.', '30–45 Task with role cards; announce the change of plan halfway.']),
        ('Block D · Review and test (45 min)', [
            'Goal: ' + goals['D'], '0–15 Mixed review: ' + plan['D_review'],
            '15–25 Unit test (low-stakes).', '25–35 Self-check and feedback.', '35–45 Preview: ' + plan['D_preview']]),
        ('Block E · Scene transfer (45 min)', [
            'Goal: ' + goals['E'], '0–5 Recall: ' + plan['E_recall'],
            '5–15 Scene listening: ' + plan['E_listening'],
            '15–30 Role-play in pairs: ' + plan['E_roleplay'], '30–40 Changed situation: ' + plan['E_variation'],
            '40–45 Culture and usage note discussion, and the home-practice briefing.']),
        ('What to listen for · 注意点', cfg['teacher_notes'])],
        ['Answer keys are on each component. Japanese text awaits native review.',
         f'Standard forms first; spoken forms are labelled. ber- verbs are taught as whole ledger forms, each with its root; '
         f'no meN- verb (chapter 11) and no suffixed verb form (chapter 12).'],
        ('先生用：45分×5ブロックの進め方、注意点、宿題です。答えは各シートのキーにあります。',
         'Teacher plan: five 45-minute blocks with timings, what to listen for and homework. Answers are on each sheet.'),
        goal=goals['A'])

    if cfg.get('extra'):
        e = cfg['extra']
        add(e['slug'], e.get('type', 'Reading and writing'), e['title'], 'Skills', 45, [
            ('Model · 例', e['model']),
            ('Plan · 45 minutes · 進め方', e['plan']),
            ('Your turn · 自分で', e['task']),
            ('Peer check · 互いに確認', e['check'])],
            ['Model: ' + e['answer'], *e.get('key_extra', []),
             'This is the extra 45-minute ' + e.get('kind', 'writing') + ' block after unit ' + label + '.'],
            (e['explain'][0], e['explain'][1]),
            subtype=e.get('sub_type', 'composition'), goal=e['goal'], skills=e.get('skills', ['speaking', 'writing']),
            grammar=e.get('grammar'), patterns=e.get('patterns'))
    return C


def unit_dict(cfg):
    label = cfg['label']
    n = cfg['chapter']
    uid = cfg['unit_id']
    return dict(unit_id=uid, label=label, chapter_id=f'ms-c{n:02}', check_unit=uid, id_prefix=uid,
                title_prefix='Unit ' + label, header=f'Unit {label} ({uid})', level='A2',
                menu_title=cfg['menu_title'], genre=cfg['genre'],
                goal=cfg['unit_goal'], blocks=cfg['goals'], prerequisites=[f'ms-c{k:02}' for k in range(1, n)],
                prerequisite_units=cfg['prerequisite_units'],
                prereq_grammar=cfg['prereq_grammar'],
                word_scope=cfg['core'] + [i for _, ids in cfg['recognition'] for i in ids]
                + [i for _, ids in cfg['revision'] for i in ids],
                components=lambda ledger: components(ledger, cfg))
