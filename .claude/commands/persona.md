---
name: workshop-marketing:persona
description: Criar perfil completo do cliente ideal usando as 3 Identidades da metodologia VTSD (Comunicador, Consumidor, Produto) e mapeamento de Urgências Ocultas.
---

# Persona — Perfil do Cliente Ideal (3 Identidades)

Cria documento completo de persona usando a metodologia VTSD: Identidade do Consumidor detalhada, paliativos, objeções e comunicação. As Urgências Ocultas já devem existir no `perfil.md` (geradas pelo `/meu-produto`).

## Usage

```
/persona
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md`. Se não existir, oriente a usar `/meu-produto` primeiro.
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

**Bloco 2/3 — Comportamento:**

Pergunta 4:
```
O que essa pessoa já tentou para resolver o problema e não funcionou?
(ex: "Cursos gratuitos no YouTube", "Dietas da moda", "Planilhas que achou no Google")
```

Pergunta 5:
```
Se tivesse um resultado mágico, qual seria? O que ela diria para a amiga?
(ex: "Consegui falar inglês na reunião sem travar")
```

Pergunta 6:
```
Onde essa pessoa busca informação?

1. Instagram
2. YouTube
3. Google
4. WhatsApp/Telegram
5. TikTok
6. Vários (quais?)

Digite o número:
```

```
--- Bloco 2/3 concluído ---
Perfil: [dados demográficos]
Paliativos: [o que já tentou]
Sonho: [resultado mágico]
Canais: [onde busca info]
Próximo: Objeções
---
```

**Bloco 3/3 — Objeções:**

Pergunta 7:
```
O que impediria essa pessoa de comprar? Quais as objeções?
(ex: "Acha caro", "Não tem tempo", "Já tentou e não deu certo", "Precisa falar com o marido")
```

```
--- Bloco 3/3 concluído ---
Persona completa. Gerando documento...
---
```

**Confirmação antes de gerar:**
```
Resumo da persona:
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
Salve em `meu-negocio/persona.md`:

```markdown
# Persona: [Nome Fictício]

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
```

NOTA: As Urgências Ocultas (dores, desejos, dúvidas, assuntos relacionados) ficam centralizadas em `meu-negocio/perfil.md`. Não duplicar aqui.

### 4. Próximo Passo
"Persona salva em `meu-negocio/persona.md`. Use `/texto-de-venda` para criar copys falando com essa persona, ou `/pagina-de-vendas` para criar a página."
