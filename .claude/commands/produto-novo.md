---
name: workshop-marketing:produto-novo
description: Porta de entrada do projeto. Verifica produto ativo, cria um novo produto ou gera ideias de produto. Acionada automaticamente em QUALQUER nova conversa pela regra de abertura de sessão do CLAUDE.md.
---

<!--
GOVERNANÇA (NÃO REMOVER):

Esta skill é a PORTA DE ENTRADA do projeto. Ela é acionada automaticamente em
toda nova conversa, por força da seção "REGRA DE ABERTURA DE SESSÃO" do
CLAUDE.md, independentemente do texto que o aluno digitou ("olá", "oi",
"começar", "quero um produto", "vamos lá", etc.).

Por isso, a skill precisa atender três cenários possíveis num mesmo ponto de
entrada:

  1) Aluno já tem produto ativo → mostrar qual é e perguntar se quer continuar
     com ele ou criar um novo. NÃO recadastrar sem o aluno pedir.
  2) Aluno quer criar um produto novo (tem ideia) → seguir o fluxo "Ramo 1".
  3) Aluno não tem ideia e quer sugestões → seguir o fluxo "Ramo 2" (pesquisa
     de mercado + 50 ideias).

Futuras edições: mantenham as três opções no Passo 1 e a detecção de produto
ativo no Passo 0. Não quebrem o comportamento determinístico de abertura.
-->

# Novo Produto. Criar e Ativar

Porta de entrada do projeto. Detecta se já existe produto ativo, cria um produto novo ou ajuda a descobrir qual produto criar.

## Usage

```
/produto-novo
```

## O Que Fazer

> **Regra obrigatória de comunicação:** siga o padrão "Pensar em Voz Alta" do CLAUDE.md. Antes de cada operação longa desta skill (pesquisa de mercado, geração de 50 ideias, criação de pasta e arquivos do produto, escrita do perfil.md), anuncie em UMA linha com `🔍 Próximo passo: {ação}. Tempo estimado: cerca de X segundos.` Ao concluir, confirme com `✅ Concluído: {entrega}. Caminho: {caminho}.`
>
> Exemplos desta skill:
> - `🔍 Próximo passo: pesquisar o nicho de {nicho} no Google e TikTok para coletar ângulos e concorrentes. Tempo estimado: cerca de 90 segundos.`
> - `🔍 Próximo passo: gerar 50 ideias de produto a partir da pesquisa de mercado. Tempo estimado: cerca de 30 segundos.`
> - `🔍 Próximo passo: criar a pasta do produto e salvar o tipo.md com o formato escolhido. Tempo estimado: cerca de 5 segundos.`
> - `✅ Concluído: produto {nome} criado e ativado. Caminho: meus-produtos/{slug}/.`

### 0. Verificar produto ativo (SEMPRE primeiro)

Antes de qualquer pergunta, leia `meus-produtos/.ativo`.

**Se o arquivo existir e tiver um slug válido**, leia `meus-produtos/{slug}/perfil.md` (ou `meus-produtos/{slug}/tipo.md` se o perfil ainda não existir) para descobrir o nome do produto e apresente:

```
Você já tem um produto ativo: **{nome do produto}** ({tipo}).

1. Continuar com este produto
2. Criar um produto novo
3. Quero ideias de novo produto

Digite o número:
```

- Se escolher **1**: encerre a skill com a mensagem "Seguindo com **{nome}**. Me diga o que quer criar (copy, página, anúncio, funil) ou digite o comando da skill que quer usar." e pare.
- Se escolher **2**: siga direto para o **Ramo 1** abaixo (pule o Passo 1).
- Se escolher **3**: siga direto para o **Ramo 2** abaixo (pule o Passo 1).

**Se não houver produto ativo** (arquivo `.ativo` inexistente ou vazio), siga para o Passo 1.

### 1. Verificar se já tem produto ou ideia

Primeira pergunta obrigatória (só quando NÃO há produto ativo):

```
Você já tem um produto cadastrado, quer criar um novo, ou quer ideias de produto?

1. Já tenho um produto e quero cadastrar agora
2. Quero criar um produto novo (tenho uma ideia)
3. Quero ideias de produto (ainda não sei o que criar)

Digite o número:
```

- Opção **1** ou **2**: siga para o **Ramo 1**.
- Opção **3**: siga para o **Ramo 2**.

---

### Ramo 1 — "Sim, já tenho"

#### Passo 1. Perguntar o nome do produto

```
Qual o nome deste produto?
(ex: "Curso de Inglês Fluente", "Mentoria Fitness Online", "Tarô para Iniciantes")
```

#### Passo 2. Perguntar o tipo do produto

```
Que tipo de produto é este?

1. Low Ticket (R$7 a R$97. quiz, desafio, mini-curso, agente GPT)
2. Middle Ticket (R$97 a R$997. curso online, workshop, grupo)

Digite o número:
```

Guarde o tipo escolhido. Ele será salvo no arquivo `meus-produtos/{slug}/tipo.md`.

#### Passo 3. Gerar slug automaticamente

Com o nome fornecido, gere um slug em kebab-case (letras minúsculas, sem acentos, palavras separadas por hífen).

Exemplos:
- "Curso de Inglês Fluente" → `curso-ingles-fluente`
- "Mentoria Fitness Online" → `mentoria-fitness-online`
- "Tarô para Iniciantes" → `taro-para-iniciantes`

Apresente para confirmação:
```
Vou criar o produto com o identificador: curso-ingles-fluente

1. Confirmar
2. Quero usar outro nome
```

#### Passo 4. Verificar se já existe

Verifique se já existe uma pasta `meus-produtos/{slug}/`. Se existir, informe:
```
Já existe um produto com esse identificador. Quer usar /produto-trocar para acessá-lo?
```

#### Passo 5. Criar estrutura de pastas

Crie as seguintes pastas:
```
meus-produtos/{slug}/
meus-produtos/{slug}/entregas/
meus-produtos/{slug}/entregas/paginas/
meus-produtos/{slug}/entregas/anuncios/
meus-produtos/{slug}/entregas/emails/
meus-produtos/{slug}/entregas/copy-pagina/
meus-produtos/{slug}/entregas/conteudo-social/
meus-produtos/{slug}/entregas/criativos/
meus-produtos/{slug}/entregas/comercial/
meus-produtos/{slug}/entregas/textos-de-venda/
```

#### Passo 6. Definir como produto ativo

Salve o slug em `meus-produtos/.ativo` (sobrescreva o conteúdo anterior).

#### Passo 7. Salvar o tipo do produto

Salve o tipo escolhido em `meus-produtos/{slug}/tipo.md`.

#### Passo 8. Atualizar o manifest do painel

Rode no terminal para regenerar `meus-produtos/index.js` (o painel global em `painel.html` lê esse arquivo):

```
py -3 scripts/painel-atualizar.py
```

#### Passo 9. Confirmar e sugerir próximo passo

```
Produto "{nome}" criado e ativado.
Identificador: {slug}
Tipo: {tipo}

Próximo passo: /produto-concepcao para cadastrar Quadro, Furadeira, Identidades e Urgências Ocultas.
```

---

### Ramo 2 — "Não, quero descobrir o que criar"

#### Passo 1. Perguntar especialidade

```
Qual é a sua especialidade? O que você ensina ou entrega para as pessoas?
(ex: "Tarô", "Emagrecimento feminino", "Marketing digital para pequenos negócios")
```

#### Passo 2. Pesquisa de mercado completa (UMA vez, agora)

Com a especialidade informada, rode imediatamente a **pesquisa de mercado completa** usando WebSearch. Esta é a pesquisa definitiva, que alimentará as 50 ideias, a sugestão de preço e todo o fluxo do `/produto-concepcao`. Não refaça em nenhuma etapa posterior.

Avise o aluno:
```
Vou fazer uma pesquisa completa do mercado de {nicho} agora.
Isso leva alguns minutos e vai embasar todas as sugestões daqui em diante.
```

Pesquise e colete obrigatoriamente:
- Dados gerais do mercado (tamanho estimado, crescimento, tendências)
- Mínimo 10 concorrentes com: nome, link do Instagram, link da página de vendas, faixa de preço praticada
- Oportunidades identificadas (ângulos pouco explorados, nichos adjacentes, formatos em alta)
- Cuidados e riscos do nicho (saturação, regulatórios, promessas problemáticas)
- Resumo das reclamações do Reclame Aqui dos principais produtores (problemas reais de entrega, resultado, suporte)
- Público real (demografias, comportamento de compra, canais de consumo)

Salve o resultado em um arquivo temporário que será movido para `meus-produtos/{slug}/pesquisa-mercado.md` assim que o produto for registrado.

#### Passo 3. Gerar 50 ideias de infoprodutos

Com base na pesquisa de mercado e no conceito de **urgências ocultas**, gere **50 ideias DIVERSAS** de infoprodutos para o nicho informado. Não são variações da mesma ideia, são 50 conceitos distintos entre si (ângulo, método, público ou promessa diferentes).

**Conceito de urgências ocultas aplicado às ideias:**
- **Dores:** problemas que o público sofre e que o produto resolve
- **Dúvidas:** perguntas reais que o público faz e que abrem porta para o produto
- **Desejos:** estados que o público quer alcançar
- **Assuntos relacionados:** temas adjacentes que atraem o mesmo público
- **Urgências quentes:** pessoas com alta intenção de compra no nicho
- **Urgências frias:** volume alto de busca, baixa intenção direta, mas público certo
- **Urgências inusitadas:** conexões inesperadas e criativas que chamam atenção

**Distribuição obrigatória por formato (10 categorias, mínimo 3 ideias cada, total 50):**
1. Mentoria em grupo
2. Mentoria individual
3. Curso gravado
4. Curso ao vivo (turma fechada)
5. Ebook
6. Template ou kit pronto
7. Consultoria
8. Comunidade paga (assinatura)
9. Workshop (evento curto e intensivo)
10. Serviço (feito para o cliente)

Distribua as 50 ideias entre as 10 categorias garantindo pelo menos 3 em cada. As 20 restantes vão para as categorias com maior aderência ao nicho pesquisado.

**Organização do output:**
Apresente a lista **agrupada por formato**, com um subtítulo para cada categoria e as ideias daquela categoria numeradas logo abaixo. Dentro de cada grupo, use tabela:

```
### Mentoria em grupo

| # | Nome | Público-alvo resumido | Faixa de preço |
|---|------|----------------------|----------------|
| 1 | ... | ... | R$ ... |
```

**Colunas da tabela:**
| # | Nome | Público-alvo resumido | Faixa de preço |

Numeração **contínua de 1 a 50** (não reinicia a cada grupo), para o aluno escolher pelo número depois.

**Regras para as ideias:**
- 50 conceitos distintos, nunca variações da mesma ideia
- Evite ideias genéricas. Use criatividade e ângulos inusitados
- Gere ofertas com alto desejo e urgência natural
- Pense em métodos pouco conhecidos, tecnologias emergentes, estratégias exclusivas
- Os produtos precisam ser simples, fáceis de consumir e permitir picos de vendas
- Faixa de preço coerente com o formato e com os concorrentes mapeados na pesquisa
- Use Light Copy nas descrições: sem exageros, sem promessas vazias, sem ponto de exclamação

#### Passo 4. Usuário escolhe a ideia

```
Qual número da tabela mais te interessa?
(Pode adaptar o título ou combinar elementos de mais de uma ideia)
```

Após a escolha, confirme:
```
Ótima escolha. Vamos criar: "{título escolhido}"

Tipo sugerido com base na ideia e na pesquisa: {Low Ticket / Middle Ticket}
Preço sugerido: R${valor} ({justificativa baseada nos concorrentes mapeados})

1. Confirmar tipo e preço
2. Quero ajustar
```

#### Passo 5. Registrar o produto

Com a ideia aprovada, gere o slug, crie a estrutura de pastas, salve `tipo.md` e defina como ativo (mesmos passos 3 a 6 do Ramo 1).

Mova ou salve a pesquisa de mercado em `meus-produtos/{slug}/pesquisa-mercado.md`.

#### Passo 6. Atualizar o manifest do painel

Rode no terminal para regenerar `meus-produtos/index.js`:

```
py -3 scripts/painel-atualizar.py
```

#### Passo 7. Criar Painel de Entregas com a primeira seção

Agora que `pesquisa-mercado.md` já existe, crie o Painel de Entregas com a seção de pesquisa preenchida e as demais como "Em breve...". O aluno já vai ter algo para visualizar antes de começar a concepção.

Avise:
```
Gerando seu painel de entregas com a pesquisa de mercado...
```

Rode no terminal:
```
py -3 scripts/painel-incremental.py --secao pesquisa
```

O script cria `meus-produtos/{ativo}/painel-entregas.html` com o shell completo (sidebar, navegação e todas as 8 seções como placeholders "Em breve"), e preenche apenas a seção **Pesquisa de Mercado** com os dados do `pesquisa-mercado.md`. Cada bloco seguinte (`/produto-concepcao`) vai atualizando o painel seção por seção.

Confirme ao aluno:
```
Painel criado com a seção Pesquisa de Mercado.
Caminho: meus-produtos/{ativo}/painel-entregas.html
```

#### Passo 8. Confirmar e sugerir próximo passo

```
Produto "{nome}" criado e ativado.
Identificador: {slug}
Tipo: {tipo}

A pesquisa de mercado do nicho já foi feita e está salva.
Ela será usada em todas as etapas seguintes sem nova busca.

Próximo passo: /produto-concepcao para cadastrar Quadro, Furadeira, Identidades e Urgências Ocultas.
```
