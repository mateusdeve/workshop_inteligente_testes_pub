---
name: workshop-marketing:ht-proposta
description: Criar documento de proposta comercial formal para consultoria C10X. diagnóstico do problema, solução proposta, escopo, entregáveis, prazo, investimento e próximos passos.
---

# HT. Proposta Comercial (Consultoria)

Cria o documento de proposta comercial completo para ser enviado ao cliente após a call de diagnóstico.

## Usage

```
/c10x-proposta
```

## O Que Fazer

### 1. Contexto
Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/5. Cliente:**
```
Qual o nome do cliente e o nome da empresa (se houver)?
(ex: "Carlos Mendes. Agência Vortex")
```

```
--- Bloco 1/5 concluído ---
Cliente: [nome]
Próximo: Problema diagnosticado
---
```

**Bloco 2/5. Problema:**
```
Qual o problema principal que foi mapeado na call de diagnóstico?
Use as palavras que o próprio cliente usou para descrever o problema.
(ex: "não consegue converter leads em vendas. taxa de fechamento de 5%")
```

```
--- Bloco 2/5 concluído ---
Problema: [descrição]
Próximo: Solução proposta
---
```

**Bloco 3/5. Solução e Escopo:**
```
O que você vai fazer por ele? Descreva o escopo da consultoria.
(ex: "reestruturação do processo comercial em 60 dias. 8 sessões + auditoria + materiais")
```

```
--- Bloco 3/5 concluído ---
Escopo: [descrição]
Próximo: Prazo e entregáveis
---
```

**Bloco 4/5. Prazo e Entregáveis:**
```
Qual a duração e quais os entregáveis concretos?
(ex: "60 dias, 8 sessões semanais de 90 min, playbook comercial, treinamento da equipe")
```

```
--- Bloco 4/5 concluído ---
Prazo: [duração] | Entregáveis: [lista]
Próximo: Investimento
---
```

**Bloco 5/5. Investimento:**
```
Qual o investimento e as formas de pagamento?
(ex: "R$8.000 à vista ou 50% na assinatura + 50% na entrega")
```

**Confirmação antes de gerar:**
```
Resumo da proposta:
- Cliente: [nome]
- Problema: [descrição]
- Escopo: [o que vai fazer]
- Prazo: [duração]
- Investimento: R$ [valor]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**DOCUMENTO DE PROPOSTA COMERCIAL. C10X**

---

**PROPOSTA COMERCIAL**
Para: [NOME DO CLIENTE] | [EMPRESA]
De: [SEU NOME]
Data: [DATA]
Válida até: [DATA + 7 dias]

---

**1. DIAGNÓSTICO**

Com base em nossa conversa em [DATA DA CALL], identifiquei os seguintes pontos:

**Situação atual:**
[Resumo do que o cliente descreveu. em 3-4 linhas, usando as palavras dele]

**Problema central:**
[O problema principal em uma frase direta]

**Impacto atual:**
[Custo do problema. financeiro e operacional. usando os números que ele citou]

**O que acontece se nada mudar:**
[Consequência de não resolver. baseada no que ele disse na call]

---

**2. SOLUÇÃO PROPOSTA**

**O que vou fazer:**
[Descrição da abordagem em 2-3 parágrafos]

**Por que essa abordagem:**
[Argumento lógico de por que essa é a solução certa para o problema específico dele]

---

**3. ESCOPO E ENTREGÁVEIS**

**O que está incluído:**

| Entregável | Descrição | Prazo |
|---|---|---|
| [Entregável 1] | [O que é] | [Quando] |
| [Entregável 2] | [O que é] | [Quando] |
| [Entregável 3] | [O que é] | [Quando] |

**O que NÃO está incluído:**
[Lista clara do que está fora do escopo. protege contra expansão não combinada]

---

**4. CRONOGRAMA**

| Fase | Atividade | Semana |
|---|---|---|
| Fase 1 | [Atividade] | Semana 1-2 |
| Fase 2 | [Atividade] | Semana 3-4 |
| Fase 3 | [Atividade] | Semana 5-8 |

---

**5. RESULTADO ESPERADO**

Ao final da consultoria, [NOME DO CLIENTE] terá [RESULTADO ESPECÍFICO. baseado na visão de sucesso que ele mesmo descreveu na call].

Métrica de sucesso: [INDICADOR CONCRETO. ex: "taxa de fechamento de 5% para 15% em 60 dias"]

---

**6. INVESTIMENTO**

Investimento total: R$ [VALOR]

Formas de pagamento:
- [Opção 1]
- [Opção 2]

---

**7. GARANTIA**

[GARANTIA. se aplicável]

---

**8. PRÓXIMOS PASSOS**

Para iniciar:
1. Aprovação desta proposta
2. Assinatura do contrato de prestação de serviços
3. Pagamento da primeira parcela
4. Agendamento da primeira sessão

Para aprovar, responda este email com "Aceito" ou me chame no WhatsApp: [NÚMERO]

Esta proposta é válida até [DATA].

---

**Regras da proposta C10X:**
- Use sempre as palavras exatas que o cliente usou na call
- O diagnóstico deve soar como se você estivesse dentro da cabeça dele
- Nunca prometa resultado garantido. prometa processo e esforço
- O escopo claro protege ambos os lados. seja específico

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`meus-produtos/{ativo}/entregas/c10x/proposta-[cliente].md`

### 6. Próximo Passo
"Proposta criada. Próximo: `/ht-apresentacao-proposta` para criar o script da call de apresentação."
