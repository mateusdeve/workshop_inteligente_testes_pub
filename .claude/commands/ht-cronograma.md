---
name: workshop-marketing:ht-cronograma
description: Montar o cronograma completo de um Retiro Online ou evento C10X. agenda por dia, blocos de conteúdo, intervalos, momentos de engajamento e timing do pitch.
---

# HT. Cronograma do Evento

Monta a agenda completa do Retiro Online ou evento high ticket com timing, blocos de conteúdo e momento estratégico do pitch.

## Usage

```
/c10x-cronograma
```

## O Que Fazer

### 1. Contexto
Leia `entregas/.ativo`, depois `entregas/{ativo}/perfil.md`.
Se existir `entregas/{ativo}/c10x/big-idea-*.md`, leia para alinhar com a promessa do evento.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4. Formato do Evento:**
```
Qual o formato do evento?

1. Retiro Online. 2 dias (formato mais comum no C10X)
2. Retiro Online. 1 dia (imersão intensiva)
3. Retiro Online. 3 dias (alta profundidade)
4. Webinar com pitch (evento único, 2-3 horas)

Digite o número:
```

```
--- Bloco 1/4 concluído ---
Formato: [tipo]
Próximo: Horários
---
```

**Bloco 2/4. Horários:**
```
Qual o horário de início e término por dia?
(ex: "9h às 18h", "10h às 20h")
```

```
--- Bloco 2/4 concluído ---
Formato: [tipo]
Horário: [início] às [término]
Próximo: Conteúdo principal
---
```

**Bloco 3/4. Conteúdo:**
```
Quais são os 3 a 5 grandes temas que vai ensinar no evento?
Não precisa ser o roteiro completo. só os temas centrais.
(ex: "posicionamento, precificação, captação de clientes, fechamento")
```

```
--- Bloco 3/4 concluído ---
Formato: [tipo]
Horário: [horário]
Temas: [lista]
Próximo: Momento do pitch
---
```

**Bloco 4/4. Momento do Pitch:**
```
Quando prefere fazer o pitch de vendas?

1. Final do último dia (clássico. melhor conversão)
2. Início do segundo dia (para fechar antes do conteúdo final)
3. Meio do último dia (antes do encerramento com conteúdo motivacional)

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do evento:
- Formato: [tipo]
- Horário: [horário] por dia
- Temas: [lista]
- Pitch: [momento]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**Estrutura padrão para Retiro Online de 2 dias:**

---

**DIA 1. [Data]**

| Horário | Bloco | Duração |
|---|---|---|
| 09h00 | Abertura e boas-vindas | 30 min |
| 09h30 | Contexto e promessa do evento | 20 min |
| 09h50 | Bloco 1: [Tema 1] | 60 min |
| 10h50 | Intervalo | 15 min |
| 11h05 | Bloco 2: [Tema 2] | 60 min |
| 12h05 | Almoço | 60 min |
| 13h05 | Recapitulação + ativação | 15 min |
| 13h20 | Bloco 3: [Tema 3] | 75 min |
| 14h35 | Intervalo | 15 min |
| 14h50 | Exercício prático / implementação | 45 min |
| 15h35 | Revisão e perguntas | 20 min |
| 15h55 | Encerramento do Dia 1 + Missão | 15 min |

---

**DIA 2. [Data]**

| Horário | Bloco | Duração |
|---|---|---|
| 09h00 | Abertura do Dia 2 + revisão da missão | 25 min |
| 09h25 | Bloco 4: [Tema 4] | 60 min |
| 10h25 | Intervalo | 15 min |
| 10h40 | Bloco 5: [Tema 5] | 60 min |
| 11h40 | Exercício de implementação | 30 min |
| 12h10 | Almoço | 60 min |
| 13h10 | Recapitulação + prova social (depoimentos ao vivo) | 30 min |
| 13h40 | Conteúdo de fechamento emocional | 30 min |
| 14h10 | PITCH DE OFERTA | 45 min |
| 14h55 | Abertura de perguntas sobre a oferta | 20 min |
| 15h15 | Encerramento + CTA final | 10 min |

---

**Notas estratégicas do cronograma:**

- Missão do Dia 1: tarefa simples que o participante faz à noite para engajar no Dia 2
- Prova social antes do pitch: depoimentos ao vivo ou em vídeo de quem já obteve resultados
- Pitch nunca começa em horário de baixa energia (logo após almoço ou após 17h)
- Intervalo de 15 min antes do pitch para o participante sair do "modo aluno" e entrar no "modo decisão"

**Para Webinar de Dia Único:**

| Horário | Bloco | Duração |
|---|---|---|
| 20h00 | Abertura e credenciamento | 15 min |
| 20h15 | Contexto + promessa | 15 min |
| 20h30 | Bloco 1 de conteúdo | 40 min |
| 21h10 | Bloco 2 de conteúdo | 30 min |
| 21h40 | Prova social | 10 min |
| 21h50 | Pitch de oferta | 30 min |
| 22h20 | Perguntas + CTA final | 10 min |

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`entregas/{ativo}/c10x/cronograma-[evento].md`

### 6. Próximo Passo
"Cronograma pronto. Próximo: `/ht-conteudo` para roteirizar os blocos de ensino, ou `/ht-pitch-palco` para criar o script do momento de venda."
