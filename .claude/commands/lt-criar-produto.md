---
name: workshop-marketing:lt-criar-produto
description: Cria o conteúdo real do produto digital de entrada. e-book, checklist, mini-curso, desafio, agente GPT ou planilha. Gera o arquivo pronto para entregar ao comprador.
---

# Criar Produto Low Ticket

Cria o conteúdo real do produto digital (o que o comprador vai receber), confirmando cada etapa com o usuário antes de avançar.

## Usage

```
/lt-criar-produto
```

## O Que Fazer

### 1. Contexto

Leia:
- `entregas/.ativo` → se não existir, oriente a usar `/produto-novo` primeiro
- `entregas/{ativo}/perfil.md` → se não existir, oriente a usar `/produto-editar` primeiro

### 2. Verificar formato

Leia `entregas/{ativo}/perfil.md` e identifique se o formato do produto já está definido.

**Se o formato já estiver no perfil**, confirme com o usuário:

```
Encontrei seu produto: [nome do produto]
Formato: [formato identificado no perfil]

Vou criar o conteúdo do produto agora.

1. Sim, pode seguir
2. Quero escolher outro formato
```

**Se o formato não estiver no perfil** ou o usuário quiser trocar, apresente as opções:

```
Qual é o formato do produto que vou criar?

1. E-book / Guia (PDF passo a passo)
2. Checklist / Roteiro de autoaplicação
3. Mini-curso (3 a 5 aulas curtas em vídeo)
4. Desafio (5 a 7 dias com tarefas diárias)
5. Agente GPT (assistente de IA personalizado)
6. Planilha (ferramenta de cálculo ou organização)

Digite o número:
```

### 3. Criar o produto

Leia `.claude/plugins/workshop-marketing/skills/criacao-produto-low-ticket/SKILL.md` e siga o fluxo do formato escolhido.

### 4. Próximo passo

Após salvar o produto, sugira:

```
Produto criado e salvo.

Próximo passo sugerido:
- Use /copy-pagina para criar a página de vendas do produto
- Use /copy-anuncio para criar anúncios que levam tráfego à página
```
