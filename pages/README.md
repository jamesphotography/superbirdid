# SuperBirdID 官方网站

这是慧眼识鸟-SuperBirdID 的官方网站源码,使用 Jekyll 和 GitHub Pages 构建。

## 网站地址

- **自定义域名**: https://superbirdid.jamesphotography.com.au
- **GitHub Pages**: (自动重定向到自定义域名)

## 本地开发

### 安装依赖

```bash
bundle install
```

### 本地预览

```bash
bundle exec jekyll serve
```

然后访问 http://localhost:4000

### 构建网站

```bash
bundle exec jekyll build
```

生成的文件将在 `_site` 目录中。

## 部署

网站会在推送到 `main` 或 `master` 分支时自动部署到 GitHub Pages。

### 部署流程

1. 推送代码到 GitHub
2. GitHub Actions 自动触发构建
3. 网站自动部署到 https://superbirdid.jamesphotography.com.au

## 网站结构

```
pages/
├── _config.yml           # Jekyll 配置文件
├── CNAME                 # 自定义域名配置
├── index.md              # 首页
├── features.md           # 功能详解页面
├── download.md           # 下载页面
├── help.md               # 帮助页面
├── aboutme.md            # 关于页面
├── images/               # 图片资源
│   ├── 主页背景图.png
│   ├── 作者头像.png
│   └── 社交分享图.png
├── icon.png              # 应用图标
├── favicon.png           # 网站图标
└── .github/
    └── workflows/
        └── jekyll.yml    # GitHub Actions 自动部署配置
```

## 自定义域名配置

域名 `superbirdid.jamesphotography.com.au` 已经配置好了。

### DNS 设置

确保在您的 DNS 提供商处设置了以下记录:

```
CNAME  superbirdid  jamesphotography.github.io
```

或者使用 A 记录:

```
A      superbirdid  185.199.108.153
A      superbirdid  185.199.109.153
A      superbirdid  185.199.110.153
A      superbirdid  185.199.111.153
```

### GitHub 设置

1. 在 GitHub 仓库设置中,进入 "Pages" 部分
2. "Custom domain" 字段应该显示: `superbirdid.jamesphotography.com.au`
3. 确保 "Enforce HTTPS" 已启用

## 更新内容

### 更新版本号

编辑以下文件来更新版本信息:
- `index.md` - 首页的版本号和下载链接
- `download.md` - 下载页面的版本号、发布日期和 SHA256
- `_config.yml` - 网站描述中的鸟类数量

### 添加新页面

1. 在 `pages/` 目录创建新的 `.md` 文件
2. 添加 Front Matter:
   ```yaml
   ---
   layout: single
   title: 页面标题
   permalink: /your-page/
   ---
   ```
3. 编写内容

## 主题

网站使用 [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) Jekyll 主题。

## 许可证

网站内容版权归 SuperBirdID 项目所有。

## 联系方式

- GitHub: https://github.com/jamesphotography/SuperBirdID
- Email: james@jamesphotography.com.au
