---
name: workshop-marketing:configurar-imagens
description: Guia para conectar uma API de geração de imagens (OpenRouter/Nano Banana) ao projeto. Salva OPENROUTER_API_KEY no .env, usado pelas skills /img-anuncio e /criativo-de-imagem.
---

# Como Configurar a Geracao de Imagens com IA

Guia completo para conectar uma API de geracao de imagens ao Workshop Marketing IA.
Tempo estimado: 5 minutos.

---

## O que isso faz?

Quando voce usa o comando `/img-anuncio`, o assistente cria imagens prontas
para usar nos seus anuncios do Instagram e Facebook. Imagens profissionais,
no tamanho certo, com o estilo que voce escolher.

Para isso funcionar automaticamente, voce precisa conectar uma API de geracao
de imagens. E como dar ao assistente acesso a uma "impressora de imagens".

**Sem a API:** o assistente gera os prompts (descricoes detalhadas da imagem)
e voce copia e cola manualmente em qualquer gerador de imagem (Midjourney,
Leonardo.ai, Freepik, etc.).

**Com a API:** o assistente gera a imagem automaticamente e salva na sua pasta
de entregas. Pronto para subir no Meta Ads.

---

## Qual API escolher?

Recomendamos o **OpenRouter** como API principal. Ele e um "portal" que da acesso
a dezenas de modelos de geracao de imagem por um unico cadastro.

| API | Custo | Qualidade | Facilidade |
|-----|-------|-----------|------------|
| **OpenRouter** (recomendado) | ~US$ 0,01-0,05 por imagem | Alta (varios modelos) | Muito facil |
| Freepik AI (alternativa) | Plano com API a partir de ~US$ 10/mes | Boa | Facil |

**Conta de padaria (OpenRouter):**
- 1 imagem de teste (Flux Schnell) = ~US$ 0,003 (menos de 1 centavo)
- 1 imagem final (Flux Pro) = ~US$ 0,05
- Se voce gera 20 imagens por mes = ~US$ 1,00
- Voce carrega creditos (minimo US$ 5) e vai usando conforme precisa

---

## Opcao 1. OpenRouter (Recomendado)

### Etapa 1. Criar sua conta

1. Abra o navegador e acesse: **openrouter.ai**
2. Clique em **"Sign Up"** (Criar conta)
3. Escolha como quer entrar:
   - **Google** (mais rapido)
   - **Email + senha**
4. Pronto, conta criada

Nao precisa de cartao de credito para criar a conta.

### Etapa 2. Adicionar creditos

Para gerar imagens, voce precisa de um saldo minimo:

1. Apos entrar, clique no seu nome (canto superior direito)
2. Clique em **"Credits"** ou **"Billing"**
3. Clique em **"Add Credits"**
4. Escolha o valor (minimo US$ 5. dura meses para geracao de imagem)
5. Preencha os dados de pagamento e confirme

**DICA:** Com US$ 5 voce gera mais de 100 imagens de teste (Flux Schnell)
ou cerca de 100 imagens finais (Flux Pro). Dura bastante.

### Etapa 3. Pegar sua chave de API

1. Acesse: **openrouter.ai/settings/keys** (ou clique no menu > Settings > API Keys)
2. Clique em **"Create Key"** (Criar chave)
3. De um nome para a chave (ex: "Workshop Marketing")
4. Clique em **"Create"**
5. A chave vai aparecer na tela. **COPIE IMEDIATAMENTE**

**ATENCAO IMPORTANTE:**
A chave so aparece uma vez. Depois que voce fechar a pagina, nao consegue
ver de novo. Se perder, gere uma nova (a antiga para de funcionar).

A chave tem este formato:
```
sk-or-v1-abc123def456...
```
Comeca com `sk-or-v1-`. Copie TUDO, sem espacos.

### Etapa 4. Colar a chave no projeto

1. Abra a pasta do projeto no seu computador
2. Procure o arquivo chamado **`.env`** na raiz do projeto
   - Se nao existir, copie o arquivo `.env.example` e renomeie para `.env`
3. Abra o arquivo `.env` com qualquer editor de texto (Bloco de Notas serve)
4. Procure a linha:
   ```
   OPENROUTER_API_KEY=
   ```
5. Cole sua chave depois do sinal de igual:
   ```
   OPENROUTER_API_KEY=sk-or-v1-abc123def456...
   ```
6. **Salve o arquivo** (Ctrl+S)

**Cuidados:**
- NAO coloque espacos antes ou depois da chave
- NAO coloque aspas ao redor da chave
- NAO compartilhe essa chave com ninguem

### Etapa 5. Escolher o modelo (opcional)

O OpenRouter da acesso a varios modelos de geracao de imagem.
O padrao ja vem configurado (Flux Schnell. rapido e barato).

Se quiser mudar, edite essa linha no `.env`:
```
OPENROUTER_IMAGE_MODEL=black-forest-labs/flux-schnell
```

**Modelos disponiveis:**

| Modelo | Para que serve | Velocidade | Custo por imagem |
|--------|---------------|------------|------------------|
| `black-forest-labs/flux-schnell` | Testes rapidos, rascunhos | Muito rapido | ~US$ 0,003 |
| `black-forest-labs/flux-1.1-pro` | Imagens finais, alta qualidade | Rapido | ~US$ 0,05 |
| `openai/dall-e-3` | Conceitos criativos, texto na imagem | Medio | ~US$ 0,04 |
| `stability-ai/stable-diffusion-3.5-large` | Fotos realistas | Medio | ~US$ 0,04 |

**Recomendacao:**
- Para testar ideias: mantenha o `flux-schnell` (padrao)
- Para imagem final do anuncio: troque para `flux-1.1-pro`
- Para imagem com texto legivel: use `dall-e-3`

### Etapa 6. Testar a conexao

Volte ao assistente e rode o comando:
```
/img-anuncio
```

Se tudo estiver certo, ele vai confirmar que a conexao esta funcionando
e te levar direto para criar sua primeira imagem de anuncio.

Se der erro, verifique:
- A chave foi copiada inteira? (sem cortar nenhum caractere)
- Tem espacos extras antes ou depois da chave?
- Voce adicionou creditos na sua conta?

---

## Opcao 2. Freepik AI (Alternativa)

Use o Freepik se preferir uma interface mais visual ou se ja tiver conta Premium.

### Etapa 1. Criar conta e assinar plano com API

1. Acesse: **freepik.com**
2. Crie uma conta (Google ou email)
3. Assine um plano que inclua acesso a API (verifique em freepik.com/pricing)

### Etapa 2. Pegar a chave de API

1. Acesse: **freepik.com** > seu perfil > API
2. Clique em **"Manage API Keys"**
3. Clique em **"Create Key"**
4. Copie a chave gerada

### Etapa 3. Colar no projeto

1. Abra o arquivo `.env` na raiz do projeto
2. Procure a linha:
   ```
   FREEPIK_API_KEY=
   ```
3. Cole sua chave:
   ```
   FREEPIK_API_KEY=sua_chave_aqui
   ```
4. Salve o arquivo

### Etapa 4. Testar

Rode `/img-anuncio` e o assistente vai detectar a chave do Freepik automaticamente.

---

## Perguntas frequentes

**Preciso instalar algum programa?**
Nao. Tudo funciona pela internet. As APIs rodam nos servidores deles.

**Quanto custa por mes?**
Depende de quantas imagens voce gera. Com OpenRouter, a maioria dos usuarios
gasta menos de US$ 2/mes gerando 20-40 imagens. E pago por uso (sem mensalidade fixa).

**Posso usar as imagens geradas nos meus anuncios?**
Sim. As imagens geradas por IA sao de uso comercial. Voce pode usar
em anuncios, posts, paginas, onde quiser.

**E se eu nao quiser pagar nada?**
Sem problema. O assistente gera os prompts detalhados e voce usa qualquer
ferramenta gratuita para criar a imagem: Canva, Leonardo.ai (plano free),
ou o proprio site do Freepik (com limite de geracoes gratuitas).

**Posso trocar de API depois?**
Sim. Basta mudar a chave no arquivo `.env`. O assistente detecta
automaticamente qual API esta configurada.

**A qualidade e boa para anuncios profissionais?**
Sim. Os modelos como Flux Pro e DALL-E 3 geram imagens em alta resolucao
(1024x1024 ou maior) com qualidade profissional. Para anuncios no Instagram,
a resolucao e mais que suficiente.

---

## Links uteis

- OpenRouter: openrouter.ai
- OpenRouter (chaves de API): openrouter.ai/settings/keys
- OpenRouter (modelos de imagem): openrouter.ai/models?modality=image
- Freepik: freepik.com
- Freepik API: freepik.com > perfil > API
