# 05 竞品/工具市场地图：S1 发现线索 · S2 背景研究 · S3 找信源

## 0. 本文件说明

- **覆盖范围**：美国记者在 S1（发现线索）、S2（背景研究）、S3（找信源）三个环节可用的工具与竞品，共约 50 个产品/项目。分 6 类：①会议/政务监测；②突发/社交/警情监测；③法院/公共记录/文档研究；④信源撮合；⑤相邻品（AI 自动生成本地新闻，抢的是 INDIE/LOCAL 的读者，不是记者工具）；⑥已关停/转型复盘。
- **来源数**：实际打开（WebFetch）并用于结论的页面约 62 个；另有约 15 条只在搜索摘要里看到、没能打开原页的信息，已标 `⚠️`/`[未核实]`，或者直接不用。
- **主要局限**：
  1. 本轮 WebSearch 配额（多个 agent 共用）中途用完。**AP Local News AI 项目、Courthouse News Service、Factiva/Nexis 定价、电视台派题台专用工具（TVEyes 等）、UniCourt** 都没来得及做定向检索，只能列为待补。
  2. 不少官网（Trellis、MuckRock 定价页、Broadcastify、UniCourt、Hamlet、OpenMHz、Axios、Press Gazette 部分页面）对抓取返回 403/405/429。这些产品的数字改用媒体报道或第三方页面核实，并注明了口径。
  3. 定价绝大多数是"报价制"，公开价很少。凡是第三方估算（Vendr、Sacra 等）都标为「报道价/估算」。
  4. 本文件以**竞品事实（供给）**为主，不能当作需求证据。真正的需求信号只引用了记者原话或使用行为（Chalkbeat、Midcoast Villager、Patch 编辑、ICIJ/WSJ 记者等）。
- 类型标签：`竞品事实` / `市场数据` / `需求信号` / `凑合方案`。群体：LOCAL / TV / INDIE / NATL / FREE。

---

## 1. 会议 / 政务监测（S1 为主，兼 S2）

### C-01 | LOCAL, INDIE | S1, S2 | 竞品事实
**Hamlet（myhamlet.com）**：融资约 1,000 万美元的 AI 会议检索公司。主要靠房地产开发商赚钱，记者版免费。2026 年 2 月称已覆盖 3,000+ 个地方机构。
- 证据：
  - 2022 年由 Sunil Rajaraman 创立，融资 1,000 万美元，尚未盈利，收入"数十万美元"。企业客户十几家，多是房地产开发商、数据中心开发商和零售商。政府客户只有 Saratoga 一家。面向本地记者免费提供，当时"已有少数记者在用"。（Nieman Lab 2026-01-13）
  - 2026-02-18 新闻稿：监测 "more than 3,000 city councils, planning commissions and other governing bodies"（3,000+ 个市议会、规划委员会等机构）。已处理近 5 亿词的转录文本，每周新增几十个机构。数据**每周刷新**，日更还在计划中。功能包括关键词提醒和"数据中心/区划/住房"情绪指数。有免费层，另有 14 天试用；付费价未公开。
  - 2024-06 与 Palo Alto 合作试点，生成市议会摘要，内容由 Hamlet 独立编辑。
  - AJP 的 AI 工具指南列出的缺点："只在房地产开发特别活跃的城市可用"。
- 来源：
  - Highlighting the funniest moments… — https://www.niemanlab.org/2026/01/highlighting-the-funniest-moments-this-startup-aims-to-bring-public-meetings-into-the-tiktok-era/ — Nieman Lab 2026-01-13 — ✅
  - Hamlet launches nationwide public meeting coverage… — https://www.publicceo.com/2026/02/hamlet-launches-nationwide-public-meeting-coverage-over-3000-local-governments-videos-now-discoverable/ — PublicCEO 2026-02-18 — ✅
  - Hamlet partners with the City of Palo Alto — https://www.publicceo.com/2024/06/hamlet-partners-with-the-city-of-palo-alto-to-provide-ai-powered-city-council-summaries/ — 2024-06-07 — ✅
  - AJP field guide vets AI vendors — https://www.niemanlab.org/2025/10/the-american-journalism-projects-new-field-guide-vets-ai-vendors-for-local-newsrooms/ — Nieman Lab 2025-10-22 — ✅
  - 官网 myhamlet.com — ❌（429）

### C-02 | LOCAL | S1 | 竞品事实 + 需求信号
**LocalLens**：2025-11 被 American Public Media 收购。此前是 Chalkbeat 的主力工具，企业账户监测约 80 个学区（30 个州）。
- 证据：
  - Chalkbeat 先自建了工具，后来"暂时"放弃自建，改用 LocalLens。随后从纽约试点扩到全部 8 个城市分社，企业账户监测约 80 个学区、30 个州。（Nieman Lab 2025-03）
  - 问题：说话人识别差（一场会有 6 个以上董事会成员）。摘要粗糙，必须人工核实。改一次提示词都要工程师介入。Chalkbeat 记者 Gorski 说 "It is a tip."（它只是线索）
  - APM 公告（2025-11-26）：仍在 beta，"available to select public media organizations and qualified newsrooms"（只对部分公共媒体和合格新闻机构开放）。早期用户有 MPR。未公布覆盖数和价格。
- 需求信号（记者原话，Nieman 2025-03）：Dellinger 说 "I'm not able to physically go to every single board meeting"（我没法亲自去每一场董事会会议）；又说 "Even watching them online, or looking at all the agendas, can take up an entire day."（就算线上看录像、翻议程也要花一整天）——这是"凑合方案很费力"的直接证据。
- 来源：
  - Local newsrooms are using AI to listen in on public meetings — https://www.niemanlab.org/2025/03/local-newsrooms-are-using-ai-to-listen-in-on-public-meetings/ — Nieman Lab 2025-03 — ✅
  - APM acquires LocalLens — https://www.americanpublicmedia.org/blog/american-public-media-acquires-locallens-ai-tool-to-empower-journalists-nationwide — APM 2025-11-26 — ✅
  - 官网 thelocallens.org — ❌（DNS 解析失败）

### C-03 | LOCAL, INDIE | S1 | 竞品事实 + 需求信号
**Civic Sunlight（缅因州）**：用 LLM 把会议做成免费 newsletter。截至 2024-12 唯一付费客户是一家缅因报纸，把它当"线索通讯社"用。出过事实性错误。
- 证据：
  - 2024 年底覆盖 Concord、Nashua、缅因 24 个市镇，另有 MA/VT/NY/NJ/PA 少量地点。每场会议成本约 25 美元。商业模式未定（面向公众的 newsletter 还是面向媒体的 wire）。早期用单个 chatbot 时"riddled with incredible amounts of errors and hallucinations"（错误和幻觉多得惊人）；之后改用 8 个 LLM 加自研代码。曾报道 Concord 议会"已批准"某项拨款，实际只是讨论。Concord Monitor 记者明确说他们的报纸绝不会直接发布它的产出。（Concord Monitor 博客 2024-12-31）
  - CJR 2025-05：免费 newsletter 覆盖约 20 个镇，注册 1,000+。Midcoast Villager 的 Seitz-Wald 称之为 "a force multiplier, an extremely useful efficiency tool"（力量倍增器，极有用的效率工具）。创始人自估准确率 90–95%。
  - 官网未公布价格，有"Tools for Newsrooms"入口。
- 来源：
  - You can get a local news-ish product built entirely by AI — https://granitegeek.concordmonitor.com/2024/12/31/you-can-get-a-local-news-ish-product-built-entirely-by-a-i-should-i-be-worried/ — Concord Monitor 2024-12-31 — ✅
  - The Rise of AI Local News — https://www.cjr.org/analysis/ai-local-news-civic-sunlight-maine.php — CJR 2025-05-15 — ✅
  - civicsunlight.ai — ✅

### C-04 | LOCAL | S1 | 竞品事实
**citymeetings.nyc**：个人开发者 Vikram Oberoi 做的单城项目（只覆盖纽约市议会和宪章修订委员会），AI 加人工审核，24 小时内出分段摘要。2025 年被宪章修订委员会付费采购。
- 证据：自 2024-08 起，市议会会议片段 24 小时内发布；工具"designed to enable human oversight every step of the way"（每一步都设计成可人工把关）。给 Bloomberg 数据新闻组做过分享。页面没说有记者付费。
- 来源：About — https://citymeetings.nyc/about/ — ✅；NY1 报道 2024-10（只看到搜索摘要）⚠️

### C-05 | LOCAL, INDIE | S1 | 竞品事实
**SeeGov（非营利）**：面向新闻机构和 civic creator 的会议高光剪辑与关注工具，目前免费，"之后推出付费方案，每档包含有限个机构"。
- 证据：可按 ZIP/县/州关注机构；带署名的高光片段来自 The Alexandria Brief、The Frame 等超本地媒体；新用户需审核。
- 来源：https://seegov.org/ — ✅

### C-06 | LOCAL | S1 | 竞品事实
**WallFly**：政府会议"转录 + 关键词即时提醒"，客户是公共事务/游说团队。新闻机构只有一个"WallFly Wire"入口。未公开价格；不需长期合同，约 1 个工作日开通。立法数据来自 LegiScan。
- 来源：https://www.getwallfly.com/ — ✅

### C-07 | LOCAL, INDIE | S1 | 竞品事实 + 凑合方案
**City Bureau Documenters**：用"付费给居民去开会做笔记"的人力方案。2022 年获 1,000 万美元，截至 2025-06 覆盖 16 个州的 24 个社区，培训 4,000+ 人，还在做 AI 原型。
- 证据：2022 年获 Stronger Democracy Award 1,000 万美元；累计向社区发放约 100 万美元；正在用 Documenters 的笔记做 AI 原型。（E&P 2025-06-24）
- 意义：说明"有人去会场、有人写笔记"这种需求真实存在，但扩张靠资助驱动，覆盖只有几十个社区。
- 来源：City Bureau is scaling civic journalism… — https://editorandpublisher.com/stories/city-bureau-is-scaling-civic-journalism-one-documenter-at-a-time,256393 — E&P 2025-06-24 — ✅；documenters.org — ❌（403）

### C-08 | LOCAL | S1 | 竞品事实
**CivicSearch（civicsearch.org）**：基于 LocalView 转录语料的会议搜索和提醒。目录站称覆盖美加 547 个市镇。
- 证据：官网正文抓不到内容；数字只出现在 civictech 目录的搜索摘要里。
- 来源：civicsearch.org — ⚠️（页面只有标题）；civictech.guide/listing/civicsearch — ⚠️（301，未展开）。**[未核实] 547 这个数字**。

### C-09 | LOCAL | S1 | 竞品事实（半停滞）
**Council Data Project（开源）**：列出 18 个部署城市（Seattle、Denver、Boston、Atlanta 等），外加 3 个由他人维护。官方警告"部分部署已不再采集新数据"，无人维护的实例会被归档。
- 来源：https://github.com/CouncilDataProject — GitHub（核心仓库最近更新 2026-02）— ✅

### C-10 | LOCAL | S1 | 竞品事实（停滞）
**Councilmatic（DataMade/PPF）**：老一代 Legistar 抓取开源项目，代表实例为 NYC/Chicago/Philly/LA Metro。找到的资料大多停在 2015–2016 年，近况不明。**[未核实，只看到搜索摘要]**

### C-11 | LOCAL, INDIE | S1 | 竞品事实（停滞迹象）
**Agenda Watch（Big Local News × RJI）**：2023-06 上线的免费议程抓取平台。原计划的"历史检索 + 关键词提醒"是否上线，没有公开证据。RJI 标签页的最近一篇文章停在 2023-08。
- 来源：https://rjionline.org/tag/agenda-watch/ — ✅（只有文章列表）

### C-12 | LOCAL, NATL | S1, S2 | 竞品事实
**CalMatters Digital Democracy**：州议会层面的"AI Tip Sheet"。AI 扫描所有听证发言、竞选献金和投票，找出异常，推送给注册记者。已扩展到夏威夷（Honolulu Civil Beat），获 Reid Hoffman/Lever for Change 每年 180 万美元、为期 5 年的资助，准备推向更多州。
- 证据：工具 "doesn't write stories, journalists will"（不写稿，稿子由记者写）；"reporters throughout the state now use" Tip Sheets（全州记者都在用 Tip Sheet），但没有给出具体数字；2025 年获艾美奖。
- 意义：**这是本次调研中唯一一个"AI 主动推送选题"且已有州内多家新闻机构使用的项目**。形态与我方"会议议题发现"最接近，只是层级在州议会。
- 来源：
  - CalMatters Digital Democracy fuses journalism, AI and data — https://calmatters.org/inside-the-newsroom/2024/04/calmatters-digital-democracy-fuses-journalism-ai-and-data/ — 2024-04-09（2026-02 更新）— ✅
  - Trust challenge win — https://calmatters.org/inside-the-newsroom/2026/04/trust-challenge-win/ — 2026-04-14 — ✅

### C-13 | NATL, LOCAL | S1, S2 | 竞品事实 + 市场数据
**立法追踪（Plural/Open States、BillTrack50、Quorum、FiscalNote）**：客户是游说/政府事务团队，价格对记者偏高。开放数据层已被并购。
- **Plural**：Essential 每席位每年 609 美元（或每月 59 美元）；Professional 每年 5,000 美元（含 AI 摘要）；Enterprise 定制。覆盖国会、50 州、DC、波多黎各。**无记者方案**。Open States 官网横幅写着 "Open States is now Plural / SAI360"，大部分工具已停用，迁到 Plural。SAI360（STG 系）于 2025-12 收购 Plural。
- **BillTrack50**：法案检索"free and unlimited"，提醒等功能需付费（官网未显示价格），有 30 天试用。
- **Quorum**：Vendr 采购数据显示中位数每年 23,500 美元，区间约 16.5k–30.7k 美元（Quorum State）。
- **FiscalNote**：2025 年 Q4 营收 2,220 万美元（上年同期 2,950 万）；ARR 从 1.07 亿降到 8,410 万美元（主要因剥离资产）；董事会在"评估战略选项"。旗下 CQ/Roll Call 保留。
- 来源：
  - https://pluralpolicy.com/pricing/ — ✅
  - https://open.pluralpolicy.com/ — ✅
  - SAI360 收购 — themiddlemarket/paulhastings ❌（403/429），收购日期只看到搜索摘要 ⚠️
  - https://www.billtrack50.com/ — ✅
  - https://www.vendr.com/marketplace/quorum-inc — ✅（第三方估算）
  - FiscalNote Q4 2025 — 搜索摘要引自 businesswire/fiscalnote.com ⚠️（官网 403）

### C-14 | LOCAL | S1 | 市场数据（供给方）
**Granicus/Legistar/CivicPlus**：政府会议软件供给方，是所有会议抓取工具的上游。Granicus 全公司 7,000+ 公共部门客户；2025-07 产品更新称生成式 AI 摘要"即将推出"。**[未核实]**（只看到搜索摘要，没有打开原页）
- 意义：如果供给方直接在 Legistar 内置 AI 摘要，第三方"转录 + 摘要"层就会被商品化。差异化必须放在跨辖区检索、异常发现和长期 timeline 上。

---

## 2. 突发 / 社交 / 警情监测（S1）

### C-20 | TV, NATL, LOCAL | S1 | 竞品事实 + 需求信号
**Dataminr for News**：行业标杆，自称服务 "over 1,500 newsrooms"（1,500 多家新闻机构），信号源 "over 1 million public data sources across 150+ languages"（100 多万个公开数据源，150 多种语言）。价格不公开。公司重心已明显转向安全和政府市场。
- 证据：
  - 2014 年与 CNN、Twitter 合作推出新闻版。2025 年三轮共融资 4.85 亿美元（含可转债）。2025-10 以 2.9 亿美元收购网络威胁情报公司 ThreatConnect。（Wikipedia、SecurityWeek）
  - 价格：Poynter 2017 年报道按受众规模定价、不公开；第三方说新闻机构合同"每年数万美元"，**[报道价，无一手出处]**。
  - 需求信号/使用行为：Patch 全国突发编辑 Anna Schier 在用。她的做法是先查来源，"I always look at the source of where it's coming from first"（我总是先看消息从哪来）。文章也指出，信息稀少的社区代表性不足，小团队会被大量提醒淹没。（Media Copilot 2026-03，基于 Patch 案例）⚠️（二手整理）
- 来源：
  - https://en.wikipedia.org/wiki/Dataminr — ✅
  - https://www.securityweek.com/dataminr-to-acquire-threatconnect-for-290-million/ — 2025-10-21 — ✅
  - https://resources.dataminr.com/news/dataminr-for-news-datasheet — ✅
  - https://mediacopilot.ai/can-you-trust-dataminr-with-your-breaking-news-workflow/ — 2026-03-03 — ✅（内容属二手整理）

### C-21 | TV, LOCAL | S1 | 竞品事实
**Samdesk**：2023-01 完成 1,350 万美元 A 轮（McRock 领投）。客户是企业安全、政府和 NGO，**没有公开的新闻机构客户**。数据源包括 Nextdoor 公共机构帖（2023 年起）、Reddit 官方 API、Snapchat。
- 来源：
  - https://samdesk.io/blog/samdesk-raises-series-a — ✅
  - https://www.samdesk.io/news-and-updates/samdesk-taps-into-nextdoor-as-their-first-ever-public-data-partner — ✅

### C-22 | TV, LOCAL, INDIE | S1 | 竞品事实 + 凑合方案
**Broadcastify / OpenMHz（警用电台流）**：记者"听 scanner"这个凑合方案的基础设施。只有原始音频，没有转录，也没有提醒。
- Broadcastify：直播免费；Premium 提供每个 feed 最长 365 天的录音存档，付费价没能从官网核实（论坛用户提到 84 美元/年，**[未核实]**）。实时 feed 数约 7,000+（搜索摘要显示首页"Live Feeds - 7,165/7,346"）⚠️。官网和帮助中心对抓取返回 403/405。
- OpenMHz：志愿者用开源 trunk-recorder 采集，按单次通话存档。App 商店页称覆盖 225+ 个系统、存档 30 天 ⚠️。官网 403。
- 加密趋势：RTDNA 把电台加密列为 2023 年头号议题。NYPD（2023）、芝加哥、科罗拉多和加州多地已加密。
- 来源：
  - Why Radio Encryption Is RTDNA's Biggest Issue In 2023 — https://rtdna.org/news/why-radio-encryption-is-rtdnas-biggest-issue-in-2023 — ✅
  - broadcastify.com / openmhz.com — ❌

### C-23 | LOCAL, INDIE | S1 | 竞品事实（**最直接竞品**）
**PSST（Public Safety Scanner Tool）**：Verso 开发，Open Vallejo、RJI、Big Local News 合作，Lenfest 出种子资金。全天候监听 scanner 的紧急提示音，通过 Slack/邮件推送"初步转录 + 音频链接"，**对新闻机构免费**，由 Big Local News 托管。第一阶段（提醒 + 转录）计划 2026 年秋公开，第二阶段做 LLM 模式分析；计划与至少 10 家新闻机构测试。支持 Broadcastify。
- 需求信号（文中原话）："Listening to the scanner 24/7 takes time that most editorial teams do not have."（全天候听 scanner 的时间，大多数编辑部都没有）
- 来源：We are building a tool to help newsrooms listen to emergency scanners — https://rjionline.org/news/we-are-building-a-tool-to-help-newsrooms-listen-to-emergency-scanners/ — RJI 2026-08-03 — ✅

### C-24 | （消费者端）| S1 | 竞品事实 + 风险案例
**CrimeRadar（Scoopz LLC）**：用 AI 总结公开调度音频并推送给居民，Android 安装量 100 万+（评分 4.8，5 万条评价），会员每月 9.99 美元或每年 79.99 美元。**多次误报，被警方公开点名。**
- 证据：
  - Android 包名是 `com.newsbreak.crimeradar`，开发者 Scoopz LLC，2025-05-22 首发。**⚠️ 包名前缀显示可能与 NewsBreak 有关，关系未核实；如属同一集团，应视为内部协同/竞争关系，需内部确认。**
  - 误报案例：2025-12-09 把俄亥俄 Streetsboro 小学的 "fire alarm" 听成 "firearm"，警长称其为"fake"，公司承认是"serious transcription error"（严重转录错误）。科罗拉多 Longmont 发出不存在的公寓火灾；把演习当真实火灾；把 "fire rider" 听成 "firefighter"。Boulder 警方说 "I wouldn't rely on them"（我不会依赖它们）。（Firehouse 2026-03-01；News5 Cleveland）
  - Nextdoor 的 AI 提醒（Firehouse 称由 Samdesk 驱动）也误报过"联邦设施枪手"。
- 意义：**"scanner → AI 摘要 → 推送"已在消费端被大规模做出来，但准确率是公开痛点**。面向记者的版本必须保留原音频，并把结果定位为"线索"而不是"事实"。
- 来源：
  - https://techdevnotes.com/apps/android/crimeradar-dispatch-alerts/com.newsbreak.crimeradar — ✅
  - https://www.firehouse.com/technology/artificial-intelligence/news/55360775/ai-powered-alert-apps-issue-inaccurate-incident-notifications-in-colorado — 2026-03-01 — ✅
  - https://www.news5cleveland.com/news/local-news/investigations/crimeradar-app-said-shots-were-fired-at-a-streetsboro-elementary-school-it-wasnt-true — ✅

### C-25 | TV, LOCAL | S1 | 竞品事实
**Citizen**：在大城市自建无线电接收器监听调度频道，员工解读后推送。覆盖 60+ 个美国城市（维基口径）。累计融资约 1.13 亿美元（维基所列各轮相加：~4,000 万 + 7,300 万）。2023-03 Sequoia 退出董事会席位。2025-04 与 Axon 合作，让执法方查看 Citizen 视频并发布验证提醒。
- 意义：Citizen 证明"人工 + 电台"模式能跑通，但它是消费者 app，不服务记者，也没有记者付费产品。
- 来源：https://en.wikipedia.org/wiki/Citizen_(app) — ✅

### C-26 | LOCAL, TV | S1 | 竞品事实
**PulsePoint**：截至 2024-01，4,950+ 个社区的调度中心接入，用户 300 万+。公众看到的事件只保留 24 小时，最多 100 条，医疗类细节被遮蔽；部分地区已移除警力编号。
- 来源：https://en.wikipedia.org/wiki/PulsePoint — ✅

### C-27 | NATL, LOCAL | S1 | 竞品事实（被收购）
**NewsWhip**：2025-07-30 被 Sprout Social 收购，现金 5,500 万美元 + 最多 1,000 万美元对赌。定位转向品牌危机/预测型媒体情报。
- 来源：https://pulse2.com/sprout-social-buying-newswhip-for-up-to-65-million-for-boosting-predictive-intelligence/amp/ — 2025-08-04 — ✅

### C-28 | NATL | S1, S5 | 竞品事实（收缩）
**Storyful（News Corp）**：爱尔兰商业媒体报道其亏损扩大到 4,200 万至近 5,000 万欧元，裁员主要在企业情报部门，新闻部门也有。原文 403，**[未核实，只看到摘要]**。

### C-29 | NATL, LOCAL | S1 | 竞品事实
**Meltwater / Talkwalker 类媒体监测**：价格不公开。第三方（Vendr 口径）报中位数每年约 2.5 万美元；通常要求 12 个月起签并自动续约，是最常见的投诉。客户主要是 PR/品牌方。原页 403，**[未核实]**。

### C-30 | 全体 | S1 | 凑合方案
**Google Alerts**：免费，但"漏报、延迟、结果骤减"的抱怨长期存在。能找到的证据主要是 2013 年前后的 BuzzFeed/Search Engine Land 文章（**年代老**），没有找到 2023 年后的记者原话。**[证据薄弱]**

---

## 3. 法院 / 公共记录 / 文档研究（S2，兼 S1）

### C-40 | NATL, LOCAL | S1, S2 | 竞品事实
**CourtListener / RECAP（Free Law Project，非营利）**：1,000 万+ 份判决，RECAP 收录"几乎所有联邦案件"、数亿条 docket 记录；典型一天发出数万条提醒，用户 100 万+。**联邦层免费方案已经很强**。
- 来源：https://free.law/projects/courtlistener — ✅

### C-41 | NATL, LOCAL | S2 | 市场数据
**PACER**：每页 0.10 美元，单份文件封顶 3 美元，音频 2.40 美元；每季度 ≤30 美元免收。页面没有 2024–2026 年费率变化。
- 来源：https://pacer.uscourts.gov/pacer-pricing-how-fees-work — ✅

### C-42 | LOCAL, NATL | S1, S2 | 竞品事实
**Trellis（州法院）**：官网口径"45 states and 3,335 courts in 2,481 counties"（45 个州、3,335 个法院、2,481 个县），但不同页面的数字互相矛盾。累计融资约 3,500 万美元（2023-08 B 轮 1,500 万）。网站订阅按内容浏览量计费，API 另行报价。第三方称 99 美元/月起 **[未核实]**。面向律师，**没有记者方案**。
- 2022-10 时还只有 21 个州（LawSites）。说明州法院数据可以靠资本堆出来，但县级文书获取仍然参差（只有部分县可调取或购买文书）。
- 来源：
  - https://www.vaquill.ai/blog/trellis-api-state-court-data-what-it-offers — 2026-08 — ✅（第三方汇总）
  - https://www.lawnext.com/2022/10/trellis-expands-its-court-analytics-platform-into-another-five-states-for-total-coverage-of-21-states.html — ✅
  - trellis.law — ❌（403）

### C-43 | NATL | S2 | 竞品事实（被收购）
**Docket Alarm → Clio Docket**：Fastcase 2018 年收购 Docket Alarm；2023 年 vLex 与 Fastcase 合并；2025-06 Clio 以 10 亿美元收购 vLex；2025 年更名 Clio Docket，2026-08 并入 Clio Work，"more than 1 billion filings"（10 亿+ 份文书）。卖给律所，没有记者定价。
- 来源：https://www.lawnext.com/2026/08/clio-docket-is-now-in-clio-work-combining-an-ai-workspace-with-access-to-more-than-1-billion-court-filings.html — ✅

### C-44 | NATL, INDIE, FREE | S2 | 竞品事实
**MuckRock + DocumentCloud（非营利，2018 年合并）**：FOIA 代发与文档托管。组织版每月 50 个请求，DocumentCloud 每月 5,000 AI 积分；非营利新闻机构有补贴价。当前价格页 403，具体美元 **[未核实]**（2019 年口径：组织版低至 25 美元/月）。
- 来源：https://en.wikipedia.org/wiki/MuckRock — ✅；accounts.muckrock.com/plans — ❌

### C-45 | NATL, LOCAL | S2 | 竞品事实
**Google Pinpoint（Journalist Studio）**：面向记者的文档、音频检索和表格抽取工具，免费（官网未写价格，生成式 AI 功能需申请）。第三方称每个 collection 上限 10 万份文档 **[未核实]**。
- 来源：https://journaliststudio.google.com/pinpoint/about — ✅

### C-46 | NATL | S2 | 竞品事实
**OpenCorporates**：API 方案为每年 2,250 / 6,600 / 12,000 英镑（每月 500 / 2,500 / 5,000 次调用）；**调查记者、NGO 和高校可申请免费大规模使用**。
- 来源：https://opencorporates.com/pricing/ — ✅

### C-47 | NATL, LOCAL | S2 | 需求信号
**通用 LLM（NotebookLM、ChatGPT/Claude/Gemini 深度研究）正在吃掉 S2**：WSJ 记者 Herrera 用 NotebookLM 准备 Larry Ellison 人物稿，说 "It really sped up the reporting process for me"（大大加快了我的采访进度）。ICIJ 的 Cota 用深度研究找到"didn't find on a normal Google search"（普通 Google 搜不到）的潜在信源，但她表示绝不会把泄露文件上传到在线 LLM。
- 意义：S2 的"通用背景研究"正被通用 AI 吞掉；剩下的空白是**专有/难抓的本地结构化数据**（县法院、地方会议、警情）。
- 来源：New AI tools that are genuinely useful to business journalists — https://businessjournalism.org/2026/03/sabew-ai/ — SABEW 2026-03 — ✅

### C-48 | NATL | S2 | 凑合方案 + 市场数据
**人物背调库（Accurint/LexisNexis、TLOxp）**：ProPublica 2016 年指出这是调查记者最常用的两种（**年代老**）。GIJN 与 LexisNexis 法治基金会的合作在 2024-02 结束（只看到搜索摘要 ⚠️）。现行定价 **[未核实]**。Factiva/Nexis 定价没能检索，**[待补]**。

### C-49 | — | S1, S2 | 需求信号（供给侧缺口）
**州/县法院在线获取不一致**：RCFP 指出各州初审法院的在线访问差异很大；内华达 2024 年调查显示多数法院没有在线文档。**[只看到搜索摘要，原文未打开 ⚠️]**

---

## 4. 信源撮合（S3）

### C-60 | 全体 | S3 | 竞品事实 + 死亡复盘
**HARO → Connectively → 关停 → 被 Featured 复活**：
- 2008 年由 Peter Shankman 创立，自称 80 万+ 信源、5.5 万记者/博主；2010 年被 Vocus 收购，2014 年随 Vocus 并入 Cision。Cision 改名 Connectively 后，于 2024-11-08 通知用户 2024-12-09 关停，理由是"concentrate our efforts on enhancing our core offering, CisionOne"（集中精力做核心产品 CisionOne）。2025-04-15 卖给 Featured.com，2025-04-22 恢复每日邮件。
- 新东家 Farmiloe 承认面临假人设和 AI 生成投稿问题，加了 AI 文本/头像检测、LinkedIn 必填和零容忍封禁。PR 从业者普遍认为 Cision 时期"请求质量和平台都在下滑"。
- 来源：
  - https://en.wikipedia.org/wiki/Help_a_Reporter_Out — ✅
  - https://www.prnewsonline.com/pr-roundup-connectively-done-x-exodus-ai-pros-and-cons/ — 2024-11 — ✅
  - https://buzzstream.com/blog/haro-is-back-podcast/ — ✅

### C-61 | 全体 | S3 | 竞品事实 + 需求信号（反向：信源污染）
**Qwoted**：每天约 15 起违规（假人设、AI 内容），每天拦截约 50 个客户注册，已封禁"数百"个机构或"专家"，用 Pangram 做 AI 检测。Press Gazette 的"Reality Wars"系列揭露的假专家已渗透英美媒体。对记者是否免费、对信源的价格没能在官网核实（第三方称 149 美元/月，**[未核实]**）。
- 意义：**S3 的真问题已从"找不到信源"转向"信源真假难辨"**。记者被迫逐个打电话核实。
- 来源：
  - Journalist response platform plays whack-a-mole… — https://pressgazette.co.uk/news/journalist-response-platform-plays-whack-a-mole-against-ai-deluge-of-pr-content/ — Press Gazette 2026-07-27 — ✅
  - qwoted.com — ✅（无统计数字）

### C-62 | 全体 | S3 | 竞品事实
**Source of Sources（SOS，原 HERO）**：Shankman 2024 年另起的炉灶，"永远免费"。2024-05-08 与 Muck Rack 合作：Muck Rack 认证记者的请求置顶，SOS 请求也会被 Muck Rack 索引。
- 来源：PR News 同上 ✅；Muck Rack 博客 2024-05-08（只看到搜索摘要 ⚠️）

### C-63 | 全体 | S3 | 竞品事实 + 市场数据
**Muck Rack**：PR 侧付费、记者侧免费的双边平台。Sacra 估算 2026-04 ARR 约 1.08 亿美元（同比约 +25%），近 6,000 家客户（2024 年底）；入门价约每年 5,000 美元，Premier 每年 5 万美元以上。2022 年获 1.8 亿美元 A 轮。记者端：免费个人主页、监测、提醒；认证记者可免费使用媒体数据库；可以设置投稿偏好，但不能完全屏蔽投稿。
- 意义：S3 里**最赚钱的是"记者数据库卖给 PR"**，记者只是免费的供给方。
- 来源：
  - https://sacra.com/c/muck-rack/ — ✅（第三方估算）
  - https://muckrack.com/journalists — ✅
  - https://en.wikipedia.org/wiki/Muck_Rack — ✅

### C-64 | 全体 | S3 | 市场数据
**Cision**：2020 年被 Platinum Equity 以约 27 亿美元收购。2025 年与债权人谈判破裂（Bloomberg 2025-01），之后获 2.5 亿美元纾困（维基口径）。CisionOne 价格不公开。**[只看到搜索摘要，原文未打开 ⚠️]**
- 意义：HARO 被关、债务压力和聚焦 CisionOne 是同一条因果链——为记者服务的免费产品是 PR 巨头最先砍掉的成本。

### C-65 | 全体 | S3 | 竞品事实
**ProfNet（PR Newswire/Cision）**：1992 年起运营，对媒体免费。**SourceBottle**：对记者免费，偏澳洲。**Featured.com**：见 C-60。
- 来源：https://www.sourcebottle.com/ — ✅；ProfNet 只看到搜索摘要 ⚠️

### C-66 | LOCAL | S3 | 空白
**本地信源（街坊、小商户、学生、基层公务员）没有任何专门工具**。Chalkbeat 的做法是从 LocalLens 的会议转录里找发言的学生和家长当信源（C-02），这是本次唯一找到的"会议数据 → 本地信源"的使用证据。

---

## 5. 相邻品：AI 自动生成本地新闻（与 INDIE/LOCAL 争读者）

### C-70 | INDIE, LOCAL | S6/S7（相邻）| 竞品事实
**Patch AI newsletter（PatchAM）**：2025-03 起从约 1,100 个社区扩到号称 3 万个。CJR（2026-03）口径：约 1.4 万个社区已上线，订阅接近 100 万。内容抓取本地新闻网站、社交群组和镇政府网站，常出现"wrong Springfield"（抓错同名城市）。Patch 自身有 85 名全职编辑。2021–2023 年的人工策展版因"经济上不成立"于 2023-11-10 关停（策展人每期报酬 15–25 美元，高峰时 85 份日报）。
- 来源：
  - https://niemanlab.org/2025/04/the-origins-of-patchs-big-ai-newsletter-experiment — Nieman 2025-04 — ✅
  - https://www.cjr.org/feature/hyperlocal-ai-patch-newsletter-million-subscribers.php — CJR 2026-03-05 — ✅

### C-71 | INDIE | 相邻 | 竞品事实（被收购）
**Good Daily**：一人公司，355 个 AI 本地 newsletter，靠聚合、没有原创报道。Nieman 曝光后有广告主撤出。2025-07-21 被 6AM City 收购，唯一员工转任 6AM 的工程副总裁。
- 来源：https://www.niemanlab.org/reading/6am-city-acquires-ai-powered-local-newsletter-startup-good-daily/ — ✅

### C-72 | INDIE | 相邻 | 竞品事实（声誉事故）
**Hoodline（Impress3）**：AI 虚构署名人设（每个城市站 3–6 个），出现事实错误和"幻觉"，没有报头，内容大量依赖警方逮捕通报和新闻稿。
- 来源：https://niemanlab.org/2024/06/whats-in-a-byline-for-hoodlines-ai-generated-local-news-everything-and-nothing — Nieman 2024-06-03 — ✅

---

## 6. 已死 / 转型复盘

| 项目 | 结局 | 时间 | 原因（有据） | 对我方的教训 | 来源 |
|---|---|---|---|---|---|
| **CrowdTangle**（Meta） | 关停，替代品 Meta Content Library 只对学术和非营利开放，"大多数记者"被排除 | 2024-08-14 | Meta 称其"degrading tool"（日益失效的工具），只测"a narrow cake slice of a cake slice"（蛋糕里的一小片）；研究者称替代品只有"1% of the features"（1% 的功能） | **依赖单一平台数据的 S1 工具随时会被平台掐断** | https://techcrunch.com/2024/08/15/meta-shut-down-crowdtangle-a-tool-for-tracking-disinformation-heres-how-its-replacement-compares ✅ |
| **Twitter/X 免费 API** | 2023-02 起取消免费读取；Basic 每月 100 美元只能读 1 万条，企业版每月 4.2 万–21 万美元；联盟信称至少 76 个长期项目会因此终止 | 2023 | 平台变现 | 同上；Dataminr 新闻版的核心依赖受冲击 | https://www.niemanlab.org/2023/04/among-all-of-his-mistakes-dont-forget-elon-musk-is-singlehandedly-crushing-a-big-chunk-of-internet-research-for-no-good-reason/ ✅ |
| **HARO→Connectively** | Cision 关停后卖给 Featured | 2024-12 / 2025-04 | 母公司聚焦 CisionOne，加上债务压力；收费改版和改名赶走用户（PR 评论口径） | 免费给记者的产品，如果没有独立收入来源，就会在母公司困难时最先被砍 | 见 C-60 ✅ |
| **Patch 人工策展 newsletter** | 关停，被 AI 版取代 | 2023-11 | 经济上不成立：地产广告下滑，策展人卖不动广告 | 人工"盯本地"在单位经济上不成立，是 AI 化的直接动因 | Nieman 2025-04 ✅ |
| **Chalkbeat 自建会议工具** | 搁置，改用 LocalLens | 2024–2025 | 改提示词需要工程师，忙碌的员工把它看成"又一件任务" | 新闻机构自建工具难以维护，愿意买现成的 | Nieman 2025-03 ✅ |
| **Open States** | 开源数据并入 Plural，大部分工具停用；Plural 再被 SAI360 收购 | 2021 / 2025-12 | 开放数据难以独立营利 | 公共数据层终会被合规/游说软件吸收，记者侧没人买单 | open.pluralpolicy.com ✅ |
| **Council Data Project / Councilmatic / Agenda Watch** | 部分实例停更或进度不明 | 2023–2025 | 资助制开源项目缺少维护者（CDP 官方明确写了） | 会议抓取的长期维护成本（每城一个 scraper）是核心壁垒，也是坑 | GitHub ✅ / RJI ✅ |
| **NewsWhip** | 被 Sprout Social 收购，转向品牌监听 | 2025-07 | 新闻机构付费能力弱，品牌/PR 市场更大（推断） | 新闻发现工具常见的结局是被 PR/营销软件吞并 | pulse2 ✅ |
| **Good Daily** | 被 6AM City 收编 | 2025-07 | 曝光后广告主流失（Nieman 口径） | 纯 AI 聚合缺乏信任背书 | Nieman ✅ |
| **Civic Sunlight**（存活但未定型） | 截至 2024-12 唯一付费客户是 1 家报纸 | 2024–2025 | 错误率加上商业模式未定 | "给记者当线索 wire"是唯一跑通的付费点 | Concord Monitor ✅ |
| **Storyful**（收缩） | 亏损扩大、裁员 | 未核实日期 | — | — | ⚠️ |

---

## 7. 空白地图（基于以上竞品事实的推断，不是需求证据）

| 环节 × 场景 | 现有覆盖 | 空白 |
|---|---|---|
| S1 地方会议 | Hamlet（3,000+ 机构，每周刷新，商业客户优先）、LocalLens（APM，限定机构）、Civic Sunlight（新英格兰）、citymeetings（单城）、Documenters（24 个社区，人力）、Digital Democracy（州议会） | **无"全国县市 + 日更 + 面向记者付费 + 议题 timeline"产品**；Hamlet 最接近，但刷新频率和客户重心都不在记者 |
| S1 警情/scanner | Dataminr（贵，偏社交信号）、Citizen/CrimeRadar（消费端，误报频发）、PSST（免费，2026 年秋才上线，只做提示音触发）、Broadcastify/OpenMHz（原始音频） | **面向记者的"scanner 转录 + 新闻交叉验证 + 事件 timeline"没有成熟产品**；PSST 是最直接的免费对手；加密是覆盖率的硬天花板 |
| S1 法院新案 | CourtListener（联邦免费）、Trellis/Clio Docket（律所付费）、Courthouse News（未核实） | **州/县初审法院"新案提醒"对地方记者没有可负担的方案** |
| S2 背景研究 | 通用 LLM、Pinpoint、DocumentCloud、OpenCorporates（记者免费） | 通用研究被大模型吃掉；剩下的是**本地结构化数据**（县法院、地方会议历史、警情历史） |
| S3 信源 | Muck Rack、Qwoted、HARO/Featured、SOS、ProfNet（全偏"专家评论"，PR 付费） | **本地/草根信源（会上发言的居民、当事人）没有工具**；**专家真伪核验**成为新痛点 |
| TV 派题台 | Dataminr + scanner + 社交 | 证据不足（本轮未能检索）|

---

## 8. 最反常识 / 最重要的 5 条发现

1. **"scanner → AI 摘要 → 推送"已经有人大规模做了，但做砸了口碑**（C-24）：CrimeRadar Android 安装量 100 万+，却因"fire alarm→firearm"等误报被多地警方公开点名。它的包名是 `com.newsbreak.crimeradar`，需内部确认与我方的关系。对记者产品来说，**准确率和原音频可追溯本身就是卖点**。
2. **最直接的免费对手 PSST 刚刚冒头**（C-23）：Lenfest 资助，Big Local News 托管，对新闻机构免费，2026 年秋上线。如果我方 scanner 能力想向地方新闻机构收费，就必须在"事件 timeline 化 + 新闻交叉验证 + 多城覆盖"上明显超过一个免费的提示音触发器。
3. **会议 AI 赛道的赢家不靠记者赚钱**（C-01、C-06、C-13）：Hamlet 收入来自房地产和数据中心开发商，对记者免费；WallFly、Quorum（中位数每年 2.35 万美元）和 Plural 卖给游说团队。记者在这里**更像免费的口碑渠道，而不是付费主体**。这对我方的商业模式是警示。
4. **S3 的痛点已经从"找不到专家"变成"专家是假的"**（C-61、C-60）：Qwoted 每天处理约 15 起违规、拦截约 50 个注册；HARO 新东家把 AI 检测和 LinkedIn 必填作为核心卖点。同时，本地草根信源完全没有工具，唯一证据是 Chalkbeat 从会议转录里找信源。
5. **为记者做的免费工具会周期性死亡**（第 6 节）：CrowdTangle、X API、HARO、Open States、CDP/Councilmatic/Agenda Watch 的死因都是"平台掐数据"或"母公司/资助方不再买单"。能活下来的是 Dataminr 和 Muck Rack 这类**由安全或 PR 客户补贴记者端**的模式。

## 9. 证据薄弱、需要补的地方

- **电视台派题台（TV）工具**：TVEyes、ENPS 插件、Dataminr 在电视台的实际渗透率，本轮没有检索到（搜索配额用尽）。这是整个地图最大的缺口。
- **AP Local News AI 项目**（AP 与 Knight 资助、为 5 家地方新闻机构做的自动化工具，含会议转录和警情简报）没有检索到，**必须补**。
- **Courthouse News Service**（法院新案每日报道，律所订阅）、**UniCourt**、**Factiva/Nexis** 的定价和覆盖都没有核实。
- **Hearst Assembly**（集团自建的会议监测工具）原文 403；其他集团（Gannett、Lee）是否自建也没查。
- Broadcastify 的 feed 数和价格、OpenMHz 的系统数、CivicSearch 的 547 城，都只来自搜索摘要或第三方。
- Dataminr 新闻版的真实价格和地方电视台的使用体验：缺少记者原话，现在只有一条二手整理。
- 竞品口碑：G2/Capterra 页面大多 403，Meltwater 和 Quorum 的评分只来自搜索摘要，没有写进结论。

---

## 10. 总表（竞品 × 环节 × 群体 × 覆盖 × 定价 × 状态）

| # | 竞品 | 环节 | 主要群体 | 覆盖（口径/年份） | 定价 | 所有者/融资 | 状态 |
|---|---|---|---|---|---|---|---|
| 1 | Hamlet | S1/S2 | LOCAL, INDIE（实际付费方：地产/数据中心） | 3,000+ 机构，每周刷新（2026-02） | 免费层 + 14 天试用；企业报价；记者免费 | VC 约 1,000 万美元 | 活跃，扩张中 |
| 2 | LocalLens | S1 | LOCAL | Chalkbeat 用约 80 学区/30 州（2025-03） | 未公开，限定机构 | APM 2025-11 收购 | beta |
| 3 | Civic Sunlight | S1 | LOCAL, INDIE | 约 20–30 个新英格兰市镇（2024–25） | 读者免费；wire 模式未定 | 初创 | 存活，规模小 |
| 4 | citymeetings.nyc | S1 | LOCAL | 纽约市议会 + 宪章委员会 | 免费 | 个人 | 活跃 |
| 5 | SeeGov | S1 | LOCAL, INDIE | 按需添加有视频的机构 | 现免费，计划付费 | 非营利 | 活跃 |
| 6 | WallFly | S1 | （游说方） | 国会到地方，按需添加 | 报价，无长期合同 | 未知 | 活跃 |
| 7 | City Bureau Documenters | S1 | LOCAL, INDIE | 24 社区/16 州，4,000+ 人（2025-06） | 资助制 | 非营利，1,000 万美元奖金 | 活跃 |
| 8 | CivicSearch | S1 | LOCAL | 547 城（未核实） | 未知 | 未知 | 不明 |
| 9 | Council Data Project | S1 | LOCAL | 18 + 3 个实例，部分停更 | 免费开源 | 志愿者 | 半停滞 |
| 10 | Councilmatic | S1 | LOCAL | NYC/Chicago/Philly/LA Metro（旧） | 开源 | DataMade/PPF | 不明 |
| 11 | Agenda Watch | S1 | LOCAL | 未公开（2023 上线） | 免费 | BLN × RJI | 停滞迹象 |
| 12 | Digital Democracy | S1/S2 | LOCAL, NATL | 加州 + 夏威夷州议会 | 注册记者使用（价格未说明） | CalMatters；每年 180 万美元 × 5 年资助 | 活跃，扩张中 |
| 13 | Plural（含 Open States） | S1/S2 | NATL（游说方） | 国会 + 50 州 + DC + PR | 609 美元/年 → 5,000 美元/年 → 定制 | SAI360 2025-12 收购 | 活跃，开放层停用 |
| 14 | BillTrack50 | S1/S2 | NATL, LOCAL | 州 + 联邦 | 检索免费，提醒付费 | 未知 | 活跃 |
| 15 | Quorum | S1/S2 | （游说方） | 州 + 联邦 | 中位数约 2.35 万美元/年（Vendr） | 私营 | 活跃 |
| 16 | FiscalNote/CQ | S1/S2 | NATL | 联邦 + 州 | 报价 | 上市；ARR 8,410 万美元 | 收缩，评估战略选项 |
| 17 | Granicus/Legistar | 供给方 | — | 7,000+ 公共客户（未核实） | B2G | 私募 | 活跃 |
| 18 | Dataminr for News | S1 | TV, NATL, LOCAL | 自称 1,500+ 新闻机构；100 万+ 数据源 | 报价（报道称每年数万美元） | 2025 年融资 4.85 亿美元；收购 ThreatConnect | 活跃，重心转安全 |
| 19 | Samdesk | S1 | （企业安全） | 全球 | 报价 | 2023 年 A 轮 1,350 万美元 | 活跃，无媒体客户 |
| 20 | PSST | S1 | LOCAL, INDIE | 计划 ≥10 家新闻机构试点 | 对新闻机构免费 | Lenfest/RJI/BLN/Verso | 2026 年秋上线 |
| 21 | Broadcastify | S1（凑合） | TV, LOCAL | 约 7,000+ feeds（未核实） | 直播免费，Premium 存档 365 天（价格未核实） | RadioReference | 活跃，受加密侵蚀 |
| 22 | OpenMHz | S1（凑合） | TV, LOCAL | 225+ 系统，存档 30 天（未核实） | 免费 | 志愿者/开源 | 活跃 |
| 23 | CrimeRadar | S1（消费端） | — | 未公开；Android 100 万+ 安装 | 9.99 美元/月，79.99 美元/年 | Scoopz LLC（包名 com.newsbreak.*，关系未核实） | 活跃，误报争议 |
| 24 | Citizen | S1（消费端） | — | 60+ 城 | Protect 订阅 | 融资约 1.13 亿美元 | 活跃 |
| 25 | PulsePoint | S1 | LOCAL, TV | 4,950+ 社区（2024-01） | 免费 | 基金会 | 活跃，信息遮蔽 |
| 26 | NewsWhip | S1 | NATL | — | 报价 | Sprout Social 2025-07 收购（5,500 万–6,500 万美元） | 被收购，转向品牌 |
| 27 | Storyful | S1/S5 | NATL | — | 报价 | News Corp | 收缩（未核实） |
| 28 | Meltwater/Talkwalker | S1 | NATL（PR 方） | 全球 | 约 2.5 万美元/年中位（未核实） | 私营 | 活跃 |
| 29 | CrowdTangle | S1 | NATL, LOCAL | — | 曾免费 | Meta | **2024-08 关停** |
| 30 | Google Alerts | S1（凑合） | 全体 | 全网 | 免费 | Google | 活跃，口碑差（旧证据） |
| 31 | CourtListener/RECAP | S1/S2 | NATL, LOCAL | 1,000 万+ 判决；几乎所有联邦案 | 免费 | Free Law Project | 活跃 |
| 32 | PACER | S2 | NATL, LOCAL | 联邦 | 每页 0.10 美元，单份封顶 3 美元，季度 ≤30 美元免 | 联邦法院 | 活跃 |
| 33 | Trellis | S1/S2 | （律师） | 45 州/3,335 法院/2,481 县（口径不一） | 约 99 美元/月起（未核实）；API 报价 | 融资约 3,500 万美元 | 活跃 |
| 34 | Clio Docket（原 Docket Alarm） | S2 | （律师） | 10 亿+ 份文书 | 未公开 | Clio（2025 年 10 亿美元收购 vLex） | 被并购整合 |
| 35 | UniCourt | S2 | （律师） | 未核实 | 未核实 | — | — |
| 36 | MuckRock/DocumentCloud | S2 | NATL, INDIE, FREE | — | 组织版每月 50 个请求；价格未核实 | 非营利 | 活跃 |
| 37 | Google Pinpoint | S2 | NATL, LOCAL | — | 免费（申请制） | Google | 活跃 |
| 38 | OpenCorporates | S2 | NATL | 全球 | 2,250–12,000 英镑/年；记者免费 | 公益公司 | 活跃 |
| 39 | Accurint/TLOxp | S2 | NATL | — | 未核实 | LexisNexis/TransUnion | 活跃 |
| 40 | Factiva/Nexis | S2 | NATL | — | 未核实 | Dow Jones/RELX | 待补 |
| 41 | NotebookLM/通用 LLM 深度研究 | S2/S3 | 全体 | — | 免费到约 20 美元/月级 | Google/OpenAI/Anthropic | 快速渗透 |
| 42 | HARO（Featured） | S3 | 全体 | 历史 80 万信源/5.5 万记者 | 记者免费 | Featured.com（2025-04 收购） | 复活 |
| 43 | Connectively | S3 | 全体 | — | 曾有付费层 | Cision | **2024-12 关停** |
| 44 | Qwoted | S3 | 全体 | 未公开 | 记者免费（未核实）；信源约 149 美元/月（未核实） | 私营 | 活跃，治理 AI 假专家 |
| 45 | Source of Sources | S3 | 全体 | — | 永久免费 | Shankman；与 Muck Rack 合作 | 活跃 |
| 46 | Muck Rack | S3（PR 侧付费） | 全体 | 600,000+ 媒体源监测 | PR 5,000 美元至 5 万美元以上/年；记者免费 | A 轮 1.8 亿美元；ARR 约 1.08 亿美元（Sacra） | 活跃，盈利型 |
| 47 | Cision | S3（PR 侧） | 全体 | — | 报价 | Platinum Equity；债务压力 | 承压（未核实细节） |
| 48 | ProfNet | S3 | 全体 | — | 记者免费 | Cision | 活跃（未核实） |
| 49 | SourceBottle | S3 | 全体（偏澳洲） | — | 记者免费 | 私营 | 活跃 |
| 50 | Patch AI newsletter | 相邻（S6/S7） | INDIE 的读者竞争 | 约 1.4 万上线/目标 3 万社区；订阅近 100 万 | 读者免费 | Patch | 活跃 |
| 51 | Good Daily | 相邻 | INDIE 的读者竞争 | 355 个 newsletter | 免费 | 6AM City 2025-07 收购 | 被收编 |
| 52 | Hoodline | 相邻 | INDIE 的读者竞争 | 多城 | 免费 | Impress3 | 活跃，声誉受损 |
