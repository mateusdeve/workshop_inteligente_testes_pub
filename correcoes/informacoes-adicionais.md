# Informações adicionais do projeto

Registro do que o usuário pediu ou esclareceu, para complementar a documentação principal do repositório.

---

## 2026-03-24

### Pedido: pasta de correções e registro contínuo

- Criar uma **pasta de correções** no projeto.
- **Guardar como informações a mais** no projeto tudo o que o usuário disser (orientações, preferências, correções), para referência futura.

*Nota para quem mantém este arquivo:* mensagens de conversas anteriores a esta sessão não foram transcritas aqui automaticamente; a partir desta data, novas falas do usuário sobre o projeto devem ser acrescentadas abaixo ou em novas entradas datadas.

### Fluxo: pesquisa de mercado após quadro, furadeira, decorados e urgências ocultas

Assim que estiver **finalizada a geração** de: **quadro**, **furadeira**, **decorados** e **urgências ocultas**, já deve ser feita a **pesquisa de mercado**, com entrega dos dados em **tabela** para sugestão de oferta e preço e para o **diferencial do produto**.

**Tabela única de concorrentes** (obrigatória), com as colunas:

| Coluna |
|--------|
| Nome concorrente |
| Link da página do concorrente |
| Promessa |
| Resumo das entregáveis |
| Bônus |
| Preço |

**Em seguida** (após essa tabela), entregar também:

- **Diferenciais** que o concorrente **não** tem e **qual diferencial** o nosso produto usa (posicionamento).
- **Sugestão de preço**.
- **Sugestão de oferta**.

### Objeções e Reclame Aqui

Para **criação de objeções**, deve ser feita também uma **pesquisa no Reclame Aqui** (reclamações relevantes ao nicho, concorrentes ou tipo de serviço/produto), para embasar objeções reais e respostas.

### Comunicação: evitar perguntas repetidas

- **Não fazer perguntas repetidas e redundantes** — antes de perguntar, usar o que já está em `meu-negocio/`, em `correcoes/` e no histórico da conversa; só perguntar o que ainda falta ou é ambíguo.

### Terminologia: não chamar de “persona”

- **“Persona”** no sentido de *identidade do consumidor* **não** deve ser o rótulo usado com o usuário nem nos entregáveis: essa identidade já está modelada nos prompts; o nome correto do artefato e do fluxo é **identidade do consumidor**.
- O **comando** deve ser **`/idconsumidor`**, não `/persona`.
- O arquivo gerado fica em **`meu-negocio/idconsumidor.md`** (não `persona.md`).

### Skill de página (`paginas`): copy antes do HTML e coleta antes da copy

- A skill de **página** deve **validar a copy com o usuário** antes de gerar o **HTML**.
- **Antes** de gerar a copy: tudo o que ainda **não tiver sido perguntado** (e que for necessário para a página) deve ser **perguntado** — **não** gerar copy (nem HTML) “direto” assumindo dados que não foram coletados ou confirmados.

### Skill de anúncio: fases do funil (definição correta)

Ao perguntar **“Qual fase?”**, a skill de **anúncio** deve usar **somente** estes significados (não confundir com descrições tipo “público frio”, “já segue”, “baixou isca”, “checkout abandonado” como definição principal):

| Fase | Significado correto |
|------|---------------------|
| **Descoberta** | Aumentar a base, aumentar seguidores |
| **Relacionamento** | Gerar relacionamento com a base |
| **Conversão** | Vender |
| **Remarketing** | Vender para quem **já viu a página** |

### Skill de anúncio: pesquisar virais antes de gerar copy de Descoberta

- **Antes de gerar qualquer anúncio de fase Descoberta**, a skill deve:
  1. Pesquisar os reels mais virais do Instagram com chamada para seguir (todos os nichos)
  2. Pesquisar os vídeos mais virais do TikTok com chamada para seguir (todos os nichos)
  3. Modelar a copy — tanto o **conteúdo** quanto o **tamanho** — com base nos padrões encontrados
- A estrutura obrigatória de todo anúncio de Descoberta é:
  - **GANCHO (0–3s):** para o scroll — hook forte, 1–2 frases
  - **O QUÊ (4–20s):** expande o problema ou a promessa
  - **O COMO (21–50s):** ensina a técnica com exemplo concreto
  - **CTA (51–60s):** convite leve para seguir o perfil
- Tamanho alvo: ~130 palavras por anúncio (equivalente a ~60 segundos de fala)
- Essa pesquisa deve ser feita a cada geração — não reutilizar pesquisa anterior

### Skill de anúncio: estrutura do texto principal deve ser explícita

- O **texto principal** de cada anúncio deve ter as seções **explicitamente rotuladas**:
  - **GANCHO:** — premissa que para o scroll
  - **DESENVOLVIMENTO:** — argumento que aprofunda
  - **CTA:** — convite direto adequado à fase do funil
- Não entregar o texto corrido sem identificar cada parte — o usuário precisa saber o que é cada elemento para usar na criação do criativo.

### Skill de anúncio: ordem correta das perguntas

- A skill `/anuncio` deve perguntar **nesta ordem** antes de gerar:
  1. **Objetivo** (captar leads, vender, engajamento, views)
  2. **Tipo(s) da Mandala** — deixar o usuário escolher os 3 tipos das 18 opções
  3. **Fase do funil** (Descoberta, Relacionamento, Conversão, Remarketing)
- Só depois de coletar essas três informações (e oferta, se fase for Conversão ou Remarketing) gerar os anúncios.
- **Não assumir os tipos da Mandala** — sempre perguntar e deixar o usuário escolher.
- **Sempre listar os 18 tipos da Mandala** para o usuário escolher — nunca sugerir ou assumir tipos por conta própria.

### Anúncio de Descoberta não precisa de oferta/promoção

- Na fase de **Descoberta**, **não perguntar sobre oferta ou promoção** — essa pergunta só faz sentido nas fases de Conversão e Remarketing.
- Na Descoberta, o foco é **gancho de conteúdo** baseado em urgências ocultas, com CTA leve (seguir, salvar, clicar para saber mais).
- Ajustar o fluxo da skill `/anuncio` para só perguntar sobre oferta quando a fase escolhida for **Conversão** ou **Remarketing**.

---

## 2026-03-24 — Sessão de revisão completa do comando `/anuncio`

### 1. Pergunta de plataforma removida

- A pergunta "Qual plataforma? (Meta / Google / Ambas)" foi **removida** do fluxo.
- O comando `/anuncio` é para **Meta Ads por padrão**. Não perguntar mais sobre plataforma.
- O nome do arquivo salvo passou a usar `anuncios-meta-[formato]-[objetivo]-[produto].md`.

---

### 2. Terminologia corrigida

| Termo antigo | Termo correto |
|---|---|
| "Funil" | **Mandala da Criatividade** |
| "Lançamento" | **Pico de Vendas** |
| "Fase do funil" | **Objetivo** (para perpétuo) ou **Fase do pico de vendas** |

---

### 3. Estrutura correta da Mandala da Criatividade

A Mandala tem **3 dimensões** que devem ser perguntadas separadamente:

**Objetivos (o que a campanha quer alcançar):**
| Objetivo | Definição |
|---|---|
| Descoberta | Atrair novas pessoas que ainda não conhecem o produto |
| Relacionamento | Criar conexão e autoridade com quem já segue |
| Conversão | Vender |
| RMKT | Converter quem já interagiu com a página de vendas |

**Momentos de Consumo (em que estágio o público está):**
| Momento | Definição |
|---|---|
| Prontidão | Está pronto para comprar |
| Urgência Oculta | Tem o problema, mas ainda não busca solução |
| Oportunidade | Público amplo, ainda não está pronto para comprar |

**18 Tipos de Anúncio:**
1. Comparação, 2. Problema/Solução, 3. Explicação, 4. Curiosidade, 5. Reflexão, 6. Certo/Errado, 7. Demonstração, 8. Procedimento, 9. Impacto Visual, 10. Oportunidade, 11. História, 12. Prova Social, 13. Clickbait, 14. Sensação, 15. Contraste, 16. Ensino, 17. Revelação, 18. Dilema

---

### 4. Fluxo de entrevista correto para Perpétuo

Perguntar **uma por vez**, nesta ordem:

1. Perpétuo ou Pico de Vendas?
2. Qual o objetivo? (Descoberta / Relacionamento / Conversão / RMKT)
3. Qual o momento de consumo? (Prontidão / Urgência Oculta / Oportunidade)
4. Qual o tipo de anúncio? (Imagem / Vídeo / Carrossel / Stories)
5. Resumo → confirmação → pode gerar

---

### 5. Descoberta de produtos no `/trocar-produto` — usar Glob, não `.ativo`

- O comando `/trocar-produto` deve descobrir todos os produtos varrendo a pasta `produtos/` com **Glob** (`produtos/*/perfil.md` e `produtos/*/`).
- O arquivo `.ativo` serve **somente** para marcar qual produto está ativo na listagem — nunca para descobrir quais produtos existem.
- Se o Claude usar só `.ativo` para montar a lista, exibirá apenas o produto ativo em vez de todos os cadastrados.

---

### 6. Fluxo de entrevista correto para Pico de Vendas

1. Perpétuo ou Pico de Vendas?
2. Qual fase? (Captura / Aquecimento / Lembrete / Venda / Remarketing)
3. **Se Captura ou Aquecimento:** nome do evento → promessa do evento → data do evento
4. **Se Venda ou Remarketing:** qual é a oferta?
5. Resumo → confirmação → pode gerar

---

### 6. Pesquisa de tendências obrigatória antes de gerar

Antes de escrever qualquer anúncio, fazer **2 buscas na web**:

**Busca 1 — Por formato:**

| Formato | Queries | O que extrair |
|---|---|---|
| Vídeo | `reels instagram virais [mês/ano]` + `tiktok trends [mês/ano]` | Estrutura dos 3 primeiros segundos, duração ideal, estilo de edição, tom, padrão de CTA |
| Imagem | `posts imagem instagram viral [mês/ano]` + `trending static ads instagram [mês/ano]` | Estilo visual, uso de texto, proporção, paleta, elemento que para o scroll |
| Carrossel | `carrossel instagram viral [mês/ano]` + `trending carousel instagram [mês/ano]` | Estrutura de slides, como começa/termina, progressão, continuidade visual, CTA final |

**Busca 2 — Por objetivo:**

| Objetivo | Queries | O que extrair |
|---|---|---|
| Descoberta | `como ganhar seguidores instagram [mês/ano]` + `conteudo que vira seguidor instagram [mês/ano]` | Gancho que atrai estranho, tema que converte em follow, CTA que gera seguidor |
| Relacionamento | `conteudo que gera comentarios instagram [mês/ano]` + `posts mais compartilhados instagram [mês/ano]` | O que faz comentar, compartilhar e salvar, tom que gera conversa |
| Conversão | `anuncio que converte instagram infoproduto [mês/ano]` + `copy anuncio link na bio [mês/ano]` | Estrutura de copy para clique, nível de prova social, CTA de conversão |
| RMKT | `remarketing anuncio instagram copy [mês/ano]` + `retargeting ad copy que converte [mês/ano]` | Abordagem para quem já viu, gatilhos, tom sem parecer perseguição |

**Após as buscas, calibrar 4 elementos nas variações:**
1. Formato do gancho — como os virais abrem nos primeiros 3 segundos
2. Estilo visual/edição — o que está funcionando esteticamente agora
3. Tom — o que está ressoando com esse objetivo
4. CTA — padrão de chamada que está gerando ação agora

O **conteúdo** (o que diz) segue VTSD + perfil do negócio. O **formato e estilo** (como diz) segue o que está funcionando agora.

---

### 7. Regra do gancho — NUNCA pergunta, NUNCA óbvio

- O gancho de todo anúncio deve ser uma **premissa não óbvia** — afirmação que surpreende quem já está no nicho.
- **NUNCA usar pergunta no gancho** (regra Light Copy).
- **NUNCA usar algo óbvio** para quem já está no universo do produto.

**Exemplos ERRADO:**
- "Você já sentiu dificuldade de [resultado do produto]?" ❌ (pergunta)
- "Você já se sentiu inseguro com [tema]?" ❌ (pergunta)
- "Aprender [tema] é difícil." ❌ (óbvio para quem está no nicho)

**Exemplos CERTO:**
- "Quem mais trava raramente é quem sabe menos." ✓ (contra-intuitivo)
- "O caminho mais rápido para travar é o que todo mundo ensina primeiro." ✓ (premissa não óbvia)
- "A parte mais difícil de [tema] é exatamente a que ninguém ensina." ✓ (revelação)

---

### 8. Aprovação antes de salvar — regra global

- Todo entregável (anúncio, texto, email, copy) deve ser **mostrado ao usuário** antes de salvar.
- Após mostrar, perguntar:
  ```
  1. Aprovar e salvar
  2. Quero ajustar algo
  ```
- **Só salvar após aprovação.**
- Exceção: páginas HTML — salvar direto e informar o caminho (mostrar código seria confuso).
- Esta regra está registrada no **CLAUDE.md** como Regra de Ouro nº 5 e no fluxo padrão como passo 5 (Aprovação).

---

### 9. Fluxo completo e numeração correta do `/anuncio`

```
1. Contexto       → ler meu-negocio/perfil.md e idconsumidor.md
2. Entrevista     → uma pergunta por vez, sem agrupar, com progresso visual
3. Pesquisa       → 2 buscas na web (formato + objetivo)
4. Geração        → 3 variações da Mandala da Criatividade (VTSD + tendências)
5. Aprovação      → mostrar conteúdo, aguardar ok do usuário
6. Salvar         → somente após aprovação
7. Próximo passo  → sugerir comando seguinte
```

---

## 2026-03-27 — Novo comando `/zerar-negocio`

### Comando criado: `/zerar-negocio`

- Novo comando adicionado ao sistema para **zerar o `perfil.md` e/ou `idconsumidor.md`** do produto ativo sem excluir o produto nem suas entregas.
- O nome original `limpar-produto` foi **rejeitado** pelo usuário por ser confuso com `/excluir-produto`. O nome correto e definitivo é **`/zerar-negocio`**.
- Arquivo: `.claude/commands/zerar-negocio.md`
- Listado na seção **Fundação** do menu do `CLAUDE.md`.

**O que o comando faz:**
1. Verifica o produto ativo
2. Pergunta o que zerar: `perfil.md`, `idconsumidor.md` ou os dois
3. Confirma antes de executar
4. Esvazia os arquivos escolhidos (não os deleta)
5. Sugere `/meu-produto` ou `/idconsumidor` como próximo passo

---

## 2026-03-26 — Melhorias estruturais no sistema

### 1. Primeira interação: detectar produto antes de mostrar menu

- O sistema **não deve mostrar a lista de comandos logo de cara**.
- Ao iniciar, deve **ler `produtos/.ativo`**:
  - **Se existir produto:** mostrar o nome do produto ativo e perguntar o que quer criar. Depois listar os comandos.
  - **Se não existir produto:** entrar em **onboarding guiado** (ver item 2).
- Esse comportamento está registrado no `CLAUDE.md` na seção "Primeira Interação".

---

### 2. Onboarding guiado para novos usuários (sem produto)

Quando o usuário não tiver produto cadastrado, conduzir o fluxo completo **sem pular etapas**, uma pergunta por vez:

1. Qual é a sua especialidade? O que você ensina ou entrega?
2. Você já tem alguma ideia de produto?
   - **Tem ideia clara** → perguntar nome → criar produto → `/meu-produto` automático
   - **Ideia vaga ou nenhuma** → fazer pesquisa de mercado no nicho → sugerir 2-3 ideias com posicionamento, formato e faixa de preço → usuário escolhe → seguir para `/meu-produto`
3. O fluxo de `/meu-produto` inclui: Quadro → Furadeira → Decorados → Urgências Ocultas
4. **O menu de comandos só aparece depois que o perfil estiver completo e salvo.**

---

### 3. `/idconsumidor`: gerar "Para Quem É" e "Baldes de Conteúdo"

O documento gerado pelo `/idconsumidor` agora inclui duas seções obrigatórias:

**Para Quem É:**
- Frase de posicionamento clara: "Este produto é para [perfil], que [problema], e quer [transformação]."
- "Não é para:" — exclusões que ajudam a posicionar

**Baldes de Conteúdo (Identidade do Comunicador):**
- 5 baldes derivados das Urgências Ocultas e dos Decorados
- Cada balde tem: Nome, Propósito (educar / engajar / converter), Tom e Exemplos de temas concretos
- Os baldes são a base da linha editorial e da Identidade do Comunicador
- Esses baldes alimentam o `/conteudo-social` — o comando deve usar os baldes para distribuir os temas quando o arquivo `idconsumidor.md` existir

---

### 4. `/anuncio`: decorados e urgências ocultas como fonte obrigatória

- **Antes de qualquer pergunta sobre a campanha**, o comando deve:
  1. Carregar todos os **Decorados** e todas as **Urgências Ocultas** do `perfil.md`
  2. Ler os arquivos existentes em `produtos/{ativo}/entregas/anuncios/` para identificar quais já foram explorados
  3. Apresentar ao usuário: total disponível, já explorados, e disponíveis para o novo pacote
- **Regra de não repetição:** priorizar urgências e decorados ainda não usados. Se todos já foram usados, indicar que está retomando o tema.
- Os decorados e urgências ocultas são a **fonte de temas** de todo anúncio — não criar temas "do zero" sem consultar essa lista.

---

### 5. `/anuncio`: pesquisa de virais obrigatória para TODOS os formatos

- A pesquisa de TikTok + Instagram virais era obrigatória só para vídeo. **Agora é obrigatória para qualquer formato** (vídeo, imagem, carrossel, texto).
- **Busca Base obrigatória (sempre):**
  - `reels instagram virais [mês e ano atual]` — todos os nichos
  - `tiktok trends virais [mês e ano atual]` — todos os nichos
- Objetivo: captar o padrão de estrutura, tom e abertura que está funcionando agora — não o conteúdo. O conteúdo vem do produto. O formato vem dos virais.
- O que extrair: estrutura de abertura, tom predominante, se entrega conteúdo real ou só promete, padrão de CTA.
- **Modelar sempre os virais que entregam conteúdo real** — nunca os que só prometem sem entregar dentro do próprio post/vídeo.

---

### 6. `/conteudo-social`: mesmas regras de fonte e pesquisa

- Carregar Decorados + Urgências Ocultas do `perfil.md` antes de qualquer geração
- Ler entregas existentes em `produtos/{ativo}/entregas/conteudo-social/` para verificar o que já foi explorado
- Apresentar ao usuário o que está disponível (já usados vs disponíveis)
- Usar os **Baldes de Conteúdo** do `idconsumidor.md` para distribuir os temas entre as categorias corretas
- **Pesquisa de virais obrigatória** (TikTok + Instagram, todos os nichos) antes de gerar qualquer peça

---

### 7. Regra de profundidade mínima — vale para anúncios e conteúdo

Todo anúncio e todo conteúdo criado pelos comandos `/anuncio` e `/conteudo-social` deve obedecer:

- **Gancho:** afirmação não óbvia, contra-intuitiva ou específica. NUNCA pergunta. NUNCA algo genérico.
- **Desenvolvimento:** **mínimo 2 parágrafos substanciais**. Cada parágrafo entrega argumento, ensinamento ou insight concreto.
- **Entrega de valor obrigatória:** o conteúdo precisa ensinar, revelar ou gerar reconhecimento dentro dele mesmo — sem depender de link externo, vídeo ou produto. Quem lê ou assiste aprende algo.
- **Raso, vago e curto são proibidos.** Um parágrafo de desenvolvimento não passa.

---

## 2026-03-24 — Correção da skill `/anuncio`: pesquisa e estrutura de vídeo de Descoberta

### Problema identificado na geração anterior

A primeira versão dos anúncios de vídeo foi considerada **rasa e genérica** pelo usuário. Os roteiros apenas prometiam ou teaseavam conteúdo — não entregavam nada de valor real dentro do vídeo.

### Correções obrigatórias aplicadas

**1. Pesquisa deve cobrir Instagram E TikTok — de todos os nichos**

- A busca de tendências de vídeo deve incluir explicitamente os dois canais: Instagram Reels e TikTok.
- Deve cobrir virais de **todos os nichos** (não só o nicho do produto), para captar o padrão de estrutura e formato vigente na plataforma.
- O que modelar: estrutura dos primeiros 3 segundos, duração ideal, estilo de edição, tom, padrão de CTA — extraídos de conteúdo viral real, não de artigos sobre tendências.

**2. A copy de Descoberta deve entregar conteúdo real dentro do vídeo**

- Vídeos de Descoberta que viralizam **ensinam algo concreto** — a pessoa aprende uma técnica, tem um insight, recebe valor antes de qualquer convite.
- **ERRADO:** vídeo que só promete o que vai ensinar ("me segue que eu te mostro como") sem ensinar nada dentro do próprio vídeo.
- **CERTO:** vídeo que entrega uma técnica, uma virada de perspectiva ou um passo prático concreto — e o CTA vem como convite natural para mais.

**3. Estrutura obrigatória para Descoberta + Vídeo**

```
[0–2s]   GANCHO      → Afirmação contra-intuitiva. Texto na tela + fala simultâneos.
[3–5s]   TEASE       → Uma frase que expande o gancho e retém.
[6–25s]  ENTREGA     → Ensina a técnica ou dá o insight real. Específico, concreto.
[26–30s] REGANCHO    → Texto na tela sintetizando a ideia central.
[31–35s] CTA         → Convite leve para seguir. Sem urgência forçada.
```

**4. Tamanho alvo**

- ~130 palavras por roteiro (equivalente a ~35–45 segundos de fala natural).
- Calibrar a partir dos virais encontrados na pesquisa — se os virais do momento forem mais curtos ou mais longos, ajustar.

**5. A estrutura modela tanto o conteúdo quanto o tempo**

- O conteúdo (o que diz) segue VTSD + perfil do negócio.
- O formato, tempo e estilo (como diz) modelam os virais encontrados na pesquisa.
- Não usar pesquisa de sessão anterior — pesquisar a cada geração.

---

## 2026-03-24 — Correção: duração do vídeo não aparece no resumo de confirmação

### Problema identificado

No resumo de confirmação (antes de gerar), o tempo do vídeo estava sendo indicado como `~35–45s`. Isso está **errado**: a duração só é determinada **após** a pesquisa de tendências (Passo 3), onde se verifica a duração predominante dos virais do momento.

### Correção

- **Não incluir duração do vídeo no resumo de confirmação** (Passo 2 — Entrevista).
- O campo de formato deve constar apenas como: `Vídeo (duração definida após pesquisa de tendências)`.
- A duração real é calibrada na pesquisa e aplicada na geração — não antes.

---

## 2026-03-26 — Princípios de Copy: estilo, leis e categorias

Toda copy gerada por qualquer skill deste projeto deve seguir estes princípios. Eles se sobrepõem a qualquer instrução genérica de "copy persuasiva" ou "copywriting".

### Princípio Central

A melhor copy não parece copy. Parece alguém inteligente explicando uma coisa que o leitor nunca tinha entendido direito.

Nunca vender na copy. Informar, avisar ou ensinar. O produto não existe nos primeiros parágrafos. Só existem o leitor e a realidade dele.

---

### As 7 Leis (seguir todas, sempre)

**1. Ensinar em vez de prometer**
A copy entrega um pedaço de conhecimento real ali mesmo, no texto. A curiosidade vem de querer saber o resto, não de uma promessa vaga.
- Certo: "O primeiro passo é não tentar explicar o que você faz para convencer alguém a comprar. Você só precisa fazer as perguntas certas para que a pessoa, ao responder, perceba por si só que ela precisa do que você faz."
- Errado: "Descubra o método que vai transformar suas vendas para sempre."

**2. Nomear cria realidade**
Sempre que possível, criar um nome próprio para o conceito, problema ou solução. A pessoa sente que está descobrindo algo que já existia e ela não conhecia.
- Nomes que funcionam: "Negociação Terapêutica", "Programação Emocional Repetitiva", "Peeling Estratificado Programado"
- Nomes que não funcionam: "Método Exclusivo de Vendas", "Sistema Revolucionário", "Fórmula Definitiva"

**3. O produto não aparece na copy**
Em nenhum momento a copy fala "esse curso", "esse treinamento", "compre." A pessoa está lendo sobre ela mesma, sobre como o mundo funciona, sobre uma mecânica que explica a vida dela. O produto aparece depois, quando ela já estiver convencida sozinha.

**4. Tom de escritor, não de vendedor**
Escrever como alguém explicando algo que sabe muito bem, não como alguém vendendo algo.
Frases proibidas: "Isso vai transformar sua vida", "Descubra o método", "Não perca essa oportunidade", "Isso pode mudar sua vida", "Você merece isso."

**5. Especificidade mata generalização**
Usar números concretos, situações específicas, detalhes que fazem o texto parecer real.
- "Antes dos 7 anos de idade" > "na infância"
- "15 mil pra 70 mil por projeto" > "multiplique seus ganhos"
- "10 franquias no primeiro ano" > "expanda seu negócio"
- "R$ 1.600" > "vai gastar dinheiro à toa"

**6. Informar, não vender: avisar ou ensinar**
As melhores copies fazem uma de duas coisas: avisam ou ensinam. Nunca vendem.
- Avisar: "Quando você for montar o enxoval do seu bebê, as vendedoras de loja vão te empurrar esses 7 itens — você vai achar que precisa, mas são totalmente desnecessários e vão te custar pelo menos R$ 1.600."
- Ensinar: "O primeiro passo é não tentar explicar o que você faz para convencer alguém a comprar."

**7. Criar um inimigo concreto (ou um cenário inevitável)**
Quando a copy tem um inimigo externo (a vendedora da loja, o professor do YouTube, o jeito antigo de fazer algo), a pessoa não precisa admitir que errou. Ela só precisa aceitar que foi mal orientada. Isso é muito mais fácil de engolir e converte mais.

---

### Vícios de Escrita Proibidos (em toda copy do projeto)

- **Travessão longo (—):** NUNCA usar. É carimbo de texto gerado por IA. Usar vírgula, ponto ou reformular a frase.
- **Estrutura "Não é X. É Y.":** NUNCA usar. Exemplos do que NÃO fazer: "Não é o produto. É o que você faz antes dele." / "Não é disciplina. É método." Reescrever de forma mais elaborada e natural.
- **Frases genéricas de vendedor:** "Transforme sua vida", "Descubra o segredo", "Método revolucionário", "Isso pode mudar tudo."
- **Mencionar o produto na copy:** Nunca falar do curso, treinamento, método ou produto nos primeiros parágrafos.
- **Emojis:** Nunca usar emojis na copy.

---

### As 4 Categorias de Copy (leads de página e anúncio)

Antes de escrever, perguntar: o público é o profissional da área ou o cliente final? Qual a faixa de preço?

Cada lead deve terminar com um parágrafo técnico/racional em itálico que explica por que aquilo funciona do ponto de vista científico ou lógico. Esse parágrafo ancora a emoção com razão.

**Categoria 1 — Inadequação**
Engrenagem: a pessoa descobre que está fazendo algo errado ou está desatualizada. Urgência silenciosa impossível de ignorar.
Estrutura: afirmação direta que desconforta → contextualização (o que mudou) → nomear o problema ou solução → parágrafo técnico em itálico.
Funciona melhor para: cursos, métodos, frameworks. Nichos com atualização constante. Versátil em preço.
Exemplos: "Se você não faz Avaliação Neuropsicológica ou faz do mesmo jeito que se fazia em 2020, você está desatualizada." / "Aquele sérum anti-idade que você passa toda noite? Se você não preparou sua pele antes, ele não penetra quase nada."

**Categoria 2 — Identificação com o Problema**
Engrenagem: a pessoa lê e pensa "isso sou eu." Você descreve a realidade dela com tanta precisão que ela sente que você está dentro da cabeça dela.
Estrutura: descrição vívida do problema com detalhes sensoriais (4-6 parágrafos) → amplificação (dor ou cenário ideal) → revelação do "grande problema" → parágrafo técnico em itálico.
Funciona melhor para: métodos, cursos práticos, mentorias. Público que já tentou e fracassou. Forte para low ticket (R$27 a R$197).

**Categoria 3 — Plug & Play**
Engrenagem: a pessoa não precisa aprender nada. Só pegar e usar. O valor está na praticidade imediata.
Estrutura: headline curta com resultado prático → parágrafo explicando o que recebe e como usa → parágrafo técnico em itálico → CTA.
Funciona melhor para: planilhas, templates, checklists, scripts prontos. Low ticket clássico (R$17 a R$97).
Exemplos: "Tenha confiança para fazer qualquer contratação no seu casamento, com a certeza que ela cabe no seu bolso!"

**Categoria 4 — Promessa Boa Demais (Específica)**
Engrenagem: a pessoa lê e pensa "não é possível, mas se for verdade..." O que segura é a combinação de resultado muito desejável com especificidade tão concreta que parece real demais para ser marketing.
Estrutura: resultado específico com números e situação concreta (antes e depois) → frase que derruba objeção → convite a ver os detalhes sem pressão → parágrafo técnico em itálico.
Tom: de quem está abrindo o jogo, não de quem está vendendo. Precisa de história verdadeira com números verificáveis.
Exemplos: "Eu cobrava 15 mil por projeto de arquitetura, tinha dificuldade de vender e de entregar. Hoje eu cobro mais de 70 mil por projeto."

---

### Matriz de Decisão Rápida

Antes de escrever qualquer copy, responder:
- O cliente precisa aprender ou usar? → Aprender: Inadequação, Identificação ou Promessa Boa Demais. Usar: Plug & Play.
- O cliente já sabe que tem o problema? → Já sabe e sofre: Identificação. Não sabe: Inadequação. Expert tem história real com números: Promessa Boa Demais.

---

### Checklist de Revisão (aplicar antes de entregar qualquer copy)

1. O produto aparece nos primeiros parágrafos? Se sim, tirar.
2. Tem alguma frase que um vendedor diria? Se sim, reescrever.
3. Tem travessão longo (—)? Se sim, substituir.
4. Tem estrutura "Não é X. É Y."? Se sim, reformular.
5. A pessoa aprende algo lendo? Se não, está prometendo em vez de ensinando.
6. Foi criado um nome próprio para o conceito ou problema? Se não, considerar criar.
7. Os detalhes são específicos o suficiente?
8. O tom soa como conversa ou como anúncio?

---

## 2026-03-26 — Estrutura correta de entrega do anúncio de imagem estática

### Problema identificado

Os anúncios de imagem estática eram entregues sem separar o que vai em cada campo. O usuário questionou como todo aquele texto caberia em uma imagem.

### Correção

Um anúncio de imagem estática no Meta Ads tem 4 campos distintos:

| Campo | Conteúdo | Limite |
|---|---|---|
| **Imagem** | Apenas o headline (5–7 palavras) | Visual |
| **Texto principal (legenda)** | GANCHO + DESENVOLVIMENTO + CTA completos | Sem limite prático |
| **Headline (Meta Ads)** | O headline do anúncio | Máx 40 chars |
| **Descrição (Meta Ads)** | Frase de apoio | Máx 90 chars |

**Na entrega de anúncios de imagem, sempre usar esses rótulos explicitamente:**

```
NA IMAGEM: [headline curto — 5–7 palavras]

LEGENDA:
[texto completo com GANCHO, DESENVOLVIMENTO e CTA]

HEADLINE (Meta Ads): [headline]
DESCRIÇÃO (Meta Ads): [frase de apoio]
```

Nunca entregar tudo junto como se coubesse em uma imagem. O texto longo vai na legenda, não na imagem.

Esta regra está registrada também em `skills/anuncios/SKILL.md`.

---

## 2026-03-26 — Exemplos de referência de copy validados (12 leads, 3 nichos)

### Arquivo de referência criado

`.claude/plugins/workshop-marketing/skills/conteudo/references/exemplos-leads-4-categorias.md`

Contém 12 exemplos das 4 categorias de lead aplicadas a 3 nichos:
- **Skincare / Beleza** — Lead 1 (Inadequação), Lead 2 (Identificação), Lead 3 (Plug & Play), Lead 4 (Promessa Boa Demais)
- **Saúde / Imunidade** — Lead 1 (Inadequação), Lead 2 (Identificação), Lead 3 (Plug & Play), Lead 4 (Promessa Boa Demais)
- **Psicologia B2B** — Lead 1 (Inadequação), Lead 2 (Identificação), Lead 3 (Plug & Play), Lead 4 (Promessa Boa Demais)

### Como usar

- Consultar antes de gerar qualquer lead ou abertura de copy
- Referência de: nível de especificidade, profundidade de desenvolvimento, tom, inimigo concreto, parágrafo técnico em itálico
- Não usar como template — usar como parâmetro de qualidade

### Skills atualizadas para referenciar esses exemplos

- `commands/copy-pagina.md`
- `commands/texto-de-venda.md`
- `skills/anuncios/SKILL.md`
- `skills/conteudo/SKILL.md`

---

## 2026-03-25 — Estrutura multi-produto: pasta `produtos/` e produto ativo

### Motivação

O projeto precisa ser replicável para os alunos via GitHub, e cada aluno pode ter mais de um produto/nicho. A estrutura anterior (`meu-negocio/` único + `entregas/` única) não suportava múltiplos produtos.

### Nova estrutura implementada

```
produtos/
  .ativo              ← contém o slug do produto ativo (ex: meu-produto)
  {slug-do-produto}/
    perfil.md
    idconsumidor.md
    entregas/
      paginas/
      anuncios/
      emails/
      copy-pagina/
      conteudo-social/
      criativos/
      comercial/
      textos-de-venda/
```

### Regra obrigatória para todos os comandos e agentes

**ANTES de qualquer operação:**
1. Ler `produtos/.ativo` para obter o slug do produto ativo.
2. Usar `produtos/{ativo}/` como caminho base para todos os arquivos do produto.
3. Se `produtos/.ativo` não existir, orientar o aluno a usar `/novo-produto` primeiro.

### Comandos novos

- `/novo-produto` — cria pasta do produto, subpastas de entregas, e escreve o slug em `produtos/.ativo`.
- `/trocar-produto` — lista subpastas de `produtos/`, mostra qual está ativa, deixa o aluno trocar.

### .gitignore

Adicionado:
```
produtos/*/
produtos/.ativo
```
Assim o aluno que clona o repositório recebe apenas a infraestrutura (`.claude/`, `CLAUDE.md`, `correcoes/`) — sem dados pessoais.

---

## 2026-03-25 — Furadeira em produtos Low Ticket (R$37–97)

### Regra: a Furadeira é a própria ferramenta

- Para produtos **Low Ticket** (faixa de R$37–97), a Furadeira **não** é um método de ensino com macroetapas e microetapas.
- A Furadeira nesses produtos **é a própria ferramenta** entregue (planilha, template, checklist, agente GPT, etc.).
- No `perfil.md`, o campo Furadeira deve registrar: `A ferramenta é a Furadeira — [descrição da ferramenta]`.
- No fluxo do `/meu-produto`, quando o produto for Low Ticket, **não perguntar** sobre macroetapas. Registrar diretamente a ferramenta como Furadeira e avançar para as Identidades.

---

## 2026-03-25 — Novo comando `/quiz` — Gerador de Quiz de Vendas (Caixa Rápido)

### O que foi criado

Arquivo: `.claude/commands/quiz.md`

Comando `/quiz` adicionado ao menu de apresentação no `CLAUDE.md`, na seção Estratégia, abaixo de `/low-ticket`.

### Fluxo do comando (duas fases)

**Fase 1 — Perguntas do quiz:**
- Lê o perfil do produto ativo (`perfil.md` + `idconsumidor.md`)
- Faz no máximo 2 perguntas se faltar Quadro ou preço
- Gera Tela de Entrada + Pergunta 1 (com prompts de imagem para cada opção) + 9 a 19 perguntas adicionais
- Perguntas organizadas em 4 blocos: A (Problema/SPIN), B (Desejo + Visualização Profunda obrigatória), C (Comprometimento), D (Diagnóstico Final)
- Exibe resumo e pede aprovação
- Salva em `produtos/{ativo}/entregas/quiz/perguntas-quiz-[produto].md`

**Fase 2 — Prompt técnico completo (automático após aprovação):**
- Lê o template de referência do prompt técnico do quiz (localizado em `Downloads` do usuário ou conforme indicado na sessão)
- Esse arquivo é o prompt técnico completo para construir o funil de quiz no Lovable.dev (React + Vite + TypeScript + Tailwind + Supabase), usando um produto de exemplo como placeholder
- Substitui todo o conteúdo específico do exemplo pelo produto do aluno: headline, subheadline, perguntas, valores de resposta, tela de resultado, página de vendas, preço, benefícios (Decorados), depoimentos, labels do painel admin
- Mantém toda a estrutura técnica intacta (banco de dados, tracking, componentes, admin)
- Salva em `produtos/{ativo}/entregas/quiz/prompt-tecnico-quiz-[produto].md`
- Entrega final: dois arquivos prontos, o segundo para colar no Lovable.dev

### Regras específicas do comando

- Headline SEMPRE: resultado específico + número concreto + prazo realista
- PROIBIDO: "sem X", "não precisa", "mesmo que", clichês, perguntas no gancho
- Cada opção de resposta deve descrever uma realidade DIFERENTE e reconhecível (não sinônimos)
- Toda pergunta tem ancoragem cotidiana concreta (não abstrata)
- Visualização Profunda obrigatória no Bloco B (cenas concretas do cotidiano transformado)
- NÃO sugerir `/pagina-de-vendas` ao final — o fluxo termina com o prompt técnico do Lovable.dev

### Fase 1 do quiz: perguntas + Tela de Resultado + Página Final de Oferta

A **Fase 1** do comando `/quiz` deve entregar **três componentes juntos**, no mesmo arquivo, antes de avançar para o prompt técnico (Fase 2):

1. Tela de Entrada + Pergunta 1 (com prompts de imagem para cada opção)
2. Perguntas dos 4 blocos (A, B, C, D)
3. Tela de Resultado (diagnóstico personalizado com mensagens condicionais por segmento + CTA)
4. **Página Final de Oferta** (copy completa da página de vendas que aparece após a Tela de Resultado)

A Página Final de Oferta segue 11 blocos obrigatórios:
1. Headline com premissas
2. Subheadline
3. Quadro Comparativo Antes × Depois (logo após o subtítulo)
4. Valor e Botão de Checkout #1
5. Entregáveis (nome + benefícios + resumo + suporte)
6. Valor e Botão de Checkout #2
7. Bônus (nome + benefícios + o que entrega)
8. Valor e Botão de Checkout #3
9. Garantia
10. Autoridade do Criador + Depoimentos (SEMPRE como [IMAGEM], nunca texto corrido)
11. Valor e Botão de Checkout #4 (última chamada)

Somente após aprovação de tudo isso é que se avança para a Fase 2 (prompt técnico do Lovable.dev).

### Template de referência

O template de referência do prompt técnico deve ser solicitado ao usuário na primeira execução caso não esteja disponível no projeto. Esse arquivo deve ser lido a cada execução do comando para gerar a Fase 2.

---

---

## 2026-03-25 — Estrutura correta da skill `/pagina-de-vendas`

### Vídeo sempre na primeira dobra

A skill de página **sempre** deve colocar o vídeo na primeira dobra, visível sem scroll.

Estrutura obrigatória da primeira dobra:
1. **Headline (Premissa)** — vende uma ideia, não o produto. Não pode estar no imperativo, sem tom de promessa. Conduz a pessoa sutilmente à conclusão pré-determinada.
   - Exemplos de padrões válidos: "Todo paciente tem cura", "Quem vende barato vende menos", "É possível...", "O melhor jeito de... é", "Como...", "Qualquer pessoa pode", "Pessoas bonitas usam maquiagem"
2. **Subheadline** — reforça a premissa gerando mais curiosidade
3. **3 bullets** — combinação de urgência oculta + decorado. Mostram o que a pessoa vai aprender/descobrir no vídeo.
   - Estrutura de cada bullet: [O que vai aprender/urgência oculta] → [Pra quê/Decorado]
   - Exemplo: "Como criar um projeto protótipo e fazer a sua primeira venda em pouco tempo e gastando pouco dinheiro"
4. **Vídeo** — já aparece na primeira dobra (começa a aparecer sem precisar rolar)

### Estrutura de seções da página

| Seção | Objetivo |
|---|---|
| Seção 1 | Fazer a pessoa assistir ao vídeo de vendas de valor |
| Seção 2 | Fazer a pessoa clicar no botão de compra — botão acompanhado de compra segura, garantia, acesso imediato |
| Seção 3 | Encantar rápido — paliativo (somente se houver paliativo; se não, ir direto para Seção 4) |
| Seção 4 | Comprovar resultados concretos |
| Seção 5 | Falar do suporte |
| Seção 6 | Vender os bônus |
| Seção 7 | Autoridade do criador |
| Seção 8 | A quem se destina — usar os baldes de "para quem" da identidade do consumidor |
| Seção 9 | Explicar a lógica do método como um todo |
| Seção 10 | Mostrar muita verdade em depoimentos incontestáveis + reflexão e ativação emocional |
| — | Botão de venda |
| Seção FAQ | Tirar dúvidas específicas com profundidade e provas |
| Seção final | Resumindo |

### Regra de copy: nunca usar travessão (—)

O texto de copy deve ser **contínuo**, sem travessão (—) separando partes da frase.
Reescrever as frases de forma fluida, sem esse separador.

**Errado:** "Como calcular o valor real — para nunca mais aceitar um preço que te deixa no prejuízo"
**Certo:** "Como calcular o valor real para nunca mais aceitar um preço que te deixa no prejuízo"

Essa regra se aplica a: bullets, headlines, subheadlines, depoimentos, descrições de bônus, entregáveis — tudo.

> **Atenção:** essa regra foi expandida para **todos os textos/copies gerados por qualquer skill** — não apenas a skill `/pagina-de-vendas`. Ver entrada de 2026-03-25 abaixo.

---

### Sobre as Premissas (headlines)

- Não podem estar no imperativo
- Não devem ter tom de promessa direta
- O objetivo é conduzir a pessoa de forma sutil para que ela chegue à conclusão (pré-determinada) sozinha
- Vendem uma ideia/crença, não o produto

---

## 2026-03-25 — Regra de qualidade obrigatória para todos os anúncios

### Problema identificado
Os anúncios gerados na primeira versão foram considerados rasos, curtos demais e genéricos — não entregavam valor real, apenas prometiam ou teasavam conteúdo.

### Regra obrigatória: todo anúncio deve entregar valor real e seguir o modelo viral

**Nenhum anúncio pode ser:**
- Óbvio para quem já está no nicho
- Raso — sem argumento concreto, sem especificidade
- Curto demais — desenvolvimento de 1-2 frases não é suficiente

**Todo anúncio deve:**
- Entregar conteúdo real dentro do próprio anúncio (ensinar, revelar, demonstrar)
- Seguir a estrutura e o estilo das referências virais encontradas na pesquisa
- Ter desenvolvimento substancial — mínimo 2-3 parágrafos com argumento, especificidade e profundidade
- Modelar o **formato e estilo** (como diz) a partir dos virais pesquisados; o **conteúdo** (o que diz) vem do VTSD + perfil do negócio

### Estrutura obrigatória para TODO vídeo (qualquer fase, qualquer objetivo)

```
[0–3s]   GANCHO      → Afirmação contra-intuitiva ou quebra-padrão. Texto na tela + fala simultâneos.
[4–15s]  TEASE       → Expande o gancho, cria tensão, contextualiza o problema.
[16–42s] ENTREGA     → Ensina, demonstra ou revela algo real e concreto. NUNCA apenas prometer.
[43–48s] REGANCHO    → Texto na tela sintetizando a ideia central (âncora visual para quem assiste sem som).
[49–55s] CTA         → Convite direto adequado à fase. Sem urgência forçada.
```

- **Duração alvo:** 45–60s para vídeos de conversão/captura; 35–45s para Descoberta
- **Palavras por roteiro:** ~150–200 palavras (não menos que isso)
- **Legendas na tela em todo o vídeo** — maioria assiste sem som

### Três estruturas de roteiro válidas (baseadas em virais 2026)

| Estrutura | Quando usar | Lógica de retenção |
|---|---|---|
| **Loop Perfeito** | Revelação, insights | O final conecta ao gancho — incentiva replay |
| **Tutorial de 3 Passos** | Procedimento, ensino | Cada passo avança a narrativa — pessoa assiste até o fim para completar |
| **Quebra-Padrão** | Contraste, paradoxo | Começo inesperado para o cérebro — força a pausa no scroll |

### Texto principal (legenda) — padrão de profundidade

- **GANCHO:** premissa não óbvia — 1-2 frases fortes
- **DESENVOLVIMENTO:** mínimo 2 parágrafos substanciais com argumento específico, concreto e não óbvio. Não pode ser resumo vago do que o vídeo mostra — precisa entregar valor por si só, mesmo sem o vídeo.
- **CTA:** convite direto adequado à fase

---

---

## 2026-03-25 — Publicação na Vercel após geração de página

### Regra: sempre oferecer publicação ao final

Após salvar qualquer página HTML, a skill deve **sempre perguntar** se o usuário quer publicar online, não assumir que sim nem que não.

### Dois fluxos distintos

**Usuário sem conta Vercel:**
Orientar passo a passo em linguagem simples (não técnica):
1. Criar conta gratuita em vercel.com (recomendado: entrar com GitHub)
2. Gerar token: avatar > Settings > Tokens > Create Token > copiar
3. Colar o token aqui, o assistente configura e publica tudo

**Usuário com conta Vercel (token já disponível):**
Pedir o token (ou usar o que está no `.env`), criar `vercel.json` + `package.json` se não existirem, executar `npx vercel --token ... --yes` e informar a URL.

### Nunca usar linguagem técnica com o usuário

Não falar em "CLI", "npm", "Node", "terminal" como se fossem pré-requisitos que o usuário já conhece. Explicar o que cada coisa é quando necessário. O usuário é empreendedor digital, não desenvolvedor.

---

## 2026-03-25 — Comando `/quiz`: número fixo de 10 perguntas

### Regra

- O comando `/quiz` deve gerar **exatamente 10 perguntas** — nem mais, nem menos.
- A estrutura dos blocos foi redefinida para respeitar esse total fixo:

| Bloco | Perguntas | Quantidade |
|---|---|---|
| Tela de Entrada + Pergunta 1 (segmentação) | P1 | 1 |
| Bloco A — Problema (SPIN) | P2 a P4 | 3 |
| Bloco B — Desejo + Visualização Profunda | P5 a P7 | 3 |
| Bloco C — Comprometimento | P8 a P9 | 2 |
| Bloco D — Diagnóstico Final | P10 | 1 |
| **Total** | | **10** |

- O resumo de confirmação deve mostrar "Total: 10 perguntas (fixo)".
- O arquivo `.claude/commands/quiz.md` foi atualizado com essa regra.

---

## 2026-03-25 — Deploy autônomo da Vercel e vídeo na página

### Regra: pedir o vídeo durante a entrevista, antes de gerar

A skill `/pagina-de-vendas` deve perguntar o link do vídeo no Bloco 2/3 (junto com os outros detalhes da página de vendas), antes de gerar. Não perguntar depois.

Pergunta obrigatória:
```
Tem um vídeo de vendas para usar na primeira dobra?
(ex: "https://www.youtube.com/watch?v=XXXX" — ou "ainda não tenho" para usar placeholder)
```

Se informado, embutir diretamente no HTML com iframe e `aspect-ratio: 16/9; display: block;`.
Se não informado, usar placeholder visual com instrução.

### Regra: aviso sobre incorporação do YouTube

Se o usuário informar um link do YouTube, incluir este aviso após a publicação:

> "Para o vídeo aparecer na página, certifique-se de que a opção 'Permitir incorporação' está ativa no YouTube: studio.youtube.com → Conteúdo → editar o vídeo → Mais opções → Permitir incorporação → Salvar."

### Regra: deploy autônomo sem perguntas desnecessárias

O fluxo de publicação deve ser o mais autônomo possível. Após o usuário aprovar a página:

1. Salvar o arquivo com o nome padrão (`vendas-[produto].html`)
2. **Sempre** criar `index.html` como cópia do arquivo na mesma pasta (a Vercel exige `index.html` para servir na raiz)
3. Publicar com o comando:
   ```
   npx vercel produtos/{ativo}/entregas/paginas --prod --yes --name {slug-do-produto}
   ```
4. Informar a URL pública ao usuário

Não usar `vercel.json` nem `package.json` para esse deploy — o comando acima já aponta direto para a pasta da página.

### Regra: nome do projeto Vercel = slug do produto ativo

Usar o slug do produto ativo (ex: `meu-produto`) como `--name` no deploy. Isso garante que a URL final seja `{slug}.vercel.app`.

---

## 2026-03-25 — Página Final de Oferta do quiz: sem vídeo

### Regra

- A **Página Final de Oferta** gerada pelo comando `/quiz` (a página de vendas que aparece após a Tela de Resultado) **não tem vídeo**.
- Remover a seção "Seção de Vídeo" do template da Página Final — tanto do arquivo de perguntas (copy) quanto do prompt técnico para o Lovable.dev.
- Essa regra se aplica ao funil de quiz (Caixa Rápido / low ticket). Páginas de vendas geradas pelo comando `/pagina-de-vendas` seguem a regra própria daquela skill (vídeo obrigatório na primeira dobra).

---

## 2026-03-25 — Comando `/quiz`: estrutura SPIN e tipos variados de pergunta

### Estrutura SPIN obrigatória (10 perguntas fixas)

| Posição | Fase | Tipo sugerido | Observação |
|---|---|---|---|
| P1 | Segmentação (Tela de Entrada) | Múltipla escolha + fotos | Fixo |
| P2 | S — Situação | Calculadora ou Input numérico | Coleta dado real para usar na Implicação |
| P3 | S — Situação | Múltipla escolha | Confirma contexto |
| P4 | P — Problema | Sim/Não ou Múltipla escolha | Dor cotidiana direta |
| P5 | P — Problema | Múltipla escolha | Comportamento-problema |
| P6 | I — Implicação | **Calculadora (obrigatório)** | Confronta o lead com dado numérico real |
| P7 | I — Implicação | Slider ou Múltipla escolha | Aprofunda tensão do resultado |
| P8 | N — Necessidade | **Múltipla escolha (Visualização Profunda obrigatória)** | Cenas cotidianas transformadas |
| P9 | N — Necessidade | Múltipla escolha | Comprometimento com a mudança |
| P10 | Diagnóstico Final | Múltipla escolha | Síntese que conecta ao Quadro |

### 5 tipos de pergunta disponíveis

1. **Múltipla escolha** — 4 opções com emoji, clicar avança
2. **Calculadora** — 2 campos de input + fórmula + resultado exibido na tela antes de avançar
3. **Slider** — barra deslizante 1–10 com labels nos extremos
4. **Sim/Não** — dois botões grandes (✅ / ❌)
5. **Input numérico** — campo único de digitação com unidade

### Regras de uso dos tipos

- Calculadora é **obrigatória** na fase I (P6) — confronta o lead com um número concreto que revela o custo real da inação
- Visualização Profunda é **obrigatória** na fase N (P8) — cenas cotidianas transformadas, nunca estados emocionais abstratos
- Nunca usar mais de 2 perguntas do mesmo tipo em sequência
- Variar tipos ao longo do quiz é regra (não opcional)
- O prompt técnico do Lovable.dev deve incluir estrutura de dados para todos os 5 tipos

### Arquivo atualizado

`.claude/commands/quiz.md` — estrutura SPIN, 5 tipos de pergunta, blocos renomeados de A/B/C/D para S/P/I/N + Diagnóstico.

---

## 2026-03-25 — Comando `/quiz`: arquivo único em vez de dois arquivos separados

### Decisão

- O comando `/quiz` gera **um único arquivo** `.md` — não dois arquivos separados.
- O arquivo único contém as perguntas (com prompts de imagem e tipos de pergunta) embutidas dentro do prompt técnico do Lovable.dev.
- Nome do arquivo: `quiz-[produto].md` (não mais `perguntas-quiz-[produto].md` + `prompt-tecnico-quiz-[produto].md`).
- Os prompts de imagem da P1 ficam embutidos diretamente no campo `image_prompt` de cada opção, dentro da Seção 5 do prompt técnico.

### Motivo

Testado e validado: um único arquivo é suficiente para copiar e colar no Lovable.dev. Dois arquivos criavam redundância sem benefício prático.

---

## 2026-03-25 — Regra global: nunca usar travessão em nenhum texto/copy

### Regra

- **Nenhum texto ou copy gerado por qualquer skill pode conter travessão (—).**
- Essa regra é global e se aplica a todas as skills: `/anuncio`, `/copy-pagina`, `/pagina-de-vendas`, `/roteiro-de-video`, `/conteudo-social`, `/sequencia-de-emails`, `/playbook-comercial`, `/low-ticket`, `/quiz` e quaisquer outras.
- Reescrever sempre de forma fluida, sem o separador.

**Errado:** "Descubra o método — e comece a vender hoje"
**Certo:** "Descubra o método e comece a vender hoje"

---

## 2026-03-25 — Comando `/novo-produto`: perguntar tipo do produto (Low Ticket ou Middle Ticket)

### Regra

- Ao criar um novo produto com `/novo-produto`, **imediatamente após perguntar o nome**, o comando deve perguntar o tipo do produto:

```
Que tipo de produto é este?

1. Low Ticket (R$7 a R$97 — quiz, desafio, mini-curso, agente GPT)
2. Middle Ticket (R$97 a R$997 — curso online, workshop, grupo)

Digite o número:
```

- O tipo escolhido é salvo em `produtos/{slug}/tipo.md`.
- Todos os comandos que leem o perfil do produto também devem verificar esse arquivo para adaptar o fluxo (ex: `/meu-produto` não pergunta sobre macroetapas se for Low Ticket).

### Arquivo atualizado

`.claude/commands/novo-produto.md` — novo Passo 2 (pergunta de tipo) e novo Passo 6 (salvar `tipo.md`). Os passos anteriores foram renumerados.

---

## 2026-03-26 — Regras de design obrigatórias em todas as skills de página

### Regra

As regras de design definidas em `skills/paginas/SKILL.md` e `skills/paginas/references/cdn-design-resources.md` são **obrigatórias para todas as skills que geram páginas HTML**, sem exceção:

- `/pagina-de-vendas` — já incluía as regras ✓
- `/paginas-low-ticket` — atualizado nesta sessão ✓
- Página de Captura — coberta pelo `/pagina-de-vendas` (opção 2) ✓
- Página de Obrigado — coberta pelo `/pagina-de-vendas` (opção 3) ✓

### Regras de design que se aplicam a todas as páginas

- **TODAS as fontes sans-serif** — heading e body. Serifadas são PROIBIDAS (ver biblioteca aprovada)
- **Mínimo 4 tipos de fundo** diferentes entre seções (claro, escuro, imagem+overlay, gradiente)
- **Pelo menos 2 seções com imagem de fundo** (picsum.photos + overlay)
- **Grid 2 colunas** para entregáveis — NUNCA 3 colunas
- **Cards** com min-width 320px, padding 28px+, font-size 0.95rem+
- **Header com logotipo** obrigatório em toda página
- **Texto sempre em pt-BR** com acentos corretos
- **NÃO parecer Lovable/v0** — sem cards brancos idênticos em fundo bege, sem gradiente roxo-azul genérico, sem ícones em quadrados arredondados pastéis
- **Mixagem de 2-3 templates** obrigatória antes de gerar — nunca usar um template sozinho

### O que mudou no `/paginas-low-ticket`

Antes: gerava só copy (4 leads) e sugeria usar `/pagina-de-vendas` para criar o HTML.

Depois: após aprovação das leads, pergunta se o usuário quer gerar o HTML agora. Se sim:
1. Pergunta qual lead usar, preço, link de checkout e cor
2. Lê `skills/paginas/SKILL.md` e `cdn-design-resources.md` para design
3. Faz mixagem de 2-3 templates conforme o nicho
4. Gera página HTML completa com estrutura de 10 seções (lead hero → problema/paliativo → solução → entregáveis → stack de valor → garantia → FAQ → CTA → rodapé)
5. Salva em `produtos/{ativo}/entregas/paginas/pagina-low-ticket-[produto].html`

---

## 2026-03-26 — Novo comando `/paginas-low-ticket`: origem e fluxo completo

### Fonte original

Prompt fornecido pelo usuário: `Downloads/prompt-copy-low-ticket.md`. Adaptado para o formato de comando do projeto e salvo em `.claude/commands/paginas-low-ticket.md`.

### O que o comando entrega

1. **4 leads de abertura** para páginas de vendas low ticket, uma para cada ângulo:
   - **Inadequação** — a pessoa descobre que está desatualizada ou fazendo errado
   - **Identificação com o Problema** — descreve a realidade com tanta precisão que a pessoa pensa "isso sou eu"
   - **Plug & Play** — só pegar e usar, zero aprendizado necessário
   - **Promessa Boa Demais** — resultado concreto com números reais (exige história verdadeira)

2. **Matriz de Decisão** incluída: ao final das 4 leads, indica qual é mais indicada para o produto com base no tipo de público e no problema.

3. **Geração opcional da página HTML** diretamente no mesmo fluxo — sem precisar chamar `/pagina-de-vendas` depois.

### Regras específicas do comando

- As 7 leis de copy D48 estão explicitadas no comando (ensinar em vez de prometer, nomear cria realidade, produto não aparece no lead, etc.)
- Categoria 4 (Promessa Boa Demais) exige história real com números verificáveis — sem isso, não usar
- Cada lead termina com parágrafo técnico/racional em itálico
- Checklist de revisão automática antes de entregar

### Registro no CLAUDE.md

Adicionado na seção "Páginas e Textos", entre `/copy-pagina` e `/anuncio`:
`/paginas-low-ticket` — Gerar as 4 leads D48 (Inadequação, Identificação, Plug & Play, Promessa Boa Demais)

---

## 2026-03-26 — Novo comando `/excluir-produto`

### Origem

O usuário pediu uma skill para excluir um produto e todas as entregas e pastas referentes a ele.

### O que o comando faz

- Lista todos os produtos cadastrados em `produtos/`, marcando qual está ativo
- Pede confirmação antes de apagar (com aviso especial se for o produto ativo)
- Apaga toda a pasta `produtos/{slug}/` e seu conteúdo recursivamente (`rm -rf`)
- Se o produto excluído era o ativo:
  - Pergunta qual outro produto ativar (se houver outros)
  - Limpa o arquivo `produtos/.ativo` se não restar nenhum produto
- Confirma a exclusão e sugere o próximo passo

### Arquivo

`.claude/commands/excluir-produto.md`

### Listagem no CLAUDE.md

Adicionado na seção **Fundação** da lista de comandos:

`/excluir-produto` — Excluir um produto e todas as suas entregas

---

---

## 2026-03-26 — Referências visuais e de copy adicionadas (VTSD, Light Copy, Stories 10x)

### Arquivos de referência criados

Três páginas de venda reais do ecossistema Leandro Ladeira foram analisadas e documentadas como referência para copy e design de páginas:

| Página | URL de origem | Conteúdo |
|---|---|---|
| VTSD (aula gratuita) | vendatodosantodia.br/pv0622-d | Método principal — design light/claro |
| Light Copy | vendatodosantodia.br/lightcopy | Copywriting — design dark premium (preto + dourado) |
| Stories 10x | vendatodosantodia.br/stories10x | Instagram — design dark vibrante (preto + rosa) |

### Arquivos criados

**1. Design** — `.claude/plugins/workshop-marketing/skills/paginas/references/design-referencia-vtsd.md`
- 3 estilos visuais documentados: Light, Dark Premium, Dark Vibrante
- Paletas reais (hex), CSS dos botões CTA, tipografias por estilo
- Seções recorrentes: hero com vídeo, tabela comparativa, para quem é, estudos de caso, bio do autor, grid de mídia, FAQ accordion
- Lógica de alternância de fundos entre seções
- Padrão de cores por categoria de produto

**2. Copy** — `.claude/plugins/workshop-marketing/skills/conteudo/references/exemplos-copy-paginas-vtsd.md`
- Headlines e subheadlines das 3 páginas com análise de estrutura
- CTAs padrão ("Quero ganhar dinheiro com a internet →", "QUERO VENDER MUITO MAIS", "QUERO ENTRAR NO STORIES 10X")
- Features, bullets de aprendizado e features rápidas (4-5 itens) de cada página
- Tabelas comparativas (com vs sem, método tradicional vs novo) — copy completa
- Para Quem É (5 perfis) e nichos listados
- Depoimentos com resultado específico em R$ ou métrica
- Currículo de módulos (Light Copy — 5 módulos com ementa)
- Bio do Leandro Ladeira em 2 versões: curta e completa
- FAQ real das 3 páginas (9 perguntas do Stories 10x)
- Padrões extraídos: estrutura de headline, padrão de CTA, bullet de resultado, copy de garantia

### Skills atualizadas

- `skills/paginas/SKILL.md` — adicionada referência ao `design-referencia-vtsd.md` como "principal referência de design"
- `skills/conteudo/SKILL.md` — adicionada seção "Referências de Copy" com o `exemplos-copy-paginas-vtsd.md` como principal referência

### Instrução de uso

**Ao gerar qualquer página de vendas** (`/pagina-de-vendas`):
- Consultar `design-referencia-vtsd.md` para calibrar o estilo visual, paleta e padrões de seção

**Ao gerar qualquer copy de página** (`/copy-pagina`, `/texto-de-venda`):
- Consultar `exemplos-copy-paginas-vtsd.md` para calibrar tom, estrutura de headline, CTA e argumentação no padrão Light Copy real

---

## 2026-03-26 — Estratégia de uso das 4 leads D48 com os mentorados

### Contexto estratégico (origem: áudio de WhatsApp)

O objetivo do comando `/paginas-low-ticket` dentro da mentoria é ensinar os alunos a usar as 4 categorias de lead como um sistema de teste:

- Cada aluno cria as 4 leads (Inadequação, Identificação, Plug & Play, Promessa Boa Demais) para o produto dele
- Ele escolhe qual lead tem mais identificação com o posicionamento do produto
- Investe 200 a 500 reais em tráfego pago naquela lead
- Se não vender, troca para a próxima lead e testa novamente
- Uma das 4 vai acabar vendendo — são 4 chances de acertar
- Além das 4 leads, ainda existe o quiz (Caixa Rápido) como mais uma opção de funil

### Implicação para o assistente

- O assistente deve reforçar essa lógica ao entregar as 4 leads: deixar claro que são ângulos diferentes para testar, não variações do mesmo texto
- A Matriz de Decisão ao final das 4 leads ajuda o aluno a escolher por qual começar — mas o fluxo de teste continua até uma vender
- O quiz é apresentado como recurso adicional (não substituto das leads), pois combina um funil de diagnóstico com a página de oferta low ticket

---

## 2026-03-27 — Comando `/zerar-negocio`: fallback para `meu-negocio/`

### Correção aplicada

O comando `/zerar-negocio` (e qualquer outro comando que precise localizar `perfil.md` e `idconsumidor.md`) deve seguir este fluxo de localização:

1. Ler `produtos/.ativo`. Se existir e tiver conteúdo (slug), usar `produtos/{ativo}/` como caminho base.
2. Se `produtos/.ativo` estiver vazio ou não existir, verificar se `meu-negocio/perfil.md` ou `meu-negocio/idconsumidor.md` existem e têm conteúdo. Se sim, usar `meu-negocio/` como caminho base.
3. Só encerrar com "nenhum produto ativo" se nenhum dos dois caminhos tiver arquivos com conteúdo.

**Motivação:** o projeto do usuário ainda usa `meu-negocio/` como pasta de dados. A nova estrutura multi-produto (`produtos/`) coexiste com a estrutura legada. O comando não pode falhar só porque `produtos/.ativo` está vazio.

**Arquivo corrigido:** `.claude/commands/zerar-negocio.md`

---

## 2026-03-27

### Framework de Decisão: Quiz vs. Página de Vendas (Low Ticket)

Antes de acionar qualquer skill de página para produto de entrada, o agente deve analisar os dados do produto e do consumidor e aplicar este framework — **nunca perguntar de cara ao aluno** qual formato ele quer. A sugestão deve vir acompanhada da explicação dos critérios.

#### Critérios de Decisão

| Critério | Aponta para QUIZ | Aponta para PÁGINA |
|---|---|---|
| Tipo de produto | Emocional / dor / identificação | Prático / ferramenta / direto ao ponto |
| Nível de consciência do lead | Não sabe que tem problema | Já sabe o que quer |
| Complexidade da decisão | Precisa diagnosticar / explicar | Decisão simples e direta |
| Faixa de preço | Até R$47 | Acima de R$97 |
| Tipo de público | Emocional | Analítico / pragmático |

**Regra:** Se 2 ou mais critérios apontarem para o mesmo lado, siga ele.
**Desempate:** Em caso de empate, recomendar QUIZ (mais rápido de validar).

#### Fluxo correto

1. Analisar `perfil.md` e `idconsumidor.md` pelos 5 critérios acima
2. Apresentar a recomendação com explicação critério a critério (baseada nos dados reais do produto)
3. Informar que o aluno pode trocar depois se quiser testar o outro formato
4. Perguntar se o aluno concorda ou prefere o outro formato
5. Só após confirmação, acionar a skill correspondente (`paginas-low-ticket` ou `quiz`)

---

## 2026-03-27 — Correção crítica: Quadro deve ser resultado final, não processo

### Regra

O Quadro é a **transformação final** que a pessoa CONQUISTA ou SE TORNA após usar o produto. É a chegada, não o caminho.

**O que NÃO é Quadro (processo / meio para chegar lá):**
- "Identificar [causa do problema]" ❌ — isso é investigação, não resultado
- "Descobrir [o que está causando X]" ❌ — é o caminho, não a chegada
- "Mapear [padrão ou comportamento]" ❌ — é diagnóstico, não transformação
- "Entender como funciona X" ❌ — é aprendizado, não mudança de vida
- "Aprender o método Y" ❌ — é processo, não conquista

**O que É Quadro (resultado final concreto e verificável):**
- "Falar inglês em 90 dias" ✓
- "Fechar R$10 mil por mês como social media" ✓
- "Vender bolo caseiro todos os dias" ✓
- "Fazer a primeira leitura de tarô com confiança" ✓
- "Emagrecer 8kg sem cortar o que você gosta" ✓

**Teste rápido:** a pessoa pode dizer "isso aconteceu na minha vida" ao final do produto? Se sim, é Quadro. Se não, é processo.

Esta regra se aplica a todos os comandos e agentes que geram opções de Quadro: `/meu-produto`, `estrategista-de-produto`, `estrategista-low-ticket`, onboarding, e qualquer outro fluxo de concepção de produto.

---

## 2026-03-27 — Agente `estrategista-low-ticket`: benchmark antes da pergunta de formato

### Regra

Na **Etapa 1 — Concepção do Produto**, passo 2 (Formato do produto), o agente deve fazer uma **pesquisa de benchmark** (WebSearch) no nicho do produto **antes** de apresentar as opções de formato.

**O que pesquisar:**
- Quais formatos os concorrentes mais usam no nicho
- Qual faixa de preço é praticada
- Quais formatos têm melhor percepção de valor pelo público do nicho

**Como apresentar a pergunta:**

```
Qual formato o produto vai ter?

1. E-book / Guia (PDF passo a passo)
2. Checklist / Roteiro de autoaplicação
3. Mini-curso (3 a 5 aulas curtas em vídeo)
4. Desafio (5 a 7 dias com tarefas diárias)
5. Agente GPT (assistente de IA personalizado)

De acordo com a pesquisa de mercado que eu fiz e com as informações que tenho sobre você e o seu projeto, eu sugiro [formato recomendado] porque [razão baseada no nicho, público e Quadro], no valor de R$[valor sugerido], com [quantidade e descrição dos entregáveis principais], [quantidade] bônus e suporte via [forma de suporte].

Digite o número:
```

**A sugestão deve ser sempre fundamentada em:**
- Resultado da pesquisa de benchmark (formatos e preços praticados no nicho)
- Quadro do produto (resultado final que o aluno conquista)
- Urgências Ocultas e público já levantados nas fases anteriores

**Arquivo atualizado:** `.claude/agents/estrategista-low-ticket.md` — passo 2 da "Ordem das fases" na Etapa 1.

---

## 2026-03-27 — Correção crítica: quiz gera prompt Lovable.dev, não HTML

### Regra

O comando `/quiz` e o fluxo de quiz dentro do `estrategista-low-ticket` **nunca geram um arquivo HTML**. O resultado é um arquivo `.md` com o **prompt técnico completo para colar no Lovable.dev**.

**ERRADO — nunca oferecer estas opções ao final do quiz:**
- "Aprovar e gerar a página HTML" ❌
- "Quero gerar o HTML agora" ❌
- Salvar em `produtos/{ativo}/entregas/paginas/quiz-[produto].html` ❌

**CERTO — opção correta ao final da Fase 1 do quiz:**
- "Aprovar e gerar o prompt técnico para o Lovable.dev" ✓
- Salvar em `produtos/{ativo}/entregas/quiz/quiz-[produto].md` ✓

### Por que

O quiz é um funil interativo com calculadora, slider, múltipla escolha com fotos, banco de dados (Supabase), tracking de etapas e painel administrativo. Isso não pode ser feito em HTML estático. O Lovable.dev constrói o app completo em React + Vite + TypeScript + Tailwind + Supabase a partir do prompt técnico.

### Arquivos corrigidos

- `.claude/agents/estrategista-low-ticket.md` — Etapa 3 (fluxo de QUIZ) reescrita com as instruções corretas
- `.claude/commands/quiz.md` — já tinha o fluxo correto; o problema estava no agente que o invocava

---

## 2026-03-27 — Otimizações de performance no `estrategista-low-ticket`

### 1. Pasta `correcoes/` não deve ser lida por agentes ou skills

A pasta `correcoes/informacoes-adicionais.md` é apenas um **registro histórico** de decisões e ajustes do projeto. Nenhum agente, skill ou comando deve ler esse arquivo durante a execução.

**Arquivos atualizados para remover a leitura:**
- `CLAUDE.md` — Regra de Ouro #8 removida, item 4 do "Contexto Persistente" removido, referência no Fluxo Padrão removida, referência na Regra #7 removida
- `.claude/agents/estrategista-low-ticket.md`
- `.claude/agents/estrategista-middle-ticket.md`
- `.claude/commands/criar-produto-low-ticket.md`
- `.claude/commands/paginas-low-ticket.md`
- `.claude/plugins/workshop-marketing/skills/anuncios/SKILL.md`

---

### 2. WebSearch unificada na Etapa 1 (duas buscas viram uma)

O agente fazia duas WebSearches separadas na Etapa 1:
- Passo 2: benchmark de formato (para sugerir o formato ao aluno)
- Passo 6: tabela de concorrentes (Pesquisa de Mercado)

Ambas buscavam informações sobre o mesmo nicho. Foram unificadas em **uma única busca** feita antes do passo de formato, cujos resultados servem para os dois propósitos.

**Impacto:** elimina 1 WebSearch completa por execução do agente.

**Arquivo atualizado:** `.claude/agents/estrategista-low-ticket.md`

---

### 3. Redução do volume de Decorados e Urgências Ocultas

Para reduzir o tempo de geração da Etapa 1 sem comprometer a qualidade do produto final:

| Item | Antes | Depois |
|---|---|---|
| Decorados | 30 benefícios (10 por categoria) | 15 benefícios (5 por categoria) |
| Urgências Ocultas — Dores | 8 | 5 |
| Urgências Ocultas — Desejos | 8 | 5 |
| Urgências Ocultas — Dúvidas | 8 | 5 |
| Urgências Ocultas — Assuntos relacionados | 6 | 4 |
| **Total Urgências** | **30** | **19** |

**Arquivo atualizado:** `.claude/agents/estrategista-low-ticket.md`

---

## 2026-03-27 — Regra crítica: nunca restaurar produtos/.ativo ao final de uma sessão

### Problema que ocorreu

O agente `estrategista-low-ticket` foi usado para criar um produto para uma mentorada (Luciane Severo). Ao final da sessão, foi instruído a "restaurar `produtos/.ativo` para `taro-para-iniciantes`" (o produto que estava ativo antes). Esse produto havia sido excluído anteriormente, então o `.ativo` ficou apontando para um slug inexistente, quebrando todos os comandos subsequentes.

### Regra

**NUNCA restaurar `produtos/.ativo` para um valor anterior ao final de qualquer sessão.**

O `.ativo` deve sempre apontar para o produto que foi criado ou estava sendo trabalhado. Se o dono do projeto quiser voltar para outro produto, ele usa `/trocar-produto` manualmente.

**Fluxo correto:**
- Criar produto → escrever slug em `produtos/.ativo` → deixar lá
- Nunca "desfazer" a ativação ao final de uma sessão
- Nunca assumir que existe um "produto original a restaurar"

**Contexto adicional:** o `estrategista-low-ticket` (e outros agentes) pode ser usado pela Elen para criar produtos de seus mentorados, não só os produtos dela. Nesses casos, o produto criado é o produto ativo até que ela troque manualmente.

### Arquivos corrigidos

- `.claude/agents/estrategista-low-ticket.md` — adicionada regra explícita proibindo restauração do `.ativo`
- `produtos/.ativo` — corrigido para `decisao-raiz` (produto da Lu, único produto existente agora)
- `produtos/crenca-raiz-intro/` — pasta criada por engano durante a sessão foi removida

---

## 2026-03-30 — Correção: skill `/meu-produto` deve gerar Argumentos Incontestáveis, não perguntar ao usuário

### Problema identificado

O Bloco 6/6 da skill `/meu-produto` perguntava ao aluno se ele tinha dados, pesquisas ou estatísticas para comprovar a eficácia do método. Isso contradiz o princípio central da skill ("Consultor, não formulário") e interrompe o fluxo de geração automática.

### Correção aplicada

**Arquivo corrigido:** `.claude/commands/meu-produto.md` — Bloco 6/6

**Comportamento anterior:**
> "Pergunte se o aluno tem dados, pesquisas ou estatísticas que comprovam a eficácia do método. Se não tiver, pule sem pressão."

**Comportamento correto:**
- Gerar automaticamente de 5 a 8 Argumentos Incontestáveis com base em tudo já coletado: pesquisa de mercado, dados do nicho, Quadro, Furadeira e Identidades
- Organizar em categorias: Dados de mercado, Evidências da lógica do método, Referências do setor, Dados de resultado
- Se a pesquisa de mercado não foi feita anteriormente, fazer WebSearch rápida por dados e estatísticas do nicho antes de gerar
- Após gerar, apresentar para validação e **então** perguntar se o aluno quer adicionar dados próprios (alunos, faturamento, resultados documentados) para incorporar à lista existente

**Regra:** os Argumentos Incontestáveis são sempre gerados pelo assistente — nunca solicitados como formulário ao aluno.

---

## Como acrescentar entradas

Use o formato:

```markdown
## AAAA-MM-DD

### Título curto

- Ponto 1
- Ponto 2
```
