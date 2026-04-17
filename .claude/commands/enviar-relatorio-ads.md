---
name: workshop-marketing:enviar-relatorio-ads
description: Busca as métricas do dia anterior no Facebook Ads e envia o relatório pelo WhatsApp via Z-API. Roda direto no CLI, sem agendamento.
allowed-tools: Read, Bash, WebFetch
model: sonnet
---

# Enviar Relatorio de Ads no WhatsApp

Executa imediatamente: busca as metricas do Facebook Ads do periodo escolhido e envia no WhatsApp via Z-API. Sem agendamento.

## PASSO 1. Verificar credenciais

Leia `.env` e verifique se existem:
- Pelo menos uma das variaveis de token do Facebook: `FB_ACCESS_TOKEN_PERMANENTE` ou `FB_ACCESS_TOKEN`
- `FB_AD_ACCOUNT_ID`
- `ZAPI_INSTANCE_ID`
- `ZAPI_TOKEN`
- `ZAPI_CLIENT_TOKEN`
- `RELATORIO_WHATSAPP_NUMERO`

**Se faltar token do Facebook ou `FB_AD_ACCOUNT_ID`:**

Pergunte primeiro:

```
Voce ja tem um App criado no Facebook Developers (developers.facebook.com)?

1. Sim, ja tenho — quero gerar o token
2. Nao tenho ainda — preciso criar o App
```

- Se opcao 1: execute a skill `gerar-token-permanente-facebook-ads`
- Se opcao 2: execute a skill `criar-aplicativo-analise-ads`, depois retorne e execute `gerar-token-permanente-facebook-ads`

Apos concluir, retorne ao Passo 1 para verificar novamente.

**Se faltar qualquer credencial da Z-API (`ZAPI_INSTANCE_ID`, `ZAPI_TOKEN`, `ZAPI_CLIENT_TOKEN`):**

```
Voce ja tem conta na Z-API com instancia e WhatsApp conectado?

1. Sim, ja tenho — quero inserir as credenciais
2. Nao tenho ainda
```

- Se opcao 1: peca as 3 credenciais uma por vez e salve no `.env` com `Edit`
- Se opcao 2: execute a skill `configurar-zapi`, depois retorne

**Se faltar `RELATORIO_WHATSAPP_NUMERO`:**

```
Para qual numero do WhatsApp devo enviar o relatorio?

Digite no formato internacional sem + e sem espacos.
(ex: 5511999887766)
```

Salve como `RELATORIO_WHATSAPP_NUMERO=valor` no `.env`.

**Quando todas as credenciais estiverem presentes:** avance para o Passo 2.

## PASSO 2. Perguntar o periodo

Pergunte ao usuario:

```
Qual periodo voce quer no relatorio?

1. Ontem
2. Ultimos 7 dias
3. Ultimos 30 dias
4. Periodo personalizado (informar data inicial e final)

Digite o numero:
```

- Opcao 1: calcule `INICIO_ISO` e `FIM_ISO` como ontem (`date -d "yesterday" +%Y-%m-%d 2>/dev/null || date -v-1d +%Y-%m-%d`). Label do periodo: `{ONTEM_BR}`.
- Opcao 2: `INICIO_ISO` = hoje menos 7 dias, `FIM_ISO` = ontem. Label: `Ultimos 7 dias`.
- Opcao 3: `INICIO_ISO` = hoje menos 30 dias, `FIM_ISO` = ontem. Label: `Ultimos 30 dias`.
- Opcao 4: peca a data inicial (formato DD/MM/AAAA) e a data final (formato DD/MM/AAAA), converta para ISO (AAAA-MM-DD). Label: `{INICIO_BR} a {FIM_BR}`.

Para calcular as datas use Bash:
```bash
# Ontem
date -d "yesterday" +%Y-%m-%d 2>/dev/null || date -v-1d +%Y-%m-%d
# 7 dias atras
date -d "7 days ago" +%Y-%m-%d 2>/dev/null || date -v-7d +%Y-%m-%d
# 30 dias atras
date -d "30 days ago" +%Y-%m-%d 2>/dev/null || date -v-30d +%Y-%m-%d
```

Guarde `INICIO_ISO`, `FIM_ISO` e `LABEL_PERIODO`.

## PASSO 3. Buscar metricas no Facebook Ads

Use WebFetch na URL abaixo, substituindo os valores reais:

```
https://graph.facebook.com/v25.0/act_{FB_AD_ACCOUNT_ID}/insights?access_token={FB_ACCESS_TOKEN}&time_range%5Bsince%5D={INICIO_ISO}&time_range%5Buntil%5D={FIM_ISO}&fields=spend,impressions,reach,clicks,ctr,cpm,cpc,actions,cost_per_action_type&level=account
```

Prompt para o WebFetch: "Retorne o JSON completo exatamente como recebido."

## PASSO 4. Montar a mensagem

Se `data` vier vazio (`[]`):

```
*Relatorio Meta Ads - {LABEL_PERIODO}*

Sem dados para o periodo. Verifique se ha campanhas ativas.
```

Se `data` tiver conteudo, monte:

```
*Relatorio Meta Ads - {LABEL_PERIODO}*

*Investimento e Alcance*
Gasto: R$ X,XX
Alcance: X.XXX
Impressoes: X.XXX

*Engajamento*
Cliques: X.XXX
CTR: X,XX%
CPM: R$ X,XX
CPC: R$ X,XX
```

Se houver `actions` com `action_type` igual a `purchase` ou `lead`, adicione:

```
*Conversoes*
Resultados: X
Custo por resultado: R$ X,XX
```

Formatacao numerica: valores monetarios com virgula decimal e ponto milhar (ex: `R$ 1.234,56`). Percentuais com virgula (ex: `3,42%`).

## PASSO 5. Confirmar envio

Mostre a mensagem montada ao usuario e pergunte:

```
Relatorio pronto. Deseja enviar para o WhatsApp {NUMERO_MASCARADO}?

1. Sim, enviar agora
2. Nao, apenas exibir aqui
```

Se opcao 2: encerre sem chamar a Z-API.

## PASSO 6. Enviar via Z-API

Use Bash com curl:

```bash
curl -s -X POST \
  "https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text" \
  -H "Content-Type: application/json" \
  -H "Client-Token: {ZAPI_CLIENT_TOKEN}" \
  -d "{\"phone\":\"{RELATORIO_WHATSAPP_NUMERO}\",\"message\":\"{MENSAGEM_ESCAPADA}\"}"
```

A mensagem deve ter as quebras de linha substituidas por `\n` para caber no JSON.

## PASSO 7. Resultado

Se a Z-API retornar sucesso: informe "Relatorio enviado para {numero mascarado}."

Se retornar erro, mostre a mensagem de erro e oriente:
- `"subscribe to this instance again"`: assinatura Z-API expirada. Acesse o painel da Z-API e renove o plano.
- `"connected":false`: WhatsApp desconectado. Acesse o painel da Z-API e reconecte escaneando o QR Code.
- Qualquer outro erro: mostre o retorno bruto para diagnostico.
