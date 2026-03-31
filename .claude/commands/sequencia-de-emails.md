---
name: workshop-marketing:sequencia-de-emails
description: Criar sequências completas de email para pico de vendas, lançamento, nutrição e carrinho aberto. Baseado na estrutura de Pico de Vendas do VTSD.
---

# Sequência de Emails — Pico de Vendas (VTSD)

Cria sequências de email seguindo a estrutura de Pico de Vendas do VTSD.

## Usage

```
/sequencia-de-emails
```

## O Que Fazer

### 1. Contexto
Leia `produtos/{ativo}/perfil.md`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Tipo de Sequência:**

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

**Bloco 2/3 — Contexto:**

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

**Bloco 3/3 — Duração:**

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

**Pico de Vendas (VTSD — sequência completa):**

Fase 1 — Convite (pré-evento):
- Email 1: Convite principal
- Email 2: Reforço com curiosidade
- Email 3: Urgência (vagas limitadas)

Fase 2 — Confirmação (pós-cadastro):
- Email 1: Confirmação + próximos passos
- Email 2: Preparação + expectativa

Fase 3 — Lembrete (dia do evento):
- Email 1: Lembrete manhã
- Email 2: Lembrete 1h antes
- Email 3: "Começou agora"

Fase 4 — Pré-abertura:
- Email 1: Bastidores da oferta
- Email 2: Antecipação de bônus

Fase 5 — Carrinho aberto:
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

**Regras de estilo Light Copy — obrigatórias em todos os emails:**
- Sem ponto de exclamação.
- Sem perguntas no gancho.
- Sem "mesmo que" / "sem precisar" como muletas.
- Sem promessas vagas.
- Travessão longo (—): nunca usar. Substituir por vírgula, ponto ou reformulação.
- Estrutura "Não é X. É Y.": nunca usar. Reformular de forma mais elaborada.
- Emojis: nunca usar.
- O produto não aparece nas primeiras linhas do email: começar pelo contexto do leitor.
- Frases genéricas: "Transforme sua vida", "Método revolucionário", "Isso pode mudar tudo."
- Nomear cria realidade: criar nome próprio para o conceito ou problema quando possível.
- Especificidade: usar números concretos, situações reais. "3 dias sem dormir" > "noites difíceis".

**Checklist obrigatório — revisar antes de entregar qualquer email:**

Antes de entregar, revise e substitua:
- Travessão (—) → reescreva a frase sem ele
- Estrutura "Não é X. É Y." → desenvolva o argumento de outra forma
- Frases genéricas de vendedor → substitua por dado ou situação concreta
- Menção ao produto nas primeiras linhas → remova ou reescreva focando no leitor
- Emojis → remova sem substituição

- [ ] Nenhum travessão no texto
- [ ] Nenhuma estrutura "Não é X. É Y."
- [ ] Nenhuma frase genérica de vendedor

### 4. Salvar
`produtos/{ativo}/entregas/emails/sequencia-[tipo]-[produto].md`

### 5. Próximo Passo
"Sequência salva. Use `/pagina-de-vendas` para criar a página do evento, ou `/anuncio` para criar anúncios de divulgação."
