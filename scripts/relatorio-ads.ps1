# Relatorio Diario Meta Ads
# Gerado automaticamente pelo Workshop Marketing IA
# Roda todo dia via Task Scheduler do Windows

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LogFile = Join-Path $ScriptDir "relatorio-ads.log"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $linha = "$ts - $msg"
    Write-Host $linha
    Add-Content -Path $LogFile -Value $linha -Encoding UTF8
}

# --- Credenciais ---
$FB_ACCESS_TOKEN_PERMANENTE = "EAAVUZAIy8ZAE4BRLAaGBnFBsboZApqPNvQZCvaRWi0s3s8gzTF5bZAApvwNBpsuLjZAXUHg3pR6uWtVR9zTCxGtMWKjyF9nWvPHq4Ru1o2iViWIaVYnJvVhgT1KtZCZCZAMSWcdZAq48mjQ6xb83ozfaUgC2bs8WAjYgM5ZCUHi6fKU5wUaWOpfZCd7UmlsxDKKMc3UYkAZDZD"
$FB_ACCESS_TOKEN_TEMPORARIO = ""
$FB_AD_ACCOUNT_ID   = "956832473206286"

# Prioriza token permanente
if ($FB_ACCESS_TOKEN_PERMANENTE -and $FB_ACCESS_TOKEN_PERMANENTE -ne "") {
    $FB_ACCESS_TOKEN = $FB_ACCESS_TOKEN_PERMANENTE
} elseif ($FB_ACCESS_TOKEN_TEMPORARIO -and $FB_ACCESS_TOKEN_TEMPORARIO -ne "") {
    $FB_ACCESS_TOKEN = $FB_ACCESS_TOKEN_TEMPORARIO
} else {
    Log "ERRO: Nenhum token encontrado. Configure FB_ACCESS_TOKEN_PERMANENTE ou FB_ACCESS_TOKEN_TEMPORARIO no script."
    exit 1
}
$ZAPI_INSTANCE_ID   = "3F1BE42A76BF134CBBEE06ABA24BC57F"
$ZAPI_TOKEN         = "40D4CEF2F70639DC22877991"
$ZAPI_CLIENT_TOKEN  = "F8e2521f13b3e4b05aa2908001542b598S"
$WHATSAPP_NUMERO    = "5511988095786"

Log "=== Iniciando relatorio Meta Ads ==="

# --- Data de ontem ---
$ontem    = (Get-Date).AddDays(-1)
$ontemISO = $ontem.ToString("yyyy-MM-dd")
$ontemBR  = $ontem.ToString("dd/MM/yyyy")
Log "Data: $ontemBR"

# --- Buscar metricas ---
$timeRange = "{`"since`":`"$ontemISO`",`"until`":`"$ontemISO`"}"
$fields    = "spend,impressions,reach,clicks,ctr,cpm,cpc,actions,cost_per_action_type"
$urlFB     = "https://graph.facebook.com/v25.0/act_$($FB_AD_ACCOUNT_ID)/insights?access_token=$FB_ACCESS_TOKEN&time_range=$([uri]::EscapeDataString($timeRange))&fields=$fields&level=account"

try {
    Log "Buscando metricas no Facebook Ads..."
    $resp  = Invoke-RestMethod -Uri $urlFB -Method GET -TimeoutSec 30
    $dados = $resp.data
} catch {
    Log "ERRO ao buscar metricas: $_"
    exit 1
}

# --- Montar mensagem ---
function FmtBRL($v) {
    try { return "R$ " + ([double]$v).ToString("N2", [System.Globalization.CultureInfo]::GetCultureInfo("pt-BR")) }
    catch { return "R$ $v" }
}
function FmtNum($v) {
    try { return ([long][double]$v).ToString("N0", [System.Globalization.CultureInfo]::GetCultureInfo("pt-BR")) }
    catch { return "$v" }
}

if (-not $dados -or $dados.Count -eq 0) {
    $mensagem = "*Relatorio Meta Ads - $ontemBR*`n`nSem dados para ontem. Verifique se ha campanhas ativas."
    Log "Sem dados para ontem."
} else {
    $d = $dados[0]

    $linhas = @()
    $linhas += "*Relatorio Meta Ads - $ontemBR*"
    $linhas += ""
    $linhas += "*Investimento e Alcance*"
    $linhas += "Gasto: $(FmtBRL $d.spend)"
    $linhas += "Alcance: $(FmtNum $d.reach)"
    $linhas += "Impressoes: $(FmtNum $d.impressions)"
    $linhas += ""
    $linhas += "*Engajamento*"
    $linhas += "Cliques: $(FmtNum $d.clicks)"
    $linhas += "CTR: $([double]$d.ctr -replace '\.',',')%"
    $linhas += "CPM: $(FmtBRL $d.cpm)"
    $linhas += "CPC: $(FmtBRL $d.cpc)"

    $conv = $d.actions | Where-Object { $_.action_type -in @("purchase","lead") } | Select-Object -First 1
    if ($conv) {
        $cpa = ($d.cost_per_action_type | Where-Object { $_.action_type -eq $conv.action_type } | Select-Object -First 1).value
        $linhas += ""
        $linhas += "*Conversoes*"
        $linhas += "Resultados: $(FmtNum $conv.value)"
        $linhas += "Custo por resultado: $(FmtBRL $cpa)"
    }

    $mensagem = $linhas -join "`n"
}

Log "Mensagem montada: $mensagem"

# --- Enviar via Z-API ---
$urlZapi  = "https://api.z-api.io/instances/$ZAPI_INSTANCE_ID/token/$ZAPI_TOKEN/send-text"
$headers  = @{ "Content-Type" = "application/json"; "Client-Token" = $ZAPI_CLIENT_TOKEN }
$payload  = @{ phone = $WHATSAPP_NUMERO; message = $mensagem } | ConvertTo-Json

try {
    Log "Enviando mensagem via Z-API..."
    $resultado = Invoke-RestMethod -Uri $urlZapi -Method POST -Headers $headers -Body $payload -TimeoutSec 30
    Log "Z-API resposta: $($resultado | ConvertTo-Json -Compress)"
    Log "=== Relatorio enviado com sucesso ==="
} catch {
    Log "ERRO ao enviar Z-API: $_"
    exit 1
}
