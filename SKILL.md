---
name: feishu-doc-to-poster
description: 输入一个飞书文档链接，自动产出竖版长图海报（HTML→PNG）。支持两种类型：课程招募海报（讲师/社群/志愿者）、线下活动海报（含场地照片、嘉宾、时间地点价格）。文档里写文案、附素材图、二维码或报名链接（会自动生成二维码）。
---

# 飞书文档 → 招募/活动海报（HTML 转图片）

读飞书文档 → 识别海报类型 → 抽文案素材 → 填对应 HTML 模板 → 无头 Chrome 出图 → 质检交付。

## 支持的海报类型

### 1. 课程海报（course）
用于讲师/社群/志愿者招募，包含「我们在寻找」「我们能提供」等招募要素。

### 2. 活动海报（event）
用于线下沙龙、活动宣传，包含嘉宾信息、时间地点、价格、场地照片等活动要素。

## 流程

1. **读取文档**：`lark-cli docs +fetch --doc "<URL>" --doc-format markdown --as user` 读全文。
2. **识别类型**：文档第一行或开头注明「课程海报」或「活动海报」。
3. **抽取文案**：
   - **课程海报**：主标题/副标题、我们在寻找、我们能提供、愿景、报名方式、底部口号
   - **活动海报**：系列名/英文标题/中文标题、钩子、嘉宾信息（姓名/社交账号/头衔/分享主题）、时间/地点/价格、截止、场地照片、情绪短句
   - 长文压成短句，每条≤2行
4. **处理素材**：
   - 二维码：内嵌图用 `docs +media-download` 下载；URL/问卷链接调二维码生成工具，四周留静区
   - logo：文档给了就用，没给就用 `assets/logo.png` 默认山禾 logo
   - 场地照片（仅活动海报）：下载后放入 `assets/`，取景要突出氛围（灯、吧台、标志物）
5. **填充模板**：
   - 课程海报：复制 `templates/course-poster-template.html`（待补充）
   - 活动海报：复制 `templates/event-poster-template.html`，替换所有 `{{变量}}` 为实际内容
   - 图片路径使用相对路径（如 `../assets/logo.png`）
6. **渲染**：经 `mac_computer_use_tool` 跑 `scripts/render.py <html> <output.png>`（沙箱 shell 直调 Chrome 会崩）。
   - 活动海报高度通常为 2000-2400px（根据内容动态调整）
7. **裁剪**：`scripts/autocrop.py <input.png> <output.png>` 裁白边。
8. **质检**：
   - 无孤字行
   - logo 完整、未变形（联名 logo 视觉重量对等）
   - 二维码清晰有白边
   - 文字不溢出
   - 场地照片清晰（仅活动海报）、渐隐过渡自然
   - 整体层级清晰、色调统一
9. **交付**：PNG 上传 URL 用 RichMediaCard 展示，HTML 源文件一起 present_files。

## 设计规范

详见 `references/design-guidelines.md`，包含：
- Logo 使用规范（官方原图、联名对齐）
- 配色规范（课程海报 vs 活动海报）
- 字体规范（PingFang SC、宋体标题）
- 版式规则（层级、间距、留白）
- 活动海报专属：场地照片处理（满宽通栏、mask 渐隐、降饱和）

## 示例参考

- 活动海报示例：`examples/event-poster-example.html` + `.png`
- 课程海报示例：待补充
