#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
麦麦副驾 · 充电 × 取餐 ETA 对齐
决定：现在就下单，还是到店前 N 分钟再点，使麦麦到手 ≈ 充电完成 / 到店。
模型见 references/eta-model.md。
"""
from dataclasses import dataclass
from typing import Dict


def decide_order(charge_remaining_min: float, cook_min: float,
                 queue_min: float, drive_min: float) -> Dict:
    """
    返回下单决策。
    - order_now: True 立即下单；False 建议延后
    - wait_min: 建议延迟的分钟数（0 表示现在点）
    """
    food_ready = cook_min + queue_min
    wait = charge_remaining_min - (food_ready + drive_min)
    if wait <= 0:
        return {
            "order_now": True,
            "wait_min": 0,
            "msg": "立即下单：到店时麦麦刚好做，最新鲜",
        }
    return {
        "order_now": False,
        "wait_min": round(wait),
        "msg": f"到店前 {round(wait)} 分钟再点，避免早做放凉",
    }


if __name__ == "__main__":
    # 充电剩 35 分钟，餐做 12 分钟，排队 3 分钟，开车去 8 分钟
    r = decide_order(35, 12, 3, 8)
    print("充电 35min / 出餐 12min / 排队 3min / 车程 8min")
    print("  →", r["msg"])
