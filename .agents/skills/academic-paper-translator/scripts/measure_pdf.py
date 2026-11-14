#!/usr/bin/env python3
"""measure_pdf.py: 量測原論文或譯本 PDF 之實體版面參數、轉出對照 PNG 並裁切圖表區域。

供 academic-paper-translator 於〈執行流程〉第 1、3、5 步使用，只於本機處理 PDF：
  1. 版面量測：紙張尺寸（A4 / US Letter）、估計頁邊距、單／雙欄判別、字型與字級統計、圖表標題清單。
  2. 轉出 PNG（--render-dir）：將指定頁碼或全份 PDF 轉成影像，方便對照原稿或檢查譯本成品。
  3. 圖表裁切（--crop / --auto-figures）：依指定座標（page:x0,y0,x1,y1 pt）或圖說位置裁出 300 DPI 原圖 PNG。

用法：
    python .agents/skills/academic-paper-translator/scripts/measure_pdf.py raw/foo.pdf
    python .agents/skills/academic-paper-translator/scripts/measure_pdf.py raw/foo.pdf --render-dir work/ref_pages --dpi 180
    python .agents/skills/academic-paper-translator/scripts/measure_pdf.py raw/foo.pdf --crop 3:45,80,550,310 --out work/fig1.png --dpi 300
    python .agents/skills/academic-paper-translator/scripts/measure_pdf.py raw/foo.pdf --auto-figures work/figs --dpi 300
"""
import argparse
from collections import Counter
import json
import os
import re
import sys

try:
    import pymupdf
except ImportError:  # pragma: no cover
    import fitz as pymupdf  # type: ignore

PT_TO_MM = 25.4 / 72.0
CAPTION_RE = re.compile(r'^(Figure|Fig\.?|Table|表|圖)\s*([0-9]+|[IVX]+)\b', re.IGNORECASE)


def parse_pages(spec, count):
    """將 'all' 或 '1-3,6'（1 起算）轉為 0 起算頁碼清單。"""
    if not spec or spec.strip().lower() == 'all':
        return list(range(count))
    pages = []
    for part in spec.split(','):
        part = part.strip()
        if '-' in part:
            lo, hi = (int(x.strip()) for x in part.split('-', 1))
        else:
            lo = hi = int(part)
        if lo < 1 or hi > count or lo > hi:
            raise ValueError(f'頁碼 {part} 超出範圍（共 {count} 頁）')
        pages.extend(range(lo - 1, hi))
    return sorted(set(pages))


def classify_paper(w_pt, h_pt):
    """依寬高比與公制／美制接近度辨識常見論文紙張規格。"""
    w_mm = w_pt * PT_TO_MM
    h_mm = h_pt * PT_TO_MM
    orient = 'portrait' if h_pt >= w_pt else 'landscape'
    short_mm, long_mm = sorted((w_mm, h_mm))
    if abs(short_mm - 210.0) <= 3.0 and abs(long_mm - 297.0) <= 3.0:
        name = 'A4'
    elif abs(short_mm - 215.9) <= 3.5 and abs(long_mm - 279.4) <= 3.5:
        name = 'US Letter'
    else:
        name = f'Custom ({w_mm:.1f} x {h_mm:.1f} mm)'
    return f'{name} {orient}', w_mm, h_mm


def inspect_pdf(pdf_path, pages=None):
    """量測 PDF 尺寸、估算邊距、判別欄數、統計字型與擷取圖表標題位置。"""
    doc = pymupdf.open(pdf_path)
    try:
        idxs = parse_pages(pages, len(doc))
        first_rect = doc[0].rect
        paper_label, w_mm, h_mm = classify_paper(first_rect.width, first_rect.height)

        left_edges, right_edges, top_edges, bottom_edges = [], [], [], []
        font_counter = Counter()
        size_counter = Counter()
        narrow_left = 0
        narrow_right = 0
        wide_blocks = 0
        captions = []
        image_counts = {}

        for i in idxs:
            page = doc[i]
            pw = page.rect.width
            mid = pw / 2.0
            imgs = page.get_images(full=True)
            if imgs:
                image_counts[i + 1] = len(imgs)

            data = page.get_text('dict')
            for blk in data.get('blocks', []):
                if blk.get('type') != 0:
                    continue
                x0, y0, x1, y1 = blk['bbox']
                bw = x1 - x0
                bh = y1 - y0
                if bw < 5 or bh < 5:
                    continue
                # 排除極貼邊之頁眉頁腳微字行，優先以主文字塊估算正文邊界
                if y0 > page.rect.height * 0.04 and y1 < page.rect.height * 0.95:
                    left_edges.append(x0)
                    right_edges.append(pw - x1)
                    top_edges.append(y0)
                    bottom_edges.append(page.rect.height - y1)

                lines_text = []
                for ln in blk.get('lines', []):
                    ln_chars = []
                    for sp in ln.get('spans', []):
                        t = sp.get('text', '')
                        ln_chars.append(t)
                        st = t.strip()
                        if st:
                            font_counter[sp.get('font', '')] += len(st)
                            size_counter[round(sp.get('size', 0.0), 1)] += len(st)
                    joined = ''.join(ln_chars).strip()
                    if joined:
                        lines_text.append(joined)

                block_text = ' '.join(lines_text).strip()
                if block_text and CAPTION_RE.match(block_text):
                    captions.append({
                        'page': i + 1,
                        'bbox_pt': [round(v, 1) for v in (x0, y0, x1, y1)],
                        'text': block_text[:140],
                    })

                if len(block_text) >= 60:
                    if x1 <= mid + 12 and bw <= pw * 0.48:
                        narrow_left += 1
                    elif x0 >= mid - 12 and bw <= pw * 0.48:
                        narrow_right += 1
                    elif bw >= pw * 0.58:
                        wide_blocks += 1

        if (narrow_left >= 2 and narrow_right >= 2) and (narrow_left + narrow_right) > wide_blocks:
            columns = '2-column'
        elif wide_blocks >= 2:
            columns = '1-column'
        else:
            columns = 'mixed/uncertain'

        margins_mm = None
        if left_edges:
            margins_mm = {
                'left': round(min(left_edges) * PT_TO_MM, 1),
                'right': round(min(right_edges) * PT_TO_MM, 1),
                'top': round(min(top_edges) * PT_TO_MM, 1),
                'bottom': round(min(bottom_edges) * PT_TO_MM, 1),
            }

        return {
            'file': pdf_path,
            'page_count': len(doc),
            'paper': paper_label,
            'size_pt': [round(first_rect.width, 2), round(first_rect.height, 2)],
            'size_mm': [round(w_mm, 1), round(h_mm, 1)],
            'estimated_columns': columns,
            'column_block_stats': {
                'left': narrow_left,
                'right': narrow_right,
                'wide': wide_blocks,
            },
            'estimated_margins_mm': margins_mm,
            'top_fonts': font_counter.most_common(6),
            'top_font_sizes_pt': size_counter.most_common(6),
            'embedded_images_by_page': image_counts,
            'detected_captions': captions,
        }
    finally:
        doc.close()


def render_pages(pdf_path, out_dir, dpi=180, pages=None):
    """將 PDF 頁面轉存為 PNG，先行清理該資料夾舊 page_*.png。"""
    os.makedirs(out_dir, exist_ok=True)
    for fn in os.listdir(out_dir):
        if re.match(r'^page_\d+\.png$', fn):
            os.remove(os.path.join(out_dir, fn))

    doc = pymupdf.open(pdf_path)
    try:
        idxs = parse_pages(pages, len(doc))
        written = []
        for i in idxs:
            out_path = os.path.join(out_dir, f'page_{i + 1}.png')
            doc[i].get_pixmap(dpi=dpi, alpha=False).save(out_path)
            written.append(out_path)
        return written
    finally:
        doc.close()


def crop_region(pdf_path, spec, out_path, dpi=300):
    """依 page:x0,y0,x1,y1（pt）裁出指定區域之高解析 PNG。"""
    m = re.match(r'^(\d+):([\d.]+),([\d.]+),([\d.]+),([\d.]+)$', spec.strip())
    if not m:
        raise ValueError('crop 參數格式須為 page:x0,y0,x1,y1（例：3:45,80,550,310）')
    page_num = int(m.group(1))
    x0, y0, x1, y1 = (float(m.group(i)) for i in range(2, 6))
    doc = pymupdf.open(pdf_path)
    try:
        if page_num < 1 or page_num > len(doc):
            raise ValueError(f'頁碼 {page_num} 超出範圍（共 {len(doc)} 頁）')
        page = doc[page_num - 1]
        clip = pymupdf.Rect(x0, y0, x1, y1) & page.rect
        if clip.is_empty or clip.width < 5 or clip.height < 5:
            raise ValueError('裁切區域為空或過小')
        parent = os.path.dirname(os.path.abspath(out_path))
        if parent:
            os.makedirs(parent, exist_ok=True)
        page.get_pixmap(dpi=dpi, clip=clip, alpha=False).save(out_path)
        return out_path
    finally:
        doc.close()


def auto_crop_figures(pdf_path, out_dir, dpi=300, pages=None):
    """結合頁面非文字繪圖／影像區塊與圖說座標，自動擷取候選原圖區域 PNG。"""
    os.makedirs(out_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    saved = []
    try:
        idxs = parse_pages(pages, len(doc))
        for i in idxs:
            page = doc[i]
            pw, ph = page.rect.width, page.rect.height
            graphic_boxes = []

            for info in page.get_image_info(xrefs=False):
                bbox = pymupdf.Rect(info['bbox'])
                if bbox.width >= 30 and bbox.height >= 30:
                    graphic_boxes.append(bbox)

            for drw in page.get_drawings():
                r = pymupdf.Rect(drw['rect'])
                if r.width >= 20 and r.height >= 20 and r.height < ph * 0.85:
                    graphic_boxes.append(r)

            # 合併相鄰繪圖邊框為群組（容差 14pt）
            clusters = []
            for box in graphic_boxes:
                expanded = box + (-14, -14, 14, 14)
                merged = False
                for idx, cl in enumerate(clusters):
                    if cl.intersects(expanded):
                        clusters[idx] = cl | box
                        merged = True
                        break
                if not merged:
                    clusters.append(box)

            # 再收斂一次相鄰群組
            changed = True
            while changed and len(clusters) > 1:
                changed = False
                out_cl = []
                while clusters:
                    cur = clusters.pop(0)
                    exp = cur + (-14, -14, 14, 14)
                    rest = []
                    for oth in clusters:
                        if oth.intersects(exp):
                            cur = cur | oth
                            changed = True
                        else:
                            rest.append(oth)
                    clusters = rest
                    out_cl.append(cur)
                clusters = out_cl

            fig_idx = 0
            for cl in sorted(clusters, key=lambda r: (round(r.y0, 1), round(r.x0, 1))):
                if cl.width < pw * 0.18 or cl.height < 45:
                    continue
                clip = (cl + (-6, -6, 6, 6)) & page.rect
                fig_idx += 1
                fname = os.path.join(out_dir, f'p{i + 1}_fig{fig_idx}.png')
                page.get_pixmap(dpi=dpi, clip=clip, alpha=False).save(fname)
                saved.append({
                    'file': fname,
                    'page': i + 1,
                    'bbox_pt': [round(clip.x0, 1), round(clip.y0, 1), round(clip.x1, 1), round(clip.y1, 1)],
                })
        return saved
    finally:
        doc.close()


def print_summary(info):
    print(f"檔案: {info['file']}")
    print(f"頁數: {info['page_count']} | 紙張: {info['paper']} ({info['size_pt'][0]} x {info['size_pt'][1]} pt / {info['size_mm'][0]} x {info['size_mm'][1]} mm)")
    print(f"欄數判別: {info['estimated_columns']} (左欄塊 {info['column_block_stats']['left']}, 右欄塊 {info['column_block_stats']['right']}, 寬塊 {info['column_block_stats']['wide']})")
    if info['estimated_margins_mm']:
        m = info['estimated_margins_mm']
        print(f"估計邊距(mm): 上 {m['top']} / 下 {m['bottom']} / 左 {m['left']} / 右 {m['right']}")
    fonts = ', '.join(f'{k} ({v})' for k, v in info['top_fonts'])
    sizes = ', '.join(f'{k}pt ({v})' for k, v in info['top_font_sizes_pt'])
    print(f"主要字型: {fonts}")
    print(f"主要字級: {sizes}")
    if info['embedded_images_by_page']:
        imgs = ', '.join(f'p.{k}: {v}張' for k, v in sorted(info['embedded_images_by_page'].items()))
        print(f"內嵌點陣圖: {imgs}")
    else:
        print("內嵌點陣圖: 0 張（如有圖表多為向量繪圖，可用 --auto-figures 或 --crop 裁切）")
    if info['detected_captions']:
        print(f"偵測圖表標題 ({len(info['detected_captions'])} 筆):")
        for c in info['detected_captions']:
            print(f"  p.{c['page']} {c['bbox_pt']} | {c['text']}")
    else:
        print("偵測圖表標題: 0 筆")


def main():
    parser = argparse.ArgumentParser(description='量測論文 PDF 版面規格、轉出 PNG 或裁切圖表區域。')
    parser.add_argument('pdf', help='輸入 PDF 檔案路徑')
    parser.add_argument('--pages', default='all', help='處理頁碼範圍，例如 1-3,6（預設 all）')
    parser.add_argument('--json', action='store_true', help='以 JSON 格式輸出量測結果')
    parser.add_argument('--render-dir', help='轉出逐頁 PNG 的資料夾路徑')
    parser.add_argument('--dpi', type=int, default=180, help='PNG 轉出或裁切解析度（預設 180；圖表建議 300）')
    parser.add_argument('--crop', help='裁切單一區域，格式為 page:x0,y0,x1,y1（pt）')
    parser.add_argument('--out', help='搭配 --crop 指定輸出 PNG 路徑')
    parser.add_argument('--auto-figures', help='自動偵測並裁切非文字圖形區域至指定資料夾')
    args = parser.parse_args()

    if not os.path.isfile(args.pdf):
        print(f'找不到檔案: {args.pdf}', file=sys.stderr)
        return 1

    try:
        if args.crop:
            if not args.out:
                print('使用 --crop 時必須搭配 --out <輸出PNG路徑>', file=sys.stderr)
                return 1
            out = crop_region(args.pdf, args.crop, args.out, dpi=args.dpi)
            print(f'已裁切區域輸出至: {out}')
            return 0

        if args.auto_figures:
            saved = auto_crop_figures(args.pdf, args.auto_figures, dpi=args.dpi, pages=args.pages)
            print(f'已擷取候選圖形 {len(saved)} 個至 {args.auto_figures}:')
            for s in saved:
                print(f"  p.{s['page']} {s['bbox_pt']} -> {s['file']}")
            return 0

        info = inspect_pdf(args.pdf, pages=args.pages)
        if args.json:
            print(json.dumps(info, ensure_ascii=False, indent=2))
        else:
            print_summary(info)

        if args.render_dir:
            written = render_pages(args.pdf, args.render_dir, dpi=args.dpi, pages=args.pages)
            print(f'已轉出 {len(written)} 頁 PNG 至 {args.render_dir}')
        return 0
    except Exception as exc:
        print(f'處理失敗: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
