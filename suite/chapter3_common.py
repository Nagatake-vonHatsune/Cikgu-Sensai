"""Chapter 3 authoring helpers. Each unit supplies factual scenarios and exact ledger IDs.

No new ledger words are introduced. Recognition-only Dunia items have their own
list and are never tested as new core vocabulary. Japanese remains draft.
"""
from . import vocab, pattern, turns, english_words

import re

# Annotate previously unmarked chapter 3 Malay examples in English rubrics,
# glossary explanations and exercise cues. Every resulting «…» span still
# passes the regular ledger, register, affix and Malaysian-form checks.
# Neither the source ledger nor the checker rules are loosened.
SCENE_TITLES = ('Ke bank dan pejabat pos', 'Pasar pagi')


def mark_ch3(raw, ledger):
    from . import ENGLISH_HOMOGRAPHS
    if not isinstance(raw, str):
        return raw
    candidates = [term for term in ledger.checker.entries
                  if ledger.checker.known_by(term, 3)
                  and term not in ENGLISH_HOMOGRAPHS
                  and term != 'ke']
    # Longest exact ledger phrase wins. This never introduces a new word.
    terms = sorted(candidates, key=lambda x: (-len(x), x))
    rx = re.compile(r'(?<![a-z-])(?:' + '|'.join(re.escape(t) for t in terms)
                    + r')(?![a-z-])', re.IGNORECASE)
    keep = re.compile(r'(«[^«»]*»|‹[^‹›]*›|Ke bank dan pejabat pos|Pasar pagi)', re.IGNORECASE)
    bits = keep.split(raw)
    return ''.join(part if keep.fullmatch(part) else
                   rx.sub(lambda m: '«' + m.group(0) + '»', part)
                   for part in bits)


GRAMMAR3 = {
    'numbers': 'ms-c03-g02',
    'age_phone': 'ms-c03-g03',
    'prices': 'ms-c03-g04',
    'ordinals': 'ms-c03-g05',
    'fractions': 'ms-c03-g06',
    'measures': 'ms-c03-g07',
    'transactions': 'ms-c03-g08',
}
QUESTIONS = ['«apa»', '«siapa»', '«di mana»', '«Siapakah» (-kah)', '«Apakah» (-kah)',
             '«di manakah» (-kah)', '«Adakah»', '«Bolehkah»', '«berapa»']


def components(ledger, cfg):
    """Make all 11 suite types plus a separate question-word drill, without generic filler."""
    C = []
    gid = [GRAMMAR3[x] for x in cfg['grammar']]
    fid = cfg['pattern_ids']
    goals = cfg['goals']
    ja = cfg['goals_ja']

    def add(slug, typ, title, block, minutes, sections, key, explain, subtype=None,
            tests=None, patterns=None, grammar=None, goal=None, skills=None):
        C.append(dict(slug=slug, type=typ, title=title, block=block, minutes=minutes,
                      sub_type=subtype, sections=sections, key=key, explain=explain,
                      tests=tests or [], patterns=patterns if patterns is not None else fid,
                      grammar=grammar if grammar is not None else gid,
                      skills=skills, goal=goal or goals.get(block, goals['A'])))

    add('opener', 'Opener', 'Chapter opener', 'A', 5, [
        ('Can-do goals · できること',
         [f'Block {b}: {goals[b]} / {ja[b]}' for b in 'ABCDE']),
        ('Setting and recall · 場面と復習', [
            cfg['setting'],
            'Without notes: greet your partner and introduce yourself from chapters 1 and 2.',
            'Recall: «Selamat pagi.» «Nama saya Tanaka.» «Siapa nama encik?»',
            'Write a question for Tanya Cikgu before the new words.']),
        ('Classroom and home learning', [
            'Before class: Kata-Kata Sedia Kelas c03; bring one question about numbers.',
            f'After class: practise the chapter 3 cards and Dunia scene {cfg["dunia_title"]}.',
            'Self-study planning figure: three hours for this full-course unit.'])],
        ['Check recall first, not as a scored item. The learner can do the block goal after practice.'],
        ('章の目標と場面を確認し、第1・2章を復習します。',
         'Read the unit goals, recall earlier greetings and names, then work with the new numbers.'))

    ex = cfg['examples']
    def entries(ids):
        return [(lid, ex[lid], cfg.get("vocab_opts", {}).get(lid, {})) for lid in ids]
    add('vocabulary', 'Vocabulary', 'Vocabulary focus', 'A', 10, [
        ('Core words · 新しい基本語', vocab(ledger, [
            ('Core words · ' + cfg['core_heading'] + ' · 学習する', entries(cfg['core']))])),
        ('Dunia · To recognise · 聞いて分かる', vocab(ledger, [
            ('Dunia · To recognise · ' + cfg['dunia_title'], entries(cfg['recognition']))])),
        ('Revision · 復習 (not new, not tested as new vocabulary)', vocab(ledger, [
            ('Revision · 復習 · Previously taught', entries(cfg['revision']))]))],
        ['Exactly %s new core entries, %s Dunia recognition entries and %s previous-chapter revision entries.'
         % (len(cfg['core']), len(cfg['recognition']), len(cfg['revision'])),
         'Dunia words are recognition-only. The test does not treat them as new core.',
         'Slash variants under one ledger ID count as one entry.'],
        ('基本語・場面の聞き取り専用語・前の章の復習語を区別します。日本語訳は未監修です。',
         'Learn the new core words; recognise, but do not test, the Dunia words; recycle the revision words.'))

    patt = []
    for i, p in enumerate(cfg['patterns'], 1):
        patt.append(pattern(i, p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
    add('pattern-grammar', 'Pattern and grammar', 'Pattern and grammar focus',
        'A', 20, patt,
        ['Model each A question and have students answer B. Correct the numerical meaning, not the accent.',
         'The listed Kata-Kata frames retain their upstream IDs; additional explanations are draft.'],
        ('文型の質問と答えを声に出し、そのあと説明を確認します。比較説明は未監修です。',
         'Read the question-and-answer examples before discussing the grammar.'),
        goal=goals['A'])

    def numbered(lines):
        return [f'{i}. {t}' for i,t in enumerate(lines,1)]
    drill = cfg['drills']
    drill_specs = [
        ('drill-1-pattern-table','repeat','Drill 1 · Pattern table','Read the numbered combinations aloud.', drill['repeat']),
        ('drill-2-substitution','substitute','Drill 2 · Substitution','Replace the indicated part; say the complete answer.',drill['substitute']),
        ('drill-3-transformation','transform','Drill 3 · Transformation','Transform the statement according to the instruction.',drill['transform']),
        ('drill-4-question-answer','question and answer','Drill 4 · Question and answer','Answer, then reverse the question and answer roles.',drill['qa']),
        ('drill-5-question-word-choice','question-word choice','Drill 5 · Question-word choice','Select from the cumulative question words taught through chapter 3.',drill['choice']),
    ]
    for slug,sub,title,instruction,items in drill_specs:
        add(slug,'Drill',title,'B',4,[
            ('Instructions · 指示', [instruction]),
            ('Practice · 練習', numbered(items))],
            ['Suggested answers in numbered order:', *cfg['drill_keys'][sub]],
            ('番号順に口頭で練習し、ペアで交代します。',
             instruction),subtype=sub,goal=goals['B'])
    dialogues = []
    for i, (a,b,setting) in enumerate(cfg['short_dialogues'],1):
        dialogues.extend([f'Dialogue {i} · {setting}', f'A: «{a}»  B: «{b}»  A: ____________________'])
    add('drill-6-short-dialogue','Drill','Drill 6 · Short dialogues','B',3,[
        ('Two lines, then add a third · 二行＋自分の一行', dialogues)],
        ['Third line must respond meaningfully; no memorised third line required.',
         *cfg['short_keys']],
        ('二行の会話を読み、自分で一行を加えます。役を交代します。',
         'Read two turns and add one meaningful turn without looking at the key.'),
        subtype='free',goal=goals['B'])
    add('drill-question-word-set','Drill','Cumulative question-word drill','D',5,[
        ('Cumulative set · これまでの疑問語', [
            'Full chapter 1 to 3 set: ' + ' / '.join(QUESTIONS),
            'Practise formal -kah forms only after the corresponding plain form.',
            *numbered(cfg['question_tasks'])])],
        ['Examples: «Apa khabar?» «Siapa nama encik?» «Di manakah pejabat encik?»',
         '«Adakah encik orang Jepun?» «Bolehkah saya tanya?» «Berapa harga ini?»'],
        ('第1章から第3章までの疑問語を一緒に復習します。',
         'Use all cumulative question words, including -kah and berapa.'),
        subtype='question-word set',goal=goals['D'])

    base = cfg['dialogue']
    gapped = [f'{sp}: {"___" if i in (1,3,5,7,9) else "«"+speech+"»"}'
              for i,(sp,speech) in enumerate(base)]
    variant = cfg['variant']
    add('model-conversation','Model conversation','Model conversation','B',15,[
        ('Model · 会話', [f'{sp}: «{speech}»' for sp,speech in base]),
        ('Gapped form · 空所', gapped),
        ('Changed facts variant · 情報を変更', [f'{sp}: «{speech}»' for sp,speech in variant])],
        ['Model has %d turns; perform the full changed-facts variant before removing the script.' % len(base),
         'Gaps correspond to turns 2, 4, 6, 8 and 10. Check the meaning, number and register.',
         'Ask learners to repeat with their own factual values; do not collect real telephone numbers.'],
        ('会話を読んでから、空所版、数字や条件を変えた版の順に進みます。',
         'Read the model, complete gaps, then perform a full conversation with changed facts.'),
        goal=goals['B'])

    spoken_script = [f'{speaker}: «{speech}»' for speaker,speech in cfg['listening']]
    nwords = sum(len(speech.split()) for speaker,speech in cfg['listening'])
    add('listening','Listening','Listening focus · Encik Tanaka', 'C', 15,[
        ('Before listening · 聞く前', [
            'Predict the topic: ' + cfg['listening_context'],
            'Read the six possible answer categories without the script.']),
        ('While listening · 聞きながら', numbered(cfg['listen_questions'])),
        ('After listening · 聞いたあと', [
            'Compare answers with a partner, then shadow the key numerical sentences.',
            'Change one fact and say why the number or total changes.'])],
        ['Teacher reads each line twice, in natural Malaysian standard pronunciation.',
         'Teacher-read script (%d Malay words):' % nwords, *spoken_script,
         'Answers: ' + ' / '.join(cfg['listen_answers']),
         'Do not distribute the script before the first listening.'],
        ('先生が台本を二度読み、数字を聞き取ります。音声ファイルはありません。',
         'Teacher-read script only; preview, listen for specific facts and then shadow.'),
        goal=goals['C'])

    add('reading-writing','Reading and writing',cfg['reading_title'],'C',10,[
        ('Real-world text · 実用文',cfg['reading']),
        ('Questions · 質問', numbered(cfg['read_questions'])),
        ('Write · 書く', [
            cfg['write_instruction'], '________________________________________',
            '________________________________________', '________________________________________'])],
        ['Reading: ' + ' / '.join(cfg['read_answers']),
         'Model writing: ' + cfg['write_model'],
         'The quantities and prices in the text are fictional teaching examples.'],
        ('短い実用文を読み、質問に答えてから、自分でも書きます。',
         'Read a practical text, answer questions, then write a short form or note.'),
        subtype=cfg['writing_type'],goal=goals['C'],skills=['reading','writing'])

    add('task','Task',cfg['task_title'],'C',15,[
        ('Role card A · Aのカード',cfg['role_a']),
        ('Role card B · Bのカード',cfg['role_b']),
        ('Change of plan · 予定変更',cfg['change']),
        ('Success criteria · できる基準',cfg['success'])],
        ['Possible result: ' + cfg['task_key'],
         'Do not use a real phone number. All practice prices, measurements and quantities are fictional.'],
        ('役割カードを使い、台本を見ずに話し、途中で条件を変えます。',
         'Use the two role cards independently and respond to a mid-task change.'),
        subtype='role-play',goal=goals['C'])

    culture = cfg['culture']
    add('culture-note','Culture note','Culture and usage note','E',10,[
        ('English',culture),
        ('日本語',cfg['culture_ja'])],
        ['English culture note: %d words.' % english_words(culture),
         'Sources: only Kata-Kata chapter 3 card notes where a word-origin or word-building claim is made.',
         'Usage guidance and Japanese comparisons are drafts for Sam and native-speaker review.'],
        ('マレーシアでの使い方について読みます。語源はKata-Kataカード注記のみを使います。',
         'Read a usage note. Word-origin claims are limited to the Kata-Kata card notes.'),
        goal=goals['E'])

    tests = []
    quiz_words=cfg['quiz_words'][:6]
    test_lines=[cfg['listening'][k] for k in cfg.get('test_listen_lines', range(5))]
    for i,(line,ans) in enumerate(zip(test_lines,cfg['test_listen_answers']),1):
        tests.append(dict(sub_type='listening', prompt=f'L{i}. Listen to the teacher and write the main number or value.',
                          answer=f'Teacher reads: «{line[1]}» Answer: {ans}',
                          words=[ledger.row(cfg['core'][i])['Malay'].split(' / ')[0]], grammar=gid))
    for i,lid in enumerate(quiz_words,1):
        row=ledger.row(lid)
        tests.append(dict(sub_type='words', prompt=f'V{i}. Write the Malay term for: {row["Meaning (EN)"]}.',
                          answer='«'+row['Malay'].split(' / ')[0]+'»', words=[row['Malay'].split(' / ')[0]], grammar=gid))
    for i,(q,a) in enumerate(cfg['grammar_quiz'],1):
        tests.append(dict(sub_type='grammar', prompt=f'G{i}. '+q,answer=a,
                          words=[ledger.row(cfg['core'][0])['Malay'].split(' / ')[0]], grammar=gid))
    for i,(q,a) in enumerate(zip(cfg['read_questions'][:4],cfg['read_answers'][:4]),1):
        tests.append(dict(sub_type='reading',prompt=f'R{i}. '+q,answer=a,
                          words=[ledger.row(cfg['core'][1])['Malay'].split(' / ')[0]], grammar=gid))
    tests.append(dict(sub_type='speaking',prompt='S1. '+cfg['speaking_test'],answer=cfg['speaking_key'],
                      words=[ledger.row(cfg['core'][2])['Malay'].split(' / ')[0]],grammar=gid))
    assert len(tests)==18, (cfg['label'],len(tests))
    add('test','Test','Unit test and self-check','D',20,[
        ('Listening · 聞く', [t['prompt'] for t in tests if t['sub_type']=='listening']),
        ('Words and grammar · 語彙と文型', [t['prompt'] for t in tests if t['sub_type'] in ('words','grammar')]),
        ('Reading · 読む',cfg['reading']+[t['prompt'] for t in tests if t['sub_type']=='reading']),
        ('Speaking · 話す',[tests[-1]['prompt']]),
        ('I can · 自己評価',[f'☐ {goals[b]}' for b in 'ABCE'])],
        [f'{t["prompt"].split(".")[0]}: {t["answer"]}' for t in tests] +
        ['17 scored items and one speaking task, low-stakes. Review mistakes next class.'],
        ('聞く・語彙・文法・読むの17問と話す課題です。低負担の確認テストです。',
         'Seventeen low-stakes written/listening items plus one speaking task and self-check.'),
        tests=tests,goal=goals['D'])

    add('teaching-plan','Teaching plan','Teaching plan and answer key','All',None,[
        ('Before and after · 授業の前後', [
            'Before Block A: Kata-Kata Sedia Kelas c03; read the numerical cards relevant to this unit.',
            'Before Block E: Kata-Kata Dunia "'+cfg['dunia_title']+'"; recognise its scene vocabulary.',
            'After Block D: Kata-Kata chapter 3 cards, frame drill and Susun Ayat; about 3 hours per full-course unit.',
            'No Hanashishou A1 scene. Listening uses the printed teacher script, not an audio file.']),
        ('Block A · Words and patterns (45 min)', [
            'Goal: '+goals['A'],
            '0–5 Recall: chapters 1 and 2 (greeting, name, origin). 5–10 Tanya Cikgu questions.',
            '10–20 core vocabulary, with recognition and revision categories kept separate.',
            '20–40 the four or five pattern boxes, Q&A first, rule second. 40–45 first substitutions.']),
        ('Block B · Drills and conversation (45 min)', [
            'Goal: '+goals['B'],
            '0–5 Recall first pattern without notes. 5–25 six drills in section 14 order.',
            '25–40 model conversation then gaps then changed-facts variant. 40–45 pair rehearsal.']),
        ('Block C · Listening and task (45 min)', [
            'Goal: '+goals['C'],
            '0–5 Recall two number sentences. 5–20 teacher-read listening, two readings.',
            '20–30 six reading questions and writing. 30–45 role-play; change the plan mid-way.']),
        ('Block D · Review and test (45 min)', [
            'Goal: '+goals['D'],
            '0–15 mixed recall with cumulative question words including «berapa», «adakah» and «bolehkah».',
            '15–25 low-stakes unit test; 25–35 self-check and correction; 35–45 Kata-Kata preview.']),
        ('Block E · Dunia scene (45 min)', [
            'Goal: '+goals['E'],
            '0–5 recall. 5–15 teacher-read Dunia scene. 15–30 pairs enact the scene.',
            '30–40 change the situation and speak freely; 40–45 usage/culture discussion.']),
        ('What to listen for · 注意点', [
            *cfg['teacher_notes'],
            'Standard first. Spoken forms labelled. No productive ber- or me- verbs.'])],
        ['Use the answer key on each corresponding component. Japanese explanations await native review.'],
        ('先生用の45分×5ブロック進行表・宿題・答えの確認方法です。',
         'Five 45-minute blocks with recall, explicit timing, assessment and independent tasks.'),
        goal=goals['A'])

    if cfg.get('extra'):
        e=cfg['extra']
        add(e['slug'],'Reading and writing',e['title'],'Skills',45,[
            ('Model · 例',e['model']),
            ('Your turn · 自分で',e['task']),
            ('Peer check · 互いに確認',e['check'])],
            ['Model: '+e['answer'],'This is an extra 45-minute skills or review block.'],
            ('追加45分ブロックでモデルを見てから自分で書くか復習します。',
             'Additional 45-minute review or writing block using the taught chapter vocabulary.'),
            subtype='composition',goal=e['goal'],skills=['reading','writing'])
    return C


def unit_dict(cfg):
    label=cfg['label']
    return dict(unit_id='ms-c03'+label[-1].lower(),label=label,chapter_id='ms-c03',
        check_unit='ms-c03'+label[-1].lower(),id_prefix='ms-c03'+label[-1].lower(),
        title_prefix='Unit '+label,header='Unit '+label+' (ms-c03'+label[-1].lower()+')',
        menu_title='Chapter 3 · Numbers and money',genre='Shopping and money',
        goal=cfg['unit_goal'], blocks=cfg['goals'], prerequisites=['ms-c01','ms-c02'],
        prerequisite_units=(['ms-c03a'] if label == '3B' else
                            ['ms-c03a','ms-c03b'] if label == '3C' else []),
        prereq_grammar=['ms-c02-g03','ms-c02-g04','ms-c02-g12'],
        word_scope=cfg['core']+cfg['recognition']+cfg['revision'],
        components=lambda ledger:components(ledger,cfg))
