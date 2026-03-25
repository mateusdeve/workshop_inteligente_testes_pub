---
name: workshop-marketing:copy-pagina
description: Criar copy completa da página de vendas com as 16 seções da estrutura 8D expandida. Texto persuasivo pronto para virar página HTML.
---

# Copy da Página — Texto Completo de Vendas

Gera a copy completa que vai dentro da página de vendas. Todas as 16 seções, no estilo Light Copy. O texto sai pronto — depois é só usar `/pagina-de-vendas` para transformar em HTML.

## Usage

```
/copy-pagina
```

## Princípios de Comportamento

### Postura: Gere, não pergunte demais

Você já tem `perfil.md` e `persona.md` com Quadro, Furadeira, Decorados, Urgências Ocultas, Identidades, objeções e pesquisa de mercado. Use TUDO isso para gerar a copy. Pergunte apenas o que não está no perfil (promoção, bônus especiais, urgência).

### Light Copy (SEMPRE)

- Argumentativo, objetivo e lógico
- Conversacional — parece conversa, não venda
- Não óbvio — curiosidade a cada linha
- Sem ponto de exclamação
- Sem perguntas no gancho
- Sem "mesmo que" / "sem precisar" como muletas
- Sem promessas vagas

Use os 26 elementos literários quando apropriado (consulte skill vtsd-completo para lista completa).

## O Que Fazer

### 1. Contexto

Leia `produtos/{ativo}/perfil.md` e `produtos/{ativo}/idconsumidor.md`. Se não existirem, oriente a usar `/meu-produto` e `/persona` primeiro.

### 2. Entrevista rápida (máximo 2-3 perguntas)

Pergunte apenas o que NÃO está no perfil:

- Tem promoção, desconto ou condição especial ativa?
- Tem bônus específicos que quer incluir? (se não tiver, gere 3 com base no perfil)
- Tem depoimentos reais? (se não tiver, gere modelos para substituir depois)

Confirme antes de gerar:
- Produto, preço, formato (já no perfil)
- Extras informados pelo aluno
- Avise que vai gerar em 2 partes

### 3. Geração em 2 Partes

A copy completa tem 16 seções. Para garantir qualidade, SEMPRE gere em duas partes separadas.

#### PARTE 1 — Persuasão (Seções 1 a 8)

Gere as seções 1 a 8 completas e salve no arquivo. Cada seção narrativa deve ter parágrafos desenvolvidos com linguagem da persona, cenas do cotidiano e elementos literários.

**Seção 1 — Primeira Dobra (Hero)**

- Headline principal (premissa matadora baseada no Quadro)
- Subheadline (expansão da promessa)
- 3 bullet points (cada um = Urgência Oculta + Decorado)
- Indicação de vídeo de vendas

**Seção 2 — Problema (Dor Amplificada)**

- Descreva a dor em detalhes vívidos e específicos do nicho
- Use linguagem da persona (frases reais que ela diria)
- Apele ao cotidiano — cenas do dia a dia
- Mínimo 3 parágrafos

**Seção 3 — Agitação (Consequências)**

- O que acontece se NÃO resolver
- Custo da inação (financeiro, emocional, tempo perdido)
- Amplifique sem ser dramático — seja lógico
- Mínimo 3 parágrafos

**Seção 4 — Paliativo (O que já tentaram)**

- Soluções que o público já tentou (use os paliativos da persona)
- Por que cada uma falhou
- Mostre que o problema não é a pessoa, é a falta de método
- Mínimo 3 parágrafos

**Seção 5 — Solução (Apresentação do Método)**

- Apresente o produto como a resposta lógica
- Mostre a Furadeira: macroetapas + o que cada uma resolve
- Nome do método em destaque
- Mínimo 3 parágrafos

**Seção 6 — Para Quem É**

- Mínimo 5 perfis ideais com marcadores positivos
- O público se reconhece aqui

**Seção 7 — Para Quem NÃO É**

- Mínimo 5 perfis que não devem comprar
- Gera credibilidade e filtra objeções

**Seção 8 — Entregáveis (Módulos/Conteúdo)**

- Lista completa do que está incluso
- Cada item com nome + descrição de valor (não só o nome)
- Use metáforas de valor para tangibilizar

Ao terminar a Parte 1, salve no arquivo e diga ao aluno:
"Parte 1 pronta (seções 1 a 8). Gerando a Parte 2 agora..."

#### PARTE 2 — Conversão (Seções 9 a 16)

Continue no mesmo arquivo. Mesmo nível de detalhe da Parte 1.

**Seção 9 — Bônus**

- 3 bônus estratégicos (gere com base no perfil e persona se o aluno não tiver)
- Cada bônus com: nome, descrição completa e valor individual em R$
- Bônus devem resolver objeções ou complementar o produto

**Seção 10 — Stack de Valor (Ancoragem)**

- Liste tudo que está incluso com valor individual
- Some o valor total
- Mostre o preço real como fração do valor total

**Seção 11 — Prova Social**

- 3-6 depoimentos completos (nome, situação antes, resultado depois)
- Se não tiver reais, gere modelos e marque: "[Depoimento modelo — substituir por depoimento real]"

**Seção 12 — Garantia**

- Tipo de garantia (7, 15 ou 30 dias)
- Texto que elimina o risco
- Tom confiante, não defensivo

**Seção 13 — Oferta Final**

- Preço com ancoragem (valor riscado + preço real)
- Parcelamento detalhado
- CTA principal forte

**Seção 14 — FAQ**

- 5-8 perguntas frequentes baseadas nas objeções da persona
- Respostas curtas, diretas, que quebram a objeção

**Seção 15 — Último CTA**

- Reforço de urgência ou escassez (se houver)
- Frase de fechamento + botão final

**Seção 16 — Rodapé**

- Indicações de termos de uso e política de privacidade

### 4. Salvar

`produtos/{ativo}/entregas/copy-pagina/copy-[produto].md`

### 5. Próximo Passo

"Copy completa salva. Use `/pagina-de-vendas` para transformar essa copy em uma página HTML profissional."
