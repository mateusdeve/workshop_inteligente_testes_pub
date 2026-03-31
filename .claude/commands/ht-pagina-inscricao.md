---
name: workshop-marketing:ht-pagina-inscricao
description: Criar a copy e página HTML de inscrição para evento C10X — estrutura específica para captação de participantes do Retiro Online ou webinar, diferente da página de vendas 8D.
---

# HT — Página de Inscrição do Evento

Cria a copy e página HTML da página de inscrição do evento high ticket. Estrutura focada em gerar cadastros qualificados, não em vender o produto final.

## Usage

```
/c10x-pagina-inscricao
```

## O Que Fazer

### 1. Contexto
Leia `produtos/.ativo`, depois `produtos/{ativo}/perfil.md` e `produtos/{ativo}/idconsumidor.md`.
Se existir `produtos/{ativo}/entregas/c10x/big-idea-*.md`, leia para usar a promessa e o mote.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4 — Tipo de Inscrição:**
```
O evento é pago ou gratuito?

1. Gratuito (foco em volume de inscritos)
2. Pago com preço simbólico (R$9-47 — filtra comprometimento)
3. Pago com ticket médio (R$97-297 — evento premium)

Digite o número:
```

```
--- Bloco 1/4 concluído ---
Tipo: [gratuito/pago]
Próximo: Dados do evento
---
```

**Bloco 2/4 — Dados do Evento:**
```
Qual o nome, data e duração do evento?
(ex: "Retiro Negócio de Alto Valor — dias 15 e 16 de abril, das 9h às 18h")
```

```
--- Bloco 2/4 concluído ---
Evento: [nome] | [data] | [horário]
Próximo: O que o participante vai aprender
---
```

**Bloco 3/4 — O Que Vai Aprender:**
```
Quais os 3 a 5 resultados concretos que o participante vai alcançar durante o evento?
(ex: "Sair com o posicionamento definido", "Criar a primeira oferta high ticket")
```

```
--- Bloco 3/4 concluído ---
Aprendizados: [lista]
Próximo: Para quem é
---
```

**Bloco 4/4 — Para Quem É:**
```
Para quem é este evento? Descreva o perfil ideal do participante.
(ex: "Especialistas que faturam entre R$5k e R$20k e querem chegar a R$50k")
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Evento: [nome] | [data]
- Tipo: [gratuito/pago]
- Resultados prometidos: [lista]
- Público: [perfil]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

**Copy da Página de Inscrição (estrutura específica para evento):**

**Seção 1 — Headline principal:**
Não é headline de produto — é convite para uma experiência.
Formato: "[MOTE DO EVENTO] — [Subtítulo com data e formato]"

Subheadline: promessa do que vai acontecer nos dias do evento (não o que vai comprar).

**Seção 2 — Para quem é:**
Lista com 3 a 5 perfis do participante ideal.
Cada ponto começa com a situação atual, não com o desejo.
Ex: "Você presta serviço e ainda cobra por hora" — não "Você quer ganhar mais"

**Seção 3 — O que vai aprender (agenda simplificada):**
3 a 5 bullets com os resultados concretos do evento.
Não revela tudo — gera curiosidade sobre o método.

**Seção 4 — Sobre o especialista:**
3 a 5 linhas de credibilidade. Foco em resultados gerados, não em títulos.

**Seção 5 — Formulário de inscrição:**
Campos: Nome completo, WhatsApp, E-mail.
Botão: "Garantir minha vaga" ou "Quero participar"

**Seção 6 — Urgência (se aplicável):**
Vagas limitadas ou data de encerramento das inscrições.

**Regras da copy da página de inscrição:**
- Sem prometer o produto (não citar o que vai ser vendido)
- Foco na experiência e transformação durante o evento
- Linguagem de convite, não de venda
- Tom mais próximo e conversacional que a página 8D

Após gerar a copy, perguntar:

```
Quer que eu também crie a página HTML completa com design profissional?

1. Sim, criar a página HTML
2. Não, só a copy em texto
```

Se sim: criar página HTML responsiva, arquivo único, sem dependências externas, com formulário visual (sem funcionalidade — placeholder para integração).

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
Copy: `produtos/{ativo}/entregas/c10x/copy-inscricao-[evento].md`
HTML: `produtos/{ativo}/entregas/paginas/inscricao-[evento].html`

### 6. Próximo Passo
"Página de inscrição pronta. Próximo: `/ht-anuncios` para criar os anúncios que vão trazer inscritos, ou `/ht-comunicacao-pre` para preparar a comunicação antes do evento."
