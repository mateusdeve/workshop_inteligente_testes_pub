# Diagnostico Completo. Workshop Marketing IA

Data: 2026-03-24 (revisado em 2026-04-08)

---

## Atualizacao 2026-04-08

Limpeza estrutural completa do projeto:

- Pastas duplicadas `entregas-familia-viajante/` e `entregas-familia-viajante2/` consolidadas em `entregas/familia-viajante/low-ticket-v1/` e `low-ticket-v2/`.
- Arquivos soltos da raiz (`funil-familia-viajante.html`, `quiz-funnel-workshop-*.md/.html/.docx`) movidos para subpastas dentro do produto correspondente.
- Pastas orfas removidas: `correcoes/`, `feedback/`, `outputs/`, `produtos/`.
- `server.js` deletado (apontava para `produtos/curso-tarot/` que ja nao existe).
- `README.md` reescrito com a estrutura real do projeto.
- `CLAUDE.md` sincronizado com a lista atual de comandos: incluidos os 17 comandos `/ht-*` da trilha High Ticket, os 4 comandos `/pagina-*` de infraestrutura, e os agentes `estrategista-low-ticket`, `estrategista-middle-ticket`, `estrategista-ht`, `copywriter`, `video-maker`, `executor-de-plano-de-acao`.
- Hook `no-emdash-guard.js` instalado em PreToolUse para fiscalizar a regra absoluta de proibicao de travessao em arquivos de copy (`.md`, `.html`, `.txt` dentro de `entregas/`).
- `.gitignore` atualizado com `entregas-*/` para evitar futuras pastas duplicadas na raiz.

Estado atual da raiz:

```
CLAUDE.md  COMO-USAR.md  README.md
docs/  entregas/  .claude/
package.json  vercel.json  .env.example
```

Inventario atualizado:

| Elemento | Quantidade | Local |
|---|---|---|
| Commands ativos | 49 | `.claude/commands/` (sem contar `gsd/` e `references/`) |
| Agents do workshop | 11 | `.claude/agents/` (sem contar os 24 `gsd-*`) |
| Skills do plugin | 22 | `.claude/plugins/workshop-marketing/skills/` |
| Hooks PreToolUse | 5 | `.claude/hooks/` (incluindo `no-emdash-guard.js`) |

Pendencia conhecida: a pasta vazia `entregas-familia-viajante2/` esta travada por outro processo do Windows e nao foi possivel removela via `rm`/`rmdir`. Reiniciar o explorer ou o IDE deve liberar.

---

## Visao Geral

O projeto esta bem estruturado na sua base. A metodologia VTSD (11 modulos) foi traduzida em 7 skills, 12 commands e 5 agents. O SKILL.md original (`_prompts-gpt`) e o implementado no plugin sao 100% identicos (1084 linhas, zero diferencas). nenhuma informacao foi perdida na conversao.

### Inventario do Projeto

| Elemento | Quantidade | Local |
|---|---|---|
| Skills (base de conhecimento) | 7 | `.claude/plugins/workshop-marketing/skills/` |
| Commands (slash commands) | 12 | `.claude/commands/` |
| Agents (especialistas autonomos) | 5 | `.claude/agents/` |
| Reference files (exemplos e templates) | 8 | Dentro de cada skill em `references/` |
| Pastas de entrega | 7 | `entregas/` |

---

## O Que Esta Bem Feito

| Elemento | Status |
|---|---|
| Metodologia VTSD completa no plugin | Identica ao original |
| 12 commands cobrindo o fluxo principal | Completo |
| 5 agents para tarefas autonomas | Bem definidos |
| Fluxo de 5 passos (Contexto, Entrevista, Confirmacao, Geracao, Entrega) | Consistente em todos os commands |
| Pastas de entrega organizadas | Todas existem (7 pastas) |
| Light Copy como padrao de escrita | Referenciado nos commands |
| Perfil persistente em `meu-negocio/perfil.md` | Funcional |
| COMO-USAR.md com fluxos recomendados | Excelente para o aluno |
| README.md com guia de instalacao | Claro e acessivel |

---

## Cofre de Chaves API. Integracao com Ferramentas Externas

O toolkit gera entregaveis (copy, HTML, roteiros, prompts), mas para automatizar a publicacao e criacao de ativos visuais, o Claude Code precisa se conectar a ferramentas externas via API.

### Arquivo de Configuracao: `.env`

Todas as chaves ficam em `.env` na raiz do projeto. Esse arquivo NUNCA sobe para o repositorio (ja incluido no `.gitignore`). Um `.env.example` serve como modelo para o aluno preencher.

### Mapa de Chaves por Ferramenta

| Ferramenta | Variavel | Para que serve | Onde obter |
|---|---|---|---|
| **Vercel** | `VERCEL_TOKEN` | Deploy automatico de paginas HTML | vercel.com/account/tokens |
| **Vercel** | `VERCEL_PROJECT_ID` | Identificar o projeto de deploy | Dashboard do Vercel |
| **Freepik** | `FREEPIK_API_KEY` | Gerar imagens de anuncios e posts via IA | freepik.com/api |
| **HeyGen** | `HEYGEN_API_KEY` | Criar videos com avatar IA | app.heygen.com/settings |
| **Meta Ads** | `META_ACCESS_TOKEN` | Gerenciar campanhas no Facebook/Instagram | developers.facebook.com |
| **Meta Ads** | `META_AD_ACCOUNT_ID` | Identificar conta de anuncios | Gerenciador de Anuncios |
| **Meta Ads** | `META_PIXEL_ID` | Rastreamento de conversoes (Pixel) | Gerenciador de Eventos |
| **Google Ads** | `GOOGLE_ADS_DEVELOPER_TOKEN` | Gerenciar campanhas no Google | ads.google.com/api |
| **Google Ads** | `GOOGLE_ADS_CUSTOMER_ID` | Identificar conta de anuncios | Google Ads Dashboard |
| **Hotmart** | `HOTMART_TOKEN` | Gerar links de checkout e consultar vendas | hotmart.com/settings/api |
| **Hotmart** | `HOTMART_PRODUCT_ID` | Identificar produto no checkout | Dashboard Hotmart |
| **WhatsApp** | `WHATSAPP_PHONE_ID` | Enviar mensagens automaticas | Meta Business Suite |
| **WhatsApp** | `WHATSAPP_ACCESS_TOKEN` | Autenticar na Cloud API | developers.facebook.com |

### Como Cada Chave Conecta com os Entregaveis

```
FLUXO: Command/Agent -> Gera entregavel -> Usa API -> Resultado automatizado

/pagina-de-vendas
  └─ Gera HTML em entregas/paginas/
     └─ VERCEL_TOKEN + VERCEL_PROJECT_ID
        └─ Deploy automatico: pagina online em minutos

/criativo-de-imagem
  └─ Gera prompts de imagem em entregas/criativos/
     └─ FREEPIK_API_KEY
        └─ Envia prompt para Freepik API -> Recebe imagem pronta

/roteiro-de-video (formato avatar)
  └─ Gera script em entregas/textos-de-venda/
     └─ HEYGEN_API_KEY
        └─ Envia script para HeyGen API -> Recebe video com avatar

/anuncio + criador-de-campanhas
  └─ Gera copy + estrutura em entregas/anuncios/
     └─ META_ACCESS_TOKEN + META_AD_ACCOUNT_ID
        └─ Cria campanhas direto no Gerenciador (opcional)
     └─ GOOGLE_ADS_DEVELOPER_TOKEN + GOOGLE_ADS_CUSTOMER_ID
        └─ Cria campanhas no Google Ads (opcional)

/pagina-de-vendas (com checkout)
  └─ Gera pagina com botao de compra
     └─ HOTMART_TOKEN + HOTMART_PRODUCT_ID
        └─ Gera link de checkout automatico na pagina

/sequencia-de-emails + /lancamento
  └─ Gera sequencias de comunicacao
     └─ WHATSAPP_PHONE_ID + WHATSAPP_ACCESS_TOKEN
        └─ Envia mensagens de lembrete/abertura de carrinho

Rastreamento (todas as paginas):
  └─ META_PIXEL_ID
     └─ Insere codigo do Pixel automaticamente nas paginas HTML geradas
```

### Niveis de Uso (o aluno escolhe)

| Nivel | O que precisa | O que consegue |
|---|---|---|
| **Basico** | Nenhuma chave | Todos os entregaveis em arquivo (copy, HTML, roteiros, prompts). uso manual |
| **Intermediario** | VERCEL_TOKEN + FREEPIK_API_KEY | Paginas publicadas online + imagens geradas automaticamente |
| **Avancado** | Todas as chaves | Automacao completa: paginas no ar, anuncios criados, videos gerados, pixel instalado |

O toolkit funciona 100% no nivel Basico. As APIs sao opcionais e progressivas.

---

## Problemas Encontrados

### CRITICO 1. README com arquitetura errada

O `README.md` mostra `commands/` dentro de `plugins/workshop-marketing/`, mas os commands estao em `.claude/commands/`. Isso confunde quem olha a estrutura.

**Diagrama atual no README (errado):**
```
plugins/
  workshop-marketing/
    commands/          <-- NAO EXISTE AQUI
```

**Realidade:**
```
.claude/
  commands/            <-- COMMANDS ESTAO AQUI
  agents/
  plugins/
    workshop-marketing/
      skills/          <-- SO SKILLS ESTAO NO PLUGIN
```

**Acao:** Corrigir o diagrama de arquitetura no README.md.

---

### CRITICO 2. Modulo low ticket (Low Ticket) esta subrepresentado

O Modulo 10 do VTSD e um dos mais praticos para quem esta comecando e NAO tem um command dedicado. O `/funil-de-vendas` menciona low ticket brevemente, mas faltam:

- **Pagina Final do Quiz** (estrutura de 12 blocos do VTSD). nao esta em nenhum command
- **Anuncios "Low Ticket"** (focados em quiz). nao cobertos
- **Produto Desafio** (3-7 dias com missoes). nao tem command
- **Agente GPT vendavel** (secao 10.6 do VTSD). nao coberto
- **Copy Hotmart** (secao 10.7). elementos especificos da plataforma nao cobertos

**Acao:** Criar um command `/low-ticket` ou `/low ticket` dedicado que cubra:
- Definicao do produto low ticket (tipos permitidos: ebook, guia, planilha, checklist, mini-curso, desafio, agente GPT, template)
- Quadro adaptado para low ticket (resultado rapido e tangivel)
- Estrutura da pagina final do quiz (12 blocos)
- Anuncios "Low Ticket" com foco em quiz
- Produto Desafio (3-7 dias)
- Copy adaptada para Hotmart

---

### IMPORTANTE 3. Agents referenciam skills por nome generico

Os 5 agents dizem coisas como "Consulte a skill `vtsd-completo`" ou "Consulte skill `paginas`", mas nao indicam o caminho real dos arquivos. Quando o agent roda como subprocesso, ele pode nao encontrar os skills.

**Exemplo atual (construtor-de-paginas.md):**
```
Consulte skill `paginas` para estruturas e paletas
Consulte templates em `skills/paginas/references/templates/`
```

**Deveria ser:**
```
Leia o arquivo `.claude/plugins/workshop-marketing/skills/paginas/SKILL.md`
Leia `.claude/plugins/workshop-marketing/skills/paginas/references/estruturas-pagina.md`
```

**Afeta todos os 5 agents:**
- estrategista-de-produto.md
- construtor-de-paginas.md
- criador-de-campanhas.md
- produtor-de-conteudo.md
- consultor-comercial.md

**Acao:** Atualizar cada agent com caminhos completos dos arquivos que devem consultar.

---

### IMPORTANTE 4. Modulo 7 (Upsell/Downsell/Order Bump) sem command dedicado

O modulo e mencionado na skill `playbook-comercial` e no `/funil-de-vendas`, mas nao ha um command ou fluxo dedicado para o aluno criar essas ofertas complementares. Isso e dinheiro na mesa para o infoprodutor.

**O que falta:**
- Definicao de upsell (oferta complementar pos-compra)
- Definicao de downsell (oferta menor para quem nao comprou)
- Definicao de order bump (complemento no checkout)
- Estrategia de precificacao para cada um

**Acao:** Incorporar de forma mais explicita no `/funil-de-vendas` com uma secao dedicada, ou adicionar no `/meu-produto` para mapear ofertas complementares durante o cadastro do produto.

---

### IMPORTANTE 5. Persona salva em local nao intuitivo

Historico: o fluxo antigo salvava em `entregas/textos-de-venda/persona-[nome].md`. Hoje o comando e `/idconsumidor` e o arquivo e `meu-negocio/idconsumidor.md` (documento de fundacao, como o perfil).

**Impacto:** Agents e commands leem `meu-negocio/idconsumidor.md`.

---

### IMPORTANTE 6. Mapa mental do Workshop menciona skills nao implementadas

O PDF do mind map (`_prompts-gpt/Workshop IA na pratica para infoprodutores`) lista:
- **"Skill de anuncios em videos"**. Nao existe separada
- **"Skill de anuncios em texto"**. Nao existe separada

O que existe e uma unica skill `anuncios` que cobre ambos. No contexto do Workshop ao vivo, pode valer separar para que o aluno entenda a diferenca entre criativos de imagem estatica vs video.

**Acao:** Avaliar se vale criar duas skills separadas (anuncios-video e anuncios-texto) ou se a skill unificada atende. Depende de como o Workshop ao vivo sera conduzido.

---

### MENOR 7. Ferramentas do Workshop nao integradas no toolkit

O mind map mostra ferramentas que o Workshop usa mas o toolkit nao orienta:

| Ferramenta | Uso no Workshop | Status no Toolkit |
|---|---|---|
| Freepik | Imagens e videos personalizados | `/criativo-de-imagem` cobre parcialmente |
| HeyGen | Avatares IA para videos | `/roteiro-de-video` menciona mas nao guia |
| Lovable | Criacao de quiz | Nao coberto |
| Vercel | Publicacao de paginas | Nao coberto |
| Facebook Pixel | Rastreamento de conversoes | Skill `trafego-pago` cobre teoria, sem guia pratico |
| API de Conversao | Dados server-side | Idem |
| WhatsApp Automacoes | Notificacoes de trafego | Nao coberto |

**Acao:** Criar um reference file `ferramentas-workshop.md` com links e orientacoes para cada ferramenta, ou um command `/ferramentas` que orienta o aluno.

---

### MENOR 8. Argumentos Incontestaveis (Modulo 2.3) pouco visiveis

O conceito de "argumentos baseados em dados e pesquisa" e poderoso para copy, mas esta diluido no SKILL.md geral. Nenhum command pede explicitamente ao aluno para fornecer dados, pesquisas ou estatisticas do nicho.

**Acao:** Adicionar no `/meu-produto` uma pergunta sobre dados, pesquisas ou estatisticas do nicho. Guardar no perfil.md como secao "Argumentos Incontestaveis".

---

### MENOR 9. Settings.json com permissoes minimas

O `.claude/settings.json` permite apenas:
- `Write(entregas/**)`
- `Write(meu-negocio/**)`
- `Read(**)`
- `Bash(ls *)`

Para suportar as integracoes com APIs externas, sera necessario expandir permissoes conforme as automacoes forem implementadas (ex: `Bash(vercel *)`, `Bash(curl *)`).

**Acao:** Expandir progressivamente conforme cada integracao for adicionada.

---

## Cobertura VTSD vs Toolkit

| Modulo VTSD | Skill | Command | Agent | Cobertura |
|---|---|---|---|---|
| 1. Fundamentos (Quadro, Furadeira, 3Is) | concepcao-produto | /meu-produto, /idconsumidor | estrategista-de-produto | TOTAL |
| 2. Oferta e Pagina 8D | paginas | /pagina-de-vendas | construtor-de-paginas | TOTAL |
| 3. VVV (Video de Vendas) | conteudo | /roteiro-de-video, /texto-de-venda |. | TOTAL |
| 4. Mandala 18 Anuncios | anuncios | /anuncio | criador-de-campanhas | TOTAL |
| 5. Conteudo Redes | conteudo | /conteudo-social | produtor-de-conteudo | TOTAL |
| 6. Emails Pico de Vendas | vtsd-completo | /sequencia-de-emails |. | TOTAL |
| 7. Upsell/Downsell/Bump | playbook-comercial | /funil-de-vendas (parcial) |. | PARCIAL |
| 8. Estrutura Campanha | trafego-pago | /anuncio (parcial) | criador-de-campanhas | TOTAL |
| 9. C10X (High Ticket) | playbook-comercial | /lancamento, /playbook-comercial | consultor-comercial | TOTAL |
| 10. low ticket (Low Ticket) | vtsd-completo | /funil-de-vendas (mencao breve) |. | FRACA |
| 11. Light Copy (26 Elementos) | conteudo + vtsd-completo | /texto-de-venda, /conteudo-social | produtor-de-conteudo | TOTAL |

**Resultado geral:** 9 de 11 modulos com cobertura TOTAL. 1 PARCIAL (Upsell). 1 FRACA (low ticket).

---

## Mapa Explicito: Ferramenta x Skill x Command x Agent x Entregavel

Essa tabela mostra exatamente quem faz o que, usando qual ferramenta, e entrega onde.

### Fundacao (dados do negocio)

| Acao | Command | Agent | Skill consultada | Ferramenta externa | Entregavel | Destino |
|---|---|---|---|---|---|---|
| Cadastrar produto | `/meu-produto` | estrategista-de-produto | concepcao-produto | Nenhuma | Perfil completo VTSD | `meu-negocio/perfil.md` |
| Identidade do consumidor | `/idconsumidor` | estrategista-de-produto | concepcao-produto | Nenhuma | Cliente ideal detalhado | `meu-negocio/idconsumidor.md` |

### Paginas

| Acao | Command | Agent | Skill consultada | Ferramenta externa | Entregavel | Destino |
|---|---|---|---|---|---|---|
| Pagina de vendas 8D | `/pagina-de-vendas` | construtor-de-paginas | paginas + vtsd-completo | **Vercel** (deploy) | HTML responsivo | `entregas/paginas/vendas-*.html` |
| Pagina de captura | `/pagina-de-vendas` | construtor-de-paginas | paginas | **Vercel** (deploy) | HTML com formulario | `entregas/paginas/captura-*.html` |
| Pagina de obrigado | `/pagina-de-vendas` | construtor-de-paginas | paginas | **Vercel** (deploy) | HTML pos-cadastro | `entregas/paginas/obrigado-*.html` |

### Textos e Copy

| Acao | Command | Agent | Skill consultada | Ferramenta externa | Entregavel | Destino |
|---|---|---|---|---|---|---|
| Headlines e copy | `/texto-de-venda` |. | conteudo + vtsd-completo | Nenhuma | Textos Light Copy | `entregas/textos-de-venda/` |
| Roteiro VVV | `/roteiro-de-video` |. | conteudo + vtsd-completo | **HeyGen** (avatar) | Script de video | `entregas/textos-de-venda/roteiro-*.md` |
| Emails pico de vendas | `/sequencia-de-emails` |. | vtsd-completo | **WhatsApp** (envio) | Sequencia completa | `entregas/emails/sequencia-*.md` |

### Anuncios e Trafego

| Acao | Command | Agent | Skill consultada | Ferramenta externa | Entregavel | Destino |
|---|---|---|---|---|---|---|
| Anuncios Mandala 18 | `/anuncio` | criador-de-campanhas | anuncios + vtsd-completo | **Meta Ads** / **Google Ads** | Copy + direcao criativa | `entregas/anuncios/` |
| Imagens de criativos | `/criativo-de-imagem` |. | anuncios | **Freepik** (geracao IA) | Prompts + imagens | `entregas/criativos/` |
| Campanha completa |. | criador-de-campanhas | anuncios + trafego-pago | **Meta Ads** + **Google Ads** | Pacote de campanha | `entregas/anuncios/campanha-completa-*.md` |

### Conteudo Social

| Acao | Command | Agent | Skill consultada | Ferramenta externa | Entregavel | Destino |
|---|---|---|---|---|---|---|
| Carrosseis e captions | `/conteudo-social` | produtor-de-conteudo | conteudo | **Freepik** (imagens) | Posts prontos | `entregas/conteudo-social/` |
| Roteiro de Reels | `/conteudo-social` | produtor-de-conteudo | conteudo | **HeyGen** (avatar) | Roteiros 60s | `entregas/conteudo-social/` |
| Plano 30 dias | `/conteudo-social` | produtor-de-conteudo | conteudo + vtsd-completo | Nenhuma | Calendario editorial | `entregas/conteudo-social/plano-*.md` |

### Estrategia e Vendas

| Acao | Command | Agent | Skill consultada | Ferramenta externa | Entregavel | Destino |
|---|---|---|---|---|---|---|
| Plano de lancamento | `/lancamento` |. | vtsd-completo (C10X) | Nenhuma | Cronograma + materiais | `entregas/textos-de-venda/lancamento-*.md` |
| Funil completo | `/funil-de-vendas` |. | vtsd-completo + trafego-pago | Nenhuma | Mapa de funil | `entregas/textos-de-venda/funil-*.md` |
| Playbook comercial | `/playbook-comercial` | consultor-comercial | playbook-comercial | Nenhuma | Scripts SPIN + fechamento (HTML, PDF via navegador) | `entregas/comercial/playbook-*.html` |

---

## Plano de Acoes (por prioridade)

### Prioridade 1. Correcoes criticas

- [x] **1.1** Corrigir diagrama de arquitetura no README.md. CONCLUIDO 2026-03-24
- [x] **1.2** Corrigir referencias dos 5 agents (caminhos reais dos arquivos). CONCLUIDO 2026-03-24
- [x] **1.3** Criar command `/low-ticket` para cobrir Modulo low ticket completo. CONCLUIDO 2026-03-24
- [x] **1.4** Criar `.env.example` com todas as chaves documentadas. CONCLUIDO 2026-03-24
- [x] **1.5** Adicionar `.env` ao `.gitignore` (proteger chaves do aluno). CONCLUIDO 2026-03-24

### Prioridade 2. Melhorias importantes

- [x] **2.1** Fortalecer Upsell/Downsell no `/funil-de-vendas` (secao 4 completa com Upsell, Order Bump, Downsell). CONCLUIDO 2026-03-24
- [x] **2.2** Arquivo de cliente ideal em `meu-negocio/idconsumidor.md` (comando `/idconsumidor`; antes `persona.md` / `/persona`). referencias atualizadas (agents, CLAUDE.md, COMO-USAR.md). CONCLUIDO 2026-03-24; renomeacao comando 2026-03-24
- [x] **2.3** Adicionar pergunta sobre Argumentos Incontestaveis no `/meu-produto` (Bloco 5 + secao no perfil.md). CONCLUIDO 2026-03-24
- [x] **2.4** Expandir permissoes no `settings.json` (adicionado: docs/**, cat .env, vercel *, curl *). CONCLUIDO 2026-03-24

### Prioridade 3. Integracoes com ferramentas externas

- [x] **3.1** Implementar deploy automatico via Vercel (agent construtor-de-paginas + command pagina-de-vendas). CONCLUIDO 2026-03-24
- [x] **3.2** Implementar geracao de imagens via Freepik API no `/criativo-de-imagem`. CONCLUIDO 2026-03-24
- [x] **3.3** Implementar criacao de video via HeyGen API no `/roteiro-de-video`. CONCLUIDO 2026-03-24
- [x] **3.4** Implementar insercao automatica do Pixel nas paginas (agent + command). CONCLUIDO 2026-03-24
- [x] **3.5** Criar skill `ferramentas` com guia completo de 9 ferramentas. CONCLUIDO 2026-03-24

### Prioridade 4. Alinhamento com Workshop ao vivo

- [x] **4.1** Skills separadas: anuncios-texto (estaticos) e anuncios-video (Reels, Stories, YouTube). CONCLUIDO 2026-03-24
- [x] **4.2** Orientacoes de Pixel/CAPI incluidas na skill ferramentas e no agent construtor-de-paginas. CONCLUIDO 2026-03-24
- [x] **4.3** Guia de WhatsApp incluido na skill ferramentas. CONCLUIDO 2026-03-24
- [x] **4.4** Guia de Lovable para quiz incluido na skill ferramentas. CONCLUIDO 2026-03-24

---

## Como o Claude Code Deve Executar Este Plano

### Principio de Execucao

O Claude Code le este documento como referencia e executa cada acao do plano modificando os arquivos do projeto. O operador (voce, Vitor) autoriza cada etapa. O Claude Code NAO executa tudo de uma vez. segue a sequencia de prioridades e pede confirmacao entre blocos.

### Sequencia de Execucao

#### FASE 1. Correcoes criticas (execucao imediata)

```
Passo 1.1: Claude Code le README.md e edita o diagrama de arquitetura
  Arquivo: README.md
  Acao: Edit. corrigir bloco de arquitetura para refletir a estrutura real

Passo 1.2: Claude Code le cada agent e corrige as referencias de skills
  Arquivos:
    .claude/agents/estrategista-de-produto.md
    .claude/agents/construtor-de-paginas.md
    .claude/agents/criador-de-campanhas.md
    .claude/agents/produtor-de-conteudo.md
    .claude/agents/consultor-comercial.md
  Acao: Edit. trocar "Consulte skill X" por "Leia o arquivo .claude/plugins/workshop-marketing/skills/X/SKILL.md"

Passo 1.3: Claude Code cria o command /low-ticket
  Arquivo novo: .claude/commands/low-ticket.md
  Base: Modulo 10 do VTSD (secoes 10.1 a 10.7) extraido de vtsd-completo/SKILL.md
  Conteudo: Entrevista sobre tipo de produto low ticket, geracao de pagina quiz (12 blocos),
            anuncios low ticket, produto desafio, copy Hotmart

Passo 1.4: Claude Code cria o arquivo .env.example
  Arquivo novo: .env.example
  Conteudo: Todas as variaveis listadas na secao "Cofre de Chaves API" com valores vazios e comentarios

Passo 1.5: Claude Code edita .gitignore
  Arquivo: .gitignore
  Acao: Edit. adicionar linha `.env` na secao de dados do aluno
```

#### FASE 2. Melhorias importantes

```
Passo 2.1: Claude Code edita /funil-de-vendas ou /meu-produto
  Arquivo: .claude/commands/funil-de-vendas.md (ou meu-produto.md)
  Acao: Edit. adicionar secao de Upsell/Downsell/Order Bump com perguntas e geracao

Passo 2.2: Claude Code edita /idconsumidor e todos os agents que leem idconsumidor.md
  Arquivos:
    .claude/commands/idconsumidor.md. destino meu-negocio/idconsumidor.md
    .claude/agents/construtor-de-paginas.md. atualizar caminho de leitura
    .claude/agents/criador-de-campanhas.md. idem
    .claude/agents/produtor-de-conteudo.md. idem
    .claude/agents/consultor-comercial.md. idem
    CLAUDE.md. atualizar tabela de "Onde Salvar Cada Entrega" se necessario

Passo 2.3: Claude Code edita /meu-produto
  Arquivo: .claude/commands/meu-produto.md
  Acao: Edit. adicionar pergunta sobre dados/estatisticas do nicho
         Salvar como secao "Argumentos Incontestaveis" no perfil.md

Passo 2.4: Claude Code edita settings.json
  Arquivo: .claude/settings.json
  Acao: Edit. adicionar permissoes para Bash(vercel *), Bash(curl *) quando integracoes forem ativadas
```

#### FASE 3. Integracoes com ferramentas externas

```
Para cada integracao, o Claude Code segue este padrao:

1. Ler .env para verificar se a chave existe
2. Se existir: executar a integracao automaticamente
3. Se nao existir: gerar o entregavel normalmente (arquivo local) e avisar:
   "Para automatizar, configure a chave X no arquivo .env"

Passo 3.1: Deploy Vercel
  Onde atua: agent construtor-de-paginas.md + command pagina-de-vendas.md
  Logica: Apos salvar o HTML em entregas/paginas/, verificar VERCEL_TOKEN.
          Se existir, rodar `vercel deploy entregas/paginas/arquivo.html --token $VERCEL_TOKEN`
          Informar URL publica ao aluno.

Passo 3.2: Geracao de imagens Freepik
  Onde atua: command criativo-de-imagem.md
  Logica: Apos gerar os prompts, verificar FREEPIK_API_KEY.
          Se existir, enviar prompt via API REST do Freepik.
          Salvar imagem gerada em entregas/criativos/.
          Se nao existir, salvar apenas os prompts para uso manual.

Passo 3.3: Criacao de video HeyGen
  Onde atua: command roteiro-de-video.md (formato avatar)
  Logica: Apos gerar o script, verificar HEYGEN_API_KEY.
          Se existir, enviar script via API do HeyGen.
          Informar link do video quando pronto.
          Se nao existir, salvar script para uso manual no app.heygen.com.

Passo 3.4: Pixel automatico nas paginas
  Onde atua: agent construtor-de-paginas.md
  Logica: Ao gerar qualquer pagina HTML, verificar META_PIXEL_ID.
          Se existir, inserir automaticamente o snippet do Pixel no <head> da pagina.
          Incluir eventos PageView, Lead (captura) ou Purchase (vendas).
          Se nao existir, gerar pagina sem Pixel e avisar o aluno.

Passo 3.5: Reference file de ferramentas
  Arquivo novo: .claude/plugins/workshop-marketing/skills/ferramentas/references/ferramentas-workshop.md
  Conteudo: Link, para que serve, como configurar API key, e como o toolkit usa cada ferramenta
```

#### FASE 4. Alinhamento com Workshop ao vivo

```
Passo 4.1: Avaliar com Vitor se separa skills de anuncios
  Acao: Perguntar antes de executar. Se sim, criar:
    .claude/plugins/workshop-marketing/skills/anuncios-video/SKILL.md
    .claude/plugins/workshop-marketing/skills/anuncios-texto/SKILL.md

Passo 4.2-4.4: Criar guias praticos
  Arquivos novos em .claude/plugins/workshop-marketing/skills/trafego-pago/references/:
    guia-pixel-capi.md. Passo a passo de instalacao
    guia-whatsapp-automacao.md. Configuracao de notificacoes
    guia-lovable-quiz.md. Como criar quiz no Lovable
```

### Regras de Execucao para o Claude Code

1. **Sempre ler antes de editar.** Nunca modificar um arquivo sem ler o conteudo atual primeiro.

2. **Uma fase por vez.** Completar toda a Fase 1 antes de iniciar a Fase 2. Pedir confirmacao entre fases.

3. **Testar apos cada mudanca.** Apos editar um command ou agent, verificar se o arquivo esta sintaticamente correto (frontmatter YAML valido, markdown bem formatado).

4. **Nao quebrar o que funciona.** Ao mudar caminhos em `meu-negocio/`, atualizar TODAS as referencias antes de comunicar a mudanca.

5. **Integracoes sao opcionais.** O toolkit deve funcionar 100% sem nenhuma chave API. As integracoes sao melhorias progressivas.

6. **Respeitar o .env.** Nunca hardcodar chaves. Sempre ler do .env. Nunca exibir valores de chaves ao aluno.

7. **Documentar cada mudanca.** Ao concluir cada fase, atualizar este arquivo marcando os itens como concluidos `[x]`.

---

## Notas Tecnicas

- **SKILL.md original vs implementado:** 100% identicos (1084 linhas, diff vazio)
- **Pasta entregas/comercial/:** Existe e esta funcional
- **Commands location:** `.claude/commands/` (correto para Claude Code)
- **Plugin structure:** `.claude/plugins/workshop-marketing/` com skills organizadas por tema
- **Agents model:** Todos usando `model: sonnet` (adequado para custo/beneficio)
- **Cofre de chaves:** `.env` na raiz, protegido por `.gitignore`, modelo em `.env.example`
