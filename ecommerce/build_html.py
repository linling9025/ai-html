#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将本报告 Markdown 转为暗色卡片 + 顶部 Tab 分章的可分享 HTML。
对标 /Users/linling/Documents/code/ai/ai-html 的风格（Outfit + 霓虹渐变 + 卡片）。
改了 md 后重跑 `python3 build_html.py` 即可同步更新 HTML。"""
import re, html
from pathlib import Path

SRC = Path(__file__).parent / "美国电商流量与变现层调研报告.md"
OUT = Path(__file__).parent / "美国电商流量与变现层调研报告.html"

ACCENTS = ['#06d6a0', '#8338ec', '#ff006e', '#3a86ff', '#22c55e', '#fb5607', '#fbbf24']

# 每个 ## 章节归入哪个 tab（关键词匹配）→ (tab_id, tab_label, icon)
def tab_of(h2):
    t = h2
    if '执行摘要' in t or '行业速览' in t: return ('overview', '概览', 'fa-compass')
    if t.startswith('1.') or '变现模式' in t: return ('models', '变现模式', 'fa-coins')
    if t.startswith('2.') or '竞品' in t: return ('competitors', '竞品拆解', 'fa-chess')
    if t.startswith('3.') or '分发平台' in t: return ('platforms', '平台地图', 'fa-diagram-project')
    if t.startswith('4.') or '品类' in t: return ('categories', '品类矩阵', 'fa-layer-group')
    if t.startswith('5.') or '综合建议' in t: return ('strategy', '综合建议', 'fa-flag-checkered')
    return ('sources', '来源 & 方法', 'fa-book-open')

TAB_ORDER = ['overview', 'models', 'competitors', 'platforms', 'categories', 'strategy', 'sources']

def inline(text):
    text = html.escape(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'(https?://[^\s)）]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return text

def render_blocks(lines):
    """把不含标题的内容行渲染为 HTML（表格/列表/引用/段落）。"""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'^---+\s*$', line) or line.strip() == '':
            i += 1; continue
        # 表格
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
        # 引用块 → callout
        if line.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i].lstrip('>').strip()); i += 1
            out.append(f'<div class="callout"><i class="fas fa-triangle-exclamation"></i><div>{inline(" ".join(buf))}</div></div>')
            continue
        # 无序列表
        if re.match(r'^\s*[-*] ', line):
            out.append('<ul>')
            while i < len(lines) and re.match(r'^\s*[-*] ', lines[i]):
                out.append(f'<li>{inline(re.sub(r"^\s*[-*] ", "", lines[i]))}</li>'); i += 1
            out.append('</ul>'); continue
        # 有序列表
        if re.match(r'^\s*\d+\. ', line):
            out.append('<ol>')
            while i < len(lines) and re.match(r'^\s*\d+\. ', lines[i]):
                out.append(f'<li>{inline(re.sub(r"^\s*\d+\. ", "", lines[i]))}</li>'); i += 1
            out.append('</ol>'); continue
        out.append(f'<p>{inline(line.strip())}</p>'); i += 1
    return '\n'.join(out)

# ---- 解析 markdown 为 tab → segments ----
md = SRC.read_text(encoding='utf-8')
lines = md.split('\n')

panels = {}          # tab_id -> list of segments
tab_meta = {}        # tab_id -> (label, icon)
cur_tab = None
seg_buf = []
segments = []        # segments of current tab

def flush_content():
    global seg_buf
    if seg_buf:
        segments.append(('content', seg_buf)); seg_buf = []

def start_tab(tid):
    global segments, cur_tab
    if cur_tab is not None:
        flush_content(); panels[cur_tab] = panels.get(cur_tab, []) + segments
    segments = panels.get(tid, [])[:] if tid in panels else []
    # 若之前已存 panel，取回续写
    if tid in panels:
        segments = panels[tid]; panels[tid] = segments  # same ref
    cur_tab = tid

for line in lines:
    if line.startswith('# ') and not line.startswith('## '):
        continue  # 跳过 H1
    if line.startswith('## '):
        h2 = line[3:].strip()
        tid, label, icon = tab_of(h2)
        if tid not in tab_meta: tab_meta[tid] = (label, icon)
        # 切换/进入该 tab
        flush_content()
        if cur_tab is not None:
            panels[cur_tab] = segments
        cur_tab = tid
        segments = panels.setdefault(tid, [])
        segments.append(('h2', h2))
        continue
    if line.startswith('#### '):
        flush_content(); segments.append(('card', line[5:].strip())); continue
    if line.startswith('### '):
        flush_content(); segments.append(('card', line[4:].strip())); continue
    seg_buf.append(line)
# 收尾
flush_content()
if cur_tab is not None:
    panels[cur_tab] = segments

# ---- 渲染每个 panel ----
def render_panel(tid):
    segs = panels.get(tid, [])
    out = []
    open_card = False
    ci = 0
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
        else:  # content
            body = render_blocks(val)
            if body.strip():
                out.append(body if open_card else f'<div class="lead">{body}</div>')
    close()
    return '\n'.join(out)

# ---- 组装 tab 导航 + 面板 ----
nav, pane = [], []
for idx, tid in enumerate(TAB_ORDER):
    if tid not in tab_meta: continue
    label, icon = tab_meta[tid]
    active = ' active' if idx == 0 else ''
    nav.append(f'<button class="tab{active}" data-tab="{tid}"><i class="fas {icon}"></i>{label}</button>')
    pane.append(f'<section class="panel{active}" id="panel-{tid}">{render_panel(tid)}</section>')

METRICS = [
    ("$136亿", "2024 美国联盟营销广告支出", "北美 16% 电商交易由联盟驱动", "#06d6a0"),
    ("8.1/10", "最优打法综合评分", "数据驱动 Deal 聚合引擎 + 多渠道分发", "#8338ec"),
    ("$90亿", "TikTok Shop 美国 2024 GMV", "同比 +650%，但受地缘政策悬顶", "#ff006e"),
    ("仅 4 个", "可直挂联盟裸链的渠道", "Pinterest / Threads / 自建站 / Newsletter", "#3a86ff"),
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
.callout{display:flex;gap:12px;background:linear-gradient(135deg,rgba(251,86,7,.09),rgba(255,0,110,.06));border:1px solid rgba(251,86,7,.28);border-radius:14px;padding:14px 16px;margin:14px 0;font-size:13.5px;color:var(--tx2);}
.callout i{color:var(--orange);margin-top:3px;}
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
<title>美国电商流量与变现层 · 深度调研</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
<style>__CSS__</style></head><body>
<div class="bg-grid"></div><div class="bg-glow g1"></div><div class="bg-glow g2"></div>
<div class="wrap">
 <nav class="topbar">
   <span class="brand"><i class="fas fa-bolt"></i> Deep Research</span>
   <span class="meta"><span><i class="far fa-calendar"></i> 2026-07</span><span><i class="far fa-folder-open"></i> E-commerce Monetization</span><span><i class="fas fa-link"></i> __SRC__ 来源</span></span>
 </nav>
 <header class="hero">
   <div class="eyebrow-top"><i class="fas fa-chart-pie"></i> 面向决策 · 以"适不适合你"为尺子</div>
   <h1>美国电商「流量与变现层」<br><span class="grad">深度调研与打法排行</span></h1>
   <p class="sub">数据窗口 2024–2025。打分权重：数据抓取契合 30% · 冷启动 25% · 联盟政策 20% · 护城河 15% · 天花板 10%。点击下方标签分章阅读。</p>
   <div class="stats">__METRICS__</div>
 </header>
 <div class="tabs">__NAV__</div>
 __PANES__
 <footer>本报告由多 Agent 并行调研 + 交叉验证生成；打分为基于既定权重的主观量化估计，用于横向排序而非绝对判断。涉及税务/合规内容属一般性信息，非持牌意见。所有抓取行为须遵守各站服务条款与当地法律。</footer>
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
