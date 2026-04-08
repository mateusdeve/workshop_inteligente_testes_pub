---
name: workshop-marketing:copy-pagina
description: Criar copy completa e/ou página HTML profissional de vendas, captura ou obrigado. Gera texto persuasivo (Light Copy, estrutura 8D) e/ou página com design responsivo baseado na metodologia VTSD.
---

# Página de Vendas. Copy e HTML

Cria a copy completa da página de vendas e/ou a página HTML profissional com estrutura de conversão baseada na metodologia VTSD.

## Usage

```
/copy-pagina
```

---

## O Que Fazer

### 1. Contexto

Leia `entregas/{ativo}/perfil.md` e `entregas/{ativo}/idconsumidor.md` se existir.

### 2. Primeira Pergunta. O que criar

```
O que você quer criar?

1. Só a copy (texto completo da página de vendas em markdown)
2. Só a página HTML (usa copy já salva ou gera durante a criação)
3. Copy + página HTML (gera o texto primeiro, depois monta a página)

Digite o número:
```

---

## FLUXO A. Só a Copy

> Ativar quando o usuário escolher a opção 1.

### A1. Entrevista rápida (máximo 2-3 perguntas)

Você já tem `perfil.md` e `idconsumidor.md` com Quadro, Furadeira, Decorados, Urgências Ocultas, Identidades, objeções e pesquisa de mercado. Use TUDO isso para gerar a copy. Pergunte apenas o que NÃO está no perfil:

```
Tem promoção, desconto ou condição especial ativa?
(ex: "Lançamento com 40% de desconto até sexta". ou "não")
```

```
Tem bônus específicos que quer incluir?
(ex: "Planilha de precificação + script de objeções". ou "não, pode criar")
```

```
Tem depoimentos reais? Se sim, passe nome e resultado de cada um.
(ex: "Ana, estava cobrando R$30, agora cobra R$120 por leitura". ou "não tenho")
```

```
Qual o ângulo de entrada da copy?

1. Inadequação. a pessoa está desatualizada ou fazendo errado
2. Identificação. a pessoa se reconhece na dor descrita
3. Plug & Play. a pessoa quer algo pronto para usar
4. Promessa Boa Demais. existe história real com números verificáveis

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

### A2. Princípios de Copy (Light Copy. SEMPRE)

**Princípio central:** A melhor copy não parece copy. Parece alguém inteligente te explicando algo que você nunca tinha entendido.

**As 7 leis da copy:**
1. Ensinar em vez de prometer: a copy entrega conhecimento real. Curiosidade vem do aprendizado, não de promessa vaga
2. Nomear cria realidade: dê nomes próprios para problemas ou soluções. Nome transforma ideia em algo concreto
3. O produto não aparece no lead: nada de "curso", "treinamento", "compre", nome do método, nome do produto ou sigla do programa no início. Só o leitor e a realidade dele. O nome do produto/método só aparece a partir da seção Solução/Método. Sem exceção, mesmo que o nome pareça um "posicionamento de identidade".
4. Tom de escritor, não de vendedor: escreva como quem explica, não como quem vende. Mostre, não empurre
5. Especificidade mata generalização: use números, datas, valores, situações reais. Quanto mais concreto, mais confiável
6. Informar, não vender: ou você ensina, ou você avisa. Nunca tenta vender diretamente
7. Crie um inimigo concreto (ou cenário inevitável): um culpado externo facilita a aceitação. Pode ser pessoa, sistema ou método antigo

**Vícios proibidos:**
- Não usar travessão (. )
- Não usar estrutura: "Não é X. É Y."
- Não usar frases genéricas de vendedor
- Não mencionar o produto no lead
- Não usar emojis

**Checklist obrigatório. revisar antes de entregar qualquer copy:**

Antes de entregar, revise e substitua:
- Travessão (. ) → reescreva a frase sem ele
- Estrutura "Não é X. É Y." → desenvolva o argumento de outra forma
- Frases genéricas de vendedor → substitua por dado ou situação concreta
- Menção ao produto nos primeiros parágrafos (inclui nome do produto, nome do método, nome do curso ou sigla) → remova ou reescreva focando no leitor
- Emojis → remova sem substituição

- [ ] Nenhum travessão no texto
- [ ] Nenhuma estrutura "Não é X. É Y."
- [ ] Nenhuma frase genérica de vendedor

**Nomear cria realidade:** sempre que possível, criar um nome próprio para o conceito, problema ou solução. Nomes como "Negociação Terapêutica" ou "Programação Emocional Repetitiva" funcionam. "Método Exclusivo" não funciona.

**Parágrafo técnico em itálico:** incluir um parágrafo em itálico que ancora a emoção com razão. explica por que aquilo funciona do ponto de vista científico ou lógico.

Use os 26 elementos literários quando apropriado (consulte skill vtsd-completo para lista completa).

### A3. Geração em 2 Partes

Para garantir qualidade, SEMPRE gere em duas partes separadas.

#### PARTE 1. Persuasão (Seções 1 a 8)

Gere as seções 1 a 8 completas e salve no arquivo. Cada seção narrativa deve ter parágrafos desenvolvidos com linguagem da persona, cenas do cotidiano e elementos literários.

**Seção 1. Primeira Dobra (Hero)**
- Headline principal (premissa matadora baseada no Quadro)
- Subheadline (expansão da promessa, focada no leitor e na transformação)
- PROIBIDO: nome do produto, nome do método, nome do curso ou sigla na headline ou subheadline. O hero fala APENAS do leitor. Sem exceção, mesmo que o nome pareça "posicionamento de identidade".
- 3 bullet points (cada um = Urgência Oculta + Decorado)
- Indicação de vídeo de vendas
- Botão de Vendas

**Seção 2. Problema/Dor**
- Dor amplificada com cenas do cotidiano do leitor

**Seção 3. Paliativo**
- O que o leitor já tentou e por que falhou

**Seção 4. Prova Social (1o bloco)**
- 2-3 depoimentos curtos de resultado rápido (nome, resultado concreto)
- Objetivo: ancorar credibilidade ANTES de apresentar o método
- Se não tiver reais, gere modelos marcados: "[Depoimento modelo, substituir por depoimento real]"

**Seção 5. Solução (Apresentação do Método)**
- Apresente o produto como a resposta lógica de forma visual
- Mostre a Furadeira: macroetapas + o que cada uma resolve
- Nome do método em destaque (aqui sim, primeira vez que o nome aparece)
- Mínimo 3 parágrafos

**Seção 6. Para Quem É**
- Use os baldes de "pra quem é" da identidade do consumidor
- O público se reconhece aqui

**Seção 7. Entregáveis (Módulos/Conteúdo)**
- Lista completa do que está incluso
- Cada item com nome + descrição de valor (não só o nome)
- Use metáforas de valor para tangibilizar

**Seção 8. Bônus**
- 3 bônus estratégicos (gere com base no perfil e persona se o aluno não tiver)
- Cada bônus com: nome, descrição completa e valor individual em R$
- Bônus devem resolver objeções ou complementar o produto

**Seção 9. Stack de Valor (Ancoragem)**
- Liste tudo que está incluso com valor individual
- Some o valor total
- Mostre o preço real como fração do valor total

Ao terminar a Parte 1, salve no arquivo e informe:
"Parte 1 pronta (seções 1 a 9). Gerando a Parte 2 agora..."

#### PARTE 2. Conversão (Seções 10 a 16)


Continue no mesmo arquivo. Mesmo nível de detalhe da Parte 1.

**Seção 10. Prova Social (2o bloco)**
- 3-5 depoimentos completos (nome, situação antes, resultado depois, foto)
- Agora o leitor já conhece o método e os depoimentos confirmam
- Se não tiver reais, gere modelos marcados: "[Depoimento modelo, substituir por depoimento real]"

**Seção 11. Garantia**
- Tipo de garantia (7, 15 ou 30 dias)
- Texto que elimina o risco
- Tom confiante, não defensivo

**Seção 12. Autoridade do Criador**
- Pequena apresentação do criador do método

**Seção 13. FAQ**
- 5-8 perguntas frequentes baseadas nas objeções da persona
- Respostas curtas, diretas, que quebram a objeção

**Seção 14. Último CTA**
- Reforço de urgência ou escassez (se houver)
- Frase de fechamento + botão final

**Seção 15. Rodapé**
- Indicações de termos de uso e política de privacidade

### A4. Revisão e Correção Automática (OBRIGATÓRIO antes de entregar)

Antes de mostrar a copy ao usuário, aplique a revisão completa da metodologia VTSD.

Leia `.claude/commands/feedback-pagina.md` e aplique todos os critérios na copy gerada. Depois corrija tudo que estiver fora do padrão:

**Checklist de revisão. corrigir automaticamente cada item:**

- [ ] **Travessão (. )**: encontrou? Reescreva a frase sem ele
- [ ] **"Não é X. É Y."**: encontrou? Desenvolva o argumento de outra forma
- [ ] **Frases genéricas de vendedor**: encontrou? Substitua por dado, situação ou número concreto
- [ ] **Produto mencionado no hero/lead**: encontrou o nome do produto, nome do método, nome do curso ou sigla na headline ou subheadline? Remova. O hero fala só do leitor e da transformação. O nome do produto/método só aparece a partir da seção Solução/Método. Sem exceção, mesmo que pareça "posicionamento de identidade".
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

`entregas/{ativo}/copy-pagina/copy-[produto].md`

### A6. Próximo Passo

```
Copy completa salva em entregas/{ativo}/copy-pagina/copy-[produto].md

Quer que eu monte a página HTML agora com essa copy?

1. Sim, montar a página HTML
2. Não agora

Digite o número:
```

Se escolher 1, execute o Fluxo B usando a copy recém-gerada.

---

## FLUXO B. Página HTML

> Ativar quando o usuário escolher a opção 2 ou 3, ou quando aceitar montar a HTML após o Fluxo A.

### B1. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3. Tipo de Página:**

```
Qual tipo de página?

1. Página de vendas (estrutura 8D completa)
2. Página de captura (coletar email/WhatsApp)
3. Página de obrigado (pós-cadastro ou pós-compra)

Digite o número:
```

**Bloco 2/3. Detalhes (varia conforme tipo):**

**Se Vendas (8D)**. perguntar UMA por vez:
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
(ex: "Ana, estava cobrando R$30, agora cobra R$120 por leitura". ou "não tenho" para criar placeholders)
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
(ex: "Guia de reajuste de preços, script de objeções". ou "não" para criar bônus coerentes)
```
```
Link de checkout (Hotmart, Kiwify)?
(ex: "https://pay.hotmart.com/ABC123" ou "ainda não tenho")
```
```
Tem um vídeo de vendas para a primeira dobra?
(ex: "https://www.youtube.com/watch?v=XXXX". ou "ainda não tenho" para usar placeholder)
```

Se escolheu **2. Captura** ou **3. Obrigado**, verificar ANTES se já existem páginas criadas em `entregas/{ativo}/paginas/`. Se existirem, perguntar:

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

**Bloco 3/3. Visual:**

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

### 3. Geração SEÇÃO POR SEÇÃO com Aprovação por Bloco

> ⛔ NUNCA gere a página inteira de uma vez. O fluxo é seção por seção, com aprovação do usuário entre cada uma. Isso é obrigatório (decisão Vitor 31/03/2026: gerar tudo junto demora 10+ minutos e o usuário fica sem controle. Seção por seção é mais dinâmico, mais rápido perceptualmente e o aluno pode ajustar antes de propagar erro para o resto da página).

**Como funciona:**
- A página é montada incrementalmente em `entregas/{ativo}/paginas/[tipo]-[produto].html`
- A cada seção: lê APENAS o template daquela seção, gera o HTML daquela seção, salva o arquivo parcial, mostra progresso visual ao usuário e pede aprovação
- Após aprovação, segue para a próxima seção. Se o usuário pedir ajuste, regera SÓ aquela seção.
- No final, todas as seções já estão montadas e o arquivo está pronto.

**Sequência das 13 seções da estrutura 8D (em ordem de geração):**

| # | Seção | Template lido |
|---|---|---|
| 1 | Primeira Dobra (Hero) | `hero_{estilo}` ou variante |
| 2 | Problema/Dor | `dor_{estilo}` |
| 3 | Paliativo | `paliativo_{estilo}` |
| 4 | Provas Sociais (1º bloco) | `provas_sociais_{estilo}` |
| 5 | Solução/Método (Furadeira) | `metodo_{estilo}` |
| 6 | Entregáveis | `entregaveis_{estilo}` |
| 7 | Bônus | `bonus_{estilo}` |
| 8 | Garantia | `garantia_{estilo}` |
| 9 | Provas Sociais (2º bloco) | `provas_sociais_{estilo}` (variação) |
| 10 | Autoridade do Criador | `autoridade_{estilo}` |
| 11 | Suporte | `suporte_{estilo}` |
| 12 | Oferta Final (Stack + Preço + CTA) | `oferta_final_{estilo}` |
| 13 | FAQ | `faq_{estilo}` |

**Passo 3a. Setup inicial (antes da primeira seção):**

1. Determinar o estilo único da página pela tabela de nicho em `skills/paginas/SKILL.md` (Etapa 1 do Fluxo de Geração)
2. Criar o esqueleto do arquivo HTML em `entregas/{ativo}/paginas/[tipo]-[produto].html` com:
   - `<!DOCTYPE html>`, `<head>` com fontes do nicho, Material Symbols, meta tags
   - `:root` com tokens mestres do estilo (`--radius`, `--border-width`, `--shadow`, paleta, tipografia)
   - `<body>` vazio com header (logotipo) e placeholder `<main id="page-sections"></main>`
3. Anunciar ao usuário:
   ```
   Vou montar sua página seção por seção. Você aprova cada uma antes da próxima.
   Estilo escolhido para o nicho [nicho]: [estilo]
   Total: 13 seções. Vamos lá.
   ```

**Passo 3b. Loop. Para CADA seção (1 a 13):**

**3b.1. Anunciar progresso visual:**
```
[Seção N/13] Gerando: [nome da seção]

Progresso geral:
[██████░░░░░░░] N de 13
```

**3b.2. Ler APENAS o template daquela seção:**
- `references/templates/{secao}_{estilo}/code.html`
- NÃO ler templates de outras seções. Otimização crítica para evitar os 10 minutos por página.

**3b.3. Gerar o HTML da seção** seguindo Etapas 4-5 do Fluxo de Geração do SKILL.md (extrair tokens, copiar estrutura, adaptar copy/cores/imagens). Aplicar varredura anti-vícios da Etapa 0 do SKILL.md ANTES de salvar.

**3b.4. Salvar parcialmente:** inserir o HTML da seção no `<main id="page-sections">` do arquivo, mantendo o que já estava. Salvar o arquivo a cada seção (snapshot incremental).

**3b.5. NÃO mostrar código no chat.** Apresentar ao usuário um resumo curto da seção em texto:
```
Seção [N/13] pronta: [Nome da seção]

Headline: "[primeira frase ou título principal]"
Conteúdo: [resumo de 1 a 2 linhas do que essa seção contém]

Arquivo atualizado em: entregas/{ativo}/paginas/[arquivo].html
Abra/recarregue no navegador para ver visualmente.

1. Aprovar e ir para a próxima seção
2. Quero ajustar essa seção
```

**3b.6. Tratar a resposta:**
- **Se "1. Aprovar"**: ir para a próxima seção do loop.
- **Se "2. Ajustar"**: perguntar O QUE ajustar (texto, cor, layout, foto, ordem dos elementos), regerar APENAS aquela seção, sobrescrever no arquivo parcial e voltar ao 3b.5.
- O usuário também pode digitar "ir direto à versão final" ou "não precisa aprovar mais" para pular as aprovações restantes e gerar tudo até o fim sem pausa. Nesse caso, continuar o loop até a seção 13 sem perguntar mais.

**Passo 3c. Após a seção 13 aprovada:**
- Rodar o Checklist final do SKILL.md (estilo único, tokens consistentes, sem vícios proibidos, acentos corretos, grid 2 colunas, fontes sans-serif)
- Confirmar que `<head>` e `<body>` estão fechados corretamente
- Confirmar que o arquivo abre limpo no navegador

### 4. Confirmação Final

Após as 13 seções aprovadas e checklist passado:

```
Página completa pronta.

✅ 13 seções aprovadas uma a uma
✅ Estilo [estilo] aplicado do início ao fim
✅ Tokens mestres consistentes em todas as seções
✅ Acentos, grids, fontes e checklist anti-vícios revisados

Arquivo final: entregas/{ativo}/paginas/[tipo]-[produto].html
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

**Passo 1. Verificar se a conta está conectada:**
```bash
npx vercel whoami
```

**Se retornar erro** (não autenticado):
```
Para publicar, você precisa de uma conta gratuita na Vercel.
São 3 passos. leva menos de 5 minutos:

1. Acesse vercel.com e crie a conta (recomendo entrar com GitHub)
2. Clique no seu avatar → Settings → Tokens → Create Token
   Dê o nome "cursor", clique em Create e copie o token (aparece só uma vez)
3. Cole o token aqui. eu conecto e publico tudo automaticamente
```

Quando o usuário colar o token:
- Salvar em `.env`: `VERCEL_TOKEN=<token>`
- Executar: `npx vercel --token <token> entregas/{ativo}/paginas --prod --yes --name {slug-do-produto}`

**Se conta conectada:**
```bash
npx vercel entregas/{ativo}/paginas --prod --yes --name {slug-do-produto}
```

Informar ao usuário:
```
Sua página está online em: https://{slug-do-produto}.vercel.app

[Se usou link do YouTube]: Para o vídeo aparecer, ative a incorporação:
studio.youtube.com → Conteúdo → editar o vídeo → Mais opções → Permitir incorporação → Salvar
```

#### Atualizar a página (nova versão após edições)
```bash
npx vercel entregas/{ativo}/paginas --prod --yes --name {slug-do-produto}
```

## B4. Revisão e Correção Automática da Copy no HTML (OBRIGATÓRIO antes de salvar)

Antes de salvar o arquivo HTML, percorra todo o texto visível da página e aplique a revisão completa.

Leia `.claude/commands/feedback-pagina.md` e aplique todos os critérios. Corrija diretamente no HTML:

**Checklist de revisão. corrigir automaticamente cada item:**

- [ ] **Travessão (. )**: encontrou? Reescreva a frase sem ele
- [ ] **"Não é X. É Y."**: encontrou? Desenvolva o argumento de outra forma
- [ ] **Frases genéricas de vendedor**: encontrou? Substitua por dado, situação ou número concreto
- [ ] **Produto mencionado no hero**: encontrou o nome do produto, nome do método, nome do curso ou sigla na headline ou subheadline? Remova. O hero fala só do leitor. O nome só aparece a partir da seção Solução/Método.
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

- `entregas/{ativo}/paginas/vendas-[produto].html`
- `entregas/{ativo}/paginas/captura-[produto].html`
- `entregas/{ativo}/paginas/obrigado-[produto].html`

**SEMPRE** criar também `index.html` como cópia do arquivo gerado na mesma pasta.

## B7. Publicar na Vercel

```
Sua página está salva. Quer publicar online agora para ter um link para compartilhar?

1. Sim, quero publicar
2. Não agora

Digite o número:
```

## B8. Próximo Passo

"Use `/copy-anuncio` para criar anúncios que levem tráfego a essa página."
