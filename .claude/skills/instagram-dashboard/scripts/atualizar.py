#!/usr/bin/env python3
"""
Workshop Inteligente - Instagram Dashboard
Le APIFY_API_TOKEN e IG_USER do .env, coleta dados do perfil e gera dashboard.html
no produto ativo lido de meus-produtos/.ativo
"""

import os
import sys
import json
import base64
import time
import argparse
import logging
import webbrowser
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("Erro: biblioteca 'requests' nao encontrada.")
    print("Instale com: pip install requests")
    sys.exit(1)

# ── Logging basico (console) — FileHandler adicionado em main() apos resolver paths ──
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ── Raiz do projeto ───────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent

def encontrar_raiz():
    p = SCRIPT_DIR
    for _ in range(10):
        if (p / '.env').exists():
            return p
        p = p.parent
    return SCRIPT_DIR

PROJECT_ROOT = encontrar_raiz()
ENV_FILE = PROJECT_ROOT / '.env'

def get_output_dir() -> Path:
    ativo_file = PROJECT_ROOT / 'meus-produtos' / '.ativo'
    if not ativo_file.exists():
        log.error('meus-produtos/.ativo nao encontrado. Use /produto-novo para criar um produto.')
        sys.exit(1)
    ativo = ativo_file.read_text(encoding='utf-8').strip()
    if not ativo:
        log.error('meus-produtos/.ativo esta vazio.')
        sys.exit(1)
    output = PROJECT_ROOT / 'meus-produtos' / ativo / 'entregas' / 'instagram-dashboard'
    output.mkdir(parents=True, exist_ok=True)
    return output

# ── .env parser ───────────────────────────────────────────────────────────────
def ler_env():
    env = {}
    if ENV_FILE.exists():
        for linha in ENV_FILE.read_text(encoding='utf-8').splitlines():
            linha = linha.strip()
            if linha and not linha.startswith('#') and '=' in linha:
                k, _, v = linha.partition('=')
                env[k.strip()] = v.strip()
    env.update({k: v for k, v in os.environ.items()})
    return env

# ── Apify ────────────────────────────────────────────────────────────────────
SCRAPER_URL = 'https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items'

def apify_post(token, url_ator, payload, timeout=60, retries=3):
    url = f'{url_ator}?token={token}&timeout={timeout}'
    for tentativa in range(1, retries + 1):
        try:
            resp = requests.post(url, json=payload, timeout=timeout + 60)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            # Erros 4xx sao permanentes - nao retentar
            if e.response is not None and 400 <= e.response.status_code < 500:
                raise
            log.warning(f'  Apify erro HTTP {e.response.status_code if e.response else "?"} (tentativa {tentativa}/{retries}): {e}')
            if tentativa < retries:
                espera = tentativa * 10
                log.info(f'  Aguardando {espera}s antes de tentar novamente...')
                time.sleep(espera)
        except Exception as e:
            log.warning(f'  Apify erro (tentativa {tentativa}/{retries}): {e}')
            if tentativa < retries:
                espera = tentativa * 10
                log.info(f'  Aguardando {espera}s antes de tentar novamente...')
                time.sleep(espera)
    raise RuntimeError(f'Apify falhou apos {retries} tentativas')

def buscar_perfil(token, ig_user):
    log.info(f'Buscando perfil @{ig_user}...')
    data = apify_post(token, SCRAPER_URL, {
        'directUrls': [f'https://www.instagram.com/{ig_user}/'],
        'resultsType': 'details',
    }, timeout=60)
    if not data:
        raise ValueError('Apify nao retornou dados de perfil')
    return data[0]

def buscar_posts(token, ig_user):
    log.info(f'Buscando posts @{ig_user}...')
    limite = 30
    todos = []
    for tentativa in range(1, 5):
        log.info(f'  Tentativa {tentativa} — resultsLimit={limite}')
        data = apify_post(token, SCRAPER_URL, {
            'directUrls': [f'https://www.instagram.com/{ig_user}/'],
            'resultsType': 'posts',
            'resultsLimit': limite,
        }, timeout=600)
        if not data:
            break
        todos = data
        visiveis = [p for p in data if p.get('likesCount', -1) != -1]
        ocultos  = [p for p in data if p.get('likesCount', -1) == -1]
        log.info(f'  {len(data)} posts — {len(visiveis)} com likes visiveis, {len(ocultos)} ocultos')
        if len(visiveis) >= 30 or (len(data) >= 30 and len(ocultos) <= 5) or limite >= 100:
            # Prioriza posts com likes visiveis
            return visiveis[:30] + ocultos[:max(0, 30 - len(visiveis[:30]))]
        limite = min(limite + 30, 100)
    return todos[:30]

def baixar_b64(url, desc=''):
    if not url:
        return ''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.instagram.com/',
        }
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200:
            return base64.b64encode(resp.content).decode('utf-8')
    except Exception as e:
        log.warning(f'Falha ao baixar {desc}: {e}')
    return ''

def salvar_jpg(b64, caminho: Path):
    if b64:
        try:
            caminho.write_bytes(base64.b64decode(b64))
        except Exception as e:
            log.warning(f'Falha ao salvar {caminho}: {e}')

# ── Normalizacao ──────────────────────────────────────────────────────────────
def tipo_post(raw):
    t = str(raw.get('type', raw.get('productType', ''))).lower()
    if 'video' in t or 'reel' in t or raw.get('isVideo'):
        return 'Reel'
    if raw.get('childPosts') or 'carousel' in t or (isinstance(raw.get('images'), list) and len(raw['images']) > 1):
        return 'Carrossel'
    return 'Foto'

def normalizar_perfil(raw):
    return {
        'username':   raw.get('username', ''),
        'nome':       raw.get('fullName') or raw.get('username', ''),
        'bio':        raw.get('biography', ''),
        'seguidores': raw.get('followersCount', 0) or 0,
        'seguindo':   raw.get('followsCount', 0) or 0,
        'totalPosts': raw.get('postsCount', 0) or 0,
        'verificado': bool(raw.get('verified')),
        'fotoPerfil': '',
        '_picUrl':    raw.get('profilePicUrl') or raw.get('profilePicUrlHD', ''),
    }

def normalizar_post(raw):
    likes       = raw.get('likesCount', -1)
    comentarios = raw.get('commentsCount', 0) or 0
    views       = raw.get('videoViewCount') or raw.get('videoPlayCount') or 0

    # Imagens do carrossel
    imgs_url = []
    if raw.get('childPosts'):
        for cp in raw['childPosts']:
            u = cp.get('displayUrl', '')
            if u: imgs_url.append(u)
    elif isinstance(raw.get('images'), list):
        for img in raw['images']:
            u = img.get('src', img) if isinstance(img, dict) else img
            if u: imgs_url.append(u)

    # Data
    ts = raw.get('timestamp', '')
    data_str = ''
    if ts:
        try:
            dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
            data_str = dt.strftime('%d/%m/%Y')
        except Exception:
            data_str = ts[:10]

    sc = raw.get('shortCode') or raw.get('shortcode', '')
    url_post = f'https://www.instagram.com/p/{sc}/' if sc else raw.get('url', '')

    return {
        'shortCode':     sc,
        'tipo':          tipo_post(raw),
        'timestamp':     ts,
        'data':          data_str,
        'likes':         likes,
        'comentarios':   comentarios,
        'views':         views,
        'shares':        raw.get('sharesCount', 0) or 0,
        'legenda':       (raw.get('caption', '') or '')[:500],
        'url':           url_post,
        '_displayUrl':   raw.get('displayUrl', ''),
        '_imgsUrl':      imgs_url,
        '_videoUrl':     raw.get('videoUrl', ''),
        'imagem':        '',
        'imagens':       [],
        'thumbnailPath': '',
        'carouselPaths': [],
        'transcricao':   '',
        'engajamento':   0,
    }

# ── Metricas (extraido de gerar_html para reuso) ─────────────────────────────
def calcular_metricas(perfil, posts):
    seg = perfil['seguidores'] or 1
    for p in posts:
        likes = max(p['likes'], 0)
        p['engajamento'] = round((likes + p['comentarios']) / seg * 100, 2)

    def grupo(tipo): return [p for p in posts if p['tipo'] == tipo]
    reels      = grupo('Reel')
    carrosseis = grupo('Carrossel')
    fotos      = grupo('Foto')

    def media(lst, campo):
        vals = [max(p[campo], 0) for p in lst]
        return round(sum(vals) / len(vals), 1) if vals else 0

    eng_medio   = round(sum(p['engajamento'] for p in posts) / len(posts), 2) if posts else 0
    contagem    = {'Reel': len(reels), 'Carrossel': len(carrosseis), 'Foto': len(fotos)}
    formato_top = max(contagem, key=contagem.get) if posts else '-'

    return {
        'engMedio':   eng_medio,
        'formatoTop': formato_top,
        'totalShares': sum(p['shares'] for p in posts),
        'reels': {
            'count':            len(reels),
            'mediaLikes':       media(reels, 'likes'),
            'mediaComentarios': media(reels, 'comentarios'),
            'mediaShares':      media(reels, 'shares'),
            'totalViews':       sum(p['views'] for p in reels),
        },
        'carrosseis': {
            'count':            len(carrosseis),
            'mediaLikes':       media(carrosseis, 'likes'),
            'mediaComentarios': media(carrosseis, 'comentarios'),
            'mediaShares':      media(carrosseis, 'shares'),
        },
        'fotos': {
            'count':            len(fotos),
            'mediaLikes':       media(fotos, 'likes'),
            'mediaComentarios': media(fotos, 'comentarios'),
            'mediaShares':      media(fotos, 'shares'),
        },
    }

# ── Historico (snapshots acumulativos entre execucoes) ────────────────────────
def atualizar_historico(base_dir, perfil, metricas):
    hist_file = base_dir / 'historico.json'
    historico = []
    if hist_file.exists():
        try:
            historico = json.loads(hist_file.read_text(encoding='utf-8'))
            if not isinstance(historico, list):
                historico = []
        except Exception:
            historico = []
    hoje = datetime.now().strftime('%Y-%m-%d')
    username = perfil.get('username', '')
    snapshot = {
        'data':        datetime.now().isoformat(),
        'username':    username,
        'seguidores':  perfil['seguidores'],
        'engMedio':    metricas['engMedio'],
        'totalPosts':  perfil['totalPosts'],
        'totalShares': metricas['totalShares'],
    }
    # Substitui snapshot do mesmo perfil + mesmo dia em vez de duplicar
    historico = [h for h in historico if not (h.get('data', '')[:10] == hoje and h.get('username', '') == username)]
    historico.append(snapshot)
    hist_file.write_text(json.dumps(historico, ensure_ascii=False, indent=2), encoding='utf-8')
    # Retorna apenas snapshots do perfil atual
    hist_perfil = [h for h in historico if h.get('username', '') == username]
    log.info(f'historico.json atualizado ({len(historico)} snapshots, {len(hist_perfil)} do @{username})')
    return hist_perfil

# ── Dashboard HTML ────────────────────────────────────────────────────────────
def gerar_html(perfil, posts, metricas, historico=None):
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')
    top3        = sorted(posts, key=lambda p: p['engajamento'], reverse=True)[:3]
    cronologico = sorted([p for p in posts if p['timestamp']], key=lambda p: p['timestamp'])

    # Campos limpos para JSON (sem _internos)
    def limpar_post(p):
        return {k: v for k, v in p.items() if not k.startswith('_')}

    dados_js = json.dumps({
        'perfil':            perfil,
        'posts':             [limpar_post(p) for p in posts],
        'top3':              [limpar_post(p) for p in top3],
        'postsCronologicos': [limpar_post(p) for p in cronologico],
        'metricas':          metricas,
        'historico':         historico or [],
        'atualizadoEm':      agora,
    }, ensure_ascii=False, default=str)

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Instagram</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#f8fafc;--card:#fff;--border:#e2e8f0;--text:#1e293b;--muted:#64748b;
  --accent:#4338ca;--accent-lt:#eef2ff;
  --reel:#7c3aed;--carrossel:#0369a1;--foto:#059669;
  --sh:0 1px 3px rgba(0,0,0,.08),0 1px 2px rgba(0,0,0,.04);
  --sh-md:0 4px 6px -1px rgba(0,0,0,.07);
  --r:12px;--r-sm:8px
}}
body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text)}}
.wrap{{max-width:1200px;margin:0 auto;padding:24px 16px}}
.hdr{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:24px;display:flex;align-items:center;gap:20px;margin-bottom:24px;box-shadow:var(--sh)}}
.avatar{{width:72px;height:72px;border-radius:50%;border:3px solid var(--accent);flex-shrink:0;background:var(--accent-lt);display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700;color:var(--accent);overflow:hidden}}
.avatar img{{width:100%;height:100%;object-fit:cover}}
.hinfo h1{{font-size:20px;font-weight:700}}
.hinfo .un{{color:var(--accent);font-size:14px;font-weight:500}}
.hinfo .bio{{color:var(--muted);font-size:13px;margin-top:4px;line-height:1.4}}
.hinfo .upd{{font-size:12px;color:var(--muted);margin-top:6px}}
.kpi-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}}
.kpi{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;box-shadow:var(--sh)}}
.kpi-lbl{{font-size:11px;font-weight:500;color:var(--muted);text-transform:uppercase;letter-spacing:.5px}}
.kpi-val{{font-size:28px;font-weight:700;margin-top:4px}}
.kpi-sub{{font-size:12px;color:var(--muted);margin-top:2px}}
.kpi-accent .kpi-val{{color:var(--accent)}}
.fmt-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}}
.fmt-card{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;box-shadow:var(--sh)}}
.fmt-nome{{font-size:14px;font-weight:700;margin-bottom:12px;display:flex;align-items:center;gap:8px}}
.dot{{width:10px;height:10px;border-radius:50%}}
.dot-r{{background:var(--reel)}}.dot-c{{background:var(--carrossel)}}.dot-f{{background:var(--foto)}}
.mets{{display:flex;gap:16px;flex-wrap:wrap}}
.met-lbl{{font-size:11px;color:var(--muted)}}
.met-val{{font-size:18px;font-weight:700}}
.sec{{font-size:16px;font-weight:700;margin-bottom:16px}}
.top3-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}}
.t3c{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);overflow:hidden;box-shadow:var(--sh)}}
.t3c img,.t3c .t3ph{{width:100%;aspect-ratio:1;object-fit:cover;display:block;background:var(--accent-lt)}}
.t3c .t3ph{{display:flex;align-items:center;justify-content:center;font-size:12px;color:var(--muted)}}
.t3b{{padding:12px}}
.badge{{display:inline-block;padding:2px 8px;border-radius:99px;font-size:11px;font-weight:600;margin-bottom:8px}}
.br{{background:#f3e8ff;color:var(--reel)}}.bc{{background:#e0f2fe;color:var(--carrossel)}}.bf{{background:#d1fae5;color:var(--foto)}}
.t3stats{{display:flex;gap:10px;font-size:13px;flex-wrap:wrap;margin-bottom:4px}}
.t3sv{{font-weight:700}}
.t3eng{{font-size:13px;font-weight:600;color:var(--accent)}}
.vlink{{display:inline-block;margin-top:6px;font-size:12px;color:var(--accent);text-decoration:none;font-weight:500}}
.vlink:hover{{text-decoration:underline}}
.chart-card{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;margin-bottom:24px;box-shadow:var(--sh)}}
.ch-title{{font-size:13px;font-weight:600;color:var(--muted);margin-bottom:8px}}
.ch-legend{{display:flex;gap:14px;margin-bottom:8px;flex-wrap:wrap}}
.leg{{display:flex;align-items:center;gap:5px;font-size:12px}}
.ldot{{width:10px;height:10px;border-radius:50%}}
canvas{{width:100%!important;display:block}}
.pg{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px;margin-bottom:24px}}
.pc{{background:var(--card);border:1px solid var(--border);border-radius:var(--r-sm);overflow:hidden;box-shadow:var(--sh)}}
.pw{{position:relative;width:100%;aspect-ratio:1;background:var(--accent-lt);cursor:pointer}}
.pw img{{width:100%;height:100%;object-fit:cover;display:block}}
.ci{{position:absolute;bottom:6px;right:6px;background:rgba(0,0,0,.55);color:#fff;font-size:10px;padding:2px 6px;border-radius:99px}}
.pb{{padding:10px}}
.pstats{{display:flex;gap:8px;font-size:12px;flex-wrap:wrap}}
.psv{{font-weight:700}}
.pdata{{font-size:11px;color:var(--muted);margin-top:3px}}
.pleg{{font-size:11px;color:var(--muted);margin-top:3px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}}
.hist-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:24px}}
.hist-card{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;box-shadow:var(--sh)}}
.heatmap-wrap{{overflow-x:auto;margin-bottom:24px}}
.heatmap{{display:grid;grid-template-columns:48px repeat(24,1fr);gap:2px;min-width:600px}}
.hm-lbl{{font-size:10px;color:var(--muted);display:flex;align-items:center;justify-content:center}}
.hm-cell{{aspect-ratio:1;border-radius:4px;position:relative;cursor:default;min-width:16px}}
.hm-cell:hover .hm-tip{{display:block}}
.hm-tip{{display:none;position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);background:#1e293b;color:#fff;padding:5px 8px;border-radius:6px;font-size:11px;white-space:nowrap;z-index:10;pointer-events:none}}
.freq-wrap{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;margin-bottom:24px;box-shadow:var(--sh)}}
.freq-bars{{display:flex;align-items:flex-end;gap:4px;height:120px;margin-top:12px}}
.freq-bar{{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:2px;min-width:0;height:100%}}
.freq-bar-inner{{width:100%;border-radius:4px 4px 0 0;transition:height .3s}}
.freq-bar-lbl{{font-size:9px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%;text-align:center}}
.freq-insight{{font-size:13px;color:var(--muted);margin-top:12px;line-height:1.5}}
.hash-wrap{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;margin-bottom:24px;box-shadow:var(--sh)}}
.hash-row{{display:flex;align-items:center;gap:10px;margin-bottom:8px}}
.hash-tag{{font-size:12px;font-weight:600;min-width:120px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.hash-bar-wrap{{flex:1;height:20px;background:var(--accent-lt);border-radius:4px;overflow:hidden}}
.hash-bar{{height:100%;background:var(--accent);border-radius:4px;transition:width .3s}}
.hash-stat{{font-size:11px;color:var(--muted);white-space:nowrap;min-width:100px}}
.cap-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:8px}}
.cap-card{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;text-align:center;box-shadow:var(--sh)}}
.cap-label{{font-size:12px;color:var(--muted);margin-bottom:4px}}
.cap-val{{font-size:24px;font-weight:700;color:var(--accent)}}
.cap-count{{font-size:11px;color:var(--muted);margin-top:2px}}
.cap-insight{{font-size:13px;color:var(--muted);margin-bottom:24px;line-height:1.5}}
.filter-bar{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px;align-items:center}}
.filter-group{{display:flex;gap:4px;align-items:center}}
.filter-group-lbl{{font-size:11px;color:var(--muted);font-weight:600;margin-right:4px;text-transform:uppercase;letter-spacing:.5px}}
.fbtn{{padding:5px 14px;border-radius:99px;border:1px solid var(--border);background:var(--card);font-size:12px;font-weight:500;cursor:pointer;transition:all .15s;font-family:inherit;color:var(--text)}}
.fbtn:hover{{border-color:var(--accent);color:var(--accent)}}
.fbtn.active{{background:var(--accent);color:#fff;border-color:var(--accent)}}
@media(max-width:768px){{
  .kpi-grid{{grid-template-columns:repeat(2,1fr)}}
  .fmt-grid,.top3-grid,.hist-grid,.cap-grid{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>
<div class="wrap">
  <div id="app"></div>
</div>
<script>
const D={dados_js};
let filterState={{type:'all',period:'all'}};

function fmt(n){{
  if(n===undefined||n===null||n<0)return'--';
  if(n>=1e6)return(n/1e6).toFixed(1)+'M';
  if(n>=1000)return(n/1000).toFixed(1)+'k';
  return n.toLocaleString('pt-BR');
}}
function bc(tipo){{return tipo==='Reel'?'br':tipo==='Carrossel'?'bc':'bf'}}
function dc(tipo){{return tipo==='Reel'?'dot-r':tipo==='Carrossel'?'dot-c':'dot-f'}}

function getFilteredPosts(){{
  let list=D.posts.slice();
  if(filterState.type!=='all'){{
    list=list.filter(p=>p.tipo===filterState.type);
  }}
  if(filterState.period!=='all'){{
    const days=parseInt(filterState.period,10);
    const cutoff=new Date();
    cutoff.setDate(cutoff.getDate()-days);
    list=list.filter(p=>{{
      if(!p.timestamp)return false;
      return new Date(p.timestamp)>=cutoff;
    }});
  }}
  list.sort((a,b)=>new Date(b.timestamp)-new Date(a.timestamp));
  return list;
}}

function recalcKPIs(posts){{
  const seg=D.perfil.seguidores||1;
  const total=posts.length;
  if(!total)return{{engMedio:0,totalShares:0,count:total}};
  const engMedio=Math.round(posts.reduce((s,p)=>s+p.engajamento,0)/total*100)/100;
  const totalShares=posts.reduce((s,p)=>s+(p.shares||0),0);
  return{{engMedio,totalShares,count:total}};
}}

function render(){{
  const{{perfil:p,posts,top3,postsCronologicos:crono,metricas:m,atualizadoEm}}=D;
  const fotoSrc=p.fotoPerfil?`data:image/jpeg;base64,${{p.fotoPerfil}}`:'';
  const avInner=fotoSrc?`<img src="${{fotoSrc}}" alt="">`:`${{(p.nome||p.username||'?')[0].toUpperCase()}}`;

  document.getElementById('app').innerHTML=`
  <div class="hdr">
    <div class="avatar">${{avInner}}</div>
    <div class="hinfo">
      <h1>${{p.nome||p.username}}${{p.verificado?' <svg style="display:inline-block;vertical-align:middle;margin-left:6px" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="10" cy="10" r="10" fill="#4338ca"/><path d="M6 10.5l2.5 2.5 5.5-5.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>':''}}</h1>
      <div class="un">@${{p.username}}</div>
      ${{p.bio?`<div class="bio">${{p.bio}}</div>`:''}}
      <div class="upd">Atualizado em ${{atualizadoEm}}</div>
    </div>
  </div>

  <div class="kpi-grid" id="kpiGrid">
    <div class="kpi"><div class="kpi-lbl">Seguidores</div><div class="kpi-val">${{fmt(p.seguidores)}}</div><div class="kpi-sub">${{fmt(p.seguindo)}} seguindo</div></div>
    <div class="kpi kpi-accent"><div class="kpi-lbl">Engajamento medio</div><div class="kpi-val" id="kpiEng">${{m.engMedio}}%</div><div class="kpi-sub">${{m.totalShares>0?fmt(m.totalShares)+' shares totais':'baseado em likes e comentarios'}}</div></div>
    <div class="kpi"><div class="kpi-lbl">Total de posts</div><div class="kpi-val" id="kpiCount">${{fmt(p.totalPosts)}}</div><div class="kpi-sub">no perfil</div></div>
    <div class="kpi"><div class="kpi-lbl">Formato mais postado</div><div class="kpi-val" style="font-size:22px">${{m.formatoTop}}</div><div class="kpi-sub">ultimos ${{posts.length}} posts</div></div>
  </div>

  <div id="historicoSection"></div>

  <div class="sec">Desempenho por Formato</div>
  <div class="fmt-grid">
    <div class="fmt-card">
      <div class="fmt-nome"><span class="dot dot-r"></span>Reels (${{m.reels.count}})</div>
      <div class="mets">
        <div><div class="met-lbl">Media de likes</div><div class="met-val">${{fmt(m.reels.mediaLikes)}}</div></div>
        <div><div class="met-lbl">Media comentarios</div><div class="met-val">${{fmt(m.reels.mediaComentarios)}}</div></div>
        <div><div class="met-lbl">Views totais</div><div class="met-val">${{fmt(m.reels.totalViews)}}</div></div>
        ${{m.reels.mediaShares>0?'<div><div class="met-lbl">Media de shares</div><div class="met-val">'+fmt(m.reels.mediaShares)+'</div></div>':''}}
      </div>
    </div>
    <div class="fmt-card">
      <div class="fmt-nome"><span class="dot dot-c"></span>Carrosseis (${{m.carrosseis.count}})</div>
      <div class="mets">
        <div><div class="met-lbl">Media de likes</div><div class="met-val">${{fmt(m.carrosseis.mediaLikes)}}</div></div>
        <div><div class="met-lbl">Media comentarios</div><div class="met-val">${{fmt(m.carrosseis.mediaComentarios)}}</div></div>
        ${{m.carrosseis.mediaShares>0?'<div><div class="met-lbl">Media de shares</div><div class="met-val">'+fmt(m.carrosseis.mediaShares)+'</div></div>':''}}
      </div>
    </div>
    <div class="fmt-card">
      <div class="fmt-nome"><span class="dot dot-f"></span>Fotos (${{m.fotos.count}})</div>
      <div class="mets">
        <div><div class="met-lbl">Media de likes</div><div class="met-val">${{fmt(m.fotos.mediaLikes)}}</div></div>
        <div><div class="met-lbl">Media comentarios</div><div class="met-val">${{fmt(m.fotos.mediaComentarios)}}</div></div>
        ${{m.fotos.mediaShares>0?'<div><div class="met-lbl">Media de shares</div><div class="met-val">'+fmt(m.fotos.mediaShares)+'</div></div>':''}}
      </div>
    </div>
  </div>

  <div id="heatmapSection"></div>
  <div id="frequencySection"></div>

  <div class="sec">Top 3 Posts</div>
  <div class="top3-grid" id="top3Grid">
    ${{top3.map(t=>`
    <div class="t3c">
      ${{t.imagem?`<img src="data:image/jpeg;base64,${{t.imagem}}" alt="">`:`<div class="t3ph">Sem imagem</div>`}}
      <div class="t3b">
        <span class="badge ${{bc(t.tipo)}}">${{t.tipo}}</span>
        <div class="t3stats">
          <span><span class="t3sv">${{fmt(t.likes)}}</span> likes</span>
          <span><span class="t3sv">${{fmt(t.comentarios)}}</span> com.</span>
          ${{t.tipo==='Reel'?`<span><span class="t3sv">${{fmt(t.views)}}</span> views</span>`:''}}
          <span><span class="t3sv">${{fmt(t.shares)}}</span> shares</span>
        </div>
        <div class="t3eng">${{t.engajamento}}% engajamento</div>
        ${{t.url?`<a class="vlink" href="${{t.url}}" target="_blank">Ver post original</a>`:''}}
      </div>
    </div>`).join('')}}
  </div>

  <div id="hashtagSection"></div>
  <div id="captionSection"></div>

  <div class="chart-card">
    <div class="sec" style="margin-bottom:12px">Linha do Tempo</div>
    <div class="ch-legend">
      <div class="leg"><div class="ldot" style="background:var(--reel)"></div>Reels</div>
      <div class="leg"><div class="ldot" style="background:var(--carrossel)"></div>Carrossel</div>
      <div class="leg"><div class="ldot" style="background:var(--foto)"></div>Foto</div>
    </div>
    <div class="ch-title">Curtidas</div>
    <canvas id="cLikes" height="120"></canvas>
    <div class="ch-title" style="margin-top:20px">Visualizacoes (Reels)</div>
    <canvas id="cViews" height="80"></canvas>
    <div class="ch-title" style="margin-top:20px">Engajamento (%)</div>
    <canvas id="cEng" height="80"></canvas>
    ${{posts.some(p=>p.shares>0)?'<div class="ch-title" style="margin-top:20px">Compartilhamentos</div><canvas id="cShares" height="80"></canvas>':''}}
  </div>

  <div id="filterBar"></div>
  <div class="sec" id="postsTitle">Todos os Posts (${{posts.length}})</div>
  <div class="pg" id="postsGrid"></div>
  `;

  renderFilterBar();
  renderPosts(posts);
  renderHistorico();
  renderHeatmap();
  renderFrequency();
  renderHashtags();
  renderCaptionAnalysis();
  setTimeout(renderCharts,100);
}}

function renderFilterBar(){{
  const el=document.getElementById('filterBar');
  if(!el)return;
  el.innerHTML=`
  <div class="filter-bar">
    <div class="filter-group">
      <span class="filter-group-lbl">Tipo</span>
      <button class="fbtn ${{filterState.type==='all'?'active':''}}" data-ft="all">Todos</button>
      <button class="fbtn ${{filterState.type==='Reel'?'active':''}}" data-ft="Reel">Reel</button>
      <button class="fbtn ${{filterState.type==='Carrossel'?'active':''}}" data-ft="Carrossel">Carrossel</button>
      <button class="fbtn ${{filterState.type==='Foto'?'active':''}}" data-ft="Foto">Foto</button>
    </div>
    <div class="filter-group">
      <span class="filter-group-lbl">Periodo</span>
      <button class="fbtn ${{filterState.period==='all'?'active':''}}" data-fp="all">Todos</button>
      <button class="fbtn ${{filterState.period==='7'?'active':''}}" data-fp="7">7 dias</button>
      <button class="fbtn ${{filterState.period==='15'?'active':''}}" data-fp="15">15 dias</button>
      <button class="fbtn ${{filterState.period==='30'?'active':''}}" data-fp="30">30 dias</button>
    </div>
  </div>`;
  el.querySelectorAll('[data-ft]').forEach(btn=>{{
    btn.addEventListener('click',()=>{{
      filterState.type=btn.getAttribute('data-ft');
      applyFilters();
    }});
  }});
  el.querySelectorAll('[data-fp]').forEach(btn=>{{
    btn.addEventListener('click',()=>{{
      filterState.period=btn.getAttribute('data-fp');
      applyFilters();
    }});
  }});
}}

function applyFilters(){{
  const filtered=getFilteredPosts();
  const kpis=recalcKPIs(filtered);
  const kpiEng=document.getElementById('kpiEng');
  if(kpiEng)kpiEng.textContent=kpis.engMedio+'%';
  const title=document.getElementById('postsTitle');
  if(title)title.textContent='Todos os Posts ('+filtered.length+')';
  const grid=document.getElementById('postsGrid');
  if(grid)grid.innerHTML='';
  renderPosts(filtered);
  const top3Filtered=filtered.slice().sort((a,b)=>b.engajamento-a.engajamento).slice(0,3);
  const t3g=document.getElementById('top3Grid');
  if(t3g){{
    t3g.innerHTML=top3Filtered.map(t=>`
    <div class="t3c">
      ${{t.imagem?`<img src="data:image/jpeg;base64,${{t.imagem}}" alt="">`:`<div class="t3ph">Sem imagem</div>`}}
      <div class="t3b">
        <span class="badge ${{bc(t.tipo)}}">${{t.tipo}}</span>
        <div class="t3stats">
          <span><span class="t3sv">${{fmt(t.likes)}}</span> likes</span>
          <span><span class="t3sv">${{fmt(t.comentarios)}}</span> com.</span>
          ${{t.tipo==='Reel'?`<span><span class="t3sv">${{fmt(t.views)}}</span> views</span>`:''}}
          <span><span class="t3sv">${{fmt(t.shares)}}</span> shares</span>
        </div>
        <div class="t3eng">${{t.engajamento}}% engajamento</div>
        ${{t.url?`<a class="vlink" href="${{t.url}}" target="_blank">Ver post original</a>`:''}}
      </div>
    </div>`).join('');
  }}
  renderFilterBar();
}}

function renderPosts(posts){{
  const grid=document.getElementById('postsGrid');
  if(!grid)return;
  posts.forEach((post,idx)=>{{
    const div=document.createElement('div');
    div.className='pc';
    const allB64=[];
    if(post.imagem)allB64.push(post.imagem);
    (post.imagens||[]).forEach(b=>{{if(b)allB64.push(b)}});
    const multi=allB64.length>1;
    let cur=0;
    const uid='fp'+Math.random().toString(36).slice(2,8);
    div.innerHTML=`
    <div class="pw" id="pw${{uid}}">
      ${{allB64.length?`<img id="pimg${{uid}}" src="data:image/jpeg;base64,${{allB64[0]}}" alt="">`:`<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:11px;color:var(--muted)">Sem imagem</div>`}}
      ${{multi?`<span class="ci" id="pci${{uid}}">1/${{allB64.length}}</span>`:''}}
    </div>
    <div class="pb">
      <span class="badge ${{bc(post.tipo)}}">${{post.tipo}}</span>
      <div class="pstats">
        <span><span class="psv">${{fmt(post.likes)}}</span> likes</span>
        <span><span class="psv">${{fmt(post.comentarios)}}</span> com.</span>
        ${{post.tipo==='Reel'?`<span><span class="psv">${{fmt(post.views)}}</span> views</span>`:''}}
        <span><span class="psv">${{fmt(post.shares||0)}}</span> shares</span>
      </div>
      <div class="pdata">${{post.data||''}}</div>
      ${{post.legenda?`<div class="pleg">${{post.legenda.substring(0,120)}}</div>`:''}}
      ${{post.url?`<a class="vlink" href="${{post.url}}" target="_blank">Ver post original</a>`:''}}
    </div>`;
    if(multi){{
      div.querySelector('.pw').addEventListener('click',()=>{{
        cur=(cur+1)%allB64.length;
        document.getElementById('pimg'+uid).src='data:image/jpeg;base64,'+allB64[cur];
        document.getElementById('pci'+uid).textContent=(cur+1)+'/'+allB64.length;
      }});
    }}
    grid.appendChild(div);
  }});
}}

function renderHistorico(){{
  const el=document.getElementById('historicoSection');
  if(!el)return;
  const h=D.historico;
  if(!h||h.length<2)return;
  el.innerHTML=`
    <div class="sec">Evolucao Historica</div>
    <div class="hist-grid">
      <div class="hist-card">
        <div class="ch-title">Seguidores ao longo do tempo</div>
        <canvas id="cHistSeg" height="100"></canvas>
      </div>
      <div class="hist-card">
        <div class="ch-title">Engajamento medio ao longo do tempo</div>
        <canvas id="cHistEng" height="100"></canvas>
      </div>
    </div>`;
  setTimeout(()=>{{
    drawHistLine('cHistSeg',h,d=>d.seguidores);
    drawHistLine('cHistEng',h,d=>d.engMedio);
  }},120);
}}

function drawHistLine(canvasId,data,getVal){{
  const canvas=document.getElementById(canvasId);
  if(!canvas||!data.length)return;
  canvas.width=canvas.parentElement.offsetWidth||400;
  const W=canvas.width,H=canvas.height;
  const PAD={{t:10,r:16,b:28,l:52}};
  const cw=W-PAD.l-PAD.r,ch=H-PAD.t-PAD.b;
  const ctx=canvas.getContext('2d');
  ctx.clearRect(0,0,W,H);
  const vals=data.map(d=>getVal(d));
  const maxV=Math.max(...vals,1);
  const minV=Math.min(...vals,0);
  const range=maxV-minV||1;
  const xStep=data.length>1?cw/(data.length-1):0;
  ctx.strokeStyle='#e2e8f0';ctx.lineWidth=1;
  for(let i=0;i<=3;i++){{
    const y=PAD.t+ch*(1-i/3);
    ctx.beginPath();ctx.moveTo(PAD.l,y);ctx.lineTo(PAD.l+cw,y);ctx.stroke();
  }}
  ctx.fillStyle='#64748b';ctx.font='11px Inter,sans-serif';ctx.textAlign='right';
  [0,0.5,1].forEach(f=>{{
    const v=minV+range*f;
    const y=PAD.t+ch*(1-f);
    ctx.fillText(fmt(Math.round(v*100)/100),PAD.l-5,y+4);
  }});
  ctx.strokeStyle='#4338ca';ctx.lineWidth=2;
  ctx.beginPath();
  data.forEach((d,i)=>{{
    const x=PAD.l+i*xStep;
    const y=PAD.t+ch*(1-(getVal(d)-minV)/range);
    i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);
  }});
  ctx.stroke();
  ctx.fillStyle='#4338ca';
  data.forEach((d,i)=>{{
    const x=PAD.l+i*xStep;
    const y=PAD.t+ch*(1-(getVal(d)-minV)/range);
    ctx.beginPath();ctx.arc(x,y,3,0,Math.PI*2);ctx.fill();
  }});
  ctx.fillStyle='#64748b';ctx.font='10px Inter,sans-serif';
  ctx.textAlign='left';
  const fmtDate=iso=>{{
    try{{return new Date(iso).toLocaleDateString('pt-BR',{{day:'2-digit',month:'2-digit'}})}}
    catch(e){{return''}}
  }};
  ctx.fillText(fmtDate(data[0].data),PAD.l,H-6);
  ctx.textAlign='right';
  ctx.fillText(fmtDate(data[data.length-1].data),PAD.l+cw,H-6);
}}

function renderHeatmap(){{
  const el=document.getElementById('heatmapSection');
  if(!el)return;
  const posts=D.posts;
  if(!posts.length)return;
  const dias=['Seg','Ter','Qua','Qui','Sex','Sab','Dom'];
  const grid=Array.from({{length:7}},()=>Array.from({{length:24}},()=>({{count:0,totalEng:0}})));
  posts.forEach(p=>{{
    if(!p.timestamp)return;
    const dt=new Date(p.timestamp);
    const day=(dt.getDay()+6)%7;
    const hour=dt.getHours();
    grid[day][hour].count++;
    grid[day][hour].totalEng+=p.engajamento||0;
  }});
  let maxAvg=0;
  grid.forEach(row=>row.forEach(cell=>{{
    if(cell.count>0){{
      const avg=cell.totalEng/cell.count;
      if(avg>maxAvg)maxAvg=avg;
    }}
  }}));
  if(!maxAvg)maxAvg=1;
  let html='<div class="sec">Melhores Horarios para Postar</div><div class="heatmap-wrap"><div class="heatmap">';
  html+='<div class="hm-lbl"></div>';
  for(let h=0;h<24;h++)html+=`<div class="hm-lbl">${{h}}</div>`;
  for(let d=0;d<7;d++){{
    html+=`<div class="hm-lbl">${{dias[d]}}</div>`;
    for(let h=0;h<24;h++){{
      const cell=grid[d][h];
      if(cell.count===0){{
        html+=`<div class="hm-cell" style="background:var(--accent-lt)"><div class="hm-tip">Nenhum post</div></div>`;
      }}else{{
        const avg=Math.round(cell.totalEng/cell.count*100)/100;
        const opacity=Math.max(0.15,avg/maxAvg);
        html+=`<div class="hm-cell" style="background:rgba(67,56,202,${{opacity.toFixed(2)}})"><div class="hm-tip">${{cell.count}} post${{cell.count>1?'s':''}} | ${{avg}}% eng</div></div>`;
      }}
    }}
  }}
  html+='</div></div>';
  el.innerHTML=html;
}}

function getISOWeek(d){{
  const dt=new Date(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate()));
  const dayNum=dt.getUTCDay()||7;
  dt.setUTCDate(dt.getUTCDate()+4-dayNum);
  const yearStart=new Date(Date.UTC(dt.getUTCFullYear(),0,1));
  return Math.ceil(((dt-yearStart)/86400000+1)/7);
}}

function renderFrequency(){{
  const el=document.getElementById('frequencySection');
  if(!el)return;
  const posts=D.posts.filter(p=>p.timestamp);
  if(!posts.length)return;
  const weeks={{}};
  posts.forEach(p=>{{
    const dt=new Date(p.timestamp);
    const yr=dt.getFullYear();
    const wk=getISOWeek(dt);
    const key=yr+'-W'+String(wk).padStart(2,'0');
    if(!weeks[key])weeks[key]={{count:0,totalEng:0,label:key}};
    weeks[key].count++;
    weeks[key].totalEng+=p.engajamento||0;
  }});
  const sorted=Object.values(weeks).sort((a,b)=>a.label.localeCompare(b.label));
  if(!sorted.length)return;
  const maxCount=Math.max(...sorted.map(w=>w.count),1);
  const highWeeks=sorted.filter(w=>w.count>=4);
  const lowWeeks=sorted.filter(w=>w.count<4);
  const avgHigh=highWeeks.length?Math.round(highWeeks.reduce((s,w)=>s+w.totalEng/w.count,0)/highWeeks.length*100)/100:0;
  const avgLow=lowWeeks.length?Math.round(lowWeeks.reduce((s,w)=>s+w.totalEng/w.count,0)/lowWeeks.length*100)/100:0;
  let bars=sorted.map(w=>{{
    const pct=Math.round(w.count/maxCount*100);
    const avg=w.count?Math.round(w.totalEng/w.count*100)/100:0;
    const shortLbl=w.label.split('-')[1];
    const px=Math.max(Math.round(pct/100*100),6);
    return`<div class="freq-bar"><div class="freq-bar-inner" style="height:${{px}}px;background:var(--accent)" title="${{w.count}} posts, ${{avg}}% eng"></div><div class="freq-bar-lbl">${{shortLbl}}</div></div>`;
  }}).join('');
  let insight='';
  if(highWeeks.length>0&&lowWeeks.length>0){{
    insight=`<div class="freq-insight">Semanas com 4+ posts: ${{avgHigh}}% engajamento medio vs ${{avgLow}}% com menos posts.</div>`;
  }}
  el.innerHTML=`<div class="freq-wrap"><div class="sec" style="margin-bottom:4px">Frequencia de Postagem</div><div class="freq-bars">${{bars}}</div>${{insight}}</div>`;
}}

function renderHashtags(){{
  const el=document.getElementById('hashtagSection');
  if(!el)return;
  const posts=D.posts;
  const tagMap={{}};
  posts.forEach(p=>{{
    const tags=(p.legenda||'').match(/#[\\w\\u00C0-\\u024F]+/g);
    if(!tags)return;
    tags.forEach(tag=>{{
      const t=tag.toLowerCase();
      if(!tagMap[t])tagMap[t]={{tag:t,totalEng:0,count:0}};
      tagMap[t].count++;
      tagMap[t].totalEng+=p.engajamento||0;
    }});
  }});
  const all=Object.values(tagMap).filter(t=>t.count>=1);
  if(!all.length){{
    el.innerHTML='<div class="hash-wrap"><div class="sec">Analise de Hashtags</div><div style="font-size:13px;color:var(--muted)">Nenhuma hashtag encontrada</div></div>';
    return;
  }}
  all.forEach(t=>t.avgEng=Math.round(t.totalEng/t.count*100)/100);
  const top10=all.sort((a,b)=>b.avgEng-a.avgEng).slice(0,10);
  const maxEng=top10[0].avgEng||1;
  const rows=top10.map(t=>{{
    const pct=Math.round(t.avgEng/maxEng*100);
    return`<div class="hash-row"><div class="hash-tag">${{t.tag}}</div><div class="hash-bar-wrap"><div class="hash-bar" style="width:${{pct}}%"></div></div><div class="hash-stat">${{t.avgEng}}% eng, ${{t.count}} post${{t.count>1?'s':''}}</div></div>`;
  }}).join('');
  el.innerHTML=`<div class="hash-wrap"><div class="sec">Analise de Hashtags (Top 10)</div>${{rows}}</div>`;
}}

function renderCaptionAnalysis(){{
  const el=document.getElementById('captionSection');
  if(!el)return;
  const posts=D.posts;
  const buckets={{curta:{{posts:[],label:'Curta (<100)'}},media:{{posts:[],label:'Media (100-300)'}},longa:{{posts:[],label:'Longa (300+)'}}}};
  posts.forEach(p=>{{
    const len=(p.legenda||'').length;
    if(len<100)buckets.curta.posts.push(p);
    else if(len<=300)buckets.media.posts.push(p);
    else buckets.longa.posts.push(p);
  }});
  const results=Object.entries(buckets).map(([k,v])=>{{
    const avg=v.posts.length?Math.round(v.posts.reduce((s,p)=>s+p.engajamento,0)/v.posts.length*100)/100:0;
    return{{key:k,label:v.label,avg,count:v.posts.length}};
  }});
  const withPosts=results.filter(r=>r.count>0);
  let insight='';
  if(withPosts.length>=2){{
    const best=withPosts.reduce((a,b)=>a.avg>b.avg?a:b);
    const worst=withPosts.reduce((a,b)=>a.avg<b.avg?a:b);
    if(best.key!==worst.key){{
      insight=`<div class="cap-insight">Legendas "${{best.label.split('(')[0].trim().toLowerCase()}}" tem ${{best.avg}}% de engajamento medio, contra ${{worst.avg}}% das "${{worst.label.split('(')[0].trim().toLowerCase()}}".</div>`;
    }}
  }}
  const cards=results.map(r=>`<div class="cap-card"><div class="cap-label">${{r.label}}</div><div class="cap-val">${{r.avg}}%</div><div class="cap-count">${{r.count}} post${{r.count!==1?'s':''}}</div></div>`).join('');
  el.innerHTML=`<div class="sec">Tamanho de Legenda vs Engajamento</div><div class="cap-grid">${{cards}}</div>${{insight}}`;
}}

function renderCharts(){{
  const posts=D.postsCronologicos;
  if(!posts.length)return;
  const COR={{Reel:'#7c3aed',Carrossel:'#0369a1',Foto:'#059669'}};

  function draw(canvasId,getVal){{
    const canvas=document.getElementById(canvasId);
    if(!canvas)return;
    canvas.width=canvas.parentElement.offsetWidth||800;
    const W=canvas.width,H=canvas.height;
    const PAD={{t:10,r:20,b:28,l:52}};
    const cw=W-PAD.l-PAD.r,ch=H-PAD.t-PAD.b;
    const ctx=canvas.getContext('2d');
    ctx.clearRect(0,0,W,H);

    ctx.strokeStyle='#e2e8f0';ctx.lineWidth=1;
    for(let i=0;i<=4;i++){{
      const y=PAD.t+ch*(1-i/4);
      ctx.beginPath();ctx.moveTo(PAD.l,y);ctx.lineTo(PAD.l+cw,y);ctx.stroke();
    }}

    const series=['Reel','Carrossel','Foto'].map(tipo=>{{
      return{{tipo,pts:posts.filter(p=>p.tipo===tipo).map(p=>{{return{{ts:p.timestamp,v:getVal(p)}}}})}}
    }}).filter(s=>s.pts.length>0);

    const allV=series.flatMap(s=>s.pts.map(pt=>pt.v));
    const maxV=Math.max(...allV,1);
    const allTs=posts.map(p=>p.timestamp).sort();
    const t0=new Date(allTs[0]),t1=new Date(allTs[allTs.length-1]);
    const tRange=t1-t0||1;

    const xOf=ts=>PAD.l+((new Date(ts)-t0)/tRange)*cw;
    const yOf=v=>PAD.t+ch*(1-v/maxV);

    ctx.fillStyle='#64748b';ctx.font='11px Inter,sans-serif';ctx.textAlign='right';
    [0,0.5,1].forEach(f=>{{
      const v=maxV*f;
      ctx.fillText(fmt(v),PAD.l-5,yOf(v)+4);
    }});

    ctx.textAlign='left';
    const fd=ts=>new Date(ts).toLocaleDateString('pt-BR',{{day:'2-digit',month:'2-digit'}});
    ctx.fillText(fd(allTs[0]),PAD.l,H-6);
    ctx.textAlign='right';
    ctx.fillText(fd(allTs[allTs.length-1]),PAD.l+cw,H-6);

    series.forEach(s=>{{
      const cor=COR[s.tipo]||'#999';
      ctx.strokeStyle=cor;ctx.fillStyle=cor;ctx.lineWidth=2;
      ctx.beginPath();
      s.pts.forEach((pt,i)=>{{
        const x=xOf(pt.ts),y=yOf(pt.v);
        i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);
      }});
      ctx.stroke();
      s.pts.forEach(pt=>{{
        ctx.beginPath();ctx.arc(xOf(pt.ts),yOf(pt.v),4,0,Math.PI*2);ctx.fill();
      }});
    }});

    canvas._s=series;canvas._xOf=xOf;canvas._yOf=yOf;canvas._COR=COR;
    if(!canvas._tt){{
      canvas._tt=true;
      canvas.addEventListener('mousemove',e=>ttMove(canvas,e));
      canvas.addEventListener('mouseleave',ttHide);
    }}
  }}

  draw('cLikes',p=>Math.max(p.likes,0));
  draw('cViews',p=>p.views||0);
  draw('cEng',p=>p.engajamento||0);
  draw('cShares',p=>p.shares||0);
}}

let ttEl=null;
function ttMove(canvas,e){{
  const r=canvas.getBoundingClientRect();
  const mx=e.clientX-r.left,my=e.clientY-r.top;
  let closest=null,minD=20;
  canvas._s.forEach(s=>s.pts.forEach(pt=>{{
    const x=canvas._xOf(pt.ts),y=canvas._yOf(pt.v);
    const d=Math.hypot(mx-x,my-y);
    if(d<minD){{minD=d;closest={{...pt,tipo:s.tipo}};}}
  }}));
  if(!closest)return ttHide();
  if(!ttEl){{
    ttEl=document.createElement('div');
    ttEl.style.cssText='position:fixed;background:#1e293b;color:#fff;padding:7px 11px;border-radius:8px;font-size:12px;font-family:Inter,sans-serif;pointer-events:none;z-index:9999';
    document.body.appendChild(ttEl);
  }}
  const dt=new Date(closest.ts).toLocaleDateString('pt-BR',{{day:'2-digit',month:'2-digit',year:'2-digit'}});
  ttEl.innerHTML=`<b style="color:${{canvas._COR[closest.tipo]||'#fff'}}">${{closest.tipo}}</b><br>${{fmt(closest.v)}} | ${{dt}}`;
  ttEl.style.display='block';
  ttEl.style.left=(e.clientX+14)+'px';
  ttEl.style.top=(e.clientY-10)+'px';
}}
function ttHide(){{if(ttEl)ttEl.style.display='none';}}

window.addEventListener('load',render);
window.addEventListener('resize',()=>{{if(typeof renderCharts==='function')renderCharts();}});
</script>
</body>
</html>'''

# ── Download paralelo de imagens ─────────────────────────────────────────────
def _baixar_post_imgs(args):
    """Baixa thumbnail e slides de um post. Chamado em paralelo via ThreadPoolExecutor."""
    i, post, images_dir = args
    result = {'imagem': '', 'thumbnailPath': '', 'imagens': [], 'carouselPaths': []}

    b64 = baixar_b64(post['_displayUrl'], f'thumb post {i+1}')
    result['imagem'] = b64
    if b64:
        thumb_path = images_dir / f'post_{i+1:02d}_thumb.jpg'
        salvar_jpg(b64, thumb_path)
        result['thumbnailPath'] = f'imagens/post_{i+1:02d}_thumb.jpg'

    carousel_b64, carousel_paths = [], []
    for j, img_url in enumerate(post['_imgsUrl'][:10]):
        b = baixar_b64(img_url, f'slide {j+1} post {i+1}')
        if b:
            carousel_b64.append(b)
            sp = images_dir / f'post_{i+1:02d}_slide_{j+1:02d}.jpg'
            salvar_jpg(b, sp)
            carousel_paths.append(f'imagens/post_{i+1:02d}_slide_{j+1:02d}.jpg')
    result['imagens']       = carousel_b64
    result['carouselPaths'] = carousel_paths
    return i, result

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--abrir', action='store_true')
    args = parser.parse_args()

    # Resolver caminhos de output a partir do produto ativo
    base_dir      = get_output_dir()
    env = ler_env()
    ig_user = env.get('IG_USER', '')
    token   = env.get('APIFY_API_TOKEN', '')

    # Subpasta por perfil (cada @ tem seus proprios arquivos)
    output_dir    = base_dir / ig_user if ig_user else base_dir
    images_dir    = output_dir / 'imagens'
    log_file      = output_dir / 'log.txt'
    insights_file = output_dir / 'insights.json'
    dashboard_file = output_dir / 'dashboard.html'
    images_dir.mkdir(parents=True, exist_ok=True)

    # Adicionar FileHandler ao logger agora que temos o caminho
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logging.getLogger().addHandler(file_handler)

    log.info('=== Iniciando atualizacao do dashboard Instagram ===')
    log.info(f'Output: {output_dir}')

    if not token:
        log.error('APIFY_API_TOKEN nao encontrado no .env'); sys.exit(1)
    if not ig_user:
        log.error('IG_USER nao encontrado no .env'); sys.exit(1)

    log.info(f'Perfil: @{ig_user}')

    # Perfil
    raw_perfil = buscar_perfil(token, ig_user)
    perfil     = normalizar_perfil(raw_perfil)
    log.info('Baixando foto de perfil...')
    perfil['fotoPerfil'] = baixar_b64(perfil['_picUrl'], 'foto de perfil')

    # Posts (aguarda 5s para o plano gratuito Apify liberar concorrencia)
    log.info('Aguardando 5s antes de buscar posts...')
    time.sleep(5)
    raw_posts = buscar_posts(token, ig_user)
    log.info(f'{len(raw_posts)} posts selecionados')
    posts = [normalizar_post(r) for r in raw_posts]

    # Imagens — download paralelo (5 workers, CDN do Instagram suporta sem rate limit)
    log.info(f'Baixando imagens de {len(posts)} posts em paralelo...')
    args_list = [(i, post, images_dir) for i, post in enumerate(posts)]
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(_baixar_post_imgs, a): a[0] for a in args_list}
        for future in as_completed(futures):
            i, result = future.result()
            posts[i].update(result)
            log.info(f'  Post {i+1}/{len(posts)} concluido')

    # Preservar transcricoes do insights.json anterior (geradas pelo /copy-variacao-post)
    transcricoes_prev = {}
    if insights_file.exists():
        try:
            prev = json.loads(insights_file.read_text(encoding='utf-8'))
            for p in prev.get('posts', []):
                sc = p.get('shortCode', '')
                tr = p.get('transcricao', '')
                if sc and tr:
                    transcricoes_prev[sc] = tr
            if transcricoes_prev:
                log.info(f'Preservando {len(transcricoes_prev)} transcricao(oes) do insights.json anterior')
        except Exception:
            pass

    # Metricas (antes do insights.json para engajamento estar calculado)
    metricas = calcular_metricas(perfil, posts)

    # insights.json (sem base64)
    def slim(p):
        s = {k: v for k, v in p.items() if k not in ('imagem', 'imagens') and not k.startswith('_')}
        # Restaurar transcricao anterior se existir e a nova estiver vazia
        sc = s.get('shortCode', '')
        if sc and not s.get('transcricao') and sc in transcricoes_prev:
            s['transcricao'] = transcricoes_prev[sc]
        return s
    insights = {
        'perfil':       {k: v for k, v in perfil.items() if not k.startswith('_') and k != 'fotoPerfil'},
        'posts':        [slim(p) for p in posts],
        'atualizadoEm': datetime.now().isoformat(),
    }
    insights_file.write_text(json.dumps(insights, ensure_ascii=False, indent=2, default=str), encoding='utf-8')
    log.info('insights.json salvo')
    historico = atualizar_historico(base_dir, perfil, metricas)

    # dashboard.html
    log.info('Gerando dashboard.html...')
    html = gerar_html(perfil, posts, metricas, historico)
    dashboard_file.write_text(html, encoding='utf-8')
    log.info(f'dashboard.html salvo: {dashboard_file}')

    log.info('=== Concluido com sucesso ===')

    if args.abrir:
        webbrowser.open(dashboard_file.as_uri())
        log.info('Dashboard aberto no navegador')

if __name__ == '__main__':
    main()
