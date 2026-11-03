# 01 行业调查取证：有公开方法论的大样本调查里的美国记者需求

## 本文件覆盖范围

- **范围**：从有公开方法论的行业调查和研究报告里提取美国记者的需求信号，覆盖五个群体（LOCAL/TV/INDIE/NATL/FREE）、九个环节（S1–S9）。另单列美国记者和媒体数量等市场数据。
- **来源数**：28 个独立来源，全部实际访问过。其中 6 份是原始 PDF 或官方 API，已下载通读：Muck Rack 2026 全文、Muck Rack 2025 工作生活平衡全文、Pew 2022 记者调查全文和 topline、BLS OES API。
- **条目数**：52 条。需求信号 34 条，市场数据 14 条，凑合方案 4 条。
- **主要局限**
  1. **商业调查的样本有偏差。** Muck Rack 和 Cision 是公关软件公司，样本来自它们的记者数据库，偏向收公关稿的记者。问题也偏媒体关系（PR pitch）。Muck Rack 以美国为主，但混了英、加、印的样本；Cision 是全球 19 个市场，最多只拆到北美。
  2. **唯一的美国记者全样本调查已经偏老。** Pew 2022 调查了 11,889 人，2022 年后 Pew 没有再做记者本人的调查。2023 年以后的美国记者 AI 使用数据只能靠 Muck Rack、Cision 这类商业调查。
  3. **"时间花在哪"几乎没有按环节拆分的量化数据。** 所有调查都只问总工时、稿量、是否有足够时间，没有问"发现线索花了多少小时"。
  4. **新闻数量页被 403 拦截。** BLS 的 OES 页面和 INN 官网都返回 403。BLS 数字改从官方 BLS Public API 取得；INN 数字来自 What Works 的二手转述，标为 ⚠️。
  5. **网页搜索配额在中途用完。** 本轮后期只能抓取已知 URL，FREE（学生、自由撰稿人）和 TV 的 AI 用法细节没能继续补。

---

## A. 记者自称的最大挑战与威胁

**01-01** | 全体（美国为主） | S5、S9 | 需求信号
- **结论**：2026 年记者眼中的头号威胁是"虚假信息"和"资金不足"并列。对"无约束 AI"的担忧一年内上升 8 个百分点。
- **证据**：最担心的问题（可选三项）：虚假信息 32%，资金不足 32%，公众信任 26%，无约束地使用 AI 26%（2025 年为 18%），政府干预 25%，政治化 23%，人手不足与时间压力 20%，地方新闻衰落 20%。"质量控制与事实核查能力"只有 7%。2025 年"虚假信息"为 36%。
- **来源**：State of Journalism 2026 — https://media.muckrack.com/documents/State_of_Journalism_2026_1.pdf — Muck Rack / 2026-03（2026-01-30 至 03-02 调查 1,044 人，有效 897 人，以美国为主）— ✅ 已下载全文

**01-02** | 全体 | S5 | 需求信号
- **结论**：过半记者表示，过去一年虚假信息让报道变难了。
- **证据**：14% 说"难了很多"（a great deal），42% 说"有些变难"，30% 说"影响不大"，9% 说"没有影响"。
- **来源**：同 01-01，第 4 页 — ✅

**01-03** | 全体（全球，含北美） | S5、S2 | 需求信号
- **结论**：Cision 2026 年调查中，"准确性、事实核查、对抗虚假信息"首次成为头号挑战，"资源约束"紧随其后。
- **证据**：准确性/事实核查/虚假信息 50%，资源约束 49%，AI 的兴起与冲击 43%，受众行为变化 42%，非传统媒体与创作者的竞争 28%。新闻稿原文："Accuracy, fact-checking, and combating misinformation emerged as the No. 1 challenge"（准确性、事实核查和对抗虚假信息成为头号挑战）。
- **来源**：PR Emerges as the Primary Source for Journalists in High-Pressure Newsrooms — https://www.cision.com/about/press-releases/2026-press-releases/pr-emerges-as-the-primary-source-for-journalists-in-high-pressure-newsrooms-302770936/ — Cision / 2026-05-13（1,899 人，19 个市场，2026 年 1–2 月）— ✅；细项见 https://www.cision.com/resources/articles/biggest-journalism-challenges-media/ — ✅

**01-04** | 全体 | S9、S1–S6 | 需求信号
- **结论**：约一半记者把"预算缩水、裁员、工作量增加"列为最大障碍。
- **证据**：49% 认为 shrinking budgets, staff cuts, and increased workloads（预算缩水、人员削减、工作量上升）是最大障碍。
- **来源**：同 01-03 的 Cision 2026 新闻稿 — ✅

**01-05** | 全体（含北美） | S9 | 需求信号
- **结论**：2024 年，"媒体缩编、资源减少"是记者个人层面最普遍的挑战。北美记者对裁员的担忧明显高于其他地区。
- **证据**：个人挑战中，媒体缩编与资源减少 60%，在重要报道和商业压力之间平衡 42%，与网上虚假信息竞争 33%。行业挑战中，北美 41% 担心裁员，EMEA 为 37%，APAC 为 22%。北美 41% 把"可信度与'假新闻'指控"列为前三挑战。
- **来源**：Journalists' use of AI…Cision State of the Media 2024 — https://pressgazette.co.uk/platforms/journalists-ai-cision-state-of-the-media-report-2024-facebook-tiktok-instagram/ — Press Gazette / 2024（转述 Cision 2024，n=3,016）— ⚠️ 二手转述

**01-06** | 全体（美国） | S5、S9 | 需求信号（2022，偏老）
- **结论**：美国记者对"编造的新闻"的担忧远高于公众，同时对行业整体评价悲观。
- **证据**：71% 的记者认为编造新闻是"非常大的问题"，成年公众为 50%。72% 用负面词形容行业，最常见的是"挣扎"和"混乱"。57% 非常或极其担心美国的新闻自由受限。
- **来源**：Journalists Sense Turmoil in Their Industry Amid Continued Passion for Their Work — https://www.pewresearch.org/journalism/2022/06/14/journalists-sense-turmoil-in-their-industry-amid-continued-passion-for-their-work/ — Pew / 2022-06-14（11,889 名美国记者，2022-02-16 至 03-17，误差 ±1.0）— ✅（另下载全文 PDF https://www.pewresearch.org/wp-content/uploads/sites/20/2022/06/PJ_2022.06.14_Journalist-Survey.pdf ✅）

**01-07** | NATL、LOCAL（调查报道） | S2 | 需求信号
- **结论**：调查记者把"拿不到信息"列为最大障碍，公共记录的延迟、拒绝和高价复印费很普遍。
- **证据**：近 70% 说受限的信息获取是最大障碍。过半经常遇到记录申请被拖延、拒绝或收取过高复印费。3/4 说预算缩水限制了长期问责报道。25% 说政治压力让他们在某些议题上犹豫。
- **来源**：UF Survey Finds Records Access Top Barrier for Investigative Journalists — https://brechner.jou.ufl.edu/2025/06/19/uf-survey/ — UF Collier Prize / 2025-06（n=51 名调查记者和编辑，样本小）— ✅

**01-08** | 全体（美国） | S2 | 需求信号
- **结论**：3/4 的美国记者用过公共记录法，56% 认为近几年记录越来越难拿。
- **证据**：505 名美国记者中，75% 用过（主要向地方和州机构申请），56% 说获取记录变难了，92% 担心美国新闻自由的前景。
- **来源**：FOI research winner: Journalists express concern for press freedom and transparency — https://brechner.jou.ufl.edu/?p=4087 — Brechner Center / 2025-11-03（Coyle、Molyneux、Haskell，9 月调查，n=505）— ✅（只有摘要，方法细节未公开）

---

## B. 时间、工作量与人员缩减

**01-09** | 全体（美国为主） | S9 | 需求信号
- **结论**：62% 的记者职责连续两年超出本职，人员缩减直接转化成"一人多岗"。
- **证据**：显著扩大 29%，有些扩大 33%，不变 33%，收窄 5%。
- **来源**：Muck Rack State of Journalism 2026，第 12 页 — 同 01-01 — ✅

**01-10** | 全体 | S1–S6 | 需求信号
- **结论**：多数记者"经常"有足够时间按自己的标准完成工作，但约 15% 很少或从来没有。时间压力没有想象中普遍。
- **证据**：总是 18%，经常 39%，有时 27%，很少 14%，从不 1%。
- **来源**：Muck Rack State of Journalism 2026，第 9 页 — ✅

**01-11** | 全体（美国为主） | S6、S9 | 需求信号
- **结论**：近一半记者每周要做 4 篇以上稿件，约 1/4 做 10 篇以上。2/3 全职记者每周工作超过 40 小时。
- **证据**：报告结论为"48% 每周写 4 篇以上"，约 1/4 每周 10 篇以上（PDF 图表各档的标签对应关系提取不清，所以只引用报告的文字结论）。67% 的全职记者周工时超过 40 小时，17% 超过 51 小时。83% 每周至少一次在非工作时间加班，21% 超过 5 次。
- **来源**：The State of Work-Life Balance in Journalism 2025 — https://media.muckrack.com/documents/3.17.2025_SoWLB_-_journo_report.pdf — Muck Rack / 2025-03（2025-01-02 至 02-17 调查 432 人，有效 408 人，以美国为主，误差 ±5%）— ✅ 已下载全文

**01-12** | 全体 | S9 | 需求信号
- **结论**：工作量本身是最大压力源。"没人替班"让记者连假期都休不了。
- **证据**：最主要的压力源是工作量、"永远在线"和薪水。不休假的原因中，工作量占 37%，没人替班 26%，必须"永远在线"21%。96% 下班后难以"断开"。58% 每晚只睡 6 小时或更少。
- **来源**：同 01-11 — ✅

**01-13** | 全体（美国为主） | S9 | 需求信号
- **结论**：一半记者在一年内想过因倦怠辞职，42% 曾因倦怠离职。
- **证据**："In the last year, have you thought about quitting your job because of exhaustion or burnout?"（过去一年你是否因疲惫或倦怠想过辞职？）回答"是"的占 50%。42% 曾因倦怠离开过上一份工作。38% 说心理健康在过去一年变差。
- **来源**：同 01-11 — ✅

**01-14** | LOCAL | S9 | 需求信号（2023）
- **结论**：地方记者的倦怠更严重，72% 考虑过离开现职。
- **证据**：500 余名地方记者用哥本哈根倦怠量表测量：个人倦怠约 72%，工作倦怠约 70%，72% 考虑过离开现职。工作倦怠高的人中约 80% 想过离开，低的人中为 53%。45 岁以下记者两类倦怠都超过 75%。只有 39% 说加薪能留住自己。
- **来源**：Local journalism's burnout crisis is unsustainable — https://www.poynter.org/local-news/2023/reporters-newsroom-burnout-problem-solutions/ — Poynter / 2023-06-22（转述 UNC CISLM 调查）— ✅（访问的是 https://www.poynter.org/?p=1063310 的跳转）

**01-15** | 全体（含管理者） | S9 | 需求信号（2023 调查）
- **结论**：记者和管理者都认为"用更少的人做更多的事"是行业最负面的因素。
- **证据**：80% 的记者经历过倦怠，91% 看到同事挣扎。20% 的在职记者计划因倦怠离开或已经离开，管理者中为 18%。
- **来源**：Newsroom burnout: the strain of doing more with less — https://rjionline.org/news/newsroom-burnout-the-strain-of-doing-more-with-less/ — RJI / 2025-02（SmithGeiger × RJI 2023 年调查，原文未给样本量）— ✅

**01-16** | TV | S9 | 需求信号
- **结论**：地方电视台新闻总监普遍观察到员工倦怠加剧，中型市场最严重。
- **证据**：62.9% 的新闻总监同意"比以往看到更多员工倦怠迹象"。前 25 大市场 52%，26–100 名市场超过 70%，最小市场 54.5%。2023 年平均每台招 8 名替补，中位数 6 名。
- **来源**：Local TV news staffing rises despite burnout challenges — https://rtdna.org/news/rtdna-syracuse-survey-local-tv-news-staffing-rises-despite-burnout-challenges — RTDNA/Newhouse / 2024-05-21（2023 年第四季度调查 1,876 家电视台，有效回复最多 1,387 家，73.9%）— ✅

**01-17** | 全体（美国为主） | S9 | 需求信号
- **结论**：记者希望领导层"多招人"而不是"用更少的人做更多事"，也希望有 AI 培训。
- **证据**：开放题原话举例："Hire more people instead of demanding we do more with less."（多招人，而不是要求我们用更少的人做更多事）；"Better training on use of AI in journalism."（更好的新闻业 AI 使用培训）。只有 56% 觉得在工具、培训和编辑指导上得到了支持。
- **来源**：Muck Rack State of Journalism 2026，第 6–7 页 — ✅

**01-18** | 全体（美国） | S9 | 需求信号（2023，偏老）
- **结论**：2023 年就有约 20% 的记者因裁员或停职而工作量增加，1/3 担心没有时间深入报道。
- **证据**：裁员和停职让约 20% 的记者工作量上升。33% 把"没有时间深入报道"列为担忧。记者平均跑 4 条线，47% 每周产出 5 篇以上稿件。
- **来源**：Muck Rack survey: Two out of three journalists have been impacted by economic uncertainty — https://www.editorandpublisher.com/stories/muck-rack-survey-two-out-of-three-journalists-have-been-impacted-by-economic-uncertainty,242757 — E&P / 2023-03（Muck Rack 2023，n=2,226，合作方含 SPJ、NABJ、ONA）— ⚠️ 二手转述

---

## C. 线索与信源（S1、S3）

**01-19** | 全体（美国为主） | S1 | 需求信号
- **结论**：线索主要靠记者自己找。只有 3% 完全由编辑派题，40% 自己选题，55% 两者混合。
- **证据**：自己提报并选题 40%，混合 55%，完全由编辑派题 3%。
- **来源**：Muck Rack State of Journalism 2026，第 25 页 — ✅

**01-20** | 全体 | S1 | 需求信号 / 凑合方案
- **结论**：公关来稿是常见的线索来源。86% 的记者至少有部分稿件起源于 PR pitch，但相关性很差，造成大量噪音。
- **证据**：51% 的人有 1–10% 的稿件来自 pitch，34% 的人超过 10%，只有 14% 完全没有。43% 很少收到与自己条线相关的 pitch。88% 会直接删除不对口的 pitch。一个正常工作日收到 6–10 封的占 29%，20 封以上的占 14%。
- **来源**：Muck Rack State of Journalism 2026，第 28–32 页 — ✅

**01-21** | 全体（全球） | S1 | 需求信号 / 凑合方案
- **结论**：在人手紧张的编辑部，公关提供的内容（新闻稿、pitch、媒体包）成为首要选题来源，但大多不相关。
- **证据**：66% 依靠公关内容寻找选题，72% 说不到 1/4 的 pitch 相关。
- **来源**：Cision 2026 新闻稿，同 01-03 — ✅

**01-22** | 全体 | S1、S3 | 需求信号
- **结论**：记者最看重 pitch 里"与条线明确相关"和"能接触到信源"，其次是原始数据。这说明找信源和找数据是真实痛点。
- **证据**：70% 要求与条线明确相关，58% 希望提供相关信源的采访机会，40% 希望有原始数据或研究，只有 14% 需要预写好的引语。78% 认为"直接影响受众所在社区"才算真正相关。
- **来源**：Muck Rack State of Journalism 2026，第 31–33 页 — ✅

**01-23** | 全体（美国） | S1、S3 | 需求信号（2022）
- **结论**：社交媒体是记者发现选题和找信源的主要渠道，但不可靠。
- **证据**：用社交媒体工作的记者中，79% 认为它有助于找信源，75% 认为有助于发现该报道的选题，但只有 49% 认为有助于获取准确信息。94% 的记者在工作中用社交媒体。
- **来源**：Pew 2022 全文 PDF 第 30–31 页 — 同 01-06 — ✅

**01-24** | 全体（美国为主） | S1、S3 | 需求信号
- **结论**：记者对社交媒体作为线索和采访渠道的依赖两年内明显下降，但发布推广仍离不开它。
- **证据**：认为社交媒体对"生产内容"非常重要的比例从 2024 年的 33% 降到 21%；对"推广"非常重要的保持 45%。X 作为最有价值平台的比例从 2024 年的 36% 降到 17%，Facebook 28% 居首。在 Bluesky 上投入更多时间的比例从 38% 降到 24%。
- **来源**：Muck Rack State of Journalism 2026，第 17–20 页 — ✅

**01-25** | TV、LOCAL | S1 | 凑合方案 / 需求信号（2022，偏老）
- **结论**：地方编辑部想自动化的是"信息搬运"类工作：转录、体育比分、筛选公共记录和社交内容。小编辑部没时间也没人力试新工具。
- **证据**：AP 调查近 200 家地方编辑部（覆盖 50 州），想要的自动化包括采访转录与翻译、高中体育比分、事实核查增强、分析公共记录、筛选社交媒体内容；转录是呼声最高的一项。障碍包括时间和资源有限、推动创新的人一走就断档、"current technology in local newsrooms is patchy and often does not sync"（地方编辑部现有技术零散，彼此不同步）。
- **来源**：Small, Local Newsrooms Slow to Adopt Artificial Intelligence, AP study shows — https://localnewsinitiative.northwestern.edu/posts/2022/03/29/associated-press-ai-study/ — Medill / 2022-03-29 — ✅；补充：https://tvtechnology.com/news/survey-tv-radio-digital-managers-support-using-ai-in-newsgathering — TV Tech / 2022-03-31（TV 管理者比电台和数字媒体更常在新闻采集中使用 AI）— ✅

---

## D. AI 的态度与实际用法

**01-26** | 全体（美国为主） | S4、S6 | 需求信号（使用行为）
- **结论**：2026 年 82% 的记者至少用过一种 AI 工具。通用聊天模型增长最快，转录工具保持在 40%。
- **证据**：ChatGPT 47%（2025 年 42%），转录工具（如 Otter）40%（持平），Grammarly 约 32–35%，Gemini 22%（2025 年 13%），Claude 12%（2025 年 6%），编辑部自建 AI 工具约 6%（图表读数），一个都没用过的 18%（2025 年 23%）。
- **来源**：Muck Rack State of Journalism 2026，第 16 页 — ✅

**01-27** | 全体（全球，北美单列） | S2、S4、S5 | 需求信号
- **结论**：AI 主要用于头脑风暴、研究和事实核查、转录和摘要，用来直接生产内容的少。北美的采用率明显低于亚太。
- **证据**：2026 年：头脑风暴 48%，研究或事实核查 43%，转录和采访摘要 41%，内容创作 27%。北美完全不用 AI 的超过 1/3（2025 年为 49%），EMEA 30%，APAC 11%。
- **来源**：https://www.cision.com/resources/articles/biggest-journalism-challenges-media/ — Cision / 2026 — ✅

**01-28** | 全体 | S2、S4 | 需求信号
- **结论**：2025 年 Cision 全球样本中约一半用 AI，最常见的用途是研究话题和转录采访。
- **证据**：53% 用 AI 辅助工作，25% 用于研究话题，23% 用于转录采访和音频。北美"不用也不打算用"的占 49%。72% 担心公关用 AI 生成的内容有事实错误。
- **来源**：https://www.cision.co.uk/resources/articles/biggest-journalism-challenges-media/ — Cision UK / 2025（>3,000 人）— ✅；另见 2025 新闻稿 https://www.cision.com/about/press-releases/2025-press-releases/cisions-2025-state-of-the-media-report-reveals-a-tipping-point-for-trust-technology-and-pr-journalist-partnerships-302448410/ — ✅

**01-29** | 全体 | S2、S6 | 需求信号（2024 基线）
- **结论**：2024 年过半记者完全不用生成式 AI。用的人主要拿来研究和起草，自由撰稿人比在职员工更担心 AI。
- **证据**：53% 完全不用，28% 用一点，12% 中等，5% 经常。使用者中 23% 用来研究话题，19% 写提纲或初稿，13% 想选题。34% 的自由撰稿人把 AI 列为前三担忧，员工为 23%。
- **来源**：同 01-05 的 Press Gazette 页面 — ⚠️ 二手转述

**01-30** | 全体（美国/欧洲为主） | S4、S6、S7 | 需求信号（2023 年 12 月调查）
- **结论**：编辑部人员用生成式 AI 主要做"周边文字活"（社交帖、newsletter、标题、翻译、转录），多数反对用 AI 生成整篇内容。
- **证据**：近 70% 用过生成式 AI，49% 说工作流程已经改变。56% 认为应该禁止用 AI 生成整篇内容。只有 7% 担心 AI 取代工作。不到一半的编辑部有 AI 准则。
- **来源**：AP survey coverage — https://www.poynter.org/ethics-trust/2024/artificial-intelligence-transforming-journalism/ — Poynter / 2024-04-10（AP × Diakopoulos 等，n=292，偏熟悉 AI 的人，非代表性样本）— ⚠️ 二手转述；原报告 ResearchGate 链接未访问

**01-31** | TV | S6、S7 | 需求信号
- **结论**：地方电视台 AI 采用率仍然只有约 1/3，大市场明显高于小市场，用途集中在后台。
- **证据**：32.6% 的新闻总监说本台"在用 AI 做些什么"（前一年 26.6%）。最大市场 42.9%，最小市场 22.9%。用途包括字幕、标题生成、转录、校对、西语配音。部分台由集团层面明令禁用。原话："credibility is hard to earn back once you've reported something that isn't true"（一旦报了不实信息，信誉很难挽回，WAPT）。
- **来源**：AI in Local TV News: How Stations Are Using It—and Why Some Still Ban It — https://newslab.org/ai-in-local-tv-news-how-stations-are-using-it-and-why-some-still-ban-it/ — NewsLab / 2025-06-30 — ✅；数字原始出处：https://www.rtdna.org/news/ai-and-ott-use-up-nextgen-tv-use-drops-at-local-tv-stations — RTDNA/Newhouse（2024 年第四季度，1,918 家电视台，有效回复最多 1,406 家，73.3%）— ✅

**01-32** | INDIE | S4、S6 | 需求信号
- **结论**：非营利新闻机构用 AI 做转录、摘要和数据分析，几乎不用它写稿。
- **证据**：多数机构用 AI 转录或摘要采访、分析数据，只有 6% 用它起草稿件。
- **来源**：Nonprofit local news is growing, but the revenue mix remains unbalanced — https://whatworks.news/2025/10/09/nonprofit-local-news-is-growing-but-the-revenue-mix-remains-unbalanced-according-to-a-new-inn-report/ — What Works（Dan Kennedy）/ 2025-10-09（转述 INN Index 2025）— ⚠️ 二手；inn.org 原页 403

**01-33** | 全体（美国） | S6 | 需求信号（2022 基线）
- **结论**：2022 年 AI 在美国编辑部几乎不存在，到 2026 年个人使用率已超过八成，四年内跳变。
- **证据**：2022 年只有 8% 的记者说所在机构"至少有一点"依赖 AI 生成内容，62% 说完全没有，29% 不确定。对比 01-26 的 82%（问法不同，一个是机构依赖，一个是个人使用，不能直接相减）。
- **来源**：Pew 2022 全文 PDF 第 31 页 — ✅

**01-34** | 全体（全球新闻高管） | S6、S7 | 需求信号（管理层）
- **结论**：新闻机构管理层把 AI 的重点放在后台自动化和新闻采集上，AI 至今基本没有替代岗位。
- **证据**：97% 认为后台自动化重要，82% 认为新闻采集重要，81% 认为编码和产品开发重要（比上年高 16 点）。13% 认为 AI 已带来变革，42% 认为影响有限。67% 说 AI 没有省下任何岗位，16% 小幅减员，9% 新增岗位。
- **来源**：Journalism, media, and technology trends and predictions 2026 — https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026 — Reuters Institute / 2026-01（280 位数字新闻领导者，51 国，2025-11-18 至 12-20，作者自称非代表性样本）— ✅

---

## E. 信任、虚假信息、安全压力

**01-35** | 全体（美国） | S5 | 需求信号（2022）
- **结论**：1/3 的记者经常在报道中碰到虚假信息，26% 曾在不知情时报道过后来证实含假信息的稿件。
- **证据**：8% 极其经常、24% 相当经常在做稿时遇到假信息，44% 有时遇到。71% 对自己识别假信息有信心。26% 的报道型记者曾无意中报道过含不实信息的稿件。约四成认为媒体在处理和纠正虚假信息上做得不好。
- **来源**：Pew 2022 全文 PDF 第 27 页及主页 — ✅

**01-36** | 全体（美国公众） | S8、S5 | 市场数据（受众侧）
- **结论**：美国公众对媒体的信任跌到 28%，首次低于 30%，共和党人只有 8%。这是记者"信任压力"的外部背景。
- **证据**：2025 年 28% 对报纸、电视、广播"有很多或相当多信任"（2024 年 31%，五年前 40%）。共和党 8%，无党派 27%，民主党 51%。
- **来源**：Trust in Media at New Low — https://news.gallup.com/poll/695762/trust-media-new-low.aspx — Gallup / 2025（2025-09-02 至 16，n=1,000，误差 ±4）— ✅

**01-37** | 全体（美国） | S8、S5 | 需求信号（2022）
- **结论**：记者严重低估了公众对新闻的信任。他们普遍认为公众不信任自己。
- **证据**：只有 14% 的记者认为公众对新闻机构有"很多或相当多"信任，而公众自报为 29%。65% 的记者认为新闻机构准确性做得好，公众只有 35%。
- **来源**：Pew 2022 主页 — 同 01-06 — ✅

**01-38** | TV、全体 | S9 | 需求信号
- **结论**：骚扰和安全问题已经改变记者的工作方式，TV 记者最常被外部骚扰。
- **证据**：Pew 2022 中，42% 的记者过去一年被外部人员骚扰或威胁，其中 78% 至少一次通过社交媒体，TV 记者高达 58%；19% 受到人身伤害威胁。Muck Rack 2026 中，32% 说安全顾虑影响了工作方式（7% 显著影响，25% 有些影响），59% 说安全、骚扰或声誉顾虑改变了在社交媒体上的职业行为。
- **来源**：Pew 2022 — 同 01-06 — ✅；Muck Rack 2026 第 8、22 页 — ✅

**01-39** | 全体（美国） | S9 | 需求信号 / 市场数据
- **结论**：2025 年美国记者遭受的人身攻击激增，主要发生在抗议现场。记者对安全培训的需求创新高。
- **证据**：截至 2025-12-15，有 32 起记者因工作被拘留或起诉（2024 年 50 起），近 90% 发生在报道抗议时，约 90% 最终没有被起诉或撤诉。2025 年记录的袭击数接近前三年总和。CPJ 2025 年在美国培训了近 1,000 名记者，开展 26 场课程（数字安全 11 场、人身安全 7 场等），称需求"激增"。
- **来源**：Press arrests used to silence protest coverage in 2025 — https://pressfreedomtracker.us/blog/press-arrests-used-to-silence-protest-coverage-in-2025/ — U.S. Press Freedom Tracker / 2025-12-15 — ✅；CPJ: Acceleration of US press freedom concerns spike demand for safety training — https://cpj.org/2025/12/cpj-acceleration-of-us-press-freedom-concerns-spike-demand-for-safety-training/ — CPJ / 2025-12-22 — ✅

---

## F. 职业与生存（S9）、受众与变现（S8）

**01-40** | 全体（美国全职） | S9 | 需求信号 / 市场数据
- **结论**：美国全职记者收入集中在 4 万到 7 万美元，长期职业信心只略过半数。
- **证据**：年薪 4 万–7 万美元 45%，7 万–10 万 30%，低于 4 万 9%，高于 10 万 17%（只统计美国全职记者）。长期职业前景有信心的 53%，没有信心的 30%。觉得未来 12 个月工作安全的 66%。对工作的感受：有意义 65%，疲惫 47%，不稳定 38%。原话举例："Raise my pay for the first time in 10 years"（十年来第一次给我加薪）。
- **来源**：Muck Rack State of Journalism 2026，第 5、10–13 页 — ✅

**01-41** | 全体 | S9、S7 | 需求信号（行为）
- **结论**：37% 的记者在传统媒体之外以个人名义或品牌独立发布内容，独立化趋势在上升。
- **证据**：独立发布者 37%（"比去年略高"）。工作类型：全职员工 58%，兼职或偶尔自由撰稿 19%，全职自由撰稿 18%，独立或自出版 12%。
- **来源**：Muck Rack State of Journalism 2026，第 23、39 页 — ✅

**01-42** | FREE | S9 | 市场数据 / 需求信号（2022）
- **结论**：自由撰稿人在美国记者中占比很大，而且更偏全国和国际选题，地方选题由在职员工承担。
- **证据**：Pew 2022 样本中 28% 是自由撰稿人或自雇者，学生和实习生不到 1%。在职员工所在机构中 48% 以社区、城市或县为主要范围；自由撰稿人中只有 25% 以地方为主，45% 以全国为主。
- **来源**：Pew 2022 全文 PDF 第 22 页脚注；Topline — https://www.pewresearch.org/journalism/wp-content/uploads/sites/8/2022/06/PJ_2022.06.14_Journalist-Survey_TOPLINE.pdf — ✅

**01-43** | FREE | S9 | 需求信号
- **结论**：自由撰稿人的痛点是没有稿费预算和收入不稳，而不是人手不足。他们对 AI 抢活更敏感。
- **证据**：Cision 2024 中，只有 22% 的自由撰稿人把人手和资源列入前三担忧，员工为 42%；34% 的自由撰稿人把 AI 列入前三担忧，员工为 23%。Cision 2025 中 20% 的样本是自由或独立记者，有自由撰稿人原话："no budget for freelance writers"（没有给自由撰稿人的预算）。
- **来源**：同 01-05（Press Gazette）⚠️；https://www.cision.co.uk/resources/articles/biggest-journalism-challenges-media/ ✅

**01-44** | FREE（学生） | S9、S2 | 需求信号（2020–21，偏老，样本小）
- **结论**：大学学生报编辑普遍遭遇校方审查，涉及校方决策、人事、财务和校园犯罪的报道最容易受阻。
- **证据**：63.8% 的编辑在一年内至少遇到一次行政审查。60.9% 被要求不发布某内容。60.3% 在发布前被叫去和校方开会（2016–17 年为 26.7%）。21.7% 认为校方不喜欢报道校园犯罪。
- **来源**：Free PRESSED: How administrative censorship is squeezing student newsrooms — https://www.fire.org/research-learn/free-pressed-how-administrative-censorship-squeezing-student-newsrooms — FIRE（数据为 2020–21 学年，n=69，回复率 14.5%）— ✅

**01-45** | INDIE | S8、S9 | 需求信号 / 市场数据
- **结论**：非营利地方新闻机构规模极小，严重依赖基金会。独立创办人最大的短板是业务运营。
- **证据**：INN 2025：近 400 家机构，收入中位数 53.2 万美元。地方机构中位数约 4 个全职当量，收入不到 36 万美元。收入构成为基金会 49%、个人捐赠 32%、广告和活动 18%。LION：有专职营收人员的机构，收入中位数比没有的高 700%；最大弱点是"lack of focus on business operations"（缺乏对业务运营的关注）。
- **来源**：What Works 转述 INN Index 2025（同 01-32）⚠️；Paths to sustainability — https://localnewsinitiative.northwestern.edu/posts/2025/11/12/lion-report-sustainability-business-development/ — Medill / 2025-11-12 ✅

**01-46** | INDIE | S7、S8 | 需求信号（行为）
- **结论**：独立地方新闻几乎全员做 newsletter，并在向直连受众的渠道转移。
- **证据**：做 newsletter 的比例从 2022 年的 81% 升到 2024 年的 95%，办活动的从 34%（2021）升到 60%。73% 认为直接搜索有效（2022 年 56%），超过 75% 仍把自然流量社交列为最有效的发现渠道之一。
- **来源**：Nearly all local online newsrooms produce newsletters, a LION report finds — https://www.niemanlab.org/2024/07/nearly-all-local-online-newsrooms-produce-newsletters-a-lion-report-finds/ — Nieman Lab / 2024-07（LION 可持续性审计 2022–2024，n=100、75、90）— ✅

**01-47** | INDIE、LOCAL | S8 | 市场数据（受众侧）
- **结论**：地方新闻的付费意愿极低且多年不涨，受众正从电视转向网站、社交和社区论坛。
- **证据**：15% 的成年人过去一年为地方新闻付费或捐款（2018 年以来几乎没变）。52% 至少有时从 Facebook 群组、Nextdoor 等论坛获取地方新闻（比 2018 年高 14 点）。31% 从地方 newsletter 或 listserv 获取。22% 非常关注地方新闻（2016 年 37%）。Reuters DNR 2025 美国在线新闻付费率 20%。
- **来源**：Americans' Changing Relationship With Local News — https://www.pewresearch.org/journalism/2024/05/07/americans-changing-relationship-with-local-news/ — Pew / 2024-05-07（n=5,146，2024-01-22 至 28）— ✅；https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/united-states — ✅

**01-48** | INDIE、FREE | S7、S8 | 竞品事实 / 市场数据
- **结论**：新闻网红正在争夺独立记者的受众，而且大多没有新闻从业背景，过半已经变现。
- **证据**：21% 的美国成年人经常从新闻网红那里获取新闻，18–29 岁为 37%。77% 的新闻网红没有新闻机构背景。59% 通过订阅、捐赠或周边变现，22% 发 newsletter。Reuters Trends 2026 中，70% 的新闻高管担心创作者分走注意力，76% 计划让记者"更像创作者"。
- **来源**：America's News Influencers — https://www.pewresearch.org/journalism/2024/11/18/americas-news-influencers/ — Pew / 2024-11-18 ✅；Reuters Trends 2026（同 01-34）✅

**01-49** | 全体 | S7 | 市场数据
- **结论**：搜索和社交带来的流量在塌缩，发布与分发环节的不确定性急剧上升。
- **证据**：Chartbeat 数据显示，Google 自然流量 2024-11 至 2025-11 全球下降 33%，美国下降 38%；Facebook 引流下降 43%，X 下降 46%。新闻高管预计三年内搜索流量平均下降约 43%。
- **来源**：Reuters Trends 2026（同 01-34）— ✅

---

## G. 市场数据（规模，不作需求证据）

**01-50** | 全体 | — | 市场数据
- **结论**：美国约有 3.9 万名"新闻分析员、记者与通讯员"，平均年薪约 10.2 万美元，中位数 6.2 万美元。另有 9.2 万名编辑，含非新闻编辑。
- **证据**：BLS OES May 2025：SOC 27-3023 就业人数 39,250，年均工资 102,460 美元，年工资中位数 62,200 美元；SOC 27-3041 Editors 就业人数 91,690。
- **来源**：BLS Public API — https://api.bls.gov/publicAPI/v2/timeseries/data/OEUN000000000000027302301 （就业）、…027302304（均值）、…027302313（中位数）、https://api.bls.gov/publicAPI/v2/timeseries/data/OEUN000000000000027304101 （编辑就业）— BLS / May 2025 估计 — ✅ 通过 API 取数；OES 页面 https://www.bls.gov/oes/current/oes273023.htm 返回 403 ❌

**01-51** | LOCAL、TV、INDIE | — | 市场数据
- **结论**：新闻荒漠持续扩大，地方记者岗位一年减少约 7%。
- **证据**：2025 年：212 个县没有任何本地新闻源（2024 年 206 个）；1,525 个县只有一个新闻源；近 5,000 万人（约 1/7 的美国人）只能有限获取或完全无法获取地方新闻。自 2005 年以来消失了近 3,500 份报纸，剩余 5,400 多份。过去一年报社失去 1,200 多个记者岗位，数字媒体失去 1,800 多个，记者职业整体从 2023 年到 2024 年下降略超 7%。追踪到 695 家独立数字新闻站、342 家公共媒体台。2024 年报告：报纸业就业 98,960 人，编辑部岗位自 2005 年减少 45,000 多个（超过 60%），报纸以每周 2 份以上的速度消失。
- **来源**：State of Local News 2025 — https://localnewsinitiative.northwestern.edu/projects/state-of-local-news/2025/report/ — Medill ✅；2024 report — https://localnewsinitiative.northwestern.edu/projects/state-of-local-news/2024/report/ — ✅

**01-52** | TV、INDIE | — | 市场数据
- **结论**：地方电视台约有 2.7 万名全职新闻员工、695 个新闻部，是地方记者的最大雇主之一。非营利新闻约 4,650 人。
- **证据**：2024 年地方台全职新闻雇员 27,066 人，同比下降 2.9%，比 2021 年峰值 28,000 低 3.3%。自制本地新闻的电视台从 697 家降到 695 家。2025 年多家集团裁员（ABC 台、Scripps、Gray、Sinclair、Tegna、Nexstar 等）。INN 成员机构员工从 4,500 人增到 4,650 人，约 70% 是编辑岗。INN 成员中地方机构占 51%。
- **来源**：Local TV news employment moves down … along with hiring — https://www.rtdna.org/news/local-tv-news-employment-moves-down--along-with-hiring — RTDNA/Newhouse / 2025-09（2024 年第四季度调查）✅；INN 数字见 01-32 ⚠️

---

## 证据—群体—环节覆盖小结

| 环节 | LOCAL | TV | INDIE | NATL | FREE | 主要条目 |
|---|---|---|---|---|---|---|
| S1 发现线索 | 中 | 弱 | 弱 | 中 | 弱 | 19–25 |
| S2 背景研究 | 中 | 无 | 无 | 强（调查记者） | 弱 | 07、08、27 |
| S3 找信源 | 中 | 无 | 无 | 中 | 无 | 22、23 |
| S4 采访与素材 | 中 | 中 | 中 | 中 | 无 | 25–28、32 |
| S5 核实 | 强 | 弱 | 无 | 强 | 无 | 01–03、35 |
| S6 写作制作 | 中 | 中 | 中 | 中 | 弱 | 11、30、31 |
| S7 发布分发 | 中 | 弱 | 强 | 中 | 弱 | 24、46、49 |
| S8 受众变现 | 弱 | 无 | 强 | 弱 | 弱 | 45–48 |
| S9 职业生存 | 强 | 强 | 中 | 中 | 中 | 09–18、38–44 |

**需要单独提出的环节问题**：媒体关系和 PR 噪音过滤（01-20 到 01-22）其实横跨 S1 和 S3，但在商业调查中权重很高，这是因为样本来自公关数据库，结论可能被放大。另外，"安全与法律风险"（01-38、01-39）在九个环节中没有独立位置，目前归入 S9，建议协调者考虑是否单列为横切维度。

---

## 最反常识或最重要的 5 条

1. **AI 用量四年从约 8% 跳到 82%，但用在"边角活"上，不用于写稿**（01-26、01-27、01-32、01-33）。最常见的用途是头脑风暴、研究和核查、转录摘要，只有约 27% 用于内容创作，非营利机构只有 6% 用 AI 起草稿件。记者需要的是帮忙找和整理信息的工具，不是写稿工具。转录在 2022 年就是地方编辑部呼声最高的需求，现在 40% 的记者在用，已经是被满足的红海。
2. **线索主要靠记者自己找，而且大量依赖公关来稿这种低质量的凑合方案**（01-19 到 01-21）。只有 3% 完全靠编辑派题。66%（Cision）说靠公关内容找选题，但 43% 很少收到对口的 pitch，88% 会直接删掉不对口的。"按条线和社区相关性过滤并推送线索"是公认存在、却靠人工凑合的需求。
3. **"没时间"不是最大痛点，"人太少、什么都得干"才是**（01-09、01-10、01-12）。57% 经常或总是有足够时间达到自己的标准，但 62% 的职责超出本职，37% 因工作量休不了假，26% 没人替班。产品机会更可能在"替代一个缺掉的岗位"（比如盯会议、盯 scanner、盯记录），而不是"让写稿快一点"。
4. **核实与虚假信息压力在 2026 年升到首位，但"核查能力不足"只有 7% 的人选**（01-01、01-03、01-35）。记者认为虚假信息是社会问题，不认为是自己的能力缺口：71% 对自己识别假信息有信心，但 26% 曾无意中报道过假信息。核查工具的需求要从"省时间、防漏"切入，而不是"教你识别"。
5. **公共记录越来越难拿**（01-07、01-08）。56% 的美国记者说近几年记录更难获取，调查记者中约 70% 认为信息获取是最大障碍。这是 S2 背景研究里少见、有量化证据、且难以自行解决的需求。市政会议和议题追踪属于"公开但分散"的信息，同属一类。

## 证据薄弱、需要补的地方

- **TV 编辑台的工作流程几乎没有调查数据。** RTDNA 只问人员、薪资、AI 是否在用。派题编辑如何发现突发新闻、scanner 依赖程度、警用电台加密的影响，都没有找到有公开方法论的问卷（RTDNA 2023 年只发了征集案例的倡议）。需要靠 JD 和记者原话补。
- **"时间花在哪个环节"没有按 S1–S8 拆分的量化数据。** 所有调查都只问总工时和稿量。
- **FREE 群体缺少 2023 年以后的美国问卷。** 自由撰稿人只有 Pew 2022 的占比和 Cision 的员工对比；学生记者只有 FIRE 2020–21 的审查数据（n=69）。稿费、拖欠和接单渠道的美国数据缺失，搜到的都是英国或澳洲的。
- **Pew 2022 后没有再做美国记者全样本调查。** 2023 年以后的 AI 数据都来自公关公司样本（Muck Rack、Cision），不能代表美国记者总体。Muck Rack 2025 年报告全文没有拿到（PDF 命名不同），只有 2026 版里的对比数字和二手报道。
- **INN Index 原站 403，数字来自二手转述。** INN 2026（2025 数据：412 家机构，约 4,700 FTE，76% 受政治环境负面影响）只在搜索摘要中见到，未实际打开，所以没有写入条目。
- **AP 2024 生成式 AI 调查原文**（ResearchGate）未打开，只采用了 Poynter 的转述。
- **地方记者专属的 AI 使用率缺失。** Reuters Institute 有英国记者调查（n=1,004），发现独立媒体的 AI 整合度低于集团媒体，但美国没有对应的分层数据。
- **本轮 WebSearch 配额在中途用完**，以上缺口建议在后续任务中补。
