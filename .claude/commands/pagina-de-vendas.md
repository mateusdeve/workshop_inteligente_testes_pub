---
name: workshop-marketing:pagina-de-vendas
description: Criar páginas web profissionais completas (vendas 8D, captura ou obrigado) com HTML/CSS responsivo, design moderno e copy persuasiva baseada na metodologia VTSD.
---

# Página de Vendas — Gerador de Páginas Profissionais

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md`, `meu-negocio/idconsumidor.md` e `correcoes/informacoes-adicionais.md` se existirem.

### 2. Entrevista (UMA pergunta por vez)

**Bloco 1/3 — Tipo:**
```
Qual tipo de página?

1. Página de vendas (estrutura 8D completa)
2. Página de captura (coletar email/WhatsApp)
3. Página de obrigado (pós-cadastro ou pós-compra)

Digite o número:
```

**Bloco 2/3 — Detalhes (varia conforme tipo):**

**Se Vendas (8D)** — perguntar UMA por vez:
- Módulos/entregáveis do produto (pode usar perfil.md se já existir)
- Depoimentos (3-5 com nome e resultado, ou "pode criar")
- Garantia (7/15/30 dias)
- Preço e parcelamento
- Bônus (ou "pode criar")
- Link de checkout (ou "ainda não tenho")

**Se Captura:**
- Isca digital (e-book, aula, checklist)
- Promessa principal da isca

**Se Obrigado:**
- Confirmação de quê (cadastro/compra/evento)
- Próximo passo do aluno

**Para Captura e Obrigado:** verificar se já existem páginas em `entregas/paginas/`. Se sim, perguntar se quer manter a identidade visual. Se sim, ler o HTML existente para extrair paleta, fontes e estilo.

**Bloco 3/3 — Visual:**
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

### 3. Geração — Delegar ao Agente com Progresso Visual

Após a confirmação, **mostrar o progresso ao usuário** e delegar ao agente `construtor-de-paginas`.

**Passo 3a — Exibir mensagem de início com progresso:**

Antes de chamar o agente, enviar esta mensagem ao usuário para que ele acompanhe:

```
Gerando sua página. Acompanhe o progresso:

⬜ Lendo design system e estrutura de seções
⬜ Escrevendo copy das 16 seções (Hero, Dor, Método, Oferta...)
⬜ Montando HTML com CSS, animações e responsivo
⬜ Revisando acentos, grids e checklist de qualidade
⬜ Salvando arquivo final

Isso leva cerca de 1–2 minutos. Aguarde...
```

**Passo 3b — Chamar o agente `construtor-de-paginas`** com o brief completo:

```
Crie uma página de [tipo] para o produto "[nome]".

DADOS DO PRODUTO:
[Colar conteúdo relevante de perfil.md — Quadro, Furadeira, Decorados, Urgências Ocultas, Argumentos Incontestáveis]

IDENTIDADE DO CONSUMIDOR:
[Colar conteúdo relevante de idconsumidor.md — quem é, paliativos, objeções, frases]

DETALHES DA PÁGINA:
- Tipo: [vendas/captura/obrigado]
- Módulos: [lista]
- Depoimentos: [fornecidos ou "criar 5 com ultra resultados"]
- Garantia: [dias]
- Preço: [preço e parcelamento]
- Bônus: [fornecidos ou "criar 3-4 estratégicos"]
- Checkout: [link ou #]
- Cor: [paleta com hex codes]
- Fontes: [heading + body]

INSTRUÇÕES DE GERAÇÃO:
1. Ler `skills/paginas/references/design-system-components.md` para padrões CSS prontos
2. Ler `skills/paginas/references/estruturas-pagina.md` para estrutura das seções
3. Ler `skills/paginas/SKILL.md` para regras de qualidade e imagens contextuais
4. Gerar arquivo HTML ÚNICO com todas as seções
5. Salvar em `entregas/paginas/[tipo]-[produto].html`

REGRAS CRÍTICAS (não violar):
- TODOS os textos em português com acentos corretos
- TODAS as fontes sans-serif (serifadas PROIBIDAS)
- Header com logotipo obrigatório
- Cards min-width 320px, padding 28px+, font-size 0.95rem+
- Entregáveis em grid de 2 colunas (NÃO 3)
- Pelo menos 4 tipos de fundo diferentes entre seções
- Pelo menos 2 seções com imagem de fundo
- FAQ com accordion funcional em JS
- CTA flutuante no mobile
- Smooth scroll ativado
- Imagens contextuais (Picsum com seed descritivo, NUNCA genérico)
- NÃO parecer design genérico de IA
```

**IMPORTANTE:** Não gerar a página no chat principal. Delegar 100% ao agente.

### 4. Após o Agente Retornar

Atualizar o progresso e informar ao usuário:

```
Página gerada com sucesso:

✅ Design system e estrutura lidos
✅ Copy das 16 seções escrita
✅ HTML montado com CSS, animações e responsivo
✅ Acentos, grids e checklist revisados
✅ Arquivo salvo

Sua página está em: entregas/paginas/[nome-do-arquivo].html
Abra no navegador para visualizar.
```

### 5. Deploy na Vercel (se configurado)

Verificar se existem `.env` com `VERCEL_TOKEN`, `vercel.json` e `package.json`. Se sim, fazer deploy automático. Se não, perguntar:

```
Quer publicar online?

1. Tenho token da Vercel
2. Não quero deploy agora

Digite o número:
```

### 6. Próximo Passo
"Use `/anuncio` para criar anúncios que levem tráfego a essa página."
