---
name: workshop-marketing:anuncio
description: Criar pacotes completos de anúncios para Meta Ads e Google Ads usando a Mandala de 18 Tipos de Anúncios da metodologia VTSD. Inclui copy, direção criativa e estratégia de campanha.
---

# Anúncio — Mandala de 18 Tipos (VTSD)

Cria pacotes de anúncios usando os 18 tipos da Mandala VTSD + estrutura de campanha.

## Usage

```
/anuncio
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md` e persona.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4 — Plataforma:**
```
Qual plataforma?

1. Meta Ads (Facebook/Instagram)
2. Google Ads
3. Ambas

Digite o número:
```

```
--- Bloco 1/4 concluído ---
Plataforma: [plataforma]
Próximo: Objetivo
---
```

**Bloco 2/4 — Objetivo:**
```
Qual o objetivo dos anúncios?

1. Captar leads (email/WhatsApp)
2. Vender produto
3. Engajamento (seguidores, curtidas)
4. Views de vídeo

Digite o número:
```

```
--- Bloco 2/4 concluído ---
Plataforma: [plataforma]
Objetivo: [objetivo]
Próximo: Fase do funil
---
```

**Bloco 3/4 — Fase do Funil:**
```
Qual fase do funil?

1. Descoberta (público frio, não te conhece)
2. Relacionamento (já te segue, engajou)
3. Conversão (já viu página, baixou isca)
4. Remarketing (visitou checkout, não comprou)

Digite o número:
```

```
--- Bloco 3/4 concluído ---
Plataforma: [plataforma]
Objetivo: [objetivo]
Fase: [fase]
Próximo: Oferta
---
```

**Bloco 4/4 — Oferta:**
```
Tem oferta ou promoção específica para incluir?
(ex: "Lançamento com 30% off", "Bônus exclusivo essa semana")
Se não tiver, digite "não".
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Plataforma: [plataforma]
- Objetivo: [objetivo]
- Fase do funil: [fase]
- Oferta: [promoção ou nenhuma]
- Quantidade: 3 variações usando tipos diferentes da Mandala

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

Use a Mandala de 18 Tipos (skill vtsd-completo):

**Para Meta Ads, gere 3 variações usando tipos diferentes da Mandala:**
- Variação 1: [tipo escolhido] — ex: Comparação, Certo vs Errado
- Variação 2: [tipo escolhido] — ex: Prova, Demonstração
- Variação 3: [tipo escolhido] — ex: Problema-Solução, Curiosidade

**Cada variação inclui:**
- Texto principal (Light Copy — sem ponto de exclamação, sem perguntas no gancho)
- Headline (máx 40 caracteres)
- Descrição
- Direção criativa para imagem/vídeo
- CTA adequado à fase do funil

**CTAs por fase (VTSD):**
| Fase | CTA |
| --- | --- |
| Descoberta | Seguir, comentar, compartilhar |
| Relacionamento | Comentar, compartilhar |
| Conversão | Assistir aula, baixar isca, saiba mais |
| Remarketing | Comprar agora, garantir vaga |

**Estrutura de todo anúncio VTSD:**
- Gancho (premissa não óbvia)
- Desenvolvimento (1 parágrafo)
- CTA direto

**Para Google Ads:**
- 15 títulos (máx 30 caracteres)
- 4 descrições (máx 90 caracteres)
- Palavras-chave + negativas

### 4. Incluir Estratégia de Campanha
Ao final, sugira a estrutura de campanha:
- Campanha 1 — Descoberta (alcance/engajamento)
- Campanha 2 — Conversão (lookalike + interesses)
- Campanha 3 — Remarketing (visitantes + engajados)

### 5. Salvar
`entregas/anuncios/anuncios-[plataforma]-[produto].md`

### 6. Próximo Passo
"Anúncios salvos. Use `/criativo-de-imagem` para gerar prompts das imagens, ou `/pagina-de-vendas` para criar a página de destino."
