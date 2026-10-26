// Copyright 2026 Moira Astro contributors. SIL Open Font License 1.1; see ../../../OFL.txt.
(() => {
  'use strict';
  const DATA = window.MOIRA_FIXTURES;
  const state = { fixture: 'balanced', theme: 'light', format: 'woff2' };
  const NS = 'http://www.w3.org/2000/svg';
  const $ = id => document.getElementById(id);
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const current = () => DATA.fixtures.find(f => f.id === state.fixture);
  let fontError = null, renderGeneration = 0;
  const symbol = (text, role, size = 18, extra = '') => `<span class="astro ${extra}" aria-hidden="true" data-font-symbol="${escape(text)}" data-role="${role}" style="font-size:${size}px">${escape(text)}</span>`;
  const longitude = value => {
    const sign = DATA.signs[Math.floor(value / 30) % 12];
    const minutes = Math.round((value % 30) * 60);
    return `${Math.floor(minutes / 60)}°${String(minutes % 60).padStart(2,'0')}′ ${sign.name}`;
  };
  const degrees = value => `${value.toFixed(1)}°`;
  const separation = (a,b) => Math.min(Math.abs(a-b),360-Math.abs(a-b));
  function aspectExamples(fixture) {
    const result=[];
    for (const definition of DATA.aspectDefinitions) {
      const matches=[];
      fixture.positions.forEach((a,i)=>fixture.positions.slice(i+1).forEach(b=>{
        const distance=separation(a.longitude,b.longitude), orb=Math.abs(distance-definition.angle);
        if(orb<=DATA.aspect_rule.orb_limit+1e-9) matches.push({a,b,definition,separation:distance,orb});
      }));
      matches.sort((a,b)=>a.orb-b.orb || a.a.id.localeCompare(b.a.id) || a.b.id.localeCompare(b.b.id));
      result.push(...matches.slice(0,2));
    }
    return result;
  }
  function node(tag, attributes={}, text=null) {
    const element=document.createElementNS(NS,tag);
    Object.entries(attributes).forEach(([name,value])=>element.setAttribute(name,String(value)));
    if(text!==null)element.textContent=text;
    return element;
  }
  function renderWheel(fixture, aspects) {
    const svg=$('chart'); svg.replaceChildren();
    svg.append(node('title',{id:'chart-title'},`${fixture.name}: twelve declared positions`));
    svg.append(node('desc',{id:'chart-description'},`${fixture.description} Equal 30-degree demonstration sectors. Exact longitude anchors connect to separated labels. The following declared-position table provides equivalent names, models, longitudes and motion states.`));
    const cx=430,cy=342,rad=201,outer=239;
    Object.assign(svg.dataset,{centerX:String(cx),centerY:String(cy),anchorRadius:String(outer+3),sectorOrigin:String(fixture.sector_origin),orientation:'degrees = 180 - (longitude - sector_origin)'});
    const point=(longitude,r)=>{const angle=(180-(longitude-fixture.sector_origin))*Math.PI/180;return [cx+Math.cos(angle)*r,cy+Math.sin(angle)*r];};
    const line=(p,q,klass,attrs={})=>svg.append(node('line',{x1:p[0],y1:p[1],x2:q[0],y2:q[1],class:klass,...attrs}));
    [154,201,239].forEach(r=>svg.append(node('circle',{cx,cy,r,class:'ring'})));
    for(let angle=0;angle<360;angle++) {
      const length=angle%30===0?12:angle%5===0?7:3;
      line(point(angle,201),point(angle,201-length),angle%30===0?'tick major-tick':'tick');
    }
    for(let i=0;i<12;i++) {
      line(point(i*30+fixture.sector_origin,77),point(i*30+fixture.sector_origin,201),'sector');
      const house=point(i*30+fixture.sector_origin+15,174);
      svg.append(node('text',{x:house[0],y:house[1]+4,'text-anchor':'middle',class:'house'},String(i+1)));
      const signPoint=point(i*30+15,221);
      const sign=node('text',{x:signPoint[0],y:signPoint[1]+6,'text-anchor':'middle',class:'astro sign','font-size':18,'data-font-symbol':DATA.signs[i].symbol,'data-role':'zodiac','aria-hidden':'true'},DATA.signs[i].symbol);
      svg.append(sign);
    }
    aspects.forEach(a=>line(point(a.a.longitude,151),point(a.b.longitude,151),'aspect-line '+(['sextile','trine'].includes(a.definition.id)?'harmonious':''),{'data-aspect-pair':a.a.id+':'+a.b.id}));
    svg.append(node('circle',{cx,cy,r:76,class:'center-disc'}));
    svg.append(node('text',{x:cx,y:cy-9,'text-anchor':'middle',class:'center-title'},state.fixture==='balanced'?'Fixture A':'Fixture B'));
    svg.append(node('text',{x:cx,y:cy+14,'text-anchor':'middle',class:'center-copy'},'DECLARED POSITIONS'));
    svg.append(node('text',{x:cx,y:cy+32,'text-anchor':'middle',class:'center-copy'},'NO ENGINE CALCULATION'));
    const objects=fixture.positions.map(p=>{const anchor=point(p.longitude,outer+3);return {p,anchor,side:anchor[0]<cx?'left':'right',targetY:anchor[1]};});
    ['left','right'].forEach(side=>{
      const list=objects.filter(o=>o.side===side).sort((a,b)=>a.targetY-b.targetY || a.p.longitude-b.p.longitude);
      let previous=69;
      list.forEach(o=>{o.y=Math.max(o.targetY,previous+42);previous=o.y;});
      if(list.length&&list.at(-1).y>618){list.at(-1).y=618;for(let i=list.length-2;i>=0;i--)list[i].y=Math.min(list[i].y,list[i+1].y-42);}
      list.forEach(({p,anchor,y})=>{
        const labelX=side==='left'?10:680, elbowX=side==='left'?191:669, endX=side==='left'?184:675;
        svg.append(node('polyline',{points:`${anchor[0]},${anchor[1]} ${elbowX},${anchor[1]} ${endX},${y-4}`,class:'leader','aria-hidden':'true'}));
        svg.append(node('circle',{cx:anchor[0],cy:anchor[1],r:2.2,class:'anchor','data-anchor-id':p.id,'data-longitude':p.longitude,'data-anchor-x':anchor[0],'data-anchor-y':anchor[1],'aria-hidden':'true'}));
        const group=node('g',{'data-callout-id':p.id,'data-label-id':p.id,'data-fixture-id':fixture.id,class:'callout','aria-hidden':'true'});
        group.append(node('title',{},`${p.name}; ${longitude(p.longitude)}; motion ${p.motion}`));
        group.append(node('text',{x:labelX,y:y+2,class:'astro',style:'font-size:18px','data-font-symbol':p.symbol,'data-role':'chart-body'},p.symbol));
        group.append(node('text',{x:labelX+34,y:y-3,class:'callout-name'},p.short_name));
        group.append(node('text',{x:labelX+34,y:y+12,class:'callout-degree'},longitude(p.longitude)));
        svg.append(group);
      });
    });
  }
  function render() {
    const fixture=current(),aspects=aspectExamples(fixture);
    document.documentElement.dataset.theme=state.theme;
    document.documentElement.dataset.format=state.format;
    $('fixture-select').value=state.fixture;$('format-select').value=state.format;
    $('theme-button').setAttribute('aria-pressed',String(state.theme==='dark'));
    $('theme-button').textContent=state.theme==='dark'?'Light theme':'Dark theme';
    $('overview-title').textContent=fixture.name;
    $('fixture-description').textContent=fixture.description;
    $('print-summary').textContent=`${fixture.name} · ${DATA.notice}`;
    renderWheel(fixture,aspects);
    $('positions').innerHTML=fixture.positions.map(p=>`<tr data-position-id="${p.id}"><td class="symbol-cell">${symbol(p.symbol,'position')}</td><th scope="row">${escape(p.name)}${p.model?`<span class="small-model">${escape(p.model)}</span>`:''}</th><td class="degree" data-longitude="${p.longitude}">${escape(longitude(p.longitude))}</td><td class="motion-cell">${symbol(DATA.motions[p.motion].symbol,'motion')}<span class="sr-only">${DATA.motions[p.motion].label}</span></td></tr>`).join('');
    $('motion-key').innerHTML=Object.values(DATA.motions).map(m=>`<span>${symbol(m.symbol,'motion-key')} ${m.label}</span>`).join('');
    $('aspects').innerHTML=aspects.length?aspects.map(a=>`<tr data-aspect="${a.definition.id}" data-a="${a.a.id}" data-b="${a.b.id}" data-separation="${a.separation}" data-orb="${a.orb}"><th scope="row" class="aspect-pair">${escape(a.a.name)} / ${escape(a.b.name)}<span class="aspect-name">${a.definition.name} · ${a.definition.angle}°</span></th><td>${symbol(a.definition.symbol,'aspect')}</td><td class="number">${degrees(a.separation)}</td><td class="number">${degrees(a.orb)}</td></tr>`).join(''):'<tr><td colspan="4">No pairs meet the declared display rule in this fixture.</td></tr>';
    $('specialist-legend').innerHTML=DATA.specialistLegend.map(e=>`${symbol(e.symbol,'specialist-aspect')}<div><strong>${e.name} · ${e.angle}°</strong><br>${escape(e.description)}</div>`).join('');
    $('lots').innerHTML=fixture.lots.map(l=>`<tr data-lot-id="${escape(l.id)}"><th scope="row" class="lot-name">${escape(l.name)}</th><td class="emblem">${symbol(l.symbol,'lot',18,'lot-symbol')}</td><td class="number">${escape(longitude(l.longitude))}</td></tr>`).join('');
    $('minor-bodies').innerHTML=fixture.minorBodies.map(p=>`<tr><th scope="row">${escape(p.name)}</th><td class="emblem">${symbol(p.symbol,'minor-body',p.em)}</td><td class="number">${escape(longitude(p.longitude))}</td></tr>`).join('');
    $('fixed-stars').innerHTML=DATA.fixedStars.map(s=>`<tr data-star-id="${escape(s.id)}"><th scope="row">${escape(s.name)} <span class="variant">${escape(s.variant)} form</span><span class="witness">${escape(s.witness)}</span></th><td class="emblem">${symbol(s.symbol,'fixed-star',s.em)}</td></tr>`).join('');
    $('satellites').innerHTML=DATA.satellites.map(s=>`<tr data-satellite-id="${s.id}"><th scope="row">${escape(s.name)}</th><td><span class="satellite" aria-label="${escape(s.accessible_label)}" data-satellite-composition="${s.id}">${symbol(s.parent_text,'satellite-parent',24)}<span class="roman" aria-hidden="true">${s.roman}</span></span></td></tr>`).join('');
    $('size-strip').innerHTML=DATA.sizeSamples.map(s=>`<div class="size-sample">${symbol(s.symbol,'size-sample',s.em)}<span class="size-label">${s.label}</span></div>`).join('');
  }
  const frame=()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
  async function setState(patch={}) {
    if(patch.fixture&&!DATA.fixtures.some(f=>f.id===patch.fixture))throw new Error('Unknown declared fixture');
    if(patch.theme&&!['light','dark'].includes(patch.theme))throw new Error('Unknown theme');
    if(patch.format&&!['ttf','woff2'].includes(patch.format))throw new Error('Unknown font format');
    Object.assign(state,patch);render();await frame();updateScrollHints();return getState();
  }
  const getState=()=>({...state,selectedFixture:JSON.parse(JSON.stringify(current())),data:JSON.parse(JSON.stringify(DATA))});
  const rect=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height};};
  function measure() {
    const svg=$('chart');
    return {ready:window.MOIRA_PILOT.ready,error:fontError,state:{...state},viewport:{width:innerWidth,height:innerHeight},bodyOverflow:document.documentElement.scrollWidth>innerWidth,
      fontFaces:[...document.fonts].map(f=>({family:f.family,status:f.status})),chart:rect(svg),
      symbols:[...document.querySelectorAll('[data-font-symbol]')].map(e=>{const style=getComputedStyle(e),scale=e instanceof SVGGraphicsElement?Math.abs(e.getScreenCTM().a):1;return {text:e.dataset.fontSymbol,role:e.dataset.role,format:state.format,fontSize:parseFloat(style.fontSize),actualFontSize:parseFloat(style.fontSize)*scale,fontFamily:style.fontFamily,advance:typeof e.getComputedTextLength==='function'?e.getComputedTextLength()*scale:rect(e).width,...rect(e)};}),
      callouts:[...document.querySelectorAll('[data-callout-id]')].map(e=>({id:e.dataset.calloutId,fixture:e.dataset.fixtureId,...rect(e)})),
      anchors:[...document.querySelectorAll('[data-anchor-id]')].map(e=>({id:e.dataset.anchorId,longitude:+e.dataset.longitude,...rect(e)})),
      satelliteCompositions:[...document.querySelectorAll('[data-satellite-composition]')].map(e=>({id:e.dataset.satelliteComposition,gap:parseFloat(getComputedStyle(e).gap),parent:rect(e.querySelector('.astro')),roman:rect(e.querySelector('.roman')),parentFont:parseFloat(getComputedStyle(e.querySelector('.astro')).fontSize),romanFont:parseFloat(getComputedStyle(e.querySelector('.roman')).fontSize)})),
      aspectExamples:aspectExamples(current()).map(a=>({a:a.a.id,b:a.b.id,aspect:a.definition.id,angle:a.definition.angle,separation:a.separation,orb:a.orb}))};
  }
  window.MOIRA_PILOT={ready:false,getState,setState,measure};
  const scrollHints=[];
  function updateScrollHints(){scrollHints.forEach(({wrapper,hint})=>{hint.hidden=wrapper.scrollWidth<=wrapper.clientWidth+1;});}
  document.querySelectorAll('.data-table').forEach(table=>{
    let wrapper=table.closest('.scroll-region');
    if(!wrapper){
      wrapper=document.createElement('div');wrapper.className='scroll-region table-scroll';wrapper.tabIndex=0;
      wrapper.setAttribute('role','region');wrapper.setAttribute('aria-label','Scrollable '+({lots:'lot entries','minor-bodies':'minor-body entries','fixed-stars':'historical fixed-star entries',satellites:'satellite compositions'}[table.tBodies[0].id]||'table'));
      table.before(wrapper);wrapper.append(table);
    }
    const hint=document.createElement('p');hint.className='scroll-hint companion-scroll-hint';hint.id='scroll-hint-'+table.tBodies[0].id;hint.hidden=true;
    hint.textContent='Scroll this table horizontally to see every column.';
    wrapper.before(hint);wrapper.setAttribute('aria-describedby',hint.id);scrollHints.push({wrapper,hint});
  });
  const resizeObserver=new ResizeObserver(updateScrollHints);scrollHints.forEach(({wrapper})=>resizeObserver.observe(wrapper));
  $('fixture-select').addEventListener('change',event=>setState({fixture:event.target.value}));
  $('format-select').addEventListener('change',event=>setState({format:event.target.value}));
  $('theme-button').addEventListener('click',()=>setState({theme:state.theme==='light'?'dark':'light'}));
  $('print-button').addEventListener('click',()=>window.print());
  render();
  Promise.race([Promise.all(['MoiraWOFF','MoiraTTF'].map(f=>document.fonts.load(`24px ${f}`,'☉[lot:Fo]'))),new Promise((_,reject)=>setTimeout(()=>reject(new Error('Font loading timed out')),10000))]).then(async results=>{
    if(results.some(r=>r.length!==1))throw new Error('A font face was unavailable');
    await document.fonts.ready;await frame();updateScrollHints();document.body.classList.remove('font-loading');window.MOIRA_PILOT.ready=true;
    $('font-status').textContent='Both font formats loaded · existing glyphs and access routes';
  }).catch(error=>{
    fontError=error.message;document.body.classList.remove('font-loading');document.body.classList.add('font-failed');
    $('font-status').classList.add('error');$('font-status').textContent='Moira Astro could not load. Symbol marks are hidden; names and declared positions remain readable. Check the local fonts folder and reload.';
  });
})();
