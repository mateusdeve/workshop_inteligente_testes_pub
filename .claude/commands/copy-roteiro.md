---
name: workshop-marketing:roteiro-de-video
description: Criar roteiros de vídeo — VVV, Reels, YouTube, Avatar HeyGen, Cenas Reais com stock footage, Motion/Remotion e Híbrido. Inclui 3 caminhos de execução (API automática, gravação própria, direção criativa para editor).
---

# Roteiro de Vídeo — VVV e Todos os Formatos

Cria roteiros e briefings de vídeo para todos os formatos usados no marketing digital, seguindo a estrutura VVV e Light Copy do VTSD.

## Usage

```
/copy-roteiro
```

## O Que Fazer

### 1. Contexto

Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md` se existir.

Extraia internamente (sem mostrar ao usuário):
- Quadro, Furadeira, Urgências Ocultas
- Tom e linguagem do público (idconsumidor)
- Estética visual e paleta do produto (se disponível no perfil)

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/4 — Formato:**

```
Qual formato de vídeo?

1. VVV completo (vídeo de vendas, 12-20 min)
2. Reels 60 segundos (Instagram/TikTok)
3. YouTube (conteúdo longo educativo)
4. Avatar IA (script para HeyGen)
5. Cenas Reais (script + shot list para filmagem própria ou stock footage)
6. Motion / Animação (brief para Remotion, CapCut ou Canva animado)
7. Híbrido (avatar + b-roll intercalado)

Digite o número:
```

```
--- Bloco 1/4 concluído ---
Formato: [formato escolhido]
Próximo: Execução
---
```

**Bloco 2/4 — Caminho de Execução:**

```
Como vai executar o vídeo?

1. Gerar automaticamente via API (HeyGen configurado no .env)
2. Só o roteiro — vou gravar ou editar eu mesmo
3. Direção criativa completa — preciso de briefing para um editor

Digite o número:
```

Regras de exibição por combinação:
- Opção 1 só faz sentido para formatos 4 (Avatar) e 7 (Híbrido). Se o usuário escolher opção 1 com formato que não suporta API, informar: "A geração via API está disponível apenas para Avatar IA e Híbrido. Para este formato, usaremos o caminho 2 ou 3."
- Opção 3 (Direção Criativa) ativa a geração de briefing completo (roteiro + paleta + ritmo de corte + referências de música + referências visuais)

```
--- Bloco 2/4 concluído ---
Formato: [formato]
Execução: [caminho]
Próximo: Objetivo
---
```

**Bloco 3/4 — Objetivo:**

```
Qual o objetivo do vídeo?

1. Vender produto
2. Educar e gerar valor
3. Captar leads
4. Engajar audiência

Digite o número:
```

```
--- Bloco 3/4 concluído ---
Formato: [formato]
Execução: [caminho]
Objetivo: [objetivo]
Próximo: Plataforma / detalhes do formato
---
```

**Bloco 4/4 — Plataforma + perguntas condicionais por formato:**

```
Onde será publicado?

1. Instagram (Reels/Stories)
2. TikTok
3. YouTube
4. Página de vendas
5. Anúncio pago (Meta Ads)

Digite o número:
```

**Perguntas adicionais condicionais (fazer UMA por vez, somente para os formatos abaixo):**

Se formato 5 (Cenas Reais):
```
Você tem filmagem própria ou vai usar stock footage?

1. Vou filmar eu mesmo
2. Vou usar stock footage (Pexels, Pixabay, Coverr)
3. Combinação de filmagem própria + stock

Digite o número:
```

Se formato 6 (Motion):
```
Qual ferramenta vai usar para animar?

1. Remotion (React/código)
2. CapCut
3. Canva animado
4. Adobe Express
5. Outra (descreva)

Digite o número:
```

Se formato 7 (Híbrido):
```
Qual proporção de avatar vs. b-roll no vídeo?

1. Predominantemente avatar (70% avatar / 30% b-roll)
2. Equilibrado (50% avatar / 50% b-roll)
3. Predominantemente b-roll (30% avatar / 70% b-roll)

Digite o número:
```

**Confirmação antes de gerar:**

```
Resumo do que vou criar:
- Formato: [formato]
- Execução: [caminho]
- Objetivo: [objetivo]
- Plataforma: [onde será publicado]
[detalhes condicionais do formato, se aplicável]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

---

### 3. Geração

#### VVV Completo (estrutura VTSD — 8 blocos)

1. Abertura — Gancho que prende (sem pergunta, premissa forte)
2. Conexão — História que gera identificação
3. Problema — Dor amplificada com Urgências Ocultas
4. Paliativo — Contraste entre as ferramentas, produtos e soluções concorrentes do mercado (Pinterest, perfis do nicho, cursos genéricos, apps, planilhas) e o método do produto: por que cada uma dessas soluções resolve parcialmente, mas não entrega o resultado completo. Paliativo é o CONCORRENTE, não é "o que a pessoa tentou e falhou"
5. Solução — Apresentação da Furadeira
6. Prova — Resultados e depoimentos
7. Oferta — Entregáveis, bônus, garantia, preço
8. CTA — Chamada direta

---

#### Reels 60s (2 formatos VTSD)

**Formato Revelação-Quebra-Solução:**
- 0-5s: Gancho (afirmação contra-intuitiva ou revelação não óbvia — nunca pergunta)
- 5-30s: Desenvolvimento (aprofunda o argumento ou ensina algo concreto)
- 30-55s: Quebra de objeção ou reforço da ideia central
- 55-60s: CTA

**Formato Problema-Solução:**
- 0-5s: Gancho com problema (afirmação que nomeia o problema de forma inesperada)
- 5-20s: Amplifica dor com especificidade
- 20-50s: Solução prática com entrega real
- 50-60s: CTA

---

#### Avatar IA (HeyGen)

- Script de até 90 segundos
- Linguagem natural e pausada, frases máx 15 palavras
- Indicações de expressão entre colchetes: [sorriso], [pausa], [ênfase]
- Sem pontuação que confunda a síntese de voz (nada de travessão, reticências múltiplas)
- Adaptado para leitura de teleprompter

---

#### Cenas Reais (stock footage ou filmagem própria)

Consultar skill `video-avancado` para referências completas de shot list e busca de stock.

Entrega obrigatória:
1. **Script narrado** — texto falado, dividido por cena, com tempo estimado por bloco
2. **Shot list** com timecodes — tabela com: nº da cena / plano / ângulo / ação / duração / mood / audio
3. **Palavras-chave para stock footage** — por cena, em inglês, prontas para buscar no Pexels/Pixabay/Coverr

Exemplo de shot list:

| # | Plano | Ângulo | Ação | Duração | Mood | Keywords stock |
|---|---|---|---|---|---|---|
| 1 | Close | Frontal | Pessoa olhando pro celular com expressão de frustração | 3s | tenso, íntimo | "person frustrated phone", "woman stressed mobile" |
| 2 | Médio | Lateral | Mãos digitando no computador, ambiente organizado | 5s | produtivo, calmo | "hands typing laptop", "work from home focused" |

Se filmagem própria: indicar também equipamento mínimo (celular estabilizado) e dicas de luz natural.

---

#### Motion / Animação

Consultar skill `video-avancado` para referências completas de animation brief.

Entrega obrigatória:
1. **Script de narração** — texto falado / narrado
2. **Animation brief** — tabela com: nº do componente / entrada / tempo de tela / saída / conteúdo / dados a mostrar
3. **Especificações por ferramenta** escolhida:
   - Remotion: props necessários, duração em frames (30fps), paleta HEX
   - CapCut / Canva animado: template de estilo sugerido, instrução de sequência de telas
4. **Paleta e tipografia** alinhadas ao produto

Exemplo de animation brief:

| # | Componente | Entrada | Duração | Saída | Conteúdo |
|---|---|---|---|---|---|
| 1 | Título hero | Fade in | 2s (60f) | Slide left | "O método que [Quadro]" |
| 2 | Dado de impacto | Scale up | 3s (90f) | Fade out | "10.000 alunos em 12 meses" |
| 3 | CTA final | Slide bottom | 5s (150f) | Permanece | "Garanta sua vaga" + botão |

---

#### Híbrido (Avatar + B-roll)

Consultar skill `video-avancado` para referências de proporção e coerência visual.

Entrega obrigatória:
1. **Script segmentado** — indicando claramente cada trecho:
   - `[AVATAR]` — falas gravadas pelo avatar
   - `[B-ROLL]` — descrição visual do que aparece em cima da narração
   - `[RETORNO AVATAR]` — quando o avatar volta em tela
2. **Shot list do b-roll** — mesma estrutura de Cenas Reais
3. **Notas de edição** — ritmo de corte, transições, quando usar texto na tela

Exemplo de estrutura segmentada:

```
[AVATAR 0-5s]
"A pessoa que mais trava raramente é a que sabe menos."

[B-ROLL 5-12s]
Cena: pessoa estudando com vários livros abertos, expressão sobrecarregada
Keywords: "overwhelmed student books", "too much information study"

[AVATAR 12-20s]
"Ela trava porque aprendeu na ordem errada. E eu vou te mostrar como reverter isso em 3 passos."

[B-ROLL 20-28s]
Cena: lousa ou tela com 3 passos aparecendo sequencialmente
Keywords: "whiteboard 3 steps process", "chalkboard writing steps"

[RETORNO AVATAR 28-35s]
"Passo 1..."
```

---

### 4. Regras de Estilo Light Copy (aplicar em TODOS os roteiros)

- Sem ponto de exclamação
- Sem perguntas no gancho: sempre afirmação contra-intuitiva ou premissa não óbvia
- Sem "mesmo que" ou "sem precisar" como muletas
- Sem promessas vagas: usar números concretos, situações reais
- Travessão longo (—): nunca usar. Substituir por vírgula, ponto ou pausa [pausa]
- Estrutura "Não é X. É Y.": nunca usar. Reformular de forma mais elaborada
- Emojis: nunca usar no roteiro
- O produto não aparece nos primeiros blocos: começar pelo problema ou pelo insight
- Nomear cria realidade: criar nome próprio para o conceito ensinado quando possível

**Checklist obrigatório antes de entregar:**

- [ ] Nenhum travessão no texto
- [ ] Nenhuma pergunta no gancho
- [ ] Nenhuma estrutura "Não é X. É Y."
- [ ] Nenhuma frase genérica de vendedor
- [ ] Produto não mencionado nos primeiros blocos
- [ ] Nenhum emoji

---

### 5. Saída por Caminho de Execução

**Caminho 1 — API automática (Avatar / Híbrido):**
- Roteiro formatado para HeyGen (texto corrido, sem marcações de cena)
- Chamada automática à API (ver Passo 6)

**Caminho 2 — Gravação / edição própria:**
- Roteiro limpo com timecodes e notas de edição entre colchetes
- Shot list (se Cenas Reais ou Híbrido)
- Palavras-chave de stock (se aplicável)

**Caminho 3 — Direção criativa para editor:**
- Roteiro completo com timecodes
- Shot list detalhada
- Paleta de cores HEX do produto
- Sugestão de música por mood (ex: "trilha motivacional sem letra, 120 BPM, referência: Epidemic Sound 'Build Up'")
- Referências visuais por cena (descrição de estética)
- Ritmo de corte sugerido (ex: "corte a cada 3-5s no desenvolvimento, a cada 1-2s no gancho")
- Instrução de montagem (ordem das cenas, transições, texto na tela)

---

### 6. Salvar Roteiro

### 4. Salvar
`meus-produtos/{ativo}/entregas/textos-de-venda/roteiro-[formato]-[produto].md`

Se caminho 3 (direção criativa), salvar briefing separado:
`meus-produtos/{ativo}/entregas/textos-de-venda/briefing-video-[formato]-[produto].md`

---

### 7. Gerar Vídeo via API (somente Caminho 1)

Leia `.env` e verifique as três variáveis: `HEYGEN_API_KEY`, `HEYGEN_AVATAR_ID`, `HEYGEN_VOICE_ID`.

**Se todas existirem**, gere via HeyGen:

```bash
curl -X POST "https://api.heygen.com/v2/video/generate" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "video_inputs": [{
      "character": {
        "type": "avatar",
        "avatar_id": "HEYGEN_AVATAR_ID",
        "avatar_style": "normal"
      },
      "voice": {
        "type": "text",
        "input_text": "ROTEIRO_AQUI",
        "voice_id": "HEYGEN_VOICE_ID",
        "speed": 1.0
      },
      "background": {
        "type": "color",
        "value": "#f8f8f8"
      }
    }],
    "dimension": {"width": 1080, "height": 1920}
  }'
```

A API retorna `video_id`. Polling a cada 30s:

```bash
curl "https://api.heygen.com/v1/video_status.get?video_id=VIDEO_ID" \
  -H "X-Api-Key: $HEYGEN_API_KEY"
```

Quando `status: completed`, fazer download do `video_url` e salvar em:
`meus-produtos/{ativo}/entregas/textos-de-venda/video-[formato]-[produto].mp4`

**Se faltar alguma variável**, instruir como configurar:

---
Para gerar o vídeo automaticamente, configure o HeyGen em 4 passos:

Passo 1 — Chave da API:
1. Acesse heygen.com e faça login
2. Clique no perfil (canto superior direito) > API
3. Clique em "Create API Key", copie a chave

Passo 2 — ID do avatar:
1. No painel HeyGen, vá em Avatars
2. Escolha um avatar > copie o "Avatar ID"

Passo 3 — ID da voz:
1. Vá em Voices
2. Filtre por "Portuguese (Brazil)"
3. Ouça e copie o "Voice ID"

Passo 4 — Configurar no projeto:
1. Abra o arquivo `.env` na raiz do projeto
2. Adicione:
```
HEYGEN_API_KEY=sua_chave_aqui
HEYGEN_AVATAR_ID=id_do_avatar_aqui
HEYGEN_VOICE_ID=id_da_voz_aqui
```
3. Salve e rode `/roteiro-de-video` novamente.
---

---

### 8. Próximo Passo

Após entregar o roteiro:
- Para Reels: "Grave direto pelo celular seguindo o roteiro. Use `/conteudo-social` para criar o plano completo de conteúdo."
- Para Avatar: "Vídeo enviado para processamento no HeyGen. Use `/anuncio` para criar a copy dos anúncios que vão usar este vídeo."
- Para Cenas Reais / Híbrido: "Shot list salva. Pesquise as cenas no Pexels (pexels.com) com as palavras-chave do arquivo. Depois use `/criativo-de-imagem` para criar os criativos estáticos da campanha."
- Para Motion: "Brief salvo. Abra a ferramenta escolhida e siga as instruções do arquivo de animation brief."
