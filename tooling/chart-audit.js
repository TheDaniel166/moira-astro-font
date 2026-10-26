// Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
// Independent browser measurements, separate from the demonstration's own report.
window.auditMoiraChart = function () {
  const box = (element) => {
    const r = element.getBoundingClientRect();
    return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height};
  };
  const symbols = [...document.querySelectorAll('[data-font-symbol]')].map((element,index) => {
    const style = getComputedStyle(element), matrix = element.getScreenCTM?.();
    const scale = matrix ? Math.hypot(matrix.a,matrix.b) : 1;
    const advance = element.getComputedTextLength ? element.getComputedTextLength()*scale : element.getBoundingClientRect().width;
    return {index,source:element.dataset.fontSymbol,text:element.textContent,role:element.dataset.role||'',
      family:style.fontFamily,featureSettings:style.fontFeatureSettings,
      fontSize:parseFloat(style.fontSize),actualFontSize:parseFloat(style.fontSize)*scale,
      advance,box:box(element),cell:element.closest('td,th') ? box(element.closest('td,th')) : null};
  });
  const groups = (attribute) => [...document.querySelectorAll('['+attribute+']')].map(element => ({
    id:element.getAttribute(attribute),text:element.textContent,box:box(element),
    visible:!!element.getClientRects().length && getComputedStyle(element).visibility!=='hidden'
  }));
  const charts=[...document.querySelectorAll('svg')].filter(e=>e.querySelector('[data-callout-id]')).map(e=>({box:box(e),label:e.getAttribute('aria-label')}));
  const wheel=document.querySelector('#chart');
  const anchors=[...document.querySelectorAll('[data-anchor-id]')].map(e=>({id:e.dataset.anchorId,
    longitude:+e.dataset.longitude,x:+e.getAttribute('cx'),y:+e.getAttribute('cy')}));
  const aspectRows=[...document.querySelectorAll('[data-aspect][data-a][data-b]')].map(e=>({
    aspect:e.dataset.aspect,a:e.dataset.a,b:e.dataset.b,separation:+e.dataset.separation,orb:+e.dataset.orb,text:e.textContent}));
  const satellites=[...document.querySelectorAll('[data-satellite-composition]')].map(e=>{
    const parent=e.querySelector('[data-font-symbol]'),roman=e.querySelector('.roman'),style=getComputedStyle(e);
    return {id:e.dataset.satelliteComposition,label:e.getAttribute('aria-label'),align:style.alignItems,gap:parseFloat(style.gap),
      parent:box(parent),roman:box(roman),romanText:roman.textContent,
      parentSize:parseFloat(getComputedStyle(parent).fontSize),romanSize:parseFloat(getComputedStyle(roman).fontSize)};
  });
  return {ready:!!window.MOIRA_PILOT?.ready,state:window.MOIRA_PILOT?.getState(),
    viewport:{width:innerWidth,height:innerHeight},bodyOverflow:document.documentElement.scrollWidth>innerWidth+1,
    fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),symbols,
    callouts:groups('data-callout-id'),labels:groups('data-label-id'),charts,anchors,aspectRows,satellites,
    wheel:wheel ? {centerX:+wheel.dataset.centerX,centerY:+wheel.dataset.centerY,
      radius:+wheel.dataset.anchorRadius,origin:+wheel.dataset.sectorOrigin,orientation:wheel.dataset.orientation} : null,
    aspectLines:[...document.querySelectorAll('[data-aspect-pair]')].map(e=>e.dataset.aspectPair),
    selfReport:window.MOIRA_PILOT?.measure(),pageTitle:document.title,
    visibleText:document.body.innerText};
};
