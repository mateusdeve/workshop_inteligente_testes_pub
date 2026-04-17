---
name: workshop-marketing:comercial-playbook
description: Criar scripts de venda 1:1 usando SPIN Selling adaptado, scripts de fechamento, quebra de objeções e pitch comercial. Entrega em HTML único, formatado para leitura e exportação em PDF. Baseado na metodologia C10X do VTSD.
---

# Playbook Comercial. Scripts de Venda 1:1

Cria scripts de vendas consultivas usando SPIN Selling adaptado (C10X). **Produto final:** arquivo **HTML** único, bem formatado, com CSS para tela e impressão, convertível em PDF pelo navegador (Imprimir → Salvar como PDF). Siga a skill `playbook-comercial` para estrutura e requisitos do HTML.

## Usage

```
/comercial-playbook
```

## O Que Fazer

### 1. Contexto
Leia `meus-produtos/{ativo}/perfil.md`.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3. Tipo de Material:**
```
O que precisa?

1. Script SPIN completo (roteiro de call/reunião)
2. Pitch comercial (apresentação curta da oferta)
3. Quebra de objeções (respostas para objeções comuns)
4. Script de WhatsApp (conversa de vendas por mensagem)
5. Playbook completo (tudo acima)

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Material: [tipo escolhido]
Próximo: Produto e preço
---
```

**Bloco 2/3. Produto e Preço:**
```
Qual o produto e a faixa de preço?
(ex: "Mentoria de marketing, R$3.000", "Consultoria de 3 meses, R$5.000")
```

```
--- Bloco 2/3 concluído ---
Material: [tipo]
Produto: [nome] | R$ [valor]
Próximo: Origem do lead
---
```

**Bloco 3/3. Origem do Lead:**
```
Como o lead chega até você?

1. Cadastro em página/isca digital
2. Participou de evento/webinar
3. Indicação de cliente
4. Tráfego direto (anúncio para WhatsApp)
5. Misto

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Material: [tipo]
- Produto: [nome] | R$ [valor]
- Origem do lead: [como chega]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

Monte o conteúdo abaixo **dentro do HTML** (seções com títulos, listas, tabelas). Use `perfil.md` e, se existir, `idconsumidor.md` para personalizar perguntas, objeções e tom.

**Script SPIN (C10X):**

**S. Situação:**
- "Qual é o seu cenário atual com [área]?"
- "Como está seu [tema] hoje?"
- "O que já fez até agora para resolver?"

**P. Problema:**
- "O que está te impedindo de [resultado]?"
- "Qual sua maior dificuldade com [tema]?"

**I. Implicação:**
- "O que acontece se continuar assim por mais 6 meses?"
- "Quanto isso está te custando?"

**N. Necessidade de Solução:**
- "Como seria se você conseguisse [resultado]?"
- "O que mudaria na sua vida/negócio?"

**Fechamento (C10X):**
1. Conexão dor-solução: "Como você me trouxe, sua dificuldade é [DOR]. É exatamente isso que nosso [PRODUTO] resolve."
2. Ancoragem de valor: Compare com alternativas
3. Preço + confirmação: "Tudo isso por [VALOR]. Acessível, né?"
4. Envio do link: "Vou te enviar o checkout. Me confirma a compra que libero seus acessos."

⚠️ Nunca pergunte "quer comprar?". Assuma o interesse.

**Quebra de Objeções:**
- "Preciso pensar" → "O que especificamente precisa pensar? Talvez eu esclareça agora."
- "Está caro" → "Comparado a quê? Quanto está te custando NÃO resolver?"
- "Preciso falar com [pessoa]" → "O que acha que [pessoa] diria?"
- "Não é o momento" → "Quando seria? O que precisa acontecer?"

**Pitch, WhatsApp e playbook completo:** expandir com roteiro linear (pitch) ou mensagens em blocos (WhatsApp) conforme o tipo escolhido na entrevista, sempre no mesmo HTML.

### 4. Salvar (HTML obrigatório)

- Caminho: `meus-produtos/{ativo}/entregas/comercial/playbook-[slug].html`
- `[slug]`: nome do produto em kebab-case (ex.: `mentoria-marketing-digital`).
- Aplicar checklist da skill `playbook-comercial` (CSS embutido, `@media print`, capa, seções, tabelas).

**Para o usuário:** não colar o código HTML no chat. Informar o caminho do arquivo e, em uma linha, como gerar PDF (abrir no navegador, Ctrl+P, Salvar como PDF, retrato).

### 5. Próximo Passo
"Playbook salvo em HTML. Abra no navegador para revisar ou exportar PDF. Use `/estrategia-lancamento` para planejar o evento que vai gerar esses leads, ou `/copy-anuncio` para trazer tráfego."
