---
name: workshop-marketing:ads-relatorio
description: Criar rotina diária automática que busca métricas do Facebook Ads e envia relatório pelo WhatsApp via Z-API. Configura as chaves de API via chat e cria um agente agendado no Claude que roda todo dia às 8h, sem precisar de Python instalado nem Task Scheduler.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
model: sonnet
---

# Relatorio Diario: Facebook Ads no WhatsApp

Cria uma rotina automatica no proprio Claude que toda manha (8h) busca as metricas do dia anterior no Facebook Ads e envia um resumo pelo WhatsApp via Z-API.

O mentoreado nunca abre arquivo, nunca instala nada. So cola as chaves no chat.

## COMO FUNCIONA

1. Claude coleta as chaves de API no chat e salva no `.env`
2. Claude cria um agente agendado na infraestrutura do proprio Claude (RemoteTrigger)
3. Todo dia as 8h03 esse agente acorda, busca os dados do Facebook Ads e envia no WhatsApp
4. Funciona sem o computador estar ligado. O agente roda na nuvem do Claude.

---

## PASSO 0. Verificar Chaves Existentes

Leia `.env`. Se existir, verifique se ja tem ao menos uma das variaveis de token (`FB_ACCESS_TOKEN_PERMANENTE` ou `FB_ACCESS_TOKEN_TEMPORARIO`) e tambem `FB_AD_ACCOUNT_ID`, `ZAPI_INSTANCE_ID`, `ZAPI_TOKEN`, `ZAPI_CLIENT_TOKEN`, `RELATORIO_WHATSAPP_NUMERO`.

Se todas existirem, pule para o Passo 2.

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

**Teste de conexao (curl puro, sem Python):**

```bash
ACCESS_TOKEN=$(grep -m1 FB_ACCESS_TOKEN .env | cut -d= -f2); AD_ID=$(grep -m1 FB_AD_ACCOUNT_ID .env | cut -d= -f2); curl -s "https://graph.facebook.com/v25.0/act_${AD_ID}?fields=name,account_status&access_token=${ACCESS_TOKEN}"
```

Se retornar `{"name":"...","id":"..."}`: confirmado, conta encontrada.
Se retornar `{"error":...}`: token invalido ou ID errado.

### 1.2 Z-API (WhatsApp)

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

### 1.3 Numero de destino (fixo)

```
Para qual numero do WhatsApp devo enviar o relatorio todo dia?

Digite no formato internacional sem + e sem espacos.
(ex: 5511999887766)

Esse numero ficara fixo. Para trocar depois, rode /ads-relatorio novamente.
```

Salve como `RELATORIO_WHATSAPP_NUMERO=valor` no `.env`.

---

## PASSO 2. Escolher Metricas

```
Quais metricas quer receber todo dia?

1. Basico: gasto, alcance e impressoes
2. Completo: gasto, alcance, impressoes, cliques, CTR, CPM, CPC
3. Completo + conversoes (compras ou leads e custo por resultado)
4. Tudo acima

Digite o numero:
```

Guarde a escolha na sessao como `metricas_escolhidas`.

---

## PASSO 3. Filtro de Campanhas

```
Quais campanhas incluir no relatorio?

1. Todas as campanhas ativas
2. Todas (ativas e pausadas)
3. Filtrar por nome (eu digo o termo)

Digite o numero:
```

Se opcao 3: pergunte o termo de filtro (ex: "baixo custo", "produto X"). Guarde como `filtro_campanha`.

---

## PASSO 4. Confirmacao

Mostre o resumo antes de criar qualquer coisa:

```
Resumo da configuracao:

- Conta Meta Ads: [nome retornado no teste]
- WhatsApp destino: [numero mascarado, ex: 5511****7766]
- Metricas: [descricao da escolha]
- Campanhas: [descricao do filtro]
- Horario: todo dia as 8h03

1. Tudo certo, criar a rotina
2. Quero ajustar algo
```

---

## PASSO 5. Escolher Onde Rodar

```
Como quer rodar o relatorio?

1. Tarefa local do Claude (mais simples)
   O proprio Claude agenda e executa o script todo dia as 8h03.
   Precisa do Claude Code aberto as 8h E na mesma sessao (tarefa some se fechar o Claude).
   Renovar a cada 7 dias rodando /ads-relatorio novamente.

2. Task Scheduler do Windows (mais robusto)
   Roda independente do Claude, mesmo com ele fechado.
   Precisa do computador ligado as 8h.
   Nao expira.

Digite o numero:
```

Se opcao 1: seguir o **Passo 5A**.
Se opcao 2: seguir o **Passo 5B**.

---

## PASSO 5A. Tarefa Local do Claude (CronCreate)

O Claude agenda um prompt diario que ele mesmo executa, rodando o script PowerShell via Bash. Nao depende do Task Scheduler do Windows.

### 5A.1 Obter o caminho absoluto do script

```bash
cygpath -w "$(pwd)/scripts/relatorio-ads.ps1"
```

Guarde o caminho retornado (ex: `C:\Users\...\scripts\relatorio-ads.ps1`).

### 5A.2 Criar a tarefa agendada

Use a ferramenta `CronCreate` com os seguintes parametros:

- `cron`: `3 8 * * *` (8h03 no horario local)
- `durable`: `true` (persiste em `.claude/scheduled_tasks.json`, sobrevive a reinicializacoes do Claude)
- `recurring`: `true`
- `prompt`: monte o texto abaixo substituindo `{CAMINHO_WINDOWS}` pelo caminho obtido no 5A.1:

```
Execute o relatorio diario de Meta Ads sem perguntar nada e sem pedir confirmacao.

Rode via Bash:
powershell.exe -ExecutionPolicy Bypass -File "{CAMINHO_WINDOWS}"

Depois leia as ultimas 10 linhas de scripts/relatorio-ads.log e mostre o resultado resumido.
```

Apos criar, guarde o job_id retornado no `.env` como `RELATORIO_CRON_ID`.

### 5A.3 Testar imediatamente

```bash
powershell.exe -ExecutionPolicy Bypass -File "scripts/relatorio-ads.ps1"
```

Leia o log:

```bash
tail -20 scripts/relatorio-ads.log
```

**Interpretando o resultado do log:**

- `=== Relatorio enviado com sucesso ===`: tudo certo, mensagem chegou no WhatsApp.
- `Sem dados para ontem.` seguido de envio com sucesso: Facebook conectou, mas nao havia campanhas ativas ontem. Normal.
- `ERRO ao buscar metricas`: token ou ID da conta invalido. Verificar os valores no `.env`.
- `ERRO ao enviar Z-API` com `"subscribe to this instance again"`: assinatura da instancia Z-API expirou. Acesse o painel da Z-API, localize a instancia e renove ou reative o plano. Depois rode o teste novamente.
- `ERRO ao enviar Z-API` com `"connected":false`: WhatsApp da instancia foi desconectado. Acesse o painel da Z-API e reconecte escaneando o QR Code.

Confirme com o usuario que a mensagem chegou no WhatsApp antes de encerrar.

**Aviso sobre expiracao:** a tarefa do CronCreate expira automaticamente em 7 dias. Para renovar, basta rodar `/ads-relatorio` novamente. O script e as credenciais continuam salvos.

---

## PASSO 5B. Task Scheduler do Windows (sem depender do Claude)

Use este passo se o usuario preferir que o relatorio rode mesmo com o Claude fechado.

### 5B.1 Registrar no Task Scheduler

Use PowerShell para registrar a tarefa (nao usar schtasks direto no bash, pois o Git Bash intercepta o comando):

```bash
WIN_PATH=$(cygpath -w "$(pwd)/scripts/relatorio-ads.ps1")
powershell.exe -Command "
\$action   = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument \"-ExecutionPolicy Bypass -WindowStyle Hidden -File '${WIN_PATH}'\"
\$trigger  = New-ScheduledTaskTrigger -Daily -At '08:03'
\$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1)
Register-ScheduledTask -TaskName 'Workshop Relatorio Ads' -Action \$action -Trigger \$trigger -Settings \$settings -Force
"
```

Se retornar uma linha com `State: Ready`: tarefa criada, continuar.

Se der erro de permissao:

```
O Windows pediu permissao de administrador para criar a tarefa automatica.

Duas opcoes:

1. Reabrir o Claude Code como Administrador (clique direito no icone > "Executar como administrador")
   e rodar /ads-relatorio novamente. A tarefa sera criada automaticamente.

2. Criar manualmente: Painel de Controle > Ferramentas Administrativas > Agendador de Tarefas >
   Criar Tarefa Basica. Nome: "Workshop Relatorio Ads".
   Programa: powershell.exe  Argumentos: -ExecutionPolicy Bypass -File "{caminho completo do relatorio-ads.ps1}"
   Frequencia: Diariamente as 08:03
```

### 5B.2 Testar imediatamente

```bash
powershell.exe -ExecutionPolicy Bypass -File "scripts/relatorio-ads.ps1"
```

Leia o log:

```bash
tail -20 scripts/relatorio-ads.log
```

Mesma tabela de interpretacao do log descrita no 5A.3.

Confirme com o usuario que a mensagem chegou no WhatsApp antes de encerrar.

---

## PASSO 6. Entrega

**Se escolheu Tarefa Claude (5A):**

```
Rotina criada.

Script: scripts/relatorio-ads.ps1
Tarefa Claude: agendada todo dia as 8h03 (CronCreate durable)
Log: scripts/relatorio-ads.log

Todo dia de manha vai chegar no WhatsApp [numero mascarado]:
- Gasto do dia anterior
- Alcance e impressoes
- Cliques, CTR, CPM, CPC
[- Conversoes, se incluiu]

Mantenha o Claude Code aberto as 8h para a tarefa disparar.
A tarefa expira em 7 dias. Para renovar: rode /ads-relatorio novamente.
Para rodar manualmente a qualquer hora: powershell.exe -ExecutionPolicy Bypass -File scripts/relatorio-ads.ps1
```

**Se escolheu Task Scheduler (5B):**

```
Rotina criada.

Script: scripts/relatorio-ads.ps1
Task Scheduler: "Workshop Relatorio Ads"
Horario: todo dia as 8h03
Log: scripts/relatorio-ads.log

Todo dia de manha vai chegar no WhatsApp [numero mascarado]:
- Gasto do dia anterior
- Alcance e impressoes
- Cliques, CTR, CPM, CPC
[- Conversoes, se incluiu]

O script roda independente do Claude. Mantenha o computador ligado as 8h.
Para rodar manualmente a qualquer hora: powershell.exe -ExecutionPolicy Bypass -File scripts/relatorio-ads.ps1
```

---

## CHECKPOINTS OBRIGATORIOS

| Etapa | Aprovacao? |
|---|---|
| Teste de conexao Facebook | Confirmado antes de continuar |
| Teste de conexao Z-API | Confirmado antes de continuar |
| Confirmacao geral (resumo) | Sim, obrigatoria |
| Escolha Claude vs Task Scheduler | Obrigatoria antes de criar |
| Teste imediato | Obrigatorio (confirmar mensagem no WhatsApp) |

---

## REGRAS

- Nunca sobrescrever chaves ja existentes no `.env` sem perguntar. Usar `Edit` cirurgico.
- Script local: credenciais embutidas diretamente no .ps1 para funcionar sem o Claude.
- Nao exibir o script PowerShell no chat. Salvar silenciosamente e informar apenas o caminho.
- RemoteTrigger: numero do WhatsApp fica fixo no prompt. Para trocar, recriar o trigger.
- Se a conta nao tiver dados no dia, o agente/script envia mensagem informando "sem dados".
