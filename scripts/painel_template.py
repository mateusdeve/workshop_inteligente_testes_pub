"""
painel_template.py

Shell HTML e funcoes de render das secoes do painel de entregas incremental.
Design: dark editorial / cyberpunk-mono (Fluxo Criativo aesthetic).

Secoes suportadas (id da secao = id do painel na sidebar):
    pesquisa
    quadro
    furadeira
    decorados
    urgencias
    identidade-produto
    identidade-consumidor
    identidade-comunicador

Cada render_* recebe um dict com os dados ja extraidos dos arquivos do produto
(perfil.md, idconsumidor.md, pesquisa-mercado.md) e devolve apenas o HTML do
miolo da secao, envolto em marcadores:

    <!-- SECTION:{id} -->...<!-- /SECTION:{id} -->

O script painel-incremental.py e responsavel por ler arquivos, popular o dict
e trocar o bloco correspondente no HTML existente, ou criar o shell inicial.
"""

from __future__ import annotations

import html
import re
from datetime import datetime
from typing import Iterable

# ----- metadados das secoes -----

SECOES: list[dict] = [
    {"id": "visao-geral", "grupo": "PRODUTO", "titulo": "Visao Geral", "ix": "01",
     "subtitulo": "Resumo do produto e informacoes principais."},
    {"id": "quadro", "grupo": "PRODUTO", "titulo": "Quadro", "ix": "02",
     "subtitulo": "A transformacao principal que o produto entrega ao cliente.",
     "proxima": "Quadro sera preenchido ao concluir o Bloco 1 de /produto-concepcao."},
    {"id": "furadeira", "grupo": "PRODUTO", "titulo": "Furadeira", "ix": "03",
     "subtitulo": "O metodo estruturado que torna visivel a eficiencia do produto.",
     "proxima": "Furadeira sera preenchida ao concluir o Bloco 2 de /produto-concepcao."},
    {"id": "decorados", "grupo": "PRODUTO", "titulo": "Decorados", "ix": "04",
     "subtitulo": "50 beneficios derivados do Quadro.",
     "proxima": "Decorados serao preenchidos ao concluir o Bloco 4 de /produto-concepcao."},
    {"id": "urgencias", "grupo": "PRODUTO", "titulo": "Urgencias Ocultas", "ix": "05",
     "subtitulo": "70 itens em 7 categorias.",
     "proxima": "Urgencias serao preenchidas ao concluir o Bloco 5 de /produto-concepcao."},
    {"id": "identidade-produto", "grupo": "IDENTIDADES", "titulo": "Identidade do Produto", "ix": "06",
     "subtitulo": "Como o produto se posiciona e se diferencia no mercado.",
     "proxima": "Sera preenchida ao concluir o Bloco 3 de /produto-concepcao."},
    {"id": "identidade-consumidor", "grupo": "IDENTIDADES", "titulo": "Identidade do Consumidor", "ix": "07",
     "subtitulo": "Perfil detalhado do cliente ideal.",
     "proxima": "Sera preenchida automaticamente no Passo 4C de /produto-concepcao."},
    {"id": "identidade-comunicador", "grupo": "IDENTIDADES", "titulo": "Identidade do Comunicador", "ix": "08",
     "subtitulo": "Tom, posicionamento e linguagem do criador.",
     "proxima": "Sera preenchida ao concluir o Bloco 3B de /produto-concepcao."},
    {"id": "comercial-playbook", "grupo": "ENTREGAS", "titulo": "Playbook Comercial", "ix": "09",
     "subtitulo": "Script de venda 1:1 por WhatsApp (middle e low ticket).",
     "proxima": "Sera preenchido ao rodar /comercial-playbook."},
    {"id": "pesquisa", "grupo": "PESQUISA", "titulo": "Pesquisa de Mercado", "ix": "10",
     "subtitulo": "Inteligencia de mercado. Use para argumentos, copy e posicionamento.",
     "proxima": "Sera preenchida ao final de /produto-novo (Ramo 2) ou do Bloco 3 de /produto-concepcao."},
    {"id": "copy-pagina", "grupo": "ENTREGAS", "titulo": "Copy da Página",
     "subtitulo": "16 blocos da página de vendas 8D. Aprove um bloco por vez em /copy-pagina.",
     "proxima": "Será preenchida conforme você aprova os blocos em /copy-pagina."},
]

SECOES_RENDERIZAVEIS = {
    s["id"] for s in SECOES if s["id"] != "visao-geral"
}

# ----- CSS -----

_CSS = """\
/* ============================================
   FLUXO CRIATIVO - Painel de Entregas
   Dark editorial / cyberpunk-mono aesthetic
============================================ */

@import url("https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap");

:root {
  --ink-0: #000000;
  --ink-1: #050505;
  --ink-2: #0b0b0b;
  --ink-3: #141414;
  --ink-4: #1c1c1c;
  --line-1: #1a1a1a;
  --line-2: #262626;
  --paper: #ededea;
  --text-hi: #ffffff;
  --text-mid: #e8e8e6;
  --text-dim: #cfcfcb;
  --text-faint: #a8a8a3;
  --neon: #c4ff5e;
  --neon-dim: #9ec947;
  --neon-deep: #4a6517;
  --neon-glow: rgba(196,255,94,0.18);
  --rust: #d97757;
  --ochre: #d4a24a;
  --plum: #9a7bb5;
  --sky: #7aa8c9;
  --font-display: "Space Grotesk", ui-sans-serif, system-ui;
  --font-body: "Inter", ui-sans-serif, system-ui;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
  --s-1:4px; --s-2:8px; --s-3:12px; --s-4:16px; --s-5:20px;
  --s-6:24px; --s-7:32px; --s-8:40px; --s-9:56px; --s-10:80px;
  --r-sm:4px; --r-md:6px; --r-lg:10px;
  --shadow-sm:0 1px 2px rgba(0,0,0,.4);
  --shadow-md:0 4px 16px rgba(0,0,0,.5);
  --shadow-glow:0 0 0 1px var(--neon-glow),0 0 24px rgba(196,255,94,.08);
  --sidebar-w:220px;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
html{scroll-behavior:smooth;color-scheme:dark;}
body{background:var(--ink-0);color:var(--text-hi);font-family:var(--font-body);font-size:13px;line-height:1.6;font-weight:300;-webkit-font-smoothing:antialiased;font-feature-settings:"ss01","cv11","tnum";overscroll-behavior:none;}
*{scrollbar-width:thin;scrollbar-color:#2a2a2a transparent;}
*::-webkit-scrollbar{width:4px;height:4px;}
*::-webkit-scrollbar-track{background:transparent;}
*::-webkit-scrollbar-thumb{background:#1f1f1f;border-radius:999px;border:2px solid transparent;background-clip:padding-box;}
*::-webkit-scrollbar-thumb:hover{background:#3a3a3a;background-clip:padding-box;border:2px solid transparent;}
*::-webkit-scrollbar-corner{background:transparent;}
::selection{background:var(--neon);color:var(--ink-0);}
a{color:inherit;text-decoration:none;}
button{font-family:inherit;}

/* App shell */
.app{display:grid;grid-template-columns:var(--sidebar-w) 1fr;min-height:100vh;}

/* Sidebar */
.sidebar{background:var(--ink-0);border-right:1px solid var(--line-1);padding:var(--s-7) 0 var(--s-5);position:sticky;top:0;height:100vh;overflow-y:auto;display:flex;flex-direction:column;}
.brand{padding:0 var(--s-5) var(--s-7);display:flex;align-items:center;gap:var(--s-3);}
.brand-mark{width:24px;height:24px;border-radius:3px;background:url("./painel-assets/logo-square.jpg") center/cover;flex-shrink:0;}
.brand-text{font-family:var(--font-mono);font-weight:400;font-size:11px;letter-spacing:.04em;line-height:1.2;color:var(--text-hi);}
.brand-text .tiny{display:block;color:var(--text-faint);font-weight:400;font-size:9px;letter-spacing:.18em;text-transform:uppercase;margin-top:3px;}
.user-block{padding:0 var(--s-5) var(--s-6);margin-bottom:var(--s-2);}
.user-block .label{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.18em;text-transform:uppercase;}
.user-block .product{font-family:var(--font-display);font-size:15px;font-weight:400;margin-top:var(--s-2);letter-spacing:-.015em;color:var(--text-hi);}
.user-block .owner{color:var(--text-dim);font-size:11px;font-weight:300;margin-top:3px;}
.product-select{width:100%;margin-top:var(--s-3);font-family:var(--font-display);font-size:12px;font-weight:400;padding:5px var(--s-3);background:var(--ink-3);border:1px solid var(--line-2);border-radius:var(--r-md);color:var(--text-hi);cursor:pointer;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 10 10'%3E%3Cpath fill='%23a8a8a3' d='M5 7L1 3h8z'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center;padding-right:24px;}
.product-select:focus{outline:none;border-color:var(--neon-deep);}
.product-select option{background:var(--ink-3);}
.nav{padding:var(--s-3) var(--s-3);flex:1;}
.nav-group{margin-bottom:var(--s-5);}
.nav-group-title{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.2em;text-transform:uppercase;padding:0 var(--s-3);margin-bottom:var(--s-2);font-weight:400;}
.nav-item{display:flex;align-items:center;gap:var(--s-3);padding:5px var(--s-3);color:var(--text-dim);font-size:12px;font-weight:300;cursor:pointer;transition:color 120ms;}
.nav-item:hover{color:var(--text-hi);}
.nav-item.active{color:var(--neon);}
.nav-item .ix{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);width:16px;flex-shrink:0;font-weight:300;}
.nav-item.active .ix{color:var(--neon);opacity:.5;}
.sidebar-footer{padding:var(--s-4) var(--s-5);}
.btn-export{width:100%;padding:6px 0;background:transparent;border:0;color:var(--text-dim);font-family:var(--font-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;transition:color 120ms;display:flex;align-items:center;justify-content:space-between;gap:var(--s-2);font-weight:300;}
.btn-export:hover{color:var(--neon);}
.btn-export .kbd{font-size:9px;color:var(--text-faint);}

/* Main */
.main{min-width:0;display:flex;flex-direction:column;}
.topbar{display:flex;align-items:center;justify-content:space-between;padding:var(--s-4) var(--s-9);background:rgba(0,0,0,.8);backdrop-filter:blur(12px);position:sticky;top:0;z-index:20;}
.crumbs{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.08em;text-transform:uppercase;font-weight:300;}
.crumbs .sep{color:var(--text-faint);margin:0 var(--s-2);}
.crumbs .now{color:var(--text-mid);}
.topbar-actions{display:flex;align-items:center;gap:var(--s-3);}
.status-dot{display:inline-flex;align-items:center;gap:var(--s-2);font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.14em;text-transform:uppercase;font-weight:300;}
.status-dot .dot{width:5px;height:5px;border-radius:50%;background:var(--neon);animation:pulse 2s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.5;}}

/* Mobile tabstrip */
.tabstrip{display:none;overflow-x:auto;padding:var(--s-3) var(--s-5);gap:var(--s-2);background:var(--ink-0);}
.tabstrip-item{flex-shrink:0;font-family:var(--font-mono);font-size:11px;color:var(--text-mid);padding:6px 10px;border-radius:999px;cursor:pointer;letter-spacing:.04em;text-transform:uppercase;white-space:nowrap;}
.tabstrip-item.active{color:var(--neon);}

/* Page */
.page{padding:var(--s-10) var(--s-9);max-width:1180px;width:100%;margin:0 auto;}
.page-head{margin-bottom:var(--s-8);display:flex;align-items:flex-end;justify-content:space-between;gap:var(--s-6);flex-wrap:wrap;}
.page-title{font-family:var(--font-display);font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1;margin:0 0 var(--s-4);}
.page-title .accent{color:var(--text-faint);font-family:var(--font-mono);font-weight:300;font-size:.45em;letter-spacing:.02em;margin-right:var(--s-3);vertical-align:.35em;}
.page-sub{color:var(--text-mid);font-size:13px;font-weight:300;max-width:560px;margin:0;}
.page-meta{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.1em;text-align:right;text-transform:uppercase;font-weight:300;}
.page-meta strong{color:var(--text-mid);font-weight:400;}

/* Hero strip (with gorilla banner default) */
.hero-strip{position:relative;overflow:hidden;aspect-ratio:1000/250;min-height:140px;background:url("./painel-assets/banner-2.jpg") center/cover;margin-bottom:var(--s-9);}
.hero-strip::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.2),transparent 40%,rgba(0,0,0,.3));pointer-events:none;}
.hero-overlay{position:absolute;bottom:var(--s-5);left:var(--s-6);display:flex;align-items:center;gap:var(--s-3);z-index:2;}
.hero-tag{font-family:var(--font-mono);font-size:9px;letter-spacing:.24em;text-transform:uppercase;color:var(--neon);font-weight:400;}
.hero-tag.dim{color:rgba(255,255,255,.5);}

/* Sections */
.section{display:none;}
.section.active{display:block;animation:fadein 240ms ease-out;}
@keyframes fadein{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}

/* Grid */
.grid{display:grid;gap:var(--s-5);}
.grid-2{grid-template-columns:repeat(2,1fr);}
.grid-3{grid-template-columns:repeat(3,1fr);}
.grid-4{grid-template-columns:repeat(4,1fr);}
.grid-5{grid-template-columns:repeat(5,1fr);}

/* Card */
.card{background:transparent;border:0;border-top:1px solid var(--line-1);border-radius:0;padding:var(--s-6) 0;transition:none;}
.card:hover{background:transparent;}
.card.glow{border-top-color:var(--neon);}
.card.flush{padding:0;overflow:hidden;}
.card-label{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.2em;text-transform:uppercase;margin-bottom:var(--s-3);display:block;font-weight:400;}
.card-title{font-family:var(--font-display);font-size:18px;font-weight:400;letter-spacing:-.015em;margin:0 0 var(--s-2);line-height:1.25;}
.card-body{color:var(--text-mid);font-size:13px;font-weight:300;}
.card-headline{font-family:var(--font-display);font-size:22px;font-weight:400;letter-spacing:-.02em;line-height:1.2;color:var(--text-hi);margin:var(--s-2) 0 0;}

/* Metric */
.metric{font-family:var(--font-mono);font-feature-settings:"tnum";font-size:32px;font-weight:300;color:var(--neon);line-height:1;letter-spacing:-.03em;}
.metric-sub{color:var(--text-mid);font-size:12px;margin-top:var(--s-3);}
.metric-trend{font-family:var(--font-mono);font-size:11px;color:var(--neon);margin-top:var(--s-2);}
.metric-trend.down{color:var(--rust);}

/* Chip */
.chip{display:inline-flex;align-items:center;gap:6px;font-family:var(--font-mono);font-size:9px;letter-spacing:.16em;text-transform:uppercase;padding:2px 0;color:var(--text-dim);font-weight:400;}
.chip.active{color:var(--neon);}
.chip.ochre{color:var(--ochre);}
.chip.rust{color:var(--rust);}
.chip.plum{color:var(--plum);}
.chip .dot{width:5px;height:5px;border-radius:50%;background:currentColor;}
.chip-group{display:flex;flex-wrap:wrap;gap:var(--s-4);}
.overview-chips{display:flex;gap:var(--s-2);flex-wrap:wrap;margin-top:var(--s-5);}
.chips-row{display:flex;flex-wrap:wrap;gap:var(--s-2);}

/* Quadro card */
.quadro-card{padding:var(--s-8) 0 var(--s-8) var(--s-7);background:transparent;border:0;border-left:1px solid var(--neon);position:relative;overflow:hidden;}
.quadro-card::before{content:"QUADRO";position:absolute;top:var(--s-5);right:0;font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.3em;font-weight:300;}
.quadro-card .big-quote{font-family:var(--font-display);font-size:26px;font-weight:300;letter-spacing:-.02em;line-height:1.3;max-width:760px;color:var(--text-hi);}
.quadro-card .big-quote .highlight{color:var(--neon);}

/* Furadeira steps */
.steps{display:flex;flex-direction:column;gap:var(--s-4);counter-reset:step;}
.step{display:grid;grid-template-columns:48px 1fr;gap:var(--s-6);padding:var(--s-5) 0;background:transparent;border:0;border-bottom:1px solid var(--line-1);border-radius:0;position:relative;}
.step:hover{background:transparent;}
.step:last-child{border-bottom:0;}
.step-num{font-family:var(--font-mono);font-size:11px;font-weight:300;color:var(--text-faint);line-height:1;letter-spacing:.1em;padding-top:6px;}
.step-num::before{content:attr(data-n);}
.step-title{font-family:var(--font-display);font-size:15px;font-weight:400;letter-spacing:-.01em;margin:0 0 var(--s-2);}
.step-desc{color:var(--text-mid);font-size:13px;font-weight:300;margin:0 0 var(--s-3);line-height:1.6;}
.step-micro{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.08em;text-transform:uppercase;display:flex;flex-wrap:wrap;gap:0;font-weight:300;}
.step-micro .tag{padding:0;}
.step-micro .tag:not(:last-child)::after{content:" · ";color:var(--text-faint);margin:0 4px;}

/* Accordion (decorados/urgencias) */
.acc{border-bottom:1px solid var(--line-1);background:transparent;overflow:hidden;}
.acc-head{display:flex;align-items:center;justify-content:space-between;padding:var(--s-4) 0;cursor:pointer;gap:var(--s-4);user-select:none;}
.acc-head:hover .acc-title{color:var(--neon);}
.acc-title{font-family:var(--font-display);font-size:14px;font-weight:400;letter-spacing:-.005em;display:flex;align-items:center;gap:var(--s-3);transition:color 120ms;}
.acc-title .cat-dot{width:4px;height:4px;border-radius:50%;background:var(--neon);}
.acc-meta{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.08em;text-transform:uppercase;font-weight:300;}
.acc-caret{color:var(--text-faint);font-size:11px;transition:transform 200ms;}
.acc.open .acc-caret{transform:rotate(180deg);color:var(--neon);}
.acc-body{display:none;padding:0 0 var(--s-6) var(--s-5);}
.acc.open .acc-body{display:block;}
.acc-list{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:var(--s-3) var(--s-6);}
.acc-list li{font-size:12px;color:var(--text-mid);padding-left:var(--s-4);position:relative;line-height:1.55;font-weight:300;}
.acc-list li::before{content:"";position:absolute;left:0;top:10px;width:4px;height:1px;background:var(--text-faint);}

/* Category colors */
.cat-dores .cat-dot{background:var(--rust);}
.cat-duvidas .cat-dot{background:var(--sky);}
.cat-desejos .cat-dot{background:var(--neon);}
.cat-relacionados .cat-dot{background:var(--plum);}
.cat-quentes .cat-dot{background:var(--ochre);}
.cat-frias .cat-dot{background:#5d7a95;}
.cat-inusitadas .cat-dot{background:#c47bb5;}

/* Objecao (identidade produto) */
.objecao{border-bottom:1px solid var(--line-1);}
.objecao-head{padding:var(--s-5) 0;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:var(--s-4);}
.objecao-head:hover .objecao-quote{color:var(--neon);}
.objecao-n{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.2em;font-weight:300;}
.objecao-quote{font-family:var(--font-display);font-size:14px;font-weight:400;font-style:italic;margin-top:4px;line-height:1.4;color:var(--text-hi);}
.objecao-body{display:none;padding:0 0 var(--s-6);padding-top:var(--s-2);}
.objecao.open .objecao-body{display:block;}
.arg{padding:var(--s-4) 0;border-bottom:1px solid var(--line-1);}
.arg:last-child{border-bottom:0;}
.arg-type{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.16em;text-transform:uppercase;font-weight:300;margin-bottom:var(--s-2);}
.arg-body{color:var(--text-mid);font-size:12px;line-height:1.7;font-weight:300;}

/* Pesquisa KPI */
.kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--s-4);margin-bottom:var(--s-8);}
.kpi{background:transparent;border:0;border-top:1px solid var(--line-1);padding:var(--s-6) 0;}
.kpi .kpi-label{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.18em;text-transform:uppercase;font-weight:400;}
.kpi .kpi-num{font-family:var(--font-mono);font-size:24px;font-weight:300;color:var(--text-hi);margin-top:var(--s-3);line-height:1;letter-spacing:-.03em;}
.kpi .kpi-foot{font-family:var(--font-mono);font-size:10px;color:var(--text-dim);margin-top:var(--s-2);font-weight:300;}
.kpi .up{color:var(--neon);}
.kpi .down{color:var(--rust);}

/* Chart cards e barras */
.chart-card h3{font-family:var(--font-display);font-size:15px;font-weight:400;margin:0 0 var(--s-2);letter-spacing:-.01em;}
.chart-card .sub{font-size:12px;color:var(--text-dim);margin-bottom:var(--s-5);font-weight:300;}
.bar-row{display:grid;grid-template-columns:140px 1fr 60px;align-items:center;gap:var(--s-4);padding:7px 0;font-size:12px;font-weight:300;}
.bar-row .bar-label{color:var(--text-hi);}
.bar-row .bar-track{height:2px;background:var(--line-1);border-radius:0;overflow:hidden;position:relative;}
.bar-row .bar-fill{height:100%;background:var(--neon);}
.bar-row .bar-val{font-family:var(--font-mono);font-size:11px;color:var(--text-mid);text-align:right;font-weight:300;}

/* Line chart SVG */
.linechart{width:100%;height:200px;}
.linechart .area{fill:url(#neonFade);}
.linechart .line{stroke:var(--neon);stroke-width:1.5;fill:none;}
.linechart .dot{fill:var(--neon);}
.linechart .axis text{font-family:var(--font-mono);font-size:10px;fill:var(--text-dim);letter-spacing:.06em;}
.linechart .axis line{stroke:var(--line-1);}

/* Price scale */
.price-scale{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin:var(--s-6) 0 var(--s-5);position:relative;}
.price-scale .tick{text-align:center;padding:var(--s-3) 0;border-top:1px solid var(--line-1);position:relative;}
.price-scale .tick:last-child{border-right:0;}
.price-scale .tick .p{font-family:var(--font-mono);font-size:14px;color:var(--text-hi);font-weight:300;letter-spacing:-.02em;}
.price-scale .tick .f{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.12em;text-transform:uppercase;margin-top:4px;font-weight:300;}
.price-scale .tick.me{border-top-color:var(--neon);}
.price-scale .tick.me .p{color:var(--neon);}
.price-scale .tick.me::after{content:"SEU PRODUTO";position:absolute;bottom:-26px;left:50%;transform:translateX(-50%);font-family:var(--font-mono);font-size:9px;color:var(--neon);letter-spacing:.18em;white-space:nowrap;}

/* Table */
.table{width:100%;border-collapse:collapse;font-size:12px;font-weight:300;}
.table thead th{text-align:left;font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.18em;text-transform:uppercase;padding:var(--s-3) var(--s-4) var(--s-3) 0;border-bottom:1px solid var(--line-1);font-weight:400;}
.table tbody td{padding:var(--s-3) var(--s-4) var(--s-3) 0;border-bottom:1px solid var(--line-1);color:var(--text-mid);}
.table tbody tr:hover td{color:var(--text-hi);}
.table tbody td.strong{color:var(--text-hi);font-weight:400;}
.table tbody td.mono{font-family:var(--font-mono);font-size:11px;}

/* Terms (keyword pills) */
.terms{display:flex;flex-wrap:wrap;gap:var(--s-2);}
.term{font-family:var(--font-mono);font-size:11px;padding:4px 10px;border:1px solid var(--line-1);border-radius:999px;color:var(--text-mid);transition:color 120ms;}
.term:hover{color:var(--neon);}
.term.danger{color:var(--rust);}

/* Confidence ring */
.conf-ring{display:flex;align-items:center;gap:var(--s-5);}
.ring-svg{width:80px;height:80px;}
.ring-bg{fill:none;stroke:var(--line-1);stroke-width:4;}
.ring-fg{fill:none;stroke:var(--neon);stroke-width:4;stroke-linecap:butt;}
.ring-val{font-family:var(--font-mono);font-size:18px;font-weight:300;fill:var(--text-hi);text-anchor:middle;dominant-baseline:central;letter-spacing:-.03em;}

/* Comp row (concorrentes simples) */
.comp-row{display:flex;align-items:center;gap:var(--s-4);padding:var(--s-4) 0;border-bottom:1px solid var(--line-1);}
.comp-row:last-child{border-bottom:0;}
.comp-avatar{width:28px;height:28px;border-radius:3px;background:transparent;border:1px solid var(--line-1);display:grid;place-items:center;font-family:var(--font-mono);font-weight:400;font-size:11px;color:var(--text-mid);flex-shrink:0;}
.comp-name{font-weight:400;color:var(--text-hi);font-size:13px;}
.comp-links{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);margin-top:3px;letter-spacing:.04em;}
.comp-links a{margin-right:var(--s-3);}
.comp-links a:hover{color:var(--neon);}
.comp-price{margin-left:auto;font-family:var(--font-mono);font-weight:300;color:var(--text-hi);font-size:13px;}

/* Callout */
.callout{padding:var(--s-3) 0 var(--s-3) var(--s-5);border-left:1px solid var(--neon);background:transparent;font-family:var(--font-display);font-size:14px;font-style:italic;font-weight:300;margin:var(--s-3) 0;color:var(--text-hi);line-height:1.5;}

/* Misc */
.section-h{font-family:var(--font-mono);font-size:10px;font-weight:400;letter-spacing:.2em;text-transform:uppercase;color:var(--text-faint);margin:var(--s-10) 0 var(--s-5);padding-bottom:var(--s-3);border-bottom:1px solid var(--line-1);display:flex;align-items:center;justify-content:space-between;}
.section-h .mini{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.16em;text-transform:uppercase;font-weight:300;}
.dt-list{display:grid;grid-template-columns:160px 1fr;gap:var(--s-3) var(--s-6);font-size:12px;font-weight:300;}
.dt-list dt{color:var(--text-faint);font-family:var(--font-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;padding-top:2px;font-weight:300;}
.dt-list dd{margin:0;color:var(--text-hi);}
.pill-list{display:flex;flex-wrap:wrap;gap:var(--s-2);}
.pill{font-family:var(--font-mono);font-size:11px;padding:4px 10px;border:1px solid var(--line-2);border-radius:999px;color:var(--text-mid);}
.pill.neon{border-color:var(--neon-deep);color:var(--neon);}
.pill.rust{border-color:#6b3020;color:var(--rust);}
.placeholder-box{padding:var(--s-10) 0;text-align:center;border-top:1px solid var(--line-1);}
.placeholder-box .ph-title{font-family:var(--font-display);font-size:18px;font-weight:300;color:var(--text-dim);margin-bottom:var(--s-3);}
.placeholder-box .ph-sub{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.12em;text-transform:uppercase;max-width:440px;margin:0 auto;line-height:1.8;}

/* ============================================
   PLAYBOOK - WhatsApp mockup, DEF/SPIN, recovery
============================================ */

/* WhatsApp bubbles */
.wa-frame{background:var(--ink-1);border:1px solid var(--line-1);border-radius:var(--r-md);padding:var(--s-5) var(--s-5) var(--s-6);position:relative;}
.wa-frame::before{content:"";position:absolute;inset:0;border-radius:inherit;background-image:radial-gradient(circle at 12% 18%,rgba(196,255,94,0.04),transparent 40%),radial-gradient(circle at 88% 82%,rgba(196,255,94,0.03),transparent 40%);pointer-events:none;}
.wa-head{display:flex;align-items:center;gap:var(--s-3);padding-bottom:var(--s-3);margin-bottom:var(--s-4);border-bottom:1px solid var(--line-1);position:relative;}
.wa-ava{width:28px;height:28px;border-radius:50%;background:var(--ink-3);border:1px solid var(--line-2);display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-size:10px;color:var(--text-faint);flex-shrink:0;}
.wa-head .who{font-size:12px;color:var(--text-hi);font-weight:400;}
.wa-head .who .sub{display:block;font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.14em;text-transform:uppercase;margin-top:2px;font-weight:300;}
.wa-head .tag{margin-left:auto;font-family:var(--font-mono);font-size:9px;color:var(--neon);letter-spacing:.16em;text-transform:uppercase;}
.wa-thread{display:flex;flex-direction:column;gap:var(--s-3);position:relative;}
.wa-row{display:flex;}
.wa-row.out{justify-content:flex-end;}
.wa-row.sys{justify-content:center;margin:var(--s-2) 0;}
.wa-bubble{max-width:78%;padding:10px 13px;border-radius:10px;font-size:13px;line-height:1.55;color:var(--text-hi);font-weight:300;position:relative;}
.wa-bubble.out{background:rgba(196,255,94,0.08);border:1px solid rgba(196,255,94,0.22);border-bottom-right-radius:3px;}
.wa-bubble.in{background:var(--ink-3);border:1px solid var(--line-2);color:var(--text-mid);border-bottom-left-radius:3px;}
.wa-bubble .time{display:block;font-family:var(--font-mono);font-size:9px;color:var(--text-faint);margin-top:4px;letter-spacing:.08em;}
.wa-sys{font-family:var(--font-mono);font-size:9px;letter-spacing:.22em;text-transform:uppercase;color:var(--text-faint);padding:3px 10px;border:1px solid var(--line-1);border-radius:999px;background:var(--ink-1);}

/* Stage (numbered step in a sequence) */
.stage{border-bottom:1px solid var(--line-1);padding:var(--s-6) 0;display:grid;grid-template-columns:220px 1fr 1fr;gap:var(--s-6);}
.stage:last-child{border-bottom:0;}
.stage-head{padding-right:var(--s-5);border-right:1px solid var(--line-1);}
.stage-n{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.2em;margin-bottom:var(--s-2);}
.stage-title{font-family:var(--font-display);font-size:16px;font-weight:500;letter-spacing:-.01em;color:var(--text-hi);margin-bottom:var(--s-3);line-height:1.25;}
.stage-hint{font-size:12px;color:var(--text-mid);font-weight:300;line-height:1.55;margin-bottom:var(--s-3);}
.stage-nota{margin-top:var(--s-3);padding-top:var(--s-3);border-top:1px solid var(--line-1);font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.04em;line-height:1.7;font-weight:300;}
.stage-nota::before{content:"NOTA \00b7 ";color:var(--neon);letter-spacing:.18em;}
.stage-col-label{font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.18em;text-transform:uppercase;margin-bottom:var(--s-3);display:flex;align-items:center;gap:6px;}
.stage-col-label .dot{width:4px;height:4px;border-radius:50%;background:var(--neon);}
.stage-col-label.direta .dot{background:var(--ochre);}

/* DEF / SPIN cards */
.def-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--s-5);margin-top:var(--s-5);}
.spin-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:var(--s-5);margin-top:var(--s-5);}
.letra-card{border:1px solid var(--line-1);padding:var(--s-6);position:relative;}
.letra-card .letra{font-family:var(--font-display);font-size:64px;font-weight:500;color:var(--neon);line-height:.9;letter-spacing:-.04em;margin-bottom:var(--s-2);}
.letra-card .letra-nome{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.2em;text-transform:uppercase;margin-bottom:var(--s-4);}
.letra-card .letra-title{font-family:var(--font-display);font-size:18px;font-weight:500;margin-bottom:var(--s-3);color:var(--text-hi);letter-spacing:-.015em;}
.letra-card .letra-obj{font-size:12px;color:var(--text-mid);margin-bottom:var(--s-4);line-height:1.55;font-weight:300;}
.letra-card .letra-sinal{font-family:var(--font-mono);font-size:10px;color:var(--neon);letter-spacing:.08em;padding:var(--s-2) 0;border-top:1px solid var(--line-1);border-bottom:1px solid var(--line-1);margin-bottom:var(--s-3);font-weight:300;line-height:1.5;}
.letra-card .letra-sinal::before{content:"\2192 ";color:var(--neon);}
.letra-frase{font-family:var(--font-display);font-size:13px;color:var(--text-hi);line-height:1.55;font-weight:400;font-style:italic;padding:var(--s-3) 0;border-bottom:1px dashed var(--line-1);}
.letra-frase:last-child{border-bottom:0;}
.letra-frase::before{content:"\201C";color:var(--text-faint);font-family:var(--font-display);font-size:20px;margin-right:4px;opacity:.4;}
.spin-card{border:1px solid var(--line-1);padding:var(--s-6);}
.spin-card .perguntas{list-style:none;padding:0;margin:0;counter-reset:spinq;}
.spin-card .perguntas li{padding:var(--s-3) 0;border-bottom:1px dashed var(--line-1);font-size:13px;line-height:1.55;color:var(--text-hi);font-weight:300;counter-increment:spinq;display:grid;grid-template-columns:32px 1fr;gap:var(--s-3);}
.spin-card .perguntas li:last-child{border-bottom:0;}
.spin-card .perguntas li::before{content:counter(spinq,decimal-leading-zero);font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.1em;padding-top:3px;}

/* Recovery / timeline */
.tl{position:relative;padding-left:36px;margin-top:var(--s-5);}
.tl::before{content:"";position:absolute;left:11px;top:8px;bottom:8px;width:1px;background:var(--line-1);}
.tl-item{position:relative;padding:var(--s-5) 0 var(--s-7);}
.tl-item::before{content:"";position:absolute;left:-30px;top:30px;width:9px;height:9px;border-radius:50%;background:var(--ink-0);border:1px solid var(--neon);box-shadow:0 0 0 3px var(--ink-0);}
.tl-when{font-family:var(--font-mono);font-size:10px;color:var(--neon);letter-spacing:.2em;text-transform:uppercase;margin-bottom:2px;}
.tl-title{font-family:var(--font-display);font-size:16px;font-weight:500;color:var(--text-hi);letter-spacing:-.01em;margin-bottom:var(--s-2);}
.tl-hint{font-size:12px;color:var(--text-mid);font-weight:300;line-height:1.55;margin-bottom:var(--s-4);}

/* Offer cards (upsell/downsell/bump) */
.offer-card{border:1px solid var(--line-1);padding:var(--s-6);position:relative;}
.offer-card.neon{border-color:var(--neon-deep);}
.offer-kind{font-family:var(--font-mono);font-size:9px;color:var(--neon);letter-spacing:.22em;text-transform:uppercase;margin-bottom:var(--s-3);}
.offer-title{font-family:var(--font-display);font-size:20px;font-weight:500;letter-spacing:-.015em;color:var(--text-hi);margin-bottom:var(--s-2);}
.offer-price{font-family:var(--font-mono);font-size:14px;color:var(--neon);letter-spacing:.04em;margin-bottom:var(--s-4);}
.offer-desc{font-size:12px;color:var(--text-mid);font-weight:300;line-height:1.6;margin-bottom:var(--s-4);}
.offer-pitch{font-family:var(--font-display);font-size:13px;color:var(--text-hi);font-style:italic;line-height:1.55;font-weight:400;padding-top:var(--s-4);border-top:1px solid var(--line-1);}
.offer-pitch::before{content:"PITCH \00b7 ";font-style:normal;font-family:var(--font-mono);font-size:9px;color:var(--text-faint);letter-spacing:.2em;display:block;margin-bottom:6px;}

/* Dictionary */
.dict-grid{display:grid;grid-template-columns:repeat(2,1fr);border-top:1px solid var(--line-1);}
.dict-item{padding:var(--s-4) var(--s-5);border-bottom:1px solid var(--line-1);display:grid;grid-template-columns:140px 1fr;gap:var(--s-4);}
.dict-item:nth-child(odd){border-right:1px solid var(--line-1);}
.dict-item dt{font-family:var(--font-mono);font-size:11px;color:var(--neon);letter-spacing:.04em;font-weight:400;padding-top:2px;}
.dict-item dd{margin:0;font-size:12px;color:var(--text-mid);font-weight:300;line-height:1.55;}

/* Pitch intro box */
.pitch-box{border-left:2px solid var(--neon);padding:var(--s-4) var(--s-5);background:linear-gradient(90deg,rgba(196,255,94,0.04),transparent 60%);margin:var(--s-5) 0 var(--s-6);font-size:13px;line-height:1.65;color:var(--text-mid);font-weight:300;}

/* Preco blocks list */
.pblock{border-bottom:1px solid var(--line-1);padding:var(--s-6) 0;display:grid;grid-template-columns:260px 1fr;gap:var(--s-6);}
.pblock:last-child{border-bottom:0;}
.pblock-head .num{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.2em;margin-bottom:var(--s-2);}
.pblock-head .t{font-family:var(--font-display);font-size:18px;font-weight:500;letter-spacing:-.015em;color:var(--text-hi);margin-bottom:var(--s-3);line-height:1.3;}
.pblock-head .hint{font-size:12px;color:var(--text-mid);font-weight:300;line-height:1.55;}

/* Regra / callout destaque */
.regra{margin-top:var(--s-5);padding:var(--s-4) var(--s-5);border:1px solid var(--neon-deep);background:rgba(196,255,94,0.04);font-family:var(--font-mono);font-size:11px;color:var(--text-hi);letter-spacing:.02em;line-height:1.7;font-weight:300;}
.regra::before{content:"REGRA \00b7 ";color:var(--neon);letter-spacing:.2em;font-weight:500;}

/* YouTube cards (pesquisa de mercado) */
.yt-video-card{border-top:1px solid var(--line-1);overflow:hidden;}
.yt-video-header{display:flex;align-items:center;gap:var(--s-4);padding:var(--s-4) 0;cursor:pointer;user-select:none;}
.yt-video-header:hover .yt-title{color:var(--neon);}
.yt-rank{font-family:var(--font-mono);font-size:11px;color:var(--text-faint);width:20px;flex-shrink:0;text-align:right;}
.yt-thumb{width:72px;height:40px;border-radius:3px;border:1px solid var(--line-1);display:flex;align-items:center;justify-content:center;font-size:11px;color:var(--text-faint);flex-shrink:0;font-family:var(--font-mono);}
.yt-info{flex:1;min-width:0;}
.yt-title{font-size:13px;color:var(--text-hi);font-weight:400;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;transition:color .15s;}
.yt-canal{font-family:var(--font-mono);font-size:10px;color:var(--text-faint);letter-spacing:.04em;margin-top:2px;}
.yt-meta{font-size:11px;color:var(--text-dim);margin-top:3px;display:flex;align-items:center;gap:var(--s-3);}
.yt-toggle{font-size:10px;color:var(--text-faint);flex-shrink:0;transition:transform .2s;margin-left:auto;}
.yt-open .yt-toggle{transform:rotate(180deg);}
.yt-detail{display:none;padding:var(--s-3) 0 var(--s-5) calc(20px + var(--s-4) + 72px + var(--s-4));border-top:1px solid var(--line-1);}
.yt-open .yt-detail{display:block;}
.yt-section-title{font-family:var(--font-mono);font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--text-faint);margin:var(--s-4) 0 var(--s-2);}
.yt-comment{font-size:12px;color:var(--text-mid);font-style:italic;padding:var(--s-2) 0;border-bottom:1px solid var(--line-1);font-weight:300;line-height:1.55;}
.yt-comment:last-of-type{border-bottom:0;}
.yt-insight{font-size:12px;color:var(--text-mid);line-height:1.55;font-weight:300;margin-bottom:var(--s-2);}
.yt-thumb-detail{font-size:12px;color:var(--text-mid);line-height:1.55;font-weight:300;}

@media(max-width:1100px){
  .stage{grid-template-columns:1fr;}
  .stage-head{border-right:0;border-bottom:1px solid var(--line-1);padding:0 0 var(--s-4);}
  .def-grid,.spin-grid{grid-template-columns:1fr;}
  .dict-grid{grid-template-columns:1fr;}
  .dict-item:nth-child(odd){border-right:0;}
  .pblock{grid-template-columns:1fr;}
}

@media(max-width:960px){
  .app{grid-template-columns:1fr;}
  .sidebar{display:none;}
  .tabstrip{display:flex;}
  .page{padding:var(--s-6) var(--s-5);}
  .page-title{font-size:32px;}
  .grid-2,.grid-3,.grid-4,.grid-5{grid-template-columns:1fr;}
  .kpi-grid{grid-template-columns:1fr 1fr;}
  .acc-list{grid-template-columns:1fr;}
}
@media print{
  .sidebar,.topbar,.tabstrip{display:none;}
  .app{grid-template-columns:1fr;}
  .section{display:block!important;}
  .acc-body,.objecao-body{display:block!important;}
}"""

# ----- JS -----

_JS = """\
(function(){
  var NAV_IDS = Array.from(document.querySelectorAll('.nav-item')).map(function(el){return el.dataset.id;});

  function show(id){
    document.querySelectorAll('.section').forEach(function(s){s.classList.remove('active');});
    document.querySelectorAll('.nav-item').forEach(function(n){n.classList.remove('active');});
    document.querySelectorAll('.tabstrip-item').forEach(function(t){t.classList.remove('active');});
    var s = document.getElementById('section-'+id);
    if(s) s.classList.add('active');
    document.querySelectorAll('[data-id="'+id+'"]').forEach(function(el){el.classList.add('active');});
    var crumb = document.getElementById('crumb-now');
    if(crumb) crumb.textContent = id.replace(/-/g,'_');
    if(history.replaceState) history.replaceState(null,'','#'+id);
  }

  function toggleAcc(head){
    head.closest('.acc').classList.toggle('open');
  }
  function toggleObjecao(head){
    head.closest('.objecao').classList.toggle('open');
  }

  document.addEventListener('DOMContentLoaded', function(){
    var hash = location.hash.replace('#','');
    show(hash || 'visao-geral');
  });

  window.showPanel = show;
  window.toggleAcc = toggleAcc;
  window.toggleObjecao = toggleObjecao;

  // Seletor de produtos: carrega ../index.js e popula o <select>
  function initProductSelect() {
    var sel = document.getElementById('product-select');
    if (!sel) return;
    var manifest = window.MEUS_PRODUTOS;
    if (!manifest || !manifest.produtos || !manifest.produtos.length) {
      sel.style.display = 'none';
      return;
    }
    var parts = location.pathname.split('/').filter(Boolean);
    var currentSlug = parts[parts.length - 2] || '';
    manifest.produtos.forEach(function(p) {
      var opt = document.createElement('option');
      opt.value = p.slug;
      opt.textContent = p.nome || p.slug;
      if (p.slug === currentSlug) opt.selected = true;
      sel.appendChild(opt);
    });
    sel.addEventListener('change', function() {
      var slug = sel.value;
      location.href = '../' + slug + '/painel-entregas.html';
    });
  }

  var s = document.createElement('script');
  s.src = '../index.js';
  s.onload = function() { initProductSelect(); };
  s.onerror = function() {
    var sel = document.getElementById('product-select');
    if (sel) sel.style.display = 'none';
  };
  document.head.appendChild(s);
})();"""


def _escape(value: str | None) -> str:
    if not value:
        return ""
    return html.escape(str(value), quote=True)


def _md(value: str | None) -> str:
    """Escapa HTML e converte **bold** para <strong>."""
    escaped = _escape(value)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escaped)


def _placeholder(proxima: str) -> str:
    return (
        '<div class="placeholder-box">'
        '<div class="ph-title">Em breve</div>'
        f'<div class="ph-sub">{_escape(proxima)}</div>'
        "</div>"
    )


def _sidebar_items() -> str:
    partes: list[str] = []
    grupo_atual = None
    for secao in SECOES:
        if secao["grupo"] != grupo_atual:
            grupo_atual = secao["grupo"]
            partes.append(f'<div class="nav-group-title">{grupo_atual}</div>')
        sid = secao["id"]
        ix = secao.get("ix", "")
        partes.append(
            f'<div class="nav-item" data-id="{sid}" onclick="showPanel(\'{sid}\')">'
            f'<span class="ix">{ix}</span>'
            f'<span>{_escape(secao["titulo"])}</span>'
            "</div>"
        )
    return "\n".join(partes)


def _tabstrip_items() -> str:
    return "\n".join(
        f'<div class="tabstrip-item" data-id="{s["id"]}" onclick="showPanel(\'{s["id"]}\')">'
        f'{_escape(s["titulo"])}</div>'
        for s in SECOES
    )


def _hero_strip(banner_url: str = "", tags: list[str] | None = None) -> str:
    """Hero strip full-width acima do page-head. Aparece apenas na Visao Geral."""
    bg = f' style="background-image:url(\'{_escape(banner_url)}\')"' if banner_url else ""
    overlay = ""
    if tags:
        spans = "".join(
            f'<span class="hero-tag{"" if i == 0 else " dim"}">{_escape(t)}</span>'
            for i, t in enumerate(tags)
        )
        overlay = f'<div class="hero-overlay">{spans}</div>'
    return (
        f'<!-- HERO:visao-geral -->'
        f'<div class="hero-strip"{bg}>{overlay}</div>'
        f'<!-- /HERO:visao-geral -->'
    )


def render_hero_visao_geral(banner_url: str = "", tags: list[str] | None = None) -> str:
    """Funcao publica que devolve o bloco HERO:visao-geral pronto para substituicao."""
    return _hero_strip(banner_url, tags)


def _page_meta(timestamp: str = "") -> str:
    ts = timestamp or datetime.now().strftime("%d/%m/%Y %H:%M")
    return (
        '<div class="page-meta">'
        f'Última atualização<br/><strong>{_escape(ts)}</strong>'
        '</div>'
    )


def _all_sections(nome_produto: str, timestamp: str = "") -> str:
    partes: list[str] = []
    for secao in SECOES:
        sid = secao["id"]
        ix = secao.get("ix", "")
        titulo = secao["titulo"]
        subtitulo = secao["subtitulo"]
        if sid == "visao-geral":
            conteudo = render_visao_geral({"nome_produto": nome_produto, "secoes_prontas": []})
            hero = _hero_strip()
            page_meta = _page_meta(timestamp)
        else:
            conteudo = (
                f'<!-- SECTION:{sid} -->\n'
                + _placeholder(secao.get("proxima", "Em breve."))
                + f'\n<!-- /SECTION:{sid} -->'
            )
            hero = ""
            page_meta = ""
        partes.append(
            f'<div class="section" id="section-{sid}">'
            f'{hero}'
            f'<div class="page">'
            f'<div class="page-head">'
            f'<div>'
            f'<h1 class="page-title"><span class="accent">{ix}/</span>{_escape(titulo)}</h1>'
            f'<p class="page-sub">{_escape(subtitulo)}</p>'
            f'</div>'
            f'{page_meta}'
            f'</div>'
            f'{conteudo}'
            f'</div>'
            f'</div>'
        )
    return "\n".join(partes)


def build_shell(nome_produto: str, owner: str = "", timestamp: str = "") -> str:
    all_sections = _all_sections(nome_produto, timestamp)
    owner_html = (
        f'<div class="owner">{_escape(owner)}</div>' if owner else ""
    )
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Painel de Entregas - Fluxo Criativo</title>
<style>
{_CSS}
</style>
</head>
<body>
<div class="app">
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-mark" aria-hidden="true"></div>
      <div class="brand-text">fluxo<br/>criativo<span class="tiny">Painel &middot; v1.0</span></div>
    </div>
    <div class="user-block">
      <div class="label">Produto ativo</div>
      <div class="product" id="sidebar-product">{_escape(nome_produto)}</div>
      {owner_html}
      <select class="product-select" id="product-select" title="Trocar produto"></select>
    </div>
    <nav class="nav">
{_sidebar_items()}
    </nav>
    <div class="sidebar-footer">
      <button class="btn-export" onclick="window.print()">
        <span>Exportar PDF</span>
        <span class="kbd">Ctrl+P</span>
      </button>
    </div>
  </aside>
  <main class="main">
    <div class="topbar">
      <div class="crumbs">
        <span>painel_de_entregas</span>
        <span class="sep">/</span>
        <span class="now" id="crumb-now">visao_geral</span>
      </div>
      <div class="topbar-actions">
        <span class="status-dot"><span class="dot"></span>produto ativo</span>
      </div>
    </div>
    <div class="tabstrip">
{_tabstrip_items()}
    </div>
    <div id="pages">
{all_sections}
    </div>
  </main>
</div>
<script>
{_JS}
</script>
</body>
</html>
"""


# ----- helpers de render -----

def _ul(items: Iterable[str], cls: str = "acc-list") -> str:
    lis = "".join(f"<li>{_md(i)}</li>" for i in items if i)
    if not lis:
        return '<p class="card-body" style="margin-top:var(--s-3)">Nenhum item ainda.</p>'
    return f'<ul class="{cls}">{lis}</ul>'


def _acc(cat_cls: str, titulo: str, meta: str, items: list[str], open_: bool = False) -> str:
    open_cls = " open" if open_ else ""
    lis = "".join(f"<li>{_md(i)}</li>" for i in items)
    return (
        f'<div class="acc{open_cls} {cat_cls}">'
        '<div class="acc-head" onclick="toggleAcc(this)">'
        f'<div class="acc-title"><span class="cat-dot"></span>{_escape(titulo)}</div>'
        '<div style="display:flex;align-items:center;gap:16px">'
        f'<span class="acc-meta">{_escape(meta)}</span>'
        '<span class="acc-caret">&#9662;</span>'
        "</div>"
        "</div>"
        '<div class="acc-body">'
        f'<ul class="acc-list">{lis}</ul>'
        "</div>"
        "</div>"
    )


def _pills(items: Iterable[str], cls: str = "") -> str:
    pill_cls = f"pill {cls}".strip()
    pills = "".join(f'<span class="{pill_cls}">{_escape(i)}</span>' for i in items if i)
    return f'<div class="pill-list">{pills}</div>' if pills else ""


# ----- renders por secao -----

def render_visao_geral(dados: dict) -> str:
    nome = dados.get("nome_produto") or "(sem nome)"
    tipo = dados.get("tipo") or "a definir"
    preco = dados.get("preco") or "a definir"
    quadro = dados.get("quadro") or "Quadro ainda nao definido."
    nicho = dados.get("nicho") or "a definir"
    diferencial = dados.get("diferencial") or "a definir"
    secoes_prontas: list[str] = dados.get("secoes_prontas") or []

    chips_prontas = "".join(
        f'<span class="chip active"><span class="dot"></span>{_escape(s)}</span>'
        for s in secoes_prontas
    )
    chips_base = (
        f'<span class="chip active"><span class="dot"></span>produto ativo</span>'
        f'<span class="chip">{_escape(tipo)}</span>'
        f'<span class="chip">{_escape(preco)}</span>'
    )

    grid1 = (
        '<div class="grid grid-3" style="margin-bottom:var(--s-7)">'
        f'<div class="card"><span class="card-label">Nome do produto</span>'
        f'<div class="card-headline">{_escape(nome)}</div></div>'
        f'<div class="card"><span class="card-label">Tipo</span>'
        f'<div class="card-headline">{_escape(tipo)}</div></div>'
        f'<div class="card"><span class="card-label">Preco</span>'
        f'<div class="metric" style="font-size:32px">{_escape(preco)}</div></div>'
        "</div>"
    )
    quadro_box = (
        f'<div class="quadro-card" style="margin-bottom:var(--s-7)">'
        f'<div class="big-quote">{_escape(quadro)}</div>'
        "</div>"
    )
    grid2 = (
        '<div class="grid grid-2" style="margin-bottom:var(--s-5)">'
        f'<div class="card"><span class="card-label">Nicho</span>'
        f'<div class="card-headline" style="font-size:20px">{_escape(nicho)}</div></div>'
        f'<div class="card glow"><span class="card-label">Diferencial</span>'
        f'<div class="card-headline" style="font-size:20px;color:var(--neon)">{_escape(diferencial)}</div></div>'
        "</div>"
    )
    status = f'<div class="chip-group">{chips_base}{chips_prontas}</div>'

    return (
        f'<!-- SECTION:visao-geral -->\n{grid1}{quadro_box}{grid2}{status}\n<!-- /SECTION:visao-geral -->'
    )


def render_quadro(dados: dict) -> str:
    quadro = dados.get("quadro") or ""
    if not quadro:
        miolo = _placeholder("Aguardando Quadro do Bloco 1.")
    else:
        miolo = (
            f'<div class="quadro-card" style="margin-bottom:var(--s-8)">'
            f'<div class="big-quote">"{_escape(quadro)}"</div>'
            "</div>"
            '<div class="grid grid-2">'
            '<div class="card"><span class="card-label">Como usar o Quadro</span>'
            '<h3 class="card-title">Presente em toda a comunicacao</h3>'
            '<p class="card-body">O Quadro aparece na headline da pagina de vendas, '
            'na primeira linha de emails, nos ganchos de anuncios e no primeiro slide de carrossel. '
            'E a promessa central que ancora toda a copy.</p></div>'
            '<div class="card"><span class="card-label">Regra do Quadro</span>'
            '<h3 class="card-title">Teste obrigatorio</h3>'
            '<p class="card-body">O aluno pode dizer que isso aconteceu na vida dele ao final do produto? '
            'Se sim, o Quadro esta correto. O Quadro sempre descreve o resultado final, '
            'nunca o processo ou os modulos.</p></div>'
            "</div>"
        )
    return f"<!-- SECTION:quadro -->\n{miolo}\n<!-- /SECTION:quadro -->"


def render_furadeira(dados: dict) -> str:
    nome_metodo = dados.get("nome_metodo") or ""
    mecanica = dados.get("mecanica") or ""
    eficiencia = dados.get("eficiencia") or ""
    macroetapas: list[dict] = dados.get("macroetapas") or []
    furadeira_png = dados.get("furadeira_png") or ""

    if not nome_metodo and not macroetapas and not furadeira_png:
        miolo = _placeholder("Aguardando Furadeira do Bloco 2.")
    else:
        steps_html = ""
        for idx, m in enumerate(macroetapas, start=1):
            titulo = m.get("titulo") or f"Etapa {idx}"
            desc = m.get("descricao") or ""
            n_str = f"0{idx}" if idx < 10 else str(idx)
            steps_html += (
                f'<div class="step">'
                f'<div class="step-num">{n_str}</div>'
                "<div>"
                f'<h3 class="step-title">{_escape(titulo)}</h3>'
                f'<p class="step-desc">{_escape(desc)}</p>'
                "</div>"
                "</div>"
            )

        badges_html = ""
        if mecanica:
            badges_html += (
                f'<span style="display:inline-block;background:var(--neon-deep);color:var(--bg-1);'
                'font-family:var(--font-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;'
                'padding:4px 10px;border-radius:999px;margin-right:8px;margin-bottom:8px;">'
                f'{_escape(mecanica)}</span>'
            )
        if eficiencia:
            badges_html += (
                f'<span style="display:inline-block;background:transparent;color:var(--neon);'
                'border:1px solid var(--neon-deep);'
                'font-family:var(--font-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;'
                'padding:3px 10px;border-radius:999px;margin-bottom:8px;">'
                f'Eficiencia: {_escape(eficiencia)}</span>'
            )

        imagem_html = ""
        if furadeira_png:
            imagem_html = (
                f'<div style="margin-top:var(--s-7);padding:var(--s-5);background:var(--bg-2);'
                'border:1px solid var(--border);border-radius:8px;text-align:center;">'
                f'<img src="{_escape(furadeira_png)}" alt="Furadeira do metodo" '
                'style="max-width:100%;height:auto;border-radius:4px;display:block;margin:0 auto;" />'
                '</div>'
            )

        miolo = (
            f'<div class="card" style="margin-bottom:var(--s-7)">'
            f'<span class="card-label">Nome do metodo</span>'
            f'<div class="card-headline" style="font-size:32px;color:var(--neon)">{_escape(nome_metodo or "(sem nome)")}</div>'
            f'<div style="margin-top:var(--s-5)">{badges_html}</div>'
            "</div>"
            f'<div class="steps">{steps_html}</div>'
            f"{imagem_html}"
        )
    return f"<!-- SECTION:furadeira -->\n{miolo}\n<!-- /SECTION:furadeira -->"


_DECORADOS_CATS = [
    ("Financeiro", ""),
    ("Tempo", ""),
    ("Autoestima", ""),
    ("Reputacao", ""),
    ("Crescimento", ""),
]


def render_decorados(dados: dict) -> str:
    categorias: dict[str, list[str]] = dados.get("decorados") or {}
    total = sum(len(v) for v in categorias.values())
    if total == 0:
        miolo = _placeholder("Aguardando Decorados do Bloco 4.")
    else:
        partes = []
        for idx, (nome, _) in enumerate(_DECORADOS_CATS):
            itens = categorias.get(nome) or categorias.get(nome.lower()) or []
            partes.append(
                _acc("", nome, f"{len(itens)} beneficios", itens, open_=(idx == 0))
            )
        miolo = "".join(partes)
    return f"<!-- SECTION:decorados -->\n{miolo}\n<!-- /SECTION:decorados -->"


_URGENCIAS_CATS = [
    ("Dores", "cat-dores", "O que incomoda"),
    ("Duvidas", "cat-duvidas", "O que pergunta"),
    ("Desejos", "cat-desejos", "O que sonha"),
    ("Assuntos Relacionados", "cat-relacionados", "Porta de entrada"),
    ("Urgencias Quentes", "cat-quentes", "Alta intencao"),
    ("Urgencias Frias", "cat-frias", "Alto volume"),
    ("Urgencias Inusitadas", "cat-inusitadas", "Angulos inesperados"),
]


def render_urgencias(dados: dict) -> str:
    categorias: dict[str, list[str]] = dados.get("urgencias") or {}
    total = sum(len(v) for v in categorias.values())
    if total == 0:
        miolo = _placeholder("Aguardando Urgencias Ocultas do Bloco 5.")
    else:
        partes = []
        for idx, (nome, cat_cls, desc) in enumerate(_URGENCIAS_CATS):
            itens = categorias.get(nome) or categorias.get(nome.lower()) or []
            partes.append(
                _acc(cat_cls, nome, f"{desc} \u00b7 {len(itens)} itens", itens, open_=(idx == 0))
            )
        miolo = "".join(partes)
    return f"<!-- SECTION:urgencias -->\n{miolo}\n<!-- /SECTION:urgencias -->"


def render_identidade_produto(dados: dict) -> str:
    diferencial = dados.get("diferencial") or ""
    formato = dados.get("formato") or ""
    argumentos: list[str] = dados.get("argumentos_incontestaveis") or []
    objecoes: list[dict] = dados.get("objecoes") or []

    if not diferencial and not formato and not argumentos and not objecoes:
        miolo = _placeholder("Aguardando Identidade do Produto do Bloco 3.")
        return f"<!-- SECTION:identidade-produto -->\n{miolo}\n<!-- /SECTION:identidade-produto -->"

    grid_topo = (
        '<div class="grid grid-2" style="margin-bottom:var(--s-7)">'
        f'<div class="card"><span class="card-label">Diferencial principal</span>'
        f'<div class="card-headline" style="color:var(--neon)">{_escape(diferencial or "a definir")}</div></div>'
        f'<div class="card"><span class="card-label">Formato</span>'
        f'<div class="card-headline">{_escape(formato or "a definir")}</div></div>'
        "</div>"
    )

    args_html = ""
    if argumentos:
        lis = "".join(f"<li>{_md(a)}</li>" for a in argumentos)
        args_html = (
            '<div class="section-h">Argumentos incontestaveis</div>'
            f'<ul class="acc-list" style="padding-left:0;margin-bottom:var(--s-8)">{lis}</ul>'
        )

    objecoes_html = ""
    if objecoes:
        acc_items = []
        for idx, obj in enumerate(objecoes, start=1):
            corpo_args = ""
            for arg in obj.get("argumentos", []):
                paragrafos = "".join(
                    f'<p class="arg-body">{_escape(p)}</p>' for p in arg.get("paragrafos", []) if p
                )
                corpo_args += (
                    '<div class="arg">'
                    f'<div class="arg-type">{_escape(arg.get("titulo", ""))}</div>'
                    f"{paragrafos}"
                    "</div>"
                )
            acc_items.append(
                '<div class="objecao">'
                '<div class="objecao-head" onclick="toggleObjecao(this)">'
                f'<div><div class="objecao-n">Objecao {idx:02d}</div>'
                f'<div class="objecao-quote">{_escape(obj.get("texto", ""))}</div></div>'
                '<span style="color:var(--text-faint);font-size:11px">&#9662;</span>'
                "</div>"
                '<div class="objecao-body">'
                f"{corpo_args or '<p class=\"card-body\">Sem argumentos registrados.</p>'}"
                "</div>"
                "</div>"
            )
        objecoes_html = (
            '<div class="section-h">Objecoes e como quebrar</div>'
            + "".join(acc_items)
        )

    miolo = grid_topo + args_html + objecoes_html
    return f"<!-- SECTION:identidade-produto -->\n{miolo}\n<!-- /SECTION:identidade-produto -->"


def render_identidade_consumidor(dados: dict) -> str:
    para_quem = dados.get("para_quem_e") or ""
    perfil: dict = dados.get("perfil_demo") or {}
    comportamento: dict = dados.get("comportamento") or {}
    paliativos: list[str] = dados.get("paliativos") or []
    baldes: list[dict] = dados.get("baldes") or []

    if not para_quem and not perfil and not comportamento and not baldes:
        miolo = _placeholder("Aguardando Identidade do Consumidor.")
        return f"<!-- SECTION:identidade-consumidor -->\n{miolo}\n<!-- /SECTION:identidade-consumidor -->"

    blocos: list[str] = []

    if para_quem:
        blocos.append(
            f'<div class="quadro-card" style="margin-bottom:var(--s-8)">'
            f'<div class="big-quote" style="font-size:22px">{_escape(para_quem)}</div>'
            "</div>"
        )

    if perfil or comportamento:
        def _dt(pares: dict) -> str:
            if not pares:
                return '<p class="card-body">Sem dados.</p>'
            return (
                '<dl class="dt-list">'
                + "".join(
                    f"<dt>{_escape(k)}</dt><dd>{_escape(v)}</dd>"
                    for k, v in pares.items() if v
                )
                + "</dl>"
            )

        blocos.append(
            '<div class="grid grid-2" style="margin-bottom:var(--s-7)">'
            f'<div class="card"><span class="card-label">Perfil demografico</span>{_dt(perfil)}</div>'
            f'<div class="card"><span class="card-label">Comportamento e canais</span>{_dt(comportamento)}</div>'
            "</div>"
        )

    if paliativos:
        lis = "".join(f"<li>{_md(p)}</li>" for p in paliativos)
        blocos.append(
            '<div class="section-h">Paliativos (concorrentes do mercado)</div>'
            f'<ul class="acc-list" style="margin-bottom:var(--s-8)">{lis}</ul>'
        )

    if baldes:
        accs = "".join(
            _acc("", balde.get("nome", "Perfil"), "5 afirmacoes", balde.get("itens", []))
            for balde in baldes
        )
        blocos.append(
            '<div class="section-h">Baldes de para quem e</div>'
            + accs
        )

    miolo = "".join(blocos)
    return f"<!-- SECTION:identidade-consumidor -->\n{miolo}\n<!-- /SECTION:identidade-consumidor -->"


def render_identidade_comunicador(dados: dict) -> str:
    nome = dados.get("nome") or ""
    especialidade = dados.get("especialidade") or ""
    valores: list[str] = dados.get("valores") or []
    mantras: list[str] = dados.get("mantras") or []
    formatos: list[str] = dados.get("formatos") or []
    visual: list[str] = dados.get("elementos_visuais") or []
    tom = dados.get("tom_de_voz") or ""
    posicionamento = dados.get("posicionamento") or ""
    conectam: list[str] = dados.get("palavras_conectam") or []
    afastam: list[str] = dados.get("palavras_afastam") or []

    if not nome and not valores and not tom and not posicionamento:
        miolo = _placeholder("Aguardando Identidade do Comunicador do Bloco 3B.")
        return f"<!-- SECTION:identidade-comunicador -->\n{miolo}\n<!-- /SECTION:identidade-comunicador -->"

    grid_topo = (
        '<div class="grid grid-3" style="margin-bottom:var(--s-7)">'
        f'<div class="card"><span class="card-label">Comunicador</span>'
        f'<div class="card-headline">{_escape(nome or "(sem nome)")}</div>'
        f'<p class="card-body" style="margin-top:var(--s-2)">{_escape(especialidade)}</p></div>'
        f'<div class="card"><span class="card-label">Valores</span>'
        f'<div style="margin-top:var(--s-3)">{_pills(valores, "neon")}</div></div>'
        f'<div class="card"><span class="card-label">Mantras e jargoes</span>'
        + ("".join(
            f'<div style="margin-top:var(--s-2);font-size:13px;color:var(--text-mid);font-style:italic">{_escape(m)}</div>'
            for m in mantras
        ) if mantras else '<p class="card-body">Nenhum ainda.</p>')
        + "</div></div>"
    )

    grid2 = (
        '<div class="grid grid-2" style="margin-bottom:var(--s-5)">'
        f'<div class="card"><span class="card-label">Formatos que combinam</span>'
        f'<div style="margin-top:var(--s-3)">{_pills(formatos)}</div></div>'
        f'<div class="card"><span class="card-label">Estilo visual recomendado</span>'
        f'<div style="margin-top:var(--s-3)">{_pills(visual)}</div></div>'
        "</div>"
    )

    tom_pos = (
        '<div class="grid grid-2" style="margin-bottom:var(--s-5)">'
        f'<div class="card"><span class="card-label">Tom de voz</span>'
        f'<p class="card-body" style="margin-top:var(--s-2)">{_escape(tom) or "&mdash;"}</p></div>'
        f'<div class="card"><span class="card-label">Posicionamento</span>'
        f'<p class="card-body" style="margin-top:var(--s-2)">{_escape(posicionamento) or "&mdash;"}</p></div>'
        "</div>"
    )

    palavras = (
        '<div class="grid grid-2">'
        f'<div class="card"><span class="card-label">Palavras que conectam</span>'
        f'<div style="margin-top:var(--s-3)">{_pills(conectam, "neon")}</div></div>'
        f'<div class="card"><span class="card-label">Palavras que afastam</span>'
        f'<div style="margin-top:var(--s-3)">{_pills(afastam, "rust")}</div></div>'
        "</div>"
    )

    miolo = grid_topo + grid2 + tom_pos + palavras
    return f"<!-- SECTION:identidade-comunicador -->\n{miolo}\n<!-- /SECTION:identidade-comunicador -->"


def render_pesquisa(dados: dict) -> str:
    if not dados or not any(dados.values()):
        miolo = _placeholder("Aguardando pesquisa de mercado.")
        return f"<!-- SECTION:pesquisa -->\n{miolo}\n<!-- /SECTION:pesquisa -->"

    kpis: list[dict] = dados.get("kpis") or []
    oportunidades: list[str] = dados.get("oportunidades") or []
    cuidados: list[str] = dados.get("cuidados") or []
    reclamacoes: list[str] = dados.get("reclamacoes") or []
    concorrentes: list[dict] = dados.get("concorrentes") or []
    fontes: list[str] = dados.get("fontes") or []

    if not kpis:
        kpis = [
            {"label": "Tamanho do mercado", "valor": dados.get("tamanho_mercado") or "a mapear", "foot": ""},
            {"label": "Crescimento anual", "valor": dados.get("crescimento") or "a mapear", "foot": ""},
            {"label": "Concorrentes mapeados", "valor": str(len(concorrentes)) if concorrentes else "0", "foot": "identificados"},
            {"label": "Ticket medio do nicho", "valor": dados.get("ticket_medio") or "a mapear", "foot": ""},
        ]

    kpis_html = "".join(
        f'<div class="kpi">'
        f'<div class="kpi-label">{_escape(k["label"])}</div>'
        f'<div class="kpi-num">{_escape(k["valor"])}</div>'
        f'<div class="kpi-foot">{_escape(k.get("foot", "") or k.get("sub", ""))}</div>'
        "</div>"
        for k in kpis
    )

    opo_html = ""
    if oportunidades:
        lis = "".join(f"<li>{_md(o)}</li>" for o in oportunidades)
        opo_html = (
            '<div class="section-h">Oportunidades identificadas</div>'
            f'<ul class="acc-list" style="margin-bottom:var(--s-8)">{lis}</ul>'
        )

    cuid_rec = ""
    if cuidados or reclamacoes:
        def _col(titulo, items):
            lis = "".join(f"<li>{_md(i)}</li>" for i in items)
            return (
                f'<div class="card"><span class="card-label">{_escape(titulo)}</span>'
                f'<ul class="acc-list" style="margin-top:var(--s-3)">{lis}</ul></div>'
            ) if items else ""
        cuid_rec = (
            '<div class="grid grid-2" style="margin-bottom:var(--s-7)">'
            + _col("Cuidados e riscos", cuidados)
            + _col("Padroes de reclamacao", reclamacoes)
            + "</div>"
        )

    conc_html = ""
    if concorrentes:
        linhas = []
        for c in concorrentes:
            nome_c = _escape(c.get("nome", ""))
            inicial = (c.get("nome") or "?")[0].upper()
            links_html = ""
            url = (c.get("pagina") or "").strip()
            insta = (c.get("instagram") or "").strip()
            if url and not _is_busca(url):
                links_html += f'<a href="{_escape(url)}" target="_blank" rel="noopener">Pagina &#8599;</a> '
            if insta and not _is_busca(insta):
                links_html += f'<a href="{_escape(insta)}" target="_blank" rel="noopener">Instagram &#8599;</a>'
            preco_c = _escape(c.get("preco", "") or "")
            promessa_c = _escape(c.get("promessa", "") or "")
            linhas.append(
                '<div class="comp-row">'
                f'<div class="comp-avatar">{inicial}</div>'
                "<div style='flex:1;min-width:0'>"
                f'<div class="comp-name">{nome_c}</div>'
                f'<div class="comp-links">{links_html or "&mdash;"}</div>'
                f'<div style="font-size:12px;color:var(--text-mid);margin-top:4px">{promessa_c}</div>'
                "</div>"
                f'<div class="comp-price">{preco_c or "&mdash;"}</div>'
                "</div>"
            )
        conc_html = (
            '<div class="section-h">Analise de concorrentes</div>'
            + "".join(linhas)
            + '<div style="margin-bottom:var(--s-8)"></div>'
        )

    fontes_html = ""
    if fontes:
        lis = "".join(f"<li>{_md(f)}</li>" for f in fontes)
        fontes_html = (
            '<div class="section-h">Fontes consultadas</div>'
            f'<ul class="acc-list">{lis}</ul>'
        )

    # publico-alvo real
    pa_html = ""
    pa = dados.get("publico_alvo") or {}
    if pa:
        def _pa_col(titulo: str, items: list) -> str:
            if not items:
                return ""
            lis = "".join(f"<li>{_md(i)}</li>" for i in items)
            return (
                f'<div><span class="card-label">{_escape(titulo)}</span>'
                f'<ul class="acc-list" style="margin-top:var(--s-3);grid-template-columns:1fr">{lis}</ul></div>'
            )
        raw = pa.get("raw") or []
        demo = pa.get("demo") or []
        comport = pa.get("comportamento") or []
        consci = pa.get("consciencia") or []
        if raw:
            lis = "".join(f"<li>{_md(i)}</li>" for i in raw)
            pa_html = (
                '<div class="section-h">Publico-alvo real</div>'
                f'<ul class="acc-list" style="margin-bottom:var(--s-8)">{lis}</ul>'
            )
        elif any([demo, comport, consci]):
            cols = _pa_col("Perfil demografico", demo) + _pa_col("Comportamento", comport) + _pa_col("Nivel de consciencia (Schwartz)", consci)
            pa_html = (
                '<div class="section-h">Publico-alvo real</div>'
                f'<div class="grid grid-2" style="margin-bottom:var(--s-8)">{cols}</div>'
            )

    # youtube top 10
    yt_html = ""
    yt_videos = dados.get("youtube") or []
    if yt_videos:
        cards = ""
        for i, v in enumerate(yt_videos[:10]):
            link = (v.get("link") or "").strip()
            link_html = (
                f'<a href="{_escape(link)}" target="_blank" rel="noopener" '
                f'style="font-family:var(--font-mono);font-size:9px;color:var(--neon);letter-spacing:.1em" '
                f'onclick="event.stopPropagation()">&#8599;</a>'
            ) if link else ""
            views = _escape(v.get("views") or "")
            meta_parts = []
            if views:
                meta_parts.append(
                    f'<span style="font-family:var(--font-mono);font-size:10px;color:var(--neon)">{views}</span>'
                )
            if link_html:
                meta_parts.append(link_html)
            meta_html = " ".join(meta_parts)
            header = (
                f'<div class="yt-video-header" onclick="this.closest(\'.yt-video-card\').classList.toggle(\'yt-open\')">'
                f'<div class="yt-rank">{i + 1}</div>'
                f'<div class="yt-thumb">&#9654;</div>'
                f'<div class="yt-info">'
                f'<div class="yt-title">{_escape(v.get("titulo") or "")}</div>'
                f'<div class="yt-canal">{_escape(v.get("canal") or "")}</div>'
                f'<div class="yt-meta">{meta_html}</div>'
                f'</div><span class="yt-toggle">&#9662;</span></div>'
            )
            detail_parts = []
            for c in (v.get("comentarios") or [])[:3]:
                detail_parts.append(f'<div class="yt-comment">&ldquo;{_escape(c)}&rdquo;</div>')
            if detail_parts:
                detail_parts.insert(0, '<div class="yt-section-title">Comentarios</div>')
            if v.get("angulo"):
                detail_parts.append(
                    f'<div class="yt-section-title">Angulo do titulo</div>'
                    f'<div class="yt-insight">{_escape(v["angulo"])}</div>'
                )
            if v.get("lacuna"):
                detail_parts.append(
                    f'<div class="yt-section-title">Lacuna para o produto</div>'
                    f'<div class="yt-insight">{_escape(v["lacuna"])}</div>'
                )
            thumb = v.get("thumbnail") or {}
            if thumb:
                td = []
                for k, lbl in [("cores", "Cores"), ("expressao", "Expressao"), ("texto", "Texto"), ("elementos", "Elementos"), ("composicao", "Composicao")]:
                    if thumb.get(k):
                        td.append(
                            f'<div class="yt-thumb-detail">'
                            f'<span style="color:var(--text-faint)">{lbl}:</span> {_escape(thumb[k])}</div>'
                        )
                if td:
                    detail_parts.append(f'<div class="yt-section-title">Thumbnail</div>{"".join(td)}')
            cards += (
                f'<div class="yt-video-card">{header}'
                f'<div class="yt-detail">{"".join(detail_parts)}</div></div>'
            )
        yt_html = (
            '<div class="section-h">Top 10 videos do YouTube</div>'
            f'<div style="margin-bottom:var(--s-8)">{cards}</div>'
        )

    # Assuntos Quentes e Ângulos Virais
    assuntos_html = ""
    assuntos = dados.get("assuntos_quentes") or {}
    if assuntos and any(assuntos.values()):
        termos_aq = assuntos.get("termos") or []
        virais_aq = assuntos.get("virais") or []
        ganchos_aq = assuntos.get("ganchos") or []
        partes_aq = []
        if termos_aq:
            lis = "".join(f"<li>{_md(t)}</li>" for t in termos_aq)
            partes_aq.append(
                '<span class="card-label">Termos em alta</span>'
                f'<ul class="acc-list" style="margin-bottom:var(--s-7)">{lis}</ul>'
            )
        if ganchos_aq:
            lis = "".join(f"<li>{_md(g)}</li>" for g in ganchos_aq)
            partes_aq.append(
                '<span class="card-label">Ganchos que performam</span>'
                f'<ul class="acc-list" style="margin-bottom:var(--s-7)">{lis}</ul>'
            )
        if virais_aq:
            lis = "".join(f"<li>{_md(v)}</li>" for v in virais_aq)
            partes_aq.append(
                '<span class="card-label">Conteúdos virais recentes</span>'
                f'<ul class="acc-list">{lis}</ul>'
            )
        if partes_aq:
            assuntos_html = (
                '<div class="section-h">Assuntos quentes e ângulos virais</div>'
                + "".join(partes_aq)
                + '<div style="margin-bottom:var(--s-8)"></div>'
            )

    # Biblioteca de Anúncios
    bibl_html = ""
    bibl = dados.get("biblioteca_anuncios") or {}
    if bibl and any(bibl.values()):
        headlines_bl = bibl.get("headlines") or []
        padroes_of = bibl.get("padroes_oferta") or []
        criativos_bl = bibl.get("criativos") or []
        obs_bl = bibl.get("observacoes") or []
        col_esq = ""
        col_dir = ""
        if headlines_bl:
            lis = "".join(f"<li>{_md(h)}</li>" for h in headlines_bl)
            col_esq += (
                '<span class="card-label">Padrões de headline</span>'
                f'<ul class="acc-list" style="grid-template-columns:1fr;margin-bottom:var(--s-5)">{lis}</ul>'
            )
        if padroes_of:
            lis = "".join(f"<li>{_md(p)}</li>" for p in padroes_of)
            col_esq += (
                '<span class="card-label">Padrões de oferta</span>'
                f'<ul class="acc-list" style="grid-template-columns:1fr">{lis}</ul>'
            )
        if criativos_bl:
            lis = "".join(f"<li>{_md(c)}</li>" for c in criativos_bl)
            col_dir += (
                '<span class="card-label">Criativos ativos no nicho</span>'
                f'<ul class="acc-list" style="grid-template-columns:1fr;margin-bottom:var(--s-5)">{lis}</ul>'
            )
        if obs_bl:
            lis = "".join(f"<li>{_md(o)}</li>" for o in obs_bl)
            col_dir += (
                '<span class="card-label">Observações</span>'
                f'<ul class="acc-list" style="grid-template-columns:1fr">{lis}</ul>'
            )
        if col_esq or col_dir:
            if col_esq and col_dir:
                content_bl = f'<div class="grid grid-2"><div>{col_esq}</div><div>{col_dir}</div></div>'
            else:
                content_bl = f'<div>{col_esq}{col_dir}</div>'
            bibl_html = (
                '<div class="section-h">Biblioteca de anúncios</div>'
                + content_bl
                + '<div style="margin-bottom:var(--s-8)"></div>'
            )

    miolo = (
        f'<div class="kpi-grid">{kpis_html}</div>'
        + opo_html
        + cuid_rec
        + conc_html
        + pa_html
        + yt_html
        + assuntos_html
        + bibl_html
        + fontes_html
    )
    return f"<!-- SECTION:pesquisa -->\n{miolo}\n<!-- /SECTION:pesquisa -->"


def render_comercial_playbook(dados: dict) -> str:
    caminho = dados.get("caminho") or ""
    existe = bool(dados.get("existe"))
    gerado_em = dados.get("gerado_em") or ""
    nome_arquivo = dados.get("nome_arquivo") or ""

    if not existe:
        miolo = _placeholder(
            "Rode /comercial-playbook para gerar o script de venda 1:1 por WhatsApp."
        )
        return f"<!-- SECTION:comercial-playbook -->\n{miolo}\n<!-- /SECTION:comercial-playbook -->"

    topo = (
        f'<div class="quadro-card" style="margin-bottom:var(--s-7)">'
        f'<div class="big-quote" style="font-size:18px">{_escape(nome_arquivo)}</div>'
        f'<div class="card-body" style="margin-top:var(--s-2)">Ultima geracao: {_escape(gerado_em)}</div>'
        "</div>"
    )

    link_card = (
        '<div class="card" style="margin-bottom:var(--s-5)">'
        '<span class="card-label">Abrir arquivo</span>'
        f'<a href="{_escape(caminho)}" target="_blank" rel="noopener" '
        'style="display:inline-flex;align-items:center;gap:8px;font-family:var(--font-mono);'
        'font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--neon);'
        'margin-top:var(--s-4);border-bottom:1px solid var(--neon-deep);padding-bottom:2px;">'
        'Abrir Playbook &#8594;</a>'
        '<p class="card-body" style="margin-top:var(--s-4)">Para exportar PDF: Imprimir &rsaquo; Salvar como PDF.</p>'
        "</div>"
    )

    blocos = [
        "1. Capa interna",
        "2. Identidade do Produto",
        "3. Identidade do Consumidor",
        "4. Identidade do Comunicador",
        "5. Principios de venda por WhatsApp",
        "6. Metodologia DEF",
        "7. Abordagem Ativa (Outbound)",
        "8. Abordagem Receptiva (Inbound)",
        "9. SPIN adaptado ao WhatsApp",
        "10. Apresentacao e ancoragem de preco",
        "11. Fechamento em 4 passos",
        "12. Quebra de objecoes (7 Argumentos)",
        "13. Recuperacao de carrinho",
        "14. Follow-up, Upsell, Downsell, Order bump",
        "15. Checklist de atendimento",
        "16. Dicionario do Comercial",
    ]
    lis = "".join(f"<li>{_md(b)}</li>" for b in blocos)
    blocos_card = (
        '<div class="section-h">Blocos cobertos</div>'
        f'<ul class="acc-list">{lis}</ul>'
    )

    miolo = topo + link_card + blocos_card
    return f"<!-- SECTION:comercial-playbook -->\n{miolo}\n<!-- /SECTION:comercial-playbook -->"


# ----- utilidades -----

_BUSCA_PATTERNS = re.compile(
    r"(google\.com/search|youtube\.com/results|bing\.com/search|search\?q=)",
    re.IGNORECASE,
)


def _is_busca(url: str) -> bool:
    return bool(_BUSCA_PATTERNS.search(url or ""))


def _preco_badge(preco: str) -> str:
    if not preco:
        return ""
    nums = re.findall(r"(\d+[\.\,]?\d*)", preco)
    if not nums:
        return ""
    try:
        valor = float(nums[0].replace(",", "."))
    except ValueError:
        return ""
    if valor <= 97:
        return "neon"
    if valor <= 497:
        return ""
    return ""


def _md_bloco_para_html(md: str) -> str:
    """Conversao simples de markdown para HTML no contexto do painel de copy.
    Trata listas (- / *), negrito (**), italico (*), cabecalhos ### e paragrafos.
    Nao pretende ser completa, so exibir os blocos de copy de forma legivel."""
    if not md:
        return '<p class="card-sub">Sem conteudo.</p>'

    md = md.strip()
    # separa em sub-secoes por cabecalho ### (vira titulo + paragrafo)
    partes: list[str] = []
    blocos = re.split(r"\n\s*\n", md)
    for bloco in blocos:
        bloco = bloco.strip()
        if not bloco:
            continue
        # Cabecalhos isolados
        m_h = re.match(r"^#{2,6}\s+(.+?)\s*$", bloco)
        if m_h and "\n" not in bloco:
            partes.append(
                '<div style="font-size:13px;font-weight:700;color:var(--text-1);margin-top:10px;margin-bottom:4px">'
                f"{_md_inline(m_h.group(1))}</div>"
            )
            continue
        # Listas puras (todo o bloco eh bullet)
        linhas = [ln for ln in bloco.splitlines() if ln.strip()]
        bullets = [re.match(r"^\s*[-*]\s+(.+?)\s*$", ln) for ln in linhas]
        if bullets and all(bullets):
            lis = "".join(f"<li>{_md_inline(b.group(1))}</li>" for b in bullets)
            partes.append(f'<ul class="bullet-list">{lis}</ul>')
            continue
        # Blocos mistos. processa linha a linha, agrupando bullets consecutivos
        partes.extend(_md_bloco_misto(linhas))
    return "".join(partes)


def _md_bloco_misto(linhas: list[str]) -> list[str]:
    """Processa um bloco com possivel mistura de titulo, bullets e paragrafo."""
    saida: list[str] = []
    buffer_para: list[str] = []
    buffer_lis: list[str] = []

    def flush_para():
        if buffer_para:
            texto = "<br>".join(_md_inline(ln) for ln in buffer_para)
            saida.append(f'<p class="para">{texto}</p>')
            buffer_para.clear()

    def flush_lista():
        if buffer_lis:
            saida.append(
                '<ul class="bullet-list">'
                + "".join(f"<li>{li}</li>" for li in buffer_lis)
                + "</ul>"
            )
            buffer_lis.clear()

    for ln in linhas:
        m_h = re.match(r"^#{2,6}\s+(.+?)\s*$", ln.strip())
        m_li = re.match(r"^\s*[-*]\s+(.+?)\s*$", ln)
        if m_h:
            flush_para()
            flush_lista()
            saida.append(
                '<div style="font-size:13px;font-weight:700;color:var(--text-1);margin-top:10px;margin-bottom:4px">'
                f"{_md_inline(m_h.group(1))}</div>"
            )
        elif m_li:
            flush_para()
            buffer_lis.append(_md_inline(m_li.group(1)))
        else:
            flush_lista()
            buffer_para.append(ln)
    flush_para()
    flush_lista()
    return saida


def _md_inline(texto: str) -> str:
    """Escapa HTML e aplica negrito e italico inline."""
    escapado = html.escape(texto, quote=False)
    escapado = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escapado)
    escapado = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", escapado)
    return escapado


_NOMES_BLOCOS_COPY = {
    1: "Hero", 2: "Dor", 3: "Paliativo", 4: "Prova social (primeiro bloco)",
    5: "CTA intermediário", 6: "Método (Furadeira)", 7: "Para quem é / não é",
    8: "Entregáveis", 9: "Bônus", 10: "Stack de valor",
    11: "Prova social (segundo bloco) ou Depoimentos", 12: "Suporte",
    13: "Garantia", 14: "Autoridade do criador", 15: "FAQ", 16: "Oferta final",
}


def parse_copy_pagina(produto_dir, slug, repo_root=None):
    """Le meus-produtos/{slug}/entregas/copy-pagina/copy-{slug}.md e extrai
    os blocos `## Bloco NN - Nome` em uma lista {numero, titulo, conteudo}.

    produto_dir: Path para meus-produtos/{slug}
    slug: slug do produto
    repo_root: Path da raiz do repo. Se omitido, assume produto_dir.parent.parent.

    Retorna dict com 'blocos' (lista ordenada pela ordem do arquivo)
    e 'arquivo_relativo' (string do caminho relativo ao repo_root)."""
    from pathlib import Path

    produto_dir = Path(produto_dir)
    if repo_root is None:
        repo_root = produto_dir.parent.parent
    else:
        repo_root = Path(repo_root)

    pasta = produto_dir / "entregas" / "copy-pagina"
    candidatos = [pasta / f"copy-{slug}.md"]
    if pasta.is_dir():
        for md in sorted(pasta.glob("copy-*.md")):
            if md not in candidatos:
                candidatos.append(md)

    arquivo = next((p for p in candidatos if p.exists()), None)
    if not arquivo:
        return {"blocos": [], "arquivo_relativo": "", "arquivo_existe": False}

    texto = arquivo.read_text(encoding="utf-8")
    pat = re.compile(
        r"^##\s+Bloco\s+(\d{1,2})\s*[\-–—\.:]?\s*(.*?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    matches = list(pat.finditer(texto))
    blocos = []
    for i, m in enumerate(matches):
        numero = int(m.group(1))
        titulo = m.group(2).strip()
        inicio = m.end()
        fim = matches[i + 1].start() if i + 1 < len(matches) else len(texto)
        conteudo = texto[inicio:fim].strip()
        if 1 <= numero <= 16:
            blocos.append({
                "numero": numero,
                "titulo": titulo,
                "conteudo": conteudo,
            })

    try:
        rel = arquivo.relative_to(repo_root)
    except ValueError:
        rel = arquivo
    return {
        "blocos": blocos,
        "arquivo_relativo": str(rel).replace("\\", "/"),
        "arquivo_existe": True,
    }


def render_copy_pagina_miolo(dados: dict) -> str:
    """Retorna o HTML interno (sem os marcadores SECTION) da secao copy-pagina.
    Util para templates que injetam via placeholder, sem precisar dos comentarios."""
    html_completo = render_copy_pagina(dados)
    # remove os marcadores SECTION:copy-pagina que sao so do fluxo incremental
    inicio = html_completo.find("-->") + 3
    fim = html_completo.rfind("<!--")
    return html_completo[inicio:fim].strip()


_DOC_CSS = """
<style>
#panel-copy-pagina { background: #eceff3; padding: 24px 0 48px; margin: -32px -40px -32px; }
#panel-copy-pagina > .breadcrumb,
#panel-copy-pagina > .section-title,
#panel-copy-pagina > .section-sub { padding-left: 40px; padding-right: 40px; }
.doc-page { max-width: 820px; margin: 24px auto 0; background: #ffffff;
  box-shadow: 0 1px 3px rgba(0,0,0,.08), 0 8px 32px rgba(0,0,0,.06);
  border-radius: 4px; padding: 72px 88px; color: #1f2937;
  font-family: 'Georgia', 'Times New Roman', 'Inter', serif; line-height: 1.75; }
.doc-head { border-bottom: 1px solid #e5e7eb; padding-bottom: 28px; margin-bottom: 44px; }
.doc-kicker { font-family: 'Inter', sans-serif; font-size: 11px; letter-spacing: 2.4px;
  color: #6b7280; text-transform: uppercase; margin-bottom: 10px; font-weight: 600; }
.doc-title { font-size: 34px; font-weight: 700; color: #111827; margin: 0 0 12px; line-height: 1.25; letter-spacing: -.3px; }
.doc-subtitle { font-size: 17px; color: #4b5563; font-style: italic; margin: 0 0 18px; line-height: 1.5; }
.doc-meta { display: flex; gap: 20px; flex-wrap: wrap; font-family: 'Inter', sans-serif;
  font-size: 12px; color: #6b7280; }
.doc-meta .approved-count { color: #16a34a; font-weight: 700; }
.doc-meta .file { font-family: 'Menlo','Consolas',monospace; color: #4b5563; word-break: break-all; }
.doc-block { margin: 0 0 48px; padding-bottom: 36px; border-bottom: 1px solid #f1f3f6; }
.doc-block:last-child { border-bottom: none; padding-bottom: 8px; }
.doc-block-head { display: flex; align-items: baseline; gap: 14px; margin-bottom: 6px; }
.doc-block-number { font-family: 'Inter', sans-serif; font-size: 11px; letter-spacing: 2px;
  text-transform: uppercase; color: #9ca3af; font-weight: 700; }
.doc-block-status { font-family: 'Inter', sans-serif; font-size: 10px; letter-spacing: 1.4px;
  text-transform: uppercase; font-weight: 700; padding: 2px 8px; border-radius: 3px; }
.doc-block-status.approved { color: #16a34a; background: #dcfce7; }
.doc-block-status.pending { color: #9ca3af; background: #f3f4f6; }
.doc-block h2 { font-size: 26px; font-weight: 700; color: #111827; margin: 4px 0 22px;
  line-height: 1.3; letter-spacing: -.2px; }
.doc-block h3 { font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 700;
  color: #1f2937; margin: 28px 0 10px; text-transform: none; letter-spacing: 0; }
.doc-block p { font-size: 16px; line-height: 1.8; color: #1f2937; margin: 0 0 18px;
  text-align: justify; hyphens: auto; }
.doc-block p em { color: #4b5563; font-size: 15px; }
.doc-block p strong { color: #111827; font-weight: 700; }
.doc-block ul { margin: 0 0 22px; padding-left: 26px; list-style: disc; }
.doc-block li { font-size: 16px; line-height: 1.8; color: #1f2937; margin-bottom: 8px; padding-left: 4px; }
.doc-block .pending-note { color: #9ca3af; font-style: italic; font-size: 14px; margin-top: 8px; }
.doc-block blockquote { border-left: 3px solid #e5e7eb; padding: 4px 0 4px 20px; margin: 0 0 22px;
  color: #4b5563; font-style: italic; }
@media (max-width: 900px) {
  #panel-copy-pagina { margin: -20px -20px -20px; padding: 16px 0 32px; }
  #panel-copy-pagina > .breadcrumb,
  #panel-copy-pagina > .section-title,
  #panel-copy-pagina > .section-sub { padding-left: 20px; padding-right: 20px; }
  .doc-page { padding: 36px 28px; margin: 16px 16px 0; max-width: none; border-radius: 2px; }
  .doc-title { font-size: 26px; }
  .doc-block h2 { font-size: 21px; }
  .doc-block p, .doc-block li { font-size: 15px; text-align: left; hyphens: none; }
}
@media print {
  #panel-copy-pagina { background: #fff; padding: 0; margin: 0; }
  .doc-page { box-shadow: none; border-radius: 0; padding: 0; max-width: none; margin: 0; }
  .doc-block { page-break-inside: avoid; }
}
</style>
"""


def _md_bloco_para_documento(md: str) -> str:
    """Conversao markdown -> HTML sem classes (para o layout tipo documento).
    O CSS dentro de .doc-block controla a tipografia."""
    if not md:
        return ""
    md = md.strip()
    partes: list[str] = []
    for bloco in re.split(r"\n\s*\n", md):
        bloco = bloco.strip()
        if not bloco or bloco == "---":
            continue
        m_h = re.match(r"^#{2,6}\s+(.+?)\s*$", bloco)
        if m_h and "\n" not in bloco:
            partes.append(f"<h3>{_md_inline(m_h.group(1))}</h3>")
            continue
        linhas = [ln for ln in bloco.splitlines() if ln.strip()]
        bullets = [re.match(r"^\s*[-*]\s+(.+?)\s*$", ln) for ln in linhas]
        if bullets and all(bullets):
            lis = "".join(f"<li>{_md_inline(b.group(1))}</li>" for b in bullets)
            partes.append(f"<ul>{lis}</ul>")
            continue
        if all(ln.lstrip().startswith(">") for ln in linhas):
            texto = "<br>".join(
                _md_inline(re.sub(r"^\s*>\s?", "", ln)) for ln in linhas
            )
            partes.append(f"<blockquote>{texto}</blockquote>")
            continue
        partes.extend(_md_doc_misto(linhas))
    return "".join(partes)


def _md_doc_misto(linhas: list[str]) -> list[str]:
    saida: list[str] = []
    buf_p: list[str] = []
    buf_li: list[str] = []

    def flush_p():
        if buf_p:
            saida.append(
                "<p>" + "<br>".join(_md_inline(ln) for ln in buf_p) + "</p>"
            )
            buf_p.clear()

    def flush_l():
        if buf_li:
            saida.append(
                "<ul>" + "".join(f"<li>{li}</li>" for li in buf_li) + "</ul>"
            )
            buf_li.clear()

    for ln in linhas:
        m_h = re.match(r"^#{2,6}\s+(.+?)\s*$", ln.strip())
        m_li = re.match(r"^\s*[-*]\s+(.+?)\s*$", ln)
        if m_h:
            flush_p()
            flush_l()
            saida.append(f"<h3>{_md_inline(m_h.group(1))}</h3>")
        elif m_li:
            flush_p()
            buf_li.append(_md_inline(m_li.group(1)))
        else:
            flush_l()
            buf_p.append(ln)
    flush_p()
    flush_l()
    return saida


def render_copy_pagina(dados: dict) -> str:
    blocos: list[dict] = dados.get("blocos") or []
    if not blocos:
        miolo = _placeholder(
            "Aguardando copy da página. Rode /copy-pagina e aprove os blocos."
        )
        return f"<!-- SECTION:copy-pagina -->\n{miolo}\n<!-- /SECTION:copy-pagina -->"

    por_numero = {b["numero"]: b for b in blocos if b.get("numero")}
    total_aprovados = len(por_numero)
    arquivo = dados.get("arquivo_relativo", "")

    cabecalho = (
        '<div class="doc-head">'
        '<div class="doc-kicker">Copy da Página de Vendas</div>'
        '<h1 class="doc-title">Copy completa em 16 blocos</h1>'
        '<div class="doc-subtitle">Documento de trabalho. Fonte única para montar a página HTML.</div>'
        '<div class="doc-meta">'
        f'<span>Progresso: <span class="approved-count">{total_aprovados}/16 blocos aprovados</span></span>'
        f'<span class="file">{_escape(arquivo)}</span>'
        "</div>"
        "</div>"
    )

    secoes: list[str] = []
    for numero in range(1, 17):
        nome = _NOMES_BLOCOS_COPY[numero]
        bd = por_numero.get(numero)
        if bd:
            status_html = '<span class="doc-block-status approved">Aprovado</span>'
            corpo = _md_bloco_para_documento(bd.get("conteudo", ""))
        else:
            status_html = '<span class="doc-block-status pending">Em breve</span>'
            corpo = (
                '<p class="pending-note">Bloco ainda não aprovado. '
                "Rode /copy-pagina e valide este bloco para ele aparecer aqui.</p>"
            )
        secoes.append(
            '<section class="doc-block">'
            '<div class="doc-block-head">'
            f'<span class="doc-block-number">Bloco {numero:02d}</span>'
            f"{status_html}"
            "</div>"
            f"<h2>{_escape(nome)}</h2>"
            f"{corpo}"
            "</section>"
        )

    miolo = _DOC_CSS + '<article class="doc-page">' + cabecalho + "".join(secoes) + "</article>"
    return f"<!-- SECTION:copy-pagina -->\n{miolo}\n<!-- /SECTION:copy-pagina -->"


def _proximo_bloco(por_numero: dict[int, dict]) -> str:
    for n in range(1, 17):
        if n not in por_numero:
            return f"{n:02d}"
    return "16"


RENDERS = {
    "quadro": render_quadro,
    "furadeira": render_furadeira,
    "decorados": render_decorados,
    "urgencias": render_urgencias,
    "identidade-produto": render_identidade_produto,
    "identidade-consumidor": render_identidade_consumidor,
    "identidade-comunicador": render_identidade_comunicador,
    "pesquisa": render_pesquisa,
    "copy-pagina": render_copy_pagina,
    "comercial-playbook": render_comercial_playbook,
}
