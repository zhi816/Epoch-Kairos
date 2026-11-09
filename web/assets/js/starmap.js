/**
 * starmap.js：首頁知識星圖（web/index.html）互動
 *
 * 資料：頁面內 <script id="ek-data">，由 tools/build_home.py 自 wiki/ Frontmatter 產生；本檔不含任何論文資料。
 * 學科色：執行時讀取 theme.css 之 --color-<domain>（色碼唯一真實來源）。
 * 桌面：滑過或點選星點顯示說明框；點學科中心或懸星索引篩選學科。
 * 手機（860px 以下）：總覽只能點學科中心；點學科中心或篩選列放大該區，放大後才能點星（DESIGN.md 第二章第 5 節）。
 * 我的星系：網址錨點 #my-constellation；入口為「人類群星閃耀時」句末之星，觸控需點兩下（DESIGN.md 第四章）。
 * 動畫一律受 prefers-reduced-motion 控制。
 */
(function () {
  'use strict';

  var D = JSON.parse(document.getElementById('ek-data').textContent);
  var FO = D.focus;
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  };
  var mqReduce = matchMedia('(prefers-reduced-motion: reduce)');
  var mqMobile = matchMedia('(max-width: 860px)');
  var reduce = mqReduce.matches;
  var mobile = mqMobile.matches;

  /* ---------- 色彩（取自 theme.css） ---------- */
  function rgbOf(c) {
    var h = String(c).trim().replace('#', '');
    if (h.length === 3) h = h.replace(/./g, function (x) { return x + x; });
    if (!/^[0-9a-f]{6}$/i.test(h)) return '232,228,218';
    var n = parseInt(h, 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255].join(',');
  }
  var css = getComputedStyle(document.documentElement);
  var DOM = {};
  D.domains.forEach(function (d) {
    d.color = css.getPropertyValue('--color-' + d.key).trim() || '#EAE6DF';
    d.rgb = rgbOf(d.color);
    DOM[d.key] = d;
  });
  var IV = '244,241,234';
  var BLUE = DOM.ai.rgb;
  var BLUE_C = DOM.ai.color;
  document.documentElement.style.setProperty('--blue-rgb', BLUE);
  var RING = 'M0.8 5 A4.2 4.2 0 1 0 9.2 5 A4.2 4.2 0 1 0 0.8 5 Z M4.1 5 A0.9 0.9 0 1 0 5.9 5 A0.9 0.9 0 1 0 4.1 5 Z';
  var DIAMOND2 = 'M5 0.3 L9.7 5 L5 9.7 L0.3 5 Z M5 2.7 L7.3 5 L5 7.3 L2.7 5 Z';
  var TH = '__thesis';

  /* ---------- 資料索引 ---------- */
  var byP = {}, byF = {}, roleName = {}, conceptBy = {};
  D.papers.forEach(function (p) { byP[p.slug] = p; });
  D.concepts.forEach(function (c) { conceptBy[c.slug] = c; });
  if (FO) {
    FO.papers.forEach(function (p) { byF[p.slug] = p; });
    FO.roles.forEach(function (r) { roleName[r[0]] = r[1]; });
  }
  var domainOrder = D.domains.slice().sort(function (a, b) { return (b.count > 0) - (a.count > 0); });
  /* 星點之鍵盤順序：依學科索引順序，同學科內依時間線由新到舊（與懸星索引之珠子同序） */
  var paperOrder = [];
  domainOrder.forEach(function (d) {
    D.papers.filter(function (p) { return p.d === d.key; }).forEach(function (p) { paperOrder.push(p); });
  });
  /* 論文是否屬於某學科篩選：本身學科相同，或帶有該學科之標籤 */
  function paperIn(p, k) { return p.d === k || p.tags.some(function (t) { return D.tags[t].d === k; }); }
  function fRgb(p) { return p.d === 'human' ? DOM.human.rgb : BLUE; }
  function fCol(p) { return p.d === 'human' ? DOM.human.color : BLUE_C; }
  function fMatch(p, key) { return key === 'all' || key === 'role:' + p.role || (key.indexOf('con:') === 0 && p.con.indexOf(key.slice(4)) >= 0); }
  function hubOf(k) { return FO.hubs.filter(function (h) { return h.key === k; })[0]; }
  var linkCount = D.domains.length + Object.keys(D.tags).length;
  D.papers.forEach(function (p) { linkCount += p.tags.length; });
  D.concepts.forEach(function (c) { linkCount += c.papers.length; });
  var fLinkCount = 0;
  if (FO) { fLinkCount = FO.hubs.length; FO.papers.forEach(function (p) { fLinkCount += p.con.length; }); }

  /* 群星開場不預選任何論文（2026-11-09 使用者決定：流光干擾操作感）；我的星系預設亮「我的碩論」 */
  var S = { mode: 'stars', filter: null, note: null, sel: null, hoverC: null, pinC: null, hover: null, hoverD: null, ffilter: 'all', fsel: TH, armed: false };

  function rndFrom(seed) {
    var s = seed | 0;
    return function () {
      s = (s + 0x6D2B79F5) | 0;
      var t = Math.imul(s ^ (s >>> 15), 1 | s);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  /* ---------- 星空背景：固定種子，約半數集中於斜向銀河帶 ---------- */
  var sky = $('sky'), sctx = sky.getContext('2d'), skyStars = [];
  (function () {
    var r = rndFrom(8161108), tints = ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFF3E2', '#E4EEFF'];
    for (var i = 0; i < 1600; i++) {
      var band = r() < 0.45, x = r();
      var y = band ? 0.84 - x * 0.66 + (r() + r() + r() - 1.5) * 0.1 : r();
      var q = r(), sz = q < 0.66 ? 1 : (q < 0.94 ? 1.5 : 2.2);
      skyStars.push({ x: x, y: Math.max(0, Math.min(0.998, y)), r: sz / 2, o: sz > 2 ? 0.92 : (sz > 1 ? 0.7 : 0.3 + r() * 0.45),
        c: tints[Math.floor(r() * tints.length)], tw: sz >= 1.5 && r() < 0.4, ph: r() * 6.283 });
    }
  })();
  function drawSky(t) {
    var w = innerWidth, h = innerHeight, dpr = Math.min(devicePixelRatio || 1, 2);
    if (sky.width !== Math.round(w * dpr) || sky.height !== Math.round(h * dpr)) { sky.width = Math.round(w * dpr); sky.height = Math.round(h * dpr); }
    sctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    sctx.clearRect(0, 0, w, h);
    var n = Math.round(1600 * Math.max(0.3, Math.min(1.25, (w * h) / (1440 * 900))));
    for (var i = 0; i < n; i++) {
      var s = skyStars[i], o = s.o;
      if (s.tw && t) o *= 0.61 + 0.39 * Math.sin(t / 764 + s.ph);
      sctx.globalAlpha = o;
      sctx.fillStyle = s.c;
      sctx.beginPath();
      sctx.arc(s.x * w, s.y * h, s.r, 0, 6.283);
      sctx.fill();
      if (s.r > 1) { sctx.globalAlpha = o * 0.18; sctx.beginPath(); sctx.arc(s.x * w, s.y * h, s.r * 2.6, 0, 6.283); sctx.fill(); }
    }
    sctx.globalAlpha = 1;
  }
  var skyRaf = 0, lastSky = 0;
  function skyLoop(t) { if (t - lastSky > 66) { drawSky(t); lastSky = t; } skyRaf = requestAnimationFrame(skyLoop); }
  function startSky() { cancelAnimationFrame(skyRaf); drawSky(0); if (!reduce) skyRaf = requestAnimationFrame(skyLoop); }

  /* ---------- 星圖共用 ---------- */
  var map = $('map'), panel = $('panel'), nodes = [], labelRects = [];
  var stage = { w: 1000, h: 1000 }, view = { x: 0, y: 0, w: 1000, h: 1000 }, tween = null, gid = 0, built = '';
  var tip = null, tipEls = null, hoverTimer = 0;

  function shapeSvg(path, color, size, sw) {
    return '<svg width="' + size + '" height="' + size + '" viewBox="0 0 10 10" aria-hidden="true" focusable="false"><path d="' + path + '" fill="none" stroke="' + color + '" stroke-width="' + (sw || 1) + '"/></svg>';
  }
  function curve(x1, y1, x2, y2) {
    var dx = x2 - x1, dy = y2 - y1, cx = (x1 + x2) / 2 - dy * 0.13, cy = (y1 + y2) / 2 + dx * 0.13;
    return 'M' + x1 + ' ' + y1 + ' Q' + cx.toFixed(1) + ' ' + cy.toFixed(1) + ' ' + x2 + ' ' + y2;
  }
  /* 連線：二次貝茲曲線＋學科色漸層；選取中的路徑加流光 */
  function edge(o) {
    var g = 'eg' + (gid++), d = curve(o.x1, o.y1, o.x2, o.y2);
    var s = '<linearGradient id="' + g + '" gradientUnits="userSpaceOnUse" x1="' + o.x1 + '" y1="' + o.y1 + '" x2="' + o.x2 + '" y2="' + o.y2 + '"><stop offset="0" stop-color="rgba(' + o.c1 + ',' + o.a.toFixed(3) + ')"/><stop offset="1" stop-color="rgba(' + o.c2 + ',' + (o.a * o.fade).toFixed(3) + ')"/></linearGradient>';
    s += '<path d="' + d + '" fill="none" stroke="url(#' + g + ')" stroke-width="' + (o.w || 1.1) + '" stroke-linecap="round" vector-effect="non-scaling-stroke"' + (o.dash ? ' stroke-dasharray="' + o.dash + '"' : '') + '/>';
    if (o.flow && !reduce) s += '<path class="flow" d="' + d + '" fill="none" stroke="rgba(255,253,248,0.9)" stroke-width="1.6" stroke-linecap="round" vector-effect="non-scaling-stroke"/>';
    return s;
  }
  function mk(html) { var w = document.createElement('div'); w.className = 'nd'; w.innerHTML = html; map.appendChild(w); return w; }
  function sideOf(x, y) {
    var dx = x - stage.w / 2, dy = y - stage.h / 2;
    if (Math.abs(dy) > Math.abs(dx) * 1.6) return dy < 0 ? 'u' : 'd';
    return dx >= 0 ? 'r' : 'l';
  }
  function addNode(el, x, y, lab, pri, side) {
    var n = { el: el, x: x, y: y, lab: lab || null, pri: pri == null ? 2 : pri, show: !!lab, side: side || sideOf(x, y) };
    if (lab) lab.style.opacity = 0; /* 避讓排好後才淡入，避免首幀重疊 */
    nodes.push(n);
    return n;
  }
  function hoverable(el, enter, leave) {
    el.addEventListener('pointerenter', function (e) { if (e.pointerType !== 'touch') enter(); });
    el.addEventListener('pointerleave', function (e) { if (e.pointerType !== 'touch') leave(); });
    el.addEventListener('focus', enter);
    el.addEventListener('blur', leave);
  }
  function setAR(r) { map.style.setProperty('--ar', String(r)); }
  function place() {
    var v = view, bg = map.querySelector('svg.bg');
    if (bg) bg.setAttribute('viewBox', v.x.toFixed(1) + ' ' + v.y.toFixed(1) + ' ' + v.w.toFixed(1) + ' ' + v.h.toFixed(1));
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      n.el.style.left = ((n.x - v.x) / v.w * 100) + '%';
      n.el.style.top = ((n.y - v.y) / v.h * 100) + '%';
    }
  }
  function fullView() { return { x: 0, y: 0, w: stage.w, h: stage.h }; }
  function animateTo(t) {
    if (tween) cancelAnimationFrame(tween.raf);
    if (reduce) { view = t; place(); layoutLabels(); return; }
    var f = { x: view.x, y: view.y, w: view.w, h: view.h }, t0 = performance.now(), dur = 560;
    tween = {};
    (function step(now) {
      var k = Math.min(1, (now - t0) / dur), e = k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
      view = { x: f.x + (t.x - f.x) * e, y: f.y + (t.y - f.y) * e, w: f.w + (t.w - f.w) * e, h: f.h + (t.h - f.h) * e };
      place();
      if (k < 1) tween.raf = requestAnimationFrame(step); else { tween = null; layoutLabels(); }
    })(t0);
  }

  /* 標籤避讓：依優先序逐一放置，試外側、另一側與上下偏移；放不下的次要標籤暫時隱藏（DESIGN.md 第二章第 5 節） */
  function slotsFor(side) {
    var base = side === 'u' ? ['u', 'r', 'l', 'd'] : side === 'd' ? ['d', 'r', 'l', 'u'] : side === 'l' ? ['l', 'r', 'u', 'd'] : ['r', 'l', 'u', 'd'];
    var out = base.map(function (s) { return [s, 0]; });
    [-12, 12, -24, 24].forEach(function (dy) { base.forEach(function (s) { if (s === 'r' || s === 'l') out.push([s, dy]); }); });
    return out;
  }
  function declutter() {
    var box = (mobile ? map : panel).getBoundingClientRect(), placed = [];
    var top = box.top + (mobile ? 0 : 38), bottom = box.bottom - (mobile ? 0 : 30);
    var items = nodes.filter(function (n) {
      if (!n.lab) return false;
      if (!n.show) { n.lab.style.opacity = 0; return false; }
      return true;
    });
    items.sort(function (a, b) { return a.pri - b.pri; });
    items.forEach(function (n) {
      var lab = n.lab, slots = slotsFor(n.side), best = null;
      function setSlot(sl) { ['r', 'l', 'u', 'd'].forEach(function (c) { lab.classList.toggle(c, sl[0] === c); }); lab.style.marginTop = sl[1] ? sl[1] + 'px' : ''; }
      for (var i = 0; i < slots.length; i++) {
        setSlot(slots[i]);
        var r = lab.getBoundingClientRect();
        if (r.left < box.left + 2 || r.right > box.right - 2 || r.top < top || r.bottom > bottom) continue;
        var ov = 0;
        placed.forEach(function (q) {
          var w = Math.min(r.right, q.right + 3) - Math.max(r.left, q.left - 3), h = Math.min(r.bottom, q.bottom + 1) - Math.max(r.top, q.top - 1);
          if (w > 0 && h > 0) ov += w * h;
        });
        if (!best || ov < best.ov) best = { i: i, ov: ov, r: r };
        if (ov === 0) break;
      }
      /* 學科與論文名稱一律顯示（取重疊最少處）；標籤與概念名稱放不下就隱藏 */
      /* 說明框避讓權重：學科與概念名稱 6、論文名稱 4、標籤 2 */
      var wt = n.pri === 1 || n.pri === 4 ? 6 : (n.pri === 3 ? 2 : 4);
      if (best && (best.ov === 0 || n.pri <= 2 || n.must)) { setSlot(slots[best.i]); placed.push(withW(best.r, wt)); lab.style.opacity = 1; }
      else if (!best && (n.pri <= 2 || n.must)) { setSlot(slots[0]); placed.push(withW(lab.getBoundingClientRect(), wt)); lab.style.opacity = 1; }
      else lab.style.opacity = 0;
    });
    labelRects = placed;
    lastCSig = cSig();
  }
  /* 目前應顯示名稱之概念頁；滑過時若有變動才重排標籤 */
  var lastCSig = '';
  function cSig() { return nodes.filter(function (n) { return n.el.dataset.c && n.show; }).map(function (n) { return n.el.dataset.c; }).join(','); }
  function withW(r, w) { return { left: r.left, right: r.right, top: r.top, bottom: r.bottom, w: w }; }
  function layoutLabels() { declutter(); renderTip(); }

  /* ---------- 群星星圖 ---------- */
  function domainView(k) {
    var d = DOM[k], pts = [d.hub];
    d.tags.forEach(function (t) { pts.push([D.tags[t].x, D.tags[t].y]); });
    D.papers.forEach(function (p) { if (p.d === k) pts.push([p.x, p.y]); });
    var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; });
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
    var size = Math.min(1000, Math.max(400, Math.max(x1 - x0, y1 - y0) + 190)), cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    return { x: Math.max(-60, Math.min(1060 - size, cx - size / 2)), y: Math.max(-60, Math.min(1060 - size, cy - size / 2)), w: size, h: size };
  }

  function buildStars() {
    stage = { w: 1000, h: 1000 };
    setAR(1);
    nodes = [];
    var h = '<svg class="bg" viewBox="0 0 1000 1000" preserveAspectRatio="none" aria-hidden="true" focusable="false"><defs>';
    D.domains.forEach(function (d) {
      h += '<radialGradient id="nb-' + d.key + '"><stop offset="0" stop-color="rgba(' + d.rgb + ',0.10)"/><stop offset="0.5" stop-color="rgba(' + d.rgb + ',0.04)"/><stop offset="1" stop-color="rgba(' + d.rgb + ',0)"/></radialGradient>';
    });
    h += '</defs><g class="nebs">';
    D.domains.forEach(function (d) { h += '<circle data-k="' + d.key + '" cx="' + d.hub[0] + '" cy="' + d.hub[1] + '" r="' + (d.count ? 280 : 160) + '" fill="url(#nb-' + d.key + ')"/>'; });
    var ticks = '';
    for (var i = 0; i < 72; i++) {
      var an = i * 5 * Math.PI / 180, r2 = i % 6 === 0 ? 474 : 482;
      ticks += 'M' + (500 + 490 * Math.cos(an)).toFixed(1) + ' ' + (500 + 490 * Math.sin(an)).toFixed(1) + ' L' + (500 + r2 * Math.cos(an)).toFixed(1) + ' ' + (500 + r2 * Math.sin(an)).toFixed(1) + ' ';
    }
    for (var j = 0; j < 24; j++) {
      var a2 = j * 15 * Math.PI / 180;
      ticks += 'M' + (500 + 210 * Math.cos(a2)).toFixed(1) + ' ' + (500 + 210 * Math.sin(a2)).toFixed(1) + ' L' + (500 + 204 * Math.cos(a2)).toFixed(1) + ' ' + (500 + 204 * Math.sin(a2)).toFixed(1) + ' ';
    }
    h += '</g><g fill="none" stroke="rgba(232,228,218,0.07)" stroke-width="1">' +
      '<circle cx="500" cy="500" r="120" stroke-dasharray="2 6" vector-effect="non-scaling-stroke"/>' +
      '<circle cx="500" cy="500" r="210" stroke-dasharray="1 7" vector-effect="non-scaling-stroke"/>' +
      '<circle cx="500" cy="500" r="490" vector-effect="non-scaling-stroke"/>' +
      '<circle cx="500" cy="500" r="498" stroke="rgba(232,228,218,0.04)" vector-effect="non-scaling-stroke"/>' +
      '<path d="' + ticks + '" stroke="rgba(232,228,218,0.10)" vector-effect="non-scaling-stroke"/>' +
      '<path d="M500 10 V990 M10 500 H990" stroke="rgba(232,228,218,0.035)" vector-effect="non-scaling-stroke"/>' +
      '<circle cx="500" cy="500" r="24" stroke="rgba(232,228,218,0.22)" vector-effect="non-scaling-stroke"/>' +
      '<circle cx="500" cy="500" r="33" stroke="rgba(232,228,218,0.12)" stroke-dasharray="1 3" vector-effect="non-scaling-stroke"/>' +
      '</g><g class="edges"></g></svg>';
    map.innerHTML = h;

    /* 中心 Kairos 奇點：十字光芒 */
    var k = '<span class="kairos" aria-hidden="true"></span>';
    if (!mobile) {
      k = [[132, 0, 0.8], [132, 90, 0.8], [52, 45, 0.45], [52, -45, 0.45]].map(function (f) {
        return '<span class="flare" aria-hidden="true" style="width:' + f[0] + 'px;transform:rotate(' + f[1] + 'deg) translate(-50%,-0.5px);opacity:' + (f[2] / 0.8) + '"></span>';
      }).join('') + k + '<span class="klbl" aria-hidden="true">KAIROS</span>';
    }
    addNode(mk(k), 500, 500);

    Object.keys(D.tags).forEach(function (t) {
      var tg = D.tags[t], d = DOM[tg.d];
      var w = mk('<span class="dot" aria-hidden="true" style="width:3px;height:3px;box-shadow:0 0 5px 1.5px rgba(' + d.rgb + ',.75)"></span><span class="lbl r" aria-hidden="true">' + esc(t) + (mobile ? '' : '<sup>' + tg.count + '</sup>') + '</span>');
      w.dataset.t = t;
      addNode(w, tg.x, tg.y, w.querySelector('.lbl'), 3);
    });
    D.domains.forEach(function (d) {
      var lab = mobile ? esc(d.name) + ' <span style="font-family:var(--font-serif);color:var(--muted)">' + d.count + '</span>' : esc(d.name) + '<sup>' + d.count + '</sup>';
      var w = mk('<button type="button" class="hub" data-hub="' + d.key + '" aria-label="' + esc('篩選學科：' + d.full + '，' + d.count + ' 篇') + '"><span class="halo"></span>' +
        shapeSvg(d.shape, d.color, mobile ? 13 : 16, mobile ? 0.9 : 0.7) + (mobile ? '' : '<span class="hc" style="box-shadow:0 0 5px 1px ' + d.color + '"></span>') +
        '</button><span class="hublbl lbl r" data-hub="' + d.key + '" aria-hidden="true">' + lab + '</span>');
      w.dataset.k = d.key;
      var b = w.querySelector('button');
      if (!mobile) hoverable(b, function () { setHoverD(d.key); }, function () { setHoverD(null); });
      addNode(w, d.hub[0], d.hub[1], w.querySelector('.hublbl'), 1, 'r');
    });
    var fr = rndFrom(1263);
    paperOrder.forEach(function (p) {
      var aw = !!p.award;
      var w = mk('<button type="button" class="star p" data-p="' + p.slug + '" aria-label="' + esc(p.name + '，' + p.years) + '" style="animation-delay:' + (-fr() * 9).toFixed(2) + 's;animation-duration:' + (7 + fr() * 5).toFixed(2) + 's">' +
        (aw ? '<span class="ring" aria-hidden="true" style="border:1px dashed rgba(244,241,234,.55)"></span>' : '') + '<span class="core" aria-hidden="true"></span></button>' +
        (mobile ? '<span class="lbl plbl r" aria-hidden="true">' + esc(p.name) + '</span>' : ''));
      w.dataset.p = p.slug;
      if (!mobile) hoverable(w.querySelector('button'), function () { setHover(p.slug); }, scheduleHoverClear);
      addNode(w, p.x, p.y, w.querySelector('.lbl'), 2);
    });
    /* 概念頁菱形：名稱預設隱藏，滑過、聚焦或點選菱形，或選中／滑過之論文屬於該概念時才顯示（DESIGN.md 第二章第 2 節）。
       排在星點之後，鍵盤先經過學科與星點；名稱另以 aria-label 提供給螢幕閱讀器。 */
    D.concepts.forEach(function (c) {
      var w = mk('<button type="button" class="cptb" data-cpt="' + c.slug + '" aria-pressed="false" aria-label="' + esc('概念頁：' + c.name + '，' + c.papers.length + ' 篇論文') + '"' + (mobile ? ' tabindex="-1"' : '') + '><span class="cpt" aria-hidden="true"></span></button>' +
        '<span class="lbl cptlbl r" aria-hidden="true">' + esc(c.name) + '</span>');
      w.dataset.c = c.slug;
      if (!mobile) hoverable(w.querySelector('button'), function () { setHoverC(c.slug); }, function () { setHoverC(null); });
      addNode(w, c.x, c.y, w.querySelector('.lbl'), 4, c.x >= 500 ? 'r' : 'l');
    });
    if (!mobile) addTip();
  }

  function starsState() {
    var z = S.filter, fx = mobile ? z : (S.hoverD || z);
    var focusSlug = mobile ? S.sel : (S.hover || (S.note ? null : S.sel)), sel = focusSlug ? byP[focusSlug] : null;
    var selTags = {}, selDom = {};
    if (sel) sel.tags.forEach(function (t) { selTags[t] = 1; selDom[D.tags[t].d] = 1; });
    var inF = function (k) { return !fx || fx === k; };
    map.dataset.zoom = (mobile && z) ? z : 'none';
    map.querySelectorAll('.nebs circle').forEach(function (c) { c.style.opacity = inF(c.dataset.k) ? 1 : 0.25; });
    nodes.forEach(function (n) {
      var el = n.el, ds = el.dataset;
      if (ds.k) {
        var d = DOM[ds.k], pressed = z === ds.k, ha = (pressed || S.hoverD === ds.k) ? 0.5 : 0.3;
        el.style.opacity = inF(ds.k) ? (d.count || pressed ? 1 : 0.62) : 0.3;
        el.querySelector('button').setAttribute('aria-pressed', pressed ? 'true' : 'false');
        el.querySelector('.halo').style.background = 'radial-gradient(closest-side,rgba(' + d.rgb + ',' + ha + '),rgba(' + d.rgb + ',' + (ha * 0.3).toFixed(3) + ') 45%,rgba(' + d.rgb + ',0) 100%)';
      } else if (ds.t) {
        var tg = D.tags[ds.t], lit = !!selTags[ds.t];
        el.style.opacity = lit ? 1 : (inF(tg.d) ? 0.85 : 0.18);
        n.lab.style.color = lit ? 'var(--fg-ivory)' : 'var(--muted)';
        n.show = mobile ? (lit || z === tg.d) : true;
      } else if (ds.p) {
        var p = byP[ds.p], dp = DOM[p.d], isSel = !!(sel && sel.slug === p.slug);
        var act = !fx || paperIn(p, fx);
        var core = el.querySelector('.core'), sz = isSel ? (mobile ? 8 : 7) : ((mobile && z) ? 6 : (p.award ? 5 : 4));
        core.style.width = core.style.height = sz + 'px';
        core.style.boxShadow = isSel ? '0 0 5px 2px rgba(' + dp.rgb + ',.95),0 0 18px 6px rgba(' + dp.rgb + ',.45)' : '0 0 4px 1px rgba(' + dp.rgb + ',.9),0 0 11px 3px rgba(' + dp.rgb + ',.3)';
        var ring = el.querySelector('.ring');
        if (ring) ring.style.borderColor = p.nobel ? (isSel ? dp.color : 'rgba(244,241,234,.6)') : 'rgba(244,241,234,.28)';
        el.style.opacity = (isSel || act) ? 1 : 0.18;
        el.style.zIndex = isSel ? 5 : 4;
        var b = el.querySelector('button');
        b.setAttribute('aria-pressed', S.sel === p.slug ? 'true' : 'false');
        b.tabIndex = mobile ? (z && act ? 0 : -1) : 0;
        if (n.lab) {
          n.show = !!(isSel || (z && z === p.d));
          n.pri = isSel ? 0 : 2;
          n.lab.classList.toggle('sel', isSel);
          n.lab.style.color = isSel ? 'var(--fg-strong)' : 'var(--body)';
        }
      } else if (ds.c) {
        var c = conceptBy[ds.c], lc = !!(sel && c.papers.indexOf(sel.slug) >= 0);
        var named = lc || S.hoverC === ds.c || S.pinC === ds.c;
        var cact = !fx || c.d === fx || c.papers.some(function (s) { return byP[s].d === fx; });
        if (mobile) el.style.opacity = named ? 1 : (sel ? 0.2 : (z ? 0.3 : 0.6));
        else el.style.opacity = named ? 1 : (cact ? 0.62 : 0.2);
        n.show = named;
        n.must = named && !mobile; /* 桌面：符合條件者一律顯示；手機沿用避讓，放不下就隱藏 */
        el.querySelector('button').setAttribute('aria-pressed', S.pinC === ds.c ? 'true' : 'false');
      }
    });
    starsEdges(fx, sel, selTags, selDom);
  }

  function starsEdges(fx, sel, selTags, selDom) {
    gid = 0;
    var s = '', inF = function (k) { return !fx || fx === k; };
    D.domains.forEach(function (d) {
      s += edge({ x1: 500, y1: 500, x2: d.hub[0], y2: d.hub[1], c1: IV, c2: d.rgb, a: selDom[d.key] ? 0.55 : (inF(d.key) ? (d.count ? 0.3 : 0.12) : 0.05), fade: 0.7 });
    });
    Object.keys(D.tags).forEach(function (t) {
      var tg = D.tags[t], d = DOM[tg.d], lit = !!selTags[t];
      s += edge({ x1: d.hub[0], y1: d.hub[1], x2: tg.x, y2: tg.y, c1: d.rgb, c2: d.rgb, a: lit ? 0.9 : (inF(tg.d) ? 0.55 : 0.08), fade: 0.35, w: lit ? 1.7 : 1.1, flow: lit });
    });
    D.papers.forEach(function (p) {
      p.tags.forEach(function (t) {
        var tg = D.tags[t], lit = !!(sel && sel.slug === p.slug);
        s += edge({ x1: tg.x, y1: tg.y, x2: p.x, y2: p.y, c1: DOM[tg.d].rgb, c2: IV, a: lit ? 0.95 : ((inF(tg.d) || inF(p.d)) ? 0.42 : 0.06), fade: 0.25, w: lit ? 1.7 : 1.1, flow: lit });
      });
    });
    D.concepts.forEach(function (c) {
      c.papers.forEach(function (slug) {
        var p = byP[slug], lit = !!(sel && sel.slug === slug);
        if (lit) s += edge({ x1: c.x, y1: c.y, x2: p.x, y2: p.y, c1: IV, c2: IV, a: 0.7, fade: 0.4, dash: '2 5' });
        else if (!mobile) s += edge({ x1: c.x, y1: c.y, x2: p.x, y2: p.y, c1: IV, c2: IV, a: (inF(p.d) || inF(c.d)) ? 0.1 : 0.03, fade: 0.5, dash: '1 6' });
      });
    });
    map.querySelector('.edges').innerHTML = s;
  }

  /* ---------- 我的星系星圖（桌面依樣稿 v5，手機依原型 v2） ---------- */
  function buildFocus() {
    var G = mobile ? FO.mob : FO.desk, pk = mobile ? 'mob' : 'desk';
    stage = { w: G.w, h: G.h };
    setAR(G.w / G.h);
    nodes = [];
    var ny = mobile ? Math.round(G.h * 0.52) : 600, nr = mobile ? 420 : 300;
    var h = '<svg class="bg" viewBox="0 0 ' + G.w + ' ' + G.h + '" preserveAspectRatio="none" aria-hidden="true" focusable="false"><defs><radialGradient id="nbf"><stop offset="0" stop-color="rgba(' + BLUE + ',0.11)"/><stop offset="0.5" stop-color="rgba(' + BLUE + ',0.045)"/><stop offset="1" stop-color="rgba(' + BLUE + ',0)"/></radialGradient></defs>';
    h += '<g class="nebs"><circle data-k="F" cx="' + (mobile ? 330 : 310) + '" cy="' + ny + '" r="' + nr + '" fill="url(#nbf)"/><circle data-k="L" cx="' + (mobile ? 670 : 690) + '" cy="' + ny + '" r="' + nr + '" fill="url(#nbf)"/></g>';
    var on = '', off = '';
    G.rows.forEach(function (r) { if (r[2]) on += 'M60 ' + r[1] + ' H960 '; else off += 'M60 ' + r[1] + ' H960 '; });
    h += '<path d="' + on + '" fill="none" stroke="rgba(' + BLUE + ',0.10)" vector-effect="non-scaling-stroke"/>';
    if (off) h += '<path d="' + off + '" fill="none" stroke="rgba(232,228,218,0.05)" stroke-dasharray="1 6" vector-effect="non-scaling-stroke"/>';
    h += '<path d="M60 ' + G.now + ' H960" fill="none" stroke="rgba(' + BLUE + ',0.24)" stroke-dasharray="3 5" vector-effect="non-scaling-stroke"/>';
    var dx1 = mobile ? 345 : 405, dx2 = mobile ? 655 : 595, dy0 = mobile ? 225 : 56;
    h += '<path d="M' + dx1 + ' ' + dy0 + ' V' + (G.now - 54) + ' M' + dx2 + ' ' + dy0 + ' V' + (G.now - 54) + '" fill="none" stroke="rgba(232,228,218,0.05)" stroke-dasharray="1 4" vector-effect="non-scaling-stroke"/><g class="edges"></g></svg>';
    map.innerHTML = h;

    G.rows.forEach(function (r) { addNode(mk('<span class="lbl yr" aria-hidden="true" style="opacity:' + (r[2] ? 1 : 0.45) + '">' + r[0] + '</span>'), 12, r[1]); });
    addNode(mk('<span class="lbl yr" aria-hidden="true" style="color:var(--blue)">NOW</span>'), 12, G.now);
    FO.cols.forEach(function (c) {
      var w = mk('<span class="lbl colh" aria-hidden="true">' + esc(c.label) + '<b>' + c.count + '</b></span>');
      w.dataset.col = c.key;
      addNode(w, G.colX[c.key], G.colY);
    });
    FO.hubs.forEach(function (hb) {
      var w = mk('<button type="button" class="hub" data-fhub="' + hb.key + '" aria-label="' + esc('篩選概念：' + hb.full + '，' + hb.count + ' 篇') + '"><span class="halo"></span>' +
        shapeSvg(DIAMOND2, '#EAE6DF', mobile ? 14 : 16, 0.8) + (mobile ? '' : '<span class="hc" style="box-shadow:0 0 5px 1px ' + BLUE_C + '"></span>') + '</button>' +
        '<span class="hublbl lbl ' + (mobile ? 'dn' : 'vt') + '" data-fhub="' + hb.key + '" aria-hidden="true">' + esc(hb.name) + '<b>' + hb.count + '</b></span>');
      w.dataset.fk = hb.key;
      if (!mobile) hoverable(w.querySelector('button'), function () { setHoverD('con:' + hb.key); }, function () { setHoverD(null); });
      addNode(w, hb[pk][0], hb[pk][1]);
    });
    var th = mk('<button type="button" class="star thesis" data-thesis="1" aria-label="' + esc(FO.thesis.name + '，' + FO.thesis.status) + '"><span class="ring" aria-hidden="true" style="border:1px dashed rgba(' + BLUE + ',.85)"></span><span class="core" aria-hidden="true" style="width:4px;height:4px"></span></button>' +
      '<span class="lbl r" aria-hidden="true" style="left:20px"><span style="font-family:var(--font-serif-zh);font-size:' + (mobile ? 13 : 14) + 'px;letter-spacing:.08em">' + esc(FO.thesis.name) + '</span><br><span style="font-family:var(--font-mono);font-size:9px;letter-spacing:.2em;color:var(--blue)">' + esc(FO.thesis.statusEn) + '</span></span>');
    th.dataset.th = '1';
    if (!mobile) hoverable(th.querySelector('button'), function () { setHover(TH); }, scheduleHoverClear);
    addNode(th, G.thesisAt[0], G.thesisAt[1]);
    var fr = rndFrom(2026);
    FO.papers.forEach(function (p) {
      var w = mk('<button type="button" class="star p f" data-f="' + p.slug + '" aria-label="' + esc(p.name + '，' + p.year + ' 發表，' + roleName[p.role]) + '" style="animation-delay:' + (-fr() * 9).toFixed(2) + 's;animation-duration:' + (7 + fr() * 5).toFixed(2) + 's"><span class="core" aria-hidden="true"></span></button>' +
        (mobile ? '<span class="lbl plbl r" aria-hidden="true">' + esc(p.name) + '</span>' : ''));
      w.dataset.f = p.slug;
      if (!mobile) hoverable(w.querySelector('button'), function () { setHover(p.slug); }, scheduleHoverClear);
      addNode(w, p[pk][0], p[pk][1], w.querySelector('.lbl'), 0);
    });
    if (!mobile) addTip();
  }

  function focusState() {
    var ff = mobile ? S.ffilter : (S.hoverD || S.ffilter), focusSlug = mobile ? S.fsel : (S.hover || S.fsel);
    var sel = focusSlug && focusSlug !== TH ? byF[focusSlug] : null, thSel = focusSlug === TH, isRoleF = ff.indexOf('role:') === 0;
    var conOn = function (k) { return ff === 'all' || isRoleF || ff === 'con:' + k; };
    map.dataset.zoom = 'focus';
    map.querySelectorAll('.nebs circle').forEach(function (c) { c.style.opacity = conOn(c.dataset.k) ? 1 : 0.3; });
    nodes.forEach(function (n) {
      var el = n.el, ds = el.dataset;
      if (ds.f) {
        var p = byF[ds.f], rgb = fRgb(p), isSel = !!(sel && sel.slug === p.slug), core = el.querySelector('.core'), sz = isSel ? 14 : (mobile ? 10 : 9);
        core.style.width = core.style.height = sz + 'px';
        core.style.background = 'radial-gradient(circle,#FFFDF8 0 ' + (isSel ? 1.8 : 1.2) + 'px,rgba(255,253,248,0) ' + (isSel ? 2.4 : 1.7) + 'px)';
        core.style.boxShadow = isSel ? 'inset 0 0 0 1.2px #EAF6FF,0 0 8px 2px rgba(' + rgb + ',.7),0 0 20px 6px rgba(' + rgb + ',.3)' : 'inset 0 0 0 1px rgba(' + rgb + ',.95),0 0 6px 1px rgba(' + rgb + ',.4)';
        el.style.opacity = (isSel || fMatch(p, ff)) ? 1 : 0.18;
        el.style.zIndex = isSel ? 5 : 4;
        el.querySelector('button').setAttribute('aria-pressed', S.fsel === p.slug ? 'true' : 'false');
        if (n.lab) { n.show = isSel; n.lab.classList.toggle('sel', isSel); }
      } else if (ds.fk) {
        var pressed = S.ffilter === 'con:' + ds.fk, ha = (pressed || S.hoverD === 'con:' + ds.fk) ? 0.5 : 0.3;
        el.style.opacity = conOn(ds.fk) ? 1 : 0.35;
        el.querySelector('button').setAttribute('aria-pressed', pressed ? 'true' : 'false');
        el.querySelector('.halo').style.background = 'radial-gradient(closest-side,rgba(' + BLUE + ',' + ha + '),rgba(' + BLUE + ',' + (ha * 0.3).toFixed(3) + ') 45%,rgba(' + BLUE + ',0) 100%)';
      } else if (ds.col) {
        el.style.opacity = (ds.col === 'F' && ff === 'con:L') || (ds.col === 'L' && ff === 'con:F') ? 0.35 : 1;
      } else if (ds.th) {
        var tc = el.querySelector('.core'), tr = el.querySelector('.ring');
        tc.style.boxShadow = thSel ? '0 0 8px 3px rgba(' + BLUE + ',.85),0 0 22px 8px rgba(' + BLUE + ',.3)' : '0 0 8px 2px rgba(' + BLUE + ',.7)';
        tr.style.borderColor = thSel ? 'rgba(' + BLUE + ',1)' : 'rgba(' + BLUE + ',.7)';
        /* 桌面選中碩論時由說明框顯示名稱與狀態，星旁名稱暫時收起以免重複 */
        el.querySelector('.lbl').style.opacity = thSel && !mobile ? 0 : 1;
        el.querySelector('button').setAttribute('aria-pressed', S.fsel === TH ? 'true' : 'false');
      }
    });
    gid = 0;
    var s = '', G = mobile ? FO.mob : FO.desk, pk = mobile ? 'mob' : 'desk';
    FO.hubs.forEach(function (hb) {
      s += edge({ x1: hb[pk][0], y1: hb[pk][1], x2: G.thesisAt[0], y2: G.thesisAt[1], c1: BLUE, c2: IV, a: thSel ? 0.6 : (sel && sel.con.indexOf(hb.key) >= 0 ? 0.42 : (conOn(hb.key) ? 0.26 : 0.05)), fade: 0.9, w: thSel ? 1.6 : 1.1 }); /* 碩論連線選中時只轉亮、不流光（2026-11-09 使用者決定） */
    });
    FO.papers.forEach(function (p) {
      p.con.forEach(function (k) {
        var hb = hubOf(k), lit = !!(sel && sel.slug === p.slug), on2 = fMatch(p, ff) && (ff.indexOf('con:') !== 0 || ff === 'con:' + k);
        s += edge({ x1: hb[pk][0], y1: hb[pk][1], x2: p[pk][0], y2: p[pk][1], c1: fRgb(p), c2: IV, a: lit ? 0.95 : (on2 ? 0.22 : 0.04), fade: 0.35, w: lit ? 1.7 : 1, flow: lit });
      });
    });
    map.querySelector('.edges').innerHTML = s;
  }

  /* ---------- 桌面說明框：名稱、雙年份、card_line、DOI（論文頁上線前不放論文頁連結） ---------- */
  function addTip() {
    tip = document.createElement('div');
    tip.className = 'tip';
    tip.hidden = true;
    tip.innerHTML = '<span class="tip-nm"></span><span class="tip-yr"></span><span class="tip-mt"></span><span class="tip-ln"></span><a class="tip-doi" target="_blank" rel="noopener"></a>';
    map.appendChild(tip);
    tipEls = { nm: tip.children[0], yr: tip.children[1], mt: tip.children[2], ln: tip.children[3], doi: tip.children[4] };
    tip.addEventListener('pointerenter', function () { clearTimeout(hoverTimer); });
    tip.addEventListener('pointerleave', scheduleHoverClear);
  }
  function nodeOf(attr, val) { return nodes.filter(function (n) { return n.el.dataset[attr] === val; })[0]; }
  function renderTip() {
    if (mobile || !tip) return;
    var t = null, anchor = null;
    if (S.mode === 'stars') {
      var slug = S.hover || (S.note ? null : S.sel);
      if (slug && byP[slug]) {
        var p = byP[slug], d = DOM[p.d];
        t = { nm: p.name, yr: p.years, mt: '', ln: p.cardLine, doi: p.doi, rgb: d.rgb, col: d.color };
        anchor = nodeOf('p', slug);
      } else if (S.note) {
        var dn = DOM[S.note];
        t = { nm: dn.full, yr: '0 篇', mt: '', ln: '這個學科還沒有已收錄的論文。', doi: '', rgb: dn.rgb, col: dn.color };
        anchor = nodeOf('k', S.note);
      }
    } else {
      var fs = S.hover || S.fsel;
      if (fs === TH) {
        t = { nm: FO.thesis.name, yr: FO.thesis.status, mt: '', ln: '', doi: '', rgb: BLUE, col: BLUE_C };
        anchor = nodeOf('th', '1');
      } else if (fs && byF[fs]) {
        var f = byF[fs];
        t = { nm: f.name, yr: f.years, mt: roleName[f.role] + '・' + f.langText, ln: f.cardLine, doi: f.doi, rgb: fRgb(f), col: fCol(f) };
        anchor = nodeOf('f', fs);
      }
    }
    if (!t || !anchor) { tip.hidden = true; return; }
    tipEls.nm.textContent = t.nm;
    tipEls.yr.textContent = t.yr;
    tipEls.mt.textContent = t.mt;
    tipEls.mt.hidden = !t.mt;
    tipEls.ln.textContent = t.ln;
    tipEls.ln.hidden = !t.ln;
    if (t.doi) {
      tipEls.doi.hidden = false;
      tipEls.doi.href = t.doi;
      tipEls.doi.textContent = t.doi.replace(/^https?:\/\//, '');
      tipEls.doi.setAttribute('aria-label', '原文 DOI：' + t.nm + '（另開新分頁）');
    } else tipEls.doi.hidden = true;
    tip.style.setProperty('--tb', 'rgba(' + t.rgb + ',.35)');
    tip.style.setProperty('--tc', t.col);
    tip.hidden = false;
    positionTip(anchor);
  }
  /* 在星點周圍格狀搜尋：不出界、不蓋住星點，並盡量避開學科與概念名稱（權重高）、標籤與其他星點；同分取離星點近者 */
  function positionTip(n) {
    var mr = map.getBoundingClientRect(), pr = panel.getBoundingClientRect(), ar = n.el.getBoundingClientRect();
    var sx = ar.left, sy = ar.top, tw = tip.offsetWidth, th = tip.offsetHeight, gap = 16, step = 10;
    var obs = labelRects.slice();
    nodes.forEach(function (m) {
      if (m === n || !(m.el.dataset.p || m.el.dataset.f || m.el.dataset.th || m.el.dataset.k || m.el.dataset.fk)) return;
      var r = m.el.getBoundingClientRect();
      obs.push({ left: r.left - 9, right: r.left + 9, top: r.top - 9, bottom: r.top + 9, w: m.el.dataset.k || m.el.dataset.fk ? 6 : 3 });
    });
    var x0 = Math.max(pr.left + 8, sx - tw - 140), x1 = Math.min(pr.right - 8 - tw, sx + 140);
    var y0 = Math.max(pr.top + 38, sy - th - 110), y1 = Math.min(pr.bottom - 30 - th, sy + 110);
    var best = null;
    for (var L = x0; L <= x1; L += step) {
      for (var T = y0; T <= y1; T += step) {
        var R = L + tw, B = T + th;
        var dx = sx < L ? L - sx : (sx > R ? sx - R : 0), dy = sy < T ? T - sy : (sy > B ? sy - B : 0), dist = Math.max(dx, dy);
        if (dist < gap) continue;
        var ov = 0;
        for (var i = 0; i < obs.length; i++) {
          var q = obs[i], w = Math.min(R, q.right + 4) - Math.max(L, q.left - 4), h = Math.min(B, q.bottom + 2) - Math.max(T, q.top - 2);
          if (w > 0 && h > 0) ov += w * h * (q.w || 2);
        }
        var score = ov + (dist - gap) * 24 + (dx ? 0 : 60);
        if (!best || score < best.s) best = { s: score, x: L, y: T };
      }
    }
    if (!best) best = { x: sx + gap, y: sy - th / 2 };
    tip.style.transform = 'translate(' + Math.round(best.x - mr.left) + 'px,' + Math.round(best.y - mr.top) + 'px)';
  }

  /* ---------- 懸星索引（桌面）與篩選列（手機） ---------- */
  function buildIndex() {
    var h = '';
    if (S.mode === 'stars') {
      domainOrder.forEach(function (d) {
        h += '<button type="button" class="strand" data-strand="' + d.key + '" aria-label="' + esc('篩選學科：' + d.full + '，' + d.count + ' 篇') + '"><span class="str" aria-hidden="true"><span class="ln top"></span>';
        D.papers.filter(function (p) { return p.d === d.key; }).forEach(function (p) { h += '<span class="bd" data-b="' + p.slug + '"></span><span class="ln"></span>'; });
        h += shapeSvg(d.shape, d.color, 13, 1) + '<span class="ct" style="color:' + d.color + '">' + d.count + '</span><span class="ix">' + d.idx + '</span></span><span class="nm" aria-hidden="true" style="color:' + d.color + '">' + esc(d.full) + '</span></button>';
      });
    } else {
      FO.roles.forEach(function (r, i) {
        var mine = FO.papers.filter(function (p) { return p.role === r[0]; });
        h += '<button type="button" class="strand" data-strand="role:' + r[0] + '" aria-label="' + esc('篩選類別：' + r[1] + '，' + mine.length + ' 篇') + '"><span class="str" aria-hidden="true"><span class="ln top"></span>';
        mine.forEach(function (p) { h += '<span class="bd" data-b="' + p.slug + '"></span><span class="ln"></span>'; });
        h += shapeSvg(RING, BLUE_C, 13, 1) + '<span class="ct" style="color:' + BLUE_C + '">' + mine.length + '</span><span class="ix">' + ('0' + (i + 1)) + '</span></span><span class="nm" aria-hidden="true" style="color:' + BLUE_C + '">' + esc(r[1]) + '</span></button>';
      });
    }
    var box = $('strands');
    box.innerHTML = h;
    box.querySelectorAll('.strand').forEach(function (b) {
      hoverable(b, function () { setHoverD(b.dataset.strand); }, function () { setHoverD(null); });
    });
    $('allCount').textContent = S.mode === 'stars' ? D.papers.length : FO.papers.length;
  }
  function updateIndex() {
    var stars = S.mode === 'stars';
    var fx = stars ? (S.hoverD || S.filter) : (S.hoverD || S.ffilter);
    var focusSlug = stars ? (S.hover || (S.note && !mobile ? null : S.sel)) : (S.hover || S.fsel);
    $('allBtn').setAttribute('aria-pressed', stars ? String(!S.filter) : String(S.ffilter === 'all'));
    $('allBtn').setAttribute('aria-label', stars ? '顯示全部學科' : '顯示全部我的關注');
    $('strands').querySelectorAll('.strand').forEach(function (b) {
      var key = b.dataset.strand, rgb, on, pressed, active, empty = false;
      if (stars) {
        var d = DOM[key];
        rgb = d.rgb; pressed = S.filter === key; active = !fx || fx === key; empty = !d.count;
        b.style.opacity = active ? (empty && !pressed ? 0.62 : 1) : 0.38;
      } else {
        rgb = BLUE; pressed = S.ffilter === key;
        var mine = FO.papers.filter(function (p) { return 'role:' + p.role === key; });
        active = fx === 'all' || fx === key || (fx.indexOf('con:') === 0 && mine.some(function (p) { return fMatch(p, fx); }));
        b.style.opacity = active ? 1 : 0.38;
      }
      on = pressed || S.hoverD === key;
      b.setAttribute('aria-pressed', pressed ? 'true' : 'false');
      b.style.setProperty('--sl', 'rgba(' + rgb + ',' + (pressed ? 0.95 : (stars ? 0.6 : 0.5)) + ')');
      b.querySelector('svg').style.filter = on ? 'drop-shadow(0 0 4px rgba(' + rgb + ',.95))' : 'drop-shadow(0 0 2px rgba(' + rgb + ',.5))';
      b.querySelectorAll('.bd').forEach(function (bd) {
        var slug = bd.dataset.b, isSel = slug === focusSlug, sz, sh, bg = '#FFFDF8';
        if (stars) {
          var p = byP[slug], dd = DOM[p.d];
          sz = isSel ? 7 : (p.nobel ? 6 : 5);
          sh = isSel ? '0 0 0 2px var(--ink),0 0 0 3px ' + dd.color + ',0 0 10px 3px rgba(' + dd.rgb + ',.7)'
            : (p.nobel ? '0 0 0 2px var(--ink),0 0 0 2.8px rgba(244,241,234,.55),0 0 6px 2px rgba(' + dd.rgb + ',.45)' : '0 0 4px 1px rgba(' + dd.rgb + ',.6)');
        } else {
          var f = byF[slug], fr = fRgb(f);
          sz = isSel ? 9 : 7;
          bg = 'radial-gradient(circle,#FFFDF8 0 1px,rgba(255,253,248,0) 1.5px)';
          sh = isSel ? 'inset 0 0 0 1px #D2EEFF,0 0 8px 2px rgba(' + fr + ',.7)' : 'inset 0 0 0 1px rgba(' + fr + ',.85),0 0 4px 1px rgba(' + fr + ',.35)';
        }
        bd.style.width = bd.style.height = sz + 'px';
        bd.style.background = bg;
        bd.style.boxShadow = sh;
      });
    });
  }
  function chipHtml(key, label, count, color, rgb, empty, shape) {
    return '<button type="button" class="chip" data-chip="' + key + '" aria-pressed="false"' + (empty ? ' data-empty="true"' : '') + ' style="--c:' + color + ';--rgb:' + rgb + '">' + (shape ? shapeSvg(shape, color, 11, 1.1) : '') + esc(label) + ' <b>' + count + '</b></button>';
  }
  function buildChips() {
    var h = '';
    if (S.mode === 'stars') {
      h += chipHtml('all', '全部', D.papers.length, '#EAE6DF', '232,228,218', false);
      domainOrder.forEach(function (d) { h += chipHtml(d.key, d.name, d.count, d.color, d.rgb, !d.count, d.shape); });
    } else {
      h += chipHtml('all', '全部', FO.papers.length, '#EAE6DF', '232,228,218', false);
      FO.roles.forEach(function (r) {
        h += chipHtml('role:' + r[0], r[1], FO.papers.filter(function (p) { return p.role === r[0]; }).length, BLUE_C, BLUE, false, RING);
      });
    }
    $('chips').innerHTML = h;
    $('chips').setAttribute('aria-label', S.mode === 'stars' ? '學科篩選' : '依角色篩選');
  }
  function updateChips() {
    $('chips').querySelectorAll('.chip').forEach(function (c) {
      var k = c.dataset.chip, pressed = S.mode === 'stars' ? (k === 'all' ? !S.filter : S.filter === k || S.note === k) : S.ffilter === k;
      c.setAttribute('aria-pressed', pressed ? 'true' : 'false');
    });
  }

  /* ---------- 手機說明框 ---------- */
  function renderInfo() {
    if (!mobile) return;
    var el = $('info'), h = '', rgb = '232,228,218';
    if (S.mode === 'stars') {
      var sel = S.sel ? byP[S.sel] : null;
      if (sel) {
        var d = DOM[sel.d];
        rgb = d.rgb;
        h += '<div class="ihd">' + shapeSvg(d.shape, d.color, 10, 1.2) + '<span class="mono" style="color:' + d.color + '">' + esc(sel.years) + '</span></div>';
        h += '<span class="nm">' + esc(sel.name) + '</span><span class="ln">' + esc(sel.cardLine) + '</span><span class="meta">' + esc(d.full + '・' + sel.tags.join(' ')) + '</span>';
        h += '<div class="foot"><span class="meta">已收錄 Wiki</span>' + (sel.doi ? '<a class="go" href="' + esc(sel.doi) + '" target="_blank" rel="noopener" aria-label="' + esc('原文 DOI：' + sel.name + '（另開新分頁）') + '">DOI 原文</a>' : '') + '</div>';
      } else if (S.note) {
        var dn = DOM[S.note];
        rgb = dn.rgb;
        h += '<div class="ihd">' + shapeSvg(dn.shape, dn.color, 10, 1.2) + '<span class="mono" style="color:' + dn.color + '">' + esc(dn.full) + '</span></div><span class="tipx">這個學科還沒有已收錄的論文。</span>';
      } else if (S.filter) {
        var dz = DOM[S.filter];
        rgb = dz.rgb;
        h += '<div class="ihd">' + shapeSvg(dz.shape, dz.color, 10, 1.2) + '<span class="mono" style="color:' + dz.color + '">' + esc(dz.full + ' ・ ' + dz.count + ' 篇') + '</span></div><span class="tipx">點星看詳情。點「← 全圖」或再點一次學科回到全圖。</span>';
      } else {
        h += '<span class="tipx">點學科放大那一區，再點星點查看論文。</span><span class="meta">' + esc(starStats()) + '</span>';
      }
    } else {
      var f = S.fsel && S.fsel !== TH ? byF[S.fsel] : null;
      rgb = BLUE;
      if (f) {
        rgb = fRgb(f);
        var cl = f.con.length > 1 ? FO.hubs.map(function (x) { return x.name; }).join(' × ') : (f.con.length ? hubOf(f.con[0]).full : '');
        h += '<span class="mono" style="color:' + fCol(f) + '">' + esc(roleName[f.role] + ' ｜ ' + f.years) + '</span><span class="nm">' + esc(f.name) + '</span><span class="ln">' + esc(f.cardLine) + '</span>';
        h += '<span class="meta">' + esc(f.langText) + '<br>' + esc(cl) + '</span>';
        h += '<div class="foot"><span class="meta">我的關注</span>' + (f.doi ? '<a class="go" href="' + esc(f.doi) + '" target="_blank" rel="noopener" aria-label="' + esc('原文 DOI：' + f.name + '（另開新分頁）') + '">DOI 原文</a>' : '') + '</div>';
      } else {
        h += '<span class="nm">' + esc(FO.thesis.name) + '</span><span class="meta">' + esc(FO.thesis.status) + '</span>';
      }
    }
    el.style.setProperty('--rgb', rgb);
    el.innerHTML = h;
  }
  function starStats() { return D.papers.length + ' 顆星・' + Object.keys(D.tags).length + ' 個標籤・' + D.concepts.length + ' 個概念・' + linkCount + ' 條連線'; }

  /* ---------- 模式文字、圖例與返回 ---------- */
  function modeTexts() {
    var f = S.mode === 'focus';
    document.querySelectorAll('.tf0').forEach(function (s) { s.setAttribute('stop-color', f ? 'rgba(' + BLUE + ',0.85)' : 'rgba(234,230,223,0.6)'); });
    document.querySelectorAll('.tagline').forEach(function (s) { s.textContent = f ? 'A PERSONAL CONSTELLATION' : 'THE KAIROS OF HUMAN THOUGHT'; });
    $('mapLabel').textContent = f ? 'MY CONSTELLATION ｜ 我的星系' : 'CONSTELLATION ｜ 知識星圖';
    $('indexLabel').textContent = f ? 'INDEX ｜ MY FOCUS' : 'INDEX';
    $('index').setAttribute('aria-label', f ? '我的星系索引' : '學科索引');
    var leg = '';
    if (f) {
      leg = '<span><span class="lg-dot" style="width:9px;height:9px;background:radial-gradient(circle,#FFFDF8 0 1.2px,rgba(255,253,248,0) 1.7px);box-shadow:inset 0 0 0 1px rgba(' + BLUE + ',.95)"></span>我的關注</span>' +
        '<span>' + shapeSvg(DIAMOND2, '#EAE6DF', 9, 1) + '概念頁</span>' +
        '<span><span class="lg-dot" style="width:10px;height:10px;background:none;border:1px dashed rgba(' + BLUE + ',.85)"></span>' + esc(FO.thesis.name) + '</span>' +
        '<span>列＝發表年　欄＝所屬概念</span>';
      $('stats').textContent = FO.papers.length + ' 顆星・' + FO.hubs.length + ' 個概念・' + fLinkCount + ' 條連線';
    } else {
      leg = '<span><span style="display:inline-flex;gap:3px">' + D.domains.map(function (d) { return shapeSvg(d.shape, d.color, 8, 1.2); }).join('') + '</span>學科</span>' +
        '<span><span class="lg-dot" style="width:3px;height:3px;box-shadow:0 0 4px 1px rgba(' + DOM.bio.rgb + ',.8)"></span>標籤</span>' +
        '<span><span class="lg-dot" style="width:4px;height:4px;box-shadow:0 0 4px 1px rgba(' + BLUE + ',.9)"></span>論文</span>' +
        '<span><span style="width:10px;height:10px;border-radius:50%;border:1px dashed rgba(244,241,234,.6);display:inline-flex;align-items:center;justify-content:center"><span class="lg-dot" style="width:3px;height:3px"></span></span>諾貝爾獎</span>' +
        '<span><span style="width:6px;height:6px;border:1px solid #EAE6DF;transform:rotate(45deg)"></span>概念頁</span>';
      $('stats').textContent = starStats();
    }
    $('legend').innerHTML = leg;
    document.querySelectorAll('[data-secret]').forEach(function (b) { b.setAttribute('aria-label', f ? '回到群星' : '進入我的星系：個人研究關注 ' + FO.papers.length + ' 篇'); });
  }
  function updateBack() {
    var b = $('back'), f = S.mode === 'focus';
    if (f) { b.hidden = false; b.innerHTML = mobile ? '← 回到群星' : '<span class="bstar" aria-hidden="true"></span>回到群星'; }
    else if (mobile && S.filter) { b.hidden = false; b.textContent = '← 全圖'; }
    else b.hidden = true;
  }

  /* ---------- 狀態更新 ---------- */
  function paint() {
    if (S.mode === 'focus') focusState(); else starsState();
    updateIndex();
    updateChips();
    renderInfo();
    updateBack();
  }
  function refresh() { paint(); if (!tween) layoutLabels(); }
  function refreshHover() { paint(); if (!tween && cSig() !== lastCSig) layoutLabels(); else renderTip(); }
  function setHover(slug) { clearTimeout(hoverTimer); if (S.hover === slug) return; S.hover = slug; refreshHover(); }
  function scheduleHoverClear() { clearTimeout(hoverTimer); hoverTimer = setTimeout(function () { if (S.hover !== null) { S.hover = null; refreshHover(); } }, 220); }
  function setHoverD(k) { if (S.hoverD === k) return; S.hoverD = k; refreshHover(); }
  function setHoverC(k) { if (S.hoverC === k) return; S.hoverC = k; refreshHover(); }
  function togglePinC(k) { S.pinC = S.pinC === k ? null : k; refresh(); }
  function announce() {
    if (mobile) return;
    var t = '';
    if (S.mode === 'stars') {
      if (S.note) t = DOM[S.note].full + '：這個學科還沒有已收錄的論文。';
      else if (S.sel) t = '已選取：' + byP[S.sel].name + '，' + byP[S.sel].years;
      if (S.filter && !S.note) t = '篩選：' + DOM[S.filter].full + '。' + t;
    } else {
      t = S.fsel === TH ? '已選取：' + FO.thesis.name + '，' + FO.thesis.status : '已選取：' + byF[S.fsel].name + '，' + byF[S.fsel].years;
    }
    $('live').textContent = t;
  }

  function rebuild() {
    if (tween) { cancelAnimationFrame(tween.raf); tween = null; }
    map.classList.toggle('desk', !mobile);
    tip = null;
    if (S.mode === 'focus') buildFocus(); else buildStars();
    view = (mobile && S.mode === 'stars' && S.filter) ? domainView(S.filter) : fullView();
    built = S.mode + (mobile ? ':m' : ':d');
    place();
    refresh();
  }
  function setMode(m, animate) {
    S.mode = m;
    document.body.dataset.mode = m;
    S.hover = null;
    S.hoverD = null;
    S.hoverC = null;
    S.pinC = null;
    setArmed(false);
    modeTexts();
    buildIndex();
    buildChips();
    rebuild();
    if (animate && !reduce) { map.classList.remove('warp'); void map.offsetWidth; map.classList.add('warp'); }
  }

  /* 篩選學科：桌面為淡化其他學科，手機為放大該區 */
  function pickDomain(k) {
    var d = k ? DOM[k] : null;
    S.hoverD = null;
    if (mobile) {
      S.note = null;
      if (d && !d.count) { S.filter = null; S.note = k; S.sel = null; animateTo(fullView()); refresh(); return; }
      if (!k || S.filter === k) { S.filter = null; S.sel = null; animateTo(fullView()); }
      else { S.filter = k; if (S.sel && byP[S.sel].d !== k) S.sel = null; animateTo(domainView(k)); }
      refresh();
      return;
    }
    /* 桌面篩選只淡化其他學科，不代選星點；已選之星若不在該學科內則取消 */
    S.note = null;
    if (!k || S.filter === k) S.filter = null;
    else {
      S.filter = k;
      if (!d.count) S.note = k;
      if (S.sel && !paperIn(byP[S.sel], k)) S.sel = null;
    }
    refresh();
    announce();
  }
  function clearSel() { S.sel = null; S.pinC = null; S.hover = null; refresh(); $('live').textContent = '已取消選取'; }
  function selectPaper(slug) { S.sel = slug; S.note = null; S.hover = null; refresh(); announce(); }
  function selectFocus(slug) { S.fsel = slug; S.hover = null; refresh(); announce(); }
  function setFFilter(k) { S.ffilter = (k === 'all' || S.ffilter === k) ? 'all' : k; S.hoverD = null; refresh(); }

  map.addEventListener('click', function (e) {
    var t = e.target.closest('[data-hub],[data-p],[data-cpt],[data-fhub],[data-f],[data-thesis]');
    if (!t || !map.contains(t)) return;
    if (t.dataset.hub) pickDomain(t.dataset.hub);
    else if (t.dataset.cpt) togglePinC(t.dataset.cpt);
    else if (t.dataset.p) selectPaper(t.dataset.p);
    else if (t.dataset.fhub) setFFilter('con:' + t.dataset.fhub);
    else if (t.dataset.f) selectFocus(t.dataset.f);
    else if (t.dataset.thesis) selectFocus(TH);
  });
  $('strands').addEventListener('click', function (e) {
    var b = e.target.closest('[data-strand]');
    if (!b) return;
    if (S.mode === 'stars') pickDomain(b.dataset.strand); else setFFilter(b.dataset.strand);
  });
  $('allBtn').addEventListener('click', function () { if (S.mode === 'stars') pickDomain(null); else setFFilter('all'); });
  $('chips').addEventListener('click', function (e) {
    var b = e.target.closest('[data-chip]');
    if (!b) return;
    var k = b.dataset.chip;
    if (S.mode === 'stars') pickDomain(k === 'all' ? null : k); else setFFilter(k);
  });
  $('back').addEventListener('click', function () { if (S.mode === 'focus') go(''); else pickDomain(null); });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (S.mode === 'stars' && (S.filter || S.note)) pickDomain(null);
    else if (S.mode === 'stars' && (S.sel || S.pinC)) clearSel();
    else if (S.mode === 'focus' && S.ffilter !== 'all') setFFilter('all');
  });

  /* ---------- 句末之星（隱藏機關） ---------- */
  var lastPointer = 'mouse', armTimer = 0;
  addEventListener('pointerdown', function (e) { lastPointer = e.pointerType || 'mouse'; }, true);
  addEventListener('keydown', function () { lastPointer = 'key'; }, true);
  function setArmed(on) {
    S.armed = on;
    var hint = $('hint');
    document.querySelectorAll('[data-secret]').forEach(function (b) { b.dataset.armed = on ? 'true' : 'false'; });
    clearTimeout(armTimer);
    if (on) {
      hint.textContent = S.mode === 'stars' ? '群星之中，還有一片我的星系・再點一下進入' : '回到群星・再點一下';
      hint.hidden = false;
      armTimer = setTimeout(function () { setArmed(false); }, 6000);
    } else hint.hidden = true;
  }
  document.querySelectorAll('[data-secret]').forEach(function (b) {
    b.addEventListener('click', function () {
      /* 手機版觸控：第一下浮出提示，第二下才進入。桌面版不顯示任何文字，滑鼠、鍵盤與觸控皆一下進入 */
      if (mobile && lastPointer === 'touch' && !S.armed) { setArmed(true); return; }
      setArmed(false);
      go(S.mode === 'stars' ? '#my-constellation' : '');
    });
  });

  /* ---------- 路由：#my-constellation 為我的星系 ---------- */
  function go(hash) {
    if (hash) { if (location.hash !== hash) location.hash = hash; else route(); }
    else { history.pushState(null, '', location.pathname + location.search); route(); }
  }
  function route() {
    var m = (location.hash === '#my-constellation' && FO) ? 'focus' : 'stars';
    if (m !== S.mode || !built) setMode(m, !!built);
  }
  addEventListener('hashchange', route);
  addEventListener('popstate', route);

  /* ---------- 版面切換、尺寸、字型與減少動態 ---------- */
  function onLayout() {
    var was = mobile;
    mobile = mqMobile.matches;
    if (was === mobile) return;
    S.hover = null;
    S.hoverD = null;
    S.hoverC = null;
    if (!mobile && S.note) { S.filter = S.note; }
    if (mobile && S.filter && !DOM[S.filter].count) { S.note = S.filter; S.filter = null; }
    if (mobile && S.sel && S.filter && byP[S.sel].d !== S.filter) S.sel = null;
    rebuild();
  }
  if (mqMobile.addEventListener) mqMobile.addEventListener('change', onLayout); else mqMobile.addListener(onLayout);
  function onReduce() { reduce = mqReduce.matches; startSky(); refresh(); }
  if (mqReduce.addEventListener) mqReduce.addEventListener('change', onReduce); else mqReduce.addListener(onReduce);
  var rz = 0;
  addEventListener('resize', function () {
    if (reduce) drawSky(0);
    cancelAnimationFrame(rz);
    rz = requestAnimationFrame(function () { if (!tween) layoutLabels(); });
  });
  if (window.ResizeObserver) new ResizeObserver(function () { if (!tween) layoutLabels(); }).observe(map);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { if (!tween) layoutLabels(); });

  startSky();
  route();
})();
