# MCP 集成说明（麦麦副驾 McCopilot）

## 接入的 MCP Server

| 项 | 内容 |
|---|---|
| Server 名称 | 麦当劳官方 MCP（mcd-mcp） |
| 接入端点 | `https://mcp.mcd.cn` |
| 传输协议 | Streamable HTTP |
| 鉴权方式 | Bearer Token（于 open.mcd.cn/mcp 手机号登录后激活领取，**不入库、仅存客户端私有配置**） |
| 工具总数 | 33 个（本项目按需选用 8 个） |

> 端点与鉴权方式以官方控制台 `open.mcd.cn/mcp` 实际开放为准；Token 通过环境变量 `MCD_MCP_TOKEN` 注入，仓库内任何文件不含真实凭证。

## 实际使用的 Tool 与业务映射

| 能力 | 调用的 Tool（类别） | 在作品中的用途 |
|---|---|---|
| 续航圈店 | `query_nearby_stores`（门店查询） | 输入经纬度/城市，返回附近门店与距离，做可达性过滤 |
| 菜单读取 | `get_menu` / `query_product`（菜单） | 拉取门店实时菜单、单品与套餐，供配餐与报价 |
| 营养约束 | `get_nutrition`（营养表） | 读取单品热量/蛋白质，支撑「充电越久吃得越丰盛」的热量预算 |
| 智能报价 | `create_order_quote`（报价下单） | 按所选餐品生成报价，计算合计与到店自取方案 |
| 优惠叠加 | `query_coupons`（优惠券） | 自动匹配并叠加最优券，降低合计 |
| 积分权益 | `get_points`（积分） | 展示可用积分，增强复购钩子 |
| 历史复点 | `get_order_list`（订单列表） | 读取历史订单，统计高频组合，支持「老样子」一键复点 |
| 地址/自取点 | `get_address`（地址） | 选定自取门店与导航目的地 |

> 以上 Tool 名为按官方能力类别标注的通用名称；最终以 `https://mcp.mcd.cn` 实际暴露的 tool name 为准，SKILL.md 在真实联调时会按实际 schema 对齐参数。

## 调用流程

```
用户意图（自然语言）
   │
   ▼
[Skill 路由] 麦麦副驾 McCopilot
   │  1) 续航圈店：query_nearby_stores → range_filter（可达/紧张/回不来 三重过滤）
   │  2) 充电即点餐：输入剩余电量/充电时长 → charge_eta（ETA 对齐算法）
   │  3) 配餐+优惠：get_menu + get_nutrition → order_compose → query_coupons
   │  4) 报价下单：create_order_quote（到店自取，支付由用户在麦当劳 App 完成）
   │  5) 老司机套餐：get_order_list → combo_memory（高频组合 + 「老样子」复点）
   ▼
麦当劳官方 MCP（mcp.mcd.cn）
   │
   ▼
实时门店 / 菜单 / 报价 / 优惠券 / 订单数据
```

## 业务价值

- **场景差异化**：529 份参赛作品清一色「手机思维」，本作品切入**车机第三空间**——电动车补能（充电 30 分钟）的等待场景，是别人抄不走的人设（作者为车机座舱工程师）。
- **时间对齐**：把「充电进度」与「出餐进度」用 ETA 算法对齐，实现「插枪即下单、充到 80% 麦麦到手」的确定性体验，而非简单点餐。
- **零触摸交互**：车机 demo 全程用方向盘方控（方向键 + Enter + Backspace）走焦操作，贴合驾驶场景的安全交互范式。
- **诚实边界**：支付环节交还用户本人（麦当劳 App），不触碰资金流，符合合规与安全声明。

## 脱敏配置示例

见 `mcp-config.example.json`（仅含端点与 `MCD_MCP_TOKEN` 占位符，不含真实凭证）。
