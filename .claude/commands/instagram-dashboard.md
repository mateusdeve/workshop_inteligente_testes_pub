---
name: workshop-marketing:instagram-dashboard
description: Criar dashboard HTML de metricas do Instagram atualizado automaticamente todo dia via Apify. Configura o perfil em entregas/conta.md, gera o script de atualizacao e agenda a tarefa local no Claude (sem Task Scheduler, sem permissao de admin). Roda localmente enquanto o Claude estiver aberto.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion, mcp__scheduled-tasks__create_scheduled_task, mcp__scheduled-tasks__list_scheduled_tasks, mcp__scheduled-tasks__update_scheduled_task
model: sonnet
---

# Dashboard Instagram. Metricas Diarias Automaticas

Cria um dashboard HTML de metricas do Instagram que se atualiza sozinho todo dia as 8h, sem o aluno precisar abrir nada. Usa o Apify para coletar dados publicos do perfil (seguidores, bio, engajamento) e dos posts recentes (likes, comentarios, tipo, data).

O aluno abre o `dashboard.html` no navegador e ve os dados mais recentes. A tarefa agendada do proprio Claude dispara o script em segundo plano todo dia as 8h.

## COMO FUNCIONA

1. Claude coleta o username do Instagram (de `entregas/conta.md`) e o token do Apify (do `.env`)
2. Claude gera o `atualizar.ps1`, script que busca dados, mescla com historico e regenera o dashboard
3. Claude cria uma tarefa agendada local no proprio Claude (sem Task Scheduler, sem permissao de admin)
4. Claude dispara o script uma vez para testar e abre o dashboard

O `dashboard.html` e gerado pelo script a cada execucao com os dados embutidos diretamente, sem depender de servidor ou CORS. O `dados.json` acumula o historico completo de posts, nunca sobrescrevendo.

**Atencao:** a tarefa agendada do Claude roda enquanto o aplicativo estiver aberto. Se o computador estiver desligado ou o Claude fechado as 8h, a tarefa nao executa naquele dia.

---

## PASSO 0. Detectar Estado e Definir Fluxo

Antes de qualquer pergunta, verifique duas coisas em paralelo:

1. `entregas/conta.md` — existe campo `Instagram:` com valor?
2. `entregas/instagram-dashboard/atualizar.ps1` — o arquivo existe?

### Cenario A. Dashboard ja configurado (ambos existem)

Mostre o menu de acoes sem fazer perguntas extras:

```
Dashboard do Instagram ja esta configurado.

Perfil monitorado: @{username}
Ultima atualizacao: {data do dados.json, campo atualizadoEm, se existir}

O que quer fazer?

1. Abrir o dashboard agora
2. Atualizar os dados agora (rodar o script manualmente)
3. Trocar o perfil monitorado
4. Recriar a tarefa agendada no Claude (se parou de funcionar)
5. Reconfigurar tudo do zero
```

Acoes de cada opcao:

**Opcao 1 — Abrir:**
```bash
start entregas/instagram-dashboard/dashboard.html
```
Informe o caminho e encerre.

**Opcao 2 — Atualizar agora:**
```bash
powershell.exe -ExecutionPolicy Bypass -File "entregas/instagram-dashboard/atualizar.ps1"
```
Aguarde, leia `entregas/instagram-dashboard/log.txt`, informe o resultado e oferte abrir o dashboard.

**Opcao 3 — Trocar perfil:**
Pergunte o novo @. Normalize. Atualize `entregas/conta.md` com Edit cirurgico. Regere o `atualizar.ps1` com o novo username e token. Recrie a tarefa agendada (Passo 3). Dispare uma vez para testar.

**Opcao 4 — Recriar tarefa agendada:**
Execute apenas o Passo 3 abaixo. Confirme o resultado.

**Opcao 5 — Reconfigurar do zero:**
Siga o fluxo completo a partir do Cenario B abaixo.

---

### Cenario B. Primeira configuracao (arquivos nao existem)

#### 0.1 Username do Instagram

Leia `entregas/conta.md`. Se o arquivo existir, procure a linha que comeca com `Instagram:`.

**Se encontrar username:** confirme com o usuario:

```
Encontrei o Instagram configurado: @{username}

E esse mesmo perfil que quer monitorar?

1. Sim, pode continuar
2. Nao, quero usar outro
```

**Se o arquivo nao existir ou o campo Instagram estiver vazio:** pergunte:

```
Qual o @ do seu perfil no Instagram?
(ex: @meuperfil ou meuperfil, sem o @)
```

Normalize o username: remova o @ se vier com ele, converta para lowercase. Salve em `entregas/conta.md`:

- Se o arquivo nao existir: crie com Write usando o template abaixo
- Se existir sem o campo: adicione a linha com Edit cirurgico

Template de `entregas/conta.md`:

```markdown
# Conta

Instagram: @{username}
YouTube:
Site:
WhatsApp:
```

### 0.2 Token do Apify

Leia `.env`. Verifique se `APIFY_API_TOKEN` existe e tem valor nao vazio.

**Se tiver:** pule para o Passo 1.

**Se nao tiver:** execute a skill `configurar-apify`. Apos concluir, retorne ao Passo 1.

---

## PASSO 1. Confirmacao

Mostre o resumo antes de criar qualquer arquivo:

```
Configuracao confirmada:

- Perfil Instagram: @{username}
- Token Apify: configurado e testado
- Dashboard: entregas/instagram-dashboard/dashboard.html
- Historico: entregas/instagram-dashboard/dados.json
- Atualizacao automatica: todo dia as 8h via tarefa agendada do Claude

Custo estimado no Apify: menos de US$ 0,15/mes no plano gratuito.

1. Tudo certo, criar o dashboard
2. Quero ajustar algo
```

---

## PASSO 2. Gerar o Script PowerShell

Crie a pasta `entregas/instagram-dashboard/` se nao existir.

Salve o script abaixo em `entregas/instagram-dashboard/atualizar.ps1`.

Antes de salvar, substitua os dois placeholders no script:
- `APIFY_TOKEN_AQUI`: valor real lido do `.env` (campo `APIFY_API_TOKEN`)
- `USERNAME_AQUI`: username sem o @, lido de `entregas/conta.md`

O token fica embutido diretamente no script para que a tarefa agendada consiga rodar sem depender do ambiente do Claude.

**Modelo de dados persistente:**

O script mantem um `dados.json` como banco de dados local. A cada execucao:
1. Le o `dados.json` existente (se houver)
2. Busca os posts recentes no Apify
3. Deduplica pelo campo `shortCode` (ID unico e imutavel de cada post)
4. Adiciona apenas os posts novos ao historico acumulado
5. Ordena todos os posts por `timestamp` decrescente (mais recente primeiro)
6. Salva o `dados.json` atualizado
7. Regenera o `dashboard.html` com o historico completo

O `dados.json` fica em `entregas/instagram-dashboard/dados.json` e nunca e sobrescrito, apenas acrescido.

```powershell
# Dashboard Instagram - Script de Atualizacao
# Gerado automaticamente pelo Workshop Marketing IA
# Disparado todo dia as 8h pela tarefa agendada do Claude

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LogFile = Join-Path $ScriptDir "log.txt"
$DashboardFile = Join-Path $ScriptDir "dashboard.html"
$DadosFile = Join-Path $ScriptDir "dados.json"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $linha = "$ts - $msg"
    Write-Host $linha
    Add-Content -Path $LogFile -Value $linha -Encoding UTF8
}

Log "=== Iniciando atualizacao ==="

$APIFY_TOKEN    = "APIFY_TOKEN_AQUI"
$IG_USERNAME    = "USERNAME_AQUI"
$PROFILE_URL    = "https://www.instagram.com/$IG_USERNAME/"
$APIFY_ENDPOINT = "https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN"
$HEADERS        = @{ "Content-Type" = "application/json" }

# --- Buscar detalhes do perfil ---
Log "Buscando dados do perfil @$IG_USERNAME..."

$bodyPerfil = @{
    addParentData = $false
    directUrls    = @($PROFILE_URL)
    resultsLimit  = 1
    resultsType   = "details"
    searchLimit   = 1
    searchType    = "hashtag"
} | ConvertTo-Json

try {
    $resPerfil = Invoke-RestMethod -Uri $APIFY_ENDPOINT -Method POST -Headers $HEADERS -Body $bodyPerfil -TimeoutSec 120
    $perfil = $resPerfil[0]
    if (-not $perfil) { throw "Perfil vazio. Verifique se o @ esta correto e se o perfil e publico." }
    Log "Perfil carregado: $($perfil.username) | $($perfil.followersCount) seguidores"
} catch {
    Log "ERRO ao buscar perfil: $_"
    exit 1
}

# --- Buscar posts recentes ---
Log "Buscando posts recentes..."

$bodyPosts = @{
    addParentData = $false
    directUrls    = @($PROFILE_URL)
    resultsLimit  = 20
    resultsType   = "posts"
    searchLimit   = 1
    searchType    = "hashtag"
} | ConvertTo-Json

try {
    $postsApify = Invoke-RestMethod -Uri $APIFY_ENDPOINT -Method POST -Headers $HEADERS -Body $bodyPosts -TimeoutSec 120
    if (-not $postsApify -or $postsApify.Count -eq 0) { throw "Nenhum post encontrado." }
    Log "$($postsApify.Count) posts retornados pelo Apify"
} catch {
    Log "ERRO ao buscar posts: $_"
    exit 1
}

# --- Carregar historico existente ---
$historico = @()
if (Test-Path $DadosFile) {
    try {
        $dadosSalvos = Get-Content $DadosFile -Raw -Encoding UTF8 | ConvertFrom-Json
        $historico = @($dadosSalvos.posts)
        Log "Historico carregado: $($historico.Count) posts ja salvos"
    } catch {
        Log "Aviso: nao foi possivel ler dados.json, iniciando historico do zero"
        $historico = @()
    }
}

# --- Deduplica e adiciona posts novos ---
$codigosExistentes = @{}
foreach ($p in $historico) {
    if ($p.shortCode) { $codigosExistentes[$p.shortCode] = $true }
}

$novosCount = 0
foreach ($p in $postsApify) {
    $sc = if ($p.shortCode) { $p.shortCode } elseif ($p.url) { $p.url -replace '.*instagram.com/p/([^/]+).*','$1' } else { $null }
    if (-not $sc) { continue }
    if ($codigosExistentes.ContainsKey($sc)) { continue }

    $ts = $p.timestamp
    $dataStr = if ($ts) {
        ([DateTimeOffset]::FromUnixTimeSeconds([long]$ts)).LocalDateTime.ToString("dd/MM/yyyy")
    } else { "" }
    $legenda = if ($p.caption) { $p.caption.Substring(0, [Math]::Min(120, $p.caption.Length)) } else { "" }

    $novoPost = [ordered]@{
        shortCode   = $sc
        tipo        = if ($p.type) { $p.type } else { "image" }
        timestamp   = if ($ts) { [long]$ts } else { 0 }
        data        = $dataStr
        likes       = if ($p.likesCount)    { [int]$p.likesCount }    else { 0 }
        comentarios = if ($p.commentsCount) { [int]$p.commentsCount } else { 0 }
        legenda     = $legenda
        url         = $p.url
        imagem      = if ($p.displayUrl) { $p.displayUrl } else { "" }
    }
    $historico += $novoPost
    $codigosExistentes[$sc] = $true
    $novosCount++
}

Log "$novosCount posts novos adicionados ao historico"

# --- Ordenar por timestamp decrescente (mais recente primeiro) ---
$historico = @($historico | Sort-Object { [long]$_.timestamp } -Descending)

# --- Calcular metricas sobre todos os posts do historico ---
$postsCount    = $historico.Count
$totalLikes    = ($historico | Measure-Object -Property likes       -Sum).Sum
$totalComments = ($historico | Measure-Object -Property comentarios -Sum).Sum

$engajamento = if ($perfil.followersCount -gt 0 -and $postsCount -gt 0) {
    [math]::Round((($totalLikes + $totalComments) / $postsCount / $perfil.followersCount) * 100, 2)
} else { 0 }

$tipoContagem = @{}
foreach ($p in $historico) {
    $t = if ($p.tipo) { $p.tipo } else { "image" }
    $tipoContagem[$t] = ($tipoContagem[$t] -as [int]) + 1
}
$melhorTipo = ($tipoContagem.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 1).Key

# --- Salvar dados.json atualizado ---
$dadosObj = [ordered]@{
    atualizadoEm = (Get-Date -Format "dd/MM/yyyy 'as' HH:mm")
    perfil = [ordered]@{
        username    = $perfil.username
        nome        = $perfil.fullName
        bio         = $perfil.biography
        seguidores  = $perfil.followersCount
        seguindo    = $perfil.followsCount
        totalPosts  = $perfil.postsCount
        verificado  = $perfil.verified
    }
    metricas = [ordered]@{
        engajamentoMedio = $engajamento
        melhorTipo       = $melhorTipo
        totalLikes       = $totalLikes
        totalComments    = $totalComments
        postsNoHistorico = $postsCount
    }
    posts = $historico
}

$dadosObj | ConvertTo-Json -Depth 5 | Out-File -FilePath $DadosFile -Encoding UTF8
Log "dados.json salvo com $postsCount posts no historico"

$dadosJson = $dadosObj | ConvertTo-Json -Depth 5 -Compress

# --- Gerar HTML com dados embutidos ---
$html = @"
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard Instagram - @$IG_USERNAME</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0f0f0f; --surface: #1a1a1a; --border: #2a2a2a;
    --text: #f0f0f0; --muted: #777; --accent: #E1306C; --accent2: #833AB4;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); padding: 32px 20px; }
  .wrap { max-width: 1080px; margin: 0 auto; }
  .header { display: flex; align-items: center; gap: 20px; margin-bottom: 28px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
  .avatar { width: 68px; height: 68px; border-radius: 50%; background: linear-gradient(135deg, var(--accent), var(--accent2)); display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: 700; color: #fff; flex-shrink: 0; }
  .pinfo h1 { font-size: 20px; font-weight: 700; }
  .pinfo .handle { color: var(--muted); font-size: 13px; margin-top: 2px; }
  .pinfo .bio { font-size: 13px; color: #aaa; margin-top: 6px; max-width: 480px; line-height: 1.5; }
  .update { margin-left: auto; text-align: right; font-size: 12px; color: var(--muted); }
  .cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 28px; }
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 18px; }
  .card.hi { border-color: var(--accent); }
  .card .lbl { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
  .card .val { font-size: 26px; font-weight: 700; line-height: 1; }
  .card .sub { font-size: 11px; color: var(--muted); margin-top: 6px; }
  .sec { font-size: 11px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 14px; }
  .chart-box { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 28px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 12px; }
  .pcard { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; }
  .pthumb { width: 100%; aspect-ratio: 1/1; background: #222; overflow: hidden; display: flex; align-items: center; justify-content: center; color: var(--muted); font-size: 12px; }
  .pthumb img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .pbody { padding: 10px; }
  .pmeta { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--muted); margin-bottom: 4px; flex-wrap: wrap; }
  .ptipo { font-size: 10px; background: #2a2a2a; border-radius: 4px; padding: 2px 6px; text-transform: uppercase; letter-spacing: 0.3px; color: #999; }
  .pdata { font-size: 11px; color: var(--muted); }
  .pleg { font-size: 12px; color: #999; margin-top: 4px; line-height: 1.4; }
  @media(max-width:700px) { .cards { grid-template-columns: repeat(2, 1fr); } .header { flex-wrap: wrap; } .update { margin-left: 0; } }
</style>
</head>
<body>
<div class="wrap">

<div class="header">
  <div class="avatar" id="av"></div>
  <div class="pinfo">
    <h1 id="nome"></h1>
    <div class="handle" id="handle"></div>
    <div class="bio" id="bio"></div>
  </div>
  <div class="update">Ultima atualizacao<br><strong id="upd"></strong></div>
</div>

<div class="cards">
  <div class="card">
    <div class="lbl">Seguidores</div>
    <div class="val" id="seg"></div>
    <div class="sub">perfil publico</div>
  </div>
  <div class="card hi">
    <div class="lbl">Engajamento medio</div>
    <div class="val" id="eng"></div>
    <div class="sub">historico completo</div>
  </div>
  <div class="card">
    <div class="lbl">Total de posts</div>
    <div class="val" id="total"></div>
    <div class="sub">no perfil</div>
  </div>
  <div class="card">
    <div class="lbl">Formato mais postado</div>
    <div class="val" id="tipo" style="font-size:16px;margin-top:6px;"></div>
    <div class="sub" id="sub-historico"></div>
  </div>
</div>

<div class="chart-box">
  <div class="sec">Likes por post (mais recente a esquerda)</div>
  <canvas id="chart"></canvas>
</div>

<div class="sec">Todos os posts (mais recente primeiro)</div>
<div class="grid" id="grid"></div>

</div>
<script>
const D = $dadosJson;
const fmt = n => n >= 1000 ? (n/1000).toFixed(1)+'k' : String(n||0);
const TIPOS = { video:'Reels', image:'Foto', sidecar:'Carrossel' };

document.getElementById('av').textContent     = (D.perfil.nome || D.perfil.username || '?')[0].toUpperCase();
document.getElementById('nome').textContent   = D.perfil.nome || '@'+D.perfil.username;
document.getElementById('handle').textContent = '@'+D.perfil.username + (D.perfil.verificado ? ' \u2713' : '');
document.getElementById('bio').textContent    = D.perfil.bio || '';
document.getElementById('upd').textContent    = D.atualizadoEm;
document.getElementById('seg').textContent    = fmt(D.perfil.seguidores);
document.getElementById('eng').textContent    = D.metricas.engajamentoMedio + '%';
document.getElementById('total').textContent  = fmt(D.perfil.totalPosts);
document.getElementById('tipo').textContent   = TIPOS[D.metricas.melhorTipo] || D.metricas.melhorTipo || 'Posts';
document.getElementById('sub-historico').textContent = D.metricas.postsNoHistorico + ' posts no historico';

const canvas = document.getElementById('chart');
const ctx    = canvas.getContext('2d');
const posts  = D.posts;
canvas.width  = canvas.parentElement.clientWidth - 40;
canvas.height = 120;
const maxL = Math.max(...posts.map(p => p.likes), 1);
const bw   = (canvas.width - 20) / Math.max(posts.length, 1);
posts.forEach((p, i) => {
  const h = Math.max(4, (p.likes / maxL) * 90);
  ctx.fillStyle = i === 0 ? '#E1306C' : '#6a6a6a';
  ctx.beginPath();
  const x = 10 + i * bw + 2;
  const y = 110 - h;
  const r = 3;
  const w = bw - 4;
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.arcTo(x+w, y, x+w, y+r, r);
  ctx.lineTo(x+w, y+h);
  ctx.lineTo(x, y+h);
  ctx.lineTo(x, y+r);
  ctx.arcTo(x, y, x+r, y, r);
  ctx.closePath();
  ctx.fill();
});

const grid = document.getElementById('grid');
posts.forEach(p => {
  const tipo = TIPOS[p.tipo] || p.tipo;
  const leg  = p.legenda.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  const thumb = p.imagem
    ? '<img src="'+p.imagem+'" alt="post" onerror="this.parentElement.innerHTML=\'[sem preview]\'">'
    : '[sem preview]';
  grid.insertAdjacentHTML('beforeend',
    '<div class="pcard">'
    + '<div class="pthumb">'+thumb+'</div>'
    + '<div class="pbody">'
    +   '<div class="pmeta">'
    +     '<span>\u2665 '+fmt(p.likes)+'</span>'
    +     '<span>\u{1F4AC} '+fmt(p.comentarios)+'</span>'
    +     '<span class="ptipo">'+tipo+'</span>'
    +   '</div>'
    +   '<div class="pdata">'+p.data+'</div>'
    +   '<div class="pleg">'+leg+'</div>'
    + '</div></div>'
  );
});
</script>
</body>
</html>
"@

$html | Out-File -FilePath $DashboardFile -Encoding UTF8
Log "Dashboard salvo: $DashboardFile"
Log "=== Atualizacao concluida ==="
```

---

## PASSO 3. Criar Tarefa Agendada no Claude

Obtenha o caminho absoluto do script:

```bash
pwd
```

Use o resultado para montar o caminho Windows do script (ex: `C:\Users\gabri\Documents\GitHub\workshop_inteligente\entregas\instagram-dashboard\atualizar.ps1`).

Crie a tarefa agendada usando `mcp__scheduled-tasks__create_scheduled_task` com os parametros abaixo. Substitua `{CAMINHO_ABSOLUTO_PS1}` pelo caminho real obtido acima e `{USERNAME}` pelo username do Instagram.

```
taskId: instagram-dashboard-{username}
description: Atualizar dashboard Instagram @{username} com dados do Apify
cronExpression: 0 8 * * *
prompt: |
  Voce e o agente de atualizacao diaria do Dashboard Instagram do Workshop Marketing IA.

  Execute o seguinte comando PowerShell para atualizar o dashboard:

  powershell.exe -ExecutionPolicy Bypass -File "{CAMINHO_ABSOLUTO_PS1}"

  Aguarde a conclusao (pode levar ate 90 segundos).

  Depois leia o arquivo de log em {CAMINHO_ABSOLUTO_PS1 com log.txt no lugar de atualizar.ps1} e verifique se terminou com sucesso.

  Se houver erro no log, registre o problema mas nao tente corrigir automaticamente.
```

**Se retornar sucesso:** tarefa criada, continuar para o Passo 4.

**Se a ferramenta `mcp__scheduled-tasks__create_scheduled_task` nao estiver disponivel:** informe ao usuario:

```
A ferramenta de tarefas agendadas do Claude nao esta disponivel nesta sessao.

Alternativa: criar a tarefa manualmente em Configuracoes > Tarefas Agendadas dentro do Claude Code,
ou reabrir o Claude Code e tentar novamente.
```

---

## PASSO 4. Primeira Execucao (Teste)

Execute o script uma vez para confirmar que tudo funciona:

```bash
powershell.exe -ExecutionPolicy Bypass -File "entregas/instagram-dashboard/atualizar.ps1"
```

Aguarde. Pode levar de 30 a 90 segundos (o Apify roda o scraper em tempo real).

Leia `entregas/instagram-dashboard/log.txt` para ver o resultado:

```bash
tail -20 entregas/instagram-dashboard/log.txt
```

**Erros comuns e solucoes:**

| Erro no log | Causa | Solucao |
|---|---|---|
| `401` ou `AuthenticationError` | Token Apify invalido | Verificar o token em console.apify.com |
| `Perfil vazio` | @ errado ou perfil privado | Confirmar o username; perfis privados nao funcionam |
| `Nenhum post encontrado` | Perfil sem posts publicos | Nada a fazer |
| `TimeoutSec` | Apify demorou mais de 2min | Rodar novamente; pode ser instabilidade temporaria |

Se o script funcionar, abra o dashboard:

```bash
start entregas/instagram-dashboard/dashboard.html
```

---

## PASSO 5. Entrega

```
Dashboard configurado.

Arquivos criados:
- Dashboard:  entregas/instagram-dashboard/dashboard.html
- Historico:  entregas/instagram-dashboard/dados.json
- Script:     entregas/instagram-dashboard/atualizar.ps1
- Log:        entregas/instagram-dashboard/log.txt

Tarefa agendada criada no Claude: roda todo dia as 8h enquanto o app estiver aberto.
A cada execucao, apenas posts novos sao adicionados ao historico.
O dashboard mostra todos os posts acumulados, ordenados do mais recente ao mais antigo.

Perfil monitorado: @{username}
Dados coletados: seguidores, engajamento, tipo de post, historico completo de posts.

Proximos passos sugeridos:
- /copy-social para criar conteudo baseado nos posts que mais engajaram
- /dados-instagram para analise mais profunda com insights de copy
- /copy-anuncio para transformar os dados em anuncios testados
```

---

## CHECKPOINTS OBRIGATORIOS

| Etapa | Aprovacao? |
|---|---|
| Username do Instagram confirmado | Sim, obrigatoria |
| Token Apify verificado no .env | Confirmado antes de continuar |
| Confirmacao geral (Passo 1) | Sim, obrigatoria |
| Script gerado com token embutido | Verificar antes de salvar |
| Tarefa agendada criada no Claude | Confirmar retorno da ferramenta |
| Primeira execucao | Rodar, ler log, confirmar criacao do dados.json |

---

## REGRAS

- Nunca sobrescrever `entregas/conta.md` inteiro. Usar Edit para atualizar so o campo `Instagram:`.
- O token do Apify fica embutido no script PowerShell (nao lido do .env em runtime) para que a tarefa agendada consiga rodar sem depender do ambiente do Claude.
- Se o perfil for privado, o Apify nao consegue coletar. Informar ao usuario e sugerir export manual via Metricool ou Instagram Insights.
- Dashboard em HTML puro. Sem libs externas alem de Google Fonts. Canvas puro para grafico de barras.
- O `dados.json` e o banco de dados local. Nunca sobrescrever; sempre ler, mesclar e salvar de volta.
- A deduplicacao usa o campo `shortCode` do post. Se o Apify nao retornar o shortCode, extrair da URL (`/p/{shortCode}/`).
- Posts sempre ordenados por `timestamp` decrescente no `dados.json` e no dashboard.
- O script regenera o `dashboard.html` completo a cada execucao com os dados do `dados.json`. Nao ha dependencia de `fetch()` ou servidor local.
- A tarefa agendada do Claude roda enquanto o app estiver aberto. Informar isso ao usuario na entrega.
- Nao usar travessao em nenhum texto exibido no dashboard.
- Nao exibir o script PS1 no chat. Salvar silenciosamente e informar apenas o caminho.
