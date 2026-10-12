---
name: feishu-doc-to-poster
description: 输入一个飞书文档链接，自动产出竖版长图招募海报（HTML→PNG）。适用于讲师/社群/志愿者/活动招募：文档里写招募文案、附品牌参考图或设计说明、附二维码图片或报名链接（问卷/表单 URL 会自动生成二维码）。
---

# 飞书文档 → 招募海报（HTML 转图片）

读飞书文档 → 抽文案素材 → 填 HTML 模板 → 无头 Chrome 出图 → 质检交付。

## 流程

1. `lark-cli docs +fetch --doc "<URL>" --doc-format markdown --as user` 读全文。
2. 识别区块：主标题/副标题、我们在寻找、我们能提供、愿景、报名方式、底部口号。长文压成短句，每条≤2行。
3. 二维码：内嵌图用 `docs +media-download` 下载；URL/问卷链接就调二维码生成工具，四周留静区。
4. logo/品牌风格：文档给了就用，没给就用 `assets/` 默认山禾规范。
5. 复制 `assets/poster-template.html` 填文案和图片路径。
6. 渲染：经 `mac_computer_use_tool` 跑 `scripts/render.py`（沙箱 shell 直调 Chrome 会崩）。
7. `scripts/autocrop.py` 裁白边。
8. 质检：无孤字行、logo 完整、二维码清晰有白边、文字不溢出。
9. PNG 上传 URL 用 RichMediaCard 展示，HTML 源文件一起 present_files。
