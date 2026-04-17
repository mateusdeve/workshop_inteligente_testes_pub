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

### "Não sei" = Oportunidade de sugerir

Quando o aluno disser que não sabe algo (diferencial, preço, público, tom de voz, qualquer coisa), NUNCA repita a pergunta nem insista. Use os dados que você já tem (pesquisa de mercado, Quadro, Furadeira, contexto do nicho) para SUGERIR a resposta. Mostre o raciocínio: o que o mercado faz, onde está o buraco, e por que a sugestão faz sentido para o caso dele. O aluno valida, ajusta ou pede outra opção.

Isso vale para TODAS as perguntas do fluxo. Se o aluno não sabe responder, você responde por ele com base em dados e pede validação.

### Regra da pesquisa de mercado (UMA vez, nunca repetir)

A pesquisa de mercado é feita **uma única vez** e salva em `meus-produtos/{ativo}/pesquisa-mercado.md`. Antes de qualquer coisa, verifique se esse arquivo já existe:

- **Se existir:** leia o arquivo e use os dados em todo o fluxo. Nunca refaça a pesquisa.
- **Se não existir:** rode a pesquisa completa no Bloco 3 e salve o arquivo. A partir daí, todos os blocos seguintes leem o arquivo salvo.

Nenhum bloco subsequente (Decorados, Urgências, Argumentos), nem o `/produto-consumidor`, faz nova busca. Todos leem `pesquisa-mercado.md`.

### Flexibilidade no fluxo

Os blocos abaixo são uma referência de ordem, não uma camisa de força. Se a conversa fluir naturalmente para outro tema, acompanhe. O importante é coletar/gerar todos os elementos antes de salvar.

## O Que Fazer

### 1. Verificar perfil existente

Leia `meus-produtos/.ativo` para obter o produto ativo. Leia `meus-produtos/{ativo}/perfil.md`. Se existir, mostre resumo e pergunte se quer atualizar.

Verifique também se `meus-produtos/{ativo}/pesquisa-mercado.md` já existe (pesquisa feita anteriormente no `/produto-novo`).

### 2. Entrevista guiada (UMA pergunta por vez, com progresso visual)

**Bloco 1/6. Quadro (Transformação Principal):**

Pergunte:
- O que o aluno vende (produto/serviço)
- Qual a transformação principal que o cliente alcança

Com as respostas, gere 5 opções de Quadro seguindo as regras: até 10 palavras, verbo no infinitivo, único resultado, específico e tangível. **ATENÇÃO: o Quadro é o resultado final, nunca o processo.** Cada opção deve descrever o que a pessoa CONQUISTA ou SE TORNA, não o que ela vai aprender, descobrir, identificar ou investigar. Teste interno antes de apresentar: "a pessoa pode dizer 'isso aconteceu na minha vida' ao final do produto?" Se não, reescreva. Apresente numeradas para o aluno escolher ou descrever outro.

Mostre progresso ao concluir.

**Bloco 2/6. Furadeira (Mecanismo Único):**

**Detecção de tipo de produto:** Verifique em `meus-produtos/{ativo}/tipo.md` se o produto é Low Ticket (R$7-97) ou se o formato é planilha, checklist, e-book, agente GPT, template ou desafio. Se for produto de entrada, siga a regra abaixo. Se for Middle Ticket, siga o fluxo padrão.

**Se for produto Low Ticket:** A Furadeira É o próprio produto/ferramenta. Não pergunte sobre macroetapas. Pergunte: "Qual ferramenta o comprador vai receber? O que ela faz? Como ele usa no dia a dia?" Registre no perfil: "A ferramenta é a Furadeira. [tipo da ferramenta + o que resolve + como o comprador usa]". Depois siga para o Bloco 3.

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

**Após validação da Furadeira — Gerar Trilha Visual (obrigatório):**

Assim que o aluno aprovar a Furadeira, acione automaticamente a skill `furadeira-visual` para gerar a representação visual do método como trilha de jornada.

Avise o aluno:
```
Ótimo. Vou gerar agora a trilha visual do seu método.
```

Execute o fluxo completo da skill `furadeira-visual`:
1. Pergunte a paleta de cores preferida (1 pergunta numerada)
2. Gere o HTML da trilha visual com o template da skill
3. Salve em `meus-produtos/{ativo}/entregas/furadeira-visual.html`
4. Converta para PNG: tente via `playwright`, `puppeteer` ou script `scripts/html-to-png.py` se disponível no ambiente
5. Se a conversão funcionar: salve em `meus-produtos/{ativo}/entregas/furadeira-visual.png` e confirme os dois caminhos
6. Se a conversão falhar: salve apenas o HTML e informe: "A versão HTML está salva. Para exportar como imagem, abra no navegador e use Ctrl+P → Salvar como PDF, ou Print Screen."
7. Registre os caminhos gerados no `perfil.md` ao final (campos: `furadeira_html` e `furadeira_png`)

Só siga para o Bloco 3 após confirmar que o HTML foi salvo.

**Bloco 3/6. Pesquisa de Mercado + Identidades e Posicionamento:**

**VERIFIQUE PRIMEIRO:** se `meus-produtos/{ativo}/pesquisa-mercado.md` já existe (criado no `/produto-novo`), leia o arquivo e use os dados. Não faça nova pesquisa.

Se o arquivo não existir, rode agora:

Pergunte brevemente quem é o público-alvo do aluno.

Avise o aluno:
```
Vou fazer uma pesquisa de mercado completa agora.
Visitando Reclame Aqui, Instagram dos concorrentes, páginas de venda e fontes do nicho.
Leva alguns minutos. Esses dados serão usados em todas as etapas seguintes.
```

Pesquise e colete obrigatoriamente:
- Dados gerais do mercado (tamanho, crescimento, tendências)
- Mínimo 10 concorrentes com: nome, link do Instagram, link da página de vendas, faixa de preço praticada
- Oportunidades identificadas (ângulos pouco explorados, nichos adjacentes, formatos em alta)
- Cuidados e riscos do nicho (saturação, regulatórios, promessas problemáticas)
- Resumo das reclamações do Reclame Aqui dos principais produtores (problemas reais de entrega, resultado, suporte)
- Público real (demografias, comportamento de compra, canais de consumo)
- Faixa de preço sugerida com justificativa baseada nos concorrentes

Salve tudo em `meus-produtos/{ativo}/pesquisa-mercado.md`.

**A partir daqui, todos os blocos seguintes usam os dados desse arquivo. Nenhuma nova busca é feita.**

Apresente um resumo conversacional dos achados (dados, números, insights principais, não o relatório inteiro) e use os dados para gerar as 3 Identidades:

- **Identidade do Consumidor.** perfil real baseado na pesquisa (demografia, comportamento, onde consome conteúdo, objeções típicas extraídas do Reclame Aqui, nível de consciência Schwartz)
- **Identidade do Produto.** diferencial vs concorrentes da tabela, posicionamento sugerido
- **Identidade do Comunicador.** tom de voz e estilo adequados ao público encontrado

Apresente para validação.

**Formato e Preço. SUGIRA com base na pesquisa:**
Use a sugestão de preço que saiu na pesquisa e explique o raciocínio apoiado nos concorrentes mapeados. Se o aluno discordar, argumente com os dados da pesquisa e ofereça alternativas em faixas diferentes, explicando o posicionamento de cada uma.

**Bloco 4/6. Decorados (Geração Automática):**

NÃO peça os decorados ao aluno. Gere automaticamente 50 Decorados com base no Quadro, na Furadeira, nas Identidades e nos dados de `pesquisa-mercado.md`.

Organize em 5 categorias: Financeiro, Tempo, Autoestima, Reputação, Crescimento (10 de cada).

Apresente a lista completa e pergunte se quer ajustar ou adicionar os seus próprios.

**Bloco 5/6. Urgências Ocultas (Geração Proativa):**

Pergunte ao aluno como prefere: geração automática (recomendado) ou dar exemplos para você expandir.

Estrutura oficial: 7 categorias com exatamente 10 itens cada (totalizando 70 itens). Não gere mais nem menos do que 10 em cada categoria.

1. DORES (o que incomoda): 10 problemas específicos que o produto resolve
2. DÚVIDAS (o que a pessoa pesquisa): 10 perguntas reais que o público faz
3. DESEJOS (o que ela quer alcançar): 10 estados desejados concretos
4. ASSUNTOS RELACIONADOS (porta de entrada): 10 temas adjacentes que interessam o público
5. URGÊNCIAS QUENTES (alta intenção): 10 itens diretamente ligados à compra
6. URGÊNCIAS FRIAS (atração): 10 itens de baixa intenção e alto volume
7. URGÊNCIAS INUSITADAS (ângulo diferente): 10 conexões inesperadas que chamam atenção

**Se geração automática:** Gere as 7 categorias completas (10 itens cada) com base em tudo que já coletou (Quadro, Identidades, dados de `pesquisa-mercado.md`). Apresente para validação e ajuste.

**Se dar exemplos:** Peça exemplos por categoria (UMA por vez) e expanda cada uma até completar 10 itens.

**Bloco 6/6. Argumentos Incontestáveis (Geração Automática):**

NÃO peça argumentos ao aluno. Gere automaticamente com base em tudo que já foi coletado: dados de `pesquisa-mercado.md`, Quadro, Furadeira e Identidades.

Os argumentos incontestáveis são evidências externas, lógicas ou estatísticas que tornam a promessa do produto difícil de contestar. Gere de 5 a 8 argumentos organizados em categorias:

- **Dados de mercado.** estatísticas, tamanho do mercado, crescimento do nicho (extraídos de `pesquisa-mercado.md`)
- **Evidências da lógica do método.** por que a sequência da Furadeira funciona (raciocínio causal, não promessa)
- **Referências do setor.** o que especialistas ou pesquisas reconhecidas dizem sobre o tema ou a transformação prometida
- **Dados de resultado.** se a pesquisa revelou resultados documentados de métodos similares no nicho, use-os

Apresente para validação e pergunte se o aluno quer adicionar dados próprios (número de alunos, faturamento gerado, resultados documentados). Se tiver, incorpore à lista existente.

### 3. Confirmação

Apresente resumo completo de tudo que foi definido/gerado e peça confirmação antes de salvar.

### 4. Salvar Perfil

Salve em `meus-produtos/{ativo}/perfil.md` com a estrutura:

```markdown
# Perfil do Negócio

## Quadro (Transformação Principal)
[Quadro escolhido]

## Furadeira (Método)
**Nome do Método:** [nome]
**Furadeira HTML:** meus-produtos/{ativo}/entregas/furadeira-visual.html
**Furadeira PNG:** meus-produtos/{ativo}/entregas/furadeira-visual.png (ou "não gerado" se falhou)
1. **[Macroetapa]**. [microetapas]
2. **[Macroetapa]**. [microetapas]
3. **[Macroetapa]**. [microetapas]

## Identidade do Produto
- **Nome:** [nome]
- **Formato:** [formato]
- **Preço:** [preço]
- **Diferencial:** [o que torna único]

## Identidade do Consumidor
- **Público-alvo:** [descrição]
- **Nicho:** [nicho]
- **Nível de consciência:** [classificação Schwartz]
- **Comportamento:** [onde consome, como compra]
- **Objeções típicas:** [objeções mapeadas]

## Identidade do Comunicador
- **Tom de voz:** [definido com base no público]
- **Posicionamento:** [definido]
- **Estilo:** [definido]

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

### 5. Próximo Passo

```
Perfil salvo em meus-produtos/{ativo}/perfil.md.

Próximo passo obrigatório: /produto-consumidor para detalhar a identidade do consumidor
e gerar o Painel de Entregas completo.
```
