---
name: workshop-marketing:imagem-prompt
description: Gerar prompts de imagem otimizados para 7 ferramentas gratuitas (Whisk, ImageFX, Gemini, Ideogram, Leonardo, Bing Image Creator, Krea). Sem gastar API. O aluno escolhe a ferramenta e a skill entrega o prompt no formato nativo dela, pronto para colar. Ideal para anúncios, carrossel e capa de produto.
---

# Imagem Prompt. Prompts Prontos para 7 Ferramentas Gratuitas

Gera prompts de imagem otimizados para as melhores ferramentas gratuitas de geração de imagem em 2026. A skill **não gera a imagem**, ela entrega o prompt no formato nativo de cada ferramenta. Você cola no site e baixa a imagem. Zero custo de API.

## Usage

```
/imagem-prompt
```

## Por Que Esta Skill

- **Zero gasto de API.** Toda geração acontece nos sites gratuitos das ferramentas.
- **Prompt otimizado por ferramenta.** Whisk usa 3 inputs visuais, Ideogram pede sintaxe de tags com texto literal, Leonardo usa negative prompt, Bing gosta de linguagem natural. A skill conhece cada formato.
- **Recomendação automática.** A skill sugere a melhor ferramenta para o seu caso de uso.
- **Base nas Urgências Ocultas.** Todas as cenas saem do perfil real do produto ativo, nunca inventadas.

## Ferramentas Cobertas

| Ferramenta | Forte em | Link |
|---|---|---|
| **Whisk** | Personagem consistente entre várias imagens | labs.google/fx/tools/whisk |
| **ImageFX** | Qualidade fotográfica, luz natural | labs.google/fx/tools/image-fx |
| **Gemini** | Variações rápidas, edição conversacional | gemini.google.com |
| **Ideogram** | Texto dentro da imagem (headline, logo) | ideogram.ai |
| **Leonardo.ai** | Estilo artístico, controle de presets | leonardo.ai |
| **Bing Image Creator** | Ilustração criativa, DALL·E 3 grátis | bing.com/create |
| **Krea.ai** | Estética moderna, mockup, realtime | krea.ai |
| **Midjourney** | Qualidade artística premium, criativos de anúncio | midjourney.com |

## O Que Fazer

### 0. Contexto

Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md`. Se não existirem, oriente o aluno a rodar `/produto-concepcao` primeiro.

Extraia:
- Quadro (transformação principal)
- Nicho e público
- 3 Urgências Ocultas mais fortes (Dores, Desejos, Urgências Quentes)
- Identidade do Consumidor (tom, estética preferida, cultura visual)

### 1. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/6. Caso de uso:**

```
O que você quer criar?

1. Imagens para anúncios (Meta Ads, formato 1:1 ou 4:5)
2. Carrossel de Instagram (10 frames com personagem fixo)
3. Capa de produto (e-book, mockup, módulo de curso)
4. Imagem com headline escrita na própria imagem (texto grande)
5. Pacote completo (anúncios + carrossel + capa)

Digite o número:
```

```
... Bloco 1/6 concluído ...
Caso de uso: [escolha]
Próximo: Ferramenta
...
```

**Bloco 2/6. Ferramenta:**

Mostre a recomendação automática baseada no caso de uso:

- Caso 1 (anúncios): recomendar **Midjourney** (criativos premium) ou **ImageFX** (fotográfico gratuito).
- Caso 2 (carrossel com personagem fixo): recomendar **Whisk** (é a única que mantém personagem consistente).
- Caso 3 (capa de produto): recomendar **Midjourney** ou **Leonardo.ai** (estética premium).
- Caso 4 (headline na imagem): recomendar **Ideogram** (única que escreve texto sem erro).
- Caso 5 (pacote completo): recomendar **Whisk** para o carrossel + **Midjourney** ou **Ideogram** para as peças com texto.

```
Ferramenta recomendada para o seu caso: **[ferramenta]**
Motivo: [1 linha explicando]

Quer usar a recomendada ou outra?

1. [Recomendada] (recomendado)
2. Midjourney. Qualidade artística premium, criativos de anúncio
3. Whisk. Personagem consistente, 3 inputs visuais
4. ImageFX. Qualidade fotográfica, prompt de texto (gratuito)
5. Gemini. Variações rápidas, conversacional (gratuito)
6. Ideogram. Texto dentro da imagem
7. Leonardo.ai. Estilo artístico, presets
8. Bing Image Creator. DALL·E 3 grátis, ilustração criativa
9. Krea.ai. Estética moderna, mockup
10. Quero gerar para mais de uma ferramenta (escolha múltipla)

Digite o número:
```

Se o aluno escolher 9, liste as ferramentas com checkbox numerado e peça os números separados por vírgula.

```
... Bloco 2/6 concluído ...
Ferramenta(s): [escolha]
Próximo: Personagem
...
```

**Bloco 3/6. Personagem (Subject):**

```
Quem vai aparecer nas imagens?

1. Você mesmo (tenho foto minha)
2. Personagem fictício (pessoa com características específicas)
3. Objeto ou símbolo do produto (nada de pessoa)
4. Mão/silhueta (meio caminho, sem rosto)

Digite o número:
```

Se escolher 1: pergunte se a foto já existe em algum lugar e instrua a deixar ela em `meus-produtos/{ativo}/entregas/criativos/imagem-assets/subject.jpg`. Avise que só Whisk e Gemini aceitam upload de foto como referência.

Se escolher 2: faça perguntas curtas, UMA por vez:
- Idade aparente
- Gênero
- Estilo (ex: empresária moderna, mãe de família, atleta, místico, profissional corporativo)
- Traço marcante (ex: cabelo cacheado, óculos, tatuagem, barba)
- Etnia (opcional, se fizer diferença no nicho)

Se escolher 3 ou 4: pergunte qual objeto/símbolo representa o produto.

```
... Bloco 3/6 concluído ...
Subject: [descrição]
Próximo: Estética visual
...
```

**Bloco 4/6. Estética (Style):**

Baseado na identidade do consumidor, sugira 3 estéticas que combinam:

```
Qual estética visual?

1. [Estética A sugerida com base no perfil]
2. [Estética B sugerida]
3. [Estética C sugerida]
4. Outro (descreva)

Digite o número:
```

Sugestões possíveis:
- Foto de celular com luz natural (autêntica, funciona para anúncios)
- Editorial minimalista (capa de e-book premium)
- Ilustração flat colorida (carrossel educativo)
- Cinematográfica com cor quente (transformação/resultado)
- Documental preto e branco (autoridade)
- 3D render moderno (tech, SaaS)
- Pintura a óleo clássica (espiritual, místico)
- Retro anos 90 (nostalgia, gaming)

```
... Bloco 4/6 concluído ...
Style: [estética]
Próximo: Cenas
...
```

**Bloco 5/6. Cenas:**

Dependendo do caso de uso, determine quantas cenas precisam ser geradas:

- Anúncios: 3 cenas (gancho de dor, gancho de desejo, prova/resultado)
- Carrossel: 10 cenas, uma por slide (abertura, 3 dores, 3 quebras de objeção, transformação, CTA, encerramento)
- Capa: 1 cena principal + 2 variações para módulos
- Headline na imagem: 3 cenas (cada uma com uma headline diferente)
- Pacote completo: soma dos anteriores

Gere as descrições de cena automaticamente a partir das Urgências Ocultas do perfil. Não pergunte cena por cena. Mostre as cenas prontas:

```
Gerei [N] cenas baseadas nas Urgências Ocultas do seu perfil:

1. [Nome da cena]. [descrição visual em português]
2. [Nome da cena]. [descrição visual em português]
...

1. Aprovar as cenas
2. Quero ajustar alguma
```

**Bloco 6/6. Texto na imagem:**

Só aparece se caso de uso for 4 (headline) ou se o aluno pediu explicitamente. Caso contrário, pule esta etapa.

```
Qual headline vai aparecer na imagem?
(ex: "Chega de amanhecer cansado", "O método que usei em 2026")

Digite o texto exato:
```

Se a ferramenta escolhida não for Ideogram, avise: "Aviso. Só o Ideogram escreve texto sem erro. As outras ferramentas vão gerar texto com letras trocadas. Recomendo fazer overlay de texto no Canva depois."

```
... Bloco 6/6 concluído ...
Caso de uso: [caso]
Ferramenta: [ferramenta]
Subject: [subject]
Style: [style]
Cenas: [N cenas]
Texto: [opção]
...
```

### 2. Confirmação

```
Resumo do que vou preparar:

- Caso de uso: [caso]
- Ferramenta(s): [ferramenta]
- Personagem: [subject]
- Estética: [style]
- Cenas: [N cenas baseadas em Urgências Ocultas]
- Texto na imagem: [opção]

Vou entregar:
1. Arquivo {ferramenta}-prompts.md com todos os prompts no formato nativo da ferramenta
2. Instruções passo a passo de como usar no site
3. Estrutura de pastas para salvar as imagens geradas

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração do Briefing

Crie o arquivo `meus-produtos/{ativo}/entregas/criativos/{ferramenta}-prompts.md` usando o formato correto da ferramenta escolhida.

Se o aluno escolheu mais de uma ferramenta, crie um arquivo para cada uma.

---

#### Formato 1. Whisk (3 inputs visuais: Subject + Scene + Style)

```markdown
# Whisk. Prompts Visuais

Produto: {nome}
Caso de uso: {caso}
Data: {data}

## Como Usar

1. Acesse https://labs.google/fx/tools/whisk
2. Faça login com conta Google
3. Na tela inicial você verá 3 boxes: **Subject**, **Scene**, **Style**
4. Para cada box, você tem duas opções: upload de imagem OU clicar em "Describe" e colar o texto
5. Para cada cena abaixo, troque apenas o Scene. Mantenha Subject e Style idênticos entre as cenas.

## Subject (fixo em todas as cenas)

Cole no box "Subject" (ou suba uma foto):
```
{descrição do personagem, em inglês, máximo 2 frases, foco em aparência física e postura}
```

## Style (fixo em todas as cenas)

Cole no box "Style":
```
{descrição da estética, em inglês, máximo 2 frases, foco em tipo de foto/ilustração, iluminação e paleta}
```

## Cenas

### Cena 1. {nome da cena}

Urgência Oculta usada: {item exato do perfil}

Cole no box "Scene":
```
{descrição da cena, em inglês, 2 a 3 frases, ação e ambiente, sem repetir o Subject}
```

Conceito: {o que a imagem vai comunicar}
Onde usar: {ex: anúncio de descoberta, slide 1}
Salvar como: meus-produtos/{ativo}/entregas/criativos/whisk-{caso}-01.png

---

### Cena 2. {nome}
... (repetir estrutura)
```

---

#### Formato 2. ImageFX (prompt único de texto descritivo)

```markdown
# ImageFX. Prompts Descritivos

Produto: {nome}
Caso de uso: {caso}

## Como Usar

1. Acesse https://labs.google/fx/tools/image-fx
2. Faça login com conta Google
3. Cole o prompt no campo principal
4. Use os chips sugeridos pelo ImageFX para refinar estilo
5. Gere 4 variações por prompt

## Prompts

### Imagem 1. {nome}

Urgência Oculta: {item}

Prompt (em inglês):
```
{prompt descritivo único, 3 a 5 frases, incluindo: quem/o quê + ação + ambiente + estilo/iluminação + detalhes visuais + cor dominante}
```

Chips recomendados para clicar depois de colar:
- {estilo, ex: "Photorealistic"}
- {iluminação, ex: "Golden hour"}
- {câmera, ex: "35mm"}

Salvar como: meus-produtos/{ativo}/entregas/criativos/imagefx-{caso}-01.png
```

---

#### Formato 3. Gemini (prompt conversacional)

```markdown
# Gemini. Prompts Conversacionais

Produto: {nome}

## Como Usar

1. Acesse https://gemini.google.com
2. Comece com "Gere uma imagem de..." seguido do prompt
3. Para variar, diga: "Faça outra versão, agora com [mudança]"
4. Para editar, envie a imagem e diga o que mudar

## Prompts

### Imagem 1. {nome}

Prompt inicial (em português, conversacional):
```
Gere uma imagem realista de {descrição completa}. A iluminação é {tipo}, a composição é {descrição}, e o clima geral é {sensação}. Formato {1:1 / 4:5 / 16:9}.
```

Refinamentos possíveis (envie depois da primeira imagem):
- "Deixa a luz mais quente"
- "Tira o fundo e coloca {outro fundo}"
- "Faz a pessoa sorrindo"
```

---

#### Formato 4. Ideogram (tags + texto literal entre aspas)

```markdown
# Ideogram. Prompts com Texto Literal

Produto: {nome}

## Como Usar

1. Acesse https://ideogram.ai
2. Cole o prompt no campo
3. Escolha o Aspect Ratio ({1:1 / 4:5})
4. Escolha o Style: Auto, Realistic, Design, 3D ou Anime
5. Gere. O Ideogram escreve o texto literal entre aspas sem erros.

## Prompts

### Imagem 1. {nome}

Headline na imagem: "{texto exato}"

Prompt (em inglês):
```
{descrição visual em inglês}, with the text "{HEADLINE EXATA EM MAIÚSCULAS}" written in {fonte/estilo do texto, ex: "bold sans-serif white font"}, {estilo geral: editorial, poster, advertisement}, {iluminação}, {paleta de cores}, high quality, detailed
```

Style sugerido: {Realistic / Design / 3D}
Aspect Ratio: {1:1 para feed, 4:5 para anúncio, 9:16 para stories}

Salvar como: meus-produtos/{ativo}/entregas/criativos/ideogram-{caso}-01.png
```

---

#### Formato 5. Leonardo.ai (prompt + negative prompt + preset)

```markdown
# Leonardo.ai. Prompts com Controle de Estilo

Produto: {nome}

## Como Usar

1. Acesse https://leonardo.ai e faça login
2. Clique em "Image Generation"
3. Modelo recomendado: **Phoenix** ou **Leonardo Lightning XL**
4. Preset Style: {escolhido abaixo}
5. Cole o prompt principal no campo superior
6. Cole o negative prompt no campo "Negative Prompt"
7. Gere (cada geração usa tokens grátis do dia, reseta a cada 24h)

## Prompts

### Imagem 1. {nome}

Modelo: Phoenix
Preset Style: {Cinematic / Dynamic / Portrait / Illustration}
Aspect Ratio: {1:1 / 4:5}

Prompt principal (em inglês):
```
{descrição detalhada em inglês, 4 a 6 frases, incluindo subject, ação, ambiente, iluminação, câmera, estilo, qualidade}
```

Negative prompt (sempre o mesmo):
```
blurry, low quality, distorted, deformed hands, extra fingers, watermark, text errors, bad anatomy, duplicate, ugly
```

Salvar como: meus-produtos/{ativo}/entregas/criativos/leonardo-{caso}-01.png
```

---

#### Formato 6. Bing Image Creator (linguagem natural, DALL-E 3)

```markdown
# Bing Image Creator. Prompts em Linguagem Natural

Produto: {nome}

## Como Usar

1. Acesse https://bing.com/create
2. Faça login com conta Microsoft
3. Cole o prompt em inglês ou português (DALL-E 3 entende os dois)
4. Gera 4 imagens por vez
5. Cada conta ganha ~15 "boosts" diários para geração rápida

## Prompts

### Imagem 1. {nome}

Prompt (em inglês, estilo descritivo natural):
```
A {estilo, ex: photorealistic / digital illustration} of {subject detalhado}, {ação}, in {ambiente}, {iluminação}, {composição e câmera}, {paleta de cores}, {clima emocional}, high resolution, award winning
```

Salvar como: meus-produtos/{ativo}/entregas/criativos/bing-{caso}-01.png
```

---

#### Formato 7. Krea.ai (prompt + referência visual opcional)

```markdown
# Krea.ai. Prompts Estética Moderna

Produto: {nome}

## Como Usar

1. Acesse https://krea.ai e faça login
2. Clique em "Generate" > "Image"
3. Modelo recomendado: **Flux** (tier free tem ~30 gerações/dia)
4. Cole o prompt no campo principal
5. Se quiser referência de estilo, suba uma imagem no slot "Style Reference"

## Prompts

### Imagem 1. {nome}

Modelo: Flux
Aspect Ratio: {1:1 / 4:5}

Prompt (em inglês):
```
{descrição visual detalhada em inglês, foco em estética moderna, mockup, produto, lifestyle, 4 a 6 frases}
```

Style reference opcional: {suba uma imagem do Pinterest com a estética desejada}

Salvar como: meus-produtos/{ativo}/entregas/criativos/krea-{caso}-01.png
```

---

#### Formato 8. Midjourney (prompt com parâmetros nativos)

```markdown
# Midjourney. Prompts Premium para Criativos

Produto: {nome}
Caso de uso: {caso}

## Como Usar

1. Acesse discord.com e entre no servidor do Midjourney (ou use midjourney.com se tiver acesso web)
2. No canal de geração, use o comando `/imagine` seguido do prompt
3. Parâmetros essenciais já incluídos em cada prompt abaixo
4. Após gerar, clique em U1-U4 para fazer upscale da variação preferida
5. Para variar: clique em V1-V4 para gerar variações daquela versão

## Referência de Parâmetros

| Parâmetro | Função | Exemplo |
|---|---|---|
| `--ar` | Aspect ratio | `--ar 1:1` (feed), `--ar 4:5` (anúncio), `--ar 9:16` (stories) |
| `--v 6.1` | Versão mais recente | Sempre usar |
| `--style raw` | Menos estilização, mais fotorrealismo | Para fotos de produto/pessoa |
| `--q 2` | Qualidade máxima | Usar nos finais |
| `--no` | Negative prompt (o que evitar) | `--no text, watermark, blurry` |
| `--s` | Stylize (0-1000) | `--s 200` para equilíbrio |

## Prompts

### Imagem 1. {nome da cena}

Urgência Oculta: {item exato do perfil}
Tipo de anúncio Mandala: {ex: Prova Social, Revelação, Contraste}

Prompt (em inglês, com parâmetros):
```
{descrição detalhada da cena em inglês: subject + ação + ambiente + iluminação + estilo fotográfico + paleta de cores + mood emocional}, {referência de estilo se aplicável, ex: "shot on Sony A7, 85mm lens, golden hour"}, professional advertising photography, high-end commercial, ultra-detailed --ar {ratio} --v 6.1 --style raw --s 250 --no text, watermark, logo, blurry, distorted
```

Conceito: {o que a imagem comunica e qual Urgência Oculta trabalha}
Onde usar: {ex: anúncio de descoberta no feed, slide 1 do carrossel}
Variações recomendadas: {ex: "U2 e U4 costumam ter o melhor enquadramento"}
Salvar como: meus-produtos/{ativo}/entregas/criativos/midjourney-{caso}-01.png

---

### Imagem 2. {nome}

... (repetir estrutura)
```

**Regra Midjourney — especificidade máxima:**
Prompts curtos geram resultados genéricos. Use no mínimo 40 palavras de descrição antes dos parâmetros. Quanto mais específico o cenário (ambiente, luz, câmera, mood), melhor o resultado.

**Para carrossel com identidade visual consistente:**
Defina um "seed" após gerar a primeira imagem (botão de envelope no resultado) e use `--seed [número]` nas demais cenas para manter coerência visual entre os slides.

---

### Regras para TODOS os prompts gerados

- Todos os prompts de descrição visual em **inglês** (modelos respondem melhor).
- Não usar travessão em nenhum lugar do arquivo, nem nas instruções em português, nem nos prompts em inglês (use vírgula ou ponto).
- Subject e Style precisam ser idênticos entre cenas da mesma ferramenta (garantia de consistência visual).
- Nunca inventar dor ou desejo. Cada cena deve citar a Urgência Oculta exata do perfil que a inspirou.
- Nunca pedir texto dentro da imagem, exceto no Ideogram (única que escreve sem erro).
- Paleta de cores deve respeitar a identidade visual do consumidor (se o produto for místico, use tons terrosos e dourados; se for corporativo, azul e cinza; etc).

### 4. Aprovação

Mostre o conteúdo completo do arquivo ao usuário:

```
1. Aprovar e salvar
2. Quero ajustar algo
```

Após aprovação, salve o arquivo e crie a pasta `meus-produtos/{ativo}/entregas/criativos/imagem-assets/` (se ainda não existir) com um README.md explicando:
- subject.jpg. foto do personagem (se for foto real, para Whisk ou Gemini)
- style-ref.jpg. referência de estética opcional (para Krea)
- Imagens geradas vão para a pasta pai com o nome indicado em cada cena

### 5. Entrega e Próximo Passo

```
Prompts prontos.

Salvei em:
- meus-produtos/{ativo}/entregas/criativos/{ferramenta}-prompts.md
- meus-produtos/{ativo}/entregas/criativos/imagem-assets/ (pasta para suas referências)

Próximo passo:

1. Abra o site da ferramenta: {link}
2. Siga a seção "Como Usar" do arquivo
3. Para cada cena, cole o prompt correspondente
4. Baixe as imagens e salve em meus-produtos/{ativo}/entregas/criativos/ com o nome indicado
5. Depois volte aqui e use:
   - /copy-anuncio. para escrever a copy dos anúncios que vão usar essas imagens
   - /copy-social. para montar o carrossel
   - /video-remotion. para jogar as cenas num vídeo
```

### 6. Modo Iterativo

Se o usuário pedir para adicionar ou refinar cenas depois:

```
O que quer fazer?

1. Adicionar N cenas novas ao arquivo existente
2. Trocar a estética (Style) de todas as cenas
3. Trocar o personagem (Subject) de todas as cenas
4. Refinar uma cena específica
5. Gerar o mesmo briefing para outra ferramenta
```

Ajuste apenas a parte solicitada e atualize o arquivo, mantendo a numeração coerente.

## Regras

- Sempre usar as Urgências Ocultas reais do perfil como base das cenas. Nunca inventar dor ou desejo que não está lá.
- Subject e Style precisam ser idênticos em todas as cenas do mesmo briefing. Essa é a razão de usar esta skill.
- Não usar travessão em lugar nenhum do arquivo.
- Não gerar texto dentro das imagens, exceto se a ferramenta escolhida for Ideogram.
- Não prometer que as ferramentas têm API. O fluxo é manual: cola no site e baixa.
- Adaptar o prompt ao formato nativo de cada ferramenta (Whisk visual, ImageFX descritivo, Ideogram com tags e aspas, Leonardo com negative prompt, etc).
- Quando o aluno escolhe múltiplas ferramentas, gere um arquivo por ferramenta, não um arquivo único misturado.
