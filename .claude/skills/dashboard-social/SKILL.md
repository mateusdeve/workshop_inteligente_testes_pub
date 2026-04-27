---
name: dashboard-social
description: >
  Porta de entrada unificada para configurar e atualizar os dashboards de
  métricas do Instagram, TikTok e YouTube. Detecta o estado de cada plataforma
  no .env, pergunta quais o aluno usa, coleta os dados necessários uma única vez
  e executa os scripts na sequência. O token Apify é pedido uma só vez e vale
  para todas as plataformas.
---

# Dashboard. Central de Métricas das Redes Sociais

## Quando Usar

- Quando o aluno quiser configurar o monitoramento de uma ou mais redes sociais de uma vez.
- Quando quiser ver o estado geral de todos os dashboards configurados.
- Quando quiser atualizar os dados de múltiplas plataformas em sequência.

**Alternativa:** cada plataforma também pode ser configurada individualmente pelas skills `instagram-dashboard`, `tiktok-dashboard` e `youtube-dashboard`.

---

## PASSO 0. Detectar Estado Atual (OBRIGATÓRIO — executar antes de qualquer outra coisa)

Leia em paralelo:
1. `.env` na raiz do projeto
2. Existência dos arquivos `dashboard.html` de cada plataforma no produto ativo

Monte a tabela de estado interna para uso nos próximos passos:

| Plataforma | Flag no .env | Username/Canal | dashboard.html existe? | Estado |
|---|---|---|---|---|
| Instagram | `INSTAGRAM_ATIVO` | `IG_USER` | `meus-produtos/{ativo}/entregas/instagram-dashboard/dashboard.html` | — |
| TikTok | `TIKTOK_ATIVO` | `TIKTOK_USER` | `meus-produtos/{ativo}/entregas/tiktok-dashboard/dashboard.html` | — |
| YouTube | `YOUTUBE_ATIVO` | `YOUTUBE_CHANNEL` | `meus-produtos/{ativo}/entregas/youtube-dashboard/dashboard.html` | — |

**Regras de estado por plataforma:**

- `CONFIGURADO` — flag=`true`, username preenchido, dashboard.html existe
- `PENDENTE` — flag=`true` ou ausente, mas falta username ou dashboard.html
- `INATIVO` — flag=`false` (aluno disse que não usa)

---

## PASSO 1. Exibir Status e Perguntar o Que Fazer

Exiba o painel de status:

```
Central de Dashboards

Instagram:  [CONFIGURADO @{IG_USER}]   ou   [PENDENTE — falta configurar]   ou   [INATIVO]
TikTok:     [CONFIGURADO @{TIKTOK_USER}]   ou   [PENDENTE — falta configurar]   ou   [INATIVO]
YouTube:    [CONFIGURADO {YOUTUBE_CHANNEL}]   ou   [PENDENTE — falta configurar]   ou   [INATIVO]

O que quer fazer?

1. Atualizar todos os dados agora (só executa os CONFIGURADOS)
2. Configurar uma plataforma que ainda está pendente
3. Adicionar uma nova plataforma
4. Abrir um dashboard específico
5. Ver o que cada dashboard mostra
```

**Regra de simplificação:** se todas as 3 plataformas estiverem CONFIGURADAS, exibir só as opções 1, 4 e 5 (sem opções 2 e 3, que não fazem sentido).

**Regra de simplificação:** se nenhuma plataforma estiver configurada (todas PENDENTES ou INATIVAS), pular direto para o fluxo de onboarding do PASSO 2, sem mostrar o menu acima.

---

## Opção 1. Atualizar Todos os Dados

Para cada plataforma com estado CONFIGURADO (na ordem Instagram → TikTok → YouTube):

```
Atualizando Instagram (@{IG_USER})...
```

Execute o script correspondente e aguarde:

```bash
python .claude/skills/instagram-dashboard/scripts/atualizar.py
```

Leia as últimas 5 linhas do log para confirmar sucesso ou erro.

Após concluir a plataforma, mostre o resultado e siga para a próxima:

```
Instagram: atualizado. Engajamento médio: {X}%
TikTok: atualizando...
```

Ao final, mostre o resumo:

```
Atualização concluída.

Instagram:  atualizado   /   erro: {mensagem}
TikTok:     atualizado   /   erro: {mensagem}
YouTube:    atualizado   /   erro: {mensagem}

Para abrir um dashboard:
python .claude/skills/instagram-dashboard/scripts/atualizar.py --abrir
```

---

## Opção 2. Configurar Plataforma Pendente

Liste as plataformas com estado PENDENTE:

```
Plataformas ainda não configuradas:

1. Instagram
2. TikTok
3. YouTube

Qual quer configurar?
```

Após a escolha, siga o fluxo da skill específica a partir do PASSO 0 (Cenário B):
- Instagram: skill `instagram-dashboard`
- TikTok: skill `tiktok-dashboard`
- YouTube: skill `youtube-dashboard`

**Regra de token:** se `APIFY_API_TOKEN` já estiver no `.env`, não perguntar. Usar diretamente.

---

## Opção 3. Adicionar Nova Plataforma

```
Qual plataforma quer adicionar?

1. Instagram
2. TikTok
3. YouTube
```

Após a escolha:

1. Se a flag estiver como `false` no `.env`, pergunte:

```
Você marcou anteriormente que não usa {plataforma}.

Quer ativar agora?

1. Sim, tenho {plataforma} agora
2. Não, cancelar
```

Se confirmar: atualize a flag para `true` no `.env` (Edit cirúrgico).

2. Siga o fluxo de primeira configuração da skill correspondente (Cenário B).

**Regra de token:** se `APIFY_API_TOKEN` já estiver no `.env`, não perguntar.

---

## Opção 4. Abrir Dashboard Específico

```
Qual dashboard quer abrir?

1. Instagram (@{IG_USER})
2. TikTok (@{TIKTOK_USER})
3. YouTube ({YOUTUBE_CHANNEL})
```

Execute o comando de abertura para o sistema operacional detectado:

| OS | Comando |
|---|---|
| Windows | `start meus-produtos/{ativo}/entregas/{plataforma}-dashboard/dashboard.html` |
| macOS | `open meus-produtos/{ativo}/entregas/{plataforma}-dashboard/dashboard.html` |
| Linux | `xdg-open meus-produtos/{ativo}/entregas/{plataforma}-dashboard/dashboard.html` |

---

## Opção 5. Ver o Que Cada Dashboard Mostra

Exibir tabela resumida:

```
O que cada dashboard mostra:

INSTAGRAM
  Seguidores, engajamento médio, formato mais postado
  Desempenho por formato (Reel, Carrossel, Foto)
  Heatmap de melhores horários para postar
  Top 3 posts, análise de hashtags, linha do tempo, grade completa de posts

TIKTOK
  Seguidores, likes totais, engajamento médio por views
  Desempenho por duração do vídeo (até 15s, 16-30s, 31-60s, 60s+)
  Heatmap de melhores horários para postar
  Top 3 vídeos, análise de hashtags, linha do tempo, grade completa de vídeos

YOUTUBE
  Inscritos, total de views do canal, engajamento médio
  Desempenho por duração (Shorts, curto, médio, longo)
  Melhores dias para publicar
  Top 3 vídeos, análise de títulos, linha do tempo, grade completa de vídeos

Todos os dashboards abrem direto no navegador, funcionam offline e têm filtros interativos.
```

---

## Fluxo de Onboarding (Primeira Vez — Nenhuma Plataforma Configurada)

Quando nenhuma plataforma está configurada, execute este fluxo antes de qualquer outra coisa:

### Pergunta 1. Quais redes sociais o aluno usa?

```
Vamos configurar o monitoramento das suas redes sociais.

Quais você usa ativamente? (pode marcar mais de uma)

1. Instagram
2. TikTok
3. YouTube
4. Nenhuma dessas por enquanto

Digite os números separados por vírgula (ex: 1,3) ou o número único:
```

Se escolher 4: salve `INSTAGRAM_ATIVO=false`, `TIKTOK_ATIVO=false`, `YOUTUBE_ATIVO=false` no `.env` e encerre com:

```
Tudo bem. Quando quiser monitorar uma rede social, é só chamar esse comando de novo.
```

Para cada plataforma NÃO selecionada: salve a flag como `false` no `.env` (Edit cirúrgico). Isso evita que as skills individuais perguntem de novo no futuro.

Para cada plataforma selecionada: salve a flag como `true` no `.env`.

### Pergunta 2. Coletar usernames das plataformas selecionadas

Para cada plataforma selecionada, UMA pergunta por vez:

**Instagram:**
```
Qual o usuário do seu perfil no Instagram? (só o nome, sem o arroba)
(ex: meuperfil)
```
Normalize: sem @, lowercase. Salve `IG_USER=<username>` no `.env`.

**TikTok:**
```
Qual o usuário do seu perfil no TikTok? (só o nome, sem o arroba)
(ex: meuperfil)
```
Normalize: sem @, lowercase. Salve `TIKTOK_USER=<username>` no `.env`.

**YouTube:**
```
Qual o endereço do seu canal no YouTube?
(ex: @meuperfil  ou  https://www.youtube.com/@meuperfil)
```
Aceitar `@handle`, URL completa ou channel ID. Salve `YOUTUBE_CHANNEL=<valor>` no `.env`.

### Pergunta 3. Token Apify (UMA VEZ para todas)

Se `APIFY_API_TOKEN` já estiver no `.env`: usar diretamente, não perguntar.

Se não estiver: execute a skill `configurar-apify` e retorne aqui após concluir. O token configurado vale para Instagram, TikTok e YouTube — não perguntar de novo para cada um.

### Confirmação Única

```
Configuração confirmada:

{se Instagram selecionado}
- Instagram: @{IG_USER}
{/se}
{se TikTok selecionado}
- TikTok: @{TIKTOK_USER}
{/se}
{se YouTube selecionado}
- YouTube: {YOUTUBE_CHANNEL}
{/se}
- Token Apify: configurado

Custo estimado por atualização completa: menos de US$ 0,60 no plano gratuito do Apify.

1. Tudo certo, gerar os dashboards agora
2. Quero ajustar algo
```

### Execução em Sequência

Para cada plataforma selecionada (ordem: Instagram → TikTok → YouTube):

```
Gerando dashboard do Instagram (@{IG_USER})...
Isso pode levar até 10 minutos (busca expandida de posts).
```

Execute o script:
```bash
python .claude/skills/instagram-dashboard/scripts/atualizar.py
```
(macOS/Linux: `python3 ...`)

Leia as últimas 5 linhas do log para confirmar sucesso. Informe o resultado e siga para a próxima plataforma.

### Entrega Final

```
Dashboards criados.

{para cada plataforma configurada com sucesso}
{Plataforma}: meus-produtos/{ativo}/entregas/{plataforma}-dashboard/dashboard.html
{/para}

Para atualizar os dados quando quiser:
- Instagram: python .claude/skills/instagram-dashboard/scripts/atualizar.py --abrir
- TikTok:    python .claude/skills/tiktok-dashboard/scripts/atualizar.py --abrir
- YouTube:   python .claude/skills/youtube-dashboard/scripts/atualizar.py --abrir

Ou chame este comando de novo para atualizar tudo de uma vez.
```

### Passo Pós-Entrega. Oferecer Plataformas Adicionais

Após exibir a Entrega Final, verifique no `.env` se há plataformas com flag `false` (INATIVAS).

**Pule este passo se:** todas as 3 plataformas estão CONFIGURADAS, ou o aluno escolheu "Nenhuma" na pergunta inicial (todas as 3 com `false` ao mesmo tempo — não faz sentido oferecer de novo).

**Se há 2 plataformas INATIVAS** (ex: aluno configurou só o Instagram):

```
Quer aproveitar e adicionar as outras redes sociais também?
O token Apify já está pronto, é só informar o usuário.

1. Configurar TikTok
2. Configurar YouTube
3. Configurar os dois em sequência
4. Depois, por enquanto está bom
```

**Se há 1 plataforma INATIVA:**

```
Quer configurar {plataforma} também?
O token Apify já está pronto, é só informar o usuário.

1. Sim
2. Depois
```

Se o aluno aceitar:
1. Coletar o username da(s) plataforma(s) escolhida(s), UMA pergunta por vez
2. Atualizar a flag de `false` para `true` no `.env` (Edit cirúrgico)
3. Executar o script correspondente na ordem TikTok → YouTube
4. Exibir o caminho do dashboard gerado ao final de cada um

**Regras do passo pós-entrega:**
- `APIFY_API_TOKEN` já está configurado. Nunca perguntar de novo.
- Se o aluno escolher "Depois" (opção 4 ou 2), encerrar normalmente sem alterar as flags.
- Não executar este passo quando o comando for chamado para "Atualizar todos" (Opção 1 do menu principal) — só no fluxo de onboarding.

---

## Regras

- **Sempre ler `.env` antes de pedir qualquer dado ao usuário.** Se `APIFY_API_TOKEN`, `IG_USER`, `TIKTOK_USER` ou `YOUTUBE_CHANNEL` já estiverem presentes, usar diretamente.
- **Token Apify é pedido uma única vez** mesmo quando múltiplas plataformas estão sendo configuradas.
- **Flags de plataforma inativa (`false`) nunca devem ser sobrescritas automaticamente.** Sempre perguntar antes de reativar.
- **Não executar scripts de plataformas com estado INATIVO** mesmo na opção de "atualizar tudo".
- **Ordem de execução sempre:** Instagram → TikTok → YouTube. Mais lento primeiro para o aluno ver progresso.
- **Sem agendamento automático:** não configurar CronCreate nem schtasks. O aluno roda manualmente.
- **Não usar travessão** em nenhum texto exibido ao usuário.

## Próximos Passos Após Configurar

- `/copy-variacao-post` — criar variações dos posts do Instagram com mais engajamento
- `/copy-social` — criar conteúdo baseado nos vídeos do TikTok que performaram melhor
- `/copy-roteiro` — criar roteiros baseados nos vídeos do YouTube com mais views
- `/dados-instagram` — análise profunda de um perfil concorrente no Instagram
