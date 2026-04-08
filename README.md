# Workshop Inteligente. Assistente de Marketing IA

Assistente de marketing digital, copy e infoprodutos baseado nas metodologias VTSD, Light Copy, C10X e Low Ticket. Roda dentro do Claude Code com agentes, comandos e skills próprios.

## Por onde começar

- **`COMO-USAR.md`**. Guia rápido para o usuário final (instalação, primeiros passos, comandos).
- **`CLAUDE.md`**. Instruções e regras do assistente. Tudo que o Claude precisa saber para operar o projeto. Leitura obrigatória antes de mexer em qualquer skill ou comando.
- **`docs/ARQUITETURA.md`**. Visão técnica da arquitetura.
- **`docs/diagnostico-projeto.md`**. Diagnóstico e decisões de evolução.

## Estrutura de pastas

```
workshop_inteligente/
├── .claude/                    Agentes, comandos, plugins, skills e configs do assistente
│   ├── agents/                 Agentes orquestradores (estrategista-*, construtor-*, etc)
│   ├── commands/               Slash commands disponíveis (/copy-*, /ht-*, /lt-*, etc)
│   └── plugins/                Plugins do workshop (skills, referências)
├── docs/                       Documentação técnica e histórico
│   ├── ARQUITETURA.md
│   ├── diagnostico-projeto.md
│   ├── setup-heygen.md
│   ├── setup-imagens.md
│   ├── historico/              Registro cronológico de decisões e correções
│   └── legado/                 Arquivos antigos preservados para referência
├── entregas/                   Tudo que o assistente gera fica aqui
│   ├── .ativo                  Identificador do produto ativo
│   └── {produto}/              Uma pasta por produto cadastrado
│       ├── perfil.md           Quadro, Furadeira, Decorados, Urgências
│       ├── idconsumidor.md     Identidade do consumidor (opcional)
│       ├── paginas/            Páginas HTML (vendas, captura, obrigado)
│       ├── copy-pagina/        Copy markdown das páginas
│       ├── emails/             Sequências de email
│       ├── anuncios/           Pacotes de anúncios
│       ├── conteudo-social/    Posts, carrosséis, Reels
│       ├── criativos/          Prompts de imagem e referências visuais
│       ├── comercial/          Scripts de venda 1:1
│       ├── videos/             Vídeos HeyGen, Remotion e roteiros
│       ├── produto/            E-book, checklist, mini-curso entregue ao comprador
│       ├── low-ticket-v1/      (familia-viajante) versão 1 do funil low ticket
│       ├── low-ticket-v2/      (familia-viajante) versão 2 do funil low ticket
│       └── funil/              HTML de funil completo
├── server.js                   Servidor mínimo para preview local
├── package.json
├── vercel.json
└── .env.example                Modelo de variáveis (chaves de API opcionais)
```

## Comandos principais

Veja a lista completa em `COMO-USAR.md` e em `CLAUDE.md`. Resumo:

- **Produto.** `/produto-novo`, `/produto-editar`, `/produto-trocar`, `/produto-consumidor`, `/produto-excluir`
- **Copy.** `/copy-pagina`, `/copy-anuncio`, `/copy-emails`, `/copy-social`, `/copy-roteiro`
- **Low ticket.** `/lt-funil`, `/lt-pagina`, `/lt-quiz`, `/lt-criar-produto`, `/lt-otimizar`
- **High ticket.** `/ht-big-idea`, `/ht-oferta`, `/ht-pagina-inscricao`, `/ht-pitch-palco`, `/ht-fechamento`, `/ht-spin`...
- **Estratégia.** `/estrategia-funil`, `/estrategia-lancamento`
- **Vídeo.** `/video-heygen`, `/video-remotion`, `/video-editar`
- **Feedback.** `/feedback-pagina`, `/feedback-low-ticket`

## Regra absoluta de estilo

Nada de travessão (—) em nenhum texto gerado. Detalhes em `CLAUDE.md`.
