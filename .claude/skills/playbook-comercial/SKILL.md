---
name: playbook-comercial
description: >
  Base de conhecimento para gerar o playbook comercial completo de um produto
  middle ou low ticket, focado em venda 1:1 por WhatsApp. Cobre abordagem ativa
  (outbound), abordagem receptiva (inbound), recuperação de carrinho, follow-up
  e quebra de objeções pelo Framework dos 7 Argumentos, com identidade do
  produto, do consumidor e do comunicador. Entregável final: HTML único de 13
  seções, bem formatado, pronto para impressão e exportação em PDF. Acionada
  pelo command /comercial-playbook.
---

# Playbook Comercial. Venda 1:1 por WhatsApp (Middle e Low Ticket)

## Princípio da skill

Esta skill gera **um único entregável**: o playbook comercial completo de venda 1:1 por WhatsApp para produtos middle ou low ticket.

**Escopo exclusivo de WhatsApp 1:1:**

1. **Abordagem ativa (outbound).** O vendedor dá o primeiro passo. Lead frio (nunca interagiu) ou morno (seguidor, consumidor de conteúdo, participou de lista).
2. **Abordagem receptiva (inbound).** Lead chega pelo próprio canal (anúncio, orgânico, link da bio, página de captura, palavra-chave).
3. **Recuperação de carrinho.** Lead chegou ao checkout e não finalizou. Resgate com mensagens temporizadas.

Fora de escopo: call de venda presencial ou por vídeo, venda high ticket (C10X), pitch de palco, proposta formal de consultoria. Para esses, ver `/ht-*`.

A skill **não gera** pitch isolado, só objeções, só WhatsApp receptivo, só recuperação. Sempre o playbook completo, com todas as seções, em um HTML único.

O playbook tem **dois públicos simultâneos:**

1. **Time comercial que não conhece o produto.** Precisa aprender o Quadro, a Furadeira, a identidade do consumidor e a voz do comunicador dentro do próprio documento. Por isso as três identidades aparecem completas nas primeiras seções.
2. **Produtor que atende o WhatsApp.** Já conhece o produto, mas precisa de mensagens prontas para copiar e colar, fluxos de atendimento e respostas para objeções na ponta da língua. Por isso os blocos de abordagem, recuperação, fechamento e objeções ficam em cards com variações prontas.

A skill **não pergunta ao usuário** dados que já existem nos arquivos do produto (nome, preço, Quadro, dor, objeções, tom). Ela lê tudo automaticamente. A única pergunta possível é **qual produto usar**, e só quando existe mais de um produto cadastrado em `meus-produtos/`. Se só há um produto cadastrado, a skill segue direto para a geração.

## Leitura obrigatória de contexto

Antes de gerar qualquer trecho do playbook, leia nesta ordem:

1. `meus-produtos/.ativo`. Identificador do produto ativo.
2. Listagem de `meus-produtos/`. Descobrir quantos produtos têm `perfil.md`.
3. `meus-produtos/{produto}/perfil.md`. Obrigatório. Sem ele, aborte e oriente rodar `/produto-concepcao`. Contém Quadro, Furadeira (macroetapas e microetapas), Decorados (50 benefícios em 5 categorias), Urgências Ocultas (7 categorias × 10 itens = 70 itens), 3 Identidades (Produto, Consumidor, Comunicador), Argumentos Incontestáveis, preço e diferenciais.
4. `meus-produtos/{produto}/idconsumidor.md`. **Obrigatório para este comando.** Contém as 5 objeções com as 7 quebras de 2 parágrafos cada (Framework dos 7 Argumentos), paliativos, frases do público, tom de comunicação e baldes de para quem é. Sem ele, aborte e oriente rodar `/produto-concepcao` (gera a identidade do consumidor automaticamente ao final do fluxo).
5. `meus-produtos/{produto}/painel-entregas.html`. Se existir. Fonte visual de referência com os mesmos dados organizados.
6. Arquivos complementares do produto em `meus-produtos/{produto}/entregas/*` (páginas, concepção, estratégia). Leitura leve, só para capturar linguagem e argumentos já aprovados.

## Voz do comunicador como régua de escrita

Todo texto do playbook é escrito na voz da **Identidade do Comunicador** do `perfil.md`:

- Tom de voz (parágrafo descritivo do comunicador)
- Palavras que conectam (usar sempre que couber)
- Palavras que afastam (nunca usar no playbook)
- Estilo de frase do comunicador (frases curtas ou longas, linguagem técnica ou coloquial, uso de metáforas próprias do nicho)

Antes de escrever qualquer seção, releia o bloco de Identidade do Comunicador e aplique como filtro. O playbook não é neutro: soa como o comunicador conversando no WhatsApp com o lead.

## Abordagem Ativa. Outbound WhatsApp

Fluxo para quando o vendedor dá o primeiro passo com um lead frio ou morno (lista de seguidores, contato que baixou material, aluno de produto anterior, indicação).

O playbook entrega a sequência em **7 blocos**, cada bloco com **3 variações de mensagem** prontas para copiar e colar, adaptadas ao nicho e à voz do comunicador:

1. **Primeiro contato.** Quebra-gelo mais motivo de ter escrito. Sem vender. Curto.
2. **Qualificação leve.** 1 ou 2 perguntas sobre o momento atual do lead (usa vocabulário do nicho).
3. **Amarrar a dor.** Uma Urgência Oculta relevante devolvida em forma de pergunta aberta.
4. **Oferecer ajuda concreta.** Conteúdo, troca de experiência, ou convite para responder uma dúvida específica. Não vende ainda.
5. **Convite para conversa real.** Chamar para falar do problema específico do lead.
6. **Transição para diagnóstico.** Quando o lead engajou, entra no SPIN curto adaptado ao WhatsApp.
7. **Encerramento se não engajou.** Fechar educadamente, deixar porta aberta, marcar para follow-up.

Cada bloco inclui **nota de condução**: o que observar na resposta, quando avançar, quando parar.

## Abordagem Receptiva. Inbound WhatsApp

Fluxo para quando o lead chega (anúncio, orgânico, link da bio, link da página, palavra-chave). Entra no WhatsApp perguntando algo ou mandando a palavra-chave.

O playbook entrega a sequência em **6 blocos**, cada bloco com **3 variações de mensagem** prontas para copiar e colar:

1. **Acolhimento imediato.** Resposta rápida, confirma o interesse, chama pelo nome.
2. **Pergunta de posicionamento.** Descobre nível de consciência do lead (o que ele viu, por que chegou ali, o que já tentou).
3. **Diagnóstico rápido.** 3 a 5 perguntas curtas no estilo SPIN adaptado ao WhatsApp.
4. **Apresentação conectada.** Explica a solução amarrando às respostas do lead (usa as palavras que ele mesmo usou).
5. **Prova mais preço.** 1 caso real (nome fictício mais situação mais resultado) mais revelação de valor no tom certo.
6. **Checkout mais confirmação.** Envia o link e pede confirmação de compra com pressuposto do sim.

Cada bloco inclui **nota de condução** com sinais de compra e de desengajamento.

## Recuperação de Carrinho

Fluxo para o lead que entrou no checkout e não finalizou. Recuperação é temporizada e assume várias razões de abandono (distração, dúvida pontual, comparação, objeção de preço, falta do cartão em mãos).

O playbook entrega **7 toques** temporizados, cada toque com **2 variações** (uma mais leve, uma mais direta):

1. **15 minutos após abandono.** Tom de ajuda, nada comercial ("tudo certo com a finalização?").
2. **1 hora.** Quebra da primeira objeção provável (preço ou segurança), no texto.
3. **4 horas.** Prova social curta (1 caso real) mais novo link.
4. **D+1 manhã.** Nova angulação usando uma Urgência Oculta diferente.
5. **D+1 noite.** Frase de escassez real (bônus, condição ou vaga).
6. **D+3.** Última chamada educada, com foco na consequência de adiar.
7. **D+7.** Encerramento respeitoso mais oferta de downsell se houver.

Cada toque respeita os 7 princípios de WhatsApp e usa a voz do comunicador.

## SPIN adaptado ao WhatsApp

O SPIN via WhatsApp é curto. Nunca 40 perguntas como em call. São **24 perguntas totais, 6 por fase**, mais diretas, adaptadas ao ritmo da troca de mensagem:

**S. Situação (6 perguntas):** mapear o cenário atual do lead (rotina, ferramentas, tentativas anteriores, momento de vida).
**P. Problema (6 perguntas):** trazer a dor central à tona com vocabulário e situações específicas do nicho.
**I. Implicação (6 perguntas):** amplificar o custo de não resolver (financeiro, emocional, tempo, reputação, saúde).
**N. Necessidade de Solução (6 perguntas):** construir a visão do resultado ideal conectada ao Quadro do produto.

Proibido perguntas genéricas tipo "como está sua área hoje?" ou "qual sua maior dificuldade?". Cada pergunta cita vocabulário, situações, rotinas e paliativos concretos que o consumidor específico vive.

Cada fase inclui **nota de condução**: o que observar nas respostas, quando avançar, quando repetir em outra angulação.

## Apresentação mais ancoragem de preço por texto

Versão da apresentação e da ancoragem adaptada para mensagem escrita:

- **Ponte dor-solução em 2 mensagens curtas** usando as palavras do próprio lead.
- **Descrição objetiva do produto em 3 a 4 mensagens** (o que é, como funciona, o que a pessoa faz semana a semana).
- **Prova em 3 formatos curtos:** caso real (nome fictício mais situação mais resultado), número agregado, depoimento de 1 linha.
- **Conexão da Furadeira com o Quadro em 1 mensagem** (trilha resumida).
- **Revelação de preço em 4 mensagens** na sequência: alta (valor total dos entregáveis somados), funcional (o que custa hoje a dor continuar), revelação do preço real, confirmação ("faz sentido pra você?").
- **Comparação com paliativos** (concorrentes diretos e indiretos do `idconsumidor.md`) em 1 ou 2 mensagens curtas.

Todo o bloco segue a voz do comunicador.

## Fechamento em 4 passos (versão WhatsApp)

1. Conexão dor-solução: "[Nome], sua dificuldade é [DOR]. É exatamente isso que [PRODUTO] resolve. Em [TEMPO] você consegue [TRANSFORMAÇÃO]."
2. Ancoragem de valor: compare com alternativas reais em 1 ou 2 mensagens curtas.
3. Preço mais confirmação: "Tudo isso por [VALOR]. Faz sentido pra você?"
4. Envio do link: "Vou te mandar o checkout agora. Me confirma a compra que já libero seus acessos."

Proibido perguntar "quer comprar?". Assuma o interesse.

## Quebra de objeções pelo Framework dos 7 Argumentos

O playbook extrai as **5 objeções** (até 7 se houver) do `idconsumidor.md`, cada uma com as 7 quebras completas de 2 parágrafos cada, na ordem fixa:

1. Argumento Incontestável (dado concreto mais fonte)
2. Argumento Lógico (causa e efeito)
3. Argumento por Analogia (sem celebridades, situações reais do público)
4. Argumento por Exemplificação (caso real com nome fictício)
5. Argumento de Valor (custo vs. benefício)
6. Argumento de Consequência (agir vs. adiar)
7. Argumento de Contradição (refutação de incoerências)

**Adaptação para WhatsApp:** ao lado da versão completa (2 parágrafos, bom para estudo do time e para áudio), cada argumento vem com uma **versão curta de 1 a 2 mensagens** pronta para copiar e colar na conversa.

Layout visual: uma objeção por accordion (fechado por padrão). No topo da seção, tabela-resumo com uma linha por objeção apontando o argumento mais forte, para o vendedor bater o olho no celular e escolher o ataque.

Nunca reescrever as quebras do `idconsumidor.md`. A versão curta é um recorte da versão completa, nunca um texto novo. Se o texto salvo estiver incompleto, orientar rodar `/produto-concepcao` de novo (e regenerar a identidade do consumidor no fluxo) antes de gerar o playbook.

## Follow-up de quem não comprou

Sequência para leads que passaram pela abordagem ativa ou receptiva, conversaram, e não fecharam (sem chegar ao checkout). Diferente da recuperação de carrinho (que trata de lead que já estava a um clique de comprar).

Estrutura em **3 tempos, 2 mensagens por tempo:**

1. **D+1.** Lembrete leve mais prova social curta.
2. **D+3.** Nova angulação com Urgência Oculta diferente mais quebra de uma objeção específica.
3. **D+7.** Última chamada com escassez real mais oferta de downsell se houver.

Todas as mensagens seguem os 7 princípios de WhatsApp e a voz do comunicador.

## Upsell, Downsell e Order Bump

**Upsell.** Oferta complementar pós-compra, enviada por WhatsApp em até 48 horas do fechamento (acelera resultado).
**Downsell.** Oferta menor para quem não comprou, enviada no D+7 ou após recusa explícita de preço (mantém relacionamento).
**Order Bump.** Complemento no próprio checkout (impulso, preço baixo).

Para cada um, sugerir valores, formatos e frase pronta de oferta em mensagem de WhatsApp compatível com a faixa de preço do produto.

## Estrutura completa do playbook

Todo playbook gerado por esta skill contém, **na ordem**, as 13 seções abaixo:

1. **Capa interna** (produto, valor em destaque, objetivo: vender 1:1 por WhatsApp, linha "Como usar este playbook" com caminhos para time e produtor)
2. **Identidade do Produto** (Quadro, Furadeira em trilha visual, entregáveis, diferenciais, Argumentos Incontestáveis, posicionamento)
3. **Identidade do Consumidor** (frase "Para quem é", perfil demográfico, dores, desejos, paliativos, 10 frases que o consumidor diria)
4. **Identidade do Comunicador** (tom, posicionamento, palavras que conectam, palavras que afastam, exemplo de frase no tom certo vs. errado)
5. **Abordagem Ativa. Outbound WhatsApp** (7 blocos, 3 variações de mensagem por bloco, notas de condução)
6. **Abordagem Receptiva. Inbound WhatsApp** (6 blocos, 3 variações de mensagem por bloco, notas de condução)
7. **SPIN adaptado ao WhatsApp** (6 perguntas por fase mais nota de condução, total 24 perguntas)
8. **Apresentação mais ancoragem de preço por texto** (sequência de mensagens pronta para copiar e colar)
9. **Fechamento em 4 passos (WhatsApp)**
10. **Quebra de objeções pelo Framework dos 7 Argumentos** (5 a 7 objeções, versão curta e completa, tabela-resumo no topo, accordions)
11. **Recuperação de Carrinho** (7 toques temporizados, 2 variações por toque)
12. **Follow-up de quem não comprou** (D+1, D+3, D+7, 2 mensagens por tempo) mais **Upsell, Downsell e Order Bump**
13. **Checklist de atendimento no WhatsApp** (antes de abrir a conversa, durante a conversa, depois do fechamento ou recusa)

## Entregável final obrigatório: HTML (PDF pelo navegador)

O produto que o aluno guarda e compartilha **não** é Markdown. É **um arquivo HTML único** salvo em `meus-produtos/{produto}/entregas/comercial/playbook-[slug].html` (slug derivado do nome do produto, kebab-case, sem acentos problemáticos no nome do arquivo).

### Requisitos do HTML

1. **Arquivo único:** todo o CSS em `<style>` no `<head>`. Sem dependências externas obrigatórias. Opcional: uma fonte do Google Fonts (DM Sans, Source Sans 3 ou Inter) via link, aceitável para PDF.
2. **Linguagem e acessibilidade:** `<html lang="pt-BR">`, `<meta charset="utf-8">`, `<meta name="viewport" ...>`, `<title>` descritivo (ex: "Playbook comercial WhatsApp · Nome do produto").
3. **Tipografia e layout:** largura máxima legível (720px a 840px centralizada), hierarquia clara de `h1` a `h3`, espaçamento confortável, contraste adequado. Tabelas com bordas leves ou zebrado sutil. Nunca depender só de cor para significado.
4. **Índice clicável no topo:** logo após a capa, índice com 13 links âncora para as seções, formato lista numerada, font-size 13px, cada link rolando até a seção correspondente. Essencial para consulta rápida no celular.
5. **Conteúdo:** incluir **todas** as 13 seções listadas em "Estrutura completa do playbook". Texto contextualizado com `perfil.md` (Quadro, oferta, preço) e com `idconsumidor.md` (objeções, frases, tom).
6. **Elementos visuais obrigatórios por seção:**
   - **Capa:** card grande com valor do curso em destaque (font-size 28px a 36px, weight 700) e selo "Venda 1:1 por WhatsApp".
   - **Identidade do Produto. Furadeira em duas representações (obrigatórias as duas):**
     - **Furadeira visual.** Diagrama horizontal (vertical no mobile) com as macroetapas em caixas conectadas por setas (`etapa 1 → etapa 2 → etapa 3 ...`). Cada caixa tem círculo numerado, prazo da etapa, nome da macroetapa e um resumo curto (máx. 2 linhas). Abaixo do diagrama, uma linha destacada com o destino final (o Quadro em 1 frase). Esta é a "vitrine" que o time comercial consegue enxergar em 5 segundos.
     - **Furadeira escrita.** Trilha numerada detalhada (step timeline com círculos numerados conectados por linha vertical), com macroetapa, prazo e **texto completo das microetapas** em cada passo. Esta é a referência de consulta que o produtor usa quando precisa explicar o método com profundidade no WhatsApp.
     Ordem obrigatória na página: subtítulo "Visão visual das 3 macroetapas" com o diagrama, depois subtítulo "Detalhamento escrito das macro e microetapas" com a trilha completa. Nunca entregar só uma das duas.
   - **Identidade do Comunicador:** pills coloridas verdes para palavras que conectam, pills rosas para palavras que afastam.
   - **Abordagem Ativa e Receptiva:** cada bloco com 3 variações em **formato de bolha de mensagem estilizada** (fundo suave tipo WhatsApp), um container por variação, para facilitar copy-paste.
   - **SPIN:** 4 blocos (S, P, I, N), cada bloco com lista numerada de 6 perguntas e box lateral de "nota de condução".
   - **Apresentação mais ancoragem:** sequência de bolhas de mensagem numeradas indicando a ordem de envio.
   - **Quebra de objeções:** tabela-resumo no topo mais accordions por objeção, cada accordion com tabs ou sub-blocos "versão curta (WhatsApp)" e "versão completa" dentro dos 7 argumentos.
   - **Recuperação de Carrinho:** timeline horizontal ou vertical com os 7 toques, cada toque como card com badge de tempo (15 min, 1h, 4h, D+1 AM, D+1 PM, D+3, D+7) e as 2 variações em bolhas.
   - **Follow-up:** timeline D+1 / D+3 / D+7 com bolhas de mensagem.
   - **Checklist de atendimento:** 3 colunas (antes, durante, depois) com checkbox visual.
7. **Capa interna:** primeira seção com título do documento, nome do produto, valor em destaque, objetivo ("Converter lead em aluno via WhatsApp 1:1 em fluxos de abordagem ativa, receptiva e recuperação de carrinho") e linha "Como usar este playbook" (dois caminhos: time aprende do bloco 2 ao 4, produtor pula direto para 5 ao 12 conforme o cenário).
8. **Impressão e PDF:** estilos `@media print` com margens (`@page` se útil), `page-break-inside: avoid` em tabelas, cartões de seção, bolhas de mensagem e diagrama da Furadeira visual, expandir todos os accordions na impressão (`max-height: none !important; overflow: visible !important`), fundo branco na impressão, links com cor legível.
9. **Botão "Exportar PDF" obrigatório.** Botão fixo (`position: fixed`) no canto inferior direito, com `onclick="window.print()"`, ícone opcional, rótulo "Exportar PDF", cor da marca do produto (fundo da etapa visual ou tom principal do documento), escondido na impressão (`@media print { .btn-pdf { display: none !important } }`). O botão dispensa o usuário de lembrar do Ctrl+P. O rodapé permanece só com o crédito da skill, sem instruções de impressão.

10. **Barra de busca global obrigatória.** Barra fixa (`position: sticky; top: 0`) com largura total da página, `z-index` acima do conteúdo, fundo `var(--color-layer-2)` com leve sombra inferior. Contém:
    - Input de texto com placeholder "Buscar no playbook..." e ícone de lupa à esquerda.
    - Lógica JavaScript: ao digitar (evento `input`), percorrer todo o conteúdo textual do `<body>`, envolver cada ocorrência com `<mark class="highlight">`, rolar até a primeira ocorrência (`scrollIntoView`), exibir contador "X resultado(s)" ao lado do input.
    - Botão "✕" para limpar a busca e remover todos os `<mark>`.
    - Estilo do `<mark>`: `background: #fff176; color: inherit; border-radius: 2px; padding: 0 2px`.
    - Escondida na impressão (`@media print { .search-bar { display: none !important } }`).
    - A barra de busca fica imediatamente acima do índice clicável, antes de qualquer seção de conteúdo.

11. **Painel "O lead disse..." obrigatório.** Painel interativo fixo, acessível via botão flutuante `position: fixed` no canto inferior esquerdo, com rótulo "💬 O lead disse..." e cor `var(--color-positive)`. Ao clicar no botão, abre um painel lateral (drawer) ou modal centralizado com:
    - **Textarea** de entrada com placeholder "Cole ou digite aqui o que o lead acabou de falar..." (mínimo 4 linhas, largura total do painel).
    - **Botão "Buscar resposta"** que aciona a lógica de matching descrita abaixo.
    - **Área de resultado** com título "Próxima mensagem sugerida:" exibindo a resposta em formato de bolha de mensagem estilizada (mesma classe das bolhas do playbook), com botão "📋 Copiar" que copia o texto ao clipboard (`navigator.clipboard.writeText`).
    - **Área de contexto** abaixo da resposta com badge indicando a seção de origem (ex: "Seção 10 — Quebra de objeções", "Seção 5 — Abordagem Ativa, Bloco 3") e link âncora clicável "Ver no playbook →" que rola até a seção correspondente.
    - **Lógica de matching (JavaScript puro, client-side):**
      - Normalizar o texto do lead: remover acentos, converter para minúsculas, remover pontuação.
      - Construir um índice de respostas no momento de geração do HTML: cada bolha de mensagem do playbook recebe um atributo `data-keywords` preenchido com palavras-chave relevantes derivadas do conteúdo da própria seção (ex: bolhas da seção de objeção de preço recebem `data-keywords="caro preço não tenho dinheiro valor investimento parcelamento"`; bolhas de recuperação de carrinho recebem `data-keywords="checkout finalizou compra link pagamento"`).
      - O matching percorre todos os elementos com `data-keywords`, calcula um score de sobreposição de palavras entre o texto do lead e os keywords de cada resposta, e retorna a resposta com maior score.
      - Em caso de empate, priorizar: (1) quebra de objeções, (2) abordagem receptiva, (3) abordagem ativa, (4) recuperação de carrinho.
      - Se score for zero (nenhuma palavra em comum), exibir mensagem: "Nenhuma resposta encontrada para este contexto. Tente reformular ou consulte o índice."
    - O painel fecha com botão "✕" ou clique fora (overlay com `backdrop-filter: blur(2px)`).
    - Escondido na impressão (`@media print { .lead-panel, .btn-lead { display: none !important } }`).
    - O atributo `data-keywords` de cada bolha é gerado durante a criação do HTML, com palavras específicas do nicho, das objeções, das dores e dos vocabulários presentes no `idconsumidor.md` e no `perfil.md`.

### Sistema de Design: Adobe Spectrum 2 (traduzido para CSS puro)

O playbook HTML segue os princípios visuais do **Adobe Spectrum 2** — Rational, Human, Focused, Collaborative — traduzidos em CSS puro (sem dependência do framework React). O arquivo é single-file, portanto todos os tokens ficam como variáveis CSS no `<style>` do `<head>`.

#### Tokens de cor obrigatórios (CSS Variables)

```css
:root {
  /* Camadas de fundo (Spectrum layer tokens) */
  --color-base:             #ffffff;
  --color-layer-1:          #f8f8f8;
  --color-layer-2:          #f0f0f0;
  --color-elevated:         #ffffff;
  --color-pasteboard:       #e8e8e8;

  /* Cores semânticas (Spectrum semantic tokens) */
  --color-accent:           #0265dc;
  --color-accent-subtle:    #e8f0fd;
  --color-neutral:          #222222;
  --color-neutral-subdued:  #555555;
  --color-neutral-subtle:   #efefef;
  --color-positive:         #0d7d45;
  --color-positive-subtle:  #d7f4e3;
  --color-negative:         #d7373f;
  --color-negative-subtle:  #fde8e8;
  --color-notice:           #c4640c;
  --color-notice-subtle:    #fdf0e0;
  --color-informative:      #0065bd;
  --color-informative-subtle: #e0f0ff;

  /* Texto (Spectrum text color tokens) */
  --color-heading:  #1a1a1a;
  --color-body:     #333333;
  --color-detail:   #6e6e6e;
  --color-disabled: #b3b3b3;
  --color-on-accent: #ffffff;
}
```

#### Escala tipográfica (Spectrum 2 type scale → CSS)

| Papel | font-size | font-weight | line-height | Uso no playbook |
|---|---|---|---|---|
| `heading-xl` | 28–36px | 700 | 1.2 | Título da capa, valor do produto |
| `heading-lg` | 22px | 700 | 1.25 | Título de seção (`h2`) |
| `heading` | 18px | 700 | 1.3 | Subtítulo de bloco (`h3`) |
| `heading-sm` | 15px | 600 | 1.35 | Título de card |
| `body-lg` | 16px | 400 | 1.6 | Corpo principal |
| `body` | 14px | 400 | 1.55 | Texto padrão, mensagens de WhatsApp |
| `body-sm` | 13px | 400 | 1.5 | Índice, notas de rodapé, badges |
| `detail` | 11px | 500 | 1.4 | Labels de seção, timestamps da recuperação |

Fonte padrão: `"Adobe Clean", Inter, "DM Sans", system-ui, sans-serif`

#### Escala de espaçamento (Spectrum baseSpacing)

Use **múltiplos de 4px** como valores de `padding`, `margin` e `gap`. Valores canônicos: `0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 80, 96`.

- `padding` interno de cards: `16px 20px`
- `gap` entre cards em grid: `16px`
- `margin-bottom` entre seções: `40px`
- `padding` de seção: `32px 40px`

#### Border radius (Spectrum tokens)

| Token | Valor CSS | Uso |
|---|---|---|
| `sm` | `4px` | Tags pequenas, inputs |
| `default` | `8px` | Cards, containers |
| `lg` | `12px` | Cards de seção, capa |
| `xl` | `16px` | Painéis principais |
| `pill` | `999px` | Pills da identidade do comunicador, badges de tempo |

#### Sombras (Spectrum shadow tokens)

| Token | Valor CSS | Uso |
|---|---|---|
| `elevated` | `0 2px 8px rgba(0,0,0,0.12)` | Cards normais |
| `emphasized` | `0 4px 16px rgba(0,0,0,0.18)` | Capa, card de destaque |
| `dragged` | `0 8px 24px rgba(0,0,0,0.22)` | Botão PDF fixo |

#### Princípios Spectrum 2 aplicados ao playbook

1. **Rational** — hierarquia visual clara: capa > seção > card > mensagem. Cada nível tem tamanho, peso e cor diferentes. Nunca usar decoração sem função.
2. **Human** — espaço de respiro generoso (padding mínimo `16px`), fontes legíveis mesmo em tela de celular (mínimo `14px`). Ícones são opcionais e nunca em excesso.
3. **Focused** — uma ação primária visível por vez (botão PDF fixo no canto, sem competição com outros CTAs). Accordions fecham o que não é necessário no momento.
4. **Collaborative** — paleta semântica consistente em todo o documento: `positive` (verde) = confirmação/fechamento, `negative` (vermelho) = objeção, `notice` (laranja) = atenção/escassez, `accent` (azul) = ação primária/link.

#### Mapeamento de cores por componente do playbook

| Componente | Background | Texto | Borda / Detalhe |
|---|---|---|---|
| Capa | `var(--color-accent)` | `var(--color-on-accent)` | — |
| Seção ímpar | `var(--color-base)` | `var(--color-heading)` | `1px solid var(--color-neutral-subtle)` |
| Seção par | `var(--color-layer-1)` | `var(--color-heading)` | `1px solid var(--color-neutral-subtle)` |
| Cards gerais | `var(--color-elevated)` | `var(--color-body)` | `border-radius: 8px; box-shadow: elevated` |
| Bolhas de mensagem | `var(--color-accent-subtle)` | `var(--color-neutral)` | `border-radius: 999px/12px` |
| Pills verde (conectar) | `var(--color-positive-subtle)` | `var(--color-positive)` | `border-radius: pill` |
| Pills rosa (afastar) | `var(--color-negative-subtle)` | `var(--color-negative)` | `border-radius: pill` |
| Badges de tempo (carrinho) | `var(--color-notice-subtle)` | `var(--color-notice)` | `border-radius: pill` |
| Tabela-resumo de objeções | zebrado `layer-1`/`base` | `var(--color-body)` | bordas `neutral-subtle` |
| Checklist — antes | `var(--color-informative-subtle)` | `var(--color-informative)` | — |
| Checklist — durante | `var(--color-notice-subtle)` | `var(--color-notice)` | — |
| Checklist — depois | `var(--color-positive-subtle)` | `var(--color-positive)` | — |
| Botão PDF fixo | `var(--color-accent)` | `var(--color-on-accent)` | `box-shadow: emphasized` |
| Barra de busca | `var(--color-layer-2)` | `var(--color-body)` | `border-bottom: 1px solid var(--color-neutral-subtle); box-shadow: 0 2px 6px rgba(0,0,0,0.08)` |
| Highlight de busca | `#fff176` | `inherit` | `border-radius: 2px` |
| Botão "O lead disse..." | `var(--color-positive)` | `var(--color-on-accent)` | `box-shadow: emphasized` |
| Painel "O lead disse..." | `var(--color-elevated)` | `var(--color-body)` | `border-left: 3px solid var(--color-positive); box-shadow: dragged` |
| Badge de seção de origem | `var(--color-accent-subtle)` | `var(--color-accent)` | `border-radius: pill` |

### Registro obrigatório no painel de entregas

Todo playbook gerado **precisa** aparecer no painel de entregas do produto, em `meus-produtos/{produto}/painel-entregas.html`. Sem esse registro, a entrega é considerada incompleta.

Passos obrigatórios após salvar o HTML do playbook em `meus-produtos/{produto}/entregas/comercial/playbook-[slug].html`:

1. **Ler** `meus-produtos/{produto}/painel-entregas.html`. Se não existir, gerar um painel mínimo seguindo a especificação do command `/produto-concepcao` (responsável pelo painel, no Passo 4C do fluxo unificado). Nunca sobrescrever o painel existente: sempre adicionar a entrega.
2. **Localizar ou criar a seção "Comercial"** (ou equivalente no painel). Se o painel já tiver uma área de entregas por categoria, incluir o playbook nela. Se não tiver, adicionar uma nova seção chamada "Comercial" com o mesmo estilo visual das demais.
3. **Adicionar um card** para o playbook com: título ("Playbook comercial WhatsApp"), data de geração (formato `YYYY-MM-DD`), link relativo para o arquivo (`entregas/comercial/playbook-[slug].html`), tag de status (`Atualizado` se acabou de gerar, `Gerado em DD/MM/YYYY`), e link "Abrir" que abre o HTML em nova aba (`target="_blank"`).
4. **Atualizar o card existente** se já houver um registro de playbook para este produto: substituir data, manter histórico apenas se o painel já tiver esse padrão. Não duplicar cards.
5. **Preservar o restante do painel intacto:** não alterar estrutura, CSS, cores, outras entregas. A edição é cirúrgica, só no bloco do playbook.
6. **Atualizar o manifest do painel global** se existir. Rodar `/painel-atualizar` ao final ou instruir o usuário a rodar, para que `painel/index.html` reflita a nova entrega na visão agregada de todos os produtos.

Na mensagem de entrega no chat, confirme os dois caminhos ao usuário: o arquivo salvo e o registro no painel, nesta ordem.

### O que não fazer

- Não perguntar ao usuário tipo de material, produto ou faixa de preço. Tudo vem dos arquivos.
- Não gerar subentregas separadas (só abordagem ativa, só objeções, só recuperação). Sempre o playbook completo.
- Não cobrir call presencial ou por vídeo, pitch de palco, proposta formal. Isso é high ticket, fica em `/ht-*`.
- Não salvar só `.md` como entrega principal do comando (salvar HTML. Markdown só se o usuário pedir cópia em texto).
- Não mostrar o código HTML no chat ao usuário final: salvar o arquivo e informar o caminho, mais a dica de PDF (conforme `CLAUDE.md` para páginas HTML).
- Não escrever SPIN genérico. Toda pergunta é específica ao nicho, vocabulário e rotina do consumidor.
- Não escrever mensagens longas de WhatsApp. Uma ideia por mensagem.
- Não reescrever as 5 objeções do `idconsumidor.md`. Extrair como estão. Se estiverem incompletas, pedir para rodar `/produto-concepcao` antes (a identidade do consumidor é gerada automaticamente ao final do fluxo).
- Não usar voz neutra. Usar a voz do comunicador em todo o documento, incluindo títulos, exemplos, frases prontas e notas.
