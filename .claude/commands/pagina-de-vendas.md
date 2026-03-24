---
name: workshop-marketing:pagina-de-vendas
description: Criar páginas web profissionais completas (vendas 8D, captura ou obrigado) com HTML/CSS responsivo, design moderno e copy persuasiva baseada na metodologia VTSD.
---

# Página de Vendas — Gerador de Páginas Profissionais

Cria páginas HTML completas e profissionais usando a estrutura 8D do VTSD.

## Usage

```
/pagina-de-vendas
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md` e `meu-negocio/idconsumidor.md` se existir.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Tipo de Página:**

Pergunta 1:
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

Se escolheu **1. Vendas (8D):**
```
Quais os módulos ou entregáveis do produto?
(ex: "5 módulos de vídeo + planilhas + grupo VIP")
```
```
Tem depoimentos de alunos? Se sim, passe 3-5 com nome e resultado.
(ex: "João, faturou R$10k no primeiro mês")
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
Qual o preço e parcelamento?
(ex: "R$497 ou 12x R$47")
```
```
Tem bônus? Quais?
(ex: "Grupo VIP, planilha de métricas, aula extra")
```
```
Link de checkout (Hotmart, Kiwify)?
(ex: "https://pay.hotmart.com/ABC123" ou "ainda não tenho")
```

Se escolheu **2. Captura** ou **3. Obrigado**, verificar ANTES se já existem páginas criadas em `entregas/paginas/`. Se existirem, perguntar:

```
Encontrei estas páginas já criadas:
[listar arquivos encontrados em entregas/paginas/]

Quer que a nova página siga o mesmo visual (cores, fontes, estilo)?

1. Sim, manter a identidade visual da página existente
2. Não, quero um visual diferente

Digite o número:
```

Se escolher **1**, ler o HTML da página existente para extrair: paleta de cores, fontes, padrões de componentes, estilo de botões e cards. Aplicar a mesma identidade visual na nova página para manter consistência entre páginas do funil.

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

Pergunta:
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

### 3. Mixagem de Templates (OBRIGATÓRIO)

**NUNCA use um template sozinho.** Sempre selecione **2-3 templates** da biblioteca e **misture** os melhores elementos de cada um para criar um resultado orgânico e único. Copiar um template inteiro gera resultado genérico.

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

De cada template, extraia pelo menos **2-3 elementos únicos**. Exemplos do que cada tipo de template oferece:

| Template | O que extrair |
|---|---|
| `terra_trama` | Assimetria intencional, imagens sobrepostas, tonal layering sem sombras |
| `artes_elegance` | Big Lead technique (headline gigante + body contrastante), ghost borders, glassmorphism |
| `ateli_moderno` | Micro-labels Vogue (10px uppercase, 0.35em tracking), imagens grayscale→cor no hover |
| `vtsd_ateli_lucrativo` | Skewed background shapes, staggered image grids, grid-line texture como overlay |
| `landing_page_croch_lucrativo` | Bento grid no problema, floating testimonial cards, progress bars em cards |
| `hyperion_growth` | Neon glow effects, dark void backgrounds, kinetic hover states |
| `zen_moderno` | Whitespace extremo, transições lentas, paleta muted com 1 acento |
| `echelon_executive` | Tipografia de autoridade, dados em destaque, grid formal com quebre inesperada |

**Passo 4 — Monte a página combinando:**
- **Layout e estrutura** do template principal (hero, grids, seções)
- **Sistema de design** do template DESIGN.md (cores, fontes, espaçamento, regras como No-Line)
- **Componentes visuais** do template complementar (cards, hovers, texturas, divisores)
- **Paleta e fontes** definidas pelo usuário na entrevista (adaptar tudo à paleta escolhida)

#### Regra de Ouro da Mixagem

O resultado final NÃO deve parecer nenhum template individual. Se alguém abrir o template original e a página gerada, devem parecer projetos diferentes. A mixagem existe para criar **identidade visual única**, não para copiar.

**Padrões obrigatórios da mixagem (aplicar SEMPRE):**
- Use **Tailwind CDN** com config customizado OU CSS puro com variables — escolha um
- Use **Material Symbols Outlined** ou **Phosphor Icons** para ícones
- **No-Line Rule**: sem bordas 1px entre seções. Usar mudanças tonais e espaçamento
- **Glassmorphism** para navs e cards sobrepostos: `backdrop-filter: blur() + rgba`
- **Assimetria intencional**: layouts não são 100% simétricos
- **Micro-labels**: pelo menos na nav e em badges, usar texto 10-11px uppercase com tracking largo
- **Tonal layering**: profundidade por camadas de cor, não por drop shadows pesados
- **Editorial spacing**: espaçamento generoso (80-96px) entre seções principais

### 4. Geração

Consulte a base de design em `skills/paginas/references/cdn-design-resources.md` para CDNs e padrões visuais. Consulte `skills/paginas/references/estruturas-pagina.md` para estrutura das seções.

Se existir `entregas/copy-pagina/copy-[produto].md`, use a copy pronta. Se não existir, gere a copy durante a construção da página.

---

## REGRAS CRÍTICAS DE QUALIDADE

### Regra #1: Texto SEMPRE em português com acentos

**OBRIGATÓRIO:** Todo texto visível na página DEVE estar em português do Brasil com acentos corretos.

- "Módulos" e NÃO "Modulos"
- "Precificação" e NÃO "Precificacao"
- "Vídeo" e NÃO "Video"
- "Método" e NÃO "Metodo"
- "Você" e NÃO "Voce"
- "Não" e NÃO "Nao"
- "É" e NÃO "E"
- "Já" e NÃO "Ja"
- "Também" e NÃO "Tambem"
- "Negócio" e NÃO "Negocio"

Use o charset UTF-8 no `<meta charset="UTF-8">` e garanta que TODOS os textos — headlines, parágrafos, botões, labels, FAQs, depoimentos, footer — tenham acentuação correta da língua portuguesa.

**Antes de salvar, revise TODOS os textos da página e corrija qualquer palavra sem acento.**

### Regra #2: Logotipo no topo OBRIGATÓRIO

Toda página DEVE ter um logotipo/marca no topo antes do hero ou como parte do header.

Estrutura:
```html
<header class="site-header">
  <div class="container">
    <div class="logo">
      <!-- Opção 1: Imagem (quando o aluno tiver logo) -->
      <img src="[caminho-do-logo]" alt="Nome do Produto" class="logo-img">

      <!-- Opção 2: Logo texto estilizado (padrão quando não há imagem) -->
      <span class="logo-text">Nome do Produto</span>
    </div>
  </div>
</header>
```

Regras do header:
- Fundo transparente ou cor sólida que combine com o hero
- Logo alinhado à esquerda
- Pode incluir um botão CTA pequeno à direita (ex: "Quero me inscrever")
- No mobile, centralizar o logo
- Placeholder instrucional: `[Insira seu logotipo aqui — tamanho recomendado: 180x50px]`
- Quando não houver logo, usar o nome do produto como texto estilizado com a fonte heading

### Regra #3: Grids e cards NÃO podem quebrar texto

**PROIBIDO** grids que cortam ou apertam texto em telas médias.

Regras de grid:
- Cards com texto descritivo: `min-width: 320px` no grid (NUNCA menor que 300px)
- Se o card tem lista de itens: usar `grid-template-columns: repeat(auto-fit, minmax(340px, 1fr))`
- Se o grid tem 3+ cards: no mobile cai para 1 coluna, no tablet pode ter 2
- Texto dentro de card: NUNCA menor que `font-size: 0.95rem` (15.2px)
- Padding interno dos cards: mínimo 28px em todos os lados
- Para seções como "Entregáveis" ou "Módulos" com listas longas: usar layout de 2 colunas (`1fr 1fr`) no desktop, 1 coluna no mobile — NÃO usar 3 colunas que apertam o texto
- Testar mentalmente: "esse texto cabe confortavelmente nessa largura?"

Exemplo correto:
```css
/* Entregáveis — 2 colunas no desktop, 1 no mobile */
.entregaveis-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 24px;
}
```

Exemplo ERRADO (evitar):
```css
/* NUNCA: 3 colunas apertadas com texto longo */
.entregaveis-grid {
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

### Regra #4: NÃO parecer design genérico de IA

Evitar padrões que identificam páginas como "feitas por IA" (Lovable, v0, Claude Code genérico):

**PROIBIDO (cara de IA/Lovable):**
- Fontes serifadas como padrão para todos os projetos (Playfair, Fraunces, Lora para body)
- Gradiente roxo-azul em fundo branco
- Cards brancos arredondados idênticos em fundo bege/cinza claro
- Espaçamento uniforme e previsível entre todas as seções
- Paleta pastel tímida sem contraste forte
- Layout 100% simétrico sem surpresa visual
- Todas as seções com o mesmo padrão visual (fundo claro → card → fundo claro → card)
- Ícones dentro de quadrados arredondados com fundo pastel (típico Lovable)
- Tudo flat sem texturas, imagens de fundo ou profundidade
- Fonte serifada no body text (dificulta leitura em telas)

**OBRIGATÓRIO (cara de profissional de verdade):**
- **TODAS as fontes sans-serif** — heading E body. Serifadas são PROIBIDAS
- Escolher da biblioteca aprovada em SKILL.md (17 opções de heading, 16 de body)
- Seções visualmente DIFERENTES entre si (ver Regra #5)
- Imagens de fundo em pelo menos 2 seções (ver Regra #6)
- Contraste forte entre seções (escura → clara → imagem → colorida)
- Elementos visuais que quebram a monotonia: badges, counters, aspas grandes, divisores decorativos
- Hover states que surpreendem (não só mudar cor — mover, escalar, revelar)

### Regra #5: Seções DEVEM ser visualmente diferentes entre si

Cada seção da página deve ter uma identidade visual própria. PROIBIDO repetir o mesmo padrão visual.

**Variações obrigatórias de fundo entre seções (alternar pelo menos 4 tipos):**

1. **Fundo sólido claro** — branco ou off-white (`#fafafa`, `#f8f7f4`)
2. **Fundo sólido escuro** — cor primária escura com texto claro
3. **Fundo com imagem** — imagem de fundo com overlay escuro + texto claro (ver Regra #6)
4. **Fundo com gradiente sutil** — gradiente de 2 cores da paleta
5. **Fundo com textura/padrão** — cor sólida + SVG pattern ou noise sutil via CSS
6. **Fundo colorido vibrante** — cor de destaque como fundo com texto contrastante

**Exemplo de sequência de seções bem variada:**
```
Hero:         Fundo escuro com gradiente + texto claro
Problema:     Fundo claro + cards com borda
Paliativo:    Fundo com imagem + overlay escuro + texto claro
CTA meio:     Fundo cor vibrante (CTA color) + texto branco
Método:       Fundo claro com textura sutil
Para quem:    Fundo escuro sólido + listas
Entregáveis:  Fundo claro + cards grandes
Bônus:        Fundo gradiente sutil
Stack:        Fundo escuro premium
Depoimentos:  Fundo com imagem + overlay + cards flutuantes
Garantia:     Fundo claro com destaque central
FAQ:          Fundo neutro alternado
CTA final:    Fundo escuro com gradiente
```

**Divisores entre seções:**
Use pelo menos 2 tipos de divisores para quebrar a monotonia:
- SVG wave/curve no topo ou base da seção
- Linha decorativa com ícone central
- Mudança abrupta de cor (escuro → claro)
- Borda superior colorida na seção

### Regra #6: Imagens de fundo em seções

Pelo menos **2 seções** da página devem ter imagem de fundo para dar profundidade e profissionalismo.

**Como implementar (sem upload de imagem):**

Opção 1 — Picsum com overlay:
```css
.section-com-imagem {
  background:
    linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
    url('https://picsum.photos/1920/1080?random=1');
  background-size: cover;
  background-position: center;
  background-attachment: fixed; /* efeito parallax */
  color: #fff;
}
```

Opção 2 — Placeholder instrucional com fallback:
```css
.section-com-imagem {
  background:
    linear-gradient(135deg, rgba(45,24,16,0.85), rgba(74,44,26,0.9)),
    url('https://picsum.photos/1920/1080?random=2');
  background-size: cover;
  background-position: center;
  color: #fff;
  position: relative;
}
/* Comentário no HTML: [Substitua pela sua imagem — tamanho recomendado: 1920x1080px] */
```

Opção 3 — CSS gradient artístico (sem imagem externa):
```css
.section-atmosferica {
  background-color: #0a0a0a;
  background-image:
    radial-gradient(at 20% 50%, hsla(28,100%,74%,0.15) 0px, transparent 50%),
    radial-gradient(at 80% 20%, hsla(189,100%,56%,0.08) 0px, transparent 50%),
    radial-gradient(at 50% 80%, hsla(355,85%,60%,0.06) 0px, transparent 50%);
}
```

**Seções recomendadas para imagem de fundo:**
- Paliativo / "O que já tentou" — imagem cria atmosfera emocional
- Depoimentos — foto real transmite autenticidade
- CTA final — imagem de fundo com overlay escuro gera impacto
- "Para quem é" — foto do público-alvo no background

**Temas de imagem por nicho (para Picsum ou instrução ao usuário):**
- Finanças: escritório, gráficos, paisagem urbana
- Saúde: natureza, alimentos, exercício
- Educação: livros, sala de aula, formatura
- Artesanato: mãos trabalhando, tecidos, ateliê
- Marketing: laptop, café, workspace criativo
- Feminino: flores, lifestyle, moda

**IMPORTANTE:** Sempre usar `loading="lazy"` em imagens. Para imagens de fundo CSS, usar fallback de cor sólida caso a imagem não carregue.

---

## Recursos CDN permitidos (arquivo único, sem build)

Cada página DEVE usar:

- **Google Fonts** — combinação heading + body (consultar lista em cdn-design-resources.md)
- **1 biblioteca de ícones** — Phosphor Icons (recomendado), Lucide ou Tabler Icons via CDN
- **AOS (Animate on Scroll)** — para animações de entrada nas seções. Ou IntersectionObserver puro em CSS/JS
- **Avatares para depoimentos** — pravatar.cc ou DiceBear quando não houver fotos reais
- **Placeholders de imagem** — Lorem Picsum com tema relacionado ao nicho, ou divs instrucionais

## Escolha de fontes por nicho

**REGRA: TODAS as fontes DEVEM ser sans-serif** — heading E body. Fontes serifadas são PROIBIDAS em qualquer parte da página. Serifadas (Playfair, Fraunces, Noto Serif, Lora, Merriweather, Instrument Serif, etc.) dão cara de template de IA e prejudicam leitura em telas.

Consulte a lista completa de fontes aprovadas em `skills/paginas/SKILL.md` → "Fontes Sans-Serif Aprovadas".

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

## Paletas por nicho

- **Finanças**: Azul marinho #1e3a5f + Dourado #d4a574 + CTA Verde #38a169
- **Saúde**: Verde #11998e + Branco + CTA Laranja #dd6b20
- **Educação**: Azul #2b6cb0 + Laranja #e07a58 + CTA Laranja #dd6b20
- **Feminino**: Rose #f5576c + Nude #fdf6ec + CTA Dourado #d69e2e
- **Tech**: Escuro #0c0c1d + Azul elétrico #667eea + CTA Verde #38a169
- **Coaching**: Terracota #c4603c + Creme #fdf6ec + CTA Laranja #ed8936
- **Artesanato**: Dourado #d4a574 + Marrom #2d1810 + CTA Verde #38a169

## Padrão técnico HTML

- Arquivo HTML único
- CSS em `<style>` (CSS custom properties para cores, fontes, espaçamento)
- JS em `<script>` no final do body
- CDNs permitidos: Google Fonts, 1 lib de ícones, AOS
- Modern CSS Reset (Josh Comeau) inline
- `scroll-behavior: smooth`
- Sistema de espaçamento base 8px via CSS variables
- Escala tipográfica consistente via CSS variables
- `lang="pt-BR"`, meta viewport, semântico
- `<meta charset="UTF-8">` para suportar acentos

## Estrutura Completa da Página de Vendas (16 seções)

Cada seção abaixo é OBRIGATÓRIA. Seguir esta ordem e estas regras ao gerar a página.

### Seção 1 — Header

**Elementos:** Logotipo + botão CTA pequeno (opcional)
**Fundo:** Transparente sobre o hero ou cor sólida que combine

Regras:
- Logo alinhado à esquerda (centralizado no mobile)
- Pode ter CTA pequeno à direita (ex: "Quero me inscrever")
- Quando não houver logo: nome do produto como texto estilizado na fonte heading
- Placeholder: `[Insira seu logotipo aqui — 180x50px]`

### Seção 2 — Hero (Primeira Dobra)

**Elementos (nesta ordem):**
1. Headline — Frase principal de impacto (até 12 palavras). Sem ponto de exclamação, sem pergunta. Declaração forte
2. Subheadline — Complementa a headline com mais contexto (1-2 linhas)
3. 3 Bullets — Combinação de Urgência Oculta + Decorado. Cada bullet toca uma dor ou desejo específico
4. CTA principal — Botão grande e contrastante com texto de ação
5. Indicação de vídeo — Espaço para VSL ou placeholder instrucional

**Fundo:** Escuro com gradiente + texto claro

Regras:
- Headline usa a fonte heading em tamanho grande (2.5rem+ no desktop)
- Bullets com ícones para facilitar a leitura rápida
- CTA com cor que contrasta contra o fundo (verde ou laranja)
- No mobile, tudo centralizado e botão ocupa largura toda
- O visitante entende o que é, para quem é e o que ganha SEM rolar a página

### Seção 3 — Vídeo (VSL)

**Elementos:** Embed de vídeo ou placeholder instrucional
**Fundo:** Claro ou continuação do hero

Regras:
- Espaço para embed do YouTube/Vimeo ou placeholder `[Insira seu vídeo de vendas aqui]`
- Proporção 16:9
- Borda sutil ou sombra para destacar
- Pode estar integrado ao hero (dentro da mesma seção) ou ser seção separada
- Se o aluno não tiver vídeo, gerar o placeholder com instrução clara

### Seção 4 — Problema/Dor

**Elementos:** Descrição vívida da dor do público, com cenas do cotidiano
**Fundo:** Claro + cards com borda lateral colorida

Regras:
- Usar frases que a persona diria (extrair de `meu-negocio/persona.md` → "Frases que a persona diria")
- Mostrar situações específicas do dia a dia, não dores genéricas
- Cards com citações em itálico + aspas grandes decorativas
- Tom empático, nunca julgador

### Seção 5 — Agitação (Consequências)

**Elementos:** O que acontece se NÃO resolver o problema
**Fundo:** Imagem de fundo + overlay escuro + texto claro

Regras:
- Amplifica a dor mostrando o futuro sem solução
- Conecta com as Urgências Ocultas (dores + consequências emocionais)
- Texto curto e direto, sem exagero — Light Copy
- Esta seção cria urgência emocional antes de apresentar a solução
- Pode usar contador ou timeline visual ("Daqui a 6 meses...")

### Seção 6 — Solução/Método

**Elementos:** Apresenta o produto como resposta. Furadeira com macroetapas visuais
**Fundo:** Claro com textura sutil

Regras:
- Mostrar as macroetapas do método (extrair de `perfil.md` → Furadeira)
- Cada etapa com número, título e descrição curta
- Layout em cards numerados ou timeline visual
- Fazer a ponte clara: "A dor que você tem → O método resolve → O resultado que você quer"
- Tom de confiança e clareza, não hype

### Seção 7 — Para Quem É

**Elementos:** Lista de perfis ideais com ícone de check verde
**Fundo:** Escuro sólido + texto claro

Regras:
- 4-6 itens descrevendo o público ideal
- Cada item com ícone check + frase que começa com "Você que..."
- Extrair de `persona.md` para ser específico

### Seção 8 — Para Quem NÃO É

**Elementos:** Lista com ícone X vermelho
**Fundo:** Continuação da seção anterior (mesmo fundo escuro)

Regras:
- 3-4 itens que filtram e geram credibilidade
- Tom honesto: "Não é pra quem quer resultado sem esforço"
- Pode ser na mesma seção que "Para Quem É" (grid 2 colunas: check à esquerda, X à direita)

### Seção 9 — Módulos/Conteúdo (Entregáveis)

**Elementos:** Detalhamento do que está incluso no produto
**Fundo:** Claro + cards grandes

Regras:
- Grid de **2 colunas** no desktop, 1 no mobile (NÃO 3 colunas)
- Cada card: ícone + título do módulo + descrição + lista de tópicos
- Cards com min-width 340px e padding 28px+
- Usar metáforas de valor ("A planilha que faz o cálculo por você")

### Seção 10 — Bônus

**Elementos:** Cada bônus com nome, descrição e valor individual em R$
**Fundo:** Gradiente sutil

Regras:
- 2-4 bônus estratégicos
- Cada card com badge "Bônus 1", "Bônus 2"
- Valor original riscado (ex: "Valor: ~~R$ 97~~")
- Se o aluno não especificou bônus, criar bônus coerentes com o produto

### Seção 11 — Stack de Valor

**Elementos:** Lista de tudo incluso + valor individual + total riscado + preço real
**Fundo:** Escuro premium

Regras:
- Tabela ou lista: item → valor em R$
- Total somado (ex: R$ 1.149) riscado
- Preço real em destaque grande + parcelamento
- CTA logo abaixo da oferta
- Selos de segurança + garantia abaixo do botão

### Seção 12 — Depoimentos

**Elementos:** 3-6 depoimentos com foto, nome e resultado específico
**Fundo:** Imagem de fundo + overlay + cards flutuantes

Regras:
- Cada depoimento: avatar (pravatar.cc) + nome + resultado quantificável + texto em itálico
- Estrelas de avaliação (5/5)
- Se o aluno forneceu depoimentos reais, usar. Se não, criar placeholders realistas
- Cards com aspas grandes decorativas

### Seção 13 — Garantia

**Elementos:** Selo visual circular + texto confiante
**Fundo:** Claro com destaque central

Regras:
- Selo visual: círculo com número de dias (7, 15 ou 30)
- Título: "Garantia incondicional de X dias"
- Texto que inverte o risco: "Se não gostar, devolvemos 100% do seu dinheiro"
- Layout: selo à esquerda + texto à direita (centralizado no mobile)

### Seção 14 — FAQ

**Elementos:** 5-8 perguntas frequentes com accordion funcional
**Fundo:** Neutro (off-white ou cinza muito claro)

Regras:
- Perguntas baseadas nas objeções reais da persona (extrair de `persona.md` → Objeções de Compra)
- Accordion em JS: clica na pergunta, abre a resposta
- Respostas curtas, diretas, sem enrolação
- Ícone de seta que gira ao abrir/fechar

### Seção 15 — CTA Final (Último Empurrão)

**Elementos:** Headline emocional + preço + parcelamento + botão grande + selos de confiança
**Fundo:** Escuro com gradiente

Regras:
- Headline que reforça a transformação (não repetir a do hero)
- Preço com parcela em destaque (ex: "12x de R$ 29,04")
- Preço à vista menor abaixo
- Botão CTA grande e contrastante
- Selos: "Compra segura", "X dias de garantia", "Até 12x sem juros"
- Senso de urgência sutil, sem countdown falso

### Seção 16 — Rodapé

**Elementos:** Copyright + links de termos e privacidade
**Fundo:** Escuro sólido (cor primária)

Regras:
- Texto pequeno centralizado
- Links: Termos de uso | Política de privacidade
- Ano atual + nome do produto

### Regras Globais da Página

- **Mínimo 3 CTAs** espalhados: após o hero, no stack de valor e no CTA final
- **CTA flutuante no mobile** — aparece ao rolar, some perto do CTA final
- **Preço com ancoragem** — valor original riscado + preço real em destaque
- **Botão CTA sempre verde ou laranja** — máximo contraste contra o fundo
- **2+ seções com imagem de fundo** — para dar profundidade (Agitação + Depoimentos recomendados)
- **Seções visualmente diferentes** — alternar fundos claros, escuros, com imagem, com gradiente
- **Smooth scroll** entre âncoras internas
- **Depoimentos com avatar + nome + resultado específico** (nunca genérico)

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

## Checklist pré-entrega (verificar ANTES de salvar)

**Texto e idioma:**
- [ ] TODOS os textos em português com acentos corretos (módulo, não modulo)
- [ ] Nenhuma palavra sem acento na página inteira
- [ ] Revisar headlines, parágrafos, botões, FAQs, footer, labels — tudo

**Estrutura:**
- [ ] Header com logotipo no topo da página
- [ ] HTML válido, semântico, `lang="pt-BR"`, `charset="UTF-8"`

**Design e layout:**
- [ ] TODAS as fontes são SANS-SERIF (heading E body) — zero serifadas na página
- [ ] Fontes escolhidas da biblioteca aprovada em SKILL.md
- [ ] Cards de conteúdo com min-width >= 320px no grid
- [ ] Texto dentro de cards com font-size >= 0.95rem
- [ ] Padding interno de cards >= 28px
- [ ] Entregáveis/módulos em grid de 2 colunas (NÃO 3)
- [ ] NÃO parece design Lovable/v0 (sem cards idênticos em fundo bege)

**Variedade visual:**
- [ ] Pelo menos 4 tipos diferentes de fundo entre as seções
- [ ] Pelo menos 2 seções com imagem de fundo (Picsum + overlay)
- [ ] Seções visualmente distintas (não repetir o mesmo padrão)
- [ ] Pelo menos 1 divisor decorativo (wave SVG, linha, mudança abrupta)
- [ ] Pelo menos 3 animações de scroll (AOS ou CSS puro)

**Conversão:**
- [ ] Paleta com cor dominante forte (não pastéis tímidos)
- [ ] Botão CTA com contraste máximo contra o fundo
- [ ] Depoimentos com avatar (pravatar.cc)
- [ ] FAQ com accordion funcional em JS
- [ ] Smooth scroll ativado
- [ ] Mobile responsivo (testar visualmente em 375px)
- [ ] CTA flutuante no mobile

### 4. Inserir Pixel (se configurado)
Leia `.env` e verifique `META_PIXEL_ID`. Se existir, insira o snippet do Facebook Pixel no `<head>` da página com os eventos adequados:
- Captura: evento `Lead` no submit
- Vendas: evento `ViewContent` no carregamento
- Obrigado: evento `Purchase` ou `CompleteRegistration`

Se não existir, gere a página sem Pixel.

### 5. Salvar
- `entregas/paginas/vendas-[produto].html`
- `entregas/paginas/captura-[produto].html`
- `entregas/paginas/obrigado-[produto].html`

### 6. Deploy na Vercel

Após salvar a página, verifique se o projeto está configurado para deploy:

**Passo 1 — Verificar pré-requisitos:**

Checar se existem os seguintes arquivos no projeto:
- `.env` com `VERCEL_TOKEN` e `VERCEL_ORG_ID` e `VERCEL_PROJECT_ID`
- `vercel.json` na raiz do projeto
- `package.json` na raiz do projeto

**Passo 2 — Se NÃO estiver configurado**, solicitar ao usuário:

```
Para publicar sua página online, preciso configurar o deploy na Vercel.

Você vai precisar de:
1. Uma conta na Vercel (gratuita) — vercel.com
2. Um token de acesso — Vercel → Settings → Tokens → Create Token
3. Instalar o Vercel CLI — `npm i -g vercel`

Quando tiver o token, me passe que eu configuro tudo.
Ou se preferir, abra o arquivo HTML direto no navegador por enquanto.

1. Tenho o token, vou passar
2. Vou criar a conta e volto depois
3. Não quero deploy agora, só salvar local

Digite o número:
```

Se o usuário passar o token:
1. Criar `.env` com `VERCEL_TOKEN=<token>`
2. Criar `package.json` mínimo:
```json
{
  "name": "paginas-marketing",
  "version": "1.0.0",
  "private": true
}
```
3. Criar `vercel.json`:
```json
{
  "buildCommand": null,
  "outputDirectory": "entregas/paginas",
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" }
      ]
    }
  ]
}
```
4. Executar o deploy:
```bash
cd <projeto> && npx vercel --token $VERCEL_TOKEN --yes
```
5. Informar a URL pública ao usuário

**Passo 3 — Se JÁ estiver configurado**, fazer o deploy diretamente:

```bash
cd <projeto> && npx vercel --token $VERCEL_TOKEN --yes
```

Informar: "Sua página está online em [URL]. Compartilhe esse link."

**Passo 4 — Deploy de produção (quando o usuário pedir):**

```bash
cd <projeto> && npx vercel --prod --token $VERCEL_TOKEN --yes
```

### 7. Próximo Passo
"Use `/anuncio` para criar anúncios que levem tráfego a essa página."
