---
name: app-saas
description: >
  Transforma uma ideia de aplicativo interno ou SaaS simples (gerenciador de
  assistente virtual, painel, mini CRM, dashboard) em especificação completa
  com schema de banco, telas, user stories e prompt pronto pra colar no
  Lovable.dev. O aluno não escreve código, só cola o prompt e gera o app.
---

# App SaaS. Gerenciador e Ferramentas Internas

Transforma um problema operacional do infoprodutor em uma ferramenta interna pronta pra ser construída no Lovable.dev. Exemplos: gerenciador do assistente virtual, painel de atendimento pros alunos, mini CRM de leads, dashboard de métricas do produto, agendador de aulas. A skill não gera código. Gera a especificação completa + o prompt técnico que o aluno cola no Lovable e o Lovable constrói.

## Quando Usar

- Quando o aluno disser "quero um sistema pra controlar X", "preciso de um painel pra Y", "um CRM simples", "uma ferramenta interna", "um assistente virtual".
- Antes do aluno tentar construir alguma coisa no Lovable sem especificação clara.
- Para qualquer ferramenta interna que o infoprodutor precisa e que uma planilha não resolve mais.

## O Que Fazer

### 0. Contexto

Leia `entregas/.ativo` e `entregas/{ativo}/perfil.md` pra entender o negócio, o Quadro e a identidade visual do produto.
Leia `entregas/{ativo}/idconsumidor.md` (se existir) para entender quem vai usar o sistema e como se comunicar.

### 1. Entrevista (uma pergunta por vez)

**Pergunta 1. Qual problema esse SaaS resolve no seu dia a dia?**
(ex: "perco tempo respondendo as mesmas dúvidas dos alunos", "não sei quem são meus leads mais quentes", "meu assistente vive me perguntando informações que já respondi")

**Pergunta 2. Quem vai usar?**
1. Só eu
2. Eu + meu time (quantas pessoas?)
3. Meus alunos ou clientes (quantos?)
4. Eu + clientes (com login separado)

**Pergunta 3. Quais dados principais precisam ser guardados?**
(ex: nome, email, telefone, status do atendimento, tags, histórico de mensagens, data da última interação)

Se o aluno não souber, ajude sugerindo com base no problema dele.

**Pergunta 4. Quais ações o usuário faz com esses dados?**
(ex: cadastrar, listar, editar, marcar como concluído, filtrar por status, exportar CSV, enviar mensagem)

**Pergunta 5. Precisa de login? Se sim, quantos perfis diferentes?**
(ex: só admin; admin + usuário comum; admin + cliente externo)

### 2. Gerar a especificação

Crie um arquivo `.md` com a seguinte estrutura:

```markdown
# {Nome do App}

## Visão geral
{Três linhas dizendo o que o app faz, pra quem e como muda a rotina do aluno}

## User stories
- Como {perfil}, eu quero {ação}, para {benefício}
- ...

## Schema do banco

### Tabela `tabela1`
- `id` (uuid, pk)
- `nome` (text)
- `email` (text)
- ...
- `created_at` (timestamp)

### Tabela `tabela2`
- `id` (uuid, pk)
- `tabela1_id` (uuid, fk)
- ...

## Telas
1. **Login** - {descrição}
2. **Dashboard** - {descrição}
3. **Lista de X** - {descrição + filtros}
4. **Detalhe de X** - {descrição + ações}
5. **Formulário de X** - {campos}

## Regras de negócio
- {regra 1}
- {regra 2}

## Prompt pro Lovable.dev

{prompt técnico completo em português, formatado como instrução direta pro Lovable}
```

### 3. Prompt pro Lovable

O prompt precisa:
- Começar com "Crie um aplicativo web de {nome} com as seguintes características"
- Especificar stack: React + Tailwind + Supabase (padrão do Lovable)
- Listar todas as telas com a ordem de navegação
- Descrever o schema do banco de forma que o Lovable entenda e crie as tabelas no Supabase
- Definir identidade visual: cores (puxar do perfil do produto se existir), fonte (Inter como padrão), estilo (clean e profissional)
- Instruções de UX: menu lateral, tabelas com paginação, botões de ação visíveis, formulários validados
- Pedir texto em português do Brasil em toda a interface
- Instruir a não usar emojis a não ser nos ícones padrão
- Fechar com "Ao finalizar, me mostre o preview e me diga quais passos ainda faltam pra eu começar a usar"

### 4. Aprovação e entrega

Mostre a especificação completa + prompt e peça:
```
1. Aprovar e salvar
2. Quero ajustar algo
```

Após aprovação, salve em `entregas/{ativo}/apps/{slug-do-app}.md`.

### 5. Próximos passos

```
Pronto. Especificação salva.

Arquivo: entregas/{ativo}/apps/{slug}.md

Próximos passos:
1. Acesse lovable.dev e faça login
2. Clique em "New Project"
3. Cole o prompt da seção "Prompt pro Lovable.dev"
4. Aguarde a geração
5. Se precisar ajustar, peça mudanças em linguagem natural dentro do Lovable
6. Quando estiver pronto, publique e volte aqui pra conectar com /pagina-vercel se quiser domínio próprio
```

## Regras

- Sempre começar pelo problema real, nunca pela tecnologia.
- Schema simples. Máximo 5 tabelas na primeira versão.
- Nunca entregar código nessa skill. Código é responsabilidade do Lovable. A skill entrega especificação + prompt.
- Prompt pro Lovable sempre em português e bem direto.
- Respeitar a identidade visual do produto ativo (pegar cores e fontes do `perfil.md` se existir).
- Se o problema puder ser resolvido com uma planilha no Google Sheets ou com `/criar-gpt`, dizer isso ao aluno antes de gerar um SaaS completo.
- Não usar travessão em nenhum texto exibido.
