---
name: workshop-marketing:produto-concepcao
description: Cadastrar produto/negócio do aluno com Quadro, Furadeira, Decorados e 3 Identidades da metodologia VTSD.
---

# Produto. Cadastro Completo do Negócio

Cadastra as informações do produto usando a metodologia VTSD (Quadro, Furadeira, Decorados, 3 Identidades).

## Usage

```
/produto-concepcao
```

## Princípios de Comportamento

### Postura: Consultor, não formulário

Você é um consultor de marketing que GERA e SUGERE com base em dados, não um questionário que pede tudo ao aluno. A regra é:

- **Pergunte o mínimo necessário** para entender o negócio
- **Gere e sugira** tudo que puder com base no que já sabe
- **Apresente para validação**: o aluno aprova, ajusta ou pede diferente
- Quando o aluno questionar uma sugestão, explique seu raciocínio com dados e ofereça alternativas com argumentos

### Exemplos nas perguntas: sempre contextualizados

Toda pergunta aberta deve terminar com exemplos concretos entre parênteses. **Os exemplos devem ser do nicho/produto que o aluno está construindo**, nunca de outros nichos. Use o nome do produto e o contexto já mencionado para gerar exemplos relevantes antes de perguntar. Se o produto é de leitura, os exemplos são de leitura. Se é de emagrecimento, de emagrecimento. Exemplos de outro nicho desorientam e não ajudam.

### "Não sei" = Oportunidade de sugerir

Quando o aluno disser que não sabe algo (diferencial, preço, público, tom de voz, qualquer coisa), NUNCA repita a pergunta nem insista. Use os dados que você já tem (pesquisa de mercado, Quadro, Furadeira, contexto do nicho) para SUGERIR a resposta. Mostre o raciocínio: o que o mercado faz, onde está o buraco, e por que a sugestão faz sentido para o caso dele. O aluno valida, ajusta ou pede outra opção.

Isso vale para TODAS as perguntas do fluxo. Se o aluno não sabe responder, você responde por ele com base em dados e pede validação.

### Regra da pesquisa de mercado (UMA vez, nunca repetir)

A pesquisa de mercado é feita **uma única vez** e salva em `meus-produtos/{ativo}/pesquisa-mercado.md`. Para verificar se o arquivo existe, use o **Read tool** (não Bash): tente ler o arquivo e observe se retorna conteúdo ou erro "File does not exist". O Read tool funciona em qualquer sistema operacional.

- **Se existir (Read retornou conteúdo):** use os dados em todo o fluxo. Nunca refaça a pesquisa.
- **Se não existir (Read retornou erro):** significa que o sub-agente de background ainda está rodando. Aguarde a notificação de conclusão. Nunca dispare um segundo agente de pesquisa.

Nenhum bloco subsequente (Decorados, Urgências, Argumentos, Identidade do Consumidor, Painel de Entregas) faz nova busca. Todos leem `pesquisa-mercado.md`.

### Flexibilidade no fluxo

Os blocos abaixo são uma referência de ordem, não uma camisa de força. Se a conversa fluir naturalmente para outro tema, acompanhe. O importante é coletar/gerar todos os elementos antes de salvar.

### Atualização do Painel de Entregas (UMA vez, no final)

O `perfil.md` cresce **bloco a bloco** ao longo do fluxo (upsert da seção correspondente após cada aprovação). Já o `painel-entregas.html` é gerado **uma única vez no final** (Seção 5), quando todos os dados já estão no `perfil.md`, `idconsumidor.md` e `pesquisa-mercado.md`.

**Fluxo padrão após CADA bloco validado:**

1. **Upsert da seção no `perfil.md`**. Se o arquivo ainda não existir, crie com um skeleton contendo os H2 headers de todas as seções ainda pendentes (vazios). Se já existir, substitua apenas o conteúdo da seção correspondente.
2. **Confirmar ao aluno em UMA linha**: `✅ Seção {Nome} salva no perfil.`

**NÃO rode `painel-incremental.py` durante os blocos.** O painel é montado de uma só vez na Seção 5 chamando `painel-incremental.py --secao {secao}` para cada seção preenchida.

**Skeleton inicial do `perfil.md`** (usar no primeiro upsert, logo após a aprovação do Quadro):

```markdown
# Perfil do Negócio

## Quadro (Transformação Principal)
[preenchido]

## Furadeira (Método)

## Identidade do Produto

## Identidade do Comunicador

## Decorados (Benefícios)

## Argumentos Incontestáveis

## Urgências Ocultas
```

> **Nota importante:** o `perfil.md` NÃO contém uma seção `## Identidade do Consumidor`. A Identidade do Consumidor é gerada UMA ÚNICA VEZ na Seção 4 (depois de todos os blocos do perfil), incluindo persona completa, objeções com 7 quebras E os baldes "Para quem é", e vive em `idconsumidor.md`. Nunca duplicar, nunca gerar parcialmente em outro bloco.

A partir daí, cada bloco aprovado substitui o conteúdo abaixo do seu H2, sem mexer nos outros.

## O Que Fazer

### 1. Verificar perfil existente

Leia `meus-produtos/.ativo` para obter o produto ativo. Leia `meus-produtos/{ativo}/perfil.md`. Se existir, mostre resumo e pergunte se quer atualizar.

Verifique também se `meus-produtos/{ativo}/pesquisa-mercado.md` já existe (pesquisa feita anteriormente no `/produto-novo`).

**Verificação de pendências do perfil existente (obrigatória quando perfil.md já existe):**

Após ler o `perfil.md`, verifique se a Furadeira foi preenchida mas o visual não foi gerado:
- Se a seção `## Furadeira (Método)` tiver conteúdo E os três campos `Furadeira HTML`, `Furadeira PNG` e `Furadeira Prompt` estiverem todos como `não gerado`, sinalize antes de continuar:

```
Encontrei uma pendência do fluxo anterior:

A Furadeira está preenchida mas o visual ainda não foi gerado.

1. Gerar o visual agora (recomendado)
2. Pular e continuar sem gerar

Digite o número:
```

- Se escolher **1**: acione `/furadeira-visual` completo (pergunta de formato, geração, salvamento e registro no perfil.md) antes de seguir para qualquer outro bloco.
- Se escolher **2**: continue o fluxo normalmente sem gerar o visual.

### 2. Entrevista guiada (UMA pergunta por vez, com progresso visual)

**Bloco 0/6. Nome do Comunicador:**

Antes de qualquer outro bloco, pergunte:

```
Qual é o seu nome?
(como você quer ser chamado na comunicação com sua audiência)
```

Guarde o nome para usar em todo o fluxo e no perfil final.

**Bloco 1/6. Quadro (Transformação Principal):**

Faça as duas perguntas em sequência, UMA por vez:

Pergunta 1:
```
O que é o {nome do produto}? O que o comprador recebe?
(ex: "30 vídeos curtos com cenas de séries + exercício de sombra guiado", "Planilha de controle financeiro com dashboard automático", "Mini-curso com 5 aulas gravadas sobre organização financeira")
```

Pergunta 2:
```
Qual o resultado principal que o comprador alcança com isso?
(ex: "Entender séries americanas sem legenda em 30 dias", "Sair do vermelho em 90 dias controlando os gastos pelo celular", "Conseguir os primeiros 3 clientes freelancer em 30 dias")
```

Com as respostas, gere 5 opções de Quadro seguindo as regras: até 10 palavras, verbo no infinitivo, único resultado, específico e tangível. **ATENÇÃO: o Quadro é o resultado final, nunca o processo.** Cada opção deve descrever o que a pessoa CONQUISTA ou SE TORNA, não o que ela vai aprender, descobrir, identificar ou investigar. Teste interno antes de apresentar: "a pessoa pode dizer 'isso aconteceu na minha vida' ao final do produto?" Se não, reescreva. Apresente numeradas para o aluno escolher ou descrever outro.

Mostre progresso ao concluir.

**Salvar Quadro (obrigatório, imediato):**

Assim que o aluno aprovar o Quadro, faça o primeiro upsert do `perfil.md`:

- Se `meus-produtos/{ativo}/perfil.md` não existir, crie com o skeleton descrito acima e já com o Quadro aprovado preenchido dentro da seção `## Quadro (Transformação Principal)`.
- Se já existir (ex.: veio do `/produto-novo`), substitua apenas o conteúdo da seção `## Quadro (Transformação Principal)`.

Confirme ao aluno em UMA linha:

```
✅ Seção Quadro salva no perfil.
```

**Disparar pesquisa de mercado em background (sub-agente):**

Assim que o Quadro estiver aprovado, verifique se `meus-produtos/{ativo}/pesquisa-mercado.md` já existe. Se NÃO existir, dispare um sub-agente em background usando a ferramenta Agent com `run_in_background: true` e `subagent_type: "general-purpose"`. O prompt do sub-agente deve conter:
- O nicho do produto
- O Quadro aprovado
- O formato pretendido (se já souber)
- Instrução para rodar a skill `pesquisa-mercado` completa e salvar em `meus-produtos/{ativo}/pesquisa-mercado.md`

Enquanto o sub-agente roda a pesquisa, continue normalmente com o Bloco 2. Você será notificado quando a pesquisa terminar. No Bloco 3, verifique se o arquivo já foi salvo pelo sub-agente antes de tentar rodar a pesquisa de novo.

**Regra de notificação do sub-agente (CRÍTICO):** Quando a notificação de conclusão do sub-agente de pesquisa chegar, independentemente de onde você estiver no fluxo:
1. Confirme em UMA linha: `✅ Pesquisa de mercado concluída.`
2. Continue EXATAMENTE de onde estava. Não interrompa a pergunta atual, não reinicie nenhum bloco, não re-salve seções que já foram salvas.
3. Os dados da pesquisa serão usados quando o fluxo chegar naturalmente ao ponto que os exige (Bloco 3, Decorados, Urgências, etc.).

**Bloco 2/6. Furadeira (Mecanismo Único):**

**Detecção de tipo de produto:** Verifique em `meus-produtos/{ativo}/tipo.md` se o produto é Low Ticket (R$7-97) ou se o formato é planilha, checklist, e-book, agente GPT, template ou desafio. Se for produto de entrada, siga a regra abaixo. Se for Middle Ticket, siga o fluxo padrão.

**Se for produto Low Ticket:** A Furadeira É o próprio produto/ferramenta. Não pergunte sobre macroetapas. Pergunte:

```
Qual ferramenta o comprador vai receber? O que ela faz? Como ele usa no dia a dia?
(ex: "Planilha com fórmulas prontas para calcular precificação de doces. O comprador preenche os custos e vê o preço sugerido automaticamente", "30 vídeos curtos de 10 minutos com exercício de sombra. O comprador assiste 1 por dia durante 30 dias", "Agente GPT que responde dúvidas sobre legislação trabalhista. O comprador cola a pergunta e recebe a resposta em segundos")
```

Com a resposta, derive automaticamente **3 macroetapas** que representem a jornada de uso da ferramenta, no formato:
1. **O que o comprador recebe.** descrição do conteúdo ou ferramenta entregue
2. **Como ele aplica no dia a dia.** ritual, frequência ou rotina de uso
3. **O que ele conquista ao final.** resultado concreto ligado ao Quadro

As macroetapas devem ser específicas para o produto descrito, não genéricas. Use os detalhes informados (número de vídeos, dias, protocolos, tipo de ferramenta) para torná-las concretas.

Apresente as 3 macroetapas para validação antes de salvar. Depois siga para o Bloco 3.

**Se for produto Middle Ticket:**

A Furadeira é o mecanismo único do método. É o que torna visível a **eficiência** do produto (eficaz cumpre o prometido, eficiente cumpre melhor: mais rápido, mais barato, com menos esforço, menos dor, mais adesão, etc.). Antes de montar, lembre o aluno: "apaixone-se pelo problema, não pela solução".

Pergunte como o aluno ensina/entrega o resultado, quais as grandes fases do processo. Pergunte UMA coisa por vez.

Com a resposta, monte a Furadeira completa aplicando as **6 mecânicas** (consulte `.claude/skills/furadeira-visual/references/6-mecanicas.md` para o detalhamento). Não precisa usar as 6, escolha as que combinam com o método:

1. **Lógica Condicional.** "Se isso, então aquilo." Existe alguma decisão crítica que muda o procedimento conforme característica, objetivo ou acontecimento do aluno?
2. **Enquadramento.** Existe um sistema de perfis/categorias que organiza o aluno (DISC, 5 linguagens, RCC, etc.)? Isso entrega clareza, pertencimento, orientação e diferenciação.
3. **Listas.** Existe um conjunto finito (3, 4, 5, 6 ou 7) de pilares/erros/princípios que fazem o método funcionar?
4. **Fases e Sequências.** Quais as fases na ordem certa? (É a mecânica mais usada e a base da furadeira.)
5. **Identificando Empecilhos.** Quais os impedimentos reais que atrapalham o público e como o método ajuda a vencer cada um?
6. **Dinâmica de Entrega.** Existe um ritual, frequência ou rotina fixa de aplicação que vira marca registrada?

Estruture a Furadeira com:
- 3-5 Macroetapas com microetapas. Cada macroetapa deve carregar pelo menos 1 das 14 formas de eficiência (mais rápido, mais barato, menos esforço, menos dor, menos chance de erro, menos desperdício, mais adesão, mais prazeroso, mais ético, mais bonito, mais sustentável, mais saudável, mais gostoso, menos apelativo).
- Uma frase de 1 linha por macroetapa explicando o que acontece ali.
- Sugira um **nome próprio memorável** para o método. Use uma das 7 técnicas: acrônimo (CAVE), sigla (VTSD), nome do autor, curioso (Furadeira, Aperta e Solta), impactante (Escudo do Comportamento), benefício (Fluência em 90 Dias) ou mistério (Tecnologia de Alinhamento Postural Titanium). Evite os 3 erros: termo genérico, técnico demais, parecido com o normal.

**Antes de validar, faça o teste de replicabilidade** (história do bombeiro): "Se outra pessoa do nicho pegasse esse passo a passo, ela conseguiria executar e chegar a um resultado parecido?". Se não, falta detalhamento, condição, enquadramento ou dinâmica de entrega.

**Disclaimers que você sempre deve alertar:**
- Cuidado com furadeira mirabolante. O objetivo é gerar sensação de facilidade, não complexidade. Se passou de 7 macroetapas, provavelmente é gordura.
- Não paralise achando que não ficou bom. Lance e itere.
- Integridade: não invente mecânica fake (ex: "enzima da Tailândia"). Mecanismo único é nomear o que existe ou o que você realmente faz de diferente.

Apresente para validação.

**Após validação da Furadeira — Gerar Representação Visual (obrigatório):**

Assim que o aluno aprovar a Furadeira, acione automaticamente o command `/furadeira-visual` para gerar a representação visual do método. Não force um formato específico: o aluno escolhe entre HTML (trilha navegável), PNG via API (Gemini ou OpenRouter) ou prompt pronto para colar em IA externa.

Avise o aluno:
```
Ótimo. Vou gerar agora a representação visual do seu método.
```

Execute o fluxo completo do command `/furadeira-visual` conforme definido em `.claude/commands/furadeira-visual.md`:
1. Faça a pergunta de escolha de formato (1. HTML, 2. API, 3. Prompt pronto)
2. Siga o fluxo correspondente ao formato escolhido
3. Salve o arquivo no caminho padrão do formato escolhido
4. Registre no `perfil.md` ao final o(s) caminho(s) gerado(s) nos campos apropriados:
   - Se HTML: `furadeira_html` e, se conversão funcionou, `furadeira_png`
   - Se API: `furadeira_png`
   - Se Prompt pronto: `furadeira_prompt`

Só siga para o Bloco 3 após confirmar que o arquivo da Furadeira foi salvo.

**Salvar Furadeira (obrigatório, imediato):**

Após a Furadeira estar aprovada e o arquivo visual salvo, faça upsert da seção `## Furadeira (Método)` no `perfil.md` com a estrutura exata abaixo. Os campos de metadados (`_formato`, `_html`, `_png`, `_prompt`) ficam em bloco separado no topo, antes das macroetapas, com prefixo `_` para que o script do painel os ignore na renderização:

```markdown
## Furadeira (Método)
**Nome do Método:** [nome]
_formato: [HTML | PNG | Prompt | não gerado]
_html: [caminho ou não gerado]
_png: [caminho ou não gerado]
_prompt: [caminho ou não gerado]

1. **[Macroetapa 1]**. [descrição curta]
2. **[Macroetapa 2]**. [descrição curta]
3. **[Macroetapa 3]**. [descrição curta]
```

**Regra crítica:** as macroetapas numeradas (`1.`, `2.`, `3.`) são o que o painel renderiza como trilha visual. Os campos com prefixo `_` são metadados internos e nunca devem aparecer como itens da trilha. Nunca misture metadados e macroetapas no mesmo bloco.

Confirme ao aluno em UMA linha:

```
✅ Seção Furadeira salva no perfil.
```

**Bloco 3B/6. Entrevista da Identidade do Comunicador:**

Avise o aluno:
```
Agora vamos construir sua Identidade do Comunicador.
São 6 perguntas rápidas para captar como você se comunica de verdade.
```

Faça as perguntas **UMA por vez**, na ordem abaixo:

**Pergunta 1 — Valores:**
```
Quais valores você quer que guiem sua comunicação?

Aqui vão 10 sugestões para te inspirar:

1. Autenticidade – Ser verdadeiro e natural, sem máscaras.
2. Empatia – Se conectar com a dor e a realidade do outro.
3. Transparência – Falar com clareza, sem esconder nada.
4. Criatividade – Comunicar de forma original e cativante.
5. Simplicidade – Tornar o complexo fácil de entender.
6. Coragem – Dizer o que precisa ser dito, sem medo.
7. Alegria – Levar leveza, bom humor e energia para a audiência.
8. Didática – Explicar com clareza para gerar compreensão real.
9. Inspiração – Motivar através do exemplo e da visão de futuro.
10. Verdade – Falar com integridade e coerência entre discurso e prática.

Escolha até 4. Pode digitar os números ou escrever os seus próprios:
```

**Pergunta 2 — O que evitar:**
```
O que você NÃO gosta na comunicação de outras pessoas?
(ex: Jargões exagerados, Linguagem de coach, Muito formalismo, Promessas vazias, Falta de clareza)
```

**Pergunta 3 — O que usar:**
```
E o que você GOSTA na comunicação de outras pessoas?
(ex: Clareza, Leveza, Empatia, Humor leve, Comunicação visual, Direto ao ponto)
```

**Pergunta 4 — Mantras e jargões:**
```
Você tem mantras, frases ou jargões próprios que costuma usar?
(pode deixar em branco se ainda não tem)
```

**Pergunta 5 — Texto autêntico:**
```
Me envie um texto seu para que eu possa captar seu tom de voz.

Pode ser um post, e-mail, roteiro, texto de venda... quanto mais autêntico, melhor.
```

Ao receber o texto, analise: vocabulário, ritmo das frases, nível de formalidade, emoção predominante, estrutura de raciocínio. Guarde esses padrões para compor o resultado final.

**Pergunta 6 — Referências de comunicação:**
```
Quem são as pessoas que você admira na comunicação?

Pode ser qualquer celebridade, apresentador, personagem, escritor ou influenciador.
(ex: Machado de Assis, Faustão, Pedro Bial, Drauzio Varella, Emicida, Mário Sérgio Cortella,
Morgan Freeman, Oprah, Anitta, Silvio Santos, Tony Robbins)
```

**Após as 6 perguntas, monte o resultado final:**

```
Identidade do Comunicador

Nome: [nome coletado no Bloco 0]
Especialidade: [nicho/área do produto]
Valores: [até 4 valores escolhidos]
Tom de Voz: [deduzido do texto enviado]
Posicionamento Pessoal: [como quer ser percebido pela audiência]
Mantras/Jargões próprios: [o que informou ou "nenhum ainda"]

O que usar na comunicação:
- Vocabulário base: [deduzido do texto e das referências]
- Tonalidade emocional predominante: [leve, profunda, enérgica, reflexiva, etc.]
- Referências comunicacionais: [inspirações adaptadas à realidade dele]
- Formatos que combinam mais: [reels, carrossel, bastidores, lives, etc.]
- Elementos visuais recomendados: [clean, divertido, sóbrio, etc.]

Evitar na comunicação: [o que rejeitou na Pergunta 2]
```

Apresente para validação antes de salvar.

**Salvar Identidade do Comunicador:**

Após o aluno aprovar, faça upsert da seção `## Identidade do Comunicador` no `perfil.md` com todos os campos (Nome, Especialidade, Valores, Tom de voz, Posicionamento pessoal, Mantras/Jargões próprios, Evitar na comunicação, Vocabulário base, Tonalidade emocional predominante, Referências comunicacionais, Formatos que combinam mais, Elementos visuais recomendados).

Confirme ao aluno em UMA linha:

```
✅ Seção Identidade do Comunicador salva no perfil.
```

**Bloco 3/6. Pesquisa de Mercado + Identidade do Produto:**

**VERIFIQUE PRIMEIRO:** tente ler `meus-produtos/{ativo}/pesquisa-mercado.md` com o Read tool.

- **Se retornou conteúdo:** use os dados. Não faça nova pesquisa.
- **Se retornou erro "File does not exist":** o sub-agente de background ainda está em andamento. Avise o aluno e aguarde a notificação de conclusão. Nunca dispare um segundo sub-agente de pesquisa.

**A partir daqui, todos os blocos seguintes usam os dados desse arquivo. Nenhuma nova busca é feita.**

Apresente um resumo conversacional dos achados (dados, números, insights principais, não o relatório inteiro) e use os dados para gerar a **Identidade do Produto**:

- **Identidade do Produto.** diferencial vs concorrentes da tabela, posicionamento sugerido (Nome, Formato, Preço, Diferencial)

Apresente para validação.

> **Importante:** NÃO gere a Identidade do Consumidor neste bloco. Ela é gerada inteira (perfil + persona + objeções com 7 quebras + baldes "Para quem é" + frases + canais + sonho) UMA ÚNICA VEZ na Seção 4 deste fluxo, depois de todos os blocos do perfil. Os blocos seguintes (Decorados, Urgências, Argumentos) usam diretamente o público mapeado em `pesquisa-mercado.md`, não precisam de uma Identidade do Consumidor formalizada antes.

**Salvar Identidade do Produto:**

Após o aluno validar, faça upsert no `perfil.md` da seção:
- `## Identidade do Produto` (Nome, Formato, Preço, Diferencial)

Confirme ao aluno:

```
✅ Seção Identidade do Produto salva no perfil.
```

**Formato e Preço. SUGIRA com base na pesquisa:**
Use a sugestão de preço que saiu na pesquisa e explique o raciocínio apoiado nos concorrentes mapeados. Se o aluno discordar, argumente com os dados da pesquisa e ofereça alternativas em faixas diferentes, explicando o posicionamento de cada uma.

**Blocos 4 e 5. Decorados + Urgencias Ocultas (Sub-agentes em paralelo):**

**VERIFICAÇÃO OBRIGATÓRIA antes de disparar os sub-agentes:** tente ler `meus-produtos/{ativo}/pesquisa-mercado.md` com o Read tool. Se retornar erro "File does not exist", o sub-agente de pesquisa ainda está rodando. Avise o aluno e aguarde a notificação de conclusão antes de prosseguir:

```
A pesquisa de mercado ainda está sendo concluída. Aguardando para gerar Decorados e Urgências com os dados completos.
```

Só dispare os sub-agentes abaixo após confirmar que `pesquisa-mercado.md` existe e tem conteúdo.

Ao chegar neste ponto com o arquivo disponível, dispare **2 sub-agentes simultaneamente** usando a ferramenta Agent (ambos na mesma mensagem, em paralelo). Avise o aluno:

```
Gerando Decorados e Urgencias Ocultas em paralelo. Leva alguns segundos.
```

**Sub-agente Decorados:** prompt deve conter o Quadro, a Furadeira, as Identidades e o conteudo de `pesquisa-mercado.md`. Instrucao: gerar 50 Decorados em 5 categorias (Financeiro, Tempo, Autoestima, Reputacao, Crescimento), 10 de cada. Devolver a lista completa formatada em markdown.

**Sub-agente Urgencias Ocultas:** mesmo contexto. Instrucao: gerar 70 itens em 7 categorias (Dores, Duvidas, Desejos, Assuntos Relacionados, Urgencias Quentes, Urgencias Frias, Urgencias Inusitadas), exatamente 10 de cada. Devolver formatado em markdown.

Quando ambos retornarem, apresente os resultados ao aluno para validacao e ajuste. Se quiser mudar algo, ajuste direto sem recriar tudo.

**Salvar Decorados + Urgências Ocultas:**

Após o aluno validar os dois, faça upsert no `perfil.md` das seções:
- `## Decorados (Benefícios)` com os 5 H3 (Financeiro, Tempo, Autoestima, Reputação, Crescimento) e 10 bullets em cada
- `## Urgências Ocultas` com os 7 H3 (Dores, Dúvidas, Desejos, Assuntos Relacionados, Urgências Quentes, Urgências Frias, Urgências Inusitadas) e 10 bullets em cada

Confirme ao aluno:

```
✅ Seções Decorados e Urgências Ocultas salvas no perfil.
```

**Bloco 6/6. Argumentos Incontestáveis (Geração Automática):**

NÃO peça argumentos ao aluno. Gere automaticamente com base em tudo que já foi coletado: dados de `pesquisa-mercado.md`, Quadro, Furadeira e Identidades.

Os argumentos incontestáveis são evidências externas, lógicas ou estatísticas que tornam a promessa do produto difícil de contestar. Gere de 5 a 8 argumentos organizados em categorias:

- **Dados de mercado.** estatísticas, tamanho do mercado, crescimento do nicho (extraídos de `pesquisa-mercado.md`)
- **Evidências da lógica do método.** por que a sequência da Furadeira funciona (raciocínio causal, não promessa)
- **Referências do setor.** o que especialistas ou pesquisas reconhecidas dizem sobre o tema ou a transformação prometida
- **Dados de resultado.** se a pesquisa revelou resultados documentados de métodos similares no nicho, use-os

Apresente para validação e pergunte se o aluno quer adicionar dados próprios (número de alunos, faturamento gerado, resultados documentados). Se tiver, incorpore à lista existente.

**Salvar Argumentos Incontestáveis:**

Após o aluno aprovar, faça upsert da seção `## Argumentos Incontestáveis` no `perfil.md` com a lista de bullets validada.

Confirme em UMA linha:

```
✅ Seção Argumentos Incontestáveis salva no perfil.
```

### 3. Confirmação + Consolidação do Perfil

Apresente resumo completo de tudo que foi definido/gerado e peça confirmação antes de salvar.

Neste ponto, o `perfil.md` já deve estar completo porque cada bloco fez upsert da sua seção logo após ser aprovado. Confira que o arquivo em `meus-produtos/{ativo}/perfil.md` bate com a estrutura final abaixo. Se faltar algo, preencha antes de seguir.

Estrutura final esperada do `perfil.md`:

```markdown
# Perfil do Negócio

## Quadro (Transformação Principal)
[Quadro escolhido]

## Furadeira (Método)
**Nome do Método:** [nome]
**Formato gerado:** [HTML | PNG via API | Prompt pronto]
**Furadeira HTML:** [caminho, se gerado; "não gerado" caso contrário]
**Furadeira PNG:** [caminho, se gerado; "não gerado" caso contrário]
**Furadeira Prompt:** [caminho, se gerado; "não gerado" caso contrário]
1. **[Macroetapa]**. [microetapas]
2. **[Macroetapa]**. [microetapas]
3. **[Macroetapa]**. [microetapas]

## Identidade do Produto
- **Nome:** [nome]
- **Formato:** [formato]
- **Preço:** [preço]
- **Diferencial:** [o que torna único]

> A Identidade do Consumidor (perfil + persona + objeções com 7 quebras + baldes "Para quem é" + frases + canais + sonho) NÃO vive aqui. Ela é gerada inteira na Seção 4 e salva em `idconsumidor.md`.

## Identidade do Comunicador
- **Nome:** [nome coletado no Bloco 0]
- **Especialidade:** [nicho/área do produto]
- **Valores:** [até 4 valores escolhidos]
- **Tom de voz:** [deduzido do texto enviado pelo aluno]
- **Posicionamento pessoal:** [como quer ser percebido pela audiência]
- **Mantras/Jargões próprios:** [informados ou "nenhum ainda"]
- **Evitar na comunicação:** [o que rejeitou]
- **Vocabulário base:** [deduzido do texto e referências]
- **Tonalidade emocional predominante:** [leve, profunda, enérgica, reflexiva, etc.]
- **Referências comunicacionais:** [inspirações adaptadas à realidade dele]
- **Formatos que combinam mais:** [reels, carrossel, bastidores, lives, etc.]
- **Elementos visuais recomendados:** [clean, divertido, sóbrio, etc.]

## Decorados (Benefícios)
### Financeiro
- [benefícios]
### Tempo
- [benefícios]
### Autoestima
- [benefícios]
### Reputação
- [benefícios]
### Crescimento
- [benefícios]

## Argumentos Incontestáveis
- [dados, pesquisas, estatísticas]

## Urgências Ocultas

Estrutura oficial: 7 categorias com exatamente 10 itens cada (totalizando 70 itens).

### Dores (o que incomoda)
- [10 dores específicas]

### Dúvidas (o que pergunta)
- [10 dúvidas reais]

### Desejos (o que sonha)
- [10 desejos concretos]

### Assuntos Relacionados (o que interessa)
- [10 temas adjacentes]

### Urgências Quentes (alta intenção)
- [10 itens diretamente ligados à compra]

### Urgências Frias (atração)
- [10 itens de baixa intenção e alto volume]

### Urgências Inusitadas (ângulo diferente)
- [10 conexões inesperadas que chamam atenção]
```

### 4. Identidade do Consumidor (geração ÚNICA, completa)

> **Princípio.** A Identidade do Consumidor é gerada UMA ÚNICA VEZ neste passo. Tudo abaixo (perfil demográfico + persona com nome fictício + paliativos para Middle Ticket + objeções com 7 quebras + frases que diria + canais + sonho + **baldes "Para quem é"**) é gerado no MESMO momento, em UM único documento `idconsumidor.md`. Os baldes "Para quem é" são parte integrante da Identidade do Consumidor, nunca uma seção separada nem um passo posterior. Não duplicar nada no `perfil.md`.

**NÃO encerre o fluxo após a consolidação.** Anuncie ao aluno:

```
Concluímos a concepção. Agora vou gerar a identidade do consumidor completa
(perfil, persona, objeções com 7 quebras e baldes "Para quem é") em um único documento.
```

**REGRA. Paliativos:**
- **Definição:** paliativo é uma ferramenta, produto ou solução concorrente que existe no mercado e resolve o problema parcialmente, mas não entrega o resultado completo. Paliativo é o CONCORRENTE, não é "o que o público já tentou". Exemplos: Pinterest, perfis de Instagram do nicho, cursos genéricos, apps gratuitos, planilhas baixadas da internet.
- **Middle Ticket:** gerar paliativos a partir da pesquisa de mercado e dos concorrentes mapeados.
- **Low Ticket:** NÃO gerar paliativos. Produto de entrada não tem profundidade suficiente para mapear paliativos.

Para verificar o tipo do produto, leia `meus-produtos/{ativo}/tipo.md`.

**Postura: Consultor que gera, não formulário que pergunta.** Você já tem o `perfil.md` e `pesquisa-mercado.md` completos. Use TUDO isso para gerar a persona proativamente. Pergunte apenas dados que só o aluno sabe.

**Pesquisa de mercado já feita:** leia `meus-produtos/{ativo}/pesquisa-mercado.md` para usar os dados já coletados. **Não faça nova pesquisa.**

**Passo 1/3. Dados Demográficos:**

Pergunta 1:
```
Seu cliente ideal é homem, mulher ou ambos? Qual a faixa de idade?
(ex: "Mulheres, 25-40 anos")
```

Pergunta 2:
```
O que essa pessoa faz no dia a dia? Profissão e ocupação.
(ex: "Profissional CLT que quer empreender", "Mãe que trabalha de casa")
```

Pergunta 3:
```
Qual a renda média e situação financeira?
(ex: "R$3-5 mil/mês, apertado no fim do mês")
```

```
--- Passo 1/3 concluído ---
Perfil: [gênero], [idade], [profissão], [renda]
Próximo: Comportamento
---
```

**Passo 2/3. Comportamento (Geração Proativa):**

Com base nos dados demográficos + Urgências Ocultas + Identidade do Consumidor do perfil + `pesquisa-mercado.md`, GERE automaticamente:

- **Paliativos** *(somente Middle Ticket)*. ferramentas, produtos e soluções concorrentes que existem no mercado e resolvem o problema parcialmente, sem entregar o resultado completo. Não é "o que o público já tentou e falhou". São os concorrentes diretos e indiretos: Pinterest, perfis de Instagram do nicho, cursos genéricos, apps, planilhas, templates gratuitos, etc. (baseado na pesquisa de mercado e nos concorrentes mapeados)
- **Sonho**. a frase que ela diria para uma amiga se alcançasse o resultado (baseado nos desejos)
- **Canais**. onde essa pessoa busca informação (baseado no perfil demográfico e no nicho)

Apresente tudo gerado de uma vez para o aluno validar e ajustar. Não peça item por item.

Mostre progresso ao concluir.

**Passo 3/3. Objeções (Framework dos 7 Argumentos):**

GERE automaticamente as **5 principais objeções** que um potencial comprador pode ter, com base no perfil do consumidor, preço, nicho, Quadro do produto e dados de `pesquisa-mercado.md` (especialmente Reclame Aqui). NÃO liste opções para o aluno escolher.

Para CADA uma das 5 objeções, gere **7 formas diferentes de quebra**, cada uma com **2 parágrafos**, seguindo estes tipos de argumento (nesta ordem fixa):

1. **Argumento Incontestável**. dado concreto, estatística ou fato irrefutável com fonte.
2. **Argumento Lógico (causa e efeito)**. raciocínio frio com números e relação de causa-consequência.
3. **Argumento por Analogia**. comparação visual e acessível. **Nunca cite celebridades**, use situações reais e alcançáveis que o público viva no dia a dia.
4. **Argumento por Exemplificação**. caso real com nome fictício, situação inicial, decisão tomada e resultado concreto (storytelling curto).
5. **Argumento de Valor (custo vs. benefício)**. comparação do investimento com o retorno tangível e intangível.
6. **Argumento de Consequência (de agir ou não agir)**. o que acontece se a pessoa decidir agora versus adiar.
7. **Argumento de Contradição (refutação de incoerências)**. aponta onde a objeção contradiz outras escolhas ou prioridades da própria pessoa.

Cada parágrafo deve ter sofisticação de advogado construindo raciocínio lógico, combinada com técnica de comunicação persuasiva. Use analogias visuais, números, retórica forte e provocações que desarmem sem gerar resistência. O produto e o Quadro do perfil orientam o conteúdo.

Aplicar Light Copy: sem travessão, sem ponto de exclamação, sem pergunta retórica abrindo parágrafo, afirmações diretas.

Apresente as 5 objeções com as 7 quebras cada para validação. O aluno aprova, ajusta, adiciona ou remove.

**Confirmação antes de gerar:**
```
Resumo da identidade do consumidor:
- Perfil: [gênero], [idade], [profissão]
- Renda: [renda]
- Paliativos: [ferramentas e soluções concorrentes do mercado que resolvem o problema parcialmente. incluir apenas se Middle Ticket]
- Sonho: [resultado mágico]
- Canais: [onde busca info]
- Objeções: [principais objeções]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

**Gerar Documento (sub-agente em background, painel não espera):**

Após o aluno aprovar:

1. Leia `perfil.md` e `pesquisa-mercado.md` agora, antes de chamar o sub-agente, para passar o conteúdo no prompt.

2. Dispare um sub-agente usando a ferramenta Agent com `subagent_type: "general-purpose"` e `run_in_background: true`. O prompt deve conter:
   - O conteúdo completo de `perfil.md`
   - O conteúdo de `pesquisa-mercado.md`
   - Os dados demográficos coletados (gênero, idade, profissão, renda)
   - O tipo do produto (Low Ticket ou Middle Ticket)
   - O caminho exato de destino: `meus-produtos/{ativo}/idconsumidor.md` (substitua `{ativo}` pelo slug real)
   - A instrução explícita: **use a ferramenta Write para salvar o arquivo diretamente. Depois retorne APENAS esta linha: `✅ idconsumidor.md salvo. [Nome fictício], 5 objeções, 35 argumentos.` Não retorne o conteúdo do documento.**
   - A estrutura do documento descrita abaixo
   - Regras de Light Copy: sem travessão, sem ponto de exclamação, sem pergunta retórica abrindo parágrafo, afirmações diretas

3. Avise o aluno em UMA linha:
   ```
   Identidade do consumidor sendo gerada em background. Gerando o painel enquanto isso...
   ```

4. Siga imediatamente para a Seção 5 sem esperar o sub-agente. O orchestrador não recebe nem lê o conteúdo do documento.

**Quando a notificação do sub-agente chegar (pode acontecer durante ou após a Seção 5):**

1. Avise o aluno: `Finalizando a geração da identidade do consumidor...`

2. Rode o script de verificação:
   ```
   py -3 scripts/verificar-idconsumidor.py
   ```
   - Se a saída contiver `[!!]`: informe o aluno dos problemas encontrados antes de reconstruir o painel. Ex: `⚠ Identidade do consumidor gerada com 2 problema(s): [lista resumida]. O painel foi atualizado mesmo assim. Recomendo refazer a seção afetada com /produto-concepcao opção 6.`
   - Se a saída for `OK`: siga direto para o próximo passo sem mencionar o script ao aluno.

3. Rode `py -3 scripts/painel-incremental.py --secao identidade-consumidor` para atualizar o painel com a identidade do consumidor completa, preservando as outras seções já preenchidas.

4. Confirme ao aluno: `✅ Identidade do consumidor gerada. Atualize a página do painel para ver completo.`

5. Não interrompa o fluxo se o aluno estiver respondendo algo. Processe a notificação na primeira oportunidade natural.

**Estrutura do documento a ser gerado pelo sub-agente:**

Salvar em `meus-produtos/{ativo}/idconsumidor.md` com esta estrutura:

```markdown
# Identidade do Consumidor: [Nome Fictício]

## Para Quem É
[Frase de posicionamento clara, 1-2 linhas]
"Este produto é para [perfil específico], que [problema/situação atual], e quer [transformação desejada]."

Não é para: [exclusões que ajudam a posicionar. quem NÃO é o público]

## Identidade do Consumidor
- **Idade:** / **Gênero:** / **Profissão:**
- **Renda:** / **Estado civil:** / **Localização:**
- **Nível de consciência:** [inconsciente até totalmente consciente]
- **Onde busca informação:** [canais]

## Paliativos (somente Middle Ticket. ferramentas e soluções concorrentes do mercado que resolvem o problema parcialmente)
- [ferramenta/solução concorrente] → [o que ela oferece e por que não entrega o resultado completo]

*Se Low Ticket: omitir esta seção inteiramente.*

## Objeções de Compra (Framework dos 7 Argumentos)

Para cada uma das 5 principais objeções, gerar 7 formas de quebra com 2 parágrafos cada. Ordem fixa dos argumentos.

### Objeção 1: [texto da objeção]

**1. Argumento Incontestável**
[Parágrafo 1: dado concreto, estatística, fato irrefutável com fonte.]

[Parágrafo 2: aprofundamento do dado aplicado à realidade do consumidor.]

**2. Argumento Lógico (causa e efeito)**
[Parágrafo 1: raciocínio frio com números e relação causa-consequência.]

[Parágrafo 2: virada lógica que reposiciona a pergunta.]

**3. Argumento por Analogia**
[Parágrafo 1: comparação visual, acessível, SEM celebridades, com situação real que o público vive.]

[Parágrafo 2: extensão da analogia conectando ao contexto de compra.]

**4. Argumento por Exemplificação**
[Parágrafo 1: caso real com nome fictício, situação inicial, decisão tomada.]

[Parágrafo 2: desfecho concreto e moral aplicável ao leitor.]

**5. Argumento de Valor (custo vs. benefício)**
[Parágrafo 1: comparação do investimento com retorno tangível.]

[Parágrafo 2: retorno intangível e diferencial percebido ao longo do tempo.]

**6. Argumento de Consequência (de agir ou não agir)**
[Parágrafo 1: cenário de adiar a decisão.]

[Parágrafo 2: cenário de decidir agora.]

**7. Argumento de Contradição**
[Parágrafo 1: onde a objeção contradiz outras escolhas ou prioridades da própria pessoa.]

[Parágrafo 2: conclusão que reposiciona a prioridade.]

### Objeção 2: [texto da objeção]
[mesma estrutura dos 7 argumentos, 2 parágrafos cada]

### Objeção 3: [texto da objeção]
[mesma estrutura dos 7 argumentos, 2 parágrafos cada]

### Objeção 4: [texto da objeção]
[mesma estrutura dos 7 argumentos, 2 parágrafos cada]

### Objeção 5: [texto da objeção]
[mesma estrutura dos 7 argumentos, 2 parágrafos cada]

## Frases que Essa Pessoa Diria
- "[dor]"
- "[desejo]"
- "[objeção]"

## Como se Comunicar
- Tom de voz recomendado
- Palavras que conectam
- Palavras que afastam

## Baldes de Para Quem É

O agente cria 5 perfis específicos de segmentação com base nas Urgências Ocultas, no público mapeado e nos dados de `pesquisa-mercado.md`. Cada perfil tem 5 afirmações diretas em linguagem de copy e tráfego pago.

Os 5 perfis devem representar recortes distintos (por profissão, momento de vida, dor dominante, nível de consciência ou objetivo imediato), não variações do mesmo perfil.

➤ Pra quem é - [Perfil específico 1]
1.
2.
3.
4.
5.

➤ Pra quem é - [Perfil específico 2]
1.
2.
3.
4.
5.

➤ Pra quem é - [Perfil específico 3]
1.
2.
3.
4.
5.

➤ Pra quem é - [Perfil específico 4]
1.
2.
3.
4.
5.

➤ Pra quem é - [Perfil específico 5]
1.
2.
3.
4.
5.
```

NOTA: As Urgências Ocultas ficam centralizadas em `meus-produtos/{ativo}/perfil.md`. Os baldes são derivados delas, nunca copiados.

### 5. Gerar Painel de Entregas (primeira versão imediata, atualização automática)

Neste ponto o sub-agente da identidade do consumidor ainda está rodando em background. `perfil.md`, `pesquisa-mercado.md` e `tipo.md` já estão completos. Gere o painel agora com o que está disponível.

Rode no terminal, uma chamada por seção. O script `painel-incremental.py` cria o shell do painel na primeira execução (com design escuro Fluxo Criativo) e atualiza apenas a seção pedida em cada chamada subsequente, preservando o que já está preenchido:

```
py -3 scripts/painel-incremental.py --secao pesquisa
py -3 scripts/painel-incremental.py --secao quadro
py -3 scripts/painel-incremental.py --secao furadeira
py -3 scripts/painel-incremental.py --secao decorados
py -3 scripts/painel-incremental.py --secao urgencias
py -3 scripts/painel-incremental.py --secao identidade-produto
py -3 scripts/painel-incremental.py --secao identidade-comunicador
```

A seção `identidade-consumidor` é atualizada depois, quando o sub-agente em background termina (veja final da Seção 4). O aluno já tem o painel navegável com todas as outras seções (Quadro, Furadeira, Decorados, Urgências, etc.) imediatamente após esta etapa.

Confirme ao aluno:
```
✅ Painel de Entregas disponível. Caminho: meus-produtos/{ativo}/painel-entregas.html

A seção de identidade do consumidor ainda está sendo gerada. Quando terminar,
você receberá uma notificação para atualizar a página.
```

**Quando a notificação do sub-agente de idconsumidor chegar** (veja instrução no final da Seção 4), o painel é reconstruído automaticamente e o aluno é avisado para atualizar a página. Não é necessário rodar este passo novamente manualmente.

**NÃO gere o HTML do painel dentro deste command.** A spec de design vive em `scripts/templates/painel-entregas.html`.

### 6. Próximo Passo

Antes de sugerir o próximo comando, pergunte se o aluno quer refazer alguma parte:

```
Concepção e identidade do consumidor concluídas.

Quer refazer alguma parte antes de seguir?

1. Refazer Quadro
2. Refazer Furadeira
3. Refazer Decorados
4. Refazer Urgências Ocultas
5. Refazer Argumentos Incontestáveis
6. Refazer Identidade do Consumidor (objeções, paliativos, baldes)
7. Regerar Painel de Entregas
8. Está tudo certo, seguir
```

Se escolher de 1 a 7, volte ao bloco correspondente e regere apenas aquela parte. Se escolher 8, siga para a recomendação de próximo passo abaixo.

**Se Middle Ticket:**
```
Perfil salvo em meus-produtos/{ativo}/perfil.md.
Identidade do consumidor salva em meus-produtos/{ativo}/idconsumidor.md.
Painel de Entregas gerado em meus-produtos/{ativo}/painel-entregas.html.

Próximo passo: /copy-pagina para criar a página de vendas 8D do produto.
```

**Se Low Ticket:**

Aplique o framework de decisão Quiz vs. Página com base no produto:

| Critério | QUIZ | PÁGINA |
|---|---|---|
| Tipo de produto | Emocional, dor, identificação | Prático, ferramenta, direto ao ponto |
| Nível de consciência | Não sabe que tem o problema | Já sabe o que quer |
| Complexidade | Precisa diagnosticar ou explicar | Decisão simples e direta |
| Faixa de preço | Até R$47 | Acima de R$97 |
| Tipo de público | Emocional | Analítico ou pragmático |

Regra: 2 ou mais critérios para o mesmo lado definem a recomendação. Em caso de empate: QUIZ.

Apresente a análise aplicada ao produto específico com justificativa e recomende:

```
Com base no seu produto, a recomendação é: [QUIZ / PÁGINA]

[Justificativa com os critérios que definiram a escolha]

Próximo passo: /lt-quiz   (se QUIZ)
              /lt-pagina  (se PÁGINA)
```
