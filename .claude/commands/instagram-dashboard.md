---
name: workshop-marketing:instagram-dashboard
description: Criar dashboard HTML de metricas do Instagram (seguidores, engajamento, posts recentes) via Apify. Roda localmente na maquina do aluno, sem servidor, sem agendamento automatico. O aluno roda o script manualmente para atualizar.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
model: sonnet
---

# Dashboard Instagram. Metricas Diarias

Cria um dashboard HTML de metricas do Instagram usando o Apify para coletar dados publicos do perfil e posts recentes. O aluno roda o script Python manualmente para atualizar.

Siga a skill `instagram-dashboard` para todas as regras tecnicas.

---

## PASSO 0. Detectar Estado

Antes de qualquer pergunta, verifique em paralelo:

1. `.env` — existe `APIFY_API_TOKEN` com valor? existe `IG_USER` com valor?
2. `entregas/conta.md` — existe campo `Instagram:` com valor?
3. `entregas/instagram-dashboard/atualizar.py` — o arquivo existe?

### Cenario A. Dashboard ja configurado (atualizar.py existe)

Mostre o menu sem perguntas:

```
Dashboard do Instagram ja esta configurado.

Perfil monitorado: @{username do .env (IG_USER)}

O que quer fazer?

1. Abrir o dashboard agora
2. Atualizar os dados agora
3. Trocar o perfil monitorado
4. Recriar o script do zero
```

**Opcao 1 — Abrir:**
```bash
start entregas/instagram-dashboard/dashboard.html
```

**Opcao 2 — Atualizar:**
```bash
python3 entregas/instagram-dashboard/atualizar.py --abrir
```
Aguarde, leia o log, informe o resultado.

**Opcao 3 — Trocar perfil:**
Pergunte o novo @. Normalize (sem @, lowercase). Atualize AMBOS com Edit cirurgico:
- `.env`: linha `IG_USER=<novo_username>`
- `entregas/conta.md`: campo `Instagram:`

Execute para testar:
```bash
python3 entregas/instagram-dashboard/atualizar.py --abrir
```

**Opcao 4 — Recriar do zero:**
Siga o fluxo completo a partir do Cenario B.

---

### Cenario B. Primeira configuracao

#### 0.1 Username do Instagram

Prioridade de leitura: `.env` primeiro (`IG_USER`), depois `entregas/conta.md` (`Instagram:`).

Se encontrar em qualquer uma das duas fontes, confirme:

```
Encontrei o Instagram configurado: @{username}

E esse mesmo perfil que quer monitorar?

1. Sim, pode continuar
2. Nao, quero usar outro
```

Se nao encontrar em nenhuma, pergunte:

```
Qual o usuario do seu perfil no Instagram? (so o nome, sem o arroba)
(ex: meuperfil)
```

Normalize: sem @, lowercase. Salve em AMBOS com Edit cirurgico:
- `.env`: adicione ou atualize a linha `IG_USER=<username>`
- `entregas/conta.md`: campo `Instagram:`

#### 0.2 Token Apify

Se `APIFY_API_TOKEN` estiver no `.env`: use diretamente, nao pergunte.

Se nao estiver: execute a skill `configurar-apify` e retorne aqui apos concluir.

---

## PASSO 1. Confirmacao

```
Configuracao confirmada:

- Perfil Instagram: @{username}
- Token Apify: configurado
- Script: entregas/instagram-dashboard/atualizar.py
- Dashboard: entregas/instagram-dashboard/dashboard.html

Custo estimado no Apify: menos de US$ 0,50/mes no plano gratuito.

1. Tudo certo, criar o dashboard
2. Quero ajustar algo
```

---

## PASSO 2. Gerar o Script Python

Crie a pasta `entregas/instagram-dashboard/` se nao existir.

**CRITICO: As credenciais ficam no `.env`, nunca no script.**

Escreva (ou atualize) as duas variaveis no `.env` da raiz do projeto:
- `APIFY_API_TOKEN` — ja deve estar la (configurado pelo configurar-apify). Se nao estiver, execute a skill `configurar-apify`.
- `IG_USER` — username do aluno sem @. Adicione ou atualize com Edit cirurgico no `.env`.

Leia `entregas/instagram-dashboard/atualizar.py`. Se existir, nao e necessario substituir nada: o script ja le do `.env`.

Se nao existir, gere do zero seguindo RIGOROSAMENTE a skill `instagram-dashboard`:
- Ator: `apify~instagram-scraper` via sync `run-sync-get-dataset-items`
- Perfil: `resultsType: "details"`, timeout 60s
- Posts: `resultsType: "posts"`, timeout 300s, busca expandida ate 100 posts para substituir likes ocultos
- Todas as imagens em base64 via requests com User-Agent e Referer do Instagram
- Thumbnails e slides salvos como .jpg em `entregas/instagram-dashboard/imagens/`
- insights.json com thumbnailPath, carouselPaths e transcricao (Reels via apify~whisper-speech-to-text)
- Dashboard HTML com 6 secoes obrigatorias: cabecalho, visao geral (4 KPIs), desempenho por formato, top 3, linha do tempo (3 graficos), todos os posts
- Linha do tempo: 3 graficos separados (Curtidas, Visualizacoes-Reels, Engajamento%)
- Likes ocultos (likesCount=-1): exibir "--", usar 0 nos calculos

Salve em `entregas/instagram-dashboard/atualizar.py`.

---

## PASSO 3. Executar e Abrir

Execute o script imediatamente:

```bash
python3 entregas/instagram-dashboard/atualizar.py --abrir
```

Aguarde a conclusao (pode levar ate 10 minutos — faz busca expandida de ate 100 posts).

Leia o log para confirmar sucesso:

```bash
tail -10 entregas/instagram-dashboard/log.txt
```

**Erros comuns:**

| Erro no log | Causa | Solucao |
|---|---|---|
| `401` ou autenticacao | Token Apify invalido | Verificar token em console.apify.com |
| `Perfil vazio` ou erro | @ errado ou perfil privado | Confirmar username; perfis privados nao funcionam |
| Arquivo travado pelo navegador | Browser com dashboard aberto | Fechar a aba do dashboard e rodar novamente |

---

## PASSO 4. Entrega

```
Dashboard criado.

Arquivos:
- Dashboard: entregas/instagram-dashboard/dashboard.html
- Script:    entregas/instagram-dashboard/atualizar.py
- Log:       entregas/instagram-dashboard/log.txt

Para atualizar quando quiser:
python3 entregas/instagram-dashboard/atualizar.py --abrir

Perfil monitorado: @{username}

Proximos passos:
- /copy-social para criar conteudo baseado nos posts com mais engajamento
- /dados-instagram para analise profunda com insights de copy
- /copy-anuncio para transformar os dados em anuncios testados
```

---

## REGRAS

- Nunca sobrescrever `entregas/conta.md` inteiro. Usar Edit cirurgico so no campo `Instagram:`.
- O token Apify e o username ficam no `.env` (`APIFY_API_TOKEN` e `IG_USER`). Nunca hardcodar no script.
- Se o perfil for privado, informar e sugerir export manual via Metricool ou Instagram Insights.
- Nao usar travessao em nenhum texto exibido no dashboard.
- Nao mostrar o codigo do script no chat. Salvar silenciosamente e informar o caminho.
- Sem agendamento automatico: nao criar CronCreate nem schtasks. O aluno atualiza manualmente.
