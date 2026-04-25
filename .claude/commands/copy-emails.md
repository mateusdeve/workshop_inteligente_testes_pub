---
name: workshop-marketing:copy-emails
description: Criar sequências completas de email para pico de vendas, lançamento, nutrição e carrinho aberto. Baseado na estrutura de Pico de Vendas do VTSD.
---

# Sequência de Emails. Pico de Vendas (VTSD)

Cria sequências de email seguindo a estrutura de Pico de Vendas do VTSD.

## Usage

```
/copy-emails
```

## O Que Fazer

### 1. Contexto
Leia `meus-produtos/{ativo}/perfil.md`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3. Tipo de Sequência:**

```
Qual tipo de sequência de emails?

1. Pico de vendas (evento + abertura de carrinho)
2. Nutrição (relacionamento para lista fria)
3. Boas-vindas (pós-cadastro em isca digital)
4. Carrinho abandonado (recuperação de vendas)

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Tipo: [tipo escolhido]
Próximo: Contexto
---
```

**Bloco 2/3. Contexto:**

```
Qual o evento ou oferta? Me conte o contexto.
(ex: "Workshop ao vivo dia 15, depois abro carrinho do curso por 5 dias")
```

```
--- Bloco 2/3 concluído ---
Tipo: [tipo]
Contexto: [resumo do contexto]
Próximo: Duração
---
```

**Bloco 3/3. Duração:**

```
Qual a duração da campanha?
(ex: "7 dias de pré-evento + 5 dias de carrinho aberto")
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Tipo: [tipo de sequência]
- Contexto: [evento/oferta]
- Duração: [período]
- Quantidade estimada: [X] emails

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**Pico de Vendas (VTSD. sequência completa):**

Fase 1. Convite (pré-evento):
- Email 1: Convite principal
- Email 2: Reforço com curiosidade
- Email 3: Urgência (vagas limitadas)

Fase 2. Confirmação (pós-cadastro):
- Email 1: Confirmação + próximos passos
- Email 2: Preparação + expectativa

Fase 3. Lembrete (dia do evento):
- Email 1: Lembrete manhã
- Email 2: Lembrete 1h antes
- Email 3: "Começou agora"

Fase 4. Pré-abertura:
- Email 1: Bastidores da oferta
- Email 2: Antecipação de bônus

Fase 5. Carrinho aberto:
- Email 1: Abertura oficial
- Email 2: Prova social
- Email 3: Objeções
- Email 4: Bônus exclusivo
- Email 5: Últimas horas
- Email 6: Última chance

Cada email deve usar Light Copy e incluir:
- Assunto (curto, curioso, sem clickbait)
- Corpo (conversacional, com elementos literários)
- CTA claro

**Regras de estilo Light Copy:**

**Fonte única e obrigatória:** antes de escrever qualquer email, leia `.claude/skills/revisora/references/manual-copy.md`. Princípio central, **15 princípios**, **20 vícios proibidos** e **checklist Blocos A/B/C/D** vivem ali. Toda sequência passa pelo `revisora` antes de chegar ao usuário.

**Reforços específicos de email:**
- **Assunto curto, curioso, sem clickbait:** afirmação ou fragmento de cena, nunca pergunta retórica nem promessa vaga.
- **Produto não aparece nas primeiras linhas:** email começa pelo contexto/cena do leitor. Nome do curso, método ou sigla só depois de estabelecer o argumento.
- **Uma ideia por email:** o email defende UMA tese e leva a UM CTA. Acumular tópicos dilui conversão.
- **Especificidade em tudo:** "3 dias sem dormir" supera "noites difíceis"; "R$ 120 por leitura" supera "cobrar bem".
- **CTA claro e único** por email, coerente com a fase da sequência (convite, lembrete, abertura, objeção, fechamento).

### 4. Salvar
`meus-produtos/{ativo}/entregas/emails/sequencia-[tipo]-[produto].md`

### 5. Próximo Passo
"Sequência salva. Use `/copy-pagina` para criar a página do evento, ou `/copy-anuncio` para criar anúncios de divulgação."
