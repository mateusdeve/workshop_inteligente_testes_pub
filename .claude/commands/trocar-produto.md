---
name: workshop-marketing:trocar-produto
description: Listar os produtos cadastrados e trocar o produto ativo.
---

# Trocar Produto — Selecionar Produto Ativo

Lista todos os produtos cadastrados em `produtos/` e permite trocar o produto ativo.

## Usage

```
/trocar-produto
```

## O Que Fazer

### 1. Ler produto ativo atual

Leia `produtos/.ativo` para saber qual produto está ativo agora.

### 2. Listar produtos disponíveis

Liste todas as subpastas dentro de `produtos/` (ignorar arquivos como `.ativo` e `.gitkeep`).

Para cada pasta, verifique se existe `produtos/{slug}/perfil.md` e mostre:
- Nome do produto (leia a linha do Quadro do `perfil.md` se existir, senão mostre só o slug)
- Indicador se é o produto ativo atual

Exemplo de listagem:
```
Seus produtos cadastrados:

1. curso-tarot — "Fazer leituras de tarô seguras para si e outros" ← ATIVO
2. mentoria-fitness — "Emagrecer 10kg sem academia em 60 dias"
3. curso-ingles — (sem perfil cadastrado ainda)

Digite o número do produto que quer ativar, ou 0 para cancelar:
```

### 3. Se não houver produtos

Se `produtos/` estiver vazio (só tem `.ativo` ou está vazia), informe:
```
Você ainda não tem produtos cadastrados.
Use /novo-produto para criar seu primeiro produto.
```

### 4. Ativar o produto escolhido

Após o aluno digitar o número:
- Salve o slug correspondente em `produtos/.ativo` (sobrescreva)
- Confirme:

```
Produto ativado: {nome/slug}
Todos os próximos comandos usarão este produto.

Quer continuar com /meu-produto para editar o perfil, ou já ir para /pagina-de-vendas?
```

### 5. Se o produto escolhido não tiver perfil

Se `produtos/{slug}/perfil.md` não existir:
```
Este produto ainda não tem perfil cadastrado.
Use /meu-produto para cadastrar o Quadro, Furadeira e as 3 Identidades.
```
