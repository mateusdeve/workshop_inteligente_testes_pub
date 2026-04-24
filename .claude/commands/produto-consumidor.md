---
name: workshop-marketing:produto-consumidor
description: Comando obsoleto. A identidade do consumidor e o Painel de Entregas agora são gerados automaticamente pelo /produto-concepcao.
---

# Identidade do Consumidor (fluxo unificado em /produto-concepcao)

Este comando foi desativado. O fluxo de identidade do consumidor (dados demográficos, paliativos, objeções pelo Framework dos 7 Argumentos, baldes e geração do `idconsumidor.md`) e a geração do `painel-entregas.html` agora rodam automaticamente dentro de `/produto-concepcao`, logo após o perfil ser salvo.

## Usage

```
/produto-consumidor
```

## O Que Fazer

Responda ao usuário, sem executar nada:

```
Este fluxo agora é automático dentro da Concepção do Produto.

Rode /produto-concepcao. A identidade do consumidor e o Painel de Entregas
são gerados automaticamente ao final da concepção, sem precisar de comando
separado.

Se o perfil já estiver salvo e só faltar regerar a identidade do consumidor
ou o painel, rode /produto-concepcao e escolha a opção de refazer aquela
parte quando ele perguntar.
```

Não crie pastas, não escreva arquivos, não faça perguntas. Apenas direcione o aluno para `/produto-concepcao` e encerre.
