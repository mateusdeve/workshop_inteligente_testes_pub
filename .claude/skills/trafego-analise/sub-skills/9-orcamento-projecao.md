# Output [9] — Orçamento & Projeção

Visão de para onde o dinheiro vai e como redistribuir. Projeção do mês corrente e identificação de candidatos a escala.

## Perguntas que cobre

- "No ritmo atual, quanto vou gastar até o fim do mês?"
- "Qual campanha tem o melhor custo-benefício pra eu aumentar o orçamento?"
- "Redistribui meu orçamento: tira de quem performa mal e joga pra quem performa bem"
- "Quanto sobra de orçamento se eu pausar os perdedores?"

## Dados necessários

- Spend mês corrente até hoje + spend acumulado
- Daily budget de cada campanha ativa
- ROAS, CPA por campanha (últimos 14 ou 30d)
- Função utilitária `ranking_top_n` para identificar melhores e piores

## O que entregar

### Bloco 1. Projeção do mês
```
💰 PROJEÇÃO DO MÊS

Hoje: dia X de Y do mês
Gasto mês até agora: R$ Z (média de R$ K/dia)
Orçamento diário total ativo: R$ W
Projeção fim do mês: R$ Z + (Y-X) * W = R$ M

Comparativo com mês anterior:
Mês anterior total: R$ N
Variação projetada: {+/-}P%
```

### Bloco 2. Distribuição atual de budget
```
🥧 ONDE SEU DINHEIRO ESTÁ HOJE

| Campanha           | Daily budget | % do total | ROAS últ 14d | Veredicto |
|--------------------|--------------|------------|--------------|-----------|
| Campanha A         | R$ 200       | 40%        | 4.5x         | 🟢 escalar |
| Campanha B         | R$ 150       | 30%        | 2.8x         | 🟡 manter  |
| Campanha C         | R$ 100       | 20%        | 1.2x         | 🟠 revisar |
| Campanha D         | R$ 50        | 10%        | 0.6x         | 🔴 pausar  |
| TOTAL              | R$ 500       | 100%       | -            | -         |

Ineficiência identificada: Campanha D queima R$ 50/dia com ROAS abaixo de 1. Pausar libera R$ 1.500/mês.
```

### Bloco 3. Candidatos a escala
Filtrar campanhas com ROAS > 3x (perpétuo) ou ROAS > 2x (lançamento) + frequência < 3.5:
```
🚀 CANDIDATOS A ESCALA

| Campanha   | ROAS | Frequência | Headroom (estimado) |
|------------|------|------------|---------------------|
| Campanha A | 4.5x | 2.1        | até +50% sem queda significativa |
| Campanha E | 3.8x | 2.8        | até +30% (freq já alto) |
...

Ação: rodar /trafego-escalar para escalar com freios.
```

### Bloco 4. Redistribuição sugerida
```
💡 REDISTRIBUIÇÃO PROPOSTA (sem mudar gasto total)

Tirar:
- Campanha D: -R$ 50/dia (pausar)
- Campanha C: -R$ 30/dia (reduzir, manter rodando)

Colocar:
- Campanha A: +R$ 50/dia (winner mais saudável)
- Campanha E: +R$ 30/dia (winner secundário)

Estimativa de impacto:
- Mantém gasto total em R$ 500/dia
- ROAS médio sobe de X para Y
- CPA médio cai de R$ X para R$ Y
```

## Protocolo padrão

1. **Diagnóstico** — projeção do mês, distribuição atual, candidatos a escala, perdedores claros.
2. **Causa provável** — desbalanceamento histórico, falta de revisão recente, dependência excessiva de um winner.
3. **No VTSD, isso significa…** — "Caixa Rápido perpétuo precisa de no mínimo 70% do budget no winner. Você está em 40%, está pulverizando demais. Concentre".
4. **Ação recomendada** — handoffs para escalar/otimizar.

## Handoffs típicos

| Achado | Para onde |
|---|---|
| Candidato claro a escala | `/trafego-escalar` (vertical ou horizontal conforme tamanho do público) |
| Perdedor com gasto significativo | `/trafego-otimizar` (atalho `pausar com filtro` ROAS<X) |
| Pulverização (nenhuma campanha > 30% do budget) | `/trafego-otimizar` (consolidar via redistribuição manual) |
| Top 1 dependência > 70% | rodar output [3] Criativos & Copy para detectar fadiga antecipadamente; preparar duplicação via `/trafego-testes` (duplicar-variando) para criar redundância |
