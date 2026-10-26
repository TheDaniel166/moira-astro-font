# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
$ErrorActionPreference='Stop'
$fontRoot=Split-Path -Parent $PSScriptRoot
$reviewRoot=Join-Path $fontRoot 'build/character-guide'
$sessionName='moira-guide-controls'
New-Item -ItemType Directory -Path $reviewRoot -Force | Out-Null
function Query-GuideControl([string]$script) {
    $payload=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($script))
    $raw=& agent-browser --session $sessionName eval -b $payload --json
    if($LASTEXITCODE -ne 0){throw 'Guide control query failed'}
    $answer=$raw | ConvertFrom-Json
    if(-not $answer.success){throw 'Guide control evaluation failed'}
    return $answer.data.result
}
function Require-Guide([string]$condition,[string]$message) {
    $ok=Query-GuideControl $condition
    if(-not $ok){throw $message}
}
$checks=@()
try {
    & agent-browser --session $sessionName open ([uri](Join-Path $fontRoot 'guide/index.html')).AbsoluteUri
    & agent-browser --session $sessionName wait --fn 'window.MOIRA_GUIDE && window.MOIRA_GUIDE.ready' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Guide did not become ready'}
    & agent-browser --session $sessionName set viewport 1360 1100 | Out-Null
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'desktop-preview.png') | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().resultIds.length===725 && window.MOIRA_GUIDE.getState().visibleIds.length===24' 'Initial index/pagination is incorrect'
    & agent-browser --session $sessionName click '#load-more' | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().visibleIds.length===48' 'Load-more did not expose another page'
    & agent-browser --session $sessionName click '[data-category="lots"]' | Out-Null
    & agent-browser --session $sessionName fill '#guide-search' Wrcp | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().resultIds.length===1 && window.MOIRA_GUIDE.getState().resultIds[0]==="glyph.lot.Wrcp"' 'Name/code search failed'
    & agent-browser --session $sessionName click '[data-select-entry="glyph.lot.Wrcp"]' | Out-Null
    & agent-browser --session $sessionName select '#size-select' 48 | Out-Null
    & agent-browser --session $sessionName select '#format-select' ttf | Out-Null
    & agent-browser --session $sessionName click '#theme-button' | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().selected==="glyph.lot.Wrcp" && window.MOIRA_GUIDE.getState().size===48 && window.MOIRA_GUIDE.getState().format==="ttf" && window.MOIRA_GUIDE.getState().theme==="dark" && document.documentElement.scrollWidth<=innerWidth' 'Native presentation controls failed'
    Query-GuideControl 'window.guideWrites=[];window.originalExecCommand=document.execCommand;Object.defineProperty(navigator,"clipboard",{configurable:true,value:{writeText:async text=>{window.guideWrites.push(text)}}});true' | Out-Null
    & agent-browser --session $sessionName click '[data-copy-route="token:[lot:Wrcp]"]' | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().lastCopy?.success && window.guideWrites.at(-1)==="[lot:Wrcp]"' 'Native token copy path failed'
    & agent-browser --session $sessionName click '[data-copy-route="token:[lot:Wrcp]"]' | Out-Null
    Query-GuideControl 'new Promise(resolve=>setTimeout(()=>resolve(true),2100))' | Out-Null
    Require-Guide 'document.querySelector("[data-copy-route=\"token:[lot:Wrcp]\"]").textContent!=="Copied"' 'Rapid successful copies left a stale success label'
    $checks+='pagination, category/name/code search, size/format/theme controls, exact recorded token copying'

    & agent-browser --session $sessionName click '[data-category="all"]' | Out-Null
    & agent-browser --session $sessionName fill '#guide-search' 'Slashed zero' | Out-Null
    & agent-browser --session $sessionName click '[data-select-entry="glyph.zero.slashed"]' | Out-Null
    & agent-browser --session $sessionName click '[data-copy-route="feature:30"]' | Out-Null
    Require-Guide 'window.guideWrites.at(-1)==="0" && document.querySelector("[data-role=detail]").dataset.zero==="1" && document.getElementById("css-example").textContent.includes("\"zero\" 1")' 'Feature-only zero route/snippet is incorrect'
    & agent-browser --session $sessionName fill '#guide-search' Spbar | Out-Null
    & agent-browser --session $sessionName click '[data-select-entry="glyph.uni29B6"]' | Out-Null
    & agent-browser --session $sessionName click '[data-copy-route="word_alias:[lot:Spbar]"]' | Out-Null
    Require-Guide 'window.guideWrites.at(-1)==="[lot:Spbar]" && window.MOIRA_GUIDE.getState().lastCopy?.success' 'Word alias copy path failed'
    Query-GuideControl 'Object.defineProperty(navigator,"clipboard",{configurable:true,value:{writeText:async()=>{throw new Error("denied")}}});document.execCommand=()=>false;true' | Out-Null
    & agent-browser --session $sessionName click '[data-copy-route="word_alias:[lot:Spbar]"]' | Out-Null
    Require-Guide '(()=>{const e=document.getElementById("manual-copy-value"),s=window.MOIRA_GUIDE.getState();return !s.lastCopy.success && s.manualValue==="[lot:Spbar]" && e.value==="[lot:Spbar]" && e.readOnly && e.selectionStart===0 && e.selectionEnd===e.value.length && /automatic copy is unavailable/i.test(s.copyStatus)})()' 'Denied copying did not expose the exact selected manual value'
    Query-GuideControl 'new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(()=>resolve(true))))' | Out-Null
    Require-Guide '(()=>{const e=document.getElementById("manual-copy-value"),r=e.getBoundingClientRect(),a=document.getElementById("detail-content").getBoundingClientRect();return r.top>=Math.max(0,a.top)-1&&r.bottom<=Math.min(innerHeight,a.bottom)+1&&document.querySelector("[data-copy-route=\"word_alias:[lot:Spbar]\"]").textContent!=="Copied"})()' 'Manual value is clipped or copy button falsely retains success feedback'
    # Preserve the real viewport and scrolled detail when recording the selected fallback.
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'manual-copy-preview.png') | Out-Null
    $checks+='slashed zero feature/snippet, Word alias, denied-clipboard manual-copy fallback'

    & agent-browser --session $sessionName fill '#guide-search' 'annotated NamesList' | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().resultIds.includes("glyph.uni2648")' 'Source-title search did not find Aries'
    & agent-browser --session $sessionName fill '#guide-search' 'North Node' | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().resultIds.includes("glyph.uni260A")' 'Qualified node alias search failed'
    & agent-browser --session $sessionName fill '#guide-search' 'no-such-Moira-form-987654' | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().resultIds.length===0 && !document.getElementById("empty-state").hidden && !document.getElementById("selection-notice").hidden' 'Empty/outside-selection states are unclear'
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'empty-preview.png') --full | Out-Null
    & agent-browser --session $sessionName click '#empty-reset' | Out-Null
    Require-Guide 'window.MOIRA_GUIDE.getState().query==="" && window.MOIRA_GUIDE.getState().category==="all" && window.MOIRA_GUIDE.getState().resultIds.length===725' 'Reset did not restore the complete index'
    & agent-browser --session $sessionName click '[data-select-entry="glyph.uni2648"]' | Out-Null
    & agent-browser --session $sessionName fill '#guide-search' Sun | Out-Null
    & agent-browser --session $sessionName click '[data-select-entry="glyph.uni2609"]' | Out-Null
    Query-GuideControl 'history.back();true' | Out-Null
    & agent-browser --session $sessionName wait --fn 'window.MOIRA_GUIDE.getState().selected === "glyph.uni2648"' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'History navigation did not restore the prior selection'}
    Query-GuideControl 'location.hash="unknown-form-for-review";true' | Out-Null
    & agent-browser --session $sessionName wait --fn 'document.getElementById("font-status").classList.contains("error")' | Out-Null
    & agent-browser --session $sessionName click '[data-select-entry="glyph.uni2609"]' | Out-Null
    Require-Guide '!document.getElementById("font-status").classList.contains("error") && window.MOIRA_GUIDE.getState().selected==="glyph.uni2609"' 'Invalid-link status did not recover after valid selection'
    $checks+='source-title/model aliases, empty/reset/stale-selection notices, real history and invalid-link recovery'

    & agent-browser --session $sessionName open ([uri](Join-Path $fontRoot 'guide/index.html')).AbsoluteUri
    & agent-browser --session $sessionName wait --fn 'window.MOIRA_GUIDE && window.MOIRA_GUIDE.ready' | Out-Null
    & agent-browser --session $sessionName set viewport 390 1000 | Out-Null
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'mobile-preview.png') | Out-Null
    & agent-browser --session $sessionName click '[data-select-entry="glyph.uni264C"]' | Out-Null
    Require-Guide 'document.getElementById("detail-dialog").open' 'Mobile details did not open as a dialog'
    $modalScroll=Query-GuideControl 'document.getElementById("detail-dialog").scrollTop=500;({windowY:scrollY,dialogY:document.getElementById("detail-dialog").scrollTop})'
    & agent-browser --session $sessionName press Escape | Out-Null
    Require-Guide '!document.getElementById("detail-dialog").open && document.activeElement.dataset.selectEntry==="glyph.uni264C"' 'Escape did not return focus to the originating Leo result'
    $returnY=Query-GuideControl 'scrollY'
    if([Math]::Abs($returnY-$modalScroll.windowY) -gt 1){throw 'Dialog close changed the reading position'}
    & agent-browser --session $sessionName click '[data-select-entry="glyph.uni2649"]' | Out-Null
    Require-Guide 'document.getElementById("detail-dialog").scrollTop===0 && document.getElementById("detail-content").scrollTop===0 && document.getElementById("detail-title").getBoundingClientRect().top>0' 'New form retained stale detail scrolling'
    & agent-browser --session $sessionName press Tab | Out-Null
    Require-Guide 'document.getElementById("detail-dialog").contains(document.activeElement)' 'Modal keyboard focus escaped the dialog'
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'mobile-detail-preview.png') | Out-Null
    $checks+='mobile dialog, Escape focus restoration, retained reading position, heading reset and keyboard focus containment'
    & agent-browser --session $sessionName close | Out-Null

    foreach($failure in @('font','data')) {
        $isolated=Join-Path ([IO.Path]::GetTempPath()) ('moira-guide-'+$failure+'-'+[IO.Path]::GetRandomFileName())
        New-Item -ItemType Directory -Path $isolated -Force | Out-Null
        Copy-Item -LiteralPath (Join-Path $fontRoot 'guide') -Destination (Join-Path $isolated 'guide') -Recurse
        if($failure -eq 'data') {
            # Delete only this explicitly verified temporary copy of the data script.
            $scriptCopy=[IO.Path]::GetFullPath((Join-Path $isolated 'guide/assets/catalog.js'))
            if(-not $scriptCopy.StartsWith([IO.Path]::GetFullPath($isolated)+[IO.Path]::DirectorySeparatorChar)){throw 'Temporary data path escaped its isolated tree'}
            Remove-Item -LiteralPath $scriptCopy
        }
        & agent-browser --session $sessionName open ([uri](Join-Path $isolated 'guide/index.html')).AbsoluteUri
        $condition=if($failure -eq 'font'){'document.body.classList.contains("font-failed")'}else{'document.body.classList.contains("data-failed")'}
        & agent-browser --session $sessionName wait --fn $condition | Out-Null
        if($LASTEXITCODE -ne 0){throw 'Readable unavailable state did not appear'}
        $proof=Query-GuideControl '({ready:window.MOIRA_GUIDE.ready,text:document.body.innerText,status:document.getElementById("font-status").innerText,hidden:[...document.querySelectorAll("[data-font-symbol]")].every(e=>getComputedStyle(e).visibility==="hidden")})'
        if($proof.ready -or -not $proof.status.Contains('could not load')){throw 'Unavailable state falsely claimed readiness'}
        if($failure -eq 'font' -and (-not $proof.hidden -or -not $proof.text.Contains('Aries'))){throw 'Font failure did not preserve named text and hide fallback marks'}
        & agent-browser --session $sessionName set viewport 390 1000 | Out-Null
        & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot "$failure-failure-preview.png") | Out-Null
        $checks+="readable $failure-unavailable state in isolated file tree"
        & agent-browser --session $sessionName close | Out-Null
    }
    $inputs=Get-ChildItem -LiteralPath (Join-Path $fontRoot 'guide') -Recurse -File | Sort-Object FullName | ForEach-Object {[ordered]@{path=[IO.Path]::GetRelativePath($fontRoot,$_.FullName).Replace([char]92,[char]47);sha256=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower()}}
    [ordered]@{status='PASS';groups=$checks;inputs=$inputs;clipboard='Recorded browser API calls and denied APIs; system clipboard was not changed'} | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $reviewRoot 'interaction-checks.json') -Encoding utf8
    Write-Output 'PASS: native guide controls, copying/manual fallback, search/history, mobile focus/scrolling and real unavailable states'
} finally { & agent-browser --session $sessionName close | Out-Null }
