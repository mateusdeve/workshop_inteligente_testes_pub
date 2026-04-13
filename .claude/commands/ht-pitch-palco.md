---
name: workshop-marketing:ht-pitch-palco
description: Criar o script completo do pitch de venda dentro do evento C10X. da transição do conteúdo à oferta, ancoragem de valor, apresentação de preço, bônus e fechamento ao vivo.
---

# HT. Pitch de Palco

Cria o script completo do momento de venda dentro do evento. da transição do conteúdo para a oferta até o CTA final.

## Usage

```
/c10x-pitch-palco
```

## O Que Fazer

### 1. Contexto
Leia `entregas/.ativo`, depois `entregas/{ativo}/perfil.md` e `entregas/{ativo}/idconsumidor.md`.
Se existir `entregas/{ativo}/c10x/oferta-*.md`, leia para usar os entregáveis, bônus e preço.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4. Produto e Preço:**
```
O que vai ser vendido no pitch e qual o investimento?
(ex: "Mentoria de 3 meses. R$5.000 à vista ou 6x R$997")
```

```
--- Bloco 1/4 concluído ---
Produto: [nome] | R$ [valor]
Próximo: Duração do pitch
---
```

**Bloco 2/4. Duração:**
```
Quanto tempo tem para o pitch?

1. 30 minutos (padrão webinar)
2. 45 minutos (retiro online)
3. 60 minutos (retiro presencial ou imersão longa)

Digite o número:
```

```
--- Bloco 2/4 concluído ---
Produto: [nome] | R$ [valor]
Duração: [tempo]
Próximo: Histórico de vendas
---
```

**Bloco 3/4. Prova Social:**
```
Tem casos ou resultados de alunos/clientes para usar no pitch?
(ex: "Sim, tenho 3 casos com números", "Tenho depoimentos mas sem números", "Ainda não tenho")
```

```
--- Bloco 3/4 concluído ---
Produto: [nome] | R$ [valor]
Duração: [tempo]
Prova: [tipo de prova disponível]
Próximo: Principal objeção
---
```

**Bloco 4/4. Principal Objeção:**
```
Qual a maior objeção do seu público para comprar no evento?

1. Preço / dinheiro
2. Tempo / agenda
3. Dúvida se funciona para mim
4. Precisa pensar / consultar alguém
5. Outra (descreva)

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do pitch:
- Produto: [nome] | R$ [valor]
- Duração: [tempo]
- Prova social: [tipo]
- Objeção principal: [objeção]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**SCRIPT DE PITCH DE PALCO. C10X**

---

**[0:00-3:00] TRANSIÇÃO DO CONTEÚDO PARA O PITCH**

Script de ligação. sair do "modo professor" e entrar no "modo oferta":

"Ao longo desses [X dias/horas], você [resumo do que aprendeu e fez].

Agora eu preciso te mostrar algo. Porque o que você viu até agora é só o começo. E quero te fazer uma pergunta honesta:

[PERGUNTA REFLEXIVA QUE CONECTA COM A DOR. ex: 'Quanto tempo você ainda vai tentar fazer isso sozinho?']"

---

**[3:00-8:00] HISTÓRIA DE PROVA SOCIAL**

Um caso de aluno/cliente com números concretos:

"Deixa eu te contar o caso de [NOME/PERFIL]. Há [TEMPO], ele estava [SITUAÇÃO INICIAL]. Depois de [MÉTODO/PROGRAMA], conseguiu [RESULTADO ESPECÍFICO]."

Se não tiver caso: use sua própria história de transformação.

---

**[8:00-15:00] APRESENTAÇÃO DA OFERTA**

Estrutura:

"O que vou te apresentar agora é [NOME DO PROGRAMA/MENTORIA].

É para quem [PERFIL IDEAL. 2-3 características].

Em [PRAZO], você vai [QUADRO. transformação principal]."

Apresente os entregáveis em sequência, com o benefício de cada um:

"Você vai ter acesso a:

[Entregável 1]. [benefício direto]
[Entregável 2]. [benefício direto]
[Entregável 3]. [benefício direto]"

---

**[15:00-22:00] ANCORAGEM DE VALOR + BÔNUS**

"Agora, antes do investimento, quero te mostrar o que mais você recebe.

Bônus 1: [NOME]. [o que é e qual objeção resolve]
Bônus 2: [NOME]. [o que é e qual objeção resolve]
Bônus 3: [NOME]. [o que é e qual objeção resolve]

Se você fosse contratar tudo isso separado: [lista com valores individuais]. Somaria [VALOR TOTAL ANCORAGEM].

Mas o investimento no [NOME DO PROGRAMA] é de [PREÇO REAL]."

---

**[22:00-27:00] QUEBRA DA PRINCIPAL OBJEÇÃO**

Abordar diretamente a objeção mais comum, antes que o participante pense nela:

Exemplo para "está caro":
"Eu sei que [PREÇO] parece muito. Mas deixa eu te fazer um cálculo rápido. [CUSTO DE NÃO RESOLVER. perda mensal, anual]. Em [X meses], o investimento se paga com [RESULTADO MÍNIMO ESPERADO]."

---

**[27:00-30:00] GARANTIA + CTA FINAL**

"E para que você possa entrar sem risco: [GARANTIA. prazo e condições].

Se em [X dias] você não estiver satisfeito, devolvo cada centavo. Sem burocracia.

Para garantir sua vaga: [INSTRUÇÃO. ex: 'acesse o link que aparece na tela agora' ou 'me chama no WhatsApp com a palavra [PALAVRA-CHAVE]'].

As vagas são limitadas a [NÚMERO]. Quem entrar primeiro garante [BÔNUS DE AÇÃO RÁPIDA, se houver].

Te espero do outro lado."

---

**SCRIPT DE PERGUNTAS E RESPOSTAS PÓS-PITCH:**

Respostas curtas para as perguntas mais comuns após o pitch:

- "Ainda tem vaga?" → "Sim, ainda temos. O link está [LOCAL]."
- "Posso parcelar?" → "Sim, [FORMAS DE PAGAMENTO]."
- "Para que nível é?" → "Para [PERFIL]. Se você [SITUAÇÃO], é exatamente para você."
- "Quando começa?" → "[DATA DE INÍCIO]."

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`entregas/{ativo}/c10x/pitch-palco-[produto].md`

### 6. Próximo Passo
"Pitch criado. Próximo: `/ht-follow-up` para montar a sequência de quem assistiu mas não comprou, ou `/ht-spin` para os scripts de venda 1:1."
