---
name: ht-repitch
description: >
  Revisa e ajusta um pitch de venda já existente (palco, call 1:1, WhatsApp)
  a partir dos resultados reais da tentativa. Identifica pontos fracos de
  ancoragem, objeções mal quebradas, CTA frouxo e entrega versão nova do
  pitch corrigido sem reescrever do zero, mantendo a voz do aluno.
---

# HT Repitch. Revisão de Pitch Existente

Pega um pitch que já foi usado em um evento, call ou fluxo de WhatsApp e gera uma versão corrigida baseada no que deu errado. Não é gerar um pitch novo. É diagnosticar, mostrar as causas raiz e reescrever só o que precisa mudar, mantendo o estilo e a voz do aluno.

## Quando Usar

- Depois que o aluno rodou um `/ht-pitch-palco`, `/ht-fechamento`, `/ht-whatsapp` ou pitch próprio e os resultados vieram abaixo do esperado.
- Quando o aluno disser "meu pitch não está convertendo", "pitchei e ninguém comprou", "preciso ajustar meu pitch", "quero um repitch".
- Antes de rodar o mesmo pitch de novo na próxima live, call ou evento.

## O Que Fazer

### 0. Contexto

Leia `entregas/.ativo`, `entregas/{ativo}/perfil.md` e `entregas/{ativo}/idconsumidor.md` (se existir).

### 1. Entrevista diagnóstica (uma pergunta por vez)

**Pergunta 1. Qual pitch vamos revisar?**
1. Pitch de palco (evento C10X, webinar)
2. Pitch de call 1:1 (SPIN, fechamento)
3. Pitch de WhatsApp
4. Outro (o aluno descreve)

Se houver arquivos em `entregas/{ativo}/comercial/`, ofereça a lista.

**Pergunta 2. Compartilhe o pitch original.**
- Caminho do arquivo em `entregas/{ativo}/comercial/`, ou
- Cola o texto direto no chat

**Pergunta 3. Quais foram os resultados reais?**
- Quantas pessoas assistiram ou ouviram
- Quantas compraram
- Taxa de conversão calculada
- Principais objeções que ouviu depois
- Onde a plateia ou o lead esfriou (no preço, no bônus, na chamada pra ação, em algum momento específico)

**Pergunta 4. O que você sente que falhou?**
(lista pro aluno marcar 1 ou mais)
1. Ancoragem fraca (preço pareceu caro)
2. Objeção de preço não foi quebrada antes do preço
3. Bônus não fez diferença
4. CTA ambíguo (ninguém sabia o que fazer)
5. Autoridade baixa (parecia inseguro)
6. Urgência fraca (não tinha motivo pra comprar agora)
7. Não sei o que falhou

### 2. Auditoria em 3 blocos

Leia o pitch original linha por linha e gere o diagnóstico estruturado:

**Bloco 1. Diagnóstico detalhado (5 a 8 pontos)**
Pra cada ponto fraco identificado, cite o trecho exato do pitch, explique o que está errado e compare com a estrutura ideal (puxando de `/ht-pitch-palco` ou `/ht-fechamento` como referência).

```
1. Ancoragem fraca na abertura
   Trecho: "Hoje eu vou te mostrar como ganhar X"
   Problema: abertura genérica sem ancorar valor do problema
   Como corrigir: começar pela dor específica + custo de não resolver
```

**Bloco 2. Causas raiz (2 ou 3)**
Agrupe os 5 a 8 pontos em 2 ou 3 causas maiores. A maioria dos pitches falha em 1 ou 2 coisas estruturais, não em 8 coisas pequenas.

```
Causa 1: Falta de ancoragem no custo de não resolver
Causa 2: Oferta apresentada antes da prova de valor
```

**Bloco 3. Ajustes propostos**
Pra cada bloco do pitch (abertura, conteúdo, transição, oferta, preço, bônus, CTA, fechamento), diga o que precisa mudar em linguagem concreta.

### 3. Mostrar diagnóstico e pedir aprovação

Mostre os 3 blocos e pergunte:
```
1. Pode reescrever o pitch com esses ajustes
2. Quero conversar sobre algum ponto antes
3. Tem algo que você discorda? Me diz o quê
```

Só reescreve depois do OK.

### 4. Reescrever o pitch

Aplique os ajustes mantendo:
- Tamanho aproximado do original (pelo menos 80% do tamanho)
- Voz do aluno (vocabulário, expressões, maneirismos)
- Estrutura geral (se era palco, continua palco; se era WhatsApp, continua WhatsApp)

Corrija:
- Ancoragem de valor (antes do preço, sempre)
- Quebra de objeção (antes da objeção aparecer)
- Stack de valor (ordem dos entregáveis + soma de valor antes do preço real)
- CTA explícito (sem ambiguidade)
- Urgência e escassez justificadas (nunca artificiais)
- Autoridade (inserir onde couber)

### 5. Mostrar versão nova e pedir aprovação

```
1. Aprovar e salvar
2. Quero ajustar X ou Y
3. Voltar pra versão antiga e reescrever outra parte
```

### 6. Salvar

Arquivo: `entregas/{ativo}/comercial/repitch-{data}.md`

Estrutura:
```markdown
# Repitch {tipo de pitch}

Data: {data}
Resultado da versão anterior: {n pessoas / n vendas / %}

## Diagnóstico
{bloco 1}

## Causas raiz
{bloco 2}

## Versão antiga (referência)
{pitch original}

## Versão nova
{pitch reescrito}

## Ajustes principais
- {ajuste 1}
- {ajuste 2}
- ...
```

### 7. Próximos passos

```
Pronto. Repitch salvo.

Arquivo: entregas/{ativo}/comercial/repitch-{data}.md

Próximos passos:
- Rode a versão nova na próxima oportunidade
- Meça de novo (pessoas, vendas, objeções)
- Se ainda tiver objeção residual, use /ht-objecoes pra mapear
- Se o CTA continuar fraco no WhatsApp, use /ht-whatsapp pra refazer o fluxo
```

## Regras

- Nunca reescrever sem o diagnóstico estar aprovado primeiro.
- Respeitar a voz do aluno. Não substituir expressões que fazem parte do estilo dele.
- Se o aluno não souber os resultados exatos, aceitar descrição qualitativa (ex: "senti que esfriou no preço", "ninguém perguntou nada depois do bônus").
- A versão nova precisa ter tamanho próximo da original. Se ficar muito menor ou muito maior, explicar porquê.
- Se o pitch original estiver fundamentalmente errado (ex: não é um pitch, é só conteúdo), interromper e sugerir `/ht-pitch-palco` ou `/ht-fechamento` pra começar do zero.
- Não usar travessão em nenhum texto exibido.
