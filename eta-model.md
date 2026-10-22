# 充电 × 取餐 ETA 对齐模型

目标：让「麦麦到手」的时刻对齐「充电完成（或到店）」的时刻，避免放凉 / 久等。

## 变量

| 符号 | 含义 | 单位 |
|---|---|---|
| `charge_remaining_min` | 插枪后预计剩余充电时长 | 分钟 |
| `cook_min` | 选定套餐预估出餐时长 | 分钟 |
| `queue_min` | 预计排队/备餐等待 | 分钟 |
| `drive_min` | 门店到充电桩车程 | 分钟 |
| `T_food` | 餐品就绪所需 = cook + queue | 分钟 |

## 决策公式

```
T_food     = cook_min + queue_min
wait       = charge_remaining_min - (T_food + drive_min)
order_now  = (wait <= 0)
```

- `wait <= 0`：现在就下单，到店 / 充好时麦麦刚做，最新鲜。
- `wait > 0`：建议「到店前 `wait` 分钟再点」，避免早做放凉。

## 直觉

充电场景里 `charge_remaining_min`（30~40 分钟）远大于 `T_food + drive_min`
（通常 15~25 分钟），所以多数情况 `wait > 0`——这正是麦麦副驾的卖点：
**插枪后不用立刻点，系统会在最佳窗口提醒你点，到店即取。**

## 实现

见 `scripts/charge_eta.py::decide_order`。
