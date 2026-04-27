---
name: workshop-marketing:copy-social
description: Criar conteúdo para redes sociais. Carrossel, roteiro de Reels e linha editorial de 30 dias. Baseado nas Urgências Ocultas e Decorados do produto ativo.
---

# Conteúdo Social

Cria conteúdo usando Urgências Ocultas como fonte de temas e Light Copy como estilo.

## O Que Fazer

### 1. Contexto

Leia `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md` se existir.

Extraia internamente: Decorados, Urgências Ocultas (7 categorias, 10 itens cada), Baldes de Conteúdo do idconsumidor.

Verifique conteúdos existentes em `meus-produtos/{ativo}/entregas/criativos/` para evitar repetir urgências já usadas.

### 2. Entrevista (UMA pergunta por vez)

**Bloco 1/3 — Tipo:**

```
O que quer criar?

1. Carrossel (7-10 slides)
2. Roteiro de Reels (30-60s)
3. Linha editorial (30 dias)

Digite o número:
```

**Bloco 2/3 — Rede:**

```
Para qual rede?

1. Instagram
2. TikTok
3. LinkedIn
4. Várias

Digite o número:
```

**Bloco 3/3 — Objetivo:**

```
Objetivo principal?

1. Educar (entregar algo prático)
2. Engajar (gerar comentários e compartilhamentos)
3. Vender (levar para página ou checkout)
4. Atrair seguidores

Digite o número:
```

**Confirmação:**

```
Resumo:
- Tipo: [tipo]
- Rede: [rede]
- Objetivo: [objetivo]
- Base: Urgências Ocultas do perfil

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração por Tipo

**Regras de estilo (aplicar em todo conteúdo):**

Antes de escrever, leia `.claude/skills/revisora/references/manual-copy.md` e aplique. Toda peça passa pela skill `revisora` antes de ir ao usuário.

- Gancho: afirmação contra-intuitiva, paradoxo ou revelação. NUNCA pergunta.
- Entregar valor real dentro do post: quem lê aprende ou se reconhece.
- Produto não aparece nos primeiros slides ou nos primeiros 3 segundos.
- Uma ideia por post, um CTA por post.
- Sem travessão em nenhuma frase.

---

**Carrossel (7-10 slides):**

- Slide 1: gancho forte (elemento literário + abertura não óbvia)
- Slides 2-8: cada slide avança o argumento com base em Urgência Oculta ou Decorado. Sem slide que parafraseia o anterior.
- Slide final: CTA + branding mínimo
- Caption: mínimo 2 parágrafos de desenvolvimento antes do CTA, com hashtags relevantes

---

**Roteiro de Reels (30-60s):**

```
[0-3s]   GANCHO    — Afirmação não óbvia. Texto na tela + fala simultâneos.
[4-15s]  TEASE     — Expande o gancho, contextualiza o problema.
[16-42s] ENTREGA   — Ensina ou revela algo concreto. NUNCA apenas prometer.
[43-48s] REGANCHO  — Texto síntese (âncora para quem assiste sem som).
[49-55s] CTA       — Convite direto e leve.
```

---

**Linha editorial (30 dias):**

- Distribuir temas entre as 7 categorias de Urgências Ocultas
- Distribuir nos Baldes de Conteúdo do idconsumidor (se existir)
- Alternar formatos: carrossel, reels, stories, post estático
- CTAs estratégicos progredindo: seguidores, leads, vendas
- Para cada dia: tema, urgência ou decorado de origem, formato e objetivo

### 4. Aprovação e Salvar

Mostrar o conteúdo gerado e perguntar:

```
1. Aprovar e salvar
2. Quero ajustar algo
```

Após aprovação, salvar em:
`meus-produtos/{ativo}/entregas/criativos/[tipo]-[produto].md`

### 5. Próximo Passo

"Use `/criativo` para gerar as artes que acompanham esse conteúdo."
