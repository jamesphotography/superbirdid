# SuperBirdID 网站部署指南

## 前提条件

1. GitHub 账户已经准备好
2. 域名 `superbirdid.jamesphotography.com.au` 已经绑定

## 部署步骤

### 1. 准备 GitHub 仓库

如果还没有创建仓库,需要先创建:

```bash
# 在 GitHub 上创建一个新仓库,例如: jamesphotography/SuperBirdID
```

### 2. 推送网站代码到 GitHub

```bash
cd /Users/jameszhenyu/Documents/Development/SuperBirdID

# 如果还没有初始化 git
git init

# 添加远程仓库
git remote add origin https://github.com/jamesphotography/SuperBirdID.git

# 或者如果已经有仓库,确保 pages 目录被跟踪
git add pages/
git commit -m "Add website files for GitHub Pages"
git push origin master
```

### 3. 配置 GitHub Pages

1. 进入 GitHub 仓库: https://github.com/jamesphotography/SuperBirdID
2. 点击 **Settings** (设置)
3. 在左侧菜单找到 **Pages**
4. 在 "Build and deployment" 部分:
   - Source: 选择 **GitHub Actions**
   - 这样会使用 `.github/workflows/jekyll.yml` 配置的自动部署

### 4. 配置自定义域名

在 GitHub Pages 设置页面:

1. 在 "Custom domain" 字段输入: `superbirdid.jamesphotography.com.au`
2. 点击 **Save**
3. 等待 DNS 检查完成
4. 启用 **Enforce HTTPS**

### 5. DNS 配置

在您的域名提供商(例如 Cloudflare, GoDaddy 等)添加以下 DNS 记录:

#### 方案 A: 使用 CNAME (推荐)

```
Type: CNAME
Name: superbirdid
Value: jamesphotography.github.io
TTL: Auto
```

#### 方案 B: 使用 A 记录

```
Type: A
Name: superbirdid
Value: 185.199.108.153
TTL: Auto

Type: A
Name: superbirdid
Value: 185.199.109.153
TTL: Auto

Type: A
Name: superbirdid
Value: 185.199.110.153
TTL: Auto

Type: A
Name: superbirdid
Value: 185.199.111.153
TTL: Auto
```

### 6. 验证部署

1. 等待 GitHub Actions 完成构建(约 2-5 分钟)
2. 访问 https://superbirdid.jamesphotography.com.au
3. 检查网站是否正常显示

### 7. 监控部署状态

#### 查看 GitHub Actions

1. 进入仓库的 **Actions** 标签
2. 查看最新的 workflow 运行状态
3. 如果构建失败,点击查看详细日志

#### 常见问题

**问题 1: 404 错误**
- 确认 GitHub Pages 已启用
- 确认 `CNAME` 文件存在于 `pages/` 目录
- 等待 DNS 传播(可能需要几分钟到几小时)

**问题 2: HTTPS 证书错误**
- 等待 GitHub 自动配置 Let's Encrypt 证书(可能需要几分钟)
- 确认域名 DNS 记录正确

**问题 3: 样式未加载**
- 检查 `_config.yml` 中的 `baseurl` 设置(应该为空字符串 `""`)
- 清除浏览器缓存

## 自动部署

每次推送到 `master` 或 `main` 分支时,GitHub Actions 会自动:

1. 检出代码
2. 安装 Ruby 和依赖
3. 构建 Jekyll 网站
4. 部署到 GitHub Pages

整个过程约 2-5 分钟。

## 更新网站

### 更新内容

```bash
cd /Users/jameszhenyu/Documents/Development/SuperBirdID/pages

# 编辑文件
# 例如: vim index.md

# 提交更改
git add .
git commit -m "Update website content"
git push origin master
```

### 更新版本信息

当发布新版本时,需要更新:

1. `index.md` - 首页版本号
2. `download.md` - 下载链接、SHA256、版本号
3. `_config.yml` - 描述信息

## 本地测试

在推送前建议本地测试:

```bash
cd pages/

# 安装依赖(首次)
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000
```

## 维护建议

1. **定期更新依赖**
   ```bash
   bundle update
   ```

2. **监控网站性能**
   - 使用 Google Analytics (如需要)
   - 监控 GitHub Actions 运行状态

3. **备份内容**
   - 定期备份 `pages/` 目录
   - 保持 Git 历史记录

## 技术支持

如有问题,请:
1. 查看 GitHub Actions 日志
2. 检查 GitHub Pages 文档: https://docs.github.com/en/pages
3. 提交 Issue: https://github.com/jamesphotography/SuperBirdID/issues

## 完成！

网站现在应该可以通过 https://superbirdid.jamesphotography.com.au 访问了。
