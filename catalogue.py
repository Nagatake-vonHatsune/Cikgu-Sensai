"""Step 2 catalogue. Structural metadata only; never rewrites lesson text.

Reference files are byte-for-byte pinned upstream snapshots. Text matches are
provisional trace links, not a ledger compliance or pedagogical coverage check.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
TYPES = ['Opener', 'Vocabulary', 'Pattern and grammar', 'Drill', 'Model conversation',
         'Listening', 'Reading and writing', 'Task', 'Culture note', 'Test', 'Teaching plan']
GENRES = {'Social encounters':'Social life','Transactions':'Shopping and money','Dining':'Shopping and money',
          'Wayfinding':'Getting around','Schedules':'Time and routines','Daily routines':'Time and routines',
          'Description':'Describing and choosing','Choices and opinions':'Describing and choosing',
          'Housing':'Home','Work':'Work and study','Study':'Work and study','Governance':'Work and study','Campus services':'Work and study'}
FOCUS = ['Greetings and titles','Pronouns, pe-, -an, -kah and questions','Numbers, money, ke- and ke-an',
         'Time, frequency and aspect','Adjectives, Bagaimana and yang','Comparatives and superlatives',
         'Location and direction','Counters','Passive di-']
GOALS = ['Greet by time of day, use titles, ask after someone, take leave',
         'Introduce yourself (name, origin, work, home, hobby) and ask the same of others',
         'Ask and pay a price, check change, give age and phone number, say which one in a sequence',
         'Tell the time and day, describe a routine, say what is done, not yet done or under way',
         'Describe food, objects and feelings, and choose between items',
         'Compare two options, say two things are equal, pick the best of three',
         'Ask where something is, follow and give a route, name transport',
         'Order and count things with the right classifier','Read signs and notices, say what was done and by whom']
BLOCKS = [
 ('A', [('Recall',5),('Tanya Cikgu',5),('Vocabulary check',10),('Pattern focus',20),('First substitutions',5)]),
 ('B', [('Recall',5),('Drill ladder',20),('Model and gapped conversation',15),('Pair rehearsal',5)]),
 ('C', [('Recall',5),('Listening',15),('Reading or writing',10),('Independent task and change of plan',15)]),
 ('D', [('Mixed review',15),('Chapter test',10),('Self-check and feedback',10),('Next Kata-Kata set preview',10)]),
 ('E', [('Recall',5),('Dunia scene listening',10),('Role-play',15),('Free variation',10),('Hanashishou link where available',5)])]
SKILLS = {'Vocabulary':['vocabulary'],'Pattern and grammar':['grammar'],'Drill':['grammar','speaking'],
          'Model conversation':['speaking','reading'],'Reading and writing':['reading','writing'],
          'Task':['speaking'],'Teaching plan':[],'Opener':[],'Listening':['listening'],'Culture note':['reading'],'Test':[]}

# Test-item sub-types. 'writing' is used only by the A1 stage test (step 5h), whose writing paper is marked by rubric.
TEST_SUBTYPES = ['words','grammar','listening','reading','speaking','writing']

def norm(s): return ' '.join(re.findall(r"[a-z]+(?:[-'][a-z]+)*",s.lower()))
def stable(s): return hashlib.sha256(s.encode()).hexdigest()[:12]

def ledger_only_words():
    """Ledger rows placed in chapters 1 to 9 with no Kata-Kata chapter card: keyed by their
    Dunia card ID if they have one, else by the ledger ID (card pending). Same choice as suite.Ledger.word_id."""
    import csv, io
    out={}
    for r in csv.DictReader(io.StringIO((ROOT/'curriculum/reference/katakata/malay-ledger.csv').read_text())):
        place=[int(x) for x in re.findall(r'Ch\s*(\d+)',r['Kata-Kata place'])]
        cards=[c.strip() for c in r['Kata-Kata (card IDs)'].split(',') if c.strip()]
        if not place or min(place)>9 or any(re.match(r'ms-c\d\d-\d+$',c) for c in cards): continue
        key=(cards or [r['ID']])[0]
        out[key]={'id':key,'ledger_id':r['ID'],'term':r['Malay'],'gloss_en':r['Meaning (EN)'],'gloss_ja':r['Meaning (JA)'],
            'pos':r['POS'],'affix_tag':r['Affix tag'],'chapter':min(place),
            'status':'Kata-Kata Dunia card' if cards else 'ledger row; Kata-Kata card pending'}
    return out

def make_catalogue(lessons, groups):
    from suite import GRAMMAR
    packs=[json.loads((ROOT/f'curriculum/reference/katakata/c{n:02}.json').read_text()) for n in range(1,10)]
    words={c['id']:c for p in packs for c in p['cards']}
    words.update(ledger_only_words())
    patterns={f['id']:f for p in packs for f in p['frames']}
    grammar=[{'id':f'ms-c{n:02}-g01','label':label,'chapter_id':f'ms-c{n:02}','review_status':'draft'} for n,label in enumerate(FOCUS,1)]
    # Narrow, provisional grammar mappings for existing Malay resource families.
    focus_by_source = {
      'Greetings':('greetings','Greetings and titles'), 'Introductions':('introduction','Pronouns and self-introduction'),
      'Counting and quantities':('numbers','Numbers and Berapa'), 'Ringgit and sen':('prices','Prices and money'),
      'Order and floors':('ordinals','ke- ordinals'), 'Clock time':('clock','Clock time'),
      'Dates and days':('dates','Days and dates'), 'Frequency and routines':('frequency','Frequency'),
      'Taste and colour':('adjectives','Adjectives'), 'Size and shape':('adjectives','Adjectives'),
      'Comparisons and superlatives':('comparison','Comparatives and superlatives'),
      'Asking where':('location','Location questions'), 'Directions and orientation':('directions','Direction expressions'),
      'Di, ke and dari':('prepositions','di, ke and dari'), 'Beli buah di pasar':('prices','Prices and money')}
    for short,label in sorted(set(focus_by_source.values())):
        grammar.append({'id':'ms-g-'+short,'label':label,'chapter_id':None,'review_status':'draft'})
    grammar.extend({**g,'review_status':'draft'} for g in GRAMMAR)
    authored={u['unit_id']:u for g in groups for u in g.get('authored_units',[])}
    chapters=[];scenes=[];components=[];by_title={l['title']:l for l in lessons}
    for n,(p,g) in enumerate(zip(packs,groups[:9]),1):
        cid=f'ms-c{n:02}'; gid=f'{cid}-g01'
        units=[{'id':cid+re.sub(r'\d','',u['label']).lower(),'label':u['label']} for u in g['units']]
        blocks=[{'id':f'{u["id"]}-b{i}','unit_id':u['id'],'label':label,'minutes':45,
                 'can_do_goal':authored[u['id']]['blocks'][label] if u['id'] in authored else None,
                 'goal_status':'authored draft' if u['id'] in authored else 'awaiting pilot authoring',
                 'activities':[{'name':name,'minutes':minutes} for name,minutes in tasks]} for u in units for i,(label,tasks) in enumerate(BLOCKS,1)]
        chapters.append({'id':cid,'language':'Malay','level':'A1','title':g['title'],'genre':GENRES.get(g['genre'],g['genre']),
            'can_do_goals':GOALS[n-1:n],'pattern_ids':[f['id'] for f in p['frames']],
            'word_ids':[c['id'] for c in p['cards']], 'grammar_points':[gid], 'units':units,'block_plan':blocks,
            'recycled_items':{'word_ids':[],'pattern_ids':[], 'status':'not yet selected',
                'planned_pattern_returns':[{'pattern_id':f['id'],'destinations':[f'ms-c{k:02}' for k in (n+1,n+3) if k<=9]+['ms-stage1-review']} for f in p['frames']]},
            'scene_ids':[f'scene-a1-ms-origin-{n:02}'],'kata_kata_set':{'pack_id':p['id'],'sedia_kelas':p['sedia_kelas'],
                'source_url':f'https://github.com/Nagatake-vonHatsune/katakata/blob/0f78179034552f85d4c0d7ac4cb9e185f8b8ac8a/content/ms/kelas/c{n:02}.json'},
            'hanashishou_scene_ids':[], 'self_study_hours':{'full':3*len(units),'fast':[9,10],'status':'provisional planning estimate'},
            'review_status':'draft','sequence':'stage1','stage_id':'ms-stage1',
            'prerequisites':[f'ms-c{k:02}' for k in range(1,n)] if n<=2 else [],
            'prerequisite_status':('none (first chapter)' if n==1 else 'mapped in the step 4 pilot') if n<=2 else 'not yet mapped',
            'fast_pack_ids':[], 'pilot_status':'step 4 pilot draft' if all(u['id'] in authored for u in units) else None})
        scenes.append({'id':f'scene-a1-ms-origin-{n:02}','level':'A1','situation':p['scenario']['title_en'],
            'can_do_goals':GOALS[n-1:n],'genre':GENRES.get(g['genre'],g['genre']),
            'task':None,'change_of_plan':None,'listening_outline':None,'reading_text_type':None,'test_item_shapes':[],
            'review_status':'draft','source':'Kata-Kata scenario title and charter draft goal; localisation not yet authored'})
    # A placement is distinct from the source worksheet. Shared resources can be
    # extracted in either context without changing their CEFR level or wording.
    placements=[]
    for gi,g in enumerate(groups):
        g['genre']=GENRES.get(g['genre'],g['genre'])
        for u in g.get('units',[{'label':None,'items':g['items']} ])+([{'label':None,'items':g['fast_items']}] if g.get('fast_items') else [])+([{'label':None,'items':g['stage_items']}] if g.get('stage_items') else []):
            for title in u['items']:
                cid=f'ms-c{gi+1:02}' if gi<9 else 'ms-c12' if g.get('sequence')=='future' else None
                uid=(cid+re.sub(r'\d','',u['label']).lower()) if cid and u['label'] else None
                placements.append((g,u,title,cid,uid))
    for g,u,title,cid,uid in placements:
        l=by_title[title]; body=list(range(3,len(l['pages'])-1)); bundles=[]
        if l.get('suite'):
            components.append(authored_component(l,body,g,u))
            continue
        if l['kind']=='Chapter pack':
            bundles=[('Vocabulary',[body[0]]),('Model conversation',[body[1]]),('Drill',[body[2]]),('Task',[body[3]])]
        elif l['kind']=='Conversation':
            role=[i for i in body if 'Role ' in l['pages'][i]['label'] or 'Transfer' in l['pages'][i]['label']]
            bundles=[('Model conversation',[i for i in body if i not in role]),('Task',role)]
        else: bundles=[({'Grammar':'Pattern and grammar','Writing':'Reading and writing','Lesson plan':'Teaching plan'}[l['kind']],body)]
        lang={'Malay':'ms','English':'en','Japanese':'ja'}[l['lang']]
        for typ,indices in bundles:
            if not indices: continue
            text=' '+norm(' '.join(line for i in indices for line in l['pages'][i]['lines']))+' '
            matches=[wid for wid,c in words.items() if any(' '+norm(v)+' ' in text for v in c['term'].split(' / '))] if lang=='ms' else []
            family=title.split(' · ')[0]
            mapped=focus_by_source.get(family) if lang=='ms' else None
            comp={'id':f'{uid or cid or lang+"-standalone"}-{typ.lower().replace(" ","-")}-{stable(title)}',
                'source_title':title,'title':title+' · '+typ,'language':l['lang'],'level':l['level'],
                'chapter_id':cid,'unit_id':uid,'component_type':typ,'sub_type':None,
                'skills':SKILLS[typ],'genre':g['genre'],'grammar_points':['ms-g-'+mapped[0]] if mapped else [], 'word_ids':matches,'pattern_ids':[],
                'time_minutes':None,'prerequisites':{'chapters':[],'grammar_points':[],'word_ids':[]},
                'course_path':'full','external_textbook_links':[],'review_status':'draft','ja_review':'pending',
                'tag_status':'provisional; grammar mappings are draft; prerequisites, subtype, timings and textbook mapping await review',
                'trace_status':'exact surface matches only; not a complete word inventory or compliance check',
                'page_indices':indices,'explainer_indices':[0,1,2],'key_indices':[len(l['pages'])-1],
                'key_scope':'source worksheet key (may include answers for other sections)',
                'availability':'existing partial content','test_item_ids':[], 'menu_title':g['title'],'unit_label':u['label']}
            components.append(comp)
    slots=[{'id':f'{u["id"]}-{typ.lower().replace(" ","-")}', 'chapter_id':c['id'],'unit_id':u['id'],'component_type':typ,
            'component_ids':[x['id'] for x in components if x['unit_id']==u['id'] and x['component_type']==typ],
            'status':('complete (pilot draft)' if u['id'] in authored else 'partial') if any(x['unit_id']==u['id'] and x['component_type']==typ for x in components) else 'not yet authored'}
            for c in chapters for u in c['units'] for typ in TYPES]
    for c in chapters:
        c['fast_pack_ids']=[x['id'] for x in components if x['chapter_id']==c['id'] and x.get('fast')]
    tests=json.loads((ROOT/'curriculum/test-items.json').read_text())+[t for l in lessons if l.get('suite') for t in l['suite']['tests']]
    extra_blocks={'pronunciation':'ms-c01-pronunciation-block','writing-2b':'ms-c02b-writing-block','review-3a':'ms-c03a-review-block','writing-3c':'ms-c03c-writing-block','review-4b':'ms-c04b-review-block','writing-5':'ms-c05-writing-block','review-6':'ms-c06-review-block','writing-7':'ms-c07-writing-block','review':'ms-stage1-review'}
    from suite.stage1 import stage_record
    # Stage records carry the stage's CEFR label and its completion rule (step 5h): the data behind the charter's
    # "CEFR label shown in the Evaluator" (section 10, phase 3). Chapters and components keep their own 'level'.
    stages=[stage_record([x for x in components if x.get('check_unit')=='ms-stage1'])]
    return {'schema_version':1,'review_status':'draft','component_types':TYPES+['Fast-course pack'],'chapters':chapters,'stages':stages,'components':components,
        'component_slots':slots,'test_items':tests, 'scenes':scenes,
        'additional_blocks':[{'id':'ms-stage1-'+name,'after_unit':unit,'minutes':45,
            'component_ids':[x['id'] for x in components if x['id']==extra_blocks.get(name)],
            'status':'pilot draft' if name in extra_blocks else 'not yet authored'} for name,unit in [('pronunciation','ms-c01'),('writing-2b','ms-c02b'),('review-3a','ms-c03a'),('writing-3c','ms-c03c'),('review-4b','ms-c04b'),('writing-5','ms-c05'),('review-6','ms-c06'),('writing-7','ms-c07'),('review','ms-c09')]],
        'language_layers':[
            {'language':'Malay','chapter_ids':[c['id'] for c in chapters],'grammar_sequence':[x['id'] for x in grammar],
             'word_ids':list(words),'pattern_ids':list(patterns),'first_language_notes':[],
             'scene_chapter_map':[{'scene_id':c['scene_ids'][0],'chapter_id':c['id']} for c in chapters],
             'hour_budget':{'class_blocks':76,'block_minutes':45,'status':'provisional','note':'Stage 1 plan of 12 Nov 2026: 74 blocks plus 2 for the A1 stage test (written papers, then speaking)'},'review_status':'draft'},
            *[{'language':lang,'chapter_ids':[],'grammar_sequence':[],'word_ids':[],'pattern_ids':[],
               'first_language_notes':[],'scene_chapter_map':[],'hour_budget':None,'review_status':'draft',
               'status':'Supplementary legacy packs; language-specific syllabus not yet authored'} for lang in ['English','Japanese']]],
        'grammar_registry':grammar,'word_registry':words,'pattern_registry':patterns,
        'source_manifest':'docs/restructure-sources.json', 'future_chapters':[{'id':'ms-c12','level':'A2','status':'Stage 2, not yet active'}]}

def authored_component(l,body,g,u):
    """Step 4 suite component: tags come from the authored metadata, not inferred."""
    m=l['suite']; first_key=len(l['pages'])-l.get('key_pages',1)
    prereq_words=m.get('prereq_word_ids',[])
    return {'id':m['id'],'source_title':l['title'],'title':l['title'],'language':'Malay','level':'A1',
        'chapter_id':m['chapter_id'],'unit_id':m['unit_id'],'check_unit':m['check_unit'],'component_type':m['component_type'],
        'sub_type':m['sub_type'],'skills':m['skills'],'genre':g['genre'],'grammar_points':m['grammar_points'],
        'word_ids':m['word_ids_override'] or m['word_ids'],'pattern_ids':m['pattern_ids'],'time_minutes':m['time_minutes'],
        'block':m['block'],'can_do_goal':m['can_do_goal'],
        'prerequisites':{'chapters':m['prerequisite_chapters'],'units':m['prerequisite_units'],
                         'grammar_points':m['prerequisite_grammar'],'word_ids':prereq_words},
        'course_path':m['course_path'],'fast':m['course_path']=='fast','external_textbook_links':[],'review_status':'draft','ja_review':'pending',
        'tag_status':'full tag set (step 4 pilot draft; awaiting Sam\'s teaching review)',
        'trace_status':'word IDs traced from every marked Malay span against the ledger',
        'page_indices':list(range(3,first_key)),'explainer_indices':[0,1,2],'key_indices':list(range(first_key,len(l['pages']))),'check_indices':list(range(len(l['pages']))),
        'key_scope':'answer key for this component only','availability':'pilot draft','authored':True,
        'test_item_ids':[t['id'] for t in m['tests']],'menu_title':g['title'],'unit_label':u['label']}

def validate_test_item(item, catalogue):
    """Item tags identify what is tested, not merely words appearing in a prompt."""
    required={'id','chapter_id','component_id','sub_type','grammar_points','word_ids','prompt','answer_key','review_status'}
    if not required <= item.keys(): raise ValueError('Missing test-item fields')
    if not item['grammar_points'] and not item['word_ids']: raise ValueError('Test item needs at least one tested grammar point or word')
    if item['sub_type'] not in TEST_SUBTYPES: raise ValueError('Invalid test subtype')
    if not set(item['word_ids'])<=catalogue['word_registry'].keys(): raise ValueError('Unknown tested word')
    if not set(item['grammar_points'])<={g['id'] for g in catalogue['grammar_registry']}: raise ValueError('Unknown tested grammar')
    if item['chapter_id'] not in {c['id'] for c in catalogue['chapters']}: raise ValueError('Unknown test chapter')
    if not any(c['id']==item['component_id'] and c['component_type']=='Test' and c['chapter_id']==item['chapter_id'] for c in catalogue['components']): raise ValueError('Test component mismatch')
    if item['review_status'] not in ['draft','reviewed','approved']: raise ValueError('Invalid review status')

def prerequisite_items(component, catalogue):
    """Test items from prerequisite chapters (or earlier units of the same chapter)
    that test a grammar point or word the component assumes."""
    req=component['prerequisites']; units=set(req.get('units',[]))
    unit_of={c['id']:c.get('unit_id') for c in catalogue['components']}
    return [t for t in catalogue['test_items'] if (t['chapter_id'] in req['chapters'] or unit_of.get(t['component_id']) in units) and
        (set(t['grammar_points'])&set(req['grammar_points']) or set(t['word_ids'])&set(req['word_ids']))]

def write_catalogue(lessons, groups):
    data=make_catalogue(lessons,groups)
    for item in data['test_items']: validate_test_item(item,data)
    (ROOT/'dist/catalogue.js').write_text('const catalogue='+json.dumps(data,ensure_ascii=False)+';\n')
    return data
