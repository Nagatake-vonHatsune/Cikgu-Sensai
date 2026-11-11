"""Read-only content inventory for step 1, NOT the step 3 build guards.

Usage: python tools/restructure_audit.py /path/to/pinned/katakata
The reference checkout needs content/ledger, content/ms/kelas and tools/affix-guard.mjs.
Does not modify either the lesson text or reference repository.
"""
import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course import MALAY_CHAPTERS

def words(text):
    return re.findall(r"[a-z]+(?:[-'][a-z]+)*", text.lower())

def norm(text):
    return ' '.join(words(text))

def read_bank():
    text = (ROOT/'dist/bank.js').read_text()
    return json.loads(text[len('const lessons='):text.index(';\nconst bankPDF=')])

def main(reference):
    ledger_path = reference/'content/ledger/malay-ledger.csv'
    ledger = list(csv.DictReader(ledger_path.open()))
    packs = [json.loads((reference/f'content/ms/kelas/c{i:02}.json').read_text()) for i in range(1,10)]
    entries = defaultdict(list)
    for row in ledger:
        # Slash-separated alternatives are individual forms, not a sentence.
        for form in re.sub(r'\([^)]*\)', '', row['Malay']).split('/'):
            if norm(form):
                entries[norm(form)].append(row)
    max_length = max(len(key.split()) for key in entries)
    def chapter(row):
        nums = [int(n) for n in re.findall(r'ms-c(\d+)-', row['Kata-Kata (card IDs)'])]
        return min(nums) if nums else None
    allow_source = (reference/'tools/affix-guard.mjs').read_text()
    allow_block = re.sub(r'//[^\n]*', '', allow_source.split('new Set([')[1].split(']);')[0])
    allow = set(re.findall(r"'([^']+)'", allow_block))
    exempt = defaultdict(list)
    for pack in packs:
        for card in pack['cards']:
            if card['affix_tag'] in ('chunk','chunk*','lex') or card.get('recognise_only'):
                for w in words(card['term']):
                    exempt[w].append(card['id'])
    lessons = read_bank()
    by_title = {l['title']:l for l in lessons}
    raw = (ROOT/'curriculum/malay-course.txt').read_text().splitlines()
    source_units = {raw[i].split('|')[0]:(i+1,raw[i:i+6]) for i in range(0,len(raw),6)}
    groups = []
    for ch,(_,_,units) in enumerate(MALAY_CHAPTERS,1):
        for unit,names in units:
            groups.append((f'Unit {unit}',ch,names,[]))
    family_titles = ['Beli buah di pasar','Ambil bungkusan di lobi','Susun giliran di kaunter','Runding masa kerja pembaikan','Menimbang dapatan tinjauan kampus']
    family_resources = {}
    for filename in ['foundation.txt','advanced.txt']:
        for block in (ROOT/'curriculum'/filename).read_text().split('@ '):
            lines = block.strip().splitlines()
            if not lines or not lines[0].startswith('Malay|'):continue
            title = lines[0].split('|')[2]
            advanced = filename == 'advanced.txt'
            grammar = lines[-2].split('|')[1 if advanced else 0]
            writing = lines[-1].split('|')[1 if advanced else 0]
            family_resources[title] = [title,grammar,writing,title+' · Learner pack']
    groups[4][3].extend(family_resources['Beli buah di pasar'])
    groups.append(('Future chapter 12 · Stage 2, not yet active',12,[],family_resources['Ambil bungkusan di lobi']+['A clear pickup message']))
    for title in family_titles[2:]:
        groups.append((f'Supplementary · {title} · unplaced / provisional',None,[],family_resources[title]))
    groups.append(('Linked A2 extension · Lunch at a Malaysian stall',None,[],['Lunch at a Malaysian stall']))
    # Preserve the original link from both fruit-market and adjective materials.
    groups[10][3].append('Di, ke and dari')

    proper = {'emi','farah','osaka','jepun','pj','shah','alam','kl','sentral','aki','mei','qr','rm','am','pm','a','b','c','d'}
    records=[]
    registers={'nak':'mahu','tak':'tidak','dah':'sudah','ni':'ini','tu':'itu','sikit':'sedikit','saja':'sahaja','tapi':'tetapi','macam mana':'bagaimana','macam tu':'seperti itu'}
    def record(group,category,term,source,evidence,detail):
        records.append(dict(unit=group,category=category,term=term,source=source,evidence=evidence,detail=detail.rstrip()))
    segments_by_group={}
    for group,ch,names,related in groups:
        segments=[]
        for name in names:
            line,rows=source_units[name]
            for term in rows[1].split('|'):
                segments.append((f'curriculum/malay-course.txt:{line+1} · {name} · vocabulary',term.split('=')[0]))
            segments.append((f'curriculum/malay-course.txt:{line+2} · {name} · Malay explainer',rows[2].split('|')[1]))
            segments.append((f'curriculum/malay-course.txt:{line+3} · {name} · model',rows[3]))
            # Keep Malay prompts and all answers, removing only known English task cues.
            guide=rows[4].split('|')
            for part in guide[:2]:
                part=re.sub(r'\([^)]*\)', '',part)
                if name in ('Taste and colour','Size and shape','Directions and orientation'):
                    part=part.split('=',1)[-1]
                part=part.replace('Among three:', '').replace('less','')
                segments.append((f'curriculum/malay-course.txt:{line+4} · {name} · guided',part))
            segments.append((f'curriculum/malay-course.txt:{line+4} · {name} · answers',guide[2]))
        for title in related:
            item=by_title[title]
            if title not in ('Di, ke and dari','A clear pickup message','Lunch at a Malaysian stall'):
                segments.append((f'{title} / title',title.split(' · ')[0]))
            segments.append((f'{title} / Bahasa Melayu',item['pages'][1]['lines'][0]))
            for page in item['pages'][3:-1]:
                if page['label']=='Words and phrases':
                    for text in page['lines']:
                        segments.append((f'{title} / {page["label"]}',text.split(' · ')[0]))
                else:
                    for text in page['lines']:
                        segments.append((f'{title} / {page["label"]}',re.sub(r'^[ABC]\s{2,}','',text)))
        segments_by_group[group]=segments
        seen=set()
        for source,text in segments:
            tokens=words(re.sub(r'\bPasar Seni\b','',text))
            for term,standard in registers.items():
                if re.search(r'(?<![a-z])'+re.escape(term)+r'(?![a-z])',text.lower()):
                    key=('Register',term,source)
                    if key not in seen:
                        record(group,'Register',term,source,text,f'Standard: {standard}. No explicit standard-first/spoken-labelled teaching sequence in this resource. A mention in a Malay explainer does not establish prior teaching. Review against actual class delivery; do not infer learner progress.')
                        seen.add(key)
            for w in sorted(set(tokens)):
                if w.startswith('ber') or re.match(r'^be[kl]|^me[^aeiou\W]',w):
                    if w in allow:
                        status='Allow-list root in Kata-Kata; not a productive-affix violation.'
                    elif w in exempt:
                        status='Kata-Kata chunk/lex/recognition exemption: '+', '.join(exempt[w])+'. Context and chapter availability still need review.'
                    else:
                        status='Affix-shaped form, not exempt in the chapter snapshot. Morphological status unverified; do not automatically treat a prefix-shaped word as productive usage.'
                    key=('Affix inventory',w,source)
                    if key not in seen:
                        record(group,'Affix inventory',w,source,text,status)
                        seen.add(key)
            i=0
            while i<len(tokens):
                matches=[]
                for length in range(min(max_length,len(tokens)-i),0,-1):
                    key=' '.join(tokens[i:i+length])
                    if key in entries:
                        matches=entries[key];break
                if not matches:
                    key=tokens[i];length=1
                    if key not in proper and len(key)>1:
                        ident=('No exact ledger match',key,source)
                        if ident not in seen:
                            record(group,'No exact ledger match',key,source,text,'No exact term/alternative/containing phrase match in the pinned ledger. Surface-form candidate, not a proposed addition; compounds, inflections and instruction language need human review.')
                            seen.add(ident)
                else:
                    placements=[chapter(row) for row in matches if chapter(row) is not None]
                    ids=', '.join(row['ID'] for row in matches)
                    if ch is not None and ch<=9 and (not placements or min(placements)>ch):
                        category='Later chapter' if placements else 'Ledger present, chapter unassigned'
                        detail=(f'Earliest chapter card: Ch{min(placements)}.' if placements else 'Only scene/bridge/other placement; no chapter card ID establishes permission here.')+' '+ids+'; '+ '; '.join(row['Kata-Kata place'] for row in matches)
                        ident=(category,key,source)
                        if ident not in seen:
                            record(group,category,key,source,text,detail)
                            seen.add(ident)
                i+=length

    manual={
        'Unit 2A':['The unchanged Introductions pack mentions home (tinggal di PJ), which the expanded plan places in 2B. No new split or duplicate lesson has been authored; 2B is empty.'],
        'Unit 3B':['Beli buah di pasar / Jumlah buah / Pesanan buah teach biji and sebiji before chapter 8 (L-0344, L-0361). This was already early in the old course and remains unresolved.', 'The fruit-market practice uses manis/masam/besar/kecil (chapter 5), sameness with sama (chapter 6), and esok/pukul (chapter 4). These are preserved forward references.', 'The existing Lunch at a Malaysian stall link is retained at A2 as an optional extension, not relabelled A1 or treated as core 3B content. Its separate issues inventory follows below.'],
        'Unit 3C':['Order and floors uses tingkat and location-related vocabulary ahead of chapter 7. Existing gap, preserved.'],
        'Unit 5':['REORDER-CREATED dependency: Size and shape now precedes Asking where and Directions and orientation. Its model uses di atas / di bawah before those location lessons in chapter 7. Previously the direction/orientation unit was before Size and shape.', 'The existing Lunch at a Malaysian stall A2 extension remains linked, with a separate audit below.'],
        'Unit 6':['REORDER-CREATED dependency: Comparisons and superlatives now precedes chapter 7. Its model uses Antara tiga buku ini and its Malay explainer uses dalam kumpulan, before the ledger introduces antara/dalam in chapter 7. Previously the location/direction lessons preceded this resource. Buku remains a ledger-to-course sequencing discrepancy (chapter 8 card, already used in unit 5).'],
        'Unit 7':['Di, ke and dari remains linked to both existing location/direction resources; it is inventoried once here.'],
    }
    lines=['# Step 1 restructure: issues log by unit','', 'Date: 11 November 2026. Status: provisional audit; no content corrections made.', '',
        '## Scope and method','',
        'Existing Malay lesson wording is preserved by Sam’s instruction. This is an issues inventory, not language validation and not the step 3 build checks. All Japanese remains an AI draft awaiting native-speaker review.', '',
        f'Compared with {len(ledger)} ledger rows and {sum(len(p["cards"]) for p in packs)} chapter cards. Source revisions and SHA-256 file hashes are in `docs/restructure-sources.json`. The raw occurrence evidence is in `restructure-issues.csv`.', '',
        'The audit covers every legacy Malay unit, each Malay scenario family, the linked Di/ke/dari sheet and the A2 lunch extension. It reads Malay vocabulary entries, Malay explainers, models, guided examples, tasks and role cards. Generated lesson plans repeat these sources; English scheduling boilerplate and English/Japanese translations are excluded. Generic Malay instruction text is included and may itself exceed beginner vocabulary.', '',
        'Ledger matching is case-insensitive, longest phrase first, with slash alternatives and parenthetical annotations normalised. A missing exact match is a review candidate, not proof that a root is absent. Known proper names, role letters and English am/pm cues are excluded. A word that occurs only inside an intact ledger phrase is not treated as an independently taught word: isolated pagi/petang/malam are therefore flagged against their later standalone cards even though the greeting phrases occur in Ch1. Scene “primes Ch…” labels are reported but do not silently confer chapter permission. Chapter availability comes from existing ms-cXX card IDs; it is not inferred from a CEFR label.', '',
        'Register inventory includes nak/tak/dah and other observed short forms. These resources do not explicitly teach the standard/spoken pair in sequence. In particular nak already appears in the greetings Malay explainer before any standard mahu teaching; tak enters the fruit-market material before a standard-first contrast; dah occurs in the linked A2 lunch pack. The ledger has tidak/tak in Ch1, sudah/dah in Ch4 and mahu/nak in Ch5, but ledger presence is not proof that the existing Cikgu Sensai sheets taught the standard form first. Other pairs in the inventory are provisional usage mappings.', '',
        'The affix inventory reproduces Kata-Kata’s shape detection and records allow-list roots and chapter chunk exemptions separately. It lists all ber-/me-shaped forms encountered, including exemptions, rather than asserting that every match is an error. Future chapter 12 and unplaced advanced packs have no validated earlier-course sequence; their later-chapter compliance is not asserted.', '',
        '## Unit inventory','']
    for group,ch,names,related in groups:
        lines.extend(['### '+group,'', '**Existing resources:** '+(', '.join(names+related) or 'None. Placeholder only; no lesson text to audit.'), ''])
        for note in manual.get(group,[]):lines.extend([note,''])
        for category in ['No exact ledger match','Ledger present, chapter unassigned','Later chapter','Register','Affix inventory']:
            subset=[r for r in records if r['unit']==group and r['category']==category]
            terms=sorted(set(r['term'] for r in subset))
            if category=='Later chapter':
                vals=[]
                for term in terms:
                    r=next(r for r in subset if r['term']==term)
                    vals.append(term+' → '+r['detail'].split(';')[0])
                value='; '.join(vals)
            elif category=='Register':
                value=', '.join(t+' → '+registers[t] for t in terms)
            elif category=='Affix inventory':
                value='; '.join(t+(' [allow-list root]' if t in allow else ' [chapter chunk/lex exemption]' if t in exempt else ' [review]') for t in terms)
            else:value=', '.join(terms)
            empty='Not applicable: no content.' if not names+related else 'Not assessed: no approved chapter sequence for this pack.' if category in ('Later chapter','Ledger present, chapter unassigned') and (ch is None or ch>9) else 'None detected in the scoped text.'
            lines.append(f'- **{category}:** '+(value or empty))
        lines.append('')
    lines.extend(['## Decisions and limitations','',
        '- No new ledger words or patterns are proposed automatically. Candidate matches must be reconciled with roots, phrases and chapter placement before Sam approves any addition.',
        '- Units 2B, 8 and 9 have no existing dedicated material. The placeholders do not claim that the agreed chapter scope is covered.',
        '- Existing units still lack much of the charter’s expanded grammar/vocabulary coverage; that content work remains outside step 1.',
        '- The old 13 resources remain intact inside the 13 planned unit slots; several slots contain two resources and three slots are empty. This is not a claim that 13 complete charter units now exist.',
        '- B1/B2/C1 families retain their existing levels as unplaced, provisional supplementary packs. Chapter 12 is Stage 2, not yet active.',
        '- Step 2 chapter records/component tags, step 3 enforcement and new teaching content have not been implemented.', ''])
    out=ROOT/'dist/restructure-issues.md';out.write_text('\n'.join(lines))
    with (ROOT/'dist/restructure-issues.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['unit','category','term','source','evidence','detail'],lineterminator='\n');writer.writeheader();writer.writerows(records)
    paths=[ledger_path,reference/'tools/affix-guard.mjs']+sorted((reference/'content/ms/kelas').glob('c0[1-9].json'))
    manifest=dict(date='2026-11-11',katakata_commit='0f78179034552f85d4c0d7ac4cb9e185f8b8ac8a',cikgu_sensai_baseline='d4813c3cb56cdc0a7cbe756284faae78c1d194dd',hanashishou_commit='ea4f93e9471204e44f1e09886cabd50a44607283',files={str(p.relative_to(reference)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (ROOT/'docs/restructure-sources.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'{len(groups)} unit/pack inventories; {len(records)} occurrence records. No content modified.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('reference',type=Path)
    main(parser.parse_args().reference.resolve())
