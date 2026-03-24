---
name: workshop-marketing:pagina-de-vendas
description: Criar páginas web profissionais completas (vendas 8D, captura ou obrigado) com HTML/CSS responsivo, design moderno e copy persuasiva baseada na metodologia VTSD.
---

# Página de Vendas — Gerador de Páginas Profissionais

Cria páginas HTML completas e profissionais usando a estrutura 8D do VTSD.

## Usage

```
/pagina-de-vendas
```

## O Que Fazer

### 1. Contexto
Leia `meu-negocio/perfil.md` e persona existente.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3 — Tipo de Página:**

Pergunta 1:
```
Qual tipo de página?

1. Página de vendas (estrutura 8D completa)
2. Página de captura (coletar email/WhatsApp)
3. Página de obrigado (pós-cadastro ou pós-compra)

Digite o número:
```

```
--- Bloco 1/3 concluído ---
Tipo: [tipo escolhido]
Próximo: Detalhes do conteúdo
---
```

**Bloco 2/3 — Detalhes (varia conforme o tipo):**

Se escolheu **1. Vendas (8D):**
```
Quais os módulos ou entregáveis do produto?
(ex: "5 módulos de vídeo + planilhas + grupo VIP")
```
```
Tem depoimentos de alunos? Se sim, passe 3-5 com nome e resultado.
(ex: "João, faturou R$10k no primeiro mês")
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
Qual o preço e parcelamento?
(ex: "R$497 ou 12x R$47")
```
```
Tem bônus? Quais?
(ex: "Grupo VIP, planilha de métricas, aula extra")
```
```
Link de checkout (Hotmart, Kiwify)?
(ex: "https://pay.hotmart.com/ABC123" ou "ainda não tenho")
```

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

**Bloco 3/3 — Visual:**

Pergunta:
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
- Tipo: [tipo de página]
- Produto: [nome do produto]
- Cor: [cor escolhida]
- [detalhes específicos do tipo]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

Consulte os templates em `skills/paginas/references/templates/` e a skill `vtsd-completo` para a estrutura 8D.

**Regras obrigatórias:**
- Arquivo HTML único (CSS em `<style>`, sem dependências externas além Google Fonts)
- Google Fonts modernas (Inter, Poppins, Montserrat)
- Paleta harmoniosa (máx 3 cores + neutros)
- 100% responsivo (mobile-first)
- Animações CSS sutis (hover, scroll suave)
- Seções com backgrounds alternados
- Botões grandes com efeito hover
- Placeholders de imagem com instrução "[Sua foto aqui]"

**Estrutura 8D para Página de Vendas:**
1. **Primeira Dobra** — Premissa (headline) + subheadline + 3 bullets (Urgência Oculta + Decorado) + vídeo
2. **Paliativo** — O que já tentaram e por que falhou
3. **Método** — Apresentação da Furadeira (macroetapas)
4. **Entregáveis** — Lista completa com metáforas de valor
5. **Bônus** — 3 bônus estratégicos com valor individual
6. **Prova Social** — Depoimentos com foto e resultado
7. **Garantia** — Selo visual + texto
8. **Oferta Final** — Ancoragem de valor + preço + CTA

**Página de Captura:**
1. Hero com headline + formulário (nome, email, WhatsApp)
2. Benefícios (3-4 bullets visuais)
3. O que vai receber
4. Sobre o autor
5. CTA final

**Página de Obrigado:**
1. Confirmação do cadastro/compra
2. Próximos passos claros
3. Instruções de acesso
4. CTA secundário (grupo WhatsApp, redes sociais)

### 4. Inserir Pixel (se configurado)
Leia `.env` e verifique `META_PIXEL_ID`. Se existir, insira o snippet do Facebook Pixel no `<head>` da página com os eventos adequados:
- Captura: evento `Lead` no submit
- Vendas: evento `ViewContent` no carregamento
- Obrigado: evento `Purchase` ou `CompleteRegistration`

Se não existir, gere a página sem Pixel.

### 5. Salvar
- `entregas/paginas/vendas-[produto].html`
- `entregas/paginas/captura-[produto].html`
- `entregas/paginas/obrigado-[produto].html`

### 6. Deploy (se configurado)
Leia `.env` e verifique `VERCEL_TOKEN`. Se existir, execute `vercel deploy` e informe a URL pública.
Se não existir, diga: "Página salva em [caminho]. Abra no navegador para visualizar."

### 7. Próximo Passo
"Use `/anuncio` para criar anúncios que levem tráfego a essa página."
