---
name: workshop-marketing:ht-conteudo
description: Criar o roteiro de conteúdo dos blocos de ensino do evento C10X. o que ensinar, em que ordem e como conduzir cada bloco para preparar o terreno para o pitch.
---

# HT. Roteiro de Conteúdo do Evento

Cria o roteiro completo dos blocos de ensino do Retiro Online ou webinar, alinhando o conteúdo ensinado com a oferta que será feita ao final.

## Usage

```
/c10x-conteudo
```

## O Que Fazer

### 1. Contexto
Leia `meus-produtos/.ativo`, depois `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md`.
Se existir `meus-produtos/{ativo}/entregas/c10x/cronograma-*.md`, leia para alinhar com a agenda.

### 2. Entrevista (UMA pergunta por vez, com progresso visual)

**Bloco 1/3. Temas do Evento:**
```
Quais os temas/blocos de conteúdo do evento?
Liste em ordem de apresentação.
(ex: "1. Diagnóstico do negócio, 2. Posicionamento, 3. Captação, 4. Fechamento")
```

```
--- Bloco 1/3 concluído ---
Temas: [lista]
Próximo: Oferta final
---
```

**Bloco 2/3. Oferta Final:**
```
O que será vendido ao final do evento?
(ex: "Mentoria de 3 meses para escalar o negócio", "Consultoria de posicionamento")
```

```
--- Bloco 2/3 concluído ---
Temas: [lista]
Oferta: [produto]
Próximo: Nível do público
---
```

**Bloco 3/3. Nível do Público:**
```
Qual o nível de conhecimento do público que vai participar?

1. Iniciante (ainda não tem resultado nenhum)
2. Intermediário (tem algum resultado, quer crescer)
3. Avançado (já fatura, quer escalar)
4. Misto

Digite o número:
```

**Confirmação antes de gerar:**
```
Resumo do que vou criar:
- Temas: [lista]
- Oferta ao final: [produto]
- Nível do público: [nível]

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

### 3. Geração

Para cada bloco de conteúdo, gere:

---

**BLOCO [N]: [Tema]**

**Objetivo do bloco:**
O que o participante deve conseguir fazer ou entender ao final deste bloco. Deve ser algo tangível.

**Conexão com a oferta:**
Como este bloco planta uma semente para a oferta final.
(ex: "Ao mostrar que posicionamento errado custa dinheiro, o participante entende por que precisa de ajuda especializada")

**Estrutura do bloco (roteiro em 4 partes):**

1. **Abertura (5 min)**. Gancho ou pergunta que conecta com a dor do participante
2. **Conteúdo principal (40-50 min)**. O que ensinar, em que ordem, com quais exemplos
3. **Ativação (10 min)**. Exercício prático que o participante faz durante o evento
4. **Fechamento do bloco (5 min)**. Resumo + gancho para o próximo bloco

**Pontos de prova social a inserir:**
Momentos onde citar casos de alunos ou resultados reais reforça a credibilidade.

**Armadilha a evitar:**
O erro mais comum ao ensinar este tema que diminui a conversão.

---

**Regras para o roteiro de conteúdo do C10X:**

- O conteúdo deve ser suficiente para gerar transformação real (não pode ser teaser vazio)
- Cada bloco deve abrir uma "ferida" (problema) e entregar uma "bandagem" (solução parcial). o remédio completo vem com a oferta
- Não ensine tudo: entregue resultado real no evento, mas deixe claro que há mais a percorrer
- A última hora antes do pitch deve subir a energia: depoimentos, perguntas ao público, celebração de pequenas vitórias

**Script de transição para o pitch:**
Texto de ligação entre o último bloco de conteúdo e o momento de apresentar a oferta:

"Ao longo desses [X dias/horas], você [resumo do que aprendeu]. Agora quero te mostrar como ir muito além disso..."

### 4. Aprovação
```
1. Aprovar e salvar
2. Quero ajustar algo
```

### 5. Salvar
`meus-produtos/{ativo}/entregas/c10x/conteudo-[evento].md`

### 6. Próximo Passo
"Roteiro de conteúdo pronto. Próximo: `/ht-pitch-palco` para criar o script completo do momento de venda."
