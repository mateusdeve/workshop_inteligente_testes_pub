---
name: workshop-marketing:ht-oferta
description: Estruturar a oferta completa de um produto High Ticket C10X. entregáveis, bônus, preço, ancoragem de valor e garantia. Usada após definir a Big Idea.
---

# HT. Oferta High Ticket

Monta a estrutura completa da oferta do produto high ticket: o que o aluno recebe, bônus estratégicos, preço e garantia.

## Usage

```
/c10x-oferta
```

## O Que Fazer

### 1. Contexto
Leia `entregas/.ativo`, depois `entregas/{ativo}/perfil.md` e `entregas/{ativo}/idconsumidor.md`.
Se existir `entregas/{ativo}/c10x/big-idea-*.md`, leia também para usar a transformação já definida.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4. Formato da Oferta:**
```
O que você está vendendo no evento?

1. Mentoria em grupo (acesso a sessões periódicas)
2. Mentoria individual (acompanhamento 1:1)
3. Consultoria por projeto (entrega de resultado específico)
4. Programa completo (curso + acompanhamento + comunidade)
5. Retiro presencial ou imersão ao vivo

Digite o número:
```

```
--- Bloco 1/4 concluído ---
Formato: [tipo]
Próximo: Entregáveis
---
```

**Bloco 2/4. Entregáveis Principais:**
```
O que o aluno/cliente recebe ao entrar?
Liste tudo que vem com a oferta principal.
(ex: "12 encontros ao vivo, gravações, material de apoio, grupo exclusivo")
```

```
--- Bloco 2/4 concluído ---
Formato: [tipo]
Entregáveis: [lista]
Próximo: Preço e prazo
---
```

**Bloco 3/4. Preço e Prazo:**
```
Qual o investimento e a duração do programa?
(ex: "R$5.000 à vista ou 12x R$497, programa de 3 meses")
```

```
--- Bloco 3/4 concluído ---
Formato: [tipo]
Entregáveis: [lista]
Investimento: R$ [valor] | Duração: [prazo]
Próximo: Objeções principais
---
```

**Bloco 4/4. Objeções Principais:**
```
Quais as 2 maiores objeções do seu público antes de comprar?
(ex: "está caro" e "não tenho tempo")
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Formato: [tipo de oferta]
- Entregáveis: [lista resumida]
- Investimento: R$ [valor] | [prazo]
- Objeções a resolver: [objeções]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**Estrutura Completa da Oferta C10X:**

**1. Linha de Transformação**
Uma frase que resume o resultado em palavras simples.
Formato: "Em [PRAZO], você [RESULTADO] com [MÉTODO]."

**2. Entregáveis Categorizados**
Organize os entregáveis em categorias com descrição persuasiva (Light Copy):
- Encontros/Sessões ao vivo
- Materiais e recursos
- Acesso e suporte
- Bônus (mínimo 3)

Para cada entregável, escreva:
- Nome do entregável
- O que é (1 linha)
- Para que serve (benefício direto. decorado)

**3. Bônus Estratégicos (3 bônus)**

Cada bônus deve:
- Resolver uma objeção específica
- Complementar o entregável principal
- Ter nome próprio
- Ter valor atribuído

Formato de cada bônus:
```
Bônus [N]: [Nome do Bônus]
O que é: [descrição em 1 linha]
Resolve: [objeção que quebra]
Valor: R$ [X]
```

**4. Ancoragem de Valor**

Compare o investimento com:
- Custo de NÃO resolver o problema (perda financeira/tempo)
- Alternativas do mercado (agência, consultor avulso, cursos)
- Valor total dos entregáveis individualmente

Formato:
"Individualmente, cada parte valeria: [lista com valores]. Total: R$ [X]. Você investe apenas R$ [preço real]."

**5. Garantia**

Escolha o tipo mais adequado ao contexto:

Opção A. Garantia Incondicional:
"Se em [X dias] você não estiver satisfeito, devolvo 100% do investimento. Sem perguntas."

Opção B. Garantia de Resultado:
"Se você implementar o método e não [resultado específico], analiso seu caso pessoalmente e ficamos juntos até funcionar."

Opção C. Garantia Dupla (recomendada para high ticket):
"[Incondicional em X dias] + [Resultado com suporte estendido]."

**6. Resumo da Oferta (para o pitch)**

Bloco de fechamento em formato de script:
"Você recebe [entregável 1], [entregável 2], [entregável 3], mais os bônus [B1], [B2] e [B3], com [garantia]. Tudo isso por R$ [preço]."

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`entregas/{ativo}/c10x/oferta-[produto].md`

### 6. Próximo Passo
"Oferta estruturada. Próximo passo: `/ht-cronograma` para montar a agenda do evento, ou `/ht-pagina-inscricao` para criar a página de captação."
