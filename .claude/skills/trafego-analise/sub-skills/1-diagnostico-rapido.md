# Output [1] — Diagnóstico Rápido (60 segundos)

Visão geral pragmática que cabe numa olhada. Para o aluno que abre o Workshop e quer saber: "está tudo bem com minhas campanhas hoje?".

---

## Perguntas que cobre

- "Qual campanha está queimando mais dinheiro sem resultado?"
- "Tem algum anúncio com frequência alta e CTR caindo? (fadiga de criativo)"
- "Quanto gastei no total essa semana vs. semana passada?"
- "Alguma campanha estourou o orçamento diário hoje?"
- "Como está a saúde geral da minha conta? (Health Score)"

---

## Dados necessários

Pedir ao `/trafego-insights`:
- Escopo: `conta_completa`
- Período: padrão últimos 7 dias (perguntar se aluno quer outro)
- Comparativo: período anterior equivalente (semana anterior)
- Breakdown: nenhum (`base`)

---

## O que entregar

### Bloco 1. Resumo de 60 segundos
```
🔍 DIAGNÓSTICO RÁPIDO. {nome conta} — últimos 7 dias

Gasto: R$ X    (vs. R$ Y semana anterior, {+/-X}%)
Compras/Leads: N    (vs. M, {+/-X}%)
ROAS médio: X.Xx    (vs. Y.Yx, {+/-X}%)
CPA médio: R$ X    (vs. R$ Y, {+/-X}%)

Health Score: XX/100 [🟢/🟡/🟠/🔴]
```

### Bloco 2. Top 3 sinais críticos (em ordem de urgência)

Para cada sinal:
- **O que é:** 1 frase
- **Quanto custa:** valor concreto (R$/dia ou % do gasto)
- **Próxima ação:** comando específico (ex: "Pause via /trafego-otimizar — atalho `pausar com filtro`")

Categorias de sinal a checar:
1. **Queima de dinheiro** — campanha com gasto > R$ 100 e zero conversão nos últimos 7d
2. **Fadiga de criativo** — anúncio com frequência > 4 e CTR caindo > 15% week-over-week
3. **Saturação de público** — adset cold com frequência ≥ 5
4. **Estouro de budget** — campanha que ultrapassou daily budget hoje
5. **Below average rankings** — anúncio com 2+ rankings Meta `below_average`

### Bloco 3. Health Score detalhado

Aplicar fórmula:

| Dimensão | Peso | Score 0-100 |
|---|---|---|
| Diversidade criativa (Mandala) | 20% | tipos ativos / 18 |
| Saúde de públicos | 20% | freq < 4 + balance HOT/COLD/SUPERCOLD |
| Eficiência de funil | 25% | etapas saudáveis / 7 |
| Performance financeira (ROAS, CPA vs benchmark) | 25% | métricas no range ideal |
| Consistência temporal | 10% | desvio CPL < 30% WoW |

Score final: 🟢 85-100 / 🟡 70-84 / 🟠 50-69 / 🔴 0-49.

### Bloco 4. Próximo passo VTSD
Em 1 linha, qual output rodar a seguir conforme o sintoma:
- Score < 50 → output [8] Problemas Ocultos
- Fadiga detectada → output [3] Criativos & Copy
- Gargalo financeiro → output [2] Performance & Funil
- Tudo verde → output [9] Orçamento & Projeção (quem escalar?)

---

## Protocolo padrão (obrigatório)

1. **Diagnóstico** — números brutos do bloco 1.
2. **Causa provável** — o que os top 3 sinais sugerem em conjunto.
3. **No VTSD, isso significa…** — ex: "Dois sinais de fadiga + 1 público saturado = a Identidade do Consumidor está esgotando, hora de criar nova"; ou "Score 92 + ROAS subindo = candidato perfeito para escalar via `/trafego-escalar`".
4. **Ação recomendada** — 1 a 3 ações concretas com handoff.

---

## Handoffs típicos

| Sinal predominante | Para onde mandar |
|---|---|
| Queima de dinheiro | `/trafego-otimizar` (ações em lote: pausar campanhas com gasto > X e zero conversão) |
| Fadiga de criativo | `/trafego-testes` (rodar A/B de criativo novo) ou `/trafego-publicos` (criar nova audience) |
| Conta saudável + ROAS alto | `/trafego-escalar` (aumentar top N) |
| Estouro de budget recorrente | `/trafego-regras` (criar regra automática para frear) |
| Pixel sem atividade | `/trafego-pixel` (diagnóstico aprofundado) |
