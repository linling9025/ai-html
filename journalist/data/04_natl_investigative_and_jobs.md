# 04 全国/调查记者（NATL）+ 招聘 JD 量化分析（跨群体）

## 0. 覆盖范围 / 来源数 / 主要局限

**覆盖范围**
- **A 部分（NATL）**：FOIA 延迟与积压（DOJ OIP 年报摘要、OGIS 年报、NYT 分析、MuckRock 数据）、法律风险（RCFP anti-SLAPP 指南、RCFP Local Legal Initiative、Press Freedom Tracker 传票数据）、信源保护与数字安全（FPF 2025 年数字、Pew 2015 IRE 会员调查）、调查记者用 AI（Tow Center 2024 报告、ProPublica 2025 方法论、NICAR 2024–2026 会议议程量化）、数据新闻工具供给（Pinpoint、Big Local News、Agenda Watch、DocumentCloud）。
- **B 部分（JD 量化，跨全部群体）**：抓取 427 条近期 JD，剔除 61 条后分析 **366 条**，按群体粗分并统计 31 个职责关键词族出现率，映射到 S1–S9。

**来源数**：A 部分实际访问并引用的网页/文件共 22 个（✅20，⚠️2：FOIA Advisor 转述的 NYT 分析、Agenda Watch 仅登录页）；打不开的单独列出。B 部分为 2 个招聘源的原始抓取数据（366 条 JD，每条带 URL）+ NICAR 官方议程 JSON 3 份。

**可复现文件**
| 文件 | 内容 |
|---|---|
| `journalist/data/scripts/scrape_jobs.py` | 抓取 journalismjobs.com 全量列表（3 页×100）+ 详情页 JSON-LD；Greenhouse 公开 API 8 家新闻机构，按标题过滤编辑岗 |
| `journalist/data/scripts/analyze_jobs.py` | 去样板句、排除、分群、关键词族正则、输出统计表（所有口径写在文件头注释和下文 §B.1） |
| `journalist/data/scripts/kw_snippets.py` | 打印任一关键词族的命中上下文，用于人工审计正则精度：`venv/bin/python journalist/data/scripts/kw_snippets.py scanner` |
| `journalist/data/scripts/nicar_sessions.py` | 下载 NICAR 2024/2025/2026 官方议程 JSON 并按主题计数 |
| `journalist/data/scripts/press_freedom_tracker_counts.py` | Press Freedom Tracker CSV 导出计数（仅 2023 成功，见局限） |
| `journalist/data/raw/jobs_journalismjobs.jsonl` (206) / `jobs_greenhouse.jsonl` (221) | 原始 JD，含 URL、全文 |
| `journalist/data/raw/jobs_classified.jsonl` (427) | 每条 JD 的群体、排除原因、命中关键词 |
| `journalist/data/raw/jobs_keyword_stats.json` | 全部统计数字（含分子/分母） |
| `journalist/data/raw/nicar_202{4,5,6}_schedule.json`, `nicar_topic_counts.json` | NICAR 议程原始数据与计数 |

复现：`cd ai-spider && venv/bin/python journalist/data/scripts/scrape_jobs.py && venv/bin/python journalist/data/scripts/analyze_jobs.py && venv/bin/python journalist/data/scripts/nicar_sessions.py`（重抓会得到新的 JD 快照；本文数字对应 2026-11-03 抓取的 raw 文件，直接跑 `analyze_jobs.py` 即可复现）。

**主要局限**
1. **WebSearch 配额在本轮被耗尽**（共享上限），A 部分后半段只能访问已知/站内可导航的 URL，GIJN（Cloudflare 403）、MuckRock 官网（403）、DocumentCloud（连接拒绝）、justice.gov（连接重置）、Muck Rack State of Journalism（CF 403）、AP 生成式 AI 报告（404）均未能直接核实。DOJ 数字通过 FOIA Advisor 对 OIP 原文的转载核实；MuckRock 数字通过 News/Media Alliance 引用 MuckRock 的信息图核实。
2. **Press Freedom Tracker 2024–2026 年度导出被 Cloudflare 质询拦截**，本文没有绕过，只用了站内类别页的累计数。
3. **JD 样本结构偏差**：TV 组 93 条中 75 条来自 Hearst Television 一家（Greenhouse）；NATL 组 91 条中 63 条来自 NYT，且 NYT 在招的多是视频/图表岗，**NATL 组不等于"调查记者"**。INN、Poynter、TVJobs、Indeed、LION 招聘页均不可访问（403/超时/无法解析/404），mediabistro 分页需逆向未做。
4. 关键词统计是**正则"出现/未出现"**，不是语义理解；已去掉在 ≥3 条 JD 中逐字重复的句子（EEO、公司介绍、福利），这会**低估**模板化写进同一雇主多条 JD 的职责（如 Hearst TV 的"夜班/周末"模板句）。各族精度可用 `kw_snippets.py` 抽查；已知假阳性见 §B.1。
5. JD 是"雇主写的期待"，属于需求信号中的"招聘 JD 工作描述"，但反映的是编辑部要求记者做什么，不直接等于记者本人想要什么工具。

---

## A. 全国 / 调查记者（NATL）

### A1 FOIA：请求量创新高，积压与等待同步恶化

**`A1-01` | NATL（亦影响 LOCAL/INDIE）| S2 背景研究 | 市场数据**
- 结论：联邦 FOIA 请求量 FY2025 再创纪录，系统负载在升，不是在降。
- 证据：FY2025 联邦政府收到 1,707,197 件 FOIA 请求（较 FY2024 +13.7%），处理 1,635,055 件（创纪录）；行政申诉收到 32,059 件（+59.38%）。原文："the government received another record-setting 1,707,197 requests during FY 2025"（政府在 FY2025 又收到创纪录的 1,707,197 件请求）。
- 来源：FOIA News: OIP publishes summary of agency annual reports — https://www.foiaadvisor.com/foia-blog/2026/7/2/foia-news-oip-publishes-summary-of-agency-annual-reports — FOIA Advisor 转载 DOJ OIP *FOIA Post*，2026-07-02 — ✅（DOJ 原文 https://www.justice.gov/oip/blog/summary-fiscal-year-2025-annual-foia-reports-published ❌ 连接被重置）

**`A1-02` | NATL | S2 | 市场数据**
- 结论：处理 FOIA 的人在减少、积压在增加——人手下降 16%，积压上升 27%。
- 证据：15 个内阁部门 + 10 个独立机构的全职 FOIA 人员 FY2024→FY2025 下降 16%，积压"increased 27 percent"（上升 27%）；教育部人手 -54%、财政部 -39%、退伍军人事务部 -36%。FY2025 OGIS 收到 6,061 件求助；"预计完成日期"（EDC）问题被称为"symptom of larger delay issue"（更大延误问题的症状）。
- 来源：OGIS 2026 Annual Report for FY 2025 — https://www.archives.gov/ogis/about-ogis/annual-reports/ogis-2026-annual-report-for-fy-2025 — 国家档案馆 OGIS，2026 — ✅

**`A1-03` | NATL | S2 | 市场数据**
- 结论：联邦积压约 34 万件、平均等待 >240 天、全部或部分公开率 47% 为 2010 年以来最低。
- 证据：截至 2025-09-30 逾期请求"nearly 340,000"；待决请求者平均等待"longer than 240 days"（法定 20 天）；文件全部或部分公开率 47%，至少 2010 年以来最低（NYT 分析）。
- 来源：FOIA News: NYT report on FOIA requests in limbo or unfulfilled — https://www.foiaadvisor.com/foia-blog/2026/7/29/foia-news-nyt-report-on-foia-requests-in-limbo-or-unfulfilled — FOIA Advisor（Ryan Mulvey）转述 NYT（Minho Kim）2026-07-29 — ⚠️（转载页已访问；NYT 原文 https://www.nytimes.com/2026/07/29/us/politics/record-numbers-of-public-document-requests-are-in-limbo-or-unfulfilled.html 付费墙未核实）

**`A1-04` | NATL/LOCAL/INDIE/FREE | S2 | 需求信号（已发生的使用行为）+ 凑合方案的失败率**
- 结论：在 MuckRock 上提交的联邦请求，平均 276 天才有回应，只有约 27% 成功拿到新信息——记者提 FOIA 本身就是高成本、低命中的"凑合方案"。
- 证据：MuckRock 数据：法定 20 天 vs 实际平均 276 天；"Only 26.60 percent of FOIA requests are successful"（仅 26.60% 的请求成功获得新信息）；平台上联邦请求总数 46,779（信息图同时列出 13,051 / 6,040 / 8,094 / 9,446 四个数，对应已完成/被拒/无相关文件/逾期，但 PDF 排版使对应关系不完全确定，暂只取总数与成功率）。被请求最多的机构：FBI 9,416、CIA 2,168。
- 来源：Sunshine Week 2026: The State of FOIA（信息图，引用 MuckRock）— https://www.newsmediaalliance.org/wp-content/uploads/2026/03/Sunshine-Week-2026-INFOGRAPHIC37862-1.pdf — News/Media Alliance，2026-03 — ✅（PDF 已下载解析）；MuckRock 原始页 https://www.muckrock.com/place/united-states-of-america/ ❌ 403

**`A1-05` | NATL | S2 | 凑合方案（大机构的）+ 需求信号（JD）**
- 结论：头部媒体用"专职 FOIA 编辑 + 内部请求数据库"来对抗延迟——这说明 FOIA 的追踪/催办/申诉管理本身是一项要专人做的工作，小编辑部没有这个配置。
- 证据：NYT 招聘 FOIA Editor，要求作为全编辑部公共记录请求的"hub"，"maintaining a centralized database of FOIA requests and appeals"（维护一个集中的 FOIA 请求与申诉数据库），并与法务部门判断哪些请求值得诉讼支持；同时"developing story ideas … through the FOIA process"（通过 FOIA 流程产出选题）。
- 来源：FOIA Editor — https://job-boards.greenhouse.io/thenewyorktimes/jobs/4739684005 — The New York Times（Greenhouse），抓取于 2026-11-03 — ✅（全文存于 raw/jobs_greenhouse.jsonl）

**`A1-06` | NATL | S2/S9 | 需求信号（记者/律师原话）**
- 结论：RCFP 诉讼主管认为 FOIA 系统长期人手不足，现在要靠打官司推动；记者需要"律师 + 诉讼"作为常规工具。
- 证据：FOIA "has never been adequately staffed or funded"（从未有足够的人手或资金）；联邦裁员（如 HHS FOIA 办公室被裁撤）让获取回复更难；RCFP 近几个月为新闻机构起诉 ICE、国务院、HHS；呼吁"Wear your name on a lawsuit as proudly as you do your byline"（像对待署名一样骄傲地署名诉讼）。
- 来源：Journalists will join forces with lawyers to fight back in court — https://www.niemanlab.org/2025/12/journalists-will-join-forces-with-lawyers-to-fight-back-in-court/ — Nieman Lab，Adam A. Marshall（RCFP），2025-12 — ✅

### A2 法律风险：SLAPP、传票、免费法律援助

**`A2-01` | NATL/LOCAL | S9 职业与生存（法律风险） | 市场数据（制度供给）**
- 结论：anti-SLAPP 保护是"看州"的拼图，40 州 + DC 有法，强弱差异很大。
- 证据：截至 2026-03，40 个州和哥伦比亚特区有 anti-SLAPP 法；南达科他州法律 2026-07-01 生效；马萨诸塞只保护"针对向政府请愿的报复"，加州则广泛覆盖公共议题言论；典型保护：发现程序前快速驳回、胜诉方追回律师费、动议提出后自动暂停发现、驳回可立即上诉。指南页未提及联邦 anti-SLAPP 法。
- 来源：Anti-SLAPP Legal Guide — https://www.rcfp.org/anti-slapp-legal-guide/ — Reporters Committee for Freedom of the Press，更新至 2026-03 — ✅

**`A2-02` | LOCAL/INDIE/NATL | S2/S9 | 需求信号（已发生的求助行为）+ 市场数据（资金）**
- 结论：地方记者对免费法律支持（拿记录、应对诽谤诉讼和传票）的请求在增加，RCFP 因"记者请求"而把州级律师项目扩到近一倍。
- 证据：Local Legal Initiative 扩展到路易斯安那、密西西比、明尼苏达、密歇根，"nearly doubling the size of the program"（规模近翻倍）；扩张是"in response to requests from journalists and newsrooms"（应记者和新闻机构的请求），理由是法律障碍增加、政府透明度不足；Press Forward 基础设施公开征集向 22 个项目提供 $22.7M，其中 RCFP 获 $1.25M；项目律师曾为记者抵御诽谤诉讼和要求交出信源的传票。原有州：科罗拉多、印第安纳、俄克拉荷马、宾州、田纳西。
- 来源：RCFP expands free legal support to local newsrooms in Gulf states and upper Midwest — https://www.rcfp.org/local-legal-initiative-expansion-announcement/ — RCFP，2026-03-04 — ✅

**`A2-03` | NATL | S3 找信源 / S9 | 市场数据（事件计数）**
- 结论：信源保密面临的法律压力是持续存在的：Tracker 累计记录了 42 起要求记者交出保密信源的传票。
- 证据："Subpoena/Legal Order" 类别累计 339 起；要求记者指认保密信源的传票 42 起；针对记者的搜查令 37 起；为调取记者记录向电信公司发传票 19 起、向科技公司 18 起；待决传票 7 起；页面说明这些数字"likely to underestimate actual cases"（很可能低估真实情况）。
- 来源：Subpoena/Legal Order — https://pressfreedomtracker.us/subpoena/ — U.S. Press Freedom Tracker（FPF），页面最新条目 2026-10-21 — ✅（累计数，未按年拆分；年度导出被 CF 拦截未核实）

**`A2-04` | 跨群体 | S5/S9 | 需求信号（JD，反向）**
- 结论：法律风险几乎不写进记者 JD——366 条 JD 里只有 7 条（2%）提到 libel/defamation/media law；法律风险由机构层面（标准编辑、法务）承担，个人记者和小编辑部缺这一层。
- 证据：见 §B 表格"libel / media law / legal"行；有法律内容的多是编辑/标准岗，如 Radio Free Asia 标准编辑 JD 写明要处理"legally complex, or high-risk stories"（法律上复杂或高风险的稿件）。
- 来源：本文 JD 数据集 `raw/jobs_classified.jsonl`；Standards Editor — https://www.journalismjobs.com/1694218-standards-editor-radio-free-asia — Radio Free Asia via JournalismJobs，2026-11 — ✅

### A3 信源保护与数字安全

**`A3-01` | NATL | S3/S9 | 需求信号（有方法论的调查）【2015 年，较旧】**
- 结论：调查记者普遍担心被监控，但多数没受过正式安全培训，而且把"资源减少"排在监控之前。
- 证据：对 671 名 IRE 会员的调查（2014-12 实施）：64% 认为美国政府可能收集过自己的通话/邮件数据（国安/外交/联邦条线 71%）；49% 过去 12 个月至少某种程度改变了保存/分享敏感文件的方式；记者中 38% 改变了与信源沟通的方式；14% 因监控/黑客担忧放弃过报道或信源；54% 没有接受过正式的电子安全培训；88% 把"新闻编辑部资源减少"列为首要挑战（监控仅 4%）。
- 来源：Investigative Journalists and Digital Security — https://www.pewresearch.org/journalism/2015/02/05/investigative-journalists-and-digital-security/ — Pew Research Center，2015-02-05 — ✅（年份较旧，需更新数据）

**`A3-02` | NATL/跨群体 | S3/S9 | 市场数据（培训/工具的使用规模）**
- 结论：数字安全培训和匿名爆料渠道是"非营利机构免费提供"的形态，规模以千人计。
- 证据：FPF 2025 年：培训记者数字安全 3,335 人；61 家新闻机构通过 SecureDrop 接收举报者线索；Tracker 记录 255 起美国新闻自由侵害；提交 FOIA 请求 250+ 件；提起 FOIA 诉讼 6 起。
- 来源：2025 by the numbers — https://freedom.press/about/announcements/2025-by-the-numbers/ — Freedom of the Press Foundation，2025-12-08 — ✅

### A4 调查记者怎么用 AI（文档分析为主）

**`A4-01` | NATL | S2/S4 | 需求信号（访谈研究）**
- 结论：调查记者用 AI/ML 主要是"处理大规模文件和记录"（OCR、模糊匹配、图像分类），但他们自己强调 AI 找不到所有故事，信源和独家仍靠人。
- 证据：170 次半结构化访谈（2021-07 至 2023-09；134 名新闻从业者来自美英德 35 家机构）；一位英国调查记者用模糊匹配调查腐败和逃税；华盛顿邮报用 Amazon Textract 做调查用文档的 OCR；采用者多依赖 Google/Amazon/Microsoft 平台 AI，并担心锁定与不透明；报告明确**不包含地方新闻机构**。
- 来源：Artificial Intelligence in the News: How AI Retools, Rationalizes, and Reshapes Journalism and the Public Arena — https://www.cjr.org/tow_center_reports/artificial-intelligence-in-the-news.php — Tow Center（Felix M. Simon），2024-02-06 — ✅

**`A4-02` | NATL | S2/S4/S5 | 需求信号（公开方法论）**
- 结论：ProPublica 把 LLM 用在"给记录分类/筛选"和"转写海量音视频"，但每条结果都人工核实——AI 用来缩小范围，不用来下结论。
- 证据：用 LLM 分析 Ted Cruz 办公室标记为"woke"的 NSF 资助数据库；2023 年与 Salt Lake Tribune 合作用 AI 找出心理健康从业者性不端纪律报告，由两名记者逐条对照执照记录核实；与 Texas Tribune 用自托管开源 AI 转写并分类数百小时的 Uvalde 音视频；记者原话：工具"still needs a lot of human supervision and vetting"（仍需要大量人工监督和审核）。
- 来源：How ProPublica Uses AI Responsibly in Its Investigations — https://www.propublica.org/article/using-ai-responsibly-for-reporting — ProPublica（Charles Ornstein），2025-03-13 — ✅

**`A4-03` | NATL（数据/调查记者）| S2/S1 | 需求信号（行业会议议程，间接）**
- 结论：在数据/调查记者的核心会议上，AI 议题三年翻倍（9%→18%），自动化/监控类议题也明显增加；但基础技能（表格/SQL/Python/R）仍占约三分之一，说明"基础数据处理"仍是大量记者的门槛。
- 证据（脚本 `nicar_sessions.py`，口径：标题+描述正则命中；一场可命中多个主题）：

| 主题 | NICAR 2024 (n=209) | NICAR 2025 (n=217) | NICAR 2026 (n=233) |
|---|---|---|---|
| AI / LLM | 19 (9%) | 26 (12%) | 41 (18%) |
| 自动化 / 监控 / 提醒 | 15 (7%) | 10 (5%) | 25 (11%) |
| FOIA / 公共记录 | 12 (6%) | 12 (6%) | 15 (6%) |
| 爬虫 | 14 (7%) | 13 (6%) | 15 (6%) |
| 文档 / PDF / OCR | 15 (7%) | 13 (6%) | 14 (6%) |
| 地方政府 / 会议 / 议程 | 4 (2%) | 2 (1%) | 7 (3%) |
| 警务 / 犯罪 / 法院 | 9 (4%) | 8 (4%) | 11 (5%) |
| 安全 / 隐私 | 8 (4%) | 3 (1%) | 5 (2%) |
| 法律 / 诽谤 | 10 (5%) | 4 (2%) | 4 (2%) |
| 表格 / SQL / Python / R | 74 (35%) | 82 (38%) | 74 (32%) |

  2026 年相关场次举例："Enhancing public records work with LLMs"（用 LLM 增强公共记录工作）、"How to get data out of complex documents using AI"、"Catching the quiet changes: Automating website monitoring for investigative journalism"、"Finding a needle in a haystack: How to manage document-heavy investigations"、"Running large language models locally"、"Editing the machine: Fact-checking AI-assisted reporting"。
- 局限：议程由 IRE 选题委员会决定，反映的是"会员愿意来学什么"，是间接需求信号；正则有噪音（如 "R" 与 "agents" 可能误中）。
- 来源：NICAR 2026 schedule — https://schedules.ire.org/nicar-2026/（官方 JSON：https://ire-nicar-conference-schedules.s3.us-east-2.amazonaws.com/nicar-2026/nicar-2026-schedule.json，2024/2025 同路径）— IRE，2026-03 — ✅；会议页 https://www.ire.org/training/conferences/nicar-2026/ ✅

### A5 工具供给（竞品事实）

**`A5-01` | NATL/跨群体 | S2/S4 | 竞品事实**
- 结论：Google Pinpoint 已覆盖"文档集检索 + 实体筛选 + 音视频转写 + 扫描表格转电子表格"，大媒体在用；生成式 AI 功能需申请。
- 证据：支持上传表单、手写文档、图片、邮件归档、PDF；按人物/组织/地点筛选；音视频转写可点击跳转；扫描表格（如多年房产记录）转可排序表格；默认私有；合作方列出 AP、NYT、Le Figaro 等；"Early access to generative AI features"需申请。页面未写价格和文档数量上限。
- 来源：Pinpoint — https://journaliststudio.google.com/pinpoint/about/ — Google Journalist Studio，访问于 2026-11-03 — ✅

**`A5-02` | LOCAL/NATL/INDIE | S1/S2 | 竞品事实**
- 结论：斯坦福 Big Local News 免费给任何新闻机构提供数据、工具和"提醒"类产品，定位正是"没有数据专员的编辑部"；其工具清单里已有地方政府文件爬虫和多种 Watch 提醒。
- 证据：自述"helps newsrooms do important accountability journalism without the need for their own data specialists"（帮助新闻编辑部在没有自己的数据专员的情况下做问责报道），数据、工具和培训对任何新闻机构免费；工具包括 Civic Scraper（下载地方政府文件的 Python 代码）、Court Scraper、Layoff Watch（WARN 裁员通知提醒）、Audit Watch（审计提醒）、CAL-ACCESS Watch（加州政治献金监控）；资方包括 Google News Initiative、Knight Foundation 等。
- 来源：About | Big Local News — https://biglocalnews.org/content/about/ ✅；Tools — https://biglocalnews.org/content/tools/ ✅ — Stanford，访问于 2026-11-03

**`A5-03` | LOCAL/INDIE | S1 | 竞品事实（与现有市政会议能力直接重叠）**
- 结论：Agenda Watch（MuckRock 体系，Big Local News 合作项目）提供地方政府议程/文件检索，仅向经过验证的机构用户开放。
- 证据：登录页写明访问权限"automatically granted to MuckRock users affiliated with a verified organization"（自动授予隶属已验证机构的 MuckRock 用户）；导航含 Search Documents、Coverage Areas、About the Data；Big Local News 合作列表中有 2021-11 RJI 文章"Making Agenda Watch useful to journalists across the country"。具体覆盖城市数、提醒功能**未核实**（需登录）。
- 来源：Agenda Watch — https://agendawatch.org/ — ⚠️（仅登录页可见）；Collaborations | Big Local News — https://biglocalnews.org/content/collaborations/ — ✅

**`A5-04` | NATL | S2 | 竞品事实【未核实】**
- 结论：DocumentCloud 由 MuckRock 运营（开源后端），官网本次无法连接，功能/规模未核实。
- 来源：https://www.documentcloud.org/ ❌（ECONNREFUSED）；GitHub MuckRock/documentcloud — https://github.com/MuckRock/documentcloud — ✅（仅确认仓库存在、由 MuckRock 维护）

---

## B. 招聘 JD 量化分析（跨全部群体）

### B.1 样本与口径

**来源与抓取**（`scrape_jobs.py`，2026-11-03）
| 来源 | 方法 | 原始条数 |
|---|---|---|
| journalismjobs.com | `/job-listings?page=N&count=100` 全量 3 页（共 206 条，即站上当时所有在招岗位），详情页 JSON-LD `JobPosting` + 页面 Industry/Specialty 字段 | 206 |
| Greenhouse 公开 API `boards-api.greenhouse.io/v1/boards/{org}/jobs?content=true` | NYT、ProPublica、Axios、Vox Media、Semafor、Insider、Hearst、Baltimore Banner；只保留标题匹配编辑类词（reporter/editor/producer/journalist/video/social/audience 等）且不匹配非编辑词（sales/engineer/marketing 等）的岗位 | 221（从 578 条中筛出） |
| 不可用 | INN jobs（CF 403）、Poynter jobs（403/域名不存在）、TVJobs（连接超时）、Indeed（403）、LION（404）、IRE 招聘板（只有 9 条且详情在 MemberSuite）、mediabistro（分页为加密 token，未做） | — |

**排除**（共 61 条，原因写在 `jobs_classified.jsonl.exclude_reason`）：非美国地点 15、非编辑部岗位标题（销售/市场/筹款/教职/总经理/公关等）26、Industry=Academia/Communications/PR 18、Greenhouse 部门=Marketing/Branded Content 2。**分析样本 n=366**，发布日期 2025-11-17 至 2026-11-02，其中 339 条（93%）发布于 2026-08-01 之后。

**分群规则**（先命中先归类：TV > RADIO > NATL > NONPROFIT_INDIE > MAGAZINE > LOCAL）
| 群体 | 规则 | n | 来源构成 |
|---|---|---|---|
| LOCAL（报社/数字，对应 LOCAL） | 其余报社、地方数字媒体、Hearst 报纸（Houston Chronicle 等）、Axios Local 城市记者 | 119 | JJ 91 + GH 28 |
| TV（对应 TV） | Industry 含 Television，或公司/部门为台呼（K/W+字母 TV） | 93 | GH(Hearst TV) 75 + JJ 18 |
| RADIO | Industry 含 Radio 或公共电台 | 13 | JJ 11 + GH 2 |
| NONPROFIT_INDIE（对应 INDIE + 非营利） | Industry 含 Nonprofit，或在非营利/独立名单内（States Newsroom、Civil Beat、Mississippi Today、Spotlight PA、Block Club 等） | 31 | JJ 31 |
| NATL | NYT/ProPublica/Vox/Semafor/Insider/Axios 全国岗，或全国媒体名单（U.S. News、Courthouse News、AFP、The Bulwark 等） | 91 | GH 77 + JJ 14 |
| MAGAZINE | Hearst Magazines 及纯杂志/出版 | 19 | GH 15 + JJ 4 |

**计数口径**：检索文本 = 标题 + 去样板后的描述；某 JD 只要命中关键词族中任一正则即计 1（出现/未出现，不计频次）；出现率 = 命中 JD 数 / 该群体 JD 数。完整正则见 `analyze_jobs.py` 的 `KW` 列表。已人工抽查 scanner、meetings、foia、ai_tool、deadline 的命中上下文；已知假阳性：`ai_tool` 有 1 条是在介绍机构产品（Civil Beat 介绍 CalMatters 的 Digital Democracy）而非岗位要求；`video` 含 "multimedia" 泛称。

### B.2 全量统计表（n=366）

| 关键词族 | 环节 | 全部 n=366 | LOCAL n=119 | TV n=93 | RADIO n=13 | NONPROFIT_INDIE n=31 | NATL n=91 | MAGAZINE n=19 |
|---|---|---|---|---|---|---|---|---|
| police/fire scanner | S1 | 4 (1%) | 0 (0%) | 3 (3%) | 0 (0%) | 0 (0%) | 1 (1%) | 0 (0%) |
| breaking news | S1 | 160 (44%) | 58 (49%) | 47 (51%) | 6 (46%) | 10 (32%) | 36 (40%) | 3 (16%) |
| city council / public meetings / school board | S1 | 18 (5%) | 13 (11%) | 0 (0%) | 0 (0%) | 5 (16%) | 0 (0%) | 0 (0%) |
| crime / police / public safety | S1 | 23 (6%) | 11 (9%) | 6 (6%) | 1 (8%) | 2 (6%) | 3 (3%) | 0 (0%) |
| courts / court filings | S1 | 14 (4%) | 7 (6%) | 2 (2%) | 0 (0%) | 1 (3%) | 4 (4%) | 0 (0%) |
| weather / severe weather coverage | S1 | 21 (6%) | 4 (3%) | 16 (17%) | 1 (8%) | 0 (0%) | 0 (0%) | 0 (0%) |
| story ideas / pitch / enterprise | S1 | 222 (61%) | 79 (66%) | 49 (53%) | 7 (54%) | 24 (77%) | 56 (62%) | 7 (37%) |
| FOIA / public records | S2 | 34 (9%) | 20 (17%) | 3 (3%) | 0 (0%) | 7 (23%) | 4 (4%) | 0 (0%) |
| data analysis / data journalism | S2 | 42 (11%) | 13 (11%) | 2 (2%) | 3 (23%) | 6 (19%) | 18 (20%) | 0 (0%) |
| investigative / accountability | S2 | 92 (25%) | 34 (29%) | 10 (11%) | 6 (46%) | 18 (58%) | 24 (26%) | 0 (0%) |
| develop / cultivate sources | S3 | 91 (25%) | 36 (30%) | 25 (27%) | 4 (31%) | 11 (35%) | 12 (13%) | 3 (16%) |
| interviews（作为采访任务） | S4 | 32 (9%) | 15 (13%) | 5 (5%) | 3 (23%) | 5 (16%) | 3 (3%) | 1 (5%) |
| transcription | S4 | 3 (1%) | 1 (1%) | 0 (0%) | 0 (0%) | 0 (0%) | 2 (2%) | 0 (0%) |
| fact-check / verification | S5 | 45 (12%) | 22 (18%) | 4 (4%) | 2 (15%) | 3 (10%) | 12 (13%) | 2 (11%) |
| accuracy / standards / ethics | S5 | 209 (57%) | 68 (57%) | 67 (72%) | 10 (77%) | 19 (61%) | 39 (43%) | 6 (32%) |
| libel / media law | S5 | 7 (2%) | 3 (3%) | 0 (0%) | 0 (0%) | 0 (0%) | 4 (4%) | 0 (0%) |
| video / multimedia | S6 | 223 (61%) | 58 (49%) | 66 (71%) | 4 (31%) | 17 (55%) | 63 (69%) | 15 (79%) |
| photography | S6 | 131 (36%) | 54 (45%) | 42 (45%) | 0 (0%) | 13 (42%) | 20 (22%) | 2 (11%) |
| audio / podcast | S6 | 75 (20%) | 16 (13%) | 4 (4%) | 8 (62%) | 8 (26%) | 36 (40%) | 3 (16%) |
| AP style / copy editing | S6 | 41 (11%) | 26 (22%) | 2 (2%) | 1 (8%) | 6 (19%) | 5 (5%) | 1 (5%) |
| CMS / web publishing | S7 | 32 (9%) | 16 (13%) | 0 (0%) | 2 (15%) | 7 (23%) | 6 (7%) | 1 (5%) |
| social media | S7 | 178 (49%) | 64 (54%) | 45 (48%) | 6 (46%) | 15 (48%) | 37 (41%) | 11 (58%) |
| SEO / search | S7 | 28 (8%) | 19 (16%) | 0 (0%) | 1 (8%) | 1 (3%) | 6 (7%) | 1 (5%) |
| newsletter | S7 | 64 (17%) | 33 (28%) | 0 (0%) | 1 (8%) | 9 (29%) | 17 (19%) | 4 (21%) |
| audience / engagement / analytics | S8 | 127 (35%) | 54 (45%) | 17 (18%) | 6 (46%) | 12 (39%) | 28 (31%) | 10 (53%) |
| community engagement / events | S8 | 48 (13%) | 25 (21%) | 5 (5%) | 3 (23%) | 6 (19%) | 7 (8%) | 2 (11%) |
| AI 任何提及（含 AI 作为报道条线） | X | 42 (11%) | 18 (15%) | 2 (2%) | 0 (0%) | 5 (16%) | 16 (18%) | 1 (5%) |
| AI 作为要用的工具 | X | 28 (8%) | 17 (14%) | 2 (2%) | 0 (0%) | 3 (10%) | 5 (5%) | 1 (5%) |
| deadlines / fast-paced / multiple stories | S9 | 247 (67%) | 79 (66%) | 52 (56%) | 8 (62%) | 21 (68%) | 68 (75%) | 19 (100%) |
| nights / weekends / holidays / on-call | S9 | 141 (39%) | 37 (31%) | 55 (59%) | 5 (38%) | 12 (39%) | 26 (29%) | 6 (32%) |
| driver's license / reliable vehicle | S9 | 49 (13%) | 22 (18%) | 25 (27%) | 0 (0%) | 1 (3%) | 1 (1%) | 0 (0%) |
| salary range disclosed | S9 | 145 (40%) | 25 (21%) | 21 (23%) | 8 (62%) | 20 (65%) | 54 (59%) | 17 (89%) |

### B.3 只看"记者岗"子集（标题含 reporter/journalist/correspondent/MMJ/writer，n=172）

去掉编辑、制片、视频剪辑等岗位后的同口径统计（完整表由 `analyze_jobs.py` 输出，数字存于 `jobs_keyword_stats.json → reporter_subset`），关键行：

| 关键词族 | 环节 | 全部 n=172 | LOCAL n=66 | TV n=45 | NONPROFIT_INDIE n=16 | NATL n=32 |
|---|---|---|---|---|---|---|
| breaking news | S1 | 81 (47%) | 30 (45%) | 18 (40%) | 7 (44%) | 19 (59%) |
| public meetings | S1 | 14 (8%) | 10 (15%) | 0 (0%) | 4 (25%) | 0 (0%) |
| scanner | S1 | 0 (0%) | 0 | 0 | 0 | 0 |
| story ideas / enterprise | S1 | 116 (67%) | 43 (65%) | 31 (69%) | 15 (94%) | 20 (62%) |
| FOIA / public records | S2 | 28 (16%) | 16 (24%) | 3 (7%) | 6 (38%) | 3 (9%) |
| data | S2 | 21 (12%) | 5 (8%) | 2 (4%) | 4 (25%) | 8 (25%) |
| develop sources | S3 | 81 (47%) | 32 (48%) | 24 (53%) | 10 (62%) | 8 (25%) |
| video | S6 | 102 (59%) | 34 (52%) | 37 (82%) | 8 (50%) | 18 (56%) |
| photography | S6 | 71 (41%) | 36 (55%) | 19 (42%) | 10 (62%) | 6 (19%) |
| social media | S7 | 83 (48%) | 37 (56%) | 23 (51%) | 9 (56%) | 8 (25%) |
| newsletter | S7 | 30 (17%) | 14 (21%) | 0 (0%) | 3 (19%) | 10 (31%) |
| AI 作为工具 | X | 7 (4%) | 6 (9%) | 0 (0%) | 1 (6%) | 0 (0%) |
| nights / weekends | S9 | 76 (44%) | 18 (27%) | 32 (71%) | 10 (62%) | 10 (31%) |
| driver's license / vehicle | S9 | 36 (21%) | 15 (23%) | 19 (42%) | 1 (6%) | 1 (3%) |

（RADIO n=10、MAGAZINE n=3 太小，略。）

### B.4 发现条目

**`B-01` | TV | S1 发现线索 | 需求信号（JD）+ 凑合方案**
- 结论：听警用 scanner 在 JD 里几乎只出现在**电视台派题编辑（assignment editor）**这一个岗位上——366 条中仅 4 条提到，但样本里 3 条 TV assignment editor JD 全部提到；记者岗子集 0 条。scanner 需求是"编辑台角色需求"，不是"记者普遍需求"。
- 证据：WMUR（NH）JD："Listen to multiple police scanners which cover more than a dozen agencies throughout our market—must have great 'scanner ears'"（同时监听覆盖本市场十几家机构的多台警用电台，必须有"scanner 耳朵"）；同一岗位还要"Gather and organize press releases, emails, phone calls and viewer tips"、"monitor multiple social media accounts"——即人工多源汇总。WCVB（Boston）JD："an assignment desk is more than scanners and press releases"（编辑台不只是 scanner 和新闻稿），并要求"Monitor social platforms for credible news tips"、"verify information quickly"。KOAT（NM）assignment editor 同样含 scanner 要求。第 4 条是 NYT 图表组 OSINT 岗，把"radio scanner data"列为开源证据之一。
- 来源：Assignment Editor (WMUR) — https://job-boards.greenhouse.io/hearst/jobs/4466219009 ✅；Assignment Editor (WCVB) — https://job-boards.greenhouse.io/hearst/jobs/4471703009 ✅；Assignment Editor (KOAT) — https://job-boards.greenhouse.io/hearst/jobs/4466289009 ✅；Open Source Reporting, Graphics — https://job-boards.greenhouse.io/thenewyorktimes/jobs/4737730005 ✅ — Hearst Television / NYT，抓取于 2026-11-03
- 局限：TV assignment editor 只有 3 条且同属 Hearst，不能推广到全行业比例。

**`B-02` | LOCAL/INDIE | S1 | 需求信号（JD）**
- 结论：跑市政会议是地方报社和非营利/超本地记者的明文职责（LOCAL 11%、INDIE 16%；记者岗子集 15% / 25%），电视台和全国媒体 JD 中为 0；而且部分 JD 把会议当作"底线"，要求"超越会议"。
- 证据：Bedford Citizen："cover local government meetings, schools, community events"；Mississippi Today 要求"pursue stories that go beyond government meetings, press releases and official statements"（追踪超越政府会议、新闻稿和官方声明的报道）；一份社区报编辑 JD 要求"Attend public meetings"并每周写多篇稿。
- 来源：命中清单 `venv/bin/python journalist/data/scripts/kw_snippets.py meetings`；例：Jackson Reporter — Mississippi Today（JournalismJobs，URL 见 raw/jobs_journalismjobs.jsonl）✅

**`B-03` | 跨群体 | S1 | 需求信号（JD）**
- 结论：S1 是所有群体 JD 的共同主轴：61% 要求自己产出选题/企业报道，44% 提到突发新闻；"自己找选题"比任何具体线索来源（scanner 1%、会议 5%、法院 4%、治安 6%）都普遍得多。
- 证据：见 B.2 表 S1 各行。INDIE 组"story ideas/enterprise"最高（77%，记者岗 94%）。
- 来源：`raw/jobs_keyword_stats.json` ✅

**`B-04` | TV | S1/S9 | 需求信号（JD）**
- 结论：电视台 JD 的特征组合是"天气 + 夜班周末 + 自己开车"：天气报道 17%（其他群体 ≤8%），夜班/周末 59%（记者岗 71%），要求驾照/可靠车辆 27%（记者岗 42%）。
- 来源：B.2/B.3 表；`kw_snippets.py weather` / `drive` ✅

**`B-05` | LOCAL/INDIE | S2 背景研究 | 需求信号（JD）**
- 结论：公共记录/FOIA 在地方和非营利 JD 里比在全国媒体 JD 里更常见（LOCAL 17%、INDIE 23%、TV 3%、NATL 4%；记者岗 INDIE 38%）——小编辑部记者自己提记录请求，没有 NYT 那样的专职 FOIA 编辑（见 A1-05）。
- 证据：一份自由撰稿岗 JD 要求"public records-based reporting, including use of the Odyssey Portal"（基于公共记录的报道，包括使用 Odyssey 法院门户）；Iowa Capital Dispatch："hold officials accountable through deep source building and public records requests"。
- 来源：`kw_snippets.py foia`；Reporter, Iowa Capital Dispatch — States Newsroom（JournalismJobs）✅
- 局限：NATL 组以 NYT 视频/图表岗为主，低估了全国调查记者的 FOIA 要求。

**`B-06` | NONPROFIT_INDIE | S2 | 需求信号（JD）**
- 结论：非营利/独立媒体是"调查/问责"写进 JD 最多的群体（58%，记者岗 62%），远高于 TV（11%）。
- 来源：B.2 表 ✅

**`B-07` | 跨群体 | S3 找信源 | 需求信号（JD）**
- 结论：找信源是记者岗最普遍的明文要求之一（记者岗子集 47%；TV 记者 53%、INDIE 62%），但它是关系型工作，JD 里没有任何工具化描述。
- 来源：B.3 表 ✅

**`B-08` | 跨群体 | S4 采访与素材处理 | 需求信号（JD，反向）**
- 结论：转写（transcription）只在 3/366 条 JD 中出现——转写已被视为默认能力/已被工具解决，不是招聘时会写的职责。
- 来源：B.2 表 ✅

**`B-09` | 跨群体 | S5 核实 | 需求信号（JD）**
- 结论："准确/标准/伦理"作为价值观被广泛写入（57%，TV 72%），但明确写"fact-check / verify"的只有 12%，法律审查 2%——核实被当作品德要求，而非一个被描述的流程。
- 来源：B.2 表 ✅

**`B-10` | LOCAL/TV | S6 写作与制作 | 需求信号（JD）**
- 结论：地方记者是"一人多工种"：LOCAL 记者岗 55% 要求拍照、52% 视频；TV 记者岗 82% 视频；地方 JD 还要 AP 风格/校对（LOCAL 22%）。
- 证据：例："Take your own photos"、"Report, write, edit, and proofread multiple stories each week for print, web, and digital platforms"（每周为纸媒、网站和数字平台采写、编辑、校对多篇稿件）。
- 来源：`kw_snippets.py deadline` 输出中的社区报 JD ✅；B.2/B.3 表

**`B-11` | LOCAL/INDIE vs TV | S7 发布与分发 | 需求信号（JD）**
- 结论：分发技能的分化很清楚：newsletter（LOCAL 28%、INDIE 29%、NATL 19%、**TV 0%**）、SEO（LOCAL 16%、TV 0%）、CMS（INDIE 23%、TV 0%）；社交媒体则各组都在 41–58%。电视台的分发是"push alert + 社交"，不是 newsletter/SEO。
- 来源：B.2 表 ✅；WMUR JD 要求"sending push alerts, Twitter and Facebook post" ✅

**`B-12` | LOCAL | S8 受众与变现 | 需求信号（JD）**
- 结论：受众/数据分析写进 45% 的 LOCAL JD（TV 只有 18%）——地方报社把流量/订阅指标压到采编岗。
- 来源：B.2 表 ✅

**`B-13` | 跨群体 | AI（横切） | 需求信号（JD）**
- 结论：AI 还不是记者岗的招聘要求：只有 8% 的 JD 要求使用 AI 工具，记者岗子集 4%，TV 2%；出现 AI 的地方集中在 McClatchy "内容专员"这类流量导向岗位和标准/管理岗。
- 证据：McClatchy Content Innovation Lab 三个岗位都写"use data, audience insights, and AI-enabled tools to surface trends"（用数据、受众洞察和 AI 工具发现趋势）；U.S. News 教育主编"use AI tools to increase workflow efficiencies"；一份编辑实习 JD 要求熟悉"Claude, ChatGPT, Perplexity, Gemini"；RFA 标准编辑负责起草"policies on the use of generative AI in reporting"。
- 来源：`kw_snippets.py ai_tool`（28 条全部列出）✅
- 对照：NICAR 数据/调查记者会议 AI 议题已占 18%（A4-03）——**会议端热、招聘端冷**。

**`B-14` | 跨群体 | S9 职业与生存 | 需求信号（JD）/ 市场数据**
- 结论：工作强度与条件是 JD 的高频内容：67% 写截稿压力/快节奏/多稿，39% 写夜班周末；薪资区间公开率在 LOCAL（21%）和 TV（23%）明显低于 NATL（59%）和 INDIE（65%）。
- 来源：B.2 表 ✅（薪资公开率受各州薪资透明法影响，属市场数据）

### B.5 九环节映射小结（JD 证据强度）

| 环节 | JD 中最强信号 | 群体差异 |
|---|---|---|
| S1 发现线索 | 自产选题 61%、突发 44% | TV 依赖 scanner（派题编辑）+ 天气；LOCAL/INDIE 依赖会议 |
| S2 背景研究 | 调查/问责 25%、FOIA 9%、数据 11% | INDIE 最高；FOIA 在地方/非营利更常见 |
| S3 找信源 | 记者岗 47% | 普遍、无工具化描述 |
| S4 采访与素材 | 采访任务 9%、转写 1% | 转写不再是招聘项 |
| S5 核实 | 价值观 57%，流程 12%，法律 2% | 法律风险不在记者 JD 里 |
| S6 制作 | 视频 61%、照片 36% | 地方"一人多工种" |
| S7 分发 | 社交 49%、newsletter 17%、SEO 8% | TV 无 newsletter/SEO |
| S8 受众 | 分析/互动 35% | LOCAL 45% |
| S9 生存 | 截稿 67%、夜班 39%、驾照 13% | TV 最重 |

**可能缺失的环节**：TV 派题编辑 JD 中大量内容是"追踪外勤摄制组、协调直播位、向主播/制片推送信息"（WMUR、WCVB JD），这是**编辑台调度/协同**，不属于 S1–S9 任何一个，建议在框架中单列为"编辑台协调（S1 与 S6/S7 之间）"。另外 FOIA 的"提交—追踪—催办—申诉—诉讼"在 NYT JD 中是一整套流程（A1-05），在 S2 下可能需要拆出"记录请求管理"子环节。

---

## C. 最反常识 / 最重要的 5 条

1. **scanner 是一个"岗位"需求，不是"记者"需求**（B-01）：366 条 JD 中只有 4 条提到 scanner，记者岗子集为 0；但样本中电视台派题编辑 JD 100%（3/3）把"同时听十几家机构的 scanner"写成首条职责，并配套人工汇总新闻稿、电话、观众爆料和社交媒体。产品若做 scanner 相关能力，用户画像是 TV assignment desk，而不是一般记者。
2. **FOIA 的痛点是"流程管理"而不是"写请求"**（A1-02~05）：联邦积压约 34 万、平均等待 >240 天（MuckRock 平台 276 天、成功率 26.6%），人手 -16%、积压 +27%；NYT 的对策是招专职编辑维护"集中的 FOIA 请求与申诉数据库"。小编辑部记者（LOCAL 17%、INDIE 23% 的 JD 要求做公共记录）没有这一层。
3. **AI 在会议端热、招聘端冷**（A4-03 vs B-13）：NICAR 的 AI 议题 2024→2026 从 9% 涨到 18%，ProPublica 已公开用 LLM 做记录筛选；但 JD 中要求用 AI 工具的只有 8%（记者岗 4%，TV 2%）。调查记者把 AI 用在"缩小文档范围 + 人工逐条核实"。
4. **法律风险由机构承担，个人和小编辑部得不到**（A2-01/02/04）：记者 JD 中 libel/media law 只占 2%；anti-SLAPP 保护看州（40 州+DC）；RCFP 因"记者请求增多"把免费州级律师项目扩大近一倍——说明需求真实存在，现在由非营利法律援助兜底。
5. **市政会议覆盖是地方/非营利的"底线职责"，已有竞品在做**（B-02、A5-02/03）：会议只写进 LOCAL 11%、INDIE 16% 的 JD（TV、NATL 0%），部分 JD 明确要求"超越会议和新闻稿"；Big Local News（Civic Scraper、多种 Watch 提醒）和 Agenda Watch 已免费向验证机构提供地方政府文件检索。

## D. 证据薄弱、需要补的地方

- **NATL 样本不代表调查记者**：NATL 组被 NYT 视频/图表岗主导。需补 ProPublica、The Marshall Project、Reveal、ICIJ、调查记者岗位，或抓 IRE 招聘板（MemberSuite 详情页）、INN 招聘板（需绕 CF，本轮未做）。
- **TV 样本来自单一雇主**（Hearst 占 81%）：需补 Gray、Nexstar、TEGNA、Sinclair、Scripps 的 Workday 招聘（有公开 JSON 接口可试），尤其要扩大 assignment editor 样本，验证 B-01 的 3/3。
- **GIJN、MuckRock、DocumentCloud、Muck Rack State of Journalism、AP 生成式 AI 报告均未核实**（403/连接失败/本轮搜索配额用尽）——这几份是"调查记者工具使用率"的关键调查，下一轮应优先补。
- **数字安全数据过旧**（Pew 2015）：需要 2023–2026 的调查记者安全/信源保护调查。
- **SLAPP/诽谤诉讼的数量数据缺失**：本文只有制度（anti-SLAPP 州数）和援助供给（RCFP LLI），没有诉讼数量、辩护成本、媒体责任险价格。Press Freedom Tracker 年度导出被 CF 拦截，需改用浏览器手动导出。
- **FOIA 记者占比**：联邦年报不区分请求者类型；FOIA Project（TRAC）媒体诉讼名单最新只到 2020 年（未核实 2021+）。
- JD 关键词统计是正则，未做人工双编码一致性检验；若要对外引用，建议对每个关键词族抽 30 条人工判定精度。
