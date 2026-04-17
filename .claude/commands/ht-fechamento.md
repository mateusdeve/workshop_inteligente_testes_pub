---
name: workshop-marketing:ht-fechamento
description: Criar script de fechamento de venda 1:1 high ticket. conexão dor-solução, ancoragem de valor, apresentação de preço e envio do link com pressuposto do sim. Baseado no método C10X.
---

# HT. Script de Fechamento

Cria o script do momento de fechamento da venda 1:1 high ticket. da transição do SPIN para a oferta até o link de pagamento.

## Usage

```
/c10x-fechamento
```

## O Que Fazer

### 1. Contexto
Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/2. Produto e Preço:**
```
Qual o produto e o investimento?
(ex: "Mentoria de 3 meses. R$5.000 à vista ou 6x R$997")
```

```
--- Bloco 1/2 concluído ---
Produto: [nome] | R$ [valor]
Próximo: Forma de pagamento
---
```

**Bloco 2/2. Condições:**
```
Quais as formas de pagamento disponíveis?
(ex: "Pix com desconto, cartão em até 12x, boleto")
```

**Confirmação antes de gerar:**
```
Resumo:
- Produto: [nome]
- Preço: R$ [valor]
- Condições: [formas de pagamento]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**SCRIPT COMPLETO DE FECHAMENTO C10X**

---

**PASSO 1. CONEXÃO DOR-SOLUÇÃO**

Recapitule o que o lead disse durante o SPIN. Use as próprias palavras dele.

Script:
"[NOME], baseado em tudo que você me contou, sua principal dificuldade é [DOR PRINCIPAL. usar as palavras do lead, não as suas].

É exatamente isso que o [NOME DO PROGRAMA] resolve. Em [PRAZO], você vai [QUADRO. transformação principal].

Você recebe: [entregáveis em 3 bullets rápidos]."

---

**PASSO 2. ANCORAGEM DE VALOR**

Compare com alternativas que o lead já conhece ou considerou.

Script. opções de ancoragem:

A) Comparação com alternativas:
"Hoje, se você fosse resolver isso contratando [ALTERNATIVA 1]. já tentou isso antes?. você pagaria [VALOR MAIOR]. Com o [PROGRAMA], você tem [DIFERENCIAL] por [PREÇO MENOR]."

B) Comparação com o custo da inação:
"Você me disse que está [perdendo/deixando de ganhar] cerca de [VALOR] por mês por conta disso. Em [X meses], são [VALOR ACUMULADO]. O investimento no programa é de [PREÇO]."

C) Comparação com o valor individual:
"Se você fosse pagar por cada parte separada: [lista rápida com valores]. Somaria [ANCORAGEM ALTA]. O investimento é de [PREÇO]."

---

**PASSO 3. APRESENTAÇÃO DO PREÇO**

Script:
"E tudo isso por [VALOR]. Acessível?"

[Faça silêncio. Aguarde a resposta. Não continue antes.]

Se resposta positiva → Passo 4.
Se objeção → acesse `/ht-objecoes`.

---

**PASSO 4. ENVIO DO LINK**

Regra C10X: nunca pergunte se quer comprar. Assuma o interesse e envie.

Script:
"Ótimo. Vou te enviar o link de pagamento agora. Me confirma quando finalizar que já libero seus acessos / já te contato para iniciarmos."

[Envie o link imediatamente após falar isso. Não espere.]

---

**VARIAÇÃO. SE O LEAD HESITAR ANTES DO PREÇO**

Quando o lead perguntar "qual o preço?" antes do fim da apresentação:

"Antes de falar o investimento, quero ter certeza que faz sentido para você. Posso te mostrar mais uma coisa?"

[Se ele insistir no preço:]

"O investimento é [VALOR]. Mas antes de você decidir baseado só nisso, deixa eu te mostrar o que você recebe."

---

**VARIAÇÃO. DOWNSELL (se a venda não fechar)**

Quando o lead não fecha mas ainda tem interesse:

"Entendo. Antes de a gente encerrar. tem uma forma de começar com um investimento menor. [OFERTA DE ENTRADA]. Faz sentido como próximo passo?"

---

**REGRAS DO FECHAMENTO C10X:**
- O silêncio após o preço é parte do script. não o quebre
- Nunca pergunte "quer comprar?". assuma e envie o link
- Nunca reduza o preço antes de esgotar as quebras de objeção
- Nunca mencione desconto antes que o lead peça
- O link vai junto com a confirmação verbal. não espere o lead pedir

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`meus-produtos/{ativo}/entregas/c10x/fechamento-[produto].md`

### 6. Próximo Passo
"Fechamento pronto. Próximo: `/ht-objecoes` para as respostas quando o lead hesitar."
