---
name: workshop-marketing:furadeira-visual
description: Gerar visualização HTML da Furadeira (método do produto) como trilha de aprendizado progressiva, com macroetapas como marcos e microetapas como checkpoints. Salva HTML e tenta capturar PNG.
---

# Furadeira Visual — Gerar Trilha do Método

Gera a representação visual do método do produto ativo como uma trilha de jornada progressiva em HTML, com possibilidade de captura em PNG.

## Usage

```
/furadeira-visual
```

## O Que Fazer

Acionar a skill `furadeira-visual` para executar o fluxo completo:

1. Ler `entregas/.ativo` e `entregas/{ativo}/perfil.md`
2. Extrair: nome do método, Quadro, macroetapas e microetapas
3. Perguntar a paleta de cores preferida (1 pergunta numerada)
4. Gerar HTML da trilha visual com o template da skill
5. Salvar em `entregas/{ativo}/furadeira-visual.html`
6. Tentar capturar PNG via Chrome se disponível
7. Confirmar o caminho ao aluno e sugerir próximo passo

**Se o perfil não tiver a Furadeira completa:**
Informe o aluno e sugira usar `/produto-concepcao` para cadastrar o método primeiro.
