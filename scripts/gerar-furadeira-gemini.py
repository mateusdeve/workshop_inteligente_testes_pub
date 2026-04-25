# -*- coding: utf-8 -*-
"""
Fluxo A da Furadeira. Gera PNG via API direta do Google Gemini.

Modelo: gemini-2.5-flash-image
Endpoint: generativelanguage.googleapis.com

Suporta imagens de referencia via inline_data (pipeline multimodal nativo do Gemini).
Coloque de 1 a 8 referencias em assets/furadeira-referencias/ (PNG, JPG, WEBP).

Chave:
  GEMINI_API_KEY no .env (https://aistudio.google.com/app/apikey).

Uso:
  py -3 scripts/gerar-furadeira-gemini.py --slug curso-tarot --prompt "..."

Saida padrao:
  meus-produtos/{slug}/entregas/furadeira/furadeira-gemini.png
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "{model}:generateContent?key={key}"
)
DEFAULT_MODEL = "gemini-2.5-flash-image"
REFS_DIR = ROOT / "assets" / "furadeira-referencias"
VALID_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
MAX_REFS = 8
MAX_REF_PX = 1024
MAX_REF_BYTES = 512 * 1024
TIMEOUT_SECONDS = 120


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


def collect_references(max_refs: int = MAX_REFS) -> list[Path]:
    if not REFS_DIR.is_dir():
        return []
    paths = sorted(
        p for p in REFS_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in VALID_EXTS
    )
    return paths[:max_refs]


def _resize_image_bytes(data: bytes, mime: str) -> tuple[bytes, str]:
    """Redimensiona para MAX_REF_PX e comprime para MAX_REF_BYTES usando Pillow.
    Se Pillow nao estiver disponivel, devolve o original sem alterar."""
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
        while len(result) > MAX_REF_BYTES and fmt == "JPEG" and quality > 40:
            quality -= 15
            buf = io.BytesIO()
            img.save(buf, format="JPEG", optimize=True, quality=quality)
            result = buf.getvalue()
        return result, f"image/{'png' if fmt == 'PNG' else 'jpeg'}"
    except Exception:
        return data, mime


def to_inline_data(path: Path) -> dict[str, Any]:
    mime, _ = mimetypes.guess_type(str(path))
    if not mime:
        mime = "image/png"
    data = path.read_bytes()
    data, mime = _resize_image_bytes(data, mime)
    b64 = base64.b64encode(data).decode("ascii")
    return {"inline_data": {"mime_type": mime, "data": b64}}


def _post_json(url: str, payload: dict[str, Any]) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
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
        raise RuntimeError(f"Falha de rede ao chamar Gemini: {exc.reason}") from exc
    return json.loads(body)


def _extract_png_bytes(resp: dict[str, Any]) -> bytes:
    candidates = resp.get("candidates") or []
    if not candidates:
        raise RuntimeError("Resposta sem candidates. " + json.dumps(resp)[:600])
    for cand in candidates:
        parts = ((cand.get("content") or {}).get("parts")) or []
        for part in parts:
            inline = part.get("inline_data") or part.get("inlineData")
            if not inline:
                continue
            data = inline.get("data")
            if data:
                return base64.b64decode(data)
    raise RuntimeError(
        "Nenhuma imagem retornada pelo Gemini. Resposta: "
        + json.dumps(resp, ensure_ascii=False)[:800]
    )


def generate(api_key: str, model: str, prompt: str, refs: list[Path]) -> bytes:
    url = ENDPOINT.format(model=model, key=api_key)

    parts: list[dict[str, Any]] = []

    if refs:
        style_prefix = (
            f"IMPORTANT — STYLE REFERENCE IMAGES ATTACHED ({len(refs)} images):\n"
            "Carefully analyze every reference image before generating anything. "
            "Your output MUST replicate their visual style: layout structure, color palette, "
            "typography weight, icon style, card shapes, spacing, and decorative elements. "
            "Treat these images as your primary visual specification — not as inspiration, "
            "but as the exact style target to match.\n\n"
        )
        parts.append({"text": style_prefix})
        for ref in refs:
            parts.append(to_inline_data(ref))

    parts.append({"text": prompt})

    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]},
    }

    resp = _post_json(url, payload)
    if resp.get("error"):
        err = resp["error"]
        msg = err.get("message") or json.dumps(err, ensure_ascii=False)
        raise RuntimeError(msg)
    return _extract_png_bytes(resp)


def main() -> int:
    load_env_file(ROOT / ".env")

    ap = argparse.ArgumentParser(description="Gera furadeira em PNG via Gemini direto.")
    ap.add_argument("--slug", required=True, help="Slug do produto ativo.")
    ap.add_argument("--prompt", required=True, help="Prompt textual completo em ingles.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-refs", type=int, default=MAX_REFS, help="Maximo de referencias (0 = sem referencias).")
    ap.add_argument("--output", default="furadeira-gemini.png")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        print(
            "Nao encontrei GEMINI_API_KEY no .env.\n"
            "Obtenha em https://aistudio.google.com/app/apikey e salve no .env.",
            file=sys.stderr,
        )
        return 1

    raw_out = args.output.strip().replace("\\", "/")
    if ".." in raw_out or raw_out.startswith("/"):
        print("Nome de --output invalido.", file=sys.stderr)
        return 1

    refs = collect_references(max_refs=args.max_refs) if args.max_refs > 0 else []

    out_dir = ROOT / "meus-produtos" / args.slug / "entregas" / "furadeira"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / raw_out

    if refs:
        print(f"Usando {len(refs)} imagens de referencia via Gemini nativo.", file=sys.stderr)

    t0 = time.time()
    try:
        png = generate(api_key, args.model, args.prompt, refs)
    except RuntimeError as exc:
        msg = str(exc)
        if "401" in msg or "API key" in msg or "INVALID_ARGUMENT" in msg:
            print("Chave do Gemini invalida. Confira GEMINI_API_KEY no .env.", file=sys.stderr)
        elif "429" in msg or "RESOURCE_EXHAUSTED" in msg:
            print("Limite de uso do Gemini atingido. Tente de novo em alguns minutos.", file=sys.stderr)
        elif "timed out" in msg.lower() or "timeout" in msg.lower():
            print("Tempo limite excedido ao chamar o Gemini.", file=sys.stderr)
        else:
            print(f"Erro ao gerar furadeira via Gemini: {msg}", file=sys.stderr)
        return 2

    out_path.write_bytes(png)
    dt = time.time() - t0
    refs_label = f"{len(refs)} refs" if refs else "sem refs"
    print(f"OK\t{out_path}\t{refs_label}\t{dt:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
