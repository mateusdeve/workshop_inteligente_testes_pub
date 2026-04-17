---
name: workshop-marketing:criativo-de-imagem
description: Criar criativos visuais completos — anúncios, posts, capas, thumbs chamativas e criativos estáticos com design. Inclui 3 caminhos de execução (API automática, prompt para ferramenta gratuita, direção criativa para designer/Canva). Conectado ao perfil do produto e às Urgências Ocultas.
---

# Criativo de Imagem — Gerador de Criativos Visuais

Gera criativos visuais conectados ao produto ativo, à copy e às Urgências Ocultas. Cobre 6 tipos de criativo com 3 caminhos de execução diferentes.

## Usage

```
/criativo-de-imagem
```

## O Que Fazer

### 1. Contexto Estratégico

Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md` se existir.

Extraia e use internamente (não mostrar ao usuário, mas aplicar na geração):
- **Urgências Ocultas dominantes** — as 3 mais fortes (dores, desejos, urgências quentes)
- **Quadro** — a transformação principal que a imagem precisa reforçar visualmente
- **Tom da copy** — como o público fala e pensa (para garantir coerência visual/textual)
- **Paleta e estética** — identidade visual do produto se descrita no perfil

Verifique anúncios existentes em `meus-produtos/{ativo}/entregas/anuncios/` e `meus-produtos/{ativo}/entregas/criativos/`. Se existirem, identifique urgências ocultas já usadas para priorizar ângulos ainda não explorados.

---

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4 — Caminho de Execução:**

Perguntar isso PRIMEIRO para calibrar toda a entrevista seguinte:

```
Como vai executar os criativos?

1. Freepik AI (API automática — precisa de FREEPIK_API_KEY no .env)
2. Midjourney (qualidade premium — precisa de conta paga)
3. DALL·E via Bing (grátis com conta Microsoft)
4. Ferramenta gratuita à sua escolha (Whisk, Ideogram, ImageFX, Leonardo, Krea)
5. Direção criativa para designer, editor ou Canva

Digite o número:
```

Se escolher opção 1: verificar `FREEPIK_API_KEY` no `.env` e gerar automaticamente.
Se escolher opções 2, 3 ou 4: ao final da entrevista, redirecionar para `/imagem-prompt` com o contexto já preenchido, entregando prompts otimizados para a ferramenta escolhida.
Se escolher opção 5: entregar briefing completo de direção criativa (sem geração de imagem).

```
--- Bloco 1/4 concluído ---
Execução: [caminho]
Próximo: Tipo de criativo
---
```

**Bloco 2/4 — Tipo de Criativo:**

```
O que você quer criar?

1. Imagem para anúncio (Meta Ads, feed ou stories)
2. Post Instagram (feed ou carrossel)
3. Capa de conteúdo (YouTube, blog, produto digital)
4. Banner de página de vendas
5. Thumb chamativa (estilo YouTube thumbnail, expressão exagerada, impacto visual)
6. Criativo estático com design (anúncio com layout gráfico completo, texto + visual estruturado)

Digite o número:
```

```
--- Bloco 2/4 concluído ---
Execução: [caminho]
Tipo: [tipo escolhido]
Próximo: Estilo visual
---
```

**Bloco 3/4 — Estilo Visual:**

Exibir sugestões adaptadas ao tipo escolhido:

Se tipo 1, 4 ou 6 (anúncio/banner/estático):
```
Qual o estilo visual?

1. Moderno e clean (fundo simples, foto real, pouco texto)
2. Minimalista (muito espaço vazio, tipografia protagonista)
3. Vibrante e colorido (contraste alto, energia, paleta forte)
4. Profissional/corporativo (tom sério, azul/cinza/branco)
5. Premium/luxo (escuro, dourado, tipografia refinada)
6. Outro (descreva)
```

Se tipo 5 (thumb chamativa):
```
Qual o estilo da thumb?

1. Caricatura expressiva (expressão exagerada, rosto em destaque, fundo simples)
2. Contraste dramático (antes/depois, dois lados, paleta de alto contraste)
3. Revelação com seta (pessoa apontando para dado ou texto chamativo)
4. Colagem estilo polêmica (múltiplos elementos, texto grande, urgência visual)
```

Se tipo 2 ou 3 (post/capa):
```
Qual o estilo visual?

1. Educacional limpo (fundo claro, ícones, tipografia, cores da marca)
2. Foto com overlay de texto (imagem real + camada de texto sobreposta)
3. Ilustração flat colorida
4. Cinematográfico (foto ambiente, luz dramática, cor quente/fria dominante)
5. Outro (descreva)
```

```
--- Bloco 3/4 concluído ---
Execução: [caminho]
Tipo: [tipo]
Estilo: [estilo]
Próximo: Texto na imagem
---
```

**Bloco 4/4 — Texto na Imagem:**

```
Que texto deve aparecer na imagem?
(ex: "Fale inglês em 90 dias", "Garanta sua vaga", ou "nenhum")
```

Para tipo 5 (thumb chamativa): adicionar regra na resposta — "Para thumbs, texto deve ter no máximo 5 palavras e ser altamente específico (número, dado, palavra de impacto)."

Para tipo 6 (criativo estático com design): informar que o briefing completo incluirá hierarquia de texto (headline, subhead, CTA) — não precisa definir tudo agora.

**Confirmação antes de gerar:**

```
Resumo do que vou criar:
- Execução: [Freepik API / Midjourney / DALL·E via Bing / [ferramenta] / Direção criativa]
- Tipo: [tipo]
- Estilo: [estilo]
- Texto: [texto ou nenhum]
- Urgência Oculta base: [urgência dominante extraída do perfil]
- Quantidade: 3 variações

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

---

### 3. Geração por Tipo

#### Tipos 1, 2, 3, 4 — Imagem para Anúncio, Post, Capa, Banner

Para cada variação, gerar:
1. **Prompt completo** otimizado para a ferramenta (ou genérico se caminho 3)
2. **Direção criativa:**
   - Conceito visual e qual Urgência Oculta ele trabalha
   - Paleta de cores (HEX quando possível)
   - Composição e enquadramento (ex: "personagem no canto esquerdo, texto à direita")
   - Estilo fotográfico ou ilustrativo
   - Texto overlay sugerido com hierarquia
3. **Especificações técnicas:**
   - Dimensões por plataforma
   - Formato de arquivo
   - Zona segura para texto

---

#### Tipo 5 — Thumb Chamativa

Regras específicas para thumbs de alto impacto:

**Elementos obrigatórios de uma thumb eficaz:**
- Expressão facial exagerada (surpresa, choque, euforia, incredulidade)
- Paleta de contraste alto: fundo de cor sólida forte (amarelo, vermelho, azul-elétrico) + elementos em preto ou branco
- Texto curto em bold (máx 5 palavras), fonte sem serifa, tamanho grande (ocupa pelo menos 30% da imagem)
- Elemento visual de atenção (seta, círculo destacando algo, marca de interrogação grande)
- Rostos em close ou 3/4

**Referências de estilo por nicho:**
- Conteúdo educativo: fundo amarelo brilhante, texto preto bold, expressão de "revelação"
- Resultado/transformação: split antes/depois, texto "RESULTADO" ou número de impacto
- Polêmica/opinião: fundo vermelho, expressão de incredulidade, texto provocativo
- Tutorial/passo a passo: fundo branco, ícones numerados, expressão confiante

Para cada variação, gerar:
1. **Descrição detalhada** da expressão facial e postura
2. **Composição** (posição do rosto, fundo, texto, elementos de destaque)
3. **Texto exato** que vai aparecer (máx 5 palavras, específico e impactante)
4. **Prompt de imagem** com ênfase no rosto expressivo e fundo limpo
5. **Dimensões:** 1280x720 (YouTube) ou 1:1 para Instagram

---

#### Tipo 6 — Criativo Estático com Design

Diferente de uma foto com texto, este tipo é uma **peça gráfica estruturada**, como um anúncio de revista ou outdoor digital. A saída é um briefing completo de design que pode ser executado no Canva, Adobe Express, ou por um designer.

Para cada variação, gerar:

**Briefing Completo da Peça:**

```
--- Variação [N] ---

Conceito: [ideia central e Urgência Oculta trabalhada]

Hierarquia visual:
  Headline principal: [texto — fonte grande, peso 700-900, cor de destaque]
  Subhead: [texto secundário — fonte média, peso 400-500, cor secundária]
  CTA: [chamada para ação — botão ou texto, cor de contraste alto]
  Rodapé (opcional): [nome do produto, URL ou branding mínimo]

Composição:
  Proporção: [1:1 / 4:5 / 9:16 / 16:9]
  Zona quente (onde o olho vai primeiro): [canto superior esquerdo / centro / etc.]
  Divisão da tela: [ex: "60% imagem à esquerda, 40% texto à direita sobre fundo escuro"]
  Zona segura para texto: [descrever margens mínimas]

Visual (fundo/foto):
  Descrição: [o que aparece na imagem de fundo ou foto]
  Prompt de IA para gerar o visual: [prompt em inglês pronto para Freepik/Ideogram]
  Alternativa no Canva: [categoria de template ou elemento a buscar]

Tipografia:
  Headline: [fonte sugerida — ex: Inter Black, Montserrat 900]
  Body/subhead: [fonte sugerida]
  Pesos e tamanhos relativos

Paleta:
  Cor primária: [HEX]
  Cor secundária: [HEX]
  Cor de fundo: [HEX]
  Cor do CTA: [HEX]

Instruções para montar no Canva:
  1. [passo 1]
  2. [passo 2]
  3. [passo 3]
```

---

### 4. Saída por Caminho de Execução

**Caminho 1 — API Freepik automática:**

Leia `.env` e verifique `FREEPIK_API_KEY`.

Se existir, gerar cada imagem via API:

```bash
curl -X POST "https://api.freepik.com/v1/ai/text-to-image" \
  -H "x-freepik-api-key: $FREEPIK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "PROMPT_AQUI", "num_images": 1, "image": {"size": "square_1_1"}}'
```

Para stories/vertical: usar `"size": "portrait_9_16"`.
Para landscape: usar `"size": "landscape_16_9"`.

Salvar em: `meus-produtos/{ativo}/entregas/criativos/imagem-[N]-[produto].png`

Informar: "Imagens geradas e salvas em entregas/criativos/."

Se não existir, orientar como configurar:

---
Configure o Freepik AI para geração automática:

1. Acesse freepik.com e crie uma conta gratuita (ou faça login)
2. Vá em: perfil > API Keys > Create API Key
3. Copie a chave gerada
4. Abra (ou crie) o arquivo `.env` na raiz deste projeto
5. Adicione: `FREEPIK_API_KEY=sua_chave_aqui`
6. Salve e rode `/criativo-de-imagem` novamente
---

**Caminhos 2, 3 e 4 — Prompts otimizados por ferramenta:**

Ao final da entrevista, entregar o contexto preenchido e direcionar para `/imagem-prompt`:

```
Contexto coletado:
- Tipo: [tipo]
- Estilo: [estilo]
- Urgência Oculta base: [urgência]
- Texto na imagem: [texto ou nenhum]
- Ferramenta: [Midjourney / Bing (DALL·E) / [ferramenta gratuita escolhida]]

Use /imagem-prompt para gerar os prompts no formato nativo da ferramenta.
O /imagem-prompt cobre: Midjourney, Bing (DALL·E 3), Whisk, Ideogram,
ImageFX, Gemini, Leonardo, Krea — cada uma com seu formato nativo otimizado.
```

Regras por ferramenta:
- **Midjourney**: prompts com parâmetros `--ar --v 6.1 --style raw` e negative prompt
- **DALL·E via Bing**: linguagem natural descritiva, sem parâmetros técnicos
- **Ideogram**: único que aceita texto literal na imagem sem erro — usar quando o criativo precisar de headline inscrita
- **Whisk**: único que mantém personagem consistente — usar para carrossel com rosto fixo

**Caminho 3 — Direção criativa para designer ou Canva:**

Entrega para cada variação:
- Briefing completo (conceito, composição, paleta, tipografia, texto)
- Prompt de IA para o visual de fundo (caso queira gerar o elemento visual separado)
- Instrução passo a passo para montar no Canva ou Adobe Express
- Referências de estilo (descrever 1-2 imagens de referência com palavras)

---

### 5. Aprovação e Salvamento

Mostrar o conteúdo gerado (prompts e briefings) e perguntar:

```
1. Aprovar e salvar
2. Quero ajustar algo
```

Após aprovação:
- Prompts e briefings: `meus-produtos/{ativo}/entregas/criativos/criativos-[tipo]-[produto].md`
- Imagens geradas via API: `meus-produtos/{ativo}/entregas/criativos/imagem-[N]-[produto].png`

---

### 6. Próximo Passo

Após entregar:
- "Use `/anuncio` para criar a copy dos anúncios que vão usar esses criativos."
- Se thumb criada: "Use `/roteiro-de-video` para criar o vídeo que acompanhará esta thumb."
- Se criativo estático: "Abra o Canva, busque o template de [proporção] e siga o briefing do arquivo salvo."
