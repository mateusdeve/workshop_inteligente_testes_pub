---
name: workshop-marketing:ht-anuncios
description: Criar anúncios específicos para captar inscritos em eventos C10X — foco em urgência, escassez, autoridade e especificidade da transformação. Diferente dos anúncios perpétuos.
---

# HT — Anúncios para Captação de Evento

Cria pacote de anúncios para atrair inscritos qualificados para o evento C10X. Foco em urgência, escassez e especificidade — diferente dos anúncios de perpétuo.

## Usage

```
/c10x-anuncios
```

## O Que Fazer

### 1. Contexto
Leia `produtos/.ativo`, depois `produtos/{ativo}/perfil.md` e `produtos/{ativo}/idconsumidor.md`.
Se existir `produtos/{ativo}/entregas/c10x/big-idea-*.md`, leia para usar a promessa e o mote.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Dados do Evento:**
```
Qual o nome, data e formato do evento?
(ex: "Retiro Negócio de Alto Valor — dias 15 e 16 de abril, online")
```

```
--- Bloco 1/3 concluído ---
Evento: [nome] | [data]
Próximo: Tipo de anúncio
---
```

**Bloco 2/3 — Tipo de Anúncio:**
```
Que tipo de anúncio precisa?

1. Conjunto completo (texto + vídeo + stories — recomendado)
2. Só anúncios de texto (feed e stories)
3. Só roteiros de vídeo (para gravar)
4. Anúncios de remarketing (para quem visitou a página mas não se inscreveu)

Digite o número:
```

```
--- Bloco 2/3 concluído ---
Tipo: [escolha]
Próximo: Orçamento e prazo
---
```

**Bloco 3/3 — Prazo de Captação:**
```
Quanto tempo antes do evento vai rodar os anúncios?
(ex: "30 dias antes", "15 dias antes", "1 semana")
```

**Confirmação antes de gerar:**
```
Resumo:
- Evento: [nome] | [data]
- Tipo de anúncio: [escolha]
- Prazo de captação: [período]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**Regras específicas para anúncios de evento C10X:**

Os anúncios de evento usam gatilhos diferentes dos anúncios perpétuos:
- Urgência real (data fixa, vagas limitadas)
- Especificidade da transformação (o que acontece DURANTE o evento)
- Autoridade (quem vai ensinar e por que pode)
- Escassez concreta (número de vagas ou prazo de inscrição)

**Pacote de anúncios:**

---

**ANÚNCIO 1 — AUTORIDADE (feed — texto longo)**

Gancho: fato surpreendente ou resultado de aluno
Desenvolvimento: contexto do problema + o que o evento resolve
CTA: "Vagas abertas para [NOME DO EVENTO] — [DATA]. Link na bio."

---

**ANÚNCIO 2 — ESPECIFICIDADE (feed — texto médio)**

Gancho: o que o participante vai ter ao final do evento (concreto, verificável)
Desenvolvimento: 3 resultados práticos que saem do evento com eles
CTA: "Inscrições abertas até [DATA]. [Link]"

---

**ANÚNCIO 3 — ESCASSEZ/URGÊNCIA (feed — texto curto)**

Gancho: número de vagas restantes ou prazo de inscrição
Desenvolvimento: o que perde quem não participar
CTA: "Garanta sua vaga agora. [Link]"

---

**ANÚNCIO 4 — PROVA SOCIAL (feed — texto médio)**

Gancho: resultado de participante de edição anterior (com números)
Desenvolvimento: contexto do resultado + como o evento contribuiu
CTA: "A próxima turma começa em [DATA]. [Link]"

---

**ANÚNCIO 5 — REMARKETING (para visitantes da página)**

Gancho: menção direta a quem já visitou mas não se inscreveu
Desenvolvimento: quebra de objeção principal (tempo, valor, momento)
CTA: urgência — "As inscrições fecham em [X dias]."

---

**ROTEIRO DE VÍDEO — ANÚNCIO DIRETO (30-60 seg):**

Estrutura:
- 0-5s: Gancho visual + frase de abertura (dor ou resultado inesperado)
- 5-20s: Desenvolvimento — o que é o evento e para quem é
- 20-40s: O que o participante vai alcançar (3 bullets rápidos)
- 40-55s: CTA + data + urgência

**Estrutura de campanha recomendada:**

Fase 1 (D-30 a D-15): Anúncios 1 e 2 — consciência e especificidade
Fase 2 (D-15 a D-7): Anúncios 2 e 3 — conversão com urgência crescente
Fase 3 (D-7 a D0): Anúncio 3 e remarketing — escassez máxima

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`produtos/{ativo}/entregas/c10x/anuncios-evento-[nome].md`

### 6. Próximo Passo
"Anúncios criados. Próximo: `/ht-comunicacao-pre` para montar a sequência de aquecimento dos inscritos antes do evento."
