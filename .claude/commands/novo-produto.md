---
name: workshop-marketing:novo-produto
description: Criar um novo produto/projeto e defini-lo como produto ativo.
---

# Novo Produto — Criar e Ativar

Cria uma nova pasta de produto dentro de `produtos/` e a define como produto ativo.

## Usage

```
/novo-produto
```

## O Que Fazer

### 1. Perguntar o nome do produto

```
Qual o nome deste produto?
(ex: "Curso de Inglês Fluente", "Mentoria Fitness Online", "Tarô para Iniciantes")
```

### 2. Perguntar o tipo do produto

Logo após receber o nome, pergunte:

```
Que tipo de produto é este?

1. Low Ticket (R$7 a R$97 — quiz, desafio, mini-curso, agente GPT)
2. Middle Ticket (R$97 a R$997 — curso online, workshop, grupo)

Digite o número:
```

Guarde o tipo escolhido. Ele será salvo no arquivo `produtos/{slug}/tipo.md`.

### 3. Gerar slug automaticamente

Com o nome fornecido, gere um slug em kebab-case (letras minúsculas, sem acentos, palavras separadas por hífen).

Exemplos:
- "Curso de Inglês Fluente" → `curso-ingles-fluente`
- "Mentoria Fitness Online" → `mentoria-fitness-online`
- "Tarô para Iniciantes" → `taro-para-iniciantes`

Apresente para confirmação:
```
Vou criar o produto com o identificador: curso-ingles-fluente

1. Confirmar
2. Quero usar outro nome
```

### 3. Verificar se já existe

Verifique se já existe uma pasta `produtos/{slug}/`. Se existir, informe:
```
Já existe um produto com esse identificador. Quer usar /trocar-produto para acessá-lo?
```

### 4. Criar estrutura de pastas

Crie as seguintes pastas:
```
produtos/{slug}/
produtos/{slug}/entregas/
produtos/{slug}/entregas/paginas/
produtos/{slug}/entregas/anuncios/
produtos/{slug}/entregas/emails/
produtos/{slug}/entregas/copy-pagina/
produtos/{slug}/entregas/conteudo-social/
produtos/{slug}/entregas/criativos/
produtos/{slug}/entregas/comercial/
produtos/{slug}/entregas/textos-de-venda/
```

### 5. Definir como produto ativo

Salve o slug em `produtos/.ativo` (sobrescreva o conteúdo anterior).

### 6. Salvar o tipo do produto

Salve o tipo escolhido em `produtos/{slug}/tipo.md` com o seguinte conteúdo:

```
Low Ticket
```

ou

```
Middle Ticket
```

### 7. Confirmar e sugerir próximo passo

```
Produto "{nome}" criado e ativado.
Identificador: {slug}
Tipo: {tipo}

Agora use /meu-produto para cadastrar o Quadro, Furadeira, Decorados e as 3 Identidades deste produto.
```
