# Output [2] — Performance & Funil

Visão narrada de **performance comparada e mapa de funil** para um período. O aluno entende quem é melhor, quem é pior, e onde o funil vaza.

---

## Perguntas que cobre

- "Me dá um ranking das 5 melhores campanhas por ROAS dos últimos 30 dias"
- "Compara o CPM de maio vs. abril — ficou mais caro anunciar?"
- "Qual posicionamento (Feed, Stories, Reels) está trazendo mais resultado?"
- "Me mostra o funil completo: impressões → cliques → conversões de cada campanha"
- "Quem são meus winners e meus losers no período?"

---

## Dados necessários

Pedir ao `/trafego-insights`:
- Escopo: `conta_completa` para ranking, `campanha_id` para drill-down de funil
- Período: padrão 30 dias (perguntar)
- Comparativo: período anterior equivalente (cálculo via `comparar_periodos`)
- Breakdowns: `publisher_platform`, `platform_position` (uma chamada cada, cacheadas)
- Função utilitária: `ranking_top_n(metric, n)` e `funil_por_campanha(id)`

---

## O que entregar

### Bloco 1. Ranking de winners e losers
Pedir ao aluno qual métrica priorizar (ROAS, CPL, CPA) ou usar default da trilha (perpétuo = ROAS, lançamento = CPL).

```
🏆 TOP 5 WINNERS (por ROAS, últimos 30d)
1. {campanha} — ROAS X.Xx | CPA R$ X | spend R$ X
2. ...

🛑 TOP 5 LOSERS (mesmo critério, ordem inversa)
1. {campanha} — ROAS X.Xx | CPA R$ X | spend R$ X
   ⚠️ candidata a pausar via /trafego-otimizar
```

### Bloco 2. Comparativo CPM período vs período anterior
```
📊 CPM EVOLUTION
Período atual:    R$ X (média)
Período anterior: R$ Y
Variação:         {+/-}X.X%  [🟢/🟡/🔴]

Leitura:
- Subiu > 20% → leilão ficou caro, hipóteses: nova competição, criativo fadigado, época sazonal
- Estável → conta saudável
- Caiu > 10% → algo melhorou (criativo novo, novo público, fora da sazonalidade)
```

### Bloco 3. Posicionamento (Feed, Stories, Reels)
Pedir breakdown `publisher_platform` + `platform_position`.

```
📱 POSICIONAMENTO (últimos X dias)
| Posição              | Spend  | CPA     | CTR   | Resultado |
|---------------------|--------|---------|-------|-----------|
| Instagram Reels     | R$ X   | R$ Y    | X%    | N         |
| Instagram Feed      | R$ X   | R$ Y    | X%    | N         |
| Facebook Feed       | R$ X   | R$ Y    | X%    | N         |
| Instagram Stories   | R$ X   | R$ Y    | X%    | N         |

Vencedor: {posição} — CPA X% mais barato que a média
Perdedor: {posição} — sugestão: testar pausar via /trafego-testes
```

### Bloco 4. Funil completo (top 1 winner OU campanha escolhida)

Pedir ao `/trafego-insights` `funil_por_campanha(id)`:

```
🔻 FUNIL — {campanha}, últimos 30d

IMPRESSÃO          186.000
       ↓ Hook 35% (🟢)        — Urgência Oculta funcionando
CLIQUE              3.348
       ↓ CTR 1.8% (🟢)         — Identidade do Produto OK
LP VIEW             2.578
       ↓ LPVR 77% (🟢)         — promessa do ad alinhada com a página
LEAD                51
       ↓ Opt-in 2.0% (🟠)      — Isca Digital pode melhorar
CHECKOUT INICIADO   89
       ↓ Offer 3.4% (🟢)       — Oferta convertendo
COMPRA              22
       ↓ Connect 43% (🟢)      — Furadeira + Decorados convencem

ROAS final: 2.04x
```

---

## Protocolo padrão

1. **Diagnóstico** — winners, losers, posicionamento vencedor, etapas saudáveis e gargalo do funil.
2. **Causa provável** — relação entre os dados (ex: "CPM subiu 18% e Connect Rate caiu 30%, dobro de vento contra").
3. **No VTSD, isso significa…** — qual elemento do método está em jogo (Identidade do Produto, Quadro na Parede, Decorados, etc.).
4. **Ação recomendada** — handoff específico (escalar winner, pausar loser, refazer criativo, testar posicionamento).

---

## Handoffs típicos

| Achado | Para onde |
|---|---|
| Top 1 winner com ROAS > 3x e freq < 3 | `/trafego-escalar` (escalar com cautela) |
| Top loser com gasto alto + zero conversão | `/trafego-otimizar` (atalho: pausar com filtro) |
| Posicionamento perdedor identificado | `/trafego-testes` (ab-posicionamento) |
| Gargalo em Hook Rate | `/trafego-testes` (ab-criativo, novo Urgência Oculta) |
| Gargalo em Offer Rate | revisão de página de vendas (não é skill de tráfego, mencionar `/copy-pagina`) |
| CPM subindo 20%+ semana a semana | output [3] Criativos & Copy (provável fadiga) |
