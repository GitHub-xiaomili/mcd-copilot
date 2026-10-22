#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
麦麦副驾 · 老司机套餐
读取历史订单（order-list），统计高频组合，提供「老样子」一键复点。
"""
from collections import Counter
from typing import Dict, List, Optional

# 示例：单条历史订单是一个餐品列表
MOCK_HISTORY = [
    ["巨无霸套餐", "美式咖啡"],
    ["麦辣鸡腿堡套餐", "可口可乐"],
    ["巨无霸套餐", "美式咖啡"],
    ["巨无霸套餐", "美式咖啡"],
    ["麦香鱼套餐", "红茶"],
]


def learn(history: List[List[str]], top_n: int = 3) -> List[Dict]:
    """返回高频组合，按出现次数降序。"""
    counter = Counter(tuple(order) for order in history)
    return [
        {"combo": list(items), "times": times}
        for items, times in counter.most_common(top_n)
    ]


def one_liner(history: List[List[str]]) -> Optional[List[str]]:
    """「老样子」返回最高频组合；无历史返回 None。"""
    result = learn(history, top_n=1)
    return result[0]["combo"] if result else None


if __name__ == "__main__":
    print("老司机套餐 Top3：")
    for r in learn(MOCK_HISTORY):
        print(f"  ×{r['times']}  {r['combo']}")
    print("「老样子」→", one_liner(MOCK_HISTORY))
