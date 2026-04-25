---
name: workshop-marketing:comercial-playbook
description: Gerar o playbook comercial completo de venda 1:1 por WhatsApp (middle e low ticket) do produto ativo. Cobre moldura DEF (Descoberta, Encantamento, Fechamento), abordagem ativa, abordagem receptiva, SPIN, recuperação de carrinho, follow-up, quebra de objeções pelo Framework dos 7 Argumentos e dicionário do comercial. Entrega em HTML único, pronto para leitura e exportação em PDF.
---

# Playbook Comercial. Venda 1:1 por WhatsApp (Middle e Low Ticket)

Gera o **playbook comercial completo** de venda 1:1 por WhatsApp do produto ativo, usando toda a identidade do produto, do consumidor e do comunicador já cadastrada. **Escopo:** abordagem ativa (outbound), abordagem receptiva (inbound) e recuperação de carrinho. Produtos middle ou low ticket.

**Fora de escopo:** call de venda presencial ou por vídeo, venda high ticket (C10X), pitch de palco, proposta formal de consultoria. Para esses, ver `/ht-*`.

**Produto final:** arquivo **HTML** único, bem formatado, com CSS para tela e impressão, convertível em PDF pelo navegador (Imprimir, Salvar como PDF). Siga a skill `playbook-comercial` para estrutura e requisitos do HTML.

## Usage

```
/comercial-playbook
```

## Princípio

Esta skill faz **uma coisa só:** o playbook comercial completo de WhatsApp 1:1 do produto. Não gera pitch isolado, nem só objeções, nem só recuperação de carrinho. Sempre o playbook completo, em um único HTML.

O playbook tem **duplo público:**

1. **Time comercial** que não conhece o produto. Precisa aprender o Quadro, a Furadeira, a identidade do consumidor e a voz do comunicador dentro do próprio documento.
2. **Produtor do produto** que atende o WhatsApp. Precisa de mensagens prontas, fluxos de abordagem, sequências de recuperação, quebra de objeções na ponta da língua.

Por isso o playbook é prático, visual, didático, dinâmico e totalmente personalizado. Toda informação vem dos arquivos do produto (perfil, identidade do consumidor, painel de entregas). A skill não pergunta dados que já existem no disco.

## Design System. Adobe Spectrum 2 (regra obrigatória)

O visual do playbook segue o **Adobe Spectrum 2** (https://react-spectrum.adobe.com/getting-started) em **CSS puro**, sem React. Os tokens e componentes vivem em `scripts/playbook_template.py` (blocos `_CSS_TOKENS`, `_CSS_BASE`, `_CSS_COMPONENTS`). Todo HTML gerado (shell automático ou seções criativas dos subagentes) precisa respeitar esses tokens.

**Tokens canônicos (definidos em `playbook_template.py`):**

- **Cores.** `--color-accent` (azul Spectrum `#0265dc`), `--color-accent-subtle`, `--color-neutral`, `--color-positive`, `--color-negative`, `--color-notice`, `--color-informative` e suas variantes `-subtle` para fundos suaves.
- **Superfícies.** `--color-base`, `--color-layer-1`, `--color-layer-2`, `--color-elevated`, `--color-pasteboard`.
- **Texto.** `--color-heading`, `--color-body`, `--color-detail`, `--color-disabled`, `--color-on-accent`.
- **Tipografia.** `Inter` + fallback `Adobe Clean`, system-ui. Escala h1/h2/h3/h4 = 32 / 22 / 18 / 15 px. Corpo 14 px, line-height 1.55.
- **Raios.** `--radius-sm` 4, `--radius-default` 8, `--radius-lg` 12, `--radius-xl` 16, `--radius-pill` 999.
- **Sombras.** `--shadow-elevated`, `--shadow-emphasized`, `--shadow-dragged` (elevações Spectrum).
- **Componentes prontos.** `.capa`, `.indice`, `.card`, `.card-grid`, `.bolha`, `.bolha-grupo`, `.nota-conducao`, `.badge-tempo`, `.pill`, `.pill-conectar`, `.pill-afastar`, `.pill-grupo`.

**Proibido:**

1. Inventar classe CSS fora das já definidas em `playbook_template.py`.
2. Hardcodar cor, fonte, raio ou sombra em `style=""`. Se precisar de variação pontual (ex: box informativo em seção criativa), use **variáveis CSS** (`style="background:var(--color-informative-subtle);border-left:3px solid var(--color-informative);"`).
3. Importar React Spectrum como biblioteca, `@spectrum-web-components`, Spectrum CSS da Adobe via CDN, ou qualquer dependência externa. O playbook é HTML único e offline. Usamos apenas os **tokens** e **padrões visuais** do Spectrum 2 adaptados a CSS puro dentro do `<style>` embutido.
4. Redesenhar estrutura do template (grid, layout, componentes de bolha/card/pill). Para evoluir o visual, edite `scripts/playbook_template.py`, nunca o HTML já gerado em `meus-produtos/.../playbook-{slug}.html`.

**Onde mexer quando quiser evoluir o design:** só em `scripts/playbook_template.py`. Tudo que for mudança de cor, espaçamento, componente, sombra ou tipografia vai nos blocos `_CSS_TOKENS`/`_CSS_BASE`/`_CSS_COMPONENTS`. Rode `playbook-montar.py` depois para regerar o HTML do produto.

## O Que Fazer

### 1. Contexto (leitura automática, sem perguntas)

Leia, nesta ordem:

1. `meus-produtos/.ativo`. Identificador do produto ativo.
2. Listagem de `meus-produtos/`. Conte quantos produtos estão cadastrados (subpastas com `perfil.md`).
3. `meus-produtos/{ativo}/perfil.md`. Obrigatório. Quadro, Furadeira, Decorados, 3 Identidades (Produto, Consumidor, Comunicador), Urgências Ocultas (7 categorias × 10 itens), preço, oferta, Argumentos Incontestáveis e diferenciais.
4. `meus-produtos/{ativo}/idconsumidor.md`. Obrigatório para este comando. Contém as 5 objeções com as 7 quebras de 2 parágrafos cada (Framework dos 7 Argumentos), paliativos, frases do público, tom e baldes de para quem é.
5. `meus-produtos/{ativo}/painel-entregas.html`. Se existir. Fonte visual de referência com os mesmos dados organizados.
6. Arquivos complementares em `meus-produtos/{ativo}/entregas/*` (páginas, concepção, anúncios). Leitura leve, para capturar linguagem e argumentos já aprovados.

Se `perfil.md` não existir, pare e oriente a usar `/produto-concepcao` antes.

Se `idconsumidor.md` não existir ou não tiver as 5 objeções com as 7 quebras completas, pare e oriente a usar `/produto-concepcao` antes (o fluxo gera a identidade do consumidor automaticamente ao final). O playbook depende desses dados para a seção de quebra de objeções.

### 2. Escolha de produto (pergunta condicional)

**Única situação em que a skill faz pergunta:** quando existe mais de um produto cadastrado em `meus-produtos/`.

**Se só existe um produto cadastrado:** pule esta etapa e siga direto para a geração.

**Se existem dois ou mais produtos cadastrados:**

```
Encontrei [N] produtos cadastrados. Pra qual deles vou gerar o playbook comercial de WhatsApp?

1. [nome do produto 1] (ativo)
2. [nome do produto 2]
3. [nome do produto 3]
...

Digite o número:
```

O produto ativo aparece marcado como `(ativo)` na lista. Se o usuário escolher um produto diferente do ativo, use esse produto como base para leitura e para o caminho de salvamento, mas **não altere** `meus-produtos/.ativo` (troca de produto ativo é responsabilidade do `/produto-trocar`).

### 3. Geração (arquitetura paralela de performance, ~1 min total)

**Por que o fluxo é rápido:**

1. Script Python monta **as 12 seções** diretamente de `perfil.md` + `idconsumidor.md` em ~1 segundo. **Inclusive as 6 seções criativas (4, 5, 6, 7, 10, 11):** o template Python já cria toda a estrutura HTML (bolha-grupos, cards, badges, notas) com marcadores `{{N.chave}}` nos lugares onde entra texto. Os agentes não geram mais HTML.
2. Os textos das 6 seções criativas rodam em **3 subagentes paralelos** (2 seções cada). Cada agente devolve apenas um JSON plano `{"4.b1.a": "texto...", ...}` com frases curtas de WhatsApp. O script `playbook-aplicar-criativas.py` substitui os marcadores `{{chave}}` pelo texto com escape HTML. Como os agentes escrevem só texto (não HTML + CSS), o tempo total é ~45-60 segundos em vez de ~3 minutos.

**Etapa 1. Montagem automática (~5 segundos)**

Anuncie: `🔍 Próximo passo: montar o shell HTML com capa, DEF, fechamento, objeções e dicionário. Tempo estimado: cerca de 1 minuto.`

**Como invocar o Python** (escolha conforme o ambiente do aluno, detectável pela variável `Platform` do sistema):
- **Windows:** `py -3 scripts/playbook-montar.py --slug {produto-escolhido}`
- **Mac/Linux:** `python3 scripts/playbook-montar.py --slug {produto-escolhido}`

Se `py -3` não estiver disponível no Windows (raro, mas acontece com instalações customizadas), use `python scripts/playbook-montar.py --slug {produto-escolhido}`.

**Proibido** hardcodar caminho absoluto do Python (ex: `C:/Users/NOME/...python.exe`). O comando precisa funcionar em qualquer máquina do aluno.

O script:

1. Lê `perfil.md` e `idconsumidor.md` do produto.
2. Preenche automaticamente as seções 1 (Capa), 2 (Identidade do Produto), 3 (Metodologia DEF), 8 (Fechamento em 4 passos) e 12 (Dicionário).
3. Delega a seção 9 (Quebra de objeções pelos 7 Argumentos) para `scripts/playbook-extrair-objecoes.py`, que devolve accordion + tabela-resumo prontos do `idconsumidor.md`. Cada argumento vira um sub-accordion (`<details class="arg-card">`), com o primeiro argumento aberto por padrão e os demais colapsados.
4. **Renderiza a estrutura HTML completa** das seções 4, 5, 6, 7, 10 e 11 (bolha-grupos, cards, badges, notas, boxes explicativos, h3s de subseção, tudo com CSS do design system). Dentro dessas seções, nos lugares onde entra texto do lead, posiciona marcadores `{{N.chave}}` (ex: `{{4.b1.a}}`, `{{6.S.q1}}`, `{{11.upsell.frase}}`). Ao todo são **93 marcadores** nas 6 seções.
5. Escreve o HTML final em `meus-produtos/{produto-escolhido}/entregas/comercial/playbook-{slug}.html` e imprime o caminho no stdout.

Se o script falhar por falta de arquivo, oriente o usuário a rodar `/produto-concepcao` e pare.

Anuncie: `✅ Shell + 12 seções renderizadas. Caminho: {caminho}. Disparando 3 subagentes para preencher os 93 textos das criativas em paralelo.`

**Etapa 2. 3 subagentes paralelos preenchem as 6 seções criativas (~60 segundos)**

Anuncie: `🔍 Próximo passo: gerar as 6 seções criativas (Outbound, Inbound, SPIN, Preço, Recuperação, Follow-up) em 3 subagentes paralelos. Tempo estimado: cerca de 1 minuto.`

**Dispare os 3 Agents em paralelo, em uma única mensagem, com múltiplas tool calls Agent simultâneas.** Cada Agent é do tipo `general-purpose` e devolve apenas o HTML do miolo das suas 2 seções (sem os marcadores `<!-- CREATIVE_N_START -->` / `<!-- CREATIVE_N_END -->`, sem `<section>`, sem `<h2>`: **só o conteúdo interno** que vai entre os marcadores).

**Grupos fixos de 2 seções por Agent:**

- **Agent 1 (Abordagens):** seções 4 (Outbound) e 5 (Inbound).
- **Agent 2 (Diagnóstico e preço):** seções 6 (SPIN) e 7 (Apresentação + ancoragem de preço).
- **Agent 3 (Pós-conversa):** seções 10 (Recuperação de carrinho) e 11 (Follow-up + Upsell + Downsell + Order bump).

**Prompt padrão de cada Agent** (montar substituindo `{slug}`, `{grupo}` e incluindo o schema de chaves específico do grupo):

```
Você vai escrever textos curtos de WhatsApp para 2 seções de um playbook comercial. Você NÃO escreve HTML nem CSS. A estrutura visual já está pronta. Seu trabalho é devolver frases prontas para bolhas de mensagem, que serão coladas em marcadores específicos do template.

Contexto obrigatório (leia antes de escrever qualquer frase):
1. `meus-produtos/{slug}/perfil.md`. Extraia: nome do produto, Quadro, Furadeira (macroetapas e microetapas), preço, diferenciais, Argumentos Incontestáveis, Identidade do Comunicador (tom, palavras que conectam, palavras que afastam, mantras), Urgências Ocultas (dores, desejos, dúvidas, quentes, frias, inusitadas, assuntos).
2. `meus-produtos/{slug}/idconsumidor.md`. Extraia: perfil do consumidor, paliativos (soluções concorrentes que ele já usa), 10 frases que ele diria, baldes de Para Quem É.

Regras de voz (obrigatórias em cada texto):
- Usar palavras que conectam, evitar palavras que afastam (da Identidade do Comunicador).
- Respeitar os 7 princípios de WhatsApp: mensagens curtas (uma ideia por bolha), pergunta curta no final sempre que possível, nome do lead como `[NOME]` na primeira e última mensagem, link sempre com contexto, nunca perguntar "quer comprar?", ritmo adequado ao canal.
- Proibido travessão (—), ponto de exclamação, estrutura "não é X, é Y", promessas vagas.
- Vocabulário, paliativos, rotina e frases concretas do consumidor aparecem em cada mensagem. Proibido genérico.
- Quando precisar inserir a palavra que o próprio lead usou, escreva entre colchetes: `[palavra que o lead usou]` ou `[dor descrita pelo lead]`.
- Cada bolha é uma frase curta de WhatsApp (máximo 2 a 3 linhas). Não escreva parágrafos longos.
- Proibido gerar HTML, markdown, listas, bullets, quebras `\n\n` artificiais. É só texto puro. O script escapa HTML e insere na bolha.

Saída:
Devolva um único JSON exato, sem markdown, sem ```json, sem texto antes ou depois. Todas as chaves listadas abaixo são obrigatórias. Cada valor é uma string curta (1 mensagem de WhatsApp). Em notas de condução, 1 a 2 frases instrutivas para o vendedor (ex: "Se o lead responder com emoji, avance para a pergunta 2. Se pedir link, volte ao bloco anterior.").

Schema exato para este Agent ({grupo}):
{schema_json}
```

**Schema por grupo (substituir `{schema_json}` no prompt):**

**Agent 1 (seções 4 + 5, 39 chaves):**

- **Seção 4. Outbound.** 7 blocos (b1 a b7) × 3 chaves cada (a = variação leve, b = variação direta, nota = nota de condução).
- **Seção 5. Inbound.** 6 blocos (b1 a b6) × 3 chaves cada (mesma convenção).

Blocos da seção 4: b1 Primeiro contato · b2 Qualificação leve · b3 Amarrar a dor (Urgência Oculta em pergunta aberta) · b4 Oferecer ajuda concreta · b5 Convite para conversa real · b6 Transição para diagnóstico · b7 Encerramento se não engajou.

Blocos da seção 5: b1 Acolhimento imediato · b2 Pergunta de posicionamento · b3 Diagnóstico rápido (3 a 5 perguntas) · b4 Apresentação conectada · b5 Prova + preço · b6 Checkout + confirmação com pressuposto do sim.

Schema literal (passe isto dentro do prompt):
```json
{
  "4.b1.a": "...", "4.b1.b": "...", "4.b1.nota": "...",
  "4.b2.a": "...", "4.b2.b": "...", "4.b2.nota": "...",
  "4.b3.a": "...", "4.b3.b": "...", "4.b3.nota": "...",
  "4.b4.a": "...", "4.b4.b": "...", "4.b4.nota": "...",
  "4.b5.a": "...", "4.b5.b": "...", "4.b5.nota": "...",
  "4.b6.a": "...", "4.b6.b": "...", "4.b6.nota": "...",
  "4.b7.a": "...", "4.b7.b": "...", "4.b7.nota": "...",
  "5.b1.a": "...", "5.b1.b": "...", "5.b1.nota": "...",
  "5.b2.a": "...", "5.b2.b": "...", "5.b2.nota": "...",
  "5.b3.a": "...", "5.b3.b": "...", "5.b3.nota": "...",
  "5.b4.a": "...", "5.b4.b": "...", "5.b4.nota": "...",
  "5.b5.a": "...", "5.b5.b": "...", "5.b5.nota": "...",
  "5.b6.a": "...", "5.b6.b": "...", "5.b6.nota": "..."
}
```

**Agent 2 (seções 6 + 7, 32 chaves):**

- **Seção 6. SPIN.** 4 fases (S, P, I, N) × 4 chaves (q1, q2, q3 = 3 perguntas + nota de condução). Total 16. **Todas as 12 perguntas personalizadas ao nicho, ao Quadro e à dor central. Cita vocabulário, situações e paliativos concretos do consumidor. Proibido genérico.**
  - S. Situação: cenário atual (rotina, ferramentas, tentativas, momento de vida).
  - P. Problema: dor central trazida à tona com vocabulário do consumidor.
  - I. Implicação: custo de não resolver (financeiro, emocional, tempo, reputação, saúde).
  - N. Necessidade: visão do resultado ideal conectada ao Quadro.

- **Seção 7. Apresentação + ancoragem de preço.** Blocos temáticos:
  - `7.ponte.a`, `7.ponte.b`: 2 mensagens de ponte dor-solução (com palavras do lead em `[colchetes]`).
  - `7.desc.a`, `7.desc.b`, `7.desc.c`, `7.desc.d`: 4 mensagens de descrição objetiva (o que é, como funciona, semana a semana baseado na Furadeira).
  - `7.prova.a`, `7.prova.b`, `7.prova.c`: 3 provas curtas (caso real com nome fictício, número agregado, depoimento de 1 linha).
  - `7.conexao`: 1 mensagem conectando Furadeira ao Quadro.
  - `7.preco.alta`, `7.preco.funcional`, `7.preco.real`, `7.preco.confirm`: revelação de preço em 4 tempos. Alta = valor total somado. Funcional = custo de a dor continuar. Real = preço real do produto. Confirm = `faz sentido pra você?` no tom do comunicador.
  - `7.paliativo.a`, `7.paliativo.b`: 2 mensagens comparando com paliativos concretos do consumidor.

Schema literal:
```json
{
  "6.S.q1": "...", "6.S.q2": "...", "6.S.q3": "...", "6.S.nota": "...",
  "6.P.q1": "...", "6.P.q2": "...", "6.P.q3": "...", "6.P.nota": "...",
  "6.I.q1": "...", "6.I.q2": "...", "6.I.q3": "...", "6.I.nota": "...",
  "6.N.q1": "...", "6.N.q2": "...", "6.N.q3": "...", "6.N.nota": "...",
  "7.ponte.a": "...", "7.ponte.b": "...",
  "7.desc.a": "...", "7.desc.b": "...", "7.desc.c": "...", "7.desc.d": "...",
  "7.prova.a": "...", "7.prova.b": "...", "7.prova.c": "...",
  "7.conexao": "...",
  "7.preco.alta": "...", "7.preco.funcional": "...", "7.preco.real": "...", "7.preco.confirm": "...",
  "7.paliativo.a": "...", "7.paliativo.b": "..."
}
```

**Agent 3 (seções 10 + 11, 22 chaves):**

- **Seção 10. Recuperação de carrinho.** 5 toques (t1 a t5) × 2 variações (a = leve, b = direta). Total 10.
  - t1 = 15 min após abandono (tom de ajuda).
  - t2 = 1h depois (quebra da primeira objeção provável: preço ou segurança + prova social curta).
  - t3 = D+1 (nova angulação com Urgência Oculta diferente + escassez real se houver).
  - t4 = D+3 (última chamada educada, foco na consequência de adiar).
  - t5 = D+7 (encerramento respeitoso + oferta de downsell se houver).

- **Seção 11. Follow-up + Upsell + Downsell + Order bump.**
  - Follow-up: 3 tempos (d1, d3, d7) × 2 variações (a, b). `11.fu.d1.a` = leve, `11.fu.d1.b` = direta, etc.
  - Upsell: `11.upsell.oferta` (nome + valor aproximado da oferta complementar pós-compra em até 48h) + `11.upsell.frase` (mensagem de WhatsApp).
  - Downsell: `11.downsell.oferta` + `11.downsell.frase`.
  - Order bump: `11.bump.oferta` + `11.bump.frase` (chamada curta para o checkout).

Schema literal:
```json
{
  "10.t1.a": "...", "10.t1.b": "...",
  "10.t2.a": "...", "10.t2.b": "...",
  "10.t3.a": "...", "10.t3.b": "...",
  "10.t4.a": "...", "10.t4.b": "...",
  "10.t5.a": "...", "10.t5.b": "...",
  "11.fu.d1.a": "...", "11.fu.d1.b": "...",
  "11.fu.d3.a": "...", "11.fu.d3.b": "...",
  "11.fu.d7.a": "...", "11.fu.d7.b": "...",
  "11.upsell.oferta": "...", "11.upsell.frase": "...",
  "11.downsell.oferta": "...", "11.downsell.frase": "...",
  "11.bump.oferta": "...", "11.bump.frase": "..."
}
```

**Etapa 3. Aplicar os textos das 6 seções criativas via script Python (~2 segundos)**

**Não faça Edits manuais um a um.** Isso reintroduz latência que a paralelização eliminou. Em vez disso:

1. Salve o JSON retornado por cada Agent como arquivo temporário em `scripts/`. Use o tool Write, um arquivo por Agent:
   - `scripts/.tmp-criativas-4-5.json` (output do Agent 1, 39 chaves)
   - `scripts/.tmp-criativas-6-7.json` (output do Agent 2, 32 chaves)
   - `scripts/.tmp-criativas-10-11.json` (output do Agent 3, 22 chaves)
   Cada arquivo é um JSON plano com as chaves e textos do schema do seu Agent (ex: `{"4.b1.a": "texto...", "4.b1.b": "texto...", ...}`).

2. Rode o aplicador que substitui os 93 marcadores `{{N.chave}}` em uma passada, escapando HTML. A flag `--cleanup` apaga os 3 JSONs temporários após aplicar (dispensa `rm`, que é bash-only):

- Windows:
```
py -3 scripts/playbook-aplicar-criativas.py --slug {produto-escolhido} --json scripts/.tmp-criativas-4-5.json --json scripts/.tmp-criativas-6-7.json --json scripts/.tmp-criativas-10-11.json --cleanup
```

- Mac/Linux:
```
python3 scripts/playbook-aplicar-criativas.py --slug {produto-escolhido} --json scripts/.tmp-criativas-4-5.json --json scripts/.tmp-criativas-6-7.json --json scripts/.tmp-criativas-10-11.json --cleanup
```

**Proibido** hardcodar caminho absoluto do Python (ex: `C:/Users/.../python.exe`). A skill precisa rodar em qualquer máquina.

O script:
1. Lê os 3 JSONs e junta em um dicionário `{chave: texto}`.
2. Para cada chave, substitui `{{chave}}` no HTML por `html.escape(texto)` (proteção contra `<`, `>`, `&`, `"`).
3. Reescreve o HTML final.
4. Se sobrar algum marcador `{{N.chave}}` não preenchido, emite aviso (mas não falha). Se alguma chave do JSON não achar marcador no HTML, também emite aviso.

Anuncie ao final: `✅ 93 textos aplicados nas 6 seções criativas. Caminho: {caminho}.`

**Regra obrigatória do Painel de Entregas (aplicada via `painel_template.py`):**

- O card do Playbook Comercial no painel exibe um **botão** (classe `.btn-primary`), nunca um link de texto simples.
- O caminho no `href` do botão deve ser relativo à pasta do produto (ex: `entregas/comercial/playbook-{slug}.html`), nunca relativo à raiz do repositório. O `painel-incremental.py` usa `arquivo.relative_to(produto_dir)` para garantir isso. Caminho errado faz o botão não abrir.
- Se o painel foi gerado antes dessa correção e o botão não abre, regere rodando `py -3 scripts/painel-incremental.py --secao comercial-playbook --slug {slug}` novamente.

**Etapa 4. Registrar o playbook no Painel de Entregas (obrigatório, ~2 segundos)**

Assim que o HTML do playbook fica pronto, a skill **precisa** registrá-lo como entrega no painel do produto. Essa é a única skill que atualiza a seção `comercial-playbook` do painel. O fluxo de `/produto-concepcao` nunca toca nessa seção: se você rodou `/produto-concepcao` e o card aparece como "Em breve", é esperado. Só muda quando você gera o playbook por aqui.

Anuncie: `🔍 Próximo passo: registrar o playbook como entrega no Painel do produto. Tempo estimado: cerca de 1 minuto.`

- Windows:
```
py -3 scripts/painel-incremental.py --secao comercial-playbook --slug {produto-escolhido}
```

- Mac/Linux:
```
python3 scripts/painel-incremental.py --secao comercial-playbook --slug {produto-escolhido}
```

O `--slug` é obrigatório aqui porque a Etapa 2 pode ter usado um produto diferente do ativo quando existem múltiplos produtos cadastrados (ver Etapa 2). Se só existe um produto, `{produto-escolhido}` é o mesmo do `.ativo` e o `--slug` pode ser omitido.

O script:

1. Lê `meus-produtos/{produto-escolhido}/entregas/comercial/playbook-{slug}.html`.
2. Detecta a data de última geração (mtime do arquivo) e injeta um card "Playbook Comercial gerado" na aba **ENTREGAS** do painel, com link clicável para o HTML.
3. Se o painel do produto é antigo e não tinha a seção `comercial-playbook`, o script faz auto-upgrade: reconstrói o shell preservando todas as seções já preenchidas (quadro, furadeira, decorados, urgências, identidades, pesquisa) e adiciona a aba nova.

Anuncie ao final: `✅ Playbook registrado no Painel de Entregas. Aba ENTREGAS → Playbook Comercial.`

#### Conteúdo das 12 seções

**1. Capa interna:**
- Título do documento (ex: "Playbook comercial WhatsApp · [Nome do produto]")
- Nome do produto
- Valor do curso em destaque (do `perfil.md`, faixa de preço ou valor cheio)
- Selo "Venda 1:1 por WhatsApp"
- Objetivo ("Converter lead em aluno via WhatsApp 1:1 em fluxos de abordagem ativa, receptiva e recuperação de carrinho")
- Linha "Como usar este playbook": dois caminhos rápidos. Time começa pela Identidade do Produto (bloco 2) para aprender o método. Produtor vai direto ao cenário (abordagem ativa, receptiva ou recuperação) conforme o atendimento em mãos.

**2. Identidade do Produto:**
Para o time aprender do zero. Extrair do `perfil.md` e do `painel-entregas.html`.
- Quadro (transformação principal em destaque)
- Furadeira completa (método em macroetapas e microetapas, como trilha numerada)
- Entregáveis (módulos, bônus, planilhas, comunidade, acessos)
- Diferenciais competitivos
- Argumentos Incontestáveis (lista com dado concreto mais fonte)
- Posicionamento (mentoria, curso, programa, método, conforme o produto)

**3. Metodologia DEF (moldura da conversa):**
Toda venda 1:1 por WhatsApp segue 3 estágios em ordem fixa: **Descoberta**, **Encantamento** e **Fechamento**. O vendedor só avança de estágio depois que o lead sinaliza prontidão. Cair fora da ordem queima a conversa.

Renderizar como 3 cards numerados (D, E, F), um embaixo do outro, cada um com título, objetivo em 1 linha, sinais de prontidão para avançar e 2 frases pronta para WhatsApp no tom do comunicador.

- **D. Descoberta:** entender o cenário, a dor real e o momento do lead. Perguntar mais do que falar. Sinais para avançar: o lead descreve a dor com as próprias palavras e pede uma saída.
- **E. Encantamento:** conectar a dor ao Quadro e à Furadeira usando as palavras que o lead acabou de dizer. Mostrar que o método resolve aquilo especificamente. Sinais para avançar: o lead pergunta preço, formato ou prazo.
- **F. Fechamento:** apresentar preço com ancoragem, quebrar a última objeção e enviar o link. Sinais de prontidão: o lead confirma que faz sentido e pede como pagar.

Regra de ouro: nunca pule da D direto para a F. Se o lead perguntar preço antes de ter passado pelo E, volte com uma pergunta que amarre o preço ao valor já reconhecido.

**4. Abordagem Ativa. Outbound WhatsApp:**
Fluxo para o vendedor dar o primeiro passo. Lead frio (nunca interagiu) ou morno (seguidor, consumidor de conteúdo, participou de lista).

Box destacado no topo da seção, antes da sequência: **Outbound = o lead tem perfil (good fit), mas ainda não tem dor consciente.** Por isso a abordagem começa leve, sem vender, e o trabalho do vendedor é levar o lead a perceber a própria dor. Referência: Mark Roberge (fase Has pain × Good fit). Quem recebe outbound precisa de tempo para se dar conta de que tem o problema, então pressão cedo queima o contato.

Sequência em **7 blocos**, cada bloco com **2 variações de mensagem** (leve/direta) prontas para copiar e colar e **nota de condução**:

1. Primeiro contato (quebra-gelo mais motivo de ter escrito, sem vender)
2. Qualificação leve (1 ou 2 perguntas sobre o momento atual do lead)
3. Amarrar a dor (Urgência Oculta relevante em forma de pergunta aberta)
4. Oferecer ajuda concreta (conteúdo, troca, resposta a dúvida específica, sem vender)
5. Convite para conversa real (chamar pra falar do problema específico)
6. Transição para diagnóstico (quando o lead engajou, entra no SPIN curto)
7. Encerramento se não engajou (fechar educadamente, marcar para follow-up)

**5. Abordagem Receptiva. Inbound WhatsApp:**
Fluxo para o lead que chega por anúncio, orgânico, link da bio, link da página ou palavra-chave.

Box destacado no topo da seção, antes da sequência: **Inbound = o lead já tem dor consciente, mas ainda não sabe se é good fit.** Por isso a abordagem pode ir direto ao diagnóstico, sem rodeios. O trabalho do vendedor é qualificar rápido e mostrar que o método encaixa com o perfil dele. Referência: Mark Roberge (fase Has pain × Good fit). Quem pede ajuda espera resposta objetiva. Aquecer demais aqui queima a intenção.

Sequência em **6 blocos**, cada bloco com **2 variações de mensagem** (leve/direta) prontas e **nota de condução**:

1. Acolhimento imediato (resposta rápida, chama pelo nome, confirma o interesse)
2. Pergunta de posicionamento (o que viu, por que chegou, o que já tentou)
3. Diagnóstico rápido (3 a 5 perguntas curtas no estilo SPIN adaptado)
4. Apresentação conectada (amarra à resposta do lead, usa as palavras dele)
5. Prova mais preço (1 caso real mais revelação de valor no tom certo)
6. Checkout mais confirmação (envia link e pede confirmação com pressuposto do sim)

**6. SPIN adaptado ao WhatsApp:**
12 perguntas totais, **3 por fase**, todas personalizadas ao nicho, ao Quadro e à dor central do produto ativo. Proibido perguntas genéricas. Cada pergunta cita vocabulário, situações, rotinas e paliativos concretos do consumidor.

- **S. Situação (3 perguntas):** cenário atual (rotina, ferramentas, tentativas anteriores, momento de vida)
- **P. Problema (3 perguntas):** dor central trazida à tona
- **I. Implicação (3 perguntas):** custo de não resolver (financeiro, emocional, tempo, reputação, saúde)
- **N. Necessidade (3 perguntas):** visão do resultado ideal conectada ao Quadro

Cada fase inclui nota curta de condução (o que observar, quando avançar, quando repetir em outra angulação).

**7. Apresentação mais ancoragem de preço por texto:**
Sequência de mensagens pronta para copiar e colar:
- Ponte dor-solução em 2 mensagens curtas (com as palavras do lead)
- Descrição objetiva em 3 a 4 mensagens (o que é, como funciona, semana a semana)
- Prova em 3 formatos curtos (caso real, número agregado, depoimento de 1 linha)
- Conexão da Furadeira com o Quadro em 1 mensagem
- Revelação de preço em 4 mensagens: alta (valor total somado), funcional (custo de a dor continuar), preço real, confirmação ("faz sentido pra você?")
- Comparação com paliativos (concorrentes diretos e indiretos) em 1 ou 2 mensagens

**8. Fechamento em 4 passos (WhatsApp):**
1. Conexão dor-solução: "[Nome], sua dificuldade é [DOR]. É exatamente isso que [PRODUTO] resolve. Em [TEMPO] você consegue [TRANSFORMAÇÃO]."
2. Ancoragem de valor: compare com alternativas reais em 1 ou 2 mensagens curtas.
3. Preço mais confirmação: "Tudo isso por [VALOR]. Faz sentido pra você?"
4. Envio do link: "Vou te mandar o checkout agora. Me confirma a compra que já libero seus acessos."

Proibido perguntar "quer comprar?". Assuma o interesse.

**9. Quebra de objeções pelo Framework dos 7 Argumentos:**

Extrair **todas** as 5 objeções do `idconsumidor.md` com as 7 quebras completas de 2 parágrafos cada. Se o produto tiver mais objeções mapeadas (até 7), incluir todas. Mínimo 5 objeções.

Para cada objeção, renderizar os 7 argumentos na ordem fixa:
1. Argumento Incontestável (dado concreto mais fonte)
2. Argumento Lógico (causa e efeito)
3. Argumento por Analogia (sem celebridades, situações reais)
4. Argumento por Exemplificação (caso real com nome fictício)
5. Argumento de Valor (custo vs. benefício)
6. Argumento de Consequência (agir vs. adiar)
7. Argumento de Contradição (refutação de incoerências)

Cada argumento mostra **2 versões lado a lado**:
- **Versão curta (WhatsApp):** 1 a 2 mensagens prontas para copiar e colar. Recorte da versão completa, sem inventar texto novo.
- **Versão completa:** 2 parágrafos exatamente como estão salvos no `idconsumidor.md`, para o time estudar e para gravar em áudio se fizer sentido.

Layout em accordion (uma objeção por accordion, fechado por padrão). No topo da seção, tabela-resumo com uma linha por objeção e o argumento mais forte (coluna "Argumento principal") para leitura rápida no celular.

Ao final da seção, nota em destaque: **Treine em roleplay antes de usar no lead real.** Separe 20 minutos por semana com um colega (ou espelho + áudio gravado) para simular objeção por objeção. Rodar o argumento em voz alta, ouvir, ajustar o tom. Esse é o ritual que separa time que improvisa de time que fecha.

**10. Recuperação de Carrinho:**
Sequência temporizada em **5 toques**, cada toque com **2 variações** (mais leve / mais direta):

1. **15 minutos após abandono** (tom de ajuda, "tudo certo com a finalização?")
2. **1 hora** (quebra da primeira objeção provável: preço ou segurança)
3. **D+1** (nova angulação usando Urgência Oculta diferente mais prova social curta)
4. **D+3** (última chamada educada, foco na consequência de adiar)
5. **D+7** (encerramento respeitoso mais oferta de downsell se houver)

Todos os toques em formato de mensagem de WhatsApp, respeitando os 7 princípios e a voz do comunicador.

**11. Follow-up de quem não comprou mais Upsell, Downsell, Order Bump:**

**Follow-up:** para leads que conversaram e não fecharam (sem chegar ao checkout). 3 tempos com 2 mensagens por tempo:
- D+1 (lembrete leve mais prova social curta)
- D+3 (nova angulação com Urgência Oculta diferente mais quebra de 1 objeção)
- D+7 (última chamada com escassez real mais oferta de downsell se houver)

**Upsell:** oferta complementar pós-compra, enviada em até 48h pelo WhatsApp. Valor aproximado, formato e frase pronta de oferta em mensagem.

**Downsell:** oferta menor para quem não comprou, enviada no D+7 ou após recusa explícita de preço. Valor aproximado, formato e frase pronta.

**Order bump:** complemento no próprio checkout (impulso, preço baixo). Sugestão de produto, valor e chamada curta.

**12. Dicionário do Comercial:**
Glossário dos termos que o time comercial vai ouvir no dia a dia. Cada termo em 1 a 2 linhas, linguagem de quem está aprendendo. Renderizar em 2 colunas no desktop, 1 coluna no mobile.

- **Lead:** pessoa que entrou em contato ou foi abordada pelo comercial. Ainda não é aluno.
- **Inbound:** lead que chega por iniciativa dele (anúncio, orgânico, link da bio). Já tem dor consciente.
- **Outbound:** lead que o comercial aborda primeiro. Tem perfil, mas ainda não sabe que tem a dor.
- **SDR:** vendedor que faz o primeiro contato, qualifica o lead e passa adiante. Não fecha venda.
- **Closer:** vendedor responsável pelo fechamento. Recebe o lead já qualificado pelo SDR.
- **CRM:** ferramenta onde o time registra lead, conversa, etiqueta e etapa do funil.
- **Funil de vendas:** caminho que o lead percorre do primeiro contato à compra. Cada etapa tem critério de passagem.
- **Follow-up:** retomada com lead que não fechou. Serve para lembrar, reaquecer ou oferecer alternativa.
- **Prospecção:** processo de encontrar e abordar leads novos (outbound).
- **Perpétuo:** modelo de venda sempre aberta, sem data de corte. Oposto de lançamento.
- **SPIN:** framework de diagnóstico com 4 fases (Situação, Problema, Implicação, Necessidade).
- **Objeção:** motivo que o lead dá para não comprar agora. Nem sempre é o motivo real.
- **Ancoragem:** apresentar um valor maior antes do preço real para fazer o preço real parecer justo.
- **Upsell:** oferta complementar enviada a quem já comprou.
- **Downsell:** oferta de menor valor para quem não aceitou a principal.
- **Order bump:** item adicional oferecido dentro do checkout, com 1 clique, preço baixo.

### 4. Aprovação (antes de rodar o script)

Apresente um **resumo em texto** no chat: lista das 12 seções do HTML (marcando quais são automáticas e quais o modelo escreve), confirmação do produto e preço, tom do comunicador aplicado e escopo "venda 1:1 por WhatsApp: ativa, receptiva e recuperação de carrinho". Depois pergunte:

```
1. Aprovar e gerar (script monta o HTML completo em ~5s com 93 marcadores de texto, 3 subagentes paralelos escrevem os textos das 6 criativas em JSON em ~45s, script aplicador cola tudo em ~2s. Total ~1 min)
2. Quero ajustar algo
```

Se o usuário pedir ajuste, refaça só o trecho pedido e volte à aprovação. Exceção: só pule a aprovação se o usuário tiver dito explicitamente na mesma sessão "vai direto à versão final" ou equivalente.

### 5. Salvamento (HTML obrigatório)

- Caminho único: `meus-produtos/{produto-escolhido}/entregas/comercial/playbook-{slug}.html`
- `{slug}`: nome da pasta do produto em kebab-case (ex: `mentoria-marketing-digital`).
- O script `playbook-montar.py` escreve o HTML completo em uma passada, já com as 5 seções estáticas preenchidas, a seção 9 com accordion de objeções gerada por `playbook-extrair-objecoes.py` e as 6 seções criativas já com toda a estrutura HTML (bolha-grupos, cards, badges, notas) e 93 marcadores `{{N.chave}}` nos lugares onde entra texto.
- Os 3 subagentes paralelos devolvem JSON plano `{"N.chave": "texto..."}` com os textos das 6 criativas (sem HTML). O script `scripts/playbook-aplicar-criativas.py` substitui os 93 marcadores de uma vez, com `html.escape`, em ~2 segundos. **Proibido** fazer Edits manuais sequenciais (reintroduz a latência que a paralelização eliminou).
- Aplicar checklist da skill `playbook-comercial` (arquivo único, CSS embutido, `lang="pt-BR"`, `@media print`, capa, índice clicável no topo, 12 seções, tabelas, accordions de objeções com sub-accordion de argumentos, bolhas de mensagem, timeline de recuperação, rodapé com instrução de PDF). O template já entrega 100% desse checklist, exceto o conteúdo das 6 criativas.

**Para o usuário:** não colar o código HTML no chat. Após o script rodar, informar o caminho e que o preenchimento das 6 seções criativas já começou. Ao terminar a última Edit, informar o caminho final e, em uma linha, como gerar PDF (abrir no navegador, Ctrl+P, Salvar como PDF, retrato).

### 6. Próximo Passo

"Playbook salvo em HTML. Abra no navegador para revisar ou exportar PDF. Se precisar de tráfego pro WhatsApp, use `/copy-anuncio`. Se ainda não tem página de vendas conectada ao checkout, rode `/copy-pagina` seguido de `/pagina-checkout`."
