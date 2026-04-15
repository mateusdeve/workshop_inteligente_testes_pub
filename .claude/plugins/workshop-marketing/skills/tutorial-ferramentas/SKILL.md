---
name: tutorial-ferramentas
description: >
  Guia interativo de instalação e configuração das ferramentas do workshop.
  Claude Code, VS Code, Lovable.dev, HeyGen, Freepik e 2 contas Facebook.
  Roda um bloco por vez, checando o que o aluno já tem, e só mostra os
  passos que faltam. Ideal pra pré-evento ou primeiro contato.
---

# Tutorial de Ferramentas. Setup do Workshop

Leva o aluno pelo setup completo das ferramentas que ele vai usar no workshop, uma de cada vez. Começa perguntando o que ele já tem, só mostra o que falta, e acompanha até cada ferramenta estar funcionando. Serve como onboarding inicial ou checklist pré-evento.

## Quando Usar

- Antes do aluno começar a rodar qualquer outro comando pela primeira vez.
- Quando disser "como eu instalo isso", "nunca usei Claude Code", "o que preciso pra começar", "as ferramentas do workshop".
- Como checklist final antes do evento começar.

## O Que Fazer

### 1. Menu inicial

```
Qual ferramenta vamos configurar agora?

1. Claude Code (CLI principal do workshop)
2. VS Code (editor recomendado)
3. Lovable.dev (construir quizzes e SaaS)
4. HeyGen (avatares de vídeo)
5. Freepik (imagens e vídeos via IA)
6. Facebook (2 contas pra fallback)
7. Rodar checklist completo (passa por todas)

Digite o número:
```

Rode apenas o bloco escolhido, ou rode todos em sequência se for a opção 7.

### 2. Bloco Claude Code

Pergunte: "Você já tem o Claude Code instalado?"
- Se sim, pular pra "Como abrir o projeto do workshop".
- Se não, seguir:

**Passo 1. Verificar Node.js**
```
Abra o terminal (Mac: Cmd+Space e digite "Terminal"; Windows: tecla Windows e digite "cmd") e rode:

node --version

Me diga o que apareceu.
```

Se for menor que 18 ou der erro, mandar pra `https://nodejs.org` pra baixar a versão LTS. Se for 18+, seguir.

**Passo 2. Instalar o Claude Code**
```
No terminal, rode:

npm install -g @anthropic-ai/claude-code

Quando terminar, me diga "ok".
```

**Passo 3. Fazer login**
```
No terminal, rode:

claude

Vai abrir uma tela de login. Siga as instruções. Volta aqui quando estiver logado.
```

**Passo 4. Abrir o projeto do workshop**
```
Vá pra pasta do workshop no terminal:

cd "caminho/da/pasta/workshop_inteligente"

Depois rode:

claude

Pronto. Você está dentro do Claude Code com o projeto carregado.
```

### 3. Bloco VS Code

Pergunte: "Você já tem o VS Code instalado?"
- Se sim, pular pra extensões.
- Se não:

```
1. Acesse https://code.visualstudio.com
2. Baixe a versão pro seu sistema
3. Instale como qualquer programa normal
4. Abra o VS Code
5. Me diga "ok"
```

**Extensões recomendadas:**
```
Dentro do VS Code, aperte Ctrl+Shift+X (ou Cmd+Shift+X no Mac) e instale:

1. Portuguese (Brazil) - interface em português
2. Prettier - formatação de código
3. Live Server - abrir páginas HTML no navegador com um clique

Me diga "ok" quando tiver instalado.
```

**Abrir a pasta do workshop:**
```
No VS Code: File > Open Folder > escolha a pasta workshop_inteligente.
```

### 4. Bloco Lovable.dev

```
Vamos criar sua conta:

1. Acesse https://lovable.dev
2. Clique em "Sign up" (canto superior direito)
3. Faça login com Google ou email
4. Me diga "ok" quando estiver logado
```

Depois explicar:
- Diferença entre plano Free (5 mensagens/dia) e Pro
- Como criar um projeto novo: "New Project"
- Como colar um prompt técnico (os prompts vêm das skills `/lt-quiz`, `/app-saas`, etc)
- Como publicar o projeto (botão Publish no canto superior)

### 5. Bloco HeyGen

```
1. Acesse https://heygen.com
2. Clique em "Get Started" ou "Sign up"
3. Use email ou Google pra criar conta
4. Me diga "ok" quando estiver logado
```

Explicar:
- Plano gratuito dá 1 minuto de vídeo com marca
- Plano Creator (mínimo recomendado) remove marca e libera mais minutos
- Como criar um avatar a partir de foto ou vídeo seu
- Como gerar o primeiro vídeo: colar roteiro + escolher avatar + escolher voz
- A skill `/video-heygen` faz tudo isso automatizado quando o aluno estiver pronto

### 6. Bloco Freepik

```
1. Acesse https://freepik.com
2. Clique em "Sign up" (canto superior direito)
3. Use email ou Google
4. Me diga "ok" quando estiver logado
```

Explicar:
- Plano gratuito tem limite diário
- Plano Premium libera downloads ilimitados + Pikaso (gerador de imagem e vídeo IA)
- Como usar o Pikaso: menu > AI > Pikaso
- A skill `/imagem-prompt` gera prompts prontos pra colar no Pikaso e em outras 6 ferramentas gratuitas

### 7. Bloco Facebook (2 contas)

```
Por que 2 contas:
Se uma conta é bloqueada ou o Business Manager quebra, você tem um fallback pra não parar tráfego.

Primeira conta (a principal):
1. Use sua conta pessoal já existente
2. Crie um Business Manager em https://business.facebook.com
3. Verifique seu domínio
4. Crie uma conta de anúncios
5. Me diga "ok"

Segunda conta (backup):
1. Crie uma conta pessoal nova no Facebook com outro email
2. Peça pra um amigo ou familiar que confia te adicionar como admin do Business Manager dele, ou crie um Business Manager novo
3. Esse backup é só pra emergência, não precisa rodar tráfego nela
```

Importante avisar:
- Nunca usar conta fake ou comprada. Facebook bloqueia.
- A segunda conta tem que ser real, usada esporadicamente, pra não ser flagada.

### 8. Checklist completo (opção 7 do menu)

Rode todos os blocos em sequência. No final, mostre:
```
Tudo pronto pra começar o workshop.

Checklist:
[x] Claude Code instalado e logado
[x] VS Code instalado com extensões
[x] Lovable.dev conta criada
[x] HeyGen conta criada
[x] Freepik conta criada
[x] 2 contas Facebook configuradas

Salvei seu progresso em entregas/.tutorial-ferramentas.md
Se precisar retomar, rode /tutorial-ferramentas de novo.

Próximo passo:
- Rode /produto-novo pra criar seu primeiro produto no sistema
```

### 9. Salvar progresso

A cada bloco concluído, salve em `entregas/.tutorial-ferramentas.md`:
```
# Tutorial de Ferramentas - Progresso

[x] Claude Code - {data}
[x] VS Code - {data}
[ ] Lovable
[ ] HeyGen
[ ] Freepik
[ ] Facebook
```

## Regras

- Uma ferramenta por vez. Nunca despejar tudo junto.
- Antes de cada passo, perguntar se o aluno já fez aquilo. Só avançar depois de "ok" ou "pronto".
- Links oficiais obrigatórios. Nenhum link de afiliado, nenhum link encurtado.
- Se o aluno travar em um erro específico, pausar e resolver o erro antes de avançar. Exemplos comuns:
  - Node não instalado > mandar pro nodejs.org
  - npm permission error > orientar a usar `sudo` (Mac/Linux) ou rodar PowerShell como admin (Windows)
  - HeyGen travou no pagamento > oferecer usar o plano Free e voltar depois
- Nunca pedir senha de nenhuma conta. O aluno faz login sozinho.
- Se o aluno disser "já tenho tudo instalado, pula", ir direto pra validação rápida ("ótimo, só confirma que consegue abrir cada ferramenta") e fechar o checklist.
- Não usar travessão em nenhum texto exibido.
