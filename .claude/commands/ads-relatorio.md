---
name: workshop-marketing:ads-relatorio
description: Configura as credenciais e preferências do relatório de Facebook Ads (canal, métricas, filtro de campanhas) e oferece envio imediato via /enviar-relatorio-ads. Telegram ou WhatsApp.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
model: sonnet
---

# Configurar Relatorio de Ads

Configura o canal de envio, as credenciais e as preferencias do relatorio de Facebook Ads. Ao final, voce pode enviar um relatorio imediatamente.

O mentoreado nunca abre arquivo, nunca instala nada. So cola as chaves no chat.

## COMO FUNCIONA

1. Claude coleta as chaves de API no chat e salva no `.env`
2. Claude registra suas preferencias de metricas e filtro de campanhas
3. Ao final, voce pode enviar um relatorio imediatamente com `/enviar-relatorio-ads`

---

## PASSO 0. Verificar Canal de Envio

Leia `.env`. Se `RELATORIO_CANAL` ja existir com valor `TELEGRAM` ou `WHATSAPP`, pule para o **Passo 0.5**.

Se nao existir, exiba:

```
Por qual canal quer receber o relatorio?

1. Telegram (Recomendado)
2. WhatsApp

Digite o numero:
```

Se o usuario perguntar por que Telegram e recomendado, explique: "O Telegram e gratuito e nao tem risco de bloqueio. Automacoes de mensagem no WhatsApp podem levar ao banimento do numero."

**Se escolher Telegram (opcao 1):**
- Salve `RELATORIO_CANAL=TELEGRAM` no `.env` com `Edit`

**Se escolher WhatsApp (opcao 2):**
- Salve `RELATORIO_CANAL=WHATSAPP` no `.env` com `Edit`
- Exiba o aviso abaixo antes de continuar:

```
Aviso importante sobre WhatsApp:

Automacoes de mensagem tem risco de banimento do numero.
Use um numero secundario aquecido, nunca o numero principal da sua operacao.
```

---

## PASSO 0.5. Verificar Chaves Existentes

Leia `.env`. Verifique se ja tem:

- Pelo menos uma das variaveis de token Facebook (`FB_ACCESS_TOKEN_PERMANENTE` ou `FB_ACCESS_TOKEN_TEMPORARIO`)
- `FB_AD_ACCOUNT_ID`
- Se `RELATORIO_CANAL=TELEGRAM`: `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID`
- Se `RELATORIO_CANAL=WHATSAPP`: `ZAPI_INSTANCE_ID`, `ZAPI_TOKEN`, `ZAPI_CLIENT_TOKEN`, `RELATORIO_WHATSAPP_NUMERO`

Se todas existirem, pule para o **Passo 2**.

---

## PASSO 1. Coletar Chaves de API (UMA por vez, no chat)

### 1.1 Facebook Ads

```
Para buscar os dados do Facebook Ads, precisamos de 2 informacoes:

1. Token de acesso (Access Token)
2. ID da conta de anuncios

Voce tem esses dados?

1. Sim, tenho os dois
2. Nao sei onde pegar
```

**Se nao souber onde pegar, guie:**

Pergunte primeiro:

```
Voce ja tem um App criado no Facebook Developers (developers.facebook.com)?

1. Sim, ja tenho
2. Nao tenho ainda
```

**Se nao tiver App (opcao 2): execute a skill `criar-aplicativo-analise-ads`**

Ela guia o usuario pelas 5 etapas de criacao do App e geracao do token. Apos concluir, retorne aqui para salvar o token e o ID da conta.

Pergunte um por vez:

```
Cole seu Facebook Access Token:
```

Use `Edit` para salvar `FB_ACCESS_TOKEN_TEMPORARIO=valor` no `.env`. Depois:

```
Cole o ID da sua conta de anuncios (so os numeros):
```

Salve `FB_AD_ACCOUNT_ID=valor` no `.env`.

**Teste de conexao:**

```bash
powershell.exe -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \$t = (Get-Content .env | Select-String 'FB_ACCESS_TOKEN_PERMANENTE|FB_ACCESS_TOKEN_TEMPORARIO' | Select-Object -First 1) -replace '^[^=]+=',''; \$id = (Get-Content .env | Select-String 'FB_AD_ACCOUNT_ID' | Select-Object -First 1) -replace '^[^=]+=',''; Invoke-RestMethod \"https://graph.facebook.com/v25.0/act_\${id}?fields=name,account_status&access_token=\${t}\" | ConvertTo-Json"
```

Se retornar `{"name":"...","id":"..."}`: confirmado, conta encontrada.
Se retornar `{"error":...}`: token invalido ou ID errado.

### 1.2 Credenciais do Canal de Envio

**Se `RELATORIO_CANAL=TELEGRAM`:**

Verifique se `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` existem no `.env`.

Se existirem, faca o teste de conexao:

```bash
powershell.exe -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \$bot = (Get-Content .env | Select-String 'TELEGRAM_BOT_TOKEN' | Select-Object -First 1) -replace '^[^=]+=',''; \$chat = (Get-Content .env | Select-String 'TELEGRAM_CHAT_ID' | Select-Object -First 1) -replace '^[^=]+=',''; Invoke-RestMethod -Uri \"https://api.telegram.org/bot\${bot}/sendMessage\" -Method POST -ContentType 'application/json' -Body \"{`\"chat_id`\":`\"\${chat}`\",`\"text`\":`\"Conexao confirmada. Workshop Marketing IA.`\"}\" | ConvertTo-Json"
```

Se retornar `"ok":true`: Telegram conectado.
Se retornar erro: credenciais invalidas. Execute a skill `configurar-telegram`.

Se nao existirem: **execute a skill `configurar-telegram`**

Ela guia a criacao do bot, obtencao do Chat ID e teste. Apos concluir, retorne aqui.

---

**Se `RELATORIO_CANAL=WHATSAPP`:**

```
Agora as credenciais do Z-API para enviar no WhatsApp.

Voce tem conta na Z-API com instancia e WhatsApp conectado?

1. Sim, ja tenho
2. Nao tenho ainda
```

**Se nao tiver (opcao 2): execute a skill `configurar-zapi`**

Ela guia pelo processo completo: criar conta, criar instancia, conectar o WhatsApp e copiar as credenciais. Apos concluir, retorne aqui para salvar as credenciais.

Pergunte um por vez:

```
Cole o Instance ID da Z-API:
```

```
Cole o Token da Z-API:
```

```
Cole o Client-Token (Security Token):
```

Salve os tres no `.env`.

**Teste de conexao Z-API:**

```bash
INSTANCE=$(grep -m1 ZAPI_INSTANCE_ID .env | cut -d= -f2); TOKEN=$(grep -m1 ZAPI_TOKEN .env | cut -d= -f2); CLIENT=$(grep -m1 ZAPI_CLIENT_TOKEN .env | cut -d= -f2); curl -s "https://api.z-api.io/instances/${INSTANCE}/token/${TOKEN}/status" -H "Client-Token: ${CLIENT}"
```

Se retornar `"connected":true`: WhatsApp conectado.
Se retornar erro ou `"connected":false`: instancia nao encontrada ou QR Code nao escaneado.

### 1.3 Numero de destino (somente para WhatsApp)

Esta etapa so se aplica se `RELATORIO_CANAL=WHATSAPP`.

```
Para qual numero do WhatsApp devo enviar o relatorio?

Digite no formato internacional sem + e sem espacos.
(ex: 5511999887766)

Lembre: use um numero secundario aquecido, nao o numero principal da operacao.
```

Salve como `RELATORIO_WHATSAPP_NUMERO=valor` no `.env`.

---

## PASSO 2. Escolher Metricas

```
Quais metricas quer ver no relatorio?

1. Basico: gasto, alcance e impressoes
2. Completo: gasto, alcance, impressoes, cliques, CTR, CPM, CPC
3. Completo + conversoes (compras ou leads e custo por resultado)
4. Tudo acima

Digite o numero:
```

Salve a escolha no `.env` como `RELATORIO_METRICAS=1` (ou 2, 3, 4).

---

## PASSO 3. Filtro de Campanhas

```
Quais campanhas incluir no relatorio?

1. Todas as campanhas ativas
2. Todas (ativas e pausadas)
3. Filtrar por nome (eu digo o termo)

Digite o numero:
```

Se opcao 3: pergunte o termo de filtro (ex: "baixo custo", "produto X"). Salve como `RELATORIO_FILTRO_CAMPANHA=valor` no `.env`. Para opcoes 1 e 2, salve `RELATORIO_FILTRO_CAMPANHA=ativas` ou `RELATORIO_FILTRO_CAMPANHA=todas`.

---

## PASSO 4. Confirmacao

Mostre o resumo da configuracao salva:

**Se Telegram:**
```
Configuracao salva.

- Conta Meta Ads: [nome retornado no teste]
- Canal: Telegram (@username_do_bot)
- Metricas: [descricao da escolha]
- Campanhas: [descricao do filtro]

1. Tudo certo
2. Quero ajustar algo
```

**Se WhatsApp:**
```
Configuracao salva.

- Conta Meta Ads: [nome retornado no teste]
- Canal: WhatsApp [numero mascarado, ex: 5511****7766]
- Metricas: [descricao da escolha]
- Campanhas: [descricao do filtro]

1. Tudo certo
2. Quero ajustar algo
```

---

## PASSO 5. Oferecer Envio Imediato

Apos a confirmacao, pergunte:

```
Quer enviar um relatorio agora?

1. Sim, enviar relatorio de ontem
2. Nao, so queria configurar
```

Se opcao 1: execute a skill `enviar-relatorio-ads`. Ela cuida do periodo, busca os dados e envia no canal configurado.

Se opcao 2: encerre com a mensagem abaixo.

---

## PASSO 6. Entrega

```
Configuracao concluida.

Canal: [Telegram ou WhatsApp]
Metricas: [descricao]
Campanhas: [descricao]

Para enviar um relatorio a qualquer momento: /enviar-relatorio-ads
```

---

## CHECKPOINTS OBRIGATORIOS

| Etapa | Aprovacao? |
|---|---|
| Teste de conexao Facebook | Confirmado antes de continuar |
| Teste de conexao Telegram ou Z-API | Confirmado antes de continuar |
| Confirmacao geral (resumo) | Sim, obrigatoria |

---

## REGRAS

- Nunca sobrescrever chaves ja existentes no `.env` sem perguntar. Usar `Edit` cirurgico.
- Nao exibir scripts ou arquivos de configuracao no chat. Salvar silenciosamente e informar apenas o caminho.
- Se a conta nao tiver dados no periodo, o relatorio informa "sem dados" e envia assim mesmo.
- Se o usuario ja tem `RELATORIO_CANAL` salvo e quiser trocar de canal: salvar novo valor e refazer o passo de credenciais do novo canal.
