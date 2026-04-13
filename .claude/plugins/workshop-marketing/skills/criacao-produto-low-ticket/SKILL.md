---
name: criacao-produto-low-ticket
description: >
  Base de conhecimento para criação do conteúdo real de produtos digitais de entrada (low ticket).
  Cobre 6 formatos: e-book, checklist, mini-curso, desafio, agente GPT e planilha.
  Acionada automaticamente pelo agente estrategista-low-ticket na Etapa 2.
---

# Criação de Produto Low Ticket. Base de Conhecimento

## Regras Gerais (válidas para todos os formatos)

1. **Propor estrutura antes de gerar conteúdo.** Sempre apresente o esqueleto do produto (sumário, abas, dias, módulos) e peça aprovação antes de escrever qualquer conteúdo.
2. **Gerar em blocos, confirmar entre eles.** Para produtos extensos (e-book, mini-curso, desafio), gere e mostre um bloco de cada vez (capítulo, aula, dia) e pergunte antes de continuar.
3. **Nunca mostrar código HTML ao aluno.** Salve silenciosamente e informe apenas o caminho do arquivo.
4. **Só salvar após aprovação final.** Sempre mostrar o conteúdo e perguntar:
   ```
   1. Aprovar e salvar
   2. Quero ajustar algo
   ```
5. **Usar dados do perfil.** Quadro, Furadeira e Urgências Ocultas do `perfil.md` devem guiar o conteúdo gerado. não inventar do zero.
6. **Tom de escrita:** claro, direto, acessível. Mesmo padrão Light Copy do restante do sistema.

---

## Formato 1. E-book / Guia (PDF passo a passo)

**Objetivo:** documento completo que o aluno lê e aplica imediatamente.

### Fluxo

**Passo 1. Sumário**

Com base no Quadro e na Furadeira, proponha:
- Título principal e subtítulo do e-book
- Lista de capítulos (4 a 8), cada um com 1 frase descrevendo o que o leitor aprende/faz nele
- Estimativa de páginas

Mostre e pergunte:
```
1. Aprovar sumário e gerar o conteúdo
2. Quero ajustar o sumário
```

**Passo 2. Conteúdo por capítulo**

Para cada capítulo, gere:
- Título do capítulo
- Introdução (2-3 parágrafos contextualizando o problema que o capítulo resolve)
- Corpo (passo a passo, conceito explicado ou exercício prático)
- Recapitulação em bullets (3-5 pontos)
- Micro CTA de transição para o próximo capítulo

Mostre cada capítulo individualmente e pergunte:
```
1. Aprovar e continuar para o próximo capítulo
2. Quero ajustar algo neste capítulo
```

**Passo 3. Geração do arquivo**

Após todos os capítulos aprovados, gere um HTML com:
- Capa com título, subtítulo e campo "[Seu nome/logo aqui]"
- Sumário com âncoras clicáveis para cada capítulo
- Tipografia otimizada para leitura (fonte sans-serif 16-18px, linha 1.7, margens generosas)
- Rodapé com instruções: "Para salvar como PDF: Ctrl+P → Salvar como PDF → Layout: Retrato"
- Design limpo e profissional (sem excesso de cor, foco em legibilidade)

**Onde salvar:** `entregas/{ativo}/produto/ebook-[slug-produto].html`

---

## Formato 2. Checklist / Roteiro de autoaplicação

**Objetivo:** ferramenta que o aluno usa enquanto executa. não lê depois, usa agora.

### Fluxo

**Passo 1. Estrutura**

Proponha:
- Título do checklist e objetivo em 1 frase
- Número de seções (2 a 5) com nome e quantidade de itens por seção
- Tipo de uso: linear (sequência obrigatória) ou modular (pode usar qualquer seção)

Mostre e pergunte:
```
1. Aprovar estrutura e gerar o checklist
2. Quero ajustar a estrutura
```

**Passo 2. Conteúdo completo**

Gere todos os itens do checklist. Cada item deve ser:
- Escrito como ação concreta no imperativo ("Confirme se...", "Anote o valor de...", "Verifique se...")
- Acompanhado de instrução curta quando o item for ambíguo
- Agrupado por seção com título destacado

**Passo 3. Geração do arquivo**

Gere HTML com:
- Caixas de checagem visíveis (estilo checkbox com CSS)
- Cabeçalho com título, nome do produto e campo "[Seu logo aqui]"
- Seções separadas visualmente
- Instruções de uso no topo ("Como usar este checklist...")
- Layout otimizado para impressão A4 e uso em tela

**Onde salvar:** `entregas/{ativo}/produto/checklist-[slug-produto].html`

---

## Formato 3. Mini-curso (roteiros de aulas)

**Objetivo:** sequência de 3 a 5 aulas curtas (5-15 min cada) que ensinam o método passo a passo.

### Fluxo

**Passo 1. Estrutura do mini-curso**

Proponha:
- Nome do mini-curso
- Número de módulos/aulas (3 a 5)
- Para cada aula: título, objetivo em 1 frase, duração estimada

Mostre e pergunte:
```
1. Aprovar estrutura e gerar os roteiros
2. Quero ajustar a estrutura
```

**Passo 2. Roteiro por aula**

Para cada aula, gere roteiro com:
- **Abertura (30 seg):** o que o aluno vai aprender nesta aula e por que importa
- **Conteúdo principal (blocos):** 2-4 blocos de ensino com explicação + exemplo prático
- **Exercício ou ação prática:** o que o aluno deve fazer após a aula
- **Encerramento (30 seg):** resumo da aula + gancho para a próxima

Mostre roteiro por roteiro. Pergunte entre cada um:
```
1. Aprovar e continuar para a próxima aula
2. Quero ajustar algo neste roteiro
```

**Passo 3. Material de apoio (opcional)**

Após todos os roteiros aprovados, pergunte:
```
Quer que eu gere um material de apoio para o aluno (slides ou apostila resumo)?

1. Sim, gerar material de apoio
2. Não, só os roteiros já bastam
```

Se sim: gere HTML com slides/apostila simples. tópicos de cada aula, espaço para anotações, design clean.

**Onde salvar:**
- Roteiros: `entregas/{ativo}/produto/roteiros-[slug-produto].md`
- Material de apoio (se gerado): `entregas/{ativo}/produto/material-apoio-[slug-produto].html`

---

## Formato 4. Desafio (5 a 7 dias)

**Objetivo:** experiência guiada dia a dia que leva o aluno a um resultado tangível ao final.

### Fluxo

**Passo 1. Estrutura do desafio**

Proponha:
- Nome do desafio
- Duração (5, 6 ou 7 dias)
- Para cada dia: título do dia, tarefa principal e resultado esperado ao final do dia
- Resultado final ao terminar o desafio completo (deve ser o Quadro ou um degrau claro para ele)

Mostre e pergunte:
```
1. Aprovar estrutura e gerar o conteúdo dos dias
2. Quero ajustar a estrutura
```

**Passo 2. Conteúdo por dia**

Para cada dia, gere:
- **Mensagem de boas-vindas do dia** (motivacional, contextualiza o que vem pela frente. 1 parágrafo)
- **Instrução da tarefa** (passo a passo detalhado do que fazer)
- **Dica do dia** (insight prático que facilita a execução)
- **Entregável esperado** (o que o aluno deve ter feito/produzido ao fim do dia)
- **Gancho para o próximo dia** (1 frase que gera antecipação)

Mostre dia a dia e pergunte:
```
1. Aprovar e continuar para o próximo dia
2. Quero ajustar algo neste dia
```

**Passo 3. Geração do arquivo**

Gere HTML como "caderno do desafio" com:
- Capa com nome do desafio e campo "[Seu nome/logo aqui]"
- 1 seção por dia com visual diferenciado (número do dia em destaque)
- Espaço para anotações em cada dia
- Design motivacional (cores energizantes, não sóbrias demais)
- Barra de progresso visual ao longo do desafio

**Onde salvar:** `entregas/{ativo}/produto/desafio-[slug-produto].html`

---

## Formato 5. Agente GPT (assistente de IA personalizado)

**Objetivo:** assistente de IA configurado para ajudar o comprador com o tema do produto, disponível 24h.

### Fluxo

**Passo 1. Escopo do agente**

Proponha:
- Nome do agente (deve soar como um assistente pessoal, não uma ferramenta genérica)
- Função principal em 1 frase (o que ele faz de melhor)
- Tom de voz (formal, descontraído, motivacional, técnico. baseado no público)
- Lista do que o agente FAZ (5-8 capacidades)
- Lista do que o agente NÃO FAZ (3-5 limitações claras)
- 3 exemplos de como o comprador usaria o agente no dia a dia

Mostre e pergunte:
```
1. Aprovar escopo e gerar o prompt
2. Quero ajustar o escopo
```

**Passo 2. Prompt completo**

Gere o prompt de configuração com:
- **Identidade:** quem é o agente, qual seu papel, como se chama
- **Comportamento:** tom de voz, como responde, o que faz e não faz
- **Conhecimento base:** principais conceitos, terminologia do nicho, abordagem preferida
- **Regras absolutas:** o que nunca deve fazer (inventar dados, recomendar substitutos ao produto principal, etc.)
- **Formato de resposta:** como estrutura as respostas (bullets, passo a passo, perguntas de clarificação, etc.)

Mostre e pergunte:
```
1. Aprovar e salvar
2. Quero ajustar algo
```

**Passo 3. Instruções de configuração**

Inclua no arquivo salvo um bloco de instruções:
- Como configurar no ChatGPT (GPTs customizados): passo a passo com imagens textuais
- Como configurar no Claude (Projects): passo a passo
- Sugestão de ícone e nome de exibição

**Onde salvar:** `entregas/{ativo}/produto/agente-gpt-[slug-produto].md`

---

## Formato 6. Planilha (ferramenta de cálculo ou organização)

**Objetivo:** ferramenta prática que o comprador usa repetidamente para resolver um problema específico.

### Fluxo

**Passo 1. Objetivo da planilha**

Pergunte:
```
O que a planilha vai ajudar o usuário a fazer?
(ex: "calcular o lucro de cada receita", "organizar metas semanais", "controlar finanças pessoais")
```

**Passo 2. Estrutura**

Com base no objetivo e no Quadro do produto, proponha:
- Nome da planilha
- Número de abas e nome de cada uma
- Para cada aba: objetivo, colunas principais, quais são de entrada (o usuário preenche) e quais são de resultado (calculadas automaticamente)
- Fórmulas principais que serão usadas (em linguagem simples, não em código)

Mostre e pergunte:
```
1. Aprovar estrutura e gerar a planilha
2. Quero ajustar a estrutura
```

**Passo 3. Geração do arquivo**

Gere HTML com:
- Tabelas funcionais por aba (use `<section>` ou tabs CSS para simular abas)
- **Células de entrada:** fundo amarelo claro `#fffbe6`, label "← preencha aqui"
- **Células de resultado:** fundo verde claro `#f0fff4`, label "← calculado automaticamente"
- **Células de referência/constante:** fundo azul claro `#ebf8ff`
- Instruções de uso no topo de cada aba
- Legenda de cores no cabeçalho da planilha

**Passo 4. Guia para Google Sheets**

No final do arquivo HTML, inclua um bloco colapsável "Como recriar no Google Sheets" com:
- Passo a passo para criar as abas
- Nome exato de cada coluna
- Fórmulas do Google Sheets prontas para copiar e colar em cada célula de resultado
- Dica de formatação (cores, negrito, largura de coluna)

**Onde salvar:** `entregas/{ativo}/produto/planilha-[slug-produto].html`
