---
layout: single
title: 使用指南
permalink: /help/
---

## 📦 安装步骤

### macOS

将 **慧眼识鸟-SuperBirdID.app** 拖拽到您的 **Applications** (应用程序) 文件夹中。

### Windows

下载 `.zip` 压缩包，解压后，双击运行其中的 `.exe` 可执行文件即可。

### Lightroom 插件安装（可选）

1. 打开 Adobe Lightroom Classic。
2. 选择菜单：**文件 → 增效工具管理器**。
3. 点击 **添加** 按钮。
4. 在弹出的窗口中，选择您解压出来的 `SuperBirdIDPlugin.lrplugin` 文件夹。
5. 点击 **完成**。

---

## 🚀 快速开始

1. **选择照片**: 启动应用后，点击“选择图片”或直接拖拽照片到主窗口。
2. **等待智能分析**: 如果照片包含GPS信息，应用会自动下载周边eBird数据以提高精度。您也可以手动选择国家进行过滤。
3. **查看结果**: AI会自动检测并识别鸟类，给出最可能的几个结果及置信度。
4. **写入元数据**: 确认结果无误后，点击“写入照片”，鸟类名称会自动保存到照片的EXIF信息中，支持RAW格式。

---

## 💡 使用技巧

- **使用带GPS的照片**: 这是提高识别准确度的最有效方法。
- **确保鸟类清晰**: 鸟类主体越清晰、越大，识别效果越好。
- **Lightroom 插件**: 在 Lightroom 中选中照片，通过 `文件 > 增效工具附加功能 > 慧眼识鸟-SuperBirdID` 来启动识别，实现高效批量处理。

---

## 🔧 常见问题 (FAQ)

**Q: 为什么识别结果不准确？**
A: 请优先尝试使用带有GPS信息的照片，或在识别前手动选择正确的拍摄国家/地区。同时，请确保照片中的鸟类主体清晰。

**Q: 支持哪些照片格式？**
A: 全面支持 JPEG, TIFF, 以及主流相机品牌的RAW格式，如 Canon (CR2, CR3), Nikon (NEF), Sony (ARW), Fujifilm (RAF) 等。

**Q: 写入照片会损坏原图吗？**
A: 不会。我们使用行业标准的 ExifTool 来安全地写入元数据，不会对您的照片质量产生任何影响。

**Q: 如何更新 eBird 数据？**
A: 删除 `~/Documents/SuperBirdID_File/ebird_cache/` 目录，下次识别时应用会自动下载最新的数据。

---

## 📮 联系与反馈

如果您遇到任何问题或有功能建议，欢迎通过 [GitHub Issues](https://github.com/jamesphotography/superbirdid/issues) 与我们联系。
