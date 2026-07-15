#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ai-html 发布版：将「行业认知报告」Markdown 转为暗色卡片 + 顶部 Tab 分章的 index.html。
与 ai-spider 工作区的教学版同源，但为公开发布做了两处调整：
  ① <title>/H1 去掉"教学版"字样；② 移除"落到你身上"(Part C) 个人化章节（保留局限/方法论）。
改了 md 后重跑 `python3 build_html.py` 即可同步。"""
import re, html
from pathlib import Path

SRC = Path(__file__).parent / "美国电商流量与变现层-行业认知报告.md"
OUT = Path(__file__).parent / "index.html"

ACCENTS = ['#06d6a0', '#8338ec', '#ff006e', '#3a86ff', '#22c55e', '#fb5607', '#fbbf24']

TAB_META = {
    'overview':    ('概览',       'fa-compass'),
    'foundation':  ('打地基',     'fa-cubes-stacked'),
    'channels':    ('获客渠道',   'fa-route'),
    'models':      ('盈利模式',   'fa-coins'),
    'lifecycle':   ('生命周期',   'fa-chart-line'),
    'competitors': ('竞品拆解',   'fa-chess'),
    'notes':       ('说明与方法', 'fa-circle-info'),
    'sources':     ('参考文献',   'fa-book-open'),
}
TAB_ORDER = list(TAB_META.keys())   # '_skip' 不在其中 → 不渲染


def classify(level, t):
    if level == 2:
        if '执行摘要' in t: return ('overview', 'title')
        if t.startswith('Part A'): return None
        if t.startswith('Part B'): return ('competitors', 'title')
        if t.startswith('Part C'): return ('_skip', 'title')   # 移除"落到你身上"
        if '局限' in t: return ('notes', 'title')
        if '方法论' in t: return ('notes', 'card')
        if '参考文献' in t: return ('sources', 'title')
        return ('overview', 'title')
    if level == 3:
        if t.startswith('A0'): return ('foundation', 'title')
        if t.startswith('A1'): return ('channels', 'title')
        if t.startswith('A2'): return ('models', 'title')
        if t.startswith('A3'): return ('lifecycle', 'title')
        if t.startswith('A4'): return ('lifecycle', 'card')
        if re.match(r'B\d', t): return ('competitors', 'card')
        return None
    return None


def inline(text):
    text = html.escape(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'(https?://[^\s)）]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return text


def render_blocks(lines):
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'^---+\s*$', line) or line.strip() == '':
            i += 1; continue
        if line.strip().startswith('|') and i+1 < len(lines) and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i+1]):
            header = [c.strip() for c in line.strip().strip('|').split('|')]
            i += 2; rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            t = ['<div class="table-wrap"><table><thead><tr>']
            for h in header: t.append(f'<th>{inline(h)}</th>')
            t.append('</tr></thead><tbody>')
            for r in rows:
                t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            t.append('</tbody></table></div>')
            out.append(''.join(t)); continue
        if line.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                seg = lines[i].lstrip('>').strip()
                if seg: buf.append(seg)
                i += 1
            out.append(f'<div class="callout"><i class="fas fa-lightbulb"></i><div>{" ".join(inline(x) for x in buf)}</div></div>')
            continue
        if re.match(r'^\s*[-*] ', line):
            out.append('<ul>')
            while i < len(lines) and re.match(r'^\s*[-*] ', lines[i]):
                out.append(f'<li>{inline(re.sub(r"^\s*[-*] ", "", lines[i]))}</li>'); i += 1
            out.append('</ul>'); continue
        if re.match(r'^\s*\d+\. ', line):
            out.append('<ol>')
            while i < len(lines) and re.match(r'^\s*\d+\. ', lines[i]):
                out.append(f'<li>{inline(re.sub(r"^\s*\d+\. ", "", lines[i]))}</li>'); i += 1
            out.append('</ol>'); continue
        out.append(f'<p>{inline(line.strip())}</p>'); i += 1
    return '\n'.join(out)


md = SRC.read_text(encoding='utf-8')
lines = md.split('\n')

panels = {}
cur_tab = 'overview'
seg_buf = []

def add(tab, seg):
    panels.setdefault(tab, []).append(seg)

def flush():
    global seg_buf
    if any(l.strip() for l in seg_buf):
        add(cur_tab, ('content', seg_buf))
    seg_buf = []

for line in lines:
    if line.startswith('# ') and not line.startswith('## '):
        continue
    if line.startswith('## '):
        text = line[3:].strip()
        cls = classify(2, text)
        flush()
        if cls is None:
            continue
        tab, mode = cls
        cur_tab = tab
        add(tab, ('h2' if mode == 'title' else 'card', text))
        continue
    if line.startswith('#### '):
        flush(); add(cur_tab, ('card', line[5:].strip())); continue
    if line.startswith('### '):
        text = line[4:].strip()
        cls = classify(3, text)
        flush()
        if cls is None:
            add(cur_tab, ('card', text)); continue
        tab, mode = cls
        cur_tab = tab
        add(tab, ('h2' if mode == 'title' else 'card', text))
        continue
    seg_buf.append(line)
flush()


def render_panel(tid):
    segs = panels.get(tid, [])
    out, open_card, ci = [], False, 0
    def close():
        nonlocal open_card
        if open_card:
            out.append('</div></div>'); open_card = False
    for typ, val in segs:
        if typ == 'h2':
            close()
            out.append(f'<div class="sec-head"><span class="eyebrow"></span><h2>{inline(val)}</h2></div>')
        elif typ == 'card':
            close()
            color = ACCENTS[ci % len(ACCENTS)]; ci += 1
            out.append(f'<div class="card" style="--c:{color}"><div class="card-head"><span class="dot"></span>'
                       f'<h3 class="card-title">{inline(val)}</h3></div><div class="card-body">')
            open_card = True
        else:
            body = render_blocks(val)
            if body.strip():
                out.append(body if open_card else f'<div class="lead">{body}</div>')
    close()
    return '\n'.join(out)


nav, pane = [], []
for idx, tid in enumerate(TAB_ORDER):
    if tid not in panels: continue
    label, icon = TAB_META[tid]
    active = ' active' if idx == 0 else ''
    nav.append(f'<button class="tab{active}" data-tab="{tid}"><i class="fas {icon}"></i>{label}</button>')
    pane.append(f'<section class="panel{active}" id="panel-{tid}">{render_panel(tid)}</section>')

METRICS = [
    ("$113亿", "联盟驱动的美国电商销售额", "占全美电商 9.4%（PMA 口径）", "#06d6a0"),
    ("17.6%", "联盟+合作占电商销售份额", "Adobe 2024 假日季，+6% YoY", "#8338ec"),
    ("−91%", "纯 SEO 测评站流量崩塌", "HouseFresh：HCU + AI 摘要三杀", "#ff006e"),
    ("31%→18%", "Ibotta EBITDA 利润率", "2024 峰值，2025 回落", "#3a86ff"),
]
metrics_html = ''.join(
    f'<div class="stat" style="--c:{c}"><div class="stat-num">{v}</div>'
    f'<div class="stat-label">{l}</div><div class="stat-note">{n}</div></div>'
    for v, l, n, c in METRICS)

src_count = len(set(re.findall(r'https?://[^\s)）]+', md)))

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');
:root{--bg:#0a0a0f;--bg2:#12121a;--card:#16161f;--card2:#1c1c28;--line:#26263400;
 --cyan:#06d6a0;--purple:#8338ec;--pink:#ff006e;--blue:#3a86ff;--green:#22c55e;--yellow:#fbbf24;--orange:#fb5607;
 --tx:#f3f4f6;--tx2:#9ca3af;--tx3:#6b7280;}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Outfit',-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--tx);
 line-height:1.75;font-size:15px;overflow-x:hidden;-webkit-font-smoothing:antialiased;}
.bg-grid{position:fixed;inset:0;z-index:0;background-image:linear-gradient(rgba(131,56,236,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(131,56,236,.04) 1px,transparent 1px);background-size:64px 64px;}
.bg-glow{position:fixed;width:620px;height:620px;border-radius:50%;filter:blur(140px);opacity:.14;z-index:0;pointer-events:none;}
.g1{top:-240px;left:-200px;background:var(--purple);}
.g2{bottom:-260px;right:-220px;background:var(--cyan);}
.wrap{position:relative;z-index:1;max-width:1080px;margin:0 auto;padding:0 24px 80px;}
.topbar{display:flex;justify-content:space-between;align-items:center;padding:22px 4px 10px;color:var(--tx2);font-size:12.5px;flex-wrap:wrap;gap:8px;}
.topbar .meta span{margin-left:16px;}
.topbar .brand{display:inline-flex;align-items:center;gap:9px;font-weight:700;color:var(--tx);font-size:14px;}
.topbar .brand i{width:30px;height:30px;border-radius:9px;display:grid;place-items:center;color:#fff;background:linear-gradient(135deg,var(--cyan),var(--purple));}
.hero{padding:26px 0 8px;}
.eyebrow-top{display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border-radius:100px;font-size:12px;font-weight:600;letter-spacing:.06em;color:var(--cyan);background:linear-gradient(135deg,rgba(6,214,160,.12),rgba(131,56,236,.12));border:1px solid rgba(6,214,160,.25);margin-bottom:18px;}
.hero h1{font-size:clamp(1.9rem,4.4vw,3rem);font-weight:800;line-height:1.15;letter-spacing:-.01em;}
.hero h1 .grad{background:linear-gradient(135deg,var(--cyan) 0%,var(--purple) 50%,var(--pink) 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.hero .sub{color:var(--tx2);max-width:760px;margin-top:14px;font-size:15px;}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:26px 0 6px;}
.stat{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:18px 18px 16px;position:relative;overflow:hidden;}
.stat::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--c);}
.stat-num{font-size:26px;font-weight:800;color:var(--c);line-height:1.1;}
.stat-label{font-size:13px;font-weight:600;margin-top:7px;}
.stat-note{font-size:11.5px;color:var(--tx3);margin-top:5px;line-height:1.5;}
.tabs{display:flex;gap:8px;margin:30px 0 22px;position:sticky;top:0;z-index:5;padding:12px 0;background:linear-gradient(180deg,var(--bg) 60%,rgba(10,10,15,0));overflow-x:auto;}
.tab{flex:0 0 auto;display:inline-flex;align-items:center;gap:8px;padding:10px 18px;border-radius:100px;border:1px solid rgba(255,255,255,.08);background:var(--card);color:var(--tx2);font-family:inherit;font-size:13.5px;font-weight:600;cursor:pointer;transition:.18s;white-space:nowrap;}
.tab:hover{color:var(--tx);border-color:rgba(255,255,255,.2);}
.tab.active{color:#fff;background:linear-gradient(135deg,var(--cyan),var(--purple));border-color:transparent;box-shadow:0 8px 24px rgba(131,56,236,.35);}
.panel{display:none;animation:fade .35s ease;}
.panel.active{display:block;}
@keyframes fade{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:none;}}
.sec-head{margin:8px 0 18px;}
.sec-head .eyebrow{display:block;height:3px;width:44px;border-radius:2px;background:linear-gradient(90deg,var(--cyan),var(--purple));margin-bottom:12px;}
.sec-head h2{font-size:21px;font-weight:800;letter-spacing:-.01em;}
.lead{color:var(--tx);margin:0 0 18px;}
.lead p{color:var(--tx2);}
.card{background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:18px;padding:22px 24px;margin:0 0 16px;position:relative;transition:.2s;}
.card:hover{border-color:color-mix(in srgb,var(--c) 45%,transparent);transform:translateY(-2px);box-shadow:0 18px 40px rgba(0,0,0,.4);}
.card-head{display:flex;align-items:center;gap:11px;margin-bottom:6px;}
.card-head .dot{flex:0 0 auto;width:11px;height:11px;border-radius:50%;background:var(--c);box-shadow:0 0 14px var(--c);}
.card-title{font-size:16.5px;font-weight:700;line-height:1.4;}
.card-body{color:var(--tx2);}
.card-body p{margin:9px 0;}
.card-body strong,.lead strong{color:var(--tx);font-weight:700;}
p strong{color:var(--tx);}
code{font-family:ui-monospace,"SF Mono",Menlo,monospace;font-size:.86em;background:rgba(131,56,236,.14);color:#c4b5fd;padding:1px 6px;border-radius:6px;}
a{color:#5e7fff;text-decoration:none;word-break:break-all;}
a:hover{text-decoration:underline;}
ul,ol{margin:10px 0 12px;padding-left:22px;}
li{margin:5px 0;}
li::marker{color:var(--tx3);}
.callout{display:flex;gap:12px;background:linear-gradient(135deg,rgba(6,214,160,.09),rgba(131,56,236,.07));border:1px solid rgba(6,214,160,.25);border-radius:14px;padding:14px 16px;margin:14px 0;font-size:13.5px;color:var(--tx2);}
.callout i{color:var(--cyan);margin-top:3px;}
.table-wrap{overflow-x:auto;margin:16px 0;border-radius:14px;border:1px solid rgba(255,255,255,.08);}
table{border-collapse:collapse;width:100%;font-size:13px;min-width:520px;}
th{background:rgba(131,56,236,.16);color:#e9d5ff;text-align:left;padding:11px 13px;font-weight:700;white-space:nowrap;border-bottom:1px solid rgba(255,255,255,.08);}
td{padding:10px 13px;border-bottom:1px solid rgba(255,255,255,.05);color:var(--tx2);vertical-align:top;}
td strong{color:var(--tx);}
tbody tr:last-child td{border-bottom:none;}
tbody tr:hover td{background:rgba(255,255,255,.025);}
footer{margin-top:40px;padding-top:22px;border-top:1px solid rgba(255,255,255,.08);color:var(--tx3);font-size:11.5px;}
@media(max-width:760px){
 .wrap{padding:0 14px 60px;}
 .stats{grid-template-columns:repeat(2,1fr);}
 .card{padding:18px 16px;}
 .topbar .meta{width:100%;} .topbar .meta span{margin-left:0;margin-right:14px;}
}
"""

TPL = """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>美国电商流量与变现层 · 行业认知报告</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
<style>__CSS__</style></head><body>
<div class="bg-grid"></div><div class="bg-glow g1"></div><div class="bg-glow g2"></div>
<div class="wrap">
 <nav class="topbar">
   <span class="brand"><i class="fas fa-graduation-cap"></i> Industry Primer</span>
   <span class="meta"><span><i class="far fa-calendar"></i> 2026-07</span><span><i class="far fa-folder-open"></i> E-commerce · 流量与变现层</span><span><i class="fas fa-link"></i> __SRC__ 来源</span></span>
 </nav>
 <header class="hero">
   <div class="eyebrow-top"><i class="fas fa-book-open-reader"></i> 行业认知 · 看懂全貌</div>
   <h1>美国电商「流量与变现层」<br><span class="grad">行业认知报告</span></h1>
   <p class="sub">帮你"看懂行业"而非"告诉你该做什么"。数据窗口 2024–2025，每个关键数字标注来源与置信度；先分类后填充（MECE），行业结构为主体。点击下方标签分章阅读。</p>
   <div class="stats">__METRICS__</div>
 </header>
 <div class="tabs">__NAV__</div>
 __PANES__
 <footer>本报告为行业认知材料，非投资或经营建议；由多来源并行调研 + 交叉验证生成。所引第三方数据存在口径与时点差异（尤其私有公司营收、渠道占比为估算），关键决策前请以一手财报/付费报告交叉验证。</footer>
</div>
<script>
document.querySelectorAll('.tab').forEach(function(t){
 t.addEventListener('click',function(){
  document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('active');});
  document.querySelectorAll('.panel').forEach(function(x){x.classList.remove('active');});
  t.classList.add('active');
  document.getElementById('panel-'+t.dataset.tab).classList.add('active');
  window.scrollTo({top:document.querySelector('.tabs').offsetTop-8,behavior:'smooth'});
 });
});
</script></body></html>"""

out = (TPL.replace('__CSS__', CSS).replace('__METRICS__', metrics_html)
       .replace('__NAV__', ''.join(nav)).replace('__PANES__', '\n'.join(pane))
       .replace('__SRC__', str(src_count)))
OUT.write_text(out, encoding='utf-8')
print(f"OK -> {OUT}  ({len(out)} bytes, {len(nav)} tabs)")
