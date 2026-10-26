// Copyright 2026 Moira Astro contributors. SIL Open Font License 1.1; see ../../OFL.txt.
(() => {
  'use strict';
  const DATA=window.MOIRA_CATALOG;
  const $=id=>document.getElementById(id);
  const escape=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const clean=value=>typeof value==='string'?value:'';
  const fold=value=>clean(value).normalize('NFKD').replace(/\p{Diacritic}/gu,'').toLowerCase();
  const state={query:'',category:'all',selected:null,size:32,format:'woff2',theme:'light',limit:24,detailOpen:false};
  const mobile=matchMedia('(max-width:1000px)');
  const detail=$('detail-content'),dialog=$('detail-dialog');
  const entries=Array.isArray(DATA?.entries)?DATA.entries:[];
  const byId=new Map(entries.map(e=>[e.id,e]));
  const categories=Array.isArray(DATA?.categories)?DATA.categories:[];
  const searchIndex=new Map(entries.map(e=>[e.id,fold([e.search_text,e.name,e.meaning,e.category_label,...(e.aliases||[]),...(e.routes||[]).flatMap(r=>[r.text,...(r.codepoints||[]),...(r.unicode_names||[])])].join(' '))]));
  let fontError=null,copyMessage='',manualValue=null,lastTriggerId=null,lastCopy=null;
  let returnPosition={x:0,y:0},closeToFirstResult=false;
  const copyButtonLabels=new WeakMap(),copyFeedbackTimers=new Map();
  let copyGeneration=0;
  let examples={html:'',css:''};
  const frame=()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
  async function ensureFonts(){
    const results=await Promise.all(['MoiraWOFF','MoiraTTF'].map(f=>document.fonts.load(`24px ${f}`,'☉[lot:Fo]')));
    if(results.some(r=>r.length!==1))throw new Error('A font face was unavailable');
    await document.fonts.ready;return results;
  }
  const current=()=>byId.get(state.selected)||entries[0];
  function resetCopyFeedback(){
    copyGeneration++;
    for(const [button,timer] of copyFeedbackTimers){
      clearTimeout(timer);if(button.isConnected)button.textContent=copyButtonLabels.get(button);
    }
    copyFeedbackTimers.clear();return copyGeneration;
  }
  const features=(record={})=>({dlig:record.dlig!==false,zero:record.zero===true});
  function symbol(entry,role,size=state.size){
    const f=features(entry.preview?.features),text=entry.preview?.text??'';
    return `<span class="astro" aria-hidden="true" data-font-symbol="${escape(text)}" data-entry-id="${escape(entry.id)}" data-role="${role}" data-dlig="${f.dlig?1:0}" data-zero="${f.zero?1:0}" style="font-size:${size}px;font-feature-settings:'dlig' ${f.dlig?1:0},'zero' ${f.zero?1:0}">${escape(text)}</span>`;
  }
  function filtered(){
    const terms=fold(state.query).trim().split(/\s+/).filter(Boolean);
    return entries.filter(e=>(state.category==='all'||e.category===state.category)&&terms.every(term=>searchIndex.get(e.id).includes(term)));
  }
  function getState(){
    const result=filtered();
    return {...state,visibleIds:result.slice(0,state.limit).map(e=>e.id),resultIds:result.map(e=>e.id),fontError,copyStatus:copyMessage,manualValue,lastCopy:lastCopy?{...lastCopy}:null};
  }
  function updateHash(id){
    if(location.hash.slice(1)!==encodeURIComponent(id))history.pushState({moiraGuide:true},'','#'+encodeURIComponent(id));
  }
  function showDetail(open=false){
    if(mobile.matches){
      $('dialog-detail-host').append(detail);
      if(open&&!dialog.open){dialog.showModal();state.detailOpen=true;}
    }else{
      if(dialog.open)dialog.close();state.detailOpen=false;$('detail-host').append(detail);
    }
  }
  const resultFor=id=>[...document.querySelectorAll('[data-select-entry]')].find(e=>e.dataset.selectEntry===id);
  function resetDetailScroll(){
    detail.scrollTop=0;detail.scrollLeft=0;$('dialog-detail-host').scrollTop=0;
    dialog.scrollTop=0;dialog.scrollLeft=0;
    if(dialog.open)$('close-detail').focus({preventScroll:true});
  }
  function restoreResultFocus(){
    const first=closeToFirstResult;closeToFirstResult=false;
    const target=first?document.querySelector('[data-select-entry]'):resultFor(lastTriggerId);
    (target||$('guide-search')).focus({preventScroll:true});
    if(first)document.querySelector('.result-area').scrollIntoView({block:'start'});
    else if(target)window.scrollTo(returnPosition.x,returnPosition.y);
  }
  function selectEntry(id,{open=true,hash=true,trigger=null}={}){
    if(!byId.has(id))return;
    if(trigger?.dataset.selectEntry){lastTriggerId=trigger.dataset.selectEntry;returnPosition={x:scrollX,y:scrollY};}
    state.selected=id;copyMessage='';manualValue=null;lastCopy=null;resetCopyFeedback();
    if(hash)updateHash(id);render();showDetail(open);resetDetailScroll();
    if(!mobile.matches){if(trigger)resultFor(lastTriggerId)?.focus({preventScroll:true});else detail.focus({preventScroll:true});}
  }
  function renderCategories(){
    const all=[{id:'all',label:'All forms',count:entries.length},...categories];
    $('category-list').innerHTML=all.map(c=>`<button type="button" class="category-button" data-category="${escape(c.id)}" aria-pressed="${state.category===c.id}"><span>${escape(c.label)}</span><span class="count">${c.count}</span></button>`).join('');
    $('category-select').innerHTML=all.map(c=>`<option value="${escape(c.id)}">${escape(c.label)} · ${c.count}</option>`).join('');
    $('category-select').value=state.category;
  }
  function routeSummary(entry){
    const unicode=entry.routes?.find(r=>r.kind==='unicode');
    if(unicode)return unicode.codepoints?.join(' ')||'Unicode character';
    if(entry.routes?.some(r=>r.kind==='feature'))return 'OpenType feature';
    return 'Exact font token';
  }
  function renderResults(){
    const result=filtered(),visible=result.slice(0,state.limit);
    $('guide-search').value=state.query;$('clear-search').hidden=!state.query;
    $('reset-filters').hidden=!state.query&&state.category==='all';
    const label=state.category==='all'?'all categories':categories.find(c=>c.id===state.category)?.label||state.category;
    $('result-heading').textContent=`${result.length.toLocaleString()} ${result.length===1?'form':'forms'} · ${label}`;
    $('result-grid').hidden=!result.length;$('empty-state').hidden=!!result.length;
    $('empty-message').textContent=state.query?`No forms match “${state.query}” in ${label}. Try a body name, an exact token or a Unicode codepoint, or clear the filters.`:'Choose another category or clear the filters.';
    $('result-grid').innerHTML=visible.map(e=>`<button type="button" class="form-card ${e.category==='lots'?'wide':''}" data-select-entry="${escape(e.id)}" aria-pressed="${e.id===state.selected}" aria-label="${escape(e.name)}; ${escape(e.form_label||'font form')}"><span class="card-preview">${symbol(e,'catalog')}${e.spacing?'<span class="space-description">Spacing form</span>':''}</span><span class="card-copy"><span class="card-name">${escape(e.name)}</span><span class="card-meta">${escape(routeSummary(e))}</span><span class="card-form">${escape(e.form_label||e.category_label)}</span></span></button>`).join('');
    $('load-row').hidden=result.length<=visible.length;
    $('visible-count').textContent=`Showing ${visible.length.toLocaleString()} of ${result.length.toLocaleString()} forms`;
    $('load-more').textContent=`Show ${Math.min(24,result.length-visible.length)} more forms`;
    updateSelectionNotice();
  }
  function updateSelectionNotice(){
    const notice=$('selection-notice');if(!notice)return;
    const outside=!filtered().some(e=>e.id===state.selected);notice.hidden=!outside;
    const message=$('selection-notice-text');if(message)message.textContent=`${current()?.name||'This form'} is selected. It is outside the current results.`;
  }
  const routeName=r=>({unicode:'Unicode character',token:'Font token',word_alias:'Word-compatible token',text_sequence:'Text-presentation sequence',feature:'Feature route'}[r.kind]||r.label||'Copy route');
  const copyLabel=r=>({unicode:'Copy Unicode',token:'Copy token',word_alias:'Copy Word token',text_sequence:'Copy text form',feature:'Copy base character'}[r.kind]||'Copy value');
  const routeCopyContext=(entry,route)=>entry.spacing?`${(route.unicode_names||[]).join(' / ')||routeName(route)} (${(route.codepoints||[]).join(' ')})`:`${routeName(route).toLowerCase()} for ${entry.name}`;
  const routeButtonLabel=(entry,route)=>entry.spacing?'Copy '+((route.unicode_names||[]).join(' / ')||'spacing character').toLowerCase():copyLabel(route);
  function routeValue(entry,route){
    if(entry.spacing&&route.kind==='unicode')return escape(route.unicode_names?.join(' / ')||'Spacing character');
    if(['unicode','text_sequence'].includes(route.kind)){
      const f=features(route.features);
      return `<span class="astro" aria-hidden="true" data-font-symbol="${escape(route.text)}" data-entry-id="${escape(entry.id)}" data-role="route-${route.kind}" data-dlig="${f.dlig?1:0}" data-zero="${f.zero?1:0}" style="font-size:20px;font-feature-settings:'dlig' ${f.dlig?1:0},'zero' ${f.zero?1:0}">${escape(route.text)}</span>`;
    }
    return escape(route.text);
  }
  function buildExamples(entry){
    const route=entry.routes.find(r=>r.kind==='unicode')||entry.routes.find(r=>r.kind==='token')||entry.routes[0];
    if(!route){examples={html:'',css:''};return;}
    const f=features(route.features||entry.preview?.features);
    const name=entry.name.replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;');
    const literal=route.text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    examples.html=`<span class="astro-symbol" role="img"\n      aria-label="${name}">${literal}</span>`;
    examples.css='@font-face {\n  font-family: "Moira Astro";\n  src: url("fonts/MoiraAstro-Regular.woff2")\n       format("woff2");\n  font-weight: 400;\n  font-style: normal;\n}\n.astro-symbol {\n  font-family: "Moira Astro";\n  font-style: normal;\n  font-weight: 400;\n  font-synthesis: none;\n  white-space: pre;\n  font-feature-settings: "dlig" '+(f.dlig?1:0)+', "zero" '+(f.zero?1:0)+';\n}';
    $('example-context').textContent=`Example for ${entry.name}. Keep any required model, formula or historical witness in the accompanying chart data and label.`;
    $('html-example').textContent=examples.html;$('css-example').textContent=examples.css;
  }
  function renderDetail(){
    const entry=current();if(!entry)return;
    const routes=Array.isArray(entry.routes)?entry.routes:[];
    const notes=(entry.notes||[]).filter(n=>typeof n==='string'&&n);
    const contexts=(entry.contexts||[]).filter(c=>c.name||c.meaning);
    const related=(entry.related_ids||[]).map(id=>byId.get(id)).filter(e=>e&&e.id!==entry.id);
    const sources=(entry.sources||[]).filter(s=>s.title);
    const stress=state.size<(entry.recommended_em||18);
    detail.innerHTML=`<div id="selection-notice" class="manual-copy" hidden><p id="selection-notice-text"></p><button type="button" data-back-results>Go to results</button></div><header class="detail-heading"><span class="form-tag">Selected form · ${escape(entry.form_label||'Font form')}</span><h2 id="detail-title">${escape(entry.name)}</h2><p class="origin">${escape(entry.origin_label||'Moira Astro drawing')}</p></header>
      <div class="large-preview">${symbol(entry,'detail')}${entry.spacing?'<span class="space-description">Spacing character</span>':''}</div>
      <p class="preview-caption"><span>${state.size} px preview</span><span>${stress?'<strong>Stress size · review at '+(entry.recommended_em||18)+' px</strong>':'Reviewed starting size: '+(entry.recommended_em||18)+' px'}</span></p>
      <p class="meaning">${escape(entry.meaning||'Use this drawing with its named chart context.')}</p>
      ${entry.witness?`<p class="witness"><strong>Witness</strong><br>${escape(entry.witness)}</p>`:''}
      ${notes.length?`<section class="detail-section"><h3>Keep with the mark</h3><ul class="usage-notes">${notes.map(n=>'<li>'+escape(n)+'</li>').join('')}</ul></section>`:''}
      ${contexts.length>1?`<section class="detail-section"><h3>Named contexts</h3><dl class="context-list">${contexts.map(c=>'<dt>'+escape(c.name)+'</dt><dd>'+escape(c.meaning)+'</dd>').join('')}</dl></section>`:''}
      <section class="detail-section"><h3>Copy a route</h3>${!routes.some(r=>r.kind==='unicode')?'<p class="route-empty">This form has no direct Unicode character. Use its listed token or feature route.</p>':''}
      <div class="routes">${routes.map(r=>`<div class="route"><div class="route-head"><strong>${escape(r.label||routeName(r))}</strong><button type="button" data-copy-route="${escape(r.id)}" aria-label="Copy ${escape(routeCopyContext(entry,r))}">${escape(routeButtonLabel(entry,r))}</button></div><code>${routeValue(entry,r)}</code>${r.codepoints?.length?'<p class="codepoint">'+escape(r.codepoints.join(' '))+(r.unicode_names?.length?' · '+escape(r.unicode_names.join(' / ')):'')+'</p>':''}${r.note?'<p class="route-note">'+escape(r.note)+'</p>':''}</div>`).join('')}</div>
      <p id="copy-status" class="copy-status" role="status" aria-live="polite">${escape(copyMessage)}</p>
      <div id="manual-copy" class="manual-copy" ${manualValue===null?'hidden':''}><label for="manual-copy-value">Select and copy this value</label><textarea id="manual-copy-value" readonly spellcheck="false" aria-describedby="manual-copy-help">${escape(manualValue??'')}</textarea><p id="manual-copy-help">Automatic copying is unavailable. The exact value is selected for your normal copy command.</p></div></section>
      ${related.length?`<section class="detail-section"><h3>Related forms</h3><div class="related-list">${related.map(e=>`<button type="button" data-related-entry="${escape(e.id)}">${escape(e.name)} · ${escape(e.form_label||'form')}</button>`).join('')}</div></section>`:''}
      <section class="detail-section"><h3>Sources & provenance</h3>${sources.length?'<ul class="source-list">'+sources.map(s=>'<li>'+(s.url&&/^(https?:|\.{1,2}\/)/.test(s.url)?'<a href="'+escape(s.url)+'">'+escape(s.title)+'</a>':escape(s.title))+'</li>').join('')+'</ul>':'<p class="reference-note">Original design and definition records are retained in the project archive.</p>'}<p class="reference-note">The named model, meaning and formula remain part of the chart data alongside the copied text.</p></section>`;
    buildExamples(entry);
    updateSelectionNotice();
  }
  function render(){
    if(window.MOIRA_GUIDE?.ready&&!fontError){$('font-status').classList.remove('error');$('font-status').textContent='Both font formats loaded · existing forms and access routes';}
    document.documentElement.dataset.theme=state.theme;document.documentElement.dataset.format=state.format;
    $('theme-button').textContent=state.theme==='dark'?'Light theme':'Dark theme';$('theme-button').setAttribute('aria-pressed',String(state.theme==='dark'));
    $('size-select').value=state.size;$('format-select').value=state.format;
    renderCategories();renderResults();renderDetail();showDetail(false);
  }
  function updateCopyStatus(message,value=null){
    copyMessage=message;manualValue=value;
    const status=$('copy-status');if(status)status.textContent=message;
    const manual=$('manual-copy');if(manual)manual.hidden=value===null;
    if(value!==null){
      const area=$('manual-copy-value');area.value=value;area.focus({preventScroll:true});area.select();
      manual.scrollIntoView({block:'nearest',inline:'nearest'});
      area.scrollIntoView({block:'nearest',inline:'nearest'});
    }
    if(!dialog.open)$('guide-copy-announcement').textContent=message;
  }
  async function copyValue(value,label,route=null,trigger=null){
    if(typeof value!=='string')return;
    const generation=resetCopyFeedback();
    if(trigger){
      if(!copyButtonLabels.has(trigger))copyButtonLabels.set(trigger,trigger.textContent);
      trigger.textContent=copyButtonLabels.get(trigger);
    }
    lastCopy=null;updateCopyStatus(`Copying ${label}…`);
    let success=false,method='manual';
    try{if(navigator.clipboard?.writeText){await navigator.clipboard.writeText(value);success=true;method='clipboard';}}catch{/* Use selected-text fallback below. */}
    if(generation!==copyGeneration)return;
    if(!success){
      const helper=document.createElement('textarea');helper.value=value;helper.readOnly=true;
      helper.style.cssText='position:fixed;left:-10000px;top:0';const active=document.activeElement;
      (dialog.open?dialog:document.body).append(helper);helper.focus();helper.select();
      try{success=helper.selectionStart===0&&helper.selectionEnd===value.length&&document.execCommand('copy')===true;}catch{/* Manual copy stays readable. */}
      if(success)method='legacy';
      helper.remove();if(active?.isConnected)active.focus();
    }
    lastCopy={routeId:route?.id||null,text:value,label,success,method};
    if(success){
      const suffix=route?.kind==='feature'?'; enable the '+(route.requires_feature||'required')+' feature in the example below':'';
      updateCopyStatus(`Copied ${label}${suffix}.`);
      if(trigger){
        trigger.textContent='Copied';
        const timer=setTimeout(()=>{
          if(copyFeedbackTimers.get(trigger)!==timer)return;
          if(trigger.isConnected)trigger.textContent=copyButtonLabels.get(trigger);
          copyFeedbackTimers.delete(trigger);
        },1800);
        copyFeedbackTimers.set(trigger,timer);
      }
    }else{showDetail(true);updateCopyStatus(`Automatic copy is unavailable for ${label}. Select and copy the exact value below.`,value);}
  }
  async function setState(patch={}){
    if(patch.query!==undefined&&typeof patch.query!=='string')throw new Error('Search query must be text');
    if(patch.selected!==undefined&&!byId.has(patch.selected))throw new Error('Unknown guide form');
    if(patch.category!==undefined&&patch.category!=='all'&&!categories.some(c=>c.id===patch.category))throw new Error('Unknown guide category');
    if(patch.size!==undefined&&![18,24,32,48].includes(+patch.size))throw new Error('Unsupported preview size');
    if(patch.format!==undefined&&!['ttf','woff2'].includes(patch.format))throw new Error('Unknown font format');
    if(patch.theme!==undefined&&!['light','dark'].includes(patch.theme))throw new Error('Unknown theme');
    if(patch.query!==undefined||patch.category!==undefined)state.limit=24;
    for(const k of ['query','category','selected','format','theme'])if(patch[k]!==undefined)state[k]=patch[k];
    if(patch.size!==undefined)state.size=+patch.size;
    copyMessage='';manualValue=null;lastCopy=null;resetCopyFeedback();render();
    if(patch.selected!==undefined){lastTriggerId=null;updateHash(state.selected);showDetail(true);resetDetailScroll();}
    await frame();await ensureFonts();await frame();return getState();
  }
  function measure(){
    const rect=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height};};
    return {ready:window.MOIRA_GUIDE.ready,state:getState(),fontError,bodyOverflow:document.documentElement.scrollWidth>innerWidth,
      viewport:{width:innerWidth,height:innerHeight},fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),
      symbols:[...document.querySelectorAll('[data-font-symbol]')].filter(e=>e.getClientRects().length).map(e=>({text:e.dataset.fontSymbol,entry:e.dataset.entryId,role:e.dataset.role,dlig:e.dataset.dlig==='1',zero:e.dataset.zero==='1',fontSize:parseFloat(getComputedStyle(e).fontSize),fontFamily:getComputedStyle(e).fontFamily,advance:e.getBoundingClientRect().width,...rect(e)})),
      copyButtons:[...detail.querySelectorAll('[data-copy-route]')].map(e=>({route:e.dataset.copyRoute,...rect(e)})),
      detail:rect(detail),dialogOpen:dialog.open,manualVisible:!$('manual-copy')?.hidden,copyStatus:$('copy-status')?.textContent||''};
  }
  window.MOIRA_GUIDE={ready:false,getState,setState,measure};
  function fromHash(){
    let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{id=null;}
    if(byId.has(id))selectEntry(id,{hash:false,open:true});
    else if(id===''){
      if(dialog.open)dialog.close();state.detailOpen=false;state.selected=entries[0].id;
      copyMessage='';manualValue=null;lastCopy=null;resetCopyFeedback();render();
    }else{
      $('font-status').classList.add('error');
      $('font-status').textContent='This form link is unavailable in this build. Search by name or choose a form from the current index.';
    }
    frame().then(ensureFonts).catch(()=>{});
  }
  if(!entries.length){
    document.body.classList.remove('font-loading');document.body.classList.add('data-failed');
    $('font-status').classList.add('error');$('font-status').textContent='The character index could not load. Keep catalog.js in the assets folder and reload.';
    $('guide-summary').textContent='Character data unavailable';$('result-heading').textContent='The form index is unavailable';$('result-grid').hidden=true;
    $('empty-state').hidden=false;$('empty-message').textContent='The character data is unavailable. Download a complete copy of the guide, then reload.';
    document.querySelectorAll('button,input,select').forEach(control=>control.disabled=true);return;
  }
  state.selected=entries[0].id;
  const summary=DATA.summary||{};
  $('guide-summary').textContent=`${summary.forms??entries.length} forms · ${summary.mapped_characters??'—'} characters · ${(summary.canonical_tokens||0)+(summary.compatibility_aliases||0)} token routes`;
  $('guide-search').addEventListener('input',event=>{state.query=event.target.value;state.limit=24;renderResults();});
  $('clear-search').addEventListener('click',()=>{state.query='';state.limit=24;renderResults();$('guide-search').focus();});
  function reset(){state.query='';state.category='all';state.limit=24;render();$('guide-search').focus();}
  $('reset-filters').addEventListener('click',reset);$('empty-reset').addEventListener('click',reset);
  $('category-select').addEventListener('change',event=>setState({category:event.target.value}));
  $('category-list').addEventListener('click',event=>{const button=event.target.closest('[data-category]');if(button)setState({category:button.dataset.category});});
  $('size-select').addEventListener('change',event=>setState({size:+event.target.value}));
  $('format-select').addEventListener('change',event=>setState({format:event.target.value}));
  $('theme-button').addEventListener('click',()=>setState({theme:state.theme==='light'?'dark':'light'}));
  $('load-more').addEventListener('click',()=>{state.limit+=24;renderResults();});
  $('result-grid').addEventListener('click',event=>{const card=event.target.closest('[data-select-entry]');if(card)selectEntry(card.dataset.selectEntry,{trigger:card});});
  detail.addEventListener('click',event=>{
    const copy=event.target.closest('[data-copy-route]');
    if(copy){const route=current().routes.find(r=>r.id===copy.dataset.copyRoute);if(route)copyValue(route.text,routeCopyContext(current(),route),route,copy);}
    const related=event.target.closest('[data-related-entry]');if(related)selectEntry(related.dataset.relatedEntry);
    if(event.target.closest('[data-back-results]')){
      closeToFirstResult=true;
      if(dialog.open)dialog.close();else restoreResultFocus();
    }
  });
  document.querySelectorAll('[data-copy-example]').forEach(button=>button.addEventListener('click',()=>copyValue(examples[button.dataset.copyExample],`${button.dataset.copyExample.toUpperCase()} example for ${current().name}`,null,button)));
  $('close-detail').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('close',()=>{state.detailOpen=false;restoreResultFocus();});
  mobile.addEventListener('change',()=>{showDetail(false);if(!fontError)ensureFonts().catch(()=>{});});
  window.addEventListener('hashchange',fromHash);window.addEventListener('popstate',fromHash);
  render();
  Promise.race([ensureFonts(),new Promise((_,reject)=>setTimeout(()=>reject(new Error('Font loading timed out')),10000))]).then(async results=>{
    if(results.some(r=>r.length!==1))throw new Error('A font face was unavailable');
    await document.fonts.ready;await frame();document.body.classList.remove('font-loading');window.MOIRA_GUIDE.ready=true;
    $('font-status').textContent='Both font formats loaded · existing forms and access routes';if(location.hash)fromHash();
  }).catch(()=>{
    fontError='Moira Astro could not load';document.body.classList.remove('font-loading');document.body.classList.add('font-failed');
    $('font-status').classList.add('error');$('font-status').textContent='Moira Astro could not load. Symbol previews are hidden; names and copy values remain available. Check the local fonts folder and reload.';
  });
})();
