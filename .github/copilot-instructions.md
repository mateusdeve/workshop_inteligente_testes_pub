---
description: "Marketing AI assistant toolkit for Brazilian infoprodutores using VTSD methodology. Always follow Light Copy rules, 6-step command pattern, and VTSD framework."
---

# Workshop Marketing IA — Copilot Instructions

## Project Overview
This is a **Claude Code-based AI assistant system** for Brazilian digital marketing professionals. It transforms Claude into a marketing consultant using structured prompts and the VTSD (Venda Todo Santo Dia) methodology.

**Stack:** Claude Code (VSCode extension) + Markdown prompts + HTML output + VTSD/Light Copy/C10X/low ticket frameworks

## Core Architecture Rules

### Component Types (5 distinct roles):
- **CLAUDE.md** (root): Global persona, rules, behavior for ALL interactions
- **Commands** (`.claude/commands/*.md`): Interactive slash commands (e.g., `/meu-produto`)
- **Agents** (`.claude/agents/*.md`): Autonomous subprocesses for complex tasks
- **Skills** (`.claude/skills/*/SKILL.md`): Reference knowledge base
- **Plugin** (`.claude/plugins/workshop-marketing/.claude-plugin/plugin.json`): Skill registry

### Data Flow:
```
User Input → CLAUDE.md (global rules) → Command → Read product context → Consult skills → Generate → Save to entregas/{ativo}/
```

## Critical Conventions (MANDATORY)

### 1. Light Copy Style (All Generated Text)
- ✅ Argumentative, logical, conversational (NOT salesly)
- ❌ NO exclamation marks, em-dashes (—), question marks in hooks
- ❌ NO "Não é X. É Y." structure, vague promises without data

### 2. The 6-Step Command Pattern (Non-negotiable)
Every command follows this sequence:
1. **Contexto** → Read `entregas/.ativo` → Read perfil.md + idconsumidor.md
2. **Entrevista** → Ask 1 question at a time, numbered options
3. **Confirmação** → Show summary, ask approval
4. **Geração** → Create deliverable using VTSD methodology
5. **Aprovação** → Show content, ask "1. Approve & save / 2. Adjust something"
6. **Entrega** → Save file, show path, suggest next command

### 3. VTSD Methodology Foundation
Every material must apply:
- **Quadro:** Main transformation (≤10 words, infinitive verb, result only)
- **Furadeira:** Structured method in macroetapas + microetapas
- **Decorados:** 50+ benefits from the Quadro
- **Urgências Ocultas:** Hidden pains, desires, doubts, topics
- **3 Identidades:** Comunicador, Consumidor, Produto

### 4. Product Data Must Exist First
Before ANY command beyond `/meu-produto` and `/idconsumidor`: check if `entregas/{ativo}/perfil.md` exists. If not: redirect to `/meu-produto`.

### 5. User Interview Pattern
```
Pergunta com opções:
1. Opção A
2. Opção B

Digite o número:

---

Pergunta aberta:
(ex: "Transformação principal que seu aluno alcança")
```

### 6. No Backticks in Output
- ❌ Forbidden: "Use the `Quadro` element"
- ✅ Required: "Use the Quadro element"

## Build & Development

**No traditional build process.** This is prompt-driven content generation.

```bash
# Test server for HTML pages
node server.js                    # Runs on http://localhost:4000
                                 # Serves from entregas/curso-tarot/paginas/
```

**Quality validation:** Manual review, user approval gates, browser testing for HTML.

## Key Files & Patterns

### Reference Files:
- **[CLAUDE.md](CLAUDE.md)**: Global role definition (300+ lines)
- **[.claude/skills/vtsd-completo/SKILL.md](.claude/skills/vtsd-completo/SKILL.md)**: VTSD foundation (1084 lines)
- **[ARQUITETURA.md](ARQUITETURA.md)**: Technical architecture guide

### Command Examples:
- **[.claude/commands/meu-produto.md](.claude/commands/meu-produto.md)**: Interview-driven with market research
- **[.claude/commands/copy-anuncio.md](.claude/commands/copy-anuncio.md)**: Complex decision tree (Mandala da Criatividade)
- **[.claude/commands/pagina-de-vendas.md](.claude/commands/pagina-de-vendas.md)**: HTML output + approval flow

## Known Pitfalls

- **Multi-product support:** Each product isolated in `entregas/{slug}/`. Active tracked in `entregas/.ativo`
- **Naming convention change:** `meu-negocio/` → `entregas/{ativo}/` (migration in progress)
- **Agents need full skill paths:** Reference `.claude/skills/X/SKILL.md`
- **low ticket (Low Ticket) underrepresented:** Missing dedicated commands for quiz pages, challenges, GPT agents
- **API integrations optional:** Vercel, Freepik, HeyGen, Meta, Google Ads, Hotmart, WhatsApp support via `.env`

## Output Locations

| Content Type | Path | Format |
|-------------|------|--------|
| Sales pages | `entregas/{ativo}/paginas/` | `.html` |
| Sales copy | `entregas/{ativo}/copy-pagina/` | `.md` |
| Email sequences | `entregas/{ativo}/emails/` | `.md` |
| Ads | `entregas/{ativo}/anuncios/` | `.md` |
| Social content | `entregas/{ativo}/conteudo-social/` | `.md` |
| Commercial scripts | `entregas/{ativo}/comercial/` | `.md` |

## HTML Quality Standards

- **Single file:** CSS in `<style>`, JS in `<script>` (no external dependencies except Google Fonts)
- **Professional design:** Modern typography, harmonious palette, generous spacing
- **Fully responsive:** Mobile-first with media queries
- **Subtle animations:** CSS transitions on hover/scroll
- **8D Structure:** Follow VTSD sales page framework
- **Ready to use:** Opens in browser immediately
- **Image placeholders:** Divs with "[Sua foto aqui]" instructions

## When to Use Specific Commands

- **New projects:** `/novo-produto` → `/meu-produto` → `/idconsumidor`
- **Sales pages:** `/pagina-de-vendas` (8D structure)
- **Lead magnets:** `/paginas-low-ticket` (low ticket: Inadequação, Identificação, Plug & Play, Promessa Boa Demais)
- **Ads:** `/copy-anuncio` (Mandala da Criatividade: 18 types × 3 objectives × 3 consumption moments)
- **Content:** `/copy-carrossel`, `/copy-variacao-post`
- **Sales:** `/comercial-playbook` (SPIN Selling)
- **Strategy:** `/lancamento`, `/estrategia-funil`

## Autonomous Agents

For complex tasks, invoke these agents:
- `estrategista-de-produto`: Complete VTSD conception
- `construtor-de-paginas`: Professional HTML pages
- `criador-de-campanhas`: Full traffic campaigns
- `produtor-de-conteudo`: 30-day content plans
- `consultor-comercial`: High-ticket sales playbooks