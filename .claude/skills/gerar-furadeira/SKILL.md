---
name: gerar-furadeira
description: Apoio tecnico para os comandos /gerar-furadeira e /furadeira-visual (opcoes 2 e 3). Contem o template de prompt, regras de traducao pt to en, e os parametros dos modelos de imagem.
---

# Skill. Gerar Furadeira (PNG via IA)

Apoio técnico para os comandos que geram a Furadeira em imagem:
- `/gerar-furadeira`. Atalho direto para PNG (dois fluxos: Gemini ou OpenRouter, ou os dois).
- `/furadeira-visual`. Comando principal com 3 opções de saída. Usa esta skill nas opções 2 (Imagem via API) e 3 (Prompt pronto).

Consulte este arquivo se precisar:
- Ajustar o prompt textual que vai para a API de imagem.
- Entender por que os dois fluxos de API existem.
- Depurar erros de retorno da API.

## Por que dois fluxos

| Critério | Rápido (Gemini direto) | Refinado (OpenRouter com refs) |
|---|---|---|
| Tempo | ~30s | 1 a 3 min |
| Consistência com marca | Baixa (sem referência) | Alta (usa fotos de inspiração) |
| Custo | Gratuito no tier free do AI Studio | ~US$ 0,04 por imagem no OpenRouter |
| Chave necessária | `GEMINI_API_KEY` | `OPENROUTER_API_KEY` |
| Script | `scripts/gerar-furadeira-gemini.py` | `scripts/gerar-furadeira-openrouter.py` |
| Modelo | `gemini-2.5-flash-image` (direto) | `google/gemini-2.5-flash-image` (via OpenRouter) |

Ambos os modelos são o mesmo motor (Nano Banana). A diferença prática é que o segundo aceita imagens de entrada, então pega estilo das suas referências.

## Template de prompt (inglês)

```
Photorealistic editorial composition representing a learning journey for
"{QUADRO_EN}" in the "{NICHO_EN}" niche. Visual metaphor of progression
through {N} stages: {MACROETAPAS_EN_COMMA}. Main audience emotional state
at the start: "{DOR_CENTRAL_EN}". Style: cinematic lighting, neutral studio
background, soft depth of field, professional color palette, no text overlays,
no logos, no readable words, no cartoon characters. Aspect ratio 4:3.
```

## Regras de tradução pt → en

- Quadro: mantém o significado do resultado final. "Falar inglês em 90 dias" → "speaking fluent English in 90 days".
- Nicho: traduz termo literal. "Finanças para MEI" → "small business finance in Brazil".
- Macroetapas: traduz cada título curto, mantém a ordem. Separar por vírgula.
- Dor central: pega a primeira dor das Urgências Ocultas, traduz como estado emocional. "Estou perdida com contas" → "feeling lost and overwhelmed with finances".

Se não houver tradução natural, use a versão em inglês mais próxima. Nunca deixe palavras em português no prompt final (o modelo responde pior).

## Ajustes possíveis no prompt

- Proporção: trocar `4:3` por `16:9` (banner horizontal) ou `1:1` (instagram).
- Paleta: adicionar `warm golden tones` / `cool blue palette` / `earth tones` conforme o nicho.
- Se o nicho for espiritual (tarô, astrologia), substituir `editorial` por `mystical editorial` e adicionar `subtle ethereal atmosphere`.
- Se o nicho for corporativo, manter `editorial` e reforçar `clean minimalist layout`.

## Erros comuns e o que significam

| Mensagem | Causa | Ação |
|---|---|---|
| `HTTP 401` Gemini | Chave inválida ou expirada | Gerar nova em aistudio.google.com |
| `HTTP 401` OpenRouter | Chave inválida | Rodar `/configurar-imagens` |
| `HTTP 402` OpenRouter | Sem crédito | Recarregar em openrouter.ai/settings/credits |
| `HTTP 429` | Rate limit | Esperar 1 a 2 min e tentar de novo |
| `RESOURCE_EXHAUSTED` Gemini | Cota diária do free tier | Esperar 24h ou ativar billing no Google Cloud |
| "Nenhuma imagem retornada" | Modelo devolveu só texto | Reforçar no prompt: `Generate an image, not text` |
| "Faltam imagens de referência" | Pasta `assets/furadeira-referencias/` tem menos de 3 arquivos | Adicionar referências |

## Por que o output é PNG e não HTML

O comando `/furadeira-visual` já cobre o caso HTML de trilha esquemática. Este comando é pra quando o aluno quer:
- Uma peça visual pronta pra usar no topo da página de vendas.
- Um criativo para anúncio do método.
- Um mockup pra thumbnail de aula.

Imagem de IA converte melhor para esses casos do que CSS/SVG.
