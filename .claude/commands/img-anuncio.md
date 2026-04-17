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
Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md` (se existir).

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

### 5. Geracao Hibrida de Criativos (IA + HTML + Screenshot)

O sistema usa abordagem hibrida em 3 camadas:
1. **IA gera o visual de fundo** (foto, textura, ilustracao) via OpenRouter
2. **Template HTML compoe** texto + layout + cores por cima
3. **Chrome/Edge headless exporta** PNG final

Isso funciona para qualquer formato (carrossel, estatico, stories) e qualquer produto.

**REGRA ABSOLUTA:** Todo JSON de config DEVE ter textos em portugues com acentos corretos (UTF-8). "não", "padrão", "você", "mês", "saída", "número". Nunca "nao", "padrao", "voce". Os prompts de IA (em ingles) nao precisam de acentos.

#### Router inteligente de modelos

O router (`scripts/openrouter_model_router.py`) analisa cada prompt e escolhe o melhor modelo:

| Categoria | Modelo escolhido | Quando usar |
|---|---|---|
| photorealistic | Flux 2 Pro (`black-forest-labs/flux.2-pro`) | Fotos reais, retratos, produtos |
| complex_scene | GPT-5 Image Mini (`openai/gpt-5-image-mini`) | Composicoes complexas, mockups, marketing |
| infographic | GPT-5 Image Mini (`openai/gpt-5-image-mini`) | Infograficos, dashboards, comparativos |
| clean_minimal | Gemini 3.1 Flash (`google/gemini-3.1-flash-image-preview`) | Backgrounds, texturas, CTAs |
| abstract_mood | Gemini 3.1 Flash (`google/gemini-3.1-flash-image-preview`) | Gradientes, vidro, 3D |
| artistic | Flux 2 Flex (`black-forest-labs/flux.2-flex`) | Arte digital, colagens, estilos ousados |

#### Como usar

Gerar um arquivo JSON de config com os slides (o assistente gera automaticamente apos aprovacao da copy). Depois rodar:

```bash
py -3 scripts/generate-creative.py --config meus-produtos/{ativo}/entregas/anuncios/{arquivo}.json --dry-run
py -3 scripts/generate-creative.py --config meus-produtos/{ativo}/entregas/anuncios/{arquivo}.json
py -3 scripts/generate-creative.py --config meus-produtos/{ativo}/entregas/anuncios/{arquivo}.json --force-model google/gemini-3.1-flash-image-preview
py -3 scripts/generate-creative.py --config meus-produtos/{ativo}/entregas/anuncios/{arquivo}.json --skip-ai
```

Compativel com Windows (Edge/Chrome), Mac (Chrome/Edge) e Linux (Chrome/Chromium).

#### Cores customizaveis por produto

No JSON, use `theme-custom` e defina cores no campo `colors`:

```json
{
  "colors": {"bg": "#0f7937", "text": "#ffffff", "accent": "#fbbf24"},
  "slides": [
    {"theme": "theme-custom", "layout": "layout-gancho", "headline": "..."}
  ]
}
```

Temas prontos disponiveis: `theme-dark`, `theme-light`, `theme-blue`, `theme-green`, `theme-warm`, `theme-red-soft`, `theme-green-soft`, `theme-custom`.

#### Layouts disponiveis

| Layout | Uso |
|---|---|
| `layout-gancho` | Slide de abertura, headline grande |
| `layout-conteudo` | Headline + corpo de texto |
| `layout-dado` | Numero em destaque + headline |
| `layout-checklist` | Lista com checkboxes |
| `layout-comparacao` | Dois blocos lado a lado (certo vs errado) |
| `layout-cta` | Call to action final |

**Para usar o router em outros scripts:**

```python
from openrouter_model_router import route_model, classify_prompt

# Retorna o model_id ideal
model_id = route_model("photorealistic portrait of a woman")
# → "black-forest-labs/flux.2-pro"

# Retorna classificacao completa
result = classify_prompt("minimalist infographic with icons")
# → {"category": "infographic", "confidence": 0.6, "model_id": "google/gemini-3.1-flash-image-preview", ...}
```

### 6. Entrega e Proximo Passo

Apos gerar e salvar as imagens:

```
Imagens geradas e salvas:

- meus-produtos/{ativo}/entregas/criativos/img-anuncio-v1-{produto}.png
- meus-produtos/{ativo}/entregas/criativos/img-anuncio-v2-{produto}.png
- meus-produtos/{ativo}/entregas/criativos/img-anuncio-v3-{produto}.png

Briefing criativo salvo em:
- meus-produtos/{ativo}/entregas/criativos/briefing-anuncio-{produto}.md

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
