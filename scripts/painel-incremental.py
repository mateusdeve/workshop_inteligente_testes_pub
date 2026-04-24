"""
painel-incremental.py

Atualiza o painel de entregas de um produto de forma incremental, secao a
secao. Na primeira execucao, cria o shell HTML com placeholders "Em breve".
Em execucoes seguintes, troca apenas o bloco da secao pedida, preservando o
resto.

Uso:
    py -3 scripts/painel-incremental.py --secao quadro
    py -3 scripts/painel-incremental.py --secao pesquisa --slug meu-produto

Secoes validas (ids que aparecem na sidebar e marcadores SECTION):
    pesquisa
    quadro
    furadeira
    decorados
    urgencias
    identidade-produto
    identidade-consumidor
    identidade-comunicador

O painel vive em:
    meus-produtos/{slug}/painel-entregas.html

Quando o slug nao e informado, o script le meus-produtos/.ativo.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import painel_template as tmpl  # noqa: E402

PRODUTOS_DIR = REPO_ROOT / "meus-produtos"
ATIVO_FILE = PRODUTOS_DIR / ".ativo"
PAINEL_NOME = "painel-entregas.html"

SECOES_VALIDAS = sorted(tmpl.SECOES_RENDERIZAVEIS)


# ----- leitura de arquivos -----

def ler_ativo() -> str | None:
    if not ATIVO_FILE.exists():
        return None
    txt = ATIVO_FILE.read_text(encoding="utf-8").strip()
    return txt or None


def ler_arquivo(p: Path) -> str:
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


# ----- helpers de parsing do markdown -----

_H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def extrair_secao(texto: str, titulo: str) -> str:
    """Extrai o conteudo entre o H2 titulo e o proximo H2 (ou fim do arquivo)."""
    if not texto:
        return ""
    # localiza H2 com o titulo (case-insensitive)
    pad = re.compile(
        rf"^##\s+{re.escape(titulo)}\s*$", re.IGNORECASE | re.MULTILINE
    )
    m = pad.search(texto)
    if not m:
        # permitir prefixos (ex: "## Furadeira (Metodo)")
        pad2 = re.compile(
            rf"^##\s+{re.escape(titulo)}\b[^\n]*$", re.IGNORECASE | re.MULTILINE
        )
        m = pad2.search(texto)
    if not m:
        return ""
    inicio = m.end()
    fim_match = _H2_RE.search(texto, pos=inicio)
    fim = fim_match.start() if fim_match else len(texto)
    return texto[inicio:fim].strip()


def extrair_subsecao(texto: str, titulo: str) -> str:
    """Extrai conteudo entre H3 titulo e proximo H3 ou H2."""
    if not texto:
        return ""
    pad = re.compile(
        rf"^###\s+{re.escape(titulo)}\s*$", re.IGNORECASE | re.MULTILINE
    )
    m = pad.search(texto)
    if not m:
        pad2 = re.compile(
            rf"^###\s+{re.escape(titulo)}\b[^\n]*$", re.IGNORECASE | re.MULTILINE
        )
        m = pad2.search(texto)
    if not m:
        return ""
    inicio = m.end()
    fim_match = re.search(r"^(?:##|###)\s", texto[inicio:], re.MULTILINE)
    fim = inicio + fim_match.start() if fim_match else len(texto)
    return texto[inicio:fim].strip()


def bullets(texto: str) -> list[str]:
    """Extrai itens de uma lista de bullets (- ou *)."""
    if not texto:
        return []
    out = []
    for linha in texto.splitlines():
        linha = linha.rstrip()
        m = re.match(r"^\s*[-*]\s+(.+?)\s*$", linha)
        if m:
            out.append(m.group(1).strip())
    return out


def kv_bullets(texto: str) -> dict[str, str]:
    """Le bullets no formato '- **Chave:** valor' e retorna dict."""
    out: dict[str, str] = {}
    if not texto:
        return out
    for linha in texto.splitlines():
        m = re.match(r"^\s*[-*]\s+\*\*(.+?)\s*:\*\*\s*(.+?)\s*$", linha)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def valor_label(texto: str, label: str) -> str:
    """Busca '**Label:** valor' (em bullet ou linha comum) e retorna valor."""
    if not texto:
        return ""
    pad = re.compile(
        rf"\*\*{re.escape(label)}\s*:\*\*\s*(.+?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    m = pad.search(texto)
    return m.group(1).strip() if m else ""


def extrair_titulo_produto(perfil_texto: str, slug: str) -> str:
    """Reusa heuristica de painel-atualizar para descobrir nome amigavel."""
    nome_via_label = valor_label(perfil_texto, "Nome")
    if nome_via_label:
        return nome_via_label
    m = re.search(r"^#\s+(.+?)\s*$", perfil_texto, re.MULTILINE)
    if m:
        titulo = m.group(1).strip()
        for sep in (" \u2014 ", " \u2013 ", " - ", ": "):
            if sep in titulo:
                return titulo.split(sep, 1)[1].strip()
        if not titulo.lower().startswith("perfil"):
            return titulo
    return slug.replace("-", " ").title()


# ----- parsers por secao -----

def parse_quadro(perfil: str) -> dict:
    bloco = extrair_secao(perfil, "Quadro (Transformacao Principal)") \
        or extrair_secao(perfil, "Quadro")
    # primeiro paragrafo nao vazio
    texto = ""
    for linha in bloco.splitlines():
        if linha.strip():
            texto = linha.strip()
            break
    return {"quadro": texto}


def parse_furadeira(perfil: str, produto_dir: Path) -> dict:
    bloco = extrair_secao(perfil, "Furadeira (Metodo)") \
        or extrair_secao(perfil, "Furadeira")
    nome_metodo = valor_label(bloco, "Nome do Metodo") or valor_label(bloco, "Nome do Método")
    furadeira_html = valor_label(bloco, "Furadeira HTML")

    macro = []
    for m in re.finditer(
        r"^\d+\.\s+\*\*(.+?)\*\*\s*\.?\s*(.+?)$",
        bloco,
        re.MULTILINE,
    ):
        macro.append({"titulo": m.group(1).strip(), "descricao": m.group(2).strip()})

    # checa existencia fisica do trilha visual
    if furadeira_html:
        rel = furadeira_html
        if rel.startswith("meus-produtos/"):
            rel = rel.split("/", 2)[-1]  # tira meus-produtos/{slug}/
            if rel.startswith(produto_dir.name + "/"):
                rel = rel[len(produto_dir.name) + 1 :]
        caminho_abs = produto_dir / rel
        if not caminho_abs.exists():
            furadeira_html = ""
        else:
            furadeira_html = rel
    else:
        fallback = produto_dir / "entregas" / "furadeira-visual.html"
        if fallback.exists():
            furadeira_html = "entregas/furadeira-visual.html"

    return {
        "nome_metodo": nome_metodo,
        "macroetapas": macro,
        "furadeira_html": furadeira_html,
    }


def parse_decorados(perfil: str) -> dict:
    bloco = extrair_secao(perfil, "Decorados (Beneficios)") \
        or extrair_secao(perfil, "Decorados")
    categorias: dict[str, list[str]] = {}
    for cat in ["Financeiro", "Tempo", "Autoestima", "Reputacao", "Reputação", "Crescimento"]:
        itens = bullets(extrair_subsecao(bloco, cat))
        if itens:
            key = "Reputacao" if cat in ("Reputação", "Reputacao") else cat
            categorias[key] = itens
    return {"decorados": categorias}


def parse_urgencias(perfil: str) -> dict:
    bloco = extrair_secao(perfil, "Urgencias Ocultas") \
        or extrair_secao(perfil, "Urgências Ocultas")
    mapa = [
        ("Dores", ["Dores", "Dores (o que incomoda)"]),
        ("Duvidas", ["Duvidas", "Dúvidas", "Duvidas (o que pergunta)", "Dúvidas (o que pergunta)"]),
        ("Desejos", ["Desejos", "Desejos (o que sonha)"]),
        ("Assuntos Relacionados", ["Assuntos Relacionados", "Assuntos Relacionados (o que interessa)"]),
        ("Urgencias Quentes", ["Urgencias Quentes", "Urgências Quentes", "Urgencias Quentes (alta intencao)", "Urgências Quentes (alta intenção)"]),
        ("Urgencias Frias", ["Urgencias Frias", "Urgências Frias", "Urgencias Frias (atracao)", "Urgências Frias (atração)"]),
        ("Urgencias Inusitadas", ["Urgencias Inusitadas", "Urgências Inusitadas", "Urgencias Inusitadas (angulo diferente)", "Urgências Inusitadas (ângulo diferente)"]),
    ]
    out: dict[str, list[str]] = {}
    for chave, variantes in mapa:
        for v in variantes:
            itens = bullets(extrair_subsecao(bloco, v))
            if itens:
                out[chave] = itens
                break
    return {"urgencias": out}


def parse_identidade_produto(perfil: str) -> dict:
    ip = extrair_secao(perfil, "Identidade do Produto")
    kv = kv_bullets(ip)
    args = bullets(extrair_secao(perfil, "Argumentos Incontestaveis") or extrair_secao(perfil, "Argumentos Incontestáveis"))
    objecoes = parse_objecoes_do_idconsumidor(None)  # preenchido depois via kwargs
    return {
        "diferencial": kv.get("Diferencial", ""),
        "formato": kv.get("Formato", ""),
        "nome": kv.get("Nome", ""),
        "preco": kv.get("Preco", "") or kv.get("Preço", ""),
        "argumentos_incontestaveis": args,
        "objecoes": objecoes,
    }


_ORDEM_ARGS = [
    "Argumento Incontestavel",
    "Argumento Logico",
    "Argumento por Analogia",
    "Argumento por Exemplificacao",
    "Argumento de Valor",
    "Argumento de Consequencia",
    "Argumento de Contradicao",
]


def parse_objecoes_do_idconsumidor(idc_texto: str | None) -> list[dict]:
    if not idc_texto:
        return []
    bloco = extrair_secao(idc_texto, "Objecoes de Compra (Framework dos 7 Argumentos)") \
        or extrair_secao(idc_texto, "Objeções de Compra (Framework dos 7 Argumentos)") \
        or extrair_secao(idc_texto, "Objecoes de Compra") \
        or extrair_secao(idc_texto, "Objeções de Compra")
    if not bloco:
        return []
    # Divide em objecoes via H3 "Objecao N:"
    objecoes = []
    partes = re.split(
        r"^###\s+Obje[cç][aã]o\s+\d+:\s*(.+?)\s*$",
        bloco,
        flags=re.MULTILINE,
    )
    # partes alterna: [prefixo, texto_obj_1, corpo_obj_1, texto_obj_2, corpo_obj_2, ...]
    for i in range(1, len(partes), 2):
        texto_obj = partes[i].strip()
        corpo = partes[i + 1] if i + 1 < len(partes) else ""
        argumentos = []
        # cada argumento comeca com **N. Nome...**
        blocos_arg = re.split(r"^\*\*(\d+)\.\s+([^\n]+?)\*\*\s*$", corpo, flags=re.MULTILINE)
        for j in range(1, len(blocos_arg), 3):
            titulo = f"{blocos_arg[j]}. {blocos_arg[j+1].strip()}"
            corpo_arg = blocos_arg[j + 2] if j + 2 < len(blocos_arg) else ""
            paragrafos = [p.strip() for p in re.split(r"\n\s*\n", corpo_arg) if p.strip()]
            # remove paragrafos que sao na verdade marcadores
            paragrafos = [re.sub(r"^\[|\]$", "", p) for p in paragrafos if not p.startswith("###")]
            argumentos.append({"titulo": titulo.upper(), "paragrafos": paragrafos})
        objecoes.append({"texto": texto_obj, "argumentos": argumentos})
    return objecoes


def parse_identidade_consumidor(perfil: str, idc: str) -> dict:
    fonte = idc or perfil
    # Para quem e
    para_quem = ""
    pq_bloco = extrair_secao(fonte, "Para Quem E") or extrair_secao(fonte, "Para Quem É")
    if pq_bloco:
        # primeira frase entre aspas ou primeiro paragrafo significativo
        for p in re.split(r"\n\s*\n", pq_bloco):
            p = p.strip()
            if p:
                para_quem = p.strip('"\'')
                break

    # Perfil demografico vem do bloco "Identidade do Consumidor" no idconsumidor ou no perfil
    ic_bloco = extrair_secao(idc, "Identidade do Consumidor")
    if not ic_bloco:
        ic_bloco = extrair_secao(perfil, "Identidade do Consumidor")
    kv = kv_bullets(ic_bloco)

    perfil_demo = {
        "Idade": kv.get("Idade", ""),
        "Genero": kv.get("Genero", "") or kv.get("Gênero", ""),
        "Profissao": kv.get("Profissao", "") or kv.get("Profissão", ""),
        "Renda": kv.get("Renda", ""),
        "Localizacao": kv.get("Localizacao", "") or kv.get("Localização", ""),
        "Nivel de consciencia": kv.get("Nivel de consciencia", "")
            or kv.get("Nível de consciência", ""),
    }
    comportamento = {
        "Onde busca info": kv.get("Onde busca informacao", "") or kv.get("Onde busca informação", ""),
        "Comportamento": kv.get("Comportamento", ""),
        "Objecoes": kv.get("Objecoes tipicas", "") or kv.get("Objeções típicas", ""),
    }

    # paliativos
    paliativos = bullets(
        extrair_secao(
            idc,
            "Paliativos (somente Middle Ticket - ferramentas e solucoes concorrentes do mercado que resolvem o problema parcialmente)",
        )
        or extrair_secao(idc, "Paliativos")
    )

    # baldes
    baldes = []
    if idc:
        baldes_txt = extrair_secao(idc, "Baldes de Para Quem E") or extrair_secao(idc, "Baldes de Para Quem É")
        if baldes_txt:
            for m in re.finditer(
                r"\u279c\s*Pra quem e\s*-\s*(.+?)\n((?:\d+\.\s+.+?\n?)+)",
                baldes_txt,
                re.IGNORECASE,
            ):
                nome = m.group(1).strip().strip("[]")
                itens = [
                    re.sub(r"^\d+\.\s+", "", ln).strip()
                    for ln in m.group(2).splitlines()
                    if ln.strip()
                ]
                baldes.append({"nome": nome, "itens": itens})

    return {
        "para_quem_e": para_quem,
        "perfil_demo": {k: v for k, v in perfil_demo.items() if v},
        "comportamento": {k: v for k, v in comportamento.items() if v},
        "paliativos": paliativos,
        "baldes": baldes,
    }


def parse_identidade_comunicador(perfil: str, idc: str) -> dict:
    bloco = extrair_secao(perfil, "Identidade do Comunicador")
    kv = kv_bullets(bloco)

    def _listar(valor: str) -> list[str]:
        if not valor:
            return []
        partes = re.split(r"[,;]\s*|\s*\|\s*", valor)
        return [p.strip() for p in partes if p.strip()]

    comunicar_idc = extrair_secao(idc, "Como se Comunicar")
    conectam = []
    afastam = []
    if comunicar_idc:
        m_c = re.search(
            r"^[-*]\s+Palavras que conectam\s*:?\s*(.+?)$",
            comunicar_idc,
            re.MULTILINE | re.IGNORECASE,
        )
        m_a = re.search(
            r"^[-*]\s+Palavras que afastam\s*:?\s*(.+?)$",
            comunicar_idc,
            re.MULTILINE | re.IGNORECASE,
        )
        if m_c:
            conectam = _listar(m_c.group(1))
        if m_a:
            afastam = _listar(m_a.group(1))

    if not conectam:
        conectam = _listar(kv.get("Vocabulario base", "") or kv.get("Vocabulário base", ""))

    return {
        "nome": kv.get("Nome", ""),
        "especialidade": kv.get("Especialidade", ""),
        "valores": _listar(kv.get("Valores", "")),
        "mantras": _listar(kv.get("Mantras/Jargoes proprios", "")
                           or kv.get("Mantras/Jargões próprios", "")),
        "formatos": _listar(kv.get("Formatos que combinam mais", "")),
        "elementos_visuais": _listar(kv.get("Elementos visuais recomendados", "")),
        "tom_de_voz": kv.get("Tom de voz", ""),
        "posicionamento": kv.get("Posicionamento pessoal", ""),
        "palavras_conectam": conectam,
        "palavras_afastam": afastam,
    }


def parse_pesquisa(texto: str) -> dict:
    """Extracao pragmatica: os campos mais comuns de pesquisa-mercado.md.
    Estrutura do arquivo varia, entao usamos heuristicas tolerantes."""
    if not texto:
        return {}

    tamanho = (
        valor_label(texto, "Tamanho do mercado")
        or valor_label(texto, "Tamanho estimado")
    )
    crescimento = valor_label(texto, "Crescimento") or valor_label(texto, "Crescimento anual")
    ticket = valor_label(texto, "Ticket medio") or valor_label(texto, "Ticket médio")

    # Oportunidades
    opo_bloco = (
        extrair_secao(texto, "Oportunidades Identificadas")
        or extrair_secao(texto, "Oportunidades")
        or extrair_subsecao(texto, "Oportunidades de posicionamento")
    )
    oportunidades = bullets(opo_bloco) if opo_bloco else []

    # Cuidados
    cuidados_bloco = (
        extrair_secao(texto, "Cuidados e Riscos")
        or extrair_secao(texto, "Alertas e Riscos")
        or extrair_secao(texto, "Cuidados")
    )
    cuidados = bullets(cuidados_bloco) if cuidados_bloco else []

    # Reclame Aqui
    rec_bloco = (
        extrair_secao(texto, "Reclame Aqui")
        or extrair_secao(texto, "Padroes de Reclamacao")
        or extrair_secao(texto, "Reclamacoes")
        or extrair_secao(texto, "Reclamações")
    )
    reclamacoes = bullets(rec_bloco) if rec_bloco else []

    # Concorrentes: busca a primeira tabela markdown
    concorrentes = parse_tabela_concorrentes(texto)

    # Fontes
    fontes_bloco = extrair_secao(texto, "Fontes") or extrair_secao(texto, "Fontes Consultadas")
    fontes = bullets(fontes_bloco) if fontes_bloco else []

    return {
        "tamanho_mercado": tamanho,
        "crescimento": crescimento,
        "ticket_medio": ticket,
        "oportunidades": oportunidades,
        "cuidados": cuidados,
        "reclamacoes": reclamacoes,
        "concorrentes": concorrentes,
        "fontes": fontes,
    }


def parse_tabela_concorrentes(texto: str) -> list[dict]:
    """Extrai tabelas markdown que contenham concorrentes. Tolerante a variacoes."""
    out: list[dict] = []
    # localiza blocos de tabela simples
    tabelas = re.findall(
        r"(^\|.+\|\s*\n\|[\s\-:\|]+\|\s*\n(?:\|.+\|\s*\n?)+)",
        texto,
        re.MULTILINE,
    )
    for tab in tabelas:
        linhas = [ln.strip() for ln in tab.strip().splitlines() if ln.strip().startswith("|")]
        if len(linhas) < 2:
            continue
        header = [c.strip().lower() for c in linhas[0].strip("|").split("|")]
        # heuristica: precisa ter alguma coluna de nome/concorrente
        if not any("nome" in h or "concorrente" in h or "marca" in h for h in header):
            continue
        col_nome = next((i for i, h in enumerate(header) if "nome" in h or "concorrente" in h or "marca" in h), 0)
        col_insta = next((i for i, h in enumerate(header) if "instagram" in h or "insta" in h), None)
        col_pagina = next((i for i, h in enumerate(header) if "pagina" in h or "página" in h or "site" in h or "link" in h), None)
        col_preco = next((i for i, h in enumerate(header) if "preco" in h or "preço" in h or "valor" in h), None)
        col_promessa = next((i for i, h in enumerate(header) if "promessa" in h), None)
        col_formato = next((i for i, h in enumerate(header) if "formato" in h), None)
        col_diferencial = next((i for i, h in enumerate(header) if "diferencial" in h), None)

        for linha in linhas[2:]:
            celulas = [c.strip() for c in linha.strip("|").split("|")]
            if len(celulas) <= col_nome or not celulas[col_nome]:
                continue
            def _cel(idx):
                if idx is None or idx >= len(celulas):
                    return ""
                return _limpa_link(celulas[idx])
            out.append({
                "nome": _limpa_texto(celulas[col_nome]),
                "promessa": _limpa_texto(_cel(col_promessa)),
                "formato": _limpa_texto(_cel(col_formato)),
                "preco": _limpa_texto(_cel(col_preco)),
                "diferencial": _limpa_texto(_cel(col_diferencial)),
                "pagina": _extrai_url(_cel(col_pagina)),
                "instagram": _extrai_url(_cel(col_insta)),
            })
        if out:
            break  # primeira tabela valida e suficiente
    return out


def _limpa_texto(s: str) -> str:
    if not s:
        return ""
    # remove markdown simples
    return re.sub(r"[\*_`]", "", s).strip()


def _limpa_link(s: str) -> str:
    return s.strip()


def _extrai_url(s: str) -> str:
    if not s:
        return ""
    m = re.search(r"\[.*?\]\((https?://[^\s)]+)\)", s)
    if m:
        return m.group(1)
    m2 = re.search(r"https?://\S+", s)
    if m2:
        return m2.group(0).rstrip("),.")
    return s.strip() if s.startswith("http") else ""


# ----- monta dados por secao -----

def montar_dados(secao: str, produto_dir: Path, slug: str) -> tuple[dict, str]:
    perfil = ler_arquivo(produto_dir / "perfil.md")
    idc = ler_arquivo(produto_dir / "idconsumidor.md")
    pesquisa = ler_arquivo(produto_dir / "pesquisa-mercado.md")
    nome_produto = extrair_titulo_produto(perfil, slug)

    if secao == "quadro":
        return parse_quadro(perfil), nome_produto
    if secao == "furadeira":
        return parse_furadeira(perfil, produto_dir), nome_produto
    if secao == "decorados":
        return parse_decorados(perfil), nome_produto
    if secao == "urgencias":
        return parse_urgencias(perfil), nome_produto
    if secao == "identidade-produto":
        dados = parse_identidade_produto(perfil)
        dados["objecoes"] = parse_objecoes_do_idconsumidor(idc)
        return dados, nome_produto
    if secao == "identidade-consumidor":
        return parse_identidade_consumidor(perfil, idc), nome_produto
    if secao == "identidade-comunicador":
        return parse_identidade_comunicador(perfil, idc), nome_produto
    if secao == "pesquisa":
        return parse_pesquisa(pesquisa), nome_produto
    raise ValueError(f"Secao desconhecida: {secao}")


# ----- visao geral (derivada) -----

def secoes_preenchidas(html_txt: str) -> list[str]:
    """Lista de secoes ja preenchidas no HTML atual (sem ser placeholder)."""
    prontas: list[str] = []
    rotulo_por_id = {
        "quadro": "Quadro",
        "furadeira": "Furadeira",
        "decorados": "Decorados",
        "urgencias": "Urgencias ocultas",
        "identidade-produto": "Identidade do produto",
        "identidade-consumidor": "Identidade do consumidor",
        "identidade-comunicador": "Identidade do comunicador",
        "pesquisa": "Pesquisa de mercado",
    }
    for sid, rotulo in rotulo_por_id.items():
        bloco = extrair_bloco_secao(html_txt, sid)
        if bloco and "placeholder-title" not in bloco:
            prontas.append(rotulo)
    return prontas


def montar_visao_geral(html_txt: str, perfil: str, slug: str, tipo: str) -> dict:
    quadro_bloco = (
        extrair_secao(perfil, "Quadro (Transformacao Principal)")
        or extrair_secao(perfil, "Quadro")
    )
    quadro = ""
    for linha in quadro_bloco.splitlines():
        if linha.strip():
            quadro = linha.strip()
            break

    ip = extrair_secao(perfil, "Identidade do Produto")
    kv_ip = kv_bullets(ip)
    ic = extrair_secao(perfil, "Identidade do Consumidor")
    kv_ic = kv_bullets(ic)

    preco = kv_ip.get("Preco", "") or kv_ip.get("Preço", "")
    diferencial = kv_ip.get("Diferencial", "")
    nicho = kv_ic.get("Nicho", "") or kv_ic.get("Publico-alvo", "") or kv_ic.get("Público-alvo", "")

    return {
        "nome_produto": extrair_titulo_produto(perfil, slug),
        "tipo": tipo,
        "preco": preco,
        "quadro": quadro or "Quadro ainda nao definido.",
        "nicho": nicho,
        "diferencial": diferencial,
        "secoes_prontas": secoes_preenchidas(html_txt),
    }


# ----- manipulacao do HTML -----

def extrair_bloco_secao(html_txt: str, secao: str) -> str:
    pat = re.compile(
        rf"<!--\s*SECTION:{re.escape(secao)}\s*-->(.*?)<!--\s*/SECTION:{re.escape(secao)}\s*-->",
        re.DOTALL,
    )
    m = pat.search(html_txt)
    return m.group(0) if m else ""


def substituir_secao(html_txt: str, secao: str, novo: str) -> str:
    pat = re.compile(
        rf"<!--\s*SECTION:{re.escape(secao)}\s*-->.*?<!--\s*/SECTION:{re.escape(secao)}\s*-->",
        re.DOTALL,
    )
    if pat.search(html_txt):
        return pat.sub(lambda m: novo, html_txt, count=1)
    # Se o marcador nao existe (painel legado), nao mexe
    return html_txt


# ----- CLI -----

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--secao",
        required=True,
        choices=SECOES_VALIDAS,
        help="Secao a atualizar",
    )
    parser.add_argument(
        "--slug",
        default=None,
        help="Slug do produto (default: le meus-produtos/.ativo)",
    )
    parser.add_argument(
        "--rebuild-shell",
        action="store_true",
        help="Forca a recriacao do shell mesmo que o painel ja exista (uso raro)",
    )
    args = parser.parse_args()

    slug = args.slug or ler_ativo()
    if not slug:
        print("Nenhum produto ativo. Use /produto-novo ou --slug.", file=sys.stderr)
        return 1

    produto_dir = PRODUTOS_DIR / slug
    if not produto_dir.is_dir():
        print(f"Produto nao encontrado: {produto_dir}", file=sys.stderr)
        return 1

    painel_path = produto_dir / PAINEL_NOME

    perfil = ler_arquivo(produto_dir / "perfil.md")
    tipo_md = ler_arquivo(produto_dir / "tipo.md").strip() or "a definir"
    nome_produto = extrair_titulo_produto(perfil, slug)

    # Cria shell se nao existir ou se o existente nao tem marcadores (legado)
    existente = painel_path.read_text(encoding="utf-8") if painel_path.exists() else ""
    tem_markers = "<!-- SECTION:" in existente
    criou_shell = False
    if not existente or args.rebuild_shell or not tem_markers:
        existente = tmpl.build_shell(nome_produto)
        criou_shell = True

    # Atualiza secao pedida
    dados, _ = montar_dados(args.secao, produto_dir, slug)
    render = tmpl.RENDERS[args.secao]
    novo_bloco = render(dados)
    existente = substituir_secao(existente, args.secao, novo_bloco)

    # Atualiza visao-geral (derivada)
    vg_dados = montar_visao_geral(existente, perfil, slug, tipo_md)
    existente = substituir_secao(existente, "visao-geral", tmpl.render_visao_geral(vg_dados))

    # Atualiza nome do produto na sidebar se o perfil mudou desde a criacao
    existente = re.sub(
        r'(<div class="sidebar-product">).*?(</div>)',
        lambda m: f"{m.group(1)}{nome_produto}{m.group(2)}",
        existente,
        count=1,
    )

    painel_path.write_text(existente, encoding="utf-8")

    caminho_rel = painel_path.relative_to(REPO_ROOT)
    if criou_shell:
        print(f"Painel criado em {caminho_rel}")
    print(f"Secao atualizada: {args.secao}")
    print(f"Caminho: {caminho_rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
