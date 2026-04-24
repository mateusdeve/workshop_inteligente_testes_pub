# -*- coding: utf-8 -*-
"""
Fluxo A da Furadeira. Gera PNG via API direta do Google Gemini.

Modelo: gemini-2.5-flash-image (Nano Banana).
Endpoint: generativelanguage.googleapis.com

Chave:
  1. Copie .env.example para .env na raiz (se ainda nao tiver).
  2. Preencha GEMINI_API_KEY= com sua chave do Google AI Studio
     (https://aistudio.google.com/app/apikey).
  3. Salve. O .env nao vai para o Git.

Uso (a partir da raiz do repositorio):
  py -3 scripts/gerar-furadeira-gemini.py --slug curso-tarot --prompt "..."

Saida padrao:
  meus-produtos/{slug}/entregas/furadeira/furadeira-gemini.png
"""
from __future__ import annotations

import argparse
import base64
import json
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
TIMEOUT_SECONDS = 60


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


def generate(api_key: str, model: str, prompt: str) -> bytes:
    url = ENDPOINT.format(model=model, key=api_key)
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
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
    ap.add_argument("--slug", required=True, help="Slug do produto ativo (pasta em meus-produtos/).")
    ap.add_argument("--prompt", required=True, help="Prompt textual completo em ingles.")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="Modelo Gemini (padrao: gemini-2.5-flash-image).")
    ap.add_argument(
        "--output",
        default="furadeira-gemini.png",
        help="Nome do arquivo dentro de meus-produtos/{slug}/entregas/furadeira/",
    )
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        print(
            "Nao encontrei GEMINI_API_KEY no .env.\n"
            "Obtenha em https://aistudio.google.com/app/apikey e salve a chave no .env.",
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
        png = generate(api_key, args.model, args.prompt)
    except RuntimeError as exc:
        msg = str(exc)
        if "401" in msg or "API key" in msg or "INVALID_ARGUMENT" in msg:
            print(
                "Chave do Gemini invalida ou sem permissao. "
                "Confira GEMINI_API_KEY no .env.",
                file=sys.stderr,
            )
        elif "429" in msg or "RESOURCE_EXHAUSTED" in msg:
            print(
                "Limite de uso do Gemini atingido ou cota esgotada. "
                "Tente de novo em alguns minutos.",
                file=sys.stderr,
            )
        elif "timed out" in msg.lower() or "timeout" in msg.lower():
            print("Tempo limite excedido ao chamar o Gemini.", file=sys.stderr)
        else:
            print(f"Erro ao gerar furadeira via Gemini: {msg}", file=sys.stderr)
        return 2

    out_path.write_bytes(png)
    dt = time.time() - t0
    print(f"OK\t{out_path}\t{dt:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
