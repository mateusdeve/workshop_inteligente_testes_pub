---
name: youtube-dashboard
description: >
  Configura dashboard HTML de metricas do YouTube via Apify. Coleta dados
  publicos do canal (inscritos, total de views, descricao), videos recentes
  (views, likes, comentarios, duracao, titulo, thumbnail). Todas as
  thumbnails embutidas em base64. Roda localmente na maquina do mentorado,
  sem servidor, sem GitHub, sem agendamento automatico.
---

# YouTube Dashboard. Metricas Diarias Automaticas

## Quando Usar

- Quando o aluno quiser monitorar o crescimento do proprio canal no YouTube de forma automatica, sem precisar abrir o YouTube Studio toda manha.
- Como base de dados para `/copy-roteiro` (roteiros baseados nos videos que performam melhor) e analise de padroes de titulo e thumbnail.
- Quando o aluno precisar mostrar evolucao de metricas para clientes ou parceiros.

**Nao usar para:**
- Analisar canais de concorrentes (adaptar o script passando outro canal).
- Dados avancados do YouTube Analytics (CPM, receita, retencao) — esses requerem a YouTube Data API com OAuth, fora do escopo do Apify.

## O Que Entrega

| Arquivo | Descricao |
|---|---|
| `.claude/skills/youtube-dashboard/scripts/atualizar.py` | Script Python principal (Windows, macOS, Linux) — compartilhado entre todos os produtos |
| `meus-produtos/{ativo}/entregas/youtube-dashboard/dashboard.html` | Dashboard HTML completo, abre no navegador |
| `meus-produtos/{ativo}/entregas/youtube-dashboard/imagens/` | Thumbnails dos videos (gerados pelo script) |
| `meus-produtos/{ativo}/entregas/youtube-dashboard/insights.json` | Dados estruturados sem base64 |
| `meus-produtos/{ativo}/entregas/youtube-dashboard/historico.json` | Snapshots acumulativos (inscritos, engajamento) entre execucoes |
| `meus-produtos/{ativo}/entregas/youtube-dashboard/log.txt` | Log de cada execucao com timestamp e status |

## Como Funciona

```
atualizar.py
  ├── POST Apify (ator YouTube, sync) — canal
  │     channelUrl ou channelId → inscritos, total views, descricao, avatar
  │     Baixa avatar → base64
  ├── POST Apify (ator YouTube, sync) — videos
  │     channelUrl → ultimos N videos
  │     Para cada video: views, likes, comentarios, duracao, titulo, data, thumbnail
  │     Baixa thumbnail de cada video → base64
  ├── Calcula metricas: engajamento = (likes + comentarios) / views * 100
  ├── Atualiza historico.json com snapshot do dia
  └── Regenera dashboard.html com dados + thumbnails embutidos como variavel JS
```

O `dashboard.html` e sempre autossuficiente. Nao depende de servidor local. Funciona abrindo direto no navegador, inclusive offline apos a primeira geracao.

## APIs Utilizadas

> **A definir durante o desenvolvimento do script:** pesquisar o ator Apify mais confiavel para YouTube no momento da implementacao. Candidatos: `apify~youtube-scraper`, `bernardo/youtube-scraper`.

| # | Ator Apify | Tipo | Parametro chave | Retorna |
|---|---|---|---|---|
| 1 | TBD (canal) | sync | `channelUrl` ou `channelId` | inscritos, total views, descricao, avatar |
| 2 | TBD (videos) | sync | `channelUrl`, `maxResults` | lista de videos com todas as metricas |

**Thumbnails do YouTube:** o YouTube disponibiliza thumbnails em URLs publicas (`https://i.ytimg.com/vi/{videoId}/hqdefault.jpg`). Testar se carregam sem base64 em HTML local. Se bloquearem, baixar via requests como no Instagram/TikTok.

Custo por execucao: a definir (depende do ator escolhido).

## Compatibilidade por Sistema Operacional

Instalacao da dependencia (unica):
```
pip install requests
```

| OS | Como rodar |
|---|---|
| Windows | `python .claude/skills/youtube-dashboard/scripts/atualizar.py --abrir` |
| macOS | `python3 .claude/skills/youtube-dashboard/scripts/atualizar.py --abrir` |
| Linux | `python3 .claude/skills/youtube-dashboard/scripts/atualizar.py --abrir` |

## Configuracao Necessaria

| Chave | Onde fica | Como obter |
|---|---|---|
| `APIFY_API_TOKEN` | `.env` | console.apify.com > Settings > Integrations > Personal API token |
| `YOUTUBE_CHANNEL` | `.env` | URL do canal ou @handle (ex: `https://www.youtube.com/@meuperfil` ou `@meuperfil`) |

## Dashboard: O Que Mostra

**ESTRUTURA OBRIGATORIA — todas as secoes devem estar presentes, nesta ordem:**

1. **Cabecalho (canal):** avatar em base64 (fallback: inicial do nome), nome do canal, descricao, data de criacao, ultima atualizacao
2. **Visao Geral (KPIs):** inscritos, total de views do canal, engajamento medio (%), total de videos
3. **Evolucao ao Longo do Tempo:** tendencia de inscritos e engajamento medio entre execucoes. So aparece com 2+ snapshots em historico.json.
4. **Desempenho por Duracao:** videos agrupados por faixa (Short ate 60s, curto 1-5min, medio 5-15min, longo 15min+). Media de views, likes, engajamento.
5. **Melhores Dias para Publicar:** heatmap ou grafico de barras por dia da semana. Intensidade = views medias.
6. **Frequencia de Publicacao:** videos por semana vs views. Insight comparando semanas mais ativas.
7. **Top 3 Videos:** os 3 com mais views, com thumbnail em base64, views, likes, comentarios, duracao, taxa de engajamento e link.
8. **Analise de Titulos:** palavras mais frequentes nos videos com mais views (wordcloud ou barras). Insight sobre comprimento ideal de titulo.
9. **Tamanho do Titulo vs Views:** 3 buckets (curto, medio, longo) com views medias por faixa.
10. **Linha do Tempo (graficos):** views, likes, engajamento (%) ao longo do tempo. Canvas puro, tooltip.
11. **Barra de Filtros:** filtros por duracao e periodo (7/15/30 dias). Afeta grade de videos, Top 3 e KPIs.
12. **Todos os Videos (grade):** thumbnail em base64, views, likes, comentarios, duracao, data, titulo truncado e link.

**NUNCA omitir nenhuma dessas 12 secoes.**

## Metricas YouTube (diferente do Instagram e TikTok)

| Metrica | Campo Apify | Observacao |
|---|---|---|
| Views | `viewCount` | Metrica principal no YouTube |
| Likes | `likes` ou `likeCount` | YouTube removeu dislikeCount da API publica |
| Comentarios | `commentCount` ou `commentsCount` | |
| Duracao | `duration` (formato ISO 8601 ou segundos) | Necessario converter PT1H2M3S para segundos |
| Titulo | `title` | |
| Thumbnail | `thumbnailUrl` ou montar de `videoId` | URL publica: `i.ytimg.com/vi/{id}/hqdefault.jpg` |
| Inscritos | `subscriberCount` | No nivel do canal |
| Engajamento YouTube | (likes + comentarios) / views * 100 | Benchmark: acima de 3% e bom |

> **Nota de implementacao:** os nomes exatos dos campos dependem do ator Apify escolhido. Verificar no JSON de retorno antes de codar.

## Fluxo

### PASSO -1. Verificar Plataforma Ativa (OBRIGATORIO — executar antes de qualquer outra coisa)

Leia `.env`. Verifique o valor de `YOUTUBE_ATIVO`.

**Cenario: `YOUTUBE_ATIVO=false` (aluno ja disse que nao tem YouTube)**

```
Voce marcou que nao tem um canal ativo no YouTube.

Quer atualizar essa preferencia?

1. Sim, tenho YouTube agora — configurar o dashboard
2. Nao, pode ignorar
```

Se escolher 1: troque `YOUTUBE_ATIVO=false` por `YOUTUBE_ATIVO=true` no `.env` e continue para o PASSO 0.
Se escolher 2: encerre sem fazer nada.

---

**Cenario: `YOUTUBE_ATIVO` nao existe no `.env` (primeira vez)**

```
Voce tem um canal ativo no YouTube que quer monitorar?

1. Sim, tenho YouTube
2. Nao tenho YouTube
```

Se escolher 1: salve `YOUTUBE_ATIVO=true` no `.env` (Edit cirurgico, adicionar linha). Continue para o PASSO 0.
Se escolher 2: salve `YOUTUBE_ATIVO=false` no `.env`. Encerre com:

```
Tudo bem. Se um dia criar um canal no YouTube, e so chamar essa skill de novo.
```

---

**Cenario: `YOUTUBE_ATIVO=true` (aluno confirmou que tem YouTube)**

Continue direto para o PASSO 0 sem perguntar nada.

---

### PASSO 0. Detectar Estado

Antes de qualquer pergunta, leia em paralelo:
1. `.env` na raiz do projeto — existe `APIFY_API_TOKEN` com valor? existe `YOUTUBE_CHANNEL` com valor?
2. `meus-produtos/{ativo}/entregas/youtube-dashboard/dashboard.html` — o arquivo existe?

---

#### Cenario A. Dashboard ja configurado (dashboard.html existe)

Mostre o menu sem perguntas:

```
Dashboard do YouTube ja esta configurado.

Canal monitorado: {YOUTUBE_CHANNEL do .env}

O que quer fazer?

1. Abrir o dashboard agora
2. Atualizar os dados agora
3. Trocar o canal monitorado
4. Recriar o script do zero
```

---

#### Cenario B. Primeira configuracao

**1. Canal do YouTube**

Prioridade: ler `.env` primeiro (`YOUTUBE_CHANNEL`). Se encontrar, confirme.
Se nao encontrar, pergunte:
```
Qual o endereco do seu canal no YouTube?
(ex: https://www.youtube.com/@meuperfil  ou  @meuperfil)
```

Normalize: aceitar `@handle`, URL completa ou channel ID. Salve com Edit cirurgico no `.env`: `YOUTUBE_CHANNEL=<valor>`.

**2. Token Apify**

Se `APIFY_API_TOKEN` estiver no `.env`: use diretamente, nao pergunte.
Se nao estiver: execute a skill `configurar-apify` e retorne aqui apos concluir.

---

### PASSO 1. Confirmacao

```
Configuracao confirmada:

- Canal YouTube: {YOUTUBE_CHANNEL}
- Token Apify: configurado
- Script: .claude/skills/youtube-dashboard/scripts/atualizar.py
- Dashboard: meus-produtos/{ativo}/entregas/youtube-dashboard/dashboard.html

1. Tudo certo, gerar agora
2. Quero ajustar algo
```

---

### PASSO 2. Executar

```bash
python .claude/skills/youtube-dashboard/scripts/atualizar.py --abrir
```

macOS / Linux: `python3 ...`

Leia o log para confirmar sucesso:
```bash
tail -10 meus-produtos/{ativo}/entregas/youtube-dashboard/log.txt
```

**Erros comuns:**

| Erro no log | Causa | Solucao |
|---|---|---|
| `401` ou autenticacao | Token Apify invalido | Verificar token em console.apify.com |
| `Canal vazio` ou erro | URL errada ou canal sem videos publicos | Confirmar URL do canal |
| Timeout | Ator YouTube lento | Aumentar timeout no script ou rodar novamente |

---

### PASSO 3. Entrega

```
Dashboard criado.

Arquivos:
- Dashboard: meus-produtos/{ativo}/entregas/youtube-dashboard/dashboard.html
- Script:    .claude/skills/youtube-dashboard/scripts/atualizar.py
- Log:       meus-produtos/{ativo}/entregas/youtube-dashboard/log.txt

Para atualizar quando quiser:
python .claude/skills/youtube-dashboard/scripts/atualizar.py --abrir

Canal monitorado: {YOUTUBE_CHANNEL}
```

**Sem agendamento automatico:** o aluno roda o script manualmente.

## Regras

- **Sempre ler `.env` antes de pedir o token Apify ao usuario.**
- O token Apify e o canal ficam no `.env` (`APIFY_API_TOKEN` e `YOUTUBE_CHANNEL`). Nunca hardcodar no script.
- Dashboard em HTML puro. Sem libs externas alem de Google Fonts. Canvas puro para graficos.
- Nao usar travessao em nenhum texto exibido no dashboard.
- Tema claro: fundo #f8fafc, cards brancos, accent vermelho YouTube #ff0000 ou neutro indigo.
- **CRITICO — Thumbnails:** verificar se as URLs publicas do YouTube (`i.ytimg.com`) carregam em HTML local. Se nao, converter para base64.
- **CRITICO — Duracao ISO 8601:** converter `PT1H2M3S` para segundos no script. Exibir no dashboard em formato `1h 2min 3s` ou `HH:MM:SS`.
- **CRITICO — Engajamento no YouTube e calculado sobre views.** Formula: (likes + comentarios) / views * 100. Benchmark: 3-5% e considerado bom.
- **YouTube removeu dislikes da API:** nao tentar coletar ou exibir dislikeCount.

## Proximos Passos Apos Configurar

- `/copy-roteiro` — criar roteiros baseados nos videos com mais views
- `/copy-social` — criar conteudo para outras plataformas baseado nos temas que performam
- `/copy-anuncio` — transformar videos de sucesso em anuncios
