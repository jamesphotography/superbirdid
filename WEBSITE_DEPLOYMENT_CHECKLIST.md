# SuperBirdID 网站部署检查清单

## ✅ 已完成

- [x] 更新网站内容到 v3.2.1
- [x] 配置自定义域名文件 (CNAME)
- [x] 添加 GitHub Actions 自动部署
- [x] 提交代码到 Git
- [x] 推送到 GitHub (commit: 53556b1)

**推送时间**: 刚刚完成
**提交信息**: feat: 更新官方网站到 v3.2.1

---

## 🔧 待配置 (需要在 GitHub 网页操作)

### 1. 配置 GitHub Pages

**步骤**:
1. 访问: https://github.com/jamesphotography/superbirdid/settings/pages
2. 在 "Build and deployment" 部分:
   - **Source**: 选择 **GitHub Actions** (不是 Deploy from a branch)
   - 这样会使用我们创建的 `.github/workflows/jekyll.yml`
3. 在 "Custom domain" 部分:
   - 输入: `superbirdid.jamesphotography.com.au`
   - 点击 **Save**
   - 等待 DNS 检查 (通常 1-2 分钟)
4. DNS 检查通过后:
   - 勾选 ✅ **Enforce HTTPS**
   - GitHub 会自动配置 Let's Encrypt 证书

**注意**: 首次配置 HTTPS 可能需要 5-10 分钟

---

### 2. 验证 DNS 配置

**检查你的域名提供商** (例如 Cloudflare, GoDaddy, etc.)

**推荐配置** (CNAME 记录):
```
Type:  CNAME
Name:  superbirdid
Value: jamesphotography.github.io
TTL:   Auto (或 3600)
```

**或者使用 A 记录**:
```
Type:  A
Name:  superbirdid
Value: 185.199.108.153
       185.199.109.153
       185.199.110.153
       185.199.111.153
```

**验证 DNS**:
```bash
# 在终端运行
dig superbirdid.jamesphotography.com.au

# 或者
nslookup superbirdid.jamesphotography.com.au
```

---

## 📊 部署监控

### GitHub Actions

**查看构建状态**:
1. 访问: https://github.com/jamesphotography/superbirdid/actions
2. 查看 "Deploy Jekyll site to Pages" workflow
3. 最新的运行应该会在几分钟内出现

**预期流程**:
```
1. 推送代码 ✅ (已完成)
   ↓
2. GitHub Actions 触发 (自动)
   ↓
3. 构建 Jekyll 网站 (约 1-2 分钟)
   ↓
4. 部署到 GitHub Pages (约 1-2 分钟)
   ↓
5. 网站上线 ✨
```

**总时间**: 约 2-5 分钟

---

## 🌐 验证网站上线

### 等待部署完成后:

1. **访问网站**: https://superbirdid.jamesphotography.com.au
2. **检查页面**:
   - [ ] 首页加载正常
   - [ ] 显示 v3.2.1 版本信息
   - [ ] 功能页面 (/features/) 正常
   - [ ] 下载页面 (/download/) 正常
   - [ ] 图片和样式加载正常
   - [ ] HTTPS 证书有效 (浏览器地址栏显示锁图标)

3. **测试链接**:
   - [ ] 导航菜单正常工作
   - [ ] 下载按钮链接正确
   - [ ] GitHub 链接有效

---

## 🐛 故障排查

### 问题 1: 网站显示 404

**可能原因**:
- GitHub Pages 未启用
- Source 未设置为 "GitHub Actions"
- GitHub Actions 构建失败

**解决方法**:
1. 检查 GitHub Pages 设置
2. 查看 Actions 标签页的构建日志
3. 确认 `pages/CNAME` 文件存在

### 问题 2: 自定义域名不工作

**可能原因**:
- DNS 记录未配置或未生效
- GitHub Pages 中未设置 Custom domain
- DNS 传播延迟

**解决方法**:
1. 验证 DNS 记录: `dig superbirdid.jamesphotography.com.au`
2. 等待 DNS 传播 (可能需要几分钟到几小时)
3. 确认 Custom domain 已保存

### 问题 3: HTTPS 证书错误

**可能原因**:
- 证书还在配置中
- DNS 记录不正确

**解决方法**:
1. 等待 5-10 分钟让 GitHub 配置证书
2. 确认 DNS 记录指向正确
3. 在 GitHub Pages 设置中重新保存 Custom domain

### 问题 4: 样式未加载

**可能原因**:
- baseurl 配置错误
- 资源路径错误

**解决方法**:
1. 检查 `_config.yml` 中 `baseurl: ""` (应该为空字符串)
2. 清除浏览器缓存
3. 查看浏览器控制台错误信息

---

## 📱 测试清单

部署成功后,建议测试:

### 桌面浏览器
- [ ] Chrome
- [ ] Safari
- [ ] Firefox
- [ ] Edge

### 移动设备
- [ ] iOS Safari
- [ ] Android Chrome

### 功能测试
- [ ] 页面加载速度
- [ ] 响应式布局
- [ ] 图片显示
- [ ] 链接跳转
- [ ] 下载链接

---

## 📈 后续维护

### 更新网站内容

```bash
cd /Users/jameszhenyu/Documents/Development/SuperBirdID/pages

# 编辑文件
vim index.md  # 或使用其他编辑器

# 提交
git add .
git commit -m "Update website content"
git push origin master

# 等待 2-5 分钟自动部署
```

### 本地预览

```bash
cd pages/
bundle exec jekyll serve
# 访问 http://localhost:4000
```

### 监控

定期检查:
- GitHub Actions 运行状态
- 网站访问速度
- HTTPS 证书有效期 (GitHub 自动续期)

---

## 🎉 完成标志

当以下全部完成,网站就上线了:

- [x] 代码推送到 GitHub
- [ ] GitHub Pages 配置完成
- [ ] DNS 记录正确
- [ ] GitHub Actions 构建成功
- [ ] 网站可以访问
- [ ] HTTPS 证书有效

---

## 📞 需要帮助?

- **GitHub Pages 文档**: https://docs.github.com/en/pages
- **Jekyll 文档**: https://jekyllrb.com/docs/
- **GitHub Actions 文档**: https://docs.github.com/en/actions

**查看详细部署指南**: `pages/DEPLOYMENT_GUIDE.md`

---

**当前状态**: 代码已推送,等待 GitHub Pages 配置 ⏳
