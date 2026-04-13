---
name: concepcao-produto
description: >
  Base de conhecimento para concepção de produto usando metodologia VTSD.
  Inclui Quadro, Furadeira, Decorados, Urgências Ocultas e 3 Identidades.
  Acionada automaticamente pelos commands /produto-editar e /produto-consumidor.
---

# Concepção de Produto. Base de Conhecimento VTSD

## Quadro (Transformação Principal)

Até 10 palavras. Verbo no infinitivo. Único resultado. Atrativo, claro, específico.

É o **resultado final** que a pessoa CONQUISTA ou SE TORNA após usar o produto. É a chegada, não o caminho.

**Teste rápido:** a pessoa pode dizer "isso aconteceu na minha vida" ao final do produto? Se sim, é Quadro. Se não, é processo.

**O que NÃO é Quadro (processo / meio):**
- "Identificar a crença que te trava" ❌. isso é o processo, não o resultado
- "Descobrir por que você sabota os resultados" ❌. é a investigação, não a chegada
- "Aprender como funciona X" ❌. é o caminho, não a transformação
- Slogan, promessa vaga, frase com imperativo ❌

**O que É Quadro (resultado final concreto e verificável):**
- Falar inglês em 90 dias ✓
- Fechar R$10 mil por mês como social media ✓
- Vender bolo caseiro todos os dias ✓
- Zerar dívidas em até 90 dias sem renda extra ✓
- Ganhar dinheiro sem culpa e guardar sem medo de perder ✓
- Cobrar o que vale sem sentir que está exagerando ✓
- Agir em direção ao que quer sem travar no último momento ✓

## Furadeira (Método)

Caminho claro, replicável e exclusivo. 3-5 macroetapas + microetapas.

**Exemplo. Protocolo Anticoceira:**
1. Raiz do Problema. identificar causa
2. Pele Blindada. higienização + produtos
3. Nutrição Antialérgica. alimentação preventiva

**Visualização da Furadeira (opcional):** depois que a Furadeira estiver definida no `perfil.md`, você pode gerar um diagrama visual da metodologia usando a skill `furadeira-visual`. Ela oferece 5 layouts (linear, roadmap, pirâmide, hub, fluxograma), gera HTML estático e converte para PNG. Útil para usar na seção Método da página de vendas (8D), em carrosséis, slides de pitch e stories. Acione `/furadeira-visual` após o produto estar com a Furadeira cadastrada.

## Decorados (50 Benefícios)

Categorias: Financeiro, Tempo, Autoestima, Reputação, Crescimento.
Gere 50 benefícios diretos e indiretos do Quadro.

## Urgências Ocultas

Estrutura oficial: 7 categorias com exatamente 10 itens cada (totalizando 70 itens). Não gere mais nem menos do que 10 em cada categoria.

1. Dores (problemas que incomodam): 10 itens
2. Dúvidas (perguntas que o público faz): 10 itens
3. Desejos (estados desejados): 10 itens
4. Assuntos Relacionados (temas adjacentes ao nicho): 10 itens
5. Urgências Quentes (alta intenção, ligadas direto à compra): 10 itens
6. Urgências Frias (baixa intenção, alto volume, atração): 10 itens
7. Urgências Inusitadas (ângulo inesperado que chama atenção): 10 itens

Usar como base para conteúdos, ganchos, anúncios e copy.

## 3 Identidades

1. **Comunicador**. Tom, valores, estilo, posicionamento, história
2. **Consumidor**. Demografia, psicografia, dores, desejos, comportamento, objeções, nível de consciência
3. **Produto**. Quadro, diferenciação, analogias, argumentos incontestáveis

## Pesquisa de Mercado (OBRIGATÓRIA em toda concepção)

A pesquisa de mercado NÃO mora mais nesta skill. Toda pesquisa de mercado, concorrência, objeções (Reclame Aqui), SEBRAE, precificação, ângulos virais e biblioteca de anúncios é responsabilidade da skill dedicada **`pesquisa-mercado`**.

**Regra absoluta:** em qualquer fluxo de concepção de produto (novo, low ticket, middle, high ticket, consultoria), a skill `pesquisa-mercado` precisa ser acionada antes de o assistente sugerir preço, posicionamento, identidades completas, oferta, argumentos incontestáveis ou ângulos de comunicação.

Fluxo padrão:
1. Definir nicho, Quadro inicial e formato pretendido.
2. Acionar `pesquisa-mercado` e aguardar o relatório completo em `entregas/{ativo}/pesquisa-mercado.md`.
3. Voltar para esta skill (`concepcao-produto`) usando os dados da pesquisa como insumo para gerar Decorados, enriquecer Urgências Ocultas, definir as 3 Identidades, preço e Argumentos Incontestáveis.

Sem pesquisa, sem sugestão. Se o aluno tentar pular, explicar que a pesquisa é obrigatória porque é ela que transforma "achismo" em decisão fundamentada.

## Níveis de Consciência (Eugene Schwartz)

1. Inconsciente. Não sabe que tem problema
2. Consciente do problema. Sabe que algo está errado
3. Consciente da solução. Sabe que existem soluções
4. Consciente do produto. Conhece seu produto
5. Totalmente consciente. Só precisa da oferta
