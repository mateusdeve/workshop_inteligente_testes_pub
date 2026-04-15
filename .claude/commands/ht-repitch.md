---
name: workshop-marketing:ht-repitch
description: Revisar e ajustar um pitch de venda já existente (palco, call, WhatsApp) a partir dos resultados reais. Identifica pontos fracos de ancoragem, objeções mal quebradas, CTA frouxo e entrega versão nova do pitch com correções específicas.
---

# HT Repitch. Revisão de Pitch Existente

Pega um pitch que já rodou em um evento, call ou WhatsApp e gera uma versão corrigida com base no que deu errado. Foco em ancoragem, quebra de objeção, CTA e timing. Não cria do zero, refaz o que já existe.

## Usage

```
/ht-repitch
```

## O Que Fazer

Acione a skill `ht-repitch` do plugin `workshop-marketing` e siga o roteiro:

1. Ler `entregas/.ativo` e `entregas/{ativo}/perfil.md`.
2. Coletar (uma pergunta por vez):
   1. Qual pitch vamos revisar? (palco, call 1:1, WhatsApp, outro). Se já existe em `entregas/{ativo}/comercial/`, oferecer a lista.
   2. Pedir pro aluno colar o pitch original ou apontar o caminho do arquivo.
   3. Quais foram os resultados reais? (quantas pessoas, quantas venderam, principais objeções ouvidas, onde a plateia ou lead esfriou)
   4. O que o aluno sente que falhou? (ancoragem, preço, bônus, urgência, CTA, autoridade)
3. Ler o pitch original e fazer uma auditoria em 3 blocos:
   - **Diagnóstico**: 5 a 8 pontos específicos do que não funcionou, com trecho citado + razão. Usar como referência a estrutura do `/ht-pitch-palco` ou `/ht-fechamento`.
   - **Causas raiz**: agrupar os problemas em 2 ou 3 causas principais (ex: "ancoragem fraca", "objeção de preço não foi quebrada antes do preço", "CTA ambíguo").
   - **Ajustes propostos**: como cada bloco precisa ser reescrito, em linguagem concreta.
4. Mostrar o diagnóstico e pedir aprovação antes de reescrever.
5. Gerar a versão nova do pitch aplicando os ajustes. Manter a voz do aluno, só corrigir estrutura, ancoragem, quebra de objeção e CTA.
6. Mostrar a versão nova e pedir aprovação.
7. Salvar em `entregas/{ativo}/comercial/repitch-{data}.md` com 3 seções: diagnóstico, versão antiga (referência) e versão nova.
8. Sugerir próximo passo: rodar a versão nova e usar `/ht-objecoes` pra mapear as objeções residuais.

## Regras Resumidas

- Nunca reescrever sem o diagnóstico estar aprovado primeiro.
- Respeitar a voz do aluno. Não substituir palavras que fazem parte do estilo dele.
- Se o aluno não souber os resultados reais, perguntar o que sentiu no momento (expressões, pausas, perguntas da plateia).
- A versão nova precisa ser pelo menos 80% parecida com a antiga em tamanho. Não é um pitch novo.
- Não usar travessão em nenhum texto exibido.
