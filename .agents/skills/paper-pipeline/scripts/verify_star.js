// 首頁星圖與我的星系之上架驗證（paper-pipeline 第四節 S9；細則見 references/publish.md 第三節）。
//
// 用法：
//   1. 於倉庫根目錄啟動本機伺服器：python -m http.server 8781 --bind 127.0.0.1 --directory web
//   2. 在瀏覽器開 http://127.0.0.1:8781/index.html ，分頁保持在前景。
//   3. 在 Console 先執行一行指定論文：var EK_SLUG = '2016-ligo-gravitational-waves';
//      再把本檔全部內容貼進 Console 執行（兩段可放在同一次執行），約 10 秒後輸出報告。
//   4. 把輸出的整段文字原樣貼進交付說明。任何一行 FAIL 都不得交付。
//
// 本腳本依首頁資料判斷這篇在群星（星圖）或我的星系（網址 #my-constellation），以隱藏 iframe 量測
// 桌面 1440 x 900 與手機 375 x 812：首頁資料有這篇、星點存在且看得見、無障礙標籤含論文名、
// 點擊後星點為選取狀態且說明框顯示論文名（群星另查一句話）。只量上架與互動，不判斷內容對錯。
(async () => {
  const SLUG = (typeof EK_SLUG === 'string' ? EK_SLUG : '').trim();
  const SIZES = [[1440, 900], [375, 812]];
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const lines = [];
  let fails = 0, warns = 0;
  const out = (ok, tag, msg) => { if (!ok) fails++; lines.push((ok ? 'PASS ' : 'FAIL ') + tag + '  ' + msg); };
  const warn = (tag, msg) => { warns++; lines.push('WARN ' + tag + '  ' + msg); };
  const base = location.href.split('#')[0].replace(/[^/]*$/, '') + 'index.html';
  const norm = s => (s || '').replace(/\s+/g, '');
  if (!SLUG) {
    const msg = '結果：FAIL 1 項（未設定 EK_SLUG；先執行 var EK_SLUG = \'<slug>\';）';
    console.log(msg);
    return msg;
  }
  for (const [w, h] of SIZES) {
    const f = document.createElement('iframe');
    f.style.cssText = 'position:fixed;left:-10000px;top:0;border:0;width:' + w + 'px;height:' + h + 'px';
    f.src = base;
    document.body.appendChild(f);
    await new Promise(r => { f.onload = r; });
    let d = f.contentDocument, W = f.contentWindow;
    const data = JSON.parse(d.getElementById('ek-data').textContent);
    const inStars = data.papers.find(p => p.slug === SLUG);
    const inFocus = data.focus ? data.focus.papers.find(p => p.slug === SLUG) : null;
    const mode = inFocus ? 'focus' : 'stars';
    const tag = w + 'x' + h + ' ' + (mode === 'stars' ? '群星' : '我的星系');
    out(!!(inStars || inFocus), tag, SLUG + (inStars ? ' 在首頁資料之群星（papers）' : inFocus ? ' 在首頁資料之我的星系（focus.papers）' : ' 不在首頁資料：論文頁未收錄、或首頁未以 build_home.py 重建'));
    if (!(inStars || inFocus)) { f.remove(); continue; }
    if (mode === 'focus') {
      W.location.hash = '#my-constellation';
      await wait(300);
    }
    if (d.fonts && d.fonts.ready) await d.fonts.ready;
    await wait(1500);
    d = f.contentDocument;
    const p = inStars || inFocus;
    const attr = mode === 'stars' ? 'data-p' : 'data-f';
    const btn = d.querySelector('button.star[' + attr + '="' + SLUG + '"]');
    out(!!btn, tag, '星點 button.star[' + attr + '="' + SLUG + '"] ' + (btn ? '存在' : '不存在：首頁未重建或星圖程式未畫出這篇'));
    if (!btn) { f.remove(); continue; }
    const r = btn.getBoundingClientRect();
    const cs = W.getComputedStyle(btn);
    const shown = r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden';
    const inside = r.right > 0 && r.left < w;
    out(shown && inside, tag, '星點看得見（' + Math.round(r.width) + ' x ' + Math.round(r.height) + 'px，左緣 ' + Math.round(r.left) + 'px）' + (inside ? '' : '，但落在畫面左右之外'));
    const label = btn.getAttribute('aria-label') || '';
    out(norm(label).indexOf(norm(p.name)) >= 0, tag, '無障礙標籤含論文名「' + p.name + '」：' + label);
    btn.click();
    await wait(500);
    const pressed = btn.getAttribute('aria-pressed') === 'true';
    const info = d.getElementById('info');
    const infoText = info ? info.innerText : '';
    const hasName = norm(infoText).indexOf(norm(p.name)) >= 0 || norm(infoText).indexOf(norm(p.titleZh)) >= 0;
    if (pressed && hasName) out(true, tag, '點擊後為選取狀態，說明框顯示論文名');
    else if (w < 600) warn(tag, '手機點擊後' + (pressed ? '' : '未成為選取狀態') + (hasName ? '' : '，說明框未見論文名') + '（手機操作方式可能不同，請以截圖目視確認）');
    else out(false, tag, '點擊後' + (pressed ? '' : '未成為選取狀態') + (hasName ? '' : '，說明框未見論文名「' + p.name + '」'));
    if (mode === 'stars' && hasName && p.cardLine) {
      if (norm(infoText).indexOf(norm(p.cardLine)) >= 0) out(true, tag, '說明框顯示一句話「' + p.cardLine + '」');
      else warn(tag, '說明框未見一句話「' + p.cardLine + '」，請以截圖目視確認');
    }
    f.remove();
  }
  const summary = (fails === 0 ? '結果：PASS' : '結果：FAIL ' + fails + ' 項') + (warns ? '，WARN ' + warns + ' 項' : '') + '（首頁星圖，指定 ' + SLUG + '）';
  const report = lines.join('\n') + '\n' + summary;
  console.log(report);
  return report;
})();
