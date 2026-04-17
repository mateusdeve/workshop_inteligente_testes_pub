# Como Usar o Workshop Marketing IA — Guia Completo

## Antes de comecar

### Opcao A. Claude Code (VS Code)

1. VSCode instalado
2. Extensao Claude Code instalada
3. Pasta do projeto aberta no VSCode

### Opcao B. Cursor

1. Cursor instalado ([cursor.com](https://cursor.com))
2. **File → Open Folder** e escolha a pasta `workshop_inteligente` (ou o nome da sua copia do repo)
3. Pronto. As regras em `.cursor/rules/` e o `CLAUDE.md` passam a orientar o chat. Veja também `AGENTS.md` para um mapa rapido de pastas.

**Comandos `/alguma-coisa` no Cursor:** a barra `/` nao e a mesma do Claude Code. Para seguir um fluxo (ex.: copy-pagina), diga no chat **"segue o comando copy-pagina"** ou anexe o arquivo **`.claude/commands/copy-pagina.md`** com `@`. O assistente executa o mesmo roteiro do `.md`.

---

## Seu primeiro uso

### 1. Abra o chat do assistente

**No VSCode:** procure o icone do Claude Code na barra lateral.

**No Cursor:** use o chat do agente (Composer ou Chat) com o projeto aberto.

### 2. Cadastre seu produto

Digite no chat:

```text
/produto-concepcao
```

O assistente vai te guiar com perguntas sobre:

- Quadro (a transformacao principal do seu produto)
- Furadeira (seu metodo estruturado)
- Identidade do consumidor (quem e seu publico)
- Decorados (beneficios do seu produto)

Responda uma pergunta por vez.

### 3. Crie a identidade do consumidor

```text
/produto-consumidor
```

O assistente cria a identidade do consumidor (cliente ideal): paliativos, objeções e tom de voz. As Urgências Ocultas ficam no `/produto-concepcao` (`perfil.md`).

### 4. Crie seus materiais

Use os comandos na ordem que fizer sentido para voce.

## Fluxos recomendados

### Para quem quer comecar a vender

1. `/produto-concepcao` — Cadastrar produto
2. `/produto-consumidor` — Perfil do cliente ideal
3. `/texto-de-venda` — Criar copy
4. `/pagina-de-vendas` — Criar pagina profissional
5. `/copy-anuncio` — Criar anuncios para trafego

### Para quem vai lancar

1. `/produto-concepcao` — Cadastrar produto
2. `/produto-consumidor` — Perfil do cliente ideal
3. `/lancamento` — Planejar o evento completo
4. `/pagina-de-vendas` — Criar pagina do evento + pagina de vendas
5. `/sequencia-de-emails` — Criar emails do pico de vendas
6. `/copy-anuncio` — Criar anuncios de captacao
7. `/copy-social` — Criar conteudo pre-lancamento

### Para quem quer vender no perpetuo

1. `/produto-concepcao` — Cadastrar produto
2. `/produto-consumidor` — Perfil do cliente ideal
3. `/estrategia-funil` — Mapear funil perpetuo
4. `/pagina-de-vendas` — Criar paginas (captura + vendas + obrigado)
5. `/sequencia-de-emails` — Criar email de nutricao
6. `/copy-anuncio` — Criar anuncios para cada fase do funil

### Para quem quer vender low ticket (low ticket)

1. `/produto-concepcao` — Cadastrar produto
2. `/produto-consumidor` — Perfil do cliente ideal
3. `/low-ticket` — Criar produto de entrada (quiz, desafio, ebook)
4. `/copy-anuncio` — Criar anuncios low ticket para o quiz
5. `/estrategia-funil` — Mapear funil low ticket com upsell

### Para quem quer vender high ticket

1. `/produto-concepcao` — Cadastrar produto
2. `/produto-consumidor` — Perfil do cliente ideal
3. `/lancamento` — Planejar retiro/evento online
4. `/playbook-comercial` — Criar scripts SPIN para venda 1:1
5. `/pagina-de-vendas` — Criar pagina do evento

## O que cada comando faz

### /produto-concepcao

Cadastra seu produto usando a metodologia VTSD: Quadro (transformacao), Furadeira (metodo), Decorados (beneficios) e 3 Identidades.

Resultado: `meus-produtos/{ativo}/perfil.md`

### /produto-consumidor

Cria a identidade do consumidor (cliente ideal): paliativos, objeções e comunicação. Urgências Ocultas permanecem em `perfil.md`.

Resultado: `meus-produtos/{ativo}/produto-consumidor.md`

### /pagina-de-vendas

Cria paginas HTML profissionais com design moderno e responsivo. Tres tipos: vendas (estrutura 8D), captura e obrigado.

Resultado: `meus-produtos/{ativo}/entregas/paginas/[tipo]-[produto].html`

Como ver: abra o arquivo `.html` no navegador.

### /copy-pagina

Cria a copy completa da pagina de vendas com todas as 16 secoes (estrutura 8D expandida). Texto pronto para virar pagina HTML.

Resultado: `meus-produtos/{ativo}/entregas/copy-pagina/copy-[produto].md`

### /copy-anuncio

Cria pacotes de anuncios usando a Mandala de 18 Tipos. Inclui copy, direcao criativa e estrategia de campanha.

Resultado: `meus-produtos/{ativo}/entregas/anuncios/anuncios-[plataforma]-[produto].md`

### /copy-social

Cria carrosseis, captions, roteiros de Reels, linha editorial e calendario de publicacao.

Resultado: `meus-produtos/{ativo}/entregas/conteudo-social/[tipo]-[produto].md`

### /roteiro-de-video

Cria roteiros para VVV (video de vendas), Reels 60s, YouTube e scripts para avatar HeyGen.

Resultado: `meus-produtos/{ativo}/entregas/textos-de-venda/roteiro-[formato]-[produto].md`

### /sequencia-de-emails

Cria sequencias completas: pico de vendas (6 fases), nutricao, boas-vindas, carrinho abandonado.

Resultado: `meus-produtos/{ativo}/entregas/emails/sequencia-[tipo]-[produto].md`

### /lancamento

Planeja lancamento ou evento completo: Big Idea, cronograma, materiais necessarios, estrutura de campanha.

Resultado: `meus-produtos/{ativo}/entregas/textos-de-venda/lancamento-[evento].md`

### /estrategia-funil

Mapeia funil completo: perpetuo, lancamento ou low ticket (low ticket com quiz). Inclui todas as etapas e metricas.

Resultado: `meus-produtos/{ativo}/entregas/textos-de-venda/funil-[tipo]-[produto].md`

### /playbook-comercial

Cria scripts de venda 1:1 usando SPIN Selling: roteiro de call, pitch, quebra de objecoes, script de WhatsApp.

Resultado: `meus-produtos/{ativo}/entregas/comercial/playbook-[produto].html` (abrir no navegador; Imprimir → Salvar como PDF)

### /img-anuncio

Gera prompts detalhados para Midjourney, DALL-E ou Freepik AI. Inclui direcao criativa e especificacoes tecnicas.

Resultado: `meus-produtos/{ativo}/entregas/criativos/prompts-[tipo]-[produto].md`

### /low-ticket

Cria produto de entrada usando a metodologia low ticket (R$37-97): pagina final do quiz (12 blocos), anuncios low ticket, produto desafio, agente GPT vendavel e copy para Hotmart/Kiwify.

Resultado: `meus-produtos/{ativo}/entregas/paginas/quiz-[produto].html`, `meus-produtos/{ativo}/entregas/anuncios/caixa-rapido-[produto].md`, `meus-produtos/{ativo}/entregas/textos-de-venda/desafio-[produto].md`

## Dicas para melhores resultados

1. Quanto mais detalhes voce der, melhor o resultado.
2. Peca alteracoes: "mude o titulo", "adicione depoimentos", "troque a cor".
3. Use os comandos na ordem sugerida — cada um usa informacoes dos anteriores.
4. Revise antes de publicar.
5. Atualize seu produto com `/produto-concepcao` quando mudar algo.

## Perguntas frequentes

**Preciso saber programar?**
Nao. Tudo funciona por conversa.

**Posso usar as paginas?**
Sim. Os arquivos HTML podem ser hospedados em qualquer servico ou publicados na Vercel. Voce tambem pode copiar os textos para WordPress, Elementor, Carrd, etc.

**Posso pedir alteracoes?**
Sim. Basta pedir no chat: "mude a cor para azul", "adicione FAQ", etc.

**Onde ficam meus arquivos?**
Na pasta `meus-produtos/{ativo}/entregas/`, organizada por tipo.

**O que e a metodologia VTSD?**
Venda Todo Santo Dia — metodologia de Leandro Ladeira para infoprodutores venderem no perpetuo com copy argumentativa e logica. Inclui conceitos como Quadro, Furadeira, Decorados, Light Copy, Mandala de Anuncios e Estrutura 8D.
