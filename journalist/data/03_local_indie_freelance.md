# 03 · LOCAL / INDIE / FREE：九环节需求取证与"条线 × 信息来源难度"

## 0. 文件说明

- **覆盖群体**：LOCAL（地方条线记者）、INDIE（独立/超本地/小型非营利）、FREE（自由撰稿人与学生记者）。
- **覆盖环节**：S1–S9 都有证据。S1（发现线索）、S2（背景研究）、S8（受众与变现）、S9（职业与生存）证据最多；S5（核实）和 S6（写作）只有间接证据。
- **来源数**：约 49 个独立 URL，全部用 WebFetch 实际打开过（其中 3 份 PDF 下载到本地后用 pypdf 抽取了全文）。正文共 51 条发现：LOCAL 28 条、INDIE 11 条、FREE 12 条（自由撰稿人 7 条、学生记者 5 条）。
- **主要局限**：
  1. 本轮的 WebSearch 配额（200 次）在取证后期用完。商业/地产条线、本地招聘 JD、Who Pays Writers 原始数据、美国本土的自由撰稿人 AI 影响数据，都没能继续搜。这些放在第 4 节"证据薄弱处"。
  2. 有几份核心原始报告打不开，只能用二手报道：INN Index 官网返回 403，改用 Nieman Lab 的报道；Axios 关于 Patch 的报道返回 403，改用 CJR；tandfonline 上的美国自由撰稿人论文返回 403，已弃用。
  3. 部分证据早于 2023 年，比如 AHCJ 2016、SEJ 2018、City Bureau 2018、Agenda Watch 2020、EWA 2021。每条都标了年份，只用来补背景，不作为主证据。
  4. 自由撰稿人中最完整的收入和费率调查来自英国（Sheffield Hallam，401 人），条目里已明确标出"非美国"。
- **类型标注**：需求信号 = 记者本人表达或已发生的行为；市场数据 = 规模和结构，不算需求证据；凑合方案 = 现在实际怎么解决；竞品事实 = 已有工具或服务的做法。

---

## 1. LOCAL（地方条线记者）

### L-01 | LOCAL | S9 / 全局 | 市场数据
- **结论**：地方新闻供给持续萎缩，"新闻荒漠"县数量创新高，而且每年仍有一百多家报纸关停。
- **证据**：Medill 2025 年报告统计到 213 个新闻荒漠县（上一年 206 个），另有 1,524 个县只剩一个新闻源。过去一年关停报纸 136 家，原文 "a rate of more than two per week"（意思是平均每周关停两家以上）。报业岗位过去一年减少 7%，自 2005 年以来减少超过四分之三。过去 5 年新出现 300 多家本地新闻创业公司，其中 80% 是纯数字媒体，大多在大都市区。
- **来源**：News deserts hit new high… — https://www.medill.northwestern.edu/news/2025/news-deserts-hit-new-high-and-50-million-have-limited-access-to-local-news-study-finds.html — Medill / 2025-10 — ✅已访问

### L-02 | LOCAL | S1 / S9 | 市场数据
- **结论**：按"记者人数"算，缺口比按"媒体数量"算更大。全美约三分之一的县连 1 名全职本地记者的工作量都没有。
- **证据**：Local Journalist Index 2025（Rebuild Local News 与 Muck Rack 合作）显示，3,141 个县中有 1,000 多个县 "do not have the equivalent of even one full-time local journalist"（连一名全职本地记者的工作量都没有）。全国平均每 10 万人 8.2 名本地记者，2002 年约为 40 名。大县同样严重不足：Maricopa 县每 10 万人 2.9 名，洛杉矶县 3.6 名，Harris 县 3.9 名。方法局限：数据取自 Muck Rack 数据库 2025 年第一季度，不含没有网站的纸媒，可能少算 Substack 作者。
- **来源**：New report maps a severe shortage of local journalists — https://www.niemanlab.org/2025/07/new-report-maps-a-severe-shortage-of-local-journalists-in-the-u-s/ — Nieman Lab / 2025-07 — ✅；Journalist Deserts — https://localnewsinitiative.northwestern.edu/posts/2025/07/10/local-journalist-index-rebuild-local-news-muck-rack/index.html — Medill LNI / 2025-07-10 — ✅

### L-03 | LOCAL | S1 | 市场数据（附研究者原话）
- **结论**：研究者直接把记者减少和"校董会、市政府没人盯"联系在一起。
- **证据**：报道说镇议会、校董会和市政府这类地方报道越来越难以维持。Muck Rack 的 Albasi 说，没有本地记者的地方，居民可能不知道 "what's going on with their school board, their local government"（校董会和地方政府在发生什么）。
- **来源**：Deseret News 对 LJI 的报道 — https://www.deseret.com/the-west/2025/07/23/local-journalism-steep-decline/ — Deseret News / 2025-07-23 — ✅

### L-04 | LOCAL | S1 | 需求信号（有方法论的访谈）
- **结论**：地方记者发现线索的主要办法是会前逐个手动扫议程，人手不够时会漏掉重大事件。
- **证据**：斯坦福团队访谈了北加州中小媒体的记者，发现 "many local journalists look at agendas from committees related to their beats prior to a meeting"（很多地方记者会在开会前翻看与自己条线相关的委员会议程）。有记者提到一起"差点漏掉"的校董会丑闻，原因是没有人手去参加小委员会的会议。另一位记者说，6 个人的编辑部要覆盖一大片乡村地区。研究给出的工作量参考：仅圣何塞一个城市，每两周发布 17–26 份议程，涉及 11–19 个委员会。（2020 年，较老）
- **来源**：Agenda Watch: personalized email alerts for public meetings（C+J 2020 论文）— https://cj2021.northeastern.edu/files/2019/11/CJ_2020_paper_69.pdf — Stanford / 2020 — ✅（PDF 已下载并抽取全文）

### L-05 | LOCAL | S1 | 需求信号 / 凑合方案
- **结论**：会议太多、蹲不过来，是新闻业内部公开承认的痛点。传统解法就是熬夜坐在会场里等议题出现。
- **证据**：RJI 和 Big Local News 发布 Agenda Watch 时写道 "many of us have missed important public meetings because there simply are too many to cover"（我们很多人错过过重要的公开会议，因为会议实在太多，跑不过来），还说记者常常在市议会和校董会熬到深夜。项目整理出 9 万多个机构站点，但上线时只支持 CivicPlus 一个平台、四个地区。
- **来源**：Welcome to Agenda Watch — https://rjionline.org/news/welcome-to-agenda-watch/ — RJI / 2023-06-23 — ✅

### L-06 | LOCAL / INDIE | S1 / S4 | 需求信号（已发生的使用行为）
- **结论**：非营利新闻机构用 AI 时，排第一的用途是"会议转写和摘要"，远远超过用 AI 写稿。
- **证据**：INN Index 2026 调查了 412 家机构（占会员的 93%），81% 在用 AI 工具。具体用途：会议摘要和转写 60%，数据分析 36%，抓取网站数据 13%，写资助申请 18%。
- **来源**：AI use, growth, challenges and funding cuts… — https://niemanlab.org/2026/06/ai-use-growth-challenges-and-funding-cuts-a-new-report-looks-at-the-state-of-nonprofit-news — Nieman Lab / 2026-06 — ✅（INN 官网 https://inn.org/research/inn-index/2025-index/ 返回 403 ❌）

### L-07 | LOCAL / INDIE | S4 / S6 | 需求信号（使用行为）
- **结论**：上一年的数据也一样：转写最常用，用 AI 起草稿件的很少。AI 的价值集中在"处理素材"，而不是"替记者写"。
- **证据**：INN Index 2025 调查了 407 家中的 376 家。63% 在用 AI（2023 年为 34%）。用途：采访转写 67%，数据分析 38%，用于资助和募款相关工作 47%，起草稿件只有 6%，编辑稿件 16%。本地机构占会员的 51%。
- **来源**：Nonprofit news is growing strong… — https://www.niemanlab.org/2025/10/nonprofit-news-is-growing-strong-especially-local-nonprofit-news-a-new-report-shows/ — Nieman Lab / 2025-10 — ✅

### L-08 | LOCAL | S1 | 凑合方案（规模化的"人肉"方案）
- **结论**：市民记录员（Documenters）付费制已经成为"会议无人报道"最主要的人工补位方案，规模在扩大，但仍是按小时付费的人力。
- **证据**：2025 年整个 Documenters 网络发布了 3,253 次公开会议记录任务（历史累计超过 12,000 次），社区成员超过 5,600 人，全年向记录员支付 369,000 美元以上。覆盖最多的是市议会、警务委员会和教育委员会。
- **来源**：Documenters Network 2025 Wrapped — https://citybureau.org/notebook/2026/1/13/documenters-network-2025-wrapped — City Bureau / 2026-01-13 — ✅

### L-09 | LOCAL | S1 | 凑合方案 / 市场数据
- **结论**：Documenters 明确定位为填补"媒体没去的会议"，已扩展到 16 个州。
- **证据**：约 4,000 人受过培训，覆盖 16 个州的 24 个社区。报道称他们在 "covering thousands of meetings that were not covered before"（报道了数千场此前没人报道的会议）。
- **来源**：City Bureau is scaling civic journalism… — https://editorandpublisher.com/stories/city-bureau-is-scaling-civic-journalism-one-documenter-at-a-time,256393 — E&P / 2025-06-24 — ✅

### L-10 | LOCAL | S1 | 需求信号（较老，2018）
- **结论**：仅芝加哥就有数百个政府会议，很多没有任何媒体到场，有的连普通公众都没有。
- **证据**：City Bureau 的 Holliday 说城里有 "hundreds of public government meetings"（数百场公开政府会议），而且 "A lot of these meetings are not reported on"（其中很多没人报道）。
- **来源**：It's not citizen journalism, but… — https://www.niemanlab.org/2018/01/its-not-citizen-journalism-but-it-is-citizens-taking-notes-at-public-meetings-with-no-reporters-around/ — Nieman Lab / 2018-01 — ✅（2018）

### L-11 | LOCAL | S1 | 凑合方案（成本参照）
- **结论**：用人工补位一场会议的成本可以量化：每小时 20 美元，一次任务 1–4 小时，包括事后整理笔记。
- **证据**：Fresnoland 的 Documenters 时薪 "$20 per hour on assignment"（执行任务时每小时 20 美元），不保证最低工时。覆盖市议会、水务区、规划委员会和县监事会。笔记和推文串由编辑部发布。
- **来源**：About the Documenters Program — https://fresnoland.org/about-the-documenters-program/ — Fresnoland / 2022 — ✅

### L-12 | LOCAL | S1 / S2 | 竞品事实（大报的内部自建工具）
- **结论**：资源充足的报社会自建"抓取→转写→关键词提醒"的流水线，并说靠它挖到了本来会漏掉的选题。中小地方媒体做不起这个。
- **证据**：旧金山纪事报用 200 多个自写爬虫每小时检查政府平台，用 Whisper 转写，命中关键词就发邮件提醒，再通过 Slack 用 GPT-4o 问答。覆盖市议会、校董会、州议会等会议，团队称发现了 "dozens of stories that we otherwise may not have found"（几十个原本可能发现不了的报道）。
- **来源**：San Francisco Chronicle – Excellence in AI Innovation — https://awards.journalists.org/entries/san-francisco-chronicle-excellence-in-ai-innovation/ — ONA 奖项 / 2025 — ✅

### L-13 | LOCAL | S9 | 需求信号（有方法论的调查）
- **结论**：地方记者的倦怠率超过七成，加薪并不是留住他们的主要办法。
- **证据**：UNC 调查了 500 多名地方记者：个人倦怠 72%，工作倦怠 70%，72% 考虑过离职。只有 39% 说加薪能让自己留下，排第二的诉求是"更多来自编辑部领导层的支持"。研究者转述记者想要 "the time and support to do work they could be proud of"（有时间和支持去做自己引以为傲的工作）。
- **来源**：Poynter 报道 UNC CISLM 调查 — https://www.poynter.org/?p=1063310 — Poynter / 2023-06-22 — ✅

### L-14 | LOCAL | S1 / S9 | 市场数据
- **结论**：Report for America 每年只能补几十到一百多人，补位的重点是"从未被专门报道过"的社区。
- **证据**：2025–26 年度新派 107 人到 101 个编辑部。超过三分之一的成员关注有色人种和移民社区，近四分之一报道乡村。报道说这些社区 "in many cases, have never received dedicated coverage"（很多从未得到专门报道）。
- **来源**：RFA places 107 journalists… — https://www.editorandpublisher.com/stories/report-for-america-responds-to-challenges-facing-local-news-by-placing-107-journalists-in-newsrooms,255938 — E&P / 2025-05-27 — ✅

### L-15 | LOCAL / INDIE | S8 / S9 | 需求信号（已发生的申请行为）
- **结论**：小型本地媒体对资金的需求极强，申请量远超供给。
- **证据**：Press Forward 2024 年的"填补报道缺口"公开征集有 931 家本地媒体申请，最后资助 205 家，大多是两年 10 万美元，申请门槛是年预算低于 100 万美元。2025 年的基础设施征集收到 550 多份申请，资助 22 个项目共 2,270 万美元，包括 City Bureau（Documenters）125 万美元、MuckRock 的 AI 公共记录工具 125 万美元、RCFP 法律援助 125 万美元。
- **来源**：Press Forward awards $20M to 205 small local newsrooms — https://www.niemanlab.org/2024/10/press-forward-awards-20-million-to-205-small-local-newsrooms/ — Nieman Lab / 2024-10-16 — ✅；Press Forward grants $22.7M to 22 projects — https://www.niemanlab.org/2025/07/press-forward-grants-22-7-million-to-22-newsroom-projects/ — Nieman Lab / 2025-07-16 — ✅

### L-16 | LOCAL / NATL | S2 | 需求信号（有方法论的调查）
- **结论**：调查和问责记者把"拿不到信息和记录"列为头号障碍，延迟、拒绝和复印费是常态。
- **证据**：UF Collier Prize 调查了 51 名调查记者和编辑：近 70% 认为信息受限是最大障碍；一半以上经常遇到延迟、拒绝或高额复印费；四分之三说预算紧张限制了长期问责报道。
- **来源**：UF Survey Finds Records Access Top Barrier — https://brechner.jou.ufl.edu/2025/06/19/uf-survey/ — Brechner Center / 2025-06-19 — ✅

### L-17 | LOCAL | S2 | 需求信号（调查，含非记者申请人）
- **结论**：向地方和州政府申请记录虽然比联邦容易，但会遇到高收费、态度恶劣和隐私理由阻挠。小地方政府没有专职人员，申请人容易被当成"麻烦"。
- **证据**：调查了 330 名公共记录申请人。研究者建议州和地方的复印费 "should be greatly reduced or eliminated"（应大幅降低或取消）。Cuillier 说小地方政府里，申请人 "more likely to be viewed as a nuisance"（更可能被当作麻烦）。他还说联邦层面的积压和延迟十年间"翻倍"。
- **来源**：Public record requesters face rudeness, high fees… — https://brechner.jou.ufl.edu/?p=4063 — Brechner Center / 2025-10-07 — ✅

### L-18 | LOCAL / NATL | S2 | 凑合方案（专家给记者的技巧）
- **结论**：资深 FOIA 记者的办法全是"人工谈判"：先报道再申请、缩小范围、打电话、用"缩小范围换更早交付"的方式讨价还价，并引用法条要求免费。
- **证据**：华盛顿邮报的 Nate Jones 说核心问题二十年没变："delays and over-redactions"（拖延和过度涂黑）。他建议给对方打电话，请对方描述可能存在哪些记录再缩小请求，把它叫作 "horse trade"（讨价还价）。还建议引用 2016 年修正案：机构超过法定期限的，不得向媒体收取大部分费用。
- **来源**：'FOIA Nate' on open access issues — https://www.pressclubinstitute.org/2025/03/20/foia-nate-on-open-access-issues-narrowing-records-requests/ — Press Club Institute / 2025-03-20 — ✅

### L-19 | LOCAL / FREE | S2 | 市场数据（制度事实）
- **结论**：联邦法院记录（PACER）按页收费，连"零结果"的搜索也收钱。对高频使用的记者来说是持续成本。
- **证据**：每页 0.10 美元，单份文件封顶 3 美元，但姓名搜索结果和庭审笔录不封顶。零结果的搜索也按 1 页收费。每季度 30 美元以下免收。政府机构同样付费。服务中心代查每次 30 美元。
- **来源**：How much does it cost to access documents using PACER — https://pacer.uscourts.gov/help/faqs/how-much-does-it-cost-access-documents-using-pacer — PACER 官方 — ✅

### L-20 | LOCAL | S1 / S2 | 需求信号（记者和法院人员原话）
- **结论**：地方法院条线被大幅削减，常常和警务条线合并，记者多在办公桌上看网上的案卷，很少去法院，所以只报"新立案和判决"。
- **证据**：Courthouse News 的 Bill Girdner 说地方法院报道队伍被 "decimated"（大量裁减），很多报纸取消了全职法院条线。文章说互联网 "allows reporters to see court decisions at their newsroom desks"（让记者在编辑部桌前就能看判决）。法院公共信息官协会说法院记者 "are not working at the same level they did previously"（工作深度已不如从前）。
- **来源**：Court Coverage – From "The Front Page" To The Internet — https://gatewayjr.org/court-coverage-from-the-front-page-to-the-internet — Gateway Journalism Review / 2025-03-06 — ✅

### L-21 | LOCAL | S2 | 市场数据（制度事实，较老，2018）
- **结论**：州法院记录的网上开放程度各州不一，很多地方仍要亲自去法院找书记员复印。
- **证据**：NEFAC 说新英格兰多数需要司法记录的人仍须到各个法院向书记员申请并现场复印。缅因州当时没有上网，有些州只对律师和当事人开放网上访问。
- **来源**：Explainer: Online Access to State Court Records — https://nefac.org/explainer-online-access-to-state-court-records/ — NEFAC / 2018-01-17 — ✅（2018；后续州别现状未能再核实）

### L-22 | LOCAL | S2 / S3 | 需求信号（有方法论的调查，2021）
- **结论**：教育记者面对的是"进校园难、接触官员难、拿信息难"，加上人手被摊得太薄。
- **证据**：EWA 2020 年调查了 400 多名教育记者。执行主任说记者受困于 "limited newsroom resources that stretch them way too thin"（编辑部资源有限，人被摊得太薄），并呼吁公立学校和大学移除障碍，保证及时进入 "campuses, staff, and information"（校园、人员和信息）。
- **来源**：Survey of education journalists sheds light on impact, obstacles — https://ewa.org/news-explainers/survey-of-education-journalists-sheds-light-on-impact-obstacles — EWA / 2021-01-26 — ✅（全文 PDF 超过 10MB 无法抓取，39% 等细分数字未核实）

### L-23 | LOCAL / FREE | S2 / S3 | 需求信号（有方法论的调查，2016，较老）
- **结论**：健康记者从联邦和州机构拿信息很难，"必须通过新闻办、书面答复、PIO 旁听"是常态。
- **证据**：联邦层面 41% 认为"非常难"、35% 认为"有些难"；州层面合计约三分之二认为难；县市层面不到一半。85% 找州信息时必须经过新闻办。一位受访者原话："Written responses to written interview questions are the worst possible waste of time"（用书面答复回应书面采访问题，是最浪费时间的做法）。样本中自由撰稿人占 46%。
- **来源**：Survey of health journalists finds roadblocks… — https://healthjournalism.org/blog/2016/06/survey-of-health-journalists-finds-roadblocks-to-information-at-federal-agencies/ — AHCJ / 2016-06 — ✅（2016）

### L-24 | LOCAL / NATL | S2 / S3 | 需求信号（行业组织正在收集的问题）
- **结论**：2026 年健康条线出现新问题：联邦数据集被下线、FOIA 拖延、专家不再接受采访。AHCJ 和 SPJ 正在系统收集记者遭遇。
- **证据**：记者被 "blocked from public datasets"（拦在公开数据集之外），面对 "extended FOIA delays"（更长的 FOIA 拖延），并且 "losing access to agency experts"（接触不到机构专家）。
- **来源**：Stonewalled by federal agencies? We want to document it — https://healthjournalism.org/blog/2026/05/report-federal-stonewalling/ — AHCJ / 2026-05-07 — ✅

### L-25 | LOCAL | S4 / S9 | 需求信号（有方法论的调查，2018，较老）
- **结论**：环境记者的主要障碍是"没时间去现场"，裁员让情况更糟。
- **证据**：调查了 617 名 SEJ 会员，三分之二认为缺少实地采访时间是重要障碍，近 60% 说裁员造成或加剧了报道障碍。
- **来源**：Survey of environmental journalists… — https://www.mediamatters.org/legacy/survey-environmental-journalists-reveals-good-and-bad-news-about-local-climate-reporting — Media Matters / 2018-03-15 — ✅（2018）

### L-26 | LOCAL | S1 / S3 | 需求信号（业内人士判断）
- **结论**：选举条线记者更少、经验更浅，而选举官员也不习惯和媒体打交道。双方建立关系要靠记者"提前去认识"。
- **证据**：作者 Pam Fessler（The Elections Group 传播顾问）预计 2024 年报道投票和选举的记者会比以往少，留下的人经验也更少。她写道 "Many election administrators are not used to working with the media"（很多选举管理者不习惯和媒体打交道），并建议记者 "Get to know your local election officials, now"（现在就去认识本地选举官员）。
- **来源**：Covering Elections and Voting in 2024 — https://electionline.org/electionline-weekly/2024/04-11 — electionline Weekly / 2024-04-11 — ✅

### L-27 | LOCAL / FREE | S1 / S3 | 凑合方案
- **结论**：地方记者把 Nextdoor 和家长 Facebook 群当作线索源和找信源的渠道，最大的问题是核实居民身份。
- **证据**：Nextdoor 的记者账号计划已有 400 多名记者。Hearst 的一位记者通过在街区发帖，几周内做出 10 多篇报道。一名自由撰稿人先在 Nextdoor "gauge what people … are thinking"（了解大家在想什么），再到费尔法克斯县公立学校的家长 Facebook 群里找一手信源。另一名记者看到"有人吊在桥上"的帖子，打电话给消防部门核实，发现只是演练。
- **来源**：Local journalists have a new sourcegathering tool: Nextdoor — https://www.pressclubinstitute.org/2026/07/31/local-journalists-have-a-new-sourcegathering-tool-nextdoor/ — Press Club Institute / 2026-07-31 — ✅

### L-28 | LOCAL / INDIE | S1 / S7 | 凑合方案（业内倡议）
- **结论**：Rebuild Local News 的创始人主张让记者"驻守"社区平台（Nextdoor、FB 群、Reddit、WhatsApp），理由是读者、谣言和选题都在那里。
- **证据**：原文 "That's where the readers are. That's where the misinformation is."（读者在那里，谣言也在那里。）纽约的 Documented 计划派 2 名记者驻守布鲁克林和皇后区 10 个邮编的 Nextdoor。
- **来源**：Steven Waldman: …we need Nextdoor beat reporters — https://www.gxpress.net/article/8164/steven-waldman-instead-of-taylor-swift-beat-reporters-we-need-nextdoor-beat-reporters — GXpress 转载 Poynter / 2023-11-17 — ✅

---

## 2. INDIE（独立 / 超本地 / 小型非营利）

### I-01 | INDIE | S8 / S9 | 需求信号（112 位发行人的调查）★
- **结论**：独立本地发行人的第一痛点是变现加时间分配，而不是内容采集。多数人靠广告生存，越成功越容易倦怠。
- **证据**："A Hard Reality" 调查了 37 个州加华盛顿特区的 112 位发行人：只有十分之四的个人收入全部来自自己的新闻站；五分之一的人不到四分之一的收入来自新闻站；五分之四几乎完全依赖广告；不到 2% 愿意回到传统编辑部。作者说很多人 "unprepared or don't have the time to balance the editorial work with sales"（没准备好，或没有时间在采编和销售之间平衡），还说 "the work gets harder and almost unmanageable with success"（越成功，工作越难，几乎难以应付）。
- **来源**：Poynter 报道 A Hard Reality — https://www.poynter.org/business-work/2026/independent-local-newsrooms-sustainability-business-models/ — Poynter / 2026-10-01 — ✅

### I-02 | INDIE | S8 | 需求信号（有方法论的项目数据）
- **结论**：LION 会员中三成年预算不到 5 万美元。有专职创收人员的机构，收入中位数是没有的 8 倍（高 700%）。
- **证据**：2022–2024 年共 357 家 LION 会员参与，其中 98 家完成了前后两次评估。31%（116 家）预算低于 5 万美元，47% 在 5 万到 50 万美元之间。参与者的收入中位数从 91,831 美元升到 148,343 美元（+62%）。有创收人员的机构收入中位数 "700% higher than those without"（比没有的高 700%）。早期的关键是创始人投入大量时间做创收。
- **来源**：Want to build a sustainable local newsroom? These 21 steps… — https://www.niemanlab.org/2025/11/want-to-build-a-sustainable-local-newsroom-these-21-steps-will-help-you-get-there-a-new-report-finds/ — Nieman Lab / 2025-11 — ✅

### I-03 | INDIE | S8 / S9 | 需求信号（行业组织判断）
- **结论**：LION 认为会员最大的短板是"不重视业务运营"，并建议创始人列一份"停止做清单"。
- **证据**：报告认为最大弱点是 "a lack of focus on business operations"（不重视业务运营）。从"发展中"进到"稳定"阶段的关键是有 "at least three clear revenue streams"（至少三条清晰的收入来源）。执行主任 Krewson 建议列 "stop doing list"（停止做清单）。
- **来源**：Paths to sustainability — https://localnewsinitiative.northwestern.edu/posts/2025/11/12/lion-report-sustainability-business-development/index.html — Medill LNI / 2025-11-12 — ✅

### I-04 | INDIE | S8 / S9 | 需求信号（会员调查评分）
- **结论**：独立发行人的政策诉求集中在资金和法律保护上，公告刊登改革在开放题里被频繁提到。信息获取类政策没有出现在评分项里。
- **证据**：LION 2025 年秋季会员评分（1–5 分）：资助机构 4.20，反 SLAPP 法 3.87，广告定向拨款 3.73，公告刊登改革 3.60，新闻奖学金 3.51。原文说公告刊登改革 "heavily mentioned by our members as one of the most urgent"（被会员大量提及为最紧迫的问题之一）。另一个反复出现的主题是平台抢走广告："Tech monopolies … capture most of the digital ad revenue"（科技巨头拿走了大部分数字广告收入）。（页面未给出样本量）
- **来源**：LION's Policy Platform — https://lionpublishers.com/?p=222185 — LION / 2025-12-23 — ✅

### I-05 | INDIE | S8 | 需求信号
- **结论**：超小型编辑部"数据太多，没时间分析"，需要的是按阶段告诉他们该看哪几个指标。
- **证据**：数据对小发行人来说 "can just be too much overwhelming noise"（可能只是压倒性的噪音）。News Revenue Hub 的人说，没有 "the time to analyze it"（分析的时间），数据就毫无意义。
- **来源**：What we are learning from studying key metrics for tiny newsrooms — https://www.tinynewsco.org/what-we-are-learning-from-studying-key-metrics-for-tiny-newsrooms/ — Tiny News Collective / 2024-07-21 — ✅

### I-06 | INDIE | S7 / S8 | 凑合方案（创始人原话，2020，较老）
- **结论**：超本地 newsletter 的增长靠每天手动推广，头七八个月没有收入。工具上选 Substack 是为了"不用自己搭系统"。
- **证据**：Charlotte Ledger 创始人说用了 Substack 就 "didn't have to build anything or integrate WordPress and Stripe and MailChimp"（不用自己搭任何东西，也不用把 WordPress、Stripe 和 MailChimp 接起来）。他说一直在 "looking for a switch … that would accelerate the growth"（找能加速增长的开关）。推广靠 Twitter、Facebook、LinkedIn、私人 FB 群和本地 NPR 节目。原话 "The money doesn't just show up on day one"（钱不会第一天就来）。
- **来源**：Can local news thrive on Substack? — https://simonowens.substack.com/p/can-local-news-thrive-on-substack — Simon Owens / 2020-11-13 — ✅（2020）

### I-07 | INDIE | S8 | 市场数据（平台激励，2021）
- **结论**：Substack 曾专门出钱扶持本地作者。当时的标杆作者付费订阅只有几百到几千人，常常还要靠别的工作补贴。
- **证据**：Substack Local 投入 100 万美元，扶持最多 30 名作者，单人最高预支 10 万美元。City Hall Watcher 有 900 名订阅者，每月 5 美元，对作者来说是 "one of several gigs"（几份兼职之一）。
- **来源**：Nieman Lab on Substack Local — https://niemanlab.org/?p=192110 — Nieman Lab / 2021-04-15 — ✅（2021）

### I-08 | INDIE | S1 / S7 / S8 | 凑合方案 / 竞品事实（厂商案例，自报数据）
- **结论**：活动和生活方式类超本地 newsletter 的内容痛点是"本地信息碎片化、没有集中来源"，变现靠活动、本地广告和周边多条线。
- **证据**：Catskill Crew 不到一年从 200 名订阅者涨到 1 万以上，有 11 条以上收入来源，每场活动约 2,000 美元。用 Facebook 广告、Reddit 和 Instagram 获客。案例里说本地活动信息分散，Instagram 噪音大，没有集中来源。
- **来源**：Catskill Crew case study — https://www.beehiiv.com/case-studies/catskill-crew — beehiiv / 2024 — ✅（厂商营销，数据未经审计）

### I-09 | INDIE | S1 / S7 | 竞品事实
- **结论**：Patch 用 AI 按邮编自动生成本地 newsletter，靠聚合、活动日历和 Nextdoor 帖子填内容，常出现"抓错同名城市"的问题。
- **证据**：已激活约 14,000 个社区（原计划 30,000），订阅者近 100 万。CEO 承认每周好几次听到 "It's the wrong Springfield"（搞错了是哪个 Springfield），并定位为 "This is a utility"（这是个工具）。
- **来源**：CJR on Patch AI newsletters — https://www.cjr.org/?p=118905 — CJR / 2026-03-05 — ✅（Axios 原文返回 403 ❌）

### I-10 | INDIE | S1 / S8 | 竞品事实（2019，较老）
- **结论**：Patch 很早就把镇议会会议纪要做成自动内容源，由 AI 整理、编辑挑选。最高利润的收入是自助广告。
- **证据**：内容源会拉取镇议会会议纪要，AI 整理后由编辑挑重点、补一个电话核实再发。自助活动推广每天 1 美元，平均订单 48 美元，是利润率最高的产品。
- **来源**：Patch wants to be the bright spot in local news — https://www.adexchanger.com/the-sell-sider/patch-wants-to-be-the-bright-spot-in-local-news/ — AdExchanger / 2019-09-27 — ✅（2019）

### I-11 | INDIE / LOCAL | S8 / S9 | 市场数据
- **结论**：非营利新闻整体收入还在涨，但单家机构已到瓶颈，新创立的机构几乎停了。
- **证据**：2025 年 INN 会员合计收入超过 7.5 亿美元（+14%），但收入中位数从 532,000 美元降到 525,000 美元，支出中位数从 434,000 美元升到 449,000 美元。2025 年只有 9 家新会员机构开始发稿，2019–2020 年每年约 20 家。76% 说受到当前政治环境的负面影响。
- **来源**：同 L-06 — https://niemanlab.org/2026/06/ai-use-growth-challenges-and-funding-cuts-a-new-report-looks-at-the-state-of-nonprofit-news — ✅

---

## 3. FREE（自由撰稿人与学生记者）

### 3a. 自由撰稿人

### F-01 | FREE | S8 / S9 | 需求信号（有方法论的调查）
- **结论**：拖欠和不付稿费是自由撰稿人的系统性问题。追款基本靠自己发邮件、打电话，几乎没人走法律途径。
- **证据**：纽约联盟调查（Authors Guild、Freelancers Union、NWU 等）：62% 至少被赖过一次账，其中 51% 损失超过 1,000 美元；91% 遇到过拖欠，54% 被拖欠三个月以上；39% 因此影响交房租或付账单；79% 靠自己发邮件或打电话追讨；76% 每周花 1–2 小时追款；不到 1% 诉诸法律。页面提到 "Freelance journalism was hit especially hard"（自由新闻业受冲击尤其严重）。
- **来源**：Survey finds 62 percent of NY freelance workers have lost wages… — https://authorsguild.org/news/survey-finds-62-percent-of-ny-freelance-workers-have-lost-wages-due-to-nonpayment — Authors Guild / 2022-05-11 — ✅（2022；样本量未披露）

### F-02 | FREE | S9 | 市场数据 / 需求信号（较老，2019）
- **结论**：在纽约，新闻和数字媒体从业者大多做过自由职业，找活主要靠人脉，被拖欠的比例超过七成。
- **证据**：5,000 人的代表性调查显示，68% 的新闻或数字媒体从业者过去 12 个月做过自由职业。80% 的媒体和娱乐类自由职业者靠亲友、客户和职业人脉找活。新闻稿写所有自由职业者中 74% 遭遇过不付款或拖欠，正文写 73%。
- **来源**：Freelancing in NY report — https://www.nyc.gov/site/mome/news/09102019-freelancing-in-ny-report.page — NYC MOME / 2019-09-10 — ✅（2019）

### F-03 | FREE | S9 | 市场数据（法律保护）
- **结论**：纽约州把"Freelance Isn't Free"从市级推到州级，在州层面为自由撰稿人和记者提供防拖欠保护。这说明问题严重到需要立法。
- **证据**：州长 Hochul 签署了 S5026，此前在 2022 年 12 月曾因成本问题否决过一版。Freelancers Union 的人说 "all work deserves pay"（所有工作都应该有报酬）。
- **来源**：Freelance Isn't Free Becomes Law in New York State — https://www.publishersweekly.com/pw/by-topic/industrynews/publisher-news/article/93811-freelance-isn-t-free-becomes-law-in-new-york-state.html — Publishers Weekly / 2023-11-22 — ✅（生效日期未核实）

### F-04 | FREE | S8 / S9 | 凑合方案（2020，较老）
- **结论**：稿酬不透明，自由撰稿人靠私下网络（Study Hall 数据库、Slack、私人 FB 群、Who Pays Writers）交换费率和编辑联系方式，而且担心被编辑报复。
- **证据**：Study Hall 会员维护一份共享数据库，记录编辑联系方式和各家媒体付的费率。一位撰稿人说 "Writers are scared of editors seeing them differently"（作者怕编辑因此对自己另眼相看）。另一位说行业 "discouraged from sharing rates"（不鼓励分享费率）。
- **来源**：Rate sharing — https://www.cjr.org/special_report/rate-sharing.php — CJR / 2020-02-25 — ✅（2020）

### F-05 | FREE | S8 / S9 | 需求信号（有方法论的调查，英国，非美国）
- **结论**：自由撰稿人最痛的是费率低和收入不稳定，其次是"不会投稿和谈价"。自由社群是主要的互助渠道。
- **证据**：Sheffield Hallam 和 Freelancing for Journalists 在 2024-11 到 2025-02 调查了 401 名英国自由记者：73% 不满意收入；一半人收到过每词不到 10 便士的报价；64% 因为稿费太低拒过活；只有 26% 经常或总是议价。最不喜欢的方面是低薪（37%）、收入不稳（22%）、行政负担（12%）。最大障碍是费率低（25%）和缺乏投稿和约稿的门道（17%）。91% 兼做其他自由工作，其中 67% 做文案。只有 29% 全部收入来自自由新闻。
- **来源**：The State of Freelance Journalism Report 2024（PDF）— https://static1.squarespace.com/static/632b1725aea33e5c7d02b12f/t/692dc9e3ae5a0d45b40e3392/1764608483447/The+State+of+Freelance+Journalism+Report+2024.pdf — Sheffield Hallam / 2025 — ✅（PDF 已抽取全文）；Press Gazette 报道 — https://pressgazette.co.uk/media-audience-and-business-data/freelance-journalists-pay-survey-2025/ — ✅

### F-06 | FREE | S9 | 需求信号（调查，作者群体）
- **结论**：美国写作者对 AI 的主要诉求是授权同意和补偿。真正确认"因 AI 丢了活"的人还少，但一半人说不清。
- **证据**：2023 年 11 月调查了 2,400 多名作者：96% 认为使用作品训练 AI 应征得同意并付费；6% 知道自己因 AI 丢过活；50% 说不知道。
- **来源**：AG AI survey reveals authors overwhelmingly want consent and compensation — https://authorsguild.org/news/ag-ai-survey-reveals-authors-overwhelmingly-want-consent-and-compensation-for-use-of-their-works/ — Authors Guild / 2023-12-21 — ✅（样本以图书作者为主，没有记者细分）

### F-07 | FREE | S9 | 市场数据
- **结论**：美国写作者收入中位数很低，而且一半收入来自书以外的工作（新闻、文案等），说明写作者普遍靠拼凑多份工作谋生。
- **证据**：5,699 名作者参与。全职作者 2022 年写作相关总收入中位数 20,000 美元，所有作者为 5,000 美元。"most authors are earning half of their writing-related income from sources other than their books"（大多数作者一半的写作收入来自书以外）。
- **来源**：Key takeaways from 2023 Author Income Survey — https://authorsguild.org/news/key-takeaways-from-2023-author-income-survey/ — Authors Guild / 2023-09-27 — ✅（没有单独的新闻收入数字）

### 3b. 学生记者

### S-01 | FREE（学生） | S2 / S9 | 需求信号（求助行为）
- **结论**：学生记者对法律求助的需求高，问题集中在公共记录、版权、采访准入、诽谤，近年还新增了 AI。
- **证据**：SPLC 法律热线 2023–24 学年回答了 941 次咨询，来自 47 个州加华盛顿特区，涉及公共记录、版权、摄影准入、记者特权、诽谤和 AI。2024 年 4–5 月的求助量比 2023 年同期多 34%。
- **来源**：SPLC Annual Report 2023-2024（PDF）— https://splc.org/wp-content/uploads/2024/08/SPLC-Annual-Report-2023-2024.1.pdf — SPLC / 2024-08 — ✅（PDF 已抽取全文）

### S-02 | FREE（学生） | S9 | 需求信号（求助行为）
- **结论**：2024 年秋季开学后，热线求助量继续大增。
- **证据**：新学年头三个月 "47% increase in inquiries to our free Legal Hotline"（免费法律热线的咨询量增长 47%）。已有 18 个州通过 New Voices 法，保护 1,050 万名学生。
- **来源**：How we're meeting the moment — https://splc.org/2024/11/how-were-meeting-the-moment/ — SPLC / 2024-11-08 — ✅

### S-03 | FREE（学生） | S6 / S9 | 需求信号（有方法论的调查）
- **结论**：大学报纸主编多数每年都会遇到校方审查，但单个人遇到的次数不多。
- **证据**：2020–21 年调查了 477 所公立四年制大学的旗舰校报，69 人回应（回应率 14.5%）。63.8% 至少遇到过一次行政审查；60.9% 被要求不发某篇报道；60.3% 被叫去开发稿前的会；14% 遭遇经费威胁。结论原文 "highly prevalent, but individually infrequent"（普遍存在，但落到每个人头上并不频繁）。
- **来源**：Free PRESSED: How administrative censorship is squeezing student newsrooms — https://www.fire.org/research-learn/free-pressed-how-administrative-censorship-squeezing-student-newsrooms — FIRE / 数据 2020–21 — ✅

### S-04 | FREE（学生） | S2 / S3 | 需求信号 + 凑合方案
- **结论**：学生记者向本校申请公共记录经常拿不到，采访又被发言人挡住。凑合办法是去 Wayback Machine 找存档、改问发言人，或者起诉。
- **证据**：UCLA 的 Daily Bruin 有 70 多份记录申请超过 6 个月没回，而加州法律要求 14 天内答复。Cal Poly 的学生 2024 年 4 月依据加州公共记录法起诉后才拿到记录。UC Berkeley 要求所有问题都发给发言人，48 小时内邮件答复。学生用 Wayback Machine 找存档数据。一名学生说 "This trend to just have a tight hold on everything is ultimately not beneficial for anybody"（什么都捂着的趋势最终对谁都没好处）。
- **来源**：The Nation on universities restricting student press — https://www.thenation.com/article/society/universities-censorship-student-press-information-access-public-records/tnamp/ — The Nation / 2026-07-30 — ✅

### S-05 | FREE（学生） | S1 / S9 | 需求信号（有方法论的访谈）
- **结论**：大学的学生报道项目被看作填补新闻荒漠的力量，但受限于教师精力和学生流动性。
- **证据**：2025 年 2–4 月访谈了 131 名负责新闻与高校合作的教师。89% 说本地媒体有强烈的合作意愿；83% 认为合作能缓解新闻荒漠；56% 说教师精力被摊薄，没时间编辑学生稿件；55% 说学生流动大，项目难以延续；66% 说学校更看重学术发表。
- **来源**：2025 Opportunities and Obstacles Report — https://www.uvm.edu/ccn/research-reports-and-case-studies/reports/2025-opportunities-and-obstacles-report — UVM Center for Community News / 2025 — ✅

---

## 4. 条线 × 主要信息来源 × 获取难度 × 证据 ID

难度分级（综合上面证据给出的判断，不是原始数据）：
- ●○○ 低：公开在网上，可以直接拿
- ●●○ 中：公开但分散，或者需要人力盯守
- ●●● 高：要付费、申请或诉讼，有制度性阻碍，或者只能到现场

| 条线 | 主要信息来源 | 获取难度 | 难点具体是什么 | 记者现有的凑合方案 | 证据 ID |
|---|---|---|---|---|---|
| 市政（市议会、县委员会、规划委员会） | 议程和会议纪要 PDF、会议直播或录像、Legistar/CivicPlus/Granicus 等平台 | ●●○ 中 | 文件公开，但数量巨大（单个城市两周约 20 份议程、15 个委员会）、平台各不相同、PDF 不好解析；人手不够就会漏掉 | 会前手动翻议程、熬夜蹲会、Documenters 付费人工记录（每小时 17–24 美元）、Agenda Watch 邮件提醒、大报自建爬虫加 Whisper 转写 | L-03, L-04, L-05, L-08, L-09, L-10, L-11, L-12, L-06 |
| 教育（学区委员会、学校） | 学区委员会议程、学校和学区数据、PIO（公共信息官） | ●●○～●●● | 委员会议程和市政一样分散；进校园难、接触官员难，要经过 PIO | 家长 Facebook 群和 Nextdoor 找信源，Documenters 记录教育委员会会议 | L-03, L-04, L-08, L-22, L-27 |
| 法院 | PACER（联邦）、各州法院系统、法院现场终端 | ●●● 高 | PACER 按页收费，零结果也收钱；州法院系统各自为政，有些只对律师开放网上访问，要到现场看终端或复印；法院专职记者被裁或和警务条线合并 | 在桌前看网上案卷，只报新立案和判决；依赖法院 PIO 提供的摘要；联邦层面可用季度 30 美元以内的免费额度 | L-19, L-20, L-21 |
| 公共记录 / FOIA（跨条线） | 州和地方公共记录申请、联邦 FOIA | ●●● 高 | 拖延、拒绝、过度涂黑、复印费高；小地方政府没有专人处理，态度差；州之间差异大 | 先报道再申请、缩小范围、电话"讨价还价"、引用法条要求免费、起诉，或借助 MuckRock 一类工具 | L-16, L-17, L-18, L-15, S-04 |
| 健康 | 联邦和州卫生机构、公开数据集、专家 | ●●● 高（2026 年变得更难） | 必须通过新闻办、只给书面答复、PIO 旁听；2026 年还出现数据集下线、专家不再接受采访 | 书面提问、走新闻办、向 AHCJ 和 SPJ 报告遭遇 | L-23, L-24 |
| 环境 | 机构数据、现场采访 | ●●○ 中（证据较老） | 主要瓶颈是没时间去现场，加上裁员 | （证据不足） | L-25 |
| 选举 | 县选举办公室、选举官员 | ●●○ 中 | 记者少、经验浅，官员不习惯和媒体打交道 | 提前建立关系，"现在就去认识"选举官员 | L-26 |
| 社区 / 突发（超本地） | Nextdoor、Facebook 群、Reddit、居民 | ●○○ 拿到容易 / ●●● 核实难 | 信息多但真假难辨，居民身份难核实，可能抓错同名城市 | 记者账号发帖征集线索，打电话向消防或警方核实 | L-27, L-28, I-08, I-09 |
| 校园（学生记者） | 本校公共记录、校方发言人 | ●●● 高 | 申请半年没回；采访必须经过发言人，48 小时邮件答复；校方审查 | Wayback Machine 找存档、SPLC 热线、起诉 | S-01, S-03, S-04 |
| 商业 / 地产 | 县产权登记、规划审批、公司注册（LLC） | 未取证 | 本轮搜索配额用完，没有拿到可核实证据 | — | （空缺，见第 5 节） |

---

## 5. 五条最重要或最反常识的发现

1. **独立和超本地记者的第一痛点是变现和时间，而不是找线索。** 五分之四靠广告；只有四成能完全靠新闻站养活自己；不到 2% 想回传统编辑部；越成功越容易倦怠；有专职创收人员的机构收入中位数高 700%。对这个群体，只做"线索发现"的产品切不中他们的要害，除非能直接省出时间去做销售。（I-01, I-02, I-03, I-05）
2. **地方新闻机构用 AI 时，"会议转写和摘要"是第一用途（60%），远高于写稿（6%）。** 市政会议处理已经是实际花钱、花时间在做的事。但大报自建一套会议流水线要 200 多个爬虫，中小机构只能雇 Documenters，每小时约 20 美元，或者人工翻议程。（L-06, L-07, L-12, L-08, L-11）
3. **最难拿的是"记录"类信源，不是会议。** 法院（PACER 按页收费、州法院系统各自为政、要到现场看终端）、公共记录（拖延、收费、涂黑）、健康机构（PIO 把关，2026 年数据集被下线），全靠人工谈判、诉讼和在网上东拼西凑，而且法院条线本身被大幅裁撤。从"条线 × 难度"看，这一块比市政会议更难自己解决。（L-16 到 L-21, L-23, L-24）
4. **"会议没人报道"的缺口可以量化，补位主要靠人力。** 全美三分之一的县没有一名全职本地记者的工作量；Documenters 一年 3,253 次任务、付出 36.9 万美元，只覆盖二十多个地点。人工补位方案贵、慢，覆盖面也有限。（L-02, L-08, L-09）
5. **自由撰稿人的核心痛点是"收钱"本身。** 91% 遇到过拖欠，54% 被拖欠三个月以上，79% 靠自己发邮件和打电话追款，每周花 1–2 小时，几乎没人走法律途径。纽约州因此立法。费率不透明，大家靠私下社群交换信息。AI 带来的焦虑主要是授权和补偿，确认因 AI 丢活的只有 6%。（F-01, F-03, F-04, F-06）

## 6. 证据薄弱、需要补的地方

- **商业/地产条线完全空白**：县产权登记费用、LLC 背后的实际所有人、规划审批文件等难点都还没取证。需要在 IRE 的 tipsheet、SEJ 或 Poynter 里找。
- **招聘 JD 没有取到**：地方条线 JD 里"参加并报道县委员会、学区委员会会议"等工作描述，可以作为需求信号补进来。
- **美国本土自由记者调查**：tandfonline 上的 2024 年美国自由撰稿人调查（据称 2,133 人，收入中位数 25,933 美元）返回 403，已弃用。Who Pays Writers 和 Study Hall 的当前费率没有原始数据。美国自由记者"如何找活、AI 对收入的影响"缺少本土数据，目前用的是英国数据和美国作者群体数据。
- **INN Index 原报告打不开**（403），数字全部来自 Nieman Lab 转述。
- **州法院记录收费的现状**：加州 AB 1524（每页 0.50 美元的网上查阅费）、明尼苏达每份文件 8 美元这类线索，原始页面返回 403 或内容为空，没有写进正文。
- **学生记者**：College Media Association 近年的顾问调查没有取到；FIRE 的数据是 2020–21 年的。
- **较老的证据**：AHCJ 2016、SEJ 2018、EWA 2021、City Bureau 2018、Agenda Watch 2020、Charlotte Ledger 2020。建议在 2024–2026 年的范围内找替代。
- **S5（核实）环节**：只有"社区信息难核实"（L-27、I-09）这样的间接证据，缺少地方记者核实负担的直接调查。
- **独立记者的工具和时间分配**：缺少 newsletter 作者公开的周工时拆分，比如采编、销售、发行各占多少时间。
