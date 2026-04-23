#!/usr/bin/env node
// PostToolUse hook: revisa copy em arquivos .md de conteudo-social/
// Verifica: travessao, ponto de exclamacao, estrutura "Nao e X. E Y.",
//           "sem precisar", "mesmo que", pergunta no GANCHO, palavra duplicada.
// Nao bloqueia (exit 0 sempre). Reporta no stdout para o Claude ver.

const path = require('path');

let input = '';
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
  try {
    const event = JSON.parse(input || '{}');
    const tool = event.tool_name || '';
    const params = event.tool_input || {};

    if (tool !== 'Write' && tool !== 'Edit') {
      process.exit(0);
    }

    const filePath = (params.file_path || '').replace(/\\/g, '/');

    // Apenas .md em conteudo-social/, anuncios/, emails/ ou copy-pagina/
    const isTarget = /\/(conteudo-social|anuncios|emails|copy-pagina)\//.test(filePath);
    const isMd = filePath.endsWith('.md');
    if (!isTarget || !isMd) {
      process.exit(0);
    }

    const content = params.content || params.new_string || '';
    if (!content || typeof content !== 'string') process.exit(0);

    const lines = content.split(/\r?\n/);
    const issues = [];

    // 1. Travessao
    lines.forEach((line, i) => {
      if (line.includes('\u2014')) {
        issues.push(`[ERRO] L${i+1}: travessao — "${line.trim().slice(0, 70)}"`);
      }
    });

    // 2. Ponto de exclamacao
    lines.forEach((line, i) => {
      if (line.includes('!')) {
        issues.push(`[ERRO] L${i+1}: ponto de exclamacao — "${line.trim().slice(0, 70)}"`);
      }
    });

    // 3. Estrutura "Nao e X. E Y." / "Nao foi X. Foi Y."
    const naoERegex = /\bNao (e|foi|era|sao|eram|sou|somos)\b[^.\n]{0,100}\.\s+\b(E|Foi|Era|Sao|Eram|Sou|Somos)\b/g;
    let m;
    while ((m = naoERegex.exec(content)) !== null) {
      const lineNum = content.substring(0, m.index).split('\n').length;
      issues.push(`[ERRO] L~${lineNum}: "Nao e X. E Y." — "${m[0].slice(0, 70)}"`);
    }

    // 4. "sem precisar" e "mesmo que"
    lines.forEach((line, i) => {
      if (/sem precisar/i.test(line)) {
        issues.push(`[ERRO] L${i+1}: "sem precisar" proibido — "${line.trim().slice(0, 70)}"`);
      }
      if (/mesmo que/i.test(line)) {
        issues.push(`[AVISO] L${i+1}: "mesmo que" como muleta — "${line.trim().slice(0, 70)}"`);
      }
    });

    // 5. Pergunta no GANCHO (linhas seguintes ao marcador [0-3s])
    lines.forEach((line, i) => {
      if (/\[0-3s\]\s+GANCHO/i.test(line)) {
        for (let j = i + 1; j <= Math.min(i + 3, lines.length - 1); j++) {
          if (lines[j].includes('?')) {
            issues.push(`[ERRO] L${j+1}: pergunta no GANCHO — "${lines[j].trim().slice(0, 70)}"`);
            break;
          }
        }
      }
    });

    // 6. Palavras duplicadas acidentais (ex: "que que", "de de")
    const dupeRegex = /\b(\w{3,})\s+\1\b/gi;
    while ((m = dupeRegex.exec(content)) !== null) {
      const lineNum = content.substring(0, m.index).split('\n').length;
      issues.push(`[AVISO] L~${lineNum}: palavra duplicada — "${m[0]}"`);
    }

    // 7. Erros de digitacao comuns em copy
    const typos = [
      [/\bvoce\b(?!\s+(?:nao|pode|vai|tem|quer|e\b|ja|ainda))/g, null], // nao e um erro, so checamos padroes abaixo
      [/\bq\b/g, '"q" sozinho (deve ser "que")'],
      [/\bp\b(?!\s*\.)/g, '"p" sozinho (deve ser "para" ou "por")'],
      [/  +/g, 'espaco duplo'],
      [/[.,;:]\s*\n\s*\n/g, 'pontuacao antes de linha em branco dupla'],
    ];
    typos.forEach(([regex, label]) => {
      if (!label) return;
      let match;
      regex.lastIndex = 0;
      while ((match = regex.exec(content)) !== null) {
        const lineNum = content.substring(0, match.index).split('\n').length;
        issues.push(`[AVISO] L~${lineNum}: ${label} — "${match[0].trim().slice(0, 40)}"`);
      }
    });

    // Relatorio
    const fileName = path.basename(filePath);
    if (issues.length === 0) {
      console.log(`COPY OK: ${fileName} — nenhum problema detectado.`);
    } else {
      const erros = issues.filter(x => x.startsWith('[ERRO]')).length;
      const avisos = issues.filter(x => x.startsWith('[AVISO]')).length;
      console.log(`REVISAO COPY: ${fileName}`);
      console.log(`${erros} erro(s), ${avisos} aviso(s):\n`);
      issues.slice(0, 12).forEach(issue => console.log('  ' + issue));
      if (issues.length > 12) {
        console.log(`  ... e mais ${issues.length - 12} ocorrencia(s).`);
      }
    }

    process.exit(0);
  } catch (_) {
    process.exit(0);
  }
});
