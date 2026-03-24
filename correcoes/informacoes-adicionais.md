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

### 5. Fluxo de entrevista correto para Pico de Vendas

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

## Como acrescentar entradas

Use o formato:

```markdown
## AAAA-MM-DD

### Título curto

- Ponto 1
- Ponto 2
```
