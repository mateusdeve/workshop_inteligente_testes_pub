---
name: workshop-marketing:criativo-de-imagem
description: Gerar prompts detalhados para criação de imagens de anúncios, posts e criativos usando Midjourney, DALL-E ou Freepik AI. Inclui direção criativa completa.
---

# Criativo de Imagem — Gerador de Prompts Visuais

Gera prompts detalhados para ferramentas de IA (Midjourney, DALL-E, Freepik AI) e direção criativa para imagens de anúncios e posts.

## Usage

```
/criativo-de-imagem
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md` e anúncios existentes em `entregas/anuncios/`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4 — Uso:**

```
Para que vai usar a imagem?

1. Anúncio Meta Ads (feed ou stories)
2. Post Instagram (feed ou carrossel)
3. Capa de conteúdo (YouTube, blog)
4. Banner de página

Digite o número:
```

```
--- Bloco 1/4 concluído ---
Uso: [uso escolhido]
Próximo: Ferramenta
---
```

**Bloco 2/4 — Ferramenta:**

```
Qual ferramenta de geração?

1. Freepik AI
2. Midjourney
3. DALL-E
4. Direção criativa para designer

Digite o número:
```

```
--- Bloco 2/4 concluído ---
Uso: [uso]
Ferramenta: [ferramenta]
Próximo: Estilo visual
---
```

**Bloco 3/4 — Estilo Visual:**

```
Qual o estilo visual?

1. Moderno e clean
2. Minimalista
3. Vibrante e colorido
4. Profissional/corporativo
5. Premium/luxo
6. Outro (descreva)

Digite o número:
```

```
--- Bloco 3/4 concluído ---
Uso: [uso]
Ferramenta: [ferramenta]
Estilo: [estilo]
Próximo: Texto na imagem
---
```

**Bloco 4/4 — Texto na Imagem:**

```
Que texto deve aparecer na imagem?
(ex: "Fale inglês em 90 dias", "Garanta sua vaga", ou "nenhum")
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Uso: [uso]
- Ferramenta: [ferramenta]
- Estilo: [estilo visual]
- Texto: [texto na imagem]
- Quantidade: 3-5 variações de prompt

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**Para cada imagem, gere:**

1. **Prompt completo** (otimizado para a ferramenta escolhida)
2. **Direção criativa:**
   - Conceito visual
   - Paleta de cores
   - Estilo fotográfico ou ilustrativo
   - Composição e enquadramento
   - Texto overlay sugerido
3. **Especificações técnicas:**
   - Dimensões
   - Formato
   - Zona segura para texto

**Gere 3-5 variações** de prompt para teste.

### 4. Salvar Prompts
`entregas/criativos/prompts-[tipo]-[produto].md`

### 5. Gerar Imagens Automaticamente (se configurado)
Leia `.env` e verifique se existe `FREEPIK_API_KEY`.

Se existir, para cada prompt gerado:
1. Envie o prompt para a API do Freepik via `curl`:
```bash
curl -X POST "https://api.freepik.com/v1/ai/text-to-image" \
  -H "x-freepik-api-key: $FREEPIK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "PROMPT_AQUI", "num_images": 1, "image": {"size": "square"}}'
```
2. Salve as imagens geradas em `entregas/criativos/imagem-[numero]-[produto].png`
3. Informe: "Imagens geradas e salvas em entregas/criativos/."

Se a chave não existir, informe:
"Prompts salvos. Copie e cole na ferramenta de IA escolhida (Freepik, Midjourney, DALL-E). Para gerar automaticamente, configure FREEPIK_API_KEY no arquivo .env."

### 6. Próximo Passo
"Use `/anuncio` para criar a copy dos anúncios que usarão essas imagens."
