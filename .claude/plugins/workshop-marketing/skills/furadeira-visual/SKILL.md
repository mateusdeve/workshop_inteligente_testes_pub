---
name: furadeira-visual
description: Gerar a Furadeira (método VTSD) como diagrama visual em HTML estatico pronto para virar imagem. 5 layouts (linear, circular, piramidal, hub, fluxograma), paleta editavel e conversao automatica para PNG via Edge headless. Use sempre que o usuario pedir furadeira em imagem, diagrama do metodo, mapa do metodo, infografico do metodo ou furadeira visual.
---

# Furadeira Visual

Gera a Furadeira (método estruturado do produto, em macroetapas e microetapas) como **diagrama visual em HTML estático**, pronto para ser convertido em imagem. Resolve o problema de diagramas nativos da IA ficarem ruins.

## Quando usar esta skill

Use SEMPRE que o usuário pedir uma das coisas abaixo:
- "Quero a furadeira em imagem"
- "Gera um diagrama do método"
- "Faz um visual da furadeira"
- "Quero mostrar o método em formato visual"
- "Mapa do método", "infográfico do método"
- "Furadeira para postar no Instagram / colocar na página de vendas"

NÃO use para:
- Apenas listar as etapas em texto (isso é o `produto-editar`)
- Criar a furadeira do zero quando ela ainda não existe (use `produto-editar` antes)

## O que é a Furadeira (referência VTSD)

**Furadeira = mecanismo único** que liga o problema do consumidor ao Quadro (transformação prometida). É a forma de tornar visível e comunicável a **eficiência** do método (eficaz cumpre o prometido, eficiente cumpre melhor: mais rápido, mais barato, com menos esforço, menos dor, mais adesão, etc.).

A furadeira é composta por:

- **Nome próprio.** Acrônimo (ex: CAVE), sigla (VTSD), nome do autor, curioso (Furadeira, Aperta e Solta), impactante (Escudo do Comportamento), benefício (Fluência em 90 Dias) ou mistério (Tecnologia de Alinhamento Postural Titanium).
- **Macroetapas:** os grandes blocos do método (3 a 7 normalmente).
- **Microetapas:** os passos dentro de cada macroetapa (opcional).
- **Mecânicas internas:** as 6 mecânicas que dão sensação de método ao produto digital (lógica condicional, enquadramento, listas, fases e sequências, identificando empecilhos, dinâmica de entrega). Não precisa ter as 6, escolha as que combinam com o método.
- **Replicabilidade:** outra pessoa do nicho consegue executar o método e chegar a um resultado próximo. Se só o criador consegue, é talento, não é método (história do bombeiro).

A furadeira não é só uma lista. É a peça central que faz o aluno enxergar como vai sair do ponto A ao ponto B. Quando virar visual, precisa transmitir **clareza, lógica, progressão e sensação de método**.

Por isso, antes de gerar o visual, garanta que a furadeira do produto ativo tenha:
1. Um nome próprio e memorável (não genérico, não bobinho, não copiado)
2. De 3 a 7 macroetapas com nome curto (até 4 palavras cada)
3. Uma frase de 1 linha por macroetapa explicando o que acontece ali
4. (Opcional) Microetapas, ícone sugerido ou número de cada etapa

Se faltar algo, **complete junto com o usuário antes de partir pro visual**. Não invente etapa que não existe.

**Disclaimer (sempre alertar):**
- Cuidado com furadeira mirabolante e complexa demais. Se virar 9 etapas e 3 fluxogramas, está gerando complexidade no lugar de facilidade. Quando o nicho exige profundidade, quebre em fases.
- Não paralise achando que "ainda não ficou bom". A furadeira evolui com cada turma.
- Integridade: não invente "enzima da Tailândia". Mecanismo único é descobrir e nomear o que **existe** ou o que você **realmente faz** de diferente. O teste é: você consegue defender isso diante de um especialista do nicho?

Para o conteúdo completo das 6 mecânicas, formas de eficiência, técnicas de naming, autores clássicos e disclaimers, consulte `references/6-mecanicas.md`.

## Fluxo da skill (6 passos)

### Passo 1. Ler contexto

1. Ler `entregas/.ativo` para descobrir o produto ativo.
2. Ler `entregas/{ativo}/perfil.md` e extrair:
   - Nome do produto
   - Quadro (transformação)
   - Furadeira (nome do método + macroetapas + microetapas se houver)
   - Nicho
3. Se a furadeira não existir ou estiver vaga (sem macroetapas nomeadas), pare e oriente:
   > "Sua furadeira ainda não está estruturada com macroetapas. Vamos primeiro estruturar com `/produto-editar` e depois voltar aqui."

### Passo 2. Entrevista (UMA pergunta por vez, sempre numerada)

**Pergunta 1. Estilo visual.** Mostre as 5 opções com descrição curta:

```
Qual estilo de visual você quer para sua furadeira?

1. Linear horizontal. As macroetapas em sequência da esquerda pra direita, com setas conectando. Bom para mostrar progressão clara. Funciona em página de vendas e em post de feed horizontal.

2. Roadmap vertical (timeline). As macroetapas empilhadas de cima para baixo, conectadas por uma linha do tempo. Bom para Reels, Story e post vertical.

3. Pirâmide invertida. Começa com o problema (base larga) e vai afunilando até o Quadro no topo. Bom para mostrar transformação.

4. Hub central. O Quadro no centro, as macroetapas em volta como satélites. Bom quando as etapas não têm ordem rígida.

5. Fluxograma com lógica condicional. Cada etapa tem ponto de decisão (se A então B, se não C). Bom para método com diagnóstico, perfis ou trilhas diferentes.

Digite o número:
```

**Pergunta 2. Formato e dimensão.**
```
Onde você vai usar essa imagem?

1. Quadrado 1080x1080. Post de feed Instagram, carrossel.
2. Vertical 1080x1920. Story, Reels, capa de WhatsApp.
3. Horizontal 1920x1080. Página de vendas, slide de apresentação, capa de YouTube.
4. Horizontal 1200x630. Capa de blog, link preview de redes sociais.

Digite o número:
```

**Pergunta 3. Paleta de cores.**
```
Qual paleta de cores combina com sua marca?

1. Amarelo handwritten (estilo workshop, igual ao mapa mental do VTSD)
2. Azul corporativo (sério, profissional, ideal para infoproduto B2B)
3. Roxo premium (para ticket alto, autoridade, mentoria)
4. Verde natureza (saúde, bem-estar, sustentabilidade)
5. Rosa feminino (autoestima, beleza, relacionamentos)
6. Personalizado. Cole abaixo a cor primária em hex (ex: #2b6cb0)

Digite o número (ou cole o hex):
```

**Pergunta 4. Incluir o nome do método e o Quadro como título?**
```
Quer incluir título e subtítulo na imagem?

1. Sim. Nome do método em destaque + Quadro como subtítulo (recomendado)
2. Só o nome do método
3. Só as macroetapas, sem cabeçalho
```

### Passo 3. Confirmação

Mostre um resumo curto antes de gerar:

```
Resumo do que vou criar:

- Produto: {nome}
- Método: {nome da furadeira}
- Estilo: {nome do estilo escolhido}
- Formato: {dimensão}
- Paleta: {paleta}
- Macroetapas: {N} etapas
- Cabeçalho: {sim/não}

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### Passo 4. Geração do HTML

Gere um arquivo HTML standalone seguindo as **regras técnicas obrigatórias**:

#### Regras técnicas

1. **Dimensão fixa**. O `<body>` tem `width` e `height` exatos da escolha. Sem scroll, sem responsivo. O HTML é uma "tela" pronta pra print.
2. **Tudo embutido**. CSS dentro de `<style>`, sem dependências externas exceto Google Fonts.
3. **Fontes**:
   - Para paleta amarelo handwritten: `Caveat` (heading) + `Patrick Hand` (body). Usa tamanhos generosos.
   - Para azul, roxo, verde, rosa, personalizado: `Plus Jakarta Sans` (heading) + `Inter` (body).
4. **Sem emoji**. Use formas geométricas, números dentro de círculos, ícones SVG inline simples (chevron, check, seta). Emoji distorce em conversão para PNG.
5. **Contraste alto** entre fundo e texto. Mínimo 4.5:1.
6. **Margem segura interna**. Padding mínimo de 60px nas bordas pra não cortar nada no print.
7. **Regra do travessão**. Em nenhum texto da imagem (títulos, subtítulos, descrições, labels) pode aparecer travessão (—). Substitua por dois pontos, ponto final ou vírgula.
8. **Sem placeholder do tipo `[Sua imagem aqui]`**. A imagem é o entregável final, não um template.
9. **Texto NÃO pode estourar o container**. Se uma macroetapa tem nome longo, quebre em duas linhas ou reduza a fonte. Teste mentalmente: "esse texto cabe?".

#### Templates por estilo

Cada estilo tem uma estrutura HTML diferente. Os templates de referência estão em `references/templates/`. Use o template do estilo escolhido como base e preencha com os dados da furadeira.

**Linear horizontal:** Grid CSS com N colunas (uma por macroetapa), setas SVG conectando. Número grande no topo de cada coluna, nome da etapa em destaque, descrição curta abaixo.

**Roadmap vertical:** Linha vertical no centro, marcadores (círculos numerados) na linha, conteúdo alternando esquerda/direita.

**Pirâmide invertida:** N camadas trapezoidais empilhadas. Base maior (problema) no rodapé, topo (Quadro) no topo. Cada camada com nome e descrição.

**Hub central:** Círculo grande no centro com Quadro/Quadrado da transformação. N círculos menores em torno (posicionados via `position: absolute` ou `transform: rotate`), conectados por linhas SVG ao centro.

**Fluxograma condicional:** Caixas com setas SVG, losangos para decisões. Estilo Mermaid mas escrito à mão em HTML/CSS.

#### Paletas (variáveis CSS)

```css
/* Amarelo handwritten */
--bg: #fde68a;
--bg-alt: #fef3c7;
--ink: #1f2937;
--accent: #f59e0b;
--line: #1f2937;

/* Azul corporativo */
--bg: #f8fafc;
--bg-alt: #e0f2fe;
--ink: #0f172a;
--accent: #2563eb;
--line: #1e40af;

/* Roxo premium */
--bg: #faf5ff;
--bg-alt: #f3e8ff;
--ink: #1e1b4b;
--accent: #7c3aed;
--line: #4c1d95;

/* Verde natureza */
--bg: #f0fdf4;
--bg-alt: #dcfce7;
--ink: #14532d;
--accent: #16a34a;
--line: #166534;

/* Rosa feminino */
--bg: #fff1f2;
--bg-alt: #ffe4e6;
--ink: #500724;
--accent: #e11d48;
--line: #9f1239;
```

Para paleta personalizada, gere as variações automaticamente a partir do hex primário:
- `--bg`: lighten(primary, 90%)
- `--bg-alt`: lighten(primary, 80%)
- `--ink`: darken(primary, 70%)
- `--accent`: o hex original
- `--line`: darken(primary, 30%)

#### Estrutura mínima do HTML

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Furadeira: {nome do método}</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root { /* paleta */ }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: {LARGURA}px; height: {ALTURA}px; overflow: hidden; }
  body {
    background: var(--bg);
    color: var(--ink);
    font-family: 'Inter', sans-serif;
    padding: 80px;
    display: flex;
    flex-direction: column;
  }
  h1, h2, h3 { font-family: 'Plus Jakarta Sans', sans-serif; }
  /* ... estilos específicos do template ... */
</style>
</head>
<body>
  <header>
    <h1>{nome do método}</h1>
    <p class="quadro">{Quadro}</p>
  </header>
  <main class="furadeira-{estilo}">
    <!-- macroetapas -->
  </main>
  <footer>
    <small>{nome do produto}</small>
  </footer>
</body>
</html>
```

### Passo 5. Salvar e converter

1. Criar pasta se necessário: `entregas/{ativo}/furadeira/`
2. Salvar HTML em `entregas/{ativo}/furadeira/furadeira-{estilo}-{timestamp}.html`
3. **Tentar converter automaticamente para PNG via Edge headless** (Windows):

```bash
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" \
  --headless \
  --disable-gpu \
  --screenshot="entregas/{ativo}/furadeira/furadeira-{estilo}-{timestamp}.png" \
  --window-size={LARGURA},{ALTURA} \
  --hide-scrollbars \
  "file:///{caminho-absoluto}/furadeira-{estilo}-{timestamp}.html"
```

Se Edge não estiver no caminho padrão, tentar:
- `"C:\Program Files\Microsoft\Edge\Application\msedge.exe"`
- `"C:\Program Files\Google\Chrome\Application\chrome.exe"`

Use Bash para executar. Espere terminar (timeout 30s). Verifique se o PNG foi criado.

4. Se a conversão automática falhar, NÃO travar a entrega. Apenas avise:
   > "Não consegui converter automaticamente para PNG aqui (Edge/Chrome não respondeu). Mas o HTML está pronto. Abra `{caminho}` no navegador e tire um print da tela inteira (Win+Shift+S), ou clique direito e 'Salvar como imagem'."

### Passo 6. Entrega

Mostre ao usuário (sem nunca colar o código HTML, conforme regra do CLAUDE.md):

```
Pronto. Sua furadeira visual foi gerada.

Arquivos:
- HTML: entregas/{ativo}/furadeira/furadeira-{estilo}-{timestamp}.html
- PNG: entregas/{ativo}/furadeira/furadeira-{estilo}-{timestamp}.png  (se conversão deu certo)

Como usar:
- Para postar no Instagram, use o PNG diretamente.
- Para colocar na página de vendas, use o PNG ou incorpore o HTML inline.
- Se quiser ajustar algo (cor, ordem, texto de uma etapa), me diga o que mudar.

Próximo passo sugerido:
- Quer que eu coloque essa furadeira na seção "Método" da sua página de vendas? Use `/copy-pagina` ou edite a página existente.
```

## Regras de qualidade (checklist antes de entregar)

Antes de salvar, verifique mentalmente:

- [ ] Todas as N macroetapas aparecem na imagem (nada cortado).
- [ ] O nome de cada etapa está legível (fonte >= 24px no design).
- [ ] Há contraste forte entre texto e fundo.
- [ ] Não tem travessão em lugar nenhum.
- [ ] Não tem texto em inglês (a não ser que o nicho exija).
- [ ] Não tem placeholder visível tipo "Lorem ipsum" ou "[texto aqui]".
- [ ] O HTML tem dimensões fixas (largura e altura definidas no body).
- [ ] As fontes do Google Fonts foram carregadas no `<link>`.
- [ ] O título da página HTML reflete o nome do método.
- [ ] Não há scroll. Tudo cabe dentro da tela.

## Erros comuns a evitar

1. **Texto estourando container.** Se a macroetapa se chama "Estruturação Estratégica do Diagnóstico Inicial", isso não cabe num card pequeno. Reduza para "Diagnóstico" ou "Diagnóstico Inicial".
2. **Inventar macroetapas que não existem no perfil.** Se o usuário tem 4 etapas, gere com 4. Não infle pra 6 só porque o template tem 6 colunas.
3. **Criar HTML responsivo.** Esse HTML não é uma página, é uma "captura de tela". Dimensões fixas, sem media queries.
4. **Esquecer da regra do travessão.** Faça uma busca de texto antes de salvar.
5. **Mostrar o código HTML para o usuário.** Salve direto e diga só o caminho.
6. **Usar Picsum ou imagem de banco aleatória.** Esse visual é geométrico, não tem foto.
7. **Ignorar o estilo escolhido pelo usuário.** Se ele pediu hub central, não entregue linear horizontal.

## Onde salvar

`entregas/{ativo}/furadeira/`

Convenção de nome:
- `furadeira-{estilo}-{YYYYMMDD-HHMM}.html`
- `furadeira-{estilo}-{YYYYMMDD-HHMM}.png`

Exemplo: `furadeira-linear-20260408-1530.html`

## Referências

- `references/templates/` — 5 templates HTML base, um por estilo.
- Mecânicas do método (PDF "Mecânica de um Produto"): lógica condicional, enquadramento, listas, fases e sequências, encontrando empecilhos, dinâmica de entrega. Use essa terminologia se o usuário pedir um visual mais técnico-explicativo da mecânica do método.
- Estrutura 8D da página de vendas: a furadeira aparece na seção "Método" (seção 3 do hero). O visual gerado aqui é o que vai nessa seção.
