# Output [5] — Timing & Sazonalidade

Quando seus anúncios performam melhor: dia da semana, horário, mês a mês, datas comemorativas, fim de semana.

## Perguntas que cobre

- "Meus resultados mudam no começo vs. final do mês? O público compra mais perto do salário?"
- "Datas comemorativas afetaram meu CPM? (Black Friday, Dia das Mães, etc.)"
- "Qual dia da semana eu deveria aumentar o orçamento?"
- "Feriado atrapalha ou melhora meus resultados?"
- "Qual horário do dia meus anúncios performam melhor?"
- "Meus resultados de segunda a sexta são diferentes do fim de semana?"

## Dados necessários

- Breakdown `hourly_stats_aggregated_by_advertiser_time_zone` para mapa por hora
- Métricas por dia (sem breakdown) para padrão semanal e mensal
- Função utilitária `historico_mensal(metric, n_meses=6)` para tendência longa
- Período: 30 dias (perguntar — 60d/90d se quiser pegar datas comemorativas)

## O que entregar

### Bloco 1. Padrão por dia da semana
```
📅 DIA DA SEMANA — últimos 30d (média)

| Dia       | Spend | CPA  | ROAS | Conversões |
|-----------|-------|------|------|-----------|
| Segunda   | R$ X  | R$ Y | X.Xx | N         |
| Terça     | R$ X  | R$ Y | X.Xx | N         |
...
| Sábado    | R$ X  | R$ Y | X.Xx | N         |
| Domingo   | R$ X  | R$ Y | X.Xx | N         |

Top 3 dias: {lista}
Bottom 2 dias: {lista}

Útil dias 1-10 vs 21-31 (efeito salário)? {sim/não, com dado}
```

### Bloco 2. Padrão por horário
```
🕐 HORÁRIO — últimos 30d

Mapa por faixa (00h-06h, 06h-12h, 12h-18h, 18h-24h):
| Faixa     | Spend | CPA  | ROAS |
|-----------|-------|------|------|
| 00h-06h   | ...   | ...  | ...  |
| 06h-12h   | ...   | ...  | ...  |
| 12h-18h   | ...   | ...  | ...  |
| 18h-24h   | ...   | ...  | ...  |

Pico de conversão: {horário}
Vale (CPA alto): {horário} → considerar pausar nesse intervalo
```

### Bloco 3. Comparativo mês a mês (CPM e CPA)
Usar `historico_mensal` para últimos 6 meses:
```
📈 EVOLUÇÃO MENSAL

| Mês     | CPM  | CPA   | Spend | Compras |
|---------|------|-------|-------|---------|
| 2025-12 | R$ X | R$ Y  | R$ Z  | N       |
| 2026-01 | R$ X | R$ Y  | R$ Z  | N       |
...
| 2026-05 | R$ X | R$ Y  | R$ Z  | N       |

Tendência: {subindo/estável/caindo}
Mês mais caro de CPM: {mês} (provável causa: {Black Friday / Dia das Mães / sazonalidade do nicho})
Mês de melhor CPA: {mês} (vale documentar o que funcionou)
```

### Bloco 4. Datas comemorativas (se aplicável)
Detectar dias com CPM > 30% acima da média e cruzar com calendário comercial brasileiro:
- Black Friday (última semana de novembro)
- Natal (semana 23-24/12)
- Dia das Mães (segunda semana de maio)
- Dia dos Pais (segunda semana de agosto)
- Volta às aulas (primeira quinzena de fev/agosto)

```
🎉 DATAS COMEMORATIVAS no período
- {data}: CPM +X%, CPA +Y%. {Estratégia: pausar / aproveitar leilão alto / mudar oferta}
```

## Protocolo padrão

1. **Diagnóstico** — picos e vales identificados em cada dimensão.
2. **Causa provável** — explicação por sazonalidade, comportamento do público, competição no leilão.
3. **No VTSD, isso significa…** — "Seu público compra mais aos fins de semana = ele consome no momento de descanso. Reflita isso na linguagem da Identidade do Comunicador" / "Pico das 21h = horário de cama, oferta deve ressoar com o estado emocional desse momento".
4. **Ação recomendada** — aplicar dayparting via `/trafego-regras` (programação liga/pausa) ou redistribuir budget via `/trafego-otimizar`.

## Handoffs típicos

| Achado | Para onde |
|---|---|
| Vale claro (horário ou dia com CPA alto) | `/trafego-regras` (liga-pausa-schedule) |
| Pico previsível em data comemorativa | `/trafego-regras` (regra automática para reduzir budget no pico de CPM) |
| Salário começo/fim do mês | `/trafego-otimizar` (redistribuir budget) ou `/trafego-regras` (regra: aumentar budget +20% nos dias 1-10) |
