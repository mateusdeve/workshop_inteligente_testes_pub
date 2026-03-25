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

## 2026-03-25 — Estrutura multi-produto: pasta `produtos/` e produto ativo

### Motivação

O projeto precisa ser replicável para os alunos via GitHub, e cada aluno pode ter mais de um produto/nicho. A estrutura anterior (`meu-negocio/` único + `entregas/` única) não suportava múltiplos produtos.

### Nova estrutura implementada

```
produtos/
  .ativo              ← contém o slug do produto ativo (ex: curso-tarot)
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
- Lê o template em `C:\Users\Elen\Downloads\prompt-quiz-funnel-detalhado (1).md`
- Esse arquivo é o prompt técnico completo para construir o funil de quiz no Lovable.dev (React + Vite + TypeScript + Tailwind + Supabase), usando um exemplo de curso de francês como placeholder
- Substitui todo o conteúdo específico do exemplo (francês) pelo produto do aluno: headline, subheadline, perguntas, valores de resposta, tela de resultado, página de vendas, preço, benefícios (Decorados), depoimentos, labels do painel admin
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

Localização local: `C:\Users\Elen\Downloads\prompt-quiz-funnel-detalhado (1).md`

Esse arquivo deve ser lido a cada execução do comando para gerar a Fase 2.

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

Usar o slug do produto ativo (ex: `precifique-seu-taro`) como `--name` no deploy. Isso garante que a URL final seja `{slug}.vercel.app`.

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

## Como acrescentar entradas

Use o formato:

```markdown
## AAAA-MM-DD

### Título curto

- Ponto 1
- Ponto 2
```
