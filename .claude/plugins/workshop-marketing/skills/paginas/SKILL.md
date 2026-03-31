---
name: paginas
description: >
  Base de conhecimento para criação de páginas web profissionais.
  Inclui estrutura 8D de página de vendas, biblioteca de 28 templates HTML/DESIGN
  e padrões visuais. Acionada automaticamente pelo command /pagina-de-vendas.
---

# Páginas — Base de Conhecimento

## Regras de Fluxo para Páginas

1. **Coletar TUDO antes de gerar copy.** Tudo o que for necessário para a página deve ser perguntado ANTES de gerar qualquer copy. Não gerar copy assumindo dados que não foram coletados ou confirmados.
2. **Validar a copy com o usuário ANTES de gerar o HTML.** Mostrar toda a copy textual, pedir aprovação, e só depois gerar o arquivo HTML.
3. **Exceção de exibição:** O HTML não é mostrado ao usuário (seria confuso). Salvar direto e informar o caminho do arquivo.

## Estrutura 8D (Página de Vendas VTSD)

1. **Header** — Logotipo + CTA pequeno (opcional)
2. **Primeira Dobra (Hero)** — Premissa (headline) + subheadline + 3 bullets (Urgência Oculta + Decorado) + vídeo + CTA
3. **Problema/Dor** — Dor amplificada com cenas do cotidiano
4. **Paliativo** — O que já tentaram e por que falhou
5. **Solução/Método** — Apresentação da Furadeira (macroetapas + microetapas)
6. **Para Quem É / Não É** — Listas com ícones check/X
7. **Entregáveis** — Lista completa com metáforas de valor (grid 2 colunas)
8. **Bônus** — 3 bônus estratégicos com valor individual
9. **Stack de Valor** — Ancoragem visual (valor total vs preço real)
10. **Prova Social** — Depoimentos com foto e resultado específico
11. **Garantia** — Tipo + prazo + selo visual
12. **FAQ** — Accordion funcional (5-8 objeções da persona)
13. **Oferta Final (CTA)** — Ancoragem de valor + preço + parcelamento + CTA grande
14. **Rodapé** — Termos, privacidade, copyright

## Regras Universais

- **Texto SEMPRE em pt-BR com acentos** (Módulos, não Modulos)
- **Header com logotipo obrigatório** em toda página
- **TODAS as fontes DEVEM ser sans-serif** — heading E body. Fontes serifadas são PROIBIDAS em qualquer parte da página (heading, body, labels, tudo). Serifadas dão cara de template genérico de IA e prejudicam leitura em telas.
- **Biblioteca de fontes aprovadas** (todas do Google Fonts CDN, todas sans-serif):

### Fontes Sans-Serif Aprovadas (Google Fonts CDN)

**PROIBIDO usar fontes serifadas** — Playfair Display, Fraunces, Noto Serif, Lora, Merriweather, Source Serif, Instrument Serif, Cormorant, Libre Baskerville, EB Garamond, Crimson Text e qualquer outra serif estão BANIDAS.

#### Heading (display/títulos) — Escolher 1

| Fonte | Estilo | Ideal para | Pesos |
|---|---|---|---|
| **Space Grotesk** | Geométrica moderna | Tech, SaaS, inovação | 400, 500, 700 |
| **Sora** | Geométrica suave | Startups, apps, moderno | 400, 600, 700, 800 |
| **Outfit** | Geométrica limpa | Clean, versátil, qualquer nicho | 400, 500, 600, 700, 800 |
| **Plus Jakarta Sans** | Humanista moderna | Premium, coaching, educação | 500, 600, 700, 800 |
| **Montserrat** | Geométrica clássica | Negócios, finanças, autoridade | 500, 600, 700, 800, 900 |
| **Raleway** | Elegante geométrica | Moda, beleza, lifestyle | 400, 500, 600, 700, 800 |
| **Poppins** | Geométrica arredondada | Amigável, saúde, educação | 400, 500, 600, 700, 800, 900 |
| **Urbanist** | Neo-grotesca | Imobiliário, luxo moderno | 400, 500, 600, 700, 800, 900 |
| **Bebas Neue** | Condensada bold | Marketing, impacto, headlines | 400 |
| **Fjalla One** | Condensada impacto | Títulos curtos, esporte, energia | 400 |
| **Albert Sans** | Grotesca variável | Versátil, clean, minimalista | 400, 500, 600, 700, 800 |
| **General Sans** (Fontshare) | Neo-grotesca | Premium, editorial moderno | 400, 500, 600, 700 |
| **Bricolage Grotesque** | Grotesca expressiva | Criativo, artsy, artesanato | 400, 600, 700, 800 |
| **Lexend** | Otimizada para leitura | Educação, acessibilidade | 400, 500, 600, 700 |
| **Figtree** | Amigável geométrica | Pet, saúde, bem-estar | 400, 500, 600, 700, 800 |
| **Clash Display** (Fontshare) | Display bold | Headlines de impacto | 400, 500, 600, 700 |
| **Cabinet Grotesk** (Fontshare) | Geométrica moderna | Tech, startup | 400, 500, 700, 800 |

#### Body (texto corrido) — Escolher 1

| Fonte | Estilo | Ideal para | Pesos |
|---|---|---|---|
| **DM Sans** | Humanista moderna | Versátil, qualquer nicho | 400, 500, 600, 700 |
| **Manrope** | Geométrica legível | Tech, SaaS, premium | 400, 500, 600, 700 |
| **Nunito** | Arredondada acolhedora | Saúde, educação, feminino | 400, 500, 600, 700 |
| **Source Sans 3** | Neo-grotesca funcional | Finanças, negócios, formal | 400, 500, 600, 700 |
| **Inter** | Neo-grotesca neutra | Tech, dados, interfaces | 400, 500, 600, 700 |
| **Outfit** | Geométrica clean | Versátil, pode ser heading e body | 400, 500, 600 |
| **Plus Jakarta Sans** | Humanista moderna | Premium, coaching | 400, 500, 600 |
| **Nunito Sans** | Companheira do Nunito | Saúde, bem-estar | 400, 500, 600, 700 |
| **Work Sans** | Grotesca compacta | Negócios, produtividade | 400, 500, 600 |
| **Rubik** | Arredondada moderna | Amigável, apps | 400, 500, 600 |
| **Karla** | Grotesca levemente humanista | Blogs, conteúdo longo | 400, 500, 600, 700 |
| **Archivo** | Neo-grotesca sólida | Estabilidade, finanças | 400, 500, 600, 700 |
| **Red Hat Display** | Display legível | Moderno, clean | 400, 500, 600, 700 |
| **Lexend** | Otimizada para leitura rápida | Educação, conteúdo denso | 400, 500, 600 |
| **Figtree** | Geométrica amigável | Pet, wellness, família | 400, 500, 600 |
| **Geist** (Vercel) | Mono-inspirada | Dev tools, tech, startup | 400, 500, 600, 700 |

#### Combinações Recomendadas por Nicho

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

**Regra**: Heading e body podem ser a mesma fonte (variando peso) ou fontes diferentes. Ambas DEVEM ser sans-serif.

- **Grids de 2 colunas** para entregáveis (NÃO 3 — evita texto apertado)
- **Cards com min-width 320px**, padding 28px+, font-size 0.95rem+
- **4+ tipos de fundo** alternando entre seções (claro, escuro, imagem+overlay, gradiente, textura)
- **2+ seções com imagem de fundo** (Picsum + overlay ou CSS artístico)
- **NÃO parecer Lovable/v0** — sem cards brancos idênticos em fundo bege

## Design System e Montagem

### Fluxo de Geração (OTIMIZADO)

1. Ler **`references/design-system-components.md`** — contém TODOS os padrões CSS pré-compilados (variáveis, componentes, animações, responsivo). Este arquivo ÚNICO substitui a leitura de templates individuais.
2. Adaptar as CSS variables à paleta e fontes do nicho
3. Montar a página seção por seção usando os componentes do design system
4. Preencher a copy com dados do perfil do negócio e identidade do consumidor

**NÃO ler templates individuais em `references/templates/`.** Usar apenas o design system compilado. Os templates existem como arquivo de referência, mas o design system já contém todos os padrões extraídos.

### Padrões Visuais (aplicar a todas as seções)

- **CSS puro com custom properties** — preferir CSS puro. Tailwind CDN apenas se necessário
- **Material Symbols Outlined** para ícones
- **No-Line Rule** — sem bordas 1px entre seções. Usar mudanças tonais e espaçamento
- **Glassmorphism** — `backdrop-filter: blur() + rgba` para navs e cards sobrepostos
- **Espaçamento como design** — separação por tom de fundo, não por linhas
- **Hierarquia tipográfica dramática** — heading 48-56px vs body 15-16px
- **NUNCA usar badges/tags** — Proibido usar elementos tipo pill/badge acima do headline

### Estilos Visuais Disponíveis (referência)

| Estilo | Tema | Característica |
|---|---|---|
| glass_escuro | Escuro | Glassmorphism, shimmer, refinado |
| flat_claro | Claro | Bordas flat, warm/dourado |
| teal_claro | Claro | Teal/verde, botão pill verde |
| purple_escuro | Escuro | Roxo, moderno |
| minimal_claro | Claro | Minimalista, neutro |

Templates individuais em `references/templates/` servem como referência visual se precisar consultar um padrão específico. Mas para geração, usar o design system compilado.

## Paletas por Nicho

| Nicho | Principal | Secundária | CTA |
|---|---|---|---|
| Finanças | Azul escuro #1a365d | Dourado #d4a72c | Verde #38a169 |
| Saúde | Verde #2f855a | Branco | Laranja #dd6b20 |
| Marketing | Roxo #6b46c1 | Azul #3182ce | Amarelo #ecc94b |
| Dev Pessoal | Azul #2b6cb0 | Branco | Laranja #ed8936 |
| Educação | Azul #2c5282 | Verde #2f855a | Laranja #dd6b20 |
| Beleza | Rosa #d53f8c | Dourado #d69e2e | Preto #1a202c |
| Artesanato | Dourado #d4a574 | Marrom #2d1810 | Verde #38a169 |
| Tech | Escuro #0c0c1d | Azul elétrico #667eea | Verde #38a169 |
| Coaching | Terracota #c4603c | Creme #fdf6ec | Laranja #ed8936 |
| Feminino | Rose #f5576c | Nude #fdf6ec | Dourado #d69e2e |

## Imagens Contextuais (OBRIGATÓRIO)

**NUNCA usar imagens genéricas.** Toda imagem na página deve ter relação semântica direta com o conteúdo da seção onde está inserida. Imagens decorativas sem significado dão cara de template de IA.

### Processo de Seleção (3 Etapas)

**Etapa 1 — Análise Semântica do Conteúdo**

Antes de escolher qualquer imagem, analisar o texto da seção e extrair:
- **Objeto central** — O que está sendo descrito? (ex: peça de crochê, feira, celular)
- **Emoção dominante** — O que a pessoa sente? (ex: frustração, vergonha, esperança)
- **Cenário físico** — Onde a cena acontece? (ex: mesa de trabalho, barraca de feira, sofá à noite)

**Etapa 2 — Mapeamento de Palavras-Chave**

Traduzir a análise em 2-3 keywords em inglês para busca de imagens. Ser específico, não genérico.

| Conteúdo da Seção | Errado (genérico) | Certo (contextual) |
|---|---|---|
| Postar no Instagram sem resultado | `phone` | `woman,phone,frustrated` |
| Vender em feira de artesanato | `market` | `craft,fair,handmade,stall` |
| Pedir para família divulgar | `friends` | `woman,sharing,phone,awkward` |
| Baixar preço para competir | `coins` | `price,tag,discount,loss` |
| Crochê de madrugada | `night` | `crochet,night,lamp,tired` |
| Peças acumuladas sem vender | `storage` | `handmade,products,shelf,unsold` |
| Síndrome do impostor em reunião | `office` | `meeting,room,anxious,silent` |
| Salário estagnado | `money` | `paycheck,calculator,worried` |
| Horas de trabalho por centavos | `work` | `hands,crafting,thread,table` |

**Etapa 3 — Construção da URL**

**Opção principal — Picsum com seed descritivo (SEMPRE funciona):**
```
https://picsum.photos/seed/{keyword1-keyword2-keyword3}/{largura}/{altura}
```
Exemplo: `https://picsum.photos/seed/crochet-night-lamp/600/300`

O seed é formado pelas keywords separadas por hífen. Mesma seed = mesma imagem (consistência entre reloads).

**Opção alternativa — Unsplash com ID específico de foto:**
```
https://images.unsplash.com/photo-{ID}?w=600&h=300&fit=crop&q=80
```
Só usar quando souber o ID exato da foto. Exemplo: `photo-1601985705806-5b9a71f6004f`

**PROIBIDO usar `source.unsplash.com`** — esse serviço foi descontinuado e as imagens não carregam.

### Regras de Uso de Imagens

1. **Mínimo 2 keywords por imagem** — nunca usar uma palavra só (ex: `phone`). Sempre combinar objeto + contexto (ex: `woman,phone,frustrated`)

2. **Keywords devem vir do texto da seção** — ler o parágrafo do card/bloco e extrair os substantivos e adjetivos mais descritivos

3. **Adaptar ao nicho do produto:**
   - Artesanato → `handmade`, `craft`, `yarn`, `thread`, `hands`, `table`
   - Gastronomia → `kitchen`, `baking`, `cake`, `ingredients`, `apron`
   - Finanças → `calculator`, `spreadsheet`, `bills`, `wallet`
   - Saúde → `wellness`, `exercise`, `tired`, `energy`
   - Tech → `laptop`, `code`, `screen`, `developer`
   - Educação → `classroom`, `books`, `studying`, `notebook`
   - Beleza → `skincare`, `mirror`, `routine`, `products`

4. **Tratamento visual conforme o design system:**

   | Estilo da página | Filtro na imagem |
   |---|---|
   | Light/clean | `opacity: 0.85` ou sem filtro |
   | Flat B&W | `filter: grayscale(100%); opacity: 0.6` |
   | Dark mode | `filter: brightness(0.35-0.4)` + gradient overlay escuro |
   | Warm/dourado | `filter: sepia(0.2) saturate(0.9)` |
   | Teal/vibrante | `filter: saturate(1.15)` + gradient overlay branco na base |

5. **Imagens de fundo de seção** — usar keywords mais amplas e emocionais (ex: `woman,workshop,creative,warm`), com overlay forte para legibilidade do texto

6. **Imagens em cards** — usar keywords específicas do conteúdo daquele card individual

### Exemplo Completo (Seção Problema/Dor — Crochê)

```
Card "Horas de trabalho por centavos":
  Texto: "Você passa a tarde inteira fazendo uma peça e vende por menos do que gastou em linha"
  Análise: mãos trabalhando crochê, mesa, linha, cansaço
  Keywords: hands,crochet,yarn,table
  URL: https://picsum.photos/seed/hands-crochet-yarn-table/600/300

Card "A pechincha que dói":
  Texto: "A cliente olha, elogia, pergunta o preço e some"
  Análise: conversa de venda, celular com mensagem, desânimo
  Keywords: phone,message,disappointed,woman
  URL: https://picsum.photos/seed/phone-message-disappointed/600/300

Card "Peças guardadas no armário":
  Texto: "Peças lindas acumulando poeira na prateleira"
  Análise: produtos handmade na estante, sem comprador
  Keywords: handmade,shelf,products,unused
  URL: https://picsum.photos/seed/handmade-shelf-products-unused/600/300

Card "Crochê de madrugada":
  Texto: "Trabalhando enquanto a família dorme"
  Análise: noite, abajur, mãos cansadas, solidão
  Keywords: night,lamp,hands,crafting
  URL: https://picsum.photos/seed/night-lamp-hands-crafting/600/300
```

## Referências

- **`references/design-system-components.md`** — **ARQUIVO PRINCIPAL** — CSS variables, componentes, animações, responsivo. Ler este arquivo substitui a leitura de todos os templates individuais.
- `references/estruturas-pagina.md` — Seções por tipo de página, fundos por seção, paletas por nicho
- `references/cdn-design-resources.md` — CDNs, fontes, ícones, animações, gradientes
- `references/performance-otimizacao.md` — Auditoria e otimização (meta: 90+ mobile / 100 desktop)
- `references/templates/` — Templates HTML individuais por seção/estilo (referência visual, NÃO ler durante geração)
