---
name: trafego-analise
description: >
  Análise narrada de tráfego pago Meta Ads com terminologia VTSD (Mandala de 18 tipos, Urgência
  Oculta, Quadro na Parede, Furadeira, Decorados, 3 Identidades, HOT/COLD/SUPERCOLD, Caixa Rápido,
  Pico vs Evergreen). Hub de menu com 9 outputs narrativos: Diagnóstico Rápido, Performance & Funil,
  Criativos & Copy, Geo & Demografia, Timing & Sazonalidade, Investigação Profunda, Lifecycle &
  Histórico, Problemas Ocultos, Orçamento & Projeção. Aluno escolhe um output por vez, recebe
  análise completa pelo método VTSD com handoff para skill executora quando ação for necessária.
  Lê dados via /trafego-insights (com cache local em arquivo .md). Use quando o aluno pedir
  análise narrada, ranking, comparativo, diagnóstico, mapa do funil, ou quiser ensinar tráfego
  pelo método.
---

# Tráfego Análise. 9 Outputs Narrativos VTSD

Análise narrada de campanhas Meta Ads pela lente da metodologia VTSD (Venda Todo Santo Dia, Leandro Ladeira). Cada métrica de tráfego é o termômetro de um elemento do método. O propósito é conectar dado → método → decisão, e entregar análise pedagógica que serve tanto para operar quanto para ensinar.

**Diferença vs outras skills de tráfego:**
- `/trafego-insights` é a **fonte de dados** (lê e cacheia, não narra).
- `/trafego-otimizar` é **técnico**, calcula, executa pausa/ajuste de budget. Foca em **operação**.
- `/trafego-escalar` **escala** campanhas validadas com freios.
- `/trafego-regras`, `/trafego-publicos`, `/trafego-pixel`, `/trafego-testes` **executam** ações específicas.
- `/trafego-analise` **narra** com terminologia VTSD. **Não executa edição.** Quando a análise sugere ação, ela faz handoff para a skill executora correspondente.

---

## Como funcionar

Ao ser invocada, validar conexão Meta e apresentar o menu. Aguardar escolha antes de pedir período ou dado.

### Passo 0. Validar conexão Meta
Ler `META_AUTH_MODO` no `.env`. Se vazio, acionar `/meta-conexao` antes de qualquer outra ação.

### Passo 1. Mostrar menu
```
╔══════════════════════════════════════════════════════════════╗
║  TRÁFEGO ANÁLISE. Análise VTSD de Meta Ads                   ║
╚══════════════════════════════════════════════════════════════╝

Que tipo de análise você quer hoje?

[1]  DIAGNÓSTICO RÁPIDO         visão geral em 60 segundos
                                queima de dinheiro, fadiga, gasto vs anterior

[2]  PERFORMANCE & FUNIL        ranking ROAS, comparativo CPM,
                                posicionamento (Feed/Stories/Reels), funil completo

[3]  CRIATIVOS & COPY           formato (estático/vídeo/carrossel),
                                tier S/A/B/C/D, fadiga, Mandala VTSD 18 tipos

[4]  GEO & DEMOGRAFIA           estado, cidade, idade, gênero,
                                capital vs interior, público mais barato

[5]  TIMING & SAZONALIDADE      mês a mês, dia da semana, horário,
                                datas comemorativas, fim de semana

[6]  INVESTIGAÇÃO PROFUNDA      primeiras 24h vs depois do aprendizado,
                                dispositivo, tempo de vídeo, taxa de rejeição

[7]  LIFECYCLE & HISTÓRICO      campanhas com mais de 60 dias, evolução do CPA,
                                melhor mês de todos, candidatos a reativar

[8]  PROBLEMAS OCULTOS          ad sets quebrados, audiências micro,
                                anúncios desaprovados, pixel sem atividade

[9]  ORÇAMENTO & PROJEÇÃO       projeção até o fim do mês, candidatos a
                                escala, redistribuição de budget

[10] descrever em texto livre o que precisa
```

### Passo 2. Aluno escolhe UM output
Aguardar escolha. Aceitar número (1 a 10) ou descrição livre. Se descrição livre, identificar qual output melhor cobre.

### Passo 3. Pergunta período
```
Qual período da análise?

[1] últimos 7 dias
[2] últimos 14 dias
[3] últimos 30 dias
[4] customizado (você informa data início e fim)
```

### Passo 4. Chama /trafego-insights
Pedir métricas com os breakdowns que aquele output exige (ver tabela em "Roteamento por output" abaixo). A skill `/trafego-insights` consulta primeiro o cache em arquivo .md, depois cache de memória, depois Graph API. Resultado é salvo no cache local.

### Passo 5. Lê o sub-skill correspondente
Ler `sub-skills/{N}-{nome}.md` e executar o protocolo daquele output específico.

### Passo 6. Entrega análise narrada
Aplicar protocolo padrão (Diagnóstico → Causa provável → No VTSD isso significa → Ação recomendada). Se ação exige execução, apontar para a skill executora certa.

### Passo 6.5. Oferece export em HTML (opcional)
Após entregar a análise narrada, perguntar:
```
Quer salvar essa análise como HTML pra revisitar depois? (s/n)

⚠️ Snapshot: o HTML é uma fotografia dos dados deste momento.
   Métricas mudam, e o arquivo NÃO atualiza sozinho. Para dado fresco,
   rode a análise de novo.
```

Se o aluno responder `s`/`sim`: acionar `sub-skills/_export-html.md`, que gera o arquivo em `meus-produtos/{ativo}/trafego/analise/{slug-output}-{YYYY-MM-DD-HHMM}.html` usando o design system Fluxo Criativo. Devolver o caminho absoluto.

Se responder `n`/`não` ou silêncio: seguir direto para o Passo 7.

### Passo 7. Pergunta se quer outro output
```
Quer rodar outro output? Digite o número (1 a 10) ou "não".
```

---

## Roteamento por output

Cada escolha do menu carrega um sub-skill específico. Dependências de breakdowns também declaradas:

| Escolha | Sub-skill | Breakdowns que pede ao /trafego-insights |
|---|---|---|
| [1] Diagnóstico Rápido | `sub-skills/1-diagnostico-rapido.md` | base (sem breakdown) |
| [2] Performance & Funil | `sub-skills/2-performance-funil.md` | base + `publisher_platform`, `platform_position` |
| [3] Criativos & Copy | `sub-skills/3-criativos.md` | base + `publisher_platform` |
| [4] Geo & Demografia | `sub-skills/4-geo-demografia.md` | `age,gender`, `country`, `region`, `dma` |
| [5] Timing & Sazonalidade | `sub-skills/5-timing-sazonalidade.md` | `hourly_stats_aggregated_by_advertiser_time_zone` + base por dia |
| [6] Investigação Profunda | `sub-skills/6-investigacao-profunda.md` | `device_platform`, `impression_device`, `publisher_platform` |
| [7] Lifecycle & Histórico | `sub-skills/7-lifecycle-historico.md` | base por mês x 6 meses (`historico_mensal`) |
| [8] Problemas Ocultos | `sub-skills/8-problemas-ocultos.md` | base + diagnóstico de pixel via `/trafego-pixel` |
| [9] Orçamento & Projeção | `sub-skills/9-orcamento-projecao.md` | base |
| [10] Livre | usa o sub-skill mais próximo da intenção identificada | conforme necessidade |

**Sub-skill compartilhada (Passo 6.5):** `sub-skills/_export-html.md` — gera HTML standalone do output usando o design system Fluxo Criativo, salvando em `meus-produtos/{ativo}/trafego/analise/`. Acionada apenas quando o aluno confirma o export.

**Total:** 9 outputs narrativos + 1 sub-skill utilitária de export. Cada output entrega análise completa em uma sessão. Aluno pode rodar quantos quiser em sequência.

---

## Protocolo padrão de cada output

Todo sub-skill entrega obrigatoriamente:

1. **Diagnóstico** — o que os dados revelam objetivamente.
2. **Causa provável** — por que está acontecendo (hipótese baseada em padrões VTSD).
3. **No VTSD, isso significa…** — interpretação dentro do método (qual elemento da metodologia está em jogo).
4. **Ação recomendada** — próximo passo concreto. Se exigir execução, apontar para skill executora:
   - Pausa/ajuste de campanha → `/trafego-otimizar`
   - Escala de winner → `/trafego-escalar`
   - Criar regra automática ou alerta → `/trafego-regras`
   - Criar audience custom/lookalike → `/trafego-publicos`
   - Diagnóstico aprofundado de pixel → `/trafego-pixel`
   - Montar teste A/B → `/trafego-testes`

---

## Fonte de Dados

**Opção A. Via `/trafego-insights` (recomendado):**
- Invocar `/trafego-insights` com escopo, período e breakdowns que o output exige.
- A skill consulta cache local em `meus-produtos/{ativo}/trafego/insights/` antes da API.
- Resultado é salvo no cache para próximas chamadas (mesma ou outras skills).

**Opção B. Entrada manual:**
- Solicitar CSV exportado do Gerenciador de Anúncios ou dados colados diretamente.
- Confirmar período: últimos 7, 14 ou 30 dias.

Ao iniciar qualquer output: confirmar a fonte se houver ambiguidade.

---

## Módulo de referência rápida. Health Score (usado no output [1])

Componente do output [1] Diagnóstico Rápido. Detalhes completos no `sub-skills/1-diagnostico-rapido.md`.

### Cálculo do Score (0 a 100)

| Dimensão | Peso | Como medir |
|----------|------|------------|
| Diversidade criativa (cobertura da Mandala VTSD) | 20% | Tipos ativos / 18 tipos totais |
| Saúde de públicos (frequência, temperatura) | 20% | HOT/COLD/SUPERCOLD equilibrados, frequência < 4 |
| Eficiência de funil (etapas acima do threshold) | 25% | Nº de etapas saudáveis / 7 etapas totais |
| Performance financeira (ROAS, CPL vs benchmark) | 25% | Métricas dentro do range ideal |
| Consistência temporal (variação de CPL) | 10% | Desvio < 30% semana a semana |

### Classificação do Score

| Score | Classificação | O que significa |
|-------|--------------|-----------------|
| 85 a 100 | 🟢 Excelente | Conta saudável, foco em escala |
| 70 a 84 | 🟡 Boa | Funcionando bem, otimizações pontuais |
| 50 a 69 | 🟠 Regular | Problemas específicos a resolver antes de escalar |
| 0 a 49 | 🔴 Crítica | Parar escalada, diagnóstico profundo urgente |

---

## O método VTSD aplicado ao tráfego

Cada métrica de tráfego é **o termômetro de um elemento do método**:

| Elemento VTSD | Onde aparece no tráfego |
|---|---|
| **Urgência Oculta** | Hook Rate. Se a dor é ativada, o Hook sobe |
| **Identidade do Produto** | CTR. Se o produto está claro, o CTR responde |
| **Identidade do Consumidor** | CPL por público. Público certo, CPL baixa |
| **Decorados** | Hold Rate. Benefícios percebidos = retenção |
| **Furadeira** | Play-Through Rate. Método claro = assiste até o fim |
| **Oferta** | Offer Rate. Oferta clara = checkout acontece |
| **Quadro na Parede** | Connect Rate. Resultado desejado = venda fecha |
| **Orderbump + Upsell** | LTV Rate. VTSD completo = ticket médio sobe |

Leitura fundamental:
> "Cada métrica que cai indica um elemento do método que está falhando."

---

## Glossário VTSD essencial

| Termo VTSD | Significado no tráfego |
|------------|----------------------|
| **Urgência Oculta** | Dor que o público sente mas não verbaliza. Deve aparecer no hook do criativo |
| **Quadro na Parede** | Resultado final que o produto entrega. Deve estar claro na promessa do anúncio |
| **Furadeira** | Método do produto. Deve ser comunicado na página e nos criativos de meio/fundo |
| **Decorados** | Benefícios percebidos. Aumentam Hold Rate e reduzem abandono de checkout |
| **Identidade do Consumidor** | Público ideal. Define segmentação, temperatura e linguagem dos anúncios |
| **Identidade do Comunicador** | Tom, valores e estilo do criador. Define como a mensagem é dita nos anúncios |
| **Identidade do Produto** | Posicionamento. Define diferencial competitivo e angle dos criativos |
| **Pico de Vendas** | Período de lançamento. Maior concentração de budget em HOT e COLD |
| **Evergreen / Perpétuo** | Funil sempre ativo. Foco em eficiência e CPL/CPA estável |
| **Caixa Rápido** | Produto low ticket de conversão rápida. ROAS mínimo 3x |
| **HOT** | Público quente (engajamento, video views, lista de leads) |
| **COLD** | Público frio (interesses, lookalike) |
| **SUPERCOLD** | Público aberto (sem segmentação específica) |
| **Mandala** | Sistema de 18 tipos de anúncio. Garante diversidade criativa |

---

## Regras Absolutas

- NUNCA inventar métricas. Se o dado não estiver disponível, informar e pedir.
- SEMPRE usar terminologia VTSD nas análises.
- NUNCA deixar uma análise sem ação recomendada concreta.
- SEMPRE identificar o gargalo principal antes de listar secundários.
- NUNCA usar jargão técnico sem explicar em linguagem do método.
- Para ações de execução (pausar, mudar budget, criar regra, criar audience, criar teste), encaminhar para a skill executora correta. Esta skill **narra**, não executa edição.
- Sempre que possível, aproveitar o cache local em `meus-produtos/{ativo}/trafego/insights/` para evitar requisições redundantes à Graph API.
- Um output por vez. Não tentar entregar 3 outputs em uma resposta.
- **Export HTML é opcional e SEMPRE precedido por confirmação explícita do aluno.** Nunca gerar HTML automaticamente. Quando gerado, o arquivo SEMPRE traz banner de "snapshot" no topo com timestamp visível, deixando claro que não é dado live.
- HTML de export sempre vai para `meus-produtos/{ativo}/trafego/analise/`. Nunca em pasta global, nunca na raiz, nunca sobrescrever (cada export é arquivo novo com timestamp próprio).
