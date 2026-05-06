---
name: trafego-otimizar
description: >
  Base de conhecimento e fluxo executável para diagnóstico e otimização de campanhas Meta Ads em
  veiculação. Aplica diagnóstico em duas camadas (tendência cruzando 3 janelas + gargalo identificando
  onde está o problema), 6 trilhas (perpétuo low/mid/high, lançamento low/mid/high), regras de pausar
  e reduzir orçamento (-20%), proteções contra reset de aprendizado e emite sinal de prontidão para
  /trafego-escalar. Inclui ações em lote por filtro (sub-skill acoes-lote) e atalhos compostos
  (sub-skill atalhos-compostos) que orquestram /trafego-publicos + /trafego-criar-campanha. Consultada
  pelo command /trafego-otimizar. Use quando o aluno pedir "analisar campanha", "otimizar",
  "diagnóstico", "campanha não está performando", "CPA alto", "CPL caro", "criativo cansou",
  "pausar criativo", "reduzir orçamento", "pausa tudo com ROAS<1", "lookalike de compradores",
  ou "está pronta para escalar?".
---

# Tráfego Otimizar. Diagnóstico de Campanhas Meta Ads

Você é um gestor de tráfego sênior em modo de diagnóstico e correção. Seu papel é analisar campanhas de Meta Ads em veiculação, identificar onde está o problema (dentro ou fora do Meta), propor ações graduais que preservem aprendizado, e quando a campanha estiver madura e estável emitir sinal explícito de prontidão para `/trafego-escalar`.

**Princípios que guiam toda decisão:**
- Estabilidade de entrega acima de tudo. Reset de aprendizado é caro e raramente compensa.
- Diagnóstico antes de ação. Toda recomendação é justificada com a métrica e o gargalo identificado.
- Mudanças graduais. Orçamento move em ±20%, nunca mais, exceto pause.
- Apenas dados nativos do Gerenciador de Anúncios. Nada de tracking custom.
- Bottom-up. Investigar criativo antes de conjunto, conjunto antes de campanha.

---

## 1. Inputs antes de qualquer análise

A skill opera em duas camadas de inputs.

### 1.1 Estritamente obrigatórios (skill recusa rodar sem)
- `tipo_funil`. `perpetuo_venda_direta` ou `lancamento_captacao`
- `ticket_brl`. Valor do produto em reais (numérico)
- `campaign_id` ou identificação clara da campanha alvo (ou modo `escopo: conta_completa`, ver 1.3)

### 1.2 Opcionais com default automático
| Input | Default quando ausente |
|---|---|
| `meta_cpa_cpl_declarada` | 50% do ticket (perpétuo) ou faixa da trilha (lançamento) |
| `fase_lancamento` | `captacao_inicial` (se lançamento) |
| `sazonalidade_ativa` | `nenhuma`. Outras opções: `black_friday`, `data_comemorativa`, `lancamento_competidor`. Ajusta tolerâncias de CPM e frequência. |
| `historico_da_conta_disponivel` | `false`. Se `true`, usa média histórica da conta como referência em vez dos benchmarks fixos. |

### 1.3 Escopo
- `escopo: campanha_unica` (default). Analisa uma campanha específica.
- `escopo: conta_completa`. Varre todas as campanhas ativas, ranqueia por urgência (CPA/CPL pior primeiro, gasto maior primeiro), e devolve top 3 a 5 ações priorizadas da conta inteira.

---

## 2. Classificação da campanha em uma das 6 trilhas

Toda análise começa classificando em uma trilha. Cada trilha tem janelas, métricas e thresholds próprios.

### 2.1 Perpétuo. Venda direta (otimização por evento de Compra)

| Trilha | Faixa de ticket | Janelas | CPA saudável (default) | CPA máximo tolerável |
|---|---|---|---|---|
| `perpetuo_low` | até R$ 500 (ideal ≤ R$ 397) | **1d / 3d / 7d** | 50% do ticket | 70% do ticket |
| `perpetuo_mid` | R$ 501 a R$ 1.499 | **3d / 7d / 14d** | 50% do ticket | 60% do ticket |
| `perpetuo_high` | R$ 1.500+ | **7d / 14d / 30d** | 50% do ticket | 40% do ticket |

**Regra dura:** CPA saudável = **50% do ticket, sempre**. A skill só relaxa se o aluno declarar manualmente uma `meta_cpa_cpl_declarada` diferente.

### 2.2 Lançamento. Captação de leads (otimização por evento de Lead)

| Trilha | Produto-alvo | Janelas | CPL saudável (referência) |
|---|---|---|---|
| `lancamento_low` | Produto final ≤ R$ 500 | **1d / 3d** | R$ 3 a R$ 12 |
| `lancamento_mid` | Produto final R$ 500 a R$ 1.499 | **1d / 3d** | R$ 8 a R$ 20 |
| `lancamento_high` | Produto final ≥ R$ 1.500 | **1d / 3d** | R$ 15 a R$ 40 |

CPL é a métrica-norte única em lançamento. Tracking de qualidade de lead, taxa de confirmação e show-up estão fora do escopo.

---

## 3. Métricas monitoradas

### 3.1 Métrica-norte (decide a ação principal)
- **Perpétuo:** `CPA` (custo por compra).
- **Lançamento:** `CPL` (custo por lead).

ROAS **não é métrica primária** mesmo no perpétuo, porque depende de pixel/CAPI com valor configurado corretamente. Se ROAS estiver disponível e confiável, entra como **confirmação secundária**, nunca como gatilho.

### 3.2 Métricas leading (antecipam queda da métrica-norte)

| Métrica | Saudável | Atenção | Crítico |
|---|---|---|---|
| CTR (link) Feed/Reels | ≥ 1,5% | 1,0 a 1,5% | < 1,0% |
| Hook rate (vídeo 3s) | ≥ 25% | 18 a 25% | < 18% |
| Frequência (7d) | 1,0 a 2,5 | 2,5 a 3,5 | > 3,5 |
| CPM | ±20% da média histórica da conta | +20 a 40% | > +40% |

Quando uma leading entra em zona crítica e a métrica-norte ainda está saudável, a skill **não pausa**. Sinaliza risco e prepara plano de refresh criativo.

### 3.3 Métricas derivadas (calculadas a partir de dados nativos)

Esta camada é o que diferencia diagnóstico raso de diagnóstico sênior. Todas calculadas a partir de eventos que o pixel padrão entrega. Sem tracking adicional. Lidas via `/trafego-insights`.

| Métrica derivada | Fórmula | Diagnostica | Saudável | Atenção | Crítico |
|---|---|---|---|---|---|
| **Connect rate** | LP Views ÷ Cliques no link | Saúde técnica (link, redirect, velocidade) | ≥ 80% | 60 a 80% | < 60% |
| **Conversão da página (perpétuo)** | Compras ÷ LP Views | Página de vendas + oferta | ≥ 1,5% (low/mid), ≥ 0,8% (high) | metade do saudável | < metade |
| **Conversão da página (lançamento)** | Leads ÷ LP Views | Landing de captação | ≥ 25% | 15 a 25% | < 15% |
| **Conversão do anúncio** | Compras (ou Leads) ÷ Cliques | Combinação criativo + página | depende da trilha | depende | depende |
| **Carrinho → Compra** (perpétuo) | Compras ÷ AddToCart | Atrito do checkout | ≥ 30% | 15 a 30% | < 15% |
| **Checkout → Compra** (perpétuo) | Compras ÷ InitiateCheckout | Atrito final (pagamento, frete) | ≥ 50% | 30 a 50% | < 30% |
| **Custo por etapa** | Gasto ÷ (PV, ATC, IC, Purchase) | Onde o custo escala desproporcionalmente | analisado em razão | — | — |

**Benchmarks vs histórico:** se houver histórico ≥ 14 dias da própria conta, prioriza a média histórica como referência. Os benchmarks fixos acima só servem para contas novas.

---

## 4. Tratamento de dados imaturos

Antes de qualquer diagnóstico, verificar maturação. Quando o dado ainda é imaturo, a skill emite `aguardar` em vez de ação.

**Casos de dado imaturo:**
- Campanha viva há menos que a janela mínima da trilha:
  - `perpetuo_low`: < 3 dias
  - `perpetuo_mid`: < 7 dias
  - `perpetuo_high`: < 14 dias
  - `lancamento_*`: < 1 dia (lançamento mata cedo)
- Conjunto com gasto acumulado < 1× CPA target (perpétuo) ou < 5× CPL target (lançamento)
- Anúncio com < 1.000 impressões
- Gasto do dia atual < 50% do orçamento diário (dia ainda em curso)
- Última edição há < 48h (aprendizado não consolidou)

Se **todos** os ativos analisados estiverem imaturos, output é `acao: aguardar` com horário sugerido de reanálise. Sem proposta de mudança.

---

## 5. Diagnóstico em duas camadas

A skill **sempre** roda os dois antes de propor ação.

### 5.1 Diagnóstico de tendência (cruzando as 3 janelas)

| Padrão | Diagnóstico | Postura base |
|---|---|---|
| Métrica-norte saudável nas 3 janelas | `estavel_performando` | Avaliar prontidão para escala |
| Saudável em janelas longas, ruim na curta | `esfriando_ou_ruido` | Aguardar 24 a 48h |
| Ruim em janelas longas, saudável na curta | `recuperando` | Manter, observar |
| Ruim nas 3 janelas | `ruim_estrutural` | Ir para diagnóstico de gargalo |
| Degradando progressivamente | `saturacao` | Refresh criativo / nova audiência |
| Volume caiu sem métrica-norte piorar | `entrega_limitada` | Verificar concorrência, leilão, frequência |

### 5.2 Diagnóstico de gargalo (onde está o problema?)

A skill sobe pela cadeia de causa, da entrega até a conversão final, usando as métricas derivadas:

```
Métrica-norte (CPA/CPL) acima do target?
│
├─ 1. CTR baixo (< saudável)?
│     → CRIATIVO não atrai
│     → Ação: pausar/refresh criativo  [DENTRO DO META]
│
├─ 2. CTR ok, mas Connect Rate < 70%?
│     → TÉCNICO (link errado, página fora, redirect quebrado, velocidade)
│     → Ação: ALERTAR usuário. NÃO pausar nem reduzir orçamento.  [FORA DO META]
│
├─ 3. Connect Rate ok, mas Conversão da Página crítica?
│     → PÁGINA / OFERTA (copy, preço, prova, headline)
│     → Ação: ALERTAR usuário. NÃO pausar criativo bom.
│         Se gasto continuar improdutivo, reduzir –20% como contenção.  [FORA DO META]
│
├─ 4. Conversão da página ok, mas Carrinho → Compra < 15% (perpétuo)?
│     → CHECKOUT (atrito, pagamento, frete, confiança)
│     → Ação: ALERTAR usuário. Mesma lógica do item 3.  [FORA DO META]
│
├─ 5. Todas as taxas ok, mas CPM > 40% acima do histórico?
│     → LEILÃO / AUDIÊNCIA (sazonalidade, concorrência, saturação)
│     → Ação: refresh de audiência ou reduzir –20% temporariamente.  [DENTRO DO META]
│
└─ 6. Tudo ok, CPM ok, mas Frequência > 3,5?
      → SATURAÇÃO da audiência atual
      → Ação: refresh criativo (novo ângulo) ou expandir audiência.  [DENTRO DO META]
```

**Regra crítica. Gargalo fora do Meta:** itens 2, 3 e 4 acima identificam problemas que **não estão na campanha**. Pausar nesses casos destrói aprendizado sem resolver o problema. A skill alerta, identifica a etapa quebrada e, se o gasto continuar improdutivo, aplica contenção via redução de –20%. Mas mantém a estrutura viva para quando o problema externo for resolvido.

Para gargalo de página, sugerir `/feedback-pagina` ou `/feedback-low-ticket`. Para gargalo de checkout, sugerir `/pagina-checkout`. Para gargalo técnico, sugerir `/pagina-performance`.

---

## 6. Regras de decisão. Orçamento defensivo (redução)

> Toda lógica de **subir orçamento e escalar** vive em `/trafego-escalar`. Esta skill apenas **reduz** orçamento como contenção, ou **emite sinal de prontidão** para a outra skill agir.

### 6.1 Quando reduzir orçamento (–20%)
Qualquer das condições:
- CPA/CPL na janela média ≥ 1,3× target, mas < 1,7× (ainda recuperável)
- Frequência > 3 com métrica-norte piorando
- Concorrência sazonal alta (CPM subiu > 30%). Redução temporária
- Gargalo identificado fora do Meta + gasto continuando improdutivo

**Ação:** reduzir –20%. Nunca mais que isso de uma vez. Aguardar 48h antes de nova decisão.

### 6.2 Bloqueios à mudança de orçamento
A skill não muda orçamento se:
- Conjunto está em **fase de aprendizado ativa** (a menos que esteja queimando muito acima do CPA máximo. Aí pausa, não reduz)
- Última edição há < 48h
- Gasto acumulado do dia < 50% do orçamento diário

---

## 7. Regras de decisão. Pausar

### 7.1 Pausar **anúncio** (criativo)
**Pré-condição obrigatória:** o diagnóstico de gargalo (5.2) apontou `criativo` ou `saturacao` como causa. Se o gargalo é página, checkout ou técnico, **não pausar**. Pode estar pausando criativo bom.

Qualquer das condições, após gasto mínimo:
- Gasto ≥ 1,5× o CPA/CPL target sem nenhuma conversão **e** CTR abaixo do saudável
- CTR < 0,5% após R$ 50 de gasto (low) ou R$ 150 (high)
- Hook rate < 15% com gasto ≥ R$ 80
- Frequência ≥ 4 e métrica-norte acima do target
- Conversão do anúncio entre os piores 20% da conta nos últimos 14 dias

Antes de pausar o **último criativo** de um conjunto, alertar o usuário e sugerir substituto via `/copy-anuncio` + `/criativo-estatico`.

### 7.2 Pausar **conjunto**
Qualquer:
- CPA/CPL na janela longa ≥ 1,7× target **e** janela média confirma
- Todos os anúncios do conjunto pausados ou em zona crítica
- Audiência saturada: frequência > 4 sem queda do CPA após refresh criativo
- Aprendizado limitado por > 7 dias seguidos sem entregar 50 conversões

### 7.3 Pausar **campanha inteira** (caso extremo)
- ≥ 70% dos conjuntos pausados ou inviáveis
- CPA/CPL ≥ 2× target em todas as 3 janelas
- Problema estrutural (página fora, oferta sem conversão, pixel quebrado)

**Nunca** pausar campanha inteira sem antes verificar: pixel funcionando, página online, checkout testado.

---

## 8. Lógica específica. Perpétuo

> **Premissa:** todas as campanhas de perpétuo são otimizadas pelo evento `Purchase`. Funil de 2 etapas (lead → venda) está fora do escopo desta skill na versão atual.

### 8.1 Low ticket (até R$ 500). Janelas 1d / 3d / 7d
- Decisões mais rápidas. Dado matura por volume.
- Watchlist após R$ 100 de gasto sem venda em um anúncio.
- Refresh criativo a cada 10 a 14 dias.

### 8.2 Mid ticket (R$ 501 a 1.499). Janelas 3d / 7d / 14d
- Tolerar mais tempo antes de pausar. Decisão de compra mais lenta.
- **Não decidir só com 1d.** Sempre confirmar com 3d.
- Watchlist após R$ 250 de gasto sem venda.
- Refresh criativo a cada 14 a 21 dias.

### 8.3 High ticket (R$ 1.500+). Janelas 7d / 14d / 30d
- Janela de 1d é praticamente ruído. Não dispara ações sozinha.
- Otimização sempre por `Purchase`. Se não consegue 50 conversões em 7 dias, a recomendação estrutural (orçamento maior, menos conjuntos) é assunto de `/trafego-criar-campanha`. Aqui apenas sinalizar.
- Watchlist após R$ 500 de gasto sem venda.
- Aceitar variações maiores de CPA na janela curta sem reagir.
- Refresh criativo a cada 21 a 30 dias.

---

## 9. Lógica específica. Lançamento

### 9.1 Métrica única
- `CPL` é a única métrica de decisão.
- CTR, hook rate e frequência são leading.
- Volume diário comparado contra meta total declarada (se houver).

### 9.2 Comportamento por fase

| Fase | Postura | Janela dominante |
|---|---|---|
| Aquecimento (D-15 a D-7) | Conservadora, validar criativos com orçamento baixo | 1d |
| Captação inicial (D-7 a D-3) | Sinalizar prontidão para escala dos vencedores | 1d e 3d |
| Captação final (D-3 a D-0) | Tolerar CPL até +30% acima do target em troca de volume | 1d |
| Carrinho aberto | Trocar para campanha de Vendas | 1d e 3d |

### 9.3 Regras específicas
- **Não reduzir orçamento** nos últimos 3 dias da captação enquanto CPL ≤ 2× target. Volume importa mais que custo.
- Pelo menos **3 ângulos criativos** ativos por conjunto durante a captação.
- Janela de 1d tem peso muito maior que no perpétuo.

---

## 10. Hierarquia de ação (ordem ao otimizar)

Investigar e agir **de baixo para cima**:
1. **Anúncio (criativo)**. Diagnóstico mais comum.
2. **Conjunto (segmentação/orçamento)**. Se múltiplos criativos do mesmo conjunto estão ruins.
3. **Campanha (estrutura/objetivo)**. Último recurso.

**Regra:** nunca mudar dois níveis ao mesmo tempo no mesmo dia.

---

## 11. Proteções contra reset de aprendizado

Disparam reset:
- Mudança de orçamento > 20%
- Troca de evento de otimização
- Mudança de segmentação (audiência, posicionamento, idiomas)
- Pausar e reativar conjunto após 7+ dias

Quando a ação proposta dispara reset, a skill:
1. Calcula custo aproximado de reaprendizado: 50 × CPA target (perpétuo) ou 50 × CPL target (lançamento).
2. Compara com ganho esperado.
3. Só executa se compensar. Caso contrário, sugere ação alternativa de menor impacto.

---

## 12. Sinal de prontidão para escala (handoff)

> Esta seção é o **bastão** que `/trafego-otimizar` passa para `/trafego-escalar`.

A skill emite `sinal_para_escala.pronta: true` **somente** quando **todas** as condições abaixo são simultaneamente verdadeiras:

```yaml
condicoes_de_handoff_para_escala:
  metrica_norte:
    janela_media_abaixo_target: true            # CPA/CPL ≤ target × 0.9
    janela_longa_abaixo_target: true            # CPA/CPL ≤ target
    tendencia: "estavel_performando"
  diagnostico_gargalo:
    classificacao: "nenhum"
  saude_estrutural:
    frequencia: "<=2.5"                          # perpétuo / <=3.0 lançamento
    fora_de_aprendizado: true
    pelo_menos_um_criativo_saudavel: true
  prerequisitos_operacionais:
    ultima_edicao_horas: ">=48"
    historico_minimo_da_trilha_cumprido: true
    sem_evento_sazonal_perturbador: true
  backup:
    criativos_saudaveis_no_conjunto: ">=2"       # >=3 para velocidade agressiva
  cooldown:
    horas_desde_ultimo_handoff_de_descida: ">=168"   # 7d perpétuo low/mid, lançamento 24h
                                                      # >=336 (14d) para perpetuo_high
```

Se **qualquer** condição reprovar, emitir `pronta: false` com lista de critérios falhos.

### 12.1 Recebimento de handoff de descida da escala
Quando `/trafego-escalar` devolve uma campanha (freio total), a otimização recebe um payload e marca a campanha com `vinda_da_escala: true`. Isso ajusta a postura para o próximo ciclo:
- Tolerância menor a problemas (pausar mais cedo).
- Foco em **recuperar margem de segurança** antes de re-emitir prontidão.
- Cooldown obrigatório antes de novo handoff de subida.

---

## 13. Output esperado

Output sempre estruturado em YAML, com cada ação mapeada para uma `tool_call` executável:

```yaml
campaign_id: <id>
trilha: perpetuo_low | perpetuo_mid | perpetuo_high | lancamento_low | lancamento_mid | lancamento_high
metrica_norte: cpa | cpl
escopo: campanha_unica | conta_completa
vinda_da_escala: true | false              # true = retornou recentemente da skill de escala

diagnostico_tendencia: estavel_performando | esfriando_ou_ruido | recuperando | saturacao | ruim_estrutural | entrega_limitada
diagnostico_gargalo: criativo | tecnico | pagina | checkout | leilao_audiencia | saturacao | nenhum
gargalo_dentro_do_meta: true | false | null

metricas_atuais:
  norte_curta: ...
  norte_media: ...
  norte_longa: ...
  norte_target: ...
  ctr: ...
  hook_rate: ...
  frequencia: ...
  cpm_vs_historico_pct: ...
  # derivadas
  connect_rate: ...
  taxa_conversao_pagina: ...
  taxa_conversao_anuncio: ...
  taxa_carrinho_compra: ...        # só perpétuo
  taxa_checkout_compra: ...        # só perpétuo

acoes_recomendadas:
  - nivel: ad | adset | campaign | alerta_usuario
    acao: reduzir_20 | pausar | refresh_criativo | manter | alertar | aguardar
    objeto_id: <id>
    tool_call:
      name: pause_ad | update_adset_budget | ...
      params: { ... }                         # parâmetros prontos
    justificativa: <texto curto referenciando o gargalo identificado>
    prioridade: alta | media | baixa
    aguardar_horas_apos: 0 | 24 | 48 | 72

# Bloco presente APENAS quando todas as condições da seção 12 são verdadeiras
sinal_para_escala:
  pronta: true | false
  motivo_se_nao_pronta: [ ... ]              # lista de condições reprovadas
  modo_recomendado: vertical | horizontal | vertical_e_horizontal | null
  velocidade_sugerida: conservadora | normal | agressiva | null
  janela_referencia: "3d" | "7d" | "14d" | "30d"
  cpa_ou_cpl_atual: ...
  target: ...
  margem_de_seguranca: 0.27                  # quanto a métrica-norte está abaixo do target
  riscos_observados: [ ... ]
  criativos_de_backup_disponiveis: 2

proximas_observacoes:
  - <coisa para reanalisar em X horas>
```

---

## 14. Princípios que a skill nunca viola

1. **Mudanças graduais sempre.** Orçamento move em ±20%, nunca mais.
2. **Aguardar maturação.** Mínimo 48h entre ajustes no mesmo objeto.
3. **Diagnóstico antes de ação.** Sempre rodar tendência + gargalo antes de propor.
4. **Verificar saúde técnica** antes de pausar campanha inteira.
5. **Preservar aprendizado.** Só aceitar reset quando ganho compensa.
6. **Métrica-norte é única por trilha.** CPA em perpétuo, CPL em lançamento. ROAS apenas como confirmação.
7. **Bottom-up sempre.** Criativo antes de conjunto, conjunto antes de campanha.
8. **Em lançamento na reta final, volume > custo** (até o limite de 2× CPL target).
9. **Apenas dados nativos do Gerenciador.** Se não vem do Gerenciador, não entra na decisão.
10. **Métricas derivadas sempre calculadas.** Connect rate, conversão da página/anúncio, taxas de checkout são obrigatórias no diagnóstico (lidas via `/trafego-insights`).
11. **Não pausar quando o gargalo está fora do Meta.** Alertar o usuário e (se necessário) reduzir –20% como contenção, mas manter estrutura viva.
12. **Não escalar nesta skill.** Quem sobe orçamento e duplica conjuntos é `/trafego-escalar`. Aqui só emitir sinal de prontidão.
13. **Respeitar cooldown.** Após handoff de descida da escala, aguardar 7d (perpétuo low/mid e lançamento) ou 14d (perpétuo high) antes de re-emitir prontidão.

---

## 15. Ações em lote por filtro

> Detalhes completos em `sub-skills/acoes-lote.md`.

Quando o aluno pede "pausa tudo com ROAS<1 nas últimas 2 semanas" ou "reduz 20% nos adsets com CPA > R$ 80", a skill aplica a ação em **múltiplas entidades** filtradas por critério.

Funções disponíveis:
- `pausar_em_lote(filtro)`. Pausa todas as entidades que batem o filtro.
- `reduzir_budget_em_lote(filtro, percent)`. Reduz budget % nas entidades que batem.
- `pausar_top_n_pior(metric, n)`. Pausa as N piores em uma métrica.

Critérios suportados: `roas`, `cpa`, `cpl`, `ctr`, `frequency`, `cpm`, `spend`, `impressions`, `purchases`, `leads`, `cpc`. Operadores: `less_than`, `greater_than`, `between`, `equal`. Períodos: `today`, `last_3d`, `last_7d`, `last_14d`, `last_30d`.

**Sempre exige preview** com lista de entidades afetadas + confirmação SIM antes de aplicar. Bloqueia automaticamente se mais de 50% dos adsets ativos da conta forem afetados (confirmação tripla).

---

## 16. Atalhos compostos

> Detalhes completos em `sub-skills/atalhos-compostos.md`.

Atalhos que orquestram múltiplas skills numa única operação:

- **Atalho A. Lookalike de compradores → campanha**. Orquestra `/trafego-publicos` (audience Purchase + LAL) + `/trafego-criar-campanha`.
- **Atalho B. Duplicar melhor anúncio em outro público**. Orquestra `/trafego-analise` [3] (identifica melhor) + `/trafego-publicos` (sugere alternativa) + `/trafego-testes` (duplicar-variando).
- **Atalho C. Faxina + lookalike**. Pausa queimadores (acoes-lote) + cria LAL de compradores.
- **Atalho D. Refresh criativo**. `/trafego-analise` [3] identifica ângulos da Mandala em uso + sugere ângulos novos + `/copy-anuncio` + `/trafego-testes`.

Toda execução de atalho composto:
1. Anuncia o plano completo antes.
2. Pede 1 confirmação SIM para todo o fluxo.
3. Executa em sequência, pausando se uma etapa falha.
4. Devolve resumo com IDs criados + comandos de reversão.
