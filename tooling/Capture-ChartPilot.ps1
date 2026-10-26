# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
$ErrorActionPreference='Stop'
$fontRoot=Split-Path -Parent $PSScriptRoot
$reviewRoot=Join-Path $fontRoot 'build/chart-pilot'
$sessionName='moira-chart-pilot-proof'
New-Item -ItemType Directory -Path $reviewRoot -Force | Out-Null
$auditScript=[System.IO.File]::ReadAllText((Join-Path $PSScriptRoot 'chart-audit.js'))
function Pilot-Inputs {
    $items=@(Get-ChildItem -LiteralPath (Join-Path $fontRoot 'demo/chart-pilot') -File -Recurse | Sort-Object FullName | ForEach-Object {
        [ordered]@{path=[System.IO.Path]::GetRelativePath($fontRoot,$_.FullName).Replace([char]92,[char]47);sha256=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower()}
    })
    foreach($name in @('fonts/MoiraAstro-Regular.ttf','fonts/MoiraAstro-Regular.woff2','tooling/chart-audit.js')) {
        $items += [ordered]@{path=$name;sha256=(Get-FileHash -LiteralPath (Join-Path $fontRoot $name) -Algorithm SHA256).Hash.ToLower()}
    }
    return $items
}
function Query-Pilot([string]$script) {
    $payload=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($script))
    $raw=& agent-browser --session $sessionName eval -b $payload --json
    if($LASTEXITCODE -ne 0){throw 'Browser query failed'}
    $answer=$raw | ConvertFrom-Json
    if(-not $answer.success){throw 'Browser evaluation failed'}
    return $answer.data.result
}
$captures=@()
$inputsBefore=Pilot-Inputs
try {
    & agent-browser --session $sessionName open ([uri](Join-Path $fontRoot 'demo/chart-pilot/index.html')).AbsoluteUri
    if($LASTEXITCODE -ne 0){throw 'Pilot browser launch failed'}
    & agent-browser --session $sessionName wait --fn 'window.MOIRA_PILOT && window.MOIRA_PILOT.ready === true' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Pilot fonts/render did not become ready'}
    Query-Pilot $auditScript | Out-Null
    foreach($width in @(1360,768,390)) {
        & agent-browser --session $sessionName set viewport $width 1000 | Out-Null
        foreach($fixture in @('balanced','crowded')) {
            foreach($theme in @('light','dark')) {
                foreach($format in @('ttf','woff2')) {
                    $state=[ordered]@{fixture=$fixture;theme=$theme;format=$format} | ConvertTo-Json -Compress
                    $proof=Query-Pilot "(async()=>{await window.MOIRA_PILOT.setState($state);window.scrollTo(0,0);return window.auditMoiraChart()})()"
                    if(-not $proof.ready -or $proof.bodyOverflow){throw "Pilot state failed: $width $fixture $theme $format"}
                    $capture="build/chart-pilot/$width-$fixture-$theme-$format.png"
                    & agent-browser --session $sessionName screenshot (Join-Path $fontRoot $capture) --full | Out-Null
                    if($LASTEXITCODE -ne 0){throw 'Pilot screenshot failed'}
                    $captures += [ordered]@{width=$width;fixture=$fixture;theme=$theme;format=$format;capture=$capture;captureSha256=(Get-FileHash -LiteralPath (Join-Path $fontRoot $capture) -Algorithm SHA256).Hash.ToLower();proof=$proof}
                }
            }
        }
        Write-Output "Captured 8 chart states at $width px"
    }
    foreach($fixture in @('balanced','crowded')) {
        $state=[ordered]@{fixture=$fixture;theme='light';format='woff2'} | ConvertTo-Json -Compress
        Query-Pilot "window.MOIRA_PILOT.setState($state)" | Out-Null
        $pdf=Join-Path $reviewRoot "MoiraAstro-$fixture-chart-pilot.pdf"
        & agent-browser --session $sessionName pdf $pdf | Out-Null
        if($LASTEXITCODE -ne 0){throw 'Chart PDF export failed'}
    }
    $inputs=Pilot-Inputs
    if(($inputsBefore | ConvertTo-Json -Depth 6 -Compress) -ne ($inputs | ConvertTo-Json -Depth 6 -Compress)){throw 'Pilot sources changed during capture; recapture the final sources'}
    [ordered]@{status='CAPTURED';captures=$captures;inputs=$inputs} | ConvertTo-Json -Depth 45 | Set-Content -LiteralPath (Join-Path $reviewRoot 'browser-captures.json') -Encoding utf8
    Write-Output 'Captured 24 browser states and two vector print PDFs; independent validation remains required'
} finally { & agent-browser --session $sessionName close | Out-Null }
