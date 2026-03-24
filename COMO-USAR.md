# Como Usar o Workshop Marketing IA — Guia Completo

## Antes de comecar

1. VSCode instalado
2. Extensao Claude Code instalada
3. Pasta do projeto aberta no VSCode

## Seu primeiro uso

### 1. Abra o chat do Claude Code

No VSCode, procure o icone do Claude Code na barra lateral.

### 2. Cadastre seu produto

Digite no chat:

```text
/meu-produto
```

O assistente vai te guiar com perguntas sobre:

- Quadro (a transformacao principal do seu produto)
- Furadeira (seu metodo estruturado)
- Identidade do consumidor (quem e seu publico)
- Decorados (beneficios do seu produto)

Responda uma pergunta por vez.

### 3. Crie a identidade do consumidor

```text
/idconsumidor
```

O assistente cria a identidade do consumidor (cliente ideal): paliativos, objeções e tom de voz. As Urgências Ocultas ficam no `/meu-produto` (`perfil.md`).

### 4. Crie seus materiais

Use os comandos na ordem que fizer sentido para voce.

## Fluxos recomendados

### Para quem quer comecar a vender

1. `/meu-produto` — Cadastrar produto
2. `/idconsumidor` — Perfil do cliente ideal
3. `/texto-de-venda` — Criar copy
4. `/pagina-de-vendas` — Criar pagina profissional
5. `/anuncio` — Criar anuncios para trafego

### Para quem vai lancar

1. `/meu-produto` — Cadastrar produto
2. `/idconsumidor` — Perfil do cliente ideal
3. `/lancamento` — Planejar o evento completo
4. `/pagina-de-vendas` — Criar pagina do evento + pagina de vendas
5. `/sequencia-de-emails` — Criar emails do pico de vendas
6. `/anuncio` — Criar anuncios de captacao
7. `/conteudo-social` — Criar conteudo pre-lancamento

### Para quem quer vender no perpetuo

1. `/meu-produto` — Cadastrar produto
2. `/idconsumidor` — Perfil do cliente ideal
3. `/funil-de-vendas` — Mapear funil perpetuo
4. `/pagina-de-vendas` — Criar paginas (captura + vendas + obrigado)
5. `/sequencia-de-emails` — Criar email de nutricao
6. `/anuncio` — Criar anuncios para cada fase do funil

### Para quem quer vender low ticket (D48)

1. `/meu-produto` — Cadastrar produto
2. `/idconsumidor` — Perfil do cliente ideal
3. `/low-ticket` — Criar produto de entrada (quiz, desafio, ebook)
4. `/anuncio` — Criar anuncios caixa rapido para o quiz
5. `/funil-de-vendas` — Mapear funil D48 com upsell

### Para quem quer vender high ticket

1. `/meu-produto` — Cadastrar produto
2. `/idconsumidor` — Perfil do cliente ideal
3. `/lancamento` — Planejar retiro/evento online
4. `/playbook-comercial` — Criar scripts SPIN para venda 1:1
5. `/pagina-de-vendas` — Criar pagina do evento

## O que cada comando faz

### /meu-produto

Cadastra seu produto usando a metodologia VTSD: Quadro (transformacao), Furadeira (metodo), Decorados (beneficios) e 3 Identidades.

Resultado: `meu-negocio/perfil.md`

### /idconsumidor

Cria a identidade do consumidor (cliente ideal): paliativos, objeções e comunicação. Urgências Ocultas permanecem em `perfil.md`.

Resultado: `meu-negocio/idconsumidor.md`

### /pagina-de-vendas

Cria paginas HTML profissionais com design moderno e responsivo. Tres tipos: vendas (estrutura 8D), captura e obrigado.

Resultado: `entregas/paginas/[tipo]-[produto].html`

Como ver: abra o arquivo `.html` no navegador.

### /copy-pagina

Cria a copy completa da pagina de vendas com todas as 16 secoes (estrutura 8D expandida). Texto pronto para virar pagina HTML.

Resultado: `entregas/copy-pagina/copy-[produto].md`

### /anuncio

Cria pacotes de anuncios usando a Mandala de 18 Tipos. Inclui copy, direcao criativa e estrategia de campanha.

Resultado: `entregas/anuncios/anuncios-[plataforma]-[produto].md`

### /conteudo-social

Cria carrosseis, captions, roteiros de Reels, linha editorial e calendario de publicacao.

Resultado: `entregas/conteudo-social/[tipo]-[produto].md`

### /roteiro-de-video

Cria roteiros para VVV (video de vendas), Reels 60s, YouTube e scripts para avatar HeyGen.

Resultado: `entregas/textos-de-venda/roteiro-[formato]-[produto].md`

### /sequencia-de-emails

Cria sequencias completas: pico de vendas (6 fases), nutricao, boas-vindas, carrinho abandonado.

Resultado: `entregas/emails/sequencia-[tipo]-[produto].md`

### /lancamento

Planeja lancamento ou evento completo: Big Idea, cronograma, materiais necessarios, estrutura de campanha.

Resultado: `entregas/textos-de-venda/lancamento-[evento].md`

### /funil-de-vendas

Mapeia funil completo: perpetuo, lancamento ou D48 (low ticket com quiz). Inclui todas as etapas e metricas.

Resultado: `entregas/textos-de-venda/funil-[tipo]-[produto].md`

### /playbook-comercial

Cria scripts de venda 1:1 usando SPIN Selling: roteiro de call, pitch, quebra de objecoes, script de WhatsApp.

Resultado: `entregas/comercial/playbook-[produto].md`

### /criativo-de-imagem

Gera prompts detalhados para Midjourney, DALL-E ou Freepik AI. Inclui direcao criativa e especificacoes tecnicas.

Resultado: `entregas/criativos/prompts-[tipo]-[produto].md`

### /low-ticket

Cria produto de entrada usando a metodologia D48 (R$37-97): pagina final do quiz (12 blocos), anuncios caixa rapido, produto desafio, agente GPT vendavel e copy para Hotmart/Kiwify.

Resultado: `entregas/paginas/quiz-[produto].html`, `entregas/anuncios/caixa-rapido-[produto].md`, `entregas/textos-de-venda/desafio-[produto].md`

## Dicas para melhores resultados

1. Quanto mais detalhes voce der, melhor o resultado.
2. Peca alteracoes: "mude o titulo", "adicione depoimentos", "troque a cor".
3. Use os comandos na ordem sugerida — cada um usa informacoes dos anteriores.
4. Revise antes de publicar.
5. Atualize seu produto com `/meu-produto` quando mudar algo.

## Perguntas frequentes

**Preciso saber programar?**
Nao. Tudo funciona por conversa.

**Posso usar as paginas?**
Sim. Os arquivos HTML podem ser hospedados em qualquer servico ou publicados na Vercel. Voce tambem pode copiar os textos para WordPress, Elementor, Carrd, etc.

**Posso pedir alteracoes?**
Sim. Basta pedir no chat: "mude a cor para azul", "adicione FAQ", etc.

**Onde ficam meus arquivos?**
Na pasta `entregas/`, organizada por tipo.

**O que e a metodologia VTSD?**
Venda Todo Santo Dia — metodologia de Leandro Ladeira para infoprodutores venderem no perpetuo com copy argumentativa e logica. Inclui conceitos como Quadro, Furadeira, Decorados, Light Copy, Mandala de Anuncios e Estrutura 8D.
