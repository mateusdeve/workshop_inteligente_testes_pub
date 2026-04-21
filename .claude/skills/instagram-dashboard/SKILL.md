---
name: instagram-dashboard
description: >
  Configura dashboard HTML de metricas do Instagram via Apify. Coleta dados
  publicos do perfil (seguidores, bio, foto), posts recentes e Reels (likes,
  comentarios, views). Todas as imagens embutidas em base64. Busca expandida
  para substituir posts com likes ocultos (ate 100 posts). Roda localmente
  na maquina do mentorado, sem servidor, sem GitHub, sem agendamento automatico.
---

# Instagram Dashboard. Metricas Diarias Automaticas

## Quando Usar

- Quando o aluno quiser monitorar o crescimento do proprio perfil no Instagram de forma automatica, sem precisar abrir ferramentas toda manha.
- Como base de dados para `/copy-social` (conteudo baseado no que ja funciona) e `/dados-instagram` (analise profunda com insights de copy).
- Quando o aluno precisar mostrar evolucao de metricas para clientes ou parceiros.

**Nao usar para:**
- Analisar perfis de concorrentes (usar `/dados-instagram`).
- Perfis privados (o Apify nao coleta dados de perfis privados).

## O Que Entrega

| Arquivo | Descricao |
|---|---|
| `entregas/instagram-dashboard/dashboard.html` | Dashboard HTML completo, abre no navegador |
| `entregas/instagram-dashboard/atualizar.py` | Script Python principal (Windows, macOS, Linux) |
| `entregas/instagram-dashboard/atualizar_powershell.ps1` | Script PowerShell de backup (Windows validado) |
| `entregas/instagram-dashboard/imagens/` | Thumbnails e slides dos top 10 posts (gerados pelo script) |
| `entregas/instagram-dashboard/log.txt` | Log de cada execucao com timestamp e status |
| `entregas/conta.md` | Config de conta (Instagram, YouTube, Site, WhatsApp) |

## Como Funciona

```
atualizar.py  (ou atualizar_powershell.ps1 no Windows como backup)
  ├── POST apify~instagram-scraper (sync, timeout 60s)
  │     directUrls + resultsType:"details"  → seguidores, bio, foto de perfil
  │     Baixa profilePicUrl via requests/WebClient → base64
  ├── POST apify~instagram-scraper (sync, timeout 300s) — loop ate 100 posts
  │     directUrls + resultsType:"posts"    → posts (fotos, carrosseis, reels)
  │     Se posts com likesCount=-1 > 0: expande resultsLimit e busca de novo
  │     Para quando tiver 30 posts com likes visiveis OU atingir 100 posts
  │     Seleciona 30 priorizando posts com likes visiveis
  ├── Para cada post: baixa displayUrl via requests/WebClient → base64
  │     Para carrosseis: baixa cada imagem do array images → base64
  │     (CDN do Instagram bloqueia URLs diretas em HTML local)
  ├── Salva thumbnails e slides como .jpg em entregas/instagram-dashboard/imagens/
  │     Armazena caminhos relativos em insights.json (thumbnailPath, carouselPaths)
  │     Para Reels: transcreve audio via apify~whisper-speech-to-text → transcricao
  └── Regenera dashboard.html com dados + imagens embutidos como variavel JS
```

O `dashboard.html` e sempre autossuficiente: dados e thumbnails embutidos diretamente no HTML gerado pelo script. Nao depende de servidor local nem de `fetch()`. Funciona abrindo direto no navegador, inclusive offline apos a primeira geracao.

## APIs Utilizadas

Uma chamada de perfil + loop de posts (ambas sync, mesmo ator):

| # | Ator Apify | Tipo | Parametro chave | Retorna |
|---|---|---|---|---|
| 1 | `apify~instagram-scraper` | sync, timeout 60s | `directUrls`, `resultsType: "details"` | seguidores, bio, foto, verificado |
| 2 | `apify~instagram-scraper` | sync, timeout 300s | `directUrls`, `resultsType: "posts"`, `resultsLimit: 30..100` | posts com likes, comentarios, views. Expande ate 100 para substituir likes ocultos. |

**Por que sync e nao async:** o endpoint async do Apify retorna run IDs que ficam inacessiveis via polling (`record-not-found`) dependendo do plano da conta. O sync e mais simples e confiavel.

**Todas as imagens em base64:** o CDN do Instagram bloqueia carregamento de imagens de arquivos HTML locais. O script baixa TODAS as imagens (foto de perfil, thumbnails dos posts, imagens do carrossel) via `requests` (Python) ou `WebClient` (PowerShell) com `User-Agent` e `Referer: https://www.instagram.com/` e converte para `data:image/jpeg;base64,...`.

**Campo de imagem usado:** `displayUrl` (thumbnail JPEG do post). Para carrosseis, o campo `images` pode estar vazio — o script usa `displayUrl` como fallback. O cycling de carrossel funciona quando `images` tem multiplas entradas.

**insights.json com caminhos de arquivo:** alem de embutir base64 no dashboard, o script salva os thumbnails e slides como `.jpg` em `entregas/instagram-dashboard/imagens/` e armazena os caminhos relativos no `insights.json` (`thumbnailPath`, `carouselPaths`). Isso permite que o `/copy-variacao-post` use o Read tool do Claude para analisar visualmente as imagens.

**Transcricao de Reels:** para posts do tipo Video, o script chama `apify~whisper-speech-to-text` com a `videoUrl` do post e armazena a transcricao em `insights.json`. O `/copy-variacao-post` usa essa transcricao para entender o conteudo real do Reel sem precisar reproduzir o video.

Custo total: ~US$0,20-0,50/mes no plano gratuito Apify (varia com quantas iteracoes de busca expandida forem necessarias).

## Compatibilidade por Sistema Operacional

O script principal e `atualizar.py` (Python 3), que funciona nativamente em todos os sistemas. O `atualizar_powershell.ps1` e o backup validado para Windows.

Instalacao da dependencia (unica):
```
pip install requests
```

| OS | Script | Como rodar |
|---|---|---|
| Windows | `atualizar.py` | `python atualizar.py --abrir` |
| macOS | `atualizar.py` | Python 3 ja incluso. `python3 atualizar.py --abrir` |
| Linux | `atualizar.py` | Python 3 ja incluso. `python3 atualizar.py --abrir` |
| Windows (backup) | `atualizar_powershell.ps1` | `powershell -ExecutionPolicy Bypass -File atualizar_powershell.ps1 -Abrir` |

## Configuracao Necessaria

| Chave | Onde fica | Como obter |
|---|---|---|
| `APIFY_API_TOKEN` | `.env` | console.apify.com > Settings > Integrations > Personal API token |
| `IG_USER` | `.env` | @ do perfil do aluno (sem @, lowercase). Tambem salvo em `entregas/conta.md` |

## Dashboard: O Que Mostra

**ESTRUTURA OBRIGATORIA — todas as 6 secoes devem estar presentes em todos os dashboards gerados, nesta ordem:**

1. **Cabecalho (perfil):** foto de perfil em base64 (fallback: inicial do nome), @username, bio, ultima atualizacao
2. **Visao Geral (4 cards KPI):** seguidores, engajamento medio (%), total de posts, formato mais postado
3. **Desempenho por Formato:** cards separados para Reels, Carrossel e Foto com media de likes, comentarios e views totais (Reels). Obrigatorio mesmo que so haja um formato.
4. **Top 3 Posts:** os 3 com maior engajamento, com thumbnail em base64, badge de tipo, likes, comentarios, views (Reels), taxa de engajamento e link "Ver post original"
5. **Linha do Tempo (3 graficos):** canvas puro, um grafico por metrica, empilhados verticalmente dentro do mesmo card. (a) **Curtidas:** uma linha por formato (Reels roxo, Carrossel azul, Foto verde), eixo Y com rotulos em 0%, 50% e 100% do maximo. (b) **Visualizacoes (Reels):** apenas a linha de Reels (unico formato com viewsCount). (c) **Engajamento (%):** uma linha por formato. Todos os graficos: pontos em cada post, linha conectando cronologicamente, eixo X com data mais antiga (esquerda) e mais recente (direita), grid horizontal sutil, tooltip colorido com tipo, valor e data ao passar o mouse.
6. **Todos os Posts (grade):** thumbnail ciclavel em base64 (click para avancar imagens do carrossel com indicador "X/N"), badge de tipo, likes, comentarios, views (Reels), data, primeiros 120 chars da legenda e link "Ver post original"

**NUNCA omitir nenhuma dessas 6 secoes.** Nao existe versao simplificada do dashboard.

## Fluxo Resumido

```
PASSO 0  Detectar estado
         ├── Ler .env para verificar APIFY_API_TOKEN (SEMPRE antes de pedir ao usuario)
         ├── Dashboard ja existe? → menu de acoes (abrir, atualizar, trocar, recriar)
         └── Primeira vez? → coletar username → (token ja vem do .env) → confirmar → criar

PASSO 1  Confirmacao com resumo
PASSO 2  Gerar atualizar.py (token e username embutidos)
         CRITICO: Ler o arquivo entregas/instagram-dashboard/atualizar.py existente
         e usar como template — substituir APENAS APIFY_TOKEN e IG_USER.
         Se nao existir, gerar do zero seguindo RIGOROSAMENTE todas as Regras desta
         skill (base64, busca expandida, likes ocultos, 6 secoes obrigatorias).
PASSO 3  Executar o script imediatamente e abrir o dashboard no navegador
PASSO 4  Entrega com proximos passos
```

**Sem agendamento automatico:** nao configurar CronCreate nem schtasks. O aluno roda o script manualmente quando quiser atualizar. Comando para atualizar:
```
python3 entregas/instagram-dashboard/atualizar.py --abrir
```
Windows sem Python no PATH:
```
python entregas/instagram-dashboard/atualizar.py --abrir
```
Backup PowerShell (Windows):
```
powershell -ExecutionPolicy Bypass -File entregas\instagram-dashboard\atualizar_powershell.ps1 -Abrir
```

## Regras

- **Sempre ler `.env` antes de pedir o token Apify ao usuario.** Se `APIFY_API_TOKEN` estiver presente, usar diretamente. So perguntar se o arquivo nao existir ou a chave estiver vazia.
- O token Apify e o username do Instagram ficam no `.env` (`APIFY_API_TOKEN` e `IG_USER`). O script le essas variaveis do `.env` em runtime. Nunca hardcodar no script.
- Nunca sobrescrever `entregas/conta.md` inteiro. Usar Edit cirurgico para atualizar so o campo `Instagram:`.
- Dashboard em HTML puro. Sem libs externas alem de Google Fonts. Canvas puro para grafico.
- Nao usar travessao em nenhum texto exibido no dashboard.
- Se o perfil for privado, informar e sugerir export manual via Metricool ou Instagram Insights.
- **CRITICO — Thumbnails obrigatorios em base64:** NUNCA usar a URL do CDN do Instagram diretamente como `src` de `<img>`. O CDN bloqueia carregamento de arquivos HTML locais. O script DEVE baixar cada thumbnail com `requests` (Python) ou `WebClient` (PowerShell) com User-Agent e Referer do Instagram e converter para `data:image/jpeg;base64,...` antes de embutir no JSON. Isso e inegociavel para as imagens aparecerem no dashboard.
- **CRITICO — Usar apenas `apify~instagram-scraper` com chamadas sync:** NAO usar atores `nH2AHrwxeTRJoN5hX` nem `xMc5Ga1oCONPmWJIa` (retornam run IDs inacessiveis no polling). Usar sempre o endpoint `run-sync-get-dataset-items` com `resultsType:"details"` (perfil) e `resultsType:"posts"` (posts), ambos via `directUrls` com a URL do perfil.
- **CRITICO — Campo de imagem correto:** o campo `displayUrl` do Apify retorna a thumbnail do post. O campo `images` pode estar vazio mesmo para carrosseis. O script deve sempre usar `displayUrl` como fallback obrigatorio para a thumbnail principal.
- **Likes ocultos (likesCount = -1):** o Instagram permite que criadores ocultem a contagem de likes por post. O Apify retorna `likesCount: -1` nesses casos. O script deve: (1) tentar buscar mais posts do perfil para substituir os com likes ocultos — expande o `resultsLimit` incrementalmente ate ter 30 posts com likes visiveis ou atingir o cap de 100 posts; (2) priorizar posts com likes visiveis na selecao final dos 30 exibidos; (3) exibir `--` no lugar de `-1` no dashboard; (4) usar `0` nos calculos internos (media, ordenacao Top 3, altura de barras no grafico).

## Proximos Passos Apos Configurar

- `/copy-social` — criar conteudo baseado nos posts com mais engajamento
- `/dados-instagram` — analise profunda com insights de copy e relatorio escrito
- `/copy-anuncio` — transformar os dados em anuncios com angulos testados
