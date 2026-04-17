---
name: workshop-marketing:configurar-zapi
description: Guia para criar conta na Z-API, configurar uma instância e conectar o WhatsApp para envio de mensagens automatizadas.
allowed-tools: Read, Write, Edit, Glob, Bash, WebFetch, WebSearch
model: sonnet
---

# Configurar Z-API

Guia para criar a conta, configurar a instancia e conectar o WhatsApp. So precisa fazer uma vez.

---

## Passo 1. Criar a conta

- Acesse app.z-api.io e crie sua conta

---

## Passo 2. Criar a instancia

- No menu lateral, clique em "Instancias Web"
- Clique em "Adicionar"
- Dê um nome para a instancia (ex: "Numero do Relatorio")
- Role até o final da tela e clique em "Salvar"

---

## Passo 3. Conectar o WhatsApp

- Na lista de instancias, clique na que acabou de criar
- Clique em "Assinar" para ativar a assinatura (obrigatorio para liberar o QR Code)
- Apos assinar, o QR Code aparece na mesma tela
- Abra o WhatsApp no celular e escaneie o QR Code (mesmo processo do WhatsApp Web)
- Aguarde a confirmacao de conexao

---

## Passo 4. Copiar as credenciais

**Instance ID e Token:**
- Na mesma tela da instancia (apos conectar), copie o Instance ID e o Token

**Client-Token (Security Token):**
- No menu lateral, clique em "Seguranca"
- Clique em "Gerar Token de seguranca da conta"
- Copie o token e guarde em um lugar seguro (ele nao aparece novamente, a menos que gere um novo)

---

## Passo 5. Testar a instancia

Use `Bash` para rodar o comando abaixo (substitua pelos valores reais):

```bash
curl -s "https://api.z-api.io/instances/INSTANCE_ID/token/TOKEN/status" -H "Client-Token: CLIENT_TOKEN"
```

Interpretacao das respostas:

- `{"connected":true}`: WhatsApp conectado, instancia pronta para uso
- `{"connected":false}`: instancia existe mas WhatsApp nao esta conectado. Volte ao Passo 3 e escaneie o QR Code
- `{"error":"To continue sending a message, you must subscribe to this instance again"}`: assinatura expirada ou nao ativada. Acesse app.z-api.io, abra a instancia e clique em "Assinar"
- `{"error":"...unauthorized..."}` ou status 401: credenciais invalidas. Verifique Instance ID, Token e Client-Token

---

## Apos configurar e testar

Retorne ao fluxo principal (`/ads-relatorio`) e cole as credenciais quando solicitado:

- Instance ID
- Token
- Client-Token
