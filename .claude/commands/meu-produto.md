---
name: workshop-marketing:meu-produto
description: Cadastrar produto/negócio do aluno com Quadro, Furadeira, Decorados e 3 Identidades da metodologia VTSD.
---

# Meu Produto — Cadastro Completo do Negócio

Cadastre as informações do produto usando a metodologia VTSD (Quadro, Furadeira, Decorados, 3 Identidades).

## Usage

```
/meu-produto
```

## O Que Fazer

### 1. Verificar perfil existente
Leia `meu-negocio/perfil.md`. Se existir, mostre resumo e pergunte se quer atualizar.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/6 — Quadro (Transformação Principal):**

Pergunta 1:
```
Qual é o seu produto ou serviço? Me conte em poucas palavras o que você vende.
(ex: "curso de inglês online", "mentoria para emagrecimento", "ebook de receitas fit")
```

Pergunta 2:
```
Qual é a transformação principal que seu aluno/cliente alcança?
O resultado que ele "pendura na parede".
(ex: "Falar inglês fluente", "Emagrecer 10kg", "Faturar R$10 mil/mês")
```

Após as respostas, gere 5 opções de Quadro e apresente numeradas:
```
Escolha o Quadro que melhor representa seu produto:

1. Falar inglês fluente em 90 dias
2. Dominar o inglês sem sair de casa
3. Conquistar fluência em inglês do zero
4. Destravar o inglês em 3 meses
5. Alcançar fluência real em inglês

Digite o número (ou descreva outro):
```

Regras do Quadro: até 10 palavras, verbo no infinitivo, único resultado, específico e tangível.

```
--- Bloco 1/6 concluído ---
Quadro: [quadro escolhido]
Próximo: Furadeira (Método)
---
```

**Bloco 2/6 — Furadeira (Método):**

Pergunta 3:
```
Como você ensina seu aluno a alcançar esse resultado?
Quais são as grandes fases do processo?
(ex: "Primeiro trabalho a base, depois conversação, depois fluência")
```

Monte a Furadeira e apresente:
- 3-5 Macroetapas (grandes fases)
- Microetapas em cada fase
- Nome memorável para o método

```
--- Bloco 2/6 concluído ---
Quadro: [quadro]
Furadeira: [nome do método] ([X] macroetapas)
Próximo: Identidades
---
```

**Bloco 3/6 — Identidades:**

Pergunta 4:
```
Quem é seu público-alvo? Descreva quem são essas pessoas.
(ex: "Mulheres 25-40 anos que querem mudar de carreira")
```

Pergunta 5:
```
Qual o formato e preço do produto?

1. Curso online
2. Mentoria/consultoria
3. E-book/guia
4. Comunidade
5. Outro

Preço: R$ ___
```

Pergunta 6:
```
O que torna seu produto diferente dos concorrentes?
(ex: "Método prático sem gramática", "Acompanhamento individual")
```

```
--- Bloco 3/6 concluído ---
Quadro: [quadro]
Furadeira: [método]
Público: [público]
Formato: [formato] | Preço: [preço]
Próximo: Decorados
---
```

**Bloco 4/6 — Decorados:**

Pergunta 7:
```
Quais benefícios indiretos seus alunos conseguem além do resultado principal?
(ex: "mais confiança", "promoção no trabalho", "viagens sem medo")
```

A partir da resposta, gere 50 Decorados em 5 categorias: Financeiro, Tempo, Autoestima, Reputação, Crescimento.

```
--- Bloco 4/6 concluído ---
Decorados: [X] benefícios gerados
Próximo: Urgências Ocultas
---
```

**Bloco 5/6 — Urgências Ocultas:**

Pergunta 8:
```
Quais são as maiores frustrações e dores do seu público? O que tira o sono deles?
(ex: "vergonha de falar em reunião", "medo de perder oportunidade")
```

Pergunta 9:
```
O que essas pessoas mais desejam? Qual o sonho delas?
(ex: "ser promovido", "viajar sem depender de ninguém")
```

Pergunta 10:
```
Quais dúvidas elas têm sobre o tema? O que perguntam no Google ou nos comentários?
(ex: "quanto tempo leva pra ficar fluente?", "preciso morar fora?")
```

Pergunta 11:
```
Que assuntos relacionados interessam esse público além do seu tema principal?
(ex: "produtividade", "carreira internacional", "intercâmbio")
```

A partir das respostas, gere as Urgências Ocultas completas:
- **Dores:** 10+ dores específicas (não genéricas)
- **Desejos:** 10+ desejos concretos
- **Dúvidas:** 10+ dúvidas reais que o público faz
- **Assuntos Relacionados:** 10+ temas adjacentes que interessam o público

Valide com o aluno e ajuste conforme feedback.

```
--- Bloco 5/6 concluído ---
Urgências Ocultas: [X] dores, [X] desejos, [X] dúvidas, [X] assuntos
Próximo: Argumentos Incontestáveis
---
```

**Bloco 6/6 — Argumentos Incontestáveis (opcional):**

Pergunta 12:
```
Você tem dados, pesquisas ou estatísticas que comprovam a eficácia do seu método?
(ex: "450 alunos formados", "92% alcançam fluência em 90 dias", "método baseado em pesquisa de Harvard")

1. Sim, tenho dados
2. Não tenho ainda (pular)

Digite o número:
```

### 3. Confirmação

Apresente resumo completo com opções:
```
Resumo do seu produto:

- Quadro: [quadro]
- Método: [nome] ([X] macroetapas)
- Público: [descrição]
- Formato: [formato] | Preço: R$ [preço]
- Diferencial: [diferencial]
- Decorados: [X] benefícios
- Urgências Ocultas: [X] dores, [X] desejos, [X] dúvidas, [X] assuntos
- Argumentos: [dados ou "nenhum"]

1. Tudo certo, pode salvar
2. Quero ajustar algo
```

### 4. Salvar Perfil
Salve em `meu-negocio/perfil.md`:

```markdown
# Perfil do Negócio

## Quadro (Transformação Principal)
[Quadro escolhido]

## Furadeira (Método)
**Nome do Método:** [nome]
1. **[Macroetapa 1]** — [microetapas]
2. **[Macroetapa 2]** — [microetapas]
3. **[Macroetapa 3]** — [microetapas]

## Identidade do Produto
- **Nome:** [nome]
- **Formato:** [curso, mentoria, etc.]
- **Preço:** [preço]
- **Diferencial:** [o que torna único]

## Identidade do Consumidor
- **Público-alvo:** [descrição]
- **Nicho:** [nicho]
- **Nível de consciência:** [inconsciente/consciente do problema/consciente da solução]

## Identidade do Comunicador
- **Tom de voz:** [a definir com base nas respostas]
- **Posicionamento:** [a definir]

## Decorados (Benefícios)
- [lista de benefícios diretos e indiretos]

## Argumentos Incontestáveis
- [dados, pesquisas, estatísticas, números de resultado]

## Urgências Ocultas

### Dores (o que incomoda)
- [10+ dores específicas]

### Desejos (o que sonha)
- [10+ desejos concretos]

### Dúvidas (o que pergunta)
- [10+ dúvidas reais]

### Assuntos Relacionados (o que interessa)
- [10+ temas adjacentes]
```

### 5. Próximo Passo
"Perfil salvo. Agora use `/persona` para detalhar o perfil do seu cliente ideal, ou `/pagina-de-vendas` se quiser ir direto para a página."
