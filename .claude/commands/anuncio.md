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

### 3. Pesquisa de Tendências (OBRIGATÓRIO antes de gerar)

**Antes de escrever qualquer anúncio**, faça 2 buscas na web — uma por formato, uma por objetivo.

---

#### Busca 1 — Por formato

**Se Vídeo**, pesquise os dois canais obrigatoriamente:
- `reels instagram virais [mês e ano atual]` — todos os nichos
- `tiktok trends virais [mês e ano atual]` — todos os nichos
- `estrutura roteiro viral reels tiktok [mês e ano atual]`

**IMPORTANTE:** Pesquisar virais de **todos os nichos** (não apenas o nicho do produto) para captar o padrão de estrutura e formato vigente na plataforma. O conteúdo (o que diz) vem do produto. O formato e estilo (como diz) vêm dos virais encontrados.

O que extrair:
- **Estrutura dos primeiros 2–3 segundos**: o que está parando o scroll (texto na tela + fala simultânea, afirmação contra-intuitiva, dado específico, revelação)
- **Duração predominante** dos vídeos com mais alcance (7s, 15s, 30s, 45s, 60s) — e usar duração similar
- **Estilo de edição**: cortes rápidos, talking head estático, câmera na mão, B-roll, texto animado
- **Tom predominante**: didático, emocional, provocativo, informal, revelação
- **Se o vídeo entrega conteúdo real ou apenas teaser** — modelar o que entrega conteúdo real
- **Padrão de CTA no final**: o que está sendo usado (salva, comenta, segue, marca alguém)

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

### 6. Salvar
`produtos/{ativo}/entregas/anuncios/anuncios-meta-[formato]-[objetivo]-[produto].md`

### 7. Próximo Passo
"Anúncios salvos em [caminho]. Use `/criativo-de-imagem` para gerar prompts das imagens, ou `/pagina-de-vendas` para criar a página de destino."
