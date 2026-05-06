# Output [8] — Problemas Ocultos

Achados que normalmente passam despercebidos: ad sets com configuração quebrada, audiências micro, anúncios desaprovados, pixel sem atividade, públicos de remarketing secando.

## Perguntas que cobre

- "Tem algum ad set que nunca gastou nada? Pode estar com problema de configuração"
- "Tem anúncio com muita impressão mas zero clique? Criativo pode estar ruim"
- "Algum conjunto de anúncios tem público menor que 1.000 pessoas?"
- "Tem campanha ativa sem nenhuma conversão nos últimos 7 dias?"
- "Estou com algum anúncio desaprovado que eu nem percebi?"
- "Meus pixels estão recebendo eventos? Tem algum sem atividade?"
- "Meus públicos de remarketing estão sendo alimentados ou estão secando?"

## Dados necessários

- Listagem completa de campanhas/adsets/ads com status `effective_status`, `delivery_info`, `disapproved_reason`
- Tamanho estimado de audiência por adset (`estimated_audience_size` se disponível)
- Diagnóstico de pixel via `/trafego-pixel` (status, último disparo, atividade 7d)
- Audiências de retargeting com `estimated_audience_size` ao longo do tempo

## O que entregar

### Bloco 1. Ad sets com gasto zero há 7+ dias
```
🔌 AD SETS QUE NÃO GASTARAM (últimos 7d, status ACTIVE)

| Adset    | Campanha | Última entrega | Provável problema |
|----------|----------|----------------|-------------------|
| {nome}   | {nome}   | há X dias      | público muito pequeno / criativo desaprovado / horário restrito |
...

Ação: investigar manualmente cada um. Maioria é bug de configuração do próprio criador.
```

### Bloco 2. Anúncios com impressão alta + 0 clique
```
👁️ ANÚNCIOS QUE APARECEM MAS NINGUÉM CLICA

| Anúncio | Impressões | Cliques | CTR  |
|---------|-----------|---------|------|
| {nome}  | 12.500    | 0       | 0%   |
...

Critério: > 5.000 impressões e 0 cliques nos últimos 7d.
Provável: criativo não comunica, link errado ou audience completamente fora.
Ação: pausar via /trafego-otimizar e refazer via /trafego-testes.
```

### Bloco 3. Audiências micro (< 1.000 pessoas)
```
🎯 ADSETS COM AUDIÊNCIA PEQUENA (< 1.000 estimadas)

| Adset    | Tamanho estimado | Status |
|----------|------------------|--------|
| {nome}   | 750              | ACTIVE |
...

Risco: audiência micro não roda. Algoritmo não tem espaço para otimizar.
Solução: combinar interesses, ampliar geo, ou usar Advantage+ Audience.
```

### Bloco 4. Campanhas ativas sem conversão nos últimos 7d
```
💸 ATIVAS SEM CONVERSÃO (últimos 7d)

| Campanha | Spend 7d | Conversões | Status |
|----------|----------|-----------|--------|
| {nome}   | R$ 240   | 0         | ACTIVE |
...

Ação: pausar via /trafego-otimizar (atalho pausar com filtro: conversoes=0 AND spend>50).
```

### Bloco 5. Anúncios desaprovados
```
🚫 ANÚNCIOS DESAPROVADOS

| Anúncio | Motivo                    | Ação |
|---------|---------------------------|------|
| {nome}  | "Conteúdo restrito"       | recriar respeitando política, ou recurso |
| {nome}  | "Promessa irreal de saúde" | revisar copy via /copy-anuncio |
...

Importante: anúncios desaprovados podem afetar o score da conta inteira (Account Quality). Resolver rápido.
```

### Bloco 6. Diagnóstico de pixel (delegado para /trafego-pixel)
Resumo curto chamando `/trafego-pixel`:
```
📡 PIXEL

Pixels da conta: 2
- Pixel "{id}" → 🟢 ativo, último disparo há 12min
- Pixel "{id}" → 🔴 sem atividade há 9 dias

Investigação completa: rodar /trafego-pixel
```

### Bloco 7. Audiências de remarketing secando
```
💧 REMARKETING — TAMANHO AO LONGO DO TEMPO

| Audience            | Tamanho hoje | há 30d | Variação |
|---------------------|--------------|--------|----------|
| Visitantes 30d      | 18.500       | 24.000 | -23%     |
| Carrinho abandonado | 1.200        | 1.800  | -33%     |
| Compradores         | 580          | 540    | +7%      |
...

Audiences encolhendo > 20% = funil topo está esfriando OU evento do pixel quebrou.
Próximo: cruzar com diagnóstico de pixel acima.
```

## Protocolo padrão

1. **Diagnóstico** — lista priorizada dos problemas ocultos.
2. **Causa provável** — config quebrada, política, evento de pixel não disparando, criativo morto.
3. **No VTSD, isso significa…** — "Audience de carrinho abandonado caiu 33% e pixel está sem atividade. Provável: evento InitiateCheckout não está mais disparando. Sem isso, todo o retargeting do meio do funil para. A Furadeira está vazando antes do checkout".
4. **Ação recomendada** — handoffs específicos por categoria.

## Handoffs típicos

| Achado | Para onde |
|---|---|
| Ad set zero gasto | Investigação manual primeiro; depois `/trafego-otimizar` (pausar) ou `/trafego-publicos` (audiência pequena demais → recriar maior) |
| Impressão sem clique | `/trafego-otimizar` (pausar) + `/trafego-testes` (novo criativo) |
| Audiência micro | `/trafego-publicos` (recriar com critérios mais amplos ou usar Advantage+ Audience) |
| Sem conversão 7d | `/trafego-otimizar` (atalho pausar com filtro) |
| Desaprovado | `/copy-anuncio` (refazer copy) e/ou recurso manual no Meta |
| Pixel sem atividade | `/trafego-pixel` (diagnóstico completo) — pode precisar de `/pagina-pixel` para reinstalar |
| Remarketing secando | `/trafego-pixel` (verificar evento) + `/trafego-publicos` (recriar audience com critério maior) |
