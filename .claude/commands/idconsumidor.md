---
name: workshop-marketing:idconsumidor
description: Criar identidade do consumidor (cliente ideal) usando as 3 Identidades da metodologia VTSD (Comunicador, Consumidor, Produto) e mapeamento alinhado às Urgências Ocultas do perfil.
---

# Identidade do consumidor — Cliente ideal (3 Identidades)

Cria o documento de **identidade do consumidor** (VTSD): perfil detalhado, paliativos, objeções e comunicação. As Urgências Ocultas já devem existir no `perfil.md` (geradas pelo `/meu-produto`).

## Usage

```
/idconsumidor
```

## Princípios de Comportamento

### Postura: Consultor que gera, não formulário que pergunta

Você já tem o `perfil.md` com Quadro, Furadeira, Identidades, Decorados, Urgências Ocultas e (possivelmente) dados de pesquisa de mercado. Use TUDO isso para gerar a persona proativamente.

- **Pergunte o mínimo** — só dados que apenas o aluno sabe (gênero, idade, profissão)
- **Gere e sugira o resto** — paliativos, objeções, canais, tom de voz, frases da persona
- **Apresente para validação** — o aluno aprova, ajusta ou complementa
- **"Não sei" = você sugere** — use dados do perfil e pesquisa de mercado para propor a resposta

### Pesquisa de mercado como apoio

Se durante o `/meu-produto` foi feita pesquisa de mercado, use os dados para alimentar a persona. Se não foi feita, ofereça fazer agora.

## O Que Fazer

### 1. Contexto
Leia `produtos/.ativo` para obter o produto ativo. Leia `produtos/{ativo}/perfil.md`. Se não existir, oriente a usar `/meu-produto` primeiro.
Verifique se as Urgências Ocultas já estão completas no perfil. Se estiverem com stubs ("a completar"), gere as Urgências Ocultas completas e atualize o `perfil.md` antes de continuar.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Dados Demográficos:**

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

**Bloco 2/3 — Comportamento (Geração Proativa):**

Com base nos dados demográficos + Urgências Ocultas + Identidade do Consumidor do perfil + pesquisa de mercado, GERE automaticamente:

- **Paliativos** — o que essa pessoa já tentou e não funcionou (baseado nas dores e no nicho)
- **Sonho** — a frase que ela diria para uma amiga se alcançasse o resultado (baseado nos desejos)
- **Canais** — onde essa pessoa busca informação (baseado no perfil demográfico e no nicho)

Apresente tudo gerado de uma vez para o aluno validar e ajustar. Não peça item por item.

Mostre progresso ao concluir.

**Bloco 3/3 — Objeções (Geração Automática):**

GERE as objeções automaticamente com base no perfil do consumidor, preço do produto, nicho e dados da pesquisa de mercado. NÃO liste opções para o aluno escolher — gere a lista completa de objeções típicas desse público e já inclua como quebrar cada uma.

Apresente tudo para validação. O aluno aprova, ajusta, adiciona ou remove.

**Confirmação antes de gerar:**
```
Resumo da identidade do consumidor:
- Perfil: [gênero], [idade], [profissão]
- Renda: [renda]
- Paliativos: [o que já tentou]
- Sonho: [resultado mágico]
- Canais: [onde busca info]
- Objeções: [principais objeções]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Gerar Documento
Salve em `produtos/{ativo}/idconsumidor.md`:

```markdown
# Identidade do consumidor: [Nome Fictício]

## Para Quem É
[Frase de posicionamento clara, 1-2 linhas]
"Este produto é para [perfil específico], que [problema/situação atual], e quer [transformação desejada]."

Não é para: [exclusões que ajudam a posicionar — quem NÃO é o público]

## Identidade do Consumidor
- **Idade:** / **Gênero:** / **Profissão:**
- **Renda:** / **Estado civil:** / **Localização:**
- **Nível de consciência:** [inconsciente → totalmente consciente]
- **Onde busca informação:** [canais]

## Paliativos (o que já tentou)
- [soluções que tentou e não funcionaram]
- [por que falharam]

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

## Baldes de Conteúdo (Identidade do Comunicador)

Os baldes são as categorias de conteúdo que o comunicador usa para se conectar com esse público. Cada balde gera uma linha de posts, vídeos e anúncios com um propósito diferente.

Gere 5 baldes com base no perfil do consumidor, nas Urgências Ocultas e nos Decorados:

### Balde 1 — [Nome do Balde]
- **Propósito:** [o que esse balde faz pelo público — educar, engajar, converter]
- **Tom:** [como falar nesse balde]
- **Exemplos de temas:** [3-5 ideias concretas baseadas nas Urgências Ocultas desse público]

### Balde 2 — [Nome do Balde]
- **Propósito:**
- **Tom:**
- **Exemplos de temas:**

### Balde 3 — [Nome do Balde]
- **Propósito:**
- **Tom:**
- **Exemplos de temas:**

### Balde 4 — [Nome do Balde]
- **Propósito:**
- **Tom:**
- **Exemplos de temas:**

### Balde 5 — [Nome do Balde]
- **Propósito:**
- **Tom:**
- **Exemplos de temas:**
```

NOTA: As Urgências Ocultas (dores, desejos, dúvidas, assuntos relacionados) ficam centralizadas em `produtos/{ativo}/perfil.md`. Não duplicar aqui. Os baldes são derivados delas — não copiados.

### 4. Próximo Passo
"Identidade do consumidor salva em `produtos/{ativo}/idconsumidor.md`. Use `/texto-de-venda` para criar copys falando com esse público, ou `/pagina-de-vendas` para criar a página."
