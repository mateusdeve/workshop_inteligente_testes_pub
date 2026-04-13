# Agentes (Cursor e IDEs)

Este repositório é o **Workshop Marketing IA**: assistente de marketing digital, copy e infoprodutos (VTSD, Light Copy, C10X, low ticket).

## Onde está cada coisa

| O quê | Onde |
| --- | --- |
| Regras completas do assistente | `CLAUDE.md` |
| Regras específicas do Cursor | `.cursor/rules/*.mdc` |
| Roteiros dos “comandos” (/copy-pagina, /pagina-ajuste, etc.) | `.claude/commands/*.md` (ex.: `pagina-ajuste.md` para pós-merge e imagens em `paginas/assets/`) |
| Skills e templates | `.claude/plugins/workshop-marketing/skills/` |
| Entregas do aluno | `entregas/` |
| Copiar templates do tema para a pasta do produto (antes de editar HTML) | `scripts/workshop-copy-template-tema.py` |
| Merge da página completa (após blocos preenchidos na cópia) | `scripts/workshop-merge-pagina.py` (`--templates-root` apontando para `entregas/.../templates-{estilo}/`) |
| Etapa de ajustes pós-merge (checkout, SEO, placeholders) | `.claude/plugins/workshop-marketing/skills/paginas/references/etapa-ajustes-pagina.md` |
| Playbook: evolução visual, imagens, abas e contraste em HTML (qualquer produto) | `.claude/plugins/workshop-marketing/skills/paginas/references/playbook-evolucao-visual-html-landing.md` |
| Estrutura da copy de vendas (16 blocos, alinhada ao HTML) | `.claude/plugins/workshop-marketing/skills/paginas/references/template-copy-pagina-vendas.md` |

## No Cursor

Com a pasta do projeto aberta, o chat usa `CLAUDE.md` e as regras em `.cursor/rules/`. Para executar um comando nomeado, o agente deve ler o `.md` correspondente em `.claude/commands/`, pois o Cursor não expõe slash commands do Claude Code da mesma forma.
