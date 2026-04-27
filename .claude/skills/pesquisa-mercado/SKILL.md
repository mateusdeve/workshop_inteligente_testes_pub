---
name: pesquisa-mercado
description: >
  Faz pesquisa de mercado completa e profunda para concepção de qualquer produto.
  Visita Reclame Aqui, SEBRAE, concorrentes, biblioteca de anúncios e fontes do
  nicho para mapear tamanho de mercado, concorrência, precificação, público,
  objeções reais e oportunidades de posicionamento. Acionada OBRIGATORIAMENTE
  em toda concepção de produto (novo, low ticket, middle ticket, high ticket)
  antes de gerar Identidades, Preço e Argumentos Incontestáveis.
---

# Pesquisa de Mercado. Skill Obrigatória na Concepção de Produto

Essa skill é a fonte de inteligência externa do sistema. Quando um produto está sendo concebido, nenhuma sugestão de preço, posicionamento, identidade, argumento incontestável ou oferta pode ser feita "de cabeça". Tudo precisa estar ancorado em dados reais de mercado coletados aqui.

## Quando é acionada

SEMPRE que qualquer fluxo de concepção de produto estiver ativo:

- `/produto-novo` → depois de definir Quadro e Furadeira, antes de Identidades
- `/produto-editar` → no Bloco 3/6 (Identidades e Posicionamento)
- `/lt-funil` e `/lt-criar-produto` → antes de sugerir preço e posicionamento low ticket
- `/ht-big-idea` e `/ht-oferta` → antes de sugerir stack de valor e preço high ticket
- Agentes `estrategista-de-produto`, `estrategista-low-ticket`, `estrategista-middle-ticket`, `estrategista-ht` → como passo obrigatório da fase de concepção

Se a conversa chegar num desses fluxos e a pesquisa ainda não foi feita (ou está desatualizada), o assistente faz a pesquisa antes de continuar. Sem pesquisa, sem sugestão.

## Entrada mínima para começar

Antes de rodar, o assistente precisa ter:

1. **Nicho / tema** do produto (ex: "crochê para iniciantes", "autoestima feminina")
2. **Quadro** (transformação principal) ou pelo menos a promessa inicial
3. **Formato pretendido** (curso, mentoria, ebook, assinatura, etc.) quando já houver

Se faltar algum desses, pergunte ao aluno UMA coisa por vez antes de iniciar.

## O que pesquisar (checklist obrigatório)

A pesquisa tem 9 eixos. Cada um precisa ser coberto. Se um eixo vier vazio, tente uma segunda busca com termos diferentes antes de marcar como "sem dados".

### 1. Tamanho e saúde do mercado
- Estimativa de tamanho do mercado no Brasil (e global, quando fizer sentido)
- Tendência de crescimento dos últimos anos
- Dados do SEBRAE, IBGE, relatórios setoriais, associações do nicho
- Sazonalidade (se existir)

**Fontes a consultar:** SEBRAE (sebrae.com.br), IBGE, Google Trends, relatórios setoriais abertos, associações, publicações de imprensa especializada.

### 2. Concorrentes diretos e indiretos
- Mínimo **10 concorrentes** mapeados (diretos, indiretos e referências aspiracionais)
- Para cada um, coletar: nome, link da oferta/página, promessa principal, entregáveis, bônus, preço, diferencial aparente
- Marcar quais são "top of mind" e quais são aspiracionais

**Fontes:** Hotmart/Kiwify/Eduzz/Braip (produtos públicos), páginas de vendas abertas, Google, YouTube (anúncios e conteúdo), Instagram, Udemy, Coursera quando couber.

### 3. Faixa de preço praticada
- Menor preço, maior preço, faixa mais comum
- Relação entre preço e formato (ebook, mini-curso, curso completo, mentoria, grupo, 1:1)
- Ofertas e parcelamentos típicos do nicho
- Cases de preço "fora da curva" (muito caro ou muito barato) e por quê

### 4. Público-alvo real
- Perfil demográfico (idade, gênero, classe, região) baseado em dados públicos
- Perfil comportamental (o que consome, onde está, como compra)
- Situações de vida típicas que levam a pessoa a procurar esse tipo de produto (renda extra, profissionalização, hobby, etc.)
- Nível de consciência predominante (Schwartz: inconsciente, consciente do problema, da solução, do produto, totalmente consciente)

### 5. Objeções reais no Reclame Aqui
- Buscar reclamações sobre produtos, cursos e serviços similares do nicho
- Mapear **padrões repetidos** de queixa (ex: "prometeram X e não entregaram", "sem suporte", "conteúdo raso")
- Traduzir cada padrão em objeção antecipável para o produto atual
- Mínimo **10 objeções reais** extraídas de reclamações concretas

**Fontes:** reclameaqui.com.br, fóruns (Reddit pt-br, grupos do Facebook quando acessíveis), comentários em vídeos do YouTube do nicho.

### 6. Assuntos quentes e ângulos virais
- Termos de busca em alta no nicho (Google Trends, sugestões automáticas)
- Conteúdos virais recentes (posts, Reels, vídeos do YouTube) com ângulos que ressoam
- Ganchos que estão performando bem em conteúdo orgânico e em anúncios
- Referências de copy que o mercado está usando agora

### 7. YouTube. Top 10 vídeos do nicho
- Mapear os **10 vídeos mais vistos do YouTube** relacionados ao tema/nicho do produto
- Priorizar vídeos com tema diretamente relacionado ao Quadro do produto
- Incluir pelo menos 1 Short se houver algum muito viral no nicho
- Limitar a 2 vídeos por canal para manter diversidade
- Descartar clickbait genérico que não tem relação real com o nicho

Para **cada um dos 10 vídeos**, coletar:
- Título exato
- Canal e número de inscritos
- Link direto do vídeo
- Número de visualizações (aproximado, com data da consulta)
- Data de publicação
- 3 a 5 comentários mais curtidos (com número de likes quando visível)
- Características da thumbnail:
  - Cores dominantes (ex: azul saturado + amarelo, preto + dourado)
  - Expressão facial do apresentador (surpresa, autoridade, espanto, seriedade)
  - Texto em destaque (número grande, palavra gatilho)
  - Elementos visuais (gráficos, dinheiro, setas, ícones, objetos do cotidiano)
  - Composição (close no rosto, cenário, antes e depois)
- Ângulo/gancho da copy do título
- Lacuna: o que o vídeo NÃO aborda e o produto do aluno pode ocupar

**Fontes:** busca direta no YouTube via WebSearch, WebFetch nos links específicos, sites agregadores de estatísticas (youtubers.me, socialblade) como plano B. Se alguma view não puder ser confirmada, marque como "estimada" com a data da consulta.

Ao final dos 10 vídeos, sintetize os **padrões observados**: thumb dominante, gancho de título dominante, dor/desejo dominante nos comentários, lacunas de conteúdo do mercado.

### 8. Biblioteca de Anúncios do Meta (quando possível)
- Anúncios ativos há mais de 30 dias no nicho (alta probabilidade de estar funcionando)
- Anúncios com muitas variações (sinal de iteração e otimização)
- Padrões de headline, gancho, oferta e CTA que se repetem
- Se acesso direto não for possível, use pesquisa web para identificar criativos conhecidos do nicho

### 9. Riscos regulatórios e éticos
- Regras específicas do nicho (CFM para saúde, CVM para finanças, etc.)
- Palavras e promessas que podem dar problema no Meta Ads / Google Ads
- Histórico de processos ou polêmicas conhecidas no nicho

## Como executar (passo a passo)

1. **Confirme os 3 inputs** (nicho, Quadro, formato). Se faltar, pergunte.
2. **Anuncie ao aluno:** "Vou fazer uma pesquisa de mercado completa agora. Isso leva alguns minutos, vou visitar Reclame Aqui, SEBRAE, concorrentes e fontes do nicho."
3. **Execute as buscas em paralelo sempre que possível** usando WebSearch e WebFetch. Agrupe queries por eixo para ganhar velocidade.
4. **Para cada fonte usada, guarde o link.** A tabela final precisa de rastreabilidade.
5. **Se um eixo falhar**, tente uma segunda query com termos alternativos antes de marcar como vazio.
6. **Cross-reference** dados entre fontes. Se duas fontes independentes concordam, marque como "alta confiança". Se só uma fonte diz algo, marque como "baixa confiança".
7. **Monte o relatório** no formato abaixo e salve.

## Formato de entrega (obrigatório)

Salve o relatório em `entregas/{ativo}/pesquisa-mercado.md` com a estrutura abaixo. Também gere PDF em `entregas/{ativo}/pesquisa-mercado.pdf` usando a skill `anthropic-skills:pdf`.

```markdown
# Pesquisa de Mercado. [Nome do Produto / Nicho]

**Data da pesquisa:** [YYYY-MM-DD]
**Nicho:** [nicho]
**Quadro:** [quadro]
**Formato pretendido:** [formato]

## 1. Tamanho e Saúde do Mercado
- Estimativa de tamanho: [valor] ([fonte])
- Tendência: [crescente / estável / em retração] ([fonte])
- Sazonalidade: [descrição ou "sem sazonalidade relevante"]
- Observações: [2 a 4 bullets com dados concretos]

## 2. Concorrentes (mínimo 10)

| Nome | Link | Promessa | Entregáveis | Bônus | Preço | Diferencial aparente |
|------|------|----------|-------------|-------|-------|----------------------|
| ...  | ...  | ...      | ...         | ...   | ...   | ...                  |

## 3. Faixa de Preço
- Menor preço encontrado: R$ [x] ([produto / link])
- Maior preço encontrado: R$ [x] ([produto / link])
- Faixa mais comum: R$ [x] a R$ [y]
- Observação por formato:
  - Ebook / mini-curso: R$ [faixa]
  - Curso completo: R$ [faixa]
  - Mentoria / grupo: R$ [faixa]
  - 1:1 / alto ticket: R$ [faixa]

**Sugestão de preço para este produto:** R$ [valor] a R$ [valor], posicionado como [premium / mid / entrada] porque [raciocínio baseado nos dados acima].

## 4. Público-Alvo Real
- Demografia dominante: [descrição]
- Comportamento: [onde está, como consome, como compra]
- Situações de vida típicas: [3 a 5 bullets]
- Nível de consciência dominante: [Schwartz: nível X. justificativa]

## 5. Objeções Reais (Reclame Aqui e fóruns)

| # | Objeção | Evidência (fonte / trecho) | Como responder no produto |
|---|---------|----------------------------|---------------------------|
| 1 | ... | ... | ... |
| ... |

(Mínimo 10 linhas)

## 6. Assuntos Quentes e Ângulos Virais
- Termos em alta: [lista]
- Conteúdos virais recentes: [3 a 5 exemplos com link e ângulo]
- Ganchos que estão performando: [lista]

## 7. YouTube. Top 10 Vídeos do Nicho

### Vídeo 1
- **Título:** [título exato]
- **Canal:** [nome] ([X milhões de inscritos])
- **Link:** [URL]
- **Visualizações:** [X] (consulta em YYYY-MM-DD)
- **Data de publicação:** [data]
- **Comentários mais curtidos:**
  1. "[comentário]" ([X likes])
  2. "[comentário]" ([X likes])
  3. "[comentário]" ([X likes])
- **Thumbnail:**
  - Cores: [descrição]
  - Expressão: [descrição]
  - Texto em destaque: [texto]
  - Elementos visuais: [descrição]
- **Ângulo do título:** [análise do gancho]
- **Lacuna para o produto:** [o que o vídeo NÃO aborda]

### Vídeo 2
[mesma estrutura]

### Vídeo 3
[mesma estrutura]

### Vídeo 4
[mesma estrutura]

### Vídeo 5
[mesma estrutura]

### Vídeo 6
[mesma estrutura]

### Vídeo 7
[mesma estrutura]

### Vídeo 8
[mesma estrutura]

### Vídeo 9
[mesma estrutura]

### Vídeo 10
[mesma estrutura]

### Padrões Observados nos 10 Vídeos
- **Padrão de thumb dominante:** [cores, expressão e texto que mais se repetem]
- **Padrão de gancho de título dominante:** [estrutura recorrente]
- **Dor/desejo dominante nos comentários:** [análise agregada]
- **Lacunas de conteúdo (o que o mercado NÃO cobre):** [3 a 5 bullets]

## 8. Biblioteca de Anúncios (insights)
- Padrões de headline: [lista]
- Padrões de oferta: [lista]
- Criativos ativos há +30 dias no nicho: [exemplos ou "acesso indireto"]
- Observações: [o que isso sugere para a comunicação do produto]

## 9. Riscos Regulatórios e Éticos
- Regras específicas do nicho: [descrição]
- Palavras/promessas a evitar em anúncio: [lista]
- Histórico de polêmicas: [descrição ou "sem registros relevantes"]

## Síntese Estratégica

### Oportunidades de posicionamento
- [3 a 5 bullets sobre o que o mercado NÃO está fazendo e o produto pode ocupar]

### Diferenciais sugeridos
- [3 a 5 bullets, cada um com justificativa "porque o mercado X"]

### Alertas
- [o que evitar, riscos, armadilhas de precificação ou posicionamento]

### Confiança geral da pesquisa
[Alta / Média / Baixa] - [justificativa: quantidade e qualidade das fontes cruzadas]

## Fontes Consultadas
- [lista de todos os links visitados, agrupados por eixo]
```

## Integração com o resto do sistema

Depois de gerar o relatório, o assistente DEVE:

1. **Cruzar com as Urgências Ocultas já definidas no perfil** (se houver). Objeções e assuntos quentes da pesquisa viram insumo para enriquecer as 7 categorias de Urgências Ocultas.
2. **Usar os dados de preço e posicionamento** para sugerir (não perguntar) o preço e a oferta do produto no fluxo em andamento.
3. **Usar as objeções reais** como base para o bloco de quebra de objeções do `comercial-playbook`, `ht-objecoes`, páginas de vendas (FAQ) e sequências de email.
4. **Usar os ângulos virais e padrões de anúncio** como insumo direto para `copy-anuncio`, `criativo-estatico` e `copy-carrossel`.
4.1. **Usar os 10 vídeos do YouTube** como referência de thumb (`criativo-estatico`), gancho de título (`copy-anuncio`) e dor viva dos comentários (`copy-carrossel`, `comercial-playbook`).
5. **Marcar no perfil.md** que a pesquisa foi feita, com data. Antes de qualquer novo fluxo de concepção, verificar se a pesquisa tem mais de 90 dias. Se tiver, sugerir refazer.

## Regras de qualidade

- **Nunca inventar dado.** Se não encontrou fonte, escreva "sem dados disponíveis" e siga.
- **Todo número tem fonte.** Nenhuma estatística no relatório pode ficar sem link ou referência.
- **Concorrentes têm que ter link real.** Se o link não abriu, marque "link indisponível" ao invés de omitir. **Proibido** preencher com `https://www.google.com/search?q=...`, `https://www.youtube.com/results?search_query=...`, `https://www.bing.com/search?q=...` ou qualquer URL de busca como fallback. URL de busca não é link de concorrente, é mascaramento de dado faltante e quebra todo consumidor downstream do dado (painel, página, copy de comparativo). Quando o link real não foi encontrado, deixe o campo vazio ou "link indisponível" e siga.
- **Objeções têm que ter evidência.** Cada objeção da tabela precisa apontar para uma reclamação real (ou padrão identificado em múltiplas reclamações).
- **Nada de copy-paste grande de fonte externa.** Resumir com palavras próprias. No máximo uma citação curta (menos de 15 palavras) entre aspas quando for crítico.
- **Idioma:** relatório em Português do Brasil, sempre.
- **Proibido travessão (—) em todo o relatório.** Use ponto, dois pontos, parênteses, vírgula.

## O que NÃO fazer

- Não pular a pesquisa porque "o aluno já tem uma ideia". Mesmo com ideia clara, a pesquisa valida ou ajusta.
- Não rodar pesquisa superficial (1 ou 2 buscas). Se os 9 eixos não foram cobertos, a pesquisa não acabou.
- Não aceitar "não encontrei nada" no primeiro try. Tente pelo menos uma segunda query por eixo antes de desistir.
- Não entregar o relatório sem a síntese estratégica. A síntese é o que transforma dado em decisão.
- Não misturar essa skill com a de concepção VTSD. Aqui é pesquisa externa; metodologia interna (Quadro, Furadeira, Decorados) fica em `concepcao-produto`.
