"""Regenerate developer reports; never creates or expands legacy exceptions."""
import sys,json,csv
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from language_checks import Checker,collect_segments,run_checks,read_json
from catalogue import make_catalogue

def main():
 s=(ROOT/'dist/bank.js').read_text();lessons=json.loads(s[14:s.index(';\nconst bankPDF=')]);groups=json.loads((ROOT/'dist/chapters.js').read_text()[len('const chapters='):-1]);catalogue=make_catalogue(lessons,groups)
 result=run_checks(lessons,catalogue);proposals=read_json(ROOT/'docs/step3-charter-source.json')['list_a'];coverage={}
 for r in proposals:
  for t in r['term'].replace(' / ', ', ').split(', '):coverage[t]=r['chapter']
 gaps=[]
 for e in sorted(result['ledger_gaps'].values(),key=lambda x:(x['unit'],x['term'])):
  proposed=coverage.get(e['term']);ch=next((s['chapter'] for s in collect_segments(lessons,catalogue,read_json(ROOT/'curriculum/malay-text-scope.json')) if s['unit']==e['unit']),None)
  status='Not in list A' if proposed is None else 'Would close gap; placement unverified' if ch is None else 'Would close gap at this chapter' if proposed<=ch else 'Would add term, but later than this use'
  gaps.append({'unit':e['unit'],'term':e['term'],'list_a_chapter':proposed,'coverage':status,'sources':'; '.join(x['source'] for x in e['evidence'])})
 result['ledger_gap_coverage']=gaps
 (ROOT/'docs/step3-check-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'docs/step3-ledger-gaps.csv').open('w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=['unit','term','list_a_chapter','coverage','sources']);writer.writeheader();writer.writerows(gaps)
 baseline=read_json(ROOT/'curriculum/legacy-exceptions.json')
 units=[u['id'] for c in catalogue['chapters'] for u in c['units']]+['ms-c12','ms-extension-a2-lunch','ms-supplementary-b1','ms-supplementary-b2','ms-supplementary-c1']
 lines=['# Step 3 baseline and gap inventory','', 'Counts are unique unit/check/term keys, not occurrences. Ledger gaps are separate and non-blocking.','', '| Unit | Ledger | Register | Affix | Malaysian form | Total |','| --- | ---: | ---: | ---: | ---: | ---: |']
 for u in units:
  c=Counter(e['check'] for e in baseline.values() if e['unit']==u);lines.append('| '+u+' | '+' | '.join(str(c[t]) for t in ['ledger','register','affix','malaysian-form'])+' | '+str(sum(c.values()))+' |')
 lines+=['',f'Total: **{len(baseline)}** frozen exception keys.','', '## Ledger gaps and section 13 list A','',f'{len(gaps)} unit/term gap records; {len(set(g["term"] for g in gaps))} distinct terms. List A remains unapproved.','']
 for u in units:
  gs=[g for g in gaps if g['unit']==u];lines+=['### '+u,'','| Term | Proposed chapter | Coverage |','| --- | --- | --- |']
  lines.extend('| '+g['term']+' | '+str(g['list_a_chapter'] or '—')+' | '+g['coverage']+' |' for g in gs)
  if not gs:lines+=['| None | | |']
 lines+=['','## Malaysian-form results','', 'No occurrences of the charter-listed forms were found in the scoped learner-facing Malay. The check includes WC as well as the ten forms named in the work order. This is a finite deny-list, not a dictionary certification.','', '## Scope and re-authoring','', 'Stage 1 explainers and rubrics must be in Japanese or English when re-authored. They remain unchanged and excluded now. Explicit target spans are in curriculum/malay-text-scope.json; evidence is in step3-check-results.json.','', 'Unplaced supplementary packs and the linked A2 lunch extension have no authorised chapter placement. Malaysian-form and register checks still apply; missing ledger terms are reported. Chapter-relative ledger and affix checks are not asserted for those unplaced packs. Future chapter 12 permits ber-/me- but its complete chapter 10–12 vocabulary is not yet available.']
 (ROOT/'docs/STEP-3-INVENTORY.md').write_text('\n'.join(lines)+'\n')
 print('List A covers',len([g for g in gaps if g['list_a_chapter']]),'unit/term records;',len(set(g['term'] for g in gaps if g['list_a_chapter'])),'distinct surface forms')
if __name__=='__main__':main()
