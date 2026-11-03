# 记者工具市场格局：谁在做、解决了什么、哪里还空着

> 日期：2026-11-03 · 面向：记者平台产品与决策层 · 姓名与术语见 [CONTEXT.md](CONTEXT.md)
> 姊妹篇：[记者需求调研](journalist_needs_report.md)。本报告沿用同一套九个工作环节（S1–S9），并**按记者整条工作流铺开，不以任何单一产品方向为中心**。
> 底稿：[05 线索/研究/信源竞品](data/05_competitors_discovery_research.md)、[06 生产/分发/变现竞品](data/06_competitors_production_revenue.md)、[07 补缺](data/07_gap_fill.md)，加上各条线专题文件（[11](data/11_beat_politics_education.md)–[16](data/16_stage_career_freelance.md)）里的工具表，共覆盖约 130 个产品和项目。正文每条事实都附可打开的原始链接。

---

## 执行摘要

**记者工具市场的规律比任何单个赛道都重要：谁向记者个人收费，谁就活不好；哪个环节平台或基金会撤资，哪个环节就塌。** 活得最好的是"记者免费、另一边付钱"的双边模式（Muck Rack 靠 PR、Hamlet 靠地产开发商、Dataminr 靠安全和政府客户）。给记者做的免费工具会周期性死掉（CrowdTangle、HARO、Open States）。所以产品方向的关键不是"做哪个功能"，而是"谁买单、数据源稳不稳"。

从记者整条工作流看，工具的疏密很不均：**生产、分发、转写、信源（专家）这些环节已经拥挤；而"下沉到地方的结构化记录"几乎是空白——地方选举结果、竞选财务、地方法院新案、许可、LLC 业主，都没有面向记者、负担得起的产品。** 我们现有的两项能力（会议、警情）落在一个"有人做、但有明显缺口"的中间地带：单场会议摘要已是红海（APM 收购了 LocalLens、Hearst 自建、Hamlet 覆盖 3000+ 机构），警情则有一个免费对手 PSST 2026 年秋上线，且数据源在被加密侵蚀。

最重要的六条发现：

1. **会议 AI 赛道的赢家不靠记者赚钱。** Hamlet 的收入来自房地产和数据中心开发商，对记者免费（[Nieman Lab 2026-01](https://www.niemanlab.org/2026/01/highlighting-the-funniest-moments-this-startup-aims-to-bring-public-meetings-into-the-tiktok-era/)）；同类的 Quorum、Plural、WallFly 卖给游说团队（Quorum 采购价中位数约 2.35 万美元/年，[Vendr](https://www.vendr.com/marketplace/quorum-inc)）。
2. **活得最好的是"记者免费、另一边付钱"的双边模式。** Muck Rack 明确写着 "journalists never pay to use Muck Rack"（记者使用 Muck Rack 从不付费）（[Muck Rack 定价页](https://muckrack.com/pricing)，该页有 Cloudflare 验证，需用浏览器打开；另见 [Wikipedia](https://en.wikipedia.org/wiki/Muck_Rack)），靠向 PR 卖记者数据库，估算 ARR 约 1.08 亿美元（[Sacra](https://sacra.com/c/muck-rack/)）。Dataminr 的重心已转向安全和政府市场，2025 年以 2.9 亿美元收购网络威胁情报公司（[SecurityWeek](https://www.securityweek.com/dataminr-to-acquire-threatconnect-for-290-million/)）。
3. **免费给记者的工具会周期性死掉。** CrowdTangle（2024 年关停）、X 免费 API（2023）、HARO / Connectively（2024 年关停后被转卖）、Open States（并入 Plural，再被 SAI360 收购），死因都是平台掐断数据，或者母公司、资助方不再买单。
4. **面向读者的全自动本地内容一再翻车，内部辅助工具反而活得好。** LedeAI 为 Gannett 写的高中体育稿被暂停（[CNN via WTOP 2023](https://wtop.com/business-finance/2023/08/gannett-to-pause-ai-experiment-after-botched-high-school-sports-articles/)）；Nota 的 11 个 AI 新闻站因抄袭下线（[Poynter 2026-04](https://www.poynter.org/ethics-trust/2026/nota-news-local-outlets-ai-plagiarism/)）。Hearst 和 AP 的内部工具则持续迭代。
5. **"scanner → AI 摘要 → 推送"已经在消费端大规模做出来，但口碑砸在准确率上，而且误报正在让数据源关门。**
   - 规模：CrimeRadar 在 Android 上下载 100 万以上，iOS 有 4.6 万个评分。
   - 误报：2025-12 到 2026-08，至少 6 个州有公开误报记录，多数涉及学校或枪击。例如把 "fire alarm" 听成 "firearm"，警长称其为 "fake"（[News5 Cleveland](https://www.news5cleveland.com/news/local-news/investigations/crimeradar-app-said-shots-were-fired-at-a-streetsboro-elementary-school-it-wasnt-true)）。
   - 后果：科罗拉多一个消防区因此要改用不公开广播的频道（[GovTech 2026-03](https://www.govtech.com/em/preparedness/ai-sends-false-emergency-alerts-in-boulder-county)）。
   - 与 NewsBreak 的关系：它的安卓包名是 `com.newsbreak.crimeradar`，NewsBreak Ads 帮助中心称它为"战略合作伙伴"并售卖其广告位（[NewsBreak Ads](https://adhelp.newsbreak.com/hc/en-us/articles/45870702577037-CrimeRadar)）。与我方的关系**需内部确认**。
6. **真正的空白集中在"下沉地方的结构化记录"**：①地方（县 / 市 / 学区）选举结果与竞选财务，AP 和 Ballotpedia 都不覆盖（[data/11](data/11_beat_politics_education.md)）；②地方 / 州法院新案提醒，现有产品只卖给律师；③按地域推送的企业 / 裁员 / 申报提醒，原有的 Sqoop 已关（[data/12](data/12_beat_business_tech_realestate.md)）；④跨辖区、按条线订阅的会议议题跟踪；⑤面向电视台派题台的多源警情聚合；⑥高中体育比分数据收集；⑦本地普通人信源。这些共同点是：信息公开但分散、下沉到地方、没有面向记者的好产品。

**对我们的含义（判断，见第 7 节）**：
- 产品内核应是"替人手不足的编辑部，持续盯住一类正在关门、下沉的公共信息，并可追溯"，会议和警情只是其中两个实例。
- 不要和免费工具拼单场"转写 + 摘要 + 提醒"。
- 卖给编辑部、电视台集团和非新闻客户，不卖给记者个人。
- 把"准确、可追溯到原始记录"做成核心卖点。
- 认真考虑双边模式：记者端免费、另一边（地产、政务、律所、安全客户）付钱。

---

## 1. 市场地图：九个环节上都有谁

S1 发现线索按"记者实际从哪类来源找线索"拆，而不是按我们的产品拆——**会议和警情只是"政府记录与申报"和"实时 / 突发"两类下面各自的一个子项**，政治、商业、教育、体育等条线的线索来源同样在表里。

图例：🔴 拥挤（多家成熟产品或免费方案） · 🟡 有人做但有明显缺口 · 🟢 基本空白

| 环节 | 拥挤度 | 主要玩家（括号内为付费方） | 记者那一侧的缺口 |
|---|---|---|---|
| **S1 发现线索：政府记录与申报**（跨政治 / 选举 / 商业 / 教育 / 法院 / 地产，最大的一类） | 🟡 多数子类空 | **会议 / 议程**：Hamlet、LocalLens / APM、Documenters、CalMatters；**法院新案**：CourtListener（联邦免费）、Trellis（律师）；**企业 / 裁员申报**：SEC EDGAR、WARN（Big Local News，会员制）；**竞选财务 / 立法**：OpenSecrets、FEC、Plural / LegiScan；**学区**：AP School Board Search | **下沉到地方的几乎全空白**：地方选举结果、竞选财务、地方法院新案、许可、LLC 业主、学区数据；会议类单场摘要已红海、跨辖区空；联邦数据源 2025–26 还在下线。会议和警情只是这一大类里的两个子项 |
| **S1 发现线索：实时 / 突发**（治安 / 天气 / 交通） | 🟡 | scanner / CAD：Broadcastify / OpenMHz（原始音频）、PSST（免费）、CrimeRadar（消费者）；突发信号：Dataminr（新闻机构）、Citizen、PulsePoint（消防 / EMS） | 加密后的替代信源（CAD 日志、警方社媒、新闻稿）没人聚合；面向派题台的准确、可追溯产品 |
| **S1 发现线索：社交 / 趋势** | 🔴 | Dataminr、NewsWhip（已被 Sprout Social 收购）、Meltwater / Talkwalker（PR 方）、Futuri TopicPulse（广电）、Google Alerts | 小编辑部负担得起的选项 |
| **S1 发现线索：条线数据 / 比分 / 研究** | 🟡 | 体育：MaxPreps / NFHS（PlayOn 系）；科学：EurekAlert、SciLine；健康 / 环境：CDC / EPA 等联邦数据集（2025–26 在下线）；地产许可：Shovels、Permitlify | 高中体育比分 / 检查数据的收集核对无工具；联邦数据源在萎缩，靠民间镜像 |
| **S2 背景研究：法院**（查案卷，区别于上面的"新案提醒"） | 🟡 | CourtListener / RECAP（联邦，免费）、PACER（按页收费）、Trellis、Clio Docket、UniCourt（律所付费） | **州 / 县初审法院的记者方案缺位** |
| **S2 背景研究：公共记录 / 文档** | 🟡 | MuckRock / DocumentCloud（非营利）、Google Pinpoint（免费）、OpenCorporates（记者免费）、通用 LLM | 记录申请的追踪、催办、申诉流程 |
| **S3 找信源** | 🔴（专家）/ 🟢（本地） | Muck Rack、Qwoted、HARO（Featured）、Source of Sources、ProfNet（都由 PR 付费） | 本地普通人信源；专家真伪核验 |
| **S4 采访与素材** | 🔴 | Otter、Rev、Descript、Trint、Happy Scribe、Whisper、Pinpoint | 安全的本地转写（技术门槛高） |
| **S5 核实** | 🟡（资助在撤） | InVID-WeVerify、Bellingcat 工具包（免费）、Reality Defender（付费）、Full Fact AI（授权） | 没有稳定的付费方；补贴在撤 |
| **S6 写作与制作** | 🔴 | Nota、United Robots、Trint、Futuri、Arc XP、各集团自建 | 记者不想交给 AI 写稿 |
| **S7 发布与分发** | 🔴 | Substack、beehiiv、Ghost、Newspack、Letterhead | — |
| **S8 受众与变现** | 🔴 | Chartbeat、Parse.ly、Piano、Poool、Village Media、Google News AI 试点 | 小媒体负担不起 |
| **S9 职业与生存** | 🟡（公益） | RCFP 法律热线、Press Freedom Defense Fund、FPF、JournalismJobs、Contently | 自由撰稿人收款（靠立法与工会） |

---

## 2. 市场覆盖：做到了多大

> 本节只深挖会议、警情、法院三类，**因为它们的竞品数据最全、也是我们现有能力所在，不代表它们是市场的全部**。政治、商业、教育、健康、体育等条线的工具覆盖见各条线专题（[data/11](data/11_beat_politics_education.md)–[16](data/16_stage_career_freelance.md)）。

### 2.1 会议 / 政务：覆盖量与总量差几个数量级

| 产品 | 覆盖（口径 / 时间） | 刷新 | 来源 |
|---|---|---|---|
| Hamlet | 3,000+ 个市议会、规划委员会等 | 每周，日更在计划中 | [PublicCEO 2026-02](https://www.publicceo.com/2026/02/hamlet-launches-nationwide-public-meeting-coverage-over-3000-local-governments-videos-now-discoverable/) |
| LocalLens（Chalkbeat 企业账户） | 约 80 个学区、30 个州 | — | [Nieman Lab 2025-03](https://www.niemanlab.org/2025/03/local-newsrooms-are-using-ai-to-listen-in-on-public-meetings/) |
| Hearst Meeting Monitor | 250+ 场会议（内部） | — | [News Machines 2025-08](https://newsmachines.substack.com/p/hearst-dev-hub-ai-tools-that-work) |
| City Bureau Documenters | 16 个州的 24 个社区；2025 年 3,253 次会议任务 | 人工 | [E&P 2025-06](https://editorandpublisher.com/stories/city-bureau-is-scaling-civic-journalism-one-documenter-at-a-time,256393)；[City Bureau 2026-01](https://citybureau.org/notebook/2026/1/13/documenters-network-2025-wrapped) |
| Civic Sunlight | 约 20 个新英格兰市镇 | — | [CJR 2025-05](https://www.cjr.org/analysis/ai-local-news-civic-sunlight-maine.php) |
| Council Data Project | 18 个城市实例，部分已停更 | — | [GitHub](https://github.com/CouncilDataProject) |
| CalMatters Digital Democracy | 加州 + 夏威夷州议会 | — | [CalMatters 2024-04](https://calmatters.org/inside-the-newsroom/2024/04/calmatters-digital-democracy-fuses-journalism-ai-and-data/) |
| **对照：总量** | Agenda Watch 项目整理出 9 万多个政府机构站点 | — | [RJI 2023-06](https://rjionline.org/news/welcome-to-agenda-watch/) |

最大的玩家 Hamlet 也只覆盖了总量的 3% 左右（3,000 / 90,000+），而且按周刷新；记者需要的是当天就知道。

### 2.2 警情：信源本身在缩

| 产品 | 覆盖 | 说明 | 来源 |
|---|---|---|---|
| Broadcastify | 约 7,000+ 路实时 feed（⚠️ 来自搜索摘要，官网拒绝抓取） | 加密流量任何 app 都解不了 | [PoliceRadio.org 2026-10](https://www.policeradio.org/blogs/news/squawster-broadcastify-scanner-app-2026) |
| PulsePoint | 4,950+ 个社区的调度中心，300 万+ 用户 | 只有消防 / EMS，事件保留 24 小时 | [Wikipedia](https://en.wikipedia.org/wiki/PulsePoint) |
| Citizen | 60+ 个美国城市 | 消费者 app | [Wikipedia](https://en.wikipedia.org/wiki/Citizen_%28app%29) |
| Dataminr for News | 自称 1,500+ 家新闻机构 | 社交信号为主 | [Dataminr](https://resources.dataminr.com/news/dataminr-for-news-datasheet) |
| PSST | 计划至少 10 家新闻机构试点 | 2026 年秋上线 | [RJI 2026-08](https://rjionline.org/news/we-are-building-a-tool-to-help-newsrooms-listen-to-emergency-scanners/) |

**信源变化**：
- Minneapolis、Snohomish（44 个机构）、东湾、Berkeley、Skagit 在 2025–2026 年接连加密警用电台。
- 纽约州的保留公开法案 2025 年被州长否决；2026 年修订版又通过两院，但要求申请者持有诽谤保险（[NY Senate A11199](https://www.nysenate.gov/legislation/bills/2025/A11199)，官网对脚本返回 403，浏览器可正常打开）。
- 科罗拉多的法律实施一年，媒体零签约（[CFOIC 2022](https://coloradofoic.org/a-year-after-the-legislature-passed-a-law-on-police-radio-encryption-denver-area-news-outlets-are-still-blocked-from-listening/)）。

细节见 [02 文件](data/02_tv_breaking_scanner.md)。

### 2.3 法院：联邦免费已经很强，地方是空白

- **联邦**：CourtListener / RECAP 收录 1,000 万+ 份判决和"几乎所有联邦案件"的案卷，免费，用户 100 万+（[Free Law Project](https://free.law/projects/courtlistener)）。
- **州 / 县**：Trellis 宣称覆盖 45 个州、3,335 个法院，但只卖给律师（[Vaquill 汇总 2026-08](https://www.vaquill.ai/blog/trellis-api-state-court-data-what-it-offers)）；Clio Docket 有 10 亿+ 份文书，卖给律所（[LawSites 2026-08](https://www.lawnext.com/2026/08/clio-docket-is-now-in-clio-work-combining-an-ai-workspace-with-access-to-more-than-1-billion-court-filings.html)）。**没有面向地方记者的州法院新案提醒产品。**

---

## 3. 分领域拆解：每个玩家解决了记者什么问题

> 下面按工具类别逐个拆。3.1 和 3.2 先讲会议和警情，是因为它们对应我们的现有能力、竞品也最密；3.3 起是跨条线的记录、信源、生产、分发、职业。各条线（政治 / 商业 / 教育 / 健康 / 体育）自己的工具拆解在 [data/11](data/11_beat_politics_education.md)–[14](data/14_beat_sports_culture_community.md)，不在这里重复。

### 3.1 会议 / 政务（对应能力 1）

| 玩家 | 解决了什么 | 没解决什么 | 商业模式 / 状态 |
|---|---|---|---|
| **Hamlet** | 3,000+ 机构的会议检索、关键词提醒、"数据中心 / 区划 / 住房"情绪指数 | 每周刷新；只在地产开发活跃的城市好用（[AJP 指南 via Nieman Lab 2025-10](https://www.niemanlab.org/2025/10/the-american-journalism-projects-new-field-guide-vets-ai-vendors-for-local-newsrooms/)） | 融资约 1,000 万美元，收入"数十万美元"，客户是开发商；记者免费 |
| **LocalLens（APM）** | 学区和市议会转写、索引、跨辖区检索、提醒 | 说话人识别差，摘要必须人工核实；"It is a tip."（这只是线索）；改提示词要工程师介入 | 2025-11 被 APM 收购，beta，只对公共媒体和"合格编辑部"开放 |
| **Hearst Meeting Monitor / Assembly** | 集团内部会议监测 | 不对外卖 | 自建 |
| **CalMatters Digital Democracy** | 州议会层面的 "AI Tip Sheet"：扫描发言、献金、投票，找出异常推送给记者；"doesn't write stories, journalists will"（不写稿，稿子由记者写） | 只有州议会层级 | 基金会每年 180 万美元，资助 5 年；获艾美奖 |
| **Civic Sunlight** | 新英格兰市镇会议 newsletter；Midcoast Villager 称之为 "a force multiplier"（力量倍增器） | 曾把"讨论"报成"已批准"；截至 2024 年底唯一付费客户是一家报纸（[Concord Monitor 2024-12](https://granitegeek.concordmonitor.com/2024/12/31/you-can-get-a-local-news-ish-product-built-entirely-by-a-i-should-i-be-worried/)） | 每场会议成本约 25 美元 |
| **City Bureau Documenters** | 付钱让居民去开会做笔记，补"没人报道的会"（时薪约 20 美元） | 靠人力，覆盖 24 个社区 | 资助驱动，在做 AI 原型 |
| **AP Local News AI（WUOM 会议工具）** | 市议会转写 + 关键词提醒，免费、开源 | 2023 年发布，后续不明 | AP + Knight（[Nieman Lab 2023-10](https://niemanlab.org/2023/10/the-ap-announces-five-ai-tools-to-help-local-newsrooms-with-tasks-like-transcription-and-sorting-pitches)） |
| **Connecticut Public Meeting Monitor** | 监听 YouTube 上的会议，每场标出最多 3 条可能有新闻价值的事项推到 Slack；当年互动最高的两篇报道来自它 | 自建自用 | [LMA 2026-07](https://localmedia.org/2026/07/how-connecticut-public-used-ai-to-uncover-more-local-stories/) |
| **Big Local News / Agenda Watch** | 免费的地方政府文件爬虫和议程检索 | 只对验证机构开放；更新停滞迹象 | 斯坦福，基金会资助 |
| **WallFly / Quorum / Plural** | 立法和会议的转写、提醒 | 价格和功能面向游说团队 | Plural 年费 609–5,000 美元（[Plural](https://pluralpolicy.com/pricing/)） |

**结论**：
- **单场会议的"转写 + 摘要 + 关键词提醒"已经是标配。** 60% 的非营利新闻机构已在用 AI 处理会议（[INN 2026 via Nieman Lab](https://niemanlab.org/2026/06/ai-use-growth-challenges-and-funding-cuts-a-new-report-looks-at-the-state-of-nonprofit-news)）。
- **还没人做好的**：①真正跨辖区（9 万个机构的长尾）；②日更或实时；③按条线订阅；④同一议题跨多次会议追踪；⑤每条结论都链回原始议程页码和录像时间点。
- **反面教训**：Chalkbeat 自建过同类工具，后来放弃改买 LocalLens，因为"改提示词要工程师"，忙碌的员工把它看成"又一件任务"。编辑部宁可买现成的，也不想维护。

### 3.2 突发 / 警情（对应能力 2）

| 玩家 | 解决了什么 | 没解决什么 | 商业模式 / 状态 |
|---|---|---|---|
| **Dataminr for News** | 社交和公开数据的实时提醒；FAZ："the news comes to us"（新闻来找我们）（[Dataminr](https://dataminr.com/resources/real-time-alerts-for-todays-newsroom)） | 贵（报道价每年数万美元，⚠️）；网络活跃度低的社区覆盖不足；提醒量会压垮小团队（[Media Copilot 2026-03](https://mediacopilot.ai/can-you-trust-dataminr-with-your-breaking-news-workflow/)） | 2025 年融资 4.85 亿美元；重心转向安全 |
| **PSST** | scanner 提示音触发 → 初步转写 + 音频链接 → Slack / 邮件 | 只能抓提示音事件；加密频道照样听不到 | **对新闻机构免费**，Lenfest 资助，Big Local News 托管 |
| **Broadcastify / OpenMHz** | 原始音频流和存档 | 没有转写和提醒，记者得一直听 | Broadcastify 2026 年推出自家 app Squawster |
| **Citizen** | 自建接收器 + 员工解读后推送 | 消费者产品；曾悬赏"人肉"一名无辜者，KARE 记者因此认为它不符合新闻标准（[Mother Jones 2021](https://www.motherjones.com/criminal-justice/2021/06/how-long-until-citizen-gets-someone-killed/)） | 融资约 1.13 亿美元 |
| **CrimeRadar** | AI 总结调度音频推送给居民 | 多次误报：Streetsboro 小学 "firearm"、Longmont 不存在的公寓火灾（[Firehouse 2026-03](https://www.firehouse.com/technology/artificial-intelligence/news/55360775/ai-powered-alert-apps-issue-inaccurate-incident-notifications-in-colorado)）；Boulder 警方："I wouldn't rely on them"（我不会依赖它们） | 会员 9.99 美元/月；包名 `com.newsbreak.crimeradar`（[techdevnotes](https://techdevnotes.com/apps/android/crimeradar-dispatch-alerts/com.newsbreak.crimeradar)），**关系待确认** |
| **PulsePoint** | 消防 / EMS 调度事件公开 | 只保留 24 小时；医疗细节被遮蔽 | 基金会 |
| **Your Assignment Desk**（初创） | AI 汇总公开来源、生成选题和播出稿初版 | 2026 年刚成立，零客户 | [Boston Globe 2026-09](https://www.bostonglobe.com/2026/09/05/business/nbc-boston-reporter-eli-rosenberg-ai-startup/) |

**TV 派题台的实际工具栈和采购**（[07 文件 G1](data/07_gap_fill.md)）：
- **工具清单**：scanner、Twitter / TweetDeck、Social News Desk 看板、Dataminr、Reddit、Nextdoor、Facebook 群组、新闻稿、PIO、观众热线（[TVNewsCheck 2022](https://tvnewscheck.com/journalism/article/the-assignment-editor-2-0-more-collaboration-newer-tools/)）。
- **Dataminr 的打法**：
  - 嵌入编辑台系统。2023 年 Wolftech（现属 Avid，与 iNEWS 打通）集成 Dataminr，带"兴趣点地图派附近团队"功能（[Wolftech](https://wolftech.no/wolftech-announces-integration-with-dataminr/)）。
  - 官网的新闻客户证言里没有一家美国地方电视台（[Dataminr for News](https://www.dataminr.com/products/dataminr-for-news/)）。
  - 密苏里大学的上手指南直说："Subscription costs may not be justified for newsrooms under five staff members"（5 人以下编辑部订阅费可能不划算）（[News Media Help Desk 2026-02](https://www.newsmediahelpdesk.org/dataminr-newsroom-getting-started-guide/)）。
  - 价位参照：Dataminr 卖给政府的同族产品 First Alert，圣安东尼奥警局三年合同约 13.49 万美元，约合每年 4.5 万（[San Antonio 采购文件](https://sanantonio.primegov.com/meeting/attachment/181177.pdf?name=Draft%20Ordinance)）。
- **其他玩家**：
  - Futuri TopicPulse 卖的是"趋势热度和竞品对标"，不是一手警情（[Futuri](https://futurimedia.freshdesk.com/support/solutions/articles/44002532428-topicpulse-best-practices-for-tv)）。
  - Rangecast 把多台 scanner 联网远程收听，经销商称 100 多家电视台、电台和报社在用（[Scanner Master](https://www.scannermaster.com/online_police_scanner_monitoring_system_a/349.htm)）。
- **集团的做法**：
  - Gray 自建私有 AI "Ask grAI"，用来总结会议录像、检索公共记录（[NPF 2026-02](https://nationalpress.org/topic/how-gray-medias-ask-grai-tool-supports-better-reporting/)）。
  - 自建还是采购由集团 VP 决定，Hearst 的说法是 "It never makes sense to build everything."（全部自建永远不划算）（[TVNewsCheck 2026-10](https://tvnewscheck.com/ai/article/build-vs-buy-how-tv-station-groups-are-deciding-their-ai-roadmaps/)）。
  - Sinclair 的 The National News Desk 在 90 家台播出，内容来自各地 "content centers"（[Sinclair 2026-09](https://sbgi.net/sinclair-expands-the-national-news-desk-with-additional-programming-and-added-news-hours/)）。潜在买方可能是集团中央台。
- **CrimeRadar 公开误报时间线**：
  - Bend, OR（"Shop with a Cop" → "shot with a cop"，[Central Oregon Daily 2025-12](https://www.centraloregondaily.com/news/local/police-warn-ai-generated-blog-posts-from-scanner-traffic-spread-misinformation/article_f20ed4dc-0ba6-4be0-818e-d89b4ba0ee48.html)）
  - Streetsboro / Twinsburg, OH（[Cleveland 19](https://www.cleveland19.com/2025/12/10/local-police-warn-against-new-crime-app-spreading-dangerously-false-reports/)）
  - Columbia, MO（跨县调度拼出"市中心少年中枪"，[KBIA](https://www.kbia.org/missouri-news-network/2025-12-11/ai-crime-app-spreads-false-report-of-downtown-shooting)）
  - Boulder 县, CO（[GovTech](https://www.govtech.com/em/preparedness/ai-sends-false-emergency-alerts-in-boulder-county)）
  - Mount Vernon, MO 小学（[KY3](https://www.ky3.com/2026/04/13/ai-app-sends-false-shooting-alert-mount-vernon-school-district-parents/)）
  - Orange, MA（[Greenfield Recorder](https://www.recorder.com/2026/08/27/local-police-chiefs-weigh-in-on-pitfalls-benefits-of-ai-scanner-apps/)）
  - University of Akron, OH（[Akron Beacon Journal via Yahoo](https://www.yahoo.com/news/us/articles/crime-app-using-ai-generated-132125713.html)）
  - 它的官网 FAQ 写明公司 "does not independently verify the live dispatch information"（不独立核实实时调度信息）（[CrimeRadar FAQ](https://uscrimeradar.com/faq)）。

**结论**：
- 这个领域的瓶颈不是"转写快不快"，而是**信源在缩**，加上**误报的代价极高**。
- 电视台对实时性的依赖最强：芝加哥五家电视台全部联署反对 30 分钟延迟。它们也已经在为 Dataminr 付钱（Telemundo 的 JD）。
- 没人在做的是：把加密后反而**变多**的替代信源统一聚合成一条可信的事件流——警方延迟日志页、警局社媒和网站新闻稿、仍然明文的消防 / EMS 频道、新闻报道，并且每条都能追溯到原始记录。

### 3.3 法院 / 公共记录（新方向候选）

| 玩家 | 解决了什么 | 没解决什么 |
|---|---|---|
| CourtListener / RECAP | 联邦案件免费检索和提醒，典型一天发出数万条提醒 | 州 / 县法院 |
| PACER | 联邦官方入口 | 收费 |
| Trellis、Clio Docket、UniCourt | 州法院数据、分析 | 卖给律师，没有记者方案 |
| MuckRock | FOIA 代发与追踪；Press Forward 资助 125 万美元做 AI 公共记录工具（[Nieman Lab 2025-07](https://www.niemanlab.org/2025/07/press-forward-grants-22-7-million-to-22-newsroom-projects/)） | 联邦请求平均 276 天、成功率 26.6% 的大环境改不了 |
| Big Local News | Court Scraper、Layoff Watch、Audit Watch 等免费提醒（[Big Local News](https://biglocalnews.org/content/tools/)） | 覆盖零散 |

**许可 / 地产 / 餐厅检查等本地记录**（[07 文件 G3](data/07_gap_fill.md)）：

| 玩家 | 做了什么 | 付费方 / 价格 |
|---|---|---|
| **United Robots DataDesk**（2026 新品） | 监控建筑许可、餐厅检查、法院文书、政府决定，向编辑部推送"值得报"的线索；"Deciding what's a story… stays with you."（判断什么是新闻仍由你负责）（[America's Newspapers 2026-07](https://www.newspapers.org/stories/united-robots,4167029)） | 编辑部，不公开价格。**与"记录类"方向几乎同构** |
| **Hamlet 地产版** | 按辖区监控项目地址、zoning variance 等关键词 | 约 1,000 美元/月起；认证记者免费开放 API（[Hamlet pricing](https://www.myhamlet.com/pricing)、[free data access](https://www.myhamlet.com/free-data-access)） |
| **Shovels** | 2,820+ 个辖区、1.96 亿条建筑许可，每月更新两次 | 0 / 599 / 999 美元/月，客户是建材、能源、地产、保险，没有媒体（[Shovels](https://www.shovels.ai/pricing)） |
| **PermitMint / RatRadar** | 许可（99 城）、餐厅检查（30+ 城）数据 | 对记者免费或开专门入口（[PermitMint](https://permitmint.com/data/)、[RatRadar](https://ratradar.com/b2b/journalists)） |
| **Business Journals** | 每周汇编地产交易、留置权、许可、破产等公共记录给付费会员；同一套能力做成 B2B 线索产品 BizLeads | 商业读者和销售，最低 66 美元/月（2020）（[BIIA](https://www.biia.com/american-city-business-journals-launches-bizleads/)） |

**规律**：本地记录类数据已经形成"商业客户付费、记者免费"的双边模式，记者是被补贴的一方。

**结论**：地方法院新案提醒是四个空白里最"干净"的一个。需求有证据（地方记者"只报新立案和判决"、法院条线被裁），供给只有律师向产品。但工程难度高：各州系统不一，有的只对律师开放网上访问，有的要到现场看终端。

### 3.4 找信源

- **专家信源**：Muck Rack、Qwoted、HARO（Featured）、Source of Sources，全部由 PR 付费。真问题已经从"找不到专家"变成"专家是假的"：Qwoted 每天处理约 15 起违规，已封禁"数百"个机构或"专家"（[Press Gazette 2026-07](https://pressgazette.co.uk/news/journalist-response-platform-plays-whack-a-mole-against-ai-deluge-of-pr-content/)）。
- **本地普通人信源**：**没有任何专门工具。** 唯一找到的做法是 Chalkbeat 从 LocalLens 的会议转录里找发言的学生和家长当信源。会议数据可以顺带补上这一块。

### 3.5 生产工具（S4–S6）：拥挤，且记者不想要"替写"

- **转写**：Otter 免费 300 分钟/月，Pro 8.33–16.99 美元/月，没有记者折扣（[Otter](https://otter.ai/pricing)）；Rev、Descript、Happy Scribe 价格公开；Trint 专做新闻编辑部但不公开价格。
- **一体化编辑部 AI**：
  - Nota 抓取议会会议、许可证、新闻稿，并帮写稿、剪视频、做 SEO；小机构要靠 Microsoft 和 INN 背书的 8 折才进得去（[EIN Presswire 2024-06](https://www.einpresswire.com/article/718799638/nota-announces-grant-program-with-the-institute-for-nonprofit-news-to-put-assistive-ai-in-reach-for-local-journalism)）。
  - United Robots 为 McClatchy、Advance 等自动生成体育和房产稿。
  - Futuri TopicPulse 面向广电。
- **教训**：面向读者的全自动内容反复翻车，包括 LedeAI、Nota News 抄袭、Good Daily 伪造推荐语（[Nieman Lab 2025-07](https://niemanlab.org/2025/07/good-dailys-network-of-more-than-350-ai-generated-local-newsletters-finds-a-buyer)），以及 Patch AI newsletter 常把别的同名城市当本地（"It's the wrong Springfield"）（[CJR 2026-03](https://www.cjr.org/feature/hyperlocal-ai-patch-newsletter-million-subscribers.php)）。

### 3.6 分发与变现（S7–S8）：平台齐全，小媒体用不起

- **newsletter**：Substack 抽成 10%；beehiiv、Ghost 收订阅费、零抽成（[beehiiv](https://www.beehiiv.com/pricing)、[Ghost](https://ghost.org/pricing/)）。
- **CMS**：Newspack 按媒体收入分档，750–2,500 美元/月，并公开写明有 GNI、Knight、Lenfest 资助（[Newspack](https://newspack.com/pricing/)）。
- **受众分析**：Chartbeat、Parse.ly、Poool 都要询价。

### 3.7 职业与生存（S9）：几乎全靠公益

RCFP 免费法律热线（[RCFP](https://www.rcfp.org/legal-hotline/)），并应记者请求把州级律师项目扩大近一倍（[RCFP 2026-03](https://www.rcfp.org/local-legal-initiative-expansion-announcement/)）；FPF 2025 年培训 3,335 名记者做数字安全（[FPF](https://freedom.press/about/announcements/2025-by-the-numbers/)）。这块没有商业产品。

---

## 4. 已死和转型的项目：为什么死

| 项目 | 结局 | 原因 | 对我们的教训 |
|---|---|---|---|
| **CrowdTangle**（Meta） | 2024-08 关停；替代品只对学术和非营利开放，"大多数记者"被排除（[TechCrunch 2024-08](https://techcrunch.com/2024/08/15/meta-shut-down-crowdtangle-a-tool-for-tracking-disinformation-heres-how-its-replacement-compares)） | 平台战略退出 | 依赖单一平台数据的线索工具，随时可能被掐断 |
| **X 免费 API** | 2023 年取消，企业版每月 4.2 万–21 万美元（[Nieman Lab 2023-04](https://www.niemanlab.org/2023/04/among-all-of-his-mistakes-dont-forget-elon-musk-is-singlehandedly-crushing-a-big-chunk-of-internet-research-for-no-good-reason/)） | 平台变现 | 同上 |
| **HARO → Connectively** | Cision 2024-12 关停，2025-04 卖给 Featured（[Wikipedia](https://en.wikipedia.org/wiki/Help_a_Reporter_Out)） | 母公司负债，聚焦核心产品 | 没有独立收入的"给记者的免费产品"最先被砍 |
| **Open States** | 并入 Plural，大部分工具停用；Plural 2025-12 被 SAI360 收购（[open.pluralpolicy.com](https://open.pluralpolicy.com/)） | 开放数据难以独立营利 | 公共数据层最终被合规 / 游说软件吸收 |
| **Council Data Project / Councilmatic / Agenda Watch** | 部分实例停更 | 资助制开源项目缺少维护者 | **每城一个爬虫的长期维护成本，既是壁垒也是坑** |
| **Patch 人工策展 newsletter** | 2023-11 关停，改为 AI 版 | 广告收入覆盖不了每期 15–25 美元的人工成本（[Nieman Lab 2025-04](https://niemanlab.org/2025/04/the-origins-of-patchs-big-ai-newsletter-experiment)） | 靠人工盯本地在经济上不成立 |
| **Chalkbeat 自建会议工具** | 搁置，改买 LocalLens | 维护成本高 | 编辑部愿意买现成的 |
| **NewsWhip** | 2025-07 被 Sprout Social 收购，转向品牌监测（[Pulse 2.0](https://pulse2.com/sprout-social-buying-newswhip-for-up-to-65-million-for-boosting-predictive-intelligence/amp/)） | 新闻机构付费能力弱（推断） | 新闻发现工具的常见结局是被 PR / 营销软件吞并 |
| **LedeAI × Gannett**、**Nota News**、**Good Daily** | 暂停、下线、被收编 | 质量差、抄袭、造假 | 别直接给读者生成报道 |
| **Logically**、**Full Fact**、**TrueMedia** | 破产出售、裁员、关停 | 平台或资助方撤资 | 核实类工具没有稳定的付费方 |
| **Artifact** | 2024 年关停 | "the market opportunity isn't big enough"（市场机会不够大）（[Engadget](https://www.engadget.com/instagrams-founders-are-shutting-down-artifact-their-year-old-news-app-233431390.html)） | 面向消费者的新闻 app 难做大 |

**共性**：
1. 依赖单一平台或资助方的项目，在对方转向时立刻死掉。
2. 全自动生成、直接给读者看的本地内容，反复因质量翻车。
3. 活下来的是两种：**内部辅助工具**（不对外卖），以及**由另一边客户补贴记者端的双边平台**。

---

## 5. 资助方怎么塑造这个市场

| 资助方 | 近两年的动向 | 对工具市场的影响 |
|---|---|---|
| Google | 免费 Pinpoint；资助 Newspack；断了 Full Fact 超过 100 万英镑（[Full Fact 2025-10](https://fullfact.org/technology/google-cuts-funding-to-full-fact/)）；取消搜索里的核查摘要（[Nieman Lab 2025-06](https://www.niemanlab.org/2025/06/google-kills-the-fact-checking-snippet/)）；改为付钱给 400+ 家出版商换"AI 增强内容"（[PPC Land 2026-10](https://ppc.land/google-now-pays-400-publications-to-feed-ai-features-in-google-news/)） | 从补贴工具转向付钱买 AI 内容 |
| Meta | 2022 年停付 News tab；2024 年关 CrowdTangle；2025 年结束美国核查计划（[Nieman Lab 2025-01](https://www.niemanlab.org/2025/01/a-hard-hit-for-the-fact-checking-community-and-journalism-meta-eliminates-fact-checking-in-the-u-s/)） | 核查和社媒监测市场塌陷 |
| OpenAI / Microsoft | Lenfest AI Collaborative 共 2,000 万美元，其中一半是算力额度（[Nieman Lab 2024-10](https://niemanlab.org/2024/10/the-lenfest-institute-launches-10-million-ai-news-program-for-big-city-dailies-with-backing-from-openai-and-microsoft)）；资助 Axios 13 城，换取训练权（[TNW 2026-08](https://thenextweb.com/news/axios-openai-local-news-newsletters-three-year-deal)） | 新的最大资助方，但钱和授权、训练权、算力额度绑在一起 |
| Press Forward | 2025 年 2,270 万美元资助 22 个项目，几乎都是共享基础设施和公益工具（[Nieman Lab 2025-07](https://www.niemanlab.org/2025/07/press-forward-grants-22-7-million-to-22-newsroom-projects/)） | **公益工具和商业工具抢同一批小编辑部** |
| Knight | 资助 AP 的 5 个免费 AI 工具、Village Media 进入美国 | 降低小编辑部的采购意愿 |

**含义**：给小编辑部做工具的商业公司，面对的竞争对手往往是**免费的、基金会资助的公益项目**（PSST、Agenda Watch、Big Local News、Documenters）。要么和它们合作（成为基础设施供应商），要么去服务它们覆盖不到的付费客户。

---

## 6. 谁买单

| 买单方 | 典型产品 | 证据 |
|---|---|---|
| **记者个人**（主要是 FREE、INDIE） | Otter、Rev、Descript 低档；Substack、beehiiv | 都是通用 SaaS，几乎没有记者折扣；自由撰稿人收入低 |
| **编辑部 / 集团** | Trint、Dataminr、Chartbeat、United Robots、Nota、TopicPulse、Newspack | 都要询价或按收入分档；大集团（Hearst、WaPo）倾向自建 |
| **另一边的客户**（双边市场） | Muck Rack（PR 付费）、Hamlet（开发商付费）、NewsGuard（广告主付费）、JournalismJobs（雇主付费） | 见第 3 节 |
| **基金会 / 平台 / AI 公司** | Pinpoint、InVID、PSST、AP 工具、LocalLens（公共媒体）、Lenfest 额度 | 见第 5 节 |

**付费意愿的补充证据**（[07 文件 G2](data/07_gap_fill.md)）：
- **受雇记者**：只有 19% 觉得在工具、培训、编辑指导上没得到支持（[Muck Rack 2025](https://media.muckrack.com/documents/6.9.2025_state_of_journalism.pdf)）。"缺工具"的抱怨不强，痛点必须落到具体环节。
- **独立记者**：39% 自出版零收入，只有约 6% 以自出版为全职收入（[Muck Rack Creator Journalism 2025](https://media.muckrack.com/documents/10.22.2025_v3_The_State_Of__Creator_Journalism_2025.pdf)）。
- **自由撰稿人**：美国新闻类稿费中位数约 0.50 美元/词，自 2019 年基本没涨，近半数低于 0.50（NWU 费率库原始数据 n=659，[The Objective 2026-09](https://www.objectivejournalism.org/p/freelance-journalism-rates-are-worse-than-you-think-theyve-barely-changed-since-2000)；此前 07 文件引用的"约 1 美元/词"是转述的平均数，以原始数据为准）。
- **小编辑部**：Press Forward 给 205 家小编辑部各约 10 万美元无限制资金。从个案看，钱主要花在人、印刷、房租和还债上，几乎不买工具（[Nieman Lab 2026-10](https://www.niemanlab.org/2026/10/press-forward-gave-20-million-to-205-local-newsrooms-over-two-years-heres-how-some-of-them-spent-it/)）。
- **电视台**：采购决策在集团层（VP 级技术或数字主管），参照价位是 Dataminr 政府版每年约 4.5 万美元、一名派题编辑年薪 7.5–8 万美元。

**小编辑部按原价付费的能力很弱**：
- 一体化 AI 厂商也要打 8 折、拉上 Microsoft 和 INN 背书，才能进入年收入低于 25 万美元的编辑部。
- Newspack 最低档 750 美元/月，也要靠基金会补贴。
- INN 会员的收入中位数从 53.2 万美元**降到** 52.5 万美元（[Nieman Lab 2026-06](https://niemanlab.org/2026/06/ai-use-growth-challenges-and-funding-cuts-a-new-report-looks-at-the-state-of-nonprofit-news)）。

---

## 7. 空白排序，以及我们两项能力的位置

### 7.1 按"空白 × 可支撑的付费模式"给机会排序（事实 + 推断）

| 机会 | 市场状态 | 付费模式是否已被验证 | 和我们现有能力的关系 |
|---|---|---|---|
| 下沉地方记录（选举结果 / 竞选财务 / 地方法院 / 许可 / LLC 业主） | 🟢 多数空白，少数（许可 / 地产）刚有人进 | ✅ 律所、地产、政务已为同类数据付费 | 新方向，但和 `crime_radar` 公共记录设计可复用 |
| 跨辖区、按条线盯会议议题 | 🟡 单场摘要已红海，跨辖区 / 议题跟踪空 | ⚠️ 会议数据的商业买家存在（地产） | **能力 1 的升级方向** |
| 多源警情聚合（服务 TV 派题台） | 🟡 有免费对手 PSST、消费端 CrimeRadar | ⚠️ TV 集团已为 Dataminr 付费 | **能力 2 的转型方向** |
| 按地域推送的企业 / 裁员 / 申报提醒 | 🟢 原有的 Sqoop 已关，只剩 BLN 部分覆盖 | ✅ Reuters、LAT 已是 BLN 付费会员 | 新方向 |
| 高中体育比分 / 数据收集 | 🟡 数据被 PlayOn 集中，收集核对无工具 | ✅ 个人站已证明订阅可变现 | 新方向 |

### 7.2 我们两项能力的现状（事实）

| | 能力 1：市政会议议题发现 + timeline | 能力 2：Broadcastify 电台识别安全事件 + 新闻 timeline |
|---|---|---|
| 最直接的对手 | LocalLens / APM、Hamlet、Hearst 自建、Civic Sunlight、AP / Knight 开源工具 | **PSST（免费）**、Dataminr、Citizen / CrimeRadar |
| 对手没做好的 | 跨辖区长尾、日更、按条线订阅、议题跨会议跟踪、引用可追溯 | 加密后的替代信源聚合、准确性与可追溯、面向派题台的工作流 |
| 结构性风险 | 上游 Legistar / Granicus 若内置 AI 摘要，"转写 + 摘要"层会被商品化；每城一个爬虫的维护成本 | **数据源在被加密**；误报的声誉风险（CrimeRadar 前车之鉴） |

### 7.3 方向建议（这是我们的判断，不是证据）

1. **把两项能力重新归位成"地方公共信息监测"这一个大类里的两个实例，而不是两个孤立产品。** 这个大类的共性是需求报告第 5 节证明的"公共信息源在系统性收缩 + 记者人手不足"。会议、警情、地方记录、申报提醒都属于它。

2. **能力 1：别和免费工具拼单场"转写 + 摘要"，拼"覆盖广度 × 准确可追溯 × 议题跟踪"。** 价值主张："你条线上 100 个政府的所有相关议题，当天到你邮箱，每条都能点回原始议程页码和录像时间点。"

3. **能力 2：先做"不依赖电台"的那一半。** 优先聚合 CAD 日志页、警方社媒和网站、明文的消防 / EMS 频道，电台转写只作补充；每条保留原始来源、定位为"线索"。用户定为 TV 派题台。先确认 CrimeRadar 与我方的关系——若同属一体系，它 6 个州的误报记录是直接声誉风险，但它覆盖 1 万多城市的转写管线也可能是现成数据底座。

4. **认真评估"下沉地方记录"作为并列的第三个主攻方向。** 痛度高、供给最空、商业买家现成，可支撑"记者免费、另一边付钱"的双边模式；和仓库 `crime_radar` 设计可复用。

5. **付费方选编辑部、电视台集团和非新闻客户，不卖给记者个人。** 这是全市场最一致的规律。

6. **考虑和公益项目合作而不是硬碰。** PSST、Big Local News、Documenters 都缺长期维护和规模化能力，正是"每城一个爬虫"的商业公司能补的，可成为它们的数据供应商。

---

## 附录：证据缺口

- **"工具费由个人还是雇主出"仍缺直接调查**，第 6 节是间接证据拼出来的。
- **TV 派题编辑的一线原话**很少，只有 2022 年 TVNewsCheck 和 2020 年 CBS Colorado 的转引；"集团中央派题台"没有直接证据。
- **Hamlet 覆盖口径不一**：2026-02 新闻稿称 3,000+ 个机构，官网称 2,400+ 个市县。
- **CrimeRadar**："200 万以上用户"只有二手来源，BBC Verify 原页没打开；与 NewsBreak 的股权或隶属关系没有公开披露。
- 很多厂商不公开价格（Trint、Nota、Dataminr、United Robots、Chartbeat），表里的价格多为报道价或第三方估算，已在底稿中标注。
- 部分覆盖数字只来自搜索摘要或第三方，已在底稿中标 ⚠️：Broadcastify feed 数、CivicSearch 547 城、Granicus 7,000+ 客户。
- 完整竞品总表见 [05 文件第 10 节](data/05_competitors_discovery_research.md) 和 [06 文件附表](data/06_competitors_production_revenue.md)。
