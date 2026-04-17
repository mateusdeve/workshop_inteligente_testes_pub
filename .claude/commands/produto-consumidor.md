---
name: workshop-marketing:produto-consumidor
description: Criar identidade do consumidor (cliente ideal) usando as 3 Identidades da metodologia VTSD e gerar o Painel de Entregas HTML completo.
---

# Identidade do Consumidor. Cliente Ideal e Painel de Entregas

Cria o documento de **identidade do consumidor** (VTSD): perfil detalhado, objeções e comunicação. Ao final, gera o Painel de Entregas HTML com todos os dados do produto.

**REGRA — Paliativos:**
- **Middle Ticket:** gerar paliativos (ferramentas dentro do produto que resolvem dores específicas do consumidor)
- **Low Ticket:** NÃO gerar paliativos. Produto de entrada não tem profundidade suficiente para mapear paliativos internos

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

- **Paliativos** *(somente Middle Ticket)* — ferramentas dentro do produto que resolvem dores específicas do consumidor (baseado nas dores mapeadas nas Urgências Ocultas e na Furadeira)
- **Sonho** — a frase que ela diria para uma amiga se alcançasse o resultado (baseado nos desejos)
- **Canais** — onde essa pessoa busca informação (baseado no perfil demográfico e no nicho)

Apresente tudo gerado de uma vez para o aluno validar e ajustar. Não peça item por item.

Mostre progresso ao concluir.

**Bloco 3/3. Objeções (Geração Automática):**

GERE as objeções automaticamente com base no perfil do consumidor, preço do produto, nicho e dados de `pesquisa-mercado.md` (especialmente o resumo do Reclame Aqui). NÃO liste opções para o aluno escolher. Gere a lista completa de objeções típicas desse público e já inclua como quebrar cada uma.

Apresente tudo para validação. O aluno aprova, ajusta, adiciona ou remove.

**Confirmação antes de gerar:**
```
Resumo da identidade do consumidor:
- Perfil: [gênero], [idade], [profissão]
- Renda: [renda]
- Paliativos: [ferramentas do produto que resolvem dores específicas — incluir apenas se Middle Ticket]
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

## Paliativos (somente Middle Ticket — ferramentas do produto que resolvem dores específicas)
- [ferramenta/recurso do produto] → [dor específica que resolve]

*Se Low Ticket: omitir esta seção inteiramente.*

## Objeções de Compra
- [objeção] → [como quebrar]

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
  --text-1: #111827;
  --text-2: #374151;
  --text-3: #6b7280;
  --border: #e5e7eb;
  --border-2: #f3f4f6;
  --badge-green-bg: #dcfce7;
  --badge-green-text: #16a34a;
  --badge-purple-bg: #ede9fe;
  --badge-purple-text: #7c3aed;
  --badge-pink-bg: #fce7f3;
  --badge-pink-text: #db2777;
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

**Estrutura da página:**

1. **Sidebar fixa** à esquerda: `width: var(--sidebar-w)`, `background: var(--sidebar-bg)`, `border-right: 1px solid var(--sidebar-border)`, `position: fixed`, `top: 0`, `left: 0`, `height: 100vh`, `overflow-y: auto`. Contém logo "Painel de Entregas" em `--text-1`, peso 700, e o nome do produto abaixo em `--text-3`, font-size 11px. Itens de nav em texto `--text-2`, sem ícones, sem emojis. Item ativo com fundo `--border-2` e texto `--primary-dark`, peso 600, borda esquerda `3px solid var(--primary)`. Sem fundos escuros, sem gradientes.

2. **Main content**: `margin-left: var(--sidebar-w)`, `background: var(--main-bg)`, `min-height: 100vh`, `padding: 32px 40px`.

3. **Breadcrumb** no topo do conteúdo: texto `Painel de Entregas › {nome da seção}` em `--text-3`, font-size 13px.

4. **Título da seção**: font-size 22px, font-weight 700, cor `--text-1`, margin-bottom 4px. Subtítulo em `--text-3`, font-size 13px.

5. **Painéis** (`display: none` por padrão, `display: block` + animação `fadeIn` quando ativo via JS).

**Componentes obrigatórios:**

**Cards de stat** (para Visão Geral): fundo `--surface`, borda `1px solid var(--border)`, border-radius `--r`, padding 24px, sombra `--sh1`. Valor numérico em font-size 28px, weight 700, cor `--text-1`. Label em font-size 12px, weight 500, cor `--text-3`, uppercase, letter-spacing 0.5px.

**Cards de conteúdo**: fundo `--surface`, borda `1px solid var(--border)`, border-radius `--r`, padding 24px, sombra `--sh1`. Hover: sombra `--sh2`. Título em font-size 11px, weight 700, cor `--text-3`, uppercase, letter-spacing 0.8px. Texto em font-size 13px, cor `--text-2`, line-height 1.65.

**Accordions**: fundo `--surface`, borda `1px solid var(--border)`, border-radius `--r`, margin-bottom 10px, sombra `--sh1`. Header com padding 14px 20px, font-size 14px, weight 600, cor `--text-1`. Ícone de toggle `▾` que rotaciona 180° quando aberto. Corpo animado com `max-height` de 0 para 3000px via `cubic-bezier(.4,0,.2,1)`. Items em lista com dot verde `•` como marcador, font-size 13px, cor `--text-2`.

**Badges/pills**: border-radius 9999px (pill), font-size 11px, font-weight 700, padding 3px 10px. Variantes: verde (`.badge-green`), roxo (`.badge-purple`), rosa (`.badge-pink`), escuro (`.badge-dark`), neutro (`.badge-neutral`).

**Botão primário**: fundo `--primary`, cor branco, border-radius `--r2`, padding 8px 18px, font-size 13px, weight 600. Hover: fundo `--primary-dark`.

**Divider**: `height: 1px`, `background: var(--border)`, `margin: 28px 0`.

**Tabela de concorrentes** (seção Pesquisa de Mercado): sem zebra-stripe, borda inferior `1px solid var(--border-2)` em cada linha. Header da tabela em font-size 11px, uppercase, letter-spacing 1px, cor `--text-3`, weight 700. Células em font-size 13px, cor `--text-2`.

**Dot de status ativo**: círculo 8px, fundo `--primary`, display inline-block, margin-right 6px.

**Responsivo:** abaixo de 768px, sidebar oculta e aparece menu de tabs horizontais sticky no topo com fundo `--surface`, borda inferior `--border`, sem emojis.

**JavaScript:** função `showPanel(id)` que remove classe `.active` de todos os painéis e adiciona no alvo. Sincroniza estado ativo nos itens de nav da sidebar e da barra mobile.

---

**Seções do painel e agrupamento na navegação:**

Grupo **Produto** (todas as seções ficam sob este grupo na sidebar):
- Visão Geral — Nome do Produto, Preço, Tipo (Low/Middle Ticket)
- Quadro — Texto do Quadro aprovado
- Furadeira — Macroetapas, microetapas, link para `furadeira-visual.html`
- Decorados — Accordion com 5 categorias: Financeiro, Tempo, Autoestima, Reputação, Crescimento (10 itens cada)
- Urgências Ocultas — Accordion com 7 categorias: Dores, Dúvidas, Desejos, Assuntos Relacionados, Urgências Quentes, Urgências Frias, Urgências Inusitadas (10 itens cada)

Grupo **Identidades**:
- Identidade do Produto — Diferencial, formato, preço, argumentos incontestáveis, objeções
- Identidade do Consumidor — Perfil demográfico, comportamento, canais, sonho, paliativos (se Middle Ticket), baldes de Para Quem É
- Identidade do Comunicador — Tom de voz, posicionamento, palavras que conectam, palavras que afastam

Grupo **Pesquisa**:
- Pesquisa de Mercado — Dados do mercado, oportunidades, cuidados, Reclame Aqui, tabela de concorrentes, link para `pesquisa-mercado.md`

**Botão "Exportar PDF":**
- Usa `window.print()` com CSS `@media print` que expande todos os accordions e remove a sidebar
- Produz PDF limpo e diagramado via Ctrl+P do navegador

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
