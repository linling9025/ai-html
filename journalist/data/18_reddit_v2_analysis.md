# Reddit 无关键词抽样分析（v2）

- 采样：r/Journalism、r/Broadcasting、r/freelanceWriters 的 top/all、top/year、new 列表（**不做关键词搜索**），去重 4,377 帖；取 2023 年起正文 >150 字的自述帖 2,073 条逐条人工编码（规则 scripts/reddit_coding_schema.md）。
- 相关帖（新闻从业者/学生/自由记者的工作与职业处境）1,032 条。r/freelanceWriters 中大量 SEO/文案/代写帖被判为不相关。
- 因为没有检索词，**同一社区内**各环节/话题的占比可以当作该社区讨论重心的近似；跨社区不可直接相加比较。局限：top 列表偏向高互动帖；Reddit 用户偏年轻、偏求职者；r/Broadcasting 混有技术岗。

## 各社区：相关帖数与环节占比（一帖可多环节）

| 环节 | r/Journalism | r/Broadcasting | r/freelanceWriters |
|---|---|---|---|
| 相关帖数 | 427 | 309 | 296 |
| S1 发现线索 | 17 (4%) | 4 (1%) | 5 (2%) |
| S2 背景研究 | 15 (4%) | 1 (0%) | 3 (1%) |
| S3 找信源 | 50 (12%) | 2 (1%) | 12 (4%) |
| S4 采访与素材 | 42 (10%) | 8 (3%) | 4 (1%) |
| S5 核实 | 21 (5%) | 0 (0%) | 4 (1%) |
| S6 写作与制作 | 50 (12%) | 60 (19%) | 31 (10%) |
| S7 发布与分发 | 42 (10%) | 12 (4%) | 52 (18%) |
| S8 受众与变现 | 27 (6%) | 4 (1%) | 11 (4%) |
| S9 职业与生存 | 232 (54%) | 244 (79%) | 234 (79%) |

## 发帖人身份（相关帖）

- r/Journalism: practitioner 134, aspiring 88, student 74, freelancer 50, unknown 30, editor 17, tv 16, indie 9, tool_builder 7, public 2
- r/Broadcasting: practitioner 163, tv 69, aspiring 31, unknown 24, student 8, freelancer 5, tool_builder 4, public 3, editor 2
- r/freelanceWriters: freelancer 254, aspiring 28, student 6, practitioner 4, tool_builder 2, unknown 1, editor 1

## 条线（相关帖中标出条线的部分）

- r/Journalism: 市政 27, 教育 19, 体育 17, 商业 15, 选举 14, 治安 11, 法院 6, 健康 5, 环境 3, 灾害天气 2, 科技 1
- r/Broadcasting: 体育 20, 灾害天气 7, 商业 6, 健康 2, 科技 1, 选举 1, 移民 1, 治安 1, 市政 1
- r/freelanceWriters: 商业 23, 体育 9, 健康 8, 选举 2, 治安 2, 科技 1, 环境 1, 教育 1

## 强度 ≥2 的痛点，按环节（r/Journalism + r/Broadcasting，每环节最多 12 条）


### S1 发现线索（10 条强度≥2）

- [Broadcasting|practitioner|强度3] Nexstar失去CBS Newspath素材后制作一小时节目压力大  
  > "It's been stressful trying to produce a show with what (little) they're providing on the content desk." — [2026-08-08](https://www.reddit.com/r/Broadcasting/comments/1vjaqjg/nexstar_producer_check_in/)
- [Journalism|practitioner|强度3] 农村唯一记者覆盖7万人，漏事件，质量下滑，不知如何向读者解释  
  > "I'm the only reporter for close to 70,000 people in a 40-mile radius around my rural home office." — [2026-08-21](https://www.reddit.com/r/Journalism/comments/1vul6xx/how_to_explain_overload/)
- [Broadcasting|practitioner|强度2] Nexstar 重心转向 NewsNation，电视台无法获取CNN或联盟台内容，只有聚合素材  
  > "we do NOT have access to CNN or our affiliate content" — [2026-05-04](https://www.reddit.com/r/Broadcasting/comments/1t3o43y/is_nexstar_going_to_drop_affiliations/)
- [Journalism|practitioner|强度2] 选题枯竭，常规办法都不起效  
  > "struggle to come up with pitches" — [2026-07-15](https://www.reddit.com/r/Journalism/comments/1uxh19v/do_you_ever_have_pitch_drought/)
- [Journalism|freelancer|强度2] 想报道本地新兴移民餐饮，向本地商业报纸投稿不被重视  
  > "all the local media covers is traffic, crime, and the occasional state wide corruption story." — [2026-08-08](https://www.reddit.com/r/Journalism/comments/1vj2lev/absolute_lack_of_curiossirty/)
- [Broadcasting|practitioner|强度2] Nexstar禁止使用非Nexstar旗下NBC/Fox台素材，新闻制作内容越来越少  
  > "They're being asked to produce more and more shows with less and less content." — [2026-08-28](https://www.reddit.com/r/Broadcasting/comments/1w15xxs/another_source_of_material_gone/)
- [Journalism|aspiring|强度2] 区域媒体被一家公司收购，20岁技术背景者想办独立新闻平台，但不会找选题、无新闻教育、缺资金  
  > "I have no formal education in journalism" — [2026-08-30](https://www.reddit.com/r/Journalism/comments/1w242ag/creating_an_independent_news_outlet/)
- [Journalism|student|强度2] 被学生报开除后又收到校内腐败(挪用奖学金、Title IX)线索，因担任公职身份不敢写，且学生报因法律风险放弃  
  > "Our student publication dropped the story like a hot potato in fear of legal retaliation" — [2026-09-19](https://www.reddit.com/r/Journalism/comments/1wkzowb/am_i_writing_too_close_to_the_sun/)
- [Journalism|student|强度2] 新手校报记者选题通过后找不到“so what”角度，不知该先定角度还是先采访  
  > "Do you find the angle first? Or do the interviews and see what comes from that?" — [2026-10-07](https://www.reddit.com/r/Journalism/comments/1wzoz4e/how_to_find_the_right_angle/)
- [Journalism|unknown|强度2] 想知道记者如何在几小时内拿到逝者信息，是县登记处实时更新还是公共记录申请  
  > "how news sites and local reporters manage to get information so quickly of deceased people" — [2026-10-11](https://www.reddit.com/r/Journalism/comments/1x2zet7/is_there_a_resource_journalists_use_to_see/)

### S2 背景研究（7 条强度≥2）

- [Journalism|freelancer|强度2] 协助OSINT团队写多方主体、资金流向的时间线，叙事容易迷失  
  > "how do you not get lost in the sauce?" — [2026-07-01](https://www.reddit.com/r/Journalism/comments/1uk8wrf/following_the_money/)
- [Journalism|student|强度2] 查找美甲产品化学成分的可靠资料困难，网上信息太杂  
  > "Someone suggested calling some of the chemical manufacturers of the brands" — [2026-07-30](https://www.reddit.com/r/Journalism/comments/1vaeiwm/need_help_finding_credible_information_on_a/)
- [Journalism|practitioner|强度2] 本地警局对视频音频记录请求收取每小时50美元编辑费，对资源少的新闻室门槛过高  
  > "Our local PD just instituted a fee of $50 per hour to redact video and audio." — [2026-07-31](https://www.reddit.com/r/Journalism/comments/1vbsgiy/how_much_is_your_newsroom_paying_police_for/)
- [Journalism|student|强度2] 高中生做数据中心禁令调查报道，采访议员后发现可疑捐款想追问，担心对方不回应，不知后续方向  
  > "my topic is on a data center moratorium in my town." — [2026-08-07](https://www.reddit.com/r/Journalism/comments/1vi5429/what_if_i_have_an_additional_question_for/)
- [Journalism|practitioner|强度2] 警局公开记录请求（宣誓书、911录音、事故报告）常拖满10个工作日，不同警局速度差异大  
  > "Also, any tips on how to encourage them to not just sit on information until their deadline?" — [2026-08-26](https://www.reddit.com/r/Journalism/comments/1vza4e8/experiences_on_public_records_response_times_from/)
- [Journalism|practitioner|强度2] 想获取教育局成员与助理校长会面的录音，已提交FOIA但录音在对方律师手里，需继续推进  
  > "I submitted a FOIA for the recording, arguing that Board of Education members are members of a public body" — [2026-08-27](https://www.reddit.com/r/Journalism/comments/1w06i3b/foia_brainstorm/)
- [Journalism|unknown|强度2] 想知道记者如何在几小时内拿到逝者信息，是县登记处实时更新还是公共记录申请  
  > "how news sites and local reporters manage to get information so quickly of deceased people" — [2026-10-11](https://www.reddit.com/r/Journalism/comments/1x2zet7/is_there_a_resource_journalists_use_to_see/)

### S3 找信源（28 条强度≥2）

- [Journalism|tv|强度3] CBS新闻高层决策导致信源拒绝采访,转去接受竞争对手NBC采访,影响与信源关系  
  > "I didn’t realize it would impact our ability to build relationships with sources." — [2026-02-12](https://www.reddit.com/r/Journalism/comments/1r2zkmt/bari_weiss_destruction_of_cbs_news_goes_deeper/)
- [Broadcasting|practitioner|强度3] 海外网络驻美分社客座制作人：临时订不到高规格嘉宾，被网络拒绝，伤害与嘉宾关系  
  > "I had 12 hours to book" — [2026-04-09](https://www.reddit.com/r/Broadcasting/comments/1sgb2a3/guest_producer_woes_network_constantly_rebuffs_my/)
- [Journalism|practitioner|强度3] 信源协议用电子签署，信源因担心云端而改走邮寄，耽误数日导致独家被对手抢先  
  > "I shot it over with Xodo Sign so he could just tap it on his screen" — [2026-08-13](https://www.reddit.com/r/Journalism/comments/1vn7j6g/lost_a_3week_scoop_to_the_physical_mail_system/)
- [Journalism|practitioner|强度3] 郊区各市官员拒绝受访、雇公关控制接触，甚至会后把记者驱逐出市政厅  
  > "Many elected officials refuse to talk to me or my fellow reporters anymore" — [2026-08-19](https://www.reddit.com/r/Journalism/comments/1vsnu8n/sudden_jump_in_local_governments_hatred_of_local/)
- [Journalism|editor|强度2] 向国务院求置评时给对方延期后，对方把独家给了福克斯  
  > "A State Department spokesperson asked us for deadline extension" — [2026-04-28](https://www.reddit.com/r/Journalism/comments/1sy9hlf/do_not_give_the_us_state_dept_extensions_on/)
- [Journalism|student|强度2] 新闻学生采访不熟悉领域(网络安全立法)时缺乏信心  
  > "I knew nothing about cybersecurity" — [2026-07-04](https://www.reddit.com/r/Journalism/comments/1un7i6i/how_do_you_gain_confidence_interviewing_people/)
- [Journalism|practitioner|强度2] 游戏媒体记者向发行商公关发评测申请、核实邮件，常常毫无回应，无法获得官方说法  
  > "But how are we supposed to include an official statement when so many PR contacts simply ignore emails?" — [2026-07-08](https://www.reddit.com/r/Journalism/comments/1ur6lll/is_anyone_else_in_games_media_tired_of_how_many/)
- [Journalism|practitioner|强度2] 报道征地纠纷，挨家敲门居民不愿开口，不知如何让抗拒的信源说话  
  > "The story of what's going on here is very absurd and deserves to be told, but now I'm at a loss." — [2026-07-19](https://www.reddit.com/r/Journalism/comments/1v1501h/how_do_i_get_people_to_talk_to_me_who_absolutely/)
- [Journalism|practitioner|强度2] 信源联系方式散落在纸质本、手机和邮件里，想要安全可搜索的信源通讯录，记录是否可引用及背景  
  > "know if they were on or off the record, what the context was of the story, etc." — [2026-07-21](https://www.reddit.com/r/Journalism/comments/1v2ksc3/what_do_you_use_for_a_secure_searchable_contact/)
- [Journalism|unknown|强度2] 报道在宗教保守国家被误认为同性恋的匿名当事人，需要在保护其免受再次伤害的前提下报道  
  > "Reporting an anonymous human rights case involving a public figure while protecting them from further harm" — [2026-08-01](https://www.reddit.com/r/Journalism/comments/1vcobd4/seeking_advice_reporting_an_anonymous_human/)
- [Journalism|editor|强度2] 合作社媒体约稿时被AI生成的假投稿骗局困扰，不得不增加审核环节  
  > "scammy AI pitches" — [2026-08-02](https://www.reddit.com/r/Journalism/comments/1vdjroc/the_issue_of_ai_scams_when_commissioning/)
- [Journalism|aspiring|强度2] 15岁音乐杂志作者想从采访DIY乐队跳到通过公关联系成名乐队  
  > "how do you go from interviewing these grassroots DIY-centric acts to reaching out to publicists or press managers" — [2026-08-03](https://www.reddit.com/r/Journalism/comments/1velt57/15_extremely_passionate_about_music/)

### S4 采访与素材（27 条强度≥2）

- [Journalism|freelancer|强度3] 积压大量采访音频，手工转写拖慢交稿，免费工具遇噪音或多人插话就失效，付不起每月30美元订阅  
  > "typing everything out manually is killing my turnaround time." — [2026-07-21](https://www.reddit.com/r/Journalism/comments/1v2ffjr/best_transcription_workflow_for_freelance/)
- [Journalism|student|强度2] 新闻学生采访不熟悉领域(网络安全立法)时缺乏信心  
  > "I knew nothing about cybersecurity" — [2026-07-04](https://www.reddit.com/r/Journalism/comments/1un7i6i/how_do_you_gain_confidence_interviewing_people/)
- [Broadcasting|practitioner|强度2] 单人摄制(MMJ)自拍出镜stand-up很别扭，求流程与设备建议  
  > "One thing I still find awkward is filming my own standups" — [2026-08-02](https://www.reddit.com/r/Broadcasting/comments/1vdr0io/question_for_the_mmjsvjs/)
- [Journalism|practitioner|强度2] 公司事后声明邮件回复仅供背景、需批准才能引用，记者不知该如何处理  
  > "We had not agreed beforehand that the response would be off the record, on background or subject to prepublication approval." — [2026-08-03](https://www.reddit.com/r/Journalism/comments/1vetpbe/can_a_source_retroactively_require_approval/)
- [Journalism|tv|强度2] 视障自拍记者拍摄自己的出镜讲述（standup）很别扭，想要流程和设备建议  
  > "How do those of you who regularly self-shoot approach them?" — [2026-08-04](https://www.reddit.com/r/Journalism/comments/1vfihc9/question_for_mmjsselfshoot_reporters/)
- [Journalism|student|强度2] 高中生做数据中心禁令调查报道，采访议员后发现可疑捐款想追问，担心对方不回应，不知后续方向  
  > "my topic is on a data center moratorium in my town." — [2026-08-07](https://www.reddit.com/r/Journalism/comments/1vi5429/what_if_i_have_an_additional_question_for/)
- [Journalism|practitioner|强度2] 采访抗议大型科技设施的居民，如何问出真实影响而非泛泛不满  
  > "How do you keep the interview focused on facts (water, noise, zoning, transparency) without sounding like you're interrogating them?" — [2026-08-11](https://www.reddit.com/r/Journalism/comments/1vlj7q6/tips_for_interviewing_residents_protesting_a/)
- [Journalism|practitioner|强度2] 新入行记者视频通话采访常尴尬冷场，不知如何收尾  
  > "interviews just feel painfully AWKWARD" — [2026-08-11](https://www.reddit.com/r/Journalism/comments/1vlel97/awkward_interviews_is_this_normal/)
- [Journalism|freelancer|强度2] 用Otter转写采访，Pro套餐月分钟数上限不够，想要不限量或固定价的替代品  
  > "I keep hitting their monthly minute caps on the Pro plan." — [2026-08-12](https://www.reddit.com/r/Journalism/comments/1vm8vdd/what_are_the_best_otter_ai_alternatives_for/)
- [Journalism|practitioner|强度2] 信源要求不记录的内容仍留存在录音、自动转写和处理账户里，需在采访前决定录音和存储方式  
  > "Removing a quote from a story does not remove those copies." — [2026-08-20](https://www.reddit.com/r/Journalism/comments/1vtqm6b/a_fast_transcript_gets_complicated_when_a_source/)
- [Journalism|unknown|强度2] Otter转写长录音混乱，多人插话时需要大量修改  
  > "short meetings are usually fine but longer ones get messy, especially when people talk over each other.." — [2026-08-22](https://www.reddit.com/r/Journalism/comments/1vvasw7/im_spending_more_time_fixing_transcripts_than/)
- [Broadcasting|practitioner|强度2] Vaxis Storm 3000 无转换功能却把59.94输出成60  
  > "vary curious as to how a device that does not do conversion is converting" — [2026-08-26](https://www.reddit.com/r/Broadcasting/comments/1vz89q7/vaxis_storm_3000_being_weird/)

### S5 核实（13 条强度≥2）

- [Journalism|practitioner|强度3] 信源协议用电子签署，信源因担心云端而改走邮寄，耽误数日导致独家被对手抢先  
  > "I shot it over with Xodo Sign so he could just tap it on his screen" — [2026-08-13](https://www.reddit.com/r/Journalism/comments/1vn7j6g/lost_a_3week_scoop_to_the_physical_mail_system/)
- [Journalism|practitioner|强度3] 入行前90天犯过地名搞错、算错数、人名拼写等错误，焦虑到发稿时手抖  
  > "Now when I go to file an article, my hands start shaking." — [2026-08-26](https://www.reddit.com/r/Journalism/comments/1vz8ibq/making_mistakes_in_the_first_90_days/)
- [Journalism|practitioner|强度3] 都市日报记者怀疑小周报同线记者抄袭自己的深度报道和独家信源内容且不署名  
  > "I report for a daily metro paper" — [2026-10-23](https://www.reddit.com/r/Journalism/comments/1xd25ri/small_competitor_paper_is_stealing_my_work_is/)
- [Journalism|editor|强度2] 向国务院求置评时给对方延期后，对方把独家给了福克斯  
  > "A State Department spokesperson asked us for deadline extension" — [2026-04-28](https://www.reddit.com/r/Journalism/comments/1sy9hlf/do_not_give_the_us_state_dept_extensions_on/)
- [Journalism|practitioner|强度2] AI摘要看似忠实却抹平矛盾、丢失限定，核实速度跟不上AI产出，核实环节无法规模化  
  > "the gap between how fast AI can produce copy and how slow verification is, is widening" — [2026-06-25](https://www.reddit.com/r/Journalism/comments/1uffh0k/the_newsroom_ai_verification_problem_is_not_going/)
- [Journalism|practitioner|强度2] 游戏媒体记者向发行商公关发评测申请、核实邮件，常常毫无回应，无法获得官方说法  
  > "But how are we supposed to include an official statement when so many PR contacts simply ignore emails?" — [2026-07-08](https://www.reddit.com/r/Journalism/comments/1ur6lll/is_anyone_else_in_games_media_tired_of_how_many/)
- [Journalism|practitioner|强度2] 公司事后声明邮件回复仅供背景、需批准才能引用，记者不知该如何处理  
  > "We had not agreed beforehand that the response would be off the record, on background or subject to prepublication approval." — [2026-08-03](https://www.reddit.com/r/Journalism/comments/1vetpbe/can_a_source_retroactively_require_approval/)
- [Journalism|practitioner|强度2] 学校新闻稿只给学生名不给姓，18岁成年人也如此  
  > "Emailed them back and said the pics won’t go in without full names but I’m not hopeful." — [2026-08-13](https://www.reddit.com/r/Journalism/comments/1vne6in/anonymous_kids_grr/)
- [Journalism|student|强度2] 被学生报开除后又收到校内腐败(挪用奖学金、Title IX)线索，因担任公职身份不敢写，且学生报因法律风险放弃  
  > "Our student publication dropped the story like a hot potato in fear of legal retaliation" — [2026-09-19](https://www.reddit.com/r/Journalism/comments/1wkzowb/am_i_writing_too_close_to_the_sun/)
- [Journalism|practitioner|强度2] 独立记者因对受访者品行质疑决定不发，如何告知对方  
  > "How would you handle telling someone this without getting into specifics?" — [2026-09-26](https://www.reddit.com/r/Journalism/comments/1wqisna/need_help_navigating_a_situation/)
- [Journalism|unknown|强度2] 整篇文章含10-15条事实声明，逐条核查耗时，想要先识别关键声明再指向研究的工具  
  > "Checking every statement individually through Google Scholar is pretty time-consuming." — [2026-10-04](https://www.reddit.com/r/Journalism/comments/1wxmn7e/is_there_a_good_way_to_fact_check_an_entire/)
- [Journalism|editor|强度2] 文章更正后，匿名人士反复来信声称“媒体审计”，不知需不需要理会  
  > "Now they’re saying that there’s a media audit involved." — [2026-10-11](https://www.reddit.com/r/Journalism/comments/1x3bkf5/media_audit_is_this_even_a_thing/)

### S6 写作与制作（50 条强度≥2）

- [Broadcasting|tv|强度3] TEGNA强制员工做AI培训并要求保密,担心AI生成图像上电视和数字部门裁员  
  > "Not to mention how many layoffs will happen in the Digital departments." — [2024-11-13](https://www.reddit.com/r/Broadcasting/comments/1gqqex6/tegna_embracing_ai_told_employees_to_keep_quiet/)
- [Broadcasting|tv|强度3] TEGNA裁撤导播并试验由一名AI辅助制片人独自完成整档新闻,担心推广到突发新闻  
  > "experimenting with a single "AI-powered" producer "writing, coding" and "switching" ) an entire newscast by themselves" — [2024-11-23](https://www.reddit.com/r/Broadcasting/comments/1gxp3wt/what_happens_when_a_tech_bro_takes_over_your/)
- [Broadcasting|practitioner|强度3] Nexstar 新闻制作人：缺内容、预算压力、推 CTV 却无奖金，担心台垮  
  > "Right now I feel like my station will colapse sometime soon because of budget issues" — [2026-05-29](https://www.reddit.com/r/Broadcasting/comments/1trayc9/nexstar_news_producers_check_in/)
- [Broadcasting|practitioner|强度3] Tegna 台导播被要求兼做剪辑、编码、摄像，却不招人  
  > "directors will have to edit, code, punch, and work cameras!" — [2026-06-18](https://www.reddit.com/r/Broadcasting/comments/1u9j4wo/tegnadeathstar/)
- [Broadcasting|practitioner|强度3] 制作人每天花6小时赶节目，加了4点档后工作量激增  
  > "I spend 6 hours grinding the day away to get my show done in time" — [2026-06-19](https://www.reddit.com/r/Broadcasting/comments/1uadfgm/how_many_newscasts_should_a_producer_really_have/)
- [Journalism|tv|强度3] 电视台网络编辑重写电视记者的错误稿件，却被新闻总监偏袒记者而撤稿  
  > "Management will always side with the TV reporters" — [2026-07-01](https://www.reddit.com/r/Journalism/comments/1ukpv2u/bias_in_the_newsroom/)
- [Broadcasting|practitioner|强度3] Nexstar失去CBS Newspath素材后制作一小时节目压力大  
  > "It's been stressful trying to produce a show with what (little) they're providing on the content desk." — [2026-08-08](https://www.reddit.com/r/Broadcasting/comments/1vjaqjg/nexstar_producer_check_in/)
- [Journalism|practitioner|强度3] 社区报唯一记者两周要写约30篇并负责排版校对，周末仍需工作，已近倦怠  
  > "I can already feel myself starting to burn out." — [2026-08-20](https://www.reddit.com/r/Journalism/comments/1vtaizd/how_much_is_too_much/)
- [Broadcasting|practitioner|强度3] 新闻制作人被调去周末早间独自制作3小时节目，压力大睡不着  
  > "I normally struggle to come up with 1.5-2 hours of news on my own" — [2026-08-26](https://www.reddit.com/r/Broadcasting/comments/1vz3fme/struggling_to_handle_the_stress_of_being_a_tv/)
- [Broadcasting|tv|强度2] 制片人节目开播前10分钟仍缺图文包装,与导播沟通差  
  > "our producers newscasts are never fully done 10 mins before the newscast starts" — [2024-08-16](https://www.reddit.com/r/Broadcasting/comments/1eu0hkl/what_are_your_guys_broadcasting_petpeeves_either/)
- [Broadcasting|practitioner|强度2] TEGNA要求市场部今后用AI生成宣传片，质量差且不尊重员工  
  > "all generated by AI" — [2025-01-15](https://www.reddit.com/r/Broadcasting/comments/1i1mmcr/new_ai_marketing_tegna_promo_fail/)
- [Broadcasting|tv|强度2] 台里把数字内容创作(含竖屏视频配额)压给摄像、剪辑、制片、指派台,令人费解  
  > "newsrooms continuing to push digital content creation on not just reporters but photogs, editors, producers" — [2025-11-30](https://www.reddit.com/r/Broadcasting/comments/1palbbn/digital_push_in_newsrooms/)

### S7 发布与分发（23 条强度≥2）

- [Journalism|freelancer|强度3] 长期自由撰稿，缺乏结构、过度投入、先写后投难以适应媒体需求，自信心耗尽  
  > "Freelancing has killed my self-esteem" — [2026-10-21](https://www.reddit.com/r/Journalism/comments/1xbsd5u/freelancing_has_killed_my_selfesteem/)
- [Journalism|practitioner|强度3] 都市日报记者怀疑小周报同线记者抄袭自己的深度报道和独家信源内容且不署名  
  > "I report for a daily metro paper" — [2026-10-23](https://www.reddit.com/r/Journalism/comments/1xd25ri/small_competitor_paper_is_stealing_my_work_is/)
- [Journalism|practitioner|强度3] 新非营利媒体独自报道谋杀案庭审，被大报几乎逐字改写抄袭，不知要求何种补救  
  > "a journalist much larger, more established paper just changed a few words here and there." — [2026-11-01](https://www.reddit.com/r/Journalism/comments/1xkpcxb/another_paper_plagiarized_my_work/)
- [Broadcasting|practitioner|强度2] 主控中枢(master control hub)集中播出,NBC电视台在橄榄球加时赛关键时刻误插广告并长时间黑屏冻结  
  > "Rolled station break right over the OT during a critical game ending play." — [2025-09-29](https://www.reddit.com/r/Broadcasting/comments/1nteu6i/master_control_hub_rolling_a_station_break_over/)
- [Broadcasting|student|强度2] 大学生电台节目毕业后想继续，考虑网络电台或播客  
  > "What is the best method for me to continue doing the show?" — [2026-05-20](https://www.reddit.com/r/Broadcasting/comments/1tikp99/what_is_the_best_way_to_continue_my_current_radio/)
- [Broadcasting|tv|强度2] 主控操作员常收不到NBC晚间新闻宣传片，经OTSM到达时节目早已播出  
  > "until long after the program has already aired" — [2026-06-25](https://www.reddit.com/r/Broadcasting/comments/1ufpsvk/nbc_promos_not_reaching_us_in_time_for_air/)
- [Journalism|editor|强度2] 独立在线新闻机构约75%读者来自社媒，Facebook降权外链和AI爬取后流量下滑，探讨转型  
  > "probably 75% of our readership comes from socials still" — [2026-07-11](https://www.reddit.com/r/Journalism/comments/1ut8xis/between_the_death_of_social_media_and_ai_crawlers/)
- [Journalism|freelancer|强度2] 编辑要看已发表剪报才肯约稿，但只有个人网站自发稿，纠结是否自发最佳稿件以免失去首发资格  
  > "before moving forward he wants to see my clips." — [2026-07-23](https://www.reddit.com/r/Journalism/comments/1v4qgn7/should_i_selfpublish_my_best_piece_if_i_need/)
- [Journalism|editor|强度2] 报社从纸媒优先转数字优先，需要技术栈、订阅、付费墙、newsletter和广告集成的经验  
  > "What tech stack does your newsroom use?" — [2026-07-24](https://www.reddit.com/r/Journalism/comments/1v5eyjq/what_is_your_newsrooms_tech_stack/)
- [Broadcasting|practitioner|强度2] 电视台推竖屏社媒内容直接上播且不重制作质量，线性新闻质量下降  
  > "My station has slowly been sacrificing its linear product to do more online content and the quality overall has suffered." — [2026-07-30](https://www.reddit.com/r/Broadcasting/comments/1vaoqps/vertical_social_posts_being_aired_on_news/)
- [Journalism|indie|强度2] 用Cargo Collective建站，每篇文章都要手工新建页面并在首页加链接，低效  
  > "At the moment, i have to create a new webpage and paste text onto it" — [2026-08-05](https://www.reddit.com/r/Journalism/comments/1vgbpar/website_for_a_journalism_startup/)
- [Journalism|freelancer|强度2] 想报道本地新兴移民餐饮，向本地商业报纸投稿不被重视  
  > "all the local media covers is traffic, crime, and the occasional state wide corruption story." — [2026-08-08](https://www.reddit.com/r/Journalism/comments/1vj2lev/absolute_lack_of_curiossirty/)

### S8 受众与变现（13 条强度≥2）

- [Journalism|editor|强度3] Google搜索流量消失，杂志数字内容预算归零，网络广告和联盟收入没了，读者以老年人为主  
  > "All the ways people would come across our website through google searches: gone." — [2026-08-23](https://www.reddit.com/r/Journalism/comments/1vwf2b7/nepo_baby_from_a_small_publishing_family_here_you/)
- [Journalism|practitioner|强度2] 地方记者人手极少、工作60+小时，却被读者抱怨广告和标题党  
  > "working 60+ hours a week with a skeleton of a newsroom covering everything from city hall to prep sports" — [2026-01-28](https://www.reddit.com/r/Journalism/comments/1qpnbuk/any_local_journalists_feeling_kind_of_let_down_by/)
- [Journalism|indie|强度2] 新办本地数字新闻平台，广告订阅短期无法支撑，找其他收入来源  
  > "can anyone here suggest alternative revenue streams to explore?" — [2026-06-23](https://www.reddit.com/r/Journalism/comments/1udr1yy/suggestions_for_nontraditional_revenue_streams/)
- [Journalism|editor|强度2] 独立在线新闻机构约75%读者来自社媒，Facebook降权外链和AI爬取后流量下滑，探讨转型  
  > "probably 75% of our readership comes from socials still" — [2026-07-11](https://www.reddit.com/r/Journalism/comments/1ut8xis/between_the_death_of_social_media_and_ai_crawlers/)
- [Journalism|indie|强度2] 家乡6000人小镇报纸萎缩，想独立办本地新闻，担心邮件通讯触达不到老年人  
  > "Any ideas for a way I can bring news back to my town independently?" — [2026-07-24](https://www.reddit.com/r/Journalism/comments/1v5g07t/small_town_local_news_is_dying/)
- [Journalism|editor|强度2] 报社从纸媒优先转数字优先，需要技术栈、订阅、付费墙、newsletter和广告集成的经验  
  > "What tech stack does your newsroom use?" — [2026-07-24](https://www.reddit.com/r/Journalism/comments/1v5eyjq/what_is_your_newsrooms_tech_stack/)
- [Journalism|tv|强度2] 本地电视台Facebook帖子下评论极其恶劣，记者担心人身安全  
  > "Are facebook commenters usually brutal?" — [2026-08-03](https://www.reddit.com/r/Journalism/comments/1vekv04/news_outlet_facebook_comments_are_they_usually/)
- [Broadcasting|practitioner|强度2] 区域新闻频道YouTube同步直播时电视广告段是否违反嵌入广告政策  
  > "getting our ad setup right on YouTube matters a lot to us." — [2026-08-14](https://www.reddit.com/r/Broadcasting/comments/1vo8yuz/policy_clarification_tv_ad_breaks_in_live_youtube/)
- [Journalism|editor|强度2] 本地Facebook群4万粉复制粘贴付费墙新闻且不署名，分流订阅用户，联系FB无果  
  > "It is causing an issue as they are stopping potential subscribers from signing up to our site" — [2026-09-30](https://www.reddit.com/r/Journalism/comments/1wuhj02/facebook_group_copying_and_pasting_content/)
- [Journalism|unknown|强度2] AI聚合与摘要使谷歌搜索导流下降、读者与记者脱节，聚合器应否存在  
  > "AI summaries and chatbots are completely disintermediating users from journalists." — [2026-10-04](https://www.reddit.com/r/Journalism/comments/1wxmqxm/what_do_journalists_think_of_aggregators_evil/)
- [Journalism|practitioner|强度2] 营销同事主张标题用"murder"以获取数字流量，与记者法律术语原则冲突  
  > "we’d have gotten more digital traction on a story with the use of murder in the headline" — [2026-10-12](https://www.reddit.com/r/Journalism/comments/1x4e30g/murder/)
- [Journalism|editor|强度2] 社区4万粉Facebook主页改写他人报道且不署名，指出后被骚扰  
  > "It regularly creates posts days after a story has run in another outlet." — [2026-10-12](https://www.reddit.com/r/Journalism/comments/1x4fkq1/fb_page_copy_and_pastes_news_articles_without/)

### S9 职业与生存（250 条强度≥2）

- [Broadcasting|practitioner|强度3] 新闻台主控员工连续7小时报道枪击事件后出现惊恐发作，想知道他人是否也有创伤反应  
  > "I woke up early this morning with a pretty bad panic attack that even medicine had a difficult time suppressing." — [2024-07-14](https://www.reddit.com/r/Broadcasting/comments/1e32yab/effects_of_major_breaking_news_on_the_psyche/)
- [Broadcasting|tv|强度3] 大市场电视导播15年后倦怠,想转行不知技能能否迁移  
  > "I am so burnt out and working tv news is just not what it used to be." — [2024-10-23](https://www.reddit.com/r/Broadcasting/comments/1gam43p/career_change_maybe/)
- [Broadcasting|practitioner|强度3] 15大市场电视新闻剪辑师干了9年，工时和管理让人倦怠，转行两年找不到出路  
  > "I am so burnt out with these horrible hours and horrible management." — [2024-10-27](https://www.reddit.com/r/Broadcasting/comments/1gczo7r/how_do_you_escape_this_failing_industry_advice/)
- [Journalism|tv|强度3] 十年本地电视摄像师大选夜后心灰意冷,工作十二小时半,曾因工作心脏病发作  
  > "I've literally had a heart attack doing this." — [2024-11-06](https://www.reddit.com/r/Journalism/comments/1gkvvmm/i_dont_know_how_to_do_my_job_anymore/)
- [Journalism|editor|强度3] 教了16年新闻学的大学教师在大选后怀疑新闻事实核查对公众已无意义，难以向学生解释这一行的价值  
  > "How am I supposed to have any legitimacy with students if the field they are choosing is just not trusted?" — [2024-11-08](https://www.reddit.com/r/Journalism/comments/1gm74bh/i_dont_know_if_i_believe_in_what_im_teaching/)
- [Broadcasting|tv|强度3] TEGNA强制员工做AI培训并要求保密,担心AI生成图像上电视和数字部门裁员  
  > "Not to mention how many layoffs will happen in the Digital departments." — [2024-11-13](https://www.reddit.com/r/Broadcasting/comments/1gqqex6/tegna_embracing_ai_told_employees_to_keep_quiet/)
- [Broadcasting|practitioner|强度3] 电视制作岗位担心被新的AI系统取代，不知道工会/罢工/政府介入能否阻止  
  > "someone who is legitimately afraid for his future" — [2024-11-21](https://www.reddit.com/r/Broadcasting/comments/1gwb4ac/what_can_really_be_done_at_this_point_for/)
- [Broadcasting|tv|强度3] TEGNA裁撤导播并试验由一名AI辅助制片人独自完成整档新闻,担心推广到突发新闻  
  > "experimenting with a single "AI-powered" producer "writing, coding" and "switching" ) an entire newscast by themselves" — [2024-11-23](https://www.reddit.com/r/Broadcasting/comments/1gxp3wt/what_happens_when_a_tech_bro_takes_over_your/)
- [Broadcasting|tv|强度3] Allen Media威斯康星四家电视台大裁员,多年主播被禁止入台,节目集中在麦迪逊  
  > "The Wisconsin Allen Media stations were gutted this week" — [2024-12-04](https://www.reddit.com/r/Broadcasting/comments/1h6nia1/the_bloodbath_in_wisconsin/)
- [Broadcasting|tv|强度3] 被裁导播警告TEGNA用AI自动化合并导播与制片职责且合同不透明  
  > "People being hired as producers are being kept in the dark until they basically sign a contract" — [2025-01-15](https://www.reddit.com/r/Broadcasting/comments/1i1vq9a/if_you_are_looking_to_get_into_this_industry_stay/)
- [Broadcasting|tv|强度3] Allen Media 22家电视台气象员全部被裁,改由亚特兰大集中录制,突发恶劣天气无预案  
  > "There is no specific plan in place right now for how severe/breaking weather will be handled." — [2025-01-17](https://www.reddit.com/r/Broadcasting/comments/1i38awy/confirmed_all_allen_media_mets_being_laid_off/)
- [Broadcasting|practitioner|强度3] 25大市场电视新闻制作人7年后倦怠：夜班带整个晨间节目、人员流失、咨询顾问每季度改制作方法、薪资不公  
  > "I’m exhausted, burnt out, and tired of consultants ripping everything we do and changing our producing methods once a quarter." — [2025-02-05](https://www.reddit.com/r/Broadcasting/comments/1iifzwe/i_fear_this_news_producing_career_is_just_not/)

## r/freelanceWriters 中的新闻类自由撰稿人：强度≥2 痛点（最多 15 条）

- [S9|强度3] 自己写的稿被AI检测软件判为近50%AI,无法修正  
  > "why are the scans showing that my work is 48-50% AI?" — [2023-01-24](https://www.reddit.com/r/freelanceWriters/comments/10kevp2/i_hate_ai/)
- [S9|强度3] 自己写的文章被客户的AI检测工具误判为41% AI,无从申辩  
  > "one of my articles which was 100% self-written was flagged by client's tool as 41% written by AI" — [2023-03-08](https://www.reddit.com/r/freelanceWriters/comments/11lo0o3/ai_detector_claiming_my_100_selfwritten_article/)
- [S9|强度3] 硅谷银行倒闭导致初创客户暂停合同、无法付款,不知是否协商部分付款  
  > "if my clients claim inability to pay due to loss of the funds in their bank accounts, should I negotiate for partial payment?" — [2023-03-11](https://www.reddit.com/r/freelanceWriters/comments/11oojae/anyone_else_affected_by_the_silicon_valley_bank/)
- [S9|强度3] 内容农场改用AI初稿,改稿稿酬降至每词1美分,主要收入丧失  
  > "one cent a word, and even less than that for some articles" — [2023-03-17](https://www.reddit.com/r/freelanceWriters/comments/11trkvz/ive_essentially_lost_my_main_source_of_income_to/)
- [S9|强度3] 最大客户因利润考虑改用ChatGPT,主要收入来源消失  
  > "I literally lost my biggest and best client to ChatGPT today." — [2023-04-08](https://www.reddit.com/r/freelanceWriters/comments/12ff5mw/it_happened_to_me_today/)
- [S9|强度3] 神经多样性自由文案因AI失去六位数收入,出现严重焦虑  
  > "I cry at least 5 times a day, every day." — [2023-06-05](https://www.reddit.com/r/freelanceWriters/comments/141qvna/the_ai_mania_is_destroying_my_mental_health_and_i/)
- [S9|强度3] 呕心写出的技术稿被客户用Winston AI判为仅35%人写而拒稿  
  > "yet this morning i got a message from the client that they're rejecting my text" — [2023-11-22](https://www.reddit.com/r/freelanceWriters/comments/1817b4p/how_the_hell_do_you_deal_with_ai_detectors/)
- [S9|强度3] 接连失去两个客户,一个改用AI,另一个把稿酬降到最低价的三分之一  
  > "their new rate for writers is three times smaller than my minimum" — [2024-02-01](https://www.reddit.com/r/freelanceWriters/comments/1afxi83/lost_my_second_client_thanks_to_ai_losing_all/)
- [S7|强度3] 稿件已提交三周未发布,编辑多次邮件不回,选题时效过期  
  > "I submitted the article 3 weeks ago and it still hasn't run." — [2024-03-01](https://www.reddit.com/r/freelanceWriters/comments/1b3xs6z/my_editor_ghosted_me/)
- [S9|强度3] 客户用AI检测截图指控文章80%为AI写作,不知如何自证  
  > "Received a message from a client with a screenshot of a detector showing my article as 80% AI written." — [2024-07-15](https://www.reddit.com/r/freelanceWriters/comments/1e3xf5v/accused_of_using_ai_for_the_first_time/)
- [S9|强度3] 游戏新闻记者因截图未署名被TheGamer开除后被GameRant拉黑，多家站点拒稿，想换赛道或转领域  
  > "GameRant informed me I’m banned from applying to their gaming department" — [2025-02-05](https://www.reddit.com/r/freelanceWriters/comments/1ii4f4j/a_niche_change_or_change_of_field/)
- [S7/S9|强度3] 新人自由撰稿人找不到具体的选题邮件范例，一年来仍不知道如何向网络刊物投稿艺术文化文章  
  > "how the hell do you pitch an article to an online publication?" — [2025-02-24](https://www.reddit.com/r/freelanceWriters/comments/1ix7w8g/can_someone_explain_to_me_how_to_pitch_an_article/)
- [S9|强度3] 有三家千字一美元媒体署名的作者，不断收到申请职位后被转为无偿稿约的请求，觉得被冒犯  
  > "Pro-bono offers are so insulting when you have rent, bills and other expenses piling up" — [2025-03-30](https://www.reddit.com/r/freelanceWriters/comments/1jnbekp/explosion_of_free_work_requests/)
- [S9|强度3] 自由撰稿市场萎缩,两年找不到写作工作,不知转哪个方向  
  > "have now spent more than 2 years futilely searching for writing jobs" — [2025-04-06](https://www.reddit.com/r/freelanceWriters/comments/1jsouwo/which_writing_field_do_you_suggest/)
- [S8/S9|强度3] NewsBreak创作者写了1200篇食谱、3万粉丝无违规，却被无解释地取消变现和发帖资格，三次邮件无回复  
  > "they erased me from monetization or even posting" — [2025-04-16](https://www.reddit.com/r/freelanceWriters/comments/1k0jhvv/questions_for_newsbreak_creators_in_firings/)

## 提到的工具 Top 25（相关帖）

linkedin(17), substack(10), cuez(9), upwork(8), chatgpt(8), ai(7), wordpress(7), otter.ai(7), medium(6), youtube(6), enps(5), ai detector(5), indeed(4), newsbreak(4), google(4), instagram(4), obs(4), static media(4), facebook(4), google docs(3), twitter(3), reddit(3), ghost(3), slack(3), perplexity(3)
