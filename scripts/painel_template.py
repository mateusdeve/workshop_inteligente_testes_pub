"""
painel_template.py

Shell HTML e funcoes de render das secoes do painel de entregas incremental.

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
from typing import Iterable

# ----- metadados das secoes -----

# Ordem importa: define a ordem na sidebar e na barra mobile.
SECOES: list[dict] = [
    {"id": "visao-geral", "grupo": "PRODUTO", "titulo": "Visao Geral",
     "subtitulo": "Resumo do produto e informacoes principais."},
    {"id": "quadro", "grupo": "PRODUTO", "titulo": "Quadro",
     "subtitulo": "A transformacao principal que o produto entrega ao cliente.",
     "proxima": "Quadro sera preenchido ao concluir o Bloco 1 de /produto-concepcao."},
    {"id": "furadeira", "grupo": "PRODUTO", "titulo": "Furadeira",
     "subtitulo": "O metodo estruturado que torna visivel a eficiencia do produto.",
     "proxima": "Furadeira sera preenchida ao concluir o Bloco 2 de /produto-concepcao."},
    {"id": "decorados", "grupo": "PRODUTO", "titulo": "Decorados",
     "subtitulo": "50 beneficios derivados do Quadro.",
     "proxima": "Decorados serao preenchidos ao concluir o Bloco 4 de /produto-concepcao."},
    {"id": "urgencias", "grupo": "PRODUTO", "titulo": "Urgencias Ocultas",
     "subtitulo": "70 itens em 7 categorias.",
     "proxima": "Urgencias serao preenchidas ao concluir o Bloco 5 de /produto-concepcao."},
    {"id": "identidade-produto", "grupo": "IDENTIDADES", "titulo": "Identidade do Produto",
     "subtitulo": "Como o produto se posiciona e se diferencia no mercado.",
     "proxima": "Sera preenchida ao concluir o Bloco 3 de /produto-concepcao."},
    {"id": "identidade-consumidor", "grupo": "IDENTIDADES", "titulo": "Identidade do Consumidor",
     "subtitulo": "Perfil detalhado do cliente ideal.",
     "proxima": "Sera preenchida automaticamente no Passo 4C de /produto-concepcao."},
    {"id": "identidade-comunicador", "grupo": "IDENTIDADES", "titulo": "Identidade do Comunicador",
     "subtitulo": "Tom, posicionamento e linguagem do criador.",
     "proxima": "Sera preenchida ao concluir o Bloco 3B de /produto-concepcao."},
    {"id": "pesquisa", "grupo": "PESQUISA", "titulo": "Pesquisa de Mercado",
     "subtitulo": "Inteligencia de mercado. Use para argumentos, copy e posicionamento.",
     "proxima": "Sera preenchida ao final de /produto-novo (Ramo 2) ou do Bloco 3 de /produto-concepcao."},
]

SECOES_RENDERIZAVEIS = {
    s["id"] for s in SECOES if s["id"] != "visao-geral"
}

# ----- shell HTML -----

_CSS_TOKENS = """\
:root {
  --sidebar-bg: #ffffff;
  --sidebar-border: #e5e7eb;
  --main-bg: #f8f9fb;
  --surface: #ffffff;
  --primary: #22c55e;
  --primary-dark: #16a34a;
  --primary-light: #dcfce7;
  --highlight-bg: #f0fdf4;
  --highlight-border: #bbf7d0;
  --text-1: #111827;
  --text-2: #374151;
  --text-3: #6b7280;
  --border: #e5e7eb;
  --border-2: #f3f4f6;
  --badge-green-bg: #dcfce7; --badge-green-text: #16a34a;
  --badge-blue-bg: #dbeafe; --badge-blue-text: #1d4ed8;
  --badge-indigo-bg: #e0e7ff; --badge-indigo-text: #4338ca;
  --badge-purple-bg: #ede9fe; --badge-purple-text: #7c3aed;
  --badge-violet-bg: #f3e8ff; --badge-violet-text: #9333ea;
  --badge-pink-bg: #fce7f3; --badge-pink-text: #db2777;
  --badge-orange-bg: #fef3c7; --badge-orange-text: #d97706;
  --badge-dark-bg: #1f2937; --badge-dark-text: #ffffff;
  --badge-neutral-bg: #f3f4f6; --badge-neutral-text: #374151;
  --sidebar-w: 220px;
  --r: 10px; --r2: 8px;
  --sh1: 0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04);
  --sh2: 0 4px 16px rgba(0,0,0,.08), 0 1px 4px rgba(0,0,0,.04);
}"""

_CSS_BASE = """\
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',sans-serif;background:var(--main-bg);color:var(--text-1)}

/* SIDEBAR */
.sidebar{position:fixed;top:0;left:0;width:var(--sidebar-w);height:100vh;background:var(--sidebar-bg);border-right:1px solid var(--sidebar-border);overflow-y:auto;padding:24px 0;z-index:100}
.sidebar-title{font-size:14px;font-weight:700;color:var(--text-1);padding:0 20px;margin-bottom:4px}
.sidebar-product{font-size:11px;color:var(--text-3);padding:0 20px;margin-bottom:24px;line-height:1.4}
.nav-group{font-size:10px;font-weight:700;color:var(--text-3);text-transform:uppercase;letter-spacing:1px;padding:0 20px;margin:16px 0 4px}
.nav-item{display:block;padding:7px 20px;font-size:13px;color:var(--text-2);text-decoration:none;border-left:3px solid transparent;cursor:pointer}
.nav-item:hover{color:var(--primary-dark)}
.nav-item.active{color:var(--primary-dark);font-weight:600;border-left:3px solid var(--primary)}
.sidebar-export{position:fixed;bottom:20px;left:0;width:var(--sidebar-w);padding:0 20px}
.btn-export{display:block;width:100%;background:var(--primary);color:#fff;border:none;border-radius:var(--r2);padding:10px 0;font-size:13px;font-weight:600;text-align:center;cursor:pointer}
.btn-export:hover{background:var(--primary-dark)}

/* MOBILE TABS */
.mobile-tabs{display:none;position:sticky;top:0;z-index:99;background:var(--surface);border-bottom:1px solid var(--border);overflow-x:auto;white-space:nowrap}
.mobile-tab{display:inline-block;padding:10px 16px;font-size:13px;color:var(--text-3);cursor:pointer;border-bottom:2px solid transparent}
.mobile-tab.active{color:var(--primary-dark);font-weight:600;border-bottom:2px solid var(--primary)}

/* MAIN */
.main{margin-left:var(--sidebar-w);min-height:100vh;padding:32px 40px}
.breadcrumb{font-size:13px;color:var(--text-3);margin-bottom:8px}
.section-title{font-size:26px;font-weight:700;color:var(--text-1);margin-bottom:4px}
.section-sub{font-size:13px;color:var(--text-3);margin-bottom:24px}
.panel{display:none;animation:fadeIn .2s ease}
.panel.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:translateY(0)}}

/* CARDS */
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:24px;box-shadow:var(--sh1)}
.card:hover{box-shadow:var(--sh2);transition:box-shadow .2s}
.card-label{font-size:11px;font-weight:700;color:var(--text-3);text-transform:uppercase;letter-spacing:.8px;margin-bottom:8px}
.card-value{font-size:15px;font-weight:600;color:var(--text-1)}
.card-sub{font-size:13px;color:var(--text-3);margin-top:4px}
.card-highlight{background:var(--highlight-bg);border:1px solid var(--highlight-border);border-radius:var(--r);padding:20px 24px}
.card-highlight .card-label{color:var(--primary)}
.card-highlight .card-value{font-size:18px;font-weight:700;color:var(--primary-dark);line-height:1.4}

/* GRIDS */
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}

/* DIVIDER */
.divider{height:1px;background:var(--border);margin:24px 0}

/* BADGES */
.badge{border-radius:9999px;font-size:11px;font-weight:700;padding:3px 10px;white-space:nowrap;display:inline-block}
.badge-green{background:var(--badge-green-bg);color:var(--badge-green-text)}
.badge-blue{background:var(--badge-blue-bg);color:var(--badge-blue-text)}
.badge-indigo{background:var(--badge-indigo-bg);color:var(--badge-indigo-text)}
.badge-purple{background:var(--badge-purple-bg);color:var(--badge-purple-text)}
.badge-violet{background:var(--badge-violet-bg);color:var(--badge-violet-text)}
.badge-pink{background:var(--badge-pink-bg);color:var(--badge-pink-text)}
.badge-orange{background:var(--badge-orange-bg);color:var(--badge-orange-text)}
.badge-dark{background:var(--badge-dark-bg);color:var(--badge-dark-text)}
.badge-neutral{background:var(--badge-neutral-bg);color:var(--badge-neutral-text)}

/* STATUS CARD */
.status-card{display:flex;align-items:center;flex-wrap:wrap;gap:10px;font-size:13px;color:var(--text-2)}
.status-dot{width:8px;height:8px;border-radius:50%;background:var(--primary);display:inline-block;margin-right:6px}
.status-sep{color:var(--text-3);margin:0 4px}

/* TIMELINE (Furadeira) */
.timeline{list-style:none}
.timeline-item{display:flex;gap:16px;padding-bottom:20px;position:relative}
.timeline-item:last-child{padding-bottom:0}
.timeline-item:not(:last-child)::before{content:'';position:absolute;left:15px;top:32px;bottom:0;width:2px;background:var(--primary-light)}
.tl-num{width:32px;height:32px;border-radius:50%;background:var(--primary);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.tl-body{flex:1;padding-top:4px}
.tl-title{font-size:15px;font-weight:600;color:var(--text-1);margin-bottom:4px}
.tl-desc{font-size:13px;color:var(--text-3);line-height:1.6}

/* ACCORDION */
.accordion{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);margin-bottom:8px;box-shadow:var(--sh1);overflow:hidden}
.accordion-header{display:flex;align-items:center;gap:12px;padding:14px 20px;cursor:pointer;user-select:none}
.accordion-label{font-size:14px;color:var(--text-1);font-weight:500;flex:1}
.accordion-arrow{color:var(--text-3);font-size:12px;transition:transform .2s;margin-left:auto}
.accordion.open .accordion-arrow{transform:rotate(180deg)}
.accordion-body{max-height:0;overflow:hidden;transition:max-height .3s cubic-bezier(.4,0,.2,1)}
.accordion.open .accordion-body{max-height:6000px}
.accordion-list{padding:0 20px 16px;list-style:none}
.accordion-list li{font-size:13px;color:var(--text-2);line-height:1.7;padding-left:14px;position:relative}
.accordion-list li::before{content:'•';color:var(--primary);position:absolute;left:0;font-weight:700}

/* BTN PRIMARY */
.btn-primary{background:var(--primary);color:#fff;border:none;border-radius:var(--r2);padding:9px 20px;font-size:13px;font-weight:600;display:inline-flex;align-items:center;gap:6px;cursor:pointer;text-decoration:none;margin-top:16px}
.btn-primary:hover{background:var(--primary-dark)}

/* BULLET LIST */
.bullet-list{list-style:none;padding:0}
.bullet-list li{font-size:13px;color:var(--text-2);line-height:1.7;padding-left:16px;position:relative;margin-bottom:4px}
.bullet-list li::before{content:'•';color:var(--primary);position:absolute;left:0;font-weight:700}

/* PILL CLOUD */
.pill-cloud,.flex-wrap{display:flex;flex-wrap:wrap;gap:6px}

/* TABLE */
.table-wrap{overflow-x:auto}
table,.table{width:100%;border-collapse:collapse}
th{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:var(--text-3);font-weight:700;padding:10px 12px;text-align:left}
td{font-size:13px;color:var(--text-2);padding:10px 12px}
tr{border-bottom:1px solid var(--border-2)}

/* KPI */
.kpi{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:20px;box-shadow:var(--sh1)}
.kpi-label{font-size:11px;font-weight:700;color:var(--text-3);text-transform:uppercase;letter-spacing:.8px}
.kpi-value{font-size:24px;font-weight:800;color:var(--text-1);margin-top:6px}
.kpi-sub{font-size:12px;color:var(--text-3);margin-top:4px}
.kpi-trend{font-size:12px;font-weight:600;display:flex;align-items:center;gap:4px;margin-top:4px}
.trend-up{color:#16a34a}
.trend-neutral{color:var(--text-3)}

/* ARGUMENTO BLOCKS */
.arg-block{margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid var(--border-2)}
.arg-block:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0}
.arg-title{font-size:13px;font-weight:700;color:var(--text-1);text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px}
.arg-block p{font-size:13px;color:var(--text-2);line-height:1.7;margin-bottom:8px}
.arg-block p:last-child{margin-bottom:0}

/* PARA */
.para{font-size:13px;color:var(--text-2);line-height:1.7;margin-top:6px}

/* COMPLAINT BARS */
.complaint-row{margin-bottom:10px}
.complaint-label{font-size:13px;color:var(--text-2);margin-bottom:4px;display:flex;justify-content:space-between}
.complaint-bar-bg{height:6px;background:var(--border-2);border-radius:3px}
.complaint-bar-fill{height:6px;background:var(--primary);border-radius:3px}

/* OPP LIST */
.opp-list{list-style:none}
.opp-item{display:flex;gap:14px;align-items:flex-start;padding:12px 0;border-bottom:1px solid var(--border-2)}
.opp-item:last-child{border-bottom:none}
.opp-num{width:28px;height:28px;border-radius:50%;background:var(--primary-light);color:var(--primary-dark);font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.opp-text{font-size:14px;color:var(--text-2);line-height:1.6}

/* ALERT CARD */
.alert-card{background:#fffbeb;border:1px solid #fde68a;border-radius:var(--r);padding:20px 24px}
.alert-title{font-size:11px;font-weight:700;color:#d97706;text-transform:uppercase;letter-spacing:.8px;margin-bottom:12px}

/* STACK */
.stack{display:flex;flex-direction:column;gap:16px}
.stack-sm{display:flex;flex-direction:column;gap:8px}

/* PLACEHOLDER */
.placeholder{padding:40px;text-align:center;background:var(--surface);border:1px dashed var(--border);border-radius:var(--r);color:var(--text-3)}
.placeholder-title{font-size:15px;font-weight:600;color:var(--text-2);margin-bottom:6px}
.placeholder-sub{font-size:13px;color:var(--text-3)}

@media(max-width:768px){
  .sidebar{display:none}
  .mobile-tabs{display:block}
  .main{margin-left:0;padding:20px 16px}
  .grid-3,.grid-2,.grid-4{grid-template-columns:1fr}
}
@media print{
  .sidebar,.mobile-tabs,.sidebar-export{display:none}
  .main{margin-left:0;padding:16px}
  .panel{display:block!important}
  .accordion-body{max-height:none!important;overflow:visible!important}
  .accordion-arrow{display:none}
}"""

_JS = """\
function showPanel(id) {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  document.querySelectorAll('.mobile-tab').forEach(t => t.classList.remove('active'));
  const panel = document.getElementById('panel-' + id);
  if (panel) panel.classList.add('active');
  document.querySelectorAll('.nav-item, .mobile-tab').forEach(el => {
    const oc = el.getAttribute('onclick') || '';
    if (oc.includes("'" + id + "'")) el.classList.add('active');
  });
}
function toggleAccordion(header) {
  header.closest('.accordion').classList.toggle('open');
}
document.addEventListener('DOMContentLoaded', () => showPanel('visao-geral'));"""


def _escape(value: str | None) -> str:
    if not value:
        return ""
    return html.escape(str(value), quote=True)


def _placeholder(proxima: str) -> str:
    return (
        '<div class="placeholder">'
        '<div class="placeholder-title">Em breve</div>'
        f'<div class="placeholder-sub">{_escape(proxima)}</div>'
        "</div>"
    )


def _sidebar_items() -> str:
    partes: list[str] = []
    grupo_atual = None
    for secao in SECOES:
        if secao["grupo"] != grupo_atual:
            grupo_atual = secao["grupo"]
            partes.append(f'<div class="nav-group">{grupo_atual}</div>')
        sid = secao["id"]
        partes.append(
            f'<span class="nav-item" onclick="showPanel(\'{sid}\')">'
            f'{_escape(secao["titulo"])}</span>'
        )
    return "\n".join(partes)


def _mobile_tabs() -> str:
    return "\n".join(
        f'<span class="mobile-tab" onclick="showPanel(\'{s["id"]}\')">'
        f'{_escape(s["titulo"])}</span>'
        for s in SECOES
    )


def _panels_placeholder(nome_produto: str) -> str:
    """Gera todos os paineis vazios. O render_* substitui secao por secao depois."""
    partes: list[str] = []
    for secao in SECOES:
        if secao["id"] == "visao-geral":
            conteudo = render_visao_geral({"nome_produto": nome_produto, "secoes_prontas": []})
        else:
            conteudo = (
                f'<!-- SECTION:{secao["id"]} -->\n'
                + _placeholder(secao.get("proxima", "Em breve."))
                + f'\n<!-- /SECTION:{secao["id"]} -->'
            )
        partes.append(
            f'<div class="panel" id="panel-{secao["id"]}">'
            f'<div class="breadcrumb">Painel de Entregas &rsaquo; {_escape(secao["titulo"])}</div>'
            f'<div class="section-title">{_escape(secao["titulo"])}</div>'
            f'<div class="section-sub">{_escape(secao["subtitulo"])}</div>'
            f'{conteudo}'
            "</div>"
        )
    return "\n".join(partes)


def build_shell(nome_produto: str) -> str:
    """Gera o HTML completo inicial com todos os placeholders."""
    painel_list = _panels_placeholder(nome_produto)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Painel de Entregas</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{_CSS_TOKENS}
{_CSS_BASE}
</style>
</head>
<body>
<nav class="sidebar">
  <div class="sidebar-title">Painel de Entregas</div>
  <div class="sidebar-product">{_escape(nome_produto)}</div>
  {_sidebar_items()}
  <div class="sidebar-export"><button class="btn-export" onclick="window.print()">Exportar PDF (Ctrl+P)</button></div>
</nav>
<div class="mobile-tabs">{_mobile_tabs()}</div>
<main class="main">
{painel_list}
</main>
<script>
{_JS}
</script>
</body>
</html>
"""


# ----- helpers de render -----

def _card(label: str, valor: str, sub: str = "", highlight: bool = False) -> str:
    cls = "card-highlight" if highlight else "card"
    sub_html = f'<div class="card-sub">{_escape(sub)}</div>' if sub else ""
    return (
        f'<div class="{cls}">'
        f'<div class="card-label">{_escape(label)}</div>'
        f'<div class="card-value">{_escape(valor) or "&mdash;"}</div>'
        f"{sub_html}"
        "</div>"
    )


def _ul(items: Iterable[str]) -> str:
    lis = "".join(f"<li>{_escape(i)}</li>" for i in items if i)
    if not lis:
        return '<div class="card-sub">Ainda sem itens.</div>'
    return f'<ul class="bullet-list">{lis}</ul>'


def _accordion(badge_cls: str, badge_txt: str, descricao: str, items: list[str]) -> str:
    lis = "".join(f"<li>{_escape(i)}</li>" for i in items)
    return (
        '<div class="accordion">'
        '<div class="accordion-header" onclick="toggleAccordion(this)">'
        f'<span class="badge {badge_cls}">{_escape(badge_txt)}</span>'
        f'<span class="accordion-label">{_escape(descricao)}</span>'
        '<span class="accordion-arrow">&#9662;</span>'
        "</div>"
        '<div class="accordion-body">'
        f'<ul class="accordion-list">{lis}</ul>'
        "</div>"
        "</div>"
    )


def _pills(items: Iterable[str], cls: str = "badge-neutral") -> str:
    pills = "".join(
        f'<span class="badge {cls}">{_escape(i)}</span>' for i in items if i
    )
    return f'<div class="pill-cloud">{pills}</div>' if pills else '<div class="card-sub">&mdash;</div>'


# ----- renders por secao -----

def render_visao_geral(dados: dict) -> str:
    """Visao geral: cards com nome, tipo, preco + quadro em destaque + status."""
    nome = dados.get("nome_produto") or "(sem nome)"
    tipo = dados.get("tipo") or "a definir"
    preco = dados.get("preco") or "a definir"
    quadro = dados.get("quadro") or "Quadro ainda nao definido."
    nicho = dados.get("nicho") or "a definir"
    diferencial = dados.get("diferencial") or "a definir"
    secoes_prontas: list[str] = dados.get("secoes_prontas") or []

    badges = "".join(
        f'<span class="badge badge-green">{_escape(s)}</span>'
        for s in secoes_prontas
    )

    grid1 = (
        f'<div class="grid-3" style="margin-bottom:16px">'
        f'{_card("Nome do produto", nome)}'
        f'{_card("Tipo", tipo)}'
        f'{_card("Preco", preco)}'
        "</div>"
    )
    quadro_box = (
        '<div class="card-highlight" style="margin-bottom:16px">'
        '<div class="card-label">Quadro — Transformacao Principal</div>'
        f'<div class="card-value">{_escape(quadro)}</div>'
        "</div>"
    )
    grid2 = (
        '<div class="grid-2" style="margin-bottom:16px">'
        f'{_card("Nicho", nicho)}'
        f'{_card("Diferencial", diferencial)}'
        "</div>"
    )

    status_extras = ""
    if tipo and tipo != "a definir":
        status_extras += f'<span class="status-sep">·</span><span>{_escape(tipo)}</span>'
    if preco and preco != "a definir":
        status_extras += f'<span class="status-sep">·</span><span>{_escape(preco)}</span>'
    if badges:
        status_extras += f'<span class="status-sep">·</span>{badges}'

    status = (
        '<div class="card">'
        '<div class="status-card">'
        '<span><span class="status-dot"></span><strong>Produto ativo</strong></span>'
        + status_extras
        + "</div></div>"
    )
    return (
        f'<!-- SECTION:visao-geral -->\n{grid1}{quadro_box}{grid2}{status}\n<!-- /SECTION:visao-geral -->'
    )


def render_quadro(dados: dict) -> str:
    quadro = dados.get("quadro") or ""
    if not quadro:
        miolo = _placeholder("Aguardando Quadro do Bloco 1.")
    else:
        como_usar = (
            "O Quadro aparece na headline da pagina de vendas, na primeira linha de emails, "
            "nos ganchos de anuncios e no primeiro slide de carrosseis."
        )
        regra = (
            "Teste: a pessoa pode dizer que isso aconteceu na vida dela ao final do produto? "
            "Se nao, o Quadro ainda esta descrevendo processo, nao resultado."
        )
        miolo = (
            '<div class="card-highlight" style="margin-bottom:16px">'
            '<div class="card-label">Quadro Aprovado</div>'
            f'<div class="card-value">{_escape(quadro)}</div>'
            "</div>"
            + '<div class="grid-2">'
            + _card("Como Usar o Quadro", como_usar)
            + _card("Regra do Quadro", regra)
            + "</div>"
        )
    return f"<!-- SECTION:quadro -->\n{miolo}\n<!-- /SECTION:quadro -->"


def render_furadeira(dados: dict) -> str:
    nome_metodo = dados.get("nome_metodo") or ""
    macroetapas: list[dict] = dados.get("macroetapas") or []
    furadeira_html = dados.get("furadeira_html") or ""

    if not nome_metodo and not macroetapas:
        miolo = _placeholder("Aguardando Furadeira do Bloco 2.")
    else:
        steps_html = ""
        for idx, m in enumerate(macroetapas, start=1):
            titulo = m.get("titulo") or f"Etapa {idx}"
            desc = m.get("descricao") or ""
            steps_html += (
                '<li class="timeline-item">'
                f'<div class="tl-num">{idx}</div>'
                '<div class="tl-body">'
                f'<div class="tl-title">{_escape(titulo)}</div>'
                f'<div class="tl-desc">{_escape(desc)}</div>'
                "</div>"
                "</li>"
            )
        if not steps_html:
            steps_html = (
                '<li class="tl-desc">Nenhuma macroetapa registrada ainda.</li>'
            )
        link_trilha = ""
        if furadeira_html:
            link_trilha = (
                f'<a class="btn-primary" href="{_escape(furadeira_html)}" target="_blank">'
                'Ver Trilha Visual Completa &#8594;</a>'
            )
        miolo = (
            _card("Nome do Metodo", nome_metodo or "(sem nome)")
            + '<div class="card" style="margin-top:16px">'
            '<div class="card-label">Trilha do Metodo</div>'
            f'<ul class="timeline" style="margin-top:16px">{steps_html}</ul>'
            f"{link_trilha}"
            "</div>"
        )
    return f"<!-- SECTION:furadeira -->\n{miolo}\n<!-- /SECTION:furadeira -->"


_DECORADOS_CATEGORIAS = [
    ("Financeiro", "badge-green"),
    ("Tempo", "badge-blue"),
    ("Autoestima", "badge-purple"),
    ("Reputacao", "badge-orange"),
    ("Crescimento", "badge-dark"),
]


def render_decorados(dados: dict) -> str:
    categorias: dict[str, list[str]] = dados.get("decorados") or {}
    total = sum(len(v) for v in categorias.values())
    if total == 0:
        miolo = _placeholder("Aguardando Decorados do Bloco 4.")
    else:
        partes = []
        for nome, badge in _DECORADOS_CATEGORIAS:
            itens = categorias.get(nome) or categorias.get(nome.lower()) or []
            partes.append(
                _accordion(badge, nome, f"{len(itens)} beneficios", itens)
            )
        miolo = "".join(partes)
    return f"<!-- SECTION:decorados -->\n{miolo}\n<!-- /SECTION:decorados -->"


_URGENCIAS_CATEGORIAS = [
    ("Dores", "badge-pink", "O que incomoda"),
    ("Duvidas", "badge-indigo", "O que pergunta"),
    ("Desejos", "badge-violet", "O que sonha"),
    ("Assuntos Relacionados", "badge-green", "Porta de entrada"),
    ("Urgencias Quentes", "badge-orange", "Alta intencao"),
    ("Urgencias Frias", "badge-neutral", "Alto volume"),
    ("Urgencias Inusitadas", "badge-purple", "Angulos inesperados"),
]


def render_urgencias(dados: dict) -> str:
    categorias: dict[str, list[str]] = dados.get("urgencias") or {}
    total = sum(len(v) for v in categorias.values())
    if total == 0:
        miolo = _placeholder("Aguardando Urgencias Ocultas do Bloco 5.")
    else:
        partes = []
        for nome, badge, desc in _URGENCIAS_CATEGORIAS:
            itens = (
                categorias.get(nome)
                or categorias.get(nome.lower())
                or []
            )
            partes.append(
                _accordion(badge, nome, f"{desc} \u00b7 {len(itens)} itens", itens)
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
        '<div class="grid-2">'
        + _card("Diferencial principal", diferencial or "a definir")
        + _card("Formato", formato or "a definir")
        + "</div>"
    )
    args_card = (
        '<div class="card" style="margin-top:16px">'
        '<div class="card-label">Argumentos incontestaveis</div>'
        + _ul(argumentos)
        + "</div>"
    )
    objecoes_html = ""
    if objecoes:
        acc_items = []
        for idx, obj in enumerate(objecoes, start=1):
            corpo_args = ""
            for arg in obj.get("argumentos", []):
                paragrafos = "".join(
                    f"<p>{_escape(p)}</p>" for p in arg.get("paragrafos", []) if p
                )
                corpo_args += (
                    '<div class="arg-block">'
                    f'<div class="arg-title">{_escape(arg.get("titulo",""))}</div>'
                    f"{paragrafos}"
                    "</div>"
                )
            acc_items.append(
                '<div class="accordion">'
                '<div class="accordion-header" onclick="toggleAccordion(this)">'
                f'<span class="badge badge-pink">Objecao {idx}</span>'
                f'<span class="accordion-label">{_escape(obj.get("texto",""))}</span>'
                '<span class="accordion-arrow">&#9662;</span>'
                "</div>"
                '<div class="accordion-body"><div style="padding:12px 20px 16px">'
                f"{corpo_args or '<p class=\"card-sub\">Sem argumentos registrados.</p>'}"
                "</div></div>"
                "</div>"
            )
        objecoes_html = (
            '<div class="card" style="margin-top:16px">'
            '<div class="card-label">Objecoes principais e como quebrar</div>'
            '<div style="margin-top:12px">'
            + "".join(acc_items)
            + "</div></div>"
        )
    miolo = grid_topo + args_card + objecoes_html
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
            '<div class="card-highlight" style="margin-bottom:16px">'
            '<div class="card-label">Para quem e</div>'
            f'<div class="card-value">{_escape(para_quem)}</div>'
            "</div>"
        )

    def _kv_card(titulo: str, pares: dict) -> str:
        linhas = "".join(
            f'<div style="margin-top:6px"><strong>{_escape(k)}:</strong> {_escape(v)}</div>'
            for k, v in pares.items() if v
        )
        if not linhas:
            linhas = '<div class="card-sub">Ainda sem dados.</div>'
        return (
            '<div class="card">'
            f'<div class="card-label">{_escape(titulo)}</div>'
            f"{linhas}"
            "</div>"
        )

    blocos.append(
        '<div class="grid-2" style="margin-top:16px">'
        + _kv_card("Perfil demografico", perfil)
        + _kv_card("Comportamento e canais", comportamento)
        + "</div>"
    )
    if paliativos:
        blocos.append(
            '<div class="card" style="margin-top:16px">'
            '<div class="card-label">Paliativos (concorrentes do mercado)</div>'
            + _ul(paliativos)
            + "</div>"
        )
    if baldes:
        accs = []
        for balde in baldes:
            accs.append(
                _accordion(
                    "badge-neutral",
                    balde.get("nome", "Perfil"),
                    "5 afirmacoes",
                    balde.get("itens", []),
                )
            )
        blocos.append(
            '<div class="card" style="margin-top:16px">'
            '<div class="card-label">Baldes de para quem e</div>'
            + '<div style="margin-top:12px">' + "".join(accs) + "</div>"
            + "</div>"
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
        '<div class="grid-3">'
        + _card("Comunicador", nome or "(sem nome)", sub=especialidade)
        + '<div class="card"><div class="card-label">Valores</div>'
        + '<div style="margin-top:10px">' + _pills(valores, "badge-green") + '</div></div>'
        + '<div class="card"><div class="card-label">Mantras e jargoes</div>'
        + ("".join(f'<div style="margin-top:6px;font-size:13px;color:var(--text-2)">{_escape(m)}</div>' for m in mantras)
           if mantras else '<div class="card-sub">Nenhum ainda.</div>')
        + "</div>"
        + "</div>"
    )
    grid2 = (
        '<div class="grid-2" style="margin-top:16px">'
        + '<div class="card"><div class="card-label">Formatos que combinam</div>'
        + '<div style="margin-top:10px">' + _pills(formatos, "badge-indigo") + '</div></div>'
        + '<div class="card"><div class="card-label">Estilo visual recomendado</div>'
        + '<div style="margin-top:10px">' + _pills(visual, "badge-neutral") + '</div></div>'
        + "</div>"
    )
    tom_pos = (
        '<div class="grid-2" style="margin-top:16px">'
        + '<div class="card"><div class="card-label">Tom de voz</div>'
        + f'<p class="para">{_escape(tom) or "&mdash;"}</p></div>'
        + '<div class="card"><div class="card-label">Posicionamento</div>'
        + f'<p class="para">{_escape(posicionamento) or "&mdash;"}</p></div>'
        + "</div>"
    )
    palavras = (
        '<div class="grid-2" style="margin-top:16px">'
        + '<div class="card"><div class="card-label">Palavras que conectam</div>'
        + '<div style="margin-top:10px">' + _pills(conectam, "badge-green") + '</div></div>'
        + '<div class="card"><div class="card-label">Palavras que afastam</div>'
        + '<div style="margin-top:10px">' + _pills(afastam, "badge-pink") + '</div></div>'
        + "</div>"
    )
    miolo = grid_topo + grid2 + tom_pos + palavras
    return f"<!-- SECTION:identidade-comunicador -->\n{miolo}\n<!-- /SECTION:identidade-comunicador -->"


def render_pesquisa(dados: dict) -> str:
    """Versao pragmatica da pesquisa: KPIs, oportunidades, cuidados, tabela
    completa de concorrentes com links reais."""
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
            {"label": "Tamanho do mercado", "valor": dados.get("tamanho_mercado") or "a mapear"},
            {"label": "Crescimento anual", "valor": dados.get("crescimento") or "a mapear"},
            {"label": "Concorrentes mapeados", "valor": str(len(concorrentes)) if concorrentes else "0"},
            {"label": "Ticket medio do nicho", "valor": dados.get("ticket_medio") or "a mapear"},
        ]
    kpis_html = "".join(
        f'<div class="kpi"><div class="kpi-label">{_escape(k["label"])}</div>'
        f'<div class="kpi-value">{_escape(k["valor"])}</div>'
        f'<div class="kpi-sub">{_escape(k.get("sub",""))}</div></div>'
        for k in kpis
    )

    opo_card = ""
    if oportunidades:
        opo_card = (
            '<div class="card" style="margin-top:16px">'
            '<div class="card-label">Oportunidades identificadas</div>'
            + _ul(oportunidades)
            + "</div>"
        )

    cuid_reclamar = ""
    if cuidados or reclamacoes:
        cuid_reclamar = (
            '<div class="grid-2" style="margin-top:16px">'
            '<div class="card"><div class="card-label">Cuidados e riscos</div>'
            + _ul(cuidados) + "</div>"
            '<div class="card"><div class="card-label">Padroes de reclamacao</div>'
            + _ul(reclamacoes) + "</div>"
            + "</div>"
        )

    tabela = ""
    if concorrentes:
        linhas = []
        for c in concorrentes:
            links_partes = []
            url = (c.get("pagina") or "").strip()
            insta = (c.get("instagram") or "").strip()
            if url and not _is_busca(url):
                links_partes.append(f'<a href="{_escape(url)}" target="_blank" rel="noopener" style="color:var(--primary);font-size:11px">&#8599; Pagina</a>')
            if insta and not _is_busca(insta):
                links_partes.append(f'<a href="{_escape(insta)}" target="_blank" rel="noopener" style="color:var(--primary);font-size:11px">&#8599; Instagram</a>')
            links_html = " &middot; ".join(links_partes) if links_partes else "&mdash;"
            preco_badge_cls = _preco_badge(c.get("preco", ""))
            preco = _escape(c.get("preco", ""))
            linhas.append(
                "<tr>"
                f"<td>{_escape(c.get('nome',''))}</td>"
                f"<td>{_escape(c.get('promessa',''))}</td>"
                f"<td>{_escape(c.get('formato',''))}</td>"
                f'<td><span class="badge {preco_badge_cls}">{preco or "&mdash;"}</span></td>'
                f"<td>{_escape(c.get('diferencial',''))}</td>"
                f"<td>{links_html}</td>"
                "</tr>"
            )
        tabela = (
            '<div class="card" style="margin-top:16px">'
            '<div class="card-label">Analise de concorrentes</div>'
            '<div class="table-wrap" style="margin-top:12px">'
            '<table>'
            "<thead><tr><th>Nome</th><th>Promessa</th><th>Formato</th><th>Preco</th><th>Diferencial</th><th>Links</th></tr></thead>"
            f"<tbody>{''.join(linhas)}</tbody>"
            "</table>"
            "</div></div>"
        )

    fontes_card = ""
    if fontes:
        fontes_card = (
            '<div class="card" style="margin-top:16px">'
            '<div class="card-label">Fontes consultadas</div>'
            + _ul(fontes)
            + "</div>"
        )

    miolo = (
        f'<div class="grid-4">{kpis_html}</div>'
        + opo_card
        + cuid_reclamar
        + tabela
        + fontes_card
    )
    return f"<!-- SECTION:pesquisa -->\n{miolo}\n<!-- /SECTION:pesquisa -->"


# ----- utilidades -----

_BUSCA_PATTERNS = re.compile(
    r"(google\.com/search|youtube\.com/results|bing\.com/search|search\?q=)",
    re.IGNORECASE,
)


def _is_busca(url: str) -> bool:
    return bool(_BUSCA_PATTERNS.search(url or ""))


def _preco_badge(preco: str) -> str:
    """Classifica preco em faixas de cor."""
    if not preco:
        return "badge-neutral"
    nums = re.findall(r"(\d+[\.\,]?\d*)", preco)
    if not nums:
        return "badge-neutral"
    try:
        valor = float(nums[0].replace(",", "."))
    except ValueError:
        return "badge-neutral"
    if valor <= 97:
        return "badge-green"
    if valor <= 497:
        return "badge-blue"
    if valor <= 1997:
        return "badge-purple"
    return "badge-dark"


RENDERS = {
    "quadro": render_quadro,
    "furadeira": render_furadeira,
    "decorados": render_decorados,
    "urgencias": render_urgencias,
    "identidade-produto": render_identidade_produto,
    "identidade-consumidor": render_identidade_consumidor,
    "identidade-comunicador": render_identidade_comunicador,
    "pesquisa": render_pesquisa,
}
