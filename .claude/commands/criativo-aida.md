---
name: workshop-marketing:criativo-aida
description: Gera um criativo de anuncio em imagem com base no AIDA. 3 passos sequenciais: imagem de fundo (Atencao), layout e cores (Interesse e Desejo), texto da imagem (Acao). Entrega um prompt consolidado em ingles pronto para colar na ferramenta de imagem escolhida.
allowed-tools: Read, Write, Bash
---

# Criativo AIDA. Anuncio em Imagem em 3 Passos

Gera o criativo completo dividido em 3 passos sequenciais baseados no AIDA.
Cada passo e validado antes de avancar para o proximo.

**Por que 3 passos separados:**
A maioria dos criativos falha porque o texto e escrito antes do layout ser definido.
O texto nao cabe na composicao, o visual nao reforca a mensagem, o botao some no fundo.
Este fluxo inverte: primeiro a imagem que para o scroll, depois onde cada coisa fica, depois o texto que cabe naquele espaco.

## Usage

```
/criativo-aida
```

## O Que Fazer

### 0. Contexto

Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e
`meus-produtos/{ativo}/idconsumidor.md` (se existir).

Extraia:
- Quadro (transformacao principal)
- Nicho e publico
- Top 5 Urgencias Ocultas mais fortes (priorizando Dores, Desejos e Urgencias Quentes)
- Identidade do Consumidor (estetica, tom, cultura visual se disponivel)

### 1. Entrevista (3 perguntas, UMA por vez)

**Pergunta 1/3. Formato:**

```
Qual formato de imagem?

1. Feed retrato (4:5, 1080x1350). mais espaco na tela, melhor para feed
2. Quadrado (1:1, 1080x1080). classico, funciona em tudo
3. Stories ou Reels (9:16, 1080x1920). tela cheia vertical

Digite o numero:
```

**Pergunta 2/3. Urgencia base:**

Liste as top 5 urgencias ocultas do perfil numeradas. Apresente assim:

```
Qual situacao vai inspirar o criativo?
(escolha a que mais ressoa com o momento de compra)

1. [Urgencia 1 exata do perfil]
2. [Urgencia 2 exata do perfil]
3. [Urgencia 3 exata do perfil]
4. [Urgencia 4 exata do perfil]
5. [Urgencia 5 exata do perfil]

Digite o numero:
```

**Pergunta 3/3. Ferramenta de imagem:**

```
Onde vai gerar a imagem de fundo?

1. Gemini. gratuito, conversacional, facil de iterar
2. ImageFX. gratuito, Google, otimo para fotorrealismo
3. Ideogram. gratuito, unico que escreve texto sem erro
4. Leonardo.ai. gratuito com limite diario, controle de estilo
5. Midjourney. qualidade premium, precisa de conta paga
6. Outra ferramenta (diga qual)

Digite o numero:
```

```
--- Entrevista concluida ---
Formato: [formato]
Urgencia base: [urgencia escolhida]
Ferramenta: [ferramenta]
Proximo: Passo 1 de 3 (imagem de fundo)
---
```

### 2. Passo 1 de 3: Imagem de Fundo (Atencao)

**Objetivo:** gerar a imagem de fundo que para o scroll.
Sem texto. Sem botao. Apenas o visual que cria impacto emocional imediato.

**Logica de construcao:**

A urgencia oculta escolhida mapeia para uma categoria visual:

| Categoria de urgencia | Direcao visual |
|---|---|
| Dor fisica ou emocional | Cena de tensao, espaco apertado, luz dura, tons frios |
| Desejo de resultado | Cena de conquista, luz quente, espaco aberto, postura confiante |
| Urgencia quente (evento proximo) | Cena de tempo passando, contraste claro/escuro, movimento |
| Urgencia fria (acumulo de tempo) | Cena estatica, peso visual, tons neutros, composicao pesada |
| Urgencia inusitada | Cena de contraste inesperado, elemento fora de lugar, curiosidade |

**Regras do prompt de fundo:**
- Sempre em ingles
- Descrever composicao primeiro (o que esta em primeiro plano, angulo)
- Iluminacao especificada explicitamente
- Referencia de camera/lente para fotorrealismo (ex: "shot on Sony A7, 85mm")
- Mood emocional no final
- Sem rostos completos e visiveis (usar silhueta, costas, maos, detalhe de corpo)
- Sujeito humano SEMPRE vestido de forma adequada para anuncios de midia social. Especificar a roupa no prompt (ex: "wearing a bikini", "in a dress", "in casual clothes"). Nunca omitir a vestimenta.
- Sem texto, logo ou watermark na cena
- Negative prompt separado quando a ferramenta suportar

**Estrutura interna do prompt (referencia para construcao):**

```
[Composicao: o que esta em cena e angulo], [sujeito sem rosto ou silhueta],
[acao ou estado], [ambiente e contexto], [iluminacao: tipo, direcao, temperatura],
[referencia de camera se fotorrealista], [paleta de cor dominante],
[mood emocional final]. --no text, faces, watermark, logo
```

**Adaptar para a ferramenta escolhida:**

- Midjourney: adicionar `--ar [ratio] --v 6.1 --style raw --s 250 --no text, faces, watermark`
- ImageFX: prompt descritivo, 4 a 6 frases, sem parametros tecnicos
- Ideogram: adicionar ao final `Style: Realistic, Aspect Ratio: [ratio]`
- Leonardo.ai: prompt principal + negative prompt separado em campo proprio
- Gemini: iniciar com "Gere uma imagem realista de..." em portugues

**Gere 3 opcoes de imagem de fundo:**

- Opcao A: mais alinhada com a dor (tom pesado, tensao)
- Opcao B: mais alinhada com o desejo (tom leve, aspiracional)
- Opcao C: composicao ousada (angulo incomum, contraste forte)

**IMPORTANTE: apresente a descricao da cena em portugues ANTES do prompt em ingles.**
O usuario precisa entender o que vai ver antes de ler o codigo tecnico.

Apresente as 3 opcoes assim:

```
Passo 1 de 3: imagem de fundo

Escolha a cena que vai parar o scroll:

Opcao A. [nome descritivo em portugues]:
Cena: [descricao visual em portugues, 2 a 3 frases. O que aparece, o angulo, a luz,
o mood. Como se voce estivesse descrevendo um quadro para alguem que nao pode ver.]
Prompt para [ferramenta]:
```[prompt em ingles com parametros da ferramenta]```

Opcao B. [nome descritivo em portugues]:
Cena: [descricao visual em portugues, 2 a 3 frases]
Prompt para [ferramenta]:
```[prompt em ingles]```

Opcao C. [nome descritivo em portugues]:
Cena: [descricao visual em portugues, 2 a 3 frases]
Prompt para [ferramenta]:
```[prompt em ingles]```

---
1. Usar Opcao A
2. Usar Opcao B
3. Usar Opcao C
4. Quero ajustar uma das opcoes
```

Apos aprovacao, avance para o Passo 2.

### 3. Passo 2 de 3: Layout e Cores (Interesse e Desejo)

**Objetivo:** definir onde cada elemento vai ficar e como vai se parecer.
Esta etapa acontece ANTES de escrever o texto para que as palavras sejam escritas
dentro dos limites reais do espaco disponivel.

**Logica de construcao do layout:**

O layout cria uma hierarquia visual que guia o olho na sequencia:
1. Imagem de fundo capta a atencao (Passo 1)
2. Titulo gera interesse em menos de 2 segundos
3. Apoio cria desejo aprofundando o beneficio
4. Botao converte o desejo em acao

**Zonas padrao por formato:**

ATENCAO: o Meta Ads sobrepoe na base da imagem o nome do anunciante e o botao nativo
("Saiba mais"). Essa sobreposicao ocupa aproximadamente os ultimos 10-12% da imagem.
Todos os elementos do criativo (apoio, botao, instrucao de clique) devem estar
posicionados acima dessa zona, com folga de pelo menos 10% extra no rodape para
nao colidir com a UI nativa da plataforma.

Para feed retrato (4:5, 1080x1350):
- Zona A (topo, 15-20%): kicker + titulo
- Zona B (centro, 50-55%): imagem de fundo domina, espaco negativo estrategico
- Zona C (base, 20%): apoio linha 1 + apoio linha 2 + botao + instrucao de clique
- Zona D (rodape, 10-12%): VAZIA — reservada para sobreposicao nativa do Meta

Para quadrado (1:1, 1080x1080):
- Zona A (topo, 20%): titulo
- Zona B (centro, 55%): imagem de fundo
- Zona C (base, 25%): apoio + botao

Para stories/reels (9:16, 1080x1920):
- Zona A (topo, 20%): titulo grande
- Zona B (centro, 50%): imagem de fundo
- Zona C (base, 30%): apoio + botao + safe zone de 14% embaixo

**Derivar paleta a partir do perfil:**

| Nicho | Paleta recomendada |
|---|---|
| Saude e bem-estar feminino | Verde-sage (#4a7c59), branco (#FFFFFF), dourado suave (#c9a84c) |
| Financas e renda | Azul escuro (#1a2b4a), dourado (#c9a84c), branco (#FFFFFF) |
| Espiritualidade e autoconhecimento | Roxo escuro (#2d1b4e), dourado (#c9a84c), creme (#f5efe6) |
| Educacao e carreira | Azul royal (#2b4acb), branco (#FFFFFF), laranja (#f97316) |
| Emagrecimento | Verde (#2d6a4f), branco (#FFFFFF), coral (#f4845f) |
| Relacionamentos | Rosa queimado (#c2667a), off-white (#faf7f5), bege (#d4b896) |

Se o produto nao se encaixar em nenhuma categoria, usar as cores da Identidade do Consumidor do perfil.

**Apresente o layout ao usuario assim:**

```
Passo 2 de 3: layout e cores

Formato: [formato] | [dimensoes]
Cena escolhida: [nome da opcao do Passo 1]

POSICIONAMENTO DO TEXTO (direto sobre a foto, sem retangulos de fundo):
Kicker (acima do titulo, topo da imagem):
  Estilo: sans-serif fino, caixa alta ou itálico leve, menor que o titulo
  Cor: #FFFFFF com sombra densa (dark drop shadow, charcoal, blur suave)
  Funcao: cria contexto antes do punch do titulo (ex: situacao, tempo, perfil)
  Limite: [numero] caracteres

Titulo (logo abaixo do kicker):
  Estilo: bold sans-serif moderno, letras bem definidas, levemente espacadas
  Cor: warm white com acento [cor hex destaque] em 1 palavra-chave
  Limite: [numero] caracteres

Apoio linha 1 (base da imagem, acima do botao):
  Estilo: sans-serif semi-bold, destaque do dado concreto (numero, prazo, resultado)
  Cor: #FFFFFF com halo escuro difuso largo
  Limite: [chars] caracteres

Apoio linha 2 (imediatamente abaixo da linha 1):
  Estilo: sans-serif regular, clean, levemente menor que a linha 1
  Cor: #FFFFFF com halo escuro difuso largo
  Limite: [chars] caracteres

Botao CTA (flutuante, sem banda de fundo):
  Fundo: [hex] | Texto: #FFFFFF bold
  Estilo: pill shape arredondado, sombra leve embaixo (box shadow suave)
  Limite: [chars] caracteres

Instrucao de clique (rodape, abaixo do botao):
  Estilo: alinhado a esquerda, icone de cursor (mao clicando) + texto em dois tons
  Texto principal: cinza claro (#BBBBBB ou similar), regular, pequeno
  Destaque: o nome do botao CTA entre aspas, em #FFFFFF bold
  Formato: [icone cursor] Clique em "[nome do botao]" e [complemento curto]
  Exemplo: [cursor] Clique em "Saiba mais" e veja como funciona

TIPOGRAFIA VISUAL (descricao para o gerador de imagem, nao nome de fonte):
  Kicker: "small thin uppercase white text, subtle dark drop shadow, above the headline"
  Titulo: "clean bold modern warm white text (soft warm white, not pure #FFFFFF), strong dark charcoal drop shadow for depth, with a warm [cor] accent on 1 key word"
  Apoio linha 1: "clean semi-bold white text, wide-spread diffused dark halo shadow, large blur radius, soft semi-transparent black behind letters (20-30% opacity, very light and airy)"
  Apoio linha 2: "lighter clean regular white text, same wide-spread diffused dark halo shadow, soft opacity"
  Botao: "rounded pill button in [hex], bold white text, soft bottom shadow"
  Instrucao de clique: "small left-aligned text at the very bottom: a hand cursor tap icon followed by light gray text, with the CTA name in bold white inside quotes"

---
1. Aprovar e seguir para o texto
2. Quero ajustar algo
```

Apos aprovacao, avance para o Passo 3.

### 4. Passo 3 de 3: Texto da Imagem (Acao)

**Objetivo:** escrever o texto exato de cada zona definida no Passo 2.
O texto e escrito para caber no espaco real, nao o contrario.

**Regras de texto interno (Light Copy aplicada a imagem):**

- Kicker: afirmacao curta de contexto ou situacao. Sem exclamacao, sem pergunta.
- Kicker: fala sobre o estado atual do leitor, nao sobre o produto
- Titulo: sem ponto de exclamacao, sem pergunta, sem travessao
- Titulo: dado concreto ou afirmacao direta (nunca promessa vaga)
- Kicker + Titulo: escrito como par. O kicker nomeia a situacao ou tensao exata que o leitor esta vivendo. O titulo entrega a resolucao com dado concreto. O titulo deve responder diretamente ao kicker, nao ser independente. Exemplo: Kicker "Verao chegando e o biquini parado na gaveta" entao Titulo "8 kg em 12 semanas muda esse cenario". Exemplo: Kicker "Mais um dia sem energia pra terminar o trabalho" entao Titulo "Quem reorganizou o sono perdeu 7 kg em 8 semanas". Regra pratica: se voce cobrir o titulo e o kicker ainda fizer sentido sozinho, o par nao esta funcionando.
- Apoio linha 1: o dado concreto isolado (numero, prazo, resultado especifico)
- Apoio linha 2: o argumento ou complemento da linha 1 (o "como" ou "sem X")
- Botao: preferir "Saiba mais" como padrao. Funciona como CTA nativo do Meta e nao entrega que e um anuncio de venda. Usar outra opcao apenas se houver razao forte e especifica.
- Instrucao de clique: SEMPRE gerar o complemento completo, nunca deixar como placeholder. O complemento e uma frase de curiosidade ou desejo que conecta com o kicker ou o titulo. Comeca com "e" (conectivo suave). Usa verbo de descoberta: "veja", "descubra", "entenda", "confira". Nao menciona "curso", "treinamento", "compra". Pode ter 1 ou 2 linhas. Max 55 chars. Exemplos: "e veja com os seus proprios olhos o porque", "e descubra o que muda nas primeiras 2 semanas", "e entenda por que tantas pessoas estao conseguindo".
- Nenhuma zona pode ter texto que nao caiba no limite de caracteres do Passo 2

**Logica AIDA para o texto:**

- Passo 1 (visual) cumpriu ATENCAO
- Passo 2 (layout) define onde INTERESSE e DESEJO vao aparecer
- Passo 3 (texto): kicker cria identificacao, titulo entrega INTERESSE, apoio cria DESEJO, botao converte em ACAO

**Gere 2 versoes completas do anuncio**, cada uma com kicker, titulo, apoio (2 linhas) e botao ja combinados.
Nao apresentar opcoes separadas por zona. O usuario escolhe a versao inteira.

Apresente assim:

```
Passo 3 de 3: texto da imagem

Versao 1:
Kicker (max [N] chars): "[kicker 1]" ([N] chars)
Titulo (max [N] chars): "[headline 1]" ([N] chars)
Apoio linha 1 (max [N] chars): "[dado concreto 1]" ([N] chars)
Apoio linha 2 (max [N] chars): "[complemento 1]" ([N] chars)
Botao: "[CTA 1]"
Instrucao de clique: Clique em "[CTA 1]" e [complemento curto]

Versao 2:
Kicker (max [N] chars): "[kicker 2]" ([N] chars)
Titulo (max [N] chars): "[headline 2]" ([N] chars)
Apoio linha 1 (max [N] chars): "[dado concreto 2]" ([N] chars)
Apoio linha 2 (max [N] chars): "[complemento 2]" ([N] chars)
Botao: "[CTA 2]"
Instrucao de clique: Clique em "[CTA 2]" e [complemento curto]

---
1. Usar Versao 1
2. Usar Versao 2
3. Quero ajustar algo
```

Apos o usuario escolher, monte o prompt final consolidado.

### 5. Confirmacao e Entrega

Apos o usuario confirmar a versao do Passo 3, monte o PROMPT FINAL CONSOLIDADO em ingles.
Este e o unico output que o aluno precisa para gerar o criativo. Um prompt unico que combina os 3 passos.

**Estrutura do prompt final consolidado (sempre em ingles):**

REGRA CRITICA: usar linguagem visual espacial (upper area, lower band, centered),
NUNCA porcentagens numericas. Porcentagens sao apenas para calculo interno no Passo 2.
O modelo de imagem nao deve renderizar nenhuma anotacao de layout.

```
Generate a complete [plataforma] ad image ([dimensoes]px).

SCENE: [descricao visual completa do Passo 1 em ingles,
com o sujeito vestido de forma adequada para anuncios de midia social.]
The top 20% of the image must be naturally dark (shadows, curtains,
overcast sky) for text legibility. The bottom 30% must fade into a
deep dark vignette (near-black gradient). Leave the very bottom 10%
completely clear and uncluttered — Meta Ads overlays the advertiser
name and native CTA button there and all creative elements must stay
above that zone.

TEXT ON PHOTO (no background bands, no colored rectangles):
- Top of the image, above the headline: small thin uppercase white
  sans-serif text, subtle dark drop shadow, centered:
  "[kicker do Passo 3]"
- Just below the kicker: clean bold modern warm white sans-serif text,
  slightly expanded letter-spacing, with the key word "[palavra-chave]"
  in [cor hex destaque], strong dark charcoal drop shadow with soft
  blur for depth, centered: "[titulo do Passo 3]"
- Bottom of the image (over the dark vignette): clean semi-bold white
  sans-serif text, wide-spread diffused dark halo shadow, large blur
  radius, soft semi-transparent black behind letters (40-50% opacity,
  not fully opaque), centered:
  "[apoio linha 1 do Passo 3]"
- Immediately below: lighter clean regular white sans-serif text, same
  wide-spread diffused soft halo shadow, centered:
  "[apoio linha 2 do Passo 3]"
- Below it: a floating rounded pill-shaped [cor hex do botao] button,
  bold white text, soft bottom shadow for elevation: "[botao do Passo 3]"
- At the very bottom of the image, left-aligned: a small hand cursor
  tap icon followed by light gray (#BBBBBB) regular small sans-serif
  text reading: Clique em — then the CTA name "[botao do Passo 3]" in
  bold white — then the rest of the instruction in light gray:
  "[instrucao de clique do Passo 3]"

Style: professional Instagram ad, photorealistic, clean typography,
high resolution. Text floats directly over the photograph.
No background bands, no colored rectangles, no overlay boxes,
no percentage labels, no zone markers, no annotations.
```

Apresente assim ao usuario:

```
Pronto. Cole esse prompt no [ferramenta escolhida]:

[PROMPT CONSOLIDADO EM INGLES]

---
1. Aprovar e salvar
2. Quero ajustar algo
```

Apos aprovacao, salve dois arquivos:

**Arquivo 1: JSON completo**
`meus-produtos/{ativo}/entregas/criativos/criativo-aida-{slug}-{numero}.json`

```json
{
  "produto": "{ativo}",
  "criativo": "criativo-aida-{slug}-{numero}",
  "data": "{data}",
  "formato": "{formato}",
  "ratio": "{ratio}",
  "urgencia_base": "{urgencia escolhida}",
  "ferramenta_imagem": "{ferramenta}",
  "aida": {
    "atencao": {
      "passo": 1,
      "objetivo": "parar o scroll com visual emocional sem texto",
      "cena": "{descricao em portugues da opcao escolhida}",
      "prompt": "{prompt em ingles escolhido}",
      "parametros": "{parametros da ferramenta se aplicavel}"
    },
    "interesse_desejo": {
      "passo": 2,
      "zonas": {
        "zona_a": {
          "nome": "titulo",
          "altura_pct": 0,
          "fonte_familia": "",
          "fonte_peso": "",
          "cor_texto": "",
          "max_chars": 0
        },
        "zona_b": {
          "nome": "fundo",
          "altura_pct": 0,
          "overlay": "",
          "espaco_negativo": ""
        },
        "zona_c": {
          "nome": "apoio_botao",
          "altura_pct": 0,
          "apoio_max_chars": 0,
          "botao_max_chars": 0,
          "cor_fundo_botao": "",
          "cor_texto_botao": ""
        }
      },
      "paleta": {
        "texto_principal": "",
        "destaque": "",
        "overlay": ""
      }
    },
    "acao": {
      "passo": 3,
      "copy": {
        "titulo": "",
        "apoio": "",
        "botao": ""
      }
    }
  },
  "prompt_final": "{prompt consolidado em ingles pronto para colar}"
}
```

**Arquivo 2: Briefing legivel**
`meus-produtos/{ativo}/entregas/criativos/criativo-aida-{slug}-{numero}.md`

Conteudo:
- Nome do criativo, data, formato, urgencia base e ferramenta
- Cena escolhida (descricao em portugues)
- Prompt de fundo em bloco de codigo pronto para copiar
- Layout em topicos (divisao das zonas, fontes, cores)
- Texto escolhido (titulo, apoio, botao)
- Prompt final consolidado em ingles em bloco de codigo

### 6. Proximo Passo

Apos salvar:

```
Criativo salvo em:
- meus-produtos/{ativo}/entregas/criativos/criativo-aida-{slug}-{numero}.json
- meus-produtos/{ativo}/entregas/criativos/criativo-aida-{slug}-{numero}.md

Proximos passos:

1. Cole o prompt acima em [ferramenta] para gerar a imagem de fundo
2. Abra a imagem gerada no Canva e aplique o layout do Passo 2 como guia
3. Adicione o texto do Passo 3 em cada zona
4. Para criar mais variacoes: rode /criativo-aida novamente
5. Para escrever a copy do anuncio que acompanha a imagem: use /copy-anuncio
```

### 7. Modo Iterativo

Se o usuario quiser refinar um passo especifico depois de salvar:

```
Qual passo quer ajustar?

1. Passo 1: imagem de fundo (trocar a cena)
2. Passo 2: layout e cores (ajustar zonas, fontes ou paleta)
3. Passo 3: texto da imagem (titulo, apoio ou botao)

O que quer mudar?
```

Ajuste apenas o passo solicitado, atualize os dois arquivos mantendo os outros passos intactos.

## Regras

- Nao escrever texto antes do Passo 2 estar aprovado. O texto do Passo 3 depende dos limites de caractere definidos no layout.
- Nunca inventar urgencia. A urgencia base vem obrigatoriamente das Urgencias Ocultas do perfil.
- Prompt do Passo 1 sempre em ingles, adaptado ao formato nativo da ferramenta escolhida.
- Passo 2 sempre em JSON valido no arquivo salvo, mesmo que apresentado como texto para o usuario.
- Light Copy obrigatoria no Passo 3: sem travessao, sem ponto de exclamacao, sem pergunta, sem promessa vaga.
- O numero do criativo e sequencial dentro da pasta do produto. Verificar arquivos existentes antes de numerar.
- Apresentar SEMPRE a descricao da cena em portugues ANTES do prompt em ingles no Passo 1.
- Passo 3 gera SEMPRE 2 versoes completas (titulo+apoio+botao juntos), nunca opcoes isoladas por zona.
- Prompt final consolidado usa linguagem visual espacial (upper area, lower band, centered). NUNCA incluir porcentagens numericas. Porcentagens sao apenas para calculo interno do limite de caracteres no Passo 2.
- Sujeito humano no prompt do Passo 1 deve estar vestido de forma adequada para anuncios. Especificar a roupa explicitamente no prompt (ex: "wearing a bikini", "in a floral dress"). Nunca omitir a vestimenta.
- Botao CTA padrao e "Saiba mais". Nao usar "Ver o metodo", "Quero agora" ou qualquer CTA que entregue que e um anuncio de venda. "Saiba mais" se camufla como botao nativo do Meta e reduz resistencia do usuario.
