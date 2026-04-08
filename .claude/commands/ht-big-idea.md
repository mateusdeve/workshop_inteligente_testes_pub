---
name: workshop-marketing:ht-big-idea
description: Criar a Big Idea completa de um evento C10X. promessa principal, mote memorável e posicionamento. Base de tudo no funil de High Ticket.
---

# HT. Big Idea do Evento

Cria a Big Idea completa do evento high ticket: promessa, mote e posicionamento estratégico.

## Usage

```
/c10x-big-idea
```

## O Que Fazer

### 1. Contexto
Leia `entregas/.ativo`, depois `entregas/{ativo}/perfil.md` e `entregas/{ativo}/idconsumidor.md`.

Verifique `entregas/{ativo}/pesquisa-mercado.md`. Se não existir ou tiver mais de 90 dias, acione a skill `pesquisa-mercado` antes de criar a Big Idea. A pesquisa é obrigatória: ela traz concorrentes do nicho high ticket, faixa de preço praticada, promessas usadas no mercado (para você diferenciar a Big Idea do que já existe) e objeções reais que a Big Idea precisa antecipar.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4. Formato do Evento:**
```
Qual o formato do evento?

1. Retiro Online (imersão 1-3 dias, alta conversão)
2. Webinar/Aula ao vivo (evento único com pitch)
3. Workshop intensivo (meio-dia ou dia cheio)

Digite o número:
```

```
--- Bloco 1/4 concluído ---
Formato: [tipo escolhido]
Próximo: Transformação do evento
---
```

**Bloco 2/4. Transformação:**
```
Qual a transformação específica que o participante alcança AO FINAL do evento?
Não é o que vai aprender. é o que vai conseguir fazer ou ter.
(ex: "sair com a estrutura do produto pronta", "fechar o primeiro cliente high ticket")
```

```
--- Bloco 2/4 concluído ---
Formato: [tipo]
Transformação: [resultado]
Próximo: Público e dor principal
---
```

**Bloco 3/4. Dor Principal:**
```
Qual a maior dor ou obstáculo do público antes do evento?
(ex: "não sabe como precificar", "tem medo de vender caro e assustar o cliente")
```

```
--- Bloco 3/4 concluído ---
Formato: [tipo]
Transformação: [resultado]
Dor: [obstáculo]
Próximo: Diferencial do evento
---
```

**Bloco 4/4. Diferencial:**
```
O que torna este evento diferente de tudo que já existe no mercado?
(ex: "metodologia exclusiva testada em 300 alunos", "acesso direto ao especialista para revisar ao vivo")
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Formato: [tipo de evento]
- Transformação: [resultado principal]
- Dor atacada: [obstáculo]
- Diferencial: [o que é único]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

Gere os 3 elementos da Big Idea:

**Elemento 1. Promessa do Evento:**

Use a fórmula:
"Em [TEMPO], você vai [TRANSFORMAÇÃO ESPECÍFICA], mesmo que [OBJEÇÃO COMUM], através do [MÉTODO ÚNICO]"

Gere 3 variações. A melhor será usada na página de inscrição, anúncios e comunicação pré-evento.

Regras da promessa:
- Tempo claro (duração do evento ou prazo de resultado)
- Transformação tangível e verificável
- Objeção real do público (não genérica)
- Método com nome próprio

**Elemento 2. Mote do Evento:**

Nome curto e memorável do evento (máx 5 palavras). Deve ser:
- Emocional. gera desejo ou curiosidade
- Claro. entendível sem contexto
- Único. não usa palavras genéricas ("Imersão", "Masterclass", "Treinamento")
- Compartilhável. fácil de falar e lembrar

Gere 5 opções de mote e indique a mais forte.

Frameworks para o mote:
- Ação + Resultado (ex: "Feche em Dois Dias")
- Elemento + Transformação (ex: "Virada de Alto Valor")
- Nome Exclusivo (ex: "Protocolo Elite")
- Desafio/Movimento (ex: "O Primeiro Sim")

**Elemento 3. Posicionamento:**

Para quem é e para quem NÃO é.

Para quem é:
- Perfil 1 (situação atual + desejo)
- Perfil 2 (situação atual + desejo)
- Perfil 3 (situação atual + desejo)

Para quem NÃO é:
- Quem espera resultado sem implementar
- Quem quer fórmula mágica sem método
- [Exclusão específica do nicho]

### 4. Aprovação
```
Mostrar os 3 elementos gerados e perguntar:

1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`entregas/{ativo}/c10x/big-idea-[evento].md`

### 6. Próximo Passo
"Big Idea criada. Próximo passo: `/ht-oferta` para estruturar o que o aluno recebe e o preço."
