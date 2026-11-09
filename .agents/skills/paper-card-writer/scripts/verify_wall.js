// 首頁卡片牆之瀏覽器驗證（paper-card-writer 第五節第 7 步之二；細則見 references/card-wall.md）。
//
// 用法：
//   1. 於倉庫根目錄啟動本機伺服器：python -m http.server 8781 --bind 127.0.0.1 --directory web
//      （不可用 file:// 直接開檔：瀏覽器會擋下讀取 iframe 內容）
//   2. 在瀏覽器開 http://127.0.0.1:8781/index.html ，分頁保持在前景（背景分頁的計時器會被節流）。
//   3. 在 Console 先執行一行，指定自己這篇（批次重建時可省略，省略則只驗全部卡片）：
//        var EK_SLUG = '1982-hopfield-network';
//      再把本檔全部內容貼進 Console 執行（或以代理之瀏覽器 JavaScript 工具執行，兩段放在同一次執行亦可），等待約 25 秒。
//   4. 把輸出的整段文字原樣貼進交付說明。任何一行 FAIL 都不得交付。
//
// 本腳本以隱藏 iframe 量測桌面 1440 x 900 與手機 375 x 812，群星與我的星系兩種模式各一次，不必手動調整視窗。
// 量測項目：卡片張數與頁面資料一致、指定之 slug 在牆上且只有一張、每張卡 3:4、卡片內容未被裁切、
// 封面一句話每行不折行且最多三行、一句話與 card_line 逐字相同、一句話未壓到代表星或語言標籤、
// 論文名與雙年份是否被截斷、欄數、手機最小字級、頁面無橫向捲動、學科（或角色）篩選後只顯示該篩選之卡片、
// 每張卡之連結可開啟。只量版面與一致性，不判斷內容對錯。
(async () => {
  const SLUG = (typeof EK_SLUG === 'string' ? EK_SLUG : '').trim();
  const SIZES = [[1440, 900], [375, 812]];
  const MODES = ['stars', 'focus'];
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const lines = [];
  let fails = 0, warns = 0;
  const out = (ok, tag, msg) => { if (!ok) fails++; lines.push((ok ? 'PASS ' : 'FAIL ') + tag + '  ' + msg); };
  const warn = (tag, msg) => { warns++; lines.push('WARN ' + tag + '  ' + msg); };
  const name = e => (e.className && e.className.baseVal !== undefined ? e.className.baseVal : e.className) || e.tagName;
  // 以文字範圍量行數：flex 項目是區塊，getClientRects() 只回傳一個方框，量不出折行
  const textLines = (d, e) => { const rg = d.createRange(); rg.selectNodeContents(e); return new Set([...rg.getClientRects()].filter(q => q.width > 0).map(q => Math.round(q.top))).size; };
  const base = location.href.split('#')[0].replace(/[^/]*$/, '') + 'index.html';
  const linkOk = {};

  for (const [w, h] of SIZES) {
    for (const mode of MODES) {
      const tag = w + 'x' + h + ' ' + (mode === 'stars' ? '群星' : '我的星系');
      const f = document.createElement('iframe');
      f.style.cssText = 'position:fixed;left:-10000px;top:0;border:0;width:' + w + 'px;height:' + h + 'px';
      f.src = base + (mode === 'focus' ? '#my-constellation' : '');
      document.body.appendChild(f);
      await new Promise(r => { f.onload = r; });
      const d = f.contentDocument, W = f.contentWindow;
      if (d.fonts && d.fonts.ready) await d.fonts.ready;
      await wait(1800);
      const data = JSON.parse(d.getElementById('ek-data').textContent);
      const lineOf = {};
      data.papers.forEach(p => { lineOf[p.slug] = p.cardLine; });
      if (data.focus) data.focus.papers.forEach(p => { lineOf[p.slug] = p.cardLine; });
      const all = [...d.querySelectorAll('#grid .wc')];
      const mine = all.filter(c => c.dataset.set === mode);
      const vis = all.filter(c => !c.hidden && W.getComputedStyle(c).display !== 'none');

      // 1. 張數：未篩選時，顯示的卡片恰為本模式之全部卡片
      out(vis.length === mine.length && vis.every(c => c.dataset.set === mode), tag,
        '顯示 ' + vis.length + ' 張，本模式卡片 ' + mine.length + ' 張' + (vis.some(c => c.dataset.set !== mode) ? '；混入另一模式之卡片' : ''));
      if (mode === 'stars' && w === SIZES[0][0]) lines.push('INFO 卡片牆共 ' + all.length + ' 張：' + all.map(c => c.dataset.slug).join('、'));

      // 2. 指定之 slug
      if (SLUG) {
        const hit = all.filter(c => c.dataset.slug === SLUG);
        if (hit.length !== 1) out(false, tag, EK_SLUG_MSG(hit.length));
        else if (hit[0].dataset.set === mode) out(!hit[0].hidden, tag, SLUG + ' 在牆上（' + hit[0].querySelector('.top span').textContent + '）且未被隱藏');
      }

      // 3. 逐張量測
      const narrow = w <= 860;
      vis.forEach(c => {
        const id = c.dataset.slug, bad = [];
        const cv = c.querySelector('.cv'), cr = cv.getBoundingClientRect();
        const ratio = cr.height / cr.width;
        if (Math.abs(ratio - 4 / 3) > 0.02) bad.push('比例 ' + ratio.toFixed(3) + '（應為 1.333）');
        // 3a. 任何元素不得超出卡片或卡片內會裁切內容的容器（星窗）；.bot、.tag、.ttl 本身以省略號截斷，另於 3d 處理
        [...cv.querySelectorAll('*')].forEach(e => {
          const b = e.getBoundingClientRect();
          if (!(b.width > 0 && b.height > 0)) return;
          for (let a = e.parentElement; a; a = a.parentElement) {
            const cs = W.getComputedStyle(a);
            if (a === cv || ['hidden', 'clip'].includes(cs.overflowX) || ['hidden', 'clip'].includes(cs.overflowY)) {
              const r = a.getBoundingClientRect();
              if (b.right > r.right + 1 || b.bottom > r.bottom + 1 || b.left < r.left - 1 || b.top < r.top - 1) { bad.push(name(e) + ' 超出 ' + name(a)); break; }
            }
            if (a === cv) break;
          }
        });
        // 3b. 封面一句話：每行不折行、最多三行、與 card_line 逐字相同、未壓到代表星或語言標籤
        const win = cv.querySelector('.win'), wl = cv.querySelector('.wl');
        const ls = wl ? [...wl.children] : [];
        if (!ls.length || ls.length > 3) bad.push('一句話 ' + ls.length + ' 行（應為 1 至 3 行）');
        const bent = ls.filter(s => textLines(d, s) > 1).map(s => s.textContent);
        if (bent.length) bad.push('一句話自動折行：「' + bent.join('」「') + '」（封面斷行該行太長）');
        const joined = ls.map(s => s.textContent).join('');
        if (joined !== lineOf[id]) bad.push('一句話「' + joined + '」與 card_line「' + lineOf[id] + '」不同');
        if (wl) {
          const lt = wl.getBoundingClientRect().top;
          const hit = [...win.querySelectorAll('.rep, .tag')].filter(e => e.getBoundingClientRect().bottom > lt + 1).map(name);
          if (hit.length) bad.push('一句話壓到 ' + hit.join('、'));
        }
        // 3c. 手機卡片內最小字（DESIGN.md 第二章第 5 節：375px 寬約 11px；iframe 有約 15px 捲軸，實測約 10.5px，故門檻 10px）
        if (narrow) {
          const small = [...cv.querySelectorAll('.top span, .ttl, .bot, .tag, .wl')].filter(e => parseFloat(W.getComputedStyle(e).fontSize) < 10).map(name);
          if (small.length) bad.push('字級小於 10px：' + [...new Set(small)].join('、'));
        }
        out(bad.length === 0, tag, (c.querySelector('.top span') || {}).textContent + ' ' + id + (bad.length ? '：' + [...new Set(bad)].join('；') : '：3:4、未裁切、一句話 ' + ls.length + ' 行未折行且與 card_line 相同'));
        // 3d. 截斷：論文名超過兩行、雙年份或語言標籤以省略號截斷（DESIGN.md 允許截斷，但須依 card-wall.md 第五節判斷）
        const ttl = cv.querySelector('.ttl');
        if (ttl && ttl.scrollHeight > ttl.clientHeight + 2) warn(tag, id + ' 論文名超過兩行，被截斷：「' + ttl.textContent + '」');
        cv.querySelectorAll('.bot, .tag').forEach(e => { if (e.scrollWidth > e.clientWidth + 1) warn(tag, id + ' ' + name(e) + ' 被截斷：「' + e.textContent + '」'); });
      });

      // 4. 欄數：桌面 1440 為 3 欄，手機為 2 欄
      const cols = W.getComputedStyle(d.getElementById('grid')).gridTemplateColumns.split(' ').length;
      out(cols === (narrow ? 2 : 3), tag, '卡片牆 ' + cols + ' 欄（應為 ' + (narrow ? 2 : 3) + ' 欄）');

      // 5. 頁面不得橫向捲動
      out(d.documentElement.scrollWidth <= W.innerWidth + 1, tag, '頁面寬 ' + d.documentElement.scrollWidth + 'px，視窗寬 ' + W.innerWidth + 'px');

      // 6. 篩選：群星點學科（桌面點左欄懸星、手機點篩選列），只顯示屬於該學科之卡片；再點一次恢復全部
      //    我的星系點角色。篩選對象取指定之 slug 所屬者，未指定時取第一張卡。
      const pick = (SLUG && mine.find(c => c.dataset.slug === SLUG)) || mine[0];
      if (pick) {
        let key, btnSel;
        if (mode === 'stars') key = pick.dataset.in.split(' ')[0];
        else key = 'role:' + data.focus.papers.find(p => p.slug === pick.dataset.slug).role;
        btnSel = narrow ? '[data-chip="' + key + '"]' : '[data-strand="' + key + '"]';
        const btn = d.querySelector(btnSel);
        if (!btn) out(false, tag, '找不到篩選按鈕 ' + btnSel);
        else {
          btn.click(); await wait(900);
          const want = mode === 'stars'
            ? mine.filter(c => c.dataset.in.split(' ').includes(key))
            : mine.filter(c => data.focus.papers.find(p => p.slug === c.dataset.slug).role === key.slice(5));
          const now = all.filter(c => !c.hidden);
          const same = now.length === want.length && want.every(c => !c.hidden);
          out(same, tag, '篩選「' + key + '」：顯示 ' + now.length + ' 張，應為 ' + want.length + ' 張（' + d.getElementById('archInfo').textContent + '）');
          d.querySelector(btnSel).click(); await wait(900);
          const back = all.filter(c => !c.hidden).length;
          out(back === mine.length, tag, '再點一次取消篩選：顯示 ' + back + ' 張，應為 ' + mine.length + ' 張');
        }
      }

      // 7. 連結：每張卡連到之論文頁可開啟（每個網址只查一次）
      for (const c of mine) {
        if (linkOk[c.href] === undefined) {
          try { linkOk[c.href] = (await fetch(c.href, { method: 'HEAD', cache: 'no-store' })).status; } catch (e) { linkOk[c.href] = 'ERR'; }
          out(linkOk[c.href] === 200, tag, c.dataset.slug + ' 連結 ' + c.getAttribute('href') + ' 回應 ' + linkOk[c.href]);
        }
      }
      f.remove();
    }
  }
  function EK_SLUG_MSG(n) { return SLUG + ' 在牆上 ' + n + ' 張（應為 1 張）：卡片檔未提交又沒加 --card、或 build_home.py 未重跑'; }
  const summary = (fails === 0 ? '結果：PASS' : '結果：FAIL ' + fails + ' 項') + (warns ? '，WARN ' + warns + ' 項' : '') + '（首頁卡片牆' + (SLUG ? '，指定 ' + SLUG : '') + '）';
  const report = lines.join('\n') + '\n' + summary;
  console.log(report);
  return report;
})();
