# 16 · S9 职业与生存 + 自由撰稿人完整工作流

## 0. 范围、来源与局限

- **范围**：
  - **在职记者的 S9**：裁员、倦怠、薪资、转型、技能更新（AI）、安全与法律风险。
  - **自由撰稿人/创作者记者（FREE、INDIE）的完整工作流**：找活与投稿 → 谈价 → 合同与版权 → 交付（含 AI 检测误判）→ 开票收款 → 作品集与个人品牌 → 多收入来源与 AI 抢活。
  - 每一环都写痛点、凑合方案和可解决度判定（✅ 能自己方便解决 / ⚠️ 费力但能 / ❌ 不好解决），并附竞品/工具表。
- **本轮新增一手来源（实际打开核实）约 30 个**，并复用 01、03、04、07、08 中的相关条目（用 ID 互引，不重复抄写）。
- **本轮新增的两项一手数据分析**：
  1. **NWU Freelance Solidarity Project（FSP）费率库原始 CSV**：GitHub 公开，1,275 条，截至 2025-11-05。我按 `news_type=news` 加美国（或国家留空）筛出 905 条，自行统计了来源渠道、付款时效、合同、版权、kill fee（稿件被毙时的补偿费）和每词费率。
  2. **08 号 Reddit 编码语料中的 1,000 条 S9 帖子**：按痛点、凑合方案、原话字段做关键词二次归类，得到 S9 子主题分布。
- **主要局限**：
  - FSP 是自愿匿名填报，选择偏差明显；字段缺失率 20%–40%，所有百分比都只以作答者为分母。
  - Reddit 的 r/freelanceWriters 里大量是内容营销和 SEO 写手，并非新闻记者。AI 抢活、AI 检测误判这两类痛点在"记者"身上的强度可能被高估。
  - 美国本土有方法论的自由记者大样本调查（Willnat 等，2,133 人，2024）只拿到摘要，正文 403。
  - UNC CISLM《Stayers and Leavers》正文页被反爬拦截，UNC 文库连接被拒，只能用摘要片段。
  - Clippings.me 当前价格页被 Cloudflare 拦截，未核实。
  - BLS 职业薪资页 403，薪资数据仍沿用 Muck Rack 2026（01-40）。

---

## 1. 在职记者：S9 痛点

**S9-01 | LOCAL, TV, NATL | S9 裁员 | 全条线 | 市场数据（事件计数）**
- **结论**：新闻业裁员在 2025 年短暂放缓后，2026 年再次加速，并且开始明确以"AI/自动化"为理由，地方电视台首当其冲。
- **证据**：
  - Press Gazette 统计的英美新闻业裁员：2023 年约 6,000 人，2024 年至少 3,875 人，2025 年至少 3,434 人。
  - 2026 年的大额裁员：华盛顿邮报 2 月裁掉约三分之一员工（含 300 多名新闻采编人员）；Scripps 确认裁 431 人，CEO 称公司在 "leaning into AI, automation, technology"（全力投入 AI、自动化和技术）；Toledo Blade 若找不到买家将于 12-31 关停，涉及 116 人。
  - 另一口径：Challenger 统计 2025 年前 11 个月美国新闻岗位裁员 2,254 个，同比下降 50%；同期整个媒体行业裁员 17,163 个，同比上升 18%。
  - 两家口径不同：Press Gazette 含英国，Challenger 只算美国公告。
- **来源**：
  - Journalism job cuts in 2026 tracked — https://pressgazette.co.uk/news/journalism-job-cuts-in-2026-updates/ — Press Gazette / 2026-10-29 更新 — ✅
  - News Layoffs Slow As Sector Shows Signs Of Stabilizing — https://www.insideradio.com/free/news-layoffs-slow-as-sector-shows-signs-of-stabilizing-challenger-reports/article_319423e2-2f5f-48f6-91ef-ddb0f5b76b72.html — Inside Radio / 2025-12-08 — ✅

**S9-02 | TV, LOCAL | S9 裁员/技能 | 电视制作 | 需求信号（记者原话）**
- **结论**：一线已经看到 AI 直接替代制作岗位，这和 S9-01 中集团层面的表态相互印证。
- **证据**：
  - 一名前 TEGNA 台员工描述原台的新流程："producers will make a rundown, then have the AI do all of the cuts and adjustments"（制片做好串联单，剪辑和调整全交给 AI）。原台的 PA 和导播被裁。
  - 另一名报社员工称报社强制全员使用 AI，原话 "everyone in editorial will have to use AI tools"（编辑部所有人都必须用 AI 工具）。他的凑合办法是在工会提出把 AI 写进集体协议。
- **来源**：r/Journalism 2026-03-12 — https://www.reddit.com/r/Journalism/comments/1rs4kek/my_old_news_station_is_downsizing_all_of/ ；r/Journalism 2025-07-05 — https://www.reddit.com/r/Journalism/comments/1ls5dr8/ai_use_becoming_compulsory_in_my_newsroom/ — ✅（08 语料原文）

**S9-03 | LOCAL, TV | S9 倦怠/薪资 | 地方综合 | 需求信号（原话）+ 既有调查**
- **结论**：地方记者的倦怠和低薪已经到了"生存线"层面。离开的凑合办法是海投传播类岗位，但转出同样困难。
- **证据**：
  - 一位东南部周报的执行主编说，报社只有他和一名记者，要跑 11 个镇加一个县，从未加过薪，靠食物银行吃饭；两年投了 250 多份传播、公关、政府岗位，只拿到一次面试。原话 "The pay is abysmal"（薪水低得可怕）。
  - 其他原话：时薪 17 美元的数字制作岗；Sinclair 首个市场年薪不到 3.5 万美元，遭同事性骚扰，HR 不作为。
  - 既有调查（不重复展开）：50% 的记者一年内想过因倦怠辞职（01-13）；地方记者约 72% 想过离开（01-14）；美国全职记者 45% 年薪在 4 万–7 万美元（01-40）。
- **来源**：
  - r/Journalism 2026-05-26 — https://www.reddit.com/r/Journalism/comments/1togfxh/how_to_transition_away_from_journalism/ — ✅（原文已复核）
  - r/Journalism 2026-07-18 — https://www.reddit.com/r/Journalism/comments/1uzzook/when_to_quit_and_move_on/ ；2025-11-21 — https://www.reddit.com/r/Journalism/comments/1p2ot82/where_do_i_go_after_my_first_market/ — ✅（08 语料）

**S9-04 | LOCAL, NATL | S9 留任 | — | 需求信号（有方法论的调查，仅摘要）**
- **结论**：CISLM 的第二份研究（2024 年初，600 多名在职和已离职的地方记者）发现，记者有使命感，但"长期职业晋升路径、工作与生活平衡、可持续的薪酬"三者都缺。
- **证据**：
  - 调查时间为 2024-01-22 至 02-16。
  - 搜索摘要显示：每周工作 31–40 小时的人，在留任者中占 24%，在离开者中占 14%。
  - 被问到"什么是可持续的地方新闻职业"时，主题集中在更好的薪酬和工作生活平衡。
- **来源**：Stayers and Leavers — https://www.cislm.org/research/stayers-and-leavers/ — UNC CISLM / 2024 — ⚠️（页面被反爬拦截，只用搜索摘要；UNC 文库 https://cdr.lib.unc.edu/concern/scholarly_works/5999nj26p 连接被拒）

**S9-05 | LOCAL, NATL, TV | S9 转型 | — | 需求信号（已发生的行为：职业流向数据）**
- **结论**：记者转型最"体面"的出口是企业内容和品牌编辑岗，但这条路慢、窄，而且偏向资深者。基层记者多数只能海投公关岗。
- **证据**：
  - HumanCount 基于 Live Data Technologies 的 1.24 亿份公开履历做了统计：2015-01 至 2026-05，至少 2,800 名记者转去非新闻企业做内容、编辑或传播，每年约 230–340 人。
  - 只有 44% 在离开编辑部后两年内落地，其余中位数约 5 年。
  - 新闻从业 5 年以上的人有 31% 拿到总监级以上职位，2 年内离开的人只有 19%。
  - 该统计排除了公关代理和内部传播岗；作者所在公司 Stacker 本身卖品牌内容，有利益相关。
  - 原话：
    - "If I leave, is the only option communications and public relations?"（离开的话，只能去做传播和公关吗？）
    - 52 岁被裁的编辑说 "I have absolutely zero clue what other jobs my … experience translates to"（完全不知道自己的经验能转去做什么工作）。
- **来源**：
  - Journalism's Most Underreported Career Move — https://humancount.substack.com/p/journalisms-most-underreported-career — HumanCount / 2026-06-09 — ✅
  - r/Journalism 2024-04-26 — https://www.reddit.com/r/Journalism/comments/1cdjjjn/postjournalism_jobs_that_arent_pr/ ；2025-08-31 — https://www.reddit.com/r/Journalism/comments/1n59nxq/laid_off_what_would_you_do/ — ✅（08 语料）

**S9-06 | 全群体 | S9 转型/求职 | — | 凑合方案（行业组织的免费支持）**
- **结论**：被裁后的支持主要来自协会的免费资源，形式是资源页、录播和社群，没有结构化的"技能翻译"或"岗位匹配"。
- **证据**：
  - ONA：给近期被裁者一年免费会员、免费录播求职课（2026-02 有一期 Phoebe Gavin 的课）、Career Center 和 Slack 招聘信息；付费课程会员享折扣。
  - SPJ：上线了"被裁资源"网页。
  - News Revenue Hub：提供"Laid Off to Launch"工具包，引导转做独立媒体。
  - Reddit 上有人用 Teal 改简历，但抱怨工具要求"量化成果"，而记者拿不到这类指标（08 语料，2023-05-04）。
- **来源**：
  - Laid off? ONA is here for you — https://www.journalists.org/laid-off-ona-is-here-for-you — ONA — ✅
  - SPJ — https://www.spj.org/spj-offers-resources-for-journalists-affected-by-layoffs/ — ⚠️（只看了搜索摘要）

**S9-07 | 全群体（FREE、INDIE 尤甚） | S9 安全与法律 | 抗议/调查 | 需求信号 + 市场数据**
- **结论**：抗议现场的拘捕、诽谤诉讼和录音合规是硬风险。员工有雇主的法务托底，自由撰稿人和独立记者只能自付律师和保险，而保险市场在收缩。
- **证据**：
  - 2025 年截至 12-15，美国有 32 起记者被拘或被起诉（2024 年 50 起），近 90% 发生在抗议现场；点名的个案里有 4 位是自由或独立记者。
  - RCFP 热线来电"有所增加"，已增派律师。PEN America 的记者安全紧急热线于 2025-04-30 关闭，是否重启取决于资金。
  - 媒体责任险：$100 万保额年费可达 "$3,500 annually or more"（每年 3,500 美元或更多）；自留额从约 5,000 美元起，调查类至少 10,000 美元。Intact 2023-10 停止承保新单，Dinghy/NSM 2022-12 停止承保。
  - 记者原话（独立调查冤案多年）："I need to consult a media attorney"（我需要咨询媒体律师），但嫌律师报价太高，只好先上 Reddit 求教。
  - 既有数据：01-38、01-39。
- **来源**：
  - Press arrests used to silence protest coverage in 2025 — https://pressfreedomtracker.us/blog/press-arrests-used-to-silence-protest-coverage-in-2025/ — U.S. Press Freedom Tracker / 2025-12-15 — ✅
  - Legal support for journalists is evolving… — https://www.poynter.org/business-work/2025/legal-help-journalists-press-threats-trump-administration/ — Poynter / 2025-05-15 — ✅
  - What freelancers need to know about media liability insurance — https://healthjournalism.org/blog/2023/11/what-freelancers-need-to-know-about-media-liability-insurance/ — AHCJ / 2023-11-27 — ✅
  - r/Journalism 2025-03-14 — https://www.reddit.com/r/Journalism/comments/1jbaq7w/wrongful_conviction_investigation/ — ✅（08 语料）

---

## 2. 自由撰稿人 / 创作者记者：完整工作流

### 2a. 人群底数

**FW-01 | FREE, INDIE | S9 | — | 市场数据 + 需求信号**
- **结论**：自由或独立工作已经是记者的常态身份之一，但自出版很少能单独养活人，所以自由记者普遍要"拼收入"。
- **证据**：
  - Muck Rack 2025（n=1,515）：兼职或偶尔做自由的占 21%，全职自由 19%（G2-01）。Pew 2022：28% 是自由撰稿人或自雇（01-42）。
  - Muck Rack《Creator Journalism 2025》：34% 的记者以个人名义发布内容。这 522 人里：
    - 自出版收入占比为 0 的 39%，低于 10% 的 31%，100% 靠自出版的只有 6%。
    - 78% 的粉丝或订阅数不到 1 万。
    - 发布渠道：个人网站 53%，newsletter 41%，Instagram 30%，LinkedIn 29%。
    - 75% 的人自出版内容和主业题材相近（问卷选项"很相似"45%、"有些不同"30%）。
    - 调查期为 2025-04-04 至 04-30，误差 ±4.3%，多数是美国样本。
    - 报告没有问创作者的痛点，主要篇幅是公关关系。
  - Willnat 等 2026 年的论文对比了 2,133 名美国自由记者（2024 年调查）和 1,600 名全职记者，结论是自由记者是"distinct segment"（独立的群体）。正文无法获取。
- **来源**：
  - The State of Creator Journalism 2025（PDF）— https://media.muckrack.com/documents/10.22.2025_v3_The_State_Of__Creator_Journalism_2025.pdf — Muck Rack / 2025-10 — ✅（全文已读）
  - Similar but not the Same — https://www.tandfonline.com/doi/full/10.1080/17512786.2026.2651415 — Journalism Practice / 2026-03-31 — [未核实]（403，只看到摘要）

### 2b. 找活与投稿（pitch）

**FW-02 | FREE | S9 找活 | 全条线 | 需求信号（一手数据，本轮自行统计）**
- **结论**：自由记者的活主要靠"老关系"，冷投只占四分之一。媒体方几乎不公开投稿指南和稿费，新人缺门路。
- **证据**：FSP 费率库，美国新闻类记录，只算作答者：
  - 稿约来源：已有合作关系 54.9%（393/716）；冷投（"Cold pitch"）26.4%（189/716）。
  - 媒体公开投稿指南：22.1%（120/544）。
  - 媒体公开稿费标准：仅 9.0%（50/557）。
- **来源**：Freelance-Solidarity-Project/Freelancer_Rates_Survey_Analysis（CSV 下载后自算）— https://github.com/Freelance-Solidarity-Project/Freelancer_Rates_Survey_Analysis — NWU FSP / 数据截至 2025-11-05 — ✅

**FW-03 | FREE | S9 找活 | 全条线 | 需求信号（编辑方与记者原话）**
- **结论**：投稿石沉大海是结构性的：编辑变少、来稿太多。记者多半无法分辨"被拒"还是"没被看到"，自信心受损。
- **证据**：
  - 编辑方：People Inc 的 Commerce Editor 每周收到约 300 份投稿；另一位编辑说编辑部 "under-resourced. There are fewer editors than ever"（人手不足，编辑比以往任何时候都少）。
  - 记者方：一名即将毕业的艺术记者投了约 30 份稿，几乎没有回音，原话 "with little to no responses"（几乎没有回复）。另一位长期自由记者说 "Freelancing has killed my self-esteem"（做自由职业毁了我的自信）。
  - 08 语料的 S9 帖子里，"找活/投稿无回音"有 66 条，其中 FREE 58 条。
- **来源**：
  - The Craft: Why did the editor ignore my pitch? — https://pitchfailclub.substack.com/p/the-craft-why-did-the-editor-ignore — Pitch Fail Club / 2026-07-06 — ✅
  - r/Journalism 2026-05-29 — https://www.reddit.com/r/Journalism/comments/1tqxal8/do_editors_just_see_my_email_and_ignore_me/ — ✅（原文已复核）；2026-10-21 — https://www.reddit.com/r/Journalism/comments/1xbsd5u/freelancing_has_killed_my_selfesteem/ — ✅（08 语料）

**FW-04 | FREE | S9 找活 | 商业/B2B | 凑合方案（列举得最完整的一条）**
- **结论**：找"愿意付钱的编辑"目前只能靠手工拼凑多个信息源，而且这些信息源正在过时。
- **证据**：一位 GenAI 出现后失去 B2B 收入的写手，逐项列出自己试过但没用的办法：
  1. Who Pays Writers："About 40 percent of listings no longer paying"（约四成条目已不再付费）。
  2. 各类自由职位板和 newsletter：信息过饱和，且有骗局。
  3. LinkedIn 关键词搜索。
  4. 回头找以前合作过的刊物：已不付费，或改用自有写手。
  5. Google 和 Talkwalker 关键词提醒，再逐个问编辑付不付费。
  6. 从署名反查作者，再找对应刊物。
  7. 问 LLM，"By now I distrust them"（到现在我已经不信任它们了）。
  - 另一名写手说，自己想写的题材"写作数据库都已用尽"，仍找不到付费刊物。
- **来源**：r/freelanceWriters 2026-06-07 — https://www.reddit.com/r/freelanceWriters/comments/1tzgarj/here_is_what_i_have_tried_where_do_i_go_from_here/ — ✅（原文已复核）；2026-06-02 — https://www.reddit.com/r/freelanceWriters/comments/1tuplfj/3_challenging_questions/ — ✅（08 语料）

**FW-05 | FREE | S9 找活 | — | 市场数据（现有付费工具）**
- **结论**：已有几类付费"征稿信息聚合"在做这件事，价格很低（每年 60–199 美元），付费方是撰稿人本人。它们只解决"哪里在征稿"，不解决"谁会回复我、付多少钱"。
- **证据**：
  - Study Hall：Basic / Professional / Premium 分别为每年 $99 / $149 / $199，7 天试用。追踪征稿、全职兼职岗位、fellowship 和资助，号称有 "over 2,500 active commissioning editors"（2,500 多名在职约稿编辑）的数据库。Sonia Weiser 的《Opportunities of the Week》（2018 年创办，原价每月 3 美元）已并入 Study Hall。
  - Inside The Newsroom Freelance Board：1,500 条常青征稿信息，每月 $7 或每年 $60。
  - SPJ Freelance Community：志愿者众包的征稿列表，免费。
- **来源**：
  - https://studyhall.xyz/ — ✅
  - https://insidethenewsroom.ghost.io/freelance-board/ — ✅
  - https://soniaweiser.wordpress.com/opportunities-of-the-week-newsletter/ — ⚠️（只看了搜索摘要）
  - https://www.spj.org/freelance-opportunity-pitching-guidelines-and-open-calls/ — ⚠️（只看了搜索摘要）

### 2c. 谈价与费率透明度

**FW-06 | FREE | S9 谈价 | 全条线 | 需求信号（一手数据，本轮自行统计）**
- **结论**：美国新闻类自由稿的每词费率中位数约 0.50 美元，2019–2025 年基本没涨；近一半低于 0.50 美元。
- **证据**：FSP 美国新闻类记录中可算每词费率的 659 条：
  - 中位数 $0.50，均值 $0.59。
  - 分布：<$0.25 占 16.7%，$0.25–0.49 占 31.7%，$0.50–0.99 占 29.9%，≥$1 占 21.7%。
  - 按年份的中位数：2019 年 $0.39，2020 年 $0.50，2021 年 $0.35，2022 年 $0.42，2023 年 $0.50，2024 年 $0.50，2025 年 $0.50。
  - **口径冲突**：The Objective 转述同一数据库"平均约 $1/词"（G2-03）。我用原始 CSV 算出的全库均值是 $0.63、中位数 $0.50，与 $1 不符，原因不明（可能是早期版本或口径不同）。**以原始数据为准，G2-03 中的"$1/词"应下调。**
  - 原话：一位 11 年资历的体育记者说，稿酬从固定稿费变成 "a $4/1000 views model"（每千次浏览 4 美元）。
- **来源**：同 FW-02 — ✅；The Objective — https://www.objectivejournalism.org/p/freelance-journalism-rates-are-worse-than-you-think-theyve-barely-changed-since-2000 — 2026-09-28 — ✅；r/freelanceWriters 2025-12-04 — https://www.reddit.com/r/freelanceWriters/comments/1pdmsww/sportswriting_is_dying/ — ✅（08 语料）

**FW-07 | FREE | S9 谈价 | — | 凑合方案 + 工具状态**
- **结论**：费率透明靠众包数据库，但这些库大多维护不善：样本少、数据过时，覆盖主要是全国性大刊。
- **证据**：
  - Who Pays Writers 首页写明由 FSP 托管，"正在开发新的费率共享落地页"。2026-11-03 访问时站点 **SSL 证书已过期**，页面是 JS 应用，看不到数据。
  - 一名写手实测约 40% 的条目已不再付费（FW-04）。
  - FSP 自 2020 年起只积累了 1,275 条；Freelancing Females 2025 年的目标是收集 1 万条费率。
  - 2020 年的旧证据（F-04）显示，撰稿人怕"被编辑另眼相看"，不敢公开分享费率。
  - 英国数据（F-05）：只有 26% 经常议价。
- **来源**：http://whopayswriters.com/ — ✅（证书过期，curl -k 读取）；https://nwu.org/freelance-solidarity-project/rate-sharing/ — ⚠️（只看了摘要）；https://freelancingfemales.com/rates — ⚠️（只看了摘要）

### 2d. 合同、版权与 AI 授权

**FW-08 | FREE | S9 合同/版权 | 全条线 | 需求信号（一手数据，本轮自行统计）**
- **结论**：四分之一的稿约没有书面合同，近四成撰稿人不清楚自己让渡了什么版权，三成不知道有没有 kill fee。范围扩大、差旅垫付不补偿的情况，在发生过这类事的样本里占近一半。
- **证据**：FSP 美国新闻类，只算作答者：
  - 合同：有书面合同 69.8%（462/662）；无合同或口头约定 26.1%（173/662）。
  - 版权：不确定 38.4%；work-for-hire（雇佣作品，版权归委托方）33.2%；首发权 21.9%（分母 599）。
  - Kill fee：有约定 35.4%；不确定 29.4%（分母 599）。
  - 工作范围扩大但没加钱：47/89。
  - 需要垫付差旅等费用但没报销：49/107。
- **来源**：同 FW-02 — ✅

**FW-09 | FREE | S9 版权/AI 授权 | — | 需求信号（调查，英国）+ 市场数据**
- **结论**：自由记者希望自己的作品被 AI 使用时"先同意、再付钱"。但现有的 AI 授权平台和合同范本只覆盖图书，单篇稿件的授权是空白。版权方面的凑合办法只能是举报或自费维权。
- **证据**：
  - NUJ 和 ALCS 调查了 414 名记者（多为英国）：60% 认为只有明确同意后才能授权给 AI 训练和推理；29% 查过自己的作品是否进了训练集，21% 发现确实被用了；59% 倾向集体授权。
  - Created by Humans：面向 "books and other written works"（图书及其他书面作品）的 AI 授权市场，状态为上线中，没有提到新闻稿件。
  - Authors Guild 的 AI 合同条款范本只针对图书出版合同。
  - 美国个案：一名自由撰稿人发现报社体育编辑抄袭了自己已发表的段落，原话 "COPIED several paragraphs"（照抄了好几段）。他只能向编辑、Google 和 ISP 举报。
  - 美国作者整体诉求见 F-06：96% 要求征得同意并付费。
- **来源**：
  - Freelance journalists want to get paid for AI using their work — https://pressgazette.co.uk/news/freelance-journalists-want-control-over-ai-using-their-work-survey-reveals/ — Press Gazette / 2025-10-21 — ✅（英国样本）
  - https://datalicenses.org/initiatives/created-by-humans/ — ✅
  - https://authorsguild.org/advocacy/artificial-intelligence/ai-model-clauses/ — ✅
  - r/Journalism 2025-11-22 — https://www.reddit.com/r/Journalism/comments/1p3ijq8/copyright_infringement_and_plagarism/ — ✅（08 语料）

### 2e. 交付：AI 检测误判

**FW-10 | FREE | S9 交付 | 内容/商业 | 需求信号（原话）+ 第三方测试**
- **结论**：委托方用 AI 检测器验收，人写的稿也可能被判为 AI，进而被拒付或解约。撰稿人没有申辩手段，只能故意加错字、换检测器、保留版本记录。不同检测器的结果差异巨大。
- **证据**：
  - Authors Guild 2026-05 把 10 篇 2022 年以前的人写文章交给 5 个检测器：
    - Pangram 全部判 0%；Originality.ai 8 篇 0%、2 篇 1%；Grammarly 最高 9%。
    - ZeroGPT 判出 5.3%–76.3%。
    - Sidekicker 全部判为 71%–100%。
    - Authors Guild 的建议原文："Publishers should never cancel a contract … on the basis of … these tools alone"（出版方绝不应仅凭这些工具就取消合同）。
  - 08 语料中"AI 检测误判"有 24 条，全部来自 FREE。原话举例：
    - "the client refuses to pay me because they've decided to use OriginalityAI"（客户决定用 OriginalityAI 检测后拒绝付款）。
    - "I had to … add typos to make it sound like human generated"（我只好故意加错字，让它看起来像人写的）。
- **来源**：
  - Can AI Detectors Be Trusted? — https://authorsguild.org/news/can-ai-detectors-be-trusted/ — Authors Guild / 2026-05-26 — ✅
  - r/freelanceWriters 2023-06-03 — https://www.reddit.com/r/freelanceWriters/comments/13zd90b/client_refusing_to_pay_because_of_ai_detector/ ；2023-03-29 — https://www.reddit.com/r/freelanceWriters/comments/125thz2/has_anybody_came_across_unreliability_of_ai/ — ✅（08 语料；多为 2023 年，且主要是内容写手而非新闻记者）

### 2f. 开票与收款

**FW-11 | FREE | S9 收款 | 全条线 | 需求信号（一手数据，本轮自行统计）**
- **结论**：新闻类稿费约七成能在 30 天内到账，但每 7 笔就有 1 笔拖到 6 周以上或拿不到。另有 14% 的记录在填报时"还在等"。
- **证据**：FSP 美国新闻类，n=692：
  - ≤2 周到账 34.5%；30 天 36.3%。
  - 6 周、2 个月、3 个月、3 个月以上或从未付款，合计 15.0%。
  - 新稿仍在等 14.2%。
  - 拖欠的普遍程度和追款耗时见 F-01：91% 遇到过拖欠，79% 自己发邮件或打电话追，76% 每周花 1–2 小时追款。
- **来源**：同 FW-02 — ✅

**FW-12 | FREE | S9 收款 | — | 需求信号（制度性求助行为）+ 凑合方案**
- **结论**：即使有法律托底，追款效果也有限：在纽约市投诉后，约一半人仍然一分钱没拿到。媒体公司是被集体投诉的对象之一。
- **证据**：
  - 纽约市 Freelance Isn't Free 法 FY2019–2023：共收到 2,542 起投诉，其中 2,184 起涉及拖欠或不付款。
  - 至少 773 人追回了钱，合计 291 万美元（自报，实际可能更高）。
  - 回访调查（n=263）：全额拿到 40%，部分拿到 9%，**完全没拿到 49%**；投诉后又走法院的占 16%。
  - 51% 的投诉合同金额不超过 5,000 美元。
  - 市政府起诉媒体公司 L'Officiel USA：投诉人包括撰稿人、编辑和摄影师，2023 年和解，向 41 人支付超过 27.5 万美元（双倍赔偿）。
  - 同类立法已在伊利诺伊、加州、纽约州和俄亥俄州 Columbus 通过（The Objective）。
  - 原话："after 3 or 4 followup emails … absolutely no response"（发了三四封催款邮件，完全没有回音）；"I have never once been paid on time"（我从来没有一次按时收到过钱）。
- **来源**：
  - 5-Year Report on NYC's Freelance Isn't Free Act（PDF）— https://www.nyc.gov/assets/dca/downloads/pdf/workers/DCWP-Freelance-Isnt-Free-Act-Five-YearReport-2023.pdf — NYC DCWP / 2023-11-01 — ✅（全文已读）
  - r/freelanceWriters 2026-06-04 — https://www.reddit.com/r/freelanceWriters/comments/1tws8wn/paymentfollowup_advice_after_potentially_being/ — ✅（08 语料）

**FW-13 | FREE | S9 收款/合同 | — | 市场数据（工具）**
- **结论**：开票、合同和追款都有现成工具，但要么是通用的自由职业 SaaS，要么是工会的人工服务，没有专门面向"对接媒体应付账款流程"的工具。
- **证据**：
  - Bonsai：开票和合同功能从 Essentials 档起步（年付每月 $19），各档每月 $9–$59。
  - Freelancers Union Contract Creator：2024-05 上线，免费，Beta 版。
  - NWU 申诉部门：由非律师的申诉官协助写催款函，累计追回 150 万美元以上。案例包括 Nautilus 拖欠 20 名自由撰稿人 6 万多美元，最终和解。需要会员身份，和 NASW 合作的会费是 $150。
- **来源**：
  - https://www.hellobonsai.com/pricing — ✅
  - https://blog.freelancersunion.org/2024/05/14/introducing-the-freelancers-union-contract-creator/ — ✅
  - https://nwu.org/grievances/ — ✅
  - https://nycclc.org/news/nwu-and-nautilus-settle-60000-non-payment-grievance — ⚠️（只看了搜索摘要）
  - https://www.nasw.org/article/have-dispute-publisher-or-client-nasw-nwu-partnership-can-help — ⚠️（只看了搜索摘要）

### 2g. 作品集与个人品牌

**FW-14 | FREE, INDIE | S9 作品集 | — | 需求信号 + 市场数据**
- **结论**：作品集是求职和投稿的"通行证"，但已发表的稿件可能被刊物删掉，导致作品集断链。自动归档类工具就是为此收费的。
- **证据**：
  - 原话："articles that don't drive traffic just take up space on my server"（不带流量的文章只是占我服务器空间）。一名撰稿人供稿两年的网站以此为由删掉了他的全部文章，求职作品集随之丢失。
  - 应届生只能靠无偿写稿攒剪报："continue to write … for free to keep gaining clips"（继续免费写稿以积累剪报）。
  - 08 语料中"作品集/个人品牌"有 45 条，FREE 占 36 条。
  - 工具：
    - Muck Rack 个人主页和作品集对记者"永久免费"，认证记者还能用媒体数据库；收入来自约 6,000 家公关客户。
    - Authory：免费档 10 篇；付费档年付每月 $9 / $15 / $24，Standard 起自动导入历史和新发表的稿件并备份。
- **来源**：
  - r/Journalism 2024-11-18 — https://www.reddit.com/r/Journalism/comments/1gu4i0a/publication_i_wrote_for_deleted_my_articles/ ；2026-05-11 — https://www.reddit.com/r/Journalism/comments/1tajin9/am_i_doing_the_right_thing_for_my_career/ — ✅（08 语料）
  - https://muckrack.com/blog/free-journalist-resources — 2026-10-08 更新 — ✅
  - https://authory.com/pricing — ✅

### 2h. 多收入来源与 AI 抢活

**FW-15 | FREE | S9 收入 | 商业/内容 | 需求信号（大样本研究）+ 原话**
- **结论**：AI 主要冲击的是"写作外包市场"的低端，而不是新闻稿约本身。但大量自由记者靠商业写作补贴收入，这块收入正在塌陷。
- **证据**：
  - Demirci、Hannane、Zhu（Management Science，2025-10）：ChatGPT 推出后 8 个月内，某全球自由职业平台上写作和编程类岗位的发布量相对减少 21%；剩下的岗位更复杂、报酬更高，但竞争加剧。图像类岗位减少 17%。
  - 原话：
    - "I lost everything with GenAI"（GenAI 让我失去了一切）。
    - "My best paying job - $2k a month … is gone"（我报酬最高的活，每月 2,000 美元，没了）。
    - 有同行靠"AI 灌水稿"抢流量拿高收入："I'm making way less money than several colleagues who crank out AI slop"（我比几个整天产出 AI 垃圾稿的同事挣得少得多）。
  - 08 语料中"AI 抢活/降价"有 28 条，FREE 占 19 条。
  - 补贴收入的常见去处：
    - 品牌内容：Contently 起价为短文 $300、报道型文章 $595、长报告 $1,250。
    - 给 AI 做标注和评测（G2-04）。
    - 书以外的写作（F-07）。
- **来源**：
  - Who Is AI Replacing? — https://spiral.imperial.ac.uk/entities/publication/88113a91-b994-4717-8526-dadac657f1cb （摘要）；Crossref 10.1287/mnsc.2024.05420 — ✅
  - r/freelanceWriters 2026-01-08 — https://www.reddit.com/r/freelanceWriters/comments/1q771ww/returning_business_writer_whats_your_advice/ ；2026-10-15 — https://www.reddit.com/r/freelanceWriters/comments/1x6ab5u/well_it_happened/ ；r/Journalism 2026-03-10 — https://www.reddit.com/r/Journalism/comments/1rq0y6p/getting_smoked_by_my_colleagues_who_publish_ai/ — ✅（08 语料）
  - https://support.contently.com/article/740-how-much-will-i-be-paid — ✅

---

## 3. 08 号 Reddit 语料中 S9 帖子的子主题分布（本轮二次归类）

- **口径**：08 号编码语料里 stage 含 S9 的帖子共 1,000 条（2023 年起）。
- **方法**：对 pain、workaround、quote 三个字段做关键词匹配，一帖可以落入多个主题。
- **用途**：只能用于比较各主题的相对多少，不代表记者总体。

| 子主题 | 帖数 | FREE | TV | LOCAL | NATL | INDIE |
|---|---|---|---|---|---|---|
| 转行/转型（含公关、内容岗） | 234 | 97 | 68 | 26 | 17 | 12 |
| 裁员/失业/求职 | 181 | 56 | 50 | 46 | 16 | 3 |
| 技能/培训/学位 | 113 | 52 | 15 | 10 | 8 | 1 |
| 薪资/福利 | 111 | 31 | 33 | 22 | 13 | 3 |
| 费率/低价/谈价 | 91 | 82 | 4 | 3 | 0 | 4 |
| 倦怠/心理 | 78 | 18 | 21 | 24 | 6 | 1 |
| 找活/投稿无回音 | 66 | 58 | 4 | 8 | 3 | 2 |
| 合同/版权 | 45 | 25 | 11 | 4 | 3 | 2 |
| 作品集/个人品牌 | 45 | 36 | 5 | 2 | 1 | 0 |
| 安全/法律/骚扰 | 30 | 11 | 6 | 4 | 6 | 4 |
| AI 抢活/降价 | 28 | 19 | 6 | 3 | 0 | 0 |
| AI 检测误判 | 24 | 24 | 0 | 0 | 0 | 0 |
| 拖欠/收款 | 22 | 21 | 0 | 0 | 0 | 2 |
| 税务/保险/行政 | 11 | 9 | 0 | 0 | 3 | 1 |

- **读法**：
  - 在职记者（TV、LOCAL）的 S9 帖子集中在"想走、走不了"：转行、裁员和求职、薪资。
  - 自由撰稿人集中在费率、找活和作品集。
  - "拖欠"在帖子数上并不突出，但调查数据显示它非常普遍（F-01、FW-11）。可能是因为太普遍，大家不再发帖。

---

## 4. 自由撰稿人工作流 × 痛点 × 凑合方案 × 可解决度

| 环节 | 核心痛点 | 现有凑合方案 | 费力/漏/门槛 | 判定 | 证据 |
|---|---|---|---|---|---|
| 找活：哪里在征稿 | 征稿信息分散，大量过时或不付费 | Study Hall、Inside the Newsroom、SPJ 列表、Google/Talkwalker 提醒、LinkedIn | 每年 $60–199，信息过饱和且有骗局，要逐条核实付不付费 | ⚠️ | FW-04, FW-05 |
| 找活：联系谁、对方会不会回 | 编辑每周约 300 份来稿；只有 22% 公开投稿指南；冷投只占 26% | 靠老关系、托公关人员要编辑邮箱、发一次跟进后换家投 | 新人无门路，无法区分"被拒"和"没被看到" | ❌ | FW-02, FW-03 |
| 谈价 | 只有 9% 公开稿费；中位数 $0.50/词且多年不涨 | 众包费率库（FSP、Who Pays Writers、Freelancing Females）、私下社群 | 样本少、数据过时，Who Pays Writers 站点证书过期；怕被报复 | ❌ | FW-06, FW-07, F-04 |
| 合同与版权 | 26% 无书面合同；38% 不清楚版权归属；AI 授权条款无从谈起 | Freelancers Union 免费合同生成器、NWU、Authors Guild 范本（仅图书） | 媒体合同多为对方模板，"不可修改"；单篇稿件 AI 授权没有市场 | ❌ | FW-08, FW-09 |
| 交付与验收 | AI 检测误判导致拒付或解约 | 保留版本历史、换检测器自证、故意加错字 | 检测器之间差距可达 0% 对 100%，没有申诉渠道 | ❌ | FW-10 |
| 开票与收款 | 15% 拖到 6 周以上或拿不到；追款每周 1–2 小时 | 自己发邮件追；纽约市 DCWP 投诉；NWU 申诉；小额法庭 | 投诉后 49% 仍拿不到；法律保护只覆盖少数州和城市 | ⚠️（有工具但收效有限） | FW-11, FW-12, F-01 |
| 开票工具 | 记账、发票、提醒 | Bonsai、Wave 等通用 SaaS（每月 $9–59） | 工具成熟；真正的瓶颈在对方应付账款流程，不在开票 | ✅ | FW-13 |
| 差旅与费用 | 46% 需要垫付的记录没报销；最长拖一年 | 谈预付款、在发票里加利息 | 依赖个人议价能力 | ⚠️ | FW-08, G2-06 |
| 作品集 | 刊物删稿导致作品集断链；应届生靠无偿写稿攒剪报 | Muck Rack（免费）、Authory 自动归档（每月 $9–29）、Clippings.me、个人网站 | 工具成熟 | ✅ | FW-14 |
| 个人品牌与自出版 | 78% 粉丝不到 1 万；39% 自出版零收入 | 个人网站、newsletter、LinkedIn | 增长难，变现更难（见 S8 相关文件） | ⚠️ | FW-01 |
| 多收入来源 | 商业写作被 AI 挤压（发布量 -21%） | 品牌内容、AI 标注、教学 | 收入下降、时薪下降 | ❌ | FW-15, G2-04 |
| 法律与安全 | 诽谤风险、录音合规、抗议现场被拘 | RCFP 热线（免费）、自费买媒体责任险（$100 万保额每年约 $3,500 起） | 保险商在退出市场，律师贵 | ❌ | S9-07 |

---

## 5. 竞品/工具表（S9 与自由撰稿人工作流）

| 工具/机构 | 解决什么 | 群体 | 价格 / 付费方 | 状态 | 来源 |
|---|---|---|---|---|---|
| Muck Rack（记者端） | 个人主页和作品集、稿件发表提醒、媒体人事变动、职位板（每周人工更新两次）、认证记者可用媒体数据库 | 全群体 | 对记者"永久免费"；由约 6,000 家公关客户付费 | 活跃，2026-10 仍在更新 | https://muckrack.com/blog/free-journalist-resources ✅；https://help.muckrack.com/en/articles/10249309-muck-rack-job-board ⚠️ |
| JournalismJobs.com | 媒体招聘职位板 | 全群体（求职方） | 雇主付费：单条 $100（挂 5 周），有套餐；求职者免费 | 活跃，1998 年起 | https://www.journalismjobs.com/post-new-job ✅ |
| ONA 被裁支持 | 被裁者一年免费会员、求职录播课、Career Center、Slack | 在职转型 | 免费（协会出资） | 活跃 | https://www.journalists.org/laid-off-ona-is-here-for-you ✅ |
| Study Hall | 征稿、职位、fellowship 聚合；2,500 多名约稿编辑数据库；已并入 Opportunities of the Week | FREE | 撰稿人付费：每年 $99 / $149 / $199 | 活跃 | https://studyhall.xyz/ ✅ |
| Inside The Newsroom Freelance Board | 1,500 条常青征稿信息 | FREE | 撰稿人付费：每月 $7 或每年 $60 | 活跃 | https://insidethenewsroom.ghost.io/freelance-board/ ✅ |
| SPJ 征稿列表 | 志愿者众包的征稿和投稿指南 | FREE | 免费 | 状态未核实 | https://www.spj.org/freelance-opportunity-pitching-guidelines-and-open-calls/ ⚠️ |
| PitchWhiz | 自由撰稿人目录，供编辑找写手 | FREE | 未知 | 页面无内容 | https://pitchwhiz.com/subscription [未核实] |
| Who Pays Writers | 匿名众包的各刊稿费 | FREE | 免费 | **失修**：SSL 证书过期，约四成条目已不付费，FSP 称在做新页面 | http://whopayswriters.com/ ✅；FW-04 |
| NWU FSP 费率库 | 匿名费率填报，原始数据公开在 GitHub | FREE | 免费（工会运营） | 活跃，但样本只有 1,275 条 | GitHub ✅ |
| Freelancing Females 费率库 | 跨行业自由职业费率计算器 | FREE（非新闻专属） | 免费 | 状态未核实 | https://freelancingfemales.com/rates ⚠️ |
| Contently | 品牌内容写作接单网络 | FREE（副业） | 品牌方付费；短文起价 $300，长报告起价 $1,250 | 活跃 | https://support.contently.com/article/740-how-much-will-i-be-paid ✅ |
| Authory | 自动导入历史和新发表的稿件并备份，生成作品集 | FREE、INDIE | 撰稿人付费：免费档 10 篇；付费档年付每月 $9 / $15 / $24 | 活跃 | https://authory.com/pricing ✅ |
| Clippings.me | 作品集建站，号称 10 万多用户 | FREE | 有免费档；Pro 价格未核实（旧报道称每月 $8） | 有 Cloudflare 防护，状态未核实 | https://www.clippings.me/ ⚠️ |
| Bonsai | 合同、发票、收款（通用自由职业 SaaS） | FREE | 每月 $9–$59，开票功能从年付每月 $19 档起 | 活跃 | https://www.hellobonsai.com/pricing ✅ |
| Freelancers Union | 免费合同生成器、推动 Freelance Isn't Free 立法、健康保险渠道 | FREE | 免费 | 活跃；合同生成器 2024-05 上线 Beta | https://blog.freelancersunion.org/2024/05/14/introducing-the-freelancers-union-contract-creator/ ✅ |
| NYC DCWP Navigation Program | 拖欠投诉、通知雇主、法律转介 | FREE（仅纽约市） | 免费（政府） | 活跃；5 年 2,542 起投诉 | DCWP 5 年报告 ✅ |
| NWU 申诉部门 | 申诉官代写催款函和谈判 | FREE | 需会员（NASW 合作价 $150） | 活跃；累计追回 150 万美元以上 | https://nwu.org/grievances/ ✅ |
| Authors Guild | AI 检测器测试、AI 合同条款范本、会员法律援助 | FREE（偏图书作者） | 会员制 | 活跃；范本只覆盖图书 | authorsguild.org ✅ |
| Created by Humans | 图书和书面作品的 AI 授权市场 | 作者（未覆盖新闻稿件） | AI 开发者付费（分成未公开） | 上线中 | datalicenses.org ✅ |
| RCFP 法律热线 | 免费法律咨询、出庭代理、Local Legal Initiative | 全群体 | 免费（基金会资助） | 活跃，来电增加 | Poynter 2025 ✅ |
| PEN America 记者安全紧急热线 | 安全事件紧急求助 | 全群体 | 免费 | **2025-04-30 关闭**，视资金再定 | Poynter 2025 ✅ |
| 媒体责任险（AXIS、Chubb、CapSpecialty 等） | 诽谤、隐私、版权诉讼的费用 | FREE、INDIE | 自付：$100 万保额每年约 $3,500 起，自留额 $5,000–10,000 起 | 市场收缩，有保险商停止承保新单 | AHCJ 2023 ✅ |
| CPJ 安全培训 | 数字和人身安全培训 | 全群体 | 免费 | 2025 年在美国约 1,000 人参加，需求激增（01-39） | 01-39 ✅ |

---

## 6. 能自己解决 / 不好解决

**✅ 能自己方便解决**
- 作品集托管与备份：Muck Rack 免费，Authory 每月几美元。
- 开票与记账：Bonsai、Wave 等通用工具。
- 起草合同：Freelancers Union 免费生成器。
- 被裁后获取基础资源：ONA、SPJ 免费资源。

**⚠️ 费力但能**
- 找"哪里在征稿"：付费 newsletter 加关键词提醒，要逐条核实是否付费。
- 追讨拖欠：发邮件和电话追，纽约市可以投诉，NWU 会员可以申诉；但约一半人追不回。
- 差旅垫付：靠个人议价。
- 转型去企业内容岗：可行，但慢（中位数约 5 年），而且偏向资深者。

**❌ 不好解决**
- **找到"会回复、会付钱"的具体编辑**：冷投成功率低，编辑人手少，信息只在老关系里流通。
- **费率透明**：只有 9% 的媒体公开稿费，众包库样本少且失修。
- **版权与 AI 授权**：近四成撰稿人不清楚版权归属；单篇稿件的 AI 授权没有市场。
- **AI 检测误判的申诉**：没有统一标准，委托方单方面认定。
- **商业写作收入被 AI 挤压**：属于结构性下降。
- **法律风险托底**：保险贵且在收缩，律师贵，热线人手有限。
- **在职记者的低薪、倦怠和"走不了"**：这是组织和行业层面的问题，个人工具难以改变。

## 7. 最重要的 5 条发现

1. **自由记者的活约 55% 来自老关系，冷投只占 26%；只有 22% 的媒体公开投稿指南，9% 公开稿费。** 找活的核心难点不是"不知道有哪些刊物"，而是"不知道谁会回、付多少"。现有工具（Study Hall、Inside the Newsroom、Who Pays Writers）只解决前半段，而且 Who Pays Writers 已经失修（证书过期，约四成条目不再付费）。（FW-02、FW-03、FW-04、FW-07）
2. **稿费中位数约 $0.50/词，2019–2025 年没有上涨，近半数低于 $0.50。** 用 FSP 原始数据算出的结果低于此前转述的"$1/词"，G2-03 需要更正。（FW-06）
3. **收款问题有法律、有工具，仍然收效有限。** 纽约市 5 年 2,542 起投诉，投诉后 49% 一分钱没拿到；新闻稿约有 15% 拖到 6 周以上或拿不到。瓶颈在对方的应付账款流程，以及个人执法成本高，不在开票本身。（FW-11、FW-12）
4. **合同和版权处在"糊涂账"状态。** 26% 没有书面合同，38% 不清楚版权归属，29% 不知道有没有 kill fee；AI 授权市场只覆盖图书。自由记者在 AI 时代的授权和补偿诉求（60% 要求先同意）没有落地渠道。（FW-08、FW-09）
5. **在职记者的 S9 声量主要是"想走、走不了"。** 在 Reddit S9 帖子里，转行和求职类在各子主题中最多。真实的流出路径（企业内容岗）慢且偏向资深者。同时裁员在 2026 年再次加速，集团已明确以 AI 和自动化为理由（Scripps、TEGNA）。（S9-01、S9-02、S9-05、第 3 节）

## 8. 证据薄弱处

- **美国自由记者大样本调查**：Willnat 等 2,133 人的论文、CISLM《Stayers and Leavers》都只拿到摘要。美国自由记者"找活渠道、投稿回复率、收入构成"的有方法论数据仍然缺失，目前靠 FSP 自愿填报数据加英国调查（F-05）补位。
- **投稿回复率**：没有找到任何系统统计，只有编辑和记者的原话（每周约 300 份来稿）。
- **AI 抢活和 AI 检测**的原话主要来自内容和 SEO 写手，新闻记者本身受影响的程度没有量化。Demirci 研究的对象是全球外包平台，不是新闻稿约。
- **工具的使用量和付费转化**：Study Hall、Authory、Muck Rack 等的用户数和付费人数都没有公开（Clippings.me 自称 10 万多用户，未核实）。
- **在职记者薪资**：BLS 页面 403，没能更新；薪资透明度只有 JD 中 40% 披露薪资区间这一条（04 B 部分）。
- **安全与法律**：缺"自由记者 vs 员工"在法律支持上的对比数据。RCFP 热线来电增幅没有给出具体数字。
