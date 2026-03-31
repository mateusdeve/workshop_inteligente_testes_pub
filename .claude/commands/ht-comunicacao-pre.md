---
name: workshop-marketing:ht-comunicacao-pre
description: Criar a sequência completa de comunicação pré-evento C10X — mensagens de WhatsApp do D-7 ao D0 e emails de aquecimento para inscritos, aumentando presença e engajamento.
---

# HT — Comunicação Pré-Evento

Cria a sequência completa de mensagens de WhatsApp e emails para os inscritos do evento, do D-7 ao dia do evento.

## Usage

```
/c10x-comunicacao-pre
```

## O Que Fazer

### 1. Contexto
Leia `produtos/.ativo`, depois `produtos/{ativo}/perfil.md`.
Se existir `produtos/{ativo}/entregas/c10x/big-idea-*.md`, leia para usar o mote e a promessa.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Dados do Evento:**
```
Qual o nome e data do evento?
(ex: "Retiro Negócio de Alto Valor — dias 15 e 16 de abril")
```

```
--- Bloco 1/3 concluído ---
Evento: [nome] | [data]
Próximo: Canais de comunicação
---
```

**Bloco 2/3 — Canais:**
```
Quais canais de comunicação vai usar com os inscritos?

1. WhatsApp + Email (completo — recomendado)
2. Só WhatsApp
3. Só Email

Digite o número:
```

```
--- Bloco 2/3 concluído ---
Canais: [escolha]
Próximo: Formato de aquecimento
---
```

**Bloco 3/3 — Aquecimento:**
```
Vai enviar algum conteúdo de preparação antes do evento?
(ex: "vídeo de boas-vindas", "material de leitura", "missão prévia", "nada ainda")
```

**Confirmação antes de gerar:**
```
Resumo:
- Evento: [nome] | [data]
- Canais: [WhatsApp / Email / ambos]
- Aquecimento: [tipo ou nenhum]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**SEQUÊNCIA DE WHATSAPP — D-7 ao D0**

---

**D-7 (7 dias antes) — Confirmação + Expectativa**

Objetivo: confirmar presença e gerar antecipação.

Mensagem:
"[Nome], sua inscrição no [NOME DO EVENTO] está confirmada.

Nos dias [DATAS], das [HORÁRIO], você vai [TRANSFORMAÇÃO PRINCIPAL DO EVENTO].

Para aproveitar ao máximo, recomendo que [TAREFA SIMPLES DE PREPARAÇÃO — ex: anote 3 perguntas que quer responder durante o evento].

Em breve te envio mais detalhes. Qualquer dúvida, responde aqui."

---

**D-5 — Conteúdo de Valor**

Objetivo: aquecimento com insight relacionado ao tema do evento.

Mensagem:
"[Nome], antes do [NOME DO EVENTO], quero te deixar um pensamento.

[INSIGHT OU DADO RELEVANTE DO NICHO — algo que gera reflexão sobre o problema que o evento resolve]

Isso é exatamente o que vamos trabalhar juntos nos dias [DATAS]. Até lá."

---

**D-3 — Missão Prévia**

Objetivo: engajar com uma tarefa simples que prepara para o evento.

Mensagem:
"[Nome], faltam 3 dias para o [NOME DO EVENTO].

Quero te pedir uma coisa antes de começarmos: [MISSÃO SIMPLES — ex: 'anote qual é o principal obstáculo no seu negócio hoje. Em uma frase.']

Isso vai tornar sua experiência muito mais prática. Me envia quando terminar."

---

**D-1 — Contagem Regressiva**

Objetivo: gerar antecipação e garantir confirmação de presença.

Mensagem:
"[Nome], amanhã começa o [NOME DO EVENTO].

[HORÁRIO DE INÍCIO] — [LINK DA SALA/PLATAFORMA]

Salva esse link. Chegamos às [HORÁRIO -10min] para resolver qualquer problema técnico.

Nos vemos amanhã."

---

**D0 (manhã do evento) — Lembrete Final**

Mensagem:
"Hoje é o dia.

[NOME DO EVENTO] começa em [X horas / às X horas].

[LINK DA SALA]

Estamos te esperando. Até já."

---

**D0 (1 hora antes) — Ativação**

Mensagem:
"Falta 1 hora. Separa água, ajeita o ambiente e desliga o que distrai.

[LINK DA SALA]

A gente começa pontualmente."

---

**SEQUÊNCIA DE EMAILS — PRÉ-EVENTO**

---

**Email 1 — Confirmação de inscrição (imediato após cadastro)**

Assunto: Sua vaga no [NOME DO EVENTO] está garantida

Corpo:
Confirmação + o que esperar + próximos passos + data na agenda (sugestão de adicionar ao calendário).

---

**Email 2 — D-5 — Preparação**

Assunto: O que fazer antes do [NOME DO EVENTO]

Corpo:
Insight de aquecimento + missão prévia + link da sala para salvar + o que levar (caderno, caneta, água).

---

**Email 3 — D-1 — Lembrete**

Assunto: Amanhã começa

Corpo:
Confirmação de horário + link + o que esperar no primeiro bloco + CTA para confirmar presença respondendo o email.

---

**Email 4 — D0 — "Começou"**

Assunto: Estamos ao vivo agora

Corpo:
Link direto para a sala. Texto mínimo. CTA único.

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`produtos/{ativo}/entregas/c10x/comunicacao-pre-[evento].md`

### 6. Próximo Passo
"Sequência de aquecimento pronta. Próximo: `/ht-pitch-palco` para criar o script do momento de venda no evento."
