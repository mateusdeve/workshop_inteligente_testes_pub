---
name: workshop-marketing:ht-apresentacao-proposta
description: Criar script da call de apresentação de proposta comercial C10X. como conduzir a reunião de apresentação, percorrer a proposta, quebrar objeções e fechar no final da call.
---

# HT. Script de Apresentação de Proposta

Cria o roteiro da call onde você apresenta a proposta comercial e fecha a consultoria.

## Usage

```
/c10x-apresentacao-proposta
```

## O Que Fazer

### 1. Contexto
Leia `entregas/.ativo`, depois `entregas/{ativo}/perfil.md`.
Se existir `entregas/{ativo}/c10x/proposta-*.md`, leia para usar os detalhes da proposta.

### 2. Entrevista (UMA pergunta por vez)

**Bloco 1/2. Investimento:**
```
Qual o investimento da proposta?
(ex: "R$8.000 à vista ou R$4.500 + R$4.500 em 30 dias")
```

**Bloco 2/2. Principal Objeção Esperada:**
```
Qual a maior objeção que você espera nessa call?

1. Preço
2. Prazo / timing
3. Dúvida sobre o resultado
4. Precisa consultar alguém
5. Outra

Digite o número:
```

**Confirmação antes de gerar:**
```
Investimento: R$ [valor]
Objeção esperada: [tipo]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**SCRIPT DE APRESENTAÇÃO DE PROPOSTA. C10X**

---

**ABERTURA (2-3 min)**

Objetivo: criar o ambiente certo. formal o suficiente para mostrar preparo, humano o suficiente para manter o rapport.

Script:
"[NOME], obrigado por separar esse tempo. Desde nossa última conversa, fiz uma análise cuidadosa do que você me trouxe e montei algo que acredito que faz muito sentido para o seu momento.

Vou te apresentar a proposta agora. Enquanto eu falo, anota qualquer dúvida que tiver. vou reservar tempo no final para responder tudo."

---

**RECAPITULAÇÃO DO DIAGNÓSTICO (3-5 min)**

Objetivo: mostrar que você entendeu o problema. essa é a parte mais importante da call.

Script:
"Antes de mostrar a proposta, quero confirmar meu entendimento do seu caso.

Na nossa conversa, você me disse que [RESUMO DO PROBLEMA NAS PALAVRAS DELE]. Isso está gerando [IMPACTO]. você chegou a mencionar que isso está custando aproximadamente [VALOR] por mês.

O que você quer alcançar é [RESULTADO QUE ELE DESCREVEU].

Está correto isso?"

[Aguarde confirmação. Se ele corrigir algo, anote. A proposta pode precisar de ajuste.]

---

**APRESENTAÇÃO DA SOLUÇÃO (5-7 min)**

Percorra a proposta em ordem:

"Baseado nisso, o que proponho é [NOME DO PROJETO/CONSULTORIA].

A lógica é simples: [EXPLICAÇÃO DA ABORDAGEM EM 2-3 frases].

Você vai receber: [ENTREGÁVEIS. 1 de cada vez, com o benefício de cada um]

O prazo é de [PRAZO], e comeríamos na semana de [DATA]."

---

**ANCORAGEM DE VALOR (2-3 min)**

"Antes do investimento, quero te mostrar o que isso vale em perspectiva.

O problema que você me descreveu está custando [CUSTO DO PROBLEMA] por mês. Em [X meses], são [CUSTO ACUMULADO].

O investimento para resolver isso de vez é de [PREÇO]."

---

**APRESENTAÇÃO DO PREÇO E SILÊNCIO (1 min)**

"O investimento total é R$ [VALOR].

Temos [OPÇÃO DE PAGAMENTO 1] ou [OPÇÃO DE PAGAMENTO 2]."

[Pare. Espere ele falar. Não preencha o silêncio.]

---

**RESPOSTA PARA OBJEÇÕES (conforme necessário)**

[Preço:]
"Entendo. Você consegue me dizer com que está comparando? Porque [ARGUMENTO DE VALOR]."

[Timing:]
"O que precisa acontecer para ser o momento certo? Porque [PROBLEMA] vai continuar existindo enquanto você espera."

[Precisa consultar alguém:]
"Faz sentido. O que você acha que [PESSOA] vai perguntar? Talvez eu consiga te dar as respostas agora."

---

**FECHAMENTO (1-2 min)**

Quando o cliente sinaliza positivamente:

"Ótimo. Para iniciarmos, preciso de: [PRÓXIMOS PASSOS. contrato / pagamento / data de início].

Posso te enviar o contrato ainda hoje?"

---

**SE A CALL NÃO FECHAR:**

Script para encerrar sem perder o cliente:
"Entendo. Fica à vontade para pensar. Se tiver qualquer dúvida, estou disponível.

A proposta é válida até [DATA]. Depois disso, posso não ter agenda disponível no prazo que você precisa."

[Agende um follow-up explícito:]
"Posso te contatar [DATA. 2 dias depois] para saber se surgiu alguma dúvida?"

---

**REGRAS DA CALL DE APRESENTAÇÃO:**
- Comece pelo diagnóstico, não pela proposta. mostre que entendeu antes de mostrar o que faz
- Nunca peça desculpa pelo preço
- Nunca ofereça desconto antes que o cliente peça
- Se o cliente hesitar, não force. pergunte o que está pesando
- Termine toda call com um próximo passo definido (sim ou follow-up com data)

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`entregas/{ativo}/c10x/apresentacao-proposta.md`

### 6. Próximo Passo
"Script pronto. Se fechar, próximo: `/ht-onboarding` para preparar a entrada do cliente."
