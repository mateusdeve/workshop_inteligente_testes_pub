---
name: workshop-marketing:trafego-analise
description: Análise narrada de tráfego pago Meta Ads com terminologia VTSD (Mandala 18 tipos, Urgência Oculta, Quadro na Parede, Furadeira, Decorados, 3 Identidades, HOT/COLD/SUPERCOLD, Caixa Rápido, Pico vs Evergreen). Hub com 4 módulos × 6 análises (Campanhas, Criativos, Funil, Conta) + Modo Demo D1-D7 com dados fictícios para ensinar. Conecta cada métrica a um elemento do método e entrega análise pedagógica + acionável. Use quando o aluno pedir análise narrada do funil, score de saúde da conta, classificação tier S/A/B/C/D de criativos, mapa da Mandala VTSD, ou quando quiser ensinar tráfego pago com a lente do método.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Skill, AskUserQuestion
model: sonnet
---

# Trafego Análise. Análise VTSD de Meta Ads

Análise narrada de campanhas Meta Ads pela lente do método VTSD (Venda Todo Santo Dia, Leandro Ladeira). Diferente de `/trafego-otimizar` que entrega ações executáveis, esta skill entrega análise pedagógica que conecta cada métrica a um elemento do método (Urgência Oculta → Hook Rate, Quadro → Connect Rate, Furadeira → Play-Through, etc.).

A especificação técnica completa está em `.claude/skills/trafego-analise/SKILL.md`. Sub-skills (campanhas, criativos, funil, conta, demo) em `.claude/skills/trafego-analise/sub-skills/`.

---

## Passo 0. Contexto e validação

### 0.1 Produto ativo
Leia `meus-produtos/.ativo` e `perfil.md`.

### 0.2 Conexão Meta (gate duro, exceto Modo Demo)
Leia `META_AUTH_MODO` no `.env`.

- **Se o aluno escolher Modo Demo (módulo 5):** pular esta validação. Modo Demo usa dados fictícios, não precisa de conexão.
- **Se vazio ou ausente** (e o aluno quer dados reais): acione `/meta-conexao` antes de prosseguir. Não tente adivinhar nem cair em fallback. Esta verificação é o passo zero de toda skill `/trafego-*`.
- **Se `MCP_CONECTOR`:** confirmar que pelo menos uma tool com prefixo `mcp__*__ads_*` está disponível. Se nenhuma estiver, pedir ao aluno para reabrir o Claude Code (MCP recém-adicionado às vezes precisa de reload). Se persistir, voltar a `/meta-conexao` para diagnosticar.
- **Se `APP`:** confirmar que `FB_ACCESS_TOKEN_PERMANENTE` e `FB_AD_ACCOUNT_ID` existem no `.env`. Se faltar algum, acionar `/meta-conexao`.

Em modo de dados reais, a skill nunca prossegue sem essa validação passar.

### 0.3 Selecao de conta de anuncio (multi-conta)

> Pular esta etapa em Modo Demo (modulo 5).

Apos a validacao da conexao, decidir qual conta analisar:

1. Ler `FB_AD_ACCOUNT_IDS` no `.env`. Lista de IDs separados por virgula.
2. Se `FB_AD_ACCOUNT_IDS` nao existe ou esta vazio, usar `FB_AD_ACCOUNT_ID` direto.
3. Se `FB_AD_ACCOUNT_IDS` tem **1 conta**, usar `FB_AD_ACCOUNT_ID` direto sem perguntar.
4. Se `FB_AD_ACCOUNT_IDS` tem **2 ou mais contas**, perguntar:

   ```
   Qual conta de anuncio voce quer analisar?

   1. {nome_conta_1} ({id_1})  ← padrao
   2. {nome_conta_2} ({id_2})
   3. {nome_conta_3} ({id_3})

   Digite o numero ou aperte Enter para usar a padrao:
   ```

   Para mostrar nomes amigaveis, fazer 1 chamada na Graph API:
   ```bash
   curl -s "https://graph.facebook.com/v25.0/me/adaccounts?fields=id,account_id,name&limit=100&access_token=TOKEN"
   ```
   Filtrar apenas as que estao em `FB_AD_ACCOUNT_IDS`. Marcar como "padrao" a que esta em `FB_AD_ACCOUNT_ID`.

5. Salvar a conta escolhida em variavel local da execucao (`AD_ACCOUNT_ID_ATUAL`). Nao sobrescrever o `.env`. Toda a analise (Campanhas, Criativos, Funil, Conta) atua dentro da conta escolhida.

### 0.4 Ler hub
Leia `.claude/skills/trafego-analise/SKILL.md`.

---

## Passo 1. Apresentar menu

Mostrar o menu da skill exatamente como definido:

```
╔══════════════════════════════════════════════╗
║  TRÁFEGO ANÁLISE. Análise VTSD de Meta Ads   ║
╚══════════════════════════════════════════════╝

O que você quer analisar?

[1] 📊 CAMPANHAS    6 análises (performance, escalabilidade, conjuntos
                    HOT/COLD/SUPERCOLD, orçamento Pareto, prospecção
                    × retargeting, dayparting)
[2] 🎨 CRIATIVOS    6 análises (tier S/A/B/C/D, Mandala VTSD 18 tipos,
                    DNA + galeria, fadiga, testes A/B, performance)
[3] 🔻 FUNIL        6 análises (mapa VTSD, gargalo, projeção, Caixa
                    Rápido, Pico × Evergreen, checkout)
[4] 🏥 CONTA        6 análises (Health Score 0-100, alertas Advantage+,
                    pausa hierárquica, plano executivo, testes A/B)
[5] 🎓 MODO DEMO    cenários D1-D7 com dados fictícios (para ensinar
                    sem expor conta real)

Ou descreva o que precisa.
```

---

## Passo 2. Roteamento

Conforme escolha do aluno, ler o arquivo da sub-skill e executar a análise específica:

| Escolha | Arquivo |
|---------|---------|
| [1] | `.claude/skills/trafego-analise/sub-skills/campanhas.md` |
| [2] | `.claude/skills/trafego-analise/sub-skills/criativos.md` |
| [3] | `.claude/skills/trafego-analise/sub-skills/funil.md` |
| [4] | `.claude/skills/trafego-analise/sub-skills/conta.md` |
| [5] | `.claude/skills/trafego-analise/sub-skills/demo.md` |

Cada sub-skill tem menu interno (ex: `[1.1]`, `[1.2]`...). Se o aluno descreveu em texto livre o que quer, mapear para a análise mais próxima.

---

## Passo 3. Fonte de dados

Antes de executar a análise (exceto Modo Demo), perguntar:

```
Vou analisar com qual fonte de dados?

1. Puxar via /trafego-insights (recomendado, mais completo)
2. Você cola CSV exportado do Gerenciador
3. Você cola dados diretamente no chat

Digite o número:
```

- **Opção 1:** invocar `/trafego-insights` com o `campaign_id` ou `escopo: conta_completa` que a sub-skill exige.
- **Opção 2:** pedir o CSV. Parsear localmente.
- **Opção 3:** pedir os dados em formato livre. Esclarecer o que está faltando.

Para **Modo Demo**, dados fictícios já estão em `sub-skills/demo.md`.

---

## Passo 4. Executar a análise

Aplicar as instruções da sub-skill selecionada. Cada análise tem:

- Inputs necessários (campanha, conjunto, anúncio ou conta inteira)
- Método de análise (cálculo de métricas + classificação VTSD)
- Template de output (com terminologia VTSD)
- Ação recomendada concreta

🔍 Próximo passo: gerar análise [nome da análise]. Tempo estimado: 1 a 2 minutos.

✅ Concluído: análise gerada.

---

## Passo 5. Apresentar com terminologia VTSD

Toda análise apresenta:

1. **Diagnóstico em linguagem VTSD.** Ex: "Hook Rate baixo em 18% indica Urgência Oculta fraca no início do criativo".
2. **Gargalo principal.** Sempre identificar UM gargalo principal antes de listar secundários.
3. **Ação recomendada concreta.** Nunca deixar análise sem ação.
4. **Conexão com método.** Para cada problema, indicar qual elemento VTSD revisar.

Exemplo de output narrado (módulo Conta):

```
🏥 SAÚDE DA CONTA. [Nome]
Período: [X] dias | Investimento: R$ [valor]
Score: [X]/100. [Classificação]

⚠️ ALERTAS PRIORITÁRIOS:
1. [Problema mais urgente] → [Ação imediata]
2. [Segundo problema] → [Ação]
3. [Terceiro problema] → [Ação]

✅ PONTOS FORTES:
- [O que está funcionando bem]

🔧 PRÓXIMOS PASSOS (VTSD):
1. [Ação prioritária com prazo]
2. [Segunda ação]
3. [Terceira ação]

💡 No VTSD, a saúde da conta reflete diretamente o equilíbrio entre
   as três identidades: Consumidor, Produto e Comunicador.
```

---

## Passo 6. Encaminhar para execução (se aluno quiser agir)

Esta skill **narra**, não executa edição em campanhas. Se a análise sugerir ações executáveis (pausar, mudar budget, escalar), encaminhar:

```
Para aplicar as ações recomendadas:

- Pausar criativos / reduzir orçamento / refresh: /trafego-otimizar
- Escalar campanhas validadas: /trafego-escalar
- Subir nova campanha (ex: nova trilha de público): /trafego-criar-campanha
- Criar criativos novos: /copy-anuncio + /criativo-estatico
- Atacar gargalo de página: /feedback-pagina ou /pagina-performance
- Atacar gargalo de checkout: /pagina-checkout
```

---

## Passo 7. Salvar análise (opcional)

Salvar em:
```
meus-produtos/{ativo}/entregas/trafego/analise-{modulo}-{slug}-{YYYY-MM-DD}.md
```

Conteúdo: análise completa narrada + ações recomendadas + próximos passos.

Caminho absoluto: `C:\Users\gabri\Documents\GitHub\workshop_inteligente\meus-produtos\{ativo}\entregas\trafego\analise-{...}.md`

---

## Modo Demo (uso especial)

O Modo Demo (sub-skill `demo.md`) usa dados fictícios para ensinar sem expor conta real. Útil para:
- Aulas e tutoriais.
- Aprender o método VTSD aplicado ao tráfego.
- Praticar leitura de métricas antes de operar conta real.

Os 7 cenários D1-D7 estão pré-prontos em `sub-skills/demo.md`. Sempre deixar claro que os dados são fictícios.

---

## Princípios que este command nunca viola

1. **Sempre usar terminologia VTSD.** Mandala, Urgência Oculta, Quadro, Furadeira, Decorados, Identidades, HOT/COLD/SUPERCOLD, Caixa Rápido, Pico vs Evergreen.
2. **Nunca inventar métricas.** Se faltar dado, pedir explicitamente.
3. **Sempre identificar gargalo principal** antes de listar secundários.
4. **Nunca deixar análise sem ação concreta.**
5. **Não executa edição.** Encaminha para `/trafego-otimizar`, `/trafego-escalar`, `/trafego-criar-campanha`.
6. **No Modo Demo, sempre declarar que dados são fictícios.**
7. **Para dados reais, sempre via `/trafego-insights`** (cache, métricas derivadas, atribuição declarada).
