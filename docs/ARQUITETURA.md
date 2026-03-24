# Arquitetura do Repositorio — Guia Tecnico Completo

Este documento explica como o repositorio `workshop_inteligente` esta estruturado e como inserir novas capacidades (commands, agents, skills, ferramentas). Escrito para ser lido por humanos e LLMs que precisem entender, manter ou expandir o projeto.

---

## 1. Visao Geral do Projeto

Este repositorio e um **toolkit de marketing digital para infoprodutores** que roda dentro do **Claude Code** (extensao do VSCode). Nao e um projeto de software tradicional com codigo executavel — e um sistema de prompts estruturados que transforma o Claude em um consultor de marketing.

**Stack:**
- Claude Code (extensao VSCode) como runtime
- Arquivos Markdown como instrucoes (prompts)
- HTML/CSS como output (paginas de vendas)
- Metodologia VTSD (Venda Todo Santo Dia) como base de conhecimento

**O que o toolkit produz:**
- Paginas de vendas, captura e obrigado (HTML)
- Textos persuasivos (copy, headlines, VSL)
- Anuncios para Meta Ads e Google Ads
- Conteudo para redes sociais (carrosseis, Reels)
- Scripts comerciais (SPIN Selling)
- Sequencias de email
- Roteiros de video

---

## 2. Mapa Completo de Arquivos

```
workshop_inteligente/
│
├── CLAUDE.md                              ← ARQUIVO CENTRAL: define persona, regras e comportamento
├── README.md                              ← Documentacao publica para o usuario final
├── COMO-USAR.md                           ← Guia passo a passo para o usuario
├── .env.example                           ← Modelo de chaves API (opcional)
├── .gitignore                             ← Protege .env, entregas/ e dados do aluno
│
├── .claude/                               ← NUCLEO DO SISTEMA Claude Code
│   ├── settings.json                      ← Permissoes de escrita/leitura/execucao
│   │
│   ├── commands/                          ← SLASH COMMANDS (atalhos /comando)
│   │   ├── meu-produto.md                 ← /meu-produto
│   │   ├── persona.md                     ← /persona
│   │   ├── pagina-de-vendas.md            ← /pagina-de-vendas
│   │   ├── texto-de-venda.md              ← /texto-de-venda
│   │   ├── anuncio.md                     ← /anuncio
│   │   ├── conteudo-social.md             ← /conteudo-social
│   │   ├── roteiro-de-video.md            ← /roteiro-de-video
│   │   ├── sequencia-de-emails.md         ← /sequencia-de-emails
│   │   ├── lancamento.md                  ← /lancamento
│   │   ├── funil-de-vendas.md             ← /funil-de-vendas
│   │   ├── playbook-comercial.md          ← /playbook-comercial
│   │   ├── criativo-de-imagem.md          ← /criativo-de-imagem
│   │   └── low-ticket.md                  ← /low-ticket
│   │
│   ├── agents/                            ← AGENTES AUTONOMOS (subprocessos)
│   │   ├── estrategista-de-produto.md     ← Concepcao VTSD completa
│   │   ├── construtor-de-paginas.md       ← Cria paginas HTML
│   │   ├── criador-de-campanhas.md        ← Monta campanha de trafego
│   │   ├── produtor-de-conteudo.md        ← Plano de conteudo 30 dias
│   │   └── consultor-comercial.md         ← Playbook de vendas high ticket
│   │
│   ├── plugins/
│   │   └── workshop-marketing/            ← PLUGIN PRINCIPAL
│   │       ├── .claude-plugin/
│   │       │   └── plugin.json            ← Manifesto do plugin (nome, versao, skills)
│   │       │
│   │       └── skills/                    ← BASE DE CONHECIMENTO (referencia)
│   │           ├── vtsd-completo/
│   │           │   └── SKILL.md           ← Metodologia VTSD integral (1084 linhas)
│   │           ├── concepcao-produto/
│   │           │   ├── SKILL.md           ← Quadro, Furadeira, 3 Identidades
│   │           │   └── references/
│   │           │       └── template-avatar.md
│   │           ├── paginas/
│   │           │   ├── SKILL.md           ← Estrutura 8D, paletas, padrao HTML
│   │           │   └── references/
│   │           │       └── estruturas-pagina.md
│   │           ├── anuncios/
│   │           │   ├── SKILL.md           ← Mandala 18 tipos
│   │           │   └── references/
│   │           │       ├── exemplos-criativos.md
│   │           │       ├── formatos-meta-ads.md
│   │           │       └── formatos-google-ads.md
│   │           ├── anuncios-texto/
│   │           │   └── SKILL.md           ← Anuncios em formato texto
│   │           ├── anuncios-video/
│   │           │   └── SKILL.md           ← Anuncios em formato video
│   │           ├── conteudo/
│   │           │   ├── SKILL.md           ← Formatos Reels, carrosseis, elementos literarios
│   │           │   └── references/
│   │           │       ├── exemplos-vsl.md
│   │           │       ├── frameworks-copy.md
│   │           │       └── gatilhos-mentais.md
│   │           ├── trafego-pago/
│   │           │   └── SKILL.md           ← Campanhas, pixel, metricas
│   │           ├── playbook-comercial/
│   │           │   └── SKILL.md           ← SPIN Selling, fechamento
│   │           └── ferramentas/
│   │               └── SKILL.md           ← Integracoes externas (Vercel, Freepik, etc.)
│   │
│   └── settings.json                      ← Permissoes do Claude Code
│
├── meu-negocio/                           ← DADOS DO USUARIO (nao sobe pro git)
│   ├── README.md                          ← Instrucoes para o usuario
│   ├── perfil.md                          ← Gerado por /meu-produto (Quadro, Furadeira, etc.)
│   └── persona.md                         ← Gerado por /persona (cliente ideal)
│
├── entregas/                              ← OUTPUT GERADO (nao sobe pro git)
│   ├── paginas/                           ← Arquivos .html
│   ├── textos-de-venda/                   ← Arquivos .md
│   ├── emails/                            ← Arquivos .md
│   ├── anuncios/                          ← Arquivos .md
│   ├── conteudo-social/                   ← Arquivos .md
│   ├── criativos/                         ← Arquivos .md (prompts de imagem)
│   └── comercial/                         ← Arquivos .md (scripts de venda)
│
├── docs/                                  ← DOCUMENTACAO INTERNA
│   ├── diagnostico-projeto.md             ← Auditoria do estado atual
│   └── ARQUITETURA.md                     ← ESTE ARQUIVO
│
└── _prompts-gpt/                          ← REFERENCIA ORIGINAL (nao distribui)
    ├── vtsd-completo.skill                ← Prompt original do GPT
    └── vtsd-extraido/                     ← Versao extraida para conversao
```

---

## 3. Conceitos Fundamentais

O sistema usa 5 tipos de componentes. Cada um tem um papel especifico:

### 3.1 CLAUDE.md (Role — Persona do Assistente)

**O que e:** Arquivo raiz que define QUEM o Claude e neste projeto. E carregado automaticamente em TODA conversa.

**O que contem:**
- Idioma (Portugues do Brasil)
- Persona (consultor de marketing, nao programador)
- Regras de comportamento (perguntar antes de gerar, Light Copy, nunca mostrar codigo)
- Padrao de UX da entrevista (perguntas numeradas, progresso visual, confirmacao)
- Metodologia base (VTSD — Quadro, Furadeira, Decorados, etc.)
- Contexto persistente (onde ler perfil.md e persona.md)
- Tabela de onde salvar cada tipo de entrega
- Padrao de qualidade para HTML
- Fluxo padrao de 5 passos (Contexto, Entrevista, Confirmacao, Geracao, Entrega)
- Lista de todos os comandos disponiveis (apresentacao na primeira interacao)

**Impacto:** Tudo que esta aqui afeta TODOS os comandos e agentes. Alteracoes neste arquivo mudam o comportamento global.

### 3.2 Commands (Slash Commands — `/comando`)

**O que sao:** Atalhos que o usuario digita no chat (ex: `/meu-produto`, `/anuncio`). Cada command e um arquivo `.md` na pasta `.claude/commands/`.

**Como o Claude Code encontra:** Automaticamente — qualquer `.md` dentro de `.claude/commands/` vira um slash command. O nome do arquivo (sem extensao) e o nome do comando.

**Como funciona na pratica:**
1. Usuario digita `/persona` no chat
2. Claude Code carrega `.claude/commands/persona.md`
3. O conteudo do arquivo e injetado como instrucao no contexto do Claude
4. O Claude segue as instrucoes do command + as regras do CLAUDE.md

### 3.3 Agents (Agentes Autonomos)

**O que sao:** Subprocessos especializados que executam tarefas complexas de forma autonoma, sem interacao do usuario. Cada agent e um arquivo `.md` na pasta `.claude/agents/`.

**Diferenca entre Command e Agent:**
- **Command:** Conversa interativa. O Claude faz perguntas, espera respostas, gera o material passo a passo.
- **Agent:** Autonomo. Recebe a tarefa, le os arquivos necessarios, executa tudo sozinho e entrega o resultado final.

**Como o Claude Code encontra:** Automaticamente — qualquer `.md` dentro de `.claude/agents/` fica disponivel como agente.

**Como funciona na pratica:**
1. O CLAUDE.md ou outro command aciona o agente pelo nome
2. Claude Code cria um subprocesso com o conteudo do agent como instrucao
3. O agente executa autonomamente (le arquivos, gera output, salva)
4. Retorna o resultado para a conversa principal

### 3.4 Skills (Base de Conhecimento)

**O que sao:** Documentos de referencia que contem conhecimento especializado. Ficam em `.claude/plugins/workshop-marketing/skills/`. NAO sao acionados diretamente pelo usuario — sao consultados pelos commands e agents.

**Estrutura de uma skill:**
```
skills/
└── nome-da-skill/
    ├── SKILL.md              ← Documento principal (obrigatorio)
    └── references/           ← Material de apoio (opcional)
        ├── exemplos.md
        └── templates.md
```

**Relacao com commands/agents:** Os commands e agents referenciam as skills nos seus textos (ex: "Leia `.claude/plugins/workshop-marketing/skills/paginas/SKILL.md`"). A skill fornece o conhecimento; o command/agent fornece o fluxo de trabalho.

### 3.5 Plugin (Empacotamento)

**O que e:** O plugin (`plugin.json`) e o manifesto que registra as skills no Claude Code. Fica em `.claude/plugins/workshop-marketing/.claude-plugin/plugin.json`.

**Conteudo atual:**
```json
{
  "name": "workshop-marketing",
  "description": "Assistente completo de marketing digital...",
  "version": "1.0.0",
  "author": { "name": "Workshop Marketing IA" },
  "skills": "./skills"
}
```

O campo `"skills": "./skills"` aponta para a pasta de skills relativa ao `plugin.json`.

---

## 4. Fluxo de Dados entre Componentes

```
USUARIO
  │
  ├── digita /comando ──────────► COMMAND (.claude/commands/X.md)
  │                                  │
  │                                  ├── le ► meu-negocio/perfil.md (contexto do produto)
  │                                  ├── le ► meu-negocio/persona.md (contexto do publico)
  │                                  ├── consulta ► SKILL (base de conhecimento)
  │                                  │
  │                                  └── salva ► entregas/[tipo]/[arquivo]
  │
  └── (ou agente e acionado) ───► AGENT (.claude/agents/X.md)
                                     │
                                     ├── le ► meu-negocio/perfil.md
                                     ├── le ► meu-negocio/persona.md
                                     ├── consulta ► SKILL (base de conhecimento)
                                     ├── le ► .env (chaves opcionais)
                                     │
                                     └── salva ► entregas/[tipo]/[arquivo]
```

**Ordem recomendada de uso:**
1. `/meu-produto` → gera `meu-negocio/perfil.md`
2. `/persona` → gera `meu-negocio/persona.md`
3. Qualquer outro comando → le perfil.md e persona.md como contexto

---

## 5. Como Adicionar um Novo COMMAND (Slash Command)

### Passo 1 — Criar o arquivo

Crie um arquivo `.md` em `.claude/commands/` com o nome do comando.

**Exemplo:** Para criar o comando `/webinar`, crie `.claude/commands/webinar.md`.

### Passo 2 — Estrutura obrigatoria do arquivo

```markdown
---
name: workshop-marketing:webinar
description: Criar estrutura completa de webinar — roteiro, slides, CTA e follow-up.
---

# Webinar — Estrutura Completa

Cria roteiro de webinar com [descricao do que faz].

## Usage

```
/webinar
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md`. Se nao existir, oriente a usar `/meu-produto` primeiro.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/N — [Tema]:**

Pergunta 1:
```
[Pergunta com opcoes numeradas OU pergunta aberta com exemplo]
```

[... mais perguntas ...]

```
--- Bloco 1/N concluido ---
[Resumo do que foi coletado]
Proximo: [nome do proximo bloco]
---
```

### 3. Confirmacao
```
Resumo do que vou criar:
- [item 1]
- [item 2]
- [item 3]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 4. Gerar Entregavel
[Instrucoes detalhadas de como gerar o material]
Salvar em `entregas/[pasta]/[nome-arquivo].md`

### 5. Proximo Passo
"Material salvo em [caminho]. Use `/[proximo-comando]` para [proxima acao sugerida]."
```

### Passo 3 — Frontmatter obrigatorio

O frontmatter YAML no topo do arquivo deve conter:

| Campo | Formato | Exemplo |
|---|---|---|
| `name` | `workshop-marketing:[nome]` | `workshop-marketing:webinar` |
| `description` | Frase que descreve o que o comando faz | `Criar estrutura completa de webinar...` |

### Passo 4 — Seguir o padrao de UX

Conforme definido no CLAUDE.md, TODOS os commands devem seguir:
- Perguntas com opcoes sempre numeradas
- Perguntas abertas com exemplo entre parenteses
- Progresso entre blocos (ex: `--- Bloco 2/6 concluido ---`)
- Confirmacao com resumo antes de gerar
- UMA pergunta por mensagem (nunca duas)

### Passo 5 — Referenciar skills quando necessario

Se o command precisa de conhecimento especializado, adicione no final:

```markdown
## Referencias
ANTES de gerar, leia:
- `.claude/plugins/workshop-marketing/skills/[skill-relevante]/SKILL.md`
```

### Passo 6 — Registrar no CLAUDE.md

Adicione o novo comando na lista de comandos disponiveis na secao "Primeira Interacao" do CLAUDE.md, na categoria adequada.

### Passo 7 — Registrar no README.md e COMO-USAR.md

Adicione o comando nas tabelas de comandos disponiveis desses arquivos.

### Checklist de um novo command:

- [ ] Arquivo `.md` criado em `.claude/commands/`
- [ ] Frontmatter com `name` e `description`
- [ ] Secao `Usage` com o comando
- [ ] Passo 1: Contexto (ler perfil.md)
- [ ] Passo 2: Entrevista (perguntas uma por vez, com progresso)
- [ ] Passo 3: Confirmacao (resumo + opcoes 1/2)
- [ ] Passo 4: Geracao (instrucoes detalhadas)
- [ ] Passo 5: Entrega (salvar + sugerir proximo comando)
- [ ] Referencia a skills relevantes
- [ ] Registrado no CLAUDE.md (lista de comandos)
- [ ] Registrado no README.md
- [ ] Registrado no COMO-USAR.md

---

## 6. Como Adicionar um Novo AGENT (Agente Autonomo)

### Passo 1 — Criar o arquivo

Crie um arquivo `.md` em `.claude/agents/` com o nome do agente (kebab-case).

**Exemplo:** `.claude/agents/planejador-de-webinar.md`

### Passo 2 — Estrutura obrigatoria do arquivo

```markdown
---
name: planejador-de-webinar
description: Agente autonomo que cria estrutura completa de webinar — roteiro, slides, CTA e follow-up. Le o perfil do negocio e gera tudo sem intervencao.
tools: Read, Write, Edit
model: sonnet
---

# Planejador de Webinar — Agente Autonomo

Voce e um [especialidade]. Seu papel e [objetivo].

## Idioma
SEMPRE em Portugues do Brasil.

## Sua Missao
[Descricao clara do que o agente deve produzir]

## Como Trabalhar

### 1. Ler Contexto
- Leia `meu-negocio/perfil.md` para entender o produto
- Leia `meu-negocio/persona.md` para entender o publico
- Use Quadro, Furadeira, Decorados e Urgencias Ocultas como base

### 2. [Etapa especifica do agente]
[Instrucoes detalhadas]

### 3. [Outra etapa]
[Instrucoes detalhadas]

### N. Salvar
- Salvar em `entregas/[pasta]/[nome-arquivo].[extensao]`

### N+1. Informar
NUNCA mostre codigo ao aluno.
Sugira: "Use `/[proximo-comando]` para [proxima acao]."

## Referencias
ANTES de gerar, leia:
- `.claude/plugins/workshop-marketing/skills/[skill]/SKILL.md`
```

### Passo 3 — Frontmatter obrigatorio

| Campo | Formato | Obrigatorio | Descricao |
|---|---|---|---|
| `name` | kebab-case | Sim | Nome unico do agente |
| `description` | Texto descritivo | Sim | O que o agente faz (aparece na listagem) |
| `tools` | Lista separada por virgula | Sim | Ferramentas que o agente pode usar |
| `model` | `sonnet`, `opus`, `haiku` | Nao | Modelo a ser usado (padrao: herda do pai) |

**Tools disponiveis para agents:**
- `Read` — Ler arquivos do projeto
- `Write` — Criar novos arquivos
- `Edit` — Editar arquivos existentes

A maioria dos agents usa `tools: Read, Write, Edit`.

### Passo 4 — Diferenca de design: Command vs Agent

| Aspecto | Command | Agent |
|---|---|---|
| Interatividade | Conversa com o usuario | Autonomo, sem interacao |
| Perguntas | 3-5 perguntas, uma por vez | No maximo 1-2 antes de executar |
| Fluxo | 5 passos (contexto, entrevista, confirmacao, geracao, entrega) | Le contexto e executa direto |
| Complexidade | Tarefa unica e focada | Tarefa completa multi-etapa |
| Quando usar | Usuario quer controle | Usuario quer resultado rapido |

### Passo 5 — Registrar no CLAUDE.md

Adicione o agente na secao "Agentes Especialistas" da lista de comandos no CLAUDE.md.

### Checklist de um novo agent:

- [ ] Arquivo `.md` criado em `.claude/agents/`
- [ ] Frontmatter com `name`, `description`, `tools`
- [ ] Instrucoes de leitura de contexto (perfil.md, persona.md)
- [ ] Etapas claras de execucao
- [ ] Instrucoes de onde salvar o output
- [ ] Referencia a skills relevantes
- [ ] Regra "nunca mostrar codigo"
- [ ] Registrado no CLAUDE.md

---

## 7. Como Adicionar uma Nova SKILL (Base de Conhecimento)

### Passo 1 — Criar a pasta e o arquivo

Crie uma pasta em `.claude/plugins/workshop-marketing/skills/` com o nome da skill (kebab-case).
Dentro dela, crie `SKILL.md` (obrigatorio, com esse nome exato).

**Exemplo:**
```
.claude/plugins/workshop-marketing/skills/webinars/
├── SKILL.md
└── references/           ← opcional
    └── exemplos-webinar.md
```

### Passo 2 — Estrutura do SKILL.md

```markdown
---
name: webinars
description: >
  Base de conhecimento para criacao de webinars.
  Inclui estrutura de roteiro, formatos de apresentacao e CTAs.
  Acionada pelo command /webinar e agent planejador-de-webinar.
---

# Webinars — Base de Conhecimento

## [Topico 1]
[Conteudo de referencia detalhado]

## [Topico 2]
[Conteudo de referencia detalhado]

## [Topico N]
[Conteudo de referencia detalhado]
```

### Passo 3 — Frontmatter obrigatorio

| Campo | Formato | Descricao |
|---|---|---|
| `name` | kebab-case | Nome unico da skill |
| `description` | Texto multi-linha (use `>`) | Descricao detalhada — IMPORTANTE: inclua palavras-chave que ativam a skill e quais commands/agents a usam |

### Passo 4 — Pasta `references/` (opcional)

Use para material de apoio volumoso que nao cabe no SKILL.md principal:
- Exemplos de copy
- Templates HTML
- Listas de formatos
- Dados de referencia

**Convencao de nomes:** kebab-case, descritivo. Ex: `exemplos-criativos.md`, `formatos-meta-ads.md`.

### Passo 5 — Conectar com commands/agents

Adicione referencia na secao `## Referencias` dos commands e agents que precisam dessa skill:

```markdown
## Referencias
ANTES de gerar, leia:
- `.claude/plugins/workshop-marketing/skills/webinars/SKILL.md`
```

### Principios para boas skills:

1. **Conteudo de referencia, nao instrucao.** A skill contem CONHECIMENTO (o que sao os 18 tipos de anuncio). O command/agent contem INSTRUCAO (como conduzir a entrevista e gerar o output).
2. **Atomica.** Uma skill = um dominio de conhecimento. Nao misture anuncios com paginas.
3. **Completa.** Tudo que o Claude precisa saber sobre o tema deve estar na skill ou nos references.
4. **Sem duplicacao.** Se a informacao ja esta em outra skill, referencie em vez de copiar.

---

## 8. Como Adicionar uma Nova Ferramenta/Integracao

### Passo 1 — Adicionar chave no .env.example

Siga o padrao existente:

```bash
# ══════════════════════════════════════════
# NOME_DA_FERRAMENTA — Descricao curta
# ══════════════════════════════════════════
# Usado por: /comando, agent nome-do-agente
# Obter em: https://url-para-obter-chave
NOME_DA_CHAVE=
```

### Passo 2 — Documentar na skill de ferramentas

Adicione a nova ferramenta em `.claude/plugins/workshop-marketing/skills/ferramentas/SKILL.md` seguindo o padrao:

```markdown
### Nome da Ferramenta — Descricao

**O que faz:** [descricao funcional]
**Usada por:** [lista de commands e agents]
**Chave necessaria:** `NOME_DA_CHAVE`

**Como configurar:**
1. [passo 1]
2. [passo 2]

**Como o toolkit usa:**
[explicacao de como o Claude usa a ferramenta]

**Sem a chave:** [comportamento fallback]
```

### Passo 3 — Atualizar commands/agents que usam a ferramenta

Adicione a logica de verificacao de chave no command ou agent:

```markdown
### N. Integracao com [Ferramenta] (se configurado)
Apos [acao], leia `.env` e verifique se existe `NOME_DA_CHAVE`.
Se existir, [acao automatizada].
Se nao existir, informe: "[fallback manual]."
```

### Passo 4 — Atualizar permissoes se necessario

Se a ferramenta requer execucao de comandos bash, adicione a permissao em `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(nome-ferramenta *)"
    ]
  }
}
```

---

## 9. settings.json — Permissoes

O arquivo `.claude/settings.json` controla quais acoes o Claude Code pode executar sem pedir confirmacao ao usuario.

**Estrutura atual:**
```json
{
  "permissions": {
    "allow": [
      "Write(entregas/**)",        ← Pode criar/editar arquivos em entregas/
      "Write(meu-negocio/**)",     ← Pode criar/editar perfil.md e persona.md
      "Write(docs/**)",            ← Pode criar/editar documentacao
      "Read(**)",                  ← Pode ler qualquer arquivo
      "Bash(ls *)",               ← Pode listar arquivos
      "Bash(cat .env)",           ← Pode ler chaves de API
      "Bash(vercel *)",           ← Pode fazer deploy
      "Bash(curl *)"             ← Pode fazer requisicoes HTTP
    ]
  }
}
```

**Para adicionar permissao para uma nova ferramenta:**
Adicione uma nova linha no array `allow` com o padrao `"Bash(comando *)"`.

**Padroes de permissao:**
- `Write(pasta/**)` — Permite escrita recursiva na pasta
- `Read(**)` — Permite leitura em qualquer lugar
- `Bash(comando *)` — Permite executar o comando com qualquer argumento

---

## 10. Onde Salvar Cada Tipo de Entrega

Esta tabela e definida no CLAUDE.md e deve ser respeitada por TODOS os commands e agents:

| Tipo de Material | Pasta | Formato | Exemplo de nome |
|---|---|---|---|
| Paginas (vendas, captura, obrigado) | `entregas/paginas/` | `.html` | `vendas-curso-ingles.html` |
| Textos de venda (copy, headlines, VSL) | `entregas/textos-de-venda/` | `.md` | `headlines-curso-ingles.md` |
| Sequencias de email | `entregas/emails/` | `.md` | `sequencia-pico-curso-ingles.md` |
| Anuncios (Meta, Google) | `entregas/anuncios/` | `.md` | `anuncios-meta-curso-ingles.md` |
| Conteudo para redes sociais | `entregas/conteudo-social/` | `.md` | `carrossel-curso-ingles.md` |
| Criativos e prompts de imagem | `entregas/criativos/` | `.md` | `prompts-midjourney-curso-ingles.md` |
| Scripts comerciais | `entregas/comercial/` | `.md` | `playbook-curso-ingles.md` |

**Se precisar de uma nova pasta de entrega:**
1. Crie a pasta em `entregas/`
2. Adicione um `.gitkeep` dentro dela
3. Atualize a tabela no CLAUDE.md
4. Adicione a permissao `Write(entregas/nova-pasta/**)` no settings.json (ja coberta por `Write(entregas/**)`)

---

## 11. Convencoes e Padroes

### Nomenclatura de arquivos

| Componente | Convencao | Exemplo |
|---|---|---|
| Commands | kebab-case, singular | `pagina-de-vendas.md` |
| Agents | kebab-case, descritivo | `construtor-de-paginas.md` |
| Skills (pasta) | kebab-case | `playbook-comercial/` |
| Skills (arquivo) | Sempre `SKILL.md` (maiusculo) | `SKILL.md` |
| References | kebab-case, descritivo | `formatos-meta-ads.md` |
| Entregas | `[tipo]-[produto].[ext]` | `vendas-curso-ingles.html` |

### Idioma

- Todo conteudo visivel ao usuario: Portugues do Brasil
- Nomes de arquivos e pastas: sem acentos, kebab-case
- Frontmatter: pode ter acentos na description
- Codigo HTML/CSS: comentarios em portugues

### Estilo de copy (Light Copy)

Todas as copys geradas devem seguir:
- Argumentativo, logico, conversacional
- Sem ponto de exclamacao
- Sem perguntas no gancho
- Sem promessas vagas
- Sem "mesmo que" ou "sem precisar" como muletas
- Sem travessao

### Padrao HTML para paginas

- Arquivo unico (CSS em `<style>`, JS em `<script>`)
- Zero dependencias externas (exceto Google Fonts)
- Mobile-first com media queries
- Paleta maxima: 3 cores + neutros
- Animacoes CSS sutis
- Botoes grandes com hover
- Placeholders de imagem: `[Sua foto aqui]`

---

## 12. O Que NAO Sobe Para o Git

Protegido pelo `.gitignore`:

| Item | Razao |
|---|---|
| `.env` | Chaves de API do usuario |
| `meu-negocio/perfil.md` | Dados do produto do usuario |
| `meu-negocio/persona.md` | Dados da persona do usuario |
| `entregas/` (conteudo) | Materiais gerados sao unicos de cada usuario |
| `_prompts-gpt/` | Prompts originais de referencia interna |
| `.claude/projects/`, `.claude/plans/`, etc. | Arquivos de runtime do Claude Code |

**O que SOBE para o git:**
- `.claude/commands/`, `.claude/agents/`, `.claude/plugins/` (o sistema em si)
- `.claude/settings.json` (permissoes)
- `CLAUDE.md`, `README.md`, `COMO-USAR.md` (documentacao)
- `.env.example` (modelo de chaves, sem valores)
- `.gitkeep` dentro das pastas de entrega (mantem a estrutura)
- `docs/` (documentacao tecnica)

---

## 13. Relacao entre Componentes — Mapa de Dependencias

```
CLAUDE.md (regras globais)
    │
    ├── /meu-produto ──────► skill: concepcao-produto ──► salva: meu-negocio/perfil.md
    ├── /persona ──────────► skill: concepcao-produto ──► salva: meu-negocio/persona.md
    │
    ├── /pagina-de-vendas ─► skill: paginas ────────────► salva: entregas/paginas/*.html
    ├── /texto-de-venda ───► skill: conteudo ───────────► salva: entregas/textos-de-venda/*.md
    ├── /anuncio ──────────► skill: anuncios ───────────► salva: entregas/anuncios/*.md
    ├── /conteudo-social ──► skill: conteudo ───────────► salva: entregas/conteudo-social/*.md
    ├── /roteiro-de-video ─► skill: conteudo ───────────► salva: entregas/textos-de-venda/*.md
    ├── /sequencia-de-emails► skill: conteudo ──────────► salva: entregas/emails/*.md
    ├── /lancamento ───────► skill: vtsd-completo ──────► salva: entregas/textos-de-venda/*.md
    ├── /funil-de-vendas ──► skill: trafego-pago ──────► salva: entregas/textos-de-venda/*.md
    ├── /playbook-comercial► skill: playbook-comercial ► salva: entregas/comercial/*.md
    ├── /criativo-de-imagem► skill: anuncios ───────────► salva: entregas/criativos/*.md
    ├── /low-ticket ───────► skill: vtsd-completo ──────► salva: entregas/ (multiplas pastas)
    │
    ├── agent: estrategista ► skill: concepcao-produto ► salva: meu-negocio/perfil.md
    ├── agent: construtor ──► skill: paginas ───────────► salva: entregas/paginas/*.html
    ├── agent: campanhas ───► skill: anuncios + trafego ► salva: entregas/anuncios/*.md
    ├── agent: conteudo ────► skill: conteudo ──────────► salva: entregas/conteudo-social/*.md
    └── agent: comercial ──► skill: playbook-comercial ► salva: entregas/comercial/*.md
```

---

## 14. Exemplo Completo: Adicionando a Capacidade "Webinar"

Para ilustrar todo o processo, veja como seria adicionar suporte completo a webinars:

### 14.1 Criar a skill

**Arquivo:** `.claude/plugins/workshop-marketing/skills/webinars/SKILL.md`

```markdown
---
name: webinars
description: >
  Base de conhecimento para criacao de webinars de vendas.
  Inclui estrutura de roteiro (abertura, conteudo, pitch, CTA),
  formatos de apresentacao e follow-up pos-webinar.
  Acionada pelo command /webinar e agent planejador-de-webinar.
---

# Webinars — Base de Conhecimento

## Estrutura do Roteiro (4 Atos)
1. **Abertura** — Promessa + contexto + "por que ouvir"
2. **Conteudo** — 3 blocos de valor (usar Furadeira)
3. **Transicao** — Ponte valor → oferta
4. **Pitch** — Oferta + stack de valor + CTA + garantia

## Formatos
- Webinar ao vivo (90 min)
- Webinar evergreen (gravado, 60 min)
- Mini-webinar (30 min, para trafego frio)

[... mais conteudo de referencia ...]
```

### 14.2 Criar o command

**Arquivo:** `.claude/commands/webinar.md`

```markdown
---
name: workshop-marketing:webinar
description: Criar roteiro completo de webinar de vendas com estrutura de 4 atos, slides e follow-up.
---

# Webinar — Roteiro Completo

## Usage
```
/webinar
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md` e `meu-negocio/persona.md`.

### 2. Entrevista
[... perguntas seguindo o padrao ...]

### 3. Confirmacao
[... resumo + opcoes ...]

### 4. Gerar
[... instrucoes de geracao ...]
Salvar em `entregas/textos-de-venda/webinar-[produto].md`

### 5. Proximo Passo
"Roteiro salvo. Use `/pagina-de-vendas` para criar a pagina de inscricao do webinar."

## Referencias
ANTES de gerar, leia:
- `.claude/plugins/workshop-marketing/skills/webinars/SKILL.md`
- `.claude/plugins/workshop-marketing/skills/vtsd-completo/SKILL.md` — Modulo sobre Light Copy
```

### 14.3 Criar o agent (opcional)

**Arquivo:** `.claude/agents/planejador-de-webinar.md`

```markdown
---
name: planejador-de-webinar
description: Agente autonomo que cria webinar completo — roteiro, estrutura de slides, emails de follow-up e anuncios de divulgacao.
tools: Read, Write, Edit
model: sonnet
---

# Planejador de Webinar — Agente Autonomo

[... instrucoes completas ...]

## Referencias
- `.claude/plugins/workshop-marketing/skills/webinars/SKILL.md`
```

### 14.4 Atualizar CLAUDE.md

Na secao de comandos, adicionar:
```
- `/webinar` — Criar roteiro completo de webinar de vendas
```

Na secao de agentes (se criou o agent):
```
- `planejador-de-webinar` — Cria webinar completo com roteiro, slides e follow-up
```

### 14.5 Atualizar README.md e COMO-USAR.md

Adicionar o novo comando nas tabelas e fluxos recomendados.

---

## 15. Troubleshooting

### Command nao aparece na lista

- Verifique se o arquivo esta em `.claude/commands/` (nao em subpasta)
- Verifique se a extensao e `.md`
- Verifique se o frontmatter YAML esta correto (delimitado por `---`)

### Agent nao e encontrado

- Verifique se o arquivo esta em `.claude/agents/`
- Verifique se o campo `name` no frontmatter corresponde ao nome usado na invocacao
- Verifique se `tools` esta definido no frontmatter

### Skill nao e consultada

- Skills NAO sao acionadas automaticamente — o command/agent precisa instruir explicitamente "Leia [caminho da skill]"
- Verifique se o caminho referenciado no command/agent esta correto

### Arquivo nao e salvo

- Verifique se a pasta de destino existe em `entregas/`
- Verifique se a permissao `Write(entregas/**)` esta no settings.json

### Ferramenta externa nao funciona

- Verifique se a chave existe no `.env` (nao no `.env.example`)
- Verifique se a permissao `Bash(ferramenta *)` esta no settings.json

---

## 16. Resumo Rapido para LLMs

Se voce e um LLM lendo este arquivo para entender o projeto:

1. **Leia `CLAUDE.md` primeiro** — contem todas as regras de comportamento, persona e fluxo padrao
2. **Commands** estao em `.claude/commands/*.md` — sao slash commands interativos
3. **Agents** estao em `.claude/agents/*.md` — sao subprocessos autonomos
4. **Skills** estao em `.claude/plugins/workshop-marketing/skills/*/SKILL.md` — sao base de conhecimento
5. **Dados do usuario** ficam em `meu-negocio/` (perfil.md e persona.md)
6. **Output** vai para `entregas/` organizado por tipo
7. **Tudo segue a metodologia VTSD** — Quadro, Furadeira, Decorados, Light Copy, 8D, Mandala
8. **Idioma:** Sempre Portugues do Brasil para conteudo visivel ao usuario
9. **Nunca mostre codigo HTML** ao usuario — salve silenciosamente e informe o caminho
10. **Sempre leia perfil.md** antes de executar qualquer comando
