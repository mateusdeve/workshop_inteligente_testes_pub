---
name: workshop-marketing:comercial-playbook
description: Gerar o playbook comercial completo de venda 1:1 por WhatsApp (middle e low ticket) do produto ativo. Cobre abordagem ativa, abordagem receptiva, recuperação de carrinho, follow-up, 15 pontos de convicção, frases de escassez e quebra de objeções pelo Framework dos 7 Argumentos. Entrega em HTML único, pronto para leitura e exportação em PDF.
---

# Playbook Comercial. Venda 1:1 por WhatsApp (Middle e Low Ticket)

Gera o **playbook comercial completo** de venda 1:1 por WhatsApp do produto ativo, usando toda a identidade do produto, do consumidor e do comunicador já cadastrada. **Escopo:** abordagem ativa (outbound), abordagem receptiva (inbound) e recuperação de carrinho. Produtos middle ou low ticket.

**Fora de escopo:** call de venda presencial ou por vídeo, venda high ticket (C10X), pitch de palco, proposta formal de consultoria. Para esses, ver `/ht-*`.

**Produto final:** arquivo **HTML** único, bem formatado, com CSS para tela e impressão, convertível em PDF pelo navegador (Imprimir, Salvar como PDF). Siga a skill `playbook-comercial` para estrutura e requisitos do HTML.

## Usage

```
/comercial-playbook
```

## Princípio

Esta skill faz **uma coisa só:** o playbook comercial completo de WhatsApp 1:1 do produto. Não gera pitch isolado, nem só objeções, nem só recuperação de carrinho. Sempre o playbook completo, em um único HTML.

O playbook tem **duplo público:**

1. **Time comercial** que não conhece o produto. Precisa aprender o Quadro, a Furadeira, a identidade do consumidor e a voz do comunicador dentro do próprio documento.
2. **Produtor do produto** que atende o WhatsApp. Precisa de mensagens prontas, fluxos de abordagem, sequências de recuperação, quebra de objeções na ponta da língua.

Por isso o playbook é prático, visual, didático, dinâmico e totalmente personalizado. Toda informação vem dos arquivos do produto (perfil, identidade do consumidor, painel de entregas). A skill não pergunta dados que já existem no disco.

## O Que Fazer

### 1. Contexto (leitura automática, sem perguntas)

Leia, nesta ordem:

1. `meus-produtos/.ativo`. Identificador do produto ativo.
2. Listagem de `meus-produtos/`. Conte quantos produtos estão cadastrados (subpastas com `perfil.md`).
3. `meus-produtos/{ativo}/perfil.md`. Obrigatório. Quadro, Furadeira, Decorados, 3 Identidades (Produto, Consumidor, Comunicador), Urgências Ocultas (7 categorias × 10 itens), preço, oferta, Argumentos Incontestáveis e diferenciais.
4. `meus-produtos/{ativo}/idconsumidor.md`. Obrigatório para este comando. Contém as 5 objeções com as 7 quebras de 2 parágrafos cada (Framework dos 7 Argumentos), paliativos, frases do público, tom e baldes de para quem é.
5. `meus-produtos/{ativo}/painel-entregas.html`. Se existir. Fonte visual de referência com os mesmos dados organizados.
6. Arquivos complementares em `meus-produtos/{ativo}/entregas/*` (páginas, concepção, anúncios). Leitura leve, para capturar linguagem e argumentos já aprovados.

Se `perfil.md` não existir, pare e oriente a usar `/produto-concepcao` antes.

Se `idconsumidor.md` não existir ou não tiver as 5 objeções com as 7 quebras completas, pare e oriente a usar `/produto-consumidor` antes. O playbook depende desses dados para a seção de quebra de objeções.

### 2. Escolha de produto (pergunta condicional)

**Única situação em que a skill faz pergunta:** quando existe mais de um produto cadastrado em `meus-produtos/`.

**Se só existe um produto cadastrado:** pule esta etapa e siga direto para a geração.

**Se existem dois ou mais produtos cadastrados:**

```
Encontrei [N] produtos cadastrados. Pra qual deles vou gerar o playbook comercial de WhatsApp?

1. [nome do produto 1] (ativo)
2. [nome do produto 2]
3. [nome do produto 3]
...

Digite o número:
```

O produto ativo aparece marcado como `(ativo)` na lista. Se o usuário escolher um produto diferente do ativo, use esse produto como base para leitura e para o caminho de salvamento, mas **não altere** `meus-produtos/.ativo` (troca de produto ativo é responsabilidade do `/produto-trocar`).

### 3. Geração (sem pedir nada ao usuário)

Monte o conteúdo do playbook **dentro do HTML**, usando os dados lidos no passo 1. Use a **Identidade do Comunicador** (tom de voz, palavras que conectam, palavras que afastam) como guia de escrita de **todo** o texto do playbook. Se o comunicador usa linguagem técnica, o playbook fala técnico. Se é coloquial, fala coloquial. O playbook tem a voz do comunicador em cada mensagem.

Todos os scripts respeitam os **7 princípios de venda por WhatsApp** (ver SKILL).

Inclua **todas** as 16 seções abaixo, nesta ordem:

**1. Capa interna:**
- Título do documento (ex: "Playbook comercial WhatsApp · [Nome do produto]")
- Nome do produto
- Valor do curso em destaque (do `perfil.md`, faixa de preço ou valor cheio)
- Selo "Venda 1:1 por WhatsApp"
- Objetivo ("Converter lead em aluno via WhatsApp 1:1 em fluxos de abordagem ativa, receptiva e recuperação de carrinho")
- Linha "Como usar este playbook": dois caminhos rápidos. Time começa pelas identidades (blocos 2 ao 5) para aprender o produto. Produtor vai direto ao cenário (abordagem ativa, receptiva ou recuperação) conforme o atendimento em mãos.

**2. Identidade do Produto:**
Para o time aprender do zero. Extrair do `perfil.md` e do `painel-entregas.html`.
- Quadro (transformação principal em destaque)
- Furadeira completa (método em macroetapas e microetapas, como trilha numerada)
- Entregáveis (módulos, bônus, planilhas, comunidade, acessos)
- Diferenciais competitivos
- Argumentos Incontestáveis (lista com dado concreto mais fonte)
- Posicionamento (mentoria, curso, programa, método, conforme o produto)

**3. Identidade do Consumidor:**
Para o time saber com quem está falando. Extrair do `idconsumidor.md`.
- Frase "Para quem é" (posicionamento em 1 ou 2 linhas)
- Perfil demográfico (idade, gênero, profissão, renda, nível de consciência, canais)
- Dor central mais dores secundárias (das Urgências Ocultas)
- Desejos (das Urgências Ocultas)
- Paliativos (ferramentas e soluções concorrentes do mercado e por que não entregam o resultado completo)
- 10 frases que o consumidor diria (mistura de dor, desejo e objeção)

**4. Identidade do Comunicador:**
Para o time adotar a voz correta. Extrair do `perfil.md` seção Identidade do Comunicador e do `idconsumidor.md` seção Como se comunicar.
- Tom de voz (parágrafo descritivo)
- Posicionamento do criador (parágrafo descritivo)
- Lista de **palavras que conectam** (8 a 12 termos em pills verdes)
- Lista de **palavras que afastam** (6 a 10 termos em pills rosas)
- Exemplo de frase no tom certo mais versão errada para contraste

**5. Princípios de venda por WhatsApp:**
Os 7 princípios em cards numerados:
1. Mensagens curtas. Uma ideia por mensagem.
2. Evitar áudios no início. Texto primeiro, áudio só depois de 2 ou 3 respostas, máximo 45 segundos.
3. Pergunta curta no final sempre que possível.
4. Nome do lead na primeira e última mensagem.
5. Nunca disparar link sem contexto.
6. Nunca perguntar "quer comprar?". Assumir o interesse.
7. Responder rápido no inbound, dar intervalo no outbound.

**6. 15 pontos para convencer:**
Lista numerada de 15 argumentos de convicção. Cada ponto combina **Urgência Oculta mais Decorado mais voz do comunicador**, formando uma frase pronta para o vendedor encaixar em qualquer momento da conversa no WhatsApp. Fonte: Urgências Ocultas (7 categorias × 10 itens) e 50 Decorados do `perfil.md`. Estrutura de cada ponto:
- Título curto (máximo 8 palavras)
- Frase pronta para WhatsApp (1 a 2 linhas) no tom do comunicador
- Quando usar (gatilho situacional, ex: "quando o lead hesita no preço", "quando diz que falta tempo")

Distribuir os 15 pontos em grupos equilibrados entre as categorias das Urgências Ocultas. Evitar repetir o mesmo ângulo.

**7. Abordagem Ativa. Outbound WhatsApp:**
Fluxo para o vendedor dar o primeiro passo. Lead frio (nunca interagiu) ou morno (seguidor, consumidor de conteúdo, participou de lista).

Sequência em **7 blocos**, cada bloco com **3 variações de mensagem** prontas para copiar e colar e **nota de condução**:

1. Primeiro contato (quebra-gelo mais motivo de ter escrito, sem vender)
2. Qualificação leve (1 ou 2 perguntas sobre o momento atual do lead)
3. Amarrar a dor (Urgência Oculta relevante em forma de pergunta aberta)
4. Oferecer ajuda concreta (conteúdo, troca, resposta a dúvida específica, sem vender)
5. Convite para conversa real (chamar pra falar do problema específico)
6. Transição para diagnóstico (quando o lead engajou, entra no SPIN curto)
7. Encerramento se não engajou (fechar educadamente, marcar para follow-up)

**8. Abordagem Receptiva. Inbound WhatsApp:**
Fluxo para o lead que chega por anúncio, orgânico, link da bio, link da página ou palavra-chave.

Sequência em **6 blocos**, cada bloco com **3 variações de mensagem** prontas e **nota de condução**:

1. Acolhimento imediato (resposta rápida, chama pelo nome, confirma o interesse)
2. Pergunta de posicionamento (o que viu, por que chegou, o que já tentou)
3. Diagnóstico rápido (3 a 5 perguntas curtas no estilo SPIN adaptado)
4. Apresentação conectada (amarra à resposta do lead, usa as palavras dele)
5. Prova mais preço (1 caso real mais revelação de valor no tom certo)
6. Checkout mais confirmação (envia link e pede confirmação com pressuposto do sim)

**9. SPIN adaptado ao WhatsApp:**
24 perguntas totais, **6 por fase**, todas personalizadas ao nicho, ao Quadro e à dor central do produto ativo. Proibido perguntas genéricas. Cada pergunta cita vocabulário, situações, rotinas e paliativos concretos do consumidor.

- **S. Situação (6 perguntas):** cenário atual (rotina, ferramentas, tentativas anteriores, momento de vida)
- **P. Problema (6 perguntas):** dor central trazida à tona
- **I. Implicação (6 perguntas):** custo de não resolver (financeiro, emocional, tempo, reputação, saúde)
- **N. Necessidade (6 perguntas):** visão do resultado ideal conectada ao Quadro

Cada fase inclui nota curta de condução (o que observar, quando avançar, quando repetir em outra angulação).

**10. Apresentação mais ancoragem de preço por texto:**
Sequência de mensagens pronta para copiar e colar:
- Ponte dor-solução em 2 mensagens curtas (com as palavras do lead)
- Descrição objetiva em 3 a 4 mensagens (o que é, como funciona, semana a semana)
- Prova em 3 formatos curtos (caso real, número agregado, depoimento de 1 linha)
- Conexão da Furadeira com o Quadro em 1 mensagem
- Revelação de preço em 4 mensagens: alta (valor total somado), funcional (custo de a dor continuar), preço real, confirmação ("faz sentido pra você?")
- Comparação com paliativos (concorrentes diretos e indiretos) em 1 ou 2 mensagens

**11. Frases de escassez:**
Box destacado com frases prontas formatadas como mensagens de WhatsApp, agrupadas por tipo. Funciona em perpétuo porque apoia escassez real (atenção, bônus, vagas), não fabricada.

- **Escassez de vaga** (2 a 3 frases): turmas, mentoria, acompanhamento limitado
- **Escassez de condição** (2 a 3 frases): preço atual, parcelamento, forma de pagamento
- **Escassez de bônus** (2 a 3 frases): bônus disponível só para quem entra agora
- **Escassez de janela de resposta** (2 a 3 frases): condição só fica em pé por X horas dentro daquela conversa
- **Escassez de janela estratégica** (2 a 3 frases): época do ano, momento do nicho, virada de trimestre

Mínimo total: 12 frases prontas. Todas alinhadas ao tom do comunicador. Sem pressão falsa, sem promessa vaga.

**12. Fechamento em 4 passos (WhatsApp):**
1. Conexão dor-solução: "[Nome], sua dificuldade é [DOR]. É exatamente isso que [PRODUTO] resolve. Em [TEMPO] você consegue [TRANSFORMAÇÃO]."
2. Ancoragem de valor: compare com alternativas reais em 1 ou 2 mensagens curtas.
3. Preço mais confirmação: "Tudo isso por [VALOR]. Faz sentido pra você?"
4. Envio do link: "Vou te mandar o checkout agora. Me confirma a compra que já libero seus acessos."

Proibido perguntar "quer comprar?". Assuma o interesse.

**13. Quebra de objeções pelo Framework dos 7 Argumentos:**

Extrair **todas** as 5 objeções do `idconsumidor.md` com as 7 quebras completas de 2 parágrafos cada. Se o produto tiver mais objeções mapeadas (até 7), incluir todas. Mínimo 5 objeções.

Para cada objeção, renderizar os 7 argumentos na ordem fixa:
1. Argumento Incontestável (dado concreto mais fonte)
2. Argumento Lógico (causa e efeito)
3. Argumento por Analogia (sem celebridades, situações reais)
4. Argumento por Exemplificação (caso real com nome fictício)
5. Argumento de Valor (custo vs. benefício)
6. Argumento de Consequência (agir vs. adiar)
7. Argumento de Contradição (refutação de incoerências)

Cada argumento mostra **2 versões lado a lado**:
- **Versão curta (WhatsApp):** 1 a 2 mensagens prontas para copiar e colar. Recorte da versão completa, sem inventar texto novo.
- **Versão completa:** 2 parágrafos exatamente como estão salvos no `idconsumidor.md`, para o time estudar e para gravar em áudio se fizer sentido.

Layout em accordion (uma objeção por accordion, fechado por padrão). No topo da seção, tabela-resumo com uma linha por objeção e o argumento mais forte (coluna "Argumento principal") para leitura rápida no celular.

**14. Recuperação de Carrinho:**
Sequência temporizada em **7 toques**, cada toque com **2 variações** (mais leve / mais direta):

1. **15 minutos após abandono** (tom de ajuda, "tudo certo com a finalização?")
2. **1 hora** (quebra da primeira objeção provável: preço ou segurança)
3. **4 horas** (prova social curta mais link novo)
4. **D+1 manhã** (nova angulação usando Urgência Oculta diferente)
5. **D+1 noite** (frase de escassez real: bônus, condição ou vaga)
6. **D+3** (última chamada educada, foco na consequência de adiar)
7. **D+7** (encerramento respeitoso mais oferta de downsell se houver)

Todos os toques em formato de mensagem de WhatsApp, respeitando os 7 princípios e a voz do comunicador.

**15. Follow-up de quem não comprou mais Upsell, Downsell, Order Bump:**

**Follow-up:** para leads que conversaram e não fecharam (sem chegar ao checkout). 3 tempos com 2 mensagens por tempo:
- D+1 (lembrete leve mais prova social curta)
- D+3 (nova angulação com Urgência Oculta diferente mais quebra de 1 objeção)
- D+7 (última chamada com escassez real mais oferta de downsell se houver)

**Upsell:** oferta complementar pós-compra, enviada em até 48h pelo WhatsApp. Valor aproximado, formato e frase pronta de oferta em mensagem.

**Downsell:** oferta menor para quem não comprou, enviada no D+7 ou após recusa explícita de preço. Valor aproximado, formato e frase pronta.

**Order bump:** complemento no próprio checkout (impulso, preço baixo). Sugestão de produto, valor e chamada curta.

**16. Checklist de atendimento no WhatsApp:**
- **Antes de abrir a conversa:** 6 a 8 itens (etiquetas no CRM, ambiente sem distração, histórico do lead, material de prova à mão, link do checkout, última mensagem anterior, horário adequado)
- **Durante a conversa:** 6 a 8 itens (nome do lead, uma ideia por mensagem, pergunta no fim, escuta ativa, anotação de objeção real, sinal de compra, sinal de desengajamento, tempo de resposta)
- **Depois do fechamento ou da recusa:** 5 a 6 itens (confirmação de pagamento, liberação de acesso, boas-vindas, agendamento de upsell ou follow-up, registro no CRM, análise do atendimento)

### 4. Aprovação

Apresente um **resumo em texto** no chat (lista das 16 seções que o HTML vai conter mais confirmação do produto, valor do curso, tom do comunicador aplicado e escopo "venda 1:1 por WhatsApp: ativa, receptiva e recuperação de carrinho") e pergunte:

```
1. Aprovar e gerar o HTML
2. Quero ajustar algo
```

Se o usuário pedir ajuste, refaça só o trecho pedido e volte à aprovação.

Exceção: só pule a aprovação se o usuário tiver dito explicitamente na mesma sessão "vai direto à versão final" ou equivalente.

### 5. Salvamento (HTML obrigatório)

- Caminho: `meus-produtos/{produto-escolhido}/entregas/comercial/playbook-[slug].html`
- `[slug]`: nome do produto em kebab-case (ex: `mentoria-marketing-digital`).
- Aplicar checklist completo da skill `playbook-comercial` (arquivo único, CSS embutido, `lang="pt-BR"`, `@media print`, capa, índice clicável no topo, 16 seções, tabelas, accordions de objeções, bolhas de mensagem, timeline de recuperação, rodapé com instrução de PDF).

**Para o usuário:** não colar o código HTML no chat. Informar o caminho do arquivo e, em uma linha, como gerar PDF (abrir no navegador, Ctrl+P, Salvar como PDF, retrato).

### 6. Próximo Passo

"Playbook salvo em HTML. Abra no navegador para revisar ou exportar PDF. Se precisar de tráfego pro WhatsApp, use `/copy-anuncio`. Se ainda não tem página de vendas conectada ao checkout, rode `/copy-pagina` seguido de `/pagina-checkout`."
