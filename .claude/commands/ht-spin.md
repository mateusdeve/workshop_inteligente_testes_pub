---
name: workshop-marketing:ht-spin
description: Criar roteiro completo de call SPIN Selling para venda high ticket 1:1 — perguntas de Situação, Problema, Implicação e Necessidade adaptadas para o produto e público do C10X.
---

# HT — SPIN Selling (Call de Vendas 1:1)

Cria o roteiro completo de call de vendas 1:1 usando SPIN Selling adaptado para high ticket.

## Usage

```
/c10x-spin
```

## O Que Fazer

### 1. Contexto
Leia `produtos/.ativo`, depois `produtos/{ativo}/perfil.md` e `produtos/{ativo}/idconsumidor.md`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Produto e Preço:**
```
Qual o produto e o investimento que vai oferecer nessa call?
(ex: "Mentoria de marketing digital por 3 meses — R$5.000")
```

```
--- Bloco 1/3 concluído ---
Produto: [nome] | R$ [valor]
Próximo: Canal da call
---
```

**Bloco 2/3 — Canal:**
```
Como essa call acontece?

1. Videochamada (Google Meet, Zoom)
2. Call de voz (WhatsApp, telefone)
3. Presencial

Digite o número:
```

```
--- Bloco 2/3 concluído ---
Produto: [nome] | R$ [valor]
Canal: [tipo]
Próximo: Origem do lead
---
```

**Bloco 3/3 — Origem do Lead:**
```
Como esse lead chegou até você?

1. Participou do evento (retiro/webinar)
2. Cadastro em isca digital
3. Indicação de cliente
4. Anúncio direto para WhatsApp
5. Seguidor nas redes sociais

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo:
- Produto: [nome] | R$ [valor]
- Canal: [tipo]
- Origem: [como chegou]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**ROTEIRO DE CALL SPIN SELLING — C10X**

---

**ABERTURA (2-3 min)**

Objetivo: criar rapport e definir a estrutura da call.

Script:
"Olá, [NOME]. Obrigado por separar esse tempo. A call de hoje tem [DURAÇÃO] — vou te fazer algumas perguntas para entender melhor o seu momento, e aí te mostro se faz sentido a gente trabalhar juntos. Pode ser assim?"

Aguarde confirmação antes de continuar.

---

**S — SITUAÇÃO (5-8 min)**

Objetivo: mapear o cenário atual sem julgamento.

Perguntas:
1. "Como está seu [negócio/área] hoje? Me conta um pouco do seu momento."
2. "O que você faz atualmente para [resultado que busca]?"
3. "Há quanto tempo você está nesse mercado / trabalhando com isso?"
4. "Qual é o seu faturamento atual, mais ou menos? [contextualize: 'para eu entender o ponto de partida']"
5. "Você tem equipe ou trabalha sozinho?"

Dica: anote as respostas. Elas viram argumentos no fechamento.

---

**P — PROBLEMA (5-8 min)**

Objetivo: identificar a dor principal e fazer o lead verbalizá-la.

Perguntas:
1. "O que está te impedindo de [resultado que quer]?"
2. "Qual a sua maior dificuldade hoje com [área]?"
3. "O que você já tentou para resolver isso? Como foi?"
4. "O que acontece quando você tenta [ação específica]?"

Dica: não interrompa. Quanto mais o lead fala da própria dor, mais próximo está de comprar.

---

**I — IMPLICAÇÃO (5-8 min)**

Objetivo: amplificar o custo de não resolver. Não é manipulação — é fazer o lead enxergar o que já existe.

Perguntas:
1. "O que acontece se esse problema continuar por mais 6 meses?"
2. "Quanto você acha que está perdendo por não ter isso resolvido?"
3. "Como isso afeta [outra área da vida/negócio]?"
4. "Se isso não mudar, onde você vai estar daqui a 1 ano?"

Dica: faça silêncio após a pergunta. Deixe o lead chegar nas conclusões.

---

**N — NECESSIDADE DE SOLUÇÃO (3-5 min)**

Objetivo: criar visão do resultado ideal e preparar terreno para a oferta.

Perguntas:
1. "Como seria a sua vida/negócio se isso estivesse resolvido?"
2. "O que mudaria para você se em [PRAZO] você conseguisse [RESULTADO]?"
3. "O que é mais importante para você nesse processo: [opção A] ou [opção B]?"

Dica: a resposta a essas perguntas vira o gancho do fechamento.

---

**TRANSIÇÃO PARA A OFERTA (1-2 min)**

Script:
"[NOME], baseado em tudo que você me contou — [resumo das dores em 2-3 frases] — eu tenho clareza do que você precisa.

Posso te apresentar como a gente pode trabalhar juntos?"

Aguarde o "sim" antes de continuar.

---

**APRESENTAÇÃO DA SOLUÇÃO (5-8 min)**

Conexão dor-solução:
"O [NOME DO PROGRAMA] foi criado exatamente para quem está na sua situação. Em [PRAZO], você vai [QUADRO].

Você recebe: [entregáveis em 3-4 bullets]."

Ancoragem:
"Hoje, para ter acesso a tudo isso separado, você precisaria de [valor comparativo]. O investimento no [PROGRAMA] é de [PREÇO]."

---

**FECHAMENTO (2-3 min)**

Script padrão C10X:
"[NOME], o investimento é de [VALOR]. Acessível?"

[Pausa — aguarde resposta]

Se sim: "Ótimo. Vou te enviar o link de pagamento agora. Me confirma quando finalizar que já libero seus acessos."

Se objeção: acesse `/ht-objecoes` para o script de resposta específico.

---

**REGRAS DA CALL:**
- Nunca pergunte "quer comprar?" — assuma o interesse
- Nunca explique o preço antes de apresentar o valor
- Nunca reduza o preço sem antes esgotar as respostas de objeção
- O silêncio após o preço é parte do script — não quebre antes do lead

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`produtos/{ativo}/entregas/c10x/spin-[produto].md`

### 6. Próximo Passo
"SPIN pronto. Próximo: `/ht-objecoes` para as respostas de quebra de objeção, ou `/ht-whatsapp` para o fluxo de vendas por mensagem."
