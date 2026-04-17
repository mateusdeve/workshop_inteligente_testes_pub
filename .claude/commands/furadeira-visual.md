---
name: workshop-marketing:furadeira-visual
description: Gerar visualização HTML da Furadeira (método do produto) como trilha de aprendizado progressiva, com macroetapas como marcos e microetapas como checkpoints. Salva HTML e converte para PNG.
---

# Furadeira Visual — Gerar Trilha do Método

Gera a representação visual do método do produto ativo como uma trilha de jornada progressiva em HTML, com conversão obrigatória para PNG.

## Usage

```
/furadeira-visual
```

## O Que Fazer

### 1. Carregar dados

Leia `meus-produtos/.ativo` e `meus-produtos/{ativo}/perfil.md`.

Extraia: nome do método, Quadro, macroetapas e microetapas.

Se o perfil não tiver a Furadeira completa, informe:
```
O perfil não tem a Furadeira cadastrada ainda.
Use /produto-concepcao para cadastrar o método primeiro.
```

### 2. Perguntar paleta de cores

```
Qual paleta de cores para a trilha visual?

1. Verde e dourado (clássico, autoridade)
2. Azul e branco (moderno, confiança)
3. Roxo e rosa (criativo, feminino)
4. Laranja e escuro (energia, impacto)
5. Personalizada (informe as cores principais)

Digite o número:
```

### 3. Gerar HTML da trilha visual

Gere o HTML com o template de trilha progressiva (consulte `.claude/skills/furadeira-visual/` para o template completo).

A trilha deve mostrar:
- Nome do método em destaque
- Cada macroetapa como um marco numerado com título e frase-resumo
- Microetapas como checkpoints visuais dentro de cada macroetapa
- Cores da paleta escolhida aplicadas no design

### 4. Salvar HTML

Salve em `meus-produtos/{ativo}/entregas/furadeira-visual.html`.

### 5. Converter para PNG (obrigatório — tente todas as opções)

Tente converter o HTML para PNG nesta ordem de prioridade:

**Opção A — Script Python:**
```
py -3 scripts/html-to-png.py --input meus-produtos/{ativo}/entregas/furadeira-visual.html --output meus-produtos/{ativo}/entregas/furadeira-visual.png
```

**Opção B — Playwright (se instalado):**
```
python -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width':1200,'height':800})
    page.goto('file:///[caminho_absoluto]/meus-produtos/{ativo}/entregas/furadeira-visual.html')
    page.screenshot(path='meus-produtos/{ativo}/entregas/furadeira-visual.png', full_page=True)
    browser.close()
"
```

**Opção C — Puppeteer (se Node disponível):**
```
node -e "
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({width:1200,height:800});
  await page.goto('file:///[caminho_absoluto]/meus-produtos/{ativo}/entregas/furadeira-visual.html');
  await page.screenshot({path:'meus-produtos/{ativo}/entregas/furadeira-visual.png',fullPage:true});
  await browser.close();
})();
"
```

**Se todas falharem:** informe ao aluno:
```
A trilha HTML foi salva com sucesso.
Para exportar como imagem PNG:
1. Abra o arquivo no navegador (Cole no endereço: file:///[caminho])
2. Use Ctrl+P → Salvar como PDF, ou
3. Pressione F12 → aba Device → capture screenshot
```

### 6. Confirmar ao aluno

Se PNG gerado:
```
Trilha visual gerada com sucesso.

HTML: meus-produtos/{ativo}/entregas/furadeira-visual.html
PNG:  meus-produtos/{ativo}/entregas/furadeira-visual.png

Para visualizar o HTML, cole no navegador:
file:///C:/Users/Elen/.cursor/Imersão IA/workshop_inteligente/meus-produtos/{ativo}/entregas/furadeira-visual.html
```

Se só HTML:
```
Trilha visual HTML gerada.

HTML: meus-produtos/{ativo}/entregas/furadeira-visual.html

Conversão para PNG não foi possível automaticamente.
[instruções de exportação manual acima]
```
