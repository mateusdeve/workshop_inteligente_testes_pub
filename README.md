# Workshop Inteligente. Assistente de Marketing IA

Toolkit completo de marketing digital, copy e infoprodutos baseado nas metodologias **VTSD (Venda Todo Santo Dia)**, **Light Copy**, **C10X (High Ticket)** e **Low Ticket**. Roda dentro do **Claude Code** (VS Code) ou no **Cursor**, transformando o chat em um consultor especialista que entrega materiais prontos para uso.

Não é software tradicional: é um sistema de prompts estruturados (CLAUDE.md, regras, comandos, agentes, skills e scripts) que orquestra o assistente do início ao fim de um funil.

## Por onde começar

| Arquivo | Para quê serve |
|---|---|
| `COMO-USAR.md` | Guia passo a passo para o usuário final. Inclui seção Cursor. |
| `CLAUDE.md` | Instruções e regras do assistente. Autoritativo, lido em toda conversa. |
| `AGENTS.md` | Mapa rápido para agentes de IDEs (Cursor, etc.) |
| `docs/ARQUITETURA.md` | Visão técnica da arquitetura. |
| `docs/diagnostico-projeto.md` | Diagnóstico e decisões de evolução. |
| `docs/processo-criativos.md` | Processo para geração de criativos. |
| `docs/setup-heygen.md` | Setup de vídeo com avatar IA. |
| `docs/setup-imagens.md` | Setup de geração de imagens para anúncios. |

## Onde roda

### Claude Code (VS Code)
Abra a pasta do projeto, instale a extensão Claude Code, use os slash commands `/copy-pagina`, `/lt-funil`, etc.

### Cursor
Abra a pasta com **File → Open Folder**. As regras em `.cursor/rules/` e o `CLAUDE.md` passam a orientar o chat. No Cursor, a barra `/` não é equivalente à do Claude Code. Para seguir um fluxo, diga no chat "segue o comando copy-pagina" ou anexe o arquivo `.claude/commands/copy-pagina.md` com `@`.

## Metodologias base

- **VTSD (Venda Todo Santo Dia).** Quadro (transformação), Furadeira (método), Decorados (50 benefícios), 3 Identidades (Comunicador, Consumidor, Produto), Urgências Ocultas (7 categorias x 10 itens = 70 itens por produto), Mandala da Criatividade (18 tipos de anúncio x 4 objetivos x 3 momentos), Estrutura 8D (11 seções de página de vendas), VVV (vídeo de vendas), 26 Elementos Literários.
- **Light Copy.** Argumentativa, lógica, conversacional, não óbvia. Proibições duras: travessão, ponto de exclamação, pergunta no gancho, "Não é X. É Y.", "mesmo que", "sem precisar", nome do produto no lead.
- **C10X (High Ticket).** Retiros online, webinar, pitch de palco, call SPIN, WhatsApp, proposta comercial, follow-up pós-evento.
- **Low Ticket.** Produto de entrada (R$37-97) com quiz ou página direta, desafio, agente GPT, copy para Hotmart/Kiwify, otimização de Ads.

## Regras absolutas de estilo

1. **Nada de travessão (—)** em nenhum texto gerado. Sem exceção.
2. **Português do Brasil** em tudo que é visível ao usuário.
3. **Nunca mostrar código HTML no chat.** Salvar silenciosamente e informar o caminho.
4. **Sempre pedir aprovação antes de salvar.** Resumo + opções numeradas.
5. **Uma pergunta por vez** nas entrevistas, com progresso visual entre blocos.
6. **Produto não aparece no lead.** Sem "curso", "treinamento", nome do produto ou sigla no início da copy.

Checklists completos (Copy Light Copy + Design HTML) estão no topo do `CLAUDE.md`.

## Arquitetura

5 tipos de componentes trabalham juntos:

| Componente | Local | Papel |
|---|---|---|
| **CLAUDE.md** | raiz | Persona, regras globais, fluxo padrão. Lido em toda conversa. |
| **Commands** | `.claude/commands/*.md` | Slash commands interativos (`/copy-pagina`, `/lt-funil`, etc.) |
| **Agents** | `.claude/agents/*.md` | Subprocessos autônomos (orquestradores e especialistas) |
| **Skills** | `.claude/plugins/workshop-marketing/skills/` | Base de conhecimento consultada por commands e agents |
| **Plugin** | `.claude/plugins/workshop-marketing/.claude-plugin/plugin.json` | Manifesto que registra as skills |

**Fluxo típico:**
```
Usuário digita /comando
  → Command carrega .md correspondente
  → Lê produtos/{ativo}/perfil.md e idconsumidor.md (contexto)
  → Consulta a skill relevante (conhecimento)
  → Roda entrevista (perguntas uma por vez)
  → Pede aprovação
  → Salva em produtos/{ativo}/entregas/[tipo]/
  → Sugere próximo comando
```

## Estrutura de pastas

```
workshop_inteligente/
├── CLAUDE.md                    Regras e papel do assistente (autoritativo)
├── AGENTS.md                    Mapa para IDEs
├── COMO-USAR.md                 Guia passo a passo
├── README.md                    Este arquivo
├── painel.html                  Painel global de visualização dos produtos
│
├── .claude/                     Núcleo do assistente
│   ├── commands/                Slash commands (60+ arquivos .md)
│   ├── agents/                  Agentes orquestradores e especialistas
│   ├── plugins/
│   │   └── workshop-marketing/
│   │       ├── .claude-plugin/plugin.json
│   │       └── skills/          Base de conhecimento (vtsd-completo, paginas, anuncios, etc.)
│   └── settings.json            Permissões
│
├── .cursor/rules/               Regras específicas do Cursor (.mdc)
│
├── docs/                        Documentação técnica e histórico
│   ├── ARQUITETURA.md
│   ├── diagnostico-projeto.md
│   ├── processo-criativos.md
│   ├── setup-heygen.md
│   ├── setup-imagens.md
│   └── historico/               Registro cronológico de decisões
│
├── scripts/                     Utilitários Python e PowerShell
│   ├── workshop-copy-template-tema.py    Copia tema para a pasta do produto
│   ├── workshop-merge-pagina.py          Faz o merge dos blocos 8D em um HTML final
│   ├── generate-avatar-video.py          Aciona HeyGen via API
│   ├── generate-creative.py              Geração de criativos visuais
│   ├── generate-openrouter-nano-banana-images.py
│   ├── openrouter_model_router.py
│   ├── painel-atualizar.py               Atualiza o painel global
│   ├── relatorio-ads.ps1                 Rotina diária de relatório Facebook Ads
│   └── creative-templates/
│
├── meus-produtos/               Produtos cadastrados (fora do git)
│   ├── .ativo                   Slug do produto ativo
│   ├── index.js
│   └── {slug-do-produto}/
│       ├── perfil.md            Quadro, Furadeira, Decorados, Urgências
│       ├── idconsumidor.md      Identidade do consumidor
│       └── entregas/            Output do assistente (por produto)
│           ├── paginas/         HTML de vendas, captura, obrigado
│           ├── copy-pagina/     Copy markdown por bloco
│           ├── emails/          Sequências de email
│           ├── anuncios/        Pacotes de anúncios
│           ├── conteudo-social/ Posts, carrosséis, Reels
│           ├── criativos/       Prompts de imagem e referências
│           ├── comercial/       Scripts de venda 1:1 (HTML)
│           ├── videos/          HeyGen, Remotion, roteiros
│           └── produto/         E-book, checklist, mini-curso final
│
├── _prompts-gpt/                Referência original (não distribui)
├── package.json
├── vercel.json
└── .env.example                 Modelo de chaves de API
```

Observação: a pasta `meus-produtos/` (e `produtos/` legado) contém os dados de cada aluno e não sobe para o git.

## Comandos disponíveis

### Produto
`/produto-novo`, `/produto-concepcao`, `/produto-consumidor`, `/produto-trocar`, `/produto-excluir`, `/produto-zerar`

### Copy
`/copy-pagina`, `/copy-anuncio`, `/copy-social`, `/copy-roteiro`, `/copy-emails`, `/elementos-literarios`

### Imagem e vídeo
`/img-anuncio`, `/imagem-prompt`, `/criativo-de-imagem`, `/avat-whisk`, `/furadeira-visual`, `/video-heygen`, `/video-remotion`, `/video-editar`

### Low Ticket
`/lt-funil`, `/lt-criar-produto`, `/lt-quiz`, `/lt-pagina`, `/lt-otimizar`

### High Ticket (C10X)
`/ht-big-idea`, `/ht-oferta`, `/ht-pagina-inscricao`, `/ht-cronograma`, `/ht-conteudo`, `/ht-pitch-palco`, `/ht-comunicacao-pre`, `/ht-anuncios`, `/ht-spin`, `/ht-fechamento`, `/ht-objecoes`, `/ht-whatsapp`, `/ht-follow-up`, `/ht-diagnostico`, `/ht-proposta`, `/ht-apresentacao-proposta`, `/ht-onboarding`, `/ht-repitch`

### Estratégia
`/estrategia-funil`, `/estrategia-lancamento`

### Comercial
`/comercial-playbook`

### Infraestrutura de página (após gerar o HTML)
`/pagina-ajuste`, `/pagina-performance`, `/pagina-pixel`, `/pagina-checkout`, `/pagina-active`, `/pagina-precheckout`, `/pagina-lovable`, `/pagina-vercel`

### Feedback e auditoria
`/feedback-pagina`, `/feedback-low-ticket`, `/feedback-de-pv`

### Toolkit (projetos estruturados)
`/toolkit-novo`, `/toolkit-planejar`, `/toolkit-executar`, `/toolkit-verificar`, `/toolkit-progresso`, `/toolkit-anotar`, `/toolkit-pausar`, `/toolkit-retomar`

Fluxo proprietário para conduzir projetos grandes (lançamento, funil completo, reestruturação). Quebra o objetivo em etapas, aciona as skills certas uma a uma e mantém o estado em `meus-produtos/{ativo}/projeto/{slug}/` entre sessões. Não use para tarefa simples de uma skill só.

### Dados e automações
`/ads-relatorio`, `/enviar-relatorio-ads`, `/instagram-dashboard`, `/dados-instagram`, `/app-saas`, `/criar-gpt`

### Configuração de integrações
`/configurar-apify`, `/configurar-zapi`, `/gerar-token-permanente-facebook-ads`, `/obter-id-conta-anuncios`, `/criar-aplicativo-analise-ads`

A lista completa com descrições está no `CLAUDE.md`.

## Agentes especialistas

Orquestradores autônomos que executam tarefas completas acionando múltiplas skills:

- `estrategista-de-produto`. Sessão completa de concepção VTSD.
- `estrategista-low-ticket`. Funil low ticket do zero à página publicável.
- `estrategista-middle-ticket`. Funil perpétuo de produto principal.
- `estrategista-ht`. Funil High Ticket C10X completo.
- `construtor-de-paginas`. Páginas profissionais do zero.
- `criador-de-campanhas`. Campanha de tráfego completa.
- `produtor-de-conteudo`. Plano de conteúdo e roteiros.
- `consultor-comercial`. Playbook comercial 1:1.
- `copywriter`. Orquestrador de copy (página, anúncio, email, roteiro, social).
- `video-maker`. Orquestrador de produção de vídeo.
- `executor-de-plano-de-acao`. Executa plano de ação acionando skills e agentes.

Além dos agentes GSD (`gsd-*`) que compõem a metodologia Get Shit Done para tarefas complexas multi-etapas.

## Skills (base de conhecimento)

Dentro de `.claude/plugins/workshop-marketing/skills/`:

- `vtsd-completo/`. Metodologia VTSD integral.
- `concepcao-produto/`. Quadro, Furadeira, 3 Identidades, Urgências Ocultas.
- `paginas/`. Estrutura 8D, design system, referências de blocos atômicos, etapa de ajustes pós-merge.
- `anuncios/`, `anuncios-texto/`, `anuncios-video/`. Mandala, formatos Meta Ads e Google Ads.
- `conteudo/`. Frameworks de copy, gatilhos, exemplos de VSL.
- `trafego-pago/`. Pixel, métricas, campanhas.
- `playbook-comercial/`. SPIN Selling, fechamento, objeções.
- `ferramentas/`. Integrações externas.

Skills não são acionadas pelo usuário: são consultadas pelos commands e agents quando precisam de conhecimento especializado.

## Scripts principais

### Páginas de vendas (fluxo 8D)
```
py -3 scripts/workshop-copy-template-tema.py --tema flat_claro
py -3 scripts/workshop-merge-pagina.py --tema flat_claro \
     --templates-root entregas/{ativo}/paginas/templates-flat_claro \
     --copiar-entregas
```
O primeiro copia o tema inteiro para a pasta do produto. O segundo mescla os blocos preenchidos num HTML final. Detalhes no command `copy-pagina` e na skill `paginas`.

### Geração de vídeo e imagens
- `scripts/generate-avatar-video.py`. HeyGen via API.
- `scripts/generate-creative.py` e `generate-openrouter-nano-banana-images.py`. Criativos via OpenRouter.

### Relatório diário de Ads
- `scripts/relatorio-ads.ps1`. Busca métricas do Facebook Ads e envia no WhatsApp via Z-API, agendado na nuvem do Claude.

### Painel
- `scripts/painel-atualizar.py`. Regenera `painel.html` com os produtos cadastrados em `meus-produtos/`.

## Integrações externas (opcionais)

Configuradas via `.env` (veja `.env.example`):

| Integração | Finalidade | Comando de setup |
|---|---|---|
| Facebook Marketing API | Relatório diário de Ads, otimização low ticket | `/gerar-token-permanente-facebook-ads`, `/criar-aplicativo-analise-ads` |
| Z-API | Envio de mensagens WhatsApp automatizadas | `/configurar-zapi` |
| Apify | Coleta de dados do Instagram | `/configurar-apify` |
| HeyGen | Vídeo com avatar IA | `docs/setup-heygen.md` |
| OpenRouter | Geração de imagens via nano-banana | `docs/setup-imagens.md` |
| Lovable / Vercel | Publicação de páginas | `/pagina-lovable`, `/pagina-vercel` |
| Hotmart, Kiwify, Eduzz, Cakto, Pepper, Stripe | Checkout das páginas | `/pagina-checkout` |
| ActiveCampaign | Lista de leads e automação de email | `/pagina-active` |

## Fluxos recomendados

### Começar a vender
1. `/produto-novo` ou `/produto-concepcao`
2. `/produto-consumidor`
3. `/copy-pagina`
4. `/copy-anuncio`

### Lançamento
1. `/produto-concepcao`
2. `/estrategia-lancamento`
3. `/copy-pagina` (evento + vendas)
4. `/copy-emails`
5. `/copy-anuncio`
6. `/copy-social`

### Perpétuo
1. `/produto-concepcao`
2. `/estrategia-funil`
3. `/copy-pagina` (captura + vendas + obrigado)
4. `/copy-emails` (nutrição)
5. `/copy-anuncio`

### Low Ticket
1. `/produto-concepcao`
2. `/lt-funil`
3. `/lt-criar-produto` (e-book, checklist, agente GPT)
4. `/lt-pagina` ou `/lt-quiz`
5. `/copy-anuncio` (formatos low ticket)
6. `/lt-otimizar` (com planilha do Gerenciador)

### High Ticket C10X
1. `/ht-big-idea`
2. `/ht-oferta`
3. `/ht-pagina-inscricao`
4. `/ht-comunicacao-pre`
5. `/ht-cronograma` e `/ht-conteudo`
6. `/ht-pitch-palco`
7. `/ht-spin`, `/ht-fechamento`, `/ht-objecoes`, `/ht-whatsapp`
8. `/ht-follow-up`

## Fluxo padrão de qualquer comando (6 passos)

1. **Contexto.** Ler `meus-produtos/.ativo`, depois `perfil.md` e `idconsumidor.md`.
2. **Entrevista.** 3 a 5 perguntas, uma por vez, com progresso visual.
3. **Confirmação.** Resumo do que vai criar, pedir OK numerado.
4. **Geração.** Criar o entregável aplicando a metodologia VTSD.
5. **Aprovação.** Mostrar o resultado e perguntar `1. Aprovar e salvar / 2. Ajustar`.
6. **Entrega.** Salvar, informar caminho, sugerir próximo comando.

## O que sobe para o git

**Sobe:** `.claude/commands/`, `.claude/agents/`, `.claude/plugins/`, `.claude/settings.json`, `CLAUDE.md`, `AGENTS.md`, `README.md`, `COMO-USAR.md`, `.env.example`, `docs/`, `scripts/`, `painel.html`.

**Não sobe:** `.env`, `meus-produtos/` (dados do aluno), `_prompts-gpt/` (referência interna), `.claude/projects/` e demais arquivos de runtime.

## Adicionando novas capacidades

Para criar um novo command, agent, skill ou integração, siga o guia completo em `docs/ARQUITETURA.md` (seções 5 a 8). Inclui frontmatter obrigatório, checklist e exemplo completo de como adicionar suporte a um novo domínio (ex: webinars).
