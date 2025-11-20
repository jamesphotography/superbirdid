# 慧眼识鸟 v3.1.0 发布说明

## 🎉 重要更新：智能地理筛选统一

这是一个**重要功能更新**，解决了 Lightroom 插件和 GUI 程序识别结果不一致的问题。

---

## ⚠️ 重要：必须完全重新安装

由于配置文件格式和 API 逻辑的重大改进，**强烈建议**：

1. ✅ **卸载旧版本** SuperBirdID 程序
2. ✅ **删除并重装** Lightroom 插件
3. ✅ **安装新版本** SuperBirdID v3.1.0
4. ✅ **重新配置** 国家/地区设置

---

## 🆕 新增功能

### 1. 智能地理筛选（API 自动化）

**问题描述**：
- 之前：Lightroom 插件的识别结果和 GUI 界面不一致
- 原因：插件没有使用 eBird 地理筛选

**解决方案**：
- API 现在**自动应用** eBird 地理筛选
- Lightroom 插件无需修改，自动享受筛选功能
- GUI 和插件现在使用**完全相同**的识别逻辑

### 2. 三级地理筛选优先级

```
📍 优先级 1: GPS 精确位置（25km 范围）
   ↓ 如果照片无 GPS 或获取失败
🌍 优先级 2: 用户最后设置的国家/地区
   ↓ 如果用户未设置
🌍 优先级 3: GPS 推断的国家（如果有 GPS）
   ↓ 如果以上都失败
🌐 优先级 4: 全球模式（无筛选）
```

**实际效果**：
- ✅ 有 GPS 的照片 → 使用拍摄地 25km 范围内的鸟类列表
- ✅ 无 GPS 的照片 → 使用您在 GUI 中设置的国家/地区
- ✅ Lightroom 插件 → 自动应用上述逻辑

### 3. 配置文件记忆功能增强

**新增字段**：
```json
{
  "selected_country": "澳大利亚 (Australia)",  // 显示名称
  "selected_region": "整个国家",
  "country_code": "AU",      // ✨ 新增：供 API 使用
  "region_code": null,       // ✨ 新增：区域代码
  "use_ebird": true
}
```

**好处**：
- GUI 记住您的选择
- API 读取您的偏好
- 无需每次重新设置

---

## 🔧 技术改进

### GUI 程序 (SuperBirdID_GUI.py)
- ✅ 保存国家代码（如 "AU"）到配置文件
- ✅ 保存区域代码（如 "AU-SA"）支持更精确筛选
- ✅ 自动从显示名称提取代码

### API 服务器 (SuperBirdID_API.py)
- ✅ 启动时自动读取 `gui_settings.json`
- ✅ `/recognize` 接口智能应用 eBird 筛选
- ✅ 返回筛选数据来源信息（`filter_source`）
- ✅ 当所有结果被过滤时返回警告

### Lightroom 插件 (SuperBirdIDPlugin.lrplugin)
- ✅ 无需修改，自动继承 API 的筛选功能

---

## 📊 识别结果对比

### 修复前：
| 方式 | GPS 筛选 | 国家筛选 | 结果 |
|------|---------|---------|------|
| GUI 界面 | ✅ 有 | ✅ 有 | 精确 |
| Lightroom 插件 | ❌ 无 | ❌ 无 | 不精确 |

### 修复后：
| 方式 | GPS 筛选 | 国家筛选 | 结果 |
|------|---------|---------|------|
| GUI 界面 | ✅ 有 | ✅ 有 | 精确 |
| Lightroom 插件 | ✅ 有 | ✅ 有 | **精确** ✨ |

---

## 🚀 安装步骤

### 1. 卸载旧版本

**macOS:**
```bash
# 删除旧版 SuperBirdID
sudo rm -rf /Applications/慧眼识鸟.app
sudo rm -rf /Applications/SuperBirdID.app

# 删除旧配置（可选，如需全新开始）
rm -rf ~/Documents/SuperBirdID_File
```

**Lightroom 插件:**
1. 打开 Lightroom → 文件 → 增效工具管理器
2. 找到 "SuperBirdID Plugin"
3. 点击"移除"
4. 删除插件文件夹：`~/Library/Application Support/Adobe/Lightroom/Modules/SuperBirdIDPlugin.lrplugin`

### 2. 安装新版本

**SuperBirdID 程序:**
1. 下载 `慧眼识鸟-v3.1.0.dmg`
2. 打开 DMG，拖动到"应用程序"文件夹
3. 首次启动时选择您的国家/地区

**Lightroom 插件:**
1. 下载 `SuperBirdIDPlugin-v3.1.0.lrplugin.zip`
2. 解压得到 `SuperBirdIDPlugin.lrplugin`
3. Lightroom → 文件 → 增效工具管理器 → 添加
4. 选择解压后的 `.lrplugin` 文件夹
5. 启用插件

### 3. 配置和验证

**配置 SuperBirdID:**
1. 启动 SuperBirdID GUI 程序
2. 点击"⚙️ 高级选项"
3. 在"国家/地区"下拉菜单中选择您的常用拍摄地区
4. 设置会**自动保存**

**配置 Lightroom 插件:**
1. 在 Lightroom 插件设置中：
   - ✅ 启用 YOLO 检测
   - ✅ 启用 GPS 定位
   - ✅ 自动写入 EXIF
   - API 地址：`http://127.0.0.1:5156`（默认）

**验证安装:**
1. 启动 SuperBirdID GUI（API 会自动启动）
2. 检查控制台输出：
   ```
   📖 读取用户配置...
   ✓ 默认地区: AU
   ✓ eBird筛选: 启用
   ```
3. 在 Lightroom 中选择一张照片 → 导出 → SuperBirdID 识别
4. 检查结果是否只显示您所在地区的鸟类

---

## 🐛 已知问题

### 配置文件兼容性
- 旧版配置文件（v3.0.2 及更早）缺少 `country_code` 和 `region_code` 字段
- 首次启动时会显示"未设置默认地区"
- **解决方案**：在 GUI 中重新选择一次国家/地区即可

### API 需要重启
- 如果在 GUI 中更改了国家/地区设置
- API 需要重启才能读取新配置
- **解决方案**：
  - 方式 1：关闭并重新打开 SuperBirdID GUI
  - 方式 2：在 GUI 中点击"停止 API" → "启动 API"

---

## 💡 使用建议

### 推荐工作流程

**场景 1: 在澳大利亚拍摄鸟类**
1. GUI 中设置国家为"澳大利亚"
2. 拍摄照片（建议开启相机 GPS）
3. 导入 Lightroom
4. 使用插件识别 → 自动筛选澳大利亚鸟类

**场景 2: 旅行到多个国家**
1. 到达新国家时，在 GUI 中切换国家设置
2. 之后的识别会自动使用新国家的鸟类列表
3. 有 GPS 的照片会优先使用精确位置（更准确）

**场景 3: 处理旧照片（无 GPS）**
1. GUI 中设置为照片拍摄的国家
2. 批量识别时，所有照片使用该国家的筛选
3. 结果更准确，减少误报

---

## 📞 技术支持

如遇到问题，请提供：
1. SuperBirdID 版本号（GUI 标题栏显示）
2. 配置文件内容（`gui_settings.json`）
3. API 控制台输出（显示筛选来源）
4. 照片是否包含 GPS 信息

GitHub Issues: [SuperBirdID Issues](https://github.com/yourusername/SuperBirdID/issues)

---

## 🙏 致谢

感谢所有用户的反馈，特别是关于 Lightroom 插件识别结果不一致的报告。这次更新就是为了解决这个问题！

---

**版本**: v3.1.0
**发布日期**: 2025-01-XX
**兼容性**: macOS 10.15+ / Lightroom Classic CC 2015+
**许可**: MIT License

---

## 📄 完整更新日志

### v3.1.0 (2025-01-XX)
**新增**:
- API 启动时自动读取 GUI 配置文件
- `/recognize` 接口三级地理筛选优先级
- 配置文件新增 `country_code` 和 `region_code` 字段
- API 响应新增 `filter_source` 字段显示筛选来源

**修复**:
- Lightroom 插件识别结果与 GUI 不一致的问题
- 无 GPS 照片无法应用地理筛选的问题

**改进**:
- GUI 配置保存逻辑优化
- eBird 筛选错误处理和降级机制

### v3.0.2 (Previous)
- GUI 界面优化
- 性能改进
