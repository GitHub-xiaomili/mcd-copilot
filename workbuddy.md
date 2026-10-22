# WorkBuddy 开发记录（专项奖励凭证）

> 本文件记录使用 WorkBuddy 开发「麦麦副驾 McCopilot」的全过程，作为麦当劳程序员
> 创意开发大赛 WorkBuddy 专项奖励的凭证（真实使用 WorkBuddy + 提交 workbuddy.md）。

## 开发环境

- WorkBuddy（Agent 模式，允许文件写入）
- Python 3.12（脚本零第三方依赖）
- 目标：2026-10-25 23:59 前提交报名

## 阶段一 · 选题与竞品分析

- 让 WorkBuddy 拉取大赛公开信息与已发布作品格局：529 份作品，Top3 全是省钱方向，
  卡路里/营养方向已拥挤，碳足迹仅 1 份。
- 结论：红海（省钱/卡路里）不碰，蓝海在「车内第三空间」——全场无人做。
- 结合我自身「车机座舱工程师」身份，确定创意 A：电动车补能场景点餐。

## 阶段二 · 方案提案与审批

- WorkBuddy 产出完整设计方案（Skill 结构 + demo 网站 + 三天计划）写入
  《麦麦副驾-设计方案.txt》供审查。
- 我按「先提案、后执行」流程，确认后下发「执行」指令，WorkBuddy 才开始写代码。

## 阶段三 · Skill 包开发（D1）

- 搭仓库骨架：SKILL.md / scripts / references / demo。
- 四个算法脚本：续航圈店、ETA 对齐、配餐优惠、老司机套餐，均已本地跑通。
- 修复两处：combo_memory 漏导 Optional；range_filter mock 距离与可达标签对齐。

## 阶段四 · 车机风 Demo（D1-D2）

- 单文件 HTML，模拟车机中控大屏，键盘方向键 + Enter + Backspace 完整模拟
  方向盘方控走焦——这是我日常做车机焦点导航的老本行。
- 五屏流程：主屏 → 续航圈店 → 充电×取餐双环对齐 → 方控点餐 → 取餐码。

## 阶段五 · 文档与发布（D2-D3）

- README（身份故事 + 架构图 + 快速开始 + Roadmap）
- 本文件 workbuddy.md
- 公开仓库发布 + 提交报名 Issue

## 复现命令

```bash
cd mcd-copilot/scripts && for f in range_filter charge_eta order_compose combo_memory; do python3 $f.py; done
# 浏览器打开 mcd-copilot/demo/index.html
```

用 WorkBuddy 开发，1024 程序员节。
