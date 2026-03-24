---
name: workshop-marketing:texto-de-venda
description: Criar textos persuasivos usando Light Copy e elementos literários da metodologia VTSD. Headlines, VSL, cartas de venda, bullets de venda e CTAs.
---

# Texto de Venda — Light Copy Profissional

Cria textos persuasivos no estilo Light Copy (argumentativo, lógico, conversacional, não óbvio).

## Usage

```
/texto-de-venda
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md` e `meu-negocio/idconsumidor.md` se existir. Use o Quadro, Furadeira, Decorados e Urgências Ocultas como base.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Tipo de Texto:**

```
Qual tipo de texto?

1. Headlines + Subheadlines
2. Carta de vendas completa
3. Script de VVV (Vídeo de Vendas de Valor)
4. Bullets de venda (Decorados)
5. CTAs variados
6. Copy completa da página 8D

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Tipo: [tipo escolhido]
Próximo: Objetivo
---
```

**Bloco 2/3 — Objetivo:**

```
Qual o objetivo desse texto?

1. Vender produto
2. Captar leads
3. Inscrever em evento
4. Engajar audiência

Digite o número:
```

```
--- Bloco 2/3 concluído ---
Tipo: [tipo]
Objetivo: [objetivo]
Próximo: Extras
---
```

**Bloco 3/3 — Extras:**

```
Tem promoção, bônus ou urgência para incluir?
(ex: "Bônus de lançamento até sexta", "Desconto de 30%", "Últimas 10 vagas")
Se não tiver, digite "não".
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Tipo: [tipo de texto]
- Objetivo: [objetivo]
- Extras: [promoção/bônus ou nenhum]
- Produto: [nome do produto do perfil]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

Aplique as regras do Light Copy (skill vtsd-completo):
- Argumentativo, objetivo e lógico
- Conversacional — parece conversa, não venda
- Não óbvio — curiosidade a cada linha
- ❌ Sem ponto de exclamação
- ❌ Sem perguntas no gancho
- ❌ Sem "mesmo que" / "sem precisar" como muletas
- ❌ Sem promessas vagas

Use os 26 elementos literários quando apropriado:
- Setup + Punchline, Hipérbole, Metáfora Visual
- Apelo ao Cotidiano, Tríade Cômica, Antítese
- Consulte skill vtsd-completo para a lista completa

**Para VVV, siga a estrutura:**
1. Abertura (gancho)
2. Conexão (história)
3. Problema (dor amplificada)
4. Paliativo (o que já tentaram)
5. Solução (método/Furadeira)
6. Prova (resultados)
7. Oferta (entregáveis, bônus, garantia)
8. CTA

### 4. Salvar
`entregas/textos-de-venda/[tipo]-[produto].md`

### 5. Próximo Passo
"Texto salvo. Use `/pagina-de-vendas` para transformar em página profissional, ou `/anuncio` para criar anúncios."
