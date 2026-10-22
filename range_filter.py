#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
麦麦副驾 · 续航圈店
给定当前续航里程，对候选门店做三重可达性过滤（单程/往返/余量）。
纯逻辑，零第三方依赖；真实门店数据来自麦当劳 MCP 门店查询接口。
"""
from dataclasses import dataclass
from typing import List, Tuple

# 可达性标签
REACHABLE = "可达"        # 能去能回，余量充足
TIGHT = "紧张"            # 能去能回，余量偏小
UNREACHABLE = "回不来"    # 单程或往返超出可用续航


@dataclass
class Store:
    name: str
    distance_km: float       # 当前位置到门店的单程距离
    one_way_min: float       # 预计单程耗时（分钟）
    has_charger: bool = False  # 门店是否自带/邻近充电桩


def classify(current_range_km: float, store: Store,
             next_leg_km: float = 0.0, safety_ratio: float = 0.8) -> str:
    """对单个门店打可达性标签。"""
    usable = current_range_km * safety_ratio
    round_trip = store.distance_km * 2 + next_leg_km
    if store.distance_km > usable or round_trip > usable:
        return UNREACHABLE
    if round_trip > usable * 0.6:
        return TIGHT
    return REACHABLE


def filter_stores(current_range_km: float, stores: List[Store],
                  next_leg_km: float = 0.0,
                  safety_ratio: float = 0.8) -> List[Tuple[Store, str]]:
    """返回 [(门店, 标签), ...]，按距离升序。"""
    result = [(s, classify(current_range_km, s, next_leg_km, safety_ratio))
              for s in stores]
    result.sort(key=lambda x: x[0].distance_km)
    return result


if __name__ == "__main__":
    mock_stores = [
        Store("麦当劳·科技园店", 6.2, 12, True),
        Store("麦当劳·滨江店", 12.0, 18, True),
        Store("麦当劳·机场店", 110.0, 95, False),
    ]
    print("当前续航 60km，下一段路程 15km：")
    for s, tag in filter_stores(60.0, mock_stores, next_leg_km=15.0):
        flag = "⚡有桩" if s.has_charger else "   "
        print(f"  [{tag}] {s.name:<14} 单程 {s.distance_km:>5}km {flag}")
