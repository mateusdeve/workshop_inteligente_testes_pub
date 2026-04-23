---
name: furadeira-visual
description: >
  Gera representação visual da Furadeira (método do produto) em HTML.
  Escolhe automaticamente o layout correto conforme a estrutura do método
  (zigzag, roadmap, puzzle, hexágonos, grid, hub, pirâmide, fluxograma,
  quadrantes 2x2, roda com pontos, roda octogonal, mandala concêntrica, trilha ondulada).
  Salva HTML em meus-produtos/{ativo}/entregas/furadeira-visual.html e captura PNG se Chrome disponível.
  Acionada automaticamente pelo /produto-concepcao após validação do Bloco 2 (Furadeira).
---

# Furadeira Visual — Trilha do Método

Gera uma página HTML de alta qualidade que visualiza o método (Furadeira) do produto ativo.
O layout é escolhido conforme a estrutura real do método, não pela preferência estética.

---

## Quando Acionar

- Automaticamente após validação da Furadeira no `/produto-concepcao` (Bloco 2)
- Diretamente via `/furadeira-visual`
- Quando o aluno pedir visualização, infográfico ou mapa do método

---

## O Que Fazer

### 1. Coletar Dados

Leia `meus-produtos/.ativo` e `meus-produtos/{ativo}/perfil.md`.

Extraia:
- **Nome do Método** (ex: "Protocolo Anticoceira")
- **Quadro** (transformação principal)
- **Macroetapas** com nomes e descrição de 1 linha cada
- **Microetapas** de cada macroetapa
- **Nome do produto**

Se faltar dados, pergunte antes de continuar.

---

### 2. Escolher o Layout Visual

**Nunca pergunte ao usuário qual template usar.** Analise os dados do método e decida automaticamente com base nas regras abaixo.

**Critérios de decisão (aplique na ordem):**

| Estrutura detectada no método | Template a usar |
|---|---|
| 3 macroetapas com relação de interdependência ou encaixe | `references/templates/06-puzzle-3pecas.html` |
| 4 pilares/dimensões que convergem para um núcleo central | `references/templates/04-hub-central.html` |
| 4 quadrantes com opostos (ex: DISC, estilos, perfis) | `references/templates/09-quadrantes-2x2.html` |
| Hub central com 4 letras/sigla + quadrantes numerados ao redor | `references/templates/16-hub-numerado-quadrantes.html` |
| Hierarquia ou afunilamento (começa amplo, afunila) | `references/templates/03-piramide-invertida.html` |
| Caminhos condicionais ("se X então Y, senão Z") | `references/templates/05-fluxograma-condicional.html` |
| 3 a 4 perfis ou trilhas paralelas (o aluno se identifica com uma) | `references/templates/08-grid-categorias.html` |
| 4 a 6 fases progressivas com múltiplos sub-passos por fase | `references/templates/07-hexagonos-cadeia.html` |
| 9 elementos em roda com conexões internas (estilo eneagrama) | `references/templates/10-roda-eneagrama.html` |
| 8 setores em roda/bússola/octógono | `references/templates/11-roda-octogonal.html` |
| Camadas concêntricas de profundidade ou complexidade | `references/templates/12-mandala-concentrica.html` |
| Jornada com paradas, fases bônus ou desvios | `references/templates/13-trilha-ondulada.html` |
| Progressão crescente com marcos de nível (curva de crescimento) | `references/templates/14-curva-exponencial.html` |
| Espectro ou escala de comportamento/maturidade | `references/templates/15-regua-comportamento.html` |
| Sequencial linear com 5 ou mais fases (padrão geral) | `references/templates/02-roadmap-vertical.html` |
| Sequencial com até 4 fases (slide ou infográfico horizontal) | `references/templates/01-linear-horizontal.html` |

> Padrão de desempate: se a estrutura for sequencial simples sem critério mais específico, use o Roadmap Vertical (02).
> Leia o template escolhido antes de gerar o HTML.

---

### 3. Escolher Paleta de Cores

Após confirmar o layout, pergunte:

```
Qual estilo visual para as cores?

1. Escuro moderno (fundo preto ou escuro, detalhes coloridos)
2. Claro minimalista (fundo branco, linhas limpas)
3. Colorido vibrante (cores saturadas, estilo motivacional)
4. Cor do meu produto (me diga a cor principal)

Digite o número:
```

Adapte as variáveis CSS `--accent`, `--bg`, `--ink` do template conforme a paleta escolhida.

---

### 4. Gerar o HTML

Leia o arquivo do template escolhido em `references/templates/`.

Preencha TODOS os placeholders `{{...}}` com os dados reais do produto ativo:
- `{{NOME_METODO}}` → nome do método
- `{{QUADRO}}` → transformação principal
- `{{NOME_PRODUTO}}` → nome do produto
- `{{MACROETAPA_N}}` → nome de cada macroetapa
- `{{DESC_MACROETAPA_N}}` → descrição de 1 linha
- `{{MICRO_N_M}}` → cada microetapa

**Regras de preenchimento:**

- Texto sempre curto: nome da etapa + 1 frase. Proibido parágrafos
- Cada macroetapa deve ter pelo menos 2 microetapas
- Adapte somente cores (variáveis CSS) e textos — nunca altere a estrutura HTML, grid, classes ou fontes do template
- Não adicione seções que não existem no template
- Não remova seções que existem no template (ajuste a quantidade de etapas dentro do padrão do layout)

**REGRA OBRIGATÓRIA — Responsividade para browser:**

Os templates originais usam dimensões fixas para exportação/screenshot (ex: `width: 1920px; height: 1080px; overflow: hidden`). Ao gerar o HTML para salvar em `meus-produtos/{ativo}/entregas/furadeira-visual.html`, **sempre substitua** essas dimensões fixas pelas regras responsivas abaixo:

```css
/* SUBSTITUIR isto: */
html, body { width: 1920px; height: 1080px; overflow: hidden; }

/* POR isto: */
html, body { width: 100%; min-height: 100vh; }
```

Adicionalmente:
- Substituir `flex: 1` e `padding: XX 0` no container de etapas por `flex-wrap: wrap; padding: 0`
- Substituir font-sizes fixos grandes (acima de 40px) por `clamp(tamanho-min, vw, tamanho-max)` para manter legibilidade em telas menores
- Adicionar `@media (max-width: 900px)` com `flex-direction: column` no container de etapas horizontais

Isso garante que o arquivo abre corretamente no navegador sem cortar o conteúdo. Templates de exportação nunca devem chegar ao aluno com `overflow: hidden`.

**Se o método tiver mais etapas que o template suporta:** agrupe as menores ou use o Roadmap Vertical (02) que é o mais flexível.

#### VERIFICAÇÃO OBRIGATÓRIA antes de salvar

- [ ] Nenhum placeholder `{{...}}` restou no código
- [ ] O nome do método está correto e visível
- [ ] O Quadro está presente
- [ ] Todas as macroetapas estão representadas
- [ ] Cada macroetapa tem pelo menos 2 microetapas
- [ ] A paleta escolhida está aplicada nas variáveis CSS
- [ ] A estrutura HTML do template não foi alterada

---

### 5. Salvar HTML

Salve em: `meus-produtos/{ativo}/entregas/furadeira-visual.html`

**Não mostre o código HTML ao usuário.**

---

### 6. Capturar PNG (se Chrome disponível)

Após salvar, tente capturar o PNG usando `mcp__Claude_in_Chrome__navigate` para abrir o arquivo local e `mcp__Claude_in_Chrome__computer` para tirar a screenshot.

- Caminho: `file:///[caminho_absoluto]/meus-produtos/{ativo}/entregas/furadeira-visual.html`
- Se captura funcionar: salve em `meus-produtos/{ativo}/entregas/furadeira-visual.png`
- Se falhar: informe apenas o HTML e oriente abrir no navegador

---

### 7. Confirmar ao Aluno

```
Trilha visual do método gerada.

Layout: [nome do layout escolhido]
HTML: meus-produtos/{ativo}/entregas/furadeira-visual.html
[PNG: meus-produtos/{ativo}/entregas/furadeira-visual.png  (se capturado)]

Abra o HTML no navegador para visualizar.
Para exportar como imagem: Ctrl+P > Salvar como PDF, ou extensão "Full Page Screen Capture" do Chrome.
```

---

### 8. Próximo Passo Sugerido

```
Agora que o método está visualizado, o próximo passo é criar sua página de vendas.
Use /copy-pagina para construir a página completa com estrutura 8D.
```

---

## Referências

- Decisão de layout: `.claude/skills/furadeira-visual/references/metodo-visual.md`
- Mecânicas da Furadeira: `.claude/skills/furadeira-visual/references/6-mecanicas.md`
- Templates HTML: `.claude/skills/furadeira-visual/references/templates/`

---

## Template Embutido — Trilha Zigzag (opcional)

Use este template apenas quando o aluno pedir explicitamente uma "trilha" ou "jornada" no estilo zigzag, ou quando nenhum dos 8 templates acima se encaixar bem.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{NOME_METODO}} — Trilha do Método</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #12121a;
    --border: rgba(255,255,255,0.08);
    --text-primary: #f0f0f8;
    --text-secondary: #8888aa;
    --accent-1: #7c6fff;
    --accent-2: #ff6fb0;
    --accent-glow: rgba(124,111,255,0.25);
    --step-bg: #1e1e30;
    --micro-bg: rgba(124,111,255,0.12);
    --micro-border: rgba(124,111,255,0.3);
    --start-color: #38a169;
    --end-color: #f6ad55;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); font-family: 'Inter', sans-serif; color: var(--text-primary); padding: 0; }
  .canvas { width: 1080px; margin: 0 auto; padding: 60px 80px 80px; }
  .header { text-align: center; margin-bottom: 60px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
  .product-label { font-size: 12px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; color: var(--text-secondary); margin-bottom: 16px; }
  .method-name { font-size: 42px; font-weight: 900; background: linear-gradient(135deg, var(--accent-1), var(--accent-2)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 16px; }
  .quadro-badge { display: inline-block; background: var(--micro-bg); border: 1px solid var(--micro-border); border-radius: 100px; padding: 10px 24px; font-size: 15px; font-weight: 500; color: var(--text-secondary); }
  .trail { position: relative; display: flex; flex-direction: column; align-items: center; }
  .trail::before { content: ''; position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, var(--start-color), var(--accent-1) 40%, var(--accent-2) 70%, var(--end-color)); transform: translateX(-50%); z-index: 0; }
  .trail-start { position: relative; z-index: 2; display: flex; align-items: center; gap: 12px; background: var(--start-color); color: #fff; border-radius: 100px; padding: 12px 28px; font-size: 13px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 40px; }
  .step-wrapper { position: relative; z-index: 2; width: 100%; margin-bottom: 8px; }
  .step-wrapper:nth-child(odd) .step-card { margin-left: 0; margin-right: calc(50% + 40px); }
  .step-wrapper:nth-child(even) .step-card { margin-left: calc(50% + 40px); margin-right: 0; }
  .step-wrapper::after { content: ''; position: absolute; top: 44px; width: 40px; height: 2px; background: var(--accent-1); z-index: 1; }
  .step-wrapper:nth-child(odd)::after { right: calc(50% - 40px); }
  .step-wrapper:nth-child(even)::after { left: calc(50% - 40px); }
  .step-card { background: var(--step-bg); border: 1px solid var(--border); border-radius: 20px; padding: 24px 28px; max-width: 380px; }
  .step-number-badge { display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; background: linear-gradient(135deg, var(--accent-1), var(--accent-2)); border-radius: 50%; font-size: 14px; font-weight: 800; color: #fff; margin-bottom: 12px; }
  .step-title { font-size: 18px; font-weight: 700; margin-bottom: 6px; }
  .step-desc { font-size: 13px; color: var(--text-secondary); margin-bottom: 16px; line-height: 1.6; }
  .microsteps { display: flex; flex-wrap: wrap; gap: 6px; }
  .micro-pill { background: var(--micro-bg); border: 1px solid var(--micro-border); border-radius: 100px; padding: 5px 12px; font-size: 11px; font-weight: 500; color: var(--text-secondary); }
  .micro-pill::before { content: '◆'; font-size: 6px; color: var(--accent-1); margin-right: 5px; }
  .trail-end { position: relative; z-index: 2; text-align: center; margin-top: 40px; padding: 32px 40px; background: linear-gradient(135deg, rgba(246,173,85,0.12), rgba(246,173,85,0.06)); border: 1px solid rgba(246,173,85,0.3); border-radius: 24px; max-width: 500px; }
  .end-icon { font-size: 36px; margin-bottom: 12px; display: block; }
  .end-label { font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--end-color); margin-bottom: 8px; }
  .end-quadro { font-size: 20px; font-weight: 800; }
  .footer { margin-top: 60px; padding-top: 32px; border-top: 1px solid var(--border); text-align: center; font-size: 11px; color: var(--text-secondary); }
  body.tema-claro { --bg: #fafafa; --surface: #fff; --border: rgba(0,0,0,0.08); --text-primary: #18181b; --text-secondary: #52525b; --accent-1: #6d28d9; --accent-2: #db2777; --step-bg: #fff; --micro-bg: rgba(109,40,217,0.06); --micro-border: rgba(109,40,217,0.2); }
</style>
</head>
<body>
<div class="canvas">
  <div class="header">
    <div class="product-label">MÉTODO DE</div>
    <h1 class="method-name">{{NOME_METODO}}</h1>
    <div class="quadro-badge">Transformação: {{QUADRO}}</div>
  </div>
  <div class="trail">
    <div class="trail-start">Ponto de Partida</div>
    <!-- Repetir .step-wrapper para cada macroetapa -->
    <div class="step-wrapper">
      <div class="step-card">
        <div class="step-number-badge">1</div>
        <div class="step-title">{{MACROETAPA_1}}</div>
        <div class="step-desc">{{DESC_MACROETAPA_1}}</div>
        <div class="microsteps">
          <span class="micro-pill">{{MICRO_1_1}}</span>
          <span class="micro-pill">{{MICRO_1_2}}</span>
        </div>
      </div>
    </div>
    <div class="trail-end">
      <span class="end-icon">🏆</span>
      <div class="end-label">Resultado Final</div>
      <div class="end-quadro">{{QUADRO}}</div>
    </div>
  </div>
  <div class="footer">{{NOME_PRODUTO}} · Metodologia exclusiva</div>
</div>
</body>
</html>
```
