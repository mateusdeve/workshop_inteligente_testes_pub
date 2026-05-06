# Output [6] — Investigação Profunda

Análises técnicas que vão além do óbvio: comportamento por dispositivo, primeiras 24h vs depois do aprendizado, tempo de visualização de vídeo, taxa de rejeição entre clique e ação no site.

## Perguntas que cobre

- "Qual o custo por resultado nas primeiras 24h de cada campanha nova vs. depois que sai do aprendizado?"
- "Meus anúncios performam diferente em Wi-Fi vs. dados móveis?"
- "Tem algum anúncio onde o custo por resultado subiu mais de 50% na última semana?"
- "Qual o tempo médio de visualização dos meus vídeos por posicionamento?"
- "Tem alguma campanha onde estou pagando caro por clique mas ninguém converte?"
- "Qual a taxa de rejeição entre clique no anúncio e ação no site?"
- "Quanto tempo em média leva do primeiro clique até a conversão?"

## Dados necessários

- Breakdown `device_platform` e `impression_device`
- Breakdown `publisher_platform` para tempo de vídeo por posicionamento
- Métricas de vídeo: `video_avg_time_watched_actions`, `video_p25_watched_actions`, `video_p50_watched_actions`, `video_p75_watched_actions`, `video_p100_watched_actions`
- Comparativo: primeiras 24h vs total da campanha (cálculo manual)
- Conversion windows: 1d_click vs 7d_click (revela tempo de decisão)

## O que entregar

### Bloco 1. Aprendizado — primeiras 24h vs maturada
Para campanhas com mais de 7d de vida:
```
🎓 FASE DE APRENDIZADO

| Campanha | CPA 24h | CPA pós-aprendizado | Variação |
|----------|---------|---------------------|----------|
| {nome}   | R$ X    | R$ Y                | -X%      |
...

Leitura: campanhas com queda > 30% após aprendizado = saudáveis (algoritmo encontrou o público).
Campanhas com aumento ou queda < 10% = aprendizado não convergiu, problema estrutural.
```

### Bloco 2. Dispositivo (mobile vs desktop, iPhone vs Android)
```
📱 DISPOSITIVO — últimos 30d

| Dispositivo        | Spend | CPA  | CTR  | ROAS |
|--------------------|-------|------|------|------|
| iPhone             | R$ X  | R$ Y | X%   | X.Xx |
| Android smartphone | R$ X  | R$ Y | X%   | X.Xx |
| Desktop            | R$ X  | R$ Y | X%   | X.Xx |
| Tablet             | R$ X  | R$ Y | X%   | X.Xx |

Vencedor: {dispositivo}
Limitação: Meta NÃO distingue Wi-Fi vs dados móveis na API pública. Para esse split, usar Pixel + GA4.
```

### Bloco 3. Subida brusca de CPA (alerta)
Listar anúncios cujo CPA subiu mais de 50% week-over-week:
```
⚠️ ANÚNCIOS COM CPA EM ALTA (>50% WoW)

| Anúncio | CPA semana atual | CPA semana anterior | Variação |
|---------|------------------|---------------------|----------|
| {nome}  | R$ X             | R$ Y                | +X%      |
...

Provável causa: fadiga (verificar frequência) ou perda de relevância (verificar rankings).
```

### Bloco 4. Tempo de vídeo por posicionamento
```
🎬 TEMPO MÉDIO DE VÍDEO

| Posição          | Avg watch time | Hold rate (50%) | Play-through (100%) |
|------------------|----------------|-----------------|---------------------|
| Reels            | XXs            | X%              | X%                  |
| Stories          | XXs            | X%              | X%                  |
| Feed             | XXs            | X%              | X%                  |
| In-stream Video  | XXs            | X%              | X%                  |

Posicionamento que retém mais: {posição} → indica que Decorados + Furadeira estão funcionando ali
```

### Bloco 5. Tempo do primeiro clique até conversão
Comparar atribuição 1d_click vs 7d_click:
```
⏱️ TEMPO DE DECISÃO

Conversões em 1d_click: N (X% do total)
Conversões em 7d_click: M (Y% do total)
Conversões entre 1d e 7d: M-N (Z% — público que precisa pensar antes)

Leitura:
- Maioria em 1d → produto de impulso, oferta direta funciona
- Maioria entre 1d-7d → produto de consideração, retargeting é decisivo
```

### Bloco 6. Taxa de rejeição (clique → ação na página)
```
🚪 RETENÇÃO DA PÁGINA

CTR no anúncio: X% (clicaram no link)
LPVR (LP views/cliques): Y% (página carregou)
Diferença = abandono entre clique e load: Z% — se > 30%, suspeita: página lenta ou redirect quebrado.

Próximo: rodar /pagina-performance para auditar peso e velocidade.
```

## Protocolo padrão

1. **Diagnóstico** — picos detectados, dispositivos vencedores, padrão de aprendizado.
2. **Causa provável** — fadiga, página lenta, público errado, oferta para produto de consideração tratada como produto de impulso.
3. **No VTSD, isso significa…** — "Hold rate baixo no Reels = Decorados não estão sendo percebidos no formato vertical curto. Adapte o criativo" / "Tempo médio até conversão > 5 dias = público precisa de retargeting; criar audience via /trafego-publicos".
4. **Ação recomendada** — handoffs específicos.

## Handoffs típicos

| Achado | Para onde |
|---|---|
| CPA sobe > 50% num anúncio específico | `/trafego-otimizar` (pausar e rodar `/trafego-testes` ab-criativo) |
| Aprendizado não convergiu | revisar segmentação ou criativos; usar `/trafego-publicos` (nova audience) |
| Dispositivo perdedor (ex: Android) | `/trafego-testes` (ab-posicionamento ou nova segmentação) |
| Tempo de decisão > 5 dias | `/trafego-publicos` (criar audience de retargeting) + `/trafego-testes` (campanha-remarketing) |
| Taxa de rejeição alta | `/pagina-performance` (auditar página) |
