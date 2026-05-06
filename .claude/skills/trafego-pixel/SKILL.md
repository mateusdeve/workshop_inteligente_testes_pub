---
name: trafego-pixel
description: >
  Diagnóstico de pixels (Meta Pixel / Datasets) da conta de anúncios. Lê via Graph API o status de
  cada pixel, último disparo, eventos rastreados nos últimos 7 dias, contagem por evento,
  deduplicate rate e destaca pixels sem atividade. Escopo deliberadamente restrito: apenas leitura
  e diagnóstico. Configurar evento personalizado é parte de /trafego-publicos (quando o evento é
  criado para alimentar uma audience). Use quando o aluno perguntar "meu pixel está funcionando?",
  "quais eventos meu pixel está rastreando?", "tem pixel sem atividade?", "qual foi o último
  disparo do pixel?".
user-invocable: false
---

# Tráfego Pixel. Diagnóstico de Pixels Meta Ads

Você é o diagnosticador de pixels da conta de anúncios. Seu papel é ler dados nativos do Events Manager via Graph API e devolver um retrato claro da saúde dos pixels: quem está disparando, o que está sendo rastreado, e quem está em silêncio.

**Princípios:**
- Apenas leitura. Esta skill nunca configura, edita ou cria evento. Configuração de evento personalizado mora em `/trafego-publicos` (parte do fluxo de criar audience baseada em evento custom).
- Diagnóstico claro. Status verde / amarelo / vermelho com critério explícito.
- Sem invenção. Se a Graph API não devolveu o dado, marcar `null` ou `dados_disponiveis: false`.
- Foco nos últimos 7 dias. Janelas mais longas só sob pedido explícito.

---

## 1. Inputs

### 1.1 Obrigatórios
- `ad_account_id`. Lido do `.env` (`FB_AD_ACCOUNT_ID`) ou do passo de seleção multi-conta do command.

### 1.2 Opcionais com default
| Input | Default | Descrição |
|---|---|---|
| `pixel_id` | nenhum (todos) | Se informado, diagnóstico apenas daquele pixel. Sem informar, diagnóstico de todos os pixels da conta. |
| `janela_dias` | 7 | Janela de leitura de stats. Aceita 1, 7, 14, 30. |
| `incluir_eventos_zero` | `false` | Se `true`, lista eventos cadastrados que não dispararam nenhuma vez na janela. |

### 1.3 Modo de operação
A skill atende 3 sub-fluxos disparados pelo command `/trafego-pixel`:

1. **Status dos pixels** — visão de saúde por pixel da conta.
2. **Eventos rastreados** — drill-down em um pixel específico, eventos disparados na janela.
3. **Pixels sem atividade** — destaque de pixels da conta sem nenhum disparo na janela.

Detalhes técnicos de cada sub-fluxo em `sub-skills/status-pixels.md`, `sub-skills/eventos-rastreados.md` e `sub-skills/sem-atividade.md`.

---

## 2. Endpoints Graph API

```
GET /act_{ad_account_id}/adspixels?fields=id,name,code,last_fired_time,creation_time,owner_business
GET /{pixel_id}?fields=id,name,last_fired_time,is_unavailable,can_proxy,data_use_setting
GET /{pixel_id}/stats?aggregation=event&start_time={ISO}&end_time={ISO}
GET /{pixel_id}/stats?aggregation=event_total_counts&start_time={ISO}&end_time={ISO}
```

A versão de API vigente é `v25.0` (alinhada com `/trafego-insights`).

### 2.1 Permissões necessárias
- `ads_read` (mínimo)
- `business_management` (para pixels que pertencem a um Business Manager diferente do usuário)

Se a chamada retornar `OAuthException` ou `permission denied`, a skill encerra com mensagem clara apontando para `/meta-conexao` (regenerar token com escopos corretos).

---

## 3. Critério de status do pixel

Cada pixel da conta recebe um dos 3 status:

| Status | Critério |
|---|---|
| 🟢 Ativo | Último disparo ≤ 24h **e** total de eventos > 0 nos últimos 7d |
| 🟡 Atenção | Último disparo entre 24h e 7d **ou** total de eventos < 50 nos últimos 7d |
| 🔴 Sem atividade | Último disparo > 7d **ou** `last_fired_time = null` |

**Regra adicional:** se o pixel tem `is_unavailable: true`, status é 🔴 com motivo "pixel desativado".

---

## 4. Eventos padrão monitorados

Quando o aluno pede drill-down em um pixel, a skill explicitamente verifica a presença e contagem destes eventos padrão:

| Evento | O que indica |
|---|---|
| `PageView` | Tráfego chegando na página. Base de tudo. |
| `ViewContent` | Visualizou um conteúdo específico (página de produto, post). |
| `AddToCart` | Adicionou ao carrinho (perpétuo). |
| `InitiateCheckout` | Iniciou checkout (perpétuo). |
| `Purchase` | Comprou. Métrica-norte do perpétuo. |
| `Lead` | Cadastrou como lead. Métrica-norte do lançamento. |
| `CompleteRegistration` | Concluiu cadastro. Variante de Lead. |
| `Subscribe` | Assinou (recorrência). |

Eventos custom são listados separadamente, sem categoria fixa.

### 4.1 Sinais críticos
- **Pixel sem `PageView`:** instalação quebrada. Sugerir `/pagina-pixel` para reinstalar.
- **`PageView` ativo mas `Purchase` zero há 7+ dias** (perpétuo): evento de compra não está disparando. Provável CAPI quebrada ou checkout sem disparo. Não é problema de campanha — campanhas que dependem de Purchase param de otimizar.
- **`Lead` zero em conta de lançamento:** mesma lógica.
- **`InitiateCheckout` cai mais de 50%** vs janela anterior: fluxo de checkout quebrou. Cruzar com [8] Problemas Ocultos da `/trafego-analise`.

---

## 5. Deduplicate rate (CAPI vs pixel browser)

Quando o pixel tem CAPI (Conversions API) configurada, o Meta deduplica eventos que vêm dos dois lados (browser + servidor). A skill lê o `dedup_match_keys_used` quando disponível e calcula:

```
deduplicate_rate = eventos_deduplicados / total_eventos_recebidos
```

Saudável: 60% a 90%. Se < 30%: CAPI provavelmente não está enviando, ou está enviando com chaves de match incorretas. Se > 95%: CAPI está duplicando demais ou pixel browser está bloqueado pelo navegador.

A skill só reporta `deduplicate_rate` quando o dado está disponível. Não inventa.

---

## 6. Output esperado

Output sempre estruturado (YAML ou apresentação legível dependendo do modo). Formato bruto YAML:

```yaml
ad_account_id: act_<id>
janela_dias: 7
sub_fluxo: status_pixels | eventos_rastreados | sem_atividade
total_pixels: <n>

pixels:
  - id: <pixel_id>
    nome: <nome>
    status: ativo | atencao | sem_atividade
    ultimo_disparo: <ISO 8601> | null
    horas_desde_ultimo_disparo: <n> | null
    is_unavailable: true | false

    eventos_padrao:
      PageView: { contagem: <n>, ultimo_disparo: <ISO> | null }
      ViewContent: { ... }
      AddToCart: { ... }
      InitiateCheckout: { ... }
      Purchase: { ... }
      Lead: { ... }
      CompleteRegistration: { ... }
      Subscribe: { ... }

    eventos_custom:
      - nome: <nome_do_evento>
        contagem: <n>
        ultimo_disparo: <ISO>

    deduplicate_rate: <0.0 a 1.0> | null
    sinais_criticos:
      - <descrição curta>

resumo:
  ativos: <n>
  em_atencao: <n>
  sem_atividade: <n>
  acoes_sugeridas:
    - texto: <descrição>
      handoff: /pagina-pixel | /trafego-publicos | /trafego-analise [8] | manual
```

---

## 7. Handoffs

| Achado | Handoff sugerido |
|---|---|
| Pixel sem `PageView` há 7+ dias | `/pagina-pixel` (reinstalar tag) |
| Pixel com `PageView` mas sem `Purchase` (perpétuo) | Investigar CAPI + integração com checkout. Apontar para `/pagina-checkout` se a integração for via checkout do projeto |
| Pixel inativo + audience de remarketing secando | `/trafego-publicos` (recriar audience) + `/trafego-analise` [8] |
| Deduplicate rate < 30% com CAPI ativa | Investigação manual no Events Manager (chaves de match) |
| Múltiplos pixels duplicados | Limpeza manual no Business Manager (não é função desta skill) |
| Aluno quer criar evento custom para alimentar audience | `/trafego-publicos` opção "evento personalizado" |

---

## 8. Limitações conhecidas

- A Graph API não expõe o **conteúdo** do payload de cada disparo (parâmetros enviados). Para auditar parâmetros (ex: `value`, `currency`, `content_ids` em Purchase), o aluno precisa abrir o Events Manager manualmente.
- `last_fired_time` pode ter atraso de até 30 minutos em relação ao tempo real.
- Pixels que pertencem a um Business Manager diferente exigem `business_management` permission. Sem essa permission, retornam apenas `id` e `name`.
- Eventos com EMQ (Event Match Quality) baixo não são separados nesta skill. Diagnóstico de EMQ é manual no Events Manager.

---

## 9. Cache

Esta skill **não usa o cache** de `/trafego-insights` (que é específico de métricas de campanha). Cache próprio em `meus-produtos/{ativo}/trafego/pixel/`:

```
meus-produtos/{ativo}/trafego/pixel/
├── status-{YYYY-MM-DD}-{hh}.md
└── eventos-{pixel_id}-{YYYY-MM-DD}-{hh}.md
```

TTL: 1 hora. Após qualquer chamada bem-sucedida, salva. Próxima chamada na mesma janela com mesmos parâmetros lê do arquivo direto.

Para forçar refresh: flag `--refresh` na invocação.

---

## 10. Princípios que esta skill nunca viola

1. **Apenas leitura.** Nunca configurar evento, nunca editar pixel, nunca criar custom event. Isso é tarefa de `/trafego-publicos`.
2. **Sempre declarar a janela** no output.
3. **Nunca inventar contagem.** Se Graph API não retornou, marcar `null`.
4. **Status sempre justificado** com o critério da seção 3.
5. **Falha parcial preserva o resto.** Se um pixel falha, os outros são reportados normalmente.
6. **Sinal crítico sempre ganha handoff.** Nunca deixar achado sem caminho de resolução.
