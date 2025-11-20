# v3.1.0 发布检查清单

## 📋 发布前准备

### 代码更新
- [x] GUI 更新配置保存逻辑（添加 country_code, region_code）
- [x] API 添加读取配置文件功能
- [x] API 实现三级地理筛选
- [x] 更新版本号到 v3.1.0
  - [x] SuperBirdID_GUI.py
  - [x] SuperBirdID_API.py
  - [x] SuperBirdId.py

### 文档准备
- [x] 完整发布说明（RELEASE_NOTES_v3.1.0.md）
- [x] 快速升级指南（UPGRADE_GUIDE_v3.1.0.md）
- [ ] 更新 README.md（如果需要）

---

## 🧪 测试清单

### GUI 程序测试

#### 基础功能
- [ ] 程序启动正常
- [ ] 版本号显示为 v3.1.0
- [ ] 首次启动时选择国家/地区
- [ ] 配置文件正确生成（包含 country_code）

#### 识别功能
- [ ] **有 GPS 照片**：
  - [ ] 提取 GPS 信息
  - [ ] 显示"GPS 25km (xxx 种)"
  - [ ] 识别结果只包含当地鸟类

- [ ] **无 GPS 照片**：
  - [ ] 使用配置文件的 country_code
  - [ ] 显示"配置国家 XX (xxx 种)"
  - [ ] 识别结果只包含该国鸟类

#### 配置保存/读取
- [ ] 更改国家设置后自动保存
- [ ] 重启程序后配置保持
- [ ] gui_settings.json 包含所有必需字段：
  ```json
  {
    "use_yolo": true,
    "use_gps": true,
    "use_ebird": true,
    "selected_country": "...",
    "selected_region": "...",
    "country_code": "XX",
    "region_code": null,
    "temperature": 0.6
  }
  ```

---

### API 服务器测试

#### 启动测试
- [ ] API 正常启动
- [ ] 读取配置文件成功
- [ ] 控制台显示：
  ```
  📖 读取用户配置...
  ✓ 默认地区: XX
  ✓ eBird筛选: 启用
  ```

#### 识别测试（通过 API）
- [ ] **/health** 端点正常响应
- [ ] **/recognize** 端点（有 GPS 照片）：
  - [ ] 返回 `filter_source: "GPS 25km (xxx 种)"`
  - [ ] 结果包含 `ebird_match: true`

- [ ] **/recognize** 端点（无 GPS 照片）：
  - [ ] 返回 `filter_source: "配置国家 XX (xxx 种)"`
  - [ ] 结果被正确筛选

#### 错误处理
- [ ] 所有结果被过滤时返回警告
- [ ] 配置文件缺失时使用全球模式
- [ ] eBird 数据加载失败时回退正常

---

### Lightroom 插件测试

#### 安装测试
- [ ] 插件正确安装
- [ ] Lightroom 识别到插件
- [ ] 插件版本显示正确

#### 识别测试
- [ ] **有 GPS 照片**：
  - [ ] 识别成功
  - [ ] 结果与 GUI 一致
  - [ ] 只显示当地鸟类

- [ ] **无 GPS 照片**：
  - [ ] 识别成功
  - [ ] 使用配置的国家筛选
  - [ ] 结果与 GUI 一致

#### EXIF 写入
- [ ] 成功写入鸟种名称到 Title
- [ ] 写入后 Lightroom 可见更改
- [ ] 支持 JPEG 和 RAW 格式

---

## 📦 打包清单

### macOS App (.dmg)

#### 构建前检查
- [ ] 清理旧的构建文件
- [ ] 检查依赖完整性
- [ ] 验证代码签名证书

#### 打包内容
- [ ] SuperBirdID.app（或慧眼识鸟.app）
- [ ] 模型文件（birdid2024.pt.enc）
- [ ] 鸟类信息（birdinfo.json）
- [ ] 数据库（bird_reference.sqlite）
- [ ] YOLO 模型（yolo11l.pt）
- [ ] ExifTool bundle
- [ ] 离线 eBird 数据

#### DMG 创建
- [ ] 创建 DMG 镜像
- [ ] 包含"应用程序"文件夹快捷方式
- [ ] 设置背景图片（如果有）
- [ ] 代码签名和公证

#### 验证
- [ ] 在干净的 macOS 系统上测试安装
- [ ] 首次启动通过 Gatekeeper
- [ ] 所有功能正常工作

---

### Lightroom 插件 (.lrplugin)

#### 打包内容
- [ ] Info.lua
- [ ] PluginInit.lua
- [ ] SuperBirdIDExportServiceProvider.lua

#### 压缩
- [ ] 创建 .zip 文件
- [ ] 命名：SuperBirdIDPlugin-v3.1.0.lrplugin.zip
- [ ] 验证解压后文件夹名称正确

#### 验证
- [ ] 在 Lightroom 中安装测试
- [ ] 插件正常工作
- [ ] 与 v3.1.0 API 兼容

---

## 🌐 发布清单

### GitHub Release

- [ ] 创建新的 Release Tag: `v3.1.0`
- [ ] 发布标题："v3.1.0 - 智能地理筛选统一"
- [ ] 发布说明（复制 RELEASE_NOTES_v3.1.0.md）
- [ ] 上传文件：
  - [ ] 慧眼识鸟-v3.1.0.dmg
  - [ ] SuperBirdIDPlugin-v3.1.0.lrplugin.zip
  - [ ] UPGRADE_GUIDE_v3.1.0.md
- [ ] 标记为"Pre-release"（测试期）或"Latest release"

### 更新文档

- [ ] 更新主 README.md（版本号、功能列表）
- [ ] 更新安装文档
- [ ] 更新 Wiki（如果有）

### 通知用户

- [ ] GitHub Release 公告
- [ ] 发送通知给测试用户
- [ ] 更新项目主页（如果有）

---

## 🐛 已知问题记录

### 需要在发布说明中提及

1. **配置文件兼容性**
   - 旧配置文件缺少新字段
   - 需要重新选择国家

2. **API 需要重启**
   - GUI 更改配置后 API 需重启
   - 已在文档中说明解决方法

3. **首次安装提示**
   - "未设置默认地区"是正常的
   - 需要在 GUI 中设置一次

---

## ✅ 最终验证

### 安装测试（模拟用户操作）

1. **全新安装**：
   - [ ] 在没有旧版本的 Mac 上安装
   - [ ] 按照 UPGRADE_GUIDE 步骤操作
   - [ ] 验证所有功能正常

2. **升级安装**：
   - [ ] 从 v3.0.2 升级到 v3.1.0
   - [ ] 验证配置迁移
   - [ ] 验证功能改进

3. **Lightroom 集成**：
   - [ ] 完整的 Lightroom 工作流测试
   - [ ] 批量识别测试
   - [ ] EXIF 写入测试

---

## 📊 发布后监控

### 第一周

- [ ] 监控 GitHub Issues
- [ ] 收集用户反馈
- [ ] 准备 Hotfix（如有严重 Bug）

### 第一个月

- [ ] 收集使用数据（如有遥测）
- [ ] 评估升级率
- [ ] 规划下一版本

---

## 🎯 成功标准

- [ ] 至少 90% 的测试用户成功升级
- [ ] Lightroom 插件识别准确度与 GUI 一致
- [ ] 没有严重 Bug 报告
- [ ] 用户反馈积极

---

**版本**: v3.1.0
**目标发布日期**: TBD
**检查清单最后更新**: 2025-01-XX

---

## 📝 备注

### 测试环境

- macOS: 10.15, 11.0, 12.0, 13.0, 14.0
- Lightroom: Classic CC 2015+, Classic CC 2024
- Python: 3.9+ (如果用户自行运行)

### 回滚计划

如果发布后出现严重问题：
1. 立即在 GitHub 标记为"Pre-release"
2. 发布紧急通知
3. 提供 v3.0.2 下载链接
4. 修复 Bug 并发布 v3.1.1

---

**准备好发布了吗？**

在所有复选框都勾选之前，请不要发布！✋
