// Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
window.auditMoiraGuide = function () {
  const box=e=>{const r=e.getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height};};
  const symbols=[...document.querySelectorAll('[data-font-symbol]')].filter(e=>e.getClientRects().length&&getComputedStyle(e).visibility!=='hidden').map(e=>{
    const style=getComputedStyle(e),surface=e.closest('.card-preview,.large-preview,.route');
    let clipped=false;
    const r=e.getBoundingClientRect();
    for(let ancestor=e.parentElement;ancestor&&ancestor!==document.body;ancestor=ancestor.parentElement){
      const s=getComputedStyle(ancestor),a=ancestor.getBoundingClientRect();
      if(/auto|scroll|hidden|clip/.test(s.overflowY)&& (r.top<a.top-.1||r.bottom>a.bottom+.1))clipped=true;
      if(/auto|scroll|hidden|clip/.test(s.overflowX)&& (r.left<a.left-.1||r.right>a.right+.1))clipped=true;
    }
    const modal=document.getElementById('detail-dialog');
    return {text:e.dataset.fontSymbol,entry:e.dataset.entryId,role:e.dataset.role,dlig:e.dataset.dlig==='1',zero:e.dataset.zero==='1',
      size:parseFloat(style.fontSize),family:style.fontFamily,features:style.fontFeatureSettings,advance:e.getBoundingClientRect().width,
      box:box(e),surface:surface?box(surface):null,clipped,occludedByDialog:modal.open&&!modal.contains(e)};
  });
  return {ready:window.MOIRA_GUIDE?.ready,state:window.MOIRA_GUIDE?.getState(),
    viewport:{width:innerWidth,height:innerHeight},bodyOverflow:document.documentElement.scrollWidth>innerWidth+1,
    fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),symbols,
    dialog:{open:document.getElementById('detail-dialog')?.open,box:box(document.getElementById('detail-dialog'))},
    buttons:[...document.querySelectorAll('#detail-content [data-copy-route]')].map(e=>({route:e.dataset.copyRoute,box:box(e)})),
    detailText:document.getElementById('detail-content').innerText,visibleText:document.body.innerText,
    htmlExample:document.getElementById('html-example').textContent,cssExample:document.getElementById('css-example').textContent};
};

window.bulkMoiraGuide = async function (ids) {
  window.__guideClipboard=[];
  Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async value=>{window.__guideClipboard.push(value);}}});
  const rows=[];
  for(const id of ids){
    await window.MOIRA_GUIDE.setState({query:'',category:'all',selected:id,size:32,format:'woff2',theme:'light'});
    const entry=window.MOIRA_CATALOG.entries.find(e=>e.id===id),e=document.querySelector('[data-role="detail"]');
    const style=getComputedStyle(e),r=e.getBoundingClientRect();
    const row={id,text:e.textContent,size:parseFloat(style.fontSize),family:style.fontFamily,
      dlig:e.dataset.dlig==='1',zero:e.dataset.zero==='1',advance:r.width,copies:[],
      htmlExample:document.getElementById('html-example').textContent,cssExample:document.getElementById('css-example').textContent};
    for(const route of entry.routes){
      const button=[...document.querySelectorAll('[data-copy-route]')].find(b=>b.dataset.copyRoute===route.id);
      if(!button)throw new Error('Missing copy action '+id+' '+route.id);
      const count=window.__guideClipboard.length;button.click();
      let copy=null;
      for(let step=0;step<10;step++){
        await new Promise(resolve=>setTimeout(resolve,1));
        copy=window.MOIRA_GUIDE.getState().lastCopy;
        if(copy?.routeId===route.id&&copy?.text===route.text)break;
      }
      if(!copy||window.__guideClipboard.length!==count+1)throw new Error('Copy action did not finish '+id+' '+route.id);
      row.copies.push({route:route.id,value:window.__guideClipboard.at(-1),receipt:copy});
    }
    rows.push(row);
    // Keep real hash/history navigation below browser flood protection. History
    // behavior is also tested separately with native controls/back navigation.
    await new Promise(resolve=>setTimeout(resolve,70));
  }
  return rows;
};
