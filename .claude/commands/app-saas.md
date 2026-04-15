---
name: workshop-marketing:app-saas
description: Criar um SaaS simples (gerenciador de assistente virtual, painel de clientes, minicrm, dashboard interno) a partir de um briefing de negócio. Gera especificação completa, schema do banco, telas e prompt pronto para colar no Lovable.dev.
---

# App SaaS. Gerenciador de Assistente Virtual

Transforma uma ideia de aplicativo interno ou SaaS simples em especificação técnica pronta para ser construída no Lovable.dev sem precisar escrever código. Ideal pra gerenciador de assistente virtual, painel de atendimento, CRM leve, dashboard de métricas ou qualquer ferramenta interna do infoprodutor.

## Usage

```
/app-saas
```

## O Que Fazer

Acione a skill `app-saas` do plugin `workshop-marketing` e siga o roteiro:

1. Ler `entregas/.ativo` e `entregas/{ativo}/perfil.md` pra pegar contexto do negócio.
2. Coletar (uma pergunta por vez):
   1. Qual problema esse SaaS resolve? (ex: "perco tempo respondendo as mesmas dúvidas dos alunos", "não tenho onde centralizar leads")
   2. Quem usa? (só você, seu time, seus alunos, seus clientes)
   3. Quais dados precisam ser guardados? (ex: nome, email, histórico de mensagens, status, tags)
   4. Quais ações o usuário precisa fazer? (cadastrar, listar, editar, marcar como concluído, enviar mensagem)
   5. Precisa de login? Se sim, quantos perfis (admin, usuário comum, etc)?
3. Gerar em um único arquivo `.md`:
   - **Visão geral** do SaaS em 3 linhas
   - **User stories** curtas (como X, eu quero Y, para Z)
   - **Schema do banco** em formato simples (tabela, campos, tipo, relações)
   - **Telas** necessárias (login, dashboard, lista, detalhe, formulário)
   - **Regras de negócio** importantes
   - **Prompt técnico pronto pro Lovable.dev**, já formatado com stack sugerida (React + Tailwind + Supabase), estrutura de páginas e instruções de UX em português. Incluir esquema de cores baseado na identidade do produto ativo.
4. Mostrar o conteúdo gerado e pedir aprovação.
5. Salvar em `entregas/{ativo}/apps/{nome-do-app}.md`.
6. Sugerir próximo passo: copiar o prompt técnico e colar no Lovable.dev (lovable.dev > New Project).

## Regras Resumidas

- Sempre começar pelo problema real, não pela tecnologia.
- Schema precisa ser simples, no máximo 5 tabelas na primeira versão.
- Nunca entregar código. Só especificação + prompt pro Lovable.
- Prompt do Lovable precisa ser em português, direto, com instruções de UX.
- Respeitar a Mandala de cores e fonte do produto ativo (pegar do `perfil.md` se existir).
- Não usar travessão em nenhum texto exibido.
