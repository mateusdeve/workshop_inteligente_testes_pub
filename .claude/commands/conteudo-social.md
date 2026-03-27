---
name: workshop-marketing:conteudo-social
description: Criar conteúdo para redes sociais — carrosséis, captions, roteiros de Reels, linha editorial e calendário de publicação. Baseado nas Urgências Ocultas e elementos literários do VTSD.
---

# Conteúdo Social — Criador de Conteúdo para Redes

Cria conteúdo usando as Urgências Ocultas como fonte de temas e os elementos literários para engajar.

## Usage

```
/conteudo-social
```

## O Que Fazer

### 1. Contexto

Leia `produtos/{ativo}/perfil.md` e `produtos/{ativo}/idconsumidor.md` se existir.

**Extraia e liste internamente (não precisa mostrar ao usuário):**
- Todos os **Decorados** do perfil — cada decorado é um benefício que pode virar tema de post
- Todas as **Urgências Ocultas** (dores, desejos, dúvidas, assuntos relacionados) — cada item é um ângulo de entrada para conteúdo
- Os **Baldes de Conteúdo** do `idconsumidor.md` se existir — usá-los para distribuir os temas entre os baldes corretos

**Verifique o histórico:** leia todos os arquivos em `produtos/{ativo}/entregas/conteudo-social/`. Identifique quais urgências ocultas e decorados já foram explorados em conteúdos anteriores.

**Regra de não repetição:** nas novas peças, priorize urgências ocultas e decorados ainda não usados. Se todos já foram usados, escolha os de maior potencial e anote que está retomando esse tema.

Apresente ao usuário (antes de perguntar sobre o tipo de conteúdo):
```
Temos [X] decorados e [Y] urgências ocultas disponíveis como fonte de ideias.
Já explorados em conteúdos anteriores: [lista resumida]
Disponíveis para este pacote: [lista resumida dos ainda não usados]
```

Se não houver conteúdos anteriores: "É o primeiro conteúdo — vamos usar as urgências e decorados mais relevantes para o objetivo escolhido."

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Tipo de Conteúdo:**

```
O que quer criar?

1. Carrossel (post com múltiplos slides)
2. Caption (legenda de post)
3. Roteiro de Reels (vídeo curto 30-60s)
4. Linha editorial (planejamento de 30 dias)
5. Calendário semanal (pauta da semana)

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Tipo: [tipo escolhido]
Próximo: Rede social
---
```

**Bloco 2/3 — Rede Social:**

```
Para qual rede?

1. Instagram
2. TikTok
3. YouTube
4. LinkedIn
5. Várias (quais?)

Digite o número:
```

```
--- Bloco 2/3 concluído ---
Tipo: [tipo]
Rede: [rede]
Próximo: Objetivo
---
```

**Bloco 3/3 — Objetivo:**

```
Qual o objetivo principal?

1. Educar (ensinar algo prático)
2. Engajar (gerar comentários e compartilhamentos)
3. Vender (levar para página/checkout)
4. Atrair seguidores (crescer a base)

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Tipo: [tipo de conteúdo]
- Rede: [rede social]
- Objetivo: [objetivo]
- Base: Urgências Ocultas do perfil

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Pesquisa de Virais (OBRIGATÓRIO antes de gerar — qualquer tipo de conteúdo)

**Antes de escrever qualquer peça de conteúdo**, faça obrigatoriamente as seguintes buscas — independentemente do formato (carrossel, caption, reels, linha editorial):

Pesquise os dois canais obrigatoriamente:
- `reels instagram virais [mês e ano atual]` — todos os nichos
- `tiktok trends virais [mês e ano atual]` — todos os nichos

**REGRA ABSOLUTA:** Pesquisar virais de **todos os nichos** (não apenas o nicho do produto). O objetivo é captar o padrão de estrutura, tom e abertura que está funcionando agora. O conteúdo (o que diz) vem das urgências ocultas e decorados. O formato e o estilo (como diz) vêm dos virais encontrados.

O que extrair:
- **Estrutura de abertura**: o que está parando o scroll nos primeiros 2–3 segundos (afirmação contra-intuitiva, dado específico, paradoxo, confissão, revelação)
- **Tom predominante no momento**: didático, emocional, provocativo, informal, polêmica suave, história pessoal
- **O que os virais entregam**: identificar se entregam conteúdo real dentro do próprio post/vídeo ou apenas prometem — **modelar sempre os que entregam conteúdo real**
- **Estrutura de progressão**: como o conteúdo se desenvolve — começo, meio, fim, cliffhanger, resolução
- **Padrão de CTA**: o que está gerando engajamento agora (salva, comenta, segue, compartilha)

**Se o formato for Reels**, pesquise adicionalmente:
- `estrutura roteiro viral reels tiktok [mês e ano atual]`
- Extrair: duração predominante, estilo de edição, ritmo, se usa texto na tela

Após as buscas, sintetize em 3–4 linhas o que está funcionando agora e use isso para calibrar o estilo e a abertura de cada peça gerada.

---

### 4. Geração

**Regras de estilo Light Copy — obrigatórias em todo conteúdo:**
 Princípio central
A melhor copy não parece copy. Parece alguém inteligente te explicando algo que você nunca tinha entendido.

As 7 leis da copy:
1. Ensinar em vez de prometer: A copy entrega conhecimento real. Curiosidade vem do aprendizado, não de promessa vaga
2. Nomear cria realidade: Dê nomes próprios para problemas ou soluções. Nome transforma ideia em algo concreto
3. O produto não aparece no lead: Nada de “curso”, “treinamento”, “compre” no início. Só o leitor e a realidade dele
4. Tom de escritor, não de vendedor. Escreva como quem explica, não como quem vende. Mostre, não empurre.
5. Especificidade mata generalização: Use números, datas, valores, situações reais: Quanto mais concreto, mais confiável
6. Informar, não vender: Ou você ensina, ou você avisa. Nunca tenta vender diretamente
7. Crie um inimigo concreto (ou cenário inevitável). Um culpado externo facilita a aceitação. Pode ser pessoa, sistema ou método antigo
Vícios proibidos:
Não usar travessão (—)
Não usar estrutura: “Não é X. É Y.”
Não usar frases genéricas de vendedor
Não mencionar o produto na copy
Não usar emojis


**REGRA DE PROFUNDIDADE OBRIGATÓRIA — vale para todo tipo de conteúdo:**
- **Gancho:** afirmação não óbvia, contra-intuitiva ou específica. NUNCA uma pergunta. NUNCA algo genérico.
- **Desenvolvimento:** mínimo 2 parágrafos substanciais. Cada parágrafo precisa entregar um argumento, ensinamento ou insight concreto. Raso, vago e curto são proibidos.
- **O conteúdo precisa entregar valor por si só** — quem lê ou assiste aprende algo, tem uma virada de perspectiva ou se reconhece. Conteúdo que só promete sem entregar nada dentro dele mesmo não é publicado.

---

**Carrossel (7-10 slides):**
- Slide 1: Gancho forte baseado nos virais pesquisados (use elemento literário + abertura modelada nos virais)
- Slides 2-8: Conteúdo de valor real — cada slide avança o argumento, não repete o anterior. Baseado em Urgências Ocultas e Decorados.
- Slide final: CTA + identidade visual
- Caption: mínimo 2 parágrafos de desenvolvimento antes do CTA. Com hashtags relevantes.

**Roteiro de Reels:**

Estrutura obrigatória (~45–60s):
```
[0–3s]   GANCHO    → Afirmação contra-intuitiva ou quebra-padrão. Texto na tela + fala simultâneos.
[4–15s]  TEASE     → Expande o gancho, contextualiza o problema ou a promessa.
[16–42s] ENTREGA   → Ensina, demonstra ou revela algo real e concreto. NUNCA apenas prometer.
[43–48s] REGANCHO  → Texto na tela sintetizando a ideia central (âncora visual para quem assiste sem som).
[49–55s] CTA       → Convite direto e leve. Sem urgência forçada.
```

Duração e estilo de edição: calibrar com base nos virais encontrados na pesquisa.

**Linha editorial (30 dias):**
- Distribuir entre: Dores, Desejos, Dúvidas, Assuntos relacionados (fonte: urgências ocultas do perfil)
- Cada tema distribuído em um balde de conteúdo do `idconsumidor.md` (se existir)
- Alternar formatos: carrossel, reels, stories, post estático
- Incluir CTAs estratégicos (seguidores → leads → vendas)
- Para cada dia: indicar tema, urgência/decorado de origem, formato e objetivo

### 4. Salvar
`produtos/{ativo}/entregas/conteudo-social/[tipo]-[produto].md`

### 5. Próximo Passo
"Conteúdo salvo. Use `/criativo-de-imagem` para gerar as artes, ou `/roteiro-de-video` para roteiros mais elaborados."
