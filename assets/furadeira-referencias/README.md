# Imagens de referência da Furadeira

Coloque aqui as imagens que servem de inspiração visual para o fluxo B (refinado) do comando `/gerar-furadeira`.

## Regras

- **Formatos aceitos:** `.png`, `.jpg`, `.jpeg`, `.webp`.
- **Quantidade:** mínimo 3, máximo 16 arquivos.
- **Tamanho:** cada arquivo abaixo de ~4 MB para não pesar o payload.
- **Conteúdo:** o que você quer que a Furadeira final se pareça (estilo de foto, paleta, composição, iconografia do método).

## Como são usadas

O script `scripts/gerar-furadeira-openrouter.py` lê todas as imagens desta pasta, converte cada uma para base64 e envia junto do prompt para o OpenRouter. O modelo usa as referências para manter consistência visual com o que você já tem.

Se você quiser testar apenas algumas referências, use `--max-refs 5` na chamada do script para limitar.

## O que não colocar aqui

- Fotos pessoais com direitos autorais de terceiros sem permissão.
- Imagens com texto legível (o modelo tende a copiar texto ruim).
- Logos de marcas registradas.
