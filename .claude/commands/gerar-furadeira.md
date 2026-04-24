---
name: workshop-marketing:gerar-furadeira
description: Gerar imagem PNG da Furadeira do produto ativo via IA. Dois fluxos: rapido (Gemini direto, ~30s) ou refinado (OpenRouter com imagens de referencia, ate 3min). Nao gera HTML.
allowed-tools: Read, Write, Bash
model: sonnet
---

# Gerar Furadeira (Imagem PNG)

Gera a peça visual da Furadeira do produto ativo como PNG. Coexiste com `/furadeira-visual` (que gera trilha HTML).

## Usage

```
/gerar-furadeira
```

## O Que Fazer

### 1. Contexto

Leia `meus-produtos/.ativo`. Se vazio, informe:

```
Nenhum produto ativo. Use /produto-novo ou /produto-trocar primeiro.
```

Leia `meus-produtos/{ativo}/perfil.md`. Se nao tiver Quadro e Furadeira preenchidos, informe:

```
O perfil ainda nao tem Quadro ou Furadeira. Use /produto-concepcao antes.
```

Extraia do perfil:
- **Nicho** (ex: "Tarô", "Finanças para MEI").
- **Quadro** (transformação principal).
- **Macroetapas da Furadeira** (títulos, ate 5).
- **Dor central** (primeira dor das Urgências Ocultas).
- **Avatar** (descrição curta do consumidor, de `idconsumidor.md` se existir).

### 2. Pergunta de fluxo

```
Qual fluxo de geração da furadeira você quer?

1. Rápido. Gemini direto, cerca de 30s, sem referências visuais
2. Refinado. OpenRouter com imagens de referência, até 3 minutos
3. Os dois. Gera as duas versões para comparar
```

### 3. Validações antes de gerar

**Se o usuário escolheu 2 ou 3 (OpenRouter):**

Conte arquivos `.png`, `.jpg`, `.jpeg`, `.webp` em `assets/furadeira-referencias/`.

Se < 3 arquivos, pare e informe:

```
Faltam imagens de referência.

Coloque de 3 a 16 imagens (PNG, JPG ou WEBP) em:
assets/furadeira-referencias/

São as referências visuais que o modelo vai usar para manter consistência.
Depois de colocar, rode /gerar-furadeira novamente.
```

**Se o usuário escolheu 1 ou 3 (Gemini):**

Leia `.env`. Se `GEMINI_API_KEY` estiver vazio ou ausente, pare e informe:

```
Falta a chave do Google Gemini.

Passo a passo:
1. Acesse https://aistudio.google.com/app/apikey
2. Clique em "Create API Key", copie o valor (começa com "AIzaSy")
3. Abra o arquivo .env na raiz do projeto
4. Cole na linha GEMINI_API_KEY=
5. Salve e rode /gerar-furadeira de novo
```

**Se escolheu 2 ou 3 (OpenRouter):**

Leia `.env`. Se `OPENROUTER_API_KEY` estiver vazio, pare e instrua rodar `/configurar-imagens` antes.

### 4. Construir o prompt

Monte um prompt único em inglês, com este esqueleto (substitua os placeholders pelos dados do produto):

```
Photorealistic editorial composition representing a learning journey for
"{quadro_em_ingles}" in the "{nicho_em_ingles}" niche. Visual metaphor of
progression through {N} stages: {macroetapas_em_ingles_separadas_por_virgula}.
Main audience emotional state at the start: "{dor_central_em_ingles}".
Style: cinematic lighting, neutral studio background, soft depth of field,
professional color palette, no text overlays, no logos, no readable words,
no cartoon characters. Aspect ratio 4:3.
```

Traduza as partes para inglês mantendo o significado. Não use o nome do produto nem termos em português no prompt final (o modelo responde melhor em inglês).

Salve o prompt completo numa variável para reutilizar nos dois fluxos.

### 5. Confirmação

Mostre um resumo:

```
Vou gerar:
- Fluxo: {Rápido | Refinado | Os dois}
- Produto: {nome}
- Quadro: {quadro}
- Etapas retratadas: {macroetapas}
- Referências (se refinado): {N} imagens

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 6. Executar o(s) script(s)

**Fluxo Rápido (Gemini):**

```bash
py -3 scripts/gerar-furadeira-gemini.py --slug {ativo} --prompt "{prompt}"
```

Timeout interno do script é 60s. Se demorar mais que isso, o script aborta com mensagem.

**Fluxo Refinado (OpenRouter):**

```bash
py -3 scripts/gerar-furadeira-openrouter.py --slug {ativo} --prompt "{prompt}"
```

Timeout interno 180s.

**Se escolheu "Os dois"**, rode os dois comandos em sequência. Se um falhar, continue com o outro e informe a falha no final.

### 7. Apresentar resultado

Leia o stdout de cada script. Ele retorna `OK\t{caminho}\t...` ou erro no stderr.

**Se só um PNG foi gerado:**

```
Furadeira gerada.

Caminho: meus-produtos/{ativo}/entregas/furadeira/{arquivo}.png

Abra no explorador de arquivos para visualizar. Se quiser regenerar com outro estilo, rode /gerar-furadeira de novo.
```

**Se os dois foram gerados:**

Gere um arquivo `comparacao.html` simples em `meus-produtos/{ativo}/entregas/furadeira/comparacao.html` com as duas imagens lado a lado:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Furadeira. Comparação</title>
<style>
  body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; background: #111; color: #eee; }
  h1 { font-size: 20px; margin-bottom: 16px; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .card { background: #1a1a1a; border-radius: 12px; padding: 16px; }
  .card h2 { font-size: 14px; margin: 0 0 12px; color: #aaa; text-transform: uppercase; letter-spacing: .05em; }
  .card img { width: 100%; border-radius: 8px; display: block; }
  @media (max-width: 800px) { .grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>
  <h1>Furadeira. Comparação dos dois fluxos</h1>
  <div class="grid">
    <div class="card"><h2>Rápido. Gemini</h2><img src="furadeira-gemini.png" alt="Furadeira Gemini"></div>
    <div class="card"><h2>Refinado. OpenRouter com referências</h2><img src="furadeira-openrouter.png" alt="Furadeira OpenRouter"></div>
  </div>
</body>
</html>
```

Informe:

```
Duas versões geradas.

Gemini:     meus-produtos/{ativo}/entregas/furadeira/furadeira-gemini.png
OpenRouter: meus-produtos/{ativo}/entregas/furadeira/furadeira-openrouter.png
Comparação: meus-produtos/{ativo}/entregas/furadeira/comparacao.html

Abra a comparação no navegador para decidir qual usar.
```

**Se algum falhou**, informe a mensagem exata que o script retornou e sugira:
- Erro de chave: rodar `/configurar-imagens` ou conferir `GEMINI_API_KEY` no `.env`.
- Sem crédito: recarregar em https://openrouter.ai/settings/credits.
- Referências insuficientes: adicionar em `assets/furadeira-referencias/`.

### 8. Próximo passo sugerido

```
Próximo:
- /copy-pagina para montar a página de vendas (vai usar essa imagem na seção do método)
- /furadeira-visual se preferir a versão em trilha HTML
```

## Regras

- Nunca gerar HTML do método neste comando. Só PNG.
- Não mostrar o código dos scripts ao usuário.
- Não chamar a revisora (não há copy aqui, só prompt técnico interno em inglês).
- Erros de API sempre em português claro, sem jargão de stack trace.
