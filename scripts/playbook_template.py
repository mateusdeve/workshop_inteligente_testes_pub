"""
playbook_template.py

Shell HTML, CSS (Adobe Spectrum 2 em CSS puro), JS e renderers das secoes
estaticas do playbook comercial de WhatsApp 1:1.

Secoes renderizadas por este template (extraidas dos arquivos do produto):
    1  Capa interna
    2  Identidade do Produto
    3  Metodologia DEF (fixo)
    8  Fechamento em 4 passos (template com variaveis do produto)
    9  Quebra de objecoes (via playbook-extrair-objecoes.py)
   12  Dicionario do Comercial (fixo)

As demais secoes (4, 5, 6, 7, 10, 11) ficam como placeholders marcados
com <!-- CREATIVE_N --> e sao preenchidas pelos agentes via JSON com
marcadores {{N.chave}}, usando a voz do comunicador e os dados do produto.

O script playbook-montar.py le perfil.md + idconsumidor.md, chama os
renderers aqui e escreve o HTML final.
"""

from __future__ import annotations

import html
import json
from typing import Any


def e(valor: Any) -> str:
    """Escape HTML seguro, aceita None."""
    if valor is None:
        return ""
    return html.escape(str(valor))


# ============================================================================
# CSS
# ============================================================================

_CSS_TOKENS = """\
:root {
  --color-base: #ffffff;
  --color-layer-1: #f8f9fb;
  --color-layer-2: #f3f4f6;
  --color-elevated: #ffffff;
  --color-pasteboard: #e5e7eb;

  --color-accent: #16a34a;
  --color-accent-strong: #15803d;
  --color-accent-subtle: #f0fdf4;
  --color-accent-border: #bbf7d0;
  --color-neutral: #111827;
  --color-neutral-subdued: #374151;
  --color-neutral-subtle: #e5e7eb;
  --color-positive: #16a34a;
  --color-positive-subtle: #dcfce7;
  --color-negative: #db2777;
  --color-negative-subtle: #fce7f3;
  --color-notice: #d97706;
  --color-notice-subtle: #fef3c7;
  --color-informative: #1d4ed8;
  --color-informative-subtle: #dbeafe;

  --color-heading: #111827;
  --color-body: #374151;
  --color-detail: #6b7280;
  --color-disabled: #9ca3af;
  --color-on-accent: #ffffff;

  --shadow-elevated: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-emphasized: 0 4px 16px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.04);
  --shadow-dragged: 0 8px 24px rgba(0,0,0,0.12), 0 2px 6px rgba(0,0,0,0.06);

  --radius-sm: 4px;
  --radius-default: 10px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-pill: 9999px;

  --font-sans: "Inter", "DM Sans", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}
"""

_CSS_BASE = """\
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: var(--font-sans);
  font-size: 14px;
  line-height: 1.55;
  color: var(--color-body);
  background: var(--color-layer-1);
  -webkit-font-smoothing: antialiased;
}
a { color: var(--color-accent); text-decoration: none; }
a:hover { text-decoration: underline; }
h1, h2, h3, h4 { color: var(--color-heading); margin: 0 0 12px 0; }
h1 { font-size: 32px; font-weight: 700; line-height: 1.2; }
h2 { font-size: 22px; font-weight: 700; line-height: 1.25; }
h3 { font-size: 18px; font-weight: 700; line-height: 1.3; }
h4 { font-size: 15px; font-weight: 600; line-height: 1.35; }
p { margin: 0 0 12px 0; }
ul, ol { margin: 0 0 12px 0; padding-left: 20px; }
li { margin-bottom: 4px; }
.container {
  max-width: 820px;
  margin: 0 auto;
  padding: 24px 32px;
  background: var(--color-base);
}
section {
  margin-bottom: 40px;
  padding: 32px 0;
  border-top: 1px solid var(--color-neutral-subtle);
}
section:first-of-type { border-top: none; padding-top: 16px; }
"""

_CSS_COMPONENTS = """\
/* Capa */
.capa {
  background: linear-gradient(135deg, var(--color-accent), var(--color-accent-strong));
  color: var(--color-on-accent);
  padding: 40px 32px;
  border-radius: var(--radius-lg);
  margin-bottom: 32px;
  box-shadow: var(--shadow-emphasized);
}
.capa h1 { color: var(--color-on-accent); margin-bottom: 8px; }
.capa .subtitulo { opacity: 0.85; font-size: 14px; margin-bottom: 24px; }
.capa .produto-nome { font-size: 20px; font-weight: 600; margin-bottom: 8px; }
.capa .valor-destaque {
  font-size: 36px;
  font-weight: 700;
  margin: 16px 0;
}
.capa .selo {
  display: inline-block;
  background: rgba(255,255,255,0.2);
  padding: 6px 14px;
  border-radius: var(--radius-pill);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-top: 16px;
}
.capa .como-usar {
  background: rgba(255,255,255,0.12);
  border-radius: var(--radius-default);
  padding: 16px 20px;
  margin-top: 24px;
  font-size: 13px;
}
.capa .como-usar strong { display: block; margin-bottom: 8px; }

/* Indice */
.indice {
  background: var(--color-layer-1);
  border-radius: var(--radius-default);
  padding: 20px 24px;
  margin-bottom: 40px;
  font-size: 13px;
}
.indice h3 { margin-top: 0; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--color-detail); }
.indice ol { margin: 0; padding-left: 20px; }
.indice li { margin-bottom: 2px; }
.indice a { color: var(--color-body); }
.indice a:hover { color: var(--color-accent); }

/* Card */
.card {
  background: var(--color-elevated);
  border-radius: var(--radius-default);
  padding: 16px 20px;
  box-shadow: var(--shadow-elevated);
  margin-bottom: 16px;
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 16px;
  margin-bottom: 16px;
}

/* Bolha WhatsApp */
.bolha {
  background: var(--color-accent-subtle);
  color: var(--color-neutral);
  padding: 12px 16px;
  border-radius: 4px 16px 16px 16px;
  margin-bottom: 8px;
  max-width: 85%;
  font-size: 14px;
  position: relative;
  border: 1px solid var(--color-accent-border);
}
.bolha-grupo {
  background: var(--color-layer-1);
  border-radius: var(--radius-default);
  padding: 16px;
  margin-bottom: 16px;
}
.bolha-grupo h4 { margin-top: 0; }
.bolha-grupo .nota-conducao {
  margin-top: 12px;
  padding: 10px 12px;
  background: var(--color-informative-subtle);
  border-left: 3px solid var(--color-informative);
  border-radius: var(--radius-sm);
  font-size: 12px;
  color: var(--color-informative);
}

/* Pills */
.pill {
  display: inline-block;
  padding: 4px 12px;
  border-radius: var(--radius-pill);
  font-size: 12px;
  font-weight: 500;
  margin: 2px 4px 2px 0;
}
.pill-conectar {
  background: var(--color-positive-subtle);
  color: var(--color-positive);
}
.pill-afastar {
  background: var(--color-negative-subtle);
  color: var(--color-negative);
}
.pill-grupo { margin-bottom: 12px; }

/* Furadeira visual */
.furadeira-visual {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  align-items: stretch;
  margin: 24px 0;
}
.furadeira-etapa {
  flex: 1;
  min-width: 200px;
  background: var(--color-accent-subtle);
  padding: 16px;
  border-radius: var(--radius-default);
  border-left: 4px solid var(--color-accent);
}
.furadeira-etapa .numero {
  display: inline-flex;
  width: 28px;
  height: 28px;
  align-items: center;
  justify-content: center;
  background: var(--color-accent);
  color: var(--color-on-accent);
  border-radius: 50%;
  font-weight: 700;
  font-size: 13px;
  margin-bottom: 8px;
}
.furadeira-etapa .prazo { font-size: 11px; color: var(--color-detail); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
.furadeira-etapa .nome { font-weight: 700; color: var(--color-heading); font-size: 15px; margin-bottom: 6px; }
.furadeira-etapa .resumo { font-size: 13px; color: var(--color-body); }
.furadeira-destino {
  background: var(--color-positive-subtle);
  color: var(--color-positive);
  padding: 12px 16px;
  border-radius: var(--radius-default);
  text-align: center;
  font-weight: 600;
  margin-top: 16px;
}

/* Accordion (objecoes) */
details.objecao {
  background: var(--color-elevated);
  border: 1px solid var(--color-neutral-subtle);
  border-radius: var(--radius-default);
  margin-bottom: 12px;
  overflow: hidden;
}
details.objecao summary {
  padding: 14px 18px;
  cursor: pointer;
  font-weight: 600;
  color: var(--color-heading);
  list-style: none;
}
details.objecao summary::-webkit-details-marker { display: none; }
details.objecao summary::before {
  content: "▸";
  margin-right: 8px;
  color: var(--color-accent);
  display: inline-block;
  transition: transform 0.2s;
}
details.objecao[open] summary::before { transform: rotate(90deg); }
.obj-num {
  display: inline-block;
  background: var(--color-negative-subtle);
  color: var(--color-negative);
  padding: 2px 8px;
  border-radius: var(--radius-pill);
  font-size: 12px;
  margin-right: 8px;
}
.obj-corpo { padding: 0 18px 18px 18px; }
.arg-card {
  background: var(--color-layer-1);
  border-radius: var(--radius-sm);
  margin-bottom: 10px;
  overflow: hidden;
}
details.arg-card > summary {
  padding: 10px 16px;
  cursor: pointer;
  color: var(--color-accent);
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 700;
  list-style: none;
}
details.arg-card > summary::-webkit-details-marker { display: none; }
details.arg-card > summary::before {
  content: "+";
  display: inline-block;
  width: 16px;
  color: var(--color-accent);
  font-weight: 700;
}
details.arg-card[open] > summary::before { content: "−"; }
.arg-card .arg-corpo { padding: 0 16px 12px 16px; }
.arg-card p { margin-bottom: 8px; font-size: 13px; }

/* Tabela */
table.tabela-objecoes, table.tabela-padrao {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
  font-size: 13px;
}
table.tabela-objecoes th, table.tabela-objecoes td,
table.tabela-padrao th, table.tabela-padrao td {
  padding: 10px 12px;
  text-align: left;
  border-bottom: 1px solid var(--color-neutral-subtle);
}
table.tabela-objecoes thead, table.tabela-padrao thead {
  background: var(--color-layer-2);
}
table.tabela-objecoes tbody tr:nth-child(even),
table.tabela-padrao tbody tr:nth-child(even) {
  background: var(--color-layer-1);
}
.num { width: 32px; font-weight: 700; color: var(--color-accent); }

/* Badges */
.badge-tempo {
  display: inline-block;
  background: var(--color-notice-subtle);
  color: var(--color-notice);
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  font-size: 11px;
  font-weight: 600;
  margin-bottom: 8px;
}

/* Placeholder criativo */
.placeholder-criativa {
  background: var(--color-notice-subtle);
  border: 1px dashed var(--color-notice);
  border-radius: var(--radius-default);
  padding: 20px 24px;
  color: var(--color-notice);
  font-size: 13px;
}
.placeholder-criativa strong { display: block; margin-bottom: 6px; font-size: 14px; }

/* Barra de busca */
.search-bar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--color-layer-2);
  border-bottom: 1px solid var(--color-neutral-subtle);
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  padding: 10px 32px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.search-bar input {
  flex: 1;
  max-width: 400px;
  padding: 8px 12px;
  border: 1px solid var(--color-neutral-subtle);
  border-radius: var(--radius-default);
  font-family: inherit;
  font-size: 13px;
}
.search-bar .contador { font-size: 12px; color: var(--color-detail); }
.search-bar button {
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
  color: var(--color-detail);
}
mark.highlight { background: #fff176; color: inherit; border-radius: 2px; padding: 0 2px; }

/* Botao PDF */
.btn-pdf {
  position: fixed;
  right: 24px;
  bottom: 24px;
  background: var(--color-accent);
  color: var(--color-on-accent);
  padding: 12px 20px;
  border-radius: var(--radius-pill);
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 14px;
  box-shadow: var(--shadow-dragged);
  z-index: 99;
}
.btn-pdf:hover { background: var(--color-accent-strong); }

/* Responsivo */
@media (max-width: 720px) {
  .container { padding: 16px; }
  .capa { padding: 24px 20px; }
  .capa .valor-destaque { font-size: 28px; }
  h1 { font-size: 24px; }
  h2 { font-size: 20px; }
  .furadeira-visual { flex-direction: column; }
  .search-bar { padding: 10px 16px; }
}
"""

_CSS_ASSISTENTE = """\
/* Assistente de resposta (matcher local) */
.btn-assistente {
  position: fixed;
  left: 24px;
  bottom: 24px;
  background: var(--color-positive);
  color: var(--color-on-accent);
  padding: 12px 18px;
  border-radius: var(--radius-pill);
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 14px;
  box-shadow: var(--shadow-dragged);
  z-index: 99;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: inherit;
}
.btn-assistente:hover { background: var(--color-accent-strong); }
.assistente-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.45);
  z-index: 200;
  display: none;
  align-items: flex-end;
  justify-content: center;
}
.assistente-overlay.open { display: flex; }
.assistente-painel {
  background: var(--color-base);
  width: 100%;
  max-width: 680px;
  max-height: 88vh;
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  box-shadow: var(--shadow-dragged);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.assistente-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  padding: 16px 20px;
  border-bottom: 1px solid var(--color-neutral-subtle);
  background: var(--color-layer-1);
}
.assistente-header h3 { margin: 0; font-size: 16px; }
.assistente-header .sub { font-size: 12px; color: var(--color-detail); margin-top: 4px; line-height: 1.45; }
.assistente-fechar {
  background: transparent;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: var(--color-detail);
  line-height: 1;
  padding: 0 4px;
}
.assistente-corpo {
  padding: 18px 20px 22px;
  overflow-y: auto;
  flex: 1;
}
.assistente-input {
  width: 100%;
  min-height: 96px;
  padding: 12px;
  border: 1px solid var(--color-neutral-subtle);
  border-radius: var(--radius-default);
  font-family: inherit;
  font-size: 14px;
  line-height: 1.5;
  resize: vertical;
  background: var(--color-layer-1);
  color: var(--color-body);
}
.assistente-input:focus {
  outline: none;
  border-color: var(--color-accent);
  background: var(--color-base);
}
.assistente-acoes {
  display: flex;
  gap: 8px;
  margin-top: 10px;
  flex-wrap: wrap;
}
.assistente-btn {
  padding: 10px 18px;
  border: none;
  border-radius: var(--radius-default);
  font-family: inherit;
  font-weight: 600;
  font-size: 13px;
  cursor: pointer;
}
.assistente-btn-primario { background: var(--color-accent); color: var(--color-on-accent); }
.assistente-btn-primario:hover { background: var(--color-accent-strong); }
.assistente-btn-secundario { background: var(--color-neutral-subtle); color: var(--color-body); }
.assistente-btn-secundario:hover { background: #e2e2e2; }
.assistente-dica { font-size: 12px; color: var(--color-detail); margin-top: 8px; }
.assistente-resultado { margin-top: 18px; display: none; }
.assistente-resultado.show { display: block; }
.assistente-intencao {
  background: var(--color-accent-subtle);
  border-left: 3px solid var(--color-accent);
  padding: 10px 14px;
  border-radius: var(--radius-default);
  font-size: 13px;
  margin-bottom: 14px;
  color: var(--color-body);
}
.assistente-intencao strong { color: var(--color-accent); }
.assistente-resposta {
  background: var(--color-layer-1);
  border: 1px solid var(--color-neutral-subtle);
  border-radius: var(--radius-default);
  padding: 14px;
  margin-bottom: 10px;
}
.assistente-resposta-texto {
  white-space: pre-wrap;
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 10px;
  color: var(--color-body);
}
.assistente-copiar {
  background: var(--color-positive);
  color: var(--color-on-accent);
  border: none;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}
.assistente-copiar:hover { background: var(--color-accent-strong); }
.assistente-copiar.copiado { background: var(--color-accent); }
.assistente-link-secao {
  display: inline-block;
  margin-top: 6px;
  font-size: 12px;
  color: var(--color-accent);
}
@media (max-width: 720px) {
  .btn-assistente { left: 12px; bottom: 12px; padding: 10px 14px; font-size: 13px; }
  .assistente-painel { max-width: 100%; max-height: 92vh; }
  .assistente-corpo { padding: 14px 16px 18px; }
}
"""

_CSS_PRINT = """\
@media print {
  body { background: white; font-size: 11pt; }
  .container { max-width: none; padding: 0; }
  .search-bar, .btn-pdf { display: none !important; }
  section { break-inside: avoid; }
  .card, .bolha-grupo, .furadeira-etapa, .arg-card { break-inside: avoid; }
  details.objecao[open] summary { display: none; }
  details.objecao { border: none; background: white; }
  details.objecao .obj-corpo { padding: 0; }
  details.objecao { max-height: none !important; overflow: visible !important; }
  details.objecao:not([open]) .obj-corpo { display: block; }
  details.arg-card .arg-corpo { display: block !important; }
  details.arg-card > summary::before { content: none; }
  a { color: inherit; text-decoration: none; }
  @page { margin: 1.5cm 2cm; }
}
"""

_JS = """\
(function() {
  function buscar(termo) {
    limpar();
    if (!termo || termo.length < 2) {
      document.getElementById('contador-busca').textContent = '';
      return;
    }
    var re = new RegExp('(' + termo.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&') + ')', 'gi');
    var container = document.querySelector('.container');
    var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
    var textos = [];
    while (walker.nextNode()) {
      var node = walker.currentNode;
      if (node.parentElement.closest('script, style, .search-bar, .btn-pdf')) continue;
      if (re.test(node.textContent)) textos.push(node);
      re.lastIndex = 0;
    }
    var total = 0;
    textos.forEach(function(node) {
      var span = document.createElement('span');
      span.innerHTML = node.textContent.replace(re, '<mark class="highlight">$1</mark>');
      total += span.querySelectorAll('mark.highlight').length;
      node.parentNode.replaceChild(span, node);
    });
    document.getElementById('contador-busca').textContent = total + ' resultado(s)';
    var primeiro = container.querySelector('mark.highlight');
    if (primeiro) primeiro.scrollIntoView({behavior: 'smooth', block: 'center'});
  }
  function limpar() {
    document.querySelectorAll('mark.highlight').forEach(function(m) {
      var pai = m.parentNode;
      pai.replaceChild(document.createTextNode(m.textContent), m);
      pai.normalize();
    });
    document.getElementById('contador-busca').textContent = '';
  }
  document.addEventListener('DOMContentLoaded', function() {
    var input = document.getElementById('input-busca');
    var btnLimpar = document.getElementById('btn-limpar-busca');
    if (input) input.addEventListener('input', function(e) { buscar(e.target.value); });
    if (btnLimpar) btnLimpar.addEventListener('click', function() {
      input.value = '';
      limpar();
    });
  });
})();
"""

_JS_ASSISTENTE = """\
(function() {
  var CTX = window.PLAYBOOK_CTX || {};
  var PRODUTO = CTX.nome_produto || 'o programa';
  var QUADRO = CTX.quadro || 'a transformação que você procura';
  var PRECO = CTX.preco_texto || 'o investimento do programa';

  var INTENCOES = [
    { id: 'pronto-comprar', label: 'Pronto para comprar', secao: 'secao-8', secao_nome: 'Fechamento em 4 passos',
      palavras: ['quero comprar','como pago','onde pago','fechado','me manda o link','pode mandar o link','mandar o link','aceitei','quero fechar','tô dentro','to dentro','pode fechar','vou fechar'] },
    { id: 'preco', label: 'Perguntou preço', secao: 'secao-7', secao_nome: 'Apresentação e ancoragem de preço',
      palavras: ['quanto custa','quanto é','qual o valor','qual o preço','valor do','preço do','valor do curso','preço do curso'] },
    { id: 'caro', label: 'Achou caro', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['caro','muito caro','acima do','alto demais','salgado','fora do orçamento','fora do orcamento','não tenho esse valor','nao tenho esse valor'] },
    { id: 'desconto', label: 'Pediu desconto ou parcelamento', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['desconto','mais barato','abater','cupom','parcelar','dividir em','quantas vezes','parcela'] },
    { id: 'sem-dinheiro', label: 'Sem dinheiro no momento', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['sem dinheiro','não tenho dinheiro','nao tenho dinheiro','apertado','mês que vem','mes que vem','agora não','agora nao','quando der','quando puder','tô duro','to duro','sem grana'] },
    { id: 'vou-pensar', label: 'Vai pensar', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['vou pensar','preciso pensar','pensar com calma','analisar com calma','vou ver','depois eu te falo','depois te falo','me dá um tempo','me da um tempo','preciso avaliar'] },
    { id: 'sem-tempo', label: 'Falta de tempo', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['sem tempo','não vou ter tempo','nao vou ter tempo','muito corrido','corrida','ocupado','ocupada','agenda cheia','não consigo acompanhar','nao consigo acompanhar','rotina cheia'] },
    { id: 'ja-tentei', label: 'Já tentou antes', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['já tentei','ja tentei','já fiz','ja fiz','não deu certo','nao deu certo','não funcionou pra mim','nao funcionou','já comprei','ja comprei','já investi','ja investi'] },
    { id: 'confiar', label: 'Dúvida se funciona', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['funciona mesmo','é sério','eh serio','é verdade','eh verdade','golpe','confiar','como sei','como saber','tenho medo','será que funciona','sera que funciona'] },
    { id: 'conjuge', label: 'Vai falar com cônjuge ou família', secao: 'secao-9', secao_nome: 'Quebra de objeções (7 Argumentos)',
      palavras: ['falar com meu marido','falar com minha esposa','conversar com meu marido','conversar com minha esposa','ver com minha família','ver com minha familia','falar em casa','minha mulher','meu esposo'] },
    { id: 'meu-caso-diferente', label: 'Acha que o caso dele é diferente', secao: 'secao-6', secao_nome: 'SPIN adaptado ao WhatsApp',
      palavras: ['meu caso é diferente','meu caso eh diferente','minha situação','minha situacao','é diferente','eh diferente','comigo é','comigo eh','no meu caso'] },
    { id: 'como-funciona', label: 'Quer entender o método', secao: 'secao-2', secao_nome: 'Identidade do Produto',
      palavras: ['como funciona','como é','como eh','me explica','o que é','o que eh','me conta mais','me fala mais','do que se trata','no que consiste','funciona como'] },
    { id: 'prova', label: 'Pediu prova ou depoimento', secao: 'secao-7', secao_nome: 'Apresentação e ancoragem de preço',
      palavras: ['depoimento','caso de sucesso','prova','resultado de aluno','quem já','quem ja','alguém conseguiu','alguem conseguiu','tem algum caso','algum resultado'] },
    { id: 'saudacao', label: 'Saudação inicial', secao: 'secao-5', secao_nome: 'Abordagem Receptiva · Inbound',
      palavras: ['oi','olá','ola','bom dia','boa tarde','boa noite','tudo bem','tudo bom','td bem','oii','e aí','e ai','opa'] }
  ];

  var RESPOSTAS = {
    'pronto-comprar': [
      '[NOME], show. Vou te mandar o checkout agora. Me confirma a compra por aqui que já libero seus acessos.',
      'Perfeito, [NOME]. Link do checkout: [COLE O LINK]. Depois do pagamento me avisa que eu mando as boas-vindas e os primeiros passos.'
    ],
    'preco': [
      '[NOME], antes de te passar o valor quero entender seu momento pra saber se faz sentido. Você está buscando resolver isso agora ou ainda tá só pesquisando?',
      'Posso te passar, [NOME]. O investimento no ' + PRODUTO + ' é ' + PRECO + '. Antes disso, me conta rapidinho: o que te fez procurar sobre isso agora?'
    ],
    'caro': [
      '[NOME], eu entendo a percepção. Pra eu te ajudar melhor: hoje você compara esse valor com o quê especificamente?',
      'Faz sentido o que você sentiu, [NOME]. Só pra gente olhar junto: se essa dificuldade continuar por mais 6 meses, quanto isso custa pra você em tempo, energia e oportunidade? Esse é o preço real de não resolver.',
      'Posso te mostrar de outro ângulo, [NOME]. O valor é ' + PRECO + '. Dividido pelo tempo de acompanhamento, sai por bem menos que a maioria gasta em coisas que não mudam o resultado. Faz sentido olhar assim?'
    ],
    'desconto': [
      '[NOME], o valor é fixo pra todo mundo, exatamente pra não gerar insegurança em quem pagou o preço cheio. O parcelamento vai até [X]x sem entrada. Te mando o link?',
      'Entendo o pedido, [NOME]. O que consigo garantir por você é o bônus [NOME DO BÔNUS] que fecha hoje. No cartão dá pra parcelar em [X]x. Como prefere, à vista ou parcelado?'
    ],
    'sem-dinheiro': [
      '[NOME], faz sentido pensar assim. Só quero te perguntar uma coisa: quanto você imagina que já gastou nos últimos 12 meses tentando resolver isso por fora? Às vezes o custo de adiar sai mais caro que o programa.',
      'Te entendo, [NOME]. Dá pra começar no cartão parcelado em [X]x, a primeira parcela só entra daqui a 30 dias. Assim você começa hoje e a parcela chega depois que já viu resultado. Faz sentido pra você?'
    ],
    'vou-pensar': [
      '[NOME], claro. Só pra eu te ajudar a pensar com mais clareza, o que ainda falta pra você sentir segurança de decidir? É o método, o tempo, o valor ou outra coisa?',
      'Faz sentido. Só te adianto uma coisa: a condição de hoje (bônus mais parcelamento) fecha em [X]h. Depois disso volta ao valor cheio. Quer que eu te mande o link pra você decidir com o material em mãos?'
    ],
    'sem-tempo': [
      '[NOME], entendo. A maioria dos alunos começa exatamente nesse cenário. O programa pede poucos minutos por dia e foi desenhado pra quem tem rotina cheia. A pergunta que faz diferença é: essa falta de tempo hoje vai sumir em 3 meses sozinha ou só vai piorar?',
      'Faz total sentido, [NOME]. Por isso o formato é gravado e você assiste no seu ritmo. Dá pra acompanhar no trânsito, na academia, na cozinha. Quer que eu te mostre como funciona a primeira semana?'
    ],
    'ja-tentei': [
      '[NOME], me conta rapidinho o que você tentou antes e onde travou. Assim consigo te falar com honestidade se o ' + PRODUTO + ' vai te servir ou não.',
      'Ajuda a gente pensar assim, [NOME]: o que a maioria tenta resolve parte, mas não resolve a causa. O que a gente faz diferente é [DIFERENCIAL DA FURADEIRA]. Por isso quem já tentou antes costuma ver resultado aqui.'
    ],
    'confiar': [
      '[NOME], pergunta justa. Tenho alunos formados nos últimos anos com resultado documentado. Te mando 2 depoimentos de pessoas com perfil parecido com o seu pra você ver com seus olhos?',
      'Faz sentido pedir prova, [NOME]. A garantia é de [X] dias: se você entrar, seguir o método e não ver resultado, devolvo 100% do valor. Quem tá errado é quem paga, não você.'
    ],
    'conjuge': [
      '[NOME], claro. Só pra você já chegar em casa com tudo na mão, te passo um resumo em 5 linhas do que é o ' + PRODUTO + ', o que entrega, prazo e valor. Posso mandar?',
      'Faz sentido, [NOME]. Quando for conversar, duas perguntas que ajudam a família a entender: 1) quanto essa dificuldade tá custando hoje em casa; 2) quanto vai custar em 6 meses sem resolver. Aí o valor faz mais sentido.'
    ],
    'meu-caso-diferente': [
      '[NOME], me conta um pouco mais do seu caso. O que você considera diferente? Assim consigo te falar com honestidade se o ' + PRODUTO + ' serve ou não.',
      'Ajuda se eu te perguntar por partes, [NOME]: 1) há quanto tempo você convive com isso? 2) o que já tentou? 3) o que mudaria na sua rotina se isso fosse resolvido nos próximos 90 dias?'
    ],
    'como-funciona': [
      '[NOME], explico em 3 mensagens rápidas. O ' + PRODUTO + ' entrega ' + QUADRO + '. O método é dividido em etapas claras e você sai de [ponto A] pra [ponto B] em [prazo].',
      'Antes de entrar nos detalhes, [NOME], me diz uma coisa: qual parte disso mais te interessa resolver hoje? Assim eu foco a explicação no que te serve.'
    ],
    'prova': [
      '[NOME], te mando 2 casos de alunos com perfil parecido com o seu. Só me fala antes: você tá mais em busca de [cenário A] ou [cenário B]? Aí te mando o caso mais próximo do seu.',
      'Claro, [NOME]. [Nome fictício], [perfil], tinha [dificuldade]. Em [tempo] conseguiu [resultado]. Quer que eu te mostre o print do depoimento?'
    ],
    'saudacao': [
      'Oi, [NOME]. Tudo bem? Vi que você chegou aqui. O que te fez procurar sobre o ' + PRODUTO + ' agora?',
      'Oi, [NOME]. Seja bem-vindo(a). Antes de te mandar qualquer coisa, me conta rapidamente o seu cenário: o que você quer resolver?'
    ]
  };

  function normalizar(texto) {
    return (texto || '').toLowerCase()
      .normalize('NFD').replace(/[\\u0300-\\u036f]/g, '')
      .replace(/\\s+/g, ' ').trim();
  }

  function detectar(mensagem) {
    var txt = normalizar(mensagem);
    if (!txt) return [];
    var achados = [];
    INTENCOES.forEach(function(intencao) {
      var pontuacao = 0;
      intencao.palavras.forEach(function(palavra) {
        var p = normalizar(palavra);
        if (txt.indexOf(p) !== -1) {
          pontuacao += p.length > 5 ? 2 : 1;
        }
      });
      if (pontuacao > 0) achados.push({ intencao: intencao, pontos: pontuacao });
    });
    achados.sort(function(a, b) { return b.pontos - a.pontos; });
    return achados;
  }

  function escaparHTML(s) {
    return String(s).replace(/[&<>"']/g, function(c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function copiarTexto(btn, texto) {
    function ok() {
      btn.classList.add('copiado');
      var original = btn.getAttribute('data-original') || btn.textContent;
      btn.setAttribute('data-original', original);
      btn.textContent = 'Copiado ✓';
      setTimeout(function() {
        btn.classList.remove('copiado');
        btn.textContent = original;
      }, 1800);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(texto).then(ok).catch(function() {
        var ta = document.createElement('textarea');
        ta.value = texto; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); } catch(e) {}
        document.body.removeChild(ta); ok();
      });
    } else {
      var ta = document.createElement('textarea');
      ta.value = texto; document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); } catch(e) {}
      document.body.removeChild(ta); ok();
    }
  }

  function ligarCopiar() {
    document.querySelectorAll('.assistente-copiar').forEach(function(btn) {
      btn.onclick = function() { copiarTexto(btn, btn.getAttribute('data-texto')); };
    });
  }

  function renderResultado(achados) {
    var box = document.getElementById('assistente-resultado');
    if (!achados.length) {
      var fallback = '[NOME], me conta um pouco mais do seu momento? O que exatamente você quer resolver aí?';
      box.innerHTML = '<div class="assistente-intencao"><strong>Sem padrão claro detectado.</strong> Sugestão: volte à Descoberta e faça uma pergunta aberta de diagnóstico (SPIN) antes de responder.</div>' +
        '<div class="assistente-resposta"><div class="assistente-resposta-texto">' + escaparHTML(fallback) + '</div>' +
        '<button class="assistente-copiar" data-texto="' + escaparHTML(fallback) + '">Copiar resposta</button></div>' +
        '<a class="assistente-link-secao" href="#secao-6">Ver SPIN no playbook →</a>';
      box.classList.add('show');
      ligarCopiar();
      return;
    }
    var principal = achados[0].intencao;
    var outros = achados.slice(1, 3).map(function(a) { return a.intencao.label; }).join(', ');
    var html = '<div class="assistente-intencao">Intenção detectada: <strong>' + escaparHTML(principal.label) + '</strong>' +
      (outros ? ' · também casou com: ' + escaparHTML(outros) : '') + '</div>';
    var respostas = RESPOSTAS[principal.id] || [];
    respostas.forEach(function(resposta) {
      html += '<div class="assistente-resposta">' +
        '<div class="assistente-resposta-texto">' + escaparHTML(resposta) + '</div>' +
        '<button class="assistente-copiar" data-texto="' + escaparHTML(resposta) + '">Copiar resposta</button>' +
        '</div>';
    });
    html += '<a class="assistente-link-secao" href="#' + principal.secao + '">Ver ' + escaparHTML(principal.secao_nome) + ' no playbook →</a>';
    box.innerHTML = html;
    box.classList.add('show');
    ligarCopiar();
  }

  document.addEventListener('DOMContentLoaded', function() {
    var btn = document.getElementById('btn-assistente');
    var overlay = document.getElementById('assistente-overlay');
    var fechar = document.getElementById('assistente-fechar');
    var analisar = document.getElementById('assistente-analisar');
    var limpar = document.getElementById('assistente-limpar');
    var input = document.getElementById('assistente-input');
    var resultado = document.getElementById('assistente-resultado');
    if (!btn || !overlay) return;

    btn.addEventListener('click', function() {
      overlay.classList.add('open');
      setTimeout(function() { if (input) input.focus(); }, 50);
    });
    fechar.addEventListener('click', function() { overlay.classList.remove('open'); });
    overlay.addEventListener('click', function(ev) { if (ev.target === overlay) overlay.classList.remove('open'); });
    document.addEventListener('keydown', function(ev) {
      if (ev.key === 'Escape' && overlay.classList.contains('open')) overlay.classList.remove('open');
    });
    analisar.addEventListener('click', function() { renderResultado(detectar(input.value)); });
    limpar.addEventListener('click', function() {
      input.value = '';
      resultado.classList.remove('show');
      resultado.innerHTML = '';
      input.focus();
    });
    input.addEventListener('keydown', function(ev) {
      if ((ev.ctrlKey || ev.metaKey) && ev.key === 'Enter') analisar.click();
    });
  });
})();
"""


# ============================================================================
# Shell HTML
# ============================================================================

INDICE_SECOES = [
    ("secao-1", "Capa"),
    ("secao-2", "Identidade do Produto"),
    ("secao-3", "Metodologia DEF"),
    ("secao-4", "Abordagem Ativa. Outbound WhatsApp"),
    ("secao-5", "Abordagem Receptiva. Inbound WhatsApp"),
    ("secao-6", "SPIN adaptado ao WhatsApp"),
    ("secao-7", "Apresentação e ancoragem de preço"),
    ("secao-8", "Fechamento em 4 passos"),
    ("secao-9", "Quebra de objeções pelos 7 Argumentos"),
    ("secao-10", "Recuperação de carrinho"),
    ("secao-11", "Follow-up, Upsell, Downsell, Order Bump"),
    ("secao-12", "Dicionário do Comercial"),
]


def render_shell(titulo: str, conteudo: str, ctx: dict | None = None) -> str:
    """Monta o HTML completo a partir do conteudo do miolo.

    ctx: dicionario opcional com dados do produto usados pelo assistente de
    resposta. Chaves esperadas: nome_produto, quadro, preco_texto.
    """
    css = _CSS_TOKENS + _CSS_BASE + _CSS_COMPONENTS + _CSS_ASSISTENTE + _CSS_PRINT
    ctx_dict = {
        "nome_produto": (ctx or {}).get("nome_produto", ""),
        "quadro": (ctx or {}).get("quadro", ""),
        "preco_texto": (ctx or {}).get("preco_texto", ""),
    }
    # Evita quebra do script via </script> embutido no JSON
    ctx_json = json.dumps(ctx_dict, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<div class="search-bar">
  <input id="input-busca" type="search" placeholder="🔍 Buscar no playbook..." />
  <span id="contador-busca" class="contador"></span>
  <button id="btn-limpar-busca" title="Limpar busca">✕</button>
</div>
<button class="btn-pdf" onclick="window.print()">📄 Exportar PDF</button>
<button id="btn-assistente" class="btn-assistente" title="Cole a mensagem do lead e receba sugestão de resposta">💬 Assistente de resposta</button>
<div id="assistente-overlay" class="assistente-overlay" role="dialog" aria-modal="true" aria-labelledby="assistente-titulo">
  <div class="assistente-painel">
    <div class="assistente-header">
      <div>
        <h3 id="assistente-titulo">Assistente de resposta</h3>
        <div class="sub">Cole o que o lead te mandou. O assistente detecta a intenção e sugere mensagens prontas pra colar no WhatsApp.</div>
      </div>
      <button id="assistente-fechar" class="assistente-fechar" aria-label="Fechar">×</button>
    </div>
    <div class="assistente-corpo">
      <textarea id="assistente-input" class="assistente-input" placeholder="Ex: Achei caro, não tô conseguindo esse valor agora..."></textarea>
      <div class="assistente-acoes">
        <button id="assistente-analisar" class="assistente-btn assistente-btn-primario">Analisar mensagem</button>
        <button id="assistente-limpar" class="assistente-btn assistente-btn-secundario">Limpar</button>
      </div>
      <div class="assistente-dica">Dica: troque [NOME] pelo primeiro nome do lead antes de enviar. Ctrl+Enter analisa.</div>
      <div id="assistente-resultado" class="assistente-resultado"></div>
    </div>
  </div>
</div>
<div class="container">
{conteudo}
</div>
<script>window.PLAYBOOK_CTX = {ctx_json};</script>
<script>
{_JS}
</script>
<script>
{_JS_ASSISTENTE}
</script>
</body>
</html>
"""


def render_indice() -> str:
    linhas = []
    for i, (sid, nome) in enumerate(INDICE_SECOES, start=1):
        linhas.append(f'    <li><a href="#{sid}">{i}. {e(nome)}</a></li>')
    return (
        '<nav class="indice" aria-label="Índice">\n'
        '  <h3>Índice</h3>\n'
        '  <ol>\n'
        + "\n".join(linhas)
        + '\n  </ol>\n'
        '</nav>\n'
    )


# ============================================================================
# Renderers de secoes estaticas
# ============================================================================


def render_capa(d: dict) -> str:
    """Secao 1. Capa."""
    return f"""<section id="secao-1">
  <div class="capa">
    <div class="subtitulo">Playbook comercial · Venda 1:1 por WhatsApp</div>
    <h1>{e(d.get("nome_produto", "Produto"))}</h1>
    <div class="produto-nome">Quadro: {e(d.get("quadro", ""))}</div>
    <div class="valor-destaque">{e(d.get("preco_texto", "Preço a definir"))}</div>
    <span class="selo">Venda 1:1 por WhatsApp</span>
    <div class="como-usar">
      <strong>Como usar este playbook</strong>
      Comece pela Identidade do Produto (seção 2) para aprender o método. Depois veja a Metodologia DEF (seção 3) para entender a moldura da conversa.
      No atendimento, vá direto ao cenário: 4 (outbound), 5 (inbound) ou 10 (recuperação de carrinho).
    </div>
  </div>
</section>
"""


def render_identidade_produto(d: dict) -> str:
    """Secao 2. Identidade do Produto (Furadeira, entregáveis, diferenciais, argumentos)."""
    nome = d.get("nome_produto", "o produto")
    quadro = d.get("quadro", "")
    furadeira_nome = d.get("furadeira_nome", "")
    etapas = d.get("furadeira_etapas", []) or []
    entregaveis = d.get("entregaveis", []) or []
    diferenciais = d.get("diferenciais", []) or []
    argumentos = d.get("argumentos_incontestaveis", []) or []
    posicionamento = d.get("posicionamento", "")
    preco = d.get("preco_texto", "")

    # Furadeira como trilha numerada
    if etapas:
        etapas_html = []
        for et in etapas:
            num = e(et.get("numero", ""))
            nm = e(et.get("nome", ""))
            prazo = et.get("prazo", "")
            resumo = et.get("resumo", "")
            badge = f'<span class="badge-tempo">{e(prazo)}</span>' if prazo else ""
            resumo_html = f'<p style="font-size:13px;margin:4px 0 0 0;color:var(--color-detail);">{e(resumo)}</p>' if resumo else ""
            etapas_html.append(
                f'<div class="card" style="margin-bottom:10px;">'
                f'<h4 style="margin:0 0 4px 0;">{num}. {nm} {badge}</h4>'
                f'{resumo_html}'
                f'</div>'
            )
        furadeira_html = "".join(etapas_html)
    else:
        furadeira_html = '<p style="color:var(--color-detail);font-size:13px;">Furadeira não cadastrada no perfil.md. Rode /produto-concepcao.</p>'

    entregaveis_html = "".join(f'<li>{e(it)}</li>' for it in entregaveis) or "<li>Não cadastrado.</li>"
    diferenciais_html = "".join(f'<li>{e(it)}</li>' for it in diferenciais) or "<li>Não cadastrado.</li>"
    argumentos_html = "".join(f'<li>{e(it)}</li>' for it in argumentos) or "<li>Não cadastrado.</li>"

    pos_html = f'<p><strong>Posicionamento:</strong> {e(posicionamento)}</p>' if posicionamento else ""
    preco_html = f'<p><strong>Preço:</strong> {e(preco)}</p>' if preco else ""
    furadeira_titulo = f"Furadeira: {e(furadeira_nome)}" if furadeira_nome else "Furadeira"

    return f"""<section id="secao-2">
  <h2>2. Identidade do Produto</h2>
  <p>Para o time aprender o produto do zero. Tudo aqui vem do perfil.md do produto ativo.</p>
  <div class="card">
    <h3 style="margin-top:0;">{e(nome)}</h3>
    <p><strong>Quadro (transformação):</strong> {e(quadro)}</p>
    {pos_html}
    {preco_html}
  </div>

  <h3 style="margin-top:24px;">{furadeira_titulo}</h3>
  <p style="font-size:13px;color:var(--color-detail);">Método em macroetapas. O que o aluno faz em cada passo.</p>
  {furadeira_html}

  <h3 style="margin-top:24px;">Entregáveis</h3>
  <ul>{entregaveis_html}</ul>

  <h3 style="margin-top:24px;">Diferenciais competitivos</h3>
  <ul>{diferenciais_html}</ul>

  <h3 style="margin-top:24px;">Argumentos Incontestáveis</h3>
  <p style="font-size:13px;color:var(--color-detail);">Dados concretos com fonte. Use no Fechamento e na quebra de objeções.</p>
  <ul>{argumentos_html}</ul>
</section>
"""


def render_def(d: dict) -> str:
    """Secao 3. Metodologia DEF (Descoberta, Encantamento, Fechamento)."""
    quadro = d.get("quadro", "a transformação do produto")
    estagios = [
        {
            "letra": "D",
            "nome": "Descoberta",
            "cor_bg": "var(--color-informative-subtle)",
            "cor_borda": "var(--color-informative)",
            "objetivo": "Entender o cenário, a dor real e o momento do lead. Perguntar mais do que falar.",
            "sinais": "O lead descreve a dor com as próprias palavras e pede uma saída.",
            "frases": [
                "Me conta rapidinho: o que está travando você hoje em relação a [tema]?",
                "Antes de eu explicar qualquer coisa, quero entender o seu momento. O que já tentou e não funcionou?",
            ],
        },
        {
            "letra": "E",
            "nome": "Encantamento",
            "cor_bg": "var(--color-notice-subtle)",
            "cor_borda": "var(--color-notice)",
            "objetivo": "Conectar a dor ao Quadro e à Furadeira com as palavras do lead. Mostrar que o método resolve aquilo especificamente.",
            "sinais": "O lead pergunta preço, formato ou prazo.",
            "frases": [
                f"Pelo que você descreveu, a saída passa exatamente por {quadro}. O método tem uma trilha pra isso.",
                "Isso que você está sentindo é o que o passo 2 da Furadeira destrava. Não é aleatório, tem ordem.",
            ],
        },
        {
            "letra": "F",
            "nome": "Fechamento",
            "cor_bg": "var(--color-positive-subtle)",
            "cor_borda": "var(--color-positive)",
            "objetivo": "Apresentar preço com ancoragem, quebrar a última objeção e enviar o link.",
            "sinais": "O lead confirma que faz sentido e pergunta como pagar.",
            "frases": [
                "Faz sentido pra você? Se sim, já te mando o checkout aqui.",
                "Vou te enviar o link agora. Me confirma a compra por aqui que libero os acessos no ato.",
            ],
        },
    ]

    cards = []
    for i, est in enumerate(estagios, start=1):
        frases_html = "".join(f'<div class="bolha">{e(fr)}</div>' for fr in est["frases"])
        cards.append(f"""  <div class="card" style="background:{est['cor_bg']};border-left:4px solid {est['cor_borda']};margin-bottom:16px;">
    <h3 style="color:{est['cor_borda']};margin-top:0;">{i}. {est['letra']}. {e(est['nome'])}</h3>
    <p><strong>Objetivo:</strong> {e(est['objetivo'])}</p>
    <p><strong>Sinais para avançar:</strong> {e(est['sinais'])}</p>
    <div style="margin-top:12px;">
      <strong style="font-size:13px;color:var(--color-detail);text-transform:uppercase;letter-spacing:0.5px;">Frases prontas</strong>
      {frases_html}
    </div>
  </div>""")

    return f"""<section id="secao-3">
  <h2>3. Metodologia DEF (moldura da conversa)</h2>
  <p>Toda venda 1:1 por WhatsApp segue 3 estágios em ordem fixa. O vendedor só avança depois que o lead sinaliza prontidão. Cair fora da ordem queima a conversa.</p>
{"".join(cards)}
  <div class="card" style="background:var(--color-negative-subtle);border-left:3px solid var(--color-negative);">
    <strong>Regra de ouro:</strong> nunca pule da D direto para a F. Se o lead perguntar preço antes do E, volte com uma pergunta que amarre o preço ao valor já reconhecido.
  </div>
</section>
"""


def render_fechamento(d: dict) -> str:
    """Secao 8. Fechamento em 4 passos (template)."""
    produto = d.get("nome_produto", "o programa")
    preco = d.get("preco_texto", "o valor da oferta")
    quadro = d.get("quadro", "a transformação principal")
    return f"""<section id="secao-8">
  <h2>8. Fechamento em 4 passos (WhatsApp)</h2>
  <p>Sequência pronta. Substitua [Nome], [DOR], [TEMPO] pelos dados do lead na conversa real.</p>
  <div class="bolha-grupo">
    <h4>Passo 1. Conexão dor-solução</h4>
    <div class="bolha">[Nome], sua dificuldade é [DOR]. É exatamente isso que {e(produto)} resolve. Em [TEMPO] você consegue {e(quadro)}.</div>
  </div>
  <div class="bolha-grupo">
    <h4>Passo 2. Ancoragem de valor</h4>
    <div class="bolha">Se você fosse resolver isso com os paliativos que já tentou, gastaria muito mais e continuaria sem método. Aqui você tem trilha, acompanhamento e ponto final.</div>
    <div class="bolha">Isso significa parar de pagar por solução avulsa e passar a ter um sistema que resolve de uma vez.</div>
  </div>
  <div class="bolha-grupo">
    <h4>Passo 3. Preço + confirmação</h4>
    <div class="bolha">Tudo isso por {e(preco)}. Faz sentido pra você?</div>
  </div>
  <div class="bolha-grupo">
    <h4>Passo 4. Envio do link</h4>
    <div class="bolha">Vou te mandar o checkout agora. Me confirma a compra por aqui que já libero seus acessos.</div>
  </div>
  <div class="card" style="background:var(--color-negative-subtle);border-left:3px solid var(--color-negative);">
    <strong>Proibido:</strong> perguntar "quer comprar?". Assuma o interesse e envie o link.
  </div>
</section>
"""


def render_dicionario() -> str:
    """Secao 12. Dicionario do Comercial (fixo, 16 termos)."""
    termos = [
        ("Lead", "Pessoa que entrou em contato ou foi abordada pelo comercial. Ainda não é aluno."),
        ("Inbound", "Lead que chega por iniciativa dele (anúncio, orgânico, link da bio). Já tem dor consciente."),
        ("Outbound", "Lead que o comercial aborda primeiro. Tem perfil, mas ainda não sabe que tem a dor."),
        ("SDR", "Vendedor que faz o primeiro contato, qualifica o lead e passa adiante. Não fecha venda."),
        ("Closer", "Vendedor responsável pelo fechamento. Recebe o lead já qualificado pelo SDR."),
        ("CRM", "Ferramenta onde o time registra lead, conversa, etiqueta e etapa do funil."),
        ("Funil de vendas", "Caminho que o lead percorre do primeiro contato à compra. Cada etapa tem critério de passagem."),
        ("Follow-up", "Retomada com lead que não fechou. Serve para lembrar, reaquecer ou oferecer alternativa."),
        ("Prospecção", "Processo de encontrar e abordar leads novos (outbound)."),
        ("Perpétuo", "Modelo de venda sempre aberta, sem data de corte. Oposto de lançamento."),
        ("SPIN", "Framework de diagnóstico com 4 fases (Situação, Problema, Implicação, Necessidade)."),
        ("Objeção", "Motivo que o lead dá para não comprar agora. Nem sempre é o motivo real."),
        ("Ancoragem", "Apresentar um valor maior antes do preço real para fazer o preço real parecer justo."),
        ("Upsell", "Oferta complementar enviada a quem já comprou."),
        ("Downsell", "Oferta de menor valor para quem não aceitou a principal."),
        ("Order bump", "Item adicional oferecido dentro do checkout, com 1 clique, preço baixo."),
    ]
    cards = []
    for termo, definicao in termos:
        cards.append(
            f'<div class="card" style="margin-bottom:0;">'
            f'<h4 style="color:var(--color-accent);margin-bottom:6px;">{e(termo)}</h4>'
            f'<p style="margin:0;font-size:13px;">{e(definicao)}</p>'
            f'</div>'
        )
    return f"""<section id="secao-12">
  <h2>12. Dicionário do Comercial</h2>
  <p>Glossário dos termos que o time comercial vai ouvir no dia a dia. Releia sempre que bater dúvida.</p>
  <div class="card-grid">
{"".join(cards)}
  </div>
</section>
"""


# ============================================================================
# Placeholders para secoes criativas (fallback legado)
# ============================================================================


def placeholder_criativa(numero: int, titulo: str, instrucao: str) -> str:
    """Marca onde o modelo deve preencher via Edit tool (legado, não usado nas 6 criativas)."""
    sid = f"secao-{numero}"
    return f"""<section id="{sid}">
  <h2>{numero}. {e(titulo)}</h2>
  <!-- CREATIVE_{numero}_START -->
  <div class="placeholder-criativa">
    <strong>Seção a preencher pelo modelo</strong>
    {e(instrucao)}
  </div>
  <!-- CREATIVE_{numero}_END -->
</section>
"""


# ============================================================================
# Renderers das 6 secoes criativas (estrutura HTML fixa, marcadores {{chave}}
# nos lugares de texto. Os agentes devolvem JSON plano {"N.chave": "texto"}
# e playbook-aplicar-criativas.py substitui os marcadores).
# ============================================================================


def _bloco_variacoes(numero: int, bid: str, titulo: str, sub: str) -> str:
    """Bolha-grupo com 2 variações (a=leve, b=direta) + 1 nota de condução."""
    sub_html = f'<p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">{e(sub)}</p>' if sub else ""
    return f"""  <div class="bolha-grupo">
    <h4>{e(titulo)}</h4>
    {sub_html}
    <div class="bolha">{{{{{numero}.{bid}.a}}}}</div>
    <div class="bolha" style="background:var(--color-neutral-subtle);">{{{{{numero}.{bid}.b}}}}</div>
    <div class="nota-conducao">{{{{{numero}.{bid}.nota}}}}</div>
  </div>"""


def render_secao_7_outbound(d: dict) -> str:  # noqa: ARG001
    """Seção 4. Outbound. 7 blocos × 2 variações + nota cada."""
    blocos = [
        ("b1", "1. Primeiro contato", "Quebra-gelo + motivo de ter escrito. Sem vender."),
        ("b2", "2. Qualificação leve", "1 ou 2 perguntas curtas sobre o momento atual do lead."),
        ("b3", "3. Amarrar a dor", "Urgência Oculta relevante em forma de pergunta aberta."),
        ("b4", "4. Oferecer ajuda concreta", "Conteúdo, troca ou resposta a dúvida específica. Sem vender."),
        ("b5", "5. Convite para conversa real", "Chamar pra falar do problema específico dele."),
        ("b6", "6. Transição para diagnóstico", "Quando o lead engajou, entra no SPIN curto."),
        ("b7", "7. Encerramento se não engajou", "Fechar educadamente e marcar para follow-up."),
    ]
    blocos_html = "\n".join(_bloco_variacoes(4, bid, titulo, sub) for bid, titulo, sub in blocos)
    return f"""<section id="secao-4">
  <h2>4. Abordagem Ativa · Outbound WhatsApp</h2>
  <!-- CREATIVE_4_START -->
  <div class="card" style="background:var(--color-informative-subtle);border-left:3px solid var(--color-informative);">
    <strong>Outbound = lead tem perfil (good fit), mas ainda não tem dor consciente.</strong>
    Referência: Mark Roberge (fase Has pain × Good fit). Por isso a abordagem começa leve, sem vender. O trabalho do vendedor é levar o lead a perceber a própria dor. Pressão cedo queima o contato.
  </div>
  <p style="font-size:13px;color:var(--color-detail);">Em cada bloco: mensagem <strong>leve</strong> (cinza-azulada) e mensagem <strong>direta</strong> (cinza). Use a que couber no tom da conversa.</p>
{blocos_html}
  <!-- CREATIVE_4_END -->
</section>
"""


def render_secao_8_inbound(d: dict) -> str:  # noqa: ARG001
    """Seção 5. Inbound. 6 blocos × 2 variações + nota cada."""
    blocos = [
        ("b1", "1. Acolhimento imediato", "Resposta rápida, chama pelo nome, confirma o interesse."),
        ("b2", "2. Pergunta de posicionamento", "O que viu, por que chegou, o que já tentou."),
        ("b3", "3. Diagnóstico rápido", "3 a 5 perguntas no estilo SPIN adaptado."),
        ("b4", "4. Apresentação conectada", "Amarra à resposta do lead, usa as palavras dele."),
        ("b5", "5. Prova + preço", "1 caso real + revelação de valor no tom certo."),
        ("b6", "6. Checkout + confirmação", "Envia link e pede confirmação com pressuposto do sim."),
    ]
    blocos_html = "\n".join(_bloco_variacoes(5, bid, titulo, sub) for bid, titulo, sub in blocos)
    return f"""<section id="secao-5">
  <h2>5. Abordagem Receptiva · Inbound WhatsApp</h2>
  <!-- CREATIVE_5_START -->
  <div class="card" style="background:var(--color-positive-subtle);border-left:3px solid var(--color-positive);">
    <strong>Inbound = lead já tem dor consciente, mas ainda não sabe se é good fit.</strong>
    Por isso a abordagem pode ir direto ao diagnóstico, sem rodeios. O trabalho do vendedor é qualificar rápido e mostrar que o método encaixa com o perfil dele. Referência: Mark Roberge. Aquecer demais aqui queima a intenção.
  </div>
  <p style="font-size:13px;color:var(--color-detail);">Em cada bloco: mensagem <strong>leve</strong> e mensagem <strong>direta</strong>. Use a que couber no tom.</p>
{blocos_html}
  <!-- CREATIVE_5_END -->
</section>
"""


def render_secao_9_spin(d: dict) -> str:  # noqa: ARG001
    """Seção 6. SPIN. 4 fases × 3 perguntas + 1 nota cada."""
    fases = [
        ("S", "S. Situação", "Cenário atual: rotina, ferramentas, tentativas anteriores, momento de vida."),
        ("P", "P. Problema", "Dor central trazida à tona com vocabulário do consumidor."),
        ("I", "I. Implicação", "Custo de não resolver: financeiro, emocional, tempo, reputação, saúde."),
        ("N", "N. Necessidade", "Visão do resultado ideal conectada ao Quadro."),
    ]
    fases_html = []
    for fid, titulo, sub in fases:
        fases_html.append(f"""  <div class="bolha-grupo">
    <h4>{e(titulo)}</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">{e(sub)}</p>
    <div class="bolha">{{{{6.{fid}.q1}}}}</div>
    <div class="bolha">{{{{6.{fid}.q2}}}}</div>
    <div class="bolha">{{{{6.{fid}.q3}}}}</div>
    <div class="nota-conducao">{{{{6.{fid}.nota}}}}</div>
  </div>""")
    return f"""<section id="secao-6">
  <h2>6. SPIN adaptado ao WhatsApp</h2>
  <!-- CREATIVE_6_START -->
  <p>12 perguntas no total: 3 por fase. Todas personalizadas ao Quadro, à dor central e ao vocabulário do consumidor. Avance de fase quando o lead sinalizar consciência crescente.</p>
{"".join(fases_html)}
  <!-- CREATIVE_6_END -->
</section>
"""


def render_secao_10_preco(d: dict) -> str:
    """Seção 7. Apresentação + ancoragem de preço. Blocos temáticos com mensagens fixas."""
    preco = d.get("preco_texto", "o valor da oferta")
    return f"""<section id="secao-7">
  <h2>7. Apresentação e ancoragem de preço por texto</h2>
  <!-- CREATIVE_7_START -->
  <p>Sequência pronta para copiar e colar. Os colchetes marcam onde colar a palavra que o próprio lead usou. Ajuste o tom, nunca o núcleo.</p>

  <div class="bolha-grupo">
    <h4>Ponte dor-solução</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">2 mensagens que amarram a dor descrita ao método, com as palavras do lead.</p>
    <div class="bolha">{{{{7.ponte.a}}}}</div>
    <div class="bolha">{{{{7.ponte.b}}}}</div>
  </div>

  <div class="bolha-grupo">
    <h4>Descrição objetiva</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">O que é, como funciona e como a Furadeira entrega o Quadro semana a semana.</p>
    <div class="bolha">{{{{7.desc.a}}}}</div>
    <div class="bolha">{{{{7.desc.b}}}}</div>
    <div class="bolha">{{{{7.desc.c}}}}</div>
    <div class="bolha">{{{{7.desc.d}}}}</div>
  </div>

  <div class="bolha-grupo">
    <h4>Provas curtas</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">Um caso real (nome fictício), um número agregado, um depoimento de 1 linha.</p>
    <div class="bolha">{{{{7.prova.a}}}}</div>
    <div class="bolha">{{{{7.prova.b}}}}</div>
    <div class="bolha">{{{{7.prova.c}}}}</div>
  </div>

  <div class="bolha-grupo">
    <h4>Conexão Furadeira → Quadro</h4>
    <div class="bolha">{{{{7.conexao}}}}</div>
  </div>

  <div class="bolha-grupo">
    <h4>Revelação de preço em 4 tempos</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">Alta (valor total somado) → funcional (custo de a dor continuar) → preço real ({e(preco)}) → confirmação.</p>
    <div class="bolha">{{{{7.preco.alta}}}}</div>
    <div class="bolha">{{{{7.preco.funcional}}}}</div>
    <div class="bolha">{{{{7.preco.real}}}}</div>
    <div class="bolha">{{{{7.preco.confirm}}}}</div>
  </div>

  <div class="bolha-grupo">
    <h4>Comparação com paliativos</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">Confronta o que o lead já tentou com o que o método entrega.</p>
    <div class="bolha">{{{{7.paliativo.a}}}}</div>
    <div class="bolha">{{{{7.paliativo.b}}}}</div>
  </div>
  <!-- CREATIVE_7_END -->
</section>
"""


def render_secao_13_recuperacao(d: dict) -> str:  # noqa: ARG001
    """Seção 10. Recuperação de carrinho. 5 toques × 2 variações com badges de tempo."""
    toques = [
        ("t1", "15 min", "15 min após abandono", "Tom de ajuda. 'Tudo certo com a finalização?'"),
        ("t2", "1 hora", "1 hora depois", "Quebra da primeira objeção provável (preço ou segurança)."),
        ("t3", "D+1", "D+1 manhã", "Nova angulação usando Urgência Oculta diferente."),
        ("t4", "D+3", "D+3", "Última chamada educada. Foco em consequência de adiar."),
        ("t5", "D+7", "D+7", "Encerramento respeitoso + oferta de downsell se houver."),
    ]
    toques_html = []
    for tid, badge, titulo, sub in toques:
        toques_html.append(f"""  <div class="bolha-grupo">
    <span class="badge-tempo">{e(badge)}</span>
    <h4 style="margin-top:4px;">{e(titulo)}</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">{e(sub)}</p>
    <div class="bolha">{{{{10.{tid}.a}}}}</div>
    <div class="bolha" style="background:var(--color-neutral-subtle);">{{{{10.{tid}.b}}}}</div>
  </div>""")
    return f"""<section id="secao-10">
  <h2>10. Recuperação de Carrinho</h2>
  <!-- CREATIVE_10_START -->
  <p>Timeline de 5 toques. Cada toque traz 2 variações: mensagem <strong>leve</strong> (azul-claro) e mensagem <strong>direta</strong> (cinza). Escolha pelo tom do lead.</p>
{"".join(toques_html)}
  <!-- CREATIVE_10_END -->
</section>
"""


def render_secao_14_follow_up(d: dict) -> str:  # noqa: ARG001
    """Seção 11. Follow-up + Upsell + Downsell + Order bump."""
    tempos = [
        ("d1", "D+1", "Lembrete leve + prova social curta."),
        ("d3", "D+3", "Nova angulação com Urgência Oculta diferente + quebra de 1 objeção."),
        ("d7", "D+7", "Última chamada com escassez real + oferta de downsell se houver."),
    ]
    follow_html = []
    for tid, titulo, sub in tempos:
        follow_html.append(f"""  <div class="bolha-grupo">
    <h4>{e(titulo)}</h4>
    <p style="font-size:12px;color:var(--color-detail);margin:0 0 8px 0;">{e(sub)}</p>
    <div class="bolha">{{{{11.fu.{tid}.a}}}}</div>
    <div class="bolha" style="background:var(--color-neutral-subtle);">{{{{11.fu.{tid}.b}}}}</div>
  </div>""")

    return f"""<section id="secao-11">
  <h2>11. Follow-up, Upsell, Downsell, Order Bump</h2>
  <!-- CREATIVE_11_START -->

  <h3>Follow-up de quem não fechou</h3>
  <p>Para leads que conversaram mas não chegaram ao checkout. 3 toques com 2 mensagens cada.</p>
{"".join(follow_html)}

  <h3>Upsell</h3>
  <p>Oferta complementar pós-compra. Enviada em até 48h pelo WhatsApp.</p>
  <div class="card">
    <p><strong>Oferta:</strong> {{{{11.upsell.oferta}}}}</p>
    <div class="bolha">{{{{11.upsell.frase}}}}</div>
  </div>

  <h3>Downsell</h3>
  <p>Para quem recusou preço ou não fechou. Enviado no D+7 ou após recusa explícita.</p>
  <div class="card">
    <p><strong>Oferta:</strong> {{{{11.downsell.oferta}}}}</p>
    <div class="bolha">{{{{11.downsell.frase}}}}</div>
  </div>

  <h3>Order bump</h3>
  <p>Complemento dentro do próprio checkout. Impulso de 1 clique, preço baixo.</p>
  <div class="card">
    <p><strong>Oferta:</strong> {{{{11.bump.oferta}}}}</p>
    <div class="bolha">{{{{11.bump.frase}}}}</div>
  </div>
  <!-- CREATIVE_11_END -->
</section>
"""
