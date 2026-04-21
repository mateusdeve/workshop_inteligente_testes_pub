param([switch]$Abrir)

# CONFIG — lido do .env na raiz do projeto
$SCRIPT_DIR   = Split-Path -Parent $MyInvocation.MyCommand.Path
$PROJECT_ROOT = Split-Path (Split-Path $SCRIPT_DIR -Parent) -Parent
$envFile      = Join-Path $PROJECT_ROOT ".env"
$envVars      = @{}
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match '^\s*([^#\s][^=]*?)\s*=\s*(.+)$') {
            $envVars[$matches[1].Trim()] = $matches[2].Trim().Trim('"').Trim("'")
        }
    }
}
$APIFY_TOKEN = $envVars["APIFY_API_TOKEN"]
$IG_USER     = $envVars["IG_USER"]

if (-not $APIFY_TOKEN) { Write-Host "Erro: APIFY_API_TOKEN nao encontrado no .env"; exit 1 }
if (-not $IG_USER)     { Write-Host "Erro: IG_USER nao encontrado no .env"; exit 1 }

$IG_URL     = "https://www.instagram.com/$IG_USER/"
$DASHBOARD  = Join-Path $SCRIPT_DIR "dashboard.html"
$LOG        = Join-Path $SCRIPT_DIR "log.txt"

function Log {
    param([string]$msg)
    $ts   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$ts] $msg"
    Add-Content -Path $LOG -Value $line -Encoding UTF8
    Write-Host $line
}

function Img64 {
    param([string]$url)
    if (-not $url) { return "" }
    try {
        $wc = New-Object System.Net.WebClient
        $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        $wc.Headers.Add("Referer", "https://www.instagram.com/")
        $bytes = $wc.DownloadData($url)
        return "data:image/jpeg;base64," + [Convert]::ToBase64String($bytes)
    } catch {
        return ""
    }
}

function SaveB64 {
    param([string]$base64, [string]$filePath)
    if (-not $base64) { return $false }
    try {
        $clean = $base64 -replace '^data:[^;]+;base64,', ''
        $bytes = [Convert]::FromBase64String($clean)
        [System.IO.File]::WriteAllBytes($filePath, $bytes)
        return $true
    } catch { return $false }
}

function Transcribe {
    param([string]$videoUrl, [string]$token)
    if (-not $videoUrl) { return "" }
    try {
        $body = '{"urls":["' + $videoUrl + '"],"language":"pt"}'
        $resp = Invoke-RestMethod `
            -Uri ("https://api.apify.com/v2/acts/apify~whisper-speech-to-text/run-sync-get-dataset-items?token=" + $token + "&timeout=120") `
            -Method POST -ContentType "application/json" -Body $body -TimeoutSec 150
        if ($resp -and $resp.Count -gt 0 -and $resp[0].text) { return $resp[0].text.Trim() }
        return ""
    } catch {
        return ""
    }
}

Log "== Iniciando atualizacao @$IG_USER =="

# --- PERFIL ---
Log "Buscando perfil..."
$pBody = '{"directUrls":["' + $IG_URL + '"],"resultsType":"details","resultsLimit":1}'
try {
    $pResp = Invoke-RestMethod `
        -Uri ("https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items?token=" + $APIFY_TOKEN + "&timeout=60") `
        -Method POST -ContentType "application/json" -Body $pBody -TimeoutSec 90
} catch { Log "ERRO no perfil: $_"; exit 1 }

if (-not $pResp -or $pResp.Count -eq 0) { Log "ERRO: perfil vazio ou privado para @$IG_USER"; exit 1 }
$prof = $pResp[0]
Log "Perfil: $($prof.fullName) | Seguidores: $($prof.followersCount)"

# --- POSTS (busca expandida para substituir likes ocultos) ---
$allPosts = @()
$limit    = 30
$maxLimit = 100

do {
    Log "Buscando $limit posts..."
    $postsBody = '{"directUrls":["' + $IG_URL + '"],"resultsType":"posts","resultsLimit":' + $limit + '}'
    try {
        $pResp2 = Invoke-RestMethod `
            -Uri ("https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items?token=" + $APIFY_TOKEN + "&timeout=300") `
            -Method POST -ContentType "application/json" -Body $postsBody -TimeoutSec 360
        if ($pResp2) { $allPosts = @($pResp2) }
    } catch { Log "Aviso posts: $_"; break }

    $visib = @($allPosts | Where-Object { $null -ne $_.likesCount -and $_.likesCount -ne -1 }).Count
    Log "Total: $($allPosts.Count) | Com likes visiveis: $visib"
    if ($visib -ge 30 -or $limit -ge $maxLimit) { break }
    $limit = [Math]::Min($limit + 20, $maxLimit)
} while ($true)

# Selecionar 30 priorizando posts com likes visiveis
$vis = @($allPosts | Where-Object { $null -ne $_.likesCount -and $_.likesCount -ne -1 } | Select-Object -First 30)
$hid = @($allPosts | Where-Object { $null -eq $_.likesCount  -or  $_.likesCount -eq -1 })
$sel = @($vis)
if ($sel.Count -lt 30) { $sel += @($hid | Select-Object -First (30 - $sel.Count)) }
$sel = @($sel | Select-Object -First 30)
Log "Posts selecionados: $($sel.Count)"

# --- IMAGENS ---
Log "Baixando foto de perfil..."
$picUrl = if ($prof.profilePicUrlHD) { $prof.profilePicUrlHD } elseif ($prof.profilePicUrl) { $prof.profilePicUrl } else { "" }
$picB64 = Img64 $picUrl

$postObjs = New-Object System.Collections.Generic.List[PSCustomObject]
$i = 0
$followers = [Math]::Max(1, [int]$prof.followersCount)

foreach ($post in $sel) {
    $i++
    Write-Host "  Imagem $i/$($sel.Count) ($($post.type))..."

    $rawType = if ($post.type) { $post.type } else { "" }
    $type = if ("GraphVideo","Video" -contains $rawType) { "Reels" }
            elseif ("GraphSidecar","Sidecar" -contains $rawType) { "Carrossel" }
            else { "Foto" }

    # Transcricao (so para Reels)
    $transcricao = ""
    if ($type -eq "Reels") {
        $videoUrl = if ($post.videoUrl) { $post.videoUrl } else { "" }
        if ($videoUrl) {
            Write-Host "  Transcricao $i/$($sel.Count)..."
            $transcricao = Transcribe $videoUrl $APIFY_TOKEN
            if ($transcricao) { Log "  Transcricao obtida: $($transcricao.Length) chars" }
            else { Log "  Sem transcricao para o post $($post.id)" }
        }
    }

    $likes    = if ($null -ne $post.likesCount) { [int]$post.likesCount } else { -1 }
    $comments = if ($post.commentsCount)  { [int]$post.commentsCount }  else { 0 }
    $views    = if ($post.videoViewCount) { [int]$post.videoViewCount } else { 0 }

    $likesCalc = if ($likes -eq -1) { 0 } else { $likes }
    $engRate   = [Math]::Round(($likesCalc + $comments) / $followers * 100, 3)

    $cap = ""
    $capFull = ""
    if ($post.caption) {
        $capClean = ($post.caption -replace "`r`n"," " -replace "`n"," ").Trim()
        $capFull  = if ($capClean.Length -gt 500) { $capClean.Substring(0, 500) + "..." } else { $capClean }
        $cap      = if ($capClean.Length -gt 200) { $capClean.Substring(0, 200) + "..." } else { $capClean }
    }

    $thumb = Img64 $post.displayUrl

    $carousel = New-Object System.Collections.Generic.List[string]
    if ($post.images -and $post.images.Count -gt 1) {
        foreach ($imgUrl in $post.images) {
            $b = Img64 $imgUrl
            if ($b) { [void]$carousel.Add($b) }
            if ($carousel.Count -ge 10) { break }
        }
    }
    if ($carousel.Count -eq 0 -and $thumb) { [void]$carousel.Add($thumb) }

    $obj = [PSCustomObject]@{
        id              = "$($post.id)"
        url             = "$($post.url)"
        type            = $type
        timestamp       = if ($post.timestamp) { "$($post.timestamp)" } else { "" }
        likesCount      = $likes
        likesDisplay    = if ($likes -eq -1) { "--" } else { "$likes" }
        commentsCount   = $comments
        viewsCount      = $views
        engagementRate  = $engRate
        caption         = $cap
        captionFull     = $capFull
        thumbnailBase64 = $thumb
        carouselBase64  = $carousel.ToArray()
        transcricao     = $transcricao
    }
    $postObjs.Add($obj)
}

# --- METRICAS ---
$fmtCounts = @{ Reels = 0; Carrossel = 0; Foto = 0 }
$fmtLikes  = @{ Reels = 0; Carrossel = 0; Foto = 0 }
$fmtComm   = @{ Reels = 0; Carrossel = 0; Foto = 0 }
$fmtViews  = 0

foreach ($o in $postObjs) {
    $f = $o.type
    $l = if ($o.likesCount -eq -1) { 0 } else { $o.likesCount }
    if ($fmtCounts.ContainsKey($f)) {
        $fmtCounts[$f]++
        $fmtLikes[$f] += $l
        $fmtComm[$f]  += $o.commentsCount
        if ($f -eq "Reels") { $fmtViews += $o.viewsCount }
    }
}

function AvgRound { param($total, $count) if ($count -gt 0) { [Math]::Round($total / $count) } else { 0 } }

$engVals = @($postObjs | ForEach-Object { $_.engagementRate })
$avgEng  = if ($engVals.Count -gt 0) { [Math]::Round(($engVals | Measure-Object -Sum).Sum / $engVals.Count, 2) } else { 0 }
$mostFmt = ($fmtCounts.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 1).Key

# --- INSIGHTS JSON ---
Log "Gerando insights.json..."
$INSIGHTS = Join-Path $SCRIPT_DIR "insights.json"

$pos = 1
$imgDir = Join-Path $SCRIPT_DIR "imagens"
if (-not (Test-Path $imgDir)) { New-Item -ItemType Directory -Path $imgDir | Out-Null }

$insightsTop10 = @($postObjs | Sort-Object engagementRate -Descending | Select-Object -First 10 | ForEach-Object {
    $vw = if ($_.type -eq "Reels") { [int]$_.viewsCount } else { $null }
    $lk = if ($_.likesCount -eq -1) { $null } else { [int]$_.likesCount }
    $dt = if ($_.timestamp.Length -ge 10) { $_.timestamp.Substring(0,10) } else { $_.timestamp }

    # Salvar thumbnail como arquivo .jpg
    $thumbPath = ""
    if ($_.thumbnailBase64) {
        $thumbFile = Join-Path $imgDir "thumb-$pos.jpg"
        if (SaveB64 $_.thumbnailBase64 $thumbFile) { $thumbPath = "entregas/instagram-dashboard/imagens/thumb-$pos.jpg" }
    }

    # Slides do carrossel (max 3: primeiro, meio, ultimo) — salvar como .jpg
    $allSlides = $_.carouselBase64
    $slidesForInsights = @()
    if ($allSlides -and $allSlides.Count -gt 0) {
        $slidesForInsights += $allSlides[0]
        if ($allSlides.Count -ge 3) { $slidesForInsights += $allSlides[[Math]::Floor($allSlides.Count / 2)] }
        if ($allSlides.Count -ge 2) { $slidesForInsights += $allSlides[$allSlides.Count - 1] }
        $slidesForInsights = @($slidesForInsights | Select-Object -Unique)
    }
    $slidesPaths = @()
    $sIdx = 1
    foreach ($slide in $slidesForInsights) {
        $slideFile = Join-Path $imgDir "slide-$pos-$sIdx.jpg"
        if (SaveB64 $slide $slideFile) { $slidesPaths += "entregas/instagram-dashboard/imagens/slide-$pos-$sIdx.jpg" }
        $sIdx++
    }

    $obj = [PSCustomObject]@{
        posicao       = $pos
        tipo          = $_.type
        engajamento   = $_.engagementRate
        likes         = $lk
        comentarios   = [int]$_.commentsCount
        visualizacoes = $vw
        data          = $dt
        caption       = $_.captionFull
        url           = $_.url
        thumbnailPath = $thumbPath
        carouselPaths = $slidesPaths
        transcricao   = $_.transcricao
    }
    $pos++
    $obj
})

$insightsObj = [PSCustomObject]@{
    gerado_em    = (Get-Date -Format "dd/MM/yyyy HH:mm")
    perfil       = "@$($prof.username)"
    seguidores   = [int]$prof.followersCount
    avg_eng_pct  = $avgEng
    formato_top  = $mostFmt
    formato_stats = [PSCustomObject]@{
        Reels     = [PSCustomObject]@{ count = $fmtCounts["Reels"];     avg_likes = (AvgRound $fmtLikes["Reels"]     $fmtCounts["Reels"]);     avg_comentarios = (AvgRound $fmtComm["Reels"]     $fmtCounts["Reels"]);     total_views = $fmtViews }
        Carrossel = [PSCustomObject]@{ count = $fmtCounts["Carrossel"]; avg_likes = (AvgRound $fmtLikes["Carrossel"] $fmtCounts["Carrossel"]); avg_comentarios = (AvgRound $fmtComm["Carrossel"] $fmtCounts["Carrossel"]); total_views = 0 }
        Foto      = [PSCustomObject]@{ count = $fmtCounts["Foto"];      avg_likes = (AvgRound $fmtLikes["Foto"]      $fmtCounts["Foto"]);      avg_comentarios = (AvgRound $fmtComm["Foto"]      $fmtCounts["Foto"]);      total_views = 0 }
    }
    top10 = $insightsTop10
}

$insightsJson = $insightsObj | ConvertTo-Json -Depth 10
$utf8i = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($INSIGHTS, $insightsJson, $utf8i)
Log "insights.json salvo: $([Math]::Round((Get-Item $INSIGHTS).Length / 1KB, 1)) KB"

# --- MONTAR JSON ---
Log "Montando JSON..."

$dashObj = [PSCustomObject]@{
    profile = [PSCustomObject]@{
        username         = "$($prof.username)"
        fullName         = if ($prof.fullName)    { "$($prof.fullName)"    } else { $IG_USER }
        bio              = if ($prof.biography)   { "$($prof.biography)"   } else { "" }
        followersCount   = [int]$prof.followersCount
        followingCount   = if ($prof.followingCount) { [int]$prof.followingCount } else { 0 }
        postsCount       = if ($prof.postsCount)  { [int]$prof.postsCount  } else { $postObjs.Count }
        isVerified       = [bool]$prof.verified
        profilePicBase64 = $picB64
        lastUpdated      = (Get-Date -Format "dd/MM/yyyy HH:mm")
        avgEngagement    = $avgEng
        mostPostedFormat = $mostFmt
    }
    formatStats = [PSCustomObject]@{
        Reels = [PSCustomObject]@{
            count       = $fmtCounts["Reels"]
            avgLikes    = AvgRound $fmtLikes["Reels"] $fmtCounts["Reels"]
            avgComments = AvgRound $fmtComm["Reels"]  $fmtCounts["Reels"]
            totalViews  = $fmtViews
        }
        Carrossel = [PSCustomObject]@{
            count       = $fmtCounts["Carrossel"]
            avgLikes    = AvgRound $fmtLikes["Carrossel"] $fmtCounts["Carrossel"]
            avgComments = AvgRound $fmtComm["Carrossel"]  $fmtCounts["Carrossel"]
            totalViews  = 0
        }
        Foto = [PSCustomObject]@{
            count       = $fmtCounts["Foto"]
            avgLikes    = AvgRound $fmtLikes["Foto"] $fmtCounts["Foto"]
            avgComments = AvgRound $fmtComm["Foto"]  $fmtCounts["Foto"]
            totalViews  = 0
        }
    }
    posts = $postObjs.ToArray()
}

$json = $dashObj | ConvertTo-Json -Depth 20 -Compress
Log "JSON: $([Math]::Round($json.Length / 1KB, 1)) KB"

# --- GERAR HTML ---
Log "Gerando HTML..."

$html = @'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Instagram Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',sans-serif;background:#f5f7fa;color:#1a1a2e;min-height:100vh}
.wrap{max-width:1200px;margin:0 auto;padding:24px 16px}
/* Header */
.hdr{background:#fff;border-radius:16px;padding:24px;display:flex;align-items:flex-start;gap:20px;margin-bottom:24px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.av-wrap{flex-shrink:0}
.av-wrap img{width:80px;height:80px;border-radius:50%;object-fit:cover}
.av-init{width:80px;height:80px;border-radius:50%;background:#e0e7ff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700;color:#4f46e5}
.hdr-info h1{font-size:1.2rem;font-weight:700;margin-bottom:4px}
.vbadge{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;background:#0095f6;border-radius:50%;color:#fff;font-size:9px;margin-left:5px;vertical-align:middle}
.bio{font-size:.85rem;color:#555;line-height:1.55;max-width:600px;margin-top:4px}
.upd{font-size:.72rem;color:#bbb;margin-top:8px}
/* KPIs */
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
.kpi{background:#fff;border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.kpi-lbl{font-size:.7rem;color:#888;text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px}
.kpi-val{font-size:1.6rem;font-weight:700;color:#1a1a2e;line-height:1.2}
.kpi-sub{font-size:.7rem;color:#ccc;margin-top:3px}
/* Secao */
.sec{font-size:.95rem;font-weight:600;color:#1a1a2e;margin-bottom:16px}
/* Formatos */
.fmt-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}
.fmt-card{background:#fff;border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.fmt-head{display:flex;align-items:center;gap:8px;font-size:.875rem;font-weight:600;margin-bottom:12px}
.dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.dr{background:#9333ea}.dc{background:#2563eb}.df{background:#16a34a}
.fmt-line{display:flex;justify-content:space-between;font-size:.8rem;color:#555;padding:5px 0;border-bottom:1px solid #f0f0f0}
.fmt-line:last-child{border-bottom:none}
.fmt-line b{color:#1a1a2e;font-weight:600}
.fmt-empty{font-size:.8rem;color:#ccc;text-align:center;padding:16px 0}
/* Top3 */
.top3-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}
.t3{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.t3-img{width:100%;height:180px;object-fit:cover;display:block;background:#f0f0f0}
.t3-noimg{width:100%;height:180px;display:flex;align-items:center;justify-content:center;background:#f5f5f5;color:#ccc;font-size:.8rem}
.t3-body{padding:14px}
.bdg{display:inline-block;padding:2px 8px;border-radius:20px;font-size:.68rem;font-weight:600;margin-bottom:8px}
.br{background:#f3e8ff;color:#7c3aed}.bc{background:#dbeafe;color:#1d4ed8}.bf{background:#dcfce7;color:#15803d}
.t3-stats{display:flex;flex-wrap:wrap;gap:10px;font-size:.78rem;color:#555}
.t3-eng{font-size:.78rem;font-weight:700;color:#f97316;margin-top:6px}
.t3-cap{font-size:.72rem;color:#aaa;margin-top:6px;line-height:1.4;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.t3-link{font-size:.72rem;color:#0095f6;text-decoration:none;display:inline-block;margin-top:8px}
.t3-link:hover{text-decoration:underline}
/* Charts */
.chart-card{background:#fff;border-radius:16px;padding:24px;margin-bottom:24px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.ch-blk{margin-bottom:28px}
.ch-blk:last-child{margin-bottom:0}
.ch-ttl{font-size:.85rem;font-weight:600;margin-bottom:8px}
.ch-leg{display:flex;gap:14px;margin-bottom:10px;flex-wrap:wrap}
.leg{display:flex;align-items:center;gap:5px;font-size:.72rem;color:#666}
.ldot{width:8px;height:8px;border-radius:50%}
canvas{width:100%;display:block;cursor:crosshair}
/* Posts grade */
.pgrd{display:grid;grid-template-columns:repeat(auto-fill,minmax(185px,1fr));gap:14px;margin-bottom:32px}
.pc{background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.06);cursor:pointer;transition:transform .15s}
.pc:hover{transform:translateY(-2px)}
.pt{position:relative;width:100%;padding-top:100%;overflow:hidden;background:#f0f0f0}
.pt img{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover}
.pi{position:absolute;bottom:6px;right:6px;background:rgba(0,0,0,.55);color:#fff;font-size:.62rem;padding:2px 6px;border-radius:10px;pointer-events:none}
.pb{padding:10px}
.pmeta{display:flex;flex-wrap:wrap;gap:6px;font-size:.75rem;color:#555;margin-top:4px}
.pdate{font-size:.68rem;color:#ccc;margin-top:3px}
.pcap{font-size:.7rem;color:#aaa;margin-top:4px;line-height:1.35;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.plink{font-size:.68rem;color:#0095f6;text-decoration:none;display:inline-block;margin-top:5px}
.plink:hover{text-decoration:underline}
@media(max-width:900px){.kpi-row{grid-template-columns:repeat(2,1fr)}.fmt-row{grid-template-columns:1fr 1fr}.top3-row{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.kpi-row{grid-template-columns:1fr 1fr}.fmt-row{grid-template-columns:1fr}.top3-row{grid-template-columns:1fr}.pgrd{grid-template-columns:repeat(2,1fr)}.hdr{flex-direction:column;align-items:center;text-align:center}}
</style>
</head>
<body>
<div class="wrap" id="root"></div>
<script>const DATA=__JSON__;</script>
<script>
(function(){
var D=DATA,p=D.profile,posts=D.posts||[],fs=D.formatStats||{};
var flw=Math.max(1,p.followersCount||1);

function N(v){return v==null?0:+v;}
function FN(v){v=+v;if(v>=1e6)return(v/1e6).toFixed(1)+"M";if(v>=1e3)return(v/1e3).toFixed(1)+"K";return ""+v;}
function BC(t){return t==="Reels"?"br":t==="Carrossel"?"bc":"bf";}
function DC(t){return t==="Reels"?"dr":t==="Carrossel"?"dc":"df";}

/* --- Secao 1: Cabecalho --- */
var avH=p.profilePicBase64
  ?'<div class="av-wrap"><img src="'+p.profilePicBase64+'" alt="@'+p.username+'"></div>'
  :'<div class="av-wrap"><div class="av-init">'+(p.fullName||p.username||"?")[0].toUpperCase()+"</div></div>";
var vf=p.isVerified?'<span class="vbadge">&#10003;</span>':"";

/* --- Secao 2: KPIs --- */
var kpis=[
  {lbl:"Seguidores",      val:FN(N(p.followersCount)), sub:""},
  {lbl:"Engajamento medio",val:N(p.avgEngagement).toFixed(2)+"%", sub:"por post"},
  {lbl:"Total de posts",  val:FN(N(p.postsCount)),     sub:""},
  {lbl:"Formato top",     val:p.mostPostedFormat||"Foto", sub:"mais postado"}
];

/* --- Secao 3: Formatos --- */
function fmtCard(nm,dc){
  var f=fs[nm];
  if(!f||f.count===0)return'<div class="fmt-card"><div class="fmt-head"><span class="dot '+dc+'"></span>'+nm+'</div><div class="fmt-empty">Sem posts</div></div>';
  var rows=[["Posts",f.count],["Media curtidas",FN(f.avgLikes)],["Media comentarios",FN(f.avgComments)]];
  if(nm==="Reels")rows.push(["Total visualizacoes",FN(f.totalViews)]);
  return'<div class="fmt-card"><div class="fmt-head"><span class="dot '+dc+'"></span>'+nm+'</div>'+rows.map(function(r){return'<div class="fmt-line"><span>'+r[0]+"</span><b>"+r[1]+"</b></div>";}).join("")+"</div>";
}

/* --- Secao 4: Top 3 --- */
var sorted=[].concat(posts).sort(function(a,b){return N(b.engagementRate)-N(a.engagementRate);});
var top3=sorted.slice(0,3);
var t3H=top3.map(function(pt){
  var imgH=pt.thumbnailBase64?'<img class="t3-img" src="'+pt.thumbnailBase64+'" alt="">':'<div class="t3-noimg">Sem imagem</div>';
  var vw=pt.type==="Reels"?'<span>&#128065; '+FN(N(pt.viewsCount))+"</span>":"";
  return'<div class="t3">'+imgH+'<div class="t3-body"><span class="bdg '+BC(pt.type)+'">'+pt.type+'</span><div class="t3-stats"><span>&#10084; '+pt.likesDisplay+"</span>"+'<span>&#128172; '+FN(N(pt.commentsCount))+"</span>"+vw+"</div>"+'<div class="t3-eng">Engajamento: '+N(pt.engagementRate).toFixed(2)+"%</div>"+(pt.caption?'<div class="t3-cap">'+pt.caption+"</div>":"")+'<a class="t3-link" href="'+pt.url+'" target="_blank">Ver post original</a></div></div>';
}).join("");

/* --- Secao 6: Posts grade (carousel) --- */
var csS={};
window.csClick=function(idx){
  var pt=posts[idx];if(!pt||!pt.carouselBase64||pt.carouselBase64.length<=1)return;
  csS[idx]=((csS[idx]||0)+1)%pt.carouselBase64.length;
  var img=document.getElementById("ti-"+idx);var ind=document.getElementById("pi-"+idx);
  if(img)img.src=pt.carouselBase64[csS[idx]];
  if(ind)ind.textContent=(csS[idx]+1)+"/"+pt.carouselBase64.length;
};
function pCard(pt,idx){
  var hasC=pt.carouselBase64&&pt.carouselBase64.length>1;
  var ind=hasC?'<span class="pi" id="pi-'+idx+'">1/'+pt.carouselBase64.length+"</span>":"";
  var vw=pt.type==="Reels"?'<span>&#128065; '+FN(N(pt.viewsCount))+"</span>":"";
  var dt=pt.timestamp?pt.timestamp.substring(0,10):"";
  return'<div class="pc" onclick="csClick('+idx+')">'+'<div class="pt"><img src="'+(pt.thumbnailBase64||"")+'" alt="" id="ti-'+idx+'">'+ind+"</div>"+'<div class="pb"><span class="bdg '+BC(pt.type)+'">'+pt.type+'</span>'+'<div class="pmeta"><span>&#10084; '+pt.likesDisplay+'</span><span>&#128172; '+FN(N(pt.commentsCount))+"</span>"+vw+"</div>"+'<div class="pdate">'+dt+"</div>"+(pt.caption?'<div class="pcap">'+pt.caption+"</div>":"")+'<a class="plink" href="'+pt.url+'" target="_blank" onclick="event.stopPropagation()">Ver post</a></div></div>';
}

/* --- Render --- */
document.getElementById("root").innerHTML=
  '<div class="hdr">'+avH+'<div class="hdr-info"><h1>@'+(p.username||"")+vf+"</h1>"+(p.bio?'<div class="bio">'+p.bio+"</div>":"")+'<div class="upd">Atualizado em '+p.lastUpdated+"</div></div></div>"+
  '<div class="kpi-row">'+kpis.map(function(k){return'<div class="kpi"><div class="kpi-lbl">'+k.lbl+'</div><div class="kpi-val">'+k.val+"</div>"+(k.sub?'<div class="kpi-sub">'+k.sub+"</div>":"")+"</div>";}).join("")+"</div>"+
  '<div class="sec">Desempenho Medio por Formato</div><div class="fmt-row">'+fmtCard("Reels","dr")+fmtCard("Carrossel","dc")+fmtCard("Foto","df")+"</div>"+
  '<div class="sec">Top 3 Posts</div><div class="top3-row">'+t3H+"</div>"+
  '<div class="sec">Linha do Tempo</div>'+
  '<div class="chart-card">'+
    '<div class="ch-blk"><div class="ch-ttl">Curtidas</div><div class="ch-leg"><div class="leg"><div class="ldot" style="background:#9333ea"></div>Reels</div><div class="leg"><div class="ldot" style="background:#2563eb"></div>Carrossel</div><div class="leg"><div class="ldot" style="background:#16a34a"></div>Foto</div></div><canvas id="ch-lk" height="150"></canvas></div>'+
    '<div class="ch-blk"><div class="ch-ttl">Visualizacoes (Reels)</div><div class="ch-leg"><div class="leg"><div class="ldot" style="background:#9333ea"></div>Reels</div></div><canvas id="ch-vw" height="150"></canvas></div>'+
    '<div class="ch-blk"><div class="ch-ttl">Engajamento (%)</div><div class="ch-leg"><div class="leg"><div class="ldot" style="background:#9333ea"></div>Reels</div><div class="leg"><div class="ldot" style="background:#2563eb"></div>Carrossel</div><div class="leg"><div class="ldot" style="background:#16a34a"></div>Foto</div></div><canvas id="ch-en" height="150"></canvas></div>'+
  "</div>"+
  '<div class="sec">Todos os Posts</div><div class="pgrd">'+posts.map(function(pt,i){return pCard(pt,i);}).join("")+"</div>";

/* --- Secao 5: Charts --- */
var chrono=[].concat(posts).sort(function(a,b){return new Date(a.timestamp)-new Date(b.timestamp);});
var rP=chrono.filter(function(x){return x.type==="Reels";});
var cP=chrono.filter(function(x){return x.type==="Carrossel";});
var fP=chrono.filter(function(x){return x.type==="Foto";});

function drawLine(cid,series,valFn,colors,isPct){
  var cv=document.getElementById(cid);if(!cv)return;
  var W=cv.parentElement.offsetWidth||800;cv.width=W;
  var H=cv.height,ctx=cv.getContext("2d");
  var P={t:10,r:20,b:28,l:52},cW=W-P.l-P.r,cH=H-P.t-P.b;
  var mx=1;
  series.forEach(function(s){s.forEach(function(x){var v=valFn(x);if(v>mx)mx=v;});});
  ctx.clearRect(0,0,W,H);
  [0,.5,1].forEach(function(f){
    var y=P.t+cH*(1-f);
    ctx.strokeStyle="#eee";ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(P.l,y);ctx.lineTo(P.l+cW,y);ctx.stroke();
    ctx.fillStyle="#bbb";ctx.font="10px Inter,sans-serif";ctx.textAlign="right";
    ctx.fillText(isPct?(mx*f).toFixed(1)+"%":FN(Math.round(mx*f)),P.l-4,y+4);
  });
  series.forEach(function(pts,si){
    if(!pts||pts.length===0)return;
    ctx.strokeStyle=colors[si];ctx.lineWidth=2;ctx.beginPath();
    pts.forEach(function(x,i){
      var px=P.l+(pts.length===1?cW/2:i/(pts.length-1)*cW);
      var py=P.t+cH*(1-valFn(x)/mx);
      if(i===0)ctx.moveTo(px,py);else ctx.lineTo(px,py);
    });
    ctx.stroke();
    pts.forEach(function(x,i){
      var px=P.l+(pts.length===1?cW/2:i/(pts.length-1)*cW);
      var py=P.t+cH*(1-valFn(x)/mx);
      ctx.beginPath();ctx.arc(px,py,4,0,Math.PI*2);
      ctx.fillStyle=colors[si];ctx.fill();
      ctx.strokeStyle="#fff";ctx.lineWidth=1.5;ctx.stroke();
    });
  });
  var flat=[];series.forEach(function(s){flat=flat.concat(s);});
  flat.sort(function(a,b){return new Date(a.timestamp)-new Date(b.timestamp);});
  if(flat.length){
    ctx.fillStyle="#ccc";ctx.font="10px Inter,sans-serif";
    ctx.textAlign="left";ctx.fillText((flat[0].timestamp||"").substring(0,10),P.l,H-4);
    if(flat.length>1){ctx.textAlign="right";ctx.fillText((flat[flat.length-1].timestamp||"").substring(0,10),P.l+cW,H-4);}
  }
  cv._s=series;cv._vf=valFn;cv._cl=colors;cv._ip=isPct;cv._P=P;cv._mx=mx;
}

function addTip(cid,names){
  var cv=document.getElementById(cid);if(!cv)return;
  cv.addEventListener("mousemove",function(e){
    var r=cv.getBoundingClientRect();
    var mx2=(e.clientX-r.left)*(cv.width/r.width);
    var my2=(e.clientY-r.top)*(cv.height/r.height);
    var P=cv._P,W=cv.width,H=cv.height,cW=W-P.l-P.r,cH=H-P.t-P.b;
    var series=cv._s,vf=cv._vf,cl=cv._cl,maxV=cv._mx,isPct=cv._ip;
    var best=null,bd=Infinity;
    series.forEach(function(pts,si){
      if(!pts)return;
      pts.forEach(function(x,i){
        var px=P.l+(pts.length===1?cW/2:i/(pts.length-1)*cW);
        var py=P.t+cH*(1-vf(x)/maxV);
        var d=Math.hypot(mx2-px,my2-py);
        if(d<bd){bd=d;best={x:x,si:si,px:px,py:py,v:vf(x)};}
      });
    });
    drawLine(cid,series,vf,cl,isPct);
    if(best&&bd<20){
      var ctx=cv.getContext("2d");
      ctx.beginPath();ctx.arc(best.px,best.py,7,0,Math.PI*2);ctx.fillStyle=cl[best.si];ctx.fill();
      var lbl=isPct?best.v.toFixed(2)+"%":FN(Math.round(best.v));
      var txt=(names[best.si]||"")+": "+lbl+"  "+(best.x.timestamp||"").substring(0,10);
      ctx.font="12px Inter,sans-serif";
      var tw=ctx.measureText(txt).width+16,tx=best.px+12,ty=best.py-32;
      if(tx+tw>W-4)tx=best.px-tw-12;if(ty<4)ty=best.py+12;
      ctx.fillStyle="rgba(26,26,46,.85)";ctx.fillRect(tx,ty,tw,22);
      ctx.fillStyle="#fff";ctx.textAlign="left";ctx.fillText(txt,tx+8,ty+15);
    }
  });
  cv.addEventListener("mouseleave",function(){
    var el=this;drawLine(cid,el._s,el._vf,el._cl,el._ip);
  });
}

setTimeout(function(){
  var rc="#9333ea",cc="#2563eb",fc="#16a34a";
  var lkFn=function(x){return N(x.likesCount===-1?0:x.likesCount);};
  var vwFn=function(x){return N(x.viewsCount);};
  var enFn=function(x){return N(x.engagementRate);};
  drawLine("ch-lk",[rP,cP,fP],lkFn,[rc,cc,fc],false);
  drawLine("ch-vw",[rP],vwFn,[rc],false);
  drawLine("ch-en",[rP,cP,fP],enFn,[rc,cc,fc],true);
  addTip("ch-lk",["Reels","Carrossel","Foto"]);
  addTip("ch-vw",["Reels"]);
  addTip("ch-en",["Reels","Carrossel","Foto"]);
},200);
})();
</script>
</body>
</html>
'@

$html = $html.Replace("__JSON__", $json)
$utf8 = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($DASHBOARD, $html, $utf8)
Log "Dashboard salvo: $DASHBOARD"
Log "== Concluido =="

if ($Abrir) {
    Start-Process $DASHBOARD
    Log "Abrindo no navegador..."
}
