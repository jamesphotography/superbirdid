---
layout: single
title: 下载
permalink: /download/
---

<style>
  .download-section {
    text-align: center;
    padding: 2rem 1rem;
  }
  .os-block {
    border: 1px solid #e9ecef;
    border-radius: 0.5rem;
    padding: 2rem;
    margin-bottom: 2rem;
    background-color: #f8f9fa;
  }
  .os-block h2 {
    margin-top: 0;
  }
  .download-btn {
    display: inline-block;
    background-color: #28a745;
    color: white !important;
    padding: 0.8rem 1.8rem;
    font-size: 1.2rem;
    font-weight: bold;
    text-decoration: none;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
  }
  .download-btn:hover {
    background-color: #218838;
  }
  .version-info {
    color: #6c757d;
    margin-bottom: 1rem;
  }
  .checksum {
    font-family: monospace;
    background-color: #e9ecef;
    padding: 1rem;
    border-radius: 0.3rem;
    word-wrap: break-word;
    text-align: left;
  }
  .features-list {
    text-align: left;
    max-width: 600px;
    margin: 1rem auto;
  }
</style>

<div class="download-section">
  <h1>下载 慧眼识鸟-SuperBirdID</h1>
  <p style="font-size: 1.1rem; color: #555;">选择适合您操作系统的版本</p>

  <div class="os-block">
    <h2><i class="fab fa-apple"></i> macOS 版本</h2>
    <p class="version-info"><strong>最新版本: v3.2.1</strong> | 发布日期: 2025-10-23</p>

    <a href="https://github.com/jamesphotography/SuperBirdID/releases/download/v3.2.1/SuperBirdID-v3.2.1.dmg" class="download-btn" target="_blank">
      <i class="fas fa-download"></i> 下载 v3.2.1 for macOS (319 MB)
    </a>

    <div class="features-list">
      <h3>系统要求</h3>
      <ul>
        <li>macOS 10.15 (Catalina) 或更高版本</li>
        <li>建议 8GB 以上内存</li>
        <li>约 500MB 可用磁盘空间</li>
        <li>支持 Apple Silicon (M1/M2/M3) 和 Intel 处理器</li>
      </ul>

      <h3>v3.2.1 新功能</h3>
      <ul>
        <li>✨ 国家列表按鸟种数量智能排序</li>
        <li>📊 51个国家显示详细鸟种统计</li>
        <li>🌍 GPS 地理定位精确化</li>
        <li>🔒 完全离线运行,保护隐私</li>
      </ul>
    </div>

    <details style="margin-top: 1rem;">
      <summary style="cursor: pointer; color: #007bff;">显示 SHA256 校验码</summary>
      <div class="checksum">
        <strong>SuperBirdID-v3.2.1.dmg</strong><br>
        <code>dfa9689b5039b16647c9d1d853253affdd205b4f50c75437bba34b754f1d95a7</code>
      </div>
    </details>

    <details style="margin-top: 1rem;">
      <summary style="cursor: pointer; color: #007bff;">安装说明</summary>
      <div style="text-align: left; max-width: 600px; margin: 1rem auto; padding: 1rem; background-color: white; border-radius: 0.3rem;">
        <ol>
          <li>下载 <code>SuperBirdID-v3.2.1.dmg</code> 文件</li>
          <li>双击打开 DMG 文件</li>
          <li>将 <code>SuperBirdID.app</code> 拖拽到 <code>Applications</code> 文件夹</li>
          <li>首次运行时,如果系统提示"无法打开",请:
            <ul>
              <li>打开 <strong>系统偏好设置</strong> → <strong>安全性与隐私</strong></li>
              <li>点击 <strong>"仍要打开"</strong> 按钮</li>
            </ul>
          </li>
          <li>（可选）安装 Lightroom 插件:
            <ul>
              <li>从 DMG 中将 <code>SuperBirdID.lrplugin</code> 复制到 <code>~/Library/Application Support/Adobe/Lightroom/Modules/</code></li>
              <li>重启 Lightroom Classic</li>
            </ul>
          </li>
        </ol>
      </div>
    </details>
  </div>

  <div style="margin-top: 3rem; padding: 2rem; background-color: #e7f3ff; border-radius: 0.5rem;">
    <h3>版本历史</h3>
    <p>查看完整的版本历史和更新日志,请访问 <a href="https://github.com/jamesphotography/SuperBirdID/releases" target="_blank">GitHub Releases</a></p>
  </div>

  <div style="margin-top: 2rem;">
    <h3>需要帮助?</h3>
    <p>如有任何问题,请访问 <a href="/help/">帮助页面</a> 或在 <a href="https://github.com/jamesphotography/SuperBirdID/issues" target="_blank">GitHub Issues</a> 提交问题。</p>
  </div>
</div>
