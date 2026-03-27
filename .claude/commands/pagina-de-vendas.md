---
name: workshop-marketing:pagina-de-vendas
description: Criar copy completa e/ou página HTML profissional de vendas, captura ou obrigado. Gera texto persuasivo (Light Copy, estrutura 8D) e/ou página com design responsivo baseado na metodologia VTSD.
---

# Página de Vendas — Copy e HTML

Cria a copy completa da página de vendas e/ou a página HTML profissional com estrutura de conversão baseada na metodologia VTSD.

## Usage

```
/pagina-de-vendas
```

---

## O Que Fazer

### 1. Contexto

Leia `produtos/{ativo}/perfil.md` e `produtos/{ativo}/idconsumidor.md` se existir.

### 2. Primeira Pergunta — O que criar

```
O que você quer criar?

1. Só a copy (texto completo da página de vendas em markdown)
2. Só a página HTML (usa copy já salva ou gera durante a criação)
3. Copy + página HTML (gera o texto primeiro, depois monta a página)

Digite o número:
```

---

## FLUXO A — Só a Copy

> Ativar quando o usuário escolher a opção 1.

### A1. Entrevista rápida (máximo 2-3 perguntas)

Você já tem `perfil.md` e `idconsumidor.md` com Quadro, Furadeira, Decorados, Urgências Ocultas, Identidades, objeções e pesquisa de mercado. Use TUDO isso para gerar a copy. Pergunte apenas o que NÃO está no perfil:

```
Tem promoção, desconto ou condição especial ativa?
(ex: "Lançamento com 40% de desconto até sexta" — ou "não")
```

```
Tem bônus específicos que quer incluir?
(ex: "Planilha de precificação + script de objeções" — ou "não, pode criar")
```

```
Tem depoimentos reais? Se sim, passe nome e resultado de cada um.
(ex: "Ana, estava cobrando R$30, agora cobra R$120 por leitura" — ou "não tenho")
```

```
Qual o ângulo de entrada da copy?

1. Inadequação — a pessoa está desatualizada ou fazendo errado
2. Identificação — a pessoa se reconhece na dor descrita
3. Plug & Play — a pessoa quer algo pronto para usar
4. Promessa Boa Demais — existe história real com números verificáveis

Digite o número:
```

Confirme antes de gerar:

```
Resumo do que vou criar:
- Produto: [nome do produto]
- Preço: [preço do perfil]
- Ângulo: [ângulo escolhido]
- Bônus: [bônus informados ou "vou criar 3 coerentes"]
- Depoimentos: [reais ou "vou criar modelos para substituir"]

Aviso: vou gerar em 2 partes para garantir qualidade.

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### A2. Princípios de Copy (Light Copy — SEMPRE)

**Princípio central:** A melhor copy não parece copy. Parece alguém inteligente te explicando algo que você nunca tinha entendido.

**As 7 leis da copy:**
1. Ensinar em vez de prometer: a copy entrega conhecimento real. Curiosidade vem do aprendizado, não de promessa vaga
2. Nomear cria realidade: dê nomes próprios para problemas ou soluções. Nome transforma ideia em algo concreto
3. O produto não aparece no lead: nada de "curso", "treinamento", "compre" no início. Só o leitor e a realidade dele
4. Tom de escritor, não de vendedor: escreva como quem explica, não como quem vende. Mostre, não empurre
5. Especificidade mata generalização: use números, datas, valores, situações reais. Quanto mais concreto, mais confiável
6. Informar, não vender: ou você ensina, ou você avisa. Nunca tenta vender diretamente
7. Crie um inimigo concreto (ou cenário inevitável): um culpado externo facilita a aceitação. Pode ser pessoa, sistema ou método antigo

**Vícios proibidos:**
- Não usar travessão (—)
- Não usar estrutura: "Não é X. É Y."
- Não usar frases genéricas de vendedor
- Não mencionar o produto no lead
- Não usar emojis

**Nomear cria realidade:** sempre que possível, criar um nome próprio para o conceito, problema ou solução. Nomes como "Negociação Terapêutica" ou "Programação Emocional Repetitiva" funcionam. "Método Exclusivo" não funciona.

**Parágrafo técnico em itálico:** incluir um parágrafo em itálico que ancora a emoção com razão — explica por que aquilo funciona do ponto de vista científico ou lógico.

Use os 26 elementos literários quando apropriado (consulte skill vtsd-completo para lista completa).

### A3. Geração em 2 Partes

Para garantir qualidade, SEMPRE gere em duas partes separadas.

#### PARTE 1 — Persuasão (Seções 1 a 8)

Gere as seções 1 a 8 completas e salve no arquivo. Cada seção narrativa deve ter parágrafos desenvolvidos com linguagem da persona, cenas do cotidiano e elementos literários.

**Seção 1 — Primeira Dobra (Hero)**
- Headline principal (premissa matadora baseada no Quadro)
- Subheadline (expansão da promessa)
- 3 bullet points (cada um = Urgência Oculta + Decorado)
- Indicação de vídeo de vendas
- Botão de Vendas

**Seção 2 — Paliativo**
- Uma parte do produto ou ferramenta que resolve uma dor específica rápido

**Seção 3 — Prova Social**
- 3-6 depoimentos completos (nome, situação antes, resultado depois)
- Se não tiver reais, gere modelos marcados: "[Depoimento modelo — substituir por depoimento real]"

**Seção 4 — Solução (Apresentação do Método)**
- Apresente o produto como a resposta lógica de forma visual
- Mostre a Furadeira: macroetapas + o que cada uma resolve
- Nome do método em destaque
- Mínimo 3 parágrafos

**Seção 5 — Para Quem É**
- Use os baldes de "pra quem é" da identidade do consumidor
- O público se reconhece aqui

**Seção 6 — Entregáveis (Módulos/Conteúdo)**
- Lista completa do que está incluso
- Cada item com nome + descrição de valor (não só o nome)
- Use metáforas de valor para tangibilizar

**Seção 7 — Bônus**
- 3 bônus estratégicos (gere com base no perfil e persona se o aluno não tiver)
- Cada bônus com: nome, descrição completa e valor individual em R$
- Bônus devem resolver objeções ou complementar o produto

**Seção 8 — Stack de Valor (Ancoragem)**
- Liste tudo que está incluso com valor individual
- Some o valor total
- Mostre o preço real como fração do valor total

Ao terminar a Parte 1, salve no arquivo e informe:
"Parte 1 pronta (seções 1 a 8). Gerando a Parte 2 agora..."

#### PARTE 2 — Conversão (Seções 9 a 14)

Continue no mesmo arquivo. Mesmo nível de detalhe da Parte 1.

**Seção 9 — Prova Social**
- 3-6 depoimentos completos (nome, situação antes, resultado depois)
- Se não tiver reais, gere modelos marcados: "[Depoimento modelo — substituir por depoimento real]"

**Seção 10 — Garantia**
- Tipo de garantia (7, 15 ou 30 dias)
- Texto que elimina o risco
- Tom confiante, não defensivo

**Seção 11 — Autoridade do Criador**
- Pequena apresentação do criador do método

**Seção 12 — FAQ**
- 5-8 perguntas frequentes baseadas nas objeções da persona
- Respostas curtas, diretas, que quebram a objeção

**Seção 13 — Último CTA**
- Reforço de urgência ou escassez (se houver)
- Frase de fechamento + botão final

**Seção 14 — Rodapé**
- Indicações de termos de uso e política de privacidade

### A4. Salvar

`produtos/{ativo}/entregas/copy-pagina/copy-[produto].md`

### A5. Próximo Passo

```
Copy completa salva em produtos/{ativo}/entregas/copy-pagina/copy-[produto].md

Quer que eu monte a página HTML agora com essa copy?

1. Sim, montar a página HTML
2. Não agora

Digite o número:
```

Se escolher 1, execute o Fluxo B usando a copy recém-gerada.

---

## FLUXO B — Página HTML

> Ativar quando o usuário escolher a opção 2 ou 3, ou quando aceitar montar a HTML após o Fluxo A.

### B1. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Tipo de Página:**

```
Qual tipo de página?

1. Página de vendas (estrutura 8D completa)
2. Página de captura (coletar email/WhatsApp)
3. Página de obrigado (pós-cadastro ou pós-compra)

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Tipo: [tipo escolhido]
Próximo: Detalhes do conteúdo
---
```

**Bloco 2/3 — Detalhes (varia conforme o tipo):**

Se escolheu **1. Vendas:**
```
Quais os entregáveis do produto? O que está incluso na compra?
(ex: "Planilha principal + guia de preenchimento + tabela de serviços")
```
```
Tem depoimentos de clientes? Se sim, passe nome e resultado de cada um.
(ex: "Ana, estava cobrando R$30, agora cobra R$120 por leitura" — ou "não tenho" para criar placeholders)
```
```
Qual a garantia?

1. 7 dias
2. 15 dias
3. 30 dias
4. Sem garantia

Digite o número:
```
```
Qual o preço?
(ex: "R$37" ou "R$497 ou 12x R$47")
```
```
Tem bônus? Quais?
(ex: "Guia de reajuste de preços, script de objeções" — ou "não" para criar bônus coerentes)
```
```
Link de checkout (Hotmart, Kiwify)?
(ex: "https://pay.hotmart.com/ABC123" ou "ainda não tenho")
```
```
Tem um vídeo de vendas para a primeira dobra?
(ex: "https://www.youtube.com/watch?v=XXXX" — ou "ainda não tenho" para usar placeholder)
```

Se escolheu **2. Captura** ou **3. Obrigado**, verificar ANTES se já existem páginas criadas em `produtos/{ativo}/entregas/paginas/`. Se existirem, perguntar:

```
Encontrei estas páginas já criadas:
[listar arquivos encontrados]

Quer que a nova página siga o mesmo visual (cores, fontes, estilo)?

1. Sim, manter a identidade visual da página existente
2. Não, quero um visual diferente

Digite o número:
```

Se escolher **1**, ler o HTML da página existente para extrair: paleta de cores, fontes, padrões de componentes, estilo de botões e cards. Aplicar a mesma identidade visual na nova página.

Se escolher **2**, seguir o fluxo normal de entrevista visual (Bloco 3/3).

---

Se escolheu **2. Captura:**
```
Qual a isca digital?
(ex: "E-book gratuito", "Aula ao vivo", "Checklist")
```
```
Qual a promessa principal da isca?
(ex: "7 passos para falar inglês em reuniões")
```

Se escolheu **3. Obrigado:**
```
Confirmação de quê?

1. Cadastro em isca digital
2. Compra de produto
3. Inscrição em evento

Digite o número:
```
```
Tem próximo passo para o aluno?
(ex: "Entrar no grupo do WhatsApp", "Acessar a plataforma", "Aguardar email")
```

```
--- Bloco 2/3 concluído ---
Tipo: [tipo]
Detalhes: [resumo dos detalhes]
Próximo: Visual
---
```

**Bloco 3/3 — Visual:**

```
Preferência de cor?

1. Azul (confiança, autoridade)
2. Verde (saúde, resultados)
3. Roxo (marketing, criatividade)
4. Vermelho (urgência, paixão)
5. Rosa (beleza, feminino)
6. Preto/Dourado (premium)
7. Deixa comigo (escolho a ideal para o nicho)

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Tipo: [tipo de página]
- Produto: [nome do produto]
- Cor: [cor escolhida]
- [detalhes específicos do tipo]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### B2. Mixagem de Templates (OBRIGATÓRIO)

**NUNCA use um template sozinho.** Sempre selecione **2-3 templates** da biblioteca e **misture** os melhores elementos de cada um para criar um resultado orgânico e único.

Os templates estão em `skills/paginas/references/templates/`. Cada template tem `code.html` (código) e/ou `DESIGN.md` (especificação).

#### Catálogo de Templates por Nicho

**Artesanato / Handmade:**
- `terra_trama/` — Assimetria orgânica, No-Line Rule, tonal layering, Noto Serif + Manrope
- `artes_elegance/` — Editorial tátil, Big Lead technique, glassmorphism, ghost borders
- `ateli_moderno/` — Micro-labels Vogue (10px uppercase), imagens grayscale→cor, whitespace agressivo
- `vtsd_ateli_lucrativo/` — HTML: skewed backgrounds, staggered image grids, grid-line texture
- `landing_page_croch_lucrativo/` — HTML: bento grid, floating cards, progress bars

**Gastronomia / Confeitaria:**
- `velvet_ganache/` — Luxo editorial gastronômico, Noto Serif + Manrope
- `vtsd_doces_de_elite/` — HTML completo, tons quentes de confeitaria
- `modelo_confeitaria_gastronomia/` — HTML completo, Epilogue + Manrope

**Marketing / Negócios:**
- `hyperion_growth/` — Dark mode, neon kinético, Space Grotesk + Manrope
- `vtsd_marketing_digital/` — HTML completo, dark mode, growth estética

**Saúde / Fitness:**
- `energia_pura/` — Brutalismo orgânico, alta energia, Space Grotesk + Manrope
- `modelo_sa_de_bem_estar/` — HTML completo, tons verdes
- `modelo_academia_fitness/` — HTML completo, foco em performance

**Desenvolvimento Pessoal / Coaching:**
- `zen_moderno/` — Minimalismo zen, santuário tátil, Noto Serif + Manrope
- `vtsd_desenvolvimento_pessoal/` — HTML completo

**Finanças / Investimentos:**
- `equity_ledger/` — Visual corporativo sólido, tons escuros
- `modelo_finan_as_investimentos/` — HTML completo, azul escuro + dourado

**Premium / High Ticket / Executivo:**
- `echelon_executive/` — Estética boardroom, Manrope + Inter
- `vtsd_executivo/` — HTML completo, visual executivo premium
- `vtsd_global_dean/` — HTML completo, global/autoridade

**Tech / SaaS:**
- `electric_velocity/` — Dark void, neon kinético, Manrope + Inter
- `modelo_tech_moderno/` — HTML completo, dark mode, AI/innovation

**Educação / Mentoria:**
- `sovereign_academic/` — Visual acadêmico sofisticado
- `modelo_educa_o_mentoria/` — HTML completo

**Beleza / Skincare / Feminino:**
- `ethereal_bloom/` — Visual etéreo, floral, feminino
- `modelo_beleza_skincare/` — HTML completo, rosa + dourado

**Imobiliário / Luxo:**
- `horizonte_thos/` — Galeria curada, Noto Serif + Manrope
- `modelo_imobili_ria_de_luxo/` — HTML completo

**Pet / Animais:**
- `amigo_fiel/` — Visual amigável para pet lovers

**Genérico / Clean:**
- `landing_page_moderno_clean/` — HTML completo, serve como base neutra

#### Como Mixar Templates

**Passo 1 — Selecione 2-3 templates:**
1. **Template principal** — o mais próximo do nicho (para estrutura e layout)
2. **Template de design** — um DESIGN.md com sistema de design sofisticado (para princípios visuais)
3. **Template complementar** (opcional) — de outro nicho, para quebrar padrões previsíveis

**Passo 2 — Leia os templates selecionados:**
- Se `code.html` existe: leia o HTML completo para extrair padrões de código
- Se só tem `DESIGN.md`: leia as especificações (paleta, fontes, componentes, regras)

**Passo 3 — Extraia elementos específicos de cada template:**

De cada template, extraia pelo menos **2-3 elementos únicos**. Exemplos:

| Template | O que extrair |
|---|---|
| `terra_trama` | Assimetria intencional, imagens sobrepostas, tonal layering sem sombras |
| `artes_elegance` | Big Lead technique (headline gigante + body contrastante), ghost borders, glassmorphism |
| `ateli_moderno` | Micro-labels Vogue (10px uppercase, 0.35em tracking), imagens grayscale→cor no hover |
| `vtsd_ateli_lucrativo` | Skewed background shapes, staggered image grids, grid-line texture como overlay |
| `landing_page_croch_lucrativo` | Bento grid no problema, floating testimonial cards, progress bars em cards |
| `hyperion_growth` | Neon glow effects, dark void backgrounds, kinetic hover states |
| `zen_moderno` | Whitespace extremo, transições lentas, paleta muted com 1 acento |
| `echelon_executive` | Tipografia de autoridade, dados em destaque, grid formal com quebra inesperada |

**Passo 4 — Monte a página combinando:**
- **Layout e estrutura** do template principal (hero, grids, seções)
- **Sistema de design** do template DESIGN.md (cores, fontes, espaçamento, regras como No-Line)
- **Componentes visuais** do template complementar (cards, hovers, texturas, divisores)
- **Paleta e fontes** definidas pelo usuário na entrevista

#### Regra de Ouro da Mixagem

O resultado final NÃO deve parecer nenhum template individual. Se alguém abrir o template original e a página gerada, devem parecer projetos diferentes.

**Padrões obrigatórios (aplicar SEMPRE):**
- Use **Tailwind CDN** com config customizado OU CSS puro com variables — escolha um
- Use **Material Symbols Outlined** ou **Phosphor Icons** para ícones
- **No-Line Rule**: sem bordas 1px entre seções. Usar mudanças tonais e espaçamento
- **Glassmorphism** para navs e cards sobrepostos: `backdrop-filter: blur() + rgba`
- **Assimetria intencional**: layouts não são 100% simétricos
- **Micro-labels**: pelo menos na nav e em badges, usar texto 10-11px uppercase com tracking largo
- **Tonal layering**: profundidade por camadas de cor, não por drop shadows pesados
- **Editorial spacing**: espaçamento generoso (80-96px) entre seções principais

### B3. Geração

Consulte a base de design em `skills/paginas/references/cdn-design-resources.md` para CDNs e padrões visuais.

**Se existir `produtos/{ativo}/entregas/copy-pagina/copy-[produto].md`, use a copy pronta.** Se não existir, gere a copy durante a construção da página aplicando os princípios Light Copy do Fluxo A.

---

## REGRAS CRÍTICAS DE QUALIDADE

### Regra 1: Texto SEMPRE em português com acentos

**OBRIGATÓRIO:** Todo texto visível na página DEVE estar em português do Brasil com acentos corretos.

- "Módulos" e NÃO "Modulos"
- "Precificação" e NÃO "Precificacao"
- "Vídeo" e NÃO "Video"
- "Método" e NÃO "Metodo"
- "Você" e NÃO "Voce"
- "Não" e NÃO "Nao"

Use `<meta charset="UTF-8">` e garanta que TODOS os textos tenham acentuação correta. **Antes de salvar, revise TODOS os textos.**

### Regra 2: Logotipo no topo OBRIGATÓRIO

Toda página DEVE ter um logotipo/marca no topo antes do hero ou como parte do header.

```html
<header class="site-header">
  <div class="container">
    <div class="logo">
      <!-- Opção 1: Imagem -->
      <img src="[caminho-do-logo]" alt="Nome do Produto" class="logo-img">
      <!-- Opção 2: Logo texto estilizado -->
      <span class="logo-text">Nome do Produto</span>
    </div>
  </div>
</header>
```

Regras do header:
- Fundo transparente ou cor sólida que combine com o hero
- Logo alinhado à esquerda
- Pode incluir botão CTA pequeno à direita
- No mobile, centralizar o logo
- Placeholder instrucional: `[Insira seu logotipo aqui — tamanho recomendado: 180x50px]`

### Regra 3: Grids e cards NÃO podem quebrar texto

- Cards com texto descritivo: `min-width: 320px` no grid
- Se o card tem lista de itens: usar `grid-template-columns: repeat(auto-fit, minmax(340px, 1fr))`
- Texto dentro de card: NUNCA menor que `font-size: 0.95rem`
- Padding interno dos cards: mínimo 28px em todos os lados
- Para seções de Entregáveis ou Módulos: usar 2 colunas no desktop, 1 no mobile (NUNCA 3 colunas)

### Regra 4: NÃO parecer design genérico de IA

**PROIBIDO:**
- Fontes serifadas em qualquer parte da página
- Gradiente roxo-azul em fundo branco
- Cards brancos arredondados idênticos em fundo bege
- Layout 100% simétrico sem surpresa visual
- Ícones dentro de quadrados arredondados com fundo pastel
- Tudo flat sem texturas ou profundidade

**OBRIGATÓRIO:**
- **TODAS as fontes sans-serif** — heading E body
- Seções visualmente diferentes entre si
- Imagens de fundo em pelo menos 2 seções
- Contraste forte entre seções (escura → clara → imagem → colorida)
- Hover states que surpreendem (mover, escalar, revelar)

### Regra 5: Seções DEVEM ser visualmente diferentes entre si

**Variações obrigatórias de fundo (alternar pelo menos 4 tipos):**
1. Fundo sólido claro — branco ou off-white
2. Fundo sólido escuro — cor primária escura com texto claro
3. Fundo com imagem — Picsum com overlay escuro + texto claro
4. Fundo com gradiente sutil
5. Fundo com textura/padrão CSS
6. Fundo colorido vibrante

**Exemplo de sequência bem variada:**
```
Hero:         Fundo escuro com gradiente + texto claro
Problema:     Fundo claro + cards com borda
Paliativo:    Fundo com imagem + overlay escuro
CTA meio:     Fundo cor vibrante + texto branco
Método:       Fundo claro com textura sutil
Para quem:    Fundo escuro sólido
Entregáveis:  Fundo claro + cards grandes
Depoimentos:  Fundo com imagem + cards flutuantes
CTA final:    Fundo escuro com gradiente
```

### Regra 6: Imagens de fundo em seções

Pelo menos **2 seções** devem ter imagem de fundo.

```css
.section-com-imagem {
  background:
    linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
    url('https://picsum.photos/1920/1080?random=1');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: #fff;
}
```

---

## Recursos CDN permitidos

- **Google Fonts** — combinação heading + body
- **1 biblioteca de ícones** — Phosphor Icons (recomendado), Lucide ou Tabler Icons
- **AOS (Animate on Scroll)** — para animações de entrada
- **Avatares para depoimentos** — pravatar.cc ou DiceBear
- **Placeholders de imagem** — Lorem Picsum com tema relacionado ao nicho

## Escolha de Fontes por Nicho

**REGRA: TODAS as fontes DEVEM ser sans-serif** — heading E body. Fontes serifadas são PROIBIDAS.

| Nicho | Heading | Body |
|---|---|---|
| Finanças/Business | Montserrat 700 | Source Sans 3 400,600 |
| Saúde/Bem-estar | Poppins 700 | Nunito 400,600 |
| Educação/Cursos | Fjalla One 400 | Nunito 400,600 |
| Feminino/Lifestyle | Raleway 700 | DM Sans 400,500 |
| Artesanato/Handmade | Bricolage Grotesque 700 | DM Sans 400,500 |
| Marketing/Negócios | Bebas Neue 400 | DM Sans 400,500,700 |
| Tech/Produtividade | Space Grotesk 500,700 | Inter 400,500 |
| Premium/High Ticket | Urbanist 700 | Manrope 400,500,600 |
| Coaching/Dev Pessoal | Plus Jakarta Sans 700 | Plus Jakarta Sans 400,500 |
| Pet/Animais | Figtree 700 | Figtree 400,500 |
| Imobiliário/Luxo | Urbanist 800 | Source Sans 3 400,600 |
| Gastronomia | Sora 700 | DM Sans 400,500 |
| Beleza/Skincare | Raleway 600 | Outfit 400,500 |

## Paletas por Nicho

- **Finanças**: Azul marinho #1e3a5f + Dourado #d4a574 + CTA Verde #38a169
- **Saúde**: Verde #11998e + Branco + CTA Laranja #dd6b20
- **Educação**: Azul #2b6cb0 + Laranja #e07a58 + CTA Laranja #dd6b20
- **Feminino**: Rose #f5576c + Nude #fdf6ec + CTA Dourado #d69e2e
- **Tech**: Escuro #0c0c1d + Azul elétrico #667eea + CTA Verde #38a169
- **Coaching**: Terracota #c4603c + Creme #fdf6ec + CTA Laranja #ed8936
- **Artesanato**: Dourado #d4a574 + Marrom #2d1810 + CTA Verde #38a169

## Padrão Técnico HTML

- Arquivo HTML único
- CSS em `<style>` (CSS custom properties para cores, fontes, espaçamento)
- JS em `<script>` no final do body
- Modern CSS Reset (Josh Comeau) inline
- `scroll-behavior: smooth`
- Sistema de espaçamento base 8px via CSS variables
- Escala tipográfica consistente via CSS variables
- `lang="pt-BR"`, meta viewport, semântico
- `<meta charset="UTF-8">`

## Regras Globais de Copy na Página

**NUNCA usar travessão (—) em copy.** Substituir por "e", vírgula, dois-pontos ou reescrever.

**Errado:** "Como calcular o valor real — para nunca mais aceitar um preço errado"
**Certo:** "Como calcular o valor real para nunca mais aceitar um preço errado"

---

## Estrutura da Página de Vendas

### Header Fixo
Logotipo + botão CTA pequeno. Glassmorphism. Logo à esquerda, CTA à direita.

### Seção 1 — Primeira Dobra (OBRIGATÓRIO: vídeo visível sem scroll)

**Objetivo:** Fazer a pessoa assistir ao vídeo de vendas.

1. **Headline (Premissa)** — vende uma ideia, não o produto. Não pode estar no imperativo. Sem tom de promessa direta.
   - Padrões válidos: "Quem vende barato vende menos", "É possível...", "Como...", "Qualquer pessoa pode"
   - Proibido: imperativos ("Pare de...", "Aprenda...", "Descubra..."), perguntas no gancho, promessas vagas

2. **Subheadline** — reforça a premissa. 1-2 linhas. Tom analítico.

3. **3 bullets** — cada bullet = urgência oculta + decorado. Numerados (1, 2, 3), não ícones de check.
   - Exemplo: "Como calcular o valor real de cada leitura para nunca mais aceitar um preço que te deixa no prejuízo"

4. **Vídeo** — OBRIGATÓRIO. Usar `aspect-ratio: 16/9`, encostado na borda inferior da seção.
   - Se tiver link do YouTube: extrair o ID e usar `/embed/ID`
   - Se não tiver: placeholder visual `[Insira aqui o embed do seu vídeo]`

**Não incluir botão CTA na primeira dobra.** O objetivo é assistir ao vídeo.

### Seção 2 — Botão de Compra

- Preço em destaque grande
- Botão CTA principal (verde ou laranja, máximo contraste)
- Selos de confiança: compra segura, garantia, acesso imediato, dados protegidos

### Seção 3 — Paliativo

**Incluir somente se houver paliativo.** Mostrar por que as tentativas anteriores falham usando cards com citação em itálico + label.

### Seção 4 — Resultados Concretos

Depoimentos com resultado quantificável em destaque (badge com o resultado). Fundo com imagem + overlay escuro. Cards glassmorphism.

### Seção 5 — Suporte

Cobrir: como e quando recebe o acesso, formatos disponíveis, canal de suporte, garantia. Grid de cards com ícone + título + descrição.

### Seção 6 — Bônus

Cada bônus com: badge "Bônus X", nome, descrição do que entrega, valor original riscado + "Incluso hoje".

### Seção 7 — Autoridade do Criador

Foto + nome + posicionamento + bio em 2 parágrafos + lista de credenciais. Placeholder instrucional se não tiver foto.

### Seção 8 — Para Quem É

Grid de 2 colunas: "É pra você se" (checks verdes) e "Não é pra você se" (X vermelhos). Extrair perfis da identidade do consumidor. Fundo escuro.

### Seção 9 — Lógica do Método

Passos numerados + grid de entregáveis detalhados com ícone, título, descrição e lista de tópicos. **2 colunas no desktop, 1 no mobile** (nunca 3 colunas).

### Seção 10 — Depoimentos + Reflexão Emocional

Mínimo 4 depoimentos. Fundo com imagem + overlay. Após os depoimentos, bloco de reflexão emocional: headline que conecta com a identidade da pessoa + parágrafo + botão CTA.

### Stack de Valor + Botão

Tabela com todos os itens e valores individuais. Total riscado. Preço real em destaque. Botão CTA. Selos de confiança.

### FAQ

5-8 perguntas baseadas nas objeções reais da identidade do consumidor. Accordion funcional em JS. Respostas diretas.

### Seção Final — Resumindo

Headline que sintetiza a transformação. Parágrafo recapitulando o que está incluso. Preço. Botão CTA. Selos.

### Rodapé

Copyright + links de termos e privacidade.

### CTA Flutuante Mobile

Aparece ao rolar no mobile. Some quando a pessoa chega na seção final.

---

## Página de Captura

1. Header com logo
2. Hero com headline + formulário (nome, email, WhatsApp)
3. Benefícios (3-4 bullets com ícones)
4. O que vai receber
5. Sobre o autor
6. CTA final

## Página de Obrigado

1. Header com logo
2. Confirmação do cadastro/compra
3. Próximos passos claros
4. Instruções de acesso
5. CTA secundário (grupo WhatsApp, redes sociais)

---

## Checklist Pré-Entrega (verificar ANTES de salvar)

**Texto e idioma:**
- [ ] TODOS os textos em português com acentos corretos
- [ ] Revisar headlines, parágrafos, botões, FAQs, footer, labels — tudo

**Estrutura:**
- [ ] Header com logotipo no topo da página
- [ ] HTML válido, semântico, `lang="pt-BR"`, `charset="UTF-8"`

**Design e layout:**
- [ ] TODAS as fontes são SANS-SERIF (heading E body)
- [ ] Fontes escolhidas da biblioteca aprovada
- [ ] Cards de conteúdo com min-width >= 320px no grid
- [ ] Texto dentro de cards com font-size >= 0.95rem
- [ ] Padding interno de cards >= 28px
- [ ] Entregáveis/módulos em grid de 2 colunas (NÃO 3)
- [ ] NÃO parece design Lovable/v0

**Variedade visual:**
- [ ] Pelo menos 4 tipos diferentes de fundo entre as seções
- [ ] Pelo menos 2 seções com imagem de fundo (Picsum + overlay)
- [ ] Seções visualmente distintas
- [ ] Pelo menos 1 divisor decorativo (wave SVG, linha, mudança abrupta)
- [ ] Pelo menos 3 animações de scroll

**Conversão:**
- [ ] Botão CTA com contraste máximo
- [ ] Depoimentos com avatar (pravatar.cc)
- [ ] FAQ com accordion funcional em JS
- [ ] Smooth scroll ativado
- [ ] Mobile responsivo (375px)
- [ ] CTA flutuante no mobile

---

## B4. Inserir Pixel (se configurado)

Leia `.env` e verifique `META_PIXEL_ID`. Se existir, insira o snippet do Facebook Pixel no `<head>`:
- Captura: evento `Lead` no submit
- Vendas: evento `ViewContent` no carregamento
- Obrigado: evento `Purchase` ou `CompleteRegistration`

## B5. Salvar

- `produtos/{ativo}/entregas/paginas/vendas-[produto].html`
- `produtos/{ativo}/entregas/paginas/captura-[produto].html`
- `produtos/{ativo}/entregas/paginas/obrigado-[produto].html`

**SEMPRE** criar também `index.html` como cópia do arquivo gerado na mesma pasta.

## B6. Publicar na Vercel

```
Sua página está salva. Quer publicar online agora para ter um link para compartilhar?

1. Sim, quero publicar
2. Não agora

Digite o número:
```

Se escolher **2**, informar o caminho do arquivo e ir para o Próximo Passo.

Se escolher **1**, executar o deploy de forma autônoma:

**Passo 1 — Verificar se a conta está conectada:**
```bash
npx vercel whoami
```

**Se retornar erro** (não autenticado):
```
Para publicar, você precisa de uma conta gratuita na Vercel.
São 3 passos — leva menos de 5 minutos:

1. Acesse vercel.com e crie a conta (recomendo entrar com GitHub)
2. Clique no seu avatar → Settings → Tokens → Create Token
   Dê o nome "cursor", clique em Create e copie o token (aparece só uma vez)
3. Cole o token aqui — eu conecto e publico tudo automaticamente
```

Quando o usuário colar o token:
- Salvar em `.env`: `VERCEL_TOKEN=<token>`
- Executar: `npx vercel --token <token> produtos/{ativo}/entregas/paginas --prod --yes --name {slug-do-produto}`

**Se conta conectada:**
```bash
npx vercel produtos/{ativo}/entregas/paginas --prod --yes --name {slug-do-produto}
```

Informar ao usuário:
```
Sua página está online em: https://{slug-do-produto}.vercel.app

[Se usou link do YouTube]: Para o vídeo aparecer, ative a incorporação:
studio.youtube.com → Conteúdo → editar o vídeo → Mais opções → Permitir incorporação → Salvar
```

#### Atualizar a página (nova versão após edições)
```bash
npx vercel produtos/{ativo}/entregas/paginas --prod --yes --name {slug-do-produto}
```

## B7. Próximo Passo

"Use `/anuncio` para criar anúncios que levem tráfego a essa página."
