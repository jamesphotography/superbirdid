# 慧眼识鸟 v3.1.0 安装指南

## 📦 安装包内容

本 DMG 镜像包含：
- **慧眼识鸟.app** - 主程序（GUI + API）
- **SuperBirdIDPlugin.lrplugin** - Adobe Lightroom 插件
- **使用说明.md** - 详细使用说明

---

## 🚀 快速安装（3 分钟）

### 第一步：安装主程序

1. 打开 DMG 镜像
2. 将 **慧眼识鸟.app** 拖到 **Applications** 文件夹
3. 首次启动时：
   - 右键点击 → "打开"（绕过 macOS 安全提示）
   - 选择您的常用拍摄国家/地区

✅ 完成！主程序已安装

---

### 第二步：安装 Lightroom 插件

#### 方法一：自动安装（推荐）⭐

**通过 Lightroom 插件管理器安装：**

1. **打开 Lightroom Classic**

2. **进入插件管理器**：
   - 菜单栏 → **文件** → **增效工具管理器**
   - 或快捷键：`Command + Shift + ,`

3. **添加插件**：
   - 点击左下角 **"添加"** 按钮
   - 浏览到 DMG 镜像中的 **SuperBirdIDPlugin.lrplugin**
   - 点击 **"添加增效工具"**

4. **验证安装**：
   - 插件列表应显示 "SuperBirdID Plugin"
   - 状态：✅ **已启用**

✅ 完成！插件已安装

---

#### 方法二：手动复制安装

如果自动安装失败，可以手动复制到插件目录：

**步骤：**

1. **复制插件文件夹**：
   ```bash
   # 从 DMG 复制到桌面（方便操作）
   cp -R "/Volumes/SuperBirdID/SuperBirdIDPlugin.lrplugin" ~/Desktop/
   ```

2. **移动到 Lightroom 插件目录**（选择适合您版本的目录）：

   **Lightroom Classic CC (2015 - 2024)**：
   ```bash
   # 创建目录（如果不存在）
   mkdir -p ~/Library/Application\ Support/Adobe/Lightroom/Modules

   # 移动插件
   mv ~/Desktop/SuperBirdIDPlugin.lrplugin \
      ~/Library/Application\ Support/Adobe/Lightroom/Modules/
   ```

   **Lightroom CC (旧版)**：
   ```bash
   mkdir -p ~/Library/Application\ Support/Adobe/Lightroom\ CC/Modules

   mv ~/Desktop/SuperBirdIDPlugin.lrplugin \
      ~/Library/Application\ Support/Adobe/Lightroom\ CC/Modules/
   ```

3. **重启 Lightroom**

4. **验证安装**：
   - 文件 → 增效工具管理器
   - 应该看到 "SuperBirdID Plugin"

---

## 📂 Lightroom 插件常见安装路径

### macOS

| Lightroom 版本 | 插件目录 |
|---------------|---------|
| **Classic CC 2015+** | `~/Library/Application Support/Adobe/Lightroom/Modules/` |
| **CC (Cloud)** | `~/Library/Application Support/Adobe/Lightroom CC/Modules/` |
| **用户自定义** | 在插件管理器中可查看其他插件的路径 |

### 如何找到插件目录？

**方法 1：通过 Lightroom 查看**
1. 文件 → 增效工具管理器
2. 选择任意已安装的插件
3. 点击"在 Finder 中显示"
4. 这就是插件目录

**方法 2：通过 Finder**
1. 打开 Finder
2. 按 `Command + Shift + G`
3. 输入：`~/Library/Application Support/Adobe/`
4. 查找 Lightroom 相关文件夹

**方法 3：终端命令**
```bash
# 查找所有 Lightroom 插件目录
find ~/Library -name "*.lrplugin" -type d 2>/dev/null | \
  xargs -I {} dirname {} | sort -u
```

---

## ✅ 验证安装

### 验证主程序

1. **启动慧眼识鸟**
2. **检查版本**：标题栏应显示 "慧眼识鸟 v3.1.0"
3. **检查 API 状态**：窗口底部应显示：
   ```
   ✅ API 已启动 | 默认地区: XX | eBird筛选: 启用
   ```

### 验证 Lightroom 插件

1. **在 Lightroom 中选择一张鸟类照片**

2. **导出识别**：
   - 右键照片 → **导出** → **SuperBirdID**
   - 或：文件 → 导出（选择 SuperBirdID 预设）

3. **检查识别结果**：
   - 应弹出识别结果对话框
   - 显示鸟种名称、置信度、GPS 信息等

4. **对比 GUI 结果**：
   - 将同一张照片拖到慧眼识鸟 GUI
   - 两者结果应**完全一致**

---

## ⚙️ 配置 Lightroom 插件

### 插件设置（推荐配置）

在 Lightroom 导出对话框中：

| 设置项 | 推荐值 | 说明 |
|-------|-------|-----|
| **API 地址** | `http://127.0.0.1:5156` | 默认本地 API |
| **返回结果数** | `3` | 显示前 3 个匹配 |
| **启用 YOLO 检测** | ✅ | 自动裁剪鸟类区域 |
| **启用 GPS 定位** | ✅ | 使用照片 GPS 信息 |
| **自动写入 EXIF** | ✅ | 识别结果写入照片 |

### 工作流程

```
选择照片 → 导出 → SuperBirdID
    ↓
检查 API 是否启动（慧眼识鸟 GUI 必须运行）
    ↓
自动识别并应用地理筛选
    ↓
显示结果（只显示当地可能出现的鸟类）
    ↓
确认保存 → 写入 EXIF → 完成
```

---

## 🐛 常见问题

### Q1: Lightroom 提示"无法连接到 API"

**原因**：慧眼识鸟主程序未启动

**解决**：
1. 启动 **慧眼识鸟.app**
2. 确认窗口底部显示"✅ API 已启动"
3. 重试 Lightroom 识别

---

### Q2: 插件安装后 Lightroom 看不到

**原因**：
- 插件未正确安装到 Modules 目录
- Lightroom 未重启
- 插件被禁用

**解决**：
1. 检查插件路径（见上文"插件常见安装路径"）
2. 重启 Lightroom Classic
3. 文件 → 增效工具管理器 → 确认插件已启用

---

### Q3: 识别结果与 GUI 不一致

**原因**：可能是旧版本插件或 API

**解决**：
1. **确认版本**：
   - GUI 标题栏：v3.1.0
   - API 健康检查：`curl http://127.0.0.1:5156/health`

2. **重装插件**：
   - 完全删除旧插件
   - 重新从 DMG 安装

3. **重置配置**：
   - 删除 `~/Documents/SuperBirdID_File/gui_settings.json`
   - 重新在 GUI 中设置国家/地区

---

### Q4: DMG 打开后提示文件损坏

**原因**：macOS Gatekeeper 安全检查

**解决**：
```bash
# 移除隔离属性
xattr -rc /path/to/SuperBirdID-v3.1.0.dmg

# 或允许任意来源（系统偏好设置）
sudo spctl --master-disable
```

---

### Q5: 如何卸载？

**卸载主程序**：
```bash
sudo rm -rf /Applications/慧眼识鸟.app
sudo rm -rf /Applications/SuperBirdID.app
```

**卸载插件**：
1. Lightroom → 增效工具管理器 → 移除
2. 或手动删除：
   ```bash
   rm -rf ~/Library/Application\ Support/Adobe/Lightroom/Modules/SuperBirdIDPlugin.lrplugin
   ```

**清理配置**（可选）：
```bash
rm -rf ~/Documents/SuperBirdID_File
```

---

## 📞 技术支持

### 安装问题

如遇到安装问题，请提供：
1. macOS 版本
2. Lightroom 版本
3. 错误截图或日志
4. 插件目录路径

### 联系方式

- GitHub Issues: [SuperBirdID/issues](https://github.com/yourusername/SuperBirdID/issues)
- 邮件: support@example.com（如果有）

---

## 🎯 安装成功标志

安装成功后，您应该能够：

- [x] 启动慧眼识鸟 GUI，看到 v3.1.0 版本号
- [x] API 状态显示"已启动"，显示默认地区
- [x] 在 Lightroom 导出菜单看到 SuperBirdID 选项
- [x] 识别照片时，结果与 GUI 一致
- [x] 有 GPS 的照片显示精确位置筛选
- [x] 无 GPS 的照片使用配置的国家筛选

---

## 📚 延伸阅读

- **完整发布说明**: `RELEASE_NOTES_v3.1.0.md`
- **升级指南**: `UPGRADE_GUIDE_v3.1.0.md`（如果从旧版本升级）
- **使用说明**: `使用说明.md`
- **FAQ**: 项目 Wiki

---

**版本**: v3.1.0
**更新日期**: 2025-01-XX
**支持平台**: macOS 10.15+
**Lightroom**: Classic CC 2015+

---

祝您使用愉快！🐦

如有问题，欢迎反馈。我们会持续改进。
