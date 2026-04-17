---
name: workshop-marketing:produto-novo
description: Criar um novo produto/projeto e defini-lo como produto ativo.
---

# Novo Produto. Criar e Ativar

Cria uma nova pasta de produto dentro de `produtos/` e a define como produto ativo.

## Usage

```
/produto-novo
```

## O Que Fazer

### 1. Verificar se já tem produto

Primeira pergunta obrigatória:

```
Você já tem um produto ou ideia de produto?

1. Sim, já tenho
2. Não, quero descobrir o que criar

Digite o número:
```

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

Guarde o tipo escolhido. Ele será salvo no arquivo `produtos/{slug}/tipo.md`.

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

Verifique se já existe uma pasta `produtos/{slug}/`. Se existir, informe:
```
Já existe um produto com esse identificador. Quer usar /produto-trocar para acessá-lo?
```

#### Passo 5. Criar estrutura de pastas

Crie as seguintes pastas:
```
produtos/{slug}/
produtos/{slug}/entregas/
produtos/{slug}/entregas/paginas/
produtos/{slug}/entregas/anuncios/
produtos/{slug}/entregas/emails/
produtos/{slug}/entregas/copy-pagina/
produtos/{slug}/entregas/conteudo-social/
produtos/{slug}/entregas/criativos/
produtos/{slug}/entregas/comercial/
produtos/{slug}/entregas/textos-de-venda/
```

#### Passo 6. Definir como produto ativo

Salve o slug em `produtos/.ativo` (sobrescreva o conteúdo anterior).

#### Passo 7. Salvar o tipo do produto

Salve o tipo escolhido em `produtos/{slug}/tipo.md`.

#### Passo 8. Confirmar e sugerir próximo passo

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

Com a especialidade informada, rode imediatamente a **pesquisa de mercado completa** usando WebSearch. Esta é a pesquisa definitiva, que alimentará as 100 ideias, a sugestão de preço e todo o fluxo do `/produto-concepcao`. Não refaça em nenhuma etapa posterior.

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

Salve o resultado em um arquivo temporário que será movido para `produtos/{slug}/pesquisa-mercado.md` assim que o produto for registrado.

#### Passo 3. Gerar 100 ideias de infoprodutos

Com base na pesquisa de mercado e no conceito de **urgências ocultas**, gere uma tabela com 100 ideias de infoprodutos altamente diferenciados para o nicho informado.

**Conceito de urgências ocultas aplicado às ideias:**
- **Dores:** problemas que o público sofre e que o produto resolve
- **Dúvidas:** perguntas reais que o público faz e que abrem porta para o produto
- **Desejos:** estados que o público quer alcançar
- **Assuntos relacionados:** temas adjacentes que atraem o mesmo público
- **Urgências quentes:** pessoas com alta intenção de compra no nicho
- **Urgências frias:** volume alto de busca, baixa intenção direta, mas público certo
- **Urgências inusitadas:** conexões inesperadas e criativas que chamam atenção

**Colunas da tabela:**
| Título do Produto | Subnicho | Diferencial | Formato | Prós |

**Regras para as ideias:**
- Evite ideias genéricas. Use criatividade e ângulos inusitados
- Gere ofertas com alto desejo e urgência natural
- Pense em métodos pouco conhecidos, tecnologias emergentes, estratégias exclusivas
- Os produtos precisam ser simples, fáceis de consumir e permitir picos de vendas
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

Mova ou salve a pesquisa de mercado em `produtos/{slug}/pesquisa-mercado.md`.

#### Passo 6. Confirmar e sugerir próximo passo

```
Produto "{nome}" criado e ativado.
Identificador: {slug}
Tipo: {tipo}

A pesquisa de mercado do nicho já foi feita e está salva.
Ela será usada em todas as etapas seguintes sem nova busca.

Próximo passo: /produto-concepcao para cadastrar Quadro, Furadeira, Identidades e Urgências Ocultas.
```
