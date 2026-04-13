---
name: playbook-comercial
description: >
  Base de conhecimento para vendas 1:1. SPIN Selling adaptado, scripts de fechamento,
  quebra de objeções e pitch comercial. Baseado na metodologia C10X do VTSD.
  Entregável final: HTML único, bem formatado, pronto para impressão e exportação em PDF.
  Acionada pelo command /comercial-playbook.
---

# Playbook Comercial. Base de Conhecimento (C10X)

## SPIN Selling Adaptado

**S. Situação:** Entender o cenário atual
**P. Problema:** Identificar a dor principal
**I. Implicação:** Amplificar o custo de não resolver
**N. Necessidade de Solução:** Criar visão do resultado ideal

## Script de Fechamento

1. Conexão dor-solução: "Sua dificuldade é [DOR]. É exatamente isso que [PRODUTO] resolve: em [TEMPO] você consegue [TRANSFORMAÇÃO]."
2. Ancoragem de valor: Compare com alternativas do mercado
3. Preço + confirmação: "Tudo isso por [VALOR]. Acessível, né?"
4. Envio do link: "Vou te enviar o checkout. Me confirma a compra que libero seus acessos."

⚠️ Nunca pergunte "quer comprar?". Assuma o interesse.

## Quebra de Objeções

| Objeção | Resposta |
| --- | --- |
| "Preciso pensar" | "O que especificamente? Talvez eu esclareça agora." |
| "Está caro" | "Comparado a quê? Quanto custa NÃO resolver?" |
| "Falar com [pessoa]" | "O que acha que [pessoa] diria? Qual a preocupação?" |
| "Não é o momento" | "Quando seria? O que precisa acontecer?" |

## Mentoria vs Consultoria

| Aspecto | Mentoria | Consultoria |
| --- | --- | --- |
| Foco | Desenvolvimento pessoal | Solução específica |
| Duração | 3-12 meses | Projeto definido |
| Entrega | Orientação + feedback | Execução + entrega |
| Preço | Recorrente ou pacote | Por projeto |

## Upsell, Downsell e Order Bump

**Upsell:** Oferta complementar pós-compra (acelera resultado)
**Downsell:** Oferta menor para quem não comprou (mantém relacionamento)
**Order Bump:** Complemento no checkout (impulso, preço baixo)

## Entregável final obrigatório: HTML (PDF pelo navegador)

O produto que o aluno guarda e compartilha **não** é Markdown. É **um arquivo HTML único** salvo em `entregas/{ativo}/comercial/playbook-[slug].html` (slug derivado do nome do produto, kebab-case, sem acentos problemáticos no nome do arquivo).

### Requisitos do HTML

1. **Arquivo único:** todo o CSS em `<style>` no `<head>`. Sem dependências externas obrigatórias. Opcional: uma fonte do Google Fonts (ex.: DM Sans ou Source Sans 3) via link, aceitável para PDF.
2. **Linguagem e acessibilidade:** `<html lang="pt-BR">`, `<meta charset="utf-8">`, `<meta name="viewport" ...>`, `<title>` descritivo (ex.: Playbook comercial · Nome do produto).
3. **Tipografia e layout:** largura máxima legível (cerca de 720px a 840px centralizada), hierarquia clara de `h1` a `h3`, espaçamento confortável, contraste adequado. Tabelas com bordas leves ou zebrado sutil; não depender só de cor para significado.
4. **Conteúdo:** incluir **todas** as seções geradas conforme o tipo escolhido no comando (SPIN, pitch, objeções, WhatsApp, ou playbook completo). Texto contextualizado com `perfil.md` (Quadro, oferta, preço). Incluir sempre no playbook completo: bloco de contexto (produto, preço, origem do lead), SPIN com perguntas prontas, fechamento, quebra de objeções (tabela), mentoria vs consultoria, upsell ou downsell ou order bump quando fizer sentido ao produto.
5. **Capa interna:** primeira seção com título do documento, nome do produto, faixa de preço, origem do lead e uma linha de uso (documento de uso interno ou equipe comercial).
6. **Impressão e PDF:** estilos `@media print` com margens (`@page` se útil), `page-break-inside: avoid` em tabelas e cartões de seção, fundo branco na impressão, links com cor legível. Rodapé visível com instrução curta: abrir no navegador, Imprimir (Ctrl+P), destino “Salvar como PDF”, layout retrato.

### O que não fazer

- Não salvar só `.md` como entrega principal do comando (salvar HTML; Markdown só se o usuário pedir cópia em texto).
- Não mostrar o código HTML no chat ao usuário final: salvar o arquivo e informar o caminho, mais a dica de PDF (conforme `CLAUDE.md` para páginas HTML).
