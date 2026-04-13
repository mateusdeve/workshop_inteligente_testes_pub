---
name: workshop-marketing:img-anuncio
description: Gerar imagens prontas para anuncios usando IA. pesquisa referencias virais do Instagram, cria prompts otimizados e gera as imagens automaticamente via OpenRouter. Inclui setup guiado da API.
---

# Imagem para Anuncio. Gerador de Criativos com IA

Gera imagens prontas para usar em anuncios do Instagram e Facebook. Pesquisa referencias virais antes de criar, gera prompts otimizados e produz as imagens automaticamente via API.

## Usage

```
/img-anuncio
```

## O Que Fazer

### 0. Contexto e Verificacao de API

**Ler contexto do produto:**
Leia `entregas/.ativo`, depois `entregas/{ativo}/perfil.md` e `entregas/{ativo}/idconsumidor.md` (se existir).

**Verificar API de geracao de imagem:**

Leia o arquivo `.env` e verifique as chaves nesta ordem:

1. `OPENROUTER_API_KEY`. se existir e nao estiver vazia, API pronta
2. `FREEPIK_API_KEY`. se existir e nao estiver vazia, API pronta (fallback)
3. Nenhuma chave configurada

**Se nenhuma API estiver configurada**, mostre:

```
Para gerar imagens automaticamente, voce precisa conectar uma API de geracao de imagem.

Eu recomendo o OpenRouter. custa menos de R$ 0,10 por imagem e tem os melhores modelos.

Quer que eu te guie na configuracao agora?

1. Sim, me guie passo a passo (5 minutos)
2. Prefiro so gerar os prompts (sem API, uso manual)
```

Se escolher 1: exiba um resumo dos passos principais do guia `docs/setup-imagens.md` de forma conversacional, orientando o usuario a:
- Criar conta no openrouter.ai
- Adicionar creditos (minimo US$ 5)
- Gerar a chave de API (openrouter.ai/settings/keys)
- Colar no arquivo `.env` na linha `OPENROUTER_API_KEY=`
- Informar que o guia completo esta em `docs/setup-imagens.md`

Apos o usuario informar que configurou, verifique lendo o `.env` novamente. Se a chave estiver la, confirme: "Conexao configurada. Vamos criar suas imagens." e siga para o passo 1.

Se escolher 2: siga o fluxo normalmente, mas ao inves de gerar imagens via API, salve apenas os prompts para uso manual.

### 1. Pesquisa de Referencias Virais

**OBRIGATORIO antes de criar qualquer imagem.**

Faca 2 buscas na web (WebSearch):

**Busca 1. Formatos virais atuais:**
```
"Instagram static ad formats high converting [mes/ano atual]"
```

**Busca 2. Referencia no nicho do produto:**
```
"Instagram ad examples [nicho do produto] [ano atual]"
```

A partir dos resultados, extraia:
- 3-5 formatos visuais que estao funcionando agora
- Padroes de composicao (cores, layout, tipografia)
- Elementos que param o scroll

Consulte tambem a referencia interna em `.claude/plugins/workshop-marketing/skills/anuncios/references/formatos-virais-instagram.md` para cruzar com os dados da pesquisa.

**Apresente ao usuario:**

```
Pesquisei as tendencias de anuncios visuais no Instagram agora.

Os formatos que mais estao convertendo no seu nicho:

1. [Formato A]. [descricao curta do por que funciona]
2. [Formato B]. [descricao curta]
3. [Formato C]. [descricao curta]

Vou usar essas referencias para criar suas imagens.

--- Pesquisa concluida ---
Proximo: Escolher o objetivo do anuncio
---
```

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4. Objetivo:**

```
Qual o objetivo desse anuncio?

1. Atrair atenção (awareness. fazer a pessoa parar e ler)
2. Gerar clique (trafego. levar para pagina ou perfil)
3. Vender direto (conversao. levar para checkout)

Digite o numero:
```

```
--- Bloco 1/4 concluido ---
Objetivo: [objetivo escolhido]
Proximo: Formato da imagem
---
```

**Bloco 2/4. Formato:**

```
Qual formato de imagem?

1. Feed retrato (1080x1350). ocupa mais espaco na tela, melhor para feed
2. Stories/Reels (1080x1920). tela cheia vertical
3. Quadrado (1080x1080). classico, funciona em tudo
4. Carrossel (1080x1080 x 3-5 slides)

Digite o numero:
```

```
--- Bloco 2/4 concluido ---
Objetivo: [objetivo]
Formato: [formato escolhido]
Proximo: Estilo visual
---
```

**Bloco 3/4. Estilo visual:**

Baseado nas referencias encontradas na pesquisa, oferecer opcoes contextualizadas:

```
Qual estilo visual? (baseado nas tendencias que encontrei)

1. [Formato viral A da pesquisa]. [descricao]
2. [Formato viral B da pesquisa]. [descricao]
3. [Formato viral C da pesquisa]. [descricao]
4. Outro (descreva o que tem em mente)

Digite o numero:
```

```
--- Bloco 3/4 concluido ---
Objetivo: [objetivo]
Formato: [formato]
Estilo: [estilo escolhido]
Proximo: Texto na imagem
---
```

**Bloco 4/4. Texto e CTA:**

```
Que texto deve aparecer na imagem?

Opcoes:
1. Headline do meu produto (vou sugerir 3 opcoes baseadas no seu perfil)
2. Dado/numero de impacto (ex: "97% dos alunos aprovaram")
3. Pergunta provocadora (ex: "Voce sabia que...")
4. Sem texto (so imagem)
5. Quero escrever meu proprio texto

Digite o numero:
```

Se escolher 1: gere 3 opcoes de headline baseadas no Quadro, Furadeira e Urgencias Ocultas do perfil. Apresente para o usuario escolher.

Se escolher 5: pergunte qual texto.

Depois, pergunte o CTA (se aplicavel):

```
Qual CTA (chamada para acao)?

1. Saiba mais
2. Garanta sua vaga
3. Acesse agora
4. Sem CTA na imagem
5. Outro (escreva)

Digite o numero:
```

```
--- Bloco 4/4 concluido ---
Objetivo: [objetivo]
Formato: [formato]
Estilo: [estilo]
Texto: [texto]
CTA: [cta]
---
```

### 3. Confirmacao

```
Resumo do que vou criar:

- Objetivo: [objetivo]
- Formato: [formato e dimensoes]
- Estilo: [estilo visual com referencia viral]
- Texto na imagem: [texto]
- CTA: [cta]
- Quantidade: 3 variacoes
- API: [OpenRouter/Freepik/Manual]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 4. Geracao de Prompts

Para cada variacao, crie um prompt seguindo esta estrutura:

**Estrutura do prompt (em ingles, otimizado para o modelo):**

```
[Descricao da cena/composicao], [estilo visual], [elementos especificos],
[paleta de cores], [mood/atmosfera], [detalhes tecnicos].
Text overlay: "[texto exato]". [formato e proporcao].
Professional advertising photography, high resolution, clean composition.
```

**Regras para prompts de anuncio:**
- Sempre em ingles (melhor resultado nos modelos)
- Descrever composicao antes de detalhes
- Incluir "professional advertising" ou "marketing material" no prompt
- Especificar proporcao e resolucao
- Nao pedir rostos realistas de pessoas (usar silhuetas, maos, cenarios)
- Incluir texto overlay como instrucao separada

**Gere 3 variacoes** com abordagens visuais diferentes:
- Variacao 1: Mais alinhada com a referencia viral principal
- Variacao 2: Mais alinhada com a identidade do produto
- Variacao 3: Mais ousada/diferente (teste criativo)

**Mostre os 3 prompts ao usuario:**

```
Variacao 1. [nome descritivo]:
[prompt em ingles]
Conceito: [explicacao em portugues do que a imagem vai mostrar]

Variacao 2. [nome descritivo]:
[prompt em ingles]
Conceito: [explicacao em portugues]

Variacao 3. [nome descritivo]:
[prompt em ingles]
Conceito: [explicacao em portugues]

---
1. Aprovar e gerar as 3 imagens
2. Gerar so a variacao [numero]
3. Quero ajustar os prompts
```

### 5. Geracao das Imagens via API

**Mapeamento de tamanho por formato escolhido:**
- Feed retrato (1080x1350) → `1024x1024` (API nao suporta 4:5 exato. sera a melhor aproximacao)
- Stories/Reels (1080x1920) → `1024x1792`
- Quadrado (1080x1080) → `1024x1024`
- Carrossel → `1024x1024`

**Se OPENROUTER_API_KEY disponivel:**

Leia o modelo definido em `OPENROUTER_IMAGE_MODEL` no `.env` (padrao: `black-forest-labs/flux-schnell`).

Para cada prompt aprovado, execute:

```bash
curl -s -X POST "https://openrouter.ai/api/v1/images/generations" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"$OPENROUTER_IMAGE_MODEL\", \"prompt\": \"PROMPT_AQUI\", \"size\": \"TAMANHO_AQUI\", \"n\": 1}"
```

Da resposta, extraia o campo `data[0].url` ou `data[0].b64_json`.

Se for URL: baixe a imagem com `curl -s -o "CAMINHO_ARQUIVO" "URL_IMAGEM"`.
Se for b64_json: decodifique e salve com `echo "BASE64" | base64 -d > "CAMINHO_ARQUIVO"`.

Salve em: `entregas/{ativo}/criativos/img-anuncio-v[N]-{produto}.png`

**Se FREEPIK_API_KEY disponivel (e nao tiver OpenRouter):**

```bash
curl -s -X POST "https://api.freepik.com/v1/ai/text-to-image" \
  -H "x-freepik-api-key: $FREEPIK_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"PROMPT_AQUI\", \"num_images\": 1, \"image\": {\"size\": \"square_1_1\"}}"
```

Mapeamento de tamanho Freepik:
- Quadrado/Feed → `square_1_1`
- Stories/Reels → `portrait_9_16`
- Banner → `landscape_16_9`

Salve em: `entregas/{ativo}/criativos/img-anuncio-v[N]-{produto}.png`

**Se nenhuma API configurada:**

Salve apenas os prompts em `entregas/{ativo}/criativos/prompts-anuncio-{produto}.md` e informe:

```
Prompts salvos em entregas/{ativo}/criativos/prompts-anuncio-{produto}.md

Copie e cole em qualquer gerador de imagem:
- Leonardo.ai (gratuito)
- Midjourney (Discord)
- Freepik AI (freepik.com)
- ChatGPT com DALL-E

Para gerar automaticamente na proxima vez, configure sua API:
Veja o guia em docs/setup-imagens.md
```

### 6. Entrega e Proximo Passo

Apos gerar e salvar as imagens:

```
Imagens geradas e salvas:

- entregas/{ativo}/criativos/img-anuncio-v1-{produto}.png
- entregas/{ativo}/criativos/img-anuncio-v2-{produto}.png
- entregas/{ativo}/criativos/img-anuncio-v3-{produto}.png

Briefing criativo salvo em:
- entregas/{ativo}/criativos/briefing-anuncio-{produto}.md

Proximo passo: Use `/copy-anuncio` para criar a copy (texto) dos anuncios
que vao acompanhar essas imagens.
```

Salve tambem um arquivo de briefing (`briefing-anuncio-{produto}.md`) contendo:
- Referencias virais usadas como inspiracao
- Prompts utilizados
- Formato e dimensoes
- Objetivo do anuncio
- Estilo visual e paleta de cores
- Texto overlay e CTA
- Caminhos das imagens geradas

### 7. Modo Iterativo

Se o usuario quiser ajustar uma imagem especifica:

```
Qual imagem quer refinar?

1. Variacao 1. [nome]
2. Variacao 2. [nome]
3. Variacao 3. [nome]

O que quer mudar?
(ex: "mais colorido", "trocar o texto", "fundo mais escuro", "estilo diferente")
```

Ajuste o prompt e regere apenas a imagem solicitada.
