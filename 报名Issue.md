# 报名 Issue 文案（复制到 GitHub 活动仓库提交）

> 提交位置：https://github.com/M-China/mcd-developer-innovation-challenge/issues
> 注意：标题与正文不要留空行；项目地址用纯文本 URL，不要用 Markdown 链接格式。

---

**Issue 标题（直接填这一行）：**

【参赛申请】麦麦副驾 McCopilot

---

**Issue 正文（从下面【参赛申请】开始整段复制）：**

【参赛申请】
项目名称:麦麦副驾 McCopilot
项目地址:https://github.com/GitHub-xiaomili/mcd-copilot
项目简介:面向电动车补能（充电等待）场景的麦当劳点餐编排 Skill——插枪即下单、充到 80% 麦麦到手；用方向盘方控零触摸走焦点餐，切入车机第三空间这一无人区。

---

**以下为补充说明（官方格式仅强制前三行，以下内容用于呈现差异化，可一并提交）：**

**与其他参赛作品的差异**
全场 529 份作品清一色「手机思维」（省钱凑单 / 卡路里配餐红海）。本作品切入**车机第三空间**——电动车充电 30 分钟的等待场景，是别人抄不走的人设：作者本身是车机座舱工程师，并把日常做的「方控走焦 / 键盘导航」直接做成可交互 demo 的卖点。

**核心能力（五步闭环）**
- 续航圈店：输入剩余续航 → 单程/往返/余量三重过滤，门店打「可达/紧张/回不来」标签
- 充电即点餐：按充电时长做 ETA 对齐，决定「立即点」还是「到店前 N 分钟再点」，实现「充好就能取」
- 配餐+优惠：充电越久可选越丰盛，自动叠加最优优惠券
- 下单：到店自取（支付交还用户本人，不碰资金流）
- 老司机套餐：读历史订单，一句「老样子」一键复点

**实际使用的麦当劳 MCP 能力**
门店查询 · 菜单 · 营养表 · 报价下单 · 优惠券 · 积分 · 订单列表 · 地址（端点 https://mcp.mcd.cn，Bearer 鉴权；Token 仅存客户端私有配置，不入库）。

**交付物**
- SKILL.md + scripts/（range_filter / charge_eta / order_compose / combo_memory，零依赖已跑通）
- references/（MCP 映射 / ETA 模型 / 方控走焦规范）
- demo/index.html：单文件车机中控大屏，五屏流程，键盘方向键+Enter+Backspace 模拟方控走焦，零依赖可交互
- CONTEST_DECLARATION.md / MCP_INTEGRATION.md / workbuddy.md 已按报名硬性要求齐备
