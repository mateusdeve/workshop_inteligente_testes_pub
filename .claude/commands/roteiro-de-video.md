---
name: workshop-marketing:roteiro-de-video
description: Criar roteiros de vídeo — VVV (Vídeo de Vendas de Valor), Reels 60 segundos, YouTube e scripts para avatar HeyGen. Baseado na estrutura VVV do VTSD.
---

# Roteiro de Vídeo — VVV e Formatos Curtos

Cria roteiros seguindo a estrutura VVV (Vídeo de Vendas de Valor) do VTSD.

## Usage

```
/roteiro-de-video
```

## O Que Fazer

### 1. Contexto
Leia `produtos/{ativo}/perfil.md`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Formato:**

```
Qual formato de vídeo?

1. VVV completo (vídeo de vendas, 12-20 min)
2. Reels 60 segundos (Instagram/TikTok)
3. YouTube (conteúdo longo educativo)
4. Avatar IA (script para HeyGen)

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Formato: [formato escolhido]
Próximo: Objetivo
---
```

**Bloco 2/3 — Objetivo:**

```
Qual o objetivo do vídeo?

1. Vender produto
2. Educar e gerar valor
3. Captar leads
4. Engajar audiência

Digite o número:
```

```
--- Bloco 2/3 concluído ---
Formato: [formato]
Objetivo: [objetivo]
Próximo: Plataforma
---
```

**Bloco 3/3 — Plataforma:**

```
Onde será publicado?

1. Instagram (Reels/Stories)
2. TikTok
3. YouTube
4. Página de vendas
5. Anúncio pago (Meta Ads)

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Formato: [formato]
- Objetivo: [objetivo]
- Plataforma: [onde será publicado]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**VVV Completo (estrutura VTSD):**
1. Abertura — Gancho que prende (sem pergunta, premissa forte)
2. Conexão — História que gera identificação
3. Problema — Dor amplificada com Urgências Ocultas
4. Paliativo — O que já tentaram e falhou
5. Solução — Apresentação da Furadeira
6. Prova — Resultados e depoimentos
7. Oferta — Entregáveis, bônus, garantia, preço
8. CTA — Chamada direta

**Reels 60s (2 formatos VTSD):**

Formato Pergunta-Resposta-Objeção:
- 0-5s: Pergunta do público
- 5-30s: Resposta direta
- 30-55s: Quebra de objeção
- 55-60s: CTA

Formato Problema-Solução:
- 0-5s: Gancho com problema
- 5-20s: Amplifica dor
- 20-50s: Solução prática
- 50-60s: CTA

**Avatar (HeyGen):**
- Script de até 90 segundos
- Linguagem natural e pausada
- Indicações de expressão e ritmo
- Adaptado para leitura de teleprompter

### 4. Salvar
`produtos/{ativo}/entregas/textos-de-venda/roteiro-[formato]-[produto].md`

### 5. Gerar Vídeo com Avatar (se formato Avatar e chave configurada)
Leia `.env` e verifique se existe `HEYGEN_API_KEY`.

Se existir E o formato escolhido for Avatar:
1. Envie o script para a API do HeyGen via `curl`:
```bash
curl -X POST "https://api.heygen.com/v2/video/generate" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_inputs": [{"character": {"type": "avatar", "avatar_id": "default"}, "voice": {"type": "text", "input_text": "SCRIPT_AQUI"}}], "dimension": {"width": 1080, "height": 1920}}'
```
2. Acompanhe o status do vídeo e informe o link quando pronto
3. Informe: "Vídeo sendo gerado no HeyGen. Você receberá o link quando ficar pronto."

Se a chave não existir, informe:
"Roteiro salvo. Para gerar o vídeo com avatar, copie o script no app.heygen.com. Para gerar automaticamente, configure HEYGEN_API_KEY no arquivo .env."

### 6. Próximo Passo
"Para Reels, grave direto pelo celular seguindo o roteiro. Use `/conteudo-social` para criar o plano completo de conteúdo."
