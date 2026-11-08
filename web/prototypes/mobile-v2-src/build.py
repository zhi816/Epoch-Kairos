"""重建 web/prototypes/mobile-v2.html。

用法（於倉庫根目錄執行）：python web/prototypes/mobile-v2-src/build.py
流程：data.py 讀取 wiki/papers 與 wiki/concepts 的 Frontmatter，計算星圖座標並輸出 JSON；
本腳本再把 JSON 內嵌到 template.html 的 /*__DATA__*/null 位置。
"""
import os, subprocess, sys, tempfile

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..', '..'))
tmp = os.path.join(tempfile.gettempdir(), 'epoch-kairos-mobile-v2-data.json')
subprocess.run([sys.executable, os.path.join(here, 'data.py'), os.path.join(root, 'wiki'), tmp], check=True, stdout=subprocess.DEVNULL)
t = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
d = open(tmp, encoding='utf-8').read().replace('</', '<' + chr(92) + '/')
assert t.count('/*__DATA__*/null') == 1
out = os.path.join(root, 'web', 'prototypes', 'mobile-v2.html')
open(out, 'w', encoding='utf-8', newline='\n').write(t.replace('/*__DATA__*/null', d))
print('built', out)
