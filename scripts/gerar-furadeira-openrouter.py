# -*- coding: utf-8 -*-
"""
Fluxo B da Furadeira. Gera PNG via OpenRouter com imagens de referencia.

Modelo padrao: google/gemini-2.5-flash-image (Nano Banana), que aceita multiplas
imagens de entrada no payload multimodal. De 3 a 16 referencias em
assets/furadeira-referencias/.

Chave:
  OPENROUTER_API_KEY no .env (mesma que o script de Nano Banana ja usa).

Uso:
  py -3 scripts/gerar-furadeira-openrouter.py --slug curso-tarot --prompt "..."

Saida padrao:
  meus-produtos/{slug}/entregas/furadeira/furadeira-openrouter.png
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-2.5-flash-image"
REFS_DIR = ROOT / "assets" / "furadeira-referencias"
MIN_REFS = 3
MAX_REFS = 16
TIMEOUT_SECONDS = 180
VALID_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def load_env_file(path: Path) -> None:
    if not path.is_file():
        return
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        return
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        key, _, rest = s.partition("=")
        key = key.strip()
        val = rest.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        if key and key not in os.environ:
            os.environ[key] = val


MAX_REF_PX = 1024   # lado máximo após redimensionamento
MAX_REF_BYTES = 512 * 1024  # 512 KB por referência após compressão


def collect_references(max_refs: int) -> list[Path]:
    if not REFS_DIR.is_dir():
        return []
    paths = sorted(
        p for p in REFS_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in VALID_EXTS
    )
    return paths[:max_refs]


def _resize_image_bytes(data: bytes, mime: str) -> tuple[bytes, str]:
    """Redimensiona para MAX_REF_PX e comprime para MAX_REF_BYTES usando Pillow.
    Retorna (bytes, mime). Se Pillow não estiver disponível, devolve original."""
    try:
        from PIL import Image  # type: ignore
        import io
        img = Image.open(io.BytesIO(data))
        img = img.convert("RGBA" if img.mode in ("RGBA", "LA", "PA") else "RGB")
        w, h = img.size
        if w > MAX_REF_PX or h > MAX_REF_PX:
            ratio = min(MAX_REF_PX / w, MAX_REF_PX / h)
            img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)
        buf = io.BytesIO()
        fmt = "PNG" if img.mode == "RGBA" else "JPEG"
        quality = 85
        img.save(buf, format=fmt, optimize=True, quality=quality)
        result = buf.getvalue()
        # se ainda grande, reduz qualidade progressivamente
        while len(result) > MAX_REF_BYTES and fmt == "JPEG" and quality > 40:
            quality -= 15
            buf = io.BytesIO()
            img.save(buf, format="JPEG", optimize=True, quality=quality)
            result = buf.getvalue()
        return result, f"image/{'png' if fmt == 'PNG' else 'jpeg'}"
    except Exception:
        return data, mime


def to_data_url(path: Path) -> str:
    mime, _ = mimetypes.guess_type(str(path))
    if not mime:
        mime = "image/png"
    data = path.read_bytes()
    data, mime = _resize_image_bytes(data, mime)
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"


def _extract_png_data_url(message: dict[str, Any]) -> str | None:
    # Formato Gemini via OpenRouter: message.images[]
    images = message.get("images")
    if images:
        first = images[0]
        if isinstance(first, dict):
            iu = first.get("image_url") or first.get("imageUrl")
            if isinstance(iu, dict):
                url = iu.get("url")
            else:
                url = iu if isinstance(iu, str) else None
            if isinstance(url, str) and url.startswith("data:image"):
                return url

    # Formato OpenAI (GPT Image 1 e outros): message.content[] com type=image_url
    content = message.get("content")
    if isinstance(content, list):
        for item in content:
            if not isinstance(item, dict):
                continue
            if item.get("type") == "image_url":
                iu = item.get("image_url")
                if isinstance(iu, dict):
                    url = iu.get("url", "")
                    if url.startswith("data:image"):
                        return url

    return None


def save_from_data_url(data_url: str, dest: Path) -> None:
    m = re.match(r"data:image/(png|jpeg|jpg|webp);base64,(.+)", data_url, re.DOTALL)
    if not m:
        raise RuntimeError("Formato de imagem inesperado na resposta.")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(base64.b64decode(m.group(2)))


def _post_json(url: str, headers: dict[str, str], payload: dict[str, Any]) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        try:
            err_body = exc.read().decode("utf-8")
        except Exception:
            err_body = ""
        raise RuntimeError(f"HTTP {exc.code}: {err_body[:800]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Falha de rede ao chamar OpenRouter: {exc.reason}") from exc
    return json.loads(body)


def build_content(prompt: str, refs: list[Path]) -> list[dict[str, Any]]:
    # Instrução de estilo reforçada antes das imagens quando há referências
    if refs:
        style_prefix = (
            f"IMPORTANT — STYLE REFERENCE IMAGES ATTACHED ({len(refs)} images):\n"
            "Carefully analyze every reference image before generating anything. "
            "Your output MUST replicate their visual style: layout structure, color palette, "
            "typography weight, icon style, card shapes, spacing, and decorative elements. "
            "Treat these images as your primary visual specification — not as inspiration, "
            "but as the exact style target to match.\n\n"
        )
        full_prompt = style_prefix + prompt
    else:
        full_prompt = prompt
    content: list[dict[str, Any]] = [{"type": "text", "text": full_prompt}]
    for ref in refs:
        content.append(
            {"type": "image_url", "image_url": {"url": to_data_url(ref)}}
        )
    return content


def generate(api_key: str, model: str, prompt: str, refs: list[Path]) -> str:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": build_content(prompt, refs)}],
        "modalities": ["image", "text"],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/workshop_inteligente",
        "X-Title": "Workshop Marketing IA furadeira",
    }
    result = _post_json(OPENROUTER_URL, headers, payload)
    if result.get("error"):
        err = result["error"]
        msg = err.get("message") if isinstance(err, dict) else json.dumps(err)
        raise RuntimeError(msg or json.dumps(err))
    choices = result.get("choices") or []
    if not choices:
        raise RuntimeError("Resposta sem choices. " + json.dumps(result)[:600])
    message = choices[0].get("message") or {}
    url = _extract_png_data_url(message)
    if not url:
        raise RuntimeError(
            "Nenhuma imagem retornada pelo OpenRouter. "
            + json.dumps(message, ensure_ascii=False)[:800]
        )
    return url


def main() -> int:
    load_env_file(ROOT / ".env")

    ap = argparse.ArgumentParser(description="Gera furadeira em PNG via OpenRouter com referencias.")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--model", default=os.environ.get("OPENROUTER_MODEL") or DEFAULT_MODEL)
    ap.add_argument("--max-refs", type=int, default=MAX_REFS)
    ap.add_argument(
        "--output",
        default="furadeira-openrouter.png",
        help="Nome do arquivo dentro de meus-produtos/{slug}/entregas/furadeira/",
    )
    args = ap.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        print(
            "Nao encontrei OPENROUTER_API_KEY no .env.\n"
            "Rode /configurar-imagens ou preencha a chave direto no .env.",
            file=sys.stderr,
        )
        return 1

    if args.max_refs == 0:
        refs = []
    else:
        refs = collect_references(min(args.max_refs, MAX_REFS))
        if len(refs) < MIN_REFS:
            print(
                f"Faltam imagens de referencia. Coloque pelo menos {MIN_REFS} arquivos "
                f"(PNG, JPG ou WEBP) em: {REFS_DIR}\n"
                f"Encontrei {len(refs)} no momento.\n"
                f"Para gerar sem referencias, passe --max-refs 0.",
                file=sys.stderr,
            )
            return 1

    raw_out = args.output.strip().replace("\\", "/")
    if ".." in raw_out or raw_out.startswith("/"):
        print("Nome de --output invalido. Use so o nome do arquivo.", file=sys.stderr)
        return 1

    out_dir = ROOT / "meus-produtos" / args.slug / "entregas" / "furadeira"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / raw_out

    t0 = time.time()
    try:
        data_url = generate(api_key, args.model, args.prompt, refs)
    except RuntimeError as exc:
        msg = str(exc)
        if "401" in msg:
            print(
                "Chave do OpenRouter invalida. Confira OPENROUTER_API_KEY no .env.",
                file=sys.stderr,
            )
        elif "402" in msg or "insufficient" in msg.lower() or "credits" in msg.lower():
            print(
                "Credito do OpenRouter acabou. Recarregue em "
                "https://openrouter.ai/settings/credits e tente de novo.",
                file=sys.stderr,
            )
        elif "429" in msg:
            print(
                "Limite de uso atingido no OpenRouter. Aguarde alguns minutos.",
                file=sys.stderr,
            )
        elif "timed out" in msg.lower() or "timeout" in msg.lower():
            print("Tempo limite excedido ao chamar o OpenRouter.", file=sys.stderr)
        else:
            print(f"Erro ao gerar furadeira via OpenRouter: {msg}", file=sys.stderr)
        return 2

    save_from_data_url(data_url, out_path)
    dt = time.time() - t0
    print(f"OK\t{out_path}\t{len(refs)} refs\t{dt:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
