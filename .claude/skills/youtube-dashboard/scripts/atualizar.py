#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Dashboard - Workshop Marketing IA
Coleta dados publicos do canal e videos via Apify (apify~youtube-scraper)
e gera um dashboard HTML autossuficiente.

Uso:
  python atualizar.py [--abrir] [--canal URL_OU_HANDLE]
"""

import os
import re
import sys
import json
import time
import base64
import logging
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("ERRO: requests nao instalado. Execute: pip install requests")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
ATOR_APIFY = "apify~youtube-scraper"
API_BASE = "https://api.apify.com/v2"
TIMEOUT_SYNC = 300
MAX_VIDEOS = 30
WORKERS_DOWNLOAD = 5

STOP_WORDS = {
    "de", "da", "do", "das", "dos", "e", "em", "para", "com", "um", "uma",
    "o", "a", "os", "as", "no", "na", "nos", "nas", "se", "que", "por",
    "ao", "ou", "seu", "sua", "seus", "suas", "me", "te", "lhe", "isso",
    "este", "esta", "esse", "essa", "isto", "aqui", "ali", "mas", "mais",
    "muito", "como", "quando", "quem", "qual", "ate", "ja", "nao", "vai",
    "sim", "vc", "td", "tb", "the", "and", "or", "in", "on", "of", "to",
    "is", "for", "at", "by", "with", "from", "that", "this", "it", "be",
    "are", "was", "were", "have", "has", "had", "not", "do", "does", "did",
    "my", "your", "his", "her", "our", "their", "we", "you", "they",
    "vs", "ft", "feat", "ep", "pt", "vol", "num", "uma", "nessa",
}

# ---------------------------------------------------------------------------
# Utilitarios
# ---------------------------------------------------------------------------

def raiz_projeto() -> Path:
    # script fica em .claude/skills/youtube-dashboard/scripts/ — sobe 4 niveis
    return Path(__file__).resolve().parents[4]


def carregar_env() -> dict:
    env_path = raiz_projeto() / ".env"
    resultado = {}
    if not env_path.exists():
        return resultado
    with open(env_path, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith("#") or "=" not in linha:
                continue
            chave, _, valor = linha.partition("=")
            resultado[chave.strip()] = valor.strip().strip('"').strip("'")
    return resultado


def get_output_dir() -> Path:
    raiz = raiz_projeto()
    ativo_path = raiz / "meus-produtos" / ".ativo"
    if ativo_path.exists():
        slug = ativo_path.read_text(encoding="utf-8").strip()
        if slug:
            out = raiz / "meus-produtos" / slug / "entregas" / "youtube-dashboard"
            out.mkdir(parents=True, exist_ok=True)
            return out
    fallback = raiz / "meus-produtos" / "youtube-dashboard"
    fallback.mkdir(parents=True, exist_ok=True)
    return fallback


def configurar_log(output_dir: Path) -> logging.Logger:
    log_path = output_dir / "log.txt"
    logger = logging.getLogger("youtube-dashboard")
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    return logger


def parse_duracao(raw) -> int:
    """Converte qualquer formato de duracao para segundos."""
    if not raw:
        return 0
    if isinstance(raw, (int, float)):
        return int(raw)
    s = str(raw).strip()
    # ISO 8601: PT1H2M3S
    m = re.match(r"^PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$", s.upper())
    if m:
        h, mi, se = (int(x or 0) for x in m.groups())
        return h * 3600 + mi * 60 + se
    # HH:MM:SS ou MM:SS
    partes = s.split(":")
    try:
        if len(partes) == 3:
            return int(partes[0]) * 3600 + int(partes[1]) * 60 + int(partes[2])
        elif len(partes) == 2:
            return int(partes[0]) * 60 + int(partes[1])
        else:
            return int(float(s))
    except Exception:
        return 0


def parse_numero_str(val) -> int:
    """Converte '1.2M', '12.3K', '1,234,567' ou int para inteiro."""
    if val is None:
        return 0
    if isinstance(val, (int, float)):
        return int(val)
    s = str(val).strip().replace(",", "")
    try:
        if s.upper().endswith("M"):
            return int(float(s[:-1]) * 1_000_000)
        if s.upper().endswith("K"):
            return int(float(s[:-1]) * 1_000)
        return int(float(s))
    except Exception:
        return 0


def parse_data_ts(raw) -> int:
    """Converte data ISO para timestamp Unix."""
    if not raw:
        return 0
    s = str(raw).strip()
    # Tenta YYYY-MM-DD (primeiros 10 chars)
    try:
        return int(datetime.strptime(s[:10], "%Y-%m-%d").timestamp())
    except Exception:
        pass
    try:
        return int(datetime.strptime(s[:10], "%d/%m/%Y").timestamp())
    except Exception:
        pass
    try:
        return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp())
    except Exception:
        return 0


def formatar_numero(n: int) -> str:
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


def formatar_duracao(segundos: int) -> str:
    if segundos <= 0:
        return "0s"
    if segundos < 60:
        return f"{segundos}s"
    m, s = divmod(segundos, 60)
    if m < 60:
        return f"{m}min {s}s" if s else f"{m}min"
    h, m = divmod(m, 60)
    return f"{h}h {m}min" if m else f"{h}h"


def formatar_data(ts: int) -> str:
    if not ts:
        return ""
    try:
        return datetime.fromtimestamp(ts).strftime("%d/%m/%Y")
    except Exception:
        return ""


def normalizar_canal_url(raw: str) -> str:
    """Garante que a URL do canal esta em formato completo."""
    s = raw.strip().strip('"').strip("'")
    if s.startswith("http"):
        return s
    if s.startswith("@"):
        return f"https://www.youtube.com/{s}"
    if s.startswith("UC"):
        return f"https://www.youtube.com/channel/{s}"
    return f"https://www.youtube.com/@{s}"


def baixar_base64(url: str, log: logging.Logger, nome: str = "") -> str:
    if not url:
        return ""
    try:
        resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        ct = resp.headers.get("Content-Type", "image/jpeg").split(";")[0]
        b64 = base64.b64encode(resp.content).decode()
        return f"data:{ct};base64,{b64}"
    except Exception as e:
        log.warning(f"Falha ao baixar {nome}: {e}")
        return ""


def extrair_palavras_titulo(videos: list, top_pct: float = 0.5) -> list:
    """Extrai palavras mais frequentes dos titulos dos videos com mais views."""
    if not videos:
        return []
    videos_sorted = sorted(videos, key=lambda v: v["views"], reverse=True)
    top_n = max(1, int(len(videos_sorted) * top_pct))
    top_videos = videos_sorted[:top_n]
    contador: Counter = Counter()
    for v in top_videos:
        palavras = re.findall(r"[a-zA-Z\u00C0-\u00FF]{3,}", v["titulo"].lower())
        for p in palavras:
            if p not in STOP_WORDS:
                contador[p] += 1
    return [{"palavra": p, "count": c} for p, c in contador.most_common(15)]


# ---------------------------------------------------------------------------
# Apify
# ---------------------------------------------------------------------------

def chamar_apify(token: str, canal_url: str, log: logging.Logger) -> list:
    url = f"{API_BASE}/acts/{ATOR_APIFY}/run-sync-get-dataset-items"
    payload = {
        "startUrls": [{"url": canal_url}],
        "maxResults": MAX_VIDEOS,
    }
    log.info(f"Chamando Apify para {canal_url} (timeout {TIMEOUT_SYNC}s)...")
    try:
        resp = requests.post(
            url,
            params={"token": token},
            json=payload,
            timeout=TIMEOUT_SYNC + 30,
        )
        if resp.status_code == 401:
            log.error("Token Apify invalido. Verifique APIFY_API_TOKEN no .env")
            sys.exit(1)
        if resp.status_code == 402:
            log.error("Limite de uso do Apify atingido. Verifique seu plano em console.apify.com")
            sys.exit(1)
        resp.raise_for_status()
        dados = resp.json()
        if isinstance(dados, list):
            log.info(f"Apify retornou {len(dados)} itens.")
            return dados
        log.error(f"Resposta inesperada: {type(dados)}")
        return []
    except requests.exceptions.Timeout:
        log.error(f"Timeout ({TIMEOUT_SYNC}s). Tente novamente.")
        sys.exit(1)
    except Exception as e:
        log.error(f"Erro ao chamar Apify: {e}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Normalizacao
# ---------------------------------------------------------------------------

def normalizar_canal(itens: list) -> dict:
    """Extrai informacoes do canal a partir dos itens retornados."""
    vazio = {
        "nome": "", "inscritos": 0, "total_views_canal": 0,
        "descricao": "", "data_criacao": "", "avatar_url": "",
        "canal_url": "", "avatar_b64": "",
    }
    if not itens:
        return vazio

    # Percorre itens buscando dados do canal
    melhor = {}
    for item in itens:
        ci = item.get("channelInfo") or item.get("aboutChannelInfo") or {}
        inscritos = parse_numero_str(
            item.get("numberOfSubscribers")
            or item.get("subscriberCount")
            or ci.get("subscriberCount")
            or ci.get("numberOfSubscribers")
            or 0
        )
        nome = (
            item.get("channelName")
            or item.get("channel")
            or ci.get("title")
            or ci.get("name")
            or ""
        )
        if nome and (not melhor or inscritos > melhor.get("inscritos", 0)):
            melhor = {
                "nome": nome,
                "inscritos": inscritos,
                "total_views_canal": parse_numero_str(
                    ci.get("viewCount")
                    or ci.get("totalViews")
                    or item.get("channelTotalViews")
                    or 0
                ),
                "descricao": ci.get("description") or item.get("channelDescription") or "",
                "data_criacao": (
                    ci.get("joinDate")
                    or ci.get("createdAt")
                    or item.get("channelJoinedDate")
                    or ""
                ),
                "avatar_url": (
                    ci.get("avatarUrl")
                    or ci.get("thumbnail")
                    or item.get("channelThumbnail")
                    or ""
                ),
                "canal_url": item.get("channelUrl") or "",
                "avatar_b64": "",
            }
        if melhor.get("inscritos", 0) > 0:
            break  # encontrou dados suficientes

    return melhor if melhor else vazio


def normalizar_video(item: dict) -> dict:
    url_video = item.get("url") or item.get("videoUrl") or ""
    vid_id = item.get("id") or item.get("videoId") or ""
    if not vid_id and "v=" in url_video:
        m = re.search(r"v=([^&]+)", url_video)
        if m:
            vid_id = m.group(1)

    titulo = item.get("title") or item.get("name") or ""
    views = parse_numero_str(item.get("views") or item.get("viewCount") or 0)
    likes = parse_numero_str(item.get("likes") or item.get("likeCount") or 0)
    comentarios = parse_numero_str(
        item.get("commentsCount") or item.get("commentCount") or item.get("comments") or 0
    )

    duracao = parse_duracao(item.get("duration") or item.get("durationSeconds") or 0)

    date_raw = (
        item.get("date")
        or item.get("publishedAt")
        or item.get("uploadDate")
        or item.get("uploadedAt")
        or ""
    )
    ts = parse_data_ts(date_raw)

    thumb_url = (
        item.get("thumbnailUrl")
        or item.get("thumbnail")
        or (f"https://i.ytimg.com/vi/{vid_id}/hqdefault.jpg" if vid_id else "")
    )

    link = url_video or (f"https://www.youtube.com/watch?v={vid_id}" if vid_id else "")

    return {
        "id": str(vid_id),
        "titulo": titulo,
        "create_time": ts,
        "views": views,
        "likes": likes,
        "comentarios": comentarios,
        "duracao": duracao,
        "thumbnail_url": thumb_url,
        "link": link,
        "engajamento": round((likes + comentarios) / views * 100, 2) if views > 0 else 0,
        "thumbnail_b64": "",
        "thumbnail_path": "",
    }


# ---------------------------------------------------------------------------
# Metricas
# ---------------------------------------------------------------------------

def calcular_metricas(videos: list) -> dict:
    if not videos:
        return {}
    total = len(videos)
    media_views = sum(v["views"] for v in videos) / total
    media_eng = sum(v["engajamento"] for v in videos) / total

    # Faixas de duracao YouTube: Short <=60s, curto 1-5min, medio 5-15min, longo 15min+
    faixas = {"short_60s": [], "curto_5min": [], "medio_15min": [], "longo": []}
    for v in videos:
        d = v["duracao"]
        if d <= 60:
            faixas["short_60s"].append(v)
        elif d <= 300:
            faixas["curto_5min"].append(v)
        elif d <= 900:
            faixas["medio_15min"].append(v)
        else:
            faixas["longo"].append(v)

    def med(lst, campo):
        return round(sum(x[campo] for x in lst) / len(lst), 2) if lst else 0

    desempenho_duracao = {
        k: {
            "count": len(lst),
            "media_views": round(med(lst, "views")),
            "media_eng": med(lst, "engajamento"),
        }
        for k, lst in faixas.items()
    }

    # Melhores dias para publicar (por dia da semana)
    dias_views: list = [[] for _ in range(7)]
    dias_eng: list = [[] for _ in range(7)]
    for v in videos:
        if v["create_time"]:
            dt = datetime.fromtimestamp(v["create_time"])
            dias_views[dt.weekday()].append(v["views"])
            dias_eng[dt.weekday()].append(v["engajamento"])

    melhores_dias = [
        {
            "dia": i,
            "media_views": round(sum(dias_views[i]) / len(dias_views[i])) if dias_views[i] else 0,
            "media_eng": round(sum(dias_eng[i]) / len(dias_eng[i]), 2) if dias_eng[i] else 0,
            "count": len(dias_views[i]),
        }
        for i in range(7)
    ]

    # Analise de titulos
    top_palavras = extrair_palavras_titulo(videos)

    # Tamanho do titulo vs views
    bucket_titulo: dict = {"curto": [], "medio": [], "longo": []}
    for v in videos:
        n = len(v["titulo"])
        if n <= 40:
            bucket_titulo["curto"].append(v["views"])
        elif n <= 70:
            bucket_titulo["medio"].append(v["views"])
        else:
            bucket_titulo["longo"].append(v["views"])
    titulo_views = {k: round(sum(vs) / len(vs)) if vs else 0 for k, vs in bucket_titulo.items()}
    titulo_counts = {k: len(vs) for k, vs in bucket_titulo.items()}

    # Semanas
    semanas: dict = defaultdict(list)
    for v in videos:
        if v["create_time"]:
            dt = datetime.fromtimestamp(v["create_time"])
            iso = dt.isocalendar()
            semanas[f"{iso[0]}-W{iso[1]:02d}"].append(v)
    semanas_data = [
        {
            "semana": k,
            "count": len(vs),
            "media_eng": round(sum(x["engajamento"] for x in vs) / len(vs), 2),
            "media_views": round(sum(x["views"] for x in vs) / len(vs)),
        }
        for k, vs in sorted(semanas.items())
    ]

    # Top 3 por views
    top3 = sorted(videos, key=lambda x: x["views"], reverse=True)[:3]

    # Timeline ordenada
    timeline = sorted(videos, key=lambda x: x["create_time"])

    return {
        "total_videos_coletados": total,
        "media_views": round(media_views),
        "media_engajamento": round(media_eng, 2),
        "total_likes": sum(v["likes"] for v in videos),
        "total_comentarios": sum(v["comentarios"] for v in videos),
        "desempenho_duracao": desempenho_duracao,
        "melhores_dias": melhores_dias,
        "top_palavras": top_palavras,
        "titulo_views": titulo_views,
        "titulo_counts": titulo_counts,
        "top3_ids": [v["id"] for v in top3],
        "semanas": semanas_data,
        "timeline_ids": [v["id"] for v in timeline],
    }


# ---------------------------------------------------------------------------
# Historico
# ---------------------------------------------------------------------------

def atualizar_historico(output_dir: Path, canal: dict, metricas: dict) -> list:
    hist_path = output_dir / "historico.json"
    historico = []
    if hist_path.exists():
        try:
            historico = json.loads(hist_path.read_text(encoding="utf-8"))
        except Exception:
            historico = []
    snapshot = {
        "data": datetime.now().strftime("%Y-%m-%d"),
        "timestamp": int(time.time()),
        "inscritos": canal.get("inscritos", 0),
        "media_engajamento": metricas.get("media_engajamento", 0),
        "media_views": metricas.get("media_views", 0),
    }
    if historico and historico[-1].get("data") == snapshot["data"]:
        historico[-1] = snapshot
    else:
        historico.append(snapshot)
    hist_path.write_text(json.dumps(historico, ensure_ascii=False, indent=2), encoding="utf-8")
    return historico


# ---------------------------------------------------------------------------
# Download de thumbnails
# ---------------------------------------------------------------------------

def baixar_thumbnails(videos: list, output_dir: Path, log: logging.Logger) -> list:
    imagens_dir = output_dir / "imagens"
    imagens_dir.mkdir(exist_ok=True)

    # Cache entre execucoes
    insights_path = output_dir / "insights.json"
    cache: dict = {}
    if insights_path.exists():
        try:
            ant = json.loads(insights_path.read_text(encoding="utf-8"))
            for v in ant.get("videos", []):
                if v.get("thumbnail_path"):
                    cache[v["id"]] = v["thumbnail_path"]
        except Exception:
            pass

    def baixar_um(video, idx):
        vid_id = video["id"] or str(idx)
        if vid_id in cache:
            rel = cache[vid_id]
            abs_path = output_dir / rel
            if abs_path.exists():
                b64 = base64.b64encode(abs_path.read_bytes()).decode()
                return idx, f"data:image/jpeg;base64,{b64}", rel
        url = video.get("thumbnail_url", "")
        if not url:
            return idx, "", ""
        try:
            resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            nome = f"video_{idx+1:02d}_{vid_id[:12]}.jpg"
            abs_path = imagens_dir / nome
            abs_path.write_bytes(resp.content)
            b64 = base64.b64encode(resp.content).decode()
            return idx, f"data:image/jpeg;base64,{b64}", f"imagens/{nome}"
        except Exception as e:
            log.warning(f"Falha thumbnail video {idx+1}: {e}")
            return idx, "", ""

    resultados = [""] * len(videos)
    caminhos = [""] * len(videos)
    with ThreadPoolExecutor(max_workers=WORKERS_DOWNLOAD) as ex:
        futuros = {ex.submit(baixar_um, v, i): i for i, v in enumerate(videos)}
        for fut in as_completed(futuros):
            idx, b64, caminho = fut.result()
            resultados[idx] = b64
            caminhos[idx] = caminho

    for i, v in enumerate(videos):
        v["thumbnail_b64"] = resultados[i]
        v["thumbnail_path"] = caminhos[i]
    return videos


# ---------------------------------------------------------------------------
# Salvar insights.json
# ---------------------------------------------------------------------------

def salvar_insights(output_dir: Path, canal: dict, videos: list, metricas: dict):
    dados = {
        "gerado_em": datetime.now().isoformat(),
        "canal": {k: val for k, val in canal.items() if k != "avatar_b64"},
        "videos": [{k: val for k, val in v.items() if k != "thumbnail_b64"} for v in videos],
        "metricas": metricas,
    }
    path = output_dir / "insights.json"
    path.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Geracao do HTML
# ---------------------------------------------------------------------------

def gerar_html(canal, videos, metricas, historico, canal_url, output_dir, log):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    nome_canal = canal.get("nome") or canal_url
    inicial = nome_canal[0].upper() if nome_canal else "Y"

    # Videos para JS
    videos_js = []
    for v in videos:
        videos_js.append({
            "id": v["id"],
            "titulo": v["titulo"][:200],
            "data": v["create_time"],
            "data_fmt": formatar_data(v["create_time"]),
            "views": v["views"],
            "views_fmt": formatar_numero(v["views"]),
            "likes": v["likes"],
            "likes_fmt": formatar_numero(v["likes"]),
            "comentarios": v["comentarios"],
            "duracao": v["duracao"],
            "duracao_fmt": formatar_duracao(v["duracao"]),
            "engajamento": v["engajamento"],
            "link": v["link"],
            "thumbnail_b64": v["thumbnail_b64"],
        })

    top3_ids = set(metricas.get("top3_ids", []))
    top3_videos = [v for v in videos_js if v["id"] in top3_ids][:3]

    nomes_faixas = {
        "short_60s": "Short (ate 60s)",
        "curto_5min": "Curto (1-5min)",
        "medio_15min": "Medio (5-15min)",
        "longo": "Longo (15min+)",
    }
    ordem_faixas = ["short_60s", "curto_5min", "medio_15min", "longo"]

    titulo_views = metricas.get("titulo_views", {"curto": 0, "medio": 0, "longo": 0})
    titulo_counts = metricas.get("titulo_counts", {"curto": 0, "medio": 0, "longo": 0})

    # Melhores dias
    dias_nomes = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
    melhores_dias = metricas.get("melhores_dias", [])
    dias_labels = json.dumps([dias_nomes[d["dia"]] for d in melhores_dias])
    dias_views_data = json.dumps([d["media_views"] for d in melhores_dias])

    # Timeline ordenada
    tl_ids = metricas.get("timeline_ids", [])
    tl_map = {v["id"]: v for v in videos_js}
    tl = [tl_map[i] for i in tl_ids if i in tl_map]

    tem_historico = "true" if len(historico) >= 2 else "false"

    hist_labels = json.dumps([h["data"] for h in historico])
    hist_ins = json.dumps([h["inscritos"] for h in historico])
    hist_eng = json.dumps([h["media_engajamento"] for h in historico])

    sem = metricas.get("semanas", [])
    sem_labels = json.dumps([s["semana"] for s in sem])
    sem_counts = json.dumps([s["count"] for s in sem])
    sem_eng = json.dumps([s["media_eng"] for s in sem])

    tl_labels = json.dumps([v["data_fmt"] for v in tl])
    tl_views = json.dumps([v["views"] for v in tl])
    tl_likes = json.dumps([v["likes"] for v in tl])
    tl_eng_js = json.dumps([v["engajamento"] for v in tl])
    tl_coments = json.dumps([v["comentarios"] for v in tl])

    top_palavras = json.dumps(metricas.get("top_palavras", []))
    videos_json = json.dumps(videos_js, ensure_ascii=False)

    # Views totais do canal (fallback: soma dos videos coletados)
    total_views = canal.get("total_views_canal") or sum(v["views"] for v in videos)

    # KPI de inscritos
    inscritos_fmt = formatar_numero(canal.get("inscritos", 0))

    badges = [("badge-gold", "#1"), ("badge-silver", "#2"), ("badge-bronze", "#3")]

    def top3_card(v, i):
        bc, bt = badges[i]
        thumb = (
            f'<img class="top3-thumb" src="{v["thumbnail_b64"]}" alt="thumb">'
            if v.get("thumbnail_b64")
            else '<div class="top3-thumb no-thumb">Sem imagem</div>'
        )
        tit = v["titulo"][:80] + "..." if len(v["titulo"]) > 80 else v["titulo"]
        link_tag = (
            f'<a class="vlink" href="{v["link"]}" target="_blank">Ver no YouTube</a>'
            if v.get("link") else ""
        )
        return (
            f'<div class="top3-card">{thumb}<div class="top3-body">'
            f'<span class="top3-badge {bc}">{bt} &mdash; {v["duracao_fmt"]}</span>'
            f'<div class="top3-titulo">{tit}</div>'
            f'<div class="top3-stats">'
            f'<span><b>{v["views_fmt"]}</b> views</span>'
            f'<span><b>{formatar_numero(v["likes"])}</b> likes</span>'
            f'<span><b>{formatar_numero(v["comentarios"])}</b> coment.</span>'
            f'<span><b>{v["engajamento"]:.1f}%</b> eng.</span>'
            f'</div>{link_tag}</div></div>'
        )

    top3_html = "\n".join(top3_card(v, i) for i, v in enumerate(top3_videos))

    duracao_cards = ""
    for k in ordem_faixas:
        d = metricas.get("desempenho_duracao", {}).get(k, {})
        mv = formatar_numero(d.get("media_views", 0))
        me = d.get("media_eng", 0)
        cnt = d.get("count", 0)
        duracao_cards += (
            f'<div class="dur-card">'
            f'<div class="dur-label">{nomes_faixas[k]}</div>'
            f'<div class="dur-views">{mv}</div>'
            f'<div class="dur-sub">media de views</div>'
            f'<div class="dur-sub">{me:.1f}% eng. &mdash; {cnt} videos</div>'
            f"</div>"
        )

    melhor_bucket = max(titulo_views, key=lambda k: titulo_views.get(k, 0))
    titulo_html = ""
    for k, label in [
        ("curto", "Curto (ate 40 char)"),
        ("medio", "Medio (41-70 char)"),
        ("longo", "Longo (71+ char)"),
    ]:
        destaque = "tit-destaque" if k == melhor_bucket else ""
        titulo_html += (
            f'<div class="tit-card {destaque}">'
            f'<div class="tit-label">{label}</div>'
            f'<div class="tit-val">{formatar_numero(titulo_views.get(k, 0))}</div>'
            f'<div class="tit-sub">media de views</div>'
            f'<div class="tit-sub">{titulo_counts.get(k, 0)} videos</div>'
            f"</div>"
        )

    avatar_tag = (
        f'<img class="avatar" src="{canal["avatar_b64"]}" alt="avatar">'
        if canal.get("avatar_b64")
        else f'<div class="avatar-fb">{inicial}</div>'
    )

    descricao = (canal.get("descricao") or "")[:200]
    data_criacao = canal.get("data_criacao") or ""
    data_criacao_html = f'<div class="data-criacao">Canal criado em: {data_criacao}</div>' if data_criacao else ""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>YouTube Dashboard - {nome_canal}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f8fafc;--sur:#fff;--bdr:#e2e8f0;--tx:#1e293b;--mu:#64748b;--ac:#dc2626;--acl:#fef2f2;--r:12px;--sh:0 1px 3px rgba(0,0,0,.08),0 4px 12px rgba(0,0,0,.04)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--tx);padding-bottom:80px}}
.topbar{{background:#0f0f0f;color:#fff;padding:14px 24px;display:flex;align-items:center;gap:12px;position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.3)}}
.topbar h1{{font-size:1.05rem;font-weight:600}}
.topbar .sub{{font-size:.78rem;color:#aaa;margin-left:auto}}
.wrap{{max-width:1280px;margin:0 auto;padding:20px 16px}}
.sec{{background:var(--sur);border-radius:var(--r);box-shadow:var(--sh);padding:20px;margin-bottom:18px}}
.sec-title{{font-size:.85rem;font-weight:600;color:var(--mu);text-transform:uppercase;letter-spacing:.06em;margin-bottom:14px}}
.profile-row{{display:flex;align-items:center;gap:18px}}
.avatar{{width:76px;height:76px;border-radius:50%;object-fit:cover;border:3px solid var(--bdr);flex-shrink:0}}
.avatar-fb{{width:76px;height:76px;border-radius:50%;background:linear-gradient(135deg,#dc2626,#7f1d1d);display:flex;align-items:center;justify-content:center;font-size:1.8rem;font-weight:700;color:#fff;flex-shrink:0}}
.profile-info h2{{font-size:1.3rem;font-weight:700}}
.handle{{color:var(--mu);font-size:.85rem;margin-bottom:4px;word-break:break-all}}
.bio{{font-size:.83rem;color:var(--mu);max-width:560px;line-height:1.45;margin-top:4px}}
.data-criacao{{font-size:.75rem;color:#94a3b8;margin-top:4px}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:14px}}
.kpi{{background:var(--acl);border-radius:10px;padding:14px;text-align:center}}
.kpi-v{{font-size:1.7rem;font-weight:700;color:var(--ac)}}
.kpi-l{{font-size:.75rem;color:var(--mu);margin-top:3px}}
.chart-row{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
@media(max-width:640px){{.chart-row{{grid-template-columns:1fr}}}}
canvas{{max-width:100%}}
.dur-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:12px}}
.dur-card{{border:1px solid var(--bdr);border-radius:10px;padding:12px;text-align:center}}
.dur-label{{font-size:.78rem;font-weight:600;color:var(--mu);margin-bottom:6px}}
.dur-views{{font-size:1.3rem;font-weight:700;color:var(--ac)}}
.dur-sub{{font-size:.72rem;color:var(--mu);margin-top:2px}}
.top3-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}}
.top3-card{{border:1px solid var(--bdr);border-radius:12px;overflow:hidden;transition:box-shadow .2s}}
.top3-card:hover{{box-shadow:0 4px 16px rgba(0,0,0,.1)}}
.top3-thumb{{width:100%;aspect-ratio:16/9;object-fit:cover;background:#e2e8f0;display:block}}
.no-thumb{{display:flex;align-items:center;justify-content:center;color:#94a3b8;font-size:.75rem}}
.top3-body{{padding:12px}}
.top3-badge{{display:inline-block;font-size:.7rem;font-weight:700;padding:2px 8px;border-radius:20px;margin-bottom:6px}}
.badge-gold{{background:#fef3c7;color:#92400e}}
.badge-silver{{background:#f1f5f9;color:#475569}}
.badge-bronze{{background:#fff7ed;color:#9a3412}}
.top3-titulo{{font-size:.85rem;color:var(--tx);font-weight:500;margin-bottom:8px;line-height:1.4}}
.top3-stats{{display:flex;flex-wrap:wrap;gap:6px;font-size:.76rem;color:var(--mu)}}
.top3-stats b{{color:var(--tx)}}
.vlink{{font-size:.76rem;color:var(--ac);text-decoration:none;display:block;margin-top:8px}}
.vlink:hover{{text-decoration:underline}}
.hb{{display:flex;align-items:center;gap:8px;margin-bottom:5px}}
.hb-name{{font-size:.8rem;color:var(--ac);min-width:110px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.hb-track{{flex:1;height:14px;background:var(--bdr);border-radius:7px;overflow:hidden}}
.hb-fill{{height:100%;background:linear-gradient(90deg,var(--ac),#f87171);border-radius:7px}}
.hb-val{{font-size:.75rem;color:var(--mu);min-width:40px;text-align:right}}
.tit-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}
.tit-card{{border:1px solid var(--bdr);border-radius:10px;padding:14px;text-align:center;transition:border-color .2s}}
.tit-destaque{{border-color:var(--ac);background:var(--acl)}}
.tit-label{{font-size:.78rem;color:var(--mu);margin-bottom:6px}}
.tit-val{{font-size:1.3rem;font-weight:700;color:var(--ac)}}
.tit-sub{{font-size:.72rem;color:#94a3b8;margin-top:2px}}
.filtros{{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:10px}}
.fb{{padding:5px 13px;border:1px solid var(--bdr);border-radius:20px;font-size:.78rem;cursor:pointer;background:var(--sur);transition:all .15s}}
.fb.on{{background:var(--ac);color:#fff;border-color:var(--ac)}}
.vg{{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}}
.vc{{border:1px solid var(--bdr);border-radius:10px;overflow:hidden;cursor:pointer;transition:box-shadow .2s}}
.vc:hover{{box-shadow:0 4px 14px rgba(0,0,0,.1)}}
.vt-wrap{{position:relative;aspect-ratio:16/9;background:#e2e8f0}}
.vt{{width:100%;height:100%;object-fit:cover;display:block}}
.vdur{{position:absolute;bottom:3px;right:5px;background:rgba(0,0,0,.75);color:#fff;font-size:.62rem;padding:1px 5px;border-radius:4px}}
.vi{{padding:8px}}
.vtit{{font-size:.78rem;color:var(--tx);font-weight:500;margin-bottom:4px;line-height:1.3;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
.vm{{font-size:.7rem;color:var(--mu);display:flex;flex-wrap:wrap;gap:3px;margin-top:2px}}
.vlink2{{font-size:.7rem;color:var(--ac);text-decoration:none}}
.freq-insight{{background:var(--acl);border-radius:10px;padding:12px;font-size:.85rem;color:var(--ac);margin-top:12px;font-weight:500}}
@media(max-width:480px){{.profile-row{{flex-direction:column;align-items:flex-start}}.tit-grid{{grid-template-columns:1fr}}.dur-grid{{grid-template-columns:1fr 1fr}}}}
</style>
</head>
<body>
<div class="topbar">
  <svg width="24" height="24" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z" fill="#ff0000"/></svg>
  <h1>YouTube Dashboard</h1>
  <span class="sub">Atualizado em {agora}</span>
</div>
<div class="wrap">

<!-- 1. Canal -->
<div class="sec">
  <div class="profile-row">
    {avatar_tag}
    <div class="profile-info">
      <h2>{nome_canal}</h2>
      <div class="handle">{canal_url}</div>
      <div class="bio">{descricao}</div>
      {data_criacao_html}
    </div>
  </div>
</div>

<!-- 2. KPIs -->
<div class="sec">
  <div class="sec-title">Visao Geral</div>
  <div class="kpi-grid">
    <div class="kpi"><div class="kpi-v">{inscritos_fmt}</div><div class="kpi-l">Inscritos</div></div>
    <div class="kpi"><div class="kpi-v">{formatar_numero(total_views)}</div><div class="kpi-l">Views Totais</div></div>
    <div class="kpi"><div class="kpi-v">{metricas.get("media_engajamento",0):.1f}%</div><div class="kpi-l">Engajamento Medio</div></div>
    <div class="kpi"><div class="kpi-v">{formatar_numero(metricas.get("media_views",0))}</div><div class="kpi-l">Media de Views</div></div>
    <div class="kpi"><div class="kpi-v">{metricas.get("total_videos_coletados",0)}</div><div class="kpi-l">Videos Analisados</div></div>
  </div>
</div>

<!-- 3. Evolucao -->
<div class="sec" id="sec-ev"{'' if len(historico)>=2 else ' style="display:none"'}>
  <div class="sec-title">Evolucao ao Longo do Tempo</div>
  <div class="chart-row">
    <div><canvas id="c-ins" height="170"></canvas></div>
    <div><canvas id="c-eh" height="170"></canvas></div>
  </div>
</div>

<!-- 4. Duracao -->
<div class="sec">
  <div class="sec-title">Desempenho por Duracao</div>
  <div class="dur-grid">{duracao_cards}</div>
</div>

<!-- 5. Melhores dias -->
<div class="sec">
  <div class="sec-title">Melhores Dias para Publicar</div>
  <canvas id="c-dias" height="170"></canvas>
</div>

<!-- 6. Frequencia -->
<div class="sec">
  <div class="sec-title">Frequencia de Publicacao</div>
  <canvas id="c-freq" height="150"></canvas>
  <div class="freq-insight" id="freq-insight"></div>
</div>

<!-- 7. Top 3 -->
<div class="sec">
  <div class="sec-title">Top 3 Videos por Views</div>
  <div class="top3-grid">{top3_html}</div>
</div>

<!-- 8. Analise de titulos -->
<div class="sec">
  <div class="sec-title">Analise de Titulos</div>
  <p style="font-size:.8rem;color:var(--mu);margin-bottom:12px">Palavras mais frequentes nos videos com mais views (top 50%):</p>
  <div id="palavras-container"></div>
</div>

<!-- 9. Tamanho do titulo vs views -->
<div class="sec">
  <div class="sec-title">Tamanho do Titulo vs Views</div>
  <div class="tit-grid">{titulo_html}</div>
</div>

<!-- 10. Timeline -->
<div class="sec">
  <div class="sec-title">Linha do Tempo</div>
  <div class="chart-row">
    <div><canvas id="c-tv" height="170"></canvas></div>
    <div><canvas id="c-te" height="170"></canvas></div>
  </div>
  <div class="chart-row" style="margin-top:14px">
    <div><canvas id="c-tl" height="170"></canvas></div>
    <div><canvas id="c-tc" height="170"></canvas></div>
  </div>
</div>

<!-- 11. Filtros -->
<div class="sec">
  <div class="sec-title">Filtrar Videos</div>
  <div class="filtros" id="fd">
    <button class="fb on" data-d="todos">Todos</button>
    <button class="fb" data-d="short_60s">Short (ate 60s)</button>
    <button class="fb" data-d="curto_5min">Curto (1-5min)</button>
    <button class="fb" data-d="medio_15min">Medio (5-15min)</button>
    <button class="fb" data-d="longo">Longo (15min+)</button>
  </div>
  <div class="filtros" id="fp">
    <button class="fb on" data-p="0">Todos</button>
    <button class="fb" data-p="7">Ultimos 7 dias</button>
    <button class="fb" data-p="15">Ultimos 15 dias</button>
    <button class="fb" data-p="30">Ultimos 30 dias</button>
  </div>
</div>

<!-- 12. Grade -->
<div class="sec">
  <div class="sec-title">Todos os Videos</div>
  <div class="vg" id="vg"></div>
</div>

</div>

<script>
const VD={videos_json};
const HL={hist_labels};const HI={hist_ins};const HE={hist_eng};
const TEM={tem_historico};
const SL={sem_labels};const SC={sem_counts};const SE={sem_eng};
const TL={tl_labels};const TV={tl_views};const TLk={tl_likes};const TE={tl_eng_js};const TC={tl_coments};
const DL={dias_labels};const DV={dias_views_data};
const TP={top_palavras};

function fmtN(n){{if(n>=1e6)return(n/1e6).toFixed(1)+'M';if(n>=1e3)return(n/1e3).toFixed(1)+'K';return String(n);}}

// Analise de titulos
(function(){{
  const c=document.getElementById('palavras-container');
  if(!TP.length){{c.innerHTML='<p style="color:#94a3b8;font-size:.83rem">Nenhuma palavra encontrada.</p>';return;}}
  const mx=Math.max(...TP.map(p=>p.count));
  c.innerHTML=TP.map(p=>{{
    const pct=mx>0?(p.count/mx*100).toFixed(1):0;
    return`<div class="hb"><span class="hb-name">${{p.palavra}}</span><div class="hb-track"><div class="hb-fill" style="width:${{pct}}%"></div></div><span class="hb-val">${{p.count}}x</span></div>`;
  }}).join('');
}})();

// Grade de videos
let curD='todos',curP=0;
function renderGrade(vids){{
  const g=document.getElementById('vg');
  g.innerHTML=vids.map(v=>{{
    const th=v.thumbnail_b64?`<img class="vt" src="${{v.thumbnail_b64}}" alt="">`:`<div class="vt" style="display:flex;align-items:center;justify-content:center;color:#94a3b8;font-size:.72rem;height:100%">Sem imagem</div>`;
    const lk=v.link?`<a class="vlink2" href="${{v.link}}" target="_blank">Ver no YouTube</a>`:'';
    const tit=v.titulo.length>70?v.titulo.substring(0,70)+'...':v.titulo;
    return`<div class="vc"><div class="vt-wrap">${{th}}<span class="vdur">${{v.duracao_fmt}}</span></div><div class="vi"><div class="vtit">${{tit}}</div><div class="vm"><span>👁 ${{v.views_fmt}}</span><span>👍 ${{v.likes_fmt}}</span><span>💬 ${{v.comentarios}}</span></div><div class="vm"><span>${{v.engajamento.toFixed(1)}}% eng.</span><span>${{v.data_fmt}}</span></div>${{lk}}</div></div>`;
  }}).join('');
}}

function filtrar(){{
  let vids=[...VD];
  if(curP>0){{const lim=Date.now()/1000-curP*86400;vids=vids.filter(v=>v.data>=lim);}}
  const ranges={{short_60s:[0,60],curto_5min:[61,300],medio_15min:[301,900],longo:[901,1e9]}};
  if(curD!=='todos'){{const[mn,mx]=ranges[curD]||[0,1e9];vids=vids.filter(v=>v.duracao>=mn&&v.duracao<=mx);}}
  renderGrade(vids);
  document.querySelectorAll('#fd .fb').forEach(b=>b.classList.toggle('on',b.dataset.d===curD));
  document.querySelectorAll('#fp .fb').forEach(b=>b.classList.toggle('on',parseInt(b.dataset.p)===curP));
}}
document.querySelectorAll('#fd .fb').forEach(b=>b.addEventListener('click',()=>{{curD=b.dataset.d;filtrar();}}));
document.querySelectorAll('#fp .fb').forEach(b=>b.addEventListener('click',()=>{{curP=parseInt(b.dataset.p);filtrar();}}));

// Insight de frequencia
(function(){{
  const el=document.getElementById('freq-insight');if(!el||!SC.length)return;
  const a2=SC.map((c,i)=>c>=2?SE[i]:null).filter(x=>x!==null);
  const ao=SC.map((c,i)=>c<2?SE[i]:null).filter(x=>x!==null);
  const avg=a=>a.length?(a.reduce((s,v)=>s+v,0)/a.length).toFixed(1):null;
  const v2=avg(a2),vo=avg(ao);
  el.textContent=v2&&vo?`Semanas com 2 ou mais videos tiveram ${{v2}}% de engajamento medio, contra ${{vo}}% nas semanas com menos uploads.`:v2?`Semanas com 2 ou mais videos: ${{v2}}% de engajamento medio.`:'Mantenha pelo menos 2 videos por semana para maximizar o engajamento.';
}})();

// Graficos canvas puro
function lineChart(id,labels,datasets,opts={{}}){{
  const cv=document.getElementById(id);if(!cv)return;
  const ctx=cv.getContext('2d');
  const W=cv.offsetWidth||480,H=cv.height||170;cv.width=W;
  const pad={{t:18,r:16,b:36,l:54}};
  const w=W-pad.l-pad.r,h=H-pad.t-pad.b;
  ctx.clearRect(0,0,W,H);
  const all=datasets.flatMap(d=>d.data).filter(v=>v!=null);
  if(!all.length)return;
  const minV=opts.min!=null?opts.min:Math.min(0,...all);
  const maxV=Math.max(...all)||1;const rng=maxV-minV||1;
  const xS=labels.length>1?w/(labels.length-1):w;
  const fmtY=opts.fmtY||(v=>v.toFixed(1));
  ctx.strokeStyle='#e2e8f0';ctx.lineWidth=1;
  for(let i=0;i<=4;i++){{const y=pad.t+(h/4)*i;ctx.beginPath();ctx.moveTo(pad.l,y);ctx.lineTo(pad.l+w,y);ctx.stroke();ctx.fillStyle='#94a3b8';ctx.font='10px Inter,sans-serif';ctx.textAlign='right';ctx.fillText(fmtY(maxV-(rng/4)*i),pad.l-3,y+4);}}
  const step=Math.ceil(labels.length/7);ctx.fillStyle='#94a3b8';ctx.font='10px Inter,sans-serif';ctx.textAlign='center';
  labels.forEach((l,i)=>{{if(i%step===0||i===labels.length-1)ctx.fillText(l,pad.l+i*xS,H-6);}});
  const colors=['#dc2626','#f59e0b','#10b981','#6366f1'];
  datasets.forEach((ds,di)=>{{
    const col=ds.color||colors[di%4];ctx.strokeStyle=col;ctx.lineWidth=2;ctx.lineJoin='round';ctx.beginPath();
    let st=false;ds.data.forEach((v,i)=>{{if(v==null)return;const x=pad.l+i*xS,y=pad.t+h-((v-minV)/rng)*h;st?(ctx.lineTo(x,y)):(ctx.moveTo(x,y),st=true);}});ctx.stroke();
    ctx.fillStyle=col;ds.data.forEach((v,i)=>{{if(v==null)return;const x=pad.l+i*xS,y=pad.t+h-((v-minV)/rng)*h;ctx.beginPath();ctx.arc(x,y,3,0,Math.PI*2);ctx.fill();}});
    if(ds.label){{ctx.fillStyle=col;ctx.font='10px Inter,sans-serif';ctx.textAlign='left';ctx.fillText(ds.label,pad.l,pad.t-4);}}
  }});
}}

function barChart(id,labels,vals,color){{
  const cv=document.getElementById(id);if(!cv)return;
  const ctx=cv.getContext('2d');const W=cv.offsetWidth||480,H=cv.height||170;cv.width=W;
  const pad={{t:16,r:16,b:44,l:52}};const w=W-pad.l-pad.r,h=H-pad.t-pad.b;
  ctx.clearRect(0,0,W,H);
  if(!vals.length)return;
  const mx=Math.max(...vals)||1;
  const fmtY=mx>=1000?v=>(v/1000).toFixed(0)+'K':v=>v.toFixed(0);
  const bw=w/vals.length*.7,gap=w/vals.length;
  ctx.strokeStyle='#e2e8f0';ctx.lineWidth=1;
  for(let i=0;i<=4;i++){{const y=pad.t+(h/4)*i;ctx.beginPath();ctx.moveTo(pad.l,y);ctx.lineTo(pad.l+w,y);ctx.stroke();ctx.fillStyle='#94a3b8';ctx.font='10px Inter,sans-serif';ctx.textAlign='right';ctx.fillText(fmtY(mx*(1-i/4)),pad.l-3,y+4);}}
  vals.forEach((v,i)=>{{const x=pad.l+i*gap+(gap-bw)/2,bh=(v/mx)*h,y=pad.t+h-bh;ctx.fillStyle=color||'#dc2626';ctx.beginPath();if(ctx.roundRect)ctx.roundRect(x,y,bw,bh,3);else ctx.rect(x,y,bw,bh);ctx.fill();ctx.fillStyle='#64748b';ctx.font='9px Inter,sans-serif';ctx.textAlign='center';ctx.fillText(labels[i]||'',x+bw/2,H-6);}});
}}

function renderAll(){{
  if(TEM&&HL.length>=2){{
    lineChart('c-ins',HL,[{{label:'Inscritos',data:HI,color:'#dc2626'}}],{{fmtY:v=>v>=1000?(v/1000).toFixed(1)+'K':v.toFixed(0)}});
    lineChart('c-eh',HL,[{{label:'Engajamento (%)',data:HE,color:'#f59e0b'}}],{{fmtY:v=>v.toFixed(1)+'%',min:0}});
  }}
  if(DL.length)barChart('c-dias',DL,DV,'#dc2626');
  if(SL.length)barChart('c-freq',SL,SC,'#6366f1');
  if(TL.length>1){{
    lineChart('c-tv',TL,[{{label:'Views',data:TV,color:'#dc2626'}}],{{fmtY:v=>v>=1000?(v/1000).toFixed(0)+'K':v.toFixed(0)}});
    lineChart('c-te',TL,[{{label:'Engajamento (%)',data:TE,color:'#f59e0b'}}],{{fmtY:v=>v.toFixed(1)+'%',min:0}});
    lineChart('c-tl',TL,[{{label:'Likes',data:TLk,color:'#10b981'}}],{{fmtY:v=>v>=1000?(v/1000).toFixed(0)+'K':v.toFixed(0)}});
    lineChart('c-tc',TL,[{{label:'Comentarios',data:TC,color:'#6366f1'}}],{{fmtY:v=>v>=1000?(v/1000).toFixed(0)+'K':v.toFixed(0)}});
  }}
}}

window.addEventListener('DOMContentLoaded',()=>{{renderGrade(VD);renderAll();}});
window.addEventListener('resize',renderAll);
</script>
</body>
</html>"""

    out_path = output_dir / "dashboard.html"
    out_path.write_text(html, encoding="utf-8")
    log.info(f"Dashboard salvo: {out_path}")
    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="YouTube Dashboard - Workshop Marketing IA")
    parser.add_argument("--abrir", action="store_true", help="Abre o dashboard no navegador ao terminar")
    parser.add_argument("--canal", help="URL ou @handle do canal (substitui YOUTUBE_CHANNEL do .env)")
    args = parser.parse_args()

    env = carregar_env()
    token = env.get("APIFY_API_TOKEN", "")
    canal_raw = args.canal or env.get("YOUTUBE_CHANNEL", "")

    if not token:
        print("ERRO: APIFY_API_TOKEN nao encontrado no .env")
        print("Configure em console.apify.com > Settings > Integrations > Personal API token")
        sys.exit(1)
    if not canal_raw:
        print("ERRO: YOUTUBE_CHANNEL nao encontrado no .env e nao foi passado via --canal")
        print("Exemplo: python atualizar.py --canal @meuperfil")
        sys.exit(1)

    canal_url = normalizar_canal_url(canal_raw)
    output_dir = get_output_dir()
    log = configurar_log(output_dir)
    log.info(f"=== YouTube Dashboard iniciado para {canal_url} ===")

    itens = chamar_apify(token, canal_url, log)
    if not itens:
        log.error("Nenhum item retornado. Verifique a URL do canal e o token.")
        sys.exit(1)

    log.info("Normalizando dados...")
    canal = normalizar_canal(itens)
    videos_raw = [normalizar_video(item) for item in itens[:MAX_VIDEOS]]
    # Filtra itens sem titulo (podem ser metadata do canal sem video)
    videos = [v for v in videos_raw if v["titulo"]]
    log.info(
        f"Canal: {canal.get('nome') or canal_url} "
        f"— {canal.get('inscritos', 0):,} inscritos "
        f"— {len(videos)} videos"
    )

    log.info("Baixando avatar do canal...")
    canal["avatar_b64"] = baixar_base64(canal.get("avatar_url", ""), log, "avatar")

    log.info("Baixando thumbnails...")
    videos = baixar_thumbnails(videos, output_dir, log)

    log.info("Calculando metricas...")
    metricas = calcular_metricas(videos)
    log.info(f"Engajamento medio: {metricas.get('media_engajamento', 0):.2f}%")

    historico = atualizar_historico(output_dir, canal, metricas)
    log.info(f"Historico: {len(historico)} snapshots")

    salvar_insights(output_dir, canal, videos, metricas)

    log.info("Gerando dashboard...")
    html_path = gerar_html(canal, videos, metricas, historico, canal_url, output_dir, log)
    log.info(f"=== Pronto: {html_path} ===")

    if args.abrir:
        import platform
        s = str(html_path)
        p = platform.system()
        if p == "Windows":
            os.startfile(s)
        elif p == "Darwin":
            os.system(f"open '{s}'")
        else:
            os.system(f"xdg-open '{s}'")


if __name__ == "__main__":
    main()
