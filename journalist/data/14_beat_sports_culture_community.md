# 14 条线深挖：体育 / 文化·餐饮·娱乐 / 社区服务型内容

## 覆盖范围、来源与局限

- **范围**：三个条线。①体育：职业、大学、高中，重点是高中；②文化、艺术、餐饮、娱乐、生活方式；③社区服务型内容：讣告、活动日历、餐厅检查、社区人物。每个条线都按 5 个记者群体 × 9 个环节梳理，并整理了专用工具/竞品表。
- **来源数**：实际打开并核实的来源约 40 个（标 ✅）；另有 9 条招聘 JD 来自本项目已抓取的 `raw/jobs_journalismjobs.jsonl`，其中 MassLive 一条已二次打开核实，其余标 ⚠️；Reddit 原话来自本项目已编码的 `raw/reddit_coded_*.jsonl`，本次 WebFetch 打不开 reddit.com，标 ⚠️。
- **主要局限**：
  1. **APSE 没有公开的"工作量/工具"问卷调查**。2025 APSE Workplace Report（前 TIDES 报告）只统计种族与性别构成，且仅会员可读。APSE 方面能用的只有会议纪要里的原话。
  2. 多家报社的"教练报比分"说明页（PennLive、SILive、Dallas News、Naples News、LA Times、Sun Sentinel、Dispatch）WebFetch 无法抓取，只能用搜索摘要佐证，标 `[未核实]`。
  3. 流量构成缺少可靠数字：没有找到公开的"高中体育/讣告/活动占地方站 PV 的百分比"数据。MassLive "2025 年三分之一新订阅来自高中体育"这一说法原文抓不到，标 `[未核实]`。
  4. 文化/艺术条线的需求证据最薄，基本只有裁员新闻、JD 和一份需填邮箱才能读的调查。
  5. 价格信息多来自较老或二手来源（Lede AI 定价是 2019 年的）。

---

## A. 体育条线

### A-01 | LOCAL, INDIE | S1/S4/S6 | 高中体育 | 需求信号（行业会议原话）
- **结论**：编辑部的共识是比分本身已经不稀缺，记者的价值在于到场、建关系和找"统计表里没有的东西"。
- **证据**：2025 APSE 夏季年会高中体育专场（Cape Cod Times 覆盖约 17 所高中，Star Tribune 覆盖 200+ 所）。Courtney Jacobs 的原话是 "Find something that you won't find in the stats."（去找统计里找不到的东西）；Nick Williams 说 "It's about community, and I cannot stress that enough."；与会者强调要亲自到场，和体育部、家长、球员建立关系。专场听众只有 15 人。
- **来源**：How high school sports coverage is being reinvented for a new generation — https://apsportseditors.com/high-school-sports-coverage-apse-summer-conference-2025/ — APSE / 2025-09-01 — ✅

### A-02 | LOCAL | S9 | 高中/大学 | 需求信号（记者原话）+ 供给
- **结论**：高中体育记者人数在减少，覆盖面在扩大；记者自己把 AI 自动稿看作人手不足的后果。
- **证据**：一位 Gannett 体育记者说 "a lot of high school reporters now are pretty thinly stretched"（如今很多高中记者被摊得很薄），还说 "when there are a few reporters for more teams, we're going to get things like AI"（几个记者要管更多球队，就会出现 AI 这种东西）。（2023）
- **来源**：Futurism — https://futurism.com/gannett-sports-writer-ai-generated-content — 2023-09-05 — ✅（2023）

### A-03 | LOCAL | S9 | 职业/大学/高中 | 供给事件（裁员）
- **结论**：2026 年体育部门仍是裁员重点。《华盛顿邮报》整体撤销体育部；USA TODAY Co. 10 月又裁了一轮体育岗。
- **证据**：2026-02-04 WaPo 裁员约三分之一，撤销体育版和书评版，本地新闻大幅缩减（约 300 人，报道数）。2026-10-01，印第安纳波利斯记者 Akeem Glaspie 宣布其 USA TODAY Co. 的岗位被裁，原定跑 Butler 篮球，属于"更大一轮体育裁员"的一部分。
- **来源**：Washingtonian — https://www.washingtonian.com/2026/02/04/washington-post-kills-sports-section-amid-mass-layoffs/ — 2026-02-04 — ✅；Who covers Friday nights now?（NewsBreak 转载，仅开头可读）— https://www.newsbreak.com/news/4933615491086-who-covers-friday-nights-now-the-press-box-is-getting-quieter — 2026-10 — ⚠️（原文 chathamjournal.com 抓取失败）

### A-04 | LOCAL, TV, INDIE | S1/S7 | 高中 | 需求信号（从业者原话）+ 供给
- **结论**：体育记者在减少，但参赛人数创新高，需求和供给的缺口在扩大。小县报消失后，周六早上的战报和 box score 也随之消失。
- **证据**：体育媒体人 Leah Lowe 2026-10 在 X 上写道 "Local sports journalism staffs are shrinking"，并指出印第安纳、肯塔基已有小报消失。供给侧数据：NFHS 统计 2024-25 学年高中参赛 **8,266,244 人**，创纪录，比上年多 203,942 人。
- **来源**：WV MetroNews — https://wvmetronews.com/2026/10/09/high-school-sports-coverage-alive-and-well-in-wv/ — 2026-10-09 — ✅；NFHS — https://www.nfhs.org/stories/participation-in-high-school-sports-hits-record-high-with-sizable-increase-in-2024-25 — 2025-09-09 — ✅

### A-05 | LOCAL | S8 | 高中 | 采购行为（逆势招人）
- **结论**：反例：有区域数字媒体把高中体育当作订阅增长引擎在扩张。这说明高中体育能变现，但要专职人员加视频。
- **证据**：MassLive（Advance Local）从 2024-09 起新增 3 名全职高中体育记者，覆盖东部 19 支队。Ronnie Ramos 说体育订户会"溢出"去读硬新闻，同时也承认 "I don't think anybody's really found a model that works."（没人真正找到可行模式）。2026-10 MassLive 又发出两条招聘：中部马萨诸塞高中体育记者（年薪 $45,000–52,000，职责包括排名、突发、深度、预告、直播），以及"高中体育 Creator"（短视频、出镜、TikTok/Instagram）。
- **来源**：Nieman Reports — https://niemanreports.org/masslive-local-news-high-school-sports/ — 2025-01-02 — ✅；JD — https://www.journalismjobs.com/1694149-high-school-sports-reporter---central-massachusetts-advance-local — 2026-10-20 — ✅；JD — https://www.journalismjobs.com/1694148-high-school-sports-creator-advance-local — 2026-10-20 — ⚠️（来自 raw 数据）
- `[未核实]`：搜索摘要称 MassLive 2025 年约三分之一的新订阅来自高中体育（chathamjournal 原文无法打开）。

### A-06 | LOCAL | S1–S9 | 高中/大学 | 招聘 JD（工作内容）
- **结论**：2026 年秋季地方体育岗位的 JD 高度一致：比分和逐节过程不再是重点，重点是招生/转学新闻、问责报道、人物故事、视频和播客，而且一人身兼多职。
- **证据**：
  - Richmond Times-Dispatch（Lee）：高中为主、大学为辅，年薪 $45–50k。JD 要求 "goes beyond scores and play-by-play"，内容包括高中"transfer portal"和问责报道。
  - Argus Leader（Lee）：高中加 D1 大学，强调 "breaks recruiting and commitment news"。
  - Butler Eagle：兼职每周 29 小时，覆盖 11 所高中、1 所 D2 大学、1 所社区学院，还要兼周播客主持、拍照剪视频、排版。
  - Maine Trust：$28.20–30.77/小时，做问责深度报道。
  - WDAY（Forum）：新闻/体育 MMJ，时薪 $18.26–19.23。
- **来源**：raw/jobs_journalismjobs.jsonl 中对应 URL：https://www.journalismjobs.com/1693943-sports-reporter---high-schoolcollege-richmond-times-dispatch ；https://www.journalismjobs.com/1693930-high-school--college-sports-reporter-sioux-falls-sd-sioux-falls-argus ；https://www.journalismjobs.com/1693966-sports-reporter-butler-eagle ；https://www.journalismjobs.com/1693923-sports-reporter-maine-trust-for-local-news ；https://www.journalismjobs.com/1694109-newssports-reporter-forum-communications-company — 2026-10 — ⚠️（本项目抓取，未逐页二次打开）

### A-07 | LOCAL | S1/S3 | 高中 | 凑合方案（比分收集）
- **结论**：比分收集的主流凑合方案是"教练主动报送"：每季发公告，让教练在当晚截止前通过邮件或电话报比分和数据。记者"不可能每场都到"。
- **证据**（以下均来自搜索摘要，页面无法抓取，`[未核实]`）：
  - SILive 每季发"教练如何报比分"公告，要求把每日结果发到 sports2@siadvance.com，并说明 "we can't be [everywhere]"；
  - Dallas News 要求比赛日 21:30 前发邮件 results@dallasnews.com 或打热线；
  - PennLive 2025 年秋季也发了同类公告。
- **来源**：https://www.silive.com/highschoolsports/2024/03/attention-all-high-school-coaches-heres-how-to-report-scores-to-silivecom-this-spring.html ；https://www.dallasnews.com/high-school-sports/article/how-high-school-coaches-can-submit-stats-scores-22196124.php ；https://www.pennlive.com/highschoolsports/2025/08/how-to-report-scores-to-pennlive-this-fall.html — ❌（无法打开，仅摘要）
- **判定**：⚠️ 费力但能做。依赖教练配合，经常漏报（尤其是客场和非热门项目），截止前还要人工录入核对。

### A-08 | INDIE | S1/S4/S6/S8/S9 | 高中/JC | 需求信号（独立运营者原话）
- **结论**：个人运营的高中体育站，最大的负担是**每晚处理邮件和数据**，而不是写稿。
- **证据**：210 Prep Sports 由 Brian Baiotto 一人运营，覆盖约 40 所高中和 4 所社区学院。他写道 "I literally do all the work myself"，"Most nights include anywhere between 8-10 hours of processing emails (with info)"（大多数晚上要花 8–10 小时处理带信息的邮件），橄榄球周五回家后还要再干约 10 小时，前两年没有广告或捐赠，差旅自掏腰包。另一例：缅因州的 Hoffer's High School Sports 一学年到场 **257 场**，付费订阅从秋季到春季翻了一倍多。
- **来源**：210 Prep Sports — https://210prepsports.com/2025/05/29/please-consider-supporting-210-prep-sports-first-fundraiser-after-six-years-of-covering-40-high-schools-four-jcs/ — 2025-05-29 — ✅；Hoffer's Newsletter #50 — https://www.hoffershighschoolsports.com/newsletter-50-what-a-year-it-was/ — 2026-07-01 — ✅

### A-09 | INDIE, FREE | S3/S7 | 高中 | 制度门槛
- **结论**：独立和新型媒体在高中赛场面临**采访证与转播权门槛**。州协会对"谁算媒体"没有统一定义，纯社交媒体账号通常不予认证；季后赛的直播、文字直播都要授权和付费。
- **证据**：
  - NFHS 2023 年文章称"什么是媒体"是 "a moving target with no definitive answer"。明尼苏达州规定，纯社交媒体、球探/招生服务不予认证。
  - 威斯康星 WIAA 的规定：传统媒体网站未经许可、未付费，不得做实时音视频或**文字逐节直播**；电台报道每次 $25；按发行量限定证件数（日发行 3 万以上的报纸最多 4 张，周报 1–2 张）。
  - 搜索摘要显示：2026-08 加州 CIF 季后赛媒体权利归 PlayOn（MaxPreps/NFHS Network 母公司）（latimes 无法打开，`[未核实]`）。
- **来源**：NFHS — https://www.nfhs.org/stories/approving-media-to-cover-high-school-sports-events — 2023-02-09 — ✅；WIAA — https://www.wiaawi.org/my-wiaa/media — 无日期 — ✅；LA Times — https://www.latimes.com/sports/highschool/story/2026-08-13/cif-playoff-media-rights-go-to-owner-of-maxpreps-nfhs-network — ❌

### A-10 | NATL, LOCAL | S3/S4 | 职业 | 需求信号（记者原话）
- **结论**：在职业体育条线，**接触不到运动员**是核心难题。更衣室没有恢复到疫情前的开放程度，球队和运动员自建媒体，独立记者的证件还可能被收回。
- **证据**：Poynter 2026 年文章：WNBA 实行两级访问制；Canucks 和 Indiana Fever 各有一名记者被收回证件。Michael Wilbon 说 "Now, they're all protected"；Fever 跑口记者 Scott Agnes 说独立记者做现场报道 "increasingly difficult"；Substack 作者 Maya Goldberg-Safir 说 "How am I supposed to make that as an indie if I want to be allowed back into the press room?"
- **来源**：Welcome to the post-journalism era of professional sports — https://www.poynter.org/reporting-editing/2026/how-athletes-teams-are-replacing-sports-journalism/ — Poynter / 2026-06-12 — ✅

### A-11 | INDIE, NATL | S1/S2/S5 | 大学 | 使用行为 + 制度门槛
- **结论**：大学体育的新空白是**公共记录调查**（开支、NIL、合同）。有人靠这个做出了独立付费刊物，但要面对 FERPA 被滥用和各州 NIL 保密立法。
- **证据**：FOIAball 由 David Covucci 在被 Daily Dot 裁员后于 2025 年秋创办，一年内向各校发出"数千份"记录申请，查出过 38 所大学花在烟花上的 280 万美元等事。他说 FERPA "wildly overused by schools to withhold records"，并说自己入行时各州 "these laws were being passed"（NIL 保密立法正在通过）。
- **来源**：Inside Higher Ed — https://www.insidehighered.com/news/students/athletics/2026/03/31/what-public-records-reveal-about-college-footballs-spending — 2026-03-31 — ✅；Colorado NIL 保密法案（Sportico，tollbit 墙）— https://www.sportico.com/leagues/college-sports/2025/colorado-nil-bill-disclosure-rick-george-1234826877/ — ❌

### A-12 | LOCAL, NATL | S6 | 大学 | 供给（信源方自动化）
- **结论**：大学体育部（SID）自己在用 AI 批量生成战报而且不披露，记者拿到的"官方战报"越来越多是机器写的。
- **证据**：FanWord 称有 250+ 所院校使用，上季生成 30,000 篇 recap；大校年费约 $4,000；FOIAball 联系的学校**没有一家披露** AI 生成；质量问题包括同一篇里四分卫称呼前后不一、节末球位反复出现。
- **来源**：FOIAball — https://www.foiaball.com/p/fan-word-assist-ai-college-sports-game-recaps — 2026-10-07 — ✅

### A-13 | LOCAL | S6 | 高中 | 竞品事故（自动化争议）
- **结论**：面向读者的全自动高中战报出过重大事故，至今仍是业内的警示案例。
- **证据**：Gannett 2023-08 在 Columbus Dispatch 等报刊登 LedeAI 战报，出现 "[[WINNING_TEAM_MASCOT]]" 占位符和 "close encounters of the athletic kind" 这类措辞后暂停。LedeAI 的 CEO 解释为给 Gannett 写的定制代码有 bug："the code had bugs in it"。系统做法：按 box score 把比赛分成"险胜、加时、大比分"等情景，再套人工写好的模板，通过 API 写入 CMS。
- **来源**：Awful Announcing — https://awfulannouncing.com/newspapers/gannett-ai-sports-writing-recaps-ledeai.html — 2023-09-29 — ✅（2023）；另见 06_competitors C6-01

### A-14 | LOCAL | S6/S8 | 高中 | 竞品（自动稿的原始模式与定价）
- **结论**：Lede AI 起源于小报 Richland Source 的内部需求：比赛太多、人手太少。数据来自 ScoreStream 众包比分，按"有流量才收费"定价。
- **证据**（2019）：$200/月，另加 $4/篇（仅当文章 30 天内 PV ≥10 时收费）。2018 赛季发了 1,866 篇，共 148,700 PV；上线前 6–8 周由人工逐篇审核。到 2024 年，Lede AI 的产品线已扩展到房产过户、**餐厅检查**和辅助写作工具 WordNerd，CEO 说 "Small newsrooms are always choosing."
- **来源**：IJNet / Nieman Lab — https://ijnet.org/en/story/local-news-outlet-automates-articles-high-school-sports — 2019-05-06 — ✅（2019）；LION Publishers — https://lionpublishers.com/ai-adoption-how-lede-ai-helps-small-publishers-quickly-generate-content-readers-love/ — 2024-07-17 — ✅

### A-15 | LOCAL, TV | S1/S6 | 高中 | 需求信号（行业调查）
- **结论**：地方编辑部点名想自动化的事情之一就是"高中体育比分"。AP 后来资助的 5 个 AI 工具里却没有一个是做体育的。
- **证据**：AP 调查了近 200 家地方编辑部（覆盖 50 州，2022 年发布），结论是需要 "the automation of basic information, such as social media content and high school sports scores"。2023 年 AP 资助的 5 个工具分别是警情、天气、视频转写、市议会转写、线索分拣，没有体育。
- **来源**：Nieman Lab — https://www.niemanlab.org/2023/10/the-ap-announces-five-ai-tools-to-help-local-newsrooms-with-tasks-like-transcription-and-sorting-pitches/ — 2023-10 — ✅

### A-16 | NATL, LOCAL | S6 | 职业/小众 | 竞品（大媒体内部自动化）
- **结论**：AP、ESPN 已把 AI 战报用在"没人写"的项目上，并加以披露和人工审核。
- **证据**：2024 年 AP 体育每年约 **12,000 篇**稿件用到该技术（与 Data Skrive 合作）；AP 副总裁 Trohanis 说 AI 工具 "don't replace the importance of human and editorial news judgment"。ESPN 从 2024-09 起为 NWSL、PLL 生成 AI 战报，署名 "ESPN Generative AI Services"，每篇经人工编辑审核。
- **来源**：APSE — https://apsportseditors.com/apse-charlotte-in-review-understanding-ai-in-sports-journalism/ — 2024-06-28 — ✅；ESPN Press Room — https://espnpressroom.com/feature/enhancing-espns-game-recaps-for-underserved-sports-using-ai/ — 2024-09-05 — ✅

### A-17 | LOCAL, INDIE | S2/S5 | 高中 | 供给（数据源集中化）
- **结论**：高中体育的数据源正在向一家私募控股公司集中。PlayOn（KKR 系）2025 年收购 MaxPreps 后，同时拥有比分/数据（MaxPreps）、直播（NFHS Network）和票务（GoFan）。
- **证据**：2025-04-02 PlayOn 从 CBS Sports（Paramount）收购 MaxPreps，交易额未披露。搜索摘要显示，MaxPreps 自称是 31 个州协会的官方数据或媒体伙伴（support 页面 403，`[未核实]`），教练可以在 MaxPreps 后台把数据报告直接推送给指定的媒体邮箱（`[未核实]`）。
- **来源**：MaxPreps — https://www.maxpreps.com/news/Qeg1tApLoUWYz53EnRnWZQ/playon-acquires-maxpreps-to-elevate-the-high-school-sports-fan-experience.htm — 2025-04-02 — ✅；https://support.maxpreps.com/hc/en-us/articles/53618845796123-MaxPreps-Official-State-Athletic-Association-Partners — ❌(403)

### A-18 | LOCAL | S1/S2 | 高中 | 供给（众包比分）
- **结论**：ScoreStream 用球迷众包比分补上了"记者到不了的那几千场"，数据分发给 AP 和媒体伙伴，接口按需询价。
- **证据**（2017–2018）：众包每周 10,000–15,000 场高中比赛；2017 年起向 AP 供应 42 州橄榄球、33 州篮球比分；提供 JSON REST/WebSocket API 和白标组件，定价按内容量、市场、展示方式询价。搜索摘要显示，2026 年 USA TODAY 的全国高中比分板仍由 ScoreStream 提供（`[未核实]`）。
- **来源**：PR Newswire — https://www.prnewswire.com/news-releases/scorestream-associated-press-collaborate-to-deliver-more-timely-local-scores-to-fans-300496286.html — 2017-08-03 — ✅（较老）；ScoreStream Blog — http://blog.scorestream.com/scorestream-local-sports-api/ — 2018-03 — ✅（较老）

### A-19 | FREE | S8/S9 | 体育（泛） | 需求信号（Reddit 原话）
- **结论**：自由体育写手的稿酬结构崩塌，从固定稿费变成按 PV 计酬。
- **证据**：一位有 11 年经验的体育写手说 "companies have gone to a $4/1000 views model"（每千次浏览 4 美元）；另一人说曾经 $7 一篇，FanSided 千次阅读约 $1。
- **来源**：r/freelanceWriters — https://www.reddit.com/r/freelanceWriters/comments/1pdmsww/sportswriting_is_dying/ — 2025-12-04 ；https://www.reddit.com/r/freelanceWriters/comments/1mogtva/sports_writer/ — 2025-08-12 — ⚠️（来自本项目 08 编码数据，本次 reddit.com 无法打开）

### A-20 | LOCAL | S1/S5 | 高中/青少年 | 需求信号（Reddit 原话）
- **结论**：地方记者收到越来越多"家长伪装成学校或机构"发来的孩子成绩新闻稿，需要额外核实。
- **证据**：原话 "But, they are being sent by their parents"。
- **来源**：r/Journalism — https://www.reddit.com/r/Journalism/comments/1rjupcq/omg_i_hope_this_is_not_a_trend/ — 2026-03-03 — ⚠️（同上）

### A-21 | 受众侧 | S8 | 体育 | 供给/受众数据
- **结论**：读者对地方体育报道的满意度中等，地区差异明显，中西部关注度最高。
- **证据**：Pew 调查 5,146 名美国成年人（2024-01）。在获取地方体育新闻的人中，43% "非常/极其满意"（天气 63%、交通 44%、地方经济 26%、地方政治 25%）；"经常"获取地方体育新闻的比例在中西部为 29%，其他地区 ≤22%。
- **来源**：Pew — https://www.pewresearch.org/journalism/2024/05/07/local-news-topics/ — 2024-05-07 — ✅；https://www.pewresearch.org/journalism/2024/05/07/americans-changing-relationship-with-local-news/ — ✅

### A-22 | LOCAL | S6 | 高中/体育 | 竞品（United Robots）
- **结论**：United Robots 的体育机器人在北欧已规模化，在美国以地方集团为客户。它有个特色功能：通过短信向教练要引语。
- **证据**：产品包括赛前预告、赛后报道、统计组件、视频转文字，以及"短信问教练、自动插入引语"（约 2,400 名活跃教练用户）。官网列举的都是北欧客户，价格不公开。07 文件已核实：McClatchy 自 2021 年起在 8 个市场使用其房产和高中体育稿。
- **来源**：United Robots — https://www.unitedrobots.ai/content-services/sports — 无日期 — ✅；另见 07_gap_fill（McClatchy）

### 体育条线：五群体 × 九环节（"推断"表示无直接证据，依据 JD 或行业惯例推断）

| 环节 | LOCAL（报社体育记者） | TV（台体育/MMJ） | INDIE（个人高中体育站） | NATL（职业/大学跑口与调查） | FREE（自由写手/学生） |
|---|---|---|---|---|---|
| S1 发现线索 | 赛程表、教练报送、招生/转学传闻、家长来信（A-06/07/20） | 选周五重点场次（推断，A-06 WDAY JD） | 邮件洪流加社交媒体（A-08） | 公共记录、内幕消息（A-11） | 自选题，缺门路（A-19） |
| S2 背景研究 | MaxPreps 历史战绩、排名（A-17） | 同左（推断） | 同左 | 合同、预算、NIL 数据库（A-11） | — |
| S3 找信源 | 教练、AD、家长关系（A-01） | 同左 | 同左，证件受限（A-09） | **运动员接触受限**（A-10） | 证件难拿 |
| S4 采访与素材 | 到场、赛后采访、拍照拍视频（A-06） | 拍摄剪辑（A-06） | 一人包办（A-08） | 新闻发布会为主（A-10） | — |
| S5 核实 | 比分与数据人工核对，教练报送易错（A-07） | — | 同左 | FOIA 文件核对 | — |
| S6 写作与制作 | 战报、深度、短视频、播客（A-06）；自动稿争议（A-13） | 广播稿、出镜 | 战报、通讯、播客 | 深度调查 | 按 PV 计酬的快稿（A-19） |
| S7 发布与分发 | 网站、高中体育通讯、直播（A-05） | 新闻节目 | 网站、通讯；直播受转播权限制（A-09） | — | 平台 |
| S8 受众与变现 | 订阅驱动（A-05）；满意度 43%（A-21） | — | 付费订阅、捐赠（A-08） | 付费通讯（A-11） | $4/千次浏览（A-19） |
| S9 职业与生存 | 被裁/兼职（A-03/06） | 低时薪 MMJ（A-06） | 一人 8–10 小时/晚（A-08） | 部门被撤（A-03） | 收入崩塌（A-19） |

---

## B. 文化 / 艺术 / 餐饮 / 娱乐 / 生活方式

### B-01 | NATL, LOCAL | S9 | 艺术评论 | 供给事件（裁员）
- **结论**：2026 年大报的艺术评论岗继续被砍。WaPo 撤销首席戏剧评论岗，书评版整体取消。
- **证据**：首席戏剧评论人 Naveen Kumar 被裁，他说自己是和 "several of the paper's other arts editors" 一起被裁的；WaPo 将收缩到全国政治、商业、健康，华盛顿本地艺术报道前景不明。
- **来源**：Playbill — https://playbill.com/article/washington-post-lays-off-theatre-critic-naveen-kumar-raising-questions-of-continuing-arts-coverage — 2026-02-04 — ✅

### B-02 | LOCAL | S9 | 餐饮评论 | 采购行为（重建）
- **结论**：反例：被 Hearst 收购后，Dallas Morning News 重建了餐厅评论团队（编辑 + 评论人 + 数字制作）。
- **证据**：该报已 4 年多没有正式的餐厅评论，2019 年后署名评论中断，2022 年连零星的自由撰稿专栏也停了；目前日常餐饮报道由两名美食记者承担。
- **来源**：CraveDFW — https://cravedfw.com/2026/07/30/the-dallas-morning-news-is-finally-hiring-a-restaurant-critic-again/ — 2026-07-30 — ✅（二手转述 JD）

### B-03 | LOCAL | S1/S3/S6 | 文化 | 招聘 JD（工作内容）
- **结论**：文化记者 JD 明确要求"超越活动预告和新闻稿"。说明日常的主要工作量就是处理活动预告和新闻稿，编辑部想把时间腾出来做独家和问责报道。
- **证据**：Quad-City Times（Lee）文化记者，$45–50k，JD 原文 "move beyond event previews and press releases"，覆盖音乐、艺术、戏剧、餐饮、节庆，还要做"帮读者决定去哪儿"的指南。Philadelphia Inquirer 美食作者：每周发稿多次，做区域美食指南和地图，要出镜，经营 Instagram/TikTok。Aspen Public Radio 艺术文化广播记者每周还要值一天晚班突发。
- **来源**：https://www.journalismjobs.com/1693918-culture-reporter-quad-city-times ；https://www.journalismjobs.com/1693945-food-writer-the-philadelphia-inquirer ；https://www.journalismjobs.com/1694217-broadcast-journalist-arts--culture-aspen-public-radio — 2026-10 — ⚠️（raw 数据）

### B-04 | INDIE | S8/S9 | 艺术文化独立刊物 | 行业调查（有方法论）
- **结论**：独立艺术文化刊物普遍是"受众在增长、人手和预算极小、资金不稳定"。
- **证据**：Rabkin Foundation 与 Critical Minded 于 2026 年初调查了 141 家独立艺术文化刊物（34 州加 DC），结论是 "remarkably small staffs and budgets"，资金难以持续，还面临言论自由方面的压力。具体数字需要填邮箱才能读到全文。
- **来源**：Rabkin Foundation — https://www.rabkinfoundation.org/survey — 2026 — ✅（仅摘要页）

### B-05 | LOCAL, TV | S1/S6 | 餐饮（检查） | 使用行为（常规栏目）
- **结论**：餐厅卫生检查已经是地方台和报社的**每周固定栏目**，数据来自县卫生部门，是典型的"数据搬运 + 选高低分"格式。
- **证据**：KRDO（科罗拉多泉）每周 "Restaurant Roundup" 依据 El Paso 县卫生部门例行检查，挑出最高分和最低分的餐厅，有时记者会到店探访。搜索结果显示 Syracuse.com、Post-Star、LancasterOnline 也都有每周检查汇总（未逐一打开）。Lede AI 和 United Robots DataDesk 都把"餐厅检查"列为自动化品类（A-14；07 文件）。
- **来源**：KRDO — https://krdo.com/news/restaurant-roundup/2026/07/24/colorado-springs-restaurant-inspections/ — 2026-07-24 — ✅

### B-06 | LOCAL, INDIE | S2/S5 | 餐饮（检查） | 数据可得性（凑合方案的难度）
- **结论**：餐厅检查数据高度碎片化，约一半的市县开放数据集已停止更新，有的地方只能走记录申请。
- **证据**：某目录站 2026-09-17 统计了 27 个市县数据集，其中 14 个停更（4 个明确冻结：达拉斯、旧金山两个、休斯顿）。平台分别用 Socrata、CKAN、ArcGIS；行的粒度不统一（纽约按违规条目一行，芝加哥按检查一行）；费城没有可下载的数据集。达拉斯和旧金山改为跳转到供应商的查询页。另据搜索摘要，俄亥俄州 Franklin 县 2025-05 换平台后，2025-05-09 至 2026-05-19 的报告只能通过记录申请获取（页面抓取为空，`[未核实]`）。
- **来源**：foodinspectiondata.us — https://foodinspectiondata.us/data/inspection-open-data-portals/ — 2026-09-17 — ⚠️（新站，发布方身份不明）；Franklin County Public Health — https://myfcph.org/food-inspection-reports/ — ❌
- **判定**：⚠️/❌。大城市有开放数据，可以自己抓；中小县和换了系统的地方很难。

### B-07 | FREE | S9 | 餐饮/艺术 | 需求信号（Reddit 原话）
- **结论**：自由美食和艺术写手投稿很难得到回应。
- **证据**："thirty or so pitches to smaller and larger arts publications with little to no responses"；Buffalo 美食写手说本市首次有两家餐厅进入 James Beard 决选，自己却 "can't get a nibble"。
- **来源**：https://www.reddit.com/r/Journalism/comments/1tqxal8/do_editors_just_see_my_email_and_ignore_me/ — 2026-05-29；https://www.reddit.com/r/freelanceWriters/comments/1cqdet1/introducing_myself_starting_solo_career_after_35/ — 2024-05-12 — ⚠️（08 编码数据）

### B-08 | 受众侧 | S8 | 艺术/文化 | 受众数据
- **结论**：读者对艺术文化类地方新闻有需求，但获取频率低于天气和治安。
- **证据**：Pew 2024 年数据显示，"至少半数（但比例较小）"成年人获取地方艺术文化新闻，没有给出精确百分比。AJP 影响报告提到，Mirror Indy 的读者调查显示，艺术文化报道带动读者参加本地活动、光顾本地商家（仅见搜索摘要，`[未核实]`）。
- **来源**：Pew — https://www.pewresearch.org/journalism/2024/05/07/americans-changing-relationship-with-local-news/ — ✅；AJP — https://theajp.org/wp-content/uploads/2026/06/American-Journalism-Project_Impact-Report-2025-compressed.pdf — ❌

### 文化/餐饮条线：五群体 × 九环节

| 环节 | LOCAL | TV | INDIE | NATL | FREE |
|---|---|---|---|---|---|
| S1 发现线索 | 新闻稿、活动预告，需要更多"公告前"的线索（B-03） | 每周检查汇总（B-05） | 周日上午搜索各站加自建爬虫（C-03） | — | 自选题 |
| S2 背景研究 | 卫生检查数据碎片化（B-06）；开业要查许可/酒牌（推断，无证据） | 同左 | — | — | — |
| S3 找信源 | 艺术家、店主、机构（B-03） | — | 读者投稿（C-03） | — | 编辑不回复（B-07） |
| S4 采访与素材 | 探店、看演出（B-03） | 到店探访（B-05） | — | — | — |
| S5 核实 | 活动时间/链接易过期，需要复核（C-03） | — | 同左 | — | — |
| S6 写作与制作 | 指南、地图、评论、短视频（B-03） | 栏目化 | 通讯 | 评论（被砍 B-01） | — |
| S7 发布与分发 | 指南页、社交平台 | 节目 | 通讯、短信 | — | — |
| S8 受众与变现 | 指南带 SEO；评论重建（B-02） | — | 广告、会员（C-03） | — | — |
| S9 职业与生存 | 评论岗被砍（B-01） | — | 小团队、资金不稳（B-04） | 部门撤销（B-01） | 投稿难（B-07） |

---

## C. 社区服务型内容（讣告 / 活动日历 / 社区人物）

### C-01 | LOCAL, INDIE | S7/S8 | 讣告 | 行业调查（有方法论）+ 供给
- **结论**：付费讣告对小报仍然重要，但在持续流失：家庭转向殡仪馆官网，报纸只覆盖少数讣告。讣告基本没有专职人员，由现有人手兼顾。
- **证据**：
  - 2026 年密苏里研究调查了 135 位周报负责人：88% 对讣告收费；其中 80% 的报纸讣告收入占总收入 <5%；89% 认为讣告是关键的社区纽带；73% 认为讣告是读者订阅或购买的关键原因；专职讣告人员很少，工作一般"折进现有流程"，靠与本地殡仪馆的关系维持。
  - Legacy.com 称讣告刊登量连续 8 年每年下降约 10%，在多数市场报纸只覆盖殡仪馆官网讣告的 <30%；42% 的讣告在非工作时间提交。
  - 一位出版人说 "Where else would we find $17,000?"
- **来源**：Editor & Publisher — https://www.editorandpublisher.com/stories/news-media-grapples-with-declining-obits-revenue,264064 — 2026-10-21 — ✅

### C-02 | LOCAL | S7/S8 | 讣告 | 竞品（Legacy.com）
- **结论**：Legacy.com 已成为讣告的中间层：消费者直投、AI 写讣告、与报业集团签全托管协议。报社在讣告环节的"人工"正在被平台接管。
- **证据**：
  - 2022 年底上线消费者直投后，累计为合作报纸带来 **$52M 收入、110,000 篇讣告**，近 40% 的订单在非工作时间或周末提交，合作报纸 2,800 家（2024-02）；
  - 推出 AI 工具 ObitWriter，可嵌入殡仪馆官网；
  - 与 iPublish 一起为 CherryRoad Media 的 95 家报纸提供全托管讣告服务（搜索摘要，未打开）。
- **来源**：America's Newspapers — https://www.newspapers.org/stories/legacy,4164299 — 2024-02-14 — ✅；Legacy ObitWriter — https://obitwriter.legacy.com/ — ⚠️（仅搜索摘要）

### C-03 | INDIE | S1/S5/S6/S8 | 活动日历 | 使用行为（运营者原话）
- **结论**：独立活动通讯的核心工作是**每周手工搜集和核对活动**。有人自己写爬虫，"准确性"是他们和别家拉开差距的地方。
- **证据**：Around Evanston 每周日上午搜索各网站，团队还**自建了抓取活动网站的工具**；建一期清单约 3 小时，校对 1 小时以上；DeRuiter 说链接错了读者就不再信任。订户从 7 人增长到约 4,400 人/周，收入来自精选列表广告和赞助活动。Broke-Ass Stuart 每期约 35,000 读者，Patreon 近 1,300 人、每月 $4,500 以上。
- **来源**：Inbox Collective — https://inboxcollective.com/what-you-can-learn-about-running-a-local-events-newsletter-from-three-publishers-who-do-it/ — 2026-02-18 — ✅
- **判定**：⚠️ 费力但能做。每周固定耗 4 小时以上，链接和售罄信息会过期，需要重复核对。

### C-04 | LOCAL, TV | S1/S7/S8 | 活动日历 | 竞品（CitySpark 等）
- **结论**：报社和电视台的活动日历普遍外包给白标平台（CitySpark、Evvnt），由主办方自助提交、平台聚合，媒体方付小额月费并分成。编辑部在这里基本只做审核。
- **证据**：CitySpark FAQ 写明，出版商通常支付 "a small monthly fee"，价格取决于流量、市场规模、配置和分成比例；升级列表的收入往往能覆盖月费；直接卖给本地商家的赞助收入 100% 归出版商；支持反向出版到印刷版和通讯；为 "hundreds of media sites" 提供服务。Sun Sentinel 和 Summit Daily 都用 CitySpark（搜索摘要）。Evvnt 宣称可一次提交同步到 5,500+ 个日历站（搜索摘要）。第三方估算 CitySpark 2025 年收入约 $2.9M、26 人（getlatka，未核实）。
- **来源**：CitySpark FAQ — https://www.cityspark.com/faq/ — ✅；Sun Sentinel calendar submission — https://www.sun-sentinel.com/calendar-submission/ — ❌（无法抓取）；Evvnt — https://evvnt.com/ — ⚠️（仅摘要）

### C-05 | 受众/信息环境 | S5 | 讣告 | 供给（风险）
- **结论**：AI 讣告农场和讣告诈骗干扰了讣告信息环境，"谁去世了、葬礼何时何地"需要回到殡仪馆或家属来源核实。
- **证据**：AI Incident 752（2024）：内容农场未经家属同意生成讣告，含有事实错误（例如虚构军功章），被归类为错误信息。Tribute Technology（殡仪馆网站供应商，有利益相关）称：殡仪馆网站的讣告每年 35 亿次访问，聚合站每篇最多分走 260 次会话，数字讣告已占死亡通知的 65%。
- **来源**：MIT AI Risk Incident 752 — https://airisk.mit.edu/ai-incidents/752-ai-generated-obituaries-are-reportedly-intensifying — ✅；Tribute Technology — https://www.tributetech.com/tribute-technology-releases-landmark-obituary-study-traffic-engagement-and-industry-threats — 2025-10-06 — ✅（供应商自报）

### C-06 | LOCAL | S1/S6 | 社区数据（检查/许可/房产） | 竞品（线索型）
- **结论**：自动化厂商正从"代写稿件"转向"推送线索"，社区服务型数据（餐厅检查、建筑许可、法院文书）是首批品类。
- **证据**：07 文件已核实：United Robots 2026 年推出 DataDesk，监控建筑许可、餐厅检查、法院文书、政府决定等，向编辑部推送"值得报"的线索；Lede AI 2024 年的产品线包括餐厅检查和房产过户（A-14）。
- **来源**：见 07_gap_fill（https://www.newspapers.org/stories/united-robots,4167029 — 2026-07-15 — ✅）；LION — 见 A-14

### 社区服务型：五群体 × 九环节

| 环节 | LOCAL | TV | INDIE | NATL | FREE |
|---|---|---|---|---|---|
| S1 发现线索 | 殡仪馆来稿、日历自助提交（C-01/04） | 社区日历表单 | 手工搜集加爬虫（C-03） | 名人讣告（不在本范围） | — |
| S2 背景研究 | — | — | — | — | — |
| S3 找信源 | 殡仪馆关系（C-01） | — | 读者投稿（C-03） | — | — |
| S4 采访与素材 | 新闻性讣告需要采访家属（推断） | — | — | — | — |
| S5 核实 | 讣告农场干扰（C-05）；活动信息过期（C-03） | 同左 | 同左 | — | — |
| S6 写作与制作 | 家属自写或 AI ObitWriter（C-02） | — | 通讯 | — | — |
| S7 发布与分发 | Legacy 托管、CitySpark 反向出版（C-02/04） | 白标日历 | 通讯、短信 | — | — |
| S8 受众与变现 | 讣告收入 <5%，被视为订阅理由（C-01）；日历分成（C-04） | 日历分成 | 广告、会员（C-03） | — | — |
| S9 职业与生存 | 无专职，兼顾处理（C-01） | — | 每周固定 4 小时以上（C-03） | — | — |

---

## 竞品 / 工具表（本范围）

| 工具 | 解决什么 | 主要群体 | 价格 / 付费方 | 状态 | 来源 |
|---|---|---|---|---|---|
| MaxPreps（PlayOn） | 高中赛程、比分、统计、排名；教练录入后推送给媒体 | LOCAL/INDIE/TV（读数据），学校（录入） | 对媒体读者免费，有消费者订阅；B2B 条款不公开 | 2025-04 被 PlayOn 收购，存活 | A-17 ✅ |
| NFHS Network / GoFan（PlayOn） | 高中直播、票务；部分州季后赛转播权 | 学校、球迷；媒体受其版权限制 | 观众订阅；学校分成 | 存活且在扩张 | A-17 ✅ / A-09 |
| ScoreStream | 众包比分、API、白标比分组件；供应 AP | LOCAL/TV | B2B 询价 | 存活（2026 年 USA TODAY 比分板 `[未核实]`） | A-18 ✅（较老） |
| Lede AI | 用比分数据加模板自动生成高中战报，另有房产过户、餐厅检查、WordNerd | LOCAL/INDIE | 2019 年：$200/月 + $4/篇（PV≥10 才收费）；现价未知 | 2023 Gannett 暂停；2024 仍在推广；2025–26 动态 `[未核实]` | A-13/14 ✅ |
| United Robots（体育 / DataDesk） | 自动体育稿、短信要教练引语、统计组件；DataDesk 推送线索 | LOCAL（集团） | 询价 | 存活；McClatchy 等在用 | A-22 ✅，07 |
| AP + Data Skrive | 体育自动稿约 12,000 篇/年 | NATL，AP 会员 | AP 会员费 | 存活 | A-16 ✅ |
| ESPN Generative AI recaps | 冷门联赛战报，署名披露并人工审核 | NATL（自用） | 自建 | 存活 | A-16 ✅ |
| FanWord Assist | 大学体育部自动生成战报、球员简介 | 信源方（SID），间接影响记者 | 大校约 $4,000/年，学校付费 | 250+ 校；Texas Tech 未续约 | A-12 ✅ |
| Sportradar | 职业和大学体育数据 API | NATL 媒体、博彩 | 企业级询价 | 存活（本次未查与地方记者的关系） | 官网（未深入） |
| CitySpark | 白标活动日历：聚合、自助提交、推广升级、票务、反向出版到印刷版 | LOCAL/TV | 出版商付小额月费加分成；主办方为升级付费 | 存活，"hundreds of media sites" | C-04 ✅ |
| Evvnt | 活动一次提交、多站同步；出版商日历 | LOCAL/TV | 主办方按活动付费 | 存活 | C-04 ⚠️ |
| Legacy.com（含 ObitWriter、消费者直投） | 讣告收稿、计费、托管、AI 写讣告 | LOCAL（报社讣告） | 家庭付费，报社分成 | 存活；合作报纸 2,800 家 | C-02 ✅ |
| Ticketmaster Discovery API | 演出、场馆、开售数据 | 文化/活动类开发者 | 免费 key | 存活（无证据显示记者在用） | 官网摘要 ⚠️ |
| 县卫生部门开放数据 / 供应商查询页 | 餐厅检查 | LOCAL/TV | 免费；碎片化，约半数停更 | — | B-06 ⚠️ |

---

## "能自己解决 / 不好解决"清单

**✅ 能自己方便解决**
- 热门高中项目的比分和基础数据：MaxPreps 和 ScoreStream 公开可查，报社也让教练报送（A-07/17/18）。
- 职业和大学的赛果与统计：AP/Sportradar 数据加 AP 自动稿（A-16）。
- 活动日历的"上架"：CitySpark/Evvnt 白标，主办方自助提交，媒体只做审核（C-04）。
- 付费讣告的收稿和计费：Legacy 直投，非工作时间也能下单（C-02）。
- 大城市的餐厅检查：开放数据或县查询页，做成每周栏目（B-05）。

**⚠️ 费力但能做**
- 冷门项目、客场、低级别比赛的比分：靠教练报送，常漏；个人站每晚要花 8–10 小时处理邮件和数据（A-07/08）。
- 精选活动通讯：每周 4 小时以上的手工搜集和核对，链接与售罄信息会过期（C-03）。
- 大学体育公共记录调查：需要发数千份申请，还要应对 FERPA 被滥用（A-11）。
- 文化条线的"公告前"独家：JD 要求如此，但日常时间被新闻稿和活动预告占满（B-03）。

**❌ 不好解决**
- 职业运动员的接触与采访权：结构性收缩，证件可能被收回（A-10）。
- 独立媒体拿高中季后赛证件和直播/文字直播权：州协会门槛加转播权付费（A-09）。
- 中小县、换了系统的地方的餐厅检查数据：停更、只能走记录申请、格式不一（B-06）。
- 各州 NIL 合同保密：立法层面的封闭（A-11）。
- 识别 AI 生成或家长代写的"信源稿"：大学体育部的 AI 战报不披露（A-12），家长伪装新闻稿（A-20），讣告农场（C-05）。

---

## 最重要的 5 条发现

1. **高中体育是"供给缩、需求涨"的典型剪刀差，而且已有人证明它能变现。** 参赛人数 826.6 万创新高（A-04），大报和集团仍在砍体育岗（A-03）；同时 MassLive 在逆势扩编，并把高中体育当订阅引擎（A-05），个人站付费订阅一季翻倍（A-08）。
2. **记者的瓶颈不在写战报，在数据收集和核对的体力活。** 个人运营者每晚 8–10 小时处理邮件和数据（A-08），报社每季靠公告求教练报比分（A-07）；AP 调查里地方编辑部点名要自动化"高中比分"（A-15）。业内认为比分本身不值钱，值钱的是统计之外的东西（A-01/06）。
3. **面向读者的全自动内容翻过车，存活下来的是"内部辅助、带披露"的形态。** LedeAI × Gannett 暂停（A-13）；AP 和 ESPN 带披露、人工审核的模式在持续（A-16）；厂商正从代写转向推送线索（C-06）。
4. **数据和渠道在向平台集中，并形成准入门槛。** PlayOn 同时控制 MaxPreps、NFHS Network、GoFan 和部分州季后赛权利（A-17/A-09）；Legacy 接管讣告流程（C-02）；CitySpark 接管活动日历（C-04）。编辑部在这些环节的人工投入很少，独立媒体则被证件和转播权挡在门外。
5. **社区服务型内容的"可靠性"成了新痛点。** 大学体育部用 AI 写战报且不披露（A-12），家长伪装新闻稿（A-20），讣告农场（C-05），活动链接过期（C-03），检查数据集停更（B-06）。核实成本在上升。

---

## 证据薄弱处

- **流量和收入构成**：没有可靠的公开数据说明高中体育、讣告、活动在地方站 PV 或订阅中的占比。MassLive "三分之一新订阅"的说法未核实；讣告收入"<5%"来自密苏里周报样本（n=135），不能推广到日报。
- **APSE 调查**：没有找到关于工作量或工具使用的 APSE 问卷，只有会议纪要原话，样本小（专场 15 人）。
- **TV 群体**：体育、文化条线几乎只有 JD 证据，缺少电视台体育编辑台的原话。
- **NATL 和 FREE 在社区服务条线**：基本空白（本身也不是他们的主战场）。
- **文化/艺术条线**：需求信号主要是 JD 和裁员新闻，Rabkin 调查的具体数字需要填邮箱获取；餐厅开业线索的来源（许可、酒牌）没有找到记者原话，表中标为推断。
- **价格**：Lede AI 只有 2019 年价格；ScoreStream、United Robots、CitySpark、MaxPreps 的 B2B 价格均为询价；FanWord 约 $4,000 来自 FOIAball 拿到的合同。
- **无法打开的来源**：多家报社的比分报送页（SILive/PennLive/Dallas News）、latimes（CIF 权利）、chathamjournal 原文、sun-sentinel、reddit.com（使用本项目已编码数据）、Sportico（tollbit 墙）。
