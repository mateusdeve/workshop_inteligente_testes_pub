#!/usr/bin/env python3
"""
atualizar.py — Instagram Dashboard (versao Python, cross-platform)
Equivalente ao atualizar.ps1. Roda em Windows, macOS e Linux com Python 3.8+.

Uso:
    python3 atualizar.py           # gera dashboard.html + insights.json
    python3 atualizar.py --abrir   # gera e abre no navegador

Dependencia unica:
    pip install requests
"""

import argparse
import base64
import json
import math
import re
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("Erro: biblioteca 'requests' nao encontrada.")
    print("Instale com:  pip install requests")
    sys.exit(1)

# ---------------------------------------------------------------------------
# CONFIG — lido do .env na raiz do projeto
# ---------------------------------------------------------------------------
def _load_env() -> dict:
    env_file = Path(__file__).resolve().parent.parent.parent / ".env"
    env: dict = {}
    try:
        with open(env_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    return env

_env        = _load_env()
APIFY_TOKEN = _env.get("APIFY_API_TOKEN", "")
IG_USER     = _env.get("IG_USER", "")

if not APIFY_TOKEN:
    print("Erro: APIFY_API_TOKEN nao encontrado no .env")
    print("Configure com /configurar-apify ou adicione ao .env: APIFY_API_TOKEN=seu_token")
    sys.exit(1)
if not IG_USER:
    print("Erro: IG_USER nao encontrado no .env")
    print("Configure com /instagram-dashboard ou adicione ao .env: IG_USER=seu_usuario")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).resolve().parent
DASHBOARD  = SCRIPT_DIR / "dashboard.html"
LOG_FILE   = SCRIPT_DIR / "log.txt"
INSIGHTS   = SCRIPT_DIR / "insights.json"
IMG_DIR    = SCRIPT_DIR / "imagens"
IG_URL     = f"https://www.instagram.com/{IG_USER}/"

HEADERS_IMG = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.instagram.com/",
}

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    ts   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def img64(url: str) -> str:
    if not url:
        return ""
    try:
        r = requests.get(url, headers=HEADERS_IMG, timeout=30)
        r.raise_for_status()
        return "data:image/jpeg;base64," + base64.b64encode(r.content).decode()
    except Exception:
        return ""


def save_b64(b64: str, file_path: Path) -> bool:
    if not b64:
        return False
    try:
        clean = re.sub(r"^data:[^;]+;base64,", "", b64)
        file_path.write_bytes(base64.b64decode(clean))
        return True
    except Exception:
        return False


def transcribe(video_url: str) -> str:
    if not video_url:
        return ""
    try:
        resp = requests.post(
            f"https://api.apify.com/v2/acts/apify~whisper-speech-to-text"
            f"/run-sync-get-dataset-items?token={APIFY_TOKEN}&timeout=120",
            json={"urls": [video_url], "language": "pt"},
            timeout=150,
        )
        data = resp.json()
        if data and isinstance(data, list) and data[0].get("text"):
            return data[0]["text"].strip()
        return ""
    except Exception:
        return ""


def apify_scrape(results_type: str, limit: int, api_timeout: int, http_timeout: int) -> list:
    resp = requests.post(
        f"https://api.apify.com/v2/acts/apify~instagram-scraper"
        f"/run-sync-get-dataset-items?token={APIFY_TOKEN}&timeout={api_timeout}",
        json={"directUrls": [IG_URL], "resultsType": results_type, "resultsLimit": limit},
        timeout=http_timeout,
    )
    resp.raise_for_status()
    return resp.json() or []


def avg_round(total: float, count: int) -> int:
    return round(total / count) if count > 0 else 0


def fmt_num(v) -> str:
    v = float(v or 0)
    if v >= 1_000_000:
        return f"{v / 1_000_000:.1f}M"
    if v >= 1_000:
        return f"{v / 1_000:.1f}K"
    return str(int(v))


# ---------------------------------------------------------------------------
# HTML TEMPLATE
# ---------------------------------------------------------------------------
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Instagram Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',sans-serif;background:#f5f7fa;color:#1a1a2e;min-height:100vh}
.wrap{max-width:1200px;margin:0 auto;padding:24px 16px}
.hdr{background:#fff;border-radius:16px;padding:24px;display:flex;align-items:flex-start;gap:20px;margin-bottom:24px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.av-wrap{flex-shrink:0}
.av-wrap img{width:80px;height:80px;border-radius:50%;object-fit:cover}
.av-init{width:80px;height:80px;border-radius:50%;background:#e0e7ff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700;color:#4f46e5}
.hdr-info h1{font-size:1.2rem;font-weight:700;margin-bottom:4px}
.vbadge{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;background:#0095f6;border-radius:50%;color:#fff;font-size:9px;margin-left:5px;vertical-align:middle}
.bio{font-size:.85rem;color:#555;line-height:1.55;max-width:600px;margin-top:4px}
.upd{font-size:.72rem;color:#bbb;margin-top:8px}
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
.kpi{background:#fff;border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.kpi-lbl{font-size:.7rem;color:#888;text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px}
.kpi-val{font-size:1.6rem;font-weight:700;color:#1a1a2e;line-height:1.2}
.kpi-sub{font-size:.7rem;color:#ccc;margin-top:3px}
.sec{font-size:.95rem;font-weight:600;color:#1a1a2e;margin-bottom:16px}
.fmt-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}
.fmt-card{background:#fff;border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.fmt-head{display:flex;align-items:center;gap:8px;font-size:.875rem;font-weight:600;margin-bottom:12px}
.dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.dr{background:#9333ea}.dc{background:#2563eb}.df{background:#16a34a}
.fmt-line{display:flex;justify-content:space-between;font-size:.8rem;color:#555;padding:5px 0;border-bottom:1px solid #f0f0f0}
.fmt-line:last-child{border-bottom:none}
.fmt-line b{color:#1a1a2e;font-weight:600}
.fmt-empty{font-size:.8rem;color:#ccc;text-align:center;padding:16px 0}
.top3-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}
.t3{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.t3-img{width:100%;height:180px;object-fit:cover;display:block;background:#f0f0f0}
.t3-noimg{width:100%;height:180px;display:flex;align-items:center;justify-content:center;background:#f5f5f5;color:#ccc;font-size:.8rem}
.t3-body{padding:14px}
.bdg{display:inline-block;padding:2px 8px;border-radius:20px;font-size:.68rem;font-weight:600;margin-bottom:8px}
.br{background:#f3e8ff;color:#7c3aed}.bc{background:#dbeafe;color:#1d4ed8}.bf{background:#dcfce7;color:#15803d}
.t3-stats{display:flex;flex-wrap:wrap;gap:10px;font-size:.78rem;color:#555}
.t3-eng{font-size:.78rem;font-weight:700;color:#f97316;margin-top:6px}
.t3-cap{font-size:.72rem;color:#aaa;margin-top:6px;line-height:1.4;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.t3-link{font-size:.72rem;color:#0095f6;text-decoration:none;display:inline-block;margin-top:8px}
.t3-link:hover{text-decoration:underline}
.chart-card{background:#fff;border-radius:16px;padding:24px;margin-bottom:24px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.ch-blk{margin-bottom:28px}
.ch-blk:last-child{margin-bottom:0}
.ch-ttl{font-size:.85rem;font-weight:600;margin-bottom:8px}
.ch-leg{display:flex;gap:14px;margin-bottom:10px;flex-wrap:wrap}
.leg{display:flex;align-items:center;gap:5px;font-size:.72rem;color:#666}
.ldot{width:8px;height:8px;border-radius:50%}
canvas{width:100%;display:block;cursor:crosshair}
.pgrd{display:grid;grid-template-columns:repeat(auto-fill,minmax(185px,1fr));gap:14px;margin-bottom:32px}
.pc{background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.06);cursor:pointer;transition:transform .15s}
.pc:hover{transform:translateY(-2px)}
.pt{position:relative;width:100%;padding-top:100%;overflow:hidden;background:#f0f0f0}
.pt img{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover}
.pi{position:absolute;bottom:6px;right:6px;background:rgba(0,0,0,.55);color:#fff;font-size:.62rem;padding:2px 6px;border-radius:10px;pointer-events:none}
.pb{padding:10px}
.pmeta{display:flex;flex-wrap:wrap;gap:6px;font-size:.75rem;color:#555;margin-top:4px}
.pdate{font-size:.68rem;color:#ccc;margin-top:3px}
.pcap{font-size:.7rem;color:#aaa;margin-top:4px;line-height:1.35;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.plink{font-size:.68rem;color:#0095f6;text-decoration:none;display:inline-block;margin-top:5px}
.plink:hover{text-decoration:underline}
@media(max-width:900px){.kpi-row{grid-template-columns:repeat(2,1fr)}.fmt-row{grid-template-columns:1fr 1fr}.top3-row{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.kpi-row{grid-template-columns:1fr 1fr}.fmt-row{grid-template-columns:1fr}.top3-row{grid-template-columns:1fr}.pgrd{grid-template-columns:repeat(2,1fr)}.hdr{flex-direction:column;align-items:center;text-align:center}}
</style>
</head>
<body>
<div class="wrap" id="root"></div>
<script>const DATA=__JSON__;</script>
<script>
(function(){
var D=DATA,p=D.profile,posts=D.posts||[],fs=D.formatStats||{};
var flw=Math.max(1,p.followersCount||1);
function N(v){return v==null?0:+v;}
function FN(v){v=+v;if(v>=1e6)return(v/1e6).toFixed(1)+"M";if(v>=1e3)return(v/1e3).toFixed(1)+"K";return ""+v;}
function BC(t){return t==="Reels"?"br":t==="Carrossel"?"bc":"bf";}
function DC(t){return t==="Reels"?"dr":t==="Carrossel"?"dc":"df";}
var avH=p.profilePicBase64
  ?'<div class="av-wrap"><img src="'+p.profilePicBase64+'" alt="@'+p.username+'"></div>'
  :'<div class="av-wrap"><div class="av-init">'+(p.fullName||p.username||"?")[0].toUpperCase()+"</div></div>";
var vf=p.isVerified?'<span class="vbadge">&#10003;</span>':"";
var kpis=[
  {lbl:"Seguidores",      val:FN(N(p.followersCount)), sub:""},
  {lbl:"Engajamento medio",val:N(p.avgEngagement).toFixed(2)+"%", sub:"por post"},
  {lbl:"Total de posts",  val:FN(N(p.postsCount)),     sub:""},
  {lbl:"Formato top",     val:p.mostPostedFormat||"Foto", sub:"mais postado"}
];
function fmtCard(nm,dc){
  var f=fs[nm];
  if(!f||f.count===0)return'<div class="fmt-card"><div class="fmt-head"><span class="dot '+dc+'"></span>'+nm+'</div><div class="fmt-empty">Sem posts</div></div>';
  var rows=[["Posts",f.count],["Media curtidas",FN(f.avgLikes)],["Media comentarios",FN(f.avgComments)]];
  if(nm==="Reels")rows.push(["Total visualizacoes",FN(f.totalViews)]);
  return'<div class="fmt-card"><div class="fmt-head"><span class="dot '+dc+'"></span>'+nm+'</div>'+rows.map(function(r){return'<div class="fmt-line"><span>'+r[0]+"</span><b>"+r[1]+"</b></div>";}).join("")+"</div>";
}
var sorted=[].concat(posts).sort(function(a,b){return N(b.engagementRate)-N(a.engagementRate);});
var top3=sorted.slice(0,3);
var t3H=top3.map(function(pt){
  var imgH=pt.thumbnailBase64?'<img class="t3-img" src="'+pt.thumbnailBase64+'" alt="">':'<div class="t3-noimg">Sem imagem</div>';
  var vw=pt.type==="Reels"?'<span>&#128065; '+FN(N(pt.viewsCount))+"</span>":"";
  return'<div class="t3">'+imgH+'<div class="t3-body"><span class="bdg '+BC(pt.type)+'">'+pt.type+'</span><div class="t3-stats"><span>&#10084; '+pt.likesDisplay+"</span>"+'<span>&#128172; '+FN(N(pt.commentsCount))+"</span>"+vw+"</div>"+'<div class="t3-eng">Engajamento: '+N(pt.engagementRate).toFixed(2)+"%</div>"+(pt.caption?'<div class="t3-cap">'+pt.caption+"</div>":"")+'<a class="t3-link" href="'+pt.url+'" target="_blank">Ver post original</a></div></div>';
}).join("");
var csS={};
window.csClick=function(idx){
  var pt=posts[idx];if(!pt||!pt.carouselBase64||pt.carouselBase64.length<=1)return;
  csS[idx]=((csS[idx]||0)+1)%pt.carouselBase64.length;
  var img=document.getElementById("ti-"+idx);var ind=document.getElementById("pi-"+idx);
  if(img)img.src=pt.carouselBase64[csS[idx]];
  if(ind)ind.textContent=(csS[idx]+1)+"/"+pt.carouselBase64.length;
};
function pCard(pt,idx){
  var hasC=pt.carouselBase64&&pt.carouselBase64.length>1;
  var ind=hasC?'<span class="pi" id="pi-'+idx+'">1/'+pt.carouselBase64.length+"</span>":"";
  var vw=pt.type==="Reels"?'<span>&#128065; '+FN(N(pt.viewsCount))+"</span>":"";
  var dt=pt.timestamp?pt.timestamp.substring(0,10):"";
  return'<div class="pc" onclick="csClick('+idx+')">'+'<div class="pt"><img src="'+(pt.thumbnailBase64||"")+'" alt="" id="ti-'+idx+'">'+ind+"</div>"+'<div class="pb"><span class="bdg '+BC(pt.type)+'">'+pt.type+'</span>'+'<div class="pmeta"><span>&#10084; '+pt.likesDisplay+'</span><span>&#128172; '+FN(N(pt.commentsCount))+"</span>"+vw+"</div>"+'<div class="pdate">'+dt+"</div>"+(pt.caption?'<div class="pcap">'+pt.caption+"</div>":"")+'<a class="plink" href="'+pt.url+'" target="_blank" onclick="event.stopPropagation()">Ver post</a></div></div>';
}
document.getElementById("root").innerHTML=
  '<div class="hdr">'+avH+'<div class="hdr-info"><h1>@'+(p.username||"")+vf+"</h1>"+(p.bio?'<div class="bio">'+p.bio+"</div>":"")+'<div class="upd">Atualizado em '+p.lastUpdated+"</div></div></div>"+
  '<div class="kpi-row">'+kpis.map(function(k){return'<div class="kpi"><div class="kpi-lbl">'+k.lbl+'</div><div class="kpi-val">'+k.val+"</div>"+(k.sub?'<div class="kpi-sub">'+k.sub+"</div>":"")+"</div>";}).join("")+"</div>"+
  '<div class="sec">Desempenho Medio por Formato</div><div class="fmt-row">'+fmtCard("Reels","dr")+fmtCard("Carrossel","dc")+fmtCard("Foto","df")+"</div>"+
  '<div class="sec">Top 3 Posts</div><div class="top3-row">'+t3H+"</div>"+
  '<div class="sec">Linha do Tempo</div>'+
  '<div class="chart-card">'+
    '<div class="ch-blk"><div class="ch-ttl">Curtidas</div><div class="ch-leg"><div class="leg"><div class="ldot" style="background:#9333ea"></div>Reels</div><div class="leg"><div class="ldot" style="background:#2563eb"></div>Carrossel</div><div class="leg"><div class="ldot" style="background:#16a34a"></div>Foto</div></div><canvas id="ch-lk" height="150"></canvas></div>'+
    '<div class="ch-blk"><div class="ch-ttl">Visualizacoes (Reels)</div><div class="ch-leg"><div class="leg"><div class="ldot" style="background:#9333ea"></div>Reels</div></div><canvas id="ch-vw" height="150"></canvas></div>'+
    '<div class="ch-blk"><div class="ch-ttl">Engajamento (%)</div><div class="ch-leg"><div class="leg"><div class="ldot" style="background:#9333ea"></div>Reels</div><div class="leg"><div class="ldot" style="background:#2563eb"></div>Carrossel</div><div class="leg"><div class="ldot" style="background:#16a34a"></div>Foto</div></div><canvas id="ch-en" height="150"></canvas></div>'+
  "</div>"+
  '<div class="sec">Todos os Posts</div><div class="pgrd">'+posts.map(function(pt,i){return pCard(pt,i);}).join("")+"</div>";
var chrono=[].concat(posts).sort(function(a,b){return new Date(a.timestamp)-new Date(b.timestamp);});
var rP=chrono.filter(function(x){return x.type==="Reels";});
var cP=chrono.filter(function(x){return x.type==="Carrossel";});
var fP=chrono.filter(function(x){return x.type==="Foto";});
function drawLine(cid,series,valFn,colors,isPct){
  var cv=document.getElementById(cid);if(!cv)return;
  var W=cv.parentElement.offsetWidth||800;cv.width=W;
  var H=cv.height,ctx=cv.getContext("2d");
  var P={t:10,r:20,b:28,l:52},cW=W-P.l-P.r,cH=H-P.t-P.b;
  var mx=1;
  series.forEach(function(s){s.forEach(function(x){var v=valFn(x);if(v>mx)mx=v;});});
  ctx.clearRect(0,0,W,H);
  [0,.5,1].forEach(function(f){
    var y=P.t+cH*(1-f);
    ctx.strokeStyle="#eee";ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(P.l,y);ctx.lineTo(P.l+cW,y);ctx.stroke();
    ctx.fillStyle="#bbb";ctx.font="10px Inter,sans-serif";ctx.textAlign="right";
    ctx.fillText(isPct?(mx*f).toFixed(1)+"%":FN(Math.round(mx*f)),P.l-4,y+4);
  });
  series.forEach(function(pts,si){
    if(!pts||pts.length===0)return;
    ctx.strokeStyle=colors[si];ctx.lineWidth=2;ctx.beginPath();
    pts.forEach(function(x,i){
      var px=P.l+(pts.length===1?cW/2:i/(pts.length-1)*cW);
      var py=P.t+cH*(1-valFn(x)/mx);
      if(i===0)ctx.moveTo(px,py);else ctx.lineTo(px,py);
    });
    ctx.stroke();
    pts.forEach(function(x,i){
      var px=P.l+(pts.length===1?cW/2:i/(pts.length-1)*cW);
      var py=P.t+cH*(1-valFn(x)/mx);
      ctx.beginPath();ctx.arc(px,py,4,0,Math.PI*2);
      ctx.fillStyle=colors[si];ctx.fill();
      ctx.strokeStyle="#fff";ctx.lineWidth=1.5;ctx.stroke();
    });
  });
  var flat=[];series.forEach(function(s){flat=flat.concat(s);});
  flat.sort(function(a,b){return new Date(a.timestamp)-new Date(b.timestamp);});
  if(flat.length){
    ctx.fillStyle="#ccc";ctx.font="10px Inter,sans-serif";
    ctx.textAlign="left";ctx.fillText((flat[0].timestamp||"").substring(0,10),P.l,H-4);
    if(flat.length>1){ctx.textAlign="right";ctx.fillText((flat[flat.length-1].timestamp||"").substring(0,10),P.l+cW,H-4);}
  }
  cv._s=series;cv._vf=valFn;cv._cl=colors;cv._ip=isPct;cv._P=P;cv._mx=mx;
}
function addTip(cid,names){
  var cv=document.getElementById(cid);if(!cv)return;
  cv.addEventListener("mousemove",function(e){
    var r=cv.getBoundingClientRect();
    var mx2=(e.clientX-r.left)*(cv.width/r.width);
    var my2=(e.clientY-r.top)*(cv.height/r.height);
    var P=cv._P,W=cv.width,H=cv.height,cW=W-P.l-P.r,cH=H-P.t-P.b;
    var series=cv._s,vf=cv._vf,cl=cv._cl,maxV=cv._mx,isPct=cv._ip;
    var best=null,bd=Infinity;
    series.forEach(function(pts,si){
      if(!pts)return;
      pts.forEach(function(x,i){
        var px=P.l+(pts.length===1?cW/2:i/(pts.length-1)*cW);
        var py=P.t+cH*(1-vf(x)/maxV);
        var d=Math.hypot(mx2-px,my2-py);
        if(d<bd){bd=d;best={x:x,si:si,px:px,py:py,v:vf(x)};}
      });
    });
    drawLine(cid,series,vf,cl,isPct);
    if(best&&bd<20){
      var ctx=cv.getContext("2d");
      ctx.beginPath();ctx.arc(best.px,best.py,7,0,Math.PI*2);ctx.fillStyle=cl[best.si];ctx.fill();
      var lbl=isPct?best.v.toFixed(2)+"%":FN(Math.round(best.v));
      var txt=(names[best.si]||"")+": "+lbl+"  "+(best.x.timestamp||"").substring(0,10);
      ctx.font="12px Inter,sans-serif";
      var tw=ctx.measureText(txt).width+16,tx=best.px+12,ty=best.py-32;
      if(tx+tw>W-4)tx=best.px-tw-12;if(ty<4)ty=best.py+12;
      ctx.fillStyle="rgba(26,26,46,.85)";ctx.fillRect(tx,ty,tw,22);
      ctx.fillStyle="#fff";ctx.textAlign="left";ctx.fillText(txt,tx+8,ty+15);
    }
  });
  cv.addEventListener("mouseleave",function(){
    var el=this;drawLine(cid,el._s,el._vf,el._cl,el._ip);
  });
}
setTimeout(function(){
  var rc="#9333ea",cc="#2563eb",fc="#16a34a";
  var lkFn=function(x){return N(x.likesCount===-1?0:x.likesCount);};
  var vwFn=function(x){return N(x.viewsCount);};
  var enFn=function(x){return N(x.engagementRate);};
  drawLine("ch-lk",[rP,cP,fP],lkFn,[rc,cc,fc],false);
  drawLine("ch-vw",[rP],vwFn,[rc],false);
  drawLine("ch-en",[rP,cP,fP],enFn,[rc,cc,fc],true);
  addTip("ch-lk",["Reels","Carrossel","Foto"]);
  addTip("ch-vw",["Reels"]);
  addTip("ch-en",["Reels","Carrossel","Foto"]);
},200);
})();
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Atualiza o Instagram Dashboard.")
    parser.add_argument("--abrir", action="store_true", help="Abre o dashboard no navegador apos gerar")
    args = parser.parse_args()

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    log(f"== Iniciando atualizacao @{IG_USER} ==")

    # --- PERFIL ---
    log("Buscando perfil...")
    try:
        p_resp = apify_scrape("details", 1, 60, 90)
    except Exception as e:
        log(f"ERRO no perfil: {e}")
        sys.exit(1)

    if not p_resp:
        log(f"ERRO: perfil vazio ou privado para @{IG_USER}")
        sys.exit(1)

    prof = p_resp[0]
    log(f"Perfil: {prof.get('fullName', '')} | Seguidores: {prof.get('followersCount', 0)}")

    # --- POSTS (busca expandida para substituir likes ocultos) ---
    all_posts: list = []
    limit = 30
    max_limit = 100

    while True:
        log(f"Buscando {limit} posts...")
        try:
            all_posts = apify_scrape("posts", limit, 300, 360)
        except Exception as e:
            log(f"Aviso posts: {e}")
            break

        visib = sum(1 for p in all_posts if p.get("likesCount") not in (None, -1))
        log(f"Total: {len(all_posts)} | Com likes visiveis: {visib}")
        if visib >= 30 or limit >= max_limit:
            break
        limit = min(limit + 20, max_limit)

    vis = [p for p in all_posts if p.get("likesCount") not in (None, -1)][:30]
    hid = [p for p in all_posts if p.get("likesCount") in (None, -1)]
    sel = vis + hid[: max(0, 30 - len(vis))]
    sel = sel[:30]
    log(f"Posts selecionados: {len(sel)}")

    # --- IMAGENS ---
    log("Baixando foto de perfil...")
    pic_url = prof.get("profilePicUrlHD") or prof.get("profilePicUrl") or ""
    pic_b64 = img64(pic_url)

    followers = max(1, int(prof.get("followersCount") or 1))
    post_objs: list[dict] = []

    for i, post in enumerate(sel, 1):
        print(f"  Imagem {i}/{len(sel)} ({post.get('type', '')})...")

        raw_type = post.get("type") or ""
        if raw_type in ("GraphVideo", "Video"):
            post_type = "Reels"
        elif raw_type in ("GraphSidecar", "Sidecar"):
            post_type = "Carrossel"
        else:
            post_type = "Foto"

        # Transcricao (so para Reels)
        transcricao = ""
        if post_type == "Reels":
            video_url = post.get("videoUrl") or ""
            if video_url:
                print(f"  Transcricao {i}/{len(sel)}...")
                transcricao = transcribe(video_url)
                if transcricao:
                    log(f"  Transcricao obtida: {len(transcricao)} chars")
                else:
                    log(f"  Sem transcricao para o post {post.get('id', '')}")

        likes_raw = post.get("likesCount")
        likes = -1 if likes_raw is None else int(likes_raw)
        comments = int(post.get("commentsCount") or 0)
        views = int(post.get("videoViewCount") or 0)

        likes_calc = 0 if likes == -1 else likes
        eng_rate = round((likes_calc + comments) / followers * 100, 3)

        cap_raw = post.get("caption") or ""
        cap_clean = re.sub(r"[\r\n]+", " ", cap_raw).strip()
        cap_full = cap_clean[:500] + "..." if len(cap_clean) > 500 else cap_clean
        cap      = cap_clean[:200] + "..." if len(cap_clean) > 200 else cap_clean

        thumb = img64(post.get("displayUrl") or "")

        carousel: list[str] = []
        images = post.get("images") or []
        if len(images) > 1:
            for img_url in images[:10]:
                b = img64(img_url)
                if b:
                    carousel.append(b)
        if not carousel and thumb:
            carousel.append(thumb)

        post_objs.append({
            "id":              str(post.get("id") or ""),
            "url":             str(post.get("url") or ""),
            "type":            post_type,
            "timestamp":       str(post.get("timestamp") or ""),
            "likesCount":      likes,
            "likesDisplay":    "--" if likes == -1 else str(likes),
            "commentsCount":   comments,
            "viewsCount":      views,
            "engagementRate":  eng_rate,
            "caption":         cap,
            "captionFull":     cap_full,
            "thumbnailBase64": thumb,
            "carouselBase64":  carousel,
            "transcricao":     transcricao,
        })

    # --- METRICAS ---
    fmt_counts = {"Reels": 0, "Carrossel": 0, "Foto": 0}
    fmt_likes  = {"Reels": 0, "Carrossel": 0, "Foto": 0}
    fmt_comm   = {"Reels": 0, "Carrossel": 0, "Foto": 0}
    fmt_views  = 0

    for o in post_objs:
        f = o["type"]
        lk = 0 if o["likesCount"] == -1 else o["likesCount"]
        if f in fmt_counts:
            fmt_counts[f] += 1
            fmt_likes[f]  += lk
            fmt_comm[f]   += o["commentsCount"]
            if f == "Reels":
                fmt_views += o["viewsCount"]

    eng_vals = [o["engagementRate"] for o in post_objs]
    avg_eng  = round(sum(eng_vals) / len(eng_vals), 2) if eng_vals else 0
    most_fmt = max(fmt_counts, key=lambda k: fmt_counts[k])

    # --- INSIGHTS JSON ---
    log("Gerando insights.json...")
    sorted_posts = sorted(post_objs, key=lambda x: x["engagementRate"], reverse=True)[:10]
    insights_top10 = []

    for pos, p in enumerate(sorted_posts, 1):
        vw = int(p["viewsCount"]) if p["type"] == "Reels" else None
        lk = None if p["likesCount"] == -1 else int(p["likesCount"])
        ts = p["timestamp"]
        dt = ts[:10] if len(ts) >= 10 else ts

        # Thumbnail
        thumb_path = ""
        if p["thumbnailBase64"]:
            thumb_file = IMG_DIR / f"thumb-{pos}.jpg"
            if save_b64(p["thumbnailBase64"], thumb_file):
                thumb_path = f"entregas/instagram-dashboard/imagens/thumb-{pos}.jpg"

        # Slides do carrossel (max 3: primeiro, meio, ultimo)
        all_slides = p["carouselBase64"]
        slides_sel: list[str] = []
        if all_slides:
            slides_sel.append(all_slides[0])
            if len(all_slides) >= 3:
                slides_sel.append(all_slides[math.floor(len(all_slides) / 2)])
            if len(all_slides) >= 2:
                slides_sel.append(all_slides[-1])
            seen: set = set()
            slides_sel = [s for s in slides_sel if not (id(s) in seen or seen.add(id(s)))]  # type: ignore

        slides_paths: list[str] = []
        for s_idx, slide in enumerate(slides_sel, 1):
            slide_file = IMG_DIR / f"slide-{pos}-{s_idx}.jpg"
            if save_b64(slide, slide_file):
                slides_paths.append(f"entregas/instagram-dashboard/imagens/slide-{pos}-{s_idx}.jpg")

        insights_top10.append({
            "posicao":       pos,
            "tipo":          p["type"],
            "engajamento":   p["engagementRate"],
            "likes":         lk,
            "comentarios":   p["commentsCount"],
            "visualizacoes": vw,
            "data":          dt,
            "caption":       p["captionFull"],
            "url":           p["url"],
            "thumbnailPath": thumb_path,
            "carouselPaths": slides_paths,
            "transcricao":   p["transcricao"],
        })

    insights_obj = {
        "gerado_em":   datetime.now().strftime("%d/%m/%Y %H:%M"),
        "perfil":      f"@{prof.get('username', IG_USER)}",
        "seguidores":  int(prof.get("followersCount") or 0),
        "avg_eng_pct": avg_eng,
        "formato_top": most_fmt,
        "formato_stats": {
            "Reels":     {"count": fmt_counts["Reels"],     "avg_likes": avg_round(fmt_likes["Reels"],     fmt_counts["Reels"]),     "avg_comentarios": avg_round(fmt_comm["Reels"],     fmt_counts["Reels"]),     "total_views": fmt_views},
            "Carrossel": {"count": fmt_counts["Carrossel"], "avg_likes": avg_round(fmt_likes["Carrossel"], fmt_counts["Carrossel"]), "avg_comentarios": avg_round(fmt_comm["Carrossel"], fmt_counts["Carrossel"]), "total_views": 0},
            "Foto":      {"count": fmt_counts["Foto"],      "avg_likes": avg_round(fmt_likes["Foto"],      fmt_counts["Foto"]),      "avg_comentarios": avg_round(fmt_comm["Foto"],      fmt_counts["Foto"]),      "total_views": 0},
        },
        "top10": insights_top10,
    }

    INSIGHTS.write_text(json.dumps(insights_obj, ensure_ascii=False, indent=4), encoding="utf-8")
    log(f"insights.json salvo: {round(INSIGHTS.stat().st_size / 1024, 1)} KB")

    # --- MONTAR JSON DO DASHBOARD ---
    log("Montando JSON...")
    dash_obj = {
        "profile": {
            "username":         str(prof.get("username") or IG_USER),
            "fullName":         str(prof.get("fullName") or IG_USER),
            "bio":              str(prof.get("biography") or ""),
            "followersCount":   int(prof.get("followersCount") or 0),
            "followingCount":   int(prof.get("followingCount") or 0),
            "postsCount":       int(prof.get("postsCount") or len(post_objs)),
            "isVerified":       bool(prof.get("verified")),
            "profilePicBase64": pic_b64,
            "lastUpdated":      datetime.now().strftime("%d/%m/%Y %H:%M"),
            "avgEngagement":    avg_eng,
            "mostPostedFormat": most_fmt,
        },
        "formatStats": {
            "Reels":     {"count": fmt_counts["Reels"],     "avgLikes": avg_round(fmt_likes["Reels"],     fmt_counts["Reels"]),     "avgComments": avg_round(fmt_comm["Reels"],     fmt_counts["Reels"]),     "totalViews": fmt_views},
            "Carrossel": {"count": fmt_counts["Carrossel"], "avgLikes": avg_round(fmt_likes["Carrossel"], fmt_counts["Carrossel"]), "avgComments": avg_round(fmt_comm["Carrossel"], fmt_counts["Carrossel"]), "totalViews": 0},
            "Foto":      {"count": fmt_counts["Foto"],      "avgLikes": avg_round(fmt_likes["Foto"],      fmt_counts["Foto"]),      "avgComments": avg_round(fmt_comm["Foto"],      fmt_counts["Foto"]),      "totalViews": 0},
        },
        "posts": post_objs,
    }

    json_str = json.dumps(dash_obj, ensure_ascii=False, separators=(",", ":"))
    log(f"JSON: {round(len(json_str) / 1024, 1)} KB")

    # --- GERAR HTML ---
    log("Gerando HTML...")
    html = HTML_TEMPLATE.replace("__JSON__", json_str)
    DASHBOARD.write_text(html, encoding="utf-8")
    log(f"Dashboard salvo: {DASHBOARD}")
    log("== Concluido ==")

    if args.abrir:
        webbrowser.open(DASHBOARD.as_uri())
        log("Abrindo no navegador...")


if __name__ == "__main__":
    main()
