---
name: app-saas
description: >
  Lê o perfil do produto ativo, sugere 10 ideias de mini-SaaS relevantes para
  os alunos do infoprodutor (tracker, diagnóstico, planner, gerador, checklist
  interativo etc.) e, após a escolha, gera o PRD completo + prompt técnico
  pronto para colar no Lovable.dev. O aluno não escreve código.
---

# App SaaS. Gerador de Épicos para Alunos

Lê o perfil do produto ativo e propõe 10 ideias de mini-SaaS que o infoprodutor pode entregar como bônus, ferramenta complementar ou produto de entrada. Após a escolha, gera o PRD completo com schema de banco, telas, user stories e o prompt técnico copiável para o Lovable.dev construir.

A skill não gera código. Entrega especificação + prompt.

## Quando Usar

- Quando o aluno quiser criar uma ferramenta digital como bônus do produto ou produto separado.
- Quando disser "quero dar algo a mais pros alunos", "quero um app como bônus", "quero uma ferramenta pra ajudar meu público".
- Antes de o aluno entrar no Lovable sem saber o que pedir.
- Para transformar o conhecimento do nicho em software simples e útil.

## O Que Fazer

### Etapa 1. Leitura mínima de contexto

- Ler `meus-produtos/.ativo` para pegar o slug do produto ativo.
- Ler `meus-produtos/{slug}/perfil.md` completo (é a fonte principal de ideias).
- Fazer `ls` em `meus-produtos/{slug}/` para ver que outros arquivos existem (idconsumidor.md, entregas etc.).
- Se `meus-produtos/{slug}/idconsumidor.md` existir, lê-lo também.

### Etapa 2. Geração de 10 ideias de mini-SaaS

Com base no perfil, no Quadro, na Furadeira, nas Urgências Ocultas e no público descrito, gerar 10 ideias. Cada ideia deve:

- Ser simples de implementar (CRUD + 1 ou 2 features diferenciadas, máximo 5 tabelas).
- Ser relevante para os alunos do infoprodutor (o público do produto, não o criador).
- Resolver um problema real do nicho ou tema.
- Ter potencial como bônus do produto, ferramenta complementar ou mini-produto separado.
- Ser variada em tipo: diagnóstico, calculadora, tracker, gerador, dashboard, checklist interativo, simulador, comparador, planner, biblioteca de recursos.

**Formato obrigatório de apresentação:**

```
## 10 ideias de Epic para [nome do produto]

**1. [Nome da ferramenta]**
O que faz: [1 linha]
Problema que resolve: [1 linha]
Por que faz sentido para o público: [1 linha]
Complexidade: Simples / Média

**2. ...**
```

### Etapa 3. Escolha do usuário

Perguntar:

```
Qual ideia você quer desenvolver?
Digite o número (1 a 10), peça novas ideias ou proponha uma mistura (ex: "misturar a 3 com a 7").
```

Aceitar variações livres: "me dá mais 10", "adapta a ideia 5 para X", "combina a 2 com a 8".

Se o usuário pedir mais ideias, gerar mais 10 diferentes, sem repetir as anteriores.

### Etapa 4. Geração do PRD completo

Após a escolha, gerar o documento PRD com a seguinte estrutura:

```markdown
# [Nome do App]

## Visão geral
[Três linhas: o que o app faz, para quem é e como muda a rotina do aluno]

## Problema resolvido
[Descrição do problema real, com referência ao público e ao nicho do produto]

## Público-alvo e contexto de uso
[Puxado do perfil.md: quem são, que situação vivem, quando vão usar o app]

## User stories
- Como [perfil], eu quero [ação], para [benefício]
- (mínimo 5, máximo 10)

## Schema do banco (máximo 5 tabelas)

### Tabela `nome_da_tabela`
- `id` (uuid, pk)
- `campo` (tipo)
- `created_at` (timestamp)

(repetir para cada tabela)

## Telas (ordem de navegação)
1. **[Nome da tela]** — [descrição do que contém e o que o usuário faz]
2. ...

## Mapa de rotas
- `/` → [Componente] (pública)
- `/login` → Login (pública)
- `/dashboard` → Dashboard (protegida)
- `/[feature]` → [Componente] (protegida)
- `*` → NotFound (pública)

(preencher com todas as rotas reais do app, sem deixar nenhuma em branco)

## Regras de negócio
- [regra 1]
- [regra 2]

## Direção de design

### Tom visual
[escolher 1-2: minimalista / bold / corporativo / playful / premium / técnico / orgânico / editorial]

### Mood em 3 palavras
[ex: "sóbrio, confiável, moderno"]

### Referência visual
Pense em algo parecido com [app/site real: Linear, Notion, Stripe, Vercel, Arc, Cron, Raycast, Superhuman, Figma, Mercury], mas com [ajuste pro nicho].

### Paleta de cores (tokens semânticos — preencher em hex concreto, nunca "a definir")
- `--primary`: #XXXXXX (ação principal, CTAs)
- `--primary-hover`: #XXXXXX (10% mais escuro que o primary)
- `--secondary`: #XXXXXX (ação secundária)
- `--accent`: #XXXXXX (destaques pontuais)
- `--background`: #XXXXXX (fundo da página)
- `--surface`: #XXXXXX (cards, modais — 1 tom acima do background)
- `--border`: #XXXXXX (divisórias, bordas sutis)
- `--text-primary`: #XXXXXX (textos principais)
- `--text-secondary`: #XXXXXX (textos secundários, labels)
- `--text-muted`: #XXXXXX (placeholders, disabled)
- `--success`: #22C55E
- `--warning`: #F59E0B
- `--error`: #EF4444

Contraste obrigatório: texto primário sobre background com pelo menos 4.5:1 (WCAG AA). Validar antes de registrar.

### Tipografia (APENAS sans-serif — qualquer fonte serifada é proibida)

Fontes aprovadas:
- Padrão neutro profissional: Inter, Geist, DM Sans
- Modernas/tech: Space Grotesk, Satoshi, Plus Jakarta Sans, Manrope
- Display/Impacto: Bricolage Grotesque, Cabinet Grotesk, General Sans
- Monoespaçadas (para código/dados): JetBrains Mono, Geist Mono, IBM Plex Mono
- Humanistas amigáveis: Nunito, Outfit, Urbanist

- Títulos: [fonte escolhida da lista acima]
- Corpo: [fonte escolhida da lista acima — pode ser a mesma dos títulos]
- Mono (se houver dados/código): [fonte mono da lista acima]

Pesos permitidos: 400, 500, 600, 700. Nunca usar 800 ou 900.
Máximo de 2 famílias tipográficas no mesmo app.

### Verificação anti-serifa (obrigatória antes de avançar para a Etapa 5)
- A fonte de títulos está na lista aprovada acima? Sim / Não
- A fonte de corpo está na lista aprovada acima? Sim / Não
- O texto desta seção contém alguma das palavras proibidas: "Serif", "Slab", "Playfair", "Merriweather", "Lora", "Garamond", "Georgia", "Cormorant", "Roboto Slab", "Baskerville", "Crimson", "Tinos"? Se sim, substituir antes de continuar.

### Escala tipográfica (usar só estes tamanhos)
- text-xs: 12px / line-height 16px (labels, captions)
- text-sm: 14px / line-height 20px (texto secundário)
- text-base: 16px / line-height 24px (corpo padrão)
- text-lg: 18px / line-height 28px (subtítulos)
- text-xl: 20px / line-height 28px (títulos de card)
- text-2xl: 24px / line-height 32px (títulos de seção)
- text-3xl: 30px / line-height 36px (título de página)
- text-4xl: 36px / line-height 40px (hero)

### Sistema de espaçamento (grid de 4px)
Usar apenas múltiplos de 4: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96.
Entre seções: 64-96px. Entre cards: 16-24px. Padding interno de card: 24px. Padding de botão: 12px vertical / 24px horizontal.

### Border radius (tokens)
- rounded-sm: 4px (tags, badges)
- rounded-md: 8px (inputs, botões)
- rounded-lg: 12px (cards)
- rounded-xl: 16px (modais, containers grandes)
- rounded-full: avatares, pills

### Shadows
- shadow-sm: cards em listas (0 1px 2px rgba(0,0,0,0.05))
- shadow-md: dropdowns, tooltips
- shadow-lg: modais, dialogs
- Nunca empilhar sombras. Nunca usar sombra decorativa.

### Componentes padrão
- Botões: 3 variantes apenas — primary, secondary, ghost. Altura 40px padrão, 32px small, 48px large. Estado loading com spinner. Estado disabled com opacidade 0.5.
- Inputs: label acima, placeholder dentro, mensagem de erro abaixo em vermelho. Border 1px. Focus ring 2px no primary. Altura 40px.
- Cards: padding 24px, border-radius consistente, border 1px OU shadow-sm (um ou outro, nunca os dois juntos).
- Modais: max-width 500px para confirmações, 700px para formulários. Backdrop escurecido. Fechar com ESC e clique fora.
- Toasts: canto superior direito, 3 variantes (success verde, error vermelho, info neutro). Auto-dismiss em 4s. Máximo 3 simultâneos.
- Ícones: usar APENAS Lucide React (`lucide-react`). Tamanho padrão 16px ou 20px. Nunca misturar bibliotecas de ícone.

### Estados obrigatórios em todo componente interativo
- Default, Hover, Active, Focus, Disabled, Loading.
- Focus visível com ring (acessibilidade).
- Transições suaves (150-200ms ease).

### Telas com estados (sempre implementar os 4)
- Loading: skeleton ou spinner centralizado, nunca texto "carregando..."
- Empty: ícone + título + descrição + CTA para a primeira ação
- Error: mensagem clara + botão para tentar de novo
- Success: toast ou feedback inline + redirecionamento quando aplicável

### Acessibilidade (mínimos)
- Contraste AA em todos os textos (4.5:1 para texto normal, 3:1 para texto grande 18px+)
- Touch targets de pelo menos 44x44px em mobile
- Todo input tem label (não substituir label por placeholder)
- Focus ring visível sempre
- Semântica HTML correta (h1 único por página, button para ações, a para links externos)
- Não usar cor como único indicador de informação

### Hierarquia visual
- Uma única ação primária por tela (botão primary). O resto é secondary ou ghost.
- Hierarquia tipográfica clara: título, subtítulo, corpo, label — diferença de pelo menos 1 nível na escala entre eles.

### Responsividade
- Mobile-first: design pensado primeiro em 375px de largura.
- Breakpoints: sm 640px, md 768px, lg 1024px, xl 1280px.
- Container max-width 1280px com padding 24px desktop / 16px mobile.
- Nenhuma tela pode quebrar em mobile.
- Navegação em mobile: bottom tab bar (3-5 seções) ou menu hamburguer.
- Tabelas em mobile: converter em cards ou lista, nunca scroll horizontal.

### Dark mode
- Nichos que pedem dark mode padrão: dev, produtividade, finanças, gaming.
- Nichos que ficam melhor em light mode: saúde, educação infantil, bem-estar, moda.
- Definir tokens de cor para o modo escolhido.

### O que não fazer
- Nenhuma fonte serifada (regra absoluta)
- Nenhum gradiente decorativo sem propósito
- Nenhuma sombra colorida ou neon
- Nenhuma animação chamativa (bounce, flip, shake) — só transições sutis (fade, slide curto)
- Nenhum emoji no lugar de ícone em UI profissional
- Mais de 2 famílias tipográficas no mesmo app
- Mais de 5 cores semânticas base (fora tons neutros)
- Texto centralizado em blocos longos (só em headers curtos, estados vazios e CTAs)
- Border com cor saturada sem motivo (bordas são neutras por padrão)
- Múltiplas CTAs competindo na mesma tela

## Prompt para o Lovable.dev

[prompt técnico completo — ver Etapa 5]
```

### Etapa 5. Prompt pronto para o Lovable.dev

O prompt deve seguir esta estrutura e ordem:

**Bloco 1. Abertura e stack**

Começar com: "Crie um aplicativo web chamado [nome] com as seguintes características:"

Especificar stack: React + Tailwind + Supabase.

**Bloco 2. Autenticação (incluir sempre este texto literal)**

> "IMPORTANTE sobre autenticação: use Supabase Auth com `signInWithPassword` e `signUp` SEM verificação de email. No painel do Supabase, desative 'Confirm email' em Authentication > Providers > Email. O usuário deve conseguir cadastrar e logar imediatamente, sem nenhum email intermediário. Não implemente magic link. Não implemente 'esqueci minha senha' por email na v1 — use reset manual depois, se necessário.
>
> IMPORTANTE sobre senha: o aluno escolhe a senha que quiser, sem restrição de complexidade. Não valide força de senha, não exija maiúscula, número ou caractere especial, não mostre 'medidor de força'. No painel do Supabase, vá em Authentication > Providers > Email e defina 'Minimum password length' como 1. No frontend, remova qualquer validação de senha além de 'campo obrigatório'. Se o aluno quiser usar '123', ele pode."

**Bloco 3. Configuração de rotas (incluir sempre este texto literal)**

> "Configuração de rotas (obrigatório para evitar 404):
> 1. Usar `react-router-dom` e configurar TODAS as rotas explicitamente em `App.tsx` ou arquivo de router dedicado.
> 2. A rota `/` DEVE ter um componente renderizado (landing ou dashboard, nunca vazio).
> 3. Adicionar rota catch-all no final: `<Route path='*' element={<NotFound />} />` com um componente NotFound.tsx amigável que tem link para home.
> 4. Para navegação interna, usar SEMPRE `<Link to='...'>` do `react-router-dom`. NUNCA usar `<a href='...'>` para rotas internas.
> 5. Botões que navegam devem usar o hook `useNavigate()`, nunca `window.location`.
> 6. Para rotas protegidas (após login), criar um componente `<ProtectedRoute>` que redireciona para `/login` se não autenticado, em vez de dar 404.
> 7. Rotas do app: [listar aqui todas as rotas do Mapa de rotas preenchido no PRD, com path, componente e tipo pública/protegida]"

**Bloco 4. Segurança (incluir sempre este texto literal)**

> "Regras de segurança obrigatórias:
>
> 1. Nenhuma chave secreta, token de API de terceiros ou credencial pode aparecer no código do frontend. Tudo que exige autenticação com serviço externo vai em Supabase Edge Functions, nunca em componente React.
>
> 2. Ativar Row Level Security (RLS) em TODAS as tabelas do Supabase. Nenhuma tabela pode ficar com RLS desativado em produção. Cada tabela deve ter políticas explícitas definindo quem pode SELECT, INSERT, UPDATE e DELETE — por padrão, negar tudo e liberar apenas o necessário.
>
> 3. O frontend nunca faz requisição direta a APIs de terceiros que retornam dados sensíveis (dados de alunos, dados de pagamento, dados pessoais). Essas chamadas ficam em Edge Functions no Supabase, que o frontend chama via `supabase.functions.invoke()`.
>
> 4. Nunca expor o `service_role` key do Supabase no frontend. Usar apenas a `anon` key pública. Operações que precisam de privilégio elevado ficam em Edge Functions com a `service_role` key no ambiente seguro do servidor.
>
> 5. Dados de um usuário nunca podem ser acessados por outro usuário. As políticas de RLS devem usar `auth.uid()` para garantir isolamento. Exemplo de política correta: `USING (user_id = auth.uid())`.
>
> 6. Inputs do usuário nunca são concatenados diretamente em queries. Usar sempre queries parametrizadas do Supabase client (`.eq()`, `.filter()`, `.match()` etc.) — nunca interpolação de string em SQL.
>
> 7. Não armazenar senhas, tokens ou dados sensíveis em `localStorage` ou `sessionStorage`. Usar apenas os cookies httpOnly gerenciados pelo Supabase Auth."

**Bloco 6. Direção de design (incluir antes das telas)**

> "Siga esta direção de design desde a primeira tela. Configure os tokens de cor e tipografia no `tailwind.config.ts`. Importe as fontes via Google Fonts no `index.html`. Proibido usar fontes serifadas. Use apenas [fonte de títulos] para títulos e [fonte de corpo] para corpo. Paleta: primary [hex], background [hex], surface [hex], text-primary [hex] — conforme tokens definidos abaixo. Referência visual: [app de referência definido no PRD]. Use Lucide React para todos os ícones (nenhuma outra biblioteca de ícones). Implemente estados de loading (skeleton), empty (ícone + CTA), error (mensagem + retry) e success (toast) em todas as telas que carregam dados."

**Bloco 7. Telas**

Descrever cada tela na ordem de navegação, com o que contém e as ações principais.

**Bloco 8. Schema do banco**

Descrever o schema de forma que o Lovable entenda e crie as tabelas no Supabase.

**Bloco 9. Regras de negócio**

Listar as regras de negócio definidas no PRD.

**Bloco 10. Padrões de UX**

> "Padrões de UX obrigatórios: menu lateral em desktop, bottom tab bar em mobile, tabelas com paginação (máximo 20 itens por página), formulários com validação inline após blur, mensagens de erro específicas (nunca 'campo inválido'), botão de submit full-width em mobile, interface 100% em português do Brasil, sem emojis na UI (usar apenas ícones Lucide)."

**Bloco 11. Imagens (incluir sempre este texto literal)**

> "Imagens do app: o Lovable pode gerar imagens para ilustrar o app. Use esse recurso para as seguintes situações, quando fizerem sentido para o app:
>
> - Ilustração na tela de estado vazio (empty state): uma imagem temática que represente o nicho ou a ação esperada, em estilo flat ou minimalista, combinando com a paleta de cores do app.
> - Imagem de capa ou banner na tela de boas-vindas ou dashboard, se houver, representando o tema do app (ex: para um tracker de leitura de tarô, uma imagem abstrata de cartas; para um planner de estudos, uma imagem de organização).
> - Avatar ou ícone padrão para perfis de usuário quando não há foto cadastrada.
> - Ilustrações de onboarding se o app tiver um fluxo de primeiro acesso com mais de 1 passo.
>
> Regras para as imagens geradas:
> 1. Estilo consistente com o tom visual definido no design system (minimalista, flat, clean — sem realismo fotográfico a não ser que o tom peça).
> 2. Paleta alinhada com as cores do app (não gerar imagem com cores que colidam com a identidade visual).
> 3. Sem texto dentro das imagens (texto vai no código, não na imagem).
> 4. Sem rostos humanos realistas em imagens geradas por IA (evita problema de uncanny valley).
> 5. Tamanho e proporção adequados ao espaço onde a imagem vai aparecer (ex: banner 16:9, avatar 1:1, ilustração de empty state com proporção livre mas sem ser muito alta).
> 6. Não gerar imagem onde um ícone Lucide já resolve (ex: não gerar imagem de lupa para campo de busca)."

**Bloco 12. Fechamento (incluir sempre este texto literal)**

> "Ao finalizar, mostre o preview e me diga quais passos ainda faltam para eu começar a usar."

### Etapa 6. Aprovação e entrega

Mostrar o PRD completo com o prompt e pedir:

```
1. Aprovar e salvar
2. Quero ajustar algo
```

Após aprovação:

- Salvar em `meus-produtos/{slug}/entregas/apps/{slug-do-epic}.md`.
- Informar o caminho do arquivo.
- Mostrar os próximos passos:

```
Pronto. PRD salvo.

Arquivo: meus-produtos/{slug}/entregas/apps/{slug-do-epic}.md

Próximos passos:
1. Acesse lovable.dev e faça login
2. Clique em "New Project"
3. Cole o conteúdo da seção "Prompt para o Lovable.dev"
4. Aguarde a geração (normalmente menos de 2 minutos)
5. No painel do Supabase do projeto criado, vá em Authentication > Providers > Email e desative "Confirm email"
6. Ajuste o que precisar pedindo em linguagem natural dentro do Lovable
7. Quando publicar, volte aqui para conectar com /pagina-vercel se quiser domínio próprio
```

## Regras

- Nunca pular a Etapa 2 (ideias). O usuário sempre escolhe, nunca recebe um PRD sem ter escolhido.
- Schema simples. Máximo 5 tabelas. Se a ideia exigir mais, simplificar o escopo.
- Nunca entregar código. Código é responsabilidade do Lovable. A skill entrega especificação + prompt.
- Prompt para o Lovable sempre em português, direto, sem markdown interno (usar listas numeradas e marcadores comuns).
- Todo PRD deve ter a seção "Mapa de rotas" preenchida com todos os paths reais antes de avançar para a Etapa 5.
- Nenhum PRD pode incluir verificação de email, confirmação por email, magic link ou qualquer fluxo que dependa de email enviado ao usuário. Login sempre direto: email + senha, validação instantânea.
- PROIBIDO sugerir fontes serifadas. Fontes bloqueadas: Playfair Display, Merriweather, Lora, EB Garamond, Georgia, Times, Cormorant, PT Serif, Source Serif, Libre Baskerville, Crimson, Tinos, Roboto Slab, e qualquer nome com "Serif" ou "Slab". Usar apenas fontes da lista aprovada na seção de tipografia do template.
- Ao gerar o PRD, sempre entregar: paleta completa em hex (nunca "a definir"), fonte escolhida da lista aprovada, referência visual real (app ou site existente). Nunca deixar campo de design em aberto.
- Executar a verificação anti-serifa (checklist inline no template) antes de passar para a Etapa 5. Se encontrar qualquer nome proibido, substituir antes de continuar.
- Identidade visual sempre inferida do `perfil.md` (nicho, público, tom). Se o perfil não tiver paleta definida, propor paleta adequada ao nicho.
- Se o problema puder ser resolvido com uma planilha ou com `/criar-gpt`, dizer ao aluno antes de gerar o PRD completo.
- Não usar travessão em nenhum texto exibido.
- Não usar ponto de exclamação.
- Acentuação em português do Brasil correta em todo o texto.
