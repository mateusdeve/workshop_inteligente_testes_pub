---
name: workshop-marketing:furadeira-visual
description: Gerar a Furadeira (método do produto) em 3 formatos à escolha. HTML (trilha visual), PNG via API (Gemini ou OpenRouter) ou prompt pronto para colar em IA externa.
allowed-tools: Read, Write, Bash
model: sonnet
---

# Furadeira Visual. Gerar o Método do Produto

Gera a representação visual do método (Furadeira) do produto ativo. O aluno escolhe entre três formatos de saída. Coexiste com `/gerar-furadeira` (atalho direto para imagem).

## Usage

```
/furadeira-visual
```

## O Que Fazer

### 1. Carregar contexto do produto ativo

Leia `meus-produtos/.ativo`. Se vazio, pare e informe:

```
Nenhum produto ativo. Use /produto-novo ou /produto-trocar primeiro.
```

Leia `meus-produtos/{ativo}/perfil.md`. Se não tiver Quadro ou Furadeira preenchidos, pare:

```
O perfil ainda não tem Quadro ou Furadeira. Use /produto-concepcao antes.
```

Leia `meus-produtos/{ativo}/idconsumidor.md` se existir. Extraia do perfil e do idconsumidor:

- **Nicho** (ex: "Tarô", "Finanças para MEI").
- **Quadro** (transformação principal).
- **Macroetapas** da Furadeira (títulos, até 5).
- **Microetapas** dentro de cada macroetapa.
- **Dor central** (primeira dor das Urgências Ocultas).
- **Avatar** (descrição curta do consumidor, se houver).

### 2. Perguntar o modo de geração

```
Como você quer gerar a Furadeira?

1. HTML. Trilha visual em página navegável (rápido, sem IA de imagem)
2. Imagem via API. PNG gerado por Gemini ou OpenRouter (precisa de chave)
3. Prompt pronto. Texto otimizado para você colar em qualquer IA externa
   (Gemini, ChatGPT, Midjourney, Ideogram, etc.)

Digite o número:
```

Siga o fluxo correspondente à escolha. As três opções são mutuamente exclusivas.

---

### 3. Opção 1. HTML (trilha visual)

#### 3.1. Perguntar paleta de cores

```
Qual paleta de cores para a trilha visual?

1. Verde e dourado (clássico, autoridade)
2. Azul e branco (moderno, confiança)
3. Roxo e rosa (criativo, feminino)
4. Laranja e escuro (energia, impacto)
5. Personalizada (informe as cores principais)

Digite o número:
```

#### 3.2. Anunciar próximo passo e gerar o HTML

```
🔍 Próximo passo: gerar trilha HTML com {N} macroetapas e microetapas. Tempo estimado: cerca de 30 segundos.
```

Gere o HTML de trilha progressiva. Consulte `.claude/skills/furadeira-visual/` para o template completo.

A trilha deve mostrar:
- Nome do método em destaque.
- Cada macroetapa como marco numerado com título e frase-resumo.
- Microetapas como checkpoints visuais dentro de cada macroetapa.
- Cores da paleta escolhida aplicadas no design.

#### 3.3. Salvar HTML

Salve em `meus-produtos/{ativo}/entregas/furadeira-visual.html`.

#### 3.4. Converter para PNG (tente todas as opções)

Tente nesta ordem de prioridade. Se uma funcionar, pare.

**A. Script Python:**
```
py -3 scripts/html-to-png.py --input meus-produtos/{ativo}/entregas/furadeira-visual.html --output meus-produtos/{ativo}/entregas/furadeira-visual.png
```

**B. Playwright (se instalado):**
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

**C. Puppeteer (se Node disponível):**
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

#### 3.5. Mensagem final

Se PNG gerado:
```
✅ Concluído: trilha visual gerada.

HTML: meus-produtos/{ativo}/entregas/furadeira-visual.html
PNG:  meus-produtos/{ativo}/entregas/furadeira-visual.png

Para visualizar o HTML, cole no navegador:
file:///C:/Users/Elen/.cursor/Imersão IA/workshop_inteligente/meus-produtos/{ativo}/entregas/furadeira-visual.html
```

Se só HTML (todas as conversões falharam):
```
✅ Concluído: trilha HTML gerada.

HTML: meus-produtos/{ativo}/entregas/furadeira-visual.html

Para exportar como PNG:
1. Abra o arquivo no navegador
2. Ctrl+P → Salvar como PDF, ou
3. F12 → aba Device → capture screenshot
```

Siga para a seção **Próximo passo sugerido**.

---

### 4. Opção 2. Imagem via API

#### 4.1. Perguntar qual API

```
Qual API usar?

1. Gemini. Rápido (cerca de 30s), sem imagens de referência
2. OpenRouter. Refinado (até 3min), usa imagens de referência em assets/furadeira-referencias/

Digite o número:
```

#### 4.2. Validar pré-condições

**Se escolheu Gemini:**

Leia `.env`. Se `GEMINI_API_KEY` estiver vazio ou ausente, pare e informe:

```
Falta a chave do Google Gemini.

Passo a passo:
1. Acesse https://aistudio.google.com/app/apikey
2. Clique em "Create API Key", copie o valor (começa com "AIzaSy")
3. Abra o arquivo .env na raiz do projeto
4. Cole na linha GEMINI_API_KEY=
5. Salve e rode /furadeira-visual de novo
```

**Se escolheu OpenRouter:**

Leia `.env`. Se `OPENROUTER_API_KEY` estiver vazio, pare e instrua rodar `/configurar-imagens` antes.

Conte arquivos `.png`, `.jpg`, `.jpeg`, `.webp` em `assets/furadeira-referencias/`. Se menos de 3, pare:

```
Faltam imagens de referência.

Coloque de 3 a 16 imagens (PNG, JPG ou WEBP) em:
assets/furadeira-referencias/

São as referências visuais que o modelo vai usar para manter consistência.
Depois de colocar, rode /furadeira-visual de novo.
```

#### 4.3. Construir o prompt em inglês

Monte um prompt único em inglês com este esqueleto (substitua os placeholders pelos dados do produto):

```
Photorealistic editorial composition representing a learning journey for
"{quadro_em_ingles}" in the "{nicho_em_ingles}" niche. Visual metaphor of
progression through {N} stages: {macroetapas_em_ingles_separadas_por_virgula}.
Main audience emotional state at the start: "{dor_central_em_ingles}".
Style: cinematic lighting, neutral studio background, soft depth of field,
professional color palette, no text overlays, no logos, no readable words,
no cartoon characters. Aspect ratio 4:3.
```

Regras de tradução pt → en:
- **Quadro:** mantém o significado do resultado final.
- **Nicho:** traduz literal.
- **Macroetapas:** traduz cada título curto, mantém a ordem, separa por vírgula.
- **Dor central:** estado emocional em inglês.

Não use o nome do produto nem termos em português. Não inclua placeholders `{}` no prompt final enviado ao script.

Para regras completas de tradução e ajustes opcionais (paleta, proporção, nicho espiritual vs corporativo), consulte `.claude/skills/gerar-furadeira/SKILL.md`.

#### 4.4. Confirmação

```
Vou gerar:
- API: {Gemini | OpenRouter}
- Produto: {nome}
- Quadro: {quadro}
- Etapas retratadas: {macroetapas}
- Referências (se OpenRouter): {N} imagens

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

#### 4.5. Executar o script

Anuncie antes:

```
🔍 Próximo passo: gerar PNG via {Gemini|OpenRouter}. Tempo estimado: cerca de {30s|3min}.
```

**Gemini:**
```
py -3 scripts/gerar-furadeira-gemini.py --slug {ativo} --prompt "{prompt}"
```

**OpenRouter:**
```
py -3 scripts/gerar-furadeira-openrouter.py --slug {ativo} --prompt "{prompt}"
```

Timeout interno do script: 60s (Gemini) ou 180s (OpenRouter). Se estourar, o script aborta com mensagem.

#### 4.6. Apresentar resultado

Leia o stdout. O script retorna `OK\t{caminho}\t...` ou erro no stderr.

**Sucesso:**
```
✅ Concluído: Furadeira gerada.

Caminho: meus-produtos/{ativo}/entregas/furadeira/{arquivo}.png

Abra no explorador de arquivos para visualizar. Se quiser regenerar com outro estilo, rode /furadeira-visual de novo.
```

**Falha:** mostre a mensagem exata do script e sugira a ação correspondente (ver seção Tratamento de erros).

Siga para a seção **Próximo passo sugerido**.

---

### 5. Opção 3. Prompt pronto (sem API)

#### 5.1. Construir o prompt em inglês

Use o mesmo esqueleto da Opção 2 (seção 4.3). Mesmas regras de tradução.

#### 5.2. Construir a versão em português

Traduza o prompt inglês para português mantendo o significado. Serve como fallback para alunos que preferem colar em português ou para conferência de conteúdo.

#### 5.3. Salvar o arquivo

Anuncie:

```
🔍 Próximo passo: salvar prompt pronto em arquivo Markdown. Tempo estimado: cerca de 5 segundos.
```

Salve em `meus-produtos/{ativo}/entregas/furadeira/prompt-furadeira.md` com esta estrutura exata:

~~~markdown
# Prompt para gerar a Furadeira em IA externa

## Onde usar

- Google Gemini (aistudio.google.com)
- ChatGPT (GPT-4o com geração de imagem)
- Midjourney, Ideogram, Leonardo, Recraft
- Qualquer outra IA de imagem que aceite prompt em inglês

## Prompt (inglês, recomendado)

```
{prompt em inglês}
```

## Prompt (português, fallback)

```
{versão em português}
```

## Dicas

- Use proporção 4:3 ou 16:9.
- Se a IA pedir estilo, repita "photorealistic editorial, cinematic lighting".
- Se o resultado vier com texto ou logo, adicione "no text, no logos".
~~~

#### 5.4. Mensagem final

```
✅ Concluído: prompt pronto salvo.

Caminho: meus-produtos/{ativo}/entregas/furadeira/prompt-furadeira.md

Copie o bloco "Prompt (inglês, recomendado)" e cole na IA de imagem de sua preferência.
```

Siga para a seção **Próximo passo sugerido**.

---

## Tratamento de erros (por opção)

Erros sempre em português claro, sem stack trace. Tabela por contexto:

**Opção 1 (HTML):**
- PNG não gerou → instrução manual (F12 → screenshot ou Ctrl+P → salvar como PDF).
- Erro ao salvar HTML → problema de permissão na pasta `entregas/`. Pedir para conferir se a pasta existe.

**Opção 2 (API):**
| Mensagem | Causa | Ação |
|---|---|---|
| `HTTP 401` Gemini | Chave inválida ou expirada | Gerar nova em https://aistudio.google.com/app/apikey |
| `HTTP 401` OpenRouter | Chave inválida | Rodar `/configurar-imagens` |
| `HTTP 402` OpenRouter | Sem crédito | Recarregar em https://openrouter.ai/settings/credits |
| `HTTP 429` | Rate limit | Esperar 1 a 2 min e tentar de novo |
| `RESOURCE_EXHAUSTED` | Cota diária do free tier Gemini | Esperar 24h ou ativar billing no Google Cloud |
| "Nenhuma imagem retornada" | Modelo devolveu só texto | Reforçar no prompt: `Generate an image, not text` |
| "Faltam imagens de referência" | Pasta com menos de 3 arquivos | Adicionar referências em `assets/furadeira-referencias/` |

**Opção 3 (prompt pronto):**
- Só pode falhar na escrita do arquivo (permissão). Mensagem simples pedindo para conferir a pasta `entregas/furadeira/`.

---

## Próximo passo sugerido

Após qualquer uma das 3 opções, mostre:

```
Próximo:
- /copy-pagina para usar a Furadeira na seção Método da página de vendas
- /furadeira-visual de novo se quiser testar outro formato
```

---

## Regras

- Nunca mostrar código dos scripts ao usuário.
- Não chamar a skill `revisora` (prompts técnicos em inglês não passam por revisão de copy).
- Erros sempre em português, sem jargão de stack trace.
- Anunciar "próximo passo" antes de operações longas (regra global do CLAUDE.md).
- Não misturar as 3 opções numa mesma execução. O aluno escolhe uma; para rodar outra, executa o comando de novo.
