# Reddit 记者原话编码分析

- 语料：r/Journalism, r/freelanceWriters, r/Broadcasting, r/FOIA, r/Substack, r/PoliceScanner 的 search.rss，按约 60 个主题关键词检索（relevance/all + top/year），去重后 4,791 帖；取 2023 年起、正文 >150 字的自述帖 2353 条逐条人工编码（规则见 scripts/reddit_coding_schema.md，逐帖编码见 raw/reddit_coded_*.jsonl）。
- 相关帖 1822 条。
- **局限（必读）**：样本由关键词驱动，且 r/freelanceWriters 体量大，各环节/群体的**绝对占比不代表记者总体**，只能用于：①同一群体内部比较各环节；②提取原话证据；③发现问卷没覆盖的具体痛点。`wants_tool` 各编码批次标准不一（批次1 偏宽），仅作参考。

## 环节 × 群体：帖数 / 平均强度(0–3)

| 环节 | LOCAL | TV | INDIE | NATL | FREE | 强度3帖数 |
|---|---|---|---|---|---|---|
| S1 发现线索 | 51 / 1.5 | 6 / 1.5 | 13 / 1.7 | 15 / 0.7 | 56 / 1.5 | 7 |
| S2 背景研究 | 38 / 1.5 | 1 / 2.0 | 28 / 1.6 | 38 / 1.1 | 30 / 1.6 | 15 |
| S3 找信源 | 32 / 1.9 | 5 / 1.6 | 15 / 1.9 | 6 / 1.0 | 60 / 1.8 | 20 |
| S4 采访与素材 | 17 / 2.0 | 2 / 1.5 | 8 / 1.6 | 8 / 1.4 | 37 / 1.8 | 10 |
| S5 核实 | 25 / 2.0 | 5 / 2.2 | 17 / 1.3 | 18 / 1.3 | 18 / 1.7 | 10 |
| S6 写作与制作 | 65 / 1.8 | 42 / 1.5 | 23 / 1.5 | 8 / 1.5 | 91 / 1.6 | 31 |
| S7 发布与分发 | 31 / 1.6 | 2 / 1.5 | 57 / 1.3 | 10 / 1.1 | 132 / 1.5 | 17 |
| S8 受众与变现 | 37 / 1.5 | 2 / 2.5 | 74 / 1.3 | 4 / 0.2 | 17 / 1.1 | 9 |
| S9 职业与生存 | 178 / 2.0 | 185 / 1.9 | 41 / 1.7 | 75 / 1.9 | 500 / 1.7 | 220 |

## 条线分布（相关帖，可多选）

- 其他: 1370
- 市政: 105
- 商业: 103
- 教育: 59
- 治安: 54
- 选举: 40
- 健康: 36
- 体育: 29
- 法院: 28
- 环境: 11
- 灾害天气: 9

## 提及工具 Top 30

substack(87), chatgpt(39), linkedin(29), upwork(21), ai(21), otter.ai(14), twitter(12), medium(12), reddit(11), google(11), facebook(10), otter(10), wordpress(9), youtube(9), foia(8), python(7), ai detector(7), instagram(7), google docs(6), indeed(6), grammarly(5), lexisnexis(5), tiktok(5), slack(5), inews(5), enps(5), google sheets(4), excel(4), notion(4), haro(4)

## 各环节高强度原话（强度≥2，每环节最多 20 条，按强度降序）


### S1 发现线索

- [FREE/LOCAL|freelancer|强度3] 选题被本地报接受并完成采访写作后编辑失联两个月,其他刊物也不回；凑合：多次邮件追问  
  > "So now I'm just here with a whole story written out and no one to publish it." — [r/freelanceWriters 2024-01-08](https://www.reddit.com/r/freelanceWriters/comments/192042m/ghosted/)
- [FREE|freelancer|强度3] 搬到大城市后转做自由记者,去议会和闲逛都找不到选题,不明白别人如何得到特稿线索；凑合：逛社区、与当地人聊天、旁听市议会  
  > "I have no idea where to even begin looking for stories." — [r/Journalism 2024-04-03](https://www.reddit.com/r/Journalism/comments/1buq8ya/transitioning_into_a_freelance_journalism_career/)
- [LOCAL|practitioner|强度3] 自己发现并提交给编辑的新闻线索被编辑拿走自己写；凑合：—  
  > "I pitched a news story to my news editor & then she took it." — [r/Journalism 2024-10-01](https://www.reddit.com/r/Journalism/comments/1ftg10q/i_pitched_a_news_story_to_my_news_editor_then_she/)
- [LOCAL|practitioner|强度3] 小周报只有两名全职记者,传闻ICE突袭当地高中却不知如何证实及找公开记录；凑合：联系教师希望有人开口  
  > "How can we know when, where they took place? Are there any public documents that can be of help?" — [r/Journalism 2025-01-28](https://www.reddit.com/r/Journalism/comments/1icdc3f/how_should_we_cover_ice_raids/)
- [INDIE|editor|强度3] 小型科技媒体新闻编辑要增加每日报道量,现有RSS、网页变更监测、邮件和公关外联全靠人工；凑合：RSS、网页变化追踪、社媒、通讯、联系公关  
  > "Right now, our news tracking is very manual." — [r/Journalism 2025-02-03](https://www.reddit.com/r/Journalism/comments/1ign1a8/what_are_your_niche_news_tracking_tools_and/)
- [LOCAL|practitioner|强度3] 住房记者覆盖九个县共109个市县政府,需要自动抓取议程并按关键词筛选；凑合：—  
  > "I cover housing in a nine-county region with 109 seperate municipal and county governments." — [r/Journalism 2025-03-06](https://www.reddit.com/r/Journalism/comments/1j51l2t/best_way_to_scrape_city_council_agendas/)
- [LOCAL|practitioner|强度3] 因稿件乱、遗漏多、编辑耗时被考察,过度依赖社媒找选题,想求提升资源；凑合：—  
  > "I'm on probation at work because my writing is messy and omits too much" — [r/Journalism 2025-08-15](https://www.reddit.com/r/Journalism/comments/1mqjbxk/my_stories_require_too_much_editing_and_i_rely/)
- [?|practitioner|强度2] Twitter趋势不好用,需要发现热门话题的平台/软件；凑合：Reddit首页、LinkedIn News  
  > "where do you turn to for trending stories?" — [r/Journalism 2023-03-29](https://www.reddit.com/r/Journalism/comments/125tpms/how_do_you_find_trending_stories_platform/)
- [FREE|freelancer|强度2] 投稿对象太多、有独家条款,每天写pitch找刊物压力大；凑合：LinkedIn找工作无效  
  > "there are soo many publications to pitch to" — [r/Journalism 2023-07-13](https://www.reddit.com/r/Journalism/comments/14yq2pw/how_much_time_a_day_do_you_spend_writing_pitches/)
- [TV|tv|强度2] 跟进多个话题/线路怕漏掉选题,想整合现有工具；凑合：Google日历、Drive、书签、通讯录  
  > "is there a better way to organize my work and integrate the tools I am already using?" — [r/Journalism 2023-09-06](https://www.reddit.com/r/Journalism/comments/16bhydq/how_to_avoid_missing_out_on_story_ideas_about/)
- [FREE|freelancer|强度2] 欧洲初级记者本国行业萎缩,想向外国杂志投稿但英文写作不够好,考虑母语写作再翻译；凑合：母语写作后翻译  
  > "the problem is my english writing is not nearly good enough for print" — [r/freelanceWriters 2023-09-24](https://www.reddit.com/r/freelanceWriters/comments/16qvgnu/pitch_foreign_editors/)
- [FREE|freelancer|强度2] 想借鉴外语主流媒体已报道过的企业选题做新稿,不确定是否合规；凑合：—  
  > "Part of me feels like this is standard practice" — [r/Journalism 2023-09-28](https://www.reddit.com/r/Journalism/comments/16uk9vy/story_ideas_that_have_been_done_before_in_other/)
- [FREE|aspiring|强度2] 非专业写作者不知何时算准备好向全国杂志投稿；凑合：—  
  > "I have a story, but I'm apprehensive about pitching." — [r/freelanceWriters 2023-10-01](https://www.reddit.com/r/freelanceWriters/comments/16x1n2v/when_will_i_know_im_ready_to_pitch_a_national/)
- [LOCAL|practitioner|强度2] 周报总编害怕某周无新闻可写、版面空白,不住在报道区缺乏地面线索；凑合：—  
  > "My worst fear is that one week will go by with zero news and the front page of the paper will be blank!" — [r/Journalism 2024-02-13](https://www.reddit.com/r/Journalism/comments/1aq2w4f/journalist_working_for_weekly_paper_dealing_with/)
- [FREE|freelancer|强度2] 杂志用投稿表单收选题,从来没回音,不知该填表还是直接找编辑；凑合：—  
  > "While they assure writers that an editor reads the pitches, I have serious doubts because I never hear back." — [r/freelanceWriters 2024-02-20](https://www.reddit.com/r/freelanceWriters/comments/1avuhnp/do_people_hear_back_after_using_submissions_forms/)
- [FREE|freelancer|强度2] 网站关停、选题不断被拒,年轻自由记者难积累作品；凑合：—  
  > "your pitches are constantly getting shot down" — [r/Journalism 2024-02-23](https://www.reddit.com/r/Journalism/comments/1ayasdl/those_of_you_who_freelance_how_are_you_doing/)
- [FREE|student|强度2] 新闻硕士新生在新城市找不到值得写的选题,议会/新闻稿/法庭案件被老师说不算真正的新闻；凑合：看议会、新闻稿、法庭案件  
  > "How do I find stories on my own" — [r/Journalism 2024-03-06](https://www.reddit.com/r/Journalism/comments/1b7ydia/advice_for_newbie/)
- [NATL|practitioner|强度2] 市场记者需要免费的信源/社交监测工具聚合网络信息发现选题,编辑有Newswhip但自己没有；凑合：以前用过DataMinr和TweetDeck  
  > "I’m looking for some sort of sourcing tool to find story ideas from." — [r/Journalism 2024-04-03](https://www.reddit.com/r/Journalism/comments/1bv30zp/any_useful_free_sourcingsocial_media_monitoring/)
- [FREE|aspiring|强度2] 有很多话题却不知道如何变成编辑感兴趣的故事；凑合：—  
  > "I have a lot of topics/ideas but I don't know how to turn them into stories that would be interesting for editors" — [r/Journalism 2024-04-06](https://www.reddit.com/r/Journalism/comments/1bxlf21/how_to_turn_ideas_into_stories/)
- [FREE|practitioner|强度2] 想兼职做自由撰稿,怕离开全职新闻岗位后失去线索和人脉,写不出选题；凑合：—  
  > "Do you still manage go build a proper network as a 'part time' journalist?" — [r/Journalism 2024-04-21](https://www.reddit.com/r/Journalism/comments/1c9rycn/anyone_who_started_freelancing_on_the_side_does/)

### S2 背景研究

- [FREE|student|强度3] 申请乔治亚州房产记录被私营公司承包商拖延、索高价、只给部分数据；凑合：升级给县首席估价员  
  > "The CEO of that company then has been trying his best to delay or find excuses to not comply with my Open Records Request" — [r/FOIA 2023-08-11](https://www.reddit.com/r/foia/comments/15oirna/georgia_foia_orr_request_being_purposefully/)
- [INDIE/FREE|freelancer|强度3] 独立记者因不隶属新闻机构被警局拒绝提供事故报告；凑合：想找新闻机构同行代为申请  
  > "told they won't release the report to me because I am not employed by a news agency" — [r/Journalism 2024-06-29](https://www.reddit.com/r/Journalism/comments/1dr67cc/advice_on_foia_requests_for_lvmpd/)
- [LOCAL|practitioner|强度3] 公共记录请求被州机构拖延,短期研究员奖金即将结束,不知何时该诉讼；凑合：多次邮件和电话催促  
  > "I have sent three messages and not received a response." — [r/Journalism 2024-08-12](https://www.reddit.com/r/Journalism/comments/1eqm63j/at_what_point_do_you_start_to_consider_a_lawsuit/)
- [?|unknown|强度3] 陆军FOIA高度分散,找不到申诉渠道,邮件无人回复,档案5年后将销毁；凑合：只能发邮件,无法邮寄或诉讼  
  > "Army FOIA is so decentralized that there's no single point for appeals" — [r/FOIA 2024-08-19](https://www.reddit.com/r/foia/comments/1evy1o1/appellate_authority_simply_cannot_be_found/)
- [LOCAL|practitioner|强度3] 县党委会公开会议禁止录音录像并叫警察,记者不确定开放会议法是否允许录音；凑合：拒绝承诺不录音,仅用电脑打字  
  > "Cops were called to trespass, but the other members didn't make a motion to oust me" — [r/Journalism 2025-01-22](https://www.reddit.com/r/Journalism/comments/1i73x45/open_meeting_law_audiovisual_recording/)
- [FREE|practitioner|强度3] 每篇稿件有笔记、草稿、照片、新闻稿等多个文档,Google Drive混乱,同时做三份工作；凑合：每篇稿件建文件夹,试用Scrivener和Notion  
  > "my Google Docs is a DISASTER" — [r/Journalism 2025-01-25](https://www.reddit.com/r/Journalism/comments/1i9us8w/document_organization_tools_programs/)
- [LOCAL|practitioner|强度3] 小周报只有两名全职记者,传闻ICE突袭当地高中却不知如何证实及找公开记录；凑合：联系教师希望有人开口  
  > "How can we know when, where they took place? Are there any public documents that can be of help?" — [r/Journalism 2025-01-28](https://www.reddit.com/r/Journalism/comments/1icdc3f/how_should_we_cover_ice_raids/)
- [LOCAL|practitioner|强度3] 住房记者覆盖九个县共109个市县政府,需要自动抓取议程并按关键词筛选；凑合：—  
  > "I cover housing in a nine-county region with 109 seperate municipal and county governments." — [r/Journalism 2025-03-06](https://www.reddit.com/r/Journalism/comments/1j51l2t/best_way_to_scrape_city_council_agendas/)
- [LOCAL|practitioner|强度3] 镇政府对邮件类FOIA开出$21,710人工费并拖到延期最后一天；凑合：—  
  > "A township is requesting $21,710.12 in labor charges for a pretty reasonable FOIA request" — [r/Journalism 2025-11-12](https://www.reddit.com/r/Journalism/comments/1outzbf/a_township_is_requesting_2171012_in_labor_charges/)
- [INDIE|practitioner|强度3] 州游说披露记录混乱、无法按法案拆分,难以识别各方并做可发表的汇总与方法说明；凑合：—  
  > "What’s your method for building an accurate “who counts” list from messy client names and inconsistent reporting?" — [r/Journalism 2025-12-23](https://www.reddit.com/r/Journalism/comments/1ptvzdm/lobbying_data_how_to_id_the_right_players_make/)
- [FREE/INDIE|freelancer|强度3] YouTube纪录片频道靠FOIA获取案件视频(讯问、执法记录仪),太慢导致选题过时；凑合：FOIA申请;考虑办记者证  
  > "the process is so slow that the story often goes stale by the time I receive the videos" — [r/Journalism 2026-01-08](https://www.reddit.com/r/Journalism/comments/1q7c9vb/does_anybody_has_any_idea_if_the_uspa/)
- [FREE/INDIE|freelancer|强度3] FOIA收费估价高达数千美元且可能更高,想知记者证能否免费用；凑合：—  
  > "Is there a way to get fee waiver through press card?" — [r/FOIA 2026-01-08](https://www.reddit.com/r/foia/comments/1q7cy70/why_are_foia_requests_so_expensive/)
- [NATL|practitioner|强度3] AI垃圾与带幻觉统计的“可信”媒体让金融记者80%时间花在找可靠数据上；凑合：—  
  > "At this point, I’m spending 80% of my time on research" — [r/Journalism 2026-04-02](https://www.reddit.com/r/Journalism/comments/1safhc0/is_anyone_else_spending_more_time_finding_data/)
- [INDIE|practitioner|强度3] 警察不当行为线索只有警员姓名和警号,德州公共信息请求(TPIA)被拒；凑合：向奥斯汀提出TPIA申请  
  > "The TPIA request (Austin, TX) I filed was just denied." — [r/Journalism 2026-04-30](https://www.reddit.com/r/Journalism/comments/1szxjcr/help_getting_records_on_cop_with_just_his_name/)
- [?|unknown|强度3] 伊利诺伊警方执法记录仪记录请求多次被以隐私豁免拒绝，想重新申请绕开；凑合：已向州检察长申请审查  
  > "How do I request the records again to get around this?" — [r/FOIA 2026-06-01](https://www.reddit.com/r/foia/comments/1ttvc4r/repeated_denials_for_body_cam_illinois/)
- [LOCAL|practitioner|强度2] 调查时需快速背景核查,各辖区逮捕/法院记录不统一,背景查询网站计费有坑；凑合：谷歌搜索,试过Truthfinder/Intelius  
  > "Arrest and court records vary so much by jurisdiction." — [r/Journalism 2023-01-22](https://www.reddit.com/r/Journalism/comments/10il6ju/background_check_sites/)
- [LOCAL|practitioner|强度2] 五年竞选财务记录是栅格化PDF,不想手工转录,需要转成表格的工具；凑合：—  
  > "I'm looking for a tool that I can use to convert the rasterized PDFs to spreadsheets." — [r/Journalism 2023-05-03](https://www.reddit.com/r/Journalism/comments/1370yuq/reccomend_a_tool_convert_pdf_to_a_spreadsheet/)
- [?|unknown|强度2] 想通过公开记录申请拿到已结案凶杀案的全部材料,不知如何措辞；凑合：—  
  > "What do you recommend I add, change or reword in order to be sure I get everything?" — [r/Journalism 2023-07-30](https://www.reddit.com/r/Journalism/comments/15da0g9/what_exactly_to_request_in_open_records_request/)
- [NATL|practitioner|强度2] 常用的背景段落存在旧邮件和Word里,查找复用低效；凑合：从旧邮件和Word复制粘贴  
  > "I usually copy and past them from my earlier emails or search for them through my old work word documents." — [r/Journalism 2023-09-04](https://www.reddit.com/r/Journalism/comments/169q1mf/what_are_the_best_methods_or_apps_to_save_and/)
- [FREE|student|强度2] 资料、信源和笔记分散在浏览器书签、苹果备忘录、纸质等多处；凑合：书签+Apple备忘录+自发短信+纸质  
  > "I have bookmarks on my internet browser, notes on Apple devices, texts to myself, papers in my backpack" — [r/Journalism 2023-09-27](https://www.reddit.com/r/Journalism/comments/16tt3sw/where_do_you_compile_your_resources_sources_and/)

### S3 找信源

- [LOCAL|practitioner|强度3] 学校/大学把采访请求统一转给媒体联络员,延误截稿；凑合：直接联系PR建立关系  
  > "I can't afford to waste my time waiting for one person to approve and coordinate multiple interview requests on a deadline." — [r/Journalism 2023-10-25](https://www.reddit.com/r/Journalism/comments/17gcib8/education_reporting_k12_and_university_admins/)
- [FREE|student|强度3] 新闻学生追信源回复压力大致倦怠,轮椅使用者采访地点不无障碍,学生记者难约访；凑合：教授同意延长截止日期  
  > "I am already experiencing burnout from the stress of chasing sources" — [r/Journalism 2024-01-19](https://www.reddit.com/r/Journalism/comments/19ac4yn/journalism_school_and_burnout/)
- [INDIE/FREE|freelancer|强度3] 独立记者因不隶属新闻机构被警局拒绝提供事故报告；凑合：想找新闻机构同行代为申请  
  > "told they won't release the report to me because I am not employed by a news agency" — [r/Journalism 2024-06-29](https://www.reddit.com/r/Journalism/comments/1dr67cc/advice_on_foia_requests_for_lvmpd/)
- [FREE|freelancer|强度3] 趋势稿找不到普通人信源,Reddit各版拒绝发征集帖；凑合：尝试10多个subreddit,LinkedIn/Twitter作为最后手段  
  > "Does anyone have tips for finding “real people” for stories ?" — [r/Journalism 2024-06-30](https://www.reddit.com/r/Journalism/comments/1dsasdl/trouble_finding_real_person_sources_any_tips/)
- [INDIE|freelancer|强度3] 独立通讯作者找不到特稿信源,HARO被收购后失效,Reddit发帖被删,直接联系太耗时；凑合：直接逐个联系信源  
  > "Previously, I used to rely on HARO but now that it is acquired it isn't nearly as helpful." — [r/Journalism 2024-07-09](https://www.reddit.com/r/Journalism/comments/1dyy3fu/how_do_you_find_sources_for_your_articles/)
- [FREE|aspiring|强度3] 退伍军人想做战地自由记者但缺钱缺门路,联系的人都没回应；凑合：私信所有去过乌克兰的记者  
  > "I feel like I'm clawing at the gates but I can't get in." — [r/Journalism 2024-07-19](https://www.reddit.com/r/Journalism/comments/1e7cn6g/how_to_start_freelancing/)
- [LOCAL/INDIE|practitioner|强度3] 一篇被视为带政治倾向的稿件导致当地组织拒绝向报纸提供消息,新手不知如何回应；凑合：—  
  > "Now they don't want any of their organization's news in the paper." — [r/Journalism 2024-09-19](https://www.reddit.com/r/Journalism/comments/1fkcjpb/newer_to_journalism_and_experiencing_my_first/)
- [LOCAL|practitioner|强度3] 市政府新闻官和议员对记者敌意,拒绝回答问题,批评性报道抹去已建立的关系；凑合：—  
  > "most of the council members refuse to answer questions" — [r/Journalism 2024-10-17](https://www.reddit.com/r/Journalism/comments/1g61h34/dealing_with_hostile_city_government/)
- [?|tool_builder|强度3] HARO式邮件找信源收到大量无关、自动化回复,筛选耗时；凑合：HARO、SOS等邮件列表  
  > "Get flooded with hundreds of responses, many automated or irrelevant" — [r/Journalism 2024-11-11](https://www.reddit.com/r/Journalism/comments/1gp2n5a/can_we_talk_about_the_state_of_haro/)
- [?|student|强度3] 内向的新闻系新生每个作业都要采访陌生人而压力极大,考虑转专业；凑合：—  
  > "I couldn’t bring myself to walk up to interview someone" — [r/Journalism 2024-12-09](https://www.reddit.com/r/Journalism/comments/1ha4vei/journalism_major_crisis/)
- [LOCAL|practitioner|强度3] 小周报只有两名全职记者,传闻ICE突袭当地高中却不知如何证实及找公开记录；凑合：联系教师希望有人开口  
  > "How can we know when, where they took place? Are there any public documents that can be of help?" — [r/Journalism 2025-01-28](https://www.reddit.com/r/Journalism/comments/1icdc3f/how_should_we_cover_ice_raids/)
- [?|tool_builder|强度3] HARO关闭后,Qwoted上充满无关推销,记者花大量时间筛选专家信源；凑合：Qwoted  
  > "Qwoted is flooded with irrelevant pitches, self-promoters, and low-quality responses" — [r/Journalism 2025-02-01](https://www.reddit.com/r/Journalism/comments/1if2tde/how_do_you_feel_about_finding_expert_sources/)
- [LOCAL|practitioner|强度3] 主编要求全员把个人行业联系人共享进公司共享文档数据库；凑合：上Reddit确认是否正常  
  > "the team has to disclose all our personal industry contacts with the whole team" — [r/Journalism 2025-04-01](https://www.reddit.com/r/Journalism/comments/1jp4i22/print_media_managing_editor_asking_to_share_all/)
- [TV|tv|强度3] CBS新闻高层决策导致信源拒绝采访,转去接受竞争对手NBC采访,影响与信源关系；凑合：—  
  > "I didn’t realize it would impact our ability to build relationships with sources." — [r/Journalism 2026-02-12](https://www.reddit.com/r/Journalism/comments/1r2zkmt/bari_weiss_destruction_of_cbs_news_goes_deeper/)
- [FREE|student|强度3] 受访者临时爽约反复改期,耽误专题截稿；凑合：—  
  > "basically lost a whole week waiting for Friday" — [r/Journalism 2026-02-14](https://www.reddit.com/r/Journalism/comments/1r4p71i/how_do_you_guys_deal_with_unprofessionalflakey/)
- [INDIE|practitioner|强度3] Live Nation采访申请门户审批标准不透明,小媒体批准而自己被拒,还破坏与艺人团队关系；凑合：—  
  > "the inconsistency of the deciding factors per tour or per specific show, opacity of the approvals process" — [r/Journalism 2026-04-18](https://www.reddit.com/r/Journalism/comments/1soimtn/fellow_music_journalists_has_anyone_cracked_the/)
- [FREE|freelancer|强度3] 想写心理健康和社会工程话题，找不到愿意付费的刊物，写作数据库都已用尽；凑合：用Google Alerts加关键词、跟踪付费作者  
  > "Do you have any other ideas how I can find publications on these topics that are actively looking for writers and are willing to pay?" — [r/freelanceWriters 2026-06-02](https://www.reddit.com/r/freelanceWriters/comments/1tuplfj/3_challenging_questions/)
- [FREE|freelancer|强度3] GenAI后B2B写作收入崩塌，付费刊物名单失效、职位板泛滥骗局，找不到付费稿源；凑合：用WhoPays Writers、求职板、LinkedIn/Talkwalker关键词快讯、反查署名均无果  
  > "I made a good living from B2B freelance writing up until GenAI." — [r/freelanceWriters 2026-06-07](https://www.reddit.com/r/freelanceWriters/comments/1tzgarj/here_is_what_i_have_tried_where_do_i_go_from_here/)
- [LOCAL|practitioner|强度3] 信源协议用电子签署，信源因担心云端而改走邮寄，耽误数日导致独家被对手抢先；凑合：改用邮寄纸质签名  
  > "I shot it over with Xodo Sign so he could just tap it on his screen" — [r/Journalism 2026-08-13](https://www.reddit.com/r/Journalism/comments/1vn7j6g/lost_a_3week_scoop_to_the_physical_mail_system/)
- [LOCAL|practitioner|强度3] 郊区各市官员拒绝受访、雇公关控制接触，甚至会后把记者驱逐出市政厅；凑合：与发言人交朋友、请官员喝咖啡  
  > "Many elected officials refuse to talk to me or my fellow reporters anymore" — [r/Journalism 2026-08-19](https://www.reddit.com/r/Journalism/comments/1vsnu8n/sudden_jump_in_local_governments_hatred_of_local/)

### S4 采访与素材

- [LOCAL|practitioner|强度3] 受伤无法长时间打字,Otter.ai年费涨到240美元,Gannett低薪负担不起,找平价转写；凑合：用Otter.ai录音后搜索引文  
  > "Otter recently up-ed their price from $99 to $119 to NOW $240 per year!" — [r/Journalism 2023-11-22](https://www.reddit.com/r/Journalism/comments/181ewnu/otterai_transcription_service_price_change/)
- [FREE|freelancer|强度3] 采访艺术家回答极短、非母语,稿件被退回要求补充介绍；凑合：事后发邮件追问  
  > "I did the interview with the artist and it went terribly." — [r/freelanceWriters 2024-02-13](https://www.reddit.com/r/freelanceWriters/comments/1aq3asb/feeling_very_dejected_at_the_moment/)
- [FREE|freelancer|强度3] 弄丢未备份的录音机,只剩笔记,不知大刊是否接受并如何事实核查；凑合：联系信源重新确认  
  > "I recently lost my audio recorder, which had a few files in it that I hadn't backed up yet." — [r/Journalism 2024-05-25](https://www.reddit.com/r/Journalism/comments/1d01q3l/how_to_proceed_with_fact_checking_after_lost/)
- [?|practitioner|强度3] 电话采访录音应用不稳定,常担心没录全,Otter太贵；凑合：手机语音备忘录上传到Alice转写  
  > "I have to cross my fingers for good luck that it records my whole conversation." — [r/Journalism 2024-07-07](https://www.reddit.com/r/Journalism/comments/1dxmdel/voice_transcription_for_interviews/)
- [LOCAL|practitioner|强度3] 小镇报社编辑突然离职,新人独自承担大部分现场报道,疲惫且采访时间难以拉长；凑合：远程编辑协助  
  > "I am exhausted. I am struggling to make interview times break ten minutes" — [r/Journalism 2025-01-18](https://www.reddit.com/r/Journalism/comments/1i4ke7g/3_months_into_my_first_journalism_job_and_i_am/)
- [LOCAL|practitioner|强度3] 县党委会公开会议禁止录音录像并叫警察,记者不确定开放会议法是否允许录音；凑合：拒绝承诺不录音,仅用电脑打字  
  > "Cops were called to trespass, but the other members didn't make a motion to oust me" — [r/Journalism 2025-01-22](https://www.reddit.com/r/Journalism/comments/1i73x45/open_meeting_law_audiovisual_recording/)
- [INDIE/FREE|freelancer|强度3] 调查冤案多年,多种录音同意情形下的使用权限不明,律师报价太高；凑合：上Reddit求教并考虑咨询媒体律师  
  > "I need to consult a media attorney" — [r/Journalism 2025-03-14](https://www.reddit.com/r/Journalism/comments/1jbaq7w/wrongful_conviction_investigation/)
- [FREE|student|强度3] 学生多媒体记者报道四天活动:搭讪嘉宾、拍摄、压缩素材成2分钟包装、先写VO还是先采访、熬夜剪辑；凑合：边采访边“摸索”再写VO  
  > "Having trouble with condensing so much footage" — [r/Journalism 2026-03-12](https://www.reddit.com/r/Journalism/comments/1rrwt7n/advice_appreciated_student_journalist_covering_a/)
- [FREE|student|强度3] 视频包装的采访音频很差无法重录,明天截止,怎么用Premiere Pro修复；凑合：—  
  > "How on earth do I fix my audio in Premiere Pro?" — [r/Journalism 2026-04-13](https://www.reddit.com/r/Journalism/comments/1sk8itv/student_video_crisis/)
- [FREE|freelancer|强度3] 积压大量采访音频，手工转写拖慢交稿，免费工具遇噪音或多人插话就失效，付不起每月30美元订阅；凑合：试用免费转写工具  
  > "typing everything out manually is killing my turnaround time." — [r/Journalism 2026-07-21](https://www.reddit.com/r/Journalism/comments/1v2ffjr/best_transcription_workflow_for_freelance/)
- [FREE|practitioner|强度2] 在智利报道需要能转写西班牙语的转写服务,otter.ai不支持；凑合：现用otter.ai  
  > "need a transcription service that at least transcribes Spanish" — [r/Journalism 2023-03-27](https://www.reddit.com/r/Journalism/comments/123bjc3/looking_for_a_transcription_service_for_spanish/)
- [NATL|practitioner|强度2] 30场一小时访谈已转写,需要能给片段打主题标签并跨访谈检索的软件；凑合：—  
  > "I'm looking for some kind of software where I can quickly tag different sections of each interview with subtopic labels." — [r/Journalism 2023-04-08](https://www.reddit.com/r/Journalism/comments/12fnh7c/interview_tracking_organizing_software/)
- [?|practitioner|强度2] 新闻伦理禁止预发问题/邮件采访,但跨时区电话采访耗时且非母语信源难沟通；凑合：—  
  > "I've spent countless hours trying to organize phone interviews across different time zones." — [r/Journalism 2023-05-26](https://www.reddit.com/r/Journalism/comments/13shx7a/why_cant_we_let_interviewees_prepare_for_their/)
- [LOCAL|practitioner|强度2] 在学校董事会/议会等大房间会议录音,手机收不到远处发言还收杂音；凑合：用Galaxy S23 Ultra手机录音  
  > "it just can't pick up voices of those farther away" — [r/Journalism 2023-08-19](https://www.reddit.com/r/Journalism/comments/15vl83l/looking_for_microphone_recommendations_for_public/)
- [FREE|student|强度2] 新闻课新手首次采访写200-300词新闻简讯,不知如何问对问题和采访学生,求导师；凑合：—  
  > "I feel like a fish out of water trying to figure all of this out." — [r/Journalism 2023-11-01](https://www.reddit.com/r/Journalism/comments/17lmk87/i_need_guidance_and_support_a_mentor_or_friend_in/)
- [?|practitioner|强度2] 外语音视频内容无人可译,想要自动翻译成英文的软件；凑合：—  
  > "does any software or something exist that I can plug the video into and get it translated?" — [r/Journalism 2023-11-13](https://www.reddit.com/r/Journalism/comments/17ui76a/does_software_exist_to_translate_dialogue_from_a/)
- [FREE|student|强度2] 采访时沉浸对话就停止记笔记,过度依赖录音,录音失败时吃亏；凑合：录音+笔记  
  > "Whenever I talk to a source, I get really into the conversation and I stop taking notes" — [r/Journalism 2023-12-26](https://www.reddit.com/r/Journalism/comments/18r1z5z/would_love_some_tips/)
- [?|practitioner|强度2] 需要免费、支持乌克兰语/俄语的转写软件；凑合：自行翻译转写稿  
  > "Dose anyone have a good transcribing software that works with Ukrainian and/or Russian that is free" — [r/Journalism 2024-02-05](https://www.reddit.com/r/Journalism/comments/1ajsrsu/transcribing_software/)
- [FREE|freelancer|强度2] 网站为防AI要求所有专家采访改为电话,不增加时间和稿酬,转写和约时间都更费事；凑合：—  
  > "They now want all expert interviews conducted by phone - no obtaining quotes by email" — [r/freelanceWriters 2024-03-08](https://www.reddit.com/r/freelanceWriters/comments/1b9cgs3/website_now_requiring_all_expert_interviews_be/)
- [FREE|student|强度2] 采访录音很多,难以取舍并压缩到编辑要求的1000字以内；凑合：—  
  > "The problem I'm having, however, is trying to prioritize what to put in the article and what to leave out" — [r/Journalism 2024-03-26](https://www.reddit.com/r/Journalism/comments/1bny2qn/having_trouble_with_article_word_count_after/)

### S5 核实

- [TV/LOCAL|practitioner|强度3] 通过公共记录合法拿到凶杀嫌疑人狱中袭警视频,公设辩护人想阻止播出,不知是否应播；凑合：—  
  > "Now my news manager is saying their office is working to block us from airing the video." — [r/Journalism 2024-04-16](https://www.reddit.com/r/Journalism/comments/1c5ttep/query_regarding_legally_obtained_video_that/)
- [FREE|freelancer|强度3] 弄丢未备份的录音机,只剩笔记,不知大刊是否接受并如何事实核查；凑合：联系信源重新确认  
  > "I recently lost my audio recorder, which had a few files in it that I hadn't backed up yet." — [r/Journalism 2024-05-25](https://www.reddit.com/r/Journalism/comments/1d01q3l/how_to_proceed_with_fact_checking_after_lost/)
- [LOCAL|practitioner|强度3] 编辑改稿时反复引入事实错误甚至标题错误,上报后无人处理；凑合：向其他编辑反映  
  > "I have an editor who sometimes introduces factual mistakes into my stories." — [r/Journalism 2024-12-03](https://www.reddit.com/r/Journalism/comments/1h5up0f/when_your_editor_adds_mistakes_to_your_work/)
- [TV/LOCAL|practitioner|强度3] 数字制作新人工作量大、出错多,担心被辞退付不起房租；凑合：—  
  > "I’ve made so many mistakes such as typos and wrong information" — [r/Journalism 2025-08-03](https://www.reddit.com/r/Journalism/comments/1mgj27h/feeling_helpless_and_not_a_right_fit_for_the_job/)
- [?|practitioner|强度3] ADHD导致稿件中人名、数字、漏词等低级错误,自检难发现,常被编辑发现；凑合：提交前反复重读  
  > "typos in names, numbers, and sometimes even whole words that are missing" — [r/Journalism 2025-08-24](https://www.reddit.com/r/Journalism/comments/1mz0ukr/adhd_and_writing_errors_in_journalism_tips_tricks/)
- [INDIE/FREE|freelancer|强度3] 首次调查报道,因安全被劝阻发表,感到气馁；凑合：仅与好友讨论,用公共记录  
  > "For my safety, i was advised not to publish a story and i feel discouraged" — [r/Journalism 2025-10-06](https://www.reddit.com/r/Journalism/comments/1nzp3st/for_my_safety_i_was_advised_not_to_publish_a/)
- [NATL|practitioner|强度3] AI垃圾与带幻觉统计的“可信”媒体让金融记者80%时间花在找可靠数据上；凑合：—  
  > "At this point, I’m spending 80% of my time on research" — [r/Journalism 2026-04-02](https://www.reddit.com/r/Journalism/comments/1safhc0/is_anyone_else_spending_more_time_finding_data/)
- [LOCAL|practitioner|强度3] 信源协议用电子签署，信源因担心云端而改走邮寄，耽误数日导致独家被对手抢先；凑合：改用邮寄纸质签名  
  > "I shot it over with Xodo Sign so he could just tap it on his screen" — [r/Journalism 2026-08-13](https://www.reddit.com/r/Journalism/comments/1vn7j6g/lost_a_3week_scoop_to_the_physical_mail_system/)
- [LOCAL|practitioner|强度3] 入行前90天犯过地名搞错、算错数、人名拼写等错误，焦虑到发稿时手抖；凑合：—  
  > "Now when I go to file an article, my hands start shaking." — [r/Journalism 2026-08-26](https://www.reddit.com/r/Journalism/comments/1vz8ibq/making_mistakes_in_the_first_90_days/)
- [LOCAL|practitioner|强度3] 都市日报记者怀疑小周报同线记者抄袭自己的深度报道和独家信源内容且不署名；凑合：—  
  > "I report for a daily metro paper" — [r/Journalism 2026-10-23](https://www.reddit.com/r/Journalism/comments/1xd25ri/small_competitor_paper_is_stealing_my_work_is/)
- [?|practitioner|强度2] 想向银行确认某人是否持有账户以核实信源,不确定法律边界；凑合：—  
  > "are they legally able to tell me that?" — [r/Journalism 2023-03-08](https://www.reddit.com/r/Journalism/comments/11lz1pa/can_a_bank_confirm_to_me_that_someone_holds_an/)
- [FREE|freelancer|强度2] 自由撰稿人在调查企业欺诈时担心诽谤诉讼,不知如何确保媒体提供法律保护；凑合：—  
  > "if you're a freelancer, how do you go about making sure whatever outlet you are working with will protect you legally?" — [r/Journalism 2024-06-29](https://www.reddit.com/r/Journalism/comments/1drlgl2/concerns_about_defamation_lawsuits_as_a_freelancer/)
- [NATL|tool_builder|强度2] 财经记者要在多篇稿件间分析公告、财报电话会纪要、写初稿和SEO,耗时且疲劳；凑合：创业者推出Journo AI自动化  
  > "analysing company market releases, extracting key insights, going through earnings call scripts, drafting initial reports" — [r/Journalism 2024-08-26](https://www.reddit.com/r/Journalism/comments/1f1dy05/seeking_feedback_new_ai_tool_for_financial/)
- [?|practitioner|强度2] 每天写四篇时核实细节耗时翻倍,如何兼顾原创报道与聚合；凑合：—  
  > "Fact checking, how in the world do you not make this an enormous time sink?" — [r/Journalism 2024-08-26](https://www.reddit.com/r/Journalism/comments/1f1flrc/fact_checking_and_work_volume_questions/)
- [LOCAL|practitioner|强度2] 邮件采访时受访者用ChatGPT回答,记者感到被冒犯且难以处理；凑合：尽量改用Zoom采访,用ChatGPT检测器识别  
  > "some people answer it with ChatGPT and it’s very obvious" — [r/Journalism 2024-11-21](https://www.reddit.com/r/Journalism/comments/1gwqmsx/people_using_chatgpt_to_answer_human_interest/)
- [?|unknown|强度2] 想免费获取某公众人物所有演讲、访谈、著作的转写文本,类似剪报服务；凑合：—  
  > "What resources are there - like clipping services where I could (ideally free) get transcripts of everything possible of a public figure" — [r/Journalism 2024-11-27](https://www.reddit.com/r/Journalism/comments/1h1ebln/naj_what_resources_are_there_like_clipping/)
- [NATL|practitioner|强度2] 多家媒体把客机和直升机视频当作不明无人机播放,缺乏基本核实；凑合：—  
  > "Not a single video on this CNN article is of a drone." — [r/Journalism 2024-12-17](https://www.reddit.com/r/Journalism/comments/1hg4p24/ufo_and_drones_quit_taking_the_bait/)
- [?|practitioner|强度2] 想搜索政治人物推特历史中是否提过某话题,需要社媒研究工具；凑合：—  
  > "see if they have ever mentioned "XYZ" topic and it would just pull up the relevant tweets" — [r/Journalism 2024-12-19](https://www.reddit.com/r/Journalism/comments/1hi5o5s/are_there_any_good_social_media_research_tools/)
- [LOCAL|editor|强度2] 乡村小报编辑怀疑自由撰稿人投稿存在利益冲突和编造引语,并推销免费公关；凑合：毙稿并与撰稿人沟通  
  > "There is a quote attributed to the former public official saying the freelancer gave them a tour" — [r/Journalism 2024-12-20](https://www.reddit.com/r/Journalism/comments/1hi9oer/did_my_freelancer_just_fabricate_a_lede/)
- [LOCAL|practitioner|强度2] 收到付费发稿平台Issue Wire伪装成AP Wire的奇怪新闻稿,无法核实当事人；凑合：在本地系统搜索当事人未果  
  > "I don't know how they got my email, and I do not want to be associated with pay to play sites like these." — [r/Journalism 2025-03-04](https://www.reddit.com/r/Journalism/comments/1j3jlsr/have_you_guys_heard_about_this_weird_company/)

### S6 写作与制作

- [FREE|freelancer|强度3] 科学记者每周写3-6篇生物医学报道,读论文如陷泥潭,缺乏创造力,不知是倦怠还是能力问题；凑合：—  
  > "I feel like my brain is hitting a wall." — [r/Journalism 2024-03-04](https://www.reddit.com/r/Journalism/comments/1b6o4t3/is_this_burnout_or_am_i_just_getting_dumber_what/)
- [?|practitioner|强度3] 每日简讯、社交帖、摘要等杂务占用时间,导语和结构变差,感觉可被取代；凑合：—  
  > "I feel like I'm losing it (mentally) a bit and I feel more replaceable every day." — [r/Journalism 2024-04-15](https://www.reddit.com/r/Journalism/comments/1c4g5im/possible_my_reportingwriting_is_getting_worse/)
- [?|practitioner|强度3] 转入陌生技术领域,写300字要一小时,被老板批评写得慢；凑合：—  
  > "usually take about an hour to finish a 300-word article" — [r/Journalism 2024-08-22](https://www.reddit.com/r/Journalism/comments/1eyiq0f/am_i_writing_too_slow/)
- [LOCAL|practitioner|强度3] 入职日报后期望含糊、培训不足,屡出错误,担心被裁；凑合：投简历准备后路  
  > "I'm floundering. I'm frustrated. My team is frustrated." — [r/Journalism 2024-11-08](https://www.reddit.com/r/Journalism/comments/1gma5fa/after_3_years_im_wondering_if_im_cut_out_for_this/)
- [TV|tv|强度3] TEGNA强制员工做AI培训并要求保密,担心AI生成图像上电视和数字部门裁员；凑合：—  
  > "Not to mention how many layoffs will happen in the Digital departments." — [r/Broadcasting 2024-11-13](https://www.reddit.com/r/Broadcasting/comments/1gqqex6/tegna_embracing_ai_told_employees_to_keep_quiet/)
- [FREE|student|强度3] 实习写手被编辑多次指控内容含AI,检测工具结果互相矛盾,反复改写；凑合：尝试多种AI检测工具  
  > "have tried numerous detection tools where it’ll come up as 90% AI on one and 0% AI on another" — [r/freelanceWriters 2024-11-20](https://www.reddit.com/r/freelanceWriters/comments/1gvwwh4/flagged_as_heavy_in_ai_but_i_didnt_use_it_at_all/)
- [TV|tv|强度3] TEGNA裁撤导播并试验由一名AI辅助制片人独自完成整档新闻,担心推广到突发新闻；凑合：—  
  > "experimenting with a single "AI-powered" producer "writing, coding" and "switching" ) an entire newscast by themselves" — [r/Broadcasting 2024-11-23](https://www.reddit.com/r/Broadcasting/comments/1gxp3wt/what_happens_when_a_tech_bro_takes_over_your/)
- [INDIE|editor|强度3] 独立新闻机构沟通分散在群聊、邮件和共享文档,想选Slack/Teams/Google Workspace统一协作并有选题日程与任务提醒；凑合：群聊+邮件+共享Google文档  
  > "conversation has basically been through group chat, email, and in the past few years a shared google doc and it's all very disjointed" — [r/Journalism 2024-12-12](https://www.reddit.com/r/Journalism/comments/1hcsisx/question_about_getting_a_workplace_app_for_our/)
- [FREE|practitioner|强度3] 每篇稿件有笔记、草稿、照片、新闻稿等多个文档,Google Drive混乱,同时做三份工作；凑合：每篇稿件建文件夹,试用Scrivener和Notion  
  > "my Google Docs is a DISASTER" — [r/Journalism 2025-01-25](https://www.reddit.com/r/Journalism/comments/1i9us8w/document_organization_tools_programs/)
- [FREE|student|强度3] 校报主编人手少、临时换头版、课业重,出版夜无暇编辑重点稿件,出现细节错误；凑合：—  
  > "i couldn’t edit it while managing a team of designers and reporters during production night" — [r/Journalism 2025-02-26](https://www.reddit.com/r/Journalism/comments/1iyi4wa/how_do_i_produce_better_work_under_pressure/)
- [LOCAL|practitioner|强度3] 编辑近期大量负面修改反馈致恐慌发作、自信受损；凑合：—  
  > "I actually now breakdown crying when I see all the red." — [r/Journalism 2025-06-15](https://www.reddit.com/r/Journalism/comments/1lbsagr/need_advice_on_dealing_with_constant_negative/)
- [LOCAL|practitioner|强度3] 困在糟糕新闻室两年半:编辑不帮忙、因政客朋友电话撤稿、校对失误,士气低、记者流失；凑合：投简历但需留在本地  
  > "I think I can objectively say I have been stuck in a bad newsroom for the past 2.5 years." — [r/Journalism 2025-06-17](https://www.reddit.com/r/Journalism/comments/1ldqwov/longtimers_how_do_you_push_through_the_tough_times/)
- [LOCAL|practitioner|强度3] 报社强制全员用AI且不披露,担心借AI裁员,工会内高层只关心薪酬；凑合：在工会提出AI应纳入集体协议  
  > "everyone in editorial will have to use AI tools" — [r/Journalism 2025-07-05](https://www.reddit.com/r/Journalism/comments/1ls5dr8/ai_use_becoming_compulsory_in_my_newsroom/)
- [FREE|freelancer|强度3] 失业后汽车自由撰稿,条件苛刻(月55稿)、CMS发布耗时；凑合：—  
  > "some of the terms out there are downright predatory" — [r/freelanceWriters 2025-08-01](https://www.reddit.com/r/freelanceWriters/comments/1mey4w6/automotive_freelancing/)
- [LOCAL|practitioner|强度3] SEO/Google更新/AI改写成强制要求,编辑决策被平台与指标支配,开会多写作少；凑合：—  
  > "I’m starting to feel like I spend more time in meetings about how to write than actually writing." — [r/Journalism 2025-08-07](https://www.reddit.com/r/Journalism/comments/1mk5s9r/dealing_with_changing_expectations_re_googleseoai/)
- [LOCAL|practitioner|强度3] 因稿件乱、遗漏多、编辑耗时被考察,过度依赖社媒找选题,想求提升资源；凑合：—  
  > "I'm on probation at work because my writing is messy and omits too much" — [r/Journalism 2025-08-15](https://www.reddit.com/r/Journalism/comments/1mqjbxk/my_stories_require_too_much_editing_and_i_rely/)
- [?|practitioner|强度3] ADHD导致稿件中人名、数字、漏词等低级错误,自检难发现,常被编辑发现；凑合：提交前反复重读  
  > "typos in names, numbers, and sometimes even whole words that are missing" — [r/Journalism 2025-08-24](https://www.reddit.com/r/Journalism/comments/1mz0ukr/adhd_and_writing_errors_in_journalism_tips_tricks/)
- [LOCAL|tv|强度3] 小镇电台新闻总监因报道议员谎言被禁止做全国新闻或带政治倾向内容；凑合：尽量依据可核实事实写作  
  > "I am no longer able to give national coverage" — [r/Journalism 2025-10-16](https://www.reddit.com/r/Journalism/comments/1o8hjx1/as_of_yesterday_i_can_no_longer_give_national/)
- [FREE|freelancer|强度3] 17年写手因破折号等被客户指控用AI,被迫改写作风格,自我怀疑；凑合：改成偷懒文风、故意加错  
  > "I've had multiple clients accuse me of AI just because of em dashes" — [r/freelanceWriters 2025-11-04](https://www.reddit.com/r/freelanceWriters/comments/1oofc4c/im_so_mad_that_i_have_to_change_my_writing_style/)
- [FREE|student|强度3] 校报手写稿被AI检测器误判,编辑和导师因此施压；凑合：—  
  > "some stories that I publish come back as AI through detectors" — [r/Journalism 2025-11-08](https://www.reddit.com/r/Journalism/comments/1orediw/ai_flagging_my_hand_written_work/)

### S7 发布与分发

- [FREE|freelancer|强度3] 稿件已提交三周未发布,编辑多次邮件不回,选题时效过期；凑合：多次邮件追问  
  > "I submitted the article 3 weeks ago and it still hasn't run." — [r/freelanceWriters 2024-03-01](https://www.reddit.com/r/freelanceWriters/comments/1b3xs6z/my_editor_ghosted_me/)
- [FREE|freelancer|强度3] 曾供稿的网站因无流量删除其两年的文章,求职作品集丢失；凑合：考虑把文章转投他处  
  > "articles that don’t drive traffic just take up space on my server" — [r/Journalism 2024-11-18](https://www.reddit.com/r/Journalism/comments/1gu4i0a/publication_i_wrote_for_deleted_my_articles/)
- [FREE|freelancer|强度3] 冷投稿即使多次跟进也无回应,所有活儿都来自熟人推荐；凑合：依靠推荐和已有关系的编辑  
  > "all my cold pitches have yielded nothing so far" — [r/freelanceWriters 2024-11-29](https://www.reddit.com/r/freelanceWriters/comments/1h2in3q/cold_pitching/)
- [INDIE/LOCAL|freelancer|强度3] 用Substack做本地新闻,站点预览不加载、不能缩短邮件长度、改不了发件地址、无法做表格；凑合：考虑离开Substack  
  > "Can't shorten post length included in email without paywalling it." — [r/Substack 2024-12-04](https://www.reddit.com/r/Substack/comments/1h65owd/losing_faith_quickly_what_am_i_missing/)
- [FREE|freelancer|强度3] 每周通过Study Hall向五位编辑投稿两个月无一被采纳,.xyz邮箱无回音；凑合：用Study Hall找编辑并投稿  
  > "I have been doing this for about two months, but I have had nothing accepted so far" — [r/freelanceWriters 2024-12-29](https://www.reddit.com/r/freelanceWriters/comments/1hp6s02/would_like_some_advice/)
- [LOCAL|practitioner|强度3] 三人社媒团队管18个账号,另两人休假后将独自承担,工作量过大；凑合：—  
  > "we manage 18 different accounts across the major platforms" — [r/Journalism 2025-02-06](https://www.reddit.com/r/Journalism/comments/1ijg97h/how_much_does_your_companynewsroom_value_social/)
- [FREE|freelancer|强度3] 跟踪乌克兰少女三年的特稿到处投稿被拒(预算、时效),重建作品集困难；凑合：向本地新闻编辑和多家媒体继续投稿  
  > "I’m having a hell of a time trying to some stories placed right now." — [r/Journalism 2025-03-05](https://www.reddit.com/r/Journalism/comments/1j4fwj3/does_anybody_know_anybody_taking_feature_stories/)
- [FREE|freelancer|强度3] 5000字长篇已被大媒体接受,但编辑长期失联、不断要求修改,稿件时效受特朗普政策变化影响需重写；凑合：反复跟进并重写  
  > "He finally got back to me mid-feburary say" — [r/Journalism 2025-03-10](https://www.reddit.com/r/Journalism/comments/1j7oeqy/editor_kind_of_ghosted_me_advice_needed_freelance/)
- [INDIE/LOCAL|editor|强度3] 被连锁报业解雇后创办农村县域本地报,需选可持续的网站平台与数字订阅方案,居民上网困难；凑合：依靠邮寄印刷和学生印刷业务,学习WordPress  
  > "Any advice on the best platform to build a future-proof news si" — [r/Journalism 2025-03-11](https://www.reddit.com/r/Journalism/comments/1j8jnue/looking_for_advice_on_launching_a_local_news/)
- [INDIE/LOCAL|freelancer|强度3] 单亲妈妈办县里唯一本地新闻号,靠Facebook发布,28天仅赚$7,难变现；凑合：通过Facebook货币化  
  > "I’ve made $7 in 28 days—so progress, but it’s not yet sustainable." — [r/Journalism 2025-09-02](https://www.reddit.com/r/Journalism/comments/1n6eey7/smalltown_single_mom_running_the_only_local_news/)
- [FREE|freelancer|强度3] 自由撰稿人投稿后被报社体育编辑抄袭其已发表文段；凑合：向编辑、Google和ISP举报  
  > "the sports writer COPIED several paragraphs from some of my published work" — [r/Journalism 2025-11-22](https://www.reddit.com/r/Journalism/comments/1p3ijq8/copyright_infringement_and_plagarism/)
- [FREE|aspiring|强度3] 无编制/硕士背景的科学新闻自由撰稿人冷投约15次仅得一次拒信,实习也未成；凑合：总结前两个月出错点  
  > "Has anyone successfully started a freelancer career on their own without a previous staff job or masters degree in it?" — [r/Journalism 2026-01-10](https://www.reddit.com/r/Journalism/comments/1q9h1f8/freelancer_success/)
- [FREE|freelancer|强度3] 稿件被接受后编辑数月不断推迟发表,不知是否该索要kill fee离开；凑合：多次发邮件催问  
  > "I am wondering if i should just ask him for a kill fee and move on." — [r/freelanceWriters 2026-02-02](https://www.reddit.com/r/freelanceWriters/comments/1qu5arl/editor_has_been_moving_publishing_date_for_months/)
- [FREE|student|强度3] 大学生向艺术媒体投了约三十篇稿几乎无回复，怀疑自己不行；凑合：通过PR人员和艺术家获得编辑邮箱  
  > "have since submitted thirty or so pitches to smaller and larger arts publications with little to no responses." — [r/Journalism 2026-05-29](https://www.reddit.com/r/Journalism/comments/1tqxal8/do_editors_just_see_my_email_and_ignore_me/)
- [FREE|freelancer|强度3] 长期自由撰稿，缺乏结构、过度投入、先写后投难以适应媒体需求，自信心耗尽；凑合：先做报道再推销  
  > "Freelancing has killed my self-esteem" — [r/Journalism 2026-10-21](https://www.reddit.com/r/Journalism/comments/1xbsd5u/freelancing_has_killed_my_selfesteem/)
- [LOCAL|practitioner|强度3] 都市日报记者怀疑小周报同线记者抄袭自己的深度报道和独家信源内容且不署名；凑合：—  
  > "I report for a daily metro paper" — [r/Journalism 2026-10-23](https://www.reddit.com/r/Journalism/comments/1xd25ri/small_competitor_paper_is_stealing_my_work_is/)
- [INDIE|practitioner|强度3] 新非营利媒体独自报道谋杀案庭审，被大报几乎逐字改写抄袭，不知要求何种补救；凑合：并排比对后向对方编辑投诉，稿件已撤下  
  > "a journalist much larger, more established paper just changed a few words here and there." — [r/Journalism 2026-11-01](https://www.reddit.com/r/Journalism/comments/1xkpcxb/another_paper_plagiarized_my_work/)
- [LOCAL/INDIE|indie|强度2] 小镇报纸网站维护不了已荒废,想用Substack做印刷+数字混合并收订阅；凑合：—  
  > "They had trouble maintaining a WordPress site, so it's gone dormant." — [r/Substack 2023-04-19](https://www.reddit.com/r/Substack/comments/12s4mee/small_newspaper_moving_to_substack/)
- [INDIE|indie|强度2] 推特压制Substack链接、嵌入失效、限流,冲击新作者建立受众；凑合：—  
  > "with the suppressing of substack links on the site, tweet embeds not working, and now this tweet rate limiting stuff" — [r/Substack 2023-07-02](https://www.reddit.com/r/Substack/comments/14oubrf/twitter_and_substack/)
- [INDIE|indie|强度2] 多作者Substack(苏丹战争)不会给阿拉伯语栏目单独设邮件列表；凑合：—  
  > "aren't sure how to do separate email lists for those who are just interested in Arabic posts" — [r/Substack 2023-08-01](https://www.reddit.com/r/Substack/comments/15frbkm/looking_for_advice_from_experienced_multiauthor/)

### S8 受众与变现

- [TV/LOCAL|tv|强度3] 选举季本地电视台分配台人员要应对愤怒观众,被辱骂,疲惫抑郁；凑合：—  
  > "I end up getting cussed out and berated when all I want to do is inform the community." — [r/Journalism 2024-10-30](https://www.reddit.com/r/Journalism/comments/1gfcqq5/election_exhaustion/)
- [LOCAL|practitioner|强度3] 数字媒体十年老兵因谷歌算法变动导致大规模裁员而失去希望；凑合：—  
  > "I’m starting to lose hope. It’s bleak out there" — [r/Journalism 2024-12-18](https://www.reddit.com/r/Journalism/comments/1hgs9to/layoffs/)
- [INDIE/FREE|freelancer|强度3] 独裁国家的匿名记者想脱离原平台自办Substack,需要100%匿名的加密货币收款以免被捕；凑合：此前在其他网站以比特币收款  
  > "He can’t transfer the money to his own bank account, that would be very dangerous" — [r/Substack 2025-02-05](https://www.reddit.com/r/Substack/comments/1iij3i4/is_there_a_way_to_get_payments_anonymously/)
- [LOCAL|practitioner|强度3] 三人社媒团队管18个账号,另两人休假后将独自承担,工作量过大；凑合：—  
  > "we manage 18 different accounts across the major platforms" — [r/Journalism 2025-02-06](https://www.reddit.com/r/Journalism/comments/1ijg97h/how_much_does_your_companynewsroom_value_social/)
- [INDIE/LOCAL|editor|强度3] 被连锁报业解雇后创办农村县域本地报,需选可持续的网站平台与数字订阅方案,居民上网困难；凑合：依靠邮寄印刷和学生印刷业务,学习WordPress  
  > "Any advice on the best platform to build a future-proof news si" — [r/Journalism 2025-03-11](https://www.reddit.com/r/Journalism/comments/1j8jnue/looking_for_advice_on_launching_a_local_news/)
- [LOCAL|practitioner|强度3] 报社人员从8人减到4人,公司不招人、无支持,硬付费墙使爆款稿转化仅2%；凑合：—  
  > "Started with 8 staff. Ten months later down to 4." — [r/Journalism 2025-08-26](https://www.reddit.com/r/Journalism/comments/1n0noxe/lost_half_the_newsroom_and_the_company_hasnt_made/)
- [INDIE/LOCAL|freelancer|强度3] 单亲妈妈办县里唯一本地新闻号,靠Facebook发布,28天仅赚$7,难变现；凑合：通过Facebook货币化  
  > "I’ve made $7 in 28 days—so progress, but it’s not yet sustainable." — [r/Journalism 2025-09-02](https://www.reddit.com/r/Journalism/comments/1n6eey7/smalltown_single_mom_running_the_only_local_news/)
- [LOCAL|practitioner|强度3] 搜索流量大幅下降、AI摘要吞掉点击,记者被告知处于裁员风险并被归咎；凑合：—  
  > "search traffic dropped significantly for my beat for several months" — [r/Journalism 2026-02-22](https://www.reddit.com/r/Journalism/comments/1rbuanl/probably_be_laid_off_soon/)
- [INDIE|editor|强度3] Google搜索流量消失，杂志数字内容预算归零，网络广告和联盟收入没了，读者以老年人为主；凑合：—  
  > "All the ways people would come across our website through google searches: gone." — [r/Journalism 2026-08-23](https://www.reddit.com/r/Journalism/comments/1vwf2b7/nepo_baby_from_a_small_publishing_family_here_you/)
- [INDIE|indie|强度2] 资深记者在Substack发了两年多仍没有付费订阅者；凑合：—  
  > "I cannot seem to get any paid subscribers" — [r/Substack 2023-09-21](https://www.reddit.com/r/Substack/comments/16o3qc0/exactly_how_do_you_get_paid_subscribers/)
- [?|practitioner|强度2] 出版方禁止在职记者运营个人newsletter,想知道是否可协商；凑合：—  
  > "why shouldn't I be able to write/publish directly to my own audience when I'm on my own time?" — [r/Journalism 2023-11-29](https://www.reddit.com/r/Journalism/comments/186xlz9/should_staff_writers_be_allowed_to_maintain/)
- [INDIE|indie|强度2] 南非作者无法用Stripe开通Substack付费订阅,最低月费对当地过高；凑合：—  
  > "Stripe doesn't operate in South Africa." — [r/Substack 2024-01-11](https://www.reddit.com/r/Substack/comments/193ylw9/paid_subscriptions_skewed_towards_developed/)
- [INDIE/FREE|practitioner|强度2] 前25年老牌报纸美食编辑单飞做Substack,但向全国媒体推水牛城詹姆斯比尔德奖入围餐厅选题无人回应；凑合：直接找对应编辑邮件投稿  
  > "Buffalo restaurants have two finalists for James Beard Awards - first in city history - and I can’t get a nibble." — [r/freelanceWriters 2024-05-12](https://www.reddit.com/r/freelanceWriters/comments/1cqdet1/introducing_myself_starting_solo_career_after_35/)
- [INDIE|indie|强度2] 科学特稿Substack仅约70位订阅者,Twitter对Substack链接限流,难推广；凑合：Twitter、考虑TikTok  
  > "but I'm struggling with building up my audience" — [r/Journalism 2024-05-29](https://www.reddit.com/r/Journalism/comments/1d3m3my/how_to_promote_a_journalism_substack/)
- [INDIE|freelancer|强度2] Substack新手订阅增长全靠大号推荐,不知如何获客及何时开启付费；凑合：依靠知名作者转发  
  > "How do I get more readers and pledges and when do I switch on paid" — [r/Substack 2024-07-24](https://www.reddit.com/r/Substack/comments/1eb36gw/relatively_new_substack_how_should_i_proceed/)
- [INDIE/LOCAL|freelancer|强度2] 四年的县级正能量本地通讯仅252订阅,增长靠订阅者推荐,想找更高效获客方式；凑合：Instagram链接、Nextdoor发帖  
  > "most of my growth has been through recommendations from existing subscribers" — [r/Substack 2024-10-19](https://www.reddit.com/r/Substack/comments/1g70nzm/local_news_newsletter/)
- [LOCAL|practitioner|强度2] 小新闻室记者需同时运营X、Bluesky、Threads,想要免费的多平台管理工具；凑合：曾用Hootsuite但现价每月99美元  
  > "Does anyone recommend a good free social media management tool for multiple platforms?" — [r/Journalism 2024-12-04](https://www.reddit.com/r/Journalism/comments/1h6mj7d/social_media_management_tools_seeking_advice/)
- [INDIE|freelancer|强度2] X算法会压制Substack外链,犹豫是否放弃Substack专攻X变现；凑合：—  
  > "if you shill substack links on X, the algo takes note and doesn't like it, reduces your traffic" — [r/Substack 2025-01-31](https://www.reddit.com/r/Substack/comments/1ieiyuy/is_substack_worth_it_anymore_2025_comparison_to/)
- [INDIE|tool_builder|强度2] 免费读者增长快但付费转化慢,多数人不知道转化付费订阅需要哪些要素；凑合：自制付费通讯运营清单(定价页、付费墙、分析、邮件自动化)  
  > "My free list keeps growing at a nice clip but my paid subs aren’t growing at nearly the same rate." — [r/Substack 2025-02-28](https://www.reddit.com/r/Substack/comments/1j0jpwa/how_do_you_get_more_free_readers_to_convert_to/)
- [LOCAL|practitioner|强度2] 找不到引用自己旧报道的研究论文和政府网站；凑合：用Google Scholar但效果差  
  > "I'm finding it impossible to track these citations down." — [r/Journalism 2025-03-29](https://www.reddit.com/r/Journalism/comments/1jmd0ox/are_there_any_search_tools_for_finding_research/)

### S9 职业与生存

- [TV|tv|强度3] 电视台主播/记者每周6天工作、时薪18美元、几乎无福利；凑合：—  
  > "we essentially have no benefits other than very expensive medical" — [r/Journalism 2023-01-05](https://www.reddit.com/r/Journalism/comments/103pof8/horrible_hourspay/)
- [?|practitioner|强度3] 被裁员后寻求应对行业动荡和求职/转自由职业建议；凑合：—  
  > "how do you cope with the volatility of the industry?" — [r/Journalism 2023-01-12](https://www.reddit.com/r/Journalism/comments/10a80wn/just_got_laid_off_advice_words_of_wisdom/)
- [FREE|freelancer|强度3] 自己写的稿被AI检测软件判为近50%AI,无法修正；凑合：—  
  > "why are the scans showing that my work is 48-50% AI?" — [r/freelanceWriters 2023-01-24](https://www.reddit.com/r/freelanceWriters/comments/10kevp2/i_hate_ai/)
- [LOCAL|practitioner|强度3] 年轻日报记者所在报社被大幅裁员/买断,编辑与同伴离职,新闻室重组；凑合：—  
  > "A round of buyouts, layoffs and people quitting because of the buyouts/layoffs cut our staff by 25%." — [r/Journalism 2023-02-25](https://www.reddit.com/r/Journalism/comments/11bw85y/handling_layoffs_working_at_a_deteriorating/)
- [FREE|freelancer|强度3] 自己写的文章被客户的AI检测工具误判为41% AI,无从申辩；凑合：—  
  > "one of my articles which was 100% self-written was flagged by client's tool as 41% written by AI" — [r/freelanceWriters 2023-03-08](https://www.reddit.com/r/freelanceWriters/comments/11lo0o3/ai_detector_claiming_my_100_selfwritten_article/)
- [FREE|freelancer|强度3] 硅谷银行倒闭导致初创客户暂停合同、无法付款,不知是否协商部分付款；凑合：—  
  > "if my clients claim inability to pay due to loss of the funds in their bank accounts, should I negotiate for partial payment?" — [r/freelanceWriters 2023-03-11](https://www.reddit.com/r/freelanceWriters/comments/11oojae/anyone_else_affected_by_the_silicon_valley_bank/)
- [FREE|freelancer|强度3] 内容农场改用AI初稿,改稿稿酬降至每词1美分,主要收入丧失；凑合：—  
  > "one cent a word, and even less than that for some articles" — [r/freelanceWriters 2023-03-17](https://www.reddit.com/r/freelanceWriters/comments/11trkvz/ive_essentially_lost_my_main_source_of_income_to/)
- [FREE|freelancer|强度3] 新手自由写手客户流失后数月无稿约,投稿石沉大海,考虑放弃；凑合：LinkedIn找客户,向编辑投稿  
  > "I’m pitching to editors and not hearing back." — [r/freelanceWriters 2023-03-26](https://www.reddit.com/r/freelanceWriters/comments/123451n/i_want_to_give_up/)
- [FREE|freelancer|强度3] AI检测工具误判无错别字的原创稿,被迫故意加错别字；凑合：故意加入错别字绕过检测  
  > "I had to do the double work and add typos to make it sound like human generated." — [r/freelanceWriters 2023-03-29](https://www.reddit.com/r/freelanceWriters/comments/125thz2/has_anybody_came_across_unreliability_of_ai/)
- [LOCAL|editor|强度3] 小报总编被远程办公的出版人半夜辱骂甩锅,同时包揽排版和采写,工作过载；凑合：—  
  > "My geriatric boss just called me in the middle of the night" — [r/Journalism 2023-04-04](https://www.reddit.com/r/Journalism/comments/12bawms/publisher_is_driving_me_crazy/)
- [FREE|freelancer|强度3] 最大客户因利润考虑改用ChatGPT,主要收入来源消失；凑合：—  
  > "I literally lost my biggest and best client to ChatGPT today." — [r/freelanceWriters 2023-04-08](https://www.reddit.com/r/freelanceWriters/comments/12ff5mw/it_happened_to_me_today/)
- [FREE|freelancer|强度3] 美国客户拖欠英国自由撰稿人发票,不知能否收滞纳金；凑合：追问发票处理日期  
  > "That invoice is now 32 days overdue." — [r/freelanceWriters 2023-05-01](https://www.reddit.com/r/freelanceWriters/comments/134hv27/can_i_charge_a_usbased_company_late_payment_fees/)
- [?|practitioner|强度3] 15年记者被裁后难求全职,简历工具要求量化成果但记者拿不到指标,ATS筛选；凑合：用Teal简历工具  
  > "it keeps suggesting that I attach achievements with numbers to my experience" — [r/Journalism 2023-05-04](https://www.reddit.com/r/Journalism/comments/137p0d1/resume_question/)
- [FREE|freelancer|强度3] 客户称稿件AI率超过60%,写手想证明是原创；凑合：—  
  > "Is there anything I can do to prove otherwise?" — [r/freelanceWriters 2023-05-26](https://www.reddit.com/r/freelanceWriters/comments/13s798e/how_do_you_deal_with_clients_who_claim_that_my/)
- [FREE|freelancer|强度3] 自由编辑/记者陷入长达半年的倦怠,收入受影响,觉得必须时刻在线；凑合：看心理咨询师  
  > "stuck in a burnout spiral that I have no clue how to escape" — [r/Journalism 2023-05-26](https://www.reddit.com/r/Journalism/comments/13snwly/imburned_out_and_i_have_no_idea_what_to_do/)
- [FREE|freelancer|强度3] 客户曾书面要求用ChatGPT,事后用OriginalityAI检测并拒付三个月稿费；凑合：自己用ZeroGPT等检测  
  > "the client refuses to pay me because they've decided to use OriginalityAI" — [r/freelanceWriters 2023-06-03](https://www.reddit.com/r/freelanceWriters/comments/13zd90b/client_refusing_to_pay_because_of_ai_detector/)
- [FREE|freelancer|强度3] 神经多样性自由文案因AI失去六位数收入,出现严重焦虑；凑合：—  
  > "I cry at least 5 times a day, every day." — [r/freelanceWriters 2023-06-05](https://www.reddit.com/r/freelanceWriters/comments/141qvna/the_ai_mania_is_destroying_my_mental_health_and_i/)
- [FREE|freelancer|强度3] 原创稿被SEO客户用AI检测软件标为90% AI,被迫修改；凑合：—  
  > "Does anyone have practical tips or advice on how to deal with this" — [r/freelanceWriters 2023-06-20](https://www.reddit.com/r/freelanceWriters/comments/14dzwwq/ai_detector_flagging_my_original_writing_as_ai/)
- [FREE|freelancer|强度3] 代理公司关闭后拖欠近700美元稿费,联系无回应；凑合：追问一次  
  > "This was an almost $700 invoice and I was relying on that money to pay my bills." — [r/freelanceWriters 2023-06-30](https://www.reddit.com/r/freelanceWriters/comments/14n3v1a/am_i_just_screwed_out_of_payment/)
- [FREE|freelancer|强度3] 原创页面被Originality AI判为100% AI,客户不信,被迫终止合同；凑合：试其他检测器、重写、取消合同  
  > "which claims my content is 100% AI generated" — [r/freelanceWriters 2023-07-13](https://www.reddit.com/r/freelanceWriters/comments/14ylnky/originality_ai_recent_experiences/)
