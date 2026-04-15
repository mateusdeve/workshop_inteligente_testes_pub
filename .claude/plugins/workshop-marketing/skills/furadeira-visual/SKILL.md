---
name: furadeira-visual
description: >
  Gera representação visual da Furadeira (método do produto) como uma trilha de aprendizado em HTML
  com design de caminho progressivo — macroetapas como marcos da jornada e microetapas como checkpoints.
  Salva HTML em entregas/{ativo}/entregas/furadeira-visual.html e captura PNG se Chrome disponível.
  Acionada automaticamente pelo /produto-concepcao após validação do Bloco 2 (Furadeira).
---

# Furadeira Visual — Trilha de Método

Gera uma página HTML de alta qualidade que visualiza o método (Furadeira) do produto ativo como uma trilha de jornada progressiva, com macroetapas como marcos e microetapas como checkpoints.

---

## Quando Acionar

- Automaticamente após validação da Furadeira no `/produto-concepcao` (Bloco 2)
- Diretamente via `/furadeira-visual`
- Quando o aluno pedir uma visualização, infográfico ou mapa do método

---

## O Que Fazer

### 1. Coletar Dados

Leia `entregas/.ativo` e depois `entregas/{ativo}/perfil.md`.

Extraia:
- **Nome do Método** (ex: "Protocolo Anticoceira")
- **Quadro** (transformação principal)
- **Macroetapas** com seus nomes e descrições de 1 linha
- **Microetapas** de cada macroetapa
- **Produto** (nome do produto/curso)

Se algum desses dados estiver ausente no perfil, pergunte ao aluno antes de gerar.

### 2. Escolher Paleta de Cores

Pergunte ao aluno (UMA pergunta, numerada):

```
Qual estilo visual você prefere para a trilha do método?

1. Escuro moderno (fundo preto, detalhes coloridos — estilo tech/premium)
2. Claro minimalista (fundo branco/creme, linhas limpas — estilo educacional)
3. Colorido vibrante (fundo gradiente colorido — estilo motivacional/coaching)
4. Usar cor do meu produto (me diga a cor principal)

Digite o número:
```

### 3. Gerar HTML da Trilha Visual

Gere um arquivo HTML completo com o design de trilha progressiva seguindo TODAS as regras abaixo.

#### Estrutura Visual Obrigatória

O visual deve conter:

**Cabeçalho:**
- Nome do método em destaque (tipografia grande, bold)
- Quadro como subtítulo (a transformação que o aluno alcança)
- Nome do produto menor abaixo

**Trilha Principal:**
- Uma linha/caminho visual que conecta todas as macroetapas
- Cada macroetapa = um NODO PRINCIPAL na trilha (círculo grande numerado)
- O nodo tem: número, nome da macroetapa, descrição de 1 linha
- Abaixo de cada nodo: microetapas como badges/pills menores conectados
- A trilha vai do início (Ponto de Partida) até o fim (o Quadro conquistado)

**Ponto de Partida e Chegada:**
- Início: badge "Ponto de Partida" com ícone de pessoa/início
- Chegada: badge especial com o Quadro e ícone de troféu/estrela

**Layout:**
- Orientação: VERTICAL (trilha de cima para baixo, ou em zigzag)
- Largura fixa: 1080px (formato para imagem/post)
- Altura: automática conforme quantidade de etapas
- Padding generoso: min 60px nas laterais

#### Template HTML Base

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[NOME_METODO] — Trilha do Método</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  /* === VARIÁVEIS — ADAPTAR CONFORME PALETA ESCOLHIDA === */
  :root {
    /* PALETA ESCURO */
    --bg: #0a0a0f;
    --surface: #12121a;
    --surface-2: #1a1a28;
    --border: rgba(255,255,255,0.08);
    --text-primary: #f0f0f8;
    --text-secondary: #8888aa;
    --accent-1: #7c6fff; /* cor principal das macroetapas */
    --accent-2: #ff6fb0; /* cor de destaque/chegada */
    --accent-glow: rgba(124,111,255,0.25);
    --step-bg: #1e1e30;
    --micro-bg: rgba(124,111,255,0.12);
    --micro-border: rgba(124,111,255,0.3);
    --line-color: rgba(124,111,255,0.4);
    --start-color: #38a169;
    --end-color: #f6ad55;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    font-family: 'Inter', sans-serif;
    color: var(--text-primary);
    min-height: 100vh;
    padding: 0;
  }

  .canvas {
    width: 1080px;
    margin: 0 auto;
    padding: 60px 80px 80px;
    position: relative;
  }

  /* === CABEÇALHO === */
  .header {
    text-align: center;
    margin-bottom: 60px;
    padding-bottom: 40px;
    border-bottom: 1px solid var(--border);
  }

  .product-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--text-secondary);
    margin-bottom: 16px;
  }

  .method-name {
    font-size: 42px;
    font-weight: 900;
    line-height: 1.1;
    background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 16px;
  }

  .quadro-badge {
    display: inline-block;
    background: var(--micro-bg);
    border: 1px solid var(--micro-border);
    border-radius: 100px;
    padding: 10px 24px;
    font-size: 15px;
    font-weight: 500;
    color: var(--text-secondary);
  }

  /* === TRILHA === */
  .trail {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
  }

  /* Linha central da trilha */
  .trail::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom, var(--start-color), var(--accent-1) 40%, var(--accent-2) 70%, var(--end-color));
    transform: translateX(-50%);
    z-index: 0;
  }

  /* === PONTO DE PARTIDA === */
  .trail-start {
    position: relative;
    z-index: 2;
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--start-color);
    color: #fff;
    border-radius: 100px;
    padding: 12px 28px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 40px;
    box-shadow: 0 0 20px rgba(56,161,105,0.4);
  }

  .trail-start svg { width: 18px; height: 18px; }

  /* === NODO DA MACROETAPA === */
  .step-wrapper {
    position: relative;
    z-index: 2;
    width: 100%;
    margin-bottom: 8px;
  }

  /* Alternância esquerda/direita */
  .step-wrapper:nth-child(odd) .step-card { margin-left: 0; margin-right: calc(50% + 40px); }
  .step-wrapper:nth-child(even) .step-card { margin-left: calc(50% + 40px); margin-right: 0; }

  /* Conector ao centro */
  .step-wrapper::after {
    content: '';
    position: absolute;
    top: 44px;
    width: 40px;
    height: 2px;
    background: var(--accent-1);
    z-index: 1;
  }
  .step-wrapper:nth-child(odd)::after { right: calc(50% - 40px); left: auto; }
  .step-wrapper:nth-child(even)::after { left: calc(50% - 40px); right: auto; }

  .step-card {
    background: var(--step-bg);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 24px 28px;
    max-width: 380px;
    position: relative;
    transition: all 0.3s ease;
  }

  .step-card:hover {
    border-color: var(--accent-1);
    box-shadow: 0 0 30px var(--accent-glow);
    transform: translateY(-2px);
  }

  .step-number-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
    border-radius: 50%;
    font-size: 14px;
    font-weight: 800;
    color: #fff;
    margin-bottom: 12px;
    box-shadow: 0 0 16px var(--accent-glow);
  }

  .step-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 6px;
    line-height: 1.3;
  }

  .step-desc {
    font-size: 13px;
    color: var(--text-secondary);
    margin-bottom: 16px;
    line-height: 1.6;
  }

  /* Microetapas */
  .microsteps {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .micro-pill {
    background: var(--micro-bg);
    border: 1px solid var(--micro-border);
    border-radius: 100px;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 500;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .micro-pill::before {
    content: '◆';
    font-size: 6px;
    color: var(--accent-1);
  }

  /* === PONTO DE CHEGADA === */
  .trail-end {
    position: relative;
    z-index: 2;
    text-align: center;
    margin-top: 40px;
    padding: 32px 40px;
    background: linear-gradient(135deg, rgba(246,173,85,0.12), rgba(246,173,85,0.06));
    border: 1px solid rgba(246,173,85,0.3);
    border-radius: 24px;
    max-width: 500px;
    box-shadow: 0 0 40px rgba(246,173,85,0.15);
  }

  .end-icon {
    font-size: 36px;
    margin-bottom: 12px;
    display: block;
  }

  .end-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--end-color);
    margin-bottom: 8px;
  }

  .end-quadro {
    font-size: 20px;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.3;
  }

  /* === RODAPÉ === */
  .footer {
    margin-top: 60px;
    padding-top: 32px;
    border-top: 1px solid var(--border);
    text-align: center;
    font-size: 11px;
    color: var(--text-secondary);
    letter-spacing: 1px;
  }

  /* === PALETA CLARO (classe no body) === */
  body.tema-claro {
    --bg: #fafafa;
    --surface: #ffffff;
    --surface-2: #f0f0f2;
    --border: rgba(0,0,0,0.08);
    --text-primary: #18181b;
    --text-secondary: #52525b;
    --accent-1: #6d28d9;
    --accent-2: #db2777;
    --accent-glow: rgba(109,40,217,0.15);
    --step-bg: #ffffff;
    --micro-bg: rgba(109,40,217,0.06);
    --micro-border: rgba(109,40,217,0.2);
    --line-color: rgba(109,40,217,0.3);
  }

  /* === PALETA VIBRANTE === */
  body.tema-vibrante {
    --bg: linear-gradient(135deg, #1a0533, #0a1628, #0d2818);
    --surface: rgba(255,255,255,0.05);
    --surface-2: rgba(255,255,255,0.08);
    --border: rgba(255,255,255,0.12);
    --text-primary: #ffffff;
    --text-secondary: rgba(255,255,255,0.6);
    --accent-1: #a855f7;
    --accent-2: #06b6d4;
    --accent-glow: rgba(168,85,247,0.3);
    --step-bg: rgba(255,255,255,0.05);
    --micro-bg: rgba(168,85,247,0.15);
    --micro-border: rgba(168,85,247,0.35);
  }
  body.tema-vibrante { background: linear-gradient(135deg, #1a0533, #0a1628, #0d2818) !important; }

</style>
</head>
<body>
<!-- Adicionar classe: tema-claro | tema-vibrante conforme escolha -->

<div class="canvas">

  <!-- CABEÇALHO -->
  <div class="header">
    <div class="product-label">MÉTODO DE</div>
    <h1 class="method-name">[NOME_DO_METODO]</h1>
    <div class="quadro-badge">Transformação: [QUADRO]</div>
  </div>

  <!-- TRILHA -->
  <div class="trail">

    <!-- INÍCIO -->
    <div class="trail-start">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/>
      </svg>
      Ponto de Partida
    </div>

    <!-- MACROETAPA 1 — Alternância automática: odd=esquerda, even=direita -->
    <div class="step-wrapper">
      <div class="step-card">
        <div class="step-number-badge">1</div>
        <div class="step-title">[NOME_MACROETAPA_1]</div>
        <div class="step-desc">[DESCRICAO_MACROETAPA_1]</div>
        <div class="microsteps">
          <span class="micro-pill">[microetapa 1.1]</span>
          <span class="micro-pill">[microetapa 1.2]</span>
          <span class="micro-pill">[microetapa 1.3]</span>
        </div>
      </div>
    </div>

    <!-- MACROETAPA 2 -->
    <div class="step-wrapper">
      <div class="step-card">
        <div class="step-number-badge">2</div>
        <div class="step-title">[NOME_MACROETAPA_2]</div>
        <div class="step-desc">[DESCRICAO_MACROETAPA_2]</div>
        <div class="microsteps">
          <span class="micro-pill">[microetapa 2.1]</span>
          <span class="micro-pill">[microetapa 2.2]</span>
        </div>
      </div>
    </div>

    <!-- MACROETAPA 3 -->
    <div class="step-wrapper">
      <div class="step-card">
        <div class="step-number-badge">3</div>
        <div class="step-title">[NOME_MACROETAPA_3]</div>
        <div class="step-desc">[DESCRICAO_MACROETAPA_3]</div>
        <div class="microsteps">
          <span class="micro-pill">[microetapa 3.1]</span>
          <span class="micro-pill">[microetapa 3.2]</span>
        </div>
      </div>
    </div>

    <!-- Repetir padrão para cada macroetapa adicional -->

    <!-- CHEGADA / RESULTADO FINAL -->
    <div class="trail-end">
      <span class="end-icon">🏆</span>
      <div class="end-label">Resultado Final Conquistado</div>
      <div class="end-quadro">[QUADRO_COMPLETO]</div>
    </div>

  </div>

  <!-- RODAPÉ -->
  <div class="footer">
    [NOME_DO_PRODUTO] · Metodologia exclusiva · [ANO]
  </div>

</div>

</body>
</html>
```

#### Regras de Preenchimento do Template

1. Substitua TODOS os placeholders com os dados reais do produto ativo
2. Gere um `<div class="step-wrapper">` para cada macroetapa (3 a 7)
3. Gere uma `<span class="micro-pill">` para cada microetapa da macroetapa
4. A alternância esquerda/direita acontece automaticamente pelo CSS `nth-child(odd/even)`
5. Ajuste as cores `--accent-1` e `--accent-2` conforme paleta escolhida pelo aluno:
   - Escuro moderno (padrão): roxo `#7c6fff` + rosa `#ff6fb0`
   - Claro minimalista: adicione `class="tema-claro"` no `<body>`
   - Colorido vibrante: adicione `class="tema-vibrante"` no `<body>`
   - Cor do produto: use a cor informada no `--accent-1`, derive variante escura no `--accent-2`

#### VERIFICAÇÃO OBRIGATÓRIA antes de salvar

Percorra o HTML gerado e confirme:
- [ ] Nenhum placeholder `[...]` restou no código
- [ ] O nome do método está correto
- [ ] O Quadro está completo
- [ ] Todas as macroetapas estão presentes
- [ ] Cada macroetapa tem pelo menos 2 microetapas
- [ ] A paleta de cores está aplicada corretamente

### 4. Salvar HTML

Salve em: `entregas/{ativo}/furadeira-visual.html`

**Não mostre o código HTML ao usuário.**

### 5. Capturar PNG (se Chrome disponível)

Após salvar o HTML, tente capturar o PNG usando `mcp__Claude_in_Chrome__navigate` para abrir o arquivo local e `mcp__Claude_in_Chrome__computer` para tirar a screenshot.

- Caminho do arquivo: `file:///[caminho_absoluto]/entregas/{ativo}/furadeira-visual.html`
- Se a captura funcionar: salve o PNG em `entregas/{ativo}/furadeira-visual.png` e informe o caminho
- Se a captura falhar ou o Chrome não estiver disponível: informe apenas o HTML e oriente o aluno a abrir no navegador e usar Ctrl+Shift+P > "Screenshot" ou imprimir como PDF

### 6. Confirmar ao Aluno

```
Trilha visual do método gerada.

HTML: entregas/{ativo}/furadeira-visual.html
[PNG: entregas/{ativo}/furadeira-visual.png  (se capturado)]

Abra o arquivo HTML no navegador para visualizar.
Para salvar como imagem: clique com o botão direito > Imprimir > Salvar como PDF,
ou use a extensão "Full Page Screen Capture" do Chrome.
```

### 7. Próximo Passo Sugerido

```
Agora que o método está visualizado, o próximo passo é criar sua página de vendas.
Use /pagina-de-vendas para construir a página completa com estrutura 8D.
```

---

## Referências

- Mecânicas de Furadeira: `.claude/plugins/workshop-marketing/skills/furadeira-visual/references/6-mecanicas.md`
- Design base: `.claude/plugins/workshop-marketing/skills/paginas/references/design-system-components.md`
