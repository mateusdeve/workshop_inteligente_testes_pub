/* ==========================================================================
   Painel de Entregas — Renderizador
   Lê window.PAINEL_DADOS (injetado inline no HTML) e monta cada painel
   no seu container respectivo. Zero dependências externas.
   ========================================================================== */

(function () {
  'use strict';

  // ---------- Utilidades ----------

  function esc(s) {
    if (s === null || s === undefined) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function get(obj, path, fallback) {
    if (!obj) return fallback;
    const parts = path.split('.');
    let cur = obj;
    for (const p of parts) {
      if (cur == null) return fallback;
      cur = cur[p];
    }
    return cur == null ? fallback : cur;
  }

  function isArray(x) { return Array.isArray(x); }

  function badgeClassForPreco(preco) {
    const n = typeof preco === 'number' ? preco : parseInt(String(preco || '').replace(/\D/g, ''), 10);
    if (!n) return 'badge-neutral';
    if (n <= 97) return 'badge-green';
    if (n <= 497) return 'badge-blue';
    if (n <= 1997) return 'badge-purple';
    return 'badge-dark';
  }

  function safeLink(url, label) {
    if (!url) return '';
    const u = String(url).trim();
    if (!u) return '';
    // Proibido: google search, youtube search, bing search (item spec)
    if (/google\.com\/search|youtube\.com\/results|bing\.com\/search/.test(u)) return '';
    return '<a class="link-small" href="' + esc(u) + '" target="_blank" rel="noopener">↗ ' + esc(label) + '</a>';
  }

  function writeSection(id, html) {
    const el = document.getElementById('panel-' + id);
    if (!el) return;
    el.innerHTML = html;
  }

  function renderError(id, sectionName, err) {
    const html =
      '<div class="breadcrumb">Painel de Entregas › ' + esc(sectionName) + '</div>' +
      '<div class="section-title">' + esc(sectionName) + '</div>' +
      '<div class="render-error">Não foi possível renderizar esta seção.<br>' +
      '<code>' + esc(String(err && err.message || err || 'dados ausentes')) + '</code></div>';
    writeSection(id, html);
  }

  function header(titulo, subtitulo) {
    return '<div class="breadcrumb">Painel de Entregas › ' + esc(titulo) + '</div>' +
      '<div class="section-title">' + esc(titulo) + '</div>' +
      '<div class="section-sub">' + esc(subtitulo || '') + '</div>';
  }

  // ---------- Componentes ----------

  function card(label, value, sub, extra) {
    return '<div class="card' + (extra && extra.cls ? ' ' + extra.cls : '') + '">' +
      (label ? '<div class="card-label">' + esc(label) + '</div>' : '') +
      (value ? '<div class="card-value"' + (extra && extra.valueStyle ? ' style="' + extra.valueStyle + '"' : '') + '>' + value + '</div>' : '') +
      (sub ? '<div class="card-sub">' + sub + '</div>' : '') +
      '</div>';
  }

  function cardHighlight(label, value) {
    return '<div class="card-highlight">' +
      '<div class="card-label">' + esc(label) + '</div>' +
      '<div class="card-value">' + esc(value) + '</div>' +
      '</div>';
  }

  function accordion(opts) {
    // opts: { headerHTML, bodyHTML, open }
    return '<div class="accordion' + (opts.open ? ' open' : '') + '">' +
      '<div class="accordion-header" onclick="toggleAcc(this)">' +
      opts.headerHTML +
      '<span class="accordion-icon">▾</span>' +
      '</div>' +
      '<div class="accordion-body">' + opts.bodyHTML + '</div>' +
      '</div>';
  }

  function pills(items, cls) {
    if (!isArray(items) || !items.length) return '';
    return '<div class="words-wrap">' +
      items.map(function (t) { return '<span class="badge ' + cls + '">' + esc(t) + '</span>'; }).join('') +
      '</div>';
  }

  function sparkline(idSuffix, path) {
    return '<div class="sparkline"><svg width="100%" height="36" viewBox="0 0 120 36" preserveAspectRatio="none">' +
      '<defs><linearGradient id="sg' + esc(idSuffix) + '" x1="0" y1="0" x2="0" y2="1">' +
      '<stop offset="0%" stop-color="#22c55e" stop-opacity="0.3"/>' +
      '<stop offset="100%" stop-color="#22c55e" stop-opacity="0"/></linearGradient></defs>' +
      '<path d="' + esc(path || 'M0,28 L30,24 L60,20 L90,14 L120,8 L120,36 L0,36 Z') + '" fill="url(#sg' + esc(idSuffix) + ')"/>' +
      '<path d="' + esc((path || 'M0,28 L30,24 L60,20 L90,14 L120,8').replace(/\sL\d+,\d+\sL\d+,\d+\sZ.*$/, '')) + '" fill="none" stroke="#22c55e" stroke-width="1.5"/>' +
      '</svg></div>';
  }

  // ---------- Renderers por seção ----------

  function renderVisaoGeral(d) {
    const p = d || {};
    const stats = isArray(p.statusBadges) ? p.statusBadges : [];
    const html =
      header('Visão Geral', get(p, 'subtitulo', 'Resumo do produto e informações principais.')) +
      '<div class="grid-3 mb-16">' +
        card('Nome do Produto', esc(get(p, 'nome', '')), esc(get(p, 'nomeSub', ''))) +
        card('Tipo', esc(get(p, 'tipo', '')), esc(get(p, 'tipoSub', ''))) +
        card('Preço', esc(get(p, 'preco', '')), esc(get(p, 'precoSub', '')), { valueStyle: 'font-size:24px;font-weight:700;color:var(--primary)' }) +
      '</div>' +
      '<div class="mb-16">' + cardHighlight('Quadro — Transformação Principal', get(p, 'quadro', '')) + '</div>' +
      '<div class="grid-2 mb-16">' +
        card('Nicho', esc(get(p, 'nicho', '')), esc(get(p, 'nichoSub', ''))) +
        card('Diferencial', esc(get(p, 'diferencial', '')), esc(get(p, 'diferencialSub', ''))) +
      '</div>' +
      '<div class="card"><div class="status-card">' +
        '<span class="status-dot"></span>' +
        '<span class="status-label">Produto ativo</span>' +
        '<span class="status-sep">·</span>' +
        '<span class="status-meta">' + esc(get(p, 'tipo', '')) + '</span>' +
        '<span class="status-sep">·</span>' +
        '<span class="status-meta">' + esc(get(p, 'preco', '')) + '</span>' +
        stats.map(function (b) { return '<span class="status-sep">·</span><span class="badge badge-green">' + esc(b) + '</span>'; }).join('') +
      '</div></div>';
    writeSection('visao-geral', html);
  }

  function renderQuadro(d) {
    const p = d || {};
    const html =
      header('Quadro', get(p, 'subtitulo', 'A transformação principal que o produto entrega ao cliente.')) +
      '<div class="mb-16">' + cardHighlight('Quadro Aprovado', get(p, 'quadro', '')) + '</div>' +
      '<div class="grid-2">' +
        card('Como Usar o Quadro', '', '<div class="card-body-text">' + (get(p, 'comoUsar', '') || '') + '</div>') +
        card('Regra do Quadro', '', '<div class="card-body-text">' + (get(p, 'regra', '') || '') + '</div>') +
      '</div>';
    writeSection('quadro', html);
  }

  function renderFuradeira(d) {
    const p = d || {};
    const steps = isArray(p.etapas) ? p.etapas : [];
    const stepsHTML = steps.map(function (s, i) {
      const isLast = i === steps.length - 1;
      return '<div class="step"><div class="step-left"><div class="step-num">' + (i + 1) + '</div>' +
        (isLast ? '' : '<div class="step-line"></div>') +
        '</div><div class="step-content">' +
        '<div class="step-title">' + esc(s.titulo || '') + '</div>' +
        '<div class="step-desc">' + esc(s.descricao || '') + '</div>' +
        '</div></div>';
    }).join('');
    const link = get(p, 'linkVisual', 'entregas/furadeira-visual.html');
    const html =
      header('Furadeira', get(p, 'subtitulo', 'O método estruturado que torna visível a eficiência do produto.')) +
      '<div class="card mb-16"><div class="card-label">Nome do Método</div>' +
        '<div class="card-value" style="font-size:20px">' + esc(get(p, 'nome', '')) + '</div></div>' +
      '<div class="card"><div class="card-label">Trilha do Método</div>' +
        '<div class="timeline">' + stepsHTML + '</div>' +
        '<a href="' + esc(link) + '" class="btn-inline" target="_blank">Ver Trilha Visual Completa →</a>' +
      '</div>';
    writeSection('furadeira', html);
  }

  function renderDecorados(d) {
    const p = d || {};
    const catBadge = {
      'Financeiro': 'badge-green',
      'Tempo': 'badge-blue',
      'Autoestima': 'badge-purple',
      'Reputação': 'badge-orange',
      'Reputacao': 'badge-orange',
      'Crescimento': 'badge-dark'
    };
    const cats = isArray(p.categorias) ? p.categorias : [];
    const accHTML = cats.map(function (c, i) {
      const badge = catBadge[c.nome] || 'badge-neutral';
      const itensHTML = '<ul>' + (isArray(c.itens) ? c.itens : []).map(function (it) {
        return '<li>' + esc(it) + '</li>';
      }).join('') + '</ul>';
      return accordion({
        open: i === 0,
        headerHTML: '<span class="badge ' + badge + '">' + esc(c.nome) + '</span>' +
                    '<span class="accordion-header-text">' + (c.itens ? c.itens.length : 10) + ' benefícios' + (c.labelExtra ? ' ' + esc(c.labelExtra) : '') + '</span>',
        bodyHTML: itensHTML
      });
    }).join('');
    const html = header('Decorados', get(p, 'subtitulo', '50 benefícios derivados do Quadro. Use para bullets de página, scripts de venda e conteúdo.')) + accHTML;
    writeSection('decorados', html);
  }

  function renderUrgencias(d) {
    const p = d || {};
    const meta = {
      'Dores':                 { badge: 'badge-pink',    desc: 'O que incomoda' },
      'Duvidas':               { badge: 'badge-indigo',  desc: 'O que pergunta' },
      'Dúvidas':               { badge: 'badge-indigo',  desc: 'O que pergunta' },
      'Desejos':               { badge: 'badge-violet',  desc: 'O que sonha' },
      'Assuntos Relacionados': { badge: 'badge-green',   desc: 'Porta de entrada' },
      'Urgências Quentes':     { badge: 'badge-orange',  desc: 'Alta intenção' },
      'Urgencias Quentes':     { badge: 'badge-orange',  desc: 'Alta intenção' },
      'Urgências Frias':       { badge: 'badge-neutral', desc: 'Alto volume' },
      'Urgencias Frias':       { badge: 'badge-neutral', desc: 'Alto volume' },
      'Urgências Inusitadas':  { badge: 'badge-purple',  desc: 'Ângulos inesperados' },
      'Urgencias Inusitadas':  { badge: 'badge-purple',  desc: 'Ângulos inesperados' }
    };
    const cats = isArray(p.categorias) ? p.categorias : [];
    const accHTML = cats.map(function (c) {
      const m = meta[c.nome] || { badge: 'badge-neutral', desc: '' };
      const itensHTML = '<ul>' + (isArray(c.itens) ? c.itens : []).map(function (it) {
        return '<li>' + esc(it) + '</li>';
      }).join('') + '</ul>';
      return accordion({
        headerHTML: '<span class="badge ' + m.badge + '">' + esc(c.nome) + '</span>' +
                    '<span class="accordion-header-text">' + esc(m.desc) + ' · ' + (c.itens ? c.itens.length : 10) + ' itens</span>',
        bodyHTML: itensHTML
      });
    }).join('');
    const html = header('Urgências Ocultas', get(p, 'subtitulo', '70 itens em 7 categorias. Use para temas de anúncio, bullets de página, ganchos de conteúdo e linhas de email.')) + accHTML;
    writeSection('urgencias', html);
  }

  function renderIdProduto(d) {
    const p = d || {};
    const args = isArray(p.argumentosIncontestaveis) ? p.argumentosIncontestaveis : [];
    const argsHTML = '<ul class="bullet-list">' +
      args.map(function (a) { return '<li>' + esc(a) + '</li>'; }).join('') + '</ul>';

    const objecoes = isArray(p.objecoes) ? p.objecoes : [];
    const argTipos = [
      '1. Argumento Incontestável',
      '2. Argumento Lógico (causa e efeito)',
      '3. Argumento por Analogia',
      '4. Argumento por Exemplificação',
      '5. Argumento de Valor (custo vs. benefício)',
      '6. Argumento de Consequência (agir vs. adiar)',
      '7. Argumento de Contradição'
    ];
    const objAccs = objecoes.map(function (o, i) {
      const quebras = isArray(o.quebras) ? o.quebras : [];
      const bodyHTML = '<div class="obj-body">' + quebras.slice(0, 7).map(function (q, idx) {
        const paragrafos = isArray(q.paragrafos) ? q.paragrafos : [q.paragrafo1, q.paragrafo2].filter(Boolean);
        return '<div class="arg-block">' +
          '<div class="arg-title">' + esc(argTipos[idx] || q.titulo || '').toUpperCase() + '</div>' +
          paragrafos.map(function (t) { return '<p class="arg-p">' + esc(t) + '</p>'; }).join('') +
          '</div>';
      }).join('') + '</div>';
      return accordion({
        headerHTML: '<span class="badge badge-pink">Objeção ' + (i + 1) + '</span>' +
                    '<span class="accordion-header-text">' + esc(o.texto || '') + '</span>',
        bodyHTML: bodyHTML
      });
    }).join('');

    const html =
      header('Identidade do Produto', get(p, 'subtitulo', 'Como o produto se posiciona e se diferencia no mercado.')) +
      '<div class="grid-2 mb-16">' +
        card('Diferencial Principal', esc(get(p, 'diferencial', '')), esc(get(p, 'diferencialSub', ''))) +
        card('Formato', '', '<div class="card-body-text">' + (get(p, 'formato', '') || '') + '</div>') +
      '</div>' +
      '<div class="card mb-16"><div class="card-label">Argumentos Incontestáveis</div>' + argsHTML + '</div>' +
      '<div class="card"><div class="card-label">Objeções Principais e Como Quebrar</div>' + objAccs + '</div>';
    writeSection('id-produto', html);
  }

  function renderIdConsumidor(d) {
    const p = d || {};
    const demo = p.demografico || {};
    const comp = p.comportamento || {};
    const paliativos = isArray(p.paliativos) ? p.paliativos : [];
    const baldes = isArray(p.baldes) ? p.baldes : [];

    const demoHTML = '<div class="profile-line">' + Object.keys(demo).map(function (k) {
      return '<strong>' + esc(k) + ':</strong> ' + esc(demo[k]) + '<br>';
    }).join('') + '</div>';

    const compHTML = '<div class="profile-line">' + Object.keys(comp).map(function (k) {
      return '<strong>' + esc(k) + ':</strong> ' + esc(comp[k]) + '<br>';
    }).join('') + '</div>';

    const paliativosHTML = paliativos.length
      ? '<div class="card mb-16"><div class="card-label">Paliativos</div>' +
        '<ul class="bullet-list">' +
        paliativos.map(function (pl) {
          return '<li><strong>' + esc(pl.nome || '') + '</strong> → ' + esc(pl.porque || '') + '</li>';
        }).join('') + '</ul></div>'
      : '';

    const baldesHTML = baldes.length
      ? '<div class="card"><div class="card-label">Baldes de Para Quem É</div>' +
        baldes.map(function (b) {
          return accordion({
            headerHTML: '<span class="badge badge-neutral">' + esc(b.perfil || '') + '</span>' +
                        '<span class="accordion-header-text">5 afirmações</span>',
            bodyHTML: '<ul>' + (isArray(b.afirmacoes) ? b.afirmacoes : []).map(function (a) {
              return '<li>' + esc(a) + '</li>';
            }).join('') + '</ul>'
          });
        }).join('') + '</div>'
      : '';

    const html =
      header('Identidade do Consumidor', get(p, 'subtitulo', 'Perfil detalhado do cliente ideal.')) +
      '<div class="mb-16">' + cardHighlight('Para Quem É', get(p, 'paraQuemE', '')) + '</div>' +
      '<div class="grid-2 mb-16">' +
        card('Perfil Demográfico', '', demoHTML) +
        card('Comportamento e Canais', '', compHTML) +
      '</div>' +
      paliativosHTML +
      baldesHTML;
    writeSection('id-consumidor', html);
  }

  function renderIdComunicador(d) {
    const p = d || {};
    const refs = isArray(p.referencias) ? p.referencias : [];
    const refsHTML = refs.length
      ? '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">' +
        refs.map(function (r) {
          return '<div style="background:var(--main-bg);border-radius:var(--r2);padding:12px">' +
            '<div style="font-weight:700;color:var(--text-1);font-size:13px;margin-bottom:4px">' + esc(r.nome || '') + '</div>' +
            '<div style="font-size:13px;color:var(--text-2);line-height:1.6">' + esc(r.motivo || '') + '</div>' +
            '</div>';
        }).join('') + '</div>'
      : '<div class="card-sub">nenhuma ainda</div>';

    const mantras = isArray(p.mantras) ? p.mantras : [];
    const mantrasHTML = mantras.length
      ? '<div class="card-body-text">' + mantras.map(esc).join('<br>') + '</div>'
      : '<div class="card-sub">nenhum ainda</div>';

    const html =
      header('Identidade do Comunicador', get(p, 'subtitulo', 'Tom, posicionamento e linguagem do criador.')) +
      '<div class="grid-3 mb-16">' +
        card('Comunicador', esc(get(p, 'nome', '')), esc(get(p, 'especialidade', ''))) +
        card('Valores', '', pills(p.valores, 'badge-green')) +
        card('Mantras e Jargões', '', mantrasHTML) +
      '</div>' +
      '<div class="grid-2 mb-16">' +
        card('Formatos que Combinam', '', pills(p.formatos, 'badge-indigo')) +
        card('Estilo Visual Recomendado', '', pills(p.estiloVisual, 'badge-neutral')) +
      '</div>' +
      '<div class="card mb-16"><div class="card-label">Referências de Comunicação</div>' + refsHTML + '</div>' +
      '<div class="grid-2 mb-16">' +
        card('Tom de Voz', '', '<div class="card-body-text">' + esc(get(p, 'tomDeVoz', '')) + '</div>') +
        card('Posicionamento', '', '<div class="card-body-text">' + esc(get(p, 'posicionamento', '')) + '</div>') +
      '</div>' +
      '<div class="grid-2">' +
        card('Palavras que Conectam', '', pills(p.palavrasConectam, 'badge-green')) +
        card('Palavras que Afastam', '', pills(p.palavrasAfastam, 'badge-pink')) +
      '</div>';
    writeSection('id-comunicador', html);
  }

  function renderPesquisa(d) {
    const p = d || {};
    const kpis = isArray(p.kpis) ? p.kpis : [];
    const kpisHTML = kpis.slice(0, 4).map(function (k, i) {
      const trendCls = k.trendDir === 'up' ? 'up' : (k.trendDir === 'down' ? 'down' : 'neutral');
      const trendSym = k.trendDir === 'up' ? '▲' : (k.trendDir === 'down' ? '▼' : '●');
      return '<div class="kpi-card">' +
        '<div class="kpi-label">' + esc(k.label || '') + '</div>' +
        '<div class="kpi-value">' + esc(k.valor || '') + '</div>' +
        '<div class="kpi-trend ' + trendCls + '">' + trendSym + ' ' + esc(k.trend || '') + '</div>' +
        sparkline(String(i + 1), k.sparkPath) +
        '</div>';
    }).join('');

    const oportunidades = isArray(p.oportunidades) ? p.oportunidades : [];
    const oppHTML = oportunidades.map(function (o, i) {
      return '<div class="opp-item"><span class="num-circle">' + (i + 1) + '</span>' + esc(o) + '</div>';
    }).join('');

    const concs = isArray(p.concorrentes) ? p.concorrentes : [];
    const avatarColors = ['#22c55e', '#3b82f6', '#a855f7', '#f97316', '#6b7280'];
    const topConcsHTML = concs.slice(0, 5).map(function (c, i) {
      const cor = avatarColors[i % avatarColors.length];
      const inicial = (c.nome || '?').charAt(0).toUpperCase();
      const links = [safeLink(c.linkPagina, 'Página'), safeLink(c.linkInstagram, 'Instagram')].filter(Boolean).join(' ');
      return '<div style="display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid var(--border-2)">' +
        '<div class="comp-avatar" style="background:' + cor + '">' + esc(inicial) + '</div>' +
        '<div style="flex:1">' +
          '<div style="font-size:14px;font-weight:600;color:var(--text-1)">' + esc(c.nome || '') + '</div>' +
          '<div style="font-size:12px;color:var(--text-3)">' + esc(c.formato || '') + '</div>' +
          (links ? '<div style="margin-top:4px">' + links + '</div>' : '') +
        '</div>' +
        '<span class="badge ' + badgeClassForPreco(c.preco) + '">' + esc(c.preco || '') + '</span>' +
        '</div>';
    }).join('');

    const tabelaRows = concs.map(function (c) {
      const links = [safeLink(c.linkPagina, 'Página'), safeLink(c.linkInstagram, 'Instagram')].filter(Boolean).join(' ');
      return '<tr>' +
        '<td>' + esc(c.nome || '') + '</td>' +
        '<td>' + esc(c.promessa || '') + '</td>' +
        '<td>' + esc(c.formato || '') + '</td>' +
        '<td><span class="badge ' + badgeClassForPreco(c.preco) + '">' + esc(c.preco || '') + '</span></td>' +
        '<td>' + esc(c.diferencial || '') + '</td>' +
        '<td>' + (links || '<span style="color:var(--text-3)">—</span>') + '</td>' +
        '</tr>';
    }).join('');

    const termosEmAlta = isArray(p.termosEmAlta) ? p.termosEmAlta : [];
    const termosHTML = termosEmAlta.map(function (t) {
      const size = t.peso === 'alto' ? '13px' : '11px';
      return '<span class="badge badge-green" style="font-size:' + size + '">' + esc(t.termo || t) + '</span>';
    }).join('');

    const padroesAnuncio = isArray(p.padroesAnuncio) ? p.padroesAnuncio : [];
    const padroesHTML = '<ul class="bullet-list">' +
      padroesAnuncio.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';

    const reclamacoes = isArray(p.reclamacoes) ? p.reclamacoes : [];
    const reclHTML = reclamacoes.map(function (r) {
      return '<div class="complaint-row">' +
        '<div class="complaint-label"><span>' + esc(r.categoria || '') + '</span><span>' + esc(r.percentual || '') + '%</span></div>' +
        '<div class="complaint-bar-bg"><div class="complaint-bar-fill" style="width:' + esc(String(r.percentual || 0)) + '%"></div></div>' +
        '</div>';
    }).join('');

    const cuidados = isArray(p.cuidados) ? p.cuidados : [];
    const cuidadosHTML = '<ul class="bullet-list">' +
      cuidados.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';

    const fontes = isArray(p.fontes) ? p.fontes : [];
    const fontesHTML = '<div style="columns:2;column-gap:16px">' +
      fontes.slice(0, 8).map(function (f) {
        return '<div style="font-size:12px;color:var(--text-2);line-height:1.6;padding:4px 0;break-inside:avoid">' +
          '<span style="color:var(--primary);margin-right:4px">↗</span>' + esc(typeof f === 'string' ? f : (f.nome || '')) +
          (f.descricao ? ' <span style="color:var(--text-3)">— ' + esc(f.descricao) + '</span>' : '') +
          '</div>';
      }).join('') + '</div>';

    const confianca = get(p, 'confianca', { percentual: 75, label: 'Média' });

    const html =
      header('Pesquisa de Mercado', get(p, 'subtitulo', 'Dashboard de inteligência de mercado. Use para argumentos, copy e posicionamento.')) +
      '<div class="grid-4 mb-16">' + kpisHTML + '</div>' +
      '<div class="card mb-16"><div class="card-label" style="color:var(--primary)">Oportunidades Identificadas</div>' +
        '<div style="margin-top:8px">' + oppHTML + '</div></div>' +
      '<div class="grid-2 mb-16">' +
        '<div class="card"><div class="card-label">Top 5 Concorrentes</div>' + topConcsHTML + '</div>' +
        '<div class="card"><div class="card-label">Padrões de Reclamação</div>' + reclHTML + '</div>' +
      '</div>' +
      '<div class="grid-2 mb-16">' +
        '<div class="card"><div class="card-label">Cuidados e Riscos</div>' + cuidadosHTML + '</div>' +
        '<div class="card"><div class="card-label">Padrões de Anúncio que Performam</div>' + padroesHTML + '</div>' +
      '</div>' +
      '<div class="card mb-16"><div class="card-label">Análise Completa de Concorrentes</div>' +
        '<table class="comp-table"><thead><tr>' +
          '<th>Nome</th><th>Promessa</th><th>Formato</th><th>Preço</th><th>Diferencial</th><th>Links</th>' +
        '</tr></thead><tbody>' + tabelaRows + '</tbody></table></div>' +
      (termosEmAlta.length ? '<div class="card mb-16"><div class="card-label">Termos em Alta</div>' +
        '<div class="words-wrap">' + termosHTML + '</div></div>' : '') +
      '<div class="card"><div class="card-label">Confiança da Pesquisa e Fontes</div>' +
        '<div class="circ-wrap"><div>' +
          '<svg viewBox="0 0 120 120" width="120" height="120">' +
          '<circle cx="60" cy="60" r="50" fill="none" stroke="var(--border-2)" stroke-width="8"/>' +
          '<circle cx="60" cy="60" r="50" fill="none" stroke="var(--primary)" stroke-width="8"' +
            ' stroke-dasharray="' + esc(String((confianca.percentual || 0) * 3.14)) + ' 314"' +
            ' transform="rotate(-90 60 60)"/>' +
          '<text x="60" y="64" font-size="22" font-weight="800" fill="var(--text-1)" text-anchor="middle">' + esc(String(confianca.percentual || 0)) + '%</text>' +
          '</svg>' +
          '<div class="circ-label">Confiança ' + esc(confianca.label || '') + '</div>' +
        '</div><div style="flex:1">' + fontesHTML + '</div></div></div>';
    writeSection('pesquisa', html);
  }

  // ---------- Bootstrap ----------

  const SECOES = [
    { id: 'visao-geral',     titulo: 'Visão Geral',               render: renderVisaoGeral },
    { id: 'quadro',          titulo: 'Quadro',                    render: renderQuadro },
    { id: 'furadeira',       titulo: 'Furadeira',                 render: renderFuradeira },
    { id: 'decorados',       titulo: 'Decorados',                 render: renderDecorados },
    { id: 'urgencias',       titulo: 'Urgências Ocultas',         render: renderUrgencias },
    { id: 'id-produto',      titulo: 'Identidade do Produto',     render: renderIdProduto },
    { id: 'id-consumidor',   titulo: 'Identidade do Consumidor',  render: renderIdConsumidor },
    { id: 'id-comunicador',  titulo: 'Identidade do Comunicador', render: renderIdComunicador },
    { id: 'pesquisa',        titulo: 'Pesquisa de Mercado',       render: renderPesquisa }
  ];

  function renderTudo() {
    const dados = window.PAINEL_DADOS || {};
    SECOES.forEach(function (s) {
      try {
        s.render(dados[s.id] || {});
      } catch (err) {
        console.error('[painel] erro ao renderizar', s.id, err);
        renderError(s.id, s.titulo, err);
      }
    });
  }

  // ---------- Navegação ----------

  window.showPanel = function (id, el) {
    document.querySelectorAll('.panel').forEach(function (p) { p.classList.remove('active'); });
    const tgt = document.getElementById('panel-' + id);
    if (tgt) tgt.classList.add('active');
    document.querySelectorAll('.nav-item, .mobile-tab').forEach(function (n) { n.classList.remove('active'); });
    if (el) el.classList.add('active');
  };

  window.toggleAcc = function (header) {
    const acc = header.closest('.accordion');
    if (acc) acc.classList.toggle('open');
  };

  // Render ao carregar. Se o script vier antes do body, espera DOMContentLoaded.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderTudo);
  } else {
    renderTudo();
  }

  // Expõe para debug/regeneração seccionada
  window.__painelRender = { renderTudo: renderTudo, secoes: SECOES };
})();
