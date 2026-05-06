# Output [4] — Geo & Demografia

Análise narrada de quem está convertendo: idade, gênero, estado, cidade, capital vs interior.

---

## Perguntas que cobre

- "Qual estado/cidade está me trazendo as conversões mais baratas?"
- "Tem região onde estou gastando muito e não vem resultado?"
- "Homens ou mulheres convertem mais nas minhas campanhas?"
- "Qual faixa etária é meu ponto cego — gasto pouco e poderia explorar?"
- "Meus anúncios performam melhor em capitais ou no interior?"

---

## Dados necessários

Pedir ao `/trafego-insights` 4 chamadas (cacheadas):
1. Breakdown `age, gender` → split demográfico
2. Breakdown `country` → top-level (esperado: Brasil >95%)
3. Breakdown `region` → estados
4. Breakdown `dma` → área metropolitana (capital vs interior)

Período: padrão 30 dias (perguntar).

---

## O que entregar

### Bloco 1. Demografia (idade + gênero)
```
🌎 DEMOGRAFIA — últimos 30d

| Idade  | Gênero | Spend | CPA  | ROAS | Conversões |
|--------|--------|-------|------|------|-----------|
| 25-34  | F      | R$ X  | R$ Y | X.Xx | N         |
| 25-34  | M      | R$ X  | R$ Y | X.Xx | N         |
| 35-44  | F      | R$ X  | R$ Y | X.Xx | N         |
...

Vencedor: {idade-gênero} — CPA X% mais barato que a média
Ponto cego: {idade-gênero} — gasto baixo (R$ X) mas CPA atrativo (R$ Y) → testar aumentar
Buraco: {idade-gênero} — gasto alto (R$ X) e CPA caro (R$ Y) → testar excluir
```

### Bloco 2. Geografia (estado)
```
🗺️ POR ESTADO — top 10 por gasto

| Estado | Spend | CPA | ROAS | Decisão |
|--------|-------|-----|------|---------|
| SP     | R$ X  | ... | ...  | manter  |
| RJ     | R$ X  | ... | ...  | escalar |
| MG     | R$ X  | ... | ...  | revisar |
...

Top 3 estados que convertem mais barato: {lista}
Estados onde gasto > 5% e ROAS < 1.5x: {lista — candidatos a excluir}
```

### Bloco 3. Capital vs interior (via DMA)
```
🏙️ CAPITAL vs INTERIOR

Capital ({DMAs principais}):     R$ X spend, CPA R$ Y, ROAS X.Xx
Interior (demais DMAs):          R$ X spend, CPA R$ Y, ROAS X.Xx

Leitura: {qual perfil é mais barato e por quanto}
```

### Bloco 4. Ponto cego (cluster sub-explorado)
Identificar combinação demográfica + geográfica com:
- Gasto < 5% do total
- CPA dentro do range ideal
- Volume não-trivial (≥ 5 conversões)

Esse cluster é candidato a **expansão de público** ou novo adset segmentado.

---

## Protocolo padrão

1. **Diagnóstico** — vencedores e perdedores em cada dimensão.
2. **Causa provável** — por que esse cluster converte (compra mais alinhada com Identidade do Consumidor declarada no perfil.md? ou descoberta nova?).
3. **No VTSD, isso significa…** — "A Identidade do Consumidor real do produto pode estar diferente da declarada no perfil.md. Ex: você desenhou para mulheres 35-44 mas quem compra são homens 45-54. Hora de revisar o perfil ou criar nova segmentação".
4. **Ação recomendada** — handoff para skill executora.

---

## Handoffs típicos

| Achado | Para onde |
|---|---|
| Cluster vencedor sub-explorado | `/trafego-publicos` (criar audience custom para esse cluster) + `/trafego-testes` (duplicar adset variando segmentação) |
| Estado/cidade com gasto alto e ROAS baixo | `/trafego-otimizar` (ajustar exclusão geográfica do adset) |
| Ponto cego promissor | `/trafego-testes` (duplicar-variando audiência para esse cluster) |
| Identidade do Consumidor real ≠ declarada | sugerir revisão do `perfil.md` do produto (não é skill de tráfego, mencionar `/produto-concepcao`) |

---

## Limitações

- `dma` no Brasil é menos rico que nos EUA. Para split capital/interior fino, pode precisar combinar com `region` + lista manual de capitais.
- Meta agrupa idades em buckets fixos: 18-24, 25-34, 35-44, 45-54, 55-64, 65+. Não dá para pedir "30-32".
- Gênero da Meta é declarado pelo usuário (não verificado). Em produtos onde o público real difere do declarado, dado pode estar enviesado.
