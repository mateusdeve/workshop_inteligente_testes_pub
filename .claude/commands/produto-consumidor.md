---
name: workshop-marketing:produto-consumidor
description: Criar identidade do consumidor (cliente ideal) usando as 3 Identidades da metodologia VTSD e gerar o Painel de Entregas HTML completo.
---

# Identidade do Consumidor. Cliente Ideal e Painel de Entregas

Cria o documento de **identidade do consumidor** (VTSD): perfil detalhado, objeções e comunicação. Ao final, gera o Painel de Entregas HTML com todos os dados do produto.

**REGRA — Paliativos:**
- **Definição:** paliativo é uma ferramenta, produto ou solução concorrente que existe no mercado e resolve o problema parcialmente, mas não entrega o resultado completo. Paliativo é o CONCORRENTE, não é "o que o público já tentou". Exemplos: Pinterest, perfis de Instagram do nicho, cursos genéricos, apps gratuitos, planilhas baixadas da internet.
- **Middle Ticket:** gerar paliativos a partir da pesquisa de mercado e dos concorrentes mapeados.
- **Low Ticket:** NÃO gerar paliativos. Produto de entrada não tem profundidade suficiente para mapear paliativos.

Para verificar o tipo do produto, leia `meus-produtos/{ativo}/tipo.md`.

## Usage

```
/produto-consumidor
```

## Princípios de Comportamento

### Postura: Consultor que gera, não formulário que pergunta

Você já tem o `perfil.md` e `pesquisa-mercado.md` com todos os dados necessários. Use TUDO isso para gerar a persona proativamente.

- **Pergunte o mínimo:** só dados que apenas o aluno sabe (gênero, idade, profissão)
- **Gere e sugira o resto:** objeções, canais, tom de voz, frases (paliativos apenas se Middle Ticket)
- **Apresente para validação:** o aluno aprova, ajusta ou complementa
- **"Não sei" = você sugere:** use dados do perfil e pesquisa de mercado para propor a resposta

### Pesquisa de mercado já feita

Leia `meus-produtos/{ativo}/pesquisa-mercado.md` para usar os dados já coletados. **Não faça nova pesquisa.**

## O Que Fazer

### 1. Contexto

Leia `meus-produtos/.ativo` para obter o produto ativo. Leia `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/pesquisa-mercado.md`. Se o `perfil.md` não existir, oriente a usar `/produto-concepcao` primeiro.

Verifique se as Urgências Ocultas já estão completas no perfil. Se estiverem com stubs ("a completar"), gere as Urgências Ocultas completas e atualize o `perfil.md` antes de continuar.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3. Dados Demográficos:**

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
--- Bloco 1/3 concluído ---
Perfil: [gênero], [idade], [profissão], [renda]
Próximo: Comportamento
---
```

**Bloco 2/3. Comportamento (Geração Proativa):**

Com base nos dados demográficos + Urgências Ocultas + Identidade do Consumidor do perfil + `pesquisa-mercado.md`, GERE automaticamente:

- **Paliativos** *(somente Middle Ticket)* — ferramentas, produtos e soluções concorrentes que existem no mercado e resolvem o problema parcialmente, sem entregar o resultado completo. Não é "o que o público já tentou e falhou". São os concorrentes diretos e indiretos: Pinterest, perfis de Instagram do nicho, cursos genéricos, apps, planilhas, templates gratuitos, etc. (baseado na pesquisa de mercado e nos concorrentes mapeados)
- **Sonho** — a frase que ela diria para uma amiga se alcançasse o resultado (baseado nos desejos)
- **Canais** — onde essa pessoa busca informação (baseado no perfil demográfico e no nicho)

Apresente tudo gerado de uma vez para o aluno validar e ajustar. Não peça item por item.

Mostre progresso ao concluir.

**Bloco 3/3. Objeções (Framework dos 7 Argumentos):**

GERE automaticamente as **5 principais objeções** que um potencial comprador pode ter, com base no perfil do consumidor, preço, nicho, Quadro do produto e dados de `pesquisa-mercado.md` (especialmente Reclame Aqui). NÃO liste opções para o aluno escolher.

Para CADA uma das 5 objeções, gere **7 formas diferentes de quebra**, cada uma com **2 parágrafos**, seguindo estes tipos de argumento (nesta ordem fixa):

1. **Argumento Incontestável** — dado concreto, estatística ou fato irrefutável com fonte.
2. **Argumento Lógico (causa e efeito)** — raciocínio frio com números e relação de causa-consequência.
3. **Argumento por Analogia** — comparação visual e acessível. **Nunca cite celebridades**, use situações reais e alcançáveis que o público viva no dia a dia.
4. **Argumento por Exemplificação** — caso real com nome fictício, situação inicial, decisão tomada e resultado concreto (storytelling curto).
5. **Argumento de Valor (custo vs. benefício)** — comparação do investimento com o retorno tangível e intangível.
6. **Argumento de Consequência (de agir ou não agir)** — o que acontece se a pessoa decidir agora versus adiar.
7. **Argumento de Contradição (refutação de incoerências)** — aponta onde a objeção contradiz outras escolhas ou prioridades da própria pessoa.

Cada parágrafo deve ter sofisticação de advogado construindo raciocínio lógico, combinada com técnica de comunicação persuasiva. Use analogias visuais, números, retórica forte e provocações que desarmem sem gerar resistência. O produto e o Quadro do perfil orientam o conteúdo.

Aplicar Light Copy: sem travessão, sem ponto de exclamação, sem pergunta retórica abrindo parágrafo, afirmações diretas.

Apresente as 5 objeções com as 7 quebras cada para validação. O aluno aprova, ajusta, adiciona ou remove.

**Confirmação antes de gerar:**
```
Resumo da identidade do consumidor:
- Perfil: [gênero], [idade], [profissão]
- Renda: [renda]
- Paliativos: [ferramentas e soluções concorrentes do mercado que resolvem o problema parcialmente — incluir apenas se Middle Ticket]
- Sonho: [resultado mágico]
- Canais: [onde busca info]
- Objeções: [principais objeções]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Gerar Documento

Salve em `meus-produtos/{ativo}/idconsumidor.md`:

```markdown
# Identidade do Consumidor: [Nome Fictício]

## Para Quem É
[Frase de posicionamento clara, 1-2 linhas]
"Este produto é para [perfil específico], que [problema/situação atual], e quer [transformação desejada]."

Não é para: [exclusões que ajudam a posicionar — quem NÃO é o público]

## Identidade do Consumidor
- **Idade:** / **Gênero:** / **Profissão:**
- **Renda:** / **Estado civil:** / **Localização:**
- **Nível de consciência:** [inconsciente → totalmente consciente]
- **Onde busca informação:** [canais]

## Paliativos (somente Middle Ticket — ferramentas e soluções concorrentes do mercado que resolvem o problema parcialmente)
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

### 4. Gerar Painel de Entregas HTML

Após salvar o `idconsumidor.md`, gere automaticamente o Painel de Entregas em `meus-produtos/{ativo}/painel-entregas.html`.

**IMPORTANTE:** NÃO leia `design-system-components.md` nem `design-referencia-vtsd.md` para gerar este arquivo. O painel de entregas é isento do Checklist 2 do `CLAUDE.md`. Siga rigorosamente a especificação de design abaixo.

---

**Especificação de Design do Painel de Entregas**

**Título da página:** sempre "Painel de Entregas" (tag `<title>` e cabeçalho da sidebar). Nunca o nome do produto.

**Fonte:** `Inter` apenas (Google Fonts, pesos 400, 500, 600, 700, 800). Nenhuma fonte serif.

**Proibido:** emojis em qualquer lugar do HTML (nav, títulos, ícones, listas). Use apenas texto ou símbolos tipográficos simples (`›`, `•`, `▾`) quando necessário.

**Tokens CSS obrigatórios:**
```css
:root {
  --sidebar-bg: #ffffff;
  --sidebar-border: #e5e7eb;
  --main-bg: #f8f9fb;
  --surface: #ffffff;
  --primary: #22c55e;
  --primary-dark: #16a34a;
  --primary-light: #dcfce7;
  --highlight-bg: #f0fdf4;
  --highlight-border: #bbf7d0;
  --text-1: #111827;
  --text-2: #374151;
  --text-3: #6b7280;
  --border: #e5e7eb;
  --border-2: #f3f4f6;
  /* badges */
  --badge-green-bg: #dcfce7;
  --badge-green-text: #16a34a;
  --badge-blue-bg: #dbeafe;
  --badge-blue-text: #1d4ed8;
  --badge-indigo-bg: #e0e7ff;
  --badge-indigo-text: #4338ca;
  --badge-purple-bg: #ede9fe;
  --badge-purple-text: #7c3aed;
  --badge-violet-bg: #f3e8ff;
  --badge-violet-text: #9333ea;
  --badge-pink-bg: #fce7f3;
  --badge-pink-text: #db2777;
  --badge-orange-bg: #fef3c7;
  --badge-orange-text: #d97706;
  --badge-dark-bg: #1f2937;
  --badge-dark-text: #ffffff;
  --badge-neutral-bg: #f3f4f6;
  --badge-neutral-text: #374151;
  --sidebar-w: 220px;
  --r: 10px;
  --r2: 8px;
  --sh1: 0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04);
  --sh2: 0 4px 16px rgba(0,0,0,.08), 0 1px 4px rgba(0,0,0,.04);
}
```

---

**Estrutura da página:**

1. **Sidebar fixa** à esquerda: `width: var(--sidebar-w)`, `background: var(--sidebar-bg)`, `border-right: 1px solid var(--sidebar-border)`, `position: fixed`, `top: 0`, `left: 0`, `height: 100vh`, `overflow-y: auto`, `padding: 24px 0`.

   - Cabeçalho da sidebar: "Painel de Entregas" em `--text-1`, font-size 14px, font-weight 700, padding 0 20px. Nome do produto logo abaixo em `--text-3`, font-size 11px, line-height 1.4, padding 0 20px, margin-bottom 24px.
   - Rótulos de grupo (PRODUTO, IDENTIDADES, PESQUISA): font-size 10px, font-weight 700, color `--text-3`, uppercase, letter-spacing 1px, padding 0 20px, margin: 16px 0 4px.
   - Itens de nav: display block, padding 7px 20px, font-size 13px, color `--text-2`, text-decoration none, border-left 3px solid transparent. Sem fundo, sem ícones, sem emojis.
   - Item ativo: color `--primary-dark`, font-weight 600, border-left `3px solid var(--primary)`. Sem fundo colorido — apenas a borda e o texto mudam.
   - Botão "Exportar PDF": posição fixed, bottom 20px, left 0, width `var(--sidebar-w)`, padding 0 20px. O botão em si ocupa 100% da largura interna, fundo `--primary`, cor branco, border-radius `--r2`, padding 10px 0, font-size 13px, weight 600, text-align center, cursor pointer. Hover: fundo `--primary-dark`.

2. **Main content**: `margin-left: var(--sidebar-w)`, `background: var(--main-bg)`, `min-height: 100vh`, `padding: 32px 40px`.

3. **Breadcrumb** no topo do conteúdo: texto `Painel de Entregas › {nome da seção}`, color `--text-3`, font-size 13px, margin-bottom 8px.

4. **Cabeçalho da seção**: título em font-size 26px, font-weight 700, color `--text-1`, margin-bottom 4px. Subtítulo descritivo em `--text-3`, font-size 13px, margin-bottom 24px.

5. **Painéis** (`display: none` por padrão; quando ativo: `display: block` + animação `fadeIn 0.2s ease`).

---

**Componentes obrigatórios:**

**Card padrão**: fundo `--surface`, borda `1px solid var(--border)`, border-radius `--r`, padding 24px, sombra `--sh1`. Label interna em font-size 11px, font-weight 700, color `--text-3`, uppercase, letter-spacing 0.8px, margin-bottom 8px. Valor/texto principal em font-size 15px, font-weight 600, color `--text-1`. Subtexto descritivo em font-size 13px, color `--text-3`, margin-top 4px.

**Card destaque verde** (usado para Quadro): fundo `--highlight-bg`, borda `1px solid var(--highlight-border)`, border-radius `--r`, padding 20px 24px. Label interna em font-size 11px, font-weight 700, color `--primary`, uppercase, letter-spacing 0.8px, margin-bottom 8px. Texto principal em font-size 18px, font-weight 700, color `--primary-dark`, line-height 1.4.

**Card de conteúdo informativo**: mesmo estilo do card padrão. Hover: sombra `--sh2`, transição 0.2s. Usado para "Como usar o Quadro", "Regra do Quadro", "Nicho", "Diferencial", etc.

**Card de status do produto** (Visão Geral, seção inferior): card padrão full-width. Contém linha com dot verde (círculo 8px, fundo `--primary`, inline-block, margin-right 6px), texto "Produto ativo" em `--text-2` font-weight 600, seguido de separadores `·` e metadados em `--text-3`, e badges coloridas ao final.

**Step timeline** (Furadeira — Trilha do Método): lista vertical dentro de um card padrão. Cada step tem:
- Círculo numerado: `width: 32px; height: 32px; border-radius: 50%; background: var(--primary); color: #fff; font-size: 14px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0`.
- Linha conectora vertical entre os círculos: `border-left: 2px solid var(--primary-light)` alinhada ao centro do círculo, `margin-left: 15px`, exceto no último step.
- Conteúdo do step: título em font-size 15px, font-weight 600, color `--text-1`. Descrição em font-size 13px, color `--text-3`, line-height 1.6, margin-top 4px.
- Espaçamento entre steps: padding-bottom 20px (exceto o último).

**Accordion**: fundo `--surface`, borda `1px solid var(--border)`, border-radius `--r`, margin-bottom 8px, sombra `--sh1`. Header: `display: flex; align-items: center; gap: 12px; padding: 14px 20px; cursor: pointer`. Contém badge colorida à esquerda, depois texto descritivo em font-size 14px, color `--text-1`, font-weight 500, e ícone `▾` em `--text-3` à direita (margin-left auto, rotaciona 180° quando aberto via transition 0.2s). Corpo animado: `max-height` de 0 para 3000px via `cubic-bezier(.4,0,.2,1) 0.3s`, `overflow: hidden`. Items dentro do corpo em lista simples, font-size 13px, color `--text-2`, line-height 1.7, padding 0 20px 16px, com marcador `•` verde antes de cada item.

**Badges/pills**: `border-radius: 9999px`, font-size 11px, font-weight 700, padding `3px 10px`, white-space nowrap. Variantes por cor:
- `.badge-green`: bg `--badge-green-bg`, color `--badge-green-text`
- `.badge-blue`: bg `--badge-blue-bg`, color `--badge-blue-text`
- `.badge-indigo`: bg `--badge-indigo-bg`, color `--badge-indigo-text`
- `.badge-purple`: bg `--badge-purple-bg`, color `--badge-purple-text`
- `.badge-violet`: bg `--badge-violet-bg`, color `--badge-violet-text`
- `.badge-pink`: bg `--badge-pink-bg`, color `--badge-pink-text`
- `.badge-orange`: bg `--badge-orange-bg`, color `--badge-orange-text`
- `.badge-dark`: bg `--badge-dark-bg`, color `--badge-dark-text`
- `.badge-neutral`: bg `--badge-neutral-bg`, color `--badge-neutral-text`

**Botão primário inline** (dentro de seções, ex: "Ver Trilha Visual Completa"): fundo `--primary`, cor branco, border-radius `--r2`, padding `9px 20px`, font-size 13px, weight 600, display inline-flex, align-items center, gap 6px. Hover: fundo `--primary-dark`. Seta `→` como texto simples após o label.

**Grid 3 colunas** (stat cards da Visão Geral): `display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px`. Em mobile (< 768px): 1 coluna.

**Grid 2 colunas** (cards informativos lado a lado): `display: grid; grid-template-columns: 1fr 1fr; gap: 16px`. Em mobile: 1 coluna.

**Tabela de concorrentes** (Pesquisa de Mercado): `width: 100%; border-collapse: collapse`. Sem zebra-stripe. Cada linha `<tr>` tem `border-bottom: 1px solid var(--border-2)`. Header `<th>`: font-size 11px, uppercase, letter-spacing 1px, color `--text-3`, weight 700, padding 10px 12px, text-align left. Células `<td>`: font-size 13px, color `--text-2`, padding 10px 12px.

**Divider**: `height: 1px; background: var(--border); margin: 24px 0`.

**Responsivo:** abaixo de 768px, sidebar fica `display: none`. Aparece barra de tabs horizontais no topo (sticky, `top: 0`), fundo `--surface`, borda inferior `1px solid var(--border)`, overflow-x auto, sem emojis. Tabs têm padding `10px 16px`, font-size 13px, color `--text-3`. Tab ativa: color `--primary-dark`, font-weight 600, border-bottom `2px solid var(--primary)`.

**JavaScript:** função `showPanel(id)` que esconde todos os painéis (`display: none`) e exibe o alvo (`display: block`). Sincroniza classe `.active` nos itens de nav da sidebar e da barra mobile. Ao carregar, exibe o painel `visao-geral` por padrão.

---

**Seções do painel, navegação e layout interno de cada seção:**

Grupo **PRODUTO** na sidebar:

- **Visão Geral** — subtítulo: "Resumo do produto e informações principais."
  1. Grid 3 colunas: card "NOME DO PRODUTO" (nome em bold + subtítulo descritivo), card "TIPO" (Low/Middle Ticket + descrição do formato), card "PREÇO" (valor em font-size 24px font-weight 700 color `--primary` + posicionamento estratégico em gray).
  2. Card destaque verde full-width: label "QUADRO — TRANSFORMAÇÃO PRINCIPAL", texto do Quadro em bold verde.
  3. Grid 2 colunas: card "NICHO" e card "DIFERENCIAL".
  4. Card full-width "STATUS DO PRODUTO": dot verde + "Produto ativo" + `·` + tipo + `·` + preço + `·` + badges de completude (`.badge-green` para cada seção preenchida: "Perfil completo", "Identidade do consumidor", "Urgências ocultas").

- **Quadro** — subtítulo: "A transformação principal que o produto entrega ao cliente."
  1. Card destaque verde: label "QUADRO APROVADO", texto do Quadro.
  2. Grid 2 colunas: card "COMO USAR O QUADRO" (explicação de onde o Quadro aparece: headline, emails, anúncios, primeiro slide de carrossel) e card "REGRA DO QUADRO" (teste: "a pessoa pode dizer que isso aconteceu na vida dela?").

- **Furadeira** — subtítulo: "O método estruturado que torna visível a eficiência do produto."
  1. Card padrão: label "NOME DO MÉTODO", nome do método em bold.
  2. Card padrão: label "TRILHA DO MÉTODO", seguido de step timeline numerado com todas as macroetapas (número, nome, descrição das microetapas). Abaixo do último step, botão primário "Ver Trilha Visual Completa →" linkando para `entregas/furadeira-visual.html` (se existir) ou `#`.

  **ATENÇÃO — caminho do link obrigatório:** o painel fica em `meus-produtos/{ativo}/painel-entregas.html` e a furadeira em `meus-produtos/{ativo}/entregas/furadeira-visual.html`. O caminho relativo correto é sempre `entregas/furadeira-visual.html`. Nunca usar apenas `furadeira-visual.html` (caminho errado que quebra o link).

- **Decorados** — subtítulo: "50 benefícios derivados do Quadro. Use para bullets de página, scripts de venda e conteúdo."
  5 accordions, header = badge + "10 benefícios". Badge por categoria:
  - Financeiro: `.badge-green`
  - Tempo: `.badge-blue`
  - Autoestima: `.badge-purple`
  - Reputação: `.badge-orange`
  - Crescimento: `.badge-dark`

- **Urgências Ocultas** — subtítulo: "70 itens em 7 categorias. Use para temas de anúncio, bullets de página, ganchos de conteúdo e linhas de email."
  7 accordions, header = badge + descrição + `·` + "10 itens". Badge e descrição por categoria:
  - Dores: `.badge-pink` / "O que incomoda"
  - Dúvidas: `.badge-indigo` / "O que pergunta"
  - Desejos: `.badge-violet` / "O que sonha"
  - Assuntos Relacionados: `.badge-green` / "Porta de entrada"
  - Urgências Quentes: `.badge-orange` / "Alta intenção"
  - Urgências Frias: `.badge-neutral` / "Alto volume"
  - Urgências Inusitadas: `.badge-purple` / "Ângulos inesperados"

Grupo **IDENTIDADES** na sidebar:

- **Identidade do Produto** — subtítulo: "Como o produto se posiciona e se diferencia no mercado."
  Layout obrigatório:
  1. Grid 2 colunas: card "DIFERENCIAL PRINCIPAL" + card "FORMATO" (descrição de módulos, planilhas, comunidade, bônus e acessos incluídos).
  2. Card full-width "ARGUMENTOS INCONTESTÁVEIS": lista `.bullet-list` com 4-6 argumentos, cada um com dado concreto + fonte entre parênteses.
  3. Card full-width "OBJEÇÕES PRINCIPAIS E COMO QUEBRAR" (Framework dos 7 Argumentos): 5 accordions, um por objeção. Header do accordion = badge `.badge-pink` com numeração ("Objeção 1", "Objeção 2", "Objeção 3", "Objeção 4", "Objeção 5") + texto da objeção em font-size 14px, font-weight 500, `--text-1`, seguido do ícone `▾` à direita. Corpo do accordion contém os 7 sub-blocos de argumento, na ordem fixa abaixo. Cada sub-bloco tem: título em font-size 13px, font-weight 700, `--text-1`, uppercase, letter-spacing 0.5px, margin-bottom 6px; 2 parágrafos em font-size 13px, color `--text-2`, line-height 1.7, margin-bottom 8px entre parágrafos; margin-bottom 18px entre sub-blocos; divider `1px solid var(--border-2)` separando os sub-blocos. Sub-blocos na ordem: "1. ARGUMENTO INCONTESTÁVEL", "2. ARGUMENTO LÓGICO (CAUSA E EFEITO)", "3. ARGUMENTO POR ANALOGIA", "4. ARGUMENTO POR EXEMPLIFICAÇÃO", "5. ARGUMENTO DE VALOR (CUSTO VS. BENEFÍCIO)", "6. ARGUMENTO DE CONSEQUÊNCIA (AGIR VS. ADIAR)", "7. ARGUMENTO DE CONTRADIÇÃO". Conteúdo textual vem da seção "Objeções de Compra" do `idconsumidor.md`. Nunca citar celebridades nas analogias, usar situações reais e alcançáveis.
  Nota: o campo "Preço" fica somente na Visão Geral. Não repetir aqui.

- **Identidade do Consumidor** — subtítulo: "Perfil detalhado do cliente ideal."
  Layout obrigatório:
  1. Card destaque verde full-width "PARA QUEM É": frase de posicionamento em 1-2 linhas descrevendo o perfil + situação atual + transformação desejada. Font-size 15px, font-weight 500, color `--primary-dark`.
  2. Grid 2 colunas: card "PERFIL DEMOGRÁFICO" (gênero, idade, profissão, renda, localização, nível de consciência — cada campo em linha separada com `<strong>` no label) + card "COMPORTAMENTO E CANAIS" (onde busca informação, conteúdo que consome, como compra, sonho em frase direta — mesmo formato `<strong>` + valor).
  3. Card full-width "PALIATIVOS" (somente Middle Ticket): lista `.bullet-list` com cada ferramenta ou solução concorrente do mercado + seta `→` + o que ela oferece e por que não entrega o resultado completo. Omitir inteiramente se Low Ticket.
  4. Card full-width "BALDES DE PARA QUEM É": 2-5 accordions (conforme os dados), badge `.badge-neutral` no header com nome do perfil. Cada accordion lista 5 afirmações diretas em linguagem de copy e tráfego pago, com marcador `•` verde.

- **Identidade do Comunicador** — subtítulo: "Tom, posicionamento e linguagem do criador."
  Layout obrigatório:
  1. Grid 3 colunas: card "COMUNICADOR" (nome em bold + especialidade como subtexto) + card "VALORES" (pills `.badge-green` com os valores escolhidos) + card "MANTRAS E JARGÕES" (frases próprias do comunicador em texto simples, cada uma em linha separada; "nenhum ainda" se vazio).
  2. Grid 2 colunas: card "FORMATOS QUE COMBINAM" (pills `.badge-indigo` com os formatos preferidos) + card "ESTILO VISUAL RECOMENDADO" (pills `.badge-neutral` com os elementos visuais recomendados).
  3. Card full-width "REFERÊNCIAS DE COMUNICAÇÃO": grid interno 3 colunas com os nomes de referência, cada um em div com fundo `--main-bg`, border-radius `--r2`, padding 12px. Cada div tem: nome em bold + `--text-1`, e breve descrição de por que essa referência em `--text-2` font-size 13px line-height 1.6.
  4. Grid 2 colunas: card "TOM DE VOZ" (parágrafo descritivo, 3-5 linhas, lendo de `perfil.md` campo Tom de voz e Tonalidade emocional predominante) + card "POSICIONAMENTO" (parágrafo descritivo, 3-5 linhas, lendo de `perfil.md` campo Posicionamento pessoal).
  5. Grid 2 colunas: card "PALAVRAS QUE CONECTAM" (pills `.badge-green` em flex-wrap, gap 6px, 8-12 palavras — vem do campo "Vocabulário base" e "Palavras que conectam" do `idconsumidor.md`) + card "PALAVRAS QUE AFASTAM" (pills `.badge-pink` em flex-wrap, gap 6px, 6-10 palavras — vem do campo "Palavras que afastam" do `idconsumidor.md`).

  **Fonte dos dados:** todos os campos desta seção vêm de `meus-produtos/{ativo}/perfil.md` (seção "Identidade do Comunicador") e de `meus-produtos/{ativo}/idconsumidor.md` (seção "Como se Comunicar"). Nunca omitir os campos de nome, valores, mantras, formatos e referências por estarem "fora da spec mínima".

Grupo **PESQUISA** na sidebar:

- **Pesquisa de Mercado** — subtítulo: "Dashboard de inteligência de mercado. Use para argumentos, copy e posicionamento."

  Esta seção é um **dashboard de relatório de mercado** no padrão de BI profissional, com gráficos SVG, donut charts, line charts, circular progress e KPIs com indicadores de tendência. Usa visualizações CSS/SVG puras (zero bibliotecas externas) para dar peso e credibilidade à entrega, transformando o relatório em um deliverable premium.

  **Bloco 1 — KPIs com tendência (grid 4 colunas):**
  Quatro cards de KPI, cada um com:
  - Label uppercase em `--text-3`, font-size 11px, letter-spacing 0.8px
  - Valor principal em font-size 28px, font-weight 800, `--text-1`
  - Linha de tendência: ícone de seta (▲ verde para positivo, ▼ vermelho para negativo, ● neutro em `--text-3`) + variação percentual em font-size 12px, font-weight 600 + label de comparação em `--text-3`
  - **Sparkline SVG** inline na base do card (altura 36px, largura 100%): mini área chart com fill gradient em `--primary` 20% de opacidade, stroke em `--primary` 1.5px

  Os 4 KPIs padrão (ajustar aos dados reais da pesquisa):
  1. Tamanho do Mercado (ex: R$2,1 bi) + trend vs ano anterior
  2. Crescimento Anual (ex: 18%) + trend pp (pontos percentuais)
  3. Concorrentes Mapeados (ex: 47) + total do nicho
  4. Ticket Médio do Nicho (ex: R$347) + posição percentil

  **Bloco 2 — Crescimento do mercado (grid 2 colunas):**

  - **Esquerda — Area chart SVG (Crescimento 5 anos):**
    Card com label "CRESCIMENTO DO MERCADO (5 ANOS)", subtítulo com fonte (ex: "ABFin, IBGE"). SVG viewBox 400x160:
    - Path curvo (cubic bezier) conectando os 5 pontos (2020-2024), stroke `--primary` 2px
    - Path de fill com gradient linear de `--primary` 30% (topo) para `--primary` 0% (base)
    - Eixo X com os anos em font-size 11px `--text-3`
    - Eixo Y com 3-4 gridlines horizontais `--border-2` 1px
    - Valores nos pontos em badges pequenos `.badge-green`
    - Destacar o último ponto com círculo maior preenchido em `--primary`

  - **Direita — Donut chart SVG (Distribuição Reclame Aqui):**
    Card com label "RECLAMAÇÕES POR CATEGORIA". SVG circular 200x200:
    - Círculo base `--border-2` 14px stroke
    - Segmentos coloridos via `stroke-dasharray` rotacionados: `--primary` (maior categoria), `--badge-orange-text` (segunda), `--badge-pink-text` (terceira), `--text-3` (outras)
    - Número grande no centro do donut: total de reclamações ou percentual dominante (ex: "62%" + label "genéricas" abaixo em `--text-3`)
    - Legenda à direita do SVG: linha por categoria com dot colorido 10px + label + percentual em bold

  **Bloco 3 — Oportunidades Identificadas (card full-width):**
  Label "OPORTUNIDADES IDENTIFICADAS" em verde uppercase. Lista numerada (não bullets) com 5-8 oportunidades. Cada item tem:
  - Círculo numerado 28px em `--primary-light` com número em `--primary-dark` font-weight 700
  - Texto da oportunidade em font-size 14px, `--text-2`, line-height 1.6
  - Separador `1px solid var(--border-2)` entre itens
  Dados da "Síntese Estratégica > Oportunidades de posicionamento" do `pesquisa-mercado.md`.

  **Bloco 4 — Mapa de Preços + Top Concorrentes (grid 2 colunas):**

  - **Esquerda — Bar chart vertical SVG (Preço médio por formato):**
    Card com label "PREÇO MÉDIO POR FORMATO". SVG viewBox 400x240:
    - 5 barras verticais (Ebook, Mini-curso, Curso, Mentoria, HT 1:1), fill `--primary`, border-radius 4px no topo
    - Valores acima de cada barra em font-size 11px, `--text-2`, font-weight 600
    - Labels de formato abaixo em font-size 11px, `--text-3`, truncadas se longas
    - Barra correspondente ao formato do produto atual em destaque: stroke `--primary-dark` 2px + badge "SEU PRODUTO" em `.badge-green` acima

  - **Direita — Top 5 Concorrentes:**
    Card com label "TOP 5 CONCORRENTES". Lista com 5 itens, cada um em uma linha:
    - Avatar circular 36px com inicial do nome em fundo colorido rotativo (verde, azul, roxo, laranja, cinza)
    - Nome em font-size 14px, font-weight 600, `--text-1`
    - Formato em font-size 12px, `--text-3`
    - Badge de preço alinhada à direita com cor por faixa
    - Links inline abaixo do nome: "Página de Vendas" e "Instagram" como `<a>` com font-size 11px, cor `--primary`, icon "↗" antes do texto, gap 8px entre os dois links
    - Divider `1px solid var(--border-2)` entre linhas

    **REGRA OBRIGATÓRIA DE LINKS (proibido violar):**
    - O `href` de "Página" e "Instagram" deve ser **a URL exata coletada em `pesquisa-mercado.md`** (campos "Link" e "Instagram" da tabela de concorrentes). Nada de inventar domínio, nada de adivinhar handle.
    - **Proibido usar busca no Google ou YouTube como fallback.** `https://www.google.com/search?q=...` é tratamento de dado faltante, não link real, e o aluno não consegue distinguir.
    - Se a pesquisa não tiver a URL real do concorrente (campo vazio, "link indisponível", concorrente fictício ou não encontrado): **omitir o link inteiro** (não renderizar o `<a>`). Mostrar apenas o nome.
    - Se um dos dois links existe e o outro não: renderizar só o que tem.
    - Antes de salvar o painel: validar cada `href` da seção. Se algum apontar para `google.com/search`, `youtube.com/results?search_query`, `bing.com/search` ou qualquer URL de busca, **substituir por omissão** (remover o `<a>`).

  **Bloco 5 — Cuidados e Reclame Aqui Detalhado (grid 2 colunas):**
  - Card "CUIDADOS E RISCOS": lista com marcador `•` laranja, itens de `pesquisa-mercado.md` seção Alertas e Riscos.
  - Card "PADRÕES DE RECLAMAÇÃO": cada padrão em uma linha com barra horizontal CSS mostrando o percentual proporcional, valor numérico à direita. Mesmo componente `complaint-row` da spec atual, porém com hover state mostrando exemplo de reclamação em tooltip.

  **Bloco 6 — Tabela Completa de Concorrentes (card full-width):**
  Label "ANÁLISE COMPLETA DE CONCORRENTES". Tabela com colunas: Nome, Promessa Principal, Formato, Preço (badge colorida por faixa: verde até R$97, azul R$98-R$497, roxo R$498-R$1.997, escuro acima de R$1.998), Diferencial Aparente, Links (dois ícones/links inline: "↗ Página" abrindo a página de vendas do concorrente e "↗ Instagram" abrindo o perfil do Instagram, ambos como `<a target="_blank">` com font-size 11px, cor `--primary`), Posição no Mercado (mini bar de 4 dots preenchidos conforme força competitiva 1-4). Até 10 linhas visíveis, resto em "Ver todos ▾".

  **A mesma REGRA OBRIGATÓRIA DE LINKS do Bloco 4 vale aqui na tabela.** Resumo: usar somente URL real coletada em `pesquisa-mercado.md`. Proibido `google.com/search`, `youtube.com/results?search_query` e similares como fallback. Sem URL real, omitir o `<a>` e renderizar a célula vazia (ou um traço discreto). Validar antes de salvar.

  **Bloco 7 — Ângulos Virais e Ganchos (card full-width, grid 2 colunas interno):**
  - Esquerdo "TERMOS EM ALTA": heatmap de pills `.badge-green` com tamanhos variados por intensidade (termos mais quentes em font-size 13px, termos secundários em font-size 11px). Layout flex-wrap, gap 8px.
  - Direito "PADRÕES DE ANÚNCIO QUE PERFORMAM": lista com marcador `•` azul, cada padrão numerado.

  **Bloco 8 — Top 10 Vídeos do YouTube do Nicho (card full-width):**

  Dados vêm da seção "9. YouTube. Top 10 Vídeos do Nicho" do `pesquisa-mercado.md`.

  Label "TOP 10 VÍDEOS DO YOUTUBE DO NICHO" uppercase em `--text-1`, weight 700, letter-spacing 0.8px. Subtítulo abaixo em `--text-3`, font-size 13px: "Referência de thumb, copy e comentários vivos do nicho."

  **Tabela visual de 10 linhas**, cada linha com 5 colunas e divider `1px solid var(--border-2)` entre linhas. Hover da linha: fundo `--main-bg`, transition 0.15s.

  - **Coluna 1 — Ranking (width 40px):** círculo 28px border-radius 50%, fundo `--primary-light`, número em `--primary-dark` font-size 12px font-weight 700, centralizado. Valores `#1` a `#10`.
  - **Coluna 2 — Thumb placeholder (width 96px):** div 80x45 (proporção 16:9), border-radius 4px, fundo `--text-3`, margin-right 12px. Sem texto interno, apenas bloco de cor.
  - **Coluna 3 — Título e canal (flex: 1):** título em font-size 13px, weight 600, `--text-1`, display -webkit-box com `-webkit-line-clamp: 2`, line-height 1.4. Canal abaixo em font-size 11px, `--text-3`, margin-top 2px.
  - **Coluna 4 — Views (width 100px, text-align right):** badge `.badge-green` com o valor em formato compacto (ex: "4,2M views", "870K views").
  - **Coluna 5 — Link (width 32px, text-align right):** ícone `↗` como `<a target="_blank" rel="noopener">`, font-size 14px, cor `--primary`, weight 600. Hover: cor `--primary-dark`.

  Padding vertical 12px por linha, padding horizontal 16px. Em mobile (< 640px): ocultar Coluna 2 (thumb); reduzir Coluna 4 para ícone compacto.

  **Accordion abaixo da tabela:** header "Ver detalhes de cada vídeo ▾" em font-size 13px, weight 600, `--text-2`, padding 14px 20px, cursor pointer. Ao abrir, lista 10 mini-cards, um por vídeo, cada mini-card com:
  - Título do vídeo em font-size 14px, weight 700, `--text-1`, margin-bottom 4px
  - Link "↗ Ver no YouTube" em font-size 11px, cor `--primary`, margin-bottom 12px
  - Grid 2 colunas interno (em mobile, 1 coluna):
    - **Esquerda — "Características da thumb":** label uppercase font-size 10px weight 700 `--text-3` letter-spacing 0.8px. Lista com 4 bullets (cores, expressão, texto em destaque, elementos visuais), marcador `•` verde, font-size 12px, `--text-2`, line-height 1.6.
    - **Direita — "Comentários mais curtidos":** label uppercase mesma formatação. 3 citações em divs empilhadas, cada uma com `padding: 8px 12px`, `border-left: 3px solid var(--primary-light)`, `background: var(--main-bg)`, `border-radius: 0 4px 4px 0`, font-size 12px, `--text-2`, line-height 1.5, font-style italic, margin-bottom 6px.
  - Linha inferior com 2 mini-blocos lado a lado (grid 2 colunas):
    - "ÂNGULO DO TÍTULO": texto curto em font-size 12px, `--text-2`
    - "LACUNA PARA O PRODUTO": texto curto em font-size 12px, `--text-2`, cor de fundo `--highlight-bg` em pill pequena
  - Divider entre mini-cards: `1px solid var(--border-2)`, margin 16px 0.

  **Card destaque verde ao final do bloco:** fundo `--highlight-bg`, borda `1px solid var(--highlight-border)`, border-radius `--r`, padding 20px 24px, margin-top 20px.
  - Label "PADRÃO IDENTIFICADO" em font-size 11px weight 700 `--primary` uppercase letter-spacing 0.8px margin-bottom 12px.
  - Lista com 4 bullets, marcador `•` verde, font-size 13px, `--primary-dark`, weight 500, line-height 1.7:
    1. Padrão de thumb (cores, expressão e texto recorrentes)
    2. Padrão de gancho de título
    3. Dor/desejo dominante nos comentários
    4. Lacunas do mercado

  Dados dos padrões vêm da subseção "Padrões Observados nos 10 Vídeos" do `pesquisa-mercado.md`.

  **Bloco 9 — Alertas Regulatórios (card full-width, fundo alaranjado):**
  Só renderizar se houver dados relevantes. Fundo `#fffbeb`, borda `1px solid #fde68a`, border-radius `--r`. Label "ALERTAS REGULATÓRIOS" em `#d97706`, uppercase, com ícone de triângulo `▲` antes. Lista de palavras proibidas em pills `.badge-orange`, regras do nicho em texto explicativo abaixo.

  **Bloco 10 — Footer com Circular Progress + Fontes (card full-width, grid 2 colunas):**

  - **Coluna 1 — Circular Progress SVG** (confiança da pesquisa):
    SVG 120x120 centralizado: círculo base `--border-2` 8px, círculo overlay com `stroke-dasharray` proporcional ao nível (Alta=88-100%, Média=50-65%, Baixa=20-35%), stroke `--primary` (Alta) ou `--badge-orange-text` (Média) ou `#ef4444` (Baixa), rotate -90deg no origin. Percentual grande no centro (font-size 22px, font-weight 800) e label "Confiança" abaixo em `--text-3`.

  - **Coluna 2 — Fontes Consultadas:**
    Label "FONTES CONSULTADAS (N)". Lista compacta de fontes em 2 colunas CSS (`columns: 2`), cada fonte com ícone `↗` antes do nome e descrição resumida. Máximo 8 fontes.

**Botão "Exportar PDF":**
- Label: "Exportar PDF (Ctrl+P)"
- Ação: `window.print()`
- CSS `@media print`: expande todos os accordions (`max-height: none !important; overflow: visible !important`), esconde sidebar e barra mobile, remove sombras, ajusta padding para impressão A4
- Produz PDF diagramado via Ctrl+P do navegador

Não mostre o código HTML ao usuário. Salve o arquivo silenciosamente.

Após salvar, informe:
```
Identidade do consumidor salva em meus-produtos/{ativo}/idconsumidor.md.

Painel de entregas gerado com todas as informações do produto.

Para visualizar, copie e cole no navegador:
file:///C:/Users/Elen/.cursor/Imersão IA/workshop_inteligente/meus-produtos/{ativo}/painel-entregas.html
```

### 5. Próximo Passo

**Se Middle Ticket:**
```
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
