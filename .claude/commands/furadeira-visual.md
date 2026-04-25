---
name: workshop-marketing:furadeira-visual
description: Gerar a Furadeira (método do produto) em 3 formatos à escolha. HTML (trilha visual), PNG via OpenRouter (Gemini Flash, Gemini Pro ou GPT-5.4 Image 2) ou prompt pronto para colar em IA externa.
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
2. Imagem via API. PNG gerado via OpenRouter (precisa de chave do OpenRouter)
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

**REGRA OBRIGATÓRIA. Botão Baixar PNG embutido no HTML.**

Todo HTML gerado nesta opção precisa incluir o bloco de botão de download ANTES de `</body>`. Conteúdo exato do bloco em `.claude/skills/furadeira-visual/references/botao-baixar-png.html`. Copie o arquivo inteiro (comentários e tudo) e cole imediatamente antes de `</body>`.

Por quê:
- O aluno precisa conseguir exportar a Furadeira como imagem sem depender de Python, Playwright, Puppeteer nem de habilidade técnica para usar DevTools.
- A conversão backend (passo 3.4) pode falhar em máquinas sem as ferramentas instaladas. O botão embutido garante que qualquer usuário, em qualquer máquina, baixe o PNG com um clique.
- Se os templates de referência em `.claude/skills/furadeira-visual/references/templates/` forem usados como base, o bloco já vem incluso. Se o HTML for gerado do zero, incluir manualmente é obrigatório.

Checklist antes de salvar o HTML:
- [ ] O arquivo contém o comentário `<!-- ===== Botão Baixar PNG` antes de `</body>`.
- [ ] O ID `btn-baixar-furadeira` aparece exatamente uma vez.
- [ ] O script carrega `html2canvas` via CDN (`cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1`).
- [ ] O botão usa `position: fixed; top: 20px; right: 20px` (não invade o conteúdo).
- [ ] O botão tem `@media print { display: none; }` (não aparece em PDF nem screenshot manual).

Se qualquer item falhar, corrija antes de salvar.

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

Para baixar como PNG:
1. Abra o arquivo no navegador
2. Clique no botão "Baixar PNG" no canto superior direito da página
3. O download começa automaticamente (arquivo furadeira.png)

O botão é embutido no HTML e funciona em qualquer máquina com internet.
```

Siga para a seção **Próximo passo sugerido**.

---

### 4. Opção 2. Imagem via API

Toda geração de imagem usa OpenRouter. A escolha é apenas de modelo.

#### 4.1. Validar chave

Leia `.env`. Se `OPENROUTER_API_KEY` estiver vazio ou ausente, informe e ofereça o prompt direto:

```
Falta a chave do OpenRouter para gerar automaticamente.

Posso te dar o prompt agora para você colar no ChatGPT e gerar sem configurar nada.

1. Me dá o prompt agora (vou colar no ChatGPT)
2. Quero configurar a chave do OpenRouter (leva 2 minutos)
```

Se escolher **1**: siga o fluxo da **Opção 3** (seção 5).

Se escolher **2**: informe os passos:
```
Passo a passo:
1. Acesse openrouter.ai/settings/keys
2. Clique em "Create Key", copie o valor
3. Abra o arquivo .env na raiz do projeto
4. Cole na linha OPENROUTER_API_KEY=sua_chave_aqui
5. Salve e rode /furadeira-visual de novo
```

#### 4.2. Referências e modelo

Pergunte sobre imagens de referência:

```
Quer usar imagens de referência para guiar o estilo visual?

1. Sim, já estão salvas na pasta (assets/furadeira-referencias/)
2. Sim, quero enviar aqui no chat agora
3. Não, gerar sem referências

As referências ajudam o modelo a replicar cores, layout e estilo de um design que você já gosta.

Digite o número:
```

**Se escolheu 1 (pasta local):**

Conte arquivos `.png`, `.jpg`, `.jpeg`, `.webp` em `assets/furadeira-referencias/`. Se menos de 3, informe:

```
Encontrei apenas {N} imagem(ns) em assets/furadeira-referencias/.
Para melhores resultados, coloque pelo menos 3 imagens de referência.

1. Vou adicionar mais imagens (retome depois)
2. Usar as {N} que já estão lá mesmo assim
3. Enviar as referências aqui no chat agora
```

**Se escolheu 2 (enviar no chat):**

```
Envie as imagens de referência aqui no chat.
Pode arrastar do explorador de arquivos, colar ou usar o botão de anexo.
Aceito de 1 a 16 imagens (PNG, JPG ou WEBP).

Quando terminar de enviar todas, diga "pronto".
```

Aguarde o aluno enviar as imagens e confirmar com "pronto". Após receber:

1. Limpe as referências antigas com Bash:
   ```
   bash -c "rm -f assets/furadeira-referencias/ref-*.png assets/furadeira-referencias/ref-*.jpg assets/furadeira-referencias/ref-*.jpeg assets/furadeira-referencias/ref-*.webp"
   ```

2. Para cada imagem recebida, identifique o caminho do arquivo. Use Bash para copiar para `assets/furadeira-referencias/` com nome sequencial (`ref-01.png`, `ref-02.jpg`, etc.):
   ```
   cp "{caminho_original}" "assets/furadeira-referencias/ref-{NN}.{ext}"
   ```

3. Se a imagem veio como conteúdo inline, leia-a com o Read tool pelo caminho temporário e salve em `assets/furadeira-referencias/ref-{NN}.png` com o Write tool.

4. Confirme quantas foram salvas:
   ```
   {N} imagens salvas em assets/furadeira-referencias/. Seguindo...
   ```

**Se escolheu 3 (sem referências):**

Guarde internamente `max_refs = 0` para usar no passo 4.5.

Após definir as referências, pergunte o modelo:

```
Qual modelo usar para gerar a Furadeira?

1. Gemini 2.5 Flash Image (padrão). O mais rápido e econômico. Bom para a maioria dos casos.
2. Gemini 2.5 Pro Image. Qualidade visual superior, mais fiel às referências. Custa um pouco mais por geração.
3. GPT-5.4 Image 2 (OpenAI). O mais avançado da lista. Raciocínio superior para seguir instruções complexas, ótimo para diagramas limpos. Mais caro por geração.

Todos os três recebem suas imagens de referência e geram PNG com fundo transparente.

Digite o número:
```

Mapeamento interno (não mostrar ao usuário):

- 1 → `google/gemini-2.5-flash-image`
- 2 → `google/gemini-2.5-pro-image`
- 3 → `openai/gpt-5.4-image-2`

Guarde o model ID e `max_refs` para usar no passo 4.5.

#### 4.3. Analisar as referências e construir o prompt em inglês

**OBJETIVO DO PROMPT:** gerar um infográfico visual que representa o método do produto, não uma foto ou cena realista. O resultado deve parecer um diagrama profissional de etapas. O prompt precisa ser altamente assertivo: o modelo recebe as imagens de referência E uma descrição textual detalhada delas, reforçando duplamente o que deve ser replicado.

---

**Passo 4.3.1 — Analisar cada imagem de referência**

Examine as imagens em `assets/furadeira-referencias/` e registre internamente os seguintes atributos para o conjunto:

**Paleta de cores:**
- Cor dominante do fundo dos cards ou elementos (ex: branco, azul royal #2B4AE8, escuro #1A1A2E)
- Cor de destaque/acento usada em ícones, setas ou bordas (ex: dourado #F5A623, verde #00C875)
- Cor dos textos dos títulos e subtítulos

**Tipografia:**
- Família: sem serifa moderna (Poppins, Inter), serifada clássica, display bold, script
- Peso predominante dos títulos (thin, regular, bold, black/heavy)
- Peso dos subtítulos ou descrições
- Tamanho relativo: compacto e denso, ou amplo e arejado

**Layout das etapas:**
- Estrutura: horizontal com setas, vertical tipo timeline, cards em grid, círculo central com ramificações
- Conexão entre etapas: setas finas, linha pontilhada, numeração progressiva, nenhuma conexão explícita
- Proporção dos cards: quadrado, retângulo largo, retângulo alto, forma orgânica

**Ícones:**
- Estilo: outline fino, preenchido sólido, ilustrativo com gradiente, emoji-like, pictograma geométrico
- Tamanho relativo ao texto: grande acima do texto, pequeno ao lado esquerdo, centralizado

**Fundo geral:**
- Sem fundo (transparente), branco limpo, gradiente suave, cor sólida, textura

**Elementos decorativos:**
- Formas geométricas no fundo (círculos, hexágonos, ondas)
- Separadores entre etapas
- Sombras nos cards (flat sem sombra, sombra suave, sombra longa)

**Tom visual geral:**
- Corporativo sóbrio, espiritualizado/etéreo, vibrante e moderno, acadêmico clean, minimalista premium

Com base na análise, monte uma descrição consolidada de 4 a 6 frases em inglês que capture a essência visual do conjunto. Ela entrará diretamente no prompt. Exemplo de boa descrição consolidada:

> "The references show a modern flat design style. Each step is represented as a rounded rectangle card with a thin-outline icon centered above the label text. Cards are connected by thin horizontal arrows. The dominant color is deep navy blue (#1A3A6B) with golden accents (#E8A200) on the icons and arrows. Typography is bold sans-serif (similar to Poppins or Inter) for step titles and regular weight for descriptions. The overall tone is professional and corporate, with no background fill."

---

**Passo 4.3.2 — Montar o prompt em inglês**

Monte o prompt usando o esqueleto abaixo. Substitua todos os placeholders. O frame técnico fica em inglês, mas os textos visíveis do infográfico (nome do método, macroetapas, rótulos) ficam em português brasileiro exatamente como estão no perfil.

```
Professional flat design infographic. Transparent background, PNG with alpha channel. No background color, no background fill, no solid or gradient fill behind the entire composition.

VISUAL STYLE — replicate faithfully from the provided reference images:
{descricao_consolidada_das_referencias_em_ingles}

METHOD CONTENT:
Method name (keep exactly in Brazilian Portuguese, do not translate): "{nome_do_metodo}"
Goal/transformation (keep exactly in Brazilian Portuguese, do not translate): "{quadro}"

STEPS — keep all labels exactly in Brazilian Portuguese, do not translate or paraphrase. Preserve all accented characters exactly as written (ã, é, ç, ó, ú, â, ê, etc.):
Step 1: "{macroetapa_1}"
Step 2: "{macroetapa_2}"
Step 3: "{macroetapa_3}"
[add more steps as needed]

LAYOUT: {horizontal flow with connecting arrows | vertical timeline | side-by-side cards} — use the layout most consistent with the references.
ICON STYLE: {outline thin icons | filled solid icons | illustrative gradient icons} — match the reference exactly.
COLOR PALETTE: {cores_em_ingles, ex: "deep navy blue #1A3A6B as dominant, golden #E8A200 as accent, white text on dark cards"}
TYPOGRAPHY: {estilo_tipografico_em_ingles, ex: "bold sans-serif titles similar to Poppins, regular weight for descriptions, tight line-height"}
SPACING: {compact and dense | balanced | airy and spacious} — match the references.
DECORATIVE ELEMENTS: {descricao_dos_elementos_decorativos_se_houver, ex: "thin horizontal arrows between cards, subtle drop shadow on cards, no other decoration"}

HARD CONSTRAINTS:
- Transparent background (PNG with alpha channel). No white fill, no colored fill, no gradient wash behind the full canvas. Only the infographic elements themselves should be visible.
- All visible text must be in Brazilian Portuguese (pt-BR). Never translate method name or step labels.
- Render all accented characters correctly: ã, á, â, à, é, ê, í, ó, ô, õ, ú, ç. Do NOT strip, replace, or ignore accents. "Açao" is wrong; "Ação" is correct.
- No people, no faces, no photographs, no realistic scenes, no handwriting.
- No logos, no watermarks, no decorative frames around the full canvas.
- Output format: PNG with transparent background, aspect ratio 4:3, minimum width 1200px.
- The result must look like a professional training material or presentation slide.
- No foreign text, no English labels visible in the final image.
```

**Regras de preenchimento:**
- `{descricao_consolidada_das_referencias_em_ingles}`: a descrição de 4 a 6 frases montada no passo 4.3.1, traduzida para inglês. Seja específico: cite cores HEX, estilo de ícone, tipo de layout, peso da tipografia.
- `{nome_do_metodo}` e `{quadro}`: extraídos do perfil, mantidos exatamente em português.
- `{macroetapas}`: exatamente como estão no perfil. Não traduzir, não parafrasear.
- Layout e ícones: escolha o que domina nas referências.
- Não inclua placeholders `{}` no prompt final enviado ao script.

**Regras críticas:**
- Nunca usar "photorealistic", "cinematic", "editorial", "photograph" ou "portrait".
- Nunca usar "no foreign text" no prompt (bloqueia o português).
- Sempre incluir `"All visible text must be in Brazilian Portuguese (pt-BR)"`.
- Fundo transparente deve aparecer em pelo menos 3 pontos do prompt: na abertura, em HARD CONSTRAINTS, e em Output format.
- **Acentuação obrigatória:** o prompt deve instruir explicitamente o modelo a renderizar os acentos do português (ã, é, ç, ó, â, etc.). Inclua a linha de acentos em HARD CONSTRAINTS e repita na instrução de STEPS. Modelos de imagem tendem a omitir ou substituir acentos se não forem instruídos com exemplo concreto ("Ação" não "Açao").

Para ajustes opcionais por nicho (espiritual vs corporativo, proporção, paleta alternativa), consulte `.claude/skills/gerar-furadeira/SKILL.md`.

#### 4.4. Confirmação

```
Vou gerar:
- Modelo: {nome do modelo escolhido, ex: "Gemini 2.5 Flash Image"}
- Produto: {nome}
- Quadro: {quadro}
- Etapas retratadas: {macroetapas}
- Referências: {N} imagens | sem referências

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

#### 4.5. Executar o script

Anuncie antes:

```
🔍 Próximo passo: gerar PNG via OpenRouter. Tempo estimado: cerca de 2 a 3 minutos.
```

Execute:

```
py -3 scripts/gerar-furadeira-openrouter.py --slug {ativo} --prompt "{prompt}" --model {model_id} --max-refs {N}
```

Onde:

- `{model_id}` é o ID do modelo escolhido (ex: `openai/gpt-5.4-image-2`)
- `{N}` é o número de referências em `assets/furadeira-referencias/` (use `0` se o aluno optou por gerar sem referências)

Timeout interno do script: 180s. Se estourar, o script aborta com mensagem.

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

**Recomendado: ChatGPT (chatgpt.com) com imagens de referência**
O ChatGPT processa imagens de referência de forma nativa — muito mais fiel do que via API.
Envie as referências E o prompt no mesmo chat para o melhor resultado possível.

**Como usar com referências no ChatGPT:**
1. Acesse chatgpt.com e abra um chat novo
2. Clique no ícone de clipe (anexo) e selecione suas imagens de referência
3. Cole o prompt abaixo no campo de texto
4. Envie tudo junto (referências + prompt) em uma única mensagem
5. O ChatGPT vai analisar as referências e gerar a imagem no estilo delas

Alternativas (sem referências visuais):
- Google Gemini (gemini.google.com)
- Ideogram ou Recraft (melhor suporte a fundo transparente)
- Midjourney, Leonardo

## Prompt (inglês, recomendado)

```
{prompt em inglês}
```

## Prompt (português, fallback)

```
{versão em português}
```

## Dicas

**OBRIGATÓRIO: salvar como PNG com fundo TRANSPARENTE.**
Após gerar no ChatGPT: clique com o botão direito na imagem e salve como PNG.
Verifique se o fundo está transparente: ao abrir no editor de imagens, deve aparecer xadrez cinza e branco no lugar do fundo, não branco sólido.
Se vier com fundo branco, adicione ao prompt: "transparent background, PNG with alpha channel, no background color, no background fill".

- Use proporção 4:3 ou 16:9.
- Se a IA gerar foto de pessoas ou cena realista, adicione: "no people, no faces, no photographs, infographic only".
- Se o resultado vier com logo ou marca d'água, adicione: "no logos, no watermarks".
~~~

#### 5.4. Mensagem final

```
✅ Concluído: prompt pronto salvo.

Caminho: meus-produtos/{ativo}/entregas/furadeira/prompt-furadeira.md

Como usar:
1. Acesse https://chatgpt.com/ e entre no chat
2. Copie todo o bloco abaixo (da primeira até a última linha):

---
[exibir aqui o prompt em inglês gerado, sem o bloco de código, direto no chat]
---

3. Cole no campo de mensagem do ChatGPT e envie
4. O ChatGPT vai gerar a imagem direto na conversa
5. Clique na imagem gerada e salve como PNG
```

Siga para a seção **Próximo passo sugerido**.

---

## Tratamento de erros (por opção)

Erros sempre em português claro, sem stack trace. Tabela por contexto:

**Opção 1 (HTML):**
- PNG não gerou → instrução manual (F12 → screenshot ou Ctrl+P → salvar como PDF).
- Erro ao salvar HTML → problema de permissão na pasta `entregas/`. Pedir para conferir se a pasta existe.

**Opção 2 (API via OpenRouter):**

| Mensagem | Causa | Ação |
|---|---|---|
| `HTTP 401` | Chave do OpenRouter inválida | Conferir `OPENROUTER_API_KEY` no `.env` |
| `HTTP 402` | Sem crédito | Recarregar em openrouter.ai/settings/credits |
| `HTTP 429` | Rate limit | Esperar 1 a 2 min e tentar de novo |
| "Nenhuma imagem retornada" | Modelo devolveu só texto | Reforçar no prompt: `Generate an image, not text` |
| "Faltam imagens de referência" | Pasta com menos de 3 arquivos e `--max-refs` não é 0 | Adicionar referências ou escolher "sem referências" |

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
- **Proibido incluir `<footer>` no HTML gerado.** Não adicionar rodapé com nome do produto nem qualquer outro texto no final da página.
- **Todo HTML gerado na opção 1 precisa ter o botão "Baixar PNG" embutido antes de `</body>`.** Conteúdo canônico em `.claude/skills/furadeira-visual/references/botao-baixar-png.html`. Se o HTML for gerado a partir dos templates em `references/templates/`, o bloco já vem junto. Se for gerado do zero, copiar o arquivo de referência inteiro e colar antes de `</body>`. Essa regra vale para qualquer aluno, em qualquer máquina, sem exceção. O botão usa html2canvas via CDN e não depende de Python, Playwright ou Puppeteer.
