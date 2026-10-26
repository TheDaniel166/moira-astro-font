# Copyright 2026 Moira Astro contributors. Licensed under SIL OFL 1.1; see OFL.txt.
$ErrorActionPreference='Stop'
$fontRoot=Split-Path -Parent $PSScriptRoot
$reviewRoot=Join-Path $fontRoot 'build/character-guide'
$sessionName='moira-guide-proof'
New-Item -ItemType Directory -Path $reviewRoot -Force | Out-Null
function Query-Guide([string]$script) {
    $payload=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($script))
    $raw=& agent-browser --session $sessionName eval -b $payload --json
    if($LASTEXITCODE -ne 0){throw 'Guide browser query failed'}
    $answer=$raw | ConvertFrom-Json
    if(-not $answer.success){throw 'Guide evaluation failed'}
    return $answer.data.result
}
function Guide-Inputs {
    $paths=@(Get-ChildItem -LiteralPath (Join-Path $fontRoot 'guide') -Recurse -File | Sort-Object FullName | Select-Object -ExpandProperty FullName)
    $paths+=@(Join-Path $fontRoot 'tooling/guide-audit.js';Join-Path $fontRoot 'fonts/MoiraAstro-Regular.ttf';Join-Path $fontRoot 'fonts/MoiraAstro-Regular.woff2')
    return @($paths | ForEach-Object {[ordered]@{path=[IO.Path]::GetRelativePath($fontRoot,$_).Replace([char]92,[char]47);sha256=(Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLower()}})
}
$before=Guide-Inputs
$data=Get-Content -LiteralPath (Join-Path $fontRoot 'guide/assets/catalog.json') -Raw | ConvertFrom-Json
$historical=($data.entries | Where-Object {$_.name -eq 'Regulus' -and $_.form_label -eq 'Historical form'} | Select-Object -First 1).id
$scenes=@(
    [ordered]@{id='index';query='';category='all';selected='glyph.uni2648';size=32},
    [ordered]@{id='long-lot';query='Wrcp';category='lots';selected='glyph.lot.Wrcp';size=48},
    [ordered]@{id='historical';query='Regulus';category='fixed-stars';selected=$historical;size=18},
    [ordered]@{id='zero';query='Slashed zero';category='letters';selected='glyph.zero.slashed';size=32}
)
$captures=@();$bulk=@()
try {
    & agent-browser --session $sessionName open ([uri](Join-Path $fontRoot 'guide/index.html')).AbsoluteUri
    if($LASTEXITCODE -ne 0){throw 'Guide browser failed to open'}
    & agent-browser --session $sessionName wait --fn 'window.MOIRA_GUIDE && window.MOIRA_GUIDE.ready' | Out-Null
    if($LASTEXITCODE -ne 0){throw 'Guide fonts/data did not become ready'}
    Query-Guide ([IO.File]::ReadAllText((Join-Path $fontRoot 'tooling/guide-audit.js'))) | Out-Null
    foreach($width in @(1360,768,390)) {
        & agent-browser --session $sessionName set viewport $width 1000 | Out-Null
        foreach($scene in $scenes) {
            foreach($theme in @('light','dark')) {
                foreach($format in @('ttf','woff2')) {
                    $state=[ordered]@{query=$scene.query;category=$scene.category;selected=$scene.selected;size=$scene.size;theme=$theme;format=$format} | ConvertTo-Json -Compress
                    $proof=Query-Guide "(async()=>{await window.MOIRA_GUIDE.setState($state);window.scrollTo(0,0);return window.auditMoiraGuide()})()"
                    if(-not $proof.ready -or $proof.bodyOverflow){throw "Guide state failed: $width $($scene.id) $theme $format"}
                    $capture="build/character-guide/$width-$($scene.id)-$theme-$format.png"
                    & agent-browser --session $sessionName screenshot (Join-Path $fontRoot $capture) --full | Out-Null
                    if($LASTEXITCODE -ne 0){throw 'Guide screenshot failed'}
                    $captures += [ordered]@{width=$width;scene=$scene.id;theme=$theme;format=$format;selected=$scene.selected;size=$scene.size;capture=$capture;sha256=(Get-FileHash -LiteralPath (Join-Path $fontRoot $capture) -Algorithm SHA256).Hash.ToLower();proof=$proof}
                }
            }
        }
        Write-Output "Captured 16 guide states at $width px"
    }
    & agent-browser --session $sessionName set viewport 1360 1000 | Out-Null
    $ids=@($data.entries | Select-Object -ExpandProperty id)
    for($start=0;$start -lt $ids.Count;$start+=50) {
        $last=[Math]::Min($start+49,$ids.Count-1)
        $batch=@($ids[$start..$last]) | ConvertTo-Json -Compress
        $rows=Query-Guide "window.bulkMoiraGuide($batch)"
        $bulk+=@($rows)
        Write-Output "Measured and copied routes for $($last+1)/$($ids.Count) guide forms"
    }
    $after=Guide-Inputs
    if(($before | ConvertTo-Json -Compress) -ne ($after | ConvertTo-Json -Compress)){throw 'Guide sources changed during capture; repeat final capture'}
    [ordered]@{status='CAPTURED';inputs=$after;captures=$captures;bulk=$bulk;clipboard='Recorded writeText calls in isolated browser; no system clipboard modification'} | ConvertTo-Json -Depth 45 | Set-Content -LiteralPath (Join-Path $reviewRoot 'browser-captures.json') -Encoding utf8
    Write-Output 'Captured 48 guide states and all 725 detail/copy flows; independent validation remains required'
} finally { & agent-browser --session $sessionName close | Out-Null }
