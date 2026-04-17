---
name: workshop-marketing:configurar-heygen
description: Guia para conectar uma conta do HeyGen ao projeto (videos com avatar IA). Salva a API key no .env como HEYGEN_API_KEY para ser usada pela skill /video-heygen.
---

# Como Configurar o HeyGen para Criar Videos com Avatar IA

Guia completo para conectar sua conta do HeyGen ao Workshop Marketing IA.
Tempo estimado: 5 minutos.

---

## O que e o HeyGen?

O HeyGen e uma plataforma que cria videos com avatares de inteligencia artificial.
Voce escolhe (ou cria) um avatar, seleciona uma voz, escreve o roteiro e ele
gera um video com o avatar "falando" o texto. Parece uma pessoa real gravando.

Isso serve para:
- Criar anuncios em video sem precisar gravar nada
- Testar diferentes "porta-vozes" para seu produto
- Escalar a producao de conteudo (varios videos por dia)
- Criar versoes diferentes do mesmo video para testar qual converte mais

---

## Quanto custa?

| Plano | Preco | O que inclui | Tem acesso a API? |
|-------|-------|--------------|-------------------|
| Gratuito | R$ 0 | 3 videos/mes, 3 min cada, com marca d'agua, 720p | NAO |
| Creator | ~US$ 29/mes (US$ 24 no anual) | Videos ilimitados, 1080p, sem marca d'agua | SIM |
| Business | ~US$ 149/mes | Tudo do Creator + 4K + time | SIM |

**IMPORTANTE:** O plano gratuito NAO da acesso a API.
Isso significa que pelo plano gratuito voce pode criar videos pelo site do HeyGen
(manualmente), mas o comando /video-heygen nao consegue gerar automaticamente.

**Recomendacao para comecar:**
1. Crie a conta gratuita e teste pelo site (app.heygen.com)
2. Quando gostar do resultado, assine o Creator
3. Pegue a chave de API e conecte aqui

**Conta de padaria:**
Um video de 60 segundos custa ~US$ 0,50 em creditos.
Se voce faz 10 videos por mes = US$ 5.
O plano Creator (US$ 29/mes) inclui 15 minutos = ~15 videos de 60s.
Compensa a partir de 5-10 videos por mes.

---

## Etapa 1. Criar sua conta no HeyGen

1. Abra o navegador e acesse: **heygen.com**
2. Clique no botao **"Get started for free"** (ou "Comecar gratis")
3. Escolha como quer entrar:
   - **Google** (mais rapido, um clique)
   - **Email + senha** (crie uma senha)
4. Pronto, voce ja tem conta

Nao precisa de cartao de credito para criar a conta.

---

## Etapa 2. Conhecer o painel (opcional, mas recomendado)

Antes de pegar a API, vale explorar o HeyGen pelo site para entender como funciona:

1. Apos entrar, voce vera o painel principal
2. Clique em **"Create Video"** para ver como funciona
3. Escolha um avatar da biblioteca (tem centenas de opcoes)
4. Escreva um texto curto e clique em **"Submit"**
5. O HeyGen vai gerar um video de teste para voce ver a qualidade

Esse teste e gratuito e ajuda a decidir se vale a pena assinar.

---

## Etapa 3. Assinar o plano Creator

Para usar o /video-heygen, voce precisa do plano Creator:

1. No painel do HeyGen, clique no seu avatar (canto superior direito)
2. Clique em **"Pricing"** ou **"Upgrade"**
3. Escolha o plano **Creator**
   - Mensal: US$ 29/mes
   - Anual: US$ 24/mes (economia de ~17%)
4. Preencha os dados de pagamento e confirme

**DICA:** Se preferir testar antes, use o painel gratuito para criar
alguns videos manualmente. Quando estiver convencido, assine e volte aqui.

---

## Etapa 4. Pegar sua chave de API

Essa e a parte mais importante. A chave de API e como uma "senha" que permite
que o assistente se conecte a sua conta do HeyGen automaticamente.

### Passo a passo:

1. Entre no painel: **app.heygen.com**
2. Clique no seu **avatar ou foto** (canto superior direito da tela)
3. Clique em **"Settings"** (Configuracoes)
4. No menu do lado esquerdo, procure e clique em **"API"**
5. Voce vera sua chave de API (ou um botao para gerar uma nova)
6. Clique em **"Copy"** (Copiar) ou **"Generate"** (Gerar) se for a primeira vez

**ATENCAO IMPORTANTE:**
Copie a chave IMEDIATAMENTE e guarde em um lugar seguro.
Depois que voce sair dessa pagina, NAO vai conseguir ver a chave de novo.
Se perder, tera que gerar uma nova (e a antiga para de funcionar).

A chave tem este formato (exemplo ficticio):
```
MGRlMjM1MzBlOTAzNDY5MmI3YjY4ZjQ5...
```
E uma sequencia longa de letras e numeros. Copie TUDO, sem espacos.

---

## Etapa 5. Colar a chave no projeto

Agora voce vai conectar o HeyGen ao seu projeto:

1. Abra a pasta do projeto no seu computador
2. Procure o arquivo chamado **`.env`** na raiz do projeto
   - Se nao existir, copie o arquivo `.env.example` e renomeie para `.env`
3. Abra o arquivo `.env` com qualquer editor de texto (Bloco de Notas serve)
4. Procure a linha:
   ```
   HEYGEN_API_KEY=
   ```
5. Cole sua chave depois do sinal de igual:
   ```
   HEYGEN_API_KEY=MGRlMjM1MzBlOTAzNDY5MmI3YjY4ZjQ5...
   ```
6. **Salve o arquivo** (Ctrl+S)

**Cuidados:**
- NAO coloque espacos antes ou depois da chave
- NAO coloque aspas ao redor da chave
- NAO compartilhe essa chave com ninguem (ela da acesso a sua conta)

---

## Etapa 6. Testar a conexao

Volte ao assistente e rode o comando:
```
/video-heygen
```

Se tudo estiver certo, ele vai confirmar que a conexao esta funcionando
e te levar direto para criar seu primeiro video.

Se der erro, verifique:
- A chave foi copiada inteira? (sem cortar nenhum caractere)
- Tem espacos extras antes ou depois da chave?
- Voce esta no plano Creator ou superior? (gratuito nao tem API)

---

## Configuracoes opcionais (para agilizar)

Se voce ja sabe qual avatar e voz quer usar, pode salvar no `.env`
para nao precisar escolher toda vez:

```
HEYGEN_AVATAR_ID=seu_avatar_id_aqui
HEYGEN_VOICE_ID=seu_voice_id_aqui
```

**Como descobrir o ID do avatar:**
- Ao rodar /video-heygen pela primeira vez, o sistema lista os avatares disponiveis com seus IDs
- Copie o ID do avatar que mais gostou e cole no `.env`

**Como descobrir o ID da voz:**
- O sistema tambem lista as vozes disponiveis com IDs
- Copie o ID da voz que prefere e cole no `.env`

Assim, nos proximos videos, ele ja usa o avatar e a voz que voce escolheu
sem precisar perguntar de novo.

---

## Perguntas frequentes

**Preciso instalar algum programa?**
Nao. Tudo funciona pela internet. O HeyGen roda nos servidores deles.

**Posso usar minha propria foto como avatar?**
Sim. O /video-heygen tem a opcao de enviar uma foto e o HeyGen transforma
em avatar falante. A foto precisa ser de rosto frontal, bem iluminada.

**Posso usar foto do Pinterest ou banco de imagens?**
Sim. Pode usar qualquer foto de rosto frontal. Muitos infoprodutores usam
fotos de banco de imagens para criar um "porta-voz" para o produto.

**Quanto tempo leva para gerar um video?**
Entre 2 e 5 minutos, dependendo da duracao do roteiro.

**Posso cancelar o plano depois?**
Sim. O plano Creator e mensal e pode ser cancelado a qualquer momento.

**A qualidade e boa para anuncios?**
Sim. O HeyGen gera videos em 1080p (Full HD) no plano Creator,
que e a qualidade padrao para Reels e anuncios no Meta Ads.

**Posso clonar minha propria voz?**
Sim. O HeyGen tem recurso de clonagem de voz. Voce envia um audio
de ~30 segundos falando naturalmente e ele cria uma voz sintetica
que soa como voce. Essa opcao esta disponivel no plano Creator.

---

## Links uteis

- Site do HeyGen: heygen.com
- Painel (login): app.heygen.com
- Precos: heygen.com/pricing
- Precos da API: heygen.com/api-pricing
- Documentacao da API: docs.heygen.com
- Suporte: help.heygen.com
