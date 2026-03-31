---
name: workshop-marketing:paginas-low-ticket
description: Criar copies e páginas de vendas low ticket com as 4 categorias da metodologia D48 — Inadequação, Identificação com o Problema, Plug & Play e Promessa Boa Demais. Cada copy segue as 7 leis e termina com parágrafo técnico/racional.
---

# Páginas Low Ticket — 4 Copies D48

Gera as 4 copies de abertura para páginas de vendas low ticket. Cada copy é um estilo diferente de gancho — você escolhe qual usar ou testa as 4.

## Usage

```
/paginas-low-ticket
```

## Princípio Central

A melhor copy não parece copy. Parece alguém inteligente explicando algo que você nunca tinha entendido direito.

A copy nunca vende. Ela informa, avisa ou ensina. O produto não existe nos primeiros parágrafos — só existe o leitor e a realidade dele.

## As 7 Leis (aplicar em todas as copies)

1. **Ensinar em vez de prometer** — A copy entrega conhecimento real ali mesmo. A curiosidade vem de querer saber o resto, não de uma promessa vaga.
2. **Nomear cria realidade** — Sempre que possível, crie um nome próprio para o conceito, problema ou solução. Exemplos que funcionam: "Negociação Terapêutica", "Programação Emocional Repetitiva", "Peeling Estratificado Programado".
3. **O produto não aparece na copy** — Nenhuma copy fala "esse curso", "esse treinamento", "compre".
4. **Tom de escritor, não de vendedor** — Frases proibidas: "Isso vai transformar sua vida", "Descubra o método", "Não perca essa oportunidade".
5. **Especificidade mata generalização** — "Antes dos 7 anos" > "na infância". "15 mil pra 70 mil por projeto" > "multiplique seus ganhos".
6. **Informar, não vender** — As copies fazem uma de duas coisas: avisam ou ensinam. Nunca vendem.
7. **Crie um inimigo concreto** — Vendedora da loja, professor do YouTube, método antigo. A pessoa não precisa admitir que errou — só que foi mal orientada.

## Vícios Proibidos

- Travessão longo (—): NUNCA usar. Use vírgula, ponto, ou reformule a frase.
- Estrutura "Não é X. É Y.": NUNCA usar. É muleta de IA.
- Frases genéricas: "Transforme sua vida", "Descubra o segredo", "Método revolucionário".
- Mencionar o produto na copy.
- Emojis.

**Checklist obrigatório — revisar antes de entregar qualquer copy:**

Antes de entregar, revise e substitua:
- Travessão (—) → reescreva a frase sem ele
- Estrutura "Não é X. É Y." → desenvolva o argumento de outra forma
- Frases genéricas de vendedor → substitua por dado ou situação concreta
- Menção ao produto nos primeiros parágrafos → remova ou reescreva focando no leitor
- Emojis → remova sem substituição

- [ ] Nenhum travessão no texto
- [ ] Nenhuma estrutura "Não é X. É Y."
- [ ] Nenhuma frase genérica de vendedor

---

## O Que Fazer

### 1. Contexto

Leia `produtos/.ativo` e `produtos/{ativo}/perfil.md`. Se não existir, oriente a usar `/meu-produto` primeiro.
Leia também `produtos/{ativo}/idconsumidor.md` se existir.

### 1.5 — Framework de Decisão: Página vs. Quiz

Antes de iniciar a entrevista, analise os dados do perfil e do consumidor e aplique este framework. **Nunca pergunte de cara qual formato o aluno quer** — recomende com base nos critérios abaixo e explique o porquê.

| Critério | Aponta para QUIZ | Aponta para PÁGINA |
|---|---|---|
| Tipo de produto | Emocional / dor / identificação | Prático / ferramenta / direto ao ponto |
| Nível de consciência do lead | Não sabe que tem problema | Já sabe o que quer |
| Complexidade da decisão | Precisa diagnosticar / explicar | Decisão simples e direta |
| Faixa de preço | Até R$47 | Acima de R$97 |
| Tipo de público | Emocional | Analítico / pragmático |

**Regra:** 2 ou mais critérios para o mesmo lado — siga ele. **Desempate:** recomendar QUIZ (mais rápido de validar).

Apresente a recomendação assim:

```
Com base no seu produto e público, minha recomendação é:

→ [QUIZ ou PÁGINA DE VENDAS]

Por quê:
• [Critério 1]: [explicação com dado real do produto]
• [Critério 2]: [explicação com dado real do produto]
• [Critério 3]: [explicação com dado real do produto]

Você pode trocar depois se quiser testar o outro formato.

1. Concordo, seguir com [recomendação]
2. Prefiro o outro formato
```

**Se escolher QUIZ:** encaminhe para `/quiz` e encerre este comando.
**Se escolher PÁGINA:** continue para a Etapa 2 abaixo.

### 2. Entrevista (UMA pergunta por vez)

**Bloco 1/2 — Público:**
```
O público do produto é:

1. O profissional da área (ex: o terapeuta, o nutricionista, o designer)
2. O cliente final (ex: quem quer emagrecer, quem quer aprender inglês)

Digite o número:
```

```
--- Bloco 1/2 concluído ---
Público: [profissional / cliente final]
Próximo: Faixa de preço
---
```

**Bloco 2/2 — Faixa de Preço:**
```
Qual a faixa de preço do produto?

1. R$17 a R$47 (entrada ultra low ticket)
2. R$47 a R$97 (low ticket clássico)
3. R$97 a R$197 (low ticket premium)
4. R$197 a R$497 (mid ticket)

Digite o número:
```

```
--- Bloco 2/2 concluído ---
Público: [tipo]
Faixa de preço: R$[faixa]
Próximo: Geração das 4 copies
---
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Produto: [nome do produto ativo]
- Público: [profissional / cliente final]
- Faixa de preço: R$[faixa]
- Entregáveis: 4 copies completas (Inadequação, Identificação, Plug & Play, Promessa Boa Demais)

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração das 4 Copies

Gere as 4 copies em sequência. Cada copy deve:
- Aplicar as 7 leis sem exceção
- Evitar todos os vícios proibidos
- Terminar com parágrafo técnico/racional em itálico

Após gerar todas as 4, revise cada uma conferindo:
- O produto aparece nos primeiros parágrafos? Se sim, tire.
- Tem frase que um vendedor diria? Se sim, reescreva.
- Tem travessão longo (—)? Se sim, substitua.
- Tem estrutura "Não é X. É Y."? Se sim, reformule.
- A pessoa aprende algo lendo a copy? Se não, está prometendo em vez de ensinando.
- Criou um nome próprio para o conceito ou problema? Se não, considere criar.
- Os detalhes são específicos o suficiente?
- O tom soa como conversa ou como anúncio?

---

#### Copy 1 — Inadequação

**Engrenagem:** A pessoa descobre que está fazendo algo errado ou está desatualizada. Sente "será que estou ficando pra trás?" — urgência silenciosa impossível de ignorar.

**Estrutura obrigatória:**
1. Afirmação direta que coloca o leitor numa posição desconfortável (desatualizado, fazendo errado, ignorando algo que deveria saber)
2. Contextualização curta: o que mudou, por que o jeito antigo não funciona mais
3. Nome próprio para o problema ou solução
4. Parágrafo técnico/racional em itálico

**Variação poderosa — Inadequação com Alerta:** crie um inimigo concreto externo (vendedora, professor, método antigo). Use números específicos (7 itens, R$1.600). Escale de consequência financeira para emocional ou de segurança.

**Melhor para:** cursos, aulas, métodos, frameworks. Nichos com atualização constante. Versátil em preço (R$47 a R$500+).

**Exemplos de referência (NÃO copiar — só como parâmetro de estilo):**
- "Se você não faz Avaliação Neuropsicológica ou faz do mesmo jeito que se fazia em 2020, você está desatualizada."
- "Quando você for montar o enxoval do seu bebê, as vendedoras de loja vão te empurrar esses 7 itens..."
- "Aquele sérum anti-idade que você passa toda noite? Se você não preparou sua pele antes, ele não penetra quase nada."

---

#### Copy 2 — Identificação com o Problema

**Engrenagem:** A pessoa lê e pensa "isso sou eu." Você descreve a realidade dela com tanta precisão que ela sente que você está dentro da cabeça dela. Confiança instantânea.

**Estrutura obrigatória:**
1. Descrição vívida do problema com detalhes sensoriais e emocionais (4 a 6 parágrafos, sem pressa)
2. Amplificação: aprofunde na dor OU pinte o cenário ideal
3. Revele o "grande problema": por que o que a pessoa já tentou não funciona
4. Parágrafo técnico/racional em itálico

**Duas abordagens:**
- Identificação pela frustração: descreve a dor com detalhes, escala o sofrimento, mostra alguém conseguindo o que o leitor não consegue
- Identificação pelo desejo: faz uma pergunta que todo mundo do nicho já se fez, depois desenha o cenário ideal

**Melhor para:** métodos, cursos práticos, mentorias. Público que já tentou resolver sozinho e fracassou. Forte para low ticket puro (R$27 a R$197).

---

#### Copy 3 — Plug & Play

**Engrenagem:** A pessoa não precisa aprender nada, estudar nada, mudar nada. Só precisa pegar e usar. O valor está na praticidade imediata.

**Estrutura obrigatória:**
1. Headline curta que mostra o resultado prático
2. Um parágrafo que explica o que a pessoa recebe e como usa (sem jargão)
3. Parágrafo técnico/racional em itálico
4. CTA

A página inteira raramente passa de 3 a 4 scrolls no celular.

**Melhor para:** planilhas, templates, checklists, scripts prontos, kits, packs. Low ticket clássico (R$17 a R$97).

**Exemplos de referência (NÃO copiar):**
- "Tenha confiança para fazer qualquer contratação no seu casamento, com a certeza que ela cabe no seu bolso!"
- "3 produtos. Menos de R$120 os três. Você usa em casa, à noite, 2 vezes por semana."

---

#### Copy 4 — Promessa Boa Demais (Específica)

**Engrenagem:** A pessoa lê e pensa "não é possível, mas se for verdade..." O que segura ela é a combinação de resultado muito desejável com especificidade tão concreta que parece real demais pra ser marketing.

**Estrutura obrigatória:**
1. Resultado específico com números e situação concreta (antes e depois pessoal)
2. Frase que derruba uma objeção ou crença limitante
3. Convite a ver os detalhes, sem pressão ("vou detalhar o que aprendi", "nessa página eu mostro")
4. Parágrafo técnico/racional em itálico

**Tom:** de quem está abrindo o jogo, não de quem está vendendo. "Deixa eu te contar o que aconteceu comigo." Parece relato, não promessa.

**ATENÇÃO:** Essa categoria exige história verdadeira com números verificáveis. Sem história real, não use essa categoria — ela desaba.

**Melhor para:** aulas, workshops, mentorias com caso real por trás.

**Exemplos de referência (NÃO copiar):**
- "Como vender 10 franquias do seu negócio no primeiro ano."
- "Eu cobrava 15 mil por projeto de arquitetura, tinha dificuldade de vender e de entregar. Hoje eu cobro mais de 70 mil por projeto."
- "Eu gastava mais de R$500 por mês em clínica de estética. Era como alugar um resultado."

---

### 4. Matriz de Decisão (indicar qual copy usar)

Após gerar as 4, indique qual é mais indicada para o produto com base nesta lógica:

**O cliente precisa aprender ou precisa usar?**
- Aprender → Inadequação, Identificação ou Promessa Boa Demais
- Usar → Plug & Play

**O cliente já sabe que tem o problema?**
- Já sabe e já sofre → Identificação com o Problema
- Não sabe ou acha que está bem → Inadequação
- O expert tem história real com números → Promessa Boa Demais

**Nota sobre combinações:** as categorias podem se misturar. Uma página pode abrir com Inadequação e desenvolver com Identificação. Mas a abertura define a categoria principal — os primeiros 3 a 5 segundos de leitura são onde o gatilho é acionado.

### 5. Aprovação e Salvamento

Mostre as 4 copies na tela e pergunte:
```
As 4 copies estão prontas.

1. Aprovar e salvar todas
2. Quero ajustar alguma copy
3. Salvar só a copy [número]
```

Salvar em: `produtos/{ativo}/entregas/copy-pagina/copies-low-ticket-[produto].md`

Após salvar, pergunte:
```
Quer que eu gere a página HTML agora com a copy escolhida?

1. Sim, gerar a página HTML completa
2. Não, vou usar /pagina-de-vendas depois

Digite o número:
```

Se escolher **1**, continue:

```
Qual copy usar na página?

1. Inadequação
2. Identificação com o Problema
3. Plug & Play
4. Promessa Boa Demais

Digite o número:
```

```
Qual o preço do produto?
(ex: "R$37" ou "R$97 ou 12x R$9")
```

```
Link de checkout (Hotmart, Kiwify)?
(ex: "https://pay.hotmart.com/ABC123" ou "ainda não tenho")
```

```
Preferência de cor?

1. Azul (confiança, autoridade)
2. Verde (saúde, resultados)
3. Roxo (marketing, criatividade)
4. Vermelho (urgência, paixão)
5. Rosa (beleza, feminino)
6. Preto/Dourado (premium)
7. Deixa comigo (escolho a ideal para o nicho)

Digite o número:
```

**Confirmação antes de gerar HTML:**
```
Resumo do que vou criar:
- Tipo: Página de vendas low ticket
- Copy: [categoria escolhida]
- Produto: [nome do produto]
- Preço: [preço]
- Cor: [cor]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

---

### 6. Geração da Página HTML

#### Design Rules (aplicar obrigatoriamente)

Antes de gerar, leia `skills/paginas/SKILL.md` e `skills/paginas/references/cdn-design-resources.md`.

**Regras críticas:**
- **TODAS as fontes DEVEM ser sans-serif** — heading E body. Serifadas são PROIBIDAS (ver biblioteca aprovada em `skills/paginas/SKILL.md`)
- **Mínimo 4 tipos de fundo** diferentes entre seções (claro, escuro, imagem+overlay, gradiente)
- **Pelo menos 2 seções com imagem de fundo** (picsum.photos + overlay)
- **Grid 2 colunas** para entregáveis — NUNCA 3 colunas
- **Cards** com min-width 320px, padding 28px+, font-size 0.95rem+
- **Header com logotipo** obrigatório
- **Texto SEMPRE em pt-BR com acentos** corretos
- **NÃO parecer Lovable/v0** — sem cards brancos idênticos em fundo bege, sem gradiente roxo-azul genérico

**Mixagem de templates (OBRIGATÓRIO):**
Selecionar 2-3 templates de `skills/paginas/references/templates/` conforme o nicho e COMBINAR os melhores elementos de cada um. NUNCA usar um template sozinho. O catálogo completo com instruções de mixagem está em `skills/paginas/SKILL.md`.

**Estrutura obrigatória da página low ticket (aplicar em TODAS as versões de copy):**
1. Promessa (hero — copy da categoria escolhida + CTA)
2. Ferramenta dentro da entrega que resolve uma dor específica rápida
3. Depoimento
4. Entregáveis/método (grid 2 colunas)
5. Bônus
6. Oferta (Stack de Valor + Preço com ancoragem visual)
7. Garantia
8. Quem sou eu
9. FAQ (3-5 objeções comuns)
10. CTA final
11. Rodapé

Salvar em: `produtos/{ativo}/entregas/paginas/pagina-low-ticket-[produto].html`

Após salvar: "Pronto. Sua página foi salva em `produtos/{ativo}/entregas/paginas/pagina-low-ticket-[produto].html`. Abra no navegador para visualizar."

---

### 7. Próximo Passo

Sugerir: `/anuncio` para criar anúncios que levam tráfego para essa página.
