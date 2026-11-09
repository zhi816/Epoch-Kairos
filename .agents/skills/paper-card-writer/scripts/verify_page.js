// 論文頁參考原型之瀏覽器驗證（paper-card-writer 第五節第 7 步）。
//
// 用法：
//   1. 於倉庫根目錄啟動本機伺服器：python -m http.server 8781 --bind 127.0.0.1 --directory web
//      （不可用 file:// 直接開檔：瀏覽器會擋下讀取 iframe 內容）
//   2. 在瀏覽器開 http://127.0.0.1:8781/prototypes/paper-v1/<slug>.html
//   3. 把本檔全部內容貼進開發者工具 Console 執行（或以代理之瀏覽器 JavaScript 工具執行），等待約 10 秒。
//   4. 把輸出的整段文字原樣貼進交付說明。任何一行 FAIL 都不得交付。
//
// 本腳本以兩個隱藏 iframe 同時量測桌面 1440 x 900 與手機 375 x 812，不必手動調整視窗。
// 量測項目：公式是否全部渲染且無錯誤、六張卡內容是否溢出卡片、卡片內公式是否需要水平捲動、
// 封面一句話是否超過三行或溢出星窗、頁面是否有橫向捲動、卡片下方控制列是否超出版面、
// 頁面是否露出 ** 或 $、長文區塊公式是否可水平捲動。只量版面，不判斷內容對錯。
(async () => {
  const SIZES = [[1440, 900], [375, 812]];
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const name = e => (e.className && e.className.baseVal !== undefined ? e.className.baseVal : e.className) || e.tagName;
  const lines = [];
  let fails = 0, warns = 0;
  const out = (ok, size, msg) => { if (!ok) fails++; lines.push((ok ? 'PASS ' : 'FAIL ') + size + '  ' + msg); };
  const warn = (size, msg) => { warns++; lines.push('WARN ' + size + '  ' + msg); };
  const clips = (W, e) => ['hidden', 'clip'].includes(W.getComputedStyle(e).overflowX) || ['hidden', 'clip'].includes(W.getComputedStyle(e).overflowY);

  for (const [w, h] of SIZES) {
    const size = w + 'x' + h;
    const f = document.createElement('iframe');
    f.style.cssText = 'position:fixed;left:-10000px;top:0;border:0;width:' + w + 'px;height:' + h + 'px';
    f.src = location.href.split('#')[0];
    document.body.appendChild(f);
    await new Promise(r => { f.onload = r; });
    await wait(4000);                       // 等 KaTeX 與字型載入
    const d = f.contentDocument, W = f.contentWindow;

    // 1. 公式
    const texN = d.querySelectorAll('[data-tex]').length;
    const done = [...d.querySelectorAll('[data-tex]')].filter(e => e.querySelector('.katex')).length;
    const errs = [...d.querySelectorAll('.katex-error')].map(e => e.getAttribute('title') || e.textContent).slice(0, 3);
    out(done === texN && errs.length === 0, size, '公式 ' + done + '/' + texN + ' 已渲染，錯誤 ' + errs.length + (errs.length ? '：' + errs.join(' / ') : ''));

    // 2. 卡片內容不得被裁掉：每個元素都不得超出卡片本身，以及卡片內任何一層會裁切內容的容器
    //    （例如封面星窗：導語太長時星窗被擠小，一句話的上緣會被星窗切掉，卡片外框卻完全正常）。
    //    KaTeX 隱藏之 MathML 除外。
    const cards = [...d.querySelectorAll('.card')];
    cards.forEach((c, i) => {
      const bad = [];
      [...c.querySelectorAll('*')].filter(e => !e.closest('.katex-mathml')).forEach(e => {
        const b = e.getBoundingClientRect();
        if (!(b.width > 0 && b.height > 0)) return;
        for (let a = e.parentElement; a; a = a.parentElement) {
          if (a === c || clips(W, a)) {
            const r = a.getBoundingClientRect();
            if (b.right > r.right + 1 || b.bottom > r.bottom + 1 || b.left < r.left - 1 || b.top < r.top - 1) { bad.push(name(e) + ' 超出 ' + name(a)); break; }
          }
          if (a === c) break;
        }
      });
      const inner = c.querySelector('.in');
      const clipped = inner && inner.scrollHeight > inner.clientHeight + 2;
      out(bad.length === 0 && !clipped, size, 'Card ' + (i + 1) + ' 內容未被裁切' + (bad.length ? '；' + [...new Set(bad)].slice(0, 3).join('；') : '') + (clipped ? '；卡片內文高度不足' : ''));
    });

    // 2b. 封面論文名最多兩行（超過會被截斷，見 cover.md 第四節）
    const nm = d.querySelector('.card.cover .name');
    if (nm) out(nm.scrollHeight <= nm.clientHeight * 1.2, size, '封面論文名未被截斷（內容高 ' + nm.scrollHeight + 'px，顯示高 ' + nm.clientHeight + 'px）');

    // 2c. 應為單行的元素不得折行，也不得超出自己的格子：Card 2 對照名稱、Card 4 大數字、Card 5 年份
    //     （例：「1.14 PeV」在桌面被擠成兩行、「99.999%」超出右欄，元素仍在卡片內，2 抓不到）
    const single = [...d.querySelectorAll('.card .row > b, .card .stat .v, .card .time p > b')];
    // 以文字範圍量行數與右緣：這些元素是 grid 格子，高度會被同列的說明撐高，不能用元素高度推算行數
    const bent = single.filter(e => {
      const rg = d.createRange(); rg.selectNodeContents(e);
      const lines = new Set([...rg.getClientRects()].filter(q => q.width > 0).map(q => Math.round(q.top))).size;
      const tr = rg.getBoundingClientRect(), er = e.getBoundingClientRect();
      return lines > 1 || tr.right > er.right + 1;
    }).map(e => 'Card ' + ([...d.querySelectorAll('.card')].indexOf(e.closest('.card')) + 1) + '「' + e.textContent.trim() + '」');
    out(bent.length === 0, size, '單行元素（Card 2 名稱、Card 4 大數字、Card 5 年份）共 ' + single.length + ' 個皆未折行或超出' + (bent.length ? '；折行或超出：' + bent.join('、') : ''));

    // 3. 卡片內公式框不得需要水平捲動（card-03-secret.md 第四節第 2 條）
    d.querySelectorAll('.card .fbox').forEach(fb => {
      const m = fb.querySelector('.m-disp') || fb;
      out(m.scrollWidth <= m.clientWidth + 1, size, 'Card 3 公式框寬 ' + Math.round(m.clientWidth) + 'px，公式寬 ' + Math.round(m.scrollWidth) + 'px');
    });

    // 4. 封面一句話：最多三行、不溢出星窗
    const win = d.querySelector('.card.cover .win');
    if (win) {
      const ln = win.querySelectorAll('.line > span');
      const wr = win.getBoundingClientRect();
      const over = [...ln].filter(s => { const b = s.getBoundingClientRect(); return b.right > wr.right + 1 || b.left < wr.left - 1; });
      const wrapped = [...ln].filter(s => s.getClientRects().length > 1);
      out(ln.length <= 3 && over.length === 0 && wrapped.length === 0, size, '封面一句話 ' + ln.length + ' 行' + (over.length ? '，有行超出星窗' : '') + (wrapped.length ? '，有行自動折行（封面斷行該行太長）' : ''));
      // 一句話不得壓到星窗內的語言標籤或代表星
      const line = win.querySelector('.line');
      if (line) {
        const lt = line.getBoundingClientRect().top;
        const hit = [...win.querySelectorAll('.lang, .rep')].filter(e => e.getBoundingClientRect().bottom > lt + 1).map(name);
        out(hit.length === 0, size, '封面一句話未壓到星窗內之標籤或代表星' + (hit.length ? '；重疊：' + hit.join(', ') : ''));
      }
      // 星窗被壓縮：導語或論文名太長時星窗變小（正常約為卡片高度之 0.33 至 0.49）
      const ratio = wr.height / win.closest('.card').getBoundingClientRect().height;
      if (ratio < 0.3) warn(size, '星窗只佔卡片高度 ' + ratio.toFixed(2) + '，導語或論文名可能太長，請縮短後重驗');
    }

    // 5. 頁面不得橫向捲動
    out(d.documentElement.scrollWidth <= W.innerWidth + 1, size, '頁面寬 ' + d.documentElement.scrollWidth + 'px，視窗寬 ' + W.innerWidth + 'px');

    // 6. 卡片下方控制列不得超出卡片欄
    const ctrl = d.querySelector('.ctrl'), stage = d.querySelector('.stage');
    if (ctrl && stage) {
      const cr = ctrl.getBoundingClientRect(), sr = stage.getBoundingClientRect();
      out(cr.left >= sr.left - 1 && cr.right <= sr.right + 1, size, '控制列 ' + Math.round(cr.width) + 'px 位於卡片欄 ' + Math.round(sr.width) + 'px 之內');
    }

    // 7. 頁面不得露出 Markdown 或公式記號
    const vis =[...d.querySelectorAll('.art, .card, .side')].map(e => {
      const c = e.cloneNode(true); c.querySelectorAll('.katex').forEach(k => k.remove()); return c.textContent;
    }).join('\n');
    out(!/\*\*/.test(vis) && !/\$/.test(vis), size, '未露出 ** 或 $' + (/\*\*/.test(vis) ? '（有 **）' : '') + (/\$/.test(vis) ? '（有 $）' : ''));

    // 8. 長文區塊公式可水平捲動（AGENTS.md 第三章第 3 條）
    const disp = [...d.querySelectorAll('.art .m-disp')];
    const noScroll = disp.filter(e => !['auto', 'scroll'].includes(W.getComputedStyle(e).overflowX));
    out(noScroll.length === 0, size, '長文區塊公式 ' + disp.length + ' 條皆可水平捲動');

    // 9. 手機（寬度 900px 以下）：卡片可左右滑動並停在整張；長文「隨卡片」時只顯示目前段落，「全文」時全部顯示且不隨卡片變動
    if (w <= 900) {
      const deck = d.querySelector('.deck'), cs = [...d.querySelectorAll('.card')];
      const shown = () => [...d.querySelectorAll('.art section[data-card]')].filter(s => W.getComputedStyle(s).display !== 'none').map(s => s.dataset.card);
      out(/x/.test(W.getComputedStyle(deck).scrollSnapType) && W.getComputedStyle(deck).overflowX === 'auto', size, '卡片列可左右滑動且停在整張（scroll-snap）');
      const lab = () => d.getElementById('label').textContent.slice(0, 2);
      // 以程式捲動卡片列時，部分環境（隱藏 iframe、背景分頁）會把 scroll 事件延遲一秒以上，故捲動後主動送出一次 scroll 事件
      const slide = async k => { deck.scrollLeft = cs[k].offsetLeft - cs[0].offsetLeft; deck.dispatchEvent(new W.Event('scroll')); await wait(400); };
      out(shown().join() === '1', size, '隨卡片：開頁只顯示 01 段（實際：' + shown().join() + '）');
      await slide(2);
      out(lab() === '03' && shown().join() === '3', size, '隨卡片：滑到第 3 張，標示 ' + lab() + '，長文顯示 ' + shown().join() + ' 段');
      const fullBtn = d.getElementById('m-full'), cardBtn = d.getElementById('m-card');
      if (fullBtn && cardBtn) {
        fullBtn.click(); await wait(200);
        const all = shown().join();
        await slide(4);
        out(all === '1,2,3,4,5,6' && shown().join() === '1,2,3,4,5,6', size, '全文：顯示全部 6 段，滑動卡片不改變長文（實際：' + all + ' → ' + shown().join() + '）');
        cardBtn.click(); await wait(200);
        out(shown().join() === lab().replace(/^0/, ''), size, '切回隨卡片：長文回到目前卡片之段落（第 ' + lab() + ' 張，顯示 ' + shown().join() + ' 段）');
      } else {
        out(false, size, '找不到長文顯示方式按鈕（#m-card、#m-full）');
      }
    }

    f.remove();
  }
  const summary = (fails === 0 ? '結果：PASS' : '結果：FAIL ' + fails + ' 項') + (warns ? '，WARN ' + warns + ' 項' : '') + '（' + location.pathname.split('/').pop() + '）';
  const report = lines.join('\n') + '\n' + summary;
  console.log(report);
  return report;
})();
