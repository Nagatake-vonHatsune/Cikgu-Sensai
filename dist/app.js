const $=id=>document.getElementById(id), chosen=new Set(), excluded=new Set();
function visible(){return lessons.filter(l=>['lang','level','kind'].every(k=>!$(k).selectedIndex||$(k).value===l[k]));}
function pages(l){return [...document.querySelectorAll('[name=note]:checked')].map(n=>l.pages[+n.value]).concat(l.pages.slice(3,-1).filter(p=>!excluded.has(p)));}
function draw(){
 const items=visible();$('list').replaceChildren();
 for(const l of items){
  const c=document.createElement('article');c.className='card';
  c.innerHTML='<label><input type="checkbox"> '+l.title+'</label><span class="meta">'+[l.lang,l.level,l.kind].join(' · ')+'</span><details><summary>Preview and choose sections</summary></details>';
  const box=c.querySelector('input');box.checked=chosen.has(l);box.onchange=()=>{box.checked?chosen.add(l):chosen.delete(l);update();};
  for(const [i,p] of l.pages.slice(0,-1).entries()){
   const row=document.createElement('div');row.innerHTML=(i>=3?'<label><input type="checkbox"> '+p.label+'</label>':'<b>'+p.label+'</b>')+'<p>'+p.lines.join('<br>')+'</p>';
   const check=row.querySelector('input');if(check){check.checked=!excluded.has(p);check.onchange=()=>{check.checked?excluded.delete(p):excluded.add(p);update();};}
   c.querySelector('details').append(row);
  }
  $('list').append(c);
 }
 if(!items.length)$('list').textContent='No matching worksheets.';
 update();
}
function update(){
 const ls=[...chosen],n=ls.flatMap(pages).length,k=$('key').value;
 $('summary').innerHTML='<b>'+ls.length+' selected</b><ol>'+ls.map(l=>'<li>'+l.title+'</li>').join('')+'</ol>'+(n?'Student pages 1–'+n:'')+(ls.length&&k!=='omit'?' · Keys '+(k==='end'?(n+1)+'–'+(n+ls.length):'1–'+ls.length+' (separate)'):'');
 $('download').disabled=!n;$('quick').replaceChildren();
 for(const [label,ps] of [['Print students',ls.flatMap(pages)],['Print keys',k==='omit'?[]:ls.map(l=>l.pages.at(-1))],['Print everything',ls.flatMap(pages).concat(k==='omit'?[]:ls.map(l=>l.pages.at(-1)))]]){
  if(!ps.length)continue;const b=document.createElement('button');b.textContent=label;b.onclick=async()=>{const w=window.open('about:blank');if(!w){$('status').textContent='Allow a new tab for the PDF viewer.';return;}w.location.replace(URL.createObjectURL(new Blob([await pdf(ps)],{type:'application/pdf'})));$('status').textContent='Choose Print in the PDF viewer.';};$('quick').append(b);
 }
 $('all').textContent=visible().length&&visible().every(l=>chosen.has(l))?'Clear shown':'Select all shown';
}
let source;
async function pdf(ps){source ||= PDFLib.PDFDocument.load(bankPDF);const out=await PDFLib.PDFDocument.create();for(const p of await out.copyPages(await source,ps.map(p=>p.index)))out.addPage(p);return out.save();}
function xml(t){return t.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');}
async function word(ps){
 const z=new JSZip();
 const para=(s,size,br=false)=>'<w:p><w:pPr>'+(br?'<w:pageBreakBefore/>':'')+'<w:spacing w:after="180"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Noto Sans" w:hAnsi="Noto Sans" w:eastAsia="Noto Sans JP"/><w:sz w:val="'+size+'"/></w:rPr><w:t xml:space="preserve">'+xml(s)+'</w:t></w:r></w:p>';
 const body=ps.map((p,i)=>para("Cikgu, Sensai!",24,i>0)+para(lessons.find(l=>l.pages.includes(p)).title,48)+para(p.label,40)+p.lines.map(s=>para(s,36)).join('')).join('');
 z.file('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>');
 z.file('_rels/.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>');
 z.file('word/document.xml','<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'+body+'<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="900" w:bottom="900" w:left="920" w:right="920"/></w:sectPr></w:body></w:document>');return z.generateAsync({type:'uint8array'});
}
function save(bytes,name){const url=URL.createObjectURL(new Blob([bytes]));const a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);}
async function download(){
 const ls=[...chosen],f=$('format').value,k=$('key').value,students=ls.flatMap(pages),keys=ls.map(l=>l.pages.at(-1)),z=new JSZip();
 if(f==='zip'){for(const l of ls){const ps=pages(l);if(k==='end')ps.push(l.pages.at(-1));if(ps.length)z.file(l.title+'.pdf',await pdf(ps));}if(k==='separate')z.file('Teacher keys.pdf',await pdf(keys));}
 else{const make=f==='pdf'?pdf:word;const bytes=await make(k==='end'?students.concat(keys):students);if(k!=='separate'){save(bytes,'Cikgu, Sensai! worksheets.'+f);return;}z.file('Student worksheets.'+f,bytes);z.file('Teacher keys.'+f,await make(keys));}
 save(await z.generateAsync({type:'uint8array'}),'Cikgu, Sensai! print pack.zip');
}
$('download').onclick=async()=>{try{await download();$('status').textContent='Pack ready.';}catch(e){$('status').textContent=e.message;}};
$('all').onclick=()=>{const items=visible(),remove=items.every(l=>chosen.has(l));items.forEach(l=>remove?chosen.delete(l):chosen.add(l));draw();};
for(const k of ['lang','level','kind'])$(k).onchange=draw;
for(const el of document.querySelectorAll('[name=note],#key,#format'))el.onchange=update;
draw();
