# 12 条线深挖：商业/经济/金融 · 科技 · 地产/住房/开发

## 本文件覆盖范围、来源、局限

- **范围**：三条线。
  1. 商业/经济/金融：地方商业、上市公司、劳动与就业、宏观经济数据。
  2. 科技：科技公司、AI、风投与创投、科技裁员。
  3. 地产/住房/开发：产权、许可、zoning、开发项目、数据中心选址。
- **每条线回答**：
  - 记者在九个环节上做什么；
  - 主要信息来源；
  - 哪些事能自己方便解决（✅ / ⚠️ / ❌）；
  - 专用工具和竞品；
  - 协会（SABEW、Reynolds Center）的调查和原话；
  - 近 2 年的变化（AI 研究工具渗透、联邦数据断档、LLC 透明度倒退）。
- **与 07 的关系**：07 G3 已有 10 条（G3-01～G3-10：许可数据碎片化、Shovels、Investigative Post 人工拼 LLC、Orlando 数据错配、RatRadar、McClatchy×United Robots、DataDesk、Hamlet、Business Journals、Wozniak）。本文件**引用但不重复**，新增 38 条证据（B 14 / T 9 / R 8 / X 7）。
- **来源**：本轮实际访问约 45 个页面或接口。
  - 搜索用 octo_search（DDG / Bing News）。
  - 核实用 curl_cffi 和 WebFetch，GitHub 内容用 GitHub API。
  - 另用了本项目已采集的两份语料：
    - `raw/jobs_*.jsonl`：2026 年 JD 原文，n=366，已剔除无关岗位；
    - `raw/reddit_posts.jsonl`：Reddit 原帖。
  - 证据状态（按条目主结论）：✅ 约 27 条；⚠️ 约 11 条，其中 Reddit 原帖 6 条（来自已采集语料，reddit.com 本轮无法直连复核），其余是第三方价格或只看到搜索摘要。
- **主要局限**
  1. **一线商业/地产记者描述日常工作流的原话仍少。**
     - 直接自述只有：SABEW 两场面板（WSJ、Reuters、Wired、ICIJ 记者），以及 6 条 Reddit 帖。
     - Business Journals 站点被 Cloudflare 拦截，只核实了它的帮助中心页。
  2. **没有找到"商业记者工具使用/付费"的专门调查。**
     - Reynolds/SABEW 2026 薪酬调查（n=235）只问薪资、岗位和招聘，没问工具。
  3. **专业终端的价格都是第三方买方数据**（Vendr、CostBench、NeuGroup 转述），厂商不公开，统一标 ⚠️。
  4. **劳动条线薄**：没拿到劳动记者的原话，只有数据源侧的证据（WARN、BLS 断档、ILR 罢工追踪）。

---

## 一、三条线 × 九环节速览（结论先行，证据见第二节编号）

| 环节 | 商业/经济/金融 | 科技 | 地产/住房/开发 |
|---|---|---|---|
| S1 发现线索 | 源头网络 + 公关稿 + 申报提醒（8-K、WARN）；SEC 按地域提醒的工具 Sqoop 已消失（B-06）；WARN 无中央库（B-03/04） | 爆料、公司页面悄改、changelog；小团队靠 RSS、网页变更监测、人工外联（T-03）；收入跟独家挂钩（T-05） | zoning/场地规划、议程、许可、契据；一人跨 109 个政府看议程（R-01）；Business Journals 每周汇编公共记录（R-02） |
| S2 背景研究 | NotebookLM 和深度研究快速做人物稿（X-01）；EDGAR 全文检索免费（B-07）；终端昂贵（B-09） | 风投/私营公司数据靠 Crunchbase/PitchBook（T-06）；layoffs.fyi 替代官方统计（T-04） | 产权、LLC、税、违规跨库拼接（07 G3-03）；联邦和纽约的 LLC 透明化落空（R-05） |
| S3 找信源 | 高管、源头网络是 JD 核心（B-12）；深度研究找"Google 搜不到"的人（X-01） | AI 实验室、风投、国会多层信源（T-01） | 开发商、律师、经纪人（R-03 JD） |
| S4 采访/素材 | 财报电话会转写（Seeking Alpha 等付费）（B-08） | 法庭文件 + 证券申报 + 内部文件（T-07） | 记录申请拿 NDA 原件（R-04） |
| S5 核实 | 私营替代数据彼此差 10 万岗位（B-02）；AI 垃圾使核实占 80% 时间（B-10） | AI 工具编造引语（X-02） | 政府数据错配（07 G3-04） |
| S6 写作制作 | AI 草稿规模化：Fortune、BI、Quartz、Reuters（X-03～X-06） | 同左 | 自动化房产交易稿（07 G3-06） |
| S7 发布分发 | 每日邮件 + 周刊纸版 + 视频（B-12） | 离开 Substack/X 有代价（T-05） | — |
| S8 受众/变现 | 把公共记录、政策追踪卖给商业读者（R-02、R-06） | 独家驱动订阅；广告售罄（T-05） | ATTOM 等以"给记者数据"换曝光（R-07） |
| S9 职业生存 | 商业记者薪资溢价，但 ACBJ 记者中位数只有 $66,667（B-01）；B2B 写手被 GenAI 冲击（X-07） | Tarbell 资助 AI 记者 $75k–135k（T-08） | 同 B-01 |

---

## 二、发现条目

### A. 商业 / 经济 / 金融 / 劳动

**B-01** | LOCAL, NATL, FREE | S9 | 商业 | 市场数据（协会调查）
- 结论：商业记者薪资高于行业平均，但不同媒体类型差距很大。商业周刊（ACBJ）**薪资最低、流动最快**，并且是最少在招人的一类。
- 证据：Reynolds Center 与 SABEW 2026 年 4–5 月调查，n=235，覆盖 34 个州（含 DC）。
  - 记者/通讯员/自由撰稿人薪资中位数 $85,278，比 BLS 记者中位数高 41.5%。
  - 按媒体类型：全国/全球媒体记者 $116,875，行业刊物 $91,667，**ACBJ $66,667（最低）**。
  - ACBJ 受访者中 47.5% 在现岗位不到 1 年。
  - 只有 20% 的 ACBJ 受访者说所在编辑部在招人；全国/全球媒体是 75.4%。
  - 受访者分布：地方/区域媒体 31.9%，全国/全球媒体 26%，ACBJ 17%，行业刊物 14.5%。
- 意义：地方商业周刊是"初级、高周转"的入口岗位，人均资源少。
- 来源：Hiring, raises show strong demand for business journalists: Reynolds Center survey — https://businessjournalism.org/2026/06/2026-salary-survey/ — Reynolds Center / 2026-06-24 — ✅

**B-02** | NATL, LOCAL | S2 / S5 | 经济/劳动 | 凑合方案（官方数据断档）
- 结论：2025 年政府停摆期间，BLS 停发就业和 CPI 报告。经济记者只能拿 ADP、Indeed、Challenger 等私营数据拼凑，而这些数据**口径不一、互相打架，本身又依赖 BLS 校准**。
- 证据：
  - CNBC 引劳工部应急计划："BLS will suspend all operations…Economic data…will not be released."（BLS 将暂停所有运作，期间应发布的经济数据不发布）
  - Business Insider 2025-11-07："Economists, journalists, and investors won't be waiting…It's the second month without this data release."（经济学家、记者和投资者今早等不到就业报告，这是连续第二个月）
  - Indeed 经济学家说替代数据"often rely on data from the Bureau of Labor Statistics to calibrate"（常常依赖 BLS 数据来校准）。
  - Richmond Fed：停摆期间两个私营数据源"diverging by 100,000 jobs"（相差 10 万个岗位）。
- 意义：**宏观数据的权威性和连续性 2025 年起首次成了记者的问题**。核实时要懂各口径差异，单靠工具解决不了。
- 来源：
  - https://www.cnbc.com/2025/09/29/bls-wont-be-releasing-data-including-fridays-key-jobs-report-in-case-of-a-shutdown.html — CNBC / 2025-09-29 — ✅
  - https://www.businessinsider.com/no-jobs-report-alternative-data-labor-market-hiring-openings-layoffs-2025-11 — BI / 2025-11-07 — ✅（导语可见，正文付费）
  - https://www.richmondfed.org/publications/research/economic_brief/2026/eb_26-04 — Richmond Fed / 2026-02 — ✅
  - 补充：2025 年 8 月特朗普解雇 BLS 局长，经济数据的政治化成为新报道议题。只看到搜索摘要，例如 https://calmatters.org/economy/2025/08/bls-commissioner-jobs-data-ca/ — ⚠️

**B-03** | LOCAL, NATL | S1 | 劳动/地方商业 | 凑合方案 + 需求信号（已发生的采购）
- 结论：WARN 裁员通知没有中央数据库。斯坦福 Big Local News（BLN）写了开源爬虫，**每天汇总几十个州的网站**，并把自动提醒做成会员服务。首批付费会员是 Reuters 和《洛杉矶时报》。
- 证据：
  - "with no centralized database of notices, journalists struggle to keep up. Newsworthy job losses often go uncovered."（没有中央数据库，记者跟不上，有新闻价值的裁员常被漏报）
  - 提醒通过 Slack/Teams 机器人推送；数据和代码对所有记者免费，**提醒只给会员**，会费养活数据采集。
  - 已带来的独家：Cedar Rapids Gazette、Sioux City Journal、Tampa Bay Times、Chicago Tribune 等。
- 意义：**"免费数据 + 付费提醒"在记者市场已被验证**，买方是机构会员，不是记者个人。
- 来源：
  - Meet Layoff Watch — https://biglocalnews.org/content/news/2022/07/27/hello-layoff-watch.html — BLN / 2022-07-27 — ✅（2022 年）
  - Layoff Watch 工具页 — https://biglocalnews.org/content/tools/layoff-watch.html — ✅

**B-04** | LOCAL, NATL | S1 | 劳动 | 凑合方案的维护成本（为什么"不好自己解决"）
- 结论：WARN 爬虫只覆盖 39/56 个州和领地，17 个仍缺，含宾州、北卡、麻州、明尼苏达。已有爬虫持续损坏：
  - 德州疑似反爬；
  - 纽约停发 CSV，改成 Tableau；
  - 华盛顿州部分条目没触发提醒；
  - 加州被标为"hopelessly inefficient"（无可救药地低效）。
- 证据：
  - 维护者 2026 年 issue："Not all entries are triggering alerts; see Starbucks and Amazon from WA file."（不是所有条目都触发了提醒，见华盛顿州文件里的 Starbucks 和 Amazon）
  - 对纽约 Tableau 改版的评价："likely to have a high chance of being painful"（很可能非常痛苦）
- 意义：**即便有斯坦福团队，持续维护几十个州门户也很吃力**。地方记者自己做更不现实，这类事属于 ❌。
- 来源：
  - Sources（39/56）— https://warn-scraper.readthedocs.io/en/latest/sources.html — ✅
  - Issue #778 Major outstanding scraper problems — https://github.com/biglocalnews/warn-scraper/issues/778 — 2026-05-15 — ✅
  - Issue 列表（#800 TX browser protection、#785 MD、#783 LA、#652 CA）— https://github.com/biglocalnews/warn-scraper/issues — 2026-11 访问 — ✅

**B-05** | LOCAL | S1 / S6 | 地方商业 | 需求信号（发稿行为）
- 结论：地方报纸把"WARN notice filed with the state"当作固定稿源，常见写法是"according to a WARN notice filed with the state"（据向州政府提交的 WARN 通知）。
- 证据：South Bend Tribune 2026-01 写 Wabash National 裁员 144 人；Peoria Journal Star 2025-07 写伊利诺伊近 1,800 人裁员汇总稿。
- 来源：
  - https://www.southbendtribune.com/story/business/2026/01/14/wabash-national-goshen-indiana-layoffs-warn-notice-march-2026/88149529007/ — ⚠️（只核对了搜索摘要）
  - https://www.pjstar.com/story/news/local/2025/07/13/illinois-businesses-set-to-lay-off-nearly-1800-workers/84580739007/ — ⚠️（只核对了搜索摘要）

**B-06** | LOCAL | S1 | 上市公司/地方商业 | 需求信号（记者原话）+ 竞品消失
- 结论：一名记者回到需要跟 SEC 申报的岗位，想找"**只推送我报道地区公司**的 SEC 申报提醒"。她以前用的 Sqoop 已经找不到了。
  - Sqoop 是面向商业记者的创业公司，免费检索 SEC、专利局和联邦法院，可设提醒。
  - 现有替代品（EDGAR RSS、KFilings 等）按公司或表格类型订阅，**不按地域**。
- 证据：
  - "get email alerts about new SEC Filings, but only for stuff in your coverage area"（只针对我报道地区的新 SEC 申报邮件提醒）
  - "as far as I can tell its gone?"（据我所知它已经没了？）
  - Sqoop 创始人当年的说法："there's no way to set an alert. Sqoop does the work for you."（没有办法设提醒，Sqoop 替你做）
- 来源：
  - Reddit r/Journalism — https://www.reddit.com/r/Journalism/comments/1ozhzra/does_anybody_remember_sqoop_tools_for_sec_filings/ — 2025-11-17 — ⚠️（项目已采集语料原文）
  - 'Sqoop' website allows reporters to search government databases faster — https://www.nfoic.org/blogs/sqoop-website-allows-reporters-search-government-databases-faster/ — NFOIC / 约 2017 年（原文写"去年三月上线"）— ✅（年代老）

**B-07** | NATL, LOCAL, FREE | S2 | 上市公司 | 基础设施事实（免费源的边界）
- 结论：EDGAR 全文检索免费，覆盖 2001 年以来全部电子申报及附件。官方页面**没有提供提醒或保存检索**。程序化访问限速 10 次/秒，并要求声明 User-Agent。
  - 本轮调研中我们自己的请求就被 SEC 返回 "Request Rate Threshold Exceeded"（请求频率超限）。
- 意义：检索（S2）✅ 已解决；"按我关心的维度实时提醒"（S1）⚠️ 要自己写脚本或另找工具。
- 来源：
  - EDGAR Full Text Search FAQ — https://www.sec.gov/edgar/search/efts-faq.html — ✅（WebFetch）
  - Accessing EDGAR Data — https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data — ✅（"Current max request rate: 10 requests/second"）

**B-08** | NATL, FREE | S4 | 上市公司 | 凑合方案（财报电话会转写要付费）
- 结论：财报电话会转写的主要消费级来源是 Seeking Alpha Premium，转写在付费墙后。
  - 专业端有 AlphaSense 的转写摘要，以及 Bloomberg 终端 2024 年起的 AI 财报电话会摘要。
  - 记者不付费时的办法：听公司 IR 网页直播、自己转写。
- 来源：
  - Does Seeking Alpha Premium include earnings call transcripts? — https://help.seekingalpha.com/does-seeking-alpha-premium-include-earnings-call-transcripts — ⚠️（只核对了搜索摘要）
  - AlphaSense Transcript Summaries — https://help.alpha-sense.com/hc/en-us/articles/41712766038675-Transcript-Summaries — ⚠️（只核对了搜索摘要）

**B-09** | NATL | S2 | 金融 | 市场数据（终端价格，第三方）
- 结论：Bloomberg 终端约 $31,980/年（单终端），多终端每台约 $28,320/年，通常签两年合同。
  - 依据是 NeuGroup 2024-10 转述的客户信函，以及 Vendr 15 笔买方数据的中位数。
  - 2025-01 起，Bloomberg 在终端上给新闻加 AI 三点摘要。
- 意义：**全国财经记者靠雇主的终端**；地方和独立记者实际上用不上。
- 来源：
  - https://costbench.com/software/financial-data-terminals/bloomberg-terminal/ — 2026-10 核实 — ⚠️（第三方）
  - https://www.thepricer.org/how-much-does-bloomberg-terminal-cost/ — 2026-10-23 — ⚠️（第三方）
  - AI 摘要：https://talkingbiznews.com/media-news/bloomberg-starts-ai-generated-news-summaries/ — 2025-01-15 — ⚠️（403，只看到搜索摘要）

**B-10** | NATL, FREE | S2 / S5 | 金融 | 需求信号（记者原话）
- 结论：一名财经记者说，网上 AI 垃圾内容和"可信"媒体里的幻觉数字太多，**80% 的时间花在找可靠来源上**，只有 20% 用来写。
- 证据："I'm spending 80% of my time on research (or more like trying to find credible sources) and only 20% on the writing."（我 80% 的时间在研究，更像是在找可信来源，只有 20% 在写）
- 来源：Reddit r/Journalism — https://www.reddit.com/r/Journalism/comments/1safhc0/is_anyone_else_spending_more_time_finding_data/ — 2026-04-02 — ⚠️（语料原文；单帖）

**B-11** | NATL | S1 | 金融/市场 | 需求信号（记者原话 + 工具可得性）
- 结论：一名美国市场记者在找能把社交帖子、公司发布、活动聚合起来的线索工具。编辑有 NewsWhip，他没有权限；前东家用过的 Dataminr、TweetDeck 现在都用不了。
- 证据："My editor has access to Newswhip, but I don't have access."（编辑有 NewsWhip，我没有）
- 意义：**工具席位按"编辑/机构"分配，一线记者常常够不着**。
- 来源：Reddit r/Journalism — https://www.reddit.com/r/Journalism/comments/1bv30zp/any_useful_free_sourcingsocial_media_monitoring/ — 2024-04-03 — ⚠️（语料原文）

**B-12** | LOCAL | S1 / S3 / S7 | 地方商业 | 需求信号（JD 工作描述）
- 结论：地方商业岗位 JD 的共同点：
  - 核心是"源头网络 + 抢独家"；
  - 一个人要跑很宽的条线：雇主、小企业、制造、开发、商业地产、零售、劳动力；
  - 要用公共记录、财务申报、法院文件核实；
  - 要盯激励/招商补贴是否兑现；
  - 产出多平台：日更邮件、周刊纸版、视频。
- 证据：
  - Birmingham Business Journal（ACBJ）："digging up news before it's announced or readily available"（在宣布或公开之前挖出新闻）；"Scoop competitors on every story of any significance"（每条重要新闻都要抢在对手前面）。
  - Quad-City Times："Scrutinize public incentives and economic development deals, tracking spending, commitments and results"（审视公共激励和招商协议，追踪支出、承诺与结果）。薪资 $45,000–50,000。
- 来源（项目已采集 JD 语料，2026-10/11）：
  - https://www.journalismjobs.com/1694221-law-and-money-reporter-birmingham-business-journal — ✅（语料原文）
  - https://www.journalismjobs.com/1693917-business-reporter-quad-city-times — ✅（语料原文）
  - 占比：366 条有效 JD 中，标题含 business / real estate / development / tech / money / growth 的只有约 15 条（有重叠），**条线专岗在招聘中占比很低**。

**B-13** | LOCAL, INDIE, FREE | S2 | 地方商业 | 市场数据（州商业登记的获取门槛）
- 结论：州务卿商业实体登记的单条查询多数免费，但**批量和"新注册公司"流**要找商业数据商买。
  - 例：OpenSOSData 按 $2.50/千条起卖，最低 $25，覆盖 53 个辖区、3,300 万条，有"新成立公司""状态变更"清单。
  - 买家定位是 B2B 销售线索，不是记者。
- 意义："本周本地新注册了哪些公司"这类线索，记者自己做是 ⚠️（花钱少，但要有数据处理能力）。
- 来源：https://opensosdata.com/datasets/ — 2026-11 访问 — ✅

**B-14** | LOCAL | S1 | 劳动 | 竞品/数据源事实
- 结论：Cornell ILR 与 Illinois LER 合办的 Labor Action Tracker，靠研究团队**人工录入公开来源**，覆盖罢工和劳工抗议。罢工数据自 2021 年起较完整；抗议数据只求"大体了解"，不求全数。面向活动人士、政策制定者和学者，**没有提记者**。
- 意义：劳动条线的"罢工线索"有学术数据集兜底，但仍是人工、滞后的。
- 来源：https://www.ilr.cornell.edu/faculty-and-research/labor-action-tracker — ✅

### B. 科技

**T-01** | NATL | S3 | 科技/AI | 需求信号（JD）
- 结论：全国科技岗的核心要求是**高层信源网络**：AI 实验室、风投/私募、国会、白宫和联邦机构。工作节奏是"high metabolism"（高代谢）：突发、次日稿、分析、问责。
- 证据：
  - NYT："cover OpenAI and Anthropic as the artificial intelligence race heats up"（在 AI 竞赛升温之际报道 OpenAI 和 Anthropic）
  - Semafor 要求候选人在"major AI labs, in venture capital and private equity, on Capitol Hill"（主要 AI 实验室、风投私募、国会山）有信源。
  - Axios 防务商业记者岗薪资 $100k–150k，要求"follow the money"（追踪资金流向）。
- 来源（项目已采集 JD 语料）：
  - https://job-boards.greenhouse.io/thenewyorktimes/jobs/4701630005 — 2026-06 — ✅
  - https://job-boards.greenhouse.io/semafor/jobs/4698822005 — 2026-05 — ✅
  - https://job-boards.greenhouse.io/axios/jobs/8122218 — 2026-08 — ✅

**T-02** | NATL | S2 | 科技 | 需求信号（AI 研究工具已在用）
- 结论：WSJ 科技记者 Herrera 用深度研究梳理"有人用 AI 自建软件"的案例，作为软件股抛售稿的背景，"to get a lay of the land"（摸清全貌）。他第一次让 AI "in a big way"（大幅度）帮到采访，是用 NotebookLM 做 Larry Ellison 人物稿（详见 05 C-47）。
- 来源：https://businessjournalism.org/2026/03/sabew-ai/ — SABEW / Reynolds 2026-03-11 — ✅

**T-03** | INDIE | S1 | 科技 | 凑合方案（记者原话）
- 结论：一家小型独立科技媒体的新闻编辑被要求增加日更量，而线索追踪"very manual"（非常手工）：RSS、网页变更监测、社交媒体、newsletter、大量联系公关。
  - 另一帖专门问：记者怎么追踪公司官网悄悄改的价格页、政策页、产品页，现有工具漏了什么。
- 证据："Right now, our news tracking is very manual. RSS feeds, web page change trackers, social media, newsletters, and lots of outreach to PR teams."（现在我们的新闻追踪非常手工：RSS、网页变更监测、社媒、通讯和大量公关外联）
- 来源：
  - https://www.reddit.com/r/Journalism/comments/1ign1a8/what_are_your_niche_news_tracking_tools_and/ — 2025-02-03 — ⚠️（语料原文）
  - https://www.reddit.com/r/Journalism/comments/1qjpe3p/journalists_what_tools_do_you_use_to_track/ — 2026-01-22 — ⚠️（语料原文；发帖者身份不明，可能是做工具的人）

**T-04** | NATL, LOCAL | S2 | 科技/劳动 | 凑合方案（个人项目替代官方统计）
- 结论：科技裁员没有官方实时统计，媒体普遍引用个人项目 layoffs.fyi。
  - 它只收"媒体报道、公司宣布或已核实"的裁员，自承**低估**。
  - 数据对编辑用途免费，要求署名。
  - Slate 认为它被广泛引用，是因为"科技行业"这个类别与 NAICS 统计分类对不上。
- 证据：
  - layoffs.fyi："the Layoffs.fyi figures are likely an undercount"（数字很可能低估）
  - Slate 2023："this one does not map neatly to the made-up categories the government uses"（这个类别与政府统计用的分类对不上）
- 来源：
  - https://layoffs.fyi/press/ — ✅
  - https://slate.com/technology/2023/01/tech-layoffs-how-many-fyi-data-tracking-kittens.html — Slate / 2023-01 — ✅

**T-05** | INDIE | S7 / S8 | 科技 | 市场数据 + 记者原话（独立科技媒体的变现）
- 结论：Platformer（Casey Newton）5 年后的情况：
  - 数千付费订阅、20 万免费订阅；广告售罄；养活 5 个岗位。
  - 增长放缓，他自己归因："revenue correlates fairly closely with scoops"（收入与独家紧密相关）。
  - 退出 Substack 和 X 后失去了主要获客渠道。
  - newsletter 经济"organized around stars"（围绕明星运转）。
- 意义：**独立科技记者的变现直接取决于 S1 独家产出**。
- 来源：What I learned in the first five years of Platformer — https://www.platformer.news/platformer-year-five-lessons/ — 2025-09-23 — ✅

**T-06** | NATL, INDIE, FREE | S2 | 科技/创投 | 市场数据（私营公司数据库价格）
- 结论：
  - Crunchbase Pro $99/月（月付），Business $199/月，API 和定制数据要询价（Vendr 中位数 $20,000/年）。
  - PitchBook 单用户约 $12,000–20,000/年（第三方）。
  - **两家都没查到面向记者的免费或折扣计划**；PitchBook 只有试用申请。
- 来源：
  - https://marketintelligencetools.com/reports/crunchbase-pricing/ — 2026-08/10 — ⚠️（第三方，称已对照 Crunchbase 官方页）
  - https://costbench.com/software/financial-data-terminals/pitchbook/ — ⚠️（第三方，自注"unverified"，即未核实）

**T-07** | NATL | S4 / S5 / S9 | 科技问责 | 需求信号（获奖调查的方法与周期）
- 结论：SABEW 2025 科技类获奖作品（The Markup 调查 Match Group）历时 **18 个月**。
  - 材料：数百页内部文件、数千页法庭记录和证券申报、几十次访谈。
  - 资助：Pulitzer Center 的 AI Accountability Network。
- 意义：科技问责报道依赖"法庭 + 证券申报 + 泄露文件"的长周期整理，并且靠基金会补贴。
- 来源：https://themarkup.org/inside-the-markup/2026/03/30/the-markup-wins-sabew-award-for-best-in-business-journalism — 2026-03-30 — ✅

**T-08** | FREE, NATL | S9 | 科技/AI | 市场数据（条线专项资助）
- 结论：Tarbell Center 专门资助 AI 记者。
  - 一年制 fellowship：3 个月培训 + 9 个月进驻编辑部，年薪 $75k–120k，资深 $115k–135k。往届东家有 CBS News、TIME、MIT Tech Review。
  - 另有机构资助，以及 $1k–20k 的报道资助（自由撰稿人也可申请）。
- 意义：**AI 条线是少数有外部资金主动"造岗"的条线**。
- 来源：
  - https://www.tarbellcenter.org/fellowship — 2026-11 访问 — ✅
  - 报道资助额度：https://www.solutionsjournalism.org/events/tarbell-center-ai-journalisms-reporting-grants — ⚠️（只看到搜索摘要）

**T-09** | LOCAL, NATL | S1 / S2 | 科技 × 地产 × 地方 | 凑合方案（数据中心保密）
- 结论：AI 数据中心选址普遍用 NDA 和代号，地方记者**只能靠公共记录申请**挖。
  - Gulf States Newsroom 与 Type Investigations 申请记录后，发现路易斯安那自 2024 年初起至少有 54 份官员签的 NDA。
  - 一个项目用了 "Project Lightning""Project Pixel" 两个代号。
  - 弗吉尼亚研究者发现，31 个数据中心项目中至少 25 个用了 NDA。
  - 2026-09，众议员 Raskin 就 NDA 致函 Amazon、Google、Meta、Oracle；多州立法禁止这类 NDA。
  - Omaha World-Herald 的 JD 已把"数据中心对公共电价的影响"写进地方政府与增长条线。
- 证据：研究者 Bonds 说发表研究后"we heard back from reporters and activists kind of around the country"（全国各地的记者和活动人士都来联系我们）。
- 意义：**项目早期信号被刻意藏起来**，会议、许可、产权里的线索只能事后拼。
- 来源：
  - NDAs are hiding data center deals… — https://www.kuow.org/npr-news/2026-08-27/ndas-are-hiding-data-center-deals-drawing-ire-from-locals-and-attention-from-lawmakers — NPR（KUOW 转载）/ 2026-08-27 — ✅
  - Raskin 致函 — https://democrats-judiciary.house.gov/media-center/press-releases/ranking-member-raskin-probes-big-tech-s-use-of-non-disclosure-agreements-to-prevent-local-officials-from-discussing-data-center-project-with-constituents/ — 2026-09-30 — ⚠️（只核对了搜索摘要）
  - Omaha JD：https://www.journalismjobs.com/1694120-local-government-and-growth-reporter-omaha-ne-omaha-world-herald — ✅（语料原文）
  - Poynter 2026-05-20（Jon Greenberg）建议地方编辑部报数据中心：要求候选人表态、查竞选捐款、参考第三方 tracker，但"verify everything for yourself"（一切自己核实）。全文没提许可、NDA、LLC 等具体记录 — https://www.poynter.org/reporting-editing/2026/how-to-report-local-data-center/ — ✅（WebFetch）

### C. 地产 / 住房 / 开发

**R-01** | LOCAL | S1 | 住房 | 需求信号（记者原话）
- 结论：一名住房记者负责九个县、**109 个市县政府**，想要工具在议程发布时自动按关键词筛出与住房相关的条例和动议。
- 证据："I cover housing in a nine-county region with 109 seperate municipal and county governments."（我在九县区域跑住房线，有 109 个独立的市县政府）
- 意义：与 07 的 Hamlet、DataDesk 对应。**"跨很多辖区监控议程"是地产/住房线最明确的 S1 需求**。
- 来源：https://www.reddit.com/r/Journalism/comments/1j51l2t/best_way_to_scrape_city_council_agendas/ — 2025-03-06 — ⚠️（语料原文）

**R-02** | LOCAL | S1 / S8 | 地方商业/地产 | 竞品事实（补 07 G3-09 的 ⚠️）
- 结论：Business Journals 的"Public Records"每周从法院、政府和联邦/州/市开放数据门户汇编记录，分 9 类：
  - 新公司
  - 地产交易（商业 + 住宅）
  - 建筑许可
  - 诉讼
  - 机械师留置权
  - 判决
  - 联邦税务留置权
  - 州税务留置权
  - 破产
  - **付费 Premium 会员**可按类型、日期、金额筛选，下载 CSV/TXT；Premium Elite 可下载全部 40 个城市。
- 意义：商业周刊**一手做记者线索、一手卖销售线索**；同一份数据既是 S1 也是 S8。
- 来源：Public Records | The Business Journals Help Center — https://support.bizjournals.com/en/articles/9876014-public-records — 2024-09-24 — ✅（主站被 Cloudflare 拦截，帮助中心可访问）

**R-03** | LOCAL, NATL | S1 / S2 | 地产 | 需求信号（JD）
- 结论：地产记者 JD 列出的日常工作：
  - 追踪交易、挂牌、开发提案、成交记录、租金报告、融资；
  - 分析公共记录、"real estate databases"（地产数据库）、公司申报；
  - 信源是开发商和业内人士。
  - KC Business Journal 还要求有市政府报道经验，跑"new projects, incentives and the players"（新项目、激励政策和参与者）。
- 来源（项目已采集 JD 语料）：
  - Curbed / New York Magazine — http://boards.greenhouse.io/voxmedia/jobs/8101003?gh_jid=8101003 — 2026-08 — ✅
  - https://www.journalismjobs.com/1694169-real-estate-and-development-reporter-kansas-city-business-journal — 2026-10 — ✅

**R-04** | LOCAL | S1 | 开发 | 凑合方案（JD 明说不靠蹲会）
- 结论：Omaha World-Herald 的增长条线 JD 写明"isn't about sitting through gavel-to-gavel meetings"（不是从头坐到尾听会），要求用公共记录、竞选财务、合同和预算**主动**发现问题。
- 意义：编辑部希望记者**跳过"听会"这一步直接拿到线索**，与会议摘要类工具的价值主张一致。
- 来源：同 T-09 的 Omaha JD — ✅

**R-05** | LOCAL, NATL | S2 | 地产/商业 | 近两年变化（LLC 所有权透明化倒退）
- 结论：
  - 联邦层面：FinCEN 2025-03 暂缓、2026-08-11 正式取消国内公司的实益所有权（BOI）申报，只剩外国公司要报。
  - 纽约州：LLC Transparency Act 2026-01 生效时，公开数据库已被删掉。
  - 住宅地产：FinCEN 的全现金住宅交易申报规则 2026-03-19 被联邦法院撤销（在上诉中）。
- 证据：纽约租户组织 Los Sures 的人说，大部分稳租楼由 LLC 持有，"tenants don't know who their landlord is"（租户不知道房东是谁）；新法"hasn't made that much of a difference"（没带来多大改变）。
- 意义：**"LLC 背后是谁"仍要记者手工追**（07 G3-03 Investigative Post 用了十几类记录），近两年没有出现公开的制度性解决方案。
- 来源：
  - Five years after the Pandora Papers, transparency laws lose their teeth — https://www.icij.org/investigations/pandora-papers/five-years-after-the-pandora-papers-transparency-laws-lose-their-teeth/ — ICIJ / 2026-10-08 — ✅
  - https://www.fincen.gov/news/news-releases/fincen-permanently-ends-beneficial-ownership-reporting-requirements-millions — FinCEN / 2026-08-11 — ✅（WebFetch）
  - Residential Real Estate Rule — https://www.fincen.gov/rre — ✅

**R-06** | LOCAL, NATL | S8 | 地产 | 竞品事实（行业媒体卖"政策追踪"）
- 结论：The Real Deal 2026-07 正式推出 TRD Policy Pro，把市政厅和州议会对地产的决定做成每日简报和可检索数据库，向个人、团队和企业订阅。
- 证据：总编 Stuart Elliott："Today, it's just as heavily influenced by public policy"（如今地产与公共政策的关系同样紧密）
- 意义：地产媒体把 S1 的"政府决定监控"**直接卖给行业**。
- 来源：The Real Deal launches TRD Policy Pro — https://finance.yahoo.com/real-estate/articles/real-deal-launches-trd-policy-141200440.html — PR Newswire / 2026-07-13 — ✅（付费新闻稿）

**R-07** | LOCAL, NATL | S2 | 地产 | 竞品事实（数据商给记者"供数换曝光"）
- 结论：ATTOM 设有媒体页，主动给记者以下数据：
  - 记录级数据：1.6 亿多块地块、3,000 多个县的产权登记、税务评估、止赎数据；
  - 聚合趋势；
  - 禁发期内（embargo）的报告推送。
  - 由公关团队按需出数。
- 意义：**全国住房趋势稿（S2）基本被数据商的公关供数解决（✅）**。代价是选题被数据商的报告日程牵着走。
- 来源：ATTOM Media — https://www.attomdata.com/media/ — ✅

**R-08** | NATL, LOCAL | S2 | 商业地产 | 市场数据（产权穿透工具价格）
- 结论：Reonomy（Altus 旗下）2026-05 开放线上自助购买，卖点是"LLC-piercing entity resolution"（穿透 LLC 的实体解析），覆盖 5,300 万+ 商业物业。月付或年付，官网元描述"plans start at $400/mo"（$400/月起），导出另计。**没看到记者计划**。
- 来源：
  - https://www.altusgroup.com/product-releases/reonomy-pricing/ — 2026-05-27 — ✅
  - https://www.reonomy.com/pricing/ — ⚠️（价格数字只出现在搜索摘要和元描述，页面主体由 JS 渲染）

### D. 跨条线：近 2 年 AI 渗透与职业变化

**X-01** | NATL | S2 / S3 | 商业/科技 | 需求信号（已发生的使用）
- 结论：SABEW 两场面板（2025-06、2026-02）显示，全国商业记者已经把 NotebookLM 和深度研究当作日常的背景研究与找信源工具。
  - Reuters 的 Ben Welsh 用深度研究预备采访对象：
    - "turned up stuff that would have taken me a lot longer to dig out of Google"（翻出了用 Google 要挖很久的东西）
    - "gave me a sort of bibliography"（给了我一份书目）
  - ICIJ 的 Cota 用它找到"I didn't find on a normal Google search"（普通 Google 搜不到）的潜在信源。
  - SABEW 文章称，一年前 AI 在报道上的用途基本限于转写。
- 来源：
  - https://businessjournalism.org/2025/07/sabew-ai-webinar/ — 2025-07-16 — ✅
  - https://businessjournalism.org/2026/03/sabew-ai/ — 2026-03-11 — ✅

**X-02** | NATL | S5 | 科技/商业 | 风险证据（记者原话）
- 结论：两类顾虑反复出现：
  - **准确性**：Wired 的 Robison 把 Meta 版权案几百页文件喂给 ChatGPT，发现它"pulling quotes that did not exist"（抽出了不存在的引语）。
  - **保密**：Cota 说泄露文件"I will never expose it"（绝不会交给在线 LLM）；Robison 也提醒信源信息可能外泄。
- 意义：**金融、科技调查中的敏感材料不能上传到通用云端 AI**，这里留有空间。
- 来源：同 X-01 两文 — ✅

**X-03** | NATL | S6 | 商业 | 已发生的生产方式变化
- 结论：Fortune 编辑 Nick Lichtenberg 8 个月内发了 600 多篇 AI 辅助稿。做法是把新闻稿、券商研报上传到 NotebookLM 和 Perplexity 生成初稿，再改写和核实。2025 下半年这类稿件占 Fortune 网站流量近 20%。
  - Fortune 设了 "Fortune Intelligence" 署名。
- 证据：他形容 AI "like a sports car that you can crash if you're not careful"（像跑车，不小心就会撞车）
- 来源：
  - https://olereissmann.com/linkpost/fortune-editor-uses-ai-to-write-600-stories-in-six-months/ — 2026-03-27，转述 WSJ — ✅（二手）
  - WSJ 原文付费 [未核实]

**X-04** | NATL | S6 / S9 | 商业 | 已发生的变化 + 劳资冲突
- 结论：Business Insider 设了 "AI News Desk" 署名，由 AI 起草、人工编辑，写快讯和讣闻类短稿。工会（NewsGuild）抗议，Axel Springer CEO 在编辑部公开说这会替代部分岗位。
- 证据："Does it replace jobs here and there? The honest answer is, yes, no doubt about it"（会不会在这里那里取代岗位？老实说，会，毫无疑问）
- 来源：
  - https://www.businessinsider.com/author/business-insider-ai-news-desk — ✅
  - https://newsguild.org/business-insiders-ai-byline/ — NewsGuild / 2025-11-07 — ✅

**X-05** | NATL | S6 | 商业 | 失败案例
- 结论：Quartz 先用 AI 自动生成标准化财报稿，后扩展到"Quartz Intelligence Newsroom"新闻稿，被发现引用其他 AI 垃圾站、来源错乱，并自带"无法保证准确"的免责声明。
- 来源：https://futurism.com/quartz-ai-generated-articles-slop-errors — Futurism / 2025-01-28 — ✅

**X-06** | NATL | S1 / S6 | 金融 | 已发生的变化（通讯社）
- 结论：Reuters 两年来的 AI 编辑工具：
  - AI 摘要覆盖 94% 的重要稿件（之前只有 33%）；
  - "Super Summaries" 财报产品 2025-07 上线后，财报覆盖新增 3,600 多家公司；
  - 从新闻稿发快讯的时间从"几小时"降到"几秒"。
  - 对照：AP 2015 年就用 Automated Insights 每季度自动生成 3,000 多篇财报稿，是人工产量的 10 倍（年代老）。
- 意义：**大公司财报的 S6 已经高度自动化**；剩下的空白是小公司和地方公司。
- 来源：
  - The tools that keep Reuters journalists… ahead of the story — https://www.thomsonreuters.com/en-us/blog/the-tools-that-keep-reuters-journalists-and-its-customers-ahead-of-the-story/ — Reuters CTO / 2026-07-23 — ✅
  - https://www.ap.org/the-definitive-source/announcements/automated-earnings-stories-multiply/ — AP / 2015-06-15 — ✅（年代老）

**X-07** | FREE, NATL | S9 | 商业/科技 | 需求信号（Reddit 语料聚合）
- 结论：项目 Reddit 编码语料中，"商业"条线共 103 条相关帖，以 S9 为主。2025–2026 年的主线是：
  - B2B 和金融内容写手被 GenAI 压价、失去客户（如"I lost everything with GenAI"，因为 GenAI 我失去了一切）；
  - 资深 B2B 记者想转行而不得；
  - 通讯社财经记者倦怠；
  - 数据公司旗下的 AI/风投记者被"numbers go up, numbers go down"（数字涨、数字跌）的条线困住。
- 意义：**商业写作中可被 AI 替代的部分（标准化内容）在萎缩**，原创采访和独家仍有溢价（对照 B-01）。
- 来源：`raw/reddit_coded_*.jsonl` 汇总；例帖：
  - https://www.reddit.com/r/freelanceWriters/comments/1q771ww/returning_business_writer_whats_your_advice/ — 2026-01-08 — ⚠️
  - https://www.reddit.com/r/Journalism/comments/1u9q44j/i_feel_like_ive_pigeonholed_myself_and_dont_know/ — 2026-06-19 — ⚠️

---

## 三、竞品 / 工具表（本范围）

| 工具 | 解决什么（环节） | 主要群体 | 价格 / 付费方 | 状态 | 来源 |
|---|---|---|---|---|---|
| Bloomberg Terminal | 行情、新闻、申报、AI 财报和新闻摘要（S1/S2） | NATL（财经通讯社、大报） | 约 $31,980/年/台，雇主付 | 活跃；2024–25 加 AI 摘要 | B-09 ⚠️ |
| LSEG Workspace / Reuters 内部 Lynx Insight、Super Summaries | 数据异常发现、财报草稿（S1/S6） | Reuters 内部 | 内部自建 | 活跃，扩张中 | X-06 ✅ |
| Factiva（Dow Jones） | 新闻档案检索 + AI Smart Summary（S2） | NATL、企业 | 询价；唯一公开数字是 2013 年 $249–399/用户/月 | 活跃 | 搜索摘要 ⚠️ |
| AlphaSense | 申报、转写、券商研报的 AI 检索（S2/S4） | 投资机构为主；未见记者计划 | Vendr 中位数 $18,375/年 | 活跃 | ⚠️ costbench |
| PitchBook | 私营公司、风投、私募数据（S2） | 科技/创投记者（雇主付） | 单用户约 $12k–20k/年 | 活跃；只有试用 | T-06 ⚠️ |
| Crunchbase | 初创公司融资（S2） | 科技记者、自由撰稿人 | Pro $99/月；Business $199/月 | 活跃；未见记者计划 | T-06 ⚠️ |
| SEC EDGAR 全文检索 / RSS | 申报检索（S2）、按公司或表格订阅（S1） | 全部 | 免费；10 次/秒限速 | 活跃；**无地域提醒** | B-07 ✅ |
| Sqoop | 按地区推送 SEC、专利、联邦法院提醒（S1） | LOCAL 商业记者 | 当年免费 | **已消失**（2025 年记者找不到） | B-06 ✅/⚠️ |
| KFilings | SEC 申报邮件提醒（按公司/表格） | 任意 | 免费（法学教授个人项目） | 证书错误，未能打开 | 搜索摘要 ⚠️ |
| Seeking Alpha Premium | 财报电话会转写（S4） | FREE、NATL | 个人订阅 | 活跃 | B-08 ⚠️ |
| Big Local News warn-scraper + Layoff Watch | WARN 汇总（免费）+ 会员提醒（S1） | LOCAL、NATL（Reuters、LAT 会员） | 数据免费；提醒要机构会员费（金额未公开） | 活跃；39/56 州，维护吃力 | B-03/B-04 ✅ |
| WARNTracker / LayoffAlert / WARNScan 等 | WARN 商业聚合站 | 求职者、HR、销售 | 免费或广告 | 活跃（2026 年新增多家） | 搜索摘要 ⚠️ |
| layoffs.fyi | 科技裁员追踪（S2） | NATL 科技记者 | 免费，需署名 | 活跃，自承低估 | T-04 ✅ |
| ILR Labor Action Tracker | 罢工、劳工抗议数据库（S1/S2） | 学者、活动人士（记者可用） | 免费 | 活跃，人工录入 | B-14 ✅ |
| NewsWhip / Dataminr | 社交和网络趋势监测（S1） | 编辑或机构席位 | 机构采购 | 活跃；一线记者常无权限 | B-11 ⚠️ |
| Muck Rack（记者端） | 记者主页、Trends | 全部 | 记者免费；PR 端付费（Vendr 中位数约 $13k/年） | 活跃 | ✅ muckrack.com/pricing |
| OpenSOSData 等 SOS 数据商 | 州商业登记批量和新注册（S1/S2） | B2B 销售；记者可用 | $2.50/千条起 | 活跃 | B-13 ✅ |
| OpenCorporates | 公司登记（S2） | NATL | 调查记者可免费 | 活跃 | 05 C-46 |
| Business Journals Public Records / BizLeads | 每周本地公共记录汇编（S1/S8） | 商业读者（付费会员）、销售 | Premium 会员；BizLeads $66/月起（2020） | 活跃 | R-02 ✅；07 G2-07 |
| ATTOM（媒体供数） | 产权、止赎、翻炒数据和趋势（S2） | NATL、LOCAL 住房记者 | 对记者免费（PR 换曝光）；商业 API 付费 | 活跃 | R-07 ✅ |
| Reonomy | 商业地产产权 + 穿透 LLC（S2） | 商业地产从业者 | 约 $400/月起 | 2026-05 起可线上自助买 | R-08 ✅/⚠️ |
| Regrid | 全国地块、产权数据 | 规划、地产 | 询价 | 活跃（每月更新约 200 县） | 搜索摘要 ⚠️ |
| Shovels / PermitMint / Permitlify | 建筑许可聚合 | 地产、建材；PermitMint 对记者免费 | Shovels $0/$599/$999 每月 | 活跃 | 07 G3-01/02、G2-09 |
| Hamlet | 会议转写 + 开发项目提醒 | 开发商付费；记者免费 API | 约 $1,000/月起 | 活跃 | 07 G3-08 |
| United Robots DataDesk | 本地公共数据线索推送 | LOCAL 编辑部 | 未公开 | 2026 年下半年上线 | 07 G3-07 |
| TRD Policy Pro | 纽约地产政策追踪数据库 + 简报（S1/S8） | 地产从业者 | 个人/团队/企业订阅（价格未见） | 2026-07 上线 | R-06 ✅ |
| NotebookLM / ChatGPT·Claude·Gemini 深度研究 | 人物和公司背景、找信源（S2/S3）；Fortune 用来起草（S6） | NATL 商业/科技记者 | 免费或个人订阅 | 快速渗透 | X-01/X-03 ✅ |

---

## 四、能自己解决 / 不好解决

### 能自己方便解决 ✅
- **上市公司申报的检索**：EDGAR 全文检索免费，2001 年起（B-07）。
- **全国住房、止赎、翻炒趋势数字**：ATTOM、Redfin 等数据商主动供数（R-07）。
- **人物和公司背景速成**：NotebookLM 加深度研究，全国商业/科技记者已普遍在用（X-01、T-02）。
- **科技裁员总量**：layoffs.fyi 免费、可引用（T-04）。
- **单家公司的州登记查询**：各州务卿网站免费。

### 费力但能 ⚠️
- **财报电话会转写和大公司财报稿**：要付费，或依赖通讯社自动化（B-08、X-06）。
- **按公司/表格的 SEC 提醒**：要自己写脚本，或用小型免费站（B-07）。
- **本地新注册公司、批量登记数据**：要买数据，还要有处理能力（B-13）。
- **私营公司和融资数据**：Crunchbase $99/月可负担；PitchBook 只能靠雇主（T-06）。
- **宏观数据断档期的替代数据**：能拿到，但口径冲突，核实成本高（B-02）。
- **AI 研究结果的核实**：引语可能是编的，敏感材料不能上传（X-02）。

### 不好自己解决 ❌
- **"只推送我报道地区"的 SEC、WARN 等申报提醒**：Sqoop 消失后，市面上没有面向记者的地域化提醒；WARN 要跨几十个州门户，斯坦福团队维护都吃力（B-03、B-04、B-06）。
- **跨很多辖区监控议程、zoning、许可，捕捉开发项目早期信号**：一人对 109 个政府（R-01）；JD 要求不靠蹲会（R-04）；现有聚合要么是半月级，要么主要卖给开发商（07 G3-02、G3-08）。
- **LLC 背后的实际所有人**：联邦 BOI 和纽约公开库都落空（R-05）；靠人工跨十几类记录拼接（07 G3-03）。
- **被 NDA 和代号隐藏的数据中心等大项目**：只能靠记录申请事后挖（T-09）。
- **一线记者够不着机构级监测工具**：NewsWhip、Dataminr、终端的席位在编辑或机构那里（B-11、B-09）。
- **地方小公司、地方雇主的财报和经营动态**：通讯社自动化只覆盖上市公司；地方要靠源头网络（B-12）。

---

## 五、最重要的 5 条发现

1. **"按我的地盘推送申报"是被反复点名、却没人在做的空白。**
   - 记者 2025 年在找"只推送我报道地区"的 SEC 提醒，以前用的 Sqoop 已经消失（B-06）。
   - WARN 的地域化提醒只有斯坦福 BLN 在做，覆盖 39/56 州，修爬虫修到"painful"（痛苦），提醒只给会员（B-03、B-04）。
   - 已经有付费方：Reuters 和 LAT 是 BLN 首批会员。
2. **住房/地产线的痛点集中在"跨辖区 + 早期信号"。**
   - 一人跨 109 个政府看议程（R-01）。
   - JD 明说不要靠蹲会（R-04）。
   - 数据中心用 NDA 和代号刻意隐藏早期信号（T-09）。
   - 行业媒体已把同一类监控卖给地产从业者：TRD Policy Pro、Business Journals Public Records、Hamlet（R-06、R-02）。
3. **LLC 所有权透明化 2025–2026 年全面倒退**：联邦 BOI 取消、纽约公开库被删、住宅现金交易申报规则被撤销（R-05）。"谁是房东/业主"仍是地产调查里最大的手工活。
4. **商业线的 AI 已经从"研究"走到"量产"。**
   - 全国记者普遍用 NotebookLM 和深度研究做 S2/S3（X-01）。
   - Fortune 和 BI 用 AI 起草，Fortune 的 AI 辅助稿约占 20% 流量；Reuters 财报覆盖新增 3,600 家（X-03、X-04、X-06）。
   - 代价是：财经记者 80% 时间花在核实来源上（B-10）；B2B 写手收入崩塌（X-07）。
5. **地方商业周刊记者是这三条线里资源最少的一线。**
   - 薪资中位数 $66,667，近半数在岗不到 1 年，所在编辑部大多不招人（B-01）。
   - JD 却要求一人跑全城商业并天天抢独家（B-12）。
   - 公司自己在卖公共记录，但这些数据**对记者的 S1 是否够用**，证据不足。

---

## 六、证据薄弱处

- **商业周刊/地方商业记者如何用 Public Records 找线索**：bizjournals.com 被 Cloudflare 拦截，没有拿到记者自述。建议访谈或找 ACBJ 记者的公开分享（播客、SABEW 会议录音）。
- **劳动记者原话**：没拿到。WARN 和罢工追踪只有数据源侧证据。可以查 SABEW、Labor Journalism 相关网络，或 Capital & Main 的方法论。
- **终端和数据库价格**：Bloomberg、PitchBook、AlphaSense、Factiva 都是第三方或买方数据，没有记者/媒体折扣的官方说明。
- **Reddit 原帖**：6 条引语来自项目已采集的语料，本轮无法直连 reddit.com 复核，标 ⚠️。其中一帖（T-03 第二帖）发帖者可能是工具开发者。
- **科技条线 S1 的具体渠道**（公司 changelog、招聘页、FCC/专利、Discord 爆料）：只有一条小媒体的原话；全国科技记者的找线索流程没有直接自述，只有 JD 和 SABEW 面板。
- **地产记者用 ATTOM/Regrid/Reonomy 的实际频率**：只有供给侧页面，没有采购或使用调查。
- **Business Journals BizNotify（2026-02，"AI-ready outreach"）和 ACBJ AI 政策**：页面被拦截，只看到搜索摘要，没有写入正文。
