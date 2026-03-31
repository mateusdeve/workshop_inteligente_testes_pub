---
name: workshop-marketing:ht-follow-up
description: Criar sequência de follow-up pós-evento C10X para quem participou mas não comprou — mensagens D+1, D+3 e D+7 com abordagens diferentes (prova social, urgência, downsell).
---

# HT — Follow-Up Pós-Evento

Cria a sequência de follow-up para participantes que assistiram ao evento mas não compraram durante o pitch.

## Usage

```
/c10x-follow-up
```

## O Que Fazer

### 1. Contexto
Leia `produtos/.ativo`, depois `produtos/{ativo}/perfil.md`.

### 2. Entrevista (UMA pergunta por vez)

**Bloco 1/3 — Produto e Prazo:**
```
Qual o produto vendido no evento e até quando as vagas estão abertas?
(ex: "Mentoria de 3 meses — vagas abertas por 5 dias após o evento")
```

**Bloco 2/3 — Tem Downsell:**
```
Tem alguma oferta menor para quem não comprar o produto principal?
(ex: "Sim, tenho um curso gravado por R$297", "Não tenho")
```

**Bloco 3/3 — Canal:**
```
O follow-up vai ser por:

1. WhatsApp (recomendado — maior taxa de resposta)
2. Email
3. Ambos

Digite o número:
```

**Confirmação antes de gerar:**
```
Produto: [nome] | Prazo: [dias]
Downsell: [sim/não]
Canal: [WhatsApp/Email/ambos]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**SEQUÊNCIA DE FOLLOW-UP PÓS-EVENTO**

---

**D+1 — PROVA SOCIAL**

Objetivo: mostrar que outras pessoas já decidiram e reforçar a transformação prometida.

WhatsApp:
"[NOME], ontem no [NOME DO EVENTO] você viu [RESUMO DO QUE APRENDEU].

Desde ontem, [X] pessoas já garantiram suas vagas no [NOME DO PROGRAMA].

Você está considerando?"

Email:
Assunto: O que aconteceu depois do [NOME DO EVENTO]

Corpo: Mencione 1 resultado rápido de quem já entrou (se possível), reforce a promessa principal e inclua o link com CTA suave.

---

**D+3 — ARGUMENTO E OBJEÇÃO**

Objetivo: abordar a objeção mais comum sem que o lead precise trazer.

WhatsApp:
"[NOME], me lembro que no evento você estava interessado em [TEMA/DOR].

A maior dúvida que as pessoas têm antes de entrar é [OBJEÇÃO MAIS COMUM]. Posso te explicar como funciona?"

[Se ele responder:]
"[RESPOSTA PARA A OBJEÇÃO]

As vagas fecham em [DATA]. Quer garantir a sua?"

Email:
Assunto: A dúvida que quase todo mundo tem antes de entrar

Corpo: Aborde a objeção principal + história de aluno que tinha a mesma dúvida + resultado + CTA com urgência.

---

**D+5 — URGÊNCIA**

Objetivo: criar urgência real baseada em escassez ou prazo.

WhatsApp:
"[NOME], as inscrições para o [NOME DO PROGRAMA] fecham [AMANHÃ / EM X HORAS].

Depois disso, [CONSEQUÊNCIA REAL: vagas encerradas / preço sobe / bônus sai].

Você quer garantir agora? [LINK]"

Email:
Assunto: Último dia

Corpo: Curto e direto. Lembrete do prazo + o que perde quem não entrar + link + CTA urgente.

---

**D+7 — ÚLTIMA MENSAGEM / DOWNSELL**

Objetivo: fechar com dignidade. Se tiver downsell, oferecer. Se não, encerrar.

[COM DOWNSELL:]

WhatsApp:
"[NOME], as vagas do [PROGRAMA PRINCIPAL] foram encerradas.

Mas se você ainda quer dar o primeiro passo, tenho uma opção para quem não está pronto para o programa completo ainda: [NOME DO DOWNSELL] por [PREÇO]. É [DESCRIÇÃO EM 1 LINHA].

Se quiser, me fala."

[SEM DOWNSELL:]

WhatsApp:
"[NOME], as vagas do [PROGRAMA] foram preenchidas.

Quando abrir a próxima turma, você é o primeiro que vou avisar. Pode ser?"

---

**REGRAS DO FOLLOW-UP:**
- Máximo 1 mensagem por dia — não sobrecarregue
- Nunca diga "só vim verificar" — sempre traga algo de valor ou urgência concreta
- Se o lead pedir para não ser mais contatado, respeite imediatamente
- Após D+7, encerrar o ciclo de follow-up desse evento

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`produtos/{ativo}/entregas/c10x/follow-up-[evento].md`

### 6. Próximo Passo
"Follow-up pronto. Se vai trabalhar com consultoria também, próximo: `/ht-diagnostico` para a call de descoberta."
