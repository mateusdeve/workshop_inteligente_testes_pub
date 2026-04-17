---
name: instagram-dashboard
description: >
  Configura dashboard HTML de metricas do Instagram atualizado automaticamente
  todo dia as 8h via Apify e Task Scheduler do Windows. Coleta dados publicos
  do perfil (seguidores, bio, engajamento) e dos posts recentes (likes,
  comentarios, tipo, data). Roda localmente na maquina do mentorado, sem
  servidor, sem GitHub.
---

# Instagram Dashboard. Metricas Diarias Automaticas

## Quando Usar

- Quando o aluno quiser monitorar o crescimento do proprio perfil no Instagram de forma automatica, sem precisar abrir ferramentas toda manha.
- Como base de dados para `/copy-social` (conteudo baseado no que ja funciona) e `/dados-instagram` (analise profunda com insights de copy).
- Quando o aluno precisar mostrar evolucao de metricas para clientes ou parceiros.

**Nao usar para:**
- Analisar perfis de concorrentes (usar `/dados-instagram`).
- Perfis privados (o Apify nao coleta dados de perfis privados).
- Ambientes sem Task Scheduler (Mac, Linux): recomendar cron job ou adaptacao manual.

## O Que Entrega

| Arquivo | Descricao |
|---|---|
| `entregas/instagram-dashboard/dashboard.html` | Dashboard HTML completo, abre no navegador |
| `entregas/instagram-dashboard/atualizar.ps1` | Script PowerShell que busca dados e regenera o dashboard |
| `entregas/instagram-dashboard/log.txt` | Log de cada execucao com timestamp e status |
| `entregas/conta.md` | Config de conta (Instagram, YouTube, Site, WhatsApp) |

## Como Funciona

```
Task Scheduler (todo dia 8h)
  └── atualizar.ps1
        ├── POST Apify → resultsType: "details"  (dados do perfil)
        ├── POST Apify → resultsType: "posts"    (20 posts recentes)
        ├── Calcula: engajamento medio, melhor tipo, total likes/comments
        └── Regenera dashboard.html com dados embutidos como variavel JS
```

O `dashboard.html` e sempre autossuficiente (dados embutidos via PowerShell here-string). Nao depende de servidor local nem de `fetch()`, funciona abrindo direto no navegador.

## APIs Utilizadas

| API | Endpoint | Custo |
|---|---|---|
| Apify Instagram Scraper | `POST /v2/acts/apify~instagram-scraper/run-sync-get-dataset-items` | ~US$ 0,10/mes plano gratuito |

Duas chamadas por execucao:
1. `resultsType: "details"`, `resultsLimit: 1` — dados do perfil
2. `resultsType: "posts"`, `resultsLimit: 20` — posts recentes

## Configuracao Necessaria

| Chave | Onde fica | Como obter |
|---|---|---|
| `APIFY_API_TOKEN` | `.env` | console.apify.com > Settings > Integrations > Personal API token |
| `Instagram:` | `entregas/conta.md` | @ do perfil do aluno |

## Dashboard: O Que Mostra

- **Cabecalho:** inicial do nome, @username, bio, ultima atualizacao
- **4 cards:** seguidores, engajamento medio (%), total de posts, formato mais postado
- **Grafico de barras:** likes por post (canvas puro, 20 barras)
- **Grade de posts:** thumbnail, tipo (Reels/Foto/Carrossel), likes, comentarios, data, primeiros 120 chars da legenda

## Fluxo Resumido

```
PASSO 0  Detectar estado
         ├── Dashboard ja existe? → menu de acoes (abrir, atualizar, trocar, recriar)
         └── Primeira vez? → coletar username + token → confirmar → criar

PASSO 1  Confirmacao com resumo
PASSO 2  Gerar atualizar.ps1 (token e username embutidos)
PASSO 3  Registrar no Task Scheduler via schtasks
PASSO 4  Primeira execucao + abrir no navegador
PASSO 5  Entrega com proximos passos
```

## Regras

- O token Apify fica embutido no `.ps1` (nao lido do `.env` em runtime) para o Task Scheduler funcionar sem ambiente do Claude.
- Nunca sobrescrever `entregas/conta.md` inteiro. Usar Edit cirurgico para atualizar so o campo `Instagram:`.
- Dashboard em HTML puro. Sem libs externas alem de Google Fonts. Canvas puro para grafico.
- Nao usar travessao em nenhum texto exibido no dashboard.
- Se o perfil for privado, informar e sugerir export manual via Metricool ou Instagram Insights.

## Proximos Passos Apos Configurar

- `/copy-social` — criar conteudo baseado nos posts com mais engajamento
- `/dados-instagram` — analise profunda com insights de copy e relatorio escrito
- `/copy-anuncio` — transformar os dados em anuncios com angulos testados
