"""Step 4 pilot: full chapter suites for Malay units 1, 2A and 2B, plus the
fast-course summary packs for chapters 1 and 2.

Authoring rules (enforced at build time):
- Every Malay target span is wrapped in «…». It is checked against the ledger,
  register, affix and Malaysian-form rules like any other learner-facing Malay.
- A Malay word quoted only as the root or standard form named in a Kata-Kata
  card note (for example ‹makan› in makan → makanan) is wrapped in ‹…›. Only the
  Malaysian-form check applies, and the word must be listed with its source in
  curriculum/malay-mentions.json.
- Unmarked text is Japanese or English. If it contains a ledger word, the build
  fails, so Malay cannot slip past the checks unmarked.
- Explainers and rubrics are Japanese or English. All Japanese is a draft
  awaiting native review.
- Lines starting with "■ " print as sub-headings.

Content modules: ms_c01 (unit 1), ms_c02a (unit 2A), ms_c02b (unit 2B), fast.
"""
import csv
import io
import json
import re
from pathlib import Path

from language_checks import Checker, norm, tokens

ROOT = Path(__file__).resolve().parents[1]
TARGET = re.compile(r'«([^«»‹›]+)»')
MENTION = re.compile(r'‹([^«»‹›]+)›')
JA_DRAFT = '（日本語は下書きです。ネイティブ・スピーカーの確認待ち）'
BM_NOTE = ('No Malay explainer for Stage 1 units: explainers and rubrics are in Japanese or English '
           '(Sam, 11 Nov 2026). Select 日本語 or English.')
# English words that are spelt like a ledger entry. Unmarked use of these is
# allowed; anything else in the ledger must be marked «…» or ‹…›.
ENGLISH_HOMOGRAPHS = {'main', 'oh', 'pun', 'best', 'bank', 'hotel', 'menu', 'fail', 'golf', 'set', 'unit'}

# Grammar points taught in the pilot (IDs extend the step 2 chapter points).
GRAMMAR = [
    dict(id='ms-c01-g02', chapter_id='ms-c01', label='Time-of-day greetings: Selamat pagi, tengah hari, petang, malam'),
    dict(id='ms-c01-g03', chapter_id='ms-c01', label='Titles before names; a title as polite "you"'),
    dict(id='ms-c01-g04', chapter_id='ms-c01', label='Asking after someone: Apa khabar?, pula, pun'),
    dict(id='ms-c01-g05', chapter_id='ms-c01', label='Thanks, apology and polite attention; ya and tidak'),
    dict(id='ms-c01-g06', chapter_id='ms-c01', label='Taking leave: minta diri dulu, Jumpa ___, Selamat jalan / tinggal'),
    dict(id='ms-c01-g07', chapter_id='ms-c01', label='Malay spelling and sounds'),
    dict(id='ms-c01-g08', chapter_id='ms-c01', label='Standard and spoken forms (tidak / tak)'),
    dict(id='ms-c02-g02', chapter_id='ms-c02', label='Pronouns and choosing a word for "you"'),
    dict(id='ms-c02-g03', chapter_id='ms-c02', label='Noun + noun sentences with no verb "to be"'),
    dict(id='ms-c02-g04', chapter_id='ms-c02', label='Question words siapa, apa, di mana in statement order'),
    dict(id='ms-c02-g05', chapter_id='ms-c02', label='Origin: orang + country, asal, dari, kampung'),
    dict(id='ms-c02-g06', chapter_id='ms-c02', label='ini and itu'),
    dict(id='ms-c02-g07', chapter_id='ms-c02', label='-nya: his, her, its; the'),
    dict(id='ms-c02-g08', chapter_id='ms-c02', label='Place with di: tinggal di, kerja di, belajar di'),
    dict(id='ms-c02-g09', chapter_id='ms-c02', label='suka and hobi'),
    dict(id='ms-c02-g10', chapter_id='ms-c02', label='pe- person nouns'),
    dict(id='ms-c02-g11', chapter_id='ms-c02', label='-an thing nouns'),
    dict(id='ms-c02-g12', chapter_id='ms-c02', label='-kah questions, adakah and bolehkah'),
    dict(id='ms-c02-g13', chapter_id='ms-c02', label='juga and pun; kami and kita'),
    dict(id='ms-c02-g14', chapter_id='ms-c02', label='Family and having: ada, dengan'),
]


GRAMMAR.extend([
    dict(id='ms-c03-g02', chapter_id='ms-c03', label='Numbers through one million: cardinal building blocks'),
    dict(id='ms-c03-g03', chapter_id='ms-c03', label='Age with umur and tahun; telephone digit sequences'),
    dict(id='ms-c03-g04', chapter_id='ms-c03', label='Asking and giving fictional prices in ringgit and sen'),
    dict(id='ms-c03-g05', chapter_id='ms-c03', label='ke- ordinals and kali; irregular first'),
    dict(id='ms-c03-g06', chapter_id='ms-c03', label='Fractions, decimals, percentages'),
    dict(id='ms-c03-g07', chapter_id='ms-c03', label='ke-an measurement nouns and units'),
    dict(id='ms-c03-g08', chapter_id='ms-c03', label='Payments, totals, cash, card and change'),
])

GRAMMAR.extend([
    dict(id='ms-c04-g02', chapter_id='ms-c04', label='Clock time with pukul and the parts of the day; suku and setengah'),
    dict(id='ms-c04-g03', chapter_id='ms-c04', label='Days of the week, days around today and dates (hari apa, hari bulan)'),
    dict(id='ms-c04-g04', chapter_id='ms-c04', label='Frequency: setiap, selalu, biasanya, kadang-kadang, jarang, tidak pernah, sekali'),
    dict(id='ms-c04-g05', chapter_id='ms-c04', label='When: bila, pukul berapa, hari apa; pukul (clock) versus jam (duration)'),
    dict(id='ms-c04-g06', chapter_id='ms-c04', label='Aspect markers: sudah, belum, sedang, masih, akan, baru'),
    dict(id='ms-c04-g07', chapter_id='ms-c04', label='Experience with pernah, belum pernah, tidak pernah'),
    dict(id='ms-c04-g08', chapter_id='ms-c04', label='Daily routine with root verbs; mula, habis, sampai; awal and lambat; sebelum and selepas'),
])


# Product and feature names, not Malay text (removed before the unmarked-Malay guard only).
PRODUCT_NAMES = ['Cikgu, Sensai!', 'Cikgu Sensai', 'Sedia Kelas', 'Tanya Cikgu', 'Kata-Kata', 'Dunia', 'Jambatan',
                 'Susun Ayat', 'Hanashishou', 'Teacher Desk',
                 # Kata-Kata Dunia scene titles (names of scenes, quoted as titles)
                 'Sembang di pantri', 'Pagi di pejabat', 'Ke bank dan pejabat pos', 'Pasar pagi',
                 'Satu hari Encik Tanaka', 'Hujan petang', 'Cuti ke pantai', 'Bangun pagi']


def strip(s):
    return s.replace('«', '').replace('»', '').replace('‹', '').replace('›', '')

def marked(s):
    return TARGET.findall(s), MENTION.findall(s)


class Ledger:
    def __init__(self, root=ROOT):
        text = (root / 'curriculum/reference/katakata/malay-ledger.csv').read_text()
        self.rows = {r['ID']: r for r in csv.DictReader(io.StringIO(text))}
        self.checker = Checker(root)

    def row(self, lid):
        return self.rows[lid]

    def word_id(self, row):
        """Kata-Kata card ID where one exists (chapter card first), else the ledger ID."""
        cards = [c.strip() for c in row['Kata-Kata (card IDs)'].split(',') if c.strip()]
        kelas = [c for c in cards if re.match(r'ms-c\d\d-\d+$', c)]
        return (kelas or cards or [row['ID']])[0]

    def terms_in(self, text):
        """Ledger rows matched in a Malay span, longest match first (as the checker does)."""
        ts = tokens(text); i = 0; found = []
        while i < len(ts):
            if ts[i] in self.checker.proper:
                i += 1; continue
            for size in range(min(self.checker.maxlen, len(ts) - i), 0, -1):
                term = ' '.join(ts[i:i + size])
                rows = self.checker.entries.get(term)
                if rows and size > 1 and self.checker.compositional(term, ts[i:i + size]):
                    continue
                if not rows and size == 1:
                    d = self.checker.derivation(term, 9)
                    rows = self.checker.entries.get(d[0]) if d else None
                if rows:
                    found.extend(rows); i += size; break
            else:
                i += 1
        return found

    def ids_for(self, terms):
        out = []
        for t in terms:
            rows = self.checker.entries.get(norm(t))
            if not rows:
                raise ValueError('Tagged word not in ledger: ' + t)
            out.append(self.word_id(rows[0]))
        return list(dict.fromkeys(out))


def malay_words(lines):
    """Number of Malay words inside «…» spans (for listening-length minimums)."""
    return sum(len(tokens(span)) for line in lines for span in TARGET.findall(line))


def english_words(lines):
    return sum(len(re.findall(r"[A-Za-z0-9āÀ-ÿ'’-]+", strip(line))) for line in lines)


def vocab(ledger, groups):
    """Vocabulary lines from ledger rows: term, EN and JA meanings, ledger ID, example."""
    lines = []
    for heading, entries in groups:
        lines.append('■ ' + heading)
        for entry in entries:
            lid, example = entry[0], entry[1]
            opts = entry[2] if len(entry) > 2 else {}
            r = ledger.row(lid)
            term = opts.get('display') or '«' + r['Malay'] + '»'
            en = opts.get('en') or GLOSS.get(lid, {}).get('en') or r['Meaning (EN)']
            ja = opts.get('ja') or GLOSS.get(lid, {}).get('ja') or r['Meaning (JA)']
            lines.append(f'{term} — {en} · {ja}  [{lid}]')
            lines.append('   e.g. ' + example)
    return lines


# Ledger glosses that contain Malay examples, re-marked so the Malay is checked.
GLOSS = {
    'L-0983': dict(en='also, too (after the word: «Saya pun baik»)'),
    'L-0988': dict(en='yes/no question opener («Adakah …?» = Is it …?)'),
    'L-0783': dict(en='Can …? / May I …? (polite)', ja='「〜できますか・〜してもいいですか」（«boleh» のていねいな形）'),
    'L-1016': dict(en='language («bahasa Melayu» = the Malay language)', ja='言語（«bahasa Melayu»＝マレー語）'),
    'L-1017': dict(en='Malay («bahasa Melayu», «orang Melayu»)', ja='マレー（«bahasa Melayu»＝マレー語）'),
    'L-1018': dict(en='English («bahasa Inggeris»)', ja='英語（«bahasa Inggeris»）'),
    'L-1020': dict(en='film, movie'),
    'L-1023': dict(en='to cook («suka masak» = like cooking)'),
    'L-1025': dict(en='the club-and-ball sport («main golf» = play golf)'),
    'L-1024': dict(en='singing along to recorded music (loan from Japanese)'),
    'L-0968': dict(en='the shuttlecock sport'),
    'L-1029': dict(en='to go on trips (spoken English loan)'),
    'L-1030': dict(en='walking in the hills (spoken English loan)'),
}


def core(ledger, ids):
    """Compact word list for fast-course packs: term, meanings, ledger ID (no example)."""
    out = []
    for lid in ids:
        r = ledger.row(lid); g = GLOSS.get(lid, {})
        out.append(f'«{r["Malay"]}» — {g.get("en", r["Meaning (EN)"])} · {g.get("ja", r["Meaning (JA)"])}  [{lid}]')
    return out


def pattern(n, fid, box, examples, en, ja, helps_en, helps_ja):
    """A pattern-focus section: box, numbered Q&A examples, explanation (EN, JA), Japanese bridge (EN, JA)."""
    return (f'Pattern {n} · {fid}', [
        'Pattern box: ' + box,
        *[f'{i}. {ex}' for i, ex in enumerate(examples, 1)],
        'Explanation: ' + en, '説明：' + ja,
        'Japanese helps or misleads: ' + helps_en, '日本語との比較：' + helps_ja])


def turns(script):
    """Dialogue lines: (speaker, line); a None speaker is a stage direction."""
    return [f'{s}: {t}' if s else '— ' + t for s, t in script]


def load_units():
    from . import ms_c01, ms_c02a, ms_c02b, ms_c03a, ms_c03b, ms_c03c, ms_c04a, fast
    return [u for u in [ms_c01.UNIT, ms_c02a.UNIT, ms_c02b.UNIT,
                       ms_c03a.UNIT, ms_c03b.UNIT, ms_c03c.UNIT, ms_c04a.UNIT,
                       *fast.PACKS] if u]


SKILLS = {'Opener': ['speaking'], 'Vocabulary': ['vocabulary'], 'Pattern and grammar': ['grammar'],
          'Drill': ['grammar', 'speaking'], 'Model conversation': ['speaking', 'reading'],
          'Listening': ['listening'], 'Reading and writing': ['reading', 'writing'], 'Task': ['speaking'],
          'Culture note': ['reading'], 'Test': ['listening', 'vocabulary', 'grammar', 'reading', 'speaking'],
          'Teaching plan': [], 'Fast-course pack': ['vocabulary', 'grammar', 'speaking']}
KIND = {'Opener': 'opener', 'Vocabulary': 'vocabulary', 'Pattern and grammar': 'model', 'Drill': 'drill',
        'Model conversation': 'model', 'Listening': 'listening', 'Reading and writing': 'reading',
        'Task': 'task', 'Culture note': 'culture', 'Test': 'test', 'Teaching plan': 'plan', 'Fast-course pack': 'model'}


def build_suite(ledger=None):
    """Return lesson dicts (unpaginated: 'sections') and unit records."""
    ledger = ledger or Ledger()
    lessons = []; units = []
    for unit in load_units():
        unit = dict(unit)
        comps = unit['components'](ledger) if callable(unit['components']) else unit['components']
        if unit['chapter_id'] == 'ms-c03':
            from .chapter3_common import mark_ch3
            for c in comps:
                c['sections'] = [(sec[0], [mark_ch3(line, ledger) for line in sec[1]], *sec[2:])
                                 for sec in c['sections']]
                c['key'] = [mark_ch3(line, ledger) for line in c['key']]
                c['explain'] = tuple(mark_ch3(line, ledger) for line in c['explain'])
                for test in c.get('tests', []):
                    for field in ('prompt', 'answer'):
                        test[field] = mark_ch3(test[field], ledger)
        titles = []
        for comp in comps:
            ctype = comp['type']
            kind_label = ctype
            title = unit['title_prefix'] + ' · ' + comp['title']
            cid = unit['id_prefix'] + '-' + comp['slug']
            meta = dict(
                id=cid, unit_id=unit.get('unit_id'), chapter_id=unit['chapter_id'], unit_label=unit.get('label'),
                check_unit=unit['check_unit'], component_type=ctype, sub_type=comp.get('sub_type'),
                skills=comp.get('skills') or SKILLS[kind_label], block=comp.get('block'),
                time_minutes=comp.get('minutes'), course_path=comp.get('course_path', unit.get('course_path', 'full')),
                grammar_points=comp.get('grammar', []), pattern_ids=comp.get('patterns', []),
                word_ids_override=comp.get('words'), genre=unit['genre'],
                can_do_goal=comp.get('goal'), prerequisite_chapters=unit.get('prerequisites', []),
                prerequisite_units=unit.get('prerequisite_units', []),
                prerequisite_grammar=comp.get('prereq_grammar', unit.get('prereq_grammar', [])),
                unit_word_scope=unit.get('word_scope'), menu_title=unit['menu_title'])
            tests = []
            for n, item in enumerate(comp.get('tests', []), 1):
                tests.append(dict(id=f'{cid}-{n:02}', chapter_id=unit['chapter_id'], component_id=cid,
                                  sub_type=item['sub_type'], grammar_points=item.get('grammar', []),
                                  word_ids=ledger.ids_for(item.get('words', [])),
                                  prompt=item['prompt'], answer_key=item['answer'], review_status='draft'))
            meta['tests'] = tests
            explain = comp['explain']
            lesson = dict(title=title, lang='Malay', level='A1', kind=kind_label, style='compact',
                          header=f'Cikgu, Sensai! / Malay · A1 · {unit["header"]} · {ctype}'
                                 + (f' · {comp["minutes"]} min' if comp.get('minutes') else '')
                                 + ' · Draft (Japanese awaiting native review)',
                          explainers=[('日本語', [explain[0], JA_DRAFT]), ('Bahasa Melayu', [BM_NOTE]),
                                      ('English', [explain[1]])],
                          sections=[(s[0], s[1], s[2] if len(s) > 2 else KIND.get(ctype, 'model'))
                                    for s in comp['sections']],
                          key=comp['key'], suite=meta)
            lessons.append(lesson); titles.append(title)
        units.append(dict(unit, titles=titles))
    return lessons, units


def paginate(lesson, fits):
    """Pack sections densely onto pages. A section that starts mid-page gets a
    "■" sub-heading; a page that starts mid-section is labelled "(cont.)".
    The raw (marked) text and its scope kind are kept per line."""
    explainers = [(label, [(x, 'explainer') for x in lines]) for label, lines in lesson['explainers']]
    stream = []
    for label, lines, kind in lesson['sections']:
        stream.append((None, label, kind))
        stream.extend((line, label, kind) for line in lines)
    body = []; label = None; current = []; section = None
    def flush():
        if current:
            body.append((label, list(current)))
    for line, sec, kind in stream:
        if line is None:
            section = sec
            item = None if not current else ('■ ' + sec, 'heading')
            if not current:
                label = sec
            if item is None:
                continue
        else:
            item = (line, kind)
        trial = current + [item]
        if fits(lesson, label, [strip(x) for x, k in trial]):
            current.append(item); continue
        # Start a new page; never leave a sub-heading orphaned at the bottom.
        carry = []
        if current and current[-1][1] == 'heading':
            carry = [current.pop()]
        if not current:
            raise ValueError(f'Line too long for one page: {lesson["title"]}: {line}')
        flush()
        if item[1] == 'heading':
            label, current = sec, []
        elif carry:
            label, current = carry[0][0][2:], [item]
        else:
            label, current = sec + ' (cont.)', [item]
        if not fits(lesson, label, [strip(x) for x, k in current]):
            raise ValueError(f'Line too long for one page: {lesson["title"]}: {line}')
    flush()
    keys = []; chunk = []
    for line in lesson['key']:
        if chunk and not fits(lesson, 'Teacher key (9/9)', [strip(x) for x, k in chunk + [(line, 'key')]]):
            keys.append(chunk); chunk = []
        chunk.append((line, 'key'))
    keys.append(chunk)
    keys = [('Teacher key' if len(keys) == 1 else f'Teacher key ({n}/{len(keys)})', c) for n, c in enumerate(keys, 1)]
    lesson['key_pages'] = len(keys)
    pages = explainers + body + keys
    for label, lines in pages:
        if not fits(lesson, label, [strip(x) for x, k in lines]):
            raise ValueError(f'Page overflow: {lesson["title"]} · {label}')
    lesson['pages'] = [dict(label=label, lines=[strip(x) for x, k in lines]) for label, lines in pages]
    lesson['_raw'] = [lines for label, lines in pages]
    del lesson['sections'], lesson['explainers'], lesson['key']


def guard(source, text, ledger, mentions):
    """Fail on Malay that is not marked, and on mentions without an approved source."""
    targets, said = marked(text)
    for m in said:
        if norm(m) not in mentions:
            raise ValueError(f'Mention ‹{m}› is not in curriculum/malay-mentions.json ({source})')
    rest = MENTION.sub(' ', TARGET.sub(' ', text))
    for name in PRODUCT_NAMES:
        rest = rest.replace(name, ' ')
    words = set(tokens(rest)) - ledger.checker.proper
    malay = [w for w in words if w in ledger.checker.entries and w not in ENGLISH_HOMOGRAPHS]
    if malay:
        raise ValueError(f'Unmarked Malay {sorted(malay)} in {source}: {text}')


def authored_scope(lessons, ledger):
    """Scope entries for the checker, generated from the markup. Keys match the bank."""
    mentions = {norm(k) for k in json.loads((ROOT / 'curriculum/malay-mentions.json').read_text())['mentions']}
    scope = {}; errors = []
    def safe_guard(source, raw):
        try:
            guard(source, raw, ledger, mentions)
        except ValueError as e:
            errors.append(str(e))
    for lesson in lessons:
        for pi, raw_lines in enumerate(lesson['_raw']):
            for li, (raw, kind) in enumerate(raw_lines):
                source = f'{lesson["title"]}|{pi}|{li}'
                safe_guard(source, raw)
                targets, said = marked(raw)
                scope[source] = dict(source_text=strip(raw), target_spans=targets, mention_spans=said,
                                     kind=kind, exclusion=None if targets else 'Japanese/English (marked source)')
        for item in lesson['suite']['tests']:
            for field in ('prompt', 'answer_key'):
                raw = item[field]
                safe_guard('test:' + item['id'], raw)
                targets, said = marked(raw)
                item[field] = strip(raw)
                scope[f'test:{item["id"]}|{field}'] = dict(source_text=item[field], target_spans=targets,
                                                           mention_spans=said, kind='test', exclusion=None)
    if errors:
        raise ValueError('\n'.join(errors))
    return scope


def component_words(lesson, ledger, units):
    """Word IDs traced from the marked Malay of a component (all pages), and the
    subset that earlier chapters or units teach (its prerequisite words)."""
    found = []
    for raw_lines in lesson['_raw']:
        for raw, kind in raw_lines:
            for span in marked(raw)[0]:
                found.extend(ledger.terms_in(span))
    rows = list({r['ID']: r for r in found}.values())
    meta = lesson['suite']
    chapter = int(meta['chapter_id'][-2:])
    earlier_units = {lid for u in units if u.get('unit_id') in meta['prerequisite_units'] for lid in u.get('word_scope', [])}
    def placed(r):
        return min([int(x) for x in re.findall(r'Ch\s*(\d+)', r['Kata-Kata place'])] or [99])
    meta['word_ids'] = list(dict.fromkeys(ledger.word_id(r) for r in rows))
    meta['prereq_word_ids'] = list(dict.fromkeys(ledger.word_id(r) for r in rows
                                                 if placed(r) < chapter or r['ID'] in earlier_units))
