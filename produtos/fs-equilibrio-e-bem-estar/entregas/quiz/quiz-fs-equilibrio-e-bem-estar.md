# Quiz RECONECTA — Protocolo FS Equilíbrio e Bem-Estar

---

## PARTE 1 — PERGUNTAS DO QUIZ

---

### TELA DE ENTRADA + PERGUNTA 1

**Headline:** Recupere o equilíbrio entre o corpo e as emoções em 7 dias com 15 minutos por dia

**Subheadline:** Responda 10 perguntas rápidas e descubra exatamente por onde começar com base na sua situação real

**Tempo estimado:** Leva apenas 2 minutos para responder

---

**Pergunta 1 — Segmentação**
Objetivo: Segmentar por rotina e criar identificação imediata
Tipo: multipla_escolha (com image_prompt por opção)

Texto: Como é o seu dia a dia na maior parte das semanas?

A) Trabalho fora e chego em casa com o corpo esgotado (value: trabalha_fora)
Prompt de imagem: "Fotografia realista de mulher entre 35 e 50 anos, expressão de cansaço sereno, sentada num sofá com os sapatos ainda no pé, fundo residencial desfocado, iluminação quente de final de tarde, qualidade fotográfica profissional, sem texto"

B) Trabalho em casa e mistura tudo o tempo todo (value: trabalha_casa)
Prompt de imagem: "Fotografia realista de mulher entre 30 e 45 anos, expressão de sobrecarga leve, sentada em mesa de trabalho home office com notebook, fundo residencial desfocado, iluminação natural, qualidade fotográfica profissional, sem texto"

C) Cuido de alguém além de mim, filhos, pais ou família (value: cuidadora)
Prompt de imagem: "Fotografia realista de mulher entre 35 e 55 anos, expressão de ternura e cansaço ao mesmo tempo, em ambiente doméstico, fundo levemente desfocado, iluminação natural, qualidade fotográfica profissional, sem texto"

D) Sou profissional da saúde e cuido de todo mundo menos de mim (value: profissional_saude)
Prompt de imagem: "Fotografia realista de mulher entre 30 e 50 anos em roupa de trabalho casual, expressão de presença e cansaço contido, fundo neutro desfocado, iluminação natural, qualidade fotográfica profissional, sem texto"

---

### PERGUNTA 2 — Situação

Objetivo: Capturar dado numérico real para usar na Implicação (P6)
Tipo: calculadora

Texto: Quanto tempo você já convive com esse nível de tensão no corpo?

Campo 1: Anos convivendo com a tensão (unidade: anos | chave: anos_tensao)
Campo 2: Dias por semana em que a tensão aparece de forma intensa (unidade: dias | chave: dias_semana_tensao)
Fórmula: campo1 × 52 × campo2
Texto do resultado: "Em todo esse período, você passou por aproximadamente {resultado} dias carregando essa tensão. Esse é o peso real do que você está vivendo."
Botão após calcular: "Entendi, continuar →"

---

### PERGUNTA 3 — Situação

Objetivo: Mapear o comportamento atual diante da tensão
Tipo: multipla_escolha

Texto: Quando você sente tensão no corpo, o que costuma fazer?

A) Tomo remédio ou peço massagem e espero passar (value: remedio_massagem)
B) Respiro fundo, tomo uma água e sigo em frente (value: respira_segue)
C) Ignoro e continuo com o que estava fazendo (value: ignora)
D) Paro um momento, mas não sei muito bem o que fazer (value: para_nao_sabe)

---

### PERGUNTA 4 — Problema

Objetivo: Confirmar a dor central com comprometimento direto
Tipo: sim_nao

Texto: Você já acordou cansada mesmo tendo dormido o tempo suficiente?

Sim (value: sim) | Não (value: nao)

---

### PERGUNTA 5 — Problema

Objetivo: Identificar o comportamento-problema mais recorrente
Tipo: multipla_escolha

Texto: Qual dessas situações se repete com mais frequência na sua vida?

A) Tensão no pescoço ou nos ombros que não passa nem com massagem (value: tensao_pescoco)
B) Me irrito ou fico impaciente por causas que não justificam a reação (value: irritabilidade)
C) Me sinto sobrecarregada mesmo quando minha agenda está razoável (value: sobrecarga)
D) Tenho dificuldade de parar mesmo quando o corpo está pedindo descanso (value: nao_consegue_parar)

---

### PERGUNTA 6 — Implicação

Objetivo: Confrontar a pessoa com o custo acumulado usando os dados de P2
Tipo: calculadora

Texto: Veja o que esse tempo representa na prática:

Campo 1: Anos com tensão intensa (unidade: anos | chave: anos_tensao — valor carregado de P2)
Campo 2: Dias por semana com tensão (unidade: dias | chave: dias_semana_tensao — valor carregado de P2)
Fórmula: campo1 × 52 × campo2
Texto do resultado: "Você passou por aproximadamente {resultado} dias carregando tensão intensa no corpo. A maioria das pessoas nunca para para ver esse número. Agora que você viu, o que sente?"
Botão após calcular: "Continuar →"

---

### PERGUNTA 7 — Implicação

Objetivo: Aprofundar a tensão emocional gerada pela calculadora
Tipo: slider

Texto: O quanto essa tensão tem interferido na sua qualidade de vida?

Mínimo (1): Quase nada, consigo lidar bem com ela
Máximo (10): Muito, ela afeta tudo ao meu redor
Chave: nivel_interferencia_tensao

---

### PERGUNTA 8 — Necessidade (Visualização Profunda)

Objetivo: Mover do problema para o desejo com cenas cotidianas concretas
Tipo: multipla_escolha

Texto: Imagine que daqui a 7 dias você já recuperou o equilíbrio entre o corpo e as emoções. O que mudou primeiro na sua vida?

A) Acordo sem aquela sensação de peso nos ombros que acompanha desde a noite anterior (value: acorda_leve)
B) Minha filha me pergunta por que estou mais presente e paciente do que de costume (value: mais_presente)
C) Paro no meio do dia e percebo que respirei fundo sem precisar me lembrar de fazer isso (value: respira_natural)
D) Durmo e acordo sentindo que o sono realmente descansou (value: sono_descansado)

---

### PERGUNTA 9 — Necessidade

Objetivo: Mapear o que o lead precisa para agir agora
Tipo: multipla_escolha

Texto: Para recuperar esse equilíbrio, o que você mais precisa neste momento?

A) Uma prática simples que caiba até nos dias mais corridos (value: pratica_simples)
B) Entender o que está causando a tensão, não só aliviar o sintoma (value: entender_causa)
C) Uma guia que me oriente sem me sobrecarregar com informação (value: guia_orientacao)
D) Algo que continue disponível depois que eu terminar, para não me deixar sozinha (value: suporte_continuo)

---

### PERGUNTA 10 — Diagnóstico Final

Objetivo: Preparar o lead para a Tela de Resultado conectando ao Quadro
Tipo: multipla_escolha

Texto: Quando você imagina se cuidar de verdade, o que passa pela sua cabeça primeiro?

A) Vontade, mas não sei por onde começar (value: vontade_sem_caminho)
B) Culpa de tirar tempo para mim com tanta coisa para fazer (value: culpa)
C) Dúvida, já tentei outras coisas antes e não funcionou (value: duvida)
D) Certeza de que preciso, só falta o caminho certo (value: certeza)

---

## RESUMO DO QUIZ

- Tela de Entrada + P1 com prompts de imagem: OK
- S — Situação: P2 (calculadora) e P3 (múltipla escolha)
- P — Problema: P4 (sim/não) e P5 (múltipla escolha)
- I — Implicação: P6 (calculadora com dados de P2) e P7 (slider)
- N — Necessidade: P8 (visualização profunda) e P9 (múltipla escolha)
- Diagnóstico Final: P10 (múltipla escolha)
- Total: 10 perguntas
- Tipos usados: Calculadora (P2, P6), Múltipla Escolha (P1, P3, P5, P8, P9, P10), Sim/Não (P4), Slider (P7)

Lógica de conversão: A calculadora P2/P6 cria confronto emocional com o tempo perdido. A visualização P8 ancora o desejo em cenas cotidianas concretas, preparando o lead para reconhecer o produto como o caminho mais curto.

---

## TELA DE RESULTADO

**Título:** Seu corpo está carregando mais do que deveria, e você já sabe disso

**Mensagem para quem respondeu A (trabalha fora, chega exausta):**
Você passa o dia inteiro dando conta de tudo, e quando chega em casa o que sobra é o peso que ficou acumulado no corpo. Essa tensão que você sente não é fraqueza. É o resultado de anos sem uma ferramenta que ajude o seu sistema nervoso a soltar o dia antes de começar o próximo. O problema não é falta de disposição. É que ninguém te ensinou como fazer isso de forma prática.

**Mensagem para quem respondeu B (trabalha em casa, mistura tudo):**
Quando o trabalho e a vida pessoal dividem o mesmo espaço, o corpo nunca recebe o sinal de que pode descansar. A tensão que você sente é o resultado dessa confusão de fronteiras. O que está faltando é uma prática que marque para o seu sistema nervoso quando o dia terminou e o cuidado com você começa.

**Mensagem para quem respondeu C (cuida de alguém além de si):**
Cuidar de quem você ama tem um custo que raramente aparece no diagnóstico médico. Ele aparece no pescoço travado, na respiração curta, no cansaço que o sono não resolve. Você está dando o tempo todo sem receber de volta, e o corpo está registrando isso. O que você precisa não é de mais uma hora no dia. É de uma prática que reconecte você a si mesma em poucos minutos.

**Mensagem para quem respondeu D (profissional da saúde):**
Você passou anos aprendendo a cuidar dos outros. E provavelmente sabe, melhor do que ninguém, o que acontece quando o cuidador não se cuida. A tensão que você carrega tem nome, você conhece a teoria. O que está faltando é um caminho prático para aplicar em si mesma o que já ensina para os seus pacientes.

**Parágrafo final (igual para todas):**
O que os seus dados mostram é que essa tensão já dura tempo suficiente para você saber que não vai resolver sozinha com o que já tentou. Existe uma abordagem que une o físico e o emocional ao mesmo tempo, e que cabe em 15 minutos por dia. Os detalhes estão na próxima página.

**CTA:** "Ver como funciona →"

---

## PÁGINA FINAL DE OFERTA

**Headline:** Recupere o equilíbrio entre o corpo e as emoções em 7 dias, com um protocolo criado por quem passa 25 anos vendo o que o estresse faz por dentro

**Subheadline:** Uma fisioterapeuta pélvica e psicanalista criou um desafio de 7 dias para mulheres que sentem a tensão no corpo mas não sabem o que fazer com ela

---

### ANTES x DEPOIS

| Antes | Depois |
|---|---|
| Acorda cansada mesmo depois de dormir | Acorda sentindo que o sono realmente descansou |
| Tensão no pescoço e nos ombros que não passa | Sabe exatamente onde o corpo guarda a tensão e como liberar |
| Respira curto sem perceber | Usa a respiração como ferramenta de regulação |
| Não sabe o que está sentindo, só que está mal | Consegue nomear a emoção por trás da tensão física |
| Tentou de tudo e largou | Tem um ritual de 5 minutos que consegue manter |
| Sem suporte depois que o produto acabou | Agente GPT disponível para continuar a jornada |

---

**R$37,00 — [INSERIR LINK DE CHECKOUT]**

---

### O QUE VOCÊ RECEBE

**Desafio RECONECTA — 7 dias**
- Prática guiada de 10 a 15 minutos por dia
- 7 dias com começo, meio e fim claro: Escuta, Respiração, Liberação, Emoção, Movimento, Integração, Ancoragem
- Caderno do desafio com espaço para anotações em cada dia
- Ao final, um ritual pessoal de 5 minutos montado para a sua realidade
- Baseado em técnicas de fisioterapia pélvica e psicanálise somática, traduzidas para quem não tem formação na área

**Agente GPT RECONECTA**
- Assistente de IA disponível após o desafio
- Sugere práticas com base no que você está sentindo
- Adapta o ritual para momentos diferentes da vida
- Disponível 24h, sem esperar consulta marcada

---

**R$37,00 — [INSERIR LINK DE CHECKOUT]**

---

### GARANTIA

Se em 7 dias você sentir que o desafio não foi o que esperava, basta pedir o reembolso. Sem perguntas, sem burocracia.

---

### QUEM CRIOU

**Fabiana Serricchio** — Fisioterapeuta pélvica há 25 anos e psicanalista desde 2018. Atende em São Paulo, em consultório e domicílio. Criou o Protocolo RECONECTA para levar para fora do consultório o que 25 anos de prática ensinaram sobre o que o corpo guarda quando as emoções não têm espaço.

**[IMAGEM — inserir foto da Fabi aqui]**

**DEPOIMENTOS:**
[IMAGEM — inserir print de depoimento real aqui]
[IMAGEM — inserir print de depoimento real aqui]
[IMAGEM — inserir print de depoimento real aqui]

---

**R$37,00 — [INSERIR LINK DE CHECKOUT]**

---

## PARTE 2 — PROMPT TÉCNICO PARA O LOVABLE.DEV

Cole o prompt abaixo diretamente no Lovable.dev para construir o funil completo.

---

# PROMPT COMPLETO — Quiz RECONECTA + Funil de Vendas + Painel Admin

Crie um sistema completo de funil de vendas baseado em quiz com painel administrativo. O projeto usa React + Vite + TypeScript + Tailwind CSS + Framer Motion + Supabase (Lovable Cloud). Siga CADA detalhe abaixo com exatidão.

---

## 1. IDENTIDADE VISUAL E DESIGN SYSTEM

### Fontes
- Importar do Google Fonts: `Playfair Display` (títulos) e `DM Sans` (corpo/textos)
- No tailwind.config.ts: `fontFamily: { display: ['"Playfair Display"', 'serif'], sans: ['"DM Sans"', 'sans-serif'] }`

### Paleta de cores (CSS variables HSL no index.css)
```
:root {
  --background: 150 20% 97%;
  --foreground: 150 40% 10%;
  --primary: 150 45% 22%;        /* Verde escuro */
  --primary-foreground: 40 50% 94%; /* Creme claro */
  --accent: 25 70% 48%;           /* Terracota */
  --accent-foreground: 150 45% 10%;
  --gold: 25 70% 48%;
  --gold-light: 25 60% 70%;
  --navy: 150 45% 22%;
  --navy-light: 150 30% 38%;
  --cream: 40 50% 96%;
  --rose: 350 55% 52%;
}
```

### Animação especial
- Criar keyframe `pulse-gold` no tailwind.config.ts:
```
"pulse-gold": {
  "0%, 100%": { boxShadow: "0 0 0 0 hsl(25 70% 48% / 0.4)" },
  "50%": { boxShadow: "0 0 0 12px hsl(25 70% 48% / 0)" },
}
```
- Classe `animate-pulse-gold` para todos os botões CTA principais.

---

## 2. BANCO DE DADOS (Supabase / Lovable Cloud)

### Tabela `leads`
```sql
CREATE TABLE public.leads (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at timestamptz NOT NULL DEFAULT now(),
  quiz_answers jsonb DEFAULT '{}'::jsonb,
  email text,
  phone text,
  status text NOT NULL DEFAULT 'aguardando',
  last_step text NOT NULL DEFAULT 'landing',
  name text
);
```
- **status**: `'aguardando'`, `'comprou'`, `'nao_comprou'`
- **last_step**: `'landing'`, `'quiz_pergunta_1'` até `'quiz_pergunta_10'`, `'resultado'`, `'pagina_vendas'`, `'pre_checkout'`
- RLS: permitir SELECT, INSERT, UPDATE, DELETE para `public`

### Tabela `funnel_events`
```sql
CREATE TABLE public.funnel_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at timestamptz NOT NULL DEFAULT now(),
  type text NOT NULL
);
```
- **type**: `'page_view'`, `'quiz_start'`, `'quiz_complete'`, `'sales_view'`, `'pre_checkout'`
- RLS: permitir SELECT, INSERT, DELETE para `public`

---

## 3. TRACKING DE FUNIL (lib/funnel-tracking.ts)

Criar módulo com:
- `ensureVisitorLead()` — verifica/cria lead no localStorage
- `updateVisitorStep(step: string)` — atualiza last_step
- `saveQuizAnswer(questionId: number, answer: string)` — salva resposta
- `completeLeadInfo({ name, email, phone })` — salva dados de contato
- `trackEvent(type)` — registra evento no funnel_events
- `getLeads()` e `getFunnelStats()` — para o admin

---

## 4. LANDING PAGE (rota `/`)

- Tela cheia (min-h-screen) com fundo verde escuro com textura de folhas suaves (usar gradiente: `from-[#1b4332] to-[#2d6a4f]`)
- Overlay sutil sobre o fundo
- Conteúdo centralizado:
  - Badge: "Protocolo RECONECTA" — fundo `bg-accent/20`, cor terracota
  - Título H1: "Recupere o equilíbrio entre o corpo e as emoções em 7 dias com 15 minutos por dia" — Playfair Display, bold, cor creme
  - Subtítulo: "Responda 10 perguntas rápidas e descubra exatamente por onde começar com base na sua situação real" — DM Sans, cor creme com opacidade
  - Botão CTA: "Começar o Diagnóstico →" — fundo terracota (`bg-accent`), `animate-pulse-gold`, tamanho grande
  - Texto: "Leva apenas 2 minutos para responder" — opacidade 50%
- Animações Framer Motion: `initial={{ opacity: 0, y: 30 }}` → `animate={{ opacity: 1, y: 0 }}`
- Ao entrar: `trackEvent("page_view")` e `ensureVisitorLead()`
- Ao clicar: `trackEvent("quiz_start")`, `updateVisitorStep("quiz_pergunta_1")`, ir para quiz

---

## 5. QUIZ (10 Perguntas)

### Estrutura da tela do quiz
- Fundo `bg-background`, centralizado
- Barra de progresso: "Pergunta X de 10", percentual, barra com preenchimento `bg-accent` animado
- Título: Playfair Display, `text-2xl md:text-3xl`, bold
- Subtítulo: DM Sans, `text-muted-foreground`
- Transição AnimatePresence mode="wait"
- A cada resposta: `saveQuizAnswer(id, value)` e `updateVisitorStep("quiz_pergunta_X")`
- Após P10: `trackEvent("quiz_complete")`, `updateVisitorStep("resultado")`, ir para resultado

### PERGUNTA 1 — Segmentação (tipo: multipla_escolha com imagem)
question: "Como é o seu dia a dia na maior parte das semanas?"
subtitle: "Escolha a opção que mais se parece com a sua rotina"
options:
- { label: "Trabalho fora e chego em casa com o corpo esgotado", value: "trabalha_fora", image_prompt: "Fotografia realista de mulher entre 35 e 50 anos, expressão de cansaço sereno, sentada num sofá com os sapatos ainda no pé, fundo residencial desfocado, iluminação quente de final de tarde, qualidade fotográfica profissional, sem texto" }
- { label: "Trabalho em casa e mistura tudo o tempo todo", value: "trabalha_casa", image_prompt: "Fotografia realista de mulher entre 30 e 45 anos, expressão de sobrecarga leve, sentada em mesa de trabalho home office com notebook, fundo residencial desfocado, iluminação natural, qualidade fotográfica profissional, sem texto" }
- { label: "Cuido de alguém além de mim, filhos, pais ou família", value: "cuidadora", image_prompt: "Fotografia realista de mulher entre 35 e 55 anos, expressão de ternura e cansaço ao mesmo tempo, em ambiente doméstico, fundo levemente desfocado, iluminação natural, qualidade fotográfica profissional, sem texto" }
- { label: "Sou profissional da saúde e cuido de todo mundo menos de mim", value: "profissional_saude", image_prompt: "Fotografia realista de mulher entre 30 e 50 anos em roupa de trabalho casual, expressão de presença e cansaço contido, fundo neutro desfocado, iluminação natural, qualidade fotográfica profissional, sem texto" }

### PERGUNTA 2 — Situação (tipo: calculadora)
question: "Quanto tempo você já convive com esse nível de tensão no corpo?"
subtitle: "Vamos calcular o peso real do que você está carregando"
type: calculadora
campo1: { label: "Há quantos anos você sente essa tensão", unit: "anos", key: "anos_tensao" }
campo2: { label: "Quantos dias por semana ela aparece de forma intensa", unit: "dias", key: "dias_semana" }
formula: "campo1 × 52 × campo2"
result_template: "Em todo esse período, você passou por aproximadamente {resultado} dias carregando essa tensão. Esse é o peso real do que você está vivendo."
button_label: "Entendi, continuar →"

### PERGUNTA 3 — Situação (tipo: multipla_escolha)
question: "Quando você sente tensão no corpo, o que costuma fazer?"
subtitle: "Seja honesta, não existe resposta certa ou errada"
options:
- { label: "Tomo remédio ou peço massagem e espero passar", emoji: "💊", value: "remedio_massagem" }
- { label: "Respiro fundo, tomo uma água e sigo em frente", emoji: "💧", value: "respira_segue" }
- { label: "Ignoro e continuo com o que estava fazendo", emoji: "🔄", value: "ignora" }
- { label: "Paro um momento, mas não sei muito bem o que fazer", emoji: "🤷", value: "para_nao_sabe" }

### PERGUNTA 4 — Problema (tipo: sim_nao)
question: "Você já acordou cansada mesmo tendo dormido o tempo suficiente?"
subtitle: "Aquele cansaço que o sono não resolve"
options:
- { label: "Sim", emoji: "✅", value: "sim" }
- { label: "Não", emoji: "❌", value: "nao" }

### PERGUNTA 5 — Problema (tipo: multipla_escolha)
question: "Qual dessas situações se repete com mais frequência na sua vida?"
subtitle: "Escolha a que mais aparece no dia a dia"
options:
- { label: "Tensão no pescoço ou nos ombros que não passa nem com massagem", emoji: "😣", value: "tensao_pescoco" }
- { label: "Me irrito ou fico impaciente por causas que não justificam a reação", emoji: "😤", value: "irritabilidade" }
- { label: "Me sinto sobrecarregada mesmo quando minha agenda está razoável", emoji: "😔", value: "sobrecarga" }
- { label: "Tenho dificuldade de parar mesmo quando o corpo está pedindo descanso", emoji: "🔁", value: "nao_consegue_parar" }

### PERGUNTA 6 — Implicação (tipo: calculadora)
question: "Veja o que esse tempo representa na prática:"
subtitle: "Com base no que você informou antes"
type: calculadora
campo1: { label: "Anos com tensão intensa", unit: "anos", key: "anos_tensao", prefill_from: "P2_campo1" }
campo2: { label: "Dias por semana com tensão", unit: "dias", key: "dias_semana", prefill_from: "P2_campo2" }
formula: "campo1 × 52 × campo2"
result_template: "Você passou por aproximadamente {resultado} dias carregando tensão intensa no corpo. A maioria das pessoas nunca para para ver esse número. Agora que você viu, o que sente?"
button_label: "Continuar →"

### PERGUNTA 7 — Implicação (tipo: slider)
question: "O quanto essa tensão tem interferido na sua qualidade de vida?"
subtitle: "Arraste o marcador para a posição que melhor representa você"
type: slider
min_label: "Quase nada, consigo lidar bem com ela"
max_label: "Muito, ela afeta tudo ao meu redor"
key: "nivel_interferencia"

### PERGUNTA 8 — Necessidade / Visualização Profunda (tipo: multipla_escolha)
question: "Imagine que daqui a 7 dias você já recuperou o equilíbrio entre o corpo e as emoções. O que mudou primeiro na sua vida?"
subtitle: "Escolha a cena que mais representa o que você deseja"
options:
- { label: "Acordo sem aquela sensação de peso nos ombros que acompanha desde a noite anterior", emoji: "🌅", value: "acorda_leve" }
- { label: "Minha filha me pergunta por que estou mais presente e paciente do que de costume", emoji: "💛", value: "mais_presente" }
- { label: "Paro no meio do dia e percebo que respirei fundo sem precisar me lembrar de fazer isso", emoji: "🌿", value: "respira_natural" }
- { label: "Durmo e acordo sentindo que o sono realmente descansou", emoji: "😴", value: "sono_descansado" }

### PERGUNTA 9 — Necessidade (tipo: multipla_escolha)
question: "Para recuperar esse equilíbrio, o que você mais precisa neste momento?"
subtitle: "O que seria mais decisivo para você começar de verdade"
options:
- { label: "Uma prática simples que caiba até nos dias mais corridos", emoji: "⏱️", value: "pratica_simples" }
- { label: "Entender o que está causando a tensão, não só aliviar o sintoma", emoji: "🔍", value: "entender_causa" }
- { label: "Uma guia que me oriente sem me sobrecarregar com informação", emoji: "🧭", value: "guia_orientacao" }
- { label: "Algo que continue disponível depois que eu terminar, para não me deixar sozinha", emoji: "🤝", value: "suporte_continuo" }

### PERGUNTA 10 — Diagnóstico Final (tipo: multipla_escolha)
question: "Quando você imagina se cuidar de verdade, o que passa pela sua cabeça primeiro?"
subtitle: "Última pergunta"
options:
- { label: "Vontade, mas não sei por onde começar", emoji: "🌱", value: "vontade_sem_caminho" }
- { label: "Culpa de tirar tempo para mim com tanta coisa para fazer", emoji: "😞", value: "culpa" }
- { label: "Dúvida, já tentei outras coisas antes e não funcionou", emoji: "🤔", value: "duvida" }
- { label: "Certeza de que preciso, só falta o caminho certo", emoji: "✨", value: "certeza" }

### Mapeamento de values para labels legíveis (Tab RESPOSTAS no admin)
P1: trabalha_fora → "Trabalha fora", trabalha_casa → "Home office", cuidadora → "Cuidadora", profissional_saude → "Prof. saúde"
P3: remedio_massagem → "Remédio/massagem", respira_segue → "Respira e segue", ignora → "Ignora", para_nao_sabe → "Para sem saber"
P4: sim → "Sim", nao → "Não"
P5: tensao_pescoco → "Tensão física", irritabilidade → "Irritabilidade", sobrecarga → "Sobrecarga", nao_consegue_parar → "Não consegue parar"
P7: (valor numérico do slider 1-10)
P8: acorda_leve → "Acorda leve", mais_presente → "Mais presente", respira_natural → "Respira natural", sono_descansado → "Sono descansado"
P9: pratica_simples → "Prática simples", entender_causa → "Entender causa", guia_orientacao → "Guia", suporte_continuo → "Suporte contínuo"
P10: vontade_sem_caminho → "Quer mas não sabe", culpa → "Culpa", duvida → "Dúvida", certeza → "Certeza"

last_step: 'landing', 'quiz_pergunta_1' até 'quiz_pergunta_10', 'resultado', 'pagina_vendas', 'pre_checkout'

---

## 6. TELA DE RESULTADO

- Fundo `bg-background`, centralizado
- Ícone CheckCircle dentro de círculo terracota (`bg-accent/20`), animação spring
- Resultado condicional baseado na resposta da P1:
  - Se `trabalha_fora`: título "Seu corpo acumulou mais do que você percebe", subtítulo "O diagnóstico mostra o que está acontecendo e como resolver"
  - Se `trabalha_casa`: título "O corpo que nunca desliga precisa aprender a fazer isso", subtítulo "O diagnóstico mostra o que está acontecendo e como resolver"
  - Se `cuidadora`: título "Quem cuida de todo mundo precisa de alguém que cuide dela", subtítulo "O diagnóstico mostra o que está acontecendo e como resolver"
  - Se `profissional_saude`: título "Você sabe o que está acontecendo. Falta o caminho para aplicar em si mesma", subtítulo "O diagnóstico mostra o que está acontecendo e como resolver"
- Box com texto personalizado por perfil (usar os textos completos da Tela de Resultado acima)
- Parágrafo final (igual para todos): "O que os seus dados mostram é que essa tensão já dura tempo suficiente para você saber que não vai resolver sozinha com o que já tentou. Existe uma abordagem que une o físico e o emocional ao mesmo tempo, e que cabe em 15 minutos por dia. Os detalhes estão na próxima página."
- Botão CTA: "Ver como funciona →" — terracota, `animate-pulse-gold`, largura total
- Texto segurança: "Acesso imediato · Garantia de 7 dias"
- Ao clicar: `updateVisitorStep("pagina_vendas")`, ir para página de vendas

---

## 7. PÁGINA DE VENDAS

### Hero
- Fundo gradiente verde escuro (`from-[#1b4332] to-[#2d6a4f]`), overlay 80%
- Badge: "Método criado por fisioterapeuta pélvica com 25 anos de experiência" — fundo `bg-accent/20`, cor terracota claro
- H1: "Recupere o equilíbrio entre o corpo e as emoções em 7 dias com 15 minutos por dia" — Playfair Display, creme
- Subtítulo: "Um protocolo criado por quem passa 25 anos vendo o que o estresse faz por dentro"
- CTA: "Quero o Protocolo RECONECTA →" — botão terracota com `animate-pulse-gold`, link âncora para `#oferta`

### Barra de prova social
- 4 itens: "Criado por fisioterapeuta pélvica" | "25 anos de prática clínica" | "Formação em psicanálise" | "Acesso imediato"

### Quadro Antes x Depois
- Título: "O que muda com o Protocolo RECONECTA"
- Tabela 2 colunas (Antes / Depois) com os 6 itens da Página Final de Oferta acima
- Ícone X vermelho para Antes, ícone Check verde para Depois

### Seção de Entregáveis
- Grid 2 colunas
- Card 1: "Desafio RECONECTA — 7 dias" com os 5 benefícios listados
- Card 2: "Agente GPT RECONECTA" com os 4 benefícios listados

### Seção de Oferta (id="oferta")
- Badge: "Acesso imediato" — cor terracota
- Título: "Comece hoje"
- Card de preço com borda terracota (`border-2 border-accent`, rounded-2xl):
  - Preço: "R$ 37,00"
  - Botão: "Quero o Protocolo RECONECTA →" — largura total, terracota, `animate-pulse-gold`
  - Link: [INSERIR LINK DE CHECKOUT]
  - Garantia: "Garantia de 7 dias — se não gostar, devolvemos o valor"
- Checkmarks: "Acesso imediato após a compra", "Pagamento 100% seguro", "Desafio em PDF para baixar", "Agente GPT com link de acesso"

### Sem seção de vídeo (produto low ticket pós-quiz não precisa)

### Depoimentos
- 3 placeholders: [SUBSTITUIR por depoimento real — inserir print aqui]

### Quem Criou
- "Fabiana Serricchio — Fisioterapeuta pélvica há 25 anos e psicanalista desde 2018. Criou o Protocolo RECONECTA para levar para fora do consultório o que décadas de prática ensinaram sobre o que o corpo guarda quando as emoções não têm espaço."
- [SUBSTITUIR por foto real da Fabi]

### FAQ (3 perguntas)
1. "Preciso ter experiência com meditação ou yoga para fazer o desafio?" — Não. O desafio foi criado para quem nunca fez nada do tipo. Cada prática começa do zero.
2. "Quanto tempo preciso separar por dia?" — De 10 a 15 minutos. Menos do que um episódio de série.
3. "O que acontece depois dos 7 dias?" — Você monta o seu próprio ritual de 5 minutos no Dia 7, e o Agente GPT fica disponível para continuar te apoiando no seu ritmo.

### CTA final
- Mesmo botão da seção de oferta
- Texto de reforço: "Garantia de 7 dias. Se não for o que esperava, devolvemos o valor."

### Ao entrar na página: `trackEvent("sales_view")`
### Ao clicar "Quero o Protocolo": abrir modal de pré-checkout

---

## 8. MODAL DE PRÉ-CHECKOUT

- Dialog/Modal com shadcn Dialog
- Título: "Quase lá" — Playfair Display
- Descrição: "Preencha seus dados para garantir o acesso com o preço de hoje."
- 3 campos: Nome completo | E-mail | WhatsApp / Telefone
- Botão: "Garantir meu acesso →" — terracota, largura total
- Texto segurança: "Seus dados estão seguros e não serão compartilhados."
- Após submit: `completeLeadInfo({ name, email, phone })` e `trackEvent("pre_checkout")`
- Redirecionar para [INSERIR LINK DE CHECKOUT] após registro

---

## 9. PAINEL ADMINISTRATIVO (rota `/admin`)

- Header: "Acompanhe a performance do Quiz RECONECTA — Boas Vendas"
- Botão "Limpar dados" com confirmação "DELETAR"
- 5 cards de métricas (mesma estrutura do template original)
- Filtro de período: 30 dias / 7 dias / 24 horas / Data personalizada
- 4 tabs: RESPOSTAS, LEADS, CRM, PERFORMANCE
- Tab RESPOSTAS: 10 colunas (P1 a P10), cores alternadas por pergunta, labels legíveis conforme mapeamento acima
- Tab LEADS: tabela com Nome, E-mail, Telefone, Status, Parou em, Data, botão WhatsApp
- Tab CRM: Kanban com drag-and-drop (Aguardando / Comprou / Não Comprou)
- Tab PERFORMANCE: barra de funil com 14 etapas (landing + 10 perguntas + resultado + vendas + checkout)

**Tipografia admin:** somente DM Sans, texto pequeno (11-13px), sem Playfair Display
**Layout admin:** max-w-[1400px], fundo `#fafafa`, padding generoso
