---
layout: splash
permalink: / 
title: 首页
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/主页背景图.png
  actions:
    - label: "下载 v1.0.1"
      url: "/download/"
---

<style>
  .hero {
    text-align: center;
    padding: 4rem 2rem;
    background-color: #f8f9fa;
    border-bottom: 1px solid #e9ecef;
  }
  .hero h1 {
    font-size: 3rem;
    font-weight: 700;
  }
  .hero p {
    font-size: 1.25rem;
    color: #6c757d;
  }
  .hero .btn {
    font-size: 1.25rem;
    padding: 0.75rem 1.5rem;
    margin-top: 1rem;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 0.3rem;
  }
  .features {
    padding: 4rem 2rem;
    text-align: center;
  }
  .features .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
  }
  .feature-item h3 {
    font-size: 1.5rem;
  }
</style>

<div class="hero">
  <h1>慧眼识鸟-SuperBirdID</h1>
  <p>您的桌面端 AI 鸟类识别专家</p>
  <p><img src="/icon.png" alt="SuperBirdID Icon" width="128"/></p>
  <a href="{{ '/download/' | relative_url }}" class="btn">查看下载</a>
</div>

<div style="text-align: center; padding: 4rem 2rem; background-color: #f8f9fa;">
  <h2 style="border-bottom: 1px solid #e0e0e0; padding-bottom: 0.5rem; display: inline-block;">关于 慧眼识鸟-SuperBirdID</h2>
  <p style="max-width: 800px; margin: 1rem auto; font-size: 1.1rem; color: #555;">
    <strong>慧眼识鸟-SuperBirdID</strong> 是一款为鸟类爱好者、生态摄影师和自然观察者量身打造的专业桌面应用。我们的使命是提供一个强大、快速、尊重用户隐私的鸟类识别工具。不同于依赖云端计算的手机App，它将先进的AI模型直接部署在您的电脑上，实现完全离线使用，充分保护您的隐私。
  </p>
</div>

<div class="features">
  <h2>核心功能</h2>
  <div class="feature-grid">
    <div class="feature-item">
      <h3>🤖 AI 智能识别</h3>
      <p>覆盖全球超过 10,965 种鸟类，无需联网，在您的 Mac 上即可完成高精度识别。</p>
    </div>
    <div class="feature-item">
      <h3>📸 RAW 格式全面支持</h3>
      <p>原生处理各大相机品牌的 RAW 文件 (NEF, CR3, ARW)，无需转换，保留最佳画质。</p>
    </div>
    <div class="feature-item">
      <h3>🌍 GPS 智能定位</h3>
      <p>自动读取照片 GPS 数据，结合 eBird 记录，智能筛选区域物种，大幅提升准确率。</p>
    </div>
    <div class="feature-item">
      <h3>🎨 Lightroom 无缝集成</h3>
      <p>提供 Lightroom Classic 插件，将鸟类识别无缝融入您的摄影工作流。</p>
    </div>
  </div>
</div>
