# Sub-skill utilitária. Export HTML de Análise

Sub-skill compartilhada por TODOS os 9 outputs da `/trafego-analise`. Não tem opção própria no menu — é acionada opcionalmente ao final de cada output, quando o aluno responde "sim" à pergunta de export.

**Propósito:** transformar o output narrado de uma análise em um HTML standalone usando o design system Fluxo Criativo, salvar no produto ativo e devolver o caminho absoluto pro aluno abrir no navegador.

---

## 1. Quando rodar

Após o Passo 6 do SKILL.md raiz (entrega da análise narrada), perguntar:

```
Quer salvar essa análise como HTML pra revisitar depois? (s/n)

⚠️ Snapshot: o HTML gerado é uma "fotografia" dos dados deste momento.
   Métricas mudam, e este arquivo NÃO atualiza sozinho. Ele tem o timestamp
   no topo pra deixar claro quando foi gerado. Pra dado fresco, rode a
   análise de novo.
```

Se `s`/`sim`: rodar esta sub-skill. Se `n`/`não` ou silêncio: encerrar normalmente.

**Nunca rodar export sem confirmação explícita.** Aluno que só quer texto rápido não recebe arquivo.

---

## 2. Onde salvar

```
meus-produtos/{ativo}/trafego/analise/{slug-output}-{YYYY-MM-DD-HHMM}.html
```

**Componentes do nome:**
- `{ativo}`: lê de `meus-produtos/.ativo`. Se ausente, recusar e instruir `/produto-novo`.
- `{slug-output}`: nome curto do output. Tabela:

| Output | slug |
|---|---|
| [1] Diagnóstico Rápido | `diagnostico-rapido` |
| [2] Performance & Funil | `performance-funil` |
| [3] Criativos & Copy | `criativos-copy` |
| [4] Geo & Demografia | `geo-demografia` |
| [5] Timing & Sazonalidade | `timing-sazonalidade` |
| [6] Investigação Profunda | `investigacao-profunda` |
| [7] Lifecycle & Histórico | `lifecycle-historico` |
| [8] Problemas Ocultos | `problemas-ocultos` |
| [9] Orçamento & Projeção | `orcamento-projecao` |

- `{YYYY-MM-DD-HHMM}`: timestamp local do momento da geração. Ex: `2026-05-05-1432`.

Exemplos de caminho final:
- `meus-produtos/curso-tarot/trafego/analise/diagnostico-rapido-2026-05-05-1432.html`
- `meus-produtos/ingles-atletas/trafego/analise/lifecycle-historico-2026-05-04-0930.html`

Se a pasta `trafego/analise/` não existir, criar.

**Não sobrescrever.** Cada export gera arquivo novo com timestamp próprio. Histórico fica disponível pra comparação depois.

---

## 3. Estrutura do HTML standalone

O arquivo é **autossuficiente**: CSS embedado em `<style>`, fontes via Google Fonts, zero dependência externa além disso. Aluno abre direto no navegador, sem servidor.

### 3.1 Esqueleto

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{Output} — {Produto} — Tráfego Análise</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Inter:wght@300;400;500&family=Space+Grotesk:wght@400;500&display=swap" rel="stylesheet">
  <style>
    {tokens-e-componentes-do-design-system}
  </style>
</head>
<body>
  <main class="page">

    <!-- Header com snapshot timestamp -->
    <header class="page-head">
      <div>
        <h1 class="page-title">
          <span class="accent">[{N}]</span>{nome do output}
        </h1>
        <p class="page-sub">{1 linha sobre o que esse output entrega}</p>
      </div>
      <div class="page-meta">
        <div>SNAPSHOT · <strong>{DD/MM/YYYY HH:MM}</strong></div>
        <div>PRODUTO · <strong>{nome do produto}</strong></div>
        <div>JANELA · <strong>{ex: últimos 30 dias}</strong></div>
        <div>CONTA · <strong>{act_id mascarado}</strong></div>
      </div>
    </header>

    <!-- Banner de "dado expira" -->
    <div class="snapshot-warn">
      Esta é uma fotografia tirada em <strong>{DD/MM HH:MM}</strong>.
      Métricas mudam continuamente. Para dado fresco, rode a análise novamente.
    </div>

    <!-- Blocos do output (ver mapeamento na seção 4) -->
    {blocos-renderizados}

    <!-- Rodapé com handoffs -->
    <footer class="page-foot">
      <div class="section-h">PRÓXIMOS PASSOS</div>
      {handoffs-em-pills}
    </footer>

  </main>
</body>
</html>
```

### 3.2 Tokens do design system (embedar em todo arquivo)

Copiar este bloco inteiro dentro de `<style>`:

```css
:root {
  /* Cores */
  --ink-0:#000; --ink-1:#050505; --ink-2:#0b0b0b; --ink-3:#141414; --ink-4:#1c1c1c;
  --line-1:#1a1a1a; --line-2:#262626;
  --text-hi:#ededea; --text-mid:#8a8a84; --text-dim:#555550; --text-faint:#2e2e2c;
  --neon:#c4ff5e; --neon-dim:#9ec947; --neon-deep:#4a6517; --neon-glow:rgba(196,255,94,0.18);
  --rust:#d97757; --ochre:#d4a24a; --plum:#9a7bb5; --sky:#7aa8c9;

  /* Tipografia */
  --font-display:"Space Grotesk",ui-sans-serif,system-ui;
  --font-body:"Inter",ui-sans-serif,system-ui;
  --font-mono:"JetBrains Mono",ui-monospace,monospace;

  /* Espaço */
  --s-1:4px; --s-2:8px; --s-3:12px; --s-4:16px; --s-5:20px;
  --s-6:24px; --s-7:32px; --s-8:40px; --s-9:56px; --s-10:80px;
}

* { box-sizing: border-box; }
html, body { margin:0; padding:0; }
html { color-scheme: dark; }
body {
  background: var(--ink-0);
  color: var(--text-hi);
  font-family: var(--font-body);
  font-size: 13px; line-height: 1.6; font-weight: 300;
  -webkit-font-smoothing: antialiased;
  font-feature-settings: "tnum";
}
::selection { background: var(--neon); color: var(--ink-0); }

.page { padding: var(--s-10) var(--s-9); max-width: 1180px; margin: 0 auto; }
.page-head {
  margin-bottom: var(--s-7);
  display: flex; align-items: flex-end; justify-content: space-between;
  gap: var(--s-6); flex-wrap: wrap;
}
.page-title {
  font-family: var(--font-display); font-size: 36px; font-weight: 300;
  letter-spacing: -0.03em; line-height: 1; margin: 0 0 var(--s-3);
}
.page-title .accent {
  color: var(--text-faint); font-family: var(--font-mono); font-weight: 300;
  font-size: 0.45em; letter-spacing: 0.02em; margin-right: var(--s-3);
  vertical-align: 0.35em;
}
.page-sub { color: var(--text-mid); font-size: 13px; font-weight: 300; max-width: 560px; margin: 0; }

.page-meta {
  font-family: var(--font-mono); font-size: 10px; color: var(--text-faint);
  letter-spacing: 0.1em; text-align: right; text-transform: uppercase;
  font-weight: 300; line-height: 1.8;
}
.page-meta strong { color: var(--text-mid); font-weight: 400; }

.snapshot-warn {
  border: 1px solid var(--neon-deep);
  background: rgba(196,255,94,0.04);
  font-family: var(--font-mono); font-size: 11px;
  color: var(--text-mid); letter-spacing: 0.02em; line-height: 1.7;
  padding: var(--s-3) var(--s-5); margin-bottom: var(--s-9);
}
.snapshot-warn::before {
  content: "SNAPSHOT · ";
  color: var(--neon); letter-spacing: 0.2em; font-weight: 500;
}
.snapshot-warn strong { color: var(--text-hi); font-weight: 400; }

.section-h {
  font-family: var(--font-mono); font-size: 10px; font-weight: 400;
  letter-spacing: 0.2em; text-transform: uppercase; color: var(--text-faint);
  margin: var(--s-10) 0 var(--s-5); padding-bottom: var(--s-3);
  border-bottom: 1px solid var(--line-1);
}

/* KPI */
.kpi-grid {
  display: grid; grid-template-columns: repeat(4,1fr); gap: var(--s-4);
  margin-bottom: var(--s-7);
}
.kpi { border-top: 1px solid var(--line-1); padding: var(--s-6) 0; }
.kpi-label {
  font-family: var(--font-mono); font-size: 9px; color: var(--text-faint);
  letter-spacing: 0.18em; text-transform: uppercase; font-weight: 400;
}
.kpi-num {
  font-family: var(--font-mono); font-size: 24px; font-weight: 300;
  color: var(--text-hi); margin-top: var(--s-3); line-height: 1; letter-spacing: -0.03em;
}
.kpi-foot {
  font-family: var(--font-mono); font-size: 10px; color: var(--text-dim);
  margin-top: var(--s-2); font-weight: 300;
}
.kpi .up { color: var(--neon); }
.kpi .down { color: var(--rust); }

/* Métrica destaque (Health Score, ROAS médio) */
.metric {
  font-family: var(--font-mono); font-feature-settings: "tnum";
  font-size: 32px; font-weight: 300; color: var(--neon);
  line-height: 1; letter-spacing: -0.03em;
}

/* Tabela */
.table { width: 100%; border-collapse: collapse; font-size: 12px; font-weight: 300; }
.table thead th {
  text-align: left; font-family: var(--font-mono); font-size: 9px;
  color: var(--text-faint); letter-spacing: 0.18em; text-transform: uppercase;
  padding: var(--s-3) var(--s-4) var(--s-3) 0;
  border-bottom: 1px solid var(--line-1); font-weight: 400;
}
.table tbody td {
  padding: var(--s-3) var(--s-4) var(--s-3) 0;
  border-bottom: 1px solid var(--line-1); color: var(--text-mid);
}
.table tbody tr:hover td { color: var(--text-hi); }
.table tbody td.strong { color: var(--text-hi); font-weight: 400; }
.table tbody td.mono { font-family: var(--font-mono); font-size: 11px; }
.table tbody td.up { color: var(--neon); }
.table tbody td.down { color: var(--rust); }
.table tbody td.warn { color: var(--ochre); }

/* Barras horizontais */
.bar-row {
  display: grid; grid-template-columns: 140px 1fr 60px;
  align-items: center; gap: var(--s-4); padding: 7px 0; font-size: 12px; font-weight: 300;
}
.bar-row .bar-label { color: var(--text-hi); }
.bar-row .bar-track { height: 2px; background: var(--line-1); position: relative; }
.bar-row .bar-fill { height: 100%; background: var(--neon); }
.bar-row .bar-val {
  font-family: var(--font-mono); font-size: 11px; color: var(--text-mid);
  text-align: right; font-weight: 300;
}

/* Chip */
.chip {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--font-mono); font-size: 9px; letter-spacing: 0.16em;
  text-transform: uppercase; padding: 2px 0; color: var(--text-dim); font-weight: 400;
}
.chip.active { color: var(--neon); }
.chip.ochre { color: var(--ochre); }
.chip.rust { color: var(--rust); }
.chip.plum { color: var(--plum); }
.chip .dot { width: 5px; height: 5px; border-radius: 50%; background: currentColor; }

/* Callout VTSD ("No VTSD isso significa...") */
.callout {
  padding: var(--s-3) 0 var(--s-3) var(--s-5);
  border-left: 1px solid var(--neon);
  font-family: var(--font-display); font-size: 14px; font-style: italic;
  font-weight: 300; margin: var(--s-5) 0; color: var(--text-hi); line-height: 1.5;
}
.callout::before {
  content: "NO VTSD · "; font-style: normal; font-family: var(--font-mono);
  font-size: 9px; color: var(--neon); letter-spacing: 0.2em;
  display: block; margin-bottom: 4px; font-weight: 500;
}

/* Caixa de ação recomendada (verde com gradiente) */
.pitch-box {
  border-left: 2px solid var(--neon);
  padding: var(--s-4) var(--s-5);
  background: linear-gradient(90deg, rgba(196,255,94,0.04), transparent 60%);
  margin: var(--s-5) 0; font-size: 13px; line-height: 1.65;
  color: var(--text-mid); font-weight: 300;
}
.pitch-box::before {
  content: "AÇÃO RECOMENDADA · "; font-family: var(--font-mono);
  font-size: 9px; color: var(--neon); letter-spacing: 0.2em;
  display: block; margin-bottom: var(--s-2); font-weight: 500;
}

/* Alerta crítico (regra) */
.regra {
  margin: var(--s-5) 0;
  padding: var(--s-4) var(--s-5);
  border: 1px solid var(--neon-deep);
  background: rgba(196,255,94,0.04);
  font-family: var(--font-mono); font-size: 11px;
  color: var(--text-hi); letter-spacing: 0.02em; line-height: 1.7; font-weight: 300;
}
.regra::before { content: "REGRA · "; color: var(--neon); letter-spacing: 0.2em; font-weight: 500; }
.regra.alerta { border-color: var(--rust); background: rgba(217,119,87,0.04); }
.regra.alerta::before { content: "ALERTA · "; color: var(--rust); }

/* Pills de handoff */
.terms { display: flex; flex-wrap: wrap; gap: var(--s-2); margin-top: var(--s-3); }
.term {
  font-family: var(--font-mono); font-size: 11px;
  padding: 4px 10px; border: 1px solid var(--line-1); border-radius: 999px;
  color: var(--text-mid);
}
.term.next { color: var(--neon); border-color: var(--neon-deep); }

/* SVG line chart (se usado) */
.linechart { width: 100%; height: 200px; }
.linechart .line { stroke: var(--neon); stroke-width: 1.5; fill: none; }
.linechart .area { fill: rgba(196,255,94,0.08); }
.linechart .dot { fill: var(--neon); }
.linechart text {
  font-family: var(--font-mono); font-size: 10px;
  fill: var(--text-dim); letter-spacing: 0.06em;
}

/* Rodapé */
.page-foot { margin-top: var(--s-10); }

/* Responsivo */
@media (max-width: 960px) {
  .page { padding: var(--s-6) var(--s-5); }
  .page-title { font-size: 28px; }
  .kpi-grid { grid-template-columns: 1fr 1fr; }
  .page-head { flex-direction: column; align-items: flex-start; }
  .page-meta { text-align: left; }
}

@media print {
  body { background: white; color: black; }
  .snapshot-warn { background: #fff8d8; color: #333; border-color: #ccc; }
  .neon, .neon * { color: #333 !important; }
}
```

### 3.3 Casca compartilhada (`index.html`) — dashboard navegável

A pasta `meus-produtos/{ativo}/trafego/analise/` ganha um arquivo **`index.html`** que serve de "porta de entrada" pra todos os exports. Estrutura: sidebar fixa à esquerda (igual `painel-entregas.html` do design system) + iframe central que carrega o snapshot do output selecionado.

**Regra:** o `index.html` é **regenerado a cada export individual**. Ele não é estático — descobre dinamicamente quais snapshots existem na pasta e qual é o mais recente de cada slug.

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Tráfego Análise — {Produto} — Dashboard</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Inter:wght@300;400;500&family=Space+Grotesk:wght@400;500&display=swap" rel="stylesheet">
  <style>
    /* Reusa todos os tokens da seção 3.2 */
    {tokens-css-da-secao-3.2}

    /* Casca App (do painel-entregas.html) */
    .app { display: grid; grid-template-columns: 220px 1fr; min-height: 100vh; }

    .sidebar {
      background: var(--ink-0);
      border-right: 1px solid var(--line-1);
      padding: var(--s-7) 0 var(--s-5);
      position: sticky; top: 0; height: 100vh;
      overflow-y: auto;
      display: flex; flex-direction: column;
    }
    .brand {
      padding: 0 var(--s-5) var(--s-7);
      display: flex; align-items: center; gap: var(--s-3);
    }
    .brand-mark {
      width: 24px; height: 24px; border-radius: 3px;
      background: var(--neon); flex-shrink: 0;
    }
    .brand-text {
      font-family: var(--font-mono); font-weight: 400; font-size: 11px;
      letter-spacing: 0.04em; line-height: 1.2; color: var(--text-hi);
    }
    .brand-text .tiny {
      display: block; color: var(--text-faint); font-weight: 400;
      font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;
      margin-top: 3px;
    }
    .user-block { padding: 0 var(--s-5) var(--s-6); margin-bottom: var(--s-2); }
    .user-block .label {
      font-family: var(--font-mono); font-size: 9px;
      color: var(--text-faint); letter-spacing: 0.18em; text-transform: uppercase;
    }
    .user-block .product {
      font-family: var(--font-display); font-size: 15px; font-weight: 400;
      margin-top: var(--s-2); letter-spacing: -0.015em; color: var(--text-hi);
    }
    .user-block .conta {
      color: var(--text-dim); font-size: 11px; font-weight: 300; margin-top: 3px;
      font-family: var(--font-mono); letter-spacing: 0.04em;
    }

    .nav { padding: var(--s-3); flex: 1; }
    .nav-group { margin-bottom: var(--s-5); }
    .nav-group-title {
      font-family: var(--font-mono); font-size: 9px; color: var(--text-faint);
      letter-spacing: 0.2em; text-transform: uppercase;
      padding: 0 var(--s-3); margin-bottom: var(--s-2); font-weight: 400;
    }
    .nav-item {
      display: flex; align-items: center; gap: var(--s-3);
      padding: 6px var(--s-3);
      color: var(--text-dim); font-size: 12px; font-weight: 300;
      cursor: pointer; transition: color 120ms;
      text-decoration: none;
    }
    .nav-item:hover { color: var(--text-hi); }
    .nav-item.active { color: var(--neon); }
    .nav-item .ix {
      font-family: var(--font-mono); font-size: 9px; color: var(--text-faint);
      width: 16px; flex-shrink: 0; font-weight: 300;
    }
    .nav-item.active .ix { color: var(--neon); opacity: 0.5; }
    .nav-item .ts {
      margin-left: auto; font-family: var(--font-mono); font-size: 9px;
      color: var(--text-faint); letter-spacing: 0.04em;
    }
    .nav-item.empty { color: var(--text-faint); cursor: default; }
    .nav-item.empty:hover { color: var(--text-faint); }
    .nav-item.empty .ts { font-style: italic; }

    .sidebar-footer { padding: var(--s-4) var(--s-5); }
    .btn-print {
      width: 100%; padding: 6px 0; background: transparent; border: 0;
      color: var(--text-dim); font-family: var(--font-mono);
      font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase;
      cursor: pointer; transition: color 120ms;
      display: flex; align-items: center; justify-content: space-between;
      font-weight: 300;
    }
    .btn-print:hover { color: var(--neon); }
    .btn-print .kbd { font-size: 9px; color: var(--text-faint); }

    /* Iframe central */
    .main { min-width: 0; display: flex; flex-direction: column; }
    .topbar {
      display: flex; align-items: center; justify-content: space-between;
      padding: var(--s-4) var(--s-7);
      background: rgba(0,0,0,0.8); backdrop-filter: blur(12px);
      position: sticky; top: 0; z-index: 20;
      border-bottom: 1px solid var(--line-1);
    }
    .crumbs {
      font-family: var(--font-mono); font-size: 10px; color: var(--text-faint);
      letter-spacing: 0.08em; text-transform: uppercase; font-weight: 300;
    }
    .crumbs .sep { margin: 0 var(--s-2); }
    .crumbs .now { color: var(--text-mid); }
    .status-dot {
      display: inline-flex; align-items: center; gap: var(--s-2);
      font-family: var(--font-mono); font-size: 9px; color: var(--text-faint);
      letter-spacing: 0.14em; text-transform: uppercase; font-weight: 300;
    }
    .status-dot .dot {
      width: 5px; height: 5px; border-radius: 50%;
      background: var(--neon); animation: pulse 2s ease-in-out infinite;
    }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }

    .iframe-host {
      flex: 1;
      background: var(--ink-0);
      position: relative;
    }
    .iframe-host iframe {
      width: 100%; height: 100%; border: 0; display: block;
      background: var(--ink-0);
    }
    .iframe-host .empty-state {
      position: absolute; inset: 0;
      display: flex; align-items: center; justify-content: center;
      flex-direction: column; gap: var(--s-3);
      color: var(--text-mid); font-family: var(--font-display);
      font-size: 18px; font-weight: 300; padding: var(--s-9);
      text-align: center;
    }
    .iframe-host .empty-state .hint {
      font-family: var(--font-mono); font-size: 11px;
      color: var(--text-faint); letter-spacing: 0.1em;
    }

    @media (max-width: 960px) {
      .app { grid-template-columns: 1fr; }
      .sidebar { position: relative; height: auto; }
    }
  </style>
</head>
<body>
<div class="app">

  <aside class="sidebar">
    <div class="brand">
      <div class="brand-mark"></div>
      <div class="brand-text">
        tráfego<br>análise
        <span class="tiny">Dashboard · v1</span>
      </div>
    </div>

    <div class="user-block">
      <div class="label">Produto ativo</div>
      <div class="product">{Produto}</div>
      <div class="conta">{act_id mascarado}</div>
    </div>

    <nav class="nav">
      <div class="nav-group">
        <div class="nav-group-title">Outputs Narrativos</div>
        <!-- Cada item: gerado dinamicamente pela skill -->
        <!-- Modelo "tem snapshot": -->
        <a class="nav-item" href="#" onclick="loadOutput('diagnostico-rapido-2026-05-05-1432.html', this); return false;">
          <span class="ix">01</span>
          <span>Diagnóstico Rápido</span>
          <span class="ts">5/5 14:32</span>
        </a>
        <!-- Modelo "ainda não rodado": -->
        <span class="nav-item empty">
          <span class="ix">04</span>
          <span>Geo & Demografia</span>
          <span class="ts">não rodado</span>
        </span>
        <!-- ... 9 itens no total ... -->
      </div>
    </nav>

    <div class="sidebar-footer">
      <button class="btn-print" onclick="document.querySelector('iframe')?.contentWindow.print()">
        <span>Imprimir / PDF</span>
        <span class="kbd">⌘P</span>
      </button>
    </div>
  </aside>

  <main class="main">
    <div class="topbar">
      <div class="crumbs">
        <span>tráfego_análise</span>
        <span class="sep">/</span>
        <span class="now" id="crumb-now">selecione um output</span>
      </div>
      <span class="status-dot"><span class="dot"></span>snapshot do dashboard</span>
    </div>

    <div class="iframe-host">
      <iframe id="output-frame" src=""></iframe>
      <div class="empty-state" id="empty-state">
        <div>Selecione um output na coluna esquerda</div>
        <div class="hint">OS DADOS APARECEM AQUI</div>
      </div>
    </div>
  </main>

</div>

<script>
  function loadOutput(fileName, navEl) {
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    if (navEl) navEl.classList.add('active');
    const frame = document.getElementById('output-frame');
    const empty = document.getElementById('empty-state');
    frame.src = fileName;
    empty.style.display = 'none';
    frame.style.display = 'block';
    // atualiza breadcrumb
    const label = navEl.querySelector('span:nth-child(2)').textContent.toLowerCase().replace(/ /g, '_');
    document.getElementById('crumb-now').textContent = label;
  }

  // Auto-carrega o primeiro output disponível ao abrir
  window.addEventListener('load', () => {
    const first = document.querySelector('.nav-item:not(.empty)');
    if (first) first.click();
  });
</script>

</body>
</html>
```

---

## 4. Mapeamento de blocos → componentes do design system

Cada um dos 9 outputs tem blocos próprios (Bloco 1, Bloco 2, etc) descritos na sua sub-skill respectiva. A regra de mapeamento é:

| Tipo de conteúdo no output narrado | Componente HTML usado |
|---|---|
| Cabeçalho de número grande (gasto total, ROAS médio, Health Score) | `.kpi-grid` com 4 a 6 `.kpi` |
| Ranking (top 5, top 10) | `.table` com colunas mono |
| Comparativo período vs período | `.table` com `.up`/`.down` |
| Distribuição por categoria (dia da semana, horário, posicionamento) | série de `.bar-row` |
| Frase "No VTSD isso significa..." | `.callout` |
| Frase "Ação recomendada..." | `.pitch-box` |
| Sinal crítico (alerta vermelho) | `.regra.alerta` |
| Status verde/amarelo/vermelho | `.chip` (`.active`, `.ochre`, `.rust`) |
| Handoff "rodar /trafego-X" | `.term.next` dentro de `.terms` |
| Evolução temporal (CPA mês a mês 6 meses) | SVG `.linechart` (gerado inline) |
| Funil completo (impressão → clique → compra) | `.table` com setas em UTF-8 (↓) ou SVG vertical |
| Bloco de texto narrativo do diagnóstico | parágrafos `<p>` com classe `card-body` |

**Regras de mapeamento:**
1. Toda métrica numérica usa fonte `--font-mono` (já vem da classe).
2. Headlines de seção sempre `.section-h` (mono caps com linha embaixo).
3. Cores categóricas:
   - `--neon` (verde lima) = positivo/winner
   - `--rust` (laranja) = perdedor/crítico
   - `--ochre` (mostarda) = atenção
   - `--plum`, `--sky` = categorias neutras quando precisar diferenciar
4. Nunca inventar cor fora da paleta do design system.
5. **Cor de fonte NUNCA pode ser escura.** O fundo do HTML é `--ink-0` (preto). Cores de texto permitidas, em ordem de hierarquia:
   - `--text-hi` (#ededea) — texto principal, headlines, valores destacados
   - `--text-mid` (#8a8a84) — texto secundário, descrições
   - `--text-dim` (#555550) — texto auxiliar, footnotes
   - `--text-faint` (#2e2e2c) — labels mono caps, separadores tipográficos
   - Cores categóricas (`--neon`, `--rust`, `--ochre`, `--plum`, `--sky`) — apenas pra destaque semântico
   **Proibido:** `#000`, `#111`, `#222`, qualquer cor com luminosidade < 30%, ou `color: black` direto. Nem em parágrafos de citação, nem em texto de tabela, nem em footnote, nem em "texto secundário". Se precisar reduzir hierarquia, usa `--text-dim` ou `--text-faint`. **Exceção única:** dentro do bloco `@media print`, onde o fundo vira branco — aí texto pode escurecer.

---

## 5. Algoritmo de geração

A skill executa **três fases**: gera o snapshot individual, regenera o `index.html` (dashboard com sidebar), e abre o `index.html` no navegador.

```
FASE 1 — Gerar snapshot individual

1. Capturar payload narrado que acabou de ser entregue ao aluno (Blocos 1, 2, 3, 4...).
2. Identificar slug do output ([1] → diagnostico-rapido, etc).
3. Ler nome do produto ativo de meus-produtos/{ativo}/perfil.md (campo Produto).
4. Calcular timestamp atual em formato YYYY-MM-DD-HHMM (local).
5. Calcular caminho final: meus-produtos/{ativo}/trafego/analise/{slug}-{timestamp}.html
6. Criar pasta trafego/analise/ se não existir.
7. Carregar template HTML da seção 3.1 + tokens da seção 3.2.
8. Substituir variáveis do header: {Output}, {Produto}, {N}, {janela}, {act_id mascarado}, {DD/MM/YYYY HH:MM}.
9. Para cada bloco do output narrado, mapear para componente HTML conforme seção 4 e injetar.
10. Para cada handoff sugerido, criar .term.next dentro do rodapé.
11. Salvar arquivo do snapshot (encoding UTF-8, sem BOM).

FASE 2 — Regenerar index.html (dashboard)

12. Listar todos os arquivos .html da pasta meus-produtos/{ativo}/trafego/analise/, exceto o próprio index.html.
13. Para cada um dos 9 slugs (diagnostico-rapido, performance-funil, criativos-copy, geo-demografia,
    timing-sazonalidade, investigacao-profunda, lifecycle-historico, problemas-ocultos, orcamento-projecao):
      a. Filtrar arquivos cujo nome começa com aquele slug.
      b. Se houver 1+ arquivo, escolher o de timestamp mais recente (parsing do sufixo YYYY-MM-DD-HHMM).
      c. Guardar (slug, nome do output, nome do arquivo mais recente, "DD/MM HH:MM" do timestamp).
      d. Se não houver nenhum, marcar como "não rodado".
14. Carregar template do index.html da seção 3.3 + tokens da seção 3.2.
15. Substituir {Produto} e {act_id mascarado} no user-block.
16. Para cada um dos 9 slugs, gerar 1 <a class="nav-item"> ou <span class="nav-item empty">:
      - Se existe snapshot: <a> com onclick=loadOutput('{nome-arquivo}.html', this) e <span class="ts">{DD/MM HH:MM}</span>
      - Se não existe: <span class="nav-item empty"> com <span class="ts">não rodado</span>
17. Salvar (sobrescreve) meus-produtos/{ativo}/trafego/analise/index.html.

FASE 3 — Abrir no navegador

18. Detectar SO (uname -s no Bash, ou variável OSTYPE) — ver seção 9.
19. Executar comando de abertura apropriado apontando para o caminho absoluto do index.html.
20. Devolver ao aluno:
    "✅ Snapshot gerado: {slug}-{timestamp}.html
     ✅ Dashboard atualizado: {caminho-absoluto-do-index.html}
     🌐 Abrindo no navegador..."
```

---

## 6. Mascarar dados sensíveis no HTML

- **`ad_account_id`**: mostrar só os 4 primeiros e 4 últimos dígitos. Ex: `act_1234******7890`.
- **IDs de campanha/adset/ad** que aparecem em rankings: mostrar últimos 4 dígitos (`...7890`) com nome legível ao lado.
- **Token de acesso, app_id, business_id**: nunca aparecer no HTML, em hipótese alguma.

A skill executa a mascaração antes de injetar no template.

---

## 7. Modo print (PDF)

O CSS já inclui `@media print` que clarifica fundo (HTML pra impressão fica branco com texto escuro). Aluno pode dar `Ctrl+P` no navegador e gerar PDF direto, sem precisar de skill adicional.

---

## 8. Princípios desta sub-skill

1. **Nunca sem confirmação.** Aluno precisa dizer "sim" pra gerar HTML.
2. **Snapshot, não live.** Banner de aviso explícito no topo + timestamp visível.
3. **Standalone.** CSS embedado, fontes via Google Fonts, zero dependência local.
4. **Naming determinístico.** `{slug}-{YYYY-MM-DD-HHMM}.html` permite ordenação cronológica e múltiplos exports do mesmo output sem sobrescrever.
5. **Pasta por produto.** Sempre `meus-produtos/{ativo}/trafego/analise/`. Nunca em pasta global, nunca na raiz.
6. **Mascara IDs.** ad_account_id, IDs internos sempre truncados.
7. **Usa só o design system Fluxo Criativo.** Sem inventar cores, fontes ou componentes fora do que está nas seções 3 e 4.
8. **Não atualiza arquivos antigos.** Cada export é arquivo novo. Histórico preservado.
9. **Mensagem final padrão:** sempre informa caminho absoluto + sugere abrir no navegador. Nunca devolve só "salvo".
10. **`index.html` regenerado a cada export.** Sem isso, o dashboard fica defasado e o aluno não vê o snapshot recém-gerado na sidebar.
11. **Snapshots individuais nunca incluem sidebar.** A sidebar mora exclusivamente no `index.html` (que carrega snapshots via iframe). Snapshot embedado precisa ser limpo, sem casca duplicada.
12. **Sempre abrir o navegador no `index.html`** (a porta de entrada), nunca no snapshot individual. O aluno entra pelo dashboard e navega.

---

## 9. Comando de abertura no navegador (cross-platform)

**Sempre executado** no fim da Fase 3 do algoritmo. Aponta para o `index.html` (não para o snapshot individual).

### 9.1 Detecção do SO

Antes de chamar o comando, descobrir o SO atual:

```bash
case "$(uname -s 2>/dev/null || echo Windows)" in
  Linux*)   SO="linux" ;;
  Darwin*)  SO="mac" ;;
  CYGWIN*|MINGW*|MSYS*|Windows*) SO="windows" ;;
  *)        SO="unknown" ;;
esac
```

Em ambientes onde `uname` não existe (PowerShell puro), assumir `windows`.

### 9.2 Comando por SO

| SO | Comando |
|---|---|
| `windows` (Bash/Git Bash) | `start "" "{caminho-absoluto-index}"` (as aspas duplas vazias são título obrigatório do `start`) |
| `windows` (PowerShell) | `Invoke-Item "{caminho-absoluto-index}"` ou `Start-Process "{caminho}"` |
| `mac` | `open "{caminho-absoluto-index}"` |
| `linux` | `xdg-open "{caminho-absoluto-index}"` |

### 9.3 Caminho absoluto (regra dura)

**Tanto o caminho do script `abrir-html.py` quanto o caminho do HTML alvo precisam ser ABSOLUTOS.** Não confiar no `cwd` do shell — ele pode estar contaminado por algum `cd` anterior na sessão.

**Forma correta (recomendada — usa o script Python helper):**

```bash
python3 "{RAIZ_PROJETO}/scripts/abrir-html.py" "{caminho-absoluto-do-index.html}"
```

Onde `{RAIZ_PROJETO}` é o caminho absoluto da raiz do workspace (descoberta no início da sessão e usada sempre — nunca relativo, nunca `./scripts/...`).

**Exemplo concreto (Windows):**

```bash
python3 "C:/Users/gabri/Documents/GitHub/workshop_inteligente/scripts/abrir-html.py" "C:/Users/gabri/Documents/GitHub/workshop_inteligente/meus-produtos/curso-tarot/trafego/analise/index.html"
```

**Forma alternativa (sem o script, comando nativo direto):**

```bash
# Windows Bash
start "" "C:/Users/gabri/Documents/GitHub/workshop_inteligente/meus-produtos/curso-tarot/trafego/analise/index.html"
```

**Erros comuns a evitar:**

| ❌ Errado | ✅ Certo | Motivo |
|---|---|---|
| `python3 scripts/abrir-html.py "..."` | `python3 "{RAIZ}/scripts/abrir-html.py" "..."` | cwd pode ter sido alterado por `cd` anterior |
| `cd meus-produtos/{ativo}/...; python3 abrir-html.py` | usar caminho absoluto pro script direto | `cd` contamina cwd pra próximas chamadas |
| `python3 ./scripts/abrir-html.py` | absoluto sempre | `./` depende de cwd |
| `start "..."` sem aspas vazias antes | `start "" "..."` | no Bash do Windows, primeiro arg é título; sem `""` o caminho vira título |

**Princípio:** o agente descobre `{RAIZ_PROJETO}` no início da sessão (path absoluto do workspace) e usa esse prefixo em TODA chamada do script. Nunca depender de cwd.

### 9.4 Falha silenciosa

Se o comando de abertura falhar (sem display em servidor remoto, ferramenta ausente), a skill **não trava**. Apenas avisa:

```
✅ Snapshot gerado: {arquivo}
✅ Dashboard atualizado: {caminho-absoluto-do-index}
⚠️ Não consegui abrir o navegador automaticamente. Abra manualmente o arquivo acima.
```

### 9.5 Mensagem padrão de sucesso

```
✅ Snapshot gerado: diagnostico-rapido-2026-05-05-1432.html
✅ Dashboard atualizado: C:\Users\gabri\...\meus-produtos\curso-tarot\trafego\analise\index.html
🌐 Abrindo no navegador...
```
