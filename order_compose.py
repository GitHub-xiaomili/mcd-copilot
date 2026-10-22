#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
麦麦副驾 · 配餐 + 优惠券组合
按充电时长给热量预算（充电越久可选越丰盛），挑选套餐，叠加最优优惠券（Mock）。
接入真实环境时，菜单来自 MCP 菜单接口，优惠券来自 query-my-coupons。
"""
from dataclasses import dataclass
from typing import Dict, List, Optional

MENU = [
    {"name": "巨无霸套餐", "kcal": 850, "price": 39.5, "cook": 10},
    {"name": "板烧鸡腿堡套餐", "kcal": 720, "price": 41.0, "cook": 11},
    {"name": "麦辣鸡腿堡套餐", "kcal": 780, "price": 36.0, "cook": 9},
    {"name": "麦香鱼套餐", "kcal": 690, "price": 34.5, "cook": 9},
    {"name": "开心乐园餐", "kcal": 520, "price": 29.5, "cook": 7},
]

BEST_COUPON = 6.0  # Mock：固定最优券；真实环境从 query-my-coupons 取最大可叠加


def kcal_budget(charge_min: float) -> int:
    """充电越久，热量预算越宽松（线性示例）。"""
    return int(400 + charge_min * 15)


def compose(charge_min: float) -> Dict:
    budget = kcal_budget(charge_min)
    candidates = [m for m in MENU if m["kcal"] <= budget]
    pick = max(candidates, key=lambda m: m["kcal"]) if candidates else MENU[0]
    after = round(max(pick["price"] - BEST_COUPON, 0), 2)
    return {
        "budget": budget,
        "pick": pick["name"],
        "kcal": pick["kcal"],
        "price": pick["price"],
        "after_coupon": after,
    }


if __name__ == "__main__":
    r = compose(35)
    print(f"充电 35min → 热量预算 {r['budget']}kcal")
    print(f"  推荐 {r['pick']}（{r['kcal']}kcal），券后 ¥{r['after_coupon']}")
