# Painel de Entregas. Arquitetura Enxuta

Este diretório guarda o **template fixo** do Painel de Entregas. A ideia é separar o que não muda (CSS, JS, shell HTML) do que muda por produto (dados).

## Por que essa estrutura

O painel antigo era um HTML monolítico de **1.600+ linhas**, gerado do zero a cada rodada do `/produto-concepcao`. Isso levava de 10 a 14 minutos e estourava o limite de contexto.

Agora o Claude gera só **JSONs estruturados** (um por seção). O HTML final é montado por um script Python em menos de 1 segundo, sem regenerar markup.

Resultados:
- HTML final: **~70 linhas** (antes: 1.653).
- Tempo de montagem: **menos de 1 segundo** por produto.
- Ajuste de uma seção: reescrever só o JSON da seção + rodar o script.
- Sem CSS inventado. O design system fica travado no `painel.css`.

## Árvore de arquivos

```
assets/templates/painel-entregas/
├── painel-base.html        # Shell fixo com placeholders
├── painel.css              # Design system completo (tokens, componentes)
├── painel-render.js        # Renderizadores por seção, lê window.PAINEL_DADOS
├── schemas/                # Schema JSON de cada seção (fonte de verdade)
│   ├── visao-geral.json
│   ├── quadro.json
│   ├── furadeira.json
│   ├── decorados.json
│   ├── urgencias.json
│   ├── id-produto.json
│   ├── id-consumidor.json
│   ├── id-comunicador.json
│   └── pesquisa.json
└── README.md               # Este arquivo

meus-produtos/{slug}/
├── dados/                  # JSONs preenchidos para o produto
│   ├── visao-geral.json
│   ├── quadro.json
│   └── ...
└── painel-entregas.html    # Gerado pelo script

scripts/
└── painel-entregas-montar.py  # Monta o HTML final a partir dos JSONs
```

## Como funciona

1. O Claude preenche cada JSON em `meus-produtos/{slug}/dados/` conforme os campos do schema correspondente. Um JSON por seção, fácil de validar e rápido de gerar.
2. `scripts/painel-entregas-montar.py` lê os 9 JSONs, lê o shell `painel-base.html` e substitui os placeholders:
   - `{{PRODUTO_NOME}}`
   - `{{COMUNICADOR_NOME}}`
   - `{{CSS_PATH}}`
   - `{{JS_PATH}}`
   - `{{DADOS_JSON}}` (JSON agregado, compacto)
3. No navegador, `painel-render.js` lê `window.PAINEL_DADOS` e renderiza cada seção dentro de `#panel-{id}`.

## Comandos

```bash
# Monta o painel do produto ativo (meus-produtos/.ativo)
py -3 scripts/painel-entregas-montar.py

# Monta um slug específico
py -3 scripts/painel-entregas-montar.py --slug curso-tarot
```

Saída:
```
Painel gerado: meus-produtos/curso-tarot/painel-entregas.html
```

## Editando um produto

**Nunca edite** `painel-entregas.html` diretamente. Edite os JSONs em `dados/` e rode o script. O HTML é saída derivada.

Exemplo. Atualizar só a pesquisa de mercado:
1. Abrir `meus-produtos/{slug}/dados/pesquisa.json`.
2. Reescrever o conteúdo conforme o schema em `schemas/pesquisa.json`.
3. Rodar `py -3 scripts/painel-entregas-montar.py --slug {slug}`.
4. Recarregar `painel-entregas.html` no navegador.

## Schemas. Regras gerais

- Cada schema tem um campo `_comentario` no topo explicando convenções específicas da seção. O script remove esse campo antes de injetar no HTML.
- Arrays vazios (`[]`) são aceitos. A seção correspondente simplesmente não renderiza aquele bloco.
- Strings aceitam `<br>`, `<strong>`, `<em>` como texto formatado em campos marcados nos schemas. O restante é escapado.
- `pesquisa.json.concorrentes[].linkPagina` e `linkInstagram`: SOMENTE URL real. URLs de busca (`google.com/search`, `youtube.com/results`, `bing.com/search`) são filtradas pelo renderizador.

## Ganho na ponta

Com essa arquitetura:

- Gerar o painel inteiro: **1 JSON por vez**, cada um pequeno o suficiente para caber no contexto sem apertar.
- Ajustar uma seção: reescrever 1 JSON + rodar o script. **Menos de 30 segundos**.
- Design consistente: CSS travado, zero chance de inventar cor ou espaçamento.
- Erro isolado por seção: `renderTudo()` tem `try/catch` por seção. Se um JSON estiver mal formado, só aquela seção mostra erro; as demais renderizam normal.
