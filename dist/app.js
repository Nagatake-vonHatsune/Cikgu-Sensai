const $=id=>document.getElementById(id), chosen=new Set(), excluded=new Set();
const componentResources=catalogue.components.map(c=>{
 const l=lessons.find(x=>x.title===c.source_title);
 const pages=[...c.explainer_indices,...c.page_indices,...c.key_indices].map(i=>({...l.pages[i],component:c}));
 return {...c,lang:c.language,kind:c.component_type,pages,key_pages:c.key_indices.length};
});
const tagFields={sub_type:'Sub-type',skills:'Skill',grammar_points:'Grammar point',time_minutes:'Time (minutes)',prerequisites:'Prerequisites',course_path:'Course path',external_textbook_links:'External textbook',review_status:'Review status'};
function tagValues(c,k){const v=c[k];if(k==='prerequisites')return [...v.chapters,...v.grammar_points,...v.word_ids];if(k==='external_textbook_links')return v.map(x=>x.label);return Array.isArray(v)?v:v==null?[]:[String(v)];}
for(const [k,label] of Object.entries(tagFields)){
 const wrap=document.createElement('label');wrap.textContent=label;const select=document.createElement('select');select.id='tag-'+k;
 select.add(new Option('All',''));select.add(new Option('Unverified / not mapped','__unmapped'));
 for(const v of [...new Set(catalogue.components.flatMap(c=>tagValues(c,k)))].sort())select.add(new Option(k==='grammar_points'?(catalogue.grammar_registry.find(g=>g.id===v)?.label||v):v,v));
 select.onchange=draw;wrap.append(select);$('tag-filters').append(wrap);
}
function exerciseOptions(){const old=$('kind').value;$('kind').replaceChildren(new Option('All exercises',''));
 for(const t of $('view').value==='components'?catalogue.component_types:['Conversation','Grammar','Writing','Chapter pack','Lesson plan'])$('kind').add(new Option(t,t));
 if([...$('kind').options].some(o=>o.value===old))$('kind').value=old;
}
exerciseOptions();
function componentHeader(c){return [c.language,c.level,c.unit_id||c.chapter_id||'Standalone',c.component_type,c.time_minutes==null?'Time unverified':c.time_minutes+' min'].join(' / ');}
function chapterOptions(){
 const match=(c,k)=>!$(k).selectedIndex || c[k]===$(k).value;
 const levels=chapters.filter(c=>match(c,'lang')&&match(c,'level'));
 const refill=(id,label,values)=>{const el=$(id),old=el.value;el.replaceChildren(new Option(label,''));for(const [text,value] of values)el.add(new Option(text,value));el.value=values.some(pair=>pair[1]===old)?old:'';};
 refill('genre','All genres',[...new Set(levels.map(c=>c.genre))].map(x=>[x,x]));
 const options=levels.filter(c=>!$('genre').value||c.genre===$('genre').value);
 refill('chapter','Browse all chapters',options.map(c=>[c.lang+' · '+c.level+' · '+c.title+(c.sequence==='future'?' · Stage 2, not yet active':c.sequence==='supplementary'?' · Unplaced · provisional':''),String(chapters.indexOf(c))]));
 const current=chapters[$('chapter').value];
 refill('unit','All units in this chapter',(current?.units||[]).map(u=>['Unit '+u.label+(u.items.length?'':' · Content not yet written'),u.label]));
 $('unit-label').hidden=!current?.units;
 const route=navigation(),pos=route.indexOf(current);
 $('prev').disabled=pos<=0;$('next').disabled=pos<0||pos>=route.length-1;
 $('outcome').textContent=current?[current.status,current.goal,current.items.length+' resources.',current.sequence==='stage1'?(current.status.startsWith('Step 4')?'Full eleven-component suite for each unit (pilot draft), plus the fast-course summary pack. Japanese awaits native review.':'Existing lessons regrouped for review. Empty units are placeholders; the full chapter suite is not yet written.'):'Select individual resources below.'].filter(Boolean).join(' '):'Malay Stage 1 follows nine A1 chapters. Stage 2 and unplaced supplementary packs are outside that sequence.';
}
function navigation(){const current=chapters[$('chapter').value];return chapters.filter(c=>(c.sequence||c.lang)===(current?.sequence||current?.lang)&&['lang','level','genre'].every(k=>!$(k).value||!$(k).selectedIndex||c[k]===$(k).value));}
function visible(){
 const selected=chapters[$('chapter').value],unit=$('unit').value,topic=$('genre').value;
 if($('view').value==='components')return componentResources.filter(c=>(!selected||c.menu_title===selected.title)&&(!unit||c.unit_label===unit)&&(!topic||c.genre===topic)&&['lang','level','kind'].every(k=>!$(k).selectedIndex||$(k).value===c[k])&&Object.keys(tagFields).every(k=>{const v=$('tag-'+k).value,values=tagValues(c,k);return !v||(v==='__unmapped'?!values.length:values.includes(v));}));
 const titles=unit?selected.units.find(u=>u.label===unit).items:selected?selected.items:[...new Set(chapters.flatMap(c=>c.items))];return titles.map(t=>lessons.find(l=>l.title===t)).filter(l=>(!topic||chapters.some(c=>c.genre===topic&&c.items.includes(l.title)))).filter(l=>['lang','level','kind'].every(k=>!$(k).selectedIndex||$(k).value===l[k]));
}
function suiteInfo(){
 $('suite').replaceChildren();const g=chapters[$('chapter').value],ch=catalogue.chapters.find(c=>c.title===g?.title);if(!ch)return;
 const p=document.createElement('p');p.textContent='Draft chapter plan: '+ch.block_plan.length+' × 45-minute blocks. Self-study: approximately '+ch.self_study_hours.full+' hours (full), 9–10 hours (fast). Prerequisites: '+(ch.prerequisites.length?ch.prerequisites.join(', '):ch.prerequisite_status)+'.';$('suite').append(p);
 const link=document.createElement('a');link.href=ch.kata_kata_set.source_url;link.textContent='Kata-Kata '+ch.kata_kata_set.pack_id+' and Sedia Kelas set';$('suite').append(link);
 const list=document.createElement('ul');for(const slot of catalogue.component_slots.filter(s=>s.chapter_id===ch.id&&(!$('unit').value||ch.units.find(u=>u.id===s.unit_id)?.label===$('unit').value))){const li=document.createElement('li');li.textContent=slot.unit_id+' · '+slot.component_type+': '+(slot.component_ids.length?slot.component_ids.length+' extractable item(s); '+(slot.status==='partial'?'suite incomplete':slot.status):'not yet authored');list.append(li);}
 const d=document.createElement('details');const summary=document.createElement('summary');summary.textContent='Eleven-component availability';d.append(summary,list);$('suite').append(d);
}
const keyCount=l=>l.key_pages||1, keyPages=l=>l.pages.slice(-keyCount(l));
function prerequisiteCheck(c){
 const req=c.prerequisites,units=req.units||[],unitOf=id=>catalogue.components.find(x=>x.id===id)?.unit_id,items=catalogue.test_items.filter(t=>(req.chapters.includes(t.chapter_id)||units.includes(unitOf(t.component_id)))&&(t.grammar_points.some(g=>req.grammar_points.includes(g))||t.word_ids.some(w=>req.word_ids.includes(w))));
 if(!req.chapters.length&&!units.length){$('status').textContent='No prerequisites: this item can be taught first.';return;}
 if(!items.length){$('status').textContent='Prerequisites: '+req.chapters.concat(units).join(', ')+'. No tagged test items match yet, so no revision sheet can be added.';return;}
 const tests=componentResources.filter(t=>t.component_type==='Test'&&items.some(i=>i.component_id===t.id));
 const keep=[...chosen];chosen.clear();tests.forEach(t=>chosen.add(t));keep.forEach(x=>chosen.add(x));if(!chosen.has(c))chosen.add(c);
 $('status').textContent='Prerequisite check added first: '+items.length+' matching test item(s) ('+items.map(i=>i.id).join(', ')+') from '+tests.map(t=>t.title).join(' and ')+'. Use them as a ten-minute revision before this item. The whole test sheet is added; the matching items are listed here.';draw();
}
function pages(l){return [...document.querySelectorAll('[name=note]:checked')].map(n=>l.pages[+n.value]).concat(l.pages.slice(3,-keyCount(l)).filter(p=>!excluded.has(p)));}
function draw(){
 chapterOptions(); suiteInfo(); const items=visible();$('list').replaceChildren();
 for(const l of items){
  const c=document.createElement('article');c.className='card';
  c.innerHTML='<label><input type="checkbox"> '+l.title+'</label><span class="meta">'+[l.lang,l.level,l.kind].join(' · ')+'</span><details><summary>Preview and choose sections</summary></details>';
  const box=c.querySelector('input');box.checked=chosen.has(l);box.onchange=()=>{box.checked?chosen.add(l):chosen.delete(l);update();};
  for(const [i,p] of l.pages.slice(0,-keyCount(l)).entries()){
   const row=document.createElement('div');row.innerHTML=(i>=3?'<label><input type="checkbox"> '+p.label+'</label>':'<b>'+p.label+'</b>')+'<p>'+p.lines.join('<br>')+'</p>';
   const check=row.querySelector('input');if(check){check.checked=!excluded.has(p);check.onchange=()=>{check.checked?excluded.delete(p):excluded.add(p);update();};}
   c.querySelector('details').append(row);
  }
  if(l.component_type){
   const meta=document.createElement('p');meta.className='meta';meta.textContent=componentHeader(l)+' · Draft · '+l.genre+' · '+(l.skills.join(', ')||'Skills unverified');c.append(meta);
   const detail=document.createElement('p');detail.textContent=l.tag_status+'. '+l.key_scope+'. Japanese text awaits native review.';c.querySelector('details').append(detail);
   const prereq=document.createElement('button');prereq.textContent='Check prerequisites';prereq.onclick=()=>prerequisiteCheck(l);c.append(prereq);
  }
  $('list').append(c);
 }
 if(!items.length)$('list').textContent=chapters[$('chapter').value]?.units?.some(u=>u.label===$('unit').value&&!u.items.length)||chapters[$('chapter').value]?.items.length===0?'Content not yet written. This placeholder preserves the agreed teaching order.':'No matching worksheets.';
 update();
}
function update(){
 const ls=[...chosen],n=ls.flatMap(pages).length,k=$('key').value;
 $('summary').innerHTML='<b>'+ls.length+' selected</b><ol>'+ls.map(l=>'<li>'+l.title+'</li>').join('')+'</ol>'+(n?'Student pages 1–'+n:'')+(ls.length&&k!=='omit'?' · Keys '+(k==='end'?(n+1)+'–'+(n+ls.flatMap(keyPages).length):'1–'+ls.flatMap(keyPages).length+' (separate)'):'');
 $('download').disabled=!n;$('quick').replaceChildren();
 for(const [label,ps] of [['Print students',ls.flatMap(pages)],['Print keys',k==='omit'?[]:ls.flatMap(keyPages)],['Print everything',ls.flatMap(pages).concat(k==='omit'?[]:ls.flatMap(keyPages))]]){
  if(!ps.length)continue;const b=document.createElement('button');b.textContent=label;b.onclick=async()=>{const w=window.open('about:blank');if(!w){$('status').textContent='Allow a new tab for the PDF viewer.';return;}w.location.replace(URL.createObjectURL(new Blob([await pdf(ps)],{type:'application/pdf'})));$('status').textContent='Choose Print in the PDF viewer.';};$('quick').append(b);
 }
 $('all').textContent=visible().length&&visible().every(l=>chosen.has(l))?'Clear shown':'Select all shown';
}
let source;
async function pdf(ps){source ||= PDFLib.PDFDocument.load(bankPDF);const out=await PDFLib.PDFDocument.create();for(const [i,p] of (await out.copyPages(await source,ps.map(p=>p.index))).entries()){if(ps[i].component){p.drawText(componentHeader(ps[i].component),{x:46,y:820,size:8});}out.addPage(p);}return out.save();}
function xml(t){return t.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');}
async function word(ps){
 const z=new JSZip();
 const para=(s,size,br=false)=>'<w:p><w:pPr>'+(br?'<w:pageBreakBefore/>':'')+'<w:spacing w:after="180"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Noto Sans" w:hAnsi="Noto Sans" w:eastAsia="Noto Sans JP"/><w:sz w:val="'+size+'"/></w:rPr><w:t xml:space="preserve">'+xml(s)+'</w:t></w:r></w:p>';
 const body=ps.map((p,i)=>para("Cikgu, Sensai!",24,i>0)+(p.component?para(componentHeader(p.component),20):'')+para(p.component?.source_title||lessons.find(l=>l.pages.includes(p)).title,48)+para(p.label,40)+p.lines.map(s=>para(s,36)).join('')).join('');
 z.file('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>');
 z.file('_rels/.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>');
 z.file('word/document.xml','<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'+body+'<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="900" w:bottom="900" w:left="920" w:right="920"/></w:sectPr></w:body></w:document>');return z.generateAsync({type:'uint8array'});
}
function save(bytes,name){const url=URL.createObjectURL(new Blob([bytes]));const a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);}
async function download(){
 const ls=[...chosen],f=$('format').value,k=$('key').value,students=ls.flatMap(pages),keys=ls.flatMap(keyPages),z=new JSZip();
 if(f==='zip'){for(const l of ls){const ps=pages(l);if(k==='end')ps.push(...keyPages(l));if(ps.length)z.file(l.title+(l.id?' - '+l.id:'')+'.pdf',await pdf(ps));}if(k==='separate')z.file('Teacher keys.pdf',await pdf(keys));}
 else{const make=f==='pdf'?pdf:word;const bytes=await make(k==='end'?students.concat(keys):students);if(k!=='separate'){save(bytes,'Cikgu, Sensai! worksheets.'+f);return;}z.file('Student worksheets.'+f,bytes);z.file('Teacher keys.'+f,await make(keys));}
 save(await z.generateAsync({type:'uint8array'}),'Cikgu, Sensai! print pack.zip');
}
$('download').onclick=async()=>{try{await download();$('status').textContent='Pack ready.';}catch(e){$('status').textContent=e.message;}};
$('all').onclick=()=>{const items=visible(),remove=items.every(l=>chosen.has(l));items.forEach(l=>remove?chosen.delete(l):chosen.add(l));draw();};
$('view').onchange=()=>{exerciseOptions();$('tag-filters').closest('details').hidden=$('view').value==='packs';draw();};
for(const k of ['lang','level','kind'])$(k).onchange=draw;
for(const id of ['genre','chapter','unit'])$(id).onchange=()=>{if(id!=='unit')$('unit').value='';draw();};
for(const [id,step] of [['prev',-1],['next',1]])$(id).onclick=()=>{const route=navigation(),next=route[route.indexOf(chapters[$('chapter').value])+step];if(next){$('chapter').value=String(chapters.indexOf(next));$('unit').value='';draw();}};
for(const el of document.querySelectorAll('[name=note],#key,#format'))el.onchange=update;
draw();
