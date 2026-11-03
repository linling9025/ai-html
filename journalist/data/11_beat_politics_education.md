# 11 · 条线深挖：①政治 / 州与联邦政府 / 选举　②教育（K-12 与高教）

## 0. 文件说明

- **覆盖范围**：两个条线 × 五个群体（LOCAL / TV / INDIE / NATL / FREE）× 九个环节（S1–S9）。重点是这两个条线的信息来源有哪些，哪些靠记者自己能方便解决、哪些不好解决，以及条线专用的工具和竞品。
- **来源数**：约 52 个独立 URL，全部实际打开过（WebFetch、curl 文本抽取，或下载 PDF 后用 pypdf 抽取全文；EWA 2021 报告 PDF 共 113k 字符，已全文检索）。另外引用了本项目已采集的两份原始数据：`raw/reddit_posts.jsonl` 和 `raw/reddit_coded_*.jsonl`（Reddit 原帖全文），以及 `raw/jobs_journalismjobs.jsonl` 和 `raw/jobs_greenhouse.jsonl`（JD 原文，2026-10～11 抓取）。这两类引用标为"✅（项目原始数据）"。
- **正文条目**：政治条线 20 条（P-01～P-20），教育条线 17 条（E-01～E-17），一张竞品/工具表（30 项）。
- **与 03、05 的关系**：EWA 2021 原来只有摘要级数字（03 的 L-22 注明"PDF 超过 10MB 无法抓取"），本轮下载 PDF 补出了完整的信源使用率、信任度和挑战分布（E-01、E-02）。Plural 价格和 SAI360 收购沿用 05，本轮重新打开了定价页核实。
- **主要局限**：
  1. **EWA 之后没有新一轮"State of the Education Beat"**。EWA 报告页只列出 2016 和 2021 两版，2021 版的调查做于 2020 年（n=419）。教育记者的量化需求数据因此偏旧，2023–2026 年只能靠记者原话、JD 和行为证据来补。
  2. **政治/选举记者没有专门的行业协会调查**。教育有 EWA，政治没有对应组织，只有 Collier Prize 2025 的小样本调查（n=51）和 Pew 2022 的州议会记者普查。
  3. 打不开、未写入结论的：opensecrets.org 新闻页（Cloudflare，其 2026-10"州与联邦数据统一看板"只见到搜索摘要）；LegiScan 价格页（Cloudflare，价格未核实）；Votebeat 原文（Akamai 拒绝访问，改用 PR Newswire 通稿）；Federal News Network（403，NCES"只剩 3 名员工"未写入，改用 Pell Institute 和 EWA 的数字）；Ballotpedia 地方选举覆盖页（内容为空）。
  4. 立法追踪、竞选财务这类工具的买方主要是游说方。工具价格属于**供给数据**，不能当作记者需求证据。
- **类型标注**：需求信号（记者原话、JD、使用或采购行为、有方法论的调查）／市场数据／凑合方案／竞品事实。

---

## 1. 条线 × 九环节速览

> 每个格子写"做什么 → 主要来源 → 难度"。难度标记：✅ 能自己方便解决　⚠️ 费力但能　❌ 不好解决。括号里是证据 ID。

### 1A 政治 / 州与联邦政府 / 选举

| 环节 | 记者日常在做什么 | 主要来源 | 难度与凑合方案 |
|---|---|---|---|
| S1 发现线索 | 盯议会日程、听证、表决、州长和机构动向；选举季盯候选人登记和竞选财务申报 | 州议会网站、听证直播、LegiScan 免费版、Digital Democracy Tip Sheets（加州、夏威夷）、新闻通稿 | ⚠️ 州议会记者在减少（P-01、P-02）。加州有 AI 提示单（P-08），其他州主要靠人在现场盯和自己跑网站 |
| S2 背景研究 | 查法案文本和历次版本、示范法案（如 ALEC）、表决记录、竞选资金与游说 | 州议会网站、LegiScan、Congress.gov API、FEC.gov、各州竞选财务系统、OpenSecrets / FollowTheMoney | ⚠️ 联邦层面免费数据多，但聚合层在流失（P-09、P-10）。❌ 地方候选人财务常是扫描 PDF（P-11） |
| S3 找信源 | 议员、幕僚、游说者、选举官员、专家 | 现场"press pack"、Votebeat Expert Desk、选举官员 | ⚠️ 选举官员不习惯和媒体打交道（03 L-26）。独立记者拿不到记者证（P-03） |
| S4 采访/素材 | 听证会、记者会、候选人活动、党组织会议 | 现场、直播、C-SPAN | ⚠️ 被排除在简报会外约占 2/3（P-04）；县党委会议禁止录音（P-18） |
| S5 核实 | 核对言论、选举规则、诉讼、选举结果 | Votebeat Expert Desk、选举官员、FactCheck | ⚠️ 免费专家台由慈善资金支撑（P-14） |
| S6 写作/制作 | 日常快讯 + 周末深度；选民指南；选举夜结果页 | AP 选举结果、DDHQ、自建爬虫 | ❌ 下沉选举结果（县、市、学区）没人提供，靠手工复制粘贴，AI 爬虫在选举夜失败（P-12） |
| S7 发布/分发 | 选举结果嵌入、选民指南插件 | AP、APFJ、Knight Election Hub（已结束）、Newspack | ⚠️ 小媒体靠基金会补贴拿到 AP 结果（P-13） |
| S8 受众/变现 | 政策情报付费产品（Politico Pro、State Affairs） | — | 主要是 NATL / B2B。Politico 的 AI 报告工具被工会仲裁叫停（P-16） |
| S9 职业/生存 | 州议会岗位缩减、学生补位、选举季倦怠 | — | 学生在 30 个州补位（P-05）；TV 编辑台在选举季被观众辱骂（P-18） |

### 1B 教育（K-12 与高教）

| 环节 | 记者日常在做什么 | 主要来源 | 难度与凑合方案 |
|---|---|---|---|
| S1 发现线索 | 盯多个学区的校董会、州教育委员会、预算季、考试成绩发布 | 校董会 YouTube 直播与录像、议程 PDF、LocalLens、AP School Board Search、家长群 | ⚠️ 大机构已用 AI 转写检索（E-06、E-07）。❌ 约三分之一亚利桑那学区根本不录像（E-08） |
| S2 背景研究 | 考试、入学、纪律、财务、教师人事数据 | 州教育厅数据门户、NCES / IPEDS / CRDC、Zelma、Big Local News | ⚠️ 州门户"clunky"、各州不可比（E-05）。❌ 联邦数据被砍或延迟、变难读（E-03、E-04） |
| S3 找信源 | 教师、学生、家长、管理者、工会、倡导团体 | 学区 PIO（新闻发言人）、家长 Facebook 群、校董会公众评论 | ❌ 采访请求被统一转给 PIO（E-02）；进校园难，K-12 为 43%（E-01） |
| S4 采访/素材 | 校董会、市民大会、债券说明会 | 现场录音、会议视频 | ⚠️ 多人发言难以记录（E-11） |
| S5 核实 | 核对学区说法与数据 | 公共记录申请、州数据 | ⚠️ 对学区 PR 信任度只有 15%（E-01） |
| S6 写作/制作 | 解释考试、预算、政策；地区趋势稿 | — | 需要"解读数据、预算、立法与公共记录"的能力（E-12） |
| S7–S8 | 家长服务型内容、学校查询工具 | Chalkbeat、The Beam GPTs | INDIE 的创新点在这里（E-08） |
| S9 职业/生存 | 综合报纸教育线缩编；教育专门媒体也在裁 | — | 综合报纸 39% 缩编、12% 扩编（E-01）；Chalkbeat 2025 年裁 3 人（E-10） |

---

## 2. 政治 / 州与联邦政府 / 选举 条目

### P-01 | LOCAL / NATL | S1 / S9 | 州政府 | 市场数据（2022）
- **结论**：州议会记者总数上升，但报纸岗位萎缩，非营利机构填补了空缺，而且只有约一半是全职。
- **证据**：Pew 2022 年普查（2014 年后的更新）：报纸的州议会记者从 604 人（占 38%）降到 448 人（26%）；非营利机构从 92 人（6%）升到 353 人（20%）；目录标题写"About half of statehouse reporters cover statehouse legislative sessions full time"（约一半全职跑议会会期）。方法是普查加 24 个定性访谈。
- **来源**：Total Number of U.S. Statehouse Reporters Rises, but Fewer Are on the Beat Full Time — https://www.pewresearch.org/journalism/2022/04/05/total-number-of-u-s-statehouse-reporters-rises-but-fewer-are-on-the-beat-full-time/ — Pew / 2022-04-05 — ✅（2022 年数据。Poynter 2026-10 写道"It is unclear how many statehouse reporters there are now"，即没有更新的普查）

### P-02 | LOCAL | S1 / S3 | 州政府 | 需求信号（记者原话）
- **结论**：2026 年州议会"记者团"继续收缩。AP 关闭了伊利诺伊州议会站，堪萨斯以前一场听证会有 6 名以上记者，现在可能只有 1 名。少了同行，追问官员也变难了。
- **证据**：AP 在 2026 年春天结束了伊利诺伊州议会的常驻报道，改为依赖合作方报道日常立法。州议会广播记者 Dave Dahl 说 "you can't really do it unless you're here a lot"（不常驻就做不了）。Kansas Reflector 主编 Sherman Smith 回忆，过去重大法案听证至少有 6 名记者，现在可能只剩他一人，"And we don't have that really anymore"（现在已经没有那种阵容了）。他还说，过去有时候是"we have to get an explanation out of this person"（大家一起逼官员给出解释）。
- **来源**：AP's Springfield closure reflects national decline in statehouse journalism — https://dailyegyptian.com/124644/showcase/aps-springfield-closure-reflects-national-decline-in-statehouse-journalism/ — Daily Egyptian / Gateway Journalism Review / 2026-07-22 — ✅；A shrinking local press is making it easier for public officials… — https://www.poynter.org/reporting-editing/2026/local-news-press-access-public-officials/ — Poynter / 2026-10-15 — ✅

### P-03 | INDIE | S3 / S4 / S9 | 州政府 | 需求信号（行为：诉讼）
- **结论**：独立/个人记者跑州议会面临"资格门槛"：拿不到记者证，被关在简报会外，只能靠起诉解决。
- **证据**：爱荷华州独立记者 Laura Belin 起诉后才拿到众议院记者证（2024-01）；2026-01-13，州长新闻秘书在预算简报会上对她关门，而其他州议会记者都在场。犹他州独立记者 Bryan Schott 被拒发记者证并起诉（2025-01），2026 年的申请又被拒。他的原话是 "It has made my job significantly harder"（这让我的工作难了很多）。堪萨斯众议院议长在 2025-01 把记者赶出议事厅的工作区。
- **来源**：同 P-02 的 Poynter 2026-10-15 — ✅

### P-04 | LOCAL / NATL | S2 / S4 | 州政府 | 需求信号（调查，小样本）
- **结论**：跑州政府的记者把"拿不到记录和人"列为最大障碍，而且多数遇到过被排除在简报会外。
- **证据**：Collier Prize（佛罗里达大学）2025 年首次调查，n=51，受访者来自大型州级或区域媒体，主办方自称"beta"：约 2/3 本人或同事被官员排除在简报会外（29% 多次遭遇）；55% 认为通过 FOIA 拿记录困难；69% 认为最大挑战是拿不到记录或接触不到人。主办方 Rick Hirsch 说，新闻机构 "don't necessarily have the resources they once did"（没有以前的资源）去打官司。
- **来源**：Survey: Statehouse reporters face growing pushback and shrinking resources — https://www.editorandpublisher.com/stories/survey-statehouse-reporters-face-growing-pushback-and-shrinking-resources,256500 — E&P / 2025-07-10 — ✅（样本小；01 文件记录过同一调查的 Poynter 版本）

### P-05 | FREE | S9 / S1 | 州政府 | 市场数据 + 行为
- **结论**：学生记者在制度化地补州议会报道的缺口。他们偏重调查和深度，不做日常快讯。
- **证据**：Center for Community News 2025 年数据：30 个州的 35 所大学有州议会报道项目，其中 11 个是 2023 年后新设或即将启动的；Pew 研究发现近 10% 的州议会记者是学生。佛罗里达项目负责人 Ted Bridis 说 "We can never fill the need of an AP or a wire service, but we can augment it"（我们永远替代不了 AP，但能补充）。
- **来源**：As statehouse coverage shrinks, student journalists are stepping in — https://www.poynter.org/reporting-editing/2026/student-journalists-statehouse-reporting-local-news-gap/ — Poynter / SPLC Student Press Report / 2026-04-20 — ✅

### P-06 | LOCAL / INDIE | S2 / S1 | 立法 | 凑合方案（记者自述工作流）
- **结论**：跑一个州法案，靠的是"州议会网站寻宝 + 免费 LegiScan 交叉核对 + 搜索示范法案 + 打电话问议会办公室"，工具零散，全靠手工。
- **证据**：States Newsroom 记者 Kelcie Moseley-Morris 给出的步骤：先用大致日期缩小会期；州网站找法案 "a bit of a treasure hunt"（像寻宝）；确认是哪个版本、最近有没有更新；到免费的 LegiScan 交叉核对阶段和共同提案人；搜索相同措辞，找其他州的先例和 ALEC 示范法案；跟踪委员会、表决和另一院的进程；看听证直播；采访提案人和两方倡导者。她指出的痛点包括：各州网站从简单到晦涩差别很大；同一会期常有相似法案；其他媒体很少写明法案编号或提案人。
- **来源**：How to Report on a State Bill — https://yourfirstbyline.substack.com/p/how-to-report-on-a-state-bill — Ryan Teague Beckwith（Your First Byline）/ 2025-01-17 — ✅
- **判定**：⚠️ 单个法案能自己搞定；同时盯几十上百个法案则缺少面向记者的工具（价格见 P-07）。

### P-07 | NATL（游说方为主） | S1 / S2 | 立法 | 竞品事实（供给）
- **结论**：商业立法追踪工具卖给政府事务团队。带 AI 摘要的档位每年 5,000 美元，没有记者价。
- **证据**：Plural 定价页：Essential 每席位每年 609 美元（或每月 59 美元），可无限追踪国会、50 州、DC、波多黎各的法案，但"No AI summaries or analysis"（无 AI 摘要）；Professional 每年 5,000 美元，含 AI 摘要、版本对比、听证议程和立法幕僚联系人；Enterprise 定制价。05 文件记录：Plural 于 2025-12 被 SAI360 收购，Open States 大部分工具已停用；Quorum 中位数约每年 2.35 万美元（Vendr 数据）。LegiScan 有免费公共服务和按州数计价的年费订阅，价格页被 Cloudflare 拦截，具体价格未核实。
- **来源**：Pricing | Plural — https://pluralpolicy.com/pricing/ — 访问于 2026-11-03 — ✅；LegiScan Price List — https://legiscan.com/pricing — [未核实]；05_competitors_discovery_research.md（C 段 Plural / Quorum）

### P-08 | LOCAL / INDIE | S1 / S2 | 立法 + 竞选财务 | 竞品事实 + 需求信号（JD 与使用行为）
- **结论**：CalMatters 的 Digital Democracy 是这个条线最接近"记者专用 AI 线索工具"的东西：把听证发言、捐款、表决汇进一个库，AI 生成"Tip Sheets"推给记者。它已经出现在 JD 里，成了岗位要求。
- **证据**：Digital Democracy 记录"every word spoken in public hearings, every dollar donated… every vote cast"（听证会上的每句话、每笔捐款、每次表决）。AI Tip Sheets 实时从听证和表决中找报道点子，只给注册记者用。一位获艾美奖的记者称之为 "a reporter in every room"（每个房间都有一个记者）。目前覆盖加州，并已和 Honolulu Civil Beat 合作扩展到夏威夷。Reid Hoffman 与 Lever for Change 每年出资 180 万美元、连续 5 年，用于推广到更多州。公众免费使用。**JD 证据**：Civil Beat 招聘"Hawaiʻi State Government Reporter"（年薪 75,000–95,000 美元，2026-10-29），要求"master our new Digital Democracy tool to land scoops"（熟练使用 Digital Democracy 抢独家），岗位还包括培训同事和外部团体，以及"obtaining state data sets to make the tool more robust"（获取州数据集来增强工具）。
- **来源**：Digital Democracy, by CalMatters, wins The Trust in American Institutions Challenge — https://calmatters.org/inside-the-newsroom/2026/04/trust-challenge-win/ — CalMatters / 2026-04-14 — ✅；Home - Digital Democracy — https://calmatters.digitaldemocracy.org/ — ✅（搜索结果与首页一致）；Hawaiʻi State Government Reporter — https://www.journalismjobs.com/1694205-hawaii-state-government-reporter-honolulu-civil-beat — ✅（项目原始数据）
- **判定**：在加州和夏威夷，S1 已有免费 AI 方案；其他 48 个州没有。资金来自慈善，没有记者付费。

### P-09 | NATL / LOCAL | S2 | 竞选财务 + 国会 | 竞品事实（近 2 年变化）
- **结论**：过去两年，"金钱与政治"的免费数据聚合层明显流失：OpenSecrets 关闭 API，ProPublica Congress API 下线，FollowTheMoney 停止维护。
- **证据**：OpenSecrets API 页："As of April 15, 2025, our API offerings have been discontinued"（自 2025-04-15 起停止 API 服务），需要数据的人联系 commercial@opensecrets.org 谈定制方案（即转为付费）。ProPublica："ProPublica's Congress API is no longer available"（已不可用），文档仅作历史参考；GitHub 公告建议迁到 Congress.gov API。FollowTheMoney.org（州级竞选财务，已与 OpenSecrets 合并）首页："data that is current through the 2024 election year… the site isn't maintained"（数据只到 2024 选举年，网站不再维护）。OpenSecrets 2026-10 发布了"统一州与联邦数据的看板"，页面被 Cloudflare 拦截，[未核实]。官方替代品 Congress.gov API 免费，通过 api.data.gov 申请 key。
- **来源**：OpenSecrets API — https://www.opensecrets.org/api/admin/index?function=signup — 访问于 2026-11-03（curl 抽取）— ✅；ProPublica Congress API — https://projects.propublica.org/api-docs/congress-api/ — ✅；DataStore for getting API key is down · Issue #284 — https://github.com/propublica/congress-api-docs/issues/284 — ⚠️（只看了搜索摘要）；FollowTheMoney.org — https://www.followthemoney.org/ — ✅；Congress.gov API — https://api.congress.gov/ — ✅（页面可达，细节来自搜索摘要）
- **判定**：⚠️ 联邦数据仍可从 FEC.gov 和 Congress.gov 直接取，但"跨州、跨联邦、按人归并"的清洗工作又落回记者身上。

### P-10 | NATL | S1 / S2 | 竞选财务 | 竞品事实（制度变化）
- **结论**：FEC 自 2025-05-01 失去法定人数，2025-10 起基本停摆。记者失去了"执法行动 → 报道线索"这条来源，申报审查也停了。
- **证据**：Public Citizen（2026-09-02）：FEC 因少于 4 名委员，2025-10 关门；停摆通知写"Virtually all core agency functions (will cease)"（几乎所有核心职能停止），包括申报审查、咨询意见、规则制定；搁置的执法案件一年内从 154 件翻倍到 307 件。FEC 自己的声明（2026-05）称合规团队仍在审查报告，两方说法不一致。申报数据能否继续及时公开，本轮未核实。
- **来源**：FEC Shutdown Nears One-Year Mark With No Quorum — https://www.citizen.org/news/fec-shutdown-nears-one-year-mark-with-no-quorum-no-consequences/ — Public Citizen / 2026-09-02 — ✅；Statement on One Year Without Quorum — https://www.fec.gov/resources/cms-content/documents/Statement_on_One_Year_Without_Quorum.pdf — ⚠️（只看了搜索摘要）

### P-11 | LOCAL | S2 | 竞选财务（地方） | 需求信号 + 凑合方案
- **结论**：地方候选人和 PAC 的财务申报常是扫描 PDF，记者只能手工转录或到处找 OCR 工具。州级岗位明确要求"跟着钱走"。
- **证据**：Reddit r/Journalism（2023-05）一位地方记者手上有 5 年、约 50 页的候选人及关联 PAC 财务文件，全是栅格化 PDF："I do not want to transcribe if I can avoid it"（能不手抄就不手抄），在找 PDF 转表格工具。Mountain State Spotlight 州政府记者 JD（50,000–70,000 美元，2026-10）写："following the money, examining campaign spending and lobbying, testing politicians' statements against evidence"（跟着钱走，审视竞选开支和游说，用证据检验政客言论）。
- **来源**：Reccomend a tool: convert pdf to a spreadsheet — https://www.reddit.com/r/Journalism/comments/1370yuq/ — 2023-05-03 — ✅（项目原始数据）；State Government Reporter, Mountain State Spotlight — https://www.journalismjobs.com/1693944-state-government-reporter-mountain-state-spotlight — ✅（项目原始数据）
- **判定**：❌ 地方一级（县、市、学区）的竞选财务没有聚合层，格式最差。

### P-12 | LOCAL / INDIE | S6 / S7 | 选举结果 | 需求信号 + 凑合方案（失败案例）
- **结论**：下沉选举（县、市、学区）的结果没有现成服务。小媒体要么在选举夜手工复制粘贴，要么自建爬虫。各县系统五花八门，AI 辅助的实时抓取在选举夜失败了。
- **证据**：Bay City News（覆盖加州 13 个县）写道，选举季需要 "methodically copying and pasting candidate names and results from dozens of county, city and school board races"（把几十个县、市、学区选举的候选人和结果一条条复制粘贴），而这类结果"not provided by AP, Ballotpedia or other large services"（AP、Ballotpedia 等大服务都不提供）。选前用 AI 抓取候选人信息成功了。选举夜的实时抓取，代码"kept breaking"（不断崩溃），原因包括：各县更新频率从 10 分钟到 1 小时不等；有的县一场选举一个标签页；候选人按票数换位；部分县用 Clarity Elections，其余是一次性自建系统；"zero ballots"（空白结果模板）有的县选举夜 8 点才给，Mendocino 和 Napa 到投票结束都没给。2026 年的复盘还记下：ChatGPT 一次只能处理约 50 名候选人，Claude 长任务常超时；搭模板用了约 18 条提示词，排错又用了 25 条，排错花了约一周；付费聊天机器人每月 20 美元。结论原话："Using an AI tool to track live results proved too complicated"（用 AI 追踪实时结果太复杂了）。
- **来源**：Election night mayhem with an AI twist — https://rjionline.org/news/election-night-mayhem-with-an-ai-twist/ — RJI / Bay City News / 2025-01-22 — ✅；A Playbook for Newsrooms: Revolutionizing Election Coverage with AI — https://localnewsmatters.org/2026/04/23/a-playbook-for-newsrooms-revolutionizing-election-coverage-with-ai/ — Local News Matters / 2026-04-23 — ✅；Reddit 转帖（引原文）— https://www.reddit.com/r/Journalism/comments/1svc7ur/ — 2026-04-25 — ✅（项目原始数据）
- **对照**：NYT 选举分析岗 JD 写，其系统背后有 "hundreds of scrapers collecting precinct data"（数百个抓取选区数据的爬虫）。大媒体自建，小媒体建不起（见 P-17）。
- **判定**：❌ 不好自己解决：每次选举格式都变，而且必须在选举夜那几个小时内跑通。

### P-13 | LOCAL / INDIE / TV | S6 / S7 | 选举结果 | 竞品事实 + 需求信号（使用方原话）
- **结论**：小媒体的选举结果、选民指南和专家支持，主要靠基金会补贴的"包"获得。付费方是慈善，不是媒体。
- **证据**：AP Fund for Journalism（2026-09-30）用 Google、Knight、Microsoft、Lilly 等的资金，向 200 家地方和州级媒体免费提供 AP 政治报道、计票、宣布胜选和州级地图图表，期限到 2026 年底。WXPR 新闻总监说用 AP 的东西可以"spend our time and resources on deepening our local reporting"（把时间花在深挖本地报道上）；The Beacon 说"much easier way than we'd be able to on our own"（比自己做容易得多）。Knight Election Hub（2024，现已结束）向 537 家媒体提供了价值超过 100 万美元的免费资源：44 家小媒体通过 DDHQ 或 Newspack 模板展示选举夜结果；25 家用 Newspack 插件做选民指南；OpenSecrets 提供竞选财务培训；Votebeat 的 Slack 专家台为 56 家媒体回答了 111 个问题。
- **来源**：AP Fund for Journalism expands election resources to 200 local newsrooms — https://www.ap.org/media-center/press-releases/2026/ap-fund-for-journalism-expands-election-resources-to-200-local-newsrooms-nationwide/ — AP / 2026-09-30 — ✅（curl 抽取）；Knight Election Hub — https://www.knightelectionhub.org/ — ✅
- **判定**：AP 的县级以上结果，通过补贴 ✅ 能拿到；AP 不覆盖的下沉选举仍是 ❌（P-12）。

### P-14 | LOCAL / NATL | S3 / S5 | 选举行政 | 竞品事实（免费服务）
- **结论**：选举行政（计票、诉讼、选举技术）专业性强，地方记者缺少能在截稿前找到的专家。Votebeat 用免费、可具名引用的专家台来补。
- **证据**：Votebeat Expert Desk（2026 中期选举）：100 多位两党专家（前选举官员、选举律师、技术专家），预计服务 150 家媒体的 600 名记者，用途是"check claims, understand lawsuits, find credible sources, pressure-test tips"（核实说法、理解诉讼、找可靠信源、检验线索）。编辑总监 Jessica Huseman 说它适用于记者"need a source, a gut check, or an answer to a technical question on deadline"（截稿前需要信源、需要把关、需要技术答案）的时候。资金来自 More Perfect。03 文件的 L-26 记录：选举官员"not used to working with the media"（不习惯和媒体打交道）。
- **来源**：Votebeat Launches Expert Desk with Support from More Perfect — https://www.prnewswire.com/news-releases/votebeat-launches-expert-desk-with-support-from-more-perfect-302878059.html — PR Newswire / 2026-09-15 — ✅；electionline Weekly 2024-04-11（见 03 L-26）— ✅

### P-15 | LOCAL / TV | S1 / S4 | 选举 | 需求信号（行业观察）+ 竞品事实
- **结论**：2026 中期选举的突出问题是"没人去报"：有的国会选区完全没有竞选报道，一个记者要跑好几场选举。C-SPAN 开始向地方媒体免费提供候选人活动视频。
- **证据**：雪城大学 Joel Kaplan（2026-10-06）："there are entire Congressional districts that are not receiving any coverage of the campaigns"（有整个国会选区完全没有竞选报道）。C-SPAN"Road to the Capitol"在 10 个州派记者和摄影师，拍候选人的市民大会、论坛和活动，把完整视频免费提供给非营利地方媒体和独立媒体，资金来自 Carnegie、Knight、MacArthur 和 More Perfect。CEO Sam Feist："Local political journalism is shrinking at exactly the moment voters need it most"（地方政治新闻恰恰在选民最需要时萎缩）。
- **来源**：Why Midterm Coverage Faces a Bigger Problem Than How It's Reported — https://news.syr.edu/2026/10/06/why-midterm-coverage-faces-a-bigger-problem-than-how-its-reported/ — Syracuse / 2026-10-06 — ✅；C-SPAN to assist local newsrooms… — https://thedesk.net/2026/06/cspan-midterm-election-news-partnership/ — The Desk / 2026-06 — ✅

### P-16 | NATL | S6 / S8 | 政治（政策情报） | 需求信号（行为：工会仲裁）
- **结论**：政治条线里最显眼的 AI 产品化尝试，被记者通过工会叫停了。不经编辑审核的 AI 政策报告和实时摘要，被认定违反合同，并且错误百出。
- **证据**：Politico 的 Capitol AI Report-Builder 给 Politico Pro 订户生成 500 字政策报告，带标题和对记者署名稿的引用，没有编辑审核，含"glaring errors"（明显错误）。Live Summaries 对 2024 年民主党全国代表大会和副总统辩论生成未经编辑的实时摘要。2025-11-26 仲裁裁定两者违反 PEN Guild 合同（没有 60 天通知、没有谈判、没有人工监督），仲裁员写道 AI "cannot yet rival the hallmarks of human output"（还比不上人工产出的水准）。2026-05-22 Politico 同意关闭这两个工具。
- **来源**：VICTORY: POLITICO agrees to shut down both AI tools — https://www.pen-guild.org/news/victory-politico-agrees-to-shut-down-both-ai-tools-at-center-of-landmark-arbitration — PEN Guild / 2026-05-22 — ✅

### P-17 | NATL | S2 / S6 | 选举数据 | 需求信号（JD）
- **结论**：全国大媒体把选举数据当成基础设施自建（选民档案、人口数据、数百个选区爬虫、清洗管道），地方媒体没有这种能力。
- **证据**：NYT Election Analytics 招聘选举数据开发者（2026-06）："the voter file… hundreds of scrapers collecting precinct data and countless pipelines for processing and cleaning data"（选民档案、数百个抓取选区数据的爬虫和无数清洗管道）。另有志愿项目 OpenElections（2012 年起，Derek Willis 维护）在做标准化的选区级认证结果。
- **来源**：Graphics/Multimedia Editor, Elections Data Developer — https://job-boards.greenhouse.io/thenewyorktimes/jobs/4706625005 — NYT / 2026-06-18 — ✅（项目原始数据）；OpenElections — https://openelections.net/ — ⚠️（只看了搜索摘要）

### P-18 | LOCAL / TV | S4 / S5 / S9 | 选举（地方） | 需求信号（Reddit 原话）
- **结论**：地方选举报道的日常摩擦包括：党组织会议不让录音、选举季线索真假难辨、候选人提供 AI 生成头像，TV 编辑台在选举季承受观众辱骂。
- **证据**：①（2025-01）一名记者到县党中央委员会公开会议报道，委员们说"passed a law"（通过了规定）禁止录音录像，还叫了警察；记者不确定开放会议法是否适用。②（2025-10）小城选举两派对立，"I'm getting constant tips and info about candidates and potential wrongdoings"（不断收到关于候选人和可能不当行为的线索），只能逐条核实。③（2025-09）市长候选人提供的头像带 Gemini 水印，记者用 AI 检测器判断。④（2024-10）本地 TV 编辑台人员说 "I end up getting cussed out and berated"（最后被骂得狗血淋头）。
- **来源**：https://www.reddit.com/r/Journalism/comments/1i73x45/ ；https://www.reddit.com/r/Journalism/comments/1odij0s/ ；https://www.reddit.com/r/Journalism/comments/1npxm5w/ ；https://www.reddit.com/r/Journalism/comments/1gfcqq5/ — ✅（项目原始数据）

### P-19 | LOCAL / NATL | S1 | 政治 | 需求信号（Reddit 原话 + 自建工具）
- **结论**：记者要的不是更多提醒，而是"只推和我在跑的东西相关的"。已有记者或开发者自建过滤工具。
- **证据**：（2025-08）CivicTracker 的作者跟踪总统和国会议员的发言与删帖，原话 "I didn't want notifications for everything he says, just the stuff that actually matters for what I'm working on"（我不要他说的每句话都推送，只要和我手上工作相关的）。（2024-12）有人想搜政治人物推特历史里是否提过某个话题。（2024-10）开发者问记者用什么工具追踪政客承诺，回答只提到了 factcheck.org。
- **来源**：https://www.reddit.com/r/Journalism/comments/1mjos6n/ ；https://www.reddit.com/r/Journalism/comments/1hi5o5s/ ；https://www.reddit.com/r/Journalism/comments/1gae6zd/ — ✅（项目原始数据）

### P-20 | LOCAL / NATL | S1–S6 | 州政治 | 需求信号（JD 工作描述）
- **结论**：2026 年州政治岗位的 JD 描述了三种干法：日常快讯加周末深度（Oregonian）；不追每场记者会、要"翻译"预算和法案（Mountain State Spotlight）；常驻议会给业内人士供稿（State Affairs）。共同点是公共记录和跟钱。
- **证据**：Oregonian 州政府与政治记者（60,000–85,000 美元）要"break daily news… while also preparing frequent weekend takeouts"（日常抢快讯，同时常做周末深度），要求有用公共记录做问责的记录。Mountain State Spotlight 要求"translating budgets, bills, regulations and court decisions into what they mean for a family"（把预算、法案、法规、判决翻译成对一个家庭的意义），并且"resisting the urge to treat every press conference… as a story"（不把每场记者会都当新闻）。State Affairs 资深州议会记者（58,000–72,000 美元，亚利桑那）大多数日子在州议会办公，雇主自称结合"AI-native tools"（AI 原生工具）和州政府数据。
- **来源**：https://www.journalismjobs.com/1694158-state-government--politics-reporter-advance-local ；https://www.journalismjobs.com/1693944-state-government-reporter-mountain-state-spotlight ；https://www.journalismjobs.com/1693536-senior-statehouse-reporter-arizona-state-affairs — 2026-10 — ✅（项目原始数据）

---

## 3. 教育（K-12 与高教）条目

### E-01 | LOCAL / NATL | S2 / S3 / S5 / S9 | 教育 | 需求信号（EWA 调查，2020 年数据）
- **结论**：教育记者最常用的信息来源是公关，但他们最不信任的也是公关。"高依赖、低信任"是这个条线的核心矛盾。资源不足和接触信源难排在挑战的前两位。
- **证据**：EWA《State of the Education Beat 2021》，n=419，调查于 2020 年 3–6 月进行，另有 24 人电话访谈。
  - **过去一个月使用过一次以上的信源**：教育机构公关人员 81%（最高）、教育研究 76%、公共数据库与记录检索 70%、学生 70%、K-12 学校或学区管理者 69%、K-12 教师 67%、非营利组织公关 66%、家长 65%、高校教师 62%、地方或州校董会 59%、智库与倡导团体 56%、州教育官员 53%、实地走访校园 52%、州或联邦议员 49%、公关公司 29%、教育企业 25%。合计 89% 用过某类公关信源。
  - **对"及时准确提供 K-12 信息"有"很大或较大"信心的比例**：教师 73%、学生 68%、家长 55%、K-12 管理者 45%、州教育厅 35%、教师工会 31%、校董会成员 30%、州议员和州长 19%、公关人员 15%、美国教育部 14%。
  - **最大挑战（开放题编码）**：资金与资源 27%、接触信源 25%、可靠信息获取 13%、难以做深度 12%、编辑不支持 11%、一人兼多条线 5%。
  - **其他**：39% 进校园有困难（K-12 43%，高教 28%）；认为教育官员不合作或敌对的比例从 23% 升到 34%（州和地方 39%，全国 21%）；61% 被受众或信源威胁骚扰过；综合性报纸教育组 39% 缩编、12% 扩编，教育专门媒体 41% 扩编。访谈原话："the only P-12 education reporter on our staff is me"（编辑部里唯一的 K-12 记者就是我），8 年前同一家报社有 5 人。另一受访者说，因为资源不足，常把找公关当"shortcut"（捷径）。
- **来源**：State of the Education Beat 2021（PDF）— https://ewa.org/wp-content/uploads/2022/01/ewa_ed_beat_report_2021_1.25.21_0.pdf — EWA / 2021-01 — ✅（下载后用 pypdf 全文检索）；报告索引页 — https://ewa.org/members-news/state-of-the-ed-beat-report — ✅（页面只有 2016 和 2021 两版，没有更新的版本）
- **注意**：数据是 2020 年的，比本轮"2023–2026 优先"的要求老，但仍是教育记者唯一的大样本行业调查。

### E-02 | LOCAL | S3 | 教育 | 需求信号（Reddit 原话）
- **结论**：学校和大学把所有采访请求统一转给媒体联络人，拖慢截稿；记者又不能得罪公关。编辑给的建议只有"照做"。
- **证据**：（2023-10）年轻教育记者说，约一半的教师、教授、管理者采访请求被直接转给媒体联络人，"I can't afford to waste my time waiting for one person to approve and coordinate multiple interview requests on a deadline"（截稿前等一个人审批协调多个采访，我耗不起）。编辑的建议是照常做，"expect the PR folks to yell at me"（等着被公关吼）。另一例（2023-11）：联系 Moms for Liberty 地方分会做采访，邮件加 Facebook 都没有回音。
- **来源**：https://www.reddit.com/r/Journalism/comments/17gcib8/ ；https://www.reddit.com/r/Journalism/comments/187p1ha/ — ✅（项目原始数据）
- **判定**：❌ 制度性门槛，靠工具难解决，只能靠人脉和"绕过 PIO"直接找教师、家长和学生。

### E-03 | NATL / LOCAL | S2 | 教育（联邦数据） | 竞品事实（近 2 年变化）
- **结论**：2025 年联邦教育统计被大幅削减。一年后只部分恢复，14 项数据产品被取消，法定报告首次延误。教育记者的背景数据底座变窄了。
- **证据**：EWA（2025-02-19）：IES 约 9 亿美元合同被取消，Regional Educational Laboratories 约 3.36 亿美元被取消，NAEP 一项长期追踪测试被取消；College Scorecard 未受影响。Pell Institute（2026-08-25）："one year later"：NCES 裁员后重新招回"about a dozen"（约十来名）员工；IPEDS 继续发布但质量受质疑；Digest of Education Statistics 刚开始发布 2023-24 表格；被取消的产品包括 College Navigator、Beginning Postsecondary Students、National Household Education Survey、Projections of Education Statistics、州纵向数据系统拨款等 14 项；Condition of Education 首次错过法定交付日期。K-12 Dive 和 Inside Higher Ed（2025-03）报道"almost all of the NCES staff"（几乎全部 NCES 员工）在裁员中被裁。
- **来源**：Tips for Safeguarding Data as Federal Databases Disappear — https://ewa.org/educated-reporter/how-to-safeguard-data-as-federal-databases-disappear — EWA / 2025-02-19 — ✅；NCES One Year Later — https://www.pellinstitute.org/news-impact/blog/nces-one-year-later-whats-back-whats-missing-and-what-comes-next/ — Pell Institute / 2026-08-25 — ✅；What will NCES layoffs mean for the Nation's Report Card? — https://www.k12dive.com/news/Education-Department-nces-layoffs-leaves-naep-assessments-nations-report-card-barebones/742837/ — ⚠️（只看了搜索摘要）

### E-04 | LOCAL / NATL | S2 | 教育（民权数据） | 竞品事实 + 研究者原话
- **结论**：联邦民权数据（CRDC）还在，但发布晚了约半年，并且取消了面向公众的"First Look"摘要，只剩原始文件。地方记者要用，就得自己写代码处理。
- **证据**：2023-24 年 CRDC 于 2026-09 初悄悄发布，比教育部自定的 2025 年底期限晚约 6 个月；OCR（民权办公室）人员减半。这次"no First Look Report — the raw data files are the primary sources"（没有 First Look 报告，原始数据文件是主要来源）。前 OCR 负责人 Catherine Lhamon 说数据 "didn't make it usable for somebody's mom"（没有做到让普通家长能用）。俄勒冈大学研究者 Maithreyi Gopalan 说她跑的程序"literally hundreds of pages of code long"（真的有几百页代码长）。
- **来源**：Long-awaited civil rights data about students is finally out — https://www.npr.org/2026/09/04/nx-s1-5955681/civil-rights-data-schools-trump — NPR / 2026-09-04 — ✅（curl 抽取）
- **判定**：❌ 对没有数据记者的 LOCAL 来说，从"开箱可用"变成了"要写代码"。

### E-05 | LOCAL / INDIE / NATL | S2 | 教育（考试数据） | 竞品事实 + 凑合方案
- **结论**：州考试数据分散在 50 个格式各异、"clunky"的州门户里，跨州不可比，有些年份缺失。Zelma 和 Education Data Center 用 AI 加清洗后的统一库免费解决了一部分问题。
- **证据**：The 74（2023-12-06）：州数据门户"a little bit clunky"（有点笨重），下拉菜单一次只能看一个指标；明尼苏达的数据能追到 1990 年代末，罗德岛 2018 年前没有；2020 和 2021 年几乎没有数据；各州考试不同，Emily Oster 说这些数据"just not well suited"（根本不适合）回答"密西西比是否胜过密歇根"这类问题；政策制定者常常要走繁琐的申请流程。Education Data Center（2026 年访问）：3–8 年级、50 州加 DC 的统一库，Zelma 用自然语言出图，"Free for researchers, journalists, parents"（对研究者、记者、家长免费），资金来自 Walton、Overdeck、Gates、Dell 等基金会。NPF 讲座（2025-04-07）也向记者推荐 Zelma、PNPI 和 Data Rescue Project。
- **来源**：Exclusive: Free New AI Tool… — https://www.the74million.org/article/exclusive-ai-tool-promises-to-make-test-data-a-lot-more-accessible-to-a-lot-more-people/ — The 74 / 2023-12-06 — ✅；zelma - Education Data Center — https://www.eddatacenter.org/ — ✅；Keeping Track of Education Data — https://nationalpress.org/topic/keeping-track-of-education-data-resources-for-journalists-amid-ed-department-dismantling/ — NPF / 2025-04 — ✅
- **判定**：⚠️→✅ 3–8 年级考试数据已有免费方案；高中、财务、人事等其他数据仍要逐州找。

### E-06 | LOCAL | S1 / S3 | 教育（校董会） | 需求信号（使用行为）+ 竞品事实
- **结论**：教育条线是会议 AI 工具最早落地的条线。Chalkbeat 先自建，因为改提示词要工程师介入而放弃，转买 LocalLens 监测约 80 个学区。记者把它当"线索"和"找信源"的工具，不当作报道替代品。
- **证据**：Chalkbeat 的 Eric Gorski 说 "We just didn't have that technical expertise on staff"（我们编辑部没有这种技术能力）；工具产出 "It is a tip… you need to check it out"（只是线索，要去核实）。记者 Hannah Dellinger 错过一场校董会，通过关键词检索找到了一名讲述被霸凌经历的学生信源，"I don't know that I would have found him if I wasn't using this tool"（不用这个工具，我可能找不到他）。问题：一场会有 6 名以上董事，说话人识别差；摘要粗糙，所有引语都要人工核对。05 文件记录：LocalLens 于 2025-11 被 American Public Media 收购。
- **来源**：Local newsrooms are using AI to listen in on public meetings — https://www.niemanlab.org/2025/03/local-newsrooms-are-using-ai-to-listen-in-on-public-meetings/ — Nieman Lab / 2025-03 — ✅

### E-07 | LOCAL | S1 / S3 | 教育（校董会） | 竞品事实（2026 新进入者）
- **结论**：AP 在 2026 年推出 School Board Search，用 YouTube 转写覆盖 49 州 3,000 多个学区，免费给 AP 会员和受资助的地方媒体用。会议检索开始变成"通讯社基础设施"。
- **证据**：AP 教育数据记者 Sharon Lurye 与研究校董会治理的学者合作开发，"searches YouTube transcripts of school board meetings for more than 3,000 districts in 49 states"（检索 49 州 3,000 多个学区校董会的 YouTube 转写），附每场会的 AI 摘要，转写可跳到视频对应时间点核实，用来"identify trends and find people who might be willing to speak on the record"（发现趋势，找愿意具名受访的人）。首批 30 多家媒体来自 AP 会员、APFJ 和 Education Reporting Network；24 名记者参加了发布演示，90 人已注册；计划扩展到整个 APFJ 项目。
- **来源**：AP School Board Search launches to transform local coverage of thousands of school boards — https://www.ap.org/news-highlights/best-of-the-week/second-winner/2026/ap-school-board-search-launches-to-transform-local-coverage-of-thousands-of-school-boards/ — AP / 2026-08-21 — ✅（curl 抽取）
- **判定**：对 AP 会员和受资助媒体是 ✅；但只覆盖会把录像发到 YouTube 的学区（见 E-08）。

### E-08 | INDIE / FREE | S1 / S2 / S7 | 教育（校董会） | 需求信号（调查报道）+ 竞品事实
- **结论**：基于视频的工具有结构性盲区：亚利桑那一半以上学区不录像，或者不把录像放到公网，3 个学区录了又提前删除。The Beam（专业记者带学生）用 Custom GPT 给家长做校董会问答，并做了逐条核验。
- **证据**：The Beam 联系了全部 208 个学区（188 个确认了做法）：一半以上不录像或不公开；约三分之一完全不录像；3 个学区承认在法定保存期前删除录像；Vail 学区 YouTube 直播后删除。The Beam 为 8 个学区各建一个 Custom GPT，基于各学区最近的 YouTube 录像转写；48 小时内就有家长要求加入自己的学区，计划覆盖全部 74 个在 YouTube 发布会议录像的学区。学生核验后"found no invented quotes"（没有发现编造的引语），但问"最近一次会议"时，机器人有时会答成更早的会议。
- **来源**：Record, delete: Arizona's school board transparency patchwork — https://thebeam.org/arizona-school-boards-delete-recordings/ — The Beam / 2026-05-31 — ✅；Shelby Grossman is making school board meetings searchable with custom GPTs — https://academy.openai.com/public/blogs/shelby-grossman-custom-gpts-school-board-meetings — OpenAI Academy / 2026-06-30 — ✅（厂商宣传页，作为行为事实使用）
- **判定**：❌ 没有录像的会议，只能靠人到场或申请公共记录。

### E-09 | LOCAL | S1 | 教育 | 市场数据（报道覆盖度）
- **结论**：记者稀少的县，本地教育新闻几乎为零。
- **证据**：Local Journalist Index 2026 分析了 2026 年 1–3 月的 420 万篇文章：3,144 个县中约 2,500 个县没有任何涉及本地地名的健康、教育、环境或交通报道；每 10 万人不足 5 名本地记者的县中，90% 没有一篇本地教育报道，犯罪报道的占比反而更高。共同作者 Matt Baker 提到"tracking what's going on with the local county board of education"（关注本县教育委员会动向）这类需求没人满足。
- **来源**：What we can learn from the 2026 Local Journalist Index — https://www.pressclubinstitute.org/2026/07/09/local-journalist-index-muck-rack-rebuild-local-news/ — NPC Journalism Institute / 2026-07-09 — ✅

### E-10 | LOCAL / NATL | S9 | 教育 | 市场数据（人员变化，弱证据）
- **结论**：教育专门媒体也开始收缩，地方报纸让教育记者兼做编辑。
- **证据**：Chalkbeat 2025 年秋裁了 3 人（一名分社社长、一名编辑、一名高层经理），理由是"preserve our reporting capacity"（保住报道力量）和节省成本；前 Chalkbeat 科罗拉多记者 4 月被裁后转做公关；Lexington Herald-Leader 的 Monica Kast 现在一半时间做编辑、一半时间跑全州教育。EWA 2021 的对照：教育专门媒体当时 41% 在扩编。
- **来源**：Shutdown worries, blue-state reluctance, & layoffs at Chalkbeat — https://alexanderrusso.substack.com/p/shutdown-worries-blue-state-reluctance — Alexander Russo / 2025-10-03 — ✅

### E-11 | LOCAL / FREE | S2 / S4 | 教育 | 需求信号 + 凑合方案（Reddit 原话）
- **结论**：教育记者的日常数据难题很具体：不知道该找什么数据；会场多人发言录不全；记录申请的文件被拆成上百个碎片。熟手的凑合方案是挖州教育厅的冷门免费数据。
- **证据**：①（2025-07）地方记者想写同一校园两所中学的资源与种族差距，"I need some guidance on what kinds of data to look for"（我不知道该找哪类数据）。②（2026-01）首次报道学区债券说明会，蓝牙夹麦覆盖不了所有发言者，只能用平板手记谁问了什么。③（2026-08）华盛顿州记录申请返回 zip，拆成 100 多个小文件。④（2026-08）申请校董会成员与副校长会面的录音，录音在对方律师手里。⑤（2026-10）公共记录研究者用华盛顿州教育厅 OSPI 的教师执照处分公告，加上 S-275 全州学校人事年表（姓名、学区、职位、薪资、证书号），比对 20 年的教职员不当行为案件，"This one source answered questions that would otherwise have taken a records request"（这一个来源就回答了原本要靠记录申请的问题）。
- **来源**：https://www.reddit.com/r/Journalism/comments/1mbrxl8/ ；https://www.reddit.com/r/Journalism/comments/1qpl93d/ ；https://www.reddit.com/r/foia/comments/1vuf5mb/ ；https://www.reddit.com/r/Journalism/comments/1w06i3b/ ；https://www.reddit.com/r/foia/comments/1xgyvep/ — ✅（项目原始数据）

### E-12 | LOCAL | S1 / S2 / S6 | 教育 | 需求信号（JD 工作描述）
- **结论**：2026 年大都市报的教育岗位从"跑一个学区"转向"跨多个郊区学区看趋势"，并明确要求解读数据、预算、立法和公共记录。
- **证据**：Houston Chronicle 区域教育记者（Hearst，2026-10-26）："focusing on the systems, policies and regional trends… rather than a traditional district-by-district beat"（关注系统、政策和区域趋势，而不是逐个学区跑），点名 Aldine、Cypress-Fairbanks、Katy、Spring 等学区；"Track enrollment trends, demographic shifts and student outcomes"（追踪入学、人口变化和学生成绩）；要求"comfortable interpreting data, budgets, legislation and public records"（能熟练解读数据、预算、立法和公共记录）。04 文件记录：U.S. News 教育主编 JD 要求"use AI tools to increase workflow efficiencies"（用 AI 工具提高效率）。
- **来源**：Regional Education Reporter — https://job-boards.greenhouse.io/hearst/jobs/4466274009 — Hearst / 2026-10-26 — ✅（项目原始数据）

### E-13 | NATL / LOCAL | S2 | 高教 | 竞品事实
- **结论**：高教数据只剩 IPEDS 这一条主线，纵向追踪研究被砍，College Navigator 被取消。高教记者做负担能力、毕业去向类报道的数据来源变少了。
- **证据**：Pell Institute 列出被取消的产品包括 College Navigator、Beginning Postsecondary Students Longitudinal Study、Postsecondary Education Transcript Collection、National Postsecondary Education Cooperative；IPEDS 继续发布，但研究者对质量持谨慎态度；NPSAS 2024 推迟到 2027 年冬天发布；Pell 自己的 2026 年报告因为缺少整理好的数据，不得不做额外分析或另找数据源。EWA（2025-02）：College Scorecard 未受影响。
- **来源**：同 E-03（Pell Institute 2026-08-25 ✅；EWA 2025-02-19 ✅）
- **局限**：本轮没有找到高教记者本人谈数据缺失的原话。

### E-14 | LOCAL | S1 / S2 | 教育 × 选举（校董会选举） | 竞品事实
- **结论**：校董会选举是教育和选举交叉的地带，大型聚合服务只覆盖大学区。
- **证据**：Ballotpedia 2025 年校董会选举分析覆盖 29 州 187 个学区（487.8 万学生）、546 个席位、990 名候选人；36% 的席位无人竞争，寻求连任者 84% 胜选。Bay City News 指出 AP 和 Ballotpedia 都不提供学区等下沉选举的结果（P-12）。
- **来源**：Ballotpedia publishes analysis of 2025 school board elections — https://news.ballotpedia.org/2026/02/02/ballotpedia-publishes-analysis-of-2025-school-board-elections/ — Ballotpedia News / 2026-02-02 — ✅

### E-15 | LOCAL / NATL | S2 | 教育 | 需求信号（协会资源被阅读的情况）+ 凑合方案
- **结论**：联邦数据下线后，EWA 给记者的方案全是"自己存档"类的凑合办法：Wayback Machine、网页变动提醒、Data Rescue Project、Big Local News。这篇在 2025 年 EWA 博客阅读量前十。
- **证据**：EWA 建议记录每个数据集的出处，下载时截图，把页面提交到 Internet Archive，保存配套文档；推荐 MuckRock 的免费网页变动提醒和 FOIA 工具；Wayback Machine 负责人说"If you see something, save something"（看到了就存下来）。EWA 2025 年"Top 10 Reporter Resources"中，这篇排第 2，是十篇里唯一讲数据获取的。
- **来源**：EWA 2025-02-19（同 E-03）— ✅；Education Writers Association: Top 10 Reporter Resources in 2025 — https://ewa.org/educated-reporter/education-writers-association-top-10-reporter-resources-in-2025 — EWA / 2025 — ✅（阅读量排名是间接的需求信号）

### E-16 | LOCAL / NATL | S3 / S8 | 教育 | 市场数据（PR 方视角，弱证据）
- **结论**：在 2025 年 EWA 年会上，PR 公司观察到记者普遍倦怠、预算紧、编辑部变小。PR 方的应对是"提供现成数据和人"，这又加深了 E-01 的"高依赖"。
- **证据**：FINN Partners 的复盘（2025-06-06）：记者谈到繁重的新闻周期、预算缩水和编辑部变小；PR 方的对策包括"Lean into data"（多给数据）、提供可直接用的材料、快速对接专家、提供进教室采访的机会。页面没有记者直接引语。
- **来源**：What We're Really Up Against: 9 Takeaways from the 2025 EWA National Seminar — https://www.finnpartners.com/news-insights/what-were-really-up-against-9-takeaways-from-the-2025-ewa-national-seminar/ — FINN Partners / 2025-06-06 — ✅（PR 方转述，不是记者原话）

### E-17 | LOCAL / NATL | S1 | 教育 | 竞品事实（历史协作模式）
- **结论**：跨州教育数据报道（如"消失的学生"）靠通讯社、大学和数据项目三方协作完成，单个地方记者做不了。
- **证据**：AP 数据记者 Sharon Lurye 与 Stanford Big Local News、Thomas Dee 合作，汇总 21 个州加 DC 的州级入学数据，估算约 24 万名学生下落不明；Big Local News 与 NYT、EdSource 分析了 7 万所学校的入学趋势。
- **来源**：Big Local News helps tracking students during the pandemic — https://biglocalnews.org/content/news/2023/02/09/tracking-students-during-covid.html — Big Local News / 2023-02-09 — ⚠️（只看了搜索摘要，没有打开全文）

---

## 4. 竞品 / 工具表（本条线专用）

| # | 工具 / 服务 | 解决什么 | 环节 | 主要群体 | 价格 / 付费方 | 状态（2026-11） | 来源 |
|---|---|---|---|---|---|---|---|
| 1 | **CalMatters Digital Democracy**（含 AI Tip Sheets） | 州议会听证转写、捐款、表决汇成一库，AI 推送报道线索 | S1/S2 | LOCAL/INDIE（加州、夏威夷） | 免费；Hoffman/Lever for Change 每年 180 万美元 × 5 年 | 活跃，向更多州扩展；已写进 JD | P-08 ✅ |
| 2 | **LegiScan** | 50 州加国会的法案检索、追踪、API | S1/S2 | LOCAL/INDIE/FREE（免费版） | 免费公共版加按州年费 | 活跃（价格未核实） | P-06 ✅ / 价格 [未核实] |
| 3 | **Plural**（原 Open States） | 法案追踪、提醒；AI 摘要在 5,000 美元档 | S1/S2 | 游说方为主 | 609 美元/年 → 5,000 美元/年 → 定制；无记者价 | 2025-12 被 SAI360 收购 | P-07 ✅ |
| 4 | **Quorum** | 政府事务全套 | S1/S2 | 游说方 | 中位数约 2.35 万美元/年 | 活跃 | 05 ✅ |
| 5 | **State Affairs** | 州议会新闻加政策情报平台，自称"AI-native" | S1/S8 | 业内订户 | 未公开 | 活跃，在招州议会记者 | P-20 ✅ |
| 6 | **Politico Pro / Capitol AI Report-Builder** | AI 生成政策报告 | S6/S8 | NATL 订户 | 订阅 | AI 工具经仲裁于 2026-05 关闭 | P-16 ✅ |
| 7 | **Congress.gov API** | 国会法案、议员、表决 | S2 | NATL/数据记者 | 免费（api.data.gov key） | 活跃，是 ProPublica API 的替代 | P-09 ✅ |
| 8 | **ProPublica Congress API** | 同上 | S2 | NATL | 免费 | **已下线** | P-09 ✅ |
| 9 | **OpenSecrets** | 联邦竞选财务、游说 | S2 | NATL/LOCAL | 网站免费；API 2025-04-15 停止，改为商业定制 | 活跃（2026-10 推出州+联邦看板 [未核实]） | P-09 ✅ |
| 10 | **FollowTheMoney.org** | 州级竞选财务 | S2 | LOCAL | 免费 | 数据止于 2024，**不再维护** | P-09 ✅ |
| 11 | **FEC.gov 数据** | 联邦申报原始数据 | S2 | NATL | 免费 | 机构失去法定人数，执法和审查停摆 | P-10 ✅ |
| 12 | **Big Local News CAL-ACCESS Watch** | 加州政治献金提醒 | S1 | LOCAL（加州） | 免费，基金会资助 | 活跃 | 04 A5-02 ✅ |
| 13 | **AP 选举结果 / APFJ** | 计票、宣布胜选、图表 | S6/S7 | LOCAL/INDIE/TV | AP 收费；APFJ 为 200 家媒体免费（基金会出钱） | 补贴至 2026 年底 | P-13 ✅ |
| 14 | **Decision Desk HQ** | 选举结果，自称覆盖到校董会 | S6/S7 | 各类 | 收费（价格未查） | 活跃 | P-13 ✅（Knight Hub 内使用） |
| 15 | **Knight Election Hub** | 2024 选举资源包（结果、选民指南、培训、专家台） | S3–S7 | LOCAL/INDIE | 免费（Knight 出钱） | **已结束** | P-13 ✅ |
| 16 | **Votebeat Expert Desk** | 选举行政专家，可具名引用 | S3/S5 | LOCAL/NATL | 免费（More Perfect 资助） | 2026 中期选举运行中 | P-14 ✅ |
| 17 | **C-SPAN Road to the Capitol** | 候选人活动完整视频 | S4/S6 | 非营利 LOCAL/INDIE、TV | 免费（基金会资助） | 2026，10 个州 | P-15 ✅ |
| 18 | **RJI / Bay City News AI 选举看板 Playbook** | 教小媒体用 AI 搭选举结果页 | S6 | LOCAL/INDIE | 免费；实操约需每月 20 美元的聊天机器人 | 选前抓取可行，选举夜实时抓取失败 | P-12 ✅ |
| 19 | **OpenElections** | 标准化选区级认证结果 | S2 | 数据记者 | 免费，志愿项目 | 活跃 | P-17 ⚠️ |
| 20 | **Ballotpedia** | 候选人、选举百科；校董会覆盖大学区 | S2 | 各类 | 免费 | 活跃；2025 年校董会分析覆盖 187 个学区 | E-14 ✅ |
| 21 | **LocalLens**（APM） | 会议转写、检索、提醒 | S1/S3 | LOCAL（Chalkbeat 约 80 个学区） | 未公开，机构账户 | 2025-11 被 APM 收购 | E-06 ✅ |
| 22 | **AP School Board Search** | 49 州 3,000 多个学区校董会 YouTube 转写检索与 AI 摘要 | S1/S3 | LOCAL（AP 会员、APFJ、ERN） | 对合作方免费 | 2026-08 上线，约 90 个账户 | E-07 ✅ |
| 23 | **The Beam 校董会 Custom GPTs** | 家长或记者用自然语言问校董会内容 | S1/S7 | INDIE/FREE（亚利桑那） | 免费（ChatGPT 免费账户约每天 5 问） | 8 个学区 → 计划 74 个 | E-08 ✅ |
| 24 | **Zelma / Education Data Center** | 50 州 3–8 年级考试数据统一库，配 AI 出图 | S2 | LOCAL/INDIE/NATL | 免费（Walton、Gates 等资助） | 活跃 | E-05 ✅ |
| 25 | **NCES / IPEDS / CCD** | 联邦教育统计 | S2 | NATL/LOCAL | 免费 | 部分恢复；14 项产品被取消 | E-03 ✅ |
| 26 | **CRDC** | 民权数据（纪律、AP 课程、霸凌） | S2 | LOCAL/NATL | 免费 | 2023-24 版晚约 6 个月发布，没有 First Look 摘要 | E-04 ✅ |
| 27 | **Data Rescue Project / Wayback / 网页变动提醒** | 联邦数据被删前存档 | S2 | 全部 | 免费 | 凑合方案 | E-15 ✅ |
| 28 | **Big Local News（入学数据等）** | 跨州教育数据集 | S2 | LOCAL/NATL | 免费 | 活跃（2025 年在找新合作方） | E-15 ✅ |
| 29 | **州教育厅数据（例：华盛顿 OSPI 处分公告、S-275 人事年表）** | 教职员处分、人事、薪资 | S2 | LOCAL | 免费 | 各州差异大 | E-11 ✅ |
| 30 | **EWA 资源**（博客、listserv、研讨会、奖项） | 选题指南、数据存档提示、同行网络 | S2/S9 | LOCAL/NATL/FREE | 会员制，研讨会常有差旅补助 | 活跃；2021 年后没有新的行业调查 | E-01、E-15 ✅ |

**付费方规律**：表中面向记者的服务（1、13、15、16、17、22、24、28）几乎全由基金会或通讯社出钱，记者免费用。真正有人掏钱的产品（3、4、5、6）卖给游说和政府事务团队。与 05 文件的判断一致：在这两个条线，记者更像免费用户，不是付费主体。

---

## 5. 能自己解决 / 不好解决

### ✅ 能自己方便解决
- 联邦层面单个法案、议员、表决的查询：Congress.gov、LegiScan 免费版（P-06、P-09）
- 县级以上选举的计票和宣布胜选：拿到 APFJ 补贴的媒体可用 AP（P-13）
- 3–8 年级州考试数据的查询和出图：Zelma（E-05）
- 已入库学区的校董会检索：AP School Board Search、LocalLens，限合作媒体（E-06、E-07）
- 选举行政专家与核实：Votebeat Expert Desk 免费（P-14）

### ⚠️ 费力但能
- 跑州法案：州网站"寻宝"，再用 LegiScan 交叉核对、搜示范法案（P-06）。同时盯大量法案时缺少平价工具，Plural 带 AI 的档位要 5,000 美元（P-07）
- 联邦竞选财务的跨源归并：OpenSecrets API 和 ProPublica API 已下线，回到 FEC 原始数据（P-09）
- 联邦教育数据：用存档、找替代源、等延迟发布；CRDC 变成原始文件，要自己写代码（E-03、E-04、E-15）
- 州教育厅冷门数据：熟手能挖出金矿，新手不知道找哪类数据（E-11）
- 进入州议会的简报会和委员会：独立记者要靠诉讼（P-03、P-04）

### ❌ 不好解决
- **下沉选举结果**（县、市、学区）：没有服务覆盖，选举夜手工复制粘贴；AI 实时抓取因格式五花八门而失败（P-12）
- **地方竞选财务**：扫描 PDF，没有聚合层（P-11）
- **州议会日常盯守的人手**：AP 撤站、记者团缩水，"不常驻就做不了"（P-02）；48 个州没有 Digital Democracy 这类工具（P-08）
- **学区 PIO 关卡与进校园**：制度性门槛（E-01、E-02）
- **没有录像的校董会**：约三分之一亚利桑那学区不录像，录了的也有删除的（E-08）；记者稀少的县有 90% 没有任何本地教育报道（E-09）
- **联邦执法线索**：FEC 停摆、OCR 人员减半，执法信息本身就没有了（P-10、E-04）

---

## 6. 最重要的 5 条发现

1. **两个条线都出现了"AI 线索工具 + 慈善或通讯社买单"的模式，而且已写进 JD。** 政治条线有 Digital Democracy（Civil Beat JD 要求"master"它，P-08），教育条线有 LocalLens、AP School Board Search 和 The Beam GPTs（E-06～E-08）。记者把产出当"tip"（线索）而不是稿件；Politico 把不经审核的 AI 产出直接卖给订户，被工会仲裁叫停（P-16）。
2. **下沉选举结果是最清楚的"❌ 不好解决"。** AP 和 Ballotpedia 不覆盖县、市、学区选举。Bay City News 的 AI 实时抓取在选举夜失败，原因包括格式不统一、zero ballots 拿不到、页面结构变化（P-12）。基金会补贴只解决了县级以上的部分（P-13）。
3. **2025–2026 年联邦数据底座被抽掉。** 政治方面：OpenSecrets API、ProPublica Congress API 下线，FollowTheMoney 停止维护，FEC 停摆（P-09、P-10）。教育方面：NCES 被砍 14 项产品，CRDC 晚发并取消面向公众的摘要（E-03、E-04）。数据还在的部分也从"开箱可用"变成了"要自己清洗"。EWA 给出的方案只有自己存档（E-15）。
4. **人手萎缩比工具缺失更根本。** 州议会：AP 撤站，堪萨斯一场听证从 6 人以上变成 1 人（P-02），学生在 30 个州补位（P-05）。中期选举：整个国会选区没人报道（P-15）。教育：综合报纸教育组 39% 缩编（E-01），记者稀少的县 90% 没有本地教育报道（E-09）。
5. **教育记者"高依赖公关、低信任公关"，信源关卡是制度性的。** 81% 每月多次找机构公关，只有 15% 信任公关（E-01）；采访请求被统一转给 PIO（E-02）。州政府记者也一样：69% 认为最大障碍是拿不到记录和接触不到人（P-04）。这类问题单靠工具难以解决。

---

## 7. 证据薄弱处

- **教育记者的量化需求数据停在 2020 年**（EWA 2021，n=419）。2023–2026 年没有新的大样本调查，EWA 页面只有两版报告。
- **政治、选举记者没有行业协会调查**，只有 Collier Prize n=51（P-04）和 Pew 2022 普查（P-01）。2026 年的州议会记者人数不明。
- **记者原话偏少，机构和行为证据偏多**：P-08、E-06、E-07 主要来自机构自述或获奖通报。Reddit 样本中"教育"标签多数是学生媒体，真正的教育条线帖子只有约 8 条。
- **价格未核实**：LegiScan（Cloudflare）、DDHQ、LocalLens、State Affairs 都没有公开价格。
- **高教条线**没有找到高教记者本人谈数据或访问困难的原话（E-13）。国际学生签证撤销期间学生报纸收到删稿请求一事，只见到 Inquirer 的搜索摘要，未写入。
- **TV 群体**在两个条线的证据很少：只有选举季的倦怠帖（P-18）和 C-SPAN 视频补位（P-15），没有找到 TV 教育报道的证据。
- **教师工会和家长群作为信源**：只有 EWA 2020 的信任度数据（工会 31%、家长 55%）和一条联系不上 Moms for Liberty 的帖子。没有找到"家长 Facebook 群当线索源"的记者原话。
- **FEC 停摆期间申报数据是否仍能及时公开**，两方说法不一致（P-10），未核实。
- **未写入的线索**（打不开）：OpenSecrets 2026-10 的州加联邦看板；Federal News Network 关于 NCES 只剩 3 人的报道；Chalkbeat 2026 年关于州考试成绩延迟（费城、纽瓦克）的报道（只看了搜索摘要）。
