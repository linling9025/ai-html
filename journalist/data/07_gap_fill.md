# 07 缺口补证：TV 编辑台工具栈 · 谁买单 · 商业/地产条线 · CrimeRadar

## 本文件覆盖范围、来源、局限

- **范围**：补 01–06 末尾"缺口"中的 4 项。
  1. TV 编辑台工具栈与集团集中化（G1）
  2. 谁买单与付费意愿（G2）
  3. 商业、地产、开发条线的信息获取（G3）
  4. CrimeRadar 公开报道（G4）
- **来源**：本轮实际访问约 55 个页面，写入 **50 条证据**（✅ 41 / ⚠️ 9）。
  - 搜索一律用 octo_search（DDG）。
  - 核实用 WebFetch、curl_cffi，以及 iTunes lookup API。
- **主要局限**
  1. **Reddit、TVSpy 类论坛一线原话仍然缺失**：reddit.com 对 WebFetch 和 curl_cffi 都返回 403/429。assignment editor 的原话只拿到 TVNewsCheck（2022）和 CBS Colorado（2020）两处转引。
  2. **以下站点被挡，相关结论只用了摘要或二手转述**：bizjournals.com（Cloudflare）、BBC、Semafor（连接超时）、newscaststudio（CF 质询）、Broadcastify Premium 页（405）。
  3. **"谁买单"仍缺直接调查**：没有找到一份美国调查明确问过"工具费由个人还是雇主出"。只能用间接证据拼出来，包括：工具支持满意度、自出版收入、费率、基金会资金去向、政府采购价。
  4. **CrimeRadar**：只陈述公开报道里的事实。它和 NewsBreak 的关系只记录可见事实（包名、广告平台合作页），不作推断。

---

## G1. TV 编辑台：工具栈、集团集中化、AI 线索工具

**G1-01** | TV | S1 | 需求信号（编辑原话 + 使用行为）
- 结论：TVNewsCheck 采访了多家台的派题台，工具清单是 scanner、Twitter/TweetDeck、Social News Desk 看板、Dataminr、Reddit、Nextdoor、Facebook 群组、新闻稿、PIO 和观众热线。科罗拉多的 scanner 已加密。Spectrum News 南加州把 4 名派题编辑分散到东西南北四个片区，是"去中心化"做法。
- 证据：
  - KNTV/KSTS 派题经理 Gonzo Rojas："often we'll see it on Twitter now before we hear it on police scanners"（现在常常先在 Twitter 上看到，再从 scanner 听到）
  - WRAL 派题编辑 Jamila Elder："We would rather wait and get it right, than to report it first and get it wrong."（宁可等一等报对，也不抢先报错）
- 来源：The Assignment Editor 2.0: More Collaboration, Newer Tools — https://tvnewscheck.com/journalism/article/the-assignment-editor-2-0-more-collaboration-newer-tools/ — TVNewsCheck / 2022-03-08（2024 年更新）— ✅（2022 年，偏旧）

**G1-02** | TV | S1 | 竞品事实 + 使用行为
- 结论：Dataminr 已经接进 TV 新闻生产系统。
  - 2023-06，Wolftech（现属 Avid，与 iNEWS 打通）集成 Dataminr，覆盖 News、Production、LIVE 模块。功能包括"兴趣点地图派附近的团队"和"按故事推送告警"。
  - 这说明 Dataminr 在 TV 端走的是"嵌入编辑台系统"的路线。
- 证据：集成功能列有 "point-of-interest map for assigning nearby teams"（用兴趣点地图派附近团队）。没有点名任何美国电视台客户。
- 来源：Wolftech Announces Integration with Dataminr — https://wolftech.no/wolftech-announces-integration-with-dataminr/ — Wolftech / 2023-06-14 — ✅

**G1-03** | TV, NATL | S1 | 市场数据（厂商自述）
- 结论：Dataminr for News 官网自称服务 "more than 1,500 newsrooms and 30,000 journalists"（1,500 多家编辑部、3 万名记者），每天处理 43TB 公开数据，可推送到 Teams 和 Slack。
  - 列出的新闻客户证言来自 Patch、Getty、Reach PLC、DW、RFE/RL，**没有一家美国地方电视台**。
  - 价格不公开，只能约 demo。
- 来源：Dataminr for News — https://www.dataminr.com/products/dataminr-for-news/ — Dataminr / 2026 访问 — ✅（厂商口径）

**G1-04** | TV, LOCAL, INDIE | S1 | 凑合方案 / 采购门槛
- 结论：密苏里大学（RJI 系）的 News Media Help Desk 给编辑部写了 Dataminr 上手指南（2026-02），要点如下：
  - **价格**：按机构规模和覆盖范围定制，不限席位。
  - **上手时间**：初始配置 1–2 小时，完整定制和培训 1–2 周，熟练要 2–4 周。
  - **局限**：信息量会压垮小编辑部；初步报告需要大量核实；历史告警难检索；对有驻地记者、本地信源强的编辑部价值较低。
- 证据：
  - "Subscription costs may not be justified for newsrooms under five staff members"（5 人以下编辑部订阅费可能不划算）
  - "most value when covering unfamiliar markets or providing regional/national coverage"（覆盖陌生市场或区域/全国报道时价值最大）
- 来源：Getting started with Dataminr: A guide for newsrooms — https://www.newsmediahelpdesk.org/dataminr-newsroom-getting-started-guide/ — Curators of the Univ. of Missouri（作者 Z. Waite）/ 2026-02-23 — ✅

**G1-05** | LOCAL（多市场数字媒体）| S1 | 需求信号（使用行为 + 原话）
- 结论：Patch 覆盖 1,900 多个社区，人手很少。全国突发编辑把 Dataminr 当"告警器"，主要订阅 Urgent 级别，按犯罪、火灾、天气、重大社区事件和地理位置过滤。收到告警后有三种处理：派稿、转给当地编辑、或等待确认。Dataminr 有时比社媒和读者爆料早 5 分钟到数小时。
- 证据：Patch 的 Anna Schier 说："Dataminr's job is to raise alarm bells and let me decide what to do with them"（Dataminr 负责拉警报，由我决定怎么处理）。她还说自己 "one ear on the scanner at all times"（一只耳朵始终在听 scanner）。
- 来源：How Dataminr Rewired Patch's Breaking News Workflow With AI — https://mediacopilot.ai/patch-dataminr-breaking-news-ai-alerts/ — Media Copilot（AI 起草、人工编辑；原文 Z. Waite 2026-02-25）/ 2026-03-03 — ⚠️（二手整理）

**G1-06** | TV | S1 | 市场数据（采购价参照，非新闻客户）
- 结论：Dataminr 卖给政府的同族产品 **First Alert** 有公开采购价。圣安东尼奥市议会批准 SAPD 购买 First Alert 许可：1 年合同加 2 次 1 年续约，总额约 **$134,900**，约合每年 4.5 万美元，按"独家供应源"免招标。
  - 这可以作为 Dataminr 产品价位的公开锚点（新闻版价格不公开）。
  - 第三方报道称新闻机构合同为"数万美元/年"，与此量级一致。
- 证据：ordinance 原文写 "estimated total cost of $134,900.00 for the contract period, including renewal options"（含续约期估计总价 134,900 美元）。
- 来源：Draft Ordinance — https://sanantonio.primegov.com/meeting/attachment/181177.pdf?name=Draft%20Ordinance — City of San Antonio / FY2022 — ✅（政府采购，非新闻版；2022 年）

**G1-07** | TV | S1 | 竞品事实（厂商使用说明 = 目标用户画像）
- 结论：Futuri TopicPulse 的 TV 最佳实践文档点名的用户是新闻总监、副总监、**派题编辑**、数字总监和执行制片。用法有三类：
  - 用 "Competitors" SmartPulse 看竞争台在报、而本台漏掉的题。
  - 用 "Excluded" 视图排除自家网站已发的内容。
  - 编辑会前检查选题是否正在升温。
- 意义：它卖的是"趋势热度和竞品对标"，**不是**警情或政务一手线索。
- 证据："Before an editorial meeting, ensure your story pitches resonate with your audience."（编辑会前确认你的选题能引起受众共鸣）
- 来源：TopicPulse Best Practices for TV — https://futurimedia.freshdesk.com/support/solutions/articles/44002532428-topicpulse-best-practices-for-tv — Futuri 帮助中心 / 日期不详 — ✅

**G1-08** | TV | S1 / S6 | 竞品事实（集团自建）
- 结论：Gray Media 自建私有 AI 工具 "Ask grAI"，目的是避免把敏感信源资料交给公共平台。
  - 用途：把播出稿改成数字稿、总结数小时会议录像、检索公共记录。例如调查组在 Potomac 空难后用它分析数千条航空安全投诉、找出可疑点。
  - 资深记者比年轻记者更愿意用。
  - 法务一开始的反应是 "absolutely not. Get it out of here"（绝对不行，拿走）。
- 意义：大集团倾向**自建**通用 AI 层，"会议总结"已被它们内化。
- 来源：How Gray Media's 'Ask grAI' Tool Supports Better Reporting — https://nationalpress.org/topic/how-gray-medias-ask-grai-tool-supports-better-reporting/ — National Press Foundation / 2026-02-09 — ✅

**G1-09** | TV | S1 / 全环节 | 需求信号（采购决策方式，原话）
- 结论：TVNewsCheck 的 NAB NY 面板（2026-10）谈各集团"自建还是采购"AI：
  - **Scripps**：默认采购，但 Newsdesk 平台是几年前自建的，覆盖"从 pitch 到派题到稿件审核"。
  - **Fox 台**：倾向尽量自建。
  - **Hearst**：先分析市场再决定。
  - **Circle City**：强调"绝不失去控制"。
  - 拍板方多是集团层的 VP 数字、VP 新闻运营与技术、VP 新兴技术，不是单台新闻总监。
- 证据：
  - Hearst 的 Michael Rosellini："It never makes sense to build everything."（全部自建永远不划算）
  - Fox 的 Erik Smith："The hard part is supporting, advancing, and growing it"（难的是后续支持、迭代和扩展）
- 来源：Build Vs. Buy: How TV Station Groups Are Deciding Their AI Roadmaps — https://tvnewscheck.com/ai/article/build-vs-buy-how-tv-station-groups-are-deciding-their-ai-roadmaps/ — TVNewsCheck / 2026-10-26 — ✅

**G1-10** | TV | S1 | 需求信号（行业路线图里的空白）
- 结论：LMA 在 GNI 支持下召集 10 家地方广电集团（Nexstar、Sinclair、WRAL、Cowles/KHQ、Draper 等）制定 AI 路线图（2026-10）。重点是：
  - 以 story 为单位的多平台改版
  - 工作流 agent
  - 销售辅助
  - FAST 和社媒的自动剪辑
  - 档案向量化（"gold in the basement"，地下室里的金子）
  - **页面没有涉及采集、派题台或监控**。
- 意义：集团的 AI 预算方向是"生产和变现"，线索发现不在路线图里。这既是空白，也说明集团层面短期内不会主动为线索发现找预算。
- 来源：LMA publishes new report: The AI Roadmap for Local Broadcasters — https://localmedia.org/2026/10/lma-publishes-new-report-the-ai-roadmap-for-local-broadcasters/ — Local Media Association / 2026-10-06 — ✅（只看了发布页，没看报告全文）

**G1-11** | TV | S6 / S9 | 竞品事实（集团集中化）
- 结论：集团集中化正从"技术中心"扩到"新闻生产"。
  - TVNewsCheck 2025-10 的网络研讨会报道称，hubbing 已是主控（master control）的成熟模式，正扩展到新闻生产。Scripps、Sinclair 参与讨论。
  - **派题台是否也被集中化，报道里没有提到。**
- 证据："is expanding to broader functions including news production"（正扩展到包括新闻生产在内的更多职能）
- 来源：Content Hubs For The TV Station Group — https://tvnewscheck.com/tech/article/content-hubs-for-the-tv-station-group/ — TVNewsCheck / 2025-10-13 — ✅

**G1-12** | TV | S1 / S6 | 竞品事实（集团工作流标准化）
- 结论：Sinclair 把旗下 60 多家台称为 "content centers"，正在推进 storycentric 工作流和上云（CMS 和播出已上 AWS）。最大难点是让所有台"按同一套规则"工作。
  - Cuez 的 CRO 说，现在来看展台演示的不只是技术负责人，**新闻总监、制片和记者**也越来越多。
- 证据：Sinclair 的 Ernie Ensign："everybody's got to play by the same rules"（所有人都得按同一套规则来）
- 来源：Are Storycentric Workflows Finally Having Their Moment? — https://tvnewscheck.com/tech/article/are-storycentric-workflows-finally-having-their-moment/ — TVNewsCheck / 2026-08-20 — ✅

**G1-13** | TV | S6 / S7 | 竞品事实（集中化的新闻产品）
- 结论：Sinclair 的 The National News Desk 在 90 家台播出，2026-09 新增 12 个市场的 5 点档和 21 个市场的日间半小时档。内容来自各地 "content centers" 的资源。
- 意义：集团通过中央台把地方采集"上收复用"。对线索工具来说，潜在买方可能是**集团中央台**，而不只是单台。
- 证据：Scott Livingston："leveraging the strength of our content centers and journalists across the country"（借助全国各地内容中心和记者的力量）
- 来源：Sinclair Expands The National News Desk… — https://sbgi.net/sinclair-expands-the-national-news-desk-with-additional-programming-and-added-news-hours/ — Sinclair / 2026-09 — ✅（公司新闻稿）

**G1-14** | TV | S9 | 市场数据（合并与集中化）
- 结论：Gray Media 于 2026-10-26 把路易斯维尔的 WDRB（Fox）和 WAVE（NBC）合并为一个编辑部，100 多名记者，每周 80 多小时直播。报道未提裁员。
- 意义：同城双台合并后，派题台通常只保留一个。这一点是推断，报道没写。
- 来源：Gray Media combines newsrooms in Louisville — https://thedesk.net/2026/10/gray-media-combines-newsrooms-in-louisville/ — TheDesk.net / 2026-10 — ✅

**G1-15** | TV | S6 / S9 | 竞品事实（自动化替代人力）
- 结论：Gray 在 North Platte 的 KNOP 用 Cuez 云自动化，让一名主播或操作员兼管机位、字幕和混音，计划推广到更多市场。
- 意义：TV 集团的技术投资优先投向"省控制室人力"。
- 来源：Computers Are Replacing News Staff at Local ABC, CBS, FOX, & NBC TV Stations — https://cordcuttersnews.com/computers-are-replacing-news-staff-at-local-abc-cbs-fox-nbc-tv-stations/ — Cord Cutters News / 2026-02-18 — ✅（行业博客）

**G1-16** | TV | S1 | 需求信号（JD，薪资与工具）
- 结论：Nexstar 在 DC 新组 WDVM/WDCW 双台，招派题编辑，年薪 **$75,000–80,000**。职责包括追突发、派记者和摄像、协调外勤、找 UGC 并取得授权、处理版权清关。**JD 没有点名任何线索工具**，只写了"文件共享平台"。
- 意义：中大市场（DMA #8）派题岗的人力成本约 8 万美元/年，可作为"省人"类工具定价的参照。
- 来源：Assignment Desk Editor — Nexstar — https://builtin.com/job/assignment-desk-editor/7601636 — Built In / 2025-12 下架 — ✅

**G1-17** | TV | S1 | 竞品事实（scanner 基础设施）
- 结论：编辑台的"听 scanner"本身有付费基础设施。
  - Rangecast 把多台 scanner 联网，可远程收听和回放。scanner 经销商 Scanner Master 称有 "over 100 television and radio stations as well as newspapers"（100 多家电视台、电台和报社）在用。
  - 不公开价格，只能约 demo。
- 来源：
  - News Gathering — https://www.scannermaster.com/online_police_scanner_monitoring_system_a/349.htm — Scanner Master — ✅
  - https://www.rangecast.com/ — ✅（经销商口径，日期不详）

**G1-18** | TV | S1 / S3 | 凑合方案（线索绕过派题台）
- 结论：9NEWS Denver 的消费调查记者 Steve Staeger 靠在 TikTok、IG、FB 出镜发视频，形成了自己的爆料网络。线索直接私信他，**绕过台里的爆料热线和派题台**，有时比编辑部的"监听工具"更早。
- 证据："Now people are bringing me into those conversations before it's trending."（现在人们在话题升温前就把我拉进对话）
- 来源：The Assignment Desk Has Migrated — https://the-trust-shift.beehiiv.com/p/the-assignment-desk-has-migrated — The Trust Shift（TVNewsCheck 专栏作者的 newsletter）/ 2026-07-16 — ✅

**G1-19** | TV | S1 / S5 | 需求信号（编辑原话，旧）
- 结论：CBS4 Denver 的派题编辑形容这份工作"参与所有大新闻"，要不停接观众电话、核实爆料，最爱的词是"confirmed"（已确认）。
- 证据："My favorite word is 'confirmed.'"（我最喜欢的词是"已确认"）
- 来源：'Involved In All The Big Stories': Behind The Scenes With A… — https://www.cbsnews.com/colorado/news/cbs4-newsroom-assignment-desk-audra-streetman/ — CBS Colorado / 2020-07-10 — ✅（2020 年，旧）

---

## G2. 谁买单 / 付费意愿 / 美国自由撰稿人

**G2-01** | 全群体 | S9 | 需求信号（有方法论的调查）
- 结论：Muck Rack 2025（n=1,515，大多在美国，误差 ±2.5%）的结果：
  - **工具支持**：60% 觉得在"工具、培训、编辑指导"上至少有些支持，只有 19% 觉得不被支持（很不支持 7% + 有点不支持 12%）。
  - **AI 使用**：77% 用 AI，其中 ChatGPT 42%、**转写工具 40%**（补核 06 中 P-01 标 [未核实] 的数字）、写作工具 35%。
- 意义：受雇记者对"工具缺口"的抱怨并不强烈。工具痛点要落到具体环节，泛泛的"缺工具"不成立。
- 证据：每人可多选的工作类型分布为：全职受雇 57%、兼职或偶尔自由 21%、全职自由 19%、独立自出版 13%（选项可多选）。
- 来源：State of Journalism 2025（PDF）— https://media.muckrack.com/documents/6.9.2025_state_of_journalism.pdf — Muck Rack / 2025-06 — ✅（已抽取全文）

**G2-02** | INDIE, FREE | S8 / S9 | 需求信号（有方法论的调查）
- 结论：Muck Rack《Creator Journalism 2025》（1,515 份有效问卷中 522 人自认 creator journalist，主要在美国）：
  - **收入**：39% 自出版完全没收入；收入占比在 10% 以下的占 31%。自出版是全职收入（100%）的只有约 6%。
  - **动机**：57% 首要动机是创作自由，只有约 13% 为了钱。
- 意义：独立记者的自出版大多是副业，**个人付费能力很弱**。
- 证据：报告原文写 "63% of creator journalists make a portion of their income from their solo work"（63% 从个人出版中获得部分收入）。
- 来源：The State of Creator Journalism 2025（PDF）— https://media.muckrack.com/documents/10.22.2025_v3_The_State_Of__Creator_Journalism_2025.pdf — Muck Rack / 2025-10 — ✅

**G2-03** | FREE | S9 | 市场数据 / 需求信号（美国样本）
- 结论：NWU（全国作家工会）Freelance Solidarity Project 的费率共享库自 2020 年起收集了 1,275 条匿名记录，自愿填报。
  - 平均约 **$1/词**，自 2020 年起基本没变。
  - 跨性别受访者报 $0.38/词，西语裔 $0.34/词。
- 证据：一名全职自由撰稿人说 "My rates are the lowest they've been since 2020 when I started"（我的费率是 2020 年入行以来最低的）。
- 来源：Freelance journalism rates are worse than you think… — https://www.objectivejournalism.org/p/freelance-journalism-rates-are-worse-than-you-think-theyve-barely-changed-since-2000 — The Objective / 2026-09-28 — ✅（自愿填报，有选择偏差）

**G2-04** | FREE, NATL | S9 | 需求信号（转行行为 + 原话）
- 结论：有记者靠给 AI 公司做标注和评测补贴收入（Outlier/Scale AI、Mindrift、HireIO 等）。
  - 一位从业 20 多年的都市报记者，时薪从约 40 美元降到 10 美元，培训时间不付费。
  - Scale AI 称约 75% 做这类工作的记者在美国以外。
  - E&P 无法统计总人数。
- 证据：匿名记者说 "Journalism really doesn't have a lot of safety nets."（新闻业真没什么安全网）
- 来源：From newsrooms to AI side hustles… — https://www.editorandpublisher.com/stories/from-newsrooms-to-ai-side-hustles-why-journalists-are-training-the-machines-that-may-replace-them,258222 — Editor & Publisher / 2025-10-21 — ✅

**G2-05** | INDIE, LOCAL | S8 / S9 | 需求信号（已发生的花钱行为）
- 结论：Press Forward 向 205 家小编辑部（年预算低于 100 万美元）各发了约 10 万美元的无限制资金，分两年发放。从 Nieman Lab 的个案看：
  - **主要用途**：人力（编辑、记者、销售、筹款）、印刷、还债、房租。
  - **技术和工具的开支**：只有一家买了"新软件"（未具名），另有电脑和相机升级、建网站和广告位。点名的软件只有 Midjourney。
- 意义：小编辑部拿到"自由支配的钱"时，**几乎不花在新闻工具上**。
- 证据：Planet Detroit 的 Ignaczak 说 "$100,000 over two years is not enough to achieve that."（两年 10 万美元不够实现那个目标）
- 来源：Press Forward gave $20 million to 205 local newsrooms… — https://www.niemanlab.org/2026/10/press-forward-gave-20-million-to-205-local-newsrooms-over-two-years-heres-how-some-of-them-spent-it/ — Nieman Lab / 2026-10-29 — ✅（个案，不是汇总统计）

**G2-06** | FREE | S9 | 凑合方案（自费垫付，旧）
- 结论：自由撰稿人通常要自己先垫付差旅（机票、住宿、租车、保险、签证），按刊发或终稿验收后才报销，可能拖数月到一年。作者本人一度垫付近 4,000 美元。
  - 应对办法：谈预付款、请编辑预付可预见的费用、在发票里加信用卡利息、申请全额资助的 fellowship。
- 证据："this has posed the biggest financial barrier and burden to me in my freelance career"（这是我自由职业生涯中最大的财务障碍和负担）
- 来源：When Travel Expenses Get Too Expensive — https://www.sej.org/publications/freelance-files/when-travel-expenses-get-too-expensive — SEJ / 2018-08-22 — ✅（2018 年，旧；没有提到软件工具开支）

**G2-07** | 全群体 | — | 市场数据（新闻相关数据工具的公开价）
- 结论：可查到的公开价格（记者或买方能直接看到的）：
  | 产品 | 公开价 | 记者政策 |
  |---|---|---|
  | Shovels（建筑许可数据）| 免费档 $0/月（1 年历史、500 credits）；Basic $599/月；Pro $999/月；企业询价 | 未提记者折扣 |
  | Hamlet（会议转写/检索）| 商业方案"约 $1,000/月起" | 对认证记者、学者、部分非营利**免费开放 API**（见 G3-07）|
  | Dataminr First Alert（政府）| 约 $45,000/年（见 G1-06）| 新闻版不公开 |
  | ACBJ BizLeads（Business Journals 的 B2B 线索数据）| 低至 $66/月（2020）| — |
- 来源：
  - https://www.shovels.ai/pricing — ✅（2026-11 访问）
  - https://www.myhamlet.com/pricing — ✅
  - BizLeads：https://www.biia.com/american-city-business-journals-launches-bizleads/ — BIIA 转载 Business Wire / 2020-03-04 — ✅

**G2-08** | TV | — | 需求信号（采购决策人）
- 结论：TV 端的 AI 和工具决策在**集团层**。
  - 参与决策的头衔有：VP digital services（Hearst）、VP news operations and technology（Fox）、VP emerging technology operations（Scripps）、AVP news technology and operations（Sinclair）。
  - 同时 Cuez 称新闻总监、制片、记者也越来越多地去看展台演示，说明一线影响力在上升。
- 来源：G1-09、G1-12 同源 — ✅

**G2-09** | INDIE, LOCAL | — | 市场数据（数据产品"记者免费、商业付费"的普遍模式）
- 结论：本地公共数据类产品普遍采用"商业客户付费、记者免费或打折"的双边模式：
  - **Hamlet**：认证记者免费 API；商业方案约 $1,000/月起。
  - **OpenCorporates**：调查记者免费（见 05 C-44）。
  - **PermitMint**（1,250 万条许可、99 个城市）：对记者免费，署名即可。
  - **RatRadar**（30+ 城市餐厅检查）：专门开了"记者与研究者"入口，价格未列。
- 意义：这类产品的收入来自地产、承包商、安全和政策客户，**记者是被补贴的一方**。
- 来源：
  - https://www.myhamlet.com/free-data-access — Hamlet / 2026-10-23 — ✅
  - https://permitmint.com/data/ — ✅
  - https://ratradar.com/b2b/journalists — ✅

---

## G3. 商业 / 地产 / 开发条线

**G3-01** | LOCAL, NATL | S1 / S2 | 凑合方案 / 市场数据（数据结构）
- 结论：美国**没有全国性的建筑许可系统**。许可由市、县、特区乃至镇各自签发，各用各的软件（Accela、EnerGov、Socrata、OpenGov、ArcGIS 及数百个定制系统）。格式、访问政策、分页和鉴权都不一样，页面改版会让爬虫"静默失效"。多数门户每天夜间更新，有的每周更新。
  - 一家商业爬取方从 DFW 的 12 个门户做起，扩展到 248 个以上，每天处理 3 万多条。
- 证据：
  - "The United States has no national building permit system."（美国没有全国性建筑许可系统）
  - "The fundamental challenge… isn't technical — it's political and jurisdictional."（根本挑战不在技术，而在政治和辖区）
- 来源：248 Cities and Counting: How We Built the Largest Permit Database… — https://permitlify.com/blog/248-cities/ — Permitlify / 2026-03-28 — ✅（厂商博客）

**G3-02** | LOCAL, NATL | S2 | 竞品事实 + 定价
- 结论：Shovels 声称覆盖 2,820 多个辖区（约占美国人口 85%）、1.96 亿多条许可，多数从 2010 年起，**每月更新两次**。客户是建材、建筑科技、能源、家装、地产、电信、保险，**页面没有提到媒体和记者**。定价 $0 / $599 / $999 每月（见 G2-07）。
- 意义：许可数据已有商业聚合，但更新频率是半月级，适合背景研究（S2），**不适合当突发线索（S1）**。
- 来源：
  - Permits Data — https://www.shovels.ai/data/permits — ✅
  - Pricing — https://www.shovels.ai/pricing — ✅

**G3-03** | LOCAL, INDIE | S2 | 凑合方案（调查记者的人工拼接）
- 结论：Investigative Post（Buffalo）追查两名房东，靠人工交叉了十几类记录：
  - 产权与交易：契据、抵押、买卖协议
  - 主体与身份：州务卿 LLC 登记、Facebook 资料（查籍贯）
  - 违规与执法：城市检查违规、住房法院罚款、911/311 呼叫记录、县卫生局铅漆检查
  - 欠费：市县房产税、排污费、垃圾费
  - 记者通过 LLC 层层追溯，把 69 处房产关联到这两人及其妻子，比市政府自己统计的 61 处还多。
- 意义：**"跨库实体关联"是地产调查的核心体力活**，目前没有现成工具，靠记者手工完成。
- 证据："Investigative Post analysis connected 69 properties to the men and/or their wives."（Investigative Post 的分析把 69 处房产关联到这两人和/或其妻子）
- 来源：Track record of landlords includes code violations, unpaid taxes — https://investigativepost.org/2026/10/20/two-downstate-investors/ — Investigative Post / 2026-10-20 — ✅

**G3-04** | LOCAL | S5 | 凑合方案的风险（政府数据错误）
- 结论：Orlando Sentinel 根据佛州餐厅检查数据报道 Hammered Lamb 因虫害被勒令停业，结果是州数据把 11 年前同一地址的一家素食店的违规记到了它头上。报社事后修改了检查报道的发布做法。
- 意义：**直接搬运政府结构化数据，需要实体消歧和核实层**。
- 证据："An error in Florida's state data confused the Hammered Lamb with a vegan restaurant"（佛州数据错误把 Hammered Lamb 和一家素食店弄混了）
- 来源：Data glitch leads to error and a reminder for journalists — https://www.editorandpublisher.com/stories/data-glitch-leads-to-error-and-a-reminder-for-journalists,249570 — E&P / 2024-05-02 — ✅

**G3-05** | LOCAL, NATL | S2 | 竞品事实 + 凑合方案描述
- 结论：餐厅检查数据的痛点有一家针对记者的数据商做了具体描述：
  - 各城门户为消费者设计，一次只能查一家店，没有批量下载、API 和历史存档。
  - 查一个有 50 家门店、横跨 8 座城的连锁要花好几天。
  - FOIA 批量申请要几周，回来的常常是 PDF。
  - 各城评分体系互不兼容：芝加哥用字母等级；纽约用字母等级加分数；洛杉矶用 A/B/C 加扣分；波士顿只公布违规数、没有等级。
- 证据："The inspection data is public. Getting it shouldn't take weeks."（检查数据是公开的，拿到它不该花几周）
- 来源：Restaurant Health Inspection Data for Journalists & Researchers — https://ratradar.com/b2b/journalists — RatRadar / 2026 访问 — ✅（厂商口径，描述的是凑合方案的痛点）

**G3-06** | LOCAL | S1 / S6 | 竞品事实 + 需求信号（已发生的采购）
- 结论：McClatchy 从 2021 年起与 United Robots 合作，用机器人生成房产交易和高中体育等"例行社区信息"，覆盖 8 个市场。理由是这些题能带来新受众，但没有记者人手去报。
- 证据：McClatchy 的 Cynthia DuBose："We want our journalists to produce journalism, not track down information."（我们希望记者做新闻，而不是去追信息）
- 来源：How McClatchy uses automation to fill content gaps — https://newspapers.org/stories/united-robots,4162172 — America's Newspapers / 2023-01-18 — ✅

**G3-07** | LOCAL | S1 | 竞品事实（新进入者，与本平台同构）
- 结论：United Robots 2026 年推出 **DataDesk**，监控建筑许可、餐厅检查、法院文书、政府决定等本地公共数据，**向编辑部推送"值得报"的线索**，判断和采访留给记者。与"几家美国地方编辑部"一起打磨，计划夏季后上线，不公开价格。
- 证据："Deciding what's a story, and doing the reporting that makes it one, stays with you."（判断什么是新闻、通过采访把它做成报道，仍由你负责）
- 来源：DataDesk: Alerting your newsroom to local stories it never had time to… — https://www.newspapers.org/stories/united-robots,4167029 — America's Newspapers（United Robots 供稿）/ 2026-07-15 — ✅

**G3-08** | LOCAL, INDIE | S1 | 竞品事实（主要客户是开发商；更新 05 的 C-01）
- 结论：Hamlet 的数据：
  - **覆盖**：2,400 多个市县、11.2 万多场会议存档、3,200 多名官员。（05 引用的 2026-02 新闻稿称 3,000 多个机构，口径不同。）
  - **地产版功能**：竞品名、项目地址、"zoning variance" 等关键词提醒，按辖区监控，社区情绪分析。
  - **商业方案**："Plans start at about $1,000 a month"（方案约每月 1,000 美元起）。Hamlet 声明不卖给被报道的官员及其竞选团队。
  - **记者政策**：免费检索前 40 条结果，申请后开通"press and research access"，认证记者可免费用 API（不得转售或批量再分发，需要署名）。
- 意义：**开发商已在为"会议 → 项目早期信号"付费**，记者版是免费的副产品。这直接对标能力 1，商业模式也已验证。
- 来源：
  - Hamlet for real estate — https://www.myhamlet.com/industries/real-estate — ✅
  - Pricing — https://www.myhamlet.com/pricing — ✅
  - Press — https://www.myhamlet.com/press — ✅
  - Free Data Access Terms — https://www.myhamlet.com/free-data-access — 2026-10-23 — ✅
  - 补充：urbanproxima 2025-06 称付费客户是 "real estate developers and retailers"（地产开发商和零售商）— https://www.urbanproxima.com/p/how-hamlet-makes-public-data-useful — ✅

**G3-09** | LOCAL | S1 / S8 | 竞品事实（Business Journals 模式）
- 结论：American City Business Journals 旗下有 44 份城市商业周刊。
  - **周度公共记录**：每周汇编本地法院和政府门户的公共记录（地产交易、留置权、建筑许可、破产），只对付费会员开放。
  - **BizLeads**：同一套"本地商业数据采集能力"还做成 B2B 线索产品，低至 $66/月（2020）。
  - 意义：**把地产和商业公共记录汇编后卖给本地商业读者，是已被验证的模式**，买方是商业读者和销售人员，不是记者。
- 来源：
  - BizLeads：https://www.biia.com/american-city-business-journals-launches-bizleads/ — 2020-03-04 — ✅
  - 公共记录栏目说明：https://www.bizjournals.com/boston/news/2024/05/28/public-records-real-estate-deals-liens-permits.html — BBJ / 2024-05-28 — ⚠️（Cloudflare 拦截，只核对了搜索摘要："collects Boston-area public records on real estate transactions, liens, building permits and bankruptcies and compiles them weekly"，即每周汇编波士顿地区的地产交易、留置权、建筑许可和破产记录）

**G3-10** | LOCAL | S1 | 需求信号（条线记者自述，弱）
- 结论：Columbus Dispatch 2025-10 起设"trending business and real estate"记者岗，覆盖 zoning、area commissions、可负担住房和住宅市场趋势。她的个人站报道样本里常见"according to preliminary site plans filed with the city"（据向市里提交的初步场地规划）这类写法。
- 意义：**场地规划和 zoning 申请是地产线索的一手来源**。至于她具体怎么找，原文被付费墙截断，没拿到。
- 证据："Who knew I could be so impassioned about zoning and area commissions…"（谁能想到我会对 zoning 和区域委员会这么上心）
- 来源：
  - Meet Dispatch trending business, real estate reporter Emma Wozniak — https://www.yahoo.com/lifestyle/articles/meet-dispatch-trending-business-real-123846749.html — Yahoo 转载 Columbus Dispatch / 2026-02-01 — ✅
  - https://www.emmagwozniak.com/ — ⚠️（只看了搜索摘要）

---

## G4. CrimeRadar（Android 包 com.newsbreak.crimeradar）公开事实

**G4-01** | （消费端）| S1 | 竞品事实（规模与形态）
- 结论：
  - **Google Play**：开发者 "Scoopz LLC"，**1M+ 下载**，4.8 星，**50.8K 条评论**，"Contains ads · In-app purchases"（含广告、有内购）。
  - **App Store**：名称为 "CrimeRadar Dispatch Audio"，卖方 **Scoopz Inc.**，类别 News，**2025-05-27 上架**，最新版本 2026-10-28，评分 4.90（45,874 个评分），免费下载。
  - **功能自述**：追踪急救人员电台音频，用 AI 摘要并上地图，按位置推送提醒。
- 来源：
  - Google Play — https://play.google.com/store/apps/details?id=com.newsbreak.crimeradar&hl=en_US&gl=US — ✅（curl_cffi 2026-11-03）
  - iTunes lookup — https://itunes.apple.com/lookup?id=6746114452&country=us — ✅
  - App Store 页 — https://apps.apple.com/us/app/crimeradar-dispatch-audio/id6746114452 — ⚠️（网页重定向到 CN 区，数据取自 lookup API）

**G4-02** | （消费端）| S1 | 竞品事实（官方 FAQ）
- 结论：官网 FAQ 写明：
  - **覆盖**：美国 10,000 多个城市和地区。
  - **数据来源**：公开的 scanner 频道、公开报告和其他开放的公共安全数据；不接受个人提交 feed。
  - **生成方式**：转写、标题、摘要都由自动系统生成。公司 "does not independently verify the live dispatch information"（不独立核实实时调度信息）。
  - **保留期**：地图只保留 14 天，旧事件不可检索。
  - **价格**：免费。（05 记录的 $9.99/月、$79.99/年是内购价，与"免费下载"并不矛盾。）
- 来源：FAQ — https://uscrimeradar.com/faq — CrimeRadar / 2026-11 访问 — ✅

**G4-03** | （消费端）| S7 / S8 | 竞品事实（与 NewsBreak 广告平台的公开关系）
- 结论：NewsBreak Ads 帮助中心有一篇专页，宣布把 CrimeRadar 作为 "another strategic partner"（又一个战略合作伙伴）接入 NewsBreak Ads 广告体系，并称 "As of May 2026, it is ranked #4 in the Apple App Store for News"（截至 2026 年 5 月，在 App Store 新闻类排第 4）。页面还建议家庭安防、保险、汽车安全类广告主投放。
- **只陈述可见事实**：包名前缀 com.newsbreak、NewsBreak Ads 把它列为合作伙伴并售卖其广告位。股权或隶属关系**没有公开披露**，第三方评测站的"由 Particle Media/NewsBreak 开发"说法未核实，不采用。
- 来源：CrimeRadar — NewsBreak Ads Help Center — https://adhelp.newsbreak.com/hc/en-us/articles/45870702577037-CrimeRadar — NewsBreak / 2026 — ✅（curl_cffi）

**G4-04** | （消费端）| S1 / S5 | 竞品事实（误报事件：Bend, OR，原始报道）
- 结论：2025-12 初，Redmond 的 "Shop with a Cop" 活动被 CrimeRadar 的 AI 文章写成 "shot with a cop"，暗示 Bend 有警员殉职。Bend 警方公开辟谣。
  - 这是 02 中 TV-C02 当时缺的**原始出处**，可替换聚合站来源。
- 证据：Bend 警方传播经理 Sheila Miller："That's scary for our community."（这让社区很害怕）；并说 "there's no accountability"（没有人负责）。
- 来源：Police warn AI-generated blog posts from scanner traffic spread misinformation — https://www.centraloregondaily.com/news/local/police-warn-ai-generated-blog-posts-from-scanner-traffic-spread-misinformation/article_f20ed4dc-0ba6-4be0-818e-d89b4ba0ee48.html — Central Oregon Daily / 2025-12-03 — ✅

**G4-05** | （消费端）| S1 / S5 | 竞品事实（误报：Streetsboro、Twinsburg, OH）
- 结论：2025-12-08 至 12-09，俄亥俄 Streetsboro 和 Twinsburg 警方在社媒警告居民。05 已记录 Streetsboro "fire alarm→firearm" 的细节，这里补两点：
  - **Twinsburg 警方**：该 app "has been found to interpret radio transmissions inaccurately"（被发现错误解读无线电通话）。
  - **Streetsboro 警方**：警告相关帖子意在引诱点击附带假音频或视频的链接，建议点过的人改密码。
  - Cleveland19 发稿时没有拿到公司回应。
- 来源：Local police warn against new crime app spreading dangerous false reports — https://www.cleveland19.com/2025/12/10/local-police-warn-against-new-crime-app-spreading-dangerously-false-reports/ — Cleveland 19 / 2025-12-10 — ✅

**G4-06** | （消费端）| S1 / S5 | 竞品事实（误报：Columbia, MO）
- 结论：2025-12-09，CrimeRadar 推送"一名青少年在哥伦比亚市中心中枪"。信息来源是 Randolph、Jackson、Perry 三个不属哥伦比亚管辖的县的调度，还引用了密苏里州并不存在的 "Genevieve County"。
- 证据：警察局长 Jill Schlude："these tools often rely on incomplete data, lack context, and can easily spread misinformation"（这些工具常依赖不完整数据、缺乏语境，很容易传播错误信息）
- 来源：AI crime app spreads false report of downtown shooting — https://www.kbia.org/missouri-news-network/2025-12-11/ai-crime-app-spreads-false-report-of-downtown-shooting — KBIA / Missouri News Network / 2025-12-11 — ✅

**G4-07** | （消费端）| S1 | 竞品事实（BBC Verify 调查与规模）
- 结论：2025-12 BBC Verify 调查后，CrimeRadar 道歉，称已注意到 "serious transcription issues"（严重的转写问题）。二手报道援引的数字是：**200 万以上用户**、"上个月"最多 70 万次下载。
- 证据：公司声明 "We apologize for any distress or disruption this caused"（对造成的困扰和干扰表示歉意）。
- 来源：
  - AI Crime App CrimeRadar Sparks Panic With False Alerts… — https://news.shib.io/2025/12/29/ai-crime-app-crimeradar-sparks-panic-with-false-alerts-company-issues-apology/ — The Shib Daily / 2025-12-29 — ⚠️（二手转述 BBC）
  - INC-25-0026 — https://www.topaithreats.com/incidents/INC-25-0026-crimeradar-ai-false-crime-alerts/ — ⚠️（事件库）
  - BBC 原页 https://www.bbc.com/news/videos/c4g4v3yd28yo — ❌（WebFetch 被拒）

**G4-08** | （消费端）| S1 / S5 | 竞品事实（误报：Boulder 县三起，CO）
- 结论：GovTech 转载 Colorado Hometown Weekly 2026-03-02 的报道，记录了 Boulder 县三起 CrimeRadar 误报：
  - **Frederick（1-30）**：把消防演习当成"市中心商业火灾"。
  - **Longmont**：报了一起不存在的公寓火灾，帖子之后消失。
  - **Boulder**：把 "fire rider" 听成 "firefighter"，编出一名消防员送医。
  - 同文还记录了 Nextdoor（Samdesk 驱动）误报"联邦设施枪手"。
- **关键事实**：Frederick-Firestone 消防区表示将改用**不公开广播的战术频道**。也就是说，**AI 误报正在促使机构把通话移出公开频道**，这直接威胁能力 2 的数据源。
- 证据：
  - Boulder Fire-Rescue 的 Jamie Barker："It took information that it heard incorrectly, and then it summarized it incorrectly"（它先听错，又总结错）
  - 公司在每条告警上标注 "Not official report. AI-generated from public dispatch audio. Verify with official sources."（非官方报告。由公开调度音频经 AI 生成。请向官方来源核实。）
- 来源：AI App Sends False Emergency Alerts in Boulder County, Colo. — https://www.govtech.com/em/preparedness/ai-sends-false-emergency-alerts-in-boulder-county — GovTech / 2026-03-02 — ✅

**G4-09** | （消费端）| S1 / S5 | 竞品事实（误报：Mount Vernon, MO 小学）
- 结论：2026-04-10，副警长在电台说 "show me out at the elementary school"（我已到小学），被转写成 "shooting at"（在……开枪）。学校随即软封锁。2026-04-14 公司道歉，说已更新音频处理流程，并加强涉及学校和枪支事件的核实。
- 证据：
  - 校监 Christina West："An app like that should not be able to cause unnecessary alarm like that with false information."（这样的 app 不应该能用错误信息造成不必要的恐慌）
  - 警长 Brad DeLay："Somehow, that AI bot translated that into shots at the elementary school."（那个 AI 机器人不知怎么就把它翻译成了小学枪击）
- 来源：AI app sends false shooting alert to Mount Vernon School District parents — https://www.ky3.com/2026/04/13/ai-app-sends-false-shooting-alert-mount-vernon-school-district-parents/ — KY3 / 2026-04-13（含 04-14 声明）— ✅

**G4-10** | （消费端）| S1 / S5 | 竞品事实（误报：Orange、Greenfield, MA）
- 结论：
  - **Orange（2026-04-27）**：把一个人名听成 "shooter at Town Hall"（市政厅有枪手），帖子被转到社媒，邻镇 Athol 警方专门打电话核实。
  - **Orange（05-11）**：危机热线电话被写成"可能的枪击"。
  - **Greenfield（07-30）**：持刀事件内容准确，但时间错了 3 小时。
  - **公司说法**：地址自动核验；涉及儿童等敏感事件升级到人工审核；负面反馈够多会自动下架帖子。Orange 那条"没有触发高风险升级标准"。
- 证据：
  - Greenfield 局长 Todd Dodge："the accuracy of information is a big concern"（信息准确性是一大担忧）
  - 调度主管 Cindy Hunter 指出，核实电话会占用正在处理紧急情况的调度员。
- 来源：Local police chiefs weigh in on pitfalls, benefits of AI scanner apps — https://www.recorder.com/2026/08/27/local-police-chiefs-weigh-in-on-pitfalls-benefits-of-ai-scanner-apps/ — Greenfield Recorder / 2026-08-27 — ✅

**G4-11** | （消费端）| S1 / S5 | 竞品事实（误报：University of Akron, OH）
- 结论：2026-07-14，CrimeRadar 发出 University of Akron "可能有活跃枪手"的提醒。校警到学生会核查，确认没有枪击。Akron 警方也没接到相关报警。公司对 BBC Verify 说 "We have enhanced our audio processing protocols"（我们已加强音频处理流程），并在推出让机构和社区提交更正的功能。
- 证据：UAPD 局长 Jim Gilbride 呼吁 "rely on official University alerts and communications"（以学校官方提醒和通报为准）。
- 来源：Crime app using AI generated false report of UA shooting — https://www.yahoo.com/news/us/articles/crime-app-using-ai-generated-132125713.html — Yahoo 转载 Akron Beacon Journal / 2026-07-14（07-15 更新）— ✅（Beacon Journal 原站 WebFetch 被拒）

**G4-12** | （消费端）| S1 | 竞品事实（其他事件，只有二手来源）
- 结论：一家 scanner 零售商的博客汇总称，2026-08-04 德州 Waco 也出现 CrimeRadar 误报引发恐慌（来源是 KWTX 的 Facebook 视频），并称 CrimeRadar 服务"数百万用户"。
- 来源：CrimeRadar AI False Alerts: Verify Before You Share (2026) — https://www.policeradio.org/blogs/news/crimeradar-ai-false-alerts-verify-before-share — PoliceRadio.org（卖 scanner 的零售商，有利益相关）/ 2026-08 — ⚠️（Waco 原始报道未打开）

**CrimeRadar 公开事件时间线（汇总）**

| 日期 | 地点 | 误报内容 | 原始报道 |
|---|---|---|---|
| 2025-05-27 | — | iOS 上架（Android 约 2025-05-22，见 05）| iTunes lookup |
| 2025-12-03 | Bend / Redmond, OR | "Shop with a Cop"→"shot with a cop" | Central Oregon Daily |
| 2025-12-08/09 | Streetsboro、Twinsburg, OH | fire alarm→firearm；警方公开警告 | News5（05）、Cleveland19 |
| 2025-12-09 | Columbia, MO | 跨县调度拼出"市中心少年中枪"，含不存在的县名 | KBIA |
| 2025-12 | 多州 | BBC Verify 调查，公司道歉；200 万以上用户（二手）| BBC（未打开）/ 二手 |
| 2026-01-30 起 | Frederick、Longmont、Boulder, CO | 演习当火灾、虚构火灾、fire rider→firefighter；消防区改用非公开频道 | GovTech / Colorado Hometown Weekly |
| 2026-04-10 | Mount Vernon, MO | "show me out at"→"shooting at"，学校软封锁 | KY3 |
| 2026-04-27 / 05-11 | Orange, MA | "shooter at Town Hall"、虚构枪击 | Greenfield Recorder |
| 2026-05 | — | NewsBreak Ads 称其为 App Store 新闻类第 4 | NewsBreak Ads 帮助中心 |
| 2026-07-14 | University of Akron, OH | 虚构活跃枪手 | Akron Beacon Journal（Yahoo）|
| 2026-08-04 | Waco, TX | 误报引发恐慌 | KWTX（未打开）|

---

## 有效证据计数

| 部分 | 条数 | 其中 ⚠️ |
|---|---|---|
| G1 | 19 | 1（G1-05）|
| G2 | 9 | 0 |
| G3 | 10 | 2（G3-09 部分、G3-10 部分）|
| G4 | 12 | 3（G4-07、G4-12；G4-01 部分）|
| **合计** | **50** | **约 6 条整体或部分为 ⚠️** |

---

## 最反常识 / 最重要的 5 条

1. **AI scanner 误报正在反过来"关掉"数据源**（G4-08）
   - Frederick-Firestone 消防区因为 CrimeRadar 误报，要改用不公开广播的战术频道。
   - 加上 02 里的警用加密趋势，说明**消费端 AI 摘要 app 的口碑问题会外溢**：每起"小学枪击"误报都在给机构撤出明文频道提供理由。
   - 能力 2 不能只看准确率，还要考虑它和整个生态的关系，包括保留原音频、标注线索属性，以及与机构的更正通道。
2. **CrimeRadar 规模很大，并且已接入 NewsBreak 广告体系**（G4-01、G4-03）
   - 规模：Android 100 万以上下载、iOS 4.6 万个评分；二手报道称用户 200 万以上；2026-05 在 App Store 新闻类排第 4。
   - 误报：从 2025-12 到 2026-08，至少 6 个州有公开记录，多数涉及学校或枪击。
   - 公开可见的关系只有包名前缀和 NewsBreak Ads 的"战略合作伙伴"专页。**如果本平台属于同一体系，品牌风险是共享的**。
3. **TV 的线索工具预算在集团层，而集团路线图里没有"线索发现"**（G1-09、G1-10、G1-12）
   - 拍板方是集团的 VP 技术或数字岗。
   - LMA 为 10 家广电集团制定的 AI 路线图聚焦改版、剪辑、销售和档案，没有提到采集或派题台。
   - Dataminr 走的路是"嵌入 Wolftech/iNEWS"，并主打政府市场（公开采购价约 4.5 万美元/年）。
   - 地方台派题岗约 8 万美元/年，JD 不点名任何线索工具。
4. **"会议/许可 → 项目早期信号"已经有人付钱，但付钱的是开发商**（G3-08、G3-02、G3-09、G2-09）
   - Hamlet 商业版约 $1,000/月起，对认证记者免费开放 API。
   - Shovels 收 $599–999/月，客户里没有媒体。
   - Business Journals 把公共记录汇编后卖给商业读者，并做成 BizLeads。
   - 地产和商业公共记录的变现路径是"B2B 收费、记者免费"。记者是**分发和信用渠道，不是收入来源**。
5. **小编辑部拿到无限制资金几乎不买工具，独立记者大多不靠自出版赚钱**（G2-05、G2-02、G2-03）
   - Press Forward 的 205 家受助者主要把钱花在人、印刷、房租和还债上。
   - 39% 的 creator journalist 自出版零收入。
   - NWU 数据显示，美国自由撰稿平均费率 6 年停在约 $1/词。
   - 结论：**向记者个人收费的天花板很低**。

---

## 证据薄弱、需要补的地方

- **一线 assignment editor 原话**：Reddit（r/TVNews、r/Journalism）和 Facebook 的 "Overheard on the Assignment Desk"（6,760 赞）都没抓到。建议用浏览器登录态补抓，或做定性访谈。
- **派题台是否被集团集中化**：目前只证实了主控和新闻生产在 hub 化（G1-11），以及同城双台合并（G1-14）。"集团中央派题台"仍然**没有找到直接证据**。
- **Dataminr 新闻版在美国地方台的实际价格和渗透率**：只有政府同族产品的采购价，以及"5 人以下编辑部不划算"的定性说法。
- **记者自费买工具的美国调查**：仍然缺。可试 Pew 2022 记者调查原始问卷、ONA 会员调查、SPJ Freelance Community 调查（如有）。
- **地产/商业条线的记者原话**：Wozniak 两篇自述都被付费墙截断。IRE tipsheet（LLC、契据）没有在本轮搜索中出现。Business Journals 公共记录页被 Cloudflare 拦截（⚠️）。
- **CrimeRadar**：BBC Verify 原文和 Waco 原始报道没打开。200 万用户和 70 万次月下载只有二手来源。公司与 NewsBreak 的股权或隶属关系没有公开披露，**需要内部确认**。
