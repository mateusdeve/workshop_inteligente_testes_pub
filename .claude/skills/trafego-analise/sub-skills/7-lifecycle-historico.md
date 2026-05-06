# Output [7] — Lifecycle & Histórico

Memória da conta. O que aconteceu nos últimos 6 meses, qual foi o melhor mês, quais campanhas pausadas valiam a pena reativar.

## Perguntas que cobre

- "Quais campanhas estão rodando há mais de 60 dias sem pausa? Precisam de refresh?"
- "Me mostra a evolução do meu CPA mês a mês nos últimos 6 meses"
- "Qual foi meu melhor mês de todos os tempos em ROAS?"
- "Tem campanha pausada que performava bem e vale a pena reativar?"
- "Qual foi o anúncio que mais gerou resultado na história da conta?"

## Dados necessários

- `historico_mensal(metric, n_meses=6)` para todas as métricas-chave (spend, cpa, roas, conversões)
- Listagem de TODAS as campanhas (incluindo `effective_status: PAUSED` e `ARCHIVED`) com data de criação e data de última pausa
- Para anúncios históricos: pedir `level=ad`, `incluir_arquivadas=true`, ordenar por `purchases` total

## O que entregar

### Bloco 1. Campanhas vivas há muito tempo (>60d)
```
🔄 CAMPANHAS LONGEVAS (rodando ininterrupto > 60d)

| Campanha | Dias ativa | CPA atual | CPA primeiro mês | Variação |
|----------|------------|-----------|------------------|----------|
| {nome}   | 92d        | R$ X      | R$ Y             | +Z%      |
...

Refresh recomendado se:
- CPA degradou > 30% vs primeiro mês
- Frequência média > 5
- Nenhum criativo novo nos últimos 30d

Ação: rodar /trafego-testes (ab-criativo) para introduzir variação.
```

### Bloco 2. Evolução mensal (gráfico em texto)
```
📈 EVOLUÇÃO 6 MESES — métrica: CPA

2025-12  ████████████ R$ 95,40  (3.200 spend, 33 compras)
2026-01  ██████████   R$ 88,20  (3.600 spend, 41 compras)
2026-02  █████████    R$ 82,50  (4.100 spend, 50 compras)
2026-03  ███████      R$ 71,20  (4.500 spend, 63 compras)  ← melhor
2026-04  █████████    R$ 86,40  (4.300 spend, 50 compras)
2026-05  ████████████ R$ 95,80  (4.800 spend, 50 compras)  ← atual

Tendência últimos 3 meses: deterioração
Causa provável: {hipótese}
```

### Bloco 3. Melhor mês de todos os tempos
```
🏆 MELHOR MÊS HISTÓRICO

Mês: 2026-03
ROAS: 4.8x
Spend: R$ 4.500
Compras: 63
CPA: R$ 71,20

O que estava ativo nesse mês que não está mais hoje:
- Campanha "{nome}" — pausada em {data}, motivo: {se houver registro}
- Anúncio "{nome}" — última atividade {data}
- Audience "{nome}" — não usada há {X dias}

Hipótese: voltar 1 ou 2 desses elementos pode reproduzir a performance.
```

### Bloco 4. Top 5 anúncios históricos (incluindo pausados)
Ordenar todos os anúncios já criados por total de purchases:
```
🥇 TOP 5 ANÚNCIOS DE TODOS OS TEMPOS

| Anúncio | Status atual | Total compras | CPA médio | Última atividade |
|---------|--------------|---------------|-----------|------------------|
| {nome}  | PAUSED       | 187           | R$ 64     | 2026-03-15       |
| {nome}  | ACTIVE       | 142           | R$ 78     | hoje             |
...

Candidatos a reativar: {nome} (pausado há {X dias} mas teve 187 compras com CPA R$ 64)
```

## Protocolo padrão

1. **Diagnóstico** — campanhas longevas, evolução mensal, melhor mês, anúncios históricos top.
2. **Causa provável** — degradação por fadiga, perda de público, perda de criativo vencedor, mudança de oferta.
3. **No VTSD, isso significa…** — "Sua melhor performance veio quando a Identidade do Comunicador estava encarnada no anúncio X. Esse anúncio sumiu, e o ROAS caiu junto. Refazer no estilo dele é caminho mais barato que recriar do zero".
4. **Ação recomendada** — refresh de longevas, reativação de pausados, replicação de elementos do melhor mês.

## Handoffs típicos

| Achado | Para onde |
|---|---|
| Campanha longeva com CPA degradado | `/trafego-testes` (ab-criativo) ou `/trafego-otimizar` (refresh defensivo) |
| Anúncio pausado com histórico forte | sugerir reativar manualmente OU duplicar via `/trafego-testes` (duplicar-variando) |
| Audience subutilizada do melhor mês | `/trafego-publicos` (recriar lookalike a partir dela) |
| Mês ruim recente | output [6] Investigação Profunda para entender o que mudou |
