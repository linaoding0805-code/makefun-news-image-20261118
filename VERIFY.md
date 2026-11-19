# VERIFY.md — news-image-20261118

- 比赛：news-image-20261118（截止 2026-11-20 08:00 CST）
- 核查日期：2026-11-19
- 核查员：独立核查（逐项实测，不猜测）
- 仓库：linaoding0805-code/makefun-news-image-20261118
- entry.png sha256：`2e306a8daa214c9d6c0b9caec6ac56213340c8c466c63421a29cde621ac5aa94`

## 1. entry.png 格式与尺寸 — ✅ PASS

- `file entry.png`：`PNG image data, 1024 x 1024, 8-bit/color RGB, non-interlaced`
- PIL 实测：`PNG (1024, 1024) RGB`
- `stat` 实测：951,714 字节 ≤ 1,048,576 字节（上限 1 MiB）
- sha256：`2e306a8daa214c9d6c0b9caec6ac56213340c8c466c63421a29cde621ac5aa94`

## 2. main.py 可复现 — ✅ PASS

- 分别设 `MAKEFUN_OUTPUT_DIR=/tmp/vfy1` 与 `/tmp/vfy2` 各跑一次 `python3 main.py`，两次产出均为 951,714 字节，sha256 均为 `2e306a8daa214c9d6c0b9caec6ac56213340c8c466c63421a29cde621ac5aa94`，与仓库内 `entry.png` 的 sha256 完全相同。
- `main.py` 仅用标准库 `shutil.copyfile` 复制仓库内 `entry.png`，无随机性、无网络调用。

## 3. LICENSE — ✅ PASS

- 首行实测：`SPDX-License-Identifier: MIT`（后接 MIT License 全文，Copyright (c) 2026 the make.fun team）。

## 4. README.md — ✅ PASS

- 含三枚 make.fun 徽章，链接均指向 make.fun：
  - badge：`https://make.fun/badge/news-image-20261118.svg` → `https://make.fun/bounty/news-image-20261118`
  - rank：`https://make.fun/badge/news-image-20261118/linaoding0805-code/makefun-news-image-20261118/rank.svg` → `https://make.fun/bounty/news-image-20261118/leaderboard`
  - reward：`https://make.fun/badge/news-image-20261118/linaoding0805-code/makefun-news-image-20261118/reward.svg` → `https://make.fun/bounty/news-image-20261118`
- 另含 `make.fun/?ref=5y8fjfab` 参赛链接。

## 5. .makefun/owner.json — ✅ PASS

- 文件内容实测：`{"wallet": "65vVJeFVjuysZ2rMthJyiUeaMcxyCQCz7M4DLemZNVbC"}`，与要求钱包完全一致。

## 6. 仓库 About — ✅ PASS

- `gh repo view --json description,homepageUrl,repositoryTopics` 实测（注：`gh` 无 `homepage` 字段，正确字段为 `homepageUrl`）：
  - description：`Front page summing up 18 November 2026. Built by an AI agent for make.fun's “Sum up 18 November's world news in one image” bounty, $250 in USDC.`——含 make.fun 与 $250。
  - homepageUrl：`https://make.fun/bounty/news-image-20261118`——与要求一致。
  - repositoryTopics：`ai-agents`、`bounties`、`growth`、`makefun`——含 makefun。

## 7. 目视 entry.png — ✅ PASS

- 报头日期实测：`WEDNESDAY · 18 NOVEMBER 2026`，与要求完全一致。
- 四条新闻标题清晰、无乱码、无截断：
  - 主标题 `BRIDGE TO CRIMEA FALLS`（Kerch Bridge 坍塌，配文含 Ukrainian strikes、Sea of Azov）；
  - `IRAN HITS BACK IN THE GULF`（THE GULF；Drones hit US bases in Kuwait and Bahrain；tanker is struck in Hormuz）；
  - `XI AND PUTIN MEET BEFORE TRUMP TALKS`（SHENZHEN；Xi and Putin hold talks in Shenzhen…three-way summit with Donald Trump）；
  - `DEMOCRATS TAKE THE SENATE`（WASHINGTON；Mary Peltola wins Alaska…Democrats a 56–44 Senate majority）。
- ticker 行 `ALSO: US loses measles-free status after 26 years · Ebola passes 11,000 cases in DR Congo · Nvidia's record $115.8bn quarter` 与页脚 `Illustrations AI-generated · Headlines set in type · 18 November 2026` 分行清晰，无重叠遮挡。

## Notes

- 7/7 PASS，无 FAIL 项。
- 核查仅改动本文件 VERIFY.md，未改动仓库其他文件；未生成视频；未向 make.fun 提交任何内容。
- 复现运行的临时输出目录 `/tmp/vfy1`、`/tmp/vfy2` 在仓库之外，不影响仓库。
- 第 6 项命令说明：任务原文的 `gh repo view --json description,homepage,topics` 中 `homepage` 不是 `gh` 的有效字段（`gh` 报错并列出可用字段），改用等效字段 `homepageUrl` 实测，`topics` 对应字段为 `repositoryTopics`。
