# Agentes (Cursor e IDEs)

Este repositório é o **Workshop Marketing IA**: assistente de marketing digital, copy e infoprodutos (VTSD, Light Copy, C10X, low ticket).

## Onde está cada coisa

| O quê | Onde |
| --- | --- |
| Regras completas do assistente | `CLAUDE.md` |
| Regras específicas do Cursor | `.cursor/rules/*.mdc` |
| Roteiros dos “comandos” (/copy-pagina, /pagina-ajuste, etc.) | `.claude/commands/*.md` (ex.: `pagina-ajuste.md` para pós-merge e imagens em `paginas/assets/`) |
| Skills e templates | `.claude/skills/` |
| Produtos e entregas do aluno (local, fora do git) | `meus-produtos/` (cada produto em `meus-produtos/{slug}/`, entregas em `meus-produtos/{slug}/entregas/`) |
| Painel global dos produtos | `painel/index.html` na raiz. Lê `meus-produtos/index.js` (manifest regenerado pelo script abaixo) |
| Copiar templates do tema para a pasta do produto (antes de editar HTML) | `scripts/workshop-copy-template-tema.py` |
| Merge da página completa (após blocos preenchidos na cópia) | `scripts/workshop-merge-pagina.py` (`--templates-root` apontando para `meus-produtos/{slug}/entregas/paginas/templates-{estilo}/`) |
| Regenerar manifest do painel (após criar, remover ou renomear produtos) | `scripts/painel-atualizar.py` ou o comando `/painel-atualizar` |
| Etapa de ajustes pós-merge (checkout, SEO, placeholders) | `.claude/skills/paginas/references/etapa-ajustes-pagina.md` |
| Playbook: evolução visual, imagens, abas e contraste em HTML (qualquer produto) | `.claude/skills/paginas/references/playbook-evolucao-visual-html-landing.md` |
| Estrutura da copy de vendas (16 blocos, alinhada ao HTML) | `.claude/skills/paginas/references/template-copy-pagina-vendas.md` |
| Toolkit de projetos estruturados (lançamento, funil completo) | `/toolkit-novo`, `/toolkit-planejar`, `/toolkit-executar`, `/toolkit-verificar`, `/toolkit-progresso`, `/toolkit-anotar`, `/toolkit-pausar`, `/toolkit-retomar`. Estado em `meus-produtos/{ativo}/projeto/{slug}/` |

## No Cursor

Com a pasta do projeto aberta, o chat usa `CLAUDE.md` e as regras em `.cursor/rules/`. Para executar um comando nomeado, o agente deve ler o `.md` correspondente em `.claude/commands/`, pois o Cursor não expõe slash commands do Claude Code da mesma forma.

