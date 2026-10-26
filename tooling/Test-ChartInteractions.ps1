# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
$ErrorActionPreference='Stop'
$fontRoot=Split-Path -Parent $PSScriptRoot
$reviewRoot=Join-Path $fontRoot 'build/chart-pilot'
$sessionName='moira-chart-pilot-controls'
New-Item -ItemType Directory -Path $reviewRoot -Force | Out-Null
function Query-Control([string]$script) {
    $payload=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($script))
    $raw=& agent-browser --session $sessionName eval -b $payload --json
    if($LASTEXITCODE -ne 0){throw 'Interaction query failed'}
    $result=$raw | ConvertFrom-Json
    if(-not $result.success){throw 'Interaction evaluation failed'}
    return $result.data.result
}
try {
    & agent-browser --session $sessionName open ([uri](Join-Path $fontRoot 'demo/chart-pilot/index.html')).AbsoluteUri
    if($LASTEXITCODE -ne 0){throw 'Interaction browser failed to open'}
    & agent-browser --session $sessionName wait --fn 'window.MOIRA_PILOT && window.MOIRA_PILOT.ready' | Out-Null
    & agent-browser --session $sessionName set viewport 1360 1250 | Out-Null
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'desktop-preview.png') | Out-Null
    & agent-browser --session $sessionName select '#fixture-select' crowded | Out-Null
    & agent-browser --session $sessionName click '#theme-button' | Out-Null
    & agent-browser --session $sessionName select '#format-select' ttf | Out-Null
    & agent-browser --session $sessionName wait --fn 'window.MOIRA_PILOT.getState().fixture === "crowded" && window.MOIRA_PILOT.getState().theme === "dark" && window.MOIRA_PILOT.getState().format === "ttf"' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Native controls did not update the chart'}
    $state=Query-Control 'window.MOIRA_PILOT.getState()'
    Query-Control 'window.chartPrintCalled=false;window.print=()=>{window.chartPrintCalled=true};true' | Out-Null
    & agent-browser --session $sessionName click '#print-button' | Out-Null
    $printCalled=Query-Control 'window.chartPrintCalled'
    if(-not $printCalled){throw 'Print button did not call browser printing'}
    & agent-browser --session $sessionName focus '#fixture-select' | Out-Null
    & agent-browser --session $sessionName press Tab | Out-Null
    $focus=Query-Control '({id:document.activeElement.id,outline:getComputedStyle(document.activeElement).outlineStyle,width:getComputedStyle(document.activeElement).outlineWidth})'
    if($focus.id -ne 'format-select' -or $focus.outline -eq 'none' -or $focus.width -eq '0px'){throw 'Keyboard focus is not visibly indicated'}
    & agent-browser --session $sessionName set viewport 390 1000 | Out-Null
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'mobile-preview.png') | Out-Null
    & agent-browser --session $sessionName focus '.chart-scroll' | Out-Null
    & agent-browser --session $sessionName press ArrowRight | Out-Null
    & agent-browser --session $sessionName wait --fn 'document.querySelector(".chart-scroll").scrollLeft > 0' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Chart region did not scroll through keyboard input'}
    $scroll=Query-Control '({left:document.querySelector(".chart-scroll").scrollLeft,overflow:document.documentElement.scrollWidth>innerWidth,regions:[...document.querySelectorAll(".scroll-region")].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>({label:e.getAttribute("aria-label"),focusable:e.tabIndex===0}))})'
    if($scroll.overflow -or @($scroll.regions | Where-Object {-not $_.focusable}).Count -gt 0){throw 'Scroll regions are not contained and keyboard reachable'}
    & agent-browser --session $sessionName select '#format-select' woff2 | Out-Null
    & agent-browser --session $sessionName focus '[aria-label="Scrollable aspect examples"]' | Out-Null
    & agent-browser --session $sessionName press ArrowRight | Out-Null
    & agent-browser --session $sessionName wait --fn 'document.querySelector("[aria-label=\"Scrollable aspect examples\"]").scrollLeft > 0' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Aspect columns did not scroll through keyboard input'}
    & agent-browser --session $sessionName set viewport 1360 1000 | Out-Null
    & agent-browser --session $sessionName pdf (Join-Path $reviewRoot 'MoiraAstro-focused-crowded-chart-pilot.pdf') | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Focused-table print export failed'}
    & agent-browser --session $sessionName close | Out-Null
    # Copy only the demo into an isolated tree without font files. This exercises
    # a real loading failure without modifying the repository or faking FontFace.
    $missingFontRoot=Join-Path ([System.IO.Path]::GetTempPath()) ('moira-chart-missing-font-' + [System.IO.Path]::GetRandomFileName())
    New-Item -ItemType Directory -Path (Join-Path $missingFontRoot 'demo') -Force | Out-Null
    Copy-Item -LiteralPath (Join-Path $fontRoot 'demo/chart-pilot') -Destination (Join-Path $missingFontRoot 'demo/chart-pilot') -Recurse
    & agent-browser --session $sessionName open ([uri](Join-Path $missingFontRoot 'demo/chart-pilot/index.html')).AbsoluteUri
    & agent-browser --session $sessionName wait --fn 'document.body.classList.contains("font-failed")' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Missing-font state did not appear'}
    $failure=Query-Control '({ready:window.MOIRA_PILOT.ready,message:document.getElementById("font-status").innerText,symbolsHidden:[...document.querySelectorAll("[data-font-symbol]")].every(e=>getComputedStyle(e).visibility==="hidden"),text:document.body.innerText})'
    if($failure.ready -or -not $failure.symbolsHidden -or -not $failure.message.Contains('could not load') -or -not $failure.text.ToLower().Contains('declared positions')){throw 'Font failure did not preserve a readable semantic fallback'}
    & agent-browser --session $sessionName set viewport 390 1000 | Out-Null
    & agent-browser --session $sessionName screenshot (Join-Path $reviewRoot 'missing-font-preview.png') | Out-Null
    $inputs=Get-ChildItem -LiteralPath (Join-Path $fontRoot 'demo/chart-pilot') -File -Recurse | Sort-Object FullName | ForEach-Object {
        [ordered]@{path=[System.IO.Path]::GetRelativePath($fontRoot,$_.FullName).Replace([char]92,[char]47);sha256=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower()}
    }
    [ordered]@{status='PASS';nativeControls=$state;printButtonCallsBrowser=$printCalled;keyboardFocus=$focus;scrolling=$scroll;fontFailure=$failure;missingFontTree=$missingFontRoot;focusedPrint='build/chart-pilot/MoiraAstro-focused-crowded-chart-pilot.pdf';inputs=$inputs} | ConvertTo-Json -Depth 16 | Set-Content -LiteralPath (Join-Path $reviewRoot 'interaction-checks.json') -Encoding utf8
    Write-Output 'PASS: native controls, print action, keyboard focus/scrolling and a real missing-font fallback'
} finally { & agent-browser --session $sessionName close | Out-Null }
