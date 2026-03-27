---
name: workshop-marketing:anuncio
description: Criar pacotes completos de anúncios para Meta Ads e Google Ads usando a Mandala de 18 Tipos de Anúncios da metodologia VTSD. Inclui copy, direção criativa e estratégia de campanha.
---

# Anúncio — Mandala de 18 Tipos (VTSD)

Cria pacotes de anúncios usando os 18 tipos da Mandala VTSD + estrutura de campanha.

## Usage

```
/anuncio
```

## O Que Fazer

### 1. Contexto

Leia `produtos/{ativo}/perfil.md` e `produtos/{ativo}/idconsumidor.md` se existir.

**Extraia e liste internamente (não precisa mostrar ao usuário):**
- Todos os **Decorados** do perfil — esses são os benefícios que podem virar tema central de anúncio
- Todas as **Urgências Ocultas** (dores, desejos, dúvidas, assuntos relacionados) — essas são os ângulos de entrada de cada anúncio

**Verifique o histórico:** leia todos os arquivos em `produtos/{ativo}/entregas/anuncios/`. Identifique quais urgências ocultas e decorados já foram explorados nos anúncios anteriores.

**Regra de não repetição:** nas novas variações, priorize urgências ocultas e decorados ainda não usados. Se todos já foram usados, escolha os de maior potencial e anote que está retomando esse tema.

Apresente ao usuário (antes de perguntar sobre a campanha):
```
Temos [X] decorados e [Y] urgências ocultas no perfil.
Já explorados em anúncios anteriores: [lista resumida]
Disponíveis para este pacote: [lista resumida dos ainda não usados]
```

Se não houver anúncios anteriores: "É o primeiro pacote de anúncios — vamos usar as urgências e decorados mais relevantes para a fase escolhida."

### 2. Entrevista

**REGRA ABSOLUTA: fazer UMA pergunta por vez. Esperar a resposta antes de fazer a próxima. Nunca agrupar perguntas.**

**Bloco 1 — Tipo de campanha:**
```
Perpétuo ou pico de vendas?

1. Perpétuo
2. Pico de vendas

Digite o número:
```

---

**Se Perpétuo — perguntar em sequência (uma por vez):**

```
Qual o objetivo dos anúncios?

1. Descoberta — atrair novas pessoas que ainda não conhecem o produto
2. Relacionamento — criar conexão e autoridade com quem já segue
3. Conversão — vender
4. RMKT — converter quem já viu a página de vendas

Digite o número:
```

```
Qual o momento de consumo do público?

1. Prontidão — está pronto para comprar
2. Urgência Oculta — tem o problema, mas ainda não busca solução
3. Oportunidade — público amplo, ainda não está pronto para comprar

Digite o número:
```

```
Qual o tipo de anúncio?

1. Imagem estática
2. Vídeo
3. Carrossel
4. Stories

Digite o número:
```

---

**Se Pico de Vendas — perguntar fase:**

```
Qual fase do pico de vendas?

1. Captura
2. Aquecimento
3. Lembrete
4. Venda
5. Remarketing

Digite o número:
```

**Se Captura ou Aquecimento — perguntar em sequência (uma por vez):**

```
Qual o nome do evento?
(ex: "Workshop Tarô Desperto", "Semana da Leitura Segura")
```

```
Qual a promessa do evento?
(ex: "Aprender a fazer sua primeira tiragem completa em 3 dias")
```

```
Qual a data do evento?
(ex: "dia 15 de abril")
```

**Se Venda ou Remarketing — perguntar:**

```
Qual é a oferta?
(ex: "Curso Tarô em Duas Pontes por R$ 497 com bônus exclusivo até domingo")
```

---

**Confirmação antes de gerar (para qualquer caminho):**
```
Resumo do que vou criar:
- Tipo: [perpétuo ou pico de vendas]
- Objetivo/Fase: [objetivo ou fase]
- Momento: [momento de consumo, se perpétuo]
- Formato: [tipo de anúncio — se vídeo: "Vídeo (duração definida após pesquisa de tendências)"]
- [dados do evento ou oferta, se aplicável]
- Quantidade: 3 variações com tipos diferentes da Mandala da Criatividade

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

**REGRA:** nunca indicar duração do vídeo no resumo de confirmação. A duração é calibrada na pesquisa de tendências (Passo 3) e definida apenas na geração.

### 3. Pesquisa de Tendências (OBRIGATÓRIO antes de gerar — qualquer formato)

**Antes de escrever qualquer anúncio**, faça obrigatoriamente as seguintes buscas — independentemente do formato escolhido (vídeo, imagem, carrossel ou texto):

#### Busca Base — SEMPRE obrigatória (todos os formatos)

Pesquise os dois canais obrigatoriamente:
- `reels instagram virais [mês e ano atual]` — todos os nichos
- `tiktok trends virais [mês e ano atual]` — todos os nichos

**REGRA ABSOLUTA:** Pesquisar virais de **todos os nichos** (não apenas o nicho do produto). O objetivo é captar o padrão de estrutura, tom e formato que está funcionando agora na plataforma — não o conteúdo em si. O conteúdo (o que diz) vem do produto e das urgências ocultas. O formato e o estilo (como diz) vêm dos virais encontrados.

O que extrair dessa busca base:
- **Estrutura de abertura**: o que está parando o scroll nos primeiros 2–3 segundos (afirmação contra-intuitiva, dado específico, paradoxo, revelação)
- **Tom predominante no momento**: didático, emocional, provocativo, informal, confissão, polêmica suave
- **O que os virais entregam**: conteúdo real dentro do próprio post/vídeo, ou apenas teasers que prometem sem entregar — **modelar sempre os que entregam conteúdo real**
- **Padrão de CTA**: o que está gerando ação agora (salva, comenta, segue, marca alguém, clica)

---

#### Busca Complementar — Por formato

**Se Vídeo**, pesquise adicionalmente:
- `estrutura roteiro viral reels tiktok [mês e ano atual]`

O que extrair:
- **Duração predominante** dos vídeos com mais alcance (7s, 15s, 30s, 45s, 60s) — usar duração similar
- **Estilo de edição**: cortes rápidos, talking head estático, câmera na mão, B-roll, texto animado
- **Se o vídeo entrega conteúdo real ou apenas teaser** — modelar o que entrega conteúdo real

**Se Imagem estática**, pesquise:
- `posts imagem instagram viral engajamento [mês e ano atual]`
- `trending static image ads instagram [mês e ano atual]`

O que extrair:
- **Estilo visual predominante**: fundo clean, foto real, mockup, texto sobre imagem, collage
- **Uso de texto na imagem**: headline grande, subtítulo, bullets, nenhum texto
- **Proporção que performa mais**: quadrado (1:1), retrato (4:5), stories (9:16)
- **Paleta e estética** dos posts com mais engajamento (minimalista, colorido, escuro, orgânico)
- **Tipo de gancho visual**: o elemento que para o scroll (rosto, número, contraste, cor, palavra)

**Se Carrossel**, pesquise:
- `carrossel instagram viral [mês e ano atual]`
- `trending carousel instagram formato [mês e ano atual]`

O que extrair:
- **Estrutura de slides**: quantos slides, como começa, como termina (cliffhanger, CTA, revelação)
- **Estilo do primeiro slide**: é o gancho — texto grande, pergunta visual, dado, afirmação
- **Progressão**: cada slide avança a narrativa ou repete o mesmo ponto?
- **Uso de continuidade visual**: seta, borda cortada, elemento que "puxa" para o próximo slide
- **CTA do último slide**: o que está funcionando (salva, comenta uma palavra, segue)

---

#### Busca 2 — Por objetivo

**Se Descoberta**, pesquise:
- `como ganhar seguidores instagram organico [mês e ano atual]`
- `conteudo que vira seguidor instagram [mês e ano atual]`

O que extrair:
- **Que tipo de gancho atrai seguidor novo** (não quem já segue — quem nunca viu o perfil)
- **Tema do conteúdo que mais converte em follow**: curiosidade, utilidade, identidade, polêmica leve
- **Tom que faz o estranho confiar rápido**: autoridade discreta, autenticidade, resultado visível
- **CTA que converte em seguidor**: "me segue", "salva para não perder", "ativa o sino"

**Se Relacionamento**, pesquise:
- `conteudo que gera comentarios instagram [mês e ano atual]`
- `posts mais compartilhados instagram [mês e ano atual]`

O que extrair:
- **O que faz a pessoa comentar** (identificação, discordância leve, completar a frase, opinião)
- **O que faz a pessoa compartilhar** (conteúdo que ela quer que alguém veja, utilidade pública)
- **O que faz a pessoa salvar** (referência futura, checklist, passo a passo, revelação)
- **Tom que gera conversa**: provocação suave, opinião contrária ao senso comum, história pessoal

**Se Conversão**, pesquise:
- `anuncio que converte instagram infoproduto [mês e ano atual]`
- `copy anuncio link na bio instagram [mês e ano atual]`

O que extrair:
- **Estrutura de copy que leva ao clique**: gancho de resultado, prova rápida, CTA direto
- **Quanto de prova social aparece**: depoimento, número de alunos, print de resultado
- **Tom do CTA de conversão**: urgência, curiosidade, benefício direto
- **Formato que mais converte para link**: vídeo curto, carrossel de prova, imagem com resultado

**Se RMKT**, pesquise:
- `remarketing anuncio instagram copy [mês e ano atual]`
- `retargeting ad copy que converte [mês e ano atual]`

O que extrair:
- **Abordagem para quem já viu**: urgência, objeção quebrada, prova adicional, desconto, bônus
- **Tom**: não pode parecer perseguição — precisa ser relevância
- **Gatilhos mais usados no RMKT**: escassez, prova social, garantia, comparação de custo
- **CTA de RMKT**: "última chance", "garante agora", "ainda dá tempo"

---

#### Como aplicar o que encontrou

Após as pesquisas, antes de gerar os anúncios, sintetize:

1. **Formato do gancho** — como os virais do momento estão abrindo (estrutura dos primeiros 2–3 segundos)
2. **Estilo visual/edição** — o que está funcionando esteticamente agora
3. **Tom** — o que está ressoando com o público nesse objetivo específico
4. **CTA** — o padrão de chamada que está gerando ação agora
5. **O vídeo entrega ou apenas promete?** — modelar os que entregam conteúdo real dentro do vídeo

Use esses 5 elementos para calibrar as 3 variações. O **conteúdo** (o que diz) segue VTSD + perfil do negócio. O **formato e estilo** (como diz) seguem o que está funcionando agora.

**REGRA CRÍTICA para TODO vídeo (qualquer fase, qualquer objetivo):** o vídeo deve entregar conteúdo real. A pessoa que assiste até o final aprende uma técnica, recebe um insight concreto ou tem uma virada de perspectiva. Vídeo que só promete sem entregar nada dentro do próprio vídeo não funciona. O CTA é consequência do valor entregue — não substituto.

**Estrutura obrigatória para TODO vídeo (~45–60s / ~150–200 palavras):**

```
[0–3s]   GANCHO      → Afirmação contra-intuitiva ou quebra-padrão.
                       Texto na tela + fala simultâneos.
[4–15s]  TEASE       → Expande o gancho, cria tensão, contextualiza o problema.
[16–42s] ENTREGA     → Ensina, demonstra ou revela algo real e concreto.
                       NUNCA apenas prometer — ENTREGAR dentro do vídeo.
[43–48s] REGANCHO    → Texto na tela sintetizando a ideia central
                       (âncora visual para quem assiste sem som).
[49–55s] CTA         → Convite direto adequado à fase. Sem urgência forçada.
```

**Para Descoberta especificamente:** duração alvo de 35–45s. Para Captura, Conversão e demais fases: 45–60s.

Calibrar a duração a partir dos virais encontrados na pesquisa — usar duração similar às referências.

**Três estruturas de roteiro baseadas em virais 2026:**

| Estrutura | Quando usar | Lógica de retenção |
|---|---|---|
| **Loop Perfeito** | Revelação, insights | O final conecta ao gancho — incentiva replay |
| **Tutorial de 3 Passos** | Procedimento, ensino | Cada passo avança a narrativa — pessoa assiste até o fim para completar |
| **Quebra-Padrão** | Contraste, paradoxo | Começo inesperado para o cérebro — força a pausa no scroll |

Usar estruturas diferentes nas 3 variações sempre que possível.

### 4. Geração (após aprovação do resumo)

Use a Mandala de 18 Tipos (skill vtsd-completo):

**Para Meta Ads, gere 3 variações usando tipos diferentes da Mandala da Criatividade:**
- Variação 1: [tipo escolhido] — ex: Comparação, Certo vs Errado
- Variação 2: [tipo escolhido] — ex: Prova, Demonstração
- Variação 3: [tipo escolhido] — ex: Problema-Solução, Curiosidade

**Cada variação inclui:**
- Texto principal (Light Copy — sem ponto de exclamação, sem perguntas no gancho)
- Headline (máx 40 caracteres)
- Descrição
- Direção criativa para imagem/vídeo
- CTA adequado à fase

**CTAs por fase:**
| Fase | CTA típico |
| --- | --- |
| Descoberta | Seguir, curtir, comentar, compartilhar |
| Relacionamento | Comentar, DM, salvar, lives |
| Captura / Aquecimento | Quero participar, garantir minha vaga, me inscrever |
| Conversão / Venda | Comprar agora, garantir vaga, quero começar |
| Remarketing | Comprar agora, retomar oferta, última chance |

**Estrutura de todo anúncio VTSD (texto/legenda) — padrão de profundidade obrigatório:**
- **GANCHO:** premissa não óbvia — NUNCA uma pergunta, NUNCA algo óbvio para quem já está no nicho. 1–2 frases fortes.
- **DESENVOLVIMENTO:** mínimo 2 parágrafos substanciais com argumento específico, concreto e não óbvio. Não pode ser resumo vago — precisa entregar valor por si só, mesmo sem o vídeo. Raso, curto e genérico são proibidos.
- **CTA:** convite direto adequado à fase do funil

**REGRA DE QUALIDADE:** todo anúncio deve entregar valor real. Nenhum anúncio pode ser óbvio, raso ou curto demais. O desenvolvimento deve ter profundidade suficiente para que a pessoa aprenda, entenda ou se reconheça — mesmo lendo só a legenda, sem ver o vídeo.

**Exemplos de gancho ERRADO:**
- "Sabe aquela sensação de travar na leitura?" ❌ (pergunta)
- "Você já se sentiu insegura com o tarô?" ❌ (pergunta)
- "Aprender tarô é difícil." ❌ (óbvio)
- "Você não sabe quanto cobrar?" ❌ (pergunta + óbvio)
- "Cobrar é difícil para tarotistas." ❌ (óbvio)

**Exemplos de gancho CERTO:**
- "A leitora que mais trava raramente é a que sabe menos." ✓ (contra-intuitivo)
- "Decorar os 78 significados é o caminho mais rápido para travar na leitura." ✓ (paradoxo)
- "Você não trava na tiragem por saber pouco. Você trava porque aprendeu na ordem errada." ✓ (revelação)
- "Parei de estudar os significados das cartas por 30 dias. Minha leitura melhorou." ✓ (quebra-padrão)
- "O método que todo mundo ensina primeiro no tarô é o que mais gera travamento na leitura real." ✓ (premissa não óbvia)

**Para Google Ads:**
- 15 títulos (máx 30 caracteres)
- 4 descrições (máx 90 caracteres)
- Palavras-chave + negativas

### 5. Aprovação

Após mostrar os anúncios gerados, perguntar:

```
1. Aprovar e salvar
2. Quero ajustar algo
```

Só salvar após aprovação do usuário.

### 6. Salvar Copy
`produtos/{ativo}/entregas/anuncios/anuncios-meta-[formato]-[objetivo]-[produto].md`

### 7. Geração Visual (imagem, vídeo ou carrossel)

Após salvar a copy, gere automaticamente os visuais de cada variação aprovada.

---

**Se Imagem Estática:**

Para cada variação, monte um prompt de imagem baseado no tipo de anúncio (ex: Comparação, Prova Social, Revelação) e no nicho do produto. O prompt deve descrever:
- Cena ou composição visual que reforça o gancho da copy
- Estilo fotográfico (foto real, clean, minimalista, etc.)
- Paleta de cores alinhada ao produto
- Texto overlay com o headline da variação (quando aplicável)
- Proporção: 1:1 para feed, 9:16 para stories

Leia o `.env` do projeto e verifique se existe `FREEPIK_API_KEY`.

**Se existir**, gere cada imagem via API:
```bash
curl -X POST "https://api.freepik.com/v1/ai/text-to-image" \
  -H "x-freepik-api-key: $FREEPIK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "PROMPT_VARIACAO_N", "num_images": 1, "image": {"size": "square_1_1"}}'
```
Salve cada imagem em: `produtos/{ativo}/entregas/anuncios/img-variacao-[N]-[produto].png`

**Se não existir**, entregue os prompts prontos e em seguida ensine o usuário como configurar, com esta mensagem exata:

---
Seus prompts de imagem estão prontos acima. Para gerar as imagens automaticamente na próxima vez, siga esses passos:

**Como configurar o Freepik AI (gratuito para começar):**

1. Acesse freepik.com e crie uma conta gratuita (ou faça login)
2. Vá em: perfil > API Keys > Create API Key
3. Copie a chave gerada
4. Abra (ou crie) o arquivo `.env` na raiz deste projeto
5. Adicione a linha: `FREEPIK_API_KEY=sua_chave_aqui`
6. Salve o arquivo

Pronto. Na próxima vez que usar `/anuncio`, as imagens serão geradas automaticamente.

Por enquanto, cole cada prompt acima em freepik.com/ai/image-generator para gerar as imagens manualmente.
---

---

**Se Vídeo (Avatar IA):**

Use o roteiro aprovado de cada variação. Verifique no `.env` se existem as três variáveis:
- `HEYGEN_API_KEY`
- `HEYGEN_AVATAR_ID`
- `HEYGEN_VOICE_ID`

**Se todas existirem**, gere o vídeo via HeyGen:
```bash
curl -X POST "https://api.heygen.com/v2/video/generate" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "video_inputs": [{
      "character": {
        "type": "avatar",
        "avatar_id": "HEYGEN_AVATAR_ID",
        "avatar_style": "normal"
      },
      "voice": {
        "type": "text",
        "input_text": "ROTEIRO_VARIACAO_N",
        "voice_id": "HEYGEN_VOICE_ID",
        "speed": 1.0
      },
      "background": {
        "type": "color",
        "value": "#f8f8f8"
      }
    }],
    "dimension": {"width": 1080, "height": 1920}
  }'
```

A API retorna um `video_id`. Faça polling a cada 30 segundos:
```bash
curl "https://api.heygen.com/v1/video_status.get?video_id=VIDEO_ID" \
  -H "X-Api-Key: $HEYGEN_API_KEY"
```

Quando status for `completed`, faça download do `video_url` e salve em:
`produtos/{ativo}/entregas/anuncios/video-variacao-[N]-[produto].mp4`

**Se faltar alguma variável**, entregue o roteiro completo formatado e em seguida ensine o usuário como configurar, com esta mensagem exata:

---
Seu roteiro está pronto acima. Para gerar o vídeo com avatar automaticamente, você precisa configurar o HeyGen. Siga estes passos:

**Como configurar o HeyGen (gerador de vídeo com avatar IA):**

**Passo 1 — Criar conta e pegar a chave da API:**
1. Acesse heygen.com e crie uma conta (plano gratuito tem créditos de teste)
2. No painel, clique no seu perfil (canto superior direito) > API
3. Clique em "Create API Key", dê um nome e copie a chave

**Passo 2 — Pegar o ID do seu avatar:**
1. No painel HeyGen, vá em Avatars (menu lateral)
2. Escolha um avatar ou crie o seu com sua foto
3. Clique no avatar > copie o "Avatar ID" exibido nos detalhes

**Passo 3 — Pegar o ID da voz:**
1. No painel HeyGen, vá em Voices (menu lateral)
2. Filtre por idioma: Portuguese (Brazil)
3. Ouça as opções e escolha a que mais combina com seu estilo
4. Copie o "Voice ID" da voz escolhida

**Passo 4 — Configurar no projeto:**
1. Abra (ou crie) o arquivo `.env` na raiz deste projeto
2. Adicione as três linhas:
```
HEYGEN_API_KEY=sua_chave_aqui
HEYGEN_AVATAR_ID=id_do_avatar_aqui
HEYGEN_VOICE_ID=id_da_voz_aqui
```
3. Salve o arquivo

Pronto. Na próxima vez que usar `/anuncio` com formato Vídeo, o vídeo será gerado automaticamente com seu avatar.

Por enquanto, use o roteiro acima para gravar o vídeo você mesmo ou cole diretamente no painel do HeyGen em app.heygen.com/video-translate ou no editor de vídeo.
---

---

**Se Carrossel:**

Para cada card do carrossel, gere um prompt de imagem individual baseado no texto e tema daquele slide. Cada prompt deve incluir:
- Identidade visual consistente entre todos os cards (mesma paleta, mesmo estilo)
- Composição específica para o conteúdo do card (ex: card 1 = gancho visual impactante, card final = CTA com destaque)
- Texto overlay com o conteúdo principal do card
- Proporção 1:1 (1080x1080)

Leia o `.env` e verifique `FREEPIK_API_KEY`.

**Se existir**, gere uma imagem por card:
```bash
# Repita para cada card (substituir N pelo número do card)
curl -X POST "https://api.freepik.com/v1/ai/text-to-image" \
  -H "x-freepik-api-key: $FREEPIK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "PROMPT_CARD_N", "num_images": 1, "image": {"size": "square_1_1"}}'
```
Salve cada card em: `produtos/{ativo}/entregas/anuncios/carrossel-[N]-[produto].png`

**Se não existir**, entregue os prompts de cada card individualmente e ensine como configurar, com esta mensagem exata:

---
Os prompts de cada slide do carrossel estão prontos acima. Para gerar as imagens automaticamente na próxima vez, configure o Freepik:

**Como configurar o Freepik AI:**
1. Acesse freepik.com e crie uma conta gratuita (ou faça login)
2. Vá em: perfil > API Keys > Create API Key
3. Copie a chave gerada
4. Abra (ou crie) o arquivo `.env` na raiz deste projeto
5. Adicione: `FREEPIK_API_KEY=sua_chave_aqui`
6. Salve

Por enquanto, cole cada prompt acima em freepik.com/ai/image-generator. Gere um slide por vez e mantenha o mesmo estilo visual entre todos para o carrossel ficar coerente.
---

---

**Se Stories:**
Trate como imagem estática com proporção vertical. Substitua `"size": "square_1_1"` por `"size": "portrait_9_16"` no parâmetro da API.

### 8. Próximo Passo
"Anúncios e visuais salvos em [caminho]. Use `/pagina-de-vendas` para criar a página de destino, ou `/sequencia-de-emails` para criar os emails da campanha."
