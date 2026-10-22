# 麦当劳 MCP 工具映射（麦麦副驾）

## 接入方式（已配置）

- 协议：Streamable HTTP
- 端点：`https://mcp.mcd.cn`
- 鉴权：请求头 `Authorization: Bearer <Token>`（Token 来自 open.mcd.cn/mcp 控制台）
- 已在 WorkBuddy 私有配置 `~/.workbuddy/mcp.json` 的 `mcd-mcp` 中配置，
  **Token 仅存于客户端私有配置，不写入本仓库**。
- 启用：WorkBuddy 左侧「专家·技能·连接器」→ 连接器 → 自定义连接器，
  对 `mcd-mcp` 点「启用 / Trust」。
- 官方开放约 33 个工具；麦麦副驾仅编排其中 8 个（下表）。
- 速率：每个 Token 每分钟最多 600 次请求。

## 能力映射

> 本文档列出麦麦副驾用到的麦当劳官方 MCP 能力。真实工具名 / 参数以
> `open.mcd.cn/mcp` 控制台实际开放为准，连通性验证后回填。

| 能力分类 | Skill 用途 | 预期调用 | 备注 |
|---|---|---|---|
| 门店查询（附近/城市） | 续航圈店 | 按经纬度或城市列出附近门店（含距离、营业中） | 距离由 MCP 返回或本地估算 |
| 菜单 / 餐品详情 | 配餐、ETA 计算 | 取套餐列表、单品价格、热量、预估出餐时长 | `cook_min` 取「预估出餐时长」 |
| 报价 / 创建订单 | 下单 | 组装购物车 → 报价 → 创建订单 | 到店自取 beType=1 |
| query-my-coupons | 优惠券叠加 | 列出可用券 → 选最优组合 | order_compose 接入 |
| query-my-account | 积分抵扣提示（彩蛋） | 读取可用/累计积分 | 仅提示，不强扣 |
| order-list | 老司机套餐 | 读取历史订单 | combo_memory 接入 |
| 营养表 | 热量预算配餐 | 餐品热量查询 | 与菜单接口可能合并 |
| delivery-addresses | 配送场景备选 | 列收货地址 | 充电场景默认自取，备用 |

## 接入位置（代码指针）

- `scripts/range_filter.py` —— 消费「门店查询」结果
- `scripts/charge_eta.py` —— 消费「餐品出餐时长」
- `scripts/order_compose.py` —— 消费「菜单」「优惠券」
- `scripts/combo_memory.py` —— 消费「order-list」

## 边界约定

- 不接充电桩 / 车辆 API：续航、剩余充电时长由用户输入或可选手填。
- 不代付：下单后支付由用户本人扫码完成。
- Token 绑定个人会员账号，仅读个人数据、写本人订单，权限最小化。
