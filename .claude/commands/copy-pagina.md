---
name: workshop-marketing:copy-pagina
description: Criar copy completa e/ou página HTML de vendas, captura ou obrigado. Para vendas 8D, preenche blocos atômicos do repositório com a copy aprovada (preserva layout do tema; não redesenha o template). Light Copy e metodologia VTSD.
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

Leia `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md` se existir.

### 2. Primeira Pergunta. O que criar

```
O que você quer criar?

1. Só a copy (texto completo da página de vendas em markdown)
2. Só a página HTML (para vendas 8D: precisa da copy em 16 blocos já salva ou aceitar exceção no passo B0)
3. Copy + página HTML (gera o texto primeiro com ## Bloco 01…16, depois monta a página)

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

**Fonte única e obrigatória:** antes de gerar uma linha de copy, leia `.claude/skills/revisora/references/manual-copy.md`. É ali que vivem:

- O **princípio central** ("a melhor copy não parece copy").
- Os **15 princípios fundamentais** (ensinar em vez de prometer; nomear cria realidade; produto não aparece no lead; tom de escritor; especificidade mata generalização; informar, não vender; crie um inimigo; argumente sempre; razão + emoção; Quadro + Decorado; dor real; ancoragem em bônus; headline em toda seção; depoimento com resultado; autoridade com conquista concreta).
- Os **20 vícios proibidos** (travessão, "não é X, é Y", perguntas no gancho, promessa vaga, "mesmo que/sem precisar", produto no lead, emojis, imperativo, lero-lero, cópia sem tese, sigla sem explicação, depoimento genérico, autoridade sem prova, copy só de promessa, bônus sem valor, seção sem headline, Quadro sem Decorado, dor só sintoma, emoção sem razão, AI slop).
- O **checklist final** (Blocos A/B/C/D) que a `revisora` aplica antes da entrega.

A aprovação do usuário só acontece depois que esse checklist passar.

**Princípios específicos de página de vendas (reforço do Manual):**
1. **Headline em TODA seção:** nenhuma seção começa sem um título curto e curioso. Seção sem headline é seção invisível.
2. **Facilitação visual do método:** a Furadeira precisa virar diagrama, esquema ou comparativo no HTML, não só parágrafo.
3. **Depoimento com resultado concreto:** cada depoimento tem antes + depois + número ou prazo. Elogio genérico é marcado para substituição.
4. **Autoridade com conquista concreta:** o bloco de autoridade precisa da jornada de origem com fragilidade + virada + número ou situação verificável. Para low ticket sem autoridade pessoal, usar "método testado com X pessoas".
5. **Bônus ancorados em valor:** cada bônus tem nome, descrição e R$ individual. Stack de valor com total maior que o preço.
6. **Vender Quadro + Decorado, não só Quadro:** a cada bloco de benefício, um Decorado tangível aparece (não só a transformação ampla).
7. **Parágrafo técnico em itálico:** ao menos um parágrafo ancora a emoção com razão (explica por que aquilo funciona logicamente ou biologicamente).
8. **Nomear cria realidade:** criar nome próprio para o problema, a causa ou o método ("Programação Emocional Repetitiva", "Negociação Terapêutica"). "Método Exclusivo" não vale.

Use os 26 elementos literários quando apropriado (consulte skill `vtsd-completo` para lista completa).

### A2.5 Estrutura do arquivo de copy (obrigatória para vendas 8D)

A copy da página de vendas **deve** ser salva com **títulos fixos** alinhados aos blocos HTML (16 blocos). Consulte o modelo:

- `.claude/skills/paginas/references/template-copy-pagina-vendas.md`

**Regras:**

- Cada bloco = um título `## Bloco NN — Nome` **exatamente** como no template (numeração com dois dígitos: 01, 02, … 16).
- Não renomeie, não una dois blocos num só, não pule número. Isso garante que a página HTML use **a mesma copy** bloco a bloco.
- O conteúdo persuasivo segue as regras das seções abaixo, mas **sempre** sob esses títulos.

### A3. Geração em 2 Partes (16 blocos)

Para garantir qualidade, SEMPRE gere em **duas partes** no **mesmo arquivo** `meus-produtos/{ativo}/entregas/copy-pagina/copy-[produto].md`.

#### PARTE 1. Blocos 01 a 09

Gere e salve no arquivo, com parágrafos desenvolvidos (persona, cenas, elementos literários onde couber):

- **Bloco 01 — Hero:** headline, subheadline, PROIBIDO nome do produto/método/curso/sigla no hero; 3 bullets (UO + decorado); indicação de vídeo; texto do botão.
- **Bloco 02 — Dor:** dor amplificada, cotidiano.
- **Bloco 03 — Paliativo:** ferramentas, produtos e soluções concorrentes do mercado que resolvem parcialmente o problema, e por que cada uma não entrega o resultado completo.
- **Bloco 04 — Prova social (primeiro bloco):** 2 a 3 depoimentos curtos; modelos marcados se não houver reais.
- **Bloco 05 — CTA intermediário:** frase + botão.
- **Bloco 06 — Método (Furadeira):** primeira vez com nome do método em destaque; macroetapas; mínimo 3 parágrafos de argumentação.
- **Bloco 07 — Para quem é / não é:** baldes da identidade do consumidor.
- **Bloco 08 — Entregáveis:** lista com nome + valor de cada item.
- **Bloco 09 — Bônus:** 3 bônus com nome, descrição e R$ cada.

Ao terminar a Parte 1, informe: `Parte 1 pronta (Blocos 01 a 09). Gerando a Parte 2 agora...`

#### PARTE 2. Blocos 10 a 16

Continue no **mesmo arquivo**, mesmo nível de detalhe:

- **Bloco 10 — Stack de valor:** itens, valores, total, preço real, parcelamento.
- **Bloco 11 — Prova social (segundo bloco) ou Depoimentos:** 3 a 5 depoimentos completos (antes/depois); modelos se necessário.
- **Bloco 12 — Suporte**
- **Bloco 13 — Garantia:** prazo (7/15/30), texto de risco zero.
- **Bloco 14 — Autoridade do criador**
- **Bloco 15 — FAQ:** 5 a 8 Q&A com objeções da persona.
- **Bloco 16 — Oferta final:** reprise de valor, preço, último CTA, urgência se houver; linha sobre termos/privacidade se aplicável.

### A4. Revisão e Correção Automática (OBRIGATÓRIO antes de entregar)

Antes de mostrar a copy ao usuário, acione a skill `revisora` passando o texto completo (todos os 16 blocos juntos). A `revisora` aplica o checklist do `.claude/skills/revisora/references/manual-copy.md` (Blocos A/B/C/D) e devolve o texto limpo com os ajustes feitos.

Aplique os ajustes propostos antes de mostrar a copy. Se a `revisora` devolver a copy sem ajustes, prossiga direto.

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

**Obrigatório:** o arquivo deve conter os **16** títulos `## Bloco NN — …` (dois dígitos), na ordem do `template-copy-pagina-vendas.md`. Sem isso, a página HTML não pode ser preenchida de forma fiel à copy.

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

## FLUXO B. Página HTML

> Ativar quando o usuário escolher a opção 2 ou 3, ou quando aceitar montar a HTML após o Fluxo A.

### B0. Fonte da copy (vendas 8D). Obrigatório para copy correta

**Se o tipo for página de vendas (8D):**

1. Verificar se existe `meus-produtos/{ativo}/entregas/copy-pagina/copy-{slug}.md` (slug = produto ativo ou nome acordado) **com** as seções `## Bloco 01` até `## Bloco 16` conforme `.claude/skills/paginas/references/template-copy-pagina-vendas.md`.
2. **Se o arquivo existir e tiver os 16 blocos:** esse arquivo é a **única fonte de texto** para preencher os templates HTML. Não inventar ofertas, preços, depoimentos ou argumentos que não estejam na copy aprovada. Só é permitido adaptar à estrutura do HTML (quebras, listas, negrito) e placeholders de mídia (`[Sua foto aqui]`, URL de vídeo, etc.).
3. **Se não existir ou faltar bloco numerado:**

```
Para a página sair com a copy correta, preciso da copy aprovada nos 16 blocos (template com títulos ## Bloco 01 … ## Bloco 16).

1. Gerar e aprovar a copy agora (Fluxo A) e depois continuo o HTML
2. O arquivo está em outro caminho (você informa o caminho completo)
3. Exceção: montar HTML sem esse arquivo (uso perfil.md e entrevista; pode divergir da copy ideal)

Digite o número:
```

- Se **1:** executar o Fluxo A até salvar `copy-[produto].md` com os 16 blocos e aprovação do usuário, **depois** retomar o Fluxo B a partir deste ponto.
- Se **2:** ler o arquivo indicado; se também não tiver os 16 `## Bloco NN`, tratar como caso 3 ou pedir correção.
- Se **3:** avisar que a página pode não refletir uma copy única aprovada; preencher a partir de `perfil.md` + respostas da entrevista B1, mantendo Etapa 0 anti-vícios.

**Captura e obrigado:** B0 não se aplica da mesma forma; use copy específica do fluxo da entrevista B1.

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

### B1.5 Melhor custo-benefício (padrão para vendas 8D)

**Objetivo:** máxima qualidade visual estável com **menor gasto de tokens**. O repositório já tem páginas completas montadas por **script**, não por texto gigante no chat.

**Proibido:** pedir ao modelo que **escreva do zero** o arquivo monolítico `pagina_completa_*/code.html` (milhares de linhas). Esse arquivo é **saída do merge**, não rascunho no chat.

**Regra de ouro (template fixo, copy variável):** o template já existe nos blocos atômicos. O agente **preserva o arquivo** (estrutura, classes, CSS do bloco) e **só substitui conteúdo textual** e dados de integração (checkout, vídeo, imagens). **Não** transformar o bloco em outro layout, **não** trocar fontes ou cores do tema, **não** apagar seções para “simplificar”. Se o aluno quiser outro design de página inteira, usar o fluxo **3-alt** (exceção) ou evoluir **depois** do merge com `/pagina-ajuste` e o playbook de visual.

**Fluxo preferido (vendas 8D): copiar template, depois copy na cópia**

1. **Copiar o tema para a entrega** (antes de editar qualquer `code.html`): na raiz do repo, `py -3 scripts/workshop-copy-template-tema.py --tema {estilo}` (`{estilo}` = um dos cinco: `flat_claro`, `minimal_claro`, `glass_escuro`, `teal_claro`, `purple_escuro`). Usa `meus-produtos/.ativo` ou `--slug nome-do-produto`. Saída: `meus-produtos/{slug}/entregas/paginas/templates-{estilo}/` com todas as pastas `*_{estilo}` e `pagina_completa_{estilo}`. Se a pasta já existir, `--force` recopia do zero (**apaga** a cópia local já editada).
2. **Trabalhar só nos blocos atômicos da cópia:** editar **apenas** `meus-produtos/{slug}/entregas/paginas/templates-{estilo}/{nome_do_bloco}_{estilo}/code.html`. O texto vem de **`## Bloco NN`** em `copy-pagina/copy-{slug}.md` (B0). **Não** editar por padrão `.claude/plugins/.../references/templates/` (original do workshop; exceção: manutenção do plugin).
3. **Segunda prova social (atenção):**
   - Temas **flat_claro** e **minimal_claro:** o merge usa **duas vezes** o mesmo tipo de bloco de provas (`provas2` = mesma família do primeiro bloco). Conteúdo pode ser diferente, **formato** é o mesmo.
   - Temas **glass_escuro**, **teal_claro** e **purple_escuro:** o segundo bloco **não** é cópia do primeiro. Preencher também `hero_{estilo}_depoimentos/code.html` quando o `build_merge.py` do tema exigir.
4. **Fechar a página (merge):** na raiz do repositório (com a cópia já preenchida):
   ```bash
   py -3 scripts/workshop-merge-pagina.py --tema {estilo} --templates-root meus-produtos/{slug}/entregas/paginas/templates-{estilo} --copiar-entregas
   ```
   No Linux/macOS pode ser `python3` em vez de `py -3`. Usa `meus-produtos/.ativo` como slug do `vendas-{slug}.html`, salvo `--slug`.  
   **Sem cópia em entregas:** omitir `--templates-root` para mergear a partir do plugin (fluxo alternativo, não o padrão de entrega).  
   **Alternativa manual:** em `entregas/.../templates-{estilo}/pagina_completa_{estilo}/`, rodar `py -3 build_merge.py`, depois copiar `code.html` se não usar `--copiar-entregas`.
5. **Entrega ao aluno:** com `--copiar-entregas`, o HTML final vai para `meus-produtos/{slug}/entregas/paginas/vendas-{slug}.html`. Ajustes finais (título, meta, checkout, pixel) como na etapa de ajustes.

**Revisão de texto:** em cada bloco aplicar a **Etapa 0 (vícios proibidos)** do SKILL `paginas`. **Não** abrir o arquivo inteiro `.claude/commands/feedback-pagina.md` a cada seção (ele é pesado). Auditoria completa com Nav fica para quando o usuário usar `/feedback-pagina` ou pedir revisão profunda.

### 3. Geração (vendas 8D). Modo padrão: blocos atômicos + merge

> ⛔ **Não** montar um único HTML em `entregas/` colando seções em `<main id="page-sections">` (salvo exceção no §3-alt). **Não** gerar no chat o `pagina_completa_*/code.html` inteiro.  
> ⛔ **NUNCA** gere a página inteira de uma vez no chat. Trabalhe **bloco a bloco**, com aprovação opcional entre blocos (o usuário pode dizer "ir direto à versão final" para pular pausas).

**Base de caminhos (padrão):** `meus-produtos/{slug}/entregas/paginas/templates-{estilo}/` após `workshop-copy-template-tema.py`. **Original do plugin (só manutenção):** `.claude/skills/paginas/references/templates/`

**Ordem dos blocos** (igual ao `build_merge.py` do tema `pagina_completa_{estilo}`). Substitua `{estilo}` pelo sufixo escolhido (ex.: `flat_claro`):

| # | Fonte da copy (`copy-*.md`) | Pasta do bloco na **cópia** (`meus-produtos/{slug}/entregas/paginas/templates-{estilo}/{pasta}/code.html`) |
|---|-----------------------------|--------------------------------------------------------|
| 1 | `## Bloco 01 — Hero` | `hero_{estilo}` |
| 2 | `## Bloco 02 — Dor` | `dor_{estilo}` |
| 3 | `## Bloco 03 — Paliativo` | `paliativo_{estilo}` |
| 4 | `## Bloco 04 — Prova social (primeiro bloco)` | `provas_sociais_{estilo}` |
| 5 | `## Bloco 05 — CTA intermediário` | `cta_{estilo}` |
| 6 | `## Bloco 06 — Método (Furadeira)` | `metodo_{estilo}` |
| 7 | `## Bloco 07 — Para quem é / não é` | `para_quem_{estilo}` |
| 8 | `## Bloco 08 — Entregáveis` | `entregaveis_{estilo}` |
| 9 | `## Bloco 09 — Bônus` | `bonus_{estilo}` |
| 10 | `## Bloco 10 — Stack de valor` | `stack_valor_{estilo}` |
| 11 | `## Bloco 11 — Prova social (segundo bloco) ou Depoimentos` | **flat/minimal:** segundo `provas_sociais_{estilo}` · **glass/teal/purple:** `hero_{estilo}_depoimentos` |
| 12 | `## Bloco 12 — Suporte` | `suporte_{estilo}` |
| 13 | `## Bloco 13 — Garantia` | `garantia_{estilo}` |
| 14 | `## Bloco 14 — Autoridade do criador` | `autoridade_{estilo}` |
| 15 | `## Bloco 15 — FAQ` | `faq_{estilo}` |
| 16 | `## Bloco 16 — Oferta final` | `oferta_final_{estilo}` |

**Passo 3a. Antes do primeiro bloco:** garantir que existe `meus-produtos/{slug}/entregas/paginas/templates-{estilo}/` (rodar `workshop-copy-template-tema.py` se ainda não existir). Escolher o tema e anunciar: `Vou preencher os blocos na cópia em entregas/.../templates-[estilo], um por vez. Total: 16 blocos. Depois rodo o merge com --templates-root e entrego vendas-{slug}.html.`

**Passo 3b. Loop para cada bloco (1 a 16):**

1. Abrir `meus-produtos/{ativo}/entregas/copy-pagina/copy-{slug}.md` e localizar **`## Bloco NN — …`** com o mesmo número do bloco atual (01 a 16). **Exceção B0 opção 3:** usar só `perfil.md` + entrevista, sem arquivo de 16 blocos.
2. Abrir o `code.html` **da cópia** em `meus-produtos/{slug}/entregas/paginas/templates-{estilo}/{pasta}/code.html` (tabela abaixo com nomes de pasta). Manter o **mesmo** HTML e CSS do arquivo; não reescrever o esqueleto.
3. Preencher o template com o **texto daquela seção da copy**, sem acrescentar promessas, preços ou depoimentos que não estejam na copy aprovada. Etapas 4 e 5 do SKILL `paginas` só para encaixe visual. Etapa 0 (anti-vícios) **antes** de salvar.
4. **Salvar só esse arquivo atômico** (não um arquivo grande em `entregas/` ainda).
5. Resumo curto ao usuário (sem colar HTML no chat). **1. Aprovar próximo bloco** / **2. Ajustar este bloco** (ou "ir direto à versão final" para não pausar mais).

**Passo 3c. Após o bloco 16 salvo:**

1. Rodar o merge e copiar para entregas (ver B1.5, passos 4 e 5). Preferir: `py -3 scripts/workshop-merge-pagina.py --tema {estilo} --templates-root meus-produtos/{slug}/entregas/paginas/templates-{estilo} --copiar-entregas`
2. **Etapa de ajustes (pós-merge):** seguir `references/etapa-ajustes-pagina.md` no SKILL `paginas` (checkout, preço, vídeo, autoridade, `<title>` e meta description no HTML em `entregas/`, segunda prova social se duplicada pelo tema, rodapé). O merge pode recolocar placeholders do shell do tema; reaplicar ajustes sempre que rodar o merge de novo.
3. Checklist anti-vícios (Etapa 0 do SKILL `paginas`) no texto visível do arquivo em `entregas/`. Pixel só se o fluxo pedir (`/pagina-pixel`).

### 3-alt. Exceção (só se o usuário pedir layout fora dos cinco temas)

Montagem manual de um único arquivo em `entregas/` ou HTML totalmente customizado. **Custo de tokens maior.** Evitar se um dos temas `pagina_completa_*` servir.

### 4. Confirmação Final

Após merge, etapa de ajustes e confirmação em `entregas/`:

```
Página entregue no arquivo abaixo.

✅ Blocos atômicos preenchidos + merge (custo-benefício)
✅ Estilo [estilo] aplicado
✅ Etapa de ajustes pós-merge (etapa-ajustes-pagina.md): checkout, SEO básico, placeholders críticos
✅ Checklist anti-vícios (Etapa 0) no HTML final

Arquivo: meus-produtos/{ativo}/entregas/paginas/vendas-[produto].html (ou nome acordado)

Próximos passos opcionais: /feedback-pagina (auditoria), /pagina-performance, /pagina-pixel, /pagina-checkout
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

Antes de salvar o arquivo HTML, percorra o **texto visível** da página (ou de cada bloco, se estiver em modo seção a seção) e corrija vícios.

**Economia de tokens:** use **este checklist** e a Etapa 0 do SKILL `paginas`. **Não** carregue o arquivo inteiro `.claude/commands/feedback-pagina.md` só para salvar uma página (esse documento é longo e serve à **auditoria** quando o usuário chama `/feedback-pagina` ou pede análise tipo Nav). Se o usuário pedir revisão profunda no mesmo fluxo, aí sim use `feedback-pagina.md` com critério.

**Fonte única de regras:** aplicar a Etapa 0 do SKILL `paginas` + o checklist dos Blocos A/B/C/D do `.claude/skills/revisora/references/manual-copy.md` (travessão, "não é X é Y", imperativo, pergunta no gancho, promessa vaga, "mesmo que/sem precisar", produto no lead, emojis, lero-lero, cópia sem tese, sigla sem explicação, depoimento genérico, autoridade sem prova, bônus sem valor, seção sem headline, Quadro sem Decorado, dor só sintoma, emoção sem razão, AI slop).

Corrija diretamente no HTML:

- Travessão → reescreva a frase sem ele
- "Não é X. É Y." → desenvolva o argumento de outra forma
- Headline no imperativo → reescreva como premissa ou observação
- Pergunta no gancho → transforme em afirmação com tensão
- Promessa vaga → especifique com número, situação real ou nome próprio
- Produto no hero (nome do produto, método, curso ou sigla) → remova, o hero fala só do leitor
- Emojis no texto → remova sem substituição
- Bullets fora do padrão urgência oculta + decorado → reescreva
- Bloco de autoridade sem conquista concreta → adicione número, prazo ou situação verificável (ou "método testado com X pessoas" se for low ticket sem autoridade pessoal)
- Depoimento sem antes/depois/número → marque para substituição
- Bônus sem R$ individual → adicione valor
- Seção sem headline curiosa → crie headline
- Ausência de parágrafo técnico em itálico → adicione pelo menos um que ancora a emoção com razão

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

"Use `/copy-anuncio` para criar anúncios que levem tráfego a essa página."
