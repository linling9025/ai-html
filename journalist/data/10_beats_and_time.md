# 10 · 美国记者在写什么条线、时间花在哪里

## 覆盖范围、来源与局限

- **问题**：(A) 美国记者实际在跑哪些条线，分布如何；(B) 记者的时间花在哪些工作上，工作量多大。
- **群体**：LOCAL / TV / INDIE / NATL 全覆盖。FREE 只在 Pew 数据里间接出现（Pew 样本 28% 是自由撰稿人）。
- **自采数据（可复现）**：
  - 招聘 JD：新抓 1,135 条原始 JD，加上旧版原始数据 427 条（旧版分析保留了其中 366 条），去重和过滤后得到 **1,277 条近 12 个月的美国编辑部 JD**（发布日期 2025-11-17 至 2026-11-02，中位数 2026-10-07）。
    - 抓取脚本 `journalist/data/scripts/scrape_jobs_v2.py`，分类脚本 `journalist/data/scripts/beat_jobs.py`。
    - 原始数据 `journalist/data/raw/jobs_v2_*.jsonl`，分类结果 `jobs_v2_beats.jsonl`，统计 `jobs_v2_beat_stats.json`。
  - Report for America（RFA）岗位：2025–26、2026–27 两届共 **274 个去重后的地方驻点岗位**，每个岗位自带 "Beat:" 标签和 RFA 自己的主题 tag。数据在 `jobs_v2_rfa.jsonl`。
- **外部来源**：共 19 个，全部实际打开过：
  - 方法论调查：Pew 2022（topline 两版加全文）、Muck Rack 2024、2025、2026 和工作生活平衡 2025、American Journalist 2022、Tow Center 2021、Syracuse IDJC 2026、FT Strategies/WAN-IFRA 2026、PEJ 2002
  - 条线协会官网：SEJ、IRE、NASW、NAHJ、AAJA
  - 新闻报道：TVNewsCheck、Lynnwood Times、Poynter、CJR
  - Reddit 原帖若干条
- **主要局限**：
  1. **JD 样本严重偏 TV。** 1,277 条里 TV 有 858 条（67%），LOCAL 139、INDIE 33、NATL 212。
     - 原因是 TV 集团（Gray、Sinclair、Nexstar、TEGNA、Scripps、Fox、Hearst TV）都有可直接 GET 的 ATS 接口。
     - 地方报业两大集团 Gannett 和 Lee 用 Dayforce，接口返回 403，按规则放弃。Advance Local 用 ADP RTI，返回 "unsupported"。INN 职位板返回 403。CalMatters 当前没有开放职位。
     - 所以**各群体之间不能合并比较绝对量，只能分群体看结构**；"ALL" 列由 TV 主导，不代表整个行业。
  2. **JD 反映的是"正在招什么"（流量），不是"现在有多少人在跑什么"（存量）。** 存量要看 Pew 2022（JBEAT 题）。
  3. **Pew 是唯一有方法论的全美条线分布，但已是 2022 年数据**，而且是开放题人工编码成 11 类，粒度比本文的 19 类粗。
  4. **时间分配几乎没有美国本土、按任务拆分的量化调查。** 唯一按任务拆时间的是 FT Strategies/WAN-IFRA 2026：全球样本、43% 欧洲、由编辑部负责人估计"期望记者怎么分配时间"，不是记者自报。
  5. **规则分类有误差。** 人工核对 30 条，记录级完全正确 26/30（87%），详见 A1.4。

---

## A. 条线分布

### A1. 招聘 JD 的条线分布（自采，n=1,277）

#### A1.1 方法（口径）

**数据源**

| 来源 | ATS | 保留条数 | 群体 |
|---|---|---|---|
| Gray Media | UKG | 228 | TV |
| Sinclair | Oracle HCM | 198 | TV |
| TEGNA | Greenhouse | 149 | TV |
| journalismjobs.com（旧版） | 页面 JSON-LD | 145 | 混合 |
| Nexstar | Workday | 130 | TV（NewsNation → NATL） |
| Hearst | Oracle HCM | 110 | 按正文分 TV / LOCAL / 杂志 |
| Fox | Workday | 86 | 地方台 → TV，Fox News/Weather/LiveNOW → NATL |
| NYT（旧版） | Greenhouse | 51 | NATL |
| Dow Jones / NY Post | Workday | 45 | NATL |
| Scripps | Workday | 31 | TV |
| Washington Post | Workday | 16 | NATL |
| Cox | Workday | 15 | 按正文分 |
| Adams Publishing Group | ADP | 13 | LOCAL |
| MediaNews Group | Workday | 8 | LOCAL |
| Disney/ABC | Workday | 8 | KABC 等 → TV |
| McClatchy | UKG | 3 | LOCAL |
| States Newsroom | WordPress RSS | 2 | INDIE |
| Axios、Vox、Semafor、Insider、ProPublica、Hearst TV 等（旧版） | Greenhouse | 余下 | 多为 NATL |

**过滤**：每条排除记录都在 `jobs_v2_beats.jsonl` 里写明了原因。

| 排除原因 | 条数 |
|---|---|
| 跨源重复（同标题、同城市） | 132 |
| 非采编岗（技术制作、销售、营销等） | 62 + 26 |
| 超过 12 个月 | 13 |
| 非美国 | 17 + 15 |
| 学术、公关等行业 | 18 |

**角色**（从标题判断，n=1,277）：

| 记者 | 制片 | 编辑 | 主播/主持 | 摄影摄像 | 气象 | 实习/fellow | 其他 |
|---|---|---|---|---|---|---|---|
| 381 | 301 | 184 | 158 | 107 | 84 | 53 | 9 |

**条线判定**（多标签）：

1. **标题命中**条线词，记为强信号。
2. **正文命中**必须同时满足两个条件：
   - 句子不是模板套话。判定标准：同一句在 2 家以上雇主的 3 条以上 JD 中出现，或在同一雇主 60% 以上的 JD 中出现，就算模板。福利、EEO、城市宣传类句子也剔除。
   - 句子里条线词处在"报道语境"中，即"cover / report on / focus on … X"，或"X beat / coverage / reporter / news"。
3. 正文里像 style、features、market、energy、college、medical 这类歧义词不计入，因为在 JD 里它们多半指 AP style、特稿、电视市场、精力充沛、大学学历、医疗保险。
4. "综合/突发 GA" 只认明确说法（general assignment、variety of stories、cover breaking news 等）。
5. 什么都没写的记为 **"未指明"**，不并入 GA。
6. "调查/问责"是跨条线属性，单独作为 flag，不算条线。

#### A1.2 全部采编岗：各群体条线分布（多标签，所以列和超过 100%）

| 条线 | ALL n=1277 | LOCAL n=139 | TV n=858 | INDIE n=33 | NATL n=212 | 其他（杂志/电台/行业）n=35 |
|---|---|---|---|---|---|---|
| 未指明 | 710 (56%) | 38 (27%) | 553 (64%) | 15 (45%) | 85 (40%) | 19 (54%) |
| 综合/突发 GA | 192 (15%) | 33 (24%) | 118 (14%) | 2 (6%) | 33 (16%) | 6 (17%) |
| 政治/政府 | 91 (7%) | 30 (22%) | 19 (2%) | 10 (30%) | 29 (14%) | 3 (9%) |
| 天气/灾害 | 89 (7%) | 1 (1%) | 85 (10%) | 0 | 3 (1%) | 0 |
| 体育 | 83 (6%) | 25 (18%) | 54 (6%) | 1 (3%) | 3 (1%) | 0 |
| 文化/艺术/餐饮/生活 | 72 (6%) | 15 (11%) | 22 (3%) | 1 (3%) | 29 (14%) | 5 (14%) |
| 商业/经济 | 64 (5%) | 17 (12%) | 8 (1%) | 4 (12%) | 32 (15%) | 3 (9%) |
| 其他（国际、军事、族裔社群、数据等） | 33 (3%) | 0 | 14 (2%) | 2 (6%) | 17 (8%) | 0 |
| 科学/环境/气候 | 32 (3%) | 8 (6%) | 10 (1%) | 4 (12%) | 8 (4%) | 2 (6%) |
| 市政/地方政府 | 27 (2%) | 19 (14%) | 1 (0%) | 6 (18%) | 0 | 1 (3%) |
| 教育 | 22 (2%) | 17 (12%) | 2 (0%) | 2 (6%) | 1 (0%) | 0 |
| 法院/司法 | 21 (2%) | 7 (5%) | 9 (1%) | 0 | 5 (2%) | 0 |
| 治安 | 18 (1%) | 11 (8%) | 3 (0%) | 0 | 3 (1%) | 1 (3%) |
| 地产/住房 | 16 (1%) | 8 (6%) | 1 (0%) | 2 (6%) | 5 (2%) | 0 |
| 健康 | 12 (1%) | 2 (1%) | 3 (0%) | 3 (9%) | 1 (0%) | 3 (9%) |
| 选举 | 11 (1%) | 2 (1%) | 3 (0%) | 3 (9%) | 2 (1%) | 1 (3%) |
| 科技 | 9 (1%) | 1 (1%) | 1 (0%) | 1 (3%) | 6 (3%) | 0 |
| 交通 | 4 (0%) | 0 | 4 (0%) | 0 | 0 | 0 |
| 移民 | 0 | 0 | 0 | 0 | 0 | 0 |
| 宗教 | 0 | 0 | 0 | 0 | 0 | 0 |

TV 的"天气/灾害"主要来自 84 个气象岗。另有一个独立 flag：**TV 的 858 条 JD 中，140 条（16%）在正文里写了要参与"恶劣天气报道"**，这是全员职责，不是条线。

#### A1.3 只看记者类岗位（reporter / correspondent / MMJ / writer，n=381）

| 条线 | ALL n=381 | LOCAL n=77 | TV n=220 | INDIE n=19 | NATL n=53 |
|---|---|---|---|---|---|
| 未指明 | 181 (48%) | 10 (13%) | 149 (68%) | 7 (37%) | 12 (23%) |
| 综合/突发 GA | 79 (21%) | 24 (31%) | 38 (17%) | 1 (5%) | 11 (21%) |
| 政治/政府 | 54 (14%) | 21 (27%) | 10 (5%) | 9 (47%) | 12 (23%) |
| 体育 | 39 (10%) | 18 (23%) | 19 (9%) | 1 (5%) | 1 (2%) |
| 商业/经济 | 37 (10%) | 14 (18%) | 6 (3%) | 4 (21%) | 10 (19%) |
| 文化/艺术/餐饮/生活 | 27 (7%) | 8 (10%) | 7 (3%) | 1 (5%) | 9 (17%) |
| 市政/地方政府 | 19 (5%) | 13 (17%) | 1 (0%) | 4 (21%) | 0 |
| 教育 | 16 (4%) | 13 (17%) | 1 (0%) | 2 (11%) | 0 |
| 科学/环境/气候 | 15 (4%) | 4 (5%) | 2 (1%) | 2 (11%) | 5 (9%) |
| 治安 | 12 (3%) | 8 (10%) | 1 (0%) | 0 | 2 (4%) |
| 法院/司法 | 12 (3%) | 5 (6%) | 5 (2%) | 0 | 2 (4%) |
| 地产/住房 | 9 (2%) | 7 (9%) | 0 | 1 (5%) | 1 (2%) |
| 选举 | 6 (2%) | 1 (1%) | 0 | 3 (16%) | 1 (2%) |
| 健康 | 6 (2%) | 0 | 1 (0%) | 3 (16%) | 1 (2%) |
| 科技 | 3 (1%) | 1 (1%) | 0 | 0 | 2 (4%) |

ALL 列另含"其他（杂志/电台/行业）"12 条，此表未单列，所以 ALL 不等于四个群体之和。

- **没有任何专题条线的记者岗**（只写 GA 或什么都没写）：

  | 群体 | 无专题条线 | 占比 |
  |---|---|---|
  | TV | 175/220 | 80% |
  | NATL | 18/53 | 34% |
  | INDIE | 7/19 | 37% |
  | LOCAL | 18/77 | 23% |

- **条线数量**：有专题条线的记者岗里，111 条只标 1 个条线，57 条标 2 个，35 条标 3 个及以上。
- **"调查/问责"**作为标题出现 18 次，其中 TV 15 次，大多是 "Investigative Reporter"。在正文出现的比例：

  | 群体 | 正文提到调查/问责 |
  |---|---|
  | LOCAL | 22/77 |
  | TV | 49/220 |
  | INDIE | 11/19 |
  | NATL | 14/53 |

#### A1.4 人工核对 30 条（随机种子 20261103，`beat_jobs.py --sample 30`）

**记录级完全正确 26/30（87%）。** 4 条有问题：

| # | 岗位 | 问题 | 原因 |
|---|---|---|---|
| 1 | WaPo "Talent Producer, Opinions" | 应标"其他（评论版）"，判成了"未指明" | 分类表里没有"评论/观点"这一类 |
| 2 | Business Insider "Managing Producer, Vertical Video" | 只标了 GA，漏了商业和科技 | 正文写的是 "spanning business, technology"，"spanning" 不在报道动词表里 |
| 3 | Sinclair "Fact-Check Reporter/Producer" | 多标了"法院"，这是误报 | 正文的 "legal issues" 指报道中的法律风险，不是条线 |
| 4 | States Newsroom "Reporter, Florida Phoenix" | 判成"未指明"，实际是州政府 | RSS 摘要只有 70 字符，正文缺失 |

**其余 26 条判断正确。** 以 13 条"未指明"为例，人工复读正文，确认 JD 确实没有写专题条线：

- Gray Telemundo 双语 MMJ 只写了 "thrives on the thrill of breaking news"，可以算边界 GA。
- TEGNA 三条 "Multiskilled Journalist" 的正文命中句全是福利和 EEO 文字。

**误差方向**：主要是漏标（3/4），误报少（1/4）。因此**本表的专题条线占比是偏低的下限估计**，"未指明"偏高。另外，GA 和"未指明"之间的边界模糊，阅读时建议把两者合并看。

#### 发现条目

**10-01 | TV | S1/S6 | 综合/突发 | JD**
- **结论**：TV 记者岗基本不按专题条线招人。80% 的 TV 记者 JD 没有写任何专题条线，只要求"接受派题、追突发、自拍自剪、直播连线"。
- **证据**：
  - TV 记者类 JD 220 条，其中 175 条没有专题条线（68% 未指明，17% 只写 GA）。
  - Scripps WTXL 的 MMJ JD 写道："You'll be a one-person band—researching, shooting, writing, and editing"（你一个人就是一支队伍：调研、拍摄、写稿、剪辑）。
- **来源**：
  - 自采 JD，`beat_jobs.py`
  - 例：Scripps Multimedia Journalist, Thomas County — https://scripps.wd115.myworkdayjobs.com/en-US/Scripps_Careers — Scripps / 2026-10 — ✅（原始记录在 `jobs_v2_workday.jsonl`）

**10-02 | LOCAL | — | 政治、市政、教育、体育、商业 | JD**
- **结论**：地方报社招聘仍按经典条线划分。最常见的组合是"政府/政治 + 市政 + 教育"，其次是体育和商业。
- **证据**：LOCAL 记者 JD 共 77 条，只有 13% 没有写条线。各条线占比：

  | 综合/突发 GA | 政治/政府 | 体育 | 商业 | 市政 | 教育 | 治安 | 地产 | 法院 |
  |---|---|---|---|---|---|---|---|---|
  | 31% | 27% | 23% | 18% | 17% | 17% | 10% | 9% | 6% |

- **注意**：LOCAL 样本小（77 条），而且 Gannett 和 Lee 缺席，置信度中等。
- **来源**：自采 JD（journalismjobs、Hearst Newspapers、Adams、MNG、McClatchy）— ✅

**10-03 | INDIE | — | 政府/政治、市政、选举、健康 | JD + RFA**
- **结论**：非营利/独立媒体的岗位最集中在"政府问责"类条线，选举和健康的占比明显高于商业媒体。
- **证据**：
  - INDIE 记者 JD 只有 19 条：政治/政府 47%，市政 21%，商业 21%，选举 16%，健康 16%。
  - RFA 的 274 个地方岗位按 RFA 自己的 tag 统计：地方政府/城镇 36%，经济商业 22%，教育 19%，环境 19%，州政府 17%，健康 12%，移民 11%。此外"乡村" tag 有 77 个（28%）。
- **来源**：
  - 自采 JD
  - Report for America, Newsrooms — https://www.reportforamerica.org/newsrooms/?rfa_year=2026 — RFA / 2026 — ✅（另抓了 rfa_year=2025）

**10-04 | NATL | — | 商业、文化/生活、政治、国际 | JD**
- **结论**：全国媒体的 JD 条线分散在商业、文化生活、政治和国际几类，单一条线占比都不高。
- **证据**：NATL 采编岗 212 条中，商业 15%、文化/生活 14%、政治 14%、其他（国际、军事等）8%，未指明 40%（多为制片和编辑岗）。
- **来源**：自采 JD（NYT、WaPo、Dow Jones/NY Post、Fox News、Axios 等）— ✅

**10-05 | 全体 | — | 移民、宗教、交通、科技 | JD 对照 RFA**
- **结论**：移民和宗教在商业媒体的 JD 中完全没有出现，交通和科技也接近 0。这几个条线主要靠资助项目维持。
- **证据**：

  | 条线 | 1,277 条 JD | RFA 274 个岗位（按 RFA tag） |
  |---|---|---|
  | 移民 | 0 | 29 个（11%） |
  | 宗教 | 0 | 9 个（3%） |

- **来源**：同 10-03 — ✅

### A2. 有方法论的条线分布：Pew 2022 JBEAT 题（全美存量）

**10-06 | 全体（含 FREE） | — | 全部 | 调查**
- **结论**：按 2022 年全美记者的自报，最常跑的条线依次是政府与政治、文娱与旅游、经济与产业。约 1/10 没有固定条线。
- **证据**：Pew 2022 记者调查，JBEAT 题问的是"一个典型月里主要报道哪些领域"，开放题，最多写 3 个，事后人工编码。样本是报道型记者，N=9,192。结果：

  | 条线 | 占比 |
  |---|---|
  | 政府与政治 | 28% |
  | 文娱与旅游 | 27% |
  | 经济与产业 | 22% |
  | 健康 | 13% |
  | 犯罪与法律 | 11% |
  | 社会议题与政策 | 9% |
  | 教育与家庭 | 9% |
  | 地方与州 | 9% |
  | 体育 | 8% |
  | 环境与能源 | 8% |
  | 科学与技术 | 8% |
  | 其他具体条线 | 18% |
  | 综合/无特定主题 | 9% |
  | 未回答 | 9% |

- **来源**：PJ_2023.04.04_Journalist-Survey_TOPLINE — https://www.pewresearch.org/journalism/wp-content/uploads/sites/8/2023/04/PJ_2023.04.04_Journalist-Survey_TOPLINE.pdf — Pew / 2023-04（调查于 2022-02-16 至 03-17）— ✅ 已下载通读
- **注**：2022-06 发布的原版 topline 没有 JBEAT 题（已核对），条线数据是 2023-04 补发的。

**10-07 | FREE / 全体 | — | 文娱、科技、犯罪 | 调查**
- **结论**：条线和雇佣形态强相关。文娱旅游是唯一以自由撰稿人为主的条线，犯罪法律几乎全由在编员工跑。
- **证据**：
  - 文娱旅游条线中 57% 是自由职业或自雇，科学技术为 46%。
  - 犯罪法律条线中 87% 是全职或兼职员工。
  - 全样本 34% 是自由职业。
  - 性别分布：体育条线 83% 是男性，健康条线 64% 是女性。
- **来源**：U.S. journalists' beats vary widely by gender and other factors — https://www.pewresearch.org/short-reads/2023/04/04/us-journalists-beats-vary-widely-by-gender-and-other-factors/ — Pew / 2023-04-04 — ✅

**JD（流量）和 Pew（存量）对照**：两套口径不同，只能看方向。

- **文娱 / 生活类**：Pew 记者中 27% 跑这类条线，但 JD 里只占 6%（记者岗 7%）。
  - 原因：这个条线主要由自由撰稿人承担，编辑部很少为它招全职岗。
- **政府 / 政治类**：两边都居前。Pew 28%，JD 记者岗 14%，其中 LOCAL 27%、INDIE 47%。
- **健康**：Pew 13%，JD 只有 1–2%。
  - 健康类岗位主要出现在 INDIE（16%）和 RFA（12%），商业媒体很少单独招聘。

### A3. 其他条线规模参考

**10-08 | 全体 | S9 | 多条线 | 调查**
- **结论**：一人跑多条线是常态。按 Muck Rack 2022 的数据，记者平均跑 4 条线，一年前是 3 条。
- **证据**：
  - 平均跑 4 条线（上一年 3 条）。
  - 74% 的人还为网络和纸媒以外的形式供稿，其中 newsletter 17%、播客 15%。
  - 50% 每周发 5 篇以上，33% 每周发 8 篇以上。
  - 样本 2,547 人，调查于 2022-01-04 至 01-25，来自 Muck Rack 数据库，**偏向收公关稿的记者**。
- **来源**：
  - Survey: Journalists Covering More Beats… — https://tvnewscheck.com/journalism/article/survey-journalists-covering-more-beats-producing-content-for-more-than-one-medium/ — TVNewsCheck 转述 Muck Rack / 2022-03 — ✅
  - SPJ 和 BusinessWire 原文页：WebFetch 返回 403，curl 抓取被拦截后已放弃 `[未核实]`
- **补充**：Muck Rack 2024、2025、2026 的 State of Journalism 全文 PDF 都已下载核对，**都没有条线分布题**，只有 "pitch 是否与我的条线相关" 一类题。Muck Rack 的条线目录 https://muckrack.com/beats 列出 23 个主题，但不显示人数 ✅。

#### 条线协会会员规模（供给/市场数据，不是需求证据）

| 协会 | 条线 | 会员数 | 口径/年份 | 来源 | 状态 |
|---|---|---|---|---|---|
| IRE | 调查（跨条线） | 4,946 | 2024-10 数据 | https://www.ire.org/about-ire/ | ✅ |
| NAHJ | 族裔（跨条线） | "more than 3,500" 和 "4,000+"（同一页面两处说法不一） | 未注年份 | https://nahj.org/about/ | ✅（数字自相矛盾） |
| NASW | 科学 | 1,881 名正式会员，加 143 名 affiliate 和 241 名学生，共 2,265 | 官网现值 | https://www.nasw.org/page/about-national-association-science-writers-inc-0 | ✅ |
| AAJA | 族裔（跨条线） | "more than 1,600" | 官网现值 | https://www.aaja.org/about/ | ✅ |
| SEJ | 环境 | "more than 1,400"（含学者，美加两国） | 官网现值 | https://www.sej.org/about-sej | ✅ |
| AHCJ | 健康 | "more than 1,500" | 维基百科，无引用，无日期 | https://en.wikipedia.org/wiki/Association_of_Health_Care_Journalists | ⚠️ 二手 |
| SABEW | 商业 | "more than 2,000"（2010 年） | 维基百科，无引用 | https://en.wikipedia.org/wiki/Society_for_Advancing_Business_Editing_and_Writing | ⚠️ 二手、过旧 |
| EWA | 教育 | 官网 membership 和 about 页面都没有给数字 | — | https://ewa.org/membership | `[未核实]` |
| APSE | 体育 | 官网会员目录有密码保护，没有数字 | — | https://apsportseditors.com/ | `[未核实]` |
| RNA | 宗教 | 官网没有数字 | — | https://rna.org/about | `[未核实]` |

**读法**：

- 协会会员数和条线规模**不是一回事**。它只能说明"有多少人愿意为这个条线付会费、参加培训"。
- 环境、科学类协会会员大约 1,400–1,900 人，和 Pew 估算的环境 8%、科技 8% 量级大致相符：按 Pew 抽样框约 16 万人粗算，这个比例对应约 1 万人以上，可见只有一小部分加入协会。
- 这是数量级推算，**不能当作精确规模**。

---

## B. 时间分配与工作量

**10-09 | 全体（全球样本） | S1–S8 | — | 调查（负责人估计）**
- **结论**：目前唯一按任务拆分时间的调查显示，记者 38% 的时间花在生产环节，33% 花在发稿前的调研采访，发稿后的受众工作只占 11%，行政和会议占 9%。
- **证据**：FT Strategies × WAN-IFRA 的 Future Newsrooms Study 2026，问题是"在一个普通的周里，你预期记者如何分配时间"，n=402。

  | 环节 | 包含的任务 | 时间占比 | 对应本项目环节 |
  |---|---|---|---|
  | 发稿前 | 调研、背景分析、采访信源、外采、策划 | 33% | S1–S4 |
  | 生产 | 写作编辑、核查、多媒体制作、CMS 排版发布 | 38% | S5–S7 |
  | 发稿后 | 社群互动、受众反馈、数据复盘、标题优化 | 11% | S7–S8 |
  | 行政 | 编辑部会议、协作、报销、合规 | 9% | — |
  | 个人发展 | 新项目、培训、行业活动 | 9% | — |

  - 读者付费型编辑部的发稿前时间比平均多 5 个百分点，生产时间少 3 个百分点。
- **偏差**：样本是全球 448 家编辑部，覆盖 86 国，43% 在欧洲；答题人是编辑部负责人，给的是"期望"而不是记者实测。
- **来源**：Future Newsrooms Study 2026 第 29–30 页 — https://s3.amazonaws.com/media.mediapost.com/uploads/FT_WAN_IFRA_Future_Newsroom_Study_2026.pdf — FT Strategies / WAN-IFRA / Arc XP，2026（MediaPost 托管的 PDF 副本）— ✅ 已下载通读

**10-10 | 全体（以美国为主） | S9 | — | 调查**
- **结论**：多数全职记者每周工作超过 40 小时，超过八成每周都有下班后加班。稿量差异很大，大约 1/4 的人每周 10 篇以上。
- **证据**：
  - **Muck Rack 2025 工作生活平衡调查**（2025-01-02 至 02-17 收到 432 份，有效 408 份，主要是美国记者）：
    - 67% 的全职记者周工时超过 40 小时，17% 超过 51 小时。
    - 83% 每周至少一次在非工作时间工作，21% 一周超过 5 天如此。
    - 48% 每周写 4 篇以上，约 1/4 每周 10 篇以上。
    - 稿量图各档的数值抽取后对不上（加总只有 90%），所以只引用报告的文字结论。
  - **Muck Rack 2024**（1,106 人，北美占 60%）：
    - 全职记者周工时：41–50 小时占 51%，51 小时以上 13%，25–40 小时 35%。
    - 每周发稿量：1 篇 17%，2–4 篇 29%，5–7 篇 22%，8–10 篇 10%，11 篇以上 22%。
    - 79% 每周至少一天下班后工作。
- **来源**：
  - The State of Work-Life Balance in Journalism 2025 第 17–19、32 页 — https://media.muckrack.com/documents/3.17.2025_SoWLB_-_journo_report.pdf — Muck Rack / 2025-03 — ✅
  - State of Journalism 2024 第 10–15、37 页 — https://media.muckrack.com/documents/Muck_Rack_-_State_of_Journalism_2024.pdf — Muck Rack / 2024-03 — ✅

**10-11 | 全体 | S6/S7 | — | 调查**
- **结论**：一稿多发、多平台是常态。主要媒介是数字，但多数人的稿件还会再出现在纸媒、电视或电台。
- **证据**：Muck Rack 2024 数据：
  - 主要媒介：数字 69%，纸媒 19%，电视 4%。
  - 66% 的人稿件另外还以传统媒体形式发布。
  - 平均每篇稿件额外出现在约 2 种媒介上。
- **来源**：同 10-10 的 Muck Rack 2024，第 14–15 页 — ✅

**10-12 | LOCAL | S6/S7/S9 | — | 调查（2020 年）**
- **结论**：小型地方报社员工普遍一人多岗，工时长，产出持续增加。
- **证据**：Tow Center 调查了 324 名发行量 5 万以下报社的员工，2020 年 8–9 月进行，自选样本：
  - 50% 每周工作 40–50 小时，37% 工作 50–60 小时。
  - 49% 说过去三年个人发稿量增加了。
  - 54% 同时做纸媒和数字。
  - 57% 花在数字上的时间比三年前多。
  - 受访者原话："the necessity to wear several hats, while only getting paid for one job"（必须身兼数职，却只拿一份工资）。
- **来源**：Life at Local Newspapers in a Turbulent Era — https://www.cjr.org/tow_center_reports/life-at-local-newspapers-in-a-turbulent-era-findings-from-a-survey-of-more-than-300-newsroom-employees-in-the-united-states.php — Tow Center/CJR / 2021-10（数据 2020）— ✅

**10-13 | TV | S1/S6 | 综合 | JD + 调查**
- **结论**：TV 记者的时间被"每天出片 + 直播 + 自拍自剪 + 被派题"占满。这种工作量结构至少从 2002 年起就已存在。
- **证据**：
  - 自采 TV 记者类 JD（n=220）中的任务提及率：

    | 被派题/突发 | 直播连线 | 自拍自剪 | 社交媒体 | 夜班/周末 | 网站稿 | 拍照 | 编辑部会议 |
    |---|---|---|---|---|---|---|---|
    | 75% | 79% | 77% | 64% | 52% | 48% | 36% | 14% |

  - PEJ 2002（调查了 103 位新闻总监）：记者被要求平均每天做 1.8 条成片（package），是五年来最高。
- **来源**：
  - 自采 JD — ✅
  - Local TV 2002 study — https://www.pewresearch.org/wp-content/uploads/sites/8/legacy/Local_TV_2002_study.pdf — PEJ / 2002 — ✅（2002 年，只作历史参照）

**10-14 | 各群体 | S1–S9 | — | JD**
- **结论**：各群体记者 JD 要求的工作内容差异很大：
  - TV 是视频生产与直播
  - LOCAL 是拍照、社交媒体、newsletter 和公共记录
  - INDIE 是公共记录、夜班周末和音频
  - NATL 是音频/播客和数据
- **证据**：记者类 JD 任务提及率（n=381，正文已去除模板套话）：

  | 任务 | LOCAL n=77 | TV n=220 | INDIE n=19 | NATL n=53 |
  |---|---|---|---|---|
  | 社交媒体发布 | 60% | 64% | 47% | 51% |
  | 突发/被派题 | 48% | 75% | 42% | 57% |
  | 夜班/周末/待命 | 31% | 52% | 53% | 26% |
  | 拍照 | 36% | 36% | 37% | 2% |
  | 网站/数字稿 | 21% | 48% | 11% | 8% |
  | Newsletter | 22% | 0% | 16% | 17% |
  | 公共记录/FOIA | 21% | 11% | 37% | 9% |
  | 音频/播客 | 9% | 9% | 26% | 49% |
  | 数据分析 | 4% | 5% | 11% | 13% |
  | 参加公共会议（措辞须含 "meeting"） | 8% | 0% | 16% | 0% |
  | 写明具体稿量 | 6% | 0% | 11% | 4% |

  - JD 中写明的稿量原文例子："3 to 5 stories a day"（LOCAL，2 条）、"10 stories each week"（LOCAL）、"three stories per day"（INDIE）、"multiple stories a day"（NATL）。
- **口径**：
  - 提及率说明"招聘方认为这是岗位职责"，**不等于时间占比**。
  - "参加公共会议"一项用的是严格措辞，所以低于 04 号报告用宽口径（提到 city council 即算）得到的比例。
- **来源**：自采 JD，`beat_jobs.py` 的任务表 — ✅

**10-15 | INDIE | S8/S9 | — | 调查**
- **结论**：独立出版人的时间被商业运营挤占。"平衡新闻工作和商业运营"是第二大挑战，倦怠是第一大。
- **证据**：Syracuse IDJC 2026 年春夏调查，联系了 277 家，112 位出版人作答，覆盖 37 州和 DC：
  - 51.9% 把"平衡新闻工作与商业运营"列为最大挑战之一。
  - 超过 55% 选了倦怠与可持续性，在拥有 100–500 名付费订户的出版人中这一比例高达 77.3%。
  - 21.8% 把"突破一人运营"列为最大财务挑战。
  - Evanston Now 的 Bill Smith 说："I'm the editor, I'm the publisher, I'm the ad salesperson … and the janitor at this point."（我是编辑、出版人、广告销售……现在还是清洁工。）
- **来源**：A Hard Reality: Independent Local Journalism in the United States（全文 PDF）— https://idjc.syracuse.edu/wp-content/uploads/A-Hard-Reality-Full-Report.pdf — Syracuse IDJC / 2026-10 — ✅；Poynter 报道 https://www.poynter.org/business-work/2026/independent-local-newsrooms-sustainability-business-models/ ✅

**10-16 | LOCAL | S6/S9 | — | 记者/工会原话**
- **结论**：有连锁报业把工资和稿量配额挂钩，日配额 2–3 篇。
- **证据**：
  - Everett Herald（Carpenter Media）的工会称，记者被要求每天写 2–3 篇，完不成就可能拿不到每小时 1 美元的加薪。
  - 工会原话："Tying wages to ridiculous story quotas punishes journalists"（把工资和荒唐的稿量配额挂钩，是在惩罚记者）。
- **来源**：Lynnwood Times — https://lynnwoodtimes.com/2024/12/06/everett-herald-low-wages/ — 2024-12-06 — ✅

**10-17 | 全体 | S3/S4 | — | 调查**
- **结论**：记者和信源打交道主要靠邮件和电话，面对面极少。社交媒体主要用于推广稿件和找信源。
- **证据**：Pew 2022，报道型记者 N=9,192：
  - 和信源最常用的沟通方式：邮件 42%，电话 33%，短信 8%，视频会议 7%，面对面 4%，社交媒体 4%。
  - 认为社交媒体对"推广稿件"有正面影响的占 86%，对"找信源"有正面影响的占 78%。
- **来源**：Pew 2022 topline（同 10-06）— ✅

**10-18 | 全体 | S1/S7 | — | 调查**
- **结论**：社交媒体占用大量工作时间。2022 年约六成记者每天花在工作相关社交媒体上的时间超过 1 小时。
- **证据**：American Journalist Study 2022，n=1,600，从媒体名录随机抽样，回复率 11%：
  - 59.3% 每天工作相关的社交媒体使用超过 1 小时。
  - 用社交媒体看突发 87.4%，找选题 74.3%，找信源 66.7%。
- **来源**：Key Findings From The 2022 American Journalist Study — https://www.theamericanjournalist.org/post/american-journalist-findings — Willnat 等 / 2022 — ✅

**10-19 | LOCAL / TV / NATL | S6/S7/S9 | — | 记者原话（Reddit）**
- **结论**：记者的原话里，时间主要被四类事务吞掉：缺人后的一人包办，SEO 与平台要求，竖屏视频配额，以及转写修正。
- **证据**：
  - **一人包办**：一名入行一年的地方记者在编辑离职后独自撑起报纸，每周 12 篇以上稿件，外加排版、开会、拍照、编辑、来信、活动和突发，每周约 55 小时。原话："I'm drowning"（我快淹死了）。
  - **SEO 与平台要求**：一名生活类记者说开会讨论怎么写，比实际写稿的时间还多："I spend more time in meetings about how to write than actually writing"（我花在"怎么写"的会上的时间比写稿还多）。
  - **竖屏视频配额**：TV 从业者说 TEGNA 给编辑和派题台也定了竖屏视频配额。
  - **转写修正**："spending more time fixing transcripts than actually reading them"（修转写稿的时间比读它的时间还多）。
  - **新人稿量预期**：一名乡村驻点新记者被要求每周写 3–6 篇，而且要自己出选题。
- **来源**（均为本项目已抓取的 Reddit 原帖，正文存于 `raw/reddit_posts.jsonl`；直接用 curl 打开会被 Reddit 返回 403）：
  - https://www.reddit.com/r/Journalism/comments/1r6vr4u/ — 2026-02-17 ✅
  - https://www.reddit.com/r/Journalism/comments/1mk5s9r/ — 2025-08-07 ✅
  - https://www.reddit.com/r/Broadcasting/comments/1palbbn/ — 2025-11-30 ✅
  - https://www.reddit.com/r/Journalism/comments/1vvasw7/ — 2026-08-22 ✅
  - https://www.reddit.com/r/Journalism/comments/1quwks6/ — 2026-02-03 ✅

**10-20 | FREE | S8/S9 | — | 调查（2015 年）**
- **结论**：调查型自由撰稿人有大量时间花在找钱和行政事务上。
- **证据**：只有 34% 的受访者用在追稿上的时间多于用在业务和行政上的时间。30% 每年自掏腰包补贴报道超过 5,000 美元。样本是 250 多名自由撰稿人，全球非科学抽样，由 IRE 下属的 Project Word 发起。
- **来源**：CJR — https://www.cjr.org/behind_the_news/new_survey_reveals_everything.php — 2015-02-17 — ✅（2015 年，只作参照）

---

## 竞品 / 工具表（本范围内出现的）

| 工具/资源 | 解决什么 | 群体 | 价格/付费方 | 状态 | 来源 |
|---|---|---|---|---|---|
| Muck Rack 条线目录 | 按条线找记者（面向公关方） | 公关方使用，记者是被检索对象 | 公关方付费；记者免费建档 | 运营中，不公开人数 | https://muckrack.com/beats ✅ |
| Report for America | 资助地方岗位，按条线设岗 | LOCAL / INDIE | 基金会和本地合作方出资 | 2025–27 两届共 274 个岗位 | https://www.reportforamerica.org/newsrooms/?rfa_year=2026 ✅ |
| Otter 等转写工具 | 会议和采访转写（S4） | 全体 | 订阅制 | 用户抱怨长会议转写质量差 | Reddit 1vvasw7 ✅ |
| 各 TV 集团 ATS（Workday、UKG、Oracle、Greenhouse） | 招聘（只作为本研究的数据源） | — | — | — | 见 A1.1 |

本范围（条线与时间）**没有发现直接面向"条线管理"或"记者时间管理"的专门工具**。条线是编辑部的人事安排，时间压力靠加班和一人多岗消化。

---

## 能自己解决 / 不好解决（本范围）

| 需求 | 凑合方案 | 判定 | 证据 |
|---|---|---|---|
| 一人跑多条线、条线经常变 | 靠加班；新人自己摸索选题来源（Facebook 群等） | ⚠️ | 10-08、10-19 |
| TV 被派题加每日出片 | 派题台派题，记者一人拍写剪，再加直播 | ⚠️ 费力，但已制度化 | 10-01、10-13 |
| 小报社缺人后的整报运营 | 一人包办，每周 55 小时 | ❌ | 10-12、10-19 |
| 独立出版人兼顾商业运营 | 雇自由撰稿人、靠配偶收入、硬扛 | ❌ | 10-15 |
| 发稿后的受众工作（S8） | 时间只剩约 11% | ⚠️ 负责人自己承认投入不足 | 10-09 |
| 稿量配额压力 | 工会谈判、写短稿 | ❌ | 10-16 |
| 移民、宗教、交通等冷门条线 | 依赖 RFA 等资助岗位 | ❌ 商业媒体几乎不招这类岗位 | 10-05 |
| 转写修正 | 手工修稿 | ⚠️ | 10-19 |

## 最重要的 5 条发现

1. **"条线"在 TV 几乎不存在。** 80% 的 TV 记者 JD 没有专题条线，记者的工作是"被派题 + 直播 + 自拍自剪"。条线概念主要适用于 LOCAL、INDIE 和 NATL（10-01、10-13）。
2. **全美存量（Pew 2022）的前三大条线是政府政治 28%、文娱旅游 27%、经济产业 22%。** 但文娱是自由撰稿人的天下（57% 是自由职业），编辑部招聘里文娱只占约 6%（10-06、10-07）。
3. **地方报社的经典条线组合是"政府 + 市政 + 教育 + 体育 + 商业"。** 非营利媒体更偏政府问责、选举和健康（10-02、10-03）。
4. **时间结构**：编辑部负责人估计记者 38% 的时间花在生产，33% 在调研采访，只有 11% 在发稿后的受众工作。记者自报的情况是：67% 的全职记者周工时超过 40 小时，83% 每周有下班后加班，约 1/4 每周 10 篇以上（10-09、10-10）。
5. **商业运营和一人多岗正在吃掉报道时间。** 51.9% 的独立出版人把平衡新闻与商业列为最大挑战之一，小报社和独立媒体普遍是一人包办（10-12、10-15、10-19）。

## 证据薄弱处

- **LOCAL 和 INDIE 的 JD 样本小**：分别为 139 和 33 条，记者岗只有 77 和 19 条。Gannett、Lee、Advance Local 的 ATS 无法直接获取，地方报业 JD 的代表性不足。
- **没有美国本土、记者自报、按任务拆分的时间调查。** FT/WAN-IFRA 是全球样本加负责人估计。Muck Rack 只给总工时和稿量，而且样本偏向收公关稿的人。
- **Pew 的条线数据是 2022 年的**，开放题编码成 11 类，没有"市政"、"天气"、"交通"、"移民"等细类，不能直接和本文的 19 类对齐。
- **JD 规则分类偏保守**（漏标多于误报，核对精度 87%），所以专题条线占比应看作下限。
- **条线协会规模**：EWA、APSE、RNA 官网没有会员数；AHCJ 和 SABEW 只有维基百科的无引用数字。
