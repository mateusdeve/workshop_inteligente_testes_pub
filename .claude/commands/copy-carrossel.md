---
name: workshop-marketing:copy-carrossel
description: Gera carrossel completo para Instagram em HTML — copy de todos os slides com Light Copy + design finalizado com Barlow Condensed + Inter, fundo escuro, destaque colorido. Pronto para screenshot e publicar. Usa Urgências Ocultas do produto ativo.
allowed-tools: Read, Write, Bash
---

# Carrossel HTML. Gerador de Carrossel para Instagram

Gera o carrossel completo: copy de todos os slides + HTML com design finalizado, pronto para screenshot e publicar no Instagram.

## Usage

```
/copy-carrossel
```

## O Que Fazer

### 0. Contexto

Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md` se existir.

Extraia internamente (não mostrar ao usuário):
- Urgências Ocultas completas (70 itens, 7 categorias)
- Decorados (50 benefícios)
- Quadro (transformação principal)
- Nicho e público

Verifique carrosséis anteriores em `meus-produtos/{ativo}/entregas/conteudo-social/` para evitar repetir ângulos já usados.

---

### 1. Entrevista (UMA pergunta por vez)

**Bloco 1/3. Formato:**

```
Qual formato de carrossel?

1. Quadrado (1:1, 1080x1080). padrão Instagram feed
2. Retrato (4:5, 1080x1350). mais espaço na tela

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Formato: [formato]
Próximo: Tema do carrossel
---
```

**Bloco 2/3. Tema:**

Liste as 8 Urgências Ocultas mais fortes do perfil, priorizando Dores, Urgências Quentes e Inusitadas:

```
Qual situação vai inspirar o carrossel?

1. [Urgência 1]
2. [Urgência 2]
3. [Urgência 3]
4. [Urgência 4]
5. [Urgência 5]
6. [Urgência 6]
7. [Urgência 7]
8. [Urgência 8]

Digite o número (ou descreva outro ângulo):
```

```
--- Bloco 2/3 concluído ---
Tema: [urgência escolhida]
Próximo: Cor de destaque
---
```

**Bloco 3/3. Cor de destaque:**

Derivar automaticamente da categoria da urgência:

| Categoria | Cor de destaque | Hex |
|---|---|---|
| Dor física ou emocional | Laranja-vermelho | #FF4500 |
| Desejo de resultado | Verde elétrico | #00D400 |
| Urgência quente (evento próximo) | Laranja elétrico | #FF6600 |
| Urgência fria (acumulado) | Teal brilhante | #00CED1 |
| Urgência inusitada | Roxo elétrico | #8B5CF6 |

Apresentar a cor escolhida:

```
Cor de destaque: [hex] ([nome da cor]) — baseada na categoria da urgência.

1. Manter essa cor
2. Escolher outra (me diga o nome ou o hex)
```

**Confirmação antes de gerar:**

```
Resumo do que vou criar:

- Formato: [formato]
- Tema: [urgência]
- Cor de destaque: [hex] ([nome])
- Slides: 7 a 8

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

---

### 2. Geração da Copy

Escreva a copy de todos os slides aplicando Light Copy. Revise cada slide antes de escrever o próximo.

**Checklist obrigatório por slide:**
- Sem travessão em nenhuma frase
- Sem ponto de exclamação
- Sem perguntas no gancho ou título
- Sem estrutura "Não é X. É Y."
- Sem promessas vagas sem dado concreto
- Produto não aparece nos primeiros 5 slides
- Linguagem cotidiana, sem jargão técnico de nicho

**Estrutura dos slides:**

**Slide 1 — Capa:**
- Kicker: monólogo interno do leitor, tempo presente, momento específico da urgência. Não é narrador, é o pensamento dela. (máx 65 chars)
- Headline: afirmação direta, ALL CAPS, dado concreto se possível. (máx 35 chars, pode quebrar em 2 linhas)
- Subtítulo: complemento do headline, linguagem cotidiana (máx 70 chars, opcional)

**Slides 2 a N-1 — Conteúdo:**
- Número do slide (02, 03, ...)
- Título do insight: afirmação concreta ou revelação (máx 55 chars, Title Case)
- Texto: 2 a 3 linhas com dado, situação real ou argumento específico (máx 180 chars)
- Cada slide avança o argumento — proibido repetir o slide anterior com outras palavras

**Slide Final — CTA:**
- Headline: resultado principal ou revelação final em ALL CAPS (máx 40 chars, Barlow Condensed)
- CTA: convite suave para próxima ação — sem "compre", sem "curso", sem "clique aqui"
- Handle: @[perfil] ou deixar como placeholder `@seuarroba`

Apresente a copy completa antes de gerar o HTML:

```
SLIDE 1 — CAPA
"[kicker]"
[HEADLINE]
[subtítulo]

SLIDE 2
[título do insight]
[texto de desenvolvimento]

SLIDE 3
[título do insight]
[texto de desenvolvimento]

[... demais slides ...]

SLIDE [N] — CTA
[HEADLINE]
[cta]
@seuarroba

---
1. Aprovar e gerar o HTML
2. Quero ajustar um slide (indique qual e o que muda)
```

---

### 3. Geração do HTML

Após aprovação da copy, gere um arquivo HTML único, completo e auto-contido.

**Fontes (Google Fonts, obrigatório):**
```html
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,700;0,900;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

**Dimensões reais e de exibição:**
- 1:1 → slide real: 1080×1080px, exibir em tela: 540×540px (scale 0.5)
- 4:5 → slide real: 1080×1350px, exibir em tela: 540×675px (scale 0.5)

**Sistema de cores:**
```css
--bg: #0F0F0F;
--bg2: #1A1A1A;
--accent: [hex escolhido];
--text: #FFFFFF;
--text-muted: rgba(255,255,255,0.65);
--border: rgba(255,255,255,0.08);
--number-ghost: rgba(255,255,255,0.04);
```

**Design dos slides:**

Cada slide é um `<div class="slide slide-N">` com position: relative, overflow: hidden.

Elementos de identidade visual presentes em todos os slides:
- Barra lateral esquerda: `position: absolute; left: 0; top: 10%; height: 80%; width: 3px; background: var(--accent); border-radius: 0 2px 2px 0;`
- Indicador de progresso: `"0N / 0X"` canto superior direito, Inter 400, 11px, var(--text-muted)

**Slide 1 (capa) — CSS e estrutura:**
```
background: linear-gradient(135deg, #0F0F0F 0%, #1C1C1C 100%);

Layout (justify-content: center, align-items: center, flex-direction: column, text-align: center):
- padding: 80px 100px (proporcional ao slide real de 1080px)

Kicker:
  font-family: 'Inter'; font-weight: 400; font-size: 28px;
  color: var(--text); opacity: 0.85; letter-spacing: 0.01em;
  margin-bottom: 28px;

Headline:
  font-family: 'Barlow Condensed'; font-weight: 900; font-size: 120px;
  line-height: 0.95; text-transform: uppercase; color: var(--accent);
  letter-spacing: -0.01em; margin-bottom: 32px;

Subtítulo:
  font-family: 'Inter'; font-weight: 500; font-size: 24px;
  color: var(--text-muted); line-height: 1.5;

Detalhe decorativo abaixo do subtítulo:
  linha horizontal 2px, 80px de largura, cor var(--accent), margin-top: 40px, centralizada

Canto inferior direito: símbolo ✦ (U+2736) 20px, var(--accent), opacity 0.6
```

**Slides de conteúdo (2 a N-1) — CSS e estrutura:**
```
background: var(--bg);

Número fantasma de fundo:
  font-family: 'Barlow Condensed'; font-weight: 900; font-size: 420px;
  color: var(--number-ghost); position: absolute; bottom: -60px; right: -20px;
  line-height: 1; user-select: none; pointer-events: none;

Layout: padding 80px 100px 80px 120px (120px à esquerda por causa da barra lateral)
justify-content: center; flex-direction: column;

Número legível:
  font-family: 'Inter'; font-weight: 600; font-size: 13px;
  color: var(--accent); text-transform: uppercase; letter-spacing: 0.12em;
  margin-bottom: 32px;

Título do insight:
  font-family: 'Barlow Condensed'; font-weight: 700; font-size: 68px;
  line-height: 1.05; color: var(--text); letter-spacing: -0.01em;
  margin-bottom: 32px;

Separador:
  height: 1px; width: 100%; background: var(--border); margin-bottom: 32px;

Texto de desenvolvimento:
  font-family: 'Inter'; font-weight: 400; font-size: 26px;
  color: var(--text-muted); line-height: 1.65;
```

**Slide CTA — CSS e estrutura:**
```
background: linear-gradient(135deg, #0F0F0F 0%, [cor de destaque com 12% opacity como second stop] 100%);
Ou: background: radial-gradient(ellipse at bottom right, [accent]20 0%, #0F0F0F 60%);

Layout: centralizado, flex-direction: column, text-align: center
padding: 80px 100px

HEADLINE CTA:
  font-family: 'Barlow Condensed'; font-weight: 900; font-size: 100px;
  text-transform: uppercase; color: var(--accent); line-height: 0.95;
  margin-bottom: 40px;

Texto CTA:
  font-family: 'Inter'; font-weight: 400; font-size: 28px;
  color: var(--text); margin-bottom: 32px; line-height: 1.5;

Handle:
  font-family: 'Inter'; font-weight: 600; font-size: 24px;
  color: var(--accent); letter-spacing: 0.02em;

Elemento decorativo: ✦ acima do headline, 28px, var(--accent), opacity 0.8
```

**Interface da página (fora dos slides):**

A página envolve os slides com uma interface clean para navegação e screenshot:

```
body background: #111111
font-family: 'Inter'

Header da página:
  padding: 24px 32px; border-bottom: 1px solid rgba(255,255,255,0.06);
  Título: "Carrossel — [Tema resumido]" em Inter 600 16px, branco
  Subtítulo: "[Produto ativo] — [formato]" em Inter 400 13px, rgba(255,255,255,0.4)
  Botão "Ver todos os slides": direita do header, abre modo screenshot

Wrapper dos slides em modo normal:
  Viewer com um slide visível por vez
  Setas prev/next (← →) nos lados, grandes e clicáveis
  Indicador de progresso: bolinhas numeradas abaixo (clicáveis para ir direto ao slide)
  Fundo do viewer: #0A0A0A com padding

Modo screenshot (classe .screenshot-mode no body):
  Header e controles de navegação desaparecem (display: none)
  Todos os slides aparecem empilhados verticalmente com gap: 32px
  Fundo da página vira #111111
  Instrução no topo: "Screenshot cada slide. Ctrl+Scroll para zoom. Esc para sair."
  ESC retorna ao modo normal
```

**JavaScript necessário:**
- Navegação prev/next entre slides (array de slides, índice atual)
- Bolinhas de progresso clicáveis
- Toggle modo screenshot (botão + tecla Esc para sair)
- Keyboard: ← → para navegar, S para modo screenshot

**Escala dos slides na tela:**

Use transform: scale(0.5) com transform-origin: top left e um wrapper com dimensões ajustadas:
```css
.slide-wrapper {
  width: 540px; /* 1080 * 0.5 */
  height: 540px; /* ou 675px para 4:5 */
  overflow: hidden;
}
.slide {
  width: 1080px;
  height: 1080px; /* ou 1350px */
  transform: scale(0.5);
  transform-origin: top left;
}
```

Em modo screenshot, trocar para scale(0.7) para visualização maior, ou mostrar em tamanho real com scroll.

**Arquivo a ser gerado:**
`meus-produtos/{ativo}/entregas/conteudo-social/carrossel-{slug}-{n}.html`

Onde `{n}` é o próximo número sequencial. Verificar arquivos existentes antes de numerar.

O HTML nunca é mostrado no chat. Salvar silenciosamente.

---

### 4. Entrega

```
Carrossel salvo em:
meus-produtos/{ativo}/entregas/conteudo-social/carrossel-{slug}-{n}.html

Para publicar:
1. Abra o arquivo no navegador
2. Clique em "Ver todos os slides" para ver a sequência limpa
3. Screenshot de cada slide (Win: Win+Shift+S | Mac: Cmd+Shift+4)
4. Suba os 7 prints como carrossel no Instagram

Próximos passos:
- Caption para o carrossel: /copy-social (opção 2. Caption)
- Anúncio com a mesma urgência: /criativo-aida
- Mais carrosséis: /copy-carrossel novamente
```

---

## Regras

- Copy gerada e aprovada ANTES do HTML. Sem exceção.
- Aprovação obrigatória da copy antes de gerar. Única exceção: usuário pediu explicitamente "vai direto" na mesma sessão.
- Light Copy em todos os slides: sem travessão, sem exclamação, sem pergunta no gancho.
- Produto não aparece nos primeiros 5 slides.
- Gancho do slide 1: monólogo interno do leitor, nunca narrador de fora.
- Numeração sequencial dos arquivos dentro do produto.
- HTML nunca mostrado no chat. Salvar silenciosamente.
- Fontes sempre Google Fonts. Barlow Condensed + Inter é o padrão obrigatório.
- Cada slide deve funcionar como unidade independente: quem vê só um slide entende o ponto.
- Cor de destaque vai APENAS na headline da capa, nos títulos de insight e nos elementos decorativos. Texto de apoio sempre branco ou muted white.
- Slide de conteúdo: o número fantasma de fundo (400px+) é elemento visual, não informação. Proibido colocar texto que conflite com ele.
