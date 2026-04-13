---
name: workshop-marketing:furadeira-visual
description: Gera a Furadeira (método VTSD) como diagrama visual em HTML estatico pronto para virar imagem. 5 layouts (linear, roadmap, piramide, hub, fluxograma) com conversao automatica para PNG.
---

# Furadeira Visual. Diagrama do Método como Imagem

Gera a Furadeira do produto ativo como visual em HTML estático com dimensões fixas, depois converte automaticamente para PNG via Edge headless. Resolve o problema de diagramas nativos da IA ficarem ruins.

## Usage

```
/furadeira-visual
```

## O Que Fazer

Invoque a skill `furadeira-visual` do plugin workshop-marketing. Ela faz todo o fluxo:

1. Lê `entregas/.ativo` e `entregas/{ativo}/perfil.md` para pegar Quadro, nome do método e macroetapas.
2. Pergunta o estilo visual (linear horizontal, roadmap vertical, pirâmide invertida, hub central, fluxograma condicional).
3. Pergunta formato (1080x1080, 1080x1920, 1920x1080, 1200x630).
4. Pergunta paleta de cores (amarelo handwritten, azul, roxo, verde, rosa ou hex personalizado).
5. Pergunta se inclui cabeçalho (nome do método + Quadro).
6. Confirma o resumo, gera o HTML, salva em `entregas/{ativo}/furadeira/`.
7. Tenta converter automaticamente para PNG via Edge headless. Se falhar, instrui o usuário a abrir e fazer print.
8. Sugere próximo passo (ex: colocar a furadeira na seção "Método" da página de vendas).

## Pré-Requisitos

- Produto ativo cadastrado (`/produto-novo` ou `/produto-trocar`)
- Furadeira do produto já estruturada com macroetapas nomeadas (`/produto-editar`)

Se faltar alguma coisa, a skill orienta o que fazer antes.

## Quando Usar

- "Quero a furadeira em imagem"
- "Faz um diagrama do método pra eu colocar no Instagram"
- "Gera um visual do método pra página de vendas"
- "Mapa do método", "infográfico do método"

## Onde Salva

`entregas/{ativo}/furadeira/furadeira-{estilo}-{timestamp}.html` e `.png`
