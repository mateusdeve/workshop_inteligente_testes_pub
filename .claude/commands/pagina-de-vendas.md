---
name: workshop-marketing:pagina-de-vendas
description: Criar copy completa e/ou página HTML profissional de vendas, captura ou obrigado. Gera texto persuasivo (Light Copy, estrutura 8D) e/ou página com design responsivo baseado na metodologia VTSD.
---

# Página de Vendas — Copy e HTML

Cria a copy completa da página de vendas e/ou a página HTML profissional com estrutura de conversão baseada na metodologia VTSD.

## Usage

```
/pagina-de-vendas
```

---

## O Que Fazer

### 1. Contexto

Leia `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md` se existir.

**VERIFICAÇÃO OBRIGATÓRIA — Tipo do produto:**

Leia `meus-produtos/{ativo}/tipo.md`. Se o arquivo indicar **Low Ticket**, interrompa o fluxo imediatamente e informe:

```
Este comando é para produtos Middle Ticket e High Ticket (estrutura 8D completa).

O Protocolo RECONECTA é um produto Low Ticket — e para Low Ticket, a metodologia
D48 usa um tipo de página diferente, mais direto e sem as seções longas da 8D.

Use o comando correto para este produto:

→ /paginas-low-ticket — gera as 4 copies D48 (Inadequação, Identificação,
  Plug & Play e Promessa Boa Demais) prontas para montar a página de vendas.
```

Não prossiga com nenhuma pergunta nem geração se o produto for Low Ticket.

### 2. Primeira Pergunta — O que criar

```
O que você quer criar?

1. Só a copy (texto completo da página de vendas em markdown)
2. Só a página HTML (usa copy já salva ou gera durante a criação)
3. Copy + página HTML (gera o texto primeiro, depois monta a página)

Digite o número:
```

---

## FLUXO A — Só a Copy

> Ativar quando o usuário escolher a opção 1.

### A1. Entrevista rápida (máximo 2-3 perguntas)

Você já tem `perfil.md` e `idconsumidor.md` com Quadro, Furadeira, Decorados, Urgências Ocultas, Identidades, objeções e pesquisa de mercado. Use TUDO isso para gerar a copy. Pergunte apenas o que NÃO está no perfil:

```
Tem promoção, desconto ou condição especial ativa?
(ex: "Lançamento com 40% de desconto até sexta" — ou "não")
```

```
Tem bônus específicos que quer incluir?
(ex: "Planilha de precificação + script de objeções" — ou "não, pode criar")
```

```
Tem depoimentos reais? Se sim, passe nome e resultado de cada um.
(ex: "Ana, estava cobrando R$30, agora cobra R$120 por leitura" — ou "não tenho")
```

```
Qual o ângulo de entrada da copy?

1. Inadequação — a pessoa está desatualizada ou fazendo errado
2. Identificação — a pessoa se reconhece na dor descrita
3. Plug & Play — a pessoa quer algo pronto para usar
4. Promessa Boa Demais — existe história real com números verificáveis

Digite o número:
```

Confirme antes de gerar:

```
Resumo do que vou criar:
- Produto: [nome do produto]
- Preço: [preço do perfil]
- Ângulo: [ângulo escolhido]
- Bônus: [bônus informados ou "vou criar 3 coerentes"]
- Depoimentos: [reais ou "vou criar modelos para substituir"]

Aviso: vou gerar em 2 partes para garantir qualidade.

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### A2. Princípios de Copy (Light Copy — SEMPRE)

**Princípio central:** A melhor copy não parece copy. Parece alguém inteligente te explicando algo que você nunca tinha entendido.

**As 7 leis da copy:**
1. Ensinar em vez de prometer: a copy entrega conhecimento real. Curiosidade vem do aprendizado, não de promessa vaga
2. Nomear cria realidade: dê nomes próprios para problemas ou soluções. Nome transforma ideia em algo concreto
3. O produto não aparece no lead: nada de "curso", "treinamento", "compre" no início. Só o leitor e a realidade dele
4. Tom de escritor, não de vendedor: escreva como quem explica, não como quem vende. Mostre, não empurre
5. Especificidade mata generalização: use números, datas, valores, situações reais. Quanto mais concreto, mais confiável
6. Informar, não vender: ou você ensina, ou você avisa. Nunca tenta vender diretamente
7. Crie um inimigo concreto (ou cenário inevitável): um culpado externo facilita a aceitação. Pode ser pessoa, sistema ou método antigo

**Vícios proibidos:**
- Não usar travessão (—)
- Não usar estrutura: "Não é X. É Y."
- Não usar frases genéricas de vendedor
- Não mencionar o produto no lead
- Não usar emojis

**Checklist obrigatório — revisar antes de entregar qualquer copy:**

Antes de entregar, revise e substitua:
- Travessão (—) → reescreva a frase sem ele
- Estrutura "Não é X. É Y." → desenvolva o argumento de outra forma
- Frases genéricas de vendedor → substitua por dado ou situação concreta
- Menção ao produto nos primeiros parágrafos → remova ou reescreva focando no leitor
- Emojis → remova sem substituição

- [ ] Nenhum travessão no texto
- [ ] Nenhuma estrutura "Não é X. É Y."
- [ ] Nenhuma frase genérica de vendedor

**Nomear cria realidade:** sempre que possível, criar um nome próprio para o conceito, problema ou solução. Nomes como "Negociação Terapêutica" ou "Programação Emocional Repetitiva" funcionam. "Método Exclusivo" não funciona.

**Parágrafo técnico em itálico:** incluir um parágrafo em itálico que ancora a emoção com razão — explica por que aquilo funciona do ponto de vista científico ou lógico.

Use os 26 elementos literários quando apropriado (consulte skill vtsd-completo para lista completa).

### A3. Geração em 2 Partes

Para garantir qualidade, SEMPRE gere em duas partes separadas.

#### PARTE 1 — Persuasão (Seções 1 a 8)

Gere as seções 1 a 8 completas e salve no arquivo. Cada seção narrativa deve ter parágrafos desenvolvidos com linguagem da persona, cenas do cotidiano e elementos literários.

**Seção 1 — Primeira Dobra (Hero)**
- Headline principal (premissa matadora baseada no Quadro)
- Subheadline (expansão da promessa)
- 3 bullet points (cada um = Urgência Oculta + Decorado)
- Indicação de vídeo de vendas
- Botão de Vendas

**Seção 2 — Paliativo**
- Ferramentas, produtos e soluções concorrentes do mercado que resolvem parcialmente o problema, e por que cada uma não entrega o resultado completo

**Seção 3 — Prova Social**
- 3-6 depoimentos completos (nome, situação antes, resultado depois)
- Se não tiver reais, gere modelos marcados: "[Depoimento modelo — substituir por depoimento real]"

**Seção 4 — Solução (Apresentação do Método)**
- Apresente o produto como a resposta lógica de forma visual
- Mostre a Furadeira: macroetapas + o que cada uma resolve
- Nome do método em destaque
- Mínimo 3 parágrafos

**Seção 5 — Para Quem É**
- Use os baldes de "pra quem é" da identidade do consumidor
- O público se reconhece aqui

**Seção 6 — Entregáveis (Módulos/Conteúdo)**
- Lista completa do que está incluso
- Cada item com nome + descrição de valor (não só o nome)
- Use metáforas de valor para tangibilizar

**Seção 7 — Bônus**
- 3 bônus estratégicos (gere com base no perfil e persona se o aluno não tiver)
- Cada bônus com: nome, descrição completa e valor individual em R$
- Bônus devem resolver objeções ou complementar o produto

**Seção 8 — Stack de Valor (Ancoragem)**
- Liste tudo que está incluso com valor individual
- Some o valor total
- Mostre o preço real como fração do valor total

Ao terminar a Parte 1, salve no arquivo e informe:
"Parte 1 pronta (seções 1 a 8). Gerando a Parte 2 agora..."

#### PARTE 2 — Conversão (Seções 9 a 14)


Continue no mesmo arquivo. Mesmo nível de detalhe da Parte 1.

**Seção 9 — Prova Social**
- 3-6 depoimentos completos (nome, situação antes, resultado depois)
- Se não tiver reais, gere modelos marcados: "[Depoimento modelo — substituir por depoimento real]"

**Seção 10 — Garantia**
- Tipo de garantia (7, 15 ou 30 dias)
- Texto que elimina o risco
- Tom confiante, não defensivo

**Seção 11 — Autoridade do Criador**
- Pequena apresentação do criador do método

**Seção 12 — FAQ**
- 5-8 perguntas frequentes baseadas nas objeções da persona
- Respostas curtas, diretas, que quebram a objeção

**Seção 13 — Último CTA**
- Reforço de urgência ou escassez (se houver)
- Frase de fechamento + botão final

**Seção 14 — Rodapé**
- Indicações de termos de uso e política de privacidade

### A4. Revisão e Correção Automática (OBRIGATÓRIO antes de entregar)

Antes de mostrar a copy ao usuário, aplique a revisão completa da metodologia VTSD.

Leia `.claude/commands/feedback-de-pv.md` e aplique todos os critérios na copy gerada. Depois corrija tudo que estiver fora do padrão:

**Checklist de revisão — corrigir automaticamente cada item:**

- [ ] **Travessão (—)**: encontrou? Reescreva a frase sem ele
- [ ] **"Não é X. É Y."**: encontrou? Desenvolva o argumento de outra forma
- [ ] **Frases genéricas de vendedor**: encontrou? Substitua por dado, situação ou número concreto
- [ ] **Produto mencionado no hero/lead**: encontrou? Remova ou reescreva focando no leitor
- [ ] **Emojis**: encontrou? Remova sem substituição
- [ ] **Headline no imperativo** ("Pare de...", "Aprenda...", "Descubra..."): encontrou? Reescreva como premissa ou observação
- [ ] **Pergunta no gancho**: encontrou? Transforme em afirmação com tensão
- [ ] **Promessa vaga sem dado**: encontrou? Especifique com número, situação real ou nome próprio
- [ ] **Bullets sem padrão urgência oculta + decorado**: encontrou? Reescreva no padrão correto
- [ ] **Ausência de parágrafo técnico em itálico**: ausente? Adicione ao menos um que ancora a emoção com razão

Após a revisão, informe ao usuário:
```
Revisão interna concluída. [X] ajuste(s) aplicado(s) na copy.
```

Só então apresente a copy corrigida e pergunte:
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### A5. Salvar

`meus-produtos/{ativo}/entregas/copy-pagina/copy-[produto].md`

### A6. Próximo Passo

```
Copy completa salva em meus-produtos/{ativo}/entregas/copy-pagina/copy-[produto].md

Quer que eu monte a página HTML agora com essa copy?

1. Sim, montar a página HTML
2. Não agora

Digite o número:
```

Se escolher 1, execute o Fluxo B usando a copy recém-gerada.

---

## FLUXO B — Página HTML

> Ativar quando o usuário escolher a opção 2 ou 3, ou quando aceitar montar a HTML após o Fluxo A.

### B1. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Tipo de Página:**

```
Qual tipo de página?

1. Página de vendas (estrutura 8D completa)
2. Página de captura (coletar email/WhatsApp)
3. Página de obrigado (pós-cadastro ou pós-compra)

Digite o número:
```

**Bloco 2/3 — Detalhes (varia conforme tipo):**

**Se Vendas (8D)** — perguntar UMA por vez:
- Módulos/entregáveis do produto (pode usar perfil.md se já existir)
- Depoimentos (3-5 com nome e resultado, ou "pode criar")
- Garantia (7/15/30 dias)
- Preço e parcelamento
- Bônus (ou "pode criar")
- Link de checkout (ou "ainda não tenho")

Se escolheu **1. Vendas:**
```
Quais os entregáveis do produto? O que está incluso na compra?
(ex: "Planilha principal + guia de preenchimento + tabela de serviços")
```
```
Tem depoimentos de clientes? Se sim, passe nome e resultado de cada um.
(ex: "Ana, estava cobrando R$30, agora cobra R$120 por leitura" — ou "não tenho" para criar placeholders)
```
```
Qual a garantia?

1. 7 dias
2. 15 dias
3. 30 dias
4. Sem garantia

Digite o número:
```
```
Qual o preço?
(ex: "R$37" ou "R$497 ou 12x R$47")
```
```
Tem bônus? Quais?
(ex: "Guia de reajuste de preços, script de objeções" — ou "não" para criar bônus coerentes)
```
```
Link de checkout (Hotmart, Kiwify)?
(ex: "https://pay.hotmart.com/ABC123" ou "ainda não tenho")
```
```
Tem um vídeo de vendas para a primeira dobra?
(ex: "https://www.youtube.com/watch?v=XXXX" — ou "ainda não tenho" para usar placeholder)
```

Se escolheu **2. Captura** ou **3. Obrigado**, verificar ANTES se já existem páginas criadas em `meus-produtos/{ativo}/entregas/paginas/`. Se existirem, perguntar:

```
Encontrei estas páginas já criadas:
[listar arquivos encontrados]

Quer que a nova página siga o mesmo visual (cores, fontes, estilo)?

1. Sim, manter a identidade visual da página existente
2. Não, quero um visual diferente

Digite o número:
```

Se escolher **1**, ler o HTML da página existente para extrair: paleta de cores, fontes, padrões de componentes, estilo de botões e cards. Aplicar a mesma identidade visual na nova página.

Se escolher **2**, seguir o fluxo normal de entrevista visual (Bloco 3/3).

---

Se escolheu **2. Captura:**
```
Qual a isca digital?
(ex: "E-book gratuito", "Aula ao vivo", "Checklist")
```
```
Qual a promessa principal da isca?
(ex: "7 passos para falar inglês em reuniões")
```

Se escolheu **3. Obrigado:**
```
Confirmação de quê?

1. Cadastro em isca digital
2. Compra de produto
3. Inscrição em evento

Digite o número:
```
```
Tem próximo passo para o aluno?
(ex: "Entrar no grupo do WhatsApp", "Acessar a plataforma", "Aguardar email")
```

```
--- Bloco 2/3 concluído ---
Tipo: [tipo]
Detalhes: [resumo dos detalhes]
Próximo: Visual
---
```

**Bloco 3/3 — Visual:**

```
Preferência de cor?

1. Azul (confiança, autoridade)
2. Verde (saúde, resultados)
3. Roxo (marketing, criatividade)
4. Vermelho (urgência, paixão)
5. Rosa (beleza, feminino)
6. Preto/Dourado (premium)
7. Deixa comigo (escolho a ideal para o nicho)

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Tipo: [tipo]
- Produto: [nome]
- Cor: [cor]
- [detalhes específicos]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração — Delegar ao Agente com Progresso Visual

Após a confirmação, **mostrar o progresso ao usuário** e delegar ao agente `construtor-de-paginas`.

**Passo 3a — Exibir mensagem de início com progresso:**

Antes de chamar o agente, enviar esta mensagem ao usuário para que ele acompanhe:

```
Gerando sua página. Acompanhe o progresso:

⬜ Lendo design system e estrutura de seções
⬜ Escrevendo copy das 16 seções (Hero, Dor, Método, Oferta...)
⬜ Montando HTML com CSS, animações e responsivo
⬜ Revisando acentos, grids e checklist de qualidade
⬜ Salvando arquivo final

🔍 Próximo passo: escrever copy das 16 seções e montar o HTML responsivo. Tempo estimado: cerca de 2 minutos.
```

**Passo 3b — Chamar o agente `construtor-de-paginas`** com o brief completo:

```
Crie uma página de [tipo] para o produto "[nome]".

DADOS DO PRODUTO:
[Colar conteúdo relevante de perfil.md — Quadro, Furadeira, Decorados, Urgências Ocultas, Argumentos Incontestáveis]

IDENTIDADE DO CONSUMIDOR:
[Colar conteúdo relevante de idconsumidor.md — quem é, paliativos, objeções, frases]

DETALHES DA PÁGINA:
- Tipo: [vendas/captura/obrigado]
- Módulos: [lista]
- Depoimentos: [fornecidos ou "criar 5 com ultra resultados"]
- Garantia: [dias]
- Preço: [preço e parcelamento]
- Bônus: [fornecidos ou "criar 3-4 estratégicos"]
- Checkout: [link ou #]
- Cor: [paleta com hex codes]
- Fontes: [heading + body]

INSTRUÇÕES DE GERAÇÃO:
1. Ler `skills/paginas/references/design-system-components.md` para padrões CSS prontos
2. Ler `skills/paginas/references/estruturas-pagina.md` para estrutura das seções
3. Ler `skills/paginas/SKILL.md` para regras de qualidade e imagens contextuais
4. Gerar arquivo HTML ÚNICO com todas as seções
5. Salvar em `entregas/paginas/[tipo]-[produto].html`

REGRAS CRÍTICAS (não violar):
- TODOS os textos em português com acentos corretos
- TODAS as fontes sans-serif (serifadas PROIBIDAS)
- Header com logotipo obrigatório
- Cards min-width 320px, padding 28px+, font-size 0.95rem+
- Entregáveis em grid de 2 colunas (NÃO 3)
- Pelo menos 4 tipos de fundo diferentes entre seções
- Pelo menos 2 seções com imagem de fundo
- FAQ com accordion funcional em JS
- CTA flutuante no mobile
- Smooth scroll ativado
- Imagens contextuais (Picsum com seed descritivo, NUNCA genérico)
- NÃO parecer design genérico de IA
```

**IMPORTANTE:** Não gerar a página no chat principal. Delegar 100% ao agente.

### 4. Após o Agente Retornar

Atualizar o progresso e informar ao usuário:

```
Página gerada com sucesso:

✅ Design system e estrutura lidos
✅ Copy das 16 seções escrita
✅ HTML montado com CSS, animações e responsivo
✅ Acentos, grids e checklist revisados
✅ Arquivo salvo

Sua página está em: entregas/paginas/[nome-do-arquivo].html
Abra no navegador para visualizar.
```

### 5. Deploy na Vercel (se configurado)

Verificar se existem `.env` com `VERCEL_TOKEN`, `vercel.json` e `package.json`. Se sim, fazer deploy automático. Se não, perguntar:

```
Quer publicar online?

1. Tenho token da Vercel
2. Não quero deploy agora

Digite o número:
```

Se escolher **2**, informar o caminho do arquivo e ir para o Próximo Passo.

Se escolher **1**, executar o deploy de forma autônoma:

**Passo 1 — Verificar se a conta está conectada:**
```bash
npx vercel whoami
```

**Se retornar erro** (não autenticado):
```
Para publicar, você precisa de uma conta gratuita na Vercel.
São 3 passos — leva menos de 5 minutos:

1. Acesse vercel.com e crie a conta (recomendo entrar com GitHub)
2. Clique no seu avatar → Settings → Tokens → Create Token
   Dê o nome "cursor", clique em Create e copie o token (aparece só uma vez)
3. Cole o token aqui — eu conecto e publico tudo automaticamente
```

Quando o usuário colar o token:
- Salvar em `.env`: `VERCEL_TOKEN=<token>`
- Executar: `npx vercel --token <token> meus-produtos/{ativo}/entregas/paginas --prod --yes --name {slug-do-produto}`

**Se conta conectada:**
```bash
npx vercel meus-produtos/{ativo}/entregas/paginas --prod --yes --name {slug-do-produto}
```

Informar ao usuário:
```
Sua página está online em: https://{slug-do-produto}.vercel.app

[Se usou link do YouTube]: Para o vídeo aparecer, ative a incorporação:
studio.youtube.com → Conteúdo → editar o vídeo → Mais opções → Permitir incorporação → Salvar
```

#### Atualizar a página (nova versão após edições)
```bash
npx vercel meus-produtos/{ativo}/entregas/paginas --prod --yes --name {slug-do-produto}
```

## B4. Revisão e Correção Automática da Copy no HTML (OBRIGATÓRIO antes de salvar)

Antes de salvar o arquivo HTML, percorra todo o texto visível da página e aplique a revisão completa.

Leia `.claude/commands/feedback-de-pv.md` e aplique todos os critérios. Corrija diretamente no HTML:

**Checklist de revisão — corrigir automaticamente cada item:**

- [ ] **Travessão (—)**: encontrou? Reescreva a frase sem ele
- [ ] **"Não é X. É Y."**: encontrou? Desenvolva o argumento de outra forma
- [ ] **Frases genéricas de vendedor**: encontrou? Substitua por dado, situação ou número concreto
- [ ] **Produto mencionado no hero**: encontrou? Remova ou reescreva focando no leitor
- [ ] **Emojis no texto**: encontrou? Remova sem substituição
- [ ] **Headline no imperativo** ("Pare de...", "Aprenda...", "Descubra..."): encontrou? Reescreva como premissa ou observação
- [ ] **Pergunta no gancho**: encontrou? Transforme em afirmação com tensão
- [ ] **Promessa vaga sem dado**: encontrou? Especifique com número, situação real ou nome próprio
- [ ] **Bullets sem padrão urgência oculta + decorado**: encontrou? Reescreva no padrão correto
- [ ] **Ausência de parágrafo técnico em itálico**: ausente? Adicione ao menos um que ancora a emoção com razão

Após a revisão e correção do HTML, informe internamente o número de ajustes e só então prossiga para salvar.

## B5. Inserir Pixel (se configurado)

Leia `.env` e verifique `META_PIXEL_ID`. Se existir, insira o snippet do Facebook Pixel no `<head>`:
- Captura: evento `Lead` no submit
- Vendas: evento `ViewContent` no carregamento
- Obrigado: evento `Purchase` ou `CompleteRegistration`

## B6. Salvar

- `meus-produtos/{ativo}/entregas/paginas/vendas-[produto].html`
- `meus-produtos/{ativo}/entregas/paginas/captura-[produto].html`
- `meus-produtos/{ativo}/entregas/paginas/obrigado-[produto].html`

**SEMPRE** criar também `index.html` como cópia do arquivo gerado na mesma pasta.

## B7. Publicar na Vercel

```
Sua página está salva. Quer publicar online agora para ter um link para compartilhar?

1. Sim, quero publicar
2. Não agora

Digite o número:
```

## B8. Próximo Passo

"Use `/anuncio` para criar anúncios que levem tráfego a essa página."
